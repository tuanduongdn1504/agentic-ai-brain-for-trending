# Codex CLI's Skills feature — what's actually real

## The claim (as demoed)

The video shows: a hidden `.codex` folder in the user's home directory, containing an existing (empty) `skill` subfolder; the presenter copies a downloaded skill folder into it; the skill is then invoked in Codex CLI's chat via `$teach`.

## Verified: the feature is real, and it's on the same open spec as Claude Code + GitHub Copilot

Confirmed directly (main-loop `WebFetch`/`WebSearch`, not just the workflow's dive/verify pass — see [[source-provenance]] for why the extra check was needed):

- **OpenAI Codex CLI shipped an official Skills feature on 2025-12-19** — independently corroborated by [Simon Willison's post](https://simonwillison.net/2025/Dec/12/openai-skills/) ("OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI") and [blog.fsck.com's "Skills in OpenAI Codex"](https://blog.fsck.com/2025/12/19/codex-skills/), plus OpenAI's own docs at `developers.openai.com/codex/skills` (redirects to `learn.chatgpt.com/docs/build-skills`).
- **A skill is a folder containing a required `SKILL.md`** (YAML frontmatter with `name` + `description`, then instructions) plus optional `scripts/`, `references/`, `assets/`, and an `agents/openai.yaml` config — the same shape as Claude Code's and GitHub Copilot's Skills.
- **It follows the open `agentskills.io` spec** — per OpenAI's own docs ecosystem: "SKILL.md is a cross-agent standard. The same SKILL.md files that work in Claude Code and OpenClaw work in Codex CLI." This makes **OpenAI a third vendor confirmed on the literal shared spec**, alongside Anthropic Claude Code and GitHub Copilot CLI (already verified in [[../github-copilot-cli-agents/agent-skills-shared-standard]]) — distinct from Pydantic AI's case, which independently converged on the *pattern* without adopting the spec itself.

## Correction: the canonical path has moved

**The video's exact install location (`~/.codex/skill/`) is not what OpenAI's current official docs specify.** Per `learn.chatgpt.com/docs/build-skills`, fetched directly:

- **User scope:** `$HOME/.agents/skills` — "any skills checked into the user's personal folder"
- **Repository scope:** `$CWD/.agents/skills`, `$CWD/../.agents/skills`, `$REPO_ROOT/.agents/skills`
- **Admin scope:** `/etc/codex/skills`

`~/.agents/skills` is a **shared, cross-vendor location** (part of the same `AGENTS.md`-adjacent convention family), not a Codex-specific folder. `~/.codex/skills` appears to be a legacy/earlier default that the video's demo still reflects — plausible since the video (2026-06-28) sits close to the feature's original December 2025 rollout, and OpenAI's own community forum has an open thread (April 2026) about skills-discovery inconsistencies between the two paths. The core claim — "Codex CLI has a real folder-drop Skills feature" — is **true**; the specific path shown is **outdated/non-canonical**.

## Confirmed: `$skillname` is a real, first-class invocation mechanism

Directly quoted from OpenAI's own docs: *"In CLI/IDE, run `/skills` or type `$` to mention a skill."* This is **not** a prompt-engineering convention baked into the skill's own instructions — it's a CLI-level feature, functionally parallel to Claude Code's `/` slash-commands. OpenAI's own built-in skills use the same syntax (`$skill-creator`, `$skill-installer linear`).

## Verdict

**CORRECT_BUT_INCOMPLETE** on the folder-feature claim (real feature, outdated path) — **CONFIRMED** on the `$`-invocation claim. See [[claims-scorecard]].

## Why this matters for hireui

Nothing directly actionable here (hireui doesn't use Codex CLI), but it reinforces a pattern already banked in [[../github-copilot-cli-agents/agent-skills-shared-standard]]: Skills as a concept are now a genuinely cross-vendor, spec-level convention, not a Claude-only bet. Any `SKILL.md` authored for hireui's own tooling would in principle be portable to Codex CLI too.

## See also

[[_index]] · [[matt-pocock-provenance]] · [[../github-copilot-cli-agents/agent-skills-shared-standard]] · [[claims-scorecard]] · [[source-provenance]]
