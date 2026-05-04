# (C) Cluster 2 — Contributor + Governance summary

> **Sources:** CONTRIBUTING.md + LICENSE (PolyForm Noncommercial 1.0.0) + SECURITY.md (absent, 404) + akonlabs.com commercial positioning + Discord community signals
> **Fetched:** 2026-04-23 via WebFetch
> **Role in wiki:** Governance depth + licensing economics + commercial-gate mechanism + contributor workflow

---

## 1. Governance files inventory

| File | Present? | Notable content |
|------|----------|-----------------|
| README.md | ✓ | Primary user-facing (cluster 1) |
| CONTRIBUTING.md | ✓ | Conventional-commit PR titles + AI-assisted contributions section |
| LICENSE | ✓ | PolyForm Noncommercial 1.0.0 (standard non-OSI) |
| SECURITY.md | ✗ | **Absent — notable for 28K-scale T4** (404 fetched 2026-04-23) |
| CODE_OF_CONDUCT.md | To verify | Not mentioned in README or CONTRIBUTING |
| AGENTS.md | ✗ | Not mentioned (Pattern #22 narrow-scope continuation — 3rd T4 absence after v32 claude-howto + v18 agency-agents at T1) |
| CLAUDE.md | To verify | Referenced in CONTRIBUTING "project context files" mention |

**Governance depth assessment: 3-4 files (medium-light)** — below spec-kit v17 (6 files heaviest) + markitdown v28 Microsoft corporate-depth; above TrendRadar v19 (sparse). Notable at 28.5K scale: SECURITY.md absence despite Sigstore-signed Docker + K8s supply-chain posture elsewhere (inconsistency observation).

## 2. CONTRIBUTING.md key content

### PR workflow
- **Conventional-commit format titles** required (e.g., `feat`, `fix`, `perf`)
- **Automated labeling + release-notes organization** from PR titles
- Verbatim: *"Commits within a PR may use any style — only the merged PR title shows up in release notes."*

### AI-assisted contributions section (NOTABLE)
- Advises: follow project context files (e.g., `AGENTS.md`, `CLAUDE.md`) and avoid drive-by refactors unrelated to the issue
- Incremental + test-backed changes preferred
- **NOT a formal AI-disclosure policy** (distinct from spec-kit v17 mandatory AI-disclosure; Pattern #23 was retired v27)
- **NOT explicit Agent-PR Fast-Track protocol** (distinct from awesome-mcp-servers v31 `🤖🤖🤖` title suffix; Pattern #69 N=1 candidate)
- **Middle-ground AI-posture** — acknowledges AI contribution without formal process

### Absences
- **No CLA requirement** mentioned — developer-friendly (contrast Microsoft CLA at markitdown v28)
- **No Code of Conduct** referenced — missing for 28.5K project (governance-depth gap)
- **No contributor-ladder / reviewer-role hierarchy** — flat contribution model

## 3. LICENSE — PolyForm Noncommercial 1.0.0 (DETAILED)

### Source
- Standard license from polyformproject.org
- Version 1.0.0 (not custom-written)
- File at root: `LICENSE` (not LICENSE.md)

### Permitted uses (free of charge)
- **Any noncommercial purpose**
- **Personal uses:** research, experiment, testing for benefit of public knowledge; hobby projects; amateur pursuits
- **Organizational uses:** charities, educational institutions, government bodies (regardless of funding source)
- **Key qualifier:** absence of "anticipated commercial application"

### Commercial use (NOT permitted without separate agreement)
- License does not address commercial licensing options within its text
- Users requiring commercial use must contact licensor separately
- GitNexus commercial path: **akonlabs.com** (founders@akonlabs.com)

### Patent provisions
- **Patent license INCLUDED** — licensor grants patent license for claims covering software usage
- **Termination clause:** patent license terminates immediately if licensee claims software infringes any patent

### Output + derivative works
- Derivative works permitted under noncommercial purposes
- **Cannot sell** software built on this code (commercial distribution prohibited)
- Licensor retains rights to license software to others independently

### Restrictions
- No sublicensing or transfer of licenses

### Structural comparison with prior corpus non-permissive licenses

| License | Corpus wiki | Type | Commercial path |
|---------|-------------|------|-----------------|
| GPL-3.0 | TrendRadar v19 (CN content) + system-prompts-leaks v21 | Copyleft OSI | Source-disclosure downstream |
| AGPL-3.0 | Unsloth Studio UI v23 + Skyvern v24 | Network-copyleft OSI | Source-disclosure for network services |
| Custom non-OSI (Fish Audio Research) | fish-speech v20 | Custom research-only | Commercial license via 39 AI, INC. |
| **PolyForm Noncommercial 1.0.0** | **GitNexus v33** | **Standard non-OSI commercial-gate** | **Commercial license via akonlabs.com** |
| MIT + separate enterprise directory | OpenHands v30 | MIT + proprietary enterprise bundle | Enterprise bundle separate |

**GitNexus introduces STANDARDIZED non-OSI commercial-gate license family** — distinct from:
- Copyleft (distribute requires source) — GPL / AGPL
- Custom research-only (bespoke written) — fish-speech
- Permissive-plus-enterprise (MIT core + separate enterprise) — OpenHands

PolyForm = structured-standard non-OSI family with several variants (Noncommercial / Small Business / Shield / Strict). Choice signals deliberate commercial-gate architecture using a proven standard rather than custom legal writing.

## 4. SECURITY.md absence (notable)

- GitHub 404 at `/main/SECURITY.md`
- **NOTABLE at 28K-scale T4 with supply-chain posture:** README documents Sigstore-signed Docker + Kubernetes policy-controller enforcement
- **Inconsistency observation:** sophisticated supply-chain TOOLING without formal vulnerability-disclosure DOCUMENTATION
- **Pattern #24 SECURITY.md as T1 Standard (CONFIRMED v18)** — T1-specific pattern; T4 absence not counter-evidence
- **Potential narrow-scope refinement:** SECURITY.md T1-vs-T4 divergence — T4 tools may embed security via tooling rather than documentation

## 5. akonlabs.com commercial entity

### Positioning
- **Website:** akonlabs.com
- **Contact:** founders@akonlabs.com (plural — team, not solo)
- **Discord (commercial):** discord.gg/AAsRVT6fGb (separate from community Discord MgJrmsqr62)
- **README verbatim:** *"Enterprise (SaaS & Self-hosted) - akonlabs.com"*

### Enterprise tier features (delta from OSS)
Per README "Enterprise" mentions:
- **PR Review** — automated code review on pull requests (GitNexus OSS doesn't include)
- **Auto-updating code wiki** — continuous refresh vs manual re-index in OSS
- **Auto-reindexing** — event-driven graph updates vs manual in OSS
- **Multi-repo support** — (note: OSS has group operations; Enterprise may expand)
- **OCaml support** — additional language beyond 14 in OSS
- **Priority feature requests** — commercial-support entitlement

### Commercial-model architecture
- **Open-core** via PolyForm license gate:
  - OSS core: permitted for noncommercial use (Pattern #31 N=4 data point)
  - Commercial usage: requires akonlabs.com agreement
- **Companion-platform** distinct from (VoltAgent + getdesign.md at v25 / Fiegel + Glama at v31 — Pattern #50 CONFIRMED):
  - GitNexus akonlabs is CLOSED Enterprise tier of SAME product (open-core)
  - NOT separate commercial platform (like getdesign.md separately-branded alongside awesome-design-md)
  - **Cleaner open-core boundary** than getdesign.md companion-platform architecture
- **4 distinct open-core approaches now observed in corpus:**
  1. Custom research-only license + separate commercial license (fish-speech v20 → 39 AI, INC.)
  2. AGPL-3.0 + cloud proprietary features (Skyvern v24)
  3. MIT + separate in-repo enterprise-directory (OpenHands v30)
  4. **Standard non-OSI PolyForm Noncommercial + separate commercial agreement (GitNexus v33 → akonlabs.com)**

## 6. Discord + community signals

- **Community Discord:** discord.gg/MgJrmsqr62 — *"discuss ideas, issues etc!"* (verbatim README)
- **Commercial Discord:** discord.gg/AAsRVT6fGb (Enterprise inquiries)
- **Member counts:** not disclosed (Discord badge in README shows member count pulled live)
- **Separation signals maturity:** paid customers in separate channel from OSS discussion

## 7. Author contribution profile

- **abhigyanpatwari:** 20 public repos, 444 followers, following 5 (selective)
- **Bio:** *"CS student & AI engineer who likes to dig into the guts of systems. If it's interesting, I'll probably try to build something with it."*
- **NOT ecosystem-layer-individual archetype** (contrast safishamsi/penpax.ai v16 with graphify + penpax.ai + related tools; contrast luongnv89 v32 with 15+ companion repos including sleek-ui / skills / context-stats / asm / ccl; contrast Yeachan v27 with oh-my-claudecode + oh-my-codex sibling)
- **Single-flagship-project-with-commercial-company variant** — Abhigyan's other repos appear tangential/exploratory; primary contribution is GitNexus + akonlabs commercial
- **Cross-reference to Pattern #17 variant refinement candidate** at next audit

## 8. Governance-depth summary (Pattern #12 correlation)

**Pattern #12 Governance Depth Correlates with Organization** (CONFIRMED v13) states: corporate = heavy / solo = lighter. GitNexus:
- **Solo-student-author + commercial-entity** = hybrid
- **Governance depth: medium-light** (3-4 files; CONTRIBUTING + LICENSE + absent SECURITY + absent CODE_OF_CONDUCT)
- **Continues Pattern #12 correlation:** solo-student depth lighter than corporate (markitdown v28 Microsoft CLA + COC + Security Considerations + Devcontainer = heavy corporate); though commercial-company presence could push toward corporate-style
- **Observation:** akonlabs commercial entity has NOT yet pushed governance to corporate-depth. Suggests commercial-entity maturity affects OSS-repo governance depth (early-stage commercial entity = OSS stays solo-style).

## 9. AI-assisted contributions posture

### Corpus state before v33
- **spec-kit v17** — FIRST formal AI-disclosure policy. Pattern #23 registered N=1, RETIRED v27 audit (no 2nd observation over 10 wikis)
- **awesome-mcp-servers v31** — `🤖🤖🤖` title suffix Agent-PR Fast-Track. Pattern #69 N=1 stale-risk-flagged v31
- **claude-howto v32** — CONTRIBUTING.md lacks AI-disclosure DESPITE being ABOUT Claude Code (strengthens Pattern #23 retirement rationale)

### GitNexus v33 position
- **Middle-ground:** CONTRIBUTING mentions AI-assisted contributions with informal guidance (follow context files + incremental changes) but NO formal disclosure policy or fast-track protocol
- **NOT new data point for Pattern #23** (which is retired)
- **NOT new data point for Pattern #69** (which requires EXPLICIT protocol like `🤖🤖🤖`)
- **Signals informal-AI-acceptance position** — acknowledges AI contribution without formal process; may be emerging norm

## 10. Supply-chain posture

### Positive signals (sophisticated)
- **Sigstore-signed Docker images** (Cosign keyless)
- **Kubernetes policy-controller** enforcement available
- **Supply-chain signing** — first in corpus documented at deployment level

### Negative signals (missing foundation)
- **No SECURITY.md** (vulnerability-disclosure channel undocumented)
- **No CODE_OF_CONDUCT** (community-behavior policy absent)
- **No AGENTS.md** (agent-context protocol absent)

**Interpretation:** Author prioritizes INFRASTRUCTURE-level supply-chain (Sigstore, K8s) over DOCUMENTATION-level governance (SECURITY.md). Typical of solo-engineer preference; commercial-entity akonlabs may push documentation-level later.

## 11. Cross-wiki observations

- **Pattern #12 Governance Depth (CONFIRMED v13)** — solo-student-author with commercial-entity = governance-light; pattern correlation holds
- **Pattern #24 SECURITY.md as T1 Standard (CONFIRMED v18)** — T4 absence continues (graphify v16 had SECURITY.md as T4 first; GitNexus doesn't); narrow-scope observation
- **Pattern #22 AGENTS.md Industry Standard (CONFIRMED v17)** — 3rd T4 absence (claude-howto v32 + GitNexus v33 both absent); potential T1/T4 divergence or meta-framework-specificity
- **Pattern #31 Open-Core Commercial Entity (CONFIRMED v24)** — **4th data point** (N=4; PolyForm standardized non-OSI commercial-gate approach)
- **Pattern #50 Commercial-Funnel Companion Platform (CONFIRMED v31 mini-audit)** — GitNexus is NOT companion-platform (OSS + Enterprise are SAME product); distinguishes #31 (open-core) vs #50 (companion-platform) cleanly
- **Pattern #23 AI-Disclosure Policy (RETIRED v27)** — CONTRIBUTING mentions AI-contribution informally; not revival trigger (retirement intact)
- **Pattern #69 Agent-PR Fast-Track (candidate v31, N=1 stale-risk)** — no formal Agent-PR protocol; not 2nd data point

## 12. Supply-chain awareness protocol (v2.1)

GitNexus consumes untrusted code as INPUT (indexed repos are user's OR external). Supply-chain risk SURFACE:
- **User-directed:** user indexes their own repos → low risk (user trusts own code)
- **Cross-repo:** user indexes external repos → low-medium risk (static analysis only; no execution)
- **MCP server output:** AI agents consume GitNexus's structured output → supply-chain INFERENCE risk (if GitNexus classifies malicious code as safe, downstream agent decisions affected)

**Risk framing:** similar to crawl4ai v29 (static analysis of external content) but LESS severe than awesome-mcp-servers v31 (1,200 MCP servers trust boundaries). Pattern #66 OBSERVATION-TRACK (supply-chain incident response) applicable framing.

## 13. Next cluster — Technical-distribution

Tech stack deep-dive (Tree-sitter + LadybugDB + Graphology + transformers.js + Sigma.js + MCP) + deployment modes + 16 MCP tools detail + 5 editor integrations + 14-language detail + Kubernetes Sigstore supply-chain.
