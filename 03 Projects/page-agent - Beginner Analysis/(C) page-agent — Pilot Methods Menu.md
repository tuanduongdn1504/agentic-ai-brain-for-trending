# (C) page-agent — Pilot Methods Menu (LLM Wiki v199)

**24 concrete ways to apply `alibaba/page-agent` to your working flow**, laddered A → F by cost/risk. page-agent is a free MIT client-side JS library — the payoff here is unusually direct because **hireui is a recruitment SaaS web app and page-agent is literally *"ship an AI copilot in your product in lines of code, no backend rewrite."*** That also means the fence matters (client-side keys, candidate PII in the DOM).

> **⭐ One-thing path: A1 → C11 → D16.** Read the loop + dehydration to see what it does → drive a scratch clone of hireui with your own Claude key to prove the loop → prototype a *read-only* recruiter copilot ("find candidates in Hanoi with React, open the top match") on an `agent-*` branch. That's a real, small, first Goal-#2 product artifact.

> **Fence (load-bearing):** `install-snapshot` + `npm-security-check page-agent` before install · **BYOK only, never the free demo proxy** (it egresses page HTML to Alibaba Cloud China; tech-eval only; EU-do-not-use) · **candidate PII lives in the dehydrated DOM** → use `transformPageContent` to redact + a no-training LLM provider · **never inline a real API key in a shipped IIFE bundle** (proxy the key server-side / short-lived tokens) · leave `execute_javascript` OFF · scratch clone before real hireui · pin `page-agent@1.11.0` · on hireui follow its CONSTITUTION (I-2 `agent-*` branch, I-8 operator-installs, GitNexus-first; hireui has no LLM spend yet → build-it-right, not a retrofit).

---

## A. Read + learn (zero install, ~1–3 h)

1. **Read the ReAct loop + the dehydration engine** (`(C) page-agent — Deep Dive.md` §4–§5, then `PageAgentCore.ts` + `page-controller/src/dom/`). Goal: internalize "give the model an indexed DOM text map + let it act by integer" — the cheapest correct way to let an LLM drive a UI. ⭐ the one thing to actually understand.
2. **Read the system prompt** (`packages/core/src/prompts/system_prompt.md`) as an *agent-honesty* exemplar: "it's ok to fail," "never assume an action succeeded," captcha→ask-the-user, "trying too hard can be harmful." Compare against your own loop-verifier / v189 discipline.
3. **Trace the browser-use lineage** (README acknowledgments + `@note Adapted from browser-use`). See exactly what page-agent *inherited* (DOM-as-text, the ReAct loop) vs *added* (in-page delivery). This is the corpus's cleanest example of one subject building openly on another (browser-use v41).
4. **Map the config surface** (`(C) Deep Dive.md` §8): note the three "safe-to-embed" levers — `experimentalScriptExecutionTool` off-by-default, `transformPageContent` redaction hook, `instructions.getPageInstructions(url)` per-route guidance.

## B. Borrow patterns into vault/hireui — zero install (~half-day each)

5. **Steal the MacroTool pattern** for any hireui LLM feature that needs "reflect + act in one call": one forced structured tool call carrying `{evaluation, memory, next_goal, action}`. Cheaper + more auditable than free-form tool loops. → composes with the mosh-ai vendor-seam thread.
6. **Steal `autoFixer` / `normalizeResponse`** as a hardening layer for *any* structured-output feature: repair JSON-in-content, double-stringified args, and missing-field → safe-default, instead of throwing on the first malformed response. Directly relevant if hireui ever runs a cheap/local model.
7. **Steal the two-stream separation** — persistent History (in LLM context) vs transient Activity (UI only), with transient errors kept *out* of the model's reasoning. A clean pattern for any agentic feature's state model.
8. **Steal the honesty-over-success prompt block** into your `05 Skills/` agent-behaviour skills ("never assume success; verify the expected change; it's ok to fail"). Reinforces the loop-verifier v189 REJECT-first stance.
9. **Steal the `transformPageContent` redaction hook idea** as a general rule: whenever you hand a real UI/data surface to an LLM, put a redaction/transform seam *between the surface and the model* — write it into hireui's LLM-feature spec now (before there's any spend).
10. **Steal the "index, not selector" idea** for hireui's own agent-facing surface: if you ever expose hireui state to an agent, hand back stable integer handles + a compact text map, not raw HTML/selectors (the token-economy + robustness win).

## C. Hands-on trial — scratch, low-risk (~1–3 h, ~cents)

