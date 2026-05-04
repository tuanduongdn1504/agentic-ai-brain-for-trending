# (C) Composio Commercial Ecosystem + Rube MCP + Pattern #50 Corpus-Strongest

**Type**: Organizational entity (commercial-startup-ecosystem)
**Wiki**: v50 awesome-claude-skills
**Pattern Library role**: **Pattern #50 N=9 — corpus-strongest commercial-funnel observation across 50 wikis**

---

## Identity

**Composio Inc.** (`ComposioHQ` on GitHub) — US-based commercial AI tool infrastructure startup. Tagline: *"Composio equips agents with well-crafted tools empowering them to tackle complex tasks"*.

| Field | Value |
|-------|-------|
| GitHub org | ComposioHQ |
| Org created | 2023-03-21 (~3 years operational) |
| Public repos | 70 (corpus-strongest variant-3 single-org evidence at v50) |
| Followers | 1,649 |
| Domains | composio.dev, dashboard.composio.dev, platform.composio.dev, rube.app, agentskb.com (sister) |
| Email | hello@composio.dev / support@composio.dev / tech@composio.dev |
| Community | Discord (composio) + X (@composio) + LinkedIn (companies/composiohq) |
| Marketing claim | "20,000+ developers building agents that ship" (unverified) |

---

## Commercial product line — 5 surfaces

### 1. Composio platform (`platform.composio.dev`)
- Top-level commercial SaaS surface
- README footer CTA: "Get Started Free" (UTM-tracked: `?utm_source=Github&utm_content=AwesomeSkills`)

### 2. Composio dashboard (`dashboard.composio.dev`)
- Authenticated user dashboard
- API key issuance for `connect-apps-plugin`
- README banner UTM target (`?utm_source=Github&utm_medium=Youtube&utm_campaign=2025-11&utm_content=AwesomeSkills`)
- **Banner positioned line 4-6 of README** — first element above tagline

### 3. Composio toolkits catalog (`composio.dev/toolkits`)
- 1000+ apps integrated (claim per README)
- Per-toolkit docs accessed via `composio.dev/toolkits/<toolkit-name>`
- Each composio-skills entry references the corresponding toolkit doc URL

### 4. Rube MCP (`https://rube.app/mcp`)
- Composio's MCP-server endpoint
- Tool namespace: `RUBE_*` (RUBE_SEARCH_TOOLS, RUBE_MANAGE_CONNECTIONS)
- 832 of 864 in-repo SKILL.md files (96.3%) declare `requires: mcp: [rube]`
- README claims "No API keys needed — just add the endpoint and it works" — but Quickstart contradicts this by requiring a key from dashboard.composio.dev. Likely free-tier with API key; paid tiers behind dashboard.

### 5. AgentsKB (`agentskb.com`) — sister product
- Mentioned at README footer: *"Upgrade your AI with researched answers. We did the research so your AI gets it right the first time."*
- Out-of-scope deep-dive flagged for v2.2

---

## UTM-tracking analysis — corpus-strongest commercial-funnel discipline

3 distinct UTM-tracked links in single README:

| URL | Position | utm_source | utm_medium | utm_campaign | utm_content |
|-----|----------|-----------|------------|--------------|-------------|
| dashboard.composio.dev/login | Banner (line 4-6) | Github | **Youtube** | 2025-11 | AwesomeSkills |
| dashboard.composio.dev/login | Quickstart | Github | — | — | AwesomeSkills |
| platform.composio.dev | Footer CTA | Github | — | — | AwesomeSkills |

**Cross-channel attribution observed**: banner sets `utm_medium=Youtube` despite living on GitHub README. Two interpretations:
- Composio drives YouTube viewers to the GitHub README, which then attributes downstream conversions back to YouTube origin (intentional cross-channel attribution).
- OR: stale UTM parameter from a banner asset reused across channels.

Either way, **this level of attribution sophistication is the corpus-strongest commercial-funnel discipline observed across 50 wikis**.

---

## Pattern #50 N=9 strengthening — comparison across 9 data points

