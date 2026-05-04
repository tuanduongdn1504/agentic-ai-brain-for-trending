# (C) Party Mode + Scale-Domain-Adaptive Planning

> **Type:** Entity — unique primitives (novel to BMAD in T1 corpus)
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README + VN summary]] §5
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

BMAD-METHOD ships two novel primitives not observed in other T1 frameworks: **Party Mode** (multi-agent collaboration in a single session) and **Scale-Domain-Adaptive Planning** (planning depth auto-adjusts to project complexity). Both are **announced but under-documented** — README provides one-line descriptions each, with algorithmic details absent. Novel but unproven empirically.

## 2. Key claims

1. **Party Mode = multi-persona collaboration** — "Bring multiple agent personas into one session to collaborate and discuss" (README)
2. **Scale-Domain-Adaptive = auto-sizing** — "Automatically adjusts planning depth based on project complexity" (README)
3. **Both are novel in T1 corpus** — no equivalent in ECC/Superpowers/gstack/GSD
4. **Both are under-documented** — no algorithm exposed publicly
5. **Both are v6-era features** — consistent with skills-architecture rewrite

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| Party Mode exists + tagline | README.md | High (explicit) |
| Scale-Domain-Adaptive exists + tagline | README.md | High (explicit) |
| No algorithm published for Scale-Adaptive | README.md (absence) | High |
| Novelty vs T1 peers | Cross-wiki comparison (Phase 4b) | High |
| Empirical effectiveness | — | **Unverified** |

## 4. How it works — Party Mode

### Mechanics (inferred)

1. User invokes Party Mode (exact CLI command not fetched)
2. User specifies N agents to include (e.g., PM + Architect + Amelia + UX)
3. Each agent loaded as persona in single conversation context
4. Agents take turns responding, each maintaining persona voice
5. User can direct specific agent (@PM) or let orchestration decide

### Possible implementation patterns (speculative)

- **Round-robin:** Each agent speaks in sequence
- **Moderated:** One "chair" agent routes turns
- **Free-for-all:** Agents respond when relevant to their domain
- **User-driven:** User explicitly addresses

README doesn't specify. `tools/skill-validator.md` or `bmad/bmm/workflows/party-mode.md` likely hold details (not fetched).

## 5. How it works — Scale-Domain-Adaptive Planning

### Mechanics (inferred)

1. User states project goal
2. BMAD assesses **scale** (code LOC? team size? deadline?) and **domain** (game dev? enterprise? prototype?)
3. Planning workflow chooses depth: quick-spec vs full-PRD vs architecture-doc vs all three
4. Output = appropriately-sized planning artifact

### Signals likely used (speculative)

- Project size (file count, repo age)
- Domain cues (package.json contents, framework detection)
- User-stated urgency or scope
- History of past BMAD use in this project

### Is this LLM-based or heuristic?

- **Heuristic:** Fixed rules in workflow `.md` — fast, predictable, fragile
- **LLM-based:** Amelia/PM reasons about appropriate depth — flexible, slower, non-deterministic

README doesn't say. Logged to Q9 (existing).

## 6. Worked example — Party Mode

**Scenario:** Designing new feature (startup, 5-person team, existing Node backend)

```
> bmad-party PM Architect Amelia UX

[PM] Let's clarify scope first. What's the user problem?
[user] Users lose sessions on page refresh

[UX] Quick question — is this a new feature or addressing a complaint?
[PM] Complaint-driven. Let's write a brief PR/FAQ.

[Architect] Heads up — session storage has 3 approaches:
  1. localStorage (client-only)
  2. Server-side sessions (stateful)
  3. Cookie + stateless JWT
  Trade-offs...

[Amelia] I'll spike #3 if we go that route. 1 day.

[user] Let's go with #3
[PM] drafting PR/FAQ now...
[Architect] ADR for JWT approach...
[Amelia] setting up test harness...
```

**Value:** One session captures multi-perspective reasoning. Contrast: invoking agents serially loses cross-agent challenge.

