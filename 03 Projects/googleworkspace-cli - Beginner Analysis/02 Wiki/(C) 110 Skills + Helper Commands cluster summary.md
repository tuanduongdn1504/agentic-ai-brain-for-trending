# (C) 110 Skills + Helper Commands cluster summary — googleworkspace/cli

> **Sources:** skills/ folder listing (110 dirs) + README §AI Agent Skills + README §Helper Commands + AGENTS.md §Helper Commands anti-patterns
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

Skills + helper commands are the **two user-facing abstraction layers** of gws beyond raw Discovery API access. Together they define how AI agents do real work. Clustered because:
- Skills are the large static surface (110 items)
- Helper commands are the curated dynamic surface (~20+ `+verb` commands)
- Both solve the "raw API is too low-level for agents" problem with different strategies

## 2. 110 skills — the exact count

From skills/ folder API listing (2026-04-19):

**Total: 110 directories** — matches README claim "100+".

Breakdown by category:

### A. gws-* service skills (44 items)

One skill per service + key sub-operations:

**Admin:**
- gws-admin-reports

**Calendar:**
- gws-calendar, gws-calendar-agenda, gws-calendar-insert

**Chat:**
- gws-chat, gws-chat-send

**Classroom:**
- gws-classroom

**Docs:**
- gws-docs, gws-docs-write

**Drive:**
- gws-drive, gws-drive-upload

**Events:**
- gws-events, gws-events-subscribe, gws-events-renew

**Forms:**
- gws-forms

**Gmail (most granular — 8 skills):**
- gws-gmail, gws-gmail-send, gws-gmail-read, gws-gmail-reply, gws-gmail-reply-all, gws-gmail-forward, gws-gmail-triage, gws-gmail-watch

**Keep:**
- gws-keep

**Meet:**
- gws-meet

**Model Armor:**
- gws-modelarmor, gws-modelarmor-create-template, gws-modelarmor-sanitize-prompt, gws-modelarmor-sanitize-response

**People:**
- gws-people

**Script:**
- gws-script, gws-script-push

**Shared (utilities):**
- gws-shared

**Sheets:**
- gws-sheets, gws-sheets-read, gws-sheets-append

**Slides:**
- gws-slides

**Tasks:**
- gws-tasks

**Workflow (orchestration):**
- gws-workflow, gws-workflow-email-to-task, gws-workflow-file-announce, gws-workflow-meeting-prep, gws-workflow-standup-report, gws-workflow-weekly-digest

**Observations:**
- Gmail has deepest granularity (8 skills) — makes sense given email is most-invoked
- Workflow has 6 orchestration skills — composite across services
- Classroom/Forms/Keep/Meet/People/Slides/Tasks each get 1 skill each (less common)

### B. persona skills (10 items) — NOVEL layer

Role-based skill bundles:

1. **persona-content-creator** — content production workflows
2. **persona-customer-support** — ticket handling, knowledge lookup
3. **persona-event-coordinator** — event planning + invites
4. **persona-exec-assistant** — calendar + email + meeting prep
5. **persona-hr-coordinator** — onboarding + admin tasks
6. **persona-it-admin** — user/group management + drive admin
7. **persona-project-manager** — sprint + status + tracking
8. **persona-researcher** — search + synthesize + report
9. **persona-sales-ops** — CRM-adjacent + reporting
10. **persona-team-lead** — 1:1s + team coordination + reporting

**Each persona likely bundles multiple gws-* + recipe skills into a coherent role context.**

**Novel in corpus:** prior skills taxonomies group by function (cm-tdd / cm-debugging in codymaster) or by methodology stage (Superpowers 7-stage). gws is first to group by **who uses them** (role/persona).

### C. recipe skills (56 items)

Workflow recipes — concrete multi-step automations:

**Backup + organize (8):**
- recipe-backup-sheet-as-csv, recipe-bulk-download-folder, recipe-organize-drive-folder, recipe-find-large-files, recipe-save-email-attachments, recipe-save-email-to-doc, recipe-email-drive-link, recipe-share-folder-with-team

