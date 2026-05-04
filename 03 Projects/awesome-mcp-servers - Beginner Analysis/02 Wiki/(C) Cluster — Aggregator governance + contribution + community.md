# (C) Cluster — Aggregator governance + contribution + community

**Sources summarized:**
- `CONTRIBUTING.md` (fetched verbatim from `github.com/punkpeye/awesome-mcp-servers/blob/main/CONTRIBUTING.md`, 2026-04-22)
- Community references from `README.md` top section (Discord link + r/mcp + Glama Chat)
- GitHub API snapshot: 839 open issues, 9,365 forks, 6 true-subscribers

**Scope:** This cluster summarizes HOW `awesome-mcp-servers` is governed and how the community interacts. Structure/taxonomy covered in sibling cluster `(C) Cluster — README structure + categorization taxonomy.md`. Ecosystem / companion projects covered in `(C) Cluster — punkpeye ecosystem + companion projects.md`.

## 1. Governance surface — files observed

| File | Status | Corpus comparison |
|------|--------|-------------------|
| `README.md` | ✅ Primary (EN + 6 i18n variants) | Standard |
| `LICENSE` | ✅ MIT | Standard (matches v8, v25 awesome-list peers) |
| `CONTRIBUTING.md` | ✅ Explicit (see §2) | **Richer than v25 awesome-design-md** (which has implicit-only) |
| `SECURITY.md` | Not observed | Gap vs graphify v16 / spec-kit v17 / agency-agents v18 |
| `CODE_OF_CONDUCT.md` | Not observed | Gap vs corporate corpus peers |
| `SUPPORT.md` | Not observed | Gap |
| Issue templates | Not observed in probe | Likely absent (839 open issues suggest low moderation automation) |

**Governance depth assessment:** LIGHT — lighter than any corpus framework at equivalent scale. Pattern #12 (Corporate-formalizes-agent-docs) is NOT active here because Fiegel is solo-individual, not corporate. Pattern #15 (Governance-Depth-Correlation-with-Autonomy) is NOT active because this is content directory not autonomous-agent framework.

**Relevant corpus pattern refinement:** Governance depth correlates with **framework autonomy claim** (confirmed v14 paperclip) AND **organization-type** (confirmed v13 gws / v17 spec-kit). Neither applies here. Aggregator genre = inherently light-governance because there's no code to govern.

## 2. CONTRIBUTING.md — full content digest

Fetched verbatim 2026-04-22. Key sections:

### 2a. Opening statement

> "Contributions are welcome and encouraged! Whether you're fixing a typo, adding a new server, or suggesting improvements, your help is appreciated."

Standard open-contribution awesome-list stance.

### 2b. 🤖🤖🤖 Agent-PR fast-track (CORPUS-FIRST GOVERNANCE PRIMITIVE)

Verbatim:

> "**Note:** If you are an automated agent, we have a streamlined process for merging agent PRs. Just add `🤖🤖🤖` to the end of the PR title to opt-in. Merging your PR will be fast-tracked."

**Significance:**
1. **First corpus evidence of explicit agent-PR governance protocol.** Pattern #23 AI-Disclosure Policy (retired post-v27 audit due to N=1-after-9-wikis) was about passive disclosure (*"disclose if AI helped"*). This is **active workflow-primitive** — opt-in merge-routing distinct from human PRs.
2. **Operationalizes a pattern observed implicitly across corpus** — spec-kit v17 has AI-disclosure-mandatory policy (passive). This goes further: routes agent traffic to a dedicated lane.
3. **Awesome-list-genre fit** — content aggregators where human review per-entry is light-touch (add link + category + description) is exactly the right venue for agent-authored PRs. Code-containing projects have higher stakes.
4. **Potential candidate:** Pattern #69 Agent-PR Fast-Track Governance Protocol (see Phase 4b deliverable + PATTERN_LIBRARY.md).

### 2c. PR workflow (7 steps)

Standard fork → branch → edit → commit → push → PR → review flow. Per-step detail:

1. **Fork** — GitHub button click.
2. **Branch naming** — descriptive, e.g., `add-new-server` or `fix-typo`.
3. **Edit README** — additions include:
   - Server name linked to repo
   - Brief description of functionality
   - Correct category placement; create new category if needed, maintaining alphabetical order
4. **Commit** — clear, concise message.
5. **Push** to forked repo.
6. **Open PR** — title + description.
7. **Review by maintainers** — iteration then merge.

### 2d. Content guidelines (5 rules)

Verbatim bullet structure:

