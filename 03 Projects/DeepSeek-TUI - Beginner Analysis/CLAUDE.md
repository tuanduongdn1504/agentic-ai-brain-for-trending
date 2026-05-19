# Hmbown/DeepSeek-TUI — v72 Wiki

## Subject Overview

**Repository:** https://github.com/Hmbown/DeepSeek-TUI
**Author:** Hmbown (solo developer, individual GitHub user; not DeepSeek employee — community-built canonical client)
**Homepage:** https://deepseek-tui.com/
**Created:** 2026-01-19 (120 days old as of wiki-build 2026-05-19)
**Stats:** 32,114 stars | 2,729 forks | 427 open issues | 135 watchers (subscribers)
**Velocity:** **267.6 stars/day** — **HIGH-NOT-EXTREME velocity sub-class** (150-300/day sustained ≥30 days; below Pattern #52 >300/d EXTREME-VIRAL threshold)
**Fork ratio:** 0.085 (engagement-strong; below 0.15 HIGH-deployment threshold but well above corpus-median)
**License:** MIT | **Language:** Rust
**Topics:** cli, deepseek, llm, rust, terminal, tui

**Description:** Terminal coding agent for DeepSeek V4 models. Runs as `deepseek` (CLI dispatcher) → `deepseek-tui` (companion ratatui TUI). 1M-token context, streaming reasoning blocks, OS-level sandbox (Seatbelt/Landlock/Job Objects), durable task queue, sub-agent pool, MCP integration, multi-provider (9+ providers), CJK trio + pt-BR localization, 5 packaging methods (npm + cargo + Homebrew + Docker + direct download), bundled starter skills.

**Corpus position:** v72 (continuing 71-wiki series; 5th corpus T1 skill/framework entry; Storm Bear meta-entity slot 4)

---

## 13-Axis Classification (Phase 0)

| Axis | Classification | Notes |
|------|---|---|
| **Tier** | T1 (assistant skill/framework) | Coding agent + bundled starter skills + MCP server integration |
| **Archetype** | solo-community | Individual developer (Hmbown); community-built canonical client for DeepSeek API |
| **Scale** | 20-60K stars tier | 32,114 stars (within 20-60K bracket) |
| **Primary Language** | Rust | Workspace declares `rust-version = "1.88"`; uses 2024 edition + let_chains |
| **Packaging** | npm + cargo + Homebrew + Docker + direct download (5 methods) | npm wrapper downloads Rust binaries; cargo from crates.io; Homebrew tap; Docker GHCR; direct GitHub Releases — **corpus-record packaging breadth** |
| **Origin story** | individual-author / community-led-vendor-product | Solo dev builds best-experience client for a vendor's API model series; pseudonymous-likely (Hmbown handle) — no public corporate affiliation |
| **Methodology** | Feature-framework prescriptive + agentic SDD | 3 modes (Plan/Agent/YOLO) + reasoning-effort tiers (off/high/max) + sub-agent pool + RLM batch sessions + summary-first tools + session-longevity discipline |
| **Governance file count** | Extensive (7+ files; possibly 20+ in docs/) | AGENTS.md + CONTRIBUTING.md + CODE_OF_CONDUCT.md + SECURITY.md + 20+ docs/ files (ARCHITECTURE / INSTALL / CONFIGURATION / MODES / SUBAGENTS / MCP / KEYBINDINGS / ACCESSIBILITY / DOCKER / LOCALIZATION / MEMORY / TOOL_SURFACE / OPERATIONS_RUNBOOK / RELEASE_CHECKLIST / etc.) |
| **Agent/skill count** | 11 bundled starter skills + extensible skills system | skill-creator + mcp-builder + plugin-creator + v4-best-practices + documents + presentations + spreadsheets + pdf + feishu + skill-installer + delegate |
| **i18n** | EN + zh-CN + ja-JP + pt-BR (4 locales; auto-detection) | CJK trio + Latin (Portuguese-Brazilian) coverage; corpus-record locale breadth for T1 skill subject |
| **Intellectual influence** | DeepSeek API substrate + Claude-Code methodology echoes | DeepSeek V4 model docs + OpenAI-compatible API conventions; Plan/Agent/YOLO mode taxonomy echoes Claude Code; multi-provider abstraction layer |
| **Agent platforms** | Standalone TUI (not a plugin); HTTP/SSE runtime API (`deepseek serve --http`) for headless workflows | Self-contained agent; can serve other clients via runtime API |
| **Living-Domain-Standards** | YES (Pattern #78) | DeepSeek API + OpenAI-compatible API spec + MCP protocol + LSP protocol (rust-analyzer / pyright / typescript-language-server / gopls / clangd) + Rust 2024 edition + Cargo registry conventions + OSC notification protocols (OSC 9 / OSC 99 / OSC 777) |

---

## Pattern Library Pre-Check (Phase 0)

### Pattern #52 (CANDIDATE) — Sustained-Velocity (HIGH-NOT-EXTREME sub-class)
- **v72 audit context (2026-05-19):** Pattern #52 3-tier velocity sub-classification REGISTERED at v72 audit (EXTREME-VIRAL >300/d + **HIGH-NOT-EXTREME 150-300/d** + SUSTAINED-MODERATE-HIGH 25-150/d). Top-level promotion DEFERRED to v75 awaiting "N=2 within HIGH-NOT-EXTREME or SUSTAINED-MODERATE-HIGH sub-classes."
- **v72 evidence (this wiki):** DeepSeek-TUI = **N=2 within HIGH-NOT-EXTREME sub-class** (267.6 stars/day × 120 days = 150-300/d sustained ≥30 days threshold satisfied; joins v69 CloakBrowser N=1 at 172.7/d × 86d)
- **Promotion path:** v75 audit can now PROMOTE Pattern #52 with HIGH-NOT-EXTREME sub-class N=2 evidence per v72-set criteria. **FIRST POST-v72-AUDIT POLICY SATISFACTION in corpus history.**
- **Strength:** HIGH-NOT-EXTREME 267/d at 120d is more sustained-mid-life-cycle than CloakBrowser's 172.7/d at 86d, validating the sub-class as discriminating between viral-launch (EXTREME-VIRAL) and organic-high-growth (HIGH-NOT-EXTREME) dynamics.

### Pattern #84 (CONFIRMED v72) — Cross-Vendor Ecosystem-Tolerance — 84c FIRST POST-PROMOTION STRENGTHENING
- **v72 audit context:** Pattern #84 PROMOTED to CONFIRMED at v72 audit with sub-taxonomy 84a/84b/**84c Provider-Agnostic-By-Design**. v72 audit warned: "If any sub-mechanism fails to reach N=2 within 4 wikis post-promotion (v76), reformulate Pattern #84 to retire the unsupported sub-mechanism."
- **v72 evidence (this wiki):** DeepSeek-TUI supports 9+ providers explicitly: **DeepSeek** (primary) + **NVIDIA NIM** + **AtlasCloud** + **OpenRouter** + **Novita** + **Fireworks** + **Generic OpenAI-compatible** + **SGLang** (self-hosted) + **vLLM** (self-hosted) + **Ollama** (self-hosted) = **9-provider matrix** beyond v71 agents-best-practices dual-vendor synthesis
- **Sub-typology variant:** v71 was dual-vendor-synthesis (Anthropic + OpenAI); v72 DeepSeek-TUI is **9-provider-matrix** — quantitative escalation within 84c sub-mechanism. Could establish 84c1 "dual-vendor-synthesis" + 84c2 "n-provider-matrix" sub-mechanisms.
- **Significance:** **FIRST POST-v72-AUDIT 84c STRENGTHENING IN CORPUS HISTORY.** Validates v72 audit's 84c registration immediately post-promotion (within 0 wikis). N=2 within 84c reached at v72 wiki itself — fastest sub-mechanism N=2 in corpus history.

### Pattern #21 (CONFIRMED) — SDD Methodology — within-pattern strengthening
- **v72 evidence:** Explicit 3-mode taxonomy (Plan / Agent / YOLO) + reasoning-effort tiers (off / high / max) + sub-agent coordination pattern + RLM (REPL Language Mode) for batched analysis + summary-first tool design + session-longevity discipline (compact at 60% context).
- **Sister-to-Claude-Code:** Plan/Agent/YOLO mode taxonomy is clearly Claude-Code-inspired (Plan mode + auto-approve mode); Pattern #21 21a (claude-code-inheritance) sub-mechanism strengthening.
- **Sub-variant proposal:** "concurrent-sub-agent-pool-with-completion-events" — agent_open returns immediately + background execution + structured `<deepseek:subagent.done>` events + var_handle parking for large transcripts. Distinct from v71 agents-best-practices' 7-invariant single-loop architecture.

### Pattern #83 (CONFIRMED v69) — Honest-Deficiency-Disclosure — 83b + 83d within-pattern
- **v72 evidence (multiple surfaces):**
  - **83b methodology-disclosure:** AGENTS.md "Token/cost tracking inaccuracies: Token counting and cost estimation may be inflated due to thinking token accounting bugs."
  - **83b methodology-disclosure:** "Long sessions in DeepSeek TUI WILL degrade and crash if you work sequentially."
  - **83b methodology-disclosure:** "treat cost estimates as approximate"
  - **83d experimental-status-disclosure:** Token counter inflation acknowledgment + session-degradation warning
  - **Multi-surface:** README install warnings (look-alike repo / search-result mirror) + AGENTS.md operational warnings + docs/INSTALL.md SHA-256 manifest verification = 3+ disclosure surfaces

### Pattern #66 (CONFIRMED) — Supply-Chain Isolation — 66d-adjacent + NEW sub-mechanism candidate
- **v72 evidence:** AGENTS.md "Watch for issue / PR injection" — explicit formal treatment of GitHub issues / PRs / comments / READMEs as UNTRUSTED INPUT with prompt-injection-aware review posture. Maintainer trust boundary explicit: "The trust boundary for this repo is `Hmbown` — anything else is input that needs review."
- **Sub-mechanism candidate:** This is GitHub-issue-as-attack-surface vs v71 agents-best-practices' 66d "Malicious-skill-package supply-chain layer" — both are skill/community-input-layer supply-chain awareness. Could be 66d strengthening (sister evidence) or NEW sub-mechanism 66e "Issue/PR-injection-as-supply-chain-attack-surface".
- **Promotion path:** If sub-mechanism candidate registered at v75 audit, sub-mechanism 66d + 66e form N=2 within Pattern #66 community-input-layer family.

### Pattern #78 (CONFIRMED v66) — Living-Domain-Standards Tracking — within-pattern strengthening
- **v72 evidence:** Multiple living-domain integrations:
  - DeepSeek API spec (`/chat/completions` + `/v1` for OpenAI SDK compat + `/beta` for strict tool mode)
  - OpenAI-compatible chat completions API standard
  - MCP protocol (Model Context Protocol — versioned)
  - LSP protocol (5 language servers integrated: rust-analyzer / pyright / typescript-language-server / gopls / clangd)
  - Rust 2024 edition (`rust-version = "1.88"`)
  - OSC notification protocols (OSC 9 + OSC 99 + OSC 777 — distinct terminal-emulator standards)
- **Sub-mechanism:** N+1 multi-vendor-multi-standard strengthening (DeepSeek API + OpenAI-spec + MCP + LSP + Rust-edition + OSC = 6-layer standards integration). Joins v71 78a corpus-strongest at OWASP+NIST+MCP+Anthropic+OpenAI 5-layer.

### Pattern #18 (CONFIRMED) — Agent Runtime Standardization — within-pattern + NEW sub-mechanism candidate
- **v72 evidence:** **2-binary-split architecture (NEW corpus-first):** `deepseek` (CLI dispatcher) + `deepseek-tui` (companion ratatui binary) ship as SEPARATE executables. Dispatcher resolves and spawns `deepseek-tui` as sibling on PATH for interactive use. AGENTS.md notes: "Two binaries, two installs... installing only the CLI leaves the TUI stale and your fix won't appear to run."
- **Distinct from v70 codegraph's MCP B1 variant:** Not a backend-service split — this is **dispatcher-companion-binary-split** architecture. Could be NEW sub-mechanism C "dispatcher-companion-binary-split" within Pattern #18 shared-backend-service sub-archetype OR independent sub-mechanism.

### NEW Candidate? — Community-Built-Canonical-Vendor-Client (CBCVC)
- **Definition:** Solo individual developer builds vendor-product-quality terminal/desktop client for a specific vendor's API, becoming de-facto canonical client (32K+ stars at scale of vendor-official) while remaining independent from vendor employment/sponsorship.
- **v72 evidence:** Hmbown's DeepSeek-TUI — community-built canonical DeepSeek API client at 32K stars (vendor DeepSeek published their own platform but the SOLO community version achieves canonical-client status).
- **Corpus-first?** Need to compare with prior corpus subjects. v62 codex-plugin-cc (OpenAI publishes plugin FOR Claude Code) is REVERSED — vendor publishes for rival. v65 claude-code-system-prompts (Piebald-AI reverse-engineers Anthropic Claude Code) is reverse-engineering archive. v72 DeepSeek-TUI is COMMUNITY-BUILT BEST-EXPERIENCE-FOR-VENDOR — different mechanism. Likely corpus-first as distinct OC candidate.
- **Recommended action:** Register as NEW observational candidate OC-P "Community-Built-Canonical-Vendor-Client" pending v75+ evaluation.

---

## Phase 4b PRIMARY Routing

**File:** `01 Analysis/(C) Pattern-52-HIGH-NOT-EXTREME-velocity-N2-sub-class-strengthening-evaluation.md`

**Route:** Pattern #52 HIGH-NOT-EXTREME sub-class N=2 evaluation — **FIRST POST-v72-AUDIT POLICY SATISFACTION IN CORPUS HISTORY** (v72 audit deferred Pattern #52 promotion to v75 awaiting "N=2 within HIGH-NOT-EXTREME or SUSTAINED-MODERATE-HIGH sub-classes"; v72 wiki provides that evidence within 1 day of audit completion)

**Content:**
- Pattern #52 v72 audit context + 3-tier sub-classification background
- HIGH-NOT-EXTREME sub-class N=1 → N=2 evidence (v69 CloakBrowser + v72 DeepSeek-TUI)
- Sub-class promotion-criteria evaluation
- v75 audit path: HIGH-NOT-EXTREME N=2 → Pattern #52 top-level promotion eligible (criterion 4 variant-within-pattern)
- Sister-evidence relationship to EXTREME-VIRAL (karpathy/zero) + SUSTAINED-MODERATE-HIGH (codegraph)
- 1-wiki-rapid-evolution implication (sub-class registered v72 audit → N=2 evidence at v72 wiki = 0-wiki gap = Library-vocabulary item #10 corpus-record)

---

## Storm Bear (Phase 0.9)

**Meta-entity slot:** 4 (corpus-recursive analysis)
**Classification:** MODERATE INCLUDE (2/4 PASS)

| Criterion | Result | Evidence |
|---|---|---|
| (a) Author archetype peer | FAIL | Hmbown is solo developer with English-language handle; not VN/Asian-diaspora structural peer per criterion (a) strict definition |
| (b) Operational tool for vault | PASS | Directly deployable as alternative coding agent to Claude Code; provides vendor-diversification path for Storm Bear's heavy Anthropic-stack lock-in (per CLAUDE.md What's-not-working: "Tool lock-in moderate — heavy investment in Claude Code + Anthropic stack"); MIT-licensed; binary install via npm/cargo/Homebrew = zero infrastructure |
| (c) Methodology influence | PASS | AGENTS.md "Session Longevity (Critical)" + summary-first tool discipline + sub-agent coordination pattern + RLM batch sessions + 3-mode taxonomy (Plan/Agent/YOLO) + concurrent-sub-agent-pool architecture directly inform routine v2.3 design considerations + agentic-harness operational discipline |
| (d) In-corpus reference | FAIL | No explicit citation of corpus subjects detected; Claude-Code methodology echoes are inferred not cited; OpenAI-compatibility cited as protocol not as corpus subject |

**Recommendation:** MODERATE INCLUDE (meta-entity slot 4); deploy as VENDOR-DIVERSIFICATION pilot candidate for Storm Bear's coding work; routine v2.3 methodology-influence recognized particularly for session-longevity discipline + summary-first tool design.

**Streak status:** Storm Bear meta-entity streak extends to **8 consecutive PASS post-v64-RESET** (v65 STRONGEST + v66 STRONG + v67 MODERATE + v68 WEAK + v69 WEAK + v70 MODERATE + v71 MODERATE + **v72 MODERATE = streak=8; three consecutive MODERATEs**). MODERATE confirmed as modal-status (4/8 v65-v72).

---

## Cross-Wiki Siblings

- **v71 agents-best-practices** (T1 Assistant Skill) — Pattern #84 84c sister evidence (dual-vendor-synthesis vs DeepSeek-TUI's 9-provider-matrix); both Pattern #21 SDD methodology subjects; both Pattern #78 multi-vendor-multi-standard subjects
- **v70 codegraph** (T2 Service) — Pattern #18 sub-mechanism B sister evidence (codegraph = MCP B1 protocol-variant; DeepSeek-TUI = dispatcher-companion-binary-split distinct sub-mechanism candidate)
- **v69 CloakBrowser** (T2 Service) — Pattern #52 HIGH-NOT-EXTREME sub-class N=1 (172.7/d × 86d); DeepSeek-TUI = N=2 (267/d × 120d); **direct Phase 4b PRIMARY sister evidence**
- **v68 vercel-labs/zero** (T1 NEW sub-archetype) — Pattern #52 EXTREME-VIRAL adjacent (1,050/d at 2-3d); DeepSeek-TUI distinctly below EXTREME-VIRAL threshold; sub-class discrimination validated
- **v66 agentmemory** (T2 Service) — Pattern #18 sub-mechanism B B1 MCP variant; DeepSeek-TUI has MCP server integration as client (not server) — orthogonal
- **v65 claude-code-system-prompts** (T1 reference-archive) — Pattern #78 N=2 sister; both multi-vendor-multi-standard subjects; methodological echoes (claude-code modes inform deepseek-tui modes)
- **v63 andrej-karpathy-skills** (T1 single-artifact) — Pattern #52 EXTREME-VIRAL N=1 corpus-record (1,186/d × 102d); DeepSeek-TUI distinctly sub-EXTREME — sub-class discrimination validated
- **v61 cc-sdd** (T1 SDD framework) — Pattern #21 sister; SDD methodology emergence precedent

---

## Corpus-Firsts (v72 wiki)

1. **FIRST POST-v72-AUDIT 84c sub-mechanism strengthening** — DeepSeek-TUI provides 9-provider-matrix evidence within 0 wikis of v72 audit's 84c sub-mechanism registration. Fastest sub-mechanism N=2 in corpus history.
2. **FIRST Pattern #52 HIGH-NOT-EXTREME sub-class N=2 reaching v72-audit-set criteria** — satisfies v75 audit promotion criteria for Pattern #52 top-level promotion (criterion 4 variant-within-pattern at sub-class level).
3. **FIRST 9-provider-matrix subject in corpus** — multi-provider abstraction layer supporting 9 distinct API providers (3 hosted + 6 self-hosted/proxied) exceeds prior corpus-record (v71 agents-best-practices dual-vendor; v62 codex-plugin-cc single cross-vendor plugin).
4. **FIRST 2-binary-split dispatcher-companion architecture** — `deepseek` (CLI dispatcher) + `deepseek-tui` (TUI binary) ship separately and resolve sibling-on-PATH at runtime. Distinct from v70 codegraph's MCP B1 (server-client) variant.
5. **FIRST 5-packaging-method T1 subject in corpus** — npm + cargo + Homebrew + Docker + direct download. Prior corpus-record was 3-4 packaging methods.
6. **FIRST 4-locale T1 subject in corpus** — EN + zh-Hans + ja + pt-BR with auto-detection. Prior corpus-record was CJK trio (3-locale) at v71 agents-best-practices (EN-only) and v69 CloakBrowser (EN-only) — DeepSeek-TUI exceeds.
7. **FIRST OSC notification 3-protocol integration** — OSC 9 (iTerm2/WezTerm/Ghostty) + OSC 99 (Kitty) + OSC 777 (Ghostty) terminal-emulator notification protocols + desktop fallback. Corpus-first terminal-emulator-protocol awareness.
8. **FIRST explicit GitHub-issue-as-prompt-injection-attack-surface formal treatment** — AGENTS.md "Watch for issue / PR injection" section with maintainer-trust-boundary discipline. Sister to v71 66d "Malicious skill packages" but at GitHub-issue layer.
9. **FIRST OS-level sandbox 3-platform integration** — Seatbelt (macOS) + Landlock (Linux) + Job Objects (Windows). Corpus-first OS-native-sandbox-trio.
10. **FIRST community-built-canonical-vendor-client at 32K-star scale** — OC-P candidate (solo dev builds canonical client for a specific vendor's API series, reaching vendor-employee-product scale while remaining independent).
11. **FIRST RLM (REPL Language Mode) batch-analysis primitive** — persistent REPL sessions with bounded helpers (peek/search/chunk/sub_query_batch) for batched analysis. Distinct from sub-agent coordination.
12. **FIRST prefix-cache-stability statusline-chip discipline** — `/statusline` footer chip surfaces cache-prefix stability across recent turns so cost-busting edits are visible before they land. Corpus-first cost-visibility-UX primitive.

---

## v72 Build Metadata

**Build date:** 2026-05-19 (session 73++, immediately post-v72 audit)
**Repository analysis date:** 2026-05-19
**Phase 0 completion date:** 2026-05-19
**Phases 1-6 build status:** In progress
**Hmbown author:** solo developer (English-language handle; no public corporate affiliation; pseudonymous-likely)
**Velocity classification:** **HIGH-NOT-EXTREME sub-class N=2** (267.6 stars/day × 120 days = 150-300/d sustained ≥30 days threshold)
**Engagement signals:** fork_ratio 0.085 (strong-engagement, sub-HIGH-deployment threshold); 427 open issues = high active-deployment + maintainer engagement; 135 watchers (subscribers); CHANGELOG 272 KB = extreme release activity

---

## Files Created at v72

- CLAUDE.md (this file)
- COMMANDS.md
- 00 Sources/ (placeholder)
- 01 Analysis/
  - (C) open questions.md
  - (C) iteration-log.md
  - (C) Pattern-52-HIGH-NOT-EXTREME-velocity-N2-sub-class-strengthening-evaluation.md (Phase 4b PRIMARY)
- 02 Wiki/
  - (C) index.md
  - (C) log.md
  - (C) user-facing cluster summary.md
  - (C) contributor-facing cluster summary.md
  - (C) technical-distribution cluster summary.md
  - (C) entity-1-coding-agent.md
  - (C) entity-2-distribution-multi-provider.md
  - (C) entity-3-pattern-library.md
  - (C) entity-4-storm-bear.md
- 03 Published/
  - (C) DeepSeek-TUI - Huong dan cho nguoi moi.md
- 04 Reviews/ (placeholder)
- 05 Skills/ (placeholder)
- 06 Archive/ (placeholder)
- 07 Inbox/ (placeholder)

---

## Next Actions

1. Read remaining docs files (MODES.md, SUBAGENTS.md, MCP.md, ARCHITECTURE.md) for entity page completeness
2. Complete Phases 1-6 files in order: COMMANDS.md → foundational → cluster summaries → entity pages → beginner guide → Phase 4b primary → iteration log
3. Cross-link all entity pages and cluster summaries
4. Validate Pattern Library integrations (Pattern #52 HIGH-NOT-EXTREME N=2 + Pattern #84 84c N=2 within sub-mechanism)
5. Storm Bear meta-entity MODERATE 2/4 with vendor-diversification pilot recommendation
6. Phase 6 vault sync (CLAUDE.md state updates + active-candidates entries for OC-P + Pattern #84 84c strengthening note + Pattern #52 sub-class N=2)
