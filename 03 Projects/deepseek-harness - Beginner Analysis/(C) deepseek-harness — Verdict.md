# (C) deepseek-harness — Verdict (v235)

**Subject:** `deepseek-ai/deepseek-harness` (`dsh`) · MIT · `0.1.0-rc.5` · released 2026-08-13
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts **46 / 11 UNCHANGED**
**Streak:** v234 GA:92 → **`GA:93 · OG:13 [7 ov]`** (16 consecutive GA) · **§35 CLEAR** (window {v233 GA, v234 GA, **v235 GA**} = 0 OG)
**Tier:** **T5 Agent-as-application** — agent-runtime / harness-kernel flavor (the grok-build v215 / Kilo Code v177 / OpenHands v30 tier) + a T2 self-hosted-service facet.

---

## Four-criteria assessment (routine v2.7)

### (a) FAIL
DeepSeek AI — a Chinese frontier-model lab, **not Anthropic** (§41: no name/heritage/locale/notability inference; a declared Anthropic affiliation or a registered (a)-7 vendor-direct source is required). The declared-non-Anthropic-institution situation: ByteDance v143/v221 · NVIDIA v169 · Google v140/v193 · Microsoft v178 · Intel v213 · xAI v215.

**#19 19a — RETURNING institution.** DeepSpec **v186** was the corpus's first *first-party* `deepseek-ai` org subject; this is the **second**. (DeepSeek-TUI **v72** was third-party — `Hmbown` — so it does not count toward first-party priority.)

### (b) STRONG — keys the tier, cleanly GA (no §40 needed)
This is an **autonomous agent runtime for software development** = Goal #1 core, and it lands on the Claude/agent substrate at four separate points, all source-verified:

1. **Claude is a first-class model** — via `packages/llm/llm-pi-ai` (OpenAI · **Anthropic** · DeepSeek · Azure · Bedrock · Vertex).
2. **Claude Code is a first-class *subagent*** — `subagent-claude-code` "starts a real Claude Code child through the **official Claude Agent SDK**."
3. **Claude Code hooks are bridged** — `packages/hooks/` runs your existing `hooks.json`.
4. **It reads CLAUDE.md** (and AGENTS.md).

Plus it is dead-center on live vault threads: harness-engineering, multi-agent orchestration, the agent-primitive-convergence watch axis, MCP-client posture, context compaction, and the claude-api-cost-optimization thread (the ~10×-token critique is a cost datum).

**STRONG, not STRONGEST:** third-party; a competitor lab's runtime; DeepSeek models are the shipped default with Claude reachable through a wrapped third-party seam; and it is a *developer preview* with no evaluation story. Comfortably above the (b) MODERATE floor — no §40 rescue required, and an OFF-GOAL reading is not defensible.

### (c) STRONG (with substantial, foregrounded caveats)
~453K lines of TypeScript · ~219 workspace packages · ~170K lines of docs · **1,386 decision records** · real cross-platform sandboxing (bubblewrap→Landlock / seatbelt / write-restricted token) · a genuine disposability kernel · MIT · 12,293 commits · an unusually dense CI gate suite (dozens of `verify-*` scripts covering docs, links, catalogs, licenses, package invariants and type equivalence).

**Caveats, load-bearing:** developer preview `0.1.0-rc.5` with breaking changes promised in bold · **ecosystem compatibility ~19%** (41/219) · **~10× token usage vs Pi** · a confirmed context-duplication bug · **`BENCHMARK.md` is a 3-line stub, no eval harness, zero evaluation claims** · squashed-merge history ("contributor-hostile") · a `postinstall` script · **⚠️ NOT source-cloned**.

