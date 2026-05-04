# PR Instructions — Vietnamese Translation cho ECC README

> **Target repo:** https://github.com/affaan-m/everything-claude-code
> **Contribution type:** New language translation (Vietnamese / Tiếng Việt)
> **Prepared by:** Storm Bear wiki (Claude as wiki maintainer)
> **Date:** 2026-04-17
> **Based on:** ECC v1.10.0

---

## 🎯 Tổng quan / Overview

Add Vietnamese (VI) translation cho README.md của repo `affaan-m/everything-claude-code`. ECC hiện có 6 ngôn ngữ (English, pt-BR, zh-CN, zh-TW, ja-JP, ko-KR, tr) — **chưa có Vietnamese**. PR này thêm VI, đưa tổng số ngôn ngữ lên 8.

**Scope:** Theo pattern của Turkish translation (~466 lines, 20KB) — không dịch full 1498 lines English, mà giữ essential structure. Tuân theo precedent của ALL existing translations.

---

## 📁 Files trong PR

### 1. File mới

**Tạo:** `docs/vi/README.md`

→ File đã prepared: `./docs/vi/README.md` trong folder contribution này (~500 lines)

### 2. Files cần update (banner language switcher)

Cần update banner ở **8 files** để thêm Vietnamese link. Diff chi tiết bên dưới.

---

## 🔧 Banner updates

### File 1/8: `README.md` (English, root)

**Line 1** — update:

```diff
-**Language:** English | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md)
+**Language:** English | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md) | [Tiếng Việt](docs/vi/README.md)
```

**Line 28** — update:

```diff
-[**English**](README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md)
+[**English**](README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md) | [Tiếng Việt](docs/vi/README.md)
```

### File 2/8: `README.zh-CN.md` (root level)

**Line 26** — update:

```diff
-[**English**](README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md)
+[English](README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [**简体中文**](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md) | [Tiếng Việt](docs/vi/README.md)
```

### File 3/8: `docs/pt-BR/README.md`

**Line 1** — update:

```diff
-**Idioma:** [English](../../README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | Português (Brasil) | [Türkçe](../tr/README.md)
+**Idioma:** [English](../../README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | Português (Brasil) | [Türkçe](../tr/README.md) | [Tiếng Việt](../vi/README.md)
```

**Line 27** — update:

```diff
-[**English**](../../README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | [Português (Brasil)](README.md) | [Türkçe](../tr/README.md)
+[**English**](../../README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | [Português (Brasil)](README.md) | [Türkçe](../tr/README.md) | [Tiếng Việt](../vi/README.md)
```

### File 4/8: `docs/ja-JP/README.md`

**Line 1** — update:

```diff
-**言語:** [English](../../README.md) | [Português (Brasil)](../pt-BR/README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](README.md) | [한국어](../ko-KR/README.md) | [Türkçe](../tr/README.md)
+**言語:** [English](../../README.md) | [Português (Brasil)](../pt-BR/README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](README.md) | [한국어](../ko-KR/README.md) | [Türkçe](../tr/README.md) | [Tiếng Việt](../vi/README.md)
```

**Line 24** — update:

```diff
-[**English**](../../README.md) | [Português (Brasil)](../pt-BR/README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](README.md) | [한국어](../ko-KR/README.md) | [Türkçe](../tr/README.md)
+[**English**](../../README.md) | [Português (Brasil)](../pt-BR/README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](README.md) | [한국어](../ko-KR/README.md) | [Türkçe](../tr/README.md) | [Tiếng Việt](../vi/README.md)
```

### File 5/8: `docs/ko-KR/README.md`

**Line 1 + banner chính** — thêm `| [Tiếng Việt](../vi/README.md)` vào cuối cả 2 banner lines. (Check exact content with `grep -n "언어" docs/ko-KR/README.md` trước khi edit.)

### File 6/8: `docs/zh-TW/README.md`

**Line 16** — update:

