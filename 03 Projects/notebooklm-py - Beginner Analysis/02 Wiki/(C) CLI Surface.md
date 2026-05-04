# (C) CLI Surface

> Entity page — Building block
> Sources: README CLI section + SKILL.md operations matrix
> Format: 13-section canonical

## 1. What is it / Nó là gì

**CLI Surface** = toàn bộ `notebooklm <command>` interface. Click-based command groups chia theo domain: notebook, source, chat, artifact, generate, download, language, profile, auth. Mỗi group có subcommands + flags + `--json` output mode để programmatic consumption.

**Not just thin wrapper around Python API** — CLI có opinionated defaults (e.g., `--wait`, `--all`) + agent-friendly conventions (`--json`, explicit `-n` notebook ID).

## 2. Why it matters / Sao quan trọng

**Three-surface design** của notebooklm-py có CLI là most-used surface for:

- **Shell script automation** — bash pipelines, cron jobs
- **Agent integration** — agents invoke CLI instead of import Python (language-agnostic)
- **Quick tasks** — researcher ad-hoc queries
- **Skill file invocation** — SKILL.md documents CLI patterns, not Python

**Evidence CLI = primary skill surface:** SKILL.md (26 KB) references CLI commands exclusively. Python examples là for "application integration," not daily agent work.

## 3. Architecture

```
CLI Layer (Click, modular per-domain)
├── session (auth, login, status, doctor)
├── notebook (create, list, use, delete, status)
├── source (add, list, fulltext, guide, delete, wait, add-research)
├── artifact (list, wait)
├── generate (audio, video, slide-deck, quiz, flashcards, report, mind-map, infographic, data-table, revise-slide, cinematic-video)
├── download (audio, video, slide-deck, quiz, flashcards, report, mind-map, data-table)
├── chat (ask, history)
├── note (via --save-as-note flag on ask/history)
├── language (list, get, set)
├── profile (list, create, switch, -p)
└── research (status, wait)
```

Mỗi group tương ứng 1 module trong `src/notebooklm/cli/`.

## 4. Universal flags

| Flag | Behavior |
|------|----------|
| `--json` | Structured output for parsing |
| `-n <id>` / `--notebook <id>` | Explicit notebook context |
| `-p <profile>` | One-off profile use |
| `--wait` | Block until task completes |
| `--no-wait` | Fire-and-forget |
| `--timeout <sec>` | Operation timeout (for wait commands) |

## 5. Command group sizes (by operation count)

| Group | Ops | Complexity |
|-------|-----|------------|
| generate | 11 types × variations | **Highest** (audio 4-format × 3-length × lang, video 2-format × 7-style, etc.) |
| download | 8 artifact types × 4+ formats | High |
| source | 9 ops (CRUD + research + wait) | Medium |
| notebook | 5 ops (CRUD + context) | Low |
| chat | 3 ops (ask, history, save-as-note) | Low-medium |
| profile | 4 ops (CRUD + switch) | Low |
| auth | 3 ops (login, check, check --test) | Low |
| artifact | 2 ops (list, wait) | Low |
| research | 2 ops (status, wait) | Low |
| language | 3 ops (list, get, set) | Low |

**Total:** ~50 distinct CLI ops.

## 6. CLI examples for common tasks

### Task 1: Create notebook + add sources + ask question
```bash
notebooklm create "Retro Q1 2026"
# Output: notebook_id=abc123...

notebooklm source add "https://retro-transcript.example.com/q1.md" -n abc123 --wait
notebooklm source add ./team-notes.pdf -n abc123 --wait

notebooklm ask "What were the biggest blockers discussed?" -n abc123 --json
# Output: JSON với answer + conversation_id + references
```

### Task 2: Generate podcast from research
```bash
notebooklm generate audio "Focus on action items" -n abc123 --format deep-dive --length long --json --wait
# Output: task_id completed → artifact_id

notebooklm download audio ./retro-podcast.mp3 -n abc123
```

### Task 3: Export multi-format artifacts
```bash
notebooklm generate slide-deck --format presenter -n abc123 --wait
notebooklm download slide-deck ./retro-slides.pptx -n abc123 --format pptx
notebooklm download slide-deck ./retro-slides.pdf -n abc123 --format pdf   # both formats
```

