# Source Provenance — verification ledger

> How this topic was built and what survived adversarial scrutiny. Rule 12 (fail-loud): every correction is logged.

## Method

- **Transcript:** `yt-dlp --write-auto-subs --sub-langs en` on [V2RIVnGCy74](https://www.youtube.com/watch?v=V2RIVnGCy74), deduped to ~3,840 words, **read in full**. (yt-dlp threw a transient 429 on the first metadata call but the subtitle fetch succeeded; ffmpeg absent → VTT parsed directly.)
- **Originals:** all 17 fetched directly — `gh api` for repo metadata + WebFetch/WebSearch for READMEs, docs, and external corroboration.
- **Adversarial verification:** Workflow **`wf_81b898cf-93e`** — 35 agents: 17 research (one per original) → 17 independent adversarial skeptics (re-checked each tool's load-bearing claims with fresh web search + `gh api`, default-to-UNVERIFIED) → 2 critics (completeness + operator-fit). Total ~1.6M tokens, 776 tool calls. **One agent failed** (`research:github-cli`, "prompt too long") — GitHub CLI was researched directly by the operator via `gh api repos/cli/cli` instead.
- **Ground-check:** every star/license/created-date confirmed against the live GitHub API on **2026-06-29**.

## Confirmed (the video got these right)

- **GWS author was fired** — Justin Poehnelt's X post ([JPoehnelt/status/2069482265953087602](https://x.com/JPoehnelt/status/2069482265953087602)): *"Two months ago I was fired by Google for creating the Google Workspace CLI."* Corroborated by HTX Insights, a Hacker News thread, officechai.com.
- **Last 30 Days was #1 GitHub Trending** — Trendshift archive: #1 on **Mar 25, 2026** (Python) and **Mar 26, 2026** (all languages); README badge corroborates.
- **Ponytail is one of the fastest-growing repos** — 17 days old, **~3,876 stars/day** (extreme tier). Benchmark numbers (−54% LOC / −22% tokens / −20% cost / −27% time, Haiku 4.5, n=4) match the repo's `benchmarks/results/2026-06-18-agentic.md` exactly.
- **Codex Plugin is the official OpenAI plugin** — `openai` org, Apache-2.0, 8 slash commands, 6-primitive architecture.
- **notebooklm-py is the PyPI package the operator runs** — and exposes more than the NotebookLM web UI.
- **autoresearch is Karpathy's** — and the operator's routine is an accurate semantic port of its design.
- **All 17 repos exist, are correctly attributed, and link to exactly what Chase says.**

## Corrected / Refuted (Rule 12 fail-loud)

1. **Impeccable "became built-in to GitHub Copilot" → REFUTED.** *Impeccable* added a Copilot **hook** (PR #279, merged 2026-06-20, 6 days before the video); users still install + enable it. GitHub's Copilot docs never mention Impeccable. Also: the live editor is **alpha** (not "beta"); 23 commands (an earlier internal draft said 26 — wrong).
2. **Obsidian "created by the founder of Obsidian" → REFUTED.** kepano = **Steph Ango is CEO**, not founder (founders: Shida Li @licat, Erica Xu @silver). And `obsidian-skills` is a **file-format tool, not a memory/RAG system** — the "improve Claude Code memory" framing is misdirected.
3. **autoresearch "ML in a box, point at any app" → PARTIAL/overstated.** It's **nanochat-pretraining-specific** (locked `prepare.py`/eval; only `train.py` editable). The **"83 experiments → 15 improvements"** statistic is **UNVERIFIED** — not in the repo, README, commits, or releases (README only estimates "~12 exp/hr, ~100/night"). License: **MIT in README only — no LICENSE file** (`gh api` → `license: null`).
4. **Firecrawl "open-source gives much of the same functionality" → REFUTED.** Self-host **lacks Fire-engine** (the bot-evasion layer) per the official `SELF_HOST.md`. "**96% coverage**" → **UNVERIFIED** (third-party Scrapeway June 2026 found ~63% on real sites). Mendable was **shut down / pivoted** to Firecrawl (not a rebrand or fork).
5. **Stripe CLI "control via natural language in Claude Code" → REFUTED.** Zero native LLM/NL features; you shell out to it like any CLI. The repo's `CLAUDE.md` is an internal dev-context file, not an integration.
6. **GWS "got the guy fired for popularity" → CONFIRMED but nuanced.** Fired **~2 days after Google announced its *own* Workspace CLI** at Cloud Next; attributed to agent-disruption fears + Legal's branding concerns. **103 skills**, not "40+." "Not official product" yet lives in the **official `@googleworkspace` org** (Google-authored, unsupported-as-product).
7. **Ponytail "even more drastic with Opus" → UNVERIFIED.** No agentic Opus benchmark exists (the repo stopped at Haiku "for cost"). The video's "50% less code" rounds the actual **−54%**.
8. **Playwright CLI "70+ commands" → ~40–50** (third-party reference). The **2020 repo date is the parent project**; the agent CLI launched **early 2026**. The "**27K vs 114K tokens (~4×)**" figure is **third-party**, not Microsoft-official.
9. **Codex "Claude over-trusts its own code" → UNVERIFIED** (video speculation, not in OpenAI docs). It ships **8** commands, not 7 (prior Storm Bear v62 missed `/codex:setup`); **ChatGPT Free** is supported.
10. **Taste Skill pre-flight gate count → UNVERIFIABLE from the public README** (the 2026-06-20 ai-web-design build cited "62"; this build's stage-1 said "54"; neither is enumerable in the public repo). Stack is **framework-agnostic + GSAP**, not React/Tailwind/Motion (a stage-1 over-specification, refuted by the skeptic).
11. **Awesome Design MD "Google Stitch design.md" provenance → UNVERIFIABLE** (no official `google/stitch` repo; spec docs inaccessible). 73–74 files (74 dirs vs 73 in the README — off-by-one).
12. **Supabase "natural language" → it's Claude Code + the Supabase MCP**, not the CLI. Free tier **auto-pauses after 1 week** + **no auto-backups**.
13. **LightRAG "real KG vs Obsidian's fake one" → false dichotomy** (different jobs). **RAG-Anything is now merged into v1.5+** (not a separate extension). Perf-vs-GraphRAG is **contradicted by arXiv:2506.06331 (2025)** — under unbiased eval, NaiveRAG outperforms LightRAG; E²GraphRAG reports ~100× speedup. **No official Claude Code skill.**
14. **notebooklm-py "no official API" → now PARTIAL** (Google NotebookLM **Enterprise API** exists, Preview, GCP-only). The vault's "bus factor = 1" note should be amended: **27 contributors** (teng-lin sole owner/gatekeeper). Vault is pinned to **v0.3.4**; current is **v0.7.2** (breaking changes between).

## Flagged / unresolved

- **Star counts as a quality signal** — the viral-skill repos (Skill Creator 156K, Firecrawl 141K, Awesome Design 94K, autoresearch 89K, Ponytail 66K) are inflated by the 2026 "skills" gold-rush + Anthropic-marketplace surfacing. Treat as *attention*, not quality. The mature vendor CLIs (Supabase 2.3K, Stripe 2.1K) are low-star but high-adoption.
- **Performance claims decay** — Firecrawl (96%→63%), LightRAG (paper claims→2025 reversal), Ponytail (Opus unverified). Re-verify any perf claim >6 months old.
- **"Works WITH Claude Code" vs "integrated INTO it"** — ≥6 of 17 are shell-out CLIs, not native skills/plugins. The video's "connect to Claude Code" language blurs this.

## Adversarial-pass note (process honesty)

The workflow's first launch was stopped immediately after a self-caught script bug (the `pipeline()` would have discarded the rich stage-1 research and returned only the verdicts); the script was patched to merge research + verdict, and the run resumed from cache (`resumeFromRunId`). The adversarial design *worked*: stage-2 skeptics overturned several stage-1 over-specifications (Taste Skill tech-stack, Impeccable's "26" commands, the autoresearch "MIT" license, the GWS "official-vs-unofficial" framing), exactly as intended.

## Cross-links
- [[claude-code-plugins-stack/video-to-original-crosswalk]] — the per-tool verdict table
- [[claude-code-plugins-stack/_index]] — topic index
