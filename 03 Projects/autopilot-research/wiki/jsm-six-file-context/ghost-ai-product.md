# Ghost AI (a.k.a. "Ghost Arc") — the product as artifact

> The app is itself evidence: an AI-agent-built SaaS whose AI features automate the very methodology that built it. Repo: [adrianhajdin/ghost-ai](https://github.com/adrianhajdin/ghost-ai) — 240★ / 93 forks / **33 commits** / 8 PRs / **no license** (field null, no LICENSE file) / created 2026-04-27, last push 2026-05-01 (video day).

## Naming note

Repo + video say **Ghost AI**; the README intro says **"Ghost Arc is an agentic planning application"** — an unresolved naming inconsistency worth knowing when searching.

## Stack (verified from package.json + tracker Session Notes)

Next.js 16.2.4 · React 19.2.4 · TypeScript 5 · Tailwind v4 · shadcn/ui · Prisma 7.8 (+`@prisma/adapter-pg`, Postgres) · Clerk `@clerk/nextjs ^7.2.7` · Liveblocks ^3.18.5 (client/node/react/react-flow/react-ui) · `@xyflow/react` ^12.10.2 (React Flow) · Trigger.dev SDK ^4.4.4 (+react-hooks) · Vercel Blob ^2.3.3 · **AI: `@ai-sdk/google` ^3.0.65 + `ai` ^6.0.170 — Gemini only, no OpenAI/Anthropic SDK present.**

## In-product AI #1: `trigger/design-agent.ts` (387 lines, read in full)

- **Model:** `google("gemini-2.5-flash")` via Vercel AI SDK `generateText` (video starts on 2.0-flash, hits deprecation mid-video, upgrades live).
- **Tools, not JSON:** 8 `tool()` definitions with Zod schemas — `addNode, moveNode, resizeNode, updateNodeData, deleteNode, addEdge, deleteEdge, finalizeDesign`. An earlier experimental structured-output attempt (`outputObject`) failed validation on camera; the tools pattern replaced it.
- **System prompt** built dynamically: 6 node shapes, 8-color semantic palette (blue→APIs, teal→databases, orange→queues, purple→auth…), layout spacing rules (240–280px horizontal), 5–12 nodes target, left→right flow.
- **Effects to the room:** tool calls mutate **Liveblocks storage** (`LiveObject` mutations applied atomically) + `broadcastEvent("ai-status")` progress ("analyzing" → "thinking" → "complete"); presence flag `thinking:true` renders an AI-is-working indicator to all collaborators.
- **Ops:** Trigger.dev task, `retry maxAttempts: 2`, `maxDuration` inherited 3600s, default machine. Frontend subscribes via `useRealtimeRun(runId, {accessToken})` with per-run scoped public tokens (1h expiry).

## In-product AI #2: `trigger/generate-spec.ts` (150 lines)

- `schemaTask` (Zod payload: projectId, roomId, nodes, edges, chatHistory) → Gemini 2.5 Flash prompt: senior-technical-architect persona; output = Markdown spec with fixed sections (Overview / Architecture / Components / Data Flow / Technology Choices / Key Considerations).
- Output → **Vercel Blob** `specs/{projectId}/{timestamp}.md` (private) → `ProjectSpec` Prisma row → downloadable via authenticated route (401/403/404 paths verified in tracker log).
- Status transitions surfaced via Trigger.dev `metadata.set()` ("starting" → "generating" → "uploading" → "complete").

## Why background jobs (and the honest nuance)

Video: generation takes 30–60s+; API routes "have execution limits" → *"the API route is to just trigger the task and then return, while the heavy work continues in the background."* Architecture invariant: "Request handlers do not run long-lived AI work."
**Nuance (verifier):** Vercel defaults are 10–15s but `maxDuration` extends to 300s+ (and Fluid Compute to ~14 min); SSE streaming exists; Inngest et al. are alternatives. Trigger.dev (a sponsor) is a *sound* choice, not the *only* one — "essential" is overstated. The durable-run + realtime-status + retry ergonomics are the honest differentiators.

## Deployment (3 attempts, all real)

1. Build fails on npm install → **deleted `package-lock.json`** and pushed without it (expedient, not best practice — no lockfile in repo tree confirms).
2. Prisma fails on Vercel → add `"postinstall": "prisma generate"`.
3. Live. Pre-deploy: swap Liveblocks + Trigger.dev dev keys → production keys.

## Meta-loop summary

User prompt → design-agent draws the architecture on a shared canvas → humans refine → generate-spec emits a Markdown technical spec → *"feed [it] into a thinking or planning AI agent... the strongest possible starting point"* for building the app. The product operationalizes steps 1–2 of the six-file methodology (architecture design + spec writing) — the methodology, productized. See [[overview]].

## Key Takeaways

- The AI implementation is **tool-use over freeform generation** — 8 narrow tools + atomic storage mutations is the reliability pattern worth stealing for any canvas/graph agent.
- Cheap-model + tight-tools works: Gemini **Flash**, not a frontier model, powers both features.
- Realtime UX = broadcast events + presence flags, not token streaming.
- The unlicensed repo means: read for patterns, don't vendor the code ([[caveats-and-corrections]] #7).
