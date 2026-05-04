# (C) 29 Categories catalog summary — build-your-own-x

> Nguồn: README.md fetched via raw.githubusercontent.com 2026-04-18
> Purpose: Deep-dive vào 29 categories + characteristics per category

## TL;DR

29 primary categories + Uncategorized + Distributed Systems reference = **~30 top-level topic sections**. Each = collection of "Build your own [X]" tutorials tagged by language. Coverage span: low-level systems (OS, processor, memory) → web infra (browser, server, framework) → data (DB, search) → AI/ML (neural net, visual recognition) → creative (game, voxel, 3D) → utility (CLI, text editor). **Flat structure + language-tagged entries = max scannability.**

---

## Full 29-category list (ordered từ README)

### Systems programming cluster

| # | Category | Notes |
|---|----------|-------|
| 17 | Operating System | Classic "write OS from scratch" tutorials — Nand2Tetris, OSDev, etc. |
| 19 | Processor | CPU design, Nand2Tetris level |
| 14 | Memory Allocator | Niche (1 entry) — malloc/free implementations |
| 15 | Network Stack | TCP/IP from scratch |
| 23 | Shell | Bash-like shells — popular entry point |
| 20 | Programming Language | Compilers + interpreters (10+ entries) |
| 21 | Regex Engine | Understanding backtracking + NFA/DFA |

### Web + infrastructure cluster

| # | Category | Notes |
|---|----------|-------|
| 28 | Web Browser | Full browser from scratch (rare, ambitious) |
| 29 | Web Server | HTTP server implementations |
| 11 | Front-end Framework / Library | React/Vue reimplementations |
| 24 | Template Engine | Jinja/Mustache-like |
| 9 | Docker | Containerization from scratch |
| 8 | Database | Popular (10+ entries) — Redis, SQLite, key-value stores |
| 22 | Search Engine | Lucene-like indexes |

### Data + AI cluster

| # | Category | Notes |
|---|----------|-------|
| 2 | AI Model | Build toy LLMs or transformers (newer entries) |
| 16 | Neural Network | Classic — build from scratch with numpy |
| 26 | Visual Recognition System | Computer vision fundamentals |

### Creative + games cluster

| # | Category | Notes |
|---|----------|-------|
| 12 | Game | Tetris, Pong, Minecraft-like |
| 27 | Voxel Engine | Minecraft-style voxel rendering |
| 1 | 3D Renderer | Ray tracing, software rasterization |
| 18 | Physics Engine | Rigid body dynamics |
| 3 | Augmented Reality | Smaller category |

### Tools + utilities cluster

| # | Category | Notes |
|---|----------|-------|
| 25 | Text Editor | Vim-like, emacs-like |
| 7 | Command-Line Tool | General CLI programs |
| 13 | Git | Version control internals |
| 4 | BitTorrent Client | P2P protocol |

### Automation + agents cluster (closest to Storm Bear)

| # | Category | Notes |
|---|----------|-------|
| 6 | Bot | Chat bots, Discord bots, etc. |
| 10 | Emulator / Virtual Machine | NES, CHIP-8, etc. |

### Blockchain

| # | Category | Notes |
|---|----------|-------|
| 5 | Blockchain / Cryptocurrency | Bitcoin-like tutorials |

### Catchall

| # | Category | Notes |
|---|----------|-------|
| 30 | Uncategorized | **50+ entries** — largest section. Experimental, novel, unclassifiable. |

### Separately referenced

- **Distributed Systems** — exists but not formally in 28-primary count

---

## Category size distribution (approximate)

| Bucket | Size | Examples |
|--------|------|----------|
| **Big (10+ entries)** | Database, Programming Language, Operating System, Shell, Web Server | Popular topics với multiple language implementations |
| **Medium (3-9 entries)** | Git, Text Editor, Neural Network, Physics Engine, Template Engine | Common topics, 1-2 per major language |
| **Small (1-2 entries)** | Memory Allocator, Augmented Reality, Regex Engine | Niche or hard topics |
| **Uncategorized catchall** | 50+ entries | Everything else |

**Pattern:** Bimodal distribution — few rich categories + long tail + catchall.

