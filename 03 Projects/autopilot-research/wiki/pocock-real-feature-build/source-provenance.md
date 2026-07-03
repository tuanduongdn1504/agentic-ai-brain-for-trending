# Source provenance — capture, verification, and the misfire ledger

## Primary source

- **Video:** [hX7yG1KVYhI](https://www.youtube.com/watch?v=hX7yG1KVYhI) — "Building a REAL feature with Claude Code: every step explained", **Matt Pocock's own channel** (first-party), uploaded 2026-03-18, 44:16, 162,785 views at capture (2026-07-03), ~285K subs.
- **Capture:** `yt-dlp --write-auto-subs --sub-langs en` → VTT → `clean_vtt.py` dedupe (1,362 lines / ~50K chars) → `raw/2026-07-03-pocock-real-feature-build.md`. **Read in full** by the compiling session. ffmpeg absent → VTT parsed directly (known-good path).
- **Relation to existing corpus:** sister to [[../pocock-agentic-workflow/_index]] (Ondrej podcast, 2026-06-18 — three months LATER than this video). Same author, zero source overlap; podcast = philosophy, this = worked example. The separate ~96-min AI-Engineer-2026 workshop remains uncompiled and is NOT this.

## Deep-dive verification run

- **Workflow `wf_8897fa8d-c95`** — 15 agents / ~880K subagent tokens / 400 tool calls / ~7.6 min wall-clock:
  - 7 deep-dive gatherers: cvm-repo, cvm-harness, skills-repo, sandcastle, aihero, ddd, cc-features (dossiers in session scratchpad).
  - 7 adversarial verifiers (REFUTE-first, one distinct lens each, with pinned discipline: *unreachable ≠ fabricated*).
  - 1 completeness critic (conflict resolution + missing-coverage + don't-re-fabricate list).
- **Operator ground-checks** (`gh api`, direct): mattpocock/skills metadata (created 2026-02-03, 154,511★), tree grep for the ubiquitous-language skill, full fetch of `skills/deprecated/ubiquitous-language/SKILL.md` + `skills/engineering/domain-modeling/SKILL.md`.

## Verifier-misfire ledger (the recurring corpus pattern, again)

- **The ddd-verifier REFUTED two true facts:**
  1. Declared the `/ubiquitous-language` skill non-existent (it searched the wrong directories) — **overridden**: the skill exists at `skills/deprecated/ubiquitous-language/`.
  2. Declared the skills repo "could not exist in February 2026" from the v1.0.0 release date (2026-06-17) — **overridden**: release tags ≠ repo creation; `created_at` = 2026-02-03.
  - The completeness critic caught #1 (cross-referencing the skills-repo dossier); the operator ground-check settled both. **Lesson: existence-refutations require a second, independent ground-check** — consistent with the standing wiki-verify memory rule.
- **The ddd deep-dive itself** carried real errors the verifier DID catch correctly: ~53K★ (→154.5K), a mischaracterized arXiv citation (Lost-in-Distance ≠ lost-in-the-middle), two unreachable sources cited as if confirmed (earezki.com, morphllm.com — dropped from the wiki).
- **Quote-accuracy elsewhere:** the cvm-harness dossier passed 100% of spot-checked quotes; cvm-repo had one material number error (170+ → 89) caught by its verifier.

## Claim-class conventions used in this topic

- **[video]** — what Matt says/shows on 2026-03-18 (may have drifted since).
- **[source, 2026-07-03]** — verified in current repo/docs at compile time.
- **[position]** — Matt's opinion (anti-spec stance, token-efficiency rationale).
- **[reported]** — unverified attribution (Jaman; dictation tool unnamed).

## Coverage notes

- Uncovered by design (flagged, not fetched): Jaman's identity; per-run performance metrics beyond on-screen observations; the video's exact issue numbers (the visible Sandcastle trail #743–#748 post-dates upload).
- The `.sandcastle/` analysis reflects the repo's **current** state — the video-era harness predates the published package; drift is documented in [[caveats-and-corrections]].

## Key Takeaways

- First-party source + public artifacts made this the **most ground-checkable Pocock item in the corpus** — nearly every on-screen claim resolved to a fetchable file.
- The misfire ledger now has a new sub-type: **release-tag-as-creation-date confusion** — add to the existence-refutation checklist alongside wrong-directory search and network-failure-as-fabrication.
