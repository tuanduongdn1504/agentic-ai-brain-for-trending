# (C) OfficeCLI — Verdict

> LLM Wiki **v206** · `iOfficeAI/OfficeCLI` · 2026-07-16 · routine v2.7.
> Deep dive → `(C) OfficeCLI — Deep Dive.md`. Pilots → `(C) OfficeCLI — Pilot Methods Menu.md`.

---

## Goal-alignment: GOAL-ALIGNED INCLUDE 3/4

| Axis | Call | Why |
|---|---|---|
| **(a)** author-is-Anthropic/cultural-peer | **FAIL** | iOfficeAI = an **anonymous, independent, non-Anthropic org** (no public members, no disclosed individuals; the DeusData v172 / Jo-Inc v179 bare-org situation). Per routine **§41**, (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source — neither applies; the Chinese-language `README_zh.md` is **not** an (a)-rescue (no name/heritage/locale inference). First `iOfficeAI` author → **#19 19a**. |
| **(b)** goal-relevance | **STRONG (keys the tier)** | Gives AI agents (**Claude Code first-class** — built-in MCP + auto-installed SKILL.md) a genuinely new, high-value **capability** (full Office-document create/read/modify **with render-and-verify**) = core agent-autonomy substrate (Goal #1) **AND** directly, sharply pilotable into **hireui** (recruitment SaaS: CV ingestion, offer-letter/report/deck generation) = a real Goal-#2 payoff. **STRONG-not-STRONGEST** = third-party + capability-augmentation + Claude one of several harnesses + an Office-document vertical (not the Claude/Anthropic substrate itself). Calibrates to Agent-Reach v174 / serve-sim v183 / fff v194 / page-agent v199 (all (b) STRONG capability layers). |
| **(c)** substance/maturity | **STRONG (with a foregrounded caveat)** | C# single-binary; HTML/PNG rendering engine; 350+-formula evaluator + pivot tables; three-layer Read→DOM→Raw-XML; resident mode; deterministic JSON; **three-channel agent delivery** (MCP + cross-harness SKILL.md + SDKs); 130 releases / v1.0.136 / ~18k★. **Caveats:** engineering internals are **page/doc/DeepWiki-stated, not source-cloned**; "world's first/best" is marketing (populated competitor space); star counts conflict (18.1k vs 8.4k, §37.4); anonymous org; install/auto-provision surface (#66). |
| **(d)** connectedness | **STRONG** | The agent-capability-layer §C cluster + the MCP family (#18 B1-MCP) + the agent-skills ecosystem (#84 84c) + markitdown v28 (direction contrast) + Anthropic's own docx/xlsx/pptx skills (conceptual peer) + the render-and-verify/maker-checker discipline + AionUi (the org's Cowork sibling). |

**§31:** the tier keys on **(b) STRONG** → **GOAL-ALIGNED INCLUDE.** No operator override needed; no §40 rescue needed; no OFF-GOAL reading in play.

---

## Pattern outcome: 1 NEW §C standalone at N=1

**"Agent-First Office-Document (Word/Excel/PowerPoint) Creation+Manipulation Capability Layer"** — a single self-contained binary + built-in MCP server + auto-installed cross-harness `SKILL.md` + SDKs that gives an AI agent **full create/read/modify control over `.docx`/`.xlsx`/`.pptx`** — with a **built-in HTML/PNG rendering engine so the agent can SEE and verify output**, a **formula/pivot evaluator**, and **deterministic JSON I/O** — **no Office install**.

- **CORPUS-FIRST for the Office-document surface** — collision grep clean; **markitdown v28** (`microsoft/markitdown`) is the closest corpus neighbor but is document→markdown **conversion for ingestion** (the opposite direction, read-only); the §C capability-layer cluster (Agent-Reach v174 web/social · serve-sim v183 mobile-simulator · camofox v179 stealth-browser · page-agent v199 in-page GUI · browser-use v41 browser-automation · fff v194 file-search) has **no Office-document surface**.
- **NOT world-first** — the Office-document-MCP space is populated (office-mcp, jenstangen1/pptx-xlsx-mcp, vAirpower/macos-office365-mcp, lingfan36/ai-office-mcp [358 tools], ForLegalAI, openpyxl-MCP, markitdown-mcp — mostly single-format Python wrappers). OfficeCLI's distinctive = single C# binary + rendering engine + formula/pivot eval + three-format unified surface + cross-harness bundle; "world's first" is a marketing tagline.
- **Mint at N=1** per the serve-sim v183 / fff v194 / page-agent v199 / openwiki v195 precedent (strong anchor: ~18k★, 130 releases, production C# suite, **no corpus peer on the surface**). **§28 ≤2-new-standalones cap honored (1 of ≤2).**
- ⚠️ **NO-MINT alternative recorded (operator/audit-reviewable)** — the camofox v179 / page-agent v199 / ai-berkshire v187 discipline: *"an Office-document vertical within the represented agent-capability-layer family; the Office surface is a new target, not a new capability MECHANISM → instance-strengthening of the capability-layer meta-shape, no fresh standalone."* **Leaned MINT** because the SURFACE (Office documents: create/modify/render/formula-eval) is genuinely distinct from every existing capability-layer surface (web/mobile/browser/file-search/in-page) — the same surface-boundary logic used for serve-sim v183 (web-vs-mobile) and page-agent v199. **Either reading counts UNCHANGED 46/11.**

**Tier: T2 Service** (self-hosted local CLI capability layer + MCP server for agents; the fff v194 / Agent-Reach v174 / camofox v179 / serve-sim v183 / codebase-memory-mcp v172 family).

---

## Secondary observations (NOT minted)

- **#18 B1-MCP instance-strengthening** — a built-in MCP server, one-server-many-clients (Claude Code / Cursor / VS Code / LM Studio) = a clean B1-MCP instance → **N≈12** (audit bookkeeping; the standalone = *capability/surface*, #18 B1 = *distribution structure* → different axes, **no double-count**, the v140/v171/v172 precedent).
- **#84 84c cross-harness** — auto-installs `SKILL.md` for Claude Code / Cursor / Windsurf / Copilot + Python/Node SDKs (**NO N-bump** per v86; **NOT** the ponytail-v168 14-platform generator mechanism — OfficeCLI distributes ONE skill + ONE MCP server that many harnesses consume).
- **#19 19a** — first `iOfficeAI` author; anonymous serial AI-agent-infra builder (AionUi ~30k★ Cowork app / OfficeCLI ~18k★ / Rust CLIs / AionHub).
- **#12 LLM-routing-artifacts INCIDENTAL** — auto-installs SKILL.md + MCP config **into** agent environments as a side-effect of capability exposure (**NO N-bump**).
- **#66 supply-chain / attack-surface cross-ref** — `curl|bash`/`irm|iex` installers + auto-provisioning SDKs (pip/npm fetch+run the native binary) + auto-writes a skill file + MCP config into detected agent configs, for a tool that reads/writes your documents. Apache-2.0 (auditable), no stated telemetry. **Fence: install-snapshot + inspect the installer + prefer a manual binary or a pinned package-manager install + scratch dir first + review what it writes into your agent configs + pin v1.0.136.**
- **Render-and-verify / maker-checker cross-ref** — `watch` live preview + `validate`/`view issues` = the vault's own loop-verifier / video-use v198 self-eval / ai-web-design redesign-gate discipline, applied to **document output** (the agent SEES the render, not blind XML). A borrowable pattern.
- **markitdown v28 DIRECTION contrast** — conversion (docs → markdown, ingestion) vs OfficeCLI's authoring (create/modify docs). Distinct, cross-ref.
- **Anthropic docx/xlsx/pptx skills cross-ref** — the closest conceptual peer (Office-doc manipulation for Claude, Anthropic-internal Python skills); OfficeCLI = the standalone, renderable, deterministic, cross-harness open-source alternative. Cross-ref, **NOT #57**.
- **AionUi cross-ref** — iOfficeAI's Cowork multi-CLI sibling → the operating-niche + Anthropic Cowork; a serial-builder identity data-point, **not a subject**.

---

## Non-claims

- **NOT #52** (~18.1k★ repo-page / ~8.4k★ SkillsLLM **conflicting**, 130 releases, v1.0.136 — all page-stated §37.4 → velocity unestablishable).
- **NOT world-first** (marketing tagline; populated MCP-server competitor space).
- **NOT corpus-first for document handling generally** (markitdown v28 preceded for the conversion direction; the claim is scoped to the **Office-document creation+manipulation** surface).
- **NOT #57** (no corpus subjects cited as influences; markitdown / Anthropic-skills are conceptual peers/contrasts, not credited influences; mentions ≠ recursion).
- **NOT a new top-level pattern** (max #85).
- **NOT a Domain-Vertical-Skill-Collection** (it's a capability layer/tool with format-specific sub-skills, not a skill collection).
- **NOT source-verified at the C# level** (engineering internals page/doc-stated — see the Deep Dive's honesty note).

---

## Counts & streak

- **Confirmed top-level patterns: 46 UNCHANGED · CONFIRMED Library-vocab: 11 UNCHANGED.**
- **§C live standalones: 40 → 41** (+1, N=1).
- **Tracked PROVISIONAL surface: ≈47 → ≈48** (7 clusters + 41 live standalones).
- **Streak: GA:65 → GA:66** — v206 cleanly goal-aligned on (b) STRONG. **52 consecutive goal-aligned ships v153 → v206.**
- **§35:** rolling-3-ship window {v204 GA, v205 GA, **v206 GA**} = 0 OG → **CLEAR** (v203 = audit, excluded).
- Lifetime operator overrides = 10; v153→v206 = **zero**.

---

## Verdict method

✅ Produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — **no workflow relied on.** The read-only deep-dive workflow has failed prompt-too-long on all agents at v200/v202/v204 (the ~205K shim snapshots into each subagent > 200K); **not run** per the self-throttle precedent (v205 was likewise hand-built). Source hand-fetched (repo page + raw README + DeepWiki + SKILL.md + org page); identity by WebSearch + org WebFetch; landscape by WebSearch; **collision by file-routed hand-grep** (the flaky-shell stdout-drop produced a false-empty on the first two attempts → defeated by routing to a file + a `markitdown` sanity check [6 hits] confirming the grep works, then OfficeCLI/iOfficeAI/AionUi = 0 hits = clean).

**Errors caught by hand:** the star-count conflict (18.1k vs 8.4k → page-stated range, **NOT #52**); the "world's first/best" tagline (→ scoped to **corpus-first-not-world-first**, populated competitor space); the DeepWiki "no pivot-table details" gap (README asserts native pivot tables → flagged page-stated); the first two false-empty collision greps (→ file-routed re-run).

`inflation_check` = discipline HELD: **1 mint ≤ the §28 2-cap**; N=1 corpus-first-for-surface-NOT-world-first with the competitor landscape credited; NO-MINT alternative recorded; **counts 46/11 unchanged**; max #85; no double-count (#18 B1 vs the §C standalone are different axes); no N-bumps on #84/#12.

---

## Ship

Branch `wiki/v206-officecli` off the v205 tip (`18a5043`, `wiki/v205-system-prompts-leaks`) — to preserve the unmerged **v204 → v205** chain, so the operator merges **v204 → v205 → v206** in order (main HEAD = `33505a3`, routine v2.7). **Not auto-merged** — operator reviews + merges.
