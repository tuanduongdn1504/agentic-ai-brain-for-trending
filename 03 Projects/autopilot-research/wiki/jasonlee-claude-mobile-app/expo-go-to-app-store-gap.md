# From Expo Go Demo to App Store Product — The Gap the Video Skips

## Verdict on the preview claims
"In-app browser preview + QR code opens the app in Expo Go; shake and reload" → **CORRECT-BUT-INCOMPLETE** (high confidence).

## The preview mechanics, corrected
- **Claude Desktop browser pane is real**: "When you run your dev server in the desktop, your app opens in the Browser pane to verify its changes" (code.claude.com/docs/en/desktop-quickstart). The localhost:3000 web preview is a documented feature, not editing magic.
- **The QR code is Expo's, not Claude's**: `npx expo start` (Metro dev server) prints an `exp://` URL as a QR; Claude Code merely renders that terminal output. Scanning it in the iPhone camera opens the project in **Expo Go**.
- **Unstated constraint**: Expo Go connects to the dev server over **LAN — phone and computer must share a Wi-Fi network** (or use tunnel mode). Viewers on hotel/office networks will hit this immediately.
- **"Shake and reload"**: shake opens the **dev menu**; updates normally arrive via automatic Fast Refresh — manual reload is the fallback, not the mechanism.
- Expo's own positioning: **"Expo Go is a playground for students and learners to try Expo quickly"** — the production path is a development build of your own app.

## Everything between this demo and a shippable product

| Layer | What's actually required | Video status |
|---|---|---|
| Authentication | Supabase Auth + session handling in both apps | "obviously, after you've set up authentication" — skipped |
| Data isolation | RLS policies per table ([[supabase-mcp-and-rls]]) | never shown |
| Secrets | server-side key proxy ([[api-key-handling-in-mobile-apps]]) | never architected |
| Native build | EAS Build (or local prebuild) — Expo Go can't ship; custom native modules need dev builds | not mentioned |
| Apple gate | Apple Developer Program **$99/yr**, certificates, provisioning | not mentioned |
| Monetization | StoreKit / RevenueCat subscriptions — **in-app purchases cannot be tested in Expo Go**; the entire "$80K/mo" mechanism is absent from the demo | not mentioned |
| App Review | Apple review incl. **Guideline 4.3 (spam/clones)** — a minimal clone of an existing receipt-scanner niche is exactly the profile 4.3 targets; differentiation is a review-survival requirement, not a nice-to-have | not mentioned |
| QuickBooks sync | Intuit developer account, OAuth 2.0 (60-min tokens, refresh rotation), **mandatory App Assessment Questionnaire** for production keys (security review; officially ~15 business days, realistically 2 weeks–2+ months), 500 req/min/realm limits | "we're not going to do this today" |
| Privacy/compliance | privacy policy, App Privacy labels, GDPR/CCPA posture for financial documents, data retention | not mentioned |
| Operations | error handling, retries, rate limiting, monitoring, support | not mentioned |
| Distribution | ASO, ads, UGC creative (the sponsor's actual role) — cloning gets you a product, not customers | outsourced to the sponsor segment |

- Also unstated: Supabase free-tier projects **pause after 1 week of inactivity** — the demo backend self-destructs on that timeline.

## Fair reading
The video never *claims* to ship — the deferrals are visible to an attentive viewer ("we're not going to do this today," "after you've set up authentication"). The misleading part is the arithmetic implied by title + niche pitch + demo: the demo covers perhaps the first 20% of the work and 0% of the revenue mechanism. The corpus' deploy-layer complement is [[external|Storm Bear: fullstack-docker-cicd]]; the demo→production checklist is [[external|Storm Bear: ai-engineering]].

## Key Takeaways
- Expo Go preview ≈ localhost for your phone. Shipping = EAS Build + Apple Developer + review + IAP — a different project.
- The QuickBooks integration — the niche's stickiness anchor — is itself a multi-week compliance project (real OAuth + Intuit security assessment).
- Budget reality for a real attempt: $99/yr Apple + ~$25/mo Supabase Pro (to avoid pausing) + API costs (trivial, [[receipt-scanning-with-claude-vision]]) + the actual cost: weeks of auth/RLS/payments/review work and a differentiation story for Guideline 4.3.

## Sources
- https://code.claude.com/docs/en/desktop-quickstart · https://docs.expo.dev/tutorial/create-your-first-app/ · https://docs.expo.dev/get-started/set-up-your-environment/ · https://reactnative.dev/docs/debugging · https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/faq · https://docs.codat.io/integrations/accounting/quickbooksonline/qbo-app-assessment-questionnaire · https://satvasolutions.com/blog/intuit-app-store-approval-timeline-developer-guide · https://supabase.com/pricing
