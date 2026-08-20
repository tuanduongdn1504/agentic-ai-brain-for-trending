# (C) Deep Dive — `andyrewlee/awesome-agent-orchestrators` (wiki v253)

> **Written by Claude.** Every number in this document came from a command I ran or a page I fetched in this session. Where I could not establish something, it says NOT ESTABLISHED.
> Analysis date: **2026-08-20**. Subject pinned at HEAD **`78d02e2fbf76891d73178203090dcc5984d89ce9`**.

---

## 0. What it is, in one paragraph

`awesome-agent-orchestrators` is a curated list of **180 tools for orchestrating AI coding agents** — parallel-session managers, autonomous loop runners, issue-queue task runners, multi-agent swarms, control planes, and always-on personal assistants. It is **one Markdown file**. There is no code, no CI, no licence, and no contributing guide: `README.md` is the only file that has ever been tracked in 188 commits across seven months. It has **1.4k stars, 188 forks, 4 open issues and 35 open pull requests** (page-stated). Its maintainer is **Andrew Lee** (`andyrewlee`), a GitHub account with **94 followers** and no stated company, location, or affiliation.

The vault has shipped **252 prior wiki analyses**. **Ten of them are single-line entries in this file.**

---

## 1. Source verification

| Fact | Value | How established |
|---|---|---|
| Clones | **2 independent**, `diff -rq` clean **both ways** | `git clone` ×2 + `diff -rq --exclude=.git` |
| HEAD | `78d02e2fbf76891d73178203090dcc5984d89ce9` | `git rev-parse HEAD` |
| Commits | **188** on HEAD; **209** `--all` | `git rev-list --count` |
| Root commits | **ONE** — `94cf1a36`, **2026-01-19 17:09:23 −0800**, Andrew Lee, *"Add initial awesome list of agent orchestrators"* | `git rev-list --max-parents=0` |
| Newest commit | **2026-08-19** — *"Add Berd to Parallel Coding Agents — Desktop & Web (#165)"* | `git log -1` |
| Files ever tracked | **1** — `README.md` | `git log --pretty=format: --name-only --all \| sort -u` |
| Size at HEAD | **233 lines / 35,639 bytes** | `wc -l`, `wc -c` |
| Tags / releases | **0** | `git tag` |
| Remote refs | 18, incl. `agent/add-comet`, `agent/add-openchamber`, `agent/add-waku`, `codex-add-hcom-to-awesome-list` | `git branch -r` |
| Merge commits | **0** (squash-merge workflow) | `git rev-list --merges --count HEAD` |
| PR-suffixed subjects | **100** of 188, PR numbers **#1–#165** | `grep -cE '\(#[0-9]+\)$'` |

**Contributor identities — D26/D27 applied.** 78 identities at HEAD, 81 across `--all`. **Andrew Lee holds two identities** (`andyrewlee@gmail.com` = 102 HEAD / 117 `--all`; `5784515+andyrewlee@users.noreply.github.com` = 3, `--all` only) ⇒ **120 of 209 `--all`; 102 of 188 at HEAD.** Mendrika and Anno/aannoo also each hold two. **72 of the 78 identities have exactly one commit.** Bus factor is one, by design and by shape.

**Commit histogram (HEAD, 188):** 2026-01 **25** · 02 **34** · 03 **36** · 04 **10** · 05 **5** · 06 **14** · 07 **40** · 08 **24**. A spring trough and a July revival.

⚠️ **Sandbox note:** my first histogram read 50 commits because **zsh silently dropped stdout on the pipeline**. Routing to a file and counting the file gave 188. Every count in this document was settled that way.

---

## 2. ⭐⭐⭐ THE HEADLINE — he diagnosed the exact bias his list suffers from, fixed 127 entries by hand, measured the fix, wrote the standard down **in a commit message**, and the bias came back at 1.93× within three weeks

### 2.1 The diagnosis

Commit **`aeecb0d`**, 2026-07-29, *"Rewrite entry descriptions, add a routing guide, fix stale links (#121)"*. Its message opens:

> *"The list had grown past the point where a reader could compare entries. Descriptions ranged from bare taglines ("A place to create with agents") to 90-word feature dumps, and **length tracked how much each submitter promoted their own project rather than what the tool does**."*

That sentence is the whole finding. In a self-submitted directory, **description length measures promotional effort, not information.** The fix he states:

> *"Rewrite 127 of 134 existing descriptions to lead with mechanism in **~15-25 words**, sourced from live GitHub data and, for the ten entries whose text said nothing usable, from reading the repos directly."*

### 2.2 The fix was real, and I measured it

