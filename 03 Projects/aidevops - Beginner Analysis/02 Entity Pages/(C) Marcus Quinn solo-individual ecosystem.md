# (C) Marcus Quinn — solo-individual ecosystem (Pattern #17 variant 1 18th data point)

**Entity type:** Individual author + ecosystem-portfolio
**Real name:** Marcus Quinn
**GitHub handle:** `marcusquinn`
**Location:** Jersey (Channel Islands, UK Crown Dependency)
**Bio (verbatim):** *"Open-Source wins. You can't lose what you give freely. Knowledge shared, multiplies."* + *"Shipping with AI agents around the clock — human hours for thinking, machine hours for doing."*

## Profile signals

| Signal | Value | Corpus comparison |
|---|---|---|
| Personal website | https://www.marcusquinn.com | Active personal brand site |
| Twitter / X | `@marcuswquinn` | Active |
| LinkedIn | `in/marcusquinn` | Active |
| Followers | 45 | Low individual following |
| Following | 28 | Low engagement |
| Public repos | 20 | Senior-dev signal |
| Top-pinned flagship (pre-aidevops) | `git-updater` (3,300 stars / 471 forks; PHP) | **8-year prior OSS track record at scale** — pre-aidevops senior-dev signal |
| Current flagship (this wiki) | `aidevops` (212 stars; Shell) | 5.5-month-old |
| Affiliations | `@evergreenjersey` / `@awardsapp` / `@wpallstars` | Multiple brand affiliations (Jersey environmental org / awards platform / WordPress community) |
| Commercial positioning | `aidevops.sh` dedicated domain + `marcus@aidevops.sh` | Brand-positioning at flagship scope |

**Senior-dev profile, NOT first-time builder.** Marcus's `git-updater` (WordPress plugin update tool, 3,300 stars / 471 forks) predates aidevops by ~8 years and represents the prior flagship. aidevops is the **current pivot to AI agent operations** by an established WordPress/PHP senior dev.

## Pattern #17 variant 1 solo-individual-multi-publisher 18th data point

**20 public repos** with documented ecosystem interconnection:

| # | Repo | Stars | Forks | Lang | Aidevops integration |
|---|---|---|---|---|---|
| 1 | **aidevops** | **212** | 39 | Shell | (this wiki) |
| 2 | **opencode** | (forked) | (forked) | TypeScript | Forked from `anomalyco/opencode`; Marcus contributing back to OpenCode platform |
| 3 | **wp-plugin-starter-template-for-ai-coding** | 15 | 5 | Shell | WordPress plugin starter optimized for AI coding |
| 4 | **git-updater** | **3,300** | 471 | PHP | Pre-aidevops flagship; WordPress plugin auto-update tool |
| 5 | **amazon-order-history-csv-download-mcp** | 4 | (low) | TypeScript | **First-class MCP in aidevops** (per-agent tier) |
| 6 | **quickfile-mcp** | 3 | 2 | TypeScript | **First-class MCP in aidevops** (Accounts domain agent) |
| 7-20 | (other public repos; not pinned) | — | — | — | Various WordPress / Jersey community / utilities |

**Ecosystem-layer playbook (corpus comparison):**

| Author | Pattern | Description |
|---|---|---|
| **Marcus Quinn (v47)** | **Vertical integration** — owns MCPs + framework + commercial site | Self-published MCPs (amazon-order-history / quickfile) consumed inside owned framework (aidevops) on owned commercial site (aidevops.sh) |
| **Frank Fiegel (v31 awesome-mcp-servers)** | **Curator + framework + commercial companion** | Aggregates third-party MCPs into directory + ships own framework (fastmcp) + commercial Glama platform |
| **VoltAgent (v25 awesome-design-md)** | **Aggregator + parent framework + commercial platform** | Curates third-party DESIGN.md files + ships parent voltagent framework + getdesign.md commercial site |
| **HuggingFace (v26 agents-course)** | **Ecosystem-scale corporate platform** | Hosts OSS framework (smolagents) + course platform + Hub + Spaces |

**Aidevops is third corpus example of solo-individual-with-ecosystem-portfolio archetype:**
- Multi-repo solo publisher
- Ecosystem-internal cross-pollination (own MCPs feed own framework)
- Commercial-positioning layer (aidevops.sh) without paid SaaS tier
- Pre-existing OSS track record (git-updater 3,300 stars × 8 years) signaling senior-dev maturity

## Pattern #20 Solo-Scale Ceiling — NEW T1 row

| Author archetype | Scale signal | Time | Sub-archetype |
|---|---|---|---|
| (Various solo T1 authors v1-v36) | (Various scales 5K-90K) | (varies) | (varies) |
| Marcus Quinn (v47 aidevops) | **212 stars / 5.5 months / ~2,665 primitives / commercial-positioning** | 5.5 months | **NEW: solo-individual + 8-year-prior-OSS-flagship + cross-domain-multi-agent + commercial-positioning + cold-start-stars-but-mature-framework-surface** |

This row distinguishes from:
- **bizos v37** (Alex Le, 18 stars at 2 days, NO mature surface, NO prior OSS history visible)
- **agency-agents v18** (msitarzewski, 82,900 stars solo, viral-Reddit path, 144 personality-driven agents)
- **claude-howto v32** (luongnv89, 28,186 stars in 5.5 months, sustained-organic-amplified, Boris-Cherny lineage)

**aidevops occupies novel point in Pattern #20 sub-axis space:** mature-framework-surface (~2,665 primitives) + cold-start-stars (212) + commercial-positioning + senior-dev-prior-flagship.

