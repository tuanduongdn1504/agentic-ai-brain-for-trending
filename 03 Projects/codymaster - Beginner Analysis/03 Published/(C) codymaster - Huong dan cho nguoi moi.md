# (C) codymaster — Hướng dẫn cho người mới (bilingual VN-first)

> **Audience:** Vietnamese developers + product leads + Scrum coaches. Đây là framework đầu tiên trong corpus Storm Bear **được viết bởi tác giả Việt Nam** (Tody Le).
> **Sources:** [[../02 Wiki/(C) index]] + 4 entity pages + 3 source summaries
> **Read time:** ~25-30 phút
> **Convention:** VN chính, EN cho technical terms. Đây là guide đầu tiên trong corpus **VN-first** (ưu tiên trải nghiệm VN reader).

---

## Phần 1 — codymaster là gì?

**codymaster** là một **"Vibe Coding Framework"** — bộ skill + CLI biến Claude Code (hoặc Cursor, Gemini CLI, OpenCode, vv.) thành **một team phát triển SaaS đầy đủ từ A-Z**, với "Brain" (bộ não), khả năng **self-improvement** (tự cải tiến), và **auto-development** (tự phát triển).

Tagline chính: **"Code Đi"** — tiếng Việt, thể hiện tinh thần "bắt tay vào làm thôi" (informal rapid-ship culture).

### Quick stats
- ⭐ **38 stars** — community nhỏ (niche project)
- 🍴 21 forks
- 📜 License: **ISC** (permissive, giống MIT)
- 📦 Version: **v5.1.0** (npm) / **v6.0.0** (website) — version skew
- 🛠️ **79 skills thực tế** (README ghi "60+", plugin.json ghi "68+" — marketing undersells)
- 🎮 **11 workflow commands** + ~10-15 CLI verbs (`cm <verb>`)
- 🌏 **8+ platforms** — Claude Desktop/Code, Cursor, Gemini CLI, OpenCode, OpenClaw, Codex, Antigravity, npm global/local
- 🗺️ **6 ngôn ngữ README** — EN/VI/ZH/RU/KO/HI

### Tác giả: Tody Le

**Điểm đặc biệt quan trọng cho người đọc VN:**

codymaster được viết bởi **Tody Le** — người Việt, Head of Product 10+ năm kinh nghiệm, **tự nhận là "không code được"**. Tody xây codymaster qua 6 tháng build sản phẩm thực tế với AI và distill patterns.

Đây là **framework đầu tiên trong corpus Storm Bear có tác giả VN**. Trước đó v11 BMAD có bản dịch VN nhưng tác giả là US-LLC; codymaster khác — tác giả IS Vietnamese.

**Website cá nhân:** cody.todyle.com
**Email:** aitodyle@gmail.com
**GitHub:** tody-agent

### Định vị (Positioning)

codymaster khác các T1 framework khác ở:
1. **VN author** — unique trong corpus
2. **79 skills** — nhiều nhất T1 (gấp 2× BMAD)
3. **8+ platforms** — rộng nhất T1
4. **Novel primitives rất sâu:** 5-Tier Memory + Smart Spine + CodeGraph + Self-Healing + Cloud Brain + SkillsBench empirical research
5. **"Can't code" author positioning** — designed for product-leads who ship via AI
6. **Vibe Coding philosophy** — informal rapid-ship vs GSD's formal context-engineering

---

## Phần 2 — Tại sao nên quan tâm?

### Cho developer VN

- **Framework từ người cùng context** — Tody Le hiểu dev VN. Có thể decision design phù hợp với budget-sensitive infra, mobile-first, ecosystem phân mảnh
- **79 skill = shelf rộng** — dễ tìm được skill phù hợp cho workflow cụ thể
- **8+ platforms** — không lock-in Claude Code; bạn đổi sang Cursor/Gemini vẫn dùng được
- **Self-Healing** — skills tự fix, tự evolve, không cần bạn maintain thủ công

