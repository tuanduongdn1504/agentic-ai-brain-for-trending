# (C) dsh-anchored-standard — Deep Dive

**Wiki v238 · built 2026-08-18 · operator-requested**
**Subject:** `xiaobright/dsh-anchored-standard`
**Provenance:** rendered repo page + raw README.md + git tree API + 7 source files read + 5 issues + FAREWELL/ACKNOWLEDGEMENTS/NOTICE/LICENSE/package.json/HANDOFF-2 + landscape research. **NOT source-cloned** (§37 fence).
**§37.4 note:** this environment mocks the GitHub API for stars/forks/dates → all counts below are **page-stated, NOT API-verified** → **no Pattern #52 claim.**

---

## 1. What it actually is

A **DeepSeek Harness (DSH) *agent preset*** — not a plugin that adds a feature, not an app. It is a composition of Cordis rows (`agent.cordis.yml`) that you copy into `~/.dsh/.agent-presets/` and select when creating a session.

Repo tagline: *"Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)."*

The thesis, in the README's own words:

> DeepSeek V4 Pro conditions strongly on the API-visible tool catalog. In the Project2 evaluation, Standard and PTC produced scores of 91 and 92, while the official Minimal preset produced 99 and 96. Permanently staying on Minimal, however, gives up the Standard preset's broader tool set.

So: DeepSeek ships a *Minimal* preset (2 tools) that scores well and a *Standard* preset (25 tools) that scores worse. Anchored Standard tries to get both — **look like Minimal on request #1, become Standard from request #2.**

**The core mechanism (source-verified):**

```
user's first message
        │
        ▼
┌ request #1 — bootstrap phase ─────────────────────────────┐
│ tools   : bash + str_replace_editor  (Minimal's REAL pair) │
│ context : every automatic injection BLANKED                │
│ budget  : adapter default (bootstrapMaxTokens optional)     │
└────────────────────────────────────────────────────────────┘
        │ first durable tool/call OR assistant/message
        ▼ PROMOTION — derived from durable events → resume-safe
┌ request #2+ — resident phase ─────────────────────────────┐
│ tools   : bootstrap pair + discovery tools + unlocked      │
│ context : standard injections restored                      │
└────────────────────────────────────────────────────────────┘
```

Crucially it does **not** dump the full Standard catalog at promotion — the README reports that doing so *"pulled the trajectory back to standard-like behavior (the post-promotion regression)"*, so heavier tools stay one `dev_tool_search` call away.

**Seven modes ship, each a self-contained directory:**

| Mode | Request #1 | Anchor mechanism | Extra cost |
|---|---|---|---|
| Anchored Standard (`preset/`) | 2 tools | Minimal tool schema | none |
| Zero-Anchored (`zero-anchored-standard/`) | 0 tools | one fixed anchor turn | +1 model call |
| Whoami (`whoami-standard/`) | 0 tools | a 「你是谁」 self-intro turn | +1 model call |
| Prefab (`prefab/`) | seeded history | a bundled successful trajectory | none to instantiate |
| Eternal Minimal (`eternal-minimal/`) | 2 tools, forever | catalog never grows; heavy tools via a `dshx` bash gateway | none |
| Wire Think-Execute (`wire-think-standard/`) | tools present, `tool_choice: none` | sibling provider route per think step | +1 call/turn + cache churn |
| Combo Anchored (`combo-anchored/`) | 0 tools every turn | think-split + depth gate + deliberation drip as 3 independent rows | +1 call/turn |

**Facts:** MIT (`Copyright (c) 2026 xiaobright` + `Portions Copyright (c) 2026 DeepSeek`). **Zero npm dependencies. No lifecycle scripts. No network calls. No telemetry.** Node ≥22.19.0. v0.1.0. 19 test files, `node --test`, CI on ubuntu/Node 24 with `permissions: contents: read`. ~3,500★ / 106 forks / 56 commits (page-stated). Targets DSH **`0.1.0-rc.5`** at commit `47f9438`, Node 24 on Windows.

