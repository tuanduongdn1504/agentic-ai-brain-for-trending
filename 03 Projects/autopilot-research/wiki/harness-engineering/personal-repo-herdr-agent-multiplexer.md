# Personal-repo extension — Herdr agent multiplexer + tmux best practices

> **Sources:** Hal Shin (explainer) — [Herdr: the Tmux for AI Agents](https://www.youtube.com/watch?v=XoitaexiCi0), 2026-05-17, 13:19, **25,219 views** + Ogulcan Celik (author) — [github.com/ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) — Rust, 2020★, AGPL-3.0, 137 forks, ~22.2MB source, active development
> **Raw:** `raw/2026-05-21-herdr-agent-multiplexer-shin-celik.md`
> **Compiled:** 2026-05-21
> **Status:** N=1 single-product extension to [[personal-repo-overview|individual-scale layer]]. Sibling to [[personal-repo-zen-mixed-effort-parallel]] but at a different layer of the stack: Zen ships a tmux config + scripts, Herdr ships an entire terminal multiplexer alternative. Explicit comparative section "Best practices for tmux + AI agents" at end answers the user's framing.

---

## Topline in one paragraph

**Herdr is an agent multiplexer that lives in your terminal** — a Rust binary positioned as "tmux for AI agents" with tmux-compatible prefix bindings (`ctrl+b`), workspace/tab/pane hierarchy, persistent background sessions surviving detach, SSH remote attach via `herdr --remote`, mouse-native UX, and **a first-class agent-state state machine** (idle / working / blocked / done) rolling up across panes/tabs/workspaces. It exposes a **local Unix socket** so agents can spawn helpers, read other panes, and `wait agent-status ... done` on each other — turning the terminal itself into an agent orchestration substrate. Single-binary install via `curl ... | sh`. **AGPL-3.0** licensed. 2020 stars at fetch with active development.

---

## Why this matters at the architectural layer

The harness-engineering individual-scale layer has accumulated 7 prior siblings covering **what runs in the panes**:
- [[personal-repo-overview]] + [[personal-repo-patterns]] — sub-agents, worktrees, validation loops inside a Claude Code session
- [[personal-repo-router-multimodel]] — cross-vendor model routing via in-process router
- [[personal-repo-hermes-orchestrator]] — cross-vendor via process-level orchestrator (Hermes) shelling out to CLI subprocesses
- [[personal-repo-zen-mixed-effort-parallel]] — same-vendor mixed-effort across 4 tmux panes via env var
- [[personal-repo-vs-org-scale]] — Lopopolo comparison
- [[personal-repo-gaps]] — production gaps

**Herdr is a new layer: the substrate that hosts the panes themselves.** The other siblings are agnostic about whether they run in tmux, iTerm, Ghostty, etc. Herdr is the first source treating the multiplexer itself as load-bearing infrastructure.

---

## Architectural primitives

### State hierarchy

```
Server (per "named session" — own socket, own state)
  └── Workspace (project context; one or more tabs)
       └── Tab (subcontext; one or more panes)
            └── Pane (terminal split running one process: shell/agent/server/log)
```

IDs: workspaces `1`, tabs `1:1`, panes `1-1`. **Not durable across closes** — SKILL.md explicitly warns agents to re-read after any close.

### Agent-state state machine

| State | Meaning | UI |
|---|---|---|
| 🔴 blocked | Needs input/approval | macOS notification + ping |
| 🟡 working | Actively running | Sidebar highlight |
| 🔵 done | Finished, not yet viewed | Sidebar highlight |
| 🟢 idle | Done and seen | Default |

Detection signals (in increasing precision):
1. Foreground process matching
2. Terminal output heuristics
3. Integration state reports (via socket API; 5 agents have direct integrations: pi, claude, codex, opencode, hermes)

12 agents supported with detection grids per state column. Detected-but-less-tested: gemini cli, cursor agent, cline, kimi, github copilot cli.

### Socket API as orchestration primitive

The Unix socket exposes ~25 CLI commands grouped by domain:

```
workspace  list / create / get / rename / focus / close
tab        list / create / get / rename / focus / close
pane       list / get / split / run / send-text / send-keys / read / close / report-agent
wait       output / agent-status
agent      list / start / attach / rename / report-agent
terminal   attach
session    list / attach / stop / delete
server     status / stop
remote     (via --remote flag)
integration install / status
```

**The 2 unique primitives** (not in raw tmux):
- `herdr wait agent-status <pane> --status done --timeout <ms>` — block until another agent reaches a given state
- `herdr pane read <pane> --source recent --lines N` — read another pane's rendered output (with `--source visible` / `recent` / `recent-unwrapped` variants)

These two together = **process-level synchronization primitives for cross-agent coordination**. Tmux can do `send-keys` and `capture-pane` but doesn't expose a state-machine wait primitive.

---

## The SKILL.md is the 2nd corpus instance of "skill files as engineering artifacts"

Sister pattern to Zen's `/smell` (see [[personal-repo-zen-mixed-effort-parallel]]). 300 lines, 5 worked recipes. Disciplines verbatim from the file:

| Discipline | Verbatim quote |
|---|---|
| Environment gate | *"check that `HERDR_ENV=1`. if it is not set to `1`, say you are not running inside a herdr-managed pane and stop."* |
| Anti-stale-id | *"ids can compact when tabs, panes, or workspaces are closed. do not treat them as durable ids. re-read ids... do not guess that an older `1-3` is still the same pane later."* |
| Source-of-truth for wait vs read | Explicit warning that `wait output --source recent` matches unwrapped text but `pane read --source recent` shows wrapped — use `pane read --source recent-unwrapped` to inspect the same transcript |
| Recipes over recipes | 5 named recipes (server-and-wait, tests-and-inspect, watch-another-pane, spawn-agent-and-give-task, coordinate-with-another-agent) |

**Distinct from both vibe prompts and SDD specs.** Catalog-driven (~25 CLI commands documented inline), anti-fabrication (gate clauses + stale-id warnings), recipe-shaped output. Same shape as Zen's `/smell` despite covering entirely different ground (multiplexer control vs code review).

If a 3rd corpus instance lands, "skill-files-as-engineering-artifacts" becomes a strong observation-track candidate for Storm Bear Pattern Library.

---

## The AGENTS.md surfaces a worked example of the worktree-naming pattern

From the file verbatim:

> "Use this layout:
> - shared integration checkout: `../herdr`
> - task worktrees: `../herdr-worktrees/<task-slug>`
> - task branches: `issue/<id>-<slug>` when an issue exists"

> "When the change is ready, fast-forward the shared checkout at `../herdr` to the task branch commit, then push `origin/master` from `../herdr`. Do not treat the task branch as the final landing branch."

> "Before committing, propose the commit message and get alignment."

This is a **concrete worked example of the worktree pattern** Zen demos in his video. Zen shows `git worktree add wt-test`; Herdr's AGENTS.md gives **the discipline around it** — naming convention, fast-forward-from-shared, propose-commit-message governance. Reusable independently of Herdr adoption.

---

## Mapping to [[core-claims|harness-engineering core claims]]

| Lopopolo claim | This source's evidence |
|---|---|
| #1 Humans steer, agents execute | **Strengthens** — sidebar visualizes agent state for the human steerer |
| #2 Pre-merge review wasted | **Silent** (Herdr is substrate; doesn't prescribe review) |
| #3 Build-loop < 1 minute | **Silent** |
| #4 Throughput scales with parallel agents | **Strengthens** — sidebar makes N-agent visibility tractable; socket API enables programmatic coordination |
| #5 5-10 PRs/day/eng via Symphony | **Silent** |
| #6 Skills > prompts | **Strengthens** — Herdr's own SKILL.md is a textbook example of a skill artifact |
| #7 Adversarial evaluation | **Enables** — `wait agent-status done` is the cross-pane sync primitive adversarial-review patterns need |
| #8 Ralph loop | **Silent** (but compatible — Herdr could host Ralph-loop scripts) |

Net: 4 strengthens / 4 silent. Consistent with Herdr being a **substrate** for the harness layer, not the harness itself.

---

## Practitioner skepticism — load-bearing comment evidence

Among 91 comments on the source video, the **highest-liked critical comment (6♥)** is:

> **@andresgutgon:** *"I came with an open mind. And kind of like this, but i feel super comfortable with tmux. Not enough difference to make the switch for me. But great video!"*

Plus **@odayfans:** *"tmux+good terminal (wezterm/ghostty) does all of these. nothing new"*.

**These are not dismissable.** A 6♥ critical comment on a 25K-view video is real practitioner signal that the existing tmux+terminal cohort sees Herdr as nice-to-have, not necessary. Don't ignore.

Counter-signals also strong: **@jaypears4148 (12♥)** highlights the SKILL.md as the pilot-worthy artifact, and **@danddand** confirms maintainer ships fixes same-day for community requests. The product is real and active.

---

## Best practices for tmux + AI agents (the user's framing)

Given both [[personal-repo-zen-mixed-effort-parallel|Zen's tmux config]] and Herdr, here is a decision tree:

### When to use which

```
Are you on Windows (non-WSL)?
  → Tmux + Zen-style scripts is the only viable path
  → (or use a Windows-native alternative outside this corpus)

Do you need mixed-effort routing (CLAUDE_CODE_EFFORT_LEVEL per pane)?
  → Zen wins. Herdr has no such primitive.

Do you need first-class agent state (blocked/working/done) visible in a sidebar?
  → Herdr wins. Tmux + scripts gives you nothing here.

Do you need programmatic agent orchestration (agent A spawns B and waits for B's status)?
  → Herdr wins clearly via `wait agent-status` + `pane read --source recent-unwrapped`.

Do you need to detach + reattach from a phone over SSH?
  → Both can do it. Tmux's persistence is ~25 years battle-tested; Herdr's is months old.
  → Herdr's `--remote workbox` (SSH config-aware) is more ergonomic.

Do you need a catalog-driven code review workflow (Zen's /smell)?
  → Zen ships it; Herdr doesn't bundle it.
  → But you can adopt Zen's /smell standalone regardless of multiplexer choice.

Do you care about AGPL-3.0 license implications?
  → Herdr is AGPL-3.0. Modifications must be open-sourced under same. Pure use is fine.
  → Zen's bundle has no LICENSE but README permits adaptation.

Do you want zero dependencies?
  → Herdr: single Rust binary, no deps.
  → Zen: requires jq + tmux + zsh + Claude Code installed.
```

### The compose pattern (Herdr-inside-tmux)

Herdr's README confirms: *"works inside tmux."* This enables a third option:

- **Outer:** tmux + Zen's `t()` launcher + Zen's `/smell` for code review
- **Inner:** Herdr pane(s) for agent-state sidebar + socket-API orchestration

**Tradeoff** (per Hal's video): you lose Herdr's own detach/reattach in this compose mode — you'd detach at the tmux layer instead. Acceptable for most workflows since tmux's detach is more battle-tested anyway.

### Three patterns extractable from Herdr regardless of adoption

Even without adopting Herdr, three primitives transfer to any tmux + scripts setup:

1. **Worktree naming convention** (from Herdr's AGENTS.md): `../<project>-worktrees/<task-slug>` for task worktrees, `issue/<id>-<slug>` for branches, fast-forward shared checkout from task branch before pushing.
2. **Environment gate clause** (from Herdr's SKILL.md): every skill checks an env var before acting. Adaptable to `CLAUDE_CODE_EFFORT_LEVEL`, `HERMES_KANBAN_WORKSPACE`, etc.
3. **Anti-stale-id discipline** (from Herdr's SKILL.md): skills must say "re-read ids; do not guess durability." Adapt to any symbolic identifier (PR numbers, issue refs, branch names).

### Default recommendation

**Tmux-comfortable practitioners:** stay with tmux + adopt Zen's setup; add Herdr only if specific gaps emerge (sidebar agent-state visibility OR cross-pane synchronization via socket API). Don't switch wholesale.

**New practitioners with no tmux investment:** start with Herdr (5-min install) for lower friction. Add Zen's `/smell` standalone (single file copy) for catalog-driven code review.

**Anyone with a real multi-agent orchestration need** (3+ agents collaborating): Herdr's `wait agent-status done` primitive is unique and worth the AGPL-3.0 cost.

---

## Pilot-readiness

**Tier-A pilotable in ~5 minutes:**

```bash
curl -fsSL https://herdr.dev/install.sh | sh
herdr
herdr integration install claude  # for richer agent state forwarding
```

Plus drop the SKILL.md into your skills folder so your agent knows the Herdr CLI vocabulary.

**Lowest-friction pilot in the individual-scale layer**, beating Zen's ~1h setup. But also lower validation depth — the 5-min ride doesn't validate license suitability, state-sync stability with your specific Claude Code version (Hal's recording surfaced bugs), or whether `wait agent-status done` works as advertised end-to-end.

**Pilot constraints to verify:**

1. **License (AGPL-3.0)** — block at any employer with copyleft prohibition for modified-and-redistributed software. Pure use is fine.
2. **OS** — Mac/Linux only. Windows = WSL only.
3. **State sync stability** — Hal's recording showed Cloud Code statuses didn't match; verify in your environment.
4. **Maturity vs alternatives** — viewer comments name 7+ competitors (cmux, agent-deck, Workmux, Conductor, T3 Code, Agent of Empires, Claude `/remote-control`). Worth a comparison sweep before deep adoption.

---

## Cross-corpus signals (Storm Bear mention only)

- **Pattern #18 Layer 2** — Herdr is a candidate for a new sub-archetype: **terminal-multiplexer-as-agent-substrate-with-socket-API**. Distinct from runtime-API-proxy / install-time-skill-translator / plugin-bridge / 3rd-party-orchestrator-wrapping-CLIs (4 prior sub-archetypes). The unique slot is "substrate publishing socket API for cross-pane semantic coordination."
- **Pattern #76 Adversarial Subagent Review Architecture** — Herdr enables but does not prescribe. The `wait agent-status done` recipe is the cross-pane sync primitive adversarial review needs.
- **Skill-files-as-engineering-artifacts** — strengthens to N=2 (Zen `/smell` + Herdr SKILL.md). If a 3rd lands, becomes top-level candidate at Storm Bear next mini-audit.
- **Agent-multiplexer category emergence** — 7+ competing products surfaced in comments. Worth registering as observation-track candidate at v66.
- **Pi project adjacency** — Pi is the first agent in Herdr's supported list + `.pi/prompts/` exists in repo. Worth separate ingest at some point.

---

## Gaps / unverified claims

1. **State sync stability for Cloud Code** — Hal demoed bug live. Verify before relying on the sidebar in production.
2. **`wait agent-status` end-to-end behavior** — documented in SKILL.md but not empirically piloted in autopilot wiki.
3. **The 7+ alternative agent multiplexers** (cmux, agent-deck, Workmux, Conductor, T3 Code, Agent of Empires, getlemonadedotdev) — none ingested. Comparison sweep would close this.
4. **Pi project relationship to Herdr** — first in supported list, `.pi/prompts/pre-release-audit.md` in repo, but actual relationship unclear.
5. **Herdr's reaction to `claude -p` headless mode** — Zen's bundle uses `CLAUDE_CODE_EFFORT_LEVEL` env var; would the agent-detection still work if Claude is invoked non-interactively? Unverified.

---

## Cross-references

- [[personal-repo-zen-mixed-effort-parallel]] — primary comparison target (tmux config + scripts vs Herdr standalone product)
- [[personal-repo-overview]] — individual-scale layer anchor
- [[personal-repo-patterns]] — 12 individual-scale techniques (sub-agents pattern is adjacent)
- [[personal-repo-hermes-orchestrator]] — Hermes is in Herdr's supported agents; composable
- [[personal-repo-router-multimodel]] — orthogonal layer (in-process model routing vs process-level terminal multiplexer)
- [[hermes-goal-mechanics]] — `/goal` is a controller; Herdr is a substrate. Composable.
- [[anthropic-large-codebases-anchor]] — Anthropic's 7-component decomposition; Herdr's SKILL.md is a textbook example of the skill primitive
- External: [[external|claudekit/_index]] — claudekit's framework approach vs Herdr's standalone-product approach (different solutions to similar problem)
- External: Herdr socket API docs — https://herdr.dev/docs/socket-api/ (not yet ingested)
- External: Pi project — https://pi.dev (first in Herdr's supported list; adjacent project worth separate audit)
