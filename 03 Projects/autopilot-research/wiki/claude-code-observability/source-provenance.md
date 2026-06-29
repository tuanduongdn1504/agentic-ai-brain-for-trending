# Source provenance — claude-code-observability

> What's first-party-verified vs creator-personal vs unverifiable. Compiled 2026-06-20 from the video transcript (read in full), a 6-agent deep-dive of the originals, and an adversarial verify pass (Workflow `wf_5398ccab-88a`, 29 agents) + a follow-up first-party fact-check (claude-code-guide).
>
> **Tier key:** T1 = first-party (Anthropic / OpenTelemetry / CNCF) · T2 = community third-party · T3 = creator-personal (Mansel Scheffel's own build, shown in the video).

---

## Sources — the video + the originals deep-dived

| Source | Tier | URL | What we took | Status |
|---|---|---|---|---|
| Mansel Scheffel, "Claude Code + OpenTelemetry = Claude Command Center" | T3 creator | [youtube.com/watch?v=dITtLiC9FzM](https://www.youtube.com/watch?v=dITtLiC9FzM) | The thesis (observability-first), the panel selection, the Telegram-HITL UX, the "just use Cowork" stance — **full auto-sub transcript read in full** | The CONCEPT is sourced; the creator's specific build is UNVERIFIABLE |
| Claude Code monitoring / OpenTelemetry docs | T1 Anthropic | https://code.claude.com/docs/en/monitoring-usage | `CLAUDE_CODE_ENABLE_TELEMETRY`, the OTEL_* env vars, exporters (otlp/prometheus/console), metric & event catalogs, cardinality controls, plan availability | AUTHORITATIVE |
| Claude Code costs / usage docs | T1 Anthropic | https://code.claude.com/docs/en/costs | Native `/cost`, `/usage`, `/stats` views; subscription-vs-API distinction; Console Analytics dashboard (Team/Enterprise) | AUTHORITATIVE |
| OpenTelemetry specification | T1 CNCF | https://opentelemetry.io/docs/ | 3 signals (traces/metrics/logs), OTLP (gRPC 4317 / HTTP 4318), Collector (receivers→processors→exporters), semantic conventions, backend-agnostic design | AUTHORITATIVE |
| Anthropic engineering: "Code execution with MCP" | T1 Anthropic | https://www.anthropic.com/engineering/code-execution-with-mcp | Why MCP is token-hungry; the code-execution / progressive-disclosure fix; documented token savings; tool-search + `defer_loading` | AUTHORITATIVE |
| Claude Code JSONL session logs | T1 Anthropic | docs (sessions) | `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl`; token fields (input/output/cache_creation/cache_read); retention | AUTHORITATIVE (path confirmed; some sub-fields single-source) |
| `ryoppippi/ccusage` | T2 community | https://github.com/ryoppippi/ccusage | JSONL cost-report parser (by model/project/day) | CONFIRMED EXISTS |
| `ColeMurray/claude-code-otel` | T2 community | https://github.com/ColeMurray/claude-code-otel | A pre-built Claude Code OTEL observability stack (Prometheus + Grafana) | CONFIRMED EXISTS |
| autopilot-research sibling wikis | T1 own | `wiki/{claude-api-cost-optimization,telegram-remote-control-stack,autonomous-loops-human-in-the-loop}/` | Cache-hit-rate-as-#1-lever; the Telegram HITL recipe (Recipe A pilot-verified); drafts-not-sends HITL framing | CROSS-LINKED, not re-derived |

---

## Claim verdicts (the video's load-bearing claims)

| Claim | Verdict | Note |
|---|---|---|
| OTEL is available on **Pro/Max** plans | **CONFIRMED** | `CLAUDE_CODE_ENABLE_TELEMETRY=1` works for individual subscription users; not gated to a tier in the docs. |
| "...they **finally released** it to Max/Pro; **previously enterprise only**" | **UNCONFIRMED** | No docs evidence of an enterprise-only era or a release-expansion date. Likely the creator's perception. Treat the history claim as unverified. |
| **JSONL logs** track everything Claude + Cowork use | **CONFIRMED (Claude Code) / PARTIAL (Cowork)** | Claude Code JSONL path + token fields confirmed. The **Cowork** JSONL path (`~/Library/Application Support/Claude/local-agent-mode-sessions/`) + metadata are the **creator's video claim, not in first-party docs**. |
| There's a **"shiny mediocre dashboard inside Claude Code's GUI, fed partially by OTEL"** | **PARTIALLY REFUTED — nuance** | Native usage *views* DO exist (`/cost` session API cost, `/usage` tokens+plan limits, `/stats` heatmap, the statusline) **and** a **Console Analytics dashboard** for Team/Enterprise — but these read **local/account data, not the OTEL pipeline**, and none is a customizable OTEL-fed *panel* dashboard. The rich command center in the video is the creator's **external** build. ⚠️ **An earlier draft over-corrected to a flat "no `/cost`/`/usage` commands exist" — that was wrong and was fixed; the commands DO exist.** |
| OTEL exposes cache hit rate, token-by-model, MCP/tool latency+error, per-skill cost | **CONFIRMED** | `claude_code.token.usage` (type incl. cacheRead/cacheCreation, model), `claude_code.cost.usage` (skill.name), `tool_result` event (`duration_ms`, `success`), `api_request` (cache_read/creation tokens). |
| Code execution fixes MCP token bloat | **CONFIRMED (first-party)** | Anthropic's "Code execution with MCP" documents the mechanism + large token reductions; tool-search + `defer_loading` avoid loading every schema up front. |
| Requires-approval task → **Telegram → approve from phone** | **CONFIRMED (pattern) / implementation UNVERIFIABLE** | The pattern is feasible + documented in [[../telegram-remote-control-stack/_index]] (Recipe A pilot-verified). The creator's exact UI is his own unreleased build. |
| Per-skill **model assignment** (don't Opus-everything) reduces cost/context | **CONFIRMED** | A real Claude Code capability + an Anthropic cost-discipline recommendation ([[../claude-api-cost-optimization/_index]]). |
| **Cache hit rate is the #1 cost lever**; timestamp in system prompt kills it | **CONFIRMED (first-party)** | Matches Anthropic Platform guidance (Puneet Shah, Code with Claude London) captured in [[../claude-api-cost-optimization/_index]]: cached reads ~0.1×, the timestamp-prefix invalidation. |
| AI-news-monitor burned **32M tokens / 23 sessions** | **UNVERIFIABLE** | The creator's personal datapoint. Reproducible in principle via `ccusage` on your own JSONL, but his exact number isn't checkable. |
| **Cowork does "98%+"** of what an IDE AI-OS does | **UNVERIFIABLE** | The creator's subjective estimate; no measured basis. |

---

## ⚠️ Single-source / not-re-confirmed metric names (Rule 12 fail-loud)

The metric/event catalog came from the first-party `monitoring-usage` docs fetch (R1). An independent cross-check (claude-code-guide, WebSearch) corroborated most names but **could not re-confirm three** (the docs page was partly truncated for the cross-checker):

- **`claude_code.pull_request.count`** — single-source.
- **`claude_code.code_edit_tool.decision`** — single-source (may instead surface as a `tool_decision` event).
- The **`type` attribute** on `claude_code.token.usage` — the input/output/cacheRead/cacheCreation split is widely reported, but the exact attribute *key* wasn't re-verified.

Also **`CLAUDE_CODE_OTEL_HEADERS_HELPER`** (dynamic OTLP auth headers): the `otelHeadersHelper` feature is real, but the exact env-var name + debounce default weren't fully confirmable. **Verify all four against your live `/usage` output / backend before depending on the exact strings.**

---

## What is the creator's own un-shared build (UNVERIFIABLE)

These appear in the video but are the creator's proprietary/unreleased work — not built-in Claude Code, not public:

1. **The command-center UI itself** — the panelized OTEL dashboard.
2. **"IQ agent"** — a task router between Sonnet/Opus.
3. **"Posture" skill** — security/MCP-poisoning audit.
4. **"Context" skill** — context-efficiency audit.
5. **The Telegram requires-approval HITL UI** — the pattern is standard; his exact implementation is not shared.
6. **The "build your own" prompt + guide** — gated behind a Google Drive folder + a paid Skool community (`skool.com/ainative`); **not publicly reproducible**.

---

## Fetch gaps / notes

- The video page itself is a YouTube SPA — metadata + transcript came via `yt-dlp` (en-orig auto-subs), not WebFetch.
- A `/cost` docs page 404'd for one research agent, which **caused the over-correction** noted above (concluding the commands don't exist). The follow-up first-party fact-check corrected it.
- The video **never names its observability backend** — so which stack Mansel runs is unconfirmed; this topic documents the canonical options instead.
- Four of the five community stacks in [[observability-backend-stack]] are unverified leads from a web-search pass (only `ColeMurray/claude-code-otel` + `ryoppippi/ccusage` were confirmed); maintenance status is not verified.

---

## See also

- [[_index]] · [[video-to-original-crosswalk]] · [[claude-code-opentelemetry]] (the load-bearing original)
- [[../claude-api-cost-optimization/_index]] (the cache/cost levers this measures) · [[../agentic-analytics-harness/_index]] (observability-over-scorecards at prod scale)