### Cho Scrum coach

- **cm-retro-cli + cm-sprint-bus + cm-planning** — 3 skill trực tiếp cho workflow Scrum
- **cm-continuity** — giữ context cross-session (nhớ team context qua nhiều session coaching)
- **cm-brainstorm-idea + cm-jtbd** — facilitation ideation + Jobs-to-be-done

### Cho product lead (đặc biệt nếu bạn "không code được")

- **Author profile giống bạn** — Tody Le self-identifies "can't code" nhưng ship được product. Framework designed for you.
- **Full Lifecycle coverage** — Idea → Plan → Design → Code → Deploy → Monitor → Learn. Không cần bạn viết code; bạn điều phối skills.
- **4-Layer Protection** — security/quality gates built-in. Bạn không cần DevOps expert để deploy an toàn.

### Cho Storm Bear operator (bạn - Vietnamese + dev + Scrum coach + product-adjacent)

codymaster là **peer-category artifact**. Tác giả có profile overlap với bạn. Đây là framework đầu tiên trong corpus bạn có thể "mượn cách nghĩ" của peer VN.

---

## Phần 3 — Cài đặt

### Yêu cầu

- Node.js 18+
- 1 trong 8+ platforms: Claude Code / Claude Desktop / Cursor / Gemini CLI / OpenCode / OpenClaw / Codex / Antigravity
- Git repo (codymaster cài vào project)

### Cách cài (nhiều lựa chọn)

**Claude Desktop (Plugin marketplace):**
Settings → Plugins → Add marketplace → `tody-agent/codymaster` → Sync

**Claude Code CLI:**
```bash
claude plugin marketplace add tody-agent/codymaster
```

**Cursor:**
```
/add-plugin cody-master
```

**Gemini CLI:**
```bash
gemini extensions install https://github.com/tody-agent/codymaster
```

**npm global (dùng CLI `cm` bất cứ đâu):**
```bash
npm install -g codymaster
```

**npm per-project:**
```bash
npm install codymaster
```

### Verify cài thành công

```bash
cm status          # xem health
cm dashboard       # visual dashboard
cm how-it-work     # onboarding tour
```

Nếu bạn thấy 79 skills listed → OK.

### Release channels

- **npm latest** (v5.1.0 hiện tại) — stable
- **Website tagging v6.0.0** — có thể là pre-release hoặc marketing version

Người mới → dùng `@latest` hoặc mặc định npm install. Đừng thử `@next` hoặc canary cho đến khi quen.

---

## Phần 4 — 79 skills theo domain

Tody Le tổ chức 79 skills theo **8 domains**:

| Domain | Số skill | Ví dụ nổi bật | Khi dùng |
|--------|---------|--------------|---------|
| **Engineering & Code** | ~9 | cm-tdd, cm-debugging, cm-code-review, cm-clean-code | Viết code mới, refactor, review |
| **DevOps & Deployment** | ~5 | cm-safe-deploy, cm-post-deploy-canary, cm-git-worktrees | Deploy production |
| **Secret & Security** | ~5 | cm-secret-shield, cm-security-gate, cm-identity-guard | Security audit, leak prevention |
| **Project & Team Mgmt** | ~6 | cm-retro-cli, cm-sprint-bus, cm-planning, cm-status | Scrum ceremonies, tracking |
| **Design & UX** | ~4 | cm-design-system, cm-ui-preview, cm-ux-master | UI/UX work |
| **Ads / Growth** | ~4 | cm-growth-hacking, cm-cro-methodology, cm-ads-tracker | Marketing (unusual for coding kit!) |
| **Publishing / Content** | ~2 | cm-content-factory, cm-auto-publisher | Content workflow |
| **Self-Healing / Skills Mgmt** | ~8 | cm-skill-health, cm-skill-evolution, cm-learning-promoter | Framework tự maintain |
| **Orchestration / Infra** | ~10 | cm-execution, cm-continuity, cm-deep-search, cm-codeintell, cm-notebooklm | Core brain + infra |

