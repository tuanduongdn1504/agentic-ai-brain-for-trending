# jsm-six-file-context

> **Topic index.** JavaScript Mastery's **Six-File Context System + spec-driven agentic build workflow** — a 4-hour mainstream build-along in which Adrian Hajdin ships a real SaaS ("Ghost AI") claiming *"I didn't write a single line of it"*, teaching: architecture-first design → six context files read in order → 29 numbered feature specs → one-new-chat-per-spec → vendor agent skills → CodeRabbit review → progress-tracker as memory. The app itself **automates the methodology it teaches** (AI design-agent draws architecture diagrams; AI spec-generator emits Markdown specs).
>
> **Entry point:** [14RP8liACqo](https://www.youtube.com/watch?v=14RP8liACqo) — "How Senior Engineers Actually Build With AI in 2026", JavaScript Mastery (1.25M subs), uploaded **2026-05-01**, 3:58:17, ~680K views. FIRST-PARTY (the methodology author's own channel). Full ~40.3K-word transcript read.
>
> **Originals (double deep-dived):** [adrianhajdin/ghost-ai](https://github.com/adrianhajdin/ghost-ai) (240★, **no license**, the methodology materialized: six `context/` files + 29 feature-specs + AGENTS.md/CLAUDE.md + 19 vendor skills) · [vercel-labs/skills](https://github.com/vercel-labs/skills) `npx skills` CLI (24.8K★, skills.sh) · official vendor skill repos (`clerk/skills`, `prisma/skills`, `liveblocks/skills`, `triggerdotdev/skills`) · Next.js 16.2 "AI Improvements" blog (AGENTS.md-by-default + bundled docs + **"AGENTS.md outperforms skills" eval**) · the email-gated six-file guide (reconstructed from repo, gate not needed) · obra/superpowers plan traces.
>
> **Verification:** Workflow `wf_2c3bd01a-8f0` (41 agents: 9 lenses + 20-claim adversarial verify incl. 5 panels; ~2.02M tokens, 670 tool calls). **Session-limit outage killed 13 panel verifiers + synthesis mid-run** — main loop took over synthesis and closed every dead panel with primary-source ground-checks (Next.js blog, gh api, transcript grep). 6 lens misfires corrected, 1 fabricated quote caught. Full ledger: [[source-provenance]] + [[caveats-and-corrections]].

---

## Articles

- [[overview]] — the thesis, the meta-loop (app automates its own methodology), the economics (Sonnet 4.6 + context files over Opus 4.7), role definition ("you are the architect, agent is just a coder").
- [[six-file-context-system]] — anatomy as implemented: per-file structure + token sizes (~14–15K total), strict reading order, load-bearing hierarchy (progress-tracker → architecture-context → ai-workflow-rules), invariants, scoping rules, strengths/weaknesses.
- [[feature-spec-workflow]] — the canonical meta-prompt, spec template shape (prose + Scope Limits + Check When Done; NOT EARS), the 06/07 split rationale, new-chat-per-spec token discipline, batch-fix degradation evidence, `current-issues.md` analyze-first pattern, on-camera failures + recoveries.
- [[skills-supply-chain]] — **headline**: vendor-published skills + `skills-lock.json` + `.agents/skills/` with `.claude/skills` symlinks via `npx skills`; skills NOT auto-consulted (verified); the reactive Liveblocks rescue; Vercel's AGENTS.md-vs-skills tension.
- [[agents-md-claude-md-portability]] — AGENTS.md as entry point; the official Next.js 16.2 managed block (markers official, wording variant); CLAUDE.md = `@AGENTS.md` + 35KB vendored Trigger.dev docs (pattern reversal); Feature-08-via-Codex portability demo.
- [[verification-and-review]] — **no test infrastructure exists** (verified); ad-hoc verification; CodeRabbit's two integration patterns and what it caught; contrast with Pocock/Anthropic verify discipline.
- [[ghost-ai-product]] — the app as artifact: stack, design-agent (Gemini 2.5 Flash + 8 canvas tools + Liveblocks atomic mutations), generate-spec (Blob + Prisma persistence), Trigger.dev rationale + honest nuance, 3 deployment failures.
- [[the-originals]] — per-artifact provenance of all 11 originals with verification state.
- [[originality-and-reception]] — repackaged prior art (spec-kit/OpenSpec/memory-bank/context-engineering, none cited), the mainstreaming signal, productivity counter-discourse, course funnel.
- [[caveats-and-corrections]] — 17-item don't-re-fabricate ledger + caption garbles + verified quotes.
- [[source-provenance]] — capture method, workflow stats, session-limit outage + main-loop takeover, misfire ledger, disclosed gaps.

## Pilot methods (how to apply this to your flow)

A ranked menu of **25 methods + skip-list + critic's reframe** lives in **`output/(C) 2026-07-03-jsm-six-file-context-pilot-methods.md`** — spanning: hireui Goal #2 (six files + feature-specs on the Candidate Detail refactor; vendor skills for hireui's stack), the skills supply chain (npx skills + lockfile discipline), AGENTS.md portability composition with the antigravity/cc-sdd pilots, measurement bake-offs, vault applications, and Scrum-coaching angles.

## Cross-topic links

- [[../pocock-real-feature-build/_index]] + [[../pocock-agentic-workflow/_index]] — the corpus's other first-party worked example; grill-me/PRD/issues ≈ planning-AI/six-files/feature-specs; Pocock verifies per-commit with tests, JSM doesn't (sharpest contrast).
- [[../google-antigravity-skills/_index]] — the `.agents/skills/` + SKILL.md + AGENTS.md portability stack this repo ships in production form.
- [[../how-we-claude-code/_index]] — Anthropic's interview-first ≈ planning-AI conversation; agent-native verification is the gap here.
- [[../harness-engineering/_index]] — six files = individual-scale harness engineering; Sonnet-over-Opus-with-context = harness-compensates-for-model.
- [[../claude-code-memory-systems/_index]] — progress-tracker = curated memory file (Karpathy LLM-Wiki lineage).
- [[../claude-md-12-rules/_index]] — ai-workflow-rules.md overlaps Rules 1/2/3/6/10 (think-first, simplicity, surgical, token budgets, checkpoints).
- [[../multi-agent-orchestration/_index]] — design-agent/generate-spec = simple orchestrator-worker productized.
- [[../ai-engineering/_index]] — the product's prompt→diagram→spec pipeline is a Ch.6-style agent app; the workflow's missing eval layer is Ch.3–4.
- [[../claude-code-skills-stack/_index]] + [[../claude-skills/_index]] — the skills landscape this vendor-skills wave extends.
- [[../codex/_index]] — Feature 08 cross-agent demo; Codex as substitutable executor.
- [[../workflow-ai-coding/_index]] + [[../10x-claude-code/_index]] — survey-level context for the practices here.

## Key Takeaways

- **Six lean context files + numbered specs + one-chat-per-spec** is a zero-install, agent-agnostic SDD on-ramp — weaker than cc-sdd on verification, stronger on approachability.
- The **skills supply chain** (vendor repos + lockfile + `.agents/skills` symlinks) is the topic's most durable artifact — skills now have a package manager, and framework vendors publish skills like SDKs.
- **Vercel's own evals favor AGENTS.md-bundled context over skills** (100% vs 79%) — the always-on vs on-demand context question is now first-party-measured; design harnesses accordingly.
- The methodology's verified soft spot: **discipline without automated verification** — pair its scoping rules with a real test/verify loop.
- Mass-market signal: SDD + agent harnesses have left the practitioner bubble; expect juniors arriving with this vocabulary.
