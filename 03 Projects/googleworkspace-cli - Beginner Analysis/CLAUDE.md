# googleworkspace-cli - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`googleworkspace/cli`](https://github.com/googleworkspace/cli) — **`gws`** — **"One CLI for all of Google Workspace — built for humans and AI agents. Drive, Gmail, Calendar, and every Workspace API."** **25,000 stars, 1,300 forks, Apache-2.0, v0.22.5 pre-1.0 (active development)**. Rust 98.8%. 283 commits, 44 releases, 84 watchers, 71 open issues. Official Google project. **Dynamic Discovery Service architecture** — does NOT ship generated crates; builds `clap` CLI tree at runtime from Discovery JSON.

**Critical milestone:** **Tier 4 "Agent-as-bridge" multi-entrant VALIDATED at N=2** (parallel to T5 validation at v10). T4 now:
- **v7 notebooklm-py** (solo, unofficial, Python, 11K stars — single-service NotebookLM bridge)
- **v13 googleworkspace/cli** (Google corporate, official, Rust, 25K stars — **multi-service bridge, 11+ Workspace APIs**)

**Subcategorization hypothesis (new v13):** T4 splits along **official-corporate vs unofficial-solo** axis — same pattern as T5 split along **corporate-generalist vs solo-specialist** at v10.

**Phase 4b routing = T4 2-way comparison** (validates T4 multi-entrant — 4th tier validated; only T2/T3 remain single-entrant).

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine` v1 (**13th auto-execution — T4 validation + first Rust + first Apache-2.0 + official Google corporate**):

- **Ingest sources via WebFetch** — README + CLAUDE.md (1-liner pointing to AGENTS.md) + AGENTS.md (209 lines) + CONTEXT.md (agent runtime rules) + skills/ listing (110 skills)
- **Cross-reference với 12 sibling wikis** — T4 peer notebooklm-py is direct 2-way comparison target
- **Phase 4b = T4 2-way comparison** — same pattern as v10 autoresearch T5 2-way
- **Beginner roadmap** — VN operator angle: Google Workspace is universal in VN corporate env

**Prime directive:** Outcome = wiki + T4 2-way comparison (validates T4 multi-entrant) + document 3 new corpus firsts (Rust, Apache-2.0, official Google corporate).

## Process — routine `llm-wiki-routine` v1

7 phases. Continuous execution. Phase 4b = **T4 2-way comparison** (notebooklm-py vs googleworkspace/cli, same-tier pattern identical to v10).

## Key People / Organization

- **googleworkspace** — GitHub org (official Google)
- **Google Workspace Developer team** — maintainers (not individually named in README)
- **Community:** Not explicit (no Discord/Slack in README)
- **Cross-project:** 12 sibling wikis. This is 13th = T4 multi-entrant validation.

## Folder Structure

```
googleworkspace-cli - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00 Sources/            ← WebFetch-based
├── 01 Analysis/
├── 02 Wiki/
├── 03 Published/
├── 04-07/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ + 13-section format
- **Cross-reference 12 siblings MANDATORY** — especially v7 notebooklm-py (T4 peer for 2-way comparison)
- **Document firsts:** first Rust, first Apache-2.0, first official-Google-corporate in corpus
- **T4 subcategorization hypothesis** — document official-corporate vs unofficial-solo alongside T5's corporate-generalist vs solo-specialist

## Positioning note

**googleworkspace/cli trong taxonomy v4 (v13 update):**

| Tier | Frameworks (n=13 now) | v13 change |
|------|----------------------|------------|
| T1: Agent-as-assistant | ECC, Superpowers, gstack, GSD, BMAD, codymaster (6) | — |
| T2: Agent-as-service | goclaw (1) | — |
| T3: Agent-as-education | course (1) | — |
| **T4: Agent-as-bridge** | **notebooklm-py, googleworkspace/cli (2 ← VALIDATED)** | **✅ Multi-entrant validation** |
| T5: Agent-as-application | deer-flow, autoresearch (2) | — |
| Outside scope | build-your-own-x (1) | — |

→ **T4 N=2 — fourth tier to validate multi-entrant after T1 (v11) and T5 (v10).**

### T4 2-way preview

