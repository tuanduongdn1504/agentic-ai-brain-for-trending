# mattpocock/skills — Hướng dẫn cho người mới (VN+EN)

> **Subject:** `mattpocock/skills` — Matt Pocock's "Skills For Real Engineers"
> **Tier:** T1 Assistant — opinionated agent-skills bundle for Claude Code / Codex / generic agents
> **License:** MIT (no commercial-use friction)
> **Wiki:** v57 (Storm Bear corpus 57th)

---

## Phần 1 — Đây là gì? / What is it?

**VN:**
mattpocock/skills là bộ sưu tập 13 skill agent (10 engineering + 3 productivity) + 4 misc skill, được Matt Pocock — nhà giáo dục TypeScript nổi tiếng (founder Total TypeScript, ex-Vercel, ex-Stately) — chắt lọc từ thư mục `.claude/` cá nhân của anh ấy. Mục tiêu: giúp lập trình viên dùng AI agent (Claude Code, Codex...) làm "real engineering" — không phải "vibe coding".

13 skill này được thiết kế để: nhỏ gọn + dễ adapt + composable + hoạt động với mọi model AI. Cài đặt qua `npx skills@latest add mattpocock/skills`.

**EN:**
mattpocock/skills is an opinionated curated collection of 13 active agent skills (10 engineering + 3 productivity) + 4 misc, distilled by Matt Pocock — TypeScript educator (founder Total TypeScript, ex-Vercel, ex-Stately) — from his personal `.claude/` directory. Goal: help developers using AI agents (Claude Code, Codex, etc.) do "real engineering" — not "vibe coding."

The 13 skills are designed: small + easy-to-adapt + composable + work-with-any-model. Install via `npx skills@latest add mattpocock/skills`.

---

## Phần 2 — Tín hiệu corpus-first / Corpus-first signals

1. **Citation 3 prior corpus subjects in single README** — Matt cite GSD + BMAD + spec-kit như "anti-pattern foils". Đây là **corpus-first multi-frontend in-corpus reference** trong toàn bộ Storm Bear corpus 57 wiki.
2. **5 named methodology citations** — README cite 4 cuốn sách (Pragmatic Programmer + DDD + Extreme Programming + Philosophy of Software Design) + 1 nhóm anti-pattern. Đây là **methodology-lineage có nhiều book-citation nhất** trong corpus.
3. **3rd skills-collection at T1** — sau awesome-claude-skills (v50) + agent-skills-of-vercel (v51). Sub-variant: **opinionated-curated-by-author** (khác với aggregator-curated v50 + plugin-manifest v51).
4. **Most-explicit anti-vibe positioning** trong corpus — câu mở đầu README: "real engineering — not vibe coding".
5. **62K stars / 66 commits** = velocity-burst extreme-density (>900 stars/commit). Cần probe time-axis tại v60 mini-audit.
6. **40th consecutive Storm Bear meta-entity** với 3 of 4 STRICT criteria PASS — strongest STRICT-amendment instance to date.
7. **21-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES streak** — new longest extending v56 20-streak.

---

## Phần 3 — Tier placement

**T1 Assistant** — install vào Claude Code / Codex / generic agents, hoạt động như invokable primitives trong conversation.

Sub-classification: **opinionated-curated-by-author skills-collection at T1**.

Khác với 2 sibling skills-collections:
- **v50 awesome-claude-skills** — aggregator-curated (community submissions, hàng trăm skills)
- **v51 agent-skills-of-vercel** — plugin-manifest aggregation (24 vendor skills, organized by Vercel)
- **v57 mattpocock/skills** — opinionated-curated-by-author (13+ skills, single-author voice + commercial-educator backing)

---

## Phần 4 — Cài đặt / Installation

### Quickstart 30 giây / 30-second setup

**Bước 1.** Chạy installer:
```bash
npx skills@latest add mattpocock/skills
```

**Bước 2.** Chọn skills bạn muốn + agent target (Claude Code / Codex). **Đặc biệt phải chọn `/setup-matt-pocock-skills`**.

