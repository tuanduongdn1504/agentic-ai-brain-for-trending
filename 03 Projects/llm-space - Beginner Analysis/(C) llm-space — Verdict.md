# (C) LLM Space — Verdict (v221)

**Subject:** `deer-flow/llm-space` — "LLM Space v4," a local-first native **desktop app for agent-builders** (author/version prompts·tools·model-settings → real-time trace of every model-call & tool-run in the agent loop → replay/step-through debug → eval across runs), built on **Pi Agent Core** (`earendil-works/pi`) + Electrobun + React/Bun.
**Author:** ByteDance's **DeerFlow team** (`deer-flow` org; sister to the official `bytedance/deer-flow`), **NOT Anthropic**.
**Facts:** MIT; TypeScript 97.1%; ~1.1k★/113 forks/**10 releases / v4.2.0** (Jul 17 2026) — page-stated §37.4; VolcEngine/BytePlus recommended default; telemetry opt-out-default-ON; **no MCP server**.

---

## Verdict: **GOAL-ALIGNED INCLUDE 3/4** · **1 NEW §C standalone at N=1** (CORPUS-FIRST for the surface, NOT world-first) · counts **46/11 UNCHANGED** · Tier **T2 Service**

| Axis | Call | Why |
|---|---|---|
| **(a)** | **FAIL** | ByteDance's DeerFlow team, not Anthropic. §41 — no name/heritage/locale/notability rescue; the ByteDance corporate-not-Anthropic situation (DeerFlow v9 / larksuite/cli v143). **#19 19a** returning-institution + first `deer-flow`-org-namespace subject. |
| **(b)** | **STRONG** — keys the tier | A tool for **building/tracing/debugging/evaluating AI agents** = dead-center on Goal #1 (agent development/engineering) + on the vault's live **prompt-eval / CC-observability-OTel / multi-agent-orchestration** threads + **directly pilotable** into the vault's own agent-building AND into hireui's "build the first LLM feature *right*" work (the candidate-LLM legibility ADR wants exactly author→trace→eval-gate). Claude is a first-class provider **via the Pi seam**. STRONG-not-STRONGEST = third-party + provider-agnostic (Claude one of several; **BytePlus/VolcEngine default → ByteDance-flavored**) + a workbench for *your custom Pi-based agents* (not Claude Code) + a developer-tooling vertical. Cleanly GA (no §40 needed). |
| **(c)** | **STRONG** | Real, iterated (**v4.2.0 / 10 releases**) native desktop app: build/version + real-time trace + replay/step-through + eval-across-runs + local-first files; TS/Bun monorepo; **dogfooded** by the DeerFlow team. ⚠️ Caveats: **NOT source-cloned** (README-stated); hard agent-loop is **upstream Pi**; ~1.1k★ modest → NOT #52; ByteDance/BytePlus default; telemetry opt-out-default-ON; **no MCP**; Claude only via the inherited Pi seam. |
| **(d)** | **STRONG** | **claude-tap v173** §C (closest §C neighbor — trace-viewer, distinct mechanism) · the **v158 observability sub-archetype** (contrast — coding-agent session monitors) · **pi-mono v36** (built on it = #57) · **DeerFlow v9** (same-team harness it debugs = cross-ref, NOT #57) · the LLM-ops landscape Langfuse/Phoenix/MLflow/Opik/Braintrust (world-first denial) · prompt-eval + CC-observability/OTel + mosh-ai vendor-seam threads · Electrobun form-factor · ByteDance cluster (larksuite/cli v143) · Kilo Code v177 / grok-build v215 (agent-product contrast). |

## Pattern outcome — **1 NEW §C standalone at N=1**

> **"Local-First Desktop Agent-Development Workbench** — author/version prompts·tools·model-settings → real-time trace of every model-call & tool-run in the agent loop → replay/step-through debug → eval across runs; for agent-**builders**." · **N=1** · **v221 llm-space**

- **CORPUS-FIRST for the surface** — hand-verified: no §C row covers the integrated agent-builder IDE (claude-tap v173 = MITM protocol-inspector of a *third-party* coding agent; the v158 observability sub-archetype = *coding-agent session monitors*; Kilo Code v177 = the coding agent itself; grok-build v215 = a coding agent; palmier-pro v192 / tabularis v212 = product-first + MCP-retrofit). prompt-evaluation exists only as a *topic* (not a shipped subject).
- **NOT world-first** — Langfuse (YC W23) / LangSmith / Phoenix-Arize / MLflow / Opik / Braintrust / Helicone / Laminar occupy the build+trace+eval LLM-ops-engineering space. The distinctive = **local-first native-DESKTOP form-factor (Electrobun) + built on Pi Agent Core + single-window agent-builder framing**.
- Mint at N=1 per the **fff v194 / serve-sim v183 / claude-tap v173 / grok-build v215** precedent (a genuinely distinct **on-goal** agent-capability surface, unrepresented in §C, minted at N=1 with honest world-first scoping) + the **Kilo-Code v177 "mint the corpus-first exemplar of a recurring world-class category"** precedent (the class recurs at world-class scale — Langfuse/LangSmith/Braintrust — and was corpus-unrepresented).

⚠️ **NO-MINT reviewable alternative** (operator/audit): read it as (a) a **desktop form-factor variant of the claude-tap v173 agent-trace-viewer surface**, or (b) an **"agent-development observability" broadening of the v158 observability sub-archetype** → instance-strengthening, no new standalone. **Leaned MINT** — LLM Space is materially distinct from claude-tap (it **authors + versions + evaluates**, not just MITM-traces) AND categorically outside the coding-agent-session-monitor sub-archetype (it's an IDE for building *your own* agents). Either reading → **counts 46/11 UNCHANGED**; §C live standalones **44 → 45**; §C surface **≈51 → ≈52**.

### Secondary (NOT minted)
- **#57 genuine** — llm-space builds on + **openly credits** `earendil-works/pi` = **Mario Zechner's pi-mono v36** (a DIFFERENT author) as its agent-framework backbone → a genuine cross-author corpus-recursive influence-citation (the page-agent v199 / OmniRoute v208 precedent; distinguish from cortex-hub v181's *silent* bundling and from the DeerFlow same-team self-reference).
- **corpus-recursive same-team cross-ref** — llm-space is the workbench the **DeerFlow v9** team built to debug DeerFlow (the browser-use v41 → video-use v198 same-org shape; **NOT #57**).
- **#19 19a** — ByteDance returning institution (DeerFlow v9 / larksuite/cli v143); first `deer-flow`-org-namespace subject; a dogfooding data-point.
- **#84 84c** — provider-agnostic **via the inherited Pi `pi-ai` seam** (OpenAI/Anthropic/Google); **NO N-bump** (inherited, not llm-space's own mechanism; not the ponytail v168 generator).
- **Electrobun form-factor** data-point — the corpus's first Electrobun (Bun-native-desktop) subject; distinct from the Tauri LV-C7 cluster (cc-switch v73 / tabularis v212) and from Electron.
- **#66** — install BENIGN (Bun/mise `bun install`; no curl|bash/postinstall evidenced; ⚠️ NOT source-cloned → `mise run setup` unverified → flagged); **telemetry opt-out-default-ON** (fence) + **BytePlus/VolcEngine default = ByteDance data-egress** if you use the recommended default provider (fence for sensitive/candidate data).

### NON-claims
NOT #52 (~1.1k★ page-stated §37.4) · NOT #18 B1-MCP (ships **no MCP server**) · NOT world-first · NOT a revisit of DeerFlow v9 (a different product by the same team) · NOT an instance of the v158 observability sub-archetype · NOT the claude-tap v173 protocol-inspector · NOT a new top-level pattern (max #85) · NOT source-cloned (flagged).

## Streak / state
- Counts **46/11 UNCHANGED**; §C live standalones **44 → 45**; §C surface **≈51 → ≈52**.
- Cleanly **GOAL-ALIGNED** → streak **GA:78 → `GA:79 · OG:13 [7 ov]`** (2 consecutive GA post the v219 OG break). **§35 CLEAR** (window {v219 OG, v220 GA, **v221 GA**} = 1 OG ≤ 1).
- **Tier T2 Service** (self-hosted local developer tool; native-desktop-app flavor — the claude-tap v173 / codebase-memory-mcp v172 / fff v194 family).

✅ Verdict produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — no workflow / no subagent; source hand-fetched (repo page + raw README); identity + landscape + Pi identity by WebSearch; **collision by hand-grep** (DeerFlow = corpus v9 [same-team cross-ref], Pi = corpus v36 [#57], no prior llm-space/agent-dev-workbench subject, §C rows read).
