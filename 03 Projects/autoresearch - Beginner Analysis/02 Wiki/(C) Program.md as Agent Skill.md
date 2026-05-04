# (C) Program.md as Agent Skill

> Entity page — Pattern concept (meta-pattern Storm Bear inherits)
> Sources: program.md summary + README agent setup + cross-vault parallels
> Format: 13-section canonical

## 1. What is it / Nó là gì

**program.md** = **Markdown document containing agent instructions**. Functions as **"skill" the agent loads at startup**. Humans iteratively refine program.md based on agent performance observed. ~7 KB. Core objective + capabilities + constraints + workflow defined in single file.

**Generalizable pattern:** `<anything>.md` as agent skill. Examples across ecosystem:
- **autoresearch:** `program.md`
- **Storm Bear vault:** `llm-wiki-routine.md`, `llm-wiki-ingest.md`
- **deer-flow:** `skills/public/*.md` + `skills/custom/*.md`
- **notebooklm-py:** `SKILL.md`
- **Claude Code:** `~/.claude/skills/*.md`

## 2. Why it matters / Sao quan trọng

### Agent skills as Markdown = emerging convention

**Pre-Markdown agent era:** code + prompts hard-coded + APIs documented via OpenAPI.
**Markdown agent era:** natural-language-first instructions, readable, versionable, editable by non-coders.

### Benefits

1. **Human-readable** — agent programmers + domain experts can collaborate
2. **Version-controllable** — git history = skill evolution trace
3. **Shareable across frameworks** — same Markdown potentially works in multiple LLM agent frameworks
4. **Iteration-friendly** — easy to refine one section at a time
5. **Documentation = execution** — no docs/code gap

### Karpathy's demonstration

autoresearch's `program.md` = **public demonstration** của this pattern from the LLM Wiki pattern author. Lends authority to broader "skill-as-Markdown" convention.

## 3. Structure of autoresearch's program.md (inferred)

Based on Phase 2 summary:

```markdown
# [Title]

## Objective
[What agent optimizes for — val_bpb]

## Capabilities
- Code modification scope (train.py only)
- Experimentation autonomy
- Git-based tracking

## Workflow
### Setup phase
[Branch creation, file reading, verification]

### Experiment loop
[Modify → commit → train → evaluate → keep/revert → log]

### Persistence
[Continue indefinitely]

## Constraints
- Don't modify prepare.py
- Don't install packages
- Don't alter evaluation functions

## Preferences
- VRAM increases for meaningful gains only
- Simplicity valued
```

## 4. Comparison to Storm Bear's llm-wiki-routine.md

Both = Markdown skill files orchestrating autonomous agent loops.

| Dimension | autoresearch program.md | Storm Bear llm-wiki-routine.md |
|-----------|------------------------|--------------------------------|
| **Size** | ~7 KB | ~420 lines (~15-20 KB) |
| **Structure** | Setup + loop + constraints | 7 phases sequenced |
| **Loop** | Infinite research iteration | One-shot per URL |
| **Target output** | Better val_bpb | LLM Wiki artifacts |
| **Human refine** | Iterative program.md edits | Planned v2 upgrade |
| **Metric** | val_bpb (objective) | 13-section format compliance (subjective) |
| **Artifact store** | Git commits + results.tsv | Obsidian vault files |
| **Duration** | Overnight / continuous | ~2h per wiki |
| **Autonomy** | Full (no human in loop) | Semi (Claude Code session) |

### Identical meta-structure

1. Human defines skill in Markdown
2. Agent loads skill at startup
3. Agent executes autonomously (within constraints)
4. Artifacts persist
5. Human reviews results
6. Human refines skill
7. Repeat

**Direct lineage:** Storm Bear's routine pattern = descendant of Karpathy's autoresearch pattern applied to knowledge domain.

## 5. Why Markdown (not JSON/YAML)

### Markdown strengths
- **Natural language first** — easier for domain expertise
- **Rich formatting** — headers, lists, emphasis = semantic structure
- **LLM-trained natively** — models trained on Markdown, interpret well
- **Editable in any editor** — no specialized tooling
- **Human + LLM share same format** — no translation layer

### JSON/YAML alternatives weaknesses
- **Schema-rigid** — changes break parsers
- **Harder to read** — nested braces + quotes
- **Less expressive** — structured data ≠ nuanced instructions
- **Require parser** — separate from agent

### Karpathy's pedagogical signal
Using Markdown = **teaching choice**. Any reader can edit program.md without JSON schema knowledge. Lowers barrier.

## 6. Skill refinement patterns

### autoresearch refinement cycle
1. Agent runs overnight
2. Human reads results.tsv
3. Human spots: "Agent missed trying X" or "Agent wastes time on Y"
4. Human edits program.md: "Also try X" or "Avoid Y"
5. Next night: agent incorporates

### Storm Bear refinement cycle
1. Routine runs (~2h per wiki)
2. Phase 5 iteration log captures observations
3. Learnings accumulate (20+ action items over v3-v9)
4. Planned routine v2 upgrade incorporates all
5. Next wiki uses v2 routine

**Cadence difference:**
- autoresearch: nightly refinement
- Storm Bear: batched refinement (every few wikis)

## 7. Agent skill taxonomy (emerging from 10 wikis)

### Skill file sizes across corpus

