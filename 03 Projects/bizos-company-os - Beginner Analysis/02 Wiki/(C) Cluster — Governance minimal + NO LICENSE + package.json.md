# (C) Cluster — Governance minimal + NO LICENSE + package.json

**Sources:** `AGENTS.md` (327B) + `CLAUDE.md` (11B) + `.claude/launch.json` (183B) + `package.json` (948B) + absent governance files + absent LICENSE file

## 1. AGENTS.md verbatim (5 lines, 327 bytes)

```markdown
<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->
```

**Analysis:**
- Single purpose: instruct AI coding agents that Next.js 16 breaks training-data assumptions
- Points at `node_modules/next/dist/docs/` (Next 16 ships docs inside npm package — corpus-first observation)
- Zero other governance content — no contribution gate, no style guide, no commit convention, no agent roster
- **Smallest AGENTS.md in corpus** by ~2 orders of magnitude (pi-mono v36 AGENTS.md = 182 lines; most corpus AGENTS.md files are 50-500 lines)

**Pattern #22 AGENTS.md industry standard strengthening:**
- Confirmed convention now extends to outside-scope business-application tier (previously observed at T1/T4/T5)
- Documents a **minimum-viable-AGENTS.md sub-variant** (327B for single-framework-version-warning)
- Contrast spectrum: pi-mono v36 maximum (182 lines, comprehensive governance) ↔ bizos v37 minimum (5 lines, single warning)
- Observation: AGENTS.md convention survives even when framework chooses "just warn about one thing" posture

## 2. CLAUDE.md verbatim (1 line, 11 bytes)

```
@AGENTS.md
```

**Analysis:**
- One-line aliasing pointer — CLAUDE.md delegates to AGENTS.md
- Pattern observed previously at gws v13 (tri-file agent docs: CLAUDE 1-liner + AGENTS 209-line + CONTEXT.md runtime)
- Bizos variant: CLAUDE 1-liner + AGENTS 5-line → **dual-file minimum** (no CONTEXT.md)
- Establishes "CLAUDE.md = AGENTS.md" convention at minimum-scale: when you only have one governance message, write it once in AGENTS.md and alias CLAUDE.md to it

## 3. `.claude/launch.json` (183 bytes)

```json
<183 bytes of Claude Code harness config — likely dev environment launch settings>
```

- Presence of `.claude/` folder with `launch.json` = strong signal that **Claude Code was used to build this project**
- Combined with:
  - AGENTS.md framework-warning pattern (typical AI-coding-agent hint)
  - 800-line bilingual /guide page (AI-generated documentation signal)
  - 64-table schema with consistent naming + triggers
  - 626-entry i18n dict
- → Inference (not verified): bizos-company-os is largely Claude-Code-built
- Cross-wiki: first corpus wiki where subject appears to be AI-coding-assistant-built product (meta: corpus wikis are ABOUT Claude Code; this subject was BUILT WITH Claude Code)

## 4. package.json dependencies (17 runtime + 8 dev)

**Runtime:**
- `next` 16.2.4 (first corpus repo using Next 16 stable) + `react` 19.2.4 + `react-dom` 19.2.4
- `@supabase/ssr` 0.10.2 + `@supabase/supabase-js` 2.104.1 (server-component-ready auth)
- `@tanstack/react-table` 8.21.3 (table primitive)
- `reactflow` 11.11.4 (org chart + KPI tree visualization)
- `recharts` 3.8.1 (charts: line/bar/donut/sparkline)
- `react-hook-form` 7.73.1 + `@hookform/resolvers` 5.2.2 + `zod` 4.3.6 (form stack)
- `lucide-react` 1.8.0 (icon library)
- `class-variance-authority` + `clsx` + `tailwind-merge` (shadcn-style component variants)
- `date-fns` 4.1.0

**Dev:**
- `@tailwindcss/postcss` v4 + `tailwindcss` v4
- `@types/node` 25.6.0 + `@types/react` 19
- `eslint` 9 + `eslint-config-next` 16.2.4
- `typescript` 5

