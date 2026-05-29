# (C) entity-2 — The concept stack: subagents + MCP + Skills

The talk's premise is that *combining* three Claude Code primitives — subagents, MCP servers, and custom Skills — is the unlock for shipping a real multi-role app fast. This entity documents those primitives from authoritative Anthropic sources, so a reader who has not watched the video still understands the building blocks.

## Primitive 1 — Subagents

**Authoritative source:** Anthropic "Skills explained" blog post (https://claude.com/blog/skills-explained); Anthropic Claude Code docs.

**What a subagent is:**
- A specialized AI assistant with its **own context window** (separate from the parent agent's)
- Has its **own custom system prompt** defining its role and responsibilities
- Has **specific tool permissions** (the parent can grant a subset of its own tools)
- Available in **Claude Code** and the **Claude Agent SDK**
- Invoked by the parent agent when work matches the subagent's specialization

**Why this matters for a 5-role app:**
- Each role (in the talk's "five roles") plausibly maps to a subagent — though the exact mapping is undocumented in public sources.
- Context-window isolation prevents role-specific noise from polluting the orchestrator's attention.
- Tool-permission scoping is a security primitive: e.g., the "deploy" subagent gets `gcloud` but not the repository write permission.

**Citation:** Anthropic Claude Code docs on subagents; see also Anthropic blog "Skills explained" for how subagents compose with Skills and MCP.

## Primitive 2 — MCP servers (Model Context Protocol)

**Authoritative source:** modelcontextprotocol.io; Anthropic Claude Code docs; Anthropic "Skills explained".

**What MCP is:**
- An **open standard** for connecting AI assistants to external systems where data and tools live
- Targets: content repositories (e.g., GitHub, Google Drive), business tools (e.g., Slack, Linear), databases, dev environments, cloud APIs
- An MCP **server** exposes a typed set of tools, resources, and prompts that any MCP-compatible **client** (Claude Code, Claude Desktop, Codex, etc.) can consume
- Decouples "what an agent can do" from "which agent" — the same MCP server works across clients

**Why this matters for a Google-Cloud-targeted live build:**
- Google Cloud operations (deploying to Cloud Run, querying BigQuery, reading Secret Manager, etc.) plausibly happen through an MCP server.
- A custom MCP server can wrap the team's internal feedback database / Jira / etc.
- The talk's mention of "MCP servers" (plural) suggests more than one — likely a mix of GCP and feedback-app-internal.
- **Note:** Which specific MCP servers are wired up in the demo is NOT documented in the public abstract — see [[entity-4-content-gaps-and-ingest-path]].

## Primitive 3 — Custom Skills (Agent Skills)

**Authoritative source:** Anthropic "Skills explained" blog (https://claude.com/blog/skills-explained); Anthropic Claude Code Skills docs.

**What a Skill is:**
- A **portable expertise unit** — a small Markdown file (`SKILL.md`) + optional supporting files (templates, schemas, references) that gives Claude domain-specific knowledge or workflows
- Triggered by the agent when context matches the skill's description
- Installable across harnesses (Claude Code, Codex, Cursor, etc. via the `agent-skills-standard` ecosystem)
- **Subagents can access and use Skills** just like the main agent — so specialized subagents leverage portable expertise (per Anthropic "Skills explained")

**Why this matters for the talk:**
- "Custom skills" in the abstract implies the speaker authored skills specific to the feedback-app domain (e.g., a "feedback-schema" skill, a "deploy-to-cloud-run" skill — these are plausible guesses, **not confirmed**).
- The combination "subagents + skills" is what Anthropic explicitly highlights as a unlock: "specialized subagents leverage portable expertise" ([Skills explained](https://claude.com/blog/skills-explained)).
- Skills are the lightest of the three primitives (just Markdown) — typically the fastest to demo.

## How the three compose (per Anthropic guidance)

From Anthropic's "Skills explained":

- **Subagents** = *who* is doing the work (role + scoped tools + isolated context)
- **MCP** = *what tools* the agent can reach (external systems)
- **Skills** = *what expertise* the agent brings (portable domain knowledge / workflows)

A multi-role app is then: **N subagents**, each with **a curated MCP server allowlist** and **a relevant Skill set**, orchestrated by a parent agent that routes work.

The talk's claim is that this composition lets you ship a feedback app in 30 minutes.

## Out-of-corpus reference

The Storm Bear vault has corpus entries that directly inform this entity:

- **v71 agents-best-practices** (DenisSergeevitch) — provider-agnostic agentic framework with the "model proposes, harness disposes" execution-separation pattern
- **v76 agent-skills-standard** (HoangNguyen0403) — codifies the portable-Skills standard across 10+ AI agents; same Vietnamese DevRel author archetype
- **v78 ECC corpus-recursive revisit** (affaan-m) — 232-skill + 60-agent + 75-command operator system as the maximal expression of this stack
- **v81 taste-skill** (Leonxlnx) — multi-skill brand portfolio with 12 skills via `npx skills add`
- **v82 huashu-design** (alchaincyf) — HTML-native design skill demonstrating single-skill multi-target distribution

The talk lands in the same conceptual neighborhood — but at the *demo / pedagogical* layer, not the *codified-ecosystem-product* layer those corpus subjects occupy.

## What is NOT in this entity

- The specific subagent decomposition the speaker chose (5 roles → 5 subagents? 1 orchestrator + 4 workers? unknown)
- The exact MCP servers wired in the demo
- The Skill content
- Code excerpts

See [[entity-4-content-gaps-and-ingest-path]] for the inventory of what video ingest would resolve.
