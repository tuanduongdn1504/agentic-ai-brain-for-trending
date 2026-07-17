# Hands-on capability evidence (BridgeMind vibe-coding livestream)

> What Kimi K3 actually produced on-stream, separated from the streamer's framing. This is the deepening pass's core value-add: an **independent, hands-on corroboration** of the corpus finding that K3's real strength is frontend/visual code and its weakness is a shaky reliability floor. Source: [[vibe-coding-livestream-bridgemind]].

## What worked — frontend / one-shot generation (the real strength)

- **Horror-house game — one-shot.** "By far better graphics than we've seen on anything... better than Fable 5... better than GBT 5.6... for a one-shot, probably better than Opus 4.8." Playable, pick-up/put-down objects worked where Grok 4.5 and Opus 4.8 had failed. (⚠️ but see the failure on re-test below.)
- **Subway Surfers clone — one-shot** from a bare prompt ("create a clone of Subway Surfers using three.js in a single HTML file. Create a structured plan first"). Coin magnet + jetpack power-ups worked. This was the head-to-head vs Fable 5 that drove the poll.
- **Remotion marketing video — one-shot.** A 30-second product promo (React-based programmatic video via [Remotion](https://www.remotion.dev/) — confirmed a real framework). Streamer: "that's literally perfect."
- **Community-submitted creations** shown mid-stream (cherry-blossom sim, a full soccer game with goal graphics, paper-plane game) reinforced the visual-polish impression.
- **A real bug fix in a real codebase** (not a from-scratch toy): reviewed BridgeSpace logs + screenshot, found the root cause of a "sign in with browser → retry failed" bug — **"port 8080 is occupied by the wrong server."** Correct diagnosis on a live production issue.

**→ This directly corroborates [[benchmarks-fact-vs-hype]]:** K3's independently-verified edge is the **Frontend / Visual Code Arena (#1)**. A biased vendor and a neutral leaderboard agree on the one thing K3 is genuinely best at.

## What failed — the reliability floor the hype elides

- **Three black-screen failures:** the solar-system explorer (1st shot — "complete fail, just a black screen"; succeeded on the 2nd), the GTA-6/"Bridge City" remake, and one Subway Surfers attempt ("this one is just a black screen").
- **Key-spawn bug on the horror-house re-test:** on the live re-run, "I've only found one of three keys... it's like the spawns didn't work" — a regression on the very demo he opened with.
- **Minecraft rebuild never finished** during the ~77-minute stream ("it's got a lot of to-dos left... it's still working... so annoying").
- **Slow.** ~25–27 tok/s; the horror-house one-shot "took maybe 30 to 45 minutes." Reasons for a long time between updates ("48 seconds elapsed here without any updates"). Speed is corrected + contextualized in [[speed-pricing-and-local-reality]].

## Head-to-head vs Fable 5 (the poll)

- Prompted **identical** Subway Surfers builds on K3 and on **Fable 5** ("high extra high effort... build this from scratch"). Chat voted on the two side by side.
- Result driven to an on-stream poll: **~87–90%** of the live chat picked K3's game (300 → 729 votes across the stream). He then drafted an X-post: *"Kimi K3 beats Fable 5 in game development. Kimi K3 87%, Fable 5 13%."*
- **This is a real event** (verbatim in the transcript at [1:07:12] and [1:09:41]) — but a **selection-biased chat poll on a single game**, not a benchmark. Methodology critique in [[bridgemind-source-and-conflict-of-interest]]. Note he *himself* conceded GPT-5.6 Sol "did a better job than both" on the FPS game — the wins are cherry-picked.

## Honest reading

- **The capability is real and matches the corpus:** K3 is genuinely strong at one-shot frontend/game generation and can do real-codebase debugging. That is not nothing, and it is the single most reproducible signal here.
- **The reliability is not production-grade:** a ~1-in-3 black-screen rate on these demos, a regression on the flagship demo, and an unfinished build — the [[reception-and-skeptics|"capability ceiling, not reliability floor"]] point, shown live.
- **The comparison is stacked:** identical-prompt A/B is a reasonable idea, but the judge (hype-primed chat), the venue (his platform), and the cherry-picking (K3 wins highlighted, GPT-5.6 win conceded in passing) make the "beats Fable 5" headline marketing, not evidence.

## Key Takeaways

- One-shot frontend/game-gen = K3's real, independently-corroborated strength (horror house, Subway Surfers, "perfect" Remotion).
- Reliability is shaky: 3 black-screen failures, a spawn-bug regression, an unfinished Minecraft, slow generation.
- The "87–90% beat Fable 5" is a real in-video chat poll on one game — biased audience, biased venue, cherry-picked win (he conceded GPT-5.6 Sol beat both on the FPS).
- A genuine bonus data point the flagship topic lacked: K3 correctly debugged a **real** codebase issue (port 8080 conflict), not just toy generation.
