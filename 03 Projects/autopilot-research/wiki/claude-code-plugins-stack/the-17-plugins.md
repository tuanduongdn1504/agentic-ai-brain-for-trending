# The 17 Plugins — Full Catalog

> Reference sheet. Every tool with `gh api`-verified metadata (2026-06-29), what it is, how it works, the video's load-bearing claim, and the adversarial verdict. Deep-dives linked per row.

## Verified metadata (all confirmed via live GitHub API, 2026-06-29)

| # | Tool | Repo | Stars | License | Lang | Created | Status |
|---|---|---|---|---|---|---|---|
| 1 | Taste Skill | `leonxlnx/taste-skill` | 52,861 | MIT | JavaScript | 2026-02-19 | covered |
| 2 | Impeccable | `pbakaus/impeccable` | 42,154 | Apache-2.0 | JavaScript | 2025-11-16 | NEW |
| 3 | Awesome Design MD | `voltagent/awesome-design-md` | 94,193 | MIT | (markdown) | 2026-03-31 | covered |
| 4 | Ponytail | `DietrichGebert/ponytail` | 65,885 | MIT | JavaScript | 2026-06-12 | NEW |
| 5 | notebooklm-py | `teng-lin/notebooklm-py` | 16,968 | MIT | Python | 2026-01-07 | you run it |
| 6 | Playwright CLI | `microsoft/playwright-cli` | 11,671 | Apache-2.0 | JavaScript | repo 2020-06-19 (CLI product early 2026) | covered |
| 7 | Codex Plugin | `openai/codex-plugin-cc` | 21,835 | Apache-2.0 | JavaScript | 2026-03-30 | covered |
| 8 | GWS (Google Workspace CLI) | `googleworkspace/cli` | 29,104 | Apache-2.0 | Rust | 2026-03-02 | NEW |
| 9 | GitHub CLI | `cli/cli` | 45,044 | MIT | Go | 2019-10-03 | NEW |
| 10 | Skill Creator | `anthropics/skills` (skill-creator) | 156,454 | source-available* | Python | 2025-09-22 | covered |
| 11 | Last 30 Days | `mvanhorn/last30days-skill` | 47,530 | MIT | Python | 2026-01-23 | NEW |
| 12 | Firecrawl | `firecrawl/firecrawl` | 141,085 | AGPL-3.0 (SDKs MIT) | TypeScript | 2024-04-15 | NEW |
| 13 | autoresearch | `karpathy/autoresearch` | 89,055 | MIT in README (no LICENSE file)** | Python | 2026-03-06 | foundation |
| 14 | Supabase CLI | `supabase/cli` | 2,315 | MIT | TypeScript | 2020-11-19 | NEW |
| 15 | Obsidian | `kepano/obsidian-skills` | 38,802 | MIT | (markdown) | 2026-01-02 | covered |
| 16 | LightRAG | `HKUDS/LightRAG` | 37,129 | MIT | Python | 2024-10-02 | covered-mention |
| 17 | Stripe CLI | `stripe/stripe-cli` | 2,101 | Apache-2.0 | Go | 2019-06-14 | NEW |

`*` `anthropics/skills` GitHub API `license` is `null` (mixed/source-available across the repo). `**` `karpathy/autoresearch` declares MIT in its README but ships no `LICENSE` file → GitHub API reports `null`. See [[claude-code-plugins-stack/source-provenance]].

> Star-count note: the two infra CLIs (Supabase 2.3K, Stripe 2.1K) are *low* not because they're obscure but because they're mature vendor tooling — adoption is measured in downloads, not stars. The viral-skill repos (Skill Creator 156K, Firecrawl 141K, Awesome Design 94K, autoresearch 89K, Ponytail 65.9K) are inflated by the 2026 "skills" gold-rush and the Anthropic plugin-marketplace surfacing — treat raw star counts as attention, not quality.

---

## Design bucket

### 1. Taste Skill — `leonxlnx/taste-skill` (covered)
**What:** an anti-slop frontend-design skill ("gives your AI good taste"). 3 dials (DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY), a non-negotiable em-dash ban, brief-inference, a "design-system map," and a pre-flight gate; 13 variants (incl. image-to-code, redesign, output). **Video claim:** "works with every agent, beyond Anthropic's default frontend-design skill." **Verdict:** CONFIRMED it's framework-agnostic and multi-agent; the exact pre-flight gate count is **not enumerable from the public README** (don't cite "54" or "62" as fact); animations are GSAP, not "Motion library." Full deep-dive lives in [[ai-web-design-workflow/_index]]; refresh in [[claude-code-plugins-stack/already-deep-dived-crosswalk]].

