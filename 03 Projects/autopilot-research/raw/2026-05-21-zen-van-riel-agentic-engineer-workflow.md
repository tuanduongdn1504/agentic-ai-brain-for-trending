---
source: yt-dlp-only + 3-webfetch
path: 5-yt-dlp + 3-webfetch
urls:
  - https://www.youtube.com/watch?v=ElYxdpYi4U0
  - https://github.com/AI-Engineer-Skool/zen-agentic-engineer-config
video_id: ElYxdpYi4U0
title: "The Only Agentic Engineer Workflow You Need In 2026"
channel: Zen van Riel
channel_id: "@zenvanriel"
duration: 17:10
uploaded: 2026-05-20
views: 3389
fetched: 2026-05-21
language: en
companion_repo: AI-Engineer-Skool/zen-agentic-engineer-config (Mac + Claude Code; tmux + zsh helpers + statusline + slash commands)
companion_links:
  - explainer_video_referenced_in_readme: https://youtu.be/LxP6qv8ep2o (DIFFERENT video — likely the longer original walkthrough; not yet ingested)
  - lead_gen_landing: https://zenvanriel.com/ai-coding (email-gated config bundle; not pursued)
notes: |
  Single-video ingest combined with full companion-repo audit (7 files,
  all small) discovered via author's comment reply on the video.
  Companion repo is public, MIT-license-style "feel free to adapt" copy
  in README, no explicit license file at fetch time.

  Strong anti-hype, anti-SDD positioning. Concrete primitives include:
  - 4-pane tmux layout with mixed effort levels via
    CLAUDE_CODE_EFFORT_LEVEL env var
  - /smell slash command with 5-step structured review + explicit
    catalog IDs (Clean Code + Gang of Four + Python-specific)
  - 30-60% productivity claim (NOT 5x)

  Cross-pattern signal worth flagging for Storm Bear (mentioned only,
  no Storm Bear writes from this scope):
  - Pattern #51 anti-vibe-pole STRONG evidence ("AI native engineer
    not vibe coder" + "30-60% not 5x" + "anti-prompt-repo-with-60K-stars")
  - Pattern #21 SDD Methodology Emergence — counter-evidence
    ("specdriven development... gimmicks that don't really stand the
    test of time")
  - Candidate: prompt-as-engineering-artifact (catalog-driven /smell)
    distinct from vibes-prompts
---

# The Only Agentic Engineer Workflow You Need In 2026 — combined transcript + companion repo

> **Video:** [YouTube ElYxdpYi4U0](https://www.youtube.com/watch?v=ElYxdpYi4U0) — Zen van Riel, 17:10, uploaded 2026-05-20, 3389 views at fetch
> **Companion repo:** [github.com/AI-Engineer-Skool/zen-agentic-engineer-config](https://github.com/AI-Engineer-Skool/zen-agentic-engineer-config) (7 files)
> **Fetched:** 2026-05-21 via `yt-dlp --write-auto-subs` + curl + GitHub API recursive tree
> **Compile target:** `wiki/harness-engineering/personal-repo-zen-mixed-effort-parallel.md` (new 7th individual-scale sibling)

---

## Part 1 — Video synthesis

### Topline thesis

> "I've shipped AI code on real engineering teams across enterprises and startups with code reviews, production users, and full accountability for everything that I merge."

The video positions itself against the "vibe coder" / "5x productivity" mainstream. Core framing: **agentic engineering as a mindset of accountability, not a tool stack.** The contrast is explicit at multiple points and reinforced by viewer comments (e.g., @maximillian000: *"One of the few sane youtubers talking about agentic coding"*).

### The 4-pane parallel setup (the load-bearing primitive)

A tmux launcher `t` opens 4 Claude Code panes simultaneously in the current directory:

| Pane | Position | Effort level (as described in video) | Effort level (actual config) |
|---|---|---|---|
| 0 | top-left | "high effort" | default (`CLAUDE_CODE_EFFORT_LEVEL` unset) |
| 1 | top-right | "high effort" | default (`CLAUDE_CODE_EFFORT_LEVEL` unset) |
| 2 | bottom-left | "medium" | `CLAUDE_CODE_EFFORT_LEVEL=medium` |
| 3 | bottom-right | "low" | `CLAUDE_CODE_EFFORT_LEVEL=low` |

**Discrepancy worth noting:** the video calls the top panes "high effort", but the shell config sets no env var on them (= "default"). Either default == high in Claude Code's current behavior, or the video simplifies the terminology. Worth verifying empirically during any pilot.

Allocation heuristic (verbatim):
- Top panes (high/default): exploratory, long-running, creative — e.g., *"scope out five potential features we can work on"*
- Bottom-right (low): quick lookups — e.g., *"explore the codebase to tell me which languages are used"* (returns Java/Python/HTML/SQL faster than the high-effort plan session)
- Bottom-left (medium): everything in between

Reasoning for choosing 4 (verbatim):
> "very often there's an opportunity to parallelize some work with AI code, but not too much. I'm not going to pretend like I'm running 50 agents at the same time. My mental capacity is pretty much at four parallel work streams."

### Context window drift management

- Status line shows current context window % (bottom-right corner of each pane)
- `/compact` to compress in-place vs `/clear` to reset entirely
- No magic rule: *"This is the whole point of being an agentic engineer. You need to just get a feeling for when to compress your context window."*

### Anti-SDD / anti-BMAD / anti-trend stance

Strongly stated at 3:22:

> "lot of these things are just gimmicks that don't really stand the test of time. Just think about all of the different AI projects that have become so popular over the past 3 years. How many of those projects are still relevant today? I'm not saying that things like spec-driven development are a fad, but I do think that anything that does work will just be rolled up into something like Claude Code as time goes by."

> "I'm just awaiting the hype and anything that survives three to four months is probably a really good pattern to apply."

> "you're not going to see anything in this video that won't be relevant anymore in 6 months."

Example given: Claude Code's built-in to-do tracker replaced hand-rolled markdown TODO files.

**Comment corroboration (@elpepelucho, 2♥):** *"thank you for saying what always seem to be obvious, all the workflows and skills packages that are effective will be rolled into future releases of the agent harnesses."*

### The `/smell` command — catalog-driven code review

Position: instead of viral prompts like *"you are a senior engineer, code and do not make any mistakes"* from 60K-star GitHub prompt repos, ground code review in actual engineering books (Clean Code + Gang of Four design patterns).

The full slash command lives at `.claude/commands/smell.md` in the companion repo and is detailed in Part 2.

**Independent practitioner extension (@priitraag comment):**
> "I inject the 'smell' patterns BEFORE letting claude write any code. More specific language guardrails I inject dynamically based on the task/feature in hand. That forces claude to think about the patterns already when setting up a new feature architecture. I have experienced that pre guardrails coupled with later smell/other guardrails compliance check yields the best results."

This proposes a **pre-write + post-write guardrails sandwich** — pattern refinement not in Zen's video.

### AI code review workflow

- Connects GitHub via the `gh` CLI (no MCP needed; Claude Code already authenticated via subprocess inheritance)
- Mentions Anthropic's own Claude Code reviews product + self-rolled Codex-headless pipelines
- **Always combine AI review + human review**
- Has personal pre-PR review commands but **refuses to share them**: *"there is not one command that fits all... depends on the programming language, the complexity of the work, how many human reviewers are in your project, what their preferences are, what the code style is that your team agreed on"*

### MCP vs Bash vs Skills decision tree

| Use | When |
|---|---|
| **Bash** | Simple commands. Common tools the LLM already knows (gh, curl, single Python scripts). |
| **Skills** | Common platforms the LLM knows about — implicit endorsement |
| **MCP** | Unknown internal services / when context-specific backend matters |
| Specific MCP highlights | **Context7** (latest framework docs in efficient cut-up format, vs generic web search) + **Serena** (LSP connection for efficient code search) |

Verbatim heuristic:
> "if you just need to execute a single command, then bash makes a lot of sense"
> "no definitive answer whether you need bash or MCP servers. It just depends on intuition. Intuition that you can only develop when you create interesting systems with these AI agents."

### Scale-dependent honesty (10:32)

| Scale | What AI coding feels like |
|---|---|
| **Freelance / MVP / POC** | "god developer" feeling; little accountability; just ship |
| **Startup** | AI code must be reviewed; partially manual + partially AI |
| **Enterprise** | Stricter still; 10K lines/day → "smaller PRs please" OR "long-term bugs" |

Verbatim warning:
> "if you come to other developers with 10,000 lines of code every single day, I can guarantee you that things aren't going to end very well"

### Git worktrees (12:58)

Concrete demo:
- The 4-pane setup shares git context — switching branch in one pane switches all (footgun)
- Worktrees create isolated copies → independent parallel work streams
- Claude Code can create and delete worktrees on command
- **Important footgun:** dependency reinstall per worktree
- **Solution:** auto-install-deps skill or hook triggered on worktree creation

Verbatim claim:
> "Just knowing how to use a work tree is a big power move."

### Realistic productivity claim — 30-60%, NOT 5x

The single most-quotable line of the video:

> "the people who are doing the best of agent coding aren't screaming from the rooftops that they're five times more productive. They might see 30 to 60% performance gains."

With pragmatic acknowledgement of spike cases:
> "they might be really fast on certain cases like creating one-off scripts to test something in production"

And the engineering-time decomposition:
> "the coding portion of the engineering job is actually not that much anymore. This is not saying that you don't have a job anymore. Engineering is much more than just coding, but it is a shift in how you need to distribute your daily work time."

### Closing: AI native engineer mindset

Frame: vibe coder (pushes 1000s of lines of AI code daily) vs AI native engineer (benefits from productivity AND can fix systems AND masters the full stack).

> "What kind of engineer do you want to be?"

Anecdote: 2-day feature got senior reviewer pushback for missing long-term architectural thinking; author admits skimming the code to ship faster.

---

## Part 2 — Companion repo artifacts (verbatim)

Repo structure (7 files, all small):

```
.claude/commands/smell.md       — the /smell slash command (232 lines)
README.md                       — README + explainer-video link
bin/clip                        — cross-platform clipboard shim (used by tmux)
install.sh                      — installer
shell.zsh                       — t() function + alias cwork=t
statusline-daemon.sh            — status line daemon
statusline.sh                   — status line script (shows context window % + branch)
tmux.conf                       — 4-pane layout config
```

License: no explicit LICENSE file at fetch. README says *"Feel free to adapt to your OS or other AI tool with an AI Agent if you need to."* Tested on Mac + Claude Code only.

### shell.zsh — the `t()` function (verbatim)

```sh
# Prevent Ctrl-S / Ctrl-Q from freezing the terminal
stty -ixon 2>/dev/null

# 4-pane Claude workspace in the current working directory
#   pane 0,1: default effort
#   pane 2:   CLAUDE_CODE_EFFORT_LEVEL=medium
#   pane 3:   CLAUDE_CODE_EFFORT_LEVEL=low
# Each invocation creates a fresh session (unique name per call).
t() {
  local dir="$PWD"
  # Always fresh: unique session name per invocation (basename + timestamp).
  local session="cwork-$(basename "$dir")-$$-$(date +%s)"

  # Launch claude as each pane's argv (not via send-keys) so we don't race
  # against .zshrc sourcing / instant-prompt plugins. `exec zsh` keeps the
  # pane alive with a shell prompt after claude exits.
  # After `select-layout tiled`, panes land as:
  #   index 0 = top-left  (high)
  #   index 1 = top-right (high)
  #   index 2 = bottom-left  (medium)
  #   index 3 = bottom-right (low)
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

  if [ -n "$TMUX" ]; then
    tmux switch-client -t "$session"
  else
    tmux attach -t "$session"
  fi
}

alias cwork=t
```

**Code-level observation: the comment block contradicts the comments at the top.** Lines 4-7 say *"pane 0,1: default effort"* but lines 13-18 say *"index 0 = top-left (high)"*. The actual launches at lines 22-29 show only panes 2 and 3 receive env vars. So **pane 0 and 1 use Claude Code's default effort**, which the author labels "high" in the video — confirming the discrepancy noted above. Worth empirical verification during any pilot.

### .claude/commands/smell.md — the `/smell` command (verbatim, 232 lines, condensed structure here)

YAML frontmatter:
```yaml
description: Scan git diff vs target branch for code smells (Clean Code + GoF + Python catalog)
argument-hint: "[target-branch]"
allowed-tools: Bash(git:*), Read, Grep, Glob
```

**5-step contract** (the entire command is structured as a forced sequence):

1. **Ingest** — Bash-embedded diff collection via `!` inline command. Collects both committed (`base...HEAD`) and working-tree (staged + unstaged) diffs with `-U10` context. Auto-detects base branch via `git symbolic-ref refs/remotes/origin/HEAD` with `origin/main` fallback. Errors out cleanly if base not found.

2. **Classify** — Pick exactly one of: `feature` / `refactor` / `bugfix` / `test` / `docs` / `config` / `mixed`. One-sentence justification required.

3. **Weight the lens** — Decide Clean Code vs Gang of Four vs Mixed. Heuristic provided:
   - New classes/hierarchies/abstractions → GoF lens
   - Inline edits / naming / function shape / duplication → Clean Code lens
   - Both → Mixed

   Plus inline reminders of Clean Code's headline rules and GoF's pattern-missing signals.

4. **Analyze** — Walk every hunk. For each issue: cite exactly ONE catalog ID from the explicit lists. Quote smallest code excerpt. One sentence *why* + one sentence *fix*.

   **Catalogs (verbatim ID counts):**
   - Clean Code: 29 IDs (`CC.C1`–`CC.T9`)
   - Gang of Four missing-pattern signals: 10 IDs (`GOF.STRATEGY-MISSING`–`GOF.FACADE-MISSING`)
   - Gang of Four design smells: 7 IDs (`DS.RIGIDITY`–`DS.OPACITY`)
   - Python-specific: 24 IDs (`PY.MUTABLE-DEFAULT`–`PY.LOG-NO-EXC`)

   Each ID has a 1-line definition. Several Python IDs map to known ruff / flake8 / bandit codes (`B006`, `E722`, `S307`, etc.) — making the cross-reference legible to existing linter tooling.

5. **Prioritize & report** — Severity ladder: BLOCKER / HIGH / MEDIUM / LOW / NIT. Strict markdown report template enforced for the final output. Empty-findings case explicitly handled.

**Anti-fabrication discipline (verbatim):**
> "Do not skip any. Do not invent findings. Cite catalog IDs verbatim from the lists below."
> "Don't invent IDs that aren't in this list."

This is a **load-bearing instance of "prompts as engineering artifacts"** — catalog-driven, anti-fabrication, deterministic-shape output. Stands in clear contrast to viral senior-engineer-persona prompts.

### tmux.conf (verbatim, abridged)

```
# --- core ---
set -g mouse on
set -s set-clipboard on
set -g default-terminal "screen-256color"
setw -g mode-keys vi
set -g history-limit 50000
set -g focus-events on

# --- 0-based indexing ---
set -g base-index 0
setw -g pane-base-index 0

# --- pane border shows pane index + current command (helps identify the 4 claude panes) ---
set -g pane-border-status top
set -g pane-border-format " #{pane_index}: #{pane_current_command} "

# [mouse-drag / double-click / triple-click → clipboard via bin/clip + green confirm banner]
# [smart scroll: WheelDown at bottom exits copy mode]
```

**Notable design choices:**
- Pane border format shows index + current command — visible distinction for the 4 panes
- Clipboard sync via a separate `bin/clip` shim → cross-platform
- 50K history — reasonable for long Claude sessions

### README.md (verbatim)

```
Explainer video: https://youtu.be/LxP6qv8ep2o

My personal simple agentic engineer workflow: tmux + zsh helpers + Claude Code status line + slash commands.
Feel free to adapt to your OS or other AI tool with an AI Agent if you need to ;)

Tested on Mac and Claude Code:

./install.sh && exec zsh
```

The referenced explainer video `LxP6qv8ep2o` is a DIFFERENT YouTube ID than the source for this raw file. Likely the longer original walkthrough. **Not yet ingested** — flagged as follow-up.

### install.sh (verbatim, 105 lines, idempotent)

Bootstrap mechanics in 4 steps:

1. **Symlink `~/.tmux.conf` → repo's `tmux.conf`.** Idempotent (already-linked detection). If a real file exists, backs up to `~/.tmux.conf.bak.<YYYYMMDD-HHMMSS>` before linking.
2. **Append `source ~/src/agentic-config/shell.zsh` to `~/.zshrc`** if not already present (uses `grep -Fq` for idempotency check).
3. **Merge `~/.claude/settings.json`** via `jq` — sets `statusLine` to `statusline.sh` + adds `SessionStart` hook (starts daemon) + `Stop` hook (stops daemon). Backs up existing settings.json before merge. **Requires `jq`** — warns and skips if not installed.
4. **Symlink slash commands** from `.claude/commands/*.md` into `~/.claude/commands/`. Same backup-then-link logic as tmux step.

**Load-bearing path assumption (verbatim):**
```sh
REPO="$HOME/src/agentic-config"
```
Pilot must clone the repo to `~/src/agentic-config` OR edit the constant. Not configurable via env var.

**Settings.json merge payload (verbatim jq expression):**
```sh
jq \
  --arg sl "$REPO/statusline.sh" \
  --arg start "$REPO/statusline-daemon.sh start" \
  --arg stop  "$REPO/statusline-daemon.sh stop" \
  '
  .statusLine = { "type": "command", "command": $sl, "padding": 0 }
  | .hooks = ((.hooks // {})
      | .SessionStart = [{ "hooks": [{ "type": "command", "command": $start }] }]
      | .Stop         = [{ "hooks": [{ "type": "command", "command": $stop  }] }])
  ' "$SETTINGS" >"$tmp"
```

**Notable design choices:**
- ANSI green/yellow output for `say` / `warn` makes the install visually legible
- `set -euo pipefail` — fails loudly on any error
- All scripts `chmod +x`'d at install time
- Final "Next steps" cat heredoc shows `exec zsh` → `tmux source ~/.tmux.conf` → `t` → open Claude Code

**Closing the install loop:** the script outputs:
```
Next steps:
  1. exec zsh                          # reload shell to pick up t/cwork + stty -ixon
  2. tmux source ~/.tmux.conf          # if tmux is already running
  3. t                                 # launch the 4-pane Claude workspace
  4. Open a new Claude Code session    # status bar + /smell command available
```

### statusline.sh (verbatim, 131 lines)

Renders the per-pane status: `<model-slug>  │  <branch>[+wt:<name>]  │  [██████░░░░] <pct>% (<used>k/<max>k)`.

**Three load-bearing details surfaced by the code:**

1. **Claude Code v2.0.65+ exposes `.context_window` in statusLine JSON input** (verbatim comment from the script):
   > "Authoritative context-window data populated by Claude Code (v2.0.65+). used_percentage is precomputed; total_input/output_tokens reflect the current in-context tokens. Both are null/0 until the first API call completes, then populate after every assistant turn. NOTE: current_usage is an OBJECT (input_tokens, output_tokens, cache_*), not a scalar — do NOT try to use it directly in arithmetic."

   This is **a piece of Anthropic Claude Code API documentation surfaced through a community config** — not in the public Claude Code docs as of fetch. Useful for any future statusLine-customizing work in the autopilot wiki.

2. **Default context window assumed at 200000 tokens:**
   ```sh
   ctx_max=$(printf '%s' "$input" | jq -r '.context_window.context_window_size // 200000')
   ```
   Hard-codes the 200K assumption when the field is absent. Worth noting if Anthropic raises the window.

3. **Worktree detection** for the worktree pattern the video promotes:
   ```sh
   gd=$(git -C "$cwd" rev-parse --git-dir 2>/dev/null)
   cd_path=$(git -C "$cwd" rev-parse --git-common-dir 2>/dev/null)
   if [ "$gd" != "$cd_path" ]; then
     wt=$(basename "$gd")
     git_seg="$branch +wt:$wt"
   fi
   ```
   Operator can visually distinguish worktree panes from main-branch panes in the status line. Concrete UX support for the parallel-worktree pattern.

**Cache architecture:**
- 3-second freshness window (`STALE_AFTER=3`)
- Cache file at `~/.claude/.statusline.cache`
- Input file at `~/.claude/.statusline.input`
- Cache valid only if newer than input — invalidates after `/clear` or any new assistant turn
- Cross-platform `stat` (GNU `-c %Y` then BSD `-f %m`)
- 20-char `█░` block via simple percentage math

### statusline-daemon.sh (verbatim, 54 lines)

Background polling daemon (refreshes cache every 2s) managed by Claude Code's `SessionStart` / `Stop` hooks.

**Mechanics:**
- PID file at `~/.claude/.statusline.pid` prevents duplicate daemons (re-runs are no-ops if alive)
- Daemon bypasses the cache fast-path by `rm -f` before calling statusline.sh → forces compute
- Standard `start` / `stop` / `restart` subcommand interface
- Hook stdin read-and-discarded at exit to avoid pipe blocking — small but load-bearing subtlety for Claude Code hook integration

**This is a concrete example of the Claude Code SessionStart/Stop hook pair for sidecar processes** — pattern worth noting independently of the rest of the bundle. Any future autopilot wiki article on Claude Code hooks should cite this.

### bin/clip (verbatim, 17 lines)

Cross-platform clipboard writer with explicit detection order:

```sh
if command -v pbcopy >/dev/null 2>&1; then
  exec pbcopy
elif [ -n "${WAYLAND_DISPLAY:-}" ] && command -v wl-copy >/dev/null 2>&1; then
  exec wl-copy
elif command -v xclip >/dev/null 2>&1; then
  exec xclip -selection clipboard
elif command -v xsel >/dev/null 2>&1; then
  exec xsel --clipboard --input
else
  echo "agentic-config/bin/clip: no clipboard tool found ..." >&2
  cat >/dev/null
  exit 1
fi
```

Order: `pbcopy` (macOS) → `wl-copy` (Wayland) → `xclip` (X11) → `xsel`. Fallback message + drain stdin + exit 1. Trivially adaptable, no Mac-only assumption despite the README claim.

---

## Part 2.5 — Net pilot picture after full repo audit (added 2026-05-21 follow-up)

The 4-file follow-up audit closes the loop on pilot readiness. Concrete observations:

1. **Install is genuinely one-command** — `./install.sh && exec zsh` does what it says. Idempotent, backed up, observable (ANSI status lines).
2. **One hidden dep:** `jq` is required for the settings.json merge. `brew install jq` on macOS. The installer warns and skips that step if missing, so settings.json wouldn't be touched but statusline + slash commands wouldn't work either.
3. **One hidden path assumption:** repo MUST live at `~/src/agentic-config`. Cloning elsewhere requires editing the `REPO=` line in install.sh + manually updating any path in the resulting settings.json.
4. **Settings.json merge is non-destructive** — preserves existing keys via `jq`'s `// {}` defaulting. Backs up before write. Safe to run on an existing Claude Code install with existing hooks (though the SessionStart/Stop hook arrays get REPLACED, not appended — operators with existing hooks should diff the result).
5. **Status line exposes Claude Code v2.0.65+ context-window JSON** — confirms Anthropic added this surface; useful corpus-level intelligence for any future statusLine work.
6. **Worktree visual indicator** (`+wt:<name>` suffix) is real and concrete — supports the worktree pattern from the video without extra tooling.
7. **The SessionStart/Stop hook pair for sidecar daemons** is reusable independently of the rest of the bundle — Claude Code hooks pattern.

**Updated pilot cost estimate:** still ~1 hour, with one tweak — add `brew install jq` to setup if missing (~30s) and `git clone` to exactly `~/src/agentic-config` rather than an arbitrary location.

---

## Part 3 — Comment-thread evidence

14 comments total. Substantive ones:

1. **@priitraag (root):** Pre-write + post-write smell guardrails sandwich (pattern refinement, see Part 1)
2. **@elpepelucho (2♥, root):** *"thank you for saying what always seem to be obvious, all the workflows and skills packages that are effective will be rolled into future releases of the agent harnesses"* — N=2 corroboration on the anti-SDD position
3. **@maximillian000 (1♥, root):** *"One of the few sane youtubers talking about agentic coding"* — anti-hype social signal
4. **@PrivacyProfessionalTraining (root):** *"Real world agentic engineering workflows show that effective AI coding is less about hype and more about structured workflows context management and disciplined software engineering practices"* — N=3 affirmation on anti-vibe position
5. **@GeobotPY → @zenvanriel (OP reply):** Companion repo URL surfaced via this exchange
6. **@nerios.v / @ThePatriotPirate:** Authority-challenges to author; author's responses calm and non-defensive

---

## Part 4 — Cross-corpus signals (autopilot wiki + Storm Bear mention)

### Within autopilot wiki

- **[[harness-engineering/personal-repo-overview]]** + sibling articles — direct sibling, this becomes 7th individual-scale source
- **[[10x-claude-code/_index]]** — direct counter-evidence to "10x" framing
- **[[claude-md-12-rules/_index]]** — Mnilax behavioral contract; this `/smell` is an example of the discipline applied as an artifact
- **[[claudekit/_index]]** — middle-rung framework; Zen's setup is the "scripts not framework" alternative
- **[[workflow-ai-coding/_index]]** — adjacent workflow source

### Storm Bear (mention only; cannot write from this scope)

- **Pattern #51 anti-vibe-pole** — STRONG evidence. Multi-axis: "AI native engineer not vibe coder" + "30-60% not 5x" + anti-prompt-repo positioning + anti-SDD claim
- **Pattern #21 SDD Methodology Emergence** — COUNTER-EVIDENCE. *"specdriven development... gimmicks that don't really stand the test of time"* explicitly. Worth flagging for v66 mini-audit consideration.
- **Pattern #76 Adversarial Subagent Review** — adjacent. `/smell` is review-but-deterministic-not-adversarial; could be a sibling sub-archetype or counter-example to the adversarial framing depending on audit interpretation.
- **Candidate: prompt-as-engineering-artifact** — catalog-driven, anti-fabrication. Distinct from "vibe prompt" and from "spec-driven plan". Worth observation-track if a second corpus instance lands.

---

## Key takeaways

1. **Concrete primitive worth piloting:** 4-pane tmux + mixed-effort layout via `CLAUDE_CODE_EFFORT_LEVEL` env var. Install is one command (`./install.sh && exec zsh`). Mac + Claude Code only as tested.
2. **The `/smell` slash command is the load-bearing engineering artifact** of the bundle. 5-step contract + 70 explicit catalog IDs + anti-fabrication discipline. Reusable independently of the rest of the setup.
3. **Productivity claim is honest:** 30-60%, not 5x. Spike cases possible (one-off scripts), but team workflows don't sustain hype numbers.
4. **Anti-SDD position is strong and independently corroborated by N=2 commenter.** Storm Bear Pattern #21 (SDD Methodology Emergence) has accumulated counter-evidence and should be reviewed at next mini-audit.
5. **Implicit pattern refinement from @priitraag:** pre-write + post-write guardrails sandwich is a sister technique not in Zen's own setup but compatible with it. Worth flagging if seen elsewhere.
6. **Discrepancy to verify empirically:** video says "high effort" for top panes but config sets no env var on them. Whether default == high in current Claude Code is unverified.
7. **Two follow-up ingest candidates:**
   - The explainer video `LxP6qv8ep2o` (longer original walkthrough, referenced in README)
   - The Anthropic Claude Code "code reviews" hosted product (referenced as a workflow option in the AI-review section)