### Scope đặc biệt

- **Growth domain** (cm-ads-tracker, cm-cro-methodology, cm-growth-hacking) — không phải framework "coding" nào cũng có. Tody Le framing: "full SaaS team A-Z" bao gồm marketing
- **Self-Healing domain** — codymaster là T1 framework DUY NHẤT có skills tự healing
- **Enterprise domain** (cm-reactor, cm-notebooklm) — chỉ 2 skills, scope nhỏ hơn tên gợi ý

---

## Phần 5 — "The Unified Brain" — cái gì làm codymaster unique

Đây là phần quan trọng nhất để hiểu codymaster. "Brain" gồm 3 lớp:

### Layer 1: 5-Tier Memory (bộ nhớ 5 tầng)

Giống mô hình memory của não người:

| Tầng | Vai trò | Ví dụ |
|------|---------|-------|
| **Sensory** | Context phiên làm việc hiện tại | Tin nhắn user vừa gõ |
| **Working** | Scratchpad cross-session | cm-continuity lưu progress sprint |
| **Long-term** | Knowledge persistent với **Ebbinghaus decay** (forgetting curve) | learnings.json — hot items stay, cold fade |
| **Semantic** | Vector retrieval — tìm theo meaning | cm-deep-search |
| **Structural** | CodeGraph AST-based | cm-codeintell — hiểu cấu trúc codebase |

### Layer 2: Smart Spine v4.6+ (xương sống điều phối)

- **SQLite + FTS5** — search nhanh theo keyword
- **Progressive loading L0/L1/L2** — load từ rẻ nhất, escalate khi cần
- **`cm://` URI scheme** — skills request context theo URI ngữ nghĩa
- **Context Bus** — skills share output real-time
- **MCP server exposing 18 tools** — codymaster là MCP PROVIDER (không chỉ consumer)
- **200k token budget pre-allocated** — ngân sách context chia sẵn theo category

### Layer 3: CodeGraph (~95% token compression)

- Parse AST codebase (tree-sitter hoặc tương tự)
- Build graph symbols + relationships (function calls, class inheritance, imports)
- Skill yêu cầu "cho tôi xem codebase" → graph summary thay vì raw code
- **Claim: compress 95% tokens** — chưa verify methodology

### Tại sao quan trọng

- **GSD** có "context rot spec" conceptual → codymaster có **solution thực tế**
- **BMAD** có Scale-Adaptive → codymaster có **memory 5-tier sâu hơn**
- **Không T1 peer nào có multi-tier memory** — codymaster unique

---

## Phần 6 — Self-Healing Skills + SkillsBench (empirical research)

### Self-Healing — framework tự sửa lỗi

Khi 1 skill bị lỗi (user gặp failure), codymaster có 3 chế độ tự repair:

| Mode | Trigger | Outcome |
|------|---------|---------|
| **FIX** | Skill structure đúng nhưng execution fail | Patch skill definition |
| **DERIVED** | Skill broken; có skill tương tự đang work | Generate skill mới từ precedent |
| **CAPTURED** | User tự solve ad-hoc, pattern lặp lại | Formalize solution thành skill permanent |

Và **cm-learning-promoter** tự graduate recurring tasks thành permanent skills.

**Tại sao unique:** Không T1 peer nào có skill-evolution primitives. codymaster là FIRST.

### SkillsBench — research empirical

Tody Le claim: **2-3 focused skills dynamically selected beats 4+ statically loaded skills by +18.6 percentage points**.

Function critical: `selectTopSkills()` — Smart Spine chọn 2-3 skills relevant nhất cho task hiện tại.

**Tại sao quan trọng:** đây là **T1 framework DUY NHẤT có empirical research published**. Các peer khác chỉ có design, không có data.

**Cảnh báo:** methodology không được public. "+18.6pp" đáng tin không kiểm chứng được.

---

## Phần 7 — Full Lifecycle (Idea → Learn)

