# Open Questions — gsd-2 v54

## Authorship identity

- **Q1**: Is **Lex Christopherson** (LICENSE + ADRs) the same person as **TÂCHES** (GSD-1 author per Storm Bear v5 wiki)?
  - **Evidence for same-person**: gsd-build org owns both repos; VISION.md says GSD-2 is the "future" of GSD-1; coherent product-line continuation
  - **Evidence against same-person**: Zero "TÂCHES" mentions in GSD-2 README/VISION/CONTRIBUTING/docs; Lex Christopherson explicit in LICENSE + ADRs + filesystem paths; voice is professional/neutral vs TÂCHES's distinctive "solo developer who doesn't write code" framing
  - **Honest verdict**: Unknown. Document as-observed; do NOT assume identity continuity
  - **Resolution path**: External verification (Twitter / Discord / personal blog cross-reference) — not done in this wiki

- **Q2**: Did GSD-1 (TÂCHES) hand off to GSD-2 (Lex Christopherson) within gsd-build org? Or is gsd-build a multi-maintainer org from the start?
  - **Resolution path**: Inspect gsd-build org members publicly; check git commit history for both repos

## Pattern Library questions

- **Q3**: Should Pattern #21 SDD un-stale at next mini-audit count aidevops v47 SDD elements as 4th data point? (GSD v5 + spec-kit v17 + aidevops v47 + gsd-2 v54)
  - Operator decision required at audit
  - Conservative interpretation: stays at N=2 single-tier (only GSD v5 + gsd-2 v54 = same product line); aidevops + spec-kit are SDD-adjacent not SDD-pure
  - Liberal interpretation: SDD methodology emergence is broader; all 4 count

- **Q4**: Should Pattern #57 sub-variant 57d (explicit-vendored-package-metadata) be registered? Or absorbed into existing 57a-c?
  - 57a = direct-citation (4 corpus prior)
  - 57b = aggregator-mediated-multi-citation (awesome-claude-skills v50)
  - 57c = forward-citation-then-wiki (multica v15 → vercel v51 ; OMC v27 → omo v52)
  - **57d candidate**: machine-readable-metadata vendoring acknowledgment (gsd-2 package.json descriptions)
  - **Conservative recommendation**: Strengthening only at this wiki (N=1 stale-flag); register only if 2nd corpus example emerges

- **Q5**: Pattern #37 Crypto-Donation-Funded Scale Path — does $GSD token at gsd-2 (commercial framework) + $GSD token at GSD-1 (predecessor) = N=1 (single product line) or N=2 (separate products)?
  - **Resolution**: Treat as N=2 strengthening only if the tokens are distinct + GSD-1 token preceded gsd-2 (probable). Currently flagged for v59 review.

## Architecture questions

- **Q6**: What does **gsd-2 daemon** (`@gsd-build/daemon`) actually do at the cloud-tier level? Discord integration mentioned but no commercial Pro tier observed in README. Is gsd.build building toward Pro tier?
  - **Resolution path**: Probe gsd.build homepage + Discord descriptions
  - **Pattern Library impact**: If Pro tier emerges, register Pattern #50 8th data point; currently observational watch

- **Q7**: What does **GSD Studio** (Electron + React 19 + Zustand) provide that the CLI doesn't? Is it Pro-tier-only or OSS GUI?
  - Studio has dev/build/preview scripts in package.json but version `0.0.0` (private workspace) — likely incubation
  - **Resolution path**: Probe Studio src/ + check if it ships in npm `gsd-pi` distribution

- **Q8**: How does **managed RTK binary** (compresses shell-command output) integrate at runtime? README mentions opt-out env vars but architectural pattern unclear.
  - **Resolution path**: Read `scripts/install.js` + `packages/native/scripts/build.js`
  - **Pattern Library impact**: First corpus managed-third-party-binary-with-telemetry-discipline observation

## Storm Bear vault impact questions

- **Q9**: Should vault adopt **state-machine-from-disk** pattern (gsd-2 reads `.gsd/STATE.md` each iteration) for routine v2.2?
  - Currently routine v2.1 has no formal state file; iteration logs are narrative
  - Potential: `02 Wiki/STATE.md` per-project file + central `vault-state.md`
  - Risk: Adds complexity; simpler narrative iteration logs may be sufficient

- **Q10**: Should vault's 5 skills migrate to **extension-first principle** (VISION.md verbatim "If it can be an extension, it should be")?
  - Currently 4 vault skills in `05 Skills/` (llm-wiki-ingest + llm-wiki-routine-v2.1 + brain-setup + new-project)
  - Question: Should new patterns become standalone skills vs CLAUDE.md additions?
  - Operator decision required (low priority; works as-is)

- **Q11**: Should vault adopt **structured journal events** (gsd-2 emits worktree-created / worktree-merged / etc.) for iteration-log-v2 enhancement?
  - Currently iteration logs are 13-section narrative
  - Potential: Add YAML frontmatter with structured event list
  - Risk: Marginal value for solo operator; high-value for multi-agent vault

## Routine v2.2 candidate inputs

- **R1**: 18-consecutive-wiki zero-registration streak (v37-v54) — reframe consolidation-forward discipline from "rare exception" to "default expected behavior at corpus maturity"
- **R2**: Cross-corpus vendoring metadata as Pattern #57 sub-variant detection signal — formalize machine-readable-metadata-vendoring as routine probe step
- **R3**: Authorship-identity-verification protocol — when wiki author identity-mapping is uncertain (e.g. TÂCHES → Lex), formalize "document as observed; do not assume continuity" as routine discipline
- **R4**: YELLOW primitive-count tier validation N=5 (pi-mono v36 + bizos v37 + DeepTutor v38 + shannon v45 + gsd-2 v54) — discipline holds at +25-33% velocity overhead band

## v27 diagnostic HIGH bundle

- **34 sessions deferred** (v28-v54). 6.8× routine v2.1 5-session threshold. **CRITICAL**: gsd-2 does NOT add new vault refactor templates (no root AGENTS.md). Existing 4-template ensemble (22a monolithic + 22b minimum-viable-shim + 22c authoritative-with-shim + 22d identical-mirror) remains operational reference for vault CLAUDE.md refactor item #1. **STRONGLY RECOMMENDED execute v27 HIGH bundle before v55.**
