# (C) dsh-TUI — Verdict (v236)

**Subject:** `ccch1mneyyy/dsh-TUI` · npm `@deepseek-harness-tui/dsh-tui` **v0.8.0** · MIT · ~1.7k★/74 forks (page-stated §37.4)
**Author:** **"Chimney"** (`ccch1mneyyy`) — pseudonymous individual, no disclosed affiliation/location. **NOT Anthropic, NOT DeepSeek.**
**Date:** 2026-08-17 · operator-requested · routine **v2.7**

---

## Verdict: GOAL-ALIGNED INCLUDE 3/4 · NO MINT

| Criterion | Call | Reasoning |
|---|---|---|
| **(a) Anthropic-authored / registered vendor-direct** | **FAIL** | Pseudonymous individual (bio 「试图用ai做点东西~」), no disclosed name/employer/location. §41: (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source — **no name/heritage/locale/notability inference**, and the disclosed-individual axis is answered NO. A Chinese-language bio is *not* an (a)-rescue (the v159→v235 discipline). **#19 19a** first `ccch1mneyyy` author. |
| **(b) Goal-relevance** | **MODERATE — keys the tier** ⚠️ STRONG-reviewable | The interaction surface of an autonomous **coding-agent** runtime = the Goal-#1 harness-UI substrate (CodePilot v161 / hermes-webui v227 family); plus a rival ecosystem's **itemised inventory of Claude Code's UX** (the understanding-agent-internals thread: v65 / claude-tap v173 / grok-build v215 / openinterpreter v223); plus the **event-log-as-truth** architecture that maps onto the RATIFIED candidate-LLM legibility ADR. **Held below STRONG:** a *presentation layer* adding **zero agent capability** (no model, tools, memory, orchestration); the host is a rival lab's four-day-old preview; Claude is an aesthetic to clone and an optional backend, not the substrate; nothing here is a hireui component. Cleanly **GA via §31** (MODERATE+); §40 available as a backstop but **not needed** — MODERATE is reached on the merits. |
| **(c) Substance** | **STRONG** ⚠️ MODERATE-reviewable | Real engineering: a **ported (vendored) Ink core** + Yoga layout + 「差分输出」 differential output + virtualised message lists with cached off-screen row heights + replay merging + bounded caches + ANSI/emoji/CJK cell-width handling + cross-platform clipboard + light/dark detection + i18n `/lang zh/en` + `@xterm/headless` testing + an **11-script `verify:*` suite** (incl. `verify:boundary`, `verify:patch-surface`) + CI + `skills/` + presets + docs. **Caveats foregrounded:** the hard parts (agent loop/model/tools/session/persistence) are **all upstream in v235**; **no automated end-to-end tests with real credentials — manual terminal verification** (author-stated); `/vim` `/connect` `/hooks` are **inert placeholders**; pinned to `^0.1.0-rc.6` of a preview promising breaking changes; stars page-stated → **NOT #52**; **NOT source-cloned**. |
| **(d) Corpus fit** | **STRONG** | v235 host (#57) · v72 DeepSeek-TUI boundary · §C#27 CodePilot v161 · hermes-webui v227 · Codex-Dream-Skin v216 floor · grok-build v215 convergence · openinterpreter v223 axis · pi v228/v36 via the host's `llm-pi-ai` seam · #84 84c · #12 · #66. |

**⚠️ The v216 discriminator (load-bearing).** Codex-Dream-Skin v216 was a UI layer for a rival's tool and was rated **OFF-GOAL, (b) FAIL** — it was CSS wallpaper injected over an Electron app, with **zero** functional surface. dsh-TUI implements the **entire interaction layer**: session lifecycle (`/resume` `/new` `/compact` `/export`), streaming reasoning display, context/TPS/cache observability, rewind-and-fork, structured tool cards, completion, and skills/MCP/subagent surfacing. Functional agent UX, not decoration → **(b) MODERATE, not FAIL.** Same shape as the v217-vs-v216 reasoning already recorded.

---

## Pattern outcome: **NO MINT** · counts **46/11 UNCHANGED** · §C live standalones **49 unchanged** · surface **≈56 unchanged**

### Primary: a front-end for an existing agent — a form factor within an already-declined genre

The corpus has ruled on this shape **twice**:

- **hermes-webui v227** — a community web UI for someone else's agent. §C mint **DECLINED** (form-factor-within-genre + not world-first + §28); the **lobehub v222** precedent was called decisive.
- **Codex-Dream-Skin v216** — a UI layer for a rival's tool. **NO MINT** (cosmetic/UI theming is not a mintable agent-capability class; §C vocab is capability-shaped).

dsh-TUI is a front end (terminal flavour) for an agent runtime. The same rule applies: **NO MINT.**

### ⚠️ The §C-mint alternative, recorded and DECLINED

*"Third-Party Replacement UI Layer Mounted as a First-Class Plugin Inside an Agent Runtime — the host retains agent loop / model / tools / session / persistence; only the UI seam is swapped, non-invasively, with the boundary enforced in CI."*

**Genuinely distinct on mechanism** — and hand-checked against every near neighbour:

- **CodePilot v161 §C#27** — a GUI that **wraps** a CLI agent from outside (spawns/drives it). dsh-TUI mounts **in-process**. Opposite direction → **NOT a clean §C#27 N=2** (the v227 "distinct on two axes → adjacency, not the N=2" handling).
- **hermes-webui v227** — a separate web server fronting an existing install; not a plugin inside the host's kernel.
- **Codex-Dream-Skin v216** — *unsanctioned* CDP injection into a running binary; dsh-TUI is a **sanctioned plugin** using the host's own extension kernel.
- **DeepSeek-TUI v72** — a standalone single-vendor terminal **client** for DeepSeek **models**; dsh-TUI is a UI **plugin** for a coding-agent **runtime**.

**It still loses, on four grounds:**

1. **The v227 / v222 / v216 precedent chain** — front-ends and UI layers are form-factor variations, not new classes.
2. **Presentation-not-capability** — §C vocab is agent-capability-shaped, and this adds no capability the host lacked.
3. **§28 anti-inflation** — minting on a delivery mechanism is the "draw-the-circle-to-make-it-first" move declined at camofox v179 / lobehub v222 / Firecrawl v214.
4. **A weak, undistinctive anchor** — one plugin among ~**1,120** in a four-day-old ecosystem that already contains a **rival UI-layer plugin** (`dsh-desktop`). Not world-first either (`gignit/claude-tui` builds a CC TUI on Anthropic's official Agent SDK; Claude Squad / tmuxcc / agent-deck / agent-manager / ralph-ai-tui populate the terminal-UI-for-agents space).

Recorded as a corpus-knowledge data-point + a **DEFERRED watch axis**: *"sanctioned in-process UI-seam replacement via a host agent's own plugin kernel"* — flagged to the badly-overdue audit, **not executed**.

### SECONDARY (recorded, NOT minted)

- ⭐ **#57 genuine corpus-recursion, of a NEW relation shape.** dsh-TUI *runs inside* v235 via **21 declared `@deepseek-ai/*` peer deps at `^0.1.0-rc.6`** — the most machine-checkable recursion form the corpus holds (a lockfile edge, not a citation). ⚠️ **NOT a corpus-first for consecutive-ship recursion** — v207→v208 (a **port**) and v231→v232 (**credited priority**) precede. What *is* new is the **relation type: host↔plugin (runs inside)** rather than port / fork / bundled-dependency / citation. Whether the #57 taxonomy needs a "runs-inside-a-prior-subject's-plugin-kernel" sub-variant is an **audit** question; N-tally is audit bookkeeping, **not self-incremented**.
- ⭐ **External validation of v235's headline thesis, four days later.** v235 claimed the UI was a hot-swappable Cordis plugin; v236 is an unaffiliated third party swapping it, keeping every other seam, and **proving non-invasiveness in CI** (`verify:boundary` / `verify:patch-surface`). The corpus rarely gets a thesis tested this fast, by a stranger, with mechanical evidence. **A corpus-knowledge finding, not a mint.**
- ⭐ **v235's append-only session log confirmed load-bearing** — the UI reconstructs history, rewind boundaries, and post-fork state purely by replaying the host's `session/event` log, keeping only a projection (「Channel 只保留适合当前 TUI 的投影」). Directly reinforces the **RATIFIED candidate-LLM legibility ADR**.
- ⭐ **grok-build v215 "agent-primitive convergence" axis MATERIALLY EXTENDED to the presentation layer** — not just skills/subagents/hooks/plan-mode/MCP but the **rendering stack** (forked/ported Ink + Yoga + ANSI diffing + virtualisation) and the **keybindings** (`Esc Esc` rewind, `/compact`, `/resume`). ⚠️ Claude Code's internals here are **third-party reverse-engineered**, not Anthropic-documented (the v65 / v205 provenance discipline). **NOT #57** — no corpus subject is cited.
- ⭐ **A third consecutive ship handing the vault machinery for its own invariants** (v234 staleness-tracking + recompilation → v235 doc-verification gates → v236 CI-enforced architectural boundary). A pointed comment on the C22–C27 stale-row backlog and the deferred retire pass.
- **DSH plugin land-rush data-point** — ~1,120 plugins across ≥8 competing, operator-undisclosed directory sites within days of v235's preview; **revises v235's 19%-compatibility / "wait 3–6 months" picture** while leaving the stability caution intact.
- **Provenance failure caught** — `dshhub.org` publishes **v0.3.3 / BSD-3-Clause** against the repo's **v0.8.0 / MIT**. Repo authoritative (the **Kilo Code v177** licence-discrepancy precedent). Do not trust the directories' metadata.
- **#19 19a** first `ccch1mneyyy` author; author portfolio note — their own `working-activity` (648★) is the `dsh-working-activity ^0.2.6` dependency this plugin pulls in, i.e. a second package in the same ecosystem. *(Their `pi_pilot` repo is a Dart mobile-control app — whether "pi" refers to the corpus's pi v228/v36 or a Raspberry Pi is **unverified and relied on for nothing**.)*
- **#84 84c** — provider-agnosticism is **inherited from the host's `llm-pi-ai` seam**, not implemented here. **NO N-bump.**
- **#12** — ships `skills/` + agent presets + a config schema consumed by the host. No N-bump.
- **#66** — MIT; a `prepare` lifecycle script (build-on-install for git/local installs); a **global** `npm i -g` of a 0.8.0 package plus a release-candidate 21-package peer set; the host's DeepSeek-default models mean **PRC cloud egress** unless routed at Claude; the surrounding ecosystem is ~1,120 unvetted plugins indexed by anonymous directories with wrong licence metadata; **NOT source-cloned** → treat the tree as untrusted.

### NON-claims

NOT **#52** (~1.7k★/74 forks page-stated §37.4) · NOT **world-first** (`gignit/claude-tui`, `dsh-desktop`, Claude Squad, tmuxcc, agent-deck, agent-manager, ralph-ai-tui) · NOT **corpus-first DeepSeek-TUI** (v72 precedes; different class) · NOT an **N=2 of §C#27** (mounts-inside vs wraps-outside) · NOT an **N=2 of v72** · NOT **#18 B1-MCP** (ships no MCP server; it *surfaces* the host's) · NOT a new **top-level pattern** (max #85) · NOT **first-party DeepSeek** (third-party plugin) · NOT **the agent** (a UI layer) · NOT a **corpus-first for consecutive-ship recursion** (v207→v208 precedes) · NOT **source-cloned**.

---

## Tier

**T4 Plugin/Extension** — an in-process UI-layer plugin for an agent runtime (the `opencode-antigravity-auth` v67 bridge-plugin tier), with a **T2-client facet** (the CodePilot v161 / hermes-webui v227 front-end family). ⚠️ **Tier reviewable** — the corpus has no clean "UI-layer plugin" tier; flagged the way v192 / v193 / v213 handled tier ambiguity.

## Streak & ceiling

**v235 GA:93 → `GA:94 · OG:13 [7 ov]`** — **17 consecutive GA**.
**§35 CLEAR** — window {v234 GA, v235 GA, **v236 GA**} = 0 OG.
⚠️ Reviewable OFF-GOAL alternative: if (b) is weighted FAIL on "it is only a skin for a rival lab's runtime" → `GA:93 · OG:14`, and §35 would still be CLEAR (1 OG ≤ 1). **Recorded GA primary on the merits** — the v216 discriminator above is the reason.

## `inflation_check`

**HELD.** 0 mints; the §C-mint alternative recorded and declined on four grounds; counts **46/11 unchanged**; §C live standalones **49 unchanged**; max top-level pattern **#85**; no N-bumps (#84 84c NO bump, #57 recorded-not-self-incremented, #12 no bump); no double-count.

---

## Pilot call

**⚠️ Read-and-borrow. Do NOT install. NOT a hireui component.**

Installing means a **global** npm install of a v0.8.0 plugin against a **four-day-old release-candidate** runtime (21 peer deps at `^0.1.0-rc.6`, breaking changes promised in bold by the host's own README), a `prepare` lifecycle script, PRC egress on the host's default models, and an ecosystem of ~1,120 unvetted plugins whose directories publish incorrect licences. The payoff for that risk is a prettier terminal for an agent the operator does not use.

**⭐ One-thing path: A1 → B5 → B6**

1. **A1** — read `docs/architecture.md` + the Claude-Code feature inventory (§3 of the Deep Dive). Zero install. Two returns: a competitor's checklist of what CC's TUI does well, and the event-log-as-truth design.
2. **B5** — write **"the event log is the source of truth; the UI holds only a projection"** into hireui's LLM-integration ADR, composing with v235's append-only-traceability invariant. Two consecutive ships now converge on the same rule; the RATIFIED candidate-LLM legibility ADR already demands it.
3. **B6** — steal **`verify:boundary` / `verify:patch-surface`**: encode an architectural boundary as a CI gate rather than a paragraph. Applies to hireui and, more pointedly, to the vault's own stale-row invariants.

**Fence (if trialled at all):** scratch container only · `--ignore-scripts` · pin `@deepseek-harness-tui/dsh-tui@0.8.0` **and** the exact rc peer set · route the model at **Claude via the host's `llm-pi-ai` seam**, never the DeepSeek default · **never candidate data** · ignore plugin-directory metadata (proved wrong) · NOT source-cloned → treat the tree as untrusted · hireui stays hand-built per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first).

---

## Blunt summary

**A pseudonymous developer re-skinned a rival lab's brand-new agent runtime to look and feel like Claude Code — and in doing so accidentally produced the best available proof that v235's "everything is a plugin" claim and its append-only session log are real.** The plugin itself is a presentation layer on a release candidate: don't install it. The two ideas inside it — *event log as the only source of truth* and *architectural boundaries enforced in CI* — are worth taking today, for free.
