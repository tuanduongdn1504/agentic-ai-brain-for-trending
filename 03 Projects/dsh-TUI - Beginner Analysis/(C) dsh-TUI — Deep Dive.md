# (C) dsh-TUI — Deep Dive

**Subject:** `ccch1mneyyy/dsh-TUI` · npm `@deepseek-harness-tui/dsh-tui` **v0.8.0** · MIT
**Wiki:** v236 · built 2026-08-17 · operator-requested
**One line:** A Claude-Code-style terminal UI, mounted as a **Cordis plugin inside DeepSeek Harness** (`dsh` = corpus subject **v235**), that replaces the host's UI seam and nothing else.

---

## 1. What it actually is

The repo description (verbatim, bilingual):

> 「DSH 官方公众号收录的 TUI 补位插件：Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚/上下文进度+TPS。npm 一键装。」
> *"DSH official WeChat featured TUI plugin — Claude Code style: whale bar, live status, streaming thoughts, double-Esc rollback, context bar + TPS. npm one-click."*

`package.json` is blunter, and more useful:

> `"Claude Code style interactive TUI front door for DeepSeek Harness agents, built on the ported Ink core."`

Install:

```bash
npm install -g @deepseek-ai/dsh @deepseek-harness-tui/dsh-tui
dsh-tui
```

Note what that install line *is*: the **host runtime plus the plugin**. dsh-TUI is not a program. It is a **front door bolted onto someone else's agent**.

Repo topics, which do the identification for us: `claude-code`, `coding-agent`, `deepseek`, **`deepseek-harness`**, **`dsh-plugin`**, `ink`, `react`, `terminal`, `tui`.

**Author:** **"Chimney"** (`ccch1mneyyy`) — bio 「试图用ai做点东西~」 (*"trying to make something with AI"*). No disclosed name, employer, location, or website; 19 followers, 8 public repos. A pseudonymous individual. **Not Anthropic, and not DeepSeek** — this is a third-party plugin, not a first-party component.

**Scale (page-stated, §37.4):** ~1.7k★ / 74 forks. Not a velocity claim.

---

## 2. The corpus finding: this runs *inside* last ship's subject

