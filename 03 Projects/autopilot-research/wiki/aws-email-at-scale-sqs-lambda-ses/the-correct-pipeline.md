# The Correct Pipeline — Outbox → SQS → Lambda → SES → SNS

The end-to-end architecture the video prescribes, step by step, with the production pieces it left out. Covers claims C6 and C7.

## Why NOT to send inline (C6 — CONFIRMED)

The anti-pattern: `createOrder()` → immediately call `SES.SendEmail()` in the same request handler. Two failure modes, both real:

1. **Dual-write / consistency risk.** The order write and the SES call are **separate transactions**. Order commits but SES fails → order exists with no confirmation email, and there's no retry because SES dropped it. Or the reverse. They aren't atomic.
2. **Availability cascade under peak load.** A flash sale drives sends past the per-second cap; SES rejects the excess synchronously. If that rejection happens *inside the request handler*, requests block/timeout and the failure cascades back into order processing. You've made an async concern (email) synchronous and coupled your checkout's uptime to SES's rate limit.

## The pipeline

```
①  BEGIN TX
     INSERT orders(...)
     INSERT email_outbox(email_id, ..., status='Q')   -- same transaction
   COMMIT
②  poller: SELECT ... WHERE status='Q'  → push to SQS → UPDATE status='P'
③  SQS: durable buffer (absorbs the burst)
④  Lambda consumer: throttle ≤ SES rate → SES.SendEmail → on success UPDATE status='D'
⑤  SES: publishes Send/Delivery/Bounce/Complaint/Reject events → SNS topic
⑥  SNS → Lambda/webhook: update DB status + add bad addresses to suppression list
```

### ① Transactional Outbox
Write the order **and** an email row in a **single DB transaction**. Now the intent-to-email is as durable as the order itself — no dual-write gap. Status starts at `Q` (queued). This is the classic **Transactional Outbox pattern** (Chris Richardson / microservices.io) and is AWS-aligned. The video credits its "video 33" for the outbox.

### ② Poller / relay
A scheduled worker (Lambda on a 1-min schedule, or a cron/background job) reads `status='Q'` rows and pushes each to SQS, flipping them to `P` (processing). **Best practice the video skips: check the suppression list *here*, before queuing** — fail-fast so known-bad addresses never pollute the queue. → [[bounce-complaint-and-suppression]]

### ③ SQS — durable buffer
Absorbs bursts so nothing is lost when sends exceed the SES rate. Managed, auto-scaling, ~free at this volume. → [[sqs-and-alternatives-and-cost]]

### ④ Lambda consumer — **where throttling happens**
Pulls batches from SQS and sends via SES **at a controlled rate ≤ the SES cap** (concurrency + batch size + limiter). On `ThrottlingException`: leave the message for visibility-timeout re-delivery. On success: delete the message and mark the row `D`. **This is the step the video mis-attributes to SQS.** → [[the-throttling-correction]]

### ⑤ SES → SNS event publishing
Configure an SES **Configuration Set** to publish outcome events (Delivery, Bounce, Complaint, Reject, …) to an **SNS topic**. SNS is pub/sub fan-out; it can push to Lambda, an HTTPS webhook, or another SQS queue. → [[bounce-complaint-and-suppression]]

### ⑥ Feedback handler
A Lambda (or webhook) subscribed to the SNS topic reads bounce/complaint events, updates the email row's status, and **adds permanently-failing addresses to the suppression list** so you never send to them again — protecting your bounce rate and your account.

## What the video under-covers (C7 — CORRECT-BUT-INCOMPLETE)

The foundation is sound and AWS-recommended, but production needs these additions the video omits:

- **Dead-Letter Queue (DLQ):** after a max receive count (e.g. 2–3), route persistently-failing messages to a DLQ + CloudWatch alarm — don't let them loop or age out silently.
- **Idempotency keys:** visibility-timeout re-delivery *will* re-process messages; without an idempotency key (`email_id`) you'll send duplicates. → [[database-design]]
- **Explicit consumer rate-limiting:** stated as a first-class requirement, not "SQS does it."
- **FIFO vs Standard:** Standard SQS does **not** guarantee order. If ordering matters (e.g. rejection email must precede a follow-up), use a **FIFO** queue (costs more). For most transactional email, Standard is fine.
- **Suppression check placement:** before SQS (fail-fast), not just before send.
- **Visibility timeout tuning:** default 30s is often too short for a consumer doing send + backoff.
- **EventBridge as an alternative to SNS** for SES events — richer filtering/routing; worth considering for new builds in 2026.

## Key Takeaways

- Inline sending is wrong for **two independent reasons**: dual-write consistency *and* peak-load availability. The Outbox fixes the first; SQS fixes the second.
- The Outbox → SQS → Lambda → SES → SNS shape is **the correct, standard AWS pattern** — verified against AWS docs.
- Before you ship it, add the **four pieces the video skips: DLQ, idempotency keys, explicit consumer throttling, and suppression-check-before-queue.**
