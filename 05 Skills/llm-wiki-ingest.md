# Skill: LLM Wiki Ingest

📍 **Status:** IN-FLUX (continues evolving — current version as of 2026-05-06)

Build a persistent, compounding knowledge wiki about a complex topic, following Karpathy's LLM Wiki pattern. Codified from successful application trong project `Everything Claude Code - Beginner Analysis` (2026-04-17).

> **Principle:** Instead of re-deriving knowledge từ RAG mỗi query, LLM incrementally builds maintained wiki — summaries, entity pages, cross-references, evolving synthesis. Obsidian là IDE, LLM là programmer, wiki là codebase.

## When to Use

### ✅ Use khi topic pass threshold:

- **≥5 sources** (articles, files, repos, specs) liên quan
- **≥3 months expected lifespan** của topic (không phải one-off)
- **Clear ownership** — có người maintain
- **Cross-references meaningful** — sources talk to each other
- **User explicitly asks** cho "knowledge base", "wiki", "beginner guide" cho topic phức tạp

### ❌ Skip (dùng `00 Notes/` flat files) khi:

- One-off task, không cần compound
- <5 sources, scope nhỏ
- Topic thay đổi quá nhanh (wiki không kịp update)
- Quick reference đã có ở nơi khác

## How It Works — 5 phases

### Phase 1: Setup (5-10 phút)

**1.1 Kiểm tra threshold với user.** Hỏi:
- "Topic này dự kiến có bao nhiêu sources (articles/files/repos)?"
- "Bạn maintain knowledge này trong ≥3 tháng không?"
- "Ai đọc wiki này — mình hay team?"

**Nếu fail threshold:** propose flat files trong `00 Notes/` thay vì wiki.

**1.2 Use skill `new-project`** để scaffold project folder trong `03 Projects/`. Folder naming reflect topic (vd `Everything Claude Code - Beginner Analysis`).

**1.3 Tạo folder structure** cho wiki pattern:

```
<project>/
├── CLAUDE.md
├── COMMANDS.md
├── 00 Sources/        ← raw content (clone/copy vào, immutable)
├── 01 Analysis/       ← working notes, open questions
├── 02 Wiki/           ← entity + concept + summary pages (LLM-maintained)
├── 03 Published/      ← finished guides ready to share
├── 04 System/
├── 05 Skills/
├── 06 Attachments/
└── 07 Iteration Logs/ ← session learnings
```

**1.4 Clone/copy sources** vào `00 Sources/`:
```bash
cd "03 Projects/<name>/00 Sources"
git clone <repo-url>  # hoặc copy files
```

**1.5 Tạo foundational wiki files NGAY** (không defer):

**`02 Wiki/(C) index.md`** — catalog với 4 sections:
```markdown
# (C) Index — <Topic> Wiki

## Sources
| Page | Summary | Ingested |

## Concepts
_Chưa có. Sẽ tạo khi ingest sâu hơn._

## Entities
| Page | Type | Sources synthesized | Status |

## Roadmaps
_Chưa có._

## Logs
- [[(C) log]]
```

**`02 Wiki/(C) log.md`** — chronological, format parseable:
```markdown
# (C) Log — <Topic> Wiki

> Append-only. Format: `## [YYYY-MM-DD] type | title` để grep được.

## [YYYY-MM-DD] setup | Wiki initialized
- Project scaffolded
- Sources cloned
- Foundational files created
```

**1.6 Tạo `01 Analysis/(C) open questions.md`** empty template — sẽ populate khi ingest.

---

### Phase 2: Source ingestion (per source, 15-20 phút each)

**Target:** 2-3 source summaries trước khi entity pages. Build breadth → depth.

**2.1 Skim source TRƯỚC khi deep read.** Nếu >20KB, grep headings first:
```bash
grep -n "^## \|^### " <source-file> | head -40
```
Identify priority sections.

**2.2 Read source** (chunk nếu quá lớn — limit 200-400 lines per read call).

**2.3 Write summary page** `02 Wiki/(C) <Source Name> summary.md` theo format:

```markdown
# (C) <Source Name> Summary