**Author:** `xiaobright` — a **bare handle**: 6 public repos, 32 followers, 0 following, **no bio, no company, no location, no website**. Portfolio is telling: `modeltest` (*"Personal LLM engineering-maintenance evaluation harness (V4.1b, frozen). Not a public benchmark."*), `modeltest-v5` (*"V5 failed experiments archive + reusable HIL tooling (stalled)."*), `remote-mcp`, `vision-mcp-pool`, plus a fork of the research repo. A measurement-first portfolio, not a product portfolio.

---

## 2. ⭐ THE FINDING — the project died yesterday, and its exit note is the most valuable thing in it

`FAREWELL.md` is dated **2026-08-17** — the day before this wiki. Development has **stopped**; the repo is maintenance-only. Why:

> 很朴素：能力和财力都有限。API 涨价之后，一轮完整评测的成本已经超过了我的承受范围，而继续在没有验证能力的情况下堆功能，是对用户不负责任。
>
> *"Simply: both capability and finances are limited. After the API price increase, the cost of one complete evaluation round has exceeded what I can bear, and continuing to pile on features without verification capability is irresponsible to users."*

`HANDOFF-2.md` puts a number on it: a full Project2 evaluation round went from **~¥2 to ~¥12** (roughly **$0.28 → $1.70**). The absolute figure is trivial — which is exactly what makes it striking. The project needed *many* rounds (multi-trial roll and probe experiments), so a ~6× multiplier on a small number killed it.

**The generalisable lesson: for inference-time research the binding constraint is the cost of EVALUATION, not the cost of development.** Writing the plugin was free. Knowing whether it worked was not.

Two more passages worth reading in full, because they are unusually honest for a 3,500-star repo:

> 项目现在有三千多个 star，但我清楚，这个数字并不等同于我个人的技术能力。
> *"The project now has over three thousand stars, but I'm clear that this number doesn't equal my personal technical ability."*

> 我们这些天的很多工作，说得好听是"推理时控制"，说得直白是替官方补位——把模型在评测条件下被训练出的好行为，在用户真实使用的环境里重新捞出来。
> *"Much of our recent work can be called 'inference-time control', or plainly: filling gaps for the official team — retrieving the good behavior the model was trained to show under evaluation conditions, back into the user's real-world environment."*

That second quote is the project's real thesis, and it is sharper than the README's. It also names its own obsolescence condition: the author hopes DeepSeek will *"absorb a more diverse range of harness environments during training"*, citing **Kimi K3's technical report** as proof the path works, so that *"our kind of patch engineering [becomes] unnecessary."*

---

## 3. The mechanism, source-verified

I read the plugin source. It does what it says.

### `shared/context-gate.mjs` — the injection gate

Two hooks, mounted so the gate registers before every injecting plugin:

- `ctx.on('system-prompt/assemble', …)` — **Path A**, blanks runtime context: `return { ...assembled, contexts: [] }`. The header comment explains why this is done wholesale rather than by source name: *"That covers the WHOLE `SystemPrompt.context()` family — the sandbox and approval policy snapshots and any third-party context provider — without enumerating them."*
- `ctx.on('agent/pre-step', …, { prepend: true })` — **Path B**, filters the message waterfall down to the *claimed* batch plus an allowlist. Default `allowKinds = ['skill-invocation']`, on the reasoning that *"a user-initiated skill gesture is not an automatic injection."* Everything else — skill catalog, AGENTS.md/CLAUDE.md digest, time/tmux context, hooks, unknown third-party injections — is stripped **by default, regardless of source identity.**

Promotion is read off durable events, so resume and reload preserve phase:

```js
const PROMOTE_EVENTS = {
  'tool-call':        ['tool/call'],
  'assistant-message':['assistant/message'],
  either:             ['tool/call', 'assistant/message'],
}
```

