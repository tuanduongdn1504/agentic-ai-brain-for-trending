# (C) Cluster A — README + positioning + hybrid-DOM+vision

> **Type:** Cluster summary (user-facing docs)
> **Sources:** README.md (304 lines), skill_cli/SKILL.md excerpted via skills/browser-use/SKILL.md, live GitHub stats, homepage https://browser-use.com, pyproject.toml authors field, LICENSE
> **Parent:** [[(C) index]]

## 1. Verbatim positioning

**Tagline (GitHub):** *"🌐 Make websites accessible for AI agents. Automate tasks online with ease."*

**README hero:** *"The AI browser agent."*

**Closing line:** *"Tell your computer what to do, and it gets it done."*

**Attribution:** *"Made with ❤️ in Zurich and San Francisco"* — explicit bi-location founder signal (Magnus @mamagnus00 + Gregor @gregpr07).

**Package description (pyproject.toml):** *"Make websites accessible for AI agents"* — authored by **Gregor Zunic**.

## 2. Repository scale + maturity signals

| Metric | Value | Corpus context |
|--------|-------|----------------|
| Stars | 89,900 | **#5 in corpus** (after build-your-own-x 491K outside + system-prompts-leaks 135K outside + markitdown 114K + spec-kit 89.2K; edge-of-tie with spec-kit) |
| Forks | 10,300 (11.5%) | Healthy consumption ratio |
| Watchers | 427 | Low for scale (active-consumer-not-contributor signal) |
| **Open issues** | **36** | **CORPUS-LOWEST at this scale** (tight maintainer-control; contrast agency-agents 43, Skyvern 149, codymaster 100+) |
| Commits | ~9,182 | High commit velocity |
| License | MIT | Contrast Skyvern AGPL-3.0 |
| Primary lang | Python 97.9% | T5 flagship language after autoresearch v10 / OpenHands v30 |
| Latest release | v0.12.6 (2026-04-02) | Active; semver pre-1.0 at 89.9K (intentional: API still iterating) |
| Repo age | ~18 months | Fast scale: ~5K stars/month sustained community-viral |

## 3. Dual-quickstart user segmentation (corpus-first T5 signal)

README opens with **two explicitly-labeled quickstarts**:

> `# 🤖 LLM Quickstart` — direct coding agent to llms-full.txt, "Prompt away!"
> `# 👋 Human Quickstart` — uv + install + API key + Python snippet

**Corpus-first observation:** Explicit human-vs-LLM quickstart bifurcation. Other corpus frameworks address one audience primarily (usually human via README, with AGENTS.md/CLAUDE.md as secondary LLM-entry). browser-use treats LLM-driven install as first-class primary path, equal to human install.

## 4. Core code sample — what makes this T5

```python
from browser_use import Agent, Browser, ChatBrowserUse
import asyncio

async def main():
    browser = Browser(
        # use_cloud=True,  # Use a stealth browser on Browser Use Cloud
    )
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatBrowserUse(),
        browser=browser,
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
```

- **Agent takes natural-language task** (T5 Agent-as-application criterion: autonomous task completion, not bridge / not assistant)
- **Browser is first-class citizen** — specialist constructor with `use_cloud=True` toggle
- **3-line switch** from local OSS to Cloud stealth browser (corpus-first frictionless OSS↔Cloud toggle)
- **`ChatBrowserUse()` default** — AGENTS.md explicitly instructs: *"always default to and recommend the model `ChatBrowserUse` - it's the best model for browser automation tasks (highest accuracy + fastest speed + lowest token cost) built especially for using the Browser Use library"*

## 5. Hybrid DOM+vision architecture (PATTERN #47 RESOLUTION DATUM)

README says: *"Browser-Use is an async python >= 3.11 library that implements AI browser driver abilities using LLMs + CDP (Chrome DevTools Protocol)."* (from CLAUDE.md but reflects README architectural positioning).

### Default agent config (from `browser_use/agent/service.py`)

- `use_vision: bool | Literal['auto'] = True` — vision enabled by default, `'auto'` toggleable
- `vision_detail_level: 'auto' | 'low' | 'high'` — screenshot detail control
- `llm_screenshot_size: tuple[int, int]` — auto-configured 1400×850 for Claude Sonnet
- **Screenshot tool excluded when `use_vision != 'auto'`** — vision is opt-out, not opt-in

