# (C) Deep Dive — `bojieli/ai-agent-book` (v280)

**Subject:** https://github.com/bojieli/ai-agent-book — 《深入理解 AI Agent：设计原理与工程实践》 / *AI Agents in Depth: Design Principles and Engineering Practice*
**Ship:** v280 · 2026-08-25 · GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts 46/12 UNCHANGED
**Licence:** Apache-2.0 (`LICENSE` line 1 = `Apache License`)

---

## 0. Source verification

Two independent clones. **They did not match** — and that is itself the first finding.

| Fact | Command | Value |
|---|---|---|
| cloneA HEAD | `git rev-parse HEAD` | `27d2ab0a441b5d5324535b254180ecf708b20604` |
| cloneB HEAD | `git rev-parse HEAD` | `baa8a8942be92aa7d5ccf0ef7f3558367223bee2` |
| A ancestor of B? | `git merge-base --is-ancestor` | **TRUE** |
| B ahead by | `git rev-list --count A..HEAD` | **1** |

The repository received a push **between my two clones**: `baa8a894`, *"docs(i18n): 第七章译本全文对齐中文版，取消散文式浓缩 (#999)"*, Bojie Li, **2026-08-25 23:12:53 +0800**. All 14 `chapter7` files differ between the clones. Analysis below is anchored to **cloneB**.

### Structural facts (D39-compliant — `rev-list`, never `log | head`)

| Fact | Command | Value |
|---|---|---|
| Commits | `git rev-list --count HEAD` | **1,670** |
| All refs | `git rev-list --count --all` | 2,055 |
| Roots | `git rev-list --max-parents=0 HEAD` | **1** — `c2da26df` *"add web search agent using Kimi API"*, 2025-09-09 |
| Merges | `git rev-list --count --merges HEAD` | 202 |
| Tags | `git tag \| wc -l` | 3 (`latest`, `v1.0`, `v1.2`) |
| Remote branches | `git branch -r \| wc -l` | 268 |
| Tracked files | `git ls-files \| wc -l` | **11,713** |
| Authors | `git shortlog -sne --all \| wc -l` | **91** |
| Size | `du -sh . / .git` | 2.0 G / 754 M |

Top authors: Bojie Li **879**, Santh 212, whanyu1212 109, Thejesh 81, santhreal 72, Hanyu 44, `github-actions[bot]` 43. Author age: 2025-09-09 → 2026-08-25 (**~11.5 months**). HEAD is PR **#999**.

### What it is

A ten-chapter engineering book on building AI agents, in **14 languages**, with **109 companion experiment directories** carrying runnable code, an evidence-status regime, and CI. Author **Bojie Li** — by his own introduction, **Chief Scientist at Pine AI** (org `19PINE-AI`, whose repos `TalkAct` and `rlvp` are pinned as experiment targets), lecturer at 图灵《AI Agent 实战营》 and 中国科学院大学. **Not Anthropic** (§41 — (a) FAILS).

---

## ⭐⭐⭐⭐⭐ 1. THE SPINE

> **Every check in this repository compares one copy to another copy. Nothing compares a claim to the tree.**

The discipline here is real and unusually high — the CI comments are among the best-reasoned in the corpus, the evidence standard is the strictest I have read, and the counts were **exact twice**. But every gate was pointed at *agreement*, and none at *truth*. I found the same mechanism at **five independent sites**.

### Site 1 — CI computes the right number on every run and never compares it to the front page

`README.md` publishes **two different experiment counts on one page**:

- `108 个配套实验` (prose)
- `**103 个** 配套实验（含本地项目与外部复现轨道）` (table)

Disk holds **109** chapter subdirectories (`ls -d chapter*/*/ | wc -l`).

And `scripts/check_i18n_consistency.py` — run by CI on every push and PR — computes a **fourth** number. Its check 5 counts, per chapter README, the rows matching `^\|.*\| [✅📖🚧]+ \|`, then:

```python
total_zh = sum(zh_counts.values())
print(f"  中文基准：{total_zh} 项目，分布 {[zh_counts[n] for n in CHAPTERS]}")
```

