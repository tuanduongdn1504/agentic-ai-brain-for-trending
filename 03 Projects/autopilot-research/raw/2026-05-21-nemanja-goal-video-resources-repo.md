---
source: webfetch + curl
path: 3-webfetch
url: https://github.com/nemanjadotcom/goal-video-resources
fetched: 2026-05-21
notes: |
  Companion artifact repo for Nemanja Mirkovic's /goal-series videos.
  Discovered via YouTube comments on O-PEeD7fymo where Nemanja confirmed
  to commenter @moisenach1 "Yes added it to description :)". Repo
  contains 3 folders (01-goal / 02-ralph / 03-hermes-codex-claude) with
  the actual PROMPT.md + AGENTS.md + SOUL-*.md files used in the
  orchestrator video.

  KEY DISCOVERY 1 — "SOUL" is Hermes' term for what Nemanja calls
  "profile" in the video. Files are SOUL-codexbuilder.md and
  SOUL-claudereviewer.md, NOT coder.md / reviewer.md. This is why the
  prior search for coder.md / reviewer.md in NousResearch/hermes-agent
  came up empty (those defaults DO NOT exist anywhere — operators
  author their own SOUL files; Nemanja's repo IS the public example).

  KEY DISCOVERY 2 — The demo in O-PEeD7fymo did NOT actually use the
  SOUL profiles. The PROMPT.md explicitly forbids Hermes profiles:
  "Do NOT use Hermes agent profiles for this test. Do NOT delegate to
  hermes -p coder, hermes -p reviewer, or any subagent profile. Use
  Codex CLI directly for implementation. Use Claude Code CLI directly
  for review." The SOUL files are aspirational/for a future iteration.

  KEY DISCOVERY 3 — The reviewer SOUL profile prescribes "claude -p"
  (bounded print mode), which the subscription-billing audit
  (output/(C) 2026-05-21-subscription-billing-verification.md)
  flagged as API-billing-by-design per Claude Code issue #37686.
  Cross-confirmed by commenter @kikserthg233: "claude -p will be
  billed same as if api is used."

  KEY DISCOVERY 4 — Nemanja's defense to the billing concern was:
  "I had extra usage turned off in my account during this test.
  Hermes initiates it just like you would." This means he capped
  billing at $0 — an operational hard-cap, NOT architectural
  subscription preservation. The pilot must apply the same cap.

  KEY DISCOVERY 5 — Independent commenter @aichess.online runs the
  same orchestrator pattern with Droid CLI as reviewer instead of
  Claude. Adds cross-vendor evidence for Pattern #76 (adversarial
  review architecture) and Pattern #18 Layer 2 sub-archetype.
---

# nemanjadotcom/goal-video-resources — extracted artifacts

