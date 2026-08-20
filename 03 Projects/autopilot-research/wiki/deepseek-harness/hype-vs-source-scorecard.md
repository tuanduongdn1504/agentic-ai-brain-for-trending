# YouTube layer vs source-verified corpus — what each caught that the other missed

> **This is why this topic exists.** DeepSeek Harness has zero coverage in this 78-topic YouTube corpus and **nine shipped source-level analyses** in the other vault (`/Users/Cvtot/KJ OS Template/03 Projects/`): v235 `deepseek-harness`, v236 `dsh-TUI`, v237 `dsh-better-sidebar`, v238 `dsh-anchored-standard`, v239 `dsh-web-ui`, v240 `awesome-dsh-plugin`, v241 `dsh-desktop`, v242 the recursive revisit with a 201MB source clone.
>
> So this ship is not an explainer. It is a **method experiment**: hand six commentary videos to the same corpus that already read the source, and see who was right about what.

## Verdict in one line

**The source read won on governance and mechanism. The video layer won on the paper, on ecosystem scale, and on failure modes.** Neither is a substitute for the other, and the specific pattern of who-missed-what is more useful than either finding.

---

## What the videos caught that the source read missed

### 1. The paper — and it was linked from the README

**The single most consequential miss.** `cordiverse/paper`, *"A Programming Paradigm for Spatiotemporal Composability"*, ~80 pages, Peking University + DeepSeek authorship, effects-and-coeffects type theory, a confluence result with stated boundaries. Two of six videos discuss it substantively; one reads the abstract aloud on camera.

**The vault's eight DSH ships do not record it.** And the DSH README — the file v242 quoted from at line 7 to establish the Cordis credit — *links the paper by title*.

This is not a subject finding. **It is a method finding: v242 opened `README.md`, extracted the credit it was looking for, and did not follow the outbound link on the same page.** The 201MB clone made the repository legible and made the *argument about* the repository invisible, because the argument was published next door.

The transferable rule:

> **A source read that stops at the repository boundary misses the literature the repository cites. Follow the outbound links in the file you are already quoting.**

Full treatment: [[deepseek-harness/cordis-and-the-paper]].

### 2. Ecosystem scale — the catalogue is a 16% sample

v240 audited the `awesome-dsh-plugin` catalogue (1,390 entries) prose-against-code and found the two views consistent. **Correct, and blind.** The `dsh-plugin` GitHub topic that the catalogue indexes holds **8,874 repositories** — the catalogue covers ~16% of it.

This is a clean N=2 confirmation of **v240's own inventory rule** (*a check between two views of one source is blind to what is MISSING from it*) — applied, this time, to v240. Full treatment: [[deepseek-harness/ecosystem-and-the-catalogue-gap]].

### 3. Failure modes under real conditions

No amount of source reading produces the Vietnamese source's 77 minutes of things going wrong: the Node ≥ 22.19 wall, the pnpm requirement, plugin-vs-harness Cordis version mismatch, plugins writing outside the selected workspace, plugins conflicting, high-star plugins that don't work while low-star ones do, per-plugin API-key sprawl.

**And one new rule, which corrects a v242 rule by extending it:** v242's D24 established that a version-number delta is not a code delta (rc.6 → rc.7 = zero code change). True of the repo. The VN source broke on that exact bump. Reconciliation:

> **A zero-code-delta version bump is not a zero-impact version bump when third-party plugins pin your kernel's version.**

Full treatment: [[deepseek-harness/install-and-operational-reality]].

### 4. The vendor's own sandbox disclaimer, surfaced and quoted

DSH's docs say the sandbox is *"containment for honest code, not a security boundary."* v240/v241/v242 built the same conclusion inferentially across three ships — catalogue checks metadata, installer checks identity, nothing measures effect. **The videos pointed at the sentence where DeepSeek says it themselves.** Same conclusion, primary-sourced instead of inferred. Full treatment: [[deepseek-harness/plugin-security-model]].

---

## What the source read caught that the videos missed

### 1. Governance produced the ecosystem — the videos see only enthusiasm

v242's headline: `CONTRIBUTING.md` refuses external pull requests and redirects contributors to publish plugins tagged `dsh-plugin`. 1,008 PR merges, all internal. `github.com/deepseek-harness` is a real org with zero public repos.

