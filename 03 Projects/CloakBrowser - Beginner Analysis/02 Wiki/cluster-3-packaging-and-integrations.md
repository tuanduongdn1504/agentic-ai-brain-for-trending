# Cluster 3 — Packaging + framework integrations + org structure

> Source: `pyproject.toml` + `examples/` + org-level repo listing · fetched 2026-05-18

## Dual SDK distribution (Python + JS)

CloakBrowser ships **two SDK packages** with parallel APIs:

| Channel | Manifest | Install command | Entry point |
|---------|----------|------------------|------|
| Python (PyPI) | `pyproject.toml` (hatchling) | `pip install cloakbrowser` | `from cloakbrowser import launch` |
| JavaScript (npm) | `package.json` | `npm install cloakbrowser playwright-core` | `import { launch } from 'cloakbrowser';` |
| JavaScript Puppeteer | (sub-module) | `npm install cloakbrowser puppeteer-core` | `import { launch } from 'cloakbrowser/puppeteer';` |

**Both SDKs trigger lazy auto-download of ~200MB Chromium binary on first use.** Binary cached locally at `~/.cloakbrowser/` (Python default; configurable via `CLOAKBROWSER_CACHE_DIR` env var).

The dual-SDK strategy is **corpus-rare**:
- v66 agentmemory ships an SDK protocol (MCP) but is API-layer not language-binding-layer
- v34 browser-use is Python-primary (no JS counterpart at parity)
- v29 crawl4ai is Python-primary (no JS counterpart at parity)
- v51 agent-skills-of-vercel skills are non-runtime artifacts

**Closest corpus parallel:** Anthropic's anthropic-sdk-python + anthropic-sdk-typescript pattern. But CloakBrowser is dual-SDK-with-binary-distribution, not just API-binding parallel SDKs.

→ Pattern observation: *Dual-SDK + Binary-Distribution architecture* — not formal pattern material at single occurrence.

## pyproject.toml — explicit Beta status + 4 optional-dependency groups

```toml
[project]
name = "cloakbrowser"
description = "Stealth Chromium that passes every bot detection test..."
requires-python = ">=3.9"
classifiers = [
    "Development Status :: 4 - Beta",
    ...
]
dependencies = [
    "playwright>=1.40",
    "httpx>=0.24",
]

[project.optional-dependencies]
geoip = ["geoip2>=4.0", "socksio>=1.0"]
patchright = ["patchright>=1.40"]
serve = ["aiohttp>=3.9", "websockets>=12.0"]
dev = ["pytest>=7.0", "pytest-asyncio>=0.23"]
```

