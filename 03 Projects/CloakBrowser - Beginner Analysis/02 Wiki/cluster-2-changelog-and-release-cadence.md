# Cluster 2 — CHANGELOG + release cadence + security incidents

> Source: `CHANGELOG.md` · 28+ entries v0.1.0 → v0.3.28 · fetched 2026-05-18

## Release cadence — corpus-rare extreme

- **v0.1.0:** 2026-02-22 (day 0)
- **v0.3.28:** 2026-05-11 (day 78)
- **Releases:** 28+ across 86 days = **~1 release every 3 days** = **0.33 releases/day**

For comparison:
- **v68 zero:** 3 releases in 2 days = 1.5/day (corpus-record per-day-cadence but tiny absolute count)
- **v68 zero** trajectory if sustained for 86 days: would be ~129 releases (not realistic; agent-first language has different curve)
- **CloakBrowser** sustained 0.33/day for 86 days = **corpus-record for sustained sustained-release-cadence** at >2 month window

This is **anti-pattern to v68 zero's "anti-compatibility-by-default" policy** — CloakBrowser ships frequently but each release is incremental and backwards-compatible (per CHANGELOG entries; no breaking-change markers in v0.3.x band).

→ Pattern-Library observation: **sustained-incremental-release-cadence-as-product-discipline** sub-archetype within Pattern #52 family (HIGH-velocity-without-EXTREME-VIRAL-stars).

## Fingerprint-patch count progression

| Release | Date | Chromium ver | Patch count | Δ |
|---------|------|---|---|---|
| v0.1.0 | 2026-02-22 | 142.0.7444.175 | **16** | — |
| v0.3.0 | 2026-03-02 | 145.0.7632.109 | **25** | +9 (~30%) |
| v0.3.25 | 2026-04-16 | 146.0.7680.177.3 (Linux) | **57** | +32 (Linux/arm64) — note: README still says "49" at v0.3.25 era |
| v0.3.26 | 2026-04-28 | 146.0.7680.177.4 (Windows) | **57** | Windows brought to parity |
| v0.3.28 | 2026-05-11 | 146.0.7680.177.4 | **57** | unchanged |

**Observation:** Patch-count growth is **non-linear** — 16 → 25 → 57 in 86 days. The largest jump (+32) happened at v0.3.25 (Chromium 146 upgrade). New patches at v0.3.25 explicitly: *"WebAuthn capabilities, AAC audio encoder, window position spoofing."*

This suggests CloakBrowser's patch-add velocity is responsive to two forcing functions:
1. **Upstream Chromium updates** — each Chromium major version forces patch-rebase + opportunity to add new patches
2. **Detection-arms-race** — when detection systems find new fingerprint axes, CloakBrowser adds patches

**Open question (Q9 in open-questions.md):** Is the patch-add velocity sustainable, or will detection systems update faster than CloakBrowser can patch?

## Chromium version-tracking discipline

| Platform | Chromium ver at v0.3.28 | Patches | Status |
|----------|---|---|---|
| Linux x86_64 | 146.0.7680.177.3 | 57 | latest |
| Linux arm64 (RPi, Graviton) | 146.0.7680.177.3 | 57 | latest |
| macOS arm64 (Apple Silicon) | 145.0.7632.109 | **26** | one major behind |
| macOS x86_64 (Intel) | 145.0.7632.109 | **26** | one major behind |
| Windows x86_64 | 146.0.7680.177.4 | 57 | latest |

