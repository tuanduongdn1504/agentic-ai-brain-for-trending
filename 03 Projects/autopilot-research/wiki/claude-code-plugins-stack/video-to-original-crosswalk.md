# Video → Original Crosswalk

> Every tool: what Chase says → the verified original → what Chase *adds* → what he gets *wrong or omits*. Sorted by the video's presentation order.

| # | Chase's framing | Original (verified) | What Chase adds | Wrong / overstated / omitted |
|---|---|---|---|---|
| 1 | Taste Skill "gives AI taste, defeats the slop monster" | `leonxlnx/taste-skill` 52.9K★ MIT | names sub-skills (image-to-code/redesign/output) | gate-count unverifiable; it's framework-agnostic + GSAP, not React/Tailwind/Motion; solo project, not "beyond Anthropic's" by any documented claim |
| 2 | Impeccable "became built-in to GitHub Copilot" | `pbakaus/impeccable` 42.2K★ Apache-2.0 | the live visual editor as differentiator | **REFUTED**: Impeccable *added a Copilot hook*; users still install+enable; GitHub didn't adopt it. Editor is **alpha** not beta |
| 3 | Awesome Design MD "clone the design language" | `voltagent/awesome-design-md` 94.2K★ MIT | the Airtable demo | "Google Stitch invented design.md" is **unverifiable** (no official repo) |
| 4 | Ponytail "50% less code, even more drastic w/ Opus" | `DietrichGebert/ponytail` 65.9K★ MIT | the 7-rung "laziest senior dev" framing | actual is **−54%** (Haiku); the **Opus claim is UNVERIFIED** (Haiku-only benchmark) |
| 5 | notebooklm-py "connect Claude Code to NotebookLM" | `teng-lin/notebooklm-py` 17.0K★ MIT | the YouTube-transcript workflow | "no official API" now **PARTIAL** (Enterprise API exists, Preview); it's the engine the operator *already runs* (v0.3.4, current is v0.7.2) |
| 6 | Playwright CLI "way less tokens than the MCP" | `microsoft/playwright-cli` 11.7K★ Apache-2.0 | productized "plugin" framing | "**70+ commands**" → ~40–50; 2020 date is the parent project (CLI launched **early 2026**); token figures are **third-party** |
| 7 | Codex Plugin "Claude loves its own code; get a 2nd opinion" | `openai/codex-plugin-cc` 21.8K★ Apache-2.0 | `/codex:rescue` + parallel work | "Claude over-trusts its code" is **video speculation**; **8** commands not 7; ChatGPT **Free** works; omits `/codex:transfer` |
| 8 | GWS "made by a Google dev, got him fired" | `googleworkspace/cli` 29.1K★ Apache-2.0 Rust | the firing hook | firing **CONFIRMED** but nuanced (fired ~2 days after Google's *own* CLI launch; agent-disruption fears); **103 skills** not 40+; "not official product" yet *is* in the official org |
| 9 | GitHub CLI "first thing you install" | `cli/cli` 45.0K★ MIT Go | — | CONFIRMED, uncontroversial; operator already has it (`gh 2.92.0`) |
| 10 | Skill Creator "most important skill; auto A/B tests" | `anthropics/skills` 156.5K★ | the AB framing (with/without skill) | loop is **semi-manual** not "auto"; "most important" is editorial |
| 11 | Last 30 Days "was #1 repo; cheaper than /deep-research" | `mvanhorn/last30days-skill` 47.5K★ MIT | the 13-source list | #1-trending **CONFIRMED** (Mar 25–26 2026); "/deep-research alternative" is **his framing, not the docs'**; TikTok/IG need a paid key |
| 12 | Firecrawl "open-source gives much of the same" | `firecrawl/firecrawl` 141.1K★ AGPL-3.0 | the scrape-vs-WebFetch comparison | **REFUTED**: self-host **lacks Fire-engine** (bot-evasion is cloud-only); "96% coverage" **unverified** (3rd-party ~63%) |
| 13 | autoresearch "ML in a box; point at any app; 83→15" | `karpathy/autoresearch` 89.1K★ | the success-criteria caveat | "any app" **overstated** (nanochat-pretraining-specific); "**83 exp → 15**" **UNVERIFIED** (not in repo); MIT is README-only |
| 14 | Supabase CLI "DBs + auth from NL; generous free tier" | `supabase/cli` 2.3K★ MIT | the form-emails use-case | NL is **Claude Code + MCP**, not the CLI; free tier **auto-pauses after 1 week** + no auto-backups |
| 15 | Obsidian "improve memory; built by Obsidian's founder" | `kepano/obsidian-skills` 38.8K★ MIT | the vault-as-knowledge-graph framing | "founder" **REFUTED** (CEO); the skill is **not a memory/RAG system** (file-format tool) |
| 16 | LightRAG "real KG+embeddings vs Obsidian's fake one" | `HKUDS/LightRAG` 37.1K★ MIT | RAG-Anything mention | false dichotomy; RAG-Anything now **merged into v1.5**; perf-vs-GraphRAG **contradicted by 2025 meta-eval**; "lightweight" ≠ low-compute |
| 17 | Stripe CLI "control your integration via NL in Claude Code" | `stripe/stripe-cli` 2.1K★ Apache-2.0 | the dashboard-is-a-pain framing | **REFUTED**: zero native LLM/NL features; you just shell out to it; CLI ≠ dashboard-superior (complementary) |

## What the video adds (the genuine contribution)

- **A curated, mostly-free starter set** across three needs (design / productivity / data) — a reasonable "what's worth your time" filter for a beginner.
- **The clearest public demo** of Awesome Design MD (Airtable) and the Ponytail decision-ladder framing.
- Surfacing **Ponytail** (17 days old) and **Impeccable** early — both genuinely useful and not yet in the wiki.

## What the video omits (matters for the operator)

- **No cost/setup honesty** — "free" hides Supabase auto-pause, Firecrawl pay-per-page, LightRAG's LLM requirement, ScrapeCreators keys.
- **No "works WITH vs integrated INTO" distinction** — most of these are CLIs you shell out to, not native skills/plugins.
- **No mention that 2 of the 17 are this operator's own foundation** (autoresearch, notebooklm-py) — naturally, since it's a general-audience video.
- **No token-cost discipline beyond Ponytail/Playwright** — and even those numbers are third-party.

## Cross-links
- [[claude-code-plugins-stack/source-provenance]] — every verdict with evidence + URLs
- [[claude-code-plugins-stack/the-17-plugins]] — the per-tool catalog
