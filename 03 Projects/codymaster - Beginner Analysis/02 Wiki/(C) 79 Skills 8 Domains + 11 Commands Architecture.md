# (C) 79 Skills 8 Domains + 11 Commands Architecture

> **Type:** Entity — building block
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README + VN summary]] §4, §7-8; [[(C) Skills + Commands + Lifecycle cluster summary]] §2-7
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

codymaster ships **79 skills** (actual folder count, not the 60+/68+ claimed in README/plugin.json) organized across **8 domains**, plus **11 workflow commands** and a CLI surface with ~10-15 `cm <verb>` operational commands. This is the **largest skill surface in T1 corpus by 2×** (BMAD 12+ agents + 34+ workflows ≈ 46; codymaster 79 skills). Skills live as markdown definitions under `skills/cm-<name>/`, invoked by the `cm` TypeScript CLI backed by SQLite + FTS5 Smart Spine.

## 2. Key claims

1. **79 skills actual** — counted from repo `skills/` folder listing
2. **"60+" in README / "68+" in plugin.json** — marketing undersells by ~10-20 skills
3. **8 domains:** Engineering / Operations / Product-UX / Growth / Enterprise / Self-Healing / Orchestration / Skills-Management
4. **All skills prefixed `cm-`** — most consistent namespace in T1
5. **11 workflow commands** in `commands/` folder (bootstrap, build, content, continuity, debug, demo, deploy, plan, review, track, ux)
6. **CLI verbs** via `cm <verb>` — additional ~10-15 operational commands
7. **Skills are markdown + TS tooling** — not pure-markdown like BMAD (needs `cm` binary runtime)
8. **Largest skill surface in T1** — 2× BMAD/GSD, 5-8× others

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 79 skills | `skills/` GitHub API listing 2026-04-19 | High |
| 60+ README claim | README.md | High |
| 68+ plugin.json claim | `.claude-plugin/plugin.json` | High |
| 11 commands | `commands/` API listing | High |
| CLI verbs existence | README install instructions (cm status, cm dashboard, cm brain, cm chain, cm deploy, cm agent, cm sprint) | Medium — exact count not enumerated |
| 8 domains | README §The 60+ Skill Arsenal | High |

## 4. How it works

### Skill anatomy (inferred)

Each `skills/cm-<name>/` folder likely contains:
- `SKILL.md` — skill definition with role, inputs, outputs, prompts
- Templates / examples (some skills have supporting files)
- Possibly TS helpers for skills that need code logic

### Invocation flow

1. User runs `cm <workflow-command>` or triggers skill via Claude/Cursor
2. `cm` CLI (TypeScript compiled) consults Smart Spine (SQLite+FTS5 store)
3. Smart Spine's `selectTopSkills()` chooses 2-3 relevant skills for current task
4. Selected skills load (Progressive L0/L1/L2 depth)
5. Skills execute, share output via Context Bus
6. Telemetry → cm-skill-health → (eventually) cm-skill-evolution if health degrades

### Skill dependencies

- `cm-codeintell` → CodeGraph (AST memory)
- `cm-continuity` → Working-tier memory
- `cm-deep-search` → Semantic-tier memory (vector)
- `cm-notebooklm` → Cloud Brain sync
- Self-healing skills (cm-skill-health, cm-skill-evolution, cm-skill-search, cm-skill-share, cm-skill-chain, cm-skill-index, cm-skill-mastery, cm-learning-promoter) → framework operates on itself

## 5. Worked example — a feature ships through codymaster

**Scenario:** Add new SaaS feature end-to-end

| Stage | Command/Skill | What happens |
|-------|---------------|--------------|
| 1. Idea | cm-brainstorm-idea + cm-jtbd | Facilitate ideation, identify Jobs-to-be-done |
| 2. Plan | cm plan / cm-planning / cm-sprint-bus | Generate sprint plan |
| 3. Design | cm-design-studio, cm-design-system, cm-ux-master | UI/UX proposals + design-system alignment |
| 4. Test First | cm-tdd | Write failing tests before code |
| 5. Code | cm-autopilot + cm-clean-code | Generate + refine implementation |
| 6. Debug | cm-debugging | Triage + fix |
| 7. Quality | cm-quality-gate + cm-code-review | Gate checks |
| 8. Security | cm-security-gate + cm-secret-shield | Vuln + leak scan |
| 9. Isolate | cm-git-worktrees | Deploy-candidate isolation |
| 10. Deploy | cm-safe-deploy | Gated pipeline |
| 11. Monitor | cm-post-deploy-canary | Canary deploy + rollback signals |
| 12. Document | cm-dockit + cm-auto-publisher | Auto-generate docs |
| 13. Learn | cm-skill-evolution | Framework learns from this run |

**13 steps, 13+ skills involved.** In practice, many are invoked automatically by workflow commands (cm deploy triggers security + canary + safe-deploy implicitly).

## 6. Edges + failure modes

