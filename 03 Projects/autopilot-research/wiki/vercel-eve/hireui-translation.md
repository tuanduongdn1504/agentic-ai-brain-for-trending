# Eve → hireui translation

## Source
- Synthesis + completeness critic from workflow `wf_e215817b-a5d`, mapped to the operator's ratified **candidate-LLM legibility ADR** and **agent-nativity spec**. Bundle `raw/2026-07-18-vercel-eve/`.

## Bottom line

> **AVOID Eve for any hireui candidate-touching LLM layer right now. WATCH it for recruiter-side (non-candidate-facing) automation post-GA. BORROW three of its patterns immediately — regardless of whether you ever adopt the framework.**

## Why AVOID (candidate-facing) — it fails the ADR on two non-technical axes

The ratified ADR: *any hireui LLM path affecting a candidate MUST be fixed / legible / audited / human-in-loop / eval+bias-gated, behind the Mosh A2 seam; emergent orchestration PROHIBITED; driver = EU AI Act Annex III.* Eve is blocked by:

1. **Data-residency = HARD BLOCKER.** No published statement on where agent state / conversation logs / eval results / sandbox output live, retention/deletion policy, or whether Vercel trains on inputs/outputs. Annex-III candidate PII cannot sit on an undocumented-residency platform. No adoption without **written** answers on (1) storage region, (2) retention/deletion SLA, (3) training/usage policy, (4) audit-log access, (5) support-team access limits.
2. **Beta / no GA date + no independent security audit.** A June-2026 public-preview framework with breakable APIs and no third-party audit is not a substrate for regulated candidate decisions.

Plus a **strategic mismatch:** Eve is Vercel-first; hireui's direction is multi-vendor + self-host flexibility. The vendor-neutral rival **Mastra** (TS-first, Inngest durability, platform-agnostic) is the better starting point if you want this DX without the binding.

## What to BORROW now (pattern adoption, zero framework lock-in)

1. **Credential-brokering discipline** → enforce "keys never on the agent" in the **Mosh A2 seam**. Eve's `connections/` (OAuth + token refresh at framework level; model never sees real keys) is the exact pattern; make it an ADR enforcement precedent for any internal LLM feature touching candidate data.
2. **Evals-as-deploy-gate** → Eve's `evals/` = scored suites that gate regressions before prod. This is precisely the verification the ADR demands for candidate-LLM behavior (and for the Candidate-Detail work). Adopt the *pattern* (evals in CI gating merges) independent of Eve.
3. **`needsApproval` HITL** → a first-class "pause for human approval on risky action, zero compute while waiting" primitive. Mirror it for any candidate-affecting action (auto-reject, auto-advance, outreach send).
4. **Filesystem-legibility** → the directory-as-manifest model (instructions.md + tools/ + skills/ + connections/) is transparent-by-construction — a good shape for the **agent-nativity spec** (first-party skills in a legible tree; cf. the geti "ship a product's first-party agent-skills" precedent). Borrow the *legibility*, keep your own harness.

## What to WATCH (revisit triggers)

- **Post-GA + published data-residency + security audit** → then reconsider Eve for **recruiter-side, non-candidate-facing** agents: job-ad enrichment, internal candidate-base screening summaries, interview/outreach scheduling. Lower compliance risk (still keep candidate PII out until residency is answered).
- **Vercel "Passport"** (shadow-AI governance) — if it addresses org-level agent governance, it may matter more to hireui than Eve itself. Flagged for a follow-up deepening.
- ⚠️ Even recruiter-side agents log execution state on Vercel with no self-host path today — prefer **Mastra** for internal agents unless the operator explicitly accepts Vercel lock-in.

## Key Takeaways

- **Candidate-facing: AVOID** — blocked by data-residency gap + beta + no audit, not by the tech.
- **Recruiter-side: WATCH** — reconsider post-GA + residency/audit clarity; still lean Mastra for vendor-neutrality.
- **BORROW now:** credential-brokering, evals-as-deploy-gate, `needsApproval` HITL, filesystem legibility — all portable to the Mosh A2 seam + agent-nativity spec **without** adopting Eve.
- The most useful thing Eve gives hireui is a **validated pattern vocabulary**, not a deployment target.

## See also
- [[vercel-eve/production-features]] · [[vercel-eve/vendor-lock-in-and-competitive-landscape]] · [[vercel-eve/caveats-and-corrections]]
- [[external|Storm Bear: career-ops]] (candidate-side inverse) · [[agent-development-lifecycle/_index]]
