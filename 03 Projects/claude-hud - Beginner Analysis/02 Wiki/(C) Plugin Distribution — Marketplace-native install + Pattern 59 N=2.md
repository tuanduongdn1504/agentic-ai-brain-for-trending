# Plugin Distribution — Marketplace-native install + Pattern #59 N=2

**Entity type:** Distribution mechanism / pattern observation
**Subject:** How claude-hud is installed, updated, and integrated with Claude Code — and what this implies for Pattern #59 (Plugin Marketplace Native)
**First documented:** 2026-04-23 (v35 wiki creation)

---

## 1. One-sentence definition

claude-hud distributes **exclusively via Claude Code's native `/plugin marketplace add` mechanism** — no npm publish, no pypi, no standalone CLI, no separate install script. The marketplace manifest (`.claude-plugin/marketplace.json`) is the sole install surface, and version updates propagate via Claude Code's `/plugin` update flow.

## 2. 3-command install

```
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/claude-hud:setup
```

**Step 1** registers the author's repo as a marketplace. Claude Code fetches `.claude-plugin/marketplace.json` and indexes available plugins.

**Step 2** installs the specific `claude-hud` plugin from the registered marketplace. Claude Code fetches the plugin's `.claude-plugin/plugin.json` and processes it.

**Step 3** runs the plugin's included slash command (`commands/setup.md`) which writes statusline config to user's `~/.claude/settings.json`.

After a Claude Code restart, the statusline is active.

**Critical note:** `statusLine` is NOT a valid field inside `plugin.json`. The setup step is required to write the statusLine config to user's settings.json. This is an Anthropic-side design: plugin manifests declare metadata, but statusLine config is user-settings-scoped.

## 3. Auto-update mechanism

Per CONTRIBUTING.md:

> *Claude Code plugins support updates through the `/plugin` interface:*
> - **Update now** — Fetches latest from main branch, installs immediately
> - **Mark for update** — Stages update for later
>
> *Claude Code compares the `version` field in `plugin.json` against the installed version. Bumping the version number (e.g., 0.0.1 → 0.0.2) allows users to see an update is available.*

**Implication:** Author bumps `plugin.json` version on release. Claude Code periodically (or on demand) checks this against installed version. Users see update prompt in `/plugin` UI.

**Triple-manifest version-bump discipline** required per CONTRIBUTING.md:
- `package.json` → build tooling / npm-convention retention
- `.claude-plugin/plugin.json` → plugin metadata
- `.claude-plugin/marketplace.json` → marketplace index entry

If author forgets to bump any one of these, update propagation may break.

## 4. Setup auto-detection feature

From CHANGELOG v0.0.2 (2025-01-04):
> *Setup command now auto-detects installed plugin version (no manual path updates needed)*

The `/claude-hud:setup` slash command does not hardcode a version. It dynamically resolves the installed plugin path at statusLine configuration time. This means users do not need to re-run setup after plugin updates — the statusLine config continues working with auto-updated versions.

**Pattern observation:** This is version-agnostic statusLine wiring. Contrast naive alternative where setup writes `node /path/to/claude-hud-v0.0.6/dist/index.js` into settings.json (which would break on update). Instead setup writes a path-resolver that finds the latest installed version at runtime.

## 5. Security posture around distribution

**Preventive supply-chain hardening** — per v0.0.2 CHANGELOG:
> *Add CI workflow to build dist/ after merge — closes attack vector where malicious code could be injected via compiled output in PRs*
> *Remove dist/ from git tracking — PRs now contain source only, CI handles compilation*

Effect:
- PRs only contain TypeScript source changes
- Reviewer can audit source without worrying about compiled-output divergence
- CI deterministically rebuilds dist/ post-merge using trusted build environment
- Supply-chain attacker cannot hide malicious code in an unreadable minified blob

**This is a preventive security posture** — distinct from Pattern #66 (Supply-Chain Security Incident Response, OBSERVATION-TRACK v29 for crawl4ai's reactive `unclecode-litellm` fork). claude-hud's approach is pre-emptive; #66 captured reactive incident handling. Cross-reference: preventive-vs-reactive could be an axis for a future #66 refinement if more data emerges.

## 6. Pattern #59 Plugin Marketplace Native — STRENGTHENS to N=2

### Pattern history

Pattern #59 registered at v27 (oh-my-claudecode) as single-observation candidate.

