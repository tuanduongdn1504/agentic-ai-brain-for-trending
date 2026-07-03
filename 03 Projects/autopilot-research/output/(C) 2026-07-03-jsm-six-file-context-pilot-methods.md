# (C) Pilot methods — jsm-six-file-context → your working flow

> **Source topic:** `wiki/jsm-six-file-context/` (JSM "How Senior Engineers Actually Build With AI in 2026" + ghost-ai repo double deep-dive, adversarially verified 2026-07-03).
> **Your standing context:** Goal #2 = *build software with these tools* → deployment target **hireui** (Candidate Detail refactor is the live ticket); pilots already ranked: **cc-sdd #1**, codex-plugin-cc #1.5; open threads: antigravity `AGENTS.md`/`SKILL.md` portability, open-design `DESIGN.md`, how-we-claude-code verify engine, v189 loop pilot, prompt-eval harness.
> **Honesty note carried from the wiki:** this methodology ships **no automated verification** — every method below that adopts it also keeps YOUR verify loop. And the repo is **unlicensed**: steal patterns, never vendor code.

**Legend:** Effort ⚡(<1h) / ⚡⚡(half-day) / ⚡⚡⚡(1–2 days) / 🏗️(week+) · Fit ★1–5 vs your goals.

---

## A. hireui / Goal #2 — the deployment-evidence lane

**A1. Six-file `context/` for hireui — scoped to the Candidate Detail refactor.** ★★★★★ ⚡⚡
Write hireui's `context/` six: project-overview (TalentAxis product frame), architecture-context (**with an Invariants section** — e.g. token SoT = Figma r2 handoff, I-2 branch policy as invariant), ui-context (the locked tokens: navy #002D79, accent #DC6803, Roboto, avatar 72px, timeline #ECFDF5/#FEF2F2 — this directly attacks the token-drift root cause), code-standards, ai-workflow-rules (their scoping rules verbatim-adapted), progress-tracker (seed from `.pilot-log`). Zero install; pure Markdown; composes with hireui's CONSTITUTION instead of replacing it.
*Measure:* agent sessions that violate a locked token before vs after; time-to-context at session start.

**A2. Numbered feature-specs for the Candidate Detail plan.** ★★★★★ ⚡⚡
Slice the locked plan (`.cm/outputs/plans/phase-2-candidate-screen-rework.md`) into `context/feature-specs/01…NN` with the verified template: prose steps + **Scope Limits** + **Check When Done**. Honor the 06/07 lesson: separate data-wiring specs from UI specs. Drive each with the canonical meta-prompt: *"Read this file. Update the progress tracker. Implement exactly as specified."*
*Measure:* corrective-prompt count per spec; specs completed in one pass.

**A3. One-new-chat-per-spec as hard WIP rule.** ★★★★★ ⚡
The single cheapest verified practice in the video: fresh session per spec, tracker carries state between. You already saw the failure mode it prevents (7-fix batch → 1 silently dropped). Apply on hireui immediately, no other adoption needed.
*Measure:* silent-miss rate on multi-issue prompts before/after.

**A4. `current-issues.md` analyze-first debugging.** ★★★★☆ ⚡
On any stubborn hireui bug: dump the error + context into an ephemeral `current-issues.md`, prompt "analyze first, propose fix, wait" — then approve. Gitignore it. Anti-spiral discipline, verified on camera (Clerk logout root-caused via latency analysis).
*Measure:* fix-attempt count on gnarly bugs.

**A5. Vendor skills for hireui's actual stack.** ★★★★☆ ⚡⚡
Ghost-ai's lesson made portable: *"whenever you're working with specific tools, verify they have agent skills, install them, and ask your agent to use them."* Audit hireui's stack for **official vendor skill repos** (e.g. `supabase/`, expo/react-native, prisma if used) via `npx skills search` / GitHub. Install per I-8 (operator-only registry!) into `.agents/skills/` + symlinks; commit `skills-lock.json`. **Invoke explicitly** (auto-consult is refuted).
*Measure:* stack-specific bug rescue events (the Liveblocks-style save).

**A6. Invariants section as CONSTITUTION bridge.** ★★★★☆ ⚡
Extract hireui's non-negotiables (I-2 agent-* branches, I-8 skills registry, GitNexus-first, parity rules) into a 5-line **Invariants** block inside architecture-context — the ghost-ai form factor for what hireui already legislates in prose. Agents respect short invariant lists better than long constitutions.
*Measure:* constitution-violation incidents in agent sessions.

