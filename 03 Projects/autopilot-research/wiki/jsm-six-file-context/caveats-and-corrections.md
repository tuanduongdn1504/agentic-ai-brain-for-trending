# Caveats & corrections — the don't-re-fabricate ledger

> Every item below was caught by the adversarial verify pass (workflow `wf_2c3bd01a-8f0`) or by operator ground-checks overriding lens claims. When citing this topic, use THESE versions.

## Refuted / corrected claims

1. **"Skills are auto-consulted by the agent" → REFUTED.** Adrian's own phrasing is hedged (*"it might even consult the Prisma skill"*); nothing in the repo auto-loads skills; the decisive Liveblocks use was an **explicit, reactive** invocation mid-debug. Say: "installed proactively, invoked explicitly."
2. **"Verification includes tests" → REFUTED.** No test framework, no test files, no test script. Verification = TS/ESLint build + manual browser testing + CodeRabbit. Do not credit the methodology with automated testing.
3. **"Agents read the six files automatically" → REFUTED.** AGENTS.md *instructs*; the developer *directs* per prompt; the in-product AI tasks (design-agent/generate-spec) never read the context files at all.
4. **Two spec systems — don't conflate.** Hand-written `context/feature-specs/01–29` (development guidance) ≠ the app's runtime **generate-spec** feature (Gemini-generated architecture spec from the canvas). A lens merged them; the verifier split them.
5. **"The per-feature workflow includes CodeRabbit PR review as a standard step" → REFUTED as stated.** Two distinct review patterns demoed (PR bot on Feature 02; VS Code extension on Features 04/09/17); `ai-workflow-rules.md` mandates **no** CodeRabbit/PR/merge step.
6. **Progress-tracker automation overstated + fabricated quote caught.** A lens cited line 4843 (*"it actually updates the progress tracker…"*) — the transcript says something else there; grep finds no such sentence. TRUE: the tracker is genuinely maintained (28 features, live on-camera inspection at Feature 16); the update is part of the meta-prompt instruction, not autonomous behavior.
7. **License: the repo has NO license** (API field null, no LICENSE file). A lens said "Apache-2.0-implied" — wrong. Default = all rights reserved: steal the *patterns*, don't vendor the code. (Skill files inside `.agents/skills/` carry their own MIT frontmatter from vendors.)
8. **`.agents/skills/` IS committed to git.** A lens claimed it was gitignored/local-only; the recursive tree shows the 19 skill dirs as blobs, and `.claude/skills/*` as mode-120000 symlinks. Operator ground truth overrides.
9. **Spec 29 exists** (`29-spec-ui-integration.md` in the repo). A lens declared it missing — it had only sampled 3 downloaded specs. Progress-tracker's "Feature 29 (TBD)" refers to the *next* feature beyond the 28 logged.
10. **Naming: README says "Ghost Arc"**, repo/video say "Ghost AI." Unresolved inconsistency; use "ghost-ai" for the repo.
11. **Sponsor gravity.** Clerk, Trigger.dev, Liveblocks, CodeRabbit all sponsor AND appear as "the" solution. Trigger.dev-"essential" verdict: UNVERIFIABLE as necessity — Vercel `maxDuration` (300s+), Fluid Compute, SSE, Inngest are documented alternatives; durable-runs + realtime-status ergonomics are the honest case.
12. **"Codex = Cursor variant" (lens confusion) → wrong.** Codex is OpenAI's coding agent; the video uses it deliberately on Feature 08 to demo agent-agnostic portability of the context files.
13. **AGENTS.md injected block: markers official, wording variant.** `<!-- BEGIN:nextjs-agent-rules -->` is the official Next.js 16.2 managed-region mechanism (create-next-app default since 16.2, 2026-03-18 blog); the current official heading is "Next.js: ALWAYS read docs before coding" — ghost-ai's "This is NOT the Next.js you know" is a variant. Cite mechanism and wording separately.
14. **Corpus-lens confabulated glosses stripped:** "GSD = GitHub's Git Sync Dashboard" (invented) and "spec-kit (Shopify)" (wrong — spec-kit is **GitHub's**). The corpus SDD lineage stands as v5 GSD / v17 spec-kit / v54 gsd-2 / v58 OpenSpec / v61 cc-sdd.
15. **Gemini model drift:** video begins on `gemini-2.0-flash`, hits deprecation on camera, ships `gemini-2.5-flash`. Cite 2.5.
16. **MCP:** committed `.mcp.json` has ONLY the Trigger.dev MCP; other MCP prompts appear during setup flows but aren't committed.
17. **superpowers usage is referenced, not proven.** Two pre-flight plan files name `superpowers:subagent-driven-development` / `superpowers:executing-plans`; no execution artifacts; pattern abandoned after Feature 02 for feature-specs.

## Caption garbles (auto-subs)

"Cloud Code" → Claude Code · "Whisper/Wizard Flow" → Wispr Flow · "Shazian tabs" → shadcn Tabs · "Win serve" → (unclear; likely Windsurf) · "Get ignore" → .gitignore · "Diagram pattern" → Dialog pattern.

## Reported-but-unverified (keep flagged)

- Course launch date/pricing ($294/quarter JSM Pro figure is lens-reported).
- Reception statistics quoted in [[originality-and-reception]] (METR %, trust %, security %) — directional, from secondary sources, not re-verified here.
- "Claude Code VS Code extension 12M downloads" (transcript claim).
- Off-camera iteration/failure rate (video shows a mostly linear success path).
- Whether Adrian's team used the six-file system before this project ("for years" is self-reported).
- Big-tech "weeks of design docs" framing — cultural truism, presented without sources (transcript-grounded as a claim made, not verified as fact).

## Verified load-bearing quotes (safe to cite verbatim)

- *"Work on one feature unit or subsystem at a time… that single rule prevents most failures that the agents cause."* (transcript ~857–863; mirrored in ai-workflow-rules.md)
- *"Combining them gives the agent too much surface area to make assumptions across."* (~2801–2809, the 06/07 split)
- *"As soon as you go deeper into the conversation, the agent can easily get lost."* (~4781–4790, batch-fix degradation)
- *"Whenever you're working with specific tools, always verify that they also have their agent skills, install them, and ask your agent to use them."* (~3715–3719)
- *"You are the architect and agent is just a coder."* (~3588)
- *"I didn't write a single line of it. An agent built the whole thing."* (~12 — rhetorical; human authored specs/context/prompts)
