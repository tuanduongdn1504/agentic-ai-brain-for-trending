# Entity: Cross-vendor cooperation pattern (CORPUS-FIRST OpenAI-publishes-for-Claude Code)

> **Wiki:** codex-plugin-cc v62 / 2026-05-08
> **Format:** 13-section entity page

---

## 1. Identity

**Cross-vendor cooperation observation:** OpenAI corporate-org publishes Apache-2.0 plugin FOR Anthropic Claude Code rival platform — corpus-first cross-vendor-cooperative-plugin-direction in 62-wiki history. NEW Pattern #77 candidate.

## 2. Source

- Repo attribution: `openai/codex-plugin-cc` (OpenAI organization)
- Host platform: Anthropic Claude Code
- License: Apache-2.0 (corporate-AI-tool default per corpus pattern)
- Distribution: Anthropic Claude Code plugin marketplace (rival's distribution channel)

## 3. Tier placement (observation, not entity itself)

This is observation-level pattern about corporate-strategy + cross-platform behavior. Not tier-classifiable as own entity but informs:
- Pattern #19 corporate-strategic archetype N=2 cross-org (Microsoft + OpenAI)
- NEW Pattern #77 candidate: Cross-Vendor Cooperative Plugin Publication

## 4. Core mechanism

**Cross-vendor publication direction observed:**

```
OpenAI organization
    ↓ publishes (Apache-2.0 OSS)
codex-plugin-cc
    ↓ installs into
Anthropic Claude Code (rival platform)
    ↓ via
Anthropic Claude Code plugin marketplace
```

**Authentication architecture:**
- Plugin host (Claude Code) does NOT proxy authentication
- User authenticates to Codex separately (ChatGPT subscription OR API key)
- Cross-vendor trust boundary explicitly maintained

**Strategic mechanism:**
- OpenAI gains: developer footprint in Claude Code marketplace; ChatGPT subscription revenue retained even when Anthropic hosts UX
- Anthropic gains: stronger plugin ecosystem (more plugins → more reasons to use Claude Code as host)
- Developer gains: best-of-both-worlds workflow (Claude Code UX + Codex review/delegation)

## 5. Pattern Library implications

### NEW Pattern #77 candidate: Cross-Vendor Cooperative Plugin Publication

**Formal statement (candidate):**
> AI provider organizations publish Apache-2.0/MIT OSS plugins targeting RIVAL provider's IDE/host platform — accepting host platform's distribution channel + UX while retaining own backend/auth. Reflects post-platform-war recognition that developer UX preference trumps platform loyalty; rival cooperation via plugin-marketplace serves marketshare-retention strategy. Distinct from same-ecosystem-publication (Microsoft for GitHub) and from rival-competition (Codex CLI vs Claude Code).

**Required for promotion:** 2+ cross-vendor cooperative plugin publications observed.

**Watch list for un-stale candidates:**
- Anthropic publishes Claude tooling for Codex CLI / OpenAI ChatGPT plugins
- Google Gemini plugin for Claude Code or Codex CLI
- Microsoft GitHub Copilot extensions for non-VSCode hosts
- xAI Grok plugin for Claude Code or Cursor

**Stale-flag at registration:** N=1 stale-flagged at codex-plugin-cc v62. Re-evaluate at v66 stale-check + v71 retire-check.

### Pattern #19 corporate-strategic archetype N=2 cross-org structural

**Pre-v62:** N=1 cross-corporate-org (Microsoft only, with 2 products spec-kit v17 + markitdown v28)

**Post-v62:** N=2 cross-corporate-org (Microsoft + OpenAI)

**Promotion-eligibility check at v66:**
- Structural-N=2 across distinct corporate orgs (Microsoft vs OpenAI distinct organizational entities, not same-org-with-2-products)
- Each org demonstrates distinct corporate-strategic positioning (Microsoft: ecosystem dominance; OpenAI: rival cooperation)
- Promotion candidate: Pattern #19 archetype N=2 cross-org sub-variant under criterion #2 structural-unambiguity

### Pattern #18 Layer 2 cross-vendor-bridge sub-archetype

3rd Pattern #18 Layer 2 sub-archetype:
- v60 free-claude-code: api-protocol-translation-proxy
- v61 cc-sdd: install-time-per-platform-skill-format-translator
- **v62 codex-plugin-cc: cross-vendor-platform-bridge-as-plugin (NEW)**

Each N=1; if 5+ Layer 2 sub-archetypes accumulate at future audit, consider meta-pattern consolidation under "Cross-Tool-Integration-Architectures" parent.

## 6. Differentiators (vs prior corpus corporate-publication patterns)

| Dimension | Microsoft (spec-kit v17 / markitdown v28) | **OpenAI (codex-plugin-cc v62)** |
|---|---|---|
| **Target ecosystem** | Own (GitHub / Microsoft tools) | **RIVAL (Anthropic Claude Code)** |
| **Distribution mechanism** | Own marketplaces | **Rival's plugin marketplace** |
| **Authentication** | Within-platform | **Cross-vendor (separate auth)** |
| **License** | Apache-2.0 | Apache-2.0 (matches corporate default) |
| **Strategic motive** | Ecosystem dominance via tooling | **Marketshare retention via cross-publication** |
| **Backward symmetry** | Microsoft for Microsoft (no cross-publication observed corpus-side) | **OpenAI for Anthropic (corpus-first)** |

## 7. Origin / lineage

- OpenAI corporate-strategic decision context (recent — v1.0.4 April 2026)
- Plugin-shaped technical implementation (vs full-IDE-fork or backend-only API)
- Apache-2.0 licensing matches corporate-AI-tool default (spec-kit + magika + codex-plugin-cc all Apache-2.0)
- No methodology lineage cited (no SDD / BMM); functional-tool framing

## 8. Adoption signals

- 17.8K stars at 26 commits = viral attention on corporate publication
- 1K forks (5.6%) = standard OSS engagement
- 104 open issues active community engagement
- Apache-2.0 compatible with most commercial use
- ChatGPT subscription gate filters audience but signals OpenAI revenue-retention strategy

## 9. Limitations / failure modes

- **Cross-vendor trust boundary risk** — supply chain spans Anthropic + OpenAI; either compromise affects user
- **Auth complexity** — separate auth for plugin backend creates UX friction
- **Symmetric expectation pressure** — OpenAI publishing for Anthropic creates implicit pressure for Anthropic to publish for Codex CLI; if not reciprocated, asymmetric cooperation observed
- **Plugin abandonment risk** — corporate strategy shifts could deprecate plugin (corpus has prior abandonment observations)

## 10. Storm Bear vault applicability

The cross-vendor cooperation pattern itself is observation-level, not directly deployable. But it implies:
- **Vault can use multi-vendor agent stacks** without lock-in (cc-sdd cross-platform + codex-plugin-cc cross-vendor + free-claude-code multi-provider proxy)
- **Storm Bear's 4-plugin Claude-Code augmentation stack** observation extends: cc-sdd + codex-plugin-cc + claude-hud + claude-context as multi-vendor stack
- **Pilot strategy implication:** Storm Bear could pilot vendor-diverse stack rather than vendor-monoculture; lower lock-in risk

## 11. Open questions

- Q2: OpenAI strategic motive — marketshare protection / UX optimization / distribution acquisition / commodification?
- Q3: License Apache-2.0 vs MIT signaling for OpenAI vs other corporate-orgs
- Q8: Is this OpenAI's first-ever plugin published for competitor platform? Or precedent (Copilot extensions for non-VSCode IDE forks)?

## 12. Cross-references

- Pattern #19 corporate-strategic archetype (CONFIRMED v20) — N=2 cross-org evidence at v62
- NEW Pattern #77 candidate: Cross-Vendor Cooperative Plugin Publication
- Pattern #18 Layer 2 cross-vendor-bridge-as-plugin sub-archetype (NEW)
- Pattern #59 Claude Code Plugin Marketplace Native — corporate-scale strengthening
- [spec-kit v17](../../spec-kit%20-%20Beginner%20Analysis/) — Microsoft corporate predecessor
- [markitdown v28](../../markitdown%20-%20Beginner%20Analysis/) — Microsoft corporate predecessor

## 13. Next action

For Pattern Library v66 mini-audit:
1. Register NEW Pattern #77 candidate Cross-Vendor Cooperative Plugin Publication N=1 stale-flagged
2. Pattern #19 corporate-archetype N=2 cross-org evidence note (promotion-eligibility check)
3. Pattern #18 Layer 2 3rd sub-archetype evidence note

For corpus monitoring:
- Watch v63-v70 for 2nd cross-vendor cooperation observation (un-stale Pattern #77)
- Watch for symmetric Anthropic publication for OpenAI / Codex platforms
- Watch for Google / xAI / Microsoft GitHub cross-vendor plugins
