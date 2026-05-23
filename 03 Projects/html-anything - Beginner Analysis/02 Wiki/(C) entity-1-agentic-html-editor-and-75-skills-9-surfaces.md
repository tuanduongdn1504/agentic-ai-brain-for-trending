# (C) Entity 1 — Core Product: Agentic HTML Editor + 75 Skills × 9 Surfaces + 8-Agent CLI Detection + Zero-API-Key Reuse-of-Logged-In-Session + Sandboxed-Iframe Preview + 5-Rule Hard-Constraint Template Discipline + Multi-Surface Export Toolchain

**Type**: Core-product entity
**Wiki version**: v91 (SECOND under routine v2.3 baseline)
**Sources**: cluster-1 (README + repo metadata), cluster-2 (nexu-io org context)

---

## Definition

`html-anything` is a **local-first agentic HTML editor** that converts markdown drafts into shipped HTML across 9 deliverable surfaces (magazine + deck + résumé + poster + Xiaohongshu/Tweet cards + web prototype + data report + Hyperframes video), powered by 75 composable skill templates, with **8-agent CLI ecosystem detection** (Claude Code + Codex + Cursor + Gemini + Copilot + OpenCode + Qwen + Aider) and **zero-API-key dependency via reuse-of-logged-in-agent-session paradigm**, rendered via **SSE streaming + sandboxed iframe preview** with **5-rule hard-constraint template discipline** (CJK-first font + 8px grid + contrast ≥ 4.5:1 + no pure black/white + no lorem ipsum), exported to WeChat (juice-inlined CSS) / X+Weibo+Xiaohongshu (PNG) / Zhihu (LaTeX placeholders) / standalone HTML / High-DPI PNG.

## Why this is a single entity (not 4)

The 75-skill × 9-surface × 8-agent matrix is **deliberately packaged as a single product** under one repository + one monorepo workspace + one homepage URL. The skill registry, agent-detection, SSE streaming, sandboxed-preview, and export-toolchain layers all operate on a **single shared substrate** (the Next.js app at `next/` with monorepo workspace `@html-anything/next`). Treating them as separate entities would lose the **single-product agentic-editor identity** which is the load-bearing structural property.

This is structurally distinct from v83 open-design's 31-skill-with-3-vector-corpus-recursive-citation density (v83 was multi-tier-corpus-recursive at single subject) and from v90's 4-nested-versioned-sub-skill-with-orchestrator architecture (v90 was nested-with-orchestrator). v91 is **single-product-multi-surface-output** at a distinct structural point.

## Architecture details

### 75-skill registry × 9-surface output × 8-agent CLI matrix

| Dimension | Count | Detail |
|---|---|---|
| Skills | 75 composable templates | LDS density mid-range; below v85 669+ and v76 259-skill records |
| Surfaces | 9 deliverable types | Multi-modal output: text-articles + slide-decks + résumés + posters + 2 social-card formats + interactive-prototypes + data-charts + frame-scripts-video |
| Agents | 8 CLI binaries | Claude Code + Codex + Cursor + Gemini + Copilot + OpenCode + Qwen + Aider; auto-detected by binary presence |
| Export targets | 5 (with sub-variants) | WeChat juice-inlined CSS / X-Weibo-Xiaohongshu PNG / Zhihu LaTeX-placeholders / standalone HTML / High-DPI PNG |

### Zero-API-key paradigm

The product invokes the **local CLI binary** of whichever supported agent is installed on the user's machine. Credentials never touch html-anything code. The local agent reuses its own session — already-logged-in user → no key handling in html-anything.

