# Raw Inventory — Single Source of Truth for Coverage

> **Purpose:** every ingestion event into `raw/` MUST have a row here, regardless of which path (1-8) brought it in. This file is the canonical answer to "what's been ingested" and "what's compiled vs uncompiled."
>
> **Why this exists:** before 2026-05-08, `topics-queue.md` was used as a coverage proxy — but the queue only tracks paths 1+2 (single-topic burst, scheduled cron). Paths 3-8 (single-URL, bundle, yt-search, custom scraper, query, promotion) bypass the queue and land directly in `raw/`. The Lark Claude course (261 markdown files via custom scraper) sat invisible to coverage audits for 1 day before the gap was noticed. This inventory bịt the gap.
>
> **Maintenance:**
> - Path 1+2 (autopilot-research-routine): Phase 0 auto-appends a row before ingestion + Phase 7 updates `Status` to `compiled`.
> - Path 3 (single notebooklm source add): user/skill MUST append manually. See `(C) notebooklm.md` reminder.
> - Path 4 (multi-URL bundle): same as path 3.
> - Path 5 (yt-search only, no ingest): NO inventory row needed (nothing landed in `raw/`).
> - Path 6 (custom scraper): scraper script SHOULD print the inventory row to append; user pastes it.
> - Path 7 (query mode): NO inventory row needed (nothing landed in `raw/`).
> - Path 8 (promotion to Storm Bear): NO new row, but update existing row's `Status` → `promoted`.
>
> **When the user asks "what topics are done"**, the librarian (Claude) reconciles this file ↔ `wiki/_master-index.md` and reports BOTH compiled and uncompiled artifacts. Never trust `topics-queue.md` alone.

---

## Inventory

| Date | Slug | Path | Source(s) | Size | NotebookLM ID | Status | Wiki link |
|---|---|---|---|---|---|---|---|
| 2026-05-07 | claude-code-hooks | 1 yt-pipeline | YouTube ×5 | 16K | (in raw file) | compiled | [wiki/claude-code-hooks/](../wiki/claude-code-hooks/_index.md) |
| 2026-05-07 | workflow-ai-coding | 1 yt-pipeline | YouTube ×6 | 20K | `ec93ea09-b589-4103-95a9-3fb2c13d5a2e` | compiled | [wiki/workflow-ai-coding/](../wiki/workflow-ai-coding/_index.md) |
| 2026-05-07 | 10x-claude-code | 1 yt-pipeline | YouTube ×6 | 20K | `d1d18b0b-ab85-4773-a999-98f36fb39cf5` | compiled | [wiki/10x-claude-code/](../wiki/10x-claude-code/_index.md) |
| 2026-05-07 | remote-agent-control-tunneling | 2 cron-overnight | YouTube ×N | 20K | `46ee01f8-81e3-47d6-b617-4c322359b6b9` | merged-into-stack | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-07 | mcp-messaging-platforms | 2 cron-overnight | YouTube ×N | 20K | `183e3635-ea8c-4c52-9c16-11aa32e19c78` | merged-into-stack | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-07 | claude-code-sdk-headless | 2 cron-overnight | YouTube ×N | 20K | `dafc8c4f-840b-41a1-b125-bfe973c919f0` | merged-into-stack | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-07 | telegram-bot-remote-control | 2 cron-overnight | YouTube ×N | 20K | `5f514e9c-d8e4-42be-af1e-c456dfa1e4c7` | merged-into-stack | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-07 | lark-claude-course | 6 custom-scraper | Lark wiki, 261 pages | 1.9M | `2a42eeff-a797-44cd-86d5-f8b8a4ee491b` ("Claude Couse 2026", 319 sources) | uncompiled | — |
| 2026-05-08 | telegram-remote-control-stack | (compile-merge) | 4 raw bundles + live pilot | (synthesis) | (multiple, see merged rows) | compiled | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-09 | harness-engineering-anchor (VTT) | 5 yt-dlp-only | YouTube am_oeAoUhew (Lopopolo talk 46:20) | 394K | — | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | harness-engineering-anchor (transcript) | 5 yt-dlp-only | derived from VTT via vtt-to-md.py | 44K | — | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | harness-engineering-anchor (structured) | 4 multi-bundle | YouTube + Latent Space podcast (2 sources, 6-section synthesis) | 22K | `d772d58b-ff6c-41c5-aec1-7cd83637226e` | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | openai-blog-harness-engineering (HTML) | bypass-403-tier-1 | Playwright vanilla after curl Tier 0 failed | 478K | — | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | openai-blog-harness-engineering (clean MD) | bypass-403-tier-1 | derived from HTML via html-to-clean-md.py (readability-lxml + pandoc) | 21K | `d772d58b-…26e` (uploaded as 3rd source) | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | openai-blog-delta-synthesis | 4 multi-bundle | NotebookLM 3-source delta-analysis (blog vs talk vs podcast) | 8K | `d772d58b-…26e` | compiled | [wiki/harness-engineering/blog-talk-evolution](../wiki/harness-engineering/blog-talk-evolution.md) |
| 2026-05-09 | openai-symphony-spec (FAILED) | bypass-403-tier-2 | Tier 1+2 failed (backend-gate Cloudflare); pivoted to community | 396K HTML (Next.js error page only) | — | dropped (pivot) | — |
| 2026-05-09 | symphony-community-implementations | 4 multi-bundle | 3 GitHub repos: ACNoonan/symphony-restate (Elixir+Restate) + ryanjdillon/symphony (Go) + howardpen9/symphony-rs (Rust) | (NotebookLM-indexed) | `d772d58b-…26e` (added as sources 4-6) | compiled | [wiki/harness-engineering/symphony-architecture](../wiki/harness-engineering/symphony-architecture.md) |
| 2026-05-09 | symphony-community-synthesis | 4 multi-bundle | NotebookLM 6-source triangulation (3 OpenAI + 3 community) | 9K | `d772d58b-…26e` | compiled | [wiki/harness-engineering/symphony-architecture](../wiki/harness-engineering/symphony-architecture.md) |
| 2026-05-11 | claude-md-12-rules-mnilax | 3 manual-paste | X.com tweet thread (auth-walled — mirrors dead) | 14K | — | compiled | [wiki/claude-md-12-rules/](../wiki/claude-md-12-rules/_index.md) |
| 2026-05-11 | vividkit-claudekit-guides (HTML) | bypass-403-tier-0 | curl 21 guides from vividkit.dev | ~600K HTML total | — | compiled | [wiki/claudekit/](../wiki/claudekit/_index.md) |
| 2026-05-11 | vividkit-claudekit-guides (clean MD) | bypass-403-tier-0 | html-to-clean-md.py with `main` selector | 250K MD total | — | compiled | [wiki/claudekit/](../wiki/claudekit/_index.md) |
| 2026-05-11 | vividkit-claudekit-synthesis | 4 multi-bundle | NotebookLM 21-source synthesis (6 sections) | 24K | `d179ac0c-428b-47e6-b859-99a6b7e7bcb1` | compiled | [wiki/claudekit/](../wiki/claudekit/_index.md) |

