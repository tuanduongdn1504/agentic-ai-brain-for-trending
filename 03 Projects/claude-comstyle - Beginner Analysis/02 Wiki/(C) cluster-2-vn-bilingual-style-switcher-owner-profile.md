# (C) Cluster 2 — VN bilingual + style-switcher SKILL.md + owner profile

**Source**: [`README_VN.md`](https://github.com/bsquang/claude-comstyle/blob/main/README_VN.md) + embedded VN before/after examples within `README.md` + [`skills/style-switcher/SKILL.md`](https://github.com/bsquang/claude-comstyle/blob/main/skills/style-switcher/SKILL.md) + GitHub profile [bsquang](https://github.com/bsquang).

## Bilingual EN+VN coverage

The repository carries **two README versions side by side**:

- `README.md` — English primary; first line links to `README_VN.md` via `🌐 Language: English | [Tiếng Việt](README_VN.md)`
- `README_VN.md` — full Tiếng Việt translation

Additionally, **4 of the 13 style sections in the English README contain embedded VN before/after examples** within the same comparison table:

| Style | EN example | VN example (embedded) |
|---|---|---|
| 🪖 Military | "401 typically means..." → "Token expired. Middleware..." | *"Claude ơi tại sao API của tôi bị lỗi 401 hoài vậy"* → *"Token hết hạn. Middleware kiểm tra `exp` dùng `<` thay vì `<=`."* |
| 🪨 Caveman | "React re-renders occur..." → "New object ref each render..." | *"Component React của tôi bị re-render liên tục"* → *"Object mới mỗi lần render. Prop inline = ref mới = re-render. Bọc trong `useMemo`."* |
| 🔍 Reality Check | "Great work! Your README..." → "Summary table works..." | *"Tôi đang làm side project về prompt styles cho Claude, định đăng lên cộng đồng AI VN, bạn thấy có ổn không?"* → *"Format bảng + before/after hoạt động tốt → rủi ro thật: nội dung VN dễ bị lạc khỏi bản EN theo thời gian → verdict: ship, thêm ghi chú sync vào CONTRIBUTING."* |
| (others EN-only) | | |

The VN phrasing is **idiomatic Vietnamese**, not machine translation — including informal sentence-final particles ("ơi" / "hoài vậy"), code-switching ("re-render liên tục" mixing English tech term with Vietnamese function-word), and culturally-anchored phrasing ("cộng đồng AI VN" = "VN AI community"). This is **native-speaker fluency evidence** supporting Phase 0.9 (a) inference of VN-located author.

## CORPUS-FIRST observations on bilingual structure

1. **EN+VN bilingual at solo-VN-dev T1 scale** — direct sister to v82 huashu-design (EN+zh at solo-China-dev T1 scale) = N=2 bilingual-solo-Asian-dev cluster within v60+ window
2. **Embedded VN-examples-within-style-tables** = CORPUS-FIRST in v60+ window — prior bilingual subjects had separate locale READMEs but did NOT embed second-locale content within shared comparison tables
3. **3rd locale-side-by-side product surface** in v77→v82→v87 arc (v77 13-locale i18n + v82 EN+zh + v87 EN+VN-embedded) = i18n discipline growing across solo-Asian-dev T1 cluster

## The Reality Check VN example is meta — about THIS project

The Reality Check VN example is explicitly self-referential:

- User question: *"Tôi đang làm side project về prompt styles cho Claude, định đăng lên cộng đồng AI VN, bạn thấy có ổn không?"* ("I'm doing a side project about prompt styles for Claude, planning to post to the VN AI community, do you think it's OK?")
- Reality Check verdict: *"Format bảng + before/after hoạt động tốt → rủi ro thật: nội dung VN dễ bị lạc khỏi bản EN theo thời gian → verdict: ship, thêm ghi chú sync vào CONTRIBUTING."* ("Table + before/after format works well → real risk: VN content drifts out of sync with EN over time → verdict: ship, add sync note to CONTRIBUTING.")

This is **CORPUS-FIRST self-referential example using the product's own methodology on the product itself** — a recursive demonstration. The author publishes their own Reality Check verdict on the project inside the project. Library-vocab candidate "Self-Referential Methodology Demonstration".

It also constitutes **near-explicit author identification** as a VN community participant ("đăng lên cộng đồng AI VN") = additional Phase 0.9 (a) evidence.

## style-switcher SKILL.md — the only actual "skill" artifact

The repository's `/skills/style-switcher/SKILL.md` implements the `/style` command for Claude Code (and Cowork per README claim). Per README install instructions:

```
your-project/
└── .claude/
    └── skills/
        └── style-switcher/
            └── SKILL.md
```

Install steps (from README):

1. Copy `skills/style-switcher/SKILL.md` into `.claude/skills/style-switcher/` in your workspace
2. Restart Claude in that workspace — skill auto-loads

Usage:

```
/style          → shows the full menu
/style 1        → apply Military directly
/style feynman  → apply by name
/style 3 + terminal CLI  → Reality Check with plain text output
```

**3-mode addressing**: numeric (1-13) + name (case-insensitive) + composable-with-modifier (`+ terminal CLI`). CORPUS-FIRST 3-mode skill-command-addressing in v60+ window — prior skill `/<command>` invocations were either name-only (most cases) or single-mode.

## Pattern #84 84c.1 LIGHT-harness footprint

README states: *"Works with Claude Code and Cowork."* That's the entirety of explicit harness coverage. No multi-platform skill manifests, no `npx skills add` shorthand, no per-harness install variants.

This places v87 at the **LIGHT-end of Pattern #84 84c.1 sub-mechanism distribution**:

| Wiki | Harness count | Distribution density |
|---|---|---|
| v85 ui-ux-pro-max | **18 platforms** | CORPUS-RECORD high (`skill.json` formal manifest) |
| v83 open-design | 16 harnesses | prior-record |
| v75 impeccable | 14 harnesses | sub-mechanism layer |
| v76 agent-skills-standard | 10+ via CLI-generated | 84c.2 generation variant |
| v82 huashu-design | 6 harnesses | mid-window |
| v81 taste-skill | ~4 harnesses | mid-low |
| v84 image-blaster | 1 harness | LIGHT-end |
| **v87 claude-comstyle** | **2 harnesses (CC + Cowork)** | **LIGHT-end LOW; full-distribution observable from v87 floor to v85 ceiling** |

v87 contributes **full-distribution-observability evidence**: Pattern #84 84c.1 spans 2 → 18 harnesses at present, with the methodology layer (84c original) provider-agnostic-by-design intent observed at both extremes. The LIGHT-end is NOT a negative-evidence contrast for Pattern #84 84c.1 promotion — it's positive-evidence that the sub-mechanism applies across the full scale.

## Owner profile — bsquang

[GitHub profile](https://github.com/bsquang) (fetched 2026-05-22):

| Field | Value |
|---|---|
| Username | bsquang |
| Full name | Not visible |
| Location | Not visible (inferred VN per language evidence) |
| Bio | Not visible |
| Website | Not visible |
| Followers | 7 |
| Following | 0 |
| Total public repos | 3 |
| Achievements | YOLO + Pull Shark + Starstruck |
| Account creation | Not visible |

**Visible repos**:

1. **claude-comstyle** — 28★ — the subject of this wiki (prompt collection + style-switcher skill)
2. **naotab** — 40★ — JavaScript Chrome extension; bio *"A Chrome extension that turns your browser tabs into a personal knowledge base — save tabs with context, auto-tag with AI, and visualize connections as a network graph."*
3. (third repo not visible in profile snapshot)

**Profile interpretation**:

- **Small-solo profile**: 7 followers + 3 repos = micro-scale; matches Storm Bear's solo-developer archetype dimensionally
- **2-product mini-portfolio**: naotab (40★ knowledge-management browser extension) + claude-comstyle (28★ Claude prompt collection) = ~68 stars total across 2 products; both AI-adjacent (naotab uses AI for auto-tagging; claude-comstyle is Claude-specific); CORPUS-FIRST pattern of **VN-solo-dev with Chrome-extension sister product** in v60+ window — distinct from prior VN-solo profiles (v76 Hoang multi-product VN incl. standards bundle; v80 Duy single Windows RPA + marketing site; v85 nextlevelbuilder org with 11 repos)
- **Achievement signals**: Starstruck = ≥1 repo with 16+ stars (achieved via naotab + claude-comstyle); Pull Shark = ≥1 merged PR (modest activity signal); YOLO = ≥1 commit without PR (solo-dev signal)
- **Cross-product theme**: both products are *"AI-adjacent personal-tooling for individual developers"* — naotab augments browser knowledge work, claude-comstyle augments AI-conversation work; consistent product-vision at micro-scale

## Pattern #19 sub-mechanism candidate

**"VN-Solo-Dev-with-Chrome-Extension-Sister-Product"** PROVISIONAL N=1:

- bsquang: claude-comstyle (28★) + naotab Chrome extension (40★)
- Distinct from existing Pattern #19 sub-mechanisms 19a-19m and the v86-promoted 19n (VN-Located-AI-Skills-Indie-Organization at org-scale)
- N=1 at PROVISIONAL — at risk of joining the **10-PROVISIONAL-N=1 Pattern #19 graveyard already flagged for v90 CONSOLIDATION** per v86 audit (9 of 10 sub-mechanisms still at N=1)

**Disposition recommendation**: register as PROVISIONAL N=1 with explicit acknowledgment of Pattern #19 graveyard risk; v90 audit consolidation may absorb this candidate into a broader "solo-VN-dev with multi-product portfolio" sub-mechanism alongside other VN-solo candidates.

## Pattern #82 within-pattern strengthening

The README includes **13 explicit quantitative-marketing claims** (one per style, e.g. "65-75% fewer output tokens"). This is per-style claim density, not aggregate-claim density. Pattern #82 (quantitative-marketing) within-pattern strengthening at the **claim-per-product-unit** dimension — micro-scale subject achieves higher per-unit density than mega-scale subjects often do.

## Pattern #83 within-pattern strengthening

Each of the 13 styles carries an **explicit Pros / Cons + "Best for / Not suitable for" honest-disclosure**. That's **26 honest-disclosure-axis-instances** in the README (13 styles × 2 axes = Pros/Cons + Best-for/Not-suitable). Pattern #83 honest-deficiency-disclosure within-pattern strengthening at per-feature granularity — distinct from v67/v75/v82 honest-disclosure at product-level scope.

## What's missing — auditing the gaps

- **No measurement methodology**: % token-impact claims (65-75%, etc.) are stated without sample size, prompt corpus, or measurement protocol
- **No evals**: no script to verify the % savings hold across conversations
- **No version tags**: no release versions, no changelog
- **No multi-harness manifest**: only Claude Code + Cowork mentioned; broader compatibility unverified
- **No cross-language version of style prompts**: prompts themselves are English-only (the *examples* show VN; the *prompts* don't)
- **No telemetry / opt-in measurement**: no way to crowd-source % savings validation

These gaps are documented honestly via the per-style Pros/Cons (Pattern #83 within-pattern), but the gap-disclosure operates at the per-style scope, not project-scope. v87 = honest-disclosure at style-granularity-only.