| Wiki | Commercial entity | Companion platform | Funnel surfaces | Notes |
|------|------------------|--------------------|-----------------|-------|
| getdesign.md (v25) | VoltAgent | getdesign.md | 1 | Initial N=1 observation |
| Frank Fiegel (v31) | Glama | glama.ai/mcp/servers + Glama Chat | 2 | Reaches structurally-unambiguous N=2 |
| Browser-Use Cloud (v41) | Browser-Use Inc | cloud.browser-use.com + browsermerch | 2 | 4th data point |
| Browser-Use Cloud (v41 sub) | Browser-Use Inc | AGENTS.md-embedded LLM upsell | 1 | sub-variant observed |
| claude-context (v40) | Zilliz | Zilliz Cloud Serverless + dashboard | 1 | UTM-tracked (corpus-first observable conversion-tracking) |
| Keygraph shannon (v45) | Keygraph | Tower vCISO service + Shannon Pro | 3 | comprehensive funnel; SOC 2 Type I |
| Ollama Cloud (v46) | Ollama, Inc. | Pro/Max tiers + integration-driven funnel | 3 | upsell embedded inside `ollama launch` |
| ruflo (v42) | Cognitum.One | Flow Nexus + Agentics Foundation | 3 | 3-layer commercial structure |
| **awesome-claude-skills (v50)** | **Composio Inc.** | **5 surfaces + 3 UTM campaigns + 832 wrappers require commercial signup** | **5+** | **CORPUS-STRONGEST funnel** |

**v50 sub-variant observations within Pattern #50**:
- **"commercial-product-as-fulfillment-layer-for-aggregated-skills"** — Rube MCP fulfills 832 of 864 skills; without it the catalog is non-functional. Corpus-first.
- **"aggregator-as-marketing-attribution-channel"** — UTM tracking from GitHub README to dashboard signup. Corpus-first observable cross-channel attribution.
- **"commercial-product-entry-as-bundled-skill"** — `connect-apps-plugin/` ships INSIDE the OSS aggregator as a Claude Code plugin manifest pointing to dashboard.composio.dev signup. Corpus-first.

---

## Pattern #17 variant 3 commercial-startup ecosystem strengthening

Composio = **strongest variant-3 single-org evidence at v50** (~19th data point overall in Pattern #17).

Variant-3 fitness criteria:
- ✅ Commercial-startup positioning (Composio Inc.)
- ✅ Multiple OSS repos (70 public repos)
- ✅ Commercial product line (5 surfaces: platform / dashboard / toolkits / Rube MCP / AgentsKB)
- ✅ Aggregator-as-lead-gen tooling (this repo)
- ✅ Multi-channel community (Discord + X + LinkedIn)
- ✅ Sister-product expansion (AgentsKB.com)

70 public repos > prior variant-3 single-org examples in corpus. Composio appears at v50 as the **strongest single commercial-startup ecosystem observation** within variant 3.

---

## Composio commercial-funnel transparency for Storm Bear operator

**Operator deserves to know**:
1. The Quickstart's first action (install `connect-apps-plugin`) routes user to dashboard.composio.dev signup within 4 commands.
2. 96.3% of in-repo skills (832 of 864) require Rube MCP commercial product to function.
3. UTM tracking is sophisticated enough to attribute YouTube → GitHub README → dashboard signup conversions.
4. Apache-2.0 README claim is not backed by a LICENSE file at root (only 9 of 31 top-level skills carry verifiable LICENSE.txt).
5. Free-tier likely exists (Quickstart implies free signup) but pricing for production / commercial use is not documented in this repo.

**Recommendation for Storm Bear operator**:
- ✅ Clone + copy 5 zero-commercial-coupling top-level skills (file-organizer / content-research-writer / meeting-insights-analyzer / changelog-generator / tailored-resume-generator) for vault automation.
- ⚠️ AVOID `connect-apps-plugin` and `composio-skills/*-automation/` until explicit Rube MCP cost / data-residency / VN-compliance evaluation.
- ⚠️ For commercial / client-facing use of any skill from this repo, treat the 22 unlicensed Composio-built skills + 832 unlicensed wrappers as "all rights reserved" until Composio adds a root LICENSE file or per-skill licenses.

---

## Cross-references

- `01 Cluster Summaries/(C) Cluster 3` — Composio commercial ecosystem detail
- `02 Entity Pages/(C) awesome-claude-skills — Aggregator Core + Pattern #68 N=4.md` — aggregator surface that funnels into commercial ecosystem
- `02 Entity Pages/(C) Composio In-Repo Skill Library + 832-Wrapper Catalog.md` — in-repo content that the commercial product fulfills
- Pattern Library `PATTERN_LIBRARY.md` — Pattern #50 strengthens to N=9 corpus-strongest with this v50 data point
- Pattern Library — Pattern #17 variant 3 strengthens to ~19th data point with this v50 data point
