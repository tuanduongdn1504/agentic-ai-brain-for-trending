# The Six-File Context System — anatomy as implemented

> Ground truth: the `context/` directory of [adrianhajdin/ghost-ai](https://github.com/adrianhajdin/ghost-ai) (fetched 2026-07-03, all six files + 3 sample feature-specs read in full). The email-gated "guide" at jsm.dev/ghost-context is a lead magnet; **the repo IS the system** — nothing is behind the gate that isn't in the repo + transcript.

## The six files

| # | File | Job | Structure (verified) | ~Tokens |
|---|------|-----|----------------------|---------|
| 1 | `project-overview.md` | Product definition | Overview → 6 numbered Goals → 10-step Core User Flow → Features by subsystem → Scope (in/out) → 6 Success Criteria | ~1,200 |
| 2 | `architecture-context.md` | System blueprint | Stack table (7 layers, each tech + its role) → System Boundaries → Storage Model → Auth/Collab coupling → AI Generation subsystems → **Invariants** (5 rules) | ~1,800 |
| 3 | `ui-context.md` | Design tokens | Dark-only theme (18 CSS color vars) → typography → radii → canvas node colors (8 pairs) / edge style / 6 shapes → component conventions | ~1,500 |
| 4 | `code-standards.md` | Implementation rules | TS strict / no `any`; `use client` only when needed; token-based Tailwind (no raw color classes); API route conventions; file organization | ~900 |
| 5 | `ai-workflow-rules.md` | Agent operating discipline | Spec-driven approach → **Scoping Rules** → When To Split → Handling Missing Requirements → Protected Components → Docs-in-sync → readiness gates | ~600 |
| 6 | `progress-tracker.md` | Memory + state machine | Current Phase/Goal → **Completed (28 feature blocks, full implementation logs)** → In Progress → Next Up → Open Questions → Architecture Decisions → Session Notes (pinned versions) | ~8–10K |

Whole system ≈ **14–15K tokens** — cheap enough to sit at the front of every session; the tracker dominates and grows.

## Reading order (AGENTS.md, verbatim mechanism)

`AGENTS.md` lists the six files 1→6 with: *"Read the following files in order before implementing or making any architectural decision"* + *"Update `context/progress-tracker.md` after each meaningful implementation change"* + if implementation changes architecture/scope/standards, **update the context file before continuing** (docs-as-master).

⚠️ This is an **instruction, not a mechanism** — nothing enforces it. The developer explicitly points the agent at files in every prompt, and the in-product AI tasks never read these files at all (verified — see [[caveats-and-corrections]] #3).

## The load-bearing rules (verified verbatim in `ai-workflow-rules.md`)

- **One feature unit or subsystem at a time.** *"Do not combine unrelated system boundaries in a single implementation step."* Video: this single rule "prevents most failures that agents cause."
- **When to split:** if a change combines UI + background task, real-time state + persistence, multiple unrelated API routes, or behavior not defined in context files. *"If a change cannot be verified end to end quickly, the scope is too broad — split it."*
- **No invention:** *"Do not invent product behavior that is not defined in the context files. If a requirement is ambiguous, resolve it in the relevant context file before implementing."*
- **Protected foundations:** never modify `components/ui/*` (shadcn) or third-party internals unless explicitly told.
- **Truth discipline:** *"Progress state must reflect the actual state of the implementation, not the intended state."*
- **Readiness gates** before the next unit: works end-to-end / no invariant violated / tracker updated.

## Invariants (architecture-context)

Non-negotiable constraints the agent must never break, e.g. *"Request handlers do not run long-lived AI work"* (→ Trigger.dev), *"project memberships must be verified before a Liveblocks token is issued"*, hybrid storage (Postgres metadata + Vercel Blob artifacts, blob URL as `canvasJsonPath` reference).

## Progress tracker as memory

- Each completed feature is a **full implementation log** (intent → design → file paths → error cases), independently parseable — an agent can resume at Feature N without re-reading N−1 histories.
- Architecture Decisions section records e.g. `middleware.ts → proxy.ts` rename (Next.js 16), dark-only theme, CSS-token approach.
- Session Notes pin exact versions (Next.js 16.2.4, React 19, Prisma 7.8.0, @trigger.dev/sdk ^4.4.4...) — agents-trained-on-old-versions insurance.
- On camera, Adrian inspects it mid-build (Feature 16) and everything done so far "is written right here" — the file is genuinely live, though "the agent updates it automatically with no human sync" is overstated (see [[caveats-and-corrections]] #6).

## How the files get written

- Not hand-typed from scratch: Adrian **converses with a planning AI** (ChatGPT/Claude/Gemini — explicitly agent-agnostic) to pressure-test the architecture, then commits distilled decisions into the files.
- `ui-context.md` generation: speak the aesthetic intent (*"dark, technical, precise, something that feels like an engineering tool"*) and let the AI propose the palette; refine by hand.
- Dictation via Wispr Flow (captions garble it as "Whisper/Wizard Flow") for long prompts.

## Assessment (what's strong / weak)

**Strong:** progress-tracker as state machine; invariants section; the When-To-Split rules (catches the classic over-scope failure); hybrid-storage clarity; per-spec "Check When Done" gates.
**Weak:** no timestamps/versioning on the five static files (staleness is invisible); `ui-context` hand-maintains 18 color vars in prose (a `colors.json`/Tailwind export would be sturdier); generic boilerplate mixed with project-specific rules in `code-standards`; no spec manifest/index for the 29 feature specs; two rule statements about shadcn components conflict (absolute vs "unless explicitly instructed").

## Relationship to our existing patterns

- The **file-structure hosting pattern** for SDD, distinct from the SDD methodology itself — sits beside cc-sdd (Storm Bear pilot #1), spec-kit, OpenSpec, GSD/gsd-2 as an independent, pedagogy-first implementation.
- vs Pocock's `CONTEXT.md` ([[../pocock-real-feature-build/ubiquitous-language-for-llms]]): one DDD glossary file vs six structural files — complementary, not competing (glossary = *language*, six files = *state + constraints*).
- vs [[../claude-code-memory-systems/_index]]: progress-tracker = curated L2/L3 memory file, Karpathy LLM-Wiki lineage.

## Key Takeaways

- Six lean files ≈ 14K tokens buy session-restart continuity, scope discipline, and drift resistance — the cost is manual curation.
- The tracker is the **only file that grows**; everything else is quasi-static constraints. That asymmetry is the design.
- The system's real enforcement is the **human's prompt discipline** (point at files every time), not the files themselves.
- Steal-ready: the invariants section, the When-To-Split rules, and version-pinned Session Notes port to any repo in an afternoon.
