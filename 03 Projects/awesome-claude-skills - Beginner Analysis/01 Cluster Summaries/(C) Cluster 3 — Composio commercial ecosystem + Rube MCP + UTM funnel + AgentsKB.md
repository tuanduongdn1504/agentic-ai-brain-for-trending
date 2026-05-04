# (C) Cluster 3 — Composio commercial ecosystem + Rube MCP + UTM funnel + AgentsKB

**Source**: README references + plugin manifests + composio-skills wrapper catalog + GitHub org metadata

**Wiki**: v50 awesome-claude-skills | **Cluster**: 3 of 3

---

## Cluster scope

The commercial ecosystem this aggregator funnels users into. The aggregator is not just curation — it's lead-generation infrastructure for Composio Inc.'s commercial product line. This cluster maps that line.

---

## Composio Inc. organizational profile

| Field | Value |
|-------|-------|
| GitHub org | `ComposioHQ` |
| Created | 2023-03-21 (~3 years old) |
| Tagline | *"Composio equips agents with well-crafted tools empowering them to tackle complex tasks"* |
| Homepage | composio.dev |
| Public repos | 70 (large org-ecosystem; corpus-strongest variant 3 single-org evidence at v50) |
| Followers | 1,649 |
| Email | hello@composio.dev / support@composio.dev / tech@composio.dev (3 distinct addresses) |
| HQ | Likely US (no explicit location disclosed) |

---

## Commercial product line (5 surfaces)

1. **Composio platform** — `platform.composio.dev`
   - Core SaaS product
   - "Get Started Free" UTM-tracked CTA at README footer (`?utm_source=Github&utm_content=AwesomeSkills`)
   - Consumer-facing signup surface

2. **Composio dashboard** — `dashboard.composio.dev`
   - Authenticated user dashboard
   - API key issuance surface (Quickstart: "Paste API key from dashboard.composio.dev")
   - UTM banner at README top (`?utm_source=Github&utm_medium=Youtube&utm_campaign=2025-11&utm_content=AwesomeSkills`)
   - **Banner is line 4-6 of README** — first element above tagline

3. **Composio toolkits catalog** — `composio.dev/toolkits`
   - 1000+ apps integrated (claim per README Quickstart "500+ apps" + "1000+ apps" — number varies)
   - Per-toolkit docs (e.g., `composio.dev/toolkits/slackbot`, `composio.dev/toolkits/gmail`, etc.)
   - Each composio-skills entry references `composio.dev/toolkits/<toolkit-name>`

4. **Rube MCP** — `https://rube.app/mcp`
   - Composio's MCP-server endpoint
   - Pricing model unstated in README (claim: "No API keys needed — just add the endpoint and it works" — but Quickstart contradicts this by requiring API key from dashboard.composio.dev)
   - Tool namespace: `RUBE_*` (RUBE_SEARCH_TOOLS, RUBE_MANAGE_CONNECTIONS)
   - **832 of 864 in-repo SKILL.md files (96.3%) declare `requires: mcp: [rube]`** — Rube MCP is the fulfillment-runtime for the entire automation catalog

5. **AgentsKB** — `agentskb.com`
   - Sister product mentioned at README footer
   - Tagline: *"Upgrade your AI with researched answers. We did the research so your AI gets it right the first time."*
   - Out of scope for v50 wiki — flagged as follow-up deep-dive

---

## UTM-tracking analysis

3 distinct UTM campaigns observed in single README (corpus-strongest UTM observation):

| URL | utm_source | utm_medium | utm_campaign | utm_content |
|-----|-----------|------------|--------------|-------------|
| dashboard.composio.dev/login (banner) | Github | **Youtube** | 2025-11 | AwesomeSkills |
| dashboard.composio.dev/login (Quickstart) | Github | — | — | AwesomeSkills |
| platform.composio.dev (footer CTA) | Github | — | — | AwesomeSkills |

