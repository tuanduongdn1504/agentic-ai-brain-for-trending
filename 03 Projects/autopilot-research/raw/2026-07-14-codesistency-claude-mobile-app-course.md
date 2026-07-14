# (C) Raw Analysis — Codesistency "Ultimate Claude Code Tutorial for Mobile Apps" (FULL COURSE)

> **Ingested:** 2026-07-14 (ad-hoc main-loop path; queue was empty)
> **Source video:** https://www.youtube.com/watch?v=p80OV6kjIO8
> **Channel:** Codesistency (@codesistency, 151K subs) · **Category:** Howto & Style
> **Published:** 2026-07-04 · **Duration:** 3:33:06 · **Views (at ingest):** ~48.5K · **Likes:** ~1.46K
> **Transcript:** `raw/2026-07-14-codesistency-mobile-course-transcript.txt` (auto-captions, cleaned/deduped, 5,270 lines / ~36K words)
> **Fetch method:** yt-dlp (metadata + en auto-subs + info.json). No block encountered.
> **Verification:** claims cross-checked by workflow `wf_46c5932a-849` (refute-first). Scorecard lives in `wiki/codesistency-mobile-app-course/caveats-and-corrections.md`.

---

## One-line

A 3.5-hour, explicitly **anti-vibe** hands-on course that builds and (nearly) ships a real AI trip-planner mobile app ("Triply") with Claude Code driving a full production tool stack, using a repeatable **plan → design → build-with-verify-loop → AI-review → PR/merge** workflow.

## What gets built ("Triply")

AI trip planner (iOS-first). User signs in (Google/Apple) → generates a trip (destination, dates, budget tier, travelers, interests, pace) → OpenAI builds a day-by-day itinerary (places, activities, budget breakdown, hotel suggestions, interactive Apple map) in the background → trip detail screen → AI assistant chat to modify the trip. Four native tabs (home / assistant / trips / profile), profile with logout + **delete account** (full DB cleanup), rate-app button, plus a web landing page with privacy policy / terms / support.

## Tech stack (all pitched as free-to-start; all are video sponsors except Expo/OpenAI/Unsplash/Cloudflare)

| Layer | Tool |
|---|---|
| Framework | React Native + **Expo** (SDK 56 at recording), **NativeWind v4** (Tailwind for RN) |
| AI agent | **Claude Code** (default model stated as **Opus 4.8**); also names Cursor/Codex/Windsurf/Gemini as substitutes |
| Auth | **Clerk** (Google + Apple via `useSSO`; free plan capped social providers) |
| DB | **Neon** serverless Postgres + **Drizzle** ORM |
| Background jobs | **Inngest** (dev server; user-sync jobs; **experiments** for model A/B) |
| Images | **ImageKit** (optimize/transform); **Unsplash** API (trip cover images, requires attribution) |
| Observability | **Sentry** (wizard, logs, tracing, session/mobile replay, **AI agent monitoring**) |
| Code review | **CodeRabbit** (auto PR review, summary+walkthrough, VS Code extension) |
| Docs-to-agent | **Context7** (Upstash MCP, "use context7" for up-to-date docs) |
| Webhook tunneling | **ngrok** (free static domain for Clerk→API webhook) |
| Legal-pages deploy | **Cloudflare Workers** via **Wrangler** |
| Mockups / compression | **shots.so** (device frames), **FFmpeg** (image compression) |

## The workflow (the actual product of the course)

1. **Plan first (never code first).** Paste a "senior technical co-founder / product architect" prompt in Claude **Plan Mode**; it *interviews* you (multi-round Q&A) to remove guesswork, then writes a full spec. Read the whole plan before accepting; push back on risky items (he rejects EAS-hosting-at-start in favor of Inngest dev server). Save the phased plan to an uppercase `PLAN.md` as a living to-do list, marked complete as features land.
2. **Design via image models.** Generate each screen + a design system with GPT image (project-agnostic prompts linked in description); "upscale" each screen; drop reference images into a `design/` folder. Use "generate a grid of 9 variations" to explore, then pick one.
3. **Build feature-by-feature with a self-verify loop.** Tell Claude to implement a screen, then **take a simulator screenshot and compare it to the design image, looping until identical** (~80–90% in practice, then hand-tune). Uses Expo **dev build** (not Expo Go) because native modules need it.
4. **Manual test → AI code review.** Test the feature by hand, then open a PR; **CodeRabbit** reviews it (summary, walkthrough, sequence diagram, inline suggestions with copy-paste "prompt for AI agents"). Fix majors via Claude, commit on the same branch, then merge.
5. **Branch-per-feature git discipline.** First commit straight to main; thereafter feature branch → PR → CodeRabbit → fix-commits → merge → pull to main. Explicitly framed as "how you'd work at a real company."
6. **Loop until no features remain.**

## Cross-cutting concepts taught

- **Webhooks**: Clerk emits `user.created/updated/deleted` → API route → Inngest job upserts/deletes the user in Neon (keeps auth store and DB in sync). ngrok exposes the local endpoint to Clerk.
- **CLAUDE.md vs AGENTS.md**: build **AGENTS.md** (agent-agnostic) with tech stack + conventions + rules (e.g. "always use native tabs", "never run the app yourself"); have **CLAUDE.md** just reference AGENTS.md.
- **Skills**: install vendor skills (Clerk) → land under `.claude/skills/`; Claude follows them as "official docs."
- **Inngest experiments**: run two code paths (e.g. GPT-4o-mini 90% / bigger model 10%) against live traffic, get free metrics, dial up the winner — low-risk model A/B.
- **Sentry rationale**: users don't email bugs, they 1-star and uninstall; Sentry = the app's watchtower (errors, structured logs, tracing, session replay, AI-agent/LLM-call monitoring with token/cost/latency).
- **App Store readiness tips**: in-app **delete account** is mandatory (Apple will reject otherwise); privacy policy + terms + support page required; rate-app button; gallery-access permission string in `app.json`.

## Provenance / business framing (self-reported — see caveats)

Presenter says he shipped a calorie-tracker app **"BulkyAI"** to the App Store in **14 days**, first paying customer **5 days** post-launch, subs in **RevenueCat**; runs a paid **Skool** community ("build your app in 2 weeks with us"); a student allegedly shipped in 14 days too. Recurring "don't be depressed about AI / just learn to build" motivational framing; recommends spending ≥$20/mo on an AI tool (mentions Codex $8 tier as budget option).

## Corpus positioning (pre-verification)

- **Direct sibling:** [[jasonlee-claude-mobile-app]] — same genre (Claude Code mobile-app tutorial, plan-first + design-first). Contrast: jasonlee = revenue-titled/looser; Codesistency = disciplined, far larger production stack, explicit verify-loop + AI-review gate.
- **Workflow kin:** [[jsm-practical-vibe-coding]] (Context7 + CodeRabbit + AGENTS.md), [[mosh-ai-powered-apps]] (first-LLM-feature seam), [[ai-web-design-workflow]] (design-as-gate), [[hoidanit-fullstack-vibe-coding]] (anti-vibe VN beginner series).
- **hireui relevance:** the verify-loop, AGENTS.md conventions, CodeRabbit PR gate, delete-account/privacy discipline, and Inngest-experiments model A/B are all portable to Goal #2.
