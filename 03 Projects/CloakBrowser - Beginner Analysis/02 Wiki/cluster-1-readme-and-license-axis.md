# Cluster 1 — README + dual-license axis

> Source: `README.md` + `LICENSE` + `BINARY-LICENSE.md` · v0.3.28 era · fetched 2026-05-18

## Subject self-positioning (verbatim tagline + claim set)

**Tagline:** *"Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed."*

**Claim set (verbatim from README):**
- "49 source-level C++ patches" (current README header) → **57 patches at v0.3.26+** (per CHANGELOG progression; README and CHANGELOG out of sync on patch count — minor disclosure-honesty observation)
- "0.9 reCAPTCHA v3 score" (human-level, server-verified)
- "Passes Cloudflare Turnstile, FingerprintJS, BrowserScan and 30+ detection sites"
- "Auto-updating binary with background update checks"
- "Free and open source — no subscriptions or usage limits" (note: wrapper is OSS; binary is proprietary-free-with-restrictions)
- "Drop-in Playwright/Puppeteer replacement — identical API, just swap imports"

## Architecture decision: source-level C++ patches vs runtime injection

The README presents the architectural decision as a **differentiation axis** vs all prior corpus-and-noncorpus competitors:

| Approach | Examples | CloakBrowser positioning |
|---------|----------|------------------------|
| **JS injection at runtime** | playwright-stealth | "Sometimes" passes Turnstile, "0.3-0.5" reCAPTCHA — implication: detected easily |
| **Config patches** | undetected-chromedriver | "Sometimes" passes Turnstile, "0.3-0.7" reCAPTCHA — implication: detected with new Chrome versions |
| **C++ source patches (Firefox)** | Camoufox | "Pass" Turnstile, "0.7-0.9" reCAPTCHA — but "Unstable beta" maintenance + Firefox engine |
| **C++ source patches (Chromium)** | **CloakBrowser** | "Pass" Turnstile, **"0.9"** reCAPTCHA, "Active" maintenance, Native Playwright |

This is a **purpose-built-for-stealth product axis** — vs corpus-prior subjects (browser-use v34 / crawl4ai v29 / Skyvern v24) which treat stealth as one feature among many. **OC-I observational candidate: Detection-Evasion-As-Product-Axis (corpus-first).**

## API surface (verbatim from README)

The Python API exposes 4 primary entry points:
- `launch()` — sync, Playwright drop-in
- `launch_async()` — asyncio drop-in
- `launch_context()` — convenience for browser+context with fingerprint settings in one call
- `launch_persistent_context()` — user profile with cookie/localStorage persistence

Plus 4 utility functions:
- `binary_info()`, `clear_cache()`, `ensure_binary()` (Python)
- `ensureBinary()`, `clearCache()`, `binaryInfo()` (JS)

CLI sub-commands:
- `cloakbrowser install` / `info` / `update` / `clear-cache`
- `cloakserve` — CDP server mode for remote Chromium control

JavaScript SDK ships TWO entry-point modules — `cloakbrowser` (Playwright) + `cloakbrowser/puppeteer` (Puppeteer). README explicitly recommends **Playwright over Puppeteer** for reCAPTCHA Enterprise sites: *"Puppeteer sends more CDP traffic that reCAPTCHA detects."*

This is **corpus-first dual-SDK-with-explicit-recommendation-against-one-SDK** — observation worth noting but probably not formal pattern material.

## `humanize=True` — behavioral-simulation-as-Boolean-flag

The `humanize=True` flag at launch replaces all mouse/keyboard/scroll with human-like equivalents. README presents this as a **behavioral-simulation layer** independent from fingerprint-spoofing:

| Interaction | Default | With `humanize=True` |
|---|---|---|
| Mouse movement | Instant teleport | Bézier curve with easing/overshoot |
| Clicks | Instant | Realistic aim point + hold duration |
| Keyboard | Instant fill | Per-character timing, thinking pauses, **typos** |
| Scroll | Jump | Accelerate → cruise → decelerate |
| `fill()` | Instant value set | Clears, types character-by-character |

Presets exposed: `"normal"` (default), `"careful"` (slower, more deliberate). Custom config via `human_config={...}` dict with knobs like `mistype_chance: 0.05`, `typing_delay: 100`, `idle_between_actions: True`, `idle_between_duration: [0.3, 0.8]`.

**Observation:** This is a corpus-rare exposure of "humanness simulation as a configurable subsystem." Prior corpus subjects (browser-use, crawl4ai, Skyvern) don't have a similar Boolean-flag-with-config layer for human-simulation. → potential observational candidate but stealth-feature-specific.

## Fingerprint flag taxonomy

