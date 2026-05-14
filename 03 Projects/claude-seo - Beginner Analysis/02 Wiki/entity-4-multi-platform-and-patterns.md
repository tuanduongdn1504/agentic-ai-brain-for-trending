# Entity 4 — 5-platform reach + Pattern Library implications

> **Type:** Multi-platform analysis + complete v64 Pattern Library implications package
> **Cross-references:** [Cluster 2 architecture](./cluster-2-architecture-and-skill-system.md) (CLAUDE.md vs AGENTS.md split) / [Entity 2 portfolio](./entity-2-ecosystem-portfolio-n3.md) / [Entity 3 NEW candidates](./entity-3-domain-vertical-and-living-standards.md)

## 5-platform reach + 1 sister-port = 6-platform combined

| # | Platform | How invoked | Discovery file |
|---|---|---|---|
| 1 | **Claude Code** | `/plugin install claude-seo@agricidaniel-seo` OR `bash install.sh` | `CLAUDE.md` (210 lines) |
| 2 | **Cursor** | Cursor reads `AGENTS.md` automatically | `AGENTS.md` (126 lines) |
| 3 | **Cursor Cloud Agents** | Same as Cursor + cloud-specific gotchas | `AGENTS.md` (Cursor Cloud section) |
| 4 | **Google Antigravity** | `plugin.json` discovery at repo root; install to `~/.gemini/antigravity/plugins/claude-seo/` | `AGENTS.md` (Antigravity section) |
| 5 | **Gemini CLI** | Via Antigravity plugin or direct integration | `AGENTS.md` (Antigravity covers) |
| **+1** | **Codex CLI (sister-port)** | Separate repo `AgriciDaniel/codex-seo` with TOML agents + deterministic runners + plugin packaging | (codex-seo repo own docs) |

**5 platforms + 1 sister-port = 6-platform combined reach — HIGHEST in corpus T1 history.**

Compared with peers:
- **cc-sdd v61**: 8 platforms (2 stable + 5 beta + 1 experimental) at framework-scale via install-time-format-translator
- **karpathy-skills v63**: 2 platforms at single-skill-scale via manual-sync (Claude Code + Cursor)
- **claude-seo v64**: 5 platforms at skill-collection-scale via CLAUDE.md vs AGENTS.md split + 1 sister-port

## The CLAUDE.md vs AGENTS.md split — Pattern #18 Layer 1 mechanism

### How the split works

| File | Audience | Content |
|---|---|---|
| **CLAUDE.md** | Claude Code only | Architecture / Commands / Development Rules / Security Rules / Report Generation Rules / Ecosystem |
| **AGENTS.md** | Cursor / Cursor Cloud / Antigravity / Gemini CLI | Overview / Quick Reference (26 commands) / Per-platform invocation sections / Cursor Cloud gotchas / Architecture / Credits |

**Key discipline**: AGENTS.md says explicitly: *"For Claude Code users: see CLAUDE.md instead."* CLAUDE.md does NOT have an analogous reverse-pointer to AGENTS.md (Claude Code reads CLAUDE.md natively; AGENTS.md exists for other-platform discovery).

### The architectural insight

- **SHARED skill content** — SKILL.md files (25 files) are platform-agnostic Markdown; they describe SEO analysis logic in natural language
- **PER-PLATFORM dispatch file** — CLAUDE.md and AGENTS.md describe HOW to invoke from each platform; they don't duplicate skill content

This mechanism scales linearly with platforms: adding a new platform = add one new section to AGENTS.md, no skill changes. Compare with cc-sdd v61's install-time-format-translator (transforms format per platform) — claude-seo's mechanism is SIMPLER (one shared format, multiple discovery files).

### Pattern #18 Layer 1 strengthening at 5-platform scale

Pattern #18 (Multi-Platform via Format Translation) tracks Layer 1 (cross-IDE-coexistence-by-discovery) and Layer 2 (runtime/install-time format-translation). claude-seo v64 strengthens Layer 1 at **5-platform scale** which is the largest single Layer 1 mechanism observed.

**Sub-archetype consolidation candidate at v66**: Layer 1 mechanism = **"shared-skill-content-with-per-platform-dispatch-file"** — distinct from cc-sdd v61 Layer 2 sub-archetype (install-time-format-translator) and karpathy-skills v63 single-skill-manual-sync. Phase 5 will note this as Pattern #18 strengthening at 5-platform scale.

## Codex sister-port — Pattern #18 Layer 2 NEW sub-archetype candidate

### What codex-seo is

