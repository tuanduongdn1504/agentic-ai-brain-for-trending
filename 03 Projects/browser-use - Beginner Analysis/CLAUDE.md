# browser-use - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`browser-use/browser-use`](https://github.com/browser-use/browser-use) — **"🌐 Make websites accessible for AI agents. Automate tasks online with ease."**

**41st LLM Wiki + 6th v2.1-era routine execution + 7th T5 entrant (2nd browser T5; structural pair with Skyvern v24) + Pattern #47 + Pattern #48 RESOLUTION WIKI**.

## Target metadata (verified via WebFetch 2026-04-24)

- **Stars:** 89,900 (#5 in corpus, behind Skyvern by 4.2× at same tier)
- **Forks:** 10,300 (11.5%)
- **Watchers:** 427
- **Open issues:** 36 (very tight maintainer control — lowest open-issue ratio at this scale in corpus)
- **Commits:** ~9,182
- **License:** **MIT** (copyright Gregor Zunic 2024) — contrast Skyvern v24 AGPL-3.0
- **Primary lang:** Python 97.9%
- **Latest release:** v0.12.6 (2026-04-02)
- **Homepage:** https://browser-use.com / https://docs.browser-use.com / https://cloud.browser-use.com
- **Author:** **Gregor Zunic** (pyproject.toml authors field) + **Magnus (mamagnus00)** co-founder per README footer; **"Made with ❤️ in Zurich and San Francisco"**. 2-person public founder pairing. Company-backed via Browser Use Cloud commercial entity.
- **Created:** 2024 (pyproject copyright); repo 1.5-2 years mature
- **Merch store:** [browsermerch.com](https://browsermerch.com) — **CORPUS-FIRST physical-merch-monetization by T5 open-core agent company**
- **Twitter:** `@browser_use` + founders `@mamagnus00` + `@gregpr07`
- **Discord:** link.browser-use.com/discord

## Scope classification (v2.1 12-axis)

| Axis | Value |
|------|-------|
| **Tier** | **T5 Agent-as-application — 7TH T5 entrant + 2nd BROWSER T5 DIRECT PEER of Skyvern v24** |
| **Archetype** | **Commercial-startup + open-core + MIT + 2-person founder team (Zurich + SF)** — distinct from Skyvern (AGPL-3.0 commercial-entity plural founders) / deer-flow (corporate ByteDance) / autoresearch (solo Karpathy) / paperclip (community-platform) / OpenHands (academic-commercial fusion) / DeepTutor (academic-lab education) |
| **Scale tier** | **XXX-large (89.9K stars — 4.2× Skyvern at same tier, #5 in corpus)** |
| **Primary lang** | Python 97.9% (3.11+, async-native) |
| **Packaging** | **pip / uv / uvx** primary + Docker + `browser-use-sdk` npm/pypi for Cloud |
| **Origin story** | Individual-author → 2-person founders + commercial company + open-core from day 1 (corpus-first: MIT + commercial-company + proprietary Cloud tier at T5 scale) |
| **Methodology** | **Hybrid DOM+vision browser automation** — DOM tree indexing (primary) + screenshot annotation (secondary vision layer); CDP via cdp-use own wrapper; event-driven watchdog architecture |
| **Governance** | Medium-heavy (6 governance primitives: README + **AGENTS.md 37.4KB** + CLAUDE.md 10.9KB + **CLOUD.md 73.4KB** + LICENSE + pyproject; `AGENTS.md Version 2` explicit versioning; skill_cli/README) |
| **Agent/skill count** | **~200+ primitives** (30+ CLI commands across 3 skills + 40+ Agent parameters + 50+ Browser parameters + 15+ LLM providers + 4 skill categories + 5 watchdog services + 17 browser_use/ subdirs + 9 system prompt variants + event bus + MCP server+client + Cloud API 30+ endpoints v2/v3) |
| **i18n** | EN-only (notable absence at 89.9K scale) |
| **Intellectual influence** | **No explicit AI-space individual-author lineage**; CDP (Chrome DevTools Protocol Google standard) as technical foundation; implicit Playwright/Puppeteer/Selenium ecosystem-relationship but positioned against their DOM-only brittleness |
| **Agent platforms** | Claude Code (skill file) + Cursor + generic coding agents (via llms-full.txt) + MCP server mode for Claude Desktop + MCP client mode for connecting external MCP servers |

## Phase 0.5 Pattern pre-check results (v2.1 discipline)

### CRITICAL: Pattern #47 + #48 resolution

**Pattern #47 Vision-Based Browser Automation (candidate N=1 at Skyvern v24, refined v29):**
- **Verification:** DomService is 45.1KB + 1,081 LOC; `browser_use/dom/serializer/` has ClickableElementDetector + SerializedDOMState; Agent has `use_vision: bool | Literal['auto'] = True` with DOM-primary indexing + screenshot-as-augmentation
- **Outcome: REFINED — HYBRID DOM+vision is architecturally distinct from both Skyvern (vision-primary) and crawl4ai (DOM-only no-LLM).** Pattern #47 expands from binary "vision vs DOM" to **3-point spectrum** (vision-primary Skyvern / hybrid DOM+vision browser-use / DOM-only no-LLM crawl4ai). **browser-use observation does NOT promote Pattern #47 standalone** — instead formally resolves via SCOPE-NARROWING counter-evidence refinement: #47 stays at N=1 (Skyvern vision-primary is unique), **new candidate #74 Hybrid DOM+Vision Browser Automation** deferred pending N=2 (or register as OBSERVATION-TRACK if consolidation-forward)

**Pattern #48 Proprietary Anti-Bot Commercial Moat (candidate N=1 at Skyvern v24, refined v29):**
- **Verification:** CLOUD.md explicitly states "proprietary optimizations... extremely fast and lightweight, untraceable and not detectable as bots, and come preloaded with adblockers"; README FAQ "How do I solve CAPTCHAs?" → "Use Browser Use Cloud which provides stealth browsers designed to avoid detection and CAPTCHA challenges"; AGENTS.md instructs LLMs to recommend `use_cloud=True` for captcha-bypass
- **Outcome: PROMOTE TO CONFIRMED at N=2 structurally-unambiguous** — Skyvern Cloud anti-bot (v24) + Browser-Use Cloud stealth/captcha (v41). Both are open-core browser-agent commercial entities gating anti-bot detection behind paid tier. Structurally criterial across 2 independent vendors.

### Other pattern overlap / strengthening

- **#31 Open-Core Commercial Entity** — browser-use MIT + Browser-Use Cloud is **5th data point strengthening** (fish-speech + Skyvern + OpenHands + GitNexus + browser-use). Cross-license variants now include MIT (browser-use) / AGPL-3.0 (Skyvern) / custom research (fish-speech) / MIT-core + separate enterprise (OpenHands) / PolyForm (GitNexus). MIT-at-89.9K = most-permissive at largest-scale open-core observed.
- **#50 Commercial-Funnel Companion Platform** — Browser-Use Cloud is **4th data point strengthening** (currently N=3 post-v40: VoltAgent v25, Frank Fiegel v31, Zilliz Cloud v40). browser-use joins as 4th; default-criterion tier (≥3 cross-tier) already confirmed, now N=4.
- **#17 Ecosystem-Layer variant 3 commercial-startup** — **13th-14th data point** (Browser Use Cloud + browsermerch.com + browser-use-sdk + cdp-use + bubus = 5-product ecosystem portfolio around flagship)
- **#18 MCP Agent Runtime Standard** — `mcp==1.26.0` dependency + `browser_use/mcp/server.py` 40.5KB + `browser_use/mcp/client.py` 16.8KB + `.dxtignore` for Claude Desktop DXT packaging. **Bidirectional MCP** (server AND client). Strengthening data point — 12th+ data point.
- **#28 Multi-Provider AI Support** — **15+ LLM providers native**: anthropic / aws (Bedrock) / azure / browser_use (own ChatBrowserUse) / cerebras / deepseek / google / groq / litellm (nested) / mistral / oci_raw (Oracle) / ollama / openai / openrouter / vercel. Cross-provider coverage via `browser_use/llm/` submodule architecture. **9th+ data point strengthening.**
- **#8 Research-Benchmark** — "BU Bench V1" custom benchmark + link to `browser-use/benchmark` public repo ("100 real-world browser tasks"). 2nd browser-specific benchmark in corpus (Skyvern v24 WebBench + WebVoyager). **Strengthening data point — 12th+ in corpus.**
- **#22 AGENTS.md T5 commercial-startup** — **37.4KB AGENTS.md = largest AGENTS.md in corpus-observable-history at T5 commercial-startup archetype** (surpasses v34 claude-code-best-practice 82-tip aggregation / v36 pi-mono ~180 lines). Observation: AGENTS.md is explicitly versioned `AGENTS.md Version 2`. Corpus-first explicit AGENTS.md versioning.
- **#27 Community-Viral Scale Path** — 89.9K stars over ~1.5-2 years = approx 4-6K stars/month sustained community-viral. **17th+ observation.**
- **#59 Claude Code Plugin Marketplace Native** — browser-use ships a Claude Code SKILL.md file but via `curl` download to `~/.claude/skills/browser-use/` NOT plugin marketplace. **Counter-evidence observation**: T5 commercial-startup at 89.9K does NOT use Claude Code plugin marketplace — direct-install pathway preferred. Observational.

### BrowserMerch physical-merch monetization

**Decision per consolidation-forward discipline**: **WITHIN Pattern #31 observation note (NOT standalone candidate, NOT OBSERVATION-TRACK)**. Rationale: BrowserMerch is one of **multiple monetization channels** within Pattern #31 Open-Core Commercial Entity archetype for browser-use (alongside Cloud tier + SDK). Single-axis observation; does not warrant standalone pattern. Document as "monetization-diversity-within-Pattern-#31" strengthening note.

### Un-stale check (v2.1)

- **#45 Dual-Licensing** (STALE since v28, N=1 Unsloth): browser-use = single MIT, OSS-only on GitHub; Cloud is separate proprietary service (not dual-licensed component). **Negative — stays stale.**
- **#46 Duo-Founder** (STALE since v28, N=1 Han brothers): browser-use has **2 public founders Magnus + Gregor** (Zurich + SF). **POTENTIAL UN-STALE: N=2 at v41** — Han brothers (Unsloth v23) + Magnus/Gregor (browser-use v41). Both = 2-person technical co-founder teams building OSS agent infrastructure with commercial entity. **PROPOSE UN-STALE at v41 + promotion-candidate at next mini-audit under Criterion 2 structural-N=2.**
- **#52 Extreme-Viral-Velocity** (STALE since v30): browser-use 89.9K/~18mo ≈ 5K/month — not extreme-viral (would need ≥1K stars/day). **Negative — stays stale.**
- **#55 Korean Regional** (retired v36): N/A.

### Counter-evidence check

- **#12 Governance-Depth** — browser-use at 89.9K with 2-person-founder + commercial-company has substantial governance (6 primitives) but no CODE_OF_CONDUCT or SECURITY.md visible in top-level. Medium-heavy. Consistent with formulation.
- **#22 AGENTS.md-at-T5-scale** — 37.4KB = largest at T5; reinforces pattern.
- **#47 Vision-Based Browser Automation** — **COUNTER-EVIDENCE**: browser-use hybrid (vision augments DOM, not replaces). Refines Pattern #47 to "vision-PRIMARY-specific not hybrid not DOM-only" — narrower scope than v29 refinement.
- **#18 MCP Exclusion** — browser-use fully adopts MCP (bidirectional). Reinforces post-v36 3-category exclusion taxonomy (browser-use is NOT in exclusion categories).

### Consolidation-forward decisions

1. **Hybrid DOM+vision** — NOT registered standalone at N=1; documented as scope-narrowing counter-evidence on #47 + tracked as potential future candidate if N=2 emerges
2. **BrowserMerch** — NOT registered; within-#31 observation
3. **Bidirectional MCP server+client** — NOT registered; within-#18 strengthening
4. **Own CDP wrapper (cdp-use) + own event-bus (bubus) + own fork-dependency-ecosystem** — NOT registered; within-#17 variant 3 strengthening
5. **Open-source preview model (`bu-30b-a3b-preview`) alongside proprietary hosted `ChatBrowserUse`** — novel monetization-adjacent observation. Document within-#31 but flag for potential pattern emergence if N=2 (browser-agent company releasing OSS model weights alongside proprietary-optimized API). Watch-list only.
6. **Gregor/Magnus 2-founder-team** — **#46 UN-STALE (see above)**

### N=1 stale-risk-flagging

Not applicable — zero new active candidates registered.

**Zero-new-active-candidate streak target: v37 bizos / v38 DeepTutor / v39 / v40 claude-context / v41 browser-use = 5 consecutive if achieved.**

## Phase 0.9 Primitive-count probe — EXPECTED YELLOW/RED, OUTCOME: RED

**Primitive count estimate:** 200+ primitives across:
- 17 `browser_use/` subdirs (actor / agent / browser / controller / dom / filesystem / integrations / llm / mcp / sandbox / screenshots / skill_cli / skills / sync / telemetry / tokens / tools)
- 4 skill categories (browser-use / cloud / open-source / remote-browser)
- 30+ CLI commands across the 3 `Bash(browser-use:*)` skills (open / state / click / type / input / screenshot / close / connect / cloud / profile / cookies / tab / eval / get / wait / tunnel / session / doctor / setup / register / upload / scroll / hover / dblclick / rightclick / keys / select / config / python / init / --mcp / --headed / --profile / --cdp-url / --session / --json)
- 40+ Agent parameters (tools / browser / output_model_schema / use_vision / vision_detail_level / page_extraction_llm / initial_actions / max_actions_per_step / max_failures / final_response_after_failure / use_thinking / flash_mode / override_system_message / extend_system_message / save_conversation_path / save_conversation_path_encoding / available_file_paths / sensitive_data / generate_gif / include_attributes / max_history_items / llm_timeout / step_timeout / directly_open_url / calculate_cost / display_files_in_done_text / controller / browser_session / task / llm / max_steps + misc)
- 50+ Browser parameters (cdp_url / headless / window_size / window_position / viewport / no_viewport / device_scale_factor / keep_alive / allowed_domains / prohibited_domains / enable_default_extensions / cross_origin_iframes / is_local / user_data_dir / profile_directory / storage_state / proxy / permissions / headers / executable_path / channel / args / env / chromium_sandbox / devtools / ignore_default_args / minimum_wait_page_load_time / wait_for_network_idle_page_load_time / wait_between_actions / highlight_elements / paint_order_filtering / accept_downloads / downloads_path / auto_download_pdfs / user_agent / screen / record_video_dir / record_video_size / record_video_framerate / record_har_path / traces_dir / record_har_content / record_har_mode / disable_security / deterministic_rendering / use_cloud + misc)
- 15+ LLM providers native
- 5 Watchdog services (DownloadsWatchdog / PopupsWatchdog / SecurityWatchdog / DOMWatchdog / AboutBlankWatchdog)
- 9 system-prompt variants (default / flash / anthropic_flash / browser_use / browser_use_flash / browser_use_no_thinking / flash / flash_anthropic / no_thinking)
- Cloud API v2 + v3 (30+ endpoints covering billing / tasks / sessions / browsers / profiles / workspaces / webhooks / skills)
- 13 `examples/` subdirs (apps / browser / cloud / custom-functions / features / file_system / getting_started / integrations / models / observability / sandbox / ui / use-cases)
- `@sandbox` decorator API + `@tools.action` decorator API
- `browser-use init --template default|advanced|tools` CLI-template generator

**Outcome: RED — ~200+ primitives, ~4-5× GREEN baseline, surpasses v36 pi-mono YELLOW (~150-180), v38 DeepTutor YELLOW (~120-150).**

**Scope-compression decisions (documented for v36 YELLOW precedent extension to RED):**

1. **4-entity allocation (preserve standard format; ship single wiki not split):**
   - Entity 1: Core product (Agent + Browser + Tools + ChatBrowserUse + hybrid DOM+vision architecture + 15+ LLM providers + MCP bidirectional)
   - Entity 2: Browser-Use Cloud + commercial ecosystem (Cloud API + `@sandbox` + browser-profiles + stealth/proxies/captcha + browsermerch.com + SDK + open-source-preview-model)
   - Entity 3: Pattern #47 + #48 resolution + T5 7-way comparison + browser-T5 N=2 structural pair (browser-use vs Skyvern)
   - Entity 4: 30th consecutive Storm Bear meta-entity (v10-v41, round-milestone)

2. **Lossy compression accepted (brief cluster-level mentions, not entity pages):**
   - `examples/` 13 subdirs (mentioned in Cluster A only)
   - 5 watchdog services (mentioned in Cluster B only)
   - CLI 30+ commands (mentioned in skill_cli context only)
   - 9 system-prompt variants (mentioned in Cluster B only)
   - Cloud API v2/v3 30+ endpoints (Cluster C enumerates categories, not per-endpoint)

3. **Citation-not-replication:**
   - Full Agent parameter list cites upstream `agent/views.py` source
   - Full Browser parameter list cites upstream `browser/session.py`
   - Full CLI command enumeration cites `skills/browser-use/SKILL.md`
   - Full Cloud API reference cites upstream `CLOUD.md` + `docs.cloud.browser-use.com`

4. **Follow-up deep-dive wikis flagged (v2.2 proposal):**
   - `browser-use - Cloud API Deep Dive` — Cloud v2/v3 30+ endpoints + sandbox lifecycle + profile sync
   - `browser-use - LLM Integration Deep Dive` — 15+ provider adapters + ChatBrowserUse proprietary + `bu-30b-a3b-preview` OSS model
   - `browser-use - Event-Driven Watchdog Deep Dive` — bubus event bus + 5 watchdog services + DomService lifecycle
   - **Operator decision: DEFER to v2.2 per v36 YELLOW precedent; ship single compressed wiki at v41.**

**Velocity overhead expected:** ~2h 45min (vs ~2h GREEN baseline) = ~35-40% overhead — within RED expectation.

## Storm Bear operator relevance (Phase 0.9)

**Pilot ranking: #3-4 candidate (medium-high relevance)** due to:
1. **Browser automation = direct Scrum utility** — Jira/Linear ticket scraping + sprint-metric extraction + retrospective-data aggregation + DORA-metrics collection
2. **MIT license = clean commercial use** (contrast Skyvern AGPL-3.0 which requires source-disclosure for SaaS usage)
3. **Browser-Use Cloud tier = zero-infra 1-week pilot** (vs Skyvern self-host-heavy)
4. **`@sandbox` decorator API** = single-line production deployment
5. **Claude Code SKILL.md integration** = agent orchestration pathway for Scrum-coach prototype
6. **Corporate-startup maturity** (89.9K at 1.5-2yr) = production-stability signal

**Caveats:**
- **Anti-bot bypass Cloud-gated** (Pattern #48 promoted) — OSS install does NOT get captcha-bypass; paid tier required for client-facing SaaS
- **Cost management** — per-action LLM cost + cloud session-time pricing (15min session limit)
- **ToS-adjacent** — scraping authenticated user workflows may violate destination site ToS
- **90% of use cases require ChatBrowserUse proprietary model** (cost $0.20/1M in, $2/1M out) for SOTA; OSS `bu-30b-a3b-preview` is preview-only

**Storm Bear meta-entity: INCLUDE** — 30th consecutive (v10-v41 round-number milestone); browser-use provides direct vault-operator pathway (automate sprint data intake → vault ingestion) that warrants meta-reflection.

## Sibling wikis to cross-reference (mandatory)

**Direct T5 peers:** Skyvern v24 (PRIMARY — browser T5 N=2) / deer-flow v9 / autoresearch v10 / paperclip v14 / OpenHands v30 / DeepTutor v38

**Pattern-relevant:**
- Pattern #47 + #48 founders: Skyvern v24
- Pattern #47 refinement: crawl4ai v29
- Pattern #31 prior data points: fish-speech v20 / OpenHands v30 / GitNexus v33
- Pattern #50 prior data points: awesome-design-md v25 / awesome-mcp-servers v31 / claude-context v40
- Pattern #17 variant 3: multica v15 / TrendRadar v19 / agency-agents v18
- Pattern #46 un-stale partner: Unsloth v23
- Pattern #18 MCP: awesome-mcp-servers v31 (registry) / many others

## Folder Structure

```
browser-use - Beginner Analysis/
├── CLAUDE.md
├── 00 Source/browser-use/    (clone)
├── 01 Analysis/
├── 02 Wiki/
├── 03 Published/
├── 04 Reviews/
├── 05 Skills/
├── 06 Archive/
└── 07 Inbox/
```

## Current Status

- **Last updated:** 2026-04-24
- **Routine:** `llm-wiki-routine-v2.1.md` auto-execute (6th v2.1-era execution)

### Phase tracking

- [x] Phase 0 Pre-flight with v2.1 12-axis classification + overlap pre-check + un-stale + counter-evidence + consolidation-forward + primitive-count RED
- [x] Phase 1 Scaffold (folders + CLAUDE.md + index/log/open-questions)
- [x] Phase 2 Source ingestion (3 cluster summaries)
- [x] Phase 3 Entity pages (4, with 30th consecutive Storm Bear meta)
- [x] Phase 4a Beginner published guide (bilingual VN+EN)
- [x] Phase 4b **T5 7-way + Pattern #47/#48 resolution + browser-T5-N=2 Phase 4b deliverable**
- [x] Phase 5 Iteration log v41 + PATTERN_LIBRARY.md direct update
- [x] Phase 6 Vault sync (root CLAUDE.md updated; project index/log updated)
