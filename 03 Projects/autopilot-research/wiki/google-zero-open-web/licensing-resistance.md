# The Resistance — RSL, Pay-Per-Crawl, Lawsuits, Regulators

## Source

- RSL: [TechCrunch launch coverage 2025-09-10](https://techcrunch.com/2025/09/10/rss-co-creator-launches-new-protocol-for-ai-data-licensing/) · [launch press release](https://www.globenewswire.com/news-release/2025/09/10/3147794/0/en/New-RSL-Web-Standard-and-Collective-Rights-Organization-Automate-Content-Licensing-for-the-AI-First-Internet-and-Enable-Fair-Compensation-for-Millions-of-Publishers-and-Creators.html) · [RSL 1.0 spec release 2025-12-10](https://www.globenewswire.com/news-release/2025/12/10/3203217/0/en/rsl-ai-licensing-1-0-now-an-official-industry-standard-with-new-capabilities-as-momentum-accelerates.html) · [rslstandard.org](https://rslstandard.org)
- Cloudflare: [MIT Tech Review on default AI-crawler blocking + Pay-Per-Crawl, 2025-07-01](https://www.technologyreview.com/2025/07/01/1119498/cloudflare-will-now-by-default-block-ai-bots-from-crawling-its-clients-websites/) · [Cloudflare press release](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/)
- Litigation/regulation: Chegg v. Google (2025-02-24) · [Penske Media v. Google (2025-09-14, TechCrunch)](https://techcrunch.com/2025/09/14/rolling-stone-owner-penske-media-sues-google-over-ai-summaries/) · [EPC complaint 2025-02-10](https://www.epceurope.eu/post/european-publishers-council-files-formal-antitrust-complaint-against-google-over-ai-overviews-and-ai) · [EU formal investigation 2025-12-09 (CNBC)](https://www.cnbc.com/2025/12/09/google-hit-with-eu-antitrust-probe-over-use-of-online-content-for-ai.html) · German liability ruling 2026-06-12 · [Digiday 2025 publisher-AI deal timeline](https://digiday.com/media/a-timeline-of-the-major-deals-between-publishers-and-ai-tech-companies-in-2025/)
- Video chapter 8 closer · verified by workflow `wf_7208577a-1cc` (C16 CONFIRMED by dive + refuter; 15 sub-claims all CONFIRMED)

## RSL — Really Simple Licensing (the video's named mechanism; the VN dub lost the proper noun)

- Launched **2025-09-10** by the **RSL Collective**: **Eckart Walther** (co-creator of RSS) + **Doug Leeds** (ex-CEO Ask.com / IAC Publishing). RSL 1.0 became an industry standard **2025-12-10**
- **The music-industry playbook, explicitly**: a collective rights organization modeled on **ASCAP/BMI** — radio pays blanket licenses for songs; AI systems pay blanket licenses for web content. The video's radio analogy is the founders' own framing, not a video invention
- Mechanics: machine-readable license terms embedded in **robots.txt**, HTTP headers, HTML tags, RSS/Atom feeds — supports attribution-only, royalty, **per-inference pricing**, subscription; optional OAuth-based access protocol (OLP)
- Adoption: **1,500+ media organizations** endorsing by Dec 2025 — incl. **Reddit** (the enclosure's winner hedging), Yahoo, Medium, AP, Vox, USA Today, Boston Globe, BuzzFeed, The Guardian, Slate, Ziff Davis, wikiHow, O'Reilly
- Sober note: payment rails (Supertab) in beta, ~12 customers; **enforcement is voluntary/market-based** — RSL declares terms, it cannot compel payment

## Cloudflare — the infrastructure lever

- **2025-07-01**: AI crawlers **blocked by default** for new Cloudflare domains (opt-in flipped from opt-out) — a unilateral rewrite of crawl norms by the network layer
- **Pay-Per-Crawl** marketplace: publishers set per-crawl prices for AI bots — the third option between allow and block

## The litigation & regulation wave (all dates verified)

| Date | Action |
|---|---|
| 2025-02-10 | European Publishers Council formal antitrust complaint (AI Overviews) |
| 2025-02-24 | **Chegg v. Google** (Sherman Act; AI Overviews trained on its 135M-question corpus; Chegg's traffic/stock collapse) |
| 2025-09-14 | **Penske Media v. Google** (Rolling Stone/Variety/Billboard owner): alleges content-for-AI-Overviews is *tied* to search visibility — cites the Pew study ([[pew-ai-overviews-study]]) |
| 2025-12-09 | **EU Commission formal investigation** into Google's use of publisher content for AI |
| 2026-01-27 | EU **DMA proceedings** ×2 (Android/Gemini interoperability; search-data sharing) |
| 2026-03-10 | EU Parliament vote scheduled on **statutory licensing** (AI firms must pay publishers); Brazil draft bill April 2026 |
| 2026-06-12 | **German court: Google liable for false AI Overview statements** — AI answers are "Google's own words," not attributed content; Google appealing. (Six days before the video shipped) |

- Meanwhile the **deal economy**: OpenAI 13+ publisher licensing deals in 2025 (Axios, Guardian, WaPo, News Corp, FT…); Amazon (NYT, Condé Nast, Hearst), Microsoft (pay-per-use marketplace), Meta (CNN, Fox, USA Today). **Google is the outlier** — few content deals (AP, Reddit); instead it is phasing News Showcase into an AI pilot that **conditions existing payments on granting AI-training rights** (Guardian, El País, Der Spiegel among participants; refusers lose Showcase money)

## Key Takeaways

- The resistance has all four layers now: **standard** (RSL), **infrastructure** (Cloudflare default-block + Pay-Per-Crawl), **courts** (Chegg/Penske/Germany), **legislators** (EU DMA + statutory licensing, Brazil). The video's closing "pushback is starting" undersells how organized it already was by its air date.
- RSL is the single most actionable artifact in this topic for any site owner: declaring terms costs a robots.txt edit ([[../google-zero-open-web/_index|pilot A4]]).
- The German liability ruling is the sleeper precedent: if AI answers are the engine's *own speech*, hallucination becomes legal exposure — for Google and for anyone shipping answer surfaces (hireui's future LLM features included).
- Google's "pay only when forced, tie payments to training rights" posture vs OpenAI's deal-making is the strategic split to watch; both converge on: **content access is becoming a licensed input, not a free crawl.**

Related: [[forum-boost-and-reddit-enclosure]] (the first purchased enclosure), [[antitrust-us-v-google]] (the US track), [[publisher-economics]] (why they're suing), [[state-of-play-2026]].
