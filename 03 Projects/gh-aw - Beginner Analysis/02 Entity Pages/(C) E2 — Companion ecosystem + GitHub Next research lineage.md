# (C) Entity 2 — Companion ecosystem + GitHub Next research lineage

> **Wiki #48** | **2026-04-25** | gh-aw is part of a 4-repo coordinated github/* sub-ecosystem with explicit GitHub Next research-incubation-to-mainline-graduation lineage and 4-named-researcher CODEOWNERS cluster.

## 1. The 4-repo github/* sub-ecosystem

### `github/gh-aw` — Core product (this wiki's subject)
- **Function:** GitHub CLI extension; compiles markdown agentic-workflow specs to GitHub Actions YAML
- **Stars:** 4,367 | **License:** MIT | **Lang:** Go

### `github/gh-aw-firewall` — Agent Workflow Firewall (AWF)
- **Function:** *"Network egress control for AI agents, providing domain-based access controls and activity logging for secure workflow execution"*
- **Role in gh-aw architecture:** Implements Layer 5 Sandbox Isolation (per W3C-style security spec) — provides domain allowlisting + activity logging that gh-aw workflows can configure via `network: { allowed: [...] }` frontmatter
- **Reusability:** Open-source companion infrastructure; can be deployed independently for any AI-agent system needing egress control

