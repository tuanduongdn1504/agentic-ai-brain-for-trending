# (C) README + VN summary — codymaster

> **Sources:** `README.md` + `README-vi.md` + `package.json` + `.claude-plugin/plugin.json` — WebFetch 2026-04-19
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Positioning + tagline

codymaster is positioned as a **"Vibe Coding Framework"** — the GitHub description reads:

> *"Vibe Coding Framework - Full SaaS Development Team from A-Z with Brain, Self Improvement, Auto Development"*

Primary tagline: **"Code Đi"** (Vietnamese: "Go code!") — informal, imperative, youth-adjacent. Signals:
- Informal rapid-ship culture (contrast: GSD's "context engineering" formalism)
- Vietnamese-cultural anchor right in the tagline
- Low-ceremony framing — "just start, figure out as you go"

Alternate EN phrasing from package.json: *"60+ Skills. Ship 10x faster. AI-powered coding skill kit for Claude, Cursor, Gemini & more."*

## 2. Author — Tody Le (VN)

Author attribution (from README + package.json):

- **Name:** Tody Le — Vietnamese surname
- **Role:** Head of Product
- **Experience:** 10+ years
- **Self-description:** Cannot code; spent 6 months building real products with AI, distilled lessons into the kit
- **Email:** aitodyle@gmail.com (package.json)
- **GitHub:** tody-agent (User, not Org — solo)
- **Website:** cody.todyle.com
- **Homepage (plugin):** cody-master-a5q.pages.dev (Cloudflare Pages)

### Storm Bear peer-category observation

Tody Le's profile overlaps significantly with Storm Bear operator:
- Vietnamese
- Product-side (vs pure-dev)
- Works with AI agents as primary surface
- Non-coder by self-description (Storm Bear = dev + Scrum coach, closer to "can code but doesn't live in code")

→ codymaster is a **peer-category artifact**, not a foreign-origin framework like ECC/Superpowers/gstack/GSD/BMAD. Relevance to Storm Bear = unique.

## 3. License — ISC (outlier)

**License:** ISC ("Free to use, modify, and distribute" per README)

ISC = permissive, functionally similar to MIT but different lineage (Internet Systems Consortium). First ISC in Storm Bear T1 corpus — all 5 prior T1 (ECC/SP/gstack/GSD/BMAD) use MIT.

→ Why ISC? Open question Q4. Possibly author preference, possibly npm ecosystem convention (Node historically ISC-heavy).

## 4. Scale — the marketing-vs-reality gap

### Claim vs actual

| Artifact | Claim | Actual | Source |
|----------|-------|--------|--------|
| Skill count | **"60+ Skills"** | **79** | skills/ folder listing |
| Skill count (alt) | **"68+ AI agent skills"** | 79 | plugin.json description |
| Command count | **"20+ Commands"** | **11** | commands/ folder listing |
| Version | **v6.0.0** | **5.1.0** | package.json |
| Version (alt) | 5.0.0 | 5.1.0 | plugin.json |

### Interpretation

- **Skill undersell (79 actual vs 60+/68+ claimed)** — surprising direction. Most projects oversell. codymaster undershoots. Could be: (1) deliberate "reserve the claim" conservatism, (2) stale README, (3) some `skills/` folders are WIP/internal, not "product skills"
- **Command oversell (11 actual vs 20+ claimed)** — typical direction. README possibly conflates command-files with CLI-verbs (`cm status`, `cm dashboard`, `cm brain`, `cm chain`, `cm deploy`, `cm agent`, `cm sprint`, etc) which could total ~20 even if the `commands/` folder has 11 workflow files. Requires verification.
- **Version skew (5.0 / 5.1 / v6.0.0)** — different publish channels. Website ahead of npm. Likely rolling `@next` vs `@latest` pattern similar to BMAD.

**Honest wiki posture:** report all three numbers + note the gap. Don't pick one and call it authoritative.

## 5. 8+ platform distribution (broadest T1)

Install paths from README:

| Platform | Install |
|----------|---------|
| Claude Desktop | Settings → Plugins → Add marketplace → `tody-agent/codymaster` → Sync |
| Claude Code CLI | `claude plugin marketplace add tody-agent/codymaster` |
| Cursor | `/add-plugin cody-master` |
| Gemini CLI | `gemini extensions install https://github.com/tody-agent/codymaster` |
| OpenCode / OpenClaw | `.opencode/INSTALL.md` |
| npm global | `npm install -g codymaster` |
| npm per-project | `npm install codymaster` |

Plus folders in repo root suggest more: `.codex/`, `.agent/`, `.cursor-plugin/`, `.claude-plugin/`, plus Antigravity (GitHub topic).

→ **8+ platforms is accurate and exceeds every T1 peer.** BMAD v6.3 added Junie = 4 platforms total. codymaster = 2× that breadth.

**Implication:** codymaster is **agnostic to harness** — framework is genuinely multi-AI-runtime, not Claude-Code-primary with others as afterthought.

## 6. Novel primitives (1-line each, detail in Phase 3 entity pages)

From README §"The Unified Brain":

1. **5-Tier Unified Memory** — Sensory / Working (cm-continuity) / Long-term (learnings.json + Ebbinghaus decay) / Semantic (cm-deep-search + vector via qmd) / Structural (cm-codeintell AST-based CodeGraph, ~95% token compression)
2. **Smart Spine v4.6+** — SQLite+FTS5 keyword search, progressive context loading (L0/L1/L2), skill execution caching, `cm://` URI context requests, 200k token budget pre-allocated by category, context bus for real-time skill output sharing, **MCP server exposing 18 tools**
3. **CodeGraph** — AST-based structural memory, ~95% token compression for full-codebase context
4. **Self-Healing Cycle** — `cm-skill-health` audits + `cm-skill-evolution` repairs (FIX/DERIVED/CAPTURED modes) + `cm-learning-promoter` auto-graduates recurring tasks to permanent skills + advisory reports drive deliberate repair
5. **Cloud Brain** — `cm-notebooklm` syncs high-value patterns to Google NotebookLM for cross-machine "soul" + auto-generates podcasts/flashcards
6. **`cm://` URI scheme** — skills request context by semantic URI, resolved by Smart Spine
7. **Context Bus** — real-time output sharing between chained skills within a single execution
8. **SkillsBench** — empirical research: 2-3 focused skills yield **+18.6 percentage points** over 4+ statically loaded skills, via `selectTopSkills()` dynamic selection

**This is the deepest novel-primitive density in T1 corpus.** BMAD (Party Mode + Scale-Adaptive) and GSD (context rot spec) both have 1-2 novel primitives each. codymaster has 8+.

## 7. Skill domain taxonomy (8 domains, 60+/79 skills)

README groups skills into 8 domains:

- **Engineering** — cm-tdd, cm-debugging, cm-code-review, cm-clean-code, cm-quality-gate
- **Operations** — cm-safe-deploy, cm-secret-shield, cm-security-gate, cm-identity-guard, cm-git-worktrees, cm-safe-i18n
- **Product/UX** — cm-planning, cm-design-system, cm-ux-master, cm-ui-preview, cm-brainstorm-idea, cm-dockit
- **Growth** — cm-content-factory, cm-ads-tracker, cm-cro-methodology, cm-growth-hacking, cm-booking-calendar
- **Enterprise** — cm-reactor, cm-notebooklm (only 2 — enterprise scope limited)
- **Self-Healing** — cm-skill-health, cm-skill-evolution, cm-skill-search, cm-skill-share
- **Orchestration** — cm-execution, cm-continuity, cm-deep-search, cm-codeintell

**Unusual scope for a "coding" framework:** Growth domain (cm-ads-tracker, cm-cro-methodology, cm-growth-hacking) crosses into marketing. This matches Tody Le's "full SaaS team A-Z" framing.

## 8. SaaS team role mapping

codymaster emulates:
- Senior Developer (cm-tdd, cm-debugging, cm-code-review)
- UX Lead (cm-design-system, cm-ux-master, cm-ui-preview)
- Product Manager (cm-planning, cm-brainstorm-idea, cm-jtbd)
- DevOps Engineer (cm-safe-deploy, cm-security-gate, cm-identity-guard)
- Technical Writer (cm-dockit, cm-content-factory, cm-auto-publisher)
- Growth Marketer (cm-ads-tracker, cm-cro-methodology, cm-growth-hacking)
- Enterprise Dev (cm-booking-calendar, cm-google-form)

→ 7 roles covered. Storm Bear Scrum-coach role = not explicit but cm-retro-cli + cm-sprint-bus adjacent.

## 9. Full Lifecycle + 4-Layer Protection

**Full Lifecycle (Idea → Production):**
Idea → Plan → Design → Test First → Code → Debug → Quality Gate → Security Scan → Deploy → Monitor → Document → Learn & Improve (feedback loop)

**4-Layer Protection (Before Deploy):**
- Layer 1: TDD + Code Review
- Layer 2: Secret scanning + Vulnerability scanning + Account validation
- Layer 3: Isolated git worktrees
- Layer 4: Quality gates + Multi-gate safe deploy pipeline

→ Lifecycle breadth exceeds all T1 peers. Most T1 stop at "Code + Debug + Test" (ECC/SP/gstack). GSD adds context. BMAD adds planning. codymaster claims Idea→Monitor→Learn.

**Claim verification:** Deliver-stage (Monitor/Learn) skills exist (cm-post-deploy-canary, cm-skill-evolution, cm-learning-promoter) but empirical effectiveness TBD.

## 10. Vietnamese README (README-vi.md) — honest assessment

### Quality verdict: Machine-translated despite VN author

**Counterintuitive finding:** Author is Vietnamese (Tody Le), yet VN README is **machine-translated from EN**, not VN-native authored.

**Evidence of translation direction (EN → VN):**
- Tool names never localized: `cm-tdd`, `cm-debugging`, `NotebookLM`, `Pencil.dev` kept in EN
- Subtitle mirrors EN structure: *"AI Agent của bạn thông minh. CodyMaster làm nó trở nên thông thái"* (direct translation-pairing of *"Your smart AI Agent. CodyMaster makes it wise"*)
- Awkward literal phrasings: *"AI sửa một lỗi, âm thầm làm hỏng 5 thứ khác"* (native speaker would restructure)
- Resume phrasing: *"Tody Le, Head of Product · 10+ năm kinh nghiệm"* — suggests original EN context

### Structure parity
Perfect — headings, mermaid diagrams, tables, section order align exactly with EN. Systematic translation.

### VN-specific content
**None detected.** Examples universally abstract (login flows, SaaS, landing pages). No Zalo, Vinahost, VNG ecosystem. No VN engineering community callouts.

### Technical terminology hybrid
- **Kept EN:** cm-tdd, MCP Server, Kanban Dashboard
- **Localized:** "Bộ Não Hợp Nhất" (Unified Brain), "Vòng đời" (Lifecycle)
- **Mixed:** Some UI/UX terms kept, some localized — inconsistent

## 11. VN-authored vs VN-translated — the axis codymaster introduces

v11 BMAD introduced VN translation (machine-quality) on EN-origin framework.
v12 codymaster = VN-author on EN-primary-written framework with VN machine-translation.

Two distinct localization modes now visible:

| Mode | Example | Primary language | Author origin | Quality |
|------|---------|-----------------|---------------|---------|
| **VN-translated** | BMAD | EN | US (LLC) | Machine-quality |
| **VN-authored, EN-primary** | codymaster | EN | VN (Tody Le) | EN-native-quality EN; machine-quality VN |
| **VN-authored, VN-primary** | (not in corpus yet) | VN | VN | N/A |

→ codymaster is middle-mode. Author IS VN but reached for global market via EN. VN README is afterthought.

**Storm Bear implication:** Author background aligns with Storm Bear, but deliverable is EN-first. VN speaker still gets machine-quality docs, just like BMAD. **VN language access = same as BMAD; VN author proximity = unique to codymaster.**

## 12. Cross-references to T1 siblings

| Claim | ECC | SP | gstack | GSD | BMAD | codymaster |
|-------|-----|----|---------|-----|------|-----------|
| Stars | ~5K | ~5K | ~5K | ~8K | 45K | **38 (smallest)** |
| License | MIT | MIT | MIT | MIT | MIT | **ISC (outlier)** |
| Author origin | US | US | US/YC | US | US-LLC | **VN (Tody Le)** |
| Author codes? | Yes | Yes | Yes | Yes | Yes | **No (self-declared)** |
| Skills/agents | Many | ~10 | ~15 | 33 | 12+ | **79 (largest)** |
| Platforms | 1 | 1 | 1 | 14 | 4 | **8+** |
| VN language | ❌ | ❌ | ❌ | ❌ | ✅ translated | **✅ translated (VN-author)** |
| Novel primitives | — | 7-stage | — | Context rot | Party Mode + Scale-Adaptive | **5-Tier + Smart Spine + CodeGraph + Self-Healing + Cloud Brain + SkillsBench (6+)** |

→ codymaster = **smallest community + largest skill surface + deepest novel primitives + only VN-authored**. Niche but unique.

## Open questions surfaced

- Skill count discrepancy root cause? (Q2)
- Command count conflation with CLI verbs? (Q3)
- "Can't code" literal or informal? (Q5)
- SkillsBench methodology? (Q7)
- Ebbinghaus decay actual algorithm? (Q8)
- Cloud Brain NotebookLM privacy? (Q9)
- Antigravity = Google's Project Antigravity? (Q24)
