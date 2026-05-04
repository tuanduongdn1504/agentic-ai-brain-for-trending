# (C) BMAD-METHOD — Hướng dẫn cho người mới (bilingual VN/EN)

> **Target audience:** VN-speaking developers + Scrum coaches exploring AI-driven development frameworks.
> **Sources:** [[../02 Wiki/(C) index]] + 4 entity pages + 3 source summaries
> **Estimated read time:** 25-30 phút
> **Bilingual convention:** VN primary, EN cho technical terms

---

## Part 1 — BMAD là gì? / What is BMAD?

**BMAD-METHOD** là một framework open-source cho **Agile AI-Driven Development** — phát triển phần mềm có AI hỗ trợ, tổ chức theo phương pháp Agile. Được xây bởi **BMad Code, LLC** (Mỹ), hiện tại ở phiên bản **v6.3.0** (phát hành 9 tháng 4, 2026).

**BMAD** có hai cách hiểu (dual acronym):
- **Breakthrough Method for Agile AI-Driven Development** — phiên bản chính thức (GitHub description)
- **Build More Architect Dreams** — phiên bản thân thiện (README subtitle)

### Quick stats
- ⭐ **45,077 stars** — lớn nhất trong corpus T1 (cao hơn 9× so với các framework cùng tầng)
- 🍴 **5,338 forks**
- 📦 42 MB, chủ yếu Markdown (không phải code)
- 📜 License: MIT
- 🇻🇳 **README_VN.md có sẵn** — framework T1 đầu tiên trong corpus có bản dịch tiếng Việt

### Định vị (Positioning)

BMAD khác các framework AI-assistant khác ở:
1. **Markdown-core:** agent là file `.md`, không phải code
2. **12+ specialized agents** — đóng vai PM / Architect / Developer (Amelia) / UX / v.v.
3. **34+ workflows** — thư viện workflow lớn nhất trong T1
4. **5 module ecosystem** — BMM / BMB / TEA / BMGD / CIS
5. **Novel primitives:** Party Mode + Scale-Domain-Adaptive Planning

---

## Part 2 — Tại sao nên quan tâm? / Why care?

### Cho developer VN

- **Framework methodology ready-made** — không cần tự thiết kế quy trình, BMAD đã có sẵn 34+ workflow tiêu chuẩn (PRD, architecture design, test strategy, v.v.)
- **AI agent đóng vai chuyên gia** — bạn prompt, agent trả lời theo góc nhìn PM / Architect / Developer / UX
- **Claude Code primary support** — nếu bạn đang dùng Claude Code, cài 1 lệnh là xài được
- **Tiếng Việt:** README có bản VN (chất lượng trung bình, xem Part 8)

### Cho Scrum coach

- **Party Mode:** cho phép nhiều agent personas tham gia trong cùng một session — giống như chạy retro ảo với đại diện nhiều role. **Ứng viên pilot cho retro/sprint planning.**
- **Scale-Domain-Adaptive:** độ sâu planning tự động điều chỉnh theo quy mô project — đỡ mất thời gian tune cho từng team/client
- **BMM core workflows:** các workflow về retrospective, sprint planning, user story elaboration — rất gần với thực hành Scrum

---

## Part 3 — Cài đặt / Installation

### Yêu cầu

- Node.js 18+
- Claude Code (hoặc Cursor, Augment, Junie — JetBrains AI mới added v6.3)
- Git repo (BMAD cài vào thư mục project)

### Lệnh cài đặt

```bash
cd your-project
npx bmad-method install
```

CLI sẽ hỏi bạn:
1. Chọn module muốn cài: **BMM** (core, bắt buộc) + tùy chọn BMB / TEA / BMGD / CIS
2. v6.3+: chọn **source** — official / community (marketplace) / custom URL (GitHub, GitLab, Bitbucket, self-hosted đều được)
3. Chọn IDE target — Claude Code, Cursor, Augment, Junie

Sau khi cài xong, BMAD đăng ký agents + workflows vào `.claude-plugin/` (hoặc tương đương theo IDE). Bạn dùng `bmad-help` để xem danh sách agent/workflow khả dụng.

### Release channels

- `@latest` — stable, phát hành mỗi tuần
- `@next` — auto-publish khi code merge vào `main` (churn cao, dành cho early adopter)

Người mới → dùng `@latest`. Đừng chạm `@next` trừ khi bạn muốn test alpha.

---

## Part 4 — 5 modules là gì? / The 5 modules

