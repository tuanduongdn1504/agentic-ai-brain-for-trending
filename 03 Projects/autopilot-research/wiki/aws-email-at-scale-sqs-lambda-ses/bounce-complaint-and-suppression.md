# Bounce, Complaint & Suppression — protecting your account from getting paused

The feedback half of the pipeline, and the risk that actually kills email systems. Covers claims C12 and C13.

## SES event publishing via SNS (C12 — CONFIRMED)

Configure an SES **Configuration Set** to publish email-outcome events to an **SNS topic** (or EventBridge). Event types SES emits:

- **Send, Delivery, Reject, RenderingFailure, DeliveryDelay, Open, Click, Subscription** — plus the two that matter most:
- **Bounce** — split into **hard/Permanent** (address doesn't exist, blocked) vs **soft/Transient** (mailbox full, temporary). Carries the receiving server's SMTP **diagnostic code** (e.g. `5.1.1` no such user).
- **Complaint** — recipient marked the mail as spam. Carries a `complaintFeedbackType` per the IANA MARF standard (`abuse`, `auth-failure`, `fraud`, `not-spam`, `other`, `virus`).

Your SNS subscriber (Lambda or webhook) reads these and reacts. **Recommended: filter the SNS subscription to just Bounce + Complaint** unless you need delivery/open/click — fewer invocations, less cost. ([AWS: monitor sending activity](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html), [notifications via SNS](https://docs.aws.amazon.com/ses/latest/dg/notifications-via-sns.html))

## Why this matters: bounce/complaint rates can pause your account (C13 — CONFIRMED)

The host's warning — "high fail rate can get your account locked, it happened to me" — is real and quantified. SES watches your **reputation** and escalates account status **Healthy → Under review → Sending paused**:

| Metric | Threshold | Consequence |
|---|---|---|
| **Bounce rate** | **> 5%** | Account placed **under review** |
| **Bounce rate** | **> 10%** | **Sending paused** |
| **Complaint rate** | **> 0.1%** | Concerning; review likely |
| **Complaint rate** | sustained **> 0.5%** | **Sending paused** |

- AWS frames exact numbers as guidance (evaluated per-account), but the 5%/10% bounce and ~0.1% complaint figures are consistently documented. Best practice: keep **bounce < 5%, complaint < 0.1%**, and alarm well below (e.g. 2% / 0.05%). ([AWS: bounce/complaint thresholds](https://repost.aws/knowledge-center/ses-reputation-dashboard-bounce-rate), [reputation dashboard](https://docs.aws.amazon.com/ses/latest/dg/reputation-dashboard-dg.html))
- The host's own anecdote (account locked after sharing SES keys with students in a course) is *plausible* — the mechanism was almost certainly **elevated bounce/complaint rates from untrained senders**, not the key-sharing itself. We catalog it as illustrative, not as a documented cause.

## Two suppression lists — SES's automatic one AND your own

A nuance the video's "blacklist table" only half-covers:

1. **SES automatic suppression list** — account-level, maintained *by AWS*. When an address hard-bounces or complains, SES can auto-add it and silently drop future sends to it. Useful but **opaque** (you can't easily audit it, and it's account-wide). ([AWS: suppression list](https://docs.aws.amazon.com/ses/latest/dg/sending-email-suppression-list.html))
2. **Application-level suppression table** — *your* DB table (the video's "bảng cấm"/blacklist). Needed **in addition** because it's:
   - **Auditable** for compliance (who was suppressed, when, why, with the diagnostic code).
   - **Checkable before you queue** — query it in the poller so bad addresses never enter SQS (fail-fast, no queue pollution). → [[the-correct-pipeline]]

**Handling policy** (recommended, sharper than the video):
- **Permanent bounce (5xx):** suppress immediately, never re-send.
- **Transient bounce (4xx):** retry once; if it fails again, suppress.
- **Complaint:** always suppress immediately (complaints hurt reputation far more per event than bounces).

## Key Takeaways

- SES emits **Bounce/Complaint/Delivery/etc. events to SNS**; subscribe a handler, filter to Bounce+Complaint, and feed results back into your DB.
- **Reputation is the real constraint, not throughput:** bounce **>5% = review, >10% = paused**; complaint **>0.1%** is dangerous. Alarm at half those.
- Keep **both** suppression lists: SES's automatic one *and* an auditable app-level table you check **before queuing**. This is what stops a stale recipient list from getting your whole account suspended — the central risk for [[hireui-translation]].
