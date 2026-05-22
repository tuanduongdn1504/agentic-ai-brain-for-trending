---
source: yt-dlp-only + 3-webfetch
path: 5-yt-dlp + 3-webfetch
urls:
  - https://www.youtube.com/watch?v=XoitaexiCi0
  - https://github.com/ogulcancelik/herdr
  - https://herdr.dev
video_id: XoitaexiCi0
video_title: "Herdr: the Tmux for AI Agents"
video_channel: Hal Shin (@halshin_software) — explainer/reviewer, NOT the repo author
video_duration: 13:19
video_uploaded: 2026-05-17
video_views: 25219
repo: ogulcancelik/herdr
repo_author: Ogulcan Celik
repo_stars: 2020
repo_forks: 137
repo_language: Rust
repo_license: AGPL-3.0 (copyleft)
repo_created: 2026-03-27
repo_size_kb: 22198
repo_open_issues: 42
fetched: 2026-05-21
notes: |
  Video is a third-party explainer; the product is Herdr. Author and
  explainer are different people. Hal Shin has 25K views and a separate
  video on cmux (competitive product) — implicit channel positioning is
  "new agent tooling explainers".

  Pulled comparison to Zen van Riel config (prior ingest 2026-05-21)
  per user request "best practice using tmux". This is a comparative
  article, not just a single-source ingest.

  6 files fetched from the herdr repo (README + SKILL + AGENTS +
  quick-start + configuration + agents + install). Repo has 5 docs pages
  + Rust source (~60 files) + CI/release workflows + .pi/ prompts
  folder. Not fully ingested — README + SKILL + AGENTS are the
  load-bearing pieces for understanding architecture.

  CRITICAL CORPUS SIGNAL: Herdr's SKILL.md is the 2nd corpus instance of
  "skill files as engineering artifacts" — distinct from vibe prompts
  AND from SDD specs. Catalog of ~25 CLI commands + anti-fabrication
  rules + gate clauses (HERDR_ENV=1 check) + recipes. Composes with
  Zen's /smell as a sister pattern.

  91 comments — highest-engagement video this session arc. Top-liked
  critical comment (6♥): "i feel super comfortable with tmux. Not
  enough difference to make the switch" — a real practitioner signal
  that Herdr is nice-to-have, not necessary.
---

# Herdr: the Tmux for AI Agents — combined video + repo audit

