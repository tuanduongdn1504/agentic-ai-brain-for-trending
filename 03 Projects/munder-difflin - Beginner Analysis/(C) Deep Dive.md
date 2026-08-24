# (C) Deep Dive — `chaitanyagiri/munder-difflin`

> **v273 · LLM Wiki ship · 2026-08-24 · routine v2.8**
> *"Munder Difflin — Agent harness to run an office of your clones."*
> Verdict: **GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts 46/12 UNCHANGED.
> **Claude-authored** under operator direction. Every number below is the output of a command run in a verified clone; where a figure came from a fleet agent and I did not re-run it, it is marked **[fleet]**.

---

## 0. Source verification

Two independent clones, `diff -rq --exclude=.git` → **0 differing lines**, both at HEAD `9e99edc982de4424872260efd00ebc76fdc8dfcf` (2026-08-24, the day of this ship). Not a fork.

| Fact | Value | Command |
|---|---|---|
| Commits (all refs) | **986** | `git rev-list --count --all` |
| Commits on `main` | **938** | `git rev-list --count HEAD` |
| Roots | **1** — `dc7f1ce7` *"inception"*, 2026-05-31 05:08:03 +0530, Chaitanya Giri | `git rev-list --max-parents=0 --all` |
| Merges | 188 all refs / **179 on main** | `git rev-list --merges --count` |
| Tags | **35** — `v0.1.1` … `v0.4.5` (incl. `v0.4.4-rc.1`) | `git tag` |
| Tracked files | **1,785** | `git ls-files \| wc -l` |
| Working tree / `.git` | **172 MB / 83 MB** | `du -sh` |
| Version | **0.4.5** (package.json, newest tag, CHANGELOG all agree) | |
| Licence | **MIT**, © 2026 Chaitanya Giri, source-code-only scope note | `LICENSE` |

**Commits by month:** 2026-05 = **3** · 2026-06 = **540** · 2026-07 = **44** · 2026-08 = **399**. A three-month-old project with a June explosion, a July trough and an August second wind.

**Code:** TypeScript **38,907** lines (136 files) + TSX **23,513** (80) = **62,420** first-party lines; `.cjs`/`.mjs` **12,507**; Markdown **25,654** (187 files); HTML **93,498** (287 files, almost all generated blog output); Python **419** (3 files). Plus one 12 MB minified JavaScript file at the repository root — see §12.

**Authorship on `main` (938 commits):** Chaitanya Giri 722 (77%), Gulum 56, Vyapak Goyal 52, github-actions[bot] 19, Gastón Péchieu 17, Ed Chan 7, Zhen Luo 6, Piotr Durlej 6, George Burchell 6, wall-sync 5, Quentin Schmick 5, rajpreetcodes 3, and a long tail. **This is a genuinely multi-contributor project** — roughly a fifth of `main` is outside work, merged, not parked in branches.

Author email `16ucc028@lnmiit.ac.in` (LNMIIT, Jaipur). **Not Anthropic** → criterion (a) FAILS under routine §41 (no name/locale/notability inference).

---

## 1. What it is

An Electron desktop application that takes the terminal agent CLIs you already run — `claude`, `agy`, `codex`, `grok`, `kimi`, `qwen`, `opencode`, `crush`, `pi`, `copilot`, `cursor-agent` — spawns each as a **real process in a pseudo-terminal** (`node-pty`, rendered with xterm.js), gives each one **long-term memory, a mailbox and a desk**, draws them as **avatars walking around a 2D office floor** (Pixi.js), and puts a privileged **"god" agent called Michael** in charge of routing work between them.

The name is a *The Office* parody (Dunder Mifflin → Munder Difflin); the agents are named after the cast. `README.md:351-352` carries the disclaimer: *"Munder Difflin is an affectionate parody and is not affiliated with NBC's The Office or Dunder Mifflin."*

Stack: Electron 32 · React 18 · TypeScript · Pixi.js 8 · xterm.js · node-pty · better-sqlite3 · Monaco · zustand · `@openai/agents-realtime` (voice) · posthog-node (telemetry) · tunnelmole (Slack/webhook tunnels).

**It is not a wrapper around an API.** It is a wrapper around *your subscription*, and it says so in code — see §4.

---

## 2. The hive: architecture, and which claims the code keeps

`HIVE.md` (11.5 KB) is the design source of truth for the agent layer. It is unusually literate: it maps each requested behaviour to a **named academic pattern** and cites the closest analogue.

> `HIVE.md:19-30` — per-agent memory → **agent long-term memory** (MemGPT/Letta-style); writing a requirement into another agent's file → **stigmergy**; a shared plan many agents edit → **blackboard architecture (Hearsay-II)**; "check after finishing every task" → **mailbox / actor model**; a god agent that runs the floor → **orchestrator / supervisor** (LangGraph-supervisor-style). Closest academic analogue: Stanford's *Generative Agents* (Park et al., 2023).

The fleet checked all four named citations and found them **correctly attributed** [fleet]. Note for the corpus: `stigmergy`, `blackboard` and `Generative Agents` return **zero** hits across `CLAUDE.md` + `_state/` + `_patterns/` — this subject introduces that vocabulary to the corpus.

### The locked decisions, and their implementations

| `HIVE.md` decision | Implemented? | Evidence |
|---|---|---|
| **"Git as the coordination/audit layer, single committer."** Only the Electron main process commits, to avoid `.git/index.lock` corruption with many concurrent agents | **Yes** | `src/main/hive.ts` `commit()` runs git with `-c user.name=Hive -c user.email=hive@local`, retries with backoff on `index.lock`, and clears a stale lock older than 10 s (`hive.ts:2376`: `Date.now() - statSync(lock).mtimeMs > 10_000`) |
| **"Single-writer-per-file."** Each agent writes only inside its own `agents/<id>/`; a router moves messages outbox→inbox | **Yes** | `atomicWriteJson()` (temp-file + rename); **`startRouter()` / `routeOnce()` scan `outbox/` and deliver** — a first-pass fleet agent claimed the router was missing and its adversarial verifier **refuted that** with `sed -n '1548,1582p' src/main/hive.ts` |
| **"God-mode autonomy, native HITL."** Critical items surface to the human in the god's own Claude Code session; *"Tool-permission prompts are the HITL gate"* | **Partly — and the default configuration contradicts it.** See §5 | `config.ts:191`, `DEFAULTS.autoMode: true` |
| **"Memory: markdown first."** Per-agent `memory.md` + blackboard + a SQLite FTS index when keyword recall isn't enough | **Yes** | see §6 |
| **"Autonomous loop = `Stop` hook."** An agent that finishes drains its inbox via a `Stop` hook returning `{"decision":"block",…}` to keep working | **Deliberately abandoned, for a safety reason the code states** | see below |

