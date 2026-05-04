# Cluster — Governance + CI discipline + release cadence

**Sources:** `CHANGELOG.md` (12.4 KB, 12 releases from v0.0.1 to v0.0.12 + Unreleased) + `CONTRIBUTING.md` (2.1 KB) + `CODE_OF_CONDUCT.md` (1.3 KB — not read verbatim; noted) + `SECURITY.md` (458 bytes) + `SUPPORT.md` (373 bytes) + `MAINTAINERS.md` (153 bytes) + `TESTING.md` (2.4 KB) + `RELEASING.md` (529 bytes — not read verbatim; CONTRIBUTING covers the same ground) + repo topology inference.

**Cluster purpose:** Captures the governance discipline layer — how contributions are managed, how releases happen, what the security posture is, what tests gate PRs.

---

## 1. 7-file governance surface (CORPUS NOTABLE at 3-month-old solo project)

| File | Size | Purpose |
|------|------|---------|
| CODE_OF_CONDUCT.md | 1.3 KB | Community conduct expectations |
| CONTRIBUTING.md | 2.1 KB | How to contribute + development commands + version-bump protocol |
| SECURITY.md | 458 B | Private advisory reporting flow |
| SUPPORT.md | 373 B | Support expectations (latest-release only, best-effort) |
| MAINTAINERS.md | 153 B | Maintainer list (just Jarrod) |
| TESTING.md | 2.4 KB | Test strategy + layers + fixtures + CI gate |
| RELEASING.md | 529 B | Version-bump procedure (overlaps CONTRIBUTING) |

**Plus:**
- LICENSE (MIT, 1.1 KB)
- README.md / README.zh.md (18 KB each)
- CHANGELOG.md (12.4 KB)
- CLAUDE.md + CLAUDE.README.md (18 KB combined)

**Observation — counter-evidence to Pattern #12 (Governance-Depth):**

Pattern #12 currently states: *"Corporate-backed projects formalize agent documentation more"* (established at v13 gws with tri-file CLAUDE+AGENTS+CONTEXT, reinforced at v17 spec-kit). The operative correlation was **organization → governance depth** (NOT scale or age).

**claude-hud is N=1 counter-evidence:**
- 3-month-old project
- Solo author
- 20K stars (medium-scale, not enterprise)
- 7 governance files (unusually heavy for this profile)

