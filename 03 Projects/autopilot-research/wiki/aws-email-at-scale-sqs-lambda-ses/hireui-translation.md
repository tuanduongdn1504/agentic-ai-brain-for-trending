# hireui Translation — transactional email for a recruitment SaaS

Mapping the pattern to **hireui** (TalentAxis recruitment SaaS; Goal-#2 build target). hireui currently has **no LLM in product code** and modest email needs; it is **nowhere near 1M/day**. So the value here is not the scale trick — it's the **reliability + reputation-protection discipline**, sized down.

## Which emails hireui sends

- **Transactional** (must arrive, fast): application confirmations, interview invitations/reminders, offer letters, recruiter notifications.
- **Bulk outreach** (batchable): messages to selected candidate lists — **this is the dangerous one**, because candidate email lists go stale (job changes, typos, dead addresses).

## The dominant risk: bounce-rate suspension, not scale

This is the headline for hireui. Bulk outreach to a stale list can blow past **SES's >5% bounce / >0.1% complaint** thresholds and get the **whole TalentAxis sending identity paused** — taking down transactional email (offer letters!) for every tenant. → [[bounce-complaint-and-suppression]]

**Adopt-now mitigations:**
- **Suppress-before-send** — check an app-level suppression table in the poller before any address is queued. Non-negotiable.
- **Never re-send to a hard-bounced address**; surface `email_bounced` on the Candidate Detail screen and block re-send until a human corrects the address.
- **CloudWatch alarms at 2% bounce / 0.05% complaint** — half the SES thresholds, so you get warning before review.
- **Show the recruiter the truth** before a blast: "200 of 500 addresses are suppressed; sending to 300."

## Adopt now (smallest useful version)

1. **Transactional Outbox** — write an `email_outbox` row in the same Postgres transaction as the candidate/action. Atomic intent-to-email. → [[database-design]]
2. **App-level suppression table** + pre-send check.
3. **Bounce/complaint feedback** via SES → SNS → handler that updates status, suppresses bad addresses, and flags the Candidate Detail UI.
4. **Fixed, versioned email templates** (see legibility note below).

## Defer (over-engineering at hireui's current scale)

- **SQS + Lambda consumer** — hireui at ~100–200/day is under the sandbox ceiling; a simple poller calling SES directly is enough. Add SQS when volume/bursts demand it or when bulk outreach launches.
- **FIFO queue** — email ordering isn't critical; Standard is fine when SQS arrives.
- **DB partitioning** — years away at this volume.
- **DLQ, DynamoDB idempotency table** — add with SQS, not before.
- **SES production quota negotiation** — don't file until sustained ~500+/day.
- **Per-recruiter sending domains** — v2 concern; for v1 use one verified TalentAxis sender with the recruiter's name in the `From` display.

## Recruitment-specific risks beyond bounce rate

- **Outcome-affecting legibility (CRITICAL).** Recruitment emails carry outcomes (rejection/offer). Per the **RATIFIED hireui candidate-LLM legibility ADR**, any LLM path affecting a candidate's outcome must be fixed + legible + audited, and **emergent orchestration is prohibited on candidate paths.** Translation for email: **templates are static, version-controlled strings; personalization is safe `{{variable}}` substitution only; no LLM-generated email bodies on candidate-facing sends; every send logged in the audit table.** This composes with the email pattern cleanly — the pipeline is deterministic; keep it that way. (See the memory ADR and [[../mosh-ai-powered-apps/_index]] for the LLM seam next door.)
- **GDPR / consent / unsubscribe (compliance).** Bulk outreach needs opt-in tracking + an unsubscribe mechanism (legally required footer). hireui has neither today → flag for v2; for a v1 pilot, include a manual unsubscribe footer and only blast opted-in candidates.
- **Multi-tenant reputation coupling.** 30+ recruiters share one SES identity → one bad actor's spam-y blast hurts everyone. Monitor **bounce rate per recruiter** (custom CloudWatch metric); educate recruiters in onboarding.
- **Email validation at import.** Typos (`gmial.com`) → bounces → lost hires. Add regex/format validation at candidate import; show a "verified/unverified" state.

## The pilot (one small step)

**"Email Outbox v1" — Outbox table + a tiny sender, no SQS/SNS yet.** ~1 week / ~20–30h:
- `email_outbox` table (+ status badge on Candidate Detail).
- A ~20-line scheduled worker: poll `status='queued'`, call SES, mark `delivered`/`failed`, log to CloudWatch. No retry logic yet (mark failed; recruiter resends).
- Request SES production access for a verified TalentAxis sender; keep sandbox rate.
- **Success:** transactional emails arrive < 60s of recruiter action; 0 lost sends over a week of real candidate email; bounces visible in logs.
- **Graduate to v2 (add SQS/SNS/suppression)** when: sustained 500/day, `ThrottlingException` shows up, OR bulk outreach launches.

**Pre-pilot checks:** confirm hireui's migration process for the new table; verify DKIM/SPF/DMARC on the TalentAxis domain with ops; locate where email templates currently live (code vs DB) and version them; audit whether order/candidate creation already sends email inline (the anti-pattern in [[the-correct-pipeline]]).

## Key Takeaways

- For hireui, **the risk is reputation, not throughput.** Adopt **Outbox + suppression-before-send + bounce/complaint feedback**; defer SQS/SNS/partitioning until volume justifies them.
- **Email stays deterministic and legible** per the candidate-LLM ADR: static versioned templates, `{{variable}}` substitution, full audit log, no LLM bodies on candidate-facing mail.
- Ship the **1-week "Outbox v1"** pilot; it de-risks email delivery before any async complexity and slots cleanly next to the mosh-ai first-LLM-feature work.
