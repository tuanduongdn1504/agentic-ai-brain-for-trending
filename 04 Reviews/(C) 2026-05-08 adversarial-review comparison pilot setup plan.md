# Adversarial-review comparison pilot — setup plan (v2)

> **Purpose:** Self-contained execution plan for piloting cc-sdd v61 + codex-plugin-cc v62 as comparison-bundle. Apple-to-apple Pattern #76 architectural-role-separation (Stratum A) vs prompt-framing variant (Stratum B) empirical evaluation.
> **Status:** PLANNED (not yet executed)
> **Prepared:** 2026-05-08 session 72 (post-v62 codex-plugin-cc ship)
> **Updated:** 2026-05-08 session 72 — **execution architecture chosen: Hybrid Option 3 + Option 5 with `_pilots/` namespace convention**
> **Target execution:** Next fresh session (operator-time)
> **Estimated effort:** ~60-90 min setup + 1 week background measurement + ~60-90 min write-up = ~3-4h total spread over 1 week

---

## Execution architecture (Hybrid Option 3 + Option 5)

**Decision:** Pilot artifacts live INSIDE vault as sub-folder; phase-specific Claude Code sessions for Setup+Measurement vs Findings+Vault-Sync.

### Architectural choices

**Choice 1 — Location: Vault-internal sub-folder (Option 5)**

Pilot sub-folder path: `03 Projects/_pilots/2026-05-08 adversarial-review/`

`_pilots/` is NEW namespace within `03 Projects/` — distinct from `<subject> - Beginner Analysis/` observation-genre folders. Convention establishes vault-as-applied-platform philosophy.

**Choice 2 — Sessions: Phase-specific Claude Code sessions (Option 3)**

| Session | CWD | Purpose | Phase |
|---|---|---|---|
| **Session A** | `03 Projects/_pilots/2026-05-08 adversarial-review/` | Setup tools + build feature + run reviews + capture pilot-log | Setup phase + Day 1-7 measurement |
| **Session B** | `/Users/Cvtot/KJ OS Template/` (vault root) | Synthesize findings + update vault state files + commit | Day 7 write-up + Pattern Library updates |

**Why this hybrid works:**
- Claude Code traverses up from CWD to find project context — Session A at sub-folder still loads vault root `CLAUDE.md` (Storm Bear rules active throughout)
- Slash commands (`/codex:review`, `/kiro-impl`) operate on Session A's CWD = sub-folder = correct review target (NOT entire vault diff)
- cc-sdd `.claude/skills/` install into sub-folder's `.claude/` directory = isolated from vault root's skills (no conflict)
- Findings + Pattern Library updates happen in Session B at vault root = vault rules + git context correct
- Pilot artifacts versioned with vault repo = git history preserved; reversible if pilot abandoned

### `_pilots/` namespace convention (NEW)

```
03 Projects/
├── (PROJECT TEMPLATE)/                         ← existing scaffolding template
├── cc-sdd - Beginner Analysis/                 ← observation-genre wiki (existing)
├── codex-plugin-cc - Beginner Analysis/        ← observation-genre wiki (existing)
├── _pilots/                                     ← NEW namespace: applied-work pilots
│   ├── 2026-05-08 adversarial-review/           ← THIS PILOT
│   │   ├── README.md                            ← Links to pilot plan + status
│   │   ├── PILOT-PLAN-LINK.md                   ← Reference back to setup plan
│   │   ├── extractor.py                         ← Real feature implementation
│   │   ├── test_extractor.py
│   │   ├── .claude/skills/kiro-*/               ← cc-sdd installed here (sub-folder scope)
│   │   ├── .kiro/                               ← cc-sdd config + specs
│   │   ├── pilot-log/
│   │   │   ├── day1-adhoc-review.md
│   │   │   ├── day2-kiro-review.md
│   │   │   ├── day3-codex-neutral-review.md
│   │   │   ├── day4-codex-adversarial-review.md
│   │   │   └── comparison-table.md
│   │   └── findings.md                          ← Consolidated findings (also copied to 04 Reviews/)
│   ├── 2026-05-XX free-claude-code-cost-test/   ← FUTURE pilot (placeholder)
│   ├── 2026-06-XX n8n-storm-bear-mcp/           ← FUTURE pilot (placeholder)
│   └── README.md                                ← Namespace-level index
└── ...
```

