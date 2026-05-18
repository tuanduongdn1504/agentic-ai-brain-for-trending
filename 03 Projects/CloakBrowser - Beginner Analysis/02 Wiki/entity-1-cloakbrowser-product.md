# Entity 1 — CloakBrowser as stealth-product-with-source-level-patches

> Tier: T2 Service · Archetype: anonymous-corporate-stealth-product · Velocity: HIGH-not-EXTREME (172/day for 86 days)

## What CloakBrowser IS

CloakBrowser is a modified Chromium binary bundled with Python/JS SDK wrappers, designed for browser automation in environments where standard Playwright/Puppeteer is detected and blocked by anti-bot systems (Cloudflare Turnstile, FingerprintJS, reCAPTCHA v3, ShieldSquare, etc.).

The architectural decision that defines the product:

> **C++ source-level modifications to compiled Chromium** (57 patches in v0.3.28) vs the corpus-default approach of **JavaScript injection at runtime** (playwright-stealth) or **config-flag patches** (undetected-chromedriver).

This decision makes detection-evasion harder for downstream anti-bot systems because the modifications are baked into the binary's behavior at compile time — not injected at runtime where detection systems can spot the injection mechanism.

## How CloakBrowser fits the corpus (T2 Service)

| Axis | CloakBrowser (v69) | Sibling: browser-use (v34) | Sibling: crawl4ai (v29) |
|------|-------------------|-------------------------|-------------------------|
| Tier | T2 Service | T2 Service | T2 Service |
| Primary lang | Python 53% + TS 43% | Python | Python |
| Stealth as feature | **Product axis (primary)** | Feature among many | Feature among many |
| Binary distribution | **Yes (~200MB Chromium)** | No (uses host browser) | No (uses host browser) |
| Drop-in compatibility | Playwright + Puppeteer + Selenium | LangChain ecosystem | Custom orchestration |
| License | MIT wrapper + Proprietary Binary | MIT | Apache-2.0 |
| Age at observation | 86 days | ~12 months | ~18 months |
| Stars | 14.9K (HIGH velocity) | 70K (sustained) | 58K (sustained) |
| Anti-detection differentiator | **Source-level C++ patches** | None | Some stealth tactics |

**CloakBrowser's distinguishing axis:** It is **corpus-first purpose-built-for-stealth subject** — stealth is the product, not a feature.

## Product architecture (3 layers)

```
┌──────────────────────────────────────────────────────────────┐
│ LAYER 1: SDK wrappers                                         │
│ - Python: launch / launch_async / launch_context /            │
│   launch_persistent_context (Playwright drop-in)              │
│ - JavaScript: ESM module (Playwright) + sub-module            │
│   (Puppeteer)                                                  │
│ - CLI: cloakbrowser install/info/update/clear-cache           │
│ - cloakserve: CDP server mode for remote control              │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│ LAYER 2: 18+ --fingerprint-* launch flags                     │
│ - --fingerprint=seed (deterministic identity)                 │
│ - --fingerprint-gpu-vendor / -gpu-renderer                    │
│ - --fingerprint-platform / -brand / -brand-version            │
│ - --fingerprint-timezone / -locale / -location                │
│ - --fingerprint-webrtc-ip (with auto value)                   │
│ - --fingerprint-fonts-dir                                      │
│ - --fingerprint-storage-quota                                  │
│ - --fingerprint-noise=false                                    │
│ - (+ ~10 more)                                                 │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│ LAYER 3: 57 C++ source-level patches in compiled binary       │
│ - canvas / WebGL / audio / fonts / GPU reporting              │
│ - WebRTC IP spoofing                                           │
│ - navigator.webdriver = false                                  │
│ - navigator.plugins.length = 5 (real plugin list)              │
│ - TLS ja3n/ja4/akamai fingerprint match                       │
│ - WebAuthn capabilities (v0.3.25 NEW)                          │
│ - AAC audio encoder (v0.3.25 NEW)                              │
│ - Window position spoofing (v0.3.25 NEW)                       │
│ (compiled into Chromium 146.0.7680.177.4 on Linux/Windows;    │
│  Chromium 145.0.7632.109 + 26 patches on macOS)               │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│ LAYER 4: humanize=True (optional behavioral layer)            │
│ - Bézier mouse curves                                          │
│ - Per-character keyboard timing with typos                     │
│ - Decelerating scroll                                          │
│ - Configurable via human_config dict                          │
│ - Presets: "normal" / "careful"                                │
└──────────────────────────────────────────────────────────────┘
```

