# Skill: Brain Setup v2

📍 **Status:** IN-FLUX (continues evolving — current version as of 2026-05-06)

> **Adapted from:** v1 `brain-setup.md` (PUBLIC-ARCHIVED 2026-05-06) + mattpocock/skills `/grill-with-docs` (v57 wiki 2026-05-06)
> **Key change vs v1:** v1 was one-shot generate. v2 is continuous: initial setup + incremental updates + lazy ADRs + glossary discipline. CLAUDE.md becomes a living artifact, not a generated-and-forgotten file.

Set up AND continuously maintain a personalized CLAUDE.md. Four invokable phases — use whichever the situation needs.

## When to Use

- **Phase 1 (initial):** New vault; CLAUDE.md missing or placeholder
- **Phase 2 (incremental):** User says "update X section", "I changed my mind about Y", or after major life/work shifts
- **Phase 3 (ADR):** User makes a hard-to-reverse decision worth preserving with rationale
- **Phase 4 (glossary):** Mid-conversation, an undefined acronym/term appears that's worth pinning down

If a CLAUDE.md already exists with real content, NEVER auto-overwrite. Phase 1 is for empty vaults. Phases 2-4 are for live ones.

## Phases (invokable independently)

| Phase | Trigger | Output |
|---|---|---|
| 1 — Initial setup | Empty/placeholder CLAUDE.md | Full CLAUDE.md from 5-round interview |
| 2 — Incremental update | User asks to update a specific section | Targeted diff to CLAUDE.md (not full rewrite) |
| 3 — Lazy ADR | Decision passes 3-gate (hard-to-reverse + surprising + trade-off-driven) | `_state/adr-YYYY-MM-DD-{topic}.md` |
| 4 — Glossary discipline | Unfamiliar term recurs in conversation | Inline CLAUDE.md glossary entry OR flag-for-user |

---

## Phase 1: Initial setup (one-shot)

This is v1's behavior. Use when the vault is fresh.

### 1a. Scan the vault

Before asking anything:

```bash
# Top-level folders
ls -d */

# Project subfolders
ls -d "03 Projects"/*/ 2>&1 || echo "No projects yet"
```

Record: which system folders exist, which projects exist under `03 Projects/`, whether `CLAUDE.md` / `GOALS.md` already exist.

### 1b. 5-round interview

Conversational. After each round, briefly summarize what you captured so the user can correct before moving on. Pacing: group related sub-questions naturally; if an answer is thin, probe once then move on. Don't interrogate.

Use AskUserQuestion for structured choices (Round 3 communication style). Everything else is open conversation.

**Round 1 — Identity & purpose:** What to call the vault, what they do (one-liner), purpose/mission, what energizes them, what they refuse to do, personal context (faith/family/health/location/life-stage).

**Round 2 — Claude's role:** What Claude should help with at vault level (not project level), what kind of thinking partner they need (strategic/accountability/creative/decision-making), the prime directive (one thing Claude must do well).

**Round 3 — Rules & boundaries:** AskUserQuestion for communication style (Blunt / Supportive / Balanced / Other). Then open: specific rules or pet peeves, file-handling preferences (default: `(C)` prefix on AI-generated, ask before editing existing), anything Claude should NEVER do.

**Round 4 — Strengths & weaknesses:** What they're genuinely great at, blind spots / recurring failure modes, default behavior under stress.

**Round 5 — Goals & current progress:** Main goal (concrete number / milestone), current state with real numbers, plan to get there, risks / time-sensitive factors. Push gently for specifics.

### 1c. Generate CLAUDE.md

Use the v1 template (preserved in `brain-setup.md` PUBLIC-ARCHIVED). Critical rules:

- **Don't fabricate.** Thin answer → thin section.
- **Use their words.** Don't sanitize "I build cool shit" into "I develop innovative solutions."
- **Folder structure auto-detected** from Phase 1a scan.
- **Weekly Update is always a blank template.** Don't pre-fill.

