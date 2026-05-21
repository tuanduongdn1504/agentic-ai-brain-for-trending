# Pilot 2 — helpline AI Layer plugin setup plan

> **Status:** PLAN — for operator review before execution. **No commands have been run.**
> **Drafted:** 2026-05-21
> **Drafted by:** Claude (autopilot-research session)
> **Pilot pattern source:** [[wiki/harness-engineering/helpline-worked-example|helpline-worked-example]] + [[wiki/harness-engineering/anthropic-large-codebases-anchor|anthropic-large-codebases-anchor]] (Anthropic blog 2026-05-14 + Cole Medin 2026-05-21 + coleam00/helpline repo, commit `72d14f5`)
> **Pilot type:** Tier-A operationally pilotable; FIRST-PARTY-AUTHORITATIVE-anchored
> **Estimated total time:** ~1-2h setup + 7-day pilot window (faster than Pilot 1)
> **Reversibility:** Full (delete `.claude/` from sandbox repo + uninstall plugin)

This plan walks the operator through installing the **`helpline-ai-layer` Claude Code plugin** (from `coleam00/helpline`) in a sandbox repo to test the **layout-agnostic portable pieces** of Anthropic's 7-component AI Layer: self-improving Stop hook + read-only `explorer` subagent + AST-based `codebase-search` MCP + generic `scoped-tests` skill.

The plan is structured for review-before-execution: each step has an EXECUTE annotation, prerequisites are explicit, and a **license gate** appears as an early-decision point.

---

## ⚠️ Critical pre-pilot decision — License gate

**STOP HERE if you haven't resolved this.** As of fetch (2026-05-21), `coleam00/helpline` has **no declared license** in the GitHub metadata. Using unlicensed code in your own projects is a legal grey zone.

Three resolution paths (operator decides BEFORE Part 1):

| Path | What it means | Recommended for |
|---|---|---|
| **A. Wait for license declaration** | Author may add license soon (repo created 2026-05-19); check the repo's LICENSE file weekly | Risk-averse operator; production-adjacent work |
| **B. Treat plugin pattern as INSPIRATION only** | Read helpline's `.claude/` structure, then hand-rebuild equivalent in your own repo (no copy-paste) | Operator who wants the architecture but not the legal risk |
| **C. Accept the risk for sandbox use only** | Install plugin in a private sandbox repo that will never ship; treat as ephemeral experiment | Operator who wants fast learning loop, accepts risk in bounded scope |

This plan assumes **Path C** (sandbox-only). If operator chose Path A or B, **stop here and revisit when the license question is resolved**. For Path B, see Part 7 (alternative path notes).

---

## Part 1 — Prerequisites checklist

Complete this checklist BEFORE running any setup commands.

### Tooling

- [ ] **Claude Code installed** on operator's primary machine
  - Verify with `claude --version`
  - **Required:** version supports `/plugin marketplace add` + `/plugin install` slash commands
  - **Pre-flight check:** in a Claude Code session, type `/plugin --help` to confirm plugin subsystem is available

- [ ] **Python toolchain `uv` installed**
  - Required to run helpline's own test suite + validator (`uv sync --extra dev`, `uv run pytest`, `uv run python tooling/validate/validate_all.py`)
  - Install: `curl -LsSf https://astral.sh/uv/install.sh | sh` (or via brew: `brew install uv`)
  - **Verify:** `uv --version` returns ≥0.4

- [ ] **`git` installed** for cloning the repo
- [ ] **`jq`** for inspecting JSON outputs (optional but useful)

### Sandbox setup

- [ ] **A non-production sandbox repo identified** for the plugin install
  - Avoid production codebases or repos with sensitive secrets
  - Ideal: a personal Python or non-Python project used for experimentation
  - The plugin's LSP/MCP pieces are Python-specific (pyright + AST-based search) — if your sandbox is non-Python, **flag for Part 6 alternative path**

