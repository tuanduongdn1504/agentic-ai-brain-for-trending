# (C) Deep Dive — `bradAGI/awesome-cli-coding-agents` (wiki v254)

> **Built 2026-08-20.** Source verified: **two independent clones, `diff -rq` clean BOTH ways**, HEAD `6e307e73e040c0be58abe2b024fc6aabae2c6e58`.
> Written by Claude. Every number below carries the command that produced it. Where something could not be established, it says so.

---

## 0. What it is, in one paragraph

`bradAGI/awesome-cli-coding-agents` — *"A curated list of **110+ CLI coding agents** — AI-powered tools that live in your terminal, read/edit repos, and run commands — plus the **harnesses** that orchestrate, sandbox, or extend them."* One Markdown file of **300 entries** across 6 sections, a banner PNG, a 192-line Python script, and a 41-line GitHub Actions workflow that runs **every Monday**, re-fetches every entry's star count from the GitHub API, re-sorts each section by stars, and stamps the date. **Four files, ever.** **No licence, ever.** 125 commits, one root (2026-02-06), 37 identities, effectively one maintainer.

**This is the direct sibling of v253** (`andyrewlee/awesome-agent-orchestrators`, 180 entries, one file, *zero* machinery) — and that makes v254 the controlled comparison v253 was begging for: **what does machinery actually buy a curated list?**

The answer is unusually clean, and it is the headline.

---

## 1. Source verification and the shape of the repository

```
two clones → diff -rq --exclude=.git  → 0 differences  (both directions)
HEAD                = 6e307e73e040c0be58abe2b024fc6aabae2c6e58
git rev-list --count HEAD   = 125      (= --all; one branch)
git rev-list --max-parents=0 --all → 0b3d5227  2026-02-06 19:53:59 -0500  Brad  "add README"   (ONE root)
git tag | wc -l     = 0
git rev-list --merges --count HEAD = 33
```

**Every file that has ever been tracked** (`git log --all --diff-filter=A --name-only`, 4 results):

| File | Size |
|---|---|
| `README.md` | 688 lines / 86,453 bytes |
| `banner.png` | 1,350,506 bytes |
| `scripts/update-stars.py` | 192 lines / 5,703 bytes |
| `.github/workflows/update-stars.yml` | 41 lines / 1,047 bytes |

**No `LICENSE`. No `contributing.md`. No tests. No `CLAUDE.md`, no `AGENTS.md`, no agent-facing surface of any kind.** A grep for `licen|copying` across every path ever added returns **zero**.

**Identity census** (`git log --format='%an <%ae>' | sort | uniq -c`, 37 identities):

- `Brad <46579244+bradAGI@users.noreply.github.com>` — 40
- `Brad <began2007@gmail.com>` — 30
- `bradAGI <46579244+bradAGI@...>` — 2
- **Brad total = 72 of 125 (57.6%)** ⚠️ *three identities — vault rules D26/D27 apply; a single-address count understates him by 44%*
- `github-actions[bot]` — 20
- **the other 33 identities have exactly ONE commit each.** 72 + 20 + 33 = 125 ✓

**Bus factor one**, same as v253 (which had 72 of 78 single-commit identities).

> ⚠️ **A grep for `bot` in commit authors/subjects returns 21, not 20.** The 21st is `dc0241c … "Add OpenClaw ecosystem section with nanobot, NullClaw, …"` — **`nanobot` contains `bot`.** The true bot count is **20**.

---

## 2. ⭐⭐⭐ THE HEADLINE — the machinery fetches the answer to every question the list gets wrong, parses it into memory, and reads one field

### 2.1 What the machine is aimed at, it does perfectly

Six sections are declared sortable in the script (`SORTED_SECTIONS`). Measured across all 300 entries:

| Section | Entries | Unstarred | **Descending-star violations** |
|---|---|---|---|
| Open Source | 83 | 0 | **0** |
| OpenClaw ecosystem | 12 | 0 | **0** |
| Closed Source | 16 | 7 | **0** |
| Session managers & parallel runners | 61 | 6 | **0** |
| Orchestrators & autonomous loops | 41 | 0 | **0** |
| Agent infrastructure | 87 | 0 | **0** |

**Zero violations in 300 entries.** Unstarred entries sit at the bottom of every section, exactly as the script's `key()` function dictates (`return (0, -stars) if stars is not None else (1, 0)`). The invariant is not just satisfied — **the file's structure is a fingerprint of the code that produced it.**

And **the numbers are real.** I fetched three rendered GitHub pages (the API is mocked in this sandbox; rendered pages are not):

| Entry | Page-stated, live 2026-08-20 | README (written 2026-08-17) | Verdict |
|---|---|---|---|
| `openclaw/openclaw` | **386,827** | `387k` | ✅ exact under the script's own `round(n/1000)` rule |
| `anthropics/claude-code` | **142,065** | `142k` | ✅ exact |
| `NousResearch/hermes-agent` | **233,195** | `232k` | ✅ 0.4% drift — 3 days of growth |

⭐ **v253's standing PIN was "never cite its star figures as verified." v254's ARE citable, to within one weekly refresh.** That is exactly one thing, and the machinery bought it well.

### 2.2 What the machine is not aimed at is broken — and the API handed it the answer

`fetch_stars()` is the whole story. Line 49:

```python
return json.load(resp).get("stargazers_count")
```

The **entire** `GET /repos/{owner}/{repo}` response is parsed into a dict, one key is selected, and the rest is discarded on the next line. The documented response body for that endpoint also contains `archived`, `full_name`, `pushed_at`, and `license` — **four fields, in memory, in the same object, thrown away.** Each one is the answer to a defect the list actually has:

| Discarded field | The defect it would have caught | Verified state |
|---|---|---|
| `archived` | **A dead project in the active list.** `letta-ai/lettabot` (327★) sits in Open Source with no marking. | 🔴 I fetched it: GitHub page title reads **"Archived - has been replaced by Letta Code channels/schedules!"**, page shows *Read-only*. |
| `full_name` | **Stale names after a rename.** | 🔴 `ruvnet/claude-flow` (68,000★, the 2nd-biggest entry in its section) **redirects to `ruvnet/ruflo`**. Also `paoloanzn/free-code` → **`freecodexyz/free-code`**. |
| `pushed_at` | **Dormancy.** There is no decay policy of any kind — no `Resting` section, no per-entry date, nothing. | v253, *with no machinery at all*, has one: a dated `Resting` section with per-entry evidence. |
| `license.spdx_id` | 45% of entries state no licence. The machine could have filled every one. | 134 of 300 silent (see §5). |

