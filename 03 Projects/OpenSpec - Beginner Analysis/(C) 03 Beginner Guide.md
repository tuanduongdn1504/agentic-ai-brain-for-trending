# OpenSpec - Hướng dẫn cho người mới (Beginner Guide)

> **Subject:** `Fission-AI/OpenSpec` — "Spec-driven development (SDD) for AI coding assistants"
> **Bilingual:** VN primary + EN technical
> **Wiki:** v58 (Storm Bear corpus)

---

## 1. OpenSpec là gì? / What is it?

**VN:** OpenSpec là một CLI scaffolder + công cụ tạo file kỹ năng (skill files) cho 30+ AI coding assistant. Mục tiêu: **đặt lớp đặc tả (specification layer) giữa hội thoại người-AI và code thực tế**, để AI assistant không "đoán mò" yêu cầu chỉ từ chat history. Áp dụng phương pháp **SDD (Spec-Driven Development)** — quy trình proposal → specs → design → tasks trước khi viết code.

**EN:** OpenSpec is a CLI scaffolder and skill-file generator for 30+ AI coding assistants. Goal: **insert a specification layer between human-AI dialogue and code generation**, so AI assistants don't guess at requirements from chat history alone. Implements **SDD (Spec-Driven Development)** — a proposal → specs → design → tasks pipeline executed before any code is written.

**Tagline (verbatim):** "Spec-driven development (SDD) for AI coding assistants"

---

## 2. Corpus-first signals

Đây là 5 tín hiệu cho thấy OpenSpec là **corpus-first** (lần đầu trong 58 wiki Storm Bear):

1. **30+ AI tool support** — corpus-broadest multi-platform-by-design (vượt n8n v56 16 LLM providers + mattpocock v57 ~8 platforms)
2. **2nd corpus SDD framework at T1** — sau spec-kit v17; cùng named-methodology lineage
3. **Pseudonymous-org with active-commercial-product** — Fission-AI org "no public members" (corpus-first; v21 system-prompts-leaks là individual-pseudonymous + leaked-content)
4. **Per-tool skill-file generation as universal deployment format** — 11 skills × 30+ tools = ~330+ artifacts
5. **Cites spec-kit v17 as anti-pattern foil** — Pattern #57 57c forward-citation grows N=7 → N=8 conservative-attribution

---

## 3. Tier placement

