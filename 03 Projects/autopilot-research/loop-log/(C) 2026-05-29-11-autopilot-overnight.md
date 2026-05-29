# (C) Autopilot Loop — 2026-05-29-11

> **Mode:** Path A (mechanical Python orchestrator + Phase-3-7 compile by Claude)
> **Trigger:** **/loop autopilot research about claude cowork and refer this video https://www.youtube.com/watch?v=zxdI5bWcnGs** (manual operator-initiated, not unattended launchd)
> **Topic:** Claude Cowork — Anthropic scheduled-agent feature
> **Anchor URL:** https://www.youtube.com/watch?v=zxdI5bWcnGs (Vietnamese tutorial — Duy Luân Dễ Thương)
> **Started:** 2026-05-29 11:18 (Phase 0 pre-flight) → drain phase 11:20–11:24 → compile + audit + log 11:24–11:50
> **Worktree:** /Users/Cvtot/KJ-OS-autopilot (autopilot-research tip = 2d5949b post-merge)

---

## Raw run log

```
[11:20:47] === Autopilot drain start 2026-05-29 ===
[11:20:47] AUTOPILOT_ROOT: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research
[11:20:47] queue: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/topics-queue.md
[11:20:47] pending topics: 1
[11:20:47]   1. Claude Cowork — Anthropic scheduled-agent feature (+ 1 anchor)
[11:20:47] will drain: 1
[11:20:47] --- Drain: Claude Cowork — Anthropic scheduled-agent feature
[11:20:47]   query: Claude Cowork scheduled agent Anthropic cron automation
[11:20:47]   slug:  claude-cowork-anthropic-scheduled-agent-feature
[11:20:47]   anchors: 1 URL(s) declared — will force-include
[11:20:47]   step 0/5: probe anchor URLs
[11:20:57]     ✓ anchor: [20260525] Cách hẹn giờ để AI tự chạy task cho bạn (Claude Cowork) — Duy Luân Dễ Thương (9,220 views)
[11:20:57]   step 1/5: yt-search (filling 5 of 6 slots; 1 from anchors)
[11:22:04]     got 11 videos
[11:22:04]   step 2/5: select top sources
[11:22:04]     picked 6 (1 anchor + 5 yt-search):
[11:22:04]       1. [ANCHOR] [20260525] Cách hẹn giờ để AI tự chạy task cho bạn (Claude Cowork) — Duy Luân Dễ Thương (9,220 views)
[11:22:04]       2. [20260316] Claude Cowork Full Tutorial: How to Use Claude Cowork Better — Bart Slodyczka (289,837 views)
[11:22:04]       3. [20260305] Your First Scheduled Task in Claude Cowork (Live Build) — Stefan Wirth - AI without the BS (2,631 views)
[11:22:04]       4. [20260228] Claude Code & Cowork Now Run 24/7 — Scheduled Tasks — Kenny Liao (8,104 views)
[11:22:04]       5. [20260310] Claude Cowork FULL COURSE (Automate Everything) — Jack Roberts (117,492 views)
[11:22:04]       6. [20260331] Claude Cowork - Full Course for Beginners — Tech With Tim (130,344 views)
[11:22:04]   step 3/5: notebooklm bundle
[11:22:08]     notebook: f851b538-c0cb-405f-9a8b-c46837464930
[11:22:43]     added 6/6 sources
[11:22:43]   step 4/5: wait for ready
[11:22:48]   step 5/5: analysis (1 summary + 4 asks)
[11:22:55]     asking: Trends
[11:23:21]     asking: Outliers
[11:23:45]     asking: Gaps
[11:24:11]     asking: Takeaways
[11:24:32]   ✅ wrote /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md (18,653 bytes)
[11:24:32] --- updating queue (1 drained)
[11:24:32]   queue updated
[11:24:32] === Done. drained=1 of 1 ===
```

---

## Phase 3 — Compile (manual, by Claude)

The drain script ends at raw-file write. Compile (raw → wiki) is the librarian's job per `CLAUDE.md` rules. Performed 11:24–11:50.

**Topic decision:** NEW topic folder `wiki/claude-cowork/` (no existing claude-cowork topic in `_master-index.md`; closest related is `autonomous-loops-human-in-the-loop` which covers the broader HITL pattern but not Cowork specifically).

**Articles written (9 total):**

