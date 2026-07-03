# Version-pinning discipline & the read-old-docs skill

## Source
- Video #4 tD0Uve-0Ltk (20:30 "Version Nestjs", 22:18 Node env, 32:23 pin-don't-latest, 55:18 VS Code TS) + course Google Doc (verbatim pins)

## The discipline
- **Exact pins, stated in the course doc:** *"Cài chính xác Node.js version 24"* → nodejs.org/download/release/**v24.14.0**/ · `npm i -g @nestjs/cli@`**11.0.23**.
- On camera [32:23]: *don't* run the docs' `@latest` — copy the exact version string, so every student (and every AI suggestion applied later) operates on the same substrate.
- **Why pins, per the teaching:** cohort reproducibility across months (the video will be watched later than it aired) + AI-suggestion reproducibility (a fix valid on 11.0.23 may not be on 12.x).
- **Read-old-docs skill** [21:18–21:46]: the docs version dropdown is a first-class tool; *"most jobs are maintaining old projects on old versions, not greenfield latest"* — the skill of reading version-matched docs beats reflexive upgrading.
- **Editor-vs-project versions** [55:18]: VS Code bundles its own TypeScript (6.0.x line, real — 6.0.2 stable 2026-03-23) while the project pins 5.9.3; the mismatch warning is cosmetic. Root-cause literacy: *"máy không lỗi — phần mềm vênh version"* (the machine isn't broken; the versions disagree).

## The procedure behind the pins
- Ep-3 (full transcript, 2026-07-04 deepening) contains the mechanical workflow that *produces* these pins — git baseline → `ncu` → strip `^`/`~` → `ncu -u` → diff review → install. See [[version-pinning-procedure]].

## Corpus placement
- Same instinct as the **committed Claude auto-memory as version-ledger** sighting in [[jsm-practical-vibe-coding/_index]] (pinning post-cutoff API knowledge for the agent) — here pinned for humans+AI in a teaching cohort.
- Composes with [[docs-first-ai-second]]: docs give the procedure, pins freeze the substrate, AI operates inside that frozen frame.
- Counter-pole to `@latest`-reflex tutorials; closest sibling teaching in corpus: [[harness-engineering/_index]] dependency-vendoring (org-scale version of the same reproducibility bet).

## Key Takeaways
- Pin exact versions when humans *or* agents will replay your steps later — reproducibility is the product.
- The doc's pin (`@nestjs/cli@11.0.23`) verified as **npm `latest` at doc-time** — pinning ≠ falling behind; it's freezing a known-good frame.
- Teach (and configure) the docs-version dropdown; version-matched docs beat newest docs.
- Editor-bundled toolchains drift from project pins by design; teach the two-layer model instead of "fixing" the warning.
