# Skill: LLM Wiki Routine — PUBLIC-ARCHIVED (2026-04-29)

⚠️ **THIS SKILL IS SUPERSEDED.** Use the current version instead:
→ `05 Skills/llm-wiki-routine-v2.1.md`

This file is preserved as a historical record of skill evolution. DO NOT modify. DO NOT use in production. For current routine see `llm-wiki-routine-v2.1.md`. For evolution rationale see `05 Skills/SKILL_LOCK_POLICY.md`.

---

# Skill: LLM Wiki Routine (v1 — historical)

> **Type:** Orchestration meta-skill (Routine pattern)
> **Codified:** 2026-04-18, dựa trên 2 thành công verified: ECC v1 (2026-04-17) + Superpowers v2 (2026-04-18)
> **Parent skill:** `llm-wiki-ingest.md` (methodology — đọc khi cần detail từng phase)
> **Sibling skills:** `new-project.md` (scaffolding), `weekly-update.md`

---

## What this Routine does

**1 input → full LLM Wiki project shipped trong 1 autonomous session.**

User chỉ cần cung cấp **source URL** (repo Github / docs URL / topic name). Routine tự handle:

1. Pre-flight threshold check
2. Project scaffolding (skill `new-project` automated)
3. Source ingestion + summaries
4. Entity pages (13-section format)
5. Published beginner guide (bilingual)
6. Cross-project comparison (auto-detect siblings)
7. Iteration log + vault file updates
8. Velocity comparison vs baselines

**KHÔNG hỏi interview questions.** Routine assumes autonomous mode — proven faster + better continuity (Superpowers v2 insight).

---

## When to invoke

User nói bất kỳ câu nào kiểu:

- "Build LLM Wiki cho `<URL>`"
- "Routine cho `<topic>`"
- "Run wiki routine on `<repo>`"
- "Tạo wiki cho `<topic>`"

→ Invoke routine NGAY. Không clarification questions trừ khi URL/topic ambiguous.

**KHÔNG invoke khi:**
- User chỉ muốn note đơn giản (`00 Notes/` flat file)
- Topic fail threshold (xem Phase 0 below)
- User explicitly nói "interview mode" hoặc "ask me first"

---

## Routine inputs (minimal)

| Input | Required? | Default |
|-------|-----------|---------|
| **Source URL hoặc topic name** | ✅ YES | n/a |
| Project name override | ❌ No | Auto-derive từ repo name + " - Beginner Analysis" |
| Bilingual? | ❌ No | YES (VN primary, EN technical terms) |
| Comparison cross-project? | ❌ No | AUTO-DETECT (xem Phase 4b logic) |
| Skim threshold | ❌ No | 20KB (>20KB → skim-first per llm-wiki-ingest skill) |

→ Single argument workflow. Defaults proven across 2 projects.

---

## Routine workflow (7 phases)

### Phase 0: Pre-flight (1 phút)

**0.1 Verify URL accessible** + repo có content thật:
```bash
# Quick probe (không clone full)
git ls-remote <URL> 2>&1 | head -3
```

**0.2 Threshold check (silent — Routine decides, không hỏi user):**
- Repo size >100KB hoặc ≥10 .md files → ✅ proceed
- Repo nhỏ (<50KB, <5 .md) → flag warning trong response, propose flat file thay vì full wiki
- 404 hoặc empty → STOP + report

**0.3 Sibling project detection:**
```bash
ls "/Users/Cvtot/KJ OS Template/03 Projects/" | grep -i "Beginner Analysis"
```
→ Nếu có ≥1 sibling project trong same domain (vd: AI tooling, dev framework), enable Phase 4b cross-project comparison.

### Phase 1: Scaffold (3-5 phút)

**1.1 Project name:** Auto-derive từ repo URL.
- `https://github.com/<owner>/<repo>` → `<repo> - Beginner Analysis` (capitalize)
- Vd: `garrytan/gstack` → `gstack - Beginner Analysis`

**1.2 Duplicate template:**
```bash
cp -R "03 Projects/(PROJECT TEMPLATE)" "03 Projects/<project-name>"
```

**1.3 Cleanup template artifacts** (per skill `new-project`):
- Remove `00 Duplicate/` folder
- Remove placeholder `CLAUDE.md`

**1.4 Create folder structure cho LLM Wiki:**
```
00 Sources/    01 Analysis/    02 Wiki/    03 Published/
04 System/     05 Skills/      06 Attachments/    07 Iteration Logs/
```

**1.5 Clone source:**
```bash
cd "03 Projects/<project>/00 Sources" && git clone <URL>
```

**1.6 Write CLAUDE.md** — populate từ template, fill in:
- Topic name, source URL, owner attribution
- Prime directive (anti-drift): "outcome là wiki + beginner guide; quay lại nếu drift"
- Folder structure block
- Rules block (`(C)` prefix, bilingual, source fidelity)
- Initial expected milestones checklist (Phases 1-5)

