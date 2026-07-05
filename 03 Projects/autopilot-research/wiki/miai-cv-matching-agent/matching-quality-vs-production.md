# Matching Quality: This Demo vs Production CV↔Job Systems

## Source

Dive `matching-architecture` + refute-first verify (wf_dd724957-cac); code cross-checked against `hr_agent_tools.py` / `hr_agent.py` / `hr_agent_format.py`.

## Where the demo sits (CONFIRMED)

- Pattern: **single-stage LLM-scoring-on-top-5** — bi-encoder vector search (text-embedding-3-small, k=5) → gpt-4o-mini reads the 5 JDs and *invents* a 0–100 score. The author's own words: the LLM "chém gió ra độ phù hợp" (bullshits out the fit score).
- Production systems use **two-stage retrieval + reranking**: LinkedIn (published) runs exhaustive k-NN retrieval + a 0.6B cross-encoder distilled 7B→1.7B→0.6B; ConFit v3 (arXiv 2605.09760) runs retrieval + LLM listwise reranking trained on preference data.

## Documented failure modes of the demo's pattern (all CONFIRMED)

1. **No grounding**: Chroma similarity scores are never surfaced — the LLM gets zero numeric signal ([[code-audit]]).
2. **Position bias**: LLM listwise scoring shifts with document order (arXiv 2604.03642 — DebiasFirst); same pair can score differently by position in context.
3. **No calibration**: 85 ≠ 85% hire probability. No labeled (CV, JD, outcome) pairs, no Platt/isotonic scaling — thresholds like "70+ = recommend" are meaningless.
4. **Whole-JD embedding**: no chunking or skill extraction — can't distinguish required vs nice-to-have skills or seniority bands. Production uses skill taxonomies (ESCO ~11K skills, O*NET, Lightcast; arXiv 2601.09119, 2512.03195).
5. **Unrepresentative corpus**: 5 pages of Google-Careers-Vietnam ≈ ~100 JDs from one employer — fine for demo, useless for real VN market matching.

## Verified upgrade path (tiers)

- **Tier 1 — add a reranker**: cross-encoder/ms-marco-MiniLM-L6-v2 (~5ms CPU/doc), BGE reranker-base, Cohere Rerank v3 ($2/1M tokens), or Voyage `rerank-2.5` ([[claude-stack-port]]). ⚠️ The dive's "4 hours effort / +20-30% recall" figures are **NOT verified** — no literature supports the specific numbers; LinkedIn's cross-encoder took a full distillation pipeline.
- **Tier 2 — calibrate**: collect labeled pairs (recruiter decisions are hireui's natural gold data), fine-tune / isotonic-regress raw scores into probabilities (cf. arXiv 2403.16950, self-calibrated listwise reranking arXiv 2411.04602).
- **Tier 3 — structured skills**: extract skills against a taxonomy (ESCO/O*NET) for explainable gap analysis instead of LLM intuition.

## What the LLM layer is genuinely good for

- **Explanation, not ranking**: reasoning, strengths/gaps narrative, improvement tips — the demo's most defensible LLM use.
- Honest architecture: retrieval ranks (with real scores), reranker refines, LLM explains. Don't let the LLM invent the number.

## Key Takeaways

- "LLM reads top-k and scores 0–100" is a demo pattern, not a ranking system — position-biased, uncalibrated, ungrounded.
- The demo is pedagogically excellent AND ~"2/10 production-ready" by the dive's assessment — both true, and the author says as much.
- Recruiter-labeled outcomes are the scarce asset; a recruitment SaaS sits on exactly that data ([[claude-stack-port]]).
- Expose retrieval rank + LLM rationale to users; hide or calibrate any numeric score before showing it — scores create legal exposure in hiring contexts ([[recruitment-ai-regulatory-context]]).
- Cross-link: [[external|Storm Bear: ai-engineering]] (Chip Huyen Ch.3–4) is the eval-first discipline this upgrade path plugs into; [[external|Storm Bear: prompt-evaluation]] has the vault's harness.