⭐⭐⭐ **And v253 caught lettabot.** Its hand-maintained `Resting` section listed it with per-entry evidence — *archived 2026-05-26, replaced by Letta Code* — which the vault verified three days ago. **v254 has weekly CI and lists it as live; v253 has no CI and retired it correctly.** A star count is the one signal an archived repo keeps.

⭐⭐ **And v253 caught the rename too.** Its 2026-07-29 pass verified five rebrands *by name*, `claude-flow`→`ruflo` among them. **v254's maintainer did a rebrand pass on the very same day** (`126e206`, *"…rename Hephaestus to Agentlas OS…"*) — fixed that one, missed this one, and it is still stale 22 days later.

### 2.3 The five duplicates, and the dict that would have caught them

**300 entries, 295 unique URLs.** Five duplicate pairs — **every one adjacent, every one byte-identical:**

| Repo | Lines | Section |
|---|---|---|
| `genai-io/san` | 188, 190 | Open Source |
| `rustykuntz/clideck` | 348, 350 | Session managers |
| `jo-inc/pi-reflect` | 602, 604 | Agent infrastructure |
| `knaisoma/data-olympus` | 618, 620 | Agent infrastructure |
| `neul-labs/grite` | 636, 638 | Agent infrastructure |

Byte-identical adjacent lines are a machine signature, not human error — two people writing the same entry would write different sentences. **I traced all five through the full history.** The duplicate count over 125 commits:

```
0b3d522  2026-02-06   95 entries   0 duplicates
   …          …           …             0
4820306  2026-07-27  242 entries   0 duplicates
126e206  2026-07-29  260 entries   5 duplicates   ← Brad, non-merge, parent 4820306
7e59e44  2026-08-01  261            5
58f6bf0  2026-08-01  261            5
b433ac5  2026-08-03  261            5   ← bot rewrite
0e01e31  2026-08-10  261            5   ← bot rewrite
151476e  2026-08-13  300            5   ← Brad, +39, "refresh all star counts"
6e307e7  2026-08-17  300            5   ← bot rewrite (HEAD)
```

**Zero for 5.7 months and 242 entries. Then 5, in one commit, and never again zero.** The commit: `126e206`, 2026-07-29, *"Add 17 entries from reviewed PRs and issues; rename Hephaestus to Agentlas OS; refresh star counts"* (+144/−108).

**The file has been completely machine-rewritten four times since** (three bot runs plus one human-run refresh), each one re-fetching ~295 repos and re-sorting every section. All four preserved the duplicates exactly. ⭐⭐ **And because the sort keys on stars, identical entries sort adjacent every single time — the machine actively holds them side by side, in the one arrangement a human reader would most easily notice.**

**The script has the answer.** Line 107:

```python
if parsed and parsed not in repos:
    repos[parsed] = None
```

`repos` is a dict keyed by `(owner, repo)`. Building it *is* deduplication. Twelve lines later:

```python
print(f"Fetching stars for {len(repos)} repos…", file=sys.stderr)
```

⭐⭐⭐ **Every Monday for 17 weeks the job has printed a number that disagrees with the file it is editing** — `295` against 300 entry lines — and nothing compares them. One `if` statement, on data already in hand, already being printed.

### 2.4 ⭐⭐ The mechanism: transcription, not merging

Why did five duplicates appear in one commit? The commit subjects give it away. There are **nine batch commits**, seven of them phrased *"from reviewed PRs"*:

```
151476e 2026-08-13 Add 39 reviewed entries and refresh all star counts
126e206 2026-07-29 Add 17 entries from reviewed PRs and issues; rename Hephaestus…
facc151 2026-07-13 Add 7 entries from token-usage leaderboard review
1ace6e2 2026-07-13 Add 20 entries from reviewed PRs
83c66fe 2026-07-02 Add 5dive, AgentPack, RoleCraft from reviewed PRs
6d71410 2026-06-29 Add 21 entries (tier 1 & 2 from reviewed PRs); update DvalinCode
c0ee24a 2026-06-17 Add 28 entries from reviewed PRs across all sections
7d0367a 2026-05-15 Merge 7 PRs: 9 new agents + harnesses
9078ddd 2026-05-02 Merge 4 PRs: Aeon, Crab Code, AgentPlane, Not Human Search
```

He **reads** contributor PRs and **re-types** their entries into his own commit. He also has 33 real merge commits. **Every duplicate came from a transcription batch; not one came from a merge.** Three of the five re-added entries were his own from six weeks earlier (`c0ee24a`); one was a contributor's from April (`3d22bf5`, Or Kuntzman); one was his own from 16 days before (`1ace6e2`).

⭐⭐⭐ **Git already knows what is in the file. Reviewing a PR and then hand-copying its contents is the one workflow that discards that knowledge.** v253's maintainer squash-*merged* 100 PRs and had zero duplicates.

**One arithmetic note, in his favour and against:** `151476e` says *"Add 39 reviewed entries"* and the entry count goes 261 → 300 = **exactly 39** ✓. `126e206` says *"Add 17"* and the count goes 242 → 260 = **+18** — off by one.

---

## 3. ⭐⭐ The count claim is hand-maintained, bumped five times, and exactly right

I expected "110+" against 300 entries to be stale. **It is not — and three separate fleet agents misread it the same way I first did.** The sentence's grammar is precise: *"110+ CLI coding agents … **plus** the harnesses."*

```
Terminal-native coding agents:  83 + 12 + 16 = 111   ← "110+"  ✓
Harnesses & orchestration:      61 + 41 + 87 = 189   ← "plus"
                                        total = 300  ✓
```

**111 agents. The claim is exact and correctly scoped.** Its history (`git show $h:README.md | grep 'curated list of'` across all 125 commits) shows it hand-bumped in five separate commits:

