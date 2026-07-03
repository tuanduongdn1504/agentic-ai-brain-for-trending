# (C) Pilot methods — jsm-practical-vibe-coding → your working flow

> **Date:** 2026-07-03 · **Source topic:** `wiki/jsm-practical-vibe-coding/` (video Q7AYc2kECDI + Vision Agents deep-dive)
> **26 methods** across 7 categories. Effort: S (<30min) / M (half-day) / L (multi-day). Fit: ★☆☆ exploratory → ★★★ direct Goal-#2 lever.
> **Standing context:** hireui = Goal-#2 deployment target (Candidate-Detail refactor is the active surface; v189 loop running; cc-sdd #1 + six-file A7 bake-off queued); hireui has NO LLM feature yet; vault runs CLAUDE.md + this memory system.

## HEADLINE (if you do only three)

1. **A1 — four-part prompt discipline on the Candidate-Detail refactor** (S, zero install, orthogonal to the queued spec-system bake-offs — it's per-prompt hygiene, not a competing methodology).
2. **E1 — the impersonation-vuln sweep** (S/M, concrete security win harvested from CodeRabbit's on-camera catch).
3. **D2 — spec the hireui voice-screening/mock-interview agent as hireui's FIRST LLM feature** (M to spec, composes ai-engineering + multi-agent-orchestration + cost-optimization threads into one Goal-#2 artifact).

---

## A. Prompt discipline → hireui Candidate-Detail (zero-install, this week)

- **A1. Four-part prompt template** (S, ★★★): Every prompt in the refactor becomes: ① "Read `<harness file>` first and follow it strictly" ② ONE task ③ behavioral constraints ④ design reference. Drop into `.pilot-log` as a template. Measure: regression count per session vs current practice.
- **A2. Behavioral-constraints bank** (S, ★★★): Harvest the locked plan's invariants into a reusable block — "keep 3 tabs (Figma deviation locked)", "avatar 72px", "verified timeline #ECFDF5/#FEF2F2", "data/behavior/copy parity with web", "don't touch navigation". Paste as prompt-part-③ every time. This is the video's sharpest idea applied to your realest surface.
- **A3. Numbered design-PNG prompt material** (S, ★★☆): Replicate `prompt_material/01…07.png` — export the materialized Figma handoff screens as numbered per-feature PNGs and attach one per prompt ("match exactly; do not approximate"). You already have the SoT at `apps/claude-design-handoff/`.
- **A4. Verification-infrastructure prompting** (S, ★★☆): Ask for the dev affordance WITH the feature ("add a temp button to reset candidate state so I can verify the empty→loaded flow"), remove after verify. Encode in the template as an optional ⑤.
- **A5. Fix-prompt discipline in the v189 loop** (S, ★★☆): Escalation/fix messages become "problem + correct behavior + protective constraint" — no feature re-explanations. Applies directly to the babysitter's PR-comment format.

## B. AGENTS.md / context-file upgrades

- **B1. CLAUDE.md `@AGENTS.md` import bridge** (S, ★★★): Now Claude-docs-confirmed (code.claude.com/docs/en/memory). Do it in hireui (per CONSTITUTION, on an agent-* branch) and optionally the vault → one canonical context file, readable by Claude Code + Codex + Cursor + Antigravity. Completes the google-antigravity-skills portability pilot.
- **B2. Version-pin rules** (S, ★★★): Port the committed NativeWind Rule verbatim-pattern into hireui mobile's context file: "Check the exact version of <expo/nativewind/router> in package.json; do not use APIs from any other version." Directly attacks the drift class behind the Candidate-Detail token mess.
- **B3. Six-part anatomy audit** (S, ★☆☆): Score existing hireui/vault context files against role/overview/stack/folders/styling/patterns + ask-permission + pixel-perfect rules; fill gaps only where a real failure occurred ("solve it once, document it" — don't speculatively bloat).

## C. Skills supply chain (second-observation follow-ups)

- **C1. skills-lock.json as I-8 governance artifact** (M, ★★★): hireui's operator-only skill registry gets tamper-evidence for free: hash-lock approved skills (`computedHash` sha256) exactly like the lockfile. Approval = a lockfile entry; drift = hash mismatch. Small script, big governance win.
- **C2. Vendor-skill audit for YOUR stack** (M, ★★☆): Check hireui's actual vendors (Supabase already flagged #1-fit in the plugins topic; Expo if mobile uses it) for official skills repos; install into a sandbox via `npx skills add`, run npm-security-check + install-snapshot first (skills now ship executable `.sh` — treat as code, not docs).
- **C3. Well-known discovery sweep** (S, ★★☆): For each tool in your stack, probe `https://<docs-domain>/.well-known/skills/index.json` (Mintlify-hosted docs auto-serve these). 15-minute script; instant inventory of which of your vendors publish skills.
- **C4. Evals inside your skills** (M, ★★☆): Copy Clerk's pattern — add `evals/evals.json` to your own skills (loop-skills, yt-pipeline, etc.) and run them through the existing `evals/` harness + skill-creator eval tooling. Vendor skills becoming *tested artifacts* is the direction; get there first for your own.
- **C5. Serve a well-known skill from your own docs** (L, ★☆☆): If hireui ever publishes API docs on Mintlify, exposing a skill endpoint is ~free. Park until there's an external consumer.

## D. Vision Agents (the deep-dived original)

- **D1. Sandbox architecture pilot** (M, ★★☆): `uvx vision-agents init` (or clone the lingua `vision-agent/` shape — pattern only, repo is UNLICENSED) + Stream Maker trial + your OpenAI key. Goal: internalize agent-joins-the-call + call-custom-data context passing in ~2h. Wiki article is the runbook.
- **D2. hireui voice-agent SPEC (the Goal-#2 LLM-feature candidate)** (M, ★★★): Candidate **mock-interview practice agent** or **structured phone-screen agent** = the multi-agent-orchestration job-screener thread made real, with Vision Agents as the realtime layer and the claude-api-cost-optimization spec as the cost rail. Spec-first via grill→PRD (pocock thread) — do NOT build first. This turns four dormant wiki threads into one deployable plan.
- **D3. Steal the two-mode prompt pattern** (S, ★★★ for any agent work): TEACHING/REACTING split + "your turn is OVER at that question mark" + "never react to speech you didn't receive" is a general anti-monologue/anti-imagined-user pattern — apply to ANY conversational agent you build, text included. File alongside the VAD numbers (0.4/200ms/400ms/interrupt) for the day voice ships.

## E. Verification & review

- **E1. Impersonation-vuln sweep of hireui API routes** (S/M, ★★★): CodeRabbit's catch generalizes: *does any endpoint mint tokens/sessions/URLs from unauthenticated client-supplied IDs?* Grep hireui's API routes for query/body-sourced user IDs flowing into signing/lookup calls; fix = verify the session JWT (JWKS pattern now in the wiki). Also add as a standing line in the review checklist.
- **E2. Review-layer bake-off on loop PRs** (M, ★★☆): Run `/code-review` (and optionally a CodeRabbit trial) over the next v189-babysitter-flagged PR; score catch quality. Evidence for the "review-as-safety-net for AI code" claim on your own codebase.
- **E3. "Explain each generated file" checkpoint** (S, ★☆☆): Adopt as a post-feature verb in loop sessions — cheap comprehension audit; pairs with Rule 10 checkpointing.

## F. Vault / memory practice

- **F1. API-version pins as a memory type** (S, ★★☆): Adrian's committed `project_clerk_api.md` is exactly your memory system used as a **post-cutoff API ledger**. Formalize: when a session discovers a version-drift gotcha, save a `project_*_api.md` memory with the new surface. (This run's NativeWind/Clerk findings are the template.)
- **F2. Committed-memory governance decision** (S, ★☆☆): Decide explicitly: hireui repos do NOT commit `.claude/` memory (leaks local paths; Adrian's shows his desktop username). Vault: n/a. Write the one-liner into hireui's CONSTITUTION notes so an agent never "helpfully" commits it.

## G. Scrum-coaching material

- **G1. "Constraints are behavior" workshop** (M, ★★☆): Exercise: given a working feature, write 3 protective constraints from the user's perspective before any AI prompt. The product-engineer framing ("what could go wrong from a user's perspective?") is teachable in 30 minutes.
- **G2. Four-part prompt as a team working agreement** (S, ★★☆): Lightweight standard for AI-assisted teams: pointer/task/constraints/reference. Cheaper to adopt than a spec system; good gateway discipline before cc-sdd-grade ceremony.
- **G3. "The app isn't the point, the workflow is"** (S, ★☆☆): Use the video (or the wiki summary) as onboarding material for RN/mobile teams new to agentic dev — with the caveats page attached so they don't absorb the corrected claims.

## SKIP-LIST (explicit non-actions)

- **Don't** adopt Clerk/Stream/PostHog/CodeRabbit into hireui because this video says so — sponsor-integrated curriculum; hireui has its own stack and constraints.
- **Don't** reuse react-native-lingua code — **no license**. Patterns only.
- **Don't** quote "Vercel: AGENTS.md beats skills 100% vs 79%" until the jsm-six-file-context citation is re-checked (this run couldn't reproduce the 79% on Vercel's published evals).
- **Don't** assume installed skills are auto-consulted — keep explicit pointers (both JSM topics confirm).
- **Don't** use "a weekend" as an estimating baseline — untimed, sponsor-scaffolded.
- **Don't** plan Claude-based realtime voice on Vision Agents yet — no anthropic realtime plugin (OpenAI Realtime / Gemini Live are the shipped paths).

## Critic reframe (what this topic does NOT give you)

The methodology has **no automated verification** — its regression story is prompts + review + manual QA. Your existing threads (how-we-claude-code verify engine, pocock per-commit tests, cc-sdd discipline) are *stronger* on exactly this axis; practical-vibe-coding's unique contributions are the **protective-constraint prompt part**, the **version-drift toolkit**, and the **supply-chain evidence** — adopt those, keep your verification layer.

## Suggested next action

Do A1+A2 today inside the already-running Candidate-Detail work (zero install, immediate), schedule E1's sweep as the next loop-verifier task, and green-light D2's spec at the next planning session — that trio converts this topic into Goal-#2 evidence without displacing the cc-sdd/six-file bake-offs already queued.