## Pattern #19 archetype 2 methodology-lineage — multi-source strongest-evidence wiki

**5+ external methodology citations** documented in CREDITS.md + README:

| Source | Type | aidevops integration |
|---|---|---|
| **Lance Martin (LangChain)** | Agent design patterns thinker | 16-pattern table mapped to aidevops implementations (README §"Agent Design Patterns"; x.com/RLanceMartin/status/2009683038272401719) — **CORPUS-FIRST Lance Martin citation** |
| **anomalyco/Claude** | Prompt template | `build.txt` system prompt derived from `anthropic.txt @ 3c41e4e8f12b` |
| **imbue-ai/mngr** (MIT) | Agent process management patterns | Ratchet pattern (`ratchets.json`) + structured code-review categories + tmux/provider/idle-detection (research input for SaaS agent hosting); CREDITS.md notes "mngr manages agent processes; aidevops manages agent intelligence and workflow. Complementary, not competing." |
| **Google Stitch** | DESIGN.md spec | Methodology + format + usage docs cited |
| **VoltAgent/awesome-design-md** | Brand DESIGN.md library | 55 brand examples imported into `.agents/tools/design/library/brands/` (**Pattern #57 4th data point — v25 wiki subject**) |
| **dominikmartn/nothing-design-skill** | Design skill | `.agents/tools/ui/nothing-design-skill/` |
| **shadcn/ui** | Component library | `.agents/tools/ui/shadcn.md` |
| **ui-skills.com** | LLM rules constraints | `.agents/tools/ui/ui-skills.md` |

**Multi-source lineage = strongest evidence in corpus for Pattern #19 archetype 2 methodology-lineage diversity.**

**Lance Martin enters Pattern #19 archetype 2 individual-influence-node graph as 4th node** alongside:
1. **Andrej Karpathy** (5+ corpus touchpoints — autoresearch v10 / LLM Wiki pattern foundation / graphify v16 inspired-by / Ollama v46 cross-corpus citation / rowboat v43 implicit structural parallel)
2. **John Lam (jflam)** (1 corpus touchpoint — spec-kit v17 explicit "heavily influenced by and based on the work and research of John Lam (jflam)")
3. **Anthropic team cluster** (Boris Cherny + Dex Horthy + Cat Wu — claude-howto v32 + claude-code-best-practice v34 — 4+ touchpoints)
4. **Lance Martin (LangChain)** ⬅️ NEW at v47 — 16-pattern documented map; aidevops first corpus subject citing

**Pattern #19 archetype 2 4-individual-influence-node-graph CORPUS-COMPLETE at v47.**

## TOON format (aidevops-originated)

aidevops claims authorship of **TOON (Token-Oriented Object Notation)** — token-efficient serialization format with 20-60% reduction vs JSON/YAML.

Used for:
- `subagent-index.toon` (900+ agent routing table)
- Mailbox / agent registry (TOON format)
- TODO.md TOON-enhanced parsing (since v3.x)

Spec: `.agents/toon-format.md` (in-repo; not separately published).

**Pattern #19 observation:** aidevops is **originator** of TOON (not lineage citation). Distinct from prior corpus subjects which cite external methodologies.

**Future Pattern #57 watch:** if other corpus subjects adopt TOON, aidevops becomes upstream node in cross-corpus citation graph (parallel to LlamaFactory v22 → dive-into-llms v39 chapter 9).

## Storm Bear operator-relevance signals

**Author archetype matches:**
- ✅ Senior solo dev with prior OSS flagship (Storm Bear operator = Scrum coach with prior product/dev career)
- ✅ Cross-domain breadth (13 domains in aidevops; Storm Bear has multi-service offering: Scrum / development / Coaching)
- ✅ Commercial-positioning + open-source layer (Storm Bear vault = personal OS; pilot of going commercial possible)
- ✅ AGENTS.md-authoritative governance pattern = template for Storm Bear vault refactor
- ⚠️ Jersey UK + WordPress prior + PHP/Bash polyglot ≠ direct Storm Bear (VN-context Scrum coach)
- ⚠️ OpenCode-first design = friction for Claude-Code-primary Storm Bear

**Mid-friction adoption pathways for Storm Bear:**
1. Adopt **AGENTS.md-authoritative + CLAUDE.md-shim pattern** for vault (closes v27 diagnostic HIGH item #1)
2. Adopt **8-tool quality stack** (Codacy + CodeFactor + Sonar + Qlty + CodeRabbit + Bandit + secretlint + ShellCheck) on vault repo independently
3. Adopt **TOON format** for vault subagent-index without aidevops infrastructure
4. Adopt **Lance Martin 16-pattern checklist** as Storm Bear vault skill audit framework

## Cross-references

- **Pattern #17** Ecosystem-Layer variant 1 — 18th data point
- **Pattern #19** archetype 2 methodology-lineage — Lance Martin 4th individual-influence-node + multi-source strongest-evidence wiki
- **Pattern #20** Solo-Scale Ceiling — NEW T1 row "cold-start-with-mature-framework-surface"
- **Pattern #57** Recursive Corpus Reference — 4th data point (CREDITS.md cites v25 wiki subject + Google Stitch v25 referenced)
- See **(C) aidevops core product**
- See **(C) Cluster C — Marcus Quinn ecosystem + OpenCode-first + commercial positioning**

---

*(C) Generated by Claude — Marcus Quinn ecosystem entity for v47 aidevops*
