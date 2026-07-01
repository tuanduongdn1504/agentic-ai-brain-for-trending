# (C) Autopilot Loop — 2026-07-01-13

> **Trigger:** manual (operator ask: "build knowledge from this video + double deep-dive into the original resource + show me many methods to apply to my workflow")
> **Topic:** google-antigravity-skills (Google Antigravity Skills + Rules)
> **Started:** 2026-07-01 ~13:10 (+07:00)
> **Ended:** 2026-07-01 ~13:40 (+07:00)
> **Duration:** ~30m (main loop) + ~8m background verification workflow (overlapped)

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video (UFmV7YsVqlM) + verified deep-dive of the original resource (Google Antigravity) | 1 (cold-start: topic didn't exist) | 0 (11 full articles + index; master-index updated; cross-links; pilot menu) | **1.0** |

## Sources ingested

- `raw/2026-07-01-google-antigravity-skills-rules-dung-chiasecongnghe.md` — Path 5 yt-dlp, Vietnamese auto-caption (592 lines / ~22K chars, read in full). **Note:** the `timedtext` endpoint 429'd on the default client; caption pulled via `--extractor-args "youtube:player_client=tv,web_safari,mweb"` + vtt fallback → `clean_vtt.py` dedupe. (Block-handling: this was a rate-limit on the *subtitle* endpoint, not a page block — resolved by client rotation, per project 403/429 discipline; no Camoufox tier needed.)
- **Original-resource deep-dive** (the operator's "double deep-dive" ask): Google Antigravity itself, verified against official Google sources via Workflow `wf_1e5cf2f6-5ec` (16 agents; ~816K tokens; 355 tool calls) + operator WebFetch/WebSearch ground-checks (codelabs, blog.google I/O-2026, cloud.google.com "choosing your surface", agentskills.io, Linux Foundation).

## Wiki articles created/updated

- `wiki/google-antigravity-skills/_index.md` (NEW)
- `wiki/google-antigravity-skills/overview.md` (NEW)
- `wiki/google-antigravity-skills/skills-system.md` (NEW)
- `wiki/google-antigravity-skills/rules-and-customization.md` (NEW)
- `wiki/google-antigravity-skills/workspace-vs-global.md` (NEW)
- `wiki/google-antigravity-skills/build-methods.md` (NEW)
- `wiki/google-antigravity-skills/anthropic-agent-skills-portability.md` (NEW)
- `wiki/google-antigravity-skills/vs-claude-code-and-cursor.md` (NEW)
- `wiki/google-antigravity-skills/caveats-and-limitations.md` (NEW)
- `wiki/google-antigravity-skills/video-summary.md` (NEW)
- `wiki/google-antigravity-skills/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — added `## google-antigravity-skills` topic)
- `raw/_inventory.md` (UPDATED — +1 row, status `compiled`)
- `output/(C) 2026-07-01-google-antigravity-skills-pilot-methods.md` (NEW — 22 methods)

## Final metric

- `gaps_closed_ratio` = **1.0** (cold-start topic fully compiled in one cycle)
- **Stop reason:** target_ratio (0.5) reached — single-cycle cold start; hand control back.

## Key findings (Rule 12 fail-loud — corrections made)

1. **The video's spoken skills path is wrong.** VN auto-caption garbled it; the official path is **`.agents/skills/`** (project) / `~/.gemini/config/skills/` (global), **not `.antigravity/skills`**.
2. **"Antigravity 2.0" is REAL** — an official standalone desktop app from Google I/O 2026 (May 2026), distinct from the IDE. My own quick first-read wrongly leaned "informal label"; the verification workflow **corrected me** (cross-checked the official cloud.google.com "choosing your surface" page).
3. **Windsurf = a $2.4B *licensing + reverse-acquihire*, not an acquisition** (Codeium licensing + Varun Mohan hire, July 2025).
4. **HEADLINE:** Antigravity Skills **= Anthropic's open `SKILL.md` format** (adopted, not reinvented) + rules ride the **`AGENTS.md`** Linux-Foundation cross-tool standard → the operator's Claude Code harness is **portable to Antigravity for ~a directory rename**. This reframes the whole topic from "new tool" to "your harness is now open standards."
5. **Verifier-confabulation caught again:** a WebFetch summarizer (stale knowledge cutoff) slapped a "this appears fictional" disclaimer on the *real* Cloud "Antigravity 2.0" page — **overridden** by its own quoted primary content. Same pattern logged in the how-we-claude-code / open-design / pocock threads.
6. **Flagged reported-not-verified** (don't re-fabricate): 6-persona names, exact version strings, "AGENTS.md in 60K repos", token-overhead/quota-lockout/403-ban specifics.

## Top-3 unclosed gaps (carry-forward)

1. Exact rule-precedence when `CLAUDE.md` + `AGENTS.md` + `GEMINI.md` coexist in one repo (Antigravity's resolution order).
2. Whether the mid-2026 quota/stability/403-ban issues have an official fix (public-preview product; re-check on a later ingest).
3. Whether skills can compose/call other skills + skill versioning story (not documented).

## Suggested next action

**Do pilot methods A1 + A2 today** (create an `AGENTS.md` for the autopilot project; audit your four project-local skills' `description`s for progressive-disclosure quality) — ~1h, no install, improves your live Claude Code hit-rate and makes the harness portable. Then schedule **A3** (harvest the hireui Candidate-Detail refactor into a portable `SKILL.md` + `AGENTS.md` guard rule) as the week's Goal-#2 deliverable, composing with the cc-sdd #1, how-we-claude-code verify, and open-design `DESIGN.md` pilots. Only after that, decide whether a metered Antigravity **sandbox** (B1/B2) is worth the public-preview caveats. Full menu: `output/(C) 2026-07-01-google-antigravity-skills-pilot-methods.md`.
