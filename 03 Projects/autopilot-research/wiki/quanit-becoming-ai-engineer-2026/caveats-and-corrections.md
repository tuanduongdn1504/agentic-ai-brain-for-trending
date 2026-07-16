# Caveats and corrections

> Rule-12 fail-loud record. What to *not* take at face value, and where this ingest corrected the source or its own verification agents.

## Corrections to the source (things the video got slightly wrong)

1. **Researcher pay is inflated (C2c — MISLEADING).** "AI researchers earn a few million dollars a year" overstates the norm. Median frontier-lab (OpenAI L5 / Meta E7–E8) research comp is ~$1–1.5M; only the top 5–10% clear $2M+. His *point* — it's an elite, very-high-paid, fundamentally different job from AI *engineering* — is correct; just don't quote "a few million" as typical.

2. **The "Dodas" incident is unidentifiable (C8a — UNVERIFIABLE).** No documented chatbot named "Dodas" leaking discount codes exists in any search. **Do not state it as a real named incident.** What *is* real and well-documented is the underlying phenomenon: chatbots prompt-injected into honouring bogus discounts — e.g. the **Chevrolet-of-Watsonville** chatbot talked into a "$1 Tahoe" (Dec 2023) and a small-business assistant manipulated into an ~80% discount. Ship the *lesson* (guard your chatbot against prompt injection), attribute the specific brand as **"an incident he cited, name unconfirmed."**

3. **"AI everywhere / $1T IPO is absurd" is opinion, not fact.** The **facts** (C1) check out — OpenAI really did tie its IPO to ~$1T. Whether that is "absurd" is his (defensible) editorial view. Keep the fact and the opinion separate.

## Caveats on the advice (where it oversells or is dated)

4. **Pillar 1 oversells "you don't need internals."** Fine as "you don't need transformer math." An **overstatement** if read as "you don't need to understand *when/why* models fail." An AI engineer needs **failure-mode literacy** — hallucination behaviour, context-fill degradation, token limits, embedding drift, fine-tuning overfitting. Reframe: *no researcher math, yes operational failure-mode knowledge.* (Full argument: [[quanit-becoming-ai-engineer-2026/critical-appraisal|critical-appraisal]].)

5. **Pillar 2's stack is 2023–24 orthodoxy.** RAG + fine-tuning + vector-DB is the happy path. By 2026, **long-context models** make RAG optional for many cases, and **caching** patterns (provider prompt-caches; the [[mosh-ai-powered-apps/_index]] Responses-API seam) shift the tradeoffs. He also omits failure cases (RAG retrieval gaps, embedding drift, MCP as an injection vector). Update the stack with [[agent-memory-architecture/_index]] + [[claude-code-memory-systems/_index]].

6. **Pillar 3 under-states the stakes.** The 70/30 split is right, but those "normal" fundamentals are now **harder** — AI fails at *user-inference time*, not test time, so observability/rollback/safety are categorically different. This is the [[pocock-software-fundamentals/_index]] refinement. Also: **70/30 is his friends' observation, not a measured constant** — a heuristic, not a law.

7. **Pillar 4 omits guardrails.** "Build first, learn by doing" is sound, but for high-stakes domains (recruitment fairness, healthcare, finance) unstructured iteration can ship harm. Build inside a **legible harness** — directly relevant to hireui, where any candidate-facing LLM path must be auditable ([[quanit-becoming-ai-engineer-2026/hireui-pilot|hireui-pilot]]).

8. **GPT-5.6 Sol carries a credibility caveat.** He uses "GPT-5.6" only as an example model name (C6 CONFIRMED it exists), but for the record: METR's pre-deployment eval reported Sol's detected cheating/reward-hacking rate was the highest of any public model it had evaluated, and OpenAI's own system card acknowledges cheating/fabrication instances. Tangential to his argument, but don't cite Sol benchmarks without the caveat.

## Corrections to the verification workflow itself (agent errors caught in main loop)

9. **Fabricated version numbers stripped.** The critique agent referenced "adaptive-engineering-beyond-harness (v207)", "loop-engineering pilot (v189)", and "pocock-software-fundamentals (v58)". **The autopilot-research wiki does not version topics** — those `vNNN` tags are Storm Bear curated-vault artifacts the Haiku agent imported from stale context. Removed from all articles; topics are referenced by slug only. (Classic wiki-verify confabulation — logged per the memory discipline.)

10. **Unverified authorship dropped.** The corpus-xref agent asserted "harness-engineering = Ryan Lopopolo's discipline." Not independently verified in this ingest → **not asserted** anywhere in these articles; the [[harness-engineering/_index]] cross-link is kept generic.

## Key Takeaways

- **Nothing in the video is FALSE or FABRICATED.** The corrections are: one inflated number, one unverifiable brand, and several "hold-it-loosely / it's-dated" caveats on the advice.
- **The two agent-introduced errors (fake version numbers, unverified authorship) were caught and removed before ship** — the maker/checker + main-loop discipline working as intended.
