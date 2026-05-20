# (C) Cluster 2 — Product GitHub repo (TroniePh/SmartMacroAI)

**Sources:**
- `https://github.com/TroniePh/SmartMacroAI` (repo)
- `README.md` (bilingual EN + VN; fetched via WebFetch from raw.githubusercontent.com 2026-05-20)
- GitHub API metadata + LICENSE-file 404 check

## 15-section format

### 1. Cluster scope

The product repo itself. Contains: C# source code (.NET 8 + WPF), README bilingual, CHANGELOG.md referenced, 11 GitHub Releases (latest v1.6.0). Topics: auto-clicker / automation / bot / csharp / macro / macros / ocr / playwright / rpa / windows / wpf.

### 2. Verified GitHub metadata (2026-05-20)

| Field | Value |
|-------|-------|
| stars | 17 |
| forks | 13 |
| subscribers | 0 |
| open_issues | 0 |
| size | 24,232 KB |
| primary language | C# |
| license | **NOASSERTION** (per GitHub API; `/contents/LICENSE` 404 — no LICENSE file exists) |
| created_at | 2026-04-10 |
| updated_at | 2026-05-20 |
| pushed_at | 2026-05-13 |
| default_branch | main |
| has_issues | true |
| has_wiki | false |
| has_pages | false |
| archived | false |
| fork | false |
| homepage | tronieph.github.io/SmartMacroAI-Website (CORPUS-FIRST homepage-points-to-corresponding-marketing-repo at solo dev scale) |
| network_count | 13 |

**Velocity**:
- 17 stars / 40 days = **0.425 stars/day LOW-velocity**
- **fork_ratio = 13/17 = 0.765 = 76.5% NEW CORPUS-RECORD-HIGH active-deployment-intent** (exceeds v79 0.484 prior record by 1.58×)

### 3. README section headings (verbatim)

1. Overview
2. Features
3. Input Automation
4. Core Capabilities
5. Productivity
6. Security & Distribution
7. Download
8. System Requirements
9. Quick Start
10. Driver Level Mode
11. Build from Source
12. Changelog
13. Donate
14. Contact
15. Tiếng Việt (Vietnamese-language mirror of preceding sections)

→ **Bilingual README structure with full-mirror Vietnamese section**. Compare to v77 easy-vibe 13-locale BREADTH; v80 is 2-locale DEPTH (single README, both languages inline, 830+ localization keys claimed for UI).

### 4. 4-input-mode architecture (verbatim from README)