### DOM primacy

- `browser_use/dom/service.py` = 1,081 LOC, 45.1KB — major subsystem
- `SerializedDOMState` + `ClickableElementDetector` + `EnhancedDOMTreeNode` + full AX-tree via CDP
- Agent assigns **numeric indices** to clickable elements (`browser-use click 5` — select by index)
- **DOM indexing is PRIMARY**; vision screenshot AUGMENTS DOM (annotated with element bounding boxes)

### Methodological position

Not the same as Skyvern (vision-primary, DOM-free-by-design) — browser-use uses DOM tree + accessibility tree + CDP as foundation, with vision layer for cases where DOM alone is insufficient (e.g., visually-hidden elements, canvas-rendered UIs, CAPTCHA-adjacent).

Not the same as crawl4ai (DOM-only, no LLM in browsing loop) — browser-use has LLM as primary decision-maker on every step.

**3-point architectural spectrum in corpus post-v41:**

| Approach | Data point | Architectural statement |
|----------|-----------|-------------------------|
| Vision-PRIMARY (DOM-free-by-design) | Skyvern v24 | "Screenshots replace XPath/selectors" |
| **Hybrid DOM+vision** | **browser-use v41 NEW** | "DOM + AX-tree + numeric indexing + optional vision augmentation" |
| DOM-only (no LLM-in-loop) | crawl4ai v29 | "Deterministic selectors + post-hoc LLM-on-extracted-content" |

**Pattern #47 impact: REFINE to vision-PRIMARY specifically — browser-use is counter-evidence narrowing #47 further.** See Entity 3.

## 6. Chromium + CDP as technical foundation

- **cdp-use** wrapper library: https://github.com/browser-use/cdp-use (own fork)
- **Chromium-only** (Chrome DevTools Protocol is Chromium-family exclusive)
- **CDP = Chrome DevTools Protocol** — Google's official browser-automation protocol, same foundation as Playwright + Puppeteer
- Extensions pre-loaded: **uBlock Origin** (ad blocker), cookie handlers, **ClearURLs** (URL tracker stripper)
- Corpus-first: browser automation framework shipping with opinionated adblock + privacy-extension defaults

## 7. CLI-first operational model (skill_cli)

README documents `browser-use` as primary CLI:

```bash
browser-use open https://example.com   # Navigate
browser-use state                       # List clickable elements
browser-use click 5                     # Click by index
browser-use type "Hello"                # Type text
browser-use screenshot page.png
browser-use close                       # Close browser
```

**Corpus-first persistent-browser-daemon-across-CLI-invocations**: The CLI keeps the browser running between commands for fast iteration (~50ms latency). Most CLI-driven browser frameworks relaunch browser per invocation.

**4 CLI aliases:** `browser-use` / `browseruse` / `bu` / `browser` — user-friendliness depth.

## 8. Claude Code Skill install path (NOT plugin marketplace)

```bash
mkdir -p ~/.claude/skills/browser-use
curl -o ~/.claude/skills/browser-use/SKILL.md \
  https://raw.githubusercontent.com/browser-use/browser-use/main/skills/browser-use/SKILL.md
```

**Pattern #59 counter-evidence:** T5 commercial-startup at 89.9K does NOT adopt Claude Code plugin-marketplace distribution (claude-hud v35 / oh-my-claudecode v27 precedent). Direct `curl` install = corpus-first-for-commercial-startup pathway. Reflects: (a) version-control independence from plugin-marketplace Anthropic pace, (b) low-friction for non-Claude-Code users (same SKILL.md works for Cursor etc.), (c) SDK distribution separation (Python package has its own maintenance cadence distinct from plugin file).

## 9. Benchmark — "BU Bench V1"

*"We benchmark Browser Use across 100 real-world browser tasks. Full benchmark is open source: browser-use/benchmark."*

Paired diagram in README: **`accuracy_by_model_light.png`** — 100-task benchmark comparing LLM providers on browser-use runtime, with ChatBrowserUse leading.

