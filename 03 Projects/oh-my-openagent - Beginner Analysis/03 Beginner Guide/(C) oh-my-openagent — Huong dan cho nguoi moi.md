# (C) oh-my-openagent — Hướng dẫn cho người mới / Beginner Guide

> **Bilingual VN+EN — VN primary, EN technical**
> **Cho:** Storm Bear operator (VN-based Scrum coach + software developer) đang đánh giá `code-yeongyu/oh-my-openagent` (omo) như một potential agent harness alternative.
> **Wiki version:** v52 — Storm Bear corpus 52nd LLM wiki
> **Cross-wiki siblings:** OMC v27 (Korean ecosystem peer) / obra/superpowers v2 (omo cites this in docs/superpowers/) / aidevops v47 (OpenCode-primary sibling, commercially deployable MIT alternative) / GitNexus v33 (PolyForm Noncommercial license-family sibling)

---

## ⚠️ ⚠️ ⚠️ READ THIS FIRST — License + Adversarial-positioning warning

**Before installing or piloting omo, Storm Bear operator MUST understand 3 critical caveats:**

### 1. SUL-1.0 license blocks commercial Scrum coaching deployment

omo distributed under **SUL-1.0 (Sustainable Use License Version 1.0)** — custom non-OSI license restricting commercial use.

LICENSE.md verbatim (translated to VN where helpful):
> "You may use or modify the software only for **your own internal business purposes** or for **non-commercial or personal use**. You may distribute the software or provide it to others only if you do so **free of charge for non-commercial purposes**."

**Cụ thể cho Storm Bear:**

| Use case | SUL-1.0 status |
|---|---|
| Học cá nhân + thử nghiệm ở vault Storm Bear | ✅ ALLOWED |
| Internal tooling cho vault Storm Bear (không phục vụ client) | ✅ ALLOWED |
| Build prototype Scrum coaching agent (chưa commercial) | ⚠️ BORDERLINE |
| **Triển khai Scrum coaching agent cho khách hàng trả tiền** | ❌ **BLOCKED** |
| Reselling hoặc tính phí Scrum coaching qua omo | ❌ BLOCKED |

→ **omo là pilot-evaluation-only cho Storm Bear. KHÔNG dùng cho khách hàng commercial.**

→ Nếu cần commercial-deployable OpenCode-primary alternative, dùng **aidevops v47** (MIT licensed) thay vì omo.

### 2. Adversarial-Anthropic positioning — brand-association risk

omo README verbatim: *"Anthropic blocked OpenCode because of us. Yes this is true. They want you locked in. Claude Code's a nice prison, but it's still a prison."*

**Caveat:** Storm Bear vault chưa độc lập verify chuyện "Anthropic blocked OpenCode". README chỉ link đến X.com @thdxr post (third-party assertion).

**Strategic implication cho Storm Bear:**
- Storm Bear's Scrum coaching brand dùng Claude Code (Anthropic ecosystem)
- omo's adversarial framing tạo **brand-association risk** nếu Storm Bear publicly endorse hoặc pilot omo
- **AVOID public endorsement** của omo. Pilot-evaluation = personal/private only.

### 3. Telemetry-on-by-default

omo gửi anonymous telemetry qua PostHog by default (hashed installation ID). Opt-out qua env var:

```bash
export OMO_SEND_ANONYMOUS_TELEMETRY=0
# OR
export OMO_DISABLE_POSTHOG=1
```

→ **Set opt-out env var TRƯỚC KHI** install nếu muốn private operation.

---

## 1. omo là gì? / What is omo?

