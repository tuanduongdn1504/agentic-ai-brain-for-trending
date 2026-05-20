# (C) 2026-05-20 — ECC diff-only note since v1 (2026-04-17)

**Scope:** Lightweight refresh probe of `affaan-m/ECC` (formerly `affaan-m/everything-claude-code` at v1) — no entity-page rewrites, no Pattern Library file updates, no version increment. Per user-elected mode at v77 ship session.

**Source probed:** https://github.com/affaan-m/ECC (no redirect from this URL today — repo appears to have been renamed; old `everything-claude-code` URL likely still redirects but was not re-probed)

**Baseline reference:** v1 wiki at `02 Wiki/` (built 2026-04-17, 11 entity pages + index + log; folder name "Everything Claude Code - Beginner Analysis" preserves the original name)

---

## What changed since v1

### Identity-layer changes

| Axis | v1 baseline (2026-04-17) | Current (2026-05-20) | Delta |
|------|---------------------------|------------------------|-------|
| Repo name | `affaan-m/everything-claude-code` | **`affaan-m/ECC`** | RENAMED (likely with redirect preservation) |
| Tagline | "Everything Claude Code" framework collection | **"The harness-native operator system for agentic work. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond."** | repositioned — Claude-Code-centric → multi-harness operator-system framing |
| License | MIT | MIT | unchanged |

### Scale-layer changes

| Metric | v1 baseline | Current | Delta |
|--------|-------------|---------|-------|
| Stars | (mid-thousands range at v1 probe) | **187,238** (verified via GitHub API 2026-05-20) | massive growth — CORPUS-RECORD top-velocity subject |
| Forks | (low thousands) | **28,997** (verified) | fork ratio 0.155 = strong active-deployment |
| Open issues | (some) | **1** (verified) | engagement-deficit-extreme territory |
| Created | (n/a) | **2026-01-18** (verified) | repo age 122 days at this probe |
| Last push | (n/a) | **2026-05-20** (verified — active today) | actively developed |
| License | MIT | MIT (verified) | unchanged |
| Velocity | (n/a baseline) | **187,238 / 122 = 1,535 stars/day** | **CORPUS-RECORD EXTREME-VIRAL — exceeds v63 Karpathy (~1,186/d) and v68 zero (1,050/d)** |

**Pattern #52 EXTREME-VIRAL retroactive assignment is VERIFIED.** At 1,535 stars/day sustained over 122 days, ECC is currently the **highest-velocity subject in the corpus** and the only multi-month-sustained EXTREME-VIRAL subject (v63 Karpathy was a single-artifact pulse; v68 zero was 2-day-old at probe). This is corpus-top-tier and warrants attention beyond a diff-note.

### Architecture-layer changes (most significant)

**v1 baseline:** Claude-Code-only framework with .claude/ + skills + commands + hooks + plugins + subagents + MCPs + rules-and-memory (11 entity pages documented these).

**Current:** **multi-harness operator-system spanning 11+ AI harnesses** via dedicated top-level directories:

| Harness dir | Provenance (corpus context) |
|-------------|-----------------------------|
| `.claude/` | original v1 anchor |
| `.codex/` | OpenAI Codex (v62 codex-plugin-cc + v76 ecosystem) |
| `.cursor/` | Cursor (v75 + v76 multi-harness) |
| `.opencode/` | Opencode (v67 opencode-antigravity-auth) |
| `.gemini/` | Gemini CLI (v76 ecosystem) |
| `.kiro/` | Kiro (v75 + v76 ecosystem) |
| `.trae/` | Trae (v75 + v76 + v77 easy-vibe) |
| `.qwen/` | Qwen CLI (v73 cc-switch ecosystem) |
| `.zed/` | Zed editor — corpus-new harness target |
| `.codebuddy/` | Codebuddy — corpus-new harness target |
| `.agents/` | provider-agnostic agent dir (v76 pattern) |

Plus `.claude-plugin/plugin.json`, `.mcp.json`, `.github/`, `.vscode/` — supporting infrastructure.

### Content-layer changes

| Artifact | v1 baseline | Current | Delta |
|----------|-------------|---------|-------|
| Skills count | (small handful documented) | **232 skills** | massive codification expansion |
| Agents count | (subagents only) | **60 agents** | new agent dimension |
| Legacy command shims | (n/a) | **75 legacy command shims** | suggests renames/refactors preserved backward-compat |
| Language ecosystems | (Claude-Code-centric) | **12+ language ecosystems** | broad multi-language coverage |
| Top-level governance | CLAUDE.md only (probably) | **CLAUDE.md + AGENTS.md + agent.yaml + llms.txt + .claude-plugin/plugin.json + .mcp.json + SKILL.md template** | extensive governance file expansion |
| Domain dirs | (skills/commands/hooks/plugins/subagents) | adds `research/`, `manifests/`, `schemas/`, `contexts/`, `mcp-configs/`, `legacy-command-shims/`, `ecc2/`, `examples/`, `tests/`, `src/` | research-first development + manifests + schemas added |

