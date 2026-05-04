# (C) Iteration Log — v1 Build Learnings (2026-04-17)

> **Session type:** Full wiki build + v1 published guide + upstream PR preparation
> **Duration:** 1 session (multi-hour)
> **Outputs:** 17 files (14 wiki + 1 published + 2 contribution docs)
> **Purpose:** Capture learnings để tái dùng cho **project LLM Wiki** tiếp theo của Storm Bear vault

---

## Tóm tắt / Summary

Trong 1 session, build được **wiki hoàn chỉnh** cho topic `affaan-m/everything-claude-code` theo LLM Wiki pattern (Karpathy). Foundation layer đầy đủ: 3 trinity guides ingested + 7 entity pages foundation + 1 published guide + 1 upstream contribution ready-to-submit.

**Pattern LLM Wiki hoạt động.** Không phải lý thuyết nữa — đã prove được với concrete deliverable cho team.

---

## ✅ Cái gì work tốt / What worked well

### 1. Iterative format evolution (không cố định format từ đầu)

**Khởi đầu:** Hooks entity page với 11 sections ad-hoc
**Sau 2 entity pages:** discover thêm 3 section cần (Comparison, Anatomy, Combination patterns) → retrofit Hooks
**Sau 7 entity pages:** 13-section format stable, generalizable cho mọi future wiki

**Lesson:** **Đừng cố gắng design format perfect từ đầu.** Build prototype → iterate sau 2-3 instances → lock in pattern. Nhanh hơn và quality cao hơn là "thiết kế format hoàn hảo rồi mới viết."

### 2. Verification early (Q2 count discrepancy)

Ingest đầu tiên (README) phát hiện mâu thuẫn số liệu: Quick Start nói 48 agents, changelog nói 38. **Thay vì assume README đúng, verify bằng `ls`:**

```bash
ls agents/ | wc -l       # → 48 (match Quick Start)
ls -d skills/*/ | wc -l  # → 185 (match Quick Start)
ls commands/ | wc -l     # → 79 (match Quick Start)
```

Kết quả: Quick Start chính xác, changelog outdated. **Gained credibility** để push back khi source contradict.

**Lesson:** Verify số liệu cụ thể bằng filesystem/code, không trust marketing claims. Paid off nhiều lần (đã tìm ra 4 contribution opportunities qua verification).

### 3. Open questions file

Tạo `01 Analysis/(C) README - open questions.md` ngay từ ingest đầu. Mỗi source ingested → thêm questions mới. Mỗi ingest sau có thể resolve questions cũ.

**Stats cuối session:**
- ~28 open questions raised
- ~6 resolved fully (Q1, Q2, Q7, Q8, Q15, và partial Q7)
- ~22 remain open cho future iterations

**Lesson:** Capture uncertainty explicit hơn hide nó. "Honest research > pretending to know." File open questions trở thành roadmap cho ingest tiếp.

### 4. Cross-reference discipline

Mọi page mới bắt buộc có "Cross-references" section link tới pages khác trong wiki. Ngay cả khi page đó chưa tồn tại (placeholder "_Sẽ link tới_ [[(C) Plugins]] khi tạo"), link vẫn thêm.

**Result:** Wiki emerge như **network of connected concepts**, không phải isolated documents. Obsidian graph view sẽ đẹp.

**Lesson:** Forward-reference OK. Even broken links better than no links. Chúng sẽ resolve khi page tiếp được tạo.

### 5. Security timing — ingest trước entity page

Sequence: đọc Security Guide → rồi mới viết (C) MCPs entity page.

Kết quả: MCPs entity page integrated **OWASP MCP Top 10, CVE context, lethal trifecta warning** thẳng vào content thay vì chỉ cross-ref. Chất lượng cao hơn hẳn.

**Counterfactual:** Nếu viết MCPs entity page TRƯỚC security guide, sau đó retrofit security section — sẽ bolt-on, ít integrated.

**Lesson:** Context compounds. Order of ingestion matters. **Ingest broad philosophy TRƯỚC detailed entity khi possible.**

### 6. "Case study" subsection cho entity quan trọng

Skills entity page có dedicated "Case study: Continuous Learning v2" section vì v2 là pattern self-improving quan trọng.

**Pattern:** Khi entity có instance đặc biệt notable → treat như mini-entity trong entity cha. Better than fragmenting across 13 sections.

**Lesson:** Format 13 sections là default, không phải rigid. Thêm section đặc biệt khi content justify.

### 7. Progressive disclosure cho published guide

