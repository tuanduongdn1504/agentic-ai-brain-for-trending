# (C) entity-3 — Companion resources and speaker context

This entity inventories everything publicly attached to the speaker and the talk's topic that helps a reader either (a) understand the talk's background or (b) reproduce something close to its build.

## Speaker — Ivan Nardini

| Channel | URL | Role |
|---|---|---|
| Employer profile | https://www.linkedin.com/in/ivan-nardini/ | Developer Relations Engineer (AI/ML), Google Cloud |
| GitHub | https://github.com/inardini | ~40 public repos focused on Vertex AI / Gemini / Claude tooling |
| Medium | https://ivnardini.medium.com/ | Long-form tutorials on Google Cloud AI/ML |
| Twitter / X | https://x.com/ivnardini | Frequent posts on Vertex AI Agent Builder, ADK, MCP |

**Public expertise overlap with the talk:**
- Co-instructor, DeepLearning.AI short course *A2A: The Agent2Agent Protocol*
- Multiple Medium tutorials on Claude Code + Vertex AI integration
- Author of the companion infrastructure repo (next section)

## Companion repo — `ship-code-with-claude-on-vertex-ai-webinar`

**URL:** https://github.com/inardini/ship-code-with-claude-on-vertex-ai-webinar
**License:** Apache 2.0 (not officially supported by Google)
**Last updated:** 2026-04-05 (~1 month pre-talk)

**Important distinction:** This repo is **NOT** the "feedback app" from the talk. It is a *separate* artifact attached to a different event (the Vertex AI webinar). Verified via README fetch 2026-05-21.

**What it actually is** (per README):
- A pre-configured Google Cloud developer environment
- Web portal serving VS Code in the browser (`code-server`) with Claude Code CLI pre-installed
- Terraform-managed infrastructure with two-persona deployment (Platform Admin + Developer)
- Three demo applications:
  1. Sandboxed code execution + Vertex AI Search (MCP on Cloud Run)
  2. LLM Gateway via LiteLLM with OpenTelemetry tracing
  3. BigQuery analytics dashboard for token usage / cost
- Security: IAP authentication, VPC-isolated VM, no public IP, Cloud NAT for outbound

**Tech stack (per README):**
- Terraform / HCL (34.3% of code)
- Shell (31.7%)
- HTML (25.1%)
- JavaScript (8.7%)
- Dockerfile (0.2%)
- FastMCP, LiteLLM, BigQuery, Cloud Trace

**Why it's still relevant to the talk:**
- Same speaker, same Claude-Code-on-Google-Cloud pedagogical context
- The repo's *infrastructure pattern* (Cloud Run + VPC + IAP) is plausibly close to what the talk's "feedback app" deployment uses
- The MCP-on-Cloud-Run pattern (demo 01) is a directly applicable building block

## Related Anthropic resources

| Resource | URL | What it covers |
|---|---|---|
| Anthropic at Google Cloud Next 2026 | https://www.anthropic.com/events/anthropic-at-google-cloud-next-2026 | Event hub with related sessions |
| Building agents with Claude on Vertex AI (webinar) | https://www.anthropic.com/webinars/agents-with-claude-on-vertex | Claude Code + Claude on Vertex AI + Google ADK integration |
| Building with Advanced Agent Capabilities for Claude on Vertex AI (webinar) | https://www.anthropic.com/webinars/claude-on-vertex-ai | More-advanced agent capabilities |
| Claude with Google Cloud's Vertex AI (Skilljar course) | https://anthropic.skilljar.com/claude-with-google-vertex | Self-paced course |
| Skills explained (foundational concept doc) | https://claude.com/blog/skills-explained | The subagents-vs-MCP-vs-Skills decision framework |
| Claude Code best practices | https://code.claude.com/docs/en/best-practices | General Claude Code guidance |

## Related Google Cloud Medium tutorials (third-party / community)

| Article | URL | Author |
|---|---|---|
| Set up Claude Code with Vertex AI | https://medium.com/google-cloud/set-up-claude-code-with-vertex-ai-8e1c9d1c9a69 | Giovanni Galloro |
| How We Built an Enterprise-Grade Claude Code Gateway on GCP | https://medium.com/@francisco.ferreira/how-we-built-an-enterprise-grade-claude-code-gateway-on-google-cloud-platform-42be6297a760 | Francisco Ferreira |
| Claude Code subagents + MCP + SOC AI Runbooks | https://medium.com/google-cloud/claude-code-subagents-mcp-soc-ai-runbooks-%EF%B8%8F-8ead2e2f7745 | Dan Dye |
| Supercharge Tech Writing with Claude Code Subagents and Agent Skills | https://medium.com/google-cloud/supercharge-tech-writing-with-claude-code-subagents-and-agent-skills-44eb43e5a9b7 | Kaz Sato |
| Run Claude Code on Google Cloud (GCP credits) | https://dev.to/timtech4u/run-claude-code-on-google-cloud-use-your-gcp-credits-for-ai-coding-desktop-control-and-more-2151 | timtech4u |

These articles each implement a slice of the "Claude Code + Google Cloud + subagents + MCP + Skills" pattern. Reading any of them gives a stronger reproduction recipe than the talk's abstract alone provides.

## Workshop / live event (follow-up)

Anthropic + Google Cloud ran a follow-up in-person workshop on 2026-05-29 in SF, 9:00 AM – 12:30 PM PT, where attendees set up Claude and Claude Code on Google Cloud and build working prototypes through guided labs. Source: Google Developer forums announcement (https://discuss.google.dev/t/google-cloud-claude-code-workshop-5-29-in-sf-ca/364279). Lab materials from that workshop, if published, would be the *closest publicly-available reconstruction recipe* for the talk's build.

## What is NOT covered here

- The talk's actual code repo (if any was published)
- Whether the feedback app was open-sourced post-talk

Both items belong in [[entity-4-content-gaps-and-ingest-path]].
