# (C) Index — googleworkspace/cli Wiki

## 🎯 Project status (2026-04-19)

- ✅ Phase 0: Pre-flight — PASSED (API probe, 25K stars, T4 multi-entrant validation, 3 corpus firsts)
- ✅ Phase 1: Setup — COMPLETE
- ✅ Phase 2: Source ingestion — 3 summaries shipped
- ✅ Phase 3: Entity pages — 4 shipped
- ✅ Phase 4a: Beginner published guide — shipped (~600 lines bilingual)
- ✅ Phase 4b: **T4 2-way comparison** — shipped (15 axes, 4 new patterns, T4a/T4b subcategorization formalized)
- ✅ Phase 5: Iteration log v13 — shipped (8 new routine v2 action items)
- ✅ Phase 6: Vault file updates — COMPLETE

**Repo:** googleworkspace/cli
- **Binary name:** `gws`
- **Description:** "One CLI for all of Google Workspace — built for humans and AI agents. Drive, Gmail, Calendar, and every Workspace API."
- **Stats:** 25,000 stars, 1,300 forks, Apache-2.0, v0.22.5 pre-1.0, 283 commits, 44 releases, 84 watchers, 71 open issues
- **Language:** Rust 98.8% (FIRST Rust in corpus)
- **License:** Apache-2.0 (FIRST Apache-2.0 in corpus)
- **Author:** Google (official)
- **Homepage:** developers.google.com/workspace
- **Routine:** `05 Skills/llm-wiki-routine.md` v1 — 13th auto-execution, T4 validation
- **Domain:** **Tier 4 "Agent-as-bridge" entrant #2** (validates T4 multi-entrant)
- **Unique:** First Rust + first Apache-2.0 + first official-Google-corporate in corpus; tri-file agent documentation (CLAUDE.md/AGENTS.md/CONTEXT.md)

## Sources (planned)

| Page | Summary | Status |
|------|---------|--------|
| [[(C) README summary]] | Tagline, 11+ services, 5 install channels, auth model, helper commands, 110 skills, Model Armor, architecture | ⏸ |
| [[(C) CONTEXT + CLAUDE + AGENTS cluster summary]] | Tri-file agent documentation pattern; CONTEXT.md runtime rules; AGENTS.md contributor guidelines (209 lines) | ⏸ |
| [[(C) 110 Skills + Helper Commands cluster summary]] | 44 gws-* service skills + 10 persona skills + 56 recipe skills + `+verb` helper commands | ⏸ |

## Concepts (planned)

- **Dynamic Discovery Service** — runtime `clap` CLI tree from Google Discovery JSON; no generated crates
- **Two-crate workspace** — google-workspace library / google-workspace-cli binary
- **Helper commands `+verb`** — handwritten multi-step orchestration (vs auto-generated Discovery methods)
- **Schema introspection** — `gws schema <method>` built-in
- **Multi-flow OAuth2** — interactive / headless / service account / pre-token
- **AES-256-GCM keyring** — encrypted credentials + OS keyring
- **Model Armor** — Google's response sanitization for agent safety
- **Input validation discipline** — validate_safe_output_dir / validate_safe_dir_path / validate_resource_name / encode_path_segment
- **Changeset-driven releases** — every PR has `.changeset/<name>.md`
- **NDJSON streaming pagination** — `--page-all`
- **Agent-user runtime rules** (CONTEXT.md) — Schema Discovery + Context Window Protection + Dry-Run Safety
- **Tri-file agent documentation** — CLAUDE.md (pointer) / AGENTS.md (contributor) / CONTEXT.md (runtime-user)
- **Persona skills** — 10 role-based skill bundles (team-lead, exec-assistant, etc)
- **Recipe skills** — 56 workflow recipes (backup-sheet-as-csv, batch-invite-to-event, etc)

## Entities (planned)

| Page | Type | Sources | Status |
|------|------|---------|--------|
| [[(C) Dynamic Discovery Service Architecture]] | Novel architecture | README §Architecture + AGENTS.md | ⏸ |
| [[(C) 110 Skills (44 gws-* + 10 personas + 56 recipes)]] | Building block | skills/ listing + README | ⏸ |
| [[(C) Multi-Flow OAuth2 + Model Armor + Validation Discipline]] | Security model | README §Authentication + AGENTS.md Input Validation | ⏸ |
| [[(C) T4 Multi-Entrant Validation + Official-vs-Unofficial + Storm Bear Enterprise Angle]] | **T4 meta-entity + Storm Bear** | 2-way comparison + VN enterprise context | ⏸ |

## Roadmaps / Published

- ⏸ [[../03 Published/(C) googleworkspace-cli - Huong dan cho nguoi moi]] — beginner guide bilingual
- ⏸ [[../03 Published/(C) Tier 4 2-way comparison]] — validates T4 multi-entrant (notebooklm-py vs gws); documents official-corporate vs unofficial-solo T4 subcategorization hypothesis

## Cross-project siblings (12 total)

- **T4 direct peer (1) — 2-way comparison target:**
  - `../../notebooklm-py - Beginner Analysis/02 Wiki/(C) index.md`
- T1: ECC, Superpowers, gstack, GSD, BMAD, codymaster (6)
- T2: goclaw (1)
- T3: course (1)
- T5: deer-flow + autoresearch (2)
- Outside: build-your-own-x (1)

## Logs

- [[(C) log]]
