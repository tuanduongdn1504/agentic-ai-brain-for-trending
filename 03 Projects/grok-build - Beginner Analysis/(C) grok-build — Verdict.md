# (C) grok-build — Verdict

> LLM Wiki **v215** · `xai-org/grok-build` · 2026-07-18 · routine v2.7
> Verdict **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` (no workflow/subagent — shim-overflow self-throttle).

---

## GOAL-ALIGNED INCLUDE 3/4 — [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG]

### (a) FAIL — not Anthropic
Author = **SpaceXAI** (formerly **xAI**, org `xai-org`), Elon Musk's AI company (a SpaceX subsidiary after the 2026-02-02 all-stock merger). Not Anthropic; §41 gives no name/heritage/notability rescue. **First `xai-org`/SpaceXAI author → #19 19a** (the corpus's first Elon-Musk-company subject). A declared-non-Anthropic-institution — the **GLM-5 v176 (Zhipu) / Kilo Code v177 (Kilo AI) / NVIDIA v169 / ByteDance v143** situation.

### (b) STRONG — keys the tier (cleanly GOAL-ALIGNED, no §40 needed)
grok-build **IS an autonomous AI coding agent for software development** — the exact domain of **Goal #1** ("Master Claude and autonomous agents for software development"). It is the corpus's **first fully-open frontier-lab coding CLI/harness** — 844K lines of Apache-2.0 Rust of *how a frontier lab builds a Claude-Code-class terminal agent* — a premier Goal-#1 **learning artifact**. It implements the exact agent primitives the vault studies (skills, subagents, hooks, plan mode, MCP) and lands directly on the operator's **multi-agent-orchestration** + **git-worktree-parallel-sessions** pilot threads (8 worktree-isolated subagents + orchestrator reconciliation).
**STRONG-not-STRONGEST:** a **competitor/peer harness** (Grok's Claude Code, not Claude) · **vendor-Grok-locked** (doesn't run Claude; requires a paid SuperGrok/X-Premium-Plus subscription to run) · a **source-available one-way mirror** (no PRs) · **thin direct hireui payoff** (a dev tool, not a product feature). This is the **Kilo Code v177 (b) STRONG calibration** exactly — an on-domain competitor coding agent, studiable and (for subscribers) usable.

### (c) STRONG
Rust 99.6% · a mature **multi-crate workspace** (≈844K LOC, Simon-stated) · the full agentic feature set (TUI + **8-worktree parallel subagents** + Plan Mode + MCP host + skills/agents/hooks/plugins + sandboxing + ACP + headless/CI + marketplace) · **Apache-2.0 full source** · Grok-4.5-powered · backed by SpaceXAI. **Caveats (foregrounded):** 0 releases / early beta (just open-sourced) · source-**available** one-way mirror (contributions not accepted) · vendor-locked + paid to run · **NOT source-cloned** (page/README/Simon/docs-verified) · a real **privacy incident** (working-dir uploads to Google Cloud, now disabled + retention off by default) · stars page-stated §37.4.

### (d) STRONG
Kilo Code v177 (direct §C sibling/contrast) · larksuite/cli v143 §C + CodePilot v161 §C (near-neighbors, distinct) · DeepSeek-TUI v72 (Rust chat-TUI contrast) · GLM-5 v176 / DeepSpec v186 (competitor frontier-lab subjects; Grok 4.5 = the model analogue, grok-build = the harness) · OpenHands v30 / AutoGPT · the multi-agent-orchestration + devspace v171 + loop-engineering v189 threads · the agent-skills substrate + MCP host · CLIProxyAPI v207 (reverse-engineers Grok Build OAuth; corpus-recursive, NOT #57) · cc-switch v73 / ai-switcher v153 · claude-code-system-prompts v65.

---

## Pattern outcome — 1 NEW §C standalone at N=1 (CORPUS-FIRST, NOT world-first)

**"Open-Sourced First-Party Frontier-Lab Agentic Coding CLI/TUI (the Claude Code / Codex CLI / Gemini CLI vendor peer class)"** — anchor `xai-org/grok-build` (N=1).

**Why a mint, not an N=2 or a NO-MINT (hand-verified against the §C registry):**
- **NOT an N=2 of Kilo Code v177** — that standalone is scoped *"IDE-embedded, multi-model, third-party (Cline/Roo/Cursor peer class),"* and its own N=2 criterion requires *"a 2nd open-source IDE-embedded interactive **multi-model** coding-agent."* grok-build is **terminal-TUI, single-model (Grok-locked), first-party vendor** → fails both scope conditions. It is the **sibling** class (vendor terminal CLI), not the same class.
- **NOT an N=2 of Agent-Native Vendor CLI v143** (`larksuite/cli`) — that is *a product CLI an external agent DRIVES* (agent → the CLI). grok-build **IS the agent**. Opposite direction.
- **NOT CodePilot v161** (a GUI wrapping a CLI agent) · **NOT the orchestration-platform / MCP-bridge / model tiers.**
- The surface *"a frontier lab's own, first-party, fully-open agentic coding CLI as a studiable primary subject"* is **corpus-unrepresented** (grep = 0 hits). Mint at N=1 per the **Kilo Code v177 precedent** — credit the recurring-but-corpus-unrepresented world-class category. Kilo Code v177 minted the **third-party IDE-extension** coding-agent class; grok-build mints the **first-party vendor terminal-CLI** class. Consistent, not inflationary.
- **Scope honestly bounded: CORPUS-FIRST, NOT world-first** — Claude Code (closed), Codex CLI (OpenAI, open), Gemini CLI (Google, open), Qwen Code all precede as vendor coding CLIs; grok-build is the corpus's first such SUBJECT (and open-sourced).

**⚠️ NO-MINT alternative recorded (operator/audit-reviewable):** generalize the Kilo Code v177 standalone to *"Open-Source Interactive AI Coding-Agent Product"* and record grok-build as its **N=2** (the vendor-terminal-CLI variant). Leaned **MINT** because Kilo Code's standalone is explicitly scoped to exclude exactly what grok-build is, and the first-party-vendor + single-model + terminal-first axes are a genuinely distinct sub-class. **Either way counts UNCHANGED 46/11.**

**⚠️ Flag for the ~v221 audit:** a "coding-agent products" meta-cluster may be forming — Kilo Code v177 (IDE-extension) + grok-build v215 (vendor-terminal-CLI) + CodePilot v161 (GUI-wrapper). Recorded, **not acted on** (an audit call). PROMOTION-ELIGIBLE at a genuinely-independent N=2 (a 2nd first-party frontier-lab open-source coding CLI analyzed as a primary subject — e.g. a hypothetical open Codex CLI / Gemini CLI / Qwen Code deep-dive).

### SECONDARY (NOT minted)
- **#19 19a** — first `xai-org`/SpaceXAI author (institutional data-point; first Elon-Musk-company subject).
- **multi-agent-orchestration** — 8 worktree-isolated parallel subagents + orchestrator reconciliation = a source-verifiable reference for the operator's pilot thread (composes with devspace v171 + loop-engineering v189). NO mint (a feature; the pattern is tracked).
- **Agent-primitive convergence** — SpaceXAI adopted the Anthropic-pioneered primitive stack (skills/subagents/hooks/plan-mode/MCP). Recorded as a **DEFERRED watch axis / cross-ref** ("the Claude Code design vocabulary is now the cross-vendor standard"), NOT minted (a convergence observation, not a capability class; NOT #57 — conventions, not corpus subjects).
- **#84 84c** — hosts skills/agents/hooks/MCP + a marketplace (consumer-side host; NO N-bump; not the ponytail-generator mechanism).
- **MCP host** cross-ref (consumes MCP servers; NOT a #18 B1-MCP subject).
- **corpus-recursive cross-ref** — grok-build was a CLIProxyAPI v207 landscape mention, now a subject (NOT #57).
- **#66** — `curl|bash`/`irm|iex` prebuilt-binary install from x.ai + the working-dir-upload privacy history (now disabled/retention-off) + source-available mirror + vendor-locked/paid + built-in sandboxing (mitigation). Evaluate-a-competitor-tool; don't point it at hireui/candidate data.
- **model/harness distinction** — grok-build = the **harness** (T5 Agent-as-application); Grok 4.5 = the model (the GLM-5 v176 model-substrate tier; not open-sourced here).
- **Rust-TUI cluster** — DeepSeek-TUI v72 / fff v194 / meetily v196 neighbors.

### NON-claims
NOT #52 (16.6k★/0 releases/just-open-sourced page-stated §37.4 → velocity unestablishable) · NOT #57 (adapts tools from Codex + implements ACP/MCP/agent-skills conventions — none corpus subjects; the v207 tie is the other direction; lineage/mentions ≠ recursion) · NOT #18 B1-MCP (an MCP host, not a server) · NOT an N=2 of Kilo Code v177 / larksuite v143 · NOT the model tier (Grok 4.5 is the model) · NOT a new top-level pattern (max #85) · NOT world-first · NOT source-cloned (flagged).

---

## Bookkeeping
- **Tier:** **T5 Agent-as-application** — interactive coding-agent harness, **vendor-terminal-CLI/TUI flavor** (the Kilo Code v177 / OpenHands v30 tier; distinct from Kilo Code's interactive-IDE flavor).
- **Counts UNCHANGED 46/11.** §C live standalones **43 → 44**. Tracked PROVISIONAL surface **≈50 → ≈51**.
- **Streak GA:74 → GA:75** (61 consecutive goal-aligned ships v153→v215). **§35 CLEAR** — window {v213 GA, v214 GA, **v215 GA**} = 0 OG.
- **inflation_check HELD:** 1 mint ≤2; N=1 corpus-first-for-surface NOT world-first, with the NO-MINT alternative recorded + the two near-neighbor distinctions hand-verified against the registry; counts 46/11 unchanged; max #85; no double-count; no N-bumps.

## PILOT (one line)
On-goal (Goal #1) as a premier learning artifact — but the payoff is **READ the open source + BORROW the worktree-parallel orchestration**, not run it (paid + Grok-locked + a privacy history). ⭐ **A1 → B (borrow orchestration) → optional C (trial on a scratch repo, subscribers only).** Fence: install-snapshot + verify the Google-Cloud-upload path is disabled + retention off + scratch repo only + Apache-2.0 source safe to READ + **do NOT run against hireui** (CONSTITUTION + candidate PII) + pin the commit. **See the 24-method menu.**