| Axis | notebooklm-py (v7) | googleworkspace/cli (v13) |
|------|--------------------|--------------------------|
| **Stars** | 11K | **25K (2.3× larger)** |
| **Service scope** | 1 service (NotebookLM) | **11+ services** (Drive/Gmail/Calendar/Sheets/Docs/Chat/Admin/Script/Workflow/Events/ModelArmor) |
| **Official status** | **Unofficial** (solo reverse-engineered) | **Official** (Google-shipped) |
| **Primary language** | Python | **Rust (first in corpus)** |
| **License** | MIT | **Apache-2.0 (first in corpus)** |
| **Author type** | Solo (teng-lin) | **Google corporate** |
| **Distribution channels** | npm single | **5 channels (binaries/npm/cargo/nix/brew)** |
| **Skill count** | Single mega-SKILL.md (~26KB) | **110 skills** (44 gws-* + 10 personas + 56 recipes) |
| **Architecture** | Reverse-engineered API wrapper | **Dynamic Discovery API — runtime command generation** |
| **Agent integration** | SKILL.md + CLI + Python API | **CLAUDE.md → AGENTS.md + CONTEXT.md + gemini-extension.json** |
| **Auth model** | Unofficial (session cookies?) | **Official OAuth2 + service account + AES-256-GCM keyring + Model Armor** |

## Unique positioning claims của googleworkspace/cli (từ Phase 0)

- **25,000 stars at v0.22.5 pre-1.0** — aggressive pre-release adoption (top 3 in corpus after build-your-own-x 491K, BMAD 45K)
- **Official Google project** — first official-corporate-backed framework in agent-tooling corpus
- **Rust 98.8%** — FIRST Rust project. Performance + distribution benefits.
- **Apache-2.0** — FIRST Apache-2.0 in corpus (vs MIT dominant)
- **11+ Workspace services** supported (Drive/Gmail/Calendar/Sheets/Docs/Chat/Admin/Script/Workflow/Events/ModelArmor)
- **Dynamic Discovery Service** architecture — no pre-generated crates, runtime `clap` tree generation
- **110 skills:** 44 gws-* service skills + 10 persona skills (team-lead/exec-assistant/etc) + 56 recipe skills (meeting-prep/backup-sheet/etc)
- **5 install channels** — binaries / npm / cargo / nix / brew (breadth rivals codymaster's 8+)
- **Helper commands prefixed `+`** — handwritten multi-step orchestration (e.g., `gws gmail +triage`, `gws workflow +standup-report`)
- **Schema introspection** — `gws schema <method>` built-in (unique feature)
- **Model Armor integration** — Google's response sanitization layer (unique security primitive)
- **Multi-flow OAuth2** — interactive local (AES-256-GCM + OS keyring) / headless / service account / pre-obtained token
- **CONTEXT.md as agent-user runtime guide** — distinct from CLAUDE.md (contributor) and AGENTS.md (contributor). First tri-file agent documentation in corpus.
- **Input validation discipline** — `validate_safe_output_dir`, `validate_safe_dir_path`, `validate_resource_name`, `encode_path_segment`. CLI args = adversarial.
- **Changeset-driven release discipline** — every PR requires `.changeset/<name>.md` with patch/minor/major
- **Two-crate workspace** — library (discovery/validation/client) vs binary (auth/commands/execution)
- **NDJSON streaming for pagination** — `--page-all` flag

## Current Status

> **Last updated:** 2026-04-19
> **Status:** 🟡 Routine auto-execute IN PROGRESS — 13th LLM Wiki, T4 multi-entrant validation

### Expected milestones

- [x] Phase 0 Pre-flight (API probe, 25K stars, T4 validation, 3 corpus firsts)
- [ ] Phase 1 Setup
- [ ] Phase 2 Source ingestion — 3 summaries (README / CONTEXT+CLAUDE+AGENTS cluster / Skills 110 + Helper Commands cluster)
- [ ] Phase 3 Entity pages (4 — Dynamic Discovery Architecture / 110 Skills + Personas + Recipes / Multi-Flow Auth + Model Armor / T4 Multi-entrant Validation + Official-vs-Unofficial Storm Bear meta-entity)
- [ ] Phase 4a Beginner published guide bilingual
- [ ] Phase 4b **T4 2-way comparison** (validates multi-entrant; notebooklm-py vs gws)
- [ ] Phase 5 Iteration log v13
- [ ] Phase 6 Vault file updates
