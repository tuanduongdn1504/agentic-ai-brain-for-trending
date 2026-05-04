# (C) Beginner guide — gsd-2 / GSD-2

> **VN-EN bilingual guide** cho `gsd-build/gsd-2` ("The evolution of Get Shit Done — now a real coding agent"). Audience: Storm Bear operator (Scrum coach + dev) + team members evaluating gsd-2 as autonomous-coding-agent platform.

## ⚠️ Read this first / Đọc cái này trước

**EN:** Before diving in, 3 things you MUST know:

1. **$GSD Solana token exists** — gsd-2 README has Dexscreener badge linking to a Solana token. This is **NOT required** to use gsd-2 (MIT license, free software), but it's a brand association that may matter for VN clients in conservative industries (banking, government, large enterprise). Decision required: do you use gsd-2 for client-facing work given crypto-association?

2. **Managed RTK binary supply-chain** — gsd-2 auto-provisions a third-party binary called RTK (compresses shell-command output). gsd-2 forces telemetry-disabled by default — this is good practice. But: you're running a third-party binary not from the original gsd-build maintainer. You can opt out via `GSD_RTK_DISABLED=1` if uncomfortable.

3. **Authorship transparency** — gsd-build is the org. GSD-1 author = TÂCHES (per Storm Bear v5 wiki). GSD-2 LICENSE + ADRs = Lex Christopherson. Same person? Hand-off? Multi-maintainer org? **Unknown** without external verification. Documenting honestly because operator should know what's verified vs not.

**VN:** Trước khi bắt đầu, 3 điều BẮT BUỘC phải biết:

1. **$GSD Solana token tồn tại** — gsd-2 README có badge Dexscreener link tới Solana token. KHÔNG bắt buộc dùng gsd-2 (MIT license, free), nhưng đây là brand association có thể ảnh hưởng tới khách VN trong ngành bảo thủ (ngân hàng, gov, enterprise lớn). Cần quyết định: có dùng gsd-2 cho client-facing work khi có crypto-association không?

2. **Managed RTK binary supply-chain** — gsd-2 tự động provision third-party binary tên RTK (compress shell-command output). gsd-2 force telemetry-disabled by default — đây là practice tốt. Nhưng: đang chạy third-party binary không phải từ gsd-build maintainer gốc. Có thể opt out qua `GSD_RTK_DISABLED=1` nếu không thoải mái.

3. **Authorship transparency** — gsd-build là org. GSD-1 author = TÂCHES (theo Storm Bear v5 wiki). GSD-2 LICENSE + ADRs = Lex Christopherson. Cùng người? Hand-off? Multi-maintainer org? **Không rõ** chưa verify external. Documenting honestly vì operator nên biết cái gì đã verify vs chưa.

---

## 1. What is gsd-2 / gsd-2 là gì

