# (C) entity-1 — Talk metadata

## The talk

- **Title:** Building with Claude on Google Cloud
- **Speaker:** Ivan Nardini — Developer Relations Engineer (AI/ML), Google Cloud
- **Event:** Code with Claude 2026
- **Location:** San Francisco
- **Date / time:** 2026-05-06, 4:05 PM – 4:35 PM PT (30 min)
- **Format:** Live build + demo
- **Authoritative session page:** https://claude.com/code-with-claude/session/sf-building-with-claude-on-google-cloud

## Authoritative abstract (verbatim from Anthropic session page)

> "A live build from zero to deployed in thirty minutes. We'll build a feedback app spanning five roles and the full software lifecycle, using Claude and Google Cloud alongside subagents, MCP servers, and custom skills."

That single paragraph is the load-bearing source for what the demo covers. Everything more specific (which roles, which Google Cloud services, which MCP servers, which custom skills) is **not stated** in the abstract and requires the video itself to verify.

## Decomposition of the abstract — what's claimed

| Claim | What it commits to | What is left undefined |
|---|---|---|
| "zero to deployed" | App is actually shipped, not just scaffolded | Deployment target (Cloud Run? GKE? App Engine? Vertex AI Reasoning Engine?) |
| "in thirty minutes" | Time-boxed live demo | — |
| "feedback app" | A user-feedback-collection product | Whose feedback (employees? customers? users of another product?) |
| "spanning five roles" | Five distinct user/agent roles | The role names + responsibilities |
| "full software lifecycle" | Design → build → test → deploy → operate (the canonical SDLC) | Which lifecycle phases are demonstrated vs. skipped |
| "using Claude" | Claude as the model | Which Claude variant (Opus, Sonnet, Haiku); via Vertex AI or direct API |
| "Google Cloud" | Some GCP services involved | Which services |
| "subagents" | Claude Code subagents — specialized agents with own context + tools | Subagent count, names, decomposition strategy |
| "MCP servers" | One or more Model Context Protocol servers | Which MCP servers (filesystem? GitHub? GCP-specific? custom?) |
| "custom skills" | Author-defined Agent Skills | Skill scope and content |

## Video artifacts

| Artifact | URL | Provenance |
|---|---|---|
| Original-language video (English, Anthropic-hosted) | https://www.youtube.com/watch?v=SqHsS737CeA | Anthropic / Code with Claude channel |
| Vietnamese-dubbed cut (operator entry-point) | https://www.youtube.com/watch?v=JUeazROlMCU | Third-party localization (publisher not yet identified) |

The two videos cover the same underlying content. The Vietnamese cut adds dubbed audio; the underlying live-build footage is the same.

## Speaker context (one-line)

Ivan Nardini is a Google Cloud DevRel engineer focused on AI/ML — co-instructor of the DeepLearning.AI short course *A2A: The Agent2Agent Protocol*, author of multiple Medium tutorials on Claude + Vertex AI, and maintainer of public companion repos for related Anthropic / Google Cloud webinars. Full speaker context in [[entity-3-companion-resources-and-speaker-context]].

## What is NOT in this entity

- The actual build steps. See [[entity-4-content-gaps-and-ingest-path]].
- A reproduction recipe. The session page links neither code nor a step-by-step.
