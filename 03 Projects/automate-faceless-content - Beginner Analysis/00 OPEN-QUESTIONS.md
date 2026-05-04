# 00 OPEN-QUESTIONS — automate-faceless-content v55

Items NOT verified during probe. Operator-resolvable or future-wiki-resolvable.

## Author identity verification

1. **Is "Chris Porter" a real person with verifiable credentials?**
   - GitHub `cporter202` claims Erie PA + "AI Automation Expert / OG AI Wizard" + 933 followers + 20 public repos
   - Facebook profile linked (`chris.porter.7731`) but unverified by probe (no API call)
   - Bio links viralwavestudio.com (Chris's own brand)
   - **Cannot verify:** real name vs persona, actual location, actual credentials, "OG AI Wizard" claim (no time-stamped first-mover evidence)
   - **Not a blocker** for outside-scope wiki classification — wiki documents the public artifact, not personal credentials

2. **Is ViralWaveStudio.com Chris Porter's solo company or a multi-person brand?**
   - Probe did NOT visit viralwavestudio.com (out of scope; brand-marketing site)
   - Buy Me Coffee link uses `viralwavestudio` slug (consistent personal brand)
   - **Not verified:** company structure, team size, legal entity (LLC? sole proprietor?)

## Affiliate disclosure compliance

3. **Does the affiliate-link disclosure meet FTC requirements?**
   - README §Disclaimer: "This guide contains affiliate links. Using the provided link supports the maintenance of this resource at no extra cost to you."
   - This is a generic disclosure statement, NOT per-link disclosure
   - FTC §16 CFR Part 255 may require more prominent / per-instance disclosure
   - **Not adjudicated:** legal compliance status; varies by jurisdiction (US/EU/VN)
   - **Implication for Storm Bear:** if vault ever publishes with affiliate links, formal disclosure protocol needed; v55 is example of MINIMUM disclosure (not best practice)

## Course completion + abandonment status

4. **Why did Chris Porter abandon at 21% (13/61 lessons)?**
   - Last commit 2026-01-27; 3 months stale at probe (2026-04-26)
   - Possible explanations: pivoted to ViralWaveStudio.com primary brand / lost interest / monetization didn't justify ongoing work / ran out of free SyllabyDays.io content / etc.
   - **Not verifiable** without contacting author
   - **Implication:** marketing-claim "complete course" mismatched with delivered artifact (61 declared / 13 actual)

5. **Are the unbuilt lesson links (48 of 61) broken?**
   - README links many lesson files that MODULE-COMPLETION-TRACKER marks ⏳ "Ready" (= unbuilt)
   - Probe did NOT verify each link target's existence
   - **Likely:** many links 404 (module-1/lesson-2-why-it-works.md exists per `/bin/ls` but other lessons unverified)
   - **Implication:** README structure overstates delivered content

## Pattern Library overlap

6. **Is the new sub-context 29-absent-5 (commercial-content-creator-affiliate-funnel-no-formal-license) genuinely structurally distinct from 29-absent-1 (commercial-cold-start)?**
   - bizos v37 (29-absent-1) = solo-developer + commercial-app + 2-day-old (extreme cold-start) + no formal license
   - v55 = solo-content-creator + commercial-affiliate-funnel + 4.5-month + abandoned + "as-is educational" + affiliate disclaimer
   - **Distinctness criteria:**
     - 29-absent-1: developer-application + cold-start + commercial-future-direction + no-LICENSE
     - 29-absent-5 candidate: content-creator-tutorial + abandoned-mid-build + active-affiliate-monetization + "as-is educational" claim + disclaimer
   - **Mechanism distinct:** product genre (app vs tutorial) + commercial-stage (pre-monetization vs active-monetization) + license-claim (none vs "as-is educational")
   - **Audit decision required:** treat as new sub-context candidate OR absorb into 29-absent-1 with broader definition?
   - **Defer to next mini-audit operator decision**

7. **Should Pattern #50 sub-variant 50e (content-creator-affiliate-funnel-with-own-product) be registered now or wait for N=2?**
   - Routine v2.1 consolidation-forward discipline says register at N=1 with stale-flag if novel mechanism
   - 50e mechanism: course-content-as-affiliate-funnel-for-third-party-SaaS + own-product upsell + tip-jar + cross-repo promotion = 4-channel content-creator funnel
   - Distinct from 50a Standard (product-tier-funnel) / 50b Recruiting / 50c Aggregator-bundled-product / 50d Incubation-waitlist
   - **Decision:** register 50e at N=1 stale-flagged per discipline; promotion path = N=2 by v60

## Storm Bear meta-entity Phase 0.9 decision

8. **Was the lightweight-INCLUDE-with-cautionary-contrast framing the correct Phase 0.9 application?**
   - Strict-skip would honor "all 4 criteria fail" outcome
   - Lightweight-include preserves 38-consecutive streak via cautionary-contrast framing
   - **Operator decision precedent:** v55 sets template for future content-marketing or domain-distant wikis — cautionary-contrast IS valid Storm Bear meta-entity framing
   - **Future risk:** if every domain-distant wiki gets cautionary-contrast meta-entity, the streak metric becomes meaningless (always preserved)
   - **Recommendation:** if v56 is also domain-distant, apply STRICT skip to break streak deliberately and preserve meaningfulness of streak metric

## Potential v55 mini-audit triggers

9. **Should v55's 3 N=1 candidates accumulate before next mini-audit, or is this enough to trigger?**
   - Pattern Library state: 17 active candidates + 3 new N=1 stale-flagged at v55 = 20 candidates / 39 confirmed = ratio 0.51:1 still well below 0.95:1 mini-audit trigger
   - 11-candidate runway preserved
   - **No mini-audit trigger at v55**
   - Next natural-cadence trigger: candidate count ≥28 OR v58 wiki (+5-wiki natural cadence from v53) OR ratio >0.95:1 mini / >1.05:1 full