**Bước 3.** Trong agent của bạn, chạy:
```
/setup-matt-pocock-skills
```
Skill này sẽ hỏi:
- Issue tracker bạn dùng (GitHub / Linear / local files)
- Triage labels bạn áp dụng
- Vị trí lưu docs được generate (CONTEXT.md / ADRs)

**Bước 4.** Done. Bắt đầu dùng được.

---

## Phần 5 — Pattern sử dụng cốt lõi / Core usage pattern

### 4 failure modes Matt giải quyết

| # | Vấn đề | Skill sửa |
|---|---|---|
| 1 | "Agent didn't do what I want" (misalignment) | `/grill-me` (non-code) + `/grill-with-docs` (code) |
| 2 | "Agent way too verbose" (no shared vocabulary) | `/grill-with-docs` + CONTEXT.md domain glossary |
| 3 | "Code doesn't work" (no feedback loop) | `/tdd` (red-green-refactor) + `/diagnose` (6-phase debugging) |
| 4 | "Built a ball of mud" (architectural decay) | `/improve-codebase-architecture` + `/zoom-out` + `/to-prd` |

### Workflow điển hình / Typical workflow

```
1. /grill-with-docs <feature description>
   → Agent hỏi bạn relentlessly, build ra CONTEXT.md + ADR
2. /to-prd
   → Synthesize conversation thành PRD GitHub issue
3. /to-issues <PRD>
   → Break PRD thành GitHub issues với vertical slices
4. /tdd <issue>
   → Red-green-refactor cycle: 1 test → 1 implementation → repeat
5. /diagnose (nếu có bug)
   → 6-phase: feedback loop → reproduce → hypothesize → instrument → fix → cleanup
6. /improve-codebase-architecture (định kỳ)
   → Audit deep-modules + ADRs + CONTEXT.md alignment
```

---

## Phần 6 — Khái niệm mới / Novel concepts

### "Grilling session" — phỏng vấn agent ngược

Trong corpus Storm Bear, đây là **convergence pattern thứ 2**: vault `brain-setup.md` (5-round interview) + mattpocock `/grill-me` + `/grill-with-docs` đều là **interview-as-skill primitive**. Hai team độc lập tiến hóa cùng pattern.

### CONTEXT.md = domain glossary

File markdown ở root repo, chứa domain language definitions. Agent đọc CONTEXT.md để **không phải đoán jargon** từ đầu mỗi session. Tiết kiệm tokens + nhất quán naming + agent dễ navigate codebase hơn.

VD từ repo `course-video-manager` của Matt:
- BEFORE: "There's a problem when a lesson inside a section of a course is made 'real'"
- AFTER: "There's a problem with the materialization cascade"

### Vertical-slice TDD (anti-horizontal)

**Anti-pattern:** viết hết tests trước, sau đó implement hết. Matt gọi đây là "horizontal slicing" → produces "crap tests".

**Pattern đúng:** **vertical slice tracer-bullet**:
```
RED → GREEN: test1 → impl1
RED → GREEN: test2 → impl2
...
```
Mỗi test response based on what you learned từ implementation trước.

### Lazy ADR documentation

ADR (Architecture Decision Record) chỉ tạo khi **3 conditions cùng đúng**:
1. Hard to reverse
2. Surprising without rationale
3. Genuinely trade-off-driven

Tránh ADR sprawl. Update inline khi decisions crystallize, không batch.

### Caveman mode

`/caveman` = ultra-compressed communication. Drops articles + filler + pleasantries. Pattern: `[thing] [action] [reason]. [next step].` Cuts ~75% token usage. Useful khi context budget tight.

---

## Phần 7 — vs other corpus frameworks

### vs awesome-claude-skills (v50, sibling skills-collection 1)

| Axis | mattpocock/skills v57 | awesome-claude-skills v50 |
|---|---|---|
| Curation | Opinionated-curated-by-author | Aggregator-curated (community) |
| Scale | 13 active skills | 100s of skills |
| Voice | Single-author | Multi-contributor |
| License | MIT | (varies per submission) |
| Stars | 62K | (significantly fewer) |

### vs agent-skills-of-vercel (v51, sibling skills-collection 2)

