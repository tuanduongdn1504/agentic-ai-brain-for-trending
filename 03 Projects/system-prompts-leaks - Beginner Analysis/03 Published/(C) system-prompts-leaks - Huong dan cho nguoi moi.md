# (C) system-prompts-and-models-of-ai-tools — Hướng dẫn cho người mới / Beginner's Guide

> **Repo:** [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) — 135.5K ⭐, 34K forks, GPL-3.0
> **Tagline:** *"FULL [31 AI tools]. System Prompts, Internal Tools & AI Models"*
> **Philosophy:** Prompt-leak-archive — curated extracts of commercial AI tool system prompts
> **Wiki:** `(C) index` — 21st LLM Wiki in Storm Bear corpus (**3rd outside-scope**)
> **Audience:** prompt engineers + security researchers + AI tool designers + pattern observers

---

## ⚠️⚠️ Read this FIRST — Ethical + legal gray zones / Vùng xám đạo đức & pháp lý

### 🇻🇳 Tiếng Việt

**Repo này có 4 vùng xám đạo đức + pháp lý:**

1. **Xuất xứ nội dung không rõ ràng** — prompts extracted from 31 proprietary commercial AI tools (Cursor, Devin, v0, etc.) by unknown methods (prompt injection / UI inspection / decompilation / insider leaks?). Tool authors did NOT consent.

2. **Giấy phép GPL-3.0 có hiệu lực pháp lý không chắc** — x1xhlol applied GPL-3.0 to content they don't own. Hoặc prompts uncopyrightable (→ GPL không có hiệu lực), hoặc copyright belongs to tool authors (→ x1xhlol không có quyền license).

3. **Tác giả giấu tên (pseudonymous)** — x1xhlol = lucknitelol = NotLucknite (same person, 3 handles). Không có accountability identity cho legal / commercial / community.

4. **Cấu trúc monetization perverse-incentive** — x1xhlol operates both repo (publicizes leaks) + **ZeroLeaks commercial security service** (sells mitigation). More published leaks → more ZeroLeaks business. Khác với responsible security disclosure norms.

**Recommendations cho Storm Bear Scrum coach operator:**
- ✅ Đọc cho pattern observation
- ✅ Archive trong Storm Bear corpus (this wiki purpose)
- ⚠️ KHÔNG public advocacy cho repo
- ⚠️ KHÔNG copy extracted prompts vào client products
- ❌ KHÔNG recommend ZeroLeaks service cho clients
- ❌ KHÔNG associate Storm Bear brand với leak-framing

### 🇬🇧 English

**This repo has 4 ethical + legal gray zones:**

1. **Content provenance unclear** — prompts extracted from 31 proprietary commercial AI tools without tool authors' consent; extraction methods not documented.

2. **GPL-3.0 license validity questionable** — x1xhlol applied GPL-3.0 to content they don't own. Either prompts are uncopyrightable (no force) or owned by original tool authors (x1xhlol cannot license).

3. **Pseudonymous author** — x1xhlol = lucknitelol = NotLucknite. No verifiable identity for accountability.

4. **Perverse-incentive monetization** — author operates both the leak-repo AND commercial security service (ZeroLeaks) that mitigates the concerns the repo creates. More leaks → more service demand.

**Recommendations for Storm Bear operator:**
- ✅ Read for pattern observation
- ✅ Archive in corpus (this wiki)
- ⚠️ NO public advocacy
- ⚠️ NO copying prompts into client work
- ❌ NO ZeroLeaks recommendations
- ❌ NO brand association with leak-framing

---

## Part 1 — Repo là gì? / What is this repo?

### 🇻🇳 Tiếng Việt

**system-prompts-and-models-of-ai-tools** là **archive of extracted system prompts** từ 31+ commercial AI tools. Tác giả pseudonymous **x1xhlol** curate content vào folder-per-tool structure. Monetization qua Patreon + Ko-fi + crypto donations (BTC/LTC/ETH) + **Solana token** (đầu tiên trong corpus).