codymaster claim cover end-to-end SaaS lifecycle:

```
Idea → Plan → Design → Test First → Code → Debug → Quality Gate
→ Security Scan → Deploy → Monitor → Document → Learn & Improve
                                                    ↓
                                          (feedback loop back to Plan)
```

**So với T1 peers:**

| Stage | codymaster | BMAD | GSD | gstack | SP | ECC |
|-------|-----------|------|-----|--------|-----|-----|
| Idea | ✅ cm-brainstorm-idea | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| Plan | ✅ cm-planning | ✅ PM | Partial | ✅ PM | ✅ stage 1 | ❌ |
| Design | ✅ cm-design-studio | ⚠️ UX | ❌ | ❌ | ❌ | ❌ |
| Test | ✅ cm-tdd | ⚠️ TEA | Partial | ⚠️ | ✅ core | ⚠️ |
| Code | ✅ cm-autopilot | ✅ Amelia | ✅ | ✅ | ✅ | ✅ |
| Debug | ✅ cm-debugging | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| Quality | ✅ cm-quality-gate | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Security | ✅ cm-security-gate | ❌ | ❌ | ❌ | ❌ | ECC ✅ |
| Deploy | ✅ cm-safe-deploy | ❌ | ❌ | ❌ | ❌ | ❌ |
| Monitor | ✅ cm-post-deploy-canary | ❌ | ❌ | ❌ | ❌ | ❌ |
| Document | ✅ cm-dockit | ❌ | ❌ | ❌ | ❌ | ❌ |
| Learn | ✅ cm-skill-evolution | ❌ | ❌ | ❌ | ❌ | ❌ |

→ **codymaster là T1 framework DUY NHẤT claim Idea→Learn end-to-end.**

**Caveat honest:** có skills ở mọi stage không có nghĩa depth bằng nhau. Code/Debug/Test deep; Idea/Monitor/Learn shallow-ish.

---

## Phần 8 — 4-Layer Protection (an toàn trước khi deploy)

codymaster bắt buộc 4 lớp bảo vệ trước khi deploy production:

| Layer | Protections | Skills |
|-------|-------------|--------|
| **Layer 1** | TDD + Code Review | cm-tdd, cm-code-review, cm-clean-code |
| **Layer 2** | Secret scan + Vuln scan + Account validation | cm-secret-shield, cm-security-gate, cm-identity-guard |
| **Layer 3** | Isolated git worktrees | cm-git-worktrees, cm-conductor-worktrees |
| **Layer 4** | Quality gates + multi-gate safe deploy | cm-quality-gate, cm-safe-deploy, cm-post-deploy-canary |

**Defense in depth** — mỗi layer bắt rủi ro khác nhau. Peers chỉ có 1-2 layer.

---

## Phần 9 — Tiếng Việt: chất lượng dịch và community

### README-vi.md — honest assessment

**Verdict: Machine-translated, dù tác giả là người Việt.**

**Evidence translation EN → VN (không phải VN-first):**
- Tool names không localize: cm-tdd, cm-debugging, NotebookLM vẫn giữ EN
- Subtitle mirror EN structure: *"AI Agent của bạn thông minh. CodyMaster làm nó trở nên thông thái"* (direct translation-pairing của *"Your smart AI Agent. CodyMaster makes it wise"*)
- Awkward literal phrasings: *"AI sửa một lỗi, âm thầm làm hỏng 5 thứ khác"* — native speaker sẽ viết khác

### Vì sao tác giả VN nhưng README-vi vẫn machine-quality?

Suy đoán (không confirm với tác giả):
- **Market reach** — English >> Vietnamese về dev community
- **Consistency** — machine translation auto-update khi EN update
- **Priority** — 6 ngôn ngữ (EN/VI/ZH/RU/KO/HI); chỉ EN get author effort; 5 khác machine

### VN-specific content
**Không có.** Examples abstract (login flow, SaaS, landing page). Không Zalo, không VNG/Tiki/Shopee reference. Community là global Discord — không có VN channel riêng.