- **Same SEO surface** as claude-seo (same 26 commands, same workflow)
- **Different host** (Codex CLI, not Claude Code)
- **Codex-native primitives**: TOML agents (not Markdown), plugin packaging (Codex-spec), deterministic runners (Codex CLI distinction)
- **Separate repo** at `AgriciDaniel/codex-seo` (not in claude-seo repo)
- **Same author** (Agrici Daniel maintains both)

### Why this is a NEW Pattern #18 Layer 2 sub-archetype candidate

Existing Layer 2 sub-archetypes (per v62 codex-plugin-cc wiki):
- **v60 free-claude-code**: api-protocol-translation-proxy (runtime translation Anthropic API ↔ 6 upstream provider protocols)
- **v61 cc-sdd**: install-time-skill-format-translator (transforms Markdown SKILL.md → per-platform format at install time, 8 platforms)
- **v62 codex-plugin-cc**: cross-vendor-platform-bridge-as-plugin (OpenAI publishes plugin FOR Claude Code rival platform)

**v64 claude-seo (codex-seo sister-port) NEW sub-archetype:** **"solo-author-cross-vendor-parallel-port-as-separate-repo"** — single author maintains parallel repos for distinct vendor primitives, NO translation layer, the two products are sibling repos. The user picks the right repo for their platform.

### Distinguishing mechanism

| Sub-archetype | Translation? | Where? | Vendor relationship |
|---|---|---|---|
| free-claude-code (60) | YES | Runtime | Bridge (single user can mix) |
| cc-sdd (61) | YES | Install-time | Single-source-many-platforms |
| codex-plugin-cc (62) | NO (prompt-framing variant) | N/A | Cross-vendor cooperation (OpenAI for Anthropic platform) |
| **claude-seo + codex-seo (64) NEW** | **NO** | **N/A** | **Solo-author parallel repos for distinct vendor primitives** |

