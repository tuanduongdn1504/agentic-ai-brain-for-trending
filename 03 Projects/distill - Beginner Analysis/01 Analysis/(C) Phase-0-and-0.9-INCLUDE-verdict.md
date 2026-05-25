# (C) Phase 0 + Phase 0.9 verdict — distill (v97)

**Subject**: `samuelfaj/distill`
**Routine**: v2.3.1 (FIRST execution under v2.3.1; supersedes v2.3 base)
**Verdict**: **STRONG INCLUDE 3/4** with (c) STRONGEST + (b)(d) STRONG + (a) FAIL
**Streak**: "30+1*" NEW CORPUS-RECORD (11-consecutive clean PASS post-v84 OVERRIDE)

---

## Phase 0 — Sanity check

| Field | Value |
|---|---|
| Repo | https://github.com/samuelfaj/distill |
| Created | 2026-03-06 |
| Last push | 2026-05-19 (6 days before fetch) |
| Owner | Samuel Fajreldines (individual, Rio Grande do Sul, Brazil) |
| Owner context | @smartplan-br company association; blog samuelfaj.com; 43 followers / 14 following / 68 public repos / GitHub since 2015-06-22 (11-year account) |
| Primary language | TypeScript |
| License | **null** (no LICENSE file; README does not declare a license) |
| Stars / Forks / Subscribers / Issues | 559 / 33 / 1 / 4 |
| Velocity | 559 stars / 80 days = ~7.0 stars/day (LOW; below all Pattern #52 sub-class floors) |
| Topics | claude-code, codex, llm, tokens |
| Discussions | DISABLED |

**Tier**: T2 Service (CLI compression tool with bundled local LLM). Side-artifact: T1 Assistant Skill (`skills/distill/` packaged Claude Code skill installed via npm postinstall).

**Architecture**: Monorepo workspace (`packages/cli` + 5 platform-specific binary packages: distill-darwin-arm64 + darwin-x64 + linux-arm64 + linux-x64 + win32-x64). 12 TypeScript source files: cli / config / dataset / dsl-memory / llm / local-server / onboarding / prompt / stream-distiller / text / user-config. Build via Bun; workspace publish via npm@11.7.0. Test via Bun. 4 HTML spec artifacts published at repo root: ANALYSIS.html + REQUIREMENTS.html + TDD.html + TODO.html.

**Runtime model**: Ships its own fine-tuned `samuelfaj/distill-1.7B-MLX` (1.7B parameters, 4-bit quantization) on Hugging Face. Recommended 8 GB+ RAM, 16 GB+ comfortable. MLX framework = Apple Silicon native.

**Inclusion preliminary**: PASS Phase 0 (LLM-augmented + Claude-Code-ecosystem-tagged + verifiable + ≤6-mo-old).

---

## Phase 0.9 — Storm Bear filter (routine v2.3.1 §9 7-axis (a) taxonomy + §10 (b) + §11+ (c)(d))

### (a) Cultural-peer / Storm Bear archetype — **FAIL** (with NEW (a)-8 PROVISIONAL N=1 registration)

| Sub-axis | Evidence | Verdict |
|---|---|---|
| (a)-1 direct-author-peer (VN-located or Vietnamese-diaspora) | Samuel Fajreldines = Brazilian, no VN signal | FAIL |
| (a)-2 native-language-fluency (Vietnamese) | README English-only; bio English; no VN strings | FAIL |
| (a)-3 product-locale-inclusion (vi-VN at first-class) | No localization in repo | FAIL |
| (a)-4 community-org | Solo dev + smartplan-br company association; smartplan-br is a Brazilian SaaS company, not a community-org | FAIL |
| (a)-5 multi-org-founder | smartplan-br is single company association; not multi-org | FAIL |
| (a)-6 cluster-extension (Asian-LOCATED cluster) | Brazil = South-American not Asian | FAIL |
| (a)-7 Foundational-Vendor-Direct-Source (Anthropic/OpenAI/Google/Microsoft/Meta) | Solo Brazilian indie; not foundational vendor | FAIL |

**All 7 sub-axes FAIL.** **(a) verdict: FAIL.**

#### NEW (a)-8 sub-axis "South-American-LOCATED" PROVISIONAL N=1 registration at observational layer

Brazil = **first South-American-LOCATED subject in v60+ window** (corpus historically dominated by Asian-LOCATED + North-American + European-LOCATED + Foundational-Vendor clusters). Registered at observational layer for cluster-formation tracking pending N=2 emergence:

- **Does NOT promote (a) to PASS at v97** (single data-point; observational only)
- **v100 first-cycle stale-check** + **v105 N=2 watch** + **v110 retire-check if N=1-only**
- v2.4 codification candidate: formal (a)-8 inclusion rule mirroring (a)-7 N=3 promotion ladder
- Routine v2.3.1 §25 does NOT specify (a)-8 registration pathway formally; this wiki proposes the mechanism by analogy to (a)-7 anchor → strengthening → promotion arc

### (b) Functional-fit × cost-of-trial — **STRONG**

| Sub-axis | Evidence | Verdict |
|---|---|---|
| Cost-of-trial | `npm i -g @samuelfaj/distill` then `distill` onboarding. ≤5-min hands-on. Reversible via `npm uninstall -g @samuelfaj/distill`. RAM requirement 8 GB+ (operator's Apple Silicon Mac comfortably exceeds). | **LOW** |
| Functional-fit (vault applicability) | Operator's vault sessions frequently pipe `grep` / `find` / `awk` outputs to agents for analysis — exactly the class of token-blow distill targets. Observed in this session: 71-item v96 audit + sequential GitHub API + WebFetch results = token-intensive. distill compression layer applicable at session-pipe boundary. | **MODERATE-DIRECT** (not direct vault-output utility like v91 html-anything but direct vault-process utility) |
| Methodology-fit | Distill Language methodology (teach LLM to compress) cross-applicable to routine v2.4 evolution: could inform compression-discipline at audit-batch + state-block writing layers where vault routinely accumulates 200K+ character state-blocks | **STRONG** |

**(b) verdict: STRONG** (LOW cost × MODERATE-DIRECT functional × STRONG methodology-fit).

### (c) Methodology-influence + corpus-novelty — **STRONGEST**

CORPUS-FIRST observations at v97 (5+ at single subject; pressure-test required at v100 audit):

1. **Own-trained fine-tuned bundled Expert Language Model at single-subject solo-founder scale** — `samuelfaj/distill-1.7B-MLX` 1.7B 4-bit on Hugging Face. CORPUS-FIRST in 96-wiki corpus. Prior subjects use BYOK + remote-API (cloud LLM) or zero-API-key reuse-of-logged-in-session (v91); none ship their own trained model. **Phase 4b PRIMARY proposal.**
2. **MLX-Apple-Silicon-bundled-fine-tuned-model** — distinct from v79 PyTorch MPS substrate at agent-research-framework layer (v79 trained tiny model on Karpathy framework; v79 didn't ship pretrained). v97 = pretrained-shipped-bundled. CORPUS-FIRST MLX framework in v60+ window.
3. **5-platform-binary monorepo via npm workspaces postinstall pattern** — `packages/cli` orchestrator + 5 platform-binary packages (distill-darwin-arm64/x64 + distill-linux-arm64/x64 + distill-win32-x64). User does `npm i -g @samuelfaj/distill`; postinstall selects correct platform-binary. CORPUS-FIRST 5-platform-binary distribution at solo-founder T2 service scale. Distinct from v83 4-distribution-method matrix (different mechanism: v83 = 4 install-channels; v97 = 1 install-channel + 5 platform-binary fan-out).
4. **Spec-as-HTML-Published-at-Repo-Root** — ANALYSIS.html (3,089 B) + REQUIREMENTS.html (3,335 B) + TDD.html (2,006 B) + TODO.html (1,593 B) all at repo root, not in docs/. CORPUS-FIRST published-dev-spec-artifacts-as-HTML-at-repo-root in v60+ window. Distinct from existing LDS sub-mechanisms (78a CLI-enforceable + 78b in-tree-curriculum + 78c educational + 78d operator-system-LDS). PROVISIONAL Library-vocab N=1.
5. **Bun-for-build + npm-for-workspace Hybrid Tooling** — `packageManager: npm@11.7.0` at workspace root + `bun run` for build/test/release-check scripts. CORPUS-FIRST hybrid Bun+npm tooling in v60+ window. (v84 OVERRIDE-provenance Bun-primary was retired at v96 §18 forced-retire; v97 = fresh non-OVERRIDE PROVISIONAL N=1 at hybrid layer.)
6. **Distill Language methodology** — secondary README section "We also teach your LLM to talk and think a more efficient way" with Distill Language reference image. Compression-as-trainable-discipline at LLM-output layer. PROVISIONAL Library-vocab N=1.

**(c) verdict: STRONGEST** (5-6 corpus-novel artifacts at single subject; v100 audit pressure-test required for ad-hoc-coined frames).

### (d) Corpus-recursion + cross-wiki density — **STRONG**

| Cross-reference | Evidence | Pattern |
|---|---|---|
| Apple Silicon hardware substrate | MLX (v97) + PyTorch MPS (v79) + WASM (v94) = 3-instance arc | Pattern #84 84d Hardware-Substrate-Tolerance **N=3 PROMOTION-ELIGIBLE administrative at v100 audit** |
| Claude Code ecosystem citation | Topic tag `claude-code` + `skills/distill/` Claude Code skill + Codex topic tag | Pattern #57 sub-variant 57c-product 2-citation MID density (Claude Code v65 + Codex v62) |
| Absent-LICENSE | NULL license + README silent | Pattern #29 absent-LICENSE strengthening (v80 SmartMacroAI N=1 anchor at NOASSERTION; v97 adds README-also-silent variant distinct from v79 README-declared-MIT-no-LICENSE-file = N+1 evidence point at Pattern #29 cluster) |
| Quantitative-marketing | "Save up to 99% of tokens" + "98.7% saved" in worked example | Pattern #82 strengthening (5+ explicit quantitative claims) |
| Repo-stored skill | `skills/distill/` Claude Code skill in monorepo | Pattern #84 84c.1 N+1 strengthening (v85+v90+v92+v93+v94+v95+v97 = 7-instance arc) |
| Token-economy at LLM layer | 99% token saving theme | Library-vocab "Token-Economy-Quantification" N=2 STRENGTHENING (v87 anchor N=1 claude-comstyle per-style %-token-impact + v97 N=2 product-level %-token-saving claim — distinct token-economy axis but compatible methodology-vocab) |

**(d) verdict: STRONG** (4+ Pattern strengthenings; 1 PROMOTION-ELIGIBLE administrative at v100; corpus-recursive depth MODERATE).

---

## Final verdict

**STRONG INCLUDE 3/4** with (c) STRONGEST + (b)(d) STRONG + (a) FAIL.

**Streak extension**: 30 PASS (v65-v83 + v85 + v87 + v88 + v89 + v90 + v91 + v92 + v93 + v94 + v95 + **v97**) + 1 OVERRIDE (v84) = **"30+1*"** NEW CORPUS-RECORD (first 30-consecutive milestone post-OVERRIDE; extends v95's 29-consecutive by 1).

**Strength distribution v65-v97 update**:
- STRONGEST × 14 (v95 last)
- STRONG × 9 (+1 from v97 = STRONG now leads its prior count; ties second-place position behind STRONGEST)
- MODERATE × 4
- WEAK × 5
- OVERRIDE × 1

32-instance window v65-v97 = 31 PASS / 1 OVERRIDE = **96.9% INCLUDE rate** (uptick from v95's 96.8%; uniform monotonic ascent continues).

Override-frequency: 1-in-32 = well below v2.3 redesign trigger thresholds (2-in-20 / 3-in-30).

**Routine v2.3.1 first-execution validation: CLEAN** — no amendments needed at this build. NEW (a)-8 sub-axis registered as v2.4 codification candidate; mechanism proposed by analogy to (a)-7 anchor-→-strengthening-→-promotion ladder. §26 corpus-recursive event-class taxonomy: negative-case execution (zero hits across Class 1/2/3/4) — exercises the class-detection methodology path cleanly.

## Vault pilot-ranking position

**Tier-1 actionable position #3 NEW** (between anthropics/skills v93 #2 and claude-comstyle v87 #4):

| Rank | Wiki | Reason |
|---|---|---|
| 1 | Understand-Anything (v94) | Most direct vault-utility at methodology-influence layer (Karpathy-LLM-Wiki-Pattern direct input) |
| 2 | claude-plugins-official (v95) | Already-installed-by-default + multi-DIRECT vault-applicable plugins (claude-md-management + skill-creator + session-report) |
| **3** | **distill (v97)** | **DIRECT vault-process utility at CLI-piping layer + LOW cost-of-trial + reversible + addresses documented context-thrashing problem at session-pipe boundary** |
| 4 | claude-comstyle (v87) | Direct prompt-style composition (DISPLACED from #3) |
| 5 | cc-switch (v73) | Provider-portability (DISPLACED) |
| 6+ | (other ranks shift down by 1) |

**Methodology-influence Tier-1-special multi-track**: v97 does NOT qualify for methodology-influence Tier-1-special track (no foundational-vendor status; no source-authoritative reference-implementation; subject does not redefine corpus methodology-direction).
