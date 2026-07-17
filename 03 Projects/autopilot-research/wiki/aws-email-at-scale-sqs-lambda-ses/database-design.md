# Database Design — outbox, suppression, audit

The three tables the video recommends, corrected and completed. Covers claim C14.

## Verdict (C14 — OVERSIMPLIFIED)

The three-table shape (email-status / blacklist / event-audit) and "use partitioning to scale" are **directionally correct** and match email-at-scale practice. But the video's schema is under-specified in ways that bite in production:

- Its status codes (`0=queued, 1=processing, 2=delivered, 3=banned, 5=retry`) have gaps and conflate **application state** with **queue state** (why is "retry" an app status if the queue's visibility timeout does re-delivery?).
- Missing the columns that make the system actually work: an **idempotency key**, `recipient_email` (for fast suppression lookups), `attempt_count`, timestamps, and a **correlation id** to trace one email across Outbox → SQS → SES → SNS → DB.
- "Use partitioning" with no partition key or retention policy.

## Table 1 — `email_outbox` (transactional state)

The row written **in the same transaction as the order/action**. Key points:

- **`email_id` (UUID) is both the primary key and the idempotency key** — carry it through SES tags and dedupe on it in the consumer, because visibility-timeout re-delivery *will* re-process messages. → [[the-throttling-correction]]
- Status set with clear, non-overlapping meaning, e.g.: `queued → processing → delivered`, plus terminal `bounced / complaint / rejected / failed`. Don't invent a "retry" status for what the queue handles; if you track scheduled retries, use `attempt_count` + `last_attempt_at`.
- Correlate: store `sqs_message_id` and `ses_message_id` so you can join to the audit table and to SNS events.
- **Partition by `created_at`** (monthly/yearly) once volume warrants; index `(status, created_at)` for the poller and `(recipient_email, created_at)` for lookups.
- **Retention:** define one (e.g. purge state rows after ~90 days) — partitioning implies a purge strategy.

## Table 2 — `suppression_list` (permanent blacklist)

- Keyed on `recipient_email` (unique). Fields: `suppression_type` (`hard_bounce` / `soft_bounce` / `complaint` / `unsubscribe` / `manual`), `reason`, SES `diagnostic_code`, `source` (`ses_automatic` vs `app_manual`), timestamps, `reviewed_at`.
- **Query this BEFORE pushing to SQS** (fail-fast) — the video only implies checking it at send time.
- This is **separate from SES's own automatic suppression list** — you keep this one for auditability and pre-queue filtering. → [[bounce-complaint-and-suppression]]

## Table 3 — `email_event_audit` (compliance trail)

- One row per SES event (Send / Delivery / Bounce / Complaint / Reject …), linked by `email_id` + `ses_message_id`.
- Store the **raw event JSON** plus parsed fields (`bounce_type`, `bounce_subtype`, `complaint_feedback_type`, `diagnostic_code`).
- **Retention longer than state** (e.g. 1–3 years) for regulatory/compliance holds — for a recruitment product this matters (see [[hireui-translation]]).
- Partition by event timestamp; index `email_id`, `ses_message_id`, `(event_type, event_timestamp)`.

## Scaling notes

- **Partition key by table:** `email_outbox` and `email_event_audit` by date (time-series); `suppression_list` by `hash(recipient_email)` or domain (lookup-optimized). The video says "partition" without saying by what.
- **Indexes are the difference at 100M rows:** `(status, created_at)` for the poller, `recipient_email` on both status + suppression, `ses_message_id` on audit.
- **Partitioning is a scale problem, not a starting requirement** — a small product does not need it for years. Add it when row counts justify it. (See the DEFER list in [[hireui-translation]].)

## Key Takeaways

- Add the columns the video omits — above all an **`email_id` idempotency key** carried end-to-end, plus `recipient_email`, `attempt_count`, timestamps, and correlation ids.
- Keep the app-level **suppression list separate from SES's automatic one**, and check it **before queuing**.
- **Partition + retention are scale-triggered**, not day-one — but design the keys/indexes so they're cheap to add later.
