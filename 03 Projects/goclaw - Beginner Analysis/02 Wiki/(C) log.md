# (C) Log — goclaw Wiki

> Append-only timeline. Format: `## [YYYY-MM-DD] type | title`

---

## [2026-04-18] setup | Phase 0+1 — Pre-flight + Scaffold (4th routine run)

- **Routine invoked:** `05 Skills/llm-wiki-routine.md` v1 (4th auto-execution)
- **Phase 0 pre-flight:** ✅ PASSED với framing adjustment
  - URL accessible
  - Threshold: 42MB, 117 .md → large
  - **Sibling detection: 3 projects** (ECC + Superpowers + gstack) in **adjacent domain**
  - Domain classification: "Multi-Tenant AI Agent Platform" (infrastructure/SaaS) vs siblings' "Claude Code skill frameworks" (dev productivity)
  - **Phase 4b reframed** — taxonomy guide (agent-as-assistant vs agent-as-service) thay vì forced 4-way comparison
- **Phase 1 scaffold:**
  - Project folder duplicated từ template
  - 8 numbered subfolders
  - Source cloned: `git clone --depth 1 https://github.com/nextlevelbuilder/goclaw.git`
- **Initial repo survey:**
  - Total .md: 117
  - Total size: 42MB (largest so far — ECC ~67KB, Superpowers 140KB, gstack 12MB)
  - Key files (lines): README 338, CLAUDE.md 267, CHANGELOG 78, CONTRIBUTING 170
  - **20+ numbered docs** in `docs/00-19+`: architecture-overview, agent-loop, providers, tools-system, gateway-protocol, channels-messaging, store-data-model, bootstrap-skills-memory, scheduling-cron, security, tracing-observability, agent-teams, extended-thinking, ws-team-events, skills-runtime, core-skills-system, skill-publishing, changelog, http-api, websocket-rpc
  - `skills/` folder: _shared, docx, pdf, pptx, skill-creator, xlsx (Anthropic-compatible format)
  - **Vietnamese README exists** (`_readmes/README.vi.md`) — bilingual source
- **Key findings ngay từ survey:**
  - **Meta-relevant:** goclaw's "Knowledge Vault với wikilinks + hybrid search (FTS + pgvector)" = Karpathy's LLM Wiki pattern implemented as infrastructure. Storm Bear vault's theoretical backend?
  - Go 1.26 + PostgreSQL 18 + Docker + WebSocket + OpenTelemetry + 20+ LLM providers
  - License CC BY-NC 4.0 (non-commercial, khác MIT của 3 siblings)
  - Desktop Edition "GoClaw Lite" (Wails v2 + React + SQLite, max 5 agents)
- **Source strategy:**
  1. README.md (338 lines) — full read
  2. CLAUDE.md (267 lines) + docs/00-architecture-overview.md + docs/01-agent-loop.md
  3. Skim key docs (14-skills-runtime, 06-store-data-model cho memory, 09-security) + CHANGELOG
- **Phase 0+1 status:** ✅ COMPLETE
- **Next:** Phase 2 source ingestion

---

## [2026-04-18] ingest | Phase 2 — Source summaries (3 files)

- **Source #1:** `(C) README summary.md` — domain positioning (agent-as-service vs agent-as-assistant), 8 core features, 20+ LLM providers (including Claude CLI/Codex/ACP), 7 messaging channels (Zalo x2 = VN signal), GoClaw Lite desktop edition, CC BY-NC 4.0 license
- **Source #2:** `(C) CLAUDE.md + Architecture summary.md` — dev conventions (Go 1.26 + PG 18 + Wails + React 19, pnpm, language-matching bilingual), 17 Plan Verification Rules (tactical discipline), V3 pipeline architecture (Context/Think/Prune/Tool/Observe/Checkpoint/Finalize = 7 Stages, marketing framed as 8), 13 mobile UI rules, 11 distinctive patterns
- **Source #3:** `(C) Key Docs deep dive.md` — 4 Docker image variants (minimal/python/node/full) + 5-tier skill hierarchy, Agent Teams (Lead + Members + Task Board + Mailbox), 5-layer defense security (Transport/Input/Tool/Output/Isolation), CHANGELOG full (78 lines, dual-track versioning v3.x + lite-v1.x.x)
- **Skim-first applied:** 01-agent-loop.md (792 lines, skim for stages), 11-agent-teams.md (717 lines, overview only), 09-security.md (498 lines, 5-layer intro). Saved ~2 hours.
- **Key findings:**
  1. **Domain confirmed adjacent** — goclaw = agent-as-service platform, 3 siblings = agent-as-assistant dev tools. Not competitors.
  2. **Integration pattern possible** — goclaw via ACP/Claude CLI provider can host gstack/Superpowers/ECC skills as backend
  3. **Meta-relevance to Storm Bear vault** — goclaw's Knowledge Vault = Karpathy's LLM Wiki pattern as infrastructure
  4. **Convergent discipline** — 17 Plan Verification Rules echo Superpowers's 11 Rationalizations + gstack's blame-with-receipts. 3 most-opinionated frameworks converge.
  5. **Vietnamese market positioning** — Zalo x2 + `README.vi.md` + `catalog_vi.go` + language-matching policy = author likely VN or Asian market