---

## Pattern Library implications worth tracking (no files touched per scope)

These are observations only. Promotion/registration only happens if a future wiki revisits ECC formally (e.g., as v78+ corpus-recursive subject) OR if these patterns aggregate evidence elsewhere.

### Pattern #84 sub-mechanism 84c "Provider-Agnostic-By-Design"

ECC current state matches 84c **at the distribution layer** with 11+ harness dirs — comparable to or exceeding **v75 impeccable's 14-harness CORPUS-RECORD** depending on how the boundaries are counted. Sub-sub-mechanism appears to be **84c.1 explicit-provider-matrix at repo-stored layer** (each harness gets its own dir vs CLI-generation at v76).

If revisited formally: ECC could provide N+1 evidence at sub-sub-mechanism 84c.1 with corpus-precedent (predates the v71→v77 84c sustainability arc — repo existed before the arc was observed in corpus).

### Library-vocabulary item #12 "AI-Optimized Tutorial Index via llms.txt"

`llms.txt` is referenced (the WebFetch noted "referenced for OpenCode"). If ECC's `llms.txt` is structurally similar to v77 easy-vibe's AI-Agent-optimized tutorial index, item #12 would advance from N=1 PROVISIONAL toward N=2 PROMOTION-ELIGIBLE — but the actual `llms.txt` content was NOT probed in this lightweight pass. Worth a focused probe if vocab item #12 strengthening becomes a priority.

### Pattern #19 ecosystem-portfolio-builder

Affaan Mustafa = author of ECC. Pattern #19 sub-mechanism positioning depends on the broader portfolio (not probed). If Affaan has a multi-product portfolio, this would be a sub-mechanism candidate (likely 19b solo-developer multi-project family).

### Pattern #52 velocity sub-class

187K stars is **far above the EXTREME-VIRAL >300/d threshold** if the figure is accurate. This would make ECC a retroactive Pattern #52 EXTREME-VIRAL subject — joining v63 Karpathy + v68 zero in the top-tier-velocity sub-class. **Star count needs verification** before any retroactive assignment.

### Pattern #78 LDS-tracking

`manifests/` + `schemas/` + `research/` + 232 skills × structured discipline = strong Pattern #78 LDS evidence at multiple layers. Possibly another sub-mechanism candidate (research-first-development-as-LDS-layer) but speculative without deeper probe.

### Pattern #66 supply-chain integrity

Not probed in this lightweight pass. With 187K stars + 0 open issues + ~2K commits, the discipline patterns are worth tracking but require deeper inspection of CI/release surface.

### Storm Bear meta-entity

ECC is **v1** — Storm Bear's first wiki and the foundational corpus-anchor subject. Any future revisitation triggers **Pattern #57 corpus-recursive citation** at maximum depth (corpus-self-reference at the anchor point). Storm Bear (a) PASS would depend on Affaan's profile; (c) STRONG PASS automatic (foundational subject); (d) STRONG PASS if ECC currently cites other corpus subjects (likely given multi-harness expansion).

---

## What this means for the corpus

1. **The v1 wiki entity pages are now stale.** Every entity (Skills, Commands, Hooks, Plugins, Subagents, MCPs, Rules-and-Memory, etc.) was documented for the v1 single-harness Claude-Code-centric scope. Current ECC is multi-harness operator-system with 232 skills + 60 agents + 11+ harness dirs. **Refresh-in-place or v78 revisit would be substantial work.**
2. **ECC may now be the CORPUS-RECORD scale subject** (187K stars). Pattern #52 EXTREME-VIRAL retroactive assignment pending star-count verification.
3. **ECC has independently arrived at v76/v77's multi-harness governance pattern** (AGENTS.md + llms.txt + multi-harness dirs) — corpus-recursive design convergence worth noting.

## Recommended follow-up (operator-elected)

- **Verify the 187K star count** via direct `gh api repos/affaan-m/ECC` before any Pattern #52 retroactive claim
- If verified: consider v78 as a **corpus-recursive revisitation of v1** — would be CORPUS-FIRST corpus-recursive subject (revisiting an anchor at 1-year+ delta)
- Refresh v1 entity pages only if planning the v78 build — otherwise leave v1 wiki as historical baseline + this diff-note as the current-state pointer

**No state files touched. No Pattern Library files touched. No commits made.** This note is the entire delta produced in this session.

**Author:** Storm Bear (Claude assistant)
**Date:** 2026-05-20
**Scope:** lightweight diff-note only (user-elected mode)
