# (C) build-your-own-x — Hướng dẫn cho người mới

> Target audience: Developers Việt Nam muốn học programming deep-level thay vì chỉ dùng framework có sẵn
> Reading time: ~25 min
> Language: Bilingual (VN primary, EN technical terms)
> Source: `codecrafters-io/build-your-own-x` (491K stars — top 10 GitHub ever)

---

## Part 1 — build-your-own-x là gì?

### 1.1 Giới thiệu 1 phút

**build-your-own-x** = **491K-star curated aggregator** các tutorials "Build Your Own [X]" — từ build OS, DB, Git, Docker, đến Neural Network, Compiler, Web Browser. 29 categories + Uncategorized catchall. **1 README (46 KB) = toàn bộ content.** CC0 public domain license.

**Philosophy (Feynman):** *"What I cannot create, I do not understand"* — Richard Feynman. **Không học bằng cách đọc docs; học bằng cách build lại.**

**Maintainer:** CodeCrafters, Inc. (company bán paid interactive courses về cùng topics). Originally Daniel Stefanovic.

### 1.2 Khác gì với 7 sibling wikis trong Storm Bear vault?

7 wiki trước đây trong Storm Bear đều về **AI agent frameworks** (ECC, Superpowers, gstack, GSD, goclaw, course, notebooklm-py). **build-your-own-x khác hoàn toàn:**

| Storm Bear 7 wikis | build-your-own-x |
|--------------------|------------------|
| AI agent ecosystem | General programming |
| Build tools | Build fundamentals |
| Use frameworks | Build from scratch |
| Productivity focus | Understanding focus |

**build-your-own-x = meta-reference.** Khác axis, khác purpose. Trong Storm Bear taxonomy này là **"outside scope"** — không fit Tier 1/2/3/4 của agent taxonomy.

### 1.3 Ai nên dùng build-your-own-x?

**Rất phù hợp:**
- Developer senior muốn understand fundamentals deeply
- Engineer chuẩn bị interview (FAANG-style system design)
- Computer Science student học với curriculum loose
- Hobbyist có thời gian + patience để build slow
- Teacher muốn curriculum materials cho students

**Ít phù hợp:**
- Junior dev cần ship nhanh (time constraint)
- Person muốn "AI làm cho tôi" (passive consumption)
- Người chỉ cần overview, không cần implementation
- Stack-specific learner (chỉ học React, chỉ học Django)

**Mix phù hợp:**
- Anyone với 3-6 tháng time investment + genuine curiosity

---

## Part 2 — 29 Categories overview

### 2.1 Systems & low-level (7)
- Operating System — Nand2Tetris level
- Processor — CPU design
- Memory Allocator — malloc/free
- Network Stack — TCP/IP
- Shell — bash-like
- Programming Language — compilers + interpreters (10+ entries, biggest)
- Regex Engine — NFA/DFA

### 2.2 Web + infrastructure (7)
- Web Browser — (hard, rare)
- Web Server — HTTP from scratch
- Front-end Framework — React/Vue reimplementations
- Template Engine — Jinja-like
- Docker — containerization
- Database — 10+ entries (biggest)
- Search Engine — Lucene-like

### 2.3 AI + perception (3)
- AI Model — LLM/transformer from scratch (newer)
- Neural Network — numpy-based
- Visual Recognition — computer vision

### 2.4 Creative + graphics (5)
- Game — Tetris, Minecraft-like
- Voxel Engine — Minecraft rendering
- 3D Renderer — ray tracing
- Physics Engine — rigid body
- Augmented Reality

### 2.5 Developer tools (4)
- Text Editor — Vim-like
- Command-Line Tool
- Git — version control internals
- BitTorrent Client — P2P

### 2.6 Automation + novelty (2)
- Bot — Discord, chat
- Emulator / VM — NES, CHIP-8

### 2.7 Blockchain (1)
- Blockchain / Cryptocurrency

### 2.8 Catchall
- Uncategorized (50+ entries)

---

## Part 3 — Best categories cho different goals

### Goal: Understand computers at hardware-to-software
**Start:** Processor → Memory Allocator → Operating System → Shell → Programming Language

**Time:** 6-12 months (slow, deep)

### Goal: Understand web stack end-to-end
**Start:** Web Server → Web Browser → Front-end Framework → Database → Search Engine

**Time:** 4-8 months

### Goal: Understand AI fundamentals (pre-LLM)
**Start:** Neural Network → Visual Recognition → AI Model

**Time:** 2-4 months

### Goal: Understand developer tools I use daily
**Start:** Git → Shell → Text Editor → Command-Line Tool → Docker

**Time:** 2-4 months (high daily-use value)