### So sánh với BMAD (v11 VN-translated)

| Aspect | codymaster | BMAD |
|--------|-----------|------|
| Tác giả | VN (Tody Le) solo | US-LLC |
| VN README | Machine-quality | Machine-quality |
| VN community | ❌ | ❌ |
| VN-specific content | ❌ | ❌ |
| Author proximity | **✅ Unique peer** | ❌ |
| Community size | 38 stars | 45K stars |
| Skill depth | 79 skills | 46 (12+ agents + 34+ workflows) |

→ **codymaster win peer-author; BMAD win community + stability. Different strengths.**

### Ý nghĩa cho Storm Bear operator (bạn)

- **BMAD** = battle-tested Agile workflows + big community + US-LLC stability. Dùng cho team production.
- **codymaster** = peer-author depth + full-lifecycle scope + novel primitives. Dùng cho exploration + product-lead workflows.

**Gợi ý:** cài cả 2, dùng song song. BMAD cho retro/sprint Agile, codymaster cho Idea/Design/Growth + Cloud Brain.

---

## Phần 10 — Lộ trình học 4 tuần

### Tuần 1: Onboarding

- Đọc README (EN + VI song song để đối chiếu)
- Cài codymaster qua Claude Code: `claude plugin marketplace add tody-agent/codymaster`
- Chạy `cm status`, `cm dashboard`, `cm how-it-work` để onboard
- Invoke 1 skill đơn giản: `cm-clean-code` hoặc `cm-debugging` trên file test

**Mục tiêu:** biết cài được, biết invoke skill, hiểu cấu trúc 8 domains.

### Tuần 2: Scrum workflows (nếu bạn là Scrum coach)

- `cm-retro-cli` — chạy 1 retro ảo; so sánh với retro thực tế
- `cm-sprint-bus` — setup sprint coordination
- `cm-planning` — generate sprint plan cho real team bạn coach
- `cm-continuity` — test cross-session memory

**Mục tiêu:** đánh giá Scrum-fit.

### Tuần 3: Novel primitives

- `cm-deep-search` — test Semantic tier (vector retrieval)
- `cm-codeintell` — test Structural tier (CodeGraph)
- `cm-notebooklm` — Cloud Brain sync (setup NotebookLM account)
- Observe: có thấy `selectTopSkills()` chọn khác nhau theo task không? (`cm` có flag verbose/debug không? chưa rõ)

**Mục tiêu:** kiểm chứng claim depth của 5-Tier Brain.

### Tuần 4: Pilot + quyết định

- Pick 1 real project → apply codymaster end-to-end (Idea → Deploy)
- Document friction trong `04 Reviews/codymaster-pilot.md`
- So sánh với BMAD pilot (v11 roadmap) nếu bạn chạy song song
- Quyết định: keep-both / keep-codymaster-only / keep-BMAD-only / drop-both

**Mục tiêu:** empirical decision, không chỉ đọc README.

---

## Next actions cho người mới

1. **Đọc** README + README-vi song song (~1h)
2. **Cài** qua Claude Code (15 min): `claude plugin marketplace add tody-agent/codymaster`
3. **Invoke** 3 skills khác nhau (30 min) — assess fit
4. **Quyết định** có chạy 4-week roadmap không
5. **Nếu chạy:** block lịch 4 tuần + log friction trong `04 Reviews/`

### Khi cần help

- Global Discord: discord.gg/codymaster (không VN channel)
- GitHub issues: github.com/tody-agent/codymaster/issues (38 stars = ít traffic, response có thể nhanh)
- Storm Bear vault: `[[(C) index]]` — wiki này + 4 entity pages + 3 source summaries
- Open questions: 27 Q outstanding trong [[../01 Analysis/(C) open questions]] — pilot trả lời được thì log lại

---

## Appendix A — Vocabulary VN/EN

