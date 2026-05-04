# (C) agent-skills-of-vercel — Hướng dẫn cho người mới / Beginner Guide

**Wiki cho:** [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) — Vercel's official collection of agent skills
**Storm Bear LLM Wiki #51** — first wiki post-corpus-half-century-milestone (v50)
**Built:** 2026-04-25
**Routine:** v2.1
**License:** MIT (claim — không có file LICENSE ở root; xem Phần 1 cảnh báo)

---

## ⚠️ Đọc cái này trước / Read this first

Trước khi cài hoặc dùng agent-skills của Vercel:

1. **License ambiguity:** README nói "MIT" nhưng repo **không có file LICENSE ở root**. Chỉ 4/7 SKILL.md có khai báo `license: MIT` trong YAML frontmatter. 3 skill còn lại không khai. Pattern #29 29-absent-3 sub-context (xem Phần 12). Cẩn thận khi commercial use — nên hỏi Vercel cho clarity nếu cần.

2. **Per-skill scope pre-evaluation:** 5/7 skills là **rule-aggregator** cho React/Next.js/React Native/Web design. 2/7 là **practical-script** cho Vercel deployment. Trước khi cài bulk, đánh giá xem skill nào thực sự liên quan đến công việc của bạn — đừng cài hết để tránh context noise.

3. **Vercel commercial-funnel transparency:** Skill `vercel-deploy-claimable` deploys ứng dụng lên Vercel preview (không cần auth) rồi return claim URL để transfer ownership sang Vercel account của bạn. Đây là **Pattern #50 commercial-funnel** rõ ràng — agent-deployed preview → Vercel account upsell. Không sai về mặt đạo đức (transparent, user opts in via claim URL), nhưng nên biết: dùng skill = bạn đang ở trong Vercel commercial funnel.