### 1d. Review & save

Show the full draft. Ask: "Read through it. Anything to change, add, or remove before I save?" Make targeted edits to flagged sections only — don't regenerate. Loop until confirmed. Save to `CLAUDE.md` at vault root.

### 1e. Next steps to user

Tell them: CLAUDE.md is live (read at every session start); update Weekly Update each week; create first project via New Project skill; run a Chess Moves session if goals feel vague.

---

## Phase 2: Incremental update (NEW)

When the user says "update [section] in CLAUDE.md" or "I want to change Y", DO NOT regenerate the file. Grill and diff.

### Mechanics (mattpocock `/grill-with-docs` adapted)

1. **One question at a time.** No batched questions. Wait for the answer. Build understanding incrementally.
2. **Vault-state validation.** Cross-reference user claims against actual vault state before accepting. Examples:
   - User says "I'm working on X" → check `03 Projects/` for evidence
   - User says "I shipped Y" → check git log
   - User says "my goals changed" → read current `GOALS.md` and ask what specifically shifted
   - **If reality contradicts the claim, surface the contradiction.** Don't silently update — ask.
3. **Lazy capture.** Only update CLAUDE.md when a fact has resolved (user confirmed, evidence checked). Half-formed answers stay in the conversation, not the file.
4. **Targeted diff.** Output a unified diff (or minimal Edit) against the current CLAUDE.md — never a full rewrite. The user reviews the diff, not a wall of regenerated text.
5. **Confirm before save.** Read the diff back to the user in plain English ("I'm changing X from Y to Z"). Save only after explicit "yes".

### Trigger phrases

- "Update [section] in CLAUDE.md"
- "I changed my mind about [thing]"
- "[Goal/role/rule] is different now"
- After Phase 4 glossary additions exceed ~3 inline edits in one section
- After a Chess Moves session that materially shifts strategy

### Anti-patterns (DO NOT DO)

- Regenerating CLAUDE.md from scratch when one section needs updating
- Asking 5 questions at once
- Accepting user claims without vault-state cross-reference
- Saving silently without showing the diff

---

## Phase 3: Lazy ADR (NEW)

ADR = Architecture Decision Record. Most decisions don't need one. This phase exists to keep the bar HIGH.

### 3-condition gate

Write an ADR ONLY if the decision passes ALL three:

1. **Hard-to-reverse** — undoing it would cost real work (e.g., refactoring 20 files, migrating data, re-onboarding a team)
2. **Surprising-without-rationale** — a future reader (or future-you) would ask "why did past-me do this?" and not know
3. **Genuinely trade-off-driven** — there was a real alternative; the chosen path won on some axis but lost on another

**If any condition fails, do NOT write an ADR.** A Weekly Update bullet or a comment in code is enough.

### File location

`_state/adr-YYYY-MM-DD-{topic}.md`

(Reuses the existing `_state/` chapter convention; no new folder.)

### Template

```markdown
# ADR — {Topic}

> **Date:** YYYY-MM-DD (session N)
> **Status:** {Decided / Superseded by adr-YYYY-MM-DD-X.md}
> **Decided by:** {operator name}

## Context

What situation forced the decision? What was the constraint, deadline, or pressure?

## Decision

What was chosen. One paragraph.

## Alternatives considered

- **Option A** — what it was, why rejected
- **Option B** — what it was, why rejected
- **Chosen:** why it won

## Trade-offs accepted

What we GAVE UP by choosing this path. (If you can't list anything, it's probably not ADR-worthy.)

## Reversibility cost

What would it take to reverse? (Concrete: hours / files touched / external commitments.)

## Cross-references

- CLAUDE.md sections affected: …
- Other ADRs: …
- Related wiki / project entries: …
```

### Invocation

User says: "ADR this", "this is an ADR", "preserve this decision". Skill checks the 3-gate. If gate fails, say so explicitly: "This doesn't pass the [missing condition] gate — a Weekly Update bullet is enough. ADR skipped."

