# (C) PRIMARY — "Agent Session-Transcript Maintenance / Housekeeping" §C standalone N=1 (v165 lazyagent)

**Filed to:** `_patterns/06-library-vocab-registry.md` §C (live standalone candidates) + §F (running log).
**Status:** PROVISIONAL N=1, CORPUS-FIRST. **§28: 1 new standalone ≤ 2 (cap respected).**

## The item
**"Agent Session-Transcript Maintenance / Housekeeping (prune / compact / full-text-search stored agent session files to reclaim disk + rate-limit budget)."**

A tool that performs **file-level maintenance on already-stored AI-coding-agent session/transcript data**:
- **prune** — delete chat files older than N days (dry-run preview + auto-backup);
- **compact** — shrink session files by truncating bulk payloads (reclaim disk + reduce rate-limit/billing impact; lazyagent cites ~80+ MiB/year);
- **search** — full-text search across transcripts with highlighted snippets.

## Why it's a genuine mint (not manufactured)
Applies the **v160 functional-novelty test** (the v158-audit test): *a clean instance of an existing sub-flavor mints nothing (v159 CodexBar / v164 oc-claw); a genuinely new function mints (v160 ping-island).*

- **Genuinely corpus-first function.** Every prior corpus subject that touches agent session data **reads + displays** it (the entire observability sub-archetype v89/v109/v154–v160/v164) or **compresses it pre-LLM at runtime** (v144 headroom). None **manages the stored files** — delete-old / shrink / index-and-search. lazyagent is the first.
- **It's a write/manage function, not display or read-path compression** — a distinct *kind*, not new stack/scale.
- **Precedent for minting on an Nth-in-niche subject:** v158 ai-token-monitor was the 6th-in-niche observability tool and still minted a corpus-first capability standalone (social-leaderboard); the v158 audit **accepted** it as "the legitimate payoff." Same shape here: a clean observability instance + one corpus-first capability.

## Distinction from the nearest neighbor — v144 headroom
| | v144 headroom ("Agent Context-Compression Layer") | v165 lazyagent (this item) |
|---|---|---|
| **Layer** | runtime read-path (intercepts what the agent reads *before* the LLM) | stored files on disk (post-hoc) |
| **Purpose** | save the **context window** (tokens at inference) | reclaim **disk + rate-limit/billing** + searchability |
| **Reversibility** | reversible retrieval (CCR keeps originals) | prune = destructive-with-backup; compact = truncates bulk payloads |
| **Surfaces** | lib / proxy / MCP / CLI / Docker | CLI subcommands of an observability tool |

Different layer, different purpose, different reversibility → not the same kind. Not a headroom strengthening.

## Distinction from the observability sub-archetype
The observability sub-archetype **OBSERVES** (read-only display of state). This item **MANAGES** stored data (deletes / shrinks / searches files). lazyagent is *both* — its core is a clean observability instance (sub-flavor (a), sub-archetype → N=11) AND it ships this maintenance capability. The standalone mints the **capability**, not a re-classification of the subject (the v158 precedent exactly).

## Promotion path
**Promotion-eligible at N=2** (a 2nd tool that does file-level maintenance/housekeeping of stored agent transcripts). Time-aware auto-retire applies (§28.3 / §39: retire only after BOTH ≥15 wikis AND ≥30 days at N=1).

## What was NOT minted (anti-inflation)
- The multi-interface delivery (TUI + menu-bar + HTTP-API + iOS) — delivery ≠ structure (observation).
- A 4th observability sub-flavor ("dashboard/mission-control") — lazyagent is sub-flavor (a); a 4th flavor would inflate (v159/v164 discipline).
- The lazy\*-TUI lineage — genre note, not a cited-to-subject elevation.
- §28 cap: 1 of ≤2 used.
