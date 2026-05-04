# (C) 29 Categories Taxonomy

> Entity page — Catalog concept
> Sources: README catalog + cluster analysis
> Format: 13-section canonical

## 1. What is it / Nó là gì

**29 Categories Taxonomy** = flat categorization build-your-own-x uses để organize hundreds of programming tutorials. Mỗi category = 1 topic (Database, OS, Shell, etc.) chứa list of language-tagged tutorials. **No nesting.** Plus Uncategorized catchall + Distributed Systems separately referenced.

## 2. Why it matters / Sao quan trọng

**Flat taxonomies scale differently from hierarchical:**

### Flat (build-your-own-x model)
- **Max scannability** — TOC lists all 29 categories
- **Easy contribution** — contributor picks 1 category, submits
- **Easy discovery** — user Ctrl+F for topic
- **Limits:** ~20-30 categories sustainable; beyond that, user overwhelmed

### Hierarchical (common alternative)
- **More organized** — group related categories (Systems → OS/Shell/Processor)
- **More clicks** to find content
- **Harder contribution** — contributor navigates hierarchy
- **Scales higher** — hundreds of sub-categories possible

**build-your-own-x chose flat deliberately.** Trade-off: simplicity over precision.

## 3. The 29 categories (grouped for understanding)

### Systems & low-level (7)
OS, Processor, Memory Allocator, Network Stack, Shell, Programming Language, Regex Engine

### Web & data infra (7)
Web Browser, Web Server, Front-end Framework, Template Engine, Docker, Database, Search Engine

### AI & perception (3)
AI Model, Neural Network, Visual Recognition

### Creative & graphics (5)
Game, Voxel Engine, 3D Renderer, Physics Engine, Augmented Reality

### Developer tools (4)
Text Editor, Command-Line Tool, Git, BitTorrent Client

### Automation & novelty (2)
Bot, Emulator / VM

### Economics (1)
Blockchain / Cryptocurrency

### Catchall (1)
Uncategorized (50+ entries)

**Total structured: 29 primary + 1 Uncategorized + Distributed Systems section.**

## 4. Taxonomy design decisions (observable)

### Decision: Flat over nested
Result: 29 categories all siblings. User sees everything.

### Decision: Single-word category names
"Database" not "Relational Database Systems". Keeps TOC clean.

### Decision: Language-tagged entries (not per-language categories)
Not "Database-in-Python" + "Database-in-C". Instead "Database" contains both. Reduces category explosion.

### Decision: Uncategorized as staging
New topics → Uncategorized → graduate to own category if accumulate.

### Decision: Category count frozen near 30
No new categories added in recent years. Stability over comprehensiveness.

## 5. Category size distribution

From Phase 0 analysis:

| Tier | Categories | Entry count |
|------|-----------|-------------|
| Large | Database, Programming Language, Operating System, Shell | 10+ per category |
| Medium | Git, Text Editor, Neural Network, Game, Web Server | 3-9 per category |
| Small | Memory Allocator, Augmented Reality, Regex Engine | 1-2 per category |
| Catchall | Uncategorized | 50+ entries |

**Pattern:** Power law — few categories rich, many sparse. Uncategorized catches the long tail.

## 6. Graduation + pruning dynamics

### How category graduates from Uncategorized
1. Similar tutorials accumulate trong Uncategorized
2. Community reaches consensus (PR comments, reactions)
3. Maintainer promotes to own category
4. Tutorials move; Uncategorized lighter

### How category prunes (rare)
- Category with 0-1 entries considered for removal
- But historical entries preserved
- Rarely observed in public history

### How entries expire
- Link dies (blog deleted, domain expires)
- Community flags broken link via issue
- Maintainer either replaces with archive.org OR removes
- **No systematic pipeline** — tribal knowledge + occasional audits

## 7. Language distribution across categories

### JavaScript
- Most frequent (~30% of entries)
- Dominates: Web Browser, Web Server, Front-end Framework, Bot, Game
- Weak in: OS, Memory, Processor (systems)

### Python
- Strong in: AI Model, Neural Network, Database, Shell (pytutor patterns)
- Weak in: Game (performance), Voxel Engine, 3D Renderer

### C
- Dominates: OS, Processor, Memory Allocator, Programming Language (compilers)
- Rare in: Front-end, Bot, AI

### Rust
- Rising across categories, especially new entries
- Common in: OS (newer), Git, Database (recent tutorials)

### Go
- Concentrated: Database, CLI, Web Server
- Rare in: Game, Graphics

### Specialty languages
- Haskell (Programming Language category — compiler writing)
- Elixir (Distributed Systems, Web Server)
- Lua (Game, Programming Language)

## 8. Trade-offs / Limitations

### Strengths
- **Scannability** — full TOC in single view
- **Newcomer-friendly** — 29 topics easy to grok
- **Contribution-friendly** — pick category + submit
- **No learning curve** — category names self-explanatory