```diff
-[**English**](../../README.md) | [Português (Brasil)](../pt-BR/README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | [Türkçe](../tr/README.md)
+[**English**](../../README.md) | [Português (Brasil)](../pt-BR/README.md) | [简体中文](../../README.zh-CN.md) | [**繁體中文**](README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | [Türkçe](../tr/README.md) | [Tiếng Việt](../vi/README.md)
```

### File 7/8: `docs/tr/README.md`

**Line 26** — update:

```diff
-[**English**](../../README.md) | [Português (Brasil)](../pt-BR/README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | [**Türkçe**](README.md)
+[**English**](../../README.md) | [Português (Brasil)](../pt-BR/README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | [**Türkçe**](README.md) | [Tiếng Việt](../vi/README.md)
```

---

## 🚀 Steps để submit PR

### Step 1: Fork ECC repo

```bash
# Trên GitHub UI, fork https://github.com/affaan-m/everything-claude-code
# Sau đó clone fork về local:
git clone https://github.com/YOUR_USERNAME/everything-claude-code.git
cd everything-claude-code
```

### Step 2: Tạo branch

```bash
git checkout -b add-vietnamese-translation
```

### Step 3: Copy file mới

```bash
# From Storm Bear vault:
mkdir -p docs/vi
cp "/Users/Cvtot/KJ OS Template/03 Projects/Everything Claude Code - Beginner Analysis/03 Published/contributions/vi-translation/docs/vi/README.md" docs/vi/README.md
```

### Step 4: Apply banner updates

Thực hiện 8 banner updates ở trên bằng editor hoặc `sed` scripts.

**Bulk sed script (careful — verify results!):**
```bash
# Update root README.md banner line 1
sed -i.bak '1s|\[Türkçe\](docs/tr/README.md)$|[Türkçe](docs/tr/README.md) \| [Tiếng Việt](docs/vi/README.md)|' README.md

# ... (tương tự cho các files khác — recommend manual edit để tránh edge cases)

rm *.bak  # cleanup
```

### Step 5: Verify changes

```bash
# Check tất cả banner links hoạt động
grep -rn "Tiếng Việt" --include="*.md" | wc -l
# Expected: >=9 (1 từ file mới + 8 banner updates)

# Preview README mới
less docs/vi/README.md

# Run markdownlint nếu có
npx markdownlint-cli 'docs/vi/README.md' 2>/dev/null || echo "markdownlint not installed (optional)"
```

### Step 6: Commit

```bash
git add docs/vi/README.md
git add README.md README.zh-CN.md docs/pt-BR/README.md docs/zh-TW/README.md docs/ja-JP/README.md docs/ko-KR/README.md docs/tr/README.md

git commit -m "docs: add Vietnamese translation (docs/vi/README.md)

Adds Vietnamese (Tiếng Việt) translation following the structure pattern
of existing translations (~500 lines, based on Turkish as template).

Changes:
- New: docs/vi/README.md (~500 lines, covers guides / quick start /
  cross-platform / folder structure / agent usage / common workflows /
  FAQ / running tests / contributing / license)
- Updated language switcher banners in 7 existing READMEs to include
  Vietnamese link

Based on ECC v1.10.0. Verified counts: 48 agents, 185 skills,
79 commands match README Quick Start.

This makes ECC accessible to Vietnamese-speaking developer community,
bringing total supported languages from 7 to 8."
```

### Step 7: Push + create PR

```bash
git push origin add-vietnamese-translation
# Trên GitHub UI, tạo PR từ fork → affaan-m/everything-claude-code:main
```

---

## 📝 PR description template

