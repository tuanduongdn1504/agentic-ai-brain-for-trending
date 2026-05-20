# (C) Cluster 3 — Distribution + community channels

**Sources:**
- GitHub Releases (linked from website + README; 11 releases including v1.6.0 latest)
- Facebook share URL (`?fbclid=...` indicates the URL Storm Bear submitted was from a Facebook share — distribution evidence)
- Donation surfaces (MB Bank Vietnam + PayPal international)
- Dual-repo discipline (PRODUCT + WEBSITE)

## 15-section format

### 1. Cluster scope

How SmartMacroAI reaches users + how it monetizes + how it represents itself across distinct surfaces. Covers: GitHub Releases binary-distribution / Facebook-share-distribution-channel evidence / dual-repo-marketing-discipline / donation-surfaces hybrid-localization.

### 2. Primary distribution channel: GitHub Releases

**Latest release**: v1.6.0 (2026-05-13)

**Total releases observed**: 11+ (per CHANGELOG.md reference; v1.5.8 was 12 days prior)

**Release artifacts (3 file formats per release)**:
1. `SmartMacroAI-v1.6.0-Setup.exe` — Windows installer (NSIS or similar)
2. `SmartMacroAI-v1.6.0-win-x64.exe` — Portable executable
3. `SmartMacroAI-v1.6.0-win-x64.zip` — Portable archive

→ **3-format binary distribution** = explicit choice-architecture for users (installer vs portable-exe vs portable-zip). Distinct from corpus conventions of single-binary or single-source-archive.

### 3. Secondary distribution channel: marketing website