### Goal: Creative programming for fun
**Start:** Game → Voxel Engine → 3D Renderer → Physics Engine

**Time:** 3-6 months

### Goal: Interview prep (FAANG system design)
**Start:** Database → Search Engine → Distributed Systems → Web Server

**Time:** 2-3 months, focused

---

## Part 4 — Feynman Philosophy: tại sao "build to understand"

### 4.1 Core quote
> "What I cannot create, I do not understand"
> — Richard Feynman

### 4.2 Passive vs active learning

**Passive (read docs, watch video):**
- Feel understanding
- Can't explain simply
- Knowledge evaporates khi library updates
- Abstract, detached

**Active (build from scratch):**
- Forced to confront every assumption
- Can explain simply (because you built it)
- Understanding persists
- Concrete, embodied

### 4.3 Ví dụ cụ thể

**Read docs about B-trees:**
- "B-trees are fast for lookups"
- "They're used in databases"
- Done. Move on.

**Build your own B-tree:**
- Why O(log N)? → because branching factor 100+
- Why not simpler tree? → disk page size 4KB matters
- Why not hash map? → range queries need order
- What breaks? → node splits + merges non-trivial
- → **Deep understanding** that persists

### 4.4 Khi Feynman approach ĐÚNG

- Long time investment acceptable
- Learning = goal (not shipping product)
- Deep understanding matters (interview, teaching)
- Curiosity high

### 4.5 Khi Feynman approach SAI

- Production pressure (ship now)
- Using commodity tech (HTTP client — use `requests`)
- Fast-changing frameworks (React API shifts yearly)
- Team standardized on specific stack

---

## Part 5 — So sánh với 7 siblings + Storm Bear positioning

### 5.1 Positioning matrix

| Project | Tier trong agent taxonomy | Verb | When use |
|---------|--------------------------|------|----------|
| **build-your-own-x** | **OUTSIDE TAXONOMY (meta-reference)** | **Study** | **Pre-career / interview / depth** |
| ECC | T1 (Assistant) | Use | Daily coding với Claude Code |
| Superpowers | T1 | Use | Methodology + TDD |
| gstack | T1 | Use | Specialist roles |
| GSD | T1 | Use | Context rot + 14 harnesses |
| goclaw | T2 (Service) | Deploy | Multi-tenant platform |
| ai-agents-for-beginners | T3 (Education) | Learn | Agent concepts curriculum |
| notebooklm-py | T4 (Bridge) | Integrate | NotebookLM automation |

### 5.2 Complementary, not competitive

**build-your-own-x doesn't replace agent frameworks.** Different layer:
- **Agent frameworks** → tooling daily productivity
- **build-your-own-x** → understanding foundations

**A senior engineer uses both.** Uses Claude Code (T1) daily AND revisits build-your-own-x for depth when needed.

### 5.3 Learning path comparison

**Agent framework learning:**
1. ai-agents-for-beginners (T3 course) → concepts
2. Pick T1 tool → productivity
3. T4 bridges → integrations
4. T2 platform → scale

**build-your-own-x learning:**
1. Pick category (Database?)
2. Pick tutorial (in your language?)
3. Type code yourself
4. Understand by building

**Different axis.** Orthogonal. Do both over career.

---

## Part 6 — Lộ trình 3-tháng / 3-month roadmap

### Approach: "1 category per month, deep"

### Month 1: Git
**Why Git first:** Daily tool, clear scope, good tutorials.

- Week 1: Read 2-3 "build your own Git" tutorials, pick one aligned với your language
- Week 2-3: Implement commits + branches từ scratch
- Week 4: Add diff + merge

**Deliverable:** Your own toy Git in ~500 lines. Understand hashes, trees, refs.

### Month 2: Database
**Why Database next:** Foundation of web apps.

- Week 1: Pick "build your own SQLite" or "build your own Redis" tutorial
- Week 2: Implement storage layer
- Week 3: Implement query engine
- Week 4: Implement indexes (B-tree!)

**Deliverable:** Your own key-value store hoặc SQL engine. Understand B-trees, transactions, query planning.

### Month 3: Programming Language
**Why Compilers next:** Most profound "aha" experience.

- Week 1: Pick "build your own Lisp" or "build your own calculator" tutorial
- Week 2: Implement lexer + parser
- Week 3: Implement evaluator
- Week 4: Add features (functions, closures)

**Deliverable:** Your own toy language. Understand AST, evaluation, scoping.

### After 3 months
You've built 3 fundamental systems from scratch. Understanding = deep. Can explain to Scrum team what DB indexes actually DO.

---

## Part 7 — Tips và pitfalls

### 7.1 Tips cho Vietnamese developer