**Rules for `_pilots/` namespace:**
1. Naming pattern: `YYYY-MM-DD <kebab-case-pilot-topic>/`
2. Each pilot self-contained (no cross-pilot dependencies)
3. `.claude/` and `.kiro/` directories scoped to pilot sub-folder (don't pollute vault root)
4. Pilot-log artifacts stay in sub-folder
5. Final `findings.md` duplicated to `04 Reviews/(C) YYYY-MM-DD <pilot-topic> findings.md` for vault-routine consistency
6. Commit pattern: pilot work committed to vault main branch with descriptive prefix `Pilot v62-v66:` or similar

### Vault philosophy commitment

Choosing this architecture commits Storm Bear vault to evolution: **pure-observation knowledge-base → applied-platform with observation + execution coexisting**.

This aligns with GOALS.md Goal #2 explicit user statement (2026-05-08): *"Tôi muốn build software with these tools"*. Operator-deployment imbalance (8 pilots accumulated / 0 deployed flagged in GOALS reflections) resolved via vault adopting applied-platform identity rather than spawning external sandbox.

---

## Why this pilot exists

### Strategic context
1. **Pilot-deferral imbalance** flagged in GOALS reflections: "8 ranked pilots accumulated / 0 deployed." Goal #2 ("Tôi muốn build software with these tools") only resolves via actual pilot deployment.
2. **Pattern #76 fast-counter-evidence cycle** at v62: Pattern #76 registered v63 mini-audit (cc-sdd v61 baseline) → v62 codex-plugin-cc counter-evidence 1-day later. Two distinct mechanism strata observed; empirical comparison needed before v66 audit.
3. **Storm Bear meta-entity Phase 0.9 criterion (b)** currently CLAIMED operational-deployability across v60+v61+v62. Pilot HARDENS criterion from claim to verified evidence.

### Pattern Library payoff
This pilot directly informs:
- **Pattern #76 Adversarial Subagent Review Architecture** (Stratum A architectural role-separation)
- **NEW sister candidate** Adversarial-Review-as-Prompt-Framing Variant (Stratum B prompt-engineering)
- **Pattern #74 EARS-Format Requirements** (vault-applicability evidence, if cc-sdd pilot exercises spec phases)
- **Pattern #75 External-IDE-Methodology Lineage Type** (Kiro IDE methodology empirical assessment)
- **Pattern #21 SDD Methodology Emergence** (promotion-rationale validation)

---

## Pre-setup checklist

Verify before starting:
- [ ] ChatGPT subscription active OR OpenAI API key available (codex-plugin-cc requires)
- [ ] Anthropic API access via Claude Code (vault primary)
- [ ] Node.js 18.18+ installed (`node --version`)
- [ ] npm functioning (`npm --version`)
- [ ] Claude Code CLI/IDE installed and operational
- [ ] ~2GB free disk space for sandbox project + plugin dependencies
- [ ] 30-60 phút available for setup phase (uninterrupted)

---

## Sandbox project scenario

**Recommended feature:** "Markdown Link Extractor CLI for Vault Notes"

**Why this scenario:**
- Small enough to complete in 1 week (~30-50 lines of code)
- Real enough to stress-test review mechanisms (file I/O + parsing + edge cases)
- Vault-relevant (could become real vault tool post-pilot)
- Has natural deliberate-design-decisions to challenge (caching strategy / regex vs parser / output format / error handling)

**Specifications:**
- **Input:** Path to vault directory or single .md file
- **Output:** JSON list of `{file, line, link_text, link_url, link_type}` (link_type = inline / reference / image / autolink / wikilink)
- **Edge cases:** Code blocks (skip links inside ``` blocks), broken/malformed links, deeply nested directories, symlinks
- **Tech stack:** Python 3.11+ with `pathlib` + `re` (or `markdown-it-py` for parser-based) + `json` + `argparse`
- **Tests:** pytest with sample markdown fixtures

**Deliberate questionable design decisions to bake in:**
1. Use regex-only (no markdown parser) — prompts review on robustness
2. Skip caching (re-parse every file) — prompts review on performance scaling
3. Synchronous I/O (no async) — prompts review on concurrency
4. Custom JSON output (no schema validation) — prompts review on contract design

These intentional weak spots let adversarial review demonstrate what it catches.

---

## Setup phase (~60-90 min on operator machine)

**Session A starts here.** Open Claude Code at vault root, then `cd` into pilot sub-folder via Bash. Vault `CLAUDE.md` rules remain active (Claude Code traverses up to find project context).

### Step 0 — Open Session A at pilot sub-folder

**Two equivalent approaches:**

**Approach 0a (recommended):** Open new Claude Code session, cd into pilot path before first prompt:
```bash
cd "/Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-08 adversarial-review"
# Then start Claude Code session in this directory
```

**Approach 0b:** Open Claude Code at vault root, immediately cd via Bash tool:
```bash
cd "/Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-08 adversarial-review"
pwd  # Verify CWD
```

**Note for Session A:** All subsequent slash commands (`/codex:*`, `/kiro-*`) and Bash operations operate on pilot sub-folder CWD. Vault rules (Storm Bear `(C)` prefix, blunt-direct style, etc.) still apply via vault root `CLAUDE.md` traversal.

### Step A — Pilot sub-folder initialization (~10 min)

```bash
# Create _pilots namespace if first pilot
mkdir -p "/Users/Cvtot/KJ OS Template/03 Projects/_pilots"

# Create this pilot's sub-folder
mkdir -p "/Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-08 adversarial-review"
cd "/Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-08 adversarial-review"

# Pilot README + reference back to setup plan
cat > README.md << 'EOF'
# Pilot: Adversarial-review comparison (cc-sdd v61 + codex-plugin-cc v62)

**Started:** 2026-05-XX (insert actual date)
**Status:** in-progress / complete (update as pilot progresses)
**Setup plan:** `04 Reviews/(C) 2026-05-08 adversarial-review comparison pilot setup plan.md`
**Findings (when complete):** `findings.md` + duplicated to `04 Reviews/(C) YYYY-MM-DD adversarial-review comparison pilot findings.md`

## Quick links
- cc-sdd entity wiki: `03 Projects/cc-sdd - Beginner Analysis/02 Wiki/(C) cc-sdd entity.md`
- codex-plugin-cc entity wiki: `03 Projects/codex-plugin-cc - Beginner Analysis/02 Wiki/(C) codex-plugin-cc entity.md`
- Pattern #76 N=1 baseline: `_patterns/03-active-candidates.md` Pattern #76 entry
EOF

# Pilot-log directory for measurement artifacts
mkdir -p pilot-log

# NO separate git init — pilot folder lives inside vault repo
# Verify pilot folder is part of vault repo
git -C "/Users/Cvtot/KJ OS Template" status --short | grep _pilots
```

**Verification:**
- `pwd` shows pilot sub-folder path
- README.md exists with reference to setup plan
- `pilot-log/` directory created
- vault `git status` shows pilot folder as untracked (will be committed at end of setup phase or after first measurement)

### Step B — Install cc-sdd v61 (Pilot #1 — Stratum A) (~10-15 min)

```bash
# Already in pilot sub-folder from Step A
pwd  # Should be: /Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-08 adversarial-review

# Install cc-sdd Skills mode for Claude Code in pilot sub-folder
npx cc-sdd@latest --claude-skills

# Verify install (skills should be in pilot sub-folder, NOT vault root)
ls -la .claude/skills/
ls -la .kiro/

# Expected directory structure (relative to pilot sub-folder):
# .claude/skills/kiro-discovery/
# .claude/skills/kiro-spec-init/
# .claude/skills/kiro-spec-requirements/
# .claude/skills/kiro-spec-design/
# .claude/skills/kiro-spec-tasks/
# .claude/skills/kiro-impl/
# .claude/skills/kiro-review/         ← key for Stratum A
# .claude/skills/kiro-debug/          ← key for Stratum A
# .claude/skills/kiro-verify-completion/  ← key for Stratum A
# .kiro/steering/  (empty — populate later)
# .kiro/specs/     (empty — populate via /kiro-spec-init)
```

**Troubleshooting:**
- If `npx cc-sdd@latest` fails with version error → check Node.js >= 18.18 (`node --version`)
- If skills not visible after install → run `/reload-plugins` in Claude Code Session A
- If `.claude/` directory not created → cc-sdd may need explicit `--target=claude` flag (check cc-sdd docs)
- **CRITICAL:** Verify install happened in pilot sub-folder `.claude/skills/`, NOT vault root `.claude/skills/`. If vault root accidentally got installation, `rm -rf` from vault root and re-install.

**Verification:** All 9 kiro-* skill directories exist under pilot sub-folder's `.claude/skills/`. Vault root's `.claude/skills/` (if exists) UNCHANGED.

### Step C — Install codex-plugin-cc v62 (Pilot #1.5 — Stratum B) (~15-20 min)

In **Claude Code Session A** (CWD = pilot sub-folder):

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**Note:** Plugin marketplace install is GLOBAL (affects Claude Code installation, not per-folder). This is correct — codex-plugin-cc is a plugin, not folder-scoped skill set.

`/codex:setup` will prompt for:
- ChatGPT subscription credentials OR OpenAI API key
- Codex backend connectivity test
- Default model selection (GPT-5.2 or similar)
- Reasoning effort level (low/medium/high)

**Troubleshooting:**
- If marketplace add fails → check Claude Code version supports plugin marketplace
- If auth fails → verify ChatGPT subscription active OR `OPENAI_API_KEY` env var set
- If `/reload-plugins` doesn't expose `/codex:*` commands → restart Claude Code Session A

**Verification:** Type `/codex:` in Claude Code Session A; autocomplete should show 7 commands (review, adversarial-review, rescue, status, result, cancel, setup).

### Step D — Implement feature (~30-45 min, with Claude Code Session A help, NO review tools)

In Claude Code Session A main conversation (no `/kiro-*` or `/codex:*` invocations yet):

```
"Build a Python CLI tool that extracts all markdown links from .md files
in a directory. Output JSON list of {file, line, link_text, link_url,
link_type}. Use regex-only parsing (no markdown library). Sync I/O.
No caching. Skip links inside code blocks. Include pytest tests with
sample fixtures."
```

Claude Code Session A will implement in pilot sub-folder. Operator commits to vault repo (NOT separate pilot git):

```bash
# Still in pilot sub-folder
git -C "/Users/Cvtot/KJ OS Template" add "03 Projects/_pilots/2026-05-08 adversarial-review/"
git -C "/Users/Cvtot/KJ OS Template" commit -m "Pilot v62-v66: feature implementation (markdown link extractor; regex-based, no caching)"
```

**Verification:** `git -C "/Users/Cvtot/KJ OS Template" log --oneline -5` shows pilot commit. Tests pass: `pytest test_extractor.py`. Example invocation works: `python extractor.py path/to/sample.md`.

---

## Measurement phase (1 week background, ~30-45 min/day active)

**Session A continues for entire measurement phase.** All Days 1-6 use Session A at pilot sub-folder CWD. Pilot-log artifacts written to pilot sub-folder's `pilot-log/` directory.

**Each day end:** commit pilot-log entry to vault repo:
```bash
git -C "/Users/Cvtot/KJ OS Template" add "03 Projects/_pilots/2026-05-08 adversarial-review/pilot-log/"
git -C "/Users/Cvtot/KJ OS Template" commit -m "Pilot v62-v66: Day N <review-mode> log captured"
```

### Day 1 (Setup day) — Baseline ad-hoc Claude Code review

In Claude Code main session (NO plugin/SDD invocations):

```
"Review the markdown link extractor implementation. Identify bugs,
design issues, performance concerns, security problems, and
improvement opportunities. Be thorough and specific."
```

**Capture in pilot log:**
- Review output (full text → save to `pilot-log/day1-adhoc-review.md`)
- Approximate token usage (Claude Code shows in status bar)
- Time elapsed (start prompt → review complete)
- Number of distinct issues raised
- Any false positives (issues that aren't real)

### Day 2 — cc-sdd `kiro-review` (Stratum A)

Two sub-paths possible:

**Path 2a — Full SDD pipeline:**
```
/kiro-discovery "I built a markdown link extractor; review and improve"
# Follow prompts through spec-init → requirements → design → tasks → impl
# /kiro-impl autonomous mode will dispatch reviewer subagent on existing code
```

**Path 2b — Direct review-only:**
```
# Manually invoke kiro-review skill on existing diff
# (exact command depends on cc-sdd v3.x API; check skills/kiro-review/skill.md)
```

**Capture:**
- Reviewer subagent output → `pilot-log/day2-kiro-review.md`
- Auto-debug invocations (kiro-debug returns) → save separately
- Completion gate result (kiro-verify-completion VERIFIED/NOT_VERIFIED) → save
- Token cost (subagent dispatch can be expensive)
- Wall-clock time
- Number of distinct issues raised
- Whether reviewer subagent invoked DIFFERENT tool access than implementer (key Stratum A signal)

### Day 3 — codex-plugin-cc `/codex:review` (Stratum B neutral baseline)

```
/codex:review
```

**Capture:**
- Codex review output → `pilot-log/day3-codex-neutral-review.md`
- ChatGPT subscription token usage (visible in OpenAI dashboard)
- Wall-clock time
- Distinct issues raised
- False positives

### Day 4 — codex-plugin-cc `/codex:adversarial-review` (Stratum B adversarial)

```
/codex:adversarial-review --base main "challenge whether the regex-only design and lack of caching are right tradeoffs"
```

**Capture:**
- Adversarial review output → `pilot-log/day4-codex-adversarial-review.md`
- Cost + time
- Distinct DESIGN-DECISION issues raised (vs implementation issues)
- Compare with Day 3 neutral output: did adversarial framing actually surface different concerns?

### Day 5-6 — Cross-comparison analysis

Build comparison spreadsheet `pilot-log/comparison-table.md`:

| Metric | Day 1 ad-hoc | Day 2 cc-sdd | Day 3 codex neutral | Day 4 codex adversarial |
|---|---|---|---|---|
| Lines of review output | | | | |
| Distinct issues raised (count) | | | | |
| Design-decision issues raised | | | | |
| Implementation-detail issues | | | | |
| False positives count | | | | |
| Real bugs caught | | | | |
| Severity distribution (high/med/low) | | | | |
| Token cost (USD est.) | | | | |
| Wall-clock time (sec) | | | | |
| Operator effort to interpret (1-5) | | | | |
| Actionability (1-5) | | | | |

**Qualitative observations (free-form):**
- Did Stratum A architectural separation produce DIFFERENT issues than Stratum B prompt-framing?
- Did adversarial framing (Day 4) catch design issues that neutral framing (Day 3) missed?
- Did cc-sdd reviewer subagent's separate tool-access constraint matter (e.g., can't write code, can only critique)?
- Did kiro-debug auto-loop add value vs manual interpretation?

### Day 7 — Write-up

**Session B starts here.** Open new Claude Code session at vault root (CWD = `/Users/Cvtot/KJ OS Template/`). Vault rules + git context active for state updates.

```bash
# Open Session B at vault root
cd "/Users/Cvtot/KJ OS Template"
# Start Claude Code session here
# Read pilot-log artifacts via relative path: 03 Projects/_pilots/2026-05-08 adversarial-review/pilot-log/*.md
```

Create comprehensive findings document:

**Primary path:** `03 Projects/_pilots/2026-05-08 adversarial-review/findings.md` (in pilot sub-folder, alongside pilot-log)
**Duplicated to:** `04 Reviews/(C) YYYY-MM-DD adversarial-review comparison pilot findings.md` (for vault routine consistency with prior reviews)

**Required sections:**

1. **TL;DR** (2-3 paragraphs)
   - Stratum A vs Stratum B empirical winner (or "no clear winner; depends on context")
   - Cost/value summary
   - Storm Bear vault recommendation

2. **Methodology**
   - Sandbox project description
   - Comparison protocol (4 review modes on same diff)
   - Measurement framework

3. **Quantitative results**
   - Comparison table (from Day 5-6)
   - Cost breakdown
   - Token consumption per review mode

4. **Qualitative observations**
   - Issue category distribution (design vs implementation)
   - False positive patterns
   - Actionability per review mode

5. **Stratum A vs Stratum B empirical findings** (KEY SECTION)
   - Did architectural role-separation deliver higher-quality review?
   - Was the cost overhead of cc-sdd's 4-skill pipeline justified?
   - Was prompt-framing variant (codex-adversarial) "good enough" at lower complexity?
   - Pattern #76 v66 audit input: refine scope or maintain current formulation?
   - NEW sister candidate (prompt-framing variant) v66 registration: confirmed warranted?

6. **Pattern Library implications for v66 audit**
   - Pattern #76 refinement specifics (with empirical evidence)
   - NEW sister candidate formulation refinement
   - Pattern #74 EARS-format vault-applicability (if pipeline exercised EARS phase)
   - Storm Bear meta-entity Phase 0.9 (b) verified-deployable evidence

7. **Storm Bear vault recommendation**
   - Adopt cc-sdd Stratum A for production?
   - Adopt codex-plugin-cc Stratum B for production?
   - Hybrid approach (use both for different review-types)?
   - Abandon both (revert to ad-hoc Claude Code review)?

8. **Pilot reproducibility notes**
   - What worked / didn't work in setup
   - Time-cost reality vs estimate
   - Recommendations for future pilots

---

## Failure modes + troubleshooting

### Hybrid architecture-specific failures (NEW — vault sub-folder considerations)

**FAILURE:** cc-sdd installs into vault root `.claude/skills/` instead of pilot sub-folder
- **Diagnostic:** `ls -la "/Users/Cvtot/KJ OS Template/.claude/skills/"` — should NOT show kiro-* skills
- **Likely cause:** Claude Code session CWD was vault root, not pilot sub-folder, when `npx cc-sdd@latest` ran
- **Fix:** `rm -rf "/Users/Cvtot/KJ OS Template/.claude/skills/kiro-*"` (only the kiro-* directories; preserve any pre-existing vault skills) + verify CWD before re-running cc-sdd install in pilot sub-folder

**FAILURE:** Slash command `/codex:review` reviews vault root diff instead of pilot sub-folder
- **Diagnostic:** Review output mentions vault wiki files instead of pilot feature
- **Likely cause:** Claude Code Session A CWD = vault root, not pilot sub-folder
- **Fix:** End session; restart Session A with explicit CWD = pilot sub-folder

**FAILURE:** `/kiro-impl` or other cc-sdd skills not found in Session A
- **Diagnostic:** Type `/kiro-` in Session A; autocomplete shows nothing
- **Likely cause:** Skills installed in pilot sub-folder but Session A loaded different `.claude/` context
- **Fix:** Verify Session A pwd matches pilot sub-folder; run `/reload-plugins` or restart session

**FAILURE:** Vault git status pollution (pilot artifacts mixed with vault wiki commits)
- **Diagnostic:** `git status` at vault root shows mixed pilot files + vault state files
- **Likely cause:** Session A + Session B running simultaneously OR commit grouping unclear
- **Fix:** Use commit message prefixes consistently: `Pilot v62-v66:` for pilot work; standard messages for vault wiki/audit work. Stage pilot artifacts separately: `git add "03 Projects/_pilots/..."` not `git add -A`.

**FAILURE:** Pilot sub-folder accidentally committed to wiki-related git operation
- **Diagnostic:** Pilot artifacts in commit titled "Ship vXX wiki..."
- **Recovery:** No critical damage — pilot files preserved either way. Note in iteration log; cleaner separation next time.

### Setup phase failures (unchanged from v1)

**FAILURE:** `npx cc-sdd@latest` errors out
- **Likely cause:** Node.js version mismatch
- **Fix:** Verify `node --version` ≥ 18.18; upgrade via `nvm install 18.18 && nvm use 18.18`

**FAILURE:** `/plugin marketplace add openai/codex-plugin-cc` fails
- **Likely cause:** Claude Code version doesn't support plugin marketplace
- **Fix:** Update Claude Code CLI/IDE to latest; restart session

**FAILURE:** `/codex:setup` auth fails
- **Likely cause:** ChatGPT subscription expired OR OpenAI API key invalid
- **Fix:** Verify ChatGPT subscription at https://chat.openai.com/billing OR set `OPENAI_API_KEY` env var

**FAILURE:** Both plugins coexist but conflict (slash command namespace collision)
- **Likely cause:** Plugin namespace overlap (unlikely but possible)
- **Fix:** Document conflict; if forced choice, prioritize cc-sdd (broader corpus payoff)

### Measurement phase failures

**FAILURE:** cc-sdd `kiro-review` doesn't dispatch separate subagent (looks like single-skill review)
- **Diagnostic:** Check Claude Code session logs for separate Task tool invocations
- **Implication:** If verified, Pattern #76 N=1 baseline (cc-sdd v61) needs revision

**FAILURE:** `/codex:adversarial-review` produces output identical to `/codex:review`
- **Diagnostic:** Compare Day 3 vs Day 4 outputs verbatim
- **Implication:** Sister candidate (Stratum B prompt-framing variant) lacks empirical distinctness; v66 registration may be premature

**FAILURE:** Token cost runaway (>$10 USD on small feature review)
- **Diagnostic:** Track per-mode cost separately
- **Implication:** Document cost-discipline insight; affects vault adoption decision

### Time-cost overruns

**SCENARIO:** Setup takes >2h instead of ~90 min
- **Action:** Pause; document blocker in `pilot-log/setup-blockers.md`; resume next session

**SCENARIO:** Day-by-day measurement falls behind schedule
- **Action:** Compress to 3-4 days instead of 7; prioritize Day 1 + Day 2 + Day 4 (skip Day 3 neutral if time-pressed)

**SCENARIO:** Write-up takes >2h
- **Action:** Compress to TL;DR + Quantitative table + Stratum A/B finding only; defer full sections

---

## v66 mini-audit input prep

When pilot complete, the findings doc should answer:

1. **Pattern #76 refinement** — Does empirical evidence support narrowing scope to Stratum A architectural-role-separation specifically?
2. **NEW sister candidate** — Does Stratum B prompt-framing variant deserve standalone pattern OR observation-track?
3. **Stratum-distinction taxonomy** — Should Pattern Library codify Stratum A / Stratum B as taxonomy item for behavioral patterns?
4. **Cost-effectiveness ranking** — Which review mode best for vault context? (Inform pilot ranking re-ordering)
5. **Pattern #74 EARS evidence** — If EARS phase exercised, does it work in vault practice?
6. **Storm Bear Phase 0.9 (b) hardening** — verified-deployable evidence for both cc-sdd + codex-plugin-cc

---

## Recommended timing

**Earliest start:** Day after this session (2026-05-09) when fresh
**Latest start:** Within 2 weeks (2026-05-22) — pilot evidence needed for v66 audit which falls at v62+4 wikis natural cadence
**Hard deadline:** Before v66 audit deliberation begins

**Fallback if pilot blocked:**
- Continue v63 wiki without pilot evidence
- v66 audit defers Pattern #76 refinement deliberation (acceptable; pattern stays N=1 stale-flagged with v62 counter-evidence noted)
- Pilot rescheduled to v66-v70 window

---

## Pilot decision framework (post-execution)

After write-up, vault operator decides per-pilot adoption:

### cc-sdd v61 (Stratum A) adoption decision

**Adopt for production if:**
- ✅ Reviewer subagent catches issues ad-hoc Claude Code missed
- ✅ Auto-debug-on-rejection adds workflow value
- ✅ Token cost overhead < 2× ad-hoc cost
- ✅ Workflow ergonomics acceptable for solo-vault-author scenarios

**Defer adoption if:**
- ❌ Catch-rate marginally better than ad-hoc
- ❌ Token cost > 3× ad-hoc cost
- ❌ Workflow overhead breaks vault flow
- ❌ Spec-discipline doesn't match vault feature size

### codex-plugin-cc v62 (Stratum B) adoption decision

**Adopt for production if:**
- ✅ Adversarial framing catches design issues neutral review misses
- ✅ ChatGPT subscription cost acceptable (operator already pays)
- ✅ Cross-vendor auth flow not friction-blocking
- ✅ Codex review quality complements cc-sdd or replaces ad-hoc

**Defer adoption if:**
- ❌ Adversarial framing produces verbose-but-not-actionable output
- ❌ ChatGPT subscription cost not justified
- ❌ Cross-vendor flow breaks vault session continuity

### Hybrid adoption decision

**Hybrid (use both) if:**
- cc-sdd kiro-review for SDD-pipelined features
- codex-plugin-cc adversarial-review for one-off design-decision challenges
- Cost overhead acceptable for both

---

## Pickup state for next session

When operator returns to execute pilot:

### Session A pickup (Setup + Measurement)

1. Read this document (`04 Reviews/(C) 2026-05-08 adversarial-review comparison pilot setup plan.md`) for full context
2. Verify pre-setup checklist
3. Open Claude Code Session A at pilot sub-folder: `cd "/Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-08 adversarial-review"` (create folder via Step A first if not exists)
4. Execute Step A → Step B → Step C → Step D in single setup-day sitting
5. Day 1-7 measurement: continue Session A (or new sessions at same CWD); commit pilot-log artifacts to vault repo end-of-day with `Pilot v62-v66:` prefix

### Session B pickup (Findings + Vault sync)

6. Open new Claude Code Session B at vault root: `cd "/Users/Cvtot/KJ OS Template"`
7. Read pilot-log artifacts from Session A's pilot sub-folder
8. Write findings to `03 Projects/_pilots/2026-05-08 adversarial-review/findings.md` (primary) + duplicate to `04 Reviews/(C) YYYY-MM-DD adversarial-review comparison pilot findings.md` (vault routine consistency)
9. Update vault state files (root CLAUDE.md state-block + GOALS.md + `_state/pilot-ranking-2026-05-07.md`) with findings + adoption decisions
10. Inform v66 mini-audit deliberation
11. Commit Session B work with descriptive message: `Document adversarial-review comparison pilot findings + update vault state`

**Context preserved:** This document is self-contained; no Claude session memory required across Session A ↔ Session B transition. Pilot-log artifacts + findings.md + vault state updates form complete record.

---

## Cross-references

- `_state/pilot-ranking-2026-05-07.md` — pilot ranking (#1 cc-sdd + #1.5 codex-plugin-cc)
- `03 Projects/cc-sdd - Beginner Analysis/` — v61 wiki + Pattern #76 N=1 baseline evidence
- `03 Projects/codex-plugin-cc - Beginner Analysis/` — v62 wiki + counter-evidence to Pattern #76
- `_patterns/03-active-candidates.md` — Pattern #76 entry (will be updated post-pilot)
- `_patterns/05-recent-additions.md` — v63 EARLY mini-audit decisions
- `04 Reviews/(C) 2026-05-07 Pattern Library mini-audit post-v61 ...md` — v63 audit document (Pattern #76 registration)
- `03 Projects/_pilots/` — NEW namespace established at this pilot (convention for future applied-work pilots)
- `03 Projects/_pilots/2026-05-08 adversarial-review/` — THIS pilot's sub-folder (created at Step A)
- `03 Projects/_pilots/README.md` — namespace-level index (created when 2nd pilot establishes pattern; defer for now)

---

## Status tracking

| Phase | Status | Date |
|---|---|---|
| Plan created | ✅ DONE | 2026-05-08 |
| Pre-setup checklist verified | pending | — |
| Setup phase complete | pending | — |
| Day 1-7 measurement | pending | — |
| Findings doc complete | pending | — |
| v66 audit input ready | pending | — |
| Pilot adoption decision | pending | — |

Update this table as pilot progresses.

---

**Plan version:** 2.0 (architecture updated to Hybrid Option 3 + Option 5 with `_pilots/` namespace convention; 2026-05-08 session 72)
**Plan v1.0 history:** Initial draft with external sandbox approach (`~/sandbox/adversarial-review-pilot`) — superseded by v2 vault-sub-folder approach
**Next update trigger:** Pilot setup attempt (any blockers/learnings update plan)
