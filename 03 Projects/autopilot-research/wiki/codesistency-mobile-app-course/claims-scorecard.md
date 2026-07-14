# Claims scorecard

All checkable claims from `p80OV6kjIO8`, verified by workflow `wf_46c5932a-849` (8 clusters × dive + refute-first, Sonnet 5) plus **3 main-loop overrides** where an agent confabulated (marked 🔧). Verification date: 2026-07-14.

**Tally: ~29 CONFIRMED · 5 CORRECT-BUT-INCOMPLETE · 2 MISLEADING · 0 FALSE · 0 FABRICATED · 2 UNVERIFIABLE.** A high-integrity course — closest in tone to [[github-copilot-cli-agents]] and [[local-ai-coding-agents]].

## Claude Code

| # | Claim | Verdict | Note |
|---|---|---|---|
| 1 | Default model is **Opus 4.8** | CORRECT-BUT-INCOMPLETE | Opus 4.8 real & default for Max/Team/Enterprise/API; defaults are **tiered by plan**, so the flat "the default is Opus 4.8" is presenter-context-specific. |
| 2 | Plan mode + auto/ask edit modes + **bypass** mode | CONFIRMED | All modes exist. Default Shift+Tab cycle is default→acceptEdits→plan; bypass needs an explicit flag (minor incompleteness). |
| 3 | Vendor **skills** install to `.claude/skills/` | CONFIRMED | Official. (`npx skills add` is a Vercel Labs third-party installer, not official Anthropic — he used copy-markdown + Clerk's own installer.) |
| 4 | **Claude Code natively reads AGENTS.md** | MISLEADING | FALSE as stated (issue #6235 open since Aug 2025). But his *setup* (CLAUDE.md → references AGENTS.md) is the correct workaround. See [[agents-md-vs-claude-md]]. |

## Expo / React Native

| # | Claim | Verdict | Note |
|---|---|---|---|
| 5 | **SDK 56** latest at recording | 🔧 CONFIRMED | SDK 56 (2026-05-21) was latest at recording; **SDK 57 shipped 2026-06-30** — presenter explicitly hedged ("if you see 57/58, follow along"). Refute agent's "FALSE" **overridden**. |
| 6 | NativeWind v5 pre-release, v4 stable | CONFIRMED | v5 docs literally say "not for production." |
| 7 | Native modules need a **dev build** (not Expo Go) | CORRECT-BUT-INCOMPLETE | True for third-party native modules; `expo-image-picker` itself runs in Expo Go for basic use. |
| 8 | **Native tabs** → iOS 26 liquid glass | CONFIRMED | Real (alpha since SDK 54+). Liquid glass is *inherited* from iOS 26 native components, not "produced" by Expo. |
| 9 | `reset-project` script clears starter files | CONFIRMED | Prompts move-vs-delete; he chose delete. His remaining `/src/app` matches the SDK 55+ template restructure. |

## Auth / DB

| # | Claim | Verdict | Note |
|---|---|---|---|
| 10 | Clerk **skills** + free plan **3 social providers** | CONFIRMED | Clerk Skills launched 2026-01-29; Hobby plan = "Up to 3" social connections. |
| 11 | Google + Apple both use **`useSSO`** hook | MISLEADING | Native Expo uses `useSignInWithGoogle` / `useSignInWithApple` (SDK v3+); `useSSO` is browser-OAuth/enterprise. |
| 12 | Clerk→DB sync via **webhooks** (created/updated/deleted) | CONFIRMED | Svix, HMAC-SHA256, eventually-consistent. |
| 13 | **Neon** free serverless Postgres | CONFIRMED | Free tier real; not production-grade. |
| 14 | **Drizzle** is a real TS ORM | CONFIRMED | ~7.4KB, 0 deps, serverless-friendly. |

## Infrastructure

| # | Claim | Verdict | Note |
|---|---|---|---|
| 15 | **Inngest** background jobs + local dev server + free | CONFIRMED | `localhost:8288`; 50K exec/mo free; self-hostable since Jan 2026. |
| 16 | **Inngest Experiments** — weighted A/B on live traffic + metrics | 🔧 CONFIRMED | Independently confirmed real (Experiments/Scoring/Defer). Refute pass died on session limit; verified in main loop. |
| 17 | **ngrok** free plan = one static domain | CONFIRMED | Persistent dev domain, webhook-usable. |
| 18 | **Context7** (Upstash) MCP for up-to-date docs | CONFIRMED | Open-source MCP; `use context7`. |

## Sentry

| # | Claim | Verdict | Note |
|---|---|---|---|
| 19 | RN SDK + setup **wizard** | CONFIRMED | `@sentry/react-native` + `@sentry/wizard`. |
| 20 | **Logs** (6 levels + `fmt`) | CONFIRMED | GA since Sept 2025; 5 GB/mo free. |
| 21 | **Tracing** + **Session Replay** (mask options) | CONFIRMED | Real; scope limits (XHR-only body, Android Canvas) unmentioned. |
| 22 | **AI Agent Monitoring** (token/latency/tool/cost) | CONFIRMED | Feature real; likely still **Open Beta**, RN needs manual instrumentation. |
| 23 | Companies use Sentry (GitHub/Vercel/Supabase/Convex/Cursor) | CORRECT-BUT-INCOMPLETE | Cursor/Supabase/GitHub confirmed; Vercel partnership; Convex only integration. |

## CodeRabbit / images / deploy

| # | Claim | Verdict | Note |
|---|---|---|---|
| 24 | **CodeRabbit** PR review (summary/walkthrough/diagram/inline + agent prompts) + free tier + VS Code ext | CORRECT-BUT-INCOMPLETE | All real; free tier rate-limited; "diagram" includes sequence diagrams in walkthroughs. |
| 25 | **ImageKit** optimize/transform/CDN/DAM + free tier | CONFIRMED | Free: 20 GB bw/mo, 3 GB DAM. |
| 26 | **Unsplash** API (access+secret key) + **mandatory attribution** | CORRECT-BUT-INCOMPLETE | Attribution mandatory ✓. Read-only search needs only Access Key/Client-ID; dashboard does show both keys (secret = user-auth). |
| 27 | **shots.so** free device mockups + transparent export | CONFIRMED | Commercial-safe, no watermark. |
| 28 | **Cloudflare Workers** + Wrangler deploy static HTML free | CONFIRMED | Workers Static Assets. |
| 29 | **FFmpeg** compresses images | CONFIRMED | True; use `-q:v`/`-qscale` for stills (CRF is a video param). |

## App Store policy

| # | Claim | Verdict | Note |
|---|---|---|---|
| 30 | **Delete account** required (Guideline **5.1.1(v)**) | CONFIRMED | Enforced since 2022-06-30. |
| 31 | Privacy policy + support page required | CONFIRMED | Privacy policy required; support contact required per Guideline 1.5. |

## Provenance

| # | Claim | Verdict | Note |
|---|---|---|---|
| 32 | Shipped **BulkyAI** (calorie tracker) in 14 days | UNVERIFIABLE | No App Store listing found under that name; `bulkyai.app` legal-pages site exists (consistent with his workflow). |
| 33 | First paying customer 5 days post-launch, subs in RevenueCat | UNVERIFIABLE | Self-report; RevenueCat is real. |
| 34 | Runs a paid **Skool** community | 🔧 CONFIRMED | Description explicitly links "Our Skool Community." Agent's "it's Discord not Skool" **overridden** (checked homepage only; may run both). |
| 35 | Sponsors = Sentry/Inngest/CodeRabbit/Clerk/Neon/ImageKit | CONFIRMED | All six appear as free-credit affiliate links in the description (read directly). |
| 36 | Channel ~**151K** subscribers | CONFIRMED | yt-dlp first-party metadata = 151,000 (third-party trackers show ~144K). |
| 37 | Presenter = **Burak** (@codesistency / burakorkmez) | CONFIRMED | Full-stack dev; channel formerly "As a Programmer." |
