# (C) Open questions — autoresearch_folktales wiki v79

20-30 questions to investigate during Phase 2-3 ingestion + entity-building.

## Authorship + provenance

1. **Thu Vu identity** — GitHub user thu-vu92 has 2,361 followers + bio "A data nerd who loves hacking stuff to learn new things" — what is the strongest evidence she is the same person as the public-internet data-science YouTuber Thu Vu? (verify only what's directly observable: README YouTube link + GitHub-public-data; AVOID fabricating biographical claims)
2. **YouTube walkthrough video** (https://www.youtube.com/watch?v=XXR0zZ0_16M) — is this hosted on her channel? Is it specifically about this repo? When was it published vs the repo's 2026-04-24 creation date?
3. **Why folk-mythology-tales dataset specifically?** — README doesn't justify the choice; was it because (a) small enough for MPS budget? (b) editorially interesting? (c) pedagogical for YouTube audience?
4. **Is this her first LLM-training repo?** — public_repos=42 + bio mentions "hacking stuff" suggests portfolio breadth; what's the lineage?
5. **Vietnamese-diaspora signal strength** — name "Thu Vu" + bio + 10-year-account → strong Vietnamese-name inference; is there any explicit national/cultural identifier in profile?

## Lineage to Karpathy (v9 corpus parent)

6. **Why miolini/autoresearch-macos as intermediate adapter** rather than direct fork of Karpathy? — what does miolini's port add that Karpathy's original lacked for MPS?
7. **Is `program.md` byte-identical to Karpathy's** original `program.md` in `karpathy/autoresearch`? — based on text, appears verbatim from Karpathy; verify if any modifications
8. **train.py vs Karpathy's train.py** — what specifically did Thu Vu modify for MPS? (FlashAttention-3 removed + native PyTorch SDPA + torch.compile-disabled + Metal-compatible optimizer states per README design-choices section)
9. **nanochat lineage** — README mentions `karpathy/nanochat` as underlying training implementation; how does v79 inherit from nanochat vs autoresearch?
10. **Does autoresearch_folktales preserve Karpathy's "git-based experiment tracking" + commit/discard/keep workflow?** — based on program.md verbatim text, YES; verify if branch `autoresearch/apr10` is the agent's working branch

## Pattern Library implications

11. **Pattern #57 57g vs 57f distinction** — v78 57f = anchor-self-reference (same subject revisited); v79 57g = derivative-chain via intermediate adapter (different subject, methodology inheritance) — is this a clean sub-variant taxonomy?
12. **Pattern #19 19j candidate "Vietnamese-Diaspora-Data-Scientist-YouTuber-with-LLM-derivative-experiments"** — does this profile have N≥2 precedent? (likely N=1 PROVISIONAL; consider 19j vs Pattern #19 strengthening)
13. **Pattern #83 83f N=4 strengthening** — README "MIT" declared but GitHub API `license: None`; does this fit 83f.3 sub-variant (declared-in-README-but-no-LICENSE-file) or NEW 83f.4 sub-variant?
14. **Pattern #84 NEW sub-typology 84d "Hardware-Substrate-Tolerance" candidate** — Apple Silicon MPS port = hardware-substrate-portability dimension distinct from 84a-Tool / 84b-Usage / 84c-Provider; does this register as 84d N=1 or as Pattern #84 within-pattern?
15. **Pattern #18 NEW sub-archetype #9 candidate "agentic-research-framework-with-constraint-architecture"** — single-modifiable-file + fixed-time-budget + never-stop-autonomy define a constraint-architecture; how does this compare to v68 zero T1 sub-archetype #7 + v70 codegraph sub-mechanism B "one-binary-many-CLIENTS"?
16. **Pattern #45 NEW sub-typology 45f candidate "README-Declared-MIT-without-LICENSE-file"** — corpus-first license-state distinct from 45a-d? OR Pattern #29 absent-LICENSE strengthening?
17. **Pattern #66 within-pattern** — minimal-dependency-discipline (PyTorch-only + agent CANNOT install new packages per program.md) — does this register as 66f sub-mechanism or 66 within-pattern strengthening?

## Storm Bear (a) axis nuance

18. **(a) STRONG PASS reasoning** — Thu Vu = Vietnamese-diaspora-data-scientist + YouTube walkthrough creator = cultural-peer at STRONG depth; second VN-diaspora subject in v60+ window after v76 HoangNguyen0403; does v79 register a sub-mechanism within (a) for "VN-diaspora-non-VN-located solo developer"?
19. **Is the YouTube walkthrough Storm Bear-relevant** — Storm Bear is a Scrum Coach + software developer; a "build LLM from scratch on MPS" YouTube tutorial is data-science-pedagogy-relevant but NOT Scrum-relevant; (b) FAIL stands

## Methodology + design choices

20. **Why 5-minute time-budget specifically?** — Karpathy choice; on MPS this yields 85-90 optimizer steps vs 1000s on GPU; is this an example of "method-preserved despite throughput collapse" tradeoff?
21. **val_bpb as vocabulary-size-independent metric** — clever choice; does this generalize beyond LLM-training (e.g., could vault routine v2.2 use a similar size-independent quality metric for wiki output?)
22. **Single-modifiable-file design** — only train.py is mutable; prepare.py + program.md read-only — what's the cognitive-load justification? does this prevent runaway-context-thrashing for the agent?
23. **Never-stop-autonomy** — program.md explicit: "Once the experiment loop has begun, do NOT pause to ask the human if you should continue" — how does this interact with current Claude Code session-handoff patterns (v71 + v73 wikis)?
24. **VRAM as soft constraint + simplicity criterion** — design-choices encode subjective trade-offs explicitly; does v79 demonstrate "explicit-tradeoff-documentation" as a meta-design-pattern observation?

## Distribution + ecosystem

25. **uv package manager dependence** — astral.sh tooling adoption; how does v79 compare to v76 agent-skills-standard (also uv-adjacent via pnpm-workspace)?
26. **Hugging Face datasets integration** — merve/folk-mythology-tales; is HF integration corpus-first or N+1?
27. **Apple Silicon as deployment platform** — first corpus subject specifically scoped to Apple Silicon; does this open NEW classification axis "hardware-substrate-target" alongside existing "i18n coverage" axis?

## Audit + future-checkpoint considerations

28. **Should v80 audit consider Pattern #57 57g promotion-acceleration?** — given v78 57f + v79 57g = 2-wiki consecutive sub-variant accumulation, is this a Library-vocabulary item #10 strengthening (1-wiki rapid-pattern-evolution)?
29. **Pattern #18 sub-archetype #9 candidate N=1** — first-cycle stale-check at v84? retire-check at v89?
30. **What does this wiki signal about routine v2.3 codification?** — single-push-and-done activity + LOW-velocity + high fork_ratio + corpus-recursive at second-order chain → potential new axes for routine v2.3