> **Video:** [YouTube XoitaexiCi0](https://www.youtube.com/watch?v=XoitaexiCi0) — Hal Shin (`@halshin_software`), 13:19, uploaded 2026-05-17, **25,219 views** at fetch
> **Product:** [Herdr](https://herdr.dev) by Ogulcan Celik — 2020★, 137 forks, Rust, **AGPL-3.0**, active development (last push 2026-05-21)
> **Tagline:** "agent multiplexer that lives in your terminal" (formally) / "tmux for AI agents" (informal positioning per Hal's video + Herdr's own marketing)
> **Compile target:** `wiki/harness-engineering/personal-repo-herdr-agent-multiplexer.md` (new 8th individual-scale sibling — with explicit `tmux-vs-herdr-best-practices` comparison section per user's framing)

---

## Part 1 — Video synthesis (Hal Shin's explainer)

### Topline framing

> "Herdr is marketed as a tmux for agents... it's a terminal multiplexer, so you're able to manage multiple terminal programs from a single screen. And this is solving a critical AI workflow problem that I've been having. And that is being able to start a really long coding session on my terminal, close my laptop, walk away, come back, and resume that session."

The hook is **session persistence for long-running AI agents**, not workspace management or mouse UX. Hal explicitly says the persistence + remote attach is the headline feature for him.

### Architecture as Hal demos it

| Primitive | Herdr's term |
|---|---|
| Top-level container | **Workspace** ("space" in the UI sidebar) |
| Within workspace | **Panes** + **tabs inside panes** |
| Cross-workspace | **Sessions** (separate persistent herdr servers, each with own socket) |

**Key tmux-compatible primitives demoed:**
- `ctrl+b` prefix mode (same as tmux default)
- `ctrl+b ?` shows keyboard bindings
- `ctrl+b q` to detach session
- `ctrl+b x` to kill a pane
- Arrow-key navigation between panes
- Configurable bindings

**Key non-tmux UX:**
- Mouse-native: right-click for split-vertical / split-horizontal / rename / close
- Drag borders to resize
- Sidebar showing workspace tree + agent statuses

### The agent-awareness feature (load-bearing)

Hal demos spinning up Claude + Codex panes. The sidebar shows agent status with visual indicators:

| State | Meaning |
|---|---|
| 🔴 blocked | Agent needs input/approval (also triggers macOS notification + ping) |
| 🟡 working | Agent is actively running |
| 🔵 done | Finished but user hasn't looked yet |
| 🟢 idle | Done and seen |

> "this is a super common problem that a lot of people who are using coding harnesses face. You just kind of start a prompt, you walk away, you come back, you're like, 'Oh, shoot, it hasn't done anything, right?'"

Demo: types `say hello back to me after 4 seconds` — pane status flips to "working", then back to idle. Then a permission-prompt scenario flips it to "blocked" with notification ping.

### Remote SSH attach

Hal demos `herdr --remote HS-Macaroni` (using SSH host config) to attach to a Herdr instance running on a home Ubuntu server. Connection bypasses interactive SSH — uses the local Herdr as a thin client streaming the remote UI.

> "this is a super way for me to be able to asynchronously [run] my coding sessions"

### Agent orchestration via CLI

The Herdr binary exposes commands that talk to the local Unix socket:
- `herdr workspace list/create/get/rename/close`
- `herdr pane list/split/run/send-keys/wait/read`
- ...

Demo: Hal prompts Codex *"Use the CLI to spin up two Codex instances and inside of those, look up for the capital of South Korea and also France."* Codex reads `herdr` help, then uses `herdr pane split` + `herdr pane run` to fan out. (First demo on Cloud Code had state mismatch issues; switched to Codex which worked.)

> "I would honestly recommend that you get your coding agent to read through the documentation, read through the CLI commands, and make a skill out of it so that you have a repeatable process to be able to spin up these panes directly."

(Note: top-liked commenter `@jaypears4148` confirms this skill **already exists in the repo as SKILL.md** — see Part 2.)

### Stated limitations

1. **No built-in browser** (vs tmux's plugin ecosystem that includes one). Agent can't "see" rendered pages without external Playwright/Chrome DevTools MCP.
2. **Mouse UX has rough edges** — Hal notes right-click split is "functional, not ideal" compared to tmux's nicer GUI in some configs.
3. **Unix-only** (Mac + Linux; Windows via WSL only).
4. **State sync bugs** — Cloud Code statuses didn't match up during recording; required switching to Codex.

### Closing case

> "you have one main orchestrating AI agent, and this AI agent is able to delegate some of these tasks to different agents so that you're able to do multiple coding sessions at the same time. Or if you go the other way, which is to use multiple agents to improve the quality of a single coding session, you're able to use maybe like a planning agent, a coding agent, a reviewing agent, a like QA agent."

Same "multi-agent role split" pattern present in [[wiki/harness-engineering/personal-repo-hermes-orchestrator]] and [[wiki/harness-engineering/personal-repo-zen-mixed-effort-parallel]] — Herdr is the **terminal substrate** that makes the pattern observable + scriptable from a single sidebar.

---

## Part 2 — Repo audit (the official artifacts)

### Repo facts (verbatim from GitHub API)

```
stars:        2020
forks:        137
language:     Rust
license:      AGPL-3.0 (copyleft — modified versions must be open-sourced under same license)
default:     master  (NOT main — initial tree fetch on main returned 404)
created:     2026-03-27  (~2 months old at fetch)
last push:   2026-05-21
size:        22.2 MB
open issues: 42
```

Tree highlights:
- Rust source: `src/main.rs` + `src/cli.rs` + `src/{app,api,terminal,server,client,integration,ghostty,protocol}/...`
- Docs: 5 `.mdx` pages (index/quick-start/install/configuration/agents)
- Top-level markdown: `README.md` + `SKILL.md` + `AGENTS.md` + `CONTRIBUTING.md` + `CHANGELOG.md`
- `.github/workflows/*` — 5 workflows incl. release + PR gate + contributor approval
- `.pi/prompts/pre-release-audit.md` — AI-driven release audit (Pi integration; not yet ingested)
- `vendor/libghostty-vt/` — vendored Ghostty terminal library

### README.md (10K+ chars verbatim — key sections)

**Install:**
```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

**Quick start verbatim:**
> "by default herdr launches or attaches to one background session server. `ctrl+b q` detaches the client. agents keep running. use `herdr server stop` to stop the default server."

**Sessions vs Workspaces (an important distinction Hal didn't fully cover):**
> "named sessions are runtime/socket namespaces for separate persistent herdr servers. they do not replace workspaces; each named session has its own panes, tabs, workspaces, sockets, and session state while sharing the same global config file."

**README's own comparison table:**

|                            | tmux | gui managers | herdr |
|----------------------------|------|--------------|-------|
| persistent sessions        | ✓    | —            | ✓     |
| detach / reattach         | ✓    | —            | ✓     |
| panes, tabs, workspaces   | ✓    | ✓            | ✓     |
| agent awareness           | —    | ✓            | ✓     |
| lives in your terminal    | ✓    | —            | ✓     |
| real terminal views       | ✓    | —            | ✓     |
| mouse-native             | —    | ✓            | ✓     |
| lightweight binary        | ✓    | —            | ✓     |
| agents can orchestrate    | ?    | ?            | ✓     |

The "?" entries for tmux+gui under "agents can orchestrate" are **load-bearing**: tmux CAN orchestrate via `tmux send-keys` etc., it's just not designed for it.

**Supported agents (12):** pi (the README author's other project), claude code, codex, droid, amp, opencode, grok cli, hermes agent, kiro cli — with detection grids per (idle/done × working × blocked). Detected but less tested: gemini cli, cursor agent, cline, kimi, github copilot cli.

**Direct integrations** for 5 of them (pi/claude/codex/opencode/hermes) install via `herdr integration install <name>` — forwarding semantic state over socket API for more precise blocked/working/done than heuristic-based detection.

**Default keybindings (tmux-compatible prefix):**
```
prefix+c       new tab
prefix+n/p     next/prev tab
prefix+1..9    switch tab
prefix+w       workspace navigation
prefix+shift+n new workspace
prefix+h/j/k/l focus pane (vi-style)
prefix+v/-     split pane (vertical/horizontal)
prefix+x       close pane
prefix+z       zoom pane
prefix+r       resize mode
prefix+q       detach
```

**Config:** `~/.config/herdr/config.toml`. `herdr --default-config` to print defaults.

**Logs:** `~/.config/herdr/herdr{-client,-server}.log` with rotation. Pane contents excluded by default. Higher verbosity via `HERDR_LOG=herdr=debug herdr`.

### SKILL.md (300 lines verbatim — the load-bearing artifact for agent orchestration)

YAML frontmatter:
```yaml
name: herdr
description: "Control herdr from inside it. Manage workspaces and tabs, split panes, spawn agents, read output, and wait for state changes — all via CLI commands that talk to the running herdr instance over a local unix socket. Use when running inside herdr (HERDR_ENV=1)."
```

**Gate clause (verbatim, first paragraph after frontmatter):**
> "before using this skill, check that `HERDR_ENV=1`. if it is not set to `1`, say you are not running inside a herdr-managed pane and stop. do not inspect or control the focused herdr pane from outside herdr."

This is the **2nd corpus instance of "skill files as engineering artifacts"** (sister to Zen's `/smell`). Distinct from vibe prompts. Discipline patterns:

1. **Environment gate clause** — agent must abort if not running inside Herdr
2. **Anti-stale-id rule (verbatim):** *"ids can compact when tabs, panes, or workspaces are closed. do not treat them as durable ids. re-read ids from `workspace list`, `tab list`, `pane list`, or create/split responses when you need a current id. do not guess that an older `1-3` is still the same pane later."*
3. **Source-of-truth discipline for waiting vs reading:** explicit warning that `pane read --source recent` shows wrapped text but `wait output --source recent` matches unwrapped — use `pane read --source recent-unwrapped` to inspect the same transcript the waiter matches
4. **JSON parsing recipe** uses python3 inline to extract `result.pane.pane_id` from split responses
5. **5 worked recipes:** server-and-wait, tests-and-inspect, watch-another-pane, spawn-agent-and-give-task, coordinate-with-another-agent

**The "coordinate with another agent" recipe (worth highlighting):**
```bash
herdr wait agent-status 1-1 --status done --timeout 120000
herdr pane read 1-1 --source recent --lines 100
```

This is a **2-line cross-pane synchronization primitive** — directly supports the multi-agent role split pattern. Equivalent to a process-level await on another agent's completion.

### AGENTS.md (project memory for AI agents working on Herdr itself)

Key principles verbatim:

> "State is separated from runtime. AppState is pure data, testable without PTYs or async."
> "Render is pure. compute_view() handles geometry and mutations. render() takes &AppState and only draws. Never mutate state during render."
> "No god objects."

**Multi-agent isolation pattern (verbatim):**
> "Use this layout:
> - shared integration checkout: `../herdr`
> - task worktrees: `../herdr-worktrees/<task-slug>`
> - task branches: `issue/<id>-<slug>` when an issue exists"

> "When the change is ready, fast-forward the shared checkout at `../herdr` to the task branch commit, then push `origin/master` from `../herdr`. Do not treat the task branch as the final landing branch."

> "Before committing, propose the commit message and get alignment."

This is **a worked example of the worktree pattern** from Zen's video — but with concrete naming conventions and a fast-forward-from-shared discipline that goes beyond the basic `git worktree add`.

### Install docs (verbatim)

```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

Single Rust binary. Manual download from GitHub releases also available with platform-specific assets:
- `herdr-linux-x86_64`
- `herdr-linux-aarch64`
- `herdr-macos-x86_64`
- `herdr-macos-aarch64`

**Windows:** *"Native Windows support is not available yet; use Herdr inside WSL for now."*

---

## Part 3 — Comments thread (91 total, top-engagement of this session arc)

### Top-liked critical comment (6♥)

> **@andresgutgon (6♥):** "I came with an open mind. And kind of like this, but i feel super comfortable with tmux. Not enough difference to make the switch for me. But great video!"

**This is the load-bearing practitioner signal.** Among 91 comments, the highest-liked non-OP-reply substantive comment is "tmux is enough." Real signal that Herdr is **nice-to-have, not necessary** for the existing tmux-comfortable cohort.

### Highest-liked pro-tip (12♥)

> **@jaypears4148 (12♥):** "Pro tip: the herdr SKILL is in the repo. Install it locally and use that for your agent."

Confirms the [SKILL.md](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) is THE concrete pilot-relevant artifact, more than the rest of the marketing.

### Cross-product mentions (corpus surface)

The thread surfaces a long list of competing tools the corpus does not yet have:

| Tool | Type | Source |
|---|---|---|
| **cmux** | tmux-like multiplexer for agents (Mac-only per commenter) | Mentioned by multiple commenters; Hal has separate cmux video |
| **Agent of Empires** | "more mature" agent orchestrator | @tantalus_complex (1♥) |
| **T3 Code** | agent orchestrator | @tantalus_complex |
| **Conductor** | agent orchestrator | @tantalus_complex |
| **Workmux** | agent orchestrator | @tantalus_complex |
| **agent-deck** | agent pool orchestrator | @misunderst00d (2♥) |
| **getlemonadedotdev** | unknown — promoted twice (suspicious double-mention from different accounts) | @devteamdrew + @DSAD___DreW (2♥ each) |
| **Claude Code `/remote-control`** | vendor-locked Anthropic alternative | @Sivxgamer (1♥) |

**Implication:** the "agent multiplexer" category is **at least 7 deep**. Herdr's 2020★ is not the leader; the @tantalus_complex comment specifically claims 4 named alternatives are "quite a bit more mature." Worth follow-up audit at next mini-audit cadence — this could be a corpus-first "agent-multiplexer category emergence" candidate at Storm Bear v66.

### Pi integration adjacency

Herdr's README lists Pi as the FIRST supported agent (above Claude Code and Codex). Pi is by `earendil-works/pi` per the README's footer reference. The Herdr author's own work appears connected to Pi (`.pi/prompts/pre-release-audit.md` exists in the repo) — Pi may be a related project by the same author/team. Worth a separate ingest at some point.

### Operational comments

- **@MightyMisanthrope:** "herdr does not support gemini or hermes at this moment. But it's a great idea" → contradicts the README's "supported" entry for Hermes. Reality may be partial/in-progress.
- **@danddand:** "If you add issue to GitHub the author is very responsive. I asked about copilot and it was added same day" → maintainer is actively shipping. Lines up with active 42 open issues + pushed-yesterday signal.
- **@odayfans:** "tmux+good terminal (wezterm/ghostty) does all of these. nothing new" → echoes the top-liked critical comment.
- **@dennis605:** Mouse copy-paste works "but not in wezterm" → terminal-emulator-specific UX gotcha.

---

## Part 4 — Best-practices-for-tmux synthesis (the user's actual ask)

Given both prior ingests ([[wiki/harness-engineering/personal-repo-zen-mixed-effort-parallel|Zen van Riel]]) and this one ([Herdr]), here is the best-practices distillation the user asked for:

### Decision tree — which tmux approach when

```
Are you on Windows (non-WSL)?
  → Tmux + scripts (Zen-style) is your only real option
  → OR use a Windows-native alternative (out of scope)

Do you need mixed-effort routing (CLAUDE_CODE_EFFORT_LEVEL per pane)?
  → Zen wins. Herdr has no such primitive.

Do you need first-class agent status (blocked / working / done) visible in a sidebar?
  → Herdr wins. Tmux + scripts gives you nothing here.

Do you need programmatic agent orchestration from inside an agent
(e.g., agent A spawns agent B and waits for B's status to reach `done`)?
  → Herdr wins clearly. The wait agent-status primitive is unmatched.

Do you need to detach + reattach from a phone over SSH?
  → Both can do it. Tmux's persistence is ~25 years battle-tested.
  → Herdr's --remote with SSH config is more ergonomic but newer.

Do you need a catalog-driven code review workflow (/smell with 70 catalog IDs)?
  → Zen ships it; Herdr doesn't bundle it.
  → BUT: you can adopt Zen's /smell alone (it's just one .md file) regardless
    of the rest of the tmux setup.

Do you care about AGPL-3.0 license implications?
  → Herdr is AGPL-3.0. If your day job has a copyleft prohibition, that's a blocker.
  → Zen's bundle has no license file but README says "feel free to adapt".

Do you want zero dependencies?
  → Herdr: single Rust binary, no deps.
  → Zen: requires jq + tmux + zsh + Claude Code installed.
```

### The compose pattern (per README: "works inside tmux")

Herdr **runs inside tmux** per its README. This means a third option exists:

- **Outer layer = tmux** with Zen's `t()` launcher for 4-pane mixed-effort + Zen's `/smell` slash command
- **Inner layer = Herdr** for first-class agent state + socket-API orchestration

Tradeoff per Hal's video: *"If you're running Herder inside Tmux, you also have access to the Tmux CLI, so you can use a Tmux browser like that. But the downside there is that you're now not able to kind of use that detach attach kind of functionality."*

So composition costs the Herdr-level detach/reattach — you'd be detaching at the tmux layer instead. Acceptable for most workflows.

### The "tmux is enough" position (top-liked critical comment, 6♥)

@andresgutgon's comment is empirically corroborated by:
- Hal's own admission of state-sync bugs during recording (Cloud Code statuses didn't match)
- Herdr's stated limitations (no built-in browser, rough mouse-UX edges)
- AGPL-3.0 license friction for enterprise

A reasonable "best practice" for a tmux-comfortable practitioner: **start with Zen's setup, adopt Herdr only if/when you hit specific gaps it solves** (multi-agent sidebar awareness or socket-API orchestration). Don't switch wholesale.

### Three concrete patterns extractable from Herdr regardless of adoption

Even if you don't adopt Herdr, three primitives from it are reusable in any tmux + scripts setup:

1. **Multi-agent isolation via worktree naming convention** (from Herdr's AGENTS.md):
   - shared checkout: `../<project>`
   - task worktrees: `../<project>-worktrees/<task-slug>`
   - task branches: `issue/<id>-<slug>` when an issue exists
   - **Fast-forward shared from task branch** before pushing — not the task branch as final landing branch
2. **The HERDR_ENV gate clause** pattern (from SKILL.md): every skill checks an env var before acting. Generalizes to any environment-specific skill (e.g., `CLAUDE_CODE_EFFORT_LEVEL` could trigger a "high-effort-only" skill).
3. **Anti-stale-id discipline** (from SKILL.md): id documents in a skill must include "re-read ids; do not guess durability." Worth adding to any Storm Bear-derived skill that references symbolic identifiers.

---

## Part 5 — Cross-corpus signals

### Within autopilot wiki

- **[[harness-engineering/personal-repo-zen-mixed-effort-parallel]]** — direct sibling and primary comparison target. Zen = personal tmux config + `/smell`; Herdr = standalone agent multiplexer product.
- **[[harness-engineering/personal-repo-hermes-orchestrator]]** — Hermes is in Herdr's supported-agents list (Herdr forwards Hermes's semantic state). Composes cleanly: Hermes for orchestration, Herdr for visibility.
- **[[harness-engineering/personal-repo-router-multimodel]]** — orthogonal to Herdr (router is in-process model routing, Herdr is process-level terminal multiplexer). Compose: run howznguyen's Claude Code in a Herdr pane.
- **[[harness-engineering/personal-repo-patterns]]** — sub-agents pattern adjacent.
- **[[harness-engineering/anthropic-large-codebases-anchor]]** — Anthropic's 7-component decomposition. Herdr is **not** Anthropic's frame at all (it's terminal-multiplexer-level), but the SKILL.md is a textbook example of Anthropic's "skill" component primitive.

### Storm Bear (mention only — cannot write from this scope)

- **Pattern #18 Layer 2** — Herdr is a candidate for a new sub-archetype: **terminal-multiplexer-as-agent-substrate**. Distinct from runtime-API-proxy (free-claude-code) / install-time-skill-translator (cc-sdd) / plugin-bridge (codex-plugin-cc) / 3rd-party-orchestrator-wrapping-CLIs (Hermes). Herdr is **multiplexer-publishing-socket-API-for-cross-pane-coordination**.
- **Pattern #76 Adversarial Subagent Review Architecture** — Herdr enables but does not prescribe this pattern. The "coordinate with another agent" recipe (`wait agent-status ... done`) is the cross-pane synchronization primitive that adversarial review needs.
- **Candidate observation-track: agent-multiplexer category emergence.** Surfaced by viewer comments listing 7 named alternatives (cmux, Agent of Empires, T3 Code, Conductor, Workmux, agent-deck, Claude `/remote-control`). Worth registering at v66 if a second corpus instance lands.
- **Candidate observation-track: skill-files-as-engineering-artifacts** strengthens. Now N=2 in corpus (Zen `/smell` + Herdr SKILL.md). Both are catalog-driven + anti-fabrication-disciplined + distinct from vibe prompts. If a 3rd lands, this becomes a top-level candidate.

---

## Part 6 — Pilot-readiness

**Tier-A pilotable in 5 minutes:**

```bash
curl -fsSL https://herdr.dev/install.sh | sh
herdr
# inside: ctrl+b shift+n to create workspace, run `claude`, ctrl+b v to split, etc.
```

Plus optional:
```bash
herdr integration install claude  # for richer semantic state
```

**Pilot cost: ~5 min** (vs ~1h for Zen's setup).

**Constraints to verify before adopting in real work:**

1. **License:** AGPL-3.0 — if you redistribute modifications, must open-source under same. Pure use is fine.
2. **OS:** macOS or Linux only. Windows = WSL only.
3. **State sync bugs** flagged in Hal's video for Cloud Code specifically — verify Claude Code integration is stable in your environment before relying on the sidebar status.
4. **Mature alternatives exist** (cmux, agent-deck, etc.) — worth a quick comparison before committing.

---

## Key takeaways

1. **Herdr is a real product (2020★), not a config.** Rust binary, AGPL-3.0, active development, official docs site.
2. **The load-bearing innovation is the agent-status state machine + socket API**, not the multiplexer itself. Tmux already does multiplexing.
3. **The SKILL.md is the 2nd corpus instance of "skill files as engineering artifacts"** — gate clauses, anti-stale-id rules, source-of-truth discipline for wait vs read, 5 worked recipes. Pattern with Zen `/smell` = corpus-first observation-track candidate.
4. **Best practice for tmux-comfortable practitioners:** stay with tmux + Zen's setup, add Herdr only if specific gaps emerge (sidebar agent state OR socket-API orchestration).
5. **Best practice for new practitioners:** Herdr's 5-minute install is materially lower-friction than Zen's ~1h setup. Easier on-ramp.
6. **Composition is valid:** Herdr runs inside tmux. Outer tmux for Zen's mixed-effort layout + `/smell`, inner Herdr for agent visibility + cross-pane wait/read primitives.
7. **Three patterns extractable regardless of adoption:** worktree naming convention from AGENTS.md, env-var gate clause from SKILL.md, anti-stale-id discipline from SKILL.md.
8. **Real practitioner skepticism** is documented in comments (top-liked critical 6♥ + repeated "tmux is enough" sentiment). Don't ignore the "nice-to-have not necessary" framing.
9. **7+ competing tools exist** in the agent-multiplexer category — Herdr is not the leader. cmux, agent-deck, Workmux, Conductor, T3 Code, Agent of Empires all surfaced in comments. Category emergence is corpus-relevant.
10. **Pi project adjacency** worth flagging — Pi appears related to Herdr (first agent in supported list, `.pi/prompts/` in repo). Worth a separate ingest at some point.
