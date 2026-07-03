# (C) palmier-pro — Verdict

**GOAL-ALIGNED INCLUDE 3/4** [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG]
**1 NEW §C standalone at N=1 (CORPUS-FIRST for this conjunction)**
**Counts: 46/11 UNCHANGED** (no new top-level pattern, no CONFIRMED Library-vocab promotion this ship)

---

## (a) — Anthropic / cultural-peer axis

**FAILS cleanly.** Palmier, Inc. is a disclosed, funded (~$500K), 2-person YC S24 startup (Marcos Rico Peng + Harrison Tin, both fully disclosed, ex-LinkedIn/ex-Microsoft) — not Anthropic, no (a)-7 rescue available. No Anthropic partnership found on either side (verified directly). Claude is one of three equally-billed agent integrations (Codex, Cursor get the same MCP-config treatment in the README) — Goal #1 centers Claude specifically, and Palmier Pro does not. First "Palmier, Inc." author in the corpus → **#19 19a** data-point, matching the declared-non-Anthropic-funded-startup class (Jo Inc v179 / Kilo AI v177 / usestrix v190).

## (b) — Goal relevance (keys the tier)

**STRONG, not STRONGEST.**

STRONG because: it is Claude-first-class MCP infrastructure (an explicit `CLAUDE.md`/`AGENTS.md` pair, a one-line `claude mcp add` config, a Claude Desktop one-click install) that hands a coding agent a **genuinely new capability domain** — real, native, semantic control of a video-editing timeline (not screen-scraping, not gesture emulation) — exactly the "give the agent a new pair of hands" move this vault has valued in serve-sim v183 (iOS Simulator) and Agent-Reach v174 (web/social reach). More importantly for the operator's own stack: it is a **concrete, source-verified architectural template for the exact move hireui would need to make to become "agent-native"** — a `ToolExecutor` dispatcher mapping ~51 well-scoped MCP tools onto a real domain model, a `.agents/skills`-reading in-app agent chat, and a clean open-core split between the free product surface and the paid AI backend. That's directly reusable knowledge for Goal #2, regardless of the video-editing vertical.

Not STRONGEST because: the *domain* is video editing, not software development; it's third-party commercial software (GPLv3 core + a paid, closed generative-AI cloud backend); Claude is one of three equally-supported agent integrations, not the center of the product; and it requires a real install (a native macOS app, Apple-Silicon + macOS-26-only) rather than a `pip`/`npm` one-liner. Calibrates below OpenMontage v188's (b) STRONG (which was rated *"arguably a STRONGER (b) than ai-berkshire's"* for landing on five operator pilot threads at once) and roughly level with serve-sim v183's (b) STRONG (a comparable "new capability domain for the agent" move, comparable install friction).

## (c) — Substance

**STRONG.** ~325 Swift files, a genuinely production-grade three-subsystem architecture (editor / agent-MCP / generation), 13.9K lines of tests across 90+ files with the MCP tool layer itself the single best-tested subsystem (1,885-line `ToolExecutorTests.swift`), Metal-shader compositing, SigLIP2 Core ML visual search, a real CI pipeline, signed+notarized distribution with auto-update. Honest caveats foregrounded: acknowledged-early product (~3 months old, missing transitions/masking/graphics per the team and Hacker News), zero published benchmarks, an undocumented Sentry telemetry consent flow (opt-out-default-on, not disclosed in the README — a doc-vs-code gap), no checksum/signature on the distributed DMG, and a narrow platform footprint (macOS 26 + Apple Silicon only).

## (d) — Cross-references

