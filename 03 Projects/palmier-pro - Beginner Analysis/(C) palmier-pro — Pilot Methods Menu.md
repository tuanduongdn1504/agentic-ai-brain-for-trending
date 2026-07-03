# (C) palmier-pro — Pilot Methods Menu

24 ways to apply this ship, cheapest/lowest-risk first within each group. **One-thing path:** B1 (spec a hireui MCP server using Palmier Pro's `ToolExecutor` as the template) → D2 (prototype the single smallest read-only tool on an `agent-*` branch) = a genuine, small, first Goal-#2 artifact that doesn't require installing anything.

---

## A — Read & learn (zero risk, no install)

**A1.** Read `ToolExecutor.swift` + `ToolDefinitions.swift` (conceptually, from the Deep Dive's summary — or clone the pinned commit yourself) as a case study in designing a clean MCP tool surface: one dispatcher enum, 51 well-scoped tools, JSON-in/JSON-out, argument validation as the single most-tested layer. This is the direct architectural template for method B1/D1 below.

**A2.** Read the `AGENTS.md` + `CLAUDE.md` pairing as a worked example of the two-file agent-routing convention already tracked in this vault's **#12 LLM-routing-artifacts** family.

**A3.** Read `FAQ.md`'s one-line open-core disclosure ("the only thing closed source is the generative AI processing") as a model sentence for any future disclosure the vault or hireui needs to write about what's open vs. proprietary.

**A4.** Read the async-generation pattern (submit → placeholder clip → poll → auto-import, no webhooks) as a generic reference architecture for "a long-running generative job inside a stateful UI" — reusable well beyond video.

**A5.** Read the `Package.swift` dependency list (Clerk for auth, Convex for backend, Sentry for telemetry, Sparkle for auto-update) as a fast "which SaaS building blocks does a lean, funded 2-person team reach for" reference.

## B — Borrow the patterns into hireui / the vault's own work (highest ROI, no install of palmier-pro itself)

**B1. ★ Recommended first step.** Spec (don't build yet) a hireui MCP server using the `ToolExecutor` dispatcher as the direct structural template — map hireui's own domain objects (candidates, job postings, interview notes, pipeline stages) onto ~10–15 well-scoped tools (`get_candidate`, `list_open_roles`, `add_interview_note`, `move_pipeline_stage`, `export_candidate_report`, …). This is *the* concrete architectural answer to "how would hireui become agent-native," source-verified from a real production codebase rather than invented from scratch.

**B2.** Borrow the cost-estimation-before-generation pattern (`ModelCatalog` pre-calculates cost per model/resolution/duration before the user commits) into any hireui feature that calls a metered LLM/API — an anti-runaway-cost UI habit that composes directly with the vault's `hireui/_bmad-output/runbooks/claude-api-cost-optimization-spec-2026-06-15.md`.

**B3.** Borrow the `.agents/skills`-reading in-app-agent-chat idea for any future hireui embedded-assistant feature: an app that reads its own skills folder to shape what its in-app chat can do, distinct from (and complementary to) external MCP access.

**B4.** Borrow the "test the tool layer hardest" discipline (1,885 lines just for `ToolExecutorTests.swift`, more than any other subsystem) into the vault's own skill/MCP work: whichever surface an agent actually touches gets the most tests, ahead of internal logic.

**B5.** Use Palmier Pro's exact MCP-config JSON (`claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp`) as a working template for documenting "how to wire an HTTP-transport MCP server into Claude Code/Codex/Cursor" for any future in-house server the vault or hireui ships.

**B6.** Borrow the open-core license sentence pattern (B2/A3 above) plus the *choice* of GPLv3-not-AGPL for a desktop app with no SaaS-hosting exposure — a useful licensing-decision data point if the vault or hireui ever needs to pick a license for something distributed as a binary rather than hosted.

## C — Low-risk hands-on trial of palmier-pro itself

**C1.** Run `install-snapshot` (the vault's own skill) before installing anything, then download the signed DMG from the GitHub releases page and try the **free editor only** — no login, no subscription — on a scratch clip. Verifies the core product claim at zero spend.

**C2.** Connect the vault's own Claude Code to the local MCP server (`claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp`) on a scratch project and ask it to call `get_timeline` — a free, read-only smoke test of the whole MCP surface, the SkillSpector-v169-class safest way to touch a new tool.

**C3.** Still on the free tier, ask Claude Code (via the MCP connection) to trim or reorder a couple of clips on a throwaway timeline and read the resulting tool-call transcript — a live, concrete case study of "what does an agent-driven native-app editing session actually look like," directly comparable to the `claude-tap` v173 / loop-engineering v189 habit of watching what the agent actually does rather than assuming.

**C4.** If curious about the paid generative layer, cap spend explicitly to the smallest possible single generation on the Pro tier rather than open-ended experimentation — the same spend-discipline already applied to the Strix v190 and OpenMontage v188 pilots.

## D — hireui-specific application (the real Goal-#2 payoff)

**D1.** Turn B1's spec into a written one-pager on an `agent-*` branch (per hireui's I-2 policy) — domain objects → tool list → auth model (hireui already has its own; no need for Clerk) → what stays read-only vs. read-write.

**D2. ★ Recommended second step.** Prototype the single smallest slice: one read-only MCP tool (e.g. `get_candidate_summary`) wired to hireui's existing internal API, tested the way Palmier Pro tests its tool layer — one dedicated test file, argument-validation-first. Small, safe, and a genuine completed Goal-#2 artifact.

**D3.** Adopt the "agent as an optional peripheral, not the whole product" framing explicitly in any hireui product conversation about adding AI features — a vocabulary borrowed straight from this ship's pattern mint, useful for scoping discussions with stakeholders who worry "are we becoming an AI company" when the honest answer is "we're adding one optional access path."

**D4.** Once D2 exists, extend it to a second read-only tool, then (only after both are proven and reviewed) a single guarded write tool with an explicit confirmation step — mirroring Palmier Pro's own read-tools-first, write-tools-tested-heaviest posture.

## E — Off-goal / personal, named honestly

**E1.** If you ever need to cut a real video (a hireui product-demo clip, a personal project), Palmier Pro is a legitimate free option — the GUI-editor-plus-agent-copilot angle, distinct from the OpenMontage v188 pilot's headless-pipeline angle to the same underlying need.

**E2.** Try the in-app agent chat (routes straight to the Anthropic API) as hands-on UX research into "what a first-party in-app Claude integration inside someone else's native app feels like" — useful reference if the vault ever advises on a similar embedded-chat feature.

## F — Vault-meta / pattern-library follow-ups

**F1.** At the next audit, revisit the recorded NO-MINT alternative for this ship's §C standalone with fresh eyes rather than self-resolving it now — matching the discipline applied to ai-berkshire v187 and DeepSpec v186.

**F2.** Watch for a second instance of "product-first app retrofitted with a first-party MCP server" — Figma/Notion/Linear/Blender-adjacent tools are all shipping MCP servers as bolt-ons in 2026; a clean 2nd cross-author instance would be PROMOTION-ELIGIBLE at N=2 and would confirm this as a real, recurring industry pattern rather than a one-off.

**F3.** If a future Palmier Pro release ships published benchmarks or documents its Sentry telemetry-consent flow, that resolves two of the flagged gaps in the Deep Dive — worth a quick re-check note, not a full re-ship.

---

**Fence (for methods C1–C4, D2, D4):** `install-snapshot` before the DMG · free tier only unless you deliberately choose to spend (Pro tier, one small generation, explicit cap) · scratch project/clip, never a real hireui asset, for C1–C3 · hireui work per its own CONSTITUTION (I-2 `agent-*` branch, I-8 operator-installs, GitNexus-first) for D1–D4 · no checksum is published for the DMG, so treat it like any unsigned-hash download — fine for a local scratch trial, don't wire it into any automated/CI pipeline without your own verification step.