**Formal statement (v27):**
> Framework uses Claude Code `/plugin marketplace add` as primary install channel. Reflects Claude Code ecosystem maturation (marketplace emerging as distribution surface). Distinct from npm install (BMAD, codymaster), `uv tool install` (spec-kit), shell script install (agency-agents), or git clone (ECC, Superpowers).

**v27 prediction:** *"High — Claude Code plugin marketplace is emerging; more frameworks will adopt within 3-5 wikis. Likely promotes quickly."*

### v35 validates the v27 prediction

**Evidence (N=2 post-v35):**

1. **oh-my-claudecode v27** (Yeachan Heo, Korean T1) — `/plugin marketplace add github.com/Yeachan-Heo/oh-my-claudecode` primary. **Sub-variant 59a:** marketplace-primary with npm-companion (published `oh-my-claude-sisyphus@latest` on npm). Sibling product `oh-my-codex` also marketplace-distributed.

2. **claude-hud v35** (Jarrod Watts, Australian T1) — `/plugin marketplace add jarrodwatts/claude-hud` is the ONLY install path. No npm publish despite TypeScript+package.json. **Sub-variant 59b:** marketplace-only (no npm companion).

**Timing:** v27 was wiki 27. v35 is wiki 35. **8 wikis between first and second observation** — fits "3-5 wikis" prediction loosely (slightly slower than predicted). Promotion-candidate at next mini-audit under Criterion 2 (structurally-unambiguous-at-N=2).

### Sub-variant classification

| Sub-variant | Marketplace | npm companion | Primary install path |
|-------------|-------------|---------------|---------------------|
| **59a marketplace-with-npm-companion** | ✅ Primary | ✅ Secondary (`oh-my-claude-sisyphus`) | `/plugin marketplace add` |
| **59b marketplace-only** | ✅ Sole surface | ❌ None | `/plugin marketplace add` |

claude-hud demonstrates that **marketplace can be the sole surface** — author has npm tooling (package.json + tsc) but chooses not to publish. Reasons plausibly:
- Audience is exclusively Claude Code users (no value in npm listing for non-CC users)
- Reduces version-sync burden (only marketplace.json + plugin.json matter)
- Simpler mental model for contributors ("no npm concerns")

### Pattern #59 post-promotion formulation (if promoted at next audit)

Proposed post-promotion formal statement:

> *T1 Claude Code plugin frameworks may distribute via Claude Code's native `/plugin marketplace add` mechanism as primary or sole install surface. Marketplace manifest (`.claude-plugin/marketplace.json`) becomes the canonical distribution anchor. Two sub-variants observed at N=2:*
>
> **59a Marketplace-with-npm-companion** — marketplace primary, npm package secondary (for discoverability or for programmatic install outside Claude Code). Example: oh-my-claudecode v27.
>
> **59b Marketplace-only** — marketplace sole surface, no npm publish (even if TypeScript build tooling present). Example: claude-hud v35.
>
> *This distribution pattern is distinct from npm install (BMAD v11, codymaster v12), `uv tool install` (spec-kit v17), shell script install (agency-agents v18), git clone (ECC v1, Superpowers v2), or pip install (markitdown v28, crawl4ai v29). It reflects Claude Code ecosystem maturation — marketplace as emerging distribution surface.*

## 7. Ecosystem-level implications

Claude Code's native plugin marketplace mechanism creates a **distribution-channel monopoly** for Claude-Code-integrated tools. Consequences:

- **Discovery:** Users find plugins via `/plugin marketplace list` rather than npm search or general Google. Marketplace curation / featured-plugins becomes high-leverage.
- **Install friction:** Near-zero for Claude Code users (3 commands). Infinite for non-Claude-Code users (can't install outside CC).
- **Update propagation:** Anthropic controls the `/plugin update` mechanism. Author can push updates but users opt-in per-update.
- **Security model:** Anthropic controls what gets indexed as a marketplace source (`marketplace add` happens per-user-consent).

**Contrast with MCP:** Model Context Protocol servers (Pattern #18 MCP consumer) are cross-runtime (Claude Code + Cursor + Codex + etc.) and use transport-level agnostic install. Marketplace native is narrower — Claude Code only.

**Pattern relationship:** #18 (Agent Runtime Standardization) has universal-transport layer (MCP) + runtime-specific layer (OpenClaw+Hermes + claude-code-plugin-marketplace). Pattern #59 is the claude-code-plugin-marketplace layer observation at N=2. **If #59 promotes, consider whether it becomes a sub-pattern of #18** (runtime-native-install-surface emergence across runtimes) or stays standalone (claude-code-specific).

## 8. Contrast with other distribution strategies in corpus

| Strategy | Pattern/Wiki | Characteristics |
|----------|--------------|-----------------|
| Git clone + manual setup | ECC v1, Superpowers v2 | Highest friction, highest transparency |
| npm install | BMAD v11, codymaster v12, multica v15 | Standard JS-ecosystem friction |
| pip install | markitdown v28, crawl4ai v29, LlamaFactory v22, Unsloth v23 | Standard Python-ecosystem friction |
| `uv tool install` | spec-kit v17 | Python-next-gen, low friction |
| Shell install script | agency-agents v18 | Bespoke script, medium friction |
| Docker | deer-flow v9, OpenHands v30, Skyvern v24 | Portability + runtime bundle |
| **Claude Code `/plugin marketplace add`** | **oh-my-claudecode v27, claude-hud v35** | **Lowest friction for Claude Code users, zero friction for non-CC users** |

claude-hud v35 is the first corpus instance where marketplace-native is the *sole* surface (59b) vs co-existing with npm (59a).

## 9. Observations at v35

1. **Pattern #59 validates v27's "likely promotes quickly" prediction** — N=2 at 8 wikis post-registration.
2. **Sub-variant emergence at N=2** — marketplace-only vs marketplace-with-npm is a meaningful distinction.
3. **Consolidation-forward discipline correctly applied** — initially considered registering #74 "Native-Plugin-Marketplace Distribution" as new candidate; rejected after overlap pre-check revealed ~100% overlap with #59. **Net candidates: +0.**
4. **Distribution surface = discovery surface** — for Claude-Code-only tools, marketplace IS the de-facto discovery channel; Reddit/Twitter/GitHub become secondary awareness funnels.
5. **Security implications** — preventive supply-chain hardening (CI-only dist/ builds) is notably strong for 3-month-old solo project; adjacent to but distinct from Pattern #66 reactive framing.

## 10. Open questions specific to Plugin Distribution

- **Will npm companion re-emerge as common sub-variant?** Most Claude-Code-native plugins with TypeScript build tooling could publish to npm cheaply; OMC did, claude-hud did not. Is 59b (marketplace-only) an author-preference or an emerging best-practice?
- **Is marketplace discoverability sufficient at scale?** claude-hud reached 20K without marketplace featuring (per observable README — no "featured" badge claim). Reddit/Twitter likely drove early traction. If marketplace scales to 10K+ plugins, will discoverability bottleneck?
- **Will Anthropic formalize curation / ratings / security-review?** Currently any GitHub repo can be `/plugin marketplace add`-ed. Supply-chain risk compounds.
- **Cross-runtime unification?** If Cursor adopts a marketplace-like mechanism, does Pattern #59 generalize across runtimes or stay Claude-Code-scoped?

## 11. Cross-references

- Pattern #59 (Plugin Marketplace Native, CANDIDATE v27) — **STRENGTHENS to N=2 at v35**; promotion-candidate at next mini-audit
- Pattern #18 (Agent Runtime Standardization, CONFIRMED v15) — claude-hud is extension-point consumer variant; runtime-native-install-surface consideration
- Pattern #2 (Distribution Evolution, CONFIRMED v6) — claude-hud has only 1 surface (marketplace); distinct from multi-surface evolution in corpus
- Pattern #66 (Supply-Chain Security Incident Response, OBSERVATION-TRACK v29) — preventive-vs-reactive axis observation

## 12. Operational takeaways for Storm Bear operator

If Storm Bear operator adopts claude-hud:

1. **Install** takes <5 min (`/plugin marketplace add jarrodwatts/claude-hud && /plugin install claude-hud && /claude-hud:setup`)
2. **Updates** propagate via `/plugin` UI on demand; version-bump in upstream triggers visibility
3. **Uninstall** also simple (`/plugin uninstall`); config.json at `~/.claude/plugins/claude-hud/config.json` removable manually
4. **Config location:** `~/.claude/plugins/claude-hud/config.json` — edit directly for advanced, or `/claude-hud:configure` for guided
5. **Roll back:** Claude Code `/plugin` likely supports version-pinning but unverified here; default is latest from main branch

## 13. Provenance

- README.md Install section analyzed 2026-04-23
- CLAUDE.md "Plugin Configuration" section analyzed 2026-04-23
- CONTRIBUTING.md release protocol analyzed 2026-04-23
- CHANGELOG.md v0.0.1-v0.0.12 analyzed 2026-04-23
- PATTERN_LIBRARY.md Pattern #59 state verified 2026-04-23

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 3.*