> **Source:** path/to/source
> **Ingested:** YYYY-MM-DD
> **Coverage:** lines X-Y (full/partial)

## TL;DR
**VI:** [bilingual summary]
**EN:** [parallel]

## [Preserve author's narrative arc — major sections from source]

## Connection to <Vault Context>
[Lessons/patterns applicable to current vault or project]

## Câu hỏi mở / Open questions
1. [Questions raised by this source]

## Cross-references
- [[(C) index]]
- [[(C) log]]
- _Sẽ link tới_ [[other pages]] khi tạo

## Citations
- <source>, lines X-Y (X KB)
- External references from source
```

**2.4 Update `(C) index.md`** — thêm row vào Sources table.

**2.5 Append entry to `(C) log.md`:**
```markdown
## [YYYY-MM-DD] ingest | <source-name>
- Source: <path> (<size>)
- Coverage: <what was read>
- Pages created: [[summary page]]
- Pages updated: [[(C) index]]
- Open questions: xem [[(C) open questions]]
- Next: [recommendation]
```

**2.6 Update `(C) open questions.md`** — thêm questions mới; mark resolved ones ✅.

**2.7 VERIFY claims** — nếu source claim số liệu, run `ls` / `grep` / `wc -l` để verify. Contradictions = contribution opportunities.

---

### Phase 3: Entity pages (per entity, 20-30 phút each)

**Target:** Tạo entity pages cho building blocks/components quan trọng sau 2-3 source summaries.

**3.1 Identify candidates từ source summaries.** Entity đáng có page riêng khi:
- ≥3 sources nói về nó
- Là building block foundation của topic
- Người mới hay confused, cần disambiguation

**3.2 Peek at concrete files** cho grounding nếu apply:
```bash
# Vd khi entity là "Hooks":
ls 00 Sources/<repo>/hooks/
cat 00 Sources/<repo>/hooks/README.md
```

**3.3 Write entity page** theo **13-section canonical format:**

```markdown
# (C) <Entity Name> — Entity Page