The new sub-archetype is distinguished by **no translation + sibling repos + single author + distinct vendor primitives**. It's a strategic choice: rather than build a translator (cc-sdd's approach) or a cross-vendor bridge (codex-plugin-cc's approach), the author **maintains two complete implementations** because the primitive systems differ enough (Markdown vs TOML / Anthropic plugin spec vs Codex plugin packaging / Python scripts vs deterministic runners) that translation would lose fidelity.

### Phase 5 registration

In `_patterns/03-active-candidates.md`, append within Pattern #18 entry:

```markdown
**v64 claude-seo Layer 2 NEW sub-archetype candidate N=1 stale-flagged:**
solo-author-cross-vendor-parallel-port-as-separate-repo (claude-seo + codex-seo sibling repos by Agrici Daniel; no translation layer; distinct vendor primitives Markdown+Anthropic-plugin-spec vs TOML+Codex-plugin-packaging). Distinct from runtime translation (v60) / install-time translation (v61) / cross-vendor bridge (v62).

Un-stale criterion: 2nd subject with solo-author cross-vendor parallel-port arrangement.
Re-evaluate at: v67 (+3 wikis).
```

## Complete v64 Pattern Library implications package

### Direct strengthenings (within already-CONFIRMED or -CANDIDATE patterns) — 6 items

**1. Pattern #19 ecosystem-portfolio-builder sub-type N=3 strengthening — PROMOTION-ELIGIBLE at v66 mini-audit (PRIMARY)**

- Evidence: claude-seo + claude-blog + banana-claude + codex-seo + FLOW (**5 products**) by single author AgriciDaniel
- 3-axis cross-archetype: gotalab v61 (4 products SDD-vertical) + forrestchang v63 (2 products viral+commercial) + AgriciDaniel v64 (5 products SEO-vertical-with-cross-vendor-port)
- 3 distinct portfolio shapes = structural-diversity-at-N=3 = strongest possible promotion evidence under criterion #2
- See [Entity 2](./entity-2-ecosystem-portfolio-n3.md) for full analysis

**2. Pattern #18 Layer 1 cross-IDE-coexistence at 5-platform scale strengthening**

- Evidence: CLAUDE.md (210 lines, Claude Code) + AGENTS.md (126 lines, 4 other platforms) split discipline
- Mechanism: SHARED skill content + PER-PLATFORM dispatch file
- 5-platform reach = largest single Layer 1 mechanism observed
- Sub-archetype candidate: "shared-skill-content-with-per-platform-dispatch-file"

**3. Pattern #18 Layer 2 NEW sub-archetype candidate: solo-author-cross-vendor-parallel-port-as-separate-repo** (codex-seo sister-port to claude-seo)

- v64 N=1 stale-flagged; re-evaluate at v67

**4. Pattern #59 Claude Code Plugin Marketplace at high-engagement-solo-individual scale strengthening**

- 6.5K stars + 15.3% fork ratio + 5 platforms + 26 commands at solo-individual scale
- Sub-variant: solo-individual with medium-high engagement (~68 stars/day below Pattern #52 EXTREME-VIRAL 300+/day threshold)
- Distinct from EXTREME-VIRAL (mattpocock + karpathy + codex-plugin-cc) AND from corporate-scale (codex-plugin-cc)

**5. Pattern #52 EXTREME-VIRAL-VELOCITY counter-evidence**

- claude-seo ~68 stars/day in same observation window as karpathy-skills (102 days at observation, ~1186/day) and codex-plugin-cc (21 days at observation, ~847/day)
- claude-seo is **NOT in any 52a/52b/52c sub-archetype** (52a author-celebrity / 52b corporate-celebrity / 52c source-celebrity-derivative)
- Provides **negative-control evidence** that Pattern #52 sub-archetypes are bounded — most subjects don't trigger
- Strengthens Pattern #52 specificity (not over-broad)

**6. Pattern #28 Progressive Disclosure across 4 dimensions strengthening**

- Skill metadata (always loaded) → instructions (on activation) → resources (on demand) — author-stated Key Principle #1
- Google API credential tiers (Tier 0 → Tier 1 → Tier 2 → Tier 3) — credential progressive disclosure
- Extension system (opt-in install via `extensions/*/install.sh`) — capability progressive disclosure
- Skill auto-discovery (per-skill loaded on first use, not eagerly) — runtime progressive disclosure

**Sub-variant candidate**: "credential-tier-progressive-disclosure" — distinct from documentation/code progressive disclosure. v66 deliberation: register as Pattern #28 sub-variant?

### NEW top-level candidate registrations — 2 items

**7. NEW T1 sub-archetype: domain-vertical-skill-collection N=1 stale-flagged**

- First SEO-vertical T1 collection in corpus
- Distinct from general-purpose (mattpocock) / curated-meta (awesome-claude-skills) / corporate-curated (vercel) / single-artifact (karpathy)
- Un-stale criterion: 2nd domain-vertical T1 collection (e.g., claude-legal / claude-medical / claude-finance)
- See [Entity 3](./entity-3-domain-vertical-and-living-standards.md)

**8. NEW Pattern: Living-Domain-Standards Tracking N=1 stale-flagged**

- Agents codify external-authority quality-criteria with explicit deprecation-aware schemas + dated standards-version tracking
- 3 criteria: explicit external-authority + date / deprecation-tracking discipline / versioned absorption ledger (CHANGELOG)
- Evidence: 8 deprecation events tracked with specific dates (HowTo Sept 2023 / FAQ Aug 2023 / SpecialAnnouncement July 2025 / FID→INP March 2024 / etc.)
- Un-stale criterion: 2nd subject satisfying all 3 criteria
- See [Entity 3](./entity-3-domain-vertical-and-living-standards.md)

### Observational candidates (not formal registrations at v64) — 4 items

**9. Manifest-Drift-As-First-Class-CI-Concern (observational)**

- claude-seo's 5-version-source atomic-bump CI discipline with 13 assertions = strongest manifest-consistency observed
- Evolution: v1.8.1 first drift noted → v1.9.7 second drift → v1.9.8 first test suite → v1.9.9 13 assertions
- Pattern Library candidate consideration deferred to v66

**10. Self-Marketing Release Pipeline as Plugin Meta-Command (observational)**

- claude-seo's `/release-blog` slash command auto-publishes to claude-seo.md/blog with full SEO+indexing pipeline
- Sister to oh-my-claudecode v27 mini-blog but higher automation
- Deferred to v66

**11. Gamified-Curated Community Contribution Mechanism (observational)**

- claude-seo's Pro Hub Challenge v1.9.0 (5 named contributors from AI Marketing Hub) vs awesome-claude-skills v50 open-curation vs mattpocock v57 solo-author
- Deferred to v66

**12. Honest-Deficiency-Disclosure Discipline (observational)**

- README "Limitations" section proactively discloses SPA/CSR + links to v2.0 epic
- Compatibility/migration section in CHANGELOG v1.9.9 calls out third-party index-coupling risk
- v2 deferrals explicit 6-item list
- Deferred to v66

## v66 audit pre-registration items (consolidated from v64 ship)

Per routine v2.1 Phase 5 discipline, v66 mini-audit agenda gains:

1. **Pattern #19 ecosystem-portfolio-builder sub-type N=3 promotion deliberation** (PRIMARY — promotion-eligible)
2. **Pattern #18 Layer 1 sub-archetype consolidation**: "shared-skill-content-with-per-platform-dispatch-file" at 5-platform scale
3. **Pattern #18 Layer 2 NEW sub-archetype**: solo-author-cross-vendor-parallel-port-as-separate-repo (codex-seo)
4. **Pattern #28 credential-tier-progressive-disclosure sub-variant** consideration
5. **NEW Pattern #80 T1 domain-vertical-skill-collection** stale-check (un-stale via N=2)
6. **NEW Pattern #81 Living-Domain-Standards Tracking** stale-check (un-stale via N=2)
7. **Manifest-Drift-As-First-Class-CI-Concern** observational → candidate consideration
8. **Self-Marketing Release Pipeline Meta-Command** observational → candidate consideration
9. **Gamified-Curated Community Contribution** observational → candidate consideration
10. **Honest-Deficiency-Disclosure** observational → candidate consideration

Combined with carry-forward from v63 EARLY mini-audit (9 items) + v62 audit gap closure documentation, v66 audit agenda grows to **~20+ items**.

## Storm Bear pilot ranking update

claude-seo v64 placement in pilot ranking (`_state/pilot-ranking-2026-05-07.md`):

| Rank | Subject | Tier | Rationale |
|---|---|---|---|
| #1 | cc-sdd v61 | T1 — already completed pilot 2026-05-13 | Methodology-workflow-harness, SDD phases, adversarial review |
| #1.5 | codex-plugin-cc v62 | T1 — completed comparison-pilot 2026-05-13 | Pattern #76 architectural-vs-prompt-framing test |
| #2 | free-claude-code v60 | T1 — pending | Cost-reduction proxy, orthogonal layer |
| #3.5 | karpathy-skills v63 | T2 — pending | Behavioral-overlay orthogonal layer (Week 3+ stack-layer test) |
| **#NEW** | **claude-seo v64** | **NOT a vault pilot candidate** | **SEO-domain not vault-relevant per Phase 0.9 SKIP at v64; vault is LLM Wiki knowledge base, not marketing site; current vault state is private GitHub repo** |

claude-seo v64 **does not enter the pilot ranking** because Phase 0.9 SKIP confirmed it's not directly operational for vault Goal #2 ("build software with these tools"). It could become relevant IF vault publishes wikis publicly AND wants SEO discoverability for vault content — speculative at present.

## Cross-wiki sibling cross-references (mandatory)

All cross-wiki siblings from project CLAUDE.md are referenced in [Wiki index](./index.md). Key relationships:

- **Pattern #19 N=3 peers**: cc-sdd v61 + karpathy-skills v63
- **T1 Augmentation peers**: mattpocock-skills v57 + awesome-claude-skills v50 + agent-skills-of-vercel v51 + karpathy-skills v63
- **Multi-platform peers**: cc-sdd v61 (8 platforms framework) + karpathy-skills v63 (2 platforms single-skill)
- **Plugin marketplace peers**: codex-plugin-cc v62 + oh-my-claudecode v27 + claude-hud v35
- **MCP extension peers**: shannon v45 + aidevops v47

## Conclusion — what v64 contributes

v64 claude-seo ship contributes to the Storm Bear vault Pattern Library:

- **1 PROMOTION-ELIGIBLE candidate** (Pattern #19 ecosystem-portfolio-builder N=3 sub-type)
- **6 direct strengthenings** of existing patterns
- **2 NEW top-level candidates** N=1 stale-flagged (T1 domain-vertical / Living-Domain-Standards)
- **4 observational candidates** for v66 deliberation
- **0 Storm Bear meta-entity** (Phase 0.9 STRICT SKIP — 0 strong PASS)
- **Streak reset 4 → 0** post-v64 SKIP

It also resets the post-v60-RESTART Storm Bear meta-streak from 4 → 0, and the 9-instance post-amendment Phase 0.9 window now stands at **77.8% INCLUDE rate** (7 PASS / 2 SKIP) — calibration healthy, neither over-inclusive nor too-strict.

The wiki ship preserves the **24-streak ZERO-NEW-CANDIDATES-from-Storm-Bear-meta-entity** historical record (Storm Bear contributes to corpus via meta-observations not its own Pattern Library entries).

Phase 5 will register all 8 items + observational notes in `_patterns/05-recent-additions.md` + queue v66 audit agenda items.
