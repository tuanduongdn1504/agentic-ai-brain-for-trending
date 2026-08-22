# (C) qiaomu-anything-to-notebooklm — Deep Dive

> **v266 LLM Wiki** · built 2026-08-22 · routine v2.8
> Subject: `joeseesun/qiaomu-anything-to-notebooklm` — a Claude Code **skill** that turns arbitrary content into NotebookLM artifacts.
> **Verdict: GOAL-ALIGNED INCLUDE 3/4 · NO MINT · counts 46/12 UNCHANGED.**
> Every `path:line` below was read in the orchestrator's own command output. Every count was measured, not estimated. Where something was not established, it says so.

---

## 0. Source verification

Two independent clones of `https://github.com/joeseesun/qiaomu-anything-to-notebooklm`:

- Identical HEAD **`cea6ceee8cdcd01a573af5ae75c2d3cffc20650b`** — 2026-04-28 09:38 +0800, `joeseesun <85378058@qq.com>`, subject *"Update skill"*.
- `diff -rq --exclude=.git A B` clean in **both** directions.
- `git rev-list --count HEAD` = **11 commits**. `git rev-list --max-parents=0 HEAD` = **one root** (`bdaef0eb`, 2026-01-25 22:47). One branch (`main`). Two tags, **both dated 2026-01-25**: `v1.0.0`, `v1.0.1`.
- `git log --format="%an <%ae>"` — **all 11 commits by one author.** No merges.
- **20 tracked files, 4,680 lines.** No `.github/` on any ref; **no CI has ever existed.**
- `git ls-remote origin` shows PR refs **1, 3, 5** — see §7, which is the most important section in this document.

Size profile: `SKILL.md` 742 · `main.py` 509 · `README.md` 506 · `feishu-read-mcp/src/scraper.py` 469 · `feishu-read-mcp/src/parser.py` 401 · `scripts/fetch_url.sh` 380.

**Sandbox constraint (stated up front):** `python3` is SIGKILLed here (exit 137). **Nothing Python was executed.** Two bash experiments *were* executed and are labelled as such. Every Python-behaviour claim below is reasoned from source and marked.

---

## 1. What it is

A **Claude Code skill** (`SKILL.md` + helper scripts + one bundled MCP server), MIT, by a single author. You say *"把这篇文章生成播客"* ("turn this article into a podcast") and hand it a URL; the skill acquires the content, uploads it to **Google NotebookLM**, and asks NotebookLM to emit a podcast, slide deck, mind map, quiz, flashcards, report, infographic or video.

Its stated span is wide: WeChat public-account articles, arbitrary web pages, **300+ paywalled news sites**, X/Twitter threads, YouTube, Chinese podcast platforms (小宇宙 / 喜马拉雅 / B站), PDF, EPUB, Office, images (OCR), audio, ZIP, and bare search keywords.

It grew by accretion. The initial commit (2026-01-25) is *"Claude skill for WeChat to NotebookLM integration"*; the repo was renamed **twice** — `weixin-to-notebooklm` → `anything-to-notebooklm` → `qiaomu-anything-to-notebooklm` — and the name change is visible in the product: the founding WeChat capability is now one of eleven advertised sources.

**Author.** `joeseesun`, self-identified at `README.md:504` as **Joe**, with X `@vista8` and the WeChat public account 「向阳乔木推荐看」. `LICENSE:3` reads *"Copyright (c) 2026 Joe"*. **No Anthropic affiliation is declared anywhere in the repository** (grepped: README, SKILL.md, LICENSE, all commit messages).

Public-source research (fleet lens, URLs supplied) identifies him as **向阳乔木 / Xiangyang Qiaomu**, an independent AI product and content creator publishing at `qiaomu.ai`, and **explicitly finds no Anthropic affiliation** — he uses and reviews Anthropic's products as a practitioner. ⭐ He also maintains a **`qiaomu-*` skill line** — `qiaomu-ppt`, `qiaomu-seo`, `qiaomu-skill-publisher` — which reframes the second rename: `anything-to-notebooklm` → `qiaomu-anything-to-notebooklm` is **namespacing a personal skill portfolio**, not vanity, and it is a Pattern #19 ecosystem-portfolio signal. ⚠️ Follower and repository counts are **page-stated** (§37.4 extends to social metrics — not cited here); the "ex-ByteDance product manager" attribution is **third-party-sourced, not self-declared in-repo**; and I have **not read** the sibling repositories, so `qiaomu-skill-publisher` is named as a sibling only, not characterised.

---

## 2. ⭐⭐⭐ The finding that reframes the subject: its dependency spine is three prior corpus subjects

This did not come from the web. It came from grepping the vault.

| Dependency | Where it is invoked | Corpus identity |
|---|---|---|
| `notebooklm-py` | `install.sh:94` — `pip3 install git+https://github.com/teng-lin/notebooklm-py.git`; credited `README.md:492` | **corpus subject v7** (2026-04-18) |
| `markitdown` | `requirements.txt:8`; ~8 formats routed through it in `SKILL.md`; credited `README.md:489` | **corpus subject v28** (Microsoft) |
| `lark-cli` | `main.py:231` — `['lark-cli', 'docs', '+create', …]` | **corpus subject v143** (`larksuite/cli`) |

`lark-cli` is confirmed as v143's actual binary, not an inference: the v143 wiki quotes `lark-cli auth login --no-wait` at `03 Projects/larksuite-cli - Beginner Analysis/02 Wiki/index.md:24`.

**That is a Pattern #57 corpus-recursive dependency at N=3 in a single subject** — and one of the three is **v7, the subject that established the corpus's own Tier 4 "Agent-as-bridge" category**, which is the category this subject sits on top of. The corpus documented the bridge in April; this is a stranger building on it.

### 2.1 ⭐⭐⭐ And v7 already ships the skill

From the vault's own v7 wiki page `(C) Skill Integration (Claude Code + Codex + OpenClaw).md`, `notebooklm-py` ships:

- a **26 KB `SKILL.md`** for Claude Code / Codex / OpenClaw;
- `notebooklm skill install` → **`~/.claude/skills/notebooklm`**, plus `npx skills add teng-lin/notebooklm-py`;
- **intent-based auto-activation** on phrases including *"Create a podcast about [topic]"*, *"Turn this into an audio overview"*, *"Make flashcards for studying"*, *"Generate a quiz from my research"*;
- the artifact enumeration **audio / video / quiz / flashcards / slide-deck / mind-map / infographic / data-table / report**;
- five named workflow patterns, including background generation via a subagent and parallel-agent safety;
- **and an explicit trust boundary.**

Compare `SKILL.md:161-173`, this subject's headline table. It maps *"生成播客"* → `generate audio`, *"做成PPT"* → `generate slide-deck`, *"画个思维导图"* → `generate mind-map`, *"生成Quiz"* → `generate quiz`, *"做成闪卡"* → `generate flashcards`. That is **v7's artifact list, with Chinese trigger phrases**. `SKILL.md:323-332` is a `generate X` → `artifact wait` → `download X` table — **v7's Patterns 1 and 2**.

⇒ **The accurate description of this project is not "give an agent NotebookLM access."** v7's subject already does that, first-party, with an installer and a skill, three months earlier. This project's real contribution is the **ingestion front end** — a multi-source *acquisition* layer that v7 has no equivalent of.

### 2.2 ⭐⭐⭐⭐ The duplicated half is the half that had a safety model, and the duplication dropped it

The vault's v7 page records the boundary verbatim, under the heading *"Autonomy rules (trust boundary)"*:

> Agent requires confirmation: **Destructive:** `delete` · **Expensive:** `generate *` (cost + time) · **Filesystem:** `download` (writes local disk) · **Persistence:** `--save-as-note`

and the vault's own assessment of it: *"**Principled autonomy boundary.** Matches usability + safety. **Mirror-able pattern for agent skill design generally.**"*

I grepped all 742 lines of this subject's `SKILL.md` for `确认|批准|授权|询问|confirm|approval|permission|征求|需要用户|等待用户`. **One hit** — `SKILL.md:175`:

> **如果没有明确指令**，默认只上传不生成任何内容，等待用户后续指令。
> *(If no explicit instruction is given, upload only and generate nothing; wait for the user.)*

That is a **default**, not a gate. Once intent *is* detected, `SKILL.md:319-338` instructs the agent to fire `generate` → `artifact wait` → `download` **with no confirmation step**. A second grep for `delete|删除|费用|成本|cost|quota|配额|额度` over the same file returns **one hit** — `SKILL.md:523`, *"文章已被删除"*, part of an error message about a deleted article. There is **no cost language and no quota language anywhere in the file.**

⇒ **It re-implements v7's generation workflow and removes v7's confirmation boundary.** NotebookLM generation consumes plan quota and takes minutes; `download` writes to the local disk. The wrapper is more autonomous than the thing it wraps, and the boundary it dropped is one the vault had already written down as worth mirroring.

**Extent of that negative:** the two greps above, over the complete 742-line `SKILL.md`. I did not find a gate elsewhere because there is no elsewhere — `SKILL.md` is the only agent-facing file.

---

## 3. ⭐⭐⭐ Proven by execution (1): two of the six advertised cascade levels cannot run

`README.md:86-100` documents the paywall engine as a **"绕过策略（6 层级联）"** — a six-level cascade, drawn as a diagram with *"↓ 失败"* arrows:

```
Level 1: 代理服务（r.jina.ai / defuddle.md）
Level 2: 站点专属 Bot UA（Googlebot ~50站 / Bingbot ~4站）
Level 3: 通用绕过（UA伪装 + X-Forwarded-For + Referer伪装 + AMP + EU IP）
Level 4: archive.today 存档（CAPTCHA 自动检测）
Level 5: Google Cache
Level 6: agent-fetch 本地工具
```

`scripts/fetch_url.sh:351` is a **top-level, unconditional `exit 75`**. Levels 5 (`:353-366`) and 6 (`:368-376`) sit below it, along with the final `exit 1` at `:380`.

