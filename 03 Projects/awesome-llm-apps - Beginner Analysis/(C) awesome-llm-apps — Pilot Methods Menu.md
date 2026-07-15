# (C) awesome-llm-apps — Pilot Methods Menu (LLM Wiki v201)

**Why this is a strong pilot:** it's a free, Apache-2.0, ~129-app learn-by-example + build-from-template gallery dead-center on Goal #1 (Claude + autonomous agents for software dev), directly usable for hireui (Goal #2) — several apps *are* recruitment/RAG/MCP patterns. Honest caveat: **it skews OpenAI/Gemini** (Claude is a supported option, often not the default) → most pilots involve *reading the pattern and re-implementing on Claude*, not running as-is.

⭐ **One-thing path: A1 (browse RAG + MCP + Multi-agent-Teams) → C11 (clone ONE app into a scratch venv, BYO key, run it) → D16 (map its pattern to a hireui candidate-search / Match-Explain feature on an `agent-*` branch).**

**Fence (applies to every hands-on method):** clone only from the author's URL · scratch venv per app + `pip freeze` a lockfile · **BYO keys in `.env` + `os.getenv`, never in a shared Streamlit UI** · `npm-security-check` before any `npx skills add` · Apache-2.0 = safe to borrow/fork · hireui work is **DESIGN-only per its CONSTITUTION** (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first; hireui has no LLM spend yet → build-it-right, don't retrofit) · pin a commit (0 releases).

---

## A — Read & learn (zero install, zero risk)
1. **⭐ Browse the three most goal-relevant categories** — 📀 RAG (~20 apps), ♾️ MCP AI Agents (~5), 🤝 Multi-agent Teams (~13) — as a pattern catalog for Goal #1.
2. **Read the two crash courses** — Google ADK + OpenAI Agents SDK — as fast onramps to two agent frameworks the vault doesn't yet use.
3. **Map the 15 categories against your own gaps** — which agent patterns (voice, memory, always-on, generative-UI) you've never built; make a personal learn-list.
4. **Read the Advisor-Orchestrator-Worker skill's design** (stateless workers + expensive advisor at decision points + verification gates to stop API-cost runaway) — a maker/checker + cost-guardrail pattern that composes with your loop-verifier + the career-ops v200 subagent cost-guardrail.

## B — Borrow patterns into hireui/the vault (zero install, high ROI)
5. **⭐ Steal the RAG architectures** (Corrective RAG, Hybrid Search, RAG-with-DB-Routing, Knowledge-Graph-RAG-with-Citations) into a hireui **candidate-search / résumé-Q&A** feature spec — pick the pattern, re-implement on Claude.
6. **Steal a Multi-agent-Team topology** (the `AI Recruitment` + `AI Legal Agent Team` shapes) as the blueprint for the hireui recruitment-agent (composes with the ai-berkshire v187 "AI Hiring Committee" design).
7. **Steal the "Chat with X" pattern** (Chat-with-PDF / Chat-with-GitHub) → "Chat with a candidate's CV / portfolio" for hireui.
8. **Steal the LLM-Apps-with-Memory pattern** (Mem0 + Qdrant) as a reference for a hireui recruiter-memory / candidate-context layer (weigh against agentmemory v66 / claude-mem v103 — pick one).
9. **Port the Advisor-Orchestrator-Worker verification-gate + cost-guardrail** into the vault's own multi-agent workflows.

## C — Hands-on scratch trial (low risk, behind the fence)
10. **`install-snapshot` then clone into a scratch dir** — `git clone … /tmp/awesome-llm-trial`; never into the vault or hireui.
11. **⭐ Clone ONE app into a scratch venv, BYO key, run it** — a RAG app (`rag_chain`) or an MCP app (`multi_mcp_agent_router`, which uses Claude primary) — prove the loop end-to-end.
12. **Convert a Streamlit-key-in-UI app to `.env` + `os.getenv`** before running (kill the key-leak footgun) — do this every time.
13. **Run the `multi_mcp_agent_router`** (Claude-primary MCP router → 4 specialist agents) — the cleanest Claude-native app in the repo + a working MCP-router reference.
14. **Swap one OpenAI-default app to Claude** — replace `ChatOpenAI` → `ChatAnthropic`; a 30-min exercise that both trials the app and produces a Claude-native fork you keep.

## D — hireui / Goal-#2 (DESIGN-only, behind the CONSTITUTION fence)
15. **Inventory the hireui-relevant apps** — AI Recruitment, AI Legal Agent Team, RAG-with-Citations, Chat-with-PDF — as a design menu for hireui's first LLM feature.
16. **⭐ Map the RAG-with-Citations + "Chat with X" pattern → a hireui candidate-search / Match-Explain feature** on an `agent-*` branch (composes with career-ops v200 D16 scoring-rubric + meetily v196 vendor-seam) = a real Goal-#2 design artifact.
17. **Prototype the smallest read-only piece** — a "explain why this candidate matches" prompt over one real (synthetic) candidate, Claude structured-output, no vector DB v1 (the miai-cv-matching thread).
18. **Reuse the "AI Recruitment" multi-agent topology** as the skeleton for a hireui screening-committee (forced verdict + never-auto-reject invariant, per career-ops v200 + ai-berkshire v187).
19. **Borrow the fine-tuning apps only as a "don't" reference** — hireui should not fine-tune; the value is seeing what the alternatives (RAG + prompting) buy you.

## E — Agent Skills (`npx skills add`, behind an extra fence)
20. **`npm-security-check` then try `Project Graveyard`** on a throwaway repo (analyzes abandoned side-projects via git history) — the lowest-stakes of the 3 skills.
21. **Study (don't necessarily install) the Advisor-Orchestrator-Worker skill** — the cost-guardrail + verification-gate design is the transferable part; compose with agent-skills v184.
22. **Treat the `npx skills add` registry as a third-party trust boundary** — inspect the skill's `SKILL.md` + code before installing; the claimed "security + eval CI gate" is unverified.

## F — Vault-meta
23. **File the "runnable-app-gallery" as a Pattern #68 code-carrying form-factor sub-variant** + record the §C-standalone MINT-alternative for the badly-overdue ~v192 audit.
24. **Note the aggregator-includes-corpus-subjects data-point** (headroom v144 + browser-use v41 demonstrated here; the v50 Pattern #57 57b shape) for the audit's #57 tally.

---
**Ladder:** A1 → A4 (learn) → B5 + B6 (borrow the RAG + recruitment-team patterns, zero install) → C11 + C14 (clone one app + Claude-swap it) → **D16 (hireui candidate-search/Match-Explain design on an `agent-*` branch = the Goal-#2 artifact)** → E20 (one low-stakes skill) → F23/F24 (vault-meta). The PILOT lever (career-ops v200 D16 / meetily v196 vendor-seam / page-agent v199 recruiter-copilot) gains another concrete Goal-#2 design input here.
