# AI Engineering Foundations (per Mosh)

## Source

Video PtETUYa3i2Q, chapters "Rise of AI Engineering" (7:48) → "What Can You Do With Language Models?" (16:12). Transcript read directly (lines ~184–440).

## AI engineer ≠ ML engineer

- **ML engineer:** builds and trains models — cleans data, tunes architectures, optimizes training pipelines. Math-heavy, research-focused.
- **AI engineer:** uses **pre-trained** models (especially LLMs) to build smarter applications. No model training required.
- **The database analogy (load-bearing):** you don't need to know MySQL internals to build on it — you need to query it, structure data, and ship a reliable product. Same with LLMs. (Verified consistent with Chip Huyen's definitions — see [[external|Storm Bear: ai-engineering]].)
- Skill list Mosh names for the role: LLMs, prompt engineering, RAG, vector databases, agents.

## The 6 real-world feature archetypes cited

| Example | Feature | hireui analog |
|---|---|---|
| Amazon | AI-generated review highlights on product pages (**verified real** — aboutamazon.com, Aug 2023) | Candidate-feedback summarization |
| ActiveCampaign | Full email-campaign generation from prompts | Outreach-email drafting |
| X/Twitter | Detect language + inline translate | Multilingual CV/job-post handling |
| YouTube/Twitch | Auto-flag spam/hate/inappropriate content | Application-content moderation |
| Freshdesk | Auto-categorize, prioritize, route tickets | **Candidate routing/triage** |
| Redfin | Per-listing Q&A chat assistant | **Per-candidate / per-job Q&A chat** |

## LLM mental model

- An LLM is a statistical structure (billions of parameters, multiple GB) trained on massive text corpora to **predict what comes next** — "autocomplete on steroids." No beliefs, no understanding; probability-based generation explains why the same question yields different answers.
- **Garbage-in-garbage-out warning applied to code:** trained on billions of GitHub lines including broken/outdated/insecure code, so generated code can *look* clean and still be buggy or insecure. (Same argument the review-layer thread makes — cf. CodeRabbit's real vuln catch in [[external|Storm Bear: jsm-practical-vibe-coding]].)
- Named models: GPT (OpenAI), Gemini (Google), Claude (Anthropic), Grok (xAI) commercial; Llama (Meta), Mistral open-source.

## Key Takeaways

- The framing is *career-defensive*: AI features are becoming baseline expectations like database skills — the exact motivation behind the operator's Goal #2.
- Every one of the 6 archetypes is a summarize/classify/route/converse pattern — i.e., **single-LLM-call tier** work (no agents needed), matching the "start simple" tier guidance in the Claude API docs.
- Two archetypes (Freshdesk routing, Redfin per-entity chat) map one-to-one onto recruitment SaaS features; see [[openai-to-claude-mapping]] for the Claude-side spec.
- Cross-link: [[tokens-and-cost]] for what these features cost; [[calling-models-responses-api]] for how they're wired.
