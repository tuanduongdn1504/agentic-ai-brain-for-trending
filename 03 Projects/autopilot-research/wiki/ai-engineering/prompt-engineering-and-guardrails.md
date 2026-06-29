# Prompt Engineering, Prompt Attacks & Guardrails (Ch. 5)

## Source

Video sections "Prompt Engineering" → "Guardrails System Design" + Huyen *AI Engineering* Ch.5 (Prompt Engineering). See [[overview]], [[source-provenance]].

## Prompt engineering — the first (and cheapest) lever

- **The fastest way to change model behavior without changing the model.** Why it matters: fast to test/iterate, low cost vs fine-tuning, controls format/tone/instructions, "often the best first step before bigger changes." It's cheap, flexible, practical, and needs no retraining.
- Huyen frames prompting as **communication**: *"Anyone can communicate, but not everyone can communicate well."* Clear instructions + examples + relevant context — same as briefing a human.
- **Tip the video stresses: version your prompts.** Keep copies of prior prompts so you can revert/compare. (Ch.5: "Organize and Version Prompts".)
- **Order of operations:** *start with prompts → then RAG → then agents or fine-tuning if needed.* (Reinforces the [[overview]] progression.)

## Anatomy of a good prompt (the video's 5 parts)

1. **Role / system** — set behavior + rules ("act as an experienced data scientist").
2. **Task** — state *exactly* what to do (be precise).
3. **Context** — provide the facts/background.
4. **Examples** — show the pattern you want (few-shot).
5. **Output format** — JSON? HTML? Markdown? Specify exactly.

> Example: *"You are an expert assistant. Summarize the report. Use the notes below. Return three bullets and one action item."* → **Clarity always beats cleverness.**

**Ch.5 best practices (fuller list):** write clear/explicit instructions · provide sufficient context · **break complex tasks into simpler subtasks** · **give the model time to think** ("Simple tricks like asking the model to slow down and think step by step can yield surprising improvements" — i.e. chain-of-thought) · iterate · evaluate prompt-engineering tools · organize + version prompts. Ch.5 also covers **in-context learning (zero-shot vs few-shot)**, the **system-prompt vs user-prompt** split, and **context length + context efficiency**.

## Prompt engineering as a *system* (production view)

Prompting in production is more than a text box. The runtime assembles a prompt from layers:

`User input (the query)` + `System prompt (the always-on role/purpose)` + `Retrieved context (from RAG — see [[rag]])` + `Few-shot examples (tested via evals)` → **`Prompt builder`** → **`Foundation model`** → **`Output parser / validator`** (e.g. enforce the JSON schema) → response.

> Production prompting needs **structure, testing, and output control** — not a hand-typed string.

## Prompt attacks & prompt injection (defensive prompt engineering)

**Untrusted input tries to override your intended system behavior.** Common attacks: "ignore previous instructions", "reveal the hidden/system prompt", **malicious instructions hidden in retrieved documents**, tricking the model into unsafe tool use. Ch.5 groups these as **jailbreaking, prompt injection, reverse prompt engineering (extracting proprietary prompts), and information extraction.**

> Huyen's caution: **"no defensive measures are foolproof."** Defense-in-depth, not a silver bullet.

**Defenses (video + Ch.5 "Defenses Against Prompt Attacks"):**
- Keep the **instruction hierarchy clear** (system > developer > user > retrieved content).
- **Treat all retrieved content as untrusted** (this is where injection most often enters — user input, files, web pages, retrieved docs).
- **Restrict tools** with allow-lists + least-privilege permissions (see [[agents-and-memory]]).
- **Check outputs before they reach the user.**

## Guardrails system design

Guardrails wrap the **entire** workflow — *before, during, and after* generation, not just at the output:

`User input → INPUT CHECK` → `Context retrieval → CONTEXT CHECK (is it usable/safe?)` → `TOOL PERMISSION LAYER (are we allowed to call this?)` → `Model` → `OUTPUT CHECK` → user (or **human review**).

The checks include: **policy filters, prompt-injection checks, schema validation**, and **escalation to a human reviewer or an LLM-as-judge when uncertain**.

> This is the same layered idea Huyen formalizes in the production architecture (Ch.10, Step 2 "Put in Guardrails") — see [[production-architecture-and-feedback]].

## Key Takeaways

- **Prompting is the first, cheapest behavior lever** — clear instructions + context + examples + explicit output format; clarity beats cleverness.
- **Version your prompts** and treat the production prompt as an assembled, tested, validated artifact (system + context + few-shot + parser).
- **Prompt injection is a real, unsolved security problem** — treat retrieved content as untrusted, keep an instruction hierarchy, restrict tools, and check outputs. No defense is foolproof.
- **Guardrails are end-to-end** (input + context + tool + output checks) with human/LLM-judge escalation when uncertain.

## Cross-links

- [[rag]] (retrieved context = injection surface) · [[agents-and-memory]] (tool allow-lists / least privilege) · [[production-architecture-and-feedback]] (guardrails as Ch.10 architecture step)
- [[../prompt-evaluation/_index]] (eval your prompts) · [[../claude-api-cost-optimization/_index]] (context efficiency = token cost) · [[../multi-agent-orchestration/_index]] (system-prompt + tool design at scale)
