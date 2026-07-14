# The originals — five books, verified

## Source

- All quote/attribution checks run 2026-07-14 via Workflow `wf_75a9c75d-7e4` (dives + independent refute-first verifiers) — details in [[source-provenance]].

## Ousterhout — *A Philosophy of Software Design* (2018; 2nd ed. 2021)

- **Complexity definition: VERBATIM CONFIRMED** (Ch. 2, "The Nature of Complexity"): *"Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system."* Matt quotes it exactly.
- **Deep vs shallow modules: FAITHFUL PARAPHRASE CONFIRMED** (Ch. 4): best modules = powerful functionality behind simple interfaces; shallow = little functionality, complex interface. Stage rendering accurate.
- Already deep-dived in [[../pocock-agentic-workflow/the-originals]] (incl. the caveat that the AI application is Matt's extension, not Ousterhout's — the book predates the agent era).

## Hunt & Thomas — *The Pragmatic Programmer* (20th Anniversary ed., 2019)

- **Software entropy: CONFIRMED** — Ch. 1 "A Pragmatic Philosophy," **Topic 3 "Software Entropy"** (broken-windows theory). Matt's "whole chapter" is a topic, close enough.
- **"No one knows exactly what they want": CONFIRMED** — **Tip 75**, Ch. 8 "Before the Project" (requirements are excavated, not collected — exactly the use Matt makes of it).
- **"Outrunning your headlights": CONFIRMED** — Ch. 4 "Pragmatic Paranoia," **Topic 27 "Don't Outrun Your Headlights"**; the on-stage tagline *"the rate of feedback is your speed limit"* is the topic's own principle, not Matt's paraphrase.

## Brooks — *The Design of Design* (2010)

- **Design concept: CONFIRMED** — Brooks describes architect and client repeatedly referring to a "**shared invisible entity**" that is not the drawings; his term for guarding it is **conceptual integrity** (the through-line from *Mythical Man-Month*). Matt's "not an asset… the invisible theory of what you're building" is a faithful rendering.
- **Design tree: CONFIRMED, WITH A NUANCE MATT OMITS** — the tree-structured design space (decision → narrowed space → next decision) is in Ch. 2, "How Engineers Think of Design — The Rational Model"… **which Brooks presents in order to critique it as unrealistic** (real designers iterate; they don't walk a predetermined tree). Grill-me's "walk down each branch of the design tree" borrows the *model* Brooks was arguing against as a description of practice — defensible as a deliberate procedure for an *interview*, but citing Brooks as endorsing tree-walking would over-read him. Notably the current skill text says "decision tree" and drops the Brooks name ([[design-concept-and-grill-me]]).
- **Brooks ↔ Naur: UNVERIFIABLE lineage** — no evidence found that Brooks cites Naur's "Programming as Theory Building" (1985); treat the design-concept/theory resemblance as **independent convergence** ([[video-to-corpus-crosswalk]]).

## Evans — *Domain-Driven Design* (2003)

- **Ubiquitous language: CONFIRMED** as the source concept (conversations among developers, expressions in code, and conversations with domain experts all derived from one domain model). Deep treatment: [[../pocock-real-feature-build/ubiquitous-language-for-llms]].

## Beck — *Extreme Programming Explained* (2nd ed., 2004, with Cynthia Andres)

- **"Invest in the design of the system every day": ATTRIBUTION CONFIRMED, QUOTE SIMPLIFIED** — the Incremental Design practice's actual line is *"We invest in the design **every day**, but we have the additional constraint that **we need to keep our APIs stable**."* Matt's stage version keeps the directive and **drops the API-stability constraint** — which happens to be load-bearing for his own thesis (stable interfaces + malleable implementations is exactly his gray-box model). Quote him as paraphrasing Beck, not quoting.

## Key Takeaways

- **Every book citation in the talk is real** — zero fabricated quotes or false attributions; the Ousterhout definition and the PragProg taglines are verbatim-grade.
- Two precision downgrades to carry: the **Beck quote is simplified** (omits API stability) and the **Brooks design tree is quoted from the model Brooks critiques**.
- The talk is a competent reading list: Ousterhout Ch. 2+4, PragProg Topics 3+27 + Tip 75, Brooks Ch. 2, Evans on ubiquitous language, Beck on incremental design — a fundamentals-for-agents syllabus in five entries.
- Cross-links: [[claims-scorecard]] (verdict table) · [[../pocock-agentic-workflow/the-originals]] (Ousterhout/Sutton/ZPD from the podcast pass) · [[../system-thinking-ai-coding/naur-programming-as-theory-building]] (the Naur side of the convergence).
