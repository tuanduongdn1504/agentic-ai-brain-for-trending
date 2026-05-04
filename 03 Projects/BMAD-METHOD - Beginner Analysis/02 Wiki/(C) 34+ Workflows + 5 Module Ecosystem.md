# (C) 34+ Workflows + 5 Module Ecosystem

> **Type:** Entity — architecture concept
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README + VN summary]] §3-4, [[(C) CHANGELOG skim summary]] §6-9
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

BMAD-METHOD ships **34+ workflows** (largest workflow library in T1) organized across **5 modules** — BMM (core), BMB (meta-builder), TEA (test), BMGD (game dev), CIS (creative). v6.3 introduced a **community module browser** (official / community / custom-URL tiers), evolving BMAD from framework → platform with marketplace ambitions.

## 2. Key claims

1. **34+ workflows** in BMM core module alone — claimed in README
2. **5 modules ship today:** BMM, BMB, TEA, BMGD, CIS
3. **BMB is meta** — it's a module that builds more modules/agents/workflows
4. **Universal source support** (v6.3) — modules install from GitHub, GitLab, Bitbucket, self-hosted
5. **Community module browser** (v6.3) — three-tier selection (official / community / custom URL)
6. **Workflow ≠ agent ≠ skill** — distinct abstractions in BMAD taxonomy

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 34+ workflows count | README.md §Modules | High (explicit) |
| 5-module roster + purposes | README.md §Modules | High |
| BMB introduced v6.0.0-alpha.14 | CHANGELOG | High |
| TEA externalized in v6.0.0-alpha.3 | CHANGELOG | High |
| Community browser v6.3 | CHANGELOG 2026-04-09 | High |
| Universal source support | CHANGELOG v6.3 | High |

## 4. How it works

### Module anatomy

Each module = a directory with:
- `agents/` — markdown agent definitions
- `workflows/` — multi-step procedures
- `templates/` — document scaffolds (PRD, architecture, etc.)
- `skills/` — v6 unit of installation
- `manifest` — tells installer what to register

### Installation flow

1. User runs `npx bmad-method install`
2. CLI prompts module selection: BMM (always) + optional BMB/TEA/BMGD/CIS
3. v6.3+: also prompts "source" — official / community / custom URL
4. CLI fetches module from source, validates skills (`npm run validate:skills`), installs into project `.claude-plugin/` or IDE equivalent
5. Agents + workflows now available via `bmad-help`

### Workflow execution

A workflow is a **sequenced procedure** an agent runs. Example (speculative, not fetched):

```
workflow: create-prd
agent: PM
steps:
  1. Gather product requirements (user interview)
  2. Apply Amazon Working Backwards framework
  3. Draft PR/FAQ document
  4. Validate with Architect (handoff)
  5. Finalize PRD template
```

34+ such workflows in BMM. Titles include PRD creation, architecture design, test strategy, retrospective facilitation — full list not fetched (in installed BMM module, not README).

## 5. Worked example — 5-module usage

**Scenario: Startup building a game**

- **BMM** core — standard agile workflows, PRD, architecture
- **BMGD** (Game Dev Studio) — Unity/Unreal-specific workflows, shader review agent, game-design doc templates
- **CIS** (Creative Intelligence Suite) — brainstorming + design thinking for gameplay innovation
- **TEA** (Test Architect) — risk-based test strategy for gameplay bugs
- **BMB** (BMad Builder) — when startup needs custom workflow not in stock modules, use BMB to generate new `.md` agent/workflow

**All 5 modules install alongside each other. User switches context via agent invocation.**

## 6. Edges + failure modes

- **Module bloat** — installing all 5 modules loads many agents; cognitive overload
- **Community module quality variance** — v6.3 marketplace tier has no quality gate (official-only has LLC review; community has none stated)
- **Universal source = supply chain risk** — installing from arbitrary GitLab URL = trusting that code. No signing
- **Workflow count inflation** — 34+ sounds impressive, but not all are equally used. Long tail likely
- **Breaking changes per module** — v6.x churn means modules can break against core between alpha versions
- **BMGD late expansion** — v6.0.0-alpha.18 reorganized game-dev module; early adopters likely broke
- **TEA externalization** (v6.0.0-alpha.3) — moving TEA out of core means TEA updates decouple but also introduce install-order dependencies

