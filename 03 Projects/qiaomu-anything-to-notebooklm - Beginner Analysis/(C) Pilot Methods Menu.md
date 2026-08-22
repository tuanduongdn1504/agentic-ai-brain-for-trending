# (C) Pilot Methods Menu — v266 qiaomu-anything-to-notebooklm

> Companion to the Deep Dive. **Overall verdict: ⭐ READ-AND-BORROW. Do not install.**
> Rungs are ordered by increasing footprint. Rungs 0–4 install nothing and touch no credential.

---

## Why not install — the assembled risk, not any one piece

Each element below is individually defensible. The install path assembles all of them:

| Element | Where | What it means |
|---|---|---|
| `notebooklm login` | `install.sh:94`, `SKILL.md:100` | Per the vault's own **v7** wiki: **Playwright-driven browser OAuth** (Chrome/Edge) against your real Google account, persisted as `storage_state.json`, wrapping *"undocumented Google APIs subject to breaking changes"*. |
| Unpinned third-party MCP server | `install.sh:49` | `git clone https://github.com/Bwkyd/wexin-read-mcp.git` — no tag, no commit, no `--depth` — then **registered as an MCP server Claude executes** (`install.sh:111-116`). Whatever HEAD it has on your install day. |
| Unpinned `pip install git+` | `install.sh:94` | `notebooklm-py` from a git URL, **into your system Python — no virtualenv.** |
| A hand-extracted commercial JWT | `get_podcast_transcript.py:12,57` | `~/.claude/skills/getnote/tokens.json`, 90-day refresh token, *"Re-initialize from browser"* — **no documented procedure exists in the repo.** |
| Crawler impersonation | `fetch_url.sh:141-142` | `User-Agent: …Googlebot/2.1…` **plus** `X-Forwarded-For: 66.249.66.1` against 54 named publishers. |
| **No confirmation gate** | `SKILL.md` (all 742 lines) | Greps for confirmation language return **one** hit — a default, not a gate. For cost/quota language: **zero**. v7's skill, which this wraps, gates `generate *` and `download`. |

⭐ **And the capability you'd want it for already exists properly**: corpus **v7** `teng-lin/notebooklm-py` ships the same NotebookLM skill first-party, MIT, with the trust boundary. If the goal is "document → podcast," pilot v7, not this.

---

## Rung 0 — Read six things, in order (20 min, zero footprint)

1. `SKILL.md:161-175` — the natural-language→intent table and the *"if no explicit instruction, upload only"* default. **The best design decision in the repo.**
2. `main.py:113-182` — `generate_questions_progressive`. **The best code in the repo** (see Rung 3).
3. `main.py:266` beside `main.py:339` — the four-parameter signature and the three-argument call. The dropped flag.
4. `scripts/fetch_url.sh:327-380` — read `:351` and then read what is below it.
5. `package.sh:23-30`, then run `git show --stat bdaef0e`. The array *is* the initial commit.
6. `git log --format="%h %ad %s" --date=short refs/remotes/pr/1 ^main` (after `git fetch origin refs/pull/1/head:refs/remotes/pr/1`) — **the actual headline.**

---

## ⭐⭐⭐ Rung 1 — Turn the finding on the vault: a merge counter, not a linter (30 min)

This ship's rule is that the correct fix sat in a diff and nobody opened the door. **Measured on this vault, not assumed:**

```bash
git log --oneline main -1                                # → e0459f1 v226 code-review-graph
git rev-list --count main..HEAD                          # → 45
git log --format=%s main..HEAD | grep -cE '^v[0-9]+ '    # → 41   (v227 … v265)
```

**`main` is at v226. Forty-five commits unmerged; forty-one ships and audits, v227 through v265.**

⭐ And the vault's standing instruction about it is itself stale in exactly this ship's way: the shim's next-action reads *"review + merge the chain (v204 → … → v265, in order)"*, but **v204–v226 are already merged.** That sentence has been copied forward across dozens of ships while the fact beneath it moved — `package.sh:23-30` with a different filename.

**Do:**
1. Rewrite the next-action to derive its range from `git rev-list`, not from the previous ship's prose.
2. Add to `CLAUDE.md` a single line recording `git rev-list --count main..HEAD`, and a threshold above which a new ship does not start.

Ten lines. Cheapest instance of the finding, and it is about us. **Composes with v265's Rung 1** (the export-boundary path check) and **v263's Rung 1** (`(C) proposed-verify-vault-inventory.sh` has nine clauses and nothing invokes it) — all three are the same shape: machinery or work that exists and is not reached.

---

## ⭐⭐ Rung 2 — Steal the trust boundary (from v7, not from v266) (30 min)

The reusable artifact is in the corpus already, at `03 Projects/notebooklm-py - Beginner Analysis/02 Wiki/(C) Skill Integration (Claude Code + Codex + OpenClaw).md`, §5:

> **Runs without confirmation:** read-only (status, list, view) · setup (auth, profile, context) · ephemeral (unsaved queries) · background waits
> **Requires confirmation:** **destructive** (`delete`) · **expensive** (`generate *` — cost + time) · **filesystem** (`download` — writes local disk) · **persistence** (`--save-as-note`)

That four-way classification — *read-only / setup / expensive / persisting* — is a complete, portable trust model for skill authoring.