```
2026-03-13  "CLI coding agents"        (no number)
2026-03-13  "80+ CLI coding agents"
2026-06-17  "90+ CLI coding agents"
2026-08-01  "100+ CLI coding agents"   ← commit 58f6bf0, subject: "Update agent count to 100+"
2026-08-13  "110+ CLI coding agents"
```

⭐⭐⭐ **So the real structure of this project is a three-way split, and it is not "machine good, human bad":**

- What the **machine** was aimed at (stars, sort order, the date stamp) — **correct, verifiably.**
- What the **human declared** (the agent count) — **correct, because he bumps it by hand, five times.**
- What **nobody declared and nothing was aimed at** (uniqueness, liveness, rename-freshness) — **broken.**

**He never claimed the entries were unique. So neither the human nor the machine was watching.** That is v250's rule — *a gate's aim, not its quality, decides what rots* — with the declaration itself revealed as a form of aim.

---

## 4. ⭐⭐⭐ The v253 length-vs-promotion finding replicates — with a better instrument, and a much weaker claim

v253's headline was that entry length tracked how hard each submitter wanted to promote their own project, measured against **hand-typed** star counts. v254 lets the same association be measured against **weekly machine-fetched** ones.

Measured over the 287 entries that have both a star count and a description (`indexOf('—')`, i.e. the **first** em-dash — see the error ledger):

```
median 25.5 words   mean 27.6   min 5   max 71
over 30 words: 120 of 300 (40.0%)     over 40: 62 (20.7%)
Spearman(stars, words) = -0.24        Pearson(log10 stars, words) = -0.20
```

| Star bucket | n | mean words | max | over 40w |
|---|---|---|---|---|
| ≥ 100k | 7 | **19.3** | 28 | **0** |
| 10k–100k | 55 | 24.9 | 62 | 13 |
| 1k–10k | 63 | 24.0 | 56 | 12 |
| 100–999 | 58 | 28.5 | 65 | 13 |
| < 100 | **104** | **31.2** | **71** | **21** |

**The seven most-starred projects average 19.3 words and not one exceeds 28. The 104 least-starred average 31.2, and 21 of them exceed 40.** Headline pair: **`openclaw` 387k★ = 19 words; `Agent AFK` 51★ = 71 words** — a 7,588× spread in adoption inverted into a 3.7× spread in words.

⭐⭐ **And the structural consequence is specific to this list: it sorts by stars. So the file gets systematically wordier as you scroll — the most self-promoting entries are concentrated at the bottom, which is exactly where a maintainer's attention runs out.** Position and promotional pressure are correlated *by construction*.

### ⚠️ The honest statistical read — the fleet's critic was right to push here

**A Spearman of −0.24 on n=287 is statistically significant but explains roughly 6% of the variance.** The bucket means (1.6×) are a far clearer signal than the coefficient. And the *causal* story — that length tracks self-promotion — is **v253's maintainer's own diagnosis of his own list**, stated in his own commit message. I cannot establish it here. A perfectly innocent alternative fits this data: **niche low-adoption tools genuinely need more words to explain what they are.**

So the defensible claim is narrow and still worth having: **the association replicates independently, in a different list, by a different author, against verified star counts.** What v253 supplied was the mechanism; what v254 supplies is the second measurement. Do not upgrade that into a claim about motive.

**Fair to `Agent AFK`, the 71-word entry:** it is describing a genuinely multi-part tool, and nothing in it is false. As with v253's `intentic`, the problem is **proportion, not accuracy**.

**And unlike v253, there is no budget to breach.** v253's maintainer wrote *"~15-25 words"* into a commit message. v254's Contributing section says only *"**1–2 line description** — what it does, who it's for."* ⭐ **v253 had a budget nobody enforced and landed at mean 18; v254 has no budget at all and sits at mean 27.6.** That is the cost of not writing the number down, measured.

---

## 5. 🔴 The operator-critical number — and here v254 beats v253 by 25×

v253's finding was blunt: licence disclosure **4 of 180 = 2.2%**, and **adversely selected** — MIT advertised as a selling point while AGPL and Elastic stayed silent.

**v254: 166 of 300 entries name a licence = 55.3%.**

| Licence named | Entries |
|---|---|
| MIT | 108 |
| Apache-2.0 | 43 |
| closed / proprietary / source-available | 10 |
| **AGPL** | **5** |
| **PolyForm** | **3** |
| SUL-1.0 | 1 |
| GPL | 1 |
| **BUSL-1.1** | **1** |

⭐⭐⭐ **The adverse selection is gone.** Eleven restrictive-licence disclosures, including `tlbx` (101★) declaring **AGPL-3.0** and `TeDDy` (**4★**) declaring AGPL. A four-star project stating AGPL is disclosure for its own sake, not marketing. **A clean Pattern #83 positive, ×11.**

And the rate is **U-shaped, not adverse**: ≥100k = 71%, 10k–100k = 45%, 1k–10k = 49%, 100–999 = 53%, **<100 = 70%**. The *smallest* projects disclose most.

⭐⭐ **Independent #83 cross-confirmation:** `asklokesh/loki-mode` discloses **BUSL-1.1** in **both** lists. Two curated lists, two authors, same honourable disclosure of a disadvantage.

### 🔴 But you still cannot filter this list by licence — for a different reason

The silence is concentrated at the top. **10 of the 20 most-starred entries name no licence:**

```
232k Hermes Agent — SILENT      198k OpenCode      — SILENT
 92k Pi           — SILENT       84.3k OpenHands   — SILENT
 68k Open Interpreter — SILENT    68k claude-flow  — SILENT
 66.3k Cline      — SILENT       64.3k Warp        — SILENT
 52.9k Goose      — SILENT       48.3k Aider       — SILENT
```

Not adverse selection — **incomplete coverage where the stakes are highest.** The vault has been burned by AGPL three times (v188 / v214 / v243). **Verify the licence yourself, every time.** And note the irony: `license.spdx_id` is in the very API response the script already parses.

---

## 6. The 300 entries as a dataset — two prior-ship findings corrected