**Possible explanations:**
1. **Solo-with-professional-aspiration** — author anticipates project outgrowing solo maintainership, front-loads governance. (Testable hypothesis; would need N=2.)
2. **Anthropic-ecosystem-norm** — Claude Code ecosystem projects may be adopting heavier governance baseline due to closeness to Anthropic corporate culture. (Plausible; OMC v27 also had SECURITY + CONTRIBUTING; claude-code-best-practice v34 was lighter.)
3. **Template-driven** — author used a governance-file template set (possibly GitHub's community standards templates). (Likely; the files are uniformly terse, which suggests template-instantiation.)

**Registration decision:** Do NOT register as new candidate. Observational only; flag as open question (#2 in `01 Analysis/(C) open questions.md`). If 2nd solo-heavy-governance T1 emerges at ≤1 year age, reconsider as **#12 refinement** toward multi-axial framing (org × age × ecosystem-norm).

---

## 2. Release cadence (CHANGELOG analysis)

| Version | Date | Days since prior |
|---------|------|-----------------|
| v0.0.1 | 2025-01-04 | — (initial) |
| v0.0.2 | 2025-01-04 | 0 (same day, security fix) |
| v0.0.3 | 2025-01-06 | 2 |
| v0.0.4 | 2026-01-07 | — *(likely CHANGELOG typo — 2025-01-07; see note below)* |
| v0.0.5 | 2026-01-14 | 7 |
| v0.0.6 | 2026-01-14 | 0 (same day) |
| v0.0.7 | 2026-02-06 | 23 |
| v0.0.8 | 2026-03-03 | 25 |
| v0.0.9 | 2026-03-05 | 2 |
| v0.0.10 | 2026-03-23 | 18 |
| v0.0.12 | 2026-04-04 | 12 |
| (Unreleased) | current | — |

**Note on date anomalies:**
- CHANGELOG lists v0.0.1-v0.0.3 as 2025 dates, v0.0.4+ as 2026 dates. GitHub API gives created_at as 2026-01-02. The 2025 dates may be CHANGELOG typos for 2026, OR they may reflect a private development period pre-public-release.
- **v0.0.11 is missing from CHANGELOG** — possibly skipped or retracted release.

**Cadence summary:**
- 12 releases over ~3 months (~4 releases/month early, tapering to ~2-3 releases/month after v0.0.7)
- Rapid early iteration (5 releases in first 2 weeks)
- Stabilizing cadence as product surface matures

**Velocity signals:**
- Each release has 3-10 changes (Added / Changed / Fixed / Dependencies categories)
- Author references PR numbers in CHANGELOG entries — contribution acknowledgement habit
- v0.0.6 is a major layout refactor (expanded vs compact modes, introduced in single release)
- v0.0.7 redesigned default layout (2-line clean default replacing prior multi-line default)

**Observation:** The product went through 2 major default-layout redesigns in 1 month (v0.0.6 Jan 14 → v0.0.7 Feb 6). Author willing to break defaults for cleaner UX. Migration notes documented per release.

---

## 3. PR → CI → dist workflow (CONTRIBUTING.md)

**Build discipline enforced:**

```
Your PR: src/ changes only → Merge → CI builds dist/ → Committed automatically
```

Explicit rule: **"PRs should only modify files in `src/` — do not include changes to `dist/`."**

Rationale from v0.0.2 CHANGELOG:
> *Add CI workflow to build dist/ after merge - closes attack vector where malicious code could be injected via compiled output in PRs*
> *Remove dist/ from git tracking - PRs now contain source only, CI handles compilation*

**Observation — corpus-notable security practice:** This is a **supply-chain hardening** pattern. Attack vector: malicious PR includes compiled output that differs from source, reviewer misses the diff in minified/built code. Fix: never review dist/ in PRs; CI deterministically rebuilds post-merge.

**Cross-reference:** Pattern #66 Supply-Chain Security Incident Response (OBSERVATION-TRACK at v29 for crawl4ai's `unclecode-litellm` fork response). claude-hud's pre-emptive dist-exclude-from-PR is a **preventive** supply-chain pattern, distinct from #66's reactive incident response. **NOT registered as new candidate** — observational only, consolidation-forward discipline.

---

## 4. Testing strategy (TESTING.md)

### Goals
- Validate core logic (parsing, aggregation, formatting) deterministically
- Catch HUD output regressions without manual review
- Keep tests fast (<5s) for frequent contributor runs

### 3 test layers

1. **Unit tests** — Pure helpers (`getContextPercent`, `getModelName`, formatters)
2. **Integration tests** — CLI with sample stdin + fixture transcript
3. **Golden-output tests** — Full output snapshot comparison for subtle UI regressions

### Fixtures

- `tests/fixtures/` — small JSONL files, one-behavior-each (basic tool flow, agent lifecycle, todo updates)

### Running

```bash
npm test                    # Build + node --test
npm run test:coverage       # Build + c8 coverage
npm run test:update-snapshots  # Regenerate golden outputs
```

### CI gate

- `npm ci` → `npm run build` → `npm test`
- GitHub Actions runs `test:coverage` on Node 18 + Node 20

**Observation:** Testing discipline is **strong for 3-month project age**. Golden-output tests (snapshot testing) on statusline output is a natural fit — terminal output is deterministic after fixture freeze.

**Cross-reference:** Pattern #4 (testing discipline) observations in corpus have been strongest at T4 bridge libraries (notebooklm-py v7, graphify v16, gws v13) which had real-user-facing API surfaces. claude-hud's statusline-snapshot testing is parallel — user sees the output, output must not regress.

---

## 5. CONTRIBUTING.md — release protocol

**3-file version bump discipline:**

```
1. Update version numbers in:
   - package.json → "version": "X.Y.Z"
   - .claude-plugin/plugin.json → "version": "X.Y.Z"
   - .claude-plugin/marketplace.json → "version": "X.Y.Z"

2. Update CHANGELOG.md with changes since last release

3. Commit and merge — CI builds dist/ automatically
```

**Observation — triple-manifest version sync:** Unusually specific protocol. Package.json is npm-convention (even though claude-hud doesn't publish to npm — retained for tsconfig/build tooling). plugin.json is claude-plugin-metadata. marketplace.json is Claude Code marketplace-manifest.

**Implication:** Users updating via `/plugin marketplace update` see version changes only when marketplace.json bumps. If author forgets to bump marketplace.json specifically, user won't get update.

**Cross-reference:** Pattern #59 (Plugin Marketplace Native) strengthened to N=2 at v35. This 3-file version-bump discipline is a sub-concern of marketplace-native distribution — observational.

### Version strategy

Semantic versioning (MAJOR.MINOR.PATCH):
- **PATCH** (0.0.x) — bug fixes, minor improvements
- **MINOR** (0.x.0) — new features, non-breaking changes
- **MAJOR** (x.0.0) — breaking changes

**Observation:** Project is still 0.0.x (pre-1.0). Per author's own scheme, current state is "bug fixes and minor improvements" even though v0.0.6 / v0.0.7 included major layout redesigns that are plausibly breaking for users with hand-edited configs. Migration notes documented case-by-case (e.g., v0.0.6 migration: `layout: "default"` → `lineLayout: "compact"`).

---

## 6. SECURITY.md (458 bytes — brief)

```
Security fixes are applied to the latest release series only.

Reporting a Vulnerability:
Please report security issues through GitHub's private advisory flow:
https://github.com/jarrodwatts/claude-hud/security/advisories/new

We will acknowledge receipt within 5 business days.
```

**Observation:** Standard GitHub advisory workflow. No PGP key, no bounty, no severity rubric. Minimal but present.

**Cross-reference:** Pattern #24 (SECURITY.md as T1 standard) — originated v16 (graphify), strengthened v17 (spec-kit), v18 (agency-agents), v32 (claude-howto 334-line heavy SECURITY.md). claude-hud is **5th T1 data point** for SECURITY.md presence. Pattern #24 is strongly approaching confirmed at this count. Will verify in Phase 5 against PATTERN_LIBRARY.md.

---

## 7. SUPPORT.md

```
This project is maintained on a best-effort basis.

What We Support:
- The latest release
- Claude Code versions documented in README.md
- Node.js 18+ or Bun

We cannot guarantee response times, but we will triage issues as time allows.
```

**Observation:** **Honest scope-limiting** — explicit "no guarantee" framing. Contrast corporate-backed T1 (spec-kit v17) which has more expansive support language.

---

## 8. MAINTAINERS.md (153 bytes — terse)

```
- Jarrod Watts (https://github.com/jarrodwatts)

If you are interested in becoming a maintainer, open an issue to start the conversation.
```

**Observation:** Explicit path for multi-maintainer future. **Single-maintainer today with documented path to change.** Small but significant — signals author is aware of bus-factor risk and open to succession.

---

## 9. CHANGELOG contributor credits

Named PR contributors per release:

| Contributor | First PR | Contributions |
|-------------|----------|---------------|
| @Tsopic | #32 | Config system, layouts, path levels, git toggle |
| @melon-hub | #34 | Usage API, configure skill, bug fixes |
| @r-firpo | #30 | Autocompact buffer ideas |
| @yansircc | #43 | Autocompact buffer ideas |
| @StephenJoshii | #49 | Autocompact buffer ideas |

**Plus numerous numbered PRs acknowledged** (#105, #106, #107, #108, #109, #110, #111, #121, #126, #132, #137, #141, #142, #144, #146, #148, #153, #154, #155, #157, #158, #159, #161, #162 visible in CHANGELOG).

**Observation:** Active PR contribution flow despite solo maintainership. Author credits prolifically. **Community-around-solo** pattern — similar to spec-kit (GitHub backs but solo-ish maintainer) or agency-agents v18 (msitarzewski solo with Reddit-viral community).

---

## 10. Observations for downstream phases

1. **7-file governance surface is corpus-notable** — counter-evidence to Pattern #12 (governance-depth → organization correlation). N=1; observational only.
2. **PR→CI→dist workflow is preventive supply-chain hardening** — distinct from reactive Pattern #66; observational.
3. **Release cadence ~4/month early, tapering to ~2/month** — active iteration with documented migrations per major change.
4. **Testing discipline strong for age** — 3 test layers including golden-output snapshots. Pattern #4 reinforcement.
5. **Triple-manifest version bump** — sub-concern of Pattern #59 Plugin Marketplace Native; observational.
6. **SECURITY.md is 5th T1 data point** for Pattern #24 (approaching strong-confirmed if not already).
7. **Honest scope-limiting** in SUPPORT + SECURITY + README caveats — consistent author voice across all governance files.
8. **Single-maintainer documented succession path** — bus-factor-aware but not bus-factor-solved.
9. **Named contributor credits in CHANGELOG** — community acknowledgement discipline, reinforces community-around-solo pattern.
10. **Date anomalies in CHANGELOG** (2025 vs 2026 first three releases) — noted for fact-verification (not consequential to wiki conclusions).

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 2.*
