# (C) log — Build history

## 2026-05-21 — Initial scaffold + citation map

**Operator entry-point:** Vietnamese-dubbed YouTube cut at `https://www.youtube.com/watch?v=JUeazROlMCU&t=33s` ("(Việt hoá chuẩn) Build & Deploy App Trên Google Cloud Với Claude Code | Code with Claude 2026").

**Resolution to original source:**
- WebFetch on the Vietnamese URL returned only YouTube footer chrome — no description content extracted.
- WebSearch using the talk's title narrowed to Anthropic's Code-with-Claude 2026 session page.
- Original-language video identified: `https://www.youtube.com/watch?v=SqHsS737CeA` (speaker: Ivan Nardini, Google Cloud).
- Anthropic session page confirmed authoritative abstract.

**Companion-repo investigation:**
- Speaker's GitHub `inardini` checked; closest repo `ship-code-with-claude-on-vertex-ai-webinar` fetched and read.
- Confirmed: this companion repo is **NOT** the talk's "feedback app" — it is a separate webinar artifact (3 demos, not a 5-role feedback app).
- Recorded distinction in entity-3.

**Honest gap call:**
- Without the actual video transcript, the wiki cannot reach v82-style entity-page depth (which had cluster pages on README positioning, methodology + assets, distribution + harness ecosystem, plus 4 entity pages).
- Decision: deliver scaffold + citation map + explicit gap inventory rather than fabricate the build's specific architectural choices.

**Files created (this session):**
- `CLAUDE.md` — project-level context including typology call ("out of T1-T5")
- `02 Wiki/(C) index.md` — entry point with citation table
- `02 Wiki/(C) entity-1-talk-metadata.md` — speaker, event, abstract decomposition
- `02 Wiki/(C) entity-2-the-concept-stack-subagents-mcp-skills.md` — Anthropic-doc-cited primitives
- `02 Wiki/(C) entity-3-companion-resources-and-speaker-context.md` — companion repo + related Anthropic / community resources
- `02 Wiki/(C) entity-4-content-gaps-and-ingest-path.md` — what's missing + 4 ingest options
- `02 Wiki/(C) log.md` — this file

**Pattern Library impact:** NONE. Subject is out-of-typology (conference talk, not T1-T5 software product). Vault state files NOT modified.

**Routine v2.3 codification candidates produced:**
1. NEW typology tier "T6 Knowledge-Source — Conference Talk / Workshop"
2. Transcript-ingest-as-required-Phase for video subjects
3. Pre-flight transcript availability check
4. Localized-entry-point → original-language-resolution discipline

**Next-step options pending operator input:**
- A: paste transcript → Claude generates 3–4 deeper entity pages
- B: green-light `yt-dlp` auto-subs extraction
- C: search for / link 2026-05-29 SF workshop materials as proxy reproduction recipe
- D: accept current state as final

**Time budget used:** ~5 WebSearch + WebFetch tool calls + 5 Write tool calls. Estimated 15-min of Claude-time.

---

## 2026-05-21 (later) — Transcript ingest + 4 deeper entity pages

**Operator decision:** Option B (auto-extract via yt-dlp).

**Extraction:**
- `yt-dlp` v2026.03.17 available at `/usr/local/bin/yt-dlp`.
- Command: `yt-dlp --skip-download --write-auto-subs --write-subs --sub-format "vtt/best" --sub-langs "en.*,en" -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=SqHsS737CeA"`
- Result: `SqHsS737CeA.en-orig.vtt` (auto-captions) + `SqHsS737CeA.en.vtt` (identical mirror), each ~204 KB / 5184 lines.
- Cleaning: `awk` pipeline strips `WEBVTT`/`Kind:`/`Language:` headers, `align:start position:0%` cue settings, inline `<HH:MM:SS.mmm><c>word</c>` per-word timing tags. Dedup on exact line repeat (rolling-window) + adjacent-line dedup → 642 unique caption lines.
- Format: timestamp marker every ~30s for navigation.
- Provenance header prepended (source URL, extraction date, processing steps, fidelity caveat).

