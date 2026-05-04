# (C) Log — deer-flow Wiki

---

## [2026-04-18] setup | Phase 0+1 — Pre-flight + Scaffold (9th routine run)

- **Routine:** `05 Skills/llm-wiki-routine.md` v1 (9th auto-execution — **third different-domain**, Tier 5 proposal)
- **Phase 0 pre-flight (API-probe-first):**
  - ✅ GitHub API HTTP 200
  - Size: 32 MB — moderate, WebFetch preferred (documentation-focused build)
  - **Stars: 62,505** — 2nd largest in corpus (behind build-your-own-x 491K; ahead of course 56K and notebooklm-py 11K)
  - **Forks: 8,079** — high engagement
  - License: MIT
  - Language: Python (primary) + TypeScript/Next.js (frontend)
  - Default branch: main
  - **Pushed: 2026-04-18 (TODAY)** — most active repo in corpus
  - Fork: false, Archived: false
  - **5 README languages** (fr/ja/ru/zh/en) — no Vietnamese (contribution opportunity)
  - Root contents: Makefile (8 KB), README (38 KB), Install.md, CONTRIBUTING.md (10 KB), config.example.yaml (36 KB), backend/ frontend/ docs/ skills/ docker/ scripts/ .agent/
  - **Sibling detection: 8 projects** — 4 T1 + 1 T2 + 1 T3 + 1 T4 + 1 outside-scope
  - **Domain classification: TIER 5 PROPOSAL** → "Agent-as-application" (standalone autonomous harness)
  - **Phase 4b routing = tier extension** (5th distinct tier extension after v4/v6/v7 — but extends further into SuperAgent category)

- **Phase 1 scaffold:**
  - Project folder created via `mkdir -p`
  - 8 subfolders created
  - Source acquisition: WebFetch (README + Install + CONTRIBUTING successfully retrieved)

- **WebFetch successful retrievals:**
  - README.md (38 KB) — full positioning + architecture + capabilities + comparisons + headline features
  - Install.md — Docker + local setup paths, make commands, configuration requirements
  - CONTRIBUTING.md (10 KB) — layered architecture (Nginx→Frontend/Gateway/LangGraph), code structure, development workflow, testing approach

- **Unique findings:**
  - **"SuperAgent harness" self-framing** — clear positioning, distinct from T1-T4
  - **Long-horizon autonomous** — "minutes to hours" tasks vs T1 interactive Claude Code sessions
  - **Full-stack app** — Frontend (Next.js 3000) + Gateway (Python 8001) + LangGraph Server (2024) + Nginx (2026)
  - **Parallel sub-agents** — fan-out pattern với isolated context per sub-agent
  - **Progressive skill loading** — context-window-conservation design
  - **Multi-channel IM integration** — 5 platforms (Telegram/Slack/Feishu/WeChat/WeCom) — unusual vs siblings
  - **Claude Code complementary** — explicit OAuth + `claude-to-deerflow` skill = interoperability architecture
  - **v2 rebuild** — no shared code với v1 = major architectural overhaul
  - **#1 GitHub Trending Feb 2026** — major launch milestone
  - **ByteDance backing** — sustainability stronger than solo maintainers (goclaw, notebooklm-py)
  - **LangGraph orchestration** — leverages popular agent framework (not reinventing)
  - **Devin/AutoGPT category** — this tier = autonomous agent apps, not Claude Code plug-ins
  - **Most active repo in corpus** — pushed TODAY

- **Source strategy:**
  1. README summary (38 KB — full positioning + architecture)
  2. Install + Setup summary (Docker + local flows)
  3. Architecture + Contributing cluster (layered design + dev workflow)

- **Phase 0+1 status:** ✅ COMPLETE
- **Next:** Phase 2 source summaries

---

## [2026-04-18] ingest | Phase 2 — Source summaries (3 files)

- **Source #1:** `(C) README summary.md` — SuperAgent harness positioning, 5-component architecture (Sandbox/Memory/Skills/Sub-agents/Gateway), layered deployment (Nginx 2026 / Frontend 3000 / Gateway 8001 / LangGraph 2024), capabilities (research/code/creation/image-video), model support (GPT/Gemini/Qwen/Doubao/DeepSeek/Kimi), comparisons (Devin/AutoGPT/CrewAI/Claude Code complementary), unique features (parallel sub-agents, progressive skill loading, persistent memory, multi-channel IM, batteries-included)
- **Source #2:** `(C) Install + Setup summary.md` — Docker-preferred + local fallback paths, make commands, prerequisites (node/pnpm/uv/nginx), config.yaml requirements (at least 1 model), port map, idempotent setup
- **Source #3:** `(C) Architecture + Contributing cluster summary.md` — layered architecture detail, code structure (backend/ frontend/ skills/), development workflow (format ruff+Prettier+ESLint, tests unit+E2E), adding skills/agents (docs reference backend config), engineering maturity signals
- **Key findings:**
  1. **"SuperAgent harness" self-framing** — clear Tier 5 positioning
  2. **Long-horizon autonomous** — minutes-hours vs Claude Code's interactive
  3. **Full-stack app** — 4 services, not skill/plug-in
  4. **Complementary với Claude Code** — OAuth both ways
  5. **ByteDance corporate-backed** — sustainability parallel to T3 Microsoft
  6. **LangGraph orchestration** — ecosystem dependency
  7. **5 IM platforms** — multi-channel gateway (missing Zalo = contribution opportunity)
  8. **Chinese LLM support strong** — Qwen/Doubao/DeepSeek/Kimi explicit
  9. **v2 rebuilt from scratch** — Feb 2026 launch, #1 GitHub Trending
  10. **Most complex deployment in corpus** — 4 services + Nginx + Docker
