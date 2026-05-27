# Subject: cmux (manaflow-ai)

**Repo:** https://github.com/manaflow-ai/cmux
**Homepage:** https://cmux.com
**Wiki version:** v99 (built under routine v2.3.1; 3rd execution post-codification 2026-05-25)
**Built:** 2026-05-27

## One-line

Ghostty-based native macOS terminal application with vertical tabs and notifications, purpose-built to host and orchestrate concurrent AI coding agent sessions.

## Tier classification

**T2 Service** — NEW sub-archetype **"Native-Desktop Terminal Multiplexer for AI Coding Agents"** PROVISIONAL N=1 (Phase 4b PRIMARY proposal at `01 Analysis/(C) T2-NEW-sub-archetype-Native-Desktop-Terminal-Multiplexer-for-AI-Coding-Agents-N1-registration.md`).

Distinct from prior T2 sub-archetypes: v66 agentmemory memory-system / v70 codegraph code-index / v73 cc-switch provider-management / v85 ui-ux-pro-max design-skill / v89 VibeCodingTracker observability / v97 distill CLI-compression. cmux occupies the active multi-session orchestration at native-desktop scale axis.

## Facts (verified GitHub API 2026-05-27)

| Field | Value |
|---|---|
| Owner | manaflow-ai (org id 171392238, created 2024-05-31 SF-based) |
| Created | 2026-01-28 |
| Last push | 2026-05-27 (same-day at fetch) |
| Age | 119 days |
| Stars | 19,853 |
| Velocity | **166.8 stars/day = Pattern #52 HIGH-NOT-EXTREME N+1 strengthening** (top-level CONFIRMED at v75) |
| Forks | 1,492 (fork ratio 0.0751) |
| Subscribers | 28 |
| Open issues | 2,187 (HIGH engagement — active community) |
| Releases | 41 (latest v0.64.10 on 2026-05-23 + `nightly` channel) |
| Repo size | ~334 MB |
| Primary language | **Swift 81.9% = CORPUS-FIRST Swift-primary subject in v60+ window** |
| License | **GPL-3.0-or-later + commercial dual-license = CORPUS-FIRST** in v60+ window (NOASSERTION at GitHub API; LICENSE file declares dual-license explicitly) |
| Topics | amp, claude-code, codex, gemini, ghostty, opencode, terminal, tmux |
| Discussions | ENABLED |

## Authors

- **Lawrence Chen** (@lawrencecchen) — SF + @manaflow-ai company affiliation + GitHub since 2019-08-11 + 179 public repos + 197 followers + Twitter @lawrencecchen
- **Austin Wang** (@austinywang) — Founder & CEO @ Manaflow + Yale + ex NASA JPL + ex Chess.com + SF + austinywang.com + bio "Founder & CEO @ Manaflow | Prev Yale, NASA JPL, Chess.com" + Twitter @austinywang
- **Manaflow Inc.** = SF-based AI startup (founders@manaflow.com); 30 public repos + 184 followers + org-created 2024-05-31

## Architecture

**Native macOS app (Swift 81.9% + AppKit)**: Xcode workspace + 4 distinct `.entitlements` files (cmux + cmux-helper + cmux.nightly + cmux.release) + AppIcon.icon + Assets.xcassets

**Terminal engine**: embedded **libghostty** for rendering with Ghostty config compatibility + GPU-accelerated; `ghostty.h` + `cmux-Bridging-Header.h` for Swift/C interop

**Top-level UX**: vertical + horizontal tabs with per-tab git / PR / port metadata; notification rings + side panels for multi-agent attention-signaling

**Auxiliary surfaces**: CLI + socket API for automation; integrated scriptable browser ported from `agent-browser` with element-interaction APIs; SSH workspace support with remote network routing; browser-auth import from 20+ browsers

