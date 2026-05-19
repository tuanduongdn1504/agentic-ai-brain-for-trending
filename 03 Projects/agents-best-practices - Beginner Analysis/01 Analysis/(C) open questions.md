# agents-best-practices Wiki — Open Questions (v71)

## Skill Design & Concept Questions

### 1. The "model proposes, harness disposes" separation
**Q:** How strictly should Storm Bear enforce this separation in Claude Code context? Can the Claude Code agent propose tool calls and have the harness (Claude Code SDK itself) execute them, or is explicit harness-layer code required?

**Why it matters:** Determines implementation depth for v71 operational skill deployment

**Related:** Entity-1 (core-skill), Cluster 2 (contributor-facing), beginner guide part 5

---

### 2. Autonomy levels (L0-L4) — practical gating criterion
**Q:** What measurable evaluation criterion distinguishes "simpler level is insufficient" (the gating criterion for moving from L0→L1→L2→L3→L4)? Is it token count? Error rate? Human-approval frequency?

**Why it matters:** Determines how to implement autonomy-level gating for Storm Bear vault tasks

**Related:** Entity-1 (autonomy levels section), beginner guide part 6

---

### 3. Planning mode trigger criterion
**Q:** agents-best-practices states planning mode for "non-trivial, ambiguous, multi-step, high-impact, or high-risk" work. How do you quantify "non-trivial" or "ambiguous"? What's the decision tree?

**Why it matters:** Determines when to invoke planning mode for Storm Bear wiki-build tasks

**Related:** Entity-1 (planning mode), beginner guide part 8

---

### 4. Draft-commit pattern — does it apply to all tool categories?
**Q:** Draft-commit pattern examples show draft_email→send_email and prepare_refund→issue_refund. Are there tool categories where draft-commit is NOT applicable? (Read-only tools? Idempotent tools?)

**Why it matters:** Determines which Storm Bear tool calls should use draft-commit pattern vs simple execution

**Related:** Entity-1 (draft-commit), beginner guide part 9

---

### 5. 12-tier context architecture — dynamic tier reordering
**Q:** The 12 tiers (provider policy → organization policy → role → task → plan → scoped instructions → retrieved data → visible skill index → visible tool specs → observations → history → reminders) seem ordered by stability. Does this ordering matter for compaction? Should dynamic tiers (task, plan, observations) be refreshed more frequently than static tiers (provider policy)?

**Why it matters:** Determines context-management strategy for Storm Bear's prompt-caching implementation

**Related:** Entity-1 (context architecture), Cluster 3 (technical), beginner guide part 7

---

