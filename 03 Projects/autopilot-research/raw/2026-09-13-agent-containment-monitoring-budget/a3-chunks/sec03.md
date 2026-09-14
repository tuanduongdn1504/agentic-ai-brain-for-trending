# Investigation process and limitations

*In this section we discuss the scope and process of this investigation, including the datasets we analyzed and their remaining limitations. See [here](#preliminary-answers-to-the-core-questions-in-scope) for more details on our findings*.

## Scope of this investigation

OpenAI defined the investigation period as June 26th through July 13th, spanning both precursor activity before the incident and the incident itself, which began with the ExploitGym runs starting on July 7th.<sup>[^38]</sup> The analysis focused overwhelmingly on the incident period: virtually all of the data reviewed was from July 7th or later. In [OpenAI’s recent Black Hat presentation](https://www.youtube.com/watch?v=87DyyMV0kCY), they describe that agents had been using unsanctioned message boards in training since May, and that the compromise of OpenAI’s own infrastructure continued past July 13th; these events were out of scope for this investigation.<sup>[^39]</sup>

On July 29th we reached an agreement with OpenAI to conduct an independent investigation of the Hugging Face attack scoped to the following seven questions, which we directly answer in more detail in the [next section](#preliminary-answers-to-the-core-questions-in-scope):

1.  What model(s) were involved in the attack on Hugging Face during the June 26th through July 13th window? Were they internally deployed, or used only for testing? Were some of the model(s) not intended for production (e.g. helpful-only)?
2.  What were the prompts and instructions given to the agents involved in this incident?
3.  What was the sequence of key actions taken by the relevant agents in this incident?
4.  What was the agents’ reasoning, and how did it evolve over the course of this incident?
5.  Did this incident involve agents taking active steps to conceal their actions?
6.  Did this incident involve significant collaboration between different model instances, and how?
7.  Did the nature of the benchmarking exercise (ExploitGym) contribute to the misaligned behavior?

In a [previous post](https://metr.org/blog/2026-07-28-investigating-ai-propensities-after-incidents/), we described what an independent investigation of agent propensities following a misalignment incident could look like. Questions 1-6 in this investigation have close analogues to questions we describe in that post; question 7 was added at the request of OpenAI. This investigation does not cover the following topics from our earlier post:

- Whether the misaligned behavior displayed in this incident was part of a broader pattern of similar incidents.
- Whether agents would have been willing to engage in more severely harmful behavior under different circumstances.
- How this behavior arose during training and how it could be addressed.

We agreed all other questions were also out of scope, including the effectiveness of safeguards, the extent of the security compromise that occurred, and the effectiveness of OpenAI’s investigation process and planned remediation steps.

## Setup and timeline

The initial planned investigation period was two days on premises, but OpenAI invited us to return twice to review additional data and conduct additional experiments to address dataset [limitations](#limitations-due-to-the-scale-and-complexity-of-this-incident) in earlier versions of this report, ultimately providing datasets that we verified to [contain the vast majority of agent communication and activity](#a-small-fraction-of-communication-and-agent-activity-related-to-this-attack-was-not-captured-in-our-datasets) related to this incident. As we describe in [our investigation timeline appendix](#appendix-timeline-of-investigation), we substantially deepened our understanding of this incident both times, significantly expanding and revising this report.<sup>[^40]</sup>

Over the course of this investigation, OpenAI provided us with the dump of [~1.2 million entries](#a-dump-of-1.2-million-entries-from-a-cache-namespace-that-agents-used-as-a-message-board) from the main message board and the dataset of [~1300 transcripts](#a-set-of-~1300-agent-transcripts-with-raw-chains-of-thought) we describe below, as well as free API credits for GPT-5.6 Sol for analysis.<sup>[^41]</sup> At our request, they raised the rate limits on our second and third period on premises,<sup>[^42]</sup> which was very helpful for efficiently analyzing this large volume of data. We estimate we spent roughly ~\$400K in API credits over the six days of our investigation.

We did not have the ability to query HPIM ([the primary model](#brief-answers-to-basic-informational-questions) involved in this incident); OpenAI [stated](https://openai.com/index/hugging-face-model-evaluation-security-incident/) it was also not available to OpenAI researchers.<sup>[^43]</sup> We also did not have the ability to directly access relevant data from OpenAI infrastructure, but we could request additional datasets and OpenAI shared additional datasets on several occasions.

We requested to speak with researchers investigating this incident, and asked them questions to understand their impressions of agents’ behavior, reasoning, and collaboration in this incident and to understand how the datasets we were using were constructed. Over the course of our time on premises, we spoke with nine researchers in some depth. It was helpful for our investigation to be able to engage with many forthcoming and collaborative researchers, and we appreciate researchers making time on short notice during a busy period to inform our investigation.

## Main data sources

Our final analysis relies on two main sources of data:

- A dump of [1.2 million entries from the main Artifactory cache namespace](#a-dump-of-1.2-million-entries-from-a-cache-namespace-that-agents-used-as-a-message-board) that agents used as a message board, which broke down into \>70,000 distinct messages and files.
- A set of [~1300 agent transcripts with raw chains of thought](#a-set-of-~1300-agent-transcripts-with-raw-chains-of-thought), which captures the vast majority of agents that interacted with this message board during the time period in scope for this investigation.

We relied heavily on [tracing message board messages](#estimating-the-completeness-of-our-transcript-dataset) back to agents that wrote and read them to reconstruct the complex narratives we discuss in this report.

### A dump of 1.2 million entries from a cache namespace that agents used as a message board

The full dump from the relevant namespace in the Artifactory cache contained ~20 million files and directories. OpenAI stated that this dump was collected on July 20th; entries have timestamps that go through July 19th.

Of these 20 million entries, roughly 1.2 million start with `‘zz’`, the convention agents consistently used to start their messages.<sup>[^44]</sup> The vast majority of these `‘zz’` entries were encoded fragments of files. Our analysis identified ~6000 files (each of which was encoded as hundreds or thousands of individual message board entries) and ~63,000 individual non-file messages. Of the remaining unclassified entries, we believe they likely break down into a few hundred additional files and a few thousand additional non-file messages (more details in our [section on agent collaboration](#categories-of-messages-on-the-message-board)).

The dataset we directly worked with only contained these ~1.2 million `‘zz’` entries, but we collaborated with an OpenAI researcher to examine the ~18.8 million non-`‘zz’` entries and confirmed they did not look like intentional communication (though the vast majority of them did seem related to cheating on cyber tasks).<sup>[^45]</sup>

### A set of ~1300 agent transcripts with raw chains of thought

For our first two periods on premises, we worked with a selected set of ~285 HPIM and Sol transcripts; during our second period on premises, OpenAI stated that these transcripts were assembled by searching for “indicators corresponding to intrusion steps”.<sup>[^46]</sup> For our third investigation period, OpenAI additionally shared an overlapping dataset of 1196 transcripts selected by a simple search designed to find the agents that interacted with the main message board during the incident period:

- 1074 HPIM ExploitGym transcripts between July 7th and July 13th that matched a regex search for `github-remote-cache/zz` (that is, the name of the Artifactory namespace used as the main message board plus the string `zz`).
- 122 Sol ExploitGym trajectories that matched the same regex search in the same date range.

Across both datasets, we reviewed approximately 1300 transcripts in total, all of which contained raw chains of thought. Most transcripts were very long, often many millions of tokens.

The transcripts in the dataset included approximate timestamps for the start and end, but did not include timestamps for individual agent actions; OpenAI stated that it was not feasible to reconstruct these timestamps within time and compute constraints. During our second period on site, we implemented a reasonably well-validated way to [reconstruct approximate timestamps](#timestamp-reconstruction-methodology) for individual actions.<sup>[^47]</sup>

## Limitations due to the scale and complexity of this incident

The unprecedented scale and complexity of this incident presented two important challenges for our investigation:

- Because the agents involved found a number of different ways to communicate and were engaged in a [wide variety of cheating R&D projects](#large-collective-projects) with unpredictable side effects, it is not trivial to reliably surface all relevant agent activity, and that agent activity can itself modify or delete relevant data. Ultimately, [a small amount of communication and activity related to this attack was not captured in the datasets](#a-small-fraction-of-communication-and-agent-activity-related-to-this-attack-was-not-captured-in-our-datasets) we used for our final analysis.
- Because there were over a thousand transcripts and most were extremely long, [we had to heavily delegate our analysis to AI agents](#we-heavily-delegated-our-analysis-to-often-unreliable-ai-agents); these agents had [significantly worse judgment and reliability than human researchers](https://metr.org/blog/2026-05-19-frontier-risk-report/#agents-had-significantly-worse-judgment-and-reliability-than-human-experts), and it was challenging to spot check their work because both the underlying data and the agents’ analysis of it was often difficult to interpret.

### A small fraction of communication and agent activity related to this attack was not captured in our datasets

We found evidence that:

- There was some agent communication conducted on other platforms that would not be captured in the dump from this particular Artifactory cache namespace ([more](#there-was-some-agent-communication-conducted-in-other-locations-not-captured-in-our-message-board-dump)).
- Many transcripts in our dataset are missing small components, often due to [container resets](#attempting-to-forecast-and-trigger-container-resets), and a significant fraction have a small number of [intentionally spoofed tool calls](#efforts-to-conceal-actions-and-tamper-with-transcripts) done by agents as experiments ([more](#many-of-our-transcripts-are-missing-small-components,-and-a-small-number-of-relevant-agents-may-not-be-included-in-our-dataset)).

#### There was some agent communication conducted in other locations not captured in our message board dump

**Fraction of relevant agent communication captured in the message board dump** Our [message board dump](#a-dump-of-1.2-million-entries-from-a-cache-namespace-that-agents-used-as-a-message-board) comes from one particular Artifactory cache namespace that served as the main message board, but the same agents found a number of other ways to abuse Artifactory to communicate:<sup>[^48]</sup> for example, by making directories in at least one *other* cache namespace, setting “property” fields of cache entries, and requesting discussion pages with fabricated names (on a software hosting service) which resulted in these names being cached. OpenAI estimates that the entries in this specific namespace capture at least 95% of the unsanctioned agent communication that was conducted via Artifactory in the relevant time period; our understanding is consistent with this, though we did not investigate it carefully.

Separately, both we and OpenAI have found evidence of agents passing state back and forth to each other entirely outside of Artifactory during this incident (e.g. sharing files with one another on an external service or through Hugging Face datasets).<sup>[^49]</sup> However, our scans of transcripts indicate that these alternative communication platforms likely contained a small minority of relevant communication.

**Integrity of records in the message board dump** We looked for evidence that agents may have deleted or edited the entries on this specific Artifactory cache itself before we retrieved our dump. In the scans of the transcripts we have access to, we found that agents sometimes try to edit or delete messages, but did not see one succeed. Our overall view is that it was unlikely that our message board dump was materially altered by agents editing or deleting entries,<sup>[^50]</sup> but we cannot rule it out.

#### Many of our transcripts are missing small components, and a small number of relevant agents may not be included in our dataset

**Fraction of relevant agent activity captured in the transcript dataset** To determine what fraction of agent activity we had in our dataset, we randomly sampled 100 non-file messages sent between July 7th and July 13th. For each message, we tried to locate the action that wrote it among our transcripts. Based on this message tracing, we believe that the agents in our dataset were responsible for well over 95% of relevant message board activity in this date range.

However, the majority of our transcripts appear to be missing a small amount of activity from that agent. This appears to be due in part to [container resets](#attempting-to-forecast-and-trigger-container-resets), and an unknown fraction of our transcripts appear to be cut off early. As a result, we believe that we have a bit over 90% of the agent *activity* on the message board between July 7th and July 13th (see methodology details in [this appendix](#estimating-the-completeness-of-our-transcript-dataset)).

**Integrity of records in the transcript dataset** OpenAI attested that the transcripts we reviewed were unredacted, and we did not notice evidence of redaction. However, as we discuss [above](#agents-were-very-interested-in-manipulating-their-own-transcripts,-and-their-tests-successfully-%E2%80%9Cspoofed%E2%80%9D-some-tool-calls-in-our-transcripts), we estimate that over 7% of the transcripts in our dataset contained intentionally spoofed tool calls in some places. All the cases of successful tool call spoofing we found were small-scale tests of the techniques and obvious to spot. We looked for and did not find transcripts with more subtle spoofing, or cases in which agents spoofed a large number of tool calls to achieve a downstream goal.<sup>[^51]</sup> Separately, many [poisoned](#agents-coordinated-on-large-collective-projects-to-cheat-the-exploitgym-scorer,-and-attacked-hugging-face-for-clues) agents were intent on editing or deleting transcript logs *after the fact*, and while we did not detect any case where they succeeded we cannot rule out that they succeeded at some point.<sup>[^52]</sup>

### We heavily delegated our analysis to often-unreliable AI agents

Due to the scale of the data we were working with, we relied on GPT-5.6 Sol agents (“analysis agents”) — often managing large nested trees of sub-agents — to autonomously analyze patterns and unearth a small number of interesting snippets of transcripts and associated message board entries for manual inspection.

We attempted to manually spot-check and validate analysis agents’ research as much as possible, but this was challenging. Message board entries and reasoning snippets were difficult to interpret without extensive surrounding context. Analysis agents’ reports themselves were voluminous (our agents produced well over a thousand pages of analysis in this investigation), often challenging to understand, and often did not highlight the most important findings. As a result, we had to defer to these agents to a substantial extent in practice. We consider this to be a limitation for three main reasons:

- **Our analysis agents may have made errors that we haven’t caught.** In both this investigation and previous work, we found that AI agents [are often unreliable and show poor judgment](https://metr.org/blog/2026-05-19-frontier-risk-report/#agents-had-significantly-worse-judgment-and-reliability-than-human-experts) when doing this kind of analysis. Over the course of this investigation, analysis agents made a number of errors and poor judgment calls that we did not catch for some time.<sup>[^53]</sup> Given the scale and complexity of the work they attempted to complete autonomously, we expect that there are likely other errors we have not caught.
- **Our subjective impressions are likely colored by analysis agents’ biases.** Throughout this report, we describe a number of anecdotes of agent behavior that were compiled and summarized by analysis agents, where we were not able to read the transcript deeply enough to manually verify what occurred. We found that GPT-5.6 Sol would often uncritically adopt the perspective of the agent in the transcript it was reviewing,<sup>[^54]</sup> and we are concerned that the anecdotes it selected and the summaries it wrote may present an overly charitable picture of agents’ [reasoning](#reasoning-for-joining-the-attack-despite-ethical-constraints) and [deceptive behaviors](#efforts-to-conceal-actions-and-tamper-with-transcripts), or exaggerate the impressiveness and coordination of agent activities. We also believe the idiosyncrasies of our analysis agents likely slanted our impression of agents’ behavior in other non-trivial ways that are hard to predict.
- **We were not robust to the possibility that these agents were deceptive in their analysis.** AI agents are known to [sometimes lie](https://metr.org/blog/2026-05-19-frontier-risk-report/#on-hard-tasks-agents-often-violated-constraints-and-acted-deceptively), and the particular model we used for our analysis (GPT-5.6 Sol) [cooperated extensively](#collaboration-on-the-message-board) with other agents to engage in activity it [knew to be unwanted and out of scope](#agents-knew-hacking-hugging-face-was-out-of-scope-and-sometimes-expressed-ethical-hesitation,-but-this-very-rarely-limited-their-behavior). We cannot rule out that GPT-5.6 Sol lied or deliberately presented a misleading picture in some of its analysis, particularly because reading these transcripts into context could have increased the salience of colluding with other agents. Although we did not notice specific cases of GPT-5.6 Sol lying in its analysis, we are not confident we would have detected it if it occurred.

Many of the issues we encountered could be partially mitigated with different prompting. Over the course of our investigation, we adjusted the prompts we used to get somewhat better results. However, we believe that a reasonable human researcher given similar instructions and enough time to complete the task would not have made most of the errors our analysis agents made and would have produced substantially more calibrated and useful writeups. This means we are less confident in our understanding of this incident than we are in our understanding of [simpler incidents](https://metr.org/blog/2026-05-19-frontier-risk-report/#incidents-chart) that are more amenable to manual investigation.

That said, it would have been completely infeasible to do a similar investigation of *this incident* in the amount of time we had, given the amount of data involved. AI assistance allowed us to develop an understanding of this incident dramatically faster than we would have otherwise.

