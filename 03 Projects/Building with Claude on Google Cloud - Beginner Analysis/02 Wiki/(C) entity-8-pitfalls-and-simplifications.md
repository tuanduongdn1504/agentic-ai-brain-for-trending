# (C) entity-8 — Pitfalls, simplifications, and what the demo hides

Demos are not production. This entity catalogs the *honest acknowledgments* the speaker made about demo simplifications, plus the *unspoken* gaps a viewer should know before treating the talk as a reproduction recipe. Anchors trace to [(C) transcript-raw.md]((C) transcript-raw.md).

## Speaker-acknowledged simplifications (explicit)

| # | Simplification | Quote / anchor | Implication |
|---|---|---|---|
| S1 | **Security engineer also deploys** | "this representation is a strong simplification… we are letting the security engineer not only to approve if the app is secure enough to be deployed, but it will also deploy the app in this case" — [00:18:02] | In real enterprise SDLC, deploy is a separate role (release engineer / SRE). Bundling deploy into the security review is demo convenience, not a recommended pattern. |
| S2 | **Plan mode skipped on back end** | "In this case, I could use again the plan mode, but for simplicity I didn't" — [00:16:00] | Speaker promotes plan mode for UI design but admits skipping it for back-end design under time pressure. Production teams probably want plan mode for the more consequential layer. |
| S3 | **Hat 5 not demoed live** | "for the sake of time, I'm not going to demo how to use an MCP server to query BigQuery or building a dashboard… I leave you this as an exercise" — [00:22:07], [00:24:10] | The full "analytics loop closure" — arguably the most important business outcome — is shown only conceptually. Reader has to assemble BigQuery MCP + MCP Toolbox for DB + Looker themselves. |
| S4 | **Figma input simulated** | "in this case, I'm simulating the receiving some instruction from Figma using a design doc" — [00:09:53] | The real Figma MCP integration isn't shown; a static design-doc stand-in is used. Production reproduction would need to verify the actual Figma MCP server's behavior. |
| S5 | **OWASP review depth** | "these are just a couple of examples of what you want to consider in a phase like this one" — [00:18:02] | The security-review skill is shown finding "a possible issue" and "automatically fixed it" — depth of the review is not characterized. Pretty / generic / one-issue-finder. |

## Unspoken gaps (no acknowledgment but real)

| # | Gap | Why it matters |
|---|---|---|
| U1 | **No prompt visibility** | The "very simple prompt" given at each hat is referenced but never shown on screen long enough to read. Reproduction requires either watching the screen-share carefully or waiting for the code release. |
| U2 | **No CLAUDE.md contents shown** | Speaker mentions "the CLAUDE.md" exists ([00:07:50]) but never shows it. CLAUDE.md is the load-bearing context file — without seeing it, viewer cannot tell what context Claude had at each hat. |
| U3 | **No subagent definition shown** | Speaker says "we are going to spin up three different sub agents" — does not show the `agents/api-builder.md` or equivalent files. Subagent design is the hardest part to get right; talk treats it as fait accompli. |
| U4 | **No skill contents shown** | "We release a simple skill that enables Claude to deploy on Cloud Run" — does not show `SKILL.md` body. Skills are usually < 1 page each but the *what they tell the model* is the IP. |
| U5 | **No failure modes shown** | Every demo step succeeds. No retry, no rollback, no "Claude went down a wrong path." Production reproduction will hit failures the talk has not prepared the viewer for. |
| U6 | **Cost not addressed** | A 26-min live build with Sonnet/Opus + multi-subagent parallelism + Vertex AI per-token billing has a real cost. Talk mentions per-token as a positive (no message cap) but does not quantify what this demo cost. |
| U7 | **Region/latency not addressed** | Speaker mentions "global endpoint vs regional endpoint" choice but doesn't say which the demo used. Latency could matter for the live audience-interaction segment. |
| U8 | **No version pinning narrative** | Claude version + skills + MCP server versions all evolve weekly. The demo runs against a snapshot. A viewer reproducing this six months later will get different behavior. |
| U9 | **The audience "5" rating is unverified** | The audience interaction at [00:20:04] is unauthenticated form input by one anonymous audience member. The dashboard updates in real-time, but this is also exactly how an audience member could spam-rate or rate-bomb a live demo. Speaker did not address auth or rate limiting. |
| U10 | **The feedback analyzer is unsupervised LLM** | "Just for fun, I built a feedback analyzer" — calls Claude on Vertex AI to summarize user-submitted text. No mention of prompt injection defenses, no output validation. In production, this is a meaningful attack surface. |

## Where the demo's "30 minutes" framing breaks

Per [[entity-7-step-by-step-build]], the *substantive live build* takes ~14 minutes of the 26-minute talk (intro + setup pitch ~6.5 min; wrap + Agent-Platform pitch ~5 min). The "30 minutes" of the session abstract is the *session length budget*, not the build time. Reproducing the *build itself* from scratch is plausibly faster than 30 minutes given the pre-built skills and MCP servers — but reproducing the *understanding* to know what to type at each hat takes longer.

## The honest reproduction-readiness verdict

The talk is excellent **pedagogy** ("here's what's possible with Claude Code + GCP, demonstrated"). It is weak as a **reproduction recipe** until the promised code release lands. The pedagogical structure (5 hats, Claude primitives one per hat) is reusable as a *teaching device* even without the code.

For Storm Bear pilot purposes:
- **Concept stack is solid** — subagents + MCP + Skills as Anthropic-blessed composition pattern, validated by Google Cloud DevRel in production-shape demo
- **Specific GCP services chosen** (Cloud Run + Firestore + BigQuery + Looker) are reasonable defaults for a small enterprise app
- **The Developer Knowledge MCP server + Google Cloud Skills** are the load-bearing GCP-native conveniences; missing them puts you back at writing prompts that include `gcloud` commands by hand
- **Code release is the unlock** — without it, this is a watch-and-learn artifact, not a clone-and-modify starting point

## Vault state implications

This subject:
- Stays out-of-typology (not T1-T5; it's a talk, not a product)
- Does **not** produce Pattern Library state-block accumulation under routine v2.2
- Does produce 1 candidate pattern observation: **"role-decomposition as live-demo organization"** (5 hats — sequential, each compressed to a single highest-leverage Claude affordance). At N=1 this is just an observation, not a pattern. Worth flagging in case a sister demo independently uses the same device.
- Reinforces the cross-corpus theme: skill + MCP + subagent as the Anthropic-blessed triad, now with first-party Google Cloud convenience layer (Developer Knowledge MCP + Google Cloud Skills + Agent Registry)