- [ ] **Workspace directory for helpline clone**
  - Plan assumes `~/code/helpline/` — operator can change path
  - Keep helpline separate from sandbox repo (don't clone INSIDE the sandbox)

### Knowledge prereqs

- [ ] Operator has read [[wiki/harness-engineering/anthropic-large-codebases-anchor|anthropic-large-codebases-anchor]] + [[wiki/harness-engineering/helpline-worked-example|helpline-worked-example]] in full
- [ ] Operator understands the 7-component model (CLAUDE.md hierarchy / hooks / skills / plugins / LSP / MCP / subagents)
- [ ] Operator understands the **3 portable pieces** the plugin ships (Stop hook + explorer subagent + codebase-search MCP + scoped-tests skill) vs the **repo-specific pieces** that won't be installed (CLAUDE.md files, domain skills)

---

## Part 2 — Setup (estimated ~1-2 hours)

### Step 2.1 — Clone helpline

```bash
# EXECUTE — clone the worked-example repo
mkdir -p ~/code
cd ~/code
git clone https://github.com/coleam00/helpline.git
cd helpline

# Verify default branch + recent commit history
git log --oneline -5
git branch
```

**Expected:** `main` branch, ~2 commits per README (commit 1 = no AI Layer, commit 2 = AI Layer added).

**⚠️ FLAG:** at fetch time (2026-05-21) the repo had 2 stars / 0 forks / no license. **Confirm license status** before proceeding — `ls LICENSE LICENSE.md COPYING 2>/dev/null` should show a license file if author has added one since fetch.

### Step 2.2 — Run helpline's own test suite

```bash
# EXECUTE — verify the repo builds + tests pass
cd ~/code/helpline
uv sync --extra dev
uv run pytest
```

**Expected:** all tests pass. **If tests fail**, the AI Layer install may still work (the AI Layer is separate from the application code), but flag for investigation.

### Step 2.3 — Run the AI Layer validator

```bash
# EXECUTE — verify all 7 AI Layer components are correctly built
cd ~/code/helpline
uv run --extra dev python tooling/validate/validate_all.py
```

**Expected per README:** `13/13` validator pass. **If the validator fails**, do NOT install the plugin — diagnose first. The validator's job is precisely to detect when the AI Layer is broken.

**⚠️ Decision gate:** if validator fails AND operator can't fix in 30 min, STOP the pilot, document the failure, defer.

### Step 2.4 — Read `AI-LAYER.md`

```bash
# EXECUTE — read the agent-readable map of components → repo artifacts
less ~/code/helpline/AI-LAYER.md   # or your preferred pager
```

**Goal:** understand what each of the 7 components looks like in this codebase BEFORE installing the plugin in your own repo. This is the most important review-step in the pilot — it's where Cole Medin's "give helpline to your agent and ask it to bootstrap your codebase" approach gets its leverage.

**Optional alternative path (Cole's recommendation):**

```bash
# In your sandbox repo, open Claude Code and run:
> Read /Users/<you>/code/helpline/AI-LAYER.md and the .claude/ folder in that repo.
> It is a worked example of the AI Layer from Anthropic's large-codebases article.
> Don't install the plugin yet — first explain to me what each of the 7 components looks like
> there, and how it would map to THIS codebase's structure.
```

This pre-install conversation gives operator a sense of what the plugin will actually do before it's installed.

### Step 2.5 — Identify sandbox repo + back up existing `.claude/`

```bash
# EXECUTE — replace <sandbox-path> with operator's sandbox repo path
SANDBOX=<sandbox-path>
cd "$SANDBOX"

# Back up any existing .claude/ folder if present
if [ -d .claude ]; then
  mkdir -p .claude-backup
  cp -r .claude ".claude-backup/pre-pilot-2-$(date +%Y%m%d-%H%M%S)"
  echo "Backed up existing .claude/"
else
  echo "No existing .claude/ — fresh setup"
fi
```

**⚠️ EDIT BEFORE EXECUTE:** replace `<sandbox-path>` with the actual sandbox repo path identified in Part 1.

### Step 2.6 — Install the plugin

From within the sandbox repo, in a Claude Code session:

```
/plugin marketplace add /Users/<you>/code/helpline/tooling
/plugin install helpline-ai-layer@helpline-tooling
```

**⚠️ EDIT BEFORE EXECUTE:** replace `/Users/<you>/code/helpline/tooling` with the actual absolute path to your cloned helpline's `tooling/` folder.

**Expected:** Claude Code reports successful plugin install. The plugin should add:
- `.claude/hooks/` — Stop hook (and possibly SessionStart hook variant)
- `.claude/agents/explorer.md` — read-only explorer subagent
- `.claude/skills/scoped-tests/` — generic scoped-tests skill
- An MCP server registration for `codebase-search`

**Verify after install:**

```bash
# EXECUTE — inspect what the plugin landed in your sandbox
cd "$SANDBOX"
ls -la .claude/
find .claude -type f | head -20
```

### Step 2.7 — Smoke test 1: explorer subagent

In a fresh Claude Code session in the sandbox repo:

```
> spawn agent explorer
> Task: map the directory structure of this repo. List top-level folders + their purpose.
> Do not edit any files — read-only exploration only.
```

**Expected:** explorer subagent runs in isolated context, returns a directory-structure summary, then the main session receives the summary without burning its own context on the exploration.

**Verify behavior:**
- Main session context window remained relatively unchanged during the exploration
- Subagent's response is summary-shaped (not raw file dumps)
- Subagent had no opportunity to call write tools (read-only constraint enforced)

### Step 2.8 — Smoke test 2: codebase-search MCP

```
> /mcp
```

**Expected:** list shows `codebase-search` MCP server as connected.

Then:

```
> Use the codebase-search MCP's where_is tool to find the definition of <some-symbol-in-your-sandbox>.
```

**Expected:** MCP returns symbol-level definition location, not text-grep matches.

**⚠️ FAILURE FLAG:** if your sandbox is non-Python, the MCP may not work — it uses AST-based search and pyright-langserver under the hood. **For non-Python sandboxes**, see Part 6 alternative path.

### Step 2.9 — Smoke test 3: Stop hook

Make a small code change in the sandbox (e.g., add a comment to a file). End the Claude Code turn.

**Expected:** when Claude Code stops, the Stop hook fires. A separate Claude session runs in headless mode, reviews the session diff, reads existing CLAUDE.md files (if any), and outputs a review markdown document (e.g., `claude-md-review.md`).

**Verify:**

```bash
ls -la ~/code/<sandbox>/claude-md-review.md 2>/dev/null || ls -la ~/code/<sandbox>/.claude/reviews/ 2>/dev/null
```

(Exact filename / location depends on plugin's hook script — verify by reading the hook script after install.)

**Expected content:** review of what changed, whether CLAUDE.md needs updating, specific edit proposals OR "no changes needed."

---

## Part 3 — Measurement plan (7-day pilot window)

Pilot 2 is faster than Pilot 1 because:
- No 30-day cost-savings claim to validate
- 3 component-specific behaviors to measure (each individually testable in days, not weeks)
- License risk argues for faster cycle anyway

Track 3 axes corresponding to the 3 plugin pieces:

### Metric 1 — Stop hook proposal accuracy

After each Claude Code session where the Stop hook fires, **manually grade** the proposal:

| Score | Meaning |
|---|---|
| 5 — accurate edit | Hook correctly identified a CLAUDE.md drift; the proposed edit improves the file |
| 4 — useful but imprecise | Hook flagged a real concern but proposed edit needs operator refinement |
| 3 — neutral | "No changes needed" + that judgment is correct |
| 2 — false negative | Hook said "no changes needed" but CLAUDE.md actually drifted |
| 1 — false positive | Hook proposed an edit that would WORSEN the CLAUDE.md |

Aim for 15-20 sessions of data. Median ≥4 = strong signal.

### Metric 2 — Explorer subagent context-burn reduction

For 3-5 exploration tasks, measure:

| Approach | Token cost of main session | Time to summary |
|---|---|---|
| **Without subagent** — main agent reads files itself | Baseline N tokens | Baseline T minutes |
| **With explorer subagent** — delegate exploration | Pilot N' tokens | Pilot T' minutes |

Expected: N' << N (subagent absorbs the exploration cost in its isolated context). T' should be similar or slightly worse than T (round-trip latency).

**Decision metric:** if N' < 0.5 × N (subagent saves >50% of main-session tokens), the pattern delivers. If N' > 0.8 × N, the subagent isn't saving much.

### Metric 3 — codebase-search MCP hit rate vs grep

For 5-10 symbol-lookup tasks, compare:

| Tool | Hit accuracy | Speed |
|---|---|---|
| **Grep** | Returns N matches; how many are the actual target? | Wall-clock seconds |
| **MCP where_is** | Returns symbol-level definition | Wall-clock seconds |

Expected: MCP returns 1 precise definition + N references; grep returns many text matches including false positives. **Decision metric:** if MCP hit precision >2x grep, it's worth keeping.

### Daily-log template

Recommended: `~/helpline-pilot-log.md` with daily entries:

```
## 2026-05-XX
- Sessions today: 3
- Stop hook fired: 3x → scores: 5, 3, 4 (median 4)
- Explorer subagent used: 1x → 8K tokens saved on main session
- codebase-search MCP used: 2x → both returned correct symbol vs grep returning 12 false-positive matches
- Notes: Stop hook flagged a real CLAUDE.md gap in services/api/CLAUDE.md — accepted the proposal
```

### Decision metric (7-day endpoint)

| Outcome | What it means | Recommended action |
|---|---|---|
| **All 3 metrics in target range** (Stop hook median ≥4, subagent saves >50%, MCP precision >2x grep) | Pilot succeeds | Keep plugin; consider extending to other repos; document N=2 corroboration |
| **2 of 3 metrics in target** | Marginal — depends on which pieces matter most | Decide piece-by-piece: keep the winning components, uninstall the others if plugin granularity allows |
| **0-1 of 3 metrics in target** | Pilot fails for THIS sandbox | Investigate whether sandbox type was the issue (e.g., non-Python). Either retry on different sandbox or abandon |
| **License resolution: still none after 7 days** | Path C risk threshold | Either: (a) hand-rebuild the components per Path B (Part 6), or (b) keep using only in private sandbox |

---

## Part 4 — Reversal procedure

```bash
# EXECUTE — uninstall plugin from sandbox repo
cd "$SANDBOX"

# In Claude Code session:
# /plugin uninstall helpline-ai-layer

# Remove .claude/ folder (or restore from backup if existing config was overwritten)
rm -rf .claude
if [ -d ".claude-backup/pre-pilot-2-<timestamp>" ]; then
  cp -r ".claude-backup/pre-pilot-2-<timestamp>" .claude
fi

# Restart Claude Code in sandbox to confirm clean state
```

**Verify:** in a Claude Code session, `spawn agent explorer` should fail (subagent no longer registered). `/mcp` should not list codebase-search. Stop hook should not fire on session end.

You can also remove the cloned helpline repo if you don't want to keep it:

```bash
rm -rf ~/code/helpline
```

---

## Part 5 — Pilot decision gates (review checkpoints)

Stop and reassess if any of these happen during the pilot:

| Trigger | Action |
|---|---|
| **Validator (Step 2.3) fails** | STOP — diagnose helpline repo issue before continuing |
| **Plugin install fails** | STOP — verify Claude Code version supports plugin format; check helpline `tooling/` structure |
| **Stop hook causes session latency >30s per session** | Disable hook; reassess whether the maintenance value justifies cost |
| **Stop hook fires headless Claude session that consumes >$0.50 per main session** | Cost-multiplier alert — calculate at scale; may not justify |
| **Explorer subagent silently fails or returns empty summaries** | Investigate subagent definition; possible Claude Code version mismatch |
| **MCP codebase-search returns errors on every query** | Likely Python-LSP requirement not met in non-Python sandbox; switch sandbox or accept this piece won't work |
| **Author publishes restrictive license** mid-pilot | Re-evaluate Path A/B/C decision |

---

## Part 6 — Alternative paths

### Path A — Wait for license declaration

```bash
# EXECUTE periodically — check helpline repo for LICENSE file
curl -s https://api.github.com/repos/coleam00/helpline | jq '.license'
```

If `.license` returns a non-null value, re-evaluate the pilot. Once license is declared and acceptable, restart this plan from Part 1.

### Path B — Hand-rebuild from inspiration only

Read helpline's `.claude/` structure. Then in your own repo:

1. Write your own `.claude/hooks/Stop` shell script that runs `claude --headless` with a review prompt
2. Write your own `.claude/agents/explorer.md` subagent definition (no write tools)
3. Build your own MCP wrapper around your language's LSP (or use a generic LSP MCP if one exists)
4. Write your own scoped-tests skill following helpline's `paths:` convention

**Pros:** zero license risk; rebuilds the pattern as understanding rather than copying
**Cons:** ~4-8 hours of operator effort instead of 1-2 hour plugin install
**Recommended for:** operators who want long-term understanding + zero legal exposure

### Path D — Non-Python sandbox handling

If sandbox is JavaScript / Go / Rust / etc., the LSP+MCP pieces won't work out of the box. Two sub-paths:

**D.1:** Install plugin anyway — get the Stop hook + explorer subagent + scoped-tests skill. **Accept that MCP codebase-search won't fire** in your sandbox.

**D.2:** Port the MCP yourself — write an equivalent AST-based search MCP for your language's LSP (e.g., `gopls` for Go, `rust-analyzer` for Rust, `typescript-language-server` for TS/JS). Reuses helpline's MCP structure as template.

---

## Part 7 — Open questions to resolve before execution

Operator should answer these BEFORE starting Step 2.1:

1. **License resolution:** Path A (wait), B (inspiration-only rebuild), or C (sandbox-only)? **Default for this plan: C.**
2. **Sandbox identification:** which non-production repo will be used? Python-stack preferred (for full LSP+MCP test); non-Python OK with caveats (see Part 6 Path D).
3. **Plugin uninstall semantics:** does Claude Code's `/plugin uninstall` cleanly remove all files the plugin added? **Verify** by inspecting `.claude/` before AND after install vs uninstall.
4. **What's the Stop hook's cost-per-fire?** It runs a headless Claude session — at scale that's non-trivial. Measure this in week 0 baseline (Step 2.9 smoke test).
5. **Does the operator's existing `.claude/` config conflict?** If sandbox already has CLAUDE.md, hooks, or skills, the plugin's additions may interact. Backup (Step 2.5) covers worst case.

---

## Part 8 — Post-pilot deliverable

At the end of the 7-day window, operator should produce:

- **`04 Reviews/(C) 2026-05-XX-pilot-2-helpline-results.md`** — final write-up with:
  - Validator output (13/13?)
  - Per-metric scores (Stop hook accuracy, subagent context savings, MCP precision)
  - Decision: keep / partial-keep / abandon
  - License status at end of pilot
  - Lessons learned
  - Cross-link to update [[wiki/harness-engineering/helpline-worked-example|helpline-worked-example]] with N=2 corroboration data (or N=1+falsification)

If pilot succeeds AND license is favorable, this becomes the second corpus source corroborating the Anthropic 7-component framework as deployable, not just theoretical. Strong promotion-candidate signal for Storm Bear Pattern Library at v66 mini-audit.

---

## Summary table for review

| Phase | Time | Reversible? | Risk level |
|---|---|---|---|
| License gate (top of plan) | 30 min | N/A | **HIGH** — gate decision affects entire pilot |
| Part 1 — Prerequisites | 30 min | N/A | None |
| Part 2.1 — Clone helpline | 5 min | Yes (rm -rf) | Low |
| Part 2.2 — Run tests | 5-10 min | N/A | None (read-only) |
| Part 2.3 — Run validator | 5 min | N/A | None (read-only) |
| Part 2.4 — Read AI-LAYER.md | 15-30 min | N/A | None (read-only) |
| Part 2.5 — Backup sandbox `.claude/` | 1 min | N/A | None |
| Part 2.6 — Install plugin | 5 min | Yes (uninstall) | Medium — modifies sandbox repo |
| Part 2.7-2.9 — Smoke tests | 30 min | N/A (read-only) | Low |
| Part 3 — Measurement | 7 days | N/A | None (observation) |
| Part 4 — Reversal | 5 min | N/A (this IS reversal) | None |
| Part 5 — Decision gates | continuous | N/A | None (review-only) |

**Total operator-active time:** ~1-2h (setup) + ~10 min/day logging × 7 days = ~3h
**Total wall-clock time:** ~1.5 weeks (1-2h setup + 7-day pilot + 1 day write-up)

---

## Pilot 1 vs Pilot 2 — which to run first?

If operator hasn't decided:

| Criterion | Pilot 1 winner | Pilot 2 winner |
|---|---|---|
| **Speed to signal** | — | Pilot 2 (7 days vs 30 days) |
| **License risk** | Pilot 1 (none) | — |
| **Authority of source** | — | Pilot 2 (first-party Anthropic) |
| **Setup complexity** | tied (both ~1-2h) | tied |
| **Reversibility** | both full | both full |
| **Orthogonality** | independent — can run both | independent — can run both |
| **Pain target** | Credit cost on Opus | CLAUDE.md decay + context bloat |

**Recommended sequencing if running both:** start **Pilot 2 first** (faster signal, stronger authority) → if it succeeds, layer Pilot 1 on top later (the router pattern is orthogonal to the AI Layer pattern). If Pilot 2 license stays unresolved, fall back to Pilot 1.

---

## Operator decision required BEFORE execution

- [ ] License gate resolved (Path A / B / C chosen, **default C**)
- [ ] All Part 1 prerequisites checked
- [ ] All Part 7 open questions answered
- [ ] Sandbox repo identified
- [ ] Pilot start date committed to calendar
- [ ] Post-pilot write-up file path pre-created in `04 Reviews/` as a placeholder

When all checkboxes are checked, execute Part 2 in sequence. Otherwise, defer.

---

## Cross-links

- [[wiki/harness-engineering/anthropic-large-codebases-anchor|Authoritative anchor article]]
- [[wiki/harness-engineering/helpline-worked-example|Worked-example article]]
- [[wiki/harness-engineering/_index|harness-engineering topic index]]
- Sibling pilot plan: `output/(C) 2026-05-21-pilot-1-router-multimodel-setup-plan.md`
- Future write-up location: `04 Reviews/(C) 2026-05-XX-pilot-2-helpline-results.md` (operator creates after pilot completes)
