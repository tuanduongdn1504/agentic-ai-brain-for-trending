# Caveats & Corrections

Concrete corrections to carry forward. Grades in [[claims-scorecard]]; framing in [[personal-vs-enterprise-framing]].

## Corrections (don't repeat these)

1. **Karpathy gist stars: "40,000" → ~5,000.** [CL4, FALSE] The gist ([442a6bf…](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), created 2026-04-04) has ~**5,000 stars / ~4,400 forks**. Cole's "40,000" is ~8× too high. When citing the Karpathy gist's popularity, use **~5K★**. (It *is* viral — the underlying tweet reportedly hit 16M+ views — but the gist star count is ~5K.)

2. **Bundle video count: "four" → five.** [CL14, FALSE] `coleam00/cole-medin-ai-coding/videos/index.md` lists **5** videos (Claude Code guide; Principled Agentic Engineer; Harnesses; Context Engineering 101; Code 100x Faster). Cole says "there's only four."

3. **"Google just quietly shipped OKF" → it had a public blog.** [CL6, MISLEADING] The [launch blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) went up **2026-06-13**, ~19 days before the video, authored by two named Google Cloud tech leads. Low-profile ≠ quiet.

4. **"Bring the bundle into Obsidian/Notion" → clone + read markdown.** [CL16, MISLEADING] The bundle README explicitly says *"you read it directly: no database, no embeddings, no API, no special tooling."* Consumption is `git clone` + read the markdown / use the small `okf-cli.py` to list/read by concept ID. There is **no Obsidian/Notion import** step; Cole's phrasing implies automatic integration that the repo doesn't provide.

5. **OKF does NOT prescribe folder hierarchy.** [CL7 nuance] The SPEC: *"The directory structure is independent of the domain — producers organize concepts however makes sense."* Cole's "it specifies exactly how you organize your files" overstates it — OKF standardizes **reserved filenames + progressive-disclosure indexes + metadata**, not a directory tree.

6. **`related` / `related_videos` is Cole's convention, not an OKF field.** [CL8 nuance] OKF defines only `type` (required) + `title`/`description`/`resource`/`tags`/`timestamp` (recommended). Cross-link fields are un-standardized (this is central to the interop critique — [[thesis-critique]]).

## The PIV-vs-context-engineering wrinkle [CL18]

Cole calls the **PIV loop** (Plan → Implement → Validate) "the primary mental model I always teach for AI coding" [14:51]. But:
- His bundle README lists **five co-equal concepts**: Claude Code, context engineering, the PIV loop, "the AI layer," and Archon.
- In his own demo [16:40–17:07], when the agent is asked *"What's Cole's single biggest idea for reliable AI code?"*, it answers **"context engineering"** — and Cole doesn't correct it.

Not an OKF issue, and not a contradiction so much as loose language ("the framework I teach" vs "the concept I emphasize most"). Flagged so the vault doesn't inherit "PIV = Cole's #1 idea" as settled fact. (Cross-ref: [[external|harness-engineering/_index]] for Cole's PIV/Archon lineage.)

## Risk to weigh before adopting: Google longevity

The [[thesis-critique]] raises the "killed-by-Google" concern. Fair framing:
- **The downside is bounded:** OKF is *just markdown + YAML + folders*. If Google abandons the spec, your wiki still opens in any editor and any LLM still reads it. You lose a *convention's future momentum*, not your data. (Contrast a proprietary format or hosted service — those strand you; OKF can't.)
- **But adoption momentum is the whole value prop.** OKF's pitch is interoperability, which needs sustained backing + native consumers. Betting a personal workflow on Google's follow-through is a real (if low-severity) dependency, and the repo is young with thin external adoption.
- **Net:** low-severity risk. Adopt-as-convention is safe; adopt-expecting-network-effects is speculative.

## Open questions (for a follow-up pass)

Surfaced by the completeness critic; none block compilation:

1. **The "paste this prompt" prompt [12:04].** Cole says you "paste this prompt" to make an agent consume the bundle, but the prompt text isn't shown in the video and wasn't located in the bundle README. → Check Cole's GitHub/Discord/Patreon, or just use the README's setup instructions.
2. **Real adoption footprint (as of 2026-07-15).** OKF repo ~7.1K★; Cole's bundle ~90★. How many *public* OKF bundles exist? Any native consumers (Claude Code / Cursor / Obsidian)? → The [[vault-adoption-pilot]] "WATCH" verdict rests partly on this being early.
3. **`samples/` dir not read.** The OKF repo has `samples/` — reviewing conformant non-Cole bundles would test whether adoption is genuinely easy across domains.

## Things the video got RIGHT that a skeptic might doubt

Per the discard-as-garble guard (don't reflexively dismiss fresh true claims):
- **OKF is genuinely from Google** — verified via the `GoogleCloudPlatform` org + named blog authors. Not vaporware, not a community fork.
- **`type` really is the only required field** — verified against SPEC.md text, not inferred.
- **GPT-5.5 and Opus 4.8 are both real** — GPT-5.5 shipped 2026-04-23; don't flag the model reference as garble.

## Key Takeaways

- Two hard number corrections: **~5,000★** (not 40,000), **5 videos** (not four).
- Three framing corrections: **public blog** (not quiet), **clone-and-read** (not Obsidian/Notion import), **no prescribed folder tree**.
- The Google-longevity risk is **low severity** (data survives; momentum may not).
- PIV-vs-context-engineering is loose language, flagged so it isn't inherited as fact.
