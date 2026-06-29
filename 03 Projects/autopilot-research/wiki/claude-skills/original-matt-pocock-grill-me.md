# Original: Matt Pocock "Grill Me" (→ Process Interviewer)

*A structured interview framework for extracting tacit process knowledge before implementation.*

## Summary

Matt Pocock's **grill-me skill** is a Claude Code capability that forces systematic interrogation of a plan or design *before* building. The skill asks one clarifying question at a time, walking decision trees until both Claude and the user reach shared understanding. Ben AI adapted this pattern into his [[claude-skills/original-anthropic-agent-skills|Process Interviewer meta-skill]], embedding Anthropic prompt-engineering best practices and second-brain context-awareness.

## What Grilling Solves

**The core problem:** Misalignment between intent and execution. The user thinks they've explained what they want. The implementer builds something. It doesn't match. Grilling-the-user *before acting* surfaces hidden assumptions, contradictory requirements, and vague terminology that surface-level planning misses.

Matt Pocock's philosophy: **Slow down, interrogate thoroughly, document shared understanding, then build.**

## Structure & Mechanics

### Grill-me (Matt Pocock Original)

- **Entry point:** User describes a plan, design, or problem statement (usually fuzzy, incompletely specified)
- **Interview loop:** Skill asks 1 question at a time; user answers; skill reflects back understanding; moves to next branch
- **Termination:** Skill continues until all decision branches are resolved and a complete decision tree is documented
- **Output:** Confirmed summary of the agreed plan + full specification ready for implementation
- **Optional enhancement:** AI-generated recommended answers (user confirms instead of re-explaining)

### Grill-with-docs (Matt Pocock Sibling Skill)

Sister skill that extends grilling to domain modeling:
- Asks same interview questions
- Requests creation of **CONTEXT.md** (domain model / shared vocabulary)
- Requests **ADR documentation** (Architecture Decision Records)
- Outputs ready-to-ship codebase scaffolding
- Designed for larger teams or complex domains where documentation debt is load-bearing

### Process Interviewer (Ben AI Adaptation)

Ben AI's adaptation layers in Anthropic-native patterns:

- **Interview depth:** 10–15+ questions (more exhaustive than grill-me baseline)
- **Outputs:** Confirmed summary + full **PRD/brief** embedding [[claude-skills/original-anthropic-agent-skills|Anthropic's skill-building best practices]]
- **Second-brain awareness:** ⚠️ If workspace/second-brain is configured, the skill **checks first** to avoid asking questions already answered in prior sessions (scope unverified)
- **Integration:** Outputs a PRD designed to bootstrap skill creation *or* complex task scoping (not just documentation)

## Key Takeaways

- **Grilling is interrogation discipline, not dialog:** Questions target *specificity* (replacing vague terms with concrete scenarios), *completeness* (walking decision trees to leaf nodes), and *alignment* (confirming shared understanding before execution).

- **One-at-a-time questions prevent decision paralysis:** By asking one clarifying question, waiting for reflection, then moving to the next branch, the user has cognitive space to surface hidden concerns. Batch questioning (FAQ-style) allows surface answers; grilling surfaces buried contradictions.

- **Documentation as execution prerequisite:** Both grill-me and grill-with-docs treat documentation (summary, CONTEXT.md, ADRs) as *required output*, not optional artifact. Structured discovery precedes implementation — a spec-driven-development discipline.

- **Second-brain compounds the pattern:** ⚠️ Ben's Process Interviewer feature (checking workspace before re-asking) is plausible but unverified in implementation scope — unclear whether it integrates with [[ai-operating-system/_index|OS-like second-brain setups]] or just simple workspace files.

- **Grill-me vs plan-mode:** Grill-me is *prescriptive interrogation*. Plan-mode assumes the user already knows what they want; both Claude and user rush to execution. Grilling forces explicit reasoning *before* the expensive phase (coding, design, implementation). Cost: 15–45 min interview. Benefit: eliminates mis-shipment and rework cycles.

- **The operator already uses this:** grill-with-docs was cross-ported into the vault's brain-setup pattern v2. Interrogation-before-implementation is the same principle whether applied to task scoping or skill design.

## Source

- **Matt Pocock's grill-me skill:** github.com/mattpocock/skills
- **Matt Pocock's grill-with-docs:** github.com/mattpocock/skills (grill-with-docs)
- **Grill-me adoption & viral notes:** aihero.dev/my-grill-me-skill-has-gone-viral
- **Ben AI's Process Interviewer adaptation:** YouTube 'Eight Claude Skills I Can't Live Without' (bXnRA3pJavE, 2026-04-18); ⚠️ free plugin at c.benai.co/8csiu-free (URL not independently verified)
- **Anthropic skill-building best practices:** platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

## Installation & Usage

**Grill-me / Grill-with-docs:**
```
Install: npx skills add mattpocock/skills
Invocation: /grill-me [describe your plan] or /grill-with-docs [describe design]
Session time: 15–45 min typical
Output: Specification summary (grill-me) or CONTEXT.md + ADRs (grill-with-docs)
```

**Process Interviewer (Ben AI):**
```
Install: ⚠️ Free plugin c.benai.co/8csiu-free or search Claude Code marketplace
Invocation: Likely /process-interviewer [fuzzy task/plan]
Output: Confirmed summary + PRD/brief + optional second-brain context
```

## Cross-References

- [[claude-skills/original-anthropic-agent-skills|Original: Anthropic Agent Skills Framework]]
- [[claude-skills/the-eight-meta-skills|Ben AI's Eight Meta-Skills Overview]]
- [[ai-operating-system/_index|AI Operating System (Second-Brain Architecture)]]