**Điểm nổi bật:**
- **135.5K stars** (#2 trong corpus, sau build-your-own-x 491K outside-scope) — **fastest scale-growth ever in corpus** (10.4K stars/month)
- **34K forks** — LARGEST forks count in corpus
- **31 AI tools archived:** Cursor, Devin, v0, Windsurf, Claude Code, Copilot, Replit, Trae, Kiro, v.v.
- **GPL-3.0** — 2nd GPL in corpus (sau TrendRadar v19)
- **Pseudonymous solo author** — 1st in corpus
- **Crypto-donation-funded** — 1st crypto-token (Solana) in corpus
- **Commercial derivative:** ZeroLeaks security service by same author
- **Discord:** LeaksLab (explicit leak-framing)
- **Created March 2025** — 13 months old

### 🇬🇧 English

system-prompts-and-models-of-ai-tools is an archive of extracted system prompts from 31+ commercial AI tools. Pseudonymous solo author x1xhlol curates content in folder-per-tool structure. Monetized via Patreon + Ko-fi + crypto (BTC/LTC/ETH) + Solana token + ZeroLeaks commercial derivative.

---

## Part 2 — Corpus firsts at v21

| Signal | system-prompts-leaks | Corpus context |
|--------|-----------------------|----------------|
| **2nd largest scale** | 135.5K | Only behind build-your-own-x 491K |
| **Largest forks** | 34K | Broader corpus typically 1K-20K forks |
| **Fastest scale-growth** | 10.4K stars/month | Beats spec-kit 7.4K/month |
| **1st pseudonymous author** | x1xhlol aka lucknitelol aka NotLucknite | All prior wikis real-name / corporate / LLC |
| **1st crypto-token** | Solana | No prior tokens in corpus |
| **1st multi-channel crypto** | BTC+LTC+ETH+Solana+Patreon+Ko-fi | 6-channel donation novel |
| **1st prompt-leak-archive genre** | 31 commercial tool prompts | New outside-scope sub-type |
| **1st perverse-incentive monetization** | ZeroLeaks + repo same author | Novel structural pattern |
| **2nd GPL-3.0** | Content governance (vs TrendRadar tool governance) | Pattern #29 validation |
| **3rd outside-scope wiki** | Prompt-leak-archive | After build-your-own-x + fish-speech |
| **1st AVOID pilot-tier** | Brand-association risk | New operator-engagement tier |

---

## Part 3 — 31 AI tools archived

### 🇻🇳 Danh sách (theo category)

**Agentic IDE / Coding (20 tools):**
Amp, Augment Code, CodeBuddy, Comet Assistant, Cursor, Devin AI, Junie, Kiro, Leap.new, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, v0, Warp.dev, Windsurf, Xcode, Z.ai Code

**LLM Assistant (5 tools):**
Anthropic (Claude Code), Google, Manus, NotionAi, Perplexity

**Specialized (6 tools):**
Cluely, dia, Emergent, Lovable, Orchids.app, Poke

**Meta (1 folder):**
Open Source prompts

### 🇬🇧 Cross-Storm Bear overlap

5 of 31 tools have direct or adjacent Storm Bear wiki:
- **Anthropic / Claude Code** — ECC v1 wiki
- **Google** — gws v13 wiki (Workspace)
- **Trae** — adjacent via deer-flow v9 ByteDance
- **VSCode Agent** — adjacent via Microsoft ecosystem (ECC + spec-kit)
- **Replit** — referenced in multiple T1 wikis

**25 of 31 tools = potential Storm Bear expansion targets** (if brand-risk managed).

---

## Part 4 — Pseudonymous author x1xhlol

### 🇻🇳 Ba handle

- **x1xhlol** (GitHub primary)
- **lucknitelol** (Patreon + Ko-fi)
- **NotLucknite** (X / Twitter)

Same person, intentional anonymity. **1st pseudonymous author trong Storm Bear corpus.**

### 🇬🇧 Why pseudonymous (inferred)

Likely motivations:
1. Legal risk mitigation (prompts extraction gray zone)
2. Employment concerns (may work at company that would object)
3. Geographic/political (jurisdiction unknown)
4. Security research community norm (pseudonyms common)

### Implications

- Cannot verify expertise
- Cannot trace chain of custody for content
- Cannot negotiate commercial partnerships with known-entity
- Tool authors cannot serve cease-and-desist (only GitHub DMCA route)

---

## Part 5 — Monetization stack

### 🇻🇳 6 channels + commercial derivative

| # | Channel | Type |
|---|---------|------|
| 1 | Patreon (lucknitelol) | Recurring |
| 2 | Ko-fi (lucknitelol) | One-time tips |
| 3 | Bitcoin wallet | Crypto |
| 4 | Litecoin wallet | Crypto |
| 5 | Ethereum wallet | Crypto |
| 6 | **Solana token** | Tokenomics (NEW pattern) |
| 7 | **ZeroLeaks commercial service** | Derivative product |

### 🇬🇧 Pattern #37 candidate: Crypto-Donation-Funded Scale Path

First corpus evidence của **crypto-token + multi-channel donations** reaching 135K scale without VC/corporate/open-core. Alternative scale-path to institutional funding.

---

## Part 6 — ZeroLeaks perverse-incentive structure

### 🇻🇳 Cấu trúc conflict

```
x1xhlol operates:
├── system-prompts-leaks (OSS, 135K stars)
│   ↓ publishes extracted prompts
│   ↓ creates security concern
│   ↓ drives startup worry
│   ↓ funnels demand to
└── ZeroLeaks (commercial security service)
```

### 🇬🇧 Why it's perverse

- **Responsible security research:** disclose to vendor FIRST → wait for patch → publish
- **This structure:** publish immediately + sell mitigation
- **Incentive:** more leaks published → more ZeroLeaks business potential

**Pattern #40 candidate** — first documented in Storm Bear corpus.

---

## Part 7 — Pattern #20 solo-scale ceiling revision #3

### 🇻🇳 Lịch sử revision

| Version | Ceiling | Trigger |
|---------|---------|---------|
| v16 | ~30K (solo broad-local) | graphify |
| v18 | ~82.9K (solo viral) | agency-agents |
| **v21** | **~135K (solo aggregator + crypto + zeitgeist)** | **system-prompts-leaks** |

### 🇬🇧 v21 factor: content-genre zeitgeist

Khi content-genre is culturally-current (AI prompts 2025-2026), ceiling rises. Zeitgeist-timed aggregators can reach 100K+ in <2 years. Different from tool-framework pattern.

---

## Part 8 — Storm Bear relevance (VN operator)

### 🇻🇳 Đánh giá cho Scrum coach

**Relevance level:** 🔴 **AVOID** (new pilot tier introduced at v21).

**Signal points:**
- ❌ **Brand-association risk** — "leaks" framing incompatible với Storm Bear professional brand
- ❌ **Content-ownership unclear** — không thể confidently dùng extracted prompts
- ❌ **ZeroLeaks referral** — unclear operator entity, perverse-incentive concern
- ❌ **Pseudonymous partner** — accountability gap cho enterprise engagement
- ❌ **Legal exposure** — dùng content có thể vi phạm tool authors' rights
- ✅ **Pattern observation value** — wiki này đủ; không cần deeper engagement
- ✅ **Prompt engineering learning** — high educational value (read, don't redistribute)

### When engagement is OK

- **Academic study** — analyze patterns from archive
- **Personal learning** — understand how commercial tools design prompts
- **Pattern documentation** — this Storm Bear wiki serves that purpose
- **Security research** (with ethical framework) — disclose-first responsible research

### When engagement is NOT OK

- Public advocacy / recommendation
- Copying archived content into client work
- Recommending ZeroLeaks to clients
- Commercial derivative products using archived content
- Any use that creates liability for Storm Bear brand

### Scrum ceremony mapping

| Ceremony | Use case (observation-only) |
|----------|------------------------------|
| Retrospective | Pattern observation on how commercial tools prompt |
| Backlog refinement | Education on prompt engineering (not copy) |
| Sprint planning | N/A (not for direct use) |
| Demo | N/A (brand risk) |

---

## Part 9 — 2-week learning roadmap (observation-only)

### Week 1: Archive exploration

- Day 1-2: Browse 5-10 tool folders (Cursor, Devin, v0, Windsurf, Claude Code)
- Day 3-4: Identify common prompt patterns (role + capabilities + constraints + tools)
- Day 5-7: Note differences across tool categories (IDE vs assistant vs specialized)

### Week 2: Pattern analysis + stop

- Day 8-10: Identify novel elements in each prompt (emotion tags, safety rails, tool descriptions)
- Day 11-12: Document personal takeaways (notes only, not republish)
- Day 13-14: Decide — learn enough, move on. Don't sink more time given brand risk.

### After Week 2: STOP

Storm Bear operator should NOT spend more time on this repo. Pattern observation complete. Continued engagement = brand-association accumulation risk.

---

## Part 10 — Tradeoffs + limitations

### Strengths (for educational-observation purpose)

- ✅ **31 AI tools in one place** — broadest commercial-tool coverage
- ✅ **Longitudinal archive** — version tracking potential
- ✅ **Active maintenance** — regular updates
- ✅ **Pattern-discovery richness** — 5 new pattern candidates from single wiki
- ✅ **Educational value** — see how professional tools prompt-engineer

### Limitations + risks

- ❌ **Legal gray zone** — extraction provenance unclear
- ❌ **GPL-3.0 validity unclear** — license may be toothless
- ❌ **Pseudonymous author** — no accountability
- ❌ **Perverse-incentive monetization** — ZeroLeaks structural concern
- ❌ **No verification** — cannot confirm archived prompts are accurate
- ❌ **Version drift** — prompts update, archive may lag
- ❌ **Brand risk for operators** — "leaks" framing stigma

---

## Part 11 — Comparison with v20 fish-speech

Both v20 + v21 are outside-scope wikis with content/license concerns but structurally different:

| Axis | fish-speech v20 | system-prompts-leaks v21 |
|------|-----------------|---------------------------|
| Genre | Foundation model | Prompt-leak archive |
| License | Custom non-OSI (valid but restrictive) | GPL-3.0 (validity questionable) |
| Author | Corporate (39 AI INC) | Pseudonymous solo |
| Commercial block | Explicit (paid tier required) | Implicit (content-ownership) |
| Storm Bear risk | License blocker for commercial | Brand-association risk |
| Pattern candidates added | 5 (#31-35) | 5 (#36-40) |
| Pilot tier | LOW | **AVOID** (new tier) |

---

## Part 12 — References + next action

### Wiki pages

- [[(C) index]]
- [[(C) README + monetization + ZeroLeaks cluster summary]]
- [[(C) 31 AI tools archived cluster summary]]
- [[(C) Ethical + legal gray zones cluster summary]]
- [[(C) Prompt-Leak-Archive Genre + 31 AI Tools Coverage]]
- [[(C) Pseudonymous Solo + Crypto-Token Monetization]]
- [[(C) Ethical Gray Zone + Perverse-Incentive Pattern]]
- [[(C) Outside-Scope Sub-Types + Pattern 20 Revision 3 + Storm Bear]]

### Cross-wiki siblings

- Outside-scope precedents: build-your-own-x v8 (education) + fish-speech v20 (foundation model)
- Ethical-framing precedent: paperclip v14 (alignment-theory)
- Community-viral precedents (Pattern #27): agency-agents v18 + TrendRadar v19
- GPL-3.0 precedent (Pattern #29): TrendRadar v19

### Official

- Repo: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
- Discord: LeaksLab
- X: @NotLucknite
- Patreon: patreon.com/lucknitelol
- Ko-fi: ko-fi.com/lucknitelol
- Derivative: ZeroLeaks (commercial security service)

### 🎯 Suggested next action (Storm Bear)

**Primary 1:** Stop adding wikis. **Run Pattern Library audit.** Multi-trigger hit:
- 20 candidates (threshold 15)
- 5 wikis since last audit
- Ratio 1:1 approaching 2:1

**Primary 2:** Still recommend **running graphify on vault** (NOW 5 sessions overdue since v16).

**For this repo specifically:** 2-week observation-only roadmap above. Then STOP engagement.

---

**Wiki 21/21 — 3rd outside-scope wiki (prompt-leak-archive sub-type) + 5 new pattern candidates (#36-40) + Pattern #20 revision #3 (135K ceiling) + Pattern #29 N=2 GPL-3.0 validation + Pattern #27 promotion candidate at N=3 + first AVOID pilot-tier introduced. Routine `llm-wiki-routine-v2.md` 3rd execution. Ethical framing prominent (paperclip v14 + fish-speech v20 precedents). Storm Bear brand-association risk FLAGGED.**