**STRONG.** Lands cleanly on several existing corpus threads without duplicating any of them exactly:
- **OpenMontage v188** (Agent-First End-to-End Generative-Media Production System) — same broad "AI video production" theme, opposite architecture (there, the coding agent *is* the runtime with no separate GUI app; here, a full human-usable GUI app *is* the runtime and the agent is an optional MCP-driven peripheral).
- **serve-sim v183** (Agent-First Mobile-Simulator Perception+Control Layer) — the closest mechanical cousin ("give an agent hands on a native app it doesn't own the internals of"), but serve-sim gets there via *screen capture + gesture emulation* over a simulator, because it has no access to the target app's internal state; Palmier Pro is the target app, and exposes its *own* internal semantic operations directly as MCP tools — a strictly richer, first-party control surface.
- **CodePilot v161 / CONFIRMED Library-vocab #22** (Tauri-Desktop Management-GUI for a Coding Agent) — contrast, not kin: that family's GUI's *subject* IS the coding agent (it manages/switches/monitors agent sessions); Palmier Pro's GUI's subject is video, and the agent is a feature of the product, not the product's reason to exist.
- **CONFIRMED Library-vocab #23** (Pre-Indexed Read-Only Code Knowledge-Graph via MCP, N=4: graphify/GitNexus/codegraph/codebase-memory-mcp) and **google_workspace_mcp v140** — both are MCP servers whose entire purpose is to serve agents; Palmier Pro's MCP server is a bolt-on to an otherwise-complete consumer product. This is the load-bearing distinction for the pattern mint below.
- **devspace v171** (manufactures a coding agent from a hosted chat host) — opposite vector again: devspace takes a host with *no* local presence and grants it one; Palmier Pro is already a complete local presence that *chooses* to expose itself.
- Agent-skills progressive disclosure (`.agents/skills` folder convention) → agent-skills-standard v76 / agent-skills v184 cross-ref.
- fish-speech v20 (media-model component) and the generative-media provider list (Seedance/Kling/Veo/Suno/Nano-Banana-Pro) → the multi-provider generative-AI abstraction theme also seen in OpenMontage v188's 7-dimension provider selector.

---

## Pattern outcome

**1 NEW §C standalone at N=1 (CORPUS-FIRST for this conjunction):**

