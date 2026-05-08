# Cluster 1 — User-facing docs

> **Sources:** README.md + 7 slash command descriptions + installation steps + FAQ + configuration.
> **Wiki:** codex-plugin-cc v62.

---

## 1. Verbatim positioning / tagline

> *"Use Codex from Claude Code to review code or delegate tasks."*

> `/codex:adversarial-review` = *"a steerable challenge review"* that *"pressure-tests assumptions, tradeoffs, failure modes, and whether a different approach would have been safer or simpler"*

## 2. 7 slash command surface

| Command | Purpose | Distinguishing detail |
|---|---|---|
| `/codex:review` | Standard read-only Codex review | Branch comparisons + uncommitted changes |
| `/codex:adversarial-review` | Steerable challenge review | **Reframes existing review function** with adversarial prompt; targets design decisions over implementation; accepts custom focus text + `--base <ref>` |
| `/codex:rescue` | Delegates investigation/fixes/continuation to Codex | Background or foreground mode |
| `/codex:status` | Display running and recent jobs | Background-task management primitive |
| `/codex:result` | Retrieve final output + session IDs | Background-task management primitive |
| `/codex:cancel` | Stop active background tasks | Background-task management primitive |
| `/codex:setup` | Verify installation + authentication | Setup utility |

## 3. Installation surface (Claude Code marketplace native)

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**Observation:** Pattern #59 Claude Code Plugin Marketplace Native at corporate scale. Distinct from prior corporate distribution mechanisms (npm install / shell script / git clone).

## 4. Requirements

- **ChatGPT subscription OR OpenAI API key** — gates access; non-OpenAI users blocked
- **Node.js 18.18+** — runtime requirement
- **Claude Code as host** — plugin requires Claude Code installed

## 5. Configuration model

User-level: `~/.codex/config.toml`
Project-level: `.codex/config.toml` (requires project trust)

Configurable: model selection + reasoning effort levels. Mirrors Codex CLI config schema (interop with existing Codex configurations supported).

## 6. Workflow examples

### Pre-shipping review
```
/codex:review
```
Standard read-only review of uncommitted changes before commit/push.

### Long-running task delegation
```
/codex:rescue --background "fix race condition in worker pool"
/codex:status                    # check progress
/codex:result <session-id>       # retrieve output
```

### Design challenge
```
/codex:adversarial-review --base main "challenge whether this was the right caching and retry design"
```
Adversarial-framed prompt targets design decisions specifically.

## 7. Corpus-first observations

- **CORPUS-FIRST competitor-published plugin for rival platform** — OpenAI publishes FOR Anthropic Claude Code; unprecedented cross-vendor cooperation in corpus
- **CORPUS-FIRST `/codex:adversarial-review` as prompt-framing variant** — counter-evidence to Pattern #76 architectural-primitive scope
- **CORPUS-FIRST background-task primitive** at framework level — `/codex:rescue --background` + `/codex:status` + `/codex:result` + `/codex:cancel` is 4-command background-job lifecycle (prior corpus subjects had implicit background; this is explicit 4-command surface)
- **Corporate-org Claude Code plugin marketplace publication** at OpenAI scale — Pattern #59 was solo (OMC v27, claude-hud v35); now corporate

## 8. Absences (vs prior corpus subjects)

- ❌ NO MCP integration (Codex backend uses local auth + Codex app server, not MCP-mediated)
- ❌ NO OpenClaw / Hermes runtime references
- ❌ NO Karpathy / Bostrom citation
- ❌ NO i18n (EN-only)
- ❌ NO methodology lineage (no SDD / BMM / TDD)
- ❌ NO marketplace beyond Claude Code's plugin marketplace
- ❌ NO AGENTS.md (uses Claude Code CLAUDE.md primitive only)

## 9. Counter-evidence flags

- **Pattern #76 Adversarial Subagent Review Architecture** — codex-plugin-cc adversarial-review = prompt-framing variant NOT separate-role architectural primitive. **Counter-evidence narrowing scope** of Pattern #76 to "adversarial-by-design role separation specifically."
- **Pattern #51 Vibe-Coding Spectrum** — codex-plugin-cc has NO anti-vibe positioning; NEUTRAL professional tool framing. Extends NEUTRAL pole observations beyond commercial-educator T1 archetype.

## 10. Cross-vendor positioning observations

- OpenAI publishes Apache-2.0 plugin for Anthropic Claude Code = corpus-first cross-vendor cooperative direction
- Acknowledges Claude Code as "where the work happens" while positioning Codex as "delegate-to" backend
- ChatGPT subscription requirement = OpenAI revenue capture even when work hosted in Claude Code
- Strategic interpretation: **OpenAI extending presence into Claude Code market** rather than competing on coding-IDE UX

---

## Length / granularity note

README is concise (~150 lines estimated). Per-command behavior detailed at slash-command-doc level. FAQ addresses account-requirement + configuration questions. Workflow-example-driven documentation style (not philosophical positioning). Corporate-pragmatic voice.