**Events + calendar (9):**
- recipe-batch-invite-to-event, recipe-block-focus-time, recipe-create-events-from-sheet, recipe-create-meet-space, recipe-find-free-time, recipe-reschedule-meeting, recipe-schedule-recurring-event, recipe-share-event-materials, recipe-plan-weekly-schedule

**Email workflows (7):**
- recipe-create-gmail-filter, recipe-create-vacation-responder, recipe-forward-labeled-emails, recipe-label-and-archive-emails, recipe-send-team-announcement, recipe-review-meet-participants, recipe-draft-email-from-doc

**Docs + Sheets (11):**
- recipe-compare-sheet-tabs, recipe-copy-sheet-for-new-month, recipe-create-doc-from-template, recipe-create-expense-tracker, recipe-create-feedback-form, recipe-create-presentation, recipe-generate-report-from-sheet, recipe-share-doc-and-notify, recipe-sync-contacts-to-sheet, recipe-collect-form-responses, recipe-create-shared-drive

**Tasks (3):**
- recipe-create-task-list, recipe-review-overdue-tasks, recipe-log-deal-update

**Classroom (1):**
- recipe-create-classroom-course

**Drive monitoring (2):**
- recipe-watch-drive-changes, recipe-review-meet-participants

**Meetings (3):**
- recipe-post-mortem-setup, recipe-review-meet-participants (duplicate?)

### Installation

```bash
# All skills
npx skills add https://github.com/googleworkspace/cli

# Select bundle
npx skills add https://github.com/googleworkspace/cli --select gws-drive

# Specific persona or recipe
npx skills add https://github.com/googleworkspace/cli --select persona-exec-assistant
npx skills add https://github.com/googleworkspace/cli --select recipe-meeting-prep
```

**OpenClaw support:** symlink-based install via skills tooling.

## 3. Skill count comparison across corpus

| Framework | Skill count | Naming pattern |
|-----------|-------------|----------------|
| googleworkspace/cli (v13) | **110** | gws-* + persona-* + recipe-* |
| codymaster (v12) | 79 | cm-* prefix |
| GSD (v5) | 33 agents + 83 commands | role-based |
| BMAD (v11) | 12+ agents + 34+ workflows | Named personas (Amelia) |
| gstack (v3) | ~15 | Specialist roles |
| Superpowers (v2) | ~10 | Methodology |
| ECC (v1) | Many small | Flat |

→ **googleworkspace/cli has the largest skill surface in corpus by ~40%.** Surpasses codymaster v12's 79.

**However:** gws skills are lighter/more-generated than codymaster's. gws skills wrap Discovery API + persona/recipe metadata; codymaster skills carry workflow logic.

## 4. Helper commands — the `+verb` layer

### Purpose (from AGENTS.md §Helper Commands)

Helpers provide:
1. **Multi-step orchestration** — `gws gmail +triage` = list + classify + label
2. **Format translation** — markdown → Gmail HTML
3. **Multi-API composition** — `gws workflow +meeting-prep` spans calendar + drive + docs

### Anti-patterns (explicitly must NOT)

- Wrap a single Discovery API call
- Expose existing response data via custom flags
- Replicate Discovery params as custom flags

**Discipline:** `--params` + `--format`/`jq` already handle simple cases. Helpers earn their existence via composition.

### Helper inventory (from README)

**auth (3):**
- `gws auth setup`, `gws auth login`, `gws auth export`

**Drive (1):**
- `gws drive +upload` (multipart)

**Gmail (4):**
- `gws gmail +send`, `gws gmail +reply`, `gws gmail +triage`, `gws gmail +watch`

**Sheets (2):**
- `gws sheets +append`, `gws sheets +read`

**Calendar (2):**
- `gws calendar +agenda`, `gws calendar +insert`

**Docs (1):**
- `gws docs +write`

