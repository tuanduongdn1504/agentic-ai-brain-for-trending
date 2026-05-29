# (C) Autopilot Loop — 2026-05-29-12 (SECOND drain — AI Operating System)

> **Mode:** Path A (mechanical Python orchestrator + Phase-3-7 compile by Claude)
> **Trigger:** **/loop autopilot research about refer this video https://www.youtube.com/watch?v=zElKhlFkqU4** (manual operator-initiated, 2nd /loop of session). Operator gave URL only; topic phrase "AI Operating System — 5-skills framework" derived from anchor video title.
> **Topic:** AI Operating System — 5-skills framework
> **Anchor URL:** https://www.youtube.com/watch?v=zElKhlFkqU4 (Ben AI — "5 Skills to Build an AI Operating System Like The 1% (Full Guide)")
> **Started:** 2026-05-29 11:49 (dry-run) → 11:51 full drain → 11:56 raw write → compile/audit/log to ~12:30
> **Worktree:** /Users/Cvtot/KJ-OS-autopilot
> **Sibling drain:** This is the SECOND drain in this session. The first (claude-cowork) ran 11:18–11:50 and was committed at aa7f7f9 with its own loop-log file at `(C) 2026-05-29-11-autopilot-overnight.md`. The drain script's hour-stamped filename would have collided — both drains finished in hour 11. To preserve separate audit trails, this file was manually renamed from the colliding `-11-` name to `-12-` (reflecting completion-by-compile time ~12:30). Same-hour drain collision worth flagging as a drain-script papercut for future fix.

---

## Raw run log

```
[11:51:31] === Autopilot drain start 2026-05-29 ===
[11:51:31] AUTOPILOT_ROOT: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research
[11:51:31] queue: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/topics-queue.md
[11:51:31] pending topics: 2
[11:51:31]   1. AI Operating System — 5-skills framework (+ 1 anchor)
[11:51:31]   2. Anthropic Cowork first-party documentation + setup-cowork skill
[11:51:31] will drain: 1
[11:51:31] --- Drain: AI Operating System — 5-skills framework
[11:51:31]   query: AI Operating System 5 skills personal agent stack build
[11:51:31]   slug:  ai-operating-system-5-skills-framework
[11:51:31]   anchors: 1 URL(s) declared — will force-include
[11:51:31]   step 0/5: probe anchor URLs
[11:51:41]     ✓ anchor: [20260516] 5 Skills to Build an AI Operating System Like The 1% (Full G — Ben AI (33,484 views)
[11:51:41]   step 1/5: yt-search (filling 5 of 6 slots; 1 from anchors)
[11:52:52]     got 13 videos
[11:52:52]   step 2/5: select top sources
[11:52:52]     picked 6 (1 anchor + 5 yt-search):
[11:52:52]       1. [ANCHOR] [20260516] 5 Skills to Build an AI Operating System Like The 1% (Full G — Ben AI (33,484 views)
[11:52:52]       2. [20260319] I Built 5 AI Employees With OpenClaw (Here's How) — Mani Kanasani (127,325 views)
[11:52:52]       3. [20260408] How AI agents & Claude skills work (Clearly Explained) — Greg Isenberg (429,594 views)
[11:52:52]       4. [20260317] Building AI Agents that actually work (Full Course) — Greg Isenberg (427,644 views)
[11:52:52]       5. [20260502] Creating Your Own Agentic OS is Easy (Insanely Powerful) — Simon Scrapes (54,274 views)
[11:52:52]       6. [20260312] 7 new open source AI tools you need right now… — Fireship (840,913 views)
[11:52:52]   step 3/5: notebooklm bundle
[11:52:56]     notebook: 1f5811fb-60c1-4857-a039-c784508b2ec4
[11:53:34]     added 6/6 sources
[11:53:34]   step 4/5: wait for ready
[11:53:38]   step 5/5: analysis (1 summary + 4 asks)
[11:53:46]     asking: Trends
[11:54:29]     asking: Outliers
[11:54:59]     asking: Gaps
[11:55:29]     asking: Takeaways
[11:56:00]   ✅ wrote /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/2026-05-29-ai-operating-system-5-skills-framework.md (19,201 bytes)
[11:56:00] --- updating queue (1 drained)
[11:56:00]   queue updated
[11:56:00] === Done. drained=1 of 1 ===
```

---

## Phase 3 — Compile (manual, by Claude)

Drain ends at raw-file write; compile is the librarian's job.

**Topic decision:** NEW topic folder `wiki/ai-operating-system/` (no existing topic; closest sibling is `claude-cowork` for the consumer-product layer of this same architectural pattern).