| Wiki | Skill file | Size | Approach |
|------|-----------|------|----------|
| ECC (T1) | Many small skills | 1-5 KB each | Many small |
| Superpowers (T1) | Pattern library skills | 3-10 KB | Pattern library |
| gstack (T1) | Specialist role skills | 5-15 KB | Role-based |
| GSD (T1) | Command + agent mix | 3 KB each | Command-library |
| goclaw (T2) | Platform-level skills | Per-tenant | Platform-managed |
| course (T3) | N/A | - | Teaches about skills |
| notebooklm-py (T4) | 1 mega SKILL.md | 26 KB | Mega-skill |
| deer-flow (T5) | Progressive public+custom | Variable | Progressive library |
| **autoresearch (T5)** | **1 program.md** | **7 KB** | **Single-purpose skill** |
| build-your-own-x (outside) | N/A | - | - |

### Insight: Skill scale correlates với agent scope

- **Narrow purpose (autoresearch):** 1 small file
- **General harness (deer-flow):** many files progressive
- **Many tasks (ECC):** many small files
- **One big purpose (notebooklm-py):** 1 large file
- **Workflow pattern (Storm Bear routine):** 1 medium file per workflow

## 8. Trade-offs / Limitations

### Strengths
- **Pattern proven** — works in autoresearch (74K stars validates)
- **Low barrier** — Markdown edit = skill change
- **Composable** — can combine multiple Markdown skills
- **Portable** — works across LLM frameworks

### Weaknesses
- **LLM interpretation variance** — different models interpret same Markdown differently
- **Instructions drift** — grows over iterations, coherence risk
- **No validation** — who checks if instructions are sound?
- **Context bloat risk** — loading multiple large skills = context window pressure
- **Versioning ambiguity** — which skill version did agent use?

## 9. Comparison to sibling skill patterns

### Skill-as-Markdown (broad adoption)
- ECC, Superpowers, gstack, GSD, notebooklm-py, deer-flow, autoresearch, Storm Bear = ALL Markdown-first skill files

### Skill composition patterns

| Pattern | Example | When |
|---------|---------|------|
| **Many small** | ECC (185 skills) | Diverse narrow tasks |
| **Progressive library** | deer-flow | General-purpose with scope |
| **Single mega** | notebooklm-py (26 KB) | One complex domain |
| **Single purpose** | autoresearch (7 KB) | One specific workflow |
| **Workflow orchestrator** | Storm Bear routine | Multi-phase task |

**Each pattern valid.** Depends on scope + agent context budget + refinement cadence.

## 10. Common pitfalls

1. **Over-instruction** — program.md becomes War and Peace; LLM ignores detail
2. **Under-instruction** — agent hallucinates behavior; needs more guidance
3. **Contradictions** — instructions conflict, agent picks arbitrarily
4. **Outdated instructions** — skill references old API/function; agent errors
5. **No constraint boundary** — agent modifies things out of scope
6. **Missing metric** — agent "tries" without clear success criterion
7. **No persistence rules** — agent asks human for everything (defeats autonomy)

## 11. When NOT to use program.md-style skill

- **Truly stateless one-shot** — just prompt, no loop
- **Hard-realtime** — instruction loading adds latency
- **Security-critical** — need cryptographic-level capability control (not Markdown)
- **Multi-agent coordination** — plain Markdown doesn't handle
- **Audit-compliance** — need machine-enforceable instructions

## 12. Storm Bear vault relevance (PEAK)

### Direct lineage

Storm Bear's skill pattern = **intellectual descendant** of Karpathy's pattern visible in:
- autoresearch (program.md = agent skill)
- nanoGPT/nanochat (minimal code = instructions)
- Various tokenization videos (human-readable explainer pattern)

### Routine v2 lessons from program.md

**From autoresearch, routine v2 could adopt:**

1. **Tight scope per skill** — program.md = 1 purpose, Storm Bear's routine handles many phases (consider splitting?)
2. **Iteration log as refinement input** — Storm Bear already does this via iteration logs
3. **Branch-per-campaign** — autoresearch uses `autoresearch/mar5` branch; Storm Bear could branch-per-wiki
4. **Results.tsv analog** — structured log of each wiki's build metrics (time, entity count, quality signals)

### Honor the lineage

Storm Bear root CLAUDE.md already credits Karpathy. This wiki reinforces:
- Karpathy's LLM Wiki pattern = foundational
- Karpathy's autoresearch = demonstration
- Storm Bear vault = application to knowledge domain
- **All 3 same meta-pattern.**

## 13. References / Nguồn

- Source: [[(C) program.md agent skill summary]] (primary)
- Related entities:
  - [[(C) 5-Minute Experiment Loop]] (what program.md orchestrates)
  - [[(C) Karpathy's Meta-contribution to Storm Bear]] (broader lineage)
- Sibling skill patterns:
  - `../../notebooklm-py - Beginner Analysis/02 Wiki/(C) Skill Integration (Claude Code + Codex + OpenClaw).md` (mega-skill)
  - `../../deer-flow - Beginner Analysis/02 Wiki/(C) Skill System (Progressive Loading).md` (progressive library)
- Storm Bear skill parallels:
  - `../../../05 Skills/llm-wiki-routine.md`
  - `../../../05 Skills/llm-wiki-ingest.md`
