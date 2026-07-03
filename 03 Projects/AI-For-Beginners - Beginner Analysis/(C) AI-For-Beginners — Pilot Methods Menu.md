# (C) AI-For-Beginners — Pilot Methods Menu (v191)

> 24 methods, laddered by risk/effort. This is a **knowledge + pedagogy subject**: the value is (1) under-the-hood LLM intuition, (2) a ready-made responsible-AI-for-hiring playbook, (3) a stealable teaching format, (4) the franchise ladder to on-goal follow-ups. Nothing here installs into the agent stack.
> **Fence (applies throughout):** pin `3662ce1` · notebooks only in a scratch conda env (`environment.yml` → `ai4beg`) or GitHub Codespaces · treat L20's model-scale claims as errata (the verified "GPT-4 = 100T" error) · Vietnamese translation is machine-generated (co-op-translator) — verify before teaching from it · hireui work per its CONSTITUTION (I-2 `agent-*` branch · I-8 operator-installs · GitNexus-first) · metrics page-stated (§37.4).
> **Honest top-3: A2 → (B8 + D13) → E17**, with F20/F21 as the on-goal follow-through.

## A — Orient (zero install, ~1–3h total)

- **A1 · 30-min triage read.** README + curriculum table + L01 (history) + L24 (ethics). Decide which of the three tracks below you actually need. *Output: a 5-line note in this folder.*
- **A2 · Personal gap-map (the loop-engineering A3 move, applied to knowledge).** Score yourself against all 24 lessons: KNOW / FUZZY / BLANK. Expected result for this operator: symbolic-AI + CV mostly skippable, L13–20 + L22–24 the live gaps. *Output: a personal syllabus of only the FUZZY/BLANK rows — probably 6–8 lessons, not 24.*
- **A3 · The "what Claude is made of" spine.** Read L13→14→15→(16–17 skim)→18→20 in order — text representation → embeddings → language modeling → (RNN interlude) → transformers → LLMs/prompting. Pair each with its modern completion: L14 ↔ embedding APIs; L18 ↔ Karpathy Zero-to-Hero; L20 ↔ the AI-Engineering book thread (Ch 1–4) + the claude-api skill. ~4–6 h. *This is the cheapest structured path to the intuition your cost-optimization and prompt-eval threads keep assuming.*
- **A4 · Dated-content pre-mortem.** Read with the 2026 lens using the Deep Dive's 8-row errata table: keep the durable math (perceptron→backprop→attention), flag the stale (BERT-centric arc, 100T cell, no RLHF/tokens/context/RAG). *Output: margin notes; protects you and anyone you teach from 2022 fossils.*

## B — Map onto live vault threads (thinking work, no code)

- **B5 · Token/context intuition → `claude-api-cost-optimization` thread.** One page: how L14 embeddings + L18 attention explain WHY prompt caching, context engineering, and the headroom compressor work. Feeds the hireui build-it-right spec.
- **B6 · "1997 MAS vs 2026 orchestration" note (L23).** Map BDI→system-prompt+plan, KQML→natural-language A2A, emergence→top-down orchestrators, NetLogo-parallelism→subagent fan-outs. *Output: 1 page into the multi-agent-orchestration thread — the durable vocabulary is genuinely clarifying.*
- **B7 · RL framing → the loop-engineering pilot (L22).** Reward function ≈ loop-verifier verdicts; exploration/exploitation ≈ when a loop may try a new fix vs repeat a proven one; reward discounting ≈ why L1→L2 graduation needs a WEEK of clean runs, not one. *Output: a paragraph appended to LOOP.md rationale.*
- **B8 · The 6 RAI principles × hireui (L24).** The lesson's own flagship example is hiring bias. Extract Fairness / Reliability / Privacy / Inclusiveness / Transparency / Accountability into recruitment-specific questions ("which features proxy protected attributes in candidate scoring?", "who is accountable for an AI-assisted reject?"). *Output: the checklist that seeds D13.*

## C — Hands-on (scratch env, low risk, 1 evening each)

