# Pilot methods — applying Claude Code observability (OpenTelemetry "command center") to your working flows

> **Source:** [[claude-code-observability/_index]] — Mansel Scheffel, "Claude Code + OpenTelemetry = Claude Command Center" ([dITtLiC9FzM](https://www.youtube.com/watch?v=dITtLiC9FzM)) + a double deep-dive of the originals (Claude Code [monitoring/OTel docs](https://code.claude.com/docs/en/monitoring-usage), the [OpenTelemetry standard](https://opentelemetry.io/docs/), the Grafana/Prometheus/Loki backend stack, JSONL logs + `/cost`/`/usage`/`/stats`, [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp), Telegram HITL). Adversarially verified (Workflow `wf_5398ccab-88a`). Provenance + the over-correction caught: [[claude-code-observability/source-provenance]].
> **Date:** 2026-06-20.
> **Your working flows:** (C) your **personal `~/.claude` Claude Code harness** — you pay for Claude and run it daily (this very session); (A) the **autopilot-research knowledge pipeline** (this vault); (B) **hireui** — TalentAxis recruitment SaaS, your **Goal #2** build target (no LLM in product yet → build-it-right); (D) **Scrum coaching / team practice**.
> **18 methods, ranked.** Each grounded in a verified fact (or flagged), with a concrete first step + a success signal.
>
> **The headline:** unlike most of this video, the value here is *immediately yours* — you already generate the data. **You can see your real Claude Code token/cache/cost spend in ~2 minutes with zero setup (C1), and stand up a live cache-hit/MCP/cost dashboard in ~90 minutes (C3).** That dashboard is literally the *measurement layer* for your [[claude-api-cost-optimization/_index]] pilot — you've been optimizing cache hits without watching the gauge.

---

## ▶ Start here (recommended sequence)

1. **Today, 2 minutes, zero setup:** **C1** — run `ccusage` over your existing `~/.claude/projects/*.jsonl`. Instant token + cost-by-model + by-project report. No telemetry pipeline, works on any plan. This is the "start simple" move — you may not need OTEL at all.
2. **This week, ~90 min:** **C3** — `CLAUDE_CODE_ENABLE_TELEMETRY=1` + a local Collector→Prometheus→Grafana (e.g. the confirmed `ColeMurray/claude-code-otel` compose) → a live **cache-hit-rate + token + cost** dashboard. **C4** tags metrics by project so you can split *hireui-dev vs autopilot vs sandbox* spend.
3. **Goal-#2 track:** **B1 → B2 → B3** — capture a **dev-time cost baseline** for hireui now (so future product-LLM cost is isolatable), then bake cost/cache/code-execution levers into the LLM-feature PRD *before* building. Build-it-right, not retrofit.
4. **Ongoing:** **A1** — emit your routine's `gaps_closed_ratio` + per-topic cost as custom metrics so the autopilot pipeline becomes self-observing (the [[agentic-analytics-harness/_index]] "observability over scorecards" discipline, at your scale).

---

## Ranked table

| # | Method | Flow | Effort | Value | Why it ranks here |
|---|---|---|---|---|---|
| **C1** | `ccusage` on existing JSONL — zero-setup cost report | C personal | **~2 min** | **High** | Truly the fastest win; needs no telemetry; "start simple" before any dashboard |
| **C3** | `CLAUDE_CODE_ENABLE_TELEMETRY=1` → local Grafana cache/token/cost dashboard | C personal | Med (~90m) | **Very High** | The headline — *measures* your cache-hit + token levers in real time |
| **C2** | Watch cache-read : cache-creation ratio (validate the #1 lever) | C personal | Low | **High** | Turns [[claude-api-cost-optimization/_index]] from belief into a tracked gauge |
| **C4** | `OTEL_RESOURCE_ATTRIBUTES=project=…` — split cost by project | C personal | Low | High | Answers "which project burns budget?" (hireui vs autopilot vs sandbox) |
| **B1** | hireui **dev-time cost baseline** before any product LLM | B hireui | Med | **Very High** | Isolates future product-LLM cost from build cost; pure build-it-right |
| **A1** | Emit `gaps_closed_ratio` + per-run cost as custom metrics | A pipeline | Med | High | Makes the autopilot routine self-observing; ties cost to output |
| **C5** | `OTEL_LOG_TOOL_DETAILS=1` → find slow MCP tools to defer/code-exec | C personal | Med | High | Surfaces the MCP-latency the video flags → feeds [[claude-code-observability/code-execution-mcp-workaround]] |
| **B2** | Spec hireui LLM-feature cost (cache/code-exec levers) in the PRD | B hireui | High | **Very High** | Extends the existing cost spec with real telemetry; pre-build discipline |
| **B3** | hireui feature PRD with a cost/cache **SLA** baked in | B hireui | High | High | "<$0.05/call @ 80% cache" as a design constraint, not a retrofit |
| **A2** | Daily JSONL→cost rollup as a metric (cron) | A pipeline | Med | Med | Auto-tracks per-day autopilot spend without manual export |
| **C6** | Console **Analytics dashboard** (if Team/Enterprise) — no setup | C personal | Low | Med | A real native dashboard you may already have; check before self-hosting |
| **D1** | Team cost-transparency dashboard + Telegram alert | D coaching | Low | Med | Cost as a team-health metric; reuses your Telegram pilot |
| **A3** | Correlate cost with topic/phase — find expensive topics | A pipeline | Med | Med | "memory-systems cost 3× prompt-eval" → guides next-topic planning |
| **C7** | Event-driven failure alert → Telegram (not a polling dashboard) | C personal | Low | Med | The video's best ops idea: get pinged on failure, don't babysit |
| **D2** | "LLM cost governance" as a monthly retro item | D coaching | Med | Med | Builds team ownership of spend; pairs with D1 |
| **A4** | A short `observability-and-cost-discipline` wiki page | A pipeline | Med | Low | Documents the setup so it compounds / is forkable |
| **B4** | hireui: feed prod LLM traces into eval triage (future) | B hireui | High | Med | Omni's daily trace-triage; only once hireui has LLM features |
| **A5** | Reconcile/observe the routine drain itself (loop-log = choke point) | A pipeline | Low | Med | Your loop-log already *is* the observability choke point |

---

## C — Your personal `~/.claude` Claude Code harness (the biggest, most-immediate surface)

> You pay for Claude and run Claude Code every day. Every fact here is *already true of your machine* — you just aren't looking at it yet. This is where this video pays off fastest.

### C1 — `ccusage` on your existing JSONL — zero-setup cost report ★
- **Verified:** Claude Code already writes every session to `~/.claude/projects/<encoded-cwd>/<uuid>.jsonl` with token usage (input/output/cache_read/cache_creation) per turn. `ryoppippi/ccusage` (confirmed real) parses it. **No telemetry pipeline, works on any plan.**
- **First step:** `npx ccusage@latest` (or `bunx ccusage`) → then `ccusage --daily` and `ccusage --breakdown` for by-model/by-project. (⚠️ run [npm-security-check] first — it's an `npx` of a third-party package.)
- **Success signal:** you see your real token + cost split by model and project for the last 30 days — and probably spot one surprise (a heavy skill/topic). This alone may answer "where do my tokens go?" without OTEL.
- **Why first:** it's the "would a single simple thing do?" gate. Don't build a dashboard until you've looked at the free report.

### C3 — Turn on OpenTelemetry → a live local cache/token/cost dashboard ★
- **Verified:** `CLAUDE_CODE_ENABLE_TELEMETRY=1` (opt-in) + an OTLP exporter emits `claude_code.token.usage` (with cacheRead/cacheCreation + model), `claude_code.cost.usage` (incl. `skill.name`), tool latency/error events, etc. There is **no built-in OTEL dashboard** — you point it at your own backend.
- **First step:** clone the confirmed **`ColeMurray/claude-code-otel`** docker-compose (Collector + Prometheus + Grafana), then set `CLAUDE_CODE_ENABLE_TELEMETRY=1` + `OTEL_METRICS_EXPORTER=otlp` + `OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317` in `~/.claude/settings.json`. (⚠️ [install-snapshot] + [npm-security-check]/docker review first.)
- **Success signal:** a Grafana panel shows cache-hit-rate %, token-by-model, and cost growing live as you work.
- **Caveat:** the video never names its backend; you're choosing one. Self-host = free + private (right for dev telemetry); managed (Grafana Cloud/Datadog) bills per metric series.

### C2 — Watch the cache-read : cache-creation ratio (validate the #1 cost lever)
- **Verified (first-party):** cached reads bill **~0.1× (≈90% off)** and don't count against rate limits; the #1 silent killer is a timestamp/volatile content high in the system prompt ([[claude-api-cost-optimization/_index]]).
- **First step:** add a Grafana panel `sum(token.usage{type="cacheRead"}) / sum(token.usage{type="cacheCreation"})` (or read it from `ccusage`). Target a healthy ratio (reads ≫ creations).
- **Success signal:** you can *see* whether your prompts are cache-friendly — and catch a regression (a new timestamp in a `CLAUDE.md` or skill tanking the ratio).
- ⚠️ The exact `type` attribute key is single-source-flagged (see provenance) — verify against your live metrics.

### C4 — Tag metrics by project (`OTEL_RESOURCE_ATTRIBUTES`)
- **Verified:** `OTEL_RESOURCE_ATTRIBUTES="project=hireui"` (comma-separated `key=value`, no spaces) tags all metrics, so you can query cost by project.
- **First step:** set it per-worktree (`project=hireui` in the hireui worktree, `project=autopilot-research` in the vault). Add a Grafana "cost by project" panel.
- **Success signal:** you can answer "hireui-dev cost $X/week vs autopilot $Y/week" — the input to C1's budget decisions and B1's baseline.

### C5 — Find slow/failing MCP tools → defer or code-execute them
- **Verified:** `OTEL_LOG_TOOL_DETAILS=1` logs tool names + `tool_result` carries `duration_ms` + `success`. MCP is token-hungry (all schemas loaded up front + every result through context); the fix is code-execution / tool-search `defer_loading` ([[claude-code-observability/code-execution-mcp-workaround]]).
- **First step:** after a week, query tool_result events for `duration_ms > 500` or `success=false`; list the top offenders.
- **Success signal:** you identify 2–3 heavy MCP tools and either drop them, `defer_loading` them, or move them behind code-execution — and the token/latency panels drop.
- ⚠️ Don't enable `OTEL_LOG_RAW_API_BODIES` — it exports full conversation history (PII). Tool-detail + metrics are enough.

### C6 — Check the native Console **Analytics dashboard** (if you're on Team/Enterprise)
- **Verified:** a real first-party usage/spend Analytics dashboard exists for **Team/Enterprise** admins (per-user activity + spend, ~1-day delay). Plus native `/cost`, `/usage`, `/stats` in-CLI.
- **First step:** run `/usage` and `/cost` in your next session; if on Team/Enterprise, open the Console Analytics page.
- **Success signal:** you've checked whether a native view already covers your need before building anything. (Often it does for "how much am I spending?")

### C7 — Event-driven failure alert → Telegram (don't babysit a dashboard)
- **Verified pattern:** the video's sharpest ops idea — get *pinged* on failure rather than watching a screen. Your Telegram stack ([[telegram-remote-control-stack/_index]], Recipe A pilot-verified) + a Grafana/Prometheus alert rule does this.
- **First step:** one alert — `claude_code` error-rate or weekly cost over a threshold → Telegram (you already have the Telegram MCP wired this session).
- **Success signal:** a real alert fires once on a real anomaly; you never sat and stared at a dashboard.

---

## A — Autopilot-research knowledge pipeline (this vault)

> Your routine already computes `gaps_closed_ratio` per run and writes a loop-log — that *is* an observability choke point. These make it self-measuring.

### A1 — Emit `gaps_closed_ratio` + per-run cost as custom metrics
- **Apply:** in the routine's Phase 5/7, emit `autopilot_research.gaps_closed_ratio` + `autopilot_research.run_cost` (with `topic` attribute) to the same OTEL/Prometheus from C3.
- **First step:** add the emission at the gaps_closed_ratio calc point; graph it over the last N runs.
- **Success signal:** a chart of ratio + cost per run/topic — you can answer "did this compile underperform, and what did it cost?" from the trace, not by re-running. This is the [[agentic-analytics-harness/_index]] "observability over scorecards" lesson at your scale.

### A2 — Daily JSONL → cost rollup (cron)
- **Apply:** a ~20-line script reads the vault's `~/.claude/projects/<autopilot>/*.jsonl`, sums tokens × model price, emits a daily metric (or just appends to a CSV).
- **First step:** write it in `bin/`, schedule it; verify the daily number appears.
- **Success signal:** a per-day autopilot spend line you can correlate with loop-logs.

### A3 — Correlate cost with topic/phase
- **Apply:** with A1's `topic` attribute, find which topics are expensive (long context, many agents). 
- **Success signal:** "memory-systems cost 3× prompt-eval" → you right-size the next drain (fewer agents / web searches). Pairs with the "scale effort to complexity" discipline.

### A4 — A short `observability-and-cost-discipline.md` wiki page
- **Apply:** after C3/A1 run for a week, document the setup (env vars, emission point, rollup) so it compounds + is forkable.
- **Success signal:** a future session can stand up the same observability in minutes.

### A5 — Treat the loop-log as the formal observability choke point
- **Apply:** add a `## Cost & coverage` block to the loop-log template (tokens, cache ratio, gaps_closed_ratio) — the cheapest version of all the above, no pipeline.
- **Success signal:** every loop-log carries its own cost + coverage line.

---

## B — hireui (Goal #2, the real build target)

> hireui has **no LLM in product yet** (verified 2026-06-15) — so these are build-it-right specs, same posture as the existing `claude-api-cost-optimization-spec` + `prompt-evaluation` specs in `hireui/_bmad-output/`. But you *build* hireui **with** Claude Code, so dev-time telemetry applies **now**. Follow hireui's CONSTITUTION (I-2 branch policy, I-8 skill registry) + BMAD harness.

### B1 — Capture a hireui **dev-time cost baseline** now ★
- **Why:** the cost of *building* hireui with Claude Code is separate from the future cost of hireui *using* Claude to serve users. Measure the build baseline now (with C3+C4's `project=hireui` tag) so you can isolate product cost later.
- **First step:** enable telemetry in the hireui worktree, run a normal week of dev, then write `hireui/_bmad-output/runbooks/dev-time-cost-baseline-2026-06-20.md` (cost/session, cache ratio, dominant model).
- **Success signal:** a documented "$X/dev-session at Y% cache" control measurement.

### B2 — Spec the LLM-feature cost *before* building (extend the existing spec)
- **Why:** you already have `hireui/_bmad-output/runbooks/claude-api-cost-optimization-spec-2026-06-15.md`. Add a "Cost from telemetry (June 2026)" section using B1's baseline + the code-execution savings + the cache levers, and model per-feature cost.
- **First step:** open that spec; add the telemetry section; estimate "recruiter-agent = N calls × $/call".
- **Success signal:** future-feature cost is grounded in observed metrics, not guesses — leadership can decide "is $/screen acceptable?" before a line of feature code.

### B3 — Bake a cost/cache **SLA** into the feature PRD
- **Why:** "Recruiter Agent must stay <$0.05/call @ ≥80% cache, using code-execution for tool calls" as a *design constraint*, not a retrofit.
- **First step:** in `hireui/_bmad-output/FEATURES.md`, add the draft feature with explicit cost SLA + cache target + token budget. Cross-refs the [[multi-agent-orchestration/_index]] job-screener thread (B6/B7/B10 there).
- **Success signal:** the team discusses "how do we hit $0.05?" before coding.

### B4 — (Future) feed prod LLM traces into eval triage
- **Why:** once hireui has LLM features, Omni's daily trace-driven session triage + LLM-as-judge ([[prompt-evaluation/_index]]) is how you keep quality + cost honest in production.
- **First step:** defer until B1–B3 ship; then spec a daily trace-triage runbook.
- **Success signal:** a documented "observe prod, triage failures daily" loop in the hireui harness.

---

## D — Scrum coaching / team practice

### D1 — Cost-transparency dashboard + Telegram alert (not surveillance)
- **Apply:** a read-only Grafana link + one Telegram alert ("Claude Code spend this sprint > $X") frames LLM cost like infra/CI cost — a team-health metric.
- **First step:** set the alert from a 2-week baseline; share the read-only link; 30-min "here's where our spend goes" standup.
- **Success signal:** the team asks "why was spend high this sprint?" — visibility is working.

### D2 — "LLM cost governance" as a monthly retro item
- **Apply:** teams track infra cost but rarely LLM cost. A 2-min retro item ("what drove cost? what worked?") builds collective ownership.
- **First step:** propose it next retro; frame as efficiency, not blame.
- **Success signal:** one concrete action emerges (e.g. "cache our prompt templates", "file an issue on slow MCP X").

---

## ✋ Skip-list (what NOT to do — the video itself argues some of this)

- **Don't build the elaborate "mission control" agent dashboard.** The creator's own thesis: it's context bloat. Observability ≠ a named-agent orchestration UI. Resist it.
- **Don't expect a built-in OTEL dashboard.** There isn't one. (And don't trust the earlier-draft over-correction that said `/cost`/`/usage` don't exist — they *do*; they're just local/account-fed, not OTEL.) Native views + an external backend, that's the model.
- **Don't enable `OTEL_LOG_RAW_API_BODIES` / full-content logging** for cost work — it exports full conversation history (PII + bloat). Metrics + tool-detail are enough.
- **Don't chase the creator's gated prompt.** "Build your own" is behind a Google Drive folder + a paid Skool community; you don't need it — C1/C3 above + `ColeMurray/claude-code-otel` get you there in the open.
- **Don't build per-team chargeback in hireui yet.** Premature — baseline dev cost (B1), then product cost (B2), *then* consider chargeback.

---

## A skeptic's reframe

The genuinely first-party, durable lessons here are small and you can act on them this week: **(1) you already have the data** (JSONL + OTEL) — `ccusage` shows it in 2 minutes; **(2) cache hit rate is the gauge for the cost lever you're already pulling**; **(3) get alerted on failure instead of watching a dashboard**; **(4) schedule predictable work + assign the cheap model per task instead of building autonomous-agent theater.** Everything beyond that — the custom UI, the "IQ agent", the paywalled prompt — is the creator's unverifiable build. Take the four; skip the theater.

## Cross-links

- [[claude-code-observability/_index]] (source topic) · [[claude-code-observability/video-to-original-crosswalk]] · [[claude-code-observability/source-provenance]] (verified vs flagged).
- Composes with: [[claude-api-cost-optimization/_index]] (the levers this *measures*) · [[agentic-analytics-harness/_index]] (observability-over-scorecards) · [[telegram-remote-control-stack/_index]] (C7/D1 alerts — already piloted) · [[prompt-evaluation/_index]] (B4 trace triage) · [[agent-dashboard-os/_index]] (the abstract landscape this concretizes) · [[multi-agent-orchestration/_index]] (B3 job-screener) · [[claude-code-hooks/_index]] (deterministic complement).

## Suggested next action

Do **C1 right now** — `npx ccusage@latest --daily` (after a quick [npm-security-check]) — and look at where your tokens actually go; it's 2 minutes and might be all you need. If the picture warrants live tracking, do **C3 this week** (the `ColeMurray/claude-code-otel` compose + one env var) so your **cache-hit-rate gauge** goes live — it's the missing measurement layer for your cost-optimization pilot. Then open the **hireui Goal-#2 track with B1** (dev-time cost baseline). Tell me which and I'll scaffold it — the C3 local stack + `~/.claude/settings.json` env block, or the B1 baseline runbook into `hireui/_bmad-output/`.
