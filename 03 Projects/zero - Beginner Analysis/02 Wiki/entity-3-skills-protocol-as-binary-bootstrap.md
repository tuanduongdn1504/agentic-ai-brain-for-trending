# (C) Entity 3: Skills-Protocol-As-Binary-Bootstrap — version-matched compiler-served skill content

**Type:** Phase 4b PRIMARY entity — NEW T1 sub-archetype "programming-language-as-agent-substrate" target + NEW observational candidate
**Slot:** Entity 3 of 4
**Sibling entities:** [Entity 1 — The Zero language](entity-1-zero-language-and-agent-first-design.md) / [Entity 2 — Compiler architecture](entity-2-compiler-architecture-and-bootstrap.md) / [Entity 4 — Storm Bear meta](entity-4-storm-bear-meta.md)

---

## 1. Why this is the Phase 4b PRIMARY entity

Three reasons make this entity the PRIMARY pattern-library-implication entity for v68:

**Reason 1 — NEW T1 sub-archetype "programming-language-as-agent-substrate"** (corpus-first). Zero v68 is the first corpus subject classified at this sub-archetype. Documenting the structural properties that distinguish it from existing T1 sub-archetypes (general-purpose / curated-meta / corporate-curated / single-artifact / domain-vertical / reverse-engineering-reference-archive) is the v68 wiki's deliverable.

**Reason 2 — Skill-As-Binary-Bootstrap mechanism is corpus-first.** Zero's solution to skill-content-version-drift (thin SKILL.md stub + compiler-served version-matched content via `zero skills get zero --full`) is structurally distinct from all prior corpus skill packaging mechanisms.

**Reason 3 — v69 Tier-Taxonomy Review T6 motivation.** Whether Zero v68 fits as T1 NEW sub-archetype OR motivates NEW Tier T6 (Language/Runtime substrate) is a structural taxonomy question that v69 audit must resolve.

---

## 2. The SKILL.md bootstrap stub (verbatim)

The file `skills/zero/SKILL.md` uses Anthropic-skills-protocol frontmatter (corpus-confirmed convention):

```markdown
---
name: zero
description: Install Zero and load version-matched workflows with zero skills.
---

# Zero

Zero is the programming language for agents.

Install this skill once in an agent's skill manager. Keep it thin; Zero's own CLI serves the version-matched workflow for each installed compiler.

Install the latest release:

```sh
curl -fsSL https://zerolang.ai/install.sh | bash
export PATH="$HOME/.zero/bin:$PATH"
zero --version
```

## Version-Matched Skills

This file is a discovery stub. Do not treat it as the full Zero workflow.

Before editing, checking, testing, or repairing Zero code, ask the installed compiler for the skill content that matches that exact binary:

```sh
zero skills list
zero skills get zero
zero skills get zero --full
```

If the user has multiple Zero binaries, use the same binary that will run the project:

```sh
/path/to/zero skills list
/path/to/zero skills get zero --full
```

Use `zero skills list` to discover additional skills bundled with that Zero version. Use `zero skills get <name>` to load the one relevant to the task. Common inner skills include `zero-agent`, `zero-language`, `zero-diagnostics`, `zero-packages`, `zero-builds`, `zero-testing`, and `zero-stdlib`.
```

The body of the SKILL.md is ~50 lines. The substantive content is the **handoff instructions**: how the agent should invoke the binary to load version-matched content.

---

## 3. The architectural problem Skill-As-Binary-Bootstrap solves

**Traditional skill packaging problem:**

Skill content lives in static SKILL.md files. When the underlying tool/compiler/runtime evolves:
- SKILL.md may describe deprecated APIs
- Examples in SKILL.md may not work with current binary
- Diagnostic codes referenced in SKILL.md may have been renumbered

**The skill-version-drift problem is observable across the corpus:**
- v51 agent-skills-of-vercel: static SKILL.md per skill — drift risk
- v62 codex-plugin-cc: static skill files bundled in plugin — same
- v63 karpathy-skills: 7 frontmatter-only single-artifact skills — same
- v64 claude-seo: 25 sub-skills + 18 sub-agents as static SKILL.md — same
- v66 agentmemory: skills exposed via MCP at runtime — DIFFERENT mechanism (runtime-served via MCP)

**Zero v68's solution:**

