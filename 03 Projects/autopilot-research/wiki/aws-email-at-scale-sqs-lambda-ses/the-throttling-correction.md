# The Throttling Correction — SQS buffers, the consumer throttles

**This is the single most important correction to the video's mental model.** Covers claims C8 and C9.

## What the video says

> "SQS handles the 14/sec rate-limiting for you."

Implying: push everything into SQS and it will meter delivery to SES so you never exceed the cap.

## What's actually true (C8 — MISLEADING)

**SQS is a durable buffer with *no knowledge* of SES's per-second limit.** It does not throttle anything downstream. A standard SQS queue can move ~120,000 messages/sec — it will happily hand your consumer messages far faster than SES will accept sends.

**The rate limit is enforced by the *consumer*.** If a Lambda pulls 100 messages and calls `SES.SendEmail` for all of them within one second, SES rejects ~86 with `ThrottlingException` — exactly the failure SQS was supposed to prevent. The consumer must deliberately hold the send rate under the cap. ([AWS: Lambda + SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html), [SES quota errors](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas-errors.html))

### Where the throttle actually lives — the levers

You keep the consumer under the SES rate with one or more of:

- **Lambda maximum concurrency on the SQS event-source mapping** — cap how many function instances run at once. AWS shipped a dedicated "maximum concurrency for SQS" control for exactly this. (Note: concurrency → send-rate is *not* a clean linear map; batch size and per-message latency interact — measure it.)
- **Batch size + a small delay/sleep loop** inside the handler — e.g. `MaxNumberOfMessages` per poll tuned to your per-second quota, spacing sends so `rate ≤ quota`.
- **A token-bucket / leaky-bucket limiter** in the consumer code (AWS's own "prevent email throttling" guidance uses this shape). ([AWS Messaging blog: prevent email throttling with concurrency](https://aws.amazon.com/blogs/messaging-and-targeting/prevent-email-throttling-concurrency-limit/))

The clean framing (three separate layers the video blurs into one):

| Layer | Job | Rate awareness |
|---|---|---|
| **SQS** | durable buffer; survives bursts & crashes | none — ~120K msg/sec capacity |
| **Consumer (Lambda)** | **throttle** to ≤ SES quota; retry rejects | **this is where the 14/sec is enforced** |
| **SES** | send; reject overflow instantly | hard per-second cap |

## "Auto-retry" is really visibility-timeout re-delivery (C9 — CORRECT-BUT-INCOMPLETE)

The video says SQS "auto-retries on failure if a consumer exists" and "messages survive an app crash." The durability half is right; "auto-retry" is imprecise:

- **Durable:** a message stays in the queue until a consumer explicitly deletes it. Crash before deleting → it's still there. (Default retention 4 days, configurable 60s–14 days.)
- **Re-delivery, not retry:** when a consumer receives a message, it becomes *invisible* for the **visibility timeout** (default 30s). If the consumer doesn't delete it within that window (crash, timeout, or a deliberate "leave it" on `ThrottlingException`), it becomes visible again for another attempt. SQS itself never actively "retries" — it just re-exposes undeleted messages.
- **Consequences you must handle:**
  - **Idempotency is mandatory.** Re-delivery means the same email can be processed twice → duplicate sends unless the consumer dedupes (idempotency key = `email_id`). → [[database-design]]
  - **Set visibility timeout > consumer runtime** (+ backoff headroom), or a slow send re-appears and gets sent twice. Rule of thumb: `visibility_timeout ≥ lambda_timeout + buffer`.
  - **Add a Dead-Letter Queue** so a message that keeps failing (after a max receive count) lands somewhere for investigation instead of looping forever or aging out silently. The video omits the DLQ. → [[the-correct-pipeline]]

## How to handle a `ThrottlingException` in the consumer

- **Do NOT delete the message.** Let the visibility timeout re-expose it so it's retried later (natural backpressure).
- Optionally exit the handler early / lower the send rate; apply exponential backoff.
- For *permanent* rejections (bad address, validation) — **do** delete it (or route to DLQ) so it doesn't retry forever.

## Key Takeaways

- **SQS never throttles to SES. Your consumer does.** Building on the video's claim as-stated will flood SES and drop mail under load.
- Enforce the rate with **Lambda max-concurrency + batch size + an in-code limiter**; then *measure* actual send rate, because concurrency↔rate isn't linear.
- "SQS retries for you" really means **undeleted messages re-appear after the visibility timeout** — so make the consumer **idempotent** and add a **DLQ**.