| Module | Viết tắt | Mục đích | Khi nào dùng |
|--------|----------|---------|-------------|
| **BMad Method** | BMM | Core framework, 34+ workflow Agile chuẩn | Luôn cài — đây là nền |
| **BMad Builder** | BMB | Meta — tạo agent/workflow/module tùy chỉnh | Khi bạn muốn viết agent của riêng mình |
| **Test Architect** | TEA | Risk-based test strategy + automation | Team quan tâm test coverage + risk |
| **Game Dev Studio** | BMGD | Workflows Unity/Unreal/Godot | Làm game |
| **Creative Intelligence Suite** | CIS | Brainstorming + design thinking | Giai đoạn ideation, innovation |

**Chiến lược cài module:**
- **Newcomer:** chỉ BMM — đủ dùng cho 80% case
- **Quan tâm tests:** BMM + TEA
- **Làm game:** BMM + BMGD
- **Muốn tùy chỉnh:** BMM + BMB
- **Full stack methodology:** tất cả 5 — nhưng chuẩn bị cognitive overload

---

## Part 5 — 12+ Agents và Amelia / 12+ Agents and Amelia

BMAD có **12+ agent personas** (README claim — danh sách đầy đủ không public trong README, chỉ xem được sau khi cài trong thư mục `bmad/bmm/agents/`).

### Agents được đặt tên trong README + CHANGELOG

| Agent | Role | Note |
|-------|------|------|
| **Amelia** | Developer | v6.3 tích hợp Barry (quick-flow) + Quinn (QA) + Bob (Scrum Master) vào Amelia |
| **PM** | Product Manager | Chủ trì PRD + requirements |
| **Architect** | Architecture design | Chịu trách nhiệm cấu trúc hệ thống |
| **UX** | UX expert | Design thinking + user flows |

### Xu hướng v6.3: ít agent hơn, phạm vi rộng hơn

Trước v6.3: 4 agent dev-adjacent (Barry / Quinn / Bob / Amelia) với scope chồng lấp → user khó chọn.

Sau v6.3: **Amelia hấp thụ cả 3** — một Amelia, competence rộng hơn, ít decision fatigue hơn.

⚠️ **Lưu ý:** Nếu bạn có script/workflow cũ gọi Barry/Quinn/Bob, **cần update để gọi Amelia** sau khi upgrade lên v6.3.

### Cách invoke agent

Trong Claude Code, sau khi cài BMAD:

```
/bmad-help           # xem tất cả agent
@PM tạo giúp PR/FAQ cho tính năng X
@Amelia implement tính năng X với TDD
@Architect review kiến trúc cho module Y
```

*(Syntax thực tế có thể khác — kiểm tra `bmad-help` sau khi cài.)*

---

## Part 6 — Party Mode (tính năng độc đáo)

**Party Mode** = nhiều agent personas cùng xuất hiện trong một session, trò chuyện và cộng tác với nhau.

### Ví dụ sử dụng

**Tình huống:** Thiết kế tính năng mới, startup 5 người, backend Node hiện hữu

```
> bmad-party PM Architect Amelia UX

[PM] Trước hết xác định scope. User problem là gì?
[user] User bị mất session khi refresh page

[UX] Hỏi nhanh — đây là feature mới hay fix complaint?
[PM] Complaint-driven. Viết PR/FAQ ngắn.

[Architect] Heads up — session storage có 3 cách:
  1. localStorage (client-only)
  2. Server-side sessions (stateful)
  3. Cookie + stateless JWT
  Trade-off...

[Amelia] Tôi spike #3 — 1 ngày.

[user] Đi với #3
[PM] Drafting PR/FAQ...
[Architect] ADR for JWT approach...
[Amelia] Setting up test harness...
```

### Giá trị

- **Multi-perspective trong 1 session** — không mất context khi chuyển agent
- **Thích hợp cho planning phase** — khi cần nhiều góc nhìn (PM + UX + Dev + Architect)
- **Transcript multi-agent** — lưu lại được reasoning từ nhiều phía

### Lưu ý (novel-but-unproven)

- Chưa có benchmark public chứng minh Party Mode hơn single strong agent
- N agent → context lớn → token cost cao
- Có thể bị vòng lặp vô tận (agent debate không kết luận)
- **Khuyến nghị người mới:** thử 1-2 session cho planning, đánh giá value rồi quyết định dùng thường xuyên không

---

## Part 7 — Scale-Domain-Adaptive Planning

**Claim:** BMAD tự động điều chỉnh độ sâu planning dựa trên độ phức tạp của project.

### Cách hoạt động (inferred — README không public algorithm)

1. User nêu goal của project
2. BMAD đánh giá **scale** (repo size, team size, deadline) + **domain** (game/enterprise/prototype)
3. Workflow planning chọn depth phù hợp: quick-spec / full-PRD / architecture-doc / full

### Giá trị

- **Đỡ mất thời gian tune** — không cần mỗi lần nhắc "làm ngắn gọn" hay "làm chi tiết"
- **Cho team trưởng thành khác nhau** — Storm Bear coaching nhiều team với maturity khác, Scale-Adaptive giúp thống nhất cách dùng

