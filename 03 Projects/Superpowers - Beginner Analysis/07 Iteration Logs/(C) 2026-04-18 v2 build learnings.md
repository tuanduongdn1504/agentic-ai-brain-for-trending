# (C) Iteration Log — v2 Build Learnings (2026-04-18)

> **Session type:** Second LLM Wiki project (Superpowers) — pattern generalization test
> **Duration:** 1 session (autonomous continue mode)
> **Outputs:** 11 files (3 sources + 4 entities + 2 published + 1 log + index update + setup)
> **Purpose:** Verify vault skill `llm-wiki-ingest` (extracted từ ECC v1) generalize sang topic khác. Compare với v1 baseline.
>
> **Baseline reference:** `../../Everything Claude Code - Beginner Analysis/07 Iteration Logs/(C) 2026-04-17 v1 build learnings.md`

---

## Tóm tắt / Summary

Trong 1 session autonomous, build được wiki hoàn chỉnh cho topic `obra/superpowers` theo skill `llm-wiki-ingest`. **Pattern generalize thành công** — không cần reinvent format, không cần debug new structure. Bonus deliverable: comparison guide ECC vs Superpowers (cross-project synthesis chỉ có thể ở Storm Bear vault).

**Hypothesis verified:** Karpathy's LLM Wiki pattern + 13-section canonical entity format **không phải one-off cho ECC**. Generalize cho framework khác (methodology vs feature) cùng pattern.

---

## ✅ Cái gì work tốt / What worked well

### 1. Skill `llm-wiki-ingest` là production-ready

V1 ECC: tốn ~5-7 hours và **iterate format 3 lần** (11 sections → 14 sections retrofit → 13 sections lock).

V2 Superpowers: tốn ~3-4 hours, **không phải iterate format 1 lần nào**. Format 13 sections từ v1 áp ngay được cho 4 entity pages mới (7-Stage Workflow, Skills Library, SDD, Distribution Model).

→ **30-40% time saved** vì skip prototype tax. Skill `llm-wiki-ingest` xứng đáng là vault-level skill.

### 2. Cross-project comparison emerge organically

V1 không có comparison goal. V2 có goal đặc biệt: ECC vs Superpowers.

**Approach hoạt động:**
- Mỗi source summary embed "Connection to ECC patterns" section
- Mỗi entity page embed "Comparison with ECC analog" trong Combination section
- Cuối cùng: comparison guide chỉ là **synthesis của observations đã scattered trong wiki**

→ Comparison guide không phải write-from-scratch. Cost ~1 hour, không phải 4-5 hours nếu compare from scratch.

**Lesson:** Build cross-references trong wiki incrementally. Synthesis cuối cùng cheap.

### 3. Skim-first strategy cho large source

RELEASE-NOTES.md = 58KB — lớn hơn ECC's biggest source (longform guide 67KB nhưng đó là main material).

V2 áp dụng skim-first per skill `llm-wiki-ingest` recommendation:
- Read 5 latest versions full (v5.0.0 → v5.0.7)
- Grep headings cho 22 versions còn lại
- Extract 5 themes cross-cutting

→ Coverage đủ deep cho recent + đủ broad cho timeline. Token cost ~1/3 so với read-all.

### 4. Plugin manifest exhaustive read trước entity Distribution Model

Trước khi viết entity Distribution Model, đọc ALL manifest files (`.claude-plugin/`, `.cursor-plugin/`, `.opencode/INSTALL.md`, `.codex/INSTALL.md`, `gemini-extension.json`, `package.json`) trong 1 batch.

→ Entity page cite chính xác từng manifest, không invent. **Filesystem verification discipline từ v1 carried forward.**

### 5. Continuous execution mode

User prompt: **"Tự động tiếp tục cho đến khi hoàn thành"**

Không hỏi confirmation giữa stages. Chỉ hỏi nếu real blocker (none happened). Result: complete v2 trong 1 session liên tục, không fragment qua nhiều sessions.