### 2. Impeccable — `pbakaus/impeccable` (NEW)
**What:** a rival anti-slop design system by **Paul Bakaus** (jQuery UI creator, at Google). 23 commands (`craft`, `audit`, `critique`, `polish`, `bolder`, `quieter`, `distill`, `live`…), **44 deterministic detector rules** (no LLM/API key needed), and a **live visual editor** (pick a DOM element on your running site, request a change, see variants via HMR). **Video claim:** "a couple days ago it became *built-in* to GitHub Copilot." **Verdict: REFUTED** — *Impeccable* added a Copilot hook (PR #279, 2026-06-20); users still install + enable it. The live editor is **alpha**, not beta. Full deep-dive: [[claude-code-plugins-stack/new-design-tools-impeccable]].

### 3. Awesome Design MD — `voltagent/awesome-design-md` (covered)
**What:** 73–74 brand `DESIGN.md` files (Airtable, Stripe, Tesla, Linear, Figma…) in **Google-Stitch format** — drop one in your repo, the agent "builds a page that looks like this." **Verdict:** CONFIRMED as a clone-the-*language* template library; the "Google Stitch" provenance is **unverifiable** (no official `google/stitch` repo; docs inaccessible). Covered in [[claude-code-skills-stack/_index]]; refresh in [[claude-code-plugins-stack/already-deep-dived-crosswalk]].

### 4. Ponytail — `DietrichGebert/ponytail` (NEW)
**What:** "makes your AI agent think like the laziest senior dev." A **7-rung decision ladder** (YAGNI → reuse → stdlib → native → dependency → one-liner → minimum) run *after* the agent understands the problem. **Video claim:** "50% less code, 22% fewer tokens, 20% cheaper, 27% faster — and even more drastic with Opus." **Verdict:** benchmark CONFIRMED (actually **−54%** LOC / −22% tokens / −20% cost / −27% time on **Haiku 4.5**, n=4, FastAPI+React); the "Opus even more drastic" claim is **UNVERIFIED** (the repo stopped at Haiku "for cost"). Fastest-growing repo in the set (**~3,880 stars/day**, 17 days old). Full deep-dive: [[claude-code-plugins-stack/new-ponytail-code-minimalism]].

---

## Productivity bucket

### 5. notebooklm-py — `teng-lin/notebooklm-py` (you run it)
**What:** unofficial Python/CLI bridge to Google NotebookLM (Playwright + undocumented endpoints); 50+ commands; exposes features the web UI doesn't (batch downloads, quiz/flashcard JSON export, chat-to-notes). **Verdict:** CONFIRMED it's the PyPI `notebooklm-py` your `yt-pipeline` runs on. Current is **v0.7.2**; your vault is pinned to **v0.3.4** (3-version gap with breaking changes). "No official API" is now **PARTIAL** — Google shipped a NotebookLM *Enterprise* API (Preview, GCP-only). 27 contributors (not solo — but teng-lin is sole owner). Full deep-dive: [[claude-code-plugins-stack/originals-this-project-runs-on]].

### 6. Playwright CLI — `microsoft/playwright-cli` (covered)
**What:** Microsoft's agent-focused browser-automation CLI; writes page state to disk instead of streaming the a11y tree into context. **Video claim:** "much more effective and way less tokens than the Playwright MCP." **Verdict:** the architecture is CONFIRMED, but "**70+ commands**" is wrong (~40–50), the 2020 repo date is the *parent* project (the CLI launched **early 2026**), and the "27K vs 114K tokens (~4×)" figure is **third-party**, not Microsoft. Covered in [[claude-code-skills-stack/_index]]; refresh in [[claude-code-plugins-stack/already-deep-dived-crosswalk]].

### 7. Codex Plugin — `openai/codex-plugin-cc` (covered)
**What:** the official OpenAI plugin to run Codex/GPT from inside Claude Code — code review, **adversarial review**, `/codex:rescue` (delegate a whole feature), background jobs. **Verdict:** CONFIRMED official + 8 slash commands (Storm Bear v62 logged 7 — missed `/codex:setup`); ChatGPT **Free** works. The premise "Claude over-trusts its own code" is **video speculation** (not in OpenAI docs). Now **21.8K★** (was 17.8K at v62 — +23% in ~7 weeks). Covered in [[codex/_index]] + Storm Bear v62; refresh in [[claude-code-plugins-stack/already-deep-dived-crosswalk]].

### 8. GWS — `googleworkspace/cli` (NEW)
**What:** one CLI for all of Google Workspace (Gmail/Drive/Calendar/Sheets/Docs/Chat/Admin), in **Rust**, built dynamically from Google's Discovery Service; **103 agent skills** (services + helpers + personas + recipes); can **send email** (the connector can't). **Video claim:** "not official, made by a Google dev, got the guy fired." **Verdict: CONFIRMED** — Justin Poehnelt's X post: *"Two months ago I was fired by Google for creating the Google Workspace CLI."* Nuance: fired ~2 days after Google announced its *own* CLI at Cloud Next; the repo lives in the **official @googleworkspace org** but is "not an officially supported product." Full deep-dive: [[claude-code-plugins-stack/new-gws-google-workspace-firing]].