| Axis | mattpocock/skills v57 | agent-skills-of-vercel v51 |
|---|---|---|
| Curation | Opinionated-curated-by-author | Plugin-manifest aggregation (vendor) |
| Backing | Solo-commercial-educator | Vercel corporate |
| Scale | 13 active | 24 vendor skills |
| Anti-vibe positioning | Most-explicit in corpus | Implicit (Vercel professional) |

### vs GSD v5 / gsd-2 v54 (cited as anti-pattern foil)

Matt cite GSD = "approach that owns the process". Trong corpus Storm Bear:
- **GSD v5** = solo-individual workflow (Mike author); SDD methodology
- **gsd-2 v54** = gsd-build org 8-repo monorepo + Pi-SDK substrate
- **Mattpocock contrast**: small + composable + author-controlled (NOT process-owning)

### vs BMAD v11 (cited as anti-pattern foil)

BMAD = methodology-feature-framework (Brain + Mind + Action + Decision). Mattpocock ngược lại: **không feature-framework hóa**, từng skill standalone.

### vs spec-kit v17 (cited as anti-pattern foil)

Spec-kit = 9-article-constitution Microsoft-corporate-official SDD. Mattpocock ngược lại: **không có constitution**, không có corporate backing, opinionated-but-unconstrained.

---

## Phần 8 — Ethical framing + supply-chain notes

### MIT license = không commercial-use barrier

Storm Bear (Scrum coach commercial) deploy được mattpocock skills vào client work tự do. Không có giới hạn như n8n SUL hay PolyForm-Noncommercial.

### Commercial-funnel awareness

Matt là commercial educator (Total TypeScript paid course + newsletter ~60K subscribers). README có 1 newsletter CTA. Không phải pure-OSS-pure-altruism — author có commercial interest. Không phải tiêu cực, nhưng **đáng biết** khi đánh giá axis-of-bias.

### Supply-chain risk

LOW. Mỗi skill = single markdown file (no executable code). Installer là shell script với explicit prompts. Tương đương awesome-claude-skills v50 / agent-skills-of-vercel v51 markdown-only pattern.

### Single-author bus-factor

Toàn bộ repo là solo-Matt-Pocock. Không có co-maintainer. Nếu Matt stop maintain, repo có thể stale (giống v55 abandoned-author cautionary). Tuy nhiên: mattpocock/skills hiện đang actively-maintained (62K stars + 16 open issues = author closing actively).

---

## Phần 9 — Storm Bear relevance (VN operator + Scrum coach fit)

### Direct deployable trong daily Storm Bear workflow

