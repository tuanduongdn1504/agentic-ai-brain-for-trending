---
title: "(C) openinterpreter — Verdict"
subject: "openinterpreter/openinterpreter (the new Rust Open Interpreter — a Codex fork; harness-emulation coding agent for low-cost/open models)"
wiki: v223
date: 2026-07-22
verdict: "GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG keys the tier · (c) STRONG · (d) STRONG]; 1 NEW §C standalone at N=1 (CORPUS-FIRST for the harness-emulation surface, NOT world-first); counts 46/11 UNCHANGED"
---

# Verdict — openinterpreter/openinterpreter (v223)

**Operator-requested** ("build LLM wiki for `https://github.com/openinterpreter/openinterpreter`").

## Phase 0.9 STRICT — GOAL-ALIGNED INCLUDE 3/4

**[(a) FAIL · (b) STRONG keys the tier · (c) STRONG · (d) STRONG] — cleanly GA on (b) STRONG (no §40).**

### (a) Anthropic authorship — FAIL
Author = **Open Interpreter Inc. / Killian Lucas** (the `openinterpreter` GitHub org), **NOT Anthropic**. §41: no name / heritage / locale / notability rescue, and the disclosed-individual (a)-axis is answered NO. **#19 19a** first `openinterpreter`-org / Killian-Lucas author (the classic Python `open-interpreter` was **never** a corpus subject — collision-grep confirms only an ollama landscape mention).

