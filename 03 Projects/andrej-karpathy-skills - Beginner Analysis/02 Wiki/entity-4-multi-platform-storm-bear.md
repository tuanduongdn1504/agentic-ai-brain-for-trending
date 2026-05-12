# Entity 4 — Multi-platform single-skill + Storm Bear meta

## 1. Multi-platform delivery at single-skill scale

karpathy-skills ships to 2 distinct host platforms (Claude Code + Cursor) with a 3rd auxiliary path (per-project curl). All 3 paths deliver **identical 4-principle content** in 3 platform-specific format wrappers:

| Platform | File | Format | Activation |
|----------|------|--------|-----------|
| Claude Code (plugin) | `skills/karpathy-guidelines/SKILL.md` | YAML frontmatter + Markdown | Plugin marketplace install |
| Claude Code (per-project) | `CLAUDE.md` (root) | Plain Markdown | curl into target project |
| Cursor (rule) | `.cursor/rules/karpathy-guidelines.mdc` | Cursor rule format with `alwaysApply: true` | Auto-applies on Cursor open |

**Manual sync discipline** per CURSOR.md note: contributors keep 3 files in parallel manually. Acceptable at 65-line content scale; would not scale to multi-skill collection.

## 2. Pattern #18 Layer 2 NEW sub-axis — single-skill multi-platform

Pattern #18 Layer 2 sub-archetypes catalog through v63:

| Sub-archetype | Scale | Mechanism | First observation |
|---------------|-------|-----------|-------------------|
| Content-transformation | various | Domain-specific | N=8 prior T4 entrants |
| Protocol-translation runtime | API-level | Runtime adapter | free-claude-code v60 |
| Per-tool format translation | install-time | Format converter | claude-context v44 (?) |
| Install-time per-platform skill format translator | framework | cc-sdd at framework scale | cc-sdd v61 (8 platforms) |
| Cross-vendor-platform-bridge-as-plugin | plugin | Cross-vendor cooperation | codex-plugin-cc v62 |
| **Multi-platform single-skill manual sync** | **skill** | **Manual file-parallel** | **andrej-karpathy-skills v63 NEW** |

**Distinction from cc-sdd v61:** cc-sdd auto-generates per-platform files via install-time translator; karpathy-skills manually maintains file-parallel.

**Sub-axis registration at v63:** Pattern #18 Layer 2 multi-platform-single-skill-manual-sync N=1 stale-flagged. Un-stale criterion: 2nd single-skill artifact shipping to 2+ platforms with manual-sync discipline.

## 3. Cursor as 2nd platform — corpus-rare observation

Most prior corpus subjects target Claude Code as primary platform. Cursor as 2nd-target appears in:

- **agent-skills-of-vercel v51** (?) — multi-IDE corporate
- **cc-sdd v61** — 8-platform spec lists Cursor in "stable" tier (1 of 2 stable)
- **andrej-karpathy-skills v63** — Claude Code + Cursor primary equals

**Pattern #18 Cursor-as-secondary observation N=2-N=3 strengthening** within already-confirmed Pattern #18 multi-platform behavior.

## 4. Storm Bear meta-entity — Phase 0.9 STRICT 1-of-4 INCLUDE evidence

**Streak counter post-v63:** Storm Bear meta-entity 4-consecutive post-v60-RESTART (v60 PASS + v61 PASS + v62 PASS + v63 PASS).

**8-instance Phase 0.9 post-amendment window (v56-v63):** v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS / v61 PASS / v62 PASS / v63 PASS = **7 PASS / 1 SKIP = 87.5% INCLUDE rate**.

**Criterion-(d) STRONGEST instance in 8-window:** Karpathy is corpus-foundation-individual. v63 derivative-distillation = direct corpus-foundation inheritance. 57c-positive-corpus-citation strengthens.

## 5. Operational deployability assessment for Storm Bear vault

**Setup cost:** ~2 minutes (single `/plugin install` from any vault project).