I extracted `README.md` at three refs and measured the word-count distribution of every entry description (`node`, output routed to a file):

| | entries | median | mean | **max** | in 15–25 band | over 25 | over 45 |
|---|---|---|---|---|---|---|---|
| **Before** (`aeecb0d^`) | 144 | 12 | 17.0 | **74** | 25.7% | 29 | 6 |
| **After** (`aeecb0d`) | 154 | 16 | 15.6 | **31** | 59.7% | **3** | **0** |
| **Now** (HEAD, 22 days later) | 180 | 17 | 18.0 | **72** | 55.6% | **22** | **1** |

The normalization worked: **max 74 → 31 words, over-45 entries 6 → 0, in-band 26% → 60%.** Then the tail went back to 72.

**His arithmetic checks out.** I verified the commit message's own claims against its diff:

- *"Add 11 entries"* — **exactly 11** genuinely new URLs (`background-agents`, `claude-code-action`, `codex-action`, `cyrus`, `gh-aw`, `open-swe`, `OpenHands`, `remote-swe-agents`, `run-gemini-cli`, `omnigent`, `sandbox-agent`). ✅
- *"Fix 15 stale repo URLs"* — **exactly 15**: 12 owner/repo migrations + 3 case-only fixes (`techdufus`→`TechDufus`, `denchclaw`→`DenchClaw`, `lobsterai`→`LobsterAI`). ✅
- *"Five were rebrands"* — all five verified in the diff: `claude-flow`→`ruflo`, `Hephaestus`→`Agentlas OS`, `CoPaw`→`QwenPaw`, `accomplish`→`Coworker`, `claude_code_bridge`→`claude_codex_bridge`. ✅
- *"Drop crystal, which renamed to Nimbalyst and was already listed separately"* — confirmed: `stravu/crystal` is the one URL removed with no replacement, and `nimbalyst` is present. ✅ **This is why my duplicate check returns zero.**
- 144 + 11 − 1 = **154**, matching my measured post-commit count. ✅

⚠️ **One figure I could not reconcile:** *"127 of 134"*. I measure **124** same-URL description rewrites, or **136** including the 12 URL-migrated entries; before the commit there were 129 active + 15 Resting = 144. The gap is most likely a counting convention (whether Resting entries and URL-migrations count as "existing descriptions"). **NOT ESTABLISHED as either right or wrong** — but note that every figure I *could* pin exactly was exact.

### 2.3 ⭐⭐⭐ The controlled experiment: the bias returned at 1.93×

Two populations in the same file, same maintainer, 22 days apart. I matched entries by URL between the post-rewrite snapshot and HEAD:

| population | n | median | **mean words** | max | in band | **over 25** |
|---|---|---|---|---|---|---|
| **Entries he normalized** | 154 | 16 | **15.9** | 41 | 59% | **5 (3%)** |
| **Entries added since** | **26** | 29 | **30.7** | **72** | 35% | **17 (65%)** |

**The incoming population is 1.93× longer and breaches the ceiling at 21× the rate.** Zero entries were removed; zero shrank. The entropy is monotonic.

And it is not only new entries. **Two normalized entries were re-expanded, both by project-affiliated submitters editing their own project's entry:**

- **`310cc43`**, 2026-08-13, author **Илия**, subject ***"docs: expand Agent Teams description (#94)"***. The diff replaces his 20-word normalized entry with a 41-word one whose insertion is a marketing feature list: *"...across Claude Code, Codex, OpenCode, Cursor, Grok, GitHub Copilot, Kiro, Z.AI, MiniMax, Kimi, **200+ models, and 75+ LLM providers**."* **Merged — and `Co-authored-by: Andrew Lee`.**
- **`9182bcc`**, 2026-08-04, author **@aaronjmars**, *"Update aeon entry: 6-harness dispatch, git-persisted memory (#132)"*: 14 → 32 words.

### 2.4 ⭐⭐⭐ The two numbers that settle it

Page-stated stars against entry length at HEAD:

| repo | stars (page-stated) | **words** |
|---|---|---|
| `ruvnet/ruflo` — vault **v42** | **68,400** | **11** |
| `agentscope-ai/QwenPaw` | 34,100 | 19 |
| `BloopAI/vibe-kanban` *(in Resting)* | 27,900 | 10 |
| `superset-sh/superset` | 13,100 | 10 |
| `humanlayer/humanlayer` | 11,300 | 22 |
| `coder/mux` | 2,000 | **7** |
| `andyrewlee/amux` — **the maintainer's own** | 147 | 10 |
| **`intentic/intentic`** | **18** | **72** |

**The 68,400-star project gets 11 words. The 18-star project gets 72.** A ~3,800× spread in adoption, inverted into a 6.5× spread in words.