**1.7 Write COMMANDS.md** — point to vault skill `llm-wiki-routine` (this skill) + `llm-wiki-ingest` (parent).

**1.8 Write 3 foundational wiki files** (per llm-wiki-ingest 1.5):
- `02 Wiki/(C) index.md` (catalog template)
- `02 Wiki/(C) log.md` (timeline append-only)
- `01 Analysis/(C) open questions.md` (template)

**1.9 Initial repo survey** (run + log to `(C) log.md`):
```bash
find <source>/ -name "*.md" -not -path "*/.git/*" | wc -l
du -sh <source>/
ls <source>/  # top-level structure
wc -l <source>/README.md
```

→ Phase 1 complete. Update `(C) log.md` với survey numbers.

### Phase 2: Source ingestion (45-60 phút target, scale với repo size)

**Target: 3 source summaries** (proven sweet spot từ ECC + Superpowers).

**Source selection logic:**
1. README.md → ALWAYS source #1 (foundational)
2. CLAUDE.md / AGENTS.md / contribution doc → source #2 (philosophy/culture)
3. CHANGELOG / RELEASE-NOTES / docs/index → source #3 (timeline + state)

**Nếu repo không có CLAUDE.md/CHANGELOG:**
- Substitute với main docs từ `docs/` folder hoặc top-cited file
- Substitute với architecture/design doc

**Per source:**
- File <20KB → full read
- File >20KB → **skim-first MANDATORY** (read TOC + headings + 5 most-recent sections)
- Write `(C) <source-name> summary.md` với:
  - TL;DR bilingual (VN + EN)
  - Skim coverage note (nếu skim-first)
  - Key insights extracted
  - "Connection to sibling projects" section (nếu có sibling — link cross-project)
  - Open questions raised

**Update `(C) log.md`** sau mỗi source. Update `(C) index.md` Sources table.

### Phase 3: Entity pages (2-3 hours target)

**Target: 3-5 entity pages** cho main building blocks của topic.

**Entity selection:** Identify từ source summaries — concepts xuất hiện ≥2 sources và đáng deep dive.

**Format: 13-section canonical** (per skill `llm-wiki-ingest.md`):
1. One-liner
2. Khi nào dùng concept này
3. Comparison sibling
4. Sub-types
5. Anatomy
6. Cơ chế
7. Out-of-box
8. Configuration
9. Recipes
10. Advanced
11. Combination với building blocks khác
12. Anti-patterns
13. Cross-references + Citations + TODO

**Cross-project links MANDATORY** — mỗi entity page reference analog trong sibling projects nếu có.

**Update `(C) index.md`** Entities table sau mỗi page.

### Phase 4a: Beginner published guide (30-45 phút)

**Output:** `03 Published/(C) <Topic> - Huong dan cho nguoi moi.md`

**Filename rule:** No diacritics in filename, diacritics OK in content.

**Structure (parallel ECC + Superpowers v1):**
- Header với metadata (author, source, date, version, bilingual note)
- Mục lục
- Tại sao đọc cái này (audience + outcomes)
- Part 1: Topic là gì (overview)
- Part 2-N: Building blocks deep (1 part per major entity)
- Part X: Setup roadmap (2-week cho narrow topic, 4-week cho broad)
- Part X+1: FAQ
- Part X+2: Resources & References

**Length target:** ~400-500 lines. Bilingual (VN primary).

### Phase 4b: Cross-project comparison guide (40-50 phút) — CONDITIONAL

**Trigger:** Run only nếu Phase 0.3 detected sibling project trong same domain.

**Output:** `03 Published/(C) <Topic> vs <Sibling> comparison.md`

**Structure (parallel ECC vs Superpowers comparison):**
- TL;DR — chọn cái nào trong 30 giây
- Cheat sheet 1 trang (axis comparison table)
- Bản chất khác biệt (philosophy contrast)
- 10-12 axis comparison detail
- Use case decision tree
- Khi nào dùng cả 2
- Migration paths
- FAQ chọn framework

→ Đây là **unique vault value** — không reproducible elsewhere.

**Skip Phase 4b nếu** không có sibling — leave note trong index về future synthesis opportunity.

### Phase 5: Iteration log (15-20 phút)

**Output:** `07 Iteration Logs/(C) YYYY-MM-DD vN build learnings.md`

**N = sequential version number** (v1 = first wiki ever, v2 = second, etc.)

**Sections:**
- Tóm tắt
- ✅ What worked
- 🟡 What to improve
- 📊 Velocity comparison vs previous baselines (bảng)
- 🎯 Insights cho vault-level
- ✏️ Action items cho vault (skill updates, root files updates)
- 🚀 Next session recommendation (Option A/B/C)

### Phase 6: Vault file updates (5-10 phút)

**6.1 Update root `CLAUDE.md`:**
- Add new project entry trong "Current Projects & Overviews" section
- Status: ✅ v1 shipped (or vN), bullet deliverables, link to project folder

**6.2 Update `GOALS.md`:**
- Add milestone entry trong "Milestones Achieved" section
- Update "Folder Structure" tree nếu cần
- Update version log