**Distribution**: 4-channel matrix
1. DMG download from GitHub releases (with Sparkle auto-update)
2. Homebrew Cask: `brew tap manaflow-ai/cmux && brew install --cask cmux`
3. Nightly channel: separate app bundle running alongside stable
4. cmux.com homepage / Founder's Edition Stripe subscription (early access to cmux AI context system + iOS app + cloud VMs + voice mode)

**State locations**: `~/Library/Application Support/cmux/` (session restore snapshots) + `~/.cmuxterm/` (agent hook mappings) + project-root `cmux.json` (per-project custom commands)

## In-product `skills/` bundle

8 in-product Claude Code skill folders: cmux + cmux-browser + cmux-customization + cmux-diagnostics + cmux-keyboard-shortcuts + cmux-markdown + cmux-settings + cmux-workspace.

= **CORPUS-FIRST in-product packaged Claude-Code-skills bundle at native-macOS-terminal-multiplexer scope**.
= **agentskills.io standard 4-implementer chain extension**:
- v76 HoangNguyen0403/agent-skills-standard (anchor; first third-party implementer)
- v93 anthropics/skills (authoritative reference + spec at `./spec/` + template at `./template/`)
- v98 mukul975/Anthropic-Cybersecurity-Skills (third-implementer at cybersecurity-vertical)
- **v99 manaflow-ai/cmux (fourth-implementer at native-terminal-multiplexer-vertical)**
- = Pattern #57 sub-variant "Standards-Conformance-Layer Corpus-Recursive Chain" PROVISIONAL N=1 from v98 → **N=2 STRENGTHENING at v99**

## Supported AI coding agents

13 corpus-subject + harness citations in supported-agents list: **Claude Code** (native integration) v65 + **Codex** v62 + **Grok** + **OpenCode** v67 + **Pi** + **Amp** + **Cursor CLI** v75/v76 + **Gemini** + **Rovo Dev** + **Copilot** + **CodeBuddy** + **Factory** + **Qoder** v83

Pattern #57 sub-variant 57c-product citation density: ties v94 Understand-Anything ~13-citation possible CORPUS-RECORD; exceeds v98 6+ citation + v85 10-citation prior records.

## i18n

**21-locale README distribution** = **CORPUS-RECORD-HIGH locale-breadth at single subject** (exceeds v77 easy-vibe 13-locale + v78 ECC 10-locale prior records by ~60%):

en (default) + **vi** (Vietnamese — first-class i18n inclusion = Phase 0.9 (a)-3 product-locale-inclusion PASS via v78 ECC precedent codified at routine v2.3.1 §24) + ar + bs + da + de + es + fr + it + ja + km (Khmer — first KM-locale subject in v60+ window) + ko + no + pl + pt-BR + ru + th + tr + uk + zh-CN + zh-TW

= NEW Library-vocab candidate "21-Locale README Distribution at Native-Desktop Product Scale" PROVISIONAL N=1.

## License

**GPL-3.0-or-later + commercial dual-license** = CORPUS-FIRST in v60+ window. LICENSE file verbatim:

> "This software is dual-licensed... GNU General Public License v3.0 or later (GPL-3.0-or-later)... For organizations that cannot comply with GPL, a commercial license is available. Contact founders@manaflow.com for details."