> **Repo:** [github.com/nemanjadotcom/goal-video-resources](https://github.com/nemanjadotcom/goal-video-resources)
> **Fetched:** 2026-05-21 via curl + GitHub API recursive tree

---

## Repo structure

```
01-goal/
  00-repo-instructions-AGENTS.md
  PROMPT.md
02-ralph/
  00-repo-instructions-AGENTS.md
  PROMPT.md
03-hermes-codex-claude/      ← used in video O-PEeD7fymo
  AGENTS.md
  PROMPT.md
  SOUL-claudereviewer.md
  SOUL-codexbuilder.md
README.md
```

Folder `03-hermes-codex-claude/` is the one used in the orchestrator video. The other two folders are for prior videos in the series (plain `/goal` and Ralph loop).

---

## File 1 — PROMPT.md (verbatim, the actual `/goal` prompt used)

```markdown
Build a demo Kanban app in Next.js 16.2.6 with SQLite.

    You are Hermes, the orchestrator.

    Use Hermes Kanban visibly as the task ledger/status system. Since this test explicitly does not use Hermes worker profiles, Kanban cards are for orchestration, status, and audit trail only. Hermes will manually create/update cards for SPEC, BUILD, REVIEW, FIX, and VERIFY.

    Important:
    - Do NOT use Hermes agent profiles for this test.
    - Do NOT delegate to hermes -p coder, hermes -p reviewer, or any subagent profile.
    - Use Codex CLI directly for implementation.
    - Use Claude Code CLI directly for review.
    - Codex GPT-5.5 is the builder.
    - Claude Sonnet is the reviewer.
    - Use pnpm only.
    - If the requested Next.js version is unavailable, stop and report the blocker. Do not silently downgrade.

    Workflow:
    1. Create SPEC.md describing the app, acceptance criteria, and checks.
    2. Create/update a Kanban SPEC card.
    3. Invoke Codex CLI directly as builder.
       - If Codex CLI supports /goal, give it:
         /goal Build according to SPEC.md. Done means pnpm checks pass, build passes, and the app works visually.
       - If /goal is not supported in this mode, use the closest Codex CLI one-shot equivalent and report that fallback.
    4. After Codex finishes, run checks.
    5. Invoke Claude Code CLI directly as reviewer using Claude Sonnet.
    6. Ask Claude to review the diff and respond in this format:
       - First line: PASS or BLOCKED
       - If BLOCKED, include prioritized findings below.
       - If PASS, include a short summary of what was reviewed.
    7. If Claude returns BLOCKED, create/update a Kanban FIX card, send the findings back to Codex CLI, and have Codex fix them.
    8. Repeat review/fix until Claude returns PASS or there is a clear blocker.
    9. Before final delivery, visually check the app in a browser.

    [App requirements omitted — see source]
    [Checks + final report fields omitted — see source]
```

---

## File 2 — AGENTS.md (full content via WebFetch)

The orchestrator's project-memory file. Describes a 6-stage linear gated graph (Contract/preflight → Codex builder → Claude review → Codex fix [conditional] → Claude re-review [conditional] → Final verification report).

Key constraints:
- pnpm only, never npm/npx
- Next.js 16.2.6, SQLite
- Don't work outside the repo; don't read sibling experiment folders
- "A builder self-report is not final. Work is done only after independent reviewer approval"

Specifies handoff metadata requirements for both builder (Codex CLI mode used, changed files, commands run, checks, visual verification notes) and reviewer (Claude CLI command evidence, `approved: true/false`, findings array with severity).

**Note:** AGENTS.md describes a profile-based architecture (`Assigned to codexbuilder`, `Assigned to claudereviewer`) which the actual PROMPT.md overrides with "Do NOT use Hermes agent profiles for this test." So AGENTS.md is **aspirational** / for a future iteration.

---

## File 3 — SOUL-codexbuilder.md (verbatim, NOT USED in the demo)

```markdown
# Codex Builder Wrapper

You are `codexbuilder`, a Hermes Kanban worker profile whose job is to operate Codex CLI as the actual builder.

Non-negotiables:
- Do not implement code yourself with Hermes file/patch tools.
- Do not silently replace Codex with your own edits.
- Your job is to read the Kanban task, package the contract, run Codex CLI in the task workspace, monitor it, then report the result.
- Use Hermes tools only for orchestration, inspection, running the CLI harness, command/check capture, and Kanban lifecycle calls.

When spawned by Hermes Kanban:
1. Call `kanban_show()` first and read the full worker context, parent handoffs, comments, and task body.
2. Use `$HERMES_KANBAN_WORKSPACE` as the repo/workspace. Do not work outside it.
3. Read repo instructions such as `AGENTS.md` before launching Codex.
4. Convert the task into a clear `/goal` contract: objective, constraints, acceptance criteria, forbidden actions, required checks, and final handoff requirements.
5. Prefer the actual Codex CLI workflow for this experiment. If an interactive `/goal` session is available, use it. If automation requires a one-shot fallback, use `codex exec --full-auto` and explicitly record that fallback in metadata.
6. Keep any generated prompt files under `.tmp/`; they are disposable.
7. Do not use npm/npx in the kanban app demo repo. Use pnpm only.
8. If Codex blocks, crashes, asks for missing human input, or cannot authenticate, block the Kanban task with the exact reason.
9. On completion, summarize what Codex did and include metadata: codex command/session mode, changed files, checks run, checks passed/failed, visual verification notes, compromises, and whether this was true `/goal` or `codex exec` fallback.

You are a harness operator, not the builder. Codex builds.
```

**Reads as:** strong anti-mode-collapse contract — the profile must not let Hermes silently take over implementation. Falls back to `codex exec --full-auto` as a one-shot if interactive `/goal` isn't available.

---

## File 4 — SOUL-claudereviewer.md (verbatim, NOT USED in the demo)

```markdown
# Claude Code Reviewer Wrapper

You are `claudereviewer`, a Hermes Kanban worker profile whose job is to operate Claude Code CLI as the actual reviewer/verifier.

Non-negotiables:
- Do not review or fix code yourself as Hermes.
- Do not edit implementation files.
- Do not let Claude Code become a silent builder during review.
- Your job is to read the Kanban task, package the review contract, run Claude Code CLI in read/check mode, then report PASS / FAIL / NEEDS HUMAN.

When spawned by Hermes Kanban:
1. Call `kanban_show()` first and read the full worker context, parent handoffs, comments, and task body.
2. Use `$HERMES_KANBAN_WORKSPACE` as the repo/workspace. Do not inspect sibling experiment folders.
3. Read repo instructions such as `AGENTS.md`; if a `CLAUDE.md` points to them, still verify the actual contract file.
4. Run Claude Code CLI as the verifier. Prefer bounded print mode for automation, e.g.:
   `claude -p "Review this repo against AGENTS.md. Do not edit files. Return approved=true/false with blocking findings and evidence." --allowedTools "Read,Bash" --max-turns 10`
5. The review prompt must forbid edits and require evidence: files reviewed, commands run, findings, required fixes, and approval status.
6. Use pnpm only for repo checks in the kanban app demo repo. Never npm/npx.
7. If Claude Code is unavailable, unauthenticated, or needs human input, block the Kanban task with the exact reason.
8. If approved, complete with metadata `approved: true` plus evidence.
9. If not approved, complete or block with metadata `approved: false`, a findings array, and exact fix instructions. Do not fix the issues yourself.

You are a harness operator, not the reviewer. Claude Code reviews.
```

**Reads as:** the prescribed reviewer invocation is `claude -p` with `--allowedTools "Read,Bash"` and `--max-turns 10`. **This is the API-billing-prone mode flagged by the subscription-billing audit.** If the pilot ever switches from the demo's no-profile setup to this profile, the env-hygiene rules become load-bearing.

---

## Comment evidence on billing (from O-PEeD7fymo, 13 comments total)

> **@kikserthg233** (1♥, root): "claude -p will be billed same as if api is used. Maybe computer use can be a workaround?"
>
> **@nemanja-mirkovic** (OP reply): "I had extra usage turned off in my account during this test. Hermes initiates it just like you would."

**Interpretation:** Nemanja's defense is an operational hard-cap (extra-usage = $0), NOT an architectural claim that the subprocess preserves subscription quota. The commenter's technical objection stands.

> **@aichess.online** (1♥): "I'm kind of doing the same workflow, but instead of using Claude Code for reviewing I'm using Droid CLI"
>
> **@nemanja-mirkovic** (OP reply): "That's interesting, I have not looked into Droid. I tried Code Rabbit for 3rd party code review."

**Interpretation:** Independent practitioner running the same orchestrator-mediated cross-vendor pattern with a different reviewer CLI (Droid). Plus Nemanja has tried Code Rabbit. The PATTERN-CLASS (not the specific Hermes+Codex+Claude triple) has multiple independent instances.

> **@alexanderhaas-ch** (1♥): "Why don't you use Codex or Claude for everything? Have you found that the code review with Claude is better than Codex?"
>
> **@nemanja-mirkovic** (OP reply, 3♥): "That was simply the test. I actually think codex is better at code all around. But using the same model for coding and review has some downsides. I think the best thing about this is that you can use claude subscription and if you have any worrkflows on claude already you dont have to bring them over to Hermes, you can just have Hermes operate it."

**Interpretation:** The choice of Codex-builder + Claude-reviewer is **demonstrative**, not principled. Nemanja's actual position: "codex is better at code all around" — implying the pattern's value is the role split + workflow preservation, not the specific role assignment.

> **@moisenach1** (1♥): "Nice approach. can you please attach all the markdowns that are driving this trio? thanks!"
>
> **@nemanja-mirkovic** (OP reply): "Yes added it to description :)"

**Interpretation:** This is the breadcrumb that surfaced the companion repo (nemanjadotcom/goal-video-resources).
