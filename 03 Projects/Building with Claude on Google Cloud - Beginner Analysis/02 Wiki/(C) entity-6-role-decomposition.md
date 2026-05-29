# (C) entity-6 — The five roles (G1 resolved)

The talk's central pedagogical device is **"wearing five hats"** — Ivan plays each SDLC role in sequence and shows what Claude Code (with skills + MCP + subagents) does for that role. This entity documents each hat with the specific affordances demonstrated. Anchors trace to [(C) transcript-raw.md]((C) transcript-raw.md).

## The team metaphor — left-to-right (transcript [00:01:06]–[00:02:40])

The speaker visualizes an enterprise feature team as five sequential roles, each handing off to the next:

```
PM ────► UI/UX Designer ────► Software Engineer ────► Security Engineer ────► Growth Marketer / Data Analyst
```

| # | Role / "hat" | Traditional responsibility | What Claude does in this demo | Transcript anchor |
|---|---|---|---|---|
| 1 | **Product Manager** | Has the idea; improves product / adds feature | Takes a **napkin sketch** drawn by PM "while drinking a coffee in San Francisco" and renders a wireframe prototype. Compresses the PM → designer back-and-forth | [00:06:48]–[00:08:22] |
| 2 | **UI/UX Designer** | Polish the prototype; design the production interface | Takes the PM's wireframe + design-doc context (simulated Figma input via MCP server). Uses **plan mode**: proposes UI components first, operator reviews, then implements all 3 pages (landing / thanks / dashboard) | [00:08:22]–[00:10:56] |
| 3 | **Software Engineer** | Build + deploy the back-end | Uses **Developer Knowledge MCP** for fresh GCP docs → designs cloud-native architecture (Cloud Run + Firestore + BigQuery + Looker). Then spawns **3 parallel subagents** (API / ingestion / dashboard) that implement in parallel + run tests | [00:10:56]–[00:16:31] |
| 4 | **Security Engineer** | Review for OWASP issues + IAM scoping; gate the release | Uses Claude Code's **pre-built security-review skill**: scans the app, finds an issue, auto-fixes, then deploys (deploy step bundled in for demo simplicity — speaker explicitly flags this as a simplification) | [00:17:02]–[00:19:33] |
| 5 | **Growth Marketer / Data Analyst** | Analyze post-launch data; close the loop back to PM | Uses **BigQuery MCP server** + **MCP Toolbox for DB** (with Looker integration) to query analytics warehouse and build dashboards. Demoed conceptually only — speaker punts the live demo "for sake of time" and leaves as exercise | [00:20:35]–[00:22:38] |

## What each role's Claude session looks like

The speaker uses Claude Code's UI (he says: "you're probably familiar with the Claude Code UI… and the CLAUDE.md") and provides "a very simple prompt" at each hat-switch. There is no MULTI-CLAUDE / multi-session orchestration — the same Claude Code instance is steered through the 5 hats sequentially by the operator. The 3 *parallel subagents* (hat 3) are subagents within that single Claude Code session, not separate sessions.

This is an important distinction for vault-relevant pattern observation: the talk does **NOT** demonstrate multi-Claude-instance orchestration; it demonstrates **role-shifting within one Claude session via prompt steering** + **subagent parallelism within one role**.

## Hand-off discipline (implicit)

Each hat passes a deliverable to the next:

| From | To | Hand-off artifact |
|---|---|---|
| PM | UI/UX | Napkin sketch (image input to Claude) |
| UI/UX | Software Engineer | Rendered wireframe + (simulated) Figma design-doc |
| Software Engineer | Security Engineer | Working code + tests, ready to deploy |
| Security Engineer | (deploy step, then) Growth Marketer | Deployed Cloud Run URL + live data flow |
| Growth Marketer | PM (loop closes) | Analytics insights from BigQuery + Looker |

The hand-offs aren't formalized in code or via any sub-agent dispatch protocol — they're conceptual stages the speaker narrates. No agent framework formalizes the role transitions.

## Why this matters as a pedagogical pattern

The "five hats" framing is the talk's *organizing trick*. It lets a 30-minute live build cover an unrealistic surface area (full SDLC) by:

1. **Compressing each role to its highest-leverage moment.** The PM doesn't do roadmapping; he draws a wireframe. The security engineer doesn't write a threat model; she runs one skill. Each hat is reduced to a 3–5 minute slice.
2. **Picking roles where Claude has a *visible* unlock.** A real team would also have a tester, an SRE, a release manager — all skipped. The chosen 5 are exactly the ones where Claude's primitives (vision input, plan mode, MCP, subagents, skills) shine.
3. **Closing the loop.** The 5th hat produces insights that feed back to the 1st hat — making the demo a microcosm of the full product lifecycle in 26 minutes.

This is a vault-relevant pattern: **role-decomposition-as-demo-organization**. May warrant its own entry in PATTERN_LIBRARY at next mini-audit if a sister demo independently uses the same structural device.

## What is NOT covered

- The QA/tester role (speaker mentions "GoCode like it also managed the testing part" at [00:16:31] — testing happens as a side-effect of the API subagent's work, not as a dedicated hat)
- An SRE / on-call role
- A release manager / project manager during sprint
- Negotiation between PM and engineering (i.e., the messy parts of real SDLC)
