# SES Limits & Throttling — "an API, not a broker"

The design constraint the whole architecture is built around. Covers claims C1–C5.

## Sandbox vs production

| | Sandbox (default) | Production (account-specific) |
|---|---|---|
| Daily quota | **200 emails / 24h** | Higher; negotiated per account |
| Send rate | **1 email/sec** | Account-specific (host's = **14/sec**) |
| Recipients | Only verified addresses / the SES mailbox simulator | Any |

- **C1 — CONFIRMED:** SES sandbox = 200 messages/24h, 1 msg/sec, verified recipients only. Persists until you request and receive production access. ([AWS: request production access](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html))
- **C2 — MISLEADING:** the video presents a fixed escalation ladder **20K → 50K → 80K → 100K → 1M/day**. **AWS publishes no such tier structure.** Quota increases are evaluated **case-by-case** by AWS Support based on sender reputation, content quality, and use case. The ladder is likely the host's own account history, not AWS policy. ([AWS: request a quota increase](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas-request-increase.html))
- **C3 — CORRECT-BUT-INCOMPLETE:** "14 emails/sec" is real but is the **host's account allocation**, not a universal default. Sandbox is uniformly 1/sec; production per-second rates are account-specific. (14/sec is a *commonly cited* early-production rate — historically bundled with the "50,000/day" first grant — but it is not a guaranteed standard tier.)

## The capacity math (C5 — CONFIRMED)

- 1,000,000 emails ÷ **86,400 seconds/day** ≈ **11.57 emails/sec**.
- A 14/sec cap therefore *suffices* for 1M/day.
- 86,400 = 60 × 60 × **24**. The host verbally garbled the factors ("60 × 60 × 60", which is 216,000) but used the correct 86,400 and reached the correct conclusion. Harmless misspeak; the reasoning is sound.

## The core insight: SES rejects overflow instantly (C4 — CONFIRMED)

- Exceed your per-second send rate and SES returns a **synchronous `ThrottlingException`** ("Maximum sending rate exceeded", `MessageRejected`); over SMTP it's **`454 Throttling failure`**.
- **SES does not queue the overflow and does not auto-retry it.** The message is gone unless *your* code catches the error and retries. AWS recommends backing off up to ~10 minutes before retrying.
- This is why the host's framing is correct and worth memorizing: **"SES is an API, not a broker."** Unlike Kafka/SQS, it has no built-in buffer or retry — all of that is on the developer. ([AWS: SES rate limiting](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html), [ThrottlingException / 454 behavior](https://www.courier.com/error-solutions/aws-ses-rate-limit))

## Why this forces an async architecture

If SES silently queued and retried, you could call it inline and forget about it. Because it doesn't, you need:
1. Something durable to hold messages during a burst → **SQS** ([[the-correct-pipeline]]).
2. Something that meters sends to stay under the cap → **the consumer** ([[the-throttling-correction]]).
3. Something to catch the rejections and retry → **consumer backoff + visibility-timeout re-delivery** ([[the-throttling-correction]]).

## Key Takeaways

- Sandbox 200/day @ 1/sec is a hard wall until you request production access; **verify a test suite hasn't silently burned the daily quota.**
- The "quota tiers" ladder is anecdotal — plan for **case-by-case increases gated on your bounce/complaint reputation**, not a guaranteed path to 1M.
- The load-bearing fact: **overflow is rejected instantly with no retry.** Everything downstream exists to work around this.
