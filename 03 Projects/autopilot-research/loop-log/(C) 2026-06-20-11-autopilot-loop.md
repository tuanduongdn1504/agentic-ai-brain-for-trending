# (C) Autopilot Loop — 2026-06-20-11

> **Trigger:** manual (interactive session — operator request: "build knowledge from this video + double deep-dive the original resource, then show many pilot methods")
> **Topic:** claude-code-memory-systems
> **Started:** 2026-06-20 ~11:10
> **Ended:** 2026-06-20 ~11:55
> **Duration:** ~45m
> **Path:** 5 (yt-dlp full transcript) + direct primary-source WebFetch (gist + article + 6 repos) — no NotebookLM (this worktree has no `.venv`; repos/articles best served by direct fetch, per the self-hosted-devops-oss precedent)

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 (cold-start) | 1 video + 7 primary fetches | 1 (topic itself) | ~0.5 (3 flagged-unverified claims documented, not closeable from sources) | **~0.5** |

Cold-start topic: all 10 planned articles written, indexed, cross-linked, inventory + master-index updated. Residual "gaps" are **documented unverifiable claims** (Kairos rumor / OpenBrain pricing / MemPalace "best benchmark") + **2 deferred operator pilots** (B5 semantic retrieval; A2 hook) — not missing wiki coverage.

## Sources ingested

- `raw/2026-06-20-claude-code-memory-systems.md` (yt-dlp transcript of UHVFcUzAGlM, 8,276 words + description w/ original-resource links)
- Primary sources fetched directly (not stored as raw files — extracted into articles): Karpathy LLM Wiki gist · Connolly youngleaders.tech · Huryn substack · MemSearch repo · MemPalace repo · claude-mem repo · OpenBrain/OB1 repo

## Wiki articles created/updated

- `wiki/claude-code-memory-systems/_index.md` (NEW)
- `wiki/claude-code-memory-systems/overview.md` (NEW — 2-axis model + 6-level table + decision guide + Rule-7 conflict flag)
- `wiki/claude-code-memory-systems/level-1-native.md` (NEW)
- `wiki/claude-code-memory-systems/level-2-reliable-recall-hooks.md` (NEW — the deep-dive)
- `wiki/claude-code-memory-systems/level-3-semantic-search.md` (NEW)
- `wiki/claude-code-memory-systems/level-4-verbatim-mempalace.md` (NEW)
- `wiki/claude-code-memory-systems/level-5-knowledge-base-llm-wiki.md` (NEW — Karpathy deep-dive + video critique)
- `wiki/claude-code-memory-systems/level-6-cross-tool-brain.md` (NEW)
- `wiki/claude-code-memory-systems/your-current-setup-mapping.md` (NEW — operator-specific synthesis)
- `wiki/claude-code-memory-systems/source-provenance.md` (NEW — verified-vs-flagged log)
- `wiki/_master-index.md` (UPDATED — added topic)
- `raw/_inventory.md` (UPDATED — added row)
- `output/(C) 2026-06-20-claude-code-memory-systems-pilot-methods.md` (NEW — 17 ranked pilot methods)

## Final metric

- `gaps_closed_ratio` ≈ **0.5** (cold-start; full coverage shipped, residual = documented unverifiable claims + deferred pilots)
- **Link integrity:** verified — all 14 internal targets resolve to the 10 created files; all 10 cross-topic targets resolve to existing topics. No broken links.
- Stop reason: single-topic interactive request fulfilled (knowledge built + originals deep-dived + pilot methods delivered).

## Verification posture

Built **primary-source-first** (gist/repos/article fetched directly, stronger than a NotebookLM bundle). **No multi-agent verification Workflow run** — would require explicit operator opt-in (~20+ agents). Three video-only claims flagged UNVERIFIED in `source-provenance.md` (Kairos / OpenBrain price / MemPalace benchmark) + naming/mechanism discrepancies (OpenClaw vs "Open Claude"; MemSearch exact hook event; AAAK grammar). Offer to run the adversarial pass stands.

## Top-3 unclosed gaps

1. **MemSearch exact hook event** unconfirmed (video says UserPromptSubmit; README emphasizes Stop) — resolvable only by inspecting the installed plugin.
2. **Kairos daemon** unverifiable from public sources (leak rumor) — left flagged, not asserted.
3. **B5 (semantic retrieval over the vault)** is the highest-value operator pilot but not yet executed — needs operator go-ahead to scaffold `qmd`/MemSearch on a `wiki/` copy.

## Suggested next action

Operator: run **`/consolidate-memory`** over `~/.claude/.../memory/` today (method A1 — overdue, free, you own the skill). Then A3+A4 this week (200-line audit + promote `vault-shell-flaky-workarounds` → a skill). When ready to scale the vault, ask me to scaffold **B5** (semantic retrieval). Optionally: authorize the adversarial verification Workflow to harden the 3 flagged claims.
