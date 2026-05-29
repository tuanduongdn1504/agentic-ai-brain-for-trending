# (C) entity-7 — Step-by-step build (chronological)

This entity walks the 26-minute talk in linear order, marking each moment as **demo** (live build action shown), **slide** (explanation only), or **transition** (hat-switch / framing). Anchors trace to [(C) transcript-raw.md]((C) transcript-raw.md).

## Timeline

| Time | Phase | Type | What happens |
|---|---|---|---|
| 00:00–00:36 | Intro | slide | Speaker introduction (Ivan Nardini, Google Cloud DevRel, AI/ML, partnership with Anthropic) |
| 00:36–01:06 | Audience poll | live | "How many used AI tools to code last week?" (most) → "How many used the same tool to build + deploy on Google Cloud?" (few) — sets the talk's gap-filler premise |
| 01:06–02:40 | The 5 hats framing | slide | Walks through PM → UI/UX → Software Engineer → Security Engineer → Growth Marketer; explains how Claude augments each |
| 02:40–03:43 | The Claude Code primitives | slide | Names the components: Claude Code + skills + MCP + subagents → all about to be demonstrated |
| 03:43–06:48 | "Why Claude on Vertex AI" pitch | slide | ADC setup; per-token billing; provisioned throughput; data residency; regions/availability. The "easy setup" wizard auto-detects project/region/models |
| 06:48–08:22 | **Hat 1: PM** | **demo** | Drop a hand-drawn wireframe sketch into Claude Code → Claude renders a prototype |
| 08:22–10:56 | **Hat 2: UI/UX Designer** | **demo** | Plan mode enabled. Pass PM's wireframe + (simulated) Figma design-doc. Claude proposes UI plan, operator accepts, Claude implements 3 pages: landing / thanks / dashboard |
| 10:56–11:57 | **Hat 3: Software Engineer — context** | slide | "You may not know how to deploy on Google Cloud — that's fine, you don't have to" |
| 11:57–13:58 | **Hat 3: Software Engineer — architecture** | slide | Introduces 2 Google Cloud primitives: (a) **Developer Knowledge MCP server** (fresh GCP docs to Claude) + (b) **Google Cloud Skills** (deploy-to-Cloud-Run skill, Cloud-Run+Firestore connection skill). Architecture: Cloud Run + Firestore + BigQuery + Looker |
| 13:58–15:30 | **Hat 3: Software Engineer — parallelism** | slide | 3 parallel subagents: API + ingestion + dashboard |
| 15:30–16:31 | **Hat 3: Software Engineer — execution** | **demo** | Claude designs cloud-native back end (no plan mode this time "for simplicity"). Calls the deploy skill. Spawns 3 subagents in parallel. They implement + manage testing |
| 16:31–17:32 | **Hat 4: Security Engineer — context** | slide | OWASP review + IAM service-account scoping as enterprise examples; speaker flags that bundling deploy into security-engineer role is a "strong simplification" |
| 17:32–19:33 | **Hat 4: Security Engineer — execution** | **demo** | Uses Claude Code's pre-built security-review skill. Skill finds an issue, auto-fixes, then deploys. App goes live on Cloud Run |
| 19:33–20:35 | **Live audience interaction** | **demo** | Speaker pulls up the deployed app on his laptop. Audience member rates the talk "5" out of 5. Real-time dashboard updates with new response, score, visualization |
| 20:35–21:06 | **Feedback Analyzer demo** | **demo** | "Just for fun, I built a feedback analyzer" — click button → calls Claude on Vertex AI → generates sentiment summary from collected feedback |
| 21:06–21:37 | **Hat 5: Growth Marketer — context** | slide | The dashboard had a "response time" KPI — this is the kind of data you analyze to improve the app. The lifecycle loop closes back to the PM |
| 21:37–22:38 | **Hat 5: Growth Marketer — punt** | slide | Speaker says: "for sake of time, I'm not going to demo BigQuery MCP or building a Looker dashboard." Points at: |
| 22:38–24:10 | Google Cloud Agent Platform + MCP Toolbox for DB | slide | Recently-announced Agent Platform → Agent Registry → natively-supported MCP servers (Developer Knowledge + BigQuery shown). Plus open-source **MCP Toolbox for DB** with Looker integration. "Leave as exercise" |
| 24:10–25:13 | Wrap | slide | Two takeaways: (1) Claude Code components (skills + MCP + subagents) speed up SDLC; (2) Claude on GCP is seamless |
| 25:13–25:45 | Code release commitment | slide | "Code is going to be available right after the session. Great quick start, well-maintained docs on both Google Cloud + Anthropic sides" |
| 25:45–26:21 | Q&A invite + thanks | slide | Social media point shared verbally (not captured in transcript) |

## What got demo'd live vs. talked about

**Live demo (6 distinct moments):**
1. Audience poll
2. PM → wireframe-from-sketch
3. UI/UX → 3-page front-end with plan mode
4. Software engineer → 3-subagent parallel build
5. Security engineer → security-review skill + deploy
6. Live audience interaction with deployed app (rating + feedback analyzer)

**Talked about but skipped:**
- BigQuery MCP server query demo
- Looker dashboard build with MCP Toolbox for DB
- Concrete OWASP-pattern threat modeling
- Multi-version / multi-region deployment

## Reproduction-recipe quality

The talk is a **demo with narration**, not a tutorial. Important reproduction details that a viewer cannot recover from this video alone:

| Missing detail | How to recover |
|---|---|
| Exact prompts to each hat | Wait for the promised code release (transcript [00:22:07], [00:25:13]) |
| The subagent definition files | Same — code release |
| Custom skill `SKILL.md` contents | Same — code release |
| Claude model variant selected | Check the Vertex AI wizard's default + the model pin (UI shown briefly at ~04:14) |
| `gcloud` commands for deploy | Embedded in the Cloud-Run-deploy skill (code release) |
| Firestore + BigQuery schemas | Generated by Claude — code release |
| Looker dashboard config | "Exercise for the reader" — operator builds with MCP Toolbox for DB |

The code-release artifact is the load-bearing follow-up. As of wiki build 2026-05-21, no public URL was located.

## Pacing observation

Speaker burned ~3.5 of 30 minutes on intro + Vertex-AI-setup pitch (00:00–06:48), then sprinted the 5 hats in ~14 minutes (06:48–21:06), then 5 minutes on the unfinished hat 5 + Agent Platform/MCP-Toolbox pitch, then wrap. Net **live build time ≈ 14 minutes** — comfortably under the abstract's "30 minutes" claim. The "30 minutes" framing is the marketing hook; the substantive build was ~half that.

## What is NOT in this entity

- The slides themselves (not in transcript)
- Visual UI of Claude Code during the demo (would need screen-recording analysis)
- Audience faces / room reactions beyond the "5" rating

See [[entity-8-pitfalls-and-simplifications]] for the gotchas and demo-conveniences the speaker acknowledged.