- **Phase 2 status:** ✅ COMPLETE

---

## [2026-04-18] entities | Phase 3 — Entity pages (4, 13-section)

- **Entity #1:** `(C) SuperAgent Harness Architecture.md` — 5 core components detailed, 4-port layered architecture diagram, Nginx routing rules, request flow example, comparison to sibling architectures (deer-flow = highest complexity), when NOT to use
- **Entity #2:** `(C) Skill System (Progressive Loading).md` — Markdown-based skill format, progressive loading mechanism, built-in skills list, custom skills workflow, comparison to sibling skill patterns (ECC 185 small / notebooklm-py 1 mega / deer-flow progressive public+custom)
- **Entity #3:** `(C) Sub-Agent System (Parallel Fan-out).md` — fan-out→execute→synthesize pattern, context isolation mechanics, use cases (research multi-angle / multi-format / data pipeline / debugging), comparison to sibling multi-agent implementations, Storm Bear potential parallel routine adoption
- **Entity #4:** `(C) Message Gateway (Multi-Channel).md` — 5 platforms (Telegram/Slack/Feishu/WeChat/WeCom), bot API architecture, use case examples, security implications, VN market gap (Zalo missing)
- **Format compliance:** 13-section canonical
- **Cross-references:** Each entity links 8 sibling wikis + internal entities
- **Phase 3 status:** ✅ COMPLETE

---

## [2026-04-18] publish | Phase 4 — Published guides (2 deliverables)

- **Phase 4a:** `03 Published/(C) deer-flow - Huong dan cho nguoi moi.md` — bilingual beginner guide (~650 lines, 10 parts). Parts: intro + positioning vs 8 siblings, 5-tier taxonomy, installation, first workflows, Skills deep dive, multi-channel gateway, sibling comparison matrix, Storm Bear use cases (Scrum retro synthesis pipeline, weekly briefing, client research, vault meta-use), 2-week roadmap, risks, next steps
- **Phase 4b:** `03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md` — **EXTENDS v7 4-tier → 5-tier** (~700 lines, 20-axis analysis, 8 personas). **Tier 5 "Agent-as-application" added.** 5 emergent patterns (Pattern 5 NEW: task-duration → form-factor correlation). T5 vs T2 distinction crystallized. Complete decision tree for Storm Bear users.
- **Phase 4 status:** ✅ COMPLETE
- **Insight:** v9 Phase 4b = 8th distinct routing mode (5-tier extension via T5). Routine handles comprehensive taxonomy evolution.

---

## [2026-04-18] iterate | Phase 5 — Iteration log v9

- **Output:** `07 Iteration Logs/(C) 2026-04-18 v9 build learnings.md`
- **Velocity plateau confirmed 4 consecutive wikis** — v6+v7+v8+v9 all ~2h
- **Key insights:**
  1. Routine handles 8 distinct Phase 4b routing modes
  2. 5-tier taxonomy covers AI agent ecosystem comprehensively
  3. Corporate backing correlates với infrastructure-heavy tiers (T3, T5)
  4. Deployment complexity → tier identifier
  5. Complementary positioning = maturity signal
  6. Task-duration → form-factor pattern (new)
  7. 32+ action items total → routine v2 CRITICAL
- **Recommendation:** Option A Storm Bear pilot với deer-flow + Option B routine v2 upgrade = combined best path
- **Phase 5 status:** ✅ COMPLETE

---

## [2026-04-18] vault-sync | Phase 6 — Vault file updates

- Updated project `(C) index.md` — all phases ✅
- Updated project `(C) log.md` — all phase entries appended
- Updated root `CLAUDE.md` — deer-flow project entry với Tier 5 framing + 9-wiki milestone
- Updated `GOALS.md` — mark v9 shipped, T5 tier established, 32+ action items urgency
- **Phase 6 status:** ✅ COMPLETE

---

## 🎉 v9 ALL PHASES COMPLETE

**9th auto-execution của routine successful.** Tier 5 "Agent-as-application" established. 5-tier taxonomy v4 documented. 8 distinct Phase 4b routing modes observed. 32+ action items accumulated.

**Routine v1 = production-stable across 9 runs covering 8 Phase 4b routing modes.** Next: routine v2 upgrade critical.