**Articles written (9 total = 1 _index + 8 topic articles):**

| File | Lines | Purpose |
|---|---|---|
| `wiki/ai-operating-system/_index.md` | 47 | Topic entry point + cross-links to 6 autopilot siblings + 4 Storm Bear externals + 6 cross-source observations |
| `wiki/ai-operating-system/overview.md` | 75 | Agentic OS framing; 8-practitioner table; AIOS-vs-Cowork-vs-Code differentiation; tooling landscape |
| `wiki/ai-operating-system/instruction-layer-markdown-files.md` | 80 | claude.md/agents.md/soul.md/identity.md/user.md hierarchy; Mani's 3-file split; Ross Mike's "95% don't need this" outlier + reconciliation matrix |
| `wiki/ai-operating-system/skills-architecture-progressive-disclosure.md` | 100 | Skills-as-SOPs (Remy); progressive disclosure (Simon/Ross Mike); build-via-failure (Ross Mike); skill chaining (Simon); skillception |
| `wiki/ai-operating-system/memory-and-context-rot.md` | 110 | Context rot problem; Simon's 6-level taxonomy; Open Viking (Fireship); Ben AI's OS Optimizer; vault `_state/` as level-1-4 instance |
| `wiki/ai-operating-system/builder-orchestrator-executor-pattern.md` | 100 | Mani's 3-role framework; Kanban orchestration (Mani+Simon); Observe-Think-Act (Remy); chef-vs-vending-machine framing |
| `wiki/ai-operating-system/security-philosophies-and-sandboxing.md` | 95 | Conservative access (Ross Mike+Remy) vs infrastructure-led (Mani's NemoClaw); decision matrix; prompt-injection-via-MCP attack |
| `wiki/ai-operating-system/off-the-shelf-vs-handbuilt-skills.md` | 95 | Sharpest disagreement axis; Ross Mike's "stars-only" critique; falsifiability tests; gradient (mechanical vs domain skills) |
| `wiki/ai-operating-system/production-readiness-gaps.md` | 95 | 5 enterprise gaps (scalability/compliance/version-control/error-handling/multi-model); **5 of 6 gaps overlap with sister Cowork corpus** |
| `wiki/ai-operating-system/takeaways.md` | 115 | 10 actionable rules + vault-application audit (vault satisfies 8 of 10) + cross-topic synthesis with Cowork 9-rule list |

**Total:** ~810 lines of wiki content from 19 KB raw.

**`_master-index.md` updated:** added `ai-operating-system` section BEFORE the existing `claude-cowork` section (alphabetic + sibling-topic ordering preserves the pattern).

**Raw file marked compiled:** `<!-- compiled: 2026-05-29 -->` appended to first heading line.

**`raw/_inventory.md` row added:** Per constitutional rule #8. Row captures: 6-source bundle including Greg Isenberg ×2 (channel-cap-2 use), Fireship-bumped-Nick-Saraev note (different yt-search rank between dry-run and full drain), full NotebookLM ID, wiki link.

---

## Phase 4 — Cross-link

**Intra-topic links:** 8 articles cross-link bidirectionally via `[[wiki link]]`. Each topic article links back to `_index` + `overview` + 2-3 closest siblings within the topic.

**Cross-topic links to existing autopilot wiki (6 topics — highest cross-link density of any AIOS-related drain):**
- `[[../claude-cowork/_index]]` — **SISTER TOPIC**, heavily cross-referenced
- `[[../claude-md-12-rules/_index]]` — `.md` behavioral-contract pattern
- `[[../harness-engineering/_index]]` — org-scale variant
- `[[../10x-claude-code/_index]]` — productivity framing overlap
- `[[../autonomous-loops-human-in-the-loop/_index]]` — observe-think-act loop pattern
- `[[../claude-code-clones/_index]]` — OpenClaw load-bearing in this corpus

**Cross-vault links to Storm Bear curated wiki (4 — per autopilot-research/CLAUDE.md format):**
- `[[external|Storm Bear: agent-skills-standard (v76)]]` — codified portable-skill format
- `[[external|Storm Bear: AutoGPT (v59)]]` — pre-Anthropic AI-employee framing predecessor
- `[[external|Storm Bear: cc-sdd (v61)]]` — SDD-discipline-as-skill-architecture
- `[[external|Storm Bear: ECC (v78)]]` — 232-skill operator system as Camp A's maximal expression (off-the-shelf-vs-handbuilt-skills cross-link)

**Dedupe check:** no >70% title-similarity duplicates. ai-operating-system is structurally distinct from claude-cowork (this = builder layer; that = product layer) — confirmed via overview.md side-by-side table.

---

## Phase 5 — Audit (gap metric)

**Gaps at start (cold-start for this topic):** 1 (topic didn't exist in `_master-index.md`)

**Gaps at end:**
- 0 stub articles (all 9 are full-length with Key Takeaways sections)
- 0 `(gap)` / `(TODO)` / `(stub)` markers in `_index.md` or articles
- 0 articles citing sources not in the bundle

**`gaps_closed_ratio` = (1 - 0) / max(1, 1) = 1.0**

(Cold-start case per routine "Edge cases" — gap of 1 closed cleanly.)

**Top-3 surviving unclosed gaps (carry-forward):**

1. **OpenClaw deep-dive** — Mani Kanasani's content is OpenClaw-heavy but the corpus doesn't unpack OpenClaw's specific architecture. Would benefit from a dedicated drain. Related to existing topic [[../claude-code-clones/_index]] which mentions OpenClaw but not deeply.
2. **Open Viking evaluation** — Fireship's source is the weakest in the bundle (6 min listicle). Open Viking deserves a dedicated drain to evaluate against vector-DB alternatives.
3. **Nick Saraev's 4-hour course** — was in dry-run selection but bumped by Fireship in the actual drain. The most-viewed video (1.78M) in the bundle that didn't make it. Worth a focused drain on its content alone (yt-pipeline with 1 anchor + tight query).

---

## Phase 6 — Decide (stop conditions)

| Stop condition | Status |
|---|---|
| `gaps_closed_ratio` ≥ 0.5 | ✓ MET (1.0) |
| `cycles_completed` ≥ 5 | 1 cycle |
| `wall_clock_used` ≥ 60min | ~45min |
| `notebooklm_calls_total` ≥ budget | ~28 calls (similar to claude-cowork drain) |
| `_master-index.md` unchanged 2 consecutive cycles | N/A (cold-start) |

**Decision: STOP.** Primary stop reason: `gaps_closed_ratio` target met cleanly.

---

## Phase 7 — Log + checkpoint

This loop log file is the artifact.

**Pending operator action:** commit. Files staged for review:
- `raw/2026-05-29-ai-operating-system-5-skills-framework.md` (drain output, compile-marker added)
- `raw/topics-queue.md` (auto-modified by drain — topic moved to Completed)
- `raw/_inventory.md` (manual row added)
- `wiki/_master-index.md` (ai-operating-system section added before claude-cowork)
- `wiki/ai-operating-system/` (NEW folder — 9 .md files)
- `loop-log/(C) 2026-05-29-11-autopilot-overnight.md` (this file)

---

## Final metrics

- **Topic:** AI Operating System — 5-skills framework
- **`gaps_closed_ratio`:** 1.0
- **Sources ingested:** 6 YouTube videos (1 anchor preserved + 5 yt-search)
- **Wiki articles produced:** 9 (1 _index + 8 topic articles, ~810 lines)
- **Cross-links:** 6 sibling autopilot topics (highest of any drain in this session) + 4 external Storm Bear references
- **NotebookLM notebook:** `1f5811fb-60c1-4857-a039-c784508b2ec4`
- **Anchor mechanism status:** **WORKED CLEANLY** — operator's URL force-included at slot 1; 0 anchor-miss
- **Selection drift:** Nick Saraev (1.78M views) appeared in dry-run but was bumped by Fireship in full drain (slightly different yt-search rank ordering between dry-run 14 results vs full-drain 13 results). Documented for transparency
- **Time:** ~45 min total (drain ~7 min including dry-run + compile ~38 min by Claude)
- **Stop reason:** `gaps_closed_ratio = 1.0 ≥ target 0.5`

---

## Suggested next action

**Operator decisions pending:**

1. **Commit the wiki?** Standard pattern matching the previous claude-cowork commit (aa7f7f9). Recommended.
2. **Queue follow-up topic for Nick Saraev 4-hour course?** — 1.78M views, was in dry-run but bumped. Single-anchor focused drain would recover this content.
3. **Queue follow-up topic for OpenClaw deep-dive?** — Mani Kanasani's content is OpenClaw-heavy; the architecture deserves its own coverage rather than being a load-bearing-but-unexamined tool in this wiki.
4. **Queue follow-up topic for Open Viking?** — agent-memory DB with file-system-as-memory philosophy; corpus source is weak (Fireship 6-min listicle) but the concept is interesting.
5. **Promote to Storm Bear?** Not yet — single drain. Re-evaluate after 1 more sibling drain or at next mini-audit. This + claude-cowork forms a 2-drain "personal AI OS" sub-corpus that's approaching promotion-readiness.