**Name:** `company-os` (not `bizos` — package-vs-branding divergence noted; Pattern #58 Branding-Package Divergence relevance, currently CANDIDATE)

**Version:** `0.1.0` — pre-release posture matches cold-start status

**Scripts:** `next dev` / `next build` / `next start` / `eslint` — minimal, no test script, no custom deploy

## 5. Absent governance files (corpus-first enumeration)

**NOT present:**
- ❌ LICENSE (most significant absence — see §7 below)
- ❌ CONTRIBUTING.md
- ❌ SECURITY.md
- ❌ CODE_OF_CONDUCT.md
- ❌ MAINTAINERS.md
- ❌ SUPPORT.md
- ❌ TESTING.md / RELEASING.md
- ❌ `.github/` workflows directory (no CI visible)
- ❌ `.github/ISSUE_TEMPLATE/` or `PULL_REQUEST_TEMPLATE.md`
- ❌ test files anywhere in repo

**Present:**
- ✅ AGENTS.md (327B, Next.js warning only)
- ✅ CLAUDE.md (11B pointer)
- ✅ README.md (10.3K)
- ✅ .claude/launch.json (183B)
- ✅ .dockerignore / .gitignore / .vercelignore
- ✅ Dockerfile / vercel.json / railway.json (deploy configs)
- ✅ eslint.config.mjs / next.config.ts / postcss.config.mjs / tsconfig.json (tooling configs)
- ✅ pnpm-lock.yaml / pnpm-workspace.yaml

**Total governance file count: 2 (AGENTS.md + CLAUDE.md)** — **lowest in corpus outside of v8 build-your-own-x and v21 system-prompts-leaks aggregator genre wikis**.

**Corpus comparison:**
| Wiki | AGENTS.md | CLAUDE.md | CONTRIBUTING | SECURITY | COC | LICENSE | Total |
|------|-----------|-----------|--------------|----------|-----|---------|-------|
| spec-kit v17 (T1 corporate) | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 6 |
| pi-mono v36 (T1 solo) | ✅ 182L | ❌ | ✅ | ❌ | ❌ | ✅ MIT | 4 |
| claude-hud v35 (T1 solo) | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ MIT | 7 files |
| codymaster v12 (T1 VN) | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ ISC | 2 |
| bizos v37 (outside-scope VN) | ✅ 327B | ✅ 11B | ❌ | ❌ | ❌ | ❌ none | 2 + NO LICENSE |

## 6. Pattern #12 Governance-Depth refinement candidate (N=1 cross-tier observation)

- Bizos = solo + cold-start (2 days) + outside-scope → **2 governance files total**
- Earlier observation (v35 claude-hud): solo + cold-start (3 months) + T1 → **7 governance files** (counter-evidence to #12)
- Pattern #12 currently: governance-depth correlates with organization-size
- v35 counter-evidence noted but N=1 at time
- v37 bizos reinforces #12 ORIGINAL formulation: solo + cold-start + outside-scope = minimum governance, CONSISTENT with #12
- Observation: claude-hud v35 was the OUTLIER (heavy governance at solo-3-month-cold-start); bizos v37 is the **baseline case** (minimum governance at solo-2-day-cold-start)
- **Strengthens #12 at 2 observations across 2 tiers** (T1 claude-hud counter-evidence + outside-scope bizos baseline). No formulation change.

## 7. NO LICENSE file — corpus-first analysis

**Factual state:**
- No `LICENSE`, `LICENSE.md`, `LICENSE.txt`, or `COPYING` file in repo
- GitHub UI renders as "No license" in sidebar
- README.md §License says: "Proprietary — Alex Le · Titan Labs. Xem code thoải mái, fork để học. Deploy production / tuỳ biến cho công ty → email alexle@titanlabs.vn."
- package.json has no `license` field

**Legal implications (US + international default):**
- Absent LICENSE file → default copyright → **all rights reserved**
- Viewers have implicit right to view code on GitHub (per GitHub ToS implicit license to display publicly-pushed content)
- Viewers DO NOT have right to:
  - Fork privately (though GitHub fork is permitted by ToS for transient use)
  - Copy code into another project
  - Deploy a derived version (even privately)
  - Use commercially (with or without modification)
- README statement "fork to learn" is **goodwill declaration, not legal license** — README != LICENSE
- Contact-email gate ("email alexle@titanlabs.vn for production deploy / custom") = commercial-gate channel

**Corpus context:**
- **Pattern #29 License-Category-Diversity (confirmed)** — previously documented categories: Permissive-OSI (MIT / Apache / ISC) + Copyleft (GPL / AGPL) + Non-OSI (PolyForm Noncommercial / Fish Audio Research License / custom Fish)
- **Bizos contributes NEW category: absent-LICENSE / proprietary-by-default** — this is structurally distinct from "custom non-OSI" because custom non-OSI still has a written license document
- **New sub-category:** "proprietary-by-default via absent LICENSE + README-declared proprietary statement"
- This is a **strengthening observation** of Pattern #29 (adds new sub-category diversity), not a new candidate

**Ethical surface:**
- ⚠️ Users attempting to fork/deploy/modify without email contact = legal gray zone
- Clone for local learning = de facto tolerated by README
- Any production use without written permission from Alex Le = copyright infringement risk
- Beginner guide must include ⚠️ prominent section explaining this (precedent: system-prompts-leaks v21 ethical framing)

## 8. Deploy configs (4 surfaces)

**`Dockerfile`** (38 lines, multi-stage):
- Base: `node:22-alpine` + `corepack enable && corepack prepare pnpm@10 --activate`
- Stage 1 `deps`: `pnpm install --frozen-lockfile`
- Stage 2 `builder`: accepts build-args for `NEXT_PUBLIC_SUPABASE_URL` + `NEXT_PUBLIC_SUPABASE_ANON_KEY` + `NEXT_PUBLIC_APP_URL` + `pnpm run build`
- Stage 3 `runner`: runs as non-root `app:app` user + `next start -p 3000`
- Exposes port 3000

**`vercel.json`** (224 bytes) — Vercel deploy config with env-var mapping

**`railway.json`** (369 bytes) — Railway deploy config (likely Nixpacks or Dockerfile path hint)

**`proxy.ts`** (root, 325 bytes) — Next 16 middleware renamed to proxy; calls `updateSession` from `@/lib/supabase/proxy`; matcher excludes `_next/static`, `_next/image`, favicons, images

**Healthcheck:** `/api/health` (referenced in README, not inspected; likely standard GET returning 200)

**Observation:** 4 deploy surfaces (Vercel / Railway / Docker / local pnpm dev) with Supabase as backend-service — standard Next.js + Supabase deployment topology, no novel architecture.

## 9. Lost opportunity flags (minor)

- Could benefit from minimum LICENSE (even "All rights reserved" as formal text file would be clearer legally than absent)
- CONTRIBUTING.md would help the 25 forks know whether PRs are welcomed
- SECURITY.md trivial at this scale but signals production-grade posture
- No `.env.example` file visible (README references it but not present in repo top-level)

## 10. Key phrases (verbatim VN)

- "Xem code thoải mái, fork để học" (view code freely, fork to learn)
- "Deploy production / tuỳ biến cho công ty → email alexle@titanlabs.vn" (production deploy / customize for company → email)
- "Không có env → tự bật **Demo mode**" (no env → auto-enables Demo mode)
- "Đổi 1 KPI lá ở **Forecast** sẽ thấy tác động lên Net Profit ngay lập tức" (change 1 leaf KPI at Forecast → see Net Profit impact immediately)

## 11. Cross-wiki echo

- v13 gws: tri-file agent docs precedent (CLAUDE 1-line + AGENTS 209L + CONTEXT.md); bizos = dual-file minimum variant
- v22 AGENTS.md industry standard (confirmed): bizos extends to outside-scope tier at minimum surface (327B)
- v29 License-Category-Diversity (confirmed): bizos introduces absent-LICENSE sub-category as 4th structural variant
- v21 system-prompts-leaks: ethical framing precedent for "legally gray zone"
- v35 claude-hud: counter-evidence pair for Pattern #12 governance-depth correlation (claude-hud = heavy/small; bizos = light/small)
