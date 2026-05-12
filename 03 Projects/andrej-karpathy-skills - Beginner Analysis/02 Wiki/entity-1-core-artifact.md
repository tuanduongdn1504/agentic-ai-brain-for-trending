# Entity 1 — andrej-karpathy-skills core artifact

## 1. One-line identity

A single-skill behavioral-guideline plugin distributed via Claude Code marketplace + per-project CLAUDE.md curl + Cursor rule, distilling Andrej Karpathy's public X-tweet observations on LLM coding pitfalls into 4 actionable principles.

## 2. Author + ownership

- **Owner:** [forrestchang](https://github.com/forrestchang) (X: [@jiayuan_jy](https://x.com/jiayuan_jy))
- **Also founder of:** [Multica](https://github.com/multica-ai/multica) — *"open-source platform for running and managing coding agents with reusable skills"* (linked in karpathy-skills README opening line as cross-promotion)
- **Org type:** Solo individual
- **Author archetype:** Solo-engineer + ecosystem-portfolio-builder (2-product portfolio: karpathy-skills viral artifact + Multica platform play); **Pattern #19 first-mover-authority-without-lineage ecosystem-portfolio-builder sub-type strengthening N=2** (was gotalab v61 N=1 with cc-sdd + skillport + uxaudit + claude-code-marimo 4-product portfolio; now forrestchang N=1 within sub-type with karpathy-skills + Multica 2-product portfolio = N=2 sub-type)

## 3. Scale + velocity (corpus-extreme)

| Metric | Value |
|--------|------:|
| Stars | **121,227** |
| Forks | **12,246** |
| Watchers | 639 |
| Commits | 28 |
| Created | 2026-01-27 |
| Last push | 2026-04-20 |
| Days at v63 ship (2026-05-09) | **102** |
| **Stars/day average** | **~1,186** |

**Corpus-extreme placements:**
- 4th-largest-stars-count in corpus (after AutoGPT v59 184K / cc-sdd-Oh My Claudecode-corpus-historical-leader / few others); **largest stars/day velocity in corpus history at observation window**
- **3× the velocity of mattpocock-skills v57** (Pattern #52 N=1 baseline at ~370 stars/day at flag-time)

## 4. License + governance

- **License:** MIT (declared in `plugin.json` and `SKILL.md` frontmatter; LICENSE file implicit)
- **Governance files:** README.md / README.zh.md / CLAUDE.md / CURSOR.md / EXAMPLES.md / .claude-plugin/marketplace.json / .claude-plugin/plugin.json / skills/karpathy-guidelines/SKILL.md / .cursor/rules/karpathy-guidelines.mdc
- **No CONTRIBUTING.md, no CODE_OF_CONDUCT.md, no SECURITY.md** — minimal-governance solo-individual default

## 5. The 4 principles (verbatim summary)

1. **Think Before Coding** — Don't assume / don't hide confusion / surface tradeoffs. State assumptions, present multiple interpretations, push back, stop when confused.
2. **Simplicity First** — Minimum code. No speculative features / abstractions / configurability / impossible-error handling. "Would a senior engineer say this is overcomplicated?"
3. **Surgical Changes** — Touch only what you must. Match existing style. Don't refactor the orthogonal. Remove only YOUR-introduced orphans.
4. **Goal-Driven Execution** — Transform tasks into verifiable success criteria. Loop independently when criteria are strong.

## 6. Distribution architecture

| Path | Mechanism | Activation |
|------|-----------|------------|
| **A — Claude Code plugin** | Marketplace add + install | Per-vault, persistent |
| **B — per-project CLAUDE.md** | curl into target repo | Per-project, manual |
| **C — Cursor rule** | `.cursor/rules/karpathy-guidelines.mdc` with `alwaysApply: true` | Per-project, automatic |

**Sync discipline:** all 3 source files (CLAUDE.md / SKILL.md / `.mdc`) maintained manually in parallel per CURSOR.md operator note. Acceptable at 65-line content scale.

## 7. i18n

- **EN** — primary (README.md / CLAUDE.md / CURSOR.md / EXAMPLES.md / SKILL.md)
- **ZH** — README.zh.md only (other content not localized)

No JP / KR / VN / DE / FR coverage.

## 8. Intellectual lineage

- **Direct source:** Andrej Karpathy [X tweet](https://x.com/karpathy/status/2015883857489522876) — explicitly cited with URL
- **Karpathy in Storm Bear corpus:** **most-corpus-cited individual** (LLM Wiki pattern → Storm Bear vault foundation per root CLAUDE.md "Who I Am & My Purpose"; autoresearch v8 = 1st corpus-explicit Karpathy citation)
- **Methodology lineage:** NONE other (no SDD / BMM / TDD-explicit / spec-kit / GSD references)

**Pattern #57 Recursive Corpus Reference:** karpathy-skills v63 IS a corpus-cited-individual derivative — derivative-distillation inherits Karpathy lineage from corpus-foundation; **57c-positive-corpus-citation** mechanism strengthens at v63.

## 9. What it is NOT

- NOT a methodology framework (no spec/plan/task scaffold)
- NOT a curated multi-skill collection (single skill only)
- NOT a runtime tool (no executable code; behavioral overlay only)
- NOT a methodology-influence-node creator (DERIVATIVE distillation, not original methodology)
- NOT anti-vibe-coding workflow critique (NEUTRAL on workflow; anti-overengineering on output)
- NOT cross-corpus-citing (does NOT reference cc-sdd / spec-kit / mattpocock / OpenSpec / etc. — Karpathy is the ONLY external reference)

## 10. Operational deployability for Storm Bear vault

**Setup cost:** ~2 minutes (single `/plugin install` command).

**Deployment plan (if pilot-elected):**
```
# In Claude Code, from any vault project:
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

**Measurable signals after deployment:**
- Diff-line-to-request-trace ratio (Surgical Changes principle)
- Clarification-questions-before-implementation count (Think Before Coding principle)
- Lines-of-code-per-feature ratio (Simplicity First principle)
- Test-first vs implementation-first cadence (Goal-Driven Execution principle)

**1-week measurement window proposed** (parallel to or after cc-sdd / codex-plugin-cc pilots).

## 11. Pattern Library positioning

| Pattern | Contribution at v63 |
|---------|---------------------|
| **#52 EXTREME-VIRAL-VELOCITY** | **N=2 strengthening** (3× mattpocock velocity); un-stale-flag candidate at v66 audit |
| **#19 individual-influence-node** | **derivative-distillation NEW sub-archetype N=1**; ecosystem-portfolio-builder N=2 (with Multica) |
| **#18 Layer 2 multi-platform** | **Cursor-as-secondary-platform NEW sub-axis N=1** at single-skill scale |
| **#57 Recursive Corpus Reference** | **57c corpus-foundation-individual inheritance strengthening** |
| **#59 Plugin Marketplace** | **EXTREME-VIRAL solo-individual scale NEW observation** |
| **#51 Vibe-Coding Spectrum** | NEW NEUTRAL-with-anti-overengineering pole observation (spectrum reformulation evidence) |

## 12. Verdict on substitution question (preview)

User's prior question: *can mattpocock-skills + andrej-karpathy-skills combo replace cc-sdd?*

**Preview answer (full analysis in entity 4 + Phase 4b):** **NO.** karpathy-skills + mattpocock-skills are both **behavioral-overlay artifacts** (modify HOW the LLM thinks); cc-sdd is a **methodology workflow harness** (adds NEW workflow phases: spec → plan → tasks → impl + adversarial review). Different categories. Combo can complement cc-sdd (orthogonal layers) but cannot substitute.

## 13. Strategic significance for Storm Bear

- **Highest viral-velocity wiki subject ever** — Pattern #52 N=2 with 3× mattpocock baseline is *the* finding of v63
- **Karpathy-corpus-foundation echo** — corpus-most-cited individual returns at v63 via derivative-distillation = cleanest Pattern #57 57c instance in corpus
- **Pilot candidate ranking:** Tier-2 (lower-priority than cc-sdd v61 / codex-plugin-cc v62 / free-claude-code v60); operational-relevance MEDIUM (orthogonal complementary layer); novelty MEDIUM (derivative not original methodology); pattern-contribution HIGH
