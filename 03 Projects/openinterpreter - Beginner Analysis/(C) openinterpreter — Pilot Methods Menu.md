---
title: "(C) openinterpreter — Pilot Methods Menu"
subject: "openinterpreter/openinterpreter (the new Rust Open Interpreter — Codex fork; harness-emulation coding agent for low-cost/open models)"
wiki: v223
date: 2026-07-22
stance: "On-goal (Goal #1). The payoff is READ the harness-emulation design + BORROW the 'match the harness to the model' cost lever, and optionally scratch-trial — NOT adopt it into hireui (hireui is Claude-Code / operator-installs / GitNexus-first per its CONSTITUTION)."
one_thing_path: "A1 → B7 → (optional) C11"
---

# openinterpreter — Pilot Methods Menu (24 methods, honestly weighted)

> **Blunt framing.** Open Interpreter (Rust) is a genuinely useful, install-able, open-source coding agent — but it is a **general coding CLI optimized for cheap/open models**, not a recruitment tool and not a Claude-first tool. So most of the value is **read + borrow**, plus an optional low-risk scratch trial as a **cost lever**. Nothing here productizes into hireui. ⭐ **One-thing path: A1 → B7 → (optional) C11.**
>
> ⚠️ **NOT source-cloned** (the v200→v222 self-throttle) → treat all install steps as untrusted-until-inspected. Every hands-on rung is fenced.

## A — Read & learn (zero install, highest ROI)

- **A1 ⭐ — Read the harness-emulation design.** Study what the `/harness` options actually contain — especially **`claude-code` vs `kimi-code` vs `native` vs `minimal`**. This is a rare, concrete "what makes Claude Code's harness effective, by contrast" artifact. Internalize the thesis: *the harness (system prompt + tool schemas + loop), not just the model, drives agentic performance.*
- **A2 — Read the Codex-fork delta.** OI is a fork of OpenAI Codex CLI. Skim the README's Codex-SDK-compatibility + native-sandboxing sections to see what OI *added* (the harness-emulation layer + open-model tuning) vs what it *inherited* (the Codex agent loop).
- **A3 — Map the harness-engineering thread.** Connect OI to the vault's existing harness-engineering subjects (TNT-Cursor-CLI-factory / Archon / Adaptive-engineering / loop-engineering v189 / grok-build v215) — OI is the *productized* form of "the harness is the lever."
- **A4 — Read the ACP integration.** `interpreter acp` = OI as an ACP agent in Zed-class editors. Compare to the ACP appearances at free-claude-code v60 / agent-of-empires v162 / grok-build v215 — reinforce ACP as a Pattern-#18-sub-mechanism-B protocol-variant candidate.
- **A5 — Contrast with the classic Python open-interpreter.** Read the 2023 "natural language interface for computers" README (now `endolith/open-interpreter`) beside the 2026 Rust one — a clean case study in *how a flagship OSS company re-scoped and re-architected its product* (any-task→coding; Python→Rust-Codex-fork; general→cost-optimized).
- **A6 — Read the native-sandboxing model.** How OI sandboxes code execution on macOS/Linux/Windows at the OS layer (vs a Docker requirement) — a security-design reference for "an agent that runs code on your machine."

## B — Borrow patterns (zero install)

