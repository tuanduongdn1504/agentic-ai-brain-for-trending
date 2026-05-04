# (C) 12+ Specialized Agents (Amelia Dev + PM + Architect + UX)

> **Type:** Entity — building block
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README + VN summary]] §2, [[(C) CHANGELOG skim summary]] §7-8
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

BMAD-METHOD ships **12+ named agent personas** (PM, Architect, Developer, UX, +8 unnamed in README). Each agent = a markdown role definition inside the BMM core module. v6.3 consolidated 3 dev-adjacent agents (Barry/Quinn/Bob) into single **Amelia** developer persona — signaling a **trend toward fewer, broader agents**, opposite of GSD's 33-agent expansion path.

## 2. Key claims

1. **12+ domain experts** — README verbiage, no full roster publicly listed
2. **Named in README:** PM, Architect, Developer (Amelia), UX
3. **Named in CHANGELOG v6.3:** Barry, Quinn, Bob (consolidated out), Amelia (kept)
4. **Consolidation over expansion** — v6.3 removed 3 agents, not added
5. **Markdown-defined** — agents are `.md` files in `bmad/bmm/agents/`, not code
6. **Party Mode enabled** — agents can collaborate in single session (see [[(C) Party Mode + Scale-Domain-Adaptive Planning]])

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 12+ agents total | README.md | High (explicit number) |
| Amelia absorbed Barry/Quinn/Bob in v6.3 | CHANGELOG 2026-04-09 | High (changelog verbatim) |
| Agents = markdown files | CONTRIBUTING + AGENTS.md | High (dev convention) |
| Full roster location | Inferred: `bmad/bmm/agents/` installed module | Medium — not verified post-install |

## 4. How it works

### Agent definition shape (inferred)

```markdown
# Amelia — Developer
role: full-stack developer persona
scope: code implementation, TDD, review
tools: [file-ops, test-runner, linter]
collaborates-with: [PM, Architect, UX]
```

(Schema conjectured from skills-based architecture + CONTRIBUTING §3. Actual schema in `tools/skill-validator.md` — not fetched.)

### Invocation

- User runs `bmad-help` in Claude Code
- User or orchestrator routes task to appropriate agent
- Agent reads `.md` definition, adopts persona, executes workflow
- In Party Mode: multiple agents active in same conversation, each maintaining persona

### Consolidation mechanics (v6.3)

Barry (quick-flow-solo-dev) + Quinn (QA) + Bob (Scrum Master) merged into Amelia:

- **Barry's speed-focus** → Amelia "quick mode" flag
- **Quinn's QA lens** → Amelia gained test-review scope
- **Bob's process lens** → Amelia gained ceremony awareness
- Result: one agent, broader competence, fewer cognitive branches for user

## 5. Worked example

**Scenario:** User wants to ship a feature end-to-end

**Pre-v6.3:** User decides — Barry for speed? Quinn for QA? Bob for retro? Amelia for full build? Four choices, three are wrong.

**Post-v6.3:** User invokes Amelia. Amelia reads project context, Scale-Domain-Adaptive kicks in, Amelia sizes work appropriately. One invocation, no decision fatigue.

**Party Mode example:** For feature needing design + review:
1. User invokes Party Mode with PM + Architect + Amelia + UX
2. PM states requirements
3. UX challenges assumptions
4. Architect proposes structure
5. Amelia implements while others watch
6. All in one session — transcript captures multi-agent reasoning

## 6. Edges + failure modes

- **Over-consolidation risk** — Amelia absorbs too much, loses specialization. v6.3 is recent (April 2026); early for judgment
- **No published roster** — users discover agents experientially. Onboarding friction for "what agents exist?"
- **Breaking changes** — v6.3 broke Barry/Quinn/Bob invocations. Existing user scripts referencing those agents failed until migration
- **Party Mode coordination** — N agents in one session can lose coherence; no known orchestration guarantees
- **Skill validator dependency** — malformed agent `.md` fails `npm run validate:skills` and won't install

## 7. Related concepts

- [[(C) 34+ Workflows + 5 Module Ecosystem]] — agents execute workflows
- [[(C) Party Mode + Scale-Domain-Adaptive Planning]] — multi-agent mechanics
- [[(C) VN Localization + Storm Bear Direct Relevance]] — agents speak VN? (Unverified)

## 8. Cross-project (T1 siblings)

| Framework | Agent count | Naming convention | Consolidation trend? |
|-----------|-------------|-------------------|----------------------|
| **BMAD** | 12+ (shrunk from 15 in v6.2) | Human names (Amelia, PM) | ✅ Yes — consolidating |
| GSD | 33 | Role names (`backend-dev`, `security-reviewer`) | ❌ No — adding |
| gstack | ~15 | Specialist roles | Stable |
| Superpowers | ~10 patterns (not "agents" framed) | Methodology tags | N/A |
| ECC | Many small skills | Task-scoped skills | N/A |

**Divergence:** BMAD and GSD go opposite directions on agent-count philosophy. BMAD → fewer + broader. GSD → more + narrower. Empirical test TBD which serves users better.

## 9. Open questions

- Full roster of 12+ — where listed? → Q17
- Are agents multilingual (VN)? → Q24
- Why opposite direction from GSD on agent-count? → Q19
- Will Amelia fragment again if she gets too broad? → Q25

## 10. Decision log

- **v4 (June 2025):** Agents established as framework primitives
- **v6.0 beta (Jan 2026):** Agents converted to skills
- **v6.3 (April 2026):** Barry/Quinn/Bob → Amelia consolidation
- **Ongoing:** Marketplace browser may allow community-contributed agents

## 11. Storm Bear relevance

- **Scrum-coach angle:** Bob (Scrum Master) was a dedicated agent pre-v6.3 — now folded into Amelia. If Storm Bear uses BMAD for Scrum coaching, Amelia's process awareness may be weaker than dedicated Bob was. **Verification needed via pilot.**
- **VN team adoption:** No evidence agents respond in VN. Agents likely use same language as user prompt — VN input → VN response plausible but unverified
- **Party Mode for retros:** Potential value for running retro conversations with multi-agent perspectives (PM + UX + Amelia). Candidate for Storm Bear pilot

## 12. Migration / adoption notes

- Pre-v6.3 users: update scripts that invoked Barry/Quinn/Bob to invoke Amelia
- New adopters (post-v6.3): ignore Barry/Quinn/Bob entirely, learn only current roster
- If on `@next`: expect further consolidation signals — watch for PM/Architect/UX merge candidates

## 13. References

- `README.md` — "12+ domain experts"
- `CHANGELOG.md` v6.3.0 (2026-04-09) entry
- `AGENTS.md` — repo contrib contract (not agent roster)
- `tools/skill-validator.md` — unfetched; agent `.md` schema source of truth
- Parent wiki: [[(C) index]]
