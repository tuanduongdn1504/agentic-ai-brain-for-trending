# OPEN-QUESTIONS — n8n Beginner Analysis (v56)

## Resolved during build

✅ **License clarity** — n8n SUL is source-available non-OSI with internal-business-use permitted but hosting-as-service restricted (verified via docs.n8n.io/sustainable-use-license)

✅ **Phase 0.9 STRICT decision** — criterion (b) PASSES (operational tool for Scrum coaching under SUL internal-use clause)

✅ **Bidirectional MCP** — n8n has BOTH MCP Client node AND MCP Server Trigger node (verified via docs.n8n.io/advanced-ai)

## Unresolved (deferred to operator or post-v56 audit)

### Q1: TrendRadar v19 cross-citation verification (Phase 0.9 criterion d)

**Question:** Does TrendRadar v19 (`xianqing-coder/TrendRadar`) actually cite n8n as multi-channel push target in its README or docs?

**Why it matters:** If YES, criterion (d) PASSES too — strengthens Phase 0.9 INCLUDE evidence + Pattern #57 sub-variant 57c forward-citation-then-wiki extends to N=3 (multica→vercel-labs + OMC→omo + TrendRadar→n8n).

**Resolution path:** Operator grep `_state/05-projects-v1-v29.md` for "n8n" string. Or reread v19 TrendRadar entry directly.

**Default if unresolved:** Phase 0.9 (b) standalone PASS sufficient; criterion (d) status remains TENTATIVE in CLAUDE.md.

### Q2: AGENTS.md presence in n8n repo

**Question:** Does n8n repository have root AGENTS.md / CLAUDE.md / contributor agent config?

**Why it matters:** Pattern #22 AGENTS.md Industry Standard tracking + 5-template ensemble taxonomy (22a/22b/22c/22d). At 185K stars + 7-year-mature commercial GmbH, AGENTS.md presence/absence is significant Pattern #22 data point.

**Resolution path:** WebFetch `https://github.com/n8n-io/n8n/blob/master/AGENTS.md` and `https://github.com/n8n-io/n8n/blob/master/CLAUDE.md` (404 = absent; 200 = present).

**Default if unresolved:** Pattern #22 observation flagged for next-session probe; not blocking v56 ship.

### Q3: i18n docs language coverage

**Question:** docs.n8n.io supports how many languages?

**Why it matters:** Mature commercial platform at 185K stars; i18n axis classification incomplete without verification.

**Resolution path:** WebFetch docs.n8n.io home page + check language switcher.

**Default if unresolved:** Assumed EN-primary; Pattern #2 5-language-at-T2 sub-variant uncertain.

### Q4: n8n.cloud pricing tier breakdown

**Question:** What are n8n.cloud Pro tier pricing + feature gates? What is the open-source vs cloud feature delta?

**Why it matters:** Pattern #31 Open-Core Commercial Entity Pro-docs-depth axis (0-4 ordinal scale post-v45). n8n.cloud appears depth 3-4 estimate but unverified.

**Resolution path:** WebFetch n8n.io/pricing + extract tier list + feature comparison.

**Default if unresolved:** Pattern #31 11th data point with depth-3-4-estimate; refine at next mini-audit if needed.

### Q5: VC funding history

**Question:** Is n8n GmbH VC-funded? Sequoia, FirstMark, etc.?

**Why it matters:** Pattern #17 variant 3 commercial-startup ecosystem — funding-stage axis is sub-discriminator (bootstrap vs seed vs Series-A vs growth-stage).

**Resolution path:** TechCrunch / Crunchbase search OR n8n.io About page deeper than imprint.

**Default if unresolved:** Pattern #17 variant 3 observation without funding-stage discriminator; not blocking v56 ship.

### Q6: Russian/Ukrainian/Belarusian usage policy

**Question:** Does n8n SUL or n8n.cloud have geographic-restriction clauses (e.g., RU/BY sanctions compliance)?

**Why it matters:** SUL-license-family geographic-restriction sub-axis; relevant to Storm Bear deployment if any cross-border Scrum coaching includes RU-aligned clients.

**Resolution path:** SUL full-text grep + n8n.cloud TOS grep for "Russia" / "sanctions" / "OFAC".

**Default if unresolved:** Assume no geographic restriction; Storm Bear compliance burden is operator-delegated.

## Verification gaps for next-session mini-audit

If/when post-v56 mini-audit is run, prioritize:

1. **Q1 corpus grep** (criterion d resolution + Pattern #57 57c potential N=3)
2. **Q2 AGENTS.md probe** (Pattern #22 ensemble update)
3. **Q4 n8n.cloud tier breakdown** (Pattern #31 depth axis refinement)

Q3 / Q5 / Q6 are non-blocking.