Published guide theo linear narrative với 4-week roadmap — beginner có clear next action mỗi tuần.

**Decision key:** Security (Part 4) integrated **giữa guide**, không phải cuối. Reason: security không thể là afterthought, phải integrated vào onboarding.

**Lesson:** Published guide ≠ wiki reference. Different readers, different formats. Wiki = random access; published = linear story.

### 8. Bilingual pragmatic, không dogmatic

VN cho narrative prose; EN giữ cho technical terms (plugin/hook/skill/agent/MCP/command/workflow). Code blocks + URLs + CVE numbers giữ nguyên.

**Result:** Vietnamese dev read được natural; vẫn match source terminology để cross-ref.

**Lesson:** Đừng force translate 100%. Technical terms EN chuẩn hoá quốc tế — không cần Vietnamese equivalent mới.

### 9. Chapter-by-chapter user confirmation

Sau mỗi ingest, present 3-5 options cho next step, user pick. Keep session momentum, avoid over-planning, adapt theo interest của user.

**Result:** Complete foundation 7/7 trong 1 session — không phải target ban đầu mà emergent qua iteration.

**Lesson:** **Complete → Options → Pick → Repeat** pattern tốt hơn "plan everything upfront then execute."

---

## ❌ Cái gì chưa work / What didn't work

### 1. Source files > 20KB khó ingest trong 1 pass

README (67KB), Security Guide (27.9KB) phải chunk. Risk: miss content ở chunks sau.

**Evidence:** README phần sau line 600 chưa đọc kỹ → có thể miss updates gần đây trong "What's New" section (older versions).

**Mitigation sai cách:** đọc lines 1-200 rồi stop cho chunks tiếp.
**Mitigation đúng cách:** Lần này nên có strategy rõ ràng — skim full file cho heading structure trước, sau đó focused read theo sections cần.

**For future:** Implement "skim-first" approach — grep headings first, identify priority sections, read those in full, skim rest.

### 2. Entity page #1 (Hooks) retrofit gây technical debt nhỏ

