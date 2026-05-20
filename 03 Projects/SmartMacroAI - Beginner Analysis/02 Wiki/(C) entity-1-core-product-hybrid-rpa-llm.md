# (C) Entity 1 — Core product: Hybrid-RPA + LLM-augmented-decision-making

**Subject:** `TroniePh/SmartMacroAI` core product = Windows-desktop RPA framework with 4-input-mode architecture (Stealth + Raw Input + Hardware + Driver Level Kernel) + Computer Vision + OCR + Optional LLM-augmented decision-making (OpenAI + Gemini APIs).

## 13-section canonical format

### 1. What is it (one-paragraph)

SmartMacroAI is a Windows-desktop RPA (Robotic Process Automation) tool by Vietnamese solo developer Phạm Quốc Duy. It automates clicking, typing, image-recognition, OCR-based screen-reading, and conditional logic on Windows 10/11 — with anti-detection features including 4 distinct input modes (Stealth PostMessage / Raw Input SendInput / Hardware mouse_event / Driver Level Kernel Interception driver) and Bézier-mouse-curves + randomized delays for human-like behavior. The framework integrates **optional LLM-augmented decision-making via OpenAI and Gemini APIs** — used at decision-layer (e.g., "is this screen showing X?") rather than orchestration-layer. Most macros run without LLM; LLM is one tool-mode option among many. Distribution: GitHub Releases binary (Setup.exe + portable .exe + portable .zip) + standalone marketing site at github.io + Facebook-share-distribution-channel + MB Bank Vietnam + PayPal donation channels.

### 2. Tier placement + archetype

**Tier**: T5 Application — **NEW sub-archetype "Hybrid-RPA-with-LLM-augmented-decision-making"** PROVISIONAL N=1

