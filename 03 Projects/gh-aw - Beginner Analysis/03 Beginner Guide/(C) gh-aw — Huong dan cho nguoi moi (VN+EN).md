# (C) gh-aw — Hướng dẫn cho người mới (VN + EN)

> **Wiki #48** | **2026-04-25** | Bilingual beginner guide for github/gh-aw — GitHub CLI extension that compiles natural-language markdown agentic-workflow specs into GitHub Actions YAML.

---

## ⚠️ Read this first — Trách nhiệm bảo mật / Security responsibility

**VN:** gh-aw cho phép AI agents chạy tự động trên GitHub repo của bạn. Nếu cấp quyền sai, agent có thể: ghi/xoá file, push lên main branch, comment trên issue/PR, tiêu API budget của bạn, hoặc rò rỉ secrets. **Đây KHÔNG phải pilot evaluation thông thường.** Trước khi deploy, bạn phải:
- Hiểu 7-layer defense-in-depth architecture của gh-aw
- Đọc Security Architecture Specification (W3C-style 130+ requirements)
- Cấu hình AWF (Agent Workflow Firewall) cho network isolation
- Bắt đầu với read-only permissions + manual approval gates
- Test trong fork/sandbox repo trước khi deploy production

**EN:** gh-aw lets AI agents run autonomously on your GitHub repo. With wrong permissions, an agent could: write/delete files, push to main branch, comment on issues/PRs, burn your API budget, or leak secrets. **This is NOT a casual pilot evaluation.** Before deployment, you must:
- Understand gh-aw's 7-layer defense-in-depth architecture
- Read the W3C-style Security Architecture Specification (130+ formal requirements)
- Configure AWF (Agent Workflow Firewall) for network isolation
- Start with read-only permissions + manual approval gates
- Test in a fork/sandbox repo before deploying to production

README verbatim: *"Using agentic workflows in your repository requires careful attention to security considerations and careful human supervision, and even then things can still go wrong. Use it with caution, and at your own risk."*

---

## 1. gh-aw là gì? / What is it?

**VN:** **gh-aw** = GitHub CLI extension (`gh aw` subcommand) compile natural-language markdown agentic-workflow specs (`.md`) thành executable GitHub Actions YAML lock files (`.lock.yml`). Cho phép viết AI-agent-driven CI/CD workflows bằng markdown thay vì handcrafted YAML.

**EN:** **gh-aw** = a GitHub CLI extension (`gh aw` subcommand) that compiles natural-language markdown agentic-workflow specs (`.md`) into executable GitHub Actions YAML lock files (`.lock.yml`). Lets you write AI-agent-driven CI/CD workflows in markdown rather than handcrafted YAML.

**Tagline:** "Write agentic workflows in natural language markdown, and run them in GitHub Actions."

**Equation:** GitHub Agentic Workflows = Actions + Agent + Safety.

## 2. Corpus-first signals / Tín hiệu corpus-first