**Per-vault vs per-project decision:**
- Per-vault install = 4 principles apply to ALL vault Claude Code sessions
- Per-project install = scoped to specific project (e.g., a real-monorepo software development project)
- **Recommendation:** per-project for monorepo software-development pilots (avoid pollution of wiki-build sessions where 4 principles would interfere with routine v2.1's defined Phase 0-6 workflow)

**Compatibility with existing pilot plan:**
- cc-sdd v61 (Tier-1 pilot) — adds spec/plan/task workflow primitives; orthogonal to karpathy-skills behavioral overlay
- codex-plugin-cc v62 (Tier-1.5 pilot) — adds adversarial-review primitive; orthogonal to karpathy-skills
- free-claude-code v60 (Tier-1 pilot) — proxy layer; orthogonal to karpathy-skills

**Stack possibility:** karpathy-skills + cc-sdd + codex-plugin-cc + free-claude-code = 4-layer stack (proxy + methodology + adversarial-review + behavioral-overlay) — all orthogonal layers.

## 6. Risks specific to karpathy-skills deployment

| Risk | Mitigation |
|------|-----------|
| **Behavioral overlay conflicts with routine v2.1 workflow** — 4 principles' "Think Before Coding" could interfere with Phase 0 probe deterministic execution | Per-project install only; never per-vault |
| **Karpathy citation could go stale** — Karpathy could publicly disagree with distillation | Treat as forrestchang's take, not Karpathy-endorsed |
| **Manual sync drift in installed plugin** — if forrestchang updates README but not SKILL.md, installed version diverges | Pin specific version; track upstream churn |
| **Anti-overengineering principles + complex monorepo pilot** — could create over-cautious behavior | Use Tradeoff Note's "trivial-task judgment" exception |

## 7. Pilot deployment recommendation

**Tier-2 pilot priority** at v63 (lower than Tier-1 cc-sdd / codex-plugin-cc / free-claude-code).

**Rationale:**
- Operational utility = MEDIUM (behavioral overlay; not adding new workflow primitives)
- Novelty = MEDIUM (derivative-distillation, not original methodology)
- Pattern-contribution = HIGH (Pattern #52 N=2-N=3 + Pattern #19 sub-type a4 + Pattern #18 sub-axis)
- Setup cost = VERY LOW (~2 min)

**Recommended deployment timing:** AFTER cc-sdd v61 + codex-plugin-cc v62 comparison-pilot (Week 1-2 from current); karpathy-skills as Week 3+ deployment to test layered stack with already-deployed methodology harness.

## 8. The substitution question — formal verdict

**User's question (v63 ship context):** Can mattpocock-skills + andrej-karpathy-skills combo replace cc-sdd?

### Comparative analysis

| Dimension | cc-sdd v61 | mattpocock-skills v57 | andrej-karpathy-skills v63 | Substitutability |
|-----------|------------|------------------------|----------------------------|------------------|
| **Category** | Methodology workflow harness | Curated skills collection | Single behavioral-guideline-as-skill | **Different** |
| **Adds new workflow phases** | YES (spec → plan → tasks → impl + adversarial review) | NO (skills are complementary) | NO (behavioral overlay only) | **NO** |
| **EARS-format requirements** | YES | NO | NO | **NO** |
| **Adversarial review architecture** | YES (kiro-review + kiro-impl + kiro-debug + kiro-verify-completion) | NO | NO | **NO** |
| **File Structure Plan primitive** | YES | NO | NO | **NO** |
| **P-wave parallel-execution annotation** | YES | NO | NO | **NO** |
| **Brief.md discovery routing artifact** | YES | NO | NO | **NO** |
| **Anti-vibe positioning** | YES (with pragmatic acknowledgment) | NO (skill-curation neutral) | NO (anti-overengineering only) | **NO** |
| **Multi-platform install-time translator** | YES (8 platforms) | NO (Claude Code only) | NO (manual 2-platform sync) | **NO** |
| **Behavioral guidelines** | Implicit | Implicit per-skill | EXPLICIT (4 principles) | Combo offers HERE |
| **Curated skills collection** | NO | YES (19 skills) | NO (1 skill) | mattpocock offers HERE |

### Verdict

**NO. Combo cannot substitute cc-sdd. Different categories.**

cc-sdd is a **methodology workflow harness** — it adds NEW workflow phases (spec/plan/tasks/impl), NEW primitives (FSP, EARS, P-wave annotation, brief.md), and NEW architectural roles (kiro-review subagent for adversarial review).

mattpocock-skills + karpathy-skills is a **behavioral-overlay + skills-collection combo**. Together they:
- Modify HOW the LLM thinks (karpathy-skills 4 principles)
- Add narrow-task skill capabilities (mattpocock 19 skills)

Neither contributes the methodology-workflow-harness primitives that constitute cc-sdd's value.

**What the combo CAN do:**
- Complement cc-sdd as orthogonal layer (behavioral overlay BENEATH methodology workflow)
- Substitute for *some* coding-discipline aspects when SDD methodology overhead is too heavy

**What the combo CANNOT do:**
- Replace SDD methodology phases
- Replace adversarial review architecture
- Replace EARS-format requirements engineering
- Replace P-wave parallel-execution discipline

**Strategic frame:** treat as orthogonal layers, not substitutes. cc-sdd answers "WHAT methodology"; karpathy-skills answers "HOW to behave within ANY methodology"; mattpocock-skills answers "WHAT narrow-task capabilities."

## 9. Cross-pattern coupled-design observation

v63 wiki demonstrates **Pattern #18 (multi-platform) × Pattern #52 (extreme-viral) × Pattern #19 (individual-influence) × Pattern #57 (recursive corpus reference)** all activating in single subject. **4-pattern coupled instantiation** = sister to v60's 4-pattern coupling (P57 polarity × P51 vibe × P19 archetype × tier).

**Pattern Library library-vocabulary item #10 candidate:** "4-pattern-coupled-design" as recurring meta-observation across viral-velocity subjects.

## 10. Storm Bear pilot ranking update

| Pilot | Priority | Tier | Setup | Window |
|-------|---------|-----|-------|--------|
| cc-sdd v61 | #1 | Tier-1 | ~1h | 1-week |
| codex-plugin-cc v62 | #1.5 | Tier-1 | ~30min | 1-week comparison-pilot to cc-sdd |
| free-claude-code v60 | #2 | Tier-1 | ~1h | 1-week |
| n8n v56 | #3 | Tier-2 | varies | 2-week+ |
| **andrej-karpathy-skills v63** | **#3.5 NEW** | **Tier-2** | **~2min** | **Week 3+ stack-layer test** |

karpathy-skills inserts at #3.5 — Tier-2 priority below n8n; can be quickly stacked AFTER Tier-1 pilots establish baseline.

## 11. v66 audit pre-registered items from v63 ship

(Phase 5 will fully register; preview):

1. **Pattern #52 N=2-N=3 retroactive strengthening** (mattpocock + codex-plugin-cc + karpathy-skills)
2. **Pattern #52 sustained-velocity check at v69** (defer formal un-stale to ~6mo+ window)
3. **Pattern #19 a4 derivative-distillation NEW sub-type N=1 stale-flagged**
4. **Pattern #19 ecosystem-portfolio-builder N=2 strengthening** (gotalab v61 + forrestchang v63)
5. **Pattern #18 Layer 2 multi-platform-single-skill-manual-sync NEW sub-axis N=1 stale-flagged**
6. **Pattern #57 57c corpus-foundation-individual inheritance strengthening**
7. **Pattern #51 NEW NEUTRAL-with-anti-overengineering pole observation** (spectrum reformulation evidence; v66 deferred deliberation)
8. **Pattern #59 EXTREME-VIRAL solo-individual scale NEW observation**

## 12. v63 corpus-firsts summary (preview)

8 corpus-firsts at v63:

1. Largest stars/day velocity in corpus history (~1,186/day)
2. Pattern #52 N=2 strengthening (was OBSERVATIONAL FLAG N=1 stale-since-v50)
3. Karpathy-corpus-foundation-individual derivative-distillation (Pattern #19 a4 NEW sub-type)
4. Multi-platform single-skill manual sync (Pattern #18 NEW sub-axis)
5. Bilingual EN+ZH at single-skill scale (corpus-rare)
6. Single-skill plugin in marketplace (vs multi-skill collections)
7. Karpathy explicit X-tweet citation in skill artifact (Pattern #57 57c-strongest instance)
8. forrestchang ecosystem-portfolio-builder N=2 sub-type (sister to gotalab v61)

## 13. Closing strategic frame

v63 karpathy-skills wiki ship clarifies that **viral velocity ≠ operational priority**. Despite 121K stars (corpus-extreme), karpathy-skills ranks Tier-2 in pilot deployment because methodology harnesses (cc-sdd) and adversarial-review architectures (codex-plugin-cc) deliver more workflow-primitive value per setup-hour for Storm Bear's Goal #2 ("build software with these tools").

**The 4 principles ARE valuable** — but as orthogonal behavioral overlay, not as primary methodology. Use karpathy-skills as a STACK LAYER, not a STACK ROOT.