**A7. The bake-off: six-file vs cc-sdd on twin tickets.** ★★★★★ ⚡⚡⚡ — **the headline**
You've been circling a cc-sdd pilot since v61. Run the comparison this topic makes possible: two comparable hireui slices (or the same slice twice in worktrees) — one under **cc-sdd** (installed harness, adversarial review), one under **six-file + feature-specs** (zero-install discipline). Same model, same verify loop (typecheck + tests + your how-we-claude-code verify engine).
*Measure:* setup time / tokens per feature / corrective prompts / review catches / subjective overhead. **This produces the Goal-#2 artifact AND finally settles the "install a harness vs write six files" question with your own data.*

## B. Skills supply chain — the harness lane

**B1. Adopt `npx skills` + `skills-lock.json` for your own harness.** ★★★★☆ ⚡
Your skills currently live loose in `.claude/skills`/`05 Skills/`. Trial vercel-labs/skills (24.8K★): `.agents/skills/` canonical + per-agent symlinks + lockfile with content hashes. Instant Antigravity/Codex portability — the pattern you predicted in the antigravity thread, now with tooling. Gate with your npm-security-check + install-snapshot skills first.
*Measure:* one skill install round-trip; does the symlink layout survive your vault's git setup.

**B2. Publish ONE vault skill in vendor format.** ★★★☆☆ ⚡⚡
Package a mature vault skill (e.g. the yt-pipeline or the A1 anchor-validation gate) as a proper SKILL.md repo with frontmatter + `evals/evals.json` (Clerk ships evals with skills — copy that bar). Install it back via `npx skills add <you>/<repo>` into a sandbox. You learn the full supply chain by walking it once.
*Measure:* installable + invocable in a fresh project.

**B3. Skills-vs-AGENTS.md experiment (Vercel's 100%-vs-79% claim, self-tested).** ★★★★☆ ⚡⚡
Vercel's eval says bundled always-on context beats on-demand skills for framework knowledge. Test on YOUR stack: same task, run A with a skill installed but un-prompted; run B with the same content inlined in AGENTS.md/CLAUDE.md. Use the `evals/` harness from the prompt-eval pilot.
*Measure:* did the agent consult the skill unprompted (predict: no); pass rate A vs B; token cost delta.

**B4. Supply-chain hygiene note → runbook.** ★★★☆☆ ⚡
Lockfile hashes ≠ signatures. Write the 10-line rule into your harness docs: only `npx skills add` from org-owned repos; pin via lockfile; diff SKILL.md on update (hash change = review). Composes with install-snapshot.

## C. AGENTS.md / portability — composing with your open threads

**C1. Managed-region AGENTS.md for the vault + hireui.** ★★★★☆ ⚡
Next.js 16.2 formalized **managed blocks** (`<!-- BEGIN:x --> … <!-- END:x -->`) inside AGENTS.md. Adopt the convention: your six-file reading order in one block, tool-injected vendor blocks kept separate, hand-written rules outside markers. Update-safe agent files — a real upgrade over monolithic CLAUDE.md editing.
*Measure:* one tool-doc update that doesn't clobber your rules.

**C2. `CLAUDE.md` = `@AGENTS.md` shim experiment.** ★★★☆☆ ⚡
Ghost-ai runs the inverted layout (AGENTS.md = brain, CLAUDE.md = include + vendored docs) — and it's the official Next.js recommendation. Trial on ONE sandbox project (not the vault — Thariq's advice to keep vault-MD stands): harness content once, per-agent shims.
*Measure:* Claude Code + one other agent (Codex/Antigravity) both pick up the same rules.

**C3. Cross-agent spec replay (their Feature-08 demo, your ticket).** ★★★☆☆ ⚡⚡
Take one completed hireui feature-spec from A2 and replay it with Codex (or Antigravity) instead of Claude Code — same context files. This is the portability proof-point on your own repo, and feeds the codex-plugin-cc #1.5 comparison thread.
*Measure:* diff quality parity; anything Claude-specific that leaked into your specs.

**C4. Bundled-docs check for your stack.** ★★☆☆☆ ⚡
Next.js now ships full Markdown docs in the npm package (`node_modules/next/dist/docs/`). Check which of hireui's dependencies do the same (or have `llms.txt`) and point AGENTS.md at them — free version-matched context, zero fetch.

## D. Vault / autopilot-research applications

**D1. Progress-tracker upgrade for vault projects.** ★★★☆☆ ⚡
Ghost-ai's tracker format (per-feature full implementation log + Architecture Decisions + version-pinned Session Notes) is a stronger STATE.md than most of yours. Adopt the three-section form for the v189 loop pilot's STATE file — especially **version pinning** (your flaky-shell workarounds belong in Session Notes form).

