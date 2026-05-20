# (C) Entity 2 — Distribution: Windows-only + dual-repo + Facebook-distribution-channel

**Subject:** Distribution + ecosystem-integration of SmartMacroAI — how the product reaches users, how it monetizes, and how it represents itself across multiple surfaces.

## 13-section canonical format

### 1. Primary distribution: GitHub Releases (binary)

**Latest**: v1.6.0 (2026-05-13). Active development cadence: ~12 days between v1.5.8 and v1.6.0.

**3 formats per release**:
- `SmartMacroAI-v1.6.0-Setup.exe` (installer)
- `SmartMacroAI-v1.6.0-win-x64.exe` (portable executable)
- `SmartMacroAI-v1.6.0-win-x64.zip` (portable archive)

→ **CORPUS-FIRST 3-format binary release discipline at solo developer scale**.

### 2. Secondary distribution: Marketing website (separate repo)

**`TroniePh/SmartMacroAI-Website`** GitHub Pages:
- HTML static site
- 0 stars (vs product repo's 17 stars)
- Vietnamese-first UX
- All CTAs link back to GitHub Releases

→ **CORPUS-FIRST dual-repo separation at solo developer scale** (product + marketing site in distinct repos).

### 3. Tertiary distribution: Facebook share (evidenced)

The URL Storm Bear submitted contained `?fbclid=...` (Facebook click ID) — direct evidence of Facebook share-discovery.

**Implications**:
- Facebook is the dominant social platform in Vietnam
- Natural VN-cultural-peer distribution channel
- Distinct from typical corpus subjects reaching users via X / Hacker News / GitHub Trending / Reddit

→ **CORPUS-FIRST Facebook-share-distribution-channel evidence in v60+ window**.

### 4. Donation surfaces: hybrid-localization

| Channel | Purpose | UX |
|---------|---------|-----|
| **MB Bank Vietnam** | VN-domestic banking transfer | QR code for mobile banking |
| **PayPal** | International transfer | Email-based + paypal.me URL |

**Two channels = dual-locale monetization discipline**:
- VN-domestic users → familiar MB Bank QR
- International users → familiar PayPal

→ **CORPUS-FIRST hybrid-donation-channel-localization at solo developer scale**.

→ Library-vocabulary candidate "Hybrid-Donation-Channel-Localization" PROVISIONAL N=1.

### 5. Active-deployment intent (fork_ratio CORPUS-RECORD-HIGH analysis)

**fork_ratio = 13/17 = 0.765 = 76.5%** — NEW CORPUS-RECORD-HIGH

**3-wiki sustained CORPUS-RECORD-HIGH ladder**:
- v76 (0.296) → v79 (0.484) → **v80 (0.765)** ← NEW NEW NEW

→ **CORPUS-FIRST 3-wiki sustained fork_ratio CORPUS-RECORD-HIGH ladder** (each redefining ceiling by ~1.6×).

**Interpretation of 76.5% fork_ratio**:
- 13 of 17 stargazers also forked (4 of 17 starred-only)
- Extremely high active-deployment / customize-your-own intent
- 0 subscribers + 0 open issues → **Try-Once-and-Move-On profile**
- Could correlate with: (a) VN devs localizing for own use, (b) RPA practitioners customizing macros for own automation, (c) gamers using Driver-Level mode for own bots

### 6. Tech stack supply chain (mixed local + remote)

**Local-bundled**:
- .NET 8.0 runtime
- WPF
- Tesseract 5.2 OCR
- Emgu.CV (OpenCV bindings)
- Playwright (Chromium browser)
- Win32 API + Interception Driver

**Remote-API**:
- OpenAI API (user provides key)
- Gemini API (user provides key)

→ **Hybrid local + remote architecture** — distinct from corpus convention of either pure-local or pure-cloud.

### 7. License-compatibility analysis

**SmartMacroAI itself**: NO LICENSE file (404-verified); GitHub API NOASSERTION.

**Bundled dependencies and their licenses**:
- .NET 8.0: MIT (Microsoft)
- WPF: MIT (Microsoft)
- Tesseract: Apache 2.0
- Emgu.CV: MS-PL or commercial (varies)
- Playwright: Apache 2.0
- Interception Driver: custom license (user-installed)

→ **License-compatibility risk**: bundles Apache 2.0 + custom-licensed deps under no-license-of-its-own. **CORPUS-FIRST unambiguous-absent-LICENSE-at-Apache-bundle-scale**. Pattern #29 absent-LICENSE strengthening + NEW sub-mechanism candidate "404-confirmed-absent-LICENSE" PROVISIONAL N=1.

### 8. Distribution-narrowness profile

**v80 SmartMacroAI distribution-narrowness profile**:
- 1 OS (Windows) — narrowest possible
- 1 hardware architecture (x64) — narrowest possible
- 2 explicit user-locales (EN + VN) with 830+ key depth
- 1 distribution surface (GitHub Releases) for binaries
- 2 distribution surfaces (binary + marketing site)
- 2 donation channels (MB Bank + PayPal)
- 1 social distribution channel observed (Facebook)

→ **Library-vocabulary candidate "Deliberately-Narrow Distribution Profile" N=2 strengthening**:
- v79 contributed: uv-exclusive + Apple-Silicon-only + 2-agent-platforms narrow
- v80 adds: GitHub-Releases-only + Windows-only + dual-repo narrow (but different axis)

→ 2-wiki sustained narrow-distribution-profile observation = candidate for codification.

### 9. Cross-wiki distribution-pattern intersections

| Sibling | Distribution-pattern axis | v80 alignment |
|---------|---------------------------|---------------|
| **v75 impeccable** | 14-harness multi-target distribution | v80 narrows to 0-harness (end-user app) + Windows-only |
| **v76 agent-skills-standard** | npm + pnpm-workspace + CLI-generated 10+ harnesses | v80 narrows to single-product + dual-repo + GitHub-Releases-only |
| **v77 easy-vibe** | 5-deploy-target + 13-locale i18n breadth | v80 narrows to 1-deploy-target + 2-locale depth |
| **v78 ECC** | 11+-harness + npm + GitHub App + ECC Pro SaaS | v80 narrows to single-binary + free-with-donations |
| **v79 autoresearch_folktales** | uv-exclusive + Apple-Silicon-only | v80 = parallel pattern (substrate-pinned + tool-pinned) but different axes |

### 10. Pattern Library tags

- **NEW T5 sub-archetype candidate** (PRIMARY)
- **Pattern #19 NEW sub-mechanism 19k candidate** — Vietnamese-Located-Solo-Developer-with-Dual-Repo-Marketing-Discipline
- **Pattern #29 absent-LICENSE strengthening + NEW sub-mechanism "404-confirmed-absent-LICENSE"** PROVISIONAL N=1
- **Pattern #66 within-pattern** — mixed local-bundled + remote-API
- **Library-vocabulary candidates**: Cultural-Distribution-Channel-Diversity / Hybrid-Donation-Channel-Localization / Deliberately-Narrow Distribution Profile (N=2 strengthening v79 + v80) / Localization-Depth-vs-Locale-Breadth Distinction (N=2 strengthening v77 + v80)
- **Pattern #84** N/A
- **Pattern #57** N/A
- **Pattern #52** N/A (LOW-velocity)

### 11. Build / install / run

**Build from source** (per README):
```bash
git clone https://github.com/TroniePh/SmartMacroAI.git
cd SmartMacroAI
dotnet restore
dotnet build
dotnet run
./build-release.ps1 win-x64
```

**Install from binary**:
- Download Setup.exe or .zip from GitHub Releases
- Run installer or extract portable archive
- Launch SmartMacroAI.exe

### 12. Counter-evidence + absences

**Notable distribution-absences**:
- No homebrew / scoop / winget package
- No Microsoft Store distribution
- No telemetry surface
- No SECURITY.md vulnerability-disclosure-policy
- No reproducible-build evidence

### 13. Phase 4b PRIMARY confirmation from Entity 2

Entity 2 strengthens PRIMARY = NEW T5 sub-archetype candidate by:
- Confirming distribution profile is end-user-binary-distribution (T5 confirmed; not framework-for-agents)
- Confirming HYBRID local + remote architecture at distribution layer
- Confirming CORPUS-FIRST observations (3-wiki fork_ratio ladder + Facebook-share-evidence + hybrid-donation-localization)

→ Phase 3 Entity 3 will tie all 3 clusters + Entity 1-2 into formal N=1 sub-archetype registration.