The SKILL.md is a **thin discovery stub**. It contains 3 things:
1. The skill name + description (frontmatter — what skill managers index)
2. Install instructions (how to get the compiler binary)
3. Handoff to compiler (`zero skills get zero --full`)

The ACTUAL skill content lives in `skill-data/` (compiled into the native binary at build time) and is served via the `zero skills get` CLI command. **Skill content is version-coupled with the compiler binary.**

When you upgrade Zero, the skill content auto-upgrades with the binary.

---

## 4. The mechanism in detail

**4-step agent workflow:**

1. **Skill manager discovers the stub.** Claude Code's skills plugin / Cursor / etc. find `skills/zero/SKILL.md` (or its installed copy) — ONE Zero skill registered.

2. **Agent reads stub instructions.** Stub says: *"This file is a discovery stub. Do not treat it as the full Zero workflow. Before editing, checking, testing, or repairing Zero code, ask the installed compiler for the skill content that matches that exact binary."*

3. **Agent invokes installed binary.** Executes `zero skills get zero --full` (or `--json` for JSON output).

4. **Binary serves version-matched content.** Native compiler reads bundled `skill-data/` and returns content matching the EXACT version of the compiler binary on disk.

**Multi-binary case:** If the user has multiple Zero versions installed (e.g., project-local installations), the agent uses the SAME binary that will run the project:

```sh
/path/to/zero skills get zero --full
```

This ensures the agent's understanding matches the specific compiler version the project uses.

**7 inner skills served (per SKILL.md):**

| Inner skill | Likely focus |
|-------------|--------------|
| `zero-agent` | Agent-specific workflow guidance |
| `zero-language` | Zero language syntax + semantics |
| `zero-diagnostics` | Diagnostic codes + explanations |
| `zero-packages` | Package management workflows |
| `zero-builds` | Build target + emit options |
| `zero-testing` | Testing patterns |
| `zero-stdlib` | Standard library usage |

Plus the umbrella `zero` skill itself (the full workflow). 8 total skill targets served by the compiler binary.

---

## 5. Why this is corpus-first

**Comparison with prior corpus skill packaging:**

| Subject | Mechanism | Version-drift handling |
|---------|-----------|------------------------|
| v51 agent-skills-of-vercel | Static SKILL.md per skill (28 skills) | None — drift accumulates over time |
| v62 codex-plugin-cc | Static skills bundled in plugin (4 skills) | Plugin re-released as needed |
| v63 karpathy-skills | 7 frontmatter-only SKILL.md (no body) | None |
| v64 claude-seo | 25 sub-skills + 18 sub-agents (static SKILL.md per primitive) | Plugin marketplace re-release |
| v65 claude-code-system-prompts | NOT a skill collection (reverse-engineering archive) | N/A |
| v66 agentmemory | Skills exposed via MCP at runtime (51 MCP tools + 107 REST endpoints) | Runtime-served; auto-version-matched |
| **v68 zero** | **Thin SKILL.md stub → compiler-served bundled skill data** | **Version-coupled with binary** |

**v66 agentmemory has a similar runtime-served pattern** but via MCP (Model Context Protocol). Zero v68 uses skill protocol (Anthropic skills format) with binary-serving rather than MCP runtime.

**Distinguishing properties of Zero's mechanism:**

1. **One SKILL.md per skill registry** (no proliferation as compiler evolves)
2. **Binary owns skill content** (skill-data/ baked into native compiler at build time)
3. **Discovery-stub-to-binary-content-handoff** (stub directs to `zero skills get`)
4. **Multi-binary-coherence** (agents use the same binary as the project)

**Pattern Library novelty:** Combines (a) skill protocol with (b) runtime serving with (c) version coupling. Distinct from MCP runtime (different protocol) and from static skill packaging (no runtime). Library-vocabulary item OR NEW Pattern candidate.

---

## 6. NEW T1 sub-archetype "programming-language-as-agent-substrate"

Existing T1 Augmentation sub-archetypes:

| # | Sub-archetype | Corpus baseline | Mechanism |
|---|---------------|-----------------|-----------|
| 1 | general-purpose | v57 mattpocock-skills | 19 general-purpose skill collection |
| 2 | curated-meta | v50 awesome-claude-skills | Multi-skill aggregator with curation |
| 3 | corporate-curated | v51 agent-skills-of-vercel | Corporate-curated skill collection |
| 4 | single-artifact | v63 andrej-karpathy-skills | 7-skill viral-distillation single bundle |
| 5 | domain-vertical | v64 claude-seo | SEO-domain-vertical 25+18 collection |
| 6 | reverse-engineering-reference-archive | v65 claude-code-system-prompts | Continuous extraction of closed-vendor product internals |
| **7** | **programming-language-as-agent-substrate (NEW v68)** | **v68 zero** | **Programming language where agents are primary users; bundled skill content served via compiler binary** |

