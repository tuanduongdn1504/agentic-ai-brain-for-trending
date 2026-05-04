# Vault Public-Release Decision — 2026-04-28 session 68

> **Status:** ✅ DECIDED
> **v27 HIGH bundle item #4: COMPLETE**
> **Posture:** MAXIMUM TRANSPARENCY + FAST TIMELINE + SINGLE-REPO + FULL PRE-LAUNCH AUDIT
> **Builds on:** `_state/license-decision-2026-04-28.md` (MIT License committed)

---

## Operator interview answers

| Q | Answer | Meaning |
|---|---|---|
| Q1 WHAT (granularity) | **D** | WHOLE VAULT published as-is (entire `KJ OS Template/` directory) |
| Q2 WHEN (timing) | **A** | NOW — within 1-2 weeks (this week or next) |
| Q3 HOW (platform) | **F = A + C** | GitHub public repo + Anthropic skills marketplace |
| Q4 Repo posture | **A** | PUBLISH WHOLE VAULT AS-IS (single-repo; NOT separate publishing repo) |
| Q5 Pre-launch checklist | **G** | ALL OF ABOVE — full audit before public-release |

**Profile cluster:** Aggressive ship-it-with-discipline posture.

## Repo naming decision

**RECOMMENDED PRIMARY:** `agentic-ai-second-brain`
- 3-word kebab-case
- GitHub-convention compliant
- Captures 2 of 3 operator-requested keywords (Agentic AI + Second Brain)
- "Trending Wiki" goes in repo description tagline
- Highest discoverability + memorability