### 9. GitHub CLI — `cli/cli` (NEW)
**What:** GitHub's official `gh` command-line tool (45K★, MIT, Go). "Everyone should already have this." **Verdict:** CONFIRMED — it *is* the canonical first-party `gh`. Pairs with Claude Code for PRs, issues, repo ops, and `gh api` (this very wiki build used `gh api` for ground-checks). Full deep-dive: [[claude-code-plugins-stack/new-infra-clis-supabase-stripe-github]].

### 10. Skill Creator — `anthropics/skills` (covered)
**What:** first-party Anthropic skill to **create, modify, improve, and *measure*** skills — Create → Eval → Improve → Benchmark, with grader/comparator/analyzer subagents and a description-optimizer. **Video claim:** "auto-runs A/B tests; arguably the most important skill." **Verdict:** CONFIRMED it does with-skill-vs-baseline + blind A/B (semi-manual, not fully "auto"); "most important" is editorial. Covered in [[claude-code-skills-stack/_index]] + [[claude-skills/_index]]; refresh in [[claude-code-plugins-stack/already-deep-dived-crosswalk]].

### 11. Last 30 Days — `mvanhorn/last30days-skill` (NEW)
**What:** deep multi-platform research skill — queries 13+ sources (Reddit, X, YouTube, TikTok, Instagram, HN, Polymarket, GitHub, Bluesky…), ranks by **engagement** (upvotes/views/market-odds), dedupes across platforms, emits a cited brief. **Video claim:** "was the #1 repo on GitHub; cheaper alternative to /deep-research." **Verdict:** #1-trending **CONFIRMED** (Trendshift: #1 GitHub Trending Mar 25–26 2026); the "/deep-research alternative" framing is **the video's, not the docs'**. Free core (Reddit/HN/Polymarket/GitHub); TikTok/IG need a paid ScrapeCreators key. Full deep-dive: [[claude-code-plugins-stack/new-research-tools-last30days-firecrawl]].

---

## Data bucket

### 12. Firecrawl — `firecrawl/firecrawl` (NEW)
**What:** web-scrape/crawl/map/search/extract/interact API that turns pages into LLM-ready markdown; **paid cloud** (proprietary "Fire-engine" beats bot-protection) + **open-source self-host** (AGPL-3.0). **Video claim:** "open-source gives much of the same functionality." **Verdict: REFUTED** — self-host **lacks Fire-engine**, the differentiating anti-bot layer. The "96% coverage" figure is **unverified** (third-party Scrapeway June 2026 found ~63% on real sites). Full deep-dive: [[claude-code-plugins-stack/new-research-tools-last30days-firecrawl]].