To be fair to `intentic`: I fetched it and **all five of its specific claims are substantiated** by its own README (per-agent Docker sandbox, outbound-only Cloudflare tunnel, plan mode, per-hunk diff review, the five named harnesses), and its MIT licence is real. **The problem is not accuracy — it is proportion.** The list has no length discipline at submission time, so an 18-star project can buy 72 words while a 68,400-star project gets 11.

### 2.5 ⭐⭐ Why the fix didn't hold — and this is the transferable rule

**The editorial standard exists in exactly one place: the body of commit `aeecb0d`.** There is no `contributing.md` — never has been, in 188 commits. A submitter opening a PR sees a README of 180 entries whose lengths range from 4 to 72 words. Nothing tells them the budget is 15–25 words and leads with mechanism. Nothing measures it.

> ⭐ **THE RULE: a normalization you perform by hand and record only in a commit message is an event, not a standard. Put the budget where the contributor writes, or measure it — otherwise you will re-do it, at the same rate, forever.**

**This is the exact inverse of v252.** There, the instrument shipped and the reading was deleted. Here the *reading* is impeccable — his own measurement, his own diagnosis, his own arithmetic, all correct — and **the instrument was never built.**

---

## 3. ⭐⭐⭐ The list is mechanically immaculate, with zero machinery

This is the finding that cuts against the last five ships. I checked every mechanically-verifiable convention (`node`, results routed to files):

| check | result |
|---|---|
| Entries extracted | **180** — matches the independent `grep -c '^- \['` exactly |
| **Alphabetical order** (case-insensitive), all 8 sections | ✅ **ZERO violations** |
| Duplicate URLs | ✅ **ZERO** |
| Duplicate display names | ✅ **ZERO** |
| Malformed URLs | ✅ **ZERO** — all 180 are canonical `https://github.com/owner/repo` |
| In-document anchor links | ✅ **7 of 7 RESOLVE** |
| `- ` separator present | ✅ **180 of 180** |

The anchor result deserves attention: the two hardest slugs are `Parallel Coding Agents — Terminal (TUI/CLI)` → `#parallel-coding-agents--terminal-tuicli` and `Agent Infrastructure & Primitives` → `#agent-infrastructure--primitives` — **double hyphens, because GitHub deletes the em-dash and the ampersand and leaves the surrounding spaces.** Hand-written, no CI, and correct.

**Contrast v250 directly:** that project shipped **11,305 lines of Python verification** — 1.56× the size of the thing it checked — and its README tree was still missing 14 of 28 type files and 21 of 28 scripts, **with CI green**. This project has **zero lines of verification** and is clean on every check I could devise. ⭐ **Gates are not what produces order here. A maintainer who reviews 100 squash-merged PRs by hand is.**

### 3.1 ⭐⭐⭐ `awesome-lint` would fail this file 21 times and be wrong 21 times

I fetched the authoritative requirements (`sindresorhus/awesome` PR template and manifesto) and tested the mechanical rules:

- **17 entries do not end with a period.** All 17 are **exactly** the 17 Resting entries. In **17 of 17**, the sentence *does* end with a period and is then followed by the italic decay-evidence tag — `_(last commit 2026-03)_`. **The "violation" IS the decay policy.**
- **4 descriptions do not start with an uppercase letter.** All 4 begin with **`tmux`** or **`macOS`** — proper nouns that are correctly lowercase. Capitalizing them would introduce an error.

**Zero of the 21 are genuine defects.** The lint rules that are mechanizable here — trailing periods, leading capitals — are *stylistic*; they carry no truth. Mechanizing them produces 21 false positives against a file that is correct.

> ⭐ This is **v250's decidability rule arriving from the other side.** v250: *you can only compile the part of your standard that becomes a lie when violated.* v253: **when you compile the part that is merely stylistic, the machine is wrong and the human is right.** The rules that matter here — is this entry true, is it proportionate, does it satisfy the scope criterion — are the ones no linter can check.

### 3.2 The requirements it fails are the ones with consequences

Verbatim from the official guidelines I fetched:

| Requirement (quoted) | This repo |
|---|---|
| *"Place a file named `license` or `LICENSE` in the repo root"*; *"We strongly recommend the CC0 license"* | 🔴 **ABSENT — never existed** (one file ever tracked) |
| *"Has contribution guidelines... The file should be named `contributing.md`"* | 🔴 **ABSENT** |
| *"Has a Table of Contents section. Should be named `Contents`"* | 🔴 **ABSENT** — replaced deliberately (see §4.1) |
| *"Run `awesome-lint` on your list and fix the reported issues"* | ⚠️ no CI; NOT ESTABLISHED whether ever run |
| *"Includes the Awesome badge"* | ✅ **PRESENT, line 1** |
| *"Has been around for at least 30 days"* | ✅ 7 months |

