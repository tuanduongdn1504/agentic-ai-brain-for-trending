# (C) 3-Tier Memory + Knowledge Vault

> **Source:** README.md (lines 63-72, 246-252), CLAUDE.md (key pattern #7), `internal/vault/` + `internal/memory/` + `internal/consolidation/` + `internal/knowledgegraph/` (not source-verified yet)
> **Ingested:** 2026-04-18
> **Type:** Entity page (storage concept) — building block #2 cho goclaw

---

## One-liner

**VI:** 3-Tier Memory + Knowledge Vault là **goclaw's cognitive architecture** — memory chia 3 tầng (Working / Episodic / Semantic) với progressive loading (L0/L1/L2), cộng với Knowledge Vault (document registry + `[[wikilinks]]` + hybrid search = BM25 FTS + pgvector semantic + filesystem sync). **Meta-relevant to Storm Bear vault** — đây là Karpathy's LLM Wiki pattern **implemented as infrastructure**.

**EN:** 3-Tier Memory + Knowledge Vault is goclaw's cognitive architecture — memory layered in 3 tiers with progressive loading, plus Knowledge Vault (wikilinks + hybrid search + FS sync). Meta-relevant: this is Karpathy's LLM Wiki pattern as infrastructure — potentially the backend for Storm Bear vault at scale.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu cách goclaw maintain long-term context across sessions
- Designing memory architecture cho own agent framework
- Compare với ECC continuous-learning v2 + Storm Bear vault's LLM Wiki pattern
- **Consider deploying goclaw as Storm Bear vault's backend** (speculative but legit)
- Debug memory-related agent behavior (why does agent remember X but not Y?)

**Không cần để use goclaw cơ bản** — memory works transparently.

---

## Comparison sibling

| Concept | ECC | Superpowers | gstack | **goclaw** |
|---------|-----|-------------|--------|------------|
| Session memory | Context files | Iteration log (manual) | `/learn` skill | **Working memory (auto)** |
| Cross-session | continuous-learning v2 skill | N/A | `/learn` manages | **Episodic + Semantic tiers (auto)** |
| Knowledge base | File docs | File docs | `/learn` + memory | **Knowledge Vault với wikilinks + hybrid search** |
| Search | Basic grep | Basic grep | Basic grep | **BM25 + pgvector hybrid** |
| Progressive loading | N/A | N/A | N/A | **L0 auto-inject, L1/L2 on-demand** |
| Filesystem sync | Manual | Manual | Manual | **Auto via `internal/vault/`** |

→ **goclaw's memory system = production-grade.** Most sophisticated of 4 projects.

---

## Sub-types: 3 memory tiers

### Tier 1: Working Memory

- **Scope:** Current conversation
- **Content:** Recent messages, tool calls, tool results
- **Lifecycle:** In-memory buffer, flushed to DB at session end
- **Access pattern:** Direct, no search needed
- **Analog:** Short-term memory (human cognitive model)

### Tier 2: Episodic Memory

- **Scope:** Past sessions
- **Content:** Session summaries (not full conversation)
- **Generator:** `internal/consolidation/` episodic worker
- **Lifecycle:** Created asynchronously after session end
- **Access pattern:** `memory_search` tool (BM25 + vector)
- **Analog:** "I remember that session last week where we discussed X"

### Tier 3: Semantic Memory

- **Scope:** Knowledge graph
- **Content:** Extracted facts, entities, relationships
- **Generator:** `internal/consolidation/` semantic worker + **dreaming** worker
- **Lifecycle:** Consolidated from episodic, promoted to KG via dreaming
- **Access pattern:** `knowledge_graph_search` tool, graph traversal
- **Analog:** "I know that X is related to Y" (abstracted knowledge)

### Progressive Loading L0/L1/L2

| Level | When injected | Content |
|-------|---------------|---------|
| **L0** | **Auto, every request** | Most relevant semantic facts (via `internal/vault/`) |
| **L1** | On-demand via tool call | Search results from episodic + semantic |
| **L2** | On-demand, deeper | Full knowledge graph traversal |

→ **Layered access.** L0 cheap (always inject), L1/L2 pay-per-use.

---

## Anatomy: Knowledge Vault structure

### Storage layers

```
┌──────────────────────────────────────────┐
│  Vault (internal/vault/)                 │
│                                          │
│  Documents (with [[wikilinks]])          │
│  ├─ Bidirectional links (graph)          │
│  ├─ Full-text index (BM25)               │
│  ├─ Embedding index (pgvector)           │
│  └─ Filesystem mirror (FS sync)          │
│                                          │
│  Memory (internal/memory/)               │
│  └─ pgvector hybrid search               │
│                                          │
│  Knowledge Graph (internal/knowledgegraph/) │
│  └─ Entity + Relationship storage        │
└──────────────────────────────────────────┘
```

### Document format (inferred)

```markdown
# Document title

Body with [[wikilinks]] to other docs.

Also [[another-doc]] linked here.
```

Processed:
- Wikilinks extracted → bidirectional link graph
- Content → BM25 index
- Content → embeddings (pgvector)
- FS sync: document written to disk in parallel to DB

### Hybrid search formula (inferred)

```
final_score = α * BM25_score + β * semantic_score
```

- BM25 = lexical match (keyword-based)
- Semantic = pgvector cosine similarity
- Combined weight-tunable

→ **Balance precision (BM25) + recall (semantic).**

### Auto-injection flow

```
User message → L0 query (semantic + wikilinks) → inject top-N results → Agent Loop ContextStage
```

Per ContextStage in `internal/pipeline/`: "Ensure per-user files exist", implying L0 auto-inject trong per-user workspace.

---

## Cơ chế

### Mechanism 1: Consolidation pipeline (async)

```
Session ends → event published via DomainEventBus
                ↓
Worker pools (bounded concurrency):
  ├─ Episodic worker: session → summary
  ├─ Semantic worker: summary → KG entities
  └─ Dreaming worker: batch → synthesis promotion
                ↓
Memory stored (PostgreSQL)
```

**Dedup + retry** built into worker pool.

→ **Async = doesn't slow user-facing agent response.** Background processing.

### Mechanism 2: L0 auto-injection

ContextStage injects L0 semantic context every request. Without user asking.

Per CLAUDE.md key pattern: "3-tier memory: Working (conversation) → Episodic (session summaries) → Semantic (KG). Progressive loading L0/L1/L2 with auto-inject for L0"

→ **Always-on context.** Agent always "remembers" critical knowledge.

### Mechanism 3: Wikilinks as semantic mesh

`[[wikilinks]]` create bidirectional link graph. Useful for:
- Navigating related docs
- Discovering connected concepts
- Building knowledge mesh organically

→ **Match Storm Bear vault pattern** — wikilinks central to Obsidian-based wikis.

### Mechanism 4: Filesystem sync

`internal/vault/` syncs docs to disk. Implies:
- Docs readable outside goclaw (e.g., grep, other tools)
- Git-versionable (plain markdown files)
- User can edit files directly, changes sync back to DB

→ **"Best of both worlds":** structured storage (DB) + filesystem-native (files).

### Mechanism 5: pgvector hybrid search

PostgreSQL extension for vector similarity. Combined với FTS (PostgreSQL's built-in):
```sql
SELECT * FROM documents
WHERE to_tsvector(content) @@ plainto_tsquery($1)  -- FTS
ORDER BY (embedding <=> $2::vector)  -- pgvector distance
LIMIT 10;
```

→ **Leverages PostgreSQL entirely.** No separate vector DB (Pinecone, Weaviate, etc.) needed.

---

## Out-of-box behavior

**Default configuration:**
- 3-tier memory enabled automatically
- L0 auto-injection enabled
- Consolidation workers running (async)
- Knowledge Vault empty until user populates
- FS sync enabled

**To populate Knowledge Vault:**
1. Drop markdown files into configured vault directory
2. `internal/vault/` auto-detects + indexes (BM25 + embeddings)
3. Wikilinks parsed automatically

**Or via agent:**
- Agent's `write_file` tool writes into vault
- Vault indexer picks up changes via FS watcher

---

## Configuration knobs

| Knob | Default | Effect |
|------|---------|--------|
| `memory.enabled` | `true` | Master toggle |
| `memory.l0_inject_count` | ~5 | Top-N L0 results auto-injected |
| `memory.consolidation_workers` | 1 each tier | Bounded concurrency for workers |
| `memory.compaction_threshold` | N tokens | PruneStage memory flush trigger |
| `vault.directory` | `./vault` | Filesystem sync location |
| `vault.search_weights` | α=0.5, β=0.5 | BM25 vs semantic balance |

→ (Inferred defaults — not source-verified. Check `config.json5` schema.)

---

## Recipes

### Recipe 1: Populate vault with Storm Bear vault content

```bash
# Hypothetical — if deploying goclaw with Storm Bear vault content
cp -r "/path/to/Storm Bear vault/02 Wiki/" /app/workspace/vault/
cp -r "/path/to/Storm Bear vault/03 Published/" /app/workspace/vault/

# goclaw's vault indexer auto-picks up markdown files
# [[wikilinks]] resolved automatically
# L0 auto-inject makes agent "know" Storm Bear vault content
```

→ **Hypothetical Storm Bear → goclaw migration** path. Compatible since both use Obsidian-style wikilinks.

### Recipe 2: Debug "agent doesn't remember"

1. Check Working memory — is current session context preserved?
2. Check Episodic — did consolidation worker run? (async, may lag)
3. Check Semantic — is knowledge graph populated?
4. Check L0 auto-inject — is threshold too high (nothing injected)?

### Recipe 3: Tune hybrid search

```json5
vault: {
  search_weights: { bm25: 0.3, semantic: 0.7 }
}
```

Higher semantic → better fuzzy matches. Higher BM25 → better exact keyword matches.

→ **Domain-dependent.** Storm Bear vault (lots of bilingual content) may prefer semantic.

### Recipe 4: Force consolidation

Per doc, consolidation is async via DomainEventBus. If need immediate:
- Trigger session end manually
- Or call internal API (if exposed)

### Recipe 5: Export vault to filesystem

Already auto-synced. But if need clean export:
```bash
rsync -av /app/workspace/vault/ /backup/vault/
```

Documents are plain markdown. Portable.

---

## Advanced patterns

### Pattern: L0/L1/L2 as cost tiers

- L0: free (always inject, cheap compute)
- L1: per-call cost (tool invocation)
- L2: highest cost (deep KG traversal)

→ **Match AWS S3 storage tiers** (Standard/IA/Glacier) pattern — tier by access frequency.

### Pattern: Dreaming for synthesis

"Dreaming" worker promotes episodic → semantic. Synthesizes patterns across sessions.

→ **Inspired by human sleep consolidation.** Novel naming + honest implementation.

### Pattern: pgvector as unifying substrate

Instead of adding Pinecone/Weaviate:
- PostgreSQL already needed (multi-tenant data)
- pgvector extension adds vector search
- Hybrid search combines with PostgreSQL FTS

→ **Reduced operational complexity.** One database instead of two.

### Pattern: Filesystem as secondary representation

DB = source of truth. FS = portable mirror.

- Version control works (git-friendly)
- Grep/ripgrep works
- Users can edit externally
- Agents still query DB for hybrid search

→ **"Export-ready" design.** No data lock-in.

### Pattern: Bidirectional wikilinks as graph edges

`[[doc-a]]` in doc-b creates edge: `doc-b → doc-a`. Also maintained reverse: `doc-a has backlinks from [doc-b]`.

→ **Obsidian-compatible** + queryable from code.

---

## Combination với building blocks khác

### + 8-Stage Pipeline
ContextStage L0 auto-inject uses vault query. Every agent request reads vault.

### + Multi-Tenant Architecture
Vault is **per-tenant**. Each tenant has own vault, own memory tiers, own knowledge graph. Isolated.

### + Agent Teams
Team lead + members share team-level vault. Plus per-agent private memory.

### + Skills Runtime
Skills can use `memory_search`, `memory_get`, `knowledge_graph_search` tools. Skills enhance vault usage.

### Cross-project: + Storm Bear vault (Karpathy LLM Wiki)
**Convergent implementations.** Storm Bear = file-based, manual maintenance. goclaw = DB-backed, auto-consolidation. Both use `[[wikilinks]]` + hybrid search philosophy.

**Hypothetical integration:**
- Storm Bear's 02 Wiki/ imported as goclaw vault
- Agents can query Storm Bear knowledge via `memory_search`
- New sessions auto-augment vault via consolidation workers
- FS sync preserves file-based editing workflow

**Blocker:** CC BY-NC 4.0 license. Storm Bear coaching = commercial?

### Cross-project: + ECC continuous-learning v2
Similar goal (persist learnings across sessions). Different implementation:
- ECC: skill `continuous-learning-v2`, manual invocation
- goclaw: auto-consolidation workers, transparent

### Cross-project: + gstack `/learn`
`/learn` manages gstack's cross-session memory. Smaller scope (gstack skill-specific). goclaw = system-wide.

---

## Anti-patterns

❌ **Treat vault as just filesystem** — FS is secondary representation. DB has semantic search. Using only FS = lose capability.

❌ **Skip consolidation workers** — async is feature, not bug. Don't wait synchronously.

❌ **Hardcode L0 count high** — every request injects L0. More = more tokens per call. Tune carefully.

❌ **Mix vault across tenants** — per-tenant isolation is feature. Shared vault = privacy breach.

❌ **Query vault as raw SQL** — use provided tools (`memory_search` etc.). Bypass = miss RBAC, tenant scoping, hybrid search logic.

❌ **Assume "dreaming" worker ≠ speculative** — it's real, runs bg. Synthesizes episodic → semantic. Agent benefits next session.

❌ **Forget wikilinks are bidirectional** — `[[doc-a]]` in doc-b creates edge both ways. Breaks if doc removed without updating refs.

---

## Cross-references

- [[(C) 8-Stage Agent Pipeline]] — ContextStage uses L0 inject
- [[(C) Multi-Tenant Architecture]] — per-tenant vault isolation
- [[(C) Agent Teams and Orchestration]] — shared vault model
- [[(C) README summary]]
- [[(C) CLAUDE.md + Architecture summary]]
- Cross-project: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Rules and Memory.md` — ECC memory pattern
- Cross-vault: Storm Bear vault's LLM Wiki pattern = file-based Karpathy convergent implementation

## Citations

- README.md lines 63-67 (3-tier memory + progressive loading)
- README.md lines 246-252 (Knowledge Vault description)
- CLAUDE.md key pattern #7 (3-tier memory)
- CLAUDE.md `internal/vault/` module: "Knowledge Vault với wikilinks, hybrid search, FS sync"
- CLAUDE.md `internal/consolidation/` module: "episodic, semantic, dreaming"
- `docs/00-architecture-overview.md` `internal/vault/` reference

## TODO

- ⏸ Read `docs/06-store-data-model.md` — vault schema details
- ⏸ Read `internal/vault/` source code — confirm hybrid search implementation
- ⏸ Verify exact L0 default inject count
- ⏸ Check if goclaw can be deployed as Storm Bear vault backend (license clarity + technical feasibility)
- ⏸ Test: drop Storm Bear's `02 Wiki/` into goclaw vault dir — does it work?
