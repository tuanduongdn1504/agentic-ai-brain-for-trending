# The production tool stack

The most complete production stack of any mobile-app tutorial in the corpus. Every tool below was **verified real and current** as of July 2026 (see [[claims-scorecard]]). Sponsors are marked ($). Free-tier reality noted where it bites.

| Layer | Tool | Verified status | Free-tier reality |
|---|---|---|---|
| Framework | **Expo** (SDK 56 at recording) + React Native | CONFIRMED. SDK 56 released 2026-05-21; **SDK 57 shipped 2026-06-30** (RN 0.86) — presenter hedged for it. | Open source |
| Styling | **NativeWind v4** (Tailwind for RN) | CONFIRMED. v5 is explicitly pre-release/"not for production"; v4 (~v4.2.6) is stable. | Open source |
| AI agent | **Claude Code** (default model Opus 4.8) | Opus 4.8 real; but "the default is Opus 4.8" is **tier-specific** — defaults vary by plan. See [[caveats-and-corrections]]. | Paid (≥$20/mo recommended) |
| Auth | **Clerk** ($) — Google + Apple | CONFIRMED. Free (Hobby) plan capped at **3 social connections**. Native hooks are `useSignInWithGoogle`/`useSignInWithApple`, **not** `useSSO` as stated. | 3 social providers free |
| Database | **Neon** ($) — serverless Postgres | CONFIRMED. Free tier real (0.5 GB/project, scale-to-zero); *"good for building/learning, not production."* | Free, non-prod |
| ORM | **Drizzle** | CONFIRMED. Lightweight TS ORM (~7.4KB, 0 deps), serverless-friendly; vs Prisma. | Open source |
| Background jobs | **Inngest** ($) — durable execution | CONFIRMED. Local dev server at `localhost:8288`; free tier; open-sourced/self-hostable since Jan 2026. | 50K executions/mo free |
| Model A/B | **Inngest Experiments** | CONFIRMED real (Experiments/Scoring/Defer). Weighted variant routing (90/10) + execution metrics. See [[webhooks-inngest-background-jobs]]. | In SDK v4 |
| Images | **ImageKit** ($) — optimize/transform + CDN + DAM | CONFIRMED. Free: 20 GB bandwidth/mo, 3 GB DAM. | Free, bandwidth-capped |
| Cover images | **Unsplash** API | CONFIRMED. **Attribution to photographer is mandatory.** Read-only search needs only the Access Key (Client-ID); dashboard also shows a Secret Key (for user-auth). | Free w/ attribution |
| Error/observability | **Sentry** ($) | CONFIRMED. RN SDK + wizard; Logs, Tracing, Session Replay, AI-agent monitoring (beta). See [[sentry-observability-layer]]. | 5 GB logs/mo free |
| AI code review | **CodeRabbit** ($) | CONFIRMED. Auto-reviews GitHub PRs (summary + walkthrough + sequence diagram + inline fixes with "prompt for AI agents"); VS Code extension. | Free tier (rate-limited) |
| Up-to-date docs | **Context7** (Upstash) MCP | CONFIRMED. Open-source MCP; `use context7` pulls version-specific library docs. | Free/open |
| Webhook tunneling | **ngrok** | CONFIRMED. Free plan gives one persistent dev domain usable as a webhook URL. | 1 static domain free |
| Legal-page deploy | **Cloudflare Workers** + Wrangler | CONFIRMED. Workers Static Assets deploys static HTML/CSS free. | Free static assets |
| Mockups | **shots.so** | CONFIRMED. Free device mockups (iPhone frames), transparent export, commercial-safe. | Free |
| Image compression | **FFmpeg** | CONFIRMED (can compress images; use `-q:v` for stills, not the video CRF param). | Open source |
| LLM | **OpenAI** (GPT-4o-mini default) | Real. Presenter used `mini` "everywhere" for cost; Gemini named as free alternative. | ~$5 min spend |

## The "everything is free to start" pitch — with the asterisk

The recurring claim is *"all of these tools are completely free to get started with."* Verified accurate **for building/learning**, with the operator caveats:

- **Neon** free tier is explicitly not production-grade (storage overage blocks writes; CU limits suspend compute).
- **ImageKit** free tier stops delivering media past 20 GB/mo bandwidth.
- **Clerk** free = 3 social providers only (fine here: Google + Apple).
- **Sentry / Inngest / CodeRabbit** free tiers are real but rate/volume-limited.
- **OpenAI** needs ~$5 to actually generate trips (Gemini free alternative offered).
- **Claude Code** itself is the one unavoidable paid piece (≥$20/mo recommended).

So: free to *learn the workflow*; a real launched app crosses into paid on several of these. This mirrors the honest-cost framing in [[local-ai-coding-agents]] and contrasts with the "free" theater flagged in [[jasonlee-claude-mobile-app]].

## Sponsor disclosure

Sentry, Inngest, CodeRabbit, Clerk, Neon, ImageKit are all video sponsors (free-credit affiliate links in the description). Notably, **each sponsor is genuinely used in the build** rather than name-dropped — which is why the scorecard is clean. See [[source-provenance]].