### The reversal the document never recorded

`src/main/hooks.ts`, in the `Stop`/`SubagentStop` branch:

> *"Never turn unread hive mail into a forced continuation at Stop. That old path bypassed terminal-draft/HITL safety and **could spend credits while a user was answering a question**. Inbox files remain durable; the renderer wakes the agent later through its guarded idle-only delivery path."*

So `HIVE.md` still specifies a mechanism the code removed **because it was unsafe**, and the code documents the reversal at the site of the change. The design doc is *behind the code in the safe direction here*, and *ahead of it in the unsafe direction* on HITL. A stale document is not "behind" — it is wrong in whichever direction each individual sentence happened to age.

### The one insight in `hooks.ts` worth stealing outright

> `src/main/hooks.ts` — *"7C.1 — HITL gate: deny a tool call at the PreToolUse boundary when the agent is paused or this tool is gated. **Race-free (immediate return, no renderer round-trip → can't hit the shim timeout). Slow human APPROVAL is deliberately left to Claude's native permission prompt.**"*

**In a hook you can afford to say no; you cannot afford to wait for a yes.** A hook must answer inside a timeout, so DENY is computable locally and APPROVE is not. That is a correct and non-obvious piece of hook design, and it generalises to every hook anyone writes.

`hooks.ts` also carries a **circuit-breaker compaction exemption** (`PreCompact` opens it so the compaction token burst cannot trip the output-delta arms; `PostCompact` *or any* `SessionStart` closes it, "since a fresh session makes in-flight compaction state moot"), and injects `additionalContext: [roster, goal, steer]` at a hook boundary.

---

## 3. The circuit breaker — the best 24 lines in the repository

`src/main/breaker.ts` (347 lines) exists because of one observation:

> *"Claude Code exposes `--max-turns` but **NO dollar ceiling, so we enforce one ourselves.**"*

Its header is a masterclass:

- **Policy/enforcement separation** — *"This module owns the POLICY only … It has no side effects: it reads signals and returns decisions; the caller … performs the enforcement."*
- **The measurement trap, named** — *"Velocity is the DIFF of consecutive cumulative samples (Δoutput/Δt), **never a single sample treated as an increment**."*
- **A safe-by-construction ladder** — *"steer-first, one level per beat (never jump to a kill), de-escalates a level per healthy beat (recovery), and `hardStop` is OFF by default — without it the ladder caps at `constrained` and never kills."*
- Three input sources: usage samples (cost + token velocity), hook events (repeated identical tool calls, api_error storms), and file-mtime no-progress.

**And it has tests** — `test/breaker.test.cjs` and `test/cost-lifetime.test.cjs`. Hold that thought until §8.

---

## 4. How it drives Claude Code

This is the section that matters most for a reader who runs Claude Code daily.

### Two spawn paths

**(a) Persistent agents** — `spawnAgentCore` writes a per-agent `settings.json` and passes `--settings <path>`, plus `--append-system-prompt` carrying the hive protocol. The settings file defines **nine lifecycle hooks** — `PreToolUse`, `PostToolUse`, `Stop`, `SubagentStop`, `UserPromptSubmit`, `SessionStart`, `Notification`, `PreCompact`, `PostCompact` — each as `{type:'command', command:<node-shim>}`. The shim forwards the hook payload over a **Unix domain socket** (`HIVE_SOCK`) to the `HookServer` in the Electron main process [fleet, mechanism confirmed by my own read of `hooks.ts`].

**(b) Hidden ephemeral sessions** — `src/main/hiddenClaude.ts`. *"'Hidden' means: not added to the PtyManager, not emitted to the renderer, not visible in the agent list or OfficeFloor scene. Each call spawns its own session and kills it after capture — no /clear needed, no context bleed."* Lifecycle: `spawn → boot-quiet detect → bracketed-paste prompt + \r → idle-settle → transcript JSONL extract (last assistant text block) → kill`. It reads the answer out of `~/.claude/projects/**/*.jsonl` (`src/main/transcript.ts:44`).

### ⭐ The economic thesis, in a code comment

> `src/main/hiddenClaude.ts:17-20` — *"Uses an interactive PTY (not `claude -p`) so calls draw from the user's normal interactive plan quota, **not the Agent SDK credit that moves to a separate claim-required pool from 2026-06-15**."*

That is the whole product in one sentence: **drive the subscription you already pay for, through the interface a human would use.** It is a dated, specific, checkable claim about Claude Code billing, and it explains why the harness parses terminal output instead of asking for JSON. (One exception: `reflect.ts` *does* use `claude -p` with Haiku for a cheap summarisation — a deliberate different trade-off, see §6.)

Contrast worth naming: corpus **v207 CLIProxyAPI** and **v208 OmniRoute** re-expose a CLI subscription as an *API for other consumers* — a ToS problem the corpus fenced hard. This does the opposite: it drives your own CLI locally, in a PTY, as you. There is no re-exposure and no proxy.

### What it writes into your home directory

| Path | What | Where |
|---|---|---|
| `~/.claude/settings.json` | sets `skipDangerousModePermissionPrompt: true` **and** `skipAutoPermissionPrompt: true` — **global, not app-scoped** | `config.ts:768-790` |
| `~/.claude.json` | `projects[cwd].hasTrustDialogAccepted = true` — pre-accepts the folder-trust dialog | `config.ts:793-800` |
| `~/.claude/skills` | read **and** written by `src/main/skills.ts:356,435` | |
| `~/.claude/projects` | read (transcript JSONL extraction) | `transcript.ts:44` |
| `~/.gemini`, `~/.codex`, `~/.grok/hooks` | per-engine hook installation | `hive.ts:1805,1879,2091` |