**Distinguishing properties of #7:**

1. **Primary artifact is a programming language**, not a skill collection
2. **Agents are PRIMARY users** (READ + WRITE + DEBUG Zero code), not augmentees
3. **Skill content is bundled into the language runtime** (compiler binary) rather than distributed as static files
4. **Language-level commitments to agent-readability** (5 design axioms enforce structural choices)

**N=1 stale-risk-flagged at registration** — corpus-first; needs future N=2 evidence. Hypothetical un-stale candidates:
- Other corporate-strategic-lab programming language launches (Google / Anthropic / OpenAI experimental language?)
- Existing language frameworks adopting "agent-first" framing (e.g., a future Rust-flavored "agent-first" variant)
- Language-level skill protocol integrations (other compilers bundling skill content)

**Stale-risk:** May stay N=1 if "programming language as agent substrate" is too specific. If the meta-pattern is "runtime-bundled skill content via discovery-stub-handoff" — that's broader and may apply to non-language runtimes.

---

## 7. NEW observational candidate: Skill-As-Binary-Bootstrap

**Formal statement (candidate):**

> Framework or runtime ships skill content via a thin discovery-stub SKILL.md (or equivalent skill-protocol bootstrap artifact) that explicitly directs skill managers to invoke the framework's runtime/binary/compiler for the actual version-matched skill content. Skill manager registers ONE skill per framework; runtime serves N inner skills version-coupled with installed framework version. Solves skill-content-version-drift by binding content to the runtime artifact lifecycle.

**Promotion criteria proposal (3):**

1. Thin SKILL.md (or equivalent skill-protocol artifact) explicitly identifies itself as a discovery stub (not the full skill content)
2. Stub directs agents/skill-managers to invoke the runtime for actual content (e.g., `<framework> skills get <name>`)
3. Runtime serves N inner skills bundled at build time (version-coupled with framework version)

**Required for promotion:** 2+ subjects with Skill-As-Binary-Bootstrap mechanism.

**Re-evaluation:** v70 stale-check / v73 retire-check.

**Rationale:** Solves observable skill-version-drift problem. Could be adopted by other runtimes (other compilers, agent runtimes, plugin systems). v68 zero is corpus-N=1; the mechanism's distinguishing trait (discovery-stub-to-binary-content-handoff) is structural and observable.

**Cross-reference:** Pattern #2 Distribution Evolution (CONFIRMED) — Pattern #2 describes packaging-channel evolution. Skill-As-Binary-Bootstrap is a SUB-VARIANT of Pattern #2 within the skill-protocol channel — combining static-distribution (the stub) with runtime-distribution (the binary-served content). Could register as Pattern #2 sub-variant rather than top-level pattern.

**Library-vocabulary candidate item alternative:** If mechanism doesn't reach N=2 by v70, demote to Library-vocabulary observational item.

---

## 8. Skills protocol corpus-citation chain

The Anthropic skills protocol is observable across multiple corpus subjects. Zero v68's adoption strengthens the protocol's corpus presence:

| Subject | Wiki | Skills protocol usage | Mechanism |
|---------|------|----------------------|-----------|
| awesome-claude-skills | v50 | Aggregator | Curated-meta sub-archetype |
| agent-skills-of-vercel | v51 | 28 skills | Corporate-curated sub-archetype |
| mattpocock-skills | v57 | 19 skills | General-purpose sub-archetype |
| codex-plugin-cc | v62 | Sub-skills as primitive | Cross-vendor bridge plugin |
| andrej-karpathy-skills | v63 | 7 frontmatter-only | Single-artifact sub-archetype |
| claude-seo | v64 | 25 sub-skills + 18 sub-agents | Domain-vertical sub-archetype |
| agentmemory | v66 | Runtime-served via MCP | Service-bundled |
| **zero** | **v68** | **1 stub + 7 binary-served inner skills** | **NEW: Skill-As-Binary-Bootstrap** |