The 4-layer architecture is conceptually clean: SDK → flags → C++ patches → behavioral simulation. Layer 4 is opt-in (off by default); Layers 1-3 always active.

## Why this matters at the corpus level

**Purpose-built-for-stealth as product axis** (OC-I observational candidate) — Prior corpus subjects with stealth treated it as one feature among many (general automation + stealth + agents + reasoning). CloakBrowser inverts the proportion: stealth is the central product axis, everything else is integration support.

This is **structurally distinct** from existing T2 Service archetypes in the corpus:
- browser-use v34 = general agent-browser-automation (stealth is one feature)
- crawl4ai v29 = LLM-friendly scraping (stealth is one tactic)
- Skyvern v24 = auth-aware automation (stealth not focus)

→ **OC-I "Detection-Evasion-As-Product-Axis"** registered for v69+v70+ stale-check.

## Maintenance velocity

- **86 days, 28+ releases** = sustained 0.33 releases/day
- **16 → 25 → 57 patches** = non-linear growth
- **3 Chromium major versions tracked** (142 → 145 → 146)
- **Single security-fix entry across 28+ releases** (v0.3.28 #217)
- **No deprecation notices** = API stability discipline despite Beta status

This is **active-maintenance T2 Service** at the highest cadence band observed in the corpus (compared to browser-use / crawl4ai which release at 1-2 weeks cadence). The ~3-day release-cadence is corpus-rare for a Beta-status product.

## Platform-tier-disparity (Pattern #83 strengthening)

| Platform | Chromium | Patches |
|----------|----------|---------|
| Linux x64 / arm64 | 146 | 57 |
| Windows x64 | 146 | 57 |
| macOS arm64 / x64 | **145 (one major behind)** | **26 (less than half)** |

README acknowledges this honestly:
> *"macOS fingerprints have inconsistencies aggressive sites catch. Use Windows fingerprint on macOS by disabling stealth defaults and setting platform/GPU flags manually."*

→ Pattern #83 strengthening evidence — honest disclosure of platform-tier-disparity in README, not buried in CHANGELOG.

## Cross-corpus references (Pattern #57 PASS)

The README explicitly cites **2 corpus subjects**:
- **browser-use** (v34 corpus) — Python framework integration; 70K stars
- **Crawl4AI** (v29 corpus) — Python framework integration; 58K stars

Plus **CloakHQ maintains a FORK** of crawl4ai (v29 corpus) as integration asset — 3-layer-cross-corpus-integration depth (cite + integrate + fork).

This is **corpus-record depth** of cross-corpus integration for a single subject. → OC-G "Fork-as-Integration-Strategy" sub-component evidence.

## Storm Bear lessons from Entity 1

For the vault operator:

- **Architectural decisions cascade pattern-strength.** The C++ source-level decision differentiates from all 4 prior competitors in a single positioning dimension. Single-axis differentiation that's deeply technical creates moat.
- **Purpose-built-product vs feature-among-many.** CloakBrowser inverts the corpus default (where stealth is one feature among many) by making stealth the entire product. This is a packaging discipline worth noting for Storm Bear's own vault tooling: if a tool's value is one specific axis, sell that axis as the entire product, not as a sub-feature.
- **Honest acknowledgment of disparity.** CloakBrowser acknowledges macOS tier-disparity in README rather than burying it — this is the v68 Pattern #83 honest-deficiency-disclosure pattern operationalized at the README surface.
