# (C) Entity 3 — Code-Indexing T4 Sub-Taxonomy (3 data points, 2 axes observable)

> **Entity type:** Cross-wiki meta-pattern observation
> **Scope:** Formal sub-taxonomy observation across 3 T4 code-indexing wikis: graphify v16 (graph-based) + GitNexus v33 (graph-based + commercial) + claude-context v40 (vector-based + commercial-ecosystem-startup). 2 axes: retrieval-architecture (graph vs vector) and commercialization (OSS vs commercial-entity).
> **Pattern relevance:** Pattern #9 Multi-Axial Tier Bifurcation Resolution D at T4 / Pattern #17 variant 3 strengthening / observational meta-pattern candidate pending N=4 (2nd vector-based data point)

---

## 1. Corpus sub-taxonomy observation

### Three T4 code-indexing wikis now observable

| Wiki | Date | Stars | Retrieval architecture | Commercial axis | Governance | License |
|------|------|-------|------------------------|-----------------|------------|---------|
| **graphify v16** | 2026-04-19 | 30K | **Graph-based** (Tree-sitter + NetworkX + Leiden clustering) | Solo-OSS | Solo-light | MIT |
| **GitNexus v33** | 2026-04-23 | 28.5K | **Graph-based** (Tree-sitter + LadybugDB) | Solo + commercial entity (akonlabs.com) | Solo-light | **PolyForm Noncommercial** |
| **claude-context v40** | 2026-04-24 | 8.6K | **Vector-based** (Tree-sitter AST chunking + BM25 + dense embedding + Milvus) | Commercial-startup + Zilliz Cloud funnel | Light-distributed | MIT |

### Shared primitives (all 3)

- **Tree-sitter AST chunking** — all 3 use Tree-sitter for AST-aware code parsing at some stage
- **MCP-primary distribution** — all 3 are MCP-native for agent integration
- **Multi-language support** — all 3 support 10+ programming languages
- **OSS license as entry** — all 3 have OSS install path
- **Incremental indexing** (implementations vary)

### Divergent primitives

| Primitive | graphify v16 | GitNexus v33 | claude-context v40 |
|-----------|--------------|--------------|---------------------|
| **Retrieval** | Graph topology + clustering | Graph topology + LadybugDB + RRF | BM25 + dense vector hybrid |
| **Storage** | NetworkX in-memory + Obsidian export | LadybugDB (embedded graph + vector) | Milvus / Zilliz Cloud |
| **Embedding** | Optional (graph-first) | Native multi-vector | Primary (4 providers) |
| **Incremental** | Full rebuild | LadybugDB diff | **Merkle tree (corpus-first)** |
| **Runtime** | CLI + MCP + Obsidian | CLI + MCP + browser-WASM | MCP + npm library + VS Code + Chrome (coming) |
| **Governance** | Solo light (3 files) | Solo light (3-4 files) | Commercial-startup light-distributed (3 root + 4 per-package) |

---

## 2. Axis 1: Retrieval architecture (Graph vs Vector)

### Graph-based sub-axis (N=2)

**graphify v16 + GitNexus v33** — both build code knowledge graphs where:
- Nodes = code entities (functions / classes / modules)
- Edges = relationships (calls / imports / inheritance)
- Traversal surfaces structural-navigation patterns

**Retrieval queries favor structural questions:**
- *"What functions does `validateUser()` call?"*
- *"What modules import the `auth` module?"*
- *"What's the blast radius of modifying `RefreshToken`?"*

**Architectural advantage:** Precise structural navigation. Impact analysis. Cross-entity relationship surfacing.