**6.3 Update project's `(C) index.md`:**
- Mark all phases ✅ COMPLETE
- Reflect final deliverables count

**6.4 Update project's `(C) log.md`:**
- Append final entry: "All phases complete, vN shipped"

---

## Routine completion criteria

Routine reports DONE chỉ khi tất cả checklist:

- [ ] Phase 0 pre-flight passed
- [ ] Phase 1 scaffold complete (project folder + 8 numbered subfolders + foundational files)
- [ ] Phase 2 ≥3 source summaries
- [ ] Phase 3 ≥3 entity pages (13-section format)
- [ ] Phase 4a beginner guide shipped (~400+ lines)
- [ ] Phase 4b comparison guide shipped (nếu sibling detected)
- [ ] Phase 5 iteration log written
- [ ] Phase 6 vault file updates pushed
- [ ] Final report tới user với deliverable count + velocity numbers + next action

---

## Status protocol (per Superpowers SDD pattern)

Routine có thể return 1 trong 4 status mid-execution:

- **DONE** — tất cả phases complete, no concerns
- **DONE_WITH_CONCERNS** — complete nhưng flag issues (vd: source repo có inconsistencies, comparison guide skip vì no sibling)
- **BLOCKED** — không tự giải quyết được, cần human input (vd: URL inaccessible, license unclear, threshold fail nhưng user muốn force)
- **NEEDS_CONTEXT** — cần thêm info để tiếp tục (vd: sibling detection ambiguous, multiple comparison candidates)

→ Match Superpowers's structured status protocol từ `02 Wiki/(C) Subagent-Driven Development.md`.

---

## Defaults (proven, không cần ask)

| Default | Value | Source of evidence |
|---------|-------|--------------------|
| Bilingual | VN primary, EN technical terms | ECC v1 + Superpowers v2 |
| Format | 13-section canonical | `llm-wiki-ingest.md` |
| Source target | 3 summaries | ECC + Superpowers |
| Entity target | 3-5 pages | Adjustable theo topic complexity |
| Continuous execution | YES — không check-in giữa phases | Superpowers v2 insight |
| Skim-first threshold | 20KB | `llm-wiki-ingest.md` |
| Filename diacritics | NO | v2 lesson |
| Cross-project links | MANDATORY khi có sibling | v2 lesson |
| Verification | Filesystem `ls`/`wc -l` cho counts | v1 lesson |
| Context isolation | Spawn subagents cho large research nếu cần | Superpowers SDD pattern |

---

## Velocity targets (per project complexity)

| Repo size | Phase 2 time | Phase 3 entities | Total session | Reference |
|-----------|--------------|------------------|---------------|-----------|
| Small (<50KB, <10 .md) | 30 phút | 3 pages | 2-3 hours | New baseline |
| Medium (50-200KB, 10-50 .md) | 45-60 phút | 4 pages | 3-4 hours | Superpowers v2 (140KB) |
| Large (>200KB, >50 .md) | 60-90 phút | 5-7 pages | 5-7 hours | ECC v1 (broad scope) |

→ Track actual vs target trong iteration log Phase 5.

---

## Anti-patterns

❌ **Hỏi interview questions** — routine designed autonomous. Nếu user muốn interview, dùng skill `llm-wiki-ingest` thẳng.

❌ **Skip Phase 5 iteration log** — log là cách skill compounds. Skip = lose pattern improvement evidence.

❌ **Skip vault file updates (Phase 6)** — root `CLAUDE.md` + `GOALS.md` đồng bộ là invariant.

❌ **Fabricate counts/numbers** — luôn verify bằng `ls`/`wc -l` filesystem commands.

❌ **Skip cross-project links khi có sibling** — đó là unique vault value.

❌ **Run trên topic fail threshold mà không warn** — degrade flat file đề xuất, không silent skip.

❌ **Continuous execution = skip verification** — continuous nghĩa không hỏi check-in, KHÔNG nghĩa skip filesystem verify.

---

## Cross-references

- Parent skill: `llm-wiki-ingest.md` — methodology detail từng phase
- Sibling skills: `new-project.md`, `brain-setup.md`, `weekly-update.md`
- Pattern evidence:
  - `03 Projects/Everything Claude Code - Beginner Analysis/07 Iteration Logs/(C) 2026-04-17 v1 build learnings.md`
  - `03 Projects/Superpowers - Beginner Analysis/07 Iteration Logs/(C) 2026-04-18 v2 build learnings.md`
- Comparison guide template: `03 Projects/Superpowers - Beginner Analysis/03 Published/(C) ECC vs Superpowers comparison.md`
- Beginner guide template: `03 Projects/Superpowers - Beginner Analysis/03 Published/(C) Superpowers - Huong dan cho nguoi moi.md`

---

## Version log

- **v1** (2026-04-18): First codification. Auto-execute baseline = `garrytan/gstack` (project #3 Storm Bear vault). Will refine sau khi v3 ship để verify routine tự nó generalize.
