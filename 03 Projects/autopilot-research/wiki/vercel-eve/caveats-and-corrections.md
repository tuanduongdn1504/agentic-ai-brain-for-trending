# Eve — caveats & corrections

## Source
- Verification workflow `wf_e215817b-a5d` (incl. an independent completeness critic that returned **NEEDS-REVISION** with mandated caveats, folded in below). Bundle `raw/2026-07-18-vercel-eve/`.

## ❌ Corrections (things sources got wrong)

1. **Timeframe — FALSE → corrected.** openclaw: agent deployments went <3%→29% *"in 6 months."* **Vercel's own blog: "A year ago… less than 3%. Now around 29%."** → the shift took **≈1 year**, not 6 months.
2. **Security posture — MISLEADING → corrected.** Rob Shocks framed deployed agents as *"completely open,"* needing manual security. In fact **credential brokering (OAuth + token refresh) and code sandboxing are framework-managed by default**; "openness" is about deployment/residency config, not insecure defaults.
3. **Lock-in wording — overstated.** "Core features run on Vercel *proprietary* infra" is misleading: durability uses the **open-source WDK**, sandbox/observability/gateway have **adapters/fallbacks**. It's **pragmatic** lock-in (best-on-Vercel), not hard lock-in.

## ❓ Unverified — reported by creators, absent from Vercel docs (do NOT treat as fact)

- **"Vercel Connect = $3 per 10K token requests"** (Elie Steinbock) — no such pricing or product name in Vercel's blog/README/pricing.
- **`eve build` → standard Nitro output for self-hosting** (Sonny Sangha) — undocumented; Vercel's path is `vercel deploy`.
- **Sandbox auto-selection fallback chain** (Docker → lighter VM → pure JS) — only adapter *support* is documented, not the order/logic.
- **Repo caching internals** (~5GB template image + copy-on-write) — undocumented.
- **"Scales to thousands/millions of concurrent users"** — no published capacity/throughput; it's beta.
- **Subagent independence** — independent model selection / per-subagent sandboxes / delegation trigger are **not** confirmed (only "isolated context + restricted tools").

## ⚠️ Mandated caveats (from the completeness critic)

1. **BETA / PUBLIC PREVIEW, no GA date.** APIs/behavior can break. Unsuitable for production-critical systems until GA + a stability SLA + reference customers. **Internal-tooling pilots only** for now.
2. **Data-residency documentation gap = HARD BLOCKER for any candidate-touching use.** No public statement on where agent state / conversation logs / eval results / sandbox output are stored/retained, or whether Vercel trains on inputs/outputs. This alone blocks adoption under the operator's candidate-LLM ADR (EU AI Act Annex III). See [[vercel-eve/hireui-translation]].
3. **Anchor-source bias.** Cole Medin **disclosed a Vercel collaboration** on the anchor video — treat as Vercel-adjacent reporting; independent claims here are cross-checked against Syntax + Vercel docs.
4. **No independent security audit.** "Credentials never reach the model" + sandbox isolation are framework claims on a June-2026 launch with **no published third-party audit, CVE history, or threat model**.
5. **Cost model absent.** No pricing for durable-session state storage, cron at scale, or sandbox resources → cannot forecast deployment cost.

## Gaps (worth a follow-up / next deepening)

- **Vercel "Passport" / shadow-AI governance** — a real adjacent feature (The Register) not covered in this bundle. Natural N=2 deepening, and directly relevant to governance/compliance.
- **Mastra head-to-head** — the vendor-neutral rival deserves its own comparison (durability via Inngest, self-host path).
- **Post-GA:** data-residency guarantees, security audit, production case studies, pricing, self-hosting story.
- **Recruiter-relevant integrations:** which of LinkedIn/Greenhouse/Workable/HRIS have prebuilt connectors vs. custom — unknown.

## Key Takeaways

- **1 FALSE (stat), 1 MISLEADING (security), 4 UNVERIFIABLE** — all corrected/flagged above.
- **The two adoption-blockers are non-technical:** beta status + an absent data-residency story.
- **Passport/shadow-AI** and a **Mastra comparison** are the highest-value follow-ups.

## See also
- [[vercel-eve/claims-scorecard]] · [[vercel-eve/hireui-translation]] · [[vercel-eve/vendor-lock-in-and-competitive-landscape]]