**I proved it by running it.** I copied the script, stubbed `curl` and `npx` to `return 1` (so **zero network traffic** — this is a paywall-bypass tool and I did not point it at anyone's servers), and injected trace markers before Level 5, Level 6 and the final error. Three runs:

| Input | Exit | `REACHED_LEVEL_5` | `REACHED_LEVEL_6` |
|---|---|---|---|
| `https://www.nytimes.com/2026/01/01/test.html` | **75** | never printed | never printed |
| `https://x.com/vista8/status/1` | **75** | never printed | never printed |
| `https://example.com/a` | **75** | never printed | never printed |

Dead on every input class. And `agent-fetch` — the unreachable Level 6 — is one of only **three** stages `SKILL.md:24` names for the X/Twitter path: *"内置代理级联（r.jina.ai → defuddle.md → agent-fetch）"*. **A third of the documented X/Twitter cascade is unreachable code.**

### 3.1 ⭐⭐ The corollary is worse than the dead code

Because `:351` is the single terminal state, **every** failure — DNS, timeout, HTTP 500, an empty body, a page that was never paywalled — emits the same thing (`:347-350`):

```
ARCHIVE_CAPTCHA:https://archive.today/newest/<url>
⚠️  archive.ph needs human verification.
```

That is a **diagnosis**, and it is the same diagnosis for every cause. My third run — `https://example.com/a`, a domain in none of the five lists — was told to go solve a CAPTCHA.

### 3.2 ⭐⭐ The URL decides whether your machine impersonates Googlebot

`_domain_matches` (`:70-75`) is `echo "$url" | grep -qE "$domains"` — **unanchored, and the dots are unescaped**, so the pattern matches anywhere in the URL, path and query included. I tested the exact predicate against the real `PAYWALL_DOMAINS` string:

| URL | Result |
|---|---|
| `https://attacker.example/?ref=economist.com` | **MATCHES** → cascade runs |
| `https://evil.test/read-about-nytimes.com/x` | **MATCHES** → cascade runs |
| `https://nytimesXcom.example/a` | **MATCHES** → cascade runs (unescaped `.`) |
| `https://safe.example/plain` | no match |

⇒ **the string that decides whether this machine sends `User-Agent: …Googlebot/2.1…` plus `X-Forwarded-For: 66.249.66.1` is attacker-controllable.** That matters here more than in an ordinary CLI, because the caller is an agent: a URL pasted by a user — or encountered in a page the agent is reading — can cause the user's machine to emit requests that look like Google's crawler, to a host of the URL author's choosing. Not a privilege-escalation bug; a **request-attribution** one, and the wrong side of it to be on.

### 3.3 ⭐⭐ The exit-code contract exists only in the implementation

`fetch_url.sh:346`:

> `# Use special exit code 75 so the caller (Claude) can detect and handle it`

The caller is Claude, and Claude reads `SKILL.md`. **`grep -n "75" SKILL.md` finds no mention of exit code 75 anywhere in the file.** Meanwhile the *other* caller, `main.py:413`, does:

```python
if result.returncode != 0:
    print(f"❌ 获取推文失败: {result.stderr}", file=sys.stderr)
    sys.exit(1)
```

⇒ a machine-readable protocol invented for one consumer, **never published to that consumer**, and **discarded by the only consumer that was coded against it.**

---

## 4. ⭐⭐⭐ Proven by execution (2): the "share this skill" script distributes no code

`README.md:350` describes `package.sh` as the *"打包分享脚本"* (package-for-sharing script). Its manifest, `package.sh:23-30`:

```bash
FILES=( "SKILL.md" "README.md" "install.sh" "check_env.py" "requirements.txt" ".gitignore" )
```

**I ran it.** `bash package.sh <scratchdir>` produced a 20 KB tarball containing exactly those 6 files. Absent — **14 of 20 tracked files**:

`LICENSE` · `main.py` · `package.sh` · `scripts/fetch_url.sh` · `scripts/get_podcast_transcript.py` · all 10 `feishu-read-mcp/*`

Now the history. `git show --stat bdaef0e` — the initial commit, 2026-01-25 22:47 — added exactly **seven** files: `.gitignore README.md SKILL.md check_env.py install.sh package.sh requirements.txt`. The `FILES` array names six of them; the seventh is `package.sh` itself.

**On day one the array was a complete and correct manifest of the repository.** `git log -p -- package.sh` shows it has **never been amended** — the only edits to the file across all 11 commits are two `SKILL_NAME=` rename lines.

⭐ And it went stale within **five minutes**: `LICENSE` was committed at 22:52 the same evening, and is the first file the array omits. So the "share it with a friend" artifact of an MIT project **strips the MIT notice**, and has done since the licence was added.

The recipient's experience is the point. `package.sh:63-68` prints:

```
cd ~/.claude/skills/
tar -xzf qiaomu-anything-to-notebooklm_<ts>.tar.gz
cd qiaomu-anything-to-notebooklm
./install.sh
```

`install.sh` clones the WeChat MCP and pip-installs; it does **not** create `main.py` or `scripts/`. So the recipient ends up with a 742-line `SKILL.md` instructing Claude to run `scripts/get_podcast_transcript.py`, `scripts/fetch_url.sh` and `main.py` — **none of which are on their disk.**

⭐⭐ The sharpest detail is `package.sh:70`, the script's only comment about its own completeness:

> `💡 注意：wexin-read-mcp 会在安装时自动克隆，无需打包`
> *(Note: wexin-read-mcp is cloned automatically at install time, no need to package it.)*

**It reasons explicitly about the one directory it correctly omits, and is silent about the four things it wrongly omits.**

---

## 5. ⭐⭐⭐ The Feishu subsystem: four independent reasons it does not work, and 1,838 lines for the wrong half

`README.md:361-366` presents `feishu-read-mcp/` in the project-structure block as the *"飞书文档 MCP 服务器"*. `SKILL.md:173` advertises *"创建飞书文档并写入内容"* (create a Feishu doc and write content into it); `README.md:254` promises *"自动创建飞书文档"*.

**(a) The bundled server cannot write.** `grep -rn "@mcp.tool"` over the entire repo returns exactly two hits, both in `feishu-read-mcp/src/server.py` — `read_feishu_doc` (`:33`) and `get_doc_info` (`:92`). A grep for `def (create|write|update|post|put|append|save)_|create_doc|write_doc` across all of `feishu-read-mcp/src/` returns **nothing**. It is a **reader**. The advertised capability is *writing*.

**(b) The actual writer is undeclared.** `main.py:231` shells out to `lark-cli docs +create`. `grep -rn lark` over the repo finds it at `main.py:229,231` and nowhere else but a CSS class. `lark-cli` appears in **no** README, **no** installer, **no** `requirements.txt`, and **no** `check_env.py`. It is corpus subject **v143** — and unlike `notebooklm-py` and `markitdown`, which are credited at `README.md:489,492`, it is **credited nowhere**.

⭐ So of three corpus-subject dependencies, two are credited and **the one invisible to the installer is also the uncredited one.** The corpus already tracks this contrast across two repositories — v181 cortex-hub silently bundled GitNexus v33, v265 credited codegraph v70. **Here one repository does both.**

**(c) The server cannot import.** `feishu-read-mcp/src/server.py:33`:

```python
async def read_feishu_doc(url: str, cookies_str: Optional[str] = None) -> dict:
```

`server.py`'s imports (`:3-19`) are `sys`, `pathlib.Path`, `fastmcp.FastMCP`, `logging`, `.scraper.FeishuScraper`. **`Optional` is never imported**, and no file in the repository contains `from __future__ import annotations`.

The corroboration is what makes this airtight: `parser.py:5`, `image_handler.py:7` and `scraper.py:6` **all** correctly do `from typing import ... Optional ...`. The author knows the idiom. **`server.py` — the entry point — is the only file that omits it**, and `feishu-read-mcp/src/__init__.py:6` is `from .server import mcp`, so importing the package fails too.

⚠️ **Reasoned, not executed** (`python3` is SIGKILLed here). Precisely: on Python **3.9–3.13**, annotations are evaluated at function-definition time, so `import server` raises `NameError: name 'Optional' is not defined`. On Python **3.14+**, PEP 649 makes annotations lazy and the module would import — but `fastmcp` builds a tool's JSON schema by introspecting the signature, which forces evaluation, so it fails at registration instead. `README.md:146` says *"Python 3.9+"*. **Broken on the versions it targets; I could not run it to confirm which failure you get.**

**(d) ⭐⭐ The only test in the repository tests everything except the file with the bug.** `feishu-read-mcp/test.py` imports `scraper`, `parser` and `image_handler` (`:12,22,23,24,56,94`). It **never imports `server`** — the one module that fails on import. A single `import server` would have caught it.

**(e) And the flag is silently dropped anyway.** `main.py:266` declares `def deep_analysis(file_path, title, content_type, to_feishu=False)`. Its four call sites — `:339` (epub), `:356` (document), `:393` (podcast), `:442` (x_twitter) — **all pass three positional arguments.** `to_feishu` defaults to `False`. Only the `url` branch honours it, inline at `:494-496`.

⭐⭐⭐ **The documented example is the broken path.** `README.md:393`: `python main.py ./book.epub --deep-analysis --to-feishu`. `SKILL.md:290-291`: `main.py /path/to/file.epub --deep-analysis --to-feishu`. **Both documents give the EPUB form, and EPUB is `:339` — the flag is parsed, accepted, and discarded.** The run prints `✅ 分析完成！`, writes its JSON, and creates no Feishu document. No warning. No error.

That is the corpus's **FALSE SUCCESS** class (v251, v260) in its purest form: not a misleading log line, but a **command-line flag that is read and thrown away**, in the exact invocation both manuals print.

---

## 6. `main.py`: the classifier was kept in sync with the docs; the dispatcher was not

`detect_input_type` (`:16-48`) returns **thirteen** values: `weixin`, `youtube`, `podcast`, `x_twitter`, `url`, `epub`, `document`, `office`, `image`, `audio`, `zip`, `search`, `unknown`. It is a faithful implementation of `SKILL.md`'s recognition table at `:183-200`.

`main()` dispatches **five**: `epub`, `document`, `podcast`, `x_twitter`, `url`. Everything else hits `:503-506`:

```
❌ 不支持的输入类型: youtube
提示: 请使用 EPUB、PDF、TXT、MD 文件或 URL
```

The dropped set includes **`weixin`** — the founding capability, still source #1 and trigger #1 in `SKILL.md` — and **`youtube`**, which owns a section marked *"🔴 特殊规则（最重要！）"* ("special rule — the most important!") at `SKILL.md:227`.

**The fair reading matters here.** There are **two runtimes**: the agent path (Claude reads `SKILL.md` and calls `notebooklm` / `markitdown` / the MCP itself) and the CLI path (`main.py`, which `README.md:347` calls *"主入口：CLI 智能处理器"*, the main entry point). WeChat and YouTube work on the agent path. They do not exist on the CLI path. **No document distinguishes the two**, and the product is presented as one thing.

⇒ **A classifier that knows thirteen types and a dispatcher that implements five, in the same 509-line file** — the boundary at which the discipline stopped is two functions apart. This is v264's and v265's finding at the smallest scale the corpus has recorded it.

**One more divergence with teeth:** the plain-URL branch (`:455-458`) calls `notebooklm source add <URL>` **directly**. `scripts/fetch_url.sh` is invoked from exactly one place, `:407`, the X/Twitter branch. So on the CLI path a **paywalled URL is handed straight to NotebookLM with no bypass** — and `README.md:189-200`'s headline worked example is *"把这篇 The Information 文章生成播客"* with *"✓ 检测付费墙 → Googlebot UA 绕过"*. The README's flagship scenario does not describe the CLI. (It does describe the agent path, where `SKILL.md:225` routes paywalled URLs through `fetch_url.sh`.)

**Smaller, real:** `tempfile.mktemp()` at `:65` and `:430` — deprecated since Python 2.3 for a documented symlink race. `create_feishu_doc` (`:231`) passes an entire analysis document as **one argv element**, which for a twelve-question book analysis is an `E2BIG` risk. `ask_round`'s `title` parameter (`:247`) is never used. `:410` sets `timeout=60` on `fetch_url.sh` while that script's own budget along the x.com path is `20 + 20 + 20 = 60s` of `--max-time` — **exactly at the boundary**, and `subprocess.TimeoutExpired` is not caught, so any latency at all yields a traceback instead of the intended handling.

**And credit where it is due.** `generate_questions_progressive` (`:113-182`) is the best code in the repository. Its docstring states its design rules — *"请基于提供的文档内容回答" 防止 NotebookLM 触发网络搜索* (phrase it this way to stop NotebookLM reaching for web search), use action verbs, avoid yes/no questions — and the three rounds are genuinely well-constructed, with a distinct round-2 set for books, for video, and for articles. `label_for` (`:98-110`) exists solely so questions read naturally in Chinese ("本书" vs "这期播客" vs "这条推文"). **Someone thought carefully about prompting here.** The rounds exploit NotebookLM's session context so later questions build on earlier answers — that is a real idea, and `README.md:388` states it explicitly.

---

## 7. ⭐⭐⭐⭐ THE HEADLINE: every defect above had a fix sitting in an open pull request

Three PR refs exist on the remote. All 11 commits on `main` are the author's. **Nothing was ever merged.** I fetched all three.

### PR #1 — Hanson Mei, 4 commits, opened **2026-01-26**, the day after the initial commit

`README.md +40` · **`SKILL.md +255/-116`** · **`install.sh +180/-32`** · `requirements.txt`

Commit `1caebb6`, body verbatim:

> - Optimize description for better trigger detection
> - Add Quick Reference table for common commands
> - Add Progress Updates section for status feedback
> - Add Output Summary templates for consistent output
> - Refactor Error Handling to structured format
> - Simplify Troubleshooting section
> - **Update install.sh to use virtual environment**
> - **Fix markitdown dependency (remove [all] extra)**
>
> `Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>`

I checked the branch rather than trusting the message. `git show refs/remotes/pr/1:install.sh` contains `VENV_DIR="$SKILL_DIR/.venv"` (`:10`), `python3 -m venv "$VENV_DIR"` (`:128`), `source "$VENV_DIR/bin/activate"` (`:132`) — **and it rewrites the emitted MCP config to `"command": "$VENV_DIR/bin/python"` (`:238`)**, instead of the bare `"python"` that `main`'s `install.sh:112` and `SKILL.md:84` still emit today.

⇒ **PR #1 fixes both the global-pip problem and the `python`-vs-`python3` problem.** In January.

It then kept going: `4cf2d35` (2026-01-26) added **bilibili as a 12th content source** via `bilibili-subtitle`, and `e26b288`/`5e879d9` (2026-02-17) added a `BBDown` dependency guard and clarified the orchestrator model. And the contributor wrote a **graceful-degradation clause into the agent-facing doc** (`refs/remotes/pr/1:SKILL.md:31-32`):

> `bilibili-subtitle` 是可选插件… 未安装时主流程可继续处理其他来源。
> *(…an optional plugin; when it is not installed the main flow can continue with the other sources.)*

### PR #3 — `octo-patch`, 2026-04-21

`main.py +106/-29` · `minimax_provider.py +90` · `requirements.txt +3` · **`tests/test_minimax_provider.py +201`**

⭐⭐ **201 lines of tests — the only test code ever offered for this project's own code.** At HEAD, the repository has none (`feishu-read-mcp/test.py` tests the bundled MCP, and as §5(d) shows, not the broken part of it). Not merged.

### PR #5 — `rice5`, 2026-05-15

`check_env.py +6/-2` — *"fix: Windows GBK 编码导致 check_env 崩溃"*. A six-line fix for a crash on Windows, opened 17 days after HEAD. Not merged.

### ⭐⭐⭐ The rule

`git log -S "bilibili"` on `main` returns exactly one commit: **`9b6bebd`, 2026-04-18** — *"feat: add paywall bypass (BPC strategies), podcast transcription, and URL fetch cascade"*. The same query on PR #1 returns `4cf2d35`, **2026-01-26**.

**The bilibili feature arrived twice: once as a merge-ready contribution in January, and once as the maintainer's own reimplementation 82 days later.** The version that shipped is not the better one. PR #1 built on `bilibili-subtitle` + `BBDown` — public tools, an optional dependency, with a written degradation path. The maintainer's version routes B站 through **Get笔记**, a commercial third party, requiring a hand-extracted browser JWT and an undocumented endpoint (§8).

⇒ **The corpus has spent five ships on gates: v261 the claim without the test, v262 the gate that cannot fail, v263 the test with no gate, v264 the gate that skips and prints which, v265 the gate that is wired and never invoked. v266 is not about gates.**

**v265 found that a discipline stops where crossing a boundary would cost something. v266 finds the cheaper failure: the discipline was already at the door, written, in a diff — and nobody opened it.** Merging PR #1 cost ten minutes of review. Not merging it cost: the venv defect survives, the `python`-vs-`python3` defect survives, the agent-facing doc stays incoherent, the repository has no tests, it crashes on Windows, and the bilibili feature gets built a second time on a worse foundation.

⭐ And the detail that closes it: **`Co-Authored-By: Claude Opus 4.5`.** The fix was written by another person's Claude Code. An agent-assisted contribution to an agent-assisted skill, declined by silence — and three months later the same maintainer, working the same way, solved the same problem again from scratch.

⚠️ **Not established:** whether the author ever saw these PRs, replied to them, or declined them for a reason. GitHub's issue/PR *conversation* is not in the git data and I did not fetch it. What is established is that the code exists on the remote, is older than the defects' survival, and is not in `main`.

---

## 8. The podcast path: an official API that cannot read its own results

`scripts/get_podcast_transcript.py` (166 lines) uses **two different services**:

- **`openapi.biji.com`** (`:20`) — the documented Get笔记 OpenAPI, authenticated with `GETNOTE_API_KEY` + `GETNOTE_CLIENT_ID` from the environment. Used to *create* the transcription job (`:95`) and poll it (`:117`).
- **`get-notes.luojilab.com/voicenotes/web/notes/{id}/links/detail`** (`:73`) — a **private web endpoint**, authenticated with a Bearer JWT and spoofed `Origin: https://www.biji.com` / `Referer: https://www.biji.com/` headers. Used to *read the transcript*.

⇒ **The official API can start the work but cannot retrieve the result**, so the script reverse-engineers the web app's own endpoint using browser-session credentials. Same species as corpus v231/v232.

The JWT lives at `~/.claude/skills/getnote/tokens.json` (`:12`) — **a path inside a different skill's directory that this repository does not ship.** `:57` tells you how to refresh it: *"refresh_token expired (90 days). **Re-initialize from browser.**"* There is **no documented procedure anywhere in the repo** for producing that file. `README.md:176-183` documents only the two environment variables; the token file is mentioned once, at `SKILL.md:214`. **You are told two of the three credentials you need.**

Handling: every credential is passed as a `curl -H` **argv element** (`:21-25`, `:74-78`), so the API key and the JWT are visible in the process table to any local user. `save_tokens` (`:36-38`) rewrites the 90-day refresh token with default permissions — no `chmod 600`.

Timing: `for i in range(40): time.sleep(30)` (`:115-116`) is up to **20 minutes**, and because the sleep precedes the first status check, the **floor is 30 seconds** even for an instant result. `README.md:209` and `SKILL.md:367` both say *"2-5 分钟"*. `main.py:370-373` invokes it with **no timeout**, so a 20-minute block is reachable. `prog['data']['status']` (`:119`) is unguarded — a malformed response raises `KeyError`.

---

## 9. ⭐⭐ The v262 test, applied and quantified: inflation scales with the size of the number

I counted the domain lists in `scripts/fetch_url.sh` by splitting on `|`.

| Claim | Where | Measured | Verdict |
|---|---|---|---|
| Bingbot **"~4 站"** | `README.md:119` | `BINGBOT_DOMAINS` = **4** | ✅ **exact** |
| AMP **"~10 站"** | `README.md:121` | `AMP_DOMAINS` = **12** | ✅ honest |
| Googlebot **"~50 站"** | `README.md:118` | `GOOGLEBOT_DOMAINS` = **22** | ❌ **2.3× over** |
| **"300+ 付费网站"** | `README.md:53,84`; `SKILL.md:27,237` | **54** unique domains across all five lists | ⚠️ see below |
| deep-analysis **12 questions** | `README.md:224,377,382-386` | `main.py`: 4 + 5 + 3 = **12** | ✅ correct |
| deep-analysis **10 questions** | `SKILL.md:296,314`; `README.md:252` | actual **12** | ❌ wrong in 3 places |
| **"13 项环境检查"** | `README.md:349,437` | `results.append` count = **13** | ✅ **correct** |
| progress labels | `check_env.py:140` prints `[1/8]`; `:145-191` print `[N/9]` | 13 results | ❌ **both self-labels wrong** |

⭐⭐ **The two small numbers are right and the two big ones are not, and the gap grows with the size of the claim.** That is v262's rule — *tests make you honest about the things they test* — with a measured gradient.

**⚠️ The "300+" claim, stated precisely, after a fair objection.** A reviewer pushed back that "300+" may describe *reachability through the proxy layer* rather than the hardcoded lists — and that objection is **partly right**: `fetch_url.sh:129,133` run **r.jina.ai and defuddle.md unconditionally, before any domain check**, so the proxy attempt does apply to any URL. So the honest formulation is three parts, not one:

1. **54** domains receive site-specific handling (bot UA, referer spoofing, AMP). "300+ sites get the bypass techniques" is **false**.
2. "300+ sites might be readable via the generic proxy" is **not falsifiable from this repository** — r.jina.ai's coverage is a property of Jina, not of this script, and nothing here measures it.
3. ⇒ **The only possible basis for the number is a third party's coverage presented as this tool's** — and that is **exactly the same move as the "~50 站" case**, which is what makes the pattern worth naming rather than either number on its own.

⭐ Because the Googlebot case makes the mechanism explicit. `fetch_url.sh:138` comments: `# 2a. Googlebot — most effective strategy, ~50 sites in BPC`. That is **true, and it is a statement about BPC.** `README.md:118` moves "~50 站" into a column headed **覆盖率** (coverage rate) in a table headed *"绕过技术"* (bypass techniques). **The honest statement is in the code; the README converted another project's coverage into a claim about this one — twice, once at ~50 and once at 300+.**

⭐ And the **"13 项环境检查"** case inverts it: the README states the true number (13 boolean results) while the script's own progress labels say 8 and 9. **The prose is right and the code's self-description is wrong** — the one place in this repository where that happens.

Two junk entries survive in the lists: **`wires.com`** (not a publication) and **`harvard.edu`** (an entire university, classified as a paywall). And `README.md:108` claims FAZ support while the list contains `frankfurter-allgemeine.de`; **`grep -c "faz\.net"` over `fetch_url.sh` = 0.**

---

## 10. `SKILL.md` as an agent-facing artifact

This is the file Claude actually loads. Its defects are therefore not cosmetic.

**The section numbers do not count.** The h3 headings in the 支持的内容源 block run **1, 2, 3, 4, 5, 5, 4, 5, 5, 6, 7, 8, 9, 10, 11** — four collisions and one backwards step, the accretion signature of sources appended without renumbering.

⭐ **A numbered list is attached to the wrong heading.** `:227-231` is the YouTube rule — *"🔴 特殊规则（最重要！）… **禁止**使用 yt-dlp"*. Immediately beneath it, `:232-237`, indented as its children:

```
  1. **r.jina.ai** — 通常能绕过软付费墙
  2. **Googlebot/Bingbot UA 伪装**
  ...
```

Those are the **paywall** steps, orphaned under the YouTube heading when `9b6bebd` added the bypass. An agent reading the "most important rule" section finds paywall-bypass instructions nested inside it.

**The file lies about its own age.** `:740-742`:

```
**Skill 创建时间**：2026-01-25
**最后更新**：2026-01-25
**版本**：v1.0.0
```

HEAD is **2026-04-28**, six commits later, and the newest tag is **v1.0.1**. The manifest-fossil pattern (v260, v262, v265) — here in the one file whose job is to tell the agent what it can do.

**A machine path in the documented config.** `:86` and `:644` both hardcode `/Users/joe/.claude/skills/...` in the JSON the reader is told to paste. `:84` specifies `"command": "python"` — not `python3`, which on a stock macOS is not a command. **PR #1 fixed both.**

**Phantom siblings.** `:625-629` lists three *"相关 Skills"*: `notebooklm` (v7's real skill), `notebooklm-deep-analyzer` (appears **exactly once** in the whole repo — this line — and is not shipped, installed, credited or linked), and `markitdown` (corpus v28, a **library**, not a skill). One real, one misdescribed, one with no referent.

**What it does well, genuinely.** The natural-language→intent table (`:161-173`) is a clean design: it makes the skill's whole surface legible in twelve rows, and the *"如果没有明确指令，默认只上传"* default at `:175` is the right default. The error-handling section (`:506-558`) writes out six failure modes with causes and suggested actions — more than most skills bother with. The six worked examples (`:340-504`) show input, execution trace and output, which is exactly what an agent needs to pattern-match against. And the YouTube rule, orphaned list aside, is a **real and correct engineering decision**: NotebookLM ingests YouTube URLs natively, so the file forbids the agent from wasting effort on `yt-dlp` or Whisper. That is the author knowing his tool.

---

## 11. Supply chain, and what installing this actually means

`install.sh` fetches two third-party artifacts, **neither pinned**:

- `:49` — `git clone https://github.com/Bwkyd/wexin-read-mcp.git "$MCP_DIR"`. No tag, no commit, no `--depth`. If the directory already exists it prints *"✅ MCP 服务器已存在"* and never updates.
- `:94` — `pip3 install git+https://github.com/teng-lin/notebooklm-py.git`. Unpinned. **No virtualenv** — straight into the user's Python.

The `wexin-read-mcp` clone is then **registered as an MCP server that Claude Code executes** (`:111-116`, `SKILL.md:79-91`). So the WeChat capability — the repository's founding feature — is arbitrary Python from a bare-handle third-party account, at whatever HEAD it has on the day you install, wired into the agent's tool surface. `README.md:491` does credit `Bwkyd/wexin-read-mcp`, so this is disclosed, not hidden.

⚠️ **Correcting my own first reading.** I initially recorded `wexin-read-mcp/` as a v265-style dangling pointer, because `git rev-list --objects --all` proves it has **never existed at any path on any ref**, while `README.md:356-360` draws it inside the project-structure tree with three named child files and per-file comments. **That was wrong**: `install.sh:40-51` fetches it deliberately, `.gitignore:28` excludes it on purpose, and `package.sh:70` explains the omission. The real finding is narrower and fairer: the README **presents a third-party clone target as first-party structure** — a presentation defect, not a broken pointer. This is the same error shape my last three ships logged (inferring a missing capability from a missing file), caught here before publication by reading the installer.

`check_env.py` is a good idea with three gaps. It checks 13 things and requires **all 13** to pass for exit 0 (`:215`), so a user who only wants PDF→podcast gets a red *"❌ 检查失败"* over `fastmcp` and `playwright` they do not need. It checks `wexin-read-mcp/src/server.py` (`:100`) — correctly, since the installer creates it. But it does **not** check `lark-cli`, which `main.py` invokes, and it does **not** check `ebooklib`, which `main.py:52` imports — and `ebooklib` appears in **no requirements file anywhere in the repo** (`grep -rn ebooklib` → `SKILL.md:192,240`, `main.py:52,53,60`; nothing else). So the EPUB path — `README.md`'s scenario 3, and a deliberate design choice at `SKILL.md:240` (*"使用 Python ebooklib… 避免 Calibre 架构问题"*) — **raises `ImportError` on a clean install.** `requirements.txt:11` also carries the project's single most load-bearing dependency as a **comment**: `# notebooklm-py`.

⚠️ `.gitignore:26-28` is a small honest curiosity: the comment reads *"Keep the directory but ignore its contents"* above the pattern `wexin-read-mcp/`, which ignores the directory **and** its contents — and git cannot track an empty directory regardless. An intent git has no way to express.

---

## 12. Legal and ethical posture — stated plainly

**What the tool does.** `fetch_url.sh` sends `User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; ...)` together with `X-Forwarded-For: 66.249.66.1` (`:141-142`, `:196-197`) — impersonating Google's crawler **and** claiming Google's IP space — plus Referer spoofing as Google/Facebook/`t.co`, cookie clearing (`-b ""`), AMP variants, and archive.today, against 54 named domains including NYT, WSJ, FT, Bloomberg and The Economist.

**What the author says.** `README.md:458-461`, verbatim: *"本工具仅用于个人学习研究。技术原理基于搜索引擎白名单（Googlebot/Bingbot），不破解任何加密。建议支持优质新闻媒体，购买订阅。"* — for personal study only; based on search-engine whitelisting; **breaks no encryption**; please subscribe to good journalism.

**Assessment, fairly.** *"Breaks no encryption"* is technically **true** — there is no cryptographic circumvention here, only HTTP header manipulation. It is also not the operative question: sending a Googlebot UA plus a Googlebot IP to obtain subscriber content is a straightforward violation of every one of those publishers' terms of service, and the provenance is disclosed at `README.md:114` — the strategies are *"学自 Bypass Paywalls Clean"*, a project now hosted on **gitflic.ru** after being removed from GitHub and GitLab. That relocation history is itself the clearest available statement of how platforms treat this category.

⭐ `README.md:496` reads **"[MIT License](LICENSE) - 仅限个人学习研究使用"** — *MIT, for personal study and research only.* That is a contradiction: MIT grants commercial use without restriction, and the `LICENSE` file (which I read in full) contains no such limitation. The README **adds a restriction the licence does not carry**, so the actual grant is ambiguous. ⚠️ And `package.sh` ships the README **without** the LICENSE (§4), so a recipient of the tarball gets the restriction and not the grant.

**Licence compliance on the derived work.** There is **no NOTICE file and no third-party licence file** — `LICENSE` is the only one, naming Joe alone. Prose credit at `README.md:114,490` is genuine and prominent, but prose credit in a README and a licence obligation in a LICENSE file are different instruments — the v264 **D44** point, inverted at v265 and recurring here.

**The credential surface, which is the part that matters most for a pilot.** From the vault's own v7 wiki: `notebooklm login` performs **browser-based OAuth via Playwright** (Chrome/Edge), persisting a `storage_state.json`, against *"undocumented Google APIs subject to breaking changes"* (v7 `(C) README summary.md:16,115,119,129`). So installing this skill means: a **Playwright-driven session of your real Google account**, plus a hand-extracted 90-day biji.com JWT, plus a Google-crawler-impersonating fetcher, driven by a skill with **no confirmation gate** (§2.2), through **two unpinned third-party packages** (§11). Each piece is defensible on its own. Assembled, that is the fence.

**What the author does responsibly.** The disclosures are real and repeated: BPC is credited by name and URL, `notebooklm-py` and `markitdown` are credited, the FAQ addresses legality directly rather than hiding it, the copyright note at `SKILL.md:608-611` asks users to respect WeChat's terms and forbids commercial use of outputs, and `README.md:460` ends by telling you to **buy the subscription**. Compared with the corpus's other bypass-adjacent subjects, this is the disclosing end of the spectrum.

---

## 13. Verdict

**GOAL-ALIGNED INCLUDE 3/4** — (a) **FAIL** · (b) **STRONG** · (c) **STRONG** · (d) **STRONG**. Cleanly GA; no §40 needed; no override.

- **(a) FAIL.** §41: no declared Anthropic affiliation, and no registered (a)-7 vendor-direct source. A disclosed individual with a real public identity (X `@vista8`, WeChat 「向阳乔木推荐看」) is not a registered (a) axis — the standing v171/v174/v183-v185/v204-v205/v212 discipline. No name, heritage or locale inference.
- **(b) STRONG.** It is a Claude Code skill, on goal #1's substrate. The agent *is* the runtime; the whole artifact is agent-facing.
- **(c) STRONG.** Instructive in both directions — a well-built progressive-questioning module and a clean intent-mapping table, alongside the most legible pull-request-shaped failure in the corpus.
- **(d) STRONG.** Three prior corpus subjects are its dependencies (v7, v28, v143); it sits in the skill-collection / agent-capability cluster.

### NO MINT — four grounds, none of them §28

1. **Not world-first, and the prior art is in the vault.** Corpus **v7** (`teng-lin/notebooklm-py`, 2026-04-18) already ships a 26 KB `SKILL.md` for Claude Code / Codex / OpenClaw, an installer (`notebooklm skill install`), intent auto-activation on the same phrases, and the same artifact enumeration — **three months earlier, first-party, with a trust boundary this subject lacks.**
2. **Form factor within an established genre.** A front end for an existing capability is not a new capability class — the **v222** lobehub (decisive), **v227** hermes-webui and **v236** dsh-TUI line. This is a localized trigger vocabulary plus an ingestion layer over v7's bridge.
3. **Domain/locale coverage is not capability.** The genuinely new-for-the-corpus part is the *Chinese-platform acquisition stack* (WeChat public accounts, 小宇宙/喜马拉雅/B站 via Get笔记, 飞书). That is domain-not-capability — the **v196** meetily / **v210** AIRI / **v213** geti discipline.
4. **The novel parts are components, not the product** (**v242 D25**), and the most distinctive component — the paywall cascade — is **openly derived** from Bypass Paywalls Clean and is one-third unreachable (§3).

`inflation_check` HELD. **Per §44 cl. 5, §28 does none of the work here.**

**Counts: 46 top-level patterns / 12 CONFIRMED Library-vocab UNCHANGED. §C-1 = 12. §C-2 = 38.**

### Recorded, NOT self-executed (a mint is an audit act)

One **§C-2 candidate** worth an audit's attention: *"Agent-Facing Paywall-Bypass Fetch Layer"* — a bypass cascade packaged as a capability an AI coding agent calls, rather than as a browser extension a human clicks. Corpus-first for the *agent-facing* surface; decisively **not** world-first (BPC and its ecosystem precede by years). I record it and decline to mint it: the strategies are borrowed, a third of the cascade is dead, and the corpus's web-acquisition family is already well populated (crawl4ai v29, browser-use v41, CloakBrowser v69, Agent-Reach v174, camofox v179, firecrawl v214, CoreOfPotato v231, gemini-web2api v232).

### Instance-strengthening recorded, not self-incremented

- ⭐⭐ **Pattern #57 corpus-recursive dependency at N=3 in one subject** — v7 `notebooklm-py` + v28 `markitdown` + v143 `lark-cli`, with **v7 being the subject that established the Tier-4 category this one occupies.** The credit asymmetry (two credited, the uncredited one also invisible to the installer) is the v181-vs-v265 contrast **inside a single repository**.
- **Pattern #18 sub-archetype B1-MCP** — bundles one MCP server and registers a second, third-party one.
- **Pattern #68 / #88** — not applicable; this is a single skill, not a collection or an anti-slop ruleset.
- **Pattern #19** 19a (individual, non-Anthropic). **Pattern #66** MIXED-to-NEGATIVE (two unpinned third-party fetches, no venv, one becoming an agent tool). **Pattern #12** MIXED. **Pattern #83** — the FAQ's legality disclosure and the BPC credit are honest-deficiency disclosure; the "300+" and "~50" claims are not.
- **NOT Pattern #52** — star/fork counts are page-stated only (§37.4). `README.md:10-13` embeds shields.io badges; **no velocity was verified and none is claimed.**

### Streak

**v265 `GA:122` → `GA:123 · OG:13 [7 ov]`** — **46 consecutive goal-aligned ships, v220→v266.** **§35 CLEAR** (window {v264 GA, v265 GA, v266 GA} = 0 OG). No override.

---

## 14. Method, and my errors

**Hand-verified throughout.** Every `path:line` in this document was read in my own command output. The repository is 4,680 lines, so I read essentially all of it directly rather than delegating. Three **local experiments were executed** — the `fetch_url.sh` reachability probe with the network stubbed (§3), the `_domain_matches` predicate test (§3.2), and a real `package.sh` run (§4). A fleet of 22 agents (9 dimensions × assess→refute, 4 prior-art/identity lenses, a completeness critic, and an adversary pointed at the critic per v261's lesson) ran in parallel for corroboration: **20 completed; 2 hit the StructuredOutput retry cap** — `main-py-dispatch` and `feishu-subsystem`, both dimensions already covered by hand, the same failure v264 and v265 recorded. **2.60M subagent tokens, 575 tool uses, 1,143s.**

**⭐⭐ What the fleet was and was not good for.** It independently reproduced the `package.sh` run and the dead-cascade result, and it contributed one finding I adopted after verifying it myself (§3.2, the URL-controlled header spoofing). But:

- ⭐ **The decisive finding — the v7/v28/v143 collision and v7's pre-existing skill with its trust boundary — came from my own hand-greps of the vault, not from the fleet.** That is precisely why the standing practice is to run collision checks by hand.
- 🔴 **A fleet dimension made my own retracted error and rated it `critical`**: *"MCP server configuration references non-existent directory… MCP server fails to initialize."* Same trap, same file, independently — **inferring a missing capability from a missing file**, when `install.sh:40-51` clones it. **The trap is structural, not personal.**
- ⚠️ **Two of its `path:line` citations are wrong** where mine are right: `server.py:31` (actually **:33**; :31 is blank) and `main.py:129-133` for `round1` (actually **:134**; :133 is the comment). Both re-verified with numbered `awk`. ⇒ **a subagent's line number is a claim, not a citation** — §43.1's rule, earning a second form.
- ⚠️ **One agent ran `fetch_url.sh` against a live URL**, which I had deliberately avoided. The target was `example.com`, a reserved test domain, so no publisher was touched — but it means outbound requests reached r.jina.ai / defuddle.md / archive.today from this session. Recorded because it was not authorised by me and is the kind of thing that should never be discovered later.

**Error ledger — 3, all mine, all caught before publication:**

- 🔴 **"`wexin-read-mcp` is a dangling pointer."** Wrong. `install.sh:40-51` clones it deliberately. I inferred a missing capability from a missing file — **the same error shape my last three ships logged**, committed again. The fix was not a better grep; it was reading the installer. Corrected in place at §11.
- ⚠️ **First-pass corpus greps returned "notebooklm = 6134 / markitdown = 3807 matches."** Substring inflation across `.claude/worktrees/` copies — the v264 `RATIFIED` trap and v265's `\bZep\b` trap recurring for a third consecutive ship. Re-measured per-file with worktrees excluded, which is what surfaced the actual v7 and v28 project directories. ⇒ **the rule holds: open the thing the measurement measured.**
- 🔴 **"the unmerged chain is 63 ships long, from v204."** Wrong, and wrong because I read it off the *previous ship's prose* instead of running `git rev-list`. The measured answer is **45 commits / 41 ships / v227→v265, with `main` at v226**. ⭐ The error is the finding: I inherited a stale number from the shim's copy-forward text — **§43.2's ground-truth-amplifier hazard, committed by the orchestrator against its own vault**, on the one claim in this document that is about us. Corrected at §15 Rung 1, where it now derives from four commands whose output is printed. **This is the third consecutive ship whose worst error was generalising from where I chose to look rather than from what I read** — and the first where the thing I failed to read was the vault's own git history.

**⚠️ The fairness challenge, on the record.** The fleet's completeness critic — whose job was to attack this audit, not the subject — returned: *"**NO. The audit is technically accurate but tonally unfair to a one-person hobby project.** … 80% of findings are documentation nits … If this were a commercial product this audit would be appropriate; for a one-person hobby project shared for free, it reads like a hatchet job."*

**Partly accepted.** It produced one correction I adopted (the "300+" ambiguity, §9) and one I rejected on evidence: it asserted `main.py` handles *"6 working types, not 5"*, and an `awk` over `main.py:315-509` returns exactly five `input_type ==` branches (`:328` epub, `:349` document, `:365` podcast, `:403` x_twitter, `:451` url) plus the `else` at `:503`. **Five.** ⭐ That is a synthesis-stage factual error of exactly the kind v261 recorded — which is why an adversary was pointed at the critic, and why the count above is quoted from a command rather than from the critic.

On tone I substantially disagree, and the disagreement is worth stating rather than quietly splitting. This document's weight does not sit on documentation nits: it sits on **three findings established by running the code** (a dead cascade, a code-free distribution artifact, a discarded flag), on **a removed safety boundary** measured against the tool this project wraps, and on **three unmerged pull requests** that make the whole picture a process finding rather than a quality one. Those are not hobby-project shortcuts; the first three are things the author would want to know, and the fourth is not a criticism of his code at all.

Where the critic is right is proportion, and I have tried to honour it: the good work is named specifically — the questioning module, the anti-escape-hatch prompt clause, the referent helper, the intent table and its default, the six worked examples, the error-handling section, the YouTube rule, and disclosures that are more honest than this genre's norm. **A free hobby project owes its users nothing. This document is a record for one reader's decisions, not a verdict on its author** — and its bottom line is *read it and borrow from it*, which is a recommendation to take the work seriously.

**Not established:**
- Whether any of this runs end to end. Nothing was installed; no credential was created; no network request was made to any subject-related service.
- The Python failure mode in §5(c) — reasoned from source and documented language semantics, **not executed** (`python3` SIGKILLed, exit 137).
- Whether the author saw, replied to, or declined PRs #1/#3/#5. GitHub conversation data was not fetched.
- Star/fork counts (§37.4 — the environment mocks the GitHub API).
- Whether `Bwkyd/wexin-read-mcp` currently exists or what its code does. **I did not clone it**, and its content is whatever it is on your install day — which is the point of §11.
- How well the deep-analysis questions actually perform. The prompting is thoughtful; **no output was measured.**

**Sandbox:** `python3` unusable (SIGKILL), bash 3.2, git 2.19 (`git branch --show-current` unsupported).

---

## 15. Pilot: ⭐ READ-AND-BORROW — do not install

The licence is permissive and the author is transparent, so the reason to decline installation is not legal. It is that the install path assembles a Playwright session of your Google account, an unpinned third-party MCP server executed by Claude, a hand-extracted commercial JWT, and a Google-crawler-impersonating fetcher — behind a skill with **no confirmation gate**. Nothing here is worth that, because **the one thing you would want it for, corpus v7 already ships properly.**

**Rung 0 (20 min) — read six things, in this order.**
`SKILL.md:161-175` (the intent table and its default) → `main.py:113-182` (the three-round question generator, the best code here) → `main.py:266` beside `:339` (the dropped flag) → `scripts/fetch_url.sh:327-380` (the dead cascade) → `package.sh:23-30` beside `git show --stat bdaef0e` (the fossil) → `git log refs/remotes/pr/1 ^main` (§7).

**⭐⭐⭐ Rung 1 (30 min) — the vault action, and it is a merge queue, not a linter.**
This ship's rule is that the fix was in the door and nobody opened it. **The vault has the same shape, and I measured it rather than assuming it:**

```
git rev-parse --abbrev-ref HEAD          → wiki/v266-qiaomu-anything-to-notebooklm
git log --oneline main -1                → e0459f1 v226 code-review-graph
git rev-list --count main..HEAD          → 45
git log --format=%s main..HEAD | grep -cE '^v[0-9]+ '  → 41   (spanning v227 → v265)
```

**`main` is at v226. Forty-five commits are unmerged, forty-one of them ships or audits, covering v227 through v265.**

⭐ And the vault's own instruction about it is stale in exactly the way this ship documents. The shim's standing next-action reads *"review + merge the chain (v204 → … → v264 → v265, in order)"* — but **v204 through v226 are already merged**; that sentence has been copied forward across ~39 ships while the fact underneath it moved. A manifest that was correct when written, carried forward unchecked, describing a state that no longer exists: `package.sh:23-30` with a different filename.

**Do two things.** (1) Correct the next-action to name the real range, and make it derive from a command rather than from the previous ship's text. (2) Write into `CLAUDE.md` the one number that matters — `git rev-list --count main..HEAD` — and a threshold above which a new ship does not start. Ten lines. It is the cheapest instance of this ship's finding, and it is about us.

**⭐⭐ Rung 2 (30 min) — steal the trust boundary, from v7, not from v266.**
v7's autonomy rules are the reusable artifact: *read-only runs unattended; destructive, expensive, filesystem-writing and persisting operations require confirmation.* Paste that four-way classification into the vault's `05 Skills/` skill-authoring guidance as a required section, then check the vault's own skills against it. v266 is the counter-example that proves it matters: a wrapper more autonomous than the tool it wraps.

**⭐⭐ Rung 3 (45 min) — the progressive-questioning module, into the vault's own reading practice.**
`main.py:113-182` is directly liftable and needs no install: three rounds (4 overview / 5 depth / 3 synthesis), per-content-type round-two variants, action verbs not yes/no, and the anti-web-search clause *"完全基于文档回答"*. That last one is a real prompting insight about a specific tool's failure mode. **Use it against a corpus document and see whether round three beats a single-shot summary.** Zero risk, zero dependencies.

**⭐⭐ Rung 4 (45 min) — the export-boundary check, extended by one clause.**
v265's Rung 1 proposed asserting that every vault-internal path reference resolves. v266 adds the **distribution** case: assert that every file the vault's own packaging or publishing paths *claim* to ship is actually shipped. `package.sh` is the specimen — a manifest that was correct for five minutes and wrong for seven months, with nothing able to notice.

**⭐ Rung 5 (60 min) — a fenced look at v7 instead, if the capability appeals.**
If "turn a document into a podcast" is genuinely wanted, pilot **corpus v7** (`teng-lin/notebooklm-py`) directly: it is the same capability, first-party, with the confirmation gate, MIT, ~11k★, and it installs its own skill. Fence it anyway — a throwaway Google account, a venv, a pinned version, and read `notebooklm auth check --test` before pointing it at anything.

**🔴 NEVER:** run `install.sh` on a machine with a Google account you care about · register `Bwkyd/wexin-read-mcp` as an MCP server without reading its code first · run `fetch_url.sh` against a publisher's site · cite the "300+ sites" or "~50 sites" figures · treat `--to-feishu` as working on any path but `url` · assume a `✅ 分析完成！` means a Feishu document exists · read *"archive.ph needs human verification"* as meaning archive.ph was the problem.

---

## 16. Blunt

**The code in this repository is better than its documentation, and its documentation is better than its process.**

The question generator is thoughtful work — three rounds, per-content-type variants, a clause that stops NotebookLM reaching for web search, and a helper whose only job is to make the questions read naturally in Chinese. The YouTube rule is a maintainer who knows his tool well enough to forbid the obvious wrong approach. The intent table makes an eleven-source product legible in twelve rows. The FAQ answers the legality question instead of dodging it, credits Bypass Paywalls Clean by name and URL, and ends by telling you to buy the subscription.

Then: a six-level cascade whose last two levels cannot execute, which I proved by running it. A share-this-skill script that ships the manual and none of the code, and has done since five minutes after the licence was committed. A `--to-feishu` flag that is parsed and discarded on the exact command both manuals print. 1,838 lines of bundled Feishu code that can only read, for a feature that only writes, whose entry point cannot import, whose single test file imports its three healthy siblings and skips it. A `SKILL.md` that numbers its sections 1, 2, 3, 4, 5, 5, 4, 5, 5 and dates itself three months before the commit that contains it.

None of that is the finding. **The finding is that all of it was fixed already.** On 2026-01-26 — the day after the initial commit — a stranger named Hanson Mei opened a pull request that added a virtualenv, fixed the `python`-vs-`python3` config, dropped the `markitdown[all]` bloat, restructured the agent-facing document, and later contributed bilibili support with a written graceful-degradation clause. Another contributor offered the repository's only 201 lines of tests. A third offered six lines to stop it crashing on Windows. **Nothing was merged.** The maintainer then shipped six more commits to the same two files over three months, and in April rebuilt the bilibili feature from scratch — routing it through a commercial third party and a private endpoint with spoofed Referer headers instead of the public subtitle tool the January patch had already wired up. The feature arrived twice, and the version that shipped is the worse one.

The corpus has spent five consecutive ships on gates: the claim without the test, the gate that cannot fail, the test with no gate, the gate that skips and says so, the gate that is wired and never invoked. v265 concluded that a discipline stops wherever the safe choice costs something. **v266 is the cheaper failure and the more common one: the discipline was already written, already reviewed-ready, sitting in a diff on the same remote — and the door was never opened.** The cost of merging was ten minutes. The cost of not merging was every defect in this document, plus three months of duplicated work, plus a contributor who wrote four commits and got silence.

And the last turn of it: that January patch carries `Co-Authored-By: Claude Opus 4.5`. Another person's agent had already found the problems. So had this maintainer's. Two agent-assisted developers converged on the same fixes three months apart, and the only thing standing between them was a merge button.

**So the question this repository asks is not "did you write tests" or "did you build a gate." It is: what is already sitting in your inbox, correct, that you have not merged — and what are you about to build for the second time because of it?**

For this vault, measured rather than assumed: `main` is at **v226**, and **45 commits — 41 ships and audits, v227 through v265 — are unmerged.** I first wrote "sixty-three, since v204," because that is what the previous ship's next-action said, and v204 through v226 have been merged for some time. **I reproduced this repository's exact defect inside the sentence diagnosing it** — a manifest copied forward, still confidently stated, describing a state that had moved. That is how cheap it is.
