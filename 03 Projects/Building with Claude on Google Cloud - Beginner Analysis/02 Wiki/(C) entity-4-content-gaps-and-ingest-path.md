# (C) entity-4 — Content gaps and ingest path (post-transcript)

**Status update 2026-05-21:** transcript ingest completed via yt-dlp en-original auto-captions. 5 of 10 original gaps now RESOLVED; the rest survive even with transcript and require the promised code release. Detailed post-transcript residual gaps in [[entity-8-pitfalls-and-simplifications]] (sections U1–U10).

## Gap inventory — updated

| # | Gap | Status | Resolution |
|---|---|---|---|
| G1 | The 5 roles | **RESOLVED** | PM / UI/UX Designer / Software Engineer / Security Engineer / Growth Marketer-Data Analyst. See [[entity-6-role-decomposition]] |
| G2 | Subagent ↔ role mapping | **PARTIALLY RESOLVED** | NOT 1:1. Roles are organizational stages the operator narrates by switching prompts; subagents are spawned within ONE role only (Software Engineer, hat 3) — 3 parallel subagents for API + ingestion + dashboard. See [[entity-6-role-decomposition]] §"What each role's Claude session looks like" |
| G3 | Specific Google Cloud services | **RESOLVED** | Cloud Run + Firestore + BigQuery + Looker (+ Vertex AI as model host). See [[entity-5-build-architecture]] |
| G4 | Vertex AI vs. direct Anthropic API | **RESOLVED** | Vertex AI, with Application Default Credentials. ~3 min of the talk pitches this setup specifically |
| G5 | MCP servers used | **MOSTLY RESOLVED** | Three named: **Developer Knowledge API** MCP (Google Cloud — for fresh GCP docs) + **BigQuery MCP server** (Agent Registry) + **MCP Toolbox for DB** (open-source, Looker integration). Figma MCP "simulated" — actual integration not shown |
| G6 | Custom Skills authored | **PARTIALLY RESOLVED** | Skills referenced by purpose: (a) Cloud-Run deploy skill, (b) Cloud-Run + Firestore connection skill, (c) Claude Code's pre-built security-review skill. **Skill body contents NOT shown** — pending code release |
| G7 | The shipping path | **RESOLVED** | Bundled into the security-review skill — it scans, auto-fixes one finding, then deploys to Cloud Run. (Note: speaker flagged the "review-deploy bundle" as a demo simplification) |
| G8 | What broke / what got skipped | **RESOLVED** | Captured in [[entity-8-pitfalls-and-simplifications]] §"Speaker-acknowledged simplifications" (S1-S5) and §"Unspoken gaps" (U1-U10) |
| G9 | Source code repository | **STILL UNRESOLVED** | Speaker said *twice* code would be released after the session. No URL located via 2026-05-21 search of speaker GitHub or related Google Cloud / Anthropic blog posts |
| G10 | Vertex AI prompt-caching usage | **STILL UNRESOLVED** | Transcript does not mention prompt caching. Speaker's separate LinkedIn post 2026-04 confirms 1-hour prompt cache on Vertex AI is GA — likely used by Claude Code under the hood, not visible to the operator |

## Original ingest options (for historical reference — Option B was chosen)

### Option A — Manual transcript paste (lowest risk, highest fidelity)

**Steps for operator:**
1. Open the original-language video https://www.youtube.com/watch?v=SqHsS737CeA
2. Open YouTube transcript (kebab menu → "Show transcript")
3. Copy/paste into `02 Wiki/(C) transcript-raw.md` here
4. Tell Claude: "ingest the transcript I just pasted"

**Outcome:** Entity pages 5–7 get added (architecture / role decomposition / step-by-step / observed pitfalls).

### Option B — Automated extraction via `yt-dlp --write-auto-subs`

**Steps:**
1. Operator confirms `yt-dlp` available locally + network access permitted
2. Claude runs `yt-dlp --write-auto-subs --skip-download --sub-format vtt 'https://www.youtube.com/watch?v=SqHsS737CeA'`
3. VTT file gets parsed into Markdown transcript
4. Same ingest as Option A

**Caveats:** Auto-subs quality varies; demos with code on screen are particularly lossy. Verify against the human transcript option if precision matters.

### Option C — Workshop-materials proxy

The 2026-05-29 SF workshop (Anthropic + Google Cloud) covers the same conceptual material with hands-on labs. **If lab materials were published**, they would give a more reproducible recipe than even the talk transcript.

**Search target:** GitHub for `googlecloudplatform/claude-code-workshop-may-2026` or similar; Google Cloud blog post within 2 weeks after 2026-05-29.

### Option D — Accept current state

Treat this wiki as the **conceptual scaffold + citation map**. The entity pages already cover the metadata, the concept stack, and the speaker context. The remaining 30% (build internals) lives in the talk itself; pointing a reader at the video is sufficient.

## Routine-v2.3 codification candidates (from this ingest)

1. **NEW typology tier for "conference-talk knowledge-source" subjects** — distinct from T1-T5 (all software products). Talks have: speaker + event + abstract + (maybe) companion repo. They are *not* shipped artifacts. Routine v2.3 should give them a discrete tier (proposal: "T6 Knowledge-Source — Conference Talk / Workshop").
2. **Transcript-ingest-as-required-Phase** — for video subjects, build is gated on transcript; without it, deliver "scaffold + gaps inventory" rather than fabricated entity pages.
3. **Pre-flight transcript availability check** — before accepting a video subject, the routine should verify transcript reachability (manual paste / yt-dlp / closed-captions presence).
4. **Vietnamese-dub vs. English-original entry-point handling** — operator-submitted entry-points may be localized; the routine should *always* resolve to original-language source for primary citation, with the localized cut as secondary reference.

These candidates flow forward to the next mini-audit (currently scheduled at v85 natural cadence). They are NOT added to vault state files in this ingest because this subject is out-of-typology.

## What would un-block full v82-style entity-page depth

~~Just one input: the transcript.~~ **DONE 2026-05-21** — transcript ingested via yt-dlp; 4 entity pages added (entity-5 through entity-8). Wiki now at transcript-deep state.

**What would un-block production-reproduction depth (next level beyond transcript):**

1. **The code release** speaker promised — would unlock G6 (skill bodies), G9 (repo URL), and the prompt visibility / subagent definition gaps from entity-8 (U1-U4).
2. **Speaker write-up** (Medium post pattern speaker is known for) — would clarify ambiguous demo choices and explain trade-offs the live demo glosses.
3. **Skill recipe extraction** — if speaker's skills (Cloud-Run-deploy, Cloud-Run+Firestore) are published under a Google-Cloud skills repo, vault should consider ingesting that repo as a separate corpus subject under the existing T-tier rubric (it's a code artifact, not a talk).
