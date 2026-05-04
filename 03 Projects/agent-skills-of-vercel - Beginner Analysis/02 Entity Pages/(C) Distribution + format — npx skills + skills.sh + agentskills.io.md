# (C) Entity Page — Distribution + Format (`npx skills` + skills.sh + agentskills.io)

**Type:** Distribution / ecosystem entity
**Source:** README §Installation + §Skill Structure + AGENTS.md §End-User Installation + homepage URL
**Cross-refs:** oh-my-claudecode v27 (Pattern #59 59a marketplace+npm) / claude-hud v35 (Pattern #59 59b marketplace-only) / awesome-claude-skills v50 (composio-skills `.claude-plugin/marketplace.json` template) / aidevops v47 (5-surface distribution incl. npm) / shannon v45 (3-surface npx + Docker + clone) / awesome-mcp-servers v31 (third-party agent ecosystem registry)

---

## 1. Distribution surface inventory

| Surface | Channel | Audience | Verbatim install command |
|---|---|---|---|
| 1 | `npx skills` (third-party registry) | Bulk agent users | `npx skills add vercel-labs/agent-skills` |
| 2 | Manual `cp -r` (filesystem) | Claude Code users | `cp -r skills/{skill-name} ~/.claude/skills/` |
| 3 | Per-skill ZIP download | Selective users | Download `{skill-name}.zip` from `skills/<skill-name>.zip` |
| 4 | Paste SKILL.md | claude.ai users | "Add the skill to project knowledge or paste SKILL.md contents into the conversation" |

**4-surface T1 standard install pattern.** Below corpus-max (magika v44 6+ channels via 5-language multi-binding); above minimum (single-channel solo wikis).

## 2. Corpus-first `npx skills add <repo>` install verb

**Distinct from prior corpus install verbs:**

| Install verb | Source | Wiki anchor |
|---|---|---|
| `/plugin marketplace add <repo>` | Claude Code native marketplace | oh-my-claudecode v27 (59a) / claude-hud v35 (59b) |
| `npm install <pkg>` / `npx <bin>` | npm registry | Multiple wikis (general npm) |
| `pip install <pkg>` / `pipx install` | PyPI | Multiple wikis |
| `cargo install <pkg>` | Crates.io | gws v13 |
| `uv tool install <pkg>` | uv (Astral) | spec-kit v17 |
| `cp -r <dir> ~/.claude/skills/` | Manual filesystem | Multiple wikis |
| **`npx skills add <repo>`** | **skills.sh / agentskills.io** | **Vercel v51 (NEW)** |

The `npx skills` invocation suggests a published npm package called `skills` (likely `@agentskills/cli` or similar canonical name) maintained by skills.sh / agentskills.io.

**Important distinction:** This is NOT Anthropic-native. It's a **third-party agent-skills registry** that wraps the existing `~/.claude/skills/` filesystem convention. Anthropic doesn't endorse skills.sh; Vercel chose this distribution because it's lower-friction than `cp -r`.

**Pattern #59 sub-variant within scope:**
- 59a: Anthropic-native marketplace + npm companion (oh-my-claudecode v27)
- 59b: Anthropic-native marketplace only (claude-hud v35)
- **NEW observational sub-variant: Third-party agent-skills registry via `npx skills add`** (Vercel v51) — NOT registered standalone (consolidation-forward; observational only)

## 3. skills.sh / agentskills.io ecosystem

**Homepage of vercel-labs/agent-skills (per GitHub):** `https://skills.sh/vercel-labs/agent-skills`

**Format reference (per README):** `https://agentskills.io/`

**Inferred ecosystem structure:**
- **agentskills.io** = format spec authority (defines what a SKILL.md must contain)
- **skills.sh** = registry / directory (lists published skills; provides `npx skills` CLI wrapper)
- These are independent of Anthropic; analogous to npmjs.com vs Node.js Foundation
- Vercel chose to publish to skills.sh rather than build its own marketplace

**Ecosystem layer parallel to Pattern #18 MCP runtime standardization:**
- MCP = Anthropic-led protocol; awesome-mcp-servers v31 is community-curated MCP server directory
- agentskills.io / skills.sh = community-led format spec + registry; vercel-labs/agent-skills is publisher

**Strategic implication:** Vercel as ecosystem-scale commercial platform (Pattern #17 variant 5) chose to participate in third-party agent-skills ecosystem rather than build proprietary registry. Reinforces variant 5 archetype: ecosystem-scale platforms participate in standards rather than imposing their own.

## 4. Per-skill ZIP packaging

**5 of 7 skills** ship pre-built zips alongside their directories:
- `deploy-to-vercel.zip`
- `react-best-practices.zip`
- `react-view-transitions.zip`
- `vercel-cli-with-tokens.zip`
- `web-design-guidelines.zip`

**2 missing zips:**
- `composition-patterns.zip` (likely newer; not yet packaged)
- `react-native-skills.zip` (likely newer; not yet packaged)

**Build instruction (per AGENTS.md):**
```bash
cd skills
zip -r {skill-name}.zip {skill-name}/
```

**Use case:** Users who can't / don't want to `git clone` the full repo can download a single zip per skill of interest. ~2-50 KB per skill.

**Pattern #2 Distribution Evolution data point:** per-skill zip-bundle distribution at T1 (corpus-first observation; prior corpus zip distributions were per-package-Docker images at T5 commercial-startup or per-platform tarballs at T4).

## 5. Paste-to-claude.ai workflow

For users on claude.ai (browser, not Claude Code CLI):

> *"Add the skill to project knowledge or paste SKILL.md contents into the conversation."* (verbatim AGENTS.md)

> *"If the skill requires network access, instruct users to add required domains at claude.ai/settings/capabilities."* (verbatim AGENTS.md)

**Implication:** SKILL.md is designed to be self-contained enough to paste directly into a conversation as Project knowledge. The 500-line cap on SKILL.md (per AGENTS.md best-practices) makes paste workable.

**Network access caveat:** If skill calls external services (e.g., `vercel deploy` hits api.vercel.com), claude.ai requires explicit domain whitelisting at user settings. deploy-to-vercel + vercel-cli-with-tokens require this; rule-aggregator skills don't.

## 6. Filesystem convention `~/.claude/skills/`

**Standard Claude Code skill location:** `~/.claude/skills/<skill-name>/SKILL.md`

**Vercel install pattern:**
```bash
cp -r skills/{skill-name} ~/.claude/skills/
```

**Note path:** `~/.claude/skills/` is the standard; some other Anthropic-native paths exist (`/mnt/skills/user/...` for claude.ai sandbox). AGENTS.md script convention uses `/mnt/skills/user/{skill-name}/scripts/{script}.sh` referring to claude.ai-specific path. Claude Code uses `~/.claude/skills/<name>/scripts/<script>.sh` naturally.

## 7. Format-spec lineage

**agentskills.io format defines:**
- YAML frontmatter (`name`, `description`, optional metadata)
- SKILL.md as canonical filename
- 500-line cap recommendation
- On-demand loading semantics
- `scripts/` and `references/` subfolder conventions

**This is structurally similar to Anthropic's published Claude Skills spec** (anthropics/skills repo). agentskills.io may be a community-led extraction/extension of Anthropic conventions, not a competing standard.

**Open question (see OPEN-QUESTIONS.md item 8):** Is skills.sh / agentskills.io community-owned or Vercel-owned? Not investigated at v51.

## 8. Pattern Library observations (this entity contributes)

| Pattern | Action |
|---|---|
| #59 Plugin Marketplace Native | Observational sub-variant: third-party registry via `npx skills add` (skills.sh / agentskills.io) |
| #2 Distribution Evolution | 4-surface install standard-T1 observation; per-skill zip-bundle corpus-first at T1 |
| #18 MCP runtime standardization | Counter-evidence observational: agent-skills format ecosystem parallels MCP ecosystem at higher abstraction (skills are Anthropic-runtime-specific while MCP is runtime-agnostic) |

## 9. Distribution comparison vs sibling wikis

| Wiki | Primary install | Channels | Marketplace? |
|---|---|---|---|
| oh-my-claudecode v27 (T1) | `/plugin marketplace add` | 2 (marketplace + npm) | Anthropic-native (Pattern #59 59a) |
| claude-hud v35 (T1) | `/plugin marketplace add` | 1 (marketplace-only) | Anthropic-native (Pattern #59 59b) |
| awesome-claude-skills v50 (outside-scope hybrid) | `composio-skills` `.claude-plugin/marketplace.json` for sub-component | 2 (marketplace via sub-component + clone) | Composio-built directory-scoped marketplace.json |
| **vercel-labs/agent-skills v51 (T1)** | **`npx skills add <repo>`** | **4 (npx skills + manual cp + per-skill zip + paste-to-claude.ai)** | **Third-party skills.sh registry (NOT Anthropic-native)** |
| pi-mono v36 (T1) | `npm install` | 2 (npm + manual) | None (purely npm-distributed) |

**Distribution maturity:** Vercel v51 has 4 surfaces — middle of pack. claude-hud v35 single-channel was minimum-friction; pi-mono v36 npm-canonical for skill-sets is most-maintainer-overhead.

## 10. Tradeoffs + caveats

**Strengths:**
- 4-surface install matches diverse user populations (CLI users / browser users / selective users / bulk users)
- Per-skill zip enables selective adoption without full-repo clone
- Self-contained SKILL.md enables paste-to-claude.ai workflow

**Caveats:**
- `npx skills add` requires trust in skills.sh / agentskills.io ecosystem (not Anthropic-vetted)
- skills.sh ecosystem maturity unclear (no public roadmap visible)
- Per-skill zip bundles can become stale relative to skill source (no automation observed; 2 of 7 skills missing zips entirely)
- Paste-to-claude.ai workflow requires domain whitelisting for network-access skills (UX friction)

**Supply-chain awareness (Pattern #66 OBSERVATION-TRACK):**
- `npx skills add` invokes skills.sh CLI which may inject arbitrary code via skill installation
- Recommend `npx skills add <repo>` only for repos with vetted authorship (Vercel = trustable; random user repos = caution)
- Per-skill zip download is auditable (zip + extract; user can read SKILL.md before install)

End of entity page.
