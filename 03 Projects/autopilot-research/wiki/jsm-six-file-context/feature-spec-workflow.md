# The feature-spec workflow — 29 specs, one chat each

> Ground truth: `context/feature-specs/01…29` (29 files verified in repo tree; specs 01/22/27 read in full) + transcript.

## The canonical loop (repeated ~28×)

1. Write `context/feature-specs/NN-<slug>.md` (with a planning AI as sparring partner).
2. **Open a NEW chat** in the coding agent.
3. Meta-prompt (canonical form): *"Read this file. Update the progress tracker. Implement exactly as specified."*
4. Agent plans → implements → (per instruction) updates `progress-tracker.md`.
5. Verify: `npm run build` (TS/ESLint), manual browser test, CodeRabbit review ([[verification-and-review]]).
6. Fix findings (isolated, one issue per corrective prompt when possible) → merge/continue.

## Spec template shape (verified — it is NOT EARS)

Prose-based, imperative, three recurring blocks:

- Opening sentence(s): what this unit produces and why.
- **Implementation** — numbered steps with file paths (later specs; spec 01 is just a bullet list).
- **Scope Limits** — explicit do-NOT list (e.g. spec 22: "don't add AI logic yet").
- **Notes** — patterns to reuse/respect (optional).
- **Check When Done** — 3–4 concrete pass/fail checks (e.g. "POST /api/ai/design triggers a background task. Task runs are stored in Prisma.").

No acceptance-criteria fields, no Cucumber/EARS syntax. Outcome-driven checks rather than prescriptive assertions. Early specs are skeletal (~80 words); later specs grew Implementation/Scope-Limits/Notes — a **maturation artifact**, no unified template documented.

## Split discipline in practice

- **Features 06/07 split** (API routes vs UI wiring), verbatim rationale: *"the API routes touch the back-end layer and the UI wiring touches the front-end and server components. Combining them gives the agent too much surface area to make assumptions across. Instead, we had two focused prompts... two clean results."*
- Specs are **behavior granules, not file counts**: Feature 18 (starter templates) orchestrates 6 files in one spec; Features 13–17 are five sequential specs polishing mostly ONE file (`canvas-node.tsx` + friends) — shape rendering / resize+label / color toolbar / edge behavior / ergonomics.
- Mock-first sequencing: Feature 04 builds dialogs on mock data ("no API calls yet"); Feature 07 swaps in real data — the ordering lives in the spec text + tracker.

## New-chat-per-spec (token discipline, verified)

> *"We're opening up a new chat for every single one of these specs. This helps us with lowering the overall context window and the amount of tokens that we're spending for each transaction, and it also makes the agent that much more focused on the task at hand."*

Counter-example shown on camera: batching **7 fixes in one chat** → one silently unfixed; *"whenever you give it more stuff to fix, it's easy for some of these to fall through... as soon as you go deeper into the conversation, the agent can easily get lost."* Recovery: isolate to a single issue per corrective prompt ("Analyze it and fix it").

## The `current-issues.md` pattern (ephemeral 7th file)

When a bug resists quick fixing (Clerk logout "unexpected response from server"), Adrian creates `context/current-issues.md` with the error details and asks the agent to **analyze first, fix after approval** — avoiding the "fix this" spiral where the agent breaks 10 things while patching one. The diagnosis surfaced proxy latency → missing `afterSignOutUrl` config. The file is later removed and gitignored (commit "Remove current-issues.md") — deliberately ephemeral.

## Corrective-prompt patterns (on-camera)

- Screenshot-driven: paste before/after screenshots + numbered issue list + "fix all of the listed issues" (Feature 12 layout; Feature 18 template sizing).
- Analysis-first: "issue one still hasn't been fully fixed... Analyze the issue further and fix it" → agent finds React strict-mode double-invoke bug.
- Isolation beats batching (see above).

## On-camera failures + recoveries (all integration-layer, <2 min each)

| Failure | Root cause | Recovery |
|---|---|---|
| Canvas drag-and-drop dead | Shape panel rendered inside React Flow viewport (pointer-events:none + D3 preventDefault) + 3 Liveblocks schema mismatches | Layout fix + **liveblocks-best-practices skill invoked reactively** — see [[skills-supply-chain]] |
| Liveblocks "authentication failed" | Missing API keys in `.env.local` | One-line fix |
| Autosave 2nd save fails | Vercel Blob "blob already exists" | `allowOverwrite: true` on `put()` |
| Delete key leaves nodes | React Flow `remove` change ignored; Liveblocks needs explicit delete mutation | Point agent at Liveblocks SDK signature |
| Gemini 2.0 Flash deprecated mid-video | Model lifecycle | Swap to `gemini-2.5-flash` |

Note the video presents a mostly linear success path; off-camera iteration count is unknown (see [[caveats-and-corrections]]).

## Cross-agent portability demo

Feature 08 is implemented with **Codex** (OpenAI's coding agent) instead of Claude Code, same spec + same context files — the six-file system is deliberately agent-agnostic. (A lens misread "Codex" as Cursor — corrected; see [[caveats-and-corrections]] #12.)

## Key Takeaways

- The meta-prompt never changes; **all variance lives in the spec file**. That's what makes execution predictable and reviewable.
- Scope-per-chat, not scope-per-day: the chat boundary is the WIP limit.
- "Check When Done" is a lightweight, outcome-level DoD — cheap to write, agent-verifiable.
- The analyze-first `current-issues.md` move is the sharpest debugging discipline in the video — steal it independently of everything else.
- The spec sequence encodes mock→real staging; the tracker carries the state between specs.