Word-boundary matched over the whole entry line (`\bClaude Code\b`, not substrings).

### Harnesses named

| Harness | Entries | % of 300 |
|---|---|---|
| Claude (any form) | **140** | **46.7%** |
| **Claude Code** | **119** | **39.7%** |
| **Codex** | **104** | **34.7%** |
| OpenCode | 49 | 16.3% |
| Gemini | 43 | 14.3% |
| Cursor | 36 | 12.0% |
| Pi | 19 | 6.3% |
| OpenClaw | 18 | 6.0% |
| Copilot | 17 | 5.7% |
| Grok | 12 | 4.0% |

⭐ **v253 concluded Claude Code and Codex were "co-equal, Codex marginally ahead" (50 vs 52 of 180).** On this larger, differently-scoped sample **Claude Code leads Codex by 15 entries (119 vs 104), and "Claude" appears in nearly half of all 300.** Both lists agree these two are the top pair by a wide margin with OpenCode a clear third — that finding is now N=2 and solid.

⚠️ **Limitation, and the fleet's critic was right to name it: this measures what authors ADVERTISE, not what anyone uses.** A silent entry is not evidence of harness-agnosticism.

### Mechanisms named

| Mechanism | Entries | % |
|---|---|---|
| **MCP** | **53** | **17.7%** |
| skill(s) | 45 | 15.0% |
| memory | 28 | 9.3% |
| **worktree** | **26** | **8.7%** |
| sandbox | 25 | 8.3% |
| isolation | 21 | 7.0% |
| hook(s) | 17 | 5.7% |
| subagent | 16 | 5.3% |
| tmux | 12 | 4.0% |

⭐⭐⭐ **This corrects v253's strongest generalisation.** v253 found `worktree` at 29/180 = 16.1% and called the git worktree *"the load-bearing primitive of the whole category."* Here it is **8.7% — half the rate — and MCP is #1 at 17.7%** where v253 measured MCP at just 6/180 = 3.3%, a **5× difference in the other direction.**

**Not a contradiction — a scoping correction.** v253's list was specifically about *orchestrating parallel agents*, where worktree isolation **is** the mechanism. v254's list is about *the agents themselves and their harnesses*, where the mechanism is **capability injection**. Together: **parallelism is solved with git worktrees; capability is solved with MCP and skills.** The load-bearing primitive depends on which problem the tool solves, and *"of the whole category"* over-reached.

⭐⭐ **A corpus benefit for the vault's own Pattern #18 B1-MCP sub-archetype (≈N=13): across 300 CLI-agent tools, MCP is the single most-named mechanism.** That is ecosystem-scale evidence, not another instance.

---

## 7. ⭐⭐⭐ Corpus recursion — a new record, 16 prior ships, spanning 206 versions