11. **⭐ Drive a scratch clone with YOUR Claude key.** `npm install page-agent`, `new PageAgent({ model:'claude-...', baseURL:<Anthropic-compatible>, apiKey:<your key>, language:'en-US' })`, `await agent.execute('…')` on a *scratch copy* of a hireui screen. BYOK, not the demo proxy. Prove the observe→think→act loop end-to-end. (Claude is first-class — v1.9.0 shipped Opus 4.8 support.)
12. **Try the one-line demo bundle on a throwaway page** (`<script src="…page-agent.demo.js">`) to *feel* the SimulatorMask + AI cursor + panel UX — but on a **non-sensitive, disposable page only** (the demo LLM is the China proxy). Delete after.
13. **Measure the token economy.** Run 3 tasks; read `InvokeResult.usage` (`promptTokens`/`completionTokens`/`cachedTokens`). Compare a DOM-heavy page vs a lean one. This quantifies the "text-DOM = cheap" claim for *your* app and pairs with the ccusage/OTel observability pilot.
14. **Test the local-model path** (Ollama `qwen3:14b` per the developer-guide) to see how far a free local model gets on a real form — the "no cloud, no cost, no PII egress" configuration. Note where `autoFixer` saves the run.
15. **Try the MCP server (Beta)** against a scratch page: run `@page-agent/mcp`, connect Claude Desktop / a coding agent, call `execute_task` — feel the external-drive-the-in-page-agent direction (and the `window.confirm()` approval gate). Keep it local.

## D. hireui / Goal #2 — the real payoff, behind the fence (`agent-*` branch, scratch clone first)

16. **⭐ Prototype a READ-ONLY recruiter copilot** on a scratch hireui clone: "find candidates in Hanoi with React experience, open the top match," "filter this pipeline to interviewed-last-week." Read-only, no writes, own Claude key, `execute_javascript` off. This is the smallest real Goal-#2 product artifact — an in-app copilot that drives hireui's *existing* DOM, zero backend rewrite.
17. **Wire `transformPageContent` to redact candidate PII** before it reaches the LLM (names/emails/phones → tokens) — then decide the provider (no-training tier). Do this *first*; it's the gate that makes any hireui pilot defensible (GDPR + candidate data).
18. **Use `getPageInstructions(url)`** to give per-screen guidance (Candidate Detail vs Pipeline vs Job Post) so the copilot knows each screen's affordances — pairs with the Candidate-Detail refactor spike.
19. **Accessibility play:** expose hireui to recruiters who prefer natural-language / voice ("mark this candidate as advanced to interview") — page-agent's stated accessibility use case, and a genuine product differentiator for TalentAxis. Read-first, gated writes later.
20. **Smart-form-filling play:** the "turn a 20-click workflow into one sentence" use case maps onto hireui's admin/job-post forms — a concrete internal-tools win. Trial on a scratch form; measure clicks-saved.
21. **Compare vs building your own:** spike page-agent *vs* a hand-rolled Responses-API feature for one recruiter task; log which is faster to a working demo and which you'd own long-term (adopt-vs-build, the TNT-factory thread). page-agent's risk: a client-side agent driving your production DOM + the key-in-browser problem — weigh it.

## E. Off-goal / personal (optional)

22. **Personal accessibility / automation:** drop page-agent into an internal admin tool *you own* to natural-language-drive a tedious workflow (with your own key, non-sensitive data).
23. **Study the SimulatorMask** as a "the agent is driving" UX pattern — the animated cursor + interaction-blocking overlay is a reusable affordance for any autonomous-UI feature (users trust what they can watch).

## F. Vault-meta

24. **Write the "structured-surface-not-raw-dump" synthesis.** page-agent joins browser-use v41 (DOM-not-screenshot) → codebase-memory-mcp v172 (graph-not-file-reads) → fff v194 (resident-index-not-re-scan) → video-use v198 (transcript-not-frames). The recurring move: *give the model a compact structured surface + act by stable handle, never the raw bytes.* Worth a one-page Pattern-Library note — and a candidate CLAUDE.md line for your own agents. (Also log the genuine #57: page-agent derives from browser-use v41 — the corpus now openly links two of its own subjects.)

---

**Ladder placement vs the standing PILOT lever:** page-agent is the **sharpest in-app product pilot for hireui since serve-sim v183** (both because hireui is a web app and because page-agent is drop-in). But it is **higher-risk than the read-only pilots** (SkillSpector v169 / claude-tap v173 / fff v194) — it's an agent driving your production DOM, with candidate PII in the dehydrated surface and the client-side-key problem. So: read-only first (D16), redaction before anything (D17), BYOK not the demo proxy always, scratch clone before real hireui, and per the hireui CONSTITUTION.
