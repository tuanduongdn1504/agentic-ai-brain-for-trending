# Source provenance — pipeline, verification, misfire log

## Pipeline

1. **Ingest (path 5, yt-dlp)** — operator-submitted VN dub `UjskE6hGx6c` (BizMate AI Official); its description links the EN original `qOjleN2-50c` (official Claude channel). Both auto-caption tracks (`en`/`vi`) deduped to plain text and **read in full in the main loop** (~27.7K + ~29.3K chars) → `raw/2026-07-04-elicit-verifiable-agent-dsl.md`. No NotebookLM (two-video operator submission + original-resource chain).
2. **Main-loop primary fetches (before + after fan-out):** claude.com/code-with-claude/london-extended (session/time/track); elicit.com/blog + elicit.com/blog/author/james-brady; ought.org "Supervise Process, not Outcomes"; pi.dev (harness identity); yt-dlp metadata for both videos + the original's description (the "quiver of models" line).
3. **Deep-dive + adversarial verify** — Workflow **`wf_7c12cab8-7c9`** (task w4q0nelua): **30 agents** = 10 primary-source dives (elicit-product / elicit-evals / ought-lineage / james-brady / pi-harness / cwc-london-event / dsl-priorart / demo-claims / bizmate-dub / talk-claims-audit) + **19 refute-first verifiers** across 16 claim clusters (2 lenses on the 3 highest-risk clusters: ÆPL-name, pi-identity, Kevin-Chen-venue) + 1 completeness/confabulation critic. **~1.79M subagent tokens, 624 tool calls, ~8.2 min.** All 30 agents returned (zero deaths).

## Source tiers

- **T1 (primary):** the two YouTube transcripts + yt-dlp metadata/description; claude.com event pages; elicit.com blog/team/docs + docs.elicit.com; ought.org update posts (2022-04-06 process, 2023-09-25 spinoff); arXiv:2310.10627 (Factored Verification); GitHub (`goodgravy`, `oughtinc/ice`, `earendil-works/pi`); pi.dev; Bazel/Dhall/CEL/Unison/Nix/git/Fowler docs; NIST + UK-gov + DeepMind/Meta/MSR/HHMI announcements for demo grounding.
- **T2 (credible secondary):** Mario Zechner's blog + Armin Ronacher (lucumr) on the Earendil transition; Latent Space (Brady × Adam Wiggins, 2024-06-21).
- **T3 (weak/echo):** general "DSLs for AI agents" explainers (Microsoft devblog, firetiger, Endo Medium) — used only for the independent-articulation point, not for Elicit facts.

## Verdict summary (19 verifier verdicts)

- **CONFIRMED (17):** provenance (incl. 14:05–14:35 over the 14:50 snippet); James Brady identity + 4 blog posts + Latent Space; ÆPL name (2-lens) + near-zero written footprint (qualified — see overreach note); all ÆPL properties; full architecture (13 sub-claims); whole-program + memoization (8 sub-claims); pi-identity (2-lens; Pi = Earendil/Zechner harness, multi-provider, embeddable SDK); demo orgs/agreements (zero refutations); the 8-item checklist + priority ordering; Elicit company facts (spinout 2023-09-25, $9M PBC, 138M+ papers, launches); Ought lineage (2017 / 2022 process paper / ICE / spinout); Elicit evals (17-PhD Reports eval, systematic-review recall 93.6%); Kevin-Chen-venue (2-lens: London, **not SF** — cross-topic fix applied).
- **PARTIAL (2):** description-quiver (couldn't fetch the raw description text via WebFetch — but the main loop *did* capture it via yt-dlp, so it's T1-confirmed here; "quiver" is the description's word, absent from the spoken transcript but functionally accurate); prior-art-accuracy (most characterizations CONFIRMED; a few of my draft glosses corrected — Starlark termination is inferred not explicit; Dhall "total" is my word; see [[dsl-prior-art-and-design-space]]).

## Verifier / critic misfire log (Rule 12 — overridden with ground truth)

1. **Codex-deprecation misread** — a pi-identity verifier "explained" Brady's "probably not supposed to say Codex" via *Codex was deprecated in 2023*. Stale-cutoff error: the 2023 deprecation was the original Codex *API*; Codex is an **active** OpenAI agentic-coding family in 2026 (this vault's [[../codex/_index]] + Storm Bear v62 codex-plugin-cc). The aside is about **naming a rival at the host's conference**, not about a dead product. Corrected in [[pi-harness-and-curator-models]]. (Misfire class: refuting/explaining via retired-then-relaunched brand — sibling of the mosh pass GPT-4.1 misfire.)
2. **"Zero public mentions" universal-quantifier overreach** — dives asserted ÆPL/curator/event-sourcing appear **nowhere** on Elicit surfaces. The critic correctly flagged this as an unbounded claim from a *sampled* crawl. Wiki wording qualified to "no mention found on sampled surfaces (homepage, blog, docs, GitHub) as of 2026-07-04," not "provably absent." (Severity: medium; handled.)
3. **description-quiver "UNVERIFIABLE"** — a verifier couldn't fetch the YouTube description and marked it unverifiable. Overridden: the main loop had the full description from `yt-dlp --print "%(description)s"` (T1). Fetch-failure ≠ absence (recurring corpus class).
4. **VN-dub "could not independently verify BizMate channel"** — one dive marked the dub existence unconfirmed via search. Overridden: main-loop yt-dlp pulled the channel/video metadata directly (470 views / 10 likes / channel `UCrAXctjaddmG8ctC3Eoha3w`). Same US-search-blindness-to-small-VN-channel class as the prior BizMate pass.
5. **Kevin-Chen-venue framed as "critical correction to the wiki"** — verifiers were right on the fact (London, Tina Vachovsky taught SF) but over-read the *existing* wiki, which had **hedged** "venue unconfirmed; London most consistent." Only coarse commit-message shorthand said "CWC-SF." Upgraded the hedge to CONFIRMED; logged the over-read in [[../agent-memory-architecture/caveats-and-corrections]].

## Fabrication-stripping note

No dive fabricated sources this run; all 30 agents returned and the failure surface was (a) one stale-brand misread and (b) two fetch-failure-as-absence slips — all caught by main-loop primary fetches (yt-dlp description + metadata; pi.dev; event pages) done *before* synthesis, exactly the countermeasure the memory-architecture pass identified.
