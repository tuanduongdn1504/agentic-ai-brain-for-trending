# QA plan + feedback button — parallelizing human QA with agent fixing

## Source

- Transcript `raw/2026-07-03-pocock-real-feature-build.md` · feedback backend verified: `api.feedback.ts` in [mattpocock/course-video-manager](https://github.com/mattpocock/course-video-manager).

## The QA plan step

- After the AFK run, in a **fresh session**, freehand prompt (his words): *"Take the last five commits and create a QA plan for me. Save that QA plan in a GitHub issue. The QA plan should give me a step-by-step guide on how to test every single part of the new implementation."*
- Status: **not yet a skill** — "I haven't come up with a skill for this yet… I think it makes sense in almost every user-facing change." (No QA-plan skill existed in mattpocock/skills at verification time.)
- **Routing discipline:** the QA-plan issue is for humans — he comments "Ralph loops should not work on this one" / renames with an AFK marker so the loop skips it; and he **closes the QA plan** once behavior drifts, "so the agent doesn't look at this as the source of truth for what it's supposed to be building."
- QA-plans-as-issues gives re-runnable, versionable test scripts — reopen if you want to re-QA.

## The feedback button (the load-bearing invention)

- An **in-app feedback button**: Matt dictates what's wrong *in context*; it files a GitHub issue with:
  - an **AI-generated title** — verified: the backend uses **Claude Haiku** for title generation (cost-tier routing; falls back to first-sentence truncation),
  - the **route** it was submitted from,
  - the dictated feedback body.
- QA session arithmetic: **six issues in 8 minutes** while Ralph fixes earlier ones in the background — "I'll just kick it off again and keep QAing… I won't interrupt."
- Feedback classes observed: bugs (minified React error, no loading state, modal not closing), UX reversals (kill the two-tab ghost/real modal → "just create a ghost course silently"), design corrections discovered only by seeing it ("this create-ghost + create-real menu doesn't seem right… just a checkbox that says *also create this on the file system*"), and missed requirements (confirmation modal on destructive delete), plus one **showstopper**: not-a-git-repo → directory/DB desync → "walk back the creation."

## The stance this demo argues for

- "We could have had an extra design phase or a prototype phase, but I don't mind jumping to code and fixing it there" — QA-with-cheap-fixes replaces upfront design for UI ambiguity.
- The showstopper found by hand, not by spec, is his evidence: *"It's this kind of stuff that makes me think the specs-to-code approach is just never going to work… in the QA loop you find weird edge cases that are really hard to plan for."* — **his position, not a corpus consensus**: the SDD thread in this vault (cc-sdd, OpenSpec, spec-kit — Storm Bear Pattern #21) bets the other way; note he still front-loads 22 minutes of requirements grilling, so the real disagreement is about *how much* upfront, not whether.
- Closing self-description: "What I'm doing is reviewing the outputs that come from AI, passing more information to it, and getting into a tight loop with it… because I can run Claude AFK, I'm able to parallelize my own QA with the fixing of the bugs."

## The loop, named

```
grill → PRD → issues → [Ralph implements] → QA plan → human QA
        ↑                                            │
        └────────── feedback button issues ←─────────┘
                    (Ralph fixes in background, in parallel)
```

- One backlog, two producers (planning + QA), one consumer (Ralph). The feedback button is what makes QA *additive* instead of blocking.

## Key Takeaways

- **Make QA feedback zero-friction and structured** (button → dictation → AI-titled issue with route context) and it becomes agent-consumable fuel, not a chore doc.
- **Generate the QA plan from the diff** ("last N commits"), store it as an issue, label it human-only, close it when stale.
- Cheap fixes change design economics: ship one UI guess, let seeing-it-in-reality drive the correction ("I couldn't get a sense for which way to go until I saw it in reality").
- Route feedback-title generation to a **cheap model** (Haiku) — right-sized model per task, even inside a hobby-scale harness.
- Cross-links: [[sandcastle-ralph-afk-loop]] · [[../how-we-claude-code/_index]] (agent-native verification — the natural next step: automate the QA plan's execution) · [[../prompt-evaluation/_index]] (QA plan ≈ eval checklist) · [[../ai-engineering/_index]] (user-feedback flywheel).