A `compaction/end` boundary **demotes** again — the first post-compaction request is treated as a "second first request." Both filters **fail open**: the comments are explicit that *"a gate bug must never eat the user's context"* / *"must never break assembly."*

**Zero imports beyond `./compaction-epoch.mjs`. No URL literals. No network. No telemetry.** (`anchor-turn.mjs` has *no* imports at all — it uses native `crypto.randomUUID()`.)

### `shared/tool-bootstrap.mjs` — the catalog restriction

It **filters**, it does not replace: `tools: assembled.tools.filter((tool) => keep.has(tool.name))`. The resident set in code:

```js
const keep = new Set([...bootstrapTools, ...RESIDENT_DISCOVERY_TOOLS, ...unlockedFor(context.agent?.session)])
// bootstrapTools           = ['bash', 'str_replace_editor']
// RESIDENT_DISCOVERY_TOOLS = ['dev_tool_search', 'skill_search', 'skill_load']
// unlockedFor()            = tools the model unlocked, parsed from durable tool/call events
```

Two details worth stealing:

- **`bootstrapMaxTokens` is explicitly stripped at promotion**, because *"the next request's seed proposal carries the previous header's maxTokens forward, so the injected cap must be stripped explicitly — otherwise it would persist for the whole session."*
- **A missing bootstrap tool degrades to the full catalog with a one-time warning**, so *"a composition drift can never brick every request of a session"* — while an invalid `promoteOn` value throws **at mount**. Fail-soft at runtime, fail-fast at config time. That is the right split.

### `preset/agent.cordis.yml` — row order and a nice conflict resolution

Rows 1–2 are confirmed `context-gate` then `tool-bootstrap`. Notably, the Standard sandboxed bash row is **disabled on every platform**, with the reason in a comment:

> Disabled on EVERY platform, not just Windows: `dsh-tool-bash-persistent` below registers the same `bash` tool name into this same preset layer, and the tools registry rejects duplicates within one layer.

Byte-identity of the tool *name* matters here, because the whole mechanism keys on schema identity. Both `tool-subagent-codex` and `tool-subagent-claude-code` are also `disabled: true`.

### `shared/toolchoice-adapter.mjs` — the most impressive single file

`tool_choice` is outside the harness's `GenerateOptions` vocabulary, and the official DeepSeek adapter can't be wrapped (its wire body is built inside a private generator). So this file **vendors a minimal, protocol-faithful subset of DeepSeek's own adapter pipeline** — its own SSE parser, its own request serializer, its own chunk translation — and registers it as a *sibling provider route*:

```js
export const DEFAULT_PROVIDER = 'deepseek-wire-think'
const toolChoice = tools !== undefined ? (config?.toolChoice ?? 'none') : undefined
```

Connection facts resolve row config → the `llm-deepseek` settings section → `DEEPSEEK_BASE_URL` / `DEEPSEEK_API_KEY`, exactly like the official row. Only URL literal: `https://api.deepseek.com`, called as `${baseURL}/chat/completions`. Registration failure (e.g. `DUPLICATE_ADAPTER`) is **caught and warned**, degrading to the zero-tool think condition rather than bricking. The `logprobs` opt-in requests `logprobs: true, top_logprobs: 1` and can only **log a per-request mean** — the harness StreamChunk vocabulary has no surface for logprob data, which the file says plainly.

`NOTICE` discloses the vendoring and attributes it to DeepSeek's MIT.

### `eternal-minimal/eternal-minimal.mjs` — the cleverest hack

⚠️ **Doc-stated, not fully source-verified** (my fetch returned a summary for this file, not raw code — flagged honestly).

The model's visible catalog stays *exactly* the Minimal pair forever, while the whole Standard toolset runs for real behind a bash gateway:

```
dshx list
dshx web_search '{"query": "..."}'
```