### (d) STRONG
grok-build v215 (the N=2 candidacy) · **pi v228/v36 (#57 dependency + the 10× yardstick)** · llm-space v221 (the other Pi-dependent subject) · openinterpreter v223 (emulate-vs-delegate contrast) · DeepSpec v186 (same org) · DeepSeek-TUI v72 · Kilo Code v177 / CodePilot v161 / larksuite v143 (the meta-cluster) · PilotDeck v175 / cortex-hub v181 / lobehub v222 · headroom v144 (`compaction`) · the #23 family (`lsp`) · open-lovable v224 (`e2b`) · Pattern #12 · Pattern #18 (MCP client).

---

## Pattern outcome: **NO MINT**

Counts **46 top-level / 11 CONFIRMED Library-vocab UNCHANGED**; §C live standalones **49 unchanged**; tracked surface **≈56 unchanged**.

### The load-bearing call: a strong N=2 candidacy, **recorded, NOT self-executed**

The natural home is §C row 102 — **"Open-Sourced First-Party Frontier-Lab Agentic Coding CLI/TUI (a frontier AI lab's OWN official agentic coding agent, released as full open source and studiable as a primary subject … the Claude Code / Codex CLI / Gemini CLI vendor peer class)"**, `N=1`, anchor **grok-build v215**.

deepseek-harness satisfies every **essential** axis of that row:

| Essential axis | dsh |
|---|---|
| A frontier AI lab | DeepSeek AI ✅ |
| Its OWN official agentic coding agent | `dsh` ✅ |
| Released as full open source | MIT ✅ |
| Studiable as a primary subject | 453K LOC, public ✅ |
| The Claude Code vendor peer class | VentureBeat's literal framing ✅ |

It differs on the row's two **descriptive** clauses:

- *"terminal-TUI-first"* → dsh is **web-UI-first** (`dsh web` → :3080; a `packages/terminal` exists but the documented entry point is the web UI).
- *"single-vendor-model"* → dsh is **multi-vendor** through the pi-ai seam.

That is precisely the shape the **v212 audit** resolved for the v192 row when it generalized a descriptive clause ("in a non-coding domain" → "any domain whose primary function is not being an agent tool").

**But row 102 is `PROMOTION-ELIGIBLE at a genuinely-independent N=2`.** Declaring the N=2 here would **silently fire a promotion to CONFIRMED Library-vocab and change the headline counts.** That is exactly what the **v232 ship refused to do** to the v207 row, on the record: *"generalising it would sweep these two in as instances #3/#4 and SILENTLY FIRE a promotion-to-CONFIRMED trigger that changes the headline counts. **A promotion is an audit act.**"*

The same discipline binds here. **Recorded as the strongest available N=2 candidate for row 102; flagged prominently to the badly-overdue audit; not executed.**

### ⚠️ Reviewable alternative recorded, NOT self-executed

**MINT a new §C standalone at N=1** — *"Frontier-Lab Plugin-Composable Agent Runtime / Harness Kernel: a frontier lab open-sources not a coding-agent product but the agent RUNTIME, on a third-party disposability meta-framework, where every capability — including the main agent loop, the UI, the scheduler, storage and the sandbox — is a hot-swappable plugin, and rival first-party harnesses (Claude Code, Codex) are themselves pluggable subagent providers."*

It is **corpus-first for that surface** (hand-checked against all 49 live §C rows: `plugin-composable` 0 · `plugin-first` 0 · `everything is a plugin` 0 · `Cordis` 0; the nearest rows — PilotDeck v175 WorkSpace-isolation agent OS, Kilo Code v177 IDE-embedded, llm-space v221 dev workbench, openinterpreter v223 harness-emulation — are each a different object). Not world-first, which per the v232 finding has never independently blocked a §C row.

**It loses**, for three reasons:

1. **A well-fitting existing row already exists** (102). Minting a fresh row when the subject satisfies an existing row's essential axes is exactly the phantom-count inflation **§28** exists to prevent — the assignment is blocked by a *governance* rule, not a substantive mismatch.
2. **Packaging-not-capability risk** — "plugin architecture" is a densely populated world class, and the corpus has twice declined to mint on architecture/packaging for far larger anchors (**cortex-hub v181**, **lobehub v222** at 80.6k★).
3. **Anchor maturity** — a four-day-old developer preview with 19% ecosystem compatibility, no eval harness, a known duplication bug and promised breaking changes is a weak anchor for a new capability class, whatever its star count.

Either reading leaves counts **UNCHANGED 46/11**.

---

## Secondary (recorded, NOT minted)

- **⭐ #57 GENUINE — `@earendil-works/pi-ai`** (= **pi v228**, the revisit of **v36 pi-mono**) backs the entire multi-provider LLM seam. A **declared, named, npm-linked dependency** — the strongest #57 form (the llm-space v221 shape), materially stronger than cortex-hub v181's silent bundling. ⚠️ The `llm-pi-ai` README links the package but carries no separate acknowledgment of Pi as a project; characterized precisely, not inflated. N = audit bookkeeping, recorded not self-incremented.
- **⭐ Pi is now a two-lab dependency** — llm-space v221 (ByteDance/DeerFlow) *and* deepseek-harness v235 (DeepSeek). A corpus-level observation worth an audit note.
- **Cordis / shigma / Koishi** — the corpus's first Cordis subject; DeepSeek vendors + rescopes it as `@deepseek-ai/cordis` **with** third-party-notice and license-verification CI gates → attributed vendoring (contrast cortex-hub v181).
- **#12 LLM-routing-artifacts** — reads AGENTS.md + CLAUDE.md (NO N-bump).
- **#18 MCP — client-only**, explicitly: *"dsh consumes MCP servers, it does not present itself as one."* → **NOT a #18 B1-MCP subject** (the pi v228 / lobehub v222 handling).
- **ACP** — `packages/acp` + `subagent-acp` + `@agentclientprotocol/sdk` + `demo:acp`. The Pattern #18 sub-mechanism-B protocol-variant candidate (free-claude-code v60 / AoE v162 / grok-build v215 / openinterpreter v223). **ACP ≠ MCP.** Not corpus-first, not a §C standalone.
- **Agent-primitive convergence** (the grok-build v215 DEFERRED watch axis) — **materially reinforced**: DeepSeek adopts skills/subagents/hooks/plan/MCP/ACP wholesale *and* consumes Anthropic's own `hooks.json` format and Claude Agent SDK. NOT #57 (a convention, not a citation).
- **NEW DEFERRED watch axis — "harness delegation vs harness emulation"**: openinterpreter v223 *reimplements* a rival harness; dsh *spawns the real one via its vendor SDK*. Two opposite answers to the same problem, one wiki apart.
- **#83 honest-disclosure POSITIVE** — the Windows sandbox gap ("reads, network, and process visibility stay unrestricted") is documented rather than hidden.
- **#84 84c** provider-agnostic by design (NO N-bump — inherited from pi-ai, not dsh's own mechanism; not the ponytail v168 generator).
- **#66 supply-chain — MODERATE.** MIT · `npx`/npm install · **a `postinstall` script** (`install-lefthook.mjs`) · 219 workspace packages + vendored deps = a large surface · squashed-merge history = provenance opacity · real sandboxing but **Windows reads/network/process unrestricted** · ⚠️ **DeepSeek models are the shipped default → PRC cloud egress** if pointed at sensitive data (the llm-space v221 BytePlus / agentic-local-brain v234 DashScope fence). ⚠️ Pointed irony: the runtime depends on **pi v228**, the corpus's strongest supply-chain *positive* exemplar (`--ignore-scripts`, lifecycle allowlist, `min-release-age=2`, shipped shrinkwrap) — and does not follow that discipline.

## NON-claims

NOT **#52** (~92.7k★/28h → ~138.5k★ page/press-stated; §37.4 mocked API → velocity unestablishable) · NOT **#18 B1-MCP** (ships no MCP server) · NOT **world-first** · NOT the corpus's first `deepseek-ai` subject (**DeepSpec v186**) · NOT the first DeepSeek-related subject (**DeepSeek-TUI v72**, third-party) · NOT an executed N=2 of row 102 (candidacy recorded only) · NOT a §C mint · NOT a new top-level pattern (max #85) · NOT the model tier (V4-Pro/Flash are the models; dsh is the harness) · NOT harness-emulation (openinterpreter v223) · NOT source-cloned (flagged).

---

## Verification

Produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — **no workflow, no subagent** (the oversized shim overflows every subagent >200K → prompt-too-long; the v200→v234 self-throttle).

**Collision by sanity-anchored hand-grep — CLEAN.** `deepseek-harness` / `deepseek_harness` = **0 hits** across `_state/` + `_patterns/`; anchors **DeepSpec 56 · DeepSeek-TUI 115 · openinterpreter 50** hit richly → the grep works, so the zero is trustworthy. All 49 §C row titles read directly; row 102 (grok-build) and row 104 (openinterpreter) read in full.

**Three errors caught by hand:**

1. **The provider contradiction** — press said "~40 providers incl. Anthropic," a code-level read said "ships exactly two models." Both true; reconciled only by fetching `packages/llm/` (five dirs, **no `llm-anthropic`**) and `llm-pi-ai/README.md`. Breadth comes from **one** wrapped SDK, not 40 adapters. Reported as verified-six + press-stated-forty.
2. **The Claude Code integration mechanism** — a press summary said "resolves the binary from the host PATH"; the repo says **"through the official Claude Agent SDK."** Source wording used.
3. **The first WebFetch summary asserted the README mentions no MCP/Claude/Anthropic** while simultaneously noting `.claude` paths — self-contradictory. Resolved by fetching the raw README (the terms genuinely are absent *from the README*) and then the package tree (where the capabilities plainly exist). Had I trusted the summary, the ship would have concluded dsh has no Claude surface — inverting (b).

`inflation_check` **HELD**: 0 mints; the §C-mint alternative recorded and declined on §28 grounds; the row-102 N=2 candidacy recorded, not executed (promotion = an audit act, the v232 precedent); counts 46/11 unchanged; max #85; no improper N-bumps (#84 84c none, #12 none, #57 recorded not self-incremented).

---

## Pilot posture

**⚠️ Read-and-borrow. Do not adopt.** A four-day-old developer preview with promised breaking changes, 19% ecosystem compatibility, ~10× token usage vs Pi and zero evaluation claims is not something to put in front of real work — its own critics suggest a 3–6 month wait. It is **not** a hireui component.

**⭐ A1 → B5 → B6.** See `(C) deepseek-harness — Pilot Methods Menu.md`.

**Fence:** never `npx` it into a real project (scratch dir only) · install-snapshot first (it has a `postinstall`) · pin `0.1.0-rc.5` · BYO key, and if you must run a model, route pi-ai at Claude rather than the DeepSeek default (**PRC cloud egress**) · never point it at candidate data · **never** enable self-modifying toolsets · verify the sandbox mode on your platform (Windows leaves reads/network/process visibility open) · NOT source-cloned → treat the 219-package tree as untrusted.
