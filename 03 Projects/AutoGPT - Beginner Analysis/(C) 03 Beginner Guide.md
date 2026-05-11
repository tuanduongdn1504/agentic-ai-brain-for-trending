# (C) AutoGPT — Hướng dẫn cho người mới (Beginner Guide)

> Bilingual VN+EN beginner guide for `Significant-Gravitas/AutoGPT`
> Wiki v59 — Storm Bear corpus 59th wiki
> 2026-05-07 (session 71)

⚠️ **Đọc trước / Read first:**

1. **License:** AutoGPT có cấu trúc dual-licensing — `autogpt_platform/` folder dùng **PolyForm Shield License** (source-available, không phải OSI; cấm dùng để xây service cạnh tranh), phần còn lại dùng **MIT**. Cân nhắc kỹ nếu định triển khai thương mại.
2. **EXTREME complexity:** AutoGPT là multi-component monorepo với 7+ primitive types — không phải "install và chạy ngay" như n8n/OpenSpec/mattpocock skills.
3. **Foundational status:** AutoGPT là dự án viral-foundational tháng 4/2023 — đã ~3 năm tuổi; cấu trúc đang transition từ Classic standalone → Platform cloud-tier.

---

## 1. AutoGPT là gì? / What is it?

**VN:** AutoGPT là một autonomous-agent platform mã nguồn mở (185K+ stars) do Toran Bruce Richards tạo ra tháng 3/2023, hiện được Significant-Gravitas org duy trì. Đây là dự án catalyst cho cả làn sóng autonomous-agent năm 2023. Hiện AutoGPT có 3 thành phần chính:

- **AutoGPT Platform** (`autogpt_platform/`) — platform xây agent + workflow + monitoring (license PolyForm-Shield, đang phát triển)
- **AutoGPT Classic** (`classic/` root) — agent gốc 2023 standalone (license MIT)
- **AutoGPT Forge** (`classic/forge/`) — toolkit để xây agent custom (license MIT)

**EN:** AutoGPT is an open-source autonomous-agent platform (185K+ stars) created by Toran Bruce Richards in March 2023, currently stewarded by the Significant-Gravitas organization. It was THE catalyst for the entire 2023 autonomous-agent boom. AutoGPT has 3 main components today:

- **AutoGPT Platform** (`autogpt_platform/`) — agent-builder + workflow management + monitoring (PolyForm-Shield licensed; in-development)
- **AutoGPT Classic** (`classic/` root) — original 2023 standalone agent (MIT licensed)
- **AutoGPT Forge** (`classic/forge/`) — toolkit for building custom agents (MIT licensed)

## 2. Corpus-first signals (v59)

- **2nd-largest pure-product in corpus** — 184,043 stars (chỉ sau n8n v56 185,728 stars; build-your-own-x v8 491K là tutorial-aggregator outside-scope)
- **7th EXTREME-tier subject** — Pattern #69 strengthening
- **Multi-tier T1+T5 monorepo** — corpus-first explicit T1+T5 convergence
- **Pattern #45 Dual-Licensing UN-STALES** sau 35 wikis stale (corpus-rare event)
- **Pattern #72 PolyForm-Family-License UN-STALES với rename** sau 26 wikis stale
- **Both AGENTS.md AND CLAUDE.md present** = Pattern #22 strengthening
- **First disciplined-skip Storm Bear meta-entity** trong 41-streak history — Phase 0.9 STRICT amendment validation

## 3. Tier placement

**Primary T1 Assistant** (AutoGPT Platform = agent-building substrate)
**Secondary T5 Application** (Classic = standalone end-user agent application)

Multi-tier subject với primary classification T1 by recent center-of-gravity (Platform là center hiện tại).

## 4. Cài đặt / Installation

**VN:** AutoGPT có nhiều cách cài đặt tùy thành phần bạn muốn dùng:

**Option A — AutoGPT Platform (cloud-tier qua agpt.co):**
1. Tạo tài khoản ở [agpt.co](https://agpt.co) (paid commercial cloud-tier — tự đánh giá phù hợp với business case của bạn)
2. Dùng UI để build agents

**Option B — AutoGPT Platform self-host:**
1. Clone repo: `git clone https://github.com/Significant-Gravitas/AutoGPT.git`
2. `cd AutoGPT/autogpt_platform/`
3. Đọc kỹ `LICENSE` PolyForm-Shield trước khi deploy thương mại
4. Docker-based deploy (xem docs trong `autogpt_platform/`)

**Option C — AutoGPT Classic (standalone, MIT):**
1. Clone repo
2. `cd classic/`
3. Follow setup hướng dẫn trong `classic/README.md`
4. Cần Python 3.x + API keys cho LLM provider (OpenAI / Anthropic / etc.)

**Option D — AutoGPT Forge (build custom agent):**
1. Clone + `cd classic/forge/`
2. Dùng Forge SDK để xây custom agent dựa trên AutoGPT primitives

**EN:** AutoGPT has multiple install paths depending on which component you want:

- **agpt.co cloud-tier** (paid, evaluate business-fit for PolyForm-Shield restrictions)
- **autogpt_platform/ self-host** (Docker-based; PolyForm-Shield license — review for commercial-competition restrictions)
- **classic/ standalone** (Python; MIT license; original 2023 agent)
- **classic/forge/** (custom-agent SDK; MIT license)

## 5. Core usage pattern

**Agent loop paradigm** (AutoGPT pioneered this):
1. Define agent goal
2. Agent breaks goal into sub-tasks
3. Agent uses tools (web search / file ops / API calls / etc.) to execute sub-tasks
4. Agent uses memory store to track progress
5. Agent loops until goal achieved or stop condition

**Use cases (from README):**
- Generate viral video from trending Reddit topics → automated short-form production
- Analyze YouTube videos → extract impactful quotes for social media

## 6. Novel concepts / key architectural choices

1. **Multi-component monorepo with explicit tier divergence** — Platform (T1) + Classic (T5) + Forge (bridge) in same repo with different licenses
2. **Dual-licensing strategy** — license-as-tier-marker (MIT for community/ecosystem; PolyForm-Shield for commercializable platform)
3. **Agent Protocol standardization** (AI Engineer Foundation) — older + narrower than MCP
4. **First-mover authority WITHOUT lineage citation** — distinct from citation-supported (mattpocock) / personal-claim (cporter) / corporate-organizational (spec-kit) / pseudonymous-org (OpenSpec) authority modes
5. **Agent-loop + tool-use + memory-store paradigm** introduced to mass adoption (paradigm-ancestor for ~all subsequent autonomous-agent corpus subjects)

## 7. So với corpus frameworks khác / vs other corpus frameworks

| Framework | Tier | Stars | Methodology | License | Multi-tier? |
|---|---|---|---|---|---|
| **AutoGPT v59** | **T1+T5** | **184K** | None explicit | **MIT + PolyForm-Shield dual** | **YES (corpus-first)** |
| n8n v56 | T2 | 185K | None explicit | n8n-SUL | No (single-T2 + many integrations) |
| OpenSpec v58 | T1 | 45.8K | SDD | MIT | No |
| mattpocock v57 | T1 | 62K | XP/DDD/Pragmatic books | MIT | No |
| spec-kit v17 | T1 | smaller | SDD | OSI | No |
| Unsloth v23 | T5 | smaller | None | Apache + commercial dual | No |
| GitNexus v33 | T5 | smaller | None | PolyForm-Noncommercial | No |

**AutoGPT đặc trưng:** EXTREME-tier complexity + multi-tier monorepo + dual-license + community-viral foundational + 0 methodology lineage cited.

## 8. Ethical framing (supply-chain + license + viral history)

**VN:** AutoGPT là dự án có ý thức vận hành lớn — không phải dùng tự do mà không cân nhắc:

1. **PolyForm-Shield restriction:** Nếu bạn định build sản phẩm/dịch vụ cạnh tranh AutoGPT (ví dụ: agent-builder platform của riêng bạn) — license cấm. Nếu bạn dùng AutoGPT làm tool nội bộ hoặc cho client consulting (Scrum-coaching) — thường OK nhưng nên consult lawyer cho business case quan trọng.

2. **autogpt_platform/ vs classic/ license boundary:** Code trong `autogpt_platform/` PolyForm-Shield, code phần còn lại MIT. Nếu fork hoặc dùng từng phần, kiểm tra license đúng folder.

3. **Supply-chain awareness:** AutoGPT ở scale 185K stars + 8K commits + 3 năm operational + commercial org stewardship — supply-chain risk thấp hơn các project N=1 author abandoned.

4. **Viral history caveats:** AutoGPT năm 2023 lan truyền cực nhanh nhưng cũng có chỉ trích về reliability (autonomous-agent paradigm còn early). Phiên bản hiện tại đã trưởng thành nhưng vẫn ở "platform-beta" (latest release autogpt-platform-beta-v0.6.58).

**EN:** AutoGPT is a major project — use it thoughtfully:

1. PolyForm-Shield restricts competing-product creation (consult legal for important commercial use)
2. License boundary is folder-based (autogpt_platform/ = PolyForm-Shield; rest = MIT)
3. Supply-chain risk is LOW (185K-scale + commercial-org stewardship)
4. "Platform-beta" status — autonomous-agent paradigm has matured but still evolving

## 9. Storm Bear relevance (VN operator + Scrum coach fit)

**Pilot relevance: MEDIUM-LOW pending license-acceptability decision.**

**Tiềm năng / Potential:**
- Agent Builder cho automated sprint-metrics aggregation
- Forge SDK để build custom Scrum-agent
- Workflow Management cho team standup digest / retro automation

**Constraints:**
- PolyForm-Shield commercial-competition restriction (cần check business-model fit)
- Multi-component complexity cao (vs OpenSpec v58 single-CLI + mattpocock v57 skill-files = simpler để adopt)
- Self-host infra not currently available cho Storm Bear vault
- agpt.co cloud-tier paid evaluation needed

**Pilot ranking estimate:** **BELOW Top-5** (claude-hud + claude-howto + OpenSpec + mattpocock + n8n likely ahead).

**Recommendation:** Re-evaluate post-v60 mini-audit. Workshop concrete Scrum-coaching use-case before pilot decision.

## 10. 4-week learning roadmap

**Week 1 — Orient:**
- Read AutoGPT README + CLAUDE.md + AGENTS.md + LICENSE thoroughly
- Tạo agpt.co account và explore UI (no commitment)
- Đọc Forge docs để hiểu agent-loop paradigm

**Week 2 — Hands-on Classic (MIT, low-risk):**
- Clone + setup `classic/` standalone agent
- Run 1-2 use cases trong README (Reddit→video / YouTube→quotes)
- Observe agent-loop + tool-use + memory behavior

**Week 3 — Forge experimentation:**
- Build 1 custom Scrum-agent prototype với Forge SDK
- Use case: sprint-metrics-aggregation hoặc retro-summary
- License: MIT — không có ràng buộc

**Week 4 — License decision:**
- Quyết định Storm Bear vault có triển khai autogpt_platform/ không (PolyForm-Shield restriction + business-fit)
- Workshop với client/team về Scrum-coaching fit
- Output: GO/NO-GO decision + roadmap nếu GO

## 11. Tradeoffs + limitations

**Pros:**
- Largest community + most-mature autonomous-agent framework in corpus
- Multi-component flexibility (platform / standalone / SDK)
- Active development + commercial-org stewardship (low abandonment risk)
- Foundational paradigm understanding ("AutoGPT-style agent loop")

**Cons:**
- EXTREME complexity (vs simpler corpus alternatives)
- PolyForm-Shield license requires explicit business-model check
- "Platform-beta" status (not fully production-stable for paid-platform users)
- Self-host infra requirement (vs OpenSpec/mattpocock simple-CLI install)
- NO methodology lineage citation (less educational scaffolding than mattpocock v57)

## 12. Caveats + safety notes

1. **License-axis caveat:** Verify business-use fit cho PolyForm-Shield BEFORE deploying autogpt_platform/ commercially. MIT portions (Classic + Forge + sister projects) không có vấn đề này.

2. **Beta-version caveat:** Current Platform release `autogpt-platform-beta-v0.6.58` (April 2026) — beta marker. Watch release notes cho production-stability changes.

3. **Multi-component caveat:** Khi clone repo, identify rõ component bạn dùng (Platform vs Classic vs Forge) — license + complexity + use-case khác nhau.

4. **Supply-chain awareness:** Dependencies trong `autogpt_platform/` includes Python + TypeScript packages — review nếu deploy production critical.

5. **Storm Bear specific:** Don't pilot AutoGPT before completing license-acceptability decision tied to v27 HIGH bundle item #5 (vault license decision) per CLAUDE.md.

## 13. References + next action

**References:**
- Repo: https://github.com/Significant-Gravitas/AutoGPT
- Cloud platform: https://agpt.co
- Wiki entities: `02 Entities/` (4 files — Core / License-axis / Multi-component-EXTREME / Foundational-viral-historical)
- License precedents in corpus:
  - Unsloth v23 (Apache + commercial)
  - GitNexus v33 (PolyForm-Noncommercial)
  - omo v52 (SUL-1.0)
  - n8n v56 (n8n-SUL)
- Pattern Library impact: Patterns #45 + #72 UN-STALE + #29 sub-context N=4 + #19 + #27 + #69 + #22 strengthening

**Next actions for Storm Bear:**
1. **Don't pilot yet** — complete license-acceptability decision (v27 HIGH item #5) first
2. **Carry to v60 mini-audit:** Pattern #45 + #72 promotion-candidates + 12-item largest-mini-audit-projected agenda
3. **Workshop** concrete Scrum-coaching use-case for AutoGPT before pilot decision
4. **Verify** AutoGPT-as-cited-subject in corpus grep (Q4 — Pattern #57 BIDIRECTIONAL-ABSENCE confirmation)