The documented twist: a `tools/pre-execute` listener intercepts `dshx …`, dispatches through the real registry, and returns the rendered output — but the **deny channel is the only sanctioned pre-dispatch way to substitute a result**, so genuine tool output arrives *flagged as an error*, and every payload has to state plainly that the tool executed and its output follows, so the model reads it as output. Working within a host's real constraints rather than pretending they aren't there.

---

## 4. ⭐⭐ The evidence — and the part the tagline doesn't tell you

This is the most important section. Read it before you believe anything about this preset.

### The three levers (issue #11, a 45-session controlled trial by @Rtyyy233)

The README's summary:

1. **Tool schema** — decisive at the adapter-default 256000 maxTokens. *"The real Minimal pair anchored 5/5; every standard-family schema fell standard-like 11/11."*
2. **Output budget** — a 1024 first-request cap also anchored (26/32), independent of tool descriptions. Left **unset** by default.
3. **Injected reminders** — with the skill catalog present, *"the anchor did not reproduce at all (0/9)."*

### Issue #6 — the finding that generalises best

@slicenferqin isolated why replication kept failing on other people's machines: `dsh-tool-skill` injects roughly **9 KB** of skill-directory reminder as a user message during `pre-step`, **only when local skills exist**.

- with the skill block: **0/9** anchored
- without it: **~81%**

> This explains why the author's machine [without local skills] could replicate, but machines with installed lark-*/story-* skills could never replicate.

**Nine kilobytes of auto-injected catalog was enough to destroy the effect completely.** Hold that thought for §7.

### Issue #60 — a third party caught the author's own doc drift

@MolecularFullerene showed the headline scores had been **retroactively re-attributed**. The runs that produced 98/99 used a first-request `pwsh` + `read` surface promoting to the *full 25-tool* catalog; the exact Minimal pair (`bash` + `str_replace_editor`) arrived later. Quoting the issue:

> the historical result description changed from the neutral "two bootstrap tools" to "the two-tool Minimal bootstrap", while the existing `98/99` table remained unchanged. This retroactively attached the later schema identity to earlier runs.

The author accepted it, and the README now carries the caveat — including that the bundled generic prefab *"was not re-benchmarked before the API price change, so those scores must not be attributed to the generic template."*

### The two independent replications — and they disagree with each other

| | #65 (@TipsyDrifter) | #51 (@JimMilk) |
|---|---|---|
| Design | 3×3 randomised block, n=3/preset | 11 rounds × 3 OSes (macOS / Win11 ARM64 / Linux) |
| Trajectory anchoring | **9/9 separated perfectly by preset** — *"real and very robust"* | *"the author's 98/99 trajectory is not reproducible on current weights"* |
| Ability | 90.0 std / **93.3 anchored** / 90.7 whale | **85–90 across all environments; 98/99 NOT reproduced** |
| Effect size | **+3.3, 95% CI [−2.6, +9.3]**, ANOVA F(2,6)=1.05, **not significant** | trajectory showed **no correlation with scores** |
| Conclusion | *"did not reproduce at n=3"*, unresolved not refuted | score losses trace to a **model-layer defect** (F3-05 session_id authorization), *"unrelated to OS/preset/trajectory"* |

**What is established:** the preset reliably changes the *style* of the model's first reasoning chain ("We need…" vs "Let me…"). #65 nails this 9/9.

**What is not established:** that this makes the model *better*. The one measured advantage has a confidence interval that crosses zero, and the other replication found no correlation between trajectory and score at all — and disputes even the style effect on current weights.

The README, to its credit, says a version of this itself: *"Treat the scores above as our original observations, not a settled effect size."* But the repo **tagline still advertises "Project2 98/99"**, which is the number nobody has reproduced.

---

## 5. Where it sits in the corpus

