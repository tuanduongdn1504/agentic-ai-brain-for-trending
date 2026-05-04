# Agentic AI Second Brain (Storm Bear vault)

> **A second brain for agentic AI:** 56-wiki trending-tools corpus + Pattern Library (39 confirmed cross-wiki patterns) + skill ecosystem. LLM Wiki pattern (Karpathy lineage), routine v2.1 autonomous orchestration. Solo-VN-Scrum-coach build.

> **Một bộ não thứ hai cho AI tự chủ:** kho 56 wiki các công cụ AI đang trending + Thư viện Pattern (39 pattern đã xác nhận giữa các wiki) + hệ sinh thái skill. Theo pattern LLM Wiki (kế thừa Karpathy), routine v2.1 autonomous orchestration. Xây dựng bởi solo-VN-Scrum-coach.

---

## What is this / Đây là gì

**EN:** This is an Obsidian vault implementing Andrej Karpathy's LLM Wiki pattern for software development knowledge. Instead of re-deriving knowledge from scratch on every Claude conversation, the vault **incrementally builds and maintains a structured knowledge base** — summaries, entity pages, cross-references, evolving synthesis. Operator curates sources + directs analysis. Claude (or any agentic AI) handles the grunt work. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

**Current scope:** 56 LLM wikis spanning T1 coding-agents (Claude Code internals / GSD / spec-kit / aidevops) + T2 workflow-platforms (n8n / multica / ruflo / goclaw) + T3 education curricula + T4 agent-bridge tools (gh-aw / ollama / claude-context) + T5 standalone agent applications + outside-scope subjects (system-prompts-leaks / awesome-list-genre / content-marketing).

**VN:** Đây là một Obsidian vault áp dụng pattern LLM Wiki của Andrej Karpathy cho kiến thức phát triển phần mềm. Thay vì re-derive kiến thức mỗi lần chat với Claude, vault **liên tục build và maintain một knowledge base có cấu trúc** — summary, entity pages, cross-reference, tổng hợp tiến hoá. Operator curate nguồn + chỉ đạo analysis. Claude (hoặc bất kỳ agentic AI nào) làm phần grunt work. Obsidian là IDE; LLM là programmer; wiki là codebase.

**Scope hiện tại:** 56 LLM wiki bao gồm T1 coding-agents + T2 workflow-platforms + T3 education curricula + T4 agent-bridge tools + T5 standalone agent applications + outside-scope subjects.

## Who built this / Ai xây?

**EN:** Solo-VN Scrum coach + developer. Email `claude1@cvtot.vn` (intentionally identifiable as vault operator). Started 2026-04-17 (vault setup); 56 wikis built in 12 days at velocity plateau ~2-3h/wiki. Vault is operator's personal knowledge base shared publicly for transparency + pattern-sharing + community-learning.

**VN:** Solo-VN Scrum coach + developer. Email `claude1@cvtot.vn` (chủ động identifiable là operator của vault). Bắt đầu 2026-04-17 (setup vault); 56 wiki build trong 12 ngày tại velocity plateau ~2-3h/wiki. Vault là knowledge base cá nhân của operator, share công khai vì transparency + pattern-sharing + community-learning.

## Scope + caveats / Phạm vi + lưu ý

This vault is **operational, not service**:

- ✅ Operator-personal LLM knowledge base
- ✅ Open-source (MIT) for community learning + pattern sharing
- ✅ Multi-runtime compatible (Claude Code primary; OpenCode / Aider / Cursor secondary via AGENTS.md shim)
- ❌ NOT a managed service (operator does not host vault-as-a-service)
- ❌ NOT a turnkey product (requires Obsidian + Claude Code subscription + setup time)
- ❌ NOT a drop-in agent framework (vault is content + methodology; runtime is your choice)

## Install / Cài đặt

### Path A: Clone for own use (most common)

```bash
git clone https://github.com/Cvtot/agentic-ai-second-brain.git
cd agentic-ai-second-brain
# Open with Obsidian (https://obsidian.md) — set this directory as vault
# Use with Claude Code (https://claude.com/product/claude-code)
```

### Path B: Read online (no install)

Browse the GitHub repo directly:
- `CLAUDE.md` — vault context entry point
- `PATTERN_LIBRARY.md` — 39 confirmed patterns
- `03 Projects/<wiki-name>/` — 56 individual LLM wiki entries
- `05 Skills/llm-wiki-routine-v2.1.md` — autonomous orchestration routine

### Path C: Copy specific skills

If you only want skill files for your own Claude Code projects:

```bash
# Copy the LLM Wiki routine skill
curl -O https://raw.githubusercontent.com/Cvtot/agentic-ai-second-brain/master/05%20Skills/llm-wiki-routine-v2.1.md

# Copy the brain-setup skill
curl -O https://raw.githubusercontent.com/Cvtot/agentic-ai-second-brain/master/05%20Skills/brain-setup.md
```

## Use cases / Use case

### For solo developers building Second Brains

- Clone vault structure as starting template
- Adapt `CLAUDE.md` operator profile to your own context
- Use routine v2.1 to build your own LLM wiki corpus

### For Scrum coaches / engineering managers

- Reference `03 Projects/<wiki>` entries for tool evaluation (n8n / claude-howto / claude-hud / pi-mono / etc.)
- Use Pattern Library for cross-tool pattern analysis (Pattern #18 Agent Runtime Standardization / Pattern #50 Commercial-Funnel Companion / etc.)
- Adapt skill ecosystem for team Scrum automation (n8n integration patterns documented)

### For Pattern Library practitioners

- 39 confirmed cross-wiki patterns documented with formal criteria
- 6 structural-promotion criteria + 13 distinct pattern-statement structural forms
- 12+ audit documents in `04 Reviews/` showing pattern evolution
- Reference for your own pattern-mining work

### For AI agent researchers

- Corpus of 56 wikis surveys agentic-AI tool space across 5 tiers
- Pattern Library identifies recurring architectural patterns
- Routine v2.1 demonstrates autonomous-orchestration discipline

## Pattern Library overview

**Current state (post-v56-mini-audit, preserved 6 cycles):**
- 39 confirmed patterns
- 17 active candidates
- 3 stale candidates (#45 Dual-Licensing / #52 Extreme-Viral-Velocity / #72 PolyForm-Noncommercial)
- 9 retired patterns
- 6 observation-tracks
- Ratio 17:39 = **0.436:1** (NEW LARGEST buffer 0.514 below 0.95:1 mini-audit trigger maintained 6 cycles)

**20-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES streak** (v37-v56) — LONGEST in corpus history.

Full Pattern Library: see `PATTERN_LIBRARY.md` + `_patterns/` chapter files.

## Skills catalog

`05 Skills/` directory contains:

- **`llm-wiki-routine-v2.1.md`** (current; tightened session 66 with STRICT Phase 0.9 4-criteria gate) — autonomous orchestration routine for building LLM wikis
- **`brain-setup.md`** — 5-round operator interview for `CLAUDE.md` generation
- **`new-project.md`** — project scaffolding for new vault entries
- `llm-wiki-routine.md` (v1; archived) — original routine
- `llm-wiki-routine-v2.md` (v2; archived) — superseded by v2.1

## License

MIT License. See `LICENSE.md`.

External projects analyzed in `03 Projects/` retain their own licenses — vault contains observational analyses, not source-code redistribution.

## Contributing

This vault is currently solo-operator. **No contributions accepted at this time.** If you find something useful, fork freely (MIT permits this). If you have feedback, open a GitHub issue or email `claude1@cvtot.vn`.

Future cohort participation may be considered at Phase 4 mastery — see `GOALS.md` for vault evolution roadmap.

## Repository topics

`agentic-ai` / `second-brain` / `llm-wiki` / `pattern-library` / `claude-code` / `obsidian-vault` / `karpathy` / `vietnamese` / `scrum-coaching` / `agent-skills` / `ai-tools-trending`

## References

- **Karpathy LLM Wiki pattern** (lineage origin) — Andrej Karpathy's LLM-as-wiki-maintainer concept
- **Anthropic Claude Code** — primary harness (https://claude.com/product/claude-code)
- **Obsidian** — vault IDE (https://obsidian.md)
- **MIT License** — https://opensource.org/licenses/MIT

## Inspiration / lineage acknowledgments

This vault would not exist without:
- Andrej Karpathy's LLM Wiki pattern thinking
- Tiago Forte's "Building a Second Brain" methodology
- John Lam's `lm-wiki` exploration
- Lance Martin's agentic engineering discipline
- Boris Cherny's Claude Code design
- Specification-Driven Development (SDD) community (GSD / spec-kit / aidevops)
- Anthropic skills marketplace community
- The 56 trending-AI-tool projects analyzed in this vault — each contributed structural patterns to the Pattern Library

## Project status

- **Phase 1 (Foundation):** ✅ Complete 2026-04-17
- **Phase 2 (Fluency):** 🟢 Massively exceeded (55+ wikis vs target 1)
- **Phase 3 (Autonomous workflows):** 🟢 Exceeded via routine v2.1 production-stable
- **Phase 4 (Mastery + Contribution):** ⏸ In progress — public-release as of 2026-04-29 IS the Phase 4 inflection
