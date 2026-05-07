# Cluster 1 — User-facing docs (README + tagline)

## Repo metadata

- **URL:** github.com/Alishahryar1/free-claude-code
- **Tagline (verbatim, ≤15 words):** "Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw"
- **Stars:** 22,100 / **Forks:** 3,200 / **Watchers:** 129 / **Open Issues:** 63 / **Commits:** 569 / **Releases:** none published
- **Language:** Python 100%
- **License:** MIT
- **Author:** Alishahryar1 (individual GitHub user)
- **Top-level files:** README.md / CLAUDE.md / AGENTS.md / PLAN.md / LICENSE / pyproject.toml / uv.lock / server.py / .env.example / .python-version / cc-model-picker.png / pic.png
- **Top-level dirs:** api/ / cli/ / core/ / messaging/ / providers/ / config/ / smoke/ / tests/ / .github/

## Verbatim positioning summary

Project = "drop-in proxy for Claude Code's Anthropic API calls" — protocol-compatible bridge between Claude Code clients (CLI / VS Code / JetBrains ACP / chat bots) and 6 alternative model backends (NVIDIA NIM / OpenRouter / DeepSeek / LM Studio / llama.cpp / Ollama).

## Core feature claims

1. **Drop-in proxy compatibility** — set `ANTHROPIC_BASE_URL=http://localhost:8082` + `ANTHROPIC_AUTH_TOKEN=...`, Claude Code talks to local proxy that translates to upstream provider API.
2. **Per-model routing** — Opus / Sonnet / Haiku tiers can each route to different providers (corpus-distinctive sub-variant of Pattern #28 multi-provider).
3. **6 backend providers** — split across cloud (NVIDIA NIM / OpenRouter / DeepSeek) and local (LM Studio / llama.cpp / Ollama).
4. **Native model picker integration** — works with Claude Code's built-in model selector (image asset `cc-model-picker.png` shipped in repo).
5. **Streaming + tool-use support** — preserves Claude Code's agent capabilities (tool calls / streaming responses).
6. **Optional Discord/Telegram bot integration** — remote coding sessions via chat platform.
7. **Voice transcription** — Whisper integration for voice-to-text input.

## Models referenced (verbatim partial)

Claude Code (Anthropic native) / GLM-4.7 / GLM-5 / Kimi K2.5 / MiniMax M2.5 — all explicitly named.

## Cluster-level corpus-first observations

| # | Observation | Cross-wiki implication |
|---|---|---|
| 1 | **Tagline cites OpenClaw via positive-parallel** ("...like OpenClaw") | **Pattern #57 57c forward-citation NEW polarity sub-variant** (positive-comparison-parallel; sister to v57+v58 anti-pattern-foil) |
| 2 | API-protocol-translation-proxy at T4 — Anthropic API → 6 different upstream API protocols (OpenAI-compatible / Ollama native / llama.cpp HTTP) | **CORPUS-FIRST T4 archetype expansion (#9 T4 entrant)** |
| 3 | Per-model-tier routing (Opus → provider A / Sonnet → provider B / Haiku → provider C) | **Pattern #28 multi-provider-with-per-tier-routing sub-variant** |
| 4 | 6 backends (3 cloud + 3 local) — broad coverage of Claude-Code-compatible inference | Pattern #28 6th data point at provider-count=6 |
| 5 | Voice transcription as ancillary feature (not core path) | Pattern #2 Distribution Surfaces — Discord/Telegram + voice = chat-platform-native client surface |
| 6 | LICENSE present + permissive (MIT) | Counter-evidence for Pattern #29 absent-LICENSE; counter-evidence for Pattern #45 dual-licensing extension at v60 |
| 7 | NO releases published despite 22.1K stars + 569 commits | Solo-community release-discipline observation; possible Pattern #19 archetype-1 sub-observation |
| 8 | NO Karpathy / Lam / Cherny / SDD / TDD / agentic-engineering methodology citation | Pattern #19 archetype-4 first-mover-no-lineage variant (echo of v59 AutoGPT — but free-claude-code is utility tool, not paradigm-foundational) |

## Notable absences (counter-evidence)

- ❌ No anti-vibe rhetoric (no "real engineering — not vibe coding" framing as v57 mattpocock or v58 OpenSpec) — **Pattern #51 NEUTRAL at v60**
- ❌ No methodology lineage (Karpathy / Cherny / Lam / SDD / TDD)
- ❌ No dual-license / non-OSI / PolyForm — Pattern #45 + #72 NOT extended at v60
- ❌ No Agent Protocol — uses Anthropic Messages API exclusively (counter-evidence for Pattern #18 Agent Protocol axis at v59 AutoGPT N=1)
- ❌ No EXTREME-tier primitive count — 5-6 module domains = YELLOW, NOT EXTREME (Pattern #69 N=7 holds)
- ❌ No bidirectional MCP at this T4 (free-claude-code consumes Anthropic protocol, doesn't expose MCP server)

## Verbatim short quotes (≤15 words each, in quotation marks)

> "Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw"

(Tagline; positions free-claude-code by parallel to OpenClaw runtime standard.)
