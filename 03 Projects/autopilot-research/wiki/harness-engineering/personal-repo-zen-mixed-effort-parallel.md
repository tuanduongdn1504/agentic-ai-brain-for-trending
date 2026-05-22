# Personal-repo extension — mixed-effort parallel-streams + catalog-driven `/smell` (Zen van Riel)

> **Source:** Zen van Riel — [The Only Agentic Engineer Workflow You Need In 2026](https://www.youtube.com/watch?v=ElYxdpYi4U0), 2026-05-20, 17:10, 3389 views
> **Companion repo:** [AI-Engineer-Skool/zen-agentic-engineer-config](https://github.com/AI-Engineer-Skool/zen-agentic-engineer-config) — 7-file Mac+Claude-Code bundle
> **Raw:** `raw/2026-05-21-zen-van-riel-agentic-engineer-workflow.md`
> **Compiled:** 2026-05-21
> **Status:** N=1 single-source extension to [[personal-repo-overview|individual-scale layer]]. Distinct contributions: (1) **mixed-effort parallel-streams** primitive via `CLAUDE_CODE_EFFORT_LEVEL` env var routed across a 4-pane tmux layout, (2) **catalog-driven `/smell` slash command** as anti-fabrication code-review artifact with 70 explicit IDs across Clean Code + Gang of Four + Python-specific catalogs, (3) **anti-hype 30-60% productivity claim** with scale-dependent honesty, (4) explicit **anti-SDD / anti-BMAD position** (counter-evidence to Storm Bear Pattern #21).

---

## The two load-bearing primitives in one sentence each

1. **Mixed-effort parallel-streams.** A single `t` tmux command opens 4 Claude Code panes in `$PWD`: two at default effort, one at medium (`CLAUDE_CODE_EFFORT_LEVEL=medium`), one at low. The operator routes tasks across panes by required reasoning depth — exploratory long-running plans to default-effort, quick lookups to low.
2. **Catalog-driven `/smell` command.** A 5-step structured code-review slash command with 70 explicit catalog IDs (Clean Code + GoF missing-pattern signals + GoF design smells + Python-specific) and verbatim anti-fabrication rules. Prompts as **engineering artifacts**, not vibes.

Both ship as a complete, installable, ~7-file repo. License: not declared at fetch, README says *"feel free to adapt"*.

---

## Architectural distinction vs prior individual-scale sources

| Axis | [[personal-repo-overview\|Tù Bà Khuỳm + 6 EN sources]] | [[personal-repo-router-multimodel\|howznguyen]] | [[personal-repo-hermes-orchestrator\|Nemanja]] | This (Zen van Riel) |
|---|---|---|---|---|
| Primary primitive | `CLAUDE.md` + sub-agents + worktrees | 3-slot config + router (cross-vendor) | Hermes orchestrator + CLI subprocesses | **`CLAUDE_CODE_EFFORT_LEVEL` env var + tmux** |
| Parallelism style | Sub-agent isolation | Cross-vendor delegation | Cross-CLI subprocess | **Same-vendor mixed-effort fan-out (4 panes)** |
| Code review approach | Adversarial eval, human-in-loop | Phase-handoff via files | Cross-CLI reviewer (Claude reviews Codex) | **Catalog-driven `/smell` deterministic-shape report** |
| Productivity framing | Not quantified | Not quantified | "much better than Ralph loop" (anecdotal) | **Explicit 30-60% claim, anti-5x** |
| Stance on SDD/BMAD | Silent | Silent | Uses `/goal` (= Ralph loop primitive) | **Explicit anti-SDD: "won't survive 6 months"** |
| Operator cognitive ceiling claim | Implicit (≤3 sub-agents typical) | Implicit | Implicit | **Explicit: "my mental capacity is pretty much at four parallel work streams"** |

The mixed-effort primitive is **corpus-first as an explicit env-var-routed configuration with concrete launcher script.** Prior sources mentioned parallelism but not effort-routing as a first-class dimension.

---

## The `t` function — verbatim mechanism

```sh
t() {
  local dir="$PWD"
  local session="cwork-$(basename "$dir")-$$-$(date +%s)"
  local p0 p1 p2 p3
  p0=$(tmux new-session  -d  -s "$session" -c "$dir" -n claude -P -F '#{pane_id}' \
       'claude; exec zsh')
  p1=$(tmux split-window -h -t "$p0" -c "$dir" -e CLAUDE_CODE_EFFORT_LEVEL=medium -P -F '#{pane_id}' \
       'claude; exec zsh')
  p2=$(tmux split-window -v -t "$p0" -c "$dir"                                    -P -F '#{pane_id}' \
       'claude; exec zsh')
  p3=$(tmux split-window -v -t "$p1" -c "$dir" -e CLAUDE_CODE_EFFORT_LEVEL=low    -P -F '#{pane_id}' \
       'claude; exec zsh')
  tmux select-layout -t "$session:0" tiled
  tmux select-pane -t "$p0"
  ...
}
```

Five interesting design choices:

1. **`claude` launched as the pane's argv**, not via `send-keys` — avoids racing with `.zshrc` instant-prompt plugins.
2. **`exec zsh` keeps the pane alive after claude exits** — operator can re-launch in same pane without losing layout.
3. **Per-pane env var injection** via tmux's `-e` flag — clean isolation, no shell-export contamination across panes.
4. **Session naming includes `$$` (PID) + timestamp** — every invocation is a fresh session, no accidental reuse.
5. **Top panes (pane 0, 1) receive NO env var** — implies Claude Code's default effort IS what the video calls "high". Worth empirical verification during pilot.

### Tmux config supporting details

The companion `tmux.conf` adds:
- `pane-border-format " #{pane_index}: #{pane_current_command} "` — visible per-pane label so you don't confuse the 4 Claudes
- Drag-select / double-click / triple-click → clipboard via cross-platform `bin/clip` shim
- 50K-line history, 0-based indexing, mouse on, focus events on
- Green flash-confirm banner for copy operations

---

## The `/smell` command — catalog-driven review as engineering artifact

YAML frontmatter (verbatim):
```yaml
description: Scan git diff vs target branch for code smells (Clean Code + GoF + Python catalog)
argument-hint: "[target-branch]"
allowed-tools: Bash(git:*), Read, Grep, Glob
```

5-step contract enforced in the body:

| Step | Purpose | Discipline |
|---|---|---|
| 1. Ingest | Collect both committed (`base...HEAD`) and working-tree diffs with `-U10` context via inline `!`bash``. Auto-detects base branch; errors if not found. | Bash-embedded — no LLM step needed |
| 2. Classify | Pick exactly one of `feature` / `refactor` / `bugfix` / `test` / `docs` / `config` / `mixed`. One-sentence justification. | Forced single-choice |
| 3. Weight lens | Decide Clean Code vs Gang of Four vs Mixed. Inline heuristic provided. | Forced lens selection |
| 4. Analyze | Walk every hunk. Each finding cites EXACTLY ONE catalog ID. Quote smallest excerpt + one-sentence *why* + one-sentence *fix*. | Per-finding format enforced |
| 5. Prioritize & report | Severity ladder BLOCKER / HIGH / MEDIUM / LOW / NIT. Strict markdown report template. Empty case handled. | Per-report format enforced |

**70 catalog IDs total:**

| Catalog | Count | Examples |
|---|---|---|
| Clean Code | 29 | `CC.G5` (Duplication), `CC.F1` (Too Many Args), `CC.N1` (Descriptive Names), `CC.T5` (Boundary Tests) |
| GoF missing-pattern signals | 10 | `GOF.STRATEGY-MISSING`, `GOF.FACTORY-MISSING`, `GOF.OBSERVER-MISSING` |
| GoF design smells (Martin) | 7 | `DS.RIGIDITY`, `DS.FRAGILITY`, `DS.NEEDLESS-COMPLEXITY` |
| Python-specific | 24 | `PY.MUTABLE-DEFAULT` (B006), `PY.BARE-EXCEPT` (E722), `PY.SHELL-TRUE` (S602) |

Python IDs explicitly cross-map to ruff / flake8 / bandit codes in parentheses — legible to existing linter tooling.

**Anti-fabrication discipline (verbatim):**
> "Do not skip any. Do not invent findings. Cite catalog IDs verbatim from the lists below."
> "Don't invent IDs that aren't in this list."

This pattern — **prompts as engineering artifacts** with explicit catalogs and anti-fabrication rules — is structurally distinct from both:
- Viral senior-engineer-persona prompts ("you are a senior engineer, code and do not make any mistakes")
- Free-form SDD prompts that emit unstructured planning

It is also distinct from a [[personal-repo-hermes-orchestrator|cross-CLI adversarial review]] — `/smell` is **deterministic-shape single-pass review by the same Claude**, not cross-vendor adversarial. Both can compose: one Claude pane runs `/smell`, another reviews the report.

### Independent practitioner refinement (from comments)

`@priitraag` proposes a **pre-write + post-write guardrails sandwich:** inject smell patterns BEFORE Claude writes code AND check compliance after. The video only shows the post-write half. This is a free pattern refinement worth empirical testing if anyone pilots Zen's setup.

---

## Mapping to [[core-claims|harness-engineering core claims]]

| Lopopolo claim | This source's evidence |
|---|---|
| #1 Humans steer, agents execute | **Strengthens** — operator runs `t`, types prompts, decides routing across 4 panes |
| #2 Pre-merge review is wasted | **Mixed** — `/smell` is pre-merge review, but is an agent-pre-merge-review not human-pre-merge — same reinterpretation as [[personal-repo-hermes-orchestrator]] |
| #4 Throughput scales with parallel agents | **Bounded-affirms** — explicit ceiling at ~4 panes ("my mental capacity is pretty much at four parallel work streams") |
| #6 Skills > prompts | **Strengthens** — `/smell` is a structured slash command, not a prompt; explicit anti-"60K-star prompt repo" position |
| #7 Adversarial evaluation | **Adjacent** — `/smell` is deterministic-shape catalog-driven review, not adversarial-agent review |
| #8 Ralph loop primitive | **Silent** — no Ralph loop, no `/goal`, no loop construct at all |

Net assessment: 4 strengthening / 1 mixed / 1 silent / 1 adjacent. Strongly consistent with the individual-scale layer's anti-vibe direction.

---

## Productivity claim and scale-honesty (load-bearing for corpus-level signal)

| Scale | Author's claim |
|---|---|
| Freelance / MVP / POC | "god developer" feeling possible; minimal accountability |
| Startup | AI code must be reviewed (mix manual + AI); 10K lines/day = trouble |
| Enterprise | Stricter; same warning |

**Productivity:** *"30 to 60% performance gains"*, NOT 5x. With pragmatic acknowledgement of spike cases (one-off scripts in production).

**Cross-link warning:** this **directly contradicts the framing** of [[external|10x-claude-code/_index]] (the autopilot wiki topic). Worth a cross-topic note: 30-60% is the median; 10x is the spike-case. Both can be true at different scales of the same workflow.

---

## Pattern Library signal (cross-vault mention only — Storm Bear writes deferred)

- **Pattern #51 anti-vibe-pole** — STRONG evidence. Multi-axis: "AI native engineer not vibe coder" + "30-60% not 5x" + anti-prompt-repo positioning + anti-SDD claim
- **Pattern #21 SDD Methodology Emergence** — COUNTER-EVIDENCE. *"specdriven development... gimmicks that don't really stand the test of time"* + comment N=2 corroboration. Worth flagging for next Storm Bear mini-audit (v66 cadence).
- **Candidate: prompt-as-engineering-artifact** — catalog-driven, anti-fabrication, deterministic-shape output. Distinct from vibe-prompt and SDD-plan. Observation-track candidate if a second corpus instance lands.
- **Pattern #18 Layer 2** — adjacent; the multi-pane mixed-effort setup is a same-vendor parallelism mechanism, not cross-vendor. Probably not a sub-archetype, but worth noting that it's a 5th parallelism mechanism in the corpus alongside [[personal-repo-router-multimodel|router-mediated]], [[personal-repo-hermes-orchestrator|orchestrator-mediated]], plugin-bridge (Storm Bear v62), and same-vendor sub-agents (existing in [[personal-repo-patterns]]).

---

## Gaps / unverified claims

1. **Empirical verification of "high == default":** the video says top panes are "high effort" but config sets no env var. Trivial to verify during pilot — observe Claude Code's reported effort level in a pane with no env var set.
2. **`CLAUDE_CODE_EFFORT_LEVEL` env var documentation:** the var name is used in the config but not documented in canonical Claude Code docs (last checked 2026-05-21). Likely supported but uncertain. Pilot would confirm.
3. **/smell command coverage:** 70 IDs is large but not exhaustive. No JavaScript/TypeScript/Rust IDs. Cross-language pilot would surface gaps.
4. **Anti-fabrication efficacy:** does "Don't invent IDs" actually prevent fabrication, or does the LLM cite IDs that don't match the cited code? Pilot needed.
5. **No corroborating source on Zen's specific setup yet** in autopilot wiki. This is the first ingest. The longer explainer video `LxP6qv8ep2o` referenced in the repo README is a follow-up ingest candidate.
6. **License unclear:** README says "feel free to adapt" but no LICENSE file. If adopting components in a real project, clarify.

---

## Pilot-readiness

**Tier-A operationally pilotable.** Setup is `./install.sh && exec zsh` on Mac. Repo is small (7 files, all readable). Catalog IDs in `/smell` are self-documenting. Mixed-effort routing requires no API changes — just env var.

Realistic pilot time: **30 min install + ~30 min `/smell` calibration test** on a real repo. Total ~1 hour to validate or reject.

Compared to [[personal-repo-hermes-orchestrator|the Hermes orchestrator pilot]] (~2h, with billing footguns) and [[personal-repo-router-multimodel|router-multimodel pilot]] (~1h, requires 9Router account), Zen's setup is the **lowest-risk pilot in the individual-scale layer**.

### Installer mechanics (verified 2026-05-21 against the full repo audit)

The install.sh is genuinely one-command but has two pre-conditions worth checking before the pilot:

1. **`jq` must be installed** (`brew install jq` on macOS). The installer warns + skips the settings.json merge step if missing — at which point the statusline and `/smell` slash command would NOT be wired into Claude Code.
2. **Repo MUST be cloned to `~/src/agentic-config`** (hard-coded in `REPO=` inside install.sh). Cloning elsewhere requires editing the constant manually.

The installer is otherwise well-engineered:
- **Idempotent** — already-linked detection on every symlink step
- **Backed-up** — existing `~/.tmux.conf` and `~/.claude/settings.json` get timestamped `.bak` copies before overwrite
- **`jq`-merged settings.json** — preserves existing top-level keys via `// {}` defaulting; only the `SessionStart` and `Stop` hook arrays get **replaced** (not appended). If you have existing hooks on those events, diff the result.

### What the statusline exposes (load-bearing corpus signal)

The statusline.sh script documents in code comments that **Claude Code v2.0.65+ provides authoritative `.context_window` data in statusLine JSON input**: `used_percentage`, `total_input_tokens`, `total_output_tokens`, `context_window_size`. This is **a piece of Claude Code API documentation surfaced through a community config** — not yet in the public Anthropic Claude Code docs as of 2026-05-21 fetch. Any future autopilot wiki article on Claude Code statusLine customization or hooks should reference this.

The script also implements **worktree visual indication** (`+wt:<name>` suffix on the branch segment when `git-dir != git-common-dir`) — concrete UX support for the worktree pattern with zero additional tooling.

### Reusable patterns extractable from the bundle independently

Three pieces of the bundle are useful in isolation, without adopting the full setup:

1. **`/smell` slash command** — drop `smell.md` into your own `~/.claude/commands/` and run it on any PR diff. The 70-ID catalog is self-contained.
2. **SessionStart/Stop hook pair for sidecar daemons** — `statusline-daemon.sh` is a clean template for any background process that should live for the duration of a Claude Code session.
3. **`bin/clip` cross-platform clipboard shim** — 17 lines, no dependencies beyond the system clipboard tool. Reusable in any tmux config.

---

## Cross-references

- [[personal-repo-overview]] — individual-scale layer anchor
- [[personal-repo-patterns]] — 12 individual-scale techniques (sub-agent technique is closest cousin to mixed-effort parallel-streams)
- [[personal-repo-router-multimodel]] — cross-vendor router-mediated parallelism (orthogonal axis: cross-vendor vs same-vendor)
- [[personal-repo-hermes-orchestrator]] — cross-vendor orchestrator-mediated parallelism (also orthogonal)
- [[personal-repo-vs-org-scale]] — Lopopolo axis-by-axis comparison
- [[hermes-goal-mechanics]] — `/goal` mechanics (Zen's position: SDD-style is "gimmick that won't survive 6 months"; explicit tension with `/goal` as primitive)
- [[anthropic-large-codebases-anchor]] — Anthropic's 7-component decomposition; Zen's `/smell` is a `commands/`-folder example of Anthropic's commands primitive
- External: [[external|claude-md-12-rules/_index]] — Mnilax behavioral contract; `/smell` is a deployable example of Mnilax-style discipline
- External: [[external|claudekit/_index]] — middle-rung framework; Zen is the "scripts not framework" alternative on the same axis
- External: [[external|10x-claude-code/_index]] — direct counter-claim ("30-60% not 5x"); worth a cross-topic synthesis note at next audit