### Weaknesses
- **Imprecise grouping** — "Game" covers 2D indie + AAA + board games
- **No topic depth hierarchy** — Database + SQLite can't be separated
- **Cross-category entries forced to pick one** — compiler might fit Programming Language + OS
- **Uncategorized accumulates noise** — 50+ entries hard to browse
- **No progressive disclosure** — user sees everything (blessing and curse)

## 9. Comparison to sibling wiki taxonomies

### Storm Bear 4-tier agent taxonomy (v7)
| Aspect | build-your-own-x 29-flat | Storm Bear 4-tier |
|--------|--------------------------|-------------------|
| Structure | Flat | Hierarchical (tier + entrant) |
| Categories | 29 | 4 tiers, ~7 entrants |
| User journey | Ctrl+F | Tier → entrant |
| Scale limit | ~30 categories | Unlimited (tiers accommodate growth) |
| Authority | Community-consensus | Curator-authored |

**Trade-off:** build-your-own-x optimizes for browsing; Storm Bear optimizes for decision-making.

### Academic taxonomies (ACM CCS, Wikipedia)
- Deep hierarchies (thousands of categories)
- Strict inclusion criteria
- Expert-curated
- build-your-own-x is **casual equivalent** — broader scope but looser rigor

## 10. Common pitfalls

### For contributors
1. **Putting entry in wrong category** — submit to most specific fit
2. **Creating new category without accumulation** — maintainer will reject; submit to Uncategorized first
3. **Duplicate entry** — search README before submitting
4. **Malformed format** — strict `[**Language**: _Title_](URL)` required

### For users
1. **Ctrl+F misses variants** — "DB" won't find "Database"
2. **Obvious categories missing** — e.g., no "iOS App"; look in Uncategorized
3. **Treating entries as equal quality** — wide variance
4. **Assuming links current** — some 2015 entries outdated

### For curators
1. **Premature category creation** — dilutes existing structure
2. **Entry proliferation** — bar for inclusion lowered = quality drops
3. **Review neglect** — PR backlog discourages contributors
4. **Spam bypass** — malicious PR's linking to SEO farms

## 11. When NOT to use flat taxonomy

- **Many thousands of entries** — need hierarchy or search
- **Strict expertise areas** — medicine/law require ACM-level precision
- **Fast-changing field** — flat can't absorb rapid category births
- **Internal enterprise use** — permissions + access need structure

## 12. Storm Bear vault relevance

### Storm Bear's own taxonomy evolution

| Version | Structure | Trigger |
|---------|-----------|---------|
| v1-v3 | Implicit (project folders) | N=1-3 small corpus |
| v4 | 2-tier (T1 assistant / T2 service) | N=4 adjacent-domain |
| v6 | 3-tier (+ T3 education) | N=6 different-domain |
| v7 | 4-tier (+ T4 bridge with orthogonality) | N=7 different-domain |
| Potential v8 | Multi-axis? | N=8+ if pattern breaks |

**Observation:** Storm Bear chose **hierarchy over flat**. build-your-own-x chose **flat over hierarchy**. Both valid; different optimization.

### Cross-vault lesson
- Storm Bear could publish **flat index** of 7 wikis in build-your-own-x style as public-facing aggregator
- Internally retain 4-tier taxonomy for decision-making
- **Dual presentation** — flat for scannability, tier for structure

### Specific Storm Bear categories (hypothetical flat version)
If Storm Bear aggregated 7 wikis using build-your-own-x flat style:

```markdown
### Agent Frameworks — Assistant Tier
* [**TS**: _Everything Claude Code by affaan-m_](URL)
* [**TS**: _Superpowers by obra_](URL)
* [**TS**: _gstack by garrytan_](URL)
* [**TS**: _GSD by gsd-build_](URL)

### Agent Platforms — Service Tier
* [**Go**: _goclaw by nextlevelbuilder_](URL)

### AI Agent Education
* [**Curriculum**: _ai-agents-for-beginners by Microsoft_](URL)

### Agent Bridges (External Services)
* [**Python**: _notebooklm-py for Google NotebookLM_](URL)
```

→ **Concise. Scannable. Would work.** Published version of Storm Bear could follow this pattern.

## 13. References / Nguồn

- Source: [[(C) README positioning summary]] (29 category list) + [[(C) 29 Categories catalog summary]] (deep-dive)
- Related entities:
  - [[(C) Feynman Philosophy Applied to Learning]]
  - [[(C) Curation Model]]
  - [[(C) Storm Bear Vault — Knowledge Architecture Lessons]]
- External references:
  - Awesome-X pattern (similar flat structure)
  - ACM CCS (hierarchical contrast)
  - Storm Bear taxonomy v7 4-tier với orthogonality