**`TroniePh/SmartMacroAI-Website`** (GitHub Pages):
- HTML static site
- 0 stars (separate from product repo's 17 stars)
- Vietnamese-first UX
- Hosts all CTAs that link back to GitHub Releases
- v1.6.0 version displayed

→ **CORPUS-FIRST dual-repo separation at solo developer scale** (product + marketing site in separate repos). Distinct from v76 HoangNguyen0403 monorepo + v74 LLMs-from-scratch monorepo + most v60+ subjects.

### 4. Tertiary distribution channel: Facebook share (evidence-based)

**Evidence**: The URL Storm Bear submitted contains `?fbclid=IwY2xjawR6KQ5leHRuA2FlbQIxMABicmlkETFPOXJFczVuVjdOSkJVd3BZc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHoCU_LnPAFNGzP9kFbdYnJyV8srz2eGZwFtycm3N-rtBbA7ysbMk9nhEVGcz_aem_mQMPIMX36x3DLG0CU_jOrg` (Facebook click identifier).

**Interpretation**:
- Storm Bear encountered SmartMacroAI via Facebook (likely Vietnamese-tech-community share)
- Facebook is the dominant social platform in Vietnam — natural distribution channel for VN-targeted product
- App ID `222039178820089` in fbclid corresponds to a Facebook app

→ **CORPUS-FIRST Facebook-share-distribution-channel evidence in v60+ window**. Corpus subjects typically reach users via GitHub Trending / dev social media (X / Hacker News / Reddit). v80 reaching VN-cultural-peer via Facebook is structurally distinct.

→ **Library-vocabulary candidate "Cultural-Distribution-Channel-Diversity"** PROVISIONAL N=1 (Facebook for VN audiences vs X for global dev audiences).

### 5. Donation surfaces — hybrid-localization

**MB Bank (Vietnam-domestic banking channel)**:
- Account holder: PHẠM QUỐC DUY
- Account number: 379997999
- QR code for mobile banking transfer (Vietnamese-mobile-payment-native UX)
- VND currency (implied)

**PayPal (international channel)**:
- Email: nhocbobi22@gmail.com
- Link: paypal.com/paypalme/nhocbobi22
- USD currency (implied default)

**Two surfaces, two locales, dual-channel monetization**:
- VN-domestic users → MB Bank QR code (familiar UX)
- International users → PayPal email (familiar UX)

→ **CORPUS-FIRST hybrid-donation-channel-localization-at-solo-developer-scale**: domestic banking + international PayPal. Distinct from corpus conventions of GitHub Sponsors (universal) or Patreon (international-only).

→ **Library-vocabulary candidate "Hybrid-Donation-Channel-Localization"** PROVISIONAL N=1.

### 6. Cross-wiki distribution-pattern intersections

| Sibling | Distribution-pattern axis | v80 alignment |
|---------|---------------------------|---------------|
| **v76 agent-skills-standard (HoangNguyen0403)** | npm + pnpm-workspace monorepo + CLI-generated harness formats + 10+ AI harness targets | v80 NARROWS to GitHub-Releases-only + Windows-only single hardware substrate (NO multi-harness) |
| **v77 easy-vibe (datawhalechina)** | 5-deploy-target intelligence with base-path auto-detection + 13-locale i18n breadth | v80 narrows to 1-deploy-target (local Windows) + 2-locale depth (EN + VN with 830+ keys) |
| **v78 ECC** | 11+-harness dirs + pnpm + GitHub App + Hermes operator multi-product distribution | v80 narrows to single-product + single-OS + dual-repo (product + marketing) |
| **v79 autoresearch_folktales (Thu Vu)** | uv-exclusive single-tool-no-fallback + Apple-Silicon-only + 0-multi-harness | v80 = also single-OS substrate-pinned (Windows vs Apple Silicon) + similar narrowness profile |

→ **v80 fits the "deliberately-narrow distribution profile" Library-vocabulary candidate** (v79 contributed this; v80 strengthens N=2):
- v79: uv-exclusive + Apple-Silicon-only + 2-explicit-agent-platforms (narrow)
- v80: GitHub-Releases-only + Windows-only + dual-repo (narrow but different axis)

### 7. Active-deployment intent analysis

**Verified GitHub API 2026-05-20**:
- stars: 17
- forks: 13
- subscribers: 0
- open_issues: 0

**fork_ratio = 13/17 = 0.765 = 76.5%**

→ **NEW CORPUS-RECORD-HIGH active-deployment-intent**: exceeds v79 autoresearch_folktales 0.484 prior record (which itself was NEW CORPUS-RECORD-HIGH on 2026-05-20) by **1.58×**.

**2-consecutive-wiki fork_ratio CORPUS-RECORD-HIGH redefinition arc**:
- v76 HoangNguyen0403: 0.296 (1.66× v65 0.178 prior record)
- v79 autoresearch_folktales: 0.484 (1.64× v76 0.296)
- **v80 SmartMacroAI: 0.765 (1.58× v79 0.484)** ← NEW NEW NEW

→ **CORPUS-FIRST 3-wiki sustained fork_ratio CORPUS-RECORD-HIGH ladder** (v76 → v79 → v80 each redefining the ceiling).

**Interpretation of v80's 76.5% fork_ratio**:
- 13 of 17 stargazers also forked (only 4 of 17 starred-without-forking)
- Extremely high active-deployment / make-your-own-version intent
- Could correlate with: (a) Vietnamese developers wanting to localize / customize for own use, (b) gamers wanting modified anti-cheat-bypass macros, (c) RPA practitioners building on the platform
- BUT 0 subscribers + 0 open issues = no ongoing engagement signal

→ **Try-once-and-move-on profile** (similar to v79's pattern but at HIGHER fork_ratio intensity).

### 8. Distribution-channel summary table

| Channel | Volume | Discoverability | Engagement |
|---------|--------|-----------------|------------|
| **GitHub Releases** | 11+ releases × 3 formats | Medium (direct linking from website + README) | Download stats not visible |
| **GitHub Pages site** | 1 live site | High (SEO-indexable; shareable URL) | 0 stars on repo |
| **Facebook share** | Inferred from fbclid evidence | High (Vietnamese-tech-community network) | Unknown reach |
| **MB Bank donation** | 1 account | VN-domestic UX | Unknown |
| **PayPal donation** | 1 account | International UX | Unknown |

→ **5-surface distribution mix at solo developer scale** — corpus-first observation.

### 9. Tech stack supply chain analysis

**Local-bundled dependencies**:
- .NET 8.0 runtime (Microsoft; ~80MB; bundled)
- WPF (Microsoft; included in .NET)
- Tesseract 5.2 OCR (Apache 2.0; bundled)
- Emgu.CV OpenCV bindings (MS-PL or commercial; bundled)
- Playwright (Apache 2.0; bundled)
- Win32 API (Microsoft; OS-provided)
- Interception Driver (custom license; user-installed)

**Remote dependencies**:
- OpenAI API (commercial; user provides own key)
- Gemini API (commercial; user provides own key)

**License-compatibility risk surface**: SmartMacroAI has **NO LICENSE file** but bundles Apache 2.0 + MS-PL + custom-licensed components. **CORPUS-FIRST unambiguous-absent-LICENSE-at-Apache-bundle-scale**. Pattern #66 within-pattern observation.

### 10. Pattern Library implications from Cluster 3

| Pattern | Evidence |
|---------|----------|
| **NEW T5 sub-archetype (PRIMARY)** | Distribution profile reinforces "Hybrid-RPA-with-LLM-augmented" classification |
| **Pattern #19 NEW sub-mechanism 19k** | VN-LOCATED solo dev + dual-repo + Facebook-share-distribution + hybrid-donation channels |
| **Pattern #29 absent-LICENSE strengthening** | 404-verified absent-LICENSE + Apache-bundle scale = license-compatibility-risk evidence |
| **Pattern #52 LOW-velocity** | 0.425 stars/day below all sub-class thresholds |
| **Pattern #66 within-pattern** | Mixed local-bundled + remote-API supply-chain layers |
| **Library-vocabulary candidates** | Cultural-Distribution-Channel-Diversity + Hybrid-Donation-Channel-Localization + Marketing-Site-vs-README AI-Positioning Divergence + Localization-Depth-vs-Locale-Breadth |
| **Pattern #84** | N/A — no cross-vendor agent-tolerance (Windows-only; not agentic) |
| **Pattern #57** | N/A — no corpus citations |

### 11. Cross-wiki distribution-pattern table

| Wiki | Primary distribution | Secondary | Localization mix |
|------|---------------------|-----------|------------------|
| v75 impeccable | 14-harness multi-target | npm CLI | EN |
| v76 agent-skills-standard | npm + pnpm + 10+ harnesses CLI-generated | MCP server | EN |
| v77 easy-vibe | VitePress + 5-deploy-target auto-detection | i18n 13-locale | 13 locales (breadth) |
| v78 ECC | npm + GitHub App + ECC Pro SaaS + 11+ harnesses | Hermes operator | 10+ locales |
| v79 autoresearch_folktales | uv-exclusive single-tool | Apple-Silicon-only | EN-only |
| **v80 SmartMacroAI** | **GitHub Releases (3 formats) + GitHub Pages marketing site** | **Facebook share + hybrid donations** | **EN + VN (depth 830+ keys)** |

### 12. Counter-evidence + absences

**Notable ABSENCES**:
- No **Discord / Telegram community** (despite Telegram alerts as feature)
- No **roadmap or public Trello / GitHub Projects**
- No **plugin / extension architecture** visible
- No **SECURITY.md / vulnerability disclosure**
- No **multi-OS** (Windows-only hard pin)
- No **mobile** (desktop-only)
- No **browser-extension** (although Playwright integrates with Chromium)

### 13. Routine v2.3 codification candidates from Cluster 3

1. **Facebook-share-distribution-channel evidence (fbclid in submitted URL)** — formal Phase 0 distribution-channel detection axis addition
2. **Hybrid-donation-channel-localization (domestic-banking + international-PayPal)** — Library-vocabulary item candidate registration
3. **Dual-repo-marketing-discipline at solo developer scale** — Phase 0 distribution-axis sub-investigation addition
4. **Localization-depth (key-count × locale-count) vs locale-breadth (locale-count alone) distinction** — Phase 0 i18n axis refinement
5. **License-state-verification via 404-on-LICENSE-file** — Phase 0 license-state probe addition (stronger than GitHub API NOASSERTION alone)

### 14. Counter-evidence + retroactive corrections

**No retroactive corrections triggered**.

### 15. Phase 4b PRIMARY confirmation

Cluster 3 strengthens Phase 4b PRIMARY = NEW T5 sub-archetype candidate "Hybrid-RPA-with-LLM-augmented-decision-making" by confirming:
- Distribution profile matches HYBRID classification (local binary + remote LLM API)
- Architecture inverts typical LLM-vs-tools relationship (LLM is one tool-mode among many)
- Storm Bear (a) cultural-peer evidence reinforced by Facebook-VN-distribution + MB-Bank-VN-donation

→ Phase 3 Entity 3 will integrate all three clusters for final N=1 registration package.
