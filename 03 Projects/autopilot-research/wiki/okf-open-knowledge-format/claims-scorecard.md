# Claims Scorecard

Every **checkable** claim in the video + description, graded by verification workflow `wf_a8b95e41-6b3` (4 fact-check clusters + completeness critic) and main-loop Opus ground-checks (WebFetch/gh against the real repo, SPEC.md, blog, and Karpathy gist). See [[source-provenance]] for methodology, [[caveats-and-corrections]] for the corrections in full.

## Headline

**20 checkable claims: 11 CONFIRMED · 5 MISLEADING · 2 FALSE · 0 FABRICATED · 2 OPINION**

**Integrity read:** a **substance-reliable, numbers-sloppy** source. Everything about *what OKF is and how it works* checks out (11/11 spec + provenance claims CONFIRMED). The 2 FALSE items are careless magnitudes (star count, video count), not invented substance. The 5 MISLEADING items are **framing/emphasis**, led by personal-vs-enterprise ([[personal-vs-enterprise-framing]]). **No fabrications.** Comparable integrity profile to the corpus' cleaner explainer topics, with a numbers-hygiene demerit.

## Facts & provenance

| # | Claim | Verdict | Note |
|---|---|---|---|
| CL1 | OKF is an **official Google release** | ✅ CONFIRMED | Repo under `GoogleCloudPlatform` org; Apache-2.0; launch blog 2026-06-13 by Google Cloud Data Cloud tech leads Sam McVeety + Amir Hormati. Not a community project. |
| CL2 | Google's blog **credits Karpathy's LLM Wiki** | ✅ CONFIRMED | Blog quotes Karpathy directly and calls OKF a formalization of "the LLM-wiki pattern." |
| CL3 | "GPT 5.5 or Opus 4.8" are current capable models | ✅ CONFIRMED | GPT-5.5 released 2026-04-23 (codename "Spud"); Opus 4.8 real. |
| CL4 | Karpathy gist "got to **40,000 stars**" | ❌ **FALSE** | Gist has **~5,000★ / ~4,400 forks** (created 2026-04-04). ~8× inflation. Multiple independent sources + gist page. |
| CL5 | "A couple months ago" Karpathy released the pattern | ⚠️ MISLEADING | Actually ~**3 months** (gist 2026-04-04 → video 2026-07-02 = 89 days). Minor understatement. |
| CL6 | Google "**just quietly shipped**" OKF (description) | ⚠️ MISLEADING | It had a **public launch blog 2026-06-13**, ~**19 days** before the video. Low-key for Google ≠ quiet/secret. |

## What OKF specifies (SPEC.md verified)

| # | Claim | Verdict | Note |
|---|---|---|---|
| CL7 | OKF standardizes **two** things: organization + metadata fields | ✅ CONFIRMED | Reserved `index.md`/`log.md` + frontmatter conventions. (Nuance: folder *hierarchy* is NOT prescribed — [[what-okf-standardizes]].) |
| CL8 | **`type` is the single required** frontmatter field | ✅ CONFIRMED | SPEC: *"Required: `type` …"*. Recommended: title, description, resource, tags, timestamp. Cole's `related` is his own convention, not an OKF key. |
| CL9 | OKF is a standard for both **consuming AND producing** knowledge bases | ✅ CONFIRMED | SPEC defines distinct producer guidance + consumer guidance (incl. unknown-field tolerance). |
| CL10 | **Zero integration** — no plugin/RAG/vector-DB; "point your agent at a folder" | ✅ CONFIRMED | SPEC: OKF "does not define storage, serving, or query infrastructure." Deliberately tool-agnostic. |
| CL11 | The "**too simple**" critique is fair (OKF ≈ folder-org + metadata over Karpathy) | ✅ CONFIRMED | Accurate *but incomplete* — Cole under-credits real additions (mandatory `type`, recommended-field contract, reserved filenames, producer/consumer roles, unknown-field tolerance). |

## Cole's OKF bundle (`coleam00/cole-medin-ai-coding`)

| # | Claim | Verdict | Note |
|---|---|---|---|
| CL12 | The bundle is a **spec-conformant OKF bundle** (index + concepts + videos, `type` frontmatter, CLI) | ✅ CONFIRMED | Repo has `index.md`, `concepts/`, `videos/`, `log.md`, `okf-cli.py`, README. Frontmatter uses `type`. |
| CL13 | It's "**transcript-verified**" | ✅ CONFIRMED | Stated in repo description; no detail on the verification process given. |
| CL14 | The bundle has "**four videos**" | ❌ **FALSE** | `videos/index.md` lists **five**: Complete Guide to Claude Code; Principled Agentic Engineer; Next Evolution of AI Coding Is Harnesses; Context Engineering 101; Code 100x Faster with AI. |
| CL15 | It has **no LICENSE** | ✅ CONFIRMED | No LICENSE file — notable for a video whose whole thesis is *sharing* knowledge bases (reuse rights unclear). |
| CL16 | Workflow = "brings the bundle into your local **Obsidian or Notion**" | ⚠️ MISLEADING | README workflow is **git clone → read markdown directly / `okf-cli.py`**; "no database, no embeddings, no API, no special tooling." No Obsidian/Notion import step. |

## Framing & opinion

| # | Claim | Verdict | Note |
|---|---|---|---|
| CL17 | OKF is "**the future of personal agents / second brains**" (Cole's primary framing) | ⚠️ MISLEADING (by emphasis) | Google's primary framing is **enterprise data sharing**; personal use is real but secondary. [[personal-vs-enterprise-framing]]. |
| CL18 | "**PIV loop** (plan-implement-validate) is the primary mental model I always teach" | ⚠️ MISLEADING | Bundle README lists **5 co-equal concepts**; the demo agent named **"context engineering"** as his single biggest idea. PIV is *a* pillar, not clearly *the* one. |
| CL19 | "MCP did for agent↔tool what OKF does for agent↔knowledge-base" | 💭 OPINION | Cole's analogy, not Google's (blog never mentions MCP). Reasonable as framing. |
| CL20 | "Google is lagging in the AI race; Gemini isn't as good as GPT/Claude" | 💭 OPINION | Subjective, dated (Gemini 3.1 Pro exists). Cole grants Google is strong at *applied*-LLM guidance. |

## Key Takeaways

- **11 CONFIRMED / 5 MISLEADING / 2 FALSE / 0 FABRICATED / 2 OPINION.**
- The **substance is trustworthy** — OKF is real, official, minimal, and works as described.
- **Do not quote the numbers:** Karpathy gist ≈ **5,000★** (not 40,000); the bundle has **5 videos** (not four).
- The **dominant distortion is emphasis** — personal-second-brain framing over Google's enterprise-first intent (CL17), reinforced by CL5/CL6/CL16/CL18.
- Two honest OPINIONs (MCP analogy; Gemini-lagging) — flagged, not scored as facts.