**Architectural limitation:** Hard to answer fuzzy-semantic questions ("find auth logic" → graph doesn't know which function is "auth" without embedding overlay).

### Vector-based sub-axis (N=1)

**claude-context v40** — builds embedding vector index where:
- Chunks = AST-bounded code segments
- Vectors = dense embeddings + BM25 sparse vectors
- Retrieval = hybrid similarity search + RRF/fusion

**Retrieval queries favor fuzzy-semantic questions:**
- *"Find functions that handle user authentication"* (semantic intent, not exact name)
- *"Where do we process payment webhooks?"* (concept, not structure)
- *"Show me the email validation logic"* (behavior, not syntax)

**Architectural advantage:** Natural-language query. Semantic proximity. Robust to naming variation.

**Architectural limitation:** Harder to answer precise structural questions ("what calls X?") without additional tooling.

### Sub-taxonomy observation

**Neither approach dominates** — they serve different query types:
- **Graph-based for structural questions** (impact analysis, call graphs, refactoring safety)
- **Vector-based for semantic questions** (intent-driven search, concept discovery)

**Hybrid opportunity:** Future T4 code-indexing tool could combine both. graphify's Leiden clustering is topology-aware, claude-context's dense embedding is semantics-aware. A combined graph+vector architecture isn't observed yet at T4.

### Sub-taxonomy status

**N=3 observations with 2+1 axis split is BELOW meta-pattern-consolidation N=3 threshold** (which requires N=3 across 3 sub-types, not 2 sub-types). **Observation formally tracked; not registered as candidate.** Wait for 2nd vector-based data point (N=2 vector + N=2 graph = clean 2×2 split) or 3rd distinct sub-type (e.g., LSP-based, which would make 3 sub-types).

**Deferred per consolidation-forward discipline.** Register as meta-pattern candidate when N ≥ 4 with clean sub-type split.

---

## 3. Axis 2: Commercialization (OSS-pure vs commercial-entity)

### Sub-axis (N=3)

| Wiki | Commercialization mode | Commercial tier |
|------|------------------------|-----------------|
| graphify v16 | **Pure-OSS** | None |
| GitNexus v33 | **Solo + commercial entity** | akonlabs.com |
| claude-context v40 | **Commercial-startup + commercial funnel** | Zilliz Cloud (Pattern #50 N=3) |

### Observation

Code-indexing T4 shows commercial-trajectory progression:
- Pure-OSS (graphify): community-contribution only
- Solo + commercial entity (GitNexus): OSS free / commercial enterprise tier (akonlabs)
- Commercial-startup (claude-context): OSS tool + managed-infrastructure commercial tier (Zilliz Cloud)

**Pattern observation:** T4 code-indexing attracts commercial development earlier than T1 (where solo-ecosystem dominant). Reason hypothesis: vector DB or graph DB infrastructure requires commercial-tier-hosting for production scale — natural commercial-funnel opportunity.

**Pattern #31 Open-Core relationship:** GitNexus + claude-context both have commercial components but differ structurally:
- **GitNexus:** Open-Core via license (PolyForm Noncommercial = Pattern #31)
- **claude-context:** Open-Core via infrastructure funnel (MIT OSS + commercial SaaS = Pattern #50)

**Two distinct commercialization structures at T4 code-indexing.** Documents Pattern #31 vs Pattern #50 as alternative commercialization paths, now observable in same sub-taxonomy.

---

## 4. Pattern #9 Multi-Axial Tier Bifurcation at T4

### Pattern #9 recap (Resolution D leading at 60%)

> *"Most tiers (T1, T4, T5) bifurcate along multiple orthogonal axes — (corporate/solo/LLC) × (scope broad/narrow) × (scale small/medium/large/X-large) × (methodology heavy/light)."*

### T4 archetype grid post-v40 (8 archetypes)

| Archetype | Example | Retrieval | Commercial | Scale |
|-----------|---------|-----------|------------|-------|
| T4a Corporate-broad-official | gws v13 | Rest API tooling | Google-backed | 25K |
| T4b Solo-narrow | notebooklm-py v7 | API wrapper | None | ~300 |
| T4c Solo-broad-local | graphify v16 | **Graph** | None | 30K |
| T4d Solo-broad-external-regional | TrendRadar v19 | News aggregator | CN donation | 52K |
| T4e Corporate-narrow-utility | markitdown v28 | File conversion | Microsoft | 114K |
| T4f Solo-enterprise-scale | crawl4ai v29 | Web crawler | Solo-sponsor | 64K |
| T4g Solo-student-with-commercial | GitNexus v33 | **Graph** | akonlabs.com | 28.5K |
| **T4h Commercial-ecosystem-startup** | **claude-context v40** | **Vector** | **Zilliz Cloud (Pattern #50 N=3)** | **8.6K** |

**8 distinct T4 archetypes.** Pattern #9 Resolution D now observable at T4 with 8-way diversity. **Multi-axial bifurcation structurally unambiguous at T4** — every cell in orthogonal grid occupied or plausibly fillable.

### Pattern #9 post-v40 probability update (speculative)

- Resolution A (2-way split): 25%
- Resolution B (3-way): 10%
- Resolution C (subsumed into D): 15%
- **Resolution D (multi-axial): 50%+** (8-way at T4 + 13-way at T1 + 5-way at T5 = corpus-wide multi-axial norm)

Audit-level promotion from candidate to confirmed-general-law deferred; already observationally confirmed at individual tiers.

---

## 5. Commercialization correlation observation

### Pattern #17 variant 3 + Pattern #50 co-occurrence

**Observation:** 2 of 3 code-indexing T4 wikis have commercial-entity structure:
- GitNexus v33 + akonlabs (solo-student + independent entity)
- claude-context v40 + Zilliz (commercial-startup ecosystem)

**graphify v16 is pure-OSS outlier.** Commercial-entity is majority at N=3 code-indexing T4.

**Hypothesis:** Code-indexing T4 bridges have natural infrastructure-commercial affinity (vector DB hosting + graph DB hosting require commercial tier for production scale).

**Falsifiable prediction:** Future T4 code-indexing wikis will continue commercial-majority trend. If N=5+ code-indexing T4 observations and commercial-rate drops below 50%, falsify hypothesis.

---

## 6. Cross-runtime landscape

### Emerging T4 code-indexing landscape (cited as peers in claude-context FAQ)

| Tool | Provider | Approach | Corpus status |
|------|----------|----------|---------------|
| **graphify** | Solo (safishamsi) | Graph-based OSS | v16 wiki |
| **GitNexus** | Solo+akonlabs | Graph + commercial | v33 wiki |
| **claude-context** | Zilliz (commercial-startup) | Vector + commercial funnel | v40 wiki |
| **Serena** | (external org) | Claim: semantic refactoring | Not in corpus |
| **Context7** | Upstash | Library docs MCP | Not in corpus |
| **DeepWiki** | Cognition | AI-generated repo wiki | Integration-observed at v34, v40 |

**Corpus coverage:** 3 of 6 currently-observable tools are wikis'd. Serena + Context7 + DeepWiki are peer products named in claude-context FAQ + Storm Bear meta-observation. At N=6 with 3 unwiki'd, sub-taxonomy already has statistical-body for observation.

---

## 7. Tree-sitter AST universality (cross-wiki primitive)

**All 3 code-indexing T4 wikis use Tree-sitter** (graphify + GitNexus + claude-context). Observational convergence at AST-chunking layer.

**Other Tree-sitter uses in corpus:**
- spec-kit v17 (potential)
- Various T1 skills

**Tree-sitter as de-facto AST parser standard in corpus.** Not a new pattern candidate (below novelty threshold; widely adopted).

---

## 8. Merkle-tree incremental-indexing corpus-first

claude-context v40 introduces Merkle-tree incremental-indexing as architectural primitive:
- graphify v16: full rebuild
- GitNexus v33: LadybugDB diff (platform-specific)
- claude-context v40: **Merkle-tree content-addressable incremental** (corpus-first)

**Novel architectural pattern candidate?** Single observation (N=1). Deferred pending N=2.

**Merkle-tree primitive advantages:**
- Content-addressable — same content → same hash → no re-index
- Subtree skipping — only hash-changed subtrees trigger re-embed
- Cross-language universality — hash-based, not language-specific

**If 2nd code-indexing T4 wiki adopts Merkle-tree incremental, register as candidate.** Until then, corpus-first architectural-detail notation.

---

## 9. Pattern Library summary (Entity 3)

| Pattern | Observation type | Registration |
|---------|------------------|--------------|
| **#9 Multi-Axial Tier Bifurcation** | T4 8-way strengthening; Resolution D observable | Existing pattern strengthening |
| **#17 variant 3 Commercial-startup** | 8th+ data point (Zilliz commercial-startup ecosystem) | Existing pattern strengthening |
| **#31 Open-Core relationship** | Alternative commercial-structure to #50 | Existing pattern cross-reference |
| **#50 Commercial-Funnel Companion** | N=3 default-criterion first T4 | Existing pattern strengthening (formal-statement update proposed) |
| Code-indexing T4 sub-taxonomy (graph vs vector) | N=2 graph + N=1 vector (N=3 total, 2-axis) | **Deferred** pending N=4 with 2nd vector data point |
| Merkle-tree incremental-indexing | N=1 corpus-first | **Deferred** pending N=2 |
| Commercial-startup governance-depth 3-tier refinement | N=2 commercial-startup (VoltAgent + Zilliz) | **Observational** pending N=3 commercial-startup |

**Target outcome achieved: 0 new active candidates registered.** All observations tracked within existing patterns or deferred per consolidation-forward discipline.

---

## 10. Cross-references

- **graphify v16** — T4c graph-based code indexing; primary code-indexing sibling
- **GitNexus v33** — T4g graph-based + commercial; secondary code-indexing sibling
- **Pattern #9 Multi-Axial Tier Bifurcation** — Resolution D at T4 8-way
- **Pattern #17 variant 3 commercial-startup** — strengthening
- **Pattern #31 Open-Core Commercial Entity** — alternative commercial path
- **Pattern #50 Commercial-Funnel Companion** — N=3 default-criterion first T4
- **Serena / Context7** — external code-indexing peers (not in corpus)
- **DeepWiki** — wiki-generation peer (integrated, not wiki'd)

---

## 11. Future-proofing: what gets observed at N=4+

**If 4th T4 code-indexing wiki emerges:**

Possible sub-taxonomy completions:
1. **N=2 vector-based** (e.g., Cursor built-in indexer wiki'd, or another Zilliz-ecosystem product) → register as meta-pattern at N=4 with 2×2 sub-taxonomy
2. **3rd sub-type (LSP-based)** (e.g., Serena if it's LSP-native) → N=3 with 3 sub-types = meta-pattern-at-N=3-consolidation eligible
3. **Hybrid sub-type** (graph + vector combined) → new axis introduced

**Observation watch: T4 code-indexing is active sub-taxonomy zone.** Likely to resolve into formal meta-pattern within 5-10 corpus wikis.

---

## 12. Summary

Code-indexing T4 sub-taxonomy emerges with 3 data points at v40 (graphify v16 + GitNexus v33 + claude-context v40). **2 axes observable:** (1) retrieval architecture (graph-based N=2 + vector-based N=1); (2) commercialization (pure-OSS + solo+commercial-entity + commercial-startup-ecosystem). **All 3 use Tree-sitter** (AST-chunking convergence). **2 of 3 have commercial-entity structure** (commercial-trajectory majority hypothesis). **Merkle-tree incremental-indexing** corpus-first architectural primitive at claude-context. **Pattern #9 Multi-Axial Tier Bifurcation at T4 now 8-way** (8 archetypes including new T4h commercial-ecosystem-startup-vector-MCP-native). **Pattern #50 N=3 default-criterion first T4 data point** with cross-tier validation beyond aggregator-genre. **Formal meta-pattern registration deferred** pending N=4 with clean sub-type split per consolidation-forward discipline. **Sub-taxonomy observation zone active** — likely to resolve within v41-v50 as 2nd vector or 3rd sub-type observation accumulates.