Hooks viết với 11 sections; sau đó retrofit 3 sections mới sau khi pattern stabilize với Subagents (#2). Retrofit tốn ~10 phút.

**Nếu predict được pattern từ đầu:** tiết kiệm retrofit effort.
**Thực tế:** không predict được — cần ít nhất 2 instances để see pattern.

**Lesson:** Accept prototype tax. **2-3 instances cost là reasonable để lock in format.**

### 3. Counts verification prolonged Q2 resolution

Q2 (count discrepancy) raised at ingest #1, chỉ fully resolved at entity #7 (Commands). Qua cả process, add từng số count (agents → skills → commands).

**Alternative:** Verify all 3 counts ngay ingest đầu — tốn 30 giây `ls` commands.

**Lesson:** Khi raise question technical verifiable, **resolve ngay** thay vì defer. 30-second task không đáng defer.

### 4. Không dùng TodoWrite từ đầu

Tool TodoWrite useful cho multi-step tasks nhưng chỉ bắt đầu dùng từ ingest #3 (Longform). 2 ingest đầu không track progress structured.

**Impact:** Minor — vẫn hoàn thành, nhưng mất visibility. User phải trust Claude nhớ đủ steps.

**Lesson:** TodoWrite should start early. Even trivial-seeming tasks benefit from explicit tracking, especially multi-file edits.

### 5. Entity pages không tận dụng codebase search agents

Khi viết entity pages, có thể dispatch Explore agent để tìm additional examples, cross-ref trong codebase. Không làm.

**Impact:** Có thể miss concrete examples trong skills/, scripts/, hooks/ folders.

**Example:** (C) Skills có TODO "đọc `skills/iterative-retrieval/SKILL.md`" chưa làm. Explore agent có thể surface nó tự động.

**For future:** Sau khi tạo entity page, dispatch agent: "Find all references to [concept] in codebase, surface concrete examples we might have missed."

---

## 📋 Patterns & templates khám phá được

### Pattern 1: 13-section canonical entity page format

```
1. One-liner (bilingual)
2. Khi nào dùng / KHÔNG dùng
3. Comparison với sibling concepts (table, 4-5 columns)
4. Sub-types / categorization
5. Anatomy (file/config format) — nếu có
6. Cơ chế / How it works
7. Out-of-box list (ECC ships) — nếu có
8. Configuration / scope
9. Recipes / concrete examples (progressive complexity)
10. Advanced patterns — nếu có
11. Combination patterns (entity A + B)
12. Anti-patterns / Sai lầm hay gặp
13. Cross-refs + Citations + TODO
```

**Sections optional điều kiện:**
- "Case study" — khi entity có instance đặc biệt notable (Skills → continuous-learning v2)
- "Validator quirks" — khi có strict schema (Plugins)
- "Migration matrix" — khi entity đang deprecate (Commands)
- "Real-world examples" — khi có folder `examples/` (Rules/Memory)

**Reusable cho mọi LLM Wiki project sau.**

### Pattern 2: Source summary format (khác entity page)

```
1. TL;DR bilingual
2. Preserve tác giả narrative arc
3. Extract key concepts thành tables/bullets
4. Connection to Storm Bear vault (nếu có overlap)
5. Open questions từ ingest
6. Cross-references
7. Citations với line ranges cụ thể
```

**Key difference vs entity page:** Summary respects source structure; entity page imposes canonical structure.

### Pattern 3: Foundational files từ ingest đầu

Ingest #1 luôn tạo 2 files trong wiki:
- `(C) index.md` — catalog có sections: Sources, Concepts, Entities, Roadmaps
- `(C) log.md` — chronological, format `## [YYYY-MM-DD] type | title` (grep-parseable)

**Don't defer these.** Tạo ngay để mọi ingest sau append vào.

### Pattern 4: "Discrepancy as content"

Khi tìm contradiction giữa 2 sources (README vs changelog, manifest vs filesystem):
- Record trong TODO/open questions
- Verify với filesystem/code
- Promote thành contribution opportunity nếu confirm

**Result:** 4 contribution opportunities identified cho ECC repo chỉ bằng verification careful.

### Pattern 5: Bilingual translation philosophy

**Framework cho future translation work:**

| Content | Keep English | Translate |
|---------|--------------|-----------|
| Technical terms (plugin, hook, API, MCP…) | ✅ | |
| Code blocks | ✅ | |
| URLs, CVE IDs, version numbers | ✅ | |
| File paths | ✅ | |
| Narrative prose | | ✅ |
| Process descriptions | | ✅ |
| Examples (natural language portion) | | ✅ |
| Commands syntax | ✅ | Params có thể translate |

### Pattern 6: Cross-reference forward-declaration

OK to link [[page-not-yet-exists]] với note "_Sẽ link tới khi tạo_". Better than no link. Broken links resolve khi page tiếp được tạo.

**Obsidian advantage:** broken wiki-links show dim/red — visual reminder to create.

---

## 📊 Metrics & numbers

### Session throughput

| Phase | Output | Est. tokens |
|-------|--------|-------------|
| Setup (brain-setup + new-project) | 2 files | ~15K |
| Source summary #1 (README) | 1 summary + index + log | ~20K |
| Source summary #2-4 (trinity) | 3 summaries | ~45K |
| 7 entity pages | 7 files | ~80K |
| Retrofit Hooks | Edit in place | ~3K |
| v1 published guide | 1 file | ~15K |
| VN translation + PR prep | 2 files | ~25K |
| Open questions updates (continuous) | Edits | ~10K |
| **Total** | **17 files** | **~213K tokens output** |

### File size distribution

| File type | Avg lines | Range |
|-----------|-----------|-------|
| Source summary | ~250 | 200-330 |
| Entity page | ~370 | 320-450 |
| Published guide | 500 | — |
| Translation README | 486 | matched Turkish 466 |
| Iteration log (this) | 400 | estimate |

### Throughput estimates (for planning next project)

- **Source summary:** ~15-20 phút (read + summarize + cross-ref)
- **Entity page:** ~20-30 phút (read source + write + cross-ref + update index/log)
- **Entity page với concrete file peek:** +10 phút
- **Published guide:** ~30-40 phút (design structure + write + cross-link)
- **Translation:** ~30-45 phút (~500 lines technical Vietnamese)
- **Retrofit/update after format evolution:** ~10 phút per entity page

### Discrepancies found

- 4 contribution opportunities qua verification
- 2 major (VN translation missing; plugin.json manifest drift)
- 2 minor (rules README count; mgrep benchmark verify)

---

## 🎯 Recommendations cho project sau

### Khi apply LLM Wiki pattern lần tới:

1. **Clone source ngay ingest đầu** — vào `00 Sources/` — separate from wiki work
2. **Create index.md + log.md ngay** — foundation
3. **Skim full source file trước khi read deep** — especially nếu > 20KB. Grep headings.
4. **Verify counts/numbers bằng filesystem** — ngay khi raise question
5. **Start với 2 source summaries trước khi entity pages** — build breadth, sau đó depth
6. **Entity page #1 là prototype** — expect retrofit sau #2-3
7. **Cross-reference mọi page mới** — kể cả forward-declare tới pages chưa tạo
8. **TodoWrite từ đầu** — track multi-step work
9. **Open questions file là deliverable** — cập nhật mỗi ingest, đừng delete questions
10. **Test format: Published guide khác Entity page** — linear vs reference
11. **Ingest philosophy TRƯỚC detail** (security guide trước MCPs entity)
12. **Bilingual decisions explicit** — document trong CLAUDE.md từ đầu

### Khi topic có translation opportunity:

1. **Read 2-3 existing translations** để thấy scope (often partial, not full)
2. **Choose shortest existing translation** làm template (low risk, proven)
3. **Translation philosophy document trước** — tech terms EN vs translate
4. **Banner updates** = nhiều files cần coordinate
5. **PR-INSTRUCTIONS.md với diffs** — reduce friction for user to submit

### Khi topic có security angle:

1. **Đọc security guide TRƯỚC entity pages** về components có security relevance
2. **Integrate security context** thẳng vào entity pages, không bolt-on cross-ref
3. **"Quick wins" section trong published guide** — actionable 15-phút tasks
4. **Minimum bar checklist** = screenshot-able deliverable

---

## 🔁 Pattern áp dụng cho Storm Bear vault context

### Nếu dùng pattern cho project khác trong vault:

**Good candidates cho LLM Wiki treatment:**
- Tech stack deep-dive (vd "Next.js 15 new features complete guide")
- Books / courses (Karpathy's original example)
- Research areas (accumulating sources over time)
- Competitor analysis
- Trip planning / event planning
- Business domain learning (vd "Indie hacker knowledge base")

**Bad candidates:**
- One-off tasks
- Personal journaling (better in `01 Journals/`)
- Quick reference (overkill)
- Topics với limited sources (<5 sources → wiki doesn't compound)

### Threshold cho "đáng build wiki":

- ≥5 sources liên quan
- ≥3 months expected lifespan của topic
- Clear ownership (người maintain)
- Cross-references meaningful (sources talk to each other)

**Under threshold:** keep in `00 Notes/` folder as flat files.

---

## 🧬 Meta-learning: LLM Wiki pattern proof

**Karpathy's hypothesis:** LLM Wiki pattern > RAG for accumulating knowledge.

**Evidence from this project:**

✅ **Knowledge compounds** — each ingest builds on previous (security guide made MCPs entity page better)
✅ **Cross-references emerge naturally** — 14 pages all interconnected
✅ **Contradictions surface** — verification caught 4 discrepancies RAG would miss
✅ **Published output is stronger** — guide references entity pages references summaries references sources
✅ **Human-readable** — can browse wiki like normal docs, không cần query interface

**Cost:**
- More upfront effort than RAG upload
- Requires maintainer (Claude here)
- Only economical when knowledge accumulates over time

**Verdict:** **Pattern proven for this use case.** Storm Bear vault nên áp dụng cho more topics.

---

## 📍 Action items cho Storm Bear vault level

1. **Update root `CLAUDE.md`** với pattern LLM Wiki đã prove — add section "Patterns đã verified work" với reference tới project này
2. **Create skill template** cho LLM Wiki pattern — include 13-section format, open questions, source summary format
3. **Consider writing** vault-level `05 Skills/llm-wiki-ingest.md` để reuse workflow
4. **Update `GOALS.md`** — đánh dấu "ECC mastery" milestone đạt được qua project này; identify next topic
5. **Weekly Update (root CLAUDE.md)** — refresh Week 1 với session này accomplishments

---

## 🔗 Cross-references

- Project CLAUDE.md: `03 Projects/Everything Claude Code - Beginner Analysis/CLAUDE.md`
- Wiki index: `02 Wiki/(C) index.md`
- Wiki log: `02 Wiki/(C) log.md` — session timeline chi tiết
- Published guide: `03 Published/(C) Everything Claude Code - Huong dan cho nguoi moi.md`
- Contribution: `03 Published/contributions/vi-translation/`

---

## Version log

- **v1** (2026-04-17): First iteration log. Captures learnings từ building wiki v1 end-to-end trong 1 session.
- *v1.1 sẽ:* capture feedback từ team sau khi publish guide; update throughput estimates với real team data
- *v2 sẽ:* compare với iteration log của project tiếp theo (meta-learnings)

---

**🤖 Storm Bear iteration log — pattern validation complete.**
