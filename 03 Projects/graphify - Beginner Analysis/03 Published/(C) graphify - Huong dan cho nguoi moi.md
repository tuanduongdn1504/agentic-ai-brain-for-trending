# (C) graphify — Hướng dẫn cho người mới / Beginner's Guide

> **Repo:** [safishamsi/graphify](https://github.com/safishamsi/graphify) — 30K ⭐, 3.3K forks, MIT, v0.4.23
> **Tagline:** *"AI coding assistant skill. Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph."*
> **Wiki:** `(C) index` — 16th LLM Wiki in Storm Bear corpus
> **Audience:** VN developers + Scrum coaches + researchers with messy folders

---

## Part 1 — graphify là gì? / What is graphify?

### 🇻🇳 Tiếng Việt

**graphify** là **một skill cho AI coding assistant** (Claude Code / Codex / Cursor / 12 platforms khác). Gõ `/graphify .` trong coding assistant, graphify sẽ:

1. Đọc tất cả file trong folder hiện tại (code, PDF, ảnh, video, note)
2. Extract concepts + relationships thành **knowledge graph**
3. Output interactive HTML + Obsidian vault + Wikipedia-style wiki + JSON + SVG

**Kết quả:** Bạn query knowledge graph thay vì re-read raw files. **71.5× ít tokens hơn** trên corpus 52 files mixed.

**Karpathy inspiration verbatim:** *"Andrej Karpathy keeps a `/raw` folder where he drops papers, tweets, screenshots, and notes. graphify is the answer to that problem."*

→ graphify giải quyết **bài toán Karpathy /raw folder** — folder chứa everything cần extract structure.

### 🇬🇧 English

**graphify** is **an AI coding assistant skill**. Invoke `/graphify .` in any of 15 supported platforms and graphify reads your folder, extracts a knowledge graph, and outputs multiple queryable formats.

Built to solve Karpathy's `/raw` folder problem — an ever-growing directory of papers, tweets, screenshots, and notes that needs structure.

**71.5× token reduction** on 52-file mixed corpus.

---

## Part 2 — Tại sao đáng chú ý? / Why it matters

### Corpus-first signals

graphify ranks **5th-largest** in Storm Bear corpus (30K ⭐, behind build-your-own-x 491K, autoresearch 74K, paperclip 55.9K, BMAD 45K).

| Signal | graphify | Corpus context |
|--------|----------|----------------|
| **15 platform install targets** | ✅ | **Broadest in corpus** |
| **CJK-trio README** (en + ja + ko + zh) | ✅ | **First in corpus** |
| **MCP server built-in** | ✅ | **First as first-class output** |
| **Graph-topology clustering, no embeddings** | ✅ | **Novel architecture** |
| **Karpathy explicit inspiration** | ✅ | **2nd Karpathy-linked wiki** |
| **Tree-sitter 25 languages** | ✅ | **Broadest language support** |
| **71.5× token reduction** | ✅ | **3rd research-style benchmark** |
| **Solo-maintainer at 30K stars** | ✅ | **Scale outlier for solo** |

### Tier 4 "Agent-as-bridge" extension

graphify = **Tier 4 N=3 entrant** (with gws v13 + notebooklm-py v7). Unique because bridges **local filesystem** not external service.

→ Xem `(C) T4 3-way Extension + Pattern 9 Test + Storm Bear.md`.

---

## Part 3 — Cài đặt / Installation

### 🇻🇳 Quick install (Claude Code)

```bash
# Install from PyPI
pip install graphifyy        # Note: double-y on PyPI

# Install skill into Claude Code
graphify install

# First run on current folder
/graphify .
```

### 🇬🇧 Install matrix (15 platforms)

Pick your platform:

```bash
pip install graphifyy

# Then one of:
graphify claude install       # Claude Code
graphify codex install        # OpenAI Codex
graphify cursor install       # Cursor
graphify copilot install      # GitHub Copilot CLI
graphify gemini install       # Gemini CLI
graphify aider install        # Aider
graphify openclaw install     # OpenClaw
graphify hermes install       # Hermes
# ... or just `graphify install` to auto-detect
```

### System requirements

- Python 3.10+
- Claude API key (for PDF/image/video extraction on first run)
- Optional: GPU for faster-whisper audio transcription

---

## Part 4 — Cách dùng cơ bản / Basic usage

### 🇻🇳 Kịch bản: Storm Bear vault

```bash
cd "/Users/Cvtot/KJ OS Template"
/graphify . --obsidian --wiki
```

Output:
```
graphify-out/
├── graph.html          # Interactive visualization
├── graph.json          # Canonical knowledge graph
├── GRAPH_REPORT.md     # Markdown summary
├── obsidian/           # Obsidian-vault-ready markdown
└── wiki/               # Wikipedia-style articles
    └── index.md
```

Mở `graph.html` → thấy network graph với communities (tier clusters) + god nodes (Karpathy, OpenClaw, Pattern #9).

### 🇬🇧 Key commands

```bash
/graphify                          # Current directory
/graphify ./path                   # Specific folder
/graphify ./path --mode deep       # Aggressive inference
/graphify ./path --update          # Incremental re-extraction
/graphify ./path --watch           # Auto-sync on changes
/graphify ./path --obsidian        # Export Obsidian vault
/graphify ./path --wiki            # Generate Wikipedia-style articles

# URL fetching
/graphify add https://arxiv.org/abs/1706.03762   # Transformer paper

# Queries
/graphify query "How does attention work?"
/graphify path "Attention" "Transformer"
/graphify explain "MultiHeadAttention"
```

---

## Part 5 — Confidence taxonomy / Phân loại độ tin cậy

graphify **label mỗi edge** với 3 mức:

| Level | Meaning | Ví dụ |
|-------|---------|-------|
| **EXTRACTED** | Explicit in source | `function foo()` calls `bar()` — found directly |
| **INFERRED** | LLM deduction | This class implements auth pattern — reasoning |
| **AMBIGUOUS** | Uncertain | Vision detects partial text, flagged for review |

**Ý nghĩa:** graphify **trung thực** về what was found vs guessed. Agents querying graphify weight EXTRACTED > INFERRED khi reasoning.

Đây là **first corpus framework** có epistemic confidence ở edge level.

---

## Part 6 — Benchmarks / Con số thực nghiệm

| Corpus | Files | Token reduction |
|--------|-------|-----------------|
| Karpathy repos + 5 papers + 4 images | 52 | **71.5×** |
| graphify source + Transformer paper | 4 | 5.4× |
| httpx synthetic library | 6 | ~1× |

**Insight:** 6 files fits in context window anyway → graph value = structural clarity, not compression. But scales dramatically past ~10 files.

**Corpus context:** graphify is 3rd framework with research-style benchmark (codymaster SkillsBench +18.6pp; autoresearch val_bpb).

---

## Part 7 — Kiến trúc / Architecture

### Pipeline (7 stages)

```
detect() → extract() → build_graph() → cluster() → analyze() → report() → export()
```

### Stack

- **tree-sitter** — AST parsing (25 languages, deterministic, no LLM)
- **Claude API** — PDF subagent + vision for images
- **faster-whisper** — local audio/video transcription
- **NetworkX** — graph construction
- **graspologic (Leiden)** — community detection
- **vis.js** — interactive HTML rendering

### Why no embeddings? / Tại sao không dùng embeddings?

**Design choice:** graph-topology clustering instead of vector similarity.

**Tradeoffs:**
- ✅ Interpretable (edges visible)
- ✅ Deterministic (Leiden converges)
- ✅ No vector DB infra
- ❌ Dependent on extraction quality
- ❌ Structural bias over semantic

**Contrast:** multica v15 uses pgvector (vector DB). graphify takes **opposite approach**.

---

## Part 8 — MCP server mode

graphify có **built-in MCP server** — first corpus framework với MCP output first-class:

```bash
python -m graphify.serve graphify-out/graph.json
```

Exposes:
- `query_graph` — free-form graph query
- `get_node` — node details
- `get_neighbors` — N-hop neighbors
- `shortest_path` — node-to-node path

Agents có thể connect via MCP stdio → structured graph access.

---

## Part 9 — Karpathy lineage / Dòng dõi trí tuệ Karpathy

### 🇻🇳 Bối cảnh

**Storm Bear vault** được xây trên **Karpathy's LLM Wiki pattern**. Vault founding document cite Karpathy.

**graphify** explicitly cite Karpathy's /raw folder workflow.

→ graphify là **2nd Karpathy-linked wiki** trong corpus (sau autoresearch v10, framework của chính Karpathy).

**Ý nghĩa cho Storm Bear:** vault đang touching Karpathy intellectual lineage 3 lần:
- vault foundation (LLM Wiki pattern)
- autoresearch v10 (Karpathy's own)
- graphify v16 (Karpathy-inspired)

### 🇬🇧 Why this matters

Storm Bear traces its intellectual origin to Karpathy's LLM Wiki methodology. Graphify is also Karpathy-inspired — meta-cycle extends.

Pattern candidate emerging: **#19 Intellectual Lineage Clustering** — certain thinkers (Karpathy, Bostrom, Linear founders) exert disproportionate influence in agent-space.

---

## Part 10 — Storm Bear relevance (DIRECT applicability)

### 🇻🇳 Action item quan trọng nhất

**Chạy graphify trên Storm Bear vault ngay trong 1 session.**

```bash
pip install graphifyy
graphify claude install
cd "/Users/Cvtot/KJ OS Template"
/graphify . --obsidian --wiki
```

Expected results:
1. **Community detection** → likely tier clusters (T1/T2/T3/T4/T5) auto-surface
2. **God nodes** → Karpathy, OpenClaw, Hermes, Pattern #9, paperclip = top centrality
3. **Missing cross-refs** → graphify infers relationships Storm Bear hasn't explicit-linked
4. **Stale claims** → `--watch` mode alerts when source wikis update
5. **Published output** → `wiki/index.md` = public-facing Storm Bear knowledge base

### 🇬🇧 Why this is the top v16 action

graphify is:
- **Free to try** (~$5-20 first run on vault)
- **Local-first** (no data leaves machine except Claude API)
- **Obsidian-compatible** (direct export)
- **Reversible** (delete graphify-out/ to undo)

**Risk: low. Upside: high.** Storm Bear vault IS Karpathy's /raw folder problem at larger scale.

### Scrum-coach relevance

graphify for Scrum:
- **Team knowledge base** — extract architecture from team's code + docs
- **Onboarding** — new members query graph instead of shadowing seniors
- **Sprint retro** — knowledge graph reveals which modules changed most
- **Technical debt** — god nodes may reveal over-coupled modules

**Onboarding cost:** low — pip install + `/graphify .`

---

## Part 11 — Tradeoffs + limitations

### Strengths

- ✅ **15-platform install** (flexibility)
- ✅ **Multi-modal** (code + docs + images + video)
- ✅ **Local-first** (privacy)
- ✅ **Persistent** (query weeks later)
- ✅ **Interpretable** (EXTRACTED/INFERRED taxonomy)
- ✅ **No infra** (no vector DB, no server)
- ✅ **Open source** (MIT)

### Limitations

- ❌ **First-run LLM cost** (~$5-20 on mid-size corpus)
- ❌ **Claude-biased** (vision tied to Claude currently)
- ❌ **Solo-maintainer bus-factor** (safishamsi only; 7 contributors total)
- ❌ **Pre-1.0 API changes expected** (v0.4.23)
- ❌ **Leiden stability** (community assignments may shift on updates)
- ❌ **No team sharing built-in** (graph is local)

---

## Part 12 — Learning roadmap / Lộ trình học

### Week 1: Personal install

- Day 1: `pip install graphifyy && graphify install`
- Day 2-3: Run on 3-5 personal folders (code repo, research /raw, docs)
- Day 4-5: Explore interactive HTML visualization
- Day 6-7: Try queries, compare with raw-file search

### Week 2: Workflow integration

- Day 8-9: Set up `graphify hook install` for auto-rebuild
- Day 10-11: Test `--watch` mode on active project
- Day 12-14: Integrate graphify output into Claude Code conversations

### Week 3: Advanced

- Day 15-17: Try `--mode deep` for aggressive inference
- Day 18-19: Set up MCP server for agent access
- Day 20-21: Experiment with `--obsidian` for Obsidian vaults

### Week 4: Storm Bear vault pilot

- Day 22-24: Run graphify on Storm Bear vault
- Day 25-26: Analyze god nodes + communities
- Day 27-28: Feed findings back into Pattern Library + routine v2

---

## Part 13 — References + next action

### Wiki pages

- [[(C) index]] — phase tracking
- [[(C) README + multi-language cluster summary]]
- [[(C) ARCHITECTURE + AGENTS + SECURITY cluster summary]]
- [[(C) Integration + Packaging + 15 Platforms cluster summary]]
- [[(C) Knowledge Graph for AI Coding Assistants]]
- [[(C) 15-Platform Install + Agent-Runtime Standards Confirmed]]
- [[(C) Karpathy-Inspired Raw-Folder Problem + Meta-Cycle Extension]]
- [[(C) T4 3-way Extension + Pattern 9 Test + Storm Bear]]

### Cross-wiki siblings

- T4 peers: gws v13 + notebooklm-py v7
- Karpathy peer: autoresearch v10
- Agent-runtime standards: codymaster v12 + paperclip v14 + multica v15

### Official

- Repo: https://github.com/safishamsi/graphify
- Homepage: https://safishamsi.github.io/penpax.ai
- PyPI: https://pypi.org/project/graphifyy/

### 🎯 Suggested next action (Storm Bear)

**Run graphify on Storm Bear vault today.** ~30-60 min investment. Potentially surface Pattern #19+ candidates + validate Pattern #18 (OpenClaw/Hermes god-nodes?) + visualize 16-wiki cross-reference density.

This is the **highest-leverage single action** available to Storm Bear at v16.

---

**Wiki 16/16 — T4 N=3 extension + Pattern #9 multi-axial refinement + Karpathy 2nd touchpoint + OpenClaw/Hermes execution-confirmed. Routine `llm-wiki-routine` v1 thứ 16 auto-execution.**