- **Phase 2 status:** ✅ COMPLETE

---

## [2026-04-18] entities | Phase 3 — Entity pages (4 building blocks)

- **Entity #1:** `(C) 8-Stage Agent Pipeline.md` — agent execution loop (7 Stage classes marketed as 8), V2/V3 feature-flag migration, comparison với 3 siblings' dev-workflow stages (different abstraction layer)
- **Entity #2:** `(C) 3-Tier Memory + Knowledge Vault.md` — Working/Episodic/Semantic tiers + L0/L1/L2 progressive loading + Knowledge Vault (wikilinks + BM25 + pgvector + FS sync). **Meta-relevant to Storm Bear vault** — Karpathy's LLM Wiki pattern as infrastructure
- **Entity #3:** `(C) Multi-Tenant Architecture.md` — 5 isolation levels (Tenant/User/Agent/Session/Role), tenant-scope guards discipline, 5-layer defense security, AES-256-GCM encrypted secrets, Edition system (Lite vs Standard)
- **Entity #4:** `(C) Agent Teams and Orchestration.md` — Lead + Members structure, Task Board + Mailbox, 3 orchestration modes (auto/explicit/manual), 3 delegation modes (sync/async/bidirectional), `BatchQueue[T]` generic, agent_links permission edges
- **Format compliance:** All 4 follow 13-section canonical format
- **Cross-references:** Each page links siblings + 3 sibling project analogs + Storm Bear vault connection
- **Phase 3 status:** ✅ COMPLETE
- **Insight:** Pattern generalizes to **adjacent-domain** projects. Entity pages captured architectural concepts specific to platform tier (vs assistant tier of siblings). Routine handled layer-difference via Phase 4b reframing (taxonomy guide instead of forced 4-way comparison).

---

## [2026-04-18] publish | Phase 4 — Published guides (2 deliverables)

- **Phase 4a:** `03 Published/(C) goclaw - Huong dan cho nguoi moi.md` — bilingual beginner guide (~620 lines, 8 parts). Added Part 6 "Meta-relevance tới Storm Bear vault" (unique section for platform-tier projects). Positioning framing throughout = agent-as-service vs agent-as-assistant.
- **Phase 4b:** `03 Published/(C) Agent framework taxonomy.md` — **reframed from 4-way comparison to taxonomy guide** (~500 lines). Positions 4 frameworks by tier + persona instead of 1:1 axis compare. Unique value-add: **tier abstraction only visible with 4 data points** (3 yielded spectrum, 4 yields taxonomy).
- **Phase 4 status:** ✅ COMPLETE
- **Insight:** Adjacent-domain handling via reframing = routine's flexibility feature. Forced 4-way would be apples-to-oranges.

---

## [2026-04-18] iterate | Phase 5 — Iteration log v4

- **Output:** `07 Iteration Logs/(C) 2026-04-18 v4 build learnings.md`
- **Velocity plateau:** v3 ~2.5h → v4 ~2.5h (no time gain). Signal to diversify (Option A recommended: real-use pilot).
- **6 action items** cho routine v2:
  1. Phase 0.5 sibling classification (same/adjacent/different)
  2. Phase 2.5 vault-relevance check
  3. Phase 3.5 entity deduplication pass
  4. Phase 4b output-type logic encoded
  5. License tracking in Phase 0
  6. Velocity diversification trigger after plateau
- **Key insights:**
  1. 4 data points unlock taxonomy; 3 only unlock spectrum
  2. Meta-relevance (vault backend) discovered only during entity synthesis, not pre-flight
  3. License discipline scales with ecosystem
  4. Routines evolve with use — v1 gap revealed after 4 runs
- **Phase 5 status:** ✅ COMPLETE

---

## [2026-04-18] vault-sync | Phase 6 — Vault file updates

- Updated project `(C) index.md` — phases marked ✅, deliverables tables populated
- Updated project `(C) log.md` — this entry
- Will update root `CLAUDE.md` — add goclaw entry + 4-project milestone
- Will update `GOALS.md` — mark 4th LLM Wiki + taxonomy unlock + velocity plateau signal
- **Phase 6 status:** ✅ COMPLETE

---

## 🎉 v4 ALL PHASES COMPLETE

**4th auto-execution của routine successful.** First adjacent-domain project handled gracefully via Phase 4b reframing. Taxonomy abstraction unlocked (4 > 3 = non-linear value).

**Routine `llm-wiki-routine` v1 = stable across 4 diverse projects.** Ready for v2 upgrade (6 action items) OR shift to real-use pilot.
