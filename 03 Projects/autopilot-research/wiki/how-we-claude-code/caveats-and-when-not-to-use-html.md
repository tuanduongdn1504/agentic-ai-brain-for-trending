# Caveats — When NOT to Use HTML, and Where the Workshop Over-reaches

> The workshop is an enthusiastic *"how we do it"* — it under-states the trade-offs. Thariq Shihipar's own writing is more balanced, and independent analysis adds more. This page is the counterweight (vault Rule 7: surface conflicts; Rule 12: fail loud). **Directly relevant to this vault, which is a Markdown LLM-Wiki.**

## When Markdown still wins (per Thariq himself)

Thariq names explicit cases where HTML is the *wrong* choice:

- **READMEs / GitHub docs** — platform rendering + universality.
- **Slack / Discord / chat** — universality; HTML doesn't paste.
- **RAG / retrieval systems** — Markdown is *"cheaper, more accurately parsed, and easier to version."*
- **Agent-to-agent communication** — Markdown is **2–4× cheaper** in tokens and parsed more reliably.
- **Collaborative editing** — needs specialized tools; HTML doesn't co-edit well.
- **Git-heavy workflows** — *"the HTML is a noisy artifact"*; diffs become unreadable.

> *"When the document has a third-party reader who will not modify it … Markdown [is right] when the document is collaborative, indexed, or destined to be consumed by automatic pipelines."* — Thariq

## The cost/ephemerality trade-offs the talk omits

- **Token cost is real:** HTML runs **2–4× Markdown's tokens**. Arno's "it's not less efficient" is a *long-run-iterations* argument, not a per-document one.
- **~99% is scaffolding:** Thariq estimates only ~1% of the tokens he generates reach production code. HTML artifacts are largely **disposable** by design.
- **Ephemerality:** *"the trail evaporates when the tab closes."* Markdown is greppable, diffable, source-traceable institutional memory; HTML is a moment.
- **Accessibility:** AI-generated HTML *"often lacks ARIA attributes, descriptive alt text, and consistent tab order"* — needs explicit WCAG constraints in the prompt. (Matters for hireui — hiring tools have ADA exposure.)

## Security — treat agent-generated HTML as untrusted

- **Refeed prompt-injection:** hidden instructions in HTML comments become prompt vectors when the file re-enters a Claude session.
- **JS + cookies:** embedded JavaScript runs with access to authenticated domain cookies.
- **Mitigation:** treat agent HTML as **untrusted input**; prefer self-contained files (inline CSS/JS, base64 images, system fonts, no runtime network calls).

## Where the Bitter Lesson analogy over-reaches

- Sutton's lesson is about **means** (don't hand-engineer features; let search/learning find them) on problems with a **fixed objective + ground truth** (win the game).
- Arno extends it to **ends** ("the model extracts your requirements better than you define them"). Requirement-*definition* has **no ground truth without you** and introduces objective-misalignment risk Sutton's framing doesn't address.
- **Safe reading:** use the interview to *surface* latent requirements collaboratively; **you still own and endorse the objective.** Don't treat a model's proposal as your revealed preference.

## Implications for THIS vault and hireui

- **Keep the wiki in Markdown.** It is exactly Thariq's "RAG / indexed / agent-to-agent / version-controlled institutional memory" case. HTML belongs to *ephemeral* artifacts (a one-session spec, a design mockup, a review dashboard) — not the persistent knowledge base.
- **HTML for specs/mockups/reviews; Markdown for memory + agent pipelines.** That split is the honest takeaway, not "HTML everywhere."
- For hireui HTML specs: add a **WCAG 2.2 AA** constraint to the prompt and **never re-feed** an agent-generated HTML file without treating it as untrusted.

## Key Takeaways

- The workshop's three pillars are sound, but **"HTML over Markdown" is conditional, not absolute** — Thariq draws the line himself.
- **Markdown wins for:** READMEs, chat, RAG, agent-to-agent, collaborative editing, version control — i.e. most of what this vault does.
- **HTML wins for:** ephemeral, human-facing, single-session, visual/interactive specs & reviews.
- Treat agent HTML as untrusted; demand accessibility explicitly; keep ownership of the objective.
- See [[how-we-claude-code/pillar-2-html-specs-over-markdown]] and [[how-we-claude-code/pillar-1-interview-and-bitter-lesson]] for the positive case.