| Mode | Technical mechanism | Anti-detection level | Use case |
|------|---------------------|---------------------|----------|
| **Stealth** | PostMessage to background window | HIGH (doesn't seize mouse) | Background macros while user works |
| **Raw Input** | SendInput with hardware scan codes | MEDIUM | General automation |
| **Hardware** | SetCursorPos + mouse_event | LOW (visible to user) | Compatible with most apps |
| **Driver Level** | Kernel Interception driver (marked "PRO") | HIGHEST (anti-cheat bypass) | Games with anti-cheat |

→ **CORPUS-FIRST 4-input-mode automation architecture in v60+ window**. Compare to v44 browser-use (single mode: Chrome DevTools Protocol).

### 5. Core capabilities (verbatim from README "Core Capabilities" section)

- "Image recognition with confidence thresholds" (computer vision)
- "Pixel color detection"
- "OCR Text Detection — Read text from screen regions via Tesseract 5.2"
- "If/Else branching with conditional logic"
- "Loop control (count-based, infinite, break-condition)"
- "CSV auto-fill functionality"
- "**AI Integration — OpenAI & Gemini for smart decision-making**" ← CRITICAL: LLM integration
- "**Web Automation — Playwright-based browser control**"
- "**CDP Stealth — Chrome DevTools Protocol for 100% background Chromium clicks**"

→ **Key finding**: LLM integration is at the **decision-making layer**, not orchestration layer. OpenAI + Gemini APIs called when image-conditions / pixel-conditions need smart fallback, not as the framework's brain.

### 6. AI integration analysis

**Verbatim**: *"AI Integration — OpenAI & Gemini for smart decision-making"*

**Interpretation**:
- OpenAI + Gemini are CONSUMED by SmartMacroAI as API services (cloud-dependence)
- LLM is OPTIONAL — most macros run without LLM
- LLM is at decision-layer (e.g., "is this screen showing X?") rather than orchestration-layer
- User must provide own API key (inferred; not stated)

**Architecture distinction**:
| Subject | LLM role |
|---------|---------|
| v9 autoresearch + v79 autoresearch_folktales | LLM as orchestration brain (researcher agent) |
| ECC v1+v78 + v66 agentmemory + v68 zero | LLM as harness consumer + tool user |
| v75 impeccable + v76 agent-skills-standard | LLM as skill consumer |
| **v80 SmartMacroAI** | **LLM as tool-mode option (one among many)** |

→ **NEW T5 sub-archetype "Hybrid-RPA-with-LLM-augmented-decision-making"** — the architectural inversion is corpus-first.

### 7. Productivity features (verbatim from README)

- Multi-dashboard macro management
- Macro recording (real-time capture)
- Time-based and interval scheduling
- Undo/Redo support
- ROI (Region of Interest) picker
- Six pre-built templates
- Execution history with filtering

### 8. Security features + Anti-detection

**Verbatim**:
- "Macro password protection"
- "Script sharing via encoded strings"
- "**Anti-Detection — Bézier mouse curves + randomized delays**"
- "Telegram alert notifications"
- "Bilingual UI (830+ localization keys)"

→ **CORPUS-FIRST Bézier-mouse-curves anti-detection discipline** in v60+ window.

→ **CORPUS-FIRST 830+ localization keys at solo developer scale** — depth-of-translation rather than breadth-of-locales.

### 9. System requirements (verbatim from README)

| Component | Specification |
|-----------|---------------|
| OS | Windows 10 x64 (build 19041+) or later |
| Runtime | .NET 8.0 (bundled) |
| RAM | 4 GB minimum |
| Storage | 300 MB (core) / 600 MB (with web automation) |
| Permissions | Admin required for Driver Level mode |

→ **Windows-only + hardware-substrate hard-pin** — distinct from v79's Apple-Silicon-MPS-only. Different hardware substrates entirely; both are substrate-pinned distributions.

### 10. Tech stack (verbatim from README)

- **.NET 8.0** — runtime and build framework
- **WPF** — UI framework
- **Tesseract 5.2** — OCR engine
- **Playwright** — web browser automation
- **OpenAI & Gemini APIs** — AI decision-making (REMOTE; not bundled)
- **Interception Driver** — kernel-level input (anti-cheat support)
- **Emgu.CV** — OpenCV bindings (computer vision)
- **Win32 API** — native Windows input

→ **Hybrid local + remote architecture**: local UI + local CV/OCR + remote LLM APIs.

### 11. Build from source instructions (verbatim)

```bash
git clone https://github.com/TroniePh/SmartMacroAI.git
cd SmartMacroAI
dotnet restore
dotnet build
dotnet run
./build-release.ps1 win-x64 (for releases)
```

→ Standard .NET dotnet workflow + PowerShell release script. No agent-specific build orchestration.

### 12. Changelog highlights (v1.6.0 + v1.5.8)

**v1.6.0 (2026-05-13)** — critical bug fixes:
- Coordinate picker returning (0,0) due to dialog Hide() corrupting WPF state
- DialogResult InvalidOperationException across 11 dialog files
- PreviewMouseLeftButtonDown event handler fix
- New: multi-image search (up to 20 images per action) + pixel color detection + scroll/drag actions + improved Driver Level mode with SetForegroundWindow retry logic

**v1.5.8 (2026-05-12)**:
- Scroll actions + drag actions + pixel color conditions + regex support in variables + CDP Stealth service + ROI picker functionality

→ Active development cadence (12 days between v1.5.8 → v1.6.0). Solo developer iteration pace.

### 13. LICENSE state verification

**GitHub API**: `license: NOASSERTION`
**Direct check**: `https://api.github.com/repos/TroniePh/SmartMacroAI/contents/LICENSE` → **HTTP 404 Not Found**
**README mentions**: NO explicit license text or SPDX identifier
**Footer mentions**: "© 2026 SmartMacroAI" (copyright claim, not license)

→ **Pattern #29 absent-LICENSE strengthening evidence with UNAMBIGUOUS confirmation via 404**. Stronger evidence than v79's README-declared-MIT-without-LICENSE-file (Pattern #83 83f.4 NEW sub-variant) because v80 doesn't declare any license. Pure absent-license state.

→ **NEW sub-mechanism candidate**: Pattern #29 sub-mechanism "404-confirmed-absent-LICENSE" PROVISIONAL N=1 (distinct from prior absent-LICENSE evidence which lacked explicit 404 verification).

### 14. Pattern Library implications from Cluster 2

| Pattern | Evidence |
|---------|----------|
| **NEW T5 sub-archetype candidate (PRIMARY)** | LLM-as-tool-mode-option architecture confirmed via "AI Integration — OpenAI & Gemini for smart decision-making" |
| **Pattern #29 absent-LICENSE strengthening** | UNAMBIGUOUS 404-confirmed absent-LICENSE state; NEW sub-mechanism candidate "404-confirmed-absent-LICENSE" PROVISIONAL N=1 |
| **Pattern #19 NEW sub-mechanism 19k candidate** | VN-LOCATED solo dev + dual-repo discipline + hybrid-RPA-LLM product |
| **Pattern #66 within-pattern** | OpenAI + Gemini API external-dependence; Tesseract + Emgu.CV + Playwright local-bundled; Interception Driver kernel-level — mixed supply-chain layers |
| **Library-vocabulary candidate "Localization-Depth-vs-Locale-Breadth"** | 830+ keys × 2 locales = 1660+ translations depth vs v77's 13 locales × N keys breadth |
| **Library-vocabulary candidate "Marketing-Site-vs-README AI-Positioning Divergence"** | Marketing site downplays LLM; README emphasizes "AI Integration" — corpus-first divergence observation |
| **Pattern #84** | N/A (no cross-vendor agent-tolerance architecture; non-agentic-distribution) |
| **Pattern #57** | N/A (no corpus citations) |
| **Pattern #52** | LOW-velocity 0.425/d below all sub-class thresholds |

### 15. Absences (counter-evidence audit)

**Notable ABSENCES from product README**:
- No LICENSE file (404 verified)
- No SECURITY.md
- No CONTRIBUTING.md
- No tests/ visible
- No CI badges
- No SBOM
- No mention of OpenAI/Gemini license-compatibility (Anthropic / Claude not mentioned)
- No multi-OS support (Windows-only)
- No release-signing visible

→ These absences are consistent with **solo-developer indie-RPA-product** profile at small-scale (17 stars). Not red flags; reinforce tier classification.