This avoids:
- BYOK credential management (typical Pattern #66 supply-chain dependency)
- OAuth flow (v67 opencode-antigravity-auth T4b Credential-Bridge sub-archetype style)
- Self-hosted model substrate (T5 Application typical pattern)

Mechanism: html-anything detects which CLI is available → invokes it via subprocess → captures streaming output → renders to iframe preview. The CLI handles its own authentication state.

### SSE streaming render

Server-Sent Events stream the agent's HTML output **as it's being written**, line-by-line, into the sandboxed iframe preview. UX-pattern observation: real-time visualization of agent thinking + immediate visibility of issues.

### Sandboxed iframe preview

`<iframe sandbox="allow-scripts allow-same-origin">` with cookie-quarantine from parent context. Allows in-template JavaScript (for interactive prototypes + chart rendering + Hyperframes) while preventing cross-context cookie leakage. CORPUS-FIRST explicit sandbox-discipline at agentic-editor-preview-layer in v60+ window.

### 5-rule hard-constraint template discipline

Encoded into every template (not aspirational README text):

1. **CJK-first font stack**: Noto Sans/Serif SC + Inter + Manrope (Simplified-Chinese-first ordering)
2. **8 px baseline grid**: vertical rhythm constraint
3. **Contrast ≥ 4.5:1**: WCAG AA accessibility
4. **No pure black/white**: softer-palette discipline
5. **No lorem ipsum**: must use real user data

CORPUS-FIRST 5-rule hard-constraint template discipline at agentic-HTML-editor layer.

### Multi-surface export toolchain

| Export target | Library | Mechanism |
|---|---|---|
| WeChat | juice | CSS-inlining (WeChat strips external stylesheets) |
| X / Weibo / Xiaohongshu | modern-screenshot | PNG via DOM-to-canvas-to-PNG |
| Zhihu | (custom) | HTML with LaTeX placeholders (Zhihu native LaTeX) |
| Standalone HTML | (native) | Single-file portable HTML |
| High-DPI PNG | modern-screenshot 2x-3x | Retina-grade PNG |

Tech: juice + modern-screenshot + xlsx + papaparse + marked + highlight.js + dompurify.

## Pattern Library implications

### Strengthening events

| Pattern / Library-vocab | Type | Implication |
|---|---|---|
| Pattern #84 84c.1 sub-sub-mechanism agent-detection layer | Sub-sub-mechanism N+1 strengthening | 8-agent CLI ecosystem at single subject; mature 84c.1 continues strengthening |
| Pattern #88 Anti-Slop-Design-Curation | N+1 strengthening via huashu-md-html attribution | "Anti-AI-slop discipline" cited from `alchaincyf/huashu-md-html` = v82 huashu-design family attribution |
| Pattern #57 sub-variant 57c-product 6+-corpus-citation density | Within-pattern strengthening | Claude Code v65 + Codex v62 + Cursor v75/v76 + OpenCode v67 in agent-detection list |
| Pattern #52 HIGH-NOT-EXTREME sub-class | N+1 strengthening at pulse-window | ~385 stars/day × 12 days |
| Pattern #83 Honest-Deficiency-Disclosure | Within-pattern strengthening | 5-of-7 features marked stable + 2 marked in-progress (honest-feature-status-accounting) |
| Pattern #57 NEW sub-variant candidate "Same-Org Cross-Product Skill-Vendoring within Indie-Org Portfolio" | NEW PROVISIONAL N=1 | op7418/guizang vendored in both v83 and v91 = same-org-cross-product-skill-vendoring layer |

### NEW Library-vocab registrations at v91 (6 items)

| Item | Status |
|---|---|
| **"Same-Org Sister-Product Sub-90-Day Multi-Product Release with Cross-Product Skill-Vendoring"** (PRIMARY) | PROVISIONAL N=1 |
| "Zero-API-Key via Reuse-of-Logged-In-Agent-Session" | PROVISIONAL N=1 |
| "Multi-Surface-Output from Single-Markdown-Input (9 surfaces)" | PROVISIONAL N=1 |
| "Hard-Constraint Template Discipline (5-rule)" | PROVISIONAL N=1 |
| "CJK-First Font-Stack at Template-Level Hard-Constraint" | PROVISIONAL N=1 |
| "Sandboxed-Iframe-Preview with allow-scripts-same-origin-quarantines-cookies" | PROVISIONAL N=1 |

### Pattern #19 NEW sub-mechanism registration

| Item | Status |
|---|---|
| Pattern #19 NEW sub-mechanism "Indie-Org-with-Rapid-Multi-Product-Release-Cadence" | PROVISIONAL N=1 |

## Comparison to peer multi-skill T1 subjects

| Aspect | v75 impeccable | v81 taste-skill | v83 open-design | v85 ui-ux-pro-max | v90 academic-research-skills | **v91 html-anything** |
|---|---|---|---|---|---|---|
| Multiplicity layer | 1-skill × 14-harness | 12-skills × ~4-harness | 31-skill × 16-harness | 1-skill × 18-platform | 4-nested-versioned-sub-skill × ≥2-harness | **75-skill × 9-surface × 8-agent** |
| Output surface | Design system | Design aesthetics | Design (UI/UX) | Design (UI/UX) | Academic publishing pipeline | **Multi-modal content (9 surfaces)** |
| Vertical | Design | Design | Design | Design | Academic-research | **Agentic content creation** |
| Orchestrator | None | None | None | None | YES (Academic Pipeline) | None (parallel-surface-output) |
| Honest-disclosure | NOTICE.md attribution | None observed | bundled-MIT attribution + 80-point honest-deficiency | None observed | 31% citation error-rate | 5-stable/2-in-progress feature-status |
| Key novelty | 14-harness multi-target | 12-skill tri-axis taxonomy | 31-skill + multi-tier corpus-recursive | 18-platform skill.json + 669+ codified-elements | 4-nested-versioned-sub-skill orchestrator | **Zero-API-key reuse-of-logged-in-session + 9-surface output + same-org sister to v83** |

v91 sits at a **distinct structural point**: single-product multi-surface output via 8-agent ecosystem with zero-API-key paradigm. Closest to v85's single-product-multi-platform-deployment but at output-axis (multi-surface) rather than platform-axis (multi-platform).

## Functional fit for Storm Bear vault (Phase 0.9 (b) STRONG)

**DIRECT-FIT mapping** (vs v90's INDIRECT):

| Vault use-case | html-anything surface | Application |
|---|---|---|
| Wiki entity-page publishing | Magazine articles surface | Convert vault markdown wikis → publishable HTML |
| Scrum sprint reports | Magazine articles surface | Markdown sprint-summary → web-readable HTML |
| Retrospective decks | Keynote deck surface | Bullet-list markdown → presentable slide deck |
| Sprint metric dashboards | Data report surface | Pattern Library state-tables → charted reports |
| Social-share of wiki insights | Tweet card / Xiaohongshu surface | Single-wiki-finding → social card PNG |
| Walkthrough screencasts | Hyperframes video surface | Routine workflow → frame-script-video |
| Embedded interactive demos | Web prototype surface | Pattern-comparison interactive demo |

**MODERATE cost-of-trial**: `git clone + pnpm install + pnpm dev` ≈ 5-15 min (Node + pnpm + 3000-port + dependency-resolution). Heavier than v87 #2 single-file-copy or cc-switch single-binary, lighter than full design-system deployment.

**Reversibility**: `rm -rf html-anything/` directory + `port 3000` freed.

**Pilot ranking**: **Tier-1 position #3** — DIRECT vault-utility at multi-surface-output layer; MODERATE cost-of-trial. DISPLACES teleport v88 from #3 → #4 + VibeCodingTracker v89 from #4 → #5 + academic-research-skills v90 from #5 → #6.

**Suggested vault application path**:
1. Clone + install in vault scratch sub-directory (`03 Projects/html-anything-pilot/`)
2. Start `pnpm dev` → localhost:3000
3. Point vault markdown wiki to html-anything as input → magazine surface output
4. Compare standalone HTML quality vs current `03 Published/` flow
5. Decision-gate: if direct-utility >2× current flow, adopt; else uninstall

## Suggested next-action (vault application)

This is the FIRST T1-actionable Tier-1 pilot with DIRECT functional-fit at the markdown→multi-surface-output layer in the v60+ corpus. Recommended IMMEDIATE next-action AFTER current Phase 5 vault sync: trial pilot on a single vault wiki (suggest: v90 academic-research-skills wiki itself as input → magazine surface output) to evaluate vs existing `03 Published/` standalone HTML workflow.
