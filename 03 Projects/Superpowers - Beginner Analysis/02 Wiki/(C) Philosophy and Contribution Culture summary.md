# (C) Philosophy and Contribution Culture Summary

> **Source:** `00 Sources/superpowers/CLAUDE.md` (6.5KB) + `00 Sources/superpowers/skills/test-driven-development/SKILL.md` (372 lines)
> **Ingested:** 2026-04-18
> **Coverage:** Full files

---

## TL;DR

**VI:** Superpowers có **văn hoá đóng góp cực strict** — repo public ghi rõ "94% PR rejection rate", warn AI agents về consequences khi submit slop. Philosophy là **"Iron Law" framing** (TDD = "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"), **anti-pattern detection tables** (11+ rationalizations + 13+ red flags), và **hard gates trong skills** (`<HARD-GATE>` blocks). Khác ECC's "best practice" tone — Superpowers dạy agent **recognize own rationalization** và STOP.

**EN:** Superpowers has an extremely strict contribution culture — the public repo states "94% PR rejection rate" and warns AI agents about consequences for submitting slop. Philosophy: **"Iron Law" framing** (TDD = "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"), **anti-pattern detection tables**, and **hard gates in skills**. Differs from ECC's "best practice" tone — Superpowers teaches the agent to **recognize its own rationalizations** and STOP.

---

## "If You Are an AI Agent" — opening warning

CLAUDE.md mở đầu với section đặc biệt cho AI agents. Tóm gọn:

> **"This repo has a 94% PR rejection rate. Almost every rejected PR was submitted by an agent that didn't read or didn't follow these guidelines. Maintainers close slop PRs within hours, often with public comments like 'This pull request is slop that's made of lies.'"**

> **"Your job is to protect your human partner from that outcome. Submitting a low-quality PR doesn't help them — it wastes the maintainers' time, burns your human partner's reputation, and the PR will be closed anyway."**

**5 mandatory checks trước khi PR:**
1. **Read entire PR template** at `.github/PULL_REQUEST_TEMPLATE.md` — fill **every** section với real, specific answers (not placeholders)
2. **Search existing PRs** — open AND closed — cho duplicate problem
3. **Verify is real problem** — push back nếu user chỉ nói "fix some issues" without specific experience
4. **Confirm change belongs in core** — domain-specific = standalone plugin, not core
5. **Show complete diff** to human partner + get explicit approval

> **"If any of these checks fail, do not open the PR."**

---

## What Will NOT Be Accepted (8 categories)

1. **Third-party dependencies** — Superpowers is "zero-dependency by design"
2. **"Compliance" changes to skills** — Superpowers' philosophy DIFFERS from Anthropic's published guidance, deliberately. Compliance PRs need extensive eval evidence.
3. **Project/personal/team-specific configuration** — belongs in own plugin
4. **Bulk or spray-and-pray PRs** — không trawl issue tracker, mỗi PR cần genuine understanding
5. **Speculative/theoretical fixes** — "my review agent flagged this" KHÔNG đủ; phải có specific session/error/UX motivating
6. **Domain-specific skills** — portfolio building, prediction markets, games → standalone plugin
7. **Fork-specific changes** — không sync fork upstream
8. **Fabricated content** — invented claims, hallucinated functionality → close immediately

---

## "Skill Changes Require Evaluation"

Quote nguyên văn:
> **"Skills are not prose — they are code that shapes agent behavior."**

**Process khi modify skill:**
- Use `superpowers:writing-skills` skill để develop + test
- **Adversarial pressure testing** across multiple sessions
- **Show before/after eval results** trong PR
- Don't modify carefully-tuned content (Red Flags tables, rationalization lists, "human partner" language) without **evidence**

**Carefully-tuned content** (không touch):
- Red Flags tables
- Rationalization lists
- "Your human partner" language
- Iron Law framing

→ Skills are **behavior-shaping artifacts**, not prose. Treat như code.

---

## Iron Law framing (từ TDD skill)

**Pattern characteristic của Superpowers:**

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

**Wording is intentional:**
- ALL CAPS = non-negotiable
- "Iron Law" framing
- Following with consequence: "Write code before the test? **Delete it. Start over.**"
- "**No exceptions:** Don't keep it as 'reference'. Don't 'adapt' it while writing tests. Don't look at it. **Delete means delete.**"

**Compare ECC tone:**
> "Use this skill when implementing any feature or bugfix. Enforces test-driven development with 80%+ coverage."

ECC: prescriptive, helpful guidance.
Superpowers: legalistic, non-negotiable mandate.

**Chosen deliberately** — per CLAUDE.md, "carefully-tuned for real-world agent behavior."

---

## Anti-pattern detection tables

Skills của Superpowers có **2 distinctive table types** không có trong ECC:

### "Common Rationalizations" table