**Saved to:** `02 Wiki/(C) transcript-raw.md` (~22 KB, 757 lines).

**Honest fidelity caveat captured in transcript header:** YouTube auto-captions, not human-transcribed. Speaker pronunciation "Code" rendered ambiguously between "Code" and "Cloud" by the captioner — context-disambiguated via Anthropic blog references when citing. Proper nouns may contain errors (verified: "Ivan Nardini", "Cloud Run", "Firestore", "BigQuery", "Looker", "Vertex AI", "ADC", "Figma", "OWASP" all caption-accurate).

**5 of 10 original gaps resolved** (G1, G3, G4, G7, G8 RESOLVED clean; G2, G5, G6 PARTIALLY RESOLVED; G9, G10 STILL UNRESOLVED — bound to code release). Inventory updated in entity-4.

**Files added:**
- `02 Wiki/(C) entity-5-build-architecture.md` — Cloud Run + Firestore + BigQuery + Looker + Vertex AI; primitives table with transcript anchors; component-by-component verified table; ASCII architecture diagram
- `02 Wiki/(C) entity-6-role-decomposition.md` — the 5 hats with traditional-vs-Claude responsibility, hand-off discipline, role-decomposition-as-demo-organization pattern candidate observation (N=1)
- `02 Wiki/(C) entity-7-step-by-step-build.md` — 21-row chronological table classifying each minute as demo/slide/transition; reproduction-recipe quality assessment; pacing observation (substantive build ~14 of 26 min)
- `02 Wiki/(C) entity-8-pitfalls-and-simplifications.md` — 5 speaker-acknowledged simplifications (S1-S5) + 10 unspoken gaps (U1-U10) + reproduction-readiness verdict + Storm Bear pilot relevance section
- `02 Wiki/(C) transcript-raw.md` — full cleaned transcript with provenance header

**Files updated:**
- `02 Wiki/(C) index.md` — entity list expanded 4→8, citation table includes transcript, completeness status flipped from "scaffold" → "transcript-deep", added quick-reference build summary
- `02 Wiki/(C) entity-4-content-gaps-and-ingest-path.md` — gap inventory updated with resolution status per gap; renamed "Ingest options" → "Original ingest options" (Option B chosen, marked DONE)
- `CLAUDE.md` — "Honest content gap" section retitled to "Content depth — TRANSCRIPT-DEEP"; folder-layout reflects new files; operator next-step options replaced (stop / find code release / pilot the architecture)

**Pattern Library impact:** still NONE on existing patterns (subject still out-of-typology). NEW observation registered: **"role-decomposition as live-demo organization"** (N=1 — 5 sequential hats, each compressed to one Claude affordance). Recorded in entity-6 + entity-8; carry-forward to next mini-audit if sister demo independently uses the structural device.

**Routine v2.3 codification candidates UPDATED:**
1. ~~NEW typology tier "T6 Knowledge-Source — Conference Talk / Workshop"~~ — still a candidate
2. ~~Transcript-ingest-as-required-Phase for video subjects~~ — VALIDATED in practice this session; if vault adds T6 typology this becomes a routine-required phase
3. ~~Pre-flight transcript availability check~~ — VALIDATED (used `which yt-dlp` + version check before commitment)
4. ~~Localized-entry-point → original-language-resolution discipline~~ — VALIDATED (Vietnamese cut → English original → transcript)
5. **NEW: VTT-cleaning recipe** — `awk` pipeline + dedup logic is reusable. Worth a Phase-X-style codification with the exact cleaning rules (header strip / align-cue strip / inline-timing strip / exact-line dedup / rolling-window dedup / 30s timestamp interval).

**Time budget used (this session):** 4 Bash tool calls (yt-dlp + awk cleaning) + 5 Write tool calls (4 entity pages + transcript) + 6 Edit tool calls (index, entity-4, CLAUDE.md, log). Estimated 25-min of Claude-time. Total wiki budget (both sessions): ~40 min.

**Verdict:** wiki is now transcript-deep. Reproduction depth would require the code release (G9). Vault state remains untouched (subject out-of-typology). Untracked status preserved — ready for commit if operator elects.