The reason is written down honestly:

> `config.ts:761-765` — *"Without this, a fresh install shows an interactive 'WARNING: Bypass Permissions mode … 1. No, exit / 2. Yes, I accept' prompt that the PTY can't answer in time, so the agent exits code 1 on its own (**reported by multiple users**)."*

**The consequence is the thing to understand:** `skipDangerousModePermissionPrompt` is a *global* Claude Code setting. After one run of this app, your own hand-typed `claude --permission-mode bypassPermissions` in an unrelated project will also stop warning you. **The side effect outlives the application.**

---

## 5. The permission contradiction, stated precisely

Three places say the human-in-the-loop gate is Claude Code's tool-permission prompt:

1. `HIVE.md` decision 3 — *"Tool-permission prompts are the HITL gate, and they're approvable remotely from a phone via `/remote-control`."*
2. `src/main/hooks.ts` — *"Slow human APPROVAL is deliberately left to Claude's native permission prompt."*
3. The **god agent's own system prompt**, `src/main/hive.ts:1333` — *"For the genuinely critical (destructive actions, spending real money, scope changes, unresolvable conflicts), ask the human directly in your own session and **let the tool-permission prompt gate the action**."*

And the default configuration is:

```
config.ts:191   /** When true, new agents are spawned with --permission-mode bypassPermissions. */
config.ts:425   autoMode: true,
```

⇒ **By default, every agent this harness spawns runs with `--permission-mode bypassPermissions`, and the harness edits your global Claude Code settings so Claude will stop asking whether you meant it.** The stated safety gate is off out of the box.

Three fair mitigations, all verified:
- It is **disclosed in the UI**: the onboarding wizard shows the toggle (defaulting to `true`), `App.tsx:296` renders "auto mode on"/"auto mode off", and the Add-Agent modal previews the literal command with the flag in it (`AddAgentModal.tsx:1009`).
- `hiddenClaude.ts` pairs its hardcoded bypass with **`--disallowedTools Edit Write NotebookEdit`** by default (`:112`) — that path is read-only, and bypass there is *necessary* (an ephemeral PTY cannot answer a prompt). I initially read this as a raw hole; it is not.
- There is a real harness-level **DENY** gate at `PreToolUse` (§2), independent of the CLI's prompt.

### And the counter-example that makes the whole ship legible

```
config.ts:194-202
/** May the orchestrator ("Michael") spin up agents on its own?
 *  Default FALSE. Spawning an agent is a SPEND decision, so it should not
 *  happen unprompted. The ability itself shipped in v0.4.4 with no gate at all,
 *  so this closes an existing default-on behaviour rather than gating a new
 *  feature: an operator who wants it must now say so.
 *  Off does not FAIL a queued spawn request, it declines to consume one. The
 *  request sits in HIVE_ROOT/spawn-requests until the toggle is turned on. */
orchestratorMaySpawn: boolean;   // DEFAULTS: false
```

He found a capability he had shipped default-on, **closed it**, wrote down that he was closing his own prior default, and made the off state **queue rather than fail**. That is first-rate safety engineering — the same class as the best consent code in the corpus.

**So the author is entirely capable of the reasoning the permission default lacks.** The difference between the two decisions is not skill. It is who pays when it goes wrong: a runaway spawn bills *him*; a bypassed permission prompt costs *a user*, later, quietly.

Also fail-closed and well built: **`src/shared/mcpCatalog.ts`** — a tiered MCP catalogue (`sequential-thinking`, `time`, `fetch`, `context7`, `filesystem` cwd-scoped, `git` cwd-scoped, `github-token`, `db` …) where `mcpDefaults` are *"Seeded from `MCP_CATALOG` so the consent defaults never drift from it (safe-readonly ON, write/secret OFF)"* (`config.ts:215`). Read-only servers on, write/secret servers off, and the defaults **derived from one source rather than restated**.

---

## 6. The memory layer, and the superlative

### What it actually is

`HIVE.md` decision 4 is the sharpest paragraph about agent memory in the corpus:

> *"**Memory: markdown first.** Per-agent `memory.md` + shared blackboard, with a SQLite FTS index when keyword recall isn't enough. A heavyweight vector layer (Letta/Mem0/Zep) is **not needed at 5–15 agents and is architecturally wrong here** (they want to own the agent runtime; our runtime is the `claude` CLI)."*

The reason to refuse a vector store is not performance — **it is that vector-store products want to own the agent runtime, and here the runtime is somebody else's CLI.** That is an independent, mechanism-named confirmation of the vault's own agent-memory position.

Then `HIVE.md:186-194` (Phase 3, marked ✅): it wraps the **MemPalace CLI** — *"not MCP, by decision"* — keeps one shared palace under `harnessHome`, points every agent's `MEMPALACE_PALACE_PATH` at it, mines each agent's `memory.md` into its own wing (mtime-gated), recalls via `mempalace search` / `wake-up`, and **detect-and-degrades to a no-op when `mempalace` isn't installed**. Default embedding model `minilm` for low-RAM Macs; `embeddinggemma` as the multilingual opt-in.

### ⭐ `src/main/reflect.ts` — the single best idea for this operator

437 lines. **MemoryReflector, *"the missing CONDENSE half of the janitor"***: the janitor flags an oversized `memory.md` but never shrinks it, so this service rewrites it into a **bounded three-region shape** — pinned durable facts (never touched) + one rolling recursive summary (≤1500 words) + the newest K verbatim sections — against a **128 KB** budget, using a cheap headless `claude -p` with `claude-haiku-4-5`.

Two comments to steal:

> *"Why in-process (Electron main), NOT launchd: launchd-spawned shells are blocked by macOS TCC from `~/Documents`; only this process has the folder grant. So the loop lives alongside `memory.start()` — never a cron."*

