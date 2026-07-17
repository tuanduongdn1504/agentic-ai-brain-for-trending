# aws-email-at-scale-sqs-lambda-ses

> **Topic:** How large systems send ~1 million emails/day on AWS without losing messages — the Outbox → SQS → Lambda → SES → SNS pipeline, taught by the Vietnamese backend channel **Tips Javascript (@anonystick)**.
> **Source video:** [`HnQ0Wt6YyO0`](https://www.youtube.com/watch?v=HnQ0Wt6YyO0) "Show dự án với cách mà các công ty lớn gửi hàng triệu email | AWS SQS, Lambda & SES" (2026-07-15, 16:13, ~1.3K views).
> **Ingested:** 2026-07-17 (path 5 yt-dlp `vi-orig` auto-subs → `vtt-to-md.py` → 35-paragraph transcript read in full in the main loop; `notebook_id: none`).
> **Verified:** Workflow `wf_d65df574-01a` (11 agents: 6 dives → 3 refute-first verifiers → 2 synthesizers; ~702K tokens, 133 tool calls, 0 errors/0 empty) + 5 main-loop WebSearch/WebFetch anchors on the load-bearing numbers.
> **Corpus-first:** the corpus' FIRST AWS / message-queue / transactional-email-at-scale topic, and the first Solution-Architect-framed subject.

## The one thing to remember

**SES is an API, not a queue.** Fire more than your per-second rate and it rejects the overflow *instantly* (`ThrottlingException` / SMTP `454`) with no auto-retry. The whole architecture exists to put a durable buffer (SQS) in front of SES and a *rate-limiting consumer* (Lambda) between them. The video's single real error: it says **"SQS handles the rate-limiting for you"** — it doesn't. SQS only buffers; **your consumer must throttle.** See [[the-throttling-correction]].

## Articles

| Article | What's in it |
|---|---|
| [[overview]] | What the video teaches, the problem, the corrected mental model, the verdict scorecard summary |
| [[ses-limits-and-throttling]] | SES sandbox (200/day, 1/sec) vs production quotas, the 14/sec rate, `ThrottlingException`, "API-not-broker" (C1–C5) |
| [[the-throttling-correction]] | **The headline fix** — where the rate-limit is *actually* enforced (consumer, not SQS); visibility-timeout ≠ auto-retry (C8, C9) |
| [[the-correct-pipeline]] | Outbox → poller → SQS → Lambda → SES → SNS → DB/suppression, step by step + what the video under-covered (DLQ, idempotency) (C6, C7) |
| [[sqs-and-alternatives-and-cost]] | SQS pricing, SQS vs RabbitMQ/Kafka, and the build-vs-buy question the video skipped (managed ESPs) (C10, C11) |
| [[bounce-complaint-and-suppression]] | SNS events, hard/soft bounces, complaints, the SES *automatic* suppression list vs an app-level blacklist, and the bounce-rate suspension thresholds (C12, C13) |
| [[database-design]] | The three tables (outbox / suppression / audit), corrected status codes, idempotency keys, partitioning (C14) |
| [[hireui-translation]] | Mapping the pattern to hireui's transactional email — adopt-now / defer / recruitment-specific risks / the smallest useful pilot |
| [[caveats-and-corrections]] | The 14-claim scorecard, every correction, and the agent confabulations excluded per wiki-verify discipline |
| [[source-and-creator]] | Video metadata, the @anonystick channel + TRYBUY series context, and how this was verified |

## Cross-links

- [[../fullstack-docker-cicd/_index]] — the deploy layer this infra sits on
- [[../api-security-7-techniques/_index]] — sibling AWS/backend topic; SES rate-limiting is a rate-limiting cousin, and the multi-tenant reputation risk echoes its BOLA/multi-tenant theme
- [[../hoidanit-fullstack-vibe-coding/_index]] — sibling VN NestJS backend educator (the two most directly comparable creators in the corpus)
- [[../mosh-ai-powered-apps/_index]] — hireui's *other* backend integration (the first LLM feature); this is the email seam next to it

## Key Takeaways

- The architecture the video teaches is **the industry-standard AWS transactional-email pattern** and it is verified sound: transactional Outbox → SQS buffer → rate-limited consumer → SES → SNS bounce/complaint feedback → DB + suppression.
- **0 FALSE, 0 FABRICATED** claims across 14 checked. The two soft spots are *over-claims*, not fabrications: "SES has fixed quota tiers" (it's case-by-case) and "SQS does the throttling" (the consumer does).
- For **hireui** specifically: the killer risk isn't scale (it's nowhere near 1M/day) — it's **bounce-rate account suspension from bulk outreach to stale candidate emails**. Suppression-before-send is the adopt-now item; SQS/SNS is deferrable.
