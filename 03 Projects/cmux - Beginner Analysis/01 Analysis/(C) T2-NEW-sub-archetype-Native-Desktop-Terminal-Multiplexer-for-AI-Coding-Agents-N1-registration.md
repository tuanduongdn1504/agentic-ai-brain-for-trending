# (C) PHASE 4b PRIMARY — NEW T2 sub-archetype "Native-Desktop Terminal Multiplexer for AI Coding Agents" PROVISIONAL N=1

**Vehicle:** Routine v2.3 §3 Phase 4b vehicle #2 (sub-archetype proposal-document)
**Subject anchor:** v99 manaflow-ai/cmux
**Confidence:** HIGH (structural-membership load-bearing; 5-criterion PASS)
**Promotion timeline:** v100 first-cycle stale-check + v104 N=2 watch + v109 5-wiki retire-watch + v114 10-wiki retire-check + v114 15-wiki forced-retire if N=1-only

---

## Why a NEW sub-archetype (not Library-vocab, not within-pattern strengthening, not existing sub-archetype)

cmux's structural-membership is load-bearing — the subject IS the archetype, not a methodology axis that happens to apply to it. Library-vocab vehicle inappropriate because:

- Methodology-axis vs structural-axis: cmux's terminal-multiplexer-for-AI-coding-agents identity is a structural property (a kind of T2 service), not a discipline/frame/measurement-axis
- Cross-wiki vocabulary use: vocabulary like "vertical tabs + notifications + concurrent agent sessions" doesn't generalize as a corpus-wide vocabulary item the way "Token-Economy-Quantification" or "Engagement-Deficit-Extreme" do

Within-pattern strengthening for an existing T2 sub-archetype also inappropriate — cmux does not fit any of the 6 prior T2 sub-archetype instances:

| Prior T2 instance | Sub-archetype | Why cmux differs |
|---|---|---|
| v66 agentmemory | Memory-system-service | cmux has no memory primitives; orthogonal layer |
| v70 codegraph | Code-index-service / MCP server backend | cmux has no code-indexing; terminal not MCP |
| v73 cc-switch | Provider-management-aggregator (multi-runtime) | cc-switch manages providers within single client; cmux hosts multiple full agent sessions |
| v85 ui-ux-pro-max-skill | Design-skill T2 hybrid | UI domain not orchestration domain |
| v89 VibeCodingTracker | AI-agent observability/metering | passive observation not active session-hosting |
| v97 distill | CLI compression-tool with bundled local LLM | pipe-stage tool not session host |

cmux's load-bearing role is **active multi-session AI-agent orchestration at native-desktop scale** — a category prior T2 instances do not occupy.

---

## 5-criterion definition (PASS evaluation)

A subject qualifies as **T2 sub-archetype "Native-Desktop Terminal Multiplexer for AI Coding Agents"** when ALL FIVE criteria PASS:

### Criterion 1: Native-desktop platform (not web/CLI/cross-platform)

cmux ships as native macOS app: Swift 81.9% + AppKit + Xcode workspace + 4 distinct `.entitlements` files (cmux + cmux-helper + cmux.nightly + cmux.release) + Sparkle auto-update + Homebrew Cask + DMG distribution. No web build, no CLI-primary surface (CLI is auxiliary), no cross-platform Electron/Tauri wrapper.

**PASS.**

### Criterion 2: Terminal-multiplexer role at top-level UX (not single-shell terminal)

cmux's primary UX is the terminal-multiplexer layer: vertical tabs + horizontal tabs + per-tab git/PR/port metadata + tab grouping. Single-shell terminals (Ghostty itself, iTerm2, Apple Terminal) lack this multi-tab-with-metadata top-level affordance. `tmux` in repo topics underscores the multiplexer positioning.

**PASS.**

### Criterion 3: Multi-agent-session-hosting (concurrent multi-agent occupancy)

README enumerates 13 supported AI coding agents (Claude Code + Codex + Grok + OpenCode + Pi + Amp + Cursor CLI + Gemini + Rovo Dev + Copilot + CodeBuddy + Factory + Qoder); the product's positioning is hosting these as **concurrent** session occupants. Notification rings + attention panels exist specifically to manage multi-session attention-routing.

**PASS.**

### Criterion 4: Substrate-tolerance via embedded terminal engine (not custom-built rendering)

cmux embeds **libghostty** for terminal rendering with Ghostty config compatibility + GPU-accelerated rendering. The subject doesn't reinvent terminal emulation; it tolerates an upstream substrate (Mitchell Hashimoto's Ghostty) while specializing the orchestration layer.

Cross-reference: Pattern #84 84d Hardware-Substrate-Tolerance N=3 PROMOTION-ELIGIBLE administrative at v100 audit gains v99 as **N=4 STRONGER PROMOTION-ELIGIBLE** strengthening (v79 PyTorch-Metal-MPS + v94 WASM + v97 MLX-Apple-native + v99 native-macOS-Swift-AppKit-with-libghostty-embed).

**PASS.**

### Criterion 5: Attention-signaling primitives at top-level UX

cmux's notification rings + side panels exist specifically to signal "agent X needs attention" across concurrent sessions. This is structurally distinct from generic OS notifications: rings are per-tab-positional + panels surface agent-context inline. The attention-routing problem is itself product-distinct to multi-agent-hosting.

**PASS.**

---

## Cross-axis spread (single instance — N=1)