**Observations:**
- **"Development Status :: 4 - Beta"** PyPI classifier is the official pre-1.0 disclosure (vs v68 zero's prominent README banner)
- **Patchright as OPTIONAL dependency** (not core) — implies wrapper supports both `playwright` and `patchright` paths at runtime (despite CHANGELOG v0.3.0 marking `playwright → patchright` as breaking change)
- **geoip optional** (geoip2 + socksio) — enables timezone/locale auto-detection from proxy exit IP
- **serve optional** (aiohttp + websockets) — enables `cloakserve` CDP server mode
- **Tight upper-bound discipline absent** — only lower bounds (`>=1.40`, `>=0.24`) without upper bounds on Playwright/httpx (corpus-typical for Python packaging; but worth noting)

## Examples directory (Phase 2 ingestion result)

```
examples/
├── integrations/        ← sub-directory (framework-specific examples)
├── basic.py
├── fingerprint_scan_test.py
├── persistent_context.py
├── recaptcha_score.py
└── stealth_test.py
```

The top-level Python examples cover 5 use cases:
- `basic.py` — minimal launch + navigate
- `fingerprint_scan_test.py` — fingerprint identity verification
- `persistent_context.py` — cookie + localStorage persistence
- `recaptcha_score.py` — reCAPTCHA v3 score testing
- `stealth_test.py` — detection-evasion smoke test

The `integrations/` subdirectory (not enumerated at Phase 2 probe — would require deeper fetch) likely contains:
- AWS Lambda integration (mentioned in CHANGELOG v0.3.26)
- browser-use integration example
- Crawl4AI integration example
- Possibly Scrapy / Crawlee / Stagehand examples

**Corpus observation:** The example file naming pattern (verb + axis) is conventional. Not pattern-distinguishing.

## Framework integrations table (from README)

| Framework | Stars | Language | Integration mode |
|-----------|-------|----------|------------------|
| browser-use ([github.com/browser-use/browser-use](https://github.com/browser-use/browser-use)) | 70K | Python | **v34 corpus subject** — framework launches CloakBrowser binary |
| Crawl4AI ([github.com/unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)) | 58K | Python | **v29 corpus subject** — framework launches CloakBrowser binary |
| Crawlee ([github.com/apify/crawlee-python](https://github.com/apify/crawlee-python)) | 8.6K | Python | non-corpus; CloakHQ maintains FORK |
| Scrapling ([github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)) | 21K | Python | non-corpus |
| Stagehand ([github.com/browserbase/stagehand](https://github.com/browserbase/stagehand)) | 21K | TypeScript | non-corpus; BrowserBase product |
| LangChain ([github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)) | 100K+ | Python | non-corpus |
| Selenium | — | Python | non-corpus |

**Integration strategies documented (two modes):**
- **Mode 1:** Framework launches the binary (framework imports `binary_path = ensure_binary()` + `stealth_args = get_default_stealth_args()`)
- **Mode 2:** CloakBrowser launches first; framework connects via CDP (CloakBrowser starts at `--remote-debugging-port=9242`, framework connects)

Mode 2 is **CDP-server-as-multiplexer** pattern (similar to `cloakserve` CDP server but in-process). → potential observational variant of Pattern #18 shared-backend-service (single browser binary serves multiple framework clients via CDP).

## Org-structure (CloakHQ, 6 public repos)

| Repo | Stars | License | Status | Role |
|------|-------|---------|--------|------|
| **CloakBrowser** ← THIS SUBJECT | 14.9k | MIT wrapper + Proprietary Binary | Beta, Active | Primary product |
| CloakBrowser-Manager | 376 | (Python — license not probed) | Active | Web profile manager sister-product |
| chromium-stealth-builds | — | (binary releases) | Active | Binary artifact distribution |
| crawl4ai **(FORK)** | — | Apache-2.0 | Active | **FORK of v29 corpus subject** |
| crawlee-python **(FORK)** | — | Apache-2.0 | Active | FORK of dependency framework |
| awesome-playwright **(FORK)** | — | CC0-1.0 | Active | FORK of discovery list |

**3 original repos + 3 forks.** The forks are integration-strategy assets:
- `crawl4ai` fork → likely maintains a CloakBrowser-patched version (or hosts CloakBrowser-integration PR)
- `crawlee-python` fork → similar; integration patches
- `awesome-playwright` fork → discoverability / curation

→ **Phase 4b OC-G observational candidate: Fork-as-Integration-Strategy** — org maintains forks of dependency frameworks for integration-with-patches. Corpus-first sub-pattern. Distinct from Pattern #19 ecosystem-portfolio-builder (forks aren't original products; they're integration assets).

## Contributors — 12 named per README

Contributors with role attribution (README closing section):
- `@evelaa123` — humanize behavior + persistent contexts
- `@yahooguntu` — persistent contexts
- `@kitiho` — null viewport fix
- `@eofreternal` — humanConfig types
- `@manaskarra` — iframe scope fix + GeoIP timeout guard
- `@Youhai020616` — SOCKS5 credential encoding
- `@AlexTech314` — AWS Lambda integration
- `@dgtlmoon` — graceful cleanup
- `@zackycodes` — Chrome extension loading
- `@aaronjmars` — security fixes
- `@Seryiza` — Nix/NixOS flake
- `@245678000000` — package-lock sync

**Observation:** README-level contributor attribution with feature-area roles is **corpus-rare**. Typical OSS projects link to CONTRIBUTORS.md or use auto-generated lists. This README-embedded form with role-attribution suggests deliberate-recognition curation. → potential Pattern #19 sub-pattern (founder-personal lineage variant: org-anonymity-with-contributor-personalization).

## Supply-chain security (verification surface)

The README documents **3-tier signature verification** for releases:

```bash
# Tier 1: GPG signature on git tags
gpg --keyserver keyserver.ubuntu.com --recv-keys C60C0DDC9D0DE2DD
git verify-tag chromium-v146.0.7680.177.3

# Tier 2: GitHub binary attestation
gh attestation verify cloakbrowser-linux-x64.tar.gz --repo CloakHQ/cloakbrowser

# Tier 3: Cosign Docker image signature
cosign verify \
  --certificate-identity-regexp "https://github.com/CloakHQ/CloakBrowser/" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  cloakhq/cloakbrowser:latest
```

**Pattern #66 strengthening:** 3-tier signature verification (GPG + GitHub attestation + cosign) is **corpus-broadest signature-verification surface** documented in a single README. Prior corpus subjects: most use 0-1 verification mechanisms.

→ Pattern #66 meta-supply-chain-awareness gets significant strengthening evidence at v69. Potential sub-archetype: *signature-verification-as-marketed-feature*.

## Funding / business model signals

- **`ko-fi.com/cloakhq`** — micro-donation link (in README "Support" section)
- **`cloakhq@pm.me`** — primary contact (pm.me = ProtonMail hosted; privacy-focused email)
- **OEM/SaaS licensing carve-out** in BINARY-LICENSE — implies B2B commercial licensing as primary revenue model
- **No Patreon / GitHub Sponsors / OpenCollective / commercial subscription** discoverable in README

**Observation:** The OEM/SaaS-licensing clause is the **primary revenue mechanism**, with ko-fi as supplementary. Pattern #45 sub-typology 45c sub-mechanism: **Acceptable Use + OEM-licensing carve-out as dual revenue/risk-mitigation lever.**

## Anti-author anonymity signals (OC-H evidence)

- **No GitHub user profile** for `CloakHQ` as individual — it's an org
- **No "About" page** at the cloakbrowser.dev homepage that would reveal a person
- **Email at `pm.me`** (ProtonMail hosted) — privacy-focused mail provider
- **No location / blog / social media** discoverable
- **No author photo / bio in README**
- **No personal twitter / linkedin** linked

→ **OC-H observational candidate: Anonymous-Corporate-Author for Dual-Use Tools** — pm.me email + no individual identity disclosure + dual-use product → defensive anonymity profile. Corpus-first.

## Cross-corpus integration depth

The framework integrations span **3 layers of corpus inter-connection:**

1. **Direct corpus citation** (Pattern #57 PASS): browser-use v34 + Crawl4AI v29 named in README
2. **Adjacent corpus tier:** Scrapling/Crawlee/Stagehand/LangChain are non-corpus but agent-ecosystem-adjacent
3. **Forked corpus subject:** CloakHQ maintains a FORK of crawl4ai (v29 corpus)

This **3-layer corpus integration** is **corpus-record-depth** for any single subject. → Pattern #57 sub-mechanism candidate: *fork-of-cited-corpus-subject-as-strongest-integration-anchor*.

## What's NOT in the packaging signals

- No **commercial product page** discoverable on cloakbrowser.dev (or not probed at Phase 2)
- No **SaaS product offering** beyond binary distribution
- No **GitHub Sponsors / Patreon** alternative funding channel (only ko-fi)
- No **commercial support tier** advertised in README
- No **service-level-agreement language** anywhere
- No **enterprise customer testimonials**

The funding/business profile is **minimal-public-surface** — consistent with anonymous-corporate-author archetype. Implies private B2B sales motion via OEM/SaaS-licensing inquiries to cloakhq@pm.me.
