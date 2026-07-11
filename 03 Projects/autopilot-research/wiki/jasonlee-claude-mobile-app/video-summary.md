# Video Summary — Annotated Walkthrough

## Source
- `UMjeSU6C4qU`, 2026-07-09, 26:04. Timestamps from the description; annotations from the verified dives.

## 00:00–01:21 · Niche pitch
- Shows App Store receipt-scanner apps "making at least $40,000 a month": SimplyWise "doing 60k per month," another at 60k, one at 80k. **No source named** for the revenue numbers (App Store pages don't show revenue). ⚠️ Unverifiable estimates presented as fact → [[the-80k-title-and-revenue-claims]]
- The competitor shown ("Receipt Tracker" website: camera capture + AI + QuickBooks sync) could not be definitively identified; the closest App Store name-match (Beatcode Srl's Receipt Tracker, 3.6★) lacks QuickBooks integration.

## 01:21–04:05 · Why the niche works (his 3 reasons)
1. Boring niche, painful problem; 2. One problem done well (not a full accounting suite); 3. B2B stickiness ("you already have all your data inside the app"). Directionally supported by B2B SaaS retention benchmarks (~88–90% annual) but with **zero receipt-app-specific evidence**; the marquee QuickBooks integration is later deferred entirely.

## 04:05–06:16 · Planning (plan-first gate)
- Claude Desktop app → Code → new session → connect to a project folder. Model: **Opus 4.8** ("smartest or second smartest model to structure the app... hand off easier work to cheaper models").
- Notable line: "you don't need Fable 5... it's overkill and token hungry. And as of July 12th, you got to use the API pricing to use Fable 5" — **✓ CONFIRMED** (included-window extension to 2026-07-12; $10/$50 per MTok credits after).
- Prompt: build iOS receipt app "Strike Rabbit" (caption garble; later consistently "Track Rabbit") + web dashboard + QuickBooks sync; includes competitor website + App Store links for Claude to crawl; ends **"Give me the full plan. Do not build first."**
- Output: tech stack (Expo React Native / Next.js / Supabase / Claude API for vision) + feature list.

## 06:16–10:07 · Front-end in Claude Design
- Asks Claude Code to **write the Claude Design prompt** ("Don't give any design direction, just the features"), adds 3 features (budget optimizer, financial-health animation, month-filterable category breakdown).
- Attaches a Pinterest/Dribbble dashboard screenshot as style reference; runs on Opus 4.8; gets web dashboard + a "Track Rabbit iOS app" variant in one project.
- Praises the recent "massive upgrade" — the **2026-06-17 Claude Design overhaul** (manual canvas editing so simple tweaks don't burn tokens). ⚠️ Note: edit controls are on the **right** (canvas/property inspector), and the "iOS app" design is a responsive mockup, not native iOS. → [[claude-design-handoff]]
- Exports **Share → Export → zip** into the Claude Code project folder.

## 10:07–14:22 · Back-end build
- Prompt: find the design files, plan the backend, both apps share one database, "use a multi-agent workflow... smaller cheaper models like Sonnet 5 for grunt work and heavier models like Opus 4.8 for heavier work, especially reviewing the codebase... give me your plan on which agents will do which task and why." Swaps a suggested Fable 5 → Opus 4.8. ⚠️ The agent table is presentational; nothing on screen demonstrates real per-subagent model pinning. → [[multiagent-cost-tiering-reality]]
- Setup 1: **Anthropic API key** from platform.claude.com (pay-as-you-go credits, separate from the Claude subscription). Advice: have Claude save it in a `.env` "cuz if you just paste it in the chat, if the chat gets leaked, then anyone has access." ⚠️ Incomplete threat model → [[api-key-handling-in-mobile-apps]]
- Setup 2: **Supabase MCP connector** via Desktop connectors directory — "Claude can actually talk and set up databases without you having to do it manually." ⚠️ No caveats given → [[supabase-mcp-and-rls]]

## 14:22–16:50 · Sponsor (Arcads AI)
- AI UGC video ads; "latest models like Cidas 2.0 4K" (= caption garble of **Seedance 2.0**) "and the newly released Omni Flash" (= **Google's** Gemini Omni Flash, 2026-06-30 — not on Arcads' documented model list); "Arcads has just added an MCP connector to Claude Code" (connector **real**; "just added" unverifiable). → [[lottie-and-arcads-layer]]

## 16:50–20:58 · Testing + fixing
- Web preview in Claude Desktop's in-app browser pane (documented feature) + localhost:3000 in Chrome; mobile via **Expo Go QR** (the QR is Expo CLI output; same-Wi-Fi LAN requirement unstated).
- Data-sync check across both apps (same Supabase rows). Live receipt scan works (Starbucks, $7 cheesecake).
- Fix loop: screenshot the broken month-selector → annotate → AirDrop → paste to Claude → fixed; "shake your phone... hit reload" (shake opens the dev menu; Fast Refresh is normally automatic).

## 20:58–end · Lottie animations + Supabase check
- Downloads 2 free LottieFiles JSONs (processing rabbit + delete button); "it's basically a JSON file... no images or videos here" (⚠️ Lottie JSON *can* embed base64 raster images/audio); prompts Claude to wire them; works after reload.
- Shows the data in Supabase table editor; claims data will be "unique to every user that signs up... obviously, after you've set up authentication" — ⚠️ auth + RLS never built on camera.
- Outro funnels to his "7 Tiny Apps Making at Least $40,000/month" video (`ThKDUQCq50I`, 2026-06-18).

## Key Takeaways
- The demo genuinely works end-to-end **as a localhost/Expo Go prototype** — receipt photo → parsed row → synced dashboard.
- Every claim with a dollar sign or a security implication needs the caveats in [[caveats-and-corrections]].
- The transferable method is in [[workflow-plan-first-design-first]].
