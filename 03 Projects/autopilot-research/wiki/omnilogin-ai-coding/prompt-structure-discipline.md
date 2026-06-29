# Original #6 — The prompt-structure discipline (HAVE / NEED / STEPS / UI / SAMPLE-DATA)

## Source

The video, `[03:01]`–`[03:29]` — the presenter explicitly pauses to "analyze what a good prompt should contain." This is the most directly transferable nugget for the operator, and it's a teachable template.

## The template

To get a working automation on the first generation, the prompt should contain **five parts, in order**:

1. **HAVE** — state your inputs and their exact shape.
   *"I have several Gmail accounts in this format, one account per line: `email----password`."*
2. **NEED** — state the goal as an artifact.
   *"Create an auto-login process for these accounts, following the steps below."*
3. **STEPS** — spell out the procedure explicitly, step by step (don't make the model guess the flow).
4. **UI** — specify the config surface you want generated.
   *"Include a UI to paste the account list, with sample data."*
5. **SAMPLE DATA** — give a concrete example of the input so the model parses the shape correctly.

## Why it works (and where you've seen it before)

This is **specification before generation** — the same discipline as:

- **Plan-first / spec-first** ([[harness-engineering/_index]], [[multi-agent-orchestration/_index]]) — describe the target before the agent acts.
- **CLAUDE.md Rule 1 (Think before coding)** + **Rule 4 (Goal-driven, define success)** ([[claude-md-12-rules/_index]]).
- **Ben AI's "Prompt Master"** (brain-dump → structured prompt) and **Process Interviewer** ([[claude-skills/_index]]).
- **The Anthropic eval discipline** — examples-with-data beat abstract instructions ([[prompt-evaluation/_index]]).

The genuinely sharp additions over a generic "write a clear prompt" are **(4) explicitly asking for the config UI** and **(5) providing sample data** — these are what make the generated artifact *re-runnable and correctly-parsing*, not just syntactically valid.

## Reusable as

A **codegen prompt skill / template** you drop in front of any "generate an automation/script" task:

```
HAVE:        <inputs + exact format>
NEED:        <the artifact, as a goal>
STEPS:       <numbered procedure>
UI:          <what config surface to generate, if any>
SAMPLE DATA: <one concrete example of the input>
```

## Key takeaways

- Five parts: **HAVE / NEED / STEPS / UI / SAMPLE-DATA** — spec-before-generation, vendor-agnostic.
- The two non-obvious parts — **ask for the config UI** and **give sample data** — are what make the output a usable tool, not just code.
- It's the same plan-first discipline already running through your harness/spec/eval threads; this is a tight, teachable packaging of it (good for Scrum coaching too).

## Cross-links

- [ai-coding-feature](ai-coding-feature.md) — where this prompt drives generation
- [[claude-md-12-rules/_index]] — Rule 1 + Rule 4
- [[claude-skills/_index]] — Prompt Master / Process Interviewer
- [[prompt-evaluation/_index]] — examples-with-data discipline