**Not one of six videos mentions this.** Five celebrate the exploding plugin ecosystem as organic community momentum. The VN source comes closest, documenting the topic tag as the discovery mechanism — but frames it as community behaviour, not as the only permitted contribution channel.

**"Everything is a plugin" is an architecture and a contribution policy.** The videos have the first half. Only the source read has the second, and the second explains the first.

### 2. Provenance discipline

v242 established: 12,404 commits with one root commit, no squash suffixes, exemplary vendoring (9 Shigma packages with author + MIT + per-package LICENSE preserved, 18 documented modifications), deny-by-default install scripts (5 allowed / 3 explicitly denied), 1,203 lockfile resolutions with zero npmmirror/taobao/cnpm, and `postinstall` de-risked as 845 lines of Node stdlib with no network fetch.

**No video checks any of this.** Chase AI's *"I actually had Claude Code take a look at it"* is the closest anyone gets to a supply-chain check, and it is one plugin, not the dependency tree.

### 3. The counts that need a language basis

v242's D23: *"1,386 decision records"* is a bilingual double-count (real: 693 EN); *"~170K doc lines"* is ~90,857 English. The project runs a git merge driver to keep `.md`/`.zh.md` pairs aligned, and naive counting doubles everything.

The videos never reach these numbers — but the VN source reads **"TypeScript 97.1%"** straight off the GitHub language bar, which is precisely the class of number D23 warns about. Recorded with that caveat in [[deepseek-harness/caveats-and-corrections]].

### 4. The absence of an eval harness

v242: 816 spec files, ~299K lines of test code against ~245K source, 4 postmortems, 11 recorded *rejected* decisions — **and no eval harness at all**, `BENCHMARK.md` still 3 lines.

**No video mentions evaluation, benchmarks, or measurement of agent quality once.** Six videos, ~127 minutes, zero. That silence is itself the finding: the commentary layer has no vocabulary for "is this agent actually better," which is the only question a pilot decision turns on.

---

## The pattern

| | Source read (v235–v242) | Video layer (this ship) |
|---|---|---|
| **Sees** | governance, provenance, counts, structure, what's absent | the argument, the ecosystem's true size, failure under load, the vendor's own words |
| **Blind to** | literature the repo cites; scale outside the repo; runtime behaviour | policy behind architecture; supply chain; measurement; anything requiring a diff |
| **Systematic bias** | treats the repository as the boundary of the subject | treats the demo as the boundary of the subject |

**Both failure modes are boundary errors.** The source read drew the boundary at the clone; the video layer drew it at the screencast. Each caught exactly what fell outside the other's boundary.

**The operational upshot for the vault:** for a subject with both a repo and a commentary layer, **the cheap complement to a source read is not another source read — it is the commentary layer, and vice versa.** v242 was a recursive revisit that re-read the same artifact more carefully and still missed the paper. A single 14-minute video caught it.

## Corrections owed to the other vault

Recorded here, **not self-executed** — editing another vault's ships is an operator decision:

1. **v242 / the DSH chain**: add `cordiverse/paper` and the spatiotemporal-composability formalism. Currently absent from all nine ships.
2. **v240**: the 1,390-entry catalogue count is correct and should be restated as *"1,390 curated entries out of 8,874 `dsh-plugin` topic repositories (~16%)."*
3. **v240/v241**: `dsh-market` — a runtime in-harness marketplace — is a third ecosystem surface neither ship covers.
4. **v242 D24**: extend with the plugin-pinning corollary above. The rule is not wrong; it is scoped to the repo and reads as scoped to the impact.
5. **v242 PIN "do not cite any star figure"**: refine to permit date-stamped page-stated figures with provenance, while continuing to forbid figures sourced from DSH's own UI and any velocity record. See [[deepseek-harness/star-velocity-and-the-superlative]].

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/cordis-and-the-paper]] · [[deepseek-harness/ecosystem-and-the-catalogue-gap]] · [[deepseek-harness/plugin-security-model]] · [[deepseek-harness/install-and-operational-reality]] · [[deepseek-harness/claims-scorecard]] · [[deepseek-harness/caveats-and-corrections]] · [[prompt-evaluation/_index]]
