# Source provenance

## The video

- **Title:** "The Ultimate Claude Code Tutorial for Mobile Apps - FULL COURSE"
- **ID / URL:** `p80OV6kjIO8` · https://www.youtube.com/watch?v=p80OV6kjIO8
- **Channel:** Codesistency (`@codesistency`, channel_id `UCiuh2rVpl8I_wZQASC6wxbg`)
- **Published:** 2026-07-04 · **Duration:** 3:33:06 · **Category:** Howto & Style
- **Stats at ingest (2026-07-14):** ~48,502 views · ~1,463 likes · 75 comments · channel ~151,000 subscribers (first-party yt-dlp metadata)
- **Chapters:** 0 Project Preview · 1 Planning & Tools Setup · 2 UI Design & Auth · 3 Webhooks & Background Jobs · 4 Native Tabs / Home / Trip Generation · 5 Sentry / Assistant / Trips · 6 Profile & Legal Pages
- **Fetch method:** yt-dlp (metadata + English auto-captions + `--write-info-json` + `--write-description`). No block/challenge encountered. Cleaned transcript archived at `../../raw/2026-07-14-codesistency-mobile-course-transcript.txt`.

## The presenter

- **Name:** Burak (GitHub `burakorkmez`, X `@codesistency`). CONFIRMED.
- Full-stack developer (React/Next/Node/Python/Go); the channel was **rebranded from "As a Programmer" to "Codesistency."** ~40 videos, several million total views.

## Business framing (mostly self-report)

- **BulkyAI** — a calorie-tracker app he says he built and shipped to the App Store in **14 days**, first paying customer **5 days** after launch, subscriptions in **RevenueCat**. **UNVERIFIABLE**: no App Store listing found under the exact name "BulkyAI" (other similarly-named apps exist but aren't attributable to him). A **`bulkyai.app`** website exists but surfaces only legal/ToS pages — which is *consistent with* the exact "deploy legal pages to Cloudflare" workflow he teaches, though not proof of a shipped app.
- **Skool community** — a paid community ("build your app in 2 weeks with us"). **CONFIRMED** via the description's explicit "Our Skool Community" link. (A public checker also shows a Discord for the channel; he may run both — see [[caveats-and-corrections]] Override 2.)
- A student is said to have shipped their own app in 14 days too — self-report, unverifiable.

## Sponsors (disclosed, all genuinely used in the build)

From the description, each a free-credit affiliate link: **Sentry** ("$80 free credits"), **Inngest**, **CodeRabbit**, **Clerk**, **Neon**, **ImageKit**. CONFIRMED. Non-sponsor tools also used: Expo, OpenAI, Unsplash, ngrok, Context7 (Upstash), Cloudflare, shots.so, GPT image.

## Linked resources (in description)

Source code repo ("triply AI", stated public at publish), diagrams, and multiple prompt docs: plan-mode prompt, design prompts, extra prompts, legal-pages prompts. A separate free ~2-hour Expo/React Native crash course is linked as the prerequisite.

## Integrity assessment

Unusually clean for a sponsor-heavy tutorial: every sponsored tool is really used, the App-Store gates and webhook concepts are taught accurately, and the honest "you won't get identical results, it's AI" + "read the plan before accepting" framing is anti-hype. The only genuine technical error is the AGENTS.md-native-read claim ([[agents-md-vs-claude-md]]); the only soft spots are the unverifiable BulkyAI revenue story and minor tier/hook imprecisions. Places it near [[github-copilot-cli-agents]] and [[local-ai-coding-agents]] on the integrity spectrum, well above [[jasonlee-claude-mobile-app]].
