# (C) Pilot Methods — mosh-ai-powered-apps → your working flow

> **Source:** wiki/mosh-ai-powered-apps/ (12 articles, compiled 2026-07-03, adversarially verified wf_05723834-938)
> **Context anchors:** hireui = Goal #2 target with **zero LLM integration today** and a ready-made build-it-right spec (`hireui/_bmad-output/runbooks/claude-api-cost-optimization-spec-2026-06-15.md`); `evals/` harness exists from the prompt-evaluation pilot; hireui CONSTITUTION applies (I-2 agent-* branches, I-8 operator-only skill registry).
> **What this topic uniquely adds:** every prior pilot improved *how you build* (harnesses, specs, skills). This one is the first that builds *the product feature itself* — the course is an implementation-grade recipe for hireui's first LLM feature, and its layered seam + the [[openai-to-claude-mapping]] article make it Claude-native.

**24 methods, ranked within groups. Effort: S <2h · M half-day · L 1–3 days.**

---

## A. hireui Goal #2 — the first LLM feature (the bullseye group)

- **A1 · HEADLINE — Candidate-feedback summarizer, Claude-native, on the course's seam (L).** The paid course's review-summarizer project ≈ hireui's candidate-feedback summarization (the Amazon-archetype). Build it per the course's shape — Zod-validated Express route → service → `llm/client.ts` — but with `@anthropic-ai/sdk` + the wiki's mapping article as the spec, and your cost-optimization spec's caching/model-tier rules baked in from line 1. This converts Goal #2 from "methodology evidence" to "shipped product capability." *Composes with A4 + A6 + C3. Execute hireui-rooted, agent-* branch.*
- **A2 · Build the vendor seam FIRST as infrastructure (M).** Before any feature: add the course's platform-agnostic layer to hireui — `llm/client.ts` + a `ChatResponse`-style interface + a conversation/message repository. Mosh's repo proves the seam works (it already fronts OpenAI+Ollama+HF); yours fronts Claude and leaves the door open for a Kimi bake-off (omnilogin thread). Every later AI feature becomes a one-file addition.
- **A3 · Candidate triage/routing — the Freshdesk archetype (M).** Single-call classification: new application → category/priority/queue. Haiku 4.5, structured outputs (`output_config.format` from your existing Zod schemas), temperature-free. Cheapest possible first feature if A1 feels big; same seam.
- **A4 · Per-candidate Q&A chat — the Redfin archetype (L).** The course's chatbot, translated: conversation repository stores the **transcript** (not a response-id pointer) in Postgres; prompt caching breakpoint on the last turn so resent history reads at ~0.1×; client-generated conversation GUIDs exactly as taught. This is the Candidate-Detail screen's natural AI companion — an "ask about this candidate" panel.
- **A5 · LLM-route security/cost posture as a checklist (S).** From [[chatbot-validation-and-errors]]: Zod `safeParse` 400s + `.trim().min(1).max(1000)` prompt cap (cost/DoS guard) + try/catch JSON 500s + Claude-typed-error branches (`RateLimitError`, `stop_reason: max_tokens/refusal`). Apply to every AI route hireui ever ships; pairs with the E1 impersonation-sweep from the jsm-practical-vibe-coding menu.
- **A6 · Eval-first twist — supply what the course lacks (M).** The course ships ZERO tests. Before A1 goes live, wire your `evals/` harness (prompt-evaluation pilot) to grade summarizer outputs (code-grader for shape via Zod, model-grader for faithfulness with reasoning-before-score). The measured eval report is itself a Goal-#2 artifact.

## B. Steal the paid half for free (repo group)

- **B1 · Read the review-summarizer + prompt-engineering code in the public repo (S–M).** The complete PAID course code is public (`mosh-hamedani/ai-powered-apps-course`, no purchase needed): the summarizer implementation, its prompts, Prisma persistence, and the Ollama/HF providers. One focused reading session = the paid half's knowledge, feeding A1 directly. ⚠️ NO LICENSE — patterns yes, file-copying no.
- **B2 · Diff Mosh's multi-provider `llm/client.ts` against your seam design (S).** Before writing A2, read how one file fronts three providers — the cheapest design review available for your abstraction.
- **B3 · Ollama local-model leg (M, optional).** The repo's tinyllama path + the course's privacy criterion → a local-model option behind the same seam for sensitive-data experiments (composes with cowork-third-party-inference + self-hosted-devops threads). Only if a real privacy requirement shows up.

