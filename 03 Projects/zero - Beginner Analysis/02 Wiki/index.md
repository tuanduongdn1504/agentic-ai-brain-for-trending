# (C) Wiki index — zero (vercel-labs) v68

**Subject:** [github.com/vercel-labs/zero](https://github.com/vercel-labs/zero)
**Homepage:** [zerolang.ai](https://zerolang.ai)
**Author:** Vercel Labs (vercel-labs org; sub-org of Vercel main)
**Tier:** **PROVISIONAL T1 Augmentation NEW sub-archetype "programming-language-as-agent-substrate"** (flag for v69 Tier-Taxonomy Review T6)
**License:** Apache-2.0
**Status:** v0.1.2 (2026-05-17) — pre-1.0 experimental
**Created:** 2026-05-16 (v0.1.0) — **2 days old at wiki build**
**Stars / Forks / Watchers / Issues:** 2,100 / 136 / 9 / 14
**Commits / Releases:** 91 / 3 (v0.1.0 + v0.1.1 + v0.1.2 — all within 2-day window)
**Velocity:** **1,050 stars/day = EXTREME-VIRAL** (2nd-highest in corpus; karpathy-skills v63 ~1,186/day held the record)
**Wiki version:** v68 (2026-05-18)
**Routine:** [llm-wiki-routine-v2.2.md](../../../05 Skills/llm-wiki-routine-v2.2.md)

---

## Phase tracking

- [x] Phase 0 — Pre-flight + probe (`CLAUDE.md`)
- [x] Phase 1 — Scaffold
- [ ] Phase 2 — Source ingestion (3 clusters)
- [ ] Phase 3 — Entity pages (4 entities)
- [ ] Phase 4a — Beginner bilingual guide
- [ ] Phase 4b — NEW T1 sub-archetype proposal + Pattern #52 v69-batch addition (`01 Analysis/`)
- [ ] Phase 5 — Iteration log + Pattern Library update
- [ ] Phase 6 — Vault sync

---

## Sources fetched

| File | Size | Purpose |
|------|------|---------|
| README.md | 73 lines | Tagline / design axioms / quick start / common commands / validation |
| AGENTS.md | 107 lines | Contributor notes / project direction / safety / development / project layout / release workflow |
| CHANGELOG.md | 44 lines | 3-release history (v0.1.0 → v0.1.2; all 2026-05-16 → 2026-05-17) |
| package.json | 49 lines | Workspace config / 40+ scripts / dependencies |
| skills/zero/SKILL.md | 51 lines | Anthropic-skills-protocol bootstrap pointing to compiler-served version-matched content |

**Repository directory tree (top-level):**
- `.github/workflows/` — CI workflows
- `benchmarks/zero/` — benchmarks (written in Zero)
- `bin/` — `zero` CLI entrypoint
- `compiler-zero/` — **Zero-authored compiler (self-hosted)**
- `conformance/` — language + CLI fixtures
- `docs-site/` — public docs (zerolang.ai)
- `examples/` — small runnable programs
- `extensions/vscode/` — VS Code extension
- `native/zero-c/` — **native C compiler bootstrap**
- `scripts/` — validation + release tooling
- `skill-data/` — skill data files (compiler-served content source)
- `skills/zero/` — single SKILL.md bootstrap stub
- `tests/`

---

## Cluster plan (Phase 2)

| Cluster | Sources | Focus |
|---------|---------|-------|
| **Cluster 1: README + agent-first design philosophy** | README.md + zerolang.ai positioning | Tagline / 5 design axioms / quick-start install flow / common commands / validation scripts / pre-1.0 disclosure block |
| **Cluster 2: AGENTS.md + project direction + safety** | AGENTS.md + LICENSE | Contributor expectations / breaking-changes policy / safety expectations / development workflow / project layout / release workflow with single-maintainer attribution |
| **Cluster 3: Skills protocol + compiler architecture + CHANGELOG** | skills/zero/SKILL.md + package.json + CHANGELOG.md + native/zero-c (referenced) + compiler-zero (referenced) | Compiler-served version-matched skills / bootstrap vs full content / 40+ npm scripts / @vercel/sandbox dep / self-hosted compiler bootstrap pattern / 3-release velocity narrative |

---

## Entity plan (Phase 3, post-v2.2 Phase 0.9 WEAK INCLUDE)

| # | Entity | Slot |
|---|--------|------|
| 1 | The Zero language: design axioms + agent-first framing + pre-1.0 discipline | Core product |
| 2 | Compiler architecture: native C bootstrap + Zero-authored compiler + skill-data + CLI surface | Distribution/ecosystem |
| 3 | **Skills-Protocol-As-Binary-Bootstrap** — version-matched compiler-served skill content as Phase 4b PRIMARY-aligned deliverable | Phase 4b PRIMARY entity |
| 4 | Storm Bear meta-entity (WEAK INCLUDE — 1/4 STRICT PASS via (d) Vercel-umbrella-corpus-reference only) | Storm Bear meta |

---

## Cross-wiki siblings

| Sibling | Why |
|---------|-----|
| **v51 agent-skills-of-vercel** | Same Vercel umbrella org parent; both engage Anthropic skills protocol |
| v63 andrej-karpathy-skills | Velocity-record sibling (corpus-record 1,186 stars/day; zero v68 is 2nd at 1,050) |
| v62 codex-plugin-cc | Corporate-strategic sibling (different vendor) |
| v66 agentmemory | Skills-protocol-integration sibling |
| v67 opencode-antigravity-auth | Adjacent v2.2-routine wiki + Pattern #83 N=3→N=4 strengthening chain |

---

## Phase 4b PRIMARY routing pre-registration

**PRIMARY:** NEW T1 sub-archetype **"programming-language-as-agent-substrate"** registration document — corpus-first programming-language subject classification; explicit flag for v69 Tier-Taxonomy Review T6 to formally decide T1-extension vs NEW Tier T6. Plus Pattern #52 v69 sustained-velocity-test batch addition.

**SECONDARY:**
- Pattern #83 Honest-Deficiency-Disclosure N=4 strengthening (already PROMOTION-ELIGIBLE at N=3 from v67; this consolidates evidence)
- NEW observational candidate: **Version-Matched-Compiler-Served Skill Content** (SKILL.md bootstrap → `zero skills get zero --full` from binary)
- NEW observational candidate: **Self-Hosted Compiler Bootstrap** (native/zero-c + compiler-zero)
- NEW observational candidate: **Agent-First-Language-Substrate design philosophy** (agents as primary users from day one as design axiom)

---

## Published pre-plan

| File | Format |
|------|--------|
| `03 Published/(C) zero - Huong dan cho nguoi moi.md` | Phase 4a bilingual VN+EN beginner guide (12-13 parts) |
| `01 Analysis/(C) T1-programming-language-as-agent-substrate NEW sub-archetype registration.md` | Phase 4b proposal-document (per v2.2 discipline) |