- **`/grill-me` + `/grill-with-docs`** — client-discovery sessions (Scrum Coach: project intake interviews)
- **`/tdd`** — software-build practice (Storm Bear là software developer cũng)
- **`/triage`** — backlog management (Scrum Coach: sprint backlog triage)
- **`/to-prd` + `/to-issues`** — sprint-planning artifacts
- **`/improve-codebase-architecture`** — technical-debt audits
- **`/zoom-out`** — strategic-thinking complement (Scrum Coach: retrospective facilitation)
- **`/diagnose`** — debugging methodology (apply to Storm Bear's wiki-build agent-thrash diagnosis từ v56)
- **`/caveman`** — token-economy mode khi context budget tight

### Vault-skill-coherence

Vault `brain-setup.md` (5-round interview) ↔ mattpocock `/grill-me` — **2 independent evolutions của cùng interview-as-skill pattern**. Có thể cross-skill-port: vault `brain-setup-v2.md` extends current 5-round interview với continuous-CONTEXT.md-maintenance discipline borrowed từ `/grill-with-docs`.

### Pattern Library implications

3 promotion candidates emerging post-v57:
1. **Pattern #57 57c-multi-frontend sub-variant** (multi-corpus-citation pattern)
2. **Pattern #18 horizontal-aggregation N=3 promotion candidate** (3 skills-collections at T1 với curation-mechanism sub-variants)
3. **Pattern #19 archetype 4 book-citation-lineage sub-variant** (named-source-via-book vs individual-name)

---

## Phần 10 — Roadmap học 4 tuần / 4-week learning roadmap

### Tuần 1 — Setup + grilling skills

- Cài: `npx skills@latest add mattpocock/skills`
- Thử: `/grill-me` cho 1 personal project plan (non-code)
- Thử: `/grill-with-docs` cho 1 small feature trong code project
- Đọc: README + CONTEXT.md + 4 SKILL.md (grill-me, grill-with-docs, tdd, diagnose)

### Tuần 2 — TDD + diagnose

- Apply `/tdd` vào 1 bug fix nhỏ với red-green-refactor
- Apply `/diagnose` vào 1 hard bug đang stuck
- Compare TDD vertical-slice vs horizontal-slice trong code review

### Tuần 3 — Architecture skills

- Run `/improve-codebase-architecture` trên 1 medium-size codebase
- Run `/zoom-out` để hiểu unfamiliar code
- Update CONTEXT.md với domain language emerging từ codebase

### Tuần 4 — Workflow integration

- Setup `/triage` với GitHub issues hoặc Linear
- Run `/to-prd` từ 1 conversation đã có
- Run `/to-issues` để break PRD thành tickets
- Decide skills nào keep, skills nào drop

---

## Phần 11 — Tradeoffs + limitations

| Tradeoff | Detail |
|---|---|
| **Single-author bias** | Toàn bộ skills phản ánh Matt's preferences (TypeScript-heavy, anti-vibe, anti-process-owning). Có thể không fit team với culture khác. |
| **EN-only** | No VN translations. Storm Bear deploy trực tiếp với VN clients có friction. |
| **Setup-friction** | `/setup-matt-pocock-skills` là interactive prerequisite cho engineering skills. Casual single-skill-grab có friction. |
| **Commercial-funnel awareness** | Newsletter CTA + Total TypeScript commercial brand backing. Author không neutral. |
| **TS-bias** | `migrate-to-shoehorn` là TS-specific. Một số skill implicit assume TS ecosystem. |
| **Process-discipline overhead** | TDD vertical-slice + lazy-ADR + grilling-sessions = overhead nếu small task. Best-fit: medium-large features. |
| **Bus-factor** | Solo-Matt-Pocock. Không có co-maintainer surface. |

---

## Phần 12 — Caveats + safety notes

- **Verify CONTEXT.md commits** — `/grill-with-docs` updates CONTEXT.md inline. Always review diff trước khi commit.
- **`/triage` reads/writes issue tracker** — verify scope of permissions; don't auto-confirm bulk operations.
- **`/git-guardrails-claude-code`** — sets up hooks blocking dangerous git commands. Good practice, nhưng review hooks installed trước khi accept.
- **MIT license requires copyright notice retention** — nếu fork hoặc adapt, retain Matt Pocock copyright.

---

## Phần 13 — References + next action

### Sibling skills-collections trong Storm Bear corpus

- `03 Projects/awesome-claude-skills - Beginner Analysis/` (v50, 1st T1 skills-collection)
- `03 Projects/agent-skills-of-vercel - Beginner Analysis/` (v51, 2nd T1 skills-collection)

### Cited corpus subjects (anti-pattern foils trong README)

- `03 Projects/BMAD-METHOD - Beginner Analysis/` (v11)
- `03 Projects/get-shit-done - Beginner Analysis/` (v5 — GSD original)
- `03 Projects/gsd-2 - Beginner Analysis/` (v54 — GSD successor)
- spec-kit (v17, folder name khác trong `03 Projects/`)

### Vault skills tham khảo

- `05 Skills/brain-setup.md` (vault interview-as-skill, parallel evolution với /grill-me)
- `05 Skills/llm-wiki-routine-v2.1.md` (vault routine; parallel với /to-prd synthesize-conversation)
- `05 Skills/new-project.md` (vault project-scaffolding; parallel với /setup-matt-pocock-skills)

### Next action recommendations

1. **For Storm Bear vault:** evaluate `/grill-with-docs` adaptation cho `brain-setup-v2.md` upgrade
2. **For Storm Bear pilot deployment:** consider mattpocock/skills as Top-3 pilot candidate alongside claude-hud + claude-howto
3. **For next mini-audit (v60):** verify Pattern #52 time-axis (62K stars / 66 commits velocity-density) for un-stale evaluation

---

**End of beginner guide.** ~410 lines. Compressed-scope per v56 lesson; dense single-document coverage.
