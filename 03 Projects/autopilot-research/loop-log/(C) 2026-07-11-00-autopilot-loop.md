# (C) Autopilot Loop — 2026-07-11-00

> **Trigger:** /loop (manual, operator-submitted single video URL)
> **Topic:** api-security-7-techniques (NEW)
> **Started:** 2026-07-11 (main-loop session)
> **Ended:** 2026-07-11
> **Mode:** path 5 (yt-dlp only) + double-dive into the ORIGINAL resource + canonical-layer verification (Workflow) + read-only hireui recon

## Request

"Build knowledge from https://www.youtube.com/watch?v=XuzRt-BFIKU and double deep dive into the original resource for knowledge in this video. Then pilot to apply knowledge into my working flow, show me many methods."

## What the source turned out to be

- **Operator video:** LetDiv (VN, 9.2K subs) "7 Kỹ Thuật Bảo Mật API…" — a faithful **Vietnamese adaptation**.
- **The original resource (double-dive target):** **Hayk Simonyan** "API Security Explained…" (`FsB_nRGdeLs`, 2025-08-12, 438K views, 136K subs) — identical 7-technique list/order/examples, 11.7 months earlier. LetDiv credits no source.
- Because both videos are the *same* explainer, the "double deep dive" targeted **the canonical authority beneath the knowledge** (OWASP / MDN / NIST / RFC / AWS-Cloudflare), where the real depth + corrections live.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 2 videos + canonical layer | 1 (new topic) | 0 | **1.0** |

Cold-start NEW topic (gaps_at_start = 1). After compile: index + 14 articles, all cross-linked, no stubs, no TODO markers → gaps_at_end = 0.

## Sources ingested

- `raw/2026-07-11-api-security-7-techniques.md` — both full transcripts (Hayk EN + LetDiv VN) + provenance + chapter map.

## Verification work

- **Workflow `wf_0d90e641-e67`** — 21 agents (9 canonical dives + 11 refute-first claim verdicts + 1 completeness critic), ~940K tokens, 195 tool calls, **0 errors / 0 empty / 0 verifier misfires**.
- **Read-only hireui recon** (Explore agent) — mapped auth model (Bearer/JWT localStorage), ORM (frontend-only), rate-limiting (absent), CORS (backend), BOLA (high-risk, backend-dependent), XSS surface (low but amplified by localStorage token), CSP (commented out), deploy edge (ambiguous).

## Wiki articles created

- `wiki/api-security-7-techniques/_index.md` (NEW topic)
- `wiki/_master-index.md` (UPDATED — added topic at top)
- 13 articles: overview · video-summary · rate-limiting · cors-is-not-a-security-control · injection-sql-and-nosql · firewall-and-waf · network-isolation-and-vpn · csrf-cookie-vs-token · xss-httponly-and-csp · what-the-videos-miss-owasp-api-top-10 · hireui-security-posture · caveats-and-corrections · source-provenance
- Pilot deliverable: `output/(C) 2026-07-11-api-security-pilot-methods.md` (24 methods + Scrum + skip-list + critic reframe)
- `raw/_inventory.md` (UPDATED — row added, raw marked compiled)

## Findings scorecard (11 claims, refute-first)

- 0 fully-correct · 5 CORRECT-BUT-INCOMPLETE · 2 OVERSIMPLIFIED · 4 MISLEADING · 0 refuted-as-false.
- **Headline gap:** authorization (BOLA/BOPLA/BFLA) absent from all 7 — the #1 real API-breach class and hireui's top risk.
- Sharpest conceptual corrections: CORS-is-not-a-security-control; CSRF-is-cookie-auth-only (hireui's Bearer/JWT ⇒ skip).

## Final metric

- `gaps_closed_ratio` = **1.0**
- Stop reason: target_ratio reached (single-cycle complete compile; no unprocessed raw remaining).

## Top unclosed gaps / follow-ups

1. hireui **backend** claims (rate limiting, ORM/injection, BOLA enforcement, JWT `exp`/rotation, CORS reflection) are marked *backend-dependent, not verified* — the backend repo wasn't in scope. A backend recon would close these.
2. hireui **production edge** ambiguous (vercel.json vs appspec.yml) — confirm before any WAF decision (pilot C6).
3. No OWASP-topic sibling existed before; future API-security or auth topics should cross-link here.

## Suggested next action

Pilot **A1 (BOLA / object-ownership audit)** on hireui's backend as the highest-value security work — it's the #1 real risk and orthogonal to all 7 video techniques. In parallel ship the two cheap frontend wins (**B2 CSP headers**, currently commented out; **A4's `searchLocation` interpolation fix**) and write the **B4 CSRF-skip ADR**. All per hireui's CONSTITUTION (I-2 agent-* branch, I-8, GitNexus-first). See `output/(C) 2026-07-11-api-security-pilot-methods.md`.
