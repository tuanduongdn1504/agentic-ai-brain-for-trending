# (C) Autopilot Compile Loop — 2026-05-14-08

> **Trigger:** manual `compile` verb (Storm Bear vault session)
> **Mode:** Phase 3-7 of `(C) autopilot-research-routine.md` (skipped Phase 0-2 — drain already done overnight)
> **Started:** 2026-05-14 ~08:00
> **Ended:** 2026-05-14 ~08:35
> **Duration:** ~35 min

---

## Per-cycle metrics

| Cycle | Sources | Topics before | Topics after | New articles | Notes |
|-------|---------|---------------|--------------|--------------|-------|
| 1 (this) | 6 raw bundles (33 YouTube videos total) | 7 | **12** (5 new + 1 extended + 6 prior) | 33 | All 6 raw files from 2026-05-13 overnight drain |

---

## Sources compiled

| # | Raw file | NotebookLM ID | Target wiki | Status flag |
|---|----------|---------------|-------------|-------------|
| 1 | `raw/2026-05-13-agent-dashboard-agent-os-claude-code-observability.md` | `54d7812d…` | `wiki/agent-dashboard-os/` | ⚠️ anchor-miss |
| 2 | `raw/2026-05-13-auto-loop-goals-with-human-in-the-loop.md` | `abe1647e…` | `wiki/autonomous-loops-human-in-the-loop/` | ⚠️ low-signal (recency relaxed) |
| 3 | `raw/2026-05-13-harness-engineering-personal-repo-continuation-vie.md` | `58c51d8e…` | `wiki/harness-engineering/` (extension; +4 articles) | ✅ on-target |
| 4 | `raw/2026-05-13-codex-long-running-agentic-harness-alternative-to.md` | `01707594…` | `wiki/codex/` | ⚠️ anchor-miss (all 3 anchors absent) |
| 5 | `raw/2026-05-13-open-source-claude-design-clones-alternative-agent.md` | `5155a280…` | `wiki/claude-code-clones/` | ⚠️ off-target (bundle is workflow-focused, not clone-focused) |
| 6 | `raw/2026-05-13-ai-daily-news-may-2026-weekly-snapshot.md` | `9f08f424…` | `wiki/ai-news-2026-w19/` | ⚠️ rumor-heavy (no first-party confirmation) |

---

## Wiki articles created / updated

### NEW topic folders (5)

- `wiki/agent-dashboard-os/` — 6 files: `_index.md` (52L) + `overview.md` (97L) + `core-patterns.md` (128L) + `expert-disagreements.md` (98L) + `practical-takeaways.md` (130L) + `gaps-and-followups.md` (165L) = 670L
- `wiki/autonomous-loops-human-in-the-loop/` — 6 files: 681L
- `wiki/codex/` — 6 files: 702L
- `wiki/claude-code-clones/` — 6 files: 589L
- `wiki/ai-news-2026-w19/` — 4 files (news snapshot, shallower): 228L

### EXTENDED topic (1)

- `wiki/harness-engineering/` — +4 articles (442L) — `personal-repo-overview.md` / `personal-repo-patterns.md` / `personal-repo-vs-org-scale.md` / `personal-repo-gaps.md` — alongside existing 10 org-scale articles. `_index.md` updated to bump article count 10→14 and add individual-scale vs org-scale comparison axis.

### Index files updated (2)

- `wiki/_master-index.md` — 5 new topic entries appended + harness-engineering description updated to reflect 14-article extension
- `raw/_inventory.md` — 6 rows: Status raw → compiled (with flag); Coverage summary footer: compiled 21→27, uncompiled 7→1

---

## Metric

- `articles_before`: ~36 (across 7 topics)
- `articles_after`: ~69 (across 12 topics)
- `gaps_closed_ratio` (proxy): N/A — this was a compile-of-drained-backlog, not a gap-closure cycle. All 6 raw bundles drained Status=raw → Status=compiled.

---

## ⚠️ CRITICAL META-FINDING — Anchor-Miss Pattern

**4 of 6 raw bundles failed to surface the user-provided anchor URLs.** The autopilot-drain.py yt-search auto-selection rubric (`log(views) + engagement_ratio × 3 + recency × 2` with channel-cap-2) is too weakly weighted toward operator-named anchors:

| Topic | User anchor | Actually picked |
|-------|-------------|-----------------|
| agent-dashboard-os | Chase AI "Claude Code Just Got a Dashboard" | LangSmith + OpenTelemetry + Tmux + Vercel sandbox + agentic RAG content |
| codex | 2 Chase AI + 1 Tù Bà Khuỳm VN | Keith AI + AI Automators + Riley Brown + Teacher's Tech + Mosh + Jack Roberts |
| claude-code-clones | Chase AI "ANOTHER Open Source Repo..." | Mostly developer-workflow content with passing clone mentions (only 4 clones named) |
| autonomous-loops (no anchor) | — | Recency-filter relaxation → generic 2025 IBM/CNN/"What is Agentic AI" explainers |

**Implication:** the drain script's search-only approach (no anchor injection) means the user-curated anchor signal is lost during selection. Topics get compiled but they're not what the operator intended.

### Operator action items

1. **Anchor injection (highest leverage):** modify `autopilot-drain.py` to accept an `Anchors:` field in the queue topic block — force-include those URLs in the NotebookLM bundle BEFORE running yt-search for the remaining slots. Would close ~70% of anchor-miss cases.
2. **Tighter queries:** until #1 ships, add specific creator names / video keywords to the query string (e.g., `Chase AI Claude Code dashboard observability 2026 status line` instead of `Claude Code dashboard agent OS observability monitoring usage 2026`).
3. **Anchor-miss flag in selection log:** the drain script could compare picked-URL list against an `Anchors:` field and log a warning when overlap < 50% — surfaces silently-failed drains before compile.
4. **Re-run flagged topics:** agent-dashboard-os / codex / claude-code-clones / autonomous-loops are all candidates for re-run with refined queries before treating as authoritative.

### Storm Bear prime directive implication

This is a **repeated-mistake risk**: if next overnight runs the same drain script with the same rubric, anchor-miss will recur. The operator action items above must close before the next `/schedule autopilot nightly` fires (currently set to midnight via launchd).

---

## Stop reason

All 6 raw bundles compiled into wiki/ topic folders + master index updated + inventory updated + meta-finding surfaced. Phase 3-7 complete.

---

## Suggested next action (per Storm Bear prime directive)

**Priority 1 (this week):** ship the anchor-injection fix to `autopilot-drain.py` so the same mistake doesn't repeat tomorrow night. Estimated effort: 30-60 min — add `Anchors:` field parsing to `parse_queue()` + skip yt-search slots equal to anchor count + prepend anchor URLs to `picked` list in `drain_topic()`.

**Priority 2 (today):** re-queue the 4 anchor-miss topics with refined queries (use specific creator names + anchor-video keywords):
- `Chase AI Claude Code dashboard status line slash commands 2026`
- `Chase AI Codex agentic harness Claude Code adversarial reviewer 2026`
- `Chase AI Open Source Claude Code clone fork CLI 2026`
- `Karpathy autoresearch Ralph loop human checkpoint plan mode grill Claude Code 2026`

**Priority 3 (next compile cycle):** lark-claude-course (261 pages, biggest remaining backlog) — still uncompiled since 2026-05-07. Coverage discipline says reconcile against `_inventory.md`; this 261-page artifact has been raw for 7 days. Decide whether to bulk-compile or drop with justification.
