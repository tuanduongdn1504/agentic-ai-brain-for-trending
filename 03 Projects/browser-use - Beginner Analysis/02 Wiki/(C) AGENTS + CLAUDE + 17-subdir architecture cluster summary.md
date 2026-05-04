# (C) Cluster B — AGENTS.md + CLAUDE.md + 17-subdir architecture

> **Type:** Cluster summary (contributor-facing + architecture)
> **Sources:** AGENTS.md (37.4KB, "Version 2"), CLAUDE.md (10.9KB), 17 `browser_use/` subdirs, 9 system_prompt markdown variants, 5 watchdog services, `examples/` 13 subdirs, `tests/` layout, pyproject.toml dev dependencies
> **Parent:** [[(C) index]]

## 1. AGENTS.md Version 2 — corpus-largest at T5 commercial-startup

**Size: 37,400 bytes** — likely corpus-largest AGENTS.md. Prior records:
- claude-code-best-practice v34: 82-tip aggregation (size not directly comparable; was tips-in-README format)
- pi-mono v36: 182 lines (explicit line count, smaller surface)
- spec-kit v17: 6-file corporate governance set (AGENTS distributed across files)

**Corpus-first explicit versioning:** `# AGENTS.md Version 2` — first corpus AGENTS.md with semantic-version-style header. Signals that browser-use treats AGENTS.md as a versioned specification, not just a living doc.

**Structure (compressed):**
```
AGENTS.md Version 2
├── <guidelines> — development rules (pip→uv, no model-rename, pydantic v2, pre-commit, descriptive names, ActionResult, no random examples, default ChatBrowserUse, recommend use_cloud)
└── <browser_use_docs> — embedded comprehensive docs of ALL public APIs (Quickstart / Production / Agent Basics / Agent All Parameters / Agent Output Format / Prompting Guide / Supported Models / Browser Basics / Browser All Parameters / Real Browser / Remote Browser / Tools / Sensitive Data / MCP / Observability / etc.)
```

**Design decision:** AGENTS.md is not just rules — it contains the **complete documentation** (compressed from docs.browser-use.com) inline. Rationale: LLMs reading AGENTS.md get full library context in one file rather than needing to crawl docs site.

**Pattern #22 strengthening at T5 commercial-startup scale** — 37KB is substantial investment; reflects commercial-startup treating LLM-as-primary-developer-audience as strategic.

## 2. CLAUDE.md — thin but opinionated pointer

10.9KB, ~163 lines. Covers:
- High-level architecture (Agent / BrowserSession / Tools / DomService / LLM)
- Event-driven watchdog list (5 services)
- CDP integration explanation
- Development commands (uv venv, pytest, pyright, ruff, pre-commit)
- Code style (async, **tabs not spaces** for Python, modern `str | None` typing, pydantic v2 with `ConfigDict(extra='forbid')`, runtime assertions, `uuid7str` for IDs)
- Test discipline (never mock except LLM, use pytest-httpserver, never real remote URLs, pytest-asyncio modern style)
- **Personality** section (!) — CLAUDE.md literally sets tone: *"Don't worry about formalities. Don't shy away from complexity. Dry wit welcome. Be critical of your information. Take however smart you're acting and write as if +2sd smarter."*
- Strategy for making changes (test-first, failing-test pattern, event-bus for refactors)
- File organization patterns (service.py + views.py + events.py per component)
- MCP integration explanation
- **"important-instruction-reminders"** at bottom (Anthropic-standard block)

**Corpus-first T5 personality-setting-in-CLAUDE.md** — browser-use's CLAUDE.md directly manipulates LLM writing style ("as if +2sd smarter", "dismissively like 'be real' or 'that's crazy man' or 'lol no' if irritating"). Distinct from pattern-#25 Personality-Driven Agent Design (retired v27) which was about agents having personalities; this is about setting LLM-contributor personality. Watch-list observational.

## 3. 17-subdir `browser_use/` architecture

```
browser_use/
├── actor/           # Page/Element/Mouse legacy API (Playwright-like)
├── agent/           # Main Agent orchestrator (service.py 158.5KB = largest LOC)
│   ├── message_manager/
│   └── system_prompts/  # 9 markdown prompt variants
├── browser/         # BrowserSession / profile / watchdogs / cloud
│   ├── cloud/
│   └── watchdogs/
├── controller/      # Backward-compat alias for tools
├── dom/             # DomService (45.1KB) + serializer + markdown_extractor + enhanced_snapshot
│   ├── playground/
│   └── serializer/
├── filesystem/      # File-access primitives
├── integrations/    # Integration adapters
├── llm/             # 15 LLM provider adapters (anthropic/aws/azure/browser_use/cerebras/...)
├── mcp/             # MCP server.py (40.5KB) + client.py (16.8KB) + manifest.json DXT
├── sandbox/         # @sandbox decorator implementation
├── screenshots/     # Screenshot service
├── skill_cli/       # CLI main + skill-based command structure
├── skills/          # Built-in skill primitives
├── sync/            # Sync/async helpers
├── telemetry/       # PostHog analytics
├── tokens/          # Token counting + cost tracking
└── tools/           # Tool registry (87.2KB service.py = 2nd-largest)
```

