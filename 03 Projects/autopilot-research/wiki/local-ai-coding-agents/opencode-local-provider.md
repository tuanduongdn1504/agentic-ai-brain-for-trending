# opencode — pointing a terminal agent at a local model

> **First-party:** [opencode.ai/docs](https://opencode.ai/docs) + [github.com/sst/opencode](https://github.com/sst/opencode) (GitHub API cross-checked). Verified in the [[source-provenance|opencode dive]]. Deeper config lives in [[../graphify-codebase-graph/opencode-integration|graphify: opencode integration]].

## What opencode is

- An **open-source, terminal-first AI coding agent** — the Claude-Code UX (project-rooted, slash commands, subagents), but **model-agnostic**.
- **TypeScript, MIT license, ~184K★.** Repo lives under `sst/opencode` but the owning org is **`anomalyco`** (Anomaly — SST and opencode are sister projects). One of the named [[../claude-code-clones/_index|Claude Code clones]].
- **75+ providers via Models.dev**, including **local models** — and *any* OpenAI-compatible endpoint via a custom `baseURL`.

## Configuring a LOCAL provider (the actual mechanism)

In `opencode.json` (project) or `~/.config/opencode/opencode.json` (global), register the LM Studio endpoint as a custom OpenAI-compatible provider:

```jsonc
{
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "http://localhost:1234/v1" },
      "models": { "qwen3.6-27b": {} }
    }
  }
}
```

Then run `opencode` in your repo and select the local model. That's the whole integration — **one `baseURL`**, because [[lm-studio|LM Studio speaks the OpenAI API]].

## ⚠️ The `modalities` correction (C8)

- Beto says: *"you can use image recognition — **you need to pass the modalities here** … once you added this to your JSON…"*
- **opencode has NO `modalities` config key.** The model-config schema supports reasoning params (`reasoningEffort`, `thinking`, `budgetTokens`) and output settings — but not `modalities`/`vision`.
- **How vision actually works:** you **drag-and-drop images into the terminal**; opencode adds them to the prompt automatically on a vision-capable model. No special config.
- **Impact for a builder:** the local vision path is *simpler* than the video implies. Don't copy a `modalities` field into config expecting it to gate vision. (For hireui, still add explicit image-type validation yourself per I-8 — opencode's "just works" default is not input validation.)

## Subagents + the "31 tool calls" (C8)

- **Subagents CONFIRMED:** opencode has 3 built-in — **General** (multi-step executor), **Explore** (read-only codebase explorer), **Scout** (external-doc researcher) — auto-invoked or `@mentioned`. So Beto's "it's running sub-agents" is real.
- **31 tool calls** scanning a whole codebase (detecting Better Auth): **plausible/normal** for an agentic loop on a real repo; no logs to verify the exact number, but nothing implausible.
- **~12 built-in tools:** bash, edit, write, read, grep, glob, lsp, apply_patch, skill, todowrite, webfetch, websearch, question — extensible via custom tools + MCP.

## Why this matters for the operator

opencode is a **vendor-agnostic harness** with a first-class **local-provider path** — the exact property that lets you run **cheap/bulk work on a local model and hard work on a cloud model** from one config. It's a candidate alternative to Claude Code + cc-sdd for hireui's harness (pilot method C1), and its `baseURL`-swap is the same seam idea as the Match-Explain vendor abstraction (method B1).

## Takeaways
- Local opencode = **one `baseURL`** pointed at LM Studio's OpenAI endpoint.
- **No `modalities` setting exists** — vision is drag-and-drop by default (the one factual error in the video).
- Model-agnostic + subagents + MCP make opencode a real harness, not a toy.

## See also
[[lm-studio]] · [[qwen3.6-27b]] · [[../graphify-codebase-graph/opencode-integration|graphify: opencode integration]] · [[../claude-code-clones/_index|claude-code-clones]]
