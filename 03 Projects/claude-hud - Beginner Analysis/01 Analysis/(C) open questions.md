# Open questions — claude-hud wiki v1

Tracked during build for follow-up or future wiki cross-reference.

## Unresolved at v35

1. **Solo-one-hit-flagship vs ecosystem-portfolio axis in Pattern #17** — Jarrod Watts has 144 public repos but only claude-hud reached 20K+. Prior Pattern #17 data points were multi-publisher (Yeachan's oh-my-codex sibling, Luong's 15+ companion repos, Shayan's 3-pinned portfolio). Is "one-hit-flagship within large portfolio" a distinct variant? N=1 at v35 (claude-hud); observational only. **Follow-up:** flag if 2nd similar case emerges (large portfolio + single breakout utility).

2. **Governance-depth counter-evidence to Pattern #12** — claude-hud has 7 governance files on a 3-month-old solo project. Pattern #12 currently states governance-depth correlates with organization (not scale). claude-hud is counter-evidence. Is Pattern #12 too narrowly framed, or is claude-hud anomaly? Hypothesis: **solo-with-professional-aspiration** sub-variant (author anticipates project outgrowing solo maintainership, front-loads governance). **Follow-up:** if 2nd solo-heavy-governance emerges, consider registering.

3. **Australian regional-archetype** — 1st Australian T1 in corpus. NOT registered per consolidation-forward discipline (would be 4th standalone regional-archetype fragment; #73 meta-pattern instead). **Follow-up:** if 2nd Australian T1 emerges, #73 meta-pattern sub-variant 73d registerable; if no 2nd Australian within 5 wikis, observational only.

4. **Native-plugin-marketplace vs npm binary split** — claude-hud has `package.json` + TypeScript + `npm run build` but does NOT publish to npm (no "publishConfig" entry; marketplace is sole install path). oh-my-claudecode v27 DOES publish to npm (`oh-my-claude-sisyphus@latest`) alongside marketplace. Is npm-companion optional for marketplace-native pattern? **Follow-up:** Pattern #59 sub-variant tracking (59a with-npm-companion / 59b marketplace-only).

5. **Does plugin.json "version" field actually trigger auto-updates?** — CONTRIBUTING.md claims Claude Code compares `version` in plugin.json against installed version. Not independently verified from outside Claude Code. Noted as author claim.

6. **Heavy test fixture discipline at 3-month-age** — TESTING.md describes unit + integration + golden-output tests with `tests/fixtures/` directory. Pattern #4 (testing culture) reinforcement possible but not primary wiki focus.

7. **Chinese-opt-in i18n pattern** — claude-hud has EN as default, `language: "zh"` as explicit opt-in. Contrast with claude-howto v32 (4 languages auto-exposed at README level) and TrendRadar v19 (bilingual CN+EN README). Is "opt-in-via-config-flag i18n" a distinct sub-pattern? Probably too narrow to register; noted.

## Resolved during build

- **T1 12-way vs sub-classification framing** — Resolved: use scope-axis sub-classification (broad-methodology vs narrow-display-plugin) framing instead of unwieldy 12-way matrix.
- **New candidate budget** — Resolved: 0 new candidates registered (consolidation-forward discipline + overlap pre-check correctly rejected #74 proposal).

---

*(C) Claude-generated 2026-04-23.*