**Archetype**: solo-VN-LOCATED-developer-with-dual-repo-marketing-discipline (Pattern #19 NEW sub-mechanism 19k candidate)

**Scale**: small (17 stars / 13 forks at 40 days; fork_ratio 0.765 NEW CORPUS-RECORD-HIGH)

**T5 sub-archetype distinction matrix**:

| T5 sub-class | LLM role | Examples |
|--------------|---------|----------|
| LLM-as-orchestration-brain | LLM drives the framework loop | v9 autoresearch + v79 autoresearch_folktales |
| LLM-as-harness-consumer | LLM is consumer of skills/tools | ECC v1 + v66 agentmemory + v68 zero |
| LLM-as-application-itself | LLM is the application UI | chat UIs |
| **LLM-as-tool-mode-option (NEW v80)** | **LLM is one of multiple tool modes** | **v80 SmartMacroAI** |

### 3. 4-input-mode architecture (PRIMARY structural feature)

**Mode 1 — Stealth (PostMessage)**:
- Mechanism: Win32 PostMessage to target window's message queue
- Anti-detection: HIGH (doesn't seize mouse; user can keep working)
- Use case: background automation while user interacts with OS

**Mode 2 — Raw Input (SendInput)**:
- Mechanism: Win32 SendInput with hardware scan codes
- Anti-detection: MEDIUM (appears as keyboard/mouse hardware input)
- Use case: general automation requiring system-wide focus

**Mode 3 — Hardware (mouse_event)**:
- Mechanism: SetCursorPos + mouse_event Win32 calls
- Anti-detection: LOW (visible cursor movement)
- Use case: compatibility with apps that detect SendInput-style inputs

**Mode 4 — Driver Level Kernel (marked "PRO")**:
- Mechanism: Kernel Interception driver (user-installed at admin permission)
- Anti-detection: HIGHEST (kernel-level; bypasses most anti-cheat)
- Use case: games with anti-cheat protection (e.g., automation that requires kernel-input-fidelity)

→ **CORPUS-FIRST 4-input-mode automation architecture in v60+ window**.

→ Note on ethics: The "anti-cheat bypass" use case explicitly mentioned in README raises ethical considerations (gaming-bot use). This is documented but not endorsed.

### 4. AI integration architecture

**Verbatim from README**: *"AI Integration — OpenAI & Gemini for smart decision-making"*

**Interpretation**:
- LLM API calls are OPTIONAL at macro-execution time
- LLM is called at decision-layer (image-condition fallback / OCR-result interpretation / template-matching reasoning)
- Macros can run entirely without LLM (rule-based mode)
- User must provide own OpenAI / Gemini API key

**Architecture inversion vs typical agentic frameworks**:
- Typical (v9, v66, v79): LLM orchestrates → tools execute
- v80 SmartMacroAI: Rule-based engine orchestrates → LLM is ONE OF MANY tools

→ This inversion is structurally novel in v60+ window. Distinct from all prior T5 entrants.

→ **Library-vocabulary candidate "LLM-Inversion-Architecture"** PROVISIONAL N=1: LLM-as-callable-tool vs LLM-as-orchestration-brain.

### 5. Computer Vision + OCR pipeline

**Image recognition**:
- Confidence thresholds (configurable)
- Multi-image search (up to 20 images per action per v1.6.0 changelog)
- ROI (Region of Interest) picker for performance
- Bound to OpenCV via Emgu.CV bindings

**OCR**:
- Tesseract 5.2 engine (bundled)
- Screen-region text detection
- Bilingual recognition support

**Pixel color detection**:
- Single-pixel + color-range queries
- Conditional logic integration

→ **Local-bundled CV + OCR + LLM-remote-augmentation** = hybrid local + remote architecture.

### 6. Anti-detection discipline

**Verbatim**: *"Anti-Detection — Bézier mouse curves + randomized delays"*

**Bézier curves**: instead of moving cursor in straight lines, agent moves along Bézier paths simulating human hand-curvature. CORPUS-FIRST Bézier-mouse-curves anti-detection in v60+ window.

**Randomized delays**: jitter between actions to avoid deterministic timing patterns.

→ **CORPUS-FIRST anti-detection-via-Bézier-curves + randomized-delays explicit discipline** in v60+ window. Compare to v44 browser-use which has its own anti-detection patterns at browser layer.

### 7. Cross-wiki sibling references (mandatory ≥3)

| Sibling | Direction |
|---------|-----------|
| **v76 agent-skills-standard (Hanoi VN solo dev)** | DIRECT STRUCTURAL PEER — both VN-LOCATED solo devs; cluster N=2 |
| **v77 easy-vibe (13-locale i18n)** | Library-vocabulary "Localization-Depth-vs-Locale-Breadth"; v80 = depth (830+ keys × 2 locales) |
| **v44 browser-use** | Playwright sibling — both use Playwright for browser automation in different contexts |
| **v79 autoresearch_folktales** | Storm Bear streak adjacency + fork_ratio CORPUS-RECORD-HIGH redefinition arc 2-consecutive |
| **v9 autoresearch (Karpathy parent)** | T5 sub-archetype comparison — LLM-orchestration vs LLM-as-tool-mode |
| **v68 zero (vercel-labs)** | Sub-archetype-precedent for v80's NEW T5 sub-archetype |
| **v66 agentmemory** | Platform-substrate-layer distinction — agentmemory is harness substrate; v80 is end-user application |

### 8. Pattern Library tags

- **NEW T5 sub-archetype candidate** (PRIMARY) — Hybrid-RPA-with-LLM-augmented-decision-making PROVISIONAL N=1
- **Pattern #19 NEW sub-mechanism 19k candidate** — Vietnamese-Located-Solo-Developer-with-Dual-Repo-Marketing-Discipline PROVISIONAL N=1
- **Pattern #29 absent-LICENSE strengthening + NEW sub-mechanism candidate** "404-confirmed-absent-LICENSE" PROVISIONAL N=1 (stronger than v79's README-declared-MIT-without-LICENSE because v80 doesn't declare any license)
- **Pattern #66 within-pattern** — mixed local-bundled + remote-API supply-chain
- **Pattern #52** N/A (LOW-velocity 0.425/d)
- **Pattern #57** N/A (no corpus citations)
- **Pattern #84** N/A (non-agentic; no cross-vendor architecture)

### 9. Novel observations + Library-vocabulary candidates

**Library-vocabulary candidates emerging from Entity 1**:
- **LLM-Inversion-Architecture** (LLM-as-callable-tool vs LLM-as-orchestration-brain)
- **Hybrid Local CV/OCR + Remote LLM-API architecture** (PRIMARY tech-stack pattern)
- **4-input-mode automation architecture as choice-architecture** (4 tools for different anti-detection trade-offs)
- **Bézier-mouse-curves anti-detection discipline** (corpus-first explicit anti-detection technique)
- **Anti-cheat-bypass use case as explicit feature** (ethically-ambiguous; documented honestly)

### 10. Verbatim feature list (full enumeration from README)

**Input Automation**: 4 modes (Stealth + Raw Input + Hardware + Driver Level)

**Core Capabilities**:
- Image recognition with confidence thresholds
- Pixel color detection
- OCR Text Detection — Read text from screen regions via Tesseract 5.2
- If/Else branching with conditional logic
- Loop control (count-based, infinite, break-condition)
- CSV auto-fill functionality
- AI Integration — OpenAI & Gemini for smart decision-making
- Web Automation — Playwright-based browser control
- CDP Stealth — Chrome DevTools Protocol for 100% background Chromium clicks

**Productivity**:
- Multi-dashboard macro management
- Macro recording (real-time capture)
- Time-based and interval scheduling
- Undo/Redo support
- ROI (Region of Interest) picker
- Six pre-built templates
- Execution history with filtering

**Security**:
- Macro password protection
- Script sharing via encoded strings
- Anti-Detection — Bézier mouse curves + randomized delays
- Telegram alert notifications
- Bilingual UI (830+ localization keys)

### 11. 3-step Getting Started (per website)

1. **Select Target** — choose Windows app or browser tab to automate
2. **Build Script** — drag-and-drop logic builder; configure actions + conditions
3. **Run & Enjoy** — execute macros in background (Stealth) or visible (Hardware) mode

→ **No-code drag-and-drop philosophy** — distinct from v9 + v79 autoresearch's code-modification-by-agent philosophy.

### 12. Performance characteristics

**System requirements**: Windows 10 x64 (build 19041+) / Windows 11; .NET 8.0 (bundled); 4 GB RAM; 300 MB core / 600 MB with Playwright web automation; admin permissions required for Driver Level mode.

**Execution profile**: ∞ parallel macros (per marketing site claim); multi-dashboard supports concurrent execution.

### 13. Notable absences (counter-evidence audit)

- **No LICENSE file** (404-verified)
- **No SECURITY.md** despite kernel-level driver mode + AI API key handling
- **No tests/ visible**
- **No CI badges** visible
- **No multi-OS** (Windows-only hard pin)
- **No mobile / browser-extension** (desktop-only)
- **No SaaS tier** (pure free-with-donations)
- **No telemetry / no signup / no watermark / no ads** (perpetually-free positioning)
- **No Discord / Telegram community channel** (despite Telegram as feature)
- **No agent-framework consumption** (this is end-user app, not framework for agents)

→ Absences consistent with **solo developer indie product** profile at small-scale (17 stars). Reinforces tier classification as T5 Application.
