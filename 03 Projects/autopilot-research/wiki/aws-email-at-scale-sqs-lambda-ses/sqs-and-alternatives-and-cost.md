# SQS, Alternatives & Cost — and the build-vs-buy question the video skipped

Covers claims C10 and C11, plus the landscape the video never addressed.

## SQS pricing (C10 — CONFIRMED)

- **1,000,000 requests/month free** — permanent free tier, all customers, all regions (except GovCloud). Resets monthly; unused portion does not roll over.
- Beyond free tier: **Standard ≈ $0.40 / million requests** (volume discounts kick in after 100B). **FIFO ≈ $0.50/million.**
- The video's "$0.40–0.44" is right for Standard (0.44 is slightly high but in range).
- **A "request" is an API call, not a message** — and a message's `SendMessage` + `ReceiveMessage` + `DeleteMessage` are separate requests, plus messages >64KB count as multiple. At transactional-email volumes this is still effectively free; at 1M emails/day (~60M+ requests/month) SQS is ~$12–15/month — **negligible next to SES**, which dominates the bill. ([AWS SQS pricing](https://aws.amazon.com/sqs/pricing/))

## Why SQS over RabbitMQ / Kafka (C11 — CONFIRMED)

All three of the host's reasons check out:

| | SQS | RabbitMQ | Kafka |
|---|---|---|---|
| **Ops** | Fully managed, zero infra | Self-host or AWS MQ ($) | Self-host or MSK ($$) |
| **AWS integration** | Native: Lambda event-source, SNS fan-out, CloudWatch | None native | None native |
| **Scaling** | Auto, no config | Manual | Manual/complex |
| **Best for** | Transactional workloads on AWS | AMQP standard, no vendor lock-in, multi-cloud | Extreme throughput + stream processing |
| **Rough cost** | ~$0 here | ~$200–600/mo (AWS MQ) + ops | ~$500+/mo (MSK) + ops |

- **SQS wins for this use case** because it's managed, cheap, and natively wired to the exact services in the pipeline (SES → SNS → SQS → Lambda → CloudWatch).
- **RabbitMQ** trades that for AMQP portability / no lock-in — worth it if multi-cloud matters.
- **Kafka is overkill** for transactional email (it's built for trillions of stream events); only relevant if you're *also* doing stream processing.

## The question the video never asks: build vs buy

The video assumes you'll hand-build the whole pipeline on SES+SQS. For most teams that's the wrong default — a **managed Email Service Provider (ESP)** already ships the hard parts (suppression lists, bounce/complaint handling, reputation management, delivery logging, webhooks) behind one REST call.

| Volume | Recommendation | Why |
|---|---|---|
| **< ~100K emails/month** | **Managed ESP** (Postmark / SendGrid / Resend / Mailgun) | ~$15–20/mo + a few hours of integration; bounce/complaint/suppression handled for you. Building the SES pipeline (~40–80 eng-hours) isn't worth it. |
| **> ~100K–1M+/month, AWS-native** | **SES + SQS + Lambda** | SES ≈ $0.10 / 1K emails wins decisively at high volume (1M/day ≈ ~$100–150/mo for SES; SQS ≈ free). You pay in engineering effort and by owning suppression/reputation logic yourself. |

Illustrative crossover: at 1M/day, Postmark-style per-email pricing (~$1.20–1.80 / 1K) would run into the tens of thousands/month → SES clearly wins. At a few thousand/month, the ESP wins on total cost of ownership once you price in engineering time. **This trade-off is the biggest thing missing from the video** — it teaches *how* to build the SES pipeline without asking *whether* you should.

## Key Takeaways

- SQS is effectively **free** at transactional-email volume; **SES is the real cost driver** at scale.
- The host's SQS-vs-RabbitMQ/Kafka reasoning is correct: **managed + native AWS integration + auto-scale.** Kafka is overkill here.
- **Decide build-vs-buy first.** Under ~100K/month, a managed ESP beats hand-building SES+SQS on total cost. The SES pipeline earns its keep at high volume or when you specifically need AWS-native control. (Directly relevant to [[hireui-translation]], which is nowhere near the crossover.)
