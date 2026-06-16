# Source Provenance & Verification Record

> Per librarian rules (NEVER fabricate; surface conflicts). This records exactly what is confirmed vs uncertain about the source video, so future readers don't over-trust it.
> Verification run: Workflow `wf_41be86b6-587` (2026-06-15) — 6 source-finding agents + 6 adversarial verifiers — cross-checked against the bundled `claude-api` skill (authoritative, first-party).

## The artifact I actually have

- **Video:** `https://www.youtube.com/watch?v=y6hvZGpwf7E` — title "Giảm 90% Chi Phí Claude API | Prompt Caching, Tool Search & Advisor Demo Thực Tế - Puneet Shah", channel **BizMate AI Official** (third-party re-uploader), Vietnamese auto-subs, 26:37, uploaded 2026-06-09, 144 views.
- **Transcript:** downloaded via `yt-dlp` (Vietnamese track), deduplicated → `raw/2026-06-15-claude-api-cost-90pct-puneet-shah.md`. Internally a coherent, single-speaker 26-min conference talk.
- **Self-introduction in the transcript:** speaker is "a Product Manager on the Platform team at Anthropic" who "shipped the 1M-token context window, FastMode, and prompt-caching improvements," opening "the final session of Code with Claude in London," bringing CTO "Ben" on stage for the HeroCorp demo.

## Verdicts

### Confirmed first-party (the knowledge is real)
Every technique was verified against Anthropic's first-party docs and the bundled `claude-api` skill:
- Prompt caching: ~90% off cached reads (0.1×), writes 1.25×/2×, timestamp-in-system-prompt invalidation, console analytics — **confirmed.**
- Tool Search (`tool_search_tool_bm25_20251119` / `_regex_20251119`, `defer_loading`) — **confirmed GA.**
- Programmatic Tool Calling (`code_execution_20260120` + `allowed_callers`) — **confirmed GA.**
- Compaction (`compact-2026-01-12`, default trigger ~150K configurable, 1M window) — **confirmed beta.**
- Advisor tool (`advisor_20260301`, beta `advisor-tool-2026-03-01`) — **confirmed.** ~85% cost cut corroborated via InfoQ Code with Claude coverage.
- Event: Code with Claude London, May 19–20 2026 — **confirmed** (`claude.com/code-with-claude/london`).
- Current pricing (Opus 4.8 $5/$25, Sonnet 4.6 $3/$15, Haiku 4.5 $1/$5) — **confirmed.**

### Speaker anecdote — NOT independently published (treat as illustrative, not citable)
Named-customer claims: Replit/Cursor/Perplexity/Claude Code 90%+ cache hit; **Lovable** ~10% token cut via tool search; **Quora** programmatic tool calling on HTML; **Hex** compaction; **Bolt** advisor strategy. Plausible and consistent, but no public case study was found. The exact "+11% / −24%" programmatic-tool-calling benchmark figures were **unverifiable** in first-party text (feature + direction are real).

### Genuine uncertainties (flagged, not resolved)
- **Original video URL not located.** Research agents could not find the original English recording on Anthropic's official YouTube/playlist. The re-upload is the only copy in hand. *(Absence of a found URL ≠ proof it doesn't exist; Code-with-Claude sessions are numerous and poorly indexed by web search.)*
- **Speaker spelling.** Video says "Puneet Shah"; a confirmed Anthropic PM is "**Punit** Shah" (joined ~Apr 2025). Likely the same person (transliteration), unconfirmed.
- **Session listing.** One agent asserted Punit Shah's actual keynote "covered developer capabilities, not cost" and could not place this exact session in London listings — uncorroborated, and contradicted by the transcript's own content.

### Corrected an agent overreach (don't propagate)
A verifier labeled the **HeroCorp demo "fabricated"** because it found no web corroboration. **This is wrong:** the HeroCorp demo is explicitly present in the transcript I downloaded. HeroCorp is simply a *fictional demo company* used as the talk's running example (normal for a conference demo) — not evidence the talk is fake. Likewise an agent "refuted" the regex tool-search variant using a third-party clone repo as evidence; the `claude-api` skill (authoritative) lists it as real, so the skill wins.

## Net assessment

**High confidence this is a genuine Anthropic "Code with Claude" London Platform-team talk, re-uploaded with Vietnamese subtitles by a third party.** The content is too technically precise — correct beta headers, current pricing, the day-before cache-miss-reasons launch, the advisor tool's exact behavior — to be a content-farm fabrication. **Use the knowledge freely; cite Anthropic's first-party docs (not the re-upload) as the authoritative source; treat customer numbers as illustrative.**

Related: [[_index]].