**File-size signals:**
- `agent/service.py` = 158.5KB (largest) — Agent orchestration is monolithic despite event-bus
- `browser/session.py` = 151.8KB — BrowserSession monolithic w/ 5-watchdog coordination
- `tools/service.py` = 87.2KB — Tool-registry monolithic
- `cli.py` = 79.6KB — Legacy TUI
- `dom/service.py` = 45.1KB — DOM extraction monolithic
- `mcp/server.py` = 40.5KB — MCP server monolithic
- `agent/views.py` = 36.3KB — Pydantic models
- `browser/profile.py` = 49.3KB — BrowserProfile (display detection, extensions, launch args)
- `browser/demo_mode.py` = 45.0KB — Demo mode (video-recording + highlighting presumed)

**Monolithic-file pattern = corpus-first for T5 at 89.9K scale.** Most corpus T5 wikis show modular-file-size distribution; browser-use has 7 files >40KB. Rationale (from CLAUDE.md): *"When doing any truly massive refactors, trend towards using simple event buses and job queues to break down systems into smaller services"* — i.e., the monoliths ARE the roadmap debt; `bubus` event-bus is the decomposition mechanism. Pre-1.0 versioning consistent with this.

## 4. Event-driven watchdog architecture (5 services)

From CLAUDE.md:
- **DownloadsWatchdog** — PDF auto-download + file management
- **PopupsWatchdog** — JavaScript dialogs + popups
- **SecurityWatchdog** — domain allowlist/blocklist + security policies
- **DOMWatchdog** — DOM snapshots + screenshots + element highlighting
- **AboutBlankWatchdog** — empty-page redirect handling

Plus `watchdog_base.py` (13.6KB) = shared base class.

