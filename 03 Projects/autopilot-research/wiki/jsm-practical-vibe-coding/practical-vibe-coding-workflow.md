# The Practical Vibe Coding Workflow

## Source

- Transcript `raw/2026-07-03-jsm-practical-vibe-coding.md`, crash-course section 00:03:07–00:23:47 + build sections throughout.

## The positioning (vs Karpathy)

- Karpathy's vibe coding post: **2025-02-02** (x.com/karpathy/status/1886192184808149383) — "fully give in to the vibes … forget that the code even exists". Video says "earlier this year" — off by ~15 months ([[caveats-and-corrections]]).
- Karpathy explicitly scoped it to **"throwaway weekend projects"**. JSM's "practical vibe coding" **removes the throwaway constraint** and rebrands the middle ground as production-viable — the brand IS a response to Karpathy's caveat, without naming it.
- Collins Dictionary named "vibe coding" Word of the Year 2025 (verified; not claimed in video).
- Failure modes he names: pure-vibe = "ask AI to fix one thing, something else breaks … code you didn't write in a project you can't fully explain"; over-engineering = "preparing for a battle without ever fighting one".

## The loop

1. Write a minimal [[agents-md-anatomy|AGENTS.md]] up front — don't perfect it; **"solve it once, document it, move on"** (rules accumulate from real failures, e.g. the NativeWind/SafeAreaView quirk).
2. Build **one feature per prompt** using the [[four-part-prompt-structure]].
3. **Verify each feature on-device before the next** (Expo Go live-reload on a real phone is the verification surface — manual, no tests; see [[verification-and-review]]).
4. When something breaks: **one targeted fix prompt** — "state the problem, state the correct behavior, add a constraint if needed". Never re-explain the feature, never paste the codebase. "One problem, one fix, one verification."
5. Commit + push per feature; CodeRabbit reviews the PR ([[verification-and-review]]).

## The closing formula

> "A perfect prompt is just an instruction with a defined scope. And the scope is three things: what you're building right now, what works that you're not touching, and what rules the AI already knows from the file."

- AGENTS.md handles the rules; the task line handles what's new; constraints handle what's protected; design refs / doc-pastes attach as needed.
- "Build this way and it's contained when it breaks, because you only changed one thing."
- "The product will change, but the workflow doesn't. That's the actual skill."

## What's genuinely his vs repackaged

- The four-part prompt template + "constraints are about behavior, not code" articulation + "prompt for the infrastructure that lets you verify the feature" are crisp, teachable formulations — pedagogy is the value-add (same verdict as [[jsm-six-file-context/originality-and-reception|the sister topic]]).
- The underlying ideas (context file, scoped tasks, protect-working-code, docs injection) are established practice — cf. [[claude-md-12-rules]] (Rules 1/3/8), [[pocock-agentic-workflow]] (scoped prompts, harness-over-model), [[harness-engineering]].
- Notably ABSENT vs the six-file system: no feature-spec files, no progress tracker, no new-chat-per-spec ritual, no architecture-first phase. One file + prompt discipline is the whole harness — ceremony scaled down for a weekend-scale app.

## Key Takeaways

- Middle-path framing: keep AI speed, add minimum structure — one file, four prompt parts, one feature at a time.
- The evolving-AGENTS.md habit ("solve it once, document it") turns every debugging session into permanent harness capital — the same compounding move as this vault's prime directive.
- Fix prompts are deliberately minimal: problem + correct behavior + protective constraint.
- Verification = manual on-device checks; the methodology has **no automated tests** — its discipline lives entirely in prompts and review.
- The "defined scope" formula is a compact restatement of what [[claude-md-12-rules|12-rules]] spreads across Rules 1, 2, 3, and 4.