| Axis | Value |
|---|---|
| Author | manaflow-ai (Lawrence Chen + Austin Wang, SF founders, Yale + NASA JPL + Chess.com lineage) |
| Vertical | Native-macOS terminal multiplexer |
| Scale | 19.9K stars (MEDIUM-HIGH) |
| Velocity-class | Pattern #52 HIGH-NOT-EXTREME 166.8/d (already CONFIRMED top-level) |
| License | GPL-3.0-or-later + commercial dual-license (CORPUS-FIRST) |
| Primary language | Swift 81.9% (CORPUS-FIRST in v60+ window) |
| Geographic | SF (US-LOCATED) |

Cross-axis spread evaluation deferred to N=2 emergence (per routine v2.3 §2 promotion ladder). At N=1 PROVISIONAL the structural criteria alone are load-bearing.

---

## N=2 emergence path

Candidate future instances within 15-wiki retire window:

1. **Warp Terminal** — Rust-primary native macOS terminal with AI features (would shift criterion 1 from Swift to Rust + still PASS criterion 2-5; cross-author + cross-language strengthening)
2. **Wave Terminal** — TypeScript/Go web-tech native terminal (would FAIL criterion 1 native-desktop, would route to NEW sub-archetype "Web-Tech Native-Desktop Terminal for AI Coding Agents" or merge with this one)
3. **Some Linux GTK4/Qt-native terminal multiplexer for AI agents** — would extend criterion 1 beyond macOS
4. **Windows-native terminal for AI agents** — same

If N=2 emerges at cross-author + cross-language + cross-OS, full N=3 PROMOTION-LOCKED-IN with formal sub-archetype taxonomy expansion is achievable at v104-v110.

If no N=2 by v114, forced-retire per routine v2.3.1 §2 + §18 retire cadence.

---

## Promotion ladder (per routine v2.3.1 §2)

| Stage | N | Status | Audit action |
|---|---|---|---|
| Registration | 1 | **PROVISIONAL N=1 at v99** | First-cycle stale-check at v100 audit |
| Strengthening | 2 | PROVISIONAL N=2 STRENGTHENING | Watch for N=3 promotion-eligibility |
| Promotion-eligibility | 3 | N=3 PROMOTION-ELIGIBLE | Evaluate at audit for CONFIRMED |
| Stronger eligibility | 4 | N=4 STRONGER PROMOTION-ELIGIBLE | Default PROMOTE at audit |
| CONFIRMED | ≥3 (with cross-author + cross-language preferred) | CONFIRMED sub-archetype | Standalone T2 taxonomy item |

**Retire cadence**: 5-wiki stale-watch (v104) + 10-wiki retire-check (v109) + 15-wiki forced-retire (v114).

---

## Adjacent observations (NOT load-bearing for this proposal but flagged for v100 audit)

These are secondary observations that this proposal does NOT promote; they may become standalone Library-vocab PROVISIONAL N=1 registrations in the wiki state-block but are NOT load-bearing for the T2 sub-archetype proposal:

1. **NEW Library-vocab "21-Locale README Distribution at Native-Desktop Product Scale" PROVISIONAL N=1** — CORPUS-RECORD locale-breadth exceeding v77 13-locale + v78 ECC 10-locale prior records by ~60%
2. **NEW Library-vocab "GPL-3.0-or-later + Commercial Dual-License at Single Subject" PROVISIONAL N=1** — distinct from v78 ECC OSS-with-hosted-Pro-SaaS-tier-on-MIT-base (RETIRED at v96) + v98 Apache+CC-BY Inter-License Boundary
3. **NEW Library-vocab "AI-Code-Review-CI-Tooling-at-AI-Coding-Agent-Product-Subject" PROVISIONAL N=1** — `.coderabbit.yaml` + `.greptile` at subject that produces AI-coding-agent infrastructure = meta-recursive AI-tooling-on-AI-tooling
4. **NEW Library-vocab "Native-Macos-Apple-Dev-Toolchain at AI-Agent-Tooling Subject" PROVISIONAL N=1** — Xcode workspace + 4 entitlements files + Sparkle + Homebrew Cask at AI-agent product
5. **NEW Library-vocab "Composable-Primitives-Over-Prescriptive-Workflows Philosophy" PROVISIONAL N=1** — anti-prescriptive architectural framing distinct from Pattern #51 vibe-coding-spectrum
6. **Pattern #57 sub-variant agentskills.io Standards-Conformance-Layer Corpus-Recursive Chain N=2 STRENGTHENING** — v98 introduced as PROVISIONAL N=1 (3-implementer); v99 = 4-implementer extension = strengthening at sub-variant layer (v76 anchor + v93 authoritative + v98 cybersecurity + v99 native-terminal)
7. **Pattern #84 84d Hardware-Substrate-Tolerance N=4 STRONGER PROMOTION-ELIGIBLE** administrative at v100 (was N=3 PROMOTION-ELIGIBLE at v97; v99 adds 4th cross-substrate instance: native-macOS-Swift-AppKit-with-libghostty-embed)
8. **Library-vocab #12 LLM-routing artifacts (CONFIRMED N=5) further strengthening** — AGENTS.md + CLAUDE.md + THIRD_PARTY_LICENSES.md + `skills/` directory all present

These adjacent observations are inventoried in the wiki Subject + state-block but do NOT receive their own Phase 4b proposal-documents at v99 ship (cascade-discipline per routine v2.3.1 §25 sub-axis registration rate-limit).

---

## Conclusion

PROVISIONAL N=1 registration of T2 sub-archetype **"Native-Desktop Terminal Multiplexer for AI Coding Agents"** filed against v99 anchor. v100 first-cycle stale-check + v104 N=2 watch + v114 forced-retire deadline if N=1-only. Adjacent observations inventoried but NOT promoted at v99 to preserve cascade-discipline.