**Anomaly**: banner URL claims `utm_medium=Youtube` despite being placed in a GitHub README. This signals either:
- Cross-channel campaign attribution (Composio drives YouTube viewers to GitHub README → which then attributes downstream conversions back to YouTube origin), OR
- Stale UTM parameter from a banner asset reused across channels.

Either way, the level of marketing-attribution sophistication embedded in the README is **the corpus-strongest commercial-funnel discipline observed across 50 wikis**.

---

## Community channels

- **Discord** — discord.com/invite/composio
- **X (Twitter)** — @composio
- **LinkedIn** — companies/composiohq
- **Email** — hello@composio.dev / support@composio.dev / tech@composio.dev
- **Composio community** — referenced as "20,000+ developers" (unverified)

---

## Pattern observations from cluster 3

| Pattern | Observation in cluster 3 |
|---------|--------------------------|
| **#50 Commercial-Funnel Companion** | **N=9 corpus-strongest data point**. 5-surface commercial product line + 3 distinct UTM campaigns + Quickstart-pushes-signup + 96.3% of skills require commercial product to function. Sub-variant: **aggregator-as-marketing-attribution-channel** (UTM tracking from GitHub README to dashboard signup). |
| **#17 variant 3 commercial-startup ecosystem** | Composio = strongest variant-3 evidence at v50 (70 public repos + 5 commercial surfaces + 3-year operational history + sister product AgentsKB). |
| **#19 archetype 4 no-individual-lineage** | Org-only branding; no founder citations; no individual-author lineage. Consistent with corporate-startup positioning. |
| **#27 Community-Viral Scale Path** | Aggregator-amplified-commercial-viral sub-path: 56K stars / ~6 months ≈ 9.4K/month. Commercial entity using OSS aggregator as community-acquisition channel. |
| **#18 MCP layer 1** | Rube MCP = corpus-first commercial-MCP-server observation at scale (832 skills require it). MCP-as-commercial-runtime sub-observation. |
| **#22 AGENTS.md absence** | Composio's 70-repo ecosystem — would be useful future check whether OTHER Composio repos have AGENTS.md (since aggregator-genre absence might be genre-specific not org-specific). Out of scope for v50. |

---

## Cross-references

- See `Cluster 1` for README surface where UTM links are placed.
- See `Cluster 2` for in-repo skill catalog that funnels into commercial product.
- See `02 Entity Pages/(C) Composio Commercial Ecosystem + Rube MCP + Pattern #50 Corpus-Strongest.md` for synthesized commercial entity.
- Pattern Library `PATTERN_LIBRARY.md` Pattern #50 — strengthen to N=9 with this v50 data point.

---

## Open questions / verification flags

- **Rube MCP pricing**: Free tier exists (Quickstart implies free signup); paid tiers unstated in this aggregator. Investigation requires direct visit to platform.composio.dev pricing page (out of scope for v50).
- **Composio funding stage**: Not disclosed in this repo; would require separate research.
- **AgentsKB business model**: Sister-product positioning unclear — separate startup? Spin-off? Different product line under same Composio Inc.? Out of scope for v50.
- **VN/non-EN market presence**: Composio appears EN-only across all surfaces visible in this repo (README EN; Discord/X/LinkedIn EN). No localization observed.

---

## Operator-relevance note (Storm Bear context)

**For Storm Bear operator considering Composio Rube MCP for Scrum-coach automation**:
- Rube MCP would in principle wire Storm Bear to Jira/Linear/Slack/Gmail/Calendar via 70+ pre-built skills — high theoretical utility.
- BUT: 832 wrappers + commercial dependency + UTM-tracking-density signals **aggressive commercial-funnel-first positioning**. Operator should evaluate Rube MCP cost + data-residency policy + VN compliance before client-facing deployment.
- Lower-friction alternative: clone 5-10 specific in-repo top-level skills (file-organizer, content-research-writer, meeting-insights-analyzer, etc.) that DON'T require Rube MCP — these are zero-commercial-coupling.
- See `03 Beginner Guide` for skill-shopping pilot table.
