# Source provenance & verification method

## The provenance chain (verified)

The specific **7-technique grouping** originates with **Hayk Simonyan**, not OWASP or ByteByteGo. Dated chain:

| Date | Artifact | Note |
|---|---|---|
| **2025-08-12** | Hayk Simonyan **video** [FsB_nRGdeLs](https://www.youtube.com/watch?v=FsB_nRGdeLs) (438K views, 136K subs) | **The original.** |
| ~Sept 2025 | Hayk's **Substack** + **Level Up Coding (gitconnected)** written versions | Author's own text version. |
| 2025-11-18 | **C# Corner** article (identical title) | Downstream repost, **unattributed**. |
| 2025-12-24 | **DEV.to** Spanish translation (Julio Santacruz) | Downstream, **unattributed**. |
| 2026-02-24 | **JavaRevisited Substack** (identical title) | Downstream, **unattributed**. |
| **2026-07-06** | **LetDiv** VN video [XuzRt-BFIKU](https://www.youtube.com/watch?v=XuzRt-BFIKU) (9.2K subs) | The operator-submitted adaptation, **11.7 months** after the original. |

## Evidence LetDiv is the derivative (not the origin)

1. **Upload-date precedence** — Hayk 11.7 months earlier.
2. **Title** — LetDiv's is a direct Vietnamese translation of Hayk's.
3. **Structure** — identical 7-technique list, order, and section boundaries.
4. **Examples** — identical illustrations: SQL `--` bypass, bank-CSRF-via-session-cookie, blog-comment-XSS-steals-cookie, per-endpoint/per-IP/overall rate limiting.
5. **Attribution** — LetDiv's description credits **no source**; it links only to LetDiv's own course + blog + socials (verified in the raw metadata). This closes the provenance dive's one open uncertainty (it couldn't fetch the LetDiv description; the main loop had it).

## Does Hayk cite anyone?

**No.** Hayk's published materials cite neither OWASP nor ByteByteGo. The 7-technique grouping appears to be **his own synthesis** of standard security knowledge. Note: ByteByteGo's own API-security material (May-2024 blog + cheatsheet) uses a *different* framework (HTTPS/OAuth/API-keys/rate-limiting/allowlisting/gateway…), so this is **not** a ByteByteGo derivative — a guess we explicitly checked and discarded rather than assumed.

## How this topic was sourced

- **Path 5 (yt-dlp only, operator-submitted single video → original resource).** No NotebookLM.
- **Ingest:** `yt-dlp --dump-json` for both videos' metadata; `yt-dlp --write-auto-subs` for captions (VN `vi` for LetDiv, EN `en` for Hayk). Both transcripts converted to timestamped text via `python3.12` (the machine's `python3` shim is broken) and **read in full in the main loop**.
- **Raw artifact:** [`raw/2026-07-11-api-security-7-techniques.md`](../../raw/2026-07-11-api-security-7-techniques.md) — both full transcripts + provenance + chapter map.

## The "double deep dive" into the original resource

Because both videos are the *same* explainer, the dive target was **the canonical authority beneath the knowledge**, not a second video:

- **9 canonical dives** (Workflow `wf_0d90e641-e67`, high-effort): one per technique + one for the OWASP API Top 10 gap analysis + one provenance chain. Each fetched primary sources: OWASP API Security Top 10 2023, the OWASP CSRF/XSS/SQLi/NoSQL/DoS/Bot-Management/Credential-Stuffing cheat sheets, MDN CORS, NIST SP 800-207 (Zero Trust), RFC 6585 (HTTP 429), AWS WAF + Cloudflare docs.
- **11 refute-first claim verdicts** — each video claim adversarially checked against the dive ground truth (methodology + scorecard in [[caveats-and-corrections]]).
- **1 completeness critic** — synthesized the gaps + the hireui pilot direction.
- **Read-only hireui recon** (separate Explore agent) — mapped the real repo's auth model, ORM, rate-limiting, CORS, BOLA surface, XSS surface, CSP, and deploy target. Findings in [[hireui-security-posture]].

Workflow totals: **21 agents, 0 errors, 0 empty results, ~940K tokens, 195 tool calls.**

## Reception (not verified beyond platform counts)

- Hayk video: 438K views / 136K subs — genuinely viral; the repost trail is consistent with that reach.
- LetDiv video: ~9.6K views / 9.2K subs at capture (2026-07-11). Small VN channel. Treat popularity as marketing.

## Key Takeaways

- Sourcing is transparent and reproducible: **video → original video → OWASP/MDN/NIST/RFC canonical layer.**
- The "original resource" was correctly identified by upload-date precedence + structural identity + a discarded ByteByteGo hypothesis — **not fabricated** (prime-directive discipline).
- The dive was **right-sized to a summary-of-canonical-knowledge**: the canonical layer *is* the deep resource, so the effort went into OWASP verification rather than a second-video fan-out.
