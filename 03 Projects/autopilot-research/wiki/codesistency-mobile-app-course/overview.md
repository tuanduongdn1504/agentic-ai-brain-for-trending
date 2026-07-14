# Overview — What the course is and what gets built

Source: `p80OV6kjIO8` (Codesistency, 2026-07-04). See [[_index]].

## What it is

A single 3h33m video framed as a "FULL COURSE." The pitch, stated up front: *"We are not building some random demo application that looks good for 5 minutes."* It builds a real, phone-installable AI product end to end and — critically — teaches a **repeatable workflow** (see [[the-anti-vibe-workflow]]) rather than a one-off app. The presenter repeats that the goal is *"understanding the workflow to build actual apps,"* not reproducing his exact UI.

Explicitly **not** a vibe-coding tutorial: *"we are not going to randomly ask AI something like 'build me a mobile app and don't make any mistakes.'"* This positions it alongside [[hoidanit-fullstack-vibe-coding]] and [[system-thinking-ai-coding]] as anti-vibe discipline, and against the looser [[jasonlee-claude-mobile-app]].

## What gets built — "Triply" (AI trip planner)

iOS-first React Native/Expo app:

- **Auth:** sign in with Google or Apple (Clerk). Email intentionally skipped for V1.
- **Trip generation:** enter destination, dates, budget tier, travelers, interests, travel pace → OpenAI builds the trip **in the background** (Inngest job) → app polls the DB for status → redirect to trip detail.
- **Trip detail:** day-by-day itinerary, places/activities, budget breakdown, hotel suggestions, interactive **Apple map** (no API key on iOS), Unsplash cover image (or a custom uploaded one, optimized by ImageKit).
- **AI assistant tab:** streamed chat to modify a trip ("make it more relaxed," "add local food," "lower the budget") + general travel Q&A. Messages persisted; clearable.
- **Four native tabs:** home / assistant / trips / profile — with the iOS 26 "liquid glass" effect via Expo **native tabs**.
- **Profile:** account details, logout, **delete account** (full DB cleanup — an App Store requirement), rate-app button.
- **Web landing page + legal pages:** privacy policy, terms of service, support page — built in the same repo (plain HTML/CSS) and deployed to **Cloudflare Workers** via Wrangler.

## Who it's for

Beginners-to-intermediate who already know a little React Native (he links a separate free 2-hour Expo crash course) and want the *process* of shipping a real AI app. Node.js is the only stated prerequisite. He recommends spending ≥$20/mo on one AI coding tool (names Claude Code as his choice; Cursor/Codex/Windsurf/Gemini as substitutes; Codex's cheaper tier as a budget option).

## Tone / framing

Motivational ("don't be depressed about AI, just learn to build"), with recurring "ship it and make money" energy backed by his self-reported app **BulkyAI** (a calorie tracker; see [[source-provenance]]). Ends on a "shameless plug" for his paid community. The sponsor stack (Sentry, Inngest, CodeRabbit, Clerk, Neon, ImageKit) is disclosed via free-credit affiliate links, and each tool is genuinely used in the build — not name-dropped.

## Why it's worth a wiki entry

- It's the most **complete production stack** of any mobile-app tutorial in the corpus (auth + DB + ORM + background jobs + image CDN + error monitoring + AI code review), all wired to Claude Code.
- The **screenshot-verify-loop** ([[screenshot-verify-loop]]) is a concrete, portable technique.
- It surfaces the **AGENTS.md/CLAUDE.md** reality ([[agents-md-vs-claude-md]]) and real **App Store gates** ([[app-store-readiness]]) that beginners routinely miss.
