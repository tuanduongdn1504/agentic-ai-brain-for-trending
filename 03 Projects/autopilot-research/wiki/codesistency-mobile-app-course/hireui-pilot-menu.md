# hireui pilot menu

What an operator can actually port from this course to a real product (Goal #2). hireui is a **web SaaS recruitment platform** (Next.js), not a mobile app — so the *app-specific* parts (Expo, native tabs) don't transfer, but the **workflow, the review gate, the async/experiment patterns, and the deletion/privacy discipline** do. Tiers: **A** = zero/low-risk now · **B** = scoped spike · **C** = larger build · **D** = decision/ADR.

> Follow hireui's own CONSTITUTION when working there: `agent-*` branches (I-2), operator-only skills (I-8), GitNexus-first. See the hireui pilot-target memory. Nothing here ships to `main` without operator review.

## A — zero/low-risk, this week

- **A1 — Screenshot-verify loop on one hireui screen.** ⭐ Port the [[screenshot-verify-loop]] to a Playwright/Chrome screenshot of a real hireui screen (e.g. the Candidate-Detail refactor spike already in flight): give Claude the Figma export as the reference, have it screenshot the running app and iterate to match. Pairs directly with the existing `candidate-detail-refactor-spike` (Figma is the source of truth there). Zero product risk (UI-only, on an `agent-*` branch). Compare against the Taste-Skill gate from [[ai-web-design-workflow]].
- **A2 — CodeRabbit on one hireui PR.** Enable CodeRabbit's free tier on a single `agent-*` PR and measure catch-rate vs your current review. The course shows its concrete value (it caught a Sentry sample-rate / hard-coded-`isDev` issue Claude had missed). Low cost, reversible, and it's already corpus-validated in [[jsm-practical-vibe-coding]].
- **A3 — Plan-mode interview + `PLAN.md` for the first LLM feature.** Run the "senior technical co-founder interview" prompt in Plan Mode to spec hireui's first LLM feature (Match-Explain), and keep a living `PLAN.md`. Cheap, and it front-loads the alignment the vault's [[system-thinking-ai-coding]] and [[pocock-real-feature-build]] both argue for.

## B — scoped spike

- **B1 — Inngest Experiments behind the Match-Explain rollout.** ⭐ The best product-grade idea in the course. When hireui ships its first LLM feature (the Match-Explain seam from [[mosh-ai-powered-apps]] / [[miai-cv-matching-agent]]), route it through an **Inngest experiment**: 90% control / 10% new prompt-or-model, and read the built-in latency/failure/cost metrics before ramping. This is a concrete, low-risk LLM-migration primitive and complements the eval-gate in [[prompt-evaluation]]. **Data-residency caveat:** Inngest routes execution through its cloud unless self-hosted — decide before candidate PII flows through it (see D2).
- **B2 — Webhook-driven cascade delete for candidate data.** Implement the [[webhooks-inngest-background-jobs]] pattern for hireui's "right to erasure": a deletion event → background job that wipes the candidate across auth store + DB + any derived/embedding data. This is a GDPR/PDPL obligation for a recruitment product, not a nice-to-have.

## C — larger build

- **C1 — Sentry AI-agent monitoring on the first LLM feature.** Once an LLM feature is live, wire Sentry's AI-agent monitoring (token/cost/latency per call) for the *product's* calls — the counterpart to the agent-observability work in [[claude-code-observability]]. **Keep Session-Replay masking ON** (candidate PII on screen). Larger because RN-style manual instrumentation isn't needed on web, but wiring + dashboards + alerting is real work.
- **C2 — Branch-per-feature + AI-review as the standard loop.** Adopt the course's full loop (feature branch → PR → CodeRabbit → fix-commits → merge) as hireui's default `agent-*` workflow, measured over a sprint. Bake-off against the current process.

## D — decisions / ADRs

- **D1 — AGENTS.md / CLAUDE.md ADR.** Codify the finding from [[agents-md-vs-claude-md]]: **CLAUDE.md is the guaranteed-read file for Claude Code; a portable AGENTS.md must be symlinked or `@import`ed from CLAUDE.md.** Prevents a silently-ignored instructions file. Aligns with the ADR already implied by [[github-copilot-cli-agents]].
- **D2 — Managed-cloud vs residency ADR for background jobs / observability.** Inngest, Sentry, Neon, Clerk, ImageKit all route data through vendor clouds. For candidate PII, decide the residency posture explicitly — the same fence-line drawn in [[local-ai-coding-agents]] (strongest = local) and [[google-ai-studio-github-import]] (weakest = free tiers that train). Recommendation: "redact/route sensitive fields locally, reason in cloud" behind the Match-Explain seam.

## Recommended sequence

**A1 + A2 now** (UI verify-loop + CodeRabbit gate — both reversible, both corpus-reinforced) → **A3 → B1** (plan the LLM feature, then ship it behind an Inngest experiment) → **D1 + D2** ADRs before any candidate PII flows to a vendor cloud → **B2 / C1** as the feature matures.

## What NOT to port

- Expo / native tabs / Expo dev builds — mobile-only, irrelevant to a web SaaS.
- The "everything's free" framing — hireui is past the learning stage; price the real tiers.
- Disabling Session-Replay masking — never, for a PII product.