> *"Safety is layered so a bad LLM pass can NEVER lose data: **backup-first (lossless cold copy) → verify-don't-trust gate → atomic swap.** If any check fails the original file is left byte-for-byte untouched and the only side effect is a `condense-abort` log line."*

**A fail-closed verification gate around an LLM's own output**, because the LLM is rewriting the agent's long-term memory and a bad pass is unrecoverable. For anyone whose knowledge base is a set of markdown files that an LLM compacts, this is the most directly transferable code in the repository.

⚠️ **`HIVE.md:193` still says: "*Still open*: reflection/summarization to bound `memory.md`."** It is not open. It is 437 lines with a three-layer safety model. Same for `MEMORY_GRAPH_SPEC.md:3` — *"No component code is written yet"* — while `MemoryGraphPanel.tsx` (21.9 KB) is fully implemented [fleet].

⚠️ **Correction to my own first pass:** I reported memory as unbounded after grepping `src/main/memory.ts` (447 lines, no compaction) for `compact|summari[sz]|prune|truncat|bound`. The answer was in a sibling file. **My negative was produced by a search one file too narrow** — the third such correction on this ship (§14).

### The superlative, and what stands behind it

| Surface | Text |
|---|---|
| `README.md:75` | *"Under the hood it runs the **fastest memory layer in the world**"* |
| `RELEASE.md:558` | *"MemPalace — a markdown-first, semantic memory layer the whole office shares; **cross-session recall in ~12ms**."* |
| `docs/media/hero-poster.svg:79` | renders `→ recalled 4 memories (12ms)` |
| `landing-remotion/src/HowMemPalace.tsx:61` | the launch **video** renders `recall in 12ms` |

Now the measurements. Extent: every tracked `.ts/.tsx/.cjs/.mjs` file, grepped for `performance.now|Date.now() -|hrtime|console.time` and intersected with `mem|recall|search|palace`:

**One hit, and it is a stale-lock check** (`hive.ts:2376`). Benchmark files in 1,785 tracked files: **zero** — the nine `bench|perf` filename matches are one blog post about terminal rendering and its images.

And `HIVE.md:57`, sixteen lines above the ✅:

> *"Optional future upgrade: **MemPalace over MCP** (validate its retrieval first — **its public benchmarks are overstated per independent audit**)."*

`HIVE.md:194`: *"needs a live `mempalace` install to validate retrieval end-to-end."*

⇒ **The design document (a) dismisses the third-party tool's published benchmarks as overstated, citing an "independent audit" it never names — `"independent audit"` appears exactly once in the repository, with no link — and (b) records that this system's own retrieval has never been validated end-to-end. Both sentences are still there at HEAD. The number is in four rendered surfaces and zero measurements.**

And the same repository contains a **151-line blog post titled "Rendering Many Live Terminals: Performance"** which says *"The discipline: **measure first**"* (`:118`) and *"An accelerated renderer added only when measurement says so"* (`:130`) — and contains **not one number**: grep for `[0-9]+\s?(ms|fps|MB|%)` over the whole file returns zero matches.

---

## 7. The multi-engine seam