**Fourth consecutive ship in one dependency graph** — v235 `deepseek-harness` (the host) → v236 `dsh-TUI` (a plugin replacing the UI seam) → v237 `DSH-better-sidebar` (a plugin adding a panel *and* publishing its own extension API) → **v238 an agent PRESET**. A third structural kind of DSH extension: not a plugin adding capability, but a *composition of the host's own rows* that changes what the model sees.

One detail worth recording: v238 pins **`0.1.0-rc.5`** — v235's exact release candidate — while v236 and v237 both carried `^0.1.0-rc.6`. So this is the one member of the chain built against the version the corpus actually documented.

**⭐ The sharpest cross-reference: openinterpreter v223.** That subject's §C standalone is *"Harness-Emulation Coding Agent"*, built on the premise that a model's agentic performance depends on the harness it was RL-tuned against — so ship one binary that *becomes* any harness and match it to the model. v238 arrives at the identical premise from the opposite end: stay inside one harness, find the *specific lever* that reproduces the trained-for condition, and measure it.

And both land on **Kimi K3**: v223 reimplemented the Kimi-Code harness Rust-native for maximum Kimi K3 performance; v238's FAREWELL cites Kimi K3's technical report as evidence that training across diverse harnesses is the real fix. Neither cites the other — this is independent convergence, not lineage (so **not** Pattern #57).

**Nearest §C neighbours, all checked and all distinct:**

- **v140 `google_workspace_mcp`** — *"Graduated / Least-Privilege Tool-Exposure for a Large-Surface MCP Server."* The closest row by shape, and **not** its N=2: that row is scoped by its own text to *"a 2nd MCP server with graduated/tiered tool exposure"* (v238 is a harness preset, not an MCP server), and its rationale is explicitly API-quota and permission-scope — a *deployment-time static tier flag*. v238 is a *per-session runtime phase machine keyed on durable events*, for reasoning quality. Same silhouette, different animal.
- **v144 `headroom`** — a pre-LLM interceptor, but it *compresses* for token economy; that row already distinguishes itself from v140's tool-registration gating.
- **v178 `SkillOpt`** — optimises a skill *document* in text space via a validation gate. Different object entirely.
- **v168 `ponytail`** — a hand-authored behaviour ruleset *injected* as prose, plus a benchmark. v238 *removes* rather than injects, and its lever is the API tool schema.
- **v186 `DeepSpec`** — DeepSeek's speculative decoding: the weights/decoding layer, not the request surface.

---

## 6. ⚠️ Novelty: what is actually new here (not much) and what is (the framing)

I looked hard for prior art. The core mechanisms are **well established**:

- **Anthropic ships this mechanism as a first-party platform feature.** The **Tool Search Tool** with `defer_loading: true` **strips deferred tools from the initial system prompt entirely** and loads them only when searched for — documented at 77K → 8.7K tokens on the first request. That is the same bootstrap → discovery-tool → promote shape. **Stated rationale: token economy.**
- **arXiv:2604.21816** *"Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading…"* (Apr 2026) — selective tool activation + deferred schema loading, and it explicitly ties minimising tool visibility to *preserved reasoning quality* at long horizons.
- **arXiv:2605.24660** *"How Many Tools Should an LLM Agent See?"* (May 2026, Meta) — tool-selection accuracy varies with catalog size.
- **arXiv:2512.15274** *"Well Begun, Half Done"* and **arXiv:2506.22058** *"Lost at the Beginning of Reasoning"* — the first reasoning step disproportionately determines the outcome; flawed openings cost ~40% accuracy.
- Least-privilege tool restriction is a whole literature (MiniScope, arXiv:2606.20023, arXiv:2606.13884) — framed as **security**.

**So the finding is not new and the mechanism is not new.** What appears genuinely unrepresented is the **rationale plus the measurement**: every documented staged-tool system justifies itself with token economy or least privilege. This project justifies itself with *reasoning-trajectory selection* — treating the tool schema as a knob on the model's cognitive style rather than on its context budget — and then measures the dose-response, publishes the ablations, and lets third parties fail to replicate it in public.

That is a real contribution. It is a contribution to *understanding*, not a new capability.

---

## 7. ⭐⭐⭐ Why this matters for your own setup

Here is the part that pays for the read.

Your Claude Code session carries a **~54K-token tool catalog** across the MCP servers you have connected. The vault has been treating that purely as a *context-budget* problem — `CLAUDE.md` literally says *"trim connected MCP servers to lower the ~54K floor"*, and this session proved the point again when 18 workflow subagents died at ~207K.

This subject's evidence says the tool surface is plausibly **also a reasoning variable**. Issue #6 measured that **~9 KB** of auto-injected skill catalog was enough to take a reproducible behavioural effect from ~81% to **0/9**. Your injection is roughly six times larger than the one that did that.

I want to be careful here, because the evidence bar matters: what is *established* is that the surface changes the model's reasoning **style**; that it changes reasoning **quality** is exactly the claim two replications failed to confirm. And this was measured on DeepSeek V4 Pro, not on Claude. So this is a **hypothesis worth testing on your own setup**, not a finding to act on blindly.

But the test is nearly free, because **the lever already exists first-party**: Anthropic's Tool Search Tool with `defer_loading: true` does the same thing this preset does, for the same first request, with vendor support and documentation. You do not need to install a dead preset for a rival harness to try the idea.

**The other durable payload is `HANDOFF-2.md`**, which is a genuinely good engineering-pitfalls document:

- *Measure the artifact the downstream process consumes, not the pre-cleaned one.* Their quality gate examined pre-cleansing session data while verification checked post-cleansing — so marginal templates passed the gate and failed verification.
- *Small-n honesty as a habit* — results at n=1–4 are labelled 探索性，n 小 ("exploratory, small n"), and every environment is tagged with four invariants (DSH version, OS, API source, model version).
- *Design probes that isolate one variable at one request per trial.* `probe-clone-runner.mjs` creates a session, seeds, sends one follow-up, cancels on the first assistant message, classifies, exits.
- *Beware checkpoint drift.* Four roll attempts scored 1/4 on 2026-08-17 versus 1/1 the day before, hypothesised as a silent model-alias switch. Validate with n≥4 before committing resources.
- *Any injection of machine-dependent discovery results must be re-rendered at deployment, not frozen at capture* — their prefab templates were baking the roll machine's skill registry into other people's sessions until they added a live re-render.

---

## 8. Risk assessment

**Unusually clean for what it is:** zero npm dependencies, no `postinstall`/`prepare`, no network calls, no telemetry, CI with `contents: read` only, atomic writes confined to `$DSH_HOME`, and an installing-agent contract (`AGENT_INSTALL.md`) that is tightly bounded — one command, exit 0, an `INSTALL READY` marker, no config edits, no credentials.

**Real risks:**

1. **The prefab seeds someone else's recorded reasoning into your session.** 80 KB (generic) and 212 KB (Project2) of real model trajectory, replayed as history. `skill_search` results are re-rendered live against your machine, but **other tool results are replayed verbatim** — stale file listings, stale web results, and the original author's intermediate reasoning, all steering your session. This is a self-inflicted context-injection surface, and the README does warn that both templates *"contain real model reasoning."*
2. **`custom-bash.mjs` runs without OS sandbox confinement on Windows** — its own tool description says so: *"runs without OS sandbox confinement on Windows (no landlock); treat output as untrusted."*
3. **The README's own trust statement:** *"The preset has the same trust level as shell access. Review its files before installation."* Correct, and worth repeating.
4. **Dead project, pre-1.0, pinned to a release candidate.** v0.1.0, maintenance-only from 2026-08-17, targeting DSH `0.1.0-rc.5` while the ecosystem has moved to rc.6. DSH itself *"explicitly permits breaking changes."*
5. **Prefix-cache churn** in the exotic modes — the wire-think mode switches the tools block twice per turn, breaking DeepSeek prefix-cache reuse each time; the README discloses this as a cost.

**Doc defects I found by hand:**

- **The README links `HANDOFF.md`, which does not exist.** The git tree contains only `HANDOFF-2.md`; the raw URL 404s. Confirmed twice, independently.
- **Directory drift** (the recurring lesson: the repo is authoritative). `deepseekdocs.com/en/ecosystem` lists **3,382★ and no license** against the repo's MIT; `dshplugin.dev` does not surface the plugin at all despite its star count; `dshplugin.store` is accurate but drops the "(Project2 98/99)" clause. Ecosystem size claims also diverge wildly — 1,253 (dshplugin.dev) vs 1,345 (deepseekdocs) vs a `dsh-plugin` GitHub topic reporting **7,164** repos, which I treat as an unreliable upper bound since the topic is self-applied. The divergence itself is the finding; v236 recorded ~1,120 plugins one day earlier.

---

## 9. The ecosystem context: this class is already crowded

The subject's own README points at two community projects users report performing better in some scenarios:

- **`yjh051108/dsh-routing-suite`** (~5.7k★, MIT) — a runtime injector plus task-aware thinking-mode routing. Its sibling `dsh-router-standard` describes *"three measured behavior bands (spec/mixed/react) with phase-transition evidence, persona + **first-turn tool injection**, agent-visible tuning"* and ships a dual-attractor policy paper. **Same lever, different author.**
- **`Tiger3807861189/J-Space-Cognition-Suite-V3.6`** — a model-agnostic inference-time cognitive control layer packaged as a Skill, with effects reported across DeepSeek, Qwen, GLM, GPT and Claude families.

And the subject's own issue **#53** is titled *"Convergent two-phase design from an independent lineage."*

So: at least three independent authors in this ecosystem are doing inference-time reasoning/trajectory control, and one of them arrived at the same two-phase design independently. The class is real and recurring — it is simply **not anchored on this repo.**

Worth noting who did the work here, too. `ACKNOWLEDGEMENTS.md` credits a genuine collective by handle: Greenhand-monster (designed and implemented Eternal Minimal, Wire Think-Execute, Combo Anchored), wushi2333 and tianmingwan (maintenance, Whoami), 0liveiraaa (the research repo), noone89A (attributing the "personality split" to the MoE routing layer), plus Rtyyy233, MolecularFullerene, TipsyDrifter, JimMilk and others on experiments and replication. The FAREWELL is explicit that *"the research and plugins from several community heavyweights are clearly beyond my own capability range."* Two of the seven shipped modes were designed by someone else.

---

## 10. Verdict

**GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · **(b) MODERATE keys the tier ⚠️STRONG-reviewable** · (c) STRONG · (d) STRONG. Cleanly goal-aligned via §31; §40 not needed.

**NO MINT.** Full reasoning in the Verdict doc, but in one line: the mechanism is a **shipped Anthropic platform feature** and the finding is **published literature**, so what is distinctive here is a *rationale and a measurement*, not a capability — and §C vocabulary is capability-shaped. Recorded as a corpus-knowledge data-point plus a DEFERRED watch axis, with the N=1 mint written down as the reviewable alternative.

**PILOT: ⚠️ read and borrow — do not install.** There is nothing here for a Claude user to install: it is a dead v0.1.0 preset for a rival harness, pinned to an old release candidate, whose benefit two independent replications failed to confirm. What *is* worth taking is the hypothesis (your tool surface may be a reasoning variable, not just a token cost), the first-party way to test it (`defer_loading`), and `HANDOFF-2.md`'s evaluation discipline.

⭐ **A1 → B5 → C11.** Read §4 and §7. Write a tool-surface hygiene rule into `CLAUDE.md`. Then actually trial `defer_loading` on your own Claude Code and measure it against the ccusage/OTel layer.
