# okf-open-knowledge-format

> **Source:** Cole Medin, *"Finally, an Open Standard for the Karpathy LLM Wiki is HERE"* — [T33iI6izAKw](https://www.youtube.com/watch?v=T33iI6izAKw), 19:37, ~59K views, uploaded 2026-07-02 (weekly YouTube upload, not a conference talk).
> **Subject:** **Google's Open Knowledge Format (OKF)** — an open standard that formalizes Andrej Karpathy's LLM-wiki pattern into portable markdown + YAML frontmatter. Repo [`GoogleCloudPlatform/knowledge-catalog/okf`](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) (Apache-2.0, ~7.1K★); launch blog [2026-06-13](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) by two Google Cloud BigQuery/Data Cloud tech leads.
> **Ingested:** 2026-07-15 (path 5 yt-dlp; EN auto-captions → deduped 43-paragraph / ~4.2K-word transcript, read in full).
> **Verification:** Workflow `wf_a8b95e41-6b3` (8 agents = 4 fact-check clusters + corpus-xref + thesis-critique + pilot-design + completeness-critic) + main-loop Opus WebFetch/gh ground-checks against the real repo, SPEC.md, blog, and Karpathy gist.
> **Scorecard: 11 CONFIRMED / 5 MISLEADING / 2 FALSE / 0 FABRICATED / 2 OPINION** (20 checkable claims) — see [[claims-scorecard]].
> **Corpus role:** **CORPUS-FIRST on OKF**, and the **first dedicated topic that treats the Karpathy LLM Wiki pattern itself as a *subject*** (rather than merely *using* it). Uniquely **reflexive** — this entire vault *is* a Karpathy LLM Wiki, so OKF is the first formal spec the vault could adopt or measure itself against. (NOT Cole Medin's first corpus appearance — he is the Archon creator; see [[external|harness-engineering/_index]].)

**The 30-second version:** Karpathy's LLM-wiki gist (2026-04-04, ~5K★) is a *pattern*, not a *standard* — everyone builds it differently, so you can't hand your wiki to someone else's agent and have it "just work." Google's **OKF** adds a thin, minimally-opinionated standard on top: **markdown files with YAML frontmatter, exactly one required field (`type`), reserved index/log filenames, and producer/consumer conventions.** Cole sells OKF as *"the future of personal agents / second brains."* Google actually shipped it for **enterprise data sharing** (BigQuery table schemas, metric definitions, incident runbooks). Both are legitimate — Cole just inverts Google's stated emphasis. The technical content of the video is **accurate**; the numbers are **sloppy** (Karpathy gist is ~5K★ not "40,000"; the bundle has 5 videos not "four").

## Articles

- [[overview]] — the whole video in one page: Karpathy pattern → the "no standard = can't share" problem → OKF as the fix → Cole's bundle "gift" → the "too simple?" critique.
- [[what-okf-standardizes]] — what the SPEC actually says: two things only (organization + metadata); `type` is the **single required field**; recommended fields; reserved `index.md`/`log.md`; **bundle** = unit of distribution; producer/consumer roles; what OKF explicitly does **not** standardize (storage/serving/query, taxonomies, folder hierarchy).
- [[personal-vs-enterprise-framing]] — **the headline nuance.** Cole = "future of personal second brains"; Google = enterprise data catalogs (BigQuery). Both true; emphasis inverted. Why this matters before you adopt.
- [[claims-scorecard]] — all 20 checkable claims graded; the 2 FALSE numbers, the 5 MISLEADING framings, the 2 OPINIONs.
- [[caveats-and-corrections]] — 40,000★ → **~5,000★**; "four videos" → **five**; "quietly shipped" → had a **public blog 19 days earlier**; "Obsidian/Notion import" → **clone + read markdown**; PIV-loop-vs-context-engineering; the Google-sunsetting risk; open questions.
- [[thesis-critique]] — adversarial: is the sharing problem real or a solution-in-search-of-a-problem? Network-effects ceiling; why "`type` is the only required field" delivers *weaker* interop than promised; Cole's own hedge ("I don't think OKF will end up being the standard") and what it costs his argument.
- [[vault-adoption-pilot]] — **the operator decision: WATCH (don't adopt yet).** The <1-hour first experiment (OKF-ify one topic + query it with a fresh agent); a proposed `type` vocabulary for this vault; honest migration cost; hireui relevance; pilot ranking.
- [[vs-karpathy-and-corpus]] — **reflexive significance.** The vault is ~80% structurally OKF-aligned but ~0–10% on metadata (no YAML `type`). What OKF would/wouldn't add. Dense cross-links to the corpus' Karpathy-lineage articles.
- [[source-provenance]] — sources, key resources, verification methodology, agent-tier note.

## Cross-links to existing autopilot topics

- [[external|claude-code-memory-systems/_index]] — its **Level-5 = Karpathy LLM Wiki** article is the corpus' canonical reference for the original gist; OKF is the formal spec for that level.
- [[external|harness-engineering/_index]] — Cole Medin's home turf in the corpus (he built **Archon**, the harness *builder*). OKF is his knowledge-*standardization* work.
- [[external|graphify-codebase-graph/_index]] — described in-corpus as "the automated version" of the Karpathy wiki; OKF standardizes what Graphify automates.
- [[external|claude-md-12-rules/_index]] — the vault's own librarian-rules layer; OKF is a contemporary, machine-readable standardization effort in the same spirit.
- [[external|agent-memory-architecture/_index]] — proposed **first pilot target** for an OKF refactor experiment (small, recent, self-contained).
- [[external|ai-engineering/_index]] — structured-knowledge-for-agents is an AI-engineering discipline theme.

## Source

- `raw/2026-07-15-okf-open-knowledge-format.md` — metadata header + full video description (with all creator links) + full deduped transcript (43 timestamped paragraphs).
