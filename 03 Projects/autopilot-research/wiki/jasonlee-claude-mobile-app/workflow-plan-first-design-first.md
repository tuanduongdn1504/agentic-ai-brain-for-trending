# The Reusable Workflow — Plan-First, Design-First, Fix-by-Screenshot

The transferable core of the video, separated from the revenue framing. Six moves, each verified against first-party tool documentation.

## 1. Plan-first gate
Prompt ends with **"Give me the full plan. Do not build first."** — explicit rationale: "otherwise it's just going to build things you don't want and you end up spending more in tokens." Same discipline as the corpus' spec-first cohort ([[external|Storm Bear: pocock-agentic-workflow]] grill-me, [[external|Storm Bear: jsm-six-file-context]], [[external|Storm Bear: system-thinking-ai-coding]] design-before-prompt), arrived at from the token-cost direction.

## 2. Competitor-crawl grounding
The planning prompt includes the competitor's website + App Store URLs so Claude crawls them and derives the feature list from a *real shipped product* rather than imagination. Cheap requirements-elicitation trick: the competitor's product page is the PRD.

## 3. Prompt-for-a-prompt (Claude Code → Claude Design)
Instead of writing the design brief by hand: "Give me a prompt I can give to Claude Design. **Don't give any design direction, just the features**" + extra feature requests + "I'm going to bring all the design back here for you to build out the back-end." The planning context generates a more detailed brief than the operator would write, while deliberately leaving visual freedom to the design tool. The round-trip intent is stated up front so the plan anticipates re-import.

## 4. Reference image instead of style prose
One Pinterest/Dribbble screenshot attached to the Claude Design prompt carries the entire visual direction (rounded corners, green/orange palette) — "give it some design direction, so it doesn't just give me any random design." Both surfaces (web dashboard + mobile variant) inherit the style in one pass. Manual tweaks (colors, placement) then happen in the editor panel **without re-prompting** — the stated token-saving move enabled by the 2026-06-17 upgrade ([[claude-design-handoff]]).

## 5. Export-zip roundtrip
Claude Design → Share → Export → **zip of design files** saved into the same folder the Claude Code session is connected to → "find the design files here... give me a plan to build out the back end for both apps." The filesystem is the handoff interface; no copy-paste of designs. (Anthropic's own supported handoff is `/design-sync` + code round-trips as of the June upgrade; the zip-into-folder flow is the manual equivalent.)

## 6. Fix-by-annotated-screenshot
Broken month-selector → phone screenshot → annotate what's wrong → AirDrop to desktop → attach + one-line prompt ("please fix the month selector on the dashboard"). Vision-grounded bug reports beat prose descriptions of visual defects. Sibling of the corpus' screenshot-verify loops ([[external|Storm Bear: how-we-claude-code]] agent-native verify).

## The cost-tiering intent (see the reality check)
The stated model policy — big model plans and reviews, cheap model executes ("maximize our token usage") — matches Anthropic's own routing guidance in spirit, but the video's *implementation* of it (a natural-language "use multi-agent workflow" prompt) does not demonstrably pin models per subagent. Full analysis: [[multiagent-cost-tiering-reality]].

## What the workflow does NOT cover
Requirements beyond the competitor's marketing page, tests, auth/RLS, secrets architecture, payments, store submission, monitoring. It is a **prototype pipeline** — pair it with the demo→production discipline in [[external|Storm Bear: ai-engineering]].

## Key Takeaways
- Plan-first + competitor-crawl + prompt-for-a-prompt is a genuinely cheap requirements pipeline for greenfield prototypes.
- Reference images > style adjectives; manual-edit panels > re-prompting for pixel tweaks.
- The filesystem (design zip in the project folder) is the lowest-friction design→code handoff.
- Screenshot-annotate-fix is the highest-signal bug-report format for UI work.
- Everything here produces a *demo*; [[expo-go-to-app-store-gap]] lists what remains.