### Scale edges
- **Cognitive load** — 79 skills impossible to memorize. SkillsBench `selectTopSkills()` exists precisely for this. If auto-selection fails, user is stuck browsing 79.
- **Skill discoverability** — `cm-skill-search` + `cm-skill-index` are themselves skills. Meta-recursion may confuse new users.
- **Skill quality variance** — 79 skills from 1 author over ~6 months. Likely wide quality variance. Self-healing helps but doesn't guarantee uniform maturity.

### Namespace edges
- **cm- prefix conflicts** — unlikely but possible if another framework also uses cm prefix
- **Versioning per skill** — unclear; all skills move together with plugin version?

### Runtime edges
- **TS + SQLite dependency** — not pure-markdown. If `better-sqlite3` fails on user's Node version, entire framework breaks
- **npm global install** — permission issues on some systems
- **Platform variance** — 8+ platforms, but each adapter may lag behind Claude Code (primary)

### Marketing vs reality
- Users reading "60+" may expect fewer than 79 and be pleasantly surprised
- Users reading "20+ Commands" expecting 20 workflow commands, finding 11 files, may feel misled (if they don't count CLI verbs)

## 7. Related concepts

- [[(C) 5-Tier Memory + Smart Spine + CodeGraph]] — the brain that these skills use
- [[(C) Self-Healing Skills + SkillsBench Dynamic Selection]] — how skills maintain themselves + which 2-3 get selected
- [[(C) VN-Author Native + Tody Le + Storm Bear Peer-Relevance]] — who built this

## 8. Cross-project (T1 siblings comparison)

| Framework | Skill/agent count | Naming | Runtime |
|-----------|-------------------|--------|---------|
| **codymaster** | **79 skills** | cm- prefix | TS + SQLite + MD |
| BMAD | 12+ agents + 34+ workflows ≈ 46 | Named personas (Amelia) | Pure MD + Node CLI |
| GSD | 33 agents + 83 commands = 116 | Role-based | MD + TS |
| gstack | ~15 specialist roles | Specialist name | TypeScript |
| Superpowers | ~10 patterns | Methodology tags | MD + bash |
| ECC | Many small skills | Flat | MD + code samples |

→ **codymaster largest by skill count.** GSD has higher combined surface (agents+commands=116) but different structure. BMAD closer to codymaster (46) but via agents+workflows distinction.

### Domain-breadth comparison
| Domain | codymaster | BMAD | GSD | Others |
|--------|-----------|------|-----|--------|
| Engineering | ✅ | ✅ | ✅ | ✅ |
| Operations/DevOps | ✅ deep | ❌ | Partial | Partial |
| Product/UX | ✅ deep | ✅ | ❌ | ❌ |
| Growth/Marketing | ✅ (unusual) | ❌ | ❌ | ❌ |
| Self-Healing | ✅ (unique) | ❌ | ❌ | ❌ |
| Security | ✅ deep | ❌ | ❌ | ECC only |

→ codymaster has **broadest domain coverage** in T1, including growth/marketing (unusual) and self-healing (unique).

## 9. Open questions

- True skill count — 79 stable or growing? (Q2)
- Marketing undersell rationale? (Q2)
- CLI verb count — is "20+ Commands" a legitimate combined claim? (Q3)
- Per-skill version? Or monolithic? (new — Q33)
- Quality uniformity across 79 skills? Audit data? (new — Q34)

## 10. Decision log

- **v1-v4 era** (~2025 — inferred from 11 tags): skill count grew from presumably ~10-20 to ~60-80
- **v5.x** (current npm): 79 skills shipped
- **v6.0.0** (website claim): likely same 79 + some polish
- **Self-Healing introduced** (version unknown): framework starts maintaining itself

## 11. Storm Bear relevance

Storm Bear's role overlap (Scrum coach + dev + product-adjacent):
- **High relevance:** cm-retro-cli, cm-sprint-bus, cm-planning, cm-brainstorm-idea, cm-jtbd, cm-continuity
- **Medium:** cm-tdd, cm-debugging, cm-code-review, cm-clean-code, cm-design-system
- **Low:** cm-ads-tracker, cm-cro-methodology, cm-growth-hacking (marketing-adjacent)
- **Meta:** cm-notebooklm (Cloud Brain sync), cm-skill-evolution (framework learns)

**Pilot candidate:** use cm-retro-cli + cm-sprint-bus for one sprint cycle with VN team. Native-VN-author alignment = possibly better intuitions than BMAD for VN Scrum culture.

## 12. Migration / adoption notes

- No prior version for most users — codymaster is niche (38 stars). Fresh adoption.
- Install `cm` globally first, then register plugin in chosen host (Claude Code / Cursor / Gemini)
- Expect some skills broken on first run — Self-Healing will repair on second run
- `cm-example` and `cm-how-it-work` skills exist — use first as onboarding

## 13. References

- `README.md` §60+ Skill Arsenal + §Commands
- `skills/` GitHub folder listing (79 items)
- `commands/` GitHub folder listing (11 items)
- `package.json` bin field (cm, codymaster)
- `.claude-plugin/plugin.json` (68+ claim)
- Parent: [[(C) index]]