The vault shipped **v235 `deepseek-ai/deepseek-harness`** four days before this (2026-08-13, `0.1.0-rc.5`). Its entire thesis was *"Everything is a Plugin"* — models, tools, skills, sessions, sandboxes, storage, the main agent loop, scheduling, **and the UI** are all hot-swappable plugins on **Cordis** (shigma's kernel, whose defining capability is *disposability*: reversible side effects, `ready`/`dispose`/`fork`).

v236 is a stranger actually doing it, to the UI seam, four days later.

The proof is mechanical, not rhetorical. `package.json` declares **21 `peerDependencies`, every one of them `@deepseek-ai/*` pinned to `^0.1.0-rc.6`**:

```
@deepseek-ai/cordis, dsh-agent, dsh-agent-instructions, dsh-agent-presets,
dsh-atomic-write, dsh-commands, dsh-cordis-host-runner, dsh-invariants,
dsh-llm, dsh-persona, dsh-session, dsh-skill, dsh-storage,
dsh-storage-domain, dsh-storage-json, dsh-system-prompt, dsh-terminal,
dsh-terminal-bash, dsh-tool-ask-user, dsh-tool-bash-persistent,
dsh-tool-cordis, dsh-user-approval, dsh-user-questions, dsh-workspace
+ @deepseek-ai/schemastery ^3.18.1
```

Two things fall out of that list:

1. **It is a declared, npm-resolvable dependence on a corpus subject's own workspace packages** — including `@deepseek-ai/cordis`, the rescoped kernel v235 documented (with third-party-notice and license-verification CI gates). This is the strongest, most checkable form of corpus recursion available: not a README citation, a lockfile edge.
2. **`^0.1.0-rc.6` is one prerelease ahead of the `0.1.0-rc.5` v235 recorded.** The host moved a version in the days between the two ships. That is the promised breaking-change treadmill, visible in the peer range.

### What it replaces, and what it pointedly does not

From `docs/architecture.md` and the plugin directory listing, the division of labour is explicit:

- It **mounts via Cordis** as a lightweight entry point that defers loading the runtime: `src/index.ts` declares the plugin name, **injection points**, and a config schema; `src/plugin.ts` does TTY checks, questionnaire/skills registration, Agent creation/recovery, React mounting, and **unified cleanup** (Cordis `dispose` — v235's headline capability, exercised).
- It **continues to use** "the official DSH agent, model, tool, session, and persistence services."
- It **replaces no core service.** The house rule, verbatim: 「不要在组件中复制 DSH Agent、session 或 tool 服务」 — *do not replicate DSH Agent, session, or tool services in components.*
- **"Zero core changes, pure plugin mounting. Install to enable; uninstall leaves no core patches."**

That last claim is the one most plugins make and few can demonstrate. This one puts it in CI — see §4.

### The finding underneath the finding: the append-only log is load-bearing

v235's wiki flagged **append-only session logs** (*anything visible to the model is permanently recorded*) as an architectural guarantee, and noted it mapped almost verbatim onto the vault's RATIFIED candidate-LLM legibility ADR.

dsh-TUI is the proof that the guarantee is real and useful, because the UI is built on top of it:

> 「Channel 只保留适合当前 TUI 的投影」 — *the Channel keeps only a projection suited to the current TUI* — while the DSH `session/event` log is responsible for history replay, streaming events, association anchors, **rewind boundaries**, and reconstruction after resume or fork.

So: an independent front end reconstructs the whole conversation, and implements time-travel (double-Esc rewind) and forking, **purely by replaying the host's event log**, holding nothing authoritative of its own. That is the cleanest external validation of an append-only-log design the corpus has seen — and it is the one architectural idea here worth stealing outright (§7).

---

## 3. The other finding: a rival ecosystem itemised Claude Code's UX

dsh-TUI is a **feature-by-feature reconstruction of Claude Code's terminal experience**, on a competitor's runtime. The inventory, as shipped:

| Claude Code behaviour | dsh-TUI |
|---|---|
| Streaming reasoning, expandable | streaming thought expansion |
| Context window pressure, visible | blue-white context progress bar |
| Throughput / cost feel | **TPS gauge**, cache-hit rate, token counts, reasoning level |
| Working-status line | real-time working-status line |
| Esc-Esc to rewind | **double-Esc time rewind** (implemented as session **fork**) |
| Structured tool output | structured tool cards |
| `@` file references, completion | `@` refs, command + file completion |
| History search, message selection | both |
| `/resume` `/new` `/compact` `/export` | all present |
| `/vim` `/connect` `/hooks` | **placeholders — declared, not implemented** |
| Skills / MCP / subagents / Goals / Todos | surfaced from the host |
| — | `/lang zh/en`, inline vs alternate-screen render modes |

Two observations the operator should take from that table.

**(a) It clones the architecture, not just the look.** Claude Code's own TUI is — per third-party reverse-engineering, *not* Anthropic documentation — a React app on a heavily forked **Ink** renderer with a **Yoga** flexbox layout engine, screen-buffer double-buffering and **ANSI diffing** (`JSX → react-reconciler → Ink DOM → Yoga → screen buffer → ANSI diff → stdout`), reportedly 140+ components and 85 hooks. dsh-TUI's stated pipeline: *Cordis profile → index.ts → plugin.ts → DSH services → channel projection → Chat screen → components → **ported Ink renderer + Yoga layout** → terminal*, with 「差分输出」 (**differential output** — write only what changed), virtualised message lists using cached off-screen row heights, replay merging of token chunks, bounded caches, and terminal cell-width handling for ANSI/emoji/CJK.

Same stack, same techniques, independently arrived at. Note the dependency list contains **no `ink` package** but does contain `react-reconciler` plus essentially Ink's entire dependency set (`@alcalzone/ansi-tokenize`, `auto-bind`, `cli-boxes`, `code-excerpt`, `indent-string`, `signal-exit`, `stack-utils`, `wrap-ansi`, `get-east-asian-width`…) — consistent with the "**ported** Ink core" phrasing: Ink was vendored and modified, exactly as Claude Code forked it.

**(b) The placeholders are the tell.** `/vim`, `/connect`, `/hooks` exist as commands with no capability behind them. Someone catalogued Claude Code's command surface and shipped the shell of it. The clone is **incomplete and knows it** — which is honest, and also tells you precisely where the imitation stops.

For an operator whose Goal #1 is mastering Claude Code, this is a competitor's checklist of what CC's TUI does that was worth copying. It also **extends the `grok-build` v215 "agent-primitive convergence" watch axis to the presentation layer**: the convergence is no longer just skills/subagents/hooks/plan-mode/MCP — it now reaches the rendering stack and the keybindings.

---

## 4. Engineering: what is genuinely good here

**An 11-script `verify:*` suite** in `package.json`:

```
verify:build   verify:boundary   verify:contract   verify:manifest-deps
verify:patch-surface   verify:packaged-presets   verify:minimal-preset-tools
verify:liangshen-bootstrap   verify:package   verify:prompt-debug
verify:clipboard-image
```

**`verify:boundary` and `verify:patch-surface` are the interesting ones**: they mechanise the "zero core changes / uninstall leaves no core patches" claim. The plugin does not ask to be trusted about non-invasiveness; it fails its own build if it starts patching the host. That is a genuinely borrowable idea — *a CI gate that enforces an architectural boundary rather than documenting it* — and it is the **third consecutive ship** to hand the vault machinery for enforcing its own invariants (v234 staleness-tracking + recompilation, v235 doc-verification gates `verify-doc-refs`/`verify-doc-budgets`/`verify-md-links`, now v236 boundary gates). Three ships in a row pointing at the same unattended vault problem is not a coincidence worth ignoring.

Also real: `@xterm/headless` in devDeps (headless terminal testing), TypeScript 6, React 19.2, Node `^22.19 || >=24`, a `skills/` directory, `presets/liangshen/` with its own bootstrap verifier, `.github/workflows`, cross-platform clipboard (PowerShell / `osascript` / `wl-paste`), automatic light/dark detection, and a custom 「轻雾蓝」 ("Gentle Mist Blue") palette.

---

## 5. The honest weaknesses

- **The hard parts are not here.** Agent loop, model access, tools, session, persistence, sandboxing — all upstream in v235. This is a presentation layer. Removing it costs you a nicer terminal, not a capability.
- **No automated end-to-end tests with real credentials.** Author-stated: integration requires **manual terminal verification**. The `verify:*` suite checks structure and boundaries, not behaviour against a live model.
- **It is pinned to a release candidate of a four-day-old developer preview** whose own README warns in bold of **compatibility-breaking changes** — via 21 peer deps at `^0.1.0-rc.6`. Expect it to break.
- **Documented limitations:** injected plugin context is not shown separately in the UI; model switching is a **session fork, not an in-place swap**; exit does not await async agent persistence; clipboard read depends on external per-platform tools; `/vim` `/connect` `/hooks` are inert.
- **The "official recognition" is author-stated.** 「DSH 官方公众号收录」 — featured in DeepSeek Harness's official WeChat account as a *"beta user selected plugin."* Echoed by third-party plugin directories, but WeChat is not web-verifiable and DeepSeek publishes no endorsement I could fetch. Treat as a claim, not a credential.
- **The directories that echo it publish wrong metadata.** `dshhub.org` lists dsh-TUI as **v0.3.3, BSD-3-Clause**; the repo and `package.json` say **v0.8.0, MIT**. Stale version *and* wrong licence. The repo is authoritative (the Kilo Code v177 licence-discrepancy precedent). This matters beyond bookkeeping — see below.
- **Not source-cloned.** Rendered repo page, raw README, raw `package.json`, raw `docs/architecture.md`, author profile, directory listings, landscape search. Treat the tree as unverified.

---

## 6. The ecosystem context nobody should miss

Searching for this plugin surfaced something larger than the plugin: **a DSH plugin land-rush**. Within days of v235's preview there are ~**1,120 plugins** listed (dshbase.com, page-stated) across at least **eight competing directory sites** — dshhub.org, deepseekplugin.org, deepseek-code.com, dshplugin.dev, dshbase.com, deepseek-harness-plugin.com, dshplugin.app, awesome-dsh-plugin.com — several of which read as automated SEO aggregation ("generated from public repository data"), none disclosing an operator, and at least one publishing the wrong licence for this very plugin.

There is also a **rival UI-layer plugin** in the same ecosystem (`dsh-desktop`), so dsh-TUI is not even alone in its niche.

Two consequences:

1. **It revises v235's picture.** v235 shipped with ~19% ecosystem compatibility (41/219 packages) and reviewers advising a 3–6 month wait. The plugin count says adoption is moving far faster than the compatibility number suggested — while the reviewers' caution about stability still stands.
2. **It is a supply-chain warning.** A thousand-plus unvetted plugins for a release-candidate runtime, indexed by anonymous directories with demonstrably incorrect licence metadata, is a hostile place to `npm i -g` from. Install from the repo/npm and read the package; do not trust a directory.

---

## 7. The one idea to steal

**Event log is the source of truth; the UI holds only a projection.**

dsh-TUI keeps no authoritative state. History, streaming, rewind boundaries, and post-fork reconstruction all come from replaying the host's append-only `session/event` log; the Channel retains only a view shaped for the current display. That buys three things at once: any number of independent front ends, free time-travel, and an audit trail that exists because the architecture needs it — not because a policy asked for it.

That is exactly the property the vault's **RATIFIED candidate-LLM legibility ADR** demands of any hireui path that touches a candidate: fixed, legible, audited, human-in-loop, eval-gated. v235 supplied the invariant (append-only, everything the model saw is recorded). v236 supplies the proof that a real UI can be built on nothing but that log — which is the part that makes the invariant cheap instead of ceremonial.

Second idea, smaller and immediately usable: **`verify:boundary` / `verify:patch-surface`** — encode an architectural boundary as a build gate.

---

## 8. Cross-references

- **v235 deepseek-harness** — the host. Genuine `#57` corpus-recursion via 21 declared peer deps; v236 exercises v235's plugin thesis, its Cordis disposability, and its append-only log.
- **v72 DeepSeek-TUI** (`Hmbown`) — the corpus's *other* third-party DeepSeek TUI, and the boundary case. v72 is a standalone single-vendor **terminal client** for DeepSeek **models**; v236 is an **in-process plugin** replacing the UI seam of a **coding-agent runtime**. Client vs plugin, models vs runtime. Not the same class.
- **CodePilot v161 (§C#27)** — a GUI that **wraps** a CLI agent from outside. v236 mounts **inside**. Opposite direction.
- **hermes-webui v227** — the closest precedent: a community front end for someone else's agent. Also the decisive NO-MINT rule (front-end form-factor within a genre).
- **Codex-Dream-Skin v216** — a UI layer for a rival's tool, rated OFF-GOAL. v236 clears that floor decisively: v216 was decoration with zero functional surface; v236 implements the entire interaction layer.
- **grok-build v215** — agent-primitive convergence, here extended to the presentation layer.
- **openinterpreter v223** — harness *emulation*; v235 was harness *delegation*; v236 is harness **re-skinning**. Three points on one watch axis.
- **pi v228 / v36** — reachable as the model backend through v235's `llm-pi-ai` seam, which is how Claude runs under this TUI.

---

## 9. Verification note

Verdict produced **inline and fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — no workflow, no subagent (the ~966 KB shim overflows any subagent's 200 K context; the v200→v235 self-throttle).

- Source hand-fetched: rendered repo page, raw `README.md`, raw `package.json`, raw `docs/architecture.md`, author profile, `dshhub.org` listing.
- Identity and landscape by WebSearch.
- **Collision by sanity-anchored hand-grep: CLEAN.** `dsh-TUI` = **0** hits and `ccch1mney` = **0** hits across `_state/` and `_patterns/`; anchors `deepseek-harness` (7 in `_state/03c`, 1 in `_patterns/06`), `DeepSeek-TUI`, `Cordis` (6), `shigma` (2), `CodePilot` (13), `hermes-webui` (1) all hit → the grep works, so the empty result is trustworthy. `Ink` = 0 in `_patterns/06` (no prior Ink subject).
- **Three things caught by hand:** the directory's **v0.3.3 / BSD-3-Clause** vs the repo's **v0.8.0 / MIT**; the absence of an `ink` dependency despite Ink's full dependency set present (→ *ported*, i.e. vendored, matching the description rather than contradicting it); and the peer range `^0.1.0-rc.6` sitting one prerelease **ahead** of the `0.1.0-rc.5` recorded at v235.
