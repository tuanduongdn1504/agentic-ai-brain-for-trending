# Hermes `/goal` mechanics + cross-vendor primitive emergence

> **Sources:** Nemanja Mirkovic — [I Was Wrong About Hermes Agent /goal](https://www.youtube.com/watch?v=CKtz9lp8X-8), 2026, 19:09 + repo audit of [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) main branch tree (2026-05-21)
> **Raw:** `raw/2026-05-21-nemanja-goal-vs-ralph-transcript.md`
> **Compiled:** 2026-05-21
> **Status:** Prerequisite article for [[personal-repo-hermes-orchestrator]] — closes the open questions on what `/goal` actually does, what profile defaults ship, and why the orchestrator pattern adds value on top of `/goal`.

---

## Why this article exists

Three questions had to be answered before a pilot of the orchestrator pattern in [[personal-repo-hermes-orchestrator]] would be informed:

1. What does `/goal` actually do? (Is it a code-reviewer or just a controller?)
2. Does the Hermes repo ship `coder.md` / `reviewer.md` profile defaults that a pilot could adopt directly?
3. Is `/goal` Hermes-exclusive or a cross-vendor primitive?

Targeted ingest 2026-05-21 answers all three.

---

## `/goal` is a controller, NOT a reviewer (5-stage architecture)

```
1. Accept goal
   ↓
2. Plan — decompose initial prompt into PRD-style document
   ↓
3. Execute step
   ↓
4. Judge: done? (yes/no — NOT a code reviewer, NOT a verifier)
   ↓ no                          ↓ yes
   loop back to step 3           exit clean / report
```

Host's verbatim framing:

> "What you have to understand is that the judge is not a code reviewer, it's not a verifier, it's just a simple yes or no check to see if the loop continues or exits, if there are any blockers or not. And with Ralph loop, you can actually have a proper code review stage or even third-party code review, so you can get as close to production code as possible."

**This is the load-bearing distinction that makes [[personal-repo-hermes-orchestrator]] interesting.** The orchestrator pattern is `/goal` PLUS a real code reviewer (Claude Code CLI invoked as subprocess) — because `/goal` alone has no review stage, only the binary judge.

If you adopt `/goal` without the Codex+Claude composition, you get a loop with no quality gate. That is exactly the gap the orchestrator pattern fills.

---

## `/goal` vs Ralph vs Kanban decision matrix (per host)

| Tool | Best for | Quality | Speed | Operator visibility |
|---|---|---|---|---|
| **`/goal`** | Specific tasks with clear end state — framework migrations (NPM→PNPM, Supabase→local-JSON). "Just type `/goal` and do something." | Lower (no review stage) | High | Low — "notify me when it finishes" |
| **Ralph loop** | Serious projects, architecture-first coding, actual features, production work | Higher (GitHub-issue-based PRD + reviewer model) | Lower (~1 hour for the demo task) | High — visible PRD, per-issue progress, stop/resume |
| **Kanban** | Non-code tasks — content production, research, scripts, social posts | N/A | Most token-efficient per host | High — board visible |

Host's verdict: *"I probably won't be replacing Ralph with /goal right now. I might be implementing /goal in some way."* He uses Ralph daily for serious work.

The orchestrator pattern in [[personal-repo-hermes-orchestrator]] is positioned as a NEW option that combines `/goal`-style automation with Ralph-style review quality — by adding cross-vendor reviewers, not by replacing Ralph's GitHub-issue substrate.

---

## Live A/B observations (same Next.js+SQLite Kanban prompt, both tools)

| Aspect | `/goal` result | Ralph result |
|---|---|---|
| Model used | GPT-5.5 single setting | GPT-5.5 low for slicing + GPT-5.5 high for review |
| Time to finish | minutes | ~1 hour |
| Sub-agent / profile use | **Prompt-dependent.** Host: *"My test with slash goal didn't use sub-agents"* — but in this test, `coder` profile WAS used because the prompt invoked it. Not automatic. |
| Drag-and-drop card-move | **Broken** | Works |
| Edit/delete cards | Works | Works |
| Compactions during run | **7** (host flagged) | not reported |
| Verdict | "It's a prototype... would you use this? Absolutely not." | "Ralph did make a better app... from features it looks better" |

Key implication for the orchestrator pattern: **profile use is not automatic**. The prompt must explicitly instruct Hermes to delegate to the `coder` and `reviewer` profiles. The orchestrator video's prompt did this; a casual `/goal` invocation will NOT trigger the role split.

---

## `/goal` is now a cross-vendor primitive (corpus signal)

> "Codex actually has goal as well, and now Claude has this as well."

Confirmed in this video without source citations. If true, **`/goal` (or its equivalent) is a primitive emerging across all 3 major harnesses simultaneously**, not a Hermes-exclusive feature.

This is corpus-relevant for the Storm Bear Pattern Library — Ralph-loop-as-slash-command is becoming a category, not a single instance. Worth tracking separately for a future cross-vendor audit. Likely candidates to verify in the parent corpus:
- Codex CLI: does it ship a `/goal` or equivalent? (search: codex CLI slash commands May 2026)
- Claude Code: does it ship a `/goal` or equivalent? (Anthropic added several slash commands in the 2026-Q2 wave — audit needed)

Until those are verified, this remains an N=1 claim from a single video.

---

## Repo audit — defaults exist in a SEPARATE companion repo (corrected 2026-05-21)

Initial repo audit of `NousResearch/hermes-agent` main branch (2026-05-21) returned no shipped `coder.md` / `reviewer.md` markdown defaults — the profile system is implemented as Python (`hermes_cli/profiles.py`, `profile_describer.py`, `profile_distribution.py`, `skills_config.py`, `skills_hub.py`, `skill_bundles.py`) and the only shipped markdown asset for Claude integration is `skills/autonomous-ai-agents/claude-code/SKILL.md`.

**Correction:** A YouTube-comments audit (2026-05-21) on the O-PEeD7fymo video revealed that Nemanja maintains a **companion artifact repo** at [github.com/nemanjadotcom/goal-video-resources](https://github.com/nemanjadotcom/goal-video-resources) containing the actual profile files used in the orchestrator video — under the term "SOUL" rather than "profile":

| Path | Content |
|---|---|
| `03-hermes-codex-claude/PROMPT.md` | The actual `/goal` prompt used in the video |
| `03-hermes-codex-claude/AGENTS.md` | Orchestrator project memory (6-stage Kanban graph spec) |
| `03-hermes-codex-claude/SOUL-codexbuilder.md` | The builder profile body |
| `03-hermes-codex-claude/SOUL-claudereviewer.md` | The reviewer profile body |

Full verbatim in `raw/2026-05-21-nemanja-goal-video-resources-repo.md`.

**Why the initial search missed:** "SOUL" is the Hermes term for what the video calls "profile" — `coder.md` / `reviewer.md` was the wrong filename pattern to search for.

### Critical clarification from PROMPT.md (verbatim)

The PROMPT.md used in the video **explicitly forbids using Hermes profiles**:

> "Do NOT use Hermes agent profiles for this test. Do NOT delegate to `hermes -p coder`, `hermes -p reviewer`, or any subagent profile. Use Codex CLI directly for implementation. Use Claude Code CLI directly for review."

So the demo shown in the video used a **simpler architecture than the SOUL files prescribe** — Hermes orchestrates via Kanban (for visibility only) and shells out to `codex` + `claude` CLIs directly, without profile indirection. The SOUL files are **aspirational** / for a future iteration.

### Implication for the pilot — revised down

| Item | Cost |
|---|---|
| Install Hermes + Codex CLI + Claude Code CLI | ~30 min (host says it's automatable via Hermes prompt) |
| Copy PROMPT.md + AGENTS.md from companion repo | **5 min** (no hand-rolling needed for the demo's actual architecture) |
| Decide whether to use the demo's no-profile setup OR the more elaborate SOUL-profile setup | 15 min |
| Pilot one cycle to measure | +1 hour |
| Env-hygiene checks (per [subscription-billing audit](../../output/(C)%202026-05-21-subscription-billing-verification.md)) | +15 min |
| Set Anthropic billing "extra usage" cap to $0 (Nemanja's operational safeguard) | 5 min |

**Revised total realistic pilot time: ~2 hours** (was ~3-4 hours; halved by discovering the companion repo eliminates profile authorship for the demo path).

### Important: the reviewer SOUL prescribes `claude -p` (API-billing risk)

If the pilot does adopt the SOUL-claudereviewer.md profile (i.e., upgrades from the no-profile demo to the full Kanban-profile architecture), the prescribed invocation is:

```
claude -p "Review this repo against AGENTS.md. Do not edit files. Return approved=true/false with blocking findings and evidence." --allowedTools "Read,Bash" --max-turns 10
```

Per the [subscription-billing audit](../../output/(C)%202026-05-21-subscription-billing-verification.md), `claude -p` is documented to require `ANTHROPIC_API_KEY` (= API billing, not subscription). Commenter `@kikserthg233` raised exactly this objection on the video: *"claude -p will be billed same as if api is used."* Nemanja's reply was an operational mitigation, not an architectural rebuttal: *"I had extra usage turned off in my account during this test."* — meaning he capped billing at $0 rather than avoiding the API path.

**Pilot guidance:** apply both safeguards together — set `extra usage` cap to $0 AND verify env-hygiene (`unset ANTHROPIC_API_KEY`). If the reviewer fails to start under that combination, you've empirically confirmed the API-billing dependency and can decide whether to (a) accept it and budget for API costs, (b) revert to the demo's interactive-mode no-profile setup, or (c) abandon the pattern.

---

## Updated open questions for the orchestrator pilot

1. ~~What does `/goal` do?~~ **Answered:** 5-stage controller with yes/no judge, no review.
2. ~~Do profile defaults ship?~~ **Answered with correction:** Hermes ships profile *system* as Python; profile *bodies* (SOUL files) for the orchestrator pattern are published in Nemanja's companion repo `nemanjadotcom/goal-video-resources`. Demo did NOT use the SOUL profiles — it used Hermes shelling out to CLIs directly.
3. **Is `/goal` actually a cross-vendor primitive on Codex + Claude?** (claim is host-asserted, not yet verified in this corpus)
4. ~~What does Nemanja's `coder.md` / `reviewer.md` contain?~~ **Answered:** verbatim in `raw/2026-05-21-nemanja-goal-video-resources-repo.md`. Reviewer profile prescribes `claude -p` (API-billing dependency confirmed). Builder profile prescribes either interactive Codex `/goal` or `codex exec --full-auto` fallback.
5. **Does the 7-compactions-per-run rate hold in the orchestrator pattern**, or does adding Claude as reviewer reduce it? Worth measuring.
6. **Empirical question for pilot:** with `extra-usage` capped at $0 AND `ANTHROPIC_API_KEY` unset, does the reviewer leg (a) succeed via OAuth fallback, (b) fail outright, or (c) hit the billing cap and block? Resolves whether the architecture is genuinely cost-zero or operationally cost-zero only because of the cap.

---

## Cross-references

- [[personal-repo-hermes-orchestrator]] — the orchestrator pattern that this article is a prerequisite for. The orchestrator's value = `/goal` (controller) + Codex (builder) + Claude (real reviewer, not a judge).
- [[personal-repo-router-multimodel]] — alternative cross-vendor mechanism (router-mediated instead of orchestrator-mediated).
- [[personal-repo-patterns]] — 12 individual-scale techniques; Ralph loop appears there as a pattern primitive.
- `../../output/(C) 2026-05-21-subscription-billing-verification.md` — env-hygiene rules that apply to any pilot of the orchestrator pattern.
- External: [Hermes' bundled Claude Code SKILL.md](https://raw.githubusercontent.com/NousResearch/hermes-agent/main/skills/autonomous-ai-agents/claude-code/SKILL.md) — the only shipped markdown asset for the Claude integration.