**macOS platform-lag observation:** Apple Silicon + Intel macOS lag by one major Chromium version + half the patch count (26 vs 57). README notes: *"macOS fingerprints have inconsistencies aggressive sites catch. Use Windows fingerprint on macOS by disabling stealth defaults..."* → **Honest acknowledgment of platform-tier-disparity** (Pattern #83 strengthening evidence).

## Security incident — v0.3.28 #217 (Pattern #83 strengthening)

The single security-fix entry across 28+ releases is **v0.3.28 #217**:

> *"Security: `cloakserve` — sanitize fingerprint seed to prevent path traversal, bind to `127.0.0.1` on bare metal, detects Podman containers"*

This is **3 security improvements in one fix:**
1. **Path traversal sanitization** in fingerprint seed → indicates a code-injection vector existed (likely Bash/shell exec via flag interpolation)
2. **Bind to `127.0.0.1` on bare metal** → indicates `cloakserve` previously bound to `0.0.0.0` (network-exposed by default)
3. **Detect Podman containers** → expand from Docker-only environment detection

**Pattern #83 evidence breakdown for v69:**
- The security-fix entry exists in CHANGELOG (vs hidden in commit-history-only)
- Linked to PR #217 (transparent issue/PR reference)
- Three distinct improvements bundled — honest scope disclosure
- No claim of "minor" or "edge case" framing

→ Strong instance of *Honest-Deficiency-Disclosure in CHANGELOG-as-disclosure-surface* (corpus-first sub-mechanism for Pattern #83; prior corpus surfaces were LICENSE, README, AGENTS.md).

## Framework integrations (added over time)

CHANGELOG references framework-integration additions across releases:
- **v0.1.0:** Playwright (Python sync + async)
- **v0.2.0:** Playwright (JS) + Puppeteer (JS)
- **v0.3.0:** Patchright dependency-switch (breaking change)
- **v0.3.25:** AWS Lambda integration example (later renumbered)
- **v0.3.26:** AWS Lambda example finalized
- **(throughout)**: Scrapy / Crawlee / BrowserBase / Stagehand / LangChain compatibility documented

**Pattern #57 cross-corpus-citation evidence:** Framework integrations table in README lists 7 frameworks; **2 are corpus subjects** (browser-use v34 + Crawl4AI v29). This is **corpus-first explicit multi-corpus-subject integration documentation in single README**.

## Breaking change at v0.3.0 — `playwright` → `patchright` dependency switch

> *"**Breaking:** Python dependency switched from `playwright` to `patchright`"*

Patchright is a stealth-Playwright fork (separate project, not by CloakHQ). The switch implies:
- Patchright provides stealth-specific patches at the Playwright-API layer
- CloakBrowser combines Patchright (Playwright stealth wrapper) + CloakBrowser binary (Chromium stealth patches)
- Dual-stealth-layer architecture: binary-level + API-level

**Pattern Library implication:** This is a **layered-stealth-architecture** observation. Worth noting but not formal pattern material at single occurrence.

## Release-cadence sub-pattern within Pattern #19 ecosystem-portfolio-builder

CloakHQ's release cadence (0.33 releases/day across 86 days) is sustained at the SUBJECT level, not portfolio level. The org doesn't have a separate release-cadence for CloakBrowser-Manager or chromium-stealth-builds (those have much lower velocity).

This is **subject-focused-not-portfolio-focused velocity** — distinct from Pattern #19 ecosystem-portfolio-builder which often distributes velocity across multiple repos. → potential Pattern #19 sub-variant or sister-observation but probably observational-only.

## What's NOT in the CHANGELOG

Notable absences:
- No **deprecation notices** for old API surfaces — implies API stability
- No **vulnerability disclosure-policy reference** — security-fix #217 documents fix but doesn't cite a CVE-style report-process
- No **co-author attribution** in CHANGELOG entries (contributors are listed at README contributors section, but CHANGELOG entries don't attribute per-release)
- No **version-naming-rationale notes** — v0.1 → v0.2 → v0.3 progression isn't tied to documented stability milestones
- No **roadmap-fulfillment tracking** — Roadmap section in README lists features as "Released" / "Planned" but CHANGELOG doesn't cross-reference

The CHANGELOG is **execution-log, not narrative-log** — focused on what shipped per-version vs why or for-whom.