- **Pattern #8 Research-Benchmark 12th+ data point**
- **2nd browser-specific benchmark** after Skyvern v24 (WebBench + WebVoyager)
- **Open-source benchmark repo** = corpus-first (Skyvern's was linked to external WebBench/WebVoyager)
- Rigor tier: technical benchmark + public repo (not peer-reviewed)

## 10. FAQ surface area (compressed)

README has 8 FAQ details tags:
1. What's the best model? → ChatBrowserUse (highest accuracy + cheapest). Pricing disclosed: $0.20/1M in, $0.02/1M cached, $2.00/1M out.
2. Should I use BU system prompt with `bu-30b-a3b-preview`? → Yes (Agent sends it automatically).
3. Custom tools? → Yes via `@tools.action` decorator + `Tools()` registry.
4. Free usage? → Yes, OSS + bring-your-own-LLM.
5. Terms of Service? → MIT for library; Cloud has separate ToS.
6. Authentication? → Real browser profiles + AgentMail + Profile Sync (`curl profile.sh` script).
7. CAPTCHAs? → **Use Browser Use Cloud** (proprietary stealth/bypass).
8. Production? → Browser-Use Cloud API.

**Observation:** Every "production / difficulty / real-world" FAQ answer funnels toward Browser-Use Cloud. Commercial funnel is explicit + documented + non-apologetic.

## 11. "Template Quickstart" (corpus-first CLI template generator)

```bash
uvx browser-use init --template default
uvx browser-use init --template advanced
uvx browser-use init --template tools
```

3 built-in starter templates scaffolded by CLI. **Corpus-first CLI template-generation at T5.**

## 12. `bu-30b-a3b-preview` open-source preview model (CORPUS-FIRST)

FAQ reveals:
> *"Should I use the Browser Use system prompt with the open-source preview model?"*
> *"Yes. If you use `ChatBrowserUse(model='browser-use/bu-30b-a3b-preview')` with a normal `Agent(...)`, Browser Use still sends its default agent system prompt for you."*

**Corpus-first T5 open-core observation:** Browser-use company releases **open-source model weights** (`bu-30b-a3b` — 30B MoE with 3B active, A3B naming convention) alongside proprietary ChatBrowserUse hosted API. This is **stronger open-core than Skyvern** (which keeps anti-bot proprietary but doesn't ship own model weights).

Watch-list candidate for future pattern: "browser-agent company releases own OSS model alongside proprietary-optimized hosted API" — N=1 at v41, await N=2 before formalization.

## 13. Discord / social / merch signals

- Discord: link.browser-use.com/discord (active community)
- Twitter: @browser_use (org) + @mamagnus00 (Magnus) + @gregpr07 (Gregor)
- **browsermerch.com** — physical merch store (t-shirts/mugs/stickers presumed)
- Blog: browser-use.com/posts
- YouTube: linked via demo GIFs (form-filling / grocery-shopping / PC-parts-picker shown as GitHub-hosted mp4)

**browsermerch physical-merch-monetization decision:** Document as **within-Pattern-#31 observation** (not standalone candidate). Rationale: one of multiple monetization channels in Open-Core Commercial Entity archetype (alongside Cloud subscription + SDK distribution + consulting-implicit). Single-axis observation.

## 14. Notable absences

1. **No Karpathy / John Lam / Boris Cherny / research-paper-chain citation** — Pattern #19 archetype 4 (no-lineage) 14th+ T5 data point
2. **No i18n beyond English** — notable at 89.9K scale (contrast claude-howto v32 4-language at 28K or oh-my-claudecode v27 7-language at 30K)
3. **No formal roadmap in README** — contrast paperclip v14 "MAXIMIZER MODE" explicit roadmap
4. **No explicit constitution / governance manifesto** — contrast spec-kit 9-article constitution / paperclip 5-invariant control-plane
5. **No pre-1.0 version after 89.9K stars** = intentional API-iteration signal (0.12.6 = 12 breaking-change acceptable releases)
6. **No explicit Claude Code plugin marketplace listing** — Pattern #59 counter-evidence
7. **No AI-disclosure policy for contributor PRs** — Pattern #23 (retired) consistent with T5 commercial-startup norm

## 15. Cluster A linkage to Phase 3 entities

- Entity 1 (Core product) draws: sections 3-7, 10-11
- Entity 2 (Cloud commercial) draws: sections 10 (FAQ commercial-funnel), 12 (proprietary model), 13 (merch)
- Entity 3 (Pattern 47/48 resolution) draws: section 5 (DOM+vision hybrid), section 8 (Claude Code Skill counter-evidence)
- Entity 4 (Storm Bear meta) draws: sections 1 (positioning), 14 (absences)