**And it is not on the official Awesome list.** I fetched `sindresorhus/awesome` and searched: no entry for `agent-orchestrators`, `awesome-agent-orchestrators`, or `andyrewlee`; the list has no agent-orchestration category at all. The badge on line 1 is a plain image anyone can paste.

> The one requirement it satisfies is the **decorative** one. The two it fails — a licence and contribution guidelines — are the two with real consequences: **nobody can legally reuse the data**, and **the editorial standard is invisible to the people who write the entries.** The second absence is the direct mechanical cause of §2.3.

---

## 4. What is genuinely well-built

### 4.1 ⭐⭐ The inclusion criterion is a real decision procedure

Line 5, verbatim:

> *"Everything here decides **what** an agent works on, **when** it runs, **where** it runs, or **what happens to its output**, and takes whatever task you point it at. Single-purpose bots, and things an agent merely consumes — memory backends, MCP servers, sandbox providers, skill libraries — are out of scope."*

A four-way positive test, a generality test, and a named exclusion list. **It resolves genuinely hard cases correctly.** The sharpest example: *"sandbox providers"* are excluded, but *"where it runs"* is included — so E2B, Daytona and Modal are out, while `sandbox-agent` (*"driving six coding agents inside E2B, Daytona, Modal..."*) and `agenttier` (*"Kubernetes runtime giving each agent its own Pod and PVC sandbox"*) are in. That distinction is not obvious, and the criterion makes it decidable from a candidate's own README.

I stress-tested it on the eight entries most likely to strain it. Two do:

- 🔴 **`skillfold`** (L179): *"Declares skills in YAML and pins exact revisions in a lockfile so installs are reproducible."* A **skill package manager** — and *"skill libraries"* is a **named exclusion**. It decides none of the four things. **Appears to violate.**
- ⚠️ **`codecast`** (L168): *"Watches your real local sessions and surfaces them in a live triage inbox."* Pure **observability** — it watches, it decides nothing. Strongest reading in its favour: a *triage inbox* is a decision surface, so it arguably decides *what happens to output*. **BORDERLINE.** (Note: this is precisely the vault's own CONFIRMED observability sub-archetype, N=12 since v158 — the vault has a name for the class that strains this list's boundary.)

**Two boundary problems in 180 entries (~1%)**, on the entries selected for being hardest. That is a good result.

**The `How to choose` block** (L7–13, added in the same `aeecb0d` commit) routes by **user intent**, not taxonomy — *"Keep an agent working while you're away"*, *"Have agents split a large job between themselves"* — and the commit says it *"doubles as the table of contents"*. It links **7 of the 8 content sections**; Resting is deliberately unrouted. This is why there is no `Contents` section: he replaced a required index with a better one and said so.

### 4.2 ⭐⭐ The `Resting` section — a decay policy that keeps the evidence

L213, verbatim:

> *"A watchlist of projects without a push in the last few months (**checked 2026-07-28**). They stay here until they're active again, then move back up."*

Seventeen entries, **each carrying its own evidence tag**: `_(last commit 2026-03)_`, `_(last commit 2026-05; archived, replaced by Letta Code)_`. This is the **v240 doctrine** — *flag, never remove; evidence, not doubt* — implemented as a section rather than as CI.

**I tested it, and the judgements are sound:**

- **`lettabot`** — claim *"last commit 2026-05; archived, replaced by Letta Code"*. Fetched: **"archived by the owner on May 26, 2026"**, README says *"All new development is happening in Letta Code"*. ✅ **All three components exact.**
- **`vibe-kanban`** — in Resting at **27,900 stars**, with a live banner *"Vibe Kanban is sunsetting."* ✅ **The list rested a project 20× more popular than the list itself.** That is the strongest single piece of evidence that this is curation and not a popularity directory.
- **Rot test on the oldest still-active entries:** of the 9 entries surviving from the root commit with unchanged URLs, **4 have already been moved to Resting**; I fetched the 3 oldest still-active (`superset` 13.1k★, `ralph-tui` 2.4k★, both alive and thriving; `humanlayer` alive). **Zero rot found.**
- ⚠️ **A false finding I caught myself.** I nearly filed `humanlayer` as a policy inconsistency: its newest commit is **2026-06-19**, which is ~2 months before today, while `vibe-kanban` (2026-04) sits in Resting. But the stamp says *checked **2026-07-28*** — and on that date humanlayer's last push was ~5 weeks old, correctly **not** "a few months". **The policy was applied correctly; only the stamp has aged.** ⭐ *Evaluate a dated claim against its own date, not against today.*

