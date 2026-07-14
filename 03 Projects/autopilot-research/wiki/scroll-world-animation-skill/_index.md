# Topic: scroll-world-animation-skill

> **Chase AI's "Scroll World" — a Claude Code / Codex skill that one-shots a scroll-triggered, AI-video-animated marketing website** (image → AI video → FFmpeg frame extraction → scroll-bound playback), demoed twice (Codex + GPT-5.6 Sol, Claude Code + Claude Fable 5) and verified original-by-original.
> **Compiled:** 2026-07-14 (path 5 yt-dlp full transcript read in main loop + adversarial Workflow `wf_885d81d7-1a2` + ~10 main-loop independent follow-up checks after 2 workflow agents died and one surviving claim looked suspicious).
> **Source video:** Chase AI — "This Skill Turns Fable 5 & GPT 5.6 Into Web Design MONSTERS" ([KBH8P0z2AL8](https://www.youtube.com/watch?v=KBH8P0z2AL8), 2026-07-11, 9:49, ~35K views on a 149K-subscriber channel). Creator already cited in [[claude-code-plugins-stack/_index]], [[10x-claude-code/_index]], [[agent-dashboard-os/_index]].

---

## The premise

Invoke a skill (`/Scroll World` in Codex, or the Claude Code plugin equivalent), describe a brand and an art direction, approve a starting "anchor" image, pick a scene-count/mobile budget, and the skill autonomously generates AI "camera flight" videos per scene (via Higgsfield calling GPT Image 2 for stills and Seedance for video), extracts their frames with FFmpeg, and binds those frames to the visitor's scroll position so the finished site plays like continuous pre-rendered video as you scroll. See [[scroll-world-animation-skill/overview]].

**The load-bearing distinction from this topic's closest sibling, [[ai-web-design-workflow/_index]] (the Taste Skill video):** that topic's skill fixes *taste* (an anti-slop design gate applied to a static build); this skill generates *motion* — a genuinely different mechanism (AI-video-frame-scrubbing) solving a genuinely different problem (scrollytelling animation), not a competing tool for the same job.

## The originals → what they are

1. **`oso95/scroll-world`** — the real, MIT-licensed, 1,552★ original skill. Author's *verified* identity is GitHub handle `cyw` (Founder/CTO @hermai-ai); the video's spoken "Peter Wang"/"Peter Wing" (inconsistent even within the same video) is **unconfirmed**, not a fact. → [[scroll-world-animation-skill/original-scroll-world-and-fork]]
2. **`cth9191/scroll-world`** — Chase's real, confirmed fork (GitHub API `fork:true`), created 3 days after the original. Its three claimed additions (budget tiers, mobile tiers, SEO copy block) are all confirmed from the fork's own `FORK-CHANGES.md`. → [[scroll-world-animation-skill/original-scroll-world-and-fork]]
3. **Higgsfield** — the real generation platform + MCP server/CLI that both AI-model calls route through. GPT Image 2 and Seedance 2.0 both confirmed available on it. One invented install-command corrected; a very-likely-undisclosed sponsor link flagged. → [[scroll-world-animation-skill/original-higgsfield-platform]]
4. **GPT-5.6 Sol (OpenAI) + Claude Fable 5 (Anthropic)** — the two AI models powering the two demo runs. Both real, both confirmed independently after a workflow agent died on Fable 5 and a different agent's GPT-5.6 finding needed a conflation corrected. Fable 5's own recent history (a real 19-day US-export-control outage, June 12–30) is a genuine and relevant omission from the video. → [[scroll-world-animation-skill/original-gpt-5-6-and-fable-5]]

## Articles

- [[scroll-world-animation-skill/overview]] — the mechanism, the two demo runs (and why the "six scenes / ~800 credits" line isn't the delivered site), the presenter's subjective transition-quality verdict
- [[scroll-world-animation-skill/original-scroll-world-and-fork]] — both repos verified from source (README + FORK-CHANGES.md + `gh api`), the creator-identity correction
- [[scroll-world-animation-skill/original-higgsfield-platform]] — the MCP/CLI, the model access, the pricing gap, the likely sponsor link
- [[scroll-world-animation-skill/original-gpt-5-6-and-fable-5]] — both models confirmed independently, incl. the Fable 5 export-control outage the video never mentions
- [[scroll-world-animation-skill/video-to-original-crosswalk]] — every video claim → verified original → verdict
- [[scroll-world-animation-skill/source-provenance]] — the verification ledger: 2 workflow agent deaths closed by main-loop takeover, 3 confabulations caught and excluded, 1 true-but-suspicious-sounding claim confirmed rather than wrongly discarded

## Pilot

Ranked methods to apply this to the operator's flows: `output/(C) 2026-07-14-scroll-world-animation-skill-pilot-methods.md`.

## Cross-links

- [[ai-web-design-workflow/_index]] — sibling "AI-generated asset → coding-agent design skill" pattern (taste vs. motion)
- [[claude-code-plugins-stack/_index]] — same creator (Chase AI), prior video, same top-of-funnel (Skool community)
- [[ai-web-design-workflow/original-seedance-2-0]] · [[ai-web-design-workflow/original-chatgpt-images-2-0]] — Seedance 2.0 and GPT Image 2 both confirmed here as the same models, same product families
- [[jasonlee-claude-mobile-app/_index]] — an earlier corpus case involving a different Fable-5 pricing-window garble-guard
- [[claude-skills/_index]] — the Claude Skills / SKILL.md format this skill ships in

## Source provenance (headline)

Adversarially verified via Workflow `wf_885d81d7-1a2` (12 agents, ~530K tokens, 190 tool calls) + ~10 main-loop independent follow-up checks. **Scorecard (12 claims): 6 CONFIRMED · 3 CORRECT-BUT-INCOMPLETE · 1 UNVERIFIABLE (cost) · 1 UNVERIFIABLE (identity) · 1 MISLEADING-BY-OMISSION (sponsor) · 0 FALSE · 0 FABRICATED.** Two workflow agents died mid-run ("Prompt is too long") and were closed by direct `gh api`/`WebSearch`/`WebFetch` takeovers; three workflow-introduced confabulations were caught and excluded (a wrong creator-name attribution, an invented MCP install command, a conflated "government-restricted GPT-5.6 preview" claim); one claim that *looked* like confabulation (Fable 5's 19-day export-control outage) was checked rather than assumed and turned out to be entirely true. Full log: [[scroll-world-animation-skill/source-provenance]].
