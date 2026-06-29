# Original #1 — Omnilogin (the antidetect browser)

## Source

Primary: [omnilogin.net](https://www.omnilogin.net), [docs.omnilogin.net](https://docs.omnilogin.net), [pricing](https://www.omnilogin.net/pricing), Omnilogin's own comparison blog posts (vs GoLogin / Multilogin / AdsPower). Cross-checked against third-party antidetect-browser roundups (proxyway, coronium, multilogin.com). All confirmed via workflow `wf_1ac2a814-456` facet 1 (+ adversarial verify).

## What it is

**Omnilogin = an antidetect browser** — a Chromium build that runs many **isolated browser profiles**, each with its own spoofed fingerprint (User-Agent, Canvas, WebGL, WebRTC, IPv6) + cookies/localStorage/cache + proxy. The point is to manage many accounts that look like separate machines to anti-bot systems. Category peers: **Multilogin** (enterprise gold standard), **GoLogin**, **AdsPower** (9M+ users, big in Chinese e-commerce), **Dolphin Anty**, **Incogniton**.

## Who uses it (typical base)

Affiliate marketers · multi-storefront e-commerce sellers (Etsy/Amazon/Shopee/TikTok Shop) · "MMO" multi-account operators · Web3/crypto wallet teams · agencies running many client accounts · QA engineers. **This is orthogonal to the operator's recruitment-SaaS domain** — the value here is the *automation architecture*, not the antidetect use case.

## Three automation surfaces (this is the load-bearing part)

Omnilogin exposes **three parallel ways** to automate, which is the context the AI Coding feature slots into:

1. **No-code visual builder** — drag-and-drop workflow with **60+ blocks** + **45+ pre-built templates** (auto-login Gmail/Twitter/Discord, account verification, crypto-wallet creation, etc.). Vendor claims **~95% task coverage**.
2. **Code / API** — a **REST API on all tiers (including free)** plus **Puppeteer / Playwright / Selenium** SDK support and JavaScript code blocks. (So the generated "script" runs on a mature, standard automation runtime — see [ai-coding-feature](ai-coding-feature.md).)
3. **AI Coding** — natural-language → generated script (the new feature; the video's subject).

Plus **Action Sync / "Synchronizer"** — mirror one profile's clicks/inputs/navigation across an entire account group simultaneously (the "do it once, run it on hundreds" primitive).

## Data posture

**Local-first by default** — profiles live client-side, "never sent to vendor servers," with *optional* encrypted backup to Google Drive / S3 / Telegram. This is its stated differentiator vs cloud-centric rivals. (Relevant analogy for hireui: a local-first + opt-in-cloud data architecture for sensitive data — see pilot methods.)

## Pricing (confirmed against the pricing page)

| Tier | Profiles | Price |
|---|---|---|
| Free | 2 | $0 (no card) |
| — | 10 | $9/mo |
| — | 100 | ~$29/mo |
| — | 500 | $59.90/mo |
| — | 1,000 | $99/mo |
| — | 10,000 | $189/mo |

Annual billing ~40% off; team seats $5/member (1–10) or $3/member (11+). REST API on every tier including free.

## Key takeaways

- It's a **multi-account browser with an RPA layer**; the AI Coding feature is a generation front-end on top of an existing Puppeteer/Playwright/Selenium automation engine.
- The **three-surface model (no-code / code / AI)** is the interesting product design: AI Coding generates the *same kind of artifact* the visual builder and SDK produce, just from a description.
- **Action Sync** = "author once, fan out across N profiles" — conceptually the same as batch processing in any multi-tenant system.
- **Local-first + optional encrypted backup** is a defensible privacy posture worth borrowing for sensitive-data products.

## ⚠️ Verified caveats

- The **~95% coverage** and **anti-bot bypass** claims are **vendor marketing**, not independently audited.
- One verification corrected Omnilogin's own comparison: **GoLogin DOES have a permanent free plan** (3 profiles) — Omnilogin's blog implies it's trial-only. Treat vendor comparison posts skeptically.
- No public benchmark on concurrent-profile limits, memory overhead, or builder-vs-hand-coded performance.

## Cross-links

- [ai-coding-feature](ai-coding-feature.md) — the generation layer that sits on this product
- [[claude-code-clones/_index]] — OpenCode and the broader "agent generates automation" landscape
- Pilot methods: the **local-first data posture** and **three-surface automation model** are the borrowable bits for [[harness-engineering/_index]] / hireui.
