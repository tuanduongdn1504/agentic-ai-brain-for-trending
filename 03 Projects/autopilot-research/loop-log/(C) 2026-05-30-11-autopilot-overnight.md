# (C) Autopilot Loop — 2026-05-30-11 (harness-engineering getting-started)

> **Mode:** Path A (mechanical Python orchestrator + Phase 3-7 compile by Claude)
> **Trigger:** **/loop autopilot research about refer this video https://www.youtube.com/watch?v=gQLhchHmRKs** (manual operator-initiated). Operator gave URL only; topic phrase "Harness Engineering — getting started / beginner introduction (Vietnamese anchor)" derived from anchor video title.
> **Topic:** Harness Engineering — getting started (extends existing wiki/harness-engineering/ topic)
> **Anchor URL:** https://www.youtube.com/watch?v=gQLhchHmRKs (Tù Bà Khuỳm — "Bắt đầu Harness Engineering từ đâu? Từ đây!!")
> **Started:** 2026-05-30 11:55 (dry-run) → 11:56 full drain → 11:59 raw write → compile/audit/log to ~12:30
> **Worktree:** /Users/Cvtot/KJ-OS-autopilot

---

## Raw run log

```
[11:56:45] === Autopilot drain start 2026-05-30 ===
[11:56:45] AUTOPILOT_ROOT: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research
[11:56:45] queue: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/topics-queue.md
[11:56:45] pending topics: 1
[11:56:45]   1. Harness Engineering — getting started / beginner introduction (Vietnamese anchor) (+ 1 anchor)
[11:56:45] will drain: 1
[11:56:45] --- Drain: Harness Engineering — getting started / beginner introduction (Vietnamese anchor)
[11:56:45]   query: harness engineering beginner introduction getting started Claude Code
[11:56:45]   slug:  harness-engineering-getting-started-beginner-intro
[11:56:45]   anchors: 1 URL(s) declared — will force-include
[11:56:45]   step 0/5: probe anchor URLs
[11:56:51]     ✓ anchor: [20260530] Bắt đầu Harness Engineering từ đâu? Từ đây!! — Tù Bà Khuỳm (469 views)
[11:56:51]   step 1/5: yt-search (filling 5 of 6 slots; 1 from anchors)
[11:57:46]     got 15 videos
[11:57:46]   step 2/5: select top sources
[11:57:46]     picked 6 (1 anchor + 5 yt-search):
[11:57:46]       1. [ANCHOR] [20260530] Bắt đầu Harness Engineering từ đâu? Từ đây!! — Tù Bà Khuỳm (469 views)
[11:57:46]       2. [20260207] How I use Claude Code (Meta Staff Engineer Tips) — John Kim (435,040 views)
[11:57:46]       3. [20251217] How I Start EVERY Claude Code Project — AI with Avthar (113,587 views)
[11:57:46]       4. [20260413] FULL Claude Tutorial For Beginners in 2026! (FULL COURSE) — Productive Dude (423,842 views)
[11:57:46]       5. [20260405] How I use Claude Code (Senior Software Engineer Tips) — Maddy Zhang (138,116 views)
[11:57:46]       6. [20260522] Agent Harness explained in 8min.. — Caleb Writes Code (114,644 views)
[11:57:46]   step 3/5: notebooklm bundle
[11:57:48]     notebook: 4c7d51e4-b450-4504-933b-3bb4be28b393
[11:58:14]     added 6/6 sources
[11:58:14]   step 4/5: wait for ready
[11:58:16]   step 5/5: analysis (1 summary + 4 asks)
[11:58:22]     asking: Trends
[11:58:48]     asking: Outliers
[11:59:08]     asking: Gaps
[11:59:31]     asking: Takeaways
[11:59:50]   ✅ wrote /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/2026-05-30-harness-engineering-getting-started-beginner-intro.md (18,304 bytes)
[11:59:50] --- updating queue (1 drained)
[11:59:51]   queue updated
[11:59:51] === Done. drained=1 of 1 ===
```

---

## Phase 3 — Compile (manual, by Claude)

**Topic decision: EXTEND existing `wiki/harness-engineering/` topic** (already 22 articles, anchored on Ryan Lopopolo Symphony/Frontier + 8 individual-scale siblings). The anchor video is by Tù Bà Khuỳm — the same Vietnamese practitioner cited in prior siblings; this is his V2 harness with corpus-first contributions. NOT a new topic.

**Articles added (2 — bringing harness-engineering from 22 to 24 articles):**

1. **`personal-repo-tu-ba-khuym-getting-started.md`** (9th individual-scale sibling) — Tù Bà Khuỳm's beginner-introduction take. Focus on **CORPUS-FIRST SQLite-as-project-memory** (first non-Markdown approach in 22-article corpus). Closed loop on harness quality (traces → friction backlog → harness refinement). Vietnamese-pedagogy lens as corpus signal. V2 is more technically opinionated than 2026-05-13 V1 — SQLite + friction-tracking did NOT appear earlier.

