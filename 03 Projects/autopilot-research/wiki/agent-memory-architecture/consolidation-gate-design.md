# Designing the consolidation gate — the full trigger/model/operation space

## Why this page

The video's most valuable 90 seconds is the consolidation gate ("don't save twice — wait, then distill"). The deep-dive found the concept confirmed everywhere and the *parameters* different everywhere. This page is the consolidated design space, with receipts.

## The trigger axis (who fires consolidation, when)

| Trigger type | Verified example | Notes |
|---|---|---|
| **Importance-sum threshold** | Generative Agents: reflect when Σ importance of recent events ≥ 150 (~2–3×/day) — [[generative-agents-reflection]] | Salience-aware; trivial chatter never triggers |
| **Time-based** | claude.ai: memory synthesis "updated every 24 hours" — [[how-claude-memory-works]] | Predictable cost; may consolidate nothing-days |
| **Continuous / async** | ChatGPT Dreaming V3: "a single asynchronous background process… updates existing memories as circumstances change" — [[how-chatgpt-memory-works]] | Freshest; opaque cost profile |
| **Configurable frequency** | Letta sleep-time agents: frequency setting, "higher frequency = more tokens" — [[memgpt-letta-sleep-time]] | The tunable version |
| **Explicit / operator-invoked** | Anthropic Managed Agents **Dreams** (API call: 1–100 sessions/dream, `instructions` ≤4,096 chars, Opus 4.8/4.7 or Sonnet 4.6, standard token rates); the vault's `consolidate-memory` skill | Auditable; human-gated; non-destructive input→output store + reviewable diff — [[anthropic-memory-stores-and-dreaming]] |
| **Count-based ("after N chats")** | The video's teaching device | No verified production system uses a bare count; folklore "50–200 episodes" is secondary-sourced only ([[langmem-and-industry-patterns]]) |

## The model axis (who does the distilling)

- **Video**: a *cheaper* summarizer agent — valid cost logic, matches common practice (RecMem's "cheaper summarizer processes"; batch/Haiku-class summarizers).
- **Letta's inversion**: fast model on the latency-critical hot path, **stronger** model on the background path "since the latter faces no latency constraints." Consolidation is where quality errors compound (a bad fact poisons every future session) — an argument for spending MORE there.
- **Generative Agents**: same model throughout.
- Rule of thumb: **cheap for volume compression (chat logs → digests), strong for canonical-fact curation (digests → durable memory)** — a two-stage gate gets both.

## The operation axis (what consolidation actually does)

- **Append summaries** (naive) → the failure Letta names: memories go "generic and lossy after repeated refinements."
- **Reflect** (Generative Agents): questions → retrieval → insights **with evidence citations** — inference, not compression.
- **Reorganize** (Anthropic Dreams): "duplicates merged, stale or contradicted entries **replaced with the latest value**, new insights surfaced" — consolidation as garbage collection + dedup + supersession.
- **Enrich / backfill** (Anthropic Dreams, workshop-demonstrated): dreams also **add** information — backfilled dates and identifiers, new synthesis files, an index file for retrieval — under the stance "write more down; Dreaming can always remove what's no longer needed" ([[anthropic-memory-stores-and-dreaming]]). Consolidation ≠ compression here; it's re-organization toward *future-agent retrievability*.
- **Update-in-place** (Dreaming V3): "You're going to Singapore in July" → "You went to Singapore in July 2026" — tense/state maintenance, the hardest part (OpenAI's own time-sensitive accuracy was 9.4% before the rewrite).

## The destination axis

- Distilled facts land in: an always-injected dossier (ChatGPT), editable summary (claude.ai), memory files (Claude Code/API tool), core memory blocks + archival store (Letta), reflection nodes in the same stream (Generative Agents). Matches the substrate decision rule in [[rag-vector-stores-and-context-limits]].

## The vault's own gate, named

The operator already runs this whole diagram manually: session transcripts = episodic log; memory files + MEMORY.md = semantic store; `consolidate-memory` skill = explicit-trigger Dream; the 200-line MEMORY.md budget = the working-memory constraint that forces distillation. The pilot menu's C-block turns this from implicit habit into a tuned system.

## Key Takeaways

- **The gate is real; the "N conversations" number is the only fictional part.** Choose trigger by workload: importance-sum for event streams, time-based for assistants, explicit for auditability.
- **Two-stage consolidation** (cheap compressor → strong curator) reconciles the video's cost logic with Letta's quality logic.
- Steal three operations regardless of stack: **supersede-don't-append**, **merge duplicates**, **make consolidated facts cite their sources**.
