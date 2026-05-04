# (C) Core product — Agent + Browser + Tools + Hybrid DOM+Vision + 15 LLM providers

> **Type:** Entity — core product architecture
> **Parent:** [[(C) index]]
> **Sources:** Cluster A §3-7, Cluster B §3-5, 7, 11; pyproject.toml; `browser_use/agent/service.py` 158.5KB; `browser_use/browser/session.py` 151.8KB; `browser_use/dom/service.py` 45.1KB; `browser_use/tools/service.py` 87.2KB; 9 system-prompt variants
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

browser-use is an **async-Python T5 Agent-as-application** for autonomous browser automation. **Agent + Browser + Tools** = 3 top-level user-facing primitives. Architecture is **hybrid DOM+vision** (DOM-tree indexing primary; screenshot-augmentation secondary via `use_vision='auto'`), distinct from vision-primary (Skyvern v24) and DOM-only (crawl4ai v29). **15+ LLM providers** native + LiteLLM (meta-provider for 100+ more). **9 system-prompt variants** with model-aware dispatch. **Event-driven 5-watchdog** architecture via own `bubus` event bus. **CDP-based** via own `cdp-use` Chromium wrapper. MIT-licensed + 89.9K stars (corpus #5) + 2-founder team (Magnus Zurich + Gregor SF) + commercial Browser-Use Cloud tier.

## 2. The Agent primitive

### Minimal API

```python
from browser_use import Agent, Browser, ChatBrowserUse
import asyncio

async def main():
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatBrowserUse(),
    )
    await agent.run()

asyncio.run(main())
```

### 40+ Agent parameters (selected)

**Vision / processing:** `use_vision: bool | Literal['auto'] = True` / `vision_detail_level='auto'|'low'|'high'` / `page_extraction_llm` / `llm_screenshot_size`

**Actions / behavior:** `max_actions_per_step=3` (form-filling multi-field) / `max_failures=3` / `final_response_after_failure=True` / `use_thinking=True` / `flash_mode=False` / `initial_actions` / `directly_open_url=True`

**System messages:** `override_system_message` (full replace) / `extend_system_message` (append)

**File / data:** `save_conversation_path` / `available_file_paths` / `sensitive_data` (dict of env→placeholder mapping; agent sees placeholder, LLM sees value)

**Visual output:** `generate_gif=False` / `include_attributes`

**Performance:** `max_history_items` / `llm_timeout=90` / `step_timeout=120`

**Advanced:** `calculate_cost=False` / `display_files_in_done_text=True` / `output_model_schema` (Pydantic class for structured output)

**Execution:** `agent.run(max_steps=100)` returns `AgentHistoryList` with ~15 helper methods (`.urls()`, `.screenshots()`, `.action_names()`, `.errors()`, `.model_thoughts()`, `.total_duration_seconds()`, `.structured_output`, etc.)

## 3. The Browser primitive (50+ parameters)

`Browser` is an alias for `BrowserSession`. Key categories:

- **Display** (8 params): `headless`, `window_size`, `window_position`, `viewport`, `device_scale_factor`
- **Behavior** (7 params): `keep_alive`, `allowed_domains` (glob patterns, wildcard-TLD prohibited for security), `prohibited_domains`, `enable_default_extensions=True` (uBlock + cookie handlers + ClearURLs), `cross_origin_iframes=False`, `is_local=True`
- **Profile** (3 params): `user_data_dir`, `profile_directory='Default'`, `storage_state`
- **Network / security** (3 params): `proxy` (ProxySettings), `permissions=['clipboardReadWrite', 'notifications']`, `headers`
- **Launch** (6 params): `executable_path`, `channel='chromium'|'chrome'|'msedge'`, `args`, `env`, `chromium_sandbox=True`, `devtools=False`, `ignore_default_args`
- **Timing** (3 params): `minimum_wait_page_load_time=0.25`, `wait_for_network_idle_page_load_time=0.5`, `wait_between_actions=0.5`
- **AI integration** (2 params): `highlight_elements=True` (annotate interactive elements in screenshots), `paint_order_filtering=True` (remove elements hidden by paint-order)
- **Downloads** (3 params): `accept_downloads=True`, `downloads_path`, `auto_download_pdfs=True`
- **Recording** (6 params): `record_video_dir`, `record_video_size`, `record_video_framerate=30`, `record_har_path`, `traces_dir`, `record_har_content='embed'|'omit'|'attach'`
- **Advanced**: `disable_security=False` (⚠️ not recommended), `deterministic_rendering=False`
- **Cloud:** `use_cloud=True` → toggle to Browser-Use Cloud stealth browser (1-line switch; primary commercial funnel)

### Domain allowlist / blocklist auto-optimization

Lists with 100+ domains auto-convert to sets for O(1) lookup; pattern matching disabled for optimized lists. `www.example.com` + `example.com` variants both checked.

### Real-Chrome profile mode

```python
browser = Browser(
    executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    user_data_dir='~/Library/Application Support/Google/Chrome',
    profile_directory='Default',
)
```

Reuses existing Chrome installation + logged-in profile. Chrome must be fully closed first.

## 4. The Tools primitive (custom actions)

### Decorator-based tool registration

```python
from browser_use import Tools

tools = Tools()

@tools.action(description='Description of what this tool does.')
def custom_tool(param: str) -> str:
    return f"Result: {param}"

agent = Agent(task="...", llm=llm, browser=browser, tools=tools)
```

`Tools` is aliased `Controller` for backward compatibility.

### Built-in tools (from tools/service.py 87.2KB + skill_cli commands)

Core browser actions: `click` / `type` / `input` (click + clear + type combined) / `scroll` / `screenshot` / `open` / `back` / `hover` / `dblclick` / `rightclick` / `keys` / `select` / `upload` / `eval` (JS execution) / `get` (title/html/text/value/attributes/bbox) / `wait` (selector/text with --state + --timeout) / `cookies` (get/set/clear/export/import)

### Scope

- **ActionResult** = structured return type (per AGENTS.md: *"Prefer returning `ActionResult` with structured content to help the agent reason better"*)
- **Pydantic v2 schema** via `ConfigDict(extra='forbid')` — strict-by-default
- **Async-only** action signatures

## 5. Hybrid DOM+Vision architecture (Pattern #47 resolution datum)

### DOM primacy

`browser_use/dom/service.py` (45.1KB, 1,081 LOC) + `browser_use/dom/serializer/` + `browser_use/dom/views.py` (32.2KB) build a rich representation per page:

- **EnhancedDOMTreeNode** — full DOM tree with accessibility annotations
- **SerializedDOMState** — serialized representation for LLM prompt
- **ClickableElementDetector** — identifies interactive elements, assigns numeric indices
- **AX-tree via CDP** (`GetFullAXTreeReturns`) — accessibility tree for semantic understanding
- **paint_order_filtering** — removes elements hidden by paint order (visible but occluded)
- **cross_origin_iframes** — optional iframe traversal
- **Hidden-elements detection** via computed styles + bounding-box + parent-visibility

### Vision augmentation (secondary layer)

- **`use_vision: bool | Literal['auto'] = True`** — vision-layer enabled by default
- **Screenshot with element highlighting** — annotated bounding boxes around clickable elements (`highlight_elements=True`)
- **`vision_detail_level`** — low/high/auto controls image detail sent to LLM
- **`llm_screenshot_size`** — auto-configured 1400×850 for Claude Sonnet models
- **Screenshot tool excluded when `use_vision != 'auto'`** — vision is opt-out of being available to Agent

### Architectural implication

DOM provides **stable element IDs** (indices) that Agent references. Vision provides **disambiguation signal** when DOM alone is ambiguous (e.g., visually-similar elements with same role / canvas-rendered text / CAPTCHA-area).

**Comparison triangle (v41 corpus):**

| Approach | Primary signal | Secondary signal | Corpus data point |
|----------|---------------|------------------|-------------------|
| Vision-PRIMARY (DOM-free-by-design) | Screenshot | LLM-coord-reasoning | Skyvern v24 |
| **Hybrid DOM+vision** | **DOM tree + AX-tree indices** | **Screenshot augmentation** | **browser-use v41 NEW** |
| DOM-only (no LLM-in-loop) | Deterministic selectors | Post-hoc LLM on extracted content | crawl4ai v29 |

See Entity 3 for full Pattern #47 resolution analysis.

## 6. Event-driven watchdog architecture

### 5 watchdogs (under `browser_use/browser/watchdogs/`)

1. **DownloadsWatchdog** — PDF auto-download + file management
2. **PopupsWatchdog** — JavaScript dialogs + popups
3. **SecurityWatchdog** — domain allowlist/blocklist enforcement
4. **DOMWatchdog** — DOM snapshots + screenshots + element highlighting
5. **AboutBlankWatchdog** — empty-page redirect handling

Plus `watchdog_base.py` (13.6KB) = shared base with event-subscription + lifecycle hooks.

### bubus event bus

`bubus==1.5.6` — own lightweight event bus package. Coordinates watchdogs through BrowserSession without blocking Agent loop.

**Design rationale:** Browser lifecycle events (download / popup / navigation / CDP target change) happen out-of-band from Agent step execution. Event-bus decouples reactive handling from sequential Agent reasoning.

### BrowserSession monolith (151.8KB)

Single file coordinates:
- CDP client + session management
- Target attach/detach
- Event-subscription dispatch
- Tab lifecycle (single vs multi-tab with `register` + `--connect`)
- Profile loading + persistence
- Extension registration
- Display configuration detection (macOS via `AppKit.NSScreen`, Linux/Windows via `screeninfo`)

## 7. CDP integration via own cdp-use wrapper

`cdp-use==1.4.5` — own fork/wrapper at https://github.com/browser-use/cdp-use.

**Usage pattern (from CLAUDE.md):**
```python
cdp_client.send.DOMSnapshot.enable(session_id=session_id)
cdp_client.send.Target.attachToTarget(params=ActivateTargetParameters(targetId=target_id, flatten=True))
cdp_client.register.Browser.downloadWillBegin(callback_func_here)
```

Typed, domain-organized CDP API. Not Playwright-compatible (different abstraction).

**Why not Playwright:** Playwright bundles opinionated browser-launching + sync/async APIs + multi-browser support (Firefox / WebKit). browser-use needs Chromium-only + pure-async + direct CDP control + own extension handling. Forking CDP-use = own dependency-surface minimization.

## 8. 15 LLM provider adapters + LiteLLM meta-provider

Under `browser_use/llm/`:

| Provider | Subdir | Corpus notes |
|----------|--------|--------------|
| Anthropic | `anthropic/` | Claude Sonnet/Opus native |
| AWS Bedrock | `aws/` | Bedrock Claude + Titan + Nova |
| Azure OpenAI | `azure/` | |
| **Browser-Use** | `browser_use/` | **ChatBrowserUse proprietary hosted** |
| Cerebras | `cerebras/` | Fast inference |
| DeepSeek | `deepseek/` | |
| Google | `google/` | Gemini |
| Groq | `groq/` | LPU inference |
| **LiteLLM** | `litellm/` | **Meta-provider for 100+ upstream** |
| Mistral | `mistral/` | |
| **OCI** | `oci_raw/` | **CORPUS-FIRST Oracle Cloud adapter** |
| Ollama | `ollama/` | Local OSS models |
| OpenAI | `openai/` | GPT + o-series |
| OpenRouter | `openrouter/` | Aggregator |
| Vercel | `vercel/` | AI Gateway |

**Total addressable providers: ~115** (15 native + 100+ via LiteLLM).

**Pattern #28 Multi-Provider AI Support — 9th+ data point + 2 corpus-firsts:**
1. **ChatBrowserUse proprietary hosted model** bundled as default within OSS multi-provider list
2. **Oracle Cloud Infrastructure (OCI) LLM adapter** — first OCI adapter in corpus

## 9. ChatBrowserUse proprietary model (corpus-first pricing-inside-README)

**Pricing disclosed in README FAQ:**
- Input tokens: $0.20/1M
- Cached input tokens: $0.02/1M
- Output tokens: $2.00/1M

**Positioning:** *"optimized Browser Use model"*. Routes to "best frontier foundation model as determined by Browser Use internal evaluations" with **batching + caching + proprietary tricks**.

**AGENTS.md instructs LLMs:** *"always default to and recommend the model `ChatBrowserUse`"*.

**Open-source preview:** `browser-use/bu-30b-a3b-preview` — open-weights MoE model (30B total / 3B active per a3b nomenclature). Usable as:
```python
ChatBrowserUse(model='browser-use/bu-30b-a3b-preview')
```

**Corpus-first browser-agent-company-releases-OSS-model-alongside-proprietary-hosted-API.** Watch-list candidate (N=1 at v41).

## 10. 9 system-prompt variants (model-aware dispatch)

From `browser_use/agent/system_prompts/`:

| Variant | Size | Target |
|---------|------|--------|
| `system_prompt.md` | 23.5K | Default generic LLM (large) |
| `system_prompt_no_thinking.md` | 21.6K | Generic LLM, no-reasoning mode |
| `system_prompt_anthropic_flash.md` | 20.3K | Claude Sonnet Flash-mode |
| `system_prompt_flash.md` | 2.4K | Generic Flash-mode compressed |
| `system_prompt_flash_anthropic.md` | 2.4K | Anthropic Flash (possibly variant of `_anthropic_flash`) |
| `system_prompt_browser_use.md` | 1.2K | **ChatBrowserUse proprietary — compressed** |
| `system_prompt_browser_use_flash.md` | 1011B | ChatBrowserUse Flash |
| `system_prompt_browser_use_no_thinking.md` | 1.0K | ChatBrowserUse no-reasoning |

**5-axis multiplexer:**
1. Default vs Flash (`flash_mode=True` skips evaluation + next-goal + thinking, uses memory only)
2. Thinking vs no-thinking
3. Generic vs ChatBrowserUse-optimized
4. Anthropic-specific optimization
5. Combined variants

**Strategic insight:** The ChatBrowserUse 1.2KB prompt vs generic 23KB delta = **19× smaller prompt surface**. Proprietary model was fine-tuned to not need the generic-model handholding. Explains why ChatBrowserUse claims "3-5× faster" on same benchmarks — less prompt overhead per step.

## 11. MCP bidirectional (server + client)

**Server mode:**
```bash
uvx browser-use[cli] --mcp
```
Exposes browser commands as MCP tools → consumable by Claude Desktop / Cursor / Windsurf / other MCP clients.

**Client mode:**
Agent connects to external MCP servers (filesystem / GitHub / database / etc.) to extend capabilities beyond browsing. Connection mgmt in `browser_use/mcp/client.py` (16.8KB).

**DXT packaging:** `browser_use/mcp/manifest.json` + `.dxtignore` → Desktop Extension format for Claude Desktop one-click install. **Corpus-first DXT integration at T5.**

**Pattern #18 strengthening — 12th+ data point** with bidirectional + DXT sub-observations.

## 12. CLI surface (skill_cli)

Primary CLI (`browser-use` binary with 4 aliases):
```
open / state / click / input / type / keys / select / upload / hover / dblclick / rightclick / scroll / back
screenshot / get (title|html|text|value|attributes|bbox) / eval / wait (selector|text)
cookies (get|set|clear|export|import) / tab (list|new|switch|close)
close / sessions / register / connect / cloud (connect|login|logout|v2|v3|signup)
config (list|set|get|unset) / doctor / setup / init (--template default|advanced|tools)
profile (list|sync|update) / tunnel (start|list|stop) / python (--file|--vars|--reset)
--mcp (run as MCP server) / --headed / --profile / --cdp-url / --session / --json / --connect
```

**Persistent-browser-daemon-across-CLI-invocations** (~50ms latency between commands via daemon). Corpus-first.

**Chaining:** `&&`-safe because daemon preserves browser state:
```bash
browser-use open https://example.com && browser-use state
browser-use input 5 "user@email" && browser-use input 6 "password" && browser-use click 7
```

## 13. Tech stack summary

- **Runtime:** Python 3.11+, async-only
- **Dependencies (main):** aiohttp / pydantic v2 / bubus (event bus) / cdp-use (CDP wrapper) / cloudpickle / rich / click / InquirerPy / httpx / posthog / psutil
- **LLM deps:** anthropic / google-genai / openai / groq / ollama / (wrapping 15 providers)
- **Browser deps:** python-dotenv / pyobjc (macOS) / screeninfo (Linux/Windows) / markdownify (page text)
- **PDF / files:** pypdf / reportlab / python-docx
- **MCP:** `mcp==1.26.0`
- **Cloud SDK:** `browser-use-sdk==3.4.2` (internal circular dep)
- **CLI extras:** textual (TUI) / imageio[ffmpeg] (video) / agentmail (examples)
- **Dev:** pytest (9.0.2) / pyright / ruff / pre-commit / lmnr[all] (Laminar) / codespell
- **CVE-active patches visible:** aiohttp 3.13.4 / pypdf 6.10.2 / pillow 12.2.0 — security discipline

## 14. Limitations + tradeoffs

### Architecture tradeoffs

- **Chromium-only** — CDP is Chromium-exclusive (not Firefox, not WebKit)
- **Monolithic files** (7 files >40KB) — refactor debt acknowledged in CLAUDE.md
- **Pre-1.0 API** (v0.12.6 at 89.9K stars) — intentional iteration signal; breaking changes possible
- **Python-only** (no Go/Rust/Node bindings; TypeScript SDK is Cloud-only not local-runtime)
- **Async-only** — no sync API
- **Tabs-not-spaces** Python indentation (contributor friction vs PEP 8 expectation)

### Commercial tradeoffs

- **Anti-bot / CAPTCHA / proxies Cloud-gated** (Pattern #48 promoted to N=2)
- **`ChatBrowserUse` default = API-key required** — 5 free tasks then billing
- **Cloud session 15-min cap** — long-horizon tasks need re-spawning

### Functional limitations

- **No output_model_schema for Tools** — structured output is agent-level, not tool-level
- **No plugin discovery system** — `@tools.action` decorator requires import-time registration
- **No local-first skills-marketplace** — skills-marketplace is Cloud-only
- **No formal constitution / invariants** — contrast spec-kit v17 / paperclip v14

## 15. Cross-references

- [[(C) Browser-Use Cloud + commercial-funnel + stealth gated + browsermerch]] — commercial ecosystem (Entity 2)
- [[(C) Pattern 47 + 48 Resolution + Browser T5 N=2 + Skyvern structural pair]] — pattern analysis (Entity 3)
- [[(C) Storm Bear meta-entity 30th consecutive + vault-adjacent lessons]] — operator meta (Entity 4)
- Cluster A §3-7, 10-11 + Cluster B §3-5, 7, 11 — source evidence
- Sibling T5: Skyvern v24 (browser peer) / deer-flow v9 / autoresearch v10 / paperclip v14 / OpenHands v30 / DeepTutor v38
- Sibling pattern: crawl4ai v29 (Pattern #47 3-point spectrum) / awesome-mcp-servers v31 (MCP registry) / Unsloth v23 (Pattern #46 un-stale partner)

---

**Agent + Browser + Tools as user-facing primitives. Hybrid DOM+vision (DOM-primary + screenshot-augmentation) = corpus-first at T5, 3rd point on architectural spectrum. 15+ LLM providers including proprietary ChatBrowserUse + open-source `bu-30b-a3b-preview`. 9 system-prompt variants with model-aware dispatch. Event-driven 5-watchdog via own `bubus`. Bidirectional MCP + DXT packaging. MIT + pre-1.0 + 89.9K stars + Zurich/SF 2-founder team.**