### `github/gh-aw-mcpg` — MCP Gateway
- **Function:** *"Routes Model Context Protocol (MCP) server calls through a unified HTTP gateway for centralized access management"*
- **Role in gh-aw architecture:** Layer 0 unified-routing-infrastructure for MCP servers; provides observable access management above per-runtime MCP. Workflows reference MCP servers via gateway URLs rather than per-agent direct connections.
- **Pattern Library implication:** **CORPUS-FIRST MCP-gateway-as-unified-routing-infrastructure** (Pattern #18 Layer 0 observation strengthening)

### `github/gh-aw-actions` — Shared GitHub Actions library
- **Function:** *"Shared library of custom GitHub Actions used by compiled workflows, providing functionality such as MCP server file management"*
- **Role in gh-aw architecture:** Reusable Actions infrastructure consumed by compiled `.lock.yml` workflows; isolates Action implementation from main gh-aw repo for independent versioning + reusability

## 2. Sub-ecosystem coordination model

| Aspect | gh-aw | gh-aw-firewall | gh-aw-mcpg | gh-aw-actions |
|--------|-------|----------------|------------|---------------|
| Org | github | github | github | github |
| License | MIT | MIT | MIT | MIT |
| Role | Compiler + CLI | Network firewall | MCP routing gateway | Shared Actions library |
| Versioning | Independent | Independent | Independent | Independent |
| Position in 7-layer security architecture | Spans all layers | Layer 5 Sandbox | Layer 0 + Layer 5 | Layer 5 + reusable infra |

= **CORPUS-FIRST 4-repo coordinated infrastructure-platform-companion at corporate-official tier** under single parent (github org).

**Distinct from prior corpus ecosystem variants:**
- RuvNet 15-package solo-flagship-with-multi-sibling (ruflo v42)
- HKUDS 7-repo academic-lab-ecosystem-portfolio (DeepTutor v38)
- Zilliz 8-product commercial-startup-with-sibling-tools (claude-context v40)
- Microsoft AutoGen + markitdown sibling (markitdown v28; 2 repos at T3+T4)
- Google Workspace + magika (gws v13 + magika v44; 2 repos different orgs)
- **gh-aw-* 4-repo coordinated infrastructure-platform-companion** (NEW v48)

## 3. GitHub Next research lineage (Pattern #19 archetype 2 strengthening)

### CODEOWNERS = the 4-researcher cluster

```text
- @dsyme @eaftan @pelikhan @krzysztof-cieslak
```

| Maintainer | Identity | Notable role |
|------------|----------|--------------|
| **@dsyme** | **Don Syme** | F# language creator; long-time Microsoft Research → GitHub Next |
| **@eaftan** | Eric Aftandilian | Engineering lead |
| **@pelikhan** | **Peli de Halleux** | "Peli's Agent Factory" namesake; researcher |
| **@krzysztof-cieslak** | **Krzysztof Cieślak** | Ionide (F# IDE for VS Code) creator |

= **CORPUS-FIRST GitHub Next 4-researcher cluster lineage** at github-corporate-official tier.

### Don Syme — corpus-first F# language creator

Don Syme is the original creator of F# (Microsoft Research, 2002+) and a major contributor to functional-programming-language design. His presence at gh-aw CODEOWNERS signals serious-language-design DNA in agentic-workflow-compiler architecture. The repo's `scratchpad/functional-patterns.md` engineering note is plausibly direct evidence of F#-influenced code-organization philosophy applied to Go.

**Pattern Library implication:** Pattern #19 archetype 2 methodology-lineage gains a NEW node-type: **language-design-researcher-as-team-member**. Distinct from individual-author-lineage (Karpathy, Lam, Cherny) — Don Syme is contributing as part of a team-cluster, not as a cited-influence.

### Krzysztof Cieślak — corpus-first Ionide creator

Krzysztof Cieślak is the original author of Ionide (F# language extension for VS Code; major OSS contributor). His presence with Don Syme at CODEOWNERS reinforces **F# / functional-design influence at gh-aw architectural level**.

### Peli de Halleux — research lineage focal point

Peli is named in 2 distinct README sections:
- **CODEOWNERS** — `@pelikhan` (maintainer)
- **Peli's Agent Factory** — README links blog post: *"a guided tour through many uses of agentic workflows"* at https://github.github.com/gh-aw/blog/2026-01-12-welcome-to-pelis-agent-factory/

= **CORPUS-FIRST personally-named feature-section at github-corporate-official tier**. Where spec-kit v17 cited John Lam as influence-source, gh-aw has Peli as named-product-positioning element. Reflects research-personality dimension at corporate-official tier rare in corpus.

### Eric Aftandilian — engineering lead

Less publicly profiled than Syme/Cieślak/de Halleux but listed first by name length in CODEOWNERS line. Plausibly the engineering lead grounding the 4-researcher cluster's outputs in production discipline.

## 4. Research-incubation-to-mainline graduation pathway

**Migration timeline (per CHANGELOG v0.40.1, 2026-02-03):**

```text
2025-08-12  ────  github/gh-aw repo created (initial development as githubnext/gh-aw)
   │
   │ ~6 months as research project under githubnext/* org
   │
2026-02-03  ────  v0.40.1 — Migration: githubnext/gh-aw → github/gh-aw
   │              CHANGELOG entry: "Move from githubnext/gh-aw to github/gh-aw.
   │              If you were a former user of the githubnext Agentic Workflows
   │              you might have to re-register the extension to reflect the
   │              new location."
   │
   │ Continued under github/* mainline org
   │
2026-04-14  ────  v0.68.3 latest release (~2.5 months post-graduation)
   │
2026-04-25  ────  Storm Bear v48 wiki snapshot
```

**Significance:** This is the **first explicit research-incubation-to-mainline-graduation observable in Storm Bear corpus**. Pattern Library implications:

- **Pattern #19 archetype 2 methodology-lineage strengthening** — research-org-cluster (GitHub Next) graduating to mainline parent (github) is observable origin pathway, distinct from purely-corporate-internal incubation.
- **Pattern #17 variant 2a strengthening** — 2nd github/* corpus entry (after spec-kit v17), but with different org-internal provenance (github mainline directly vs githubnext incubation graduated).
- **Counter-evidence to "research-projects stay in research-org" assumption** — at sufficient maturity, github/* org adopts research products into mainline.

**Open question (registered in Open Questions v48):** What were the graduation criteria? Internal milestones? This would inform Storm Bear's potential public-publication pathway if vault ever externalizes.

## 5. Comparison to prior corpus lineage clusters

| Cluster | Wiki source | Cluster members | Lineage type |
|---------|-------------|------------------|--------------|
| **Anthropic-team-cluster** | claude-howto v32 + claude-code-best-practice v34 + aidevops v47 | Boris Cherny (creator) + Dex Horthy + Cat Wu + Lance Martin (LangChain ext) | Anthropic-direct + adjacent-influencer |
| **Karpathy-individual** | autoresearch v10 + Storm Bear vault foundation + graphify v16 + rowboat v43 (implicit) | Andrej Karpathy (single individual) | Individual-author-lineage |
| **John Lam (jflam)** | spec-kit v17 (cited as influence) | John Lam (single individual) | Individual-author-lineage |
| **GitHub Next 4-researcher cluster (NEW v48)** | gh-aw v48 | Don Syme + Eric Aftandilian + Peli de Halleux + Krzysztof Cieślak | Research-org-cluster-as-team-members |

**Pattern observation:** Lineage clusters in corpus are now N=4 distinct types observable across 47 wikis (4-node graph corpus-complete per v47 aidevops + new v48 GitHub Next cluster as 5th point).

## 6. Why this matters for Pattern #66 OT

The 4-repo sub-ecosystem is **architecturally significant for Pattern #66 OT supply-chain framing**:

- **gh-aw-firewall (AWF)** = sandbox isolation Layer 5 of the 7-layer security architecture
- **gh-aw-mcpg (MCP Gateway)** = unified routing layer for MCP, providing centralized access management above per-runtime MCP
- **gh-aw-actions** = shared SHA-pinned Actions library (per W3C spec compliance)

Together, these companion repos make gh-aw the **first corpus framework with explicitly-modularized defense-in-depth architecture across 4 coordinated repos** at corporate-official tier. Defense-in-depth isn't just internal to one repo — it's distributed across the sub-ecosystem.

## 7. Comparison to non-coordinated alternatives

Without the companion repos, gh-aw would face:
- AWF-equivalent: per-workflow custom firewall config (no central reusable infra)
- MCP-gateway-equivalent: per-agent MCP-server connection (no centralized access management)
- Shared-Actions-equivalent: every workflow re-implements common primitives (no library reuse)

The 4-repo coordination thus provides **architectural-leverage at corporate-official tier**: each repo serves a distinct Layer (or set of Layers) in the 7-layer security architecture. This is more than ecosystem-portfolio (where multiple products serve different markets) — it's **architectural-decomposition-into-coordinated-repos** (where multiple repos serve a single coordinated product's architectural layers).

## 8. Storm Bear vault implications

If Storm Bear ever externalizes (publishes wiki + skills as public asset), the gh-aw 4-repo decomposition is a reference for:
1. **Core wiki** = `storm-bear-wiki` (analog of gh-aw)
2. **Skill library** = `storm-bear-skills` (analog of skills/ subdir promoted to own repo)
3. **Routine specifications** = `storm-bear-routines` (analog of gh-aw-actions for shared workflow primitives)
4. **Maybe?** Pattern Library = `storm-bear-pattern-library` (own repo for cross-wiki taxonomy)

This decomposition is NOT recommended at current vault scale (47 wikis is well-served by single-vault structure), but provides a reference architecture if scale grows beyond single-repo manageable.

## 9. Pattern Library cross-tags

- Pattern #17 variant 2a corporate-official — STRENGTHENING (github/* now has 2 corpus entries: spec-kit T1 + gh-aw T4 + 4-repo sub-ecosystem under gh-aw)
- Pattern #19 archetype 2 methodology-lineage — STRENGTHENING (GitHub Next 4-researcher cluster as research-org-cluster lineage type)
- Pattern #18 Layer 0 — N=1 observation (MCP Gateway as unified routing infrastructure)
- Pattern #66 OT — MAJOR STRENGTHENING via 4-repo defense-in-depth decomposition

## 10. Cross-references

- **spec-kit v17** — sister github/* corpus entry; both share parent org but have different methodologies + tier placements
- **aidevops v47** — recent 4-research-influence-node graph (Karpathy + Lam + Anthropic-team + Lance Martin); gh-aw adds 5th cluster type (GitHub Next research-cluster)
- **awesome-mcp-servers v31** — Pattern #18 ancestor; gh-aw consumes MCP servers via gateway companion repo (`gh-aw-mcpg` is adjacent infrastructure layer to awesome-mcp-servers content layer)
- **claude-howto v32** — Anthropic-team-cluster precedent (Boris Cherny + Dex Horthy + Cat Wu); GitHub Next 4-researcher cluster is structural parallel
- **claude-code-best-practice v34** — Anthropic-team-cluster 2nd citation precedent; cluster-as-lineage convention extended at v48 to research-org-cluster

## 11. Open questions

(See `06 Open Questions/(C) Open questions v48.md` for full list.)

Most pressing:
1. What were the graduation criteria from `githubnext/gh-aw` to `github/gh-aw` at v0.40.1?
2. How is contributor attribution split — % from Don Syme / Peli / Eric / Krzysztof / Copilot agent / community?
3. Is gh-aw used at GitHub.com production-development scale, or is it primarily research-output?
4. Will MCP Gateway (`gh-aw-mcpg`) become a corpus-cited reference for Pattern #18 Layer 0 if 2nd MCP-gateway-pattern observation arrives in future wikis?

## 12. Status

**Production-stable** sub-ecosystem at coordinated v0.68.3 release cadence (~3-week iteration). 4-research-cluster CODEOWNERS preserves continuity from githubnext incubation through github mainline graduation.