I ran that predicate myself: **118** (✅ 99 runnable + 📖 15 external-reproduction + 🚧 4 design-doc).

That number is **printed in the CI log of every single run**. It is never compared to the README that publishes 108 and 103.

**And the claim was born exact.** Measuring the claim against the derivation at every commit that touched it (`git log -G"[0-9]+ 个配套实验" -- README.md`):

| commit | date | README claims | rows CI derives | |
|---|---|---|---|---|
| `2ed3f298` | 2026-07-21 | **88** | **88** | ✅ exact |
| `2c2c832d` | 2026-07-22 | **92** | **92** | ✅ exact — *"Fix stale project counts"* |
| `049fd34d` | 2026-07-30 | 94 / 94 | 93 | ❌ −1 |
| `8c2b7f55` | 2026-07-31 | 95 / 95 | 105 | ❌ −10 |
| `ba57d72e` | 2026-08-17 | 103 / 103 | 113 | ❌ −10 |
| `686d1a59` | 2026-08-24 | 107 / **103** | 115 | ❌ and now **internally split** |
| `78f70d18` | 2026-08-25 | 108 / **103** | **118** | ❌ −10 / −15 |

⭐ The number was right while one person could hold it in his head, and has never been right since. The two copies agreed through five updates and split on **2026-08-24**, when one was bumped to 107 and the other left at 103. ⚠️ Note the trap: **99 ✅ + 4 🚧 = 103**, so a reader can "derive" the published number with the *wrong* definition.

> ⚠️ **Never cite an experiment count for this repo from the README.** The derivable figure is **118 table rows / 109 directories**, depending on which you mean — and you must say which.

### Site 2 — 13 translations condensed the book, and the structure stayed perfect

The commit that landed mid-clone says it plainly:

> 译本此前在若干节把中文版的多段内容压缩成一两段散文，其中最突出的是「失败归因」一节：**中文版的 9 行错误分类表在 13 个语种里全被改写成了一段概述**。散文式浓缩不是有意的体例。

I measured the parent commit and HEAD myself:

| edition | table rows **before** | **after** | sections before | after |
|---|---|---|---|---|
| `book/chapter7.md` (zh source) | **39** | 39 | 49 | 49 |
| `book-en`, `book-ja`, `book-ko`, `book-es` … | **28** | **39** | **49** | 49 |

