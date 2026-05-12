# Cluster 3 — EXAMPLES.md illustration corpus

## What this cluster covers

The 522-line `EXAMPLES.md` file — code-driven illustration of all 4 principles via deliberate ❌/✅ before-after pairs. This is the **pedagogical core** of the artifact; the README + SKILL.md + CLAUDE.md state the principles, but EXAMPLES.md teaches them.

## Structure

8 worked examples (2 per principle):

| Principle | Example 1 | Example 2 |
|-----------|-----------|-----------|
| **1. Think Before Coding** | Hidden Assumptions ("export user data") | Multiple Interpretations ("make search faster") |
| **2. Simplicity First** | Over-abstraction ("calculate discount") | Speculative Features ("save preferences") |
| **3. Surgical Changes** | Drive-by Refactoring ("fix empty email bug") | Style Drift ("add logging to upload") |
| **4. Goal-Driven Execution** | (additional examples in remainder of file) | (additional examples in remainder of file) |

## Pedagogical pattern: ❌-then-✅ contrastive

Each example follows identical structure:

1. **User Request** (one line, realistic)
2. **❌ What LLMs Do** (concrete failure-mode code, often 30-40 lines)
3. **Problems** (bullet list naming what's wrong)
4. **✅ What Should Happen** (corrected version, usually much shorter)

**Key teaching device:** the failure-mode code is REALISTIC, not strawman. It looks like code an LLM would actually generate — typed, abstracted, "professional"-looking — but solves a problem that wasn't asked.

## Example 1.1 dissected — "Hidden Assumptions"

**Request:** *"Add a feature to export user data"*

**❌ failure-mode (30 lines):** Function with `format='json'/'csv'` params, hardcoded file paths, hardcoded fieldnames `['id', 'email', 'name']`, dumps ALL users.

**Problems named:**
- Assumed it should export ALL users (privacy implications)
- Assumed file location
- Assumed which fields to include
- Assumed CSV fieldnames without checking actual data

**✅ correct:** Don't write code. Ask 4 clarifying questions: scope / format intent / fields / volume. Suggest minimal start (paginated JSON API endpoint).

**Pedagogical move:** the ✅ is **NOT code** — it's *a clarification dialog*. This is unusual for code-examples docs. It teaches that "implementing" the wrong thing is the failure; the correct first response can be zero code.

## Example 2.1 dissected — "Over-abstraction"

**Request:** *"Add a function to calculate discount"*

**❌ failure-mode (40+ lines):** `DiscountStrategy` ABC + `PercentageDiscount` + `FixedDiscount` + `DiscountConfig` dataclass + `DiscountCalculator` class + 30+ lines of setup.

**✅ correct (3 lines):**
```python
def calculate_discount(amount: float, percent: float) -> float:
    """Calculate discount amount. percent should be 0-100."""
    return amount * (percent / 100)
```

**Pedagogical move:** explicit ratio comparison — 40 lines vs 3 lines for same functional outcome. Operator gets visceral feel for "would a senior engineer say this is overcomplicated?" test.

**Caveat included:** *"When to add complexity: Only when you actually need multiple discount types. If that requirement comes later, refactor then."* — anti-YAGNI explicit.

## Example 3.1 dissected — "Drive-by Refactoring"

**Request:** *"Fix the bug where empty emails crash the validator"*

**❌ failure-mode (diff):** Adds docstring + reformats variables + adds `.split('@')[1]` validation + adds username minimum-length check + adds `isalnum()` check.

**✅ correct (diff):** Modifies ONLY the 2 lines that fix empty-email handling. Email-format check beyond the bug stays as-is. Username untouched.

**Pedagogical move:** **diff-format presentation** makes the surgery explicit. Reader sees `+`/`-` lines and can directly count "drive-by" changes vs "request-fulfilling" changes.

## Example 3.2 — "Style Drift" (in-progress in source)

**Request:** *"Add logging to the upload function"*

**❌ failure-mode (diff):** Adds type annotations, adds docstring, **changes single quotes to double quotes**, refactors return logic, removes blank lines.

**Pedagogical signal:** quote-style change is the most insidious — semantically identical, but pollutes the diff and reviewer attention.

## What the EXAMPLES.md teaches that the principles DON'T

The 4 principles are abstract; EXAMPLES.md anchors them in:

1. **Concrete realistic failure-modes** — not strawmen
2. **Diff-aware surgical-change discipline** — visualizes which lines trace to request
3. **Clarification-dialog as legitimate first response** — not all requests need code
4. **Senior-engineer-overcomplication test** — operationalizable judgment heuristic
5. **Anti-YAGNI explicit** — defer abstraction until concrete second use case

## Cross-corpus comparison: pedagogical density

| Subject | Pedagogical artifact | Lines | Examples |
|---------|---------------------|------:|----------|
| **andrej-karpathy-skills v63** | EXAMPLES.md | 522 | 8 explicit ❌/✅ pairs |
| cc-sdd v61 | docs/why-cc-sdd.md + spec-driven.md | similar scale | Methodology rationale |
| mattpocock-skills v57 | per-skill SKILL.md docs | distributed | Per-skill scenario |
| spec-kit v17 | docs + agent prompts | extensive | Methodology-driven |

karpathy-skills' EXAMPLES.md is **density-high pedagogical artifact** — single 522-line file, all examples colocated, contrastive-by-design. Compare to mattpocock's distributed-per-skill model.

## What's NOT in EXAMPLES.md

- No tests / no test framework setup
- No project-specific constraints / no language-stack restrictions
- No machine-verifiable rubric (visual judgment only)
- No "how to use this with [specific stack]" guidance

The artifact accepts that **judgment cannot be machine-verified**. It teaches taste, not a checklist.

## Connection to Pattern #51 Vibe-Coding Spectrum

EXAMPLES.md takes a **clear stance: anti-overengineering, anti-silent-assumption, pro-clarification**. But it does NOT take an anti-vibe stance — it doesn't argue against vibe-coding workflow itself. The `Tradeoff Note` explicitly calibrates: trivial tasks don't need full rigor.

This is **NEUTRAL on workflow + anti-overengineering on output** — a distinct spectrum point not currently captured in Pattern #51's existing observations (anti-vibe-with-pragmatic-acknowledgment cc-sdd / NEUTRAL free-claude-code / anti-vibe-pure earlier subjects).