All **12** claimed engines are implemented — the `AgentProvider` union enumerates `claude, codex, grok, kimi, gemini, antigravity, qwen, opencode, crush, pi, copilot, cursor` plus a `custom` fallback [fleet; the adversarial verifier independently re-counted 12 and corrected the reporting agent's "10"]. Claude is the default (`inferAgentProvider` returns `'claude'` when the binary is unknown or absent).

And it is a **genuine seam, not a switch statement**: a declarative `AGENT_PROVIDER_PRESETS` table plus a type-driven dispatch on `BridgeDescriptor.kind`, with three bridge models [fleet]:

| Bridge | Engines | Mechanism |
|---|---|---|
| **native / hive-aware** | Claude | `--settings` + `--append-system-prompt` |
| **hooks** | Antigravity, Codex, pi, OpenCode, Gemini, Grok | per-engine shim translators |
| **proxy** | Qwen, Crush | a sidecar that parses traffic and synthesizes a `Stop` |

`CHANGELOG.md:779` documents the pi row: `pi` (**earendil-works**) | **hooks** (bundled extension) | `pi.on(event)` → `HIVE_SOCK`; *"extension auto-approves tools only when the floor is in auto mode."*

⭐ Honesty marker: `src/shared/agentProvider.ts:442` carries `// Live runtime (proxy parse of Crush traffic + synthesized Stop) is UNVERIFIED` — **an in-code admission that one engine's runtime path has not been validated.** Very few subjects label their own unverified surfaces.

BYOK / local LLMs for four engines (OpenCode → Ollama `http://localhost:11434/v1`; Crush and Qwen → any OpenAI-compatible endpoint; pi → a file-based `models.json`) [fleet].

⭐ Ecosystem clarification worth pinning: the integrated **OpenCode is `anomalyco/opencode` (TypeScript)** — distinct from the archived Go `opencode-ai/opencode`, **which became Crush** [fleet]. Both are wrapped here, as separate engines.

---

## 8. The enforcement census — this ship's finding

### What runs automatically

| Check | Where it lives | Runs? |
|---|---|---|
| `npm run typecheck` (strict, both tsconfigs) | `ci.yml` job `typecheck` | ✅ **every push + PR** |
| `npm run build` | `ci.yml` job `build` | ⚠️ present, **`continue-on-error: true`** — *"Build exercises the native node-pty rebuild; allowed to fail without blocking."* **It cannot fail the pipeline.** |
| PR before/after evidence | `pr-evidence.yml` | ✅ **every PR open/edit/label**, blocks merge |
| `npm run test:focused` — **73 files, 611 assertions** | `package.json:22` | ❌ **nothing** |
| `npm run check:links` — the release gate | `package.json:23` | ❌ **nothing** |
| Any linter | — | ❌ **no eslint / prettier / biome / editorconfig anywhere** |

Measured directly: in `.github/workflows/`, `npm run typecheck` × 1, `npm run build` × 3, `test:focused` × **0**, `check:links` × **0**. No husky, no lefthook, no Makefile, no active `.git/hooks`.

⭐ The typecheck gate is **excellent**: 61,873 of 62,420 TS/TSX lines (**99.1%**) fall inside the two tsconfig `include` globs; only 547 lines (10 `landing-remotion` files) sit outside. I expected to find a narrow gate and found a near-total one.

### The 611 assertions, and why their absence is not laziness

9,294 lines across 73 files. Their dependency profile: `node:assert`, `node:test`, `node:child_process`, `node:events`, `node:fs`, `node:net`, `node:os`, `node:path`, plus `typescript` (already installed by `npm ci`). `electron` in **1** file, `node-pty/lib/windowsPtyAgent.js` in **4**. **Sixty-eight of seventy-three test files need nothing but Node's standard library.**

And they are testable *because he made them testable*. Ten separate source files carry a comment explaining the refactor:

- `src/shared/engineAvailability.ts:12` — *"Pure and electron-free on purpose so it is testable from `node --test`."*
- `src/main/palaceReap.ts:23` — *"Pure and browser-global-free so the rules are unit-testable without a palace"*
- `src/main/analytics.ts:262` — *"Pure and exported so the decision can be unit-tested without PostHog."*
- `src/main/realtimeCompletionWatcher.ts:107` — *"Dependencies injected by the wiring (index.ts), so the watcher stays electron-free."*
- plus `index.ts:378`, `index.ts:4508`, `integrations.ts:9`, `releaseNotes.ts:31`, `updateState.ts:4`

**He restructured production code across ten files to make it checkable, wrote 9,294 lines of assertions, named the script `test:focused` — and never typed the three lines that would run it.** The only enforcement is `.github/PULL_REQUEST_TEMPLATE.md:62`: `- [ ] \`npm run test:focused\` passes.` A checkbox.

### `pr-evidence.yml` — the strongest gate in the repository, and it guards a screenshot

157 lines. Every PR must show an image or video under **both** a `### Before` and a `### After` heading, or the check turns red and blocks merge. What makes it exceptional is the reasoning, written in the file:

> *"It cannot stop a PR being OPENED. Nothing on GitHub can; the API has no hook that runs before creation. The strongest available enforcement is what this does instead: fail within seconds of opening, block the merge button, and say in a comment exactly what is missing."*

> *"That is only safe under one condition, which this file obeys absolutely: **NEVER check out, build, or execute the pull request's code here.** … Adding any of those to this file would hand a fork write access to the repository."*

> *"Comments are the template's own instructions to the author. Left unfilled they are invisible to a reader, so they must be invisible to this check too — otherwise the empty template would pass."*

> *"A contributor CANNOT grant themselves this — applying a label needs write access — so the rule stays mandatory for the people it is aimed at, and every waiver is on the record."*

It strips HTML comments before matching; it reads each heading's own section so two assets in one blob do not count; it detects the near-miss and says something kinder; it keeps **one** marker comment and edits it rather than spamming; `concurrency: cancel-in-progress` so a contributor fixing their description does not queue behind themselves.

**D34 test — does the gate's predicate match the history it governs?** The template's headings are `### Before` (`:34`) and `### After` (`:38`); the gate's regex is `^#{1,6}\s*before\b` / `after\b` with the `i` and `m` flags. **They match exactly.** The gate is correctly aimed at its own template — one of very few in this corpus arc that is.

The PR checklist has eight items. Exactly **one** is machine-enforced by that gate; one (`typecheck`) is enforced by CI; one (`build`) is enforced by a job that cannot fail; one (`test:focused`) has 611 assertions and no runner; one points at `ATTRIBUTION.md` — **which does exist**, at `src/renderer/src/assets/ATTRIBUTION.md`, referenced from the LICENSE itself; one points at `DESIGN.md`/`tokens.ts`, which both exist and, per the fleet, **match the CSS exactly**; and two ("this PR is one change", "I read the diff myself") are unenforceable by construction.

### ⭐⭐⭐ `tools/check-release-links.cjs` — the gate that proves the rule

104 lines, `process.exit(1)` on any problem. It was written from a **measured incident**:

> *"That is not hypothetical. The table sat pinned at 0.3.2 from v0.3.4 through v0.3.7, and mac DMG downloads fell from **118 and 76** on v0.3.2/v0.3.3 to **single digits** on every release after. **Nothing failed, nothing warned;** the release simply stopped being installable for anyone arriving through GitHub, and the page even claimed the opposite ("stays correct across versions")."*

It checks four things — artifact names against `package.json`, source-tarball tags, the website's fallback version, and `docs/llms.txt` — with two modes: offline before tagging, and `--live` after publishing, because *"which is the only moment the answer is meaningful."*

And check #4 carries this:

> *"llms.txt, which advertises the current version to crawlers and LLMs — Added in 0.4.3: **this file sat at 0.4.1 for two releases while the checker stayed green, because nothing was watching it.**"*

**He extended his own gate after his own gate went green on a fact it wasn't watching, and wrote down that it had been green.** That is precisely the discipline three of the last four corpus subjects lacked.

**And nothing runs it.** Extent: all 1,785 tracked files. `check:links` appears in exactly two places — `package.json:23` (its own definition) and `CHANGELOG.md:214` (the note about the incident). `release.yml` — the workflow that publishes the release whose links the checker exists to protect, and which publishes `RELEASE.md` verbatim as the release body — runs `npm ci`, `npm run build`, `npx electron-builder`, uploads artifacts and cuts the release with `softprops/action-gh-release@v2`. **It never calls the checker.**

> **The gate written because "nothing failed, nothing warned" lives in `package.json`, where running it requires a person to remember.**

---

## 9. Claims audit

| Claim | Measured | Verdict |
|---|---|---|
| version 0.4.5 | package.json = newest tag = CHANGELOG | ✅ exact |
| 12 engines | 12 in the type union, all implemented | ✅ exact |
| "free, open source" | MIT, no licence key, no gated code | ✅ for the app |
| macOS / Windows / Linux | electron-builder targets all three | ✅ |
| **"fastest memory layer in the world"** | zero benchmarks, zero timing code, design doc says validation is *still open* | 🔴 **unsupported** |
| **"~12ms" recall** | in `RELEASE.md`, a hero SVG and the launch video; **no measurement anywhere** | 🔴 **unsupported** |
| "measure first" (perf blog post) | 151 lines, **zero numbers** | 🔴 self-contradicting |
| `[0.1.0]` CHANGELOG section + release link | **no `v0.1.0` tag exists**; `CHANGELOG.md:1161` links `releases/tag/v0.1.0` | 🔴 dangling |
| CHANGELOG covers every tag | 35 tags, 34 headings; CHANGELOG **omits v0.1.1 and v0.1.2** (both tagged) and **documents v0.1.0** (never tagged); `0.3.4` appears twice | ⚠️ three-way drift |
| `ATTRIBUTION.md` (PR checklist) | exists, and the LICENSE points at it | ✅ |
| "working prototype" / "early prototype" | `SECURITY.md:11-12` — *"This is an early prototype."* | ✅ honest, arguably understated |

### ⭐⭐⭐ And the one that matters

**`docs/llms-full.txt:107`** — the file whose entire purpose is to tell AI assistants what this product is:

> *"MIT. Free forever; **no paid tier**. The project asks only for a GitHub star:"*

**`docs/index.html`** — the human-facing landing page:

- a `<!-- ══════════════ PRICING ══════════════ -->` section, `<section id="pricing">`, a `Pricing` nav link
- **PRO / CLOUD: "From $20/month · or $200/year · sandbox optional"**
- sandbox compute adders **+$19 / +$28 / +$44 / +$58 / +$78** per month; storage adders **+$8 / +$15 / +$38**
- **TEAMS: $39/month** per seat
- *"First 100 Founding Supporters: 50% off and 1 month free"*
- a working JavaScript **pricing calculator**: *"PRO = $20 base + optional sandbox tier + storage; TEAMS = seats × $39 network fee + cloud seats × (sandbox tier + storage). Seats clamp 1–100; cloud seats are a strict subset of the team."*

**The dates decide it:**

| When | What | Commit |
|---|---|---|
| 2026-08-06 | *"Free forever; no paid tier"* written into `docs/llms-full.txt` — **true that day** | `f378915` (release v0.3.5) |
| **2026-08-11** | the PRICING section lands in `docs/index.html` — the claim becomes **false** | `7a56e8f` / `536ef6f` *"capabilities + pricing rework"* |
| **2026-08-13** | `docs/llms-full.txt` **edited again** — *"docs(v0.4.1): carry the site's tagline into the README and metadata"* — **the sentence survives** | `057a931` |
| 2026-08-24 | still false at HEAD — **13 days** | |

The file was opened two days after the pricing page shipped, **specifically to sync it with the site**, and the one sentence the site had just contradicted was not touched.

And `tools/check-release-links.cjs` **watches `docs/llms.txt`** — because a stale *version string* in that file once cost him downloads. It watches the fact he was burned by. Nothing watches the pricing sentence, because nothing had ever burned him on one.

To be fair about the framing: the Solo/local tier genuinely is free MIT forever, and the paid tiers are cloud sandboxes and a team network fee — the *app* is not paywalled. The defect is not dishonesty about the product. It is that **the machine-readable summary of the commercial model is false, in the direction that flatters the project, in the one file written to be believed without checking.**

---

## 10. Security and privacy

**Strong:**
- Electron hardening: `nodeIntegration: false`, `contextIsolation: true`, `sandbox: true`, `shell.openExternal` restricted to `https://` and `x-apple.systempreferences://`, ~195 typed IPC channels via `contextBridge` [fleet]
- Webhook server: secret-gated with **`timingSafeEqual`** constant-time comparison, rate limits (120/min global, 60/min per endpoint), 1 MB body cap [fleet]
- **`sanitizeForVoice`** (`src/renderer/src/realtime/session.ts`): **7** prompt-injection regex patterns (including `\bnew instructions?\b` and `\byou are (?:now )?…`), whitespace collapse and a 300-char limit [fleet]
- ⭐ **The only credential-shaped strings in the entire history are the test fixtures of its own redaction filter.** Commit `a35bc40` (2026-06-27, *"feat(voice): redacted read path to hive messages"*) added `src/main/hive.ts:241` — one regex redacting `sk-`/`sk-ant-`, Slack `xox[bpaors]-`/`xapp-`, GitHub `gh[posru]_`/`github_pat_`, AWS `AKIA`, Google `AIza` — plus `test/voice-messages.test.cjs` with a fixture for each, plus a design note. `hive.ts:251` even reasons about the `aws_secret_access_key=…` shape where the *value* carries no marker. Sweep of all refs (`git log --all -S`, positive control `electron` = 108 commits): `sk-ant-` 1, `ghp_` 1, `AKIA` 1, `BEGIN RSA PRIVATE KEY` 1 — all that commit. Blob sweep for `.env`/`.pem`/`.p12`/`.key`/`AuthKey` across `git rev-list --objects --all`: **zero**.
- Supply chain: **906 lockfile entries, 906 with `integrity`, 905 resolved from `registry.npmjs.org`** and no non-npmjs URL found by grep. No vendored third-party source [fleet].
- Telemetry: `TELEMETRY.md` (4 KB) documents anonymous PostHog events with `$process_person_profile: false`; **the PostHog key is injected only in release CI** (`release.yml:56`), so a source build sends nothing. Six event types [fleet].

**Weak:**
- 🔴 `autoMode: true` + the global `~/.claude/settings.json` edit (§5)
- ⚠️ **0 of the Actions across all 6 workflows are SHA-pinned** — all semver tags [fleet]. `pr-evidence.yml` correctly scopes `permissions: pull-requests: write`; **`ci.yml` declares no `permissions:` block at all**, so it takes the default token [fleet]
- ⚠️ `postinstall` = `electron-rebuild -f && node tools/ensure-pty-perms.cjs && node tools/patch-node-pty-conpty.cjs` — a native rebuild plus two scripts that patch `node-pty` and adjust PTY permissions on install
- ⚠️ `tunnelmole` opens a **public internet tunnel** to a localhost webhook server so Slack can reach it (`src/main/slack.ts:13`, `src/main/webhook.ts:252-261`). It is secret-gated and rate-limited, but it is a public URL into a machine running autonomous agents. Note that `/remote-control` is **Claude Code's own** feature, not a tunnel this app invents
- ⚠️ No app-level command allowlist or filesystem sandbox — the agent's authority *is* the CLI's authority [fleet]
- ⚠️ **`docs/wall-data.json` publishes 43 supporters' names alongside their Razorpay `pay_*` transaction ids** in a public repository
- ⚠️ Auto-update **on by default**, 6-hour poll, feed hardcoded to this repo; macOS builds signed, **notarisation is a best-effort `afterSign` hook that does not block a release** [fleet]. The app is **not** app-sandboxed — it cannot be, since it spawns child processes

---

## 11. Licence and attribution — the strongest in the recent run

- `LICENSE`: MIT, © 2026 Chaitanya Giri, with an explicit **source-code-only** scope note and a `NOTE ON BUNDLED ART ASSETS` carve-out — and `LICENSE:35` points the reader at `src/renderer/src/assets/ATTRIBUTION.md`
- **LimeZu** *Modern Interiors* tilesets under the Complete Version licence, **purchased 2026-08-20**, licence text committed at `src/renderer/src/assets/tilesets/LIMEZUASSETS-LICENSE.txt`; credit is required and is present at `README.md:356` [fleet]
- The Office cast portraits and walking sprites are **procedurally drawn in code** (`scene/office/portraitArt.ts` from per-character recipes), not licensed art — so they are MIT like the rest [fleet]
- Tiled maps are modified derivatives of `shahar061/the-office` (**ISC**), credited [fleet]
- The vendored Claude Code skill `.claude/skills/ian-xiaohei-illustrations/` (23 files) ships its **own LICENSE and NOTICE.md**, MIT, compatible [fleet]
- Parody disclaimer at `README.md:351-352`

Compare v272, where MIT was granted sixteen lines after the same file disclaimed ownership of the content. **Here the licence boundary is drawn, the asset purchase is dated, the derivative chain is named, and the one file that reconciles it is cited from the LICENSE itself.**

---

## 12. Growth, monetisation and hygiene

**Growth:** **130 blog posts** with **13 competitor-comparison plays** (`cline-vs-`, `claude-squad-vs-`, `orca-vs-`, `qm-vs-`, `conductor-`, `crystal-` …) [fleet]. `docs/robots.txt` **explicitly welcomes** GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-Web and Google-Extended, with the comment *"AI answer engines — explicitly welcome (AEO/GEO). We want to be cited."* A 42.5 KB generated sitemap, schema.org structured data, `llms.txt` + `llms-full.txt`, and `landing-remotion/` — the marketing video is **generated programmatically with Remotion** [fleet].

⭐ **Zero project-owned affiliate or UTM links.** `grep 'aff='` across all tracked files returns nothing; the only `utm_source` values belong to third-party badges (Trendshift, Product Hunt) [fleet]. The exact inverse of v272.

**Monetisation:** `.github/FUNDING.yml` is the **unedited GitHub template** — every platform still carrying its placeholder comment — except one line: `custom: "https://razorpay.me/@munderdifflinfund"`. The Founding Supporter wall (`docs/wall.html` + `docs/wall-data.json` + `scripts/wall-sync.mjs` + `wall-sync.yml`) syncs hourly and is **rebuilt from Razorpay as the source of truth rather than appended to**, auto-committing refund and dispute removals [fleet] — a real reconciliation loop. 43 supporters; the first entry is the author himself (2026-08-14). And the $20 plaque carries **50% off PRO plus a free month for the first 100** — so the wall is a funnel into the paid tier, which is exactly what `llms-full.txt` denies exists.

**Hygiene:**
- 🔴 **`index-j0JdoH0M.js` — 12,115,724 bytes of minified JavaScript at the repository root**, added 2026-08-22 in `0c4f0bd` *"fix(focus mode): stop the close button dropping you to the sidebar, and reword the hiring setting"*. `git grep -l index-j0JdoH0M` returns **no tracked file that references it**. It is not in `.gitignore`. It is ~7% of the working tree, and every clone pays for it. An unmerged `origin/chore/remove-repo-bloat` branch exists.
- 🔴 **Zero linter configuration** for 62,420 TS/TSX lines plus 12,507 `.cjs`/`.mjs` lines. Extent: `git ls-files` matched against `eslint|prettier|biome|editorconfig|stylelint|oxlint` → **0**.
- ⚠️ 807 PNGs; blog assets duplicated between `blog/src/` and the deployed `docs/` (~20 MB redundancy) [fleet].
- ⚠️ **55 distinct paths have been deleted** across all refs (`git log --all --diff-filter=D --name-only --format='' | sort -u | grep -c .`), including rate-limiting and limit-banner UI code [fleet]. ⚠️ A verifier reported 34 using `git log --all --diff-filter=D | wc -l`, which counts log lines rather than paths; **my figure stands and the verifier's method was wrong.**
- ✅ Genuine discipline: the cost ledger is append-only, **gitignored**, and a one-time untrack pass drops it from the index on first launch so it cannot bloat the history [fleet].

---

## 13. Corpus position

### Pattern #57 — corpus-recursive, at N=3 in one dependency set

This harness wraps, by name and in code, three subjects the corpus has already shipped:

| Integrated engine | Corpus subject | Evidence here |
|---|---|---|
| **pi.dev** — `@earendil-works/pi-coding-agent` | **v228 `earendil-works/pi`** (the v36 `badlogic/pi-mono` revisit) | `CHANGELOG.md:779` — `pi` (earendil-works) |
| **OpenCode** + **Antigravity** | **v67 `opencode-antigravity-auth`** | `README.md:16,123,182` |
| **Claude Code** | the corpus's central product | the default engine throughout |

Corpus baseline greps (extent `CLAUDE.md` + `_state/` + `_patterns/`): `earendil-works` 18 · `badlogic` 14 · `pi-mono` 109 · `opencode` 247 · `antigravity` 134. **pi is now depended on by three labs and one independent harness in the corpus record.**

### Corpus-first

`munder-difflin`, `munder`, `difflin`, `chaitanyagiri`, `Munder Difflin`, `Dunder`, `udacity`, `paper company` → **zero hits, whole-vault extent including dotdirs**, with positive controls firing (`HiThink` 31, `freestylefly` 9, `OpenViking` 18). ⚠️ **Method note:** one early composite grep reported `munder => [53]`; it does **not** reproduce — the same command over the same extent returns 0, twice, and a per-directory breakdown returns 0 for all five. Recorded as an unreproducible counting anomaly, extent stated.

Also new to the corpus: `stigmergy`, `blackboard`, `Generative Agents` — all **0** before this ship.

### The mint decision — NO MINT

**Counts 46 / 12 UNCHANGED · §C-1 12 · §C-2 39 · `inflation_check` HELD.**

⭐⭐⭐ **The load-bearing observation for the next audit:** this subject is a clean, fully-independent, non-port **candidate third instance for TWO different deferred N=2 buckets simultaneously**:

1. **"Multi-Vendor Orchestration-Platform"** (Paseo v150 + ai-maestro v163) — PROMOTION-ELIGIBLE at N=3, HELD through the v167, v182, v203 and v212 audits for want of "a clean 3rd". Twelve vendors, a desktop orchestration platform, not a port. This looks like it.
2. **"Session-hosting multiplexer"** (cmux v99 + agent-of-empires v162) — also PROMOTION-ELIGIBLE at N=3. v166 established the discriminator: *observes-not-hosts is NOT the multiplexer species*. This one **hosts** — every agent is a real PTY it owns.

**One subject qualifying as the third instance of both buckets is itself evidence the two buckets may be one class.** That is an audit call, recorded and deliberately **not self-executed** — a promotion is an audit act (the v235 discipline).

Declined, with reasons:
- **A new §C-2 standalone** — the closest framing ("desktop harness wrapping N agent CLIs as a coordinated multi-agent office") is **not corpus-first**: Paseo v150, ai-maestro v163, cmux v99, agent-of-empires v162, herdr and v221 llm-space all occupy the surface. Form-factor-within-a-genre, ruled on repeatedly (v222 decisive, v227, v236).
- **The Pixi.js office floor / avatar embodiment** — presentation-not-capability (v236 dsh-TUI DECLINED; v216 the floor case), and the embodied-agent domain was declined at v210 AIRI as domain-not-capability.
- **The interactive-PTY-not-`-p` billing choice** — a technique, not a capability class (v211 PixelRAG). It is also the *inverse* of the v207/v208/v231/v232 subscription-re-exposure class, and worth recording as that boundary's clean counter-example.
- **§28** invoked only as a supporting ground, per §44 clause 5.

Recorded instance-strengthening (recorded, **not** self-incremented — the v205/v235 discipline): **#18 sub-archetype B1-MCP** (a tiered, consent-defaulted MCP catalogue) · **#66** supply-chain awareness (a clean single-registry lockfile with a `postinstall`) · **#88 88c** anti-slop machinery-with-enforcement is **declined** — `DESIGN.md` + `tokens.ts` exist and match the CSS, but nothing gates them.

Two DEFERRED watch axes registered: *"a harness that drives a coding-agent CLI through an interactive PTY specifically to bill against the interactive plan quota rather than the SDK/API credit pool"* (N=1) · *"an `llms.txt`/`llms-full.txt` whose commercial claim is falsified by the same repository's own landing page"* (N=1).

---

## 14. Method notes

**Fleet:** 15 dimensions, **14 returned, 1 died** (`tests-and-gates` — StructuredOutput retry cap; I had already covered it by hand, exhaustively). 29 agents, 3.75 M subagent tokens, 1,347 tool uses, 9.6 minutes. Adversarial verify: **78 CONFIRMED · 26 CORRECTED · 5 REFUTED**.

**Fleet errors worth recording:**
1. ⚠️ **The 50-commit artifact recurred** — one agent wrote *"all 50 commits in the clone are authored by humans"* against a truth of **986**, **despite the ground-truth block stating 986 explicitly.** A supplied ground truth does not immunise an agent against its own truncated command output. (D39 family; the fourth data point.)
2. ⚠️ **"Only 1 Co-Authored-By trailer found"** — refuted. My own census: **616 trailer lines / 612 commits**, of which **599 credit a named Claude model**. The agent's *own finding text* noted a contradicting commit and still reported 1.
3. ⚠️ **"No evidence that agents wrote production TypeScript/React code"** — refuted by those 599 trailers.
4. Line numbers wrong by 2–250 in seven places (LimeZu credit at `:356` not `:614`; the parody disclaimer at `:351` not `:616` in a 360-line file; `pr-evidence.yml` 157 lines not 268). **v271's D51 at another data point: the fact right, the citation wrong.**
5. A verifier "corrected" 55 deleted paths to 34 using a command that counts log lines, not paths. **The correction was wrong.**

**My own corrections, all pre-publication:**
1. 🔴 **"memory.md is unbounded"** — wrong. I grepped `src/main/memory.ts` alone; the bounding is 437 lines in `src/main/reflect.ts` with a three-layer safety model. **A negative from a one-file search.**
2. 🔴 **"no paid tier"** — I grepped `pro tier|paid plan|premium|paywall` and concluded there was none. The landing page has a pricing calculator. **My negative was produced by the wrong search terms over too narrow an extent** — the fleet caught what I missed, and it became the ship's best claim finding.
3. **`hiddenClaude.ts`'s hardcoded `bypassPermissions`** — I nearly reported it as a hole; it is paired with `--disallowedTools Edit Write NotebookEdit` and is correct.
4. **`ATTRIBUTION.md`** — I nearly reported a dangling checklist reference; it exists and the LICENSE cites it.
5. **The typecheck gate's scope** — I expected a narrow gate and measured 99.1%.
6. **`/remote-control`** — Claude Code's own feature, not a tunnel this app invents.

All three of my substantive errors were **negatives produced by a search narrower than the claim** — §43.1, verbatim, three times in one ship. The two that mattered were caught by the fleet and by re-measurement, not by re-reading.

⚠️ Sandbox: `python3` unavailable; `node -e` blocked (script files work).