## Language coverage matrix (rough patterns)

| Language | Concentrated in | Approx share |
|----------|----------------|--------------|
| **JavaScript** | Web, Game, Bot, Front-end Framework | ~30% of entries |
| **Python** | AI/Neural Network, Database, general | ~20% |
| **C** | OS, Processor, Memory, Network Stack, Programming Language | ~15% |
| **C++** | Game, 3D Renderer, Physics | ~10% |
| **Go** | CLI, DB, Web Server | ~8% |
| **Rust** | Systems programming (newer entries) | ~5% |
| Other (Java, Haskell, Elixir, etc.) | Scattered | ~12% |

**Observations:**
- **JavaScript dominates** due to web breadth
- **Python 2nd** due to AI/ML + accessibility
- **C/C++ for systems** — expected for OS, processor, memory topics
- **Rust rising** — newer entries skew Rust
- **Go for infrastructure** — DB, CLI, web server
- Non-mainstream languages present but rare

## Format characteristics per category

### Tier 1 popular (Database, Programming Language, OS, Shell)
- Multiple entries per language
- Mix of blog posts, books, video series, interactive tutorials
- Established "classic" tutorials (cited everywhere in programming)

### Tier 2 niche (Memory Allocator, Regex Engine)
- 1-2 entries, usually specific language
- Deep technical content
- Less frequent updates

### Tier 3 emerging (AI Model)
- Newer additions (post-LLM era)
- Python-dominant
- Fast-moving area, entries may age quickly

### Tier 4 catchall (Uncategorized)
- Diverse topics don't fit elsewhere
- Sometimes graduate to own category
- Experimental / novel

## Cross-category meta-patterns

### Tutorials spanning categories
- **OS + Programming Language** overlap — compilers bridge both
- **Neural Network + AI Model** overlap — distinction blurry
- **Game + Voxel Engine + 3D Renderer** cluster — creative cluster
- **Web Browser spans Front-end + HTML parser + JS engine** — super-category

### Graduation path
1. Tutorial submitted → Uncategorized
2. Similar tutorials accumulate
3. Maintainer promotes to own category when ~3-5 entries cluster
4. Category becomes canonical

### Deprecation path
1. Blog post link dies
2. Community flags broken link via issue
3. Maintainer either prunes or leaves for historical record
4. No systematic deprecation policy apparent

## What's NOT covered (gaps)

- **Mobile apps from scratch** — no iOS/Android-specific category
- **Real-time systems** — no embedded/RT category
- **Security tools** — no scanner/fuzzer/exploit category
- **Collaboration tools** — no wiki/forum/chat category
- **DevOps tooling** — no CI/CD/monitoring category

**Opportunity:** Storm Bear vault could propose these as PR categories if build-your-own-x opens to broader scope.

## Meta-observations for Storm Bear vault

### 1. Flat categorization scales if topic count stable

29 categories = manageable. If hit 100+, would need nesting. Storm Bear's 7 wikis currently flat in `03 Projects/` — sustainable até ~20-30 projects before needing nest.

### 2. Standardized format = scannability

`[**Language**: _Title_](URL)` = 3 elements consistent. Storm Bear wiki has 13-section format = richer but less scannable.

**Hybrid idea:** Storm Bear could publish "index" view of wikis in build-your-own-x format while preserving 13-section deep pages.

### 3. Catchall "Uncategorized" = staging area

build-your-own-x uses Uncategorized as intake. Promotes after critical mass.

**Vault analogy:** Storm Bear has `00 Notes/` as catchall — same pattern.

### 4. Community contribution vs solo curation

build-your-own-x = 491K stars, thousands of contributors.
Storm Bear vault = 1 curator.

**Structural difference:** build-your-own-x trades quality variance for volume. Storm Bear trades volume for consistency. Both valid.

## Cross-references

- Main positioning: [[(C) README positioning summary]]
- Governance: [[(C) Governance + Curation cluster summary]]
- Entity pages:
  - [[(C) 29 Categories Taxonomy]] (deep-dive this catalog)
  - [[(C) Storm Bear Vault — Knowledge Architecture Lessons]] (meta lessons)
