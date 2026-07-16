# Pillar 3 — ~70% is normal engineering

## Source
Quân IT, [`RcF6ofU2nLs`](https://www.youtube.com/watch?v=RcF6ofU2nLs) [09:34–15:44]. **The strongest pillar in the talk.**

## What he says

Friends who switched into AI-engineer roles told him: only ~**30%** of the new skillset is AI-specific; the other ~**70%** is the same engineering work you already do. Concretely:

- **System design** [10:02–11:31] — take the company's requirements and design a system with the LLM ("the brain") in the middle. How do you process **PDF / Excel / SQL / text** data? **Caching** — if a user re-asks "2016 revenue," serve it from cache to save tokens. What can run **async / in parallel** vs what must be **sequential**? All ordinary system-design knowledge.
- **SQL / databases** [11:31] — write the queries that pull exactly the data the model needs.
- **Reading (often incomplete) documentation** [11:59–12:55] — if you're already an engineer, moving to AI is "just learning a new stack." His own "Claude" integration video was conceptually simple: read the docs, configure the plan/limits, wire it in. And when the docs are **incomplete** (beta features — "it was too new, the docs weren't finished"), the skill is figuring it out yourself.
- **Domain / business knowledge** [12:55–14:47] — *the load-bearing insight.* His hotel/restaurant IT background: deploying a system like **Oracle OPERA** means hundreds/thousands of config parameters (occupancy thresholds like 0.5 vs 0.8, etc.), and the IT person who understands operations configures it better than the operators. Why it matters for AI: an AI system is **Input → Process → Output**, and the model is **nondeterministic** — same question, differently-worded answers, but the *content* must be correct. **Domain knowledge is what lets you verify the output is right.**
- **Security & permissions** [14:47–15:44] — guardrails so a chatbot can't be prompt-injected into leaking company secrets (revenue, the director's phone number, customer PII). You need basics of **security, users, roles, permissions, group permissions**. His example: on **GCP**, create a user, create a "Log Viewer" role, assign it → they can only view logs, nothing else. He references a real-world pattern of chatbots being prompt-injected to leak discount codes (see the UNVERIFIABLE "Dodas" note in [[quanit-becoming-ai-engineer-2026/caveats-and-corrections|caveats]]). *"This is pure technical work — nothing to do with AI."*

## Verified facts behind the pillar

- **C7 — CONFIRMED.** Oracle Hospitality **OPERA** is a real, dominant, highly-configurable hotel PMS (OPERA 5 + OPERA Cloud; hundreds of integrations, thousands of REST APIs). His config-heaviness claim is accurate.
- **GCP IAM least-privilege** (part of C8) — the "Logs Viewer" role (`roles/logging.viewer`) and the create-user → create-role → assign-role pattern are real and correctly described.
- **The chatbot-coupon-leak phenomenon is real** (documented: Chevrolet's $1-Tahoe chatbot, an 80%-discount prompt-injection case), even though the specific brand he named ("Dodas") is **UNVERIFIABLE**.

## The caveat: correct allocation, under-stated stakes

The critical appraisal agrees the **70/30 split is right** but warns Quân under-sells the escalation:
- Those "normal" fundamentals are now **harder**, not just present. Classical software fails at **test time**; AI fails at **user-inference time**. Observability, safety gates, and rollback are categorically different problems. This is exactly the [[pocock-software-fundamentals/_index]] refinement — *fundamentals matter MORE because they're now the bottleneck.*
- A cache bug hits one user; a hallucinating model hits a whole cohort. Same disciplines, **orders-of-magnitude higher stakes.**
- Attribution: the 70/30 figure is **Quân's friends' observation**, not an industry-measured constant — treat it as a useful heuristic, not a law.

## Key Takeaways

- **This is the pillar to trust most.** "The scarce skills are the ordinary engineering ones" is correct and evergreen.
- **Domain knowledge = the verifier for nondeterministic output** — the single most transferable idea in the talk, and the direct bridge to [[prompt-evaluation/_index]] and the [[quanit-becoming-ai-engineer-2026/hireui-pilot|hireui pilot]] (recruiters as the domain experts who label matches).
- **Security is not optional and not AI-specific** — permissions + guardrails against prompt-injection; connect to [[api-security-7-techniques/_index]].
- Take the **70/30 as a heuristic**, and add Pocock's escalation: those fundamentals are now *harder*, because failure moved to inference time.
