# vercel-eve

> **Topic:** **Vercel Eve** — Vercel's open-source (Apache-2.0), filesystem-first framework for **durable AI agents**, launched at Vercel Ship London 2026-06-17 (PUBLIC PREVIEW/BETA). Core thesis: **"an agent is a directory."** Cataloged as a **full topic bundle + refute-first fact-check** — the mechanics are real; the failures are a timeframe error, a security overstatement, and a cluster of under-documented specifics.
> **Anchor video:** [`m8VC2SV2igM`](https://www.youtube.com/watch?v=m8VC2SV2igM) — Cole Medin, "This Completely Changes the Way We Build Production AI Agents (Vercel Eve)" (2026-07-16, 16:23, ~24.9K views, EN). **⚠️ creator disclosed a Vercel collaboration.**
> **Bundle:** 7 YouTube sources (operator anchor + yt-search) + primary Vercel docs. Ingested 2026-07-18 (path 1 `/loop` yt-dlp `en` captions → `vtt-to-md.py`, read in full; ~29.1K words; `notebook_id: none`). Manifest: `raw/2026-07-18-vercel-eve/_sources.md`.
> **Verified:** primary-source grounding (Vercel blog `introducing-eve` + `github.com/vercel/eve` README + changelog) + Workflow `wf_e215817b-a5d` (40 agents: 7 digests → consolidate → 30 refute-first verifiers → synthesis → independent completeness critic; 0 errors/0 empty; ~1.58M tokens).
> **Corpus-first:** FIRST dedicated **agent-framework** topic (vs. coding-agent/harness topics); FIRST **Vercel-authored** framework topic; FIRST "directory-as-agent" pattern entry.

## The one thing to remember

**Eve is "Next.js for agents" — a real, well-designed reliability stack (durable checkpointing, `needsApproval` HITL, evals-as-deploy-gate, credential brokering, MCP-native) wrapped in a genuinely novel filesystem-first packaging — but it's BETA, Vercel-optimized, and ships with NO data-residency story.** For hireui that means **BORROW its patterns now, AVOID it for candidate-facing LLM work, WATCH it for recruiter-side automation post-GA.**

## Verification scorecard

**30 load-bearing claims: 14 CONFIRMED · 10 CORRECT-BUT-INCOMPLETE · 4 UNVERIFIABLE · 1 FALSE · 1 MISLEADING · 0 fabricated.**
- **FALSE:** the "<3%→29% in 6 months" stat — Vercel says **"a year ago"** (≈1 year).
- **MISLEADING:** deployed agents are "completely open / need manual security" — creds-brokering + sandboxing are **framework-managed by default**.
- **Don't quote as fact:** $3/10K "Vercel Connect" pricing · `eve build`→Nitro self-host · sandbox fallback order · "scales to millions."

## Articles

- [[vercel-eve/what-is-eve-directory-is-an-agent]] — core thesis, launch/license/status, positioning.
- [[vercel-eve/primitives-and-file-structure]] — the **10 directories** + the compilation/auto-discovery step.
- [[vercel-eve/production-features]] — durability (open-source WDK), `needsApproval` HITL, evals-gate, credential brokering, sandbox, OTel observability.
- [[vercel-eve/deployment-and-claude-code-plugin]] — `init → eve dev → vercel deploy`; the Claude Code/Cursor plugin (Eve skills + Vercel MCP); self-host caveat.
- [[vercel-eve/vendor-lock-in-and-competitive-landscape]] — pragmatic-not-hard lock-in; Mastra/LangGraph/AgentKit/Flue/Dawn.
- [[vercel-eve/claims-scorecard]] — all 30 claims by verdict.
- [[vercel-eve/caveats-and-corrections]] — corrections, unverified claims, mandated caveats, gaps (incl. **Passport/shadow-AI**).
- [[vercel-eve/sources-and-stances]] — the 7 sources, stances, biases, primary sources.
- [[vercel-eve/hireui-translation]] — **AVOID candidate-facing / WATCH recruiter-side / BORROW 3 patterns.**

## Key Takeaways

- **What it is:** Apache-2.0 filesystem-first durable-agent framework by Vercel; agent = folder of markdown + TypeScript, auto-compiled into a wired manifest.
- **Real & strong:** durable checkpointed sessions (open-source WDK), HITL approvals, evals deploy-gate, credential brokering (keys never reach the model), MCP-native connections, multi-channel.
- **Novelty = packaging, not components** (durability/sandbox/gateway already existed) — the DX + distribution is the moat, à la Next.js.
- **Two adoption blockers are non-technical:** BETA (no GA date, no audit) + **absent data-residency documentation**.
- **Lock-in is pragmatic, not hard** — but **Mastra** is the vendor-neutral alternative to reach for.
- **hireui:** borrow credential-brokering + evals-gate + `needsApproval` + filesystem-legibility into the Mosh A2 seam / agent-nativity spec **now**; don't put candidate PII near Eve until residency + GA + audit land.
- **Anchor source (Cole Medin) is Vercel-collaborated** — corroborated against Syntax (independent) + Vercel's own docs.

## Cross-links
[[claude-skills/_index]] · [[claude-code-plugins-stack/_index]] · [[claude-code-skills-stack/_index]] · [[agent-development-lifecycle/_index]] · [[external|Storm Bear: career-ops]]

## Suggested next actions / deepenings
- **N=2 deepening: Vercel "Passport" + shadow-AI governance** (adjacent, compliance-relevant, gap here).
- **Mastra head-to-head** (vendor-neutral rival — durability via Inngest, self-host path).
- Re-visit at **Eve GA** for data-residency guarantees, security audit, pricing, self-hosting story.
