# (C) index — Building with Claude on Google Cloud

**Subject:** 30-minute live build session at Code with Claude 2026 (SF), 2026-05-06. Speaker: Ivan Nardini (Google Cloud DevRel, AI/ML). Live build of a "feedback app spanning five roles and the full software lifecycle" using Claude Code + Google Cloud + subagents + MCP servers + custom skills.

**Entry point:** Operator submitted the Vietnamese-dubbed cut at `youtube.com/watch?v=JUeazROlMCU`. The original-language video is `youtube.com/watch?v=SqHsS737CeA`.

## What's verifiable (now: public sources + auto-caption transcript)

1. **Session abstract** — confirms the build's 5-role + full-SDLC + 30-min + Claude + Google Cloud + 3 primitives (subagents, MCP, custom skills) framing.
2. **Concept primitives** — Anthropic blog + docs confirm what subagents, MCP servers, and custom skills are and how they compose.
3. **Speaker / event metadata** — Anthropic session page + speaker LinkedIn + Anthropic event page.
4. **Companion infrastructure repo** — same speaker, related topic, NOT the feedback app itself (confirmed via README fetch).
5. **Full build content** — transcript at [(C) transcript-raw.md]((C) transcript-raw.md) (yt-dlp en-original auto-captions, extracted 2026-05-21). Resolves G1, G3, G4, G6, G7 from the original gap inventory.

## Quick-reference: the build (transcript-verified)

- **App:** feedback collection web app, live audience interaction during talk
- **5 roles:** PM → UI/UX → Software Engineer → Security Engineer → Growth Marketer/Data Analyst
- **Stack:** Cloud Run (API) + Firestore (raw) + BigQuery (analytics) + Looker (dashboards)
- **Model auth:** Claude on Vertex AI via Application Default Credentials (ADC)
- **Primitives:** plan mode (UI/UX hat) · 3 parallel subagents (Software Engineer hat: API/ingestion/dashboard) · Developer Knowledge MCP + BigQuery MCP + MCP Toolbox for DB (Looker) · Google Cloud Skills (Cloud-Run-deploy, Cloud-Run+Firestore) + Claude Code pre-built security-review skill

## What still ISN'T verifiable (post-transcript residual gaps)

Surviving gaps per [[entity-4-content-gaps-and-ingest-path]] G2/G5/G9/G10 + entity-8 U1–U10:

- Exact prompts at each hat, full CLAUDE.md, subagent definitions, skill bodies (load-bearing for reproduction) — speaker promised a code release that has not been located as of 2026-05-21
- Claude model variant (Sonnet / Opus / Haiku)
- Region selection (global vs regional endpoint)
- Demo cost
- Failure modes the demo papers over

## Entity index

- [[entity-1-talk-metadata]] — speaker, event, dates, authoritative session page text
- [[entity-2-the-concept-stack-subagents-mcp-skills]] — the 3 Claude Code primitives the talk composes, each with citation to Anthropic docs
- [[entity-3-companion-resources-and-speaker-context]] — speaker's other public work, related Anthropic webinars, related blog posts
- [[entity-4-content-gaps-and-ingest-path]] — gap inventory + ingest path (G1, G3, G4, G6, G7 now RESOLVED via transcript)
- [[entity-5-build-architecture]] — Cloud Run + Firestore + BigQuery + Looker; Claude on Vertex AI via ADC; subagents + MCP + Skills composition (transcript-verified)
- [[entity-6-role-decomposition]] — the 5 hats (PM / UI/UX / Software Engineer / Security Engineer / Growth Marketer) with affordances per role
- [[entity-7-step-by-step-build]] — chronological walk of all 26 minutes; demo vs slide vs transition annotation
- [[entity-8-pitfalls-and-simplifications]] — 5 speaker-acknowledged + 10 unspoken gaps; reproduction-readiness verdict

## Citation discipline

All factual claims in entity pages link back to one of these primary sources:

| Source | URL |
|---|---|
| Anthropic session page (abstract) | https://claude.com/code-with-claude/session/sf-building-with-claude-on-google-cloud |
| Original-language video | https://www.youtube.com/watch?v=SqHsS737CeA |
| Vietnamese-dubbed video (operator entry-point) | https://www.youtube.com/watch?v=JUeazROlMCU |
| Auto-caption transcript (this vault) | [(C) transcript-raw.md]((C) transcript-raw.md) |
| Anthropic: Skills explained (subagents/MCP/Skills comparison) | https://claude.com/blog/skills-explained |
| Anthropic: Claude Code best practices | https://code.claude.com/docs/en/best-practices |
| Anthropic at Google Cloud Next 2026 | https://www.anthropic.com/events/anthropic-at-google-cloud-next-2026 |
| Related webinar — Building agents with Claude on Vertex AI | https://www.anthropic.com/webinars/agents-with-claude-on-vertex |
| Speaker GitHub | https://github.com/inardini |
| Companion webinar repo (different artifact) | https://github.com/inardini/ship-code-with-claude-on-vertex-ai-webinar |
| Speaker Medium | https://ivnardini.medium.com/ |
| Speaker LinkedIn | https://www.linkedin.com/in/ivan-nardini/ |
| Companion Medium tutorial | https://medium.com/google-cloud/set-up-claude-code-with-vertex-ai-8e1c9d1c9a69 |

## Status

- **Built:** 2026-05-21
- **Routine:** v2.2 *adapted for out-of-typology video subject*
- **Phase 0.9 STRICT inclusion:** not applicable (subject is a video / knowledge-source, not a T1-T5 product)
- **Pattern Library impact:** none yet — see CLAUDE.md "Typology call" section for routine-v2.3 codification candidate
- **Completeness:** transcript-deep. 8 entity pages + transcript-raw. Build architecture, role decomposition, chronology, and pitfalls all transcript-verified. Surviving gaps are code-release-bound (prompts/skills/subagent definitions).

## Log

See [(C) log.md]((C) log.md) for build history.
