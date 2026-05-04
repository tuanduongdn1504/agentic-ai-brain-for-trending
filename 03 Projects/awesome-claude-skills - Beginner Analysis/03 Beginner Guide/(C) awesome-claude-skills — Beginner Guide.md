# (C) awesome-claude-skills — Beginner Guide (VN + EN)

> **Storm Bear corpus wiki v50 — corpus half-century milestone** | Source: `ComposioHQ/awesome-claude-skills`

---

## ⚠️ Đọc trước khi bắt đầu / Read this first

### License ambiguity (license claim mà không có file)
- README claim repo dùng Apache License 2.0 (badge + `## License` section).
- **NHƯNG**: không có file LICENSE ở root của repo. Chỉ có 9 trên 31 top-level skills mang LICENSE.txt (nội dung Apache-2.0 verbatim, là Anthropic skills nguyên bản được import).
- 22 skills còn lại + 832 wrappers trong `composio-skills/` không có file license nào.
- **Kết luận**: Apache-2.0 chỉ là claim ở README; không phải legal license file. Cho personal / vault-internal use thì OK; cho commercial / client-facing / public-distribution thì rủi ro pháp lý — coi như "all rights reserved" cho 856 trong 864 skills.

### Commercial-funnel transparency (operator deserves to know)
- Banner đầu README dẫn đến `dashboard.composio.dev` với UTM tracking đầy đủ (utm_source=Github, utm_medium=Youtube, utm_campaign=2025-11).
- Quickstart chỉ user install `connect-apps-plugin` rồi đăng ký dashboard.composio.dev trong 4 commands.
- **96.3% (832 trong 864)** skills trong repo này yêu cầu **Rube MCP** (sản phẩm thương mại của Composio) để hoạt động — không có Rube MCP thì 832 wrappers vô dụng.
- 5 surface thương mại: platform.composio.dev / dashboard.composio.dev / composio.dev/toolkits / rube.app/mcp / agentskb.com (sister product).
- Đây là **commercial-funnel mạnh nhất corpus đã quan sát qua 50 wikis** (Pattern #50 N=9).

### Recommendation
- ✅ **Clone-and-copy 5 skills "zero-commercial-coupling"** (xem pilot table phần 7 dưới) → an toàn, miễn phí, ~30-60 phút.
- ⚠️ **TRÁNH `connect-apps-plugin` và `composio-skills/*-automation/`** cho đến khi đánh giá rõ chi phí Rube MCP + chính sách dữ liệu + tuân thủ pháp luật VN.

---

## 1. awesome-claude-skills là gì? / What is awesome-claude-skills?

**VN**: Một danh mục curated các Claude Skill — kết hợp giữa **danh sách awesome-list** (style giống `awesome-mcp-servers`, `awesome-design-md`) **VÀ** **library skill bundle sẵn trong repo**. Repo này có 864 file SKILL.md / 905 directory — quy mô EXTREME (hạng 5 trong corpus, sau aidevops v47 ~2,665+ và ruflo v42 ~500+).

**EN**: A curated catalog of Claude Skills — hybrid of **awesome-list aggregator** (similar to `awesome-mcp-servers`, `awesome-design-md` style) **AND** **bundled in-repo skill library**. The repo ships 864 SKILL.md files / 905 directories — EXTREME primitive-count tier (5th in corpus, after aidevops v47 ~2,665+ and ruflo v42 ~500+).

3 tầng nội dung / 3 content layers:
1. **Aggregator README** — curate ~120 external skill links across 10 categories
2. **31 top-level in-repo skills** — Composio-built + 9 Anthropic-imported (with LICENSE.txt)
3. **832 Rube-MCP wrappers** in `composio-skills/` — thin instructions wrapping Composio's commercial product

---

## 2. Owner: Composio Inc. / Composio Inc. organization

| | VN | EN |
|---|---|---|
| Org | ComposioHQ trên GitHub | ComposioHQ on GitHub |
| Tuổi | ~3 năm (created 2023-03-21) | ~3 years (created 2023-03-21) |
| Public repos | 70 (lớn nhất corpus theo variant 3) | 70 (corpus-strongest variant 3 single-org) |
| Sản phẩm thương mại | platform.composio.dev / dashboard / Rube MCP / toolkits / AgentsKB | 5 commercial surfaces |
| Cộng đồng | Discord + X (@composio) + LinkedIn | Discord + X + LinkedIn |
| Tagline | "Composio equips agents with well-crafted tools" | same |

---

## 3. 10 categories trong README / 10 README categories

1. Document Processing (5 entries — docx/pdf/pptx/xlsx từ anthropics/skills + Markdown→EPUB)
2. Development & Code Tools (24 entries — bao gồm 5 entry từ obra/superpowers)
3. Data & Analysis (4 entries)
4. Business & Marketing (5 entries — all in-repo: brand-guidelines, competitive-ads-extractor, domain-name-brainstormer, internal-comms, lead-research-assistant)
5. Communication & Writing (7 entries)
6. Creative & Media (7 entries)
7. Productivity & Organization (8 entries)
8. Collaboration & Project Management (5 entries)
9. Security & Systems (4 entries)
10. App Automation via Composio (~70+ entries — broken relative links pointing to composio-skills/ subdirectory)

---

## 4. 31 top-level in-repo skills / 31 top-level in-repo skills

### Anthropic-imported (9, with LICENSE.txt = Apache-2.0)
artifacts-builder, brand-guidelines, canvas-design, internal-comms, mcp-builder, skill-creator, slack-gif-creator, theme-factory, webapp-testing

### Composio-built (19, no LICENSE)
changelog-generator, competitive-ads-extractor, connect, connect-apps, connect-apps-plugin, content-research-writer, developer-growth-analysis, document-skills, domain-name-brainstormer, file-organizer, image-enhancer, invoice-organizer, langsmith-fetch, lead-research-assistant, meeting-insights-analyzer, raffle-winner-picker, tailored-resume-generator, twitter-algorithm-optimizer, video-downloader

### Meta-skills (3)
skill-creator (also Anthropic-imported), skill-share, template-skill

---

## 5. composio-skills/ — 832 Rube MCP wrappers / 832 Rube MCP wrappers

Mỗi entry là một thin wrapper với YAML frontmatter:
```yaml
---
name: <toolkit>-automation
description: "Automate <toolkit> tasks via Rube MCP (Composio)..."
requires:
  mcp: [rube]
---
```

**Toolkit categories** (per README pseudo-grouping): CRM (5), Project Management (10), Communication (6), Email (4), Code & DevOps (10), Storage (4), Spreadsheets/DBs (3), Calendar (4), Social Media (6), Marketing (5), Support (4), E-commerce (3), Design/Collaboration (6), Analytics (5), HR (1), Automation (1), Zoom (1) = ~76 catalogued in README; full 832 entries inside `composio-skills/`.

**Tất cả không hoạt động nếu không signup Rube MCP commercial.**

---

## 6. Cách install / How to install

### Option A — Clone-and-copy 1 skill (recommended for vault use)
```bash
# 1. Clone repo
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cd awesome-claude-skills

# 2. Copy skill into Claude Code skills directory
mkdir -p ~/.config/claude-code/skills/
cp -r meeting-insights-analyzer ~/.config/claude-code/skills/

# 3. Verify
head ~/.config/claude-code/skills/meeting-insights-analyzer/SKILL.md

# 4. Restart Claude Code; skill auto-activates when relevant
```

### Option B — Plugin marketplace (Claude Code 2.x+)
```bash
# Inside Claude Code:
/plugin marketplace add ComposioHQ/awesome-claude-skills
# Then browse and install individual skills via /plugin UI
```

### Option C — connect-apps-plugin (commercial signup REQUIRED — proceed with caution)
```bash
claude --plugin-dir ./connect-apps-plugin
/connect-apps:setup
# Paste API key from dashboard.composio.dev (signup required)
exit
claude
```
**⚠️ Option C routes user into Composio commercial product. Skip unless explicitly evaluating Rube MCP commercial product.**

### Option D — Skills API (programmatic, requires Claude API key)
```python
import anthropic
client = anthropic.Anthropic(api_key="your-api-key")
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    skills=["skill-id-here"],
    messages=[{"role": "user", "content": "Your prompt"}]
)
```

---

## 7. Storm Bear pilot table — 5-skill shopping list (clone-and-copy)

| Rank | Skill | Storm Bear use case | LICENSE.txt? | Effort |
|------|-------|---------------------|--------------|--------|
| 1 | **meeting-insights-analyzer** | Phân tích transcript Scrum retro / behavioral patterns / speaking ratios | ❌ | 5 min |
| 2 | **file-organizer** | Tổ chức file trong vault (tìm trùng lặp, gợi ý cấu trúc) | ❌ | 5 min |
| 3 | **content-research-writer** | Hỗ trợ Storm Bear publishing (research + citations + section feedback) | ❌ | 5 min |
| 4 | **changelog-generator** | Tự động sinh changelog cho Storm Bear corpus version-history (50-wiki milestone là timing đẹp) | ❌ | 5 min |
| 5 | **skill-creator** | Meta-skill: cải thiện chất lượng `05 Skills/` của Storm Bear vault | ✅ Apache-2.0 | 5 min |

**Tổng**: 25-60 phút cho 5 skills + activation testing.
**Risk**: THẤP. Tất cả read-only / không yêu cầu auth / uninstall đơn giản (xóa folder).
**License caveat**: Skills 1-4 không có LICENSE.txt riêng; dựa vào README claim Apache-2.0 (mà không có root LICENSE file). Cho VAULT-INTERNAL OK; cho commercial / public release coi như "all rights reserved" cho đến khi Composio thêm LICENSE.

---

## 8. Roadmap 4 tuần đánh giá / 4-week evaluation roadmap

### Week 1 — Pilot 5 skills (~1h tổng)
- Day 1: Clone repo + install meeting-insights-analyzer + test với 1 transcript Scrum retro thật
- Day 2: Install file-organizer + chạy trên 1 subfolder của Storm Bear vault (`03 Projects/` chẳng hạn)
- Day 3-4: Install content-research-writer + thử với 1 đoạn writing sắp publish
- Day 5: Install changelog-generator + thử sinh changelog cho corpus 50-wiki
- Day 6-7: skill-creator + audit chất lượng `05 Skills/` của Storm Bear

### Week 2 — Đánh giá fitness từng skill (~30 min/skill)
- Skill nào activate đúng context? Skill nào noise / over-trigger?
- Skill nào cần customize (vd: fix VN-specific terminology)?
- Skill nào keep / remove sau pilot?

### Week 3 — (Tùy chọn) Đánh giá Composio commercial track
- ⚠️ **CHỈ làm nếu Storm Bear thực sự cần workflow Jira/Linear/Slack/Gmail automation**.
- Đăng ký free tier dashboard.composio.dev. Đọc pricing page.
- Test 1 wrapper (vd: jira-automation hoặc gmail-automation) với data thật.
- Đánh giá: data residency? VN compliance? Cost projection cho client-facing use?

### Week 4 — Decision point
- Keep 3-5 skills cố định trong `~/.config/claude-code/skills/`
- Document decision trong vault (`(C) awesome-claude-skills pilot summary.md` hoặc tương tự)
- Reject Composio commercial product OR commit to free-tier-only OR commit to paid-tier evaluation
- Update Storm Bear pilot ranking

---

## 9. Recursive corpus reference (Storm Bear-specific) / Storm Bear-specific recursion observation

awesome-claude-skills README cite **`obra/superpowers`** (chính là chủ đề wiki v2 của Storm Bear corpus) **5 lần** trong 1 README:
- test-driven-development
- brainstorming
- root-cause-tracing
- finishing-a-development-branch
- using-git-worktrees

Đây là **observation Pattern #57 thứ 5 trong corpus và LẦN ĐẦU TIÊN aggregator-mediated multi-citation**. Storm Bear corpus đang được catalog tại external aggregator một cách gián tiếp — qua Superpowers v2.

**Ý nghĩa cho Storm Bear**:
- Corpus member (Superpowers v2) được external commercial aggregator cite 5× → external validation cho corpus selection criteria.
- Khi Storm Bear publish public skills, có thể được aggregator này (hoặc aggregator khác) curate. Storm Bear publish chiến lược nên để ý awesome-list-genre dynamics.

---

## 10. Pattern observations (Storm Bear corpus context) / Pattern observations

| Pattern | v50 contribution |
|---------|-----------------|
| **#68 Awesome-list-genre** | 4th data point; sub-type c (AI-runtime-infrastructure-directory) reaches N=2; hybrid sub-variant observed (corpus-first) |
| **#50 Commercial-Funnel** | N=9 — corpus-strongest funnel (5 surfaces + 3 UTM campaigns + 96.3% skills require commercial) |
| **#57 Recursive Corpus Reference** | 5th data point; corpus-first aggregator-mediated multi-citation (obra/superpowers 5× + anthropics/skills 5×) |
| **#29 License-Diversity** | 4th absent-LICENSE sub-context (absent-LICENSE-with-README-claim) |
| **#59 Plugin Marketplace** | corpus-first directory-scoped marketplace.json |
| **#22 AGENTS.md** | 4/4 awesome-list-genre absence pattern preserved |
| **#18 MCP** | corpus-first explicit MCP-requirement field in skill YAML at scale (832 wrappers) |
| **#19 archetype 4** | no individual lineage; org-only branding |
| **#27 Community-Viral** | aggregator-amplified-commercial-viral 9.4K stars/month |
| **#17 variant 3** | strongest commercial-startup-ecosystem evidence (Composio 70 repos) |
| **#2 Distribution** | 4 surfaces (clone+copy / marketplace UI / `--plugin-dir` / Skills API) |

**Net Pattern Library delta v50**: 0 new active candidates / 0 new OBSERVATION-TRACKs / 11 patterns strengthened. **14-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES STREAK** (v37-v50 — corpus record).

---

## 11. v50 corpus half-century milestone

50 wikis / 8 days (v1 ECC: 2026-04-17 → v50 awesome-claude-skills: 2026-04-25).

Storm Bear corpus đã đạt half-century milestone với:
- 73 patterns (37 confirmed + 19 active + 3 stale + 9 retired + 5 OT)
- Pattern Library health unprecedented (ratio 0.513:1, 14-streak zero-registration)
- 5 distinct tiers + outside-scope all multi-validated
- 39 consecutive Storm Bear meta-entities (v10-v50)
- 28+ consecutive wikis at ~2h velocity plateau

**Strategic recommendation tại v50**: thực hiện v27 diagnostic HIGH bundle TRƯỚC v51. 50-wiki milestone là natural cadence-break tốt nhất.

---

## 12. Resources / References

### Official Anthropic
- [Claude Skills Overview](https://www.anthropic.com/news/skills)
- [Skills User Guide](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Creating Custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Skills API Documentation](https://docs.claude.com/en/api/skills-guide)
- [Anthropic Skills Repo](https://github.com/anthropics/skills) (official example skills)

### awesome-claude-skills repo
- Repo: https://github.com/ComposioHQ/awesome-claude-skills
- Discord: https://discord.com/invite/composio
- Twitter: https://x.com/composio
- Email: support@composio.dev

### Composio commercial (proceed with caution)
- platform.composio.dev (free tier signup)
- dashboard.composio.dev (authenticated dashboard)
- composio.dev/toolkits (1000+ apps)
- rube.app/mcp (Rube MCP endpoint)

### Storm Bear corpus context
- v2 Superpowers wiki (corpus member; cited 5× by v50)
- v8 build-your-own-x (Pattern #68 1st)
- v25 awesome-design-md (Pattern #68 2nd)
- v31 awesome-mcp-servers (Pattern #68 3rd; sibling sub-type c)
- v49 MiroFish (immediate predecessor; ratio-preservation chain)
- Storm Bear vault `PATTERN_LIBRARY.md`

---

## 13. Verdict cho Storm Bear operator / Verdict for Storm Bear

**Pilot rating**: MEDIUM — direct utility cho 5 skills cụ thể; observational HIGH cho pattern + architectural reference + Pattern #57 recursion.

**Storm Bear pilot ranking refresh tại v50**:
1. claude-hud v35 (statusline; 5-min install; immediate ROI)
2. spec-kit v17 (SDD methodology)
3. claude-howto v32 (self-onboarding meta-ROI)
4. OMC v27 (multi-runtime orchestration)
5. rowboat v43 (corpus direct-peer-category)
6. claude-context v40 (vault semantic-search pilot)
7. **awesome-claude-skills v50 🆕 (5-skill clone-and-copy + Pattern #57 recursion observation; 30-60 min)**
8. pi-mono v36 / 9. claude-code-best-practice v34 / 10. ruflo v42

**Caveat strongest** corpus đã observe: commercial-funnel mạnh nhất Storm Bear đã thấy. Operator phải tỉnh táo về UTM tracking + Rube MCP commercial dependency + license-claim-without-file ambiguity.

**50-wiki milestone reflection**: Storm Bear corpus đã chứng minh routine v2.1 + Pattern Library compounds. v50 là cadence-break tốt để execute v27 diagnostic HIGH bundle (30 sessions deferred — BLOCKING-RECOMMENDATION 6× threshold).
