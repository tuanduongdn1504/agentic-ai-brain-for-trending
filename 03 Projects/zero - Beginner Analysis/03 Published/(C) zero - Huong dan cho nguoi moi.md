# (C) zero (vercel-labs) — Hướng dẫn cho người mới

> **Bilingual: VN primary, EN technical.** v68 wiki ship — 2026-05-18.
> Subject: [github.com/vercel-labs/zero](https://github.com/vercel-labs/zero) (Homepage: [zerolang.ai](https://zerolang.ai))

---

## 1. Nó là gì? / What is it?

**TL;DR (VN):** **Zero là một ngôn ngữ lập trình mới do Vercel Labs phát hành** (sub-org của Vercel main) với khái niệm cốt lõi là **"agent-first"** — nghĩa là **agents (LLM-based AI agents như Claude, Cursor, etc.) là người dùng chính từ ngày đầu**, không phải là afterthought sau khi thiết kế cho con người. Đây là một ngôn ngữ pre-1.0 (v0.1.2), thử nghiệm, **ra mắt chỉ 2 ngày trước thời điểm wiki này được build** (v0.1.0 ra mắt 2026-05-16, wiki build 2026-05-18). Tốc độ phát triển cực kỳ nhanh: 91 commits + 3 releases trong 2 ngày, 2,100 stars = **1,050 stars/ngày** (cao thứ 2 trong toàn bộ 67-wiki corpus, chỉ sau karpathy-skills v63 với ~1,186/ngày).

**TL;DR (EN):** Zero is Vercel Labs' agent-first programming language. Pre-1.0 experimental; 2 days old at wiki build; corpus-2nd-highest velocity at 1,050 stars/day. Treats AI agents as primary users from day one — language design, stdlib structure, tooling, and skill packaging all optimized for agent consumption rather than human consumption.

**⚠️ Cảnh báo chính (CRITICAL WARNING — verbatim from README + AGENTS.md):**

> *"Security vulnerabilities should be expected. Zero is not ready for production systems, sensitive data, or trusted infrastructure. If you plan to run or develop Zero, do so in an isolated, disposable environment."*

Đây không phải lời cảnh báo template — README + AGENTS.md đều khẳng định:
- ⚠️ Compiler crashes có thể xảy ra
- ⚠️ Malformed output có thể được generate
- ⚠️ Unsafe runtime behavior có thể manifest
- ⚠️ Không an toàn cho production / sensitive data / trusted infrastructure
- ⚠️ Chỉ chạy trong **isolated, disposable environment** (e.g., Docker container, VM throwaway, sandbox)

---

## 2. Tín hiệu corpus-first / Corpus-first signals

Zero v68 có **12+ đặc điểm corpus-first** (lần đầu xuất hiện trong vault 68-wiki cumulative):

1. **CORPUS-FIRST programming-language subject** — 67 wikis trước đều là skill collections, agent frameworks, plugins, etc. Zero là wiki đầu tiên về **một ngôn ngữ lập trình thực thụ**.
2. **CORPUS-FIRST C-primary language subject** — C 65.9% của codebase. Trước đó corpus có TypeScript / Python / Markdown làm primary, không có C.
3. **CORPUS-FIRST explicit "agent-first" design philosophy** — agents là primary users, không phải augmentee. Đây là design axiom inversion (đảo ngược giả thuyết thiết kế truyền thống).
4. **CORPUS-FIRST self-hosted compiler bootstrap architecture** — `native/zero-c/` (C bootstrap) + `compiler-zero/` (Zero-authored, self-hosted). Classic compiler engineering pattern, lần đầu xuất hiện trong corpus.
5. **CORPUS-FIRST Skill-As-Binary-Bootstrap mechanism** — SKILL.md là "discovery stub" mỏng, content thật được compiler binary serve qua `zero skills get zero --full`. Giải pháp đột phá cho skill-version-drift problem.
6. **CORPUS-FIRST in-browser-compiler-via-WASM** — compiler-zero/ compile thành WASM cho docs-site playground tại zerolang.ai.
7. **CORPUS-FIRST Rust-style borrow checking as language feature** — v0.1.2 CHANGELOG chi tiết "borrow provenance tracking" + "borrow conflict checking from provenance and concrete places".
8. **CORPUS-FIRST anti-compatibility-as-project-policy** — AGENTS.md explicit: "Do not preserve legacy behavior by default."
9. **CORPUS-FIRST synchronicity-discipline-as-policy** — examples + docs + tests + command-contracts phải align với current behavior; repo phải describe "one coherent current system".
10. **CORPUS-FIRST fix-plan-as-first-class-primitive at compiler level** — `bin/zero fix --plan --json` produces structured plan that agents can inspect before applying.
11. **CORPUS-FIRST corporate-published-but-individual-maintained sub-pattern** — Vercel Labs publishes Zero corporately, nhưng `@ctate` maintains individually với release-branch namespace `ctate/v0.1.x`.
12. **CORPUS-FIRST 8-layer test pipeline at 2-day-old project** — conformance + native + WASM + zero + docs + ZLS + agent-demo + workspace.

**Corpus-records (records, không phải first-occurrences):**
- 2nd-highest velocity in corpus history: 1,050 stars/day (chỉ sau karpathy-skills v63 ~1,186/day)
- Corpus-record release cadence: 1.5 releases/day (3 releases trong 2 ngày)

---

## 3. Phân loại theo Tier system (corpus taxonomy)

**Tier (PROVISIONAL):** **T1 Augmentation NEW sub-archetype #7 "programming-language-as-agent-substrate"** — được đề nghị cho v69 Tier-Taxonomy Review T6 để chính thức quyết định: T1-extension HOẶC NEW Tier T6 Language/Runtime substrate.

| Trục phân loại | Giá trị |
|---------------|---------|
| Archetype | corporate-strategic-lab (Vercel Labs experimental sub-org) |
| Quy mô | small (2.1K stars at 2 days old) but EXTREME-VIRAL velocity |
| Ngôn ngữ chính | **C 65.9%** (corpus-first) + JavaScript 26.9% + Shell 5.4% |
| Đóng gói | curl-installer-shellscript + npm workspaces + native make |
| Origin story | corporate-strategic-lab experiment |
| Methodology | NEW corpus methodology: agent-first language design |
| Governance file count | 5 (README + AGENTS.md + CHANGELOG + LICENSE + package.json) — medium |
| Agent/skill count | 1 SKILL.md bootstrap + 7+ inner skills served by compiler binary |
| i18n | EN-only |
| Influence cited | NONE (corpus-first explicit "agent-first" framing) |
| Living-Domain-Standards Tracking | NO (Zero establishes its own standards) |

**So sánh với corpus siblings:**
- **v51 agent-skills-of-vercel**: STRONG sibling — same Vercel umbrella org parent (vercel-labs is sub-org)
- **v63 andrej-karpathy-skills**: velocity-record sibling (corpus-record 1,186 stars/day; Zero v68 is 2nd at 1,050)
- **v62 codex-plugin-cc**: corporate-strategic sibling (different vendor)
- **v66 agentmemory**: skills-protocol-integration sibling (different protocol mechanism — agentmemory uses MCP runtime, Zero uses Skill-As-Binary-Bootstrap)
- **v67 opencode-antigravity-auth**: adjacent v2.2-routine wiki + Pattern #83 N=3→N=4 strengthening chain

---

## 4. Cách cài đặt / Installation

**⚠️ Đọc warning ở Section 1 trước khi cài. Sử dụng isolated environment (Docker, VM, throwaway machine).**

### Quick install (verbatim từ README)

```bash
curl -fsSL https://zerolang.ai/install.sh | bash
export PATH="$HOME/.zero/bin:$PATH"
zero --version
```

**Install pipeline (chi tiết per CHANGELOG v0.1.1):**
1. `curl` fetches `install.sh` từ `zerolang.ai` (Vercel-hosted Vercel-Labs domain)
2. Script detect platform (Linux / Darwin / etc.)
3. Download platform-specific binary từ GitHub Releases
4. **Verify checksum** (corpus-distinctive supply-chain-aware install step)
5. Install vào `$HOME/.zero/bin/zero`

### Kiểm tra cài đặt

```bash
zero --version              # Display version (v0.1.2 hiện tại)
zero doctor --json          # Environment diagnostics (machine-readable)
```

---

## 5. Cách sử dụng cơ bản / Core usage pattern

### 5.1 Compile + Run

```bash
# Check a program (type/syntax checking)
zero check examples/hello.0

# Build + execute in one command
zero run examples/add.0
# Expected output: "math works"

# Build to executable file
zero build --emit exe --target linux-musl-x64 examples/add.0 --out .zero/out/add
```

### 5.2 Agent-friendly inspection (JSON output)

5 trong 8 common commands có `--json` flag — output dạng JSON cho agents consume mechanically:

```bash
zero check --json <file>                  # Type/syntax issues as JSON
zero graph --json <file-or-package>       # Module graph as JSON
zero size --json <file>                   # Program size report as JSON
zero routes --json <web-package>          # Web routes as JSON
zero fix --plan --json <file>             # Fix plan (NOT auto-applied) as JSON
zero explain <diagnostic-code>            # Explain diagnostic code
zero doctor --json                        # Environment health as JSON
```

### 5.3 Skills integration (Skill-As-Binary-Bootstrap)

```bash
# List skills bundled with this compiler version
zero skills list

# Get a specific skill (returns version-matched content)
zero skills get zero
zero skills get zero --full

# 7 known inner skills (full content via compiler):
# zero-agent     — agent workflow guidance
# zero-language  — language syntax + semantics
# zero-diagnostics — diagnostic codes + explanations
# zero-packages  — package management
# zero-builds    — build targets + emit options
# zero-testing   — testing patterns
# zero-stdlib    — standard library usage
```

**Multi-binary case:** Nếu user có multiple Zero binaries (e.g., project-local installations với version khác nhau):

```bash
/path/to/specific/zero skills get zero --full   # Match content with binary
```

---

## 6. Concept mới + Kiến trúc / Novel concepts + Architectural choices

### 6.1 5 design axioms (agent-first programming language design)

Zero's design philosophy có 5 axioms explicit trong README:

1. **Agent-first learnability** — surface ngôn ngữ nhỏ + regular để agents pick up nhanh từ examples + docs + compiler feedback
2. **Standard-library depth** — common capabilities sống trong stdlib thay vì dependency stacks. Agents không cần search "package nào cho X"
3. **Deterministic tooling** — diagnostics, graph facts, size reports, fix plans STRUCTURED enough để agents inspect và act on
4. **Direct developer experience** — checking + running + formatting + inspecting + repairing fast, copyable, scriptable
5. **Regularity over syntax** — "one obvious way" cho hầu hết operations, kể cả khi code dài hơn so với ngôn ngữ khác

**Axiom 5 đặc biệt corpus-first:** Zero EXPLICITLY prefers verbose-but-regular over concise-but-irregular. Most languages optimize for human-conciseness; Zero inverts for agent-parseability.

### 6.2 Self-hosted compiler bootstrap (corpus-first)

```
native/zero-c/          ← Bootstrap compiler written in C
  src/main.c            ← Entry point (version bumped at each release)
  Makefile              ← `make -C native/zero-c` to build native binary

compiler-zero/          ← Self-hosted compiler written in Zero
                        ← `bin/zero build --emit wasm --target wasm32-web compiler-zero`
                        ← Compiles to WASM for in-browser playground
```

**Tại sao 2 compilers?** Classic bootstrap pattern:
1. Write the language trong language khác trước (C cho Zero)
2. Use bootstrap compile self-hosted version (Zero → Zero compiler)
3. Eventually retire bootstrap khi self-hosting complete (aspirational; hiện tại both retained)

### 6.3 Skill-As-Binary-Bootstrap mechanism (corpus-first)

**Problem:** Skill content static có thể drift khỏi runtime/compiler version.

**Zero's solution:**

```
skills/zero/SKILL.md (thin stub — registers skill in skill manager)
   ↓ "Do not treat as full workflow"
   ↓
zero skills get zero --full (compiler binary serves version-matched content)
   ↓
skill-data/ (bundled into native binary at build time)
```

**Mechanism:**
1. Skill manager (Claude Code's skills plugin / Cursor / etc.) discovers ONE Zero skill via thin SKILL.md
2. Stub directs agent to invoke `zero skills get zero --full`
3. Native compiler binary returns version-matched content
4. Multi-binary case: agent uses same binary as project (`/path/to/zero skills get`)

**Tại sao đặc biệt:**
- Skill manager chỉ register 1 entry (không proliferate)
- Binary owns skill content (version-coupled at install time)
- Update Zero → skill content auto-update

### 6.4 8-layer test pipeline (corpus-distinctive at 2-day-old project)

```bash
npm test  # Runs all 8 layers chained:
```

1. `conformance` — language + CLI fixture conformance
2. `native:test` — native compiler tests (sandboxed via `@vercel/sandbox`)
3. `wasm:runtime:smoke` — WASM target smoke
4. `test:zero` — Zero-authored test files
5. `docs:test` — docs-site tests
6. `zls --self-test` — language server self-test
7. `agent:demo` — `scripts/agent-repair-demo.mjs` (agent-first repair flow as test)
8. `test -w zero-lang` — workspace extension tests

### 6.5 `bin/zero fix --plan --json` (corpus-first fix-plan primitive)

Truyền thống: `fix --auto` áp dụng changes ngay lập tức (destructive).
Zero: `fix --plan` chỉ produces plan structure (JSON), agent có thể inspect BEFORE applying.

Cho agents — đặc biệt useful: receive plan → validate → optionally apply.

---

## 7. So với corpus frameworks khác / vs other corpus frameworks

| Subject | Tier | Skills protocol mechanism | Velocity at observation | Vendor archetype |
|---------|------|---------------------------|--------------------------|-------------------|
| **zero (vercel-labs)** | **PROVISIONAL T1 NEW sub-archetype #7 programming-language-as-agent-substrate** | **Skill-As-Binary-Bootstrap (thin stub → binary-served)** | **1,050 stars/day (2 days old)** | corporate-strategic-lab |
| v51 agent-skills-of-vercel | T1 corporate-curated | Static SKILL.md (28 skills) | (early Vercel skills launch) | corporate-curated |
| v63 andrej-karpathy-skills | T1 single-artifact | Static SKILL.md (7 frontmatter-only) | 1,186 stars/day (102 days) | viral-distillation |
| v66 agentmemory | T2 Service | Runtime-served via MCP (51 tools + 107 REST endpoints) | 226 stars/day (35 days) | solo Platform-Primitive |
| v67 opencode-antigravity-auth | T4 Bridge | N/A (auth plugin, not skill collection) | 66 stars/day (159 days) | solo legally-gray-utility |

**Diagnostic differences:**
- Zero v68 is **the first programming language in corpus** — fundamentally different subject type
- Zero's Skill-As-Binary-Bootstrap is **corpus-first mechanism** — combines static-stub + runtime-served-content
- Zero's velocity at 2 days old shows extreme-launch-momentum; v69 audit tests sustained-velocity

---

## 8. Ethical framing / Khung đạo đức

Zero is a **pre-1.0 experimental language with explicit honest-deficiency-disclosure**. Khác với một số corpus subjects (e.g., v67 opencode-antigravity-auth có TOS-violation framing), Zero's framing là legitimate-experimental:

- **Author intent:** Vercel Labs experimental incubation, không phải production tool
- **License:** Apache-2.0 (permissive open source)
- **Honesty:** "Security vulnerabilities should be expected" stated upfront
- **Use case boundary:** "Not for production systems, sensitive data, or trusted infrastructure"

**Compared with v67 opencode-antigravity-auth:**
- v67: TOS-violation tool with explicit risk framing
- v68: legitimate experimental tool with explicit limitation framing

Both qualify Pattern #83 honest-deficiency-disclosure but at different risk axes.

**Đối với Storm Bear / vault operator context:**
- ✅ Pre-1.0 experimental tool có quyền tồn tại — encouraging field experimentation
- ✅ Apache-2.0 permissive license cho phép vault adopt nếu domain match
- ❌ Vault uses Markdown + Claude Code, không phải programming language context — domain mismatch
- ❌ Pre-1.0 instability không acceptable cho client-facing Scrum-coaching work
- ⚠️ Có thể experiment với Zero trong throwaway personal environment cho learning về compiler internals + agent-first language design

---

## 9. Liên quan tới Storm Bear / Storm Bear relevance (VN operator + Scrum coach fit)

**Phase 0.9 STRICT verdict:** **WEAK INCLUDE — 1/4 PASS** (FIRST WEAK in post-amendment window v57-v68):
- (a) **FAIL** — Vercel Labs is corporate-strategic-lab, không phải solo-engineer-coach peer
- (b) **FAIL** — Zero pre-1.0 experimental C-primary language, không vault-deployable
- (c) **FAIL** — Vercel không methodology-influence-node cho vault routines
- (d) **PASS** — vercel-labs là sub-org của Vercel main (v51 corpus subject parent); `@vercel/sandbox` dep linked to Vercel ecosystem; skills protocol integration anchors to corpus convention

**What Storm Bear can learn (despite WEAK INCLUDE):**

1. **Pre-1.0 honesty disclosure as branding asset** — 2,100 stars trong 2 ngày DESPITE (or because of) "Security vulnerabilities should be expected" framing. Honest disclosure không suppress adoption; nó strengthen credibility. Vault application: lead with explicit limitations + counter-evidence khi publishing wiki content publicly.

2. **"One coherent current system" repository discipline** — Zero's AGENTS.md đòi hỏi examples + docs + tests + contracts align với current behavior. Vault application: routine v2.2 evolution → tất cả dependent artifacts (skills + project CLAUDE.md templates + state-block) phải evolve cùng nhau. v68 housekeeping pass demonstrate this pattern.

3. **Structured-JSON-as-first-class CLI output** — Zero ưu tiên machine-readable output cho agents consume mechanically. Vault application: future routine v2.3 có thể codify structured-state-block format thay vì narrative.

4. **Anti-compatibility as deliberate policy** — Zero's framing là counter-discipline cho vault context. Vault valuates backward compatibility (v2.1 → v2.2 → v2.3 carry forward). Diagnostic question: fresh-slate situation (anti-compat) vs accumulated-state situation (compat)?

5. **Skill-As-Binary-Bootstrap mechanism** — Aspirational vault lesson: skill content auto-version-matched với runtime. Vault hiện không có "runtime", nhưng nguyên tắc (skill manager registers 1 entry, content lives elsewhere with version coupling) có thể inform future vault routine design.

**Pilot ranking:** **NOT a pilot candidate** — domain mismatch + pre-1.0 instability + intended-use disclaimer. Useful as comparative reference khi pilot khác T1-NEW-sub-archetype subjects hoặc evaluate Skill-As-Binary-Bootstrap mechanism.

---

## 10. Lộ trình học tập 4 tuần / 4-week learning roadmap (nếu vẫn muốn explore — for experimentation only)

### Tuần 1 — Understand context

- Đọc README (73 lines) — paying attention đến 5 design axioms + pre-1.0 disclosure
- Đọc AGENTS.md (107 lines) — hiểu project direction + safety expectations + release workflow
- Đọc CHANGELOG (44 lines) — narrative của v0.1.0 → v0.1.1 → v0.1.2 trong 2-day window
- Visit zerolang.ai docs site for tutorials (nếu có)
- KHÔNG install plugin chưa — chỉ đọc

### Tuần 2 — Local sandbox setup

- Tạo isolated environment: Docker container hoặc VM throwaway
- Install Zero: `curl -fsSL https://zerolang.ai/install.sh | bash`
- Verify: `zero --version` + `zero doctor --json`
- Run hello example: `zero run examples/add.0` (expect "math works")
- Inspect JSON output: `zero check --json` + `zero graph --json` + `zero size --json`
- Observe behavior 1-2 ngày

### Tuần 3 — Agent integration experimentation

- Try `zero skills list` + `zero skills get zero --full` to understand Skill-As-Binary-Bootstrap mechanism
- Install VS Code extension (`extensions/vscode/` workspace member)
- Try language server: `npm run zls -- --self-test`
- Experiment with `zero fix --plan --json` workflow (request fix plan, inspect, optionally apply)
- Browse zerolang.ai playground (in-browser WASM compiler)

### Tuần 4 — Evaluation + decision

- Đọc compiler-zero/ sources (self-hosted Zero compiler written in Zero)
- Đánh giá: does Zero's agent-first framing change how YOU write programs?
- Compare với mainstream language (TypeScript / Python / Rust) trên trục agent-readability
- Decision: continue exploring (personal learning), uninstall (not aligned with current work), or contribute (open PR with Apache-2.0 contribution)

---

## 11. Tradeoffs + limitations

**Pros:**
- ✅ Corpus-first programming-language-as-agent-substrate design — novel research direction
- ✅ Strong design discipline (5 explicit axioms; anti-compatibility + synchronicity policies)
- ✅ Structured-JSON-as-first-class output (8 commands; 5 with --json)
- ✅ Skill-As-Binary-Bootstrap solves skill-version-drift problem
- ✅ Self-hosted compiler bootstrap (classic compiler engineering done well)
- ✅ In-browser WASM playground at zerolang.ai
- ✅ Apache-2.0 permissive license
- ✅ Active maintenance (corpus-record 1.5 releases/day in 2-day window)

**Cons:**
- ❌ **Pre-1.0 experimental** — "Security vulnerabilities should be expected" verbatim disclosure
- ❌ Not for production systems / sensitive data / trusted infrastructure
- ❌ Anti-compatibility means breaking changes are the default — your code may break across versions
- ❌ Single maintainer (`@ctate`) for releases despite Vercel Labs corporate publishing — bus-factor concern
- ❌ Domain narrow — programming language is wrong tool for many use cases (e.g., vault Markdown)
- ❌ C 65.9% codebase — most agents not optimal at C
- ❌ 2-day-old project means tooling ecosystem is still forming
- ❌ Velocity-vs-substance test pending — 1,050 stars/day in 2 days may decay; sustained velocity TBD at v69 audit

**Decision matrix:**

| Use case | Recommended? |
|----------|--------------|
| Production client work | ❌ NO |
| Personal experimentation with throwaway environment | ⚠️ Yes (with caveats) |
| Learning agent-first language design principles | ✅ YES (read README + AGENTS.md) |
| Contributing to Zero (Apache-2.0 + open community) | ✅ YES (welcome to engage) |
| Building production tools in Zero | ❌ NO (pre-1.0 unstable) |
| Reference for evaluating "agent-first" framing in other tools | ✅ YES (corpus reference implementation) |

---

## 12. Caveats + safety notes / Ghi chú an toàn

**Supply-chain awareness:**
- Install via `curl -fsSL https://zerolang.ai/install.sh | bash` includes checksum verification (corpus-distinctive)
- Binary stored at `$HOME/.zero/bin/zero` — verify integrity if security-sensitive
- Native tests sandboxed via `@vercel/sandbox` by default — `local` variants require `ZERO_NATIVE_TEST_ALLOW_LOCAL=1` env guard

**Operational safety (verbatim from AGENTS.md):**
- *"Run and develop Zero in safe environments: isolated workspaces, disposable inputs, and systems where compiler crashes, malformed output, or unsafe runtime behavior cannot damage production state."*
- *"Treat generated artifacts and examples as experimental unless they have been reviewed for the specific environment where they will run."*

**Compatibility expectations:**
- Breaking changes are the project's DEFAULT (per AGENTS.md anti-compatibility stance)
- Don't pin Zero programs to specific compiler version expecting forward-compatibility
- Re-validate code against new versions; assume APIs WILL change

**Skills integration awareness:**
- Skill content is bundled with binary at build time → upgrading Zero changes skill content
- Multi-binary scenarios: agents must use SAME binary that will run the project
- Pre-1.0 skill content itself may be incomplete or change between releases

**License + attribution:**
- Apache-2.0 — permissive open source
- Vercel Labs publishes; `@ctate` maintains
- Contributors named per release in CHANGELOG (auto-extracted from commit trailers)

---

## 13. References + next action

**Primary sources:**
- [README.md](https://raw.githubusercontent.com/vercel-labs/zero/main/README.md) (73 lines)
- [AGENTS.md](https://raw.githubusercontent.com/vercel-labs/zero/main/AGENTS.md) (107 lines)
- [CHANGELOG.md](https://raw.githubusercontent.com/vercel-labs/zero/main/CHANGELOG.md) (44 lines; v0.1.0 → v0.1.2)
- [package.json](https://raw.githubusercontent.com/vercel-labs/zero/main/package.json) (49 lines; 40+ scripts)
- [skills/zero/SKILL.md](https://raw.githubusercontent.com/vercel-labs/zero/main/skills/zero/SKILL.md) (51 lines)

**Homepage + docs:**
- [zerolang.ai](https://zerolang.ai) — official site with browser playground
- GitHub: [vercel-labs/zero](https://github.com/vercel-labs/zero)

**Corpus cross-references:**
- [v51 agent-skills-of-vercel — STRONG sibling](../../agent-skills-of-vercel - Beginner Analysis/CLAUDE.md) — Vercel umbrella org parent
- [v63 andrej-karpathy-skills — velocity-record sibling](../../andrej-karpathy-skills - Beginner Analysis/CLAUDE.md) — corpus-record 1,186 stars/day
- [v62 codex-plugin-cc](../../codex-plugin-cc - Beginner Analysis/CLAUDE.md) — corporate-strategic sibling
- [v66 agentmemory](../../agentmemory - Beginner Analysis/CLAUDE.md) — skills-protocol-integration sibling (MCP runtime vs Skill-As-Binary-Bootstrap)
- [v67 opencode-antigravity-auth](../../opencode-antigravity-auth - Beginner Analysis/CLAUDE.md) — adjacent v2.2-routine wiki + Pattern #83 chain

**Wiki cross-references:**
- [Entity 1: The Zero language + agent-first design](../02 Wiki/entity-1-zero-language-and-agent-first-design.md)
- [Entity 2: Compiler architecture + bootstrap pattern](../02 Wiki/entity-2-compiler-architecture-and-bootstrap.md)
- [Entity 3: Skills-Protocol-As-Binary-Bootstrap](../02 Wiki/entity-3-skills-protocol-as-binary-bootstrap.md) — Phase 4b PRIMARY
- [Entity 4: Storm Bear meta-entity (WEAK INCLUDE 1/4)](../02 Wiki/entity-4-storm-bear-meta.md)
- [NEW T1 sub-archetype registration proposal](../01 Analysis/(C) T1-programming-language-as-agent-substrate NEW sub-archetype registration.md)

**Next action (suggested):**

🎯 **Đối với Storm Bear / vault operator:** Không deploy Zero. Đọc CLAUDE.md v68 entry để hiểu Phase 4b PRIMARY (NEW T1 sub-archetype + Skill-As-Binary-Bootstrap mechanism) + v69 Tier-Taxonomy Review T6 motivation (T1 sub-archetype #7 vs NEW Tier T6).

🎯 **Đối với người mới muốn learn:** Bắt đầu từ Tuần 1 (read-only study) trong roadmap section 10. Không install Zero cho đến khi setup isolated environment. Apache-2.0 + permissive welcomes engagement.

🎯 **Đối với compiler engineers:** Zero's self-hosted compiler bootstrap (`native/zero-c/` + `compiler-zero/`) is corpus reference implementation. Đọc CHANGELOG v0.1.2 cho borrow checker provenance tracking details.

🎯 **Đối với language designers:** Zero's 5 design axioms (agent-first learnability + standard-library depth + deterministic tooling + direct DX + regularity-over-syntax) là corpus-first explicit articulation của agent-first design philosophy. Excellent reference for evaluating "is this language agent-friendly?".