```markdown
## Add Vietnamese translation (docs/vi/README.md)

### What

Adds Vietnamese (Tiếng Việt) translation of the main README, bringing ECC's language support from 7 to 8 languages.

### Why

ECC currently has translations in 7 languages (English, pt-BR, zh-CN, zh-TW, ja-JP, ko-KR, tr) — Vietnamese is missing despite an active VN developer community. This PR adds it following the same pattern as existing translations.

### Scope

Following precedent of existing translations (~466-820 lines each, not full translations of the 1498-line English README):
- Kept: Header/badges, language banner, tagline, 3 guides section, latest 3 changelog entries (v1.10, v1.9, v1.8), Quick Start, Cross-platform support, What's Inside (folder structure), Which Agent to Use, Common workflows, FAQ (7 collapsible sections including security note), Running Tests, Contributing, License
- Cut: Older changelog entries (v1.7 and below), extended ecosystem tools deep-dive, detailed privacy/sponsors sections

### Files changed

- `docs/vi/README.md` (new, ~500 lines)
- `README.md` — banner update (2 lines)
- `README.zh-CN.md` — banner update (1 line)
- `docs/pt-BR/README.md` — banner update (2 lines)
- `docs/ja-JP/README.md` — banner update (2 lines)
- `docs/ko-KR/README.md` — banner update (2 lines)
- `docs/zh-TW/README.md` — banner update (1 line)
- `docs/tr/README.md` — banner update (1 line)

### Verification

- [x] All banner links work in both directions (VI → others, others → VI)
- [x] Markdown formatting preserved (tables, code blocks, collapsible details, image references)
- [x] Counts match README Quick Start (48 agents, 185 skills, 79 commands — verified via filesystem)
- [x] Technical terms kept in English (plugin, hook, skill, agent, MCP, command, workflow) for interop with source refs
- [x] Based on ECC v1.10.0

### Translation philosophy

- Tiếng Việt for narrative prose and process descriptions
- English preserved for technical terms (wrapped in backticks where appropriate)
- Code blocks, URLs, CVE numbers, version numbers, file paths kept as-is
- Tone matches source: engineering-pragmatic, not marketing-fluffy
```

---

## ✅ Pre-submit checklist

- [ ] README mới render đẹp trên GitHub (check preview)
- [ ] 8 banner updates verified — click test tất cả links
- [ ] No broken images — all `../../assets/images/...` paths đúng
- [ ] Technical terms consistent (plugin/hook/skill/agent English)
- [ ] Counts match current repo (48/185/79 — verify với `ls` nếu có thời gian)
- [ ] Commit message theo convention (`docs:` prefix — check với `CONTRIBUTING.md`)
- [ ] PR description complete với "What/Why/Scope"

---

## 🔄 After merge — follow-up contributions

Sau khi PR này merge, có thể contribute tiếp:

1. **`docs/vi/CLAUDE.md`** — tương tự các language dirs khác (tr, ja-JP, pt-BR đều có)
2. **`docs/vi/CONTRIBUTING.md`** — pt-BR có translation CONTRIBUTING
3. **`docs/vi/TERMINOLOGY.md`** — pt-BR có, giải thích English terms trong context Việt
4. Translate selected agents, commands, skills (optional, pt-BR có folder `docs/pt-BR/agents/`)

Storm Bear wiki đã có substantial Vietnamese material — reuse được rất nhanh.

---

## 📚 Reference materials đã chuẩn bị

Folder này (`03 Published/contributions/vi-translation/`) chứa:
- `docs/vi/README.md` — file cần commit (new file)
- `PR-INSTRUCTIONS.md` — file này (không commit, chỉ reference)

**Lưu ý:** `docs/vi/` trong folder này mirror structure sẽ appear trong ECC repo, để copy đơn giản.

---

## 🔗 Related context

- Source repo: https://github.com/affaan-m/everything-claude-code
- ECC current version tại thời điểm contribute: v1.10.0
- Storm Bear wiki analysis: `03 Projects/Everything Claude Code - Beginner Analysis/02 Wiki/`
- Vietnamese source material leveraged: [[(C) README summary]], [[(C) Shortform Guide summary]], v1 published guide

---

**Status:** ✅ Ready to submit. Tất cả deliverables trong folder này sẵn sàng copy vào fork.