**EN:** gsd-2 is a **standalone TypeScript CLI coding agent** built on the Pi SDK (Mario Zechner's pi-mono — Storm Bear v36 wiki subject). You give it a spec, run `/gsd auto`, walk away, and come back to working software with clean git history.

**Core idea**: Each task gets a fresh 200k-token context window. State lives in `.gsd/` directory on disk. Auto mode reads files, dispatches work to LLM, advances through milestones. Crash recovery, cost tracking, git worktree isolation, automatic verification — all built-in.

**vs GSD-1 (TÂCHES, 57.4K stars)**: GSD-1 was a prompt framework injecting instructions into Claude Code via slash commands. GSD-2 is a real TypeScript application that controls the agent session directly.

**VN:** gsd-2 là **standalone TypeScript CLI coding agent** xây trên Pi SDK (pi-mono của Mario Zechner — Storm Bear v36 wiki subject). Đưa spec, chạy `/gsd auto`, walk away, quay lại có working software với clean git history.

**Ý tưởng cốt lõi**: Mỗi task được fresh 200k-token context window. State sống trong thư mục `.gsd/` trên disk. Auto mode đọc files, dispatch work tới LLM, advance qua milestones. Crash recovery, cost tracking, git worktree isolation, automatic verification — tất cả built-in.

**vs GSD-1 (TÂCHES, 57.4K stars)**: GSD-1 là prompt framework inject instructions vào Claude Code qua slash commands. GSD-2 là real TypeScript application control agent session trực tiếp.

---

## 2. Install (5-minute first run)

**EN:**
```bash
# Step 1: Install (Node.js >= 22.0.0 required; Node 24 LTS recommended)
npm install -g gsd-pi

# Step 2: First launch (interactive setup wizard)
gsd

# Inside gsd:
/login                  # Choose LLM provider (Anthropic / OpenAI / Google / OpenRouter / 20+ others)
                        # OAuth supported for Claude Max + GitHub Copilot subscriptions
                        # ⚠️ For Google Gemini: USE API KEY, not OAuth (ToS risk per README)

# Step 3: First project (interactive)
cd ~/projects/my-test-project
gsd
/gsd                    # Step mode — pause-between-units wizard
```

**VN:**
```bash
# Bước 1: Install (Node.js >= 22.0.0 yêu cầu; Node 24 LTS recommended)
npm install -g gsd-pi

# Bước 2: First launch (interactive setup wizard)
gsd

# Trong gsd:
/login                  # Chọn LLM provider (Anthropic / OpenAI / Google / OpenRouter / 20+ khác)
                        # OAuth support cho Claude Max + GitHub Copilot subscriptions
                        # ⚠️ Cho Google Gemini: DÙNG API KEY, không OAuth (rủi ro ToS theo README)

# Bước 3: First project (interactive)
cd ~/projects/my-test-project
gsd
/gsd                    # Step mode — pause-between-units wizard
```

---

## 3. The Two Modes — Step vs Auto / Hai Mode — Step vs Auto

| Mode | Command | When to use / Khi nào dùng |
|------|---------|------|
| **Step** | `/gsd` or `/gsd next` | First-time learning gsd-2 / Lần đầu học gsd-2; đánh giá trước khi commit auto-mode |
| **Auto** | `/gsd auto` | After understanding step mode + ready to walk away / Sau khi hiểu step mode + sẵn sàng walk away |

**EN:** Step mode is the on-ramp. Auto mode is the highway. Both run the same state machine — the difference is whether you pause between units to inspect.

**VN:** Step mode là on-ramp. Auto mode là highway. Cả hai chạy cùng state machine — khác biệt là có pause giữa units để inspect hay không.

---

## 4. Storm Bear use cases / Use cases cho Storm Bear

### 4.1. Custom Scrum-tool development (MEDIUM-HIGH conditional)

**EN:** If Storm Bear builds custom internal tools (Scrum dashboard / retro assistant / DORA metric collector / Jira integration), gsd-2 is **strong fit**:
- Spec-driven discipline matches Storm Bear's wiki-routine philosophy
- Worktree isolation = safe experimentation
- Cost tracking + budget ceiling = predictable spend
- Crash recovery + headless mode = overnight unattended runs

Example workflow:
```bash
mkdir scrum-dashboard && cd scrum-dashboard
echo "# Scrum Dashboard MVP\n\nNext.js + Tailwind dashboard pulling Jira sprint velocity, cycle time, DORA metrics. Owner: Storm Bear. Audience: VN dev teams." > spec.md
gsd
/gsd auto    # walk away for 2-4 hours
```

**VN:** Nếu Storm Bear xây custom internal tools (Scrum dashboard / retro assistant / DORA metric collector / Jira integration), gsd-2 là **fit mạnh**:
- Spec-driven discipline match philosophy của wiki-routine
- Worktree isolation = safe experimentation
- Cost tracking + budget ceiling = chi tiêu dự đoán được
- Crash recovery + headless mode = overnight unattended runs

### 4.2. Vault tooling experiments (LOW direct / HIGH observational)

**EN:** Storm Bear vault itself is Markdown-knowledge-base, not code product. gsd-2 doesn't directly apply. **But**: gsd-2's architectural patterns (state-machine-from-disk, extension-first, worktree forensics, validate-gate-before-sealing) are **direct templates** for vault routine v2.2 evolution. See `(C) Entity 4` for vault-architectural lessons.

**VN:** Storm Bear vault tự nó là Markdown-knowledge-base, không phải code product. gsd-2 không apply trực tiếp. **Nhưng**: architectural patterns của gsd-2 (state-machine-from-disk, extension-first, worktree forensics, validate-gate-before-sealing) là **template trực tiếp** cho vault routine v2.2 evolution.

### 4.3. NOT a fit for / KHÔNG fit cho

- **Pure Markdown vault maintenance** — gsd-2 is for code projects, not knowledge-base curation
- **Client-facing Scrum coaching content** — wiki ingestion / ceremony notes / retro analysis don't need autonomous coding agent
- **One-off scripts** — overhead of gsd-2 (`.gsd/` directory + state machine + milestone planning) too heavy for 5-minute scripts

---

## 5. Cost & budget control / Kiểm soát cost & budget

**EN:** gsd-2 has 3-layer cost discipline:
1. **`token_profile: budget`** (40-60% savings via tier downgrades + skip research/reassess + minimal context)
2. **Complexity-based routing** (heuristic classifier picks light/standard/heavy tier per task)
3. **`budget_ceiling: 50.00`** (USD; auto mode pauses at limit; graduated downgrading at 50/75/90%)

**Initial sandbox**: Set `budget_ceiling: 5.00` for first week. Monitor `/gsd status` dashboard. Adjust based on actual spend.

**VN:** gsd-2 có 3-layer cost discipline:
1. **`token_profile: budget`** (tiết kiệm 40-60% qua tier downgrades + skip research/reassess + minimal context)
2. **Complexity-based routing** (heuristic classifier chọn light/standard/heavy tier per task)
3. **`budget_ceiling: 50.00`** (USD; auto mode pause khi đạt; graduated downgrading at 50/75/90%)

**Initial sandbox**: Set `budget_ceiling: 5.00` cho tuần đầu. Monitor `/gsd status` dashboard. Adjust theo actual spend.

---

## 6. GSD-1 vs GSD-2 decision matrix / Bảng quyết định GSD-1 vs GSD-2

| Question / Câu hỏi | Use GSD-1 | Use GSD-2 |
|---|:---:|:---:|
| Beginner just learning prompt framework patterns? | ✅ | |
| Want autonomous milestone execution with crash recovery? | | ✅ |
| Need cost tracking + budget ceilings? | | ✅ |
| Want fresh context window per task? | | ✅ |
| Already invested in `.planning/` directory? Migrate? | | ✅ (run `/gsd migrate`) |
| Want minimal install footprint (just slash commands)? | ✅ | |
| Need git worktree isolation + squash-merge? | | ✅ |
| Want HTML reports per milestone? | | ✅ |
| Building production code overnight unattended? | | ✅ |

**EN:** Per VISION.md verbatim, gsd-build's plan is to "eventually migrate GSD-1 users to GSD-2." If starting fresh, **start with gsd-2**. If on GSD-1 already, migrate when convenient.

**VN:** Theo VISION.md verbatim, plan của gsd-build là "eventually migrate GSD-1 users to GSD-2." Nếu starting fresh, **bắt đầu với gsd-2**. Nếu đang dùng GSD-1, migrate khi thuận tiện.

---

## 7. 4-week pilot roadmap / Roadmap pilot 4 tuần

### Week 1 — Step mode + 1 small milestone

**EN:** Goal: understand `.gsd/` directory structure + step mode workflow. Pick small project (CRUD app or static site).

- Day 1-2: Install + `/login` + step through 1 small milestone via `/gsd next`
- Day 3-4: Inspect `.gsd/` files (`PROJECT.md`, `M001-ROADMAP.md`, `S01-PLAN.md`)
- Day 5-7: Try `/gsd discuss` for architecture decisions; review HTML report

Budget: $5-10. Effort: ~6 hours.

**VN:** Mục tiêu: hiểu structure `.gsd/` + step mode workflow. Chọn project nhỏ (CRUD app hoặc static site).

### Week 2 — Auto mode supervised

**EN:** Goal: 1 milestone via `/gsd auto` — but stay supervising in nearby terminal.

- Day 1-2: Same project as Week 1, queue 2nd milestone, run `/gsd auto`
- Day 3-4: Use `/gsd discuss` from second terminal to steer mid-execution
- Day 5-7: Trigger pause + restart cycle to test crash recovery

Budget: $10-20. Effort: ~8 hours active + 8-16 hours auto-mode runtime.

### Week 3 — Headless + cron experiment

**EN:** Goal: validate headless mode for unattended overnight runs.

- Day 1-2: `gsd headless query` for instant JSON snapshots; integrate into shell scripts
- Day 3-4: Set up cron job: `gsd headless next` every 1h on a hobby project
- Day 5-7: Review `/gsd forensics` for any auto-mode failures

Budget: $20-40. Effort: ~6 hours active.

### Week 4 — Pilot decision

**EN:** Goal: decide adoption status for Storm Bear.

- Day 1-2: Review cost-spent vs value delivered
- Day 3-4: Compare with manual development workflow
- Day 5-7: Decision: integrate into Storm Bear toolkit / shelve / hand off to team for further evaluation

**Cumulative budget**: $35-70 over 4 weeks. Cumulative effort: ~25 active hours + ~30 unattended hours.

**VN:** **Cumulative budget**: $35-70 trong 4 tuần. Cumulative effort: ~25 giờ active + ~30 giờ unattended.

---

## 8. Two-terminals workflow / Workflow 2 terminal

**EN:** Recommended pattern (from README):
- **Terminal 1**: `gsd` → `/gsd auto` (let it build)
- **Terminal 2**: `gsd` → `/gsd discuss` (architecture decisions) / `/gsd status` (progress) / `/gsd queue` (next milestone)

Both terminals read+write same `.gsd/` files. Decisions in terminal 2 picked up at next phase boundary — no need to stop auto mode.

**VN:** Pattern recommended (từ README):
- **Terminal 1**: `gsd` → `/gsd auto` (để nó build)
- **Terminal 2**: `gsd` → `/gsd discuss` (architecture decisions) / `/gsd status` (progress) / `/gsd queue` (milestone tiếp)

Cả 2 terminal đọc+write cùng `.gsd/` files. Decisions ở terminal 2 picked up ở next phase boundary — không cần stop auto mode.

---

## 9. Common pitfalls / Pitfalls thường gặp

**EN:**
- **Don't run gsd-2 in production-critical repo without `git.isolation: worktree`** — auto mode CAN make destructive changes. Default is `none` (current branch) which is risky for high-stakes work.
- **Don't skip the budget ceiling** — without it, runaway loops can rack up significant LLM cost
- **Don't ignore `/gsd doctor`** — runs diagnostic checks; surface issues before they cascade
- **Don't blindly trust `validate-milestone`** — it compares roadmap criteria to results but can miss real-world acceptance issues
- **Don't run multiple gsd-2 instances on same project simultaneously** — `auto.lock` is per-session; concurrent runs may corrupt state

**VN:**
- **Đừng chạy gsd-2 trong production-critical repo mà không có `git.isolation: worktree`** — auto mode CÓ THỂ làm destructive changes. Default là `none` (current branch) rủi ro cho high-stakes work.
- **Đừng skip budget ceiling** — không có nó, runaway loops có thể tạo significant LLM cost
- **Đừng ignore `/gsd doctor`** — chạy diagnostic checks; phát hiện issues trước khi cascade
- **Đừng blindly trust `validate-milestone`** — compare roadmap criteria với results nhưng có thể miss real-world acceptance issues
- **Đừng chạy multiple gsd-2 instances trên cùng project simultaneously** — `auto.lock` per-session; concurrent runs có thể corrupt state

---

## 10. Key concepts to internalize / Concept cốt cần nắm

| Concept | Why it matters |
|---|---|
| **Hierarchy: Milestone → Slice → Task** | Iron rule: task fits in 1 context window. If can't, it's 2 tasks. |
| **Auto mode = state machine** | Not magic; reads `.gsd/` files + dispatches per disk state |
| **Worktree isolation** | Each milestone runs on own branch; squash-merged on completion |
| **Verification commands** | `npm run lint`, `npm run test` auto-run after task; auto-fix retries on failure |
| **Token profile** | budget/balanced/quality coordinates 40-60% / 10-20% / 0% savings |
| **Stuck detection** | Sliding-window detector; bounded artifact retries; pauses on indefinite loops |
| **Headless mode** | CI/cron-friendly; `gsd headless query` = instant JSON snapshot, no LLM, ~50ms |

---

## 11. Storm Bear architectural lessons (link to vault routine v2.2)

**EN:** gsd-2's `.gsd/STATE.md` + `.gsd/auto.lock` + `.gsd/journal/` + `.gsd/event-log.jsonl` are **direct architectural templates** for Storm Bear vault routine v2.2 evolution. See `(C) Entity 4` for full lessons. Highest-ROI lesson: **validate-gate-before-sealing pattern** = direct mini-audit protocol enhancement.

**VN:** `.gsd/STATE.md` + `.gsd/auto.lock` + `.gsd/journal/` + `.gsd/event-log.jsonl` của gsd-2 là **template architectural trực tiếp** cho Storm Bear vault routine v2.2 evolution. Xem `(C) Entity 4` cho full lessons. Lesson ROI cao nhất: **validate-gate-before-sealing pattern** = direct enhancement cho mini-audit protocol.

---

## 12. References / Tài liệu tham khảo

**Primary sources**:
- README: https://github.com/gsd-build/gsd-2/blob/main/README.md
- VISION: https://github.com/gsd-build/gsd-2/blob/main/VISION.md
- CONTRIBUTING: https://github.com/gsd-build/gsd-2/blob/main/CONTRIBUTING.md
- CHANGELOG: https://github.com/gsd-build/gsd-2/blob/main/CHANGELOG.md
- Mintlify docs: (per `mintlify-docs/` workspace)

**Cross-corpus**:
- Pi SDK origin: pi-mono v36 (`03 Projects/pi-mono - Beginner Analysis/`) — Storm Bear ranks **MEDIUM-HIGH #3** for multi-provider escape-hatch
- GSD-1 predecessor: get-shit-done v5 (`03 Projects/get-shit-done - Beginner Analysis/`) — TÂCHES author + 14+ harness support + context-rot framing
- SDD methodology peer: spec-kit v17 (`03 Projects/spec-kit - Beginner Analysis/`) — corporate-official SDD baseline

**External**:
- Pi SDK: https://github.com/badlogic/pi-mono
- RTK binary: https://github.com/rtk-ai/rtk
- $GSD Solana token: https://dexscreener.com/solana/dwudwjvan7bzkw9zwlbyv6kspdlvhwzrqy6ebk8xzxkv
- Discord: https://discord.com/invite/nKXTsAcmbT

---

## 13. Verdict / Kết luận

**EN:** gsd-2 is a **well-architected autonomous coding agent** with mature SDD discipline, strong cost-control, and architectural patterns worth studying even if you don't adopt the tool. For Storm Bear:
- **Direct adoption**: LOW (Markdown vault use case mismatch)
- **Conditional adoption**: MEDIUM-HIGH (if Storm Bear builds custom Scrum tools)
- **Architectural reference**: HIGH (state-machine-from-disk + extension-first + validate-gates → vault routine v2.2)

**Suggested next action for Storm Bear**: Document gsd-2 patterns in vault `(C) Entity 4` (already done in this wiki); defer pilot decision until Storm Bear has concrete custom-tool need; revisit at v60 wiki milestone.

**VN:** gsd-2 là **autonomous coding agent well-architected** với SDD discipline trưởng thành, cost-control mạnh, và architectural patterns đáng học ngay cả khi không adopt tool. Cho Storm Bear:
- **Direct adoption**: LOW (Markdown vault use case mismatch)
- **Conditional adoption**: MEDIUM-HIGH (nếu Storm Bear build custom Scrum tools)
- **Architectural reference**: HIGH (state-machine-from-disk + extension-first + validate-gates → vault routine v2.2)

**Action tiếp theo cho Storm Bear**: Document gsd-2 patterns trong vault `(C) Entity 4` (đã xong trong wiki này); defer pilot decision tới khi Storm Bear có concrete custom-tool need; revisit ở v60 wiki milestone.