**ALTERNATIVES (operator pick at publish-time):**
- `agentic-second-brain-trending-wiki` (5 words; all 3 keywords explicit; longer)
- `agentic-ai-brain-for-trending` (operator's original framing; 4 words; drops "second brain" + "wiki")
- `storm-bear-agentic-brain` (operator-branded; 3 words; drops "second brain" + "trending wiki")

**Suggested repo description tagline:**
> "A second brain for agentic AI: 56-wiki trending-tools corpus + Pattern Library (39 confirmed cross-wiki patterns) + skill ecosystem. LLM Wiki pattern (Karpathy lineage), routine v2.1 autonomous orchestration. Solo-VN-Scrum-coach build."

**Final repo name + description: DEFER to operator at publish-time.** Decision-doc commits to recommendation only; operator confirms before `gh repo create`.

## What gets published (Q1=D)

**Entire `KJ OS Template/` directory → published as-is single GitHub repo.** Includes:

- ✅ `CLAUDE.md` (vault root shim)
- ✅ `GOALS.md` (vault root shim)
- ✅ `PATTERN_LIBRARY.md` (vault root shim)
- ✅ `LICENSE.md` (MIT, committed session 68)
- ✅ `_state/` chapter files (6 chapters)
- ✅ `_goals/` chapter files (2 chapters)
- ✅ `_patterns/` chapter files (6 chapters)
- ✅ `00 Notes/` (general notes + raw sources)
- ✅ `01 Journals/` (journal entries — ⚠️ ANTI-LEAK GREP REQUIRED)
- ✅ `02 Chess Moves (Long-Term Planning)/` (strategic thinking sessions — ⚠️ may contain private musings)
- ✅ `03 Projects/` (56 wiki projects, each with own CLAUDE.md)
- ✅ `04 Reviews/` (Pattern Library audit documents)
- ✅ `05 Skills/` (skill definitions — `llm-wiki-routine-v2.1.md` + `brain-setup.md` + `new-project.md` + superseded v1/v2)
- ⚠️ Unknown: any other top-level files/dirs (full repo scan needed pre-launch)

## Timing (Q2=A — NOW within 1-2 weeks)

**Target launch date:** 2026-05-12 latest (2 weeks from 2026-04-29).

**Aggressive timeline rationale:**
- Operator-discipline-restoration cycle is at peak (20-streak / 2-CONSERVATIVE-DISCIPLINE-audit / vault-refactor-complete / v56-shipped)
- Phase 4 mastery momentum
- Sooner-shipped = sooner-feedback = faster Phase 4 iteration

**Risks of NOW timeline:**
- Pre-launch audit must be thorough (Q5=G enforces this)
- Personal-info leak risk highest at fast pace
- "Ship-it-with-discipline" posture requires both ship AND discipline

**Mitigations:**
- Full Q5=G pre-launch checklist (anti-leak grep + (C) audit + don't-be-Chris-Porter + AGENTS.md template + README polish + topics)
- Decision-freeze on each phase (#5 license / #4 release / #2 publishing / #3 skill-lock) before next phase opens

## Platforms (Q3=F=A+C)

### Platform 1: GitHub public repo (primary)

- **URL:** `github.com/Cvtot/agentic-ai-second-brain` (recommended; operator confirms repo name at publish-time)
- **License:** MIT (committed session 68)
- **Visibility:** Public
- **Topics (recommended):** `agentic-ai`, `second-brain`, `llm-wiki`, `pattern-library`, `claude-code`, `obsidian-vault`, `karpathy`, `vietnamese`, `scrum-coaching`, `agent-skills`, `ai-tools-trending`
- **README.md:** Bilingual VN+EN; clear scope statement; install/clone instructions; LLM Wiki pattern explanation; Pattern Library overview; skills catalog reference

### Platform 2: Anthropic skills marketplace (secondary)

- **Skills published:** `llm-wiki-routine-v2.1.md` + `brain-setup.md` + `new-project.md` (3 actively-maintained skills)
- **Format:** Vercel-style SKILL.md (corpus reference v51 vercel-labs)
- **Distribution:** Per Anthropic skills marketplace process (claude.ai integration)
- **License compatibility:** MIT works with Anthropic skills marketplace requirements ✅

### Platforms NOT chosen at this decision

- npm package (B) — no JS-tooling wrapper at scope; defer to Phase 4 if demand emerges
- claude.ai project knowledge (D) — covered by Anthropic skills marketplace path
- Obsidian community plugin (E) — high infrastructure cost; defer indefinitely
- Other (Twitter / Substack / etc.) — out-of-scope at v27 HIGH bundle

## Repo posture (Q4=A — single-repo whole-vault)

**Repo strategy: SINGLE REPO published as-is.** No separate publishing repo; no multi-repo split.

**Implications:**
1. **Vault becomes the public artifact.** No private working space for in-flux content. All future vault work is public-by-default once published.
2. **Future commits are public.** Operator must apply pre-launch discipline to ALL future commits (anti-leak / (C) prefix / don't-be-Chris-Porter cautionary).
3. **Audit trail is public.** Full vault history including `04 Reviews/` audit documents become public-readable. Strengthens transparency / authenticity.
4. **Mistakes preserve.** Imperfections in early v1-v55 wikis stay public. Acceptable per Phase 1-3 progression authentic-record posture.

**Counter-decision considered + rejected:** Q4=B (separate publishing repo) was the conservative-default. Operator chose Q4=A (whole-vault) for maximum-transparency posture. This commits operator to public-first vault discipline going forward.

## Pre-launch checklist (Q5=G — ALL items)

**MUST EXECUTE before `gh repo create --public`:**

### Item A: `(C)` prefix audit

```bash
# Verify all AI-generated files have (C) prefix
find "/Users/Cvtot/KJ OS Template" -type f -name "*.md" \
  | xargs grep -L "^# " 2>/dev/null  # find files without H1 header
# Manually verify each (C)-prefix candidate file actually has (C) prefix
```

### Item B: Anti-leak grep (CRITICAL for Q4=A whole-vault posture)

```bash
# Personal email
grep -r "claude1@cvtot.vn" "/Users/Cvtot/KJ OS Template" 2>/dev/null

# Real names / sensitive contacts
grep -ri "duongtuan\|<real-name>" "/Users/Cvtot/KJ OS Template" 2>/dev/null

# Internal references
grep -ri "<company-name>\|<client-name>\|<private-key>" "/Users/Cvtot/KJ OS Template" 2>/dev/null

# Token/secret fragments
grep -rE "(sk-ant-|pk_|api_key|password|token)" "/Users/Cvtot/KJ OS Template" 2>/dev/null
```

**Expected matches:** Email mentions in CLAUDE.md "Operator profile" sections — these are intentional + public-safe (operator chose to be identified as `claude1@cvtot.vn`). Any other matches require redaction or removal.

### Item C: Don't-be-Chris-Porter cautionary checklist (v55 reference)

7-point self-audit:
1. ✋ Don't ship 21%-built abandoned-then-monetized work — vault is 55-wiki + Pattern Library + skills = 90%+ complete on declared scope
2. ✋ Don't omit LICENSE — ✅ MIT committed session 68
3. ✋ Don't use informal "as-is educational" claims — vault clearly states research-pattern + Karpathy lineage; not informal
4. ✋ Don't rely on generic affiliate-disclaimer — N/A (no affiliate links in vault)
5. ✋ Don't multi-repo cross-promote shallow portfolio — Q4=A single-repo avoids this trap
6. ✋ Don't use "OG / Expert / Master / Wizard" self-claims — operator profile is "solo-VN Scrum coach + developer in early-fluency phase" (honest, not hyperbolic)
7. ✋ Don't claim quantified outcomes without methodology + N + cost-basis — Pattern Library has explicit methodology + N counts + audit trail; ✅ compliant

**Verdict: vault PASSES Chris-Porter cautionary checklist.**

### Item D: AGENTS.md template choice (4-template ensemble from v53 mini-audit)

**Decision: 22c authoritative-with-shim** (closest archetype match)

**Rationale:**
- v47 aidevops 22c precedent is closest to Storm Bear archetype (solo-multi-runtime; multi-platform agent ecosystem)
- 22a monolithic (gh-aw v48) is too dense for vault's chapter-file architecture
- 22b minimum-shim (bizos v37 327B) is too sparse for 56-wiki corpus
- 22d identical-mirror (vercel-labs v51) duplicates content unnecessarily

**Implementation:**
- Create `AGENTS.md` (vault root) — short shim pointing to authoritative `CLAUDE.md`
- ~1KB content; references CLAUDE.md as source-of-truth
- Compatible with Anthropic Claude Code + OpenCode + future agentic runtimes

### Item E: README.md polish (bilingual VN+EN)

- Sections: Title + tagline / What is this / Who built / Scope / Install (clone) / Use cases / Pattern Library overview / Skills catalog / License / Contributing (or "no contributions yet — observational repository")
- Length: ~5-10KB (corpus-typical for T2/T4 entrants)
- Bilingual VN+EN side-by-side (corpus precedent: many wikis bilingual)

### Item F: Repository topics (max 20 per GitHub)

Recommended 11 topics:
`agentic-ai` / `second-brain` / `llm-wiki` / `pattern-library` / `claude-code` / `obsidian-vault` / `karpathy` / `vietnamese` / `scrum-coaching` / `agent-skills` / `ai-tools-trending`

### Item G: ALL OF ABOVE — gate to launch

Launch is gated on A through F all complete + verified. Decision-freeze at this step before any `gh repo create`.

## Pattern Library impact

**Pattern #29 License-Category Diversity** — Storm Bear vault enters corpus at MIT-permissive sub-cluster. Strengthens MIT-permissive observation count. No new candidate.

**Pattern #57 Recursive Corpus Reference** — Storm Bear vault becomes self-referential corpus subject when published. NEW STRUCTURAL FORM: vault publishes content ABOUT its own corpus. Could be Pattern #57 sub-variant **57e meta-corpus-self-reference** candidate at v57+ if vault becomes wiki subject in future corpus iteration.

**Pattern #45 Dual-Licensing** — STAYS STALE (Q5=C in license decision confirms no dual-license).

**No new candidates registered at this decision.** **20-streak ZERO-NEW-ACTIVE-CANDIDATES preserved at session 68 mid-execution.**

## Files created at this decision

- ✅ `_state/public-release-decision-2026-04-28.md` (this file)
- (deferred to next phase) `AGENTS.md` (vault root) — 22c authoritative-with-shim template; will be created in Phase 3 (#2 publishing strategy)
- (deferred to next phase) `README.md` (vault root) — bilingual VN+EN; will be created in Phase 3
- (deferred to operator at publish-time) Final repo name confirmation + `gh repo create` execution

## Decision freeze + open items for Phase 3

**FROZEN at this decision:**
- License: MIT ✅
- Granularity: Whole vault ✅
- Timeline: NOW (1-2 weeks; target 2026-05-12 latest) ✅
- Platform: GitHub public + Anthropic skills marketplace ✅
- Repo posture: Single-repo whole-vault ✅
- Pre-launch checklist: Q5=G all items ✅
- AGENTS.md template: 22c authoritative-with-shim ✅
- Repo description tagline: "A second brain for agentic AI: 56-wiki trending-tools corpus + Pattern Library (39 confirmed cross-wiki patterns) + skill ecosystem. LLM Wiki pattern (Karpathy lineage), routine v2.1 autonomous orchestration." ✅
- Repo topics: 11 topics (committed list above) ✅

**OPEN for Phase 3 / pre-launch:**
- Final repo name (3 candidates; operator picks at publish-time)
- AGENTS.md content (write 22c shim)
- README.md content (write bilingual)
- Anti-leak grep execution (verify no leaks)
- (C) prefix audit execution (verify all AI-files have prefix)
- Anthropic skills marketplace submission process (research)

## Next phase

**Phase 3 — v27 HIGH item #2 (Publishing strategy formalization)** — write AGENTS.md + README.md + skill-format compliance + distribution registry config. Estimated 60-90 min.
