# The original resource — Peter Naur, "Programming as Theory Building" (1985)

## Source

- **Primary essay:** Peter Naur, *"Programming as Theory Building"*, **Microprocessing and Microprogramming** vol. 15 (1985); reprinted in Naur, *Computing: A Human Activity* (ACM Press / Addison-Wesley, 1992).
- **Deep-dived in this pass** (secondary mirrors that reproduce the essay's body text + canonical quotes; the essay itself is offline/journal): riverandsoftware.com, catenary.wordpress.com, embeddedartistry.com, inventwithpython.com; author facts from en.wikipedia.org/wiki/Peter_Naur + amturing.acm.org.
- This is the intellectual anchor the video attributes at [3:14] (garbled auto-caption *"Peter Law … Programming Story Building"*). See [[overview]] and [[caveats-and-corrections]].

## Who Peter Naur actually was (correcting "Peter Law")

- **Peter Naur (1928–2016)** — Danish computer-science pioneer, *not* "Peter Law."
- Co-author of **Backus–Naur Form (BNF)**; editor of the **ALGOL 60 Report (1960)**; University of Copenhagen professor (1969–1998).
- **2005 ACM Turing Award** — the only Dane to win it. The 1985 essay came 25 years after ALGOL 60, as a reflection on what programming *really is*.

## The core argument

- Naur borrows **Gilbert Ryle's** sense of "theory": *the knowledge a person must have in order not only to do certain things intelligently but also to explain them, answer queries about them, and argue about them.* A theory is more than any set of rules/documentation you could write down.
- **The primary aim of programming is not to produce programs, but to have the programmers build a theory** of how the problem is solved by program execution. Quote:
  > "the proper, primary aim of programming is, not to produce programs, but to have the programmers build theories of the manner in which the problems at hand are solved by program execution."
- **Code and documentation are secondary, lossy artifacts.** The *theory* — why the program is the way it is, how it maps to the world — lives in the builders' heads and is not fully recoverable from the text.

## Three things a programmer *with the theory* can do (that docs alone cannot)

1. **Explain how the program relates to the world** it helps handle.
2. **Explain why each part of the program is what it is** (design intent, not just behavior).
3. **Respond constructively to any demand for modification** — judge which changes are safe, which violate the domain, which map to real constraints.

> A programmer possessing a theory "can explain how the solution relates to the affairs of the world … can explain why each part of the program is what it is … [and] is able to respond constructively to any demand for a modification."

## Program life, death, and revival (the sharpest idea)

- **Death:** *"The death of a program happens when the programmer team possessing its theory is dissolved."* A dead program can keep running and producing useful results — death only becomes *visible* when a modification demand can no longer be answered intelligently.
- **Execution ≠ life.** Source + docs surviving does not keep the program alive; the *theory-holding team* does.
- **Revival = rebuilding the theory** by a new team — not "reading the code harder." Naur's implication: the theory cannot be fully reconstructed from text, which is why reviving a legacy system is so expensive.

## Fidelity check — the video's paraphrases vs. Naur's actual text

| # | Video claim | Verdict | Note |
|---|---|---|---|
| a | "Code is not the program; the real program lives in the programmer's head; code is just the shadow." | **FAITHFUL** | Matches Naur: theory is primary/present-in-the-mind; text is secondary and insufficient. "Shadow" is a fair gloss of "insufficient / not fully conveyed." |
| b | "The whole program is completed in the programmer's brain *before* we touch the code." | **PARTIAL / overstated** | Naur says theory is *built through* the work of solving the problem — it emerges iteratively, not pre-composed waterfall-style. Faithful in spirit, wrong on timing. |
| c | Programmer = "conductor" (nhạc trưởng); AI plays instruments, never the conductor. | **STRETCH** | Naur never uses the conductor metaphor. It captures the essence (irreplaceable integrating judgment) but is an interpretive gloss. |
| d | Using AI to generate code without building the theory = "we stop building the theory." | **FAITHFUL (with nuance)** | Direct logical extension of Naur: if code appears while the programmer stays passive, theory-building has ceased. Naur predates AI (1985) so doesn't say it literally. |

## Why this matters for AI coding (the bridge the talk makes)

- If the *program is the theory*, then an AI that emits code but leaves **no theory in your head** hands you a program that is **born dead** — it runs, but no one can answer modification demands. That is the video's technical-debt and junior-crisis argument, restated in Naur's terms. See [[code-vs-architecture-and-tech-debt]] and [[junior-crisis-and-hiring-2026]].
- The [[four-practice-steps]] (draw-it, spec-it, chaos-delete, reverse-review) are all **theory-building rituals** — they force the theory back into the human even when the AI wrote the code.
- Corpus resonance: [[agent-memory-architecture]] (theory ≈ the context/understanding a system must retain), [[elicit-verifiable-agent-dsl]] ("the plan *is* the executable" — externalizing part of the theory as a checkable artifact), [[harness-engineering]] (harness encodes procedure, human holds the theory).

## Key Takeaways

- Naur's thesis: **programming is an epistemological act** — building a shared, internalized theory of a domain that code can only partially express.
- A program is **alive only while a team holds its theory**; it *dies* when they disperse, regardless of whether it still runs.
- The video conveys the **core insight faithfully**; only the "brain-before-code" timing and the "conductor" metaphor are looser than Naur's text.
- Practical upshot for the AI era: **optimize for theory retained in humans, not lines emitted by machines.**
