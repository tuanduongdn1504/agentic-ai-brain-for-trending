# awesome-design-md — Hướng dẫn cho người mới / Beginner Guide

> **Dành cho:** Developer dùng Claude Code / Cursor / Stitch / Lovable muốn generate UI matching brand design systems mà không phải viết design spec từ đầu.
> **Scope note:** Đây là content aggregator (không phải code framework). Drop-in DESIGN.md files, AI agent generates UI.

---

## 0. Đọc trước khi đi tiếp / Read this first

**VN:** awesome-design-md là bộ sưu tập 69 file DESIGN.md mô tả design system của các brand nổi tiếng (Stripe, Airbnb, Tesla, Claude, v.v.). Thiết kế cho:

- Developer dùng AI coding agents (Claude Code, Cursor, Google Stitch, Lovable)
- Muốn generate landing page / UI **matching 1 brand cụ thể** nhanh
- Không muốn tự viết design spec từ đầu

**Nếu bạn:**
- Không dùng AI coding agents → không cần tool này
- Có design team riêng → có thể tham khảo nhưng không cần
- Làm Scrum coaching / không build UI → observational value only

**EN:** Collection of 69 DESIGN.md files for AI coding agents to generate UI matching popular brand design systems. Drop-in files → AI builds matching UI.

## 1. Concept — DESIGN.md là gì?

**VN:** **DESIGN.md** = file markdown mô tả design system đủ chi tiết cho AI agent generate UI matching. Concept do **Google Stitch** (Google design-to-code AI tool) pioneer.

### 9 sections trong DESIGN.md spec:

1. **Color** — palette + tokens
2. **Typography** — fonts + scale + weights
3. **Components** — button / input / card / modal patterns
4. **Layout** — grid / spacing / breakpoints
5. **Depth** — shadow / elevation / layering
6. **Patterns** — hero / testimonial / pricing patterns
7. **Responsive** — breakpoint behavior
8. **Agent prompts** — instructions cho AI
9. (implicit) aesthetic character via descriptive language

**EN:** DESIGN.md = markdown spec for AI agents to generate UI matching a design system. Pioneered by Google Stitch. 9 standardized sections.

## 2. Cấu trúc repo — per-site 3-file bundle

```
awesome-design-md/
├── stripe/
│   ├── DESIGN.md           # The spec (copy this)
│   ├── preview.html        # Light mode reference
│   └── preview-dark.html   # Dark mode reference
├── airbnb/
│   ├── DESIGN.md
│   ├── preview.html
│   └── preview-dark.html
├── ... (69 design systems total)
```

## 3. Usage — 3 bước

### Bước 1 — Copy DESIGN.md

```bash
# Clone repo hoặc browse getdesign.md
git clone https://github.com/VoltAgent/awesome-design-md.git

# Copy design bạn muốn
cp awesome-design-md/stripe/DESIGN.md ./my-project/
```

### Bước 2 — Tell AI agent

Trong Claude Code / Cursor:

```
"Use the DESIGN.md in this project root. 
Build me a landing page for a SaaS product that sells fintech API."
```

AI agent đọc DESIGN.md → generate UI matching Stripe brand feel.

### Bước 3 — Verify via preview.html

```bash
open awesome-design-md/stripe/preview.html
```

Check if generated UI matches reference preview.

## 4. 69 design systems — 10 categories

| Category | Examples |
|----------|----------|
| **AI/LLM platforms** | Claude, Cohere, ElevenLabs, Mistral |
| **Developer tools** | Cursor, Vercel, Raycast, Warp |
| **Database/DevOps** | MongoDB, Supabase, PostHog |
| **Fintech/Crypto** | Stripe, Coinbase, Wise |
| **E-commerce** | Airbnb, Nike, Shopify |
| **Automotive** | Tesla, Ferrari, BMW |
| **Other categories** | 4 more (browse getdesign.md for full list) |

## 5. Compatible AI tools

| Tool | Support |
|------|---------|
| **Claude Code** | ✅ Explicit |
| **Cursor** | ✅ Explicit |
| **Google Stitch** | ✅ Native (methodology origin) |
| **Lovable** | ✅ Explicit |
| Any markdown-reading LLM | ✅ Implicit |

## 6. Khi nào bạn cần

### ✅ Dùng khi:

- Prototype landing page nhanh (15 phút → have UI matching Stripe-style)
- Learning: reverse-engineer how brand design translates to markdown spec
- Greenfield project: establish design DNA from day 1
- Client want UI "like Airbnb's": have reference spec

### ❌ KHÔNG dùng khi:

- Có design team riêng producing custom specs
- Unique brand identity (not matching any famous brand)
- Don't use AI coding agents
- Scrum coaching / non-UI work

## 7. Viral context — 60K stars in 20 days

