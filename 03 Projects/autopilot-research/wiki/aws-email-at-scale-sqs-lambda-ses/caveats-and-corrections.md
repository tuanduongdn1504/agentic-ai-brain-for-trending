# Caveats, Corrections & Verification Scorecard

How reliable the video is, claim by claim, and what we excluded per wiki-verify discipline.

## Scorecard — 14 claims

**7 CONFIRMED · 4 CORRECT-BUT-INCOMPLETE · 2 MISLEADING · 1 OVERSIMPLIFIED · 0 FALSE · 0 FABRICATED.**
Failure mode = **over-claim / omission, not fabrication.** This is a technically honest talk.

| # | Claim | Verdict | Note |
|---|---|---|---|
| C1 | SES sandbox = 200 emails/24h | **CONFIRMED** | + 1 msg/sec, verified recipients only |
| C2 | Production scales in fixed tiers 20K→50K→80K→100K→1M | **MISLEADING** | AWS publishes **no fixed tiers**; case-by-case on reputation |
| C3 | Host's max send rate = 14/sec | **CORRECT-BUT-INCOMPLETE** | Account-specific, not a universal default; sandbox is 1/sec |
| C4 | SES rejects overflow instantly, no auto-retry ("API not broker") | **CONFIRMED** | `ThrottlingException` / SMTP `454`; retriable *by the caller* (~10-min backoff) |
| C5 | 1M/day ÷ 86,400s ≈ 12/sec, 14/sec suffices | **CONFIRMED** | Verbal "60×60×60" garble; correct is 60×60×24; conclusion right |
| C6 | Inline send is an anti-pattern (dual-write + peak cascade) | **CONFIRMED** | Both failure modes real |
| C7 | Pipeline = Outbox→SQS→Lambda→SES→SNS→DB/blacklist | **CORRECT-BUT-INCOMPLETE** | Sound + standard; missing DLQ, idempotency, explicit throttle, FIFO-if-ordered |
| C8 | **"SQS handles the 14/sec rate-limiting for you"** | **MISLEADING** | SQS only buffers; the **consumer** throttles — [[the-throttling-correction]] |
| C9 | SQS auto-retries + survives crash | **CORRECT-BUT-INCOMPLETE** | Durable yes; "auto-retry" is really visibility-timeout re-delivery → needs idempotency |
| C10 | SQS: 1M/mo free, then ~$0.40–0.44/M | **CONFIRMED** | $0.40 Standard / $0.50 FIFO; "0.44" slightly high |
| C11 | SQS > RabbitMQ/Kafka (managed, native, auto-scale) | **CONFIRMED** | All three reasons hold |
| C12 | SES publishes bounce/complaint/delivery events (with reasons) via SNS | **CONFIRMED** | Send/Delivery/Bounce/Complaint/Reject/…; hard vs soft; IANA MARF complaint types |
| C13 | High bounce rate can suspend your account | **CONFIRMED** (thresholds sharpened) | **>5% under review, >10% paused**; complaint >0.1% |
| C14 | 3-table DB design + partitioning | **OVERSIMPLIFIED** | Right shape; missing idempotency key, correlation ids, retention, partition key — [[database-design]] |

## The two things to un-learn

1. **"SES has quota tiers."** It doesn't — increases are negotiated per account on your demonstrated reputation. Don't plan a product roadmap around a guaranteed 20K→…→1M ladder.
2. **"SQS throttles to SES for you."** It doesn't — it's a buffer. **Your consumer enforces the rate.** Implement it wrong and you'll flood SES and drop mail under load. This is the one place a junior following the video verbatim would ship a bug.

## Excluded per wiki-verify discipline (agent output NOT put in the wiki)

Following the vault rule that lens/verifier agents can confabulate — these were caught in the main loop and dropped:

- **A "self-correction on camera" ("nope, 86400 giây")** an agent attributed to the host for C5. The transcript at `[06:15]` shows the host *saying* the wrong factors then stating 86,400 — there is **no explicit self-correction**. We describe it accurately as a misspeak, not a self-correction.
- **A strawman "correction"** from the landscape agent claiming the host said "inline email send is fine because email is fast." **He said the opposite** (inline is wrong). Discarded — you can't correct a claim the source never made.
- **The host's real name / employer / location.** The creator agent (correctly, refute-first) found only the handle **@anonystick** and refused to assert identity. We assert only the handle. → [[source-and-creator]]
- **Version numbers (`vNNN`)** — none injected here, but flagged as a known synthesis-agent artifact from prior ships; autopilot wiki does not version.

## Genuinely unverified / open

- **Exact SES quota-increase SLA** — commonly "~24h" but no hard published SLA found.
- **Whether 14/sec is a *default* first-production grant** vs a custom bump — sources conflict; treated as account-specific (the conservative reading).
- **Whether SES returns a `Retry-After` header** on throttle — not confirmed in docs; assume not and use your own backoff.
- The host's **account-lockdown anecdote** — plausible, cataloged as illustrative; the documented mechanism is bounce/complaint reputation, not key-sharing per se.

## Key Takeaways

- **Trust the architecture; correct two over-claims** (fixed tiers, SQS-throttles) and add the four omitted production pieces.
- **0 FALSE / 0 FABRICATED** — this is a high-integrity source, comparable to the corpus' cleanest technical talks.
- Wiki-verify caught **3 agent embellishments** (fake self-correction, strawman correction, would-be PII) — logged here so the pattern is visible for future ships.