## Status legend

- **raw** — landed in `raw/`, not yet compiled
- **uncompiled** — same as `raw` but explicitly waiting for compile (vs in flight)
- **partial** — some articles compiled, more pending
- **compiled** — fully synthesized into `wiki/<topic>/`
- **merged-into-stack** — content folded into a larger compiled topic; raw file kept for audit trail
- **promoted** — already compiled here AND lifted to Storm Bear curated wiki via `llm-wiki-routine-v2.1`
- **dropped** — deliberately not compiled (e.g., low signal, off-scope); reason should be in a comment row below

## Path legend (8 ingestion surfaces)

1. `/loop autopilot research <topic>` — single-topic burst (yt-pipeline)
2. `/schedule autopilot nightly` — overnight cron, drains `topics-queue.md`
3. `notebooklm source add <url>` — single URL/PDF/YouTube
4. `notebooklm notebook create + source add ×N` — multi-URL bundle
5. `yt-dlp ytsearch20:"<q>"` — search only, no ingest (NO inventory row)
6. Custom scraper (Playwright + SPA) — Lark/Notion/Confluence
7. `notebooklm ask` — query mode (NO inventory row)
8. Promotion → Storm Bear curated wiki (UPDATE existing row, no new row)

## Coverage summary (auto-derivable; manually maintained until Lớp 3 ships)

- **Total ingestions logged:** 23 rows (4 added 2026-05-11: 1 manual paste + 3 vividkit bulk fetch)
- **Compiled (or merged):** 21
- **Dropped (intentional):** 1 (Symphony spec page failed Tier 2; pivoted to community impls)
- **Uncompiled:** 1 (lark-claude-course — 261 pages, biggest backlog)
- **Promoted to Storm Bear:** 0
- **New topics 2026-05-11:** 2 added — claude-md-12-rules (3 articles, Mnilax behavioral contract) + claudekit (7 articles, vividkit.dev framework comparison with harness-engineering + 12-rules)
- **Path 9 emerged:** manual paste when source is auth-walled + mirrors dead (X.com 2026-05-11). Update CLAUDE.md "8 ingestion surfaces" table when this pattern occurs ≥3× total.
- **Bulk fetch pattern emerged:** 21-URL fetch via `bin/bulk-fetch-vividkit.sh` (Path 6 custom scraper variant for sites without Cloudflare) — codify as reusable pattern when 2nd bulk-fetch occurs.