### Task 4: Profile isolation for parallel agents
```bash
# Agent 1 (research assistant)
NOTEBOOKLM_PROFILE=agent-research notebooklm create "Research"
# Uses profile "agent-research" isolated from other agents

# Agent 2 (briefing generator)
NOTEBOOKLM_PROFILE=agent-brief notebooklm create "Briefing"
```

## 7. Output format philosophy

### Default: Human-readable
```
Notebook created: Retro Q1 2026 (abc123de-...)
Source added: Team Notes (def456...)
```

### `--json` flag: Agent-consumable
```json
{"notebook_id": "abc123de-...", "title": "Retro Q1 2026", "created_at": "..."}
{"source_id": "def456...", "title": "Team Notes", "status": "processing"}
```

**AGENTS.md explicitly mandates `--json` for agent use.** Default human-readable = for humans.

## 8. Trade-offs / Limitations

- **Surface complexity** — 50+ CLI ops = learning curve. SKILL.md provides reference but can overwhelm.
- **Rate limit propagation** — CLI doesn't throttle; fails fast on Google limits
- **No built-in retry** — agent must implement retry logic for rate-limited ops
- **Session state file** — `use` command writes context file; parallel agents collide if not using `-n` explicit
- **Windows quirks** — v0.3.1-0.3.2 fixed Windows-specific issues; may still lag Linux/macOS
- **Playwright dependency** — `--browser` install adds chromium (~300 MB)

## 9. Comparison to sibling CLIs

| Sibling | CLI surface | Style |
|---------|-------------|-------|
| **ECC** (Claude Code) | Rich TUI + /slash commands | Interactive |
| **Superpowers** | Skills + subagent delegation | Composed |
| **gstack** | Sprint commands + specialist invocations | Sprint-oriented |
| **GSD** | 83 slash commands | Command-heavy |
| **goclaw** | CLI + API platform | Platform |
| **course** | N/A (curriculum) | — |
| **notebooklm-py** | **50+ ops Click-based** | **Domain-grouped** |

→ **notebooklm-py CLI = most Unix-pure of 7.** Click commands compose via shell pipes, stdin/stdout, exit codes. Similar to `git` or `kubectl` design.

## 10. Common pitfalls

1. **Forgetting `-n <id>`** — CLI relies on context file; parallel agents collide
2. **Missing `--json`** — human output hard to parse, breaks agent workflows
3. **Ignoring `--wait`** — generation tasks async; forgetting wait = downloading before ready
4. **Timeout too short** — audio/video can take 10-45 min; default timeout may be insufficient
5. **Profile switching confusion** — `profile switch` is persistent; `-p` is one-off
6. **`delete` without confirmation** — CLI doesn't confirm by default; agents must honor autonomy rules
7. **Rate limit cascade** — parallel generate ops → all throttled together

## 11. When NOT to use CLI

- **Python-native application** — use Python API for tight integration
- **Long-running streams** — CLI isn't built for streaming (use Python async)
- **Complex conditional logic** — shell scripts get unwieldy; Python cleaner
- **Type safety required** — CLI = strings; Python API = typed

## 12. Storm Bear vault relevance

**CLI is Storm Bear's most likely integration path:**
- Claude Code invokes CLI commands (agent skill pattern)
- Shell scripts chain CLI for batch workflows
- Vault's `llm-wiki-ingest` skill could optionally call CLI to:
  - Create NotebookLM notebook per LLM Wiki project
  - Upload source URLs as sources
  - Generate "Study guide" report as sanity check vs Storm Bear's wiki
  - Generate podcast for team listening

**Potential Storm Bear pipeline:**
```
Repo URL
  → Storm Bear routine builds wiki (existing)
  → notebooklm-py creates mirror notebook with same sources
  → Generate podcast from mirror
  → Team listens on commute, reviews wiki on desk
```

→ **Complementary.** Wiki = written reference; NotebookLM podcast = consumable audio.

## 13. References / Nguồn

- Source: [[(C) README summary]] (CLI section) + [[(C) SKILL summary]] (operations matrix)
- Related entities:
  - [[(C) Python API Architecture]]
  - [[(C) Skill Integration (Claude Code + Codex + OpenClaw)]]
  - [[(C) Web-UI-Exclusive Capabilities]]
- External: `notebooklm --help` for live reference
- Sibling CLI patterns:
  - `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Commands.md` (if exists)
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) 33 Specialized Agents + Commands.md`