**bubus event-bus** (`bubus==1.5.6` in pyproject, own package at https://github.com/browser-use/bubus presumed) coordinates all watchdogs through BrowserSession.

**Design implication:** Browser lifecycle + page state are event-driven, not polling. This enables single-browser-multiple-agents (skill_cli register + --connect pattern) and prevents watchdogs from blocking agent loop.

**Corpus-first 5-watchdog named architecture at T5 browser-agent.** Skyvern v24 wraps Playwright events directly; browser-use builds custom event layer.

## 5. 9 system-prompt variants (markdown-based agent skill)

```
browser_use/agent/system_prompts/
├── system_prompt.md                      (23.5K  — default large)
├── system_prompt_anthropic_flash.md      (20.3K  — Claude Sonnet Flash-mode)
├── system_prompt_browser_use.md          (1.2K   — proprietary ChatBrowserUse)
├── system_prompt_browser_use_flash.md    (1011B  — ChatBrowserUse Flash)
├── system_prompt_browser_use_no_thinking.md (1.0K — ChatBrowserUse no-reasoning)
├── system_prompt_flash.md                (2.4K   — generic Flash)
├── system_prompt_flash_anthropic.md      (2.4K   — dup of anthropic_flash?)
├── system_prompt_no_thinking.md          (21.6K  — no-reasoning large)
└── __init__.py
```

**5-axis prompt variant matrix:**
1. Default vs Flash (`flash_mode=True` skips evaluation + next-goal + thinking, uses memory only — fast mode)
2. Thinking vs no-thinking (`use_thinking=True` default — explicit reasoning)
3. Generic LLM vs ChatBrowserUse-optimized (proprietary model gets 1.2KB compressed prompt; generic LLMs get 23KB detailed prompt)
4. Anthropic-specific vs generic
5. Combined variants (anthropic + flash; no-thinking + default; etc.)

**Corpus-first T5 prompt-variant multiplexer** — most T5 agents ship 1-2 system prompts. browser-use has 9 + model-aware dispatch logic in Agent service.

**Strategic interpretation:** LLM-vendor differences matter at T5 browser-agent scale. Fast-cheap models (Flash / no-thinking) and cost-premium models (Sonnet / GPT-4) get materially different prompts. This is one of **why ChatBrowserUse wins benchmarks** — it's paired with a specifically-optimized 1.2KB prompt where generic models get 23KB.

## 6. MCP bidirectional integration

```
browser_use/mcp/
├── __init__.py        (617B)
├── __main__.py        (199B — module entry)
├── client.py          (16.8K — connect to external MCP servers)
├── controller.py      (8.0K)
├── manifest.json      (9.8K — Claude Desktop DXT package descriptor)
├── server.py          (40.5K — expose browser-use tools as MCP)
└── .dxtignore         (4.0K — DXT packaging exclude list)
```

**Bidirectional MCP** (both server + client) is **corpus-first at T5**:
- **Server mode**: `uvx browser-use[cli] --mcp` — expose 30+ browser commands as MCP tools for Claude Desktop / other MCP clients
- **Client mode**: Agent can connect to external MCP servers (filesystem / GitHub / database / etc.) to extend its capabilities beyond browsing

**DXT (Desktop Extension Toolkit) packaging**: manifest.json + .dxtignore = **corpus-first DXT integration at T5**. DXT is Anthropic's Claude Desktop extension format (concurrent with MCP rollout); browser-use ships a `.dxt`-packageable manifest enabling one-click Claude Desktop installation.

**Pattern #18 strengthening — 12th+ data point** with novel bidirectional + DXT sub-observations.

## 7. 15-provider `browser_use/llm/` adapter architecture

```
browser_use/llm/
├── anthropic/         # Claude Sonnet / Opus via Anthropic API
├── aws/               # Bedrock Claude / Titan / Nova
├── azure/             # Azure OpenAI
├── browser_use/       # ChatBrowserUse (proprietary hosted)
├── cerebras/          # Cerebras inference
├── deepseek/          # DeepSeek API
├── google/            # Gemini API
├── groq/              # Groq LPU inference
├── litellm/           # LiteLLM proxy (meta-provider)
├── mistral/           # Mistral API
├── oci_raw/           # Oracle Cloud Infrastructure (OCI)
├── ollama/            # Local Ollama (OSS)
├── openai/            # GPT-4 / o1 / GPT-5 etc.
├── openrouter/        # OpenRouter aggregator
├── vercel/            # Vercel AI Gateway
├── __init__.py (5.0K)
├── base.py (1.5K)
├── messages.py (6.4K)
├── models.py (10.1K)  — model registry
├── schema.py (7.6K)
├── tests/
└── views.py (1.3K)
```

**15 native providers + LiteLLM (meta-provider for 100+ more) = 17-way multi-provider support.** **Largest per-project multi-provider breadth in corpus.** Contrast:
- Skyvern v24: 10+ providers (OpenAI/Anthropic/Bedrock/Gemini/+)
- TrendRadar v19: LiteLLM (100+)
- OpenHands v30: multi-provider native (Claude/GPT/Minimax/BYO)
- multica v15: 8 agent models
- OMC v27: 4 runtimes (Claude/Codex/Gemini/Cursor)

**Pattern #28 Multi-Provider AI Support — 9th+ data point with 2 corpus-first observations:**
1. **Proprietary own-hosted model** (ChatBrowserUse) ALONGSIDE multi-provider — corpus-first commercial-company-ships-own-LLM-as-default
2. **Oracle Cloud Infrastructure (OCI)** — corpus-first OCI LLM-adapter

## 8. `@sandbox` decorator — production deployment primitive

AGENTS.md documents:
```python
from browser_use import Browser, sandbox, ChatBrowserUse

@sandbox(cloud_profile_id='your-profile-id')
async def production_task(browser: Browser):
    agent = Agent(task="Your authenticated task", browser=browser, llm=ChatBrowserUse())
    await agent.run()
```

**Corpus-first T5 decorator-based-deployment**:
- Wraps async function → runs on Browser-Use Cloud infrastructure
- `cloud_proxy_country_code='us'` → geo-routed proxy
- `cloud_profile_id='...'` → uses uploaded browser profile with persisted cookies/auth

**Distinction from Skyvern:** Skyvern has `curl POST /api/v1/run` + YAML workflow builder. browser-use uses Python decorator + `@sandbox` API-first-in-Python.

**Developer UX impact:** same Python code works locally and in production by adding `@sandbox`. Zero config changes. Distinctive T5 commercial-ergonomics move.

## 9. `examples/` 13-subdir taxonomy

```
examples/
├── apps/              # Full applications
├── browser/           # Browser configuration examples
├── cloud/             # Cloud API usage
├── custom-functions/  # @tools.action examples
├── features/          # Agent feature demos (custom_output / initial_actions / sensitive_data / etc.)
├── file_system/       # File access
├── getting_started/   # Simple quickstart
├── integrations/      # 3rd-party integrations
├── models/            # Per-LLM-provider examples (bedrock_claude.py noted in pyproject)
├── observability/     # Laminar + OpenLIT
├── sandbox/           # @sandbox decorator examples
├── ui/                # Terminal UI examples
└── use-cases/         # apply_to_job.py / buy_groceries.py / pcpartpicker.py (demo-shown)
```

**Observation:** Examples are **feature-oriented** (custom-functions / observability / sandbox) rather than task-oriented. Reflects design: browser-use is a library with features, not a workflow builder with templates. Contrast Skyvern's workflow-block template library.

## 10. Test discipline + CI

pyproject dev-dependencies include:
- `pytest==9.0.2` + `pytest-asyncio==1.3.0` + `pytest-httpserver==1.1.3` + `pytest-xdist==3.8.0` + `pytest-timeout==2.4.0`
- `pyright==1.1.408` (static typing)
- `ruff==0.14.14` (linter + formatter)
- `pre-commit==4.5.1`
- `lmnr[all]==0.7.42` (Laminar observability)
- `codespell==2.4.1`

CLAUDE.md test policy:
- **Never mock except LLM** — real objects with pytest-httpserver for HTML fixtures
- **Never real remote URLs** — pytest-httpserver only
- **`tests/ci/` is default test set** — CI runs automatically on commits
- **File naming: `tests/ci/test_action_EventNameHere.py`** — per-event test file

**Corpus-first strict-anti-mock test policy at T5 browser-agent** — enforces realistic test conditions, prevents false-pass via over-mocking.

## 11. Code style opinions

From CLAUDE.md:
- **Async-only** Python (no sync API)
- **Tabs for indentation** in Python (!) — deliberate divergence from PEP 8 (PEP 8 prefers spaces)
- **Python 3.12+ typing**: `str | None` not `Optional[str]`; `list[str]` not `List[str]`
- **pydantic v2 with `ConfigDict(extra='forbid')`** — strict schema
- **`Annotated[..., AfterValidator(...)]`** for validation logic in types
- **`service.py` + `views.py` + `events.py`** file pattern
- **Runtime assertions at function entry/exit** — defensive programming
- **`uuid7str` for all ID fields** — time-sortable UUIDs (uuid-extensions package)
- **Log methods prefixed `_log_...`** — conventional namespace for logging helpers

**Tabs-not-spaces at 89.9K-star Python project** = corpus-first rebellion against PEP 8. Rationale not given in CLAUDE.md; likely founder-preference + "tokens are fewer" considerations for LLM-ingestion.

## 12. Contribution paths

**No CONTRIBUTING.md** visible at repo root (contrast claude-hud v35 7-governance-file set).
**No CODE_OF_CONDUCT.md** visible.
**No SECURITY.md** visible.

Governance: README + AGENTS.md + CLAUDE.md + LICENSE + pyproject.toml + `.pre-commit-config.yaml`. **Medium-light** by contributor-governance count, but **heavy** by AGENTS.md size. Pattern #12 Governance-Depth observation: browser-use inverts the usual heuristic (fewer files, larger individual files).

**Design implication:** browser-use treats AGENTS.md as the single source of truth that replaces multi-file governance. Practical tradeoff: easier to maintain one file; harder for casual contributors who expect standard `.github/CONTRIBUTING.md` lookup.

## 13. Integrations mentioned in skills/remote-browser/SKILL.md

- **Cloudflare tunnels** — `browser-use tunnel <port>` idempotent local-dev-server exposure
- **Multi-agent shared browser** — `--connect $INDEX` with tab-locking (write) + read-only-any-tab (read)
- **Agent session expiry** — 5-minute inactivity timeout for registered agents
- **Python REPL** — `browser-use python "code"` with persisted namespace + `browser` object auto-available

## 14. Notable architectural absences

1. **No Go/Rust components** — pure Python (contrast multica v15 TypeScript+Go; Skyvern adds Node.js frontend)
2. **No GraphQL** — REST only in CLOUD.md
3. **No in-repo benchmarks** — benchmark repo is separate `browser-use/benchmark`
4. **No explicit structured-output schema catalog** — `output_model_schema` is per-task Pydantic (not a browser-use-curated schema library)
5. **No plugin system** beyond `@tools.action` — extensibility is function-registration, not discovery-based plugin loading
6. **No local-first DB** — PostHog for analytics, not local sqlite/duckdb like other T5 entrants
7. **No multi-repo monorepo** — single-package; `browser-use-sdk` + `bubus` + `cdp-use` are independent repos (contrast pi-mono v36 7-package lockstep monorepo)

## 15. Cluster B linkage to Phase 3 entities

- Entity 1 (Core product) draws: sections 3-4, 7, 9, 11
- Entity 2 (Cloud commercial) draws: sections 6 (MCP DXT), 8 (@sandbox), 13 (integrations)
- Entity 3 (Pattern 47/48 resolution) draws: sections 3 (monolithic-file architecture), 4 (watchdog event-driven design)
- Entity 4 (Storm Bear meta) draws: sections 1-2 (AGENTS/CLAUDE discipline), 12 (governance-inversion), 14 (absences)