> **Type:** [building block #N / bridge concept / legacy]
> **Status:** [Nth entity page]
> **Sources:** N (list them)
> **Last updated:** YYYY-MM-DD

---

## Một câu / One-liner
**VI:** [1-2 sentences bilingual]
**EN:** [parallel]

---

## Khi nào dùng / KHÔNG dùng
### ✅ Dùng khi:
- ...
### ❌ KHÔNG dùng khi:
- ...

---

## <Entity> vs sibling concepts (chọn cái nào?)
| Tiêu chí | <Entity> | Sibling A | Sibling B |
|----------|----------|-----------|-----------|
| ...      |          |           |           |

> **Quy tắc quyết định:** [clear rule]

---

## Sub-types / Categorization
[Table hoặc list, theo nhóm]

---

## Anatomy: Entity trông như thế nào
[File/config format với inline annotations. Skip section này nếu entity không có file format]

### Frontmatter fields / Field reference
| Field | Bắt buộc | Ý nghĩa |

---

## Cơ chế / How It Works
[Flow diagram ASCII hoặc sequence]

---

## Out-of-box list (ECC/source ships) — nếu apply
[What's shipped ready-to-use]

---

## Configuration
[How to enable/disable/customize]

---

## Recipes (progressive complexity)
### Recipe 1: Minimal safe default
### Recipe 2: Common use case
### Recipe 3: Advanced

---

## Advanced patterns
[Nâng cao từ longform/deep dive]

---

## Patterns kết hợp / Combination patterns
### <Entity> + Sibling A
### <Entity> + Sibling B
[Compose patterns]

---

## Anti-patterns / Sai lầm hay gặp
1-10 common mistakes với explanation.

---

## Tools liên quan / Related tools
| Tool | Purpose |

---

## Cross-references
- [[(C) other-entity]]
- [[(C) source summaries]]
- [[(C) index]]

## Citations
- Specific file paths with line ranges
- External links

---

## TODO cho lần ingest tiếp
- [ ] Things discovered but not yet integrated
- [ ] Follow-up research items
```

**3.4 Optional sections** thêm khi content justify:
- **"Case study"** — khi entity có instance đặc biệt notable (vd Skills → continuous-learning v2)
- **"Validator quirks"** — khi entity có strict schema (vd Plugins manifest)
- **"Migration matrix"** — khi entity đang deprecate (vd legacy Commands)
- **"Real-world examples"** — khi có folder `examples/` dedicated
- **"Security considerations integrated"** — khi ingest security source TRƯỚC entity page

**3.5 Update `(C) index.md`** — Entities table.

**3.6 Append log entry** với key learnings + format observations.

**3.7 Expect retrofit sau entity #2-3** — pattern stabilize qua iteration, không phải upfront design. Entity #1 là prototype.

---

### Phase 4: Published guide (30-40 phút)

**Target:** Tạo **1 published guide** trong `03 Published/` sau foundation entity pages đủ (thường 4+).

**Key differences vs entity page:**
- **Linear narrative** (entity page = random access reference)
- **Progressive disclosure** (intro → foundation → action → security → FAQ)
- **Copy-paste commands** (mọi action có command cụ thể)
- **Progressive complexity trong roadmap** (tuần 1 minimal → tuần 4 advanced)
- **Security integrated giữa guide** (không phải cuối — không thể afterthought)

**Structure template:**

```markdown
# <Topic> — Hướng dẫn cho người mới

> **For team:** 30-minute read, sufficient để setup + productive workflow.
> **Version:** v1 | **Date:** YYYY-MM-DD | **Bilingual**

## Mục lục
[Linked ToC]

## Tại sao đọc cái này
### Ai nên đọc
### Bạn sẽ có gì
### Không phải là gì

## Part 1: <Topic> là gì
[Positioning + comparison với alternatives]

## Part 2: Core concepts/building blocks
[Link ra entity pages]
| Priority | Entity | Why read this first |

## Part 3: Setup roadmap N tuần
### Tuần 1 — Foundation
### Tuần 2 — [...]
### Tuần 3 — [...]
### Tuần 4 — [...]
[Each tuần có concrete todos với commands]

## Part 4: Security minimum bar
[Nếu topic có security angle. 11-item checklist format works well]

## Part 5: FAQ
[7 realistic questions — cost, team sharing, context full, contribution opportunities]

## Part 6: Resources
[Cross-links wiki + external]

## Bước tiếp theo
[Concrete next actions]
```

**Save trong `03 Published/(C) <Topic> - Huong dan.md`.**

---

### Phase 5: Iteration log (15-20 phút)

**Target:** Capture learnings mỗi major milestone hoặc end-of-session.

**Save trong `07 Iteration Logs/(C) YYYY-MM-DD <description>.md`.**

**9-section iteration log format:**

```markdown
# (C) Iteration Log — <Description> (YYYY-MM-DD)

## Tóm tắt
## ✅ Cái gì work tốt (list với explanation mỗi item)
## ❌ Cái gì chưa work (list với explanation + alternative)
## 📋 Patterns & templates khám phá được
## 📊 Metrics & numbers (throughput, file sizes, time estimates)
## 🎯 Recommendations cho project sau
## 🔁 Pattern áp dụng cho vault context (threshold, candidates, anti-candidates)
## 🧬 Meta-learning (prove/disprove hypotheses)
## 📍 Action items cho vault level
```

---

## Critical rules — DON'T violate

1. **Tạo foundational files (`index.md`, `log.md`) NGAY ingest đầu** — không defer
2. **`(C)` prefix** cho mọi file Claude-generated (theo vault CLAUDE.md rule)
3. **Cross-reference mọi page mới** — kể cả forward-declare tới pages chưa tạo
4. **Verify claims số liệu** bằng filesystem/code — đừng trust marketing
5. **Append-only log** — không rewrite history
6. **Open questions file là deliverable** — cập nhật mỗi ingest
7. **Ingest philosophy source TRƯỚC detail entity** khi có overlap (vd security guide trước entity về components có security risk)
8. **Source summary preserve author's narrative**; entity page imposes canonical 13-section format
9. **Published guide format ≠ entity page format** — linear vs reference
10. **TodoWrite từ đầu** cho multi-step ingest work

## Anti-patterns — tránh

1. **Format perfect trước khi viết entity #1** — accept prototype tax, retrofit sau #2-3
2. **Translate 100% technical terms** — keep English cho plugin/hook/skill/etc.; translate narrative only
3. **Skip verification** — luôn verify counts/claims với `ls`, `wc -l`, `grep`
4. **Delete open questions** — move to resolved ✅ mark, không delete
5. **Nhồi mọi thứ vào CLAUDE.md** — move static standards sang rules, dynamic context sang `--system-prompt`
6. **Arbitrary terminal counts cho parallel work** — minimum viable parallelization
7. **Ignore contradictions giữa sources** — contradictions = contribution opportunities
8. **Build wiki cho topic <5 sources** — không compound, overhead lãng phí
9. **Publish guide trước khi foundation entity đủ** — guide sẽ thin
10. **Skip iteration log** — meta-learning cực value, đừng defer

## Meta-learning: LLM Wiki pattern proof

**Pattern proven trong project `Everything Claude Code - Beginner Analysis`:**

- ✅ **Knowledge compounds** — each ingest builds on previous context
- ✅ **Cross-references emerge naturally** — 14 pages interconnected
- ✅ **Contradictions surface** — 4 discrepancies found via verification
- ✅ **Published output stronger** — guide → entity → summary → source chain
- ✅ **Human-readable** — can browse like normal docs, không cần query interface

**Cost:**
- Upfront effort > RAG upload
- Requires maintainer (Claude)
- Economic chỉ khi knowledge accumulates ≥3 months

## Time estimates (từ v1 project data)

| Task | Time |
|------|------|
| Setup (Phase 1) | 5-10 phút |
| Source summary (typical) | 15-20 phút |
| Source summary (large >20KB) | 25-35 phút (với chunking) |
| Entity page (typical) | 20-30 phút |
| Entity page (với concrete file peek) | +10 phút |
| Format retrofit | 10 phút per entity |
| Published guide | 30-40 phút |
| Iteration log | 15-20 phút |
| **Full foundation (4 summaries + 7 entities + published)** | **~4-6 hours** |

## Expected deliverable shape

Sau khi apply full skill, project folder sẽ có:

```
03 Projects/<name>/
├── CLAUDE.md + COMMANDS.md
├── 00 Sources/<sources cloned>
├── 01 Analysis/
│   └── (C) open questions.md        ← continuous updates
├── 02 Wiki/
│   ├── (C) index.md                  ← catalog with milestones
│   ├── (C) log.md                    ← chronological activity
│   ├── (C) <source> summary.md x N  ← 1 per major source
│   └── (C) <entity>.md x 4-7        ← 1 per building block
├── 03 Published/
│   └── (C) <topic> - Huong dan.md   ← v1 published guide
└── 07 Iteration Logs/
    └── (C) YYYY-MM-DD v1 build learnings.md
```

**~15-20 files typical cho 1 complete wiki.**

## Usage trigger

User says anything like:
- "Tôi muốn build knowledge base cho <topic>"
- "Analyze <repo> và tạo wiki"
- "Write beginner guide cho team về <tool>"
- "Document <framework> theo LLM Wiki pattern"
- "Apply Karpathy's pattern cho <topic>"

**→ Invoke this skill**, start với Phase 1 threshold check.

## References

- **Verified execution:** `03 Projects/Everything Claude Code - Beginner Analysis/`
- **Iteration log:** `03 Projects/.../07 Iteration Logs/(C) 2026-04-17 v1 build learnings.md`
- **Karpathy's LLM Wiki pattern:** original description trong vault root CLAUDE.md "Purpose" section
- **Storm Bear vault conventions:** `CLAUDE.md` (root) — rules/boundaries/bilingual decisions