> - **Keep it consistent:** Follow the existing format and style of the `README.md` file. This includes formatting, capitalization, and punctuation.
> - **Alphabetical order:** Maintain alphabetical order within each category of servers. This makes it easier to find specific servers.
> - **Accurate information:** Ensure that all information is accurate and up-to-date. Double-check links and descriptions before submitting your changes.
> - **One server per line:** List each server on a separate line for better readability.
> - **Clear descriptions:** Write concise and informative descriptions for each server. Explain what the server does and what its key features are.

**Observations:**
- **Alphabetical-within-category** is enforced. Contrasts with build-your-own-x v8 (alphabetical-by-language-within-topic is looser).
- **No quality bar** — no "server must be X months old" or "must have Y stars." This is inclusive-by-design; quality signaling via legend badges and descriptions.
- **No moderation SLA** — 839 open issues + no SLA = backlog-tolerant.

## 3. Moderation / curation policy

**Explicit policy:** None beyond CONTRIBUTING.md above.

**Inferred policy:**
- Fiegel + potentially a small team (6 subscribers suggests tight inner circle) review PRs.
- No automated validation observed (no GitHub Actions bot references in probe; would need deeper repo inspection to confirm).
- Category creation is **PR-approval-gated**, not self-service. This is the main quality gate.

**Curation ratio:** Aggregators category references `tadas-github/a2asearch-mcp` claiming **"search 4,800+ MCP servers"** — implies ~4x larger full MCP-server universe. `awesome-mcp-servers` ~1,200 entries = ~25% curation ratio (quality filter active).

## 4. Open issues signal — 839 is large

**Contextualized:**
| Repo | Open issues | Stars | Ratio (open-issues / 1K-stars) |
|------|-------------|-------|-------------------------------|
| awesome-mcp-servers v31 | 839 | 85.3K | 9.84 |
| spec-kit v17 | 506 | 89.2K | 5.67 |
| markitdown v28 | 621 | 114K | 5.45 |
| LlamaFactory v22 | 978 | 70.3K | 13.91 |
| awesome-design-md v25 | 271 | 60.5K | 4.48 |

**Interpretation:** awesome-mcp-servers has **above-average issue-backlog-per-star** but NOT extreme. Suggests solo-maintainer + no auto-moderation + permissive PR-intake. Not a red flag; awesome-list-genre typical.

## 5. Community channels

From README verbatim:

> **Community:**
> - r/mcp Reddit [link]
> - Discord Server [link]

