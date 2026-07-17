# Source & Provenance

## The source

- **Title:** Tất Tần Tật Về Cấu Trúc Dữ Liệu Trong 32 Phút (Everything About Data Structures in 32 Minutes)
- **URL:** https://www.youtube.com/watch?v=uHpzKcm8qh0
- **Channel:** Học Giải Thuật Cùng HPN (Learning Algorithms with HPN)
- **Uploaded:** 2026-07-12 · **Duration:** 32:22 · **Views:** ~15,034 (at ingest)
- **Language:** Vietnamese · **Type:** educational explainer (animated, single-narrator)

## Ingestion

- **Path:** 5 (yt-dlp transcript) — operator-submitted anchor URL, ingested **2026-07-17**.
- **Captions:** `--write-auto-subs vi-orig` → `sub.vi-orig.vtt` (301 KB) → deduped to **715 lines / ~27 KB** clean text.
- **Reading:** full Vietnamese transcript **read directly in the main loop** (Claude reads VN); **no NotebookLM** used (`notebook_id: none`).
- **Raw artifact:** `raw/2026-07-17-data-structures-16-in-32-min.md` (metadata + cleaned transcript).
- **Metadata:** `yt-dlp --skip-download --print` (title/channel/date/duration/views/description).

## Verification

- **Workflow:** `wf_83c9b13a-5b9` — **10 agents**, ~377.6K subagent tokens, 88 tool calls, **0 errors / 0 empty / 0 skipped**; all **Haiku 4.5**.
  - 6 refute-first fact-check clusters (WebSearch-grounded) over 24 date/inventor/Big-O claims.
  - 1 corpus-xref librarian (ls/grep the local wiki to ground-truth cross-links + collision check).
  - 1 CS-history nuance-hunter (contested/anecdotal claims).
  - 1 educational appraisal (pedagogy + hireui applicability).
  - 1 completeness critic (gap analysis → [[beyond-the-video]]).
- **Main-loop role:** transcript comprehension, article synthesis, ASR-garble correction, and honest re-grading of the corpus-xref agent's cross-link verdicts (thematic vs. content).
- **Result:** [[claims-scorecard]] — **22 CONFIRMED / 1 ANECDOTAL / 1 CORRECT-BUT-INCOMPLETE / 0 FALSE / 0 FABRICATED**.

### Verification discipline notes (Rule 12 fail-loud)

- **Cross-link honesty:** the corpus-xref agent (correctly skeptical) rated most intended cross-links MISLEADING/FALSE on *content* grounds. Rather than suppress that, the main loop **kept the useful ones but re-labeled them thematic vs. content** in [[corpus-and-hireui-relevance]] — the fundamentals-thread links (Pocock, Quân IT, system-thinking) are explicitly marked thematic; only [[graphify-codebase-graph/_index]] is a true content link.
- **No collision:** grep confirmed no pre-existing data-structures/algorithms topic; the only prior "skip-list"/"bloom-filter" hits were incidental metaphors in unrelated pilot docs.
- **ASR garbles** (≈20 mangled proper names) were corrected against verified spellings — see [[caveats-and-corrections]] §A. These are transcription artifacts, **not** errors in the video.

## Corpus context

- **First pure CS-fundamentals topic**; **2nd non-Claude/non-agent topic** (structural sibling of [[self-hosted-devops-oss/_index]]).
- **62nd topic** in the autopilot-research wiki (unversioned; the numbering is external/operator-side, not part of this wiki).

## Files (20)

`_index` · `overview` · `big-o-primer` · `linear-structures` · `hashing` · `balanced-trees` · `heap-and-priority` · `graph-and-traversal` · `string-trie` · `disjoint-set` · `probabilistic` · `disk-scale` · `historical-timeline` · `selection-framework` · `beyond-the-video` · `claims-scorecard` · `caveats-and-corrections` · `corpus-and-hireui-relevance` · `critical-appraisal` · `source-provenance`

## Key Takeaways

- Operator-submitted VN video, **path-5 yt-dlp**, full transcript read in main loop; raw at `raw/2026-07-17-data-structures-16-in-32-min.md`.
- Adversarially verified (`wf_83c9b13a-5b9`, 10 agents, 0 errors) → **exceptionally high integrity** ([[claims-scorecard]]).
- Cross-links graded honestly (thematic vs. content); no collision; ~20 ASR garbles corrected.