| EN | VN | Note |
|----|-----|------|
| Skill | Skill | Giữ nguyên |
| Vibe Coding | Vibe Coding | Informal coding culture — giữ nguyên |
| Code Đi | Code Đi | VN tagline |
| Brain / Unified Brain | Bộ não / Bộ Não Hợp Nhất | Localize OK |
| Memory tier | Tầng bộ nhớ | Localize |
| Ebbinghaus decay | Đường cong quên Ebbinghaus | Technical term |
| Self-Healing | Tự sửa / Self-Healing | Giữ EN hoặc VN đều OK |
| Smart Spine | Smart Spine | Giữ nguyên |
| CodeGraph | CodeGraph | Giữ nguyên |
| Cloud Brain | Cloud Brain | Giữ nguyên |
| SkillsBench | SkillsBench | Research brand |
| Full Lifecycle | Vòng đời đầy đủ | Localize |
| 4-Layer Protection | Bảo vệ 4 lớp | Localize |
| Context Bus | Context Bus | Technical term |
| MCP server | MCP server | Giữ nguyên |

## Appendix B — Quick reference

### Install
```bash
# Claude Code
claude plugin marketplace add tody-agent/codymaster

# Cursor
/add-plugin cody-master

# Gemini CLI
gemini extensions install https://github.com/tody-agent/codymaster

# npm global
npm install -g codymaster
```

### Common commands
```bash
cm status           # health + dashboard
cm dashboard        # visual dashboard
cm brain            # inspect brain state
cm chain <skills>   # chain skills
cm deploy           # trigger safe-deploy pipeline
cm sprint           # sprint workflow
cm how-it-work      # onboarding tour
```

### Numbers
- 79 skills (actual) / 60+ (README claim) / 68+ (plugin.json claim)
- 11 workflow commands + ~10-15 CLI verbs
- 8+ platforms supported
- 6 language READMEs
- 38 stars / 21 forks / 120 commits / 11 tags
- 200k token budget pre-allocated
- 5-Tier Memory / 4-Layer Protection

### Named primitives
- **5-Tier Memory** = Sensory + Working + Long-term (+Ebbinghaus) + Semantic + Structural
- **Smart Spine v4.6+** = SQLite+FTS5 + L0/L1/L2 + cm:// URI + Context Bus + MCP 18 tools
- **CodeGraph** = AST-based, ~95% compression
- **Self-Healing** = FIX / DERIVED / CAPTURED + auto-graduation
- **SkillsBench** = +18.6pp dynamic selection `selectTopSkills()`
- **Cloud Brain** = cm-notebooklm NotebookLM sync

---

## Cross-references

- Parent wiki: [[../02 Wiki/(C) index]]
- Entity pages:
  - [[../02 Wiki/(C) 79 Skills 8 Domains + 11 Commands Architecture]]
  - [[../02 Wiki/(C) 5-Tier Memory + Smart Spine + CodeGraph]]
  - [[../02 Wiki/(C) Self-Healing Skills + SkillsBench Dynamic Selection]]
  - [[../02 Wiki/(C) VN-Author Native + Tody Le + Storm Bear Peer-Relevance]]
- Comparison: [[(C) Tier 1 6-way comparison]]
- VN sibling for pilot-comparison:
  - `../../BMAD-METHOD - Beginner Analysis/03 Published/(C) BMAD-METHOD - Huong dan cho nguoi moi.md`
- Sibling T1 wikis:
  - `../../Everything Claude Code - Beginner Analysis/03 Published/`
  - `../../Superpowers - Beginner Analysis/03 Published/`
  - `../../gstack - Beginner Analysis/03 Published/`
  - `../../get-shit-done - Beginner Analysis/03 Published/`

---

**🐻 Storm Bear note:** codymaster là framework ĐẦU TIÊN trong corpus do tác giả VN viết. Đáng pilot. Dùng song song với BMAD. Log friction trong `04 Reviews/codymaster-pilot.md` để có empirical data cho decision.