- **C9 · Build-it-to-grok-it: run ONE notebook end-to-end.** Best pick: L03 Perceptron or L04 own-framework (the from-scratch layer — the v74 LLMs-from-scratch move at 1/20th the effort). Codespaces = zero local install.
- **C10 · Embeddings lab with recruitment-shaped toys (L14).** Word2Vec/GloVe cosine similarity over toy CV-vs-job-description strings. *The intuition seed for any future hireui semantic-matching feature — and for why embedding-based candidate search beats keyword search.*
- **C11 · GPT-2 locally, then Claude (L20).** Run `GPT-PyTorch.ipynb` (HuggingFace GPT-2), then the same prompts through Claude via the claude-api skill. Feeling the 2019→2026 gap firsthand is the fastest cure for both LLM-mystique and LLM-dismissal.
- **C12 · CartPole policy gradient (L22, optional).** Reward loops hands-on; pairs with B7.

## D — hireui / Goal-#2 artifacts (the real deployment track)

- **D13 · Responsible-AI gate spec for hireui's future LLM features.** B8's checklist → a real spec doc: pre-launch fairness review, feature-proxy audit, human-in-the-loop rule for rejects, transparency copy for candidates, incident accountability. Composes with the `claude-api-cost-optimization-spec` (hireui has NO LLM yet — this is build-it-right, not retrofit) and the v187 **AI Hiring Committee** design. On an `agent-*` branch, per CONSTITUTION. **The single most direct Goal-#2 artifact this subject offers.**
- **D14 · Fairlearn spike on a toy screening model.** Scratch repo: train a deliberately-biased toy candidate-screening classifier, run the Fairlearn dashboard (L24's RAI Toolbox), show the disparity metrics. *A 2-hour measurable demo that makes D13's checklist concrete for the team.*
- **D15 · Semantic candidate-matching spike (spec-first).** L14's intuition + modern embedding APIs → a 1-page design for CV↔job matching in hireui (cost model via the cost-optimization spec; NOT built yet — spec-first per the hireui-no-LLM memory).

## E — Teach it (the Scrum-coach leverage)

- **E16 · Steal the lesson template.** Pre-lecture quiz → content → 🚀 Challenge → post-lecture quiz → Review & Self Study → lab (hand-verified from L03). Adopt for vault teaching docs / hireui onboarding modules. It is the LLM-wiki pattern's pedagogical cousin: force retrieval before and after every unit.
- **E17 · Team AI-literacy workshop (2-week sprint-embedded track).** 4 sessions from the curriculum: ① L01 history/what-AI-is → ② L14 embeddings (with C10 as the live demo) → ③ L18+L20 transformers/LLMs (with the errata!) → ④ L24 RAI-for-hiring (with D14's demo). Pre/post quizzes from the quiz app. *A real deliverable for a Scrum coach whose team ships a recruitment product into the AI era.*
- **E18 · Quiz-first discipline.** Port the pre/post-quiz mechanic into team onboarding or vault skills; optionally redeploy `etc/quiz-app` (Vue 2) with your own per-lesson JSON.
- **E19 · VN-locale asset.** `translations/vi` as team-shareable material for Vietnamese colleagues — with the machine-translation caveat stated up front (spot-check 1 lesson against the English before circulating).

## F — The franchise ladder + vault-meta (the on-goal follow-through)

- **F20 · Queue `microsoft/generative-ai-for-beginners` (113k★, 21 lessons; L17 = agents).** The LLM-era layer this course lacks — the natural NEXT wiki subject on this track.
- **F21 · Queue an `ai-agents-for-beginners` REVISIT (corpus v6).** Apr-2026 fork snapshot = 10+4 lessons; now 15 lessons / 68.4k★ (page-stated) + protocols/security lessons. The corpus-recursive-revisit precedent (v78 ECC, v185 agency-agents) fits exactly, and it would close the franchise loop v6↔v191.
- **F22 · `mcp-for-beginners` targeted read (16.7k★, 12 modules).** Only the modules matching the vault's live MCP surface (server security, tool design) — not a full wiki.
- **F23 · `Azure/co-op-translator` as a tool candidate.** The 50-language automated-docs mechanism, applied to hireui's own docs? (Fence: Azure OpenAI cost + translation-quality gate. Investigate-only.)
- **F24 · Vault-meta cross-link pass.** Link this wiki into the education-cluster pages (v6 / ~v26 / v74 / v77 / v170) + the AI-Engineering thread; file the "pre-LLM curriculum now agent-maintained (root AGENTS.md + Copilot-authored HEAD)" observation + the T3 sub-typology data-point for the ~v192 audit.

---

**Sequencing suggestion (2 weeks, ~1–2 h/day):** Week 1 = A2 → A3 → B8 → C10. Week 2 = D13 (+D14 if the team demo lands) → E17 planning → F20 queued. Everything else is optional depth.