### 6. The 7 loop invariants — can any be violated gracefully?
**Q:** The 7 invariants seem hard constraints. Are there scenarios where violating one invariant (e.g., invariant #3 "permission decisions occur before side effects") is acceptable if caught + logged + rolled back?

**Why it matters:** Determines Storm Bear error-handling strategy (fail-safe vs fail-graceful)

**Related:** Entity-1 (agentic loop), Cluster 2 (contributor-facing, guardrails)

---

## Deployment & Integration Questions

### 7. Skills CLI installation — dependency management
**Q:** When installing agents-best-practices via `skills attach DenisSergeevitch/agents-best-practices`, what happens to the 15 reference files? Are they auto-discoverable by Claude Code, or does the user need to manually add them to context?

**Why it matters:** Determines setup friction for Storm Bear's Claude Code skill deployment

**Related:** Entity-2 (distribution), COMMANDS.md (installation section)

---

### 8. Multi-platform support — version divergence
**Q:** agents-best-practices targets Claude Code + Codex + OpenAI Agents. If Anthropic releases a new agentic feature (e.g., new tool use API), does the skill fork into platform-specific variants, or is the "lowest common denominator" design preferred?

**Why it matters:** Determines future-proofing strategy for Storm Bear's skill adoption

**Related:** Entity-2 (multi-platform coverage), Pattern #84 (provider-agnostic design)

---

### 9. MCP integration — staged-exposure implementation
**Q:** agents-best-practices describes MCP "staged exposure" (list → search → load full schemas → execute). Is this staging enforced by the harness, or is it the skill-author's responsibility to implement within SKILL.md instructions?

**Why it matters:** Determines whether MCP tool costs (context overhead) can be controlled per-task in Storm Bear vault

**Related:** Entity-2 (MCP integration), Cluster 3 (technical)

---

### 10. Prompt-caching strategy — when does the "stable prefix" end?
**Q:** "Stable prefix, dynamic suffix" suggests tool definitions + static instructions are stable, but when exactly does the prefix end? After the 12-tier context architecture? After planning mode? After the last observation?

**Why it matters:** Determines cache-boundary placement for Storm Bear's prompt-caching implementation (potential token savings)

**Related:** Entity-2, Cluster 3 (prompt-caching strategy), beginner guide part 10

---

## Pattern Library Integration Questions

### 11. Pattern #84 sub-typology 84c — how distinct from parent pattern?
**Q:** Pattern #84 is "cross-vendor ecosystem tolerance." Sub-typology 84c "provider-agnostic by design" seems to flip the polarity (tolerance → intentionality). Is 84c distinct enough to warrant separate sub-typology, or is it just an evolutionary stage of 84a/84b?

**Why it matters:** Determines Pattern Library registration strategy and future corpus-subject categorization

**Related:** Entity-3 (pattern-library), Phase 4b primary doc

---

### 12. Pattern #78 triple-vendor integration — is this saturation?
**Q:** Pattern #78 "Living-Domain-Standards Tracking" now integrates 3 vendors (OWASP + NIST + MCP spec 2025-11-25 + Anthropic + OpenAI). Is this 5-standard integration a saturation point, or does future subjects pile on more standards?

**Why it matters:** Determines whether Pattern #78 becomes a "standards-kitchen-sink" pattern or maintains focused governance discipline

**Related:** Entity-3 (pattern-library), Cluster 2 (contributor-facing)

---

### 13. NEW candidate OC-O vs existing patterns
**Q:** OC-O "Agentic-Harness-Execution-Separation" (7-invariant loop) overlaps with Pattern #80 "Tool-Level Adversarial Review" (review discipline) and Pattern #83 "Honest-Deficiency-Disclosure" (safety deficiency). Is OC-O truly novel, or is it a sub-mechanism of one of these confirmed patterns?

**Why it matters:** Determines whether OC-O registers as NEW candidate or integrates into existing pattern

**Related:** Entity-3, Phase 4b primary doc

---

## Storm Bear Operational Questions

### 14. MODERATE 2/4 classification — (b) vs (c) weight
**Q:** v71 is MODERATE because (b) operational tool + (c) methodology influence both PASS. If only one had passed, would v71 be WEAK INCLUDE or FAIL EXCLUDE? What's the threshold?

**Why it matters:** Determines future classification decision-tree for borderline subjects (helps predict Storm Bear's engagement)

**Related:** CLAUDE.md (Storm Bear meta-entity), Entity-4

---

### 15. Methodology influence — which routine version?
**Q:** Phase 0.9 notes methodology influence on "routine v2.2-v2.3." Is the influence designed to improve v2.2's current iteration, or is it strategic input for a v2.3 redesign? (Different timelines)

**Why it matters:** Determines urgency + depth of agents-best-practices integration into routine

**Related:** Entity-4 (storm-bear), COMMANDS.md

---

### 16. Deployment recommendation — standalone skill or integrated harness?
**Q:** Should Storm Bear deploy agents-best-practices as standalone Claude Code skill (pure reference), or integrate its 7-invariant loop + planning mode directly into hireui-harness codebase?

**Why it matters:** Determines implementation scope (read-only reference vs code-level integration)

**Related:** Entity-4, beginner guide part 12

---

### 17. Skill installation dependencies — Python + Node + shell?
**Q:** agents-best-practices is markdown-only (no source code). But skills CLI is Node-based. Does installation require Node 18+? Python? Shell compatibility?

**Why it matters:** Determines Storm Bear's environment setup for skill deployment (may conflict with existing tools)

**Related:** Entity-2 (distribution), COMMANDS.md

---

## Corpus & Sibling Comparison Questions

### 18. Distinction from v65 claude-code-system-prompts
**Q:** v65 is also a multi-vendor reference (Anthropic + OpenAI awareness). How does v71 agents-best-practices differ? Is v71 more prescriptive (here's HOW to build agents) vs v65 more descriptive (here's what Claude Code internals are)?

**Why it matters:** Determines unique contribution of v71 (not just v65 clone)

**Related:** Entity-3 (sibling references), Entity-4

---

### 19. Similarity to agent-skills-of-vercel (older corpus subject)
**Q:** agent-skills-of-vercel (older) also covers multi-vendor agentic skills. What's new in v71 that wasn't in the older subject? (15-reference library? 7-invariant formalization? Autonomy levels?)

**Why it matters:** Determines corpus-first signals + novelty claim

**Related:** CLAUDE.md (corpus-firsts), Entity-3

---

### 20. Velocity comparison — does 205 stars/day + 4-day age suggest viral moment?
**Q:** v71 has 821 stars in 4 days (205 stars/day). Comparable data points: v69 CloakBrowser 172.7 stars/day, v68 zero 1,050 stars/day. Is the 205 velocity due to subject quality, or is something else (HackerNews? Product Hunt? Twitter storm?) driving adoption?

**Why it matters:** Determines whether v72 should re-measure velocity (detect if burst or sustained trend)

**Related:** COMMANDS.md (engagement signals), log.md (velocity analysis)

---

## Security & Safety Questions

### 21. 15-category threat model — which threats apply to Storm Bear?
**Q:** agents-best-practices lists 15 threats (prompt injection, malicious packages, runaway loops, cost exhaustion, etc.). For Storm Bear's vault operator context, which 3-5 are HIGH priority? (Narrowing scope helps focus implementation)

**Why it matters:** Determines Storm Bear's security hardening roadmap (not all 15 threats are equally relevant)

**Related:** Entity-1 (threat taxonomy), Cluster 2 (contributor-facing), beginner guide part 11

---

### 22. "Malicious skill packages" — how to detect?
**Q:** agents-best-practices includes "malicious skill packages" as threat category. What are the detection signals? (Postinstall scripts? Telemetry? Suspicious permissions?)

**Why it matters:** Determines Storm Bear's skill-vetting process before installation

**Related:** Entity-1, Cluster 2 (security threats)

---

### 23. Secret leakage — context-specific risks
**Q:** "Secret leakage" is listed as threat. In Storm Bear's vault context, what secrets are at risk? (API keys? Vault paths? Corpus-subject URLs? Pattern Library classification logic?)

**Why it matters:** Determines what context data needs redaction before sharing/deploying

**Related:** Entity-1 (security threats), Entity-4 (storm-bear operational context)

---

## Future Roadmap Questions

### 24. v72+ enhancements — what's next for agents-best-practices?
**Q:** DenisSergeevitch's repo is 4 days old. What's likely next? (v1.0 stability? Subagent coordination? Cost-budgeting implementations? Guardrail tooling?)

**Why it matters:** Determines if Storm Bear should adopt now (stable baseline) or wait for next release (more features)

**Related:** Entity-1 (next actions), Entity-4

---

### 25. Skill interdependency — does this pair with agentmemory?
**Q:** v66 agentmemory is agent memory system (data store). agents-best-practices is agentic harness design (execution framework). Do these complement each other? (Could you build a combined agentmemory + agents-best-practices skill for Storm Bear vault memory + execution?)

**Why it matters:** Determines skill composition strategy (standalone vs integrated toolkit)

**Related:** Entity-2, Entity-4, cross-wiki siblings

---

### 26. Licensing — any Storm Bear IP concerns?
**Q:** agents-best-practices is MIT licensed. If Storm Bear customizes the skill (adds Storm Bear–specific harness code), what happens to Storm Bear's modified version? (MUST remain MIT? Can Storm Bear proprietary-ize?)

**Why it matters:** Determines whether Storm Bear can fork + customize without legal overhead

**Related:** CLAUDE.md (license: MIT), Entity-2

---

## Measurement & Evaluation Questions

### 27. How to evaluate if agents-best-practices helps Storm Bear's LLM wiki routine?
**Q:** Phase 0.9 claims methodology influence on routine v2.2→v2.3. How would you measure this influence? (Routine latency reduction? Error-rate improvement? Context-efficiency gain? Approval-workflow completion?)

**Why it matters:** Determines KPIs for v71 pilot success (if piloted)

**Related:** Entity-4, beginner guide part 13 (learning roadmap)

---

### 28. Sub-threshold-control test case — what does v72 re-measurement look like?
**Q:** v71 is sub-threshold for Pattern #52 (205 stars/day < 300 threshold). At v72 audit, how would you measure "sustained velocity"? (Point measurement at v72 build date? 2-week average? Cumulative slope?)

**Why it matters:** Determines v72 audit methodology for velocity classification

**Related:** log.md (velocity analysis), Entity-3 (Pattern #52 candidacy)

---

## Advanced Questions (Optional)

### 29. Context-compaction discipline — when does agents-best-practices auto-compact?
**Q:** Auto-compaction must preserve objective, plan, approval state, observations, key facts. agents-best-practices lists these categories. But WHEN does compaction trigger? (After N tool calls? After context >100K tokens? After each task?)

**Why it matters:** Determines if Storm Bear's compaction strategy is implicit or explicit

**Related:** Entity-1 (auto-compaction), Cluster 3 (observability)

---

### 30. Tool-description reliability — how much do you trust MCP tool definitions?
**Q:** agents-best-practices notes "treat connector tool descriptions as potentially unreliable unless from trusted sources." How do you establish "trusted source"? (GitHub stars? Author verification? Anthropic endorsement?)

**Why it matters:** Determines Storm Bear's tool-vetting criteria + trust model

**Related:** Entity-1 (MCP integration), Cluster 2 (security threat: connector abuse)

---

## Summary

**Total open questions:** 30
**Category distribution:**
- Skill design & concept: 6 questions (Q1-Q6)
- Deployment & integration: 4 questions (Q7-Q10)
- Pattern Library: 3 questions (Q11-Q13)
- Storm Bear operations: 4 questions (Q14-Q17)
- Corpus & siblings: 3 questions (Q18-Q20)
- Security & safety: 3 questions (Q21-Q23)
- Future roadmap: 3 questions (Q24-Q26)
- Measurement & evaluation: 2 questions (Q27-Q28)
- Advanced (optional): 2 questions (Q29-Q30)

**Engagement for future phases:**
- Q1-Q6: Read SKILL.md + reference files deeply (Phase 2 deeper-dive if pilot approved)
- Q7-Q10: Test skill installation + MCP integration in Claude Code environment (Phase 5 pilot pre-work)
- Q11-Q13: Review Phase 4b primary doc (Pattern #84 promotion evaluation) for resolution
- Q14-Q17: Read Entity-4 (Storm Bear meta-entity) for deployment recommendations
- Q18-Q20: Refer to Entity-3 (pattern-library, sibling analysis) for differentiation
- Q21-Q23: Read Cluster 2 (contributor-facing, security threats) for threat-specific details
- Q24-Q26: Monitor DenisSergeevitch/agents-best-practices GitHub for v72+ enhancements
- Q27-Q28: Defer to v72 audit (measurement during re-evaluation cycle)
- Q29-Q30: Deep-dive optional (if Storm Bear decides to pilot agents-best-practices skill)