### (b) Goal-relevance — STRONG (keys the tier; cleanly GA)
It **IS an autonomous coding agent for software development** (Goal #1 core) and it lands on **four live vault threads at once**:
- **harness-engineering** — the product's *organizing principle* (harness emulation) is a productized statement of the exact "the harness is the lever, not just the model" thesis the vault studies (TNT-Cursor-CLI-factory / Archon / Adaptive-engineering / loop-engineering v189 / grok-build v215); reading OI's `claude-code` vs `kimi-code` harness definitions is a rare, concrete "what makes Claude Code effective, by contrast" study.
- **claude-api-cost-optimization** — it is a **cost lever**: run a cheap/open model (Kimi K3 / DeepSeek / Qwen) under its *native* harness for routine agentic coding, reserving Claude for the hard parts (the cc-switch v73 / ai-switcher v153 workflow, but at the *harness* level).
- **coding-agent-products cluster** — a direct peer of grok-build v215 / Kilo Code v177 / DeepSeek-TUI v72 (both Rust, both Codex-derived).
- **agent primitives** — a Codex fork, so it embodies the Codex agent loop + native sandboxing + ACP the vault tracks.

**STRONG-not-STRONGEST:** third-party + a **Codex fork** (hard base is upstream) + **Claude is one harness among many, and the product is explicitly optimized for NON-Claude open/cheap models** + a competitor/peer harness (the grok-build v215 / Kilo Code v177 (b)-STRONG calibration). Cleanly GA — no §40 needed.

### (c) Substance — STRONG
An open-source (Apache-2.0) Rust coding agent by an established brand/company: a Codex fork + a genuinely-distinct harness-emulation layer + a Rust-native Kimi-Code harness reimplementation + native OS sandboxing + ACP embedding + Codex-SDK compatibility + 62 releases + ~67.1k★. **Caveats foregrounded:** NOT source-cloned (README/page/landscape only — the v200→v222 self-throttle); a Codex fork (upstream base does the heavy lifting); v0.0.x young despite the release count; star count page-stated + likely brand-carried (§37.4 → NOT #52); harness-emulation performance claims are the project's own.

### (d) Cross-refs — STRONG
**grok-build v215 §C** (direct sibling — Rust, Codex-derived coding CLI) · **Kilo Code v177 §C** + **larksuite/cli v143 §C** + **CodePilot v161 §C** (the coding-agent-products cluster) · **DeepSeek-TUI v72** (a *named emulated harness* → corpus-recursive) · **GLM-5 v176** (the `zcode`/Z.AI harness target) · **Kimi K3** (topic #65; the flagship target model) · **cc-switch v73 / ai-switcher v153 / CLIProxyAPI v207 / OmniRoute v208** (the LLM-access + cost thread) · **OpenHands v30 / AutoGPT** (the agent-as-application lineage) · **ACP** (free-claude-code v60 / agent-of-empires v162 / grok-build v215) · **OpenAI Codex** (the base; landscape) · the classic Python `open-interpreter` (contrast — a different repo the corpus never wiki'd).

## Pattern outcome — 1 NEW §C standalone at N=1 (leaning MINT); NO-MINT alternative recorded

### PRIMARY (minted): §C standalone N=1 — "Harness-Emulation Coding Agent"
**"Harness-Emulation Coding Agent — one binary that emulates a target model's *native* agent harness (swappable `claude-code` / `kimi-code` / `qwen-code` / `deepseek-tui` / `zcode` / `swe-agent` / …) to maximize agentic performance from low-cost / open-weight models."**

**Why MINT, and why N=1:** the harness-emulation *organizing principle* is a genuinely-distinct, **corpus-unrepresented capability** — no existing §C standalone covers "emulate the model's native harness, swappably, in one product." Hand-checked distinct from:
- **grok-build v215 §C** "first-party frontier-lab CLI" — OI is a *third-party indie-company Codex fork*, not a frontier lab (OI fails grok-build's criterion exactly as grok-build failed Kilo Code's).
- **Kilo Code v177 §C** "IDE-embedded multi-model" — OI is *terminal*, and its multi-model angle is harness-emulation (match the harness to the model), not Kilo's 500-provider routing.
- **larksuite/cli v143 §C** "agent-native vendor CLI an agent drives" — OI *is* the agent (opposite direction).
- **CodePilot v161 §C** "desktop GUI wrapping a CLI agent" — OI is the CLI agent.
- **DeepSeek-TUI v72** "single-model TUI" — OI is multi-harness (and *emulates* the DeepSeek-TUI harness).
- cc-switch v73 / ai-switcher v153 (switch provider/account/config, not the *harness*); CLIProxyAPI v207 / OmniRoute v208 (re-expose subscriptions as APIs, gateway not harness).

Mint at **N=1** per the grok-build v215 / fff v194 / serve-sim v183 / llm-space v221 precedent (mint N=1 for a genuinely-distinct corpus-first *capability* surface). **Scope: corpus-first for the surface, NOT asserted world-first** (harness-engineering is a recognized 2026 field — a `harness-engineering` GitHub topic, `awesome-cli-coding-agents`; OI's productized *swappable multi-harness emulation* is plausibly novel but scoped conservatively, the grok-build/lobehub discipline). Counts **46/11 UNCHANGED**; **§C live standalones 45 → 46**; **§C surface ≈52 → ≈53**.

### ⚠️ NO-MINT reviewable ALTERNATIVE (recorded operator/audit-reviewable)
"OI is simply the 4th member of the coding-agent-products meta-cluster (Kilo Code v177 / grok-build v215 / larksuite v143 / CodePilot v161) — a Codex-fork variant; harness-emulation is a distinctive *feature* (a `/harness` command) of a Codex fork, not a new *primitive* → NO MINT, instance-strengthening of the cluster." **Leaned MINT** on the genuinely-distinct-and-corpus-unrepresented-capability logic (grok-build precedent), but this reading is defensible and RECORDED.

### ⚠️ AUDIT FLAG (load-bearing): the coding-agent-products meta-cluster is now 4+ standalones and the ~v221 audit is OVERDUE
grok-build v215 flagged "a 'coding-agent products' meta-cluster may be forming (Kilo Code v177 IDE-extension + grok-build v215 vendor-terminal-CLI + CodePilot v161 GUI-wrapper — cluster or keep standalones?)" and deferred it to the **~v221 audit**. That audit has **not run** (last audit v212, window v203–v212; v213–v223 all shipped since → the ~v221 audit is **overdue**). OI adds a **4th** distinct-capability standalone to this space (now: Kilo Code v177 / grok-build v215 / larksuite v143 / CodePilot v161 / **OI v223** + DeepSeek-TUI v72 the single-model TUI). The audit must decide: **cluster these into one Library-vocab "coding-agent products" item, or keep N distinct standalones?** OI's harness-emulation standalone is minted provisionally and flagged prominently into that decision.

### SECONDARY (NOT minted)
- **#19 19a** first `openinterpreter`-org / Killian-Lucas author.
- **corpus-recursive — emulates DeepSeek-TUI v72's harness** (`/harness deepseek-tui`): a genuine derive-from a corpus subject (stronger than a mention), **leaning #57** but ⚠️ **NOT source-verified** that OI's `deepseek-tui` harness is specifically Hmbown's v72 codebase vs the generic DeepSeek-TUI harness concept → recorded as a notable corpus-recursive cross-ref, hand-caveated (the `feedback_wiki_verify_independently_check_collisions` discipline). **GLM-5 v176** via `zcode`/Z.AI = a target-model cross-ref.
- **#84 84c** provider-agnostic-by-design (multi-model via swappable harnesses; **NO N-bump**; the harness-emulation mechanism is distinct from cc-switch's config-switch + the ponytail v168 native-rule-file generator).
- **ACP** cross-ref (`interpreter acp`): a Pattern #18 sub-mechanism-B protocol-variant candidate (free-claude-code v60 / AoE v162 / grok-build v215); **NOT corpus-first, NOT a §C standalone, NOT a #18 B1-MCP subject** (ACP ≠ MCP).
- **Codex fork / Codex-SDK compatible** — landscape note (Codex not a corpus subject; also grok-build v215's base; NOT #57).
- **claude-api-cost-optimization thread** — OI is the "run cheap models well" pole (contrast the CLIProxyAPI v207 / OmniRoute v208 "re-expose subscriptions" gray-zone pole; OI uses your own keys / open weights, no ToS issue).
- **#66 supply-chain / runtime** — `curl | sh` / `irm | iex` install (attack-surface note; install-snapshot fence) + a coding agent that **runs code on your machine** (the classic OI risk), **mitigated by native OS sandboxing** (a security-forward feature); Apache-2.0.

### NON-claims
NOT the classic Python `open-interpreter` (a different repo + the `endolith/open-interpreter` community fork; the corpus never wiki'd either) · NOT #52 (~67.1k★ page-stated §37.4 + likely brand-carried → velocity unestablishable) · NOT #57 (the DeepSeek-TUI-v72 harness-emulation link is a hand-caveated corpus-recursive cross-ref, not an asserted lineage; Codex/OpenAI base ≠ recursion) · NOT #18 B1-MCP (ships no MCP server; ACP ≠ MCP) · NOT world-first (harness-engineering is an active field) · NOT a frontier-lab product (grok-build v215 is; OI is an indie-company Codex fork) · NOT a new top-level pattern (max #85) · NOT source-cloned (flagged).

## Tier
**T5 Agent-as-application** (interactive coding-agent harness, terminal-TUI flavor — the grok-build v215 / Kilo Code v177 / OpenHands v30 tier).

## Streak & §35
- v222 lobehub = GA:80. **OI v223 = cleanly GA on (b) STRONG → `GA:81 · OG:13 [7 ov]`** (4 consecutive GA post the v219 OG break).
- **§35 CLEAR** — window {v221 GA, v222 GA, **v223 GA**} = 0 OG.

## inflation_check (HELD)
1 mint ≤ 2 cap; N=1 corpus-first-for-surface-NOT-world-first; NO-MINT alternative recorded + flagged to the overdue meta-cluster audit; top-level counts **46/11 UNCHANGED**; max top-level pattern #85; no double-count (the §C standalone = *capability*, the coding-agent-products cluster question = *classification*, ACP = a #18-B candidate, #84 84c = NO N-bump); no improper N-bumps.

## Verification note (`feedback_wiki_verify_independently_check_collisions`)
Verdict produced **INLINE + fully hand-verified** — **no workflow / no subagent** (the ~205K shim overflows every subagent >200K → deep-dive workflows fail prompt-too-long, the v200→v222 self-throttle). Source hand-fetched (rendered repo page + raw README); identity + the Python→Rust pivot + `endolith` community fork + the Codex-fork + harness-emulation thesis + the 2026 CLI-coding-agent landscape by **WebSearch**; collision by **sanity-anchored hand-grep** (open-interpreter = an ollama landscape mention only → collision-clean; anchors grok-build v215 / Kilo Code / DeepSeek-TUI v72 / AoE v162 all hit richly → grep works). The one flagged-unverified claim (the DeepSeek-TUI-v72 harness lineage) is explicitly hand-caveated, not asserted.

## PILOT (one-line)
On-goal (Goal #1): an install-able open-source coding agent to **read (the harness-emulation design) + borrow (the "match the harness to the model" cost lever), and optionally scratch-trial** with a cheap open model under native sandboxing — **not** a hireui component (hireui is Claude-Code / operator-installs / GitNexus-first per its CONSTITUTION). ⭐ **A1 → B7 → (optional) C11.** Full menu in `(C) openinterpreter — Pilot Methods Menu.md`.
