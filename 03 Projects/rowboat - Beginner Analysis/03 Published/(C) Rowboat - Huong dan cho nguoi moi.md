# (C) Rowboat — Hướng dẫn cho người mới / Beginner's Guide

**Song ngữ VN + EN / Bilingual Vietnamese + English**
**Đối tượng / Audience:** Người mới dùng Rowboat, đặc biệt là người đang dùng Obsidian vault hoặc Karpathy LLM Wiki pattern
**Wiki v43 Storm Bear corpus** | 2026-04-24

---

## Phần 1 — Rowboat là gì? / What is Rowboat?

### VN

Rowboat là một **AI coworker open-source** — một ứng dụng desktop (Mac/Windows/Linux) biến công việc của bạn thành một knowledge graph và dùng nó để giúp bạn hoàn thành công việc. Khác biệt quan trọng so với các AI assistant thông thường:

- **Local-first:** Tất cả dữ liệu lưu trên máy bạn, dưới dạng Markdown thuần
- **Obsidian-compatible:** Notes có backlinks, có thể inspect + edit thủ công
- **Memory compounds:** Context tích luỹ theo thời gian, không phải mỗi câu hỏi bắt đầu từ số 0
- **Bring-your-own-model:** Dùng Ollama/LM Studio local hoặc OpenAI/Anthropic/Google/OpenRouter với API key riêng

Được build bởi **Rowboat Labs**, một **startup Y Combinator S24** (Summer 2024 batch).

### EN

Rowboat is an **open-source AI coworker** — a desktop app (Mac/Windows/Linux) that turns your work into a knowledge graph and uses it to help you get work done. Key differences from typical AI assistants:

- **Local-first:** All data lives on your machine as plain Markdown
- **Obsidian-compatible:** Notes have backlinks, can be inspected + edited manually
- **Memory compounds:** Context accumulates over time, not cold-start per query
- **Bring-your-own-model:** Use local Ollama/LM Studio or hosted OpenAI/Anthropic/Google/OpenRouter with your own API key

Built by **Rowboat Labs**, a **Y Combinator S24 (Summer 2024)** batch startup.

---

## Phần 2 — Corpus-first signals (so với 43 wiki trước)

**Rowboat là corpus-first về:**

1. **YC S24 badge đặt ở project-level** (43 wiki đầu tiên mới có wiki có YC-batch badge trên README header)
2. **`claude-cowork` repo topic** — signal định vị Anthropic-runtime-aligned + AI-coworker-category
3. **4-surface OSS-only distribution ở T5** (desktop binary + Docker compose + npm + PyPI, tất cả Apache-2.0)
4. **Knowledge-graph-as-Markdown explicitly Obsidian-compatible ở T5** — đây là **peer-category trực tiếp nhất với Storm Bear vault** trong 43 wiki
5. **Implicit Karpathy touchpoint ở T5** — Rowboat sao chép cấu trúc Karpathy /raw folder + LLM Wiki pattern nhưng KHÔNG cite Karpathy. Đây là first implicit-not-explicit Karpathy structural parallel trong corpus.
6. **Track Blocks:** YAML-fenced live-updating notes với 4 trigger types + 2-pass LLM classifier (liberal Pass 1 + strict Pass 2)
7. **Product-pivot-in-monorepo:** Legacy multi-agent SaaS (Next.js) coexist với new Electron flagship trong cùng 1 repo
8. **Triple-package distribution:** rowboat repo + `@rowboatlabs/rowboatx` npm + `rowboat` PyPI

---

## Phần 3 — Tier placement (T5 Agent-as-application)

**Tier 5 (Agent-as-application):** Rowboat là 8TH T5 entrant trong Storm Bear corpus.

- v9 deer-flow (research) / v10 autoresearch (ML) / v14 paperclip (orchestration) / v24 Skyvern (browser) / v30 OpenHands (SWE) / v38 DeepTutor (education) / v41 browser-use (browser-hybrid) / **v43 rowboat (personal-productivity)**
- **100% archetype diversity** ở N=8 — mỗi T5 entrant có distinct sub-archetype

