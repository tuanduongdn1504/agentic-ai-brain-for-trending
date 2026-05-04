# (C) 110 Skills (44 gws-* + 10 personas + 56 recipes)

> **Type:** Entity — building block, novel taxonomy
> **Parent:** [[(C) index]]
> **Sources:** skills/ folder listing + [[(C) 110 Skills + Helper Commands cluster summary]] §2-6
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

googleworkspace/cli ships **110 agent skills** organized in a **three-category taxonomy** — 44 `gws-*` service skills (functional), 10 `persona-*` role bundles (by user), 56 `recipe-*` workflow automations (by task). This is the **largest skill surface in corpus** (surpasses codymaster v12's 79) and introduces a **novel multi-axis classification** (function × role × workflow) not observed in any prior wiki.

## 2. Key claims

1. **110 total skills** (verified from skills/ API listing; README claims 100+)
2. **3-category taxonomy** — gws-* / persona-* / recipe-* — novel in corpus
3. **44 gws-* service skills** — one-per-service + sub-operations (Gmail has 8 sub-skills; deepest)
4. **10 persona skills** — role-based bundles, first in corpus
5. **56 recipe skills** — workflow automations, largest single category
6. **Install granularity** — all-or-selected via `npx skills add ... --select <name>`
7. **OpenClaw support** — symlink-based install
8. **Skills are lighter than codymaster's** — metadata layer on Discovery-generated commands, not self-contained workflows

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 110 folder count | skills/ API listing 2026-04-19 | High |
| 3-category taxonomy | Directory naming prefixes | High |
| Gmail 8-skill granularity | Listing: gws-gmail + 7 sub-skills | High |
| Persona role list (10) | Listing enumeration | High |
| Recipe list (56) | Listing enumeration | High |
| Install via npx skills | README §AI Agent Skills | High |
| Lighter than codymaster | Inferred — gws skills wrap Discovery; no full workflow logic | Medium |

## 4. How it works

### Skill anatomy (inferred from npx skills pattern)

Each `skills/<skill-name>/` directory likely contains:
- `SKILL.md` — agent-facing definition (how to use)
- Metadata (package.json or similar) — dependencies, version
- Possibly test fixtures or examples

### Installation flow

```bash
# Browse skills
gh repos/googleworkspace/cli/skills/   # see directory

# Install all 110
npx skills add https://github.com/googleworkspace/cli

# Install specific bundle
npx skills add https://github.com/googleworkspace/cli --select gws-gmail
npx skills add https://github.com/googleworkspace/cli --select persona-exec-assistant
npx skills add https://github.com/googleworkspace/cli --select recipe-meeting-prep

# OpenClaw install (symlink)
[platform-specific path]
```

### Invocation model

Agent reads SKILL.md → learns which `gws` commands to invoke → executes via subprocess → parses JSON output.

**Contrast with codymaster:** codymaster skills have their own runtime (Smart Spine, 5-Tier Memory, cm CLI). gws skills are **pure knowledge assets** that teach the agent how to drive the `gws` binary.

## 5. Worked example — persona-exec-assistant

User installs persona-exec-assistant. Skill's SKILL.md likely describes:

```markdown
# persona-exec-assistant

You are an executive assistant agent. You have access to:

- Calendar: gws calendar +agenda, gws calendar +insert
- Email: gws gmail +triage, gws gmail +send, gws gmail +reply
- Drive: gws drive files list, gws drive +upload
- Docs: gws docs +write
- Workflow: gws workflow +meeting-prep, gws workflow +standup-report

Common tasks:

## Morning briefing
1. gws calendar +agenda today
2. gws gmail +triage priority
3. Compose summary with gws docs +write

## Meeting preparation
1. gws workflow +meeting-prep <calendar-event-id>
2. Share attendees list

## Daily standup aggregation
1. gws workflow +standup-report
...
```

**Agent reads persona → executes `gws` commands → achieves executive-assistant-style output.**

## 6. Worked example — recipe-backup-sheet-as-csv

Recipe skills are more concrete. recipe-backup-sheet-as-csv SKILL.md likely:

```markdown
# recipe-backup-sheet-as-csv

Backup a Google Sheet to a CSV file in Google Drive.

## Steps
1. gws sheets +read --params '{"spreadsheetId":"<ID>"}' > /tmp/sheet.json
2. Convert JSON to CSV (provided script or jq transform)
3. gws drive +upload /tmp/backup.csv --params '{"parents":["<FOLDER>"]}'

## Parameters
- sheet_id: string (required)
- output_folder_id: string (optional, default: sheet's parent folder)
- filename_pattern: string (optional, default: "{sheet_name}-{date}.csv")
```

**Agent receives user's "backup this sheet" request → loads recipe → executes 3-step pipeline → confirms completion.**

## 7. Edges + failure modes

### Skill staleness
- Discovery API evolves; gws-* skills may reference deprecated methods
- Mitigation: cm-skill-health-equivalent not present in gws (gws trusts upstream Google stability)

### Persona over-scope
- persona-exec-assistant covers many tools; agent may get confused by breadth
- Mitigation: recipe-level entry point for narrow tasks

### Recipe breakage
- 56 recipes maintained manually; API changes = recipe breakage
- No self-healing like codymaster v12

### Category overlap
- `gws-gmail-triage` (service skill) vs `recipe-label-and-archive-emails` (recipe) — both about email organization
- Agent may not know which to prefer
- Needs disambiguation in SKILL.md content (not verified post-install)

### Install size
- All 110 skills = large docs corpus. Agent context window stress if all loaded.
- Mitigation: `--select` granular install + dynamic skill selection (agent side)

## 8. Related concepts

- [[(C) Dynamic Discovery Service Architecture]] — what skills wrap
- [[(C) CONTEXT + CLAUDE + AGENTS cluster summary]] — rules for agents using skills
- [[(C) Multi-Flow OAuth2 + Model Armor + Validation Discipline]] — security layer skills depend on

## 9. Cross-project comparison

### Skill count vs peers

| Project | Tier | Skill count | Classification |
|---------|------|-------------|----------------|
| gws (v13) | **T4** | **110** | **3-category (function / role / workflow)** |
| codymaster (v12) | T1 | 79 | 8-domain functional |
| GSD (v5) | T1 | 33 agents + 83 commands | Role-based |
| BMAD (v11) | T1 | 12+ agents + 34+ workflows | Named personas + workflows |
| notebooklm-py (v7) | T4 | 1 mega-SKILL.md | Single |

→ **gws has largest skill count AND most sophisticated taxonomy.** First corpus project with 3-axis classification.

### Skill weight comparison

| Project | Skills hold logic? | Runtime dependency |
|---------|--------------------|--------------------|
| codymaster | Yes (Smart Spine executes) | cm binary + SQLite + memory tiers |
| BMAD | Yes (agent personas) | Node + markdown parse |
| gws | **No (metadata only)** | **gws Rust binary does work** |
| notebooklm-py | Yes (single mega-skill) | Python API + CLI |

→ **gws skills are lightest** — pure documentation. This is deliberate: Discovery does the work, skills guide the agent to use it correctly.

**Architectural insight:** skills-as-metadata + runtime-as-binary is a cleaner separation than skills-as-logic. Trade-off: can't do skill-level customization without modifying Rust code.

## 10. Persona-layer architectural contribution

The persona-* layer is **novel in agent-framework corpus**. Prior taxonomies:

- **By task** — Superpowers (TDD), BMAD workflows
- **By function** — codymaster cm-* prefix domains
- **By role** — GSD 33 agents (backend-dev, security-reviewer)
- **By API** — notebooklm-py (single API bundle)
- **By persona (NEW)** — gws persona-exec-assistant, persona-team-lead, etc

**Persona = who uses it, bundling multiple task + function + API skills.**

**Why now:**
- Workspace has 11+ services — too many for a user to orchestrate manually
- Roles cluster typical usage — execs need calendar+email+docs, IT admins need admin+drive+groups
- Persona bundles reduce cognitive load: "pick your role" vs "pick your skill"

**Predicts:** future agent frameworks will add persona layer. codymaster's cm-autopilot + workflow commands half-hint at it; gws formalizes it.

## 11. Open questions

- Skill category ratios (44/10/56) intentional? (Q28)
- Persona implementation — composition or standalone? (Q29)
- Recipe validation policy — who ensures 56 recipes still work? (Q8)
- Skill growth trajectory to v1.0? (Q31)
- Category overlap resolution (gws-gmail-triage vs recipe-label-archive)? (new — Q37)
- Persona bundle size — does installing persona-* install dependent gws-* + recipe-*? (new — Q38)

## 12. Decision log

- **Initial**: gws-* service skills only (likely v0.1-0.5 era)
- **Mid-phase**: persona layer added — indicates user research showed role-based entry helps
- **Recipe proliferation**: community + team-driven additions
- **v0.22.5 current**: 110 skills
- **v1.0 target** (speculation): likely 150+ with recipe growth primary

## 13. Storm Bear relevance

**Persona-exec-assistant + persona-project-manager + persona-team-lead = direct Storm Bear Scrum coaching fit.**

Pilot plan:
1. Install persona-project-manager bundle
2. Use for 1 sprint cycle
3. Compare with cm-sprint-bus + cm-retro-cli (codymaster v12)
4. Document which bundle/skill serves Scrum-coach role better

## References

- skills/ folder listing (GitHub API)
- README §AI Agent Skills
- [[(C) 110 Skills + Helper Commands cluster summary]]
- Parent: [[(C) index]]