Matched by **exact `owner/repo` pair** against 4,996,866 characters of vault state (`CLAUDE.md` + 21 `_state/` and `_patterns/` files): **28 of 282 pairs present.** Then adjudicated — a mention is not a ship (v253's fleet inflated exactly this from 10 to 29). **16 are numbered vault ships:**

| Ship | Entry | Line | README stars |
|---|---|---|---|
| **v9** | `bytedance/deer-flow` — DeerFlow | 410 | 80.1k |
| **v15** | `multica-ai/multica` — Multica | 286 | — |
| **v30** | `All-Hands-AI/OpenHands` | 58 | 84.3k |
| **v36 / v228** | `badlogic/pi-mono` — Pi | 56 | 92k |
| **v42** | `ruvnet/claude-flow` — *(now `ruflo`)* | 412 | 68k |
| **v48** | `github/gh-aw` | 520 | — |
| **v52** | `code-yeongyu/oh-my-openagent` | 62 | 68k |
| **v72** | `Hmbown/CodeWhale` — *(formerly `deepseek-tui`)* | 70 | 40.8k |
| **v99** | `manaflow-ai/cmux` | 294 | — |
| **v144** | `headroomlabs-ai/headroom` | 496 | 66.6k |
| **v150** | `getpaseo/paseo` | 296 | 14k |
| **v162** | `njbrake/agent-of-empires` | 312 | — |
| **v177** | `Kilo-Org/kilocode` | 82 | 26.9k |
| **v179** | `jo-inc/camofox-browser` | 516 | — |
| **v195** | `langchain-ai/openwiki` | 510 | — |
| **v215** | `xai-org/grok-build` | 84 | 25.5k |

**16 ships, v9 → v215 = 206 versions of vault history. The prior record was v253's 10.**

⭐⭐⭐ **And the vault has already cited this exact list — twice — without ever analysing it.** `grep -c "awesome-cli-coding-agents"` over vault state returns **2**, both in the **v223 openinterpreter** entry, as evidence that *"harness-engineering is a recognized 2026 field."* The subject was a citation at v223 and is the subject at v254. (`bradAGI` returns **0** — the author is new to the corpus.)

⭐⭐ **Two methodological false-negative classes I had to close, both worth recording:**
1. **Renames defeat pair-matching.** `Hmbown/CodeWhale` is v72 under a new name; `ruvnet/claude-flow` is v42 under an old one.
2. **The vault often names a ship without its owner path.** `All-Hands-AI/OpenHands` never appears as a pair in vault state — only as "OpenHands v30" — so exact-pair matching missed it entirely.

### Cross-list overlap: seven repos the vault knows only from v253

`coder/mux`, `superset-sh/superset`, `johannesjo/parallel-code`, `asheshgoplani/agent-deck`, `andyrewlee/amux`, `madarco/agentbox`, `cfal/garcon` — all appear here **and** in v253's list, and the vault knows every one of them from *analysing the other list three days ago*. Including:

- ⭐ **`johannesjo/parallel-code`** — v253's Rung 2 pilot pick (MIT, worktree + built-in diff viewer). **Its author, Johannes Millan, submitted it here himself** (`git log --author='johannesjo'`).
- ⭐ **`andyrewlee/amux`** — **v253's own author's tool.** And it collides: **`amux` appears twice as two different projects**, `mixpeek/amux` (line 342) and `andyrewlee/amux` (line 352). A name collision of exactly the cataloguing-hazard class the vault recorded at v148.
- ⭐ **`asheshgoplani/agent-deck`** — the near-miss the vault explicitly ruled on and declined.
- ⭐ **`HKUDS/nanobot`** (line 218) — the v233 PIN. Listed correctly.

⭐⭐ **Neither list links to the other.** Seven shared entries, two adjacent domains, zero cross-reference.

### One precise cross-check the vault can make and the list cannot

⚠️ **`OpenInterpreter/open-interpreter` (line 60) is the confusable twin the vault warned about, not the ship.** v223's subject was `openinterpreter/openinterpreter` (no hyphen) — a different, newer repo — and the vault pinned in bold: *"NOT the famous 2023 Python 'Open Interpreter.'"* **This list carries the twin and not the ship.** That is not a defect in the list; it is a demonstration that the vault's own disambiguation was worth writing down.

---

## 8. Editorial quality — one strong defect and three unsourced extraordinary claims

### 🔴 The third-most-starred entry is contradicted by its own repository

**README line 50** (195,000★, position #3 in Open Source):

> *"Clean-room Python/Rust rewrite of Claude Code architecture using **oh-my-codex**; **fastest repo in GitHub history to 100K stars**. Born from the **March 2026 Claude Code source leak**. MIT."*

**`ultraworkers/claw-code`'s own GitHub tagline, fetched:**

> *"An agent-managed museum exhibit, built in Rust with **Gajae-Code / LazyCodex** — developed and maintained with no human intervention."*

- A grep for `fastest|100K stars|source leak|leaked` on the repo's own page returns **zero hits**.
- The tooling attribution differs (`oh-my-codex` vs `Gajae-Code / LazyCodex`).
- *"An agent-managed museum exhibit"* is not *"a clean-room rewrite that set a GitHub record."*

⚠️ **"Fastest repo in GitHub history to 100K stars" is NOT ESTABLISHED**, and the vault has a standing prior against this claim class: its DSH YouTube thread records that **no authoritative GitHub velocity record exists**. The list asserts one as fact.

⚠️ **"The March 2026 Claude Code source leak" is asserted as settled fact in THREE entries** (lines 50, 108, 160), and one adds *"includes discoveries from the source leak (KAIROS persistent assistant, buddy system)."* **I cannot verify that any such leak occurred.** The list catalogues three projects whose stated premise is derived from allegedly leaked proprietary source, with no qualification anywhere.

✅ **In fairness — one extraordinary claim checks out near-verbatim.** README: *"Fork of Claude Code with all telemetry removed, guardrails stripped, and all experimental features enabled."* The repo's own tagline: *"The free build of Claude Code. All telemetry removed, security-prompt guardrails stripped, all experimental features enabled."* **Substantiated.** (Its owner is stale: `paoloanzn` → `freecodexyz`.)

⚠️ **But note what that means: the list catalogues, in its main Open Source section with no warning of any kind, a build of Claude Code with its security guardrails deliberately stripped** — confirmed by the project itself. That is the v209 dual-use class, presented neutrally. **Presence in this list is not a safety signal.**

### Liveness sample

**22 URLs fetched, spread across the star range; all HTTP 200. Three defects (13.6%):** `lettabot` archived-but-listed-active, `claude-flow`→`ruflo` stale owner, `paoloanzn/free-code`→`freecodexyz` stale owner. **278 URLs remain unchecked** — do not generalise this rate.

---

## 9. ⭐⭐⭐ `awesome-lint` would fail this file ~13 times — and be RIGHT 6 of them. That inverts v253.

v253's finding was that all 21 of its lint deviations were **lint being wrong**. I ran the same battery here.

**Where lint would be WRONG (7):**

- **6 lowercase description starts** — and every single one is a proper noun that *must* stay lowercase: `xAI's official…` (84), `tmux-based harness…` (302), `macOS daemon…` (384), `macOS TUI…` (390), `macOS GUI harness…` (402), `macOS and Windows…` (404).
  ⭐⭐⭐ **v253 found exactly 4, all `tmux` or `macOS`. Two lists, two authors, 10 instances, 10 of them `macOS`/`tmux`/`xAI`. That is an independent N=2 establishing that a capitalization rule is *systematically* wrong on a technology catalogue** — technology names are disproportionately lowercase-initial. The rule is not misapplied here; the rule is defective for this domain.
- **1 missing trailing period** — line 622, a description ending in a backticked `pip install …` command. Cosmetic at worst.

**Where lint would be RIGHT (6):**

- 🔴 **5 duplicate entries.** awesome-lint has a no-duplicates rule. It would fire five times and be correct five times.
- 🔴 **No `LICENSE` file.** Required.

**Where it passes cleanly:** 0 malformed URLs · 0 missing em-dash separators · ToC named **`Contents`** ✓ (line 24) · **9 of 9 anchors resolve**, including the two hard slugs where GitHub drops the `&` and keeps a double hyphen (`#harnesses--orchestration`, `#session-managers--parallel-runners`) · the Awesome badge is present on line 8.

⭐⭐⭐ **THE SYNTHESIS ACROSS THREE SHIPS. v250: you can only compile the part of your aesthetic that becomes a lie when violated. v253: compile the merely-stylistic part and the machine is wrong while the human is right. v254 completes it — they BUILT the machine, aimed it at the one decidable thing nobody doubted, and left both decidable-and-actually-broken things unchecked.** Duplicates and a missing licence are trivially machine-decidable. Star ordering was never in question. **The machinery went to the certainty and not to the risk.**

### 🔴 And the licence badge is a claim, not just an absence

README line 11 renders `img.shields.io/github/license/bradAGI/awesome-cli-coding-agents`, hyperlinked to `/blob/main/LICENSE`. **No `LICENSE` file has ever existed.** v253 had no licence and no badge — an absence. **v254 has no licence and a badge advertising one, pointing at a path that has never resolved.** With no licence, all rights are reserved by default: **nobody can cleanly fork 300 curated judgements**, and the badge suggests otherwise.

---

## 10. What is genuinely well built

1. ⭐ **The inclusion criterion is three explicit tests**, not a topic label: *"Must have a **CLI or terminal interface** (IDE-only tools don't qualify) · Must be able to **read/write code or run commands** autonomously · Link must point to a **valid, active** project (no dead repos)."* All three are decidable from a candidate's own README. ⚠️ **The list violates its own third test** — `lettabot` is archived.
2. ⭐ **The taxonomy earns its six sections.** Agents split Open Source / OpenClaw ecosystem / Closed Source; harnesses split Session managers / Orchestrators / Infrastructure. The OpenClaw section exists because that ecosystem (387k★) generated a dozen distinct agents — a defensible editorial call, made in one commit (`dc0241c`).
3. ⭐⭐ **The date stamp is machine-maintained and honest.** The workflow's `Bump "Last updated"` step `sed`s in the run date every Monday. **v253's equivalent stamp had exactly two values in its entire life and was 23 days stale.** v254's is 3 days old because a machine writes it. *This is machinery working.*
4. ⭐ **The CI history is clean.** 20 bot runs. The first four (2026-04-21, 04-26, 04-27, 04-30) are 5/1/3/4 days apart — manual `workflow_dispatch` while building it — then **every Monday from 2026-05-04 to 2026-08-17 without a gap.** No `continue-on-error`, no `|| true`.
5. ⭐ **The closed-source entries are handled honestly.** 16 entries, 7 with no star badge because they are not GitHub repos, sorted to the bottom by the script's own rule. `CodeAgentSwarm` discloses *"Closed source, account required; Pro free during the open beta (€6.99/mo after)"* — **an actual price**, which v253's fleet had to fabricate.

---

## 11. ⭐⭐ Provenance — the exact inverse of v253

**Exactly 4 `Co-Authored-By: Claude` trailer lines in 125 commits** (`grep -ci` on `%B` bodies; 4 lines, 4 commits — **D26: lines ≠ commits, verified separately**). Models named: Opus 4.6 ×2, Opus 4.6 (1M context) ×1, Sonnet 4.6 ×1. Plus one `Made-with: Cursor`.

⭐⭐⭐ **All four belong to outside contributors, not the maintainer:**

```
92e430d  Ethan Steininger    Add amux (mixpeek/amux)
3397ef0  maheshwar kanitkar  Add Praman — CLI agents for SAP UI5/Fiori
f08b6a4  Duys                Add Forge - autonomous spec-driven development loop
465e306  oxgeneral           Add ORCH — CLI agent orchestrator
```

**Brad's 72 commits carry zero AI trailers.** The root commit — 95 entries, 251 lines — is a bare `add README` with no body at all.

⭐⭐⭐ **v253: 92 of 188 commits (48.9%) carried a Claude trailer, 84 of them the maintainer's own — its founding quarter was 100% AI-built and its busy quarter was human PRs. v254 is the mirror image: the maintainer uses no AI and his contributors' PRs are the Claude-assisted ones. The AI sits on the opposite side of the transaction.**

⚠️ **Do not draw the tempting causal line.** It is n=2, and the cleanliness difference tracks the **merge strategy** (squash-merge with per-PR review vs. hand-transcribed batches), which I traced directly, not the AI usage.

⭐ **One contributor is an agent.** `e583490`, 2026-04-16, author **`OpenClaw Agent (basd) <basd@openclaw.ai>`**, subject *"Add skill-optimizer to Agent infrastructure."* Its diff adds `fastxyz/skill-optimizer` — *"benchmarks SDK, CLI, and MCP guidance docs (SKILL.md) across multiple LLMs … Iteratively rewrites docs until every configured model meets a PASS/FAIL score floor."* **An AI agent autonomously submitted, to a human-curated list, a tool for optimizing agent instructions.**

⚠️ Two unconfigured-machine addresses — `雷浪声 <…@leilangshengdeMacBook-Pro.local>` and `maheshwar kanitkar <…@Aparnas-MacBook-Air.fritz.box>` — the same species as v252's `Smoke <smoke@example.com>` and v253's `Ubuntu <ubuntu@ip-…compute.internal>`. **Third consecutive ship.**

### Who actually wrote this list

Entry lines added, by author class (`git show $h -- README.md | grep -c '^+- \*\*\['` per commit):

- **Brad: 833** of 2,962 added entry-lines (28.1%)
- bot: 2,096 (re-writes, not additions)
- **outside contributors: 33 (1.1%)**

⭐⭐⭐ **Only 33 of the 300 entries came from outside; Brad added the other ~267.** This is a **maintainer-authored list with a thin contributor layer** — the opposite shape from v253's community list. That single fact explains the transcription batches, the duplicates, the zero AI trailers on his side, and the bus factor.

**Self-submission:** 15 of the 33 contributor commits match the added repo's owner by strict identity (`ZENG3LD`→`ZENG3LD/gate4agent`, `rustykuntz`→`rustykuntz/clideck`, `johannesjo`→`johannesjo/parallel-code`, …) = **45.5% of contributor commits, a LOWER BOUND.** The unmatched list is visibly full of more: company accounts (`ozz@stacklok.com`→`stacklok/brood-box`, `najmuzzaman@nex.ai`→`nex-crm`, Mixpeek's founder→`mixpeek/amux`) and name variants my matcher missed (`kanitkar`→`mrkanitkar`, `amaar`→`amaar-mc`, `雷浪声`→`launsion-boop`). A defensible generous count is ~26 of 33 ≈ **79%**.

⚠️⚠️ **This is NOT comparable to v253's "18.3%"** — different denominators. v253 measured self-submitted **entries as a share of all entries**. The comparable figure here is **~15–26 of 300 = 5–9%**, *lower* than v253, because Brad writes 89% of the entries himself.

---

## 12. ⚠️⚠️ The v246 `silent` detector returns ZERO — and the null is now more interesting than a hit

I **ran it** (v252's worst self-error was recording this null without running it):

```
/usr/bin/grep -rni "silent" <repo> --include=*.md --include=*.py --include=*.yml   → 0
/usr/bin/grep -rni "silent" <repo>                                                 → 0
```

**Zero. Second consecutive null** (v246→v252 was seven straight hits; v253 broke it; v254 stays broken).

⭐⭐⭐ **But v253's explanation for its null no longer holds, and the failure sharpens it.** v253 reasoned: *"a curated list has no runtime — it cannot fail confidently."* **v254 HAS a runtime** — 192 lines of Python running unattended every Monday — **and still returns zero.** So the detector's domain is not "artifacts that run." It is **artifacts whose authors have debugged them.**

And this runtime's defining property is that it fails silently in precisely the ways that matter:

```python
except urllib.error.HTTPError as e:
    print(f"  WARN {owner}/{repo}: HTTP {e.code}", file=sys.stderr)
...
return None
```

A permanently-404'd or renamed repo prints one `WARN` to **stderr, in an unattended weekly CI log nobody reads**, and then `key()` falls back to `parse_existing_stars()` — re-parsing the **badge already printed in the file**. ⭐⭐⭐ **So a dead repo keeps its last-known star count forever, rendered as current fact.** The word `warn` appears twice in the script: they thought about the failure and made it a stderr line in an unattended job. **A warning in an unattended job is a silent failure with extra steps.**

⭐⭐ **Worse, and structurally:** if every fetch returned `None`, the script would still rewrite the file, `git diff --quiet README.md` would find no change, the step would print `"No changes."` and **exit 0**. **A total API outage or an expired token produces a green, silent, successful run indistinguishable from "no stars changed this week."** That is the v246 pattern exactly — cause, consequence and remedy all knowable, none stated — and the word `silent` appears nowhere.

---

## 13. Security

**Essentially no attack surface in the artifact.** One Markdown file, one PNG, one stdlib-only Python script, one workflow. No server, no port, no CORS, no credentials, no dependencies, no install path ⇒ **the v231/v232 broken-authentication triad is structurally impossible.**

**The workflow, read line by line:**
- `permissions: contents: write` — correctly scoped; the job's only side effect is committing `README.md`.
- `actions/checkout@v4`, `actions/setup-python@v5` — **tag-pinned, not SHA-pinned.** Standard practice, a real (low) supply-chain exposure to tag mutation.
- Triggers are `schedule` + `workflow_dispatch` only — **no `pull_request` trigger**, so a fork PR never reaches a write-scoped token. **The obvious injection path does not exist.**
- The script interpolates the regex-captured `owner`/`repo` into an `api.github.com` URL. The capture classes are `([^/\s]+)` and `([^)\s]+)` — a crafted entry *could* inject path segments (e.g. `owner/repo/../../something`). ⚠️ Worst realistic outcome: the job queries an unintended GitHub API path with a repo-scoped token and writes a wrong star badge. **Not credential exfiltration** — the token is never placed in the URL, only in a header, and the host is fixed. **Low.**

🔴 **The real risk is downstream: 282 GitHub repos plus 13 external sites, all installable, essentially none vetted.** 16 have been through this vault. The catalogued capabilities include remote execution, SSH/PTY control of machines *"that hold your repos and credentials"* (`tlbx`), VM and microVM provisioning, git-hook installation, and harness-config rewriting (`FireConnect` — *"rewriting each harness's own config"*). And one entry is a Claude Code build with **security guardrails deliberately stripped**.

⭐ **And a list is data.** Point an agent at this file and say *"install the best one"* and **300 untrusted third-party descriptions become 300 attempts to steer that choice** — in a file that sorts by popularity, has no licence column you can trust, and contains one archived project and two stale redirects.

---

## 14. Defect ledger

| # | Defect | Severity | Evidence |
|---|---|---|---|
| 1 | **5 duplicate entries**, adjacent + byte-identical, all from `126e206` (2026-07-29); survived 4 machine rewrites | 🔴 HIGH | full-history dup trace, §2.3 |
| 2 | **No `LICENSE`, ever — plus a badge claiming one** and linking to a path that never resolved | 🔴 HIGH | `git log --all --name-only \| grep -i licen` = 0; README line 11 |
| 3 | **An archived project in the active list** — `letta-ai/lettabot` (327★); violates the list's own criterion #3 | 🔴 HIGH | fetched: title *"Archived - has been replaced by Letta Code"* |
| 4 | **Two stale owner redirects** — `ruvnet/claude-flow`→`ruflo` (68k★), `paoloanzn/free-code`→`freecodexyz` | 🔴 MED | `curl -L` final URLs |
| 5 | **Top-20 licence silence (10 of 20)** — you cannot filter by licence where it matters most | 🔴 MED | §5 |
| 6 | **The #3 entry is contradicted by its own repo**, plus an unsourced "fastest in GitHub history" superlative and an unverifiable "source leak" premise in 3 entries | 🔴 MED | fetched tagline, §8 |
| 7 | **No decay/dormancy policy at all** — `pushed_at` is in the response and unread; v253 has one with no machinery | ⚠️ MED | §2.2 |
| 8 | **Name collision** — `amux` = two different projects | ⚠️ LOW | lines 342, 352 |
| 9 | **No word budget stated**; mean 27.6 words, max 71, and the file gets wordier as it descends | ⚠️ LOW | §4 |
| 10 | **Bus factor one**; 33 of 37 identities have a single commit | ⚠️ LOW | §1 |
| 11 | **`126e206` says "Add 17"; measured +18** | ⚠️ TRIVIAL | 242 → 260 |

---

## 15. NOT ESTABLISHED

- **Star/fork/watcher figures generally.** The GitHub API is mocked here. I verified **3** entries against rendered pages; the other ~292 are README-stated. **NOT Pattern #52** — no velocity data.
- **Full link liveness.** 22 of 295 URLs fetched. **273 unchecked.**
- **Whether `awesome-lint` was ever run.** No config, no CI step, no mention.
- **Whether this list is on the official `sindresorhus/awesome` list**, and the manifesto requirements verbatim — the fleet agent assigned to fetch them failed its schema, and I did not close the gap myself. *(v253's equivalent check found it absent and failing two of three substantive requirements; do not assume the same result here without fetching.)*
- **Precedence.** Whether this is the first curated list of CLI coding agents. Creation dates would come from the mocked API ⇒ under the v222 rule, canonical status cannot be established.
- **Who `bradAGI` is.** A bare handle, a gmail, no bio surfaced. **`bradAGI` returns 0 hits in vault state.**
- **The "March 2026 Claude Code source leak."** Asserted as fact in 3 entries; I cannot verify it occurred.
- **"Fastest repo in GitHub history to 100K stars."** No authoritative GitHub velocity record exists (vault prior).
- **Whether the maintainer knows about the duplicates.** Issue/PR contents are unreachable (API mocked).
- **Any external discussion, launch post, or criticism.**
- **The causal claim that description length reflects self-promotion.** The association replicates; the motive is v253's maintainer's diagnosis of his own list, not a finding here.
- **No code was executed.** I read the script; I did not run it.

---

## 16. Error ledger — 19 caught, 6 mine

**Mine (all corrected before shipping):**

1. ⚠️ **My median was wrong.** I reported 26; for n=300 the median is the mean of the 150th and 151st values = **25.5**. I had taken the upper-middle element. Small, and mine.
2. ⚠️ **I assumed "110+" was stale against 300 entries.** It is **exact** — 83+12+16 = 111 agents, harnesses are *"plus."* I settled it with arithmetic instead of trusting the instinct. **Three fleet agents made the same misreading.**
3. ⚠️ **A loose URL regex produced non-comparable unique counts** (`grep -o 'https://github.com/[^)]*'` swept up inline links inside descriptions). Caught it in the same turn and redid the whole history pass with the strict entry regex.
4. ⚠️ **My exact-pair corpus matcher had two false-negative classes** — renames (`Hmbown/CodeWhale` = v72) and vault references that omit the owner path (`OpenHands` = v30, never written as a pair). Closed both with a reverse-direction pass; **the ship count went 13 → 16.**
5. ⚠️ **My self-submission matcher missed obvious cases** (`kanitkar`→`mrkanitkar`, `amaar`→`amaar-mc`) and **cannot see self-submissions behind company accounts or non-GitHub URLs at all.** Reported as a lower bound with the misses listed.
6. ⚠️ **I nearly compared 45.5% to v253's 18.3%.** Different denominators — contributor commits vs. all entries. Caught before writing it down.

**The fleet's (13), worst first:**

1. 🔴🔴 **THE WORST — the critic declared the root commit date and commit count "CRITICAL fabrications," escalated to *"the entire edifice of the situate report is compromised… no claim built from it can be trusted,"* and was itself wrong on both.** Root is `0b3d5227` **2026-02-06** and the count is **125**, each confirmed three ways including `git rev-list --max-parents=0 --all` and `git rev-list --count`. ⭐⭐⭐ **A fabricated verdict was used to destroy correct work** — a worse failure mode than v253's, where fabrication merely *added* a false finding.
2. 🔴 **The mechanism, and it is a portable rule.** The verifier used `git log --reverse --oneline | head -1` as a proxy for "the root commit" and got `7a1e54e` — **a real commit, dated 2026-04-06, but not a root.** ⭐⭐ **D39: to establish a structural git fact, use the command whose semantics ARE the definition, not one whose output usually coincides with it.** `rev-list --max-parents=0` for roots, `rev-list --count` for counts — never `log | head` or `log | wc`.
3. 🔴 **A commit count of "50."** I could not reproduce it: `git log --all --oneline | wc -l`, the file-routed variant, and `git rev-list --count --all` all return **125**. ⚠️ **I initially hypothesised the zsh stdout-dropping artifact the vault recorded at v253 (which also produced exactly 50) — the live test refutes that. My hypothesis was wrong; the number remains unexplained.**
4. 🔴 **Description length "median 23.5, mean 26.8."** Their method was `sed 's/.*— //'` — **greedy, truncating at the LAST em-dash.** **15 of 300 entries contain more than one em-dash.** Re-running with the greedy method reproduces **exactly 23.5 / 26.8**, which *proves* the method was the cause. Correct: **25.5 / 27.6**.
5. 🔴 **`worktree` reported at "3.0% (9 entries)"** — actual **26 (8.7%)**, a 3× undercount, caught by their own verifier. The headline built on it ("MCP replaced worktree") was right for the wrong reason.
6. 🔴 **"46% of entries mention no harness"** — actual 34.3%.
7. 🔴 **"Claude mentions 135"** then "128" — a bare-substring `grep -i 'Claude '` with a trailing space. Word-boundary matched: **140** any-Claude, **119** Claude Code.
8. 🔴 **A finding marked `VERIFIED by WebSearch` citing four projects with zero URLs and zero quoted results** — caught by the situating verifier, correctly.
9. 🔴 **"110+ is a 2.7× discrepancy against 300"** — repeated by both a verifier and the critic. Wrong; see §3.
10. ⚠️ **"Bot commits exactly 7 days apart"** — the first four are 5/1/3/4 days apart (manual dispatches). The verifier caught this correctly and it is a genuinely useful detail.
11. ⚠️ **A licence count of 165 vs my 166** — a narrower regex, one entry. Immaterial; mine is stated with its pattern.
12. ⚠️ **"Bot commits do not touch the date line"** — refuted correctly by its own verifier; the workflow has an explicit `Bump "Last updated"` step.
13. ⚠️ **The critic's operator recommendation was to write a verifier *for the subject's repository*** — a repo the operator does not own. Same class as v253's discarded suggestion. Reframed to the vault's own inventory script.

**Method notes for the next run:**
- ⭐⭐ **Point an adversary at the critic.** The final synthesis is the only stage with no adversary, and it is the stage whose output reads as authority. v249: *the contradiction stage only protects the stages it is pointed at.* v253: *point one at the subject's git history.* **v254: point one at the last stage.**
- ⚠️ **A pipeline whose final stage is a verifier discards the mapper's report.** My `pipeline()` returned only the verdicts; the map reports' content was lost. Have the verifier carry the report forward, or return both.
- 3 of 16 agents failed the structured-output cap. 13 done, ~2.08M tokens, 446 tool uses, 736 s.

---

## 17. Verdict in one line

**A 300-entry curated index of the exact tooling category this vault has written twenty wikis about, maintained almost single-handedly, with a weekly CI job that does one thing correctly and verifiably — and leaves unchecked every other question the same API response already answered.**