### Lưu ý

- Algorithm là **black box** (heuristic hay LLM-based — README không nói)
- Nếu Scale-Adaptive đoán sai, user nhận output sai size
- User override? Chưa rõ từ README

---

## Part 8 — Tiếng Việt: chất lượng dịch và cộng đồng

### BMAD là framework T1 đầu tiên trong corpus có bản dịch VN

- `README_VN.md` (7.5 KB) — release v6.3 (9/4/2026) cùng với Czech (cs-CZ)
- URL: `docs.bmad-method.org/vi-vn/`

### Chất lượng dịch — đánh giá thẳng thắn

**Verdict: Professional machine-translation, minimal human polish.**

- ✅ Structure parity — đầy đủ sections như EN README
- ✅ Technical terms preserved — Agent, AI, CI/CD, Node.js, Python giữ nguyên
- ⚠️ Một số cụm awkward: `"một mô-đun khung phát triển hướng AI"` (clunky)
- ⚠️ "Build More Architect Dreams" dịch literal, không idiomatic VN
- ⚠️ Inconsistent: "Skills" untranslated nhưng "process" → "quy trình"
- ❌ Không có VN-specific examples (dùng cùng examples EN)
- ❌ Không có VN community signal (Discord global, không có Zalo/channel VN)

### Ý nghĩa với người mới VN

- **Đọc README_VN** để hiểu framework — đủ dùng, không xuất sắc
- **Agent responses trong VN** — Claude/Amelia có thể trả lời VN khi bạn prompt VN (nhờ LLM bên dưới, không phải BMAD dịch)
- **Agent names + CLI + workflow prompts vẫn EN** — cognitive friction nhẹ
- **Đóng góp cộng đồng:** bạn có thể submit PR cải thiện chất lượng dịch (low-barrier OSS contribution)

### Với Storm Bear operator

**Nếu bạn là coach làm việc với team VN:**
- BMAD là **option khả dụng đầu tiên** trong T1 — đáng thử
- Nhưng không kỳ vọng deep localization — đây là docs layer, không phải product localization
- Pilot 1 sprint với VN team, đo friction, quyết định tiếp

---

## Part 9 — So sánh với các framework T1 khác

| Aspect | BMAD | ECC | Superpowers | gstack | GSD |
|--------|------|-----|-------------|--------|-----|
| **Stars** | **45K ⭐** | ~5K | ~5K | ~5K | ~8K |
| **Specialization** | Agile AI-driven + marketplace | All-round Claude Code | Methodology + TDD | Specialist roles | Context rot solution |
| **Agents** | 12+ (shrinking) | Many skills | ~10 patterns | ~15 roles | 33 (growing) |
| **Modules** | 5 (BMM/BMB/TEA/BMGD/CIS) | Skills catalog | Pattern library | Flat roles | Commands |
| **VN support** | **✅ v6.3** | ❌ | ❌ | ❌ | ❌ |
| **Install** | `npx bmad-method install` | git setup | plugin | `npm` | `npx get-shit-done-cc` |
| **Author** | BMad Code, LLC | Solo | Solo (Jesse Vincent) | YC (Garry Tan) | Solo (TÂCHES) |
| **Marketplace** | ✅ (v6.3 browser) | ❌ | ❌ | ❌ | ❌ |
| **Novel features** | Party Mode, Scale-Adaptive | — | 7-stage workflow | YC team framing | Context rot spec |

**Xem [[(C) Tier 1 5-way comparison]] để so sánh sâu 18+ axis.**

### Recommendation theo profile

- **VN operator** → BMAD (duy nhất có VN)
- **Individual developer, Claude Code native** → ECC hoặc Superpowers
- **Team startup kiểu YC** → gstack
- **Methodology thuần TDD** → Superpowers
- **Context engineering focus** → GSD
- **Methodology Agile + nhiều workflow** → BMAD

---

## Part 10 — Lộ trình học 4 tuần / 4-week learning roadmap

### Tuần 1: Làm quen

- Đọc `README_VN.md` (cả bản VN và EN để đối chiếu)
- Cài BMAD vào 1 project test: `npx bmad-method install` → chọn chỉ BMM
- Chạy `bmad-help` xem danh sách agent + workflow
- Invoke Amelia cho 1 task đơn giản (fix bug nhỏ, add test)

**Goal:** biết BMAD cài được, agent invoke được, workflow output là gì.

### Tuần 2: Workflow chính

- Thử 3 workflow: PRD creation (PM), architecture design (Architect), feature implementation (Amelia)
- Document 3 workflow output của bạn — so sánh với cách bạn tự làm không có BMAD
- Note friction points — chỗ nào BMAD giúp thật sự, chỗ nào cảm thấy thừa