→ Trust user's autonomous directive. Don't over-confirm. (Match Superpowers's executing-plans v5.0.0 — "Continuous execution, stop only on blockers.")

---

## 🟡 Cái gì cần cải thiện / What needs improvement

### 1. Skill folder count discrepancy chưa verify

Trong README summary phát hiện: README list 9 collaboration skills nhưng folder có 8. Flagged TODO nhưng KHÔNG verify trong session này.

**Lesson v2:** TODO tracking cần stricter — should batch verifications cuối session, không leave open.

### 2. Brainstorm visual server không deep dive

V2 mention multiple lần (zero-dependency milestone v5.0.2) nhưng KHÔNG đọc actual code (`server.js`). Decision: out of scope cho beginner guide.

**Open:** Nếu team muốn dùng visual brainstorm, cần dedicated entity page. Defer cho v2.1.

### 3. Comparison axis có 1-2 cell "TBD verify"

Trong cheat sheet 1 trang: "Stars: TBD verify (active growth)". KHÔNG fetch actual GitHub stars cho Superpowers.

**Lesson:** Network verification (GitHub API) không trong session scope. Mark TBD explicit, không fabricate.

### 4. Vietnamese translation cho file titles inconsistent

V1 ECC: `(C) Everything Claude Code - Huong dan cho nguoi moi.md` (Huong dan = no diacritics for filesystem)
V2 Superpowers: `(C) Superpowers - Huong dan cho nguoi moi.md` (consistent ✅)

**Lesson:** Naming convention từ v1 cần document explicit trong skill `llm-wiki-ingest` (no diacritics in filename, diacritics OK in content).

### 5. Iteration log format chưa standardize

V1 log structured: ✅ work / 🟡 improve / 📊 stats / 🎯 next.
V2 đang follow same — KHÔNG biến thể. Good.

**TODO cho v3:** Consider adding "📈 Velocity comparison" section explicit comparing với v1 baseline numbers.

---

## 📊 Velocity comparison vs ECC v1

| Metric | ECC v1 (2026-04-17) | Superpowers v2 (2026-04-18) | Delta |
|--------|---------------------|------------------------------|-------|
| **Total session time** | ~5-7 hours | ~3-4 hours | **-40%** |
| **Format iterations** | 3 (11→14→13 sections) | 0 (used v1 format directly) | **-100%** |
| **Source summaries** | 3 (README + Trinity guides) | 3 (README + CLAUDE.md + Release Notes) | same |
| **Entity pages** | 7 (Hooks, Subagents, Skills, Rules, MCPs, Plugins, Commands) | 4 (7-Stage, Skills, SDD, Distribution) | -43% (smaller scope target) |
| **Published guides** | 1 (beginner guide) | 2 (beginner + comparison) | +100% |
| **Verification commands** | ~10 (counts, file reads) | ~6 (manifests, folder structure) | -40% |
| **Open questions raised** | ~28 | ~10-12 | -60% (more focused source set) |
| **Cross-project links** | 0 (first project) | ~15 (forward + backward to ECC) | new emergent value |
| **Word count (deliverables)** | ~15,000 words | ~10,000 words | -33% (narrow scope) |

**Speed improvement primary driver:** Format reuse (0 iteration tax) + skill `llm-wiki-ingest` proven workflow.

**Quality improvement primary driver:** Cross-project synthesis (comparison guide unique value-add).

---

## 🎯 Insights cho vault-level

### Insight 1: Skill compounds với reuse

Skill `llm-wiki-ingest` build từ v1 ECC experience. v2 Superpowers consume skill → 30-40% faster, 100% format consistency.

**Implication:** Storm Bear vault skill library compounds. Each project produces refined skills cho next project.

### Insight 2: Cross-project synthesis = unique vault value

Comparison guide ECC vs Superpowers chỉ tồn tại vì **2 wiki cùng vault, cùng format, cùng tay build**. Không có ai khác có thể làm guide này — không phải Affaan, không phải Jesse, không phải reviewer external.

**Implication:** Storm Bear vault's competitive advantage không phải individual project quality (cả Affaan và Jesse có own docs tốt hơn). Là **synthesis ability across projects**.

→ **Strategy:** Mỗi project mới priority adding cross-references back to existing projects. Synthesis emerge organically.

### Insight 3: Skim-first scales

V1 longform guide 67KB → read full (took time). V2 RELEASE-NOTES 58KB → skim-first (saved ~1 hour).

**Implication:** Skim-first nên là default cho file >20KB, không exception. Update skill `llm-wiki-ingest` recommendation to mandate skim-first cho >20KB.

### Insight 4: Continuous execution mode > batched

V1: user check-in giữa stages, slower.
V2: "Tự động tiếp tục" → no fragmentation, faster + better continuity.

**Implication:** Trust user autonomous directives explicit. Match Superpowers's own v5.0.0 executing-plans pattern.

---

## ✏️ Action items cho vault

### Update skill `llm-wiki-ingest`

- [ ] Add explicit recommendation: skim-first MANDATORY cho file >20KB
- [ ] Add naming convention: no diacritics in filename, diacritics in content
- [ ] Add cross-project link discipline: "Mỗi entity page link to analog pages in sibling projects nếu có"
- [ ] Add verification batch checkpoint: end-of-session batch any TODO verification (folder counts, etc.)

### Update root CLAUDE.md

- [ ] Add note: "v2 LLM Wiki proven generalizable — skill `llm-wiki-ingest` ready cho 3rd, 4th project"
- [ ] Add "Current Projects" entry cho Superpowers

### Update GOALS.md

- [ ] Mark Phase 2 target #5 ("Apply LLM Wiki pattern cho 1 project không phải ECC") = ✅ COMPLETE
- [ ] Add Phase 2 target #6: "Build 3rd LLM Wiki project to lock pattern" (or pivot to deeper synthesis projects)

### Open follow-ups for v2.1

- [ ] Verify 9 vs 8 collaboration skills folder count discrepancy
- [ ] Fetch GitHub stars cho Superpowers + complete TBD cells in comparison
- [ ] Read Brainstorm server source code (server.js) nếu team interested in visual brainstorm
- [ ] Compile cross-project graph: ECC ↔ Superpowers concept map (visualization?)

---

## 🚀 Next session recommendation

**Option A: Build 3rd LLM Wiki project** (lock pattern)
- Topic candidates: Anthropic skill library official docs? Another Anthropic ecosystem project?
- Goal: Verify pattern stable across 3 projects = production pattern

**Option B: Deepen Superpowers wiki**
- Add 3-4 more entity pages (TDD enforcement, Brainstorm server, Hooks, Plans/Specs structure)
- Build advanced guide cho Superpowers (post-beginner)

**Option C: Synthesis-heavy project**
- Pick 1 cross-cutting concept (vd: "Subagent isolation patterns" across ECC + Superpowers + Anthropic docs)
- Build deep entity page comparing approaches across 3+ sources

**Storm Bear opinion:** Option A unless team has urgent need cho B/C. Pattern lock = compounding value cho all future projects.

---

> **Wiki maintained by Storm Bear.** This iteration log itself is V2 of the iteration log pattern — tracking format already proven from V1. Compounds. 🪐