Liệt kê excuses agent có thể nghĩ ra + counter-argument. From TDD skill:

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Tests after achieve same goals" | Tests-after = "what does this do?" Tests-first = "what should this do?" |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "Deleting X hours is wasteful" | Sunk cost fallacy. Keeping unverified code is technical debt. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. **Delete means delete.** |
| "Need to explore first" | Fine. Throw away exploration, start with TDD. |
| "Test hard = design unclear" | Listen to test. Hard to test = hard to use. |
| "TDD will slow me down" | TDD faster than debugging. Pragmatic = test-first. |
| "Manual test faster" | Manual doesn't prove edge cases. You'll re-test every change. |
| "Existing code has no tests" | You're improving it. Add tests for existing code. |

→ Agent gặp 1 trong 11 patterns → recognize → counter immediately, không rationalize.

### "Red Flags - STOP and Start Over" table

Liệt kê specific anti-pattern phrases agent should detect + STOP:

```
- Code before test
- Test after implementation
- Test passes immediately
- Can't explain why test failed
- Tests added "later"
- Rationalizing "just this once"
- "I already manually tested it"
- "Tests after achieve the same purpose"
- "It's about spirit not ritual"
- "Keep as reference" or "adapt existing code"
- "Already spent X hours, deleting is wasteful"
- "TDD is dogmatic, I'm being pragmatic"
- "This is different because..."
```

> **"All of these mean: Delete code. Start over with TDD."**

→ Self-policing mechanism. Agent monitors own internal monologue cho these patterns.

---

## Hard gates in skills

`brainstorming` skill mở đầu với:

```
<HARD-GATE>
Do NOT invoke any implementation skill, write any code, scaffold any project,
or take any implementation action until you have presented a design and the
user has approved it. This applies to EVERY project regardless of perceived simplicity.
</HARD-GATE>
```

→ XML-style tags để mark non-negotiable boundaries. ECC không có pattern tương tự.

---

## "Your human partner" terminology

Throughout skills, agent **không** call user "the user" hoặc "you" — luôn "your human partner".

**Quoted rationale từ CLAUDE.md:**
> *"Superpowers has its own tested philosophy about skill design, agent behavior shaping, and **terminology (e.g., 'your human partner' is deliberate, not interchangeable with 'the user')**."*

**Effect dự đoán:**
- Frames human as collaborator, not customer/operator
- Anchors agent identity (tools partner with humans, not serve them)
- Distinctive voice — instantly recognizable Superpowers content

→ ECC dùng "you" + "the user" interchangeably — no enforced voice.

---

## "Mandatory workflows, not suggestions"

README closes 7-stage workflow section with:

> **"The agent checks for relevant skills before any task. Mandatory workflows, not suggestions."**

→ Skills auto-trigger qua description matching, agent enforced to use. ECC's skills can be invoked or skipped — Superpowers' skills enforce themselves.

---

## "Spec self-review" pattern

`brainstorming` skill có step #7 explicit: "Spec self-review — quick inline check for placeholders, contradictions, ambiguity, scope".

→ Agent reviews own work before passing to user. Build trust qua self-check.

---

## Evaluating skill quality (the meta-skill)

`writing-skills` skill (chưa đọc full nhưng implied) is the **meta-skill** cho contributing.

**Per CLAUDE.md:**
- Skills must work across all supported coding agents
- Skill changes need eval evidence
- Adversarial pressure testing required
- "Skills are not prose — they are code that shapes agent behavior"

→ Treat skills as production code. ECC treats them as documentation.

---

## Connection to Storm Bear vault

**Pattern Storm Bear có thể adopt:**

1. **"Iron Law" framing** cho mandatory rules trong vault CLAUDE.md? E.g., `(C)` prefix là Iron Law, ASK before edit existing files là Iron Law.
2. **Anti-pattern tables** trong vault skills? Vd `llm-wiki-ingest` skill có thể có "Common Rationalizations" cho ingest workflow.
3. **Hard gates** trong skills? Vd `brain-setup` có thể có `<HARD-GATE>` cho "must complete all 5 rounds before generating CLAUDE.md".
4. **"Your human partner"** terminology test-drive cho 1 skill?
5. **Spec self-review** pattern cho mọi document Storm Bear ship.

**Storm Bear hiện tại closer to ECC tone:** prescriptive best practices, không legalistic mandates. Worth experimenting with Superpowers tone cho high-stakes skills.

---

## Open questions từ ingest này

1. ⏸ **Eval methodology cho skills** — "extensive eval evidence" claim. Format/methodology cụ thể? **→ đọc `writing-skills/SKILL.md`.**
2. ⏸ **`writing-skills` skill anatomy** — meta-skill, đáng đọc full.
3. ⏸ **History của 94% PR rejection rate** — empirical data từ đâu? Public stats không?
4. ⏸ **"Adversarial pressure testing"** — cụ thể là gì? Pattern reusable cho Storm Bear?

---

## Cross-references

- [[(C) README summary]] — overview của Superpowers
- [[(C) index]]
- [[(C) log]]
- [[../01 Analysis/(C) open questions]]

## Citations

- `00 Sources/superpowers/CLAUDE.md` (full file, 6.5KB, lines 1–~150)
- `00 Sources/superpowers/skills/test-driven-development/SKILL.md` (lines 1–372) — TDD Iron Law + Common Rationalizations + Red Flags tables
- Excerpt patterns observed: hard gates, "your human partner" usage