**Corpus observation:** **8 corpus subjects engage the Anthropic skills protocol with structurally distinct mechanisms.** This is itself notable — the skills protocol has become a CORPUS-DOMINANT integration surface for agentic-AI subjects. Pattern #57 57c sub-variant evidence is implicit (many subjects citing the same external standard).

---

## 9. v69 Tier-Taxonomy Review T6 implications

v69 audit (already scheduled per CLAUDE.md root state) includes:

> *"Tier-Taxonomy Review T6 consideration (deferred from v66 Decision 14)"*

Zero v68 is a corpus-first programming-language subject. Whether it fits as:
- (a) **T1 NEW sub-archetype** "programming-language-as-agent-substrate" (current PROVISIONAL classification)
- (b) **NEW Tier T6 Language/Runtime substrate** (distinct from T1 Augmentation; foundational rather than augmenting)

→ v69 audit decision required.

**Arguments for (a) T1 NEW sub-archetype:**
- Skills protocol integration anchors to T1 mechanism
- Agents-as-primary-users is augmentation-axis-compatible
- Compiler-bundled skill content acts like T1 skill collection from inside the binary

**Arguments for (b) NEW Tier T6:**
- A programming language is foundational substrate, not augmentation
- T1 Augmentation has 6 prior sub-archetypes all centered on skill content; Zero is structurally different (language + compiler + ecosystem)
- Future corpus subjects (other languages, agent runtimes) need a tier home distinct from T1

**Recommended:** Defer to v69 audit decision. For v68 wiki, classify PROVISIONAL T1 NEW sub-archetype with explicit flag.

---

## 10. Cross-references to corpus

| Sibling | Why |
|---------|-----|
| **[v51 agent-skills-of-vercel](../../agent-skills-of-vercel - Beginner Analysis/CLAUDE.md)** | T1 corporate-curated sub-archetype; same Vercel umbrella org parent; both engage skills protocol |
| **[v66 agentmemory](../../agentmemory - Beginner Analysis/CLAUDE.md)** | T2 Service with runtime-served skills via MCP; structurally adjacent to v68's Skill-As-Binary-Bootstrap (both runtime-served, different protocols) |
| [v62 codex-plugin-cc](../../codex-plugin-cc - Beginner Analysis/CLAUDE.md) | T4 Bridge with skills protocol integration |
| [v63 karpathy-skills](../../andrej-karpathy-skills - Beginner Analysis/CLAUDE.md) | T1 single-artifact sub-archetype; minimal SKILL.md contrast with Zero v68's discovery-stub mechanism |
| [v64 claude-seo](../../claude-seo - Beginner Analysis/CLAUDE.md) | T1 domain-vertical sub-archetype with largest static SKILL.md count (25 + 18 = 43 primitives) — illustrates skill-version-drift problem Zero v68 addresses |

---

## 11. Pattern Library implications from Entity 3

- **NEW T1 sub-archetype "programming-language-as-agent-substrate" registration** — PRIMARY Phase 4b deliverable; N=1 stale-risk-flagged; v69 Tier-Taxonomy Review T6 decision required (T1 sub-archetype vs NEW T6).
- **NEW observational candidate: Skill-As-Binary-Bootstrap** — corpus-first mechanism; 3-criterion promotion proposal; could be sub-variant of Pattern #2 Distribution Evolution OR top-level pattern.
- **Pattern #57 corpus-citation strengthening** — 8 corpus subjects now engage Anthropic skills protocol with 7 structurally distinct mechanisms (after v68). Skills-protocol-as-corpus-dominant integration surface observation.
- **Pattern #19 ecosystem-portfolio-builder strengthening** — Vercel umbrella has BOTH v51 (main org corporate-curated skills) and v68 (vercel-labs sub-org experimental language). 2-product Vercel portfolio in corpus.

---

## 12. References

- skills/zero/SKILL.md (51 lines) — primary source for Phase 4b PRIMARY entity
- CHANGELOG.md v0.1.1 entry (skills protocol introduction)
- Cross-cluster: cluster-3 (full mechanism analysis)
- Cross-corpus: v51 + v62 + v63 + v64 + v65 + v66 + v67 skills protocol observations
- **Phase 4b PRIMARY proposal-document:** [(C) T1-programming-language-as-agent-substrate NEW sub-archetype registration.md](../01 Analysis/(C) T1-programming-language-as-agent-substrate NEW sub-archetype registration.md) (TO BE WRITTEN at Phase 4b)