**"Product-First Native Application Retrofitted with a First-Party MCP Server"** — an independently complete, commercially viable, human-usable GUI application in a non-coding domain, whose maker *also* ships that same application's own MCP server exposing the app's real internal/semantic operations as tools (not a screen/gesture-emulation bridge, not a third-party wrapper of someone else's API) — so an external coding agent becomes an **optional peripheral co-worker inside a product a human can use completely independently**, rather than the product being a tool built *for* agents in the first place.

**Why this clears the "generalize-to-fit" bar** (the ai-berkshire v187 / DeepSpec v186 test this vault applies before minting): the defining fact is not "video editor" (a domain) or "has an MCP server" (a capability) taken separately — both already have corpus precedent independently. It's that **every prior corpus MCP-server subject was built to BE an agent tool** (the MCP surface *is* the product: the code-graph family, `google_workspace_mcp`, `devspace`, `cortex-hub`, `agentmemory`). Palmier Pro is the first subject where the MCP server is a **secondary access path bolted onto an otherwise-complete, independently sellable product** — the same move now spreading across Figma/Notion/Linear/Blender-class SaaS and desktop tools. That's a different relationship between agent and artifact, not just a new vertical for an old capability.

**DISTINCT from:**
- OpenMontage v188 §C (agent IS the runtime — no separate app to retrofit)
- serve-sim v183 §C (perception + gesture-emulation over an app whose internals it does *not* own)
- CodePilot v161 / CONFIRMED #22 (GUI *about* managing a coding agent, not a domain product with agent-nativity as a feature)
- CONFIRMED #23 code-knowledge-graph family + google_workspace_mcp v140 + devspace v171 + cortex-hub v181 (all agent-tool-first MCP servers)

**⚠️ NO-MINT alternative recorded operator/audit-reviewable** (the ai-berkshire v187 / DeepSpec v186 precedent for a genuine judgment call): *"Palmier Pro is simply the video-editing vertical of the already-well-represented MCP-server-for-coding-agents family (CONFIRMED #23 + the devspace/cortex-hub/google_workspace_mcp cluster); domain-crossing alone doesn't warrant a new standalone."* Either reading leaves **counts UNCHANGED at 46/11**; this note exists so a future audit can revisit the call with fresh eyes, exactly as done for ai-berkshire and DeepSpec.

**SECONDARY (NOT minted, tracked at their own layers):**
- **#19 19a** — first `Palmier, Inc.` author (disclosed, funded, YC-backed institution class).
- **Open-core license-split cross-reference** — GPLv3 product/MCP/chat + closed-source generative-AI cloud backend, a clean and honestly-disclosed variant of the open-core pattern already seen in PilotDeck v175 / OpenMontage v188 (both AGPL-3.0); worth noting Palmier Pro chose the weaker copyleft (GPLv3, not AGPL) despite having no SaaS-hosting exposure to defend against.
- **Multi-provider generative-AI abstraction** cross-ref → OpenMontage v188's 7-dimension provider selector; Palmier Pro's `ModelCatalog`/`GenerationService` is the same idea at native-app scale.
- **`.agents/skills` progressive-disclosure convention** → agent-skills-standard v76 / agent-skills v184.
- **#66 supply-chain note** — benign install (signed/notarized DMG, no `curl|bash`, no postinstall), but flag the undocumented Sentry telemetry consent gap and the absence of a published DMG checksum/signature for anyone pinning a specific build.

**NON-claims:** NOT a new top-level pattern (max #85 holds) · NOT #52 (stars/forks page-stated only, §37.4 — velocity unestablishable, and no figure is asserted as a claim) · NOT #57 (the repo mentions Claude/Codex/Cursor as integration targets it serves, and Google/SigLIP2 as an upstream dependency it credits in `models/README.md` — genuine attribution, but not a corpus-subject influence-citation, since none of Seedance/Kling/Veo/Suno/Clerk/Convex/Sentry/Sparkle are corpus subjects) · NOT #18 B1-MCP in the strict sense used elsewhere (it is a real MCP server with multiple clients, so the *distribution-structure* observation applies as a data-point, but the standalone above is about the *product-first* relationship, not the one-server-many-clients shape) · NOT a Domain-Vertical-Skill-Collection instance (no skills bundle beyond the thin `.agents/skills` convenience folder; this is an application, not a skill pack) · NOT corpus-first for AI video production generally (OpenMontage v188 precedes; this is scoped to the "product-first app retrofitted with agent-nativity" conjunction specifically).

---

## Tier

**Audit-reviewable — no existing tier is a clean fit.** Closest neighbors: **T2 Service** (self-hosted backend/MCP server — doesn't fit, since Palmier Pro is a full paid consumer GUI product, not a backend) and **T5 Agent-as-application** (an autonomous agent product — doesn't fit either, since the human-usable editor is the primary product and the agent is optional). Provisional label, matching the GLM-5 v176 "model/inference substrate" provisional-tier precedent: **"Native creative/production application with an embedded agent-capability layer."**

## Streak & counts

Counts: confirmed top-level patterns **46 UNCHANGED**; CONFIRMED Library-vocab **11 UNCHANGED**; §C live standalones **34 → 35**; tracked PROVISIONAL surface **≈41 → ≈42**. Streak: **GA:53 · OG:11 [7 ov]** (⚠️ under the v176/v186/v191 OFF-GOAL reading → GA:50·OG:14). §35 rolling-3-ship window {v190 GA, v191 GA, **v192 GA**} = 0 OG → **CLEAR**. **38 consecutive goal-aligned ships v153→v192** (GA reading). *(Renumbered v191→v192 2026-07-03: a concurrent session independently shipped `microsoft/AI-For-Beginners` as v191 off the same v190 tip — this ship is re-based on top of that branch and renumbered per operator direction; see the Verification note below.)*

## Verification note

Verdict produced **inline + hand-verified** per `feedback_wiki_verify_independently_check_collisions`: a 6-agent read-only research fan-out did source-reading (a real clone at commit `9a3ae502…`) + upstream/author/landscape research ONLY; all corpus-collision claims verified by hand (grep across `_state/` + `_patterns/` for "palmier" and for the broader "video editor / native macOS app / GUI-exposes-MCP" surface — clean, no prior subject); the CONFIRMED #23 code-graph family and the CodePilot v161/#22 management-GUI family were read directly from `_patterns/06` to establish the DISTINCT-from boundary above; one research agent's claim that "macOS 26 (Tahoe)" was a "future/unreleased OS, inconsistent with the current date" was **checked and dismissed as its own confusion** — macOS 26 Tahoe is Apple's real current version-naming scheme (renamed to match the calendar year starting with iOS/macOS 26 in 2025), not an anomaly in the source.

inflation_check: discipline HELD — 1 mint (≤2 cap honored), NO-MINT alternative explicitly recorded, max top-level pattern stays #85, counts 46/11 unchanged, no double-count against the code-graph or Domain-Vertical-Skill-Collection families.