The README documents **18+ `--fingerprint-*` flags** as launch-time configuration:
- Master: `--fingerprint=seed` (deterministic identity)
- Hardware: `--fingerprint-gpu-vendor`, `-gpu-renderer`, `-hardware-concurrency`, `-device-memory`, `-screen-width`, `-screen-height`, `-taskbar-height`
- Identity: `--fingerprint-brand` (Chrome/Edge/Opera/Vivaldi), `-brand-version`, `-platform`, `-platform-version`
- Geographic: `--fingerprint-location`, `-timezone`, `-locale`
- Network: `--fingerprint-webrtc-ip` (with `auto` value derived from proxy IP)
- Storage: `--fingerprint-storage-quota`
- Fonts: `--fingerprint-fonts-dir` (path to target-platform fonts)
- Modes: `--fingerprint-noise=false` (disable noise injection), `--enable-blink-features=FakeShadowRoot`

This is **corpus-broadest fingerprint-axis surface** explicitly enumerated as flags. The breadth suggests substantial C++ patch work — each flag corresponds to a code path inserted into Chromium's source tree.

## Test results table (corpus-first artifact)

The README contains a **detection-test-results table** comparing stock Playwright vs CloakBrowser across 14 detection-axis dimensions:

| Detection Service / Axis | Stock Playwright | CloakBrowser |
|---|---|---|
| reCAPTCHA v3 | 0.1 (bot) | **0.9** (human) |
| Cloudflare Turnstile (non-interactive) | FAIL | **PASS** |
| Cloudflare Turnstile (managed) | FAIL | **PASS** |
| ShieldSquare | BLOCKED | **PASS** |
| FingerprintJS bot detection | DETECTED | **PASS** |
| BrowserScan bot detection | DETECTED | **NORMAL (4/4)** |
| bot.incolumitas.com | 13 fails | **1 fail** |
| deviceandbrowserinfo.com | 6 true flags | **0 true flags** |
| `navigator.webdriver` | `true` | **`false`** |
| `navigator.plugins.length` | 0 | **5** |
| `window.chrome` | `undefined` | **`object`** |
| UA string | `HeadlessChrome` | **`Chrome/146.0.0.0`** |
| CDP detection | Detected | **Not detected** |
| TLS fingerprint | Mismatch | **Identical to Chrome** |

**Corpus-first observation:** A subject README that documents its own detection-test results with a baseline comparison table. Compare: crawl4ai v29 / browser-use v34 don't include comparable benchmark tables in README. → potential OC: *Benchmark-Table-In-README-As-Marketing*.

## Comparison table (corpus-first 5-tool head-to-head)

The README contains a 5-tool feature-comparison table — also corpus-rare:

| Feature | Playwright | playwright-stealth | undetected-chromedriver | Camoufox | **CloakBrowser** |
|---|---|---|---|---|---|
| reCAPTCHA v3 score | 0.1 | 0.3-0.5 | 0.3-0.7 | 0.7-0.9 | **0.9** |
| Cloudflare Turnstile | Fail | Sometimes | Sometimes | Pass | **Pass** |
| Patch level | None | JS injection | Config patches | C++ (Firefox) | **C++ (Chromium)** |
| Survives Chrome updates | N/A | Breaks often | Breaks often | Yes | **Yes** |
| Maintained | Yes | Stale | Stale | Unstable | **Active** |
| Browser engine | Chromium | Chromium | Chrome | Firefox | **Chromium** |
| Playwright API | Native | Native | No (Selenium) | No | **Native** |

**Pattern Library link:** This table is a strong instance of **Pattern #57 cross-corpus-citation** sub-variant 57c-product-comparison-parallel (NEW v60 audit registered at N=1). At v69, this is a structurally-parallel observation — 57c-product N=2 evidence candidate.