⭐⭐⭐ **The section count was already identical — 49 — in all fourteen editions, before and after.** Thirteen translations kept every heading and dropped **11 rows out of the middle of them**. No structural check could ever have seen it. (49 = h2 13 + h3 33 + h4 3 — I derived it; the author's stated figure is exactly right.)

**And the gate that exists for this is triggered by the book and does not read it.** `i18n-check.yml` fires on `book*/**`. The script it invokes:

```
$ grep -n "book" scripts/check_i18n_consistency.py
0 matches            # exit 1
```

Its six checks read `README.md`, `docs/<locale>/README.md`, `docs/<locale>/LEARNING.md` and `chapterN/README[.locale].md`. **It never opens a single file under `book/` or `book-*/`.**

⚠️ The fix commit touched **only the 14 book files** — `git show --name-only baa8a894 | grep -c "^scripts/\|^\.github/"` = **0**. It installed no check. The invariant it declares (*"13 个语种的节数（49）、表格行数（39）… 与中文版完全一致"*) is **true at HEAD in all 14 editions — I verified it — and guarded by nothing.** A normalization recorded only in a commit message is an event, not a standard.

### Site 3 — the 14th language is invisible to the gate that exists to check languages

`discover_locales()` builds the locale list from `docs/<locale>/README.md`. `ls docs/` returns 13 locales: `ar en es hu id ja ko ru ta tr vi zh-CN zh-TW`. **There is no `docs/he`.** Hebrew's README lives at the repository root as `README.he.md`.

⇒ **Hebrew never enters the list, and is exempt from all six checks** — while `book-he/` is a complete 14th edition and the front page advertises 14 languages. `README.he.md` *is* an explicit trigger path of `i18n-check.yml`; the script it runs has no code path that reads Hebrew.

⭐ The script's own docstring states the cause: *"核心原则：**自动发现语言，不硬编码**"* — auto-discover, don't hardcode. Auto-discovery keyed on a path convention does not report a language that breaks the convention as non-compliant; it **cannot see it at all**.

### Site 4 — two experiments are "Complete" and their evidence was never committable

`docs/EXPERIMENT_STATUS.md` sets the strictest evidence bar in the corpus:

> *Statuses in this file describe evidence **retained in the repository**. … Cloning a pinned source repository, installing its dependencies, or passing a smoke test does not establish that an experiment is complete.*

Two rows cite evidence that is not there:

| row | linked evidence | on disk |
|---|---|---|
| **7-3** *"**Complete.** … full scope in the [saved evidence](…/full_7_3_structured_rubric_evidence.json)"* | `chapter7/…/results/full_7_3_structured_rubric_evidence.json` | **MISSING** |
| **7-4** *"**Complete.** … in the [saved campaign](…/full_7_4_60_cases_costed.json)"* | `chapter7/…/results/full_7_4_60_cases_costed.json` | **MISSING** |
| 7-11 (control) | `full_7_11_60_case_matrix.json` | **EXISTS — 14,959,594 bytes** |

`git log --all -- <path>` returns **nothing** for both: they were never committed at any point in history.

⭐⭐⭐ **And `.gitignore` explains exactly why.** Line 4 blanket-ignores `results/`. At the bottom sits a hand-built allowlist, commented *"Canonical Chapter 7 evidence. Keep ad-hoc run outputs ignored while making the renamed complete matrix … visible to normal `git add` workflows"*:

```
!/chapter7/user-memory-system-evaluation/results/
/chapter7/user-memory-system-evaluation/results/*
!/chapter7/user-memory-system-evaluation/results/full_7_11_60_case_matrix.json
!/chapter7/user-memory-system-evaluation/results/live_7_11_matrix_layer1.json
```

It names 7-11. **It does not name 7-3 or 7-4.** The status file says the evidence is retained; the ignore file made retaining it impossible. Both statements are sincere; nothing compares them. *(The defect is a missing allowlist entry, not a wrong rule — and nothing can see an entry that was never added.)*

### ⭐⭐⭐⭐⭐ Site 5 — the capstone: a test named for this exact job, scoped past it

`tests/test_docs_experiment_status_links.py` exists. Its docstring names the failure class outright:

> *"Closes the class where … **linked ledger files could drift out of existence**."*
> `test_ledger_links_resolve_to_existing_files`: *"**Every** ledger link in the detailed-ledgers section must point to a real file."*

Its regex:

```python
_LEDGER_LINK_RE = re.compile(r"^- \[.+?\]\((\.\./.+?\.md)\)$", re.MULTILINE)
```

Three clauses gut it — the link must be a **bullet at line start**, must end in **`.md`**, and must **end the line**. The broken links are `.json` targets **inside table cells**:

```
| 7-3 | Local implementation | **Complete.** … with full scope in the [saved evidence](../chapter7/…/full_7_3_structured_rubric_evidence.json). |
```

I counted what it sees:

| | count |
|---|---|
| `../` links in `EXPERIMENT_STATUS.md` | **53** |
| matched by the regex | **7** (13%) |
| non-`.md` targets — categorically invisible | **31** |

⭐ **The author identified the precise failure class, wrote a test for it, and scoped the regex to the one section where it had never happened.** All 7 checked links resolve, so the test is permanently green. ⚠️ And it lives in `tests/`, which only runs when `chapter1/web-search-agent/**`, `agentbook/**`, `tests/**` or `pyproject.toml` change — **a docs-only edit to the file it checks does not trigger it.** Wrong scope *and* wrong trigger.

---

## 2. The CI coverage seam

The only job running the root suite is the `agentbook` job in `web-search-agent-tests.yml` → `python -m pytest tests -q`. Its trigger paths are exactly `chapter1/web-search-agent/**`, `agentbook/**`, `tests/**`, `pyproject.toml`, and its own file. **`chapter2/` … `chapter10/` are not triggers.**

Yet the suite tests all of them. `tests/test_ch10_werewolf_wolf_vote_tie_consensus.py:5-10`:

```python
ch10_werewolf = Path(__file__).resolve().parent.parent / "chapter10" / "voice-werewolf"
sys.path.insert(0, str(ch10_werewolf))
from werewolf.game import Judge
```

**D34 against real history:** of **94** non-merge commits touching `chapter10/`, **78 (83%)** touched no test-triggering path. *(An independent fleet agent measured 89/103 = 86% including merges; both land in the same band. Extent: `rev-list --no-merges HEAD -- chapter10/`, first 400.)*

Test-file distribution by chapter: ch1 3, ch2 2, ch3 7, ch4 5, ch5 5, ch6 10, ch7 9, ch8 10, ch9 11, ch10 8 — **70 of 86 files test chapters whose directories cannot trigger them.**

⚠️ **Count correction on myself:** I first reported **739** test functions using `^def test_` plus the indented form. An adversarial verifier caught the omission and I confirmed it with my own command — **33 `async def test_` functions** were excluded. **The definitional count is 772.** The same trap this arc keeps finding, this time in my own pattern.

### The renumber residue

The 2.0 restructure merged old ch4-async + old ch9-multimodal into a new chapter 6, shifting 6/7/8 → 7/8/9. Chapter titles are consistent at HEAD. But four tests keep `ch9` in their filenames while importing from `chapter6`:

```python
# tests/test_ch9_qwen2_acoustic_events.py:7
ch9_streaming = Path(__file__).resolve().parent.parent / "chapter6" / "streaming-speech"
```

⭐ The **variable is still named `ch9_streaming` and points at `chapter6`.** The paths were corrected because they must resolve or the test fails; the names were not because nothing reads them. One pair (`phone_agent_redact_secrets_non_serializable`) is byte-identical under both numbers and therefore runs twice.

⚠️ Same class: `chapter6/EXPERIMENT_LEDGER.md` **exists on disk (2.5 K)** but is absent from `EXPERIMENT_STATUS.md`'s "Detailed ledgers" list, which names chapters 1, 2, 3, 4, 5, 7, 8. **The chapter created by the restructure is the one missing from the index** — and the link test cannot detect a missing entry, only a broken one.

---

## ✅ 3. What is genuinely excellent

This is a high-discipline repository and the failures above are the failures of a careful person outrunning his own hand-maintenance. In fairness:

- **⭐⭐⭐ The evidence regime publishes negative results as `Complete`.** This is rare and valuable. Verbatim from `EXPERIMENT_STATUS.md`: *"**Complete; accuracy uplift not observed**"* (4-1) · *"**Complete; strict joint-advantage hypothesis not observed**"* (5-16) · *"**Complete; the distillation uplift hypothesis was not supported**"* (8-9, with `baseline 1/24, student 2/24, teacher 23/24, nonsignificant paired improvement (p=1.0)`) · *"**the full subjective ordering was not reproduced** … C > B > A did not reproduce because A outscored B"* (6-6) · 7-12 publishes a **4.4828%** success rate including evaluator failures.
- **⭐⭐⭐ It refuses to over-claim.** 7-12: *"Candidate Qwen differs from the paired-source Doubao model, so the result establishes neither same-model uplift nor noninferiority."* 10-3: *"The invalid Gemini credential required TalkAct's supported Anthropic Sonnet caller override, so this same-family configuration **must not be silently pooled with upstream default-Gemini results**."*
- **⭐⭐ A clean D32 declaration.** *"This table is a selective operational ledger, not a second numbered index. **Each chapter README remains the authoritative ordered experiment list.**"* — declaring which copy wins, inside the copy that loses.
- **⭐⭐ The CI comments are among the best-reasoned in the corpus.** `provider-adoption-tests.yml` names its three deliberate exclusions (`chapter2/kv-cache`, `chapter2/agent-skills-ppt`, `chapter4/multimodal-agent`) with the specific blocker for each, and sets API keys to **empty rather than unset** because *"a resolver bug that reads a key from the runner environment must fail here, not silently pass."*
- **✅ Security surface is clean.** All actions version-pinned; explicit `permissions:` on all 7 workflows; **no `pull_request_target`**; `deploy-pages.yml` guards publication with `if: github.repository == 'bojieli/ai-agent-book'`. The only key-shaped strings in 11,713 tracked files are fixtures in the repo's own **redaction tests** (extent: `sk-…`/`AKIA…` patterns over `*.py|*.md|*.json|*.sh`).
- **⭐ `.env.example` leads with zero-cost options** — an uncommented `OPENROUTER_MODEL=google/gemma-4-31b-it:free` default and Ollama — and names the one experiment that genuinely cannot be substituted (chapter 1's Kimi `$web_search`). **The default configuration costs nothing.**
- **⭐ 58 of the tests encode a specific discovered bug**, with the failure named in the docstring (fleet finding; consistent with the files I read).

---

## 4. Intellectual content

The thesis, from `book/introduction.md`, is a single formula: **Agent = LLM + 上下文 + 工具** — *brain + eyes + hands*, mapped to RL as *Policy / Observation Space / Action Space*. Ten chapters: 1 入门 · 2 上下文工程 · 3 用户记忆和知识库 · 4 工具 · 5 Coding Agent 与通用 Agent · 6 交互 · 7 评估 · 8 模型后训练 · 9 持续进化 · 10 多 Agent 协作. 7,386 lines of Chinese prose.

Two claims matter to this vault:

- **⭐⭐⭐ 实践在前，命名在后 — "practice comes first, naming comes after."** He claims Pine independently arrived at dynamic prompt loading *before* "Skills", CLI-execution tools to fight tool-list bloat, a status-bar technique, Claude-Code-like harness methods *before* "harness", and proposer–reviewer *before* "loop engineering". *(This is the author's priority claim from production experience; the repository is not evidence for the priority itself. Corpus cross-refs: v238 — Anthropic ships the mechanism as `defer_loading`; v189 loop-engineering.)*
- **Chapter 5's thesis: Coding Agent + filesystem is the technical foundation of all general agents**, with OpenClaw as the worked case. Directly on goal #1.
- Chapter 7: *"没有评估，就无法判断一次改动带来的提升究竟源于设计本身，还是仅仅来自随机波动"* — without evaluation you cannot separate design improvement from noise.

**AI authorship is disclosed, in the introduction**: the book was written by **whisper coding (口述式协作)** with Pine's voice agent — *"这本书不仅讨论 Agent，也记录了一种由 Agent 深度参与的知识生产方式."* ⚠️ But the disclosure is partial: `cursor-chats/` holds **269** published transcripts, and exactly **1** commit in 2,055 carries an AI trailer — `baa8a894`, the HEAD commit, `Co-authored-by: Claude Opus 5 (1M context)` plus a `Claude-Session:` URL. A book about agents, whose newest commit was written with Claude Opus 5, repairing the book's own translations.

---

## 5. Pattern #57 — corpus-recursive, N=3 in one subject

Pinned experiment targets that are prior corpus subjects (extent: `github.com/...` URLs across `chapter*/**/*.md`):

| dependency | corpus |
|---|---|
| `NousResearch/hermes-agent` | **v227** hermes-webui, **v268** hermes-desktop |
| `unslothai/unsloth` (7 refs) | **v245** (revisit) |
| `browser-use/browser-use` (8 refs) | **v41** |

⭐ Experiment **9-8** hands **the entire ten-chapter book plus Hermes's own source code to Hermes**, with no supplied gap list, and asks it to improve itself. It chose to add evidence-backed learning signals to persisted trajectories, was rejected by three fresh terminal reviewers, corrected each defect, and got `VERDICT: ACCEPT` on the fourth. The ledger then records, honestly: *"remains unmerged; the proposed downstream ablation campaign was not run."* The experiment idea came from a **reader**, credited by name (Grace).

Also pinned: `openclaw/openclaw` (11), `anthropics/skills` (7), `19PINE-AI/TalkAct`, `microsoft/magentic-ui`, `google-research/android_world`, `sierra-research/tau2-bench`, `volcengine/verl`, `huggingface/trl`.

---

## 6. Method

**Fleet:** 11 dimensions × (read → adversarially refute) = **22 agents, 22 completed, 0 errors, ~2.83 M subagent tokens, 546 s.**

The adversarial layer did real work, in both directions:

- ⭐ **It corrected me** on the test count (739 → **772**, missing `async def test_`) and surfaced the 7-3/7-4 evidence gap and the Hebrew exemption — all three of which **I then re-derived with my own commands** before using them.
- ⭐ **I refuted the fleet** on the central count: both the reader and its refuter concluded *"108 is correct."* My historical derivation shows the CI-derived figure is **118** and the claim has not matched since 2026-07-30.
- ⚠️ **One reader fabricated line citations** (the pilot dimension — `EXPERIMENT_CONVENTIONS.md` / `EXPERIMENT_STATUS.md` line numbers off by 10–100+, some beyond file length). Its *thematic* conclusions were sound and are used; **none of its line numbers are cited in this document.** Another reader miscounted top contributors by ~40% and misread 268 total branches as 268 codex branches. Every number in this document is from my own command output.

⚠️ **A hazard I hit myself, worth recording.** In zsh, `git show "$rev:chapter$n/README.md"` silently returns the **wrong file** — `$rev:c…` triggers the `:c` history modifier. It returned 4 lines where the correct file has 22, and produced a table of zeros I nearly reported. `git show "${rev}:chapter${n}/README.md"` is correct. *(Candidate method rule: brace every variable preceding a colon in a git revspec — a counting method that fails silently, per D51.)*

**Extent not overcome:** no network access — star counts, the GitHub Trending badge, PR review threads and upstream claims are **unverified**; `python3`/`pip` are SIGKILLed in this sandbox, so **nothing was executed** — the 772 tests were read, never run, and no experiment was reproduced; the 2.0 GB tree means several negatives rest on scoped searches whose extent is stated inline.

---

## 7. Verdict summary

**GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL (Pine AI, not Anthropic; §41 — no inference from notability) · (b) **STRONG** (a ten-chapter engineering book on building agents; Claude 82× / Anthropic 60× in the Chinese source; Claude Code a named reference architecture; ch5 = coding-agent-as-foundation; ch7 = evaluation methodology) · (c) STRONG · (d) STRONG. No §40, no override.

**NO MINT.** Books and curricula are consistently declined in this corpus — **v197** mlsysbook, **v191** AI-For-Beginners, **v270** Foundations-of-LLMs, **v220** little-book-rl — on domain-not-capability. The genuinely distinctive artifact is the **evidence-gated companion-experiment ledger**, but that is a documentation *practice*, not a capability class, and not world-first (ACM artifact evaluation, ML reproducibility checklists, papers-with-code precede). **Recorded as the audit-reviewable §C-2 candidate, not minted** — the v279 handling.

**Counts 46/12 UNCHANGED; §C-1 13, §C-2 39 UNCHANGED.**

**Recorded, not self-executed:** Pattern **#57 at N=3 in one subject** (Hermes v227/v268 · unsloth v245 · browser-use v41) · **T3 Education tier** instance-strengthening · the evidence-ledger **§C-2 candidate** · the zsh-revspec method-rule candidate.

**Streak:** v279 `GA:136` → **`GA:137 · OG:13 [7 ov]` — 60 consecutive GA v220→v280.** §35 CLEAR ({v278, v279, v280} = 0 OG). Override review **20th consecutive discharge**.

**Artifact:** https://claude.ai/code/artifact/d5eb5324-4ca3-4f51-84fe-e1699462655b
