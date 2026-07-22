# Karpathy — "Software Is Changing (Again)": 3.0, LLM-as-OS, the Autonomy Slider

> **Source:** Andrej Karpathy, "Software Is Changing (Again)," Y Combinator **AI Startup School, June 17 2025** (`LCEmiRjPEtQ`). *Note: ~13 months older than the rest of the bundle — the canonical foundation the newer talks build on. Some specifics are mid-2025-vintage.*

## Software 1.0 / 2.0 / 3.0

- **1.0** = code you write for the computer.
- **2.0** = neural-net **weights** (you tune datasets + run an optimizer; HuggingFace ≈ "GitHub of Software 2.0").
- **3.0** = **LLMs programmed in English** — prompts *are* programs. "Remarkably, we're now programming computers in English."
- Be **fluent in all three** and transition fluidly (some functionality belongs in 1.0, some 2.0, some 3.0). At Tesla, the 2.0 stack "ate through" the C++ autopilot stack over time.

## LLMs as utility / fab / operating system

- **Utility:** capex to train ≈ building a grid; opex to serve ≈ metered per-token API; OpenRouter ≈ a transfer switch between providers; when models go down it's an **"intelligence brownout."**
- **Fab:** huge capex, deep R&D tech-trees centralizing in the labs.
- **Operating system (best analogy):** LLM ≈ CPU, context window ≈ memory; closed providers (Windows/macOS) vs open (Llama ≈ Linux); apps like Cursor run on GPT/Claude/Gemini via a dropdown. We're in the **1960s time-sharing era** — compute is expensive, centralized in the cloud, thin clients; the personal-computing revolution hasn't happened (Mac minis are a hint). Talking to an LLM in raw text ≈ using a **terminal**.
- **Diffusion is flipped:** normally new tech goes government/corp → consumer; LLMs went **consumer-first** (help me boil an egg, not ballistics).

## LLM psychology — "people spirits"

Stochastic simulations of people (autoregressive transformers). Superpowers: encyclopedic memory (Rain Man). Deficits to design around:
- **Hallucination**; poor self-knowledge.
- **Jagged intelligence** — superhuman in places, then insists "9.11 > 9.9" or "two R's in strawberry."
- **Anterograde amnesia** — context window ≈ working memory that wipes (Memento / 50 First Dates); they don't consolidate knowledge like a new hire.
- **Gullibility / prompt-injection** risk.

## Partial-autonomy apps + the autonomy slider

Cursor is the model example: a traditional interface **plus** LLM integration. Shared properties of good LLM apps:
1. LLMs do the **context management**.
2. They **orchestrate multiple model calls** (embeddings, chat, diff-apply).
3. **App-specific GUI** to audit fallible output fast — a diff in red/green, ⌘Y/⌘N to accept/reject. ("A GUI utilizes the computer-vision GPU in your head; reading text is effortful, looking is fun.")
4. An **autonomy slider** (tab → ⌘K → ⌘L → ⌘I). *You* choose how much autonomy to grant per task. Perplexity has the same shape (search / research / deep-research).

## The generation-verification loop

Humans **verify**, AI **generates** — it's in our interest to make the loop spin fast, two ways:
1. **Speed up verification** (GUIs, visual diffs).
2. **Keep the AI on a leash** — small, concrete, incremental chunks. "It's not useful to get a 10,000-line diff to my repo — I'm still the bottleneck." Concrete prompts raise the odds verification passes. (Osmani's human-side echo: the *orchestration tax* — see [[engineer-of-the-future/three-failure-modes]].)

## "Decade of agents," Iron Man suits, build-for-agents

- **Decade, not year, of agents:** Karpathy rode a flawless self-driving demo in **2013**; ~12 years later autonomy still needs humans in the loop. "This is software. Let's be serious. We need humans in the loop."
- **Iron Man suit** = augmentation *and* agent. Build **suits (partial autonomy)**, not **robots (full autonomy)**; slide autonomy left→right over the decade.
- **Everyone's a programmer** (English). **Vibe coding** — Karpathy coined it (Feb 2 2025 tweet → meme → Wikipedia page → Collins 2025 Word of the Year). His **MenuGen** (at **menugen.app**) was easy to vibe-code; making it "real" (auth, payments, domain, deploy) was the slow part — "all this DevOps stuff was not code."
- **Build for agents** — agents are a new consumer of digital info: `llms.txt` (≈ robots.txt); docs in **Markdown** (Vercel, Stripe early movers, via content negotiation); **MCP** (Anthropic); **GitIngest** (github→gitingest) and **DeepWiki** (Cognition/Devin). "Meet the LLM halfway."

## Key Takeaways

- **Software 1.0 (code) / 2.0 (weights) / 3.0 (English prompts)** — be fluent in all three.
- LLMs are best understood as **new operating systems in a 1960s time-sharing era**; they're "people spirits" with jagged intelligence + amnesia to design around.
- Build **partial-autonomy apps** with an **autonomy slider** and a **fast generation-verification loop**; **keep the AI on a leash** (small diffs, concrete prompts).
- It's the **decade of agents**, not the year — humans stay in the loop; build **Iron Man suits, not robots.**
- **Build for agents**: llms.txt, Markdown docs, MCP, GitIngest/DeepWiki.

## See also

- [[engineer-of-the-future/inner-loop-outer-loop]] — "keep on a leash" ≈ humans own the outer loop
- [[engineer-of-the-future/convergent-thesis]] — how this grounds the whole bundle
- [[harness-engineering/_index]] · [[workflow-ai-coding/_index]] · [[adaptive-engineering-beyond-harness/_index]]