## 7. Related concepts

- [[(C) 12+ Specialized Agents (Amelia Dev + PM + Architect + UX)]] — agents live inside modules
- [[(C) Party Mode + Scale-Domain-Adaptive Planning]] — workflows can invoke Party Mode
- [[(C) VN Localization + Storm Bear Direct Relevance]] — are modules translated too, or only README?

## 8. Cross-project (T1 + taxonomy)

| Framework | Module/extension story | Count | Marketplace? |
|-----------|-------------------------|-------|--------------|
| **BMAD** | 5 modules, marketplace browser v6.3 | 5 + community | ✅ Emerging |
| GSD | 33 agents + commands | No module layer | ❌ |
| gstack | ~15 specialist roles | Flat structure | ❌ |
| Superpowers | Pattern library + skills | Skill index | ❌ |
| ECC | Skills catalog | Flat | ❌ |

**BMAD = only T1 with explicit module hierarchy + marketplace model.** Convergent with NPM / Claude Code plugin marketplace paradigms.

### Comparison to T5 (deer-flow SuperAgent)

- deer-flow has Skill System (progressive loading) — similar "install-time discovery" pattern
- BMAD installs at `bmad-method install` time; deer-flow loads at runtime
- Different model: BMAD = static bundle; deer-flow = dynamic loader

## 9. Open questions

- Full 34+ workflow roster — documented anywhere public? → Q17
- Community module quality process — who reviews? → Q20
- Will community modules ever be paid? → Q6 existing
- TEA externalization — performance penalty? → Q26
- BMB can generate modules — bootstrapping loop? Can BMB generate BMB? → Q27

## 10. Decision log

- **v4.0.0:** BMM established as core module (framework birth)
- **v4.10.0+:** CIS added (creative domain)
- **v4.20.0:** BMGD introduced (game dev)
- **v6.0.0-alpha.3:** TEA externalized (separable test module)
- **v6.0.0-alpha.14:** BMB introduced (meta-builder)
- **v6.0.0-alpha.18:** BMGD major expansion
- **v6.3 (2026-04-09):** Community module browser + universal source support

**Trajectory:** Core (v4) → domain-specific (CIS/BMGD mid-v4) → meta-tooling (BMB v6) → ecosystem platform (browser v6.3). Classic "framework → platform" evolution.

## 11. Storm Bear relevance

- **Scrum coaching workflows:** BMM's agile workflows directly relevant. Storm Bear could evaluate how BMAD's retrospective / sprint-planning workflows compare to practice
- **CIS for facilitation:** Creative Intelligence Suite = brainstorming/design thinking workflows. Potential pairing with Storm Bear's coach-facilitator role
- **BMB as pilot:** If Storm Bear builds custom agents, BMB is the onramp. `npx bmad-method install` + select BMB → get agent builder scaffolding
- **VN module candidacy:** No VN-localized workflow module exists. Potential contribution: fork BMM, translate workflow prompts to VN, submit as community module

## 12. Migration / adoption notes

- Pre-v6 users: v4 module layout ≠ v6 module layout; migration required at v6 upgrade
- v6.0 → v6.3: TEA externalization may require explicit install flag (verify in CHANGELOG per user)
- Community modules: no guaranteed compatibility matrix; track `@next` channel for churn signals

## 13. References

- `README.md` §Modules
- `CHANGELOG.md` — v4.0.0, v4.10, v4.20, v6.0.0-alpha.3/14/18, v6.3.0
- Parent wiki: [[(C) index]]
- Sibling T1 wikis for cross-reference:
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) index.md`
  - `../../gstack - Beginner Analysis/02 Wiki/(C) index.md`
