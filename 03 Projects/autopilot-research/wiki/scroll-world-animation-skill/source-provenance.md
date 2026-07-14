# Source provenance — verification ledger

## Method

Full transcript read in the main loop (`raw/2026-07-14-scroll-world-animation-skill.md`, reconstructed from yt-dlp EN auto-captions). Verified via Workflow **`wf_885d81d7-1a2`** (12 of 12 launched agents completed or errored = 6 dives + 6 refute-first verifiers, all on Haiku 4.5) + 1 completeness critic, **~530K tokens, 190 tool calls**, followed by **~10 main-loop independent checks** (`gh api` ×2, `WebSearch` ×3, `WebFetch` ×5) specifically because two agents died mid-workflow and because one surviving finding (the GPT-5.6 government-restriction detail) read as suspicious enough to warrant independent re-checking before publication.

## Workflow agent failures (both "Prompt is too long")

- `dive:claude-fable-5` — died before returning anything. **Closed by main-loop takeover**: direct `WebSearch` + `WebFetch` of `anthropic.com/news/claude-fable-5-mythos-5` and `anthropic.com/news/redeploying-fable-5` produced a fuller, more specific finding (including the 19-day export-control outage) than the workflow would likely have surfaced.
- `verify:scrollworld-original` — the refute-first pass for the original repo's dive died before returning a verdict. **Closed by main-loop takeover**: direct `gh api repos/oso95/scroll-world` + `gh api users/oso95 --jq '{login,name,bio,blog,twitter_username,company}'` calls independently confirmed the repo's metadata and — critically — turned up the corrected identity finding below, which no agent had actually surfaced correctly.

## Confabulations caught and excluded (Rule 12 fail-loud)

1. **A dive agent claimed "GitHub profile oso95 reveals author's full name as Peter Wang."** This is not what the GitHub API says. A direct `gh api users/oso95` call shows the account's public `name` field is **`cyw`**, with bio "Founder & CTO @hermai-ai" and X handle `@the_cyw` — no field says "Peter Wang." The agent likely over-interpreted a secondary source (or the X handle itself) as confirming the video's spoken name. **This wiki treats "Peter Wang"/"Peter Wing" as an unconfirmed attribution, not a fact**, and uses the verified handle/company instead.
2. **A dive agent invented a specific Higgsfield MCP install command** (`claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp`). A direct `WebFetch` of `higgsfield.ai/mcp` shows the actual documented flow is a Settings→Connectors UI step, with a separately-mentioned (but not quoted) CLI path for terminal agents. The invented command does not appear on the page. **Excluded; corrected in [[scroll-world-animation-skill/original-higgsfield-platform]].**
3. **A verify agent claimed OpenAI's GPT-5.6 limited preview (2026-06-26) was restricted to "~20 government-approved organizations," gated "per US gov."** Independent main-loop `WebSearch` against OpenAI's own announcement pages and multiple press outlets (9to5Mac, TechCrunch, MarkTechPost, GitHub's own changelog) found no such restriction described anywhere for GPT-5.6. **This appears to be a cross-contamination/conflation error**, not a claim invented from nothing: it is very likely the agent merged this with the *separate, and genuinely real*, Anthropic Fable-5 export-control story (below) — both involve "government," "limited access," and the same rough two-week window, which is exactly the kind of surface similarity that causes an LLM research agent to merge two unrelated stories. **Excluded from the wiki.**

## A near-miss the other direction: don't discard true things that sound made up

Before accepting the workflow's Fable-5-adjacent findings, the main loop's own reaction to "Fable 5 was unavailable June 12–30 due to a US government export-control action after a safeguard bypass" was **initial skepticism** — it read like exactly the kind of oddly-specific, plausible-sounding detail that gets confabulated (per this project's own house rule against discarding date-sensitive claims as garble without checking first). **A direct fetch of `anthropic.com/news/redeploying-fable-5` confirmed the story is entirely true**, in detail: Amazon researchers found the bypass, the US government applied export controls June 12, Anthropic couldn't verify user nationality in real time so it suspended access for everyone, and access was restored July 1 after an improved safety classifier was trained. **This is logged as a discipline win, not a correction** — the claim was checked rather than assumed either way, and turned out to be real. See [[scroll-world-animation-skill/original-gpt-5-6-and-fable-5]] for the full writeup.

## Scorecard (12 claims from the crosswalk)

- **6 CONFIRMED** — Scroll World repo mechanism; Chase's fork improvements; Higgsfield MCP/CLI existence; GPT Image 2 + Seedance model access via Higgsfield; GPT-5.6 Sol identity/timeline; Fable 5 identity/timeline + single-invocation mechanism (with an omission noted separately)
- **3 CORRECT-BUT-INCOMPLETE** — the MCP connection flow (real, but not via the specific command a dive agent cited); the native-image-gen-in-Codex-vs-Higgsfield-carries-Claude-Code claim (architecturally plausible, not independently line-by-line re-verified); Fable-5-one-shot claim (true but omits the recent outage)
- **1 UNVERIFIABLE** — the exact "~800 credits" figure
- **1 UNVERIFIABLE (identity only)** — the creator's real name
- **1 MISLEADING-BY-OMISSION** — the likely undisclosed Higgsfield sponsorship
- **0 FALSE / 0 FABRICATED** — no claim in the video itself was found to be false; every correction made in this topic targets an over-claim or a conflation introduced by the *research workflow*, not by the video

This lands close to this corpus's higher-integrity end (alongside [[github-copilot-cli-agents/_index]] and [[local-ai-coding-agents/_index]]): the tooling claims all check out, the omissions are the usual creator-content pattern (sponsor + own-course promotion not disclosed on camera), and the one subjective claim (Fable 5's transitions) is treated as opinion rather than fact.

## Cross-links

[[scroll-world-animation-skill/_index]] · [[scroll-world-animation-skill/video-to-original-crosswalk]] · [[scroll-world-animation-skill/original-scroll-world-and-fork]] · [[scroll-world-animation-skill/original-higgsfield-platform]] · [[scroll-world-animation-skill/original-gpt-5-6-and-fable-5]]