**Chat (1):**
- `gws chat +send`

**Workflow (2+):**
- `gws workflow +standup-report`, `gws workflow +meeting-prep`

**Events (2):**
- `gws events +subscribe`, `gws events +renew`

**Schema (1):**
- `gws schema <method>`

**Total identified: ~20 helper commands** (may be more — full list requires post-install inspection)

## 5. Skills vs helpers — two abstractions, same goal

| Abstraction | Form | Invoked by | Strength | Limitation |
|-------------|------|-----------|----------|-----------|
| **Skills** (110) | Markdown `SKILL.md` + metadata | AI agent reads, invokes gws CLI | High-volume, narrative, discoverable | Static — must update when APIs change |
| **Helpers** (~20 `+verb`) | Compiled Rust code | User/agent invokes directly | Fast, validated, composed | Hand-maintained, limited number |

**Design insight:** two-layer strategy. Bulk coverage via skills (auto-generable), precision/composition via helpers (hand-written).

## 6. Persona + recipe layer — novel taxonomy

**Persona skills (10) and recipe skills (56) are new in corpus.** No prior framework organizes skills by role or workflow-type.

### Why it matters

- **Persona** = entry point for users who know their role but not specific tool
  - "I'm an exec assistant" → persona-exec-assistant → bundles relevant gws + recipes
- **Recipe** = entry point for users who know the task but not the tools
  - "I need to backup this sheet as CSV" → recipe-backup-sheet-as-csv

**Classification axes:**
- gws-* skills = by **what it does** (functional)
- persona-* skills = by **who does it** (role)
- recipe-* skills = by **why/when** (workflow)

### Parallel to BMAD's Party Mode + codymaster's cm-retro-cli etc

- BMAD has named personas (Amelia, PM, Architect) — personalities
- codymaster has role-adjacent skills but not explicit persona bundles
- gws persona skills = **first explicit role-bundled skill taxonomy** in corpus

## 7. Skill count growth trajectory

gws at v0.22.5 (pre-1.0) = 110 skills. Growth over 44 releases = roughly ~2.5 skills/release.

**Predictions:**
- Likely to hit 150+ by v1.0
- Persona count may grow slowly (10 covers most roles)
- Recipe count likely to grow aggressively (user-contributed wisdom)
- gws-* service skills grow only when new Workspace APIs ship

## 8. Agent invocation patterns

From README + CONTEXT.md:

**Pattern 1: agent picks skill, invokes gws**
```
Agent sees persona-exec-assistant skill → reads SKILL.md →
uses gws calendar +agenda today → gws gmail +triage → ...
```

**Pattern 2: user invokes helper directly via agent**
```
User: "Triage my inbox"
Agent: gws gmail +triage (helper does the work)
```

**Pattern 3: agent composes via Discovery**
```
Agent: gws drive files list --params '{"fields":"id,name"}' 
       → gws drive files get ... 
       → gws sheets +append ...
```

**Pattern 4: schema-first**
```
Agent: gws schema drive.files.list → sees params → 
       gws drive files list --params '...'
```

All 4 patterns documented in CONTEXT.md §Rules of Engagement.

## 9. Cross-references

- [[(C) README summary]] — overall framing
- [[(C) CONTEXT + CLAUDE + AGENTS cluster summary]] — tri-file agent docs + helper anti-patterns
- [[(C) Dynamic Discovery Service Architecture]] (Phase 3 entity) — foundation for skills
- [[(C) 110 Skills (44 gws-* + 10 personas + 56 recipes)]] (Phase 3 entity) — deep-dive

## Open questions surfaced

- Skill category ratios (44/10/56) — intentional or organic? (new — Q28)
- Persona bundles — implemented as composition or independent docs? (new — Q29)
- Recipe quality audit — who validates 56 recipes work at scale? (Q8)
- Helper command total inventory (beyond visible ~20)? (new — Q30)
- Skill growth rate target for v1.0? (new — Q31)