### 13. autoresearch — `karpathy/autoresearch` (foundation)
**What:** Karpathy's autonomous research loop — an agent edits `train.py`, runs a fixed 5-minute experiment, scores `val_bpb`, git-checkpoints, and loops overnight; behaviour steered by a human-editable `program.md`. **Video claim:** "ML in a box — point it at any app you want to improve; 83 experiments → 15 improvements." **Verdict:** the loop is CONFIRMED, but it's **specifically single-GPU nanochat pretraining** (not "any app" — `prepare.py`/eval is locked; only `train.py` is editable), and the **"83 → 15"** figure is **not in the repo** (README says ~12 exp/hr, ~100/night). **This is the ur-pattern your [[autopilot-research-routine]] is built on.** Full deep-dive: [[claude-code-plugins-stack/originals-this-project-runs-on]].

### 14. Supabase CLI — `supabase/cli` (NEW)
**What:** run the full Supabase stack locally (Postgres + Auth + Realtime + Storage + Edge Functions via Docker), manage migrations, deploy functions, **generate TypeScript types from your schema**. **Video claim:** "create DBs and auth from Claude Code with natural language; generous free tier." **Verdict:** the CLI is CONFIRMED; the "natural language" part is **Claude Code + Supabase MCP**, not the CLI; the free tier **auto-pauses after 1 week** + has **no auto-backups** (the "generous" framing hides this). **The #1 hireui-Goal-#2 fit.** Full deep-dive: [[claude-code-plugins-stack/new-infra-clis-supabase-stripe-github]].

### 15. Obsidian — `kepano/obsidian-skills` (covered)
**What:** 5 agent skills (obsidian-markdown, obsidian-bases, json-canvas, obsidian-cli, defuddle) that teach an agent to *write* Obsidian's open file formats. **Video claim:** "easiest way to improve Claude Code memory; created by the founder of Obsidian." **Verdict:** "founder" **REFUTED** (kepano = Steph Ango, **CEO**; founders are Shida Li + Erica Xu); and the skill is **not itself a memory/RAG system** — it's a file-format tool (the RAG is the Karpathy pattern *this vault runs*). Covered in [[claude-code-skills-stack/_index]] + [[claude-code-memory-systems/_index]]; refresh in [[claude-code-plugins-stack/already-deep-dived-crosswalk]].

### 16. LightRAG — `HKUDS/LightRAG` (covered-mention)
**What:** graph + vector RAG (EMNLP 2025, arXiv:2410.05779); dual-level retrieval, 5 query modes, pluggable stores; **RAG-Anything** (multimodal) now **merged into v1.5+**. **Video claim:** "the real deal vs Obsidian's *fake* knowledge graph; lightweight." **Verdict:** the false dichotomy is flagged (Obsidian's graph and a retrieval graph solve different problems); "lightweight" applies to *architecture*, not compute (needs a capable LLM); and its perf-vs-GraphRAG edge is **contradicted by a 2025 meta-eval** (arXiv:2506.06331 — NaiveRAG outperforms under unbiased eval). No official Claude Code skill. Mentioned in [[claude-code-memory-systems/_index]] (L5); refresh in [[claude-code-plugins-stack/already-deep-dived-crosswalk]].

### 17. Stripe CLI — `stripe/stripe-cli` (NEW)
**What:** test/manage Stripe from the terminal — local webhook listening (no tunneling), `stripe trigger <event>`, CRUD on API objects, log tailing, fixtures, sandboxes. **Video claim:** "control/edit your Stripe integration via terminal + natural language in Claude Code." **Verdict:** the CLI scope is CONFIRMED, but "natural language in Claude Code" is **REFUTED** — it has **zero** native LLM features; you just shell out to it (the `CLAUDE.md` in the repo is an internal dev file, not an integration). Full deep-dive: [[claude-code-plugins-stack/new-infra-clis-supabase-stripe-github]].

---

## Next

- The 8 NEW tools, deep: [[claude-code-plugins-stack/new-design-tools-impeccable]] · [[claude-code-plugins-stack/new-ponytail-code-minimalism]] · [[claude-code-plugins-stack/new-research-tools-last30days-firecrawl]] · [[claude-code-plugins-stack/new-infra-clis-supabase-stripe-github]] · [[claude-code-plugins-stack/new-gws-google-workspace-firing]]
- The two you run: [[claude-code-plugins-stack/originals-this-project-runs-on]]
- The 7 you already deep-dived: [[claude-code-plugins-stack/already-deep-dived-crosswalk]]
- Every correction: [[claude-code-plugins-stack/source-provenance]]