**The one real defect:** the stamp has only ever had **two values** — `checked 2026-07-21` and `checked 2026-07-28`. It was refreshed **once, seven days later, and never again** — across the **33 commits since**. Today it is **23 days old**. ⭐ **The decay policy decayed.** Which is the vault's own disease exactly (see §7).

### 4.3 ⭐⭐ The self-listing is the least promotional entry in the file

`amux` (L25) → `github.com/andyrewlee/amux` — **the maintainer's own project**, page-stated **147 stars**.

- **There is no disclosure anywhere.** I grepped the file for `disclos|i built|my own|i maintain|author of|conflict of interest|maintainer of`: **zero hits.** That is a genuine gap.
- **And the behaviour it would police is absent.** The entry is **10 words** — *"Minimal TUI for spawning parallel coding agents in git worktrees."* No feature list, no harness list, no licence brag. Exactly **one** entry in 180 is owned by `andyrewlee`.
- Its history is six versions over seven months, **never leaving the 10-word class** — and in the normalization commit he added the word **"Minimal"** to his own entry, making it *more* modest while cutting 126 others.

Meanwhile a submitted neighbour in the same section runs **72 words and ends with "MIT."**

> Both halves belong in the record: **the disclosure is missing, and the abuse is not there.**

### 4.4 The convention holds with nothing enforcing it

**162 of 188** commit subjects begin with `Add`; **105** match `Add <name> to <Section>`; only **6** use a conventional-commit prefix. Zero merge commits, squash-merged, PR numbers #1–#165.

And there is **evidence of actual gatekeeping**: numbering runs to #165, **100** appear as merged squashes on HEAD, **35 PRs and 4 issues are open** ⇒ roughly **26–30 submissions were closed without merging**. (Approximate: GitHub shares numbering between issues and PRs.) **The list says no.**

---

## 5. ⭐⭐ The curation was bootstrapped by Claude, then handed to a community — and the handover is a clean curve

I counted co-authorship trailers properly (D26: commits vs lines; D27: declared ref population).

**HEAD, 188 commits:** 114 `Co-authored-by:` **lines**; 95 name `noreply@anthropic.com`; **92 commits (48.9%) carry a Claude trailer.**

**Whose commits?** **84 of the 92 are Andrew Lee's own** ⇒ **84 of his 102 commits (82%) were Claude co-authored.**

**Model versions are recorded in the trailers** — a longitudinal record: Claude Opus **4.5** ×32 (Jan–Feb) → **4.6** ×53 (Feb–Apr) → **4.6 (1M context)** ×3 (Apr–May) → **4.7** ×2 and **4.8** ×2 (Jun–Jul).

**And the share collapses monotonically:**

| month | Claude-trailered / total | share |
|---|---|---|
| 2026-01 | 25 / 25 | **100.0%** |
| 2026-02 | 33 / 34 | 97.1% |
| 2026-03 | 26 / 36 | 72.2% |
| 2026-04 | 2 / 10 | 20.0% |
| 2026-05 | 2 / 5 | 40.0% |
| 2026-06 | 3 / 14 | 21.4% |
| 2026-07 | 1 / 40 | **2.5%** |
| 2026-08 | 0 / 24 | **0.0%** |

**The founding quarter was AI-built; the growth quarter is human.** July–August carry the heaviest traffic in the list's history (64 of 188 commits) at ~1% Claude trailers, because those commits are other people's pull requests.

⭐ **This is the cold-start pattern, measured.** The hardest part of an awesome list is the first hundred entries, and that is the part Claude did. Also present: `Co-authored-by: Ubuntu <ubuntu@ip-172-26-15-226.ap-southeast-1.compute.internal>` — an unconfigured cloud box identity, the same species as v252's `Smoke <smoke@example.com>`.

⚠️ **NOT ESTABLISHED:** that the *prose currently in the file* is Claude's. The July normalization (`aeecb0d`), which rewrote 127 descriptions, carries **no** Claude trailer. The trailers establish authorship of commits, not of surviving text.

⚠️ **The `agent/*` branches** — `agent/add-comet`, `agent/add-openchamber`, `agent/add-waku`, `codex-add-hcom-to-awesome-list` — are branch *names*. Their commits are on HEAD authored by **Andrew Lee** (Comet, OpenChamber, Waku, 2026-08-12/13). Suggestive of an agent-assisted submission workflow; **not evidence that the content is AI-written.**

---

## 6. The 180 entries as a dataset