- **B7 ⭐ — Steal "match the harness to the model" as a cost lever.** Add to the vault's model-routing / `claude-api-cost-optimization` notes: *for routine agentic coding, a cheap/open model under its NATIVE harness can rival a premium model under a foreign one — reserve Claude for the hard parts.* This is the cc-switch v73 / ai-switcher v153 idea, sharpened to the harness level.
- **B8 — Borrow the harness taxonomy into `05 Skills/`.** Write a one-page "harness = system prompt + tool schemas + turn loop + formatting" reference (with OI's harness list as the worked example) so the vault has a durable model of what a "harness" is when reading future coding-agent subjects.
- **B9 — Borrow the "one binary, swappable harness" architecture idea.** For any future multi-model tool the operator builds: the pattern of *one agent core + pluggable harness definitions matched to the target model* is reusable design.
- **B10 — Borrow the native-sandboxing-not-Docker stance** into the vault's "how to safely let an agent run code" notes (composes with the Strix v190 fence + the loop-engineering v189 L0→L3 discipline).
- **B11 — Document the Codex-fork convergence.** Add a landscape note: the 2026 open-source coding-agent field is *Codex-fork-heavy* (grok-build v215, OI v223, others) — OpenAI's Codex CLI has become the base layer many agents fork, the way Claude Code's design vocabulary went cross-vendor (the grok-build v215 agent-primitive-convergence watch axis).

## C — Hands-on scratch (low-risk trial, fenced)

- **C11 ⭐ — Install-snapshot + scratch trial with a cheap open model.** `install-snapshot` → install OI (prefer inspecting the install script over blind `curl|sh`) → point it at a cheap model (Kimi K3 / DeepSeek / Qwen via your own key or a local model) under its native harness, **native sandboxing ON**, in a **throwaway scratch dir**, on a trivial task. Prove the "cheap-model-under-native-harness" loop actually works before trusting it. Pin **v0.0.34**.
- **C12 — Bake-off: same task, different harnesses.** Run one small coding task through `native` vs `claude-code` vs `kimi-code` on the same model and observe the behavior delta — the fastest empirical way to *feel* what harness-emulation buys.
- **C13 — Bake-off: OI-cheap-model vs Claude Code.** Run a routine refactor/test-write task through OI (cheap model, native harness) and through your normal Claude Code, compare quality + cost. Decide empirically where the "reserve Claude for hard parts" line is.
- **C14 — Try OI as an ACP agent in an editor.** `interpreter acp` in a Zed-class editor on a scratch repo — evaluate the embedded-agent UX vs terminal.
- **C15 — Local-model path.** If the operator has the local-AI-coding-agents setup (topic: Qwen3.6 + MLX + LM Studio), run OI against a fully-local model under its native harness = 100% offline agentic coding (the data-residency angle).

## D — hireui / Goal #2 (mostly "don't"; borrow-only)

- **D16 — Borrow the cost-lever THESIS into hireui's future LLM-feature spec, not the tool.** When hireui builds its first LLM feature (Match-Explain / candidate-summariser, per the RATIFIED candidate-LLM legibility ADR + the Mosh A2 seam), record the "cheap-model-under-native-harness for routine, premium for hard" principle as a *cost-design note* — but hireui stays Claude-Code / official-keys per its CONSTITUTION.
- **D17 — ⚠️ Do NOT run OI against hireui.** It runs code on your machine (native sandboxing helps, but candidate PII + the CONSTITUTION [I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first / Claude-Code]). If ever trialed on hireui code, scratch clone only, sandboxing on, no candidate data, operator-installed.
- **D18 — Contrast for hireui's own agent-nativity work.** OI's harness layer is a reference for *how a product exposes different agentic surfaces* — a light input to the palmier-pro v192 / geti v213 "hireui agent-nativity" thread (read-only).

## E — Off-goal / personal

- **E19 — Personal cheap-model coding agent.** If you want an agentic terminal coding companion that runs on cheap/open models (Kimi K3 / DeepSeek), OI is a legitimate daily-driver option — BYO keys, native sandboxing, scratch projects first.
- **E20 — Follow the Open Interpreter company's pivot.** As a Scrum-coach / builder, the Python→Rust-Codex-fork re-scoping is a real case study in OSS product strategy (kill your darling flagship, hand it to the community, rebuild for the current wave).

## F — Vault-meta / audit

- **F21 — File the §C standalone + NO-MINT alternative** ("Harness-Emulation Coding Agent," N=1, corpus-first-for-surface NOT world-first) into `_patterns/06` §C + §F.
- **F22 ⭐ — Feed the OVERDUE coding-agent-products meta-cluster audit.** OI is now the 4th distinct-capability standalone in the coding-agent space (Kilo Code v177 / grok-build v215 / larksuite v143 / CodePilot v161 / **OI v223** + DeepSeek-TUI v72). The ~v221 audit (overdue — last was v212) must decide: cluster into one Library-vocab item, or keep N standalones? Flag prominently.
- **F23 — Record the DeepSeek-TUI-v72 harness-emulation corpus-recursive link** (leaning #57, hand-caveated unverified) for the audit to source-verify or drop.
- **F24 — Add the "harness-engineering as a corpus thread" synthesis** (TNT / Archon / Adaptive-engineering / loop-engineering v189 / grok-build v215 / OI v223 harness-emulation) to the vault's thread map.