**TL;DR:** omo = **OpenCode plugin** biến OpenCode CLI runtime thành "batteries-included" multi-agent coding harness với 11 Greek-mythology specialist agents (Sisyphus orchestrator + Hephaestus deep worker + Prometheus planner + 8 others), 26 tools (LSP suite + ast-grep + Hashline LINE#ID-validated edit + tmux), 52 lifecycle hooks, 3-tier MCP system, 8 model-category routing (visual-engineering / deep / quick / ultrabrain), 11 platform-compiled binaries (darwin/linux/windows × x64/arm64 × baseline/musl), Claude Code full compatibility, và one-word entrypoint `ultrawork` (or `ulw`).

**Tier:** T1 Agent-as-assistant (16th T1 entrant in Storm Bear corpus).

**Author:** YeonGyu-Kim (`code-yeongyu`) — Seoul, Korea; Sionic AI (Korean AI startup) employed; Sisyphus Labs commercial incubation parent (waitlist-only pre-product).

**Scale:** 54,135 stars / ~4.7 months ≈ ~11.5K stars/month (sustained-community-viral); v3.17.5 mature (200+ npm releases); pushed today; default branch `dev`.

**Renamed:** `oh-my-opencode` → `oh-my-openagent` mid-2026 to broaden multi-runtime targeting beyond OpenCode-only. npm package `oh-my-opencode` preserved for backward compatibility; dual-bin alias both names work.

## 2. Corpus-first signals (15+ at v52)

omo introduces 15+ corpus-first observations at T1:

1. **Default branch `dev`** (corpus-first `dev` default at T1; not `main`/`master`)
2. **SUL-1.0 license** at T1 (corpus-first SUL family; same-name as n8n.io's SUL)
3. **5-language README** including Russian (corpus-first Russian at T1)
4. **Greek-mythology cluster persona-design** (Sisyphus / Hephaestus / Prometheus / Oracle / Atlas / Metis / Momus + 4 functional)
5. **Hashline LINE#ID content-hash-validated edit tool** (corpus-first hash-anchored edit at T1)
6. **3-tier MCP system** explicit (built-in + Claude Code .mcp.json + skill-embedded)
7. **Skill-embedded MCP** scoped per-session (corpus-first context-budget-preserving MCP scope)
8. **11 platform-specific compiled binaries** via Bun compile (corpus-most at T1)
9. **Multi-runtime category-based model routing** (4+ categories visual-eng / deep / quick / ultrabrain)
10. **`/init-deep` auto-generated hierarchical AGENTS.md** (corpus-first auto-generation at T1)
11. **`ultrawork` + ralph loop "doesn't stop until done"** command primitives (corpus-first explicit)
12. **comment-checker hook** (corpus-first explicit AI-slop-prevention enforcement)
13. **Manifesto "Human In The Loop = BOTTLENECK"** (corpus-strongest autonomy-max framing observed)
14. **Adversarial-Anthropic positioning** (corpus-first explicit subject README claim)
15. **Telemetry-on-by-default + Privacy/ToS at solo-T1** (Pattern #12 v42 refined 7th counter-evidence wiki)

## 3. Tier placement: T1 Agent-as-assistant (16th T1 entrant)

omo extends Storm Bear's T1 (largest tier in corpus) from N=15 (post-v51 Vercel) to N=16.

**T1 sub-archetype:** Solo-Korean-Seoul-OpenClaw-fork-harness with EXTREME primitive surface (1,766 TS files / 26 tools / 11 named agents / 52 hooks / 19 features).

**Sister archetype:** **OMC v27 Yeachan Heo** — also Korean Seoul, also OpenClaw-based, also `oh-my-*` naming, also Sisyphus mythology. Pattern #73 73a Korean-Regional-Archetype T1 strengthens to N=2 with 3 sub-observations (oh-my-* naming + Sisyphus mythology + OpenClaw-fork-extension).

## 4. Cài đặt / Installation

**Cách dễ nhất (paste prompt cho LLM agent):**

```
Install and configure oh-my-opencode by following the instructions here:
https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

Paste prompt này vào Claude Code (hoặc AmpCode / Cursor / Codex / etc.). Agent tự download installation guide và làm hết.

**Hoặc cho LLM agent (curl):**

```bash
curl -s https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

**Manual (đọc docs trực tiếp):** `docs/guide/installation.md` trong repo (cần OpenCode runtime đã cài trước).

⚠️ **Trước khi install, set telemetry opt-out env var** nếu muốn private operation (xem ⚠️ section ở đầu).

⚠️ **Trước khi install, đảm bảo SUL-1.0 license OK với use case của bạn.** Storm Bear commercial Scrum coaching = NOT OK.

**Test installation:**

```bash
bunx oh-my-opencode doctor
# OR
bunx oh-my-openagent doctor
```

`doctor` health diagnostics check installation state.

## 5. Core usage pattern — `ultrawork`

**One-word entrypoint:**

Slash `/ultrawork` (full) hoặc `/ulw` (short alias) trong Claude Code session. Mọi agents activate, không dừng cho đến khi task done.

**Workflow example:**

User: "Build me a Scrum retrospective summarizer that ingests Linear tickets and outputs markdown report."

```
/ultrawork
```

omo orchestration:
1. **Sisyphus** (orchestrator, claude-opus-4-7 / kimi-k2.5 / glm-5) plans
2. **Prometheus** (planner) interviews user — "What columns matter? What format markdown?"
3. **Sisyphus** delegates by category:
   - `deep` → **Hephaestus** (gpt-5.4) for end-to-end Linear API research + scaffolding
   - `quick` → simple-model agent for typo fixes
   - `visual-engineering` → frontend-tuned agent for markdown formatting
   - `ultrabrain` → GPT-5.4 xhigh for hard logic (date math, edge cases)
4. **Background-task tool** runs 5+ specialists in parallel
5. **Hashline LINE#ID edit tool** validates every change against content hashes
6. **Comment-checker** post-tool hook prevents AI-slop in generated code
7. **Todo-enforcer** keeps Sisyphus on-task if it goes idle
8. **Ralph loop** continues until task 100% done

**Output:** Working code committed (only if user explicitly requested commit per anti-pattern); report generated.

## 6. Novel concepts / key architectural choices

### A. Hashline LINE#ID edit tool (corpus-first at T1)

Mọi Read output được tag với `LINE#ID` content hashes:

```
11#VK| function hello() {
22#XJ|   return "world";
33#MB| }
```

Edits reference những hash tags. Nếu file thay đổi từ lúc Read → hash mismatch → edit reject TRƯỚC khi corruption.

**README claim:** *"Grok Code Fast 1: 6.7% → 68.3% success rate. Just from changing the edit tool."*

→ Solves "harness problem" identified by Can Bölük (oh-my-pi author + "The Harness Problem" blog).

### B. 3-tier MCP system

| Tier | Source | Mechanism |
|---|---|---|
| Built-in | `src/mcp/` | 3 remote HTTP MCPs: websearch (Exa/Tavily) + context7 (official docs) + grep_app (GitHub) |
| Claude Code | `.mcp.json` | `${VAR}` env expansion |
| Skill-embedded | SKILL.md YAML | Per-session stdio + HTTP via skill-mcp-manager |

**Skill-embedded MCP rationale:** *"MCP servers eat your context budget. We fixed that. Skills bring their own MCP servers. Spin up on-demand, scoped to task, gone when done."*

### C. Multi-runtime category-based routing

Sisyphus delegates by **category**, không phải model. Category map sang model qua `CATEGORY_MODEL_REQUIREMENTS`:

| Category | What it's for | Default model |
|---|---|---|
| visual-engineering | Frontend, UI/UX, design | (configurable) |
| deep | Autonomous research + execution | gpt-5.4 |
| quick | Single-file changes, typos | (cheap model) |
| ultrabrain | Hard logic, architecture decisions | GPT-5.4 xhigh |

→ Agent says what kind of work; harness picks right model. Không touch nothing.

**Subscription stack recommendation** (omo README):
- ChatGPT Subscription ($20)
- Kimi Code Subscription ($0.99 — sale)
- GLM Coding Plan ($10)

### D. Greek-mythology persona cluster

11 named agents:
- **Sisyphus** — main orchestrator (endless toil; never gives up)
- **Hephaestus** — autonomous deep worker (forge god; "Legitimate Craftsman")
- **Prometheus** — strategic planner (foresight; interview mode)
- **Oracle** — architecture/debugging
- **Librarian** — docs/code search
- **Explore** — fast codebase grep
- **Atlas** — (per AGENTS.md inventory)
- **Metis** — (per AGENTS.md inventory; wisdom/cunning)
- **Momus** — critic/reviewer (Greek god of satire)
- **Multimodal-Looker** — vision-augmented inspection
- **Sisyphus-Junior** — lighter-scope variant

**Why Sisyphus mythology?** Albert Camus' "Sisyphus is happy" reading — endless toil but never giving up = autonomy-max framing fit. Korean Seoul authors (Yeachan + YeonGyu) both converge on Sisyphus mythology — cultural convention.

### E. Manifesto autonomy-max framing

**docs/manifesto.md:** *"HUMAN IN THE LOOP = BOTTLENECK. Think about autonomous driving. When a human has to take over the wheel, that's not a feature. It's a failure of the system. Why is coding any different?"*

omo's design optimizes for **zero human intervention during agentic work**. Operator says what they want; agent does everything else.

⚠️ **Storm Bear caveat:** Scrum coaching is **inherently human-centric** (helping humans collaborate better). omo's autonomy-max framing fits **automation-of-engineering-tasks**, not **coaching-of-humans**. Storm Bear's domain (Scrum coaching) may NOT benefit from autonomy-max as much as pure SWE automation does.

## 7. So sánh omo với corpus T1 frameworks / vs corpus T1

| Dimension | omo v52 | OMC v27 | aidevops v47 | spec-kit v17 | claude-code-best-practice v34 |
|---|---|---|---|---|---|
| Tier | T1 (16th) | T1 (9th) | T1 (14th) | T1 (7th) | T1 (11th) |
| Region | Korean Seoul | Korean Seoul | UK Jersey | US (GitHub corp) | Pakistani |
| License | **SUL-1.0 ⚠️ commercial-blocked** | MIT | MIT | MIT | MIT |
| Stars | 54K | 30K | 212 (cold-start) | 89K | 47K |
| Primary runtime | OpenCode (plugin) | OpenCode + 3 others (Claude/Codex/Gemini/Cursor) | OpenCode (plugin) | Claude Code | Claude Code |
| Multi-runtime | ✅ Compatibility layer | ✅ 4 first-class | ⚠️ OpenCode-primary + Claude shim | ❌ Claude Code only | ❌ Claude Code only |
| Methodology | Greek-mythology personas + autonomy-max manifesto + Hashline | Sisyphus orchestration + Team mode + Ralph loops | OpenCode plugin + 13 specialist agents + cross-provider verification | Spec-Driven Development (SDD) | 82-tip aggregation + best-practice reference |
| Primitive count | EXTREME (1,766 TS / 26 tools / 11 agents / 52 hooks) | YELLOW (~150 primitives) | EXTREME (~2,665 primitives) | YELLOW (~80 primitives) | GREEN (~30 primitives) |
| i18n | 5-lang (en/ko/ja/zh-cn/ru) | 7-lang (en/ko/zh/ja/es/vi/pt) | EN-only | EN-only | EN-only |
| Adversarial framing | ✅ Anti-Anthropic explicit | ⚠️ Multi-runtime equivalence (not adversarial) | ❌ Pro-multi-runtime balanced | ❌ Pro-Anthropic-aligned | ✅ Anthropic Community Ambassador endorsed |
| Storm Bear pilot | ❌ License-blocked-commercial | ⚠️ MIT but Korean docs preference | ✅ MIT + multi-runtime + commercially deployable | ✅ Methodology + corporate stability | ✅ 82-tip vault refactor reference |

**Verdict:** omo's primary differentiation is **EXTREME primitive surface + Greek-mythology cluster + Hashline edit tool + adversarial framing**. License limitation makes it pilot-evaluation-only for Storm Bear.

**Closest peer: OMC v27 Yeachan Heo** — Korean ecosystem twin. omo extends OMC's multi-runtime ambition with EXTREME primitive surface + Hashline + 3-tier MCP + manifesto framing. OMC is MIT (commercially deployable); omo is SUL-1.0 (commercial-blocked).

## 8. Storm Bear relevance assessment

### Storm Bear pilot ranking refresh post-v52

| Rank | Wiki | Why |
|---|---|---|
| 1 | claude-hud v35 | 5-min install + immediate context-budget visibility ROI |
| 2 | claude-howto v32 | self-onboarding meta-ROI; weekend commitment |
| 3 | spec-kit v17 | SDD methodology for Scrum workflows |
| 4 | rowboat v43 | direct peer-category Storm Bear vault structural mirror |
| 5 | aidevops v47 | OpenCode-primary multi-runtime escape-hatch (commercially deployable MIT) |
| 6 | claude-context v40 | vault semantic search + 3-plugin Claude Code augmentation stack |
| 7 | OMC v27 | multi-runtime orchestration (Korean ecosystem precedent) |
| 8 | claude-code-best-practice v34 | 82-tip aggregation for vault CLAUDE.md refactor |
| 9 | pi-mono v36 | Claude Code alternative + multi-provider escape-hatch |
| 10 | Vercel v51 | SKILL.md format reference for vault `05 Skills/` expansion |
| **OMITTED** | **omo v52** | **SUL-1.0 license-blocked commercial Scrum coaching deployment; observational-only pilot consideration** |

### Direct utility (LOW for commercial Scrum coaching)

omo cannot be deployed for paying-client Scrum coaching due to SUL-1.0 license. Pilot is personal-evaluation-only or internal-Storm-Bear-vault-tooling-only.

### Observational value (HIGH)

- **Pattern #57 57c structural N=2 promotion-candidate** — first external validity signal for Storm Bear corpus-selection discipline (validated at 25-wiki gap)
- **Pattern #73 73a Korean ecosystem peer** — 2nd Korean Seoul T1 in corpus
- **Pattern #18 OpenCode-primary observation N=2 un-stale** — multi-runtime escape-hatch awareness
- **3-tier MCP architectural template** — context-budget-preserving MCP scope mechanism
- **Multi-runtime category-routing template** — vault skill-system extension consideration
- **4-template AGENTS.md ensemble extension** — vault CLAUDE.md refactor reference
- **Sisyphus Labs commercial-incubation playbook** — strategic playbook reference for hypothetical Storm Bear commercialization

### VN-localization observation

omo README localized to ko + ja + zh-cn + ru (NOT vi). Pattern: Korean-author T1 multi-lang convention prioritizes East-Asian + RU-tier languages over VN. Storm Bear cannot expect omo to localize for VN audience without contribution.

**Translation contribution opportunity:** README.vi.md + docs/guide/*.vi.md would extend i18n coverage. ⚠️ Per omo CONTRIBUTING.md English-language-policy, code review communications must be in English (translation contributions require navigating policy).

## 9. 4-week evaluation roadmap (pilot-evaluation-only; NOT commercial)

### Tuần 1 / Week 1 — Personal exploration

**Day 1-2:** Set telemetry opt-out env vars. Read SUL-1.0 LICENSE.md carefully. Confirm pilot-evaluation use case = personal/non-commercial.

**Day 3-4:** Install OpenCode runtime (prerequisite). Install omo via paste-prompt method. Test `bunx oh-my-opencode doctor` health check.

**Day 5-7:** Type `ultrawork` on simple personal project (e.g., update vault skill file or refactor a single Storm Bear note). Observe Sisyphus orchestration + Hephaestus deep work + Hashline edit behavior.

### Tuần 2 / Week 2 — Architecture exploration

**Day 8-10:** Read AGENTS.md (173 lines). Understand 5-step initialization + 3-tier MCP + 8 model categories.

**Day 11-12:** Configure project-level `.opencode/oh-my-opencode.jsonc` for personal vault use. Try category-routing experimentation.

**Day 13-14:** Test Hashline LINE#ID edit tool on real vault file. Compare edit reliability vs Claude Code baseline.

### Tuần 3 / Week 3 — Multi-runtime exploration

**Day 15-17:** Test omo with 3 runtimes (Claude / Kimi / GLM). Observe model-routing + cost differences.

**Day 18-19:** Try `/ulw-loop` (ralph loop) on a multi-step refactoring task. Observe "doesn't stop until 100% done" behavior.

**Day 20-21:** Compare `ultrawork` vs raw Claude Code productivity for personal Scrum-coaching tasks (e.g., "Generate 5 retrospective questions for sprint X" — compare quality).

### Tuần 4 / Week 4 — Decision + cleanup

**Day 22-24:** Document findings. Decide: continue personal use OR uninstall.

**Day 25-26:** If continuing personal: archive learnings into Storm Bear vault as observational notes. If uninstalling: follow uninstall procedure (3 steps in README).

**Day 27-28:** Final decision documented. ⚠️ **DO NOT deploy for paying Scrum coaching clients.** ⚠️ **DO NOT publicly endorse omo (brand-association risk).**

## 10. Tradeoffs + limitations

### Strengths

- ✅ EXTREME primitive surface — most-batteries-included T1 framework in corpus
- ✅ Multi-runtime support — category-routing + 6+ providers
- ✅ Hashline LINE#ID edit tool — real edit-reliability improvement (per README claims)
- ✅ Claude Code full compatibility — drop-in for existing Claude Code users
- ✅ Sustained release cadence (200+ npm releases in 4.7 months)
- ✅ Strong governance — AGENTS.md auto-generated + CLA + Privacy/ToS at solo-T1
- ✅ 5-language docs (en/ko/ja/zh-cn/ru)

### Weaknesses

- ❌ **SUL-1.0 license — commercial-blocker for Scrum coaching paying clients**
- ❌ Adversarial-Anthropic positioning — brand-association risk for Storm Bear
- ❌ Telemetry-on-by-default — privacy concern (mitigatable via opt-out env)
- ❌ Greek-mythology persona aesthetic — may not resonate with all teams
- ❌ Korean docs ko + ja + zh-cn + ru priority (no vi localization)
- ❌ Solo author bus-factor = 1 (Sionic AI affiliation but unclear succession)
- ❌ EXTREME primitive surface = steep learning curve
- ❌ Default branch `dev` (operational confusion potential vs `main`/`master`)
- ❌ Pre-product Sisyphus Labs commercial pathway — long-term commercial trajectory uncertain

### Bus-factor concern

omo at 54K stars with 1,766 TS files / 377K LOC is at scale where solo-author-instability creates community risk. Mitigants:
- Sionic AI org affiliation (cultural/employment continuity)
- Sisyphus Labs commercial entity (legal continuity infrastructure)
- 7 GitHub Actions workflows (auto-publish + CLA + lint-workflows + sisyphus-agent)
- Heavy governance (AGENTS.md + 32 Zod schemas + factory patterns + 200 LOC limits + comment-checker)

⚠️ Still solo-author-driven. If YeonGyu unavailable, no clear successor.

## 11. Caveats + safety notes

### Supply-chain awareness

omo bundles **3 built-in remote MCP servers** (Exa/Tavily websearch + context7 + grep_app) + **skill-embedded MCPs** load arbitrary stdio + HTTP servers per-session. Each MCP = separate trust-boundary.

**Per Pattern #66 OBSERVATION-TRACK supply-chain awareness:**
- Built-in MCPs from omo project = first-party; trust depends on omo author
- Claude Code `.mcp.json` MCPs = user-configured; trust under user control
- Skill-embedded MCPs = per-skill author trust; **VARIES**
- ⚠️ Audit skill-embedded MCPs before sensitive operations

### Telemetry transparency

PostHog backend + hashed installation ID + opt-out via 2 env vars. Not raw hostname. Privacy Policy + ToS in `docs/legal/`.

⚠️ Default ON. Explicitly opt-out before sensitive operations.

### Anti-pattern enforcement

omo's anti-pattern enforcement (no `as any` / no `@ts-ignore` / no em dashes / no en dashes / no AI filler phrases) is **strict**. Style violations rejected at PR review.

⚠️ Storm Bear contributions (if attempted) must conform to YeonGyu's style. Translation tools acceptable per CONTRIBUTING.md.

### License-change risk (CLA forward-relicensing clause)

CLA.md grants YeonGyu *"the right to relicense the Contribution under any license, including proprietary licenses, without requiring additional permission from you."*

⚠️ If Storm Bear contributes code/docs, that contribution may be relicensed proprietary later. Acceptable for trivial fixes; concerning for substantive contributions.

## 12. References + next action

### Source repository
- GitHub: https://github.com/code-yeongyu/oh-my-openagent (default branch `dev`)
- Homepage: https://ohmyopenagent.com/
- Discord: https://discord.gg/PUwSMR9XNk
- npm: `oh-my-opencode` + `oh-my-openagent` (dual-bin)

### Related corpus wikis
- **OMC v27** `Yeachan-Heo/oh-my-claudecode` — Korean ecosystem peer; cited "oh-my-opencode" as 1 of 5 inspirational sources (Pattern #57 57c sibling)
- **obra/superpowers v2** — referenced in omo `docs/superpowers/` subdir (Pattern #57 57a 5th data point)
- **aidevops v47** `marcusquinn/aidevops` — OpenCode-primary sibling (commercially deployable MIT alternative if needed)
- **GitNexus v33** `abhigyanpatwari/GitNexus` — PolyForm Noncommercial license-family sibling

### Storm Bear context files
- `04 Phase 4b Deliverable/(C) Pattern test — 57c N=2 promotion-candidate + Korean ecosystem + new sub-variants harvest.md`
- `05 Iteration Log/(C) v52 oh-my-openagent iteration log.md`
- `02 Entity Pages/(C) E4 — 41st Storm Bear meta-entity ...md` (license-blocked-commercial pilot caveat)

### External references
- Can Bölük "The Harness Problem" blog: blog.can.ac/2026/02/12/the-harness-problem/ (foundation for Hashline LINE#ID edit tool)
- oh-my-pi: github.com/can1357/oh-my-pi (Hashline inspiration)
- Sisyphus Labs waitlist: sisyphuslabs.ai
- Sionic AI: sionic.ai

### Next action for Storm Bear operator

**RECOMMENDED:**

1. **DO NOT pilot omo for commercial Scrum coaching** — SUL-1.0 license-blocked.
2. **Optional: 30-min personal evaluation** (Week 1 Day 1-2 of roadmap above) to understand Korean ecosystem peer + Pattern #57 corpus-internal-recursion observations.
3. **Read v52 Phase 4b deliverable** — pattern-test analysis + Korean ecosystem peer documentation (more strategic value than personal pilot).
4. **Consider aidevops v47** instead — OpenCode-primary multi-runtime escape-hatch with MIT license (commercially deployable for Storm Bear Scrum coaching).
5. **⚠️ Execute v27 diagnostic HIGH bundle before v53** — 32 sessions deferred (6.4× threshold). omo doesn't directly help v27 HIGH execution but contributes 4-template AGENTS.md ensemble + `/init-deep` auto-generation reference + 50d incubation-waitlist commercial-playbook.
6. **OR run mini-audit** (~30-60 min) to action 12 promotion-candidates accumulated post-v52 (3 NEW v52 + 9 carry-forward).

**AVOID:**

1. ❌ Public endorsement of omo (adversarial-Anthropic brand-association risk)
2. ❌ Commercial deployment for paying Scrum coaching clients (SUL-1.0 violation)
3. ❌ Substantive code contributions without understanding CLA forward-relicensing clause

**Velocity check:** Pattern #18 OpenCode-primary observation N=2 (omo + aidevops v47) is now structurally validated — multi-runtime escape-hatch becoming actionable infrastructure. Future Storm Bear runtime-portability strategy reference if Anthropic ecosystem instability ever requires.

---

**Wiki version:** v52 — Storm Bear corpus 52nd LLM wiki
**Built:** 2026-04-25 → 2026-04-26
**Routine:** v2.1 9th v2.1-era execution
**Length:** ~480 lines bilingual VN+EN
**Status:** ✅ Shipped