1. **Đừng sợ tutorial tiếng Anh** — programming English tương đối đơn giản, đọc lâu thành quen
2. **Chọn tutorial language quen thuộc** — nếu bạn biết Python, tìm Python-based tutorial
3. **Không lo chậm** — Feynman approach SLOW by design
4. **Team retro discussion** — build-your-own-X làm topic thú vị cho 1-on-1
5. **Kết hợp LLM hỗ trợ** — dùng Claude explain concepts khó, NHƯNG vẫn tự type code

### 7.2 Pitfalls tránh

1. **Copy-paste without understanding** — đặc biệt khi dùng AI, mất hết value
2. **Skip chapters vội** — mỗi chapter xây trên trước; skip = lose context
3. **Only read, no code** — Feynman test fail
4. **Expect production-quality** — tutorial versions = toy; real systems much harder
5. **Yak-shaving** — 6 months build your own Git, never ship real product → balance

### 7.3 Khi nên dừng tutorial

- **Hiểu core concept đã** — không cần complete all features
- **Gets tedious** — find better tutorial
- **Prerequisites missing** — stop, build prereq first
- **Tutorial broken** — links dead, code doesn't run → find alternative

---

## Part 8 — build-your-own-x + Storm Bear synergy

### 8.1 Cvtot's Scrum coaching application

**Scrum team retrospective topic:** "What did we NOT understand last sprint?"

Use build-your-own-x tutorials as learning nuggets:
- Team uses Git daily → suggests "build your own Git" study group
- Team DB issues → "build your own DB" for better troubleshooting
- Team CI/CD mysteries → "build your own Docker" demystifies

**Builds team's depth-knowledge.** Better Scrum coach has team members who understand tools deeply.

### 8.2 Cvtot's personal growth

Storm Bear vault already has 7 agent wikis. build-your-own-x complements:
- **Morning:** Agent wiki for daily productivity (use)
- **Evening/weekend:** build-your-own-x tutorial (understand)
- **Over career:** deep foundation + current tooling

### 8.3 Vault architecture lessons

build-your-own-x's **491K-star aggregator model** = reference pattern for Storm Bear growth:
- Flat README index possible for vault projects
- CC0 license for content
- Curator voice preservation
- Community contribution flow if opens to team

→ **See [[(C) Storm Bear Vault — Knowledge Architecture Lessons]] entity page** for detailed vault lessons.

---

## Part 9 — Next steps

### 9.1 Sau hướng dẫn này

**Option 1 — Start 1 tutorial this week:**
Pick category aligned với current work. Commit 1 hour/day for month.

**Option 2 — Team retro incorporation:**
Propose team studies "build your own Git" together over 4 weeks. Bond + learn.

**Option 3 — Contribution back:**
- Translate build-your-own-x README into Vietnamese → PR
- Submit Vietnamese-authored "build your own X" tutorial
- Share Storm Bear vault lessons as English blog post

**Option 4 — Integrate into Storm Bear vault:**
Flat aggregator INDEX.md in `03 Projects/` following build-your-own-x model.

### 9.2 Related Storm Bear vault reading

- `../../../05 Skills/llm-wiki-routine.md` — routine pattern
- [[(C) Storm Bear Vault — Knowledge Architecture Lessons]] — meta lessons
- Taxonomy v7 (4-tier): `../../notebooklm-py - Beginner Analysis/03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge.md`

---

## Tóm tắt / Summary

**build-your-own-x = 491K-star Feynman-philosophy aggregator.** 29 categories curated by CodeCrafters Inc. Outside Storm Bear's agent taxonomy — different axis (understanding fundamentals, not productivity).

**Khi dùng:** Deep understanding goals (interview prep, teaching, curiosity, Scrum coaching team development).

**Khi không dùng:** Production pressure, commodity tech, fast shipping.

**Cross-pollination với Storm Bear:** Complement daily agent framework work. Knowledge organization lessons applicable to vault architecture.

**Next:** Start 1 tutorial (Git recommended first). Commit month. Report back.

---

## Cross-references

- Main vault: `../../../CLAUDE.md`
- Goals: `../../../GOALS.md`
- Routine: `../../../05 Skills/llm-wiki-routine.md`
- Wiki entities this project:
  - [[../02 Wiki/(C) 29 Categories Taxonomy]]
  - [[../02 Wiki/(C) Feynman Philosophy Applied to Learning]]
  - [[../02 Wiki/(C) Curation Model]]
  - [[../02 Wiki/(C) Storm Bear Vault — Knowledge Architecture Lessons]]
- Taxonomy v7 (4-tier, for context): `../../notebooklm-py - Beginner Analysis/03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge.md`
- Meta-reference (this wiki): [[(C) Meta-reference — Storm Bear vault architecture lessons]]