**Goal:** có opinion về giá trị của BMAD trong context của bạn.

### Tuần 3: Novel features

- Thử **Party Mode** 2-3 lần cho planning session (PM + Architect + Amelia + UX)
- Đánh giá: Party Mode có hơn invoke agent serial không?
- Observe **Scale-Adaptive** — planning output cho small feature vs large feature có khác rõ rệt không?

**Goal:** kiểm chứng empirical value của features độc đáo.

### Tuần 4: Pilot + quyết định

- Nếu bạn là Scrum coach: chạy 1 retro với Party Mode (ghi lại transcript, share với team)
- Nếu bạn là developer: dùng BMAD cho 1 tính năng production (1 PR thực tế với Amelia đồng hành)
- Quyết định: **keep / drop / recommend-to-team** sau 4 tuần empirical

**Goal:** đưa ra quyết định dựa trên use thực tế, không phải đọc README.

---

## Next actions — cho người mới

1. **Đọc** README_VN + README EN song song (1 giờ)
2. **Cài** BMAD vào 1 project test (15 phút): `npx bmad-method install`
3. **Invoke** Amelia cho 1 task nhỏ (30 phút) → đánh giá fit
4. **Quyết định** có đi tiếp 4-week roadmap không
5. **Nếu tiếp:** block lịch 4 tuần + track friction points trong note riêng

### Khi cần help

- Discord BMad: link từ README (global channel, không có VN specific)
- YouTube BMad: tutorials EN
- Storm Bear vault: `[[(C) index]]` — quick ref này + 4 entity pages + 3 source summaries
- Open questions: 15+ Q outstanding trong [[../01 Analysis/(C) open questions]] — nếu bạn trả lời được qua pilot, ghi lại vào wiki

---

## Appendix A — Vocabulary VN/EN

| EN | VN | Note |
|----|-----|------|
| Agent | Agent | Giữ nguyên |
| Workflow | Quy trình / workflow | Thường giữ EN |
| Skill | Skill | Giữ nguyên |
| Module | Module / mô-đun | Linh hoạt |
| Party Mode | Party Mode | Không có VN term tương đương |
| Scale-Adaptive | Scale-Adaptive | Giữ nguyên |
| PR/FAQ | PR/FAQ | Amazon Working Backwards artifact |
| ADR | ADR | Architecture Decision Record |
| Marketplace | Marketplace | Giữ nguyên |
| Trunk-based | Trunk-based | Giữ nguyên |
| Breaking change | Breaking change | Giữ nguyên |

## Appendix B — Quick reference

### Commands

```bash
npx bmad-method install           # cài BMAD vào project
bmad-help                          # list agents + workflows
npm run validate:skills            # validate agent .md files (contributor)
npm ci && npm run quality          # quality gate trước push (contributor)
```

### Module abbreviations

- **BMM** = BMad Method (core)
- **BMB** = BMad Builder (meta)
- **TEA** = Test Architect
- **BMGD** = Game Dev Studio
- **CIS** = Creative Intelligence Suite

### Named agents

- **Amelia** = Developer (v6.3 consolidated Barry+Quinn+Bob)
- **PM** = Product Manager
- **Architect** = Architecture design
- **UX** = UX expert

### Version timeline (evolution)

v1.0 (2025-04) Foundation → v2.0 Modularization → v3.0 Orchestration → v4.0 NPM framework → v5.0 **SKIPPED** (NPX corruption) → v6.0 (2026-01) Skills architecture → v6.3 (2026-04) VN+Czech+Amelia consolidation+marketplace

---

## Cross-references

- Parent wiki: [[../02 Wiki/(C) index]]
- Entity pages:
  - [[../02 Wiki/(C) 12+ Specialized Agents (Amelia Dev + PM + Architect + UX)]]
  - [[../02 Wiki/(C) 34+ Workflows + 5 Module Ecosystem]]
  - [[../02 Wiki/(C) Party Mode + Scale-Domain-Adaptive Planning]]
  - [[../02 Wiki/(C) VN Localization + Storm Bear Direct Relevance]]
- Comparison: [[(C) Tier 1 5-way comparison]]
- Sibling wikis T1:
  - `../../Everything Claude Code - Beginner Analysis/03 Published/`
  - `../../Superpowers - Beginner Analysis/03 Published/`
  - `../../gstack - Beginner Analysis/03 Published/`
  - `../../get-shit-done - Beginner Analysis/03 Published/`

---

**🐻 Storm Bear note:** BMAD là first T1 với VN — đáng thử pilot. Nhưng đừng kỳ vọng deep localization. Đánh giá empirical sau 4 tuần rồi quyết định.