- **Tier:** **T1 Assistant** (SDD framework targeting AI coding assistants — augments assistants, doesn't replace them)
- **Archetype:** Pseudonymous-org (Fission-AI) + small-team
- **Methodology lineage:** SDD (Spec-Driven Development) — sibling lineage with v17 spec-kit
- **Scale tier:** X-Large 45.8K stars
- **Primary lang:** TypeScript 98.9%

---

## 4. Cài đặt (Installation)

**Yêu cầu / Requirements:** Node.js 20.19.0 trở lên / Node.js 20.19.0+

```bash
# Cài global package / Install global package
npm install -g @fission-ai/openspec@latest

# Vào project hiện có / Enter your existing project
cd your-project

# Khởi tạo OpenSpec (tự động phát hiện AI tool đang dùng)
# Initialize OpenSpec (auto-detects which AI tools you use)
openspec init
```

`openspec init` sẽ phát hiện công cụ AI bạn đang dùng (Claude Code / Cursor / Copilot / etc.) và tự động sinh các file kỹ năng phù hợp ở đúng directory (vd `.claude/skills/openspec-*/SKILL.md`).

`openspec init` detects which AI tools you use and generates appropriate skill files in the right directories (e.g. `.claude/skills/openspec-*/SKILL.md`).

---

## 5. Quy trình sử dụng cốt lõi (Core usage pattern)

### Workflow gồm 3 phase chính:

**Phase 1: Đề xuất (Propose)**

```
/opsx:propose add-dark-mode
```

OpenSpec tạo folder cho thay đổi này:

```
changes/add-dark-mode/
├── proposal.md     # lý do làm tính năng / rationale + scope
├── specs/          # đặc tả yêu cầu / requirements specifications
├── design.md       # thiết kế kỹ thuật / technical approach
└── tasks.md        # checklist công việc / implementation checklist
```

**Phase 2: Áp dụng (Apply)**

```
/opsx:apply
```

AI assistant đọc proposal/specs/design/tasks và bắt đầu thực thi từng task. Tiến độ được track theo checklist trong `tasks.md`.

The AI assistant reads proposal/specs/design/tasks and executes each task, tracking progress via the `tasks.md` checklist.

**Phase 3: Lưu trữ (Archive)**

```
/opsx:archive
```

Khi tính năng hoàn thành, archive sẽ chuyển change-folder vào `archive/` và update các spec canonical trong project.

When complete, archive moves the change-folder to `archive/` and updates canonical specs.

### Mở rộng (Extended commands):

`/opsx:new` / `/opsx:continue` / `/opsx:ff` (fast-forward) / `/opsx:verify` / `/opsx:bulk-archive` / `/opsx:onboard` / `/opsx:explore`

---

## 6. Khái niệm mới + lựa chọn kiến trúc (Novel concepts + key architectural choices)

1. **Lớp đặc tả (specification layer)** — giữa con người và AI có thêm lớp formalization. Không phải chat thẳng → AI generate code, mà là chat → proposal → specs → design → tasks → AI thực thi.

2. **Per-tool format translation** — OpenSpec không dùng 1 format chung cho tất cả 30+ tool, mà translate ra format đúng của từng tool (markdown / TOML / prompt). Đây là corpus-first cross-tool-skill-format-translator pattern.

3. **Brownfield-first** — phương châm "built for brownfield not just greenfield". OpenSpec hoạt động trên project có sẵn, không bắt user phải làm lại từ đầu.

4. **Fluid không phải rigid (Fluid not rigid)** — đây là điểm OpenSpec self-distinguish khỏi spec-kit v17. spec-kit có "rigid phase gates" (theo OpenSpec); OpenSpec cho phép update artifact bất cứ lúc nào.

5. **Multi-platform-by-design** — 30+ AI tool support là điểm mạnh nhất của OpenSpec. Bạn không bị lock vào 1 IDE / 1 model như Kiro (theo OpenSpec).

---

## 7. So sánh với các framework corpus khác (vs other corpus frameworks)

| Aspect | OpenSpec v58 | spec-kit v17 | mattpocock v57 | BMAD v11 | GSD v5/v54 |
|---|---|---|---|---|---|
| Methodology | SDD | SDD | Pragmatic + DDD + XP + PoSD | BMM | GSD |
| Author archetype | Pseudonymous-org | Microsoft GitHub | Solo-individual + commercial-educator | Solo-individual | Solo-individual |
| Scale | 45.8K stars | (corpus v17) | 62K stars | (corpus v11) | (corpus v5/v54) |
| Multi-platform | **30+ tools** | Limited | ~8 tools | Limited | Limited |
| Phase discipline | Fluid | Rigid (per OpenSpec) | "Real engineering" | Phased | "Get shit done" |
| License | MIT | (corpus v17) | MIT | (corpus v11) | (corpus v5/v54) |
| Lang | TypeScript | Python | Shell/markdown | (corpus v11) | (corpus v5/v54) |

**OpenSpec self-positioning vs siblings:** "Lighter and lets you iterate freely" (vs spec-kit) + "Works with the tools you already use" (vs Kiro AWS).

---

## 8. Ethical framing + supply-chain awareness

**1. Pseudonymous-org transparency:** Fission-AI org có "no public members" — không biết ai đứng sau. Khi dùng OpenSpec trong client work, lưu ý tính minh bạch về supply chain. Đây không phải red flag tự động (nhiều dự án OSS có maintainer ẩn) nhưng là điểm cần aware.

**Pseudonymous-org transparency:** Fission-AI has no public members — unclear who maintains. Not an automatic red flag (many OSS projects have hidden maintainers) but worth noting for supply-chain awareness in client work.

**2. Posthog-node telemetry dependency:** package.json có `posthog-node` (analytics). Default behavior (opt-in / opt-out telemetry) chưa được verify (Q4 trong OPEN-QUESTIONS). Trước khi deploy vào client work, kiểm tra xem có gửi data ra ngoài không.

**Posthog-node telemetry:** package.json includes `posthog-node` (analytics). Default opt-in/opt-out behavior unverified (Q4 in OPEN-QUESTIONS). Verify telemetry behavior before client deployment.

**3. Multi-tool spec generation:** OpenSpec sinh ra ~330+ skill-file (11 × 30+ tool) trên project. Một số directory không phải tool bạn dùng. Kiểm tra `.gitignore` để tránh commit skill-file không cần thiết.

**Multi-tool spec generation:** OpenSpec generates ~330+ skill-files (11 × 30+ tools) in project. Some directories may not be tools you use. Check `.gitignore` to avoid committing unneeded skill-files.

---

## 9. Storm Bear relevance (VN operator + Scrum coach fit)

**8 use case cụ thể cho Storm Bear vault:**

1. **Client-discovery-session output** → proposal.md → specs/ → tasks pipeline (thay note ad-hoc bằng artifact formal)
2. **Sprint-planning artifact pipeline** — sprint goal → user stories (specs) → design decisions → task list (sprint backlog formalized)
3. **Retro decision capture** as design.md (architectural decisions traceable across sprints)
4. **Onboarding new client engagements** via `/opsx:onboard`
5. **Sprint review verification** via `/opsx:verify`
6. **Backlog grooming bulk-archive** via `/opsx:bulk-archive`
7. **Cross-team-tool standardization** — Storm Bear team Claude Code primary; client teams có thể dùng Cursor / Copilot / Gemini CLI; 1 install OpenSpec coverage cho tất cả 30+ tool
8. **Pattern Library candidate-registration analog** — proposal/specs/design/tasks pipeline song song với candidate → refinement → confirmation → archive lifecycle của Storm Bear vault

**Pilot relevance: HIGH rank #2-3** (cùng claude-hud + claude-howto). Top recommendation: trial OpenSpec trên 1 client engagement at v60+ để validate spec-driven Scrum coaching applicability.

---

## 10. Roadmap học 4 tuần / 4-week learning roadmap

**Tuần 1 (Week 1): Setup + first proposal**
- Cài `npm install -g @fission-ai/openspec@latest`
- Verify telemetry behavior (Q4 OPEN-QUESTIONS)
- Khởi tạo trên 1 personal project nhỏ với `openspec init`
- Tạo proposal đầu tiên với `/opsx:propose`
- Đọc `proposal.md` + `specs/` + `design.md` + `tasks.md` được sinh ra
- Compare format với `.claude/skills/openspec-*/SKILL.md`

**Tuần 2 (Week 2): End-to-end workflow**
- Apply 1 proposal end-to-end (`/opsx:propose` → `/opsx:apply` → `/opsx:archive`)
- Quan sát archive structure + canonical specs update
- Trial 2-3 proposals song song để hiểu fluid-iteration model
- So sánh với spec-kit v17 (nếu đã thử) — tìm ra cái nào hợp workflow của bạn

**Tuần 3 (Week 3): Cross-tool deployment**
- Cài Cursor (hoặc 1 IDE thứ 2) + run `openspec init` lần nữa
- Verify per-tool skill files được sinh ra ở đúng directory
- Trial workflow trên Cursor + so sánh với Claude Code
- Identify tool nào hợp Scrum coaching workflow của bạn nhất

**Tuần 4 (Week 4): Vault integration**
- Trial OpenSpec trên 1 client engagement (Scrum coach work)
- Capture client-discovery-session as proposal.md → specs/ → tasks pipeline
- Compare outcome với non-OpenSpec engagement (qualitative)
- Decide: pilot adoption / pause / reject; document quyết định trong `04 Reviews/`

---

## 11. Tradeoffs + limitations

**Strengths:**
- Corpus-broadest multi-platform breadth (30+ tools)
- MIT license, no commercial-use barrier
- Lighter-weight than spec-kit per OpenSpec self-positioning
- Brownfield-first design (works on existing projects)
- npm distribution + Node.js 20+ requirement standard

**Tradeoffs:**
- Pseudonymous-org maintainer (Fission-AI hidden members) — supply-chain awareness flag
- Posthog-node telemetry dependency (default behavior unverified)
- Per-tool format translation = maintenance burden across 30+ tool format-spec
- Generates ~330+ files in your project (11 × 30+ tools); requires `.gitignore` discipline
- "Fluid not rigid" can become "no discipline" if user doesn't enforce review gates
- 5-principle list less formal than spec-kit's 9-article constitution (per spec-kit comparison)

**Limitations:**
- TypeScript-only codebase (98.9%); no Python / Go alternatives
- Node.js 20.19.0+ requirement excludes legacy environments
- Multi-language support listed in docs TOC but not yet verified at probe (Q in OPEN-QUESTIONS)

---

## 12. Caveats + safety notes

1. **Supply-chain awareness:** posthog-node telemetry; pseudonymous-org maintainer; 30+ tool dependency surface. Run on non-critical project first.
2. **Spec discipline:** OpenSpec gives you the artifact pipeline but doesn't enforce review. Without team discipline, "fluid not rigid" = no quality gate.
3. **Corpus-first multi-platform = early-adopter risk:** 30+ tool format support means OpenSpec is a leading-edge tool. Some tool integrations may break when target tools update format.
4. **Data sensitivity:** before piloting on client engagements, verify OpenSpec data flow + posthog-node telemetry behavior. Storm Bear vault default = privacy-preserving for client data.

---

## 13. References + next action

**References:**
- Repo: https://github.com/Fission-AI/OpenSpec
- Homepage: openspec.dev
- Package: `@fission-ai/openspec` on npm
- Sibling SDD framework: spec-kit (corpus v17; cited by OpenSpec as anti-pattern foil)
- Sibling skill-collection: mattpocock/skills (corpus v57; both v57 + v58 strengthen Pattern #51 anti-vibe pole)

**Next action:**
- Sprint 1: Cài OpenSpec trên 1 personal project nhỏ; trial 1 proposal end-to-end
- Sprint 2: Verify posthog-node telemetry behavior (Q4 OPEN-QUESTIONS)
- Sprint 3: Decide pilot vs pause; if pilot → trial on 1 client Scrum engagement at v60+

**Pattern Library impact post-v58:**
- Pattern #57 57c forward-citation grows N=7 → N=8 conservative-attribution
- Pattern #18 Layer 1 STRONGEST multi-platform evidence (30+ tools)
- Pattern #51 anti-vibe pole strengthening 2 consecutive wikis
- 41st consecutive Storm Bear meta-entity (3-of-4 STRICT criteria pass — 3rd consecutive STRICT-instance satisfied)
- 22-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES streak NEW LONGEST extends v57 21-streak