4. **Supply-chain awareness (Pattern #66):** `npx skills add vercel-labs/agent-skills` invokes third-party CLI tool `skills` từ skills.sh / agentskills.io ecosystem — KHÔNG phải Anthropic-vetted. Vercel = trustable; nhưng `npx skills add <random-repo>` cần cẩn thận. Per-skill ZIP download là auditable alternative (download zip + extract + read SKILL.md trước khi install).

---

## 1. Đây là gì? / What is it?

**VN:** Vercel agent-skills là một bộ sưu tập 7 SKILL.md files — instruction packages cho AI coding agents (Claude.ai, Claude Code, Cursor, Copilot) — được Vercel Engineering tự viết và publish public. Mỗi skill dạy agent một thứ cụ thể: cách deploy app lên Vercel, cách audit accessibility cho UI, cách viết React component composition không dùng boolean props, v.v.

Skill = markdown file với YAML frontmatter (chứa `name`, `description`, trigger phrases) + bash scripts (nếu cần) + supporting docs. Khi user nói câu trigger ("Deploy my app", "Review this React component"), agent tự động load skill liên quan và follow instructions trong đó.

**EN:** Vercel agent-skills is a collection of 7 SKILL.md files — instruction packages for AI coding agents (Claude.ai, Claude Code, Cursor, Copilot) — authored by Vercel Engineering and published publicly. Each skill teaches an agent something specific: how to deploy apps to Vercel, how to audit UI accessibility, how to write React component composition without boolean prop proliferation, etc.

A skill is a markdown file with YAML frontmatter (containing `name`, `description`, trigger phrases) + bash scripts (if needed) + supporting docs. When a user says a trigger phrase ("Deploy my app", "Review this React component"), the agent automatically loads the relevant skill and follows its instructions.

---

## 2. Corpus-first signals (so với 50 wiki trước)

| Signal | Lần đầu thấy trong corpus | Wiki anchor |
|---|---|---|
| AGENTS.md = CLAUDE.md byte-identical-mirror (Pattern #22 22d) | ✅ FIRST | Vercel v51 |
| Forward-citation-then-wiki (Pattern #57 57c — multica v15 cited Vercel agent-skills 36 wikis BEFORE v51) | ✅ FIRST | Vercel v51 |
| Pattern #17 variant 5 ecosystem-scale platform N=3 default-criterion (HuggingFace + Microsoft + Vercel) | ✅ N=3 milestone | Vercel v51 |
| Pattern #29 29-absent-3 N=2 strengthening (per-skill license metadata variation) | ✅ N=2 promotion-candidate | Vercel v51 |
| `npx skills add <repo>` install verb (third-party non-Anthropic registry) | ✅ FIRST | Vercel v51 |
| Per-skill semver YAML metadata (deploy-to-vercel at v3.0.0; others v1.0.0) | ✅ corpus-first explicit per-skill semver | Vercel v51 |
| `argument-hint: <file-or-pattern>` YAML field | ✅ FIRST | Vercel v51 (web-design-guidelines) |
| Per-rule prefix-namespace (`architecture-`, `state-`, `patterns-`, `react19-`) | ✅ FIRST | Vercel v51 (composition-patterns) |
| Build pipeline for rule-aggregator skill (`packages/react-best-practices-build/`) | ✅ FIRST | Vercel v51 |
| Claim-URL-as-funnel-terminus deployment workflow | ✅ Most-explicit observed | Vercel v51 |
| Corporate-collective lineage "Vercel Engineering" (Pattern #19 archetype 4) | strengthening | Vercel v51 (joins magika v44 + gh-aw v48) |

---

## 3. Tier placement / Vị trí trong taxonomy

**T1 Agent-as-assistant** — corporate-narrow-skill-library sub-archetype.

Distinct from prior T1 entrants:
- Methodology frameworks (BMAD v11, spec-kit v17, gstack)
- Best-practice aggregators (claude-code-best-practice v34)
- Tutorials (claude-howto v32)
- Display utilities (claude-hud v35)
- Multi-package monorepos (pi-mono v36)
- Multi-domain orchestration platforms (aidevops v47)
- Workflow automation (gh-aw v48)

**Corporate-narrow-skill-library** = official corporate publisher (Vercel) + narrow domain scope (React/Next.js/Vercel ecosystem) + 7 skills curated for ecosystem reinforcement.

NOT outside-scope: not aggregator (no curation of external skills); not training-infra; not foundation-model.
NOT Pattern #68 awesome-list-genre: no external curation, only Vercel-Engineering-authored.

---

## 4. Cài đặt / Installation

**4 surfaces available:**

### 4a. `npx skills add` (bulk install — corpus-first verb)

```bash
npx skills add vercel-labs/agent-skills
```

Installs all 7 skills via the `skills.sh` / `agentskills.io` registry CLI. **Third-party — không phải Anthropic-vetted.** Vercel-trusted, OK.

### 4b. Manual `cp -r` (selective install — Claude Code)

```bash
git clone https://github.com/vercel-labs/agent-skills.git
cd agent-skills
cp -r skills/deploy-to-vercel ~/.claude/skills/
cp -r skills/web-design-guidelines ~/.claude/skills/
# ... per-skill selective
```

Ưu điểm: chỉ cài skill bạn cần, đọc SKILL.md trước, no third-party CLI.

### 4c. Per-skill ZIP download (selective — claude.ai or Claude Code)

5/7 skills có ZIP file:
- `deploy-to-vercel.zip`
- `react-best-practices.zip`
- `react-view-transitions.zip`
- `vercel-cli-with-tokens.zip`
- `web-design-guidelines.zip`

Download zip, extract, copy vào `~/.claude/skills/`.

### 4d. Paste SKILL.md vào claude.ai

Copy nội dung SKILL.md → paste vào Claude.ai project knowledge hoặc trực tiếp vào conversation.

Dành cho users dùng claude.ai (browser) thay vì Claude Code CLI. Nếu skill cần network access (deploy-to-vercel, vercel-cli-with-tokens), phải whitelist domains tại `claude.ai/settings/capabilities`.

---

## 5. Core usage pattern / Cách dùng cốt lõi

**Skills auto-activate** trên trigger phrases. Không cần invoke manually.

### Examples (verbatim từ README)

```
Deploy my app
```
→ activates `deploy-to-vercel` skill (vercel-deploy-claimable workflow)

```
Review this React component for performance issues
```
→ activates `vercel-react-best-practices` skill

```
Help me optimize this Next.js page
```
→ activates `vercel-react-best-practices` (overlapping trigger)

```
Check accessibility
```
→ activates `web-design-guidelines` skill

```
Refactor this component — too many boolean props
```
→ activates `vercel-composition-patterns` skill

---

## 6. 7 skills cụ thể / 7 skills detail

### Rule-aggregator skills (5)

| Skill | Trigger | Use case |
|---|---|---|
| **vercel-react-best-practices** | "review React perf", "optimize Next.js" | 70 rules across 8 categories — waterfalls / bundle / SSR / data fetch / re-render / rendering / JS micro |
| **vercel-react-native-skills** | "build React Native app", "optimize mobile perf" | 16 rules across 7 sections — perf / layout / animation / images / state / arch / platform |
| **vercel-react-view-transitions** | "add page transitions", "animate route changes" | `<ViewTransition>` API + `addTransitionType` + Next.js `transitionTypes` |
| **vercel-composition-patterns** | "refactor boolean prop proliferation", "build flexible component library" | Compound components / state lifting / `architecture-` `state-` `patterns-` `react19-` rule prefixes |
| **web-design-guidelines** | "review my UI", "audit design", "check accessibility" | 100+ rules across 11 categories incl. accessibility / focus / forms / animation / typography / images / perf / nav / dark mode / touch / i18n |

### Practical-script skills (2)

| Skill | Trigger | Use case |
|---|---|---|
| **deploy-to-vercel** (vercel-deploy-claimable; v3.0.0) | "Deploy my app", "Push this live" | 4-step: gather state / choose method / execute / return preview-URL + claim-URL |
| **vercel-cli-with-tokens** | "deploy to vercel", "set up vercel" | Token-authenticated CLI workflow (vs interactive `vercel login`) |

---

## 7. So với corpus frameworks khác / vs other corpus frameworks

| Wiki | Tier | Scope | Skill count | Distribution | Compare with Vercel |
|---|---|---|---|---|---|
| awesome-claude-skills v50 | outside-scope | Hybrid awesome-list + commercial | 864 SKILL.md | Aggregation | **Different form-factor** — Vercel author-built; awesome-claude-skills curates external |
| aidevops v47 | T1 | Cross-domain multi-agent | ~2,665+ primitives | npm + Bun + Homebrew + curl + manual | **EXTREME vs GREEN** — Vercel narrow scope |
| gh-aw v48 | T1 | Workflow automation | ~50 workflows | npm + clone | **Different domain** — Vercel ecosystem extension; gh-aw GitHub Actions |
| pi-mono v36 | T1 | Coding agent CLI | 7 packages monorepo | npm scoped | **Multi-package vs skill collection** — Vercel narrower per-skill scope |
| claude-howto v32 | T1 | Tutorial pedagogical | 45+ templates | clone + reference | **Skills vs templates** — Vercel agent-skills are runtime-active; claude-howto templates are copy-paste |
| spec-kit v17 | T1 | SDD methodology | 9-article constitution | uv tool install | **Methodology vs skill** — Vercel applies existing methods; spec-kit defines methodology |
| HuggingFace agents-course v26 | T3 | Course curriculum | 4 units | hf.co/learn + clone | **Same Pattern #17 variant 5 archetype** — both ecosystem-scale platforms; different tier |
| Microsoft markitdown v28 | T4 | Doc-to-Markdown utility | 1 utility | pip + Docker | **Same Pattern #17 variant 5 archetype** — both ecosystem-scale platforms; different tier |

---

## 8. Ethical framing / Khía cạnh đạo đức

### Ethical assessment: LOW-MEDIUM concern

**Concerns:**

1. **License ambiguity (Pattern #29 29-absent-3):** README claims MIT, no LICENSE file at root, 4/7 SKILL.md declare `license: MIT` in YAML, 3/7 don't. **Strict legal reading:** README claim has goodwill but no legal force. Per-skill YAML metadata for 4 skills *may* apply per-skill but is non-standard. **Recommendation:** for commercial use, ask Vercel for written license clarification or assume default copyright.

2. **Vercel commercial-funnel via claim-URL (Pattern #50 50a):** vercel-deploy-claimable funnels users into Vercel commercial tier via claim-URL ownership transfer. **Transparent** — README explicitly says "claimable" — but be aware: using skill = participating in Vercel commercial funnel. Not sneaky; explicit.

3. **Supply-chain via `npx skills add` (Pattern #66 OBSERVATION-TRACK):** Third-party skills.sh CLI, not Anthropic-vetted. Vercel-published repo = trustable, but the CLI mechanism is generic and could be abused for `npx skills add <random-repo>`. Use per-skill zip download or manual `cp -r` for paranoid security.

4. **Trigger-phrase-based activation:** Skills auto-activate when user says trigger phrases. If you install many skills with overlapping triggers, agent may activate unexpectedly. Curate skill library carefully.

**Non-concerns:**

- ✅ Authorship transparent (Vercel Engineering corporate-collective)
- ✅ MIT-claim + per-skill YAML license metadata for major content skills
- ✅ Source code public + auditable
- ✅ No anti-distillation clauses
- ✅ No attribution-display requirements
- ✅ No litigation-termination clauses
- ✅ No obfuscation; well-documented

---

## 9. Storm Bear relevance / Ý nghĩa cho Storm Bear

### Direct utility (HIGH for SKILL.md format reference)

**SKILL.md format spec từ Vercel** là **most-direct corpus template cho vault `05 Skills/` directory expansion**. Currently vault có 8 skills, all prose markdown, no YAML frontmatter, no trigger-phrase activation, no on-demand loading.

Adopting Vercel-style YAML frontmatter sẽ:
- Enable trigger-phrase-based skill activation (vs current "manually invoke")
- Enable on-demand loading (vs current "always loaded")
- Enable per-skill versioning + license metadata (vs current implicit)

**Pilot proposal:** Convert 1 vault skill (đề xuất `llm-wiki-routine-v2.1.md`) sang Vercel-style SKILL.md format. Effort: 30-60 min. Compatibility: Claude Code natively reads YAML frontmatter.

### Indirect utility (MEDIUM)

- **AGENTS.md identical-mirror (22d)** = 4th template thêm vào reference ensemble cho vault CLAUDE.md refactor (v27 diagnostic HIGH item #1, deferred 30 sessions). Tuy nhiên 22d không phù hợp cho vault (không cần cả 2 file).
- **Claim-URL deployment workflow** = reference cho "agent-deployed asset → ownership transfer" — không trực tiếp áp dụng cho Scrum coach role.

### No direct utility

- React/Next.js/React Native rule-aggregator skills không phù hợp với markdown vault (không có UI code).
- Pattern #17 variant 5 archetype reference chỉ aspirational (vault chưa scale tới ecosystem-scale platform).

### Storm Bear pilot ranking refresh post-v51

| # | Pilot | Effort |
|---|---|---|
| 1 | rowboat v1 vault pilot | 4 weeks |
| 2 | claude-hud install | 5 min |
| 3 | spec-kit methodology | 1-2 weeks |
| 4 | claude-howto self-onboarding | 13h weekend |
| 5 | OMC multi-runtime | 1 weekend |
| 6 | pi-mono coding agent alt | 2-4h |
| 7 | aidevops AGENTS.md template | 6-8h |
| **8 NEW** | **Vercel SKILL.md format adoption** | **30-60 min single-skill / 3-4h full vault** |

---

## 10. 4-week skill evaluation roadmap / Lộ trình đánh giá 4 tuần

**Mục tiêu:** thử từng skill 1 tuần (5/7 skills phù hợp với hầu hết developer), đánh giá fit, quyết định long-term adoption.

### Week 1: Setup + deploy-to-vercel (skill phổ quát nhất)

- Day 1-2: `git clone vercel-labs/agent-skills` → đọc README + AGENTS.md
- Day 3-4: `cp -r skills/deploy-to-vercel ~/.claude/skills/` → test trên test project (`vercel deploy` workflow)
- Day 5-7: Đánh giá ergonomics — claim-URL ownership transfer có hữu ích cho workflow của bạn không?

### Week 2: web-design-guidelines (UI/UX audit cho non-React projects cũng dùng được)

- Day 1-3: Cài skill, run "Review my UI" trên dự án có UI. Đánh giá rule coverage.
- Day 4-7: Compare với existing tools (axe DevTools / Lighthouse / Pa11y) — Vercel skill có cover được không, hay chỉ một subset?

### Week 3: Một skill React-specific phù hợp với stack của bạn

- Nếu dùng Next.js → `vercel-react-best-practices`
- Nếu dùng React Native → `vercel-react-native-skills`
- Nếu dùng React 19 + View Transitions → `vercel-react-view-transitions`
- Nếu refactoring component architecture → `vercel-composition-patterns`

Test 1 skill trong workflow thực tế, đánh giá rule quality.

### Week 4: vercel-cli-with-tokens (only if dùng Vercel CI/CD)

- Skip nếu không dùng Vercel
- Otherwise: setup token-based CI deploy workflow

### Decision point post-Week 4

- Giữ lại skills nào bạn thực sự dùng
- Uninstall skills không phù hợp (chỉ delete folder từ `~/.claude/skills/`)
- Optional: contribute back nếu phát hiện rule bị thiếu (Vercel chấp nhận PRs)

---

## 11. Tradeoffs + limitations

### Strengths

- ✅ Production-grade SKILL.md quality (vercel-deploy-claimable v3.0.0; thoughtful state-detection logic)
- ✅ Format-spec compliance (500-line cap respected; on-demand loading; scripts-not-inline)
- ✅ Light governance enables fast iteration (4.5 months → 25.7K stars + 7 skills + v3 maturity)
- ✅ Corporate-amplified-organic distribution (no aggressive marketing; growth via Vercel ecosystem reach)
- ✅ Per-skill semver versioning
- ✅ Verbatim user-quote trigger phrases (intuitive activation)

### Limitations

- ❌ Light governance gaps (no SECURITY / CONTRIBUTING / CoC / LICENSE-file)
- ❌ Per-skill license metadata variation (3 of 7 lack `license:` declaration in YAML)
- ❌ Skill scope narrow to React/Next.js/Vercel ecosystem
- ❌ README label vs YAML name vs directory name divergence (3 conventions per skill — ergonomics friction)
- ❌ AGENTS.md aspirational requirements (composition-patterns + react-native-skills missing zips; rule-aggregator skills have rules/ not scripts/)
- ❌ Slight positioning drift between README + AGENTS.md scopes
- ❌ EN-only (no i18n)
- ❌ No tests / no CI for skill validation

### Risk to Storm Bear vault

**LOW** if scoped to SKILL.md format reference + 1-skill conversion pilot.
**MEDIUM** if attempting full vault `05 Skills/` refactor (8 skills × 30-60 min each = 4-8 hours).
**HIGH** if conflating with v27 diagnostic HIGH bundle vault CLAUDE.md refactor (different scope; 22d not applicable).

---

## 12. Caveats + safety notes

**Pattern #29 29-absent-3 caveat:** README MIT-claim + no LICENSE file + per-skill YAML license variation = **legal ambiguity for commercial use.** For internal Storm Bear vault use (non-commercial), MIT-claim sufficient. For commercial productization, ask Vercel.

**Pattern #50 50a transparency:** Vercel commercial-funnel via claim-URL is **transparent** — explicit in README. Not sneaky. Use is informed-consent.

**Pattern #66 supply-chain:** `npx skills add` invokes third-party `skills` CLI from skills.sh. Vercel-published repo trustable; the install mechanism generic. For maximum security: use `git clone` + `cp -r` instead of `npx skills add`.

**Pattern #18 MCP absence:** Skills don't use MCP. Pure SKILL.md + bash scripts + claude.ai/Code direct. Counter-evidence to Pattern #18 corporate-official-tier — not all corporate-official frameworks adopt MCP.

**Pattern #22 22d identical-mirror caveat:** AGENTS.md = CLAUDE.md byte-identical. **Drift risk** if either is edited without mirroring. Vercel-recommended: edit one, copy to the other (manual discipline). Storm Bear vault should NOT adopt 22d (no need for both files).

---

## 13. References + next action

### References
- Source repo: https://github.com/vercel-labs/agent-skills
- Format spec: https://agentskills.io/
- Registry: https://skills.sh/vercel-labs/agent-skills
- Vercel: https://vercel.com
- Pattern Library: `PATTERN_LIBRARY.md` (vault root) — patterns #17 variant 5 / #22 / #57 / #29 / #50 / #59 / #19 / #27 / #2 / #18

### Cross-wiki siblings
- **awesome-claude-skills v50** — corpus-half-century milestone aggregator (curation contrast)
- **aidevops v47** — Pattern #22 22c authoritative-with-shim
- **gh-aw v48** — Pattern #22 22a monolithic 49.8KB
- **multica v15** — forward-citation source (Pattern #57 57c)
- **HuggingFace v26 + Microsoft v28** — Pattern #17 variant 5 N=2 anchors

### Next action

**For Storm Bear vault operator:**

1. **IMMEDIATE (2 min):** Read this guide; decide whether to pilot Vercel-style SKILL.md format conversion
2. **OPTIONAL Week 1 (30-60 min):** Pilot — convert `llm-wiki-routine-v2.1.md` to Vercel-style YAML frontmatter as proof-of-concept
3. **OPTIONAL Month 1 (3-4h):** Full vault `05 Skills/` refactor if Week 1 pilot successful
4. **DEFERRED:** v27 diagnostic HIGH item #1 (vault CLAUDE.md refactor) — Vercel v51 adds 4th template (22d) but not recommended for vault; 22c (aidevops v47) more aligned

**For Storm Bear pilot evaluation:**

- If you want skill ergonomics improvement → Pilot SKILL.md format adoption (Storm Bear pilot #8 NEW)
- If you want React/Next.js code quality skills → Install relevant Vercel skills selectively
- If you want Vercel deployment workflow → Install `deploy-to-vercel` skill (deploy-to-vercel v3.0.0)

**Final recommendation:** Vercel agent-skills là HIGH-quality skill library cho React/Next.js/Vercel ecosystem; SKILL.md format reference value > direct skill adoption value cho Storm Bear use case. Pilot SKILL.md format conversion là highest-ROI immediate action.

---

End of beginner guide.
