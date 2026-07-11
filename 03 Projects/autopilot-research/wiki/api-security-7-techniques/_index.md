# api-security-7-techniques

> **"7 API security techniques you must know"** — a viral 7-min explainer, verified against the canonical layer beneath it. The operator-submitted video is a **Vietnamese adaptation** ([LetDiv](https://www.youtube.com/watch?v=XuzRt-BFIKU), 9.2K subs, 2026-07-06) of the **original English resource** ([Hayk Simonyan](https://www.youtube.com/watch?v=FsB_nRGdeLs), 136K subs, **2025-08-12, 438K views**) — the double-dive target. Both present the same 7 techniques in the same order: **Rate Limiting · CORS · SQL/NoSQL Injection · Firewall/WAF · VPN · CSRF · XSS**.
>
> **The double-dive's payload:** because both videos are the *same* explainer, depth comes from verifying that knowledge against **OWASP (API Security Top 10 2023 + the CSRF/XSS/SQLi cheat sheets), MDN CORS, NIST Zero Trust (SP 800-207), RFC 6585, AWS/Cloudflare WAF docs**.
>
> **Source:** [XuzRt-BFIKU](https://www.youtube.com/watch?v=XuzRt-BFIKU) (VN) ← [FsB_nRGdeLs](https://www.youtube.com/watch?v=FsB_nRGdeLs) (original) · [raw](../../raw/2026-07-11-api-security-7-techniques.md) · ingested 2026-07-11 (path 5 yt-dlp; both transcripts read in full).
> **Status:** compiled · 14 files. Verified via Workflow `wf_0d90e641-e67` (21 agents: 9 canonical dives + 11 refute-first claim verdicts + completeness critic; ~940K tokens, 195 tool calls) + a read-only hireui posture recon.

## The verdict in one line

The 7 techniques are a **decent starter taxonomy but not a sufficient one** — every single claim needs a caveat, and the videos **completely omit authorization (BOLA/BOPLA/BFLA)**, which is the #1 real-world API-breach class and hireui's top risk. Scorecard across 11 checked claims: **0 fully-correct · 5 correct-but-incomplete · 2 oversimplified · 4 misleading · 0 refuted-as-false.**

## Articles

- [[overview]] — the 7 techniques, the thesis, and the video-vs-canonical scorecard.
- [[video-summary]] — annotated chapter-by-chapter walkthrough of both videos + what LetDiv changed.
- [[rate-limiting]] — scopes (per-endpoint / per-user / per-IP / global), why per-IP is weak, the **per-username bucket** + **shared Redis** the videos omit, and "rate limiting ≠ DDoS defense."
- [[cors-is-not-a-security-control]] — **the load-bearing correction.** CORS relaxes the same-origin policy; it does *not* block requests or stop a non-browser attacker.
- [[injection-sql-and-nosql]] — parameterized queries are #1; ORMs are not automatic; **NoSQL injection is a different beast** parameterization doesn't fix.
- [[firewall-and-waf]] — WAF is signature-based L7 defense-in-depth (evadable, ≠ network firewall), not a complete solution.
- [[network-isolation-and-vpn]] — "network location is not identity" (NIST Zero Trust); VPN alone is necessary-not-sufficient; cloud SaaS uses VPC + IAM.
- [[csrf-cookie-vs-token]] — **the applicability flip:** CSRF only bites *cookie* auth; Bearer/JWT APIs are immune. SameSite is the modern primary defense the videos skip.
- [[xss-httponly-and-csp]] — context-aware encoding + framework auto-escape + CSP + **HttpOnly** (which neutralizes the videos' *own* cookie-theft example).
- [[what-the-videos-miss-owasp-api-top-10]] — **the headline gap.** The authorization trio (API1/API3/API5) dominates breaches and is absent from all 7.
- [[hireui-security-posture]] — read-only recon of the real hireui repo: Bearer/JWT auth (CSRF N/A, localStorage-token amplifies XSS), frontend-only repo, BOLA backend-dependent, CSP commented out.
- [[caveats-and-corrections]] — Rule 12 ledger: the full claim-by-claim verdict table.
- [[source-provenance]] — the Hayk → Substack/gitconnected → C#Corner/DEV.to/JavaRevisited → LetDiv chain (none cite OWASP/ByteByteGo — Hayk's own synthesis).

## The payload worth stealing

1. **Invert the priority:** authorization-first (BOLA audit) *before* the videos' 7 hygiene techniques.
2. **Decide, don't implement blindly:** CSRF is a *skip* for hireui's Bearer-token API; that decision is an ADR, not a code change.
3. **Ship the cheap frontend wins now:** CSP headers (currently commented out), the one unsafe URL-interpolation site, CORS-is-not-authz documentation.

→ Pilot methods (**24 across A–E tiers + Scrum + skip-list + critic reframe**): [`output/(C) 2026-07-11-api-security-pilot-methods.md`](../../output/(C)%202026-07-11-api-security-pilot-methods.md)

## Closest siblings

[[miai-cv-matching-agent]] (recruitment-domain code audit) · [[mosh-ai-powered-apps]] (hireui's first LLM feature / vendor seam — the endpoint this secures) · [[ai-engineering]] (demo→production discipline) · [[hoidanit-fullstack-vibe-coding]] / [[system-thinking-ai-coding]] (VN first-party educators; junior-onboarding) · [[fullstack-docker-cicd]] (the deploy layer where WAF/edge lives) · [[google-zero-open-web]] (platform/economics lens).