**Do:** add it as a **required section** to the vault's `05 Skills/` authoring guidance, then audit the vault's own nine skills against it. v266 is the counter-example that earns the rule: **a wrapper that is more autonomous than the tool it wraps, having removed a boundary the vault had already flagged as worth mirroring.**

⚠️ Note the copy-forward exposure v259 handed forward applies here: `05 Skills/` holds re-versioned copies, so decide *where* this rule lives before writing it, or it will reach one file and not the others.

---

## ⭐⭐ Rung 3 — Lift the progressive-questioning module into vault practice (45 min)

`main.py:113-182` is directly usable as a **prompt pattern**, no install, no dependency:

- **Round 1 — overview (4):** summarize purpose · enumerate structure module-by-module · list core claims with supporting text · **name the 3–5 most counter-intuitive things**.
- **Round 2 — depth (5), with a distinct set per content type:** for books/documents — decompose the argument (premises → reasoning → conclusion) with quoted passages · inventory the evidence and its role · **find internal contradictions or explain why the argument holds** · state the single core insight in one sentence · **make the sharpest available criticism**.
- **Round 3 — synthesis (3):** the one belief a reader should change · extract 3–5 actionable principles · three reasons to persuade someone to read it.

Two techniques worth keeping:
- ⭐ **The anti-web-search clause.** Every question ends *"完全基于文档回答"* / *"不要搜索网络"*, and the docstring says why: *"防止 NotebookLM 触发网络搜索"*. That is a real insight about a specific tool's failure mode — **the general form is: name the tool's escape hatch and close it in the prompt.**
- ⭐ **The referent helper.** `label_for` (`:98-110`) exists solely so questions read naturally — "本书" for a book, "这期播客" for a podcast, "这条推文" for a tweet. Small, and it makes every one of the twelve questions better.

**Do:** run the three rounds by hand against one corpus document and compare round 3's output against a single-shot summary. If it wins, add it to the vault's reading practice. **Zero risk.**

---

## ⭐⭐ Rung 4 — Extend the export-boundary check to distribution manifests (45 min)

v265's Rung 1 proposed asserting that every vault-internal path reference resolves. v266 adds the second half: **assert that every file a packaging or publishing path claims to ship is actually shipped.**

`package.sh` is the specimen — a manifest that was correct for five minutes and wrong for seven months, with nothing in either repository able to notice, because a list of filenames that *exist* is valid; it is the list of files that *should be there* that no checker holds.

**Do:** add a clause to `(C) proposed-verify-vault-inventory.sh` that diffs "files a publish path enumerates" against "files the publish path's own directory contains." Then **wire the script to something** (v263's Rung 1) so the clause can fire.

---

## ⭐ Rung 5 — If you actually want the capability, pilot v7 instead (60 min)

`teng-lin/notebooklm-py` — corpus **v7**, MIT, ~11k★ as recorded at v7, `notebooklm skill install`, and the confirmation gate built in.

Fence it anyway:
- a **throwaway Google account** with nothing in Drive;
- a **virtualenv**, and a **pinned version** (v7 recorded v0.3.4 / 1–2 week cadence — check the current tag);
- run `notebooklm auth check --test` and read what it stores before pointing it anywhere;
- one document you own, and read the generated artifact before generating a second.

Its own README warns it wraps undocumented Google endpoints and may break without notice. That is a stability warning, not a safety one — but it means **do not build anything load-bearing on it.**

---

## 🔴 NEVER

- Run `install.sh` on a machine with a Google account you care about.
- Register `Bwkyd/wexin-read-mcp` as an MCP server without reading its code first — it is unpinned and Claude executes it.
- Run `fetch_url.sh` against a publisher's site. It impersonates Googlebot **and** claims Googlebot's IP.
- Cite the **"300+ 付费网站"** or **"~50 站"** figures. Measured: **54** unique domains across all five lists; **22** in the Googlebot list. (The `~4` and `~10` figures *are* right.)
- Treat `--to-feishu` as functional on any path but a plain URL.
- Read `✅ 分析完成！` as meaning a Feishu document was created.
- Read *"archive.ph needs human verification"* as meaning archive.ph was the problem — **every** failure emits that message, including for URLs that were never paywalled.
- Expect `main.py` to handle WeChat, YouTube, Office, images, audio, ZIP or search. The classifier knows thirteen types; the dispatcher implements five.
- Assume the bundled Feishu MCP works. It cannot write, and its entry point does not import.

---

## Composition with live vault threads

| Thread | How v266 touches it |
|---|---|
| **RATIFIED candidate-LLM legibility ADR** | Rung 2's four-way autonomy classification is directly addable: *which operations may a candidate-facing agent perform unattended, and which require a human?* v266 is the counter-example; v7 is the template. |
| **v265 Rung 2 — "which of my safe defaults were free?"** | v266 answers it from the other side: v7's confirmation gate was **free** to keep and was dropped anyway, in a re-implementation. **A safe default can be lost by duplication, not only by cost.** |
| **v263 / v265 Rung 1 — the un-invoked inventory script** | Rung 1 and Rung 4 both extend it. Three consecutive ships have now handed this vault machinery for its own invariants, and it is still not wired. |
| **CC memory / skills threads** | v7's skill (`~/.claude/skills/notebooklm`) and this one compete for the same intents in different languages. If both are installed, an English "make this a podcast" matches both. Worth knowing before installing either. |
| **hireui** | **No component here is usable.** The only transferable artifact is Rung 2's trust boundary, applied to candidate data. |