**Honesty:** The comparison table acknowledges Camoufox achieves 0.7-0.9 reCAPTCHA score (only marginally below CloakBrowser's 0.9) — not framed as decisive superiority. Aligns with Pattern #83 honest-disclosure-discipline.

## License axis — the v69 PRIMARY contribution

CloakBrowser ships **two distinct license files** with structurally distinct scopes:

### LICENSE — MIT (wrapper code only)

```
MIT License
Copyright (c) 2026 CloakHQ
[standard MIT permissions: use, copy, modify, merge, publish, distribute, sublicense, sell]
```

Scope: the Python + JS wrapper source code in this repository. **Not the binary.**

### BINARY-LICENSE.md — Proprietary + Acceptable Use (binary)

Scope: the compiled CloakBrowser Chromium binary distributed via GitHub Releases and `cloakbrowser.dev`.

Key clauses (verbatim quotes from BINARY-LICENSE.md):

**Grant of Use** *(broad personal/commercial usage)*:
> "You are granted a non-exclusive, non-transferable, royalty-free license to use the Binary for personal or commercial purposes. No fees are required."

**Restrictions** *(5 explicit "may NOT" actions)*:
> "You may NOT: 1. Redistribute the Binary, in whole or in part, whether modified or unmodified; 2. Resell, sublicense, or repackage the Binary, or include it in any product or service distributed to third parties; 3. Reverse engineer, decompile, or disassemble the Binary [...] except to the extent permitted by applicable law; 4. Modify the Binary or create derivative works based on it; 5. Remove or alter any copyright notices, license files, or attribution included with the Binary."

**Cloud/Container/Integration Use** *(internal-use carve-out)*:
> "Internal use — You may store and run the unmodified Binary within internal infrastructure, including Docker images, VM templates, CI runners, container registries, and artifact repositories [...] solely for your organization's internal operational purposes."

**Acceptable Use** *(enumerated prohibited uses — corpus-first density)*:
> "Without limiting the above, the following uses are expressly prohibited:
> - Unauthorized access to financial, banking, healthcare, or government authentication systems
> - Credential stuffing, brute-force login attempts, or automated account creation
> - Circumventing authentication on systems you do not own or have authorization to test
> - Any activity that constitutes fraud, identity theft, or unauthorized data collection"

**Indemnification + Limitation of Liability**:
> "You agree to indemnify and hold harmless CloakHQ and its contributors from any claims, damages, losses, liabilities, and expenses (including reasonable legal fees) arising from your unlawful use of the Binary or your violation of this license."
> "CLOAKHQ'S TOTAL AGGREGATE LIABILITY SHALL NOT EXCEED ONE HUNDRED US DOLLARS (US $100)."

The **$100 max-liability cap** is corpus-rare (most OSS license shapes have no liability cap, just disclaimers). → OC-J observational candidate evidence.

**Data Collection clause** (worth noting given Pattern #66 supply-chain):
> "CloakHQ does not intentionally include telemetry, analytics, or tracking mechanisms in the Binary. The Binary is built on ungoogled-chromium, which removes Google-specific services and telemetry."

**ungoogled-chromium upstream attribution** — corpus-first explicit acknowledgment of ungoogled-chromium as direct upstream (Pattern #66 strengthening evidence).

### Why this is corpus-first license-shape

Prior corpus Pattern #45 dual-licensing exemplars:
- **45a:** Unsloth v23 — Apache-2.0 + commercial-shield clause (single license file with hybrid clauses; product license + revenue gate)
- **45b:** AutoGPT v59 — MIT + PolyForm-Shield (single license file with PolyForm overlay; commercial-protection focused)
- **45c (NEW at v69):** CloakBrowser — **two separate license files** + **artifact-scope split** (MIT for source code, proprietary-with-acceptable-use for compiled binary) + **explicit Acceptable Use enumeration** + **Indemnification** + **$100 max-liability cap**

The distinguishing mechanisms of 45c:
1. **Two separate license files in repo** (LICENSE + BINARY-LICENSE.md) — not one file with hybrid clauses
2. **Artifact-scope-split** — license boundary follows artifact compilation rather than usage tier
3. **Acceptable Use enumeration** — explicit list of prohibited uses (rather than open-ended "for legitimate purposes only")
4. **Indemnification + max-liability cap** — defensive legal scaffolding rare in OSS license shapes
5. **OEM/SaaS-licensing carve-out** — bundling into third-party-distributed product requires separate commercial license (B2B revenue gate)

This is **substantively different from 45a/45b mechanisms**. → Phase 4b PRIMARY proposal: register Pattern #45 sub-typology 45c.

## ungoogled-chromium upstream chain (Pattern #66 strengthening)

BINARY-LICENSE explicitly documents the upstream chain:
> "The Binary is built on Chromium, which is open-source software by The Chromium Authors under the BSD 3-Clause License, and incorporates components from the open-source ungoogled-chromium project."

This is **corpus-first 3-level upstream attribution**:
1. Chromium (Google / The Chromium Authors / BSD-3-Clause)
2. ungoogled-chromium (community fork; removes Google telemetry)
3. CloakBrowser (CloakHQ patches; 57 fingerprint patches on top)

Pattern #66 meta-supply-chain-awareness gains structurally strongest evidence at v69 — full upstream chain documented in the license itself, not just CHANGELOG or attribution notes.

## What's NOT in the README

Notable absences:
- No `AGENTS.md` or `CLAUDE.md` file (404 at root)
- No `SKILL.md` (no Anthropic skills protocol integration)
- No author bio / personal identity
- No funding-source transparency (ko-fi link present but no enterprise customer references)
- No security disclosure policy in README itself (`.github/SECURITY.md` not probed)
- No code-of-conduct
- No CONTRIBUTING.md presence verified
- No explicit pre-1.0 instability disclosure (vs v68 zero's pre-1.0 explicit notice) — CloakBrowser is at v0.3.28 (still pre-1.0) but README does NOT prominently warn about instability

The pre-1.0 status (v0.3.28) without prominent instability disclosure is observationally distinct from v68 zero's explicit "pre-1 and intentionally unstable" framing. → potential Pattern #83 sub-variant or counter-evidence axis.