Counted by **entries mentioning** each term (word-boundary matched; `Pi` required delimiter context to avoid substring collisions), out of 180:

**Harnesses.** Claude (any) **55 (30.6%)** · **Codex 52 (28.9%)** · **Claude Code 50 (27.8%)** · OpenCode 26 · Gemini 18 · Cursor 15 · Grok 9 · Pi 8 · OpenClaw 8 · Hermes 5 · Copilot 5 · Antigravity 4 · Aider 3 · Kimi 3 · Kilo 2 · Amp 2 · Goose 2 · Cline/Droid/Qwen 1 each.

> ⭐ **Claude Code (50) and Codex (52) are co-equal first-class targets, with Codex marginally ahead by entry count**; OpenCode is a clear third at half the rate. This is a useful correction to a Claude-centric picture of the ecosystem. **Caveat: this measures what tool authors advertise supporting — not usage, market share, or quality.**

**Mechanisms.** **`worktree` 29 (16.1%)** · memory 13 · sandbox 12 · isolation 12 · kanban 11 · mobile/phone 10 · cron/schedule 9 · approval 9 · diff 8 · verify/test 8 · tmux 7 · Slack 7 · MCP 6 · remote/SSH 6 · Docker 5 · Telegram 5 · GitHub Actions 5 · Linear 4 · graph 4 · PTY 3.

> ⭐ **The git worktree is the load-bearing primitive of the entire category** — nearly 3× the next mechanical primitive, and 4× tmux. Mechanically, "agent orchestration" is mostly **worktree isolation plus a review surface** (diff 8 + approval 9). Only **6 entries mention MCP**, consistent with line 5 excluding MCP servers.

**Shape.** **51 of 163 active entries (31%) sit in one section** — Desktop & Web parallel coding agents. `Autonomous Task Runners` nearly tripled (6 → 17) since July. The modal product is: *a desktop or web app that gives each agent its own git worktree, shows you diffs, and supports Claude Code plus Codex plus OpenCode.*

### 6.1 🔴 The operator-critical gap: licence disclosure is 2.2% and adversely selected

Only **4 of 180 entries (2.2%)** mention a licence:

- `intentic` — "MIT." (verified MIT, **18 stars**)
- `Hivekeep` — "Single container, MIT."
- `iva` — "Self-hosted in one command, MIT."
- `loki-mode` — *"Source-available under BUSL-1.1."* ← the honourable exception: disclosing a **disadvantage**

Meanwhile, the two restrictive licences I happened to check are **both silent**:

- 🔴 **`coder/mux`** — **AGPL-3.0**, 2.0k stars, Coder Technologies. Entry: 7 words, no licence.
- 🔴 **`superset-sh/superset`** — **Elastic License 2.0** (source-available, not open source), **13.1k stars**. Entry: 10 words, no licence.

> **The selection is adverse: small projects advertise permissive licences as a selling point; larger projects with copyleft or source-available terms say nothing.** You cannot filter this list by licence. For an operator whose Goal #2 is a commercial SaaS — and whom the vault has already burned three times on AGPL (**v188** OpenMontage, **v214** firecrawl, **v243** ToolJet) — **every candidate needs a licence check before it goes anywhere near hireui.**

---

## 7. ⭐⭐⭐ Corpus recursion — 10 of the vault's own ships are single lines here

I extracted all 180 owner/repo pairs and matched them against the **complete** vault state (24 files: `CLAUDE.md`, `PATTERN_LIBRARY.md`, `GOALS.md`, all `_state/*.md`, all `_patterns/*.md` — 4,963,794 characters), then pinned each version number by command.

**Confirmed prior numbered wiki subjects — 10:**

| entry | owner/repo | vault | section here |
|---|---|---|---|
| paperclip | `paperclipai/paperclip` | **v14** | Multi-Agent Swarms |
| multica | `multica-ai/multica` | **v15** | Autonomous Task Runners |
| OpenHands | `OpenHands/OpenHands` | **v30** | Autonomous Task Runners |
| ruflo | `ruvnet/ruflo` | **v42** | Multi-Agent Swarms |
| rowboat | `rowboatlabs/rowboat` | **v43** | Personal Assistants |
| gh-aw | `github/gh-aw` | **v48** | Autonomous Task Runners |
| cmux | `manaflow-ai/cmux` | **v99** | Terminal (TUI/CLI) |
| agent-of-empires | `agent-of-empires/agent-of-empires` | **v162** | Terminal (TUI/CLI) |
| ai-maestro | `23blocks-OS/ai-maestro` | **v163** | Desktop & Web |
| Loop Engineering | `cobusgreyling/loop-engineering` | **v189** | Autonomous Loop Runners |

