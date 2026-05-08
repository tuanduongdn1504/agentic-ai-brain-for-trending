# cc-sdd — Hướng dẫn cho người mới (bilingual VN + EN)

> **Subject:** [`gotalab/cc-sdd`](https://github.com/gotalab/cc-sdd) — *"Turn approved specs into long-running autonomous implementation. A minimal, adaptable SDD harness with Agent Skills for Claude Code, Codex, Cursor, Copilot, Windsurf, OpenCode, Gemini CLI, and Antigravity."*
> **Wiki:** Storm Bear corpus v61 / 2026-05-07
> **Tier:** T1 (Assistant — SDD harness)
> **Stars:** 3.3K / **License:** MIT / **Lang:** TypeScript 99.6% / **Author:** gotalab (solo-Japanese)

---

## 1. Đây là gì? / What is it?

**VN:** cc-sdd là một **bộ harness Spec-Driven Development (SDD) đa nền tảng**, cài qua npm (`npx cc-sdd@latest`), biến spec đã được duyệt thành quá trình thực thi tự động dài-hạn trên 8 AI coding agent platforms khác nhau. Tư tưởng cốt lõi: spec = hợp đồng giữa các thành phần (không phải mệnh lệnh top-down), code vẫn là source of truth, spec làm rõ **boundary** (ranh giới trách nhiệm) để con người và AI agent có thể làm việc song song.

**EN:** cc-sdd is a **multi-platform Spec-Driven Development (SDD) harness** installed via npm (`npx cc-sdd@latest`) that turns approved specs into long-running autonomous implementation across 8 AI coding agent platforms. Core philosophy: specs are contracts between system components (not top-down commands), code remains source of truth, specs make boundaries explicit so humans and agents can work in parallel without constant synchronization.

**Tagline verbatim:** *"Turn approved specs into long-running autonomous implementation. A minimal, adaptable SDD harness with Agent Skills for Claude Code, Codex, Cursor, Copilot, Windsurf, OpenCode, Gemini CLI, and Antigravity."*

---

## 2. Corpus-first signals

cc-sdd v61 đóng góp những điều mới chưa từng có trong corpus 60 wiki trước đó / cc-sdd v61 contributes the following corpus-firsts:

1. **Kiro IDE methodology lineage** — đầu tiên có lineage chain bắt nguồn từ ngoài AI-coding-agent ecosystem (Kiro IDE là AWS-affiliated coding IDE, không phải AI agent). gotalab port methodology vào multi-agent harness.
2. **Solo-Japanese T1 author** — đầu tiên trong corpus có solo-author người Nhật (sau solo-VN codymaster v12 + solo-CN TrendRadar v19 + solo-Korean OMC v27 + solo-VN-secondary). Pattern #55 mở rộng thêm Nhật làm 4th regional archetype.
3. **EARS-format requirements explicit reference** — đầu tiên corpus thấy EARS (Easy Approach to Requirements Syntax) được tham chiếu rõ ràng. EARS có nguồn gốc từ aerospace/systems engineering — predates AI agents.
4. **File Structure Plan (FSP) primitive** — đầu tiên corpus thấy FSP làm sub-section riêng trong design.md (mapping directory + file responsibilities).
5. **P-wave parallel-execution annotation** — đầu tiên có task priority + concurrency-safety đóng gói trong một primitive (P0 = blocking, same P# = concurrent-safe).
6. **`brief.md` discovery routing artifact** — đầu tiên corpus thấy file pre-spec routing decision riêng biệt.
7. **Adversarial subagent review architecture at framework level** — đầu tiên corpus thấy reviewer subagent + auto-debug-on-rejection được codified ở framework level (không phải pattern do operator design).
8. **Anti-vibe-with-pragmatic-acknowledgment positioning** — counter-evidence cho Pattern #51 vibe-coding spectrum: cc-sdd là anti-vibe nhưng acknowledges vibe-coding's legitimate use cases.
9. **agent-platform-format-translation-installer mechanism** — install-time per-platform skill format translation (8 platforms; phân biệt với runtime API protocol translation của free-claude-code v60 và per-tool format translation của OpenSpec v58 ở 30+ tools).
10. **Architecture-as-foundation explicit acknowledgment** — đầu tiên corpus thấy SDD framework explicit-state rằng SDD downstream của architectural discipline (*"writing more specs will not create independence"* khi architecture vague hoặc circular).

---

## 3. Tier placement

**T1 (Assistant — SDD harness for AI coding agents).**

**VN:** cc-sdd là framework methodology (SDD), không phải bridge protocol (T4) hay platform service (T2). Tương tự spec-kit v17 và OpenSpec v58 — tất cả đều T1 SDD framework. Multi-platform deployment (8 agents) chỉ là cơ chế distribution; methodology là substance.

**EN:** cc-sdd is a methodology framework (SDD), not a protocol bridge (T4) or platform service (T2). Sibling to spec-kit v17 and OpenSpec v58 — all T1 SDD frameworks. Multi-platform deployment (8 agents) is distribution mechanism; methodology is the substance.

**4 independent SDD-centered T1 frameworks in corpus post-v61:**
- v5 GSD (gsd-build solo-product-line) + v54 gsd-2 successor
- v17 spec-kit (Microsoft corporate)
- v58 OpenSpec (Fission-AI pseudonymous-org)
- **v61 cc-sdd (gotalab solo-Japanese) ← NEW**

→ 4 distinct organizational archetypes. Strong evidence for **Pattern #21 SDD Methodology Emergence un-stale + promotion** at next mini-audit.

---

## 4. Cài đặt / Installation

```bash
cd your-project
npx cc-sdd@latest
```

**VN:** Mặc định cài cho Claude Code (`--claude-skills`). Để cài cho platform khác, thêm flag tương ứng:

**EN:** Default install targets Claude Code. For other platforms, add the corresponding flag:

| Platform | Status | Flag |
|---|---|---|
| Claude Code | Stable | `--claude-skills` (default) |
| Codex | Stable | `--codex-skills` |
| Cursor IDE | Beta | `--cursor-skills` |
| GitHub Copilot | Beta | `--copilot-skills` |
| Windsurf IDE | Beta | `--windsurf-skills` |
| OpenCode | Beta | `--opencode-skills` |
| Gemini CLI | Beta | `--gemini-skills` |
| Antigravity | Experimental | `--antigravity` |

**Ngôn ngữ / Language:**
```bash
npx cc-sdd@latest --lang ja           # Japanese
npx cc-sdd@latest --lang zh-TW        # Traditional Chinese
# 13 ngôn ngữ tổng (Greek added v2.0.5)
```

**Caveat / Lưu ý:**
- 5/8 platforms vẫn beta (Cursor / Copilot / Windsurf / OpenCode / Gemini CLI). Antigravity experimental.
- Production-stable chỉ trên Claude Code + Codex.

---

## 5. Workflow cốt lõi / Core usage pattern

**VN — quy trình 6 bước:**

```
1. /kiro-discovery <ý tưởng>
   → routing decision + brief.md (+ roadmap.md nếu multi-feature)
   → 5 outcome: extend spec / direct impl / single spec / multi-spec / no-spec-needed

2. /kiro-spec-init <feature-name>
   → tạo spec.json + thư mục .kiro/specs/<feature>/

3. /kiro-spec-requirements <feature-name>
   → requirements.md theo EARS-format
   ⚠️ HUMAN APPROVAL GATE — review + duyệt requirements

4. /kiro-spec-design <feature-name>
   → design.md (architecture + Mermaid diagrams + File Structure Plan)
   → research.md (nếu cần investigate)
   ⚠️ HUMAN APPROVAL GATE

5. /kiro-spec-tasks <feature-name>
   → tasks.md (P-waves priority + Boundary markers + dependency annotations)
   ⚠️ HUMAN APPROVAL GATE

6. /kiro-impl
   → autonomous mode: subagent dispatch, fresh-roles per iteration
     - Implementer subagent (TDD: RED → GREEN → REFACTOR)
     - Reviewer subagent (kiro-review: spec compliance / boundary / mechanical / RED-evidence)
     - On rejection: kiro-debug → fix → retry
     - On pass: kiro-verify-completion → VERIFIED → mark complete
```

**EN — same 6-step flow** — see `02 Wiki/(C) cc-sdd entity.md` §5 for ASCII diagram.

**Optional validation gates / Quality gates không bắt buộc:**
- `/kiro-validate-gap` — brownfield codebase analysis
- `/kiro-validate-design` — design review with GO/NO-GO assessment
- `/kiro-validate-impl` — implementation validation against requirements + design + test coverage

---

## 6. Khái niệm / Key architectural choices

### 6.1 Steering vs Specs

**VN:** cc-sdd phân chia rõ ràng giữa:
- **Steering** (`.kiro/steering/`): rules + context cho cả project, dài-hạn
  - Default: `product.md` (business context) + `tech.md` (technology decisions) + `structure.md` (directory map)
  - Custom: API standards / testing practices / security / domain-specific
- **Specs** (`.kiro/specs/<feature>/`): development process cho từng feature, scoped theo feature

**EN:** Clean separation between project-wide (steering) and feature-scoped (specs).

### 6.2 EARS-format requirements

**VN:** EARS = Easy Approach to Requirements Syntax — chuẩn requirements từ aerospace/systems engineering. cc-sdd dùng EARS cho `requirements.md` để có testable acceptance criteria thay vì free-form prose.

**EN:** EARS-formatted acceptance criteria over free-form prose for testability.

### 6.3 File Structure Plan (FSP)

**VN:** Sub-section trong `design.md` mapping directory structure + file responsibilities. Là "boundary contract" giữa các module: ai chịu trách nhiệm gì, allowed dependencies, downstream revalidation needs.

**EN:** Sub-section in `design.md` mapping directory structure + per-file responsibility ownership.

### 6.4 P-wave priority + Boundary marker

**VN:** Trong `tasks.md`:
- P0 = blocking work (chặn các P khác)
- Same P# = concurrent-safe (có thể chạy song song)
- Boundary marker per-task: định nghĩa trách nhiệm local của task đó

**EN:** Task-priority + concurrency-safety annotation in single primitive.

### 6.5 Adversarial review architecture

**VN:** `/kiro-impl` dispatch 2 subagent với role tách biệt:
- **Implementer** làm code (TDD)
- **Reviewer** kiểm tra spec compliance + boundary fit + mechanical verification + RED-phase evidence
- Khi reviewer reject → `kiro-debug` returns ROOT_CAUSE + FIX_PLAN
- Trước khi mark task complete → `kiro-verify-completion` returns VERIFIED / NOT_VERIFIED / MANUAL_VERIFY_REQUIRED

**EN:** Separate implementer + reviewer subagents with auto-debug-on-rejection loop and fresh-evidence completion gate.

---

## 7. So sánh với corpus framework khác / vs other corpus frameworks

| Dimension | spec-kit v17 | OpenSpec v58 | GSD v5 + gsd-2 v54 | **cc-sdd v61** |
|---|---|---|---|---|
| **Org archetype** | Microsoft corporate | Fission-AI pseudonymous-org | gsd-build solo-product-line | **gotalab solo-Japanese** |
| **Methodology shape** | 9-article constitution | per-tool format translation (30+ tools) | feature-shaped SDD | **Multi-platform Skills harness + Kiro IDE lineage** |
| **Multi-platform** | None | 30+ tools | None | **8 AI agent platforms** |
| **Workflow steps** | 3 (specify/plan/tasks) | varies per tool | feature-level | **6 (discovery → spec init → req → design → tasks → impl)** |
| **Approval gates** | constitution-gates | varies | implicit | **3 explicit human-approval gates** |
| **Adversarial review** | absent | absent | absent | **reviewer subagent + auto-debug** |
| **Vibe-coding stance** | Pure anti-vibe | Anti-vibe | Anti-vibe-light | **Anti-vibe-with-pragmatic-acknowledgment** |
| **Marketplace** | 80+ ecosystem | None | None | None |
| **Stars** | unknown | 45.8K | varies | **3.3K** |

**Key takeaway / Điểm khác biệt chính:**
- cc-sdd có **adversarial review architecture** ở framework level — không có ở 3 frameworks SDD trước
- cc-sdd **acknowledge vibe-coding** thay vì rejecting tuyệt đối — counter-evidence cho Pattern #51
- cc-sdd có **Kiro IDE methodology lineage** — first non-AI-ecosystem methodology lineage trong corpus
- cc-sdd nhỏ hơn (3.3K stars) so với OpenSpec (45.8K) hay spec-kit nhưng có roadmap velocity cao (3 major releases trong 6 tháng)

---

## 8. Ethical framing + Caveats / Khía cạnh đạo đức

### 8.1 Supply-chain awareness

**VN:** cc-sdd KHÔNG phải aggregator-genre (như awesome-mcp-servers / awesome-claude-skills). Chỉ install templates do gotalab maintain. Supply-chain risk thấp.

**EN:** cc-sdd is NOT an aggregator-genre subject. Only installs gotalab-maintained templates. Low supply-chain risk surface.

**Standard npm risk applies:** `npx cc-sdd@latest` runs latest npm package — pin version (`npx cc-sdd@3.0.2`) for production-critical workflows.

### 8.2 Bus factor / Maintainership risk

**VN:** gotalab là solo-Japanese author. 4 sản phẩm pinned (cc-sdd / skillport / uxaudit / claude-code-marimo) — ecosystem-portfolio-builder. Sustainability risk cao hơn corporate (Microsoft) hay org-stewardship (Fission-AI).

**EN:** Solo-author bus-factor concern; mitigated somewhat by ecosystem-portfolio commitment (4 pinned products in Claude Code / Agent Skills space).

### 8.3 Auto-approval flag (`-y`) footgun

**VN:** Cờ `-y` cho `/kiro:spec-design` và `/kiro:spec-tasks` SKIPS human review. Chỉ dùng cho trusted automation workflow — không dùng khi cần governance.

**EN:** `-y` flag bypasses human approval gates — operator footgun if used carelessly.

### 8.4 Long-running autonomous = high token cost

**VN:** `/kiro-impl` autonomous mode chạy long-running, dispatch nhiều subagent → tốn token đáng kể. Cost discipline cần thiết cho production deployment.

**EN:** Autonomous `/kiro-impl` is token-intensive due to subagent dispatch + adversarial review cycles.

### 8.5 Anti-vibe-with-pragmatic-acknowledgment

**VN:** cc-sdd CHẤP NHẬN vibe-coding có legitimate use cases (*"`/kiro-discovery` can legitimately conclude that no specification is needed"*). Đây là position **counter-evidence** so với spec-kit v17 pure anti-vibe. Không phải lỗi — là refinement của Pattern #51 spectrum.

**EN:** cc-sdd's anti-vibe stance is pragmatic, not absolute — counter-evidence narrowing Pattern #51 spectrum nuance.

---

## 9. Storm Bear vault relevance / Mức độ phù hợp với Storm Bear vault

**VN:** **HIGH-OPERATIONAL pilot ranking** (top-3 cùng với free-claude-code v60).

Lý do:
- Storm Bear primary tool: Claude Code → cc-sdd `--claude-skills` install path production-stable
- Storm Bear dual role (software dev + Scrum coach): SDD methodology fit cả hai (3-phase approval gates ↔ Scrum sprint review boundaries)
- 13-language i18n (incl. Japanese) → vault potential VN i18n contribution opportunity
- Adversarial review architecture: provides quality discipline beyond ad-hoc Claude Code

Caveat:
- 6-step workflow over-engineered cho solo-vault-author small features
- Vault projects thường single-feature → không tận dụng multi-spec batch
- gotalab solo-author bus factor concern cho production-critical use

**EN:** HIGH-OPERATIONAL pilot ranking. Direct deployable for Claude Code workflow with SDD discipline overlay.

**Recommended Storm Bear pilot:**
1. Install `npx cc-sdd@latest --claude-skills` in 1 sandbox vault project
2. Run `/kiro-discovery` + `/kiro-spec-init` cho 1 feature nhỏ
3. So sánh với ad-hoc Claude Code workflow trên cùng feature
4. Đo:
   - Discipline-overhead vs value-add
   - Anti-vibe-pragmatism (cc-sdd có thật sự skip spec khi appropriate?)
   - Adversarial review catch-rate (defects prevented vs naive Claude Code)
5. Compare với free-claude-code v60 pilot nếu cả hai pilot complete

---

## 10. Roadmap học 4 tuần / 4-week learning roadmap

### Week 1 — Surface understanding
- Đọc README + AGENTS.md + CLAUDE.md (project root) — ~30 min
- Đọc `docs/guides/why-cc-sdd.md` (philosophy) + `spec-driven.md` (methodology)
- Cài thử: `npx cc-sdd@latest --claude-skills` trong 1 sandbox project
- Chạy `/kiro-discovery` cho 1 ý tưởng nhỏ → quan sát brief.md + routing decision

### Week 2 — Single spec pipeline
- Chạy đầy đủ pipeline cho 1 feature: discovery → spec-init → requirements → design → tasks → impl
- Quan sát kỹ: EARS format trong requirements.md / Mermaid diagrams trong design.md / P-waves trong tasks.md
- Test 3 human-approval gates: thực sự review hay rubber-stamp?

### Week 3 — Adversarial review observation
- Chạy `/kiro-impl` autonomous mode, observe subagent dispatch
- Force 1 spec-violation → quan sát reviewer rejection + kiro-debug loop
- Force 1 mechanical-failure (test breaking) → quan sát auto-debug ROOT_CAUSE / FIX_PLAN

### Week 4 — Customization + comparison
- Edit `.kiro/steering/` custom files cho domain mình
- Compare cc-sdd vs ad-hoc Claude Code workflow
- Decide: sustainable cho daily use, or pilot-only insight tool?
- Document findings → vault `04 Reviews/`

---

## 11. Tradeoffs + Limitations

**Trade-offs:**
- ✅ Discipline + auditability + parallel-safe ↔ ❌ Overhead for small/solo work
- ✅ Multi-platform reach (8 agents) ↔ ❌ 5/8 platforms beta
- ✅ Adversarial review prevents defects ↔ ❌ High token cost from subagent dispatch
- ✅ EARS + FSP + P-waves precision ↔ ❌ Learning curve for unfamiliar primitives
- ✅ Kiro IDE methodology depth ↔ ❌ External lineage = additional dependency to track

**Limitations:**
- No marketplace / plugin ecosystem (vs spec-kit v17 80+ marketplace)
- No persona library (vs BMAD v11)
- Solo-author bus factor risk
- Beta status on 5/8 platforms
- Antigravity experimental (avoid in production)

---

## 12. Caveats + safety notes / Lưu ý + an toàn

- **Pin npm version** for production: `npx cc-sdd@3.0.2` (not `@latest`)
- **Audit `.kiro/` directory** before checking into git: ensure no sensitive data in `brief.md` / `requirements.md`
- **Test `-y` auto-approval** in sandbox first; never use `-y` for production-critical features without prior trust
- **Token cost monitoring**: `/kiro-impl` autonomous mode runs long; set budget alerts
- **Beta platform caveats**: Cursor / Copilot / Windsurf / OpenCode / Gemini CLI behavior may differ from Claude Code reference
- **External methodology dependency**: Kiro IDE methodology evolution affects cc-sdd; track Kiro IDE updates if production-critical
- **License compatibility**: MIT — compatible with most commercial use; verify if your downstream license has constraints

---

## 13. References + Next action

**Repository:** https://github.com/gotalab/cc-sdd

**Documentation:**
- README.md — overview + installation + supported platforms + workflow
- AGENTS.md — cross-agent compatibility note + autonomy heuristic
- CLAUDE.md (project root) — agentic SDLC + 3-phase approval workflow
- CHANGELOG.md — v0.0.1 → v3.0.2 release history
- `docs/guides/why-cc-sdd.md` — positioning + when-to-use vs when-NOT
- `docs/guides/spec-driven.md` — SDD methodology detailed
- `docs/guides/skill-reference.md` — 6 primary skills detail
- `docs/guides/command-reference.md` — v2.x command set (still available; v3.0+ uses Skills mode primary)

**Sibling corpus wikis:**
- [spec-kit v17](../../spec-kit%20-%20Beginner%20Analysis/) — Microsoft official SDD
- [OpenSpec v58](../../OpenSpec%20-%20Beginner%20Analysis/) — Fission-AI per-tool SDD
- [GSD v5](../../get-shit-done%20-%20Beginner%20Analysis/) + [gsd-2 v54](../../gsd-2%20-%20Beginner%20Analysis/) — gsd-build SDD lineage
- [free-claude-code v60](../../free-claude-code%20-%20Beginner%20Analysis/) — T4 multi-provider proxy (HIGH-OPERATIONAL pilot peer)
- [mattpocock-skills v57](../../mattpocock-skills%20-%20Beginner%20Analysis/) — Agent Skills builder

**Phase 4b deliverable:** `03 Published/(C) Pattern 21 un-stale - SDD methodology promotion case at v61.md` — detailed Pattern Library un-stale case + promotion-recommendation for next mini-audit.

**Next action / Bước tiếp theo:**

1. **Storm Bear pilot:** Install `npx cc-sdd@latest --claude-skills` in 1 sandbox vault project (~1h setup) → 1-week measurement → write-up in `04 Reviews/`
2. **Pattern Library:** at next mini-audit (v63 natural cadence per pre-registered v60 audit triggers), evaluate Pattern #21 un-stale + promotion under criterion #2 structural-unambiguity-at-N=2
3. **Corpus monitoring:** watch v62-v65 for T2-T5 SDD framework (would satisfy Pattern #21 default-criterion #1 cross-tier) and 2nd external-IDE-methodology lineage observation