Structurally distinct from:
- v78 ECC `OSS-with-hosted-Pro-SaaS-tier-on-MIT-base` (RETIRED at v96 forced-retire)
- v98 Anthropic-Cybersecurity-Skills `Apache 2.0 + CC-BY 4.0` Inter-License Boundary
- v77 easy-vibe `CC-BY-NC-SA 4.0`
- v74 LLMs-from-scratch `Apache-2.0 with Book-Content-Exclusion` (Pattern #45 45d)

NEW Library-vocab candidate "GPL-3.0-or-later + Commercial Dual-License at Single Subject" PROVISIONAL N=1.

## Methodology framing

> "cmux is not prescriptive about how developers hold their tools... Give a million developers composable primitives and they'll collectively find the most efficient workflows faster."

= Anti-prescriptive architectural philosophy. NEW Library-vocab "Composable-Primitives-Over-Prescriptive-Workflows" PROVISIONAL N=1. Distinct from Pattern #51 vibe-coding-spectrum (this is meta-architectural framing not vibe-leaning).

## CI / AI-code-review tooling

`.coderabbit.yaml` (CodeRabbit AI code review) + `.greptile` (Greptile AI code search) = **CORPUS-FIRST AI-code-review-CI-tooling at AI-coding-agent product subject** = meta-recursive AI-tooling-on-AI-tooling. NEW Library-vocab "AI-Code-Review-CI-Tooling-at-AI-Coding-Agent-Product-Subject" PROVISIONAL N=1.

## Quantitative-marketing claims

**Pattern #82 NEGATIVE-EVIDENCE**: README header contains zero quantitative marketing claims (no token-savings %, no benchmark numbers, no performance figures, no scale claims). Anti-prescriptive philosophy + active-development positioning. Distinct from v78 ECC's 9+ README-header claims and v85 ui-ux-pro-max's 669+ codified element claims.

## Pattern observations summary

**PHASE 4b PRIMARY** (in companion proposal-document):
- NEW T2 sub-archetype **"Native-Desktop Terminal Multiplexer for AI Coding Agents"** PROVISIONAL N=1

**SECONDARY (within-wiki observations; NOT promoted at v99 per cascade-discipline)**:

1. **Pattern #52 HIGH-NOT-EXTREME N+1 strengthening** (already CONFIRMED top-level v75); 166.8/d × 119d at mid-life-cycle band
2. **Pattern #57 sub-variant 57c-product 13-citation density** ties v94 ~13-citation possible CORPUS-RECORD
3. **Pattern #57 sub-variant agentskills.io 4-implementer chain N=2 STRENGTHENING** (v76 + v93 + v98 + v99); v100 audit promotion-eligibility candidate
4. **Pattern #84 84c.1 N+1 post-CONFIRMED-strengthening 9-instance arc** v85+v90+v92+v93+v94+v95+v97+v98+v99
5. **Pattern #84 84d Hardware-Substrate-Tolerance N=4 STRONGER PROMOTION-ELIGIBLE administrative at v100** (v79 PyTorch-MPS + v94 WASM + v97 MLX-Apple + v99 native-macOS-Swift-AppKit-with-libghostty-embed; was N=3 at v97 → N=4 at v99)
6. **Library-vocab #12 LLM-routing artifacts (CONFIRMED N=5) strengthening** — AGENTS.md + CLAUDE.md + THIRD_PARTY_LICENSES.md + `skills/` directory all present
7. **Pattern #82 quantitative-marketing NEGATIVE-EVIDENCE** at README header (zero claims; anti-prescriptive framing)
8. **Pattern #66 supply-chain awareness within-pattern strengthening** at native-macOS Apple-dev-toolchain layer (4 distinct `.entitlements` files + Sparkle auto-update + Homebrew Cask verification + CodeRabbit + greptile code-review)
9. **NEW Library-vocab candidates (5 PROVISIONAL N=1, NOT registered at v99 ship per cascade-discipline)**: 21-Locale README CORPUS-RECORD-Distribution + GPL+Commercial Dual-License + AI-Code-Review-CI-Tooling-at-AI-Coding-Agent-Subject + Native-Macos-Apple-Dev-Toolchain at AI-Agent Subject + Composable-Primitives-Over-Prescriptive-Workflows Philosophy
10. **Pattern #19 NEW sub-mechanism candidate "SF-Indie-Founder-Org-with-Native-Macos-Product Profile" NOT registered at v99** to avoid worsening Pattern #19 graveyard (~10-11 PROVISIONAL N=1 candidates post-v98; v100 CONSOLIDATION pressure CRITICAL)
11. **Khmer (km) locale-inclusion = first-instance corpus-novel localization** in v60+ window (observational note only; not Library-vocab vehicle)

## Storm Bear evaluation (Phase 0.9 STRICT)

**STRONG INCLUDE 4/4** with (c) STRONGEST + (a)(b)(d) STRONG:

- **(a) STRONG** via (a)-3 product-locale-inclusion (`README.vi.md` + 21-locale CORPUS-RECORD); STRONG not STRONGEST because single-sub-axis support without direct cultural-peer overlap
- **(b) STRONG** LOW cost-of-trial (`brew install --cask cmux` ~5min reversible) × DIRECT functional-fit for Storm Bear's intensive multi-session Claude Code workflow at macOS-native env
- **(c) STRONGEST** 10+ corpus-firsts + NEW T2 sub-archetype + multiple Library-vocab candidates + Pattern #84 84d N=4 PROMOTION-ELIGIBLE strengthening
- **(d) STRONG** 13-citation density ties v94 possible CORPUS-RECORD + agentskills.io 4-implementer chain N=2 strengthening + Pattern #84 84c.1 9-instance arc + Library-vocab #12 strengthening

**Streak: "32+1*"** NEW CORPUS-RECORD = first 13-consecutive milestone post-v84 OVERRIDE
**Window: 34-instance v65-v99** = 33 PASS + 1 OVERRIDE = **97.1% INCLUDE rate** uptick from v98's 97.0%
**Strength categorization v65-v99**: STRONGEST × 14 + STRONG × 11 + MODERATE × 4 + WEAK × 5 + OVERRIDE × 1 (STRONG +1 from v99 = STRONG ties WEAK by 6)
**Override-frequency**: 1-in-34 well below v2.3.1 redesign trigger thresholds (2-in-20 / 3-in-30)

## Pilot recommendation

**HIGH-RELEVANCE vault pilot Tier-1 actionable position #4 NEW** (between distill v97 #3 and v98 #5):

Recommended trial path ~5-10 min hands-on, reversible:
1. `brew tap manaflow-ai/cmux && brew install --cask cmux` (~3 min)
2. Launch cmux; create 2-3 vertical tabs (one Claude Code, one shell, optionally one Codex)
3. Test notification rings + attention panels with a long-running task (e.g. wiki build); observe attention-signaling when agent needs input
4. Reversible: `brew uninstall --cask cmux` + remove `~/Library/Application Support/cmux/` + `~/.cmuxterm/`

NOT a methodology-influence Tier-1-special (cmux uses corpus methodology rather than influencing it). DIRECT vault-utility track.

## v100 audit batch additions from v99 (~10-12 items)

- NEW T2 sub-archetype first-cycle stale-check
- 21-locale CORPUS-RECORD-Distribution Library-vocab first-cycle stale-check + locale-count-axis discipline as v2.4 codification candidate
- GPL+commercial dual-license Library-vocab first-cycle stale-check
- Swift-primary CORPUS-FIRST stale-check
- Pattern #84 84d Hardware-Substrate-Tolerance N=4 STRONGER PROMOTION-ELIGIBLE administrative promotion at v100 (PROMOTE: 4-variant cross-substrate spread PASS at PyTorch-MPS + WASM + MLX-Apple + native-macOS-Swift)
- Pattern #57 sub-variant agentskills.io 4-implementer chain N=2 STRENGTHENING administrative entry
- Library-vocab #12 LLM-routing artifacts N=5+ further-strengthening entry
- AI-Code-Review-CI-Tooling-at-AI-Coding-Agent-Product-Subject Library-vocab first-cycle
- Native-Macos-Apple-Dev-Toolchain-at-AI-Agent-Subject Library-vocab first-cycle
- Composable-Primitives-Over-Prescriptive-Workflows Library-vocab first-cycle
- Khmer-locale-inclusion observational note (no Library-vocab vehicle until N=2)

Combined v100 batch projection: ~38-44 items (climbing toward CORPUS-RECORD audit territory; v96's 71-item record still safely ahead).
