# (C) entity-5 — Build architecture (from transcript)

All claims here trace to specific timestamps in [(C) transcript-raw.md]((C) transcript-raw.md). Auto-caption fidelity caveat applies — product names verified against the live demo + Google Cloud public docs.

## The deployed application

**What it is:** A feedback collection web app. Audience members rate the talk via a web form; submissions land in real time on a dashboard; an LLM "feedback analyzer" generates a sentiment summary on demand.

**Confirmed live during the demo** (transcript [00:19:33]–[00:20:35]): app deployed to Cloud Run, a real audience member rated the talk a "5", dashboard updated in real time, feedback analyzer button summarized the comment.

## The end-to-end architecture (transcript [00:12:58]–[00:13:58])

```
                                       ┌──────────────────────────────────┐
   user (audience)                     │  Claude on Vertex AI             │
       │                               │  (auth via ADC; per-token)       │
       ▼                               └──────────────────────────────────┘
   ┌────────────────┐                            ▲
   │  Feedback web  │                            │ called by feedback-analyzer
   │  app (HTML +   │                            │ button
   │  realtime UI)  │                            │
   └───────┬────────┘                            │
           │ POST                                │
           ▼                                     │
   ┌────────────────┐    write raw    ┌─────────────────┐
   │  Feedback API  │ ───────────────►│   Firestore     │
   │  (Cloud Run,   │                 │   (raw          │
   │  serverless)   │                 │   responses)    │
   └────────────────┘                 └────────┬────────┘
                                               │ ingestion pipeline
                                               ▼
                                      ┌─────────────────┐
                                      │   BigQuery      │
                                      │   (analytical   │
                                      │   warehouse,    │
                                      │   post-process) │
                                      └────────┬────────┘
                                               │
                                               ▼
                                      ┌─────────────────┐
                                      │   Looker        │
                                      │   (dashboard,   │
                                      │   KPIs incl.    │
                                      │   response time)│
                                      └─────────────────┘
```

## Component-by-component (verified from transcript)

| Component | Service | Why | Transcript anchor |
|---|---|---|---|
| Claude model | **Vertex AI** (Claude as managed model) | Per-token billing (no message cap), enterprise option of provisioned throughput, ADC-based auth, data stays in project, global + regional endpoints | [00:04:14]–[00:06:18] |
| Auth | **Application Default Credentials (ADC)** | "No API to rotate, no environment variable to set... it's a happy journey" — recently added wizard auto-detects project + region + lists available models | [00:03:43]–[00:04:44] |
| Feedback API | **Cloud Run** (serverless) | Speaker calls it "a serverless service that you can use in order to deploy app" | [00:12:58], [00:19:33] |
| Raw storage | **Firestore** | "web-oriented DB to collect the raw responses" | [00:12:58]–[00:13:28] |
| Analytics warehouse | **BigQuery** | Post-process + store responses for analytical queries | [00:13:28]–[00:13:58] |
| Dashboards | **Looker** | KPIs including response time per submission | [00:13:28], [00:21:37]–[00:22:07] |

## Claude Code primitives in this build (verified)

| Primitive | Where used | Transcript anchor |
|---|---|---|
| **Plan mode** | UI/UX hat — Claude proposes architecture + UI components before writing code; operator can correct before code is touched. Used for the front-end build (3 pages: landing / thanks / dashboard). Skipped intentionally for the back-end "for simplicity" | [00:09:23]–[00:09:53], [00:16:00] |
| **Subagents** | Software engineer hat — **3 parallel subagents** spun up: one for the API, one for the ingestion pipeline, one for the dashboard. Speaker calls this "like you run a team sprint" | [00:15:00]–[00:15:30], [00:16:31] |
| **MCP servers** | Two: (1) **Developer Knowledge API** MCP server (Google Cloud — gives Claude fresh GCP documentation to figure out best architecture/implementation). (2) **BigQuery MCP server** (natively supported in Google Cloud's Agent Registry). Also mentioned: (3) **MCP Toolbox for DB** — open-source MCP server with Looker integration | [00:12:28]–[00:12:58], [00:22:38]–[00:24:10] |
| **Skills** | "Google Cloud Skills" — specifically mentions a skill that **deploys to Cloud Run**, and one that **connects Cloud Run with Firestore**. Plus Claude Code's **pre-built security-review skill** (used by the security engineer hat to find + auto-fix issues + deploy) | [00:13:58]–[00:14:30], [00:18:32]–[00:19:02] |

## Setup story for Claude on Google Cloud (the "why Vertex AI" pitch)

Five enterprise reasons given (transcript [00:04:44]–[00:06:18]):

1. **Per-token billing** — no message cap; pay for what you use
2. **Provisioned throughput** — reserved capacity for production enterprise apps
3. **ADC setup** — no API keys to rotate, no env vars to set; wizard detects project/region/models
4. **Data residency** — model access via your project's policies; data stays in your project
5. **Availability + region choice** — global endpoint and regional endpoints

## Google Cloud's "Agent Platform" (transcript [00:22:38]–[00:23:40])

A recently-announced service. Contains:
- **Agent Registry** — list of MCP servers natively supported on Google Cloud, with observability features and tool documentation
- Natively-supported MCP servers shown: **Developer Knowledge** + **BigQuery** (more not enumerated in the talk)

This is the *meta-product* the talk pitches as the "official path" for connecting Claude Code to Google Cloud services.

## Code release commitment (transcript [00:22:07], [00:25:13]–[00:25:45])

Speaker stated twice: **"we are going to release the code"** — both for the feedback app itself and for the BigQuery + Looker MCP setup left as exercise. As of wiki build 2026-05-21, no public link has been located; the [companion webinar repo](https://github.com/inardini/ship-code-with-claude-on-vertex-ai-webinar) is a different artifact (confirmed in [[entity-3-companion-resources-and-speaker-context]]).

## What is NOT in the transcript

- Exact `gcloud` commands or Dockerfile contents
- Firestore schema or BigQuery DDL
- The Looker dashboard configuration (intentionally "exercise for the reader")
- The custom Skill bodies (referenced by name but content not shown)
- The exact subagent prompts (only role names: API / ingestion / dashboard)
- The specific Claude model variant used (Sonnet vs. Opus vs. Haiku — speaker says only "Claude on Vertex AI")

Those gaps survive even with transcript ingest. See updated [[entity-4-content-gaps-and-ingest-path]] for the post-transcript gap inventory.
