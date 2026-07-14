# App Store readiness (the gates beginners miss)

A genuinely useful thread running through the course: the non-obvious requirements that get an app **rejected** by Apple, and how the presenter handles them. All verified (see [[claims-scorecard]]).

## Mandatory: in-app account deletion

> "Delete your account is not really an optional feature. If you want to deploy to the App Store, you have to have it — otherwise Apple will reject your application."

**Verified CONFIRMED.** Apple **App Store Review Guideline 5.1.1(v)** requires apps that support account creation to also offer in-app account deletion (full deletion, not just deactivation; must be easy to find; must remove associated personal data unless legally retained). **Enforced since 2022-06-30** — longstanding policy, not new. The presenter's guideline framing is accurate.

Implementation in the app: profile screen → delete-account → confirmation → deletes from Clerk → `user.deleted` webhook → Inngest job wipes the user's DB data (trips, chat messages). See [[webhooks-inngest-background-jobs]].

## Mandatory: privacy policy + support contact

The course builds a web landing page with **privacy policy, terms of service, and a support page** (with an email), framed as required to publish.

**Verified:** Apple **requires a privacy policy URL** (App Privacy Details — "Privacy Policy (Required)"), and **requires support contact information** (Review Guideline 1.5 — a support URL or in-app contact). So both the privacy-policy and support-page claims are correct. (The verify pass initially undersold the support-URL requirement; the adversarial pass corrected it — Guideline 1.5 makes it mandatory.)

## Also covered

- **Rate-app button** for App Store reviews (StoreKit review prompt).
- **Permission strings** in `app.json` — e.g. the photo-library usage description (*"Allow Triply to access your photos…"*) that iOS shows before gallery access. Required for `expo-image-picker`.
- **Development build (not Expo Go)** for shipping real apps — native modules need it. (Nuance: some Expo SDK modules like `expo-image-picker` do run in Expo Go for basic use; the general principle holds for third-party native modules. See [[caveats-and-corrections]].)

## How the legal pages ship

- Built in the **same repo** (a `legal/` folder), plain **HTML/CSS only** (he tells Claude: no external tech), reusing the app's logo/theme.
- Device mockups via **shots.so** (free, transparent export); images compressed with **FFmpeg**.
- Deployed to **Cloudflare Workers** via the **Wrangler** CLI (`wrangler deploy`) — free static-asset hosting. Verified real (Workers Static Assets).

## Operator relevance (hireui)

hireui is a web SaaS, not an App Store app, so 5.1.1(v) doesn't apply directly — but the *discipline* does: a **user-data-deletion path with downstream cleanup** (auth store + DB + any derived data) is exactly the GDPR/PDPL "right to erasure" obligation for a recruitment product holding candidate PII. The webhook-driven cascade delete here is a clean reference pattern. Privacy policy + support contact + data-deletion should be treated as launch gates for hireui too, per the residency/PII posture in [[local-ai-coding-agents]].