2. **`getting-started-consensus-and-divergences.md`** (cross-cutting synthesis) — 6-speaker drain bundle map. **6 consensus items** (plan-first methodology N=5; claude.md as project brain N=6; validation hooks; git worktrees; MCP N=4; specialist sub-agents) + **6 divergence axes** (claude.md length 100/200/300; `/clear` vs resume; **John Kim's anti-MCP** corpus-strongest minority; Markdown vs SQLite; Starcraft-juggling vs git-worktrees; Artifacts-only vs inline). **CORPUS-FIRST: 3 competing proprietary prompting frameworks emerge in one drain** — GCAO (Productive Dude) + DBS (Productive Dude) + PSB (AI with Avthar). Proprietary-framework-branding-maturity-stage observation.

**`_index.md` updated:** added 2026-05-30 extension note + new subsection "Individual-scale 9th sibling + cross-cutting consensus-and-divergences (added 2026-05-30)" + article count bumped 22→24 + promotion-candidacy flagged.

**`_master-index.md` updated:** appended 2026-05-30 extension to existing harness-engineering paragraph + final article count 22→24 + promotion-candidacy note for next mini-audit (v66+).

**Raw file marked compiled:** `<!-- compiled: 2026-05-30 -->` appended.

**`raw/_inventory.md` row added:** captures 6-source bundle (Tù Bà Khuỳm anchor + 5 yt-search picks: John Kim Meta / AI with Avthar / Productive Dude / Maddy Zhang / Caleb Writes Code), NotebookLM ID, wiki link to existing harness-engineering topic, EXTENSION status.

---

## Phase 4 — Cross-link

**In-topic links:** Both new articles cross-link bidirectionally + back to existing harness-engineering siblings (`_index` / `personal-repo-overview` / `personal-repo-patterns` / `personal-repo-gaps` / `contrarian-stances` / `anchor-bundle-overview`).

**Cross-topic links (to other autopilot wiki):**
- `[[../ai-operating-system/memory-and-context-rot]]` — SQLite-as-memory slots at level 4-5 of Simon Scrapes's 6-level taxonomy (sister-topic cross-reference)
- `[[../ai-operating-system/instruction-layer-markdown-files]]` — same `.md` hierarchy pattern with the SQLite-divergence
- `[[../claude-md-12-rules/_index]]` — vault's behavioral-contract framework at a different abstraction level

**Cross-vault links to Storm Bear (external):** None new added; existing harness-engineering cross-vault links remain intact.

**Dedupe check:** no >70% title-similarity duplicates. New articles are structurally distinct from existing 22.

**Carry-forward — articles NOT updated but flagged for future:**
- `contrarian-stances.md` — should add John Kim's anti-MCP stance + Tù Bà Khuỳm's anti-Markdown stance
- `cited-references.md` — should add 5 new speakers + Maddy Zhang's 100-200-line claude.md ceiling
- `personal-repo-patterns.md` — should fold in PSB system, GCAO/DBS frameworks, SQLite-trace pattern
- `open-questions.md` — should add: SQLite schema migration / multi-machine sync / cross-project memory / version control for SQLite memory

Flagged for next ingest cycle rather than touched this pass to keep commit scope tight.

---

## Phase 5 — Audit (gap metric)

This is an EXTENSION not a cold-start, so gap accounting is different:

**Gaps at start:** 0 stub markers / 0 TODOs in the existing harness-engineering topic. Topic was healthy.

**Gaps at end:**
- 0 new stub markers
- 0 new `(gap)` / `(TODO)` markers
- 0 articles citing sources not in bundle

**However**, this drain identified 4 structural-file updates that ARE pending (listed in §Carry-forward above). These count as soft-gaps even though the new articles themselves are complete.

**`gaps_closed_ratio` computation for extension cycle:**

- Inputs: 6 new sources ingested. 2 new articles compiled. Existing topic article count 22 → 24.
- Per routine §Audit definitions, this is a positive-progress cycle: new sources fully synthesized into new articles, all consensus items + divergences mapped, corpus-first findings codified.
- No regression from existing topic state.
- `gaps_closed_ratio` ≈ 1.0 (extension fully synthesizes the new bundle).

**Top-3 surviving unclosed gaps (carry-forward):**

1. **Structural-file updates** (contrarian-stances / cited-references / personal-repo-patterns / open-questions) — pending; would consolidate findings into the topic's structural skeleton
2. **John Kim's anti-MCP stance** — covered in `getting-started-consensus-and-divergences` but should also be a first-class entry in `contrarian-stances.md`
3. **3 proprietary prompting frameworks** (GCAO/DBS/PSB) deserve their own article — currently lumped into the consensus-and-divergences article but warrant dedicated `prompting-frameworks-comparison.md` if a future drain surfaces N=2+ adoption signal

---

## Phase 6 — Decide (stop conditions)

| Stop condition | Status |
|---|---|
| `gaps_closed_ratio` ≥ 0.5 | ✓ MET (~1.0 extension-equivalent) |
| `cycles_completed` ≥ 5 | 1 cycle |
| `wall_clock_used` ≥ 60min | ~35min |
| `notebooklm_calls_total` ≥ budget | ~28 (similar to prior drains) |
| `_master-index.md` unchanged 2 consecutive cycles | N/A — modified this cycle |

**Decision: STOP.** Primary stop reason: gaps_closed_ratio target met cleanly. Structural-file updates are carry-forward, not blockers.

---

## Phase 7 — Log + checkpoint

This loop log is the artifact.

**Pending operator action:** commit. Files staged for review:
- `raw/2026-05-30-harness-engineering-getting-started-beginner-intro.md` (drain output, compile-marker added)
- `raw/topics-queue.md` (auto-modified by drain — topic moved to Completed)
- `raw/_inventory.md` (manual row added)
- `wiki/_master-index.md` (harness-engineering paragraph extended with 2026-05-30 note + count 22→24)
- `wiki/harness-engineering/_index.md` (article count bumped + new subsection)
- `wiki/harness-engineering/personal-repo-tu-ba-khuym-getting-started.md` (NEW)
- `wiki/harness-engineering/getting-started-consensus-and-divergences.md` (NEW)
- `loop-log/(C) 2026-05-30-11-autopilot-overnight.md` (this file)

ALSO sitting uncommitted from prior overnight cron (separate concern — not part of this /loop):
- `raw/2026-05-30-anthropic-cowork-first-party-documentation-setup-c.md` (overnight cron drained the Anthropic Cowork follow-up; raw exists, NOT yet compiled to wiki — pending separate compile session)
- `loop-log/(C) 2026-05-30-00-autopilot-overnight.md` (overnight cron log for that drain)

---

## Final metrics

- **Topic:** Harness Engineering — getting started (EXTENSION to existing topic)
- **`gaps_closed_ratio`:** ~1.0 (extension fully synthesizes new bundle)
- **Sources ingested:** 6 YouTube videos (1 anchor preserved + 5 yt-search)
- **Wiki articles produced:** 2 NEW (existing topic goes 22→24); ~330 lines total
- **Cross-links:** Heavy — both articles tie into the existing harness-engineering structure + cross-topic to ai-operating-system + claude-md-12-rules
- **NotebookLM notebook:** `4c7d51e4-b450-4504-933b-3bb4be28b393`
- **Anchor mechanism status:** **WORKED CLEANLY** — operator's URL force-included at slot 1; 0 anchor-miss (Tù Bà Khuỳm anchor preserved despite 469-view-only count — anchor-injection mechanism reliably ignores popularity rubric)
- **Time:** ~35 min (drain ~3 min + compile ~32 min)
- **Stop reason:** `gaps_closed_ratio = 1.0 ≥ target 0.5`

---

## CORPUS-FIRST findings this drain

1. **SQLite-as-project-memory** (Tù Bà Khuỳm V2) — first non-Markdown approach in the harness-engineering corpus
2. **3 competing proprietary prompting frameworks in ONE drain** — GCAO + DBS + PSB. Proprietary-framework-branding-maturity-stage observation worth a future Storm Bear pattern-library candidate.
3. **Maddy Zhang's 100-200-line claude.md ceiling** — tightest documented constraint in the corpus
4. **John Kim's "very very hard to NOT use MCPs"** — corpus-strongest minority position against MCP consensus
5. **Tù Bà Khuỳm's friction-tracking → backlog → harness-refinement loop** — closed loop on harness quality, distinct from but compatible with build-via-failure pattern

---

## Suggested next action

**Operator decisions pending:**

1. **Commit this drain?** Standard pattern. Recommended.
2. **Compile the stranded Anthropic Cowork raw** from overnight cron (~9 KB at `raw/2026-05-30-anthropic-cowork-first-party-documentation-setup-c.md`)? Closes the gap-#1-follow-up from claude-cowork wiki. Separate scope from this /loop.
3. **Structural-file updates** to harness-engineering topic — fold consensus-and-divergences findings into contrarian-stances + cited-references + personal-repo-patterns + open-questions (4 file edits, ~15-20 min). Could be a follow-up commit.
4. **Promotion-to-Storm-Bear audit** at v66+ mini-audit cadence — harness-engineering is now at 24 articles + cross-cohort coverage + N=6 consensus, approaching promotion criteria.