### Cross-reference back to CLAUDE.md

After writing an ADR, add a one-line reference to the relevant CLAUDE.md section: `> **ADR:** see _state/adr-YYYY-MM-DD-{topic}.md`. Don't duplicate the rationale into CLAUDE.md — the ADR is the source of truth.

---

## Phase 4: Glossary discipline (NEW)

CLAUDE.md should hold the vault's domain vocabulary so Claude doesn't repeatedly ask "what does X mean?"

### Trigger

Mid-conversation, an acronym, nickname, or jargon term appears that:
- Isn't defined in CLAUDE.md or any `_state/` chapter
- Has been used 2+ times in this session OR is likely to recur
- Has a real, stable meaning (not a one-off label)

### Two paths

**(a) Define inline in CLAUDE.md** — if term is recurring + stable + vault-specific. Use a Glossary subsection or inline definition where it first appears in context. Keep it ONE LINE.

**(b) Flag for user** — if term is fuzzy, contested, or you suspect the user means something specific you don't know. Ask: "When you say [X], do you mean [interpretation A] or [interpretation B]?" Don't define until resolved.

### Anti-patterns

- Pre-emptive glossary additions (don't define terms that haven't been used)
- Long definitions (one line, max two)
- Defining everything in one big Glossary section — prefer inline-where-relevant
- Defining the same term in CLAUDE.md AND a `_state/` chapter — pick one

### Periodic compaction

If the inline glossary entries in CLAUDE.md grow past ~10 terms in any single section, trigger Phase 2 to extract them into a dedicated `_state/glossary.md` chapter. Phase 4's job is to MAINTAIN the vocabulary; cleaning up sprawl is Phase 2's job.

---

## Critical rules (apply to all phases)

1. **NEVER auto-overwrite a populated CLAUDE.md.** Phase 1 is for empty vaults only.
2. **NEVER fabricate.** Thin answers stay thin. Vault-state contradictions get surfaced, not ignored.
3. **NEVER batch questions in Phase 2-4.** One question at a time. Mattpocock discipline.
4. **NEVER write an ADR that fails the 3-gate.** A Weekly Update bullet is fine.
5. **ALWAYS show the diff before saving** in Phase 2.
6. **ALWAYS suggest a next action** at the end of each invocation (per Storm Bear prime directive).

## Relationship to v1

v1 `brain-setup.md` is now PUBLIC-ARCHIVED (mirrors v1/v2/v2.1 routine versioning convention). v1's content is fully reachable as a historical record. v2 SUPERSEDES v1 for active use:

- Phase 1 of v2 = v1's full skill, condensed. Detail preserved in v1 file for reference.
- Phases 2-4 are NEW capabilities not present in v1.
- Vault should default to v2 going forward.

## Lineage / provenance

- **v1 lineage:** Storm Bear vault, codified 2026-04-17, proven across initial vault setup
- **`/grill-with-docs` lineage:** mattpocock/skills, MIT license, decades-of-engineering-experience claim, methodology-grounded (Pragmatic Programmer + DDD + XP + Philosophy of Software Design)
- **Convergence (v57 wiki finding):** Storm Bear vault and mattpocock/skills are independent evolutions of similar agent-skills-system patterns. v2 explicitly cross-pollinates the most useful primitive (`/grill-with-docs` continuous-CONTEXT-maintenance) into vault discipline.
- **Cross-skill-coherence observation:** This is the **2nd interview-as-skill convergence in corpus** (v1 brain-setup ↔ /grill-me at one-shot tier; v2 brain-setup ↔ /grill-with-docs at continuous tier).

## Next action

After codification: invoke Phase 2 once on the current root CLAUDE.md to dogfood the incremental-update flow — pick one section that feels stale, grill it, output the diff. Calibrates Phase 2 mechanics before broader use.
