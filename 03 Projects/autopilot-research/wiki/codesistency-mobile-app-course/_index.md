# Codesistency — Ultimate Claude Code Tutorial for Mobile Apps (FULL COURSE)

> **Topic type:** hands-on full-course walkthrough (Claude Code + React Native/Expo mobile app, "Triply")
> **Source:** Codesistency (@codesistency, ~151K subs) — YouTube `p80OV6kjIO8`, 2026-07-04, 3h33m
> **Ingested:** 2026-07-14 (ad-hoc main-loop path) · **Raw:** `../../raw/2026-07-14-codesistency-claude-mobile-app-course.md`
> **Verification:** workflow `wf_46c5932a-849` (8 clusters × dive+refute) + 3 main-loop overrides. Scorecard: [[claims-scorecard]].

## One-line

A 3.5-hour, explicitly **anti-vibe** course that builds and nearly ships a real AI trip-planner mobile app with Claude Code driving a full production tool stack, using a repeatable **plan → design → build-with-verify-loop → AI-review → PR/merge** workflow. Unusually high factual integrity for a sponsor-heavy tutorial.

## Articles

- [[overview]] — what the course is, what gets built ("Triply"), who it's for
- [[the-anti-vibe-workflow]] — the 6-step workflow that IS the product of the course
- [[screenshot-verify-loop]] — the distinctive "screenshot the simulator, compare to the design, loop until identical" technique
- [[production-tool-stack]] — the full stack, what each tool does, and free-tier reality
- [[agents-md-vs-claude-md]] — ⚠️ headline correction: Claude Code does NOT natively read AGENTS.md (the presenter's *setup* is right, his *claim* is wrong)
- [[webhooks-inngest-background-jobs]] — Clerk→Neon user sync via webhooks + Inngest jobs + the Experiments A/B feature
- [[sentry-observability-layer]] — logs / tracing / session replay / AI-agent monitoring, and why it matters
- [[app-store-readiness]] — delete-account requirement, privacy/terms/support, legal-page deploy
- [[claims-scorecard]] — all ~40 factual claims verified, with verdicts
- [[caveats-and-corrections]] — the corrections + the Rule-12 agent overrides (SDK 57, Skool, Inngest)
- [[source-provenance]] — channel, presenter (Burak), BulkyAI app, sponsors
- [[hireui-pilot-menu]] — what an operator can actually port to a real product (Goal #2)

## Corpus positioning

- **Direct sibling:** [[jasonlee-claude-mobile-app]] — same genre (Claude Code mobile-app tutorial, plan-first + design-first). **Contrast:** jasonlee = revenue-titled, looser vibe; Codesistency = disciplined, far larger production stack, explicit verify-loop + AI-review gate. This is the *disciplined* mobile sibling.
- **Workflow kin:** [[jsm-practical-vibe-coding]] (Context7 + CodeRabbit + AGENTS.md), [[mosh-ai-powered-apps]] (first-LLM-feature vendor seam), [[ai-web-design-workflow]] (design-as-gate), [[hoidanit-fullstack-vibe-coding]] (anti-vibe beginner discipline), [[system-thinking-ai-coding]] (design-before-prompt).
- **AGENTS.md finding aligns with** [[github-copilot-cli-agents]] (Claude Code AGENTS.md non-support, issue #6235).

## Headline findings

1. **The workflow is the real deliverable, not the app.** Plan-mode interview → `PLAN.md` phases → GPT-image designs → screenshot-verify-loop → manual test → CodeRabbit PR review → branch/merge. Repeatable across projects.
2. **Every tool in the stack is real and current** (Expo, Clerk, Neon, Drizzle, Inngest incl. Experiments, ImageKit, Sentry incl. AI-agent monitoring, CodeRabbit, Context7). No vaporware.
3. **One genuine technical error:** the claim that Claude Code natively reads `AGENTS.md` is false — but the setup he actually shows (CLAUDE.md → references AGENTS.md) is the correct workaround. See [[agents-md-vs-claude-md]].
4. **Provenance is mostly self-report:** "BulkyAI shipped in 14 days / first customer in 5 days" is **unverifiable** (no App Store listing found under that name), though a `bulkyai.app` legal-pages site exists.
