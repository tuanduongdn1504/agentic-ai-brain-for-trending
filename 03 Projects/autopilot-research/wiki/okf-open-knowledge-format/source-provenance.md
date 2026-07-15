# Source Provenance & Verification Methodology

## Primary source

- **Video:** Cole Medin, *"Finally, an Open Standard for the Karpathy LLM Wiki is HERE"* — [youtube.com/watch?v=T33iI6izAKw](https://www.youtube.com/watch?v=T33iI6izAKw)
- **Channel:** Cole Medin (@ColeMedin) — AI-coding YouTuber; creator of **Archon** (open-source AI-coding harness builder; see [[external|harness-engineering/_index]]). Weekly uploads ("every Wednesday 7:00 PM CDT").
- **Uploaded:** 2026-07-02 · **Duration:** 19:37 · **Views at ingest:** 59,047
- **Ingestion path:** 5 (yt-dlp operator-submitted single video). EN auto-captions → `vtt-to-md.py` dedupe → 43 timestamped paragraphs / ~4,177 words, **read in full**.
- **Raw file:** `raw/2026-07-15-okf-open-knowledge-format.md` (metadata header + full description + full transcript).
- **NotebookLM:** none (transcript-based pipeline).

## Subject + key resources (all verified live 2026-07-15)

| Resource | URL | Verified |
|---|---|---|
| OKF repo (Google) | [github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) | Apache-2.0; parent repo ~7,068★; created 2026-05-04; `okf/` = SPEC.md, README.md, LICENSE.md, bundles, samples, src, tests, pyproject.toml |
| OKF SPEC.md (v0.1) | [.../okf/SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) | `type` = single required field; reserved `index.md`/`log.md`; bundle = unit of distribution; no storage/serving/query |
| OKF launch blog | [cloud.google.com/blog/…/how-the-open-knowledge-format-can-improve-data-sharing](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) | Published **2026-06-13**; authors **Sam McVeety + Amir Hormati** (Google Cloud Data Cloud / BigQuery); credits Karpathy |
| Cole's OKF bundle | [github.com/coleam00/cole-medin-ai-coding](https://github.com/coleam00/cole-medin-ai-coding) | Created 2026-06-25; ~90★; **no LICENSE**; index.md + concepts/ + videos/ (5 videos) + log.md + okf-cli.py |
| Karpathy LLM Wiki gist | [gist.github.com/karpathy/442a6bf…](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Created **2026-04-04**; **~5,000★ / ~4,400 forks** (NOT the "40,000" in the video) |

## Verification methodology

**Two layers**, matching corpus discipline (maker/checker + discard-as-garble guard):

1. **Main-loop Opus ground-checks (before compile)** — `gh api` on both repos (existence, license, stars, dates); WebFetch on SPEC.md (raw), the launch blog, the Karpathy gist; WebSearch to pin the gist star count + confirm GPT-5.5/Opus-4.8 are real models. These caught the 40,000→5,000 star error and established the enterprise-vs-personal framing before any wiki text was written.

2. **Workflow `wf_a8b95e41-6b3`** — 8 agents, 0 errors, 0 empty, ~392K tokens, 56 tool calls, ~170s:
   - **4 fact-check clusters** (A numbers/models · B provenance/framing · C SPEC content · D Cole's bundle) — each re-verified the main-loop findings independently against live sources (instructed *not* to trust the orchestrator's ground-truth blindly).
   - **corpus-xref** — grep across `wiki/`, `_state/`, `PATTERN_LIBRARY.md`, root `CLAUDE.md`, and operator memory; verified corpus-first status + cross-link targets + no naming collision.
   - **thesis-critique** — adversarial stress-test of Cole's argument.
   - **pilot-design** — vault-adoption decision + hireui relevance.
   - **completeness-critic** — read all prior outputs; flagged the PIV-vs-context-engineering wrinkle, the missing "paste this prompt," and the adoption-footprint gap (all logged in [[caveats-and-corrections]]).

**Agent-tier note:** the 4 fact-checkers + corpus-xref were requested at `sonnet`/analytical agents at `opus`, but the workflow runtime resolved all 8 to **Haiku 4.5** (visible in the run's progress log). This did not degrade output — every claim carries a live source URL and the main-loop Opus pass independently corroborated the load-bearing facts (repos, SPEC required-field, blog authorship, star count). Flagged per Rule 12 (fail loud): the model override didn't take effect; results stand because they're source-backed and double-checked.

## Scorecard

**11 CONFIRMED / 5 MISLEADING / 2 FALSE / 0 FABRICATED / 2 OPINION** (20 checkable claims). Full table: [[claims-scorecard]].

## Secondary / related

- Google Cloud Knowledge Catalog product page: `cloud.google.com/products/knowledge-catalog` (the OKF repo's homepage — the enterprise anchor).
- Karpathy gist reception (independent): rdworldonline, theaioperator, and several build-guides confirm the ~5K★ / viral-tweet context.

## Key Takeaways

- Every load-bearing fact was verified against the **actual repo/SPEC/blog/gist**, not the video's paraphrase or model memory.
- Two-layer verification (Opus ground-check → 8-agent workflow → completeness critic) caught the 40K-star and 4-video errors and the framing inversion.
- The one process note worth remembering: the workflow **ignored the per-agent model overrides** and ran everything on Haiku — fine here (source-backed + Opus-corroborated), but worth watching on future runs.
