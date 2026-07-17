# Overview — Sending a Million Emails a Day on AWS

## Source

- Video: [`HnQ0Wt6YyO0`](https://www.youtube.com/watch?v=HnQ0Wt6YyO0) — "Show dự án với cách mà các công ty lớn gửi hàng triệu email | AWS SQS, Lambda & SES", channel **Tips Javascript** ([@anonystick](https://www.youtube.com/@anonystick)), 2026-07-15, 16:13, ~1.3K views.
- Raw transcript: `raw/2026-07-17-aws-email-at-scale-sqs-lambda-ses.md` (Vietnamese `vi-orig` auto-subs, read in full in the main loop).
- Part of the channel's high-concurrency / large-data project series (the **TRYBUY** e-commerce backend build); the prior episode covered duplicate-payment idempotency, and it references an earlier "video 33" for the Outbox pattern.

## What the video is

A Vietnamese backend tutorial framed as a **Solution-Architect design session**: given the requirement "send 1,000,000 emails/day," design the architecture *before* writing code. The host draws the whiteboard, names each AWS service, and explains why the naive approach fails. It is a design/whiteboard talk, not a live coding demo.

## The problem it solves

- AWS **SES (Simple Email Service)** is how you actually send mail, but it enforces hard limits:
  - **Sandbox:** 200 emails / 24h, max **1 email/sec**, verified recipients only.
  - **Production:** higher, account-specific quotas (the host's account = **14 emails/sec**).
- **SES is a synchronous API, not a message broker.** If you ask it to send faster than your per-second rate, it **rejects the excess immediately** with a `ThrottlingException` (SMTP `454`) and does **not** queue or auto-retry. Retry is the developer's job.
- So at a flash-sale peak — say 100 emails hit in one second against a 14/sec cap — SES sends 14 and **drops 86**. The naive "send email inline right after creating the order" approach loses those 86 emails *and* risks cascading the order request into a timeout.

## The corrected mental model (the fix)

Put a **durable buffer** in front of SES and a **rate-limiting consumer** between them:

```
Order write ─┐
             ├─(same DB transaction)→ Outbox row (status = queued)
             │
   poller ───┴→ SQS (durable buffer) ──→ Lambda consumer ──(throttled to <14/sec)──→ SES ──→ recipient
                                                                                        │
                     DB update + suppression list ←── Lambda/webhook ←── SNS topic ←────┘
                                                                        (Bounce / Complaint / Delivery events)
```

- **SQS** absorbs the burst so nothing is dropped; it's cheap (1M requests/month free) and fully managed.
- The **Lambda consumer** pulls from SQS at a controlled rate and is what actually keeps sends under the SES cap. → [[the-throttling-correction]]
- **SNS** carries SES's delivery/bounce/complaint events back to your system so you can update state and blacklist bad addresses — which protects your account from suspension. → [[bounce-complaint-and-suppression]]

## Verdict at a glance

The architecture is **the real, AWS-recommended pattern** and the technical claims hold up. Full detail in [[caveats-and-corrections]] and [[verification scorecard|caveats-and-corrections]].

- **14 claims checked: 7 CONFIRMED · 4 CORRECT-BUT-INCOMPLETE · 2 MISLEADING · 1 OVERSIMPLIFIED · 0 FALSE · 0 FABRICATED.**
- The failure mode is **over-claim / omission, not fabrication.** The two MISLEADING items:
  1. **"SES quota scales in fixed tiers (20K→50K→80K→100K→1M)"** — AWS publishes *no* fixed tiers; increases are case-by-case on reputation.
  2. **"SQS handles the 14/sec rate-limiting for you"** — SQS only buffers; the *consumer* throttles. This is the one mental-model error a junior could implement wrong.

## Key Takeaways

- The whole design exists because **SES rejects overflow instantly with no retry** — internalize "SES is an API, not a queue."
- The pattern is sound and standard: **transactional Outbox → SQS → rate-limited consumer → SES → SNS feedback → DB + suppression.**
- The video is ~90% accurate; the one thing to un-learn is "SQS throttles for you." It doesn't — you write the throttle in the consumer.
- What the video under-covers (production-critical): **Dead-Letter Queue, idempotency keys, and SES's own built-in suppression list.** See [[the-correct-pipeline]] and [[database-design]].