## C. Cost & token discipline (the 13× group)

- **C1 · Per-feature model-tier memo (S).** Apply the course's 6-criteria framework to each planned hireui AI feature; assign Haiku/Sonnet/Opus per feature *in the cost spec* before any code. The 13× lesson: model choice is the biggest cost lever and it's free.
- **C2 · `count_tokens` baseline harness (S).** Measure real candidate-profile/feedback payloads via `POST /v1/messages/count_tokens` (never tiktoken for Claude — undercounts 15–20%). Feeds C1's memo with real numbers and sets `max_tokens` sanely.
- **C3 · Caching-verified conversation design (M).** Bake the wiki's billing fact in: chained/multi-turn conversations bill full history on BOTH vendors; the savings live in caching. Acceptance test for A4: `cache_read_input_tokens > 0` on turn 2+, asserted in the eval harness.
- **C4 · Prompt-length budget as product policy (S).** The course's max-1000-chars is a *product decision* (input-token cap). Set per-feature input budgets in hireui's spec — the input-side twin of `max_tokens`.

## D. Personal / vault workflow

- **D1 · Repo-first, video-optional consumption rule (S).** The wiki + public repo now supersede the 2h25m video for you. Skip watching; read [[the-originals]] + B1. Keep the video link for teammates who learn by watching.
- **D2 · Workbench-before-code teaching ritual (S).** Mosh's playground-first pedagogy, Claude-flavored: demonstrate temperature/effort/structured-outputs in the Anthropic Console workbench before showing SDK code — your standard move when onboarding anyone to the Claude API.
- **D3 · Queue Mosh's "Claude Code for Professional Developers" (9h) as a future topic (S).** Reported-unverified in his catalog; verify it exists, then it's a natural drain: the biggest mainstream educator teaching your daily tool. Add to raw/topics-queue.md.
- **D4 · Vendor-seam audit of your own sandboxes (S).** `sandbox/claude-cost-arc/` and future demos: do they hardcode the SDK into route handlers, or keep a seam? Ten-minute audit; refactor next time you touch them.

## E. Scrum-coaching / team leverage

- **E1 · The six-archetype product-discovery workshop (M).** Amazon-summaries / campaign-drafts / translate / moderation / routing / per-entity-chat as a card deck; teams map each archetype onto their own backlog. Concrete, vendor-neutral, and produces a ranked AI-feature backlog in one session — reusable across clients.
- **E2 · The database analogy as stakeholder language (S).** "AI engineer : model :: backend dev : MySQL" — the cleanest one-liner in the corpus for de-mystifying AI hiring and roadmap talk with non-technical stakeholders; verified consistent with Chip Huyen's definitions.
- **E3 · AI-engineer vs ML-engineer role clarity (S).** Use the distinction to head off "we need to hire ML PhDs" conversations — most SaaS AI features are AI-engineering (pre-trained models + product integration), not ML research.

## F. Skip-list (explicitly not worth piloting)

- **Buying the course ($29/mo)** — the code is public and the free half is in the wiki; buy only if you want the guided walkthrough experience itself.
- **Adopting Bun in hireui** — conformance beats taste (Rule 11); hireui has its tooling. Bun stays a sandbox-only option.
- **The `previous_response_id` / Map-chaining pattern on Claude** — Claude is stateless; resend-history + caching is the correct translation (A4). Don't emulate OpenAI's state model.
- **Any concrete model/pricing number from the video** — GPT-4.1/4o/o3 are retired; frameworks yes, numbers no.
- **Copying repo files into hireui** — NO LICENSE. Patterns only.

---

## Critic's reframe (read before picking)

Every prior Goal-#2 pilot candidate has been *methodology* (cc-sdd, six-files, loops, verify harnesses) — evidence about *how* you'd build. This topic is the first *what*: an actual LLM feature recipe matching hireui's domain, with the operator's existing assets (cost-optimization spec, evals harness, verify loop, CodeRabbit-style review) supplying exactly the three things the course omits (cost discipline at production grade, tests/evals, deployment posture). The strongest move is therefore **not another bake-off** but the A2→A1→A6 chain: seam, then summarizer, then evals — one week, and Goal #2 has a shipped, measured, Claude-native product feature. The methodology pilots then have something real to be measured *on*.

**Suggested next action:** say the word and the A2 seam spec (file list + interfaces + branch plan per hireui CONSTITUTION) gets drafted for the next hireui session — or pick any method above by ID.
