# Source & Creator

## Video

| Field | Value |
|---|---|
| Title | "Show dự án với cách mà các công ty lớn gửi hàng triệu email \| AWS SQS, Lambda & SES" |
| Translation | "Showcasing a project on how big companies send millions of emails — AWS SQS, Lambda & SES" |
| URL / ID | https://www.youtube.com/watch?v=HnQ0Wt6YyO0 |
| Channel | **Tips Javascript** ([@anonystick](https://www.youtube.com/@anonystick)) |
| Uploaded | 2026-07-15 (ingested 2 days later, 2026-07-17) |
| Length / Views | 16:13 / ~1,349 views |
| Language | Vietnamese |
| Category | People & Blogs |

## Creator (@anonystick)

- **Independently verified** (main-loop WebSearch, not just agent output): "Tips Javascript" is the YouTube arm of **anonystick** — blog [anonystick.com](https://anonystick.com/), GitHub [github.com/anonystick](https://github.com/anonystick) (~93 repos), Facebook [TipJS](https://www.facebook.com/TipJS/). A **Vietnamese developer community** focused on JavaScript / Node.js / NestJS / Go / database / backend / system design.
- **Identity held to the handle only.** In the video the host calls himself "Anistic" / "Tip" (a caption garble of the handle). Per wiki-verify refute-first discipline, **no real name, employer, or location is asserted** — none was found on the official channel/about pages.
- **Series context:** this episode belongs to the channel's high-concurrency / large-data project series built around **TRYBUY** — their e-commerce + developer-social-network project, whose backend stack is publicly described as **NestJS, TypeORM, Redis, Elasticsearch, AWS**. The prior episode covered duplicate-payment idempotency (Stripe-style, DB ACID); this one references an earlier "video 33" for the Outbox pattern and prior videos on partitioning and Lambda.
- **Framing:** pitched as **Solution-Architect** practice — "design the architecture and analyze the problem before coding" — with a recurring note that the SA role is highly valued / well-paid in the IT job market. A member/course funnel (NestJS "Note ZS" backend series) sits alongside the free video.

## Corpus placement

- **Corpus-first** on three counts: first AWS topic, first message-queue / cloud-infrastructure topic, and first transactional-email-at-scale subject. Also the first **Solution-Architect-framed** whiteboard-design talk.
- **Creator neighbors:** the most comparable corpus creators are the other Vietnamese backend educators — [[../hoidanit-fullstack-vibe-coding/_index]] (Eric / Hỏi Dân IT, NestJS beginner series) and the VN adaptation channel in [[../api-security-7-techniques/_index]] (LetDiv). anonystick sits at the more senior / architecture end of that group.
- **Not Anthropic-related**; no Claude/AI-agent content — this is pure backend cloud architecture.

## How this was verified

- **Ingest:** path 5 yt-dlp `vi-orig` auto-subs → `bin/vtt-to-md.py` → 35-paragraph `[mm:ss]` transcript, **read in full in the main loop** (`raw/2026-07-17-aws-email-at-scale-sqs-lambda-ses.md`; `notebook_id: none`).
- **Workflow `wf_d65df574-01a`** — 11 agents: 6 research dives (SES / SQS / SNS+events / architecture patterns / creator / landscape) → 3 refute-first verifiers over the 14 claims → 2 synthesizers (corrected playbook + hireui translation & completeness critic). ~702K tokens, 133 tool calls, **0 errors / 0 empty / 0 skipped**; dives on Haiku 4.5, verify + synth on Opus 4.8 (high effort).
- **Main-loop anchors (independent of the agents):** 5 WebSearch/WebFetch checks on the load-bearing numbers — SES sandbox/quotas, SES throttling behavior, SQS pricing, the throttle-location question, and the bounce/complaint thresholds — plus an independent WebSearch confirming the @anonystick ↔ Tips Javascript ↔ TRYBUY linkage. All corroborated the corrected wiki.
- **Independent collision check:** grep of `wiki/_master-index.md` + `raw/_inventory.md` confirmed no prior AWS/queue/email topic (matches were false positives). Verified in the main loop, not via agent.
- **Authoritative sources** cited throughout are AWS's own docs (SES quotas / rate-limiting / event-publishing / reputation-dashboard / suppression-list; SQS pricing / Lambda-with-SQS; the AWS Messaging blog on preventing email throttling).

## Key Takeaways

- Real, live, verifiable VN backend educator (**@anonystick**), architecture-tier; identity intentionally held to the handle.
- The video is the corpus' first cloud-infrastructure / email-at-scale entry and part of the TRYBUY project series.
- Verification combined an 11-agent adversarial workflow with independent main-loop anchors on every quotable number — see the scorecard in [[caveats-and-corrections]].