| File | Purpose |
|---|---|
| `wiki/claude-cowork/_index.md` | Topic entry point; lists all articles + cross-links to 5 sibling topics + 2 Storm Bear cross-links + 4 key topical observations |
| `wiki/claude-cowork/overview.md` | What Claude Cowork is; 3-way Cowork-vs-Code-vs-Chat taxonomy disagreements; pricing posture (Jack's "$200 = headcount" reframe) |
| `wiki/claude-cowork/contextual-engineering.md` | 4 patterns for persistent `.md` brain files (minimalist / specialist / strategic-injection / Kenny Liao's automated brain-dump) |
| `wiki/claude-cowork/sandboxing-and-workspace-structure.md` | Bart's 3-folder workspace structure (context/projects/output) + Tech With Tim's irreversibility warning |
| `wiki/claude-cowork/mcp-connectors-landscape.md` | Recurring table-stakes (Google + Notion + Gmail) + specialist long tail (Linear / Mercury / Fireflies / Playwright / custom Context-OS) + RPA fallback pattern (Vietnamese anchor) |
| `wiki/claude-cowork/scheduling-and-the-app-open-constraint.md` | The core limitation (4 of 6 speakers cite); Kenny Liao's cron-plugin workaround; Jack Roberts's Railway alternative; comparison table; vault `/schedule` analog |
| `wiki/claude-cowork/skills-to-plugins-pipeline.md` | Codify-after-success pattern + Jack's "handover test" + Tech With Tim's "skills are Markdown" framing; vault analog at `05 Skills/` |
| `wiki/claude-cowork/token-and-cost-management.md` | Sonnet-default consensus (N=3+) + Bart's script-in-skill + Tim's parallel sub-agents + Jack's session cycling + Jack's headcount reframe; synthesized decision tree |
| `wiki/claude-cowork/production-readiness-gaps.md` | 5 gap areas (resilience / security / version-control / infra / telemetry) + 7 recommended follow-up topics for future drains |
| `wiki/claude-cowork/takeaways.md` | The 9 actionable rules from raw §Takeaways + 1 implicit (Sonnet-default) + how the vault itself satisfies many of them |

**`_master-index.md` updated:** added claude-cowork section at end with rich one-paragraph description capturing cross-source synthesis points (3-way taxonomy disagreement, app-open constraint, 4 context patterns including Kenny's outlier, handover-test, Sonnet-default consensus, production-readiness gaps).

**Raw file marked compiled:** `<!-- compiled: 2026-05-29 -->` appended to first heading line.

**`raw/_inventory.md` row added (constitutional rule #8):** The drain script does NOT auto-update inventory — added manually for this run. Row marks status=compiled with full sources list + NotebookLM ID + wiki link.

---

## Phase 4 — Cross-link

**In-topic links (intra-wiki):** 8 articles cross-link bidirectionally via `[[wiki link]]` syntax. Each topic article links back to `_index` + `overview` + 2-3 closest siblings.

**Cross-topic links to existing autopilot wiki:**
- `[[../autonomous-loops-human-in-the-loop/_index]]` — Cowork is the first-party desktop instance of the broader HITL pattern
- `[[../agent-dashboard-os/_index]]` — fills the telemetry gap explicitly called out in production-readiness-gaps
- `[[../harness-engineering/_index]]` — Cowork sits at the consumer-end of the harness spectrum
- `[[../10x-claude-code/_index]]` — productivity-multiplier framing overlap
- `[[../claude-md-12-rules/_index]]` — same `.md`-as-behavioral-contract pattern at developer scale

**Cross-vault links (Storm Bear curated wiki):** 5 `[[external|Storm Bear: <topic>]]` references (per `../CLAUDE.md` cross-vault link policy):
- Storm Bear: AutoGPT (v59) — first-party AI-employee framing predecessor
- Storm Bear: Building with Claude on Google Cloud (talk wiki) — developer-layer composition (just committed onto autopilot-research at 4dc6484 → merged at 2d5949b)
- Storm Bear: Setting up /loop + /schedule — vault docs on the scheduling alternatives
- Storm Bear: CLAUDE.md librarian discipline + autopilot-research scope-clamp
- Storm Bear: 05 Skills/ curation cycle + agent-skills-standard (v76)

**Dedupe check:** no >70% title-similarity duplicates against existing topics. claude-cowork is structurally distinct from autonomous-loops-human-in-the-loop (Cowork = the product; autonomous-loops = the pattern abstraction).

---

## Phase 5 — Audit (gap metric)

**Gaps at start (cold-start for this topic):** 1 (the topic itself didn't exist in `wiki/_master-index.md`)

**Gaps at end:**
- 0 stub articles (all 9 are full-length, bullet-dense, 5+ bullet "Key Takeaways" each)
- 0 `(gap)` / `(TODO)` / `(stub)` markers in `_index.md` or in any article
- 0 articles citing sources that weren't compiled (all 6 sources from the NotebookLM bundle are cited across the 9 articles)

**`gaps_closed_ratio` = (1 - 0) / max(1, 1) = 1.0**

(Cold-start case per routine "Edge cases" — gap of 1 closed cleanly.)

**Top-3 surviving unclosed gaps (not stub-marked but identified by Claude as next-cycle work):**

1. **Anthropic first-party documentation** for Cowork is NOT in the corpus (yt-search rubric only surfaces YouTube). A 3-webfetch ingest of `claude.com/cowork` (or wherever Anthropic officially documents it) would let us replace speaker-guess about taxonomy with first-party canonical positioning.
2. **Quantitative cost data** absent (no speaker says "this scheduled task costs $X/day"). A pilot deployment + telemetry capture could fill this.
3. **Cross-validation against `setup-cowork` Anthropic-skill** — that skill exists in this session's skill registry but its content isn't ingested. A 6-custom-scraper or 5-yt-dlp-only pull of the skill's docs would close the gap between this wiki's external-creator-view and Anthropic's intended-onboarding-view.

---

## Phase 6 — Decide (stop conditions)

| Stop condition | Status |
|---|---|
| `gaps_closed_ratio` ≥ 0.5 (target for /loop) | ✓ MET (1.0) |
| `cycles_completed` ≥ 5 (max-cycles default) | 1 cycle |
| `wall_clock_used` ≥ 60min | ~30min |
| `notebooklm_calls_total` ≥ budget | 6 (anchor probe) + 11 (yt-search) + 6 (source-add) + 5 (analysis) = ~28 |
| `_master-index.md` unchanged 2 consecutive cycles | N/A (cold-start) |

**Decision: STOP.** Primary stop reason: `gaps_closed_ratio` target met cleanly. No need for another drain cycle.

---

## Phase 7 — Log + checkpoint

This loop log file is the artifact (constitutional rule #2 satisfied).

**Git checkpoint deferred** — operator will commit explicitly per project convention (vault rule "ONLY commit when explicitly asked"). Files staged for review:
- `raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md` (drain output, compile-marker added)
- `raw/topics-queue.md` (modified by drain script — topic moved to Completed)
- `raw/_inventory.md` (manual row added — constitutional rule #8)
- `wiki/_master-index.md` (claude-cowork topic added)
- `wiki/claude-cowork/` (NEW folder — 9 .md files)
- `loop-log/(C) 2026-05-29-11-autopilot-overnight.md` (this file)

---

## Final metrics

- **Topic:** Claude Cowork — Anthropic scheduled-agent feature
- **`gaps_closed_ratio`:** 1.0
- **Sources ingested:** 6 YouTube videos (1 anchor preserved + 5 yt-search)
- **Wiki articles produced:** 9 (1 _index + 8 topic articles)
- **Cross-links:** 5 sibling autopilot topics + 5 external Storm Bear references
- **NotebookLM notebook:** `f851b538-c0cb-405f-9a8b-c46837464930`
- **Anchor mechanism status:** **WORKED CLEANLY** — Vietnamese anchor URL force-included at slot 1; 0 anchor-miss (closes 2026-05-13 / 2026-05-14 anchor-miss incidents AS the 4th post-fix drain to demonstrate the fix)
- **Time:** ~30 min total (drain ~4 min + compile ~25 min by Claude)
- **Stop reason:** `gaps_closed_ratio = 1.0 ≥ target 0.5`

---

## Suggested next action (per Storm Bear prime directive — don't repeat the same mistake twice)

**Operator decisions pending:**

1. **Commit the wiki?** 6 new/modified files + 9 new articles ready to stage. Recommended: yes, with a clean message reflecting "autopilot-research: claude-cowork wiki" convention.
2. **Queue follow-up topic for Anthropic first-party Cowork docs?** Currently 100% of corpus is YouTube speakers; first-party docs would tighten the taxonomy section and let us replace speaker-disagreement with canonical positioning. Suggested queue entry: `Anthropic Cowork official documentation + setup-cowork skill content`.
3. **Pilot the Cowork product** as a Storm Bear pilot ranked alongside cc-sdd + codex-plugin-cc + free-claude-code? Would generate the quantitative cost data the corpus lacks (Phase 5 surviving gap #2).
4. **Promote to Storm Bear curated wiki?** Not yet — single drain, 1-day-old topic, needs 2+ audit cycles per `04 Reviews/` promotion criteria. Re-evaluate after a 2nd sibling drain or at next mini-audit.
