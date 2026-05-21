---
source: yt-dlp-only
path: 5-yt-dlp
url: https://www.youtube.com/watch?v=CKtz9lp8X-8
video_id: CKtz9lp8X-8
title: "I Was Wrong About Hermes Agent /goal"
channel: Nemanja Mirkovic
channel_id: "@nemanja-mirkovic"
duration: 19:09
uploaded: unknown
language: en
fetched: 2026-05-21
notes: |
  Pre-requisite video for understanding the orchestrator pattern in
  O-PEeD7fymo (the Hermes+Codex+Claude video). Targeted ingest to verify
  /goal mechanics before any pilot. Subject scope: what /goal actually
  does, how it compares to plain Ralph loop, where the judge fits.

  Combined with negative finding from hermes-agent repo audit
  (NousResearch/hermes-agent main branch): no shipped coder.md /
  reviewer.md profile defaults — those are entirely user-authored. Repo
  ships Python profile system (hermes_cli/profiles.py, profile_describer.py,
  profile_distribution.py, skills_config.py, skills_hub.py, skill_bundles.py)
  + the bundled Claude Code SKILL.md previously fetched, NOT markdown
  profile defaults.
---

# I Was Wrong About Hermes Agent /goal — transcript

> **Source:** [YouTube](https://www.youtube.com/watch?v=CKtz9lp8X-8) — Nemanja Mirkovic, 19:09
> **Fetched:** 2026-05-21 via `yt-dlp --write-auto-subs`
> **Compile target:** `wiki/harness-engineering/hermes-goal-mechanics.md` (new article)

---

## Topline thesis

> "Hermes agents recently released an update that allows you to orchestrate long-running agents and long-running tasks using a single `/goal` command... is it really better than the Ralph loop workflow I showed in one of my previous videos and how it compares to this `/goal` command."

The video answers: **No, not for serious work.** Ralph wins on quality and control. `/goal` wins on time-to-first-output but produces lower-quality artifacts and offers less observability.

---

## /goal architecture (5 stages, narrated)

```
1. Accept goal
   ↓
2. Create plan — decompose initial prompt into PRD-style document
   ↓
3. Execute step
   ↓
4. Judge says done? (yes/no — NOT a code reviewer, NOT a verifier)
   ↓ no                              ↓ yes
   loop back to step 3               exit clean / report
```

> "What you have to understand is that the judge is not a code reviewer, it's not a verifier, it's just a simple yes or no check to see if the loop continues or exits, if there are any blockers or not."

> "With Ralph loop, you can actually have a proper code review stage or even third-party code review, so you can get as close to production code as possible."

**Critical implication for the orchestrator pattern (video O-PEeD7fymo):** the Hermes+Codex+Claude orchestrator is `/goal` PLUS a real code reviewer (Claude CLI subprocess), specifically because `/goal` alone has no review stage — just the yes/no judge.

---

## /goal is becoming a cross-vendor primitive

> "Codex actually has goal as well, and now Claude has this as well."

Confirmed in this video (without source citations) that all 3 major harnesses now expose a `/goal`-equivalent primitive. This is corpus-relevant — it means Ralph-loop-as-slash-command is no longer Hermes-exclusive. Worth a separate cross-vendor audit.

---

## Shubham origin confirmed

> "the interesting part here is that Codex actually has goal as well, and now Claude has this as well. So you can do pretty interesting things here with the slash goal command, which you can see here, Shubham, and I'm hopefully not butchering his name, made this post where he uses Hermes as the orchestrator and then Claude and as the reviewer and Codex as a builder."

Same Shubham referenced in the orchestrator video. Origin attribution validated. (X.com auth-walled = Path 9 ingest if/when worth the effort.)

---

## Decision matrix host gives (when to use what)

| Tool | Best for |
|---|---|
| `/goal` | Specific tasks with clear end state — e.g., framework migration (NPM→PNPM, Next→Svelte, Supabase→local-JSON). "Just type `/goal` and do something." |
| Ralph loop | Serious projects, architecture-first coding, actual features, production. "More precise, I can check the PRD, I can edit the PRD, I can see how it's broken into issues, I can stop it, I can resume it." |
| Kanban | Non-code tasks. Content production (research/script/social-media). Most token-efficient per the host's breakdown. |

> "I probably won't be replacing Ralph with /goal right now. I might be implementing /goal in some way."

---

## Live A/B test observations

Both side-by-side: same Next.js + SQLite Kanban prompt, `/goal` vs Ralph.

| Aspect | `/goal` | Ralph |
|---|---|---|
| Model | GPT-5.5 (single setting) | GPT-5.5 low for slices, GPT-5.5 high for review |
| Time to finish | minutes | ~1 hour |
| PRD visibility | created internally; visible in folder | first-class GitHub issues |
| Sub-agent use | "My test with slash goal didn't use sub-agents" — but in THIS run, "It's actually using the correct agent. It's using the coder." So **profile use is prompt-dependent, not automatic** |
| Card-move feature | **broken** — drag-and-drop did NOT work | works |
| Edit/delete feature | works | works |
| Compactions during run | **7** (host flagged as concern) | not reported |
| Verdict | "you have something, right?... It's a prototype... would you use this? Absolutely not." | "Ralph did make a better app. Technically, it's not the best by far. It has a long way to go." |

Net: **Ralph better quality, /goal faster.**

---

## Caveats from host on /goal

- 7 compactions during the test "kind of made me worry about if the output will be clean."
- "I wouldn't let it run for 12 hours like people say they did. So it's just my preference."
- Less control: "here, it just says notify me when it finishes" — vs Ralph's visible per-issue progress.

---

## Negative finding — Hermes repo has no shipped profile defaults

Repo audit 2026-05-21 (NousResearch/hermes-agent main branch, GitHub API recursive tree):

| Path | Type |
|---|---|
| `hermes_cli/profiles.py` | Python — profile system implementation |
| `hermes_cli/profile_describer.py` | Python — profile metadata |
| `hermes_cli/profile_distribution.py` | Python — profile distribution |
| `hermes_cli/skills_config.py` | Python — skill config |
| `hermes_cli/skills_hub.py` | Python — skill registry |
| `hermes_cli/skill_bundles.py` | Python — bundled skill orchestration |
| `agent/skill_utils.py` etc. | Python — agent runtime |
| `skills/autonomous-ai-agents/claude-code/SKILL.md` | Markdown — bundled Claude Code skill (previously audited) |

**No `coder.md`, `reviewer.md`, or similar markdown profile defaults.** The `coder` and `reviewer` profile names visible in both videos refer to **user-authored profiles** that the operator creates locally — Hermes ships the profile system as Python code but does not ship example/default profile bodies in the public repo.

Implication for the pilot: **profile content for the orchestrator pattern must be hand-rolled or sourced from the host's comments** (Nemanja offered to attach in the original O-PEeD7fymo video comments). There is no canonical default to audit.

---

## Key takeaways for the orchestrator pilot decision

1. **`/goal` alone is insufficient for the orchestrator pattern's value proposition.** `/goal`'s judge is yes/no, not a code review. The Hermes+Codex+Claude orchestrator video specifically adds Claude as a real reviewer on top of `/goal` — and that addition IS the contribution.
2. **Sub-agent/profile use during `/goal` is prompt-dependent**, not automatic. The orchestrator pattern depends on the prompt explicitly instructing Hermes to delegate to the `coder` and `reviewer` profiles.
3. **Ralph loop remains the host's serious-work default.** The orchestrator pattern is positioned as Ralph-augmented (with cross-CLI reviewers), not as Ralph-replaced.
4. **`/goal` as primitive is cross-vendor now** (Hermes + Codex + Claude). Worth tracking separately for a future corpus-wide audit.
5. **No profile defaults in the repo.** Pilot must hand-author `coder.md` and `reviewer.md` profile bodies — adds 1-2h to setup time beyond install.
6. **7 compactions in a 13-minute run** is a context-bloat signal worth measuring during pilot.