**Fun fact:** awesome-design-md hit 60,585 stars trong 20 ngày đầu (2026-03-31 → 2026-04-20) = ~3,000 stars/day = **fastest viral velocity** trong corpus Storm Bear (9× system-prompts-leaks v21).

**Why viral:**
- Immediate utility (copy-paste → UI)
- Broad audience (millions of Claude Code / Cursor users)
- Shareable concept ("get UI matching Stripe in 1 command")
- Vibe-coding zeitgeist peak 2025-2026
- Visual payoff (preview.html immediately impressive)
- Google Stitch validation (Google product = credibility)

## 8. Vibe-design philosophy

awesome-design-md explicitly embraces **vibe-design**:
- "warm terracotta" / "void-black canvas" / "cinematic dark UI"
- Aesthetic-first descriptive language
- AI agents interpret vibe + match

**Contrast với spec-kit v17** (GitHub/Microsoft SDD framework):
- spec-kit: *"focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch"* (anti-vibe)
- awesome-design-md: embraces vibe (pro-vibe)

**First corpus explicit pair** vibe-pro vs vibe-anti.

## 9. Contribution

### How to add new DESIGN.md

1. **Open issue** — discuss với maintainers
2. **PR approved** — add DESIGN.md + preview.html + preview-dark.html
3. **Improvements** — fix colors, tokens, descriptions

### Community

- Discord community
- GitHub issues
- Sponsorship via getdesign.md

## 10. VoltAgent ecosystem context

**VoltAgent** = commercial startup with 3 layers:
- **VoltAgent/voltagent** — TypeScript AI agent framework (parent product)
- **VoltAgent/awesome-design-md** — this aggregator (community amplifier)
- **getdesign.md** — commercial companion platform (sponsorship monetization)

**Strategic:** aggregator virality drives attention to parent framework + commercial platform.

## 11. Lộ trình — tried in 1 hour / 1-hour test drive

### 15 phút — orient

- [ ] Clone repo hoặc browse getdesign.md
- [ ] Pick 1 design system (VD: Stripe)
- [ ] Copy DESIGN.md sang test project
- [ ] Open preview.html reference

### 30 phút — generate first UI

- [ ] Open Claude Code / Cursor trong project
- [ ] Prompt: "Use DESIGN.md, build me a SaaS landing page"
- [ ] Compare result với preview.html
- [ ] Iterate on agent prompt if needed

### 15 phút — evaluate

- [ ] Was result "pixel-perfect"? (Usually 70-80%)
- [ ] Time saved vs writing spec from scratch?
- [ ] Worth integrating into workflow?

## 12. Storm Bear operator relevance

**VN:** Storm Bear operator (Scrum coach + developer):

**Direct adoption: LOW** — không build UI trong vault / Scrum work.

**Observational value: HIGH:**

1. **Ecosystem-layer playbook** — VoltAgent strategy (framework + aggregator + platform) là model cho nếu Storm Bear commercialize
2. **Commercial-funnel model** — getdesign.md sponsorship = alternative to open-core
3. **Viral dynamics** — content-aggregator genre has proven 3K stars/day reach
4. **Vibe-spec spectrum** — axis Storm Bear can position on when publishing content
5. **Methodology-lineage** — Google Stitch DESIGN.md spec = example of design-system methodology (Pattern #19 archetype 2 broadening)

**Hypothetical Storm Bear content aggregator** (pure speculation):
- `awesome-scrum-templates` — retrospective formats, standup structures
- `awesome-ai-coaching-prompts` — Scrum coaching prompt library
- Could tap awesome-list-genre virality

## 13. Next actions

**Nếu bạn là developer dùng AI coding agents:**
1. Browse getdesign.md → pick 1 design system relevant to your project
2. 1-hour test drive (section 11 above)
3. Decide: integrate into workflow / stick with current approach

**Nếu bạn là Storm Bear operator:**
1. Wiki này = pattern library asset, không phải adoption roadmap
2. Note ecosystem-layer playbook (Pattern #17) for future reference
3. Consider hypothetical Scrum content aggregator if/when publishing

**Nếu bạn build content library / aggregator:**
1. Study VoltAgent's 3-layer strategy
2. Study viral dynamics (immediate utility + shareable + visual payoff)
3. Consider getdesign.md-style companion platform

## 14. References

- GitHub: github.com/VoltAgent/awesome-design-md
- Platform: getdesign.md
- Parent: github.com/VoltAgent/voltagent
- Google Stitch: Google's design-to-code AI tool
- Compatible: Claude Code, Cursor, Google Stitch, Lovable
- License: MIT

---

**awesome-design-md = 69 DESIGN.md files for AI agents to generate UI matching brand design systems. 9-section spec pioneered by Google Stitch. 60K stars in 20 days (fastest viral velocity in corpus). Compatible with Claude Code + Cursor + Stitch + Lovable. Storm Bear: observational value (ecosystem-layer playbook + vibe-spec axis), not direct adoption.**