**Western-community-platform pattern (#18) confirmed:** Discord + Reddit combo — matches corpus peers (multica v15, paperclip v14, agency-agents v18, VoltAgent v25, OpenHands v30).

**Glama Chat integration:**
- `glama.ai/chat` = multi-modal AI client with MCP support
- README positions Glama Chat in Clients section, linking to companion `awesome-mcp-clients` repo
- **Tension observation:** repo owner runs commercial chat product; listing Glama Chat in-repo is conflict-of-interest-adjacent. Resolved via transparency (open declaration of commercial companion; see `punkpeye ecosystem` cluster).

## 6. Maintainer profile — Frank Fiegel (punkpeye)

GitHub API (`/users/punkpeye`):
- Name: **Frank Fiegel**
- Company: **Glama**
- Blog: **glama.ai**
- Location: **Miami, FL**
- Bio: *"Engineer turned founder"*
- Public repos: **7** (all MCP-adjacent; see ecosystem cluster)
- Followers: 1,786
- Twitter: `@punkpeye`
- Account created: 2022-06-28 (GitHub account only 4 years old — relatively new)

**Archetype:** **Individual-ecosystem-layer-with-commercial-platform** — distinct from:
- **Yeachan Heo v27** (individual-multi-runtime-publisher; no explicit commercial companion at v27)
- **VoltAgent v25** (organization with parent framework + aggregator + getdesign.md)
- **safishamsi v16 graphify** (individual with `penpax.ai` companion; Pattern #17 N=1-as-candidate)
- **hiyouga v22 LlamaFactory** (academic-lab-affiliated; research lineage)
- **unclecode v29 crawl4ai** (solo-enterprise-scale; no commercial platform yet at v29)

Closest match: **safishamsi + penpax.ai** (Pattern #17 candidate at v16). Fiegel + Glama is **stronger** structural evidence because Glama is >1 product (mcp/servers directory + mcp/clients directory + Chat + blog-as-ecosystem-historian).

**Pattern #17 implication:** Fiegel + Glama = **2nd data point for individual-ecosystem-layer-with-commercial-platform variant** (with safishamsi + penpax.ai v16). Potentially promotes this specific variant to N=2 structurally-unambiguous.

## 7. The State of MCP in 2025 report

**Source:** `glama.ai/blog/2025-12-07-the-state-of-mcp-in-2025`

**Significance:** First corpus instance of an ecosystem-historian output from an aggregator maintainer. Fiegel doesn't just curate the list — produces industry-state synthesis. This is **ecosystem-layer behavior** consistent with Pattern #17.

**Meta-observation:** Storm Bear vault is ALSO an ecosystem-historian practice at smaller scale (31-wiki corpus of agent-ecosystem analysis). Fiegel's State-of-MCP report is a **peer methodological output** to Storm Bear's Pattern Library — both are structured synthesis from observed entity set.

## 8. Governance risk surface for users / Storm Bear

**Risks to flag:**

1. **Supply-chain:** Listing a server ≠ endorsing it. ~1,200 community-contributed servers = ~1,200 potential untrusted-code-execution points. Per Pattern #66 (observation-track, corpus-first documented at crawl4ai v29), installing MCP servers from this list = equivalent attack surface to `npm install`-ing from any registry. **Users must audit each server individually.**
2. **Moderation latency:** 839 open issues suggests servers may stay listed after becoming abandoned/malicious. No "decay policy" observed.
3. **Commercial-companion conflict of interest:** Fiegel runs `glama.ai/chat` (commercial) and curates the directory (OSS). Ecosystem-layer-with-commercial-platform archetype inherently has this tension. Mitigated by transparency (in-README disclosure) but not eliminated.
4. **Bus factor 1:** 6 subscribers suggests Fiegel is sole maintainer. If Fiegel departs, directory could stall. Fork-and-replace is cheap (MIT + markdown-only) but coordination cost is real.

## 9. Cross-wiki governance comparison

| Wiki | Governance depth | Agent-PR protocol | License |
|------|------------------|-------------------|---------|
| build-your-own-x v8 | Light (README-only) | Implicit | CC0 |
| awesome-design-md v25 | Light | Implicit | MIT |
| **awesome-mcp-servers v31** | **Light + explicit agent-lane** | **`🤖🤖🤖` fast-track EXPLICIT** | **MIT** |
| spec-kit v17 | Heavy (9-article constitution + 6 governance files) | AI-disclosure policy passive | MIT |
| graphify v16 | Medium (SECURITY.md standalone) | Not explicit | MIT |
| multica v15 | Medium (skills-lock.json) | Not explicit | MIT |

**Finding:** awesome-mcp-servers is the **first in the awesome-list-genre trio** to operationalize agent contributors. v8 + v25 predate this (2020 + 2026-03-31 respectively). v31 novelty reflects 2025-2026 normalization of agent-authored PRs.

## 10. Contribution pathway for Storm Bear

**Scenario:** Storm Bear operator writes an MCP server for VN Scrum facilitation and wants it listed.

1. Build server per MCP spec (modelcontextprotocol.io).
2. Publish to GitHub under operator's account.
3. Fork `punkpeye/awesome-mcp-servers`.
4. Branch `add-vn-scrum-coach-server`.
5. Add entry under appropriate category:
   - If Scrum-ceremony facilitation: **Product Management** category (near Jira/Linear MCPs)
   - If Vietnamese-specific utility: **Other Tools** catch-all
6. Commit with alphabetical-order discipline.
7. PR with title suffix `🤖🤖🤖` if Claude Code authored it — fast-track merge.
8. Respond to maintainer review feedback.

**Expected merge latency:** hours-to-days given fast-track + light governance. Cost to Storm Bear operator: low.

## 11. Cross-references

- **Agent-PR governance candidate:** see Pattern #69 proposal in `(C) Pattern Implications...` entity + PATTERN_LIBRARY.md v31 updates
- **Pattern #17 Ecosystem-layer peers:** [[03 Projects/awesome-design-md - Beginner Analysis/|VoltAgent v25]] + [[03 Projects/graphify - Beginner Analysis/|safishamsi + penpax.ai v16]]
- **Pattern #18 Community-platform peers:** multica v15 / paperclip v14 / agency-agents v18 / OpenHands v30
- **Pattern #66 Supply-chain peer:** [[03 Projects/crawl4ai - Beginner Analysis/|crawl4ai v29]] (first documented corpus incident response)
- **Aggregator peers:** [[03 Projects/build-your-own-x - Beginner Analysis/|build-your-own-x v8]] + [[03 Projects/awesome-design-md - Beginner Analysis/|awesome-design-md v25]]

---

_Part of Storm Bear LLM Wiki — 31st wiki. Written by Claude (C). Verified 2026-04-22._
