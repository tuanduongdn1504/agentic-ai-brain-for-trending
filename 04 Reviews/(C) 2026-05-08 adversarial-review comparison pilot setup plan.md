# Adversarial-review comparison pilot — setup plan

> **Purpose:** Self-contained execution plan for piloting cc-sdd v61 + codex-plugin-cc v62 as comparison-bundle. Apple-to-apple Pattern #76 architectural-role-separation (Stratum A) vs prompt-framing variant (Stratum B) empirical evaluation.
> **Status:** PLANNED (not yet executed)
> **Prepared:** 2026-05-08 session 72 (post-v62 codex-plugin-cc ship)
> **Target execution:** Next fresh session (operator-time)
> **Estimated effort:** ~60-90 min setup + 1 week background measurement + ~60-90 min write-up = ~3-4h total spread over 1 week

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

### Step A — Sandbox project initialization (~10 min)

```bash
# Create sandbox outside vault to avoid pollution
mkdir -p ~/sandbox/adversarial-review-pilot
cd ~/sandbox/adversarial-review-pilot

# Initialize git
git init -b main
echo "# Adversarial Review Pilot — Vault link extractor" > README.md
echo "" >> README.md
echo "Sandbox for cc-sdd v61 + codex-plugin-cc v62 comparison pilot." >> README.md
echo "Storm Bear vault corpus reference: 04 Reviews/(C) 2026-05-08 adversarial-review comparison pilot setup plan.md" >> README.md
git add README.md
git commit -m "Initial commit: pilot sandbox"

# Verify clean state
git log --oneline
```

**Verification:** `git log --oneline` shows 1 commit "Initial commit: pilot sandbox".

### Step B — Install cc-sdd v61 (Pilot #1 — Stratum A) (~10-15 min)

```bash
cd ~/sandbox/adversarial-review-pilot

# Install cc-sdd Skills mode for Claude Code
npx cc-sdd@latest --claude-skills

# Verify install
ls -la .claude/skills/
ls -la .kiro/

# Expected directory structure:
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
- If skills not visible after install → run `/reload-plugins` in Claude Code
- If `.claude/` directory not created → cc-sdd may need explicit `--target=claude` flag (check cc-sdd docs)

**Verification:** All 9 kiro-* skill directories exist under `.claude/skills/`.

### Step C — Install codex-plugin-cc v62 (Pilot #1.5 — Stratum B) (~15-20 min)

In **Claude Code session** (cd-ed into `~/sandbox/adversarial-review-pilot`):

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

`/codex:setup` will prompt for:
- ChatGPT subscription credentials OR OpenAI API key
- Codex backend connectivity test
- Default model selection (GPT-5.2 or similar)
- Reasoning effort level (low/medium/high)

**Troubleshooting:**
- If marketplace add fails → check Claude Code version supports plugin marketplace
- If auth fails → verify ChatGPT subscription active OR `OPENAI_API_KEY` env var set
- If `/reload-plugins` doesn't expose `/codex:*` commands → restart Claude Code session

**Verification:** Type `/codex:` in Claude Code; autocomplete should show 7 commands (review, adversarial-review, rescue, status, result, cancel, setup).

### Step D — Implement feature (~30-45 min, with Claude Code main-session help, NO review tools)

In Claude Code main session (no `/kiro-*` or `/codex:*` invocations yet):

```
"Build a Python CLI tool that extracts all markdown links from .md files
in a directory. Output JSON list of {file, line, link_text, link_url,
link_type}. Use regex-only parsing (no markdown library). Sync I/O.
No caching. Skip links inside code blocks. Include pytest tests with
sample fixtures."
```

Claude Code will implement. Operator commits when complete:

```bash
git add -A
git commit -m "Feature: markdown link extractor CLI (regex-based, no caching)"
```

**Verification:** `git log --oneline` shows 2 commits. Tests pass: `pytest`. Example invocation works: `python extractor.py path/to/sample.md`.

---

## Measurement phase (1 week background, ~30-45 min/day active)

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

Create comprehensive findings document:

**Path:** `04 Reviews/(C) 2026-05-15 adversarial-review comparison pilot findings.md`

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

### Setup phase failures

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

1. Read this document (`04 Reviews/(C) 2026-05-08 adversarial-review comparison pilot setup plan.md`)
2. Verify pre-setup checklist
3. Execute Step A → Step B → Step C → Step D in single setup-day sitting
4. Schedule Day 1-7 measurement across calendar
5. Write findings to `04 Reviews/(C) YYYY-MM-DD adversarial-review comparison pilot findings.md`
6. Update vault state files (CLAUDE.md state-block + pilot-ranking + GOALS.md) with findings
7. Inform v66 mini-audit deliberation

**Context preserved:** This document is self-contained; no Claude session memory required.

---

## Cross-references

- `_state/pilot-ranking-2026-05-07.md` — pilot ranking (#1 cc-sdd + #1.5 codex-plugin-cc)
- `03 Projects/cc-sdd - Beginner Analysis/` — v61 wiki + Pattern #76 N=1 baseline evidence
- `03 Projects/codex-plugin-cc - Beginner Analysis/` — v62 wiki + counter-evidence to Pattern #76
- `_patterns/03-active-candidates.md` — Pattern #76 entry (will be updated post-pilot)
- `_patterns/05-recent-additions.md` — v63 EARLY mini-audit decisions
- `04 Reviews/(C) 2026-05-07 Pattern Library mini-audit post-v61 ...md` — v63 audit document (Pattern #76 registration)

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

**Plan version:** 1.0 (initial draft 2026-05-08)
**Next update trigger:** Pilot setup attempt (any blockers/learnings update plan)
