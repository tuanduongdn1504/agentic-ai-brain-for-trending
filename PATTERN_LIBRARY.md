# Storm Bear Pattern Library

> **Purpose:** Authoritative register of cross-wiki patterns observed across the Storm Bear corpus. Refactored 2026-04-27 session 67 — bulk content moved to `_patterns/` chapter files for agent-context-fit.

## Current state (post-v56-mini-audit, preserved 6 cycles)

- **Confirmed:** 39 (UNCHANGED post-mini-audit; 2nd CONSERVATIVE-DISCIPLINE audit in corpus history; ZERO top-level state transitions)
- **Active candidates:** 17
- **Stale candidates:** 3 (#45 Dual-Licensing / #52 Extreme-Viral-Velocity / #72 PolyForm-Noncommercial)
- **Retired:** 9
- **Observation-tracks:** 6
- **Total:** 74 full / 56 active
- **Ratio:** 17:39 = **0.436:1** — first sub-0.45:1 ratio in corpus history (achieved at v53 mini-audit; preserved through v54 + v55 + v56 + v56-mini-audit)
- **Buffer:** 0.514 below 0.95:1 mini-audit trigger — NEW LARGEST in corpus history maintained 6 cycles
- **Streaks:**
  - **20-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES (v37-v56) — NEW LONGEST in corpus history**
  - **39-consecutive Storm Bear meta-entity (v10-v56)** — v56 is **1st under STRICT amendment session 66** with **2 criteria PASSED (b + d)** post-audit Q1-resolution (criterion-d via Skyvern v24→n8n v56 32-wiki gap)
  - **2 consecutive CONSERVATIVE-DISCIPLINE mini-audits** (post-v54 session 65 + post-v56 session 67)
- **Library-vocabulary:** 13 distinct pattern-statement structural forms (UNCHANGED)
- **Promotion criteria:** 6 structural-promotion criteria (UNCHANGED)
- **Pattern #18 reaches 10th refinement** (extends from 9 baseline at v53 mini-audit; most-refined pattern in library; NEW = Layer 0 0b horizontal-aggregation N=2 promotion at v56-mini-audit)
- **Pattern #29 sub-context taxonomy now has 6 sub-contexts** (5 absent-LICENSE + 1 NEW non-commercial-restriction-custom-license; license-axis is corpus's most-richly-categorized pattern axis)
- **Audit triggers RESET. Next triggers:** active candidate count ≥30 (currently 17 — 13-candidate runway) / ratio >0.95:1 mini / v60 wiki natural cadence

**Audit document:** `04 Reviews/(C) 2026-04-27 Pattern Library mini-audit post-v56 (5 candidates, ZERO state transitions, 2nd conservative-discipline audit).md`

## Vault State Architecture

**Why refactored:** Pre-refactor PATTERN_LIBRARY.md was 536KB / ~135K tokens — too large for any agent to read without context-thrashing. Bulk content moved to `_patterns/` chapter files post-session-67 vault-wide refactor.

**Chapter files in `_patterns/`:**

| Chapter | Content | Size |
|---|---|---|
| `_patterns/01-audit-history.md` | Full audit summary v21-v55 (every direct-update + mini-audit + full audit decision history) | 136KB |
| `_patterns/02a-confirmed-patterns-pre-v42.md` | Confirmed patterns #1-50ish (originally-confirmed pre-v13 + promotions through v36 mini-audit) | 92KB |
| `_patterns/02b-confirmed-patterns-v42-plus.md` | Confirmed patterns from v42 mini-audit onwards (#46 + #48 + #58 + #57 + #38 + sub-variant promotions) | 106KB |
| `_patterns/03-active-candidates.md` | 17 active candidates with formal statements + observations + N tracking | 62KB |
| `_patterns/04-retired-stale.md` | 9 retired patterns + 3 stale candidates with retirement / stale-flag rationale | 11KB |
| `_patterns/05-recent-additions.md` | Post-v54 strengthening notes + post-v54 mini-audit decisions + post-v55 strengthening notes | 22KB |

**Reading discipline for agents:**
- Never read more than 1 chapter file per session — context-thrashing risk
- Use `awk` via Bash for surgical line-range extracts when looking up specific Pattern #
- For most pattern-pre-check tasks: read `_patterns/03-active-candidates.md` + `_patterns/05-recent-additions.md` together (74KB combined ≈ ~18K tokens — safe)
- For full pattern definition lookup: identify which chapter (02a or 02b) by pattern number, read only that one

**Authoritative state pointer:** Chapter files are the authoritative state record. Root PATTERN_LIBRARY.md (this file) is entry-point shim only. Updates go to chapter files; root only updated when adding new chapters or major state-summary changes.


## Formal criteria (preserved from pre-refactor)

**Confirmed pattern criteria (pattern PROMOTED to confirmed if any of 6 met):**

1. **Default ≥3-cross-tier:** ≥3 observations across 2+ tiers
2. **Structural-N=2:** 2 structurally-unambiguous observations (e.g., 2 distinct organizations both implementing pattern with same architectural signature; license-axis-invariance across maximally-divergent licenses)
3. **Spectrum-N=2:** 2 distinct points on a multi-point architectural spectrum (introduced v29 mini-audit; e.g., spec-kit anti-vibe + awesome-design-md pro-vibe)
4. **Variant-within-pattern-at-N=2:** 2 observations of NEW within-pattern variant (introduced v29 mini-audit)
5. **Meta-pattern-at-N=3-consolidation:** Meta-pattern wrapping ≥3 sub-variants (introduced v31 mini-audit; e.g., #68 Awesome-List-Genre wraps build-your-own-x + awesome-design-md + awesome-mcp-servers)
6. **Sister-archive-structural-N=2:** 2 structurally-parallel archives with mechanism-distinct sub-variant divergence axes (introduced v53 mini-audit; e.g., #38 system-prompts-leaks + learn-coding-agent)

**Pattern statuses:**
- **Confirmed:** Meets one of 6 criteria above; entered formal pattern register
- **Refined:** Confirmed but formulation adjusted by later evidence
- **Candidate:** 1-2 observations OR confined to single tier; tracked but not formal
- **Stale-Candidate (NEW v21 audit):** N=1 after 5+ wikis without additional evidence; keep-observing, lower priority
- **Retired:** Explicitly invalidated OR absorbed into meta-pattern OR no longer relevant
- **Observation-Track (NEW v29 audit):** Observation worth tracking but not active candidate; may evolve to candidate or stay as historical observation

## Pattern-statement structural forms in library (13)

1. Categorical sub-variants (e.g., Pattern #29 absent-LICENSE 1/2/3/4/5)
2. Sub-distinctions within variants (e.g., Pattern #17 variant 2 → 2a corporate-official / 2b corporate-research-OSS)
3. Sub-signals ordinal scale (e.g., Pattern #31 Pro-docs-depth 0-4)
4. Sub-axes (e.g., Pattern #28 routing-abstraction / native-multi-provider / verification-not-routing)
5. Multi-point spectra (e.g., Pattern #47 vision-primary / hybrid / DOM-only — retired v46)
6. Multi-layer formulations (e.g., Pattern #18 Layer 0 + Layer 1 + Layer 2)
7. Cross-pattern same-archetype correlations (e.g., Pattern #44 44d ↔ Pattern #17 2b)
8. Cross-pattern coupled-design correlations (e.g., Pattern #22 22c ↔ Pattern #18 OpenCode-primary)
9. Pre-registered conditional retirement triggers (e.g., Pattern #47 retired at v46)
10. Retirement-to-OBSERVATION-TRACK pathway (e.g., Pattern #47 → OT)
11. Runtime-primacy-choice sub-observations (e.g., Pattern #18 OpenCode-primary)
12. Mechanistically-distinct sub-variants (e.g., Pattern #57 57a authorial-intent vs 57b selection-topology)
13. Observation-track sub-categorization (e.g., Pattern #66 event-based / by-design — introduced v53 mini-audit)

## N=1 candidate stale-flag tracking protocol (introduced v27 audit)

**Trigger:** N=1 candidate enters stale-tracking at registration with explicit stale-check window (typically +5 wikis) + retirement-check window (typically +10 wikis).

**Stale-flagged at registration (current open windows post-v55):**
- 57b aggregator-mediated multi-citation (registered v50; stale-check v55 → preserved as 57b CONFIRMED sub-variant within Pattern #57)
- 50c aggregator-with-commercial-product-entry-bundled (registered v50)
- 29-absent-3 aggregator-mixed-license (registered v50; reached structural-N=2 at v51)
- 22c authoritative-with-shim (registered v47; narrowed at v53 mini-audit)
- 28-verification-not-routing (registered v47)
- 18 OpenCode-primary (registered v47; reached structural-N=2 at v52; promoted at v53 mini-audit)
- 22d identical-mirror (registered v51)
- 57c forward-citation-then-wiki (registered v51; reached structural-N=2 at v52; promoted at v53 mini-audit)
- 58c rebrand-repo-keep-npm-package + dual-bin-alias (registered v52)
- 50d incubation-waitlist-as-funnel-terminus (registered v52)
- 57d machine-readable-vendoring-metadata (registered v54)
- 58e successor-repo-not-rename (registered v54)
- 18 Pi-SDK-substrate (registered v54; corrected to N=1 at v54 mini-audit)
- 29-absent-5 commercial-content-creator-affiliate-funnel (registered v55)
- 50e content-creator-affiliate-funnel-with-own-product (registered v55)
- OT 10th outside-scope sub-type content-creation-automation-tutorial (registered v55)


## Pattern application guidelines

- New wikis check against this library at Phase 0.5 overlap pre-check
- Reject standalone candidates with >70% overlap → route to within-pattern strengthening
- Pattern observations feed back into library via direct-update OR mini-audit OR full audit
- Audit triggers: candidate count ≥30 OR ratio >0.95:1 (mini) / >1.05:1 (full)


## Next audit trigger

**Current state:** 17 active candidates / 39 confirmed = 0.436:1 ratio (NEW LARGEST buffer 0.514 below 0.95:1 mini-audit trigger; preserved 6 cycles post-v53 mini-audit through post-v56 mini-audit; 2nd consecutive CONSERVATIVE-DISCIPLINE mini-audit at session 67).

**Audit triggers RESET at v53 mini-audit. Next triggers:**
- Active candidate count ≥30 (currently 17 — 13-candidate runway)
- v60 wiki natural cadence (+5-wiki natural cadence from v55)
- Ratio >0.95:1 mini-audit / >1.05:1 full audit


## References

- Pattern Library audit documents: `04 Reviews/(C) 2026-04-XX Pattern Library *.md` (12+ documents v21-v54)
- Routine v2.1: `05 Skills/llm-wiki-routine-v2.1.md`
- Vault state architecture (refactor 2026-04-27 session 67): root CLAUDE.md "Vault State Architecture" section
