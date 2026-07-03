# Stack facts + sponsor structure

## Source

- Workflow wf_5993da5f-31c dimensions stack-claims / stream-platform / monetization-and-bias (each with independent skeptic); primary fetches of clerk.com/pricing, posthog docs, coderabbit.ai/pricing, nativewind.dev, jsm.dev redirects.

## Verified stack facts

- **Clerk**: free Hobby plan = **50,000 Monthly Retained Users** per app (confirmed at clerk.com/pricing); MRU counts only users returning ≥24h after signup — more favorable counting than MAU. Clerk Billing exists as claimed. "Most generous free plan I've ever seen" = sponsor superlative: **tied** at 50K with Supabase/Firebase (Auth0 = 25K), though MRU-vs-MAU counting arguably edges it.
- **Stream**: real free paths exist but gated — **Maker plan** (free for <5 team, <$10K/mo revenue: Chat 2K MAU, Video ~333K participant-minutes) + trial credits. RN Video SDK `@stream-io/video-react-native-sdk` confirmed on npm. Physical-device recommendation for WebRTC mic testing is real (simulator mic is famously unreliable; the video hits exactly this and switches to a wired iPhone).
- **PostHog**: `npx @posthog/wizard` is real — an **agentic setup CLI** (PostHog/wizard) that analyzes the codebase and wires the SDK; it also installed a skill into `.claude/skills/` ([[skills-supply-chain-second-observation]]). Nuance: it auto-instruments standard capture; **custom events still need manual `posthog.capture()`** (the video does add manual events later: language_selected, lesson_started, funnels). A PostHog MCP for querying analytics from the agent is mentioned in-video; not independently verified this run.
- **CodeRabbit**: free tier exists (unlimited repos; PR summaries; quotas unspecified). Video's "over 3 million repos checked" — verifiable public figure is **2M+ connected repos** ~2026; treat 3M as marketing. Its real catch in this build is what matters: [[verification-and-review]].
- **NativeWind**: v5 used in **pre-release** (`5.0.0-preview.3`); `react-native-css` is a peer dep on all platforms (not iOS-only as the build section implies). The "doesn't work with SafeAreaView" rule is real-but-nuanced: core-RN SafeAreaView is deprecated; use react-native-safe-area-context (className support there is partial/version-dependent) — his AGENTS.md rule is a pragmatic workaround, not documented doctrine.
- **Expo**: `npx create-expo-app@latest` + `npm run reset-project` (a generated template script, not a documented CLI command) both real.
- **Zustand + AsyncStorage**: standard persistence pattern. ⚠️ "Many companies like WhatsApp use AsyncStorage" — implausible (WhatsApp is a native app); treat as filler.
- Reported-only: "OpenAI Codex Go plan $8/mo" (mentioned as budget option); "Xcode adding agentic coding via Codex + Claude" (mentioned in passing).

## Sponsor / monetization structure (mirrors [[jsm-six-file-context/_index|the sister topic]])

- **5 tracked partner links** confirmed by redirect resolution: jsm.dev/lingua-stream → getstream.io?utm_campaign=jsmasteryq2; lingua-clerk → go.clerk.com partner link; lingua-posthog → posthog.com/jsmastery; lingua-vision → getstream.io/vision-agents; lingua-coderabbit → coderabbit partner URL. No explicit affiliate disclosure verified in-description.
- Sponsor-integrated curriculum: Stream+Vision Agents get the largest share of runtime (agents estimated ~28% / ~54% total sponsor-touching sections — estimates, not exact).
- **Funnel**: free "Practical Vibe Coding playbook" (jsm.dev/lingua-ebook → jsmastery.com/waitlist/practical-vibe-coding-mobile, **email-gated lead magnet**) → AI-course waitlist (real, "working on it for more than a year") → JS Mastery Pro **$48/mo** (regional pricing exists, e.g. VN ~$36/mo). Video kit (code/assets/prompts) also gated; the repo itself is public and contains the prompts' design PNGs.
- Weighting rule for this wiki: **workflow claims = high credibility** (stack-agnostic, demonstrated); **service superlatives = discount** ("most generous", "most developer-friendly", "exactly what we needed" — all sponsor-shaded; alternatives like Twilio never evaluated).

## Key Takeaways

- The stack facts mostly check out; the superlatives don't survive comparison shopping.
- Clerk 50K MRU is genuinely strong; Stream's free path has eligibility gates the video doesn't mention.
- The PostHog wizard is the most interesting sponsor tech: agentic setup CLI + skill injection.
- Same JSM monetization pattern as the six-file video: sponsor-integrated curriculum + tracked links + email-gated playbook + subscription funnel. Knowledge real, packaging commercial.
