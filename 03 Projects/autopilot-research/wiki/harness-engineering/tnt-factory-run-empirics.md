# TNT factory run — the empirical ledger (what an individual-scale dark-factory-with-brakes actually looks like)

> Companion to [[tnt-cursor-cli-factory-anchor]]. This is the corpus' **most complete public run record of an individual-scale factory**: append-only `progress.md`, `guardrails.md`, per-run JSONs, and 687 commits — every claim below is computed from them (git dive, `wf_3740e2d5-2b4`), not self-reported.

## Headline numbers (2026-06-24 → 2026-07-03 window; repo pushed as late as 07-05)

- **687 commits**, **566 (82.4%) `aih:`-prefixed** (harness-authored).
- **we-event-app: 437 commits in 5 days** (06-24..29 — repo created 4 days before the FPT talk; he built the demo app the same week he presented it).
- **158 `aih: complete slice` commits; median gap 16.6 min** (P10 5.0 / P90 99.4) → the talk's "15–30 min per module" claim is **median-true** with a heavy tail (the tail = review-fail loops, see below).
- **40.5% of commits (278/687) in VN overnight hours 23:00–06:00, peak 90 commits at 00:00** → the unattended-overnight claim is real, not staged.
- **Zero human application-code commits found.** Non-`aih:` commits (121) touch harness orchestration, docs, env config, and one big cleanup. The talk's "I never edit code, I only improve the harness" survives an adversarial git audit.
- Branch discipline: `master` + `develop`, 6 PRs, merged at phase boundaries — the factory works on `develop`; the human merges.

## The run story (progress.md, 06-25)

1. **Bootstrap thrash**: 28 consecutive `checks_failed` on `repo-monorepo-bootstrap` (08:24–08:31) — the loop hammering a failing gate. Guardrails absorbed ~30 duplicate noise lines. Lesson: a factory's *first* slice is the hardest (empty repo = no conventions to imitate); loop-level dedupe/backoff was the missing primitive (later variants add cross-slice deferral, then remove it again — see evolution below).
2. Then the **entire backend in ~80 minutes**: docker-compose-db 09:20, domain-package 09:23, api-foundation 09:35, module-event 09:51, module-registration 10:08, module-checkin 10:15, module-feedback-eligibility 10:25, module-audit 10:32 — each with 0–1 `review_failed` retry.
3. **Frontend was 4× harder**: `web-design-system-shell` took 4 consecutive `review_failed` (11:02–11:27) before passing at 14:09 (~3h); participant/organizer journeys similar. The reviewer gate did real work — most corpus sources assert review value; here it's *measurable* (fail→retry→pass cycles logged with reasons: pagination envelope violations, UUID sub requirements, N+1 fan-out).
4. **Distilled guardrails that survived**: "List endpoints must return the paginated envelope (items/page/pageSize/total/totalPages) — bare arrays deprecated"; "no client-fetch-all + N+1 registration calls; use GET /me/registrations"; "e2e dev tokens must use UUID subs (Postgres 22P02 otherwise)"; "registration-status must use latest registration incl. Attended/Absent, not findActiveRegistration" — machine-written institutional memory, injected into every future implementer prompt.
5. **TestGen ran in dense batches**: 60 tag commits 11:07–14:13 and 51 more 18:05–20:13 on 06-26, plus the overnight batches he narrates in the talk ("12am–1am it was still generating while I slept").
6. **The demo slice**: `aih: complete slice web-event-cover-image` = commit `161edee`, 2026-06-27 18:02 — the exact feature he reverted on stage (06-28), re-ran the loop on, and watched rebuild live with a 9/9 browser-case pass. The live demo was a *re-run of a recorded factory event* — reproducibility as stagecraft.

## Was the output real? (app-quality audit)

Verdict: **production-grade data layer + solid MVP frontend** — not demo-slop. Evidence: real Postgres 16 via Compose with migrations; composite unique index blocking duplicate active registrations; **concurrency integration test spawning 5 parallel registrations against a full event → all deterministically waitlisted, FIFO positions distinct** (`registration.integration.test.ts` TC-AC-02-007); idempotency keys `(actorId, key, operationScope)`; audit writes with actor/reason on every state change; pagination bounds (20–100) + sort whitelist; RBAC checks with 403s; test titles traced to AC/FR/BR/NFR tags; 74 unit + 12 integration test files across 555 project files; e2e via Node native `--test` (not Vitest — dive misfire corrected). Gaps: frontend polish took multiple iterations; no license on the repo; the UI bugs visible in the talk (ID shown instead of display name, feedback panel misplacement) are honest artifacts of underspecified requirements — which is his pedagogical point: fix the docs, let the loop re-converge.

## The harness evolved across projects (reuse claim, ground-truthed)

Post-we-event, the same harness skeleton was re-instantiated with mutations:

- **we-check-app** (the 07-02/03 "academic admin/identity" commit window; successor): drops cross-slice `SLICE_DEFER` deferral complexity, simplifies the test-case gate, **adds design-tokens/accessibility/frontend-design skills to frontend+tester context** — direct response to frontend being the weak phase in we-event.
- **hesd** (Higher-Ed workshop/attendance product on Next.js + Supabase): docs family upgraded — BDD Given/When/Then acceptance criteria (23 MVP ACs), multi-level tags incl. OBJ/INV, flaky-test control policy, mobile+desktop screenshot requirements, retry-failed-first browser gate; 73 tags all `current:true` as of 07-02. (Docs-layer AI-generation likelihood assessed 70–85% — template perfection, zero human artifacts.)
- **hesd_bmad**: the **same product scaffolded with BMAD-METHOD persona agents** (bmad-agent-architect "Winston" + analyst + builder skills, 8-step activation, `_bmad/` config) — i.e., he is running an **adopt-a-framework vs build-your-own comparison on the same app, in public**. This is the exact experiment shape of the operator's queued Archon-vs-cc-sdd comparison pilot, run independently by a VN practitioner.
- **generator** (removed 07-02, commit `eeadb6f`, −7,873 lines): a scaffolding harness with doc-reviewer agents used to initialize project structure, then deleted once applied — a disposable mini **harness-builder** ([[archon-harness-builder-anchor]] distinction, at throwaway scale).

So the talk's portability answer ("structure portable, content per-project") is not aspiration — the repo contains **four sequential instantiations** with visible design mutations.

## Key takeaways

- This is the corpus' first **auditable** individual-scale factory: every velocity/autonomy claim checks out against the ledger, including the inconvenient parts (bootstrap thrash, 3h frontend slice, guardrail noise).
- Review gates demonstrably earn their cost here: distinct `review_failed → passed` cycles with named defect classes, feeding permanent guardrails.
- Frontend is the persistent weak phase (4× retries; skill-context enrichment in the successor confirms he saw it too) — matches the corpus-wide "browser/UI is the hard gate" signal.
- The `develop`-branch + phase-boundary-PR + `HUMAN_REVIEW_PASS` checklist = **dark-factory-with-brakes** at N=1 scale (cf. Archon's repo-triage maintainer layer; StrongDM's zero-review posture is the contrast case).
- Harness authorship lifecycle observed end-to-end: vibe-code it → run it → mutate it per project → extract a generator → delete the generator. Harnesses here are *livestock, not pets*.

## Related

[[tnt-cursor-cli-factory-anchor]] · [[tnt-we-event-harness-mechanics]] · [[tnt-vs-corpus-positioning]] · [[archon-default-workflows-and-dogfood]] (maintainer-layer factory sibling) · [[core-claims]] (org-scale throughput claims this partially corroborates at N=1)