| Signal | VN summary | EN summary |
|--------|-----------|-----------|
| Markdown-as-source-truth-compiled-to-CI | Workflows viết bằng markdown, compile thành GitHub Actions YAML | Workflows authored in markdown, compiled to GitHub Actions YAML |
| 5-engine first-class | Hỗ trợ Copilot / Claude / Codex / Custom + extensibility | First-class support for Copilot / Claude / Codex / Custom + extensibility |
| W3C-style security spec | Tài liệu spec chính thức 130+ requirements (RFC 2119 MUST/SHOULD), 70+ tests | Formal W3C-style spec with 130+ requirements (RFC 2119), 70+ tests |
| 7-layer defense-in-depth | Compilation-time → Input → Output → Network → Permission → Sandbox → Threat | 7 named layers from compile-time to threat detection |
| 4-repo coordinated sub-ecosystem | gh-aw + AWF + MCP Gateway + Actions library | 4 coordinated repos under github/* parent |
| GitHub Next research-incubation | Migrate githubnext/gh-aw → github/gh-aw v0.40.1 (2026-02-03) | Research-graduated-to-mainline observable pathway |
| 4-researcher CODEOWNERS cluster | Don Syme (F# creator) + Eric Aftandilian + Peli de Halleux + Krzysztof Cieślak (Ionide creator) | GitHub Next 4-researcher cluster lineage |
| AGENTS.md 49.8 KB | Lớn nhất corpus tại github-corporate-official tier | Corpus-largest at github-corporate-official tier |
| `.architecture.yml` thresholds | File-line BLOCKER (2000) + WARNING (1000) + function-line + export-count | Architectural-degradation detection manifest |

## 3. Tier placement (Pattern Library)

**T4 Agent-as-bridge** — 8th T4 entrant + NEW T4i sub-archetype: **agentic-workflow-compiler-for-CICD-bridge**.

**VN:** T4 là tier bridge (cầu nối giữa các surface); gh-aw là cầu nối từ markdown specs đến executable CI/CD workflows. Cùng tier với gws (Google Workspace bridge) / markitdown (file → markdown) / graphify (code → knowledge graph).

**EN:** T4 is bridge tier (between surfaces); gh-aw bridges markdown specs to executable CI/CD workflows. Same tier as gws (Google Workspace bridge) / markitdown (file → markdown) / graphify (code → knowledge graph).

## 4. Cài đặt / Installation

```bash
# 3 install channels (chọn 1)

# Channel 1: GitHub CLI extension (canonical)
gh extension install github/gh-aw

# Channel 2: curl bash installer
curl -sL https://raw.githubusercontent.com/github/gh-aw/main/install-gh-aw.sh | bash

# Channel 3: Homebrew
brew install gh-aw   # availability per release notes

# Verify
gh aw version

# Initialize repo for agentic workflows
cd /path/to/your/repo
gh aw init
```

`gh aw init` tạo: `.gitattributes` + `.github/agents/agentic-workflows.agent.md` (dispatcher) + `.vscode/settings.json` + `.github/mcp.json` + `.github/workflows/copilot-setup-steps.yml`.

## 5. Core usage pattern

### Tạo workflow đầu tiên

```bash
# Method 1: Use Claude/Copilot to generate
gh aw new my-first-workflow
# Or in GitHub Copilot Chat:
# /agent
# > "Create a workflow that summarizes weekly PRs"

# Method 2: Manual creation
cat > .github/workflows/weekly-digest.md <<'EOF'
---
on:
  schedule:
    - cron: '0 9 * * 1'
permissions:
  contents: read
  issues: write
engine: copilot
tools:
  github:
    toolsets: [default]
---

# Weekly Digest

Summarize PRs and issues from the last week into a Markdown report
and post it as an issue comment in the latest open issue.
EOF

# Compile to .lock.yml
gh aw compile

# Run manually (test)
gh aw run weekly-digest

# Audit results
gh aw audit <run-id>
```

### Inspect MCP usage

```bash
gh aw mcp list                          # List all MCP server configs
gh aw mcp inspect weekly-digest         # Inspect MCP usage in workflow
```

## 6. Novel architectural choices / Những lựa chọn kiến trúc novel

| Choice | VN | EN |
|--------|-----|-----|
| Markdown → YAML compilation | Workflows viết bằng tiếng Anh tự nhiên + frontmatter; compile thành YAML | Workflows authored in natural English + frontmatter; compiled to YAML |
| `.lock.yml` track-compiled | File compile được track trong git, KHÔNG bao giờ .gitignore | Compiled lock files tracked in git; NEVER .gitignored |
| 5-engine via frontmatter | `engine: copilot|claude|codex|custom` chọn AI engine per workflow | `engine:` frontmatter selects AI engine per workflow |
| Safe-outputs sanitization | Write operations chỉ qua sanitized `safe-outputs` | Write operations only via sanitized `safe-outputs` |
| Compile-time validation | Schema + permissions + expressions validate trước khi execute | Schema + permissions + expressions validated before execution |
| AWF network firewall | Companion repo cho domain-based egress control | Companion repo for domain-based egress control |
| MCP Gateway | Companion repo route MCP calls qua unified HTTP gateway | Companion repo routes MCP calls through unified HTTP gateway |
| 24-skill engineering library | Mỗi skill = 1 engineering surface; load lazy theo nhu cầu | Each skill = one engineering surface; lazy-loaded on demand |

## 7. So sánh với các framework corpus / vs other corpus frameworks

| Dimension | gh-aw v48 | spec-kit v17 | aidevops v47 | graphify v16 |
|-----------|-----------|--------------|--------------|--------------|
| Tier | T4 (CICD bridge) | T1 (methodology) | T1 (assistant) | T4 (knowledge bridge) |
| Parent | github/* | github/* | solo Marcus Quinn | solo safishamsi |
| Lang | Go | Python | Bash + TS | Python |
| AGENTS.md | 49.8 KB | medium | 22c sub-variant | absent |
| Engines | 5 first-class | spec-driven | OpenCode-primary | Claude Code primary |
| Security | W3C-style 130+ reqs | 9-article constitution | SHA-pinned + AGENTS.md | minimal |
| Companion repos | 3 (AWF + MCP G + Actions) | 0 | 0 | 0 |
| Storm Bear pilot rank | Not top-11 | #3 | #8 | low |

**VN:** gh-aw là **đặc thù CI/CD agentic-workflow** — không phải general-purpose Claude Code skills (như spec-kit) hoặc multi-agent orchestration framework (như aidevops). Phù hợp nếu bạn muốn AI agents chạy theo schedule trong GitHub Actions với security gates rõ ràng.

**EN:** gh-aw is **CI/CD-specific agentic-workflow** — not general-purpose Claude Code skills (like spec-kit) or multi-agent orchestration framework (like aidevops). Best fit if you want AI agents running on schedule in GitHub Actions with explicit security gates.

## 8. Storm Bear pilot relevance / Mức độ phù hợp với Storm Bear

**Direct pilot: LOW.** Domain mismatch (CICD-workflow vs Markdown-knowledge-vault) + security-binding deployment friction.

**Observational value: HIGH cho:**
- **AGENTS.md template** (vault refactor reference; v27 diagnostic HIGH item #1)
- **skills/ directory architecture** (khi scale vault > 15 skills)
- **Compile-time-validation philosophy** (cho vault validation discipline)
- **Research-incubation-to-mainline-graduation pathway** (nếu vault publish externally)
- **4-repo decomposition** (reference architecture nếu vault scale > 100 wikis)

**Pilot ranking unchanged at v48: Not in top-11.**

## 9. 4-week evaluation roadmap (NẾU bạn quyết định pilot)

### Tuần 1: Setup + observation
- Cài đặt `gh extension install github/gh-aw` trong sandbox repo
- Chạy `gh aw init` + observe các file tạo ra
- Đọc AGENTS.md (49.8 KB; ~1 hour) để hiểu agent governance philosophy
- Đọc Security Architecture Spec summary (~30 min)
- Run sample workflow (e.g., `gh aw add githubnext/agentics` rồi pick simplest)

### Tuần 2: Build first custom workflow
- Tạo workflow read-only test (e.g., weekly-digest)
- Test với `engine: copilot` và `engine: claude` để so sánh
- Configure GitHub MCP toolsets cẩn thận
- Validate output qua `gh aw audit`

### Tuần 3: Production hardening
- Configure AWF firewall cho network isolation
- Configure MCP Gateway nếu cần multi-MCP routing
- Setup human approval gates cho write operations
- Review compliance với W3C-style spec Level 2 (Standard Conformance)

### Tuần 4: Decision + roadmap
- Đánh giá: phù hợp với current Scrum coach workflow? Hoặc thuần observational?
- Document lessons learned trong vault
- Decide: continue / pause / escalate to v27 HIGH bundle

## 10. Tradeoffs + limitations

| Aspect | Tradeoff |
|--------|----------|
| Power | Strong: agents chạy autonomously với security gates |
| Friction | Cao: GitHub Actions + LLM API key + repo-write trust required |
| Learning curve | Cao: 7-layer security architecture + 5-engine selection + 24 skills |
| Lock-in | GitHub Actions specific (không port sang GitLab CI / Jenkins / etc.) |
| Cost | LLM API budget + GitHub Actions minutes |
| Audit trail | Mạnh: SG-06 đảm bảo all actions produce auditable artifacts |
| Reversibility | Tốt: read-only by default; explicit opt-in cho write operations |

## 11. ⚠️ Caveats + safety notes

**Supply-chain awareness:**
- gh-aw consumes MCP servers via gateway — **trust boundaries** với each MCP server
- Companion AWF (Agent Workflow Firewall) provides domain-based egress control
- SBOM auto-generated per release (SPDX + CycloneDX) — review for compliance
- Pin Action versions explicitly (`@v1.2.3` not `@latest`)

**Production deployment checklist:**
- [ ] Read SECURITY.md + Security Architecture Specification full version
- [ ] Configure AWF firewall with explicit domain allowlist
- [ ] Start with `permissions: contents: read` + grant write permissions piecewise
- [ ] Use `safe-outputs` for ALL write operations
- [ ] Enable human approval gates for production environments
- [ ] Test in fork/sandbox repo before deploying to production
- [ ] Set LLM API budget alerts (engine config)
- [ ] Monitor audit trails via `gh aw audit` regularly
- [ ] Review skill-optimizer config nếu enable autonomous self-improvement

**Storm Bear specific concerns:**
- gh-aw không phù hợp cho Markdown-knowledge-vault use case (vault không có CICD workflow nature)
- Observational value cao cho AGENTS.md template, không phải direct pilot
- Nếu Storm Bear vault ever publishes externally, gh-aw research-incubation-to-mainline-graduation pathway là reference

## 12. References + next action

### Key links
- **Repo:** https://github.com/github/gh-aw
- **Docs:** https://github.github.com/gh-aw/
- **LLM-consumable:** https://github.github.com/gh-aw/llms.txt
- **Quick Start:** https://github.github.com/gh-aw/setup/quick-start/
- **Architecture:** https://github.github.com/gh-aw/introduction/architecture/
- **Peli's Agent Factory:** https://github.github.com/gh-aw/blog/2026-01-12-welcome-to-pelis-agent-factory/
- **Companion repos:** github/gh-aw-firewall + github/gh-aw-mcpg + github/gh-aw-actions
- **Workflow catalog:** github/gh-aw-actions + githubnext/agentics

### Storm Bear cross-references
- Sister github/* corpus T1: spec-kit v17 (`03 Projects/spec-kit - Beginner Analysis/`)
- Recent EXTREME-tier comparison: aidevops v47 (`03 Projects/aidevops - Beginner Analysis/`)
- T4 sibling bridges: graphify v16 / markitdown v28 / claude-context v40
- Pattern #18 ancestor: awesome-mcp-servers v31

### Next action recommendation

**For Storm Bear operator (Scrum Coach + software developer + vault maintainer):**

1. **DON'T pilot gh-aw directly** — domain mismatch + security-binding deployment.
2. **DO read gh-aw's 49.8 KB AGENTS.md** as reference for vault CLAUDE.md refactor (~1-2h investment) — third corpus template alongside spec-kit v17 + aidevops v47 22c.
3. **Consider executing v27 diagnostic HIGH bundle** with the 3 AGENTS.md templates available (gh-aw + spec-kit + aidevops). Bundle has been deferred 28 sessions — BLOCKING-RECOMMENDATION threshold exceeded 5.6×.
4. **Optionally explore W3C-style spec discipline** as model for vault validation discipline (compile-time validation philosophy applied to wiki structure validation).

**Estimated time investment:**
- Read gh-aw AGENTS.md + understand template: ~1-2h
- Apply vault CLAUDE.md refactor (v27 HIGH item #1): ~6-8h
- Total: ~7-10h investment for highest-leverage outcome

---

**Status:** v48 wiki shipped 2026-04-25. 12-CONSECUTIVE-WIKI ZERO-NEW-CANDIDATES STREAK extended (v37-v48). Pattern Library ratio preserved at 0.513:1 (12th consecutive cycle).