Plus **three vault memory threads** that are not numbered ships: `herdr`, `Archon` (`coleam00/Archon`), `hermes-agent` (`NousResearch/hermes-agent`).

**Two more the vault names but deliberately did *not* ship:**

- ⭐ **`asheshgoplani/agent-deck`** — recorded in vault state as a ***"cataloguing-hazard (v148 lesson)... a different TUI session manager"***. The vault ruled on this entry as a near-miss and declined it. It is here as a plain line.
- **`HKUDS/nanobot`** — the vault's **v233** PIN (*"nanobot is NOT Anthropic's"*, a confabulation the vault caught and discarded). **This list gets it right**: `HKUDS/nanobot`, correctly attributed.

**Interpretation, both directions:**

1. **Independent convergent selection.** An unaffiliated curator applying an explicit written criterion picked **10 of the same projects** the vault chose to analyse in depth — spanning **v14 to v189, 175 versions of vault history**. That is a genuine external validation of the vault's subject-selection instinct.
2. **The more useful direction:** this file is a **163-entry candidate pipeline for the vault's own subject selection, of which 10 are done and 153 have never been touched** — including **66 parallel-agent tools** (15 Terminal + 51 Desktop & Web), which is exactly the niche where the vault has shipped ~20 wikis and **piloted zero**.

⚠️ **Note also what the list does *not* carry:** the vault's warnings. `ruflo` (v42) is 11 words; `mux` is AGPL; `superset` is Elastic-licensed. **That is not a defect** — a one-line directory entry is not the place for a security or licence review, and the list never claims to be. It is a statement of what the list *is not*, and of why the vault's deep dives are not redundant with it.

---

## 8. Code-vs-prose — the 8th consecutive ship, at the limit

The vault has tracked this axis from **v246** to **v252**. This subject is the boundary case: **100% prose, 0% code, by construction.** No CI, no lint, no tests, no scripts, no licence, no contributing guide, no bot, no ToC generator, no link checker.

Applying **v250's decidability rule** — *you can only compile the part of your standard that becomes a lie when violated* — the verdict splits three ways:

1. **Correctly prose.** "Is this entry true?", "does it satisfy line 5?", "is 72 words proportionate to 18 stars?" — none of these are decidable by a machine. Leaving them to a maintainer is right.
2. **Wrongly compiled if compiled.** Trailing periods and leading capitals **are** machine-checkable, and `awesome-lint` would flag **21** of them and be **wrong all 21 times** (§3.1). Mechanizing a stylistic rule buys false positives, not truth.
3. 🔴 **The genuinely checkable, genuinely load-bearing set that nothing checks:**
   - **Link liveness** — 180 URLs, no checker. (Sampled clean, but that is luck plus a diligent maintainer, not a guarantee.)
   - **Description length against the stated 15–25-word budget** — trivially measurable, measurably breached: **65% of new entries** exceed it.
   - **The `checked YYYY-MM-DD` freshness stamp** — 23 days stale, refreshed exactly once in its life.
   - **Whether a Resting entry has become active again** — the policy explicitly promises this and nothing detects it.

> ⭐ **The sharpest reading: the standard that would have prevented the measured regression is neither a gate nor prose — it is simply missing.** It was written once, in a commit message, where no contributor will ever read it. **v250 called unguarded rules "non-negotiable" (a normative overclaim). v252 called unautomated rules "Automated" (a factual overclaim). v253 makes no claim at all — and that honesty is why its one real regression is measurable rather than deniable.**

---

## 9. The v246 `silent` detector — ⚠️ ZERO. The seven-ship streak breaks here

I ran it, routed to a file, counted the file:

```
/usr/bin/grep -rni 'silent' README.md        -> 0 hits (exit 1)
/usr/bin/grep -rni 'silent' --exclude-dir=.git .  -> 0 hits
```