Rowboat introduces sub-archetype **personal-productivity-application**:
- Deploy trên thiết bị end-user (desktop)
- Operate trên personal data (emails / calendar / notes)
- Maintain knowledge graph persistent (vault)
- Augment user's work (không autonomous thay thế)
- Local-first data stewardship

---

## Phần 4 — Cài đặt / Installation

### VN (5 phút)

**Cách 1 — Desktop binary (khuyên dùng):**
1. Vào https://www.rowboatlabs.com/downloads
2. Tải file cho OS của bạn (Mac DMG / Windows .exe / Linux AppImage/DEB)
3. Cài bình thường
4. Mở app → chọn thư mục vault (khuyến nghị: tạo test vault mới, KHÔNG chỉ đến Storm Bear vault chính)

**Cách 2 — Docker compose (legacy SaaS, advanced):**
```bash
git clone https://github.com/rowboatlabs/rowboat
cd rowboat
cp .env.example .env
# Edit .env with OPENAI_API_KEY
./start.sh
```
(Deploy `apps/rowboat/` legacy multi-agent SaaS tại http://localhost:3000)

**Cách 3 — CLI server (npm):**
```bash
npm install -g @rowboatlabs/rowboatx
rowboatx
```

**Cách 4 — Python SDK:**
```bash
pip install rowboat
```

### EN

**Option 1 — Desktop binary (recommended):**
1. Visit https://www.rowboatlabs.com/downloads
2. Download for your OS (Mac DMG / Windows .exe / Linux AppImage/DEB)
3. Install normally
4. Open app → select vault directory (recommend: create a fresh test vault, do NOT point at primary Obsidian vault)

**Option 2 — Docker compose** (legacy SaaS, advanced):
```bash
git clone https://github.com/rowboatlabs/rowboat
cd rowboat
cp .env.example .env
# Edit .env with OPENAI_API_KEY
./start.sh
```

**Option 3 — CLI server:** `npm install -g @rowboatlabs/rowboatx && rowboatx`

**Option 4 — Python SDK:** `pip install rowboat`

---

## Phần 5 — Kết nối Google (Gmail + Calendar + Drive)

### VN (15 phút, following google-setup.md 7-step guide)

1. Vào https://console.cloud.google.com/
2. Tạo project mới (ví dụ: "Rowboat Integration")
3. Enable 3 APIs: Gmail API + Google Calendar API + Google Drive API
4. Configure OAuth consent screen (External, Testing mode OK)
5. Add test user (email của bạn)
6. Create OAuth Client ID kiểu **Web application**, redirect URI `http://localhost:8080/oauth/callback`
7. Copy Client ID + Client Secret vào Rowboat khi được hỏi

**Lưu ý:** Giữ app ở Testing mode — không cần publish. App hoạt động bình thường với Testing mode cho cá nhân.

### EN

Follow the 7-step guide in `google-setup.md`. 15 minutes. Keep app in Testing mode — no publication needed for personal use.

---

## Phần 6 — Tính năng chính / Core features

### VN

**1. Knowledge graph tự động từ Gmail + Calendar:**
- Rowboat đồng bộ email threads và calendar events
- Agent `note_creation` extract entities (people / companies / projects / decisions) → Markdown notes với backlinks
- Hybrid mtime+hash change detection tránh re-process files không đổi

**2. Track Blocks (live-updating notes):**
YAML fence `` ```track...``` `` trong bất kỳ Markdown note nào → tự động refresh theo schedule hoặc event.

4 trigger types:
- **Manual:** Chạy khi bạn/Copilot click Run
- **Cron:** Chạy theo cron expression (ví dụ: `"0 * * * *"` = mỗi giờ)
- **Window:** Tối đa 1 lần trong time-of-day window (ví dụ: "buổi sáng")
- **Once:** Chạy một lần ở thời điểm tương lai
- **Event-driven:** Chạy khi có event matching natural-language criteria

Ví dụ track "Chicago time mỗi giờ":
~~~markdown
```track
trackId: chicago-time
instruction: Show current time in Chicago in 12-hour format
schedule: { type: cron, expression: "0 * * * *" }
```

<!--track-target:chicago-time-->
(generated output refreshes here)
<!--/track-target:chicago-time-->
~~~

**3. Cmd+K Copilot inline:**
- Ở bất kỳ đâu trong editor, nhấn Cmd+K → Copilot modal
- Ví dụ: *"Add a track that shows competitor news from Twitter weekly"* → Copilot tạo track block
- Ví dụ: *"Prep me for my meeting with Alex"* → Copilot tạo brief từ prior emails + calendar events + meeting notes

**4. Voice memo → knowledge graph:**
- Dùng Deepgram API (paid) cho voice input
- Voice memos auto-capture key takeaways vào graph

**5. PDF deck generation:**
- *"Build me a deck about Q2 roadmap"* → Rowboat generates PDF using vault context

### EN

**1. Auto knowledge graph from Gmail + Calendar:**
- Syncs email threads + calendar events
- `note_creation` agent extracts entities → Markdown notes with backlinks
- Hybrid mtime+hash change detection avoids reprocessing

**2. Track Blocks:** YAML-fenced auto-updating regions. 4 trigger types (manual / cron / window / once / event-driven). Natural-language event-match-criteria.

**3. Cmd+K inline Copilot:** Context-aware assistant at cursor.

**4. Voice memos:** Deepgram STT → knowledge graph auto-capture.

**5. PDF deck generation:** Generate decks from vault context.

---

## Phần 7 — Bring-your-own-model (BYOM)

### VN

Rowboat hỗ trợ swap model bất kỳ lúc nào:

| Provider | Type | Cài đặt |
|---|---|---|
| Ollama | **Local** | Install Ollama + pull model → Rowboat tự detect |
| LM Studio | **Local** | Mở LM Studio + load model → Rowboat qua OpenAI-compatible API |
| OpenAI | Hosted | API key |
| Anthropic | Hosted | API key (khuyến nghị cho Claude-compatibility) |
| Google | Hosted | API key |
| OpenRouter | Hosted abstraction | API key (access 100+ models) |
| Vercel AI Gateway | Routing layer | Sign in tới Vercel (fallback cho signed-in users) |

**Config file:** `~/.rowboat/config/models.json`
```json
{
  "provider": { "flavor": "anthropic", "apiKey": "sk-ant-..." },
  "model": "claude-3-5-sonnet-20241022"
}
```

**Privacy nuance:** Local-first áp dụng cho data-at-rest (vault files). Khi dùng hosted LLM (OpenAI/Anthropic/etc.), prompts vẫn flow tới provider. Muốn full-local: dùng Ollama hoặc LM Studio.

### EN

Rowboat supports swapping any model anytime. Local option: Ollama/LM Studio. Hosted options: OpenAI/Anthropic/Google/OpenRouter/Vercel AI Gateway.

**Privacy nuance:** Local-first applies to data-at-rest (vault files). Hosted LLM prompts still flow to provider. For full-local: use Ollama or LM Studio.

---

## Phần 8 — MCP + External tools

### VN

Rowboat kết nối với external tools qua:

- **MCP servers:** Bất kỳ Model Context Protocol-compatible server (Linear / Jira / GitHub / Slack / Twitter / custom)
- **Composio.dev:** Library of pre-built product integrations (API key ở `~/.rowboat/config/composio.json`)
- **Exa:** Web research search (API key ở `~/.rowboat/config/exa-search.json`)
- **Fireflies:** Alternative meeting-notes capture

**Workflow Scrum Coach:**
- MCP Linear/Jira → pull sprint tickets → auto-summarize vào retrospective notes
- MCP Slack → track decision threads → auto-add vào knowledge graph
- MCP GitHub → monitor PR activity → update project status tracks

### EN

Connect MCP servers (Linear/Jira/GitHub/Slack/Twitter/custom) + Composio.dev external tools + Exa web search + Fireflies meeting notes.

---

## Phần 9 — Storm Bear pilot relevance (HIGH #1)

### VN

Rowboat là **#1 pilot candidate** cho Storm Bear operator ở v43 (displace claude-hud v35):

**Tại sao HIGH relevance:**

1. **Direct peer-category:** Rowboat IS structurally what Storm Bear vault is — local Markdown knowledge graph với LLM assistance. Trong 43 wiki, đây là match cấu trúc gần nhất.

2. **Empirical test thesis:** Storm Bear bet on human-maintainer + LLM-assistant. Rowboat bet on AI-maintainer + human-reviewer. Pilot test → answer: "Automate wiki maintenance có work better không?"

3. **Zero-commitment evaluation:** Apache-2.0 + no subscription + 5-min install + uninstallable. Không mất gì.

4. **Non-disruptive:** Point Rowboat ở fresh test vault, KHÔNG Storm Bear primary vault. Observe rồi decide.

**Pilot protocol đề xuất (1-4 tuần):**

**Tuần 1:**
- Install Mac DMG
- Connect Gmail + Calendar
- Fresh test vault
- Quan sát: entity extraction quality, cross-reference emergence, false-positive rate

**Tuần 2:**
- Compare knowledge-graph structure vs Storm Bear entity-page format (13-section canonical)
- Test Track Blocks: tạo 3 scheduled + 2 event-driven tracks
- Test voice memo workflow
- Test "prep me for meeting" query quality

**Tuần 3-4 (nếu evaluation tiếp tục):**
- Point Rowboat ở Storm Bear primary vault (read-only test)
- Does Rowboat respect Storm Bear naming + cross-references?
- Does Rowboat auto-tagging conflict với Obsidian property syntax?
- Decision: **adopt / hybrid / reject**

**Outcome interpretation:**

- **Rowboat produces pattern-level observations** → adopt hybrid (Rowboat for sync + Storm Bear for deliberate patterns)
- **Rowboat produces only entity-level extraction** → Storm Bear Pattern Library function validated as distinct
- **Rowboat produces hallucinations** → Storm Bear manual discipline vindicated

Dù outcome nào, kết quả pilot đều strengthen Storm Bear (validate hoặc deepen pattern library).

### EN

Rowboat ranks **#1 Storm Bear pilot** at v43. Most direct peer-category match in 43 wikis. Empirical test of "automate wiki maintenance" thesis. Zero-commitment evaluation: Apache-2.0 + 5-min install + uninstallable. Fresh test vault + 1-4 week protocol. Outcome either validates Storm Bear's human-maintainer discipline OR motivates hybrid adoption.

---

## Phần 10 — 4-tuần learning roadmap

### VN

**Tuần 1: Install + Core workflow**
- Day 1-2: Install + Google setup + fresh test vault
- Day 3-4: Sync 1 week of Gmail + Calendar → observe knowledge graph build
- Day 5-7: Test Cmd+K Copilot với 5 different query types (meeting prep / email draft / topic summary / track creation / ad-hoc Q&A)

**Tuần 2: Advanced features**
- Day 8-10: Create 3 scheduled Track Blocks (daily morning briefing / weekly competitor tracker / monthly retrospective)
- Day 11-12: Create 2 event-driven Track Blocks (trigger on new Gmail with Project X / trigger on Calendar event containing "1:1")
- Day 13-14: Test voice memos + "prep me for meeting" workflow

**Tuần 3: Integration depth**
- Day 15-17: Add Composio integration (Linear hoặc Jira)
- Day 18-19: Add Exa web research
- Day 20-21: Add custom MCP server (choice: GitHub / Slack / Twitter)

**Tuần 4: Decision + hybrid evaluation**
- Day 22-24: Point Rowboat ở Storm Bear primary vault (read-only mode recommended)
- Day 25-26: Compare knowledge-graph quality vs manual Storm Bear curation
- Day 27-28: **Decision:** adopt / hybrid / reject với documentation in `04 Reviews/(C) 2026-05-24 Rowboat pilot evaluation.md`

### EN

**Week 1:** Install + Google + fresh test vault; test Cmd+K Copilot across 5 query types
**Week 2:** Create 3 scheduled + 2 event-driven Track Blocks; test voice + meeting prep
**Week 3:** Add Composio (Linear/Jira) + Exa + 1 MCP server
**Week 4:** Point at Storm Bear primary (read-only); decide adopt/hybrid/reject

---

## Phần 11 — Caveats + Tradeoffs

### VN

**Rủi ro / Risks:**

1. **YC-stage bus factor:** Rowboat Labs là startup YC S24, team nhỏ (2-4 người ước tính). Nếu startup fail, binary tiếp tục work nhưng no future updates.

2. **Product pivot in progress:** Legacy multi-agent SaaS (`apps/rowboat`) coexist với new Electron flagship (`apps/x`). Unclear dual-product maintenance strategy.

3. **EN-only:** Không có VN/CN/JA/KO i18n. Giao diện English-only.

4. **Data flow to LLM provider:** Local-first áp dụng data-at-rest. Hosted LLM (OpenAI/Anthropic/etc.) nhận prompts. Mitigation: dùng Ollama/LM Studio local.

5. **Voice paid APIs:** Deepgram (STT) + ElevenLabs (TTS) tính phí per-usage. Cost management cần thiết.

6. **No mobile:** Desktop-only. Mobile không planned.

7. **No multi-user:** Personal coworker positioning. Team features yêu cầu legacy SaaS tier.

8. **No built-in vault sync:** User tự manage sync (Git / iCloud / Dropbox). Không có official sync mechanism.

9. **Undeclared paid tier possibility:** Rowboat Labs có commercial entity + `billing/` subsystem in code. Paid tier có thể launch bất kỳ lúc nào, có thể alter OSS experience.

10. **Product-pivot risk:** Nếu Rowboat Labs pivot again, current Electron app có thể bị deprecate.

### EN

**Risks:** YC-stage bus factor (2-4 team) / product pivot mid-life / EN-only / hosted LLM data flow / voice paid APIs / desktop-only / no multi-user / no built-in vault sync / undeclared paid tier possibility / product-pivot risk.

---

## Phần 12 — References + Next action

### VN

**Chính thức:**
- Repo: https://github.com/rowboatlabs/rowboat
- Download: https://www.rowboatlabs.com/downloads
- Discord: https://discord.gg/wajrgmJQ6b
- Twitter: @rowboatlabshq

**Storm Bear wiki context:**
- Wiki này: `03 Projects/rowboat - Beginner Analysis/`
- Phase 4b deliverable: `(C) T5 8-way + personal-productivity-application + Storm Bear direct-peer-category.md`
- Pattern library post-v43: 0 new active candidates (7-streak), ratio 0.54:1 UNPRECEDENTED
- Prior peer wikis: v10 autoresearch (explicit Karpathy) / v16 graphify (explicit Karpathy) / v15 multica (1st Electron) / v14 paperclip (T5 orchestration)

**Next action (HIGH priority):**

1. **Schedule 2-4h** cho Rowboat pilot Week 1 trong 2 tuần tới
2. **Backup Storm Bear primary vault** trước khi touch anything (Git push latest)
3. **Create `04 Reviews/(C) YYYY-MM-DD Rowboat pilot week 1.md`** structure cho evaluation documentation
4. **v27 diagnostic HIGH bundle:** 21 sessions deferred. Rowboat pilot có thể integrate với diagnostic-HIGH item #1 vault CLAUDE.md refactor nếu pilot outcome favorable.

### EN

**Official:** repo github.com/rowboatlabs/rowboat / rowboatlabs.com/downloads / Discord / Twitter @rowboatlabshq

**Storm Bear context:** v43 wiki folder / Phase 4b deliverable / 7-streak zero-registration preserved / ratio 0.54:1 UNPRECEDENTED

**Next action HIGH:** Schedule 2-4h Rowboat pilot Week 1 within 2 weeks. Backup Storm Bear primary vault first. Rowboat pilot could integrate with v27 diagnostic bundle if outcome favorable.

---

**End of bilingual beginner guide.** Ngày shipped: 2026-04-24. Wiki số 43 trong Storm Bear corpus.
