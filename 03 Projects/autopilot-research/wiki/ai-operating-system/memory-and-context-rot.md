# Memory architecture + context rot

The most-cited technical hurdle in the corpus. Simon Scrapes's 6-level taxonomy is the most-actionable framework; Ben AI's OS-Optimizer audit pattern is the cleanest hygiene practice.

## Source

- Raw: [`raw/2026-05-29-ai-operating-system-5-skills-framework.md`](../../raw/2026-05-29-ai-operating-system-5-skills-framework.md), §Trends-4

## The problem — "context rot"

Simon Scrapes: **"out of the box memory is pretty poor"** — agents suffer from **context rot**, where they forget project requirements as more data is added to a single chat. The cost is paid in two ways:

1. **Quality** — agent forgets earlier context, produces inconsistent output
2. **Tokens** — every message re-reads the full chat history; cost grows quadratically with conversation length

This is the same problem Jack Roberts addresses in [[../claude-cowork/token-and-cost-management]] via 30-45 min session-cycling, but here the corpus zooms in on the *architectural* fix rather than the *operational* habit.

## Simon Scrapes's 6 levels of memory

Memory is not a single thing — it's a stack:

| Level | Mechanism | Use case |
|---|---|---|
| 1 | Static files (`.md`) | Identity / preferences (see [[instruction-layer-markdown-files]]) |
| 2 | Session-local conversation | Ephemeral, dies at session end |
| 3 | Append-only logs | Audit trail; doesn't help retrieval |
| 4 | Categorized files (per topic) | Manual organization; agent reads as needed |
| 5 | Auto-categorized memory | Agent organizes ingestion automatically — Kenny Liao's brain-dump pattern from [[../claude-cowork/contextual-engineering]] |
| 6 | **Semantic search** | Vector embeddings + retrieval — true RAG |

Each level is more powerful + more complex. Most operators sit at levels 1-3 and creep upward as scale demands it. **Don't jump to level 6 prematurely** — corpus consensus is to bottom-up the memory stack.

## Open Viking (Fireship introduction)

Fireship's short video introduces **Open Viking** — an open-source database designed specifically to organize an agent's memory **into a file system rather than just a vector database**.

The framing is structurally significant:
- Vector DBs (Pinecone / pgvector / etc.) treat memory as opaque embeddings
- Open Viking treats memory as **structured files** the agent can navigate
- Closer to the AIOS philosophy (file-system-as-memory) than the RAG-orthodoxy

Worth flagging: Fireship's source is the **weakest** in the corpus (6 min listicle, broad-coverage). Open Viking deserves a dedicated drain to evaluate against more rigorous claims.

## Ben AI's OS Optimizer (the hygiene practice)

Ben AI introduces an **"OS Optimizer" skill** that routinely audits the Second Brain:
- **Merges duplicate information**
- **Deletes irrelevant data**
- Keeps the system performant by preventing memory bloat

Run frequency: not specified explicitly; weekly is sensible (matches the Takeaways §9 "weekly context-hygiene audits" recommendation).

The OS-Optimizer is itself a **skill that maintains skills + memory** — recursive, in the same family as Kenny Liao's nightly brain-dump from the Cowork corpus. See [[../claude-cowork/contextual-engineering]] Pattern D.

## Context-rot mitigation toolkit (consolidated)

| Tactic | Source | When to use |
|---|---|---|
| 30-45 min session cycling | Jack Roberts (Cowork sibling) | Operational habit; immediate effect |
| Progressive disclosure on skills | Simon Scrapes / Ross Mike | Structural; reduces per-turn token load |
| Lean `.md` files | Ross Mike | Structural; counter to the heavy-context orthodoxy |
| OS Optimizer audits | Ben AI | Hygiene; weekly cadence |
| Auto-categorized memory (level 5) | Simon Scrapes / Kenny Liao | When manual categorization becomes the bottleneck |
| Semantic search (level 6) | Simon Scrapes / Open Viking | Only when scale demands it |
| External DB (Open Viking) | Fireship | Production / multi-agent / cross-session retrieval |

## The unaddressed risk — memory poisoning

The corpus does NOT discuss what happens when an agent **learns incorrect information** from a misleading source and writes it to persistent memory. Specifically:

- No version control on memory files (covered in [[production-readiness-gaps]] §Version control)
- No mechanism to "unlearn" a bad update
- No audit trail showing **what the agent knew at time T**

In a production environment running for weeks/months, memory poisoning is a real attack surface. Worth a dedicated follow-up drain.

## Composition with vault state architecture

The vault's `_state/` chapter files are a real-world instance of **level 4 categorized memory** at the vault-management layer:

| Vault layer | Memory level (Simon Scrapes) |
|---|---|
| `_state/01-skill-references.md` | Level 4 — categorized by topic |
| `_state/02-pattern-library-state-history.md` | Level 3 — append-only log + level 4 hybrid |
| `_state/03a-projects-v48-v61.md` | Level 4 — categorized by version range |
| Per-project `CLAUDE.md` | Level 1 — static instruction |
| Per-wiki `(C) log.md` files | Level 3 — append-only audit trail |

The vault has explicitly chosen **levels 1-4** and rejected level 6 (no embeddings DB in use). This is consistent with the corpus's "bottom-up the memory stack" consensus.

## Key Takeaways

- **Context rot is the central memory problem** — quality degrades + tokens inflate as conversation length grows
- **Simon Scrapes's 6-level taxonomy** is the most-actionable framework; bottom-up the stack, don't jump to level 6 prematurely
- **Open Viking** is an interesting alternative to vector-DB orthodoxy (file-system-as-memory) but the corpus source on it is weak — deserves a dedicated follow-up
- **OS Optimizer audits** (Ben AI) are the cleanest hygiene practice — weekly cadence
- **Memory poisoning is an unaddressed attack surface** — no corpus speaker covers version-control of agent memory; flag for production
- **Vault `_state/` architecture** sits at levels 1-4 of the taxonomy and is consistent with corpus consensus

## Related

- [[overview]] — AIOS framing
- [[instruction-layer-markdown-files]] — level 1 of the memory stack
- [[skills-architecture-progressive-disclosure]] — token-cost defense; complementary to memory architecture
- [[production-readiness-gaps]] — version-control + memory-poisoning gaps
- [[../claude-cowork/contextual-engineering]] — Kenny Liao's brain-dump = level 5 instance
- [[../claude-cowork/token-and-cost-management]] — operational counterpart (session cycling)