**Zero.** After **seven consecutive replications** (v246→v252, including v252's richest species yet, 22 hits), the detector returns nothing.

⭐ **And the null is informative, not a miss.** The detector finds places where an author noticed that a *failure mode* was invisible. **A curated list has no runtime and therefore no failure modes to be silent about** — the artifact cannot fail confidently, it can only be wrong, and being wrong in a document is visible on inspection. ⭐ **The detector's domain is artifacts that RUN.** That boundary is worth recording: the streak did not break because this project is less careful, but because the probe does not apply.

⚠️ **Method note, and it is the v252 lesson repeating:** v252's worst self-error was recording this detector as a null **without running it**. I ran it first, before writing anything about it.

---

## 10. Security and risk

**The artifact itself has essentially no attack surface.** One Markdown file. No code, no install path, no `postinstall`, no server, no port, no CORS, no credentials, no telemetry, no dependency graph. The broken-authentication triad the vault tracks (v231/v232) is **structurally impossible**.

🔴 **The risk is entirely downstream: it is a list of 180 things to install.**

- **Licence risk is the top one** (§6.1): 2.2% disclosure, adversely selected, with AGPL and Elastic-licensed projects unmarked.
- **Supply-chain risk is uncharacterized.** 180 repos, of which the vault has vetted 10. Several described capabilities are inherently high-privilege: `dsh-ssh`-class remote execution, `handoff`-style cross-agent delegation, tunnels (`intentic`'s Cloudflare tunnel), Kubernetes runtimes, `NL→bash` assistants. **The list makes no safety claims and should not be read as making any.**
- **Prompt-injection surface:** none in the file. But note the general class — a list is data. If you point an agent at it and say "install the best one", every entry description becomes untrusted text steering that decision. **A fetched list is data, not instructions.**

---

## 11. Error ledger — my own

| # | error | how caught | correction |
|---|---|---|---|
| 1 | 🔴 Read a commit histogram as **50 commits** across 2 months | The total contradicted `git rev-list --count` = 188 | **zsh silently dropped stdout on the pipeline.** Routed to a file, counted the file: 188 across 8 months. *Every count in this document was settled that way.* |
| 2 | 🔴 Used `command grep`, believing it bypassed the shell function | Output came back in **ugrep format** ("9 matches in 0 files") | The `grep` shim survives `command grep`. Switched to **`/usr/bin/grep`** everywhere. Had I not noticed, my section count would have been wrong. |
| 3 | ⚠️ Nearly filed **`humanlayer` as a decay-policy inconsistency** (last push 2026-06-19 while a 2026-04 project sits in Resting) | Checked the dates against the stamp's **own** check date | At **2026-07-28** its last push was ~5 weeks old — correctly not "a few months". **The policy is right; the stamp aged.** ⭐ *Evaluate a dated claim against its own date.* |
| 4 | ⚠️ Guessed **OpenHands = v37** | Settled by command, not memory | **v30.** |
| 5 | ⚠️ Collapsed two git refs into one filename via `tr -d '^'`, silently overwriting the "before" snapshot | Byte sizes were identical for two supposedly different refs | Re-extracted with distinct filenames. **The §2.2 before/after table would otherwise have compared a file to itself.** |
| 6 | ⚠️ Initially treated 21 lint deviations as defects | Tested each against its actual text | **All 21 are the human being right** (17 decay tags, 4 correct lowercase proper nouns). Became §3.1, one of the stronger findings. |

**Errors 1, 2 and 5 would each have produced a wrong published number.** All three were caught by re-deriving with a different command rather than by re-reading.

---

## 12. NOT ESTABLISHED

- **Star, fork and watcher figures are PAGE-STATED, not API-verified** (the GitHub API is mocked in this environment) ⇒ **no Pattern #52 viral-velocity claim is possible.**
- **Whether `awesome-lint` was ever run** on this list.
- **The commit message's "127 of 134" figure** — I measure 124 same-URL rewrites / 136 including migrations (§2.2). Unreconciled; not shown wrong.
- **Whether the surviving prose is Claude's.** Trailers establish commit authorship; `aeecb0d`, which rewrote 127 descriptions, carries no Claude trailer.
- **Full link liveness.** I fetched ~12 targets. **168 URLs were not checked.**
- **Whether `QwenPaw` was formerly `CoPaw`** per the target — the repo does not say so; the rename is supported by the same-owner URL migration in this list's own history.
- **Issue and PR *contents*** — only counts were read.
- **Any external discussion** of this list (HN/Reddit/newsletters) — not searched by me.
- **No code was executed** — there is none to execute.

---

## 13. Fleet method

**19-agent `Workflow`**: 6 map lenses → 6 pipelined adversarial contradiction → 3 situating → 3 contradiction-over-situating → 1 synthesis critic. Everything in §§1–9 above is **my own hand verification**, run in parallel with the fleet, per the v250→v252 lesson that the run's worst error is caught only by running the check yourself. The fleet's contribution and its error ledger are recorded in **(C) Verdict**.

⚠️ **Sandbox facts confirmed this session:** `python3` is **SIGKILLed (exit 137)** — even `print("hello")`. **`command grep` does not bypass the `ugrep` shim; use `/usr/bin/grep`.** **zsh silently drops stdout on some pipelines — route counts to a file and count the file.** `git` is 2.19.0 (`--show-current` and `%(trailers:...)` unsupported). `node`, `awk`, `perl`, `sed` work. Some compound `Bash` commands are permission-denied.