**D2. In-product AI pattern file → hireui's future LLM feature.** ★★★★☆ ⚡⚡
hireui has no LLM yet; its first feature is spec'd (cost-optimization runbook). Ghost-ai contributes the implementation shape: **background task + narrow tool set + cheap model** (8 Zod tools, Gemini Flash, atomic mutations, broadcast status). Write a 1-page addendum to `claude-api-cost-optimization-spec` mapping this pattern onto the recruitment-agent feature (from the multi-agent-orchestration thread) — Claude Haiku/Sonnet in the same role Gemini Flash plays here.

**D3. Six-file guide WITHOUT the email gate → wiki article as your template.** ★★☆☆☆ ⚡ (done-by-default)
The wiki page [[../wiki/jsm-six-file-context/six-file-context-system]] IS the reconstructed guide. When you want the six files for any new project, instantiate from the wiki, not the funnel.

**D4. Pattern-Library feed at next mini-audit.** ★★★☆☆ ⚡
Queue for v66+: (a) Pattern #21 SDD — candidate N+1 as first *pedagogy-first* instance (new author: Adrian Hajdin/JSM, grep-verified new); (b) Pattern #18 Layer 2 — vendor-skills-via-lockfile as candidate 4th sub-archetype (declarative dependency mgmt vs runtime-proxy/install-translator/plugin-bridge); (c) the AGENTS.md-vs-skills Vercel eval as evidence on the skills-format threads. Registration at audit-time per discipline, not now.

## E. Scrum-coaching angles

**E1. "Check When Done" = lightweight DoD per story.** ★★★★☆ ⚡
The spec template's terminal gate (3–4 concrete pass/fail bullets, outcome-level) is a teachable Definition-of-Done format for teams adopting AI agents — cheaper than Gherkin, agent-verifiable. Use in your next coaching engagement as the bridge between acceptance criteria and agent prompts.

**E2. New-chat-per-spec as WIP limit — the Kanban translation.** ★★★★☆ ⚡
"One chat = one work item; the tracker is the board" translates agent hygiene into vocabulary teams already have. The batch-degradation quote (*"give it more stuff… some fall through"*) is your evidence slide — it's Little's Law for context windows.

**E3. Architecture-first sprint-zero workshop.** ★★★☆☆ ⚡⚡
The video's crash-course segment (design docs → six files → specs) is a ready-made 1h workshop arc for teams: have the team write project-overview + invariants + 3 feature-specs for their real backlog, then run one spec through an agent live. The 4h video is your prep; the team never watches it.

**E4. The counter-evidence slide.** ★★★☆☆ ⚡
Pair E3 with the reception data (METR slowdown, trust decline, Zen van Riel's anti-SDD position from your own corpus) — coach teams to **measure** their agent adoption, not vibe it. Your bake-off (A7) becomes the demonstration.

---

## Skip-list (deliberately NOT piloting)

- **Building a Ghost-AI-style canvas product** — fun, off-goal; hireui is the target.
- **Vendoring any ghost-ai code** — unlicensed repo; patterns only.
- **CodeRabbit subscription** — you already have `/code-review` + how-we-claude-code verify + loop-verifier agent covering the adversarial-review role; adding a SaaS reviewer is redundant until a team context demands it.
- **Buying the course / joining waitlists** — the repo + wiki supersede the gate; course unreleased/unpriced.
- **Trigger.dev adoption for the vault** — its niche (durable 30–60s+ jobs with realtime status) doesn't exist in your current pipelines; revisit iff hireui's LLM feature needs background jobs (D2 notes the pattern without the vendor).
- **Deleting package-lock.json to fix builds** — the video did it; do not import that habit.

## Critic's reframe (read before picking)

The six-file system is **the beginner-legible 20% of what you already run.** Your vault has CLAUDE.md discipline, pattern library, loop logs, STATE files; hireui has a CONSTITUTION + BMAD + pilot-log. You are not adopting a new methodology — you are **borrowing three specific artifacts** it does better than your current stack: (1) the Invariants form factor, (2) the Scope-Limits + Check-When-Done spec template, (3) the lockfile-managed skills layout. Plus one habit: new-chat-per-spec. If a pilot grows beyond those four, it's probably momentum, not signal. And its one real hole — no automated verification — is exactly where your existing pilots (cc-sdd, verify engine, loop-verifier) are strongest. **Compose, don't convert.**

## Recommended sequence (2-week arc)

1. **Day 1:** A3 (new-chat rule) + A4 (current-issues.md) — free wins, effective immediately.
2. **Day 1–2:** A1+A6 (six files + invariants on hireui, Candidate-Detail-scoped).
3. **Day 3–4:** A2 (feature-specs from the locked plan) → start shipping slices.
4. **Week 2:** A7 (the cc-sdd bake-off) — the Goal-#2 artifact. B1/C1 in idle moments (⚡ each).
5. **Audit-time:** D4 (pattern registrations at v66+ cadence).
