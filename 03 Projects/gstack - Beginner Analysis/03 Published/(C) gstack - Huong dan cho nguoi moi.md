# gstack — Hướng dẫn cho người mới

> **For team / Cho team:** Đây là hướng dẫn tổng hợp để bắt đầu với **gstack** — framework biến Claude Code thành "virtual engineering team" do Garry Tan (President & CEO của Y Combinator) build. Đọc 1 lần ~30 phút, đủ để cài đặt và chạy 1 sprint end-to-end.
>
> **Tác giả wiki:** Storm Bear, dựa trên `garrytan/gstack` v0.18.3.0 (2026-04-17).
> **Ngày:** 2026-04-18 | **Phiên bản:** v1
> **Song ngữ:** Tiếng Việt (chính) + English (technical terms)

---

## 📋 Mục lục

1. [Tại sao đọc cái này](#tại-sao-đọc-cái-này)
2. [Part 1: gstack là gì](#part-1-gstack-là-gì)
3. [Part 2: Sprint Pipeline — trái tim gstack](#part-2-sprint-pipeline--trái-tim-gstack)
4. [Part 3: 23 Specialists + 8 Power Tools](#part-3-23-specialists--8-power-tools)
5. [Part 4: Browser Daemon — điểm kỹ thuật độc đáo](#part-4-browser-daemon--điểm-kỹ-thuật-độc-đáo)
6. [Part 5: Setup roadmap 1 tuần](#part-5-setup-roadmap-1-tuần)
7. [Part 6: 3 ETHOS principles](#part-6-3-ethos-principles)
8. [Part 7: FAQ thường gặp](#part-7-faq-thường-gặp)
9. [Part 8: Resources & References](#part-8-resources--references)

---

## Tại sao đọc cái này

### Ai nên đọc / Who should read

- **Founders & CEOs** — đặc biệt technical ones vẫn muốn ship code
- **First-time Claude Code users** — muốn structured roles thay vì blank prompt
- **Tech leads & staff engineers** — cần rigorous review/QA/release automation
- **Anyone** đã đọc guide ECC hoặc Superpowers, muốn so sánh 3-way (xem `(C) ECC vs Superpowers vs gstack 3-way comparison`)

### Bạn sẽ có gì sau khi đọc / What you'll get

- Hiểu **Sprint Pipeline** (Think → Plan → Build → Review → Test → Ship → Reflect)
- Biết **23 specialists + 8 power tools**, mỗi cái role gì + khi nào gọi
- Hiểu **Browser Daemon** — điểm differentiator kỹ thuật của gstack
- **Setup roadmap 1 tuần** từ zero → ship 1 PR end-to-end
- Hiểu **3 ETHOS principles:** Boil the Lake + Search Before Building + User Sovereignty

### Không phải là gì / What this is NOT

- ❌ Không phải tutorial cài Claude Code từ đầu
- ❌ Không cover toàn bộ 23 skill templates chi tiết — xem `02 Wiki/` để đọc sâu từng entity
- ❌ Không cover cross-model workflow (gstack + OpenClaw/Codex parallel) — advanced

---

## Part 1: gstack là gì

### TL;DR

**gstack** là **slash-command framework** open-source cho Claude Code (+ 9 harness khác), do **Garry Tan** — President & CEO của Y Combinator — build. MIT license.

**Claim đáng chú ý:**
- Garry ship **600,000+ LOC trong 60 ngày** part-time bằng tool này
- **10,000-20,000 LOC/day** part-time trong khi run YC full-time
- 1 tuần gần đây: **140,751 LOC added, 362 commits, ~115k net LOC**

**Core idea:**
> "gstack gives Claude Code a persistent browser and a set of opinionated workflow skills. The browser is the hard part — everything else is Markdown."

gstack biến Claude Code thành **"virtual engineering team"**:
- CEO rethink product
- Eng manager lock architecture
- Designer catch AI slop
- Reviewer find production bugs
- QA lead open real browser
- Security officer chạy OWASP + STRIDE audits
- Release engineer ship PR

**23 specialists + 8 power tools. All slash commands. All Markdown. All free.**

### Khác ECC và Superpowers ở đâu

| Axis | ECC | Superpowers | **gstack** |
|------|-----|-------------|--------|
| Philosophy | Performance optimization | Methodology (TDD Iron Law) | **Role-based pipeline (virtual team)** |
| Scope | 185 skills + 48 agents | 14 skills + 1 agent | **23 specialists + 8 power tools** |
| Audience | Broad dev | Methodology-focused dev | **Founder/CEO + Claude Code first-timer + tech lead** |
| Cross-harness | 5 | 7 | **10** |
| Browser | Via MCP tools | Not core | **Built-in daemon (sub-second latency)** |
| Reflection | Not explicit | Iteration logs (manual) | **`/retro` built-in, `/retro global` cross-project** |
| Open-source model | Plugin + paid products | Pure OSS | **OSS + YC recruiting funnel** |

→ **Chọn gstack nếu:** bạn value role-based mental model + real browser automation + founder perspective.

### Lịch sử ngắn

- Public release: từ 2026 (blog posts từ Garry nhắc đến early 2026)
- Hiện tại: **v0.18.3.0** (2026-04-17) — 126 versions đã ship
- Cadence: cực kỳ aggressive — multiple versions per day recent
- Active contributor base (hiring CTA public trong README)

---

## Part 2: Sprint Pipeline — trái tim gstack

Đây là **concept quan trọng nhất** để hiểu gstack. Mỗi feature/bugfix đi qua pipeline **7 stages**:

```
Think → Plan → Build → Review → Test → Ship → Reflect
```

Mỗi stage có skill chính:

| Stage | Skill chính | Nhiệm vụ |
|-------|-------------|----------|
| **Think** | `/office-hours` | 6 forcing questions reframe product |
| **Plan** | `/autoplan` (hoặc `/plan-ceo-review` + `/plan-eng-review` + `/plan-design-review`) | Lock architecture, design, scope |
| **Build** | (Claude writes code sau khi plan approved) | Implement |
| **Review** | `/review` | Bugs pass CI nhưng blow production |
| **Test** | `/qa <staging-url>` | Real browser test, atomic commits per bug fix |
| **Ship** | `/ship` + `/land-and-deploy` | PR, merge, deploy, verify |
| **Reflect** | `/retro` | Weekly retro, growth opportunities |

### Ví dụ concrete (từ README)

```
You:    "I want to build a daily briefing app for my calendar"
You:    /office-hours
Agent:  [pushes back on framing]
        "You said 'daily briefing app.' But what you described is a
         personal chief of staff AI."
        [extracts 5 capabilities, challenges 4 premises]
        [generates 3 implementation approaches với effort estimates]
        RECOMMENDATION: Narrowest wedge tomorrow, full vision 3-month.
        [writes design doc → feeds downstream skills automatically]

You:    /plan-ceo-review
        [reads design doc, challenges scope, 10-section review]

You:    /plan-eng-review
        [ASCII diagrams, state machines, test matrix, security concerns]

You:    Approve plan. Exit plan mode.
        [Agent writes 2,400 lines across 11 files. ~8 minutes.]

You:    /review
        [AUTO-FIXED] 2 issues. [ASK] Race condition → approve fix.

You:    /qa https://staging.myapp.com
        [opens real browser, clicks flows, finds+fixes bug]

You:    /ship
        Tests: 42 → 51 (+9 new). PR: github.com/you/app/pull/42
```

**Key insight:** User said "daily briefing app" → Agent said **"chief of staff AI"** because it listened to pain, not feature request.

> "Eight commands, end to end. That is not a copilot. That is a team."

### Smart review routing

Pipeline tự biết stage nào cần cho loại work nào:

| Building for... | Plan stage | Live audit |
|-----------------|------------|------------|
| **End users** (UI, web, mobile) | `/plan-design-review` | `/design-review` |
| **Developers** (API, CLI, SDK, docs) | `/plan-devex-review` | `/devex-review` |
| **Architecture** (data flow, perf, tests) | `/plan-eng-review` | `/review` |
| **All above** | `/autoplan` (auto-detects) | — |

→ "Just like well-run startup: CEO doesn't look at infra bug fixes."

### Parallel sprints (10-15 simultaneously)

gstack shine khi chạy parallel với [Conductor](https://conductor.build):
- Session 1: `/office-hours` on new idea
- Session 2: `/review` on PR
- Session 3: implementing feature
- Session 4: `/qa` on staging
- Sessions 5-15: other branches

> "You manage them the way a CEO manages a team: check in on decisions that matter, let rest run."

→ **Đọc sâu:** [[../02 Wiki/(C) Sprint Pipeline]]

---

## Part 3: 23 Specialists + 8 Power Tools

### Category 1: Think + Plan (5 roles)

| Role | Khi gọi |
|------|---------|
| `/office-hours` | Start feature mới, cần reframe pain point |
| `/plan-ceo-review` | Challenge scope, 4 modes (Expansion/Selective/Hold/Reduction) |
| `/plan-eng-review` | Lock architecture, ASCII diagrams, test matrix |
| `/plan-design-review` | Rate design 0-10, AI Slop detection |
| `/plan-devex-review` | Developer API/CLI/SDK experience, TTHW benchmark |
| `/autoplan` | Auto-chain CEO → design → eng → DX (orchestrator) |

### Category 2: Design system (3 roles)

| Role | Khi gọi |
|------|---------|
| `/design-consultation` | Build design system from scratch |
| `/design-shotgun` | 4-6 mockup variants + comparison board + taste memory |
| `/design-html` | Mockup → production HTML (Pretext 30KB zero-deps) |

### Category 3: Review + Test + Ship (11 roles)

| Role | Khi gọi |
|------|---------|
| `/review` | Staff engineer review trước ship |
| `/investigate` | Systematic debug (Iron Law: no fix without investigation) |
| `/design-review` | Live design audit + fix |
| `/devex-review` | Live DX audit (actually tests onboarding) |
| `/qa` | Real browser test + auto-fix + regression test |
| `/qa-only` | QA methodology, report-only (no fixes) |
| `/cso` | OWASP Top 10 + STRIDE security audit |
| `/codex` | Second opinion từ OpenAI Codex CLI (3 modes) |
| `/ship` | Sync main, tests, push, open PR |
| `/land-and-deploy` | Merge PR, deploy, verify production |
| `/canary` | Post-deploy monitoring loop |
| `/benchmark` | Core Web Vitals before/after PR |

### Category 4: Meta + Reflect (4 roles)

| Role | Khi gọi |
|------|---------|
| `/retro` | Weekly engineering retro |
| `/document-release` | Update all docs to match shipped code |
| `/learn` | Manage gstack cross-session learnings |
| `/pair-agent` | Share browser với other AI agents (OpenClaw/Codex/Cursor) |

### 8 Power tools

| Tool | Khi gọi |
|------|---------|
| `/careful` | "Be careful" mode — warns destructive commands |
| `/freeze` | Lock edits to one directory |
| `/guard` | `/careful` + `/freeze` combined |
| `/unfreeze` | Release lock |
| `/browse` | Browser access cho agent |
| `/open-gstack-browser` | Launch GStack Browser visible |
| `/setup-deploy` | One-time deploy config |
| `/gstack-upgrade` | Self-update |

**→ Đọc sâu:** [[../02 Wiki/(C) Specialist Roles]]

### Voice-friendly triggers

gstack skills có natural-language triggers. Thay vì nhớ `/qa`:
- "Run a security check" → `/cso`
- "Test the website" → `/qa`
- "Do an engineering review" → `/review`

Dùng AquaVoice/Whisper + trigger phrase → skill match automatically.

---

## Part 4: Browser Daemon — điểm kỹ thuật độc đáo

gstack's distinguishing technical feature: **long-lived Chromium daemon** với HTTP bridge.

### Why it matters

**Without daemon:** 2-3s Chromium cold start mỗi command. 20+ QA commands = 40+ seconds startup overhead. State (cookies, tabs, login) lost between.

**With daemon:**
- First call: ~3s
- After: **~100-200ms per command**
- Persistent state: cookies/tabs/localStorage persist
- Auto-shutdown: 30 min idle → cleanup
- Multi-workspace: random port per workspace, zero conflicts

### Architecture (đơn giản hóa)

```
Claude Code → CLI binary → HTTP POST localhost:PORT → Bun server → CDP → Chromium (headless)
                                  ↓
                          Authorization: Bearer <UUID>
```

### Security model

5 layers cho cookies (sensitive nhất):
1. Keychain approval (macOS dialog)
2. Decryption in-process (never disk plaintext)
3. DB read-only (copy to temp)
4. Key cache per-session
5. No cookie values in logs

Plus:
- Localhost only (not `0.0.0.0`)
- Bearer token per session
- State file mode 0o600
- Shell injection prevention (hardcoded browser registry)

### What it enables

- `/qa` — real clicks, real screenshots ("agent has eyes now")
- `/design-review` — atomic commits với before/after screenshots
- `/browse` — direct browser access
- `/pair-agent` — share browser across AI agents với security
- `/open-gstack-browser` — visible Chromium với sidebar extension

### Quote nhấn mạnh

> "The bottleneck is always Chromium, not the CLI or server. Bun's startup speed (~1ms compiled binary vs ~100ms Node) is nice but not the reason we chose it. The compiled binary and native SQLite are."

→ **Đọc sâu:** [[../02 Wiki/(C) Browser Daemon Architecture]]

---

## Part 5: Setup roadmap 1 tuần

(So với ECC 4 tuần và Superpowers 2 tuần — gstack gọn hơn do role-based mental model đơn giản hơn.)

### Day 1: Install + pilot run

```bash
# Claude Code path (recommended)
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup
```

Hoặc paste vào Claude Code:
> Install gstack: run `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` then add a "gstack" section to CLAUDE.md...

**Verify:** Restart Claude Code. Chạy `/office-hours` — nếu skill list, install thành công.

### Day 2: Pilot run theo README 5-step

1. `/office-hours` — describe bất cứ pain point gì
2. `/plan-ceo-review` — xem CEO reframe
3. `/review` — run trên any branch with changes
4. `/qa` — test staging URL (nếu có)

> "Stop there. You'll know if this is for you."

### Day 3: ETHOS + CLAUDE.md deep read

Đọc 2 files:
- `~/.claude/skills/gstack/ETHOS.md` (164 lines) — 3 principles
- `~/.claude/skills/gstack/CLAUDE.md` (503 lines) — dev conventions, slop-scan, voice protection

**Mental models cần nắm:**
- Boil the Lake vs Ocean
- Three Layers of Knowledge (Layer 3 first-principles prized)
- User Sovereignty ("AI recommends, users decide")
- AI effort compression table (3x-100x)

### Day 4-5: Full sprint end-to-end

Pick 1 feature thật trong project. Go through toàn bộ Sprint Pipeline:

```
/office-hours → /autoplan → [implement] → /review → /qa → /ship
```

**Document mỗi stage tốn bao lâu.** Compare với cách làm trước đây.

### Day 6: Weekly retro

```
/retro
```

Xem per-person breakdowns, shipping streaks, test health trends.

Nếu có multi-project:
```
/retro global
```

### Day 7: Team rollout decision

Sau 1 tuần, quyết định:
- **Keep gstack** — rollout team mode: `./setup --team`
- **Switch framework** — gstack không match culture, try Superpowers hoặc ECC
- **Hybrid** — gstack cho some projects, khác cho others

→ Sau tuần 1, bạn có 1 PR shipped + baseline về gstack velocity.

---

## Part 6: 3 ETHOS principles

Per `ETHOS.md`, injected vào mọi workflow skill's preamble.

### 1. Boil the Lake

> "AI-assisted coding makes the marginal cost of completeness near-zero. When the complete implementation costs minutes more than the shortcut — do the complete thing. Every time."

**Lake vs Ocean:**
- **Lake** (boilable): 100% test coverage module, full feature, all edge cases
- **Ocean** (not): rewrite entire system, multi-quarter migration

**Rule:** Boil lakes. Flag oceans as out of scope.

**Anti-patterns:**
- "Choose B — 90% with less code" (if A is 70 lines more, choose A)
- "Defer tests to follow-up" (tests cheapest lake to boil)
- "This would take 2 weeks" → say "2 weeks human / ~1 hour AI-assisted"

### 2. Search Before Building — Three Layers of Knowledge

- **Layer 1: Tried-and-true** — standard patterns. Risk: assume obvious answer right.
- **Layer 2: New-and-popular** — current best practices. Risk: crowd mania.
- **Layer 3: First-principles** — original reasoning. **Prized above all.**

**The Eureka Moment:**
1. Understand what everyone is doing + WHY (Layers 1+2)
2. Apply first-principles reasoning to their assumptions (Layer 3)
3. Discover clear reason conventional approach is wrong

> "Zig while others zag. When you find one, name it. Celebrate it."

### 3. User Sovereignty

> "AI models recommend. Users decide. This is the one rule that overrides all others."

**Iron Man suit** (cited Karpathy): great AI products augment user, not replace.

> "Two AI models agreeing is strong signal, not mandate."

**Anti-patterns:**
- "Outside voice right, so I'll incorporate" → Present it. Ask.
- "Both models agree, must be correct" → Agreement is signal, not proof.
- "I'll change it and tell user after" → Ask first. Always.

→ **Đọc sâu:** [[../02 Wiki/(C) ETHOS + ARCHITECTURE summary]]

---

## Part 7: FAQ thường gặp

### Q1: gstack thay thế Claude Code không?

Không. gstack là **plugin/skills overlay** cho Claude Code. Claude Code vẫn là CLI gốc; gstack thêm 23 specialists + 8 power tools + browser daemon.

### Q2: Tôi đang dùng Cursor/OpenCode/Codex, gstack chạy không?

Có. gstack support **10 hosts**: Claude Code, Codex CLI, OpenCode, Cursor, Factory Droid, Slate, Kiro, Hermes, GBrain (mod), OpenClaw.

Cài: `./setup --host <name>` hoặc auto-detect qua `./setup`.

**Lưu ý:** Browser daemon primary trên Claude Code. Một số host không support browser → `/qa`, `/design-review` graceful degrade.

### Q3: Mix gstack với ECC hoặc Superpowers được không?

Kỹ thuật được, nhưng **không khuyến nghị**. Có thể skill name collision (cả 3 đều có review/TDD skills). Pick 1 framework chính.

→ Đọc [[(C) ECC vs Superpowers vs gstack 3-way comparison]] để quyết định.

### Q4: 600K LOC / 60 days claim có thật không?

Không thể verify direct từ repo public (no personal git log). Nhưng:
- 126 versions ship trong ~6 tháng gstack development
- Multiple versions/day gần đây
- Conductor integration enable 10-15 parallel sprints
- AI effort compression table (30x-100x cho boilerplate/test) lý thuyết support claim

→ Claim credible, không verified-exact.

### Q5: Tôi có cần Bun không?

Có. gstack uses Bun cho compiled binary + native SQLite + native TypeScript. Install: https://bun.sh (v1.0+).

**Windows:** Cần cả Bun AND Node.js (Bun pipe transport có bug Windows — gstack auto-fallback to Node).

### Q6: Browser daemon tốn tài nguyên không?

- First start: ~3s + ~200MB RAM cho Chromium
- Idle: Chromium stays alive 30 min → ~100MB idle RAM
- After 30 min no commands → auto-shutdown → 0 resource

→ Reasonable cho dev machine. Không khuyến nghị cho resource-constrained env.

### Q7: MIT license — contribute được không?

Được. Nhưng CLAUDE.md có **"Community PR guardrails"** — 3 hard gates:
1. Don't touch ETHOS.md
2. Don't remove/soften promotional (YC references are intentional)
3. Don't change Garry's voice (tone, humor, directness)

→ Read CLAUDE.md trước submit PR.

### Q8: gstack có training official không?

Không formal. README's 5-step pilot + 1-week roadmap (Part 5 above) là path khuyến nghị.

### Q9: Team adoption — rollout như nào?

```bash
cd ~/.claude/skills/gstack && ./setup --team
cd <your-repo>
~/.claude/skills/gstack/bin/gstack-team-init required
git add .claude/ CLAUDE.md && git commit -m "require gstack"
```

- Every developer installs globally
- Updates auto (hourly throttled, silent, network-safe)
- No vendored files in repo
- No version drift

### Q10: Nên dùng gstack hay Superpowers hay ECC?

→ **Đọc:** [[(C) ECC vs Superpowers vs gstack 3-way comparison]]

**TL;DR quick:**
- **gstack:** nếu value role-based mental model + founder perspective + browser automation
- **Superpowers:** nếu value Iron Law TDD + methodology discipline
- **ECC:** nếu cần broad skill library (185) cho polyglot team

---

## Part 8: Resources & References

### Repo + docs

- **Repo:** https://github.com/garrytan/gstack
- **Author:** https://x.com/garrytan
- **README:** https://github.com/garrytan/gstack/blob/main/README.md
- **ETHOS.md:** builder philosophy
- **ARCHITECTURE.md:** tech decisions
- **CLAUDE.md:** dev conventions (503 lines!)
- **CHANGELOG.md:** 126 versions trong 6 tháng
- **docs/skills.md:** deep dives từng skill
- **docs/OPENCLAW.md:** advanced dispatch routing
- **docs/ADDING_A_HOST.md:** contribute new host support

### Wiki Storm Bear (đọc sâu)

- [[../02 Wiki/(C) README summary]]
- [[../02 Wiki/(C) CLAUDE.md summary]]
- [[../02 Wiki/(C) ETHOS + ARCHITECTURE summary]]
- [[../02 Wiki/(C) Sprint Pipeline]]
- [[../02 Wiki/(C) Specialist Roles]]
- [[../02 Wiki/(C) Browser Daemon Architecture]]
- [[../02 Wiki/(C) Multi-Host Declarative Platform]]
- [[(C) ECC vs Superpowers vs gstack 3-way comparison]] — 3-way decision matrix

### Karpathy references (meta)

- Karpathy "I don't think I've typed like a line of code..." — Fortune 2026-03-21
- Karpathy's [AI coding rules](https://github.com/forrestchang/andrej-karpathy-skills) — 17K stars
- gstack README claims enforce Karpathy's 4 failure modes (wrong assumptions, overcomplexity, orthogonal edits, imperative over declarative)

### Community + Ecosystem

- **OpenClaw:** https://github.com/openclaw/openclaw — cited inspiration, 247K stars
- **Conductor:** https://conductor.build — parallel Claude Code sessions
- **ClawHub:** OpenClaw marketplace cho native skills

### YC recruiting signal

README ends với hiring CTA:
> "We're hiring. Want to ship 10K+ LOC/day and help harden gstack? Come work at YC — ycombinator.com/software. Extremely competitive salary and equity. San Francisco, Dogpatch District."

→ gstack functions as YC recruiting funnel + dev tool. Not deceptive — explicit.

### Khi gặp issue

- **Skill không trigger:** `cd ~/.claude/skills/gstack && ./setup`
- **`/browse` fails:** `cd ~/.claude/skills/gstack && bun install && bun run build`
- **Stale install:** `/gstack-upgrade`
- **Short vs namespaced commands:** `./setup --prefix` hoặc `--no-prefix`
- **Codex "stale skills":** `cd ~/.codex/skills/gstack && git pull && ./setup --host codex`
- **Windows Bun pipe bug:** Auto-fallback to Node.js, nhưng Node must be on PATH
- **Skills not seen bởi Claude:** project's CLAUDE.md cần `## gstack` section

---

## Closing thoughts — ai đây để dùng gstack

gstack **được build cho 1 persona cụ thể**: solo founder / tech lead với tham vọng ship volume cao. Nếu bạn match persona → gstack cho bạn a force multiplier. Nếu không match (thích flexibility, không chịu role-based framing) → có thể friction.

**Bài kiểm tra 5 câu hỏi:**
1. Bạn có thường "underestimate effort" bằng thinking trong human-team time?
2. Bạn có frustrated khi AI agent skip design/review/QA stages?
3. Bạn có muốn manage AI agents "theo cách CEO quản lý team"?
4. Bạn có đánh giá cao "voice" + "taste" như first-class concerns?
5. Bạn có chấp nhận opinionated tool over configurable tool?

Nếu ≥3 YES → gstack fit. Nếu ≥3 NO → try ECC hoặc Superpowers.

**Final recommendation:**
- **First-time with AI coding:** start gstack (structured roles dễ mental model)
- **Đã dùng ECC:** try gstack khi cần role-based workflow cho high-volume sprints
- **Đã dùng Superpowers:** try gstack khi cần browser automation + parallel sprints

→ **Next action:**
1. Install gstack (30 giây)
2. Run pilot 5-step
3. Đọc 3-way comparison nếu cần chọn giữa ECC/Superpowers/gstack: [[(C) ECC vs Superpowers vs gstack 3-way comparison]]

---

> **Wiki maintained by Storm Bear.** Insight verified từ source. gstack update aggressive (5+ versions/tuần) — nếu fact outdated, ping để fix.