## 7. Edges + failure modes

### Party Mode

- **Coherence degradation** — N agents → context bloat → responses lose persona fidelity
- **Infinite loops** — agents debate without resolution; user must break in
- **Token cost** — multi-persona context = expensive per turn
- **Empirical value unclear** (Q8) — is N-agent collab actually better than single strong agent? No public data
- **Orchestration failures** — no published guarantee that turn-taking works cleanly

### Scale-Domain-Adaptive

- **Wrong-size output** — if heuristic misreads scale, user gets over/under-planned artifact
- **Black-box frustration** — no way to inspect why BMAD chose that depth
- **Domain detection fragility** — mislabel a game-dev project as enterprise → wrong workflows
- **Adversarial user** — what if user wants full PRD for 10-line script? Can they force it?

## 8. Related concepts

- [[(C) 12+ Specialized Agents (Amelia Dev + PM + Architect + UX)]] — Party Mode participants
- [[(C) 34+ Workflows + 5 Module Ecosystem]] — Scale-Adaptive likely selects workflow variant
- [[(C) VN Localization + Storm Bear Direct Relevance]] — does Party Mode work in VN?

## 9. Cross-project (T1 siblings comparison)

| Primitive | BMAD | ECC | Superpowers | gstack | GSD |
|-----------|------|-----|-------------|--------|-----|
| Multi-agent in-session | **Party Mode ✅** | ❌ | ❌ | ❌ | Serial only |
| Auto-size planning | **Scale-Adaptive ✅** | ❌ | Stage-based | ❌ | ❌ |
| Meta-tooling | BMB ✅ | ❌ | ❌ | ❌ | ❌ |

→ BMAD's **novelty in T1 is real** on both primitives. No sibling has equivalents. **Whether novelty = value is unproven.**

### T5 comparison (deer-flow SuperAgent)

- deer-flow's **Sub-Agent System** = parallel fan-out (programmatic, not conversational)
- BMAD's Party Mode = conversational co-presence
- Different use cases: fan-out for parallel work; Party Mode for collaborative planning

## 10. Open questions

- Party Mode algorithm — turn-taking? Moderator? → Q28
- Party Mode empirical value vs single-agent — any benchmarks? → Q8 existing
- Scale-Adaptive heuristic vs LLM-based? → Q9 existing
- Can user force planning depth override? → Q29
- Does Party Mode preserve persona across long sessions (10+ turns)? → Q30
- VN support in Party Mode? Multi-agent VN conversation? → Q31

## 11. Decision log

- **v6.x era** (late 2025-2026): both features appeared. Exact alpha version not extracted (CHANGELOG deep-dive needed)
- **v6.3 (2026-04-09):** no mention of changes to either — features stable
- **Amelia consolidation (v6.3)** — simplifies Party Mode invocation (fewer named agents to choose among)

## 12. Storm Bear relevance

- **Party Mode for Scrum ceremonies:** Retrospectives benefit from multi-perspective input (dev + PM + QA + facilitator). Party Mode = software analog. **Pilot candidate.**
- **Scale-Adaptive for coaching teams:** Teams of varying maturity need different planning depths. If Scale-Adaptive works, Storm Bear can use BMAD across engagements without per-client tuning
- **VN verification:** Both features need VN-language testing. Storm Bear VN pilot = natural proving ground
- **Risk:** Both features are novel-but-unproven. Storm Bear should not bet production reliance on Party Mode until empirical data exists

## 13. Migration / adoption notes

- Not applicable for migration — these are discovery features, not breaking ones
- Adoption friction = low (no code change) but discovery friction = high (docs thin)
- Recommended: try Party Mode for one planning session, then assess

## References

- `README.md` §Features
- Parent wiki: [[(C) index]]
- Open question ledger: [[../01 Analysis/(C) open questions]]
- Cross-wiki:
  - `../../deer-flow - Beginner Analysis/02 Wiki/(C) Sub-Agent System (Parallel Fan-out).md` — alternative multi-agent model
