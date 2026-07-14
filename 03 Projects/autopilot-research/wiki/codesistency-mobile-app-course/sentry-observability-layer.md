# The Sentry observability layer

One of the course's stronger conceptual segments: *why* a solo builder needs error monitoring, then the concrete features. All verified real (see [[claims-scorecard]]); the only nuance is the maturity status of AI-agent monitoring.

## The "why" (the presenter's best argument)

> "When your users face an error, do you think they'll email you the problem — or delete the app and leave a one-star review? 99% of the time they delete and leave one star." *"App doesn't work"* — but which feature? You have no idea.

So Sentry is *"your app's watchtower."* The pitch is sound and generalizes to any shipped product.

## Features shown (all verified)

- **React Native SDK + setup wizard.** `@sentry/react-native` + `npx @sentry/wizard@latest -i reactNative` (auto-configures metro/Gradle/Xcode + source-map upload). Needs a Sentry **auth token** in `.env`.
- **Sentry Logs** — structured, searchable, cloud-persisted logs, vs ephemeral `console.log`. Six severity methods: `trace / debug / info / warn / error / fatal`, plus an `fmt` template formatter (both confirmed). GA since Sept 2025. 5 GB/mo free.
- **Tracing** — `Sentry.startSpan()` for performance/latency/throughput. Real.
- **Session Replay** — `Sentry.mobileReplayIntegration()` with `maskAllText` / `maskAllImages` / `maskAllVectors` (all default `true` for privacy; he sets them `false` in the demo to see content). A video of what the user saw when it broke.
  - **Nuance:** body capture is XHR-only (fetch unsupported), auth-like headers are always stripped, and masking doesn't apply on Android Canvas rendering. Scope limits the tutorial doesn't mention.
- **AI Agent Monitoring / LLM calls dashboard** — tracks per-call token usage, latency, tool usage, cost, and error rates, connected to the rest of your Sentry data. He wires it into the assistant screen and inspects the LLM call breakdown.
  - **Status nuance:** the feature is **real and works**, but verification suggests it is still **Open Beta** (not fully GA) as of July 2026, and on React Native it needs **manual instrumentation** (Node require-hooks aren't available on Hermes/JSC). So "just turn it on" undersells the RN effort.

## The privacy angle (important for the operator)

Session Replay records what the user saw; the default masking (text/images/vectors) exists precisely because a naive setup can capture PII on screen. The presenter turns masking **off** for the demo — reasonable for a throwaway tutorial app, **dangerous for a recruitment product** where the screen shows candidate data. For hireui this connects to the data-residency/PII discipline established in [[local-ai-coding-agents]] and [[google-ai-studio-github-import]]: **keep masking on**, allowlist replay/network capture narrowly, and treat AI-agent-monitoring inputs/outputs as PII-bearing.

## "Companies that use Sentry" — partially verified

The video shows a logo wall (GitHub, Vercel, Supabase, Convex, Cursor). Verification: **Cursor, Supabase, and GitHub** are confirmable Sentry customers (published case studies / references); **Vercel** is a partnership/integration with weaker customer evidence; **Convex** appears only as a technical integration. Minor marketing overreach, not fabrication — verdict CORRECT-BUT-INCOMPLETE.

## Operator relevance

Sentry's AI-agent monitoring + Logs is a concrete answer to the observability layer discussed in [[claude-code-observability]] — but for the *product's* LLM calls, not the coding agent's. If hireui ships an LLM feature, this is a ready-made way to watch token/cost/latency in production, complementing the OTel-for-the-agent approach in that topic.
