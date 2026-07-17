# (C) Pilot Methods — aws-email-at-scale-sqs-lambda-ses (2026-07-17)

> Deployable takeaways from wiki topic [[../wiki/aws-email-at-scale-sqs-lambda-ses/_index]] (video `HnQ0Wt6YyO0`, Tips Javascript / @anonystick).
> Tiers: **A** = hireui product · **B** = ADR/decision · **C** = vault/personal · **D** = Scrum-coaching · **E** = evals/skip-list.
> **Headline:** hireui's email risk is **reputation (bounce-rate suspension), not scale.** Ship **A1 Email Outbox v1** first; everything async is deferrable.

---

## A — hireui product

- **A1 (HEADLINE) — "Email Outbox v1": Outbox table + tiny sender, NO SQS/SNS.** ~1 week / 20–30h. `email_outbox` row written in the same Postgres TX as the candidate/action; a ~20-line scheduled worker polls `status='queued'`, calls SES, marks `delivered`/`failed`, logs to CloudWatch; status badge on Candidate Detail. Success = transactional email arrives <60s, 0 lost over a week. This de-risks delivery before any async complexity. Must run hireui-rooted (its CONSTITUTION: agent-* branch, GitNexus-first, I-8 operator-only skills).
- **A2 — Suppress-before-send.** App-level `suppression_list` table checked in the worker *before* sending; hard-bounced addresses never re-sent; `email_bounced` surfaced on Candidate Detail with re-send blocked until a human fixes the address. The cheapest guard against the #1 risk.
- **A3 — Bounce/complaint feedback loop.** SES Configuration Set → SNS (filtered to Bounce+Complaint) → handler updates status + suppression + flags the recruiter. Add with A2 or just after.
- **A4 — Email-address validation at candidate import** (regex/format + "verified/unverified" state) to keep bounce rate down at the source.
- **A5 — CloudWatch alarms at 2% bounce / 0.05% complaint** (half the SES >5%/>0.1% thresholds) — early warning before AWS review. Per-recruiter bounce metric for the multi-tenant coupling risk.
- **A6 (DEFER) — SQS + Lambda consumer with explicit throttling**, DLQ, FIFO-if-ordered, DynamoDB idempotency, partitioning. Graduate here when sustained ~500/day, `ThrottlingException` appears, OR bulk outreach launches — NOT before.

## B — ADR / decisions

- **B1 — "Email stays deterministic + legible" ADR.** Composes with the RATIFIED candidate-LLM legibility ADR: candidate-facing emails use **static, version-controlled templates + `{{variable}}` substitution only; no LLM-generated bodies; every send audited.** Emergent orchestration prohibited on this path (it's a candidate-outcome path).
- **B2 — Build-vs-buy decision, recorded.** hireui is under the ~100K/month crossover where a **managed ESP (Postmark/Resend/SendGrid) beats hand-building SES+SQS** on total cost of ownership. Decide explicitly: managed-ESP-now vs SES-pipeline-now. (The video never asks this; it's the biggest strategic fork.)
- **B3 — SQS Standard (unordered) ADR** if/when SQS lands: "email ordering is not business-critical → Standard, not FIFO."
- **B4 — GDPR/consent + unsubscribe for bulk outreach** — flag as required for any bulk feature (opt-in tracking + legal unsubscribe footer). hireui has neither today.

## C — vault / personal

- **C1 — Cross-link the deploy layer.** This topic + [[../wiki/fullstack-docker-cicd/_index]] + [[../wiki/api-security-7-techniques/_index]] now form a small hireui-infrastructure cluster (deploy / secure / notify). Consider a synthesis note.
- **C2 — Watch @anonystick's TRYBUY series** for the other high-concurrency episodes (idempotency/duplicate-payment already referenced; partitioning; Lambda) — a coherent VN backend-architecture source worth deeper coverage if hireui backend work ramps.

## D — Scrum-coaching

- **D1 — "Design the architecture before coding" as a team ritual.** The video's SA-first framing (whiteboard the failure modes, then hand a diagram to devs) is a clean anti-vibe practice — pairs with the harness-engineering / system-thinking topics for junior onboarding.
- **D2 — "Know your platform's hard limits" teaching case.** SES-is-an-API-not-a-broker is a memorable lesson in reading the constraint before designing around it.

## E — evals / skip-list

- **E1 — Skip:** the 1M/day scale trick itself — hireui won't need it for years. Extract the *reliability* discipline, not the throughput mechanics.
- **E2 — Skip for v1:** SQS/Lambda/DLQ/partitioning/idempotency-table (A6) — deferred per the graduation criteria.
- **E3 — Verify before A1:** does hireui already send email inline on candidate/order creation? If so, that's the anti-pattern to replace, not extend.

---

## Ranking

**A1 → A2 → A3** is the deployable spine (Outbox → suppress-before-send → bounce feedback). **B2 (build-vs-buy) should be decided first** — it may make A6 moot (a managed ESP subsumes SQS/SNS/suppression). Recommended sequence: **decide B2 → ship A1+A2 → add A3 → revisit A6 only at the graduation trigger.**
