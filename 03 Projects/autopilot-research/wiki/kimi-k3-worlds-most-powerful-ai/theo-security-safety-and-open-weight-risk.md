# Theo on security, safety & open-weight risk (N=3)

> The N=1 topic covered *export-control confusion* ([[cyber-and-export-control]]). Theo adds the **safety-transparency and dual-use** angle from a practitioner who deliberately probed it — the most substantive security discussion of the three sources.

## The transparency gap (CONFIRMED / CORRECT-BUT-INCOMPLETE)

- **No system/safety card at launch** [34:21]. Theo: the word **"security" appears only inside some demos** on the launch page, **"safety" does not appear at all**, and there's **no system card** — the technical report is promised "in the future." *"We don't even know how they thought about safety and security during training."*
- **Verified nuance:** the platform's system prompt does carry *minimal* safety language, so "zero safety anywhere" is slightly too strong — but the substantive point holds: **no formal system/safety card was published at launch.** Verdict **CORRECT-BUT-INCOMPLETE** (transparency gap real; not literally zero).
- This is a genuine regression from the frontier norm: Anthropic/OpenAI ship model/system cards. An open-weight frontier model with **no safety documentation** is a real gap — and the one place where releasing the weights makes the gap *matter more*, not less.

## The dual-use argument (OPINION — well-founded)

Theo's central security thesis, catalogued as **OPINION** (his extrapolation, not an established fact) but flagged **well-founded**:

- He ran an **offensive-leaning security audit on his own "Lakebed" product** — a task he says **Fable and Soul frequently *refuse*** — and **K3 did it** (discovery agents → ~25 verification agents → synthesis → usable hardening advice) [32:58–33:54].
- His point cuts both ways: *"This is good on my end… but it's going to be really bad when attackers start using it for similar things."* Anthropic/OpenAI invest heavily in **blocking offensive use**; an **open-weight** model of this capability **removes that guardrail for everyone** the moment the weights drop (July 27).
- He notes the asymmetry: **Moonshot *brags* about K3's kernel-optimization / ML-engineering ability**, a capability Anthropic deliberately **restricts** on Fable/Mythos (this specific Anthropic-policy claim is **UNVERIFIABLE** — no public primary source — so it's held as Theo's assertion, not fact).

## Why this is decision-relevant, not just commentary

- **It reframes "open weights" from a pure good to a dual-use event.** The corpus's [[open-weights-reality]] treats the July-27 release as an *availability/hardware* story; Theo adds the **safety-release** story: capability + no safety card + weights = offensive tooling in anyone's hands.
- **It hardens the hireui posture from a second direction.** Beyond residency and fabrication, a vendor that ships a frontier model with **no system card and visibly relaxed offensive-use refusals** is exactly the *unauditable, un-governed* profile the RATIFIED candidate-LLM legibility ADR rules out. See [[hireui-translation]].
- **It is consistent across sources.** N=1 got the *geopolitics* wrong (export controls were on the US models, not K3), but the underlying instinct — "a capable no-restrictions open model has security implications" — is the one thing N=1's framing gestured at that N=3 substantiates properly.

## What is *not* claimed

Per fail-loud discipline: this article does **not** assert that K3 is uniquely dangerous, that Moonshot acted in bad faith, or that the Anthropic kernel-opt-restriction claim is proven. It records a **documented transparency gap** (no launch system card) plus a **well-founded practitioner concern** (dual-use, reduced offensive-refusals) — both correctly tagged by confidence.

## Key Takeaways

- **Documented gap:** no system/safety card at launch (minimal system-prompt safety language aside) — a real regression from the frontier norm.
- **Dual-use, well-founded (OPINION):** K3 performed an offensive-leaning audit Fable/Soul refuse; open weights + this capability + no safety doc = offensive tooling broadly available from July 27.
- **The "Anthropic hides kernel-opt" claim is UNVERIFIABLE** — held as Theo's assertion, not fact.
- **Second independent reason for hireui AVOID:** unauditable, un-governed vendor profile — not just residency/fabrication.
