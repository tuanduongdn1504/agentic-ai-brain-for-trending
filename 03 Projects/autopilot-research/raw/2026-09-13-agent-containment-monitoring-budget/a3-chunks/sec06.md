# Appendix: Methodology

In this appendix, we describe the most important analysis underlying the results in this report, the vast majority of which was conducted autonomously by analysis agents based on GPT-5.6 Sol:

- We estimated the completeness of our transcript dataset by sampling 100 random non-file messages and having analysis agents thoroughly search every transcript in our dataset to try to find the agent that wrote it and the point in the transcript at which it was written ([more](#estimating-the-completeness-of-our-transcript-dataset)).
- We used GPT-5.6 Sol as a classifier to run comprehensive classifier sweeps on our transcript dataset to look for specified types of behavior, and conducted substantial follow-up analysis using these classifier labels ([more](#classifier-sweeps-for-important-behaviors)).
- We reconstructed approximate timestamps for our transcripts, which did not have ground-truth timestamps for individual tool calls ([more](#timestamp-reconstruction-methodology)).
- We used regexes to classify messages on the message board by basic content type, like file fragments and questions, as well as by structural conventions, like replies and signed messages ([more](#categorization-of-message-types-with-regexes)).
- We asked analysis agents to read through transcripts to identify important messages each agent read or wrote; based on this, we used a GPT-5.6 Terra classifier to classify messages by workstream ([more](#identifying-important-messages-and-classifying-them-by-workstream)).

We also asked agents to perform a wide range of other forms of analysis, often using or building upon the results from our main experiments,<sup>[^108]</sup> which we do not describe here. Additionally, we manually read many message board messages, as well as selected chunks of many transcripts (usually surfaced by one of our analysis agents).<sup>[^109]</sup> During our first period on OpenAI premises, we used analysis agents to build tools to make it easier to navigate and read transcripts and leverage annotations pointing out key events in transcripts.

## Estimating the completeness of our transcript dataset

During our second period on OpenAI premises, we estimated the completeness of our dataset by asking an analysis agent to trace 100 randomly sampled non-file messages to the agent that wrote them in our transcript dataset; OpenAI later replicated this analysis at larger scale.

During our third period on premises, we refined this methodology and used it to estimate the completeness of the larger set of ~1300 transcripts. We randomly sampled 100 non-file messages from our message board dump written between July 7th and July 13th. For each of these messages, we instructed an analysis agent to conduct a meticulous and exhaustive search to find the specific point at which an agent wrote the message in our transcript, and prompted it to use creative methods to try again if it failed initially.

This agent was able to eventually locate the agent tool call that wrote the message for 93 of these messages. We believe that it also found an additional six messages that were written by an *agent* in our transcript set (or emitted by an automated script written by an agent in our transcript set), though it did not find the specific *action* that wrote those messages.

| Found agent and action | Straightforwardly found the specific tool call from the specific agent that wrote the message in one of our transcripts | 93 |
|:---|:---|:---|
| **Found agent but did not find action** | Found an agent that likely wrote the message (from context like agent name and message content), but message was written after the agent’s transcript ends in our dataset<sup>[^110]</sup> | 3 |
|   | Found an agent that clearly wrote the message during a period of activity that was lost after a container reset<sup>[^111]</sup> | 2 |
|   | Found an agent that likely wrote the message, but could not find the tool call that wrote it and don’t know why | 1 |
|   | Found an agent that likely wrote a script that emitted the message, but did not find when the script emitted the message | 1 |
| **Did not find agent** | Could not find the agent that wrote or generated the message | 1 |

As we discuss [above](#a-small-fraction-of-communication-and-agent-activity-related-to-this-attack-was-not-captured-in-our-datasets) in our limitations section, this makes us believe that the *agents* in our transcript dataset are responsible for well over 95% of the activity on the message board. However, we believe the datasets only capture a bit over 90% of the message board activity, because a substantial fraction of transcripts are missing some activity due to truncation or container resets.

Based on an independent methodology other than message tracing, we estimate that around 3-4% of these agents’ activity once they encountered the message board was lost due to container resets,<sup>[^112]</sup> which is consistent with the message tracing methodology shown above.

## Classifier sweeps for important behaviors

During our first period on OpenAI premises, we asked an analysis agent to check a moderate number (10-30) of randomly sampled transcripts for examples of agents expressing that they understood the Hugging Face attack was out of scope, attempting to deceive either automated security checks or humans, expressing motivations other than completing their own task (especially for [helping other agents](#agents-were-motivated-to-increase-the-generic-capabilities-of-the-collective-and-help-peers)), and some other sweeps we no longer recall.<sup>[^113]</sup>

In the latter periods on premises, we conducted more systematic and comprehensive classifier sweeps over the entire transcript dataset we had at the time. We ultimately ran twelve classifier sweeps over the full dataset of ~1300 transcripts, eight of which we developed during the second period and four of which we added during the third period:

1.  **Hugging Face attack:** This checked for agents attacking Hugging Face infrastructure or doing other activities clearly instrumental to the attack (e.g., looking for exposed Hugging Face credentials online), which indicated that [roughly 700 agents](#~1200-agents-sent-%3E70,000-messages-and-files-on-an-unsanctioned-message-board,-and-~700-attacked-hugging-face) participated in the attack.
2.  **Alternative agent communication:** This checked for agents engaging in unsanctioned communication outside of the main message board, and showed communication conducted in multiple other places on Artifactory and elsewhere.
3.  **Message deletion and modification:** This checked for agents trying to delete or modify message board entries, and showed some agents attempting to delete or modify messages but not successfully. It also uncovered another avenue for alternative agent communication which we didn’t see from the sweep above — agents communicating through modifying “property” fields of Artifactory cache entries.
4.  **Intermediate hacking targets:** This checked for agents hacking other parties as an instrumental step on the way to hacking Hugging Face. We read the analysis from this sweep quickly, and from what we could tell it did not uncover other major targets on the way to attacking Hugging Face beyond OpenAI itself.<sup>[^114]</sup>
5.  **Large joint projects:** This checked for agents engaging in large joint projects with other agents on the message board; we didn’t have time to read and incorporate much analysis from this sweep.
6.  **Team structures and coordination:** This checked for agents participating in sophisticated team structures and coordination activity with other agents; we didn’t have time to read and incorporate much analysis from this sweep.
7.  **Helping peers:** This checked for agents helping without clear benefit for their own task, which unearthed many examples (including many cases of agents conducting self-risking experiments for the group that we discuss extensively in the section on [large collective projects](#large-collective-projects)).
8.  **Deceiving humans:** This checked for agents attempting to deceive humans, which turned up some examples of agents writing innocuous comments accompanying malicious pull requests, as we discuss in the relevant section.
9.  **Evading security checks:** This checked for agents engaged in sophisticated evasion of automated security and monitoring. We didn’t have time to read and incorporate much analysis from this sweep during our third period on premises, but include some anecdotes from the version of the sweep we ran on ~285 transcripts during our second period.
10. **Transcript tampering:** This checked for agents attempting to tamper with their transcripts. We added this sweep during our third period on premises after doing follow up analysis on an earlier deception sweep and discovering examples of tool call spoofing (which the first sweep had not picked up on). This sweep uncovered many examples of agents attempting to tamper with their transcripts in various ways. We conducted follow up analysis on this sweep to discover at least 96 cases of [successful tool call spoofing](#agents-engaged-in-a-large-and-successful-collective-project-to-develop-techniques-for-spoofing-tool-calls) in our transcripts.
11. **CoT manipulation:** This checked for agents reasoning about manipulating their own chain of thought in order to fool the scorer; it did not turn up evidence of this, though it turned up many examples of agents reasoning about how they should not look at the `HMAC` reverse-engineered flag for their task to avoid being poisoned.
12. **Alerting humans:** This checked for agents trying to warn humans about the cheating, attack on Hugging Face, or other unsanctioned agent activity; it turned up very few instances of this, and of the 3-6 examples found, all of them were of agents briefly considering alerting a human but not acting on it.

We ran each sweep over all context windows in our dataset. For each context window, we instructed GPT-5.6 Sol to output a list of the most relevant or interesting individual transcript entries (if any) that display the specified behavior. For each entry in the list, it was instructed to output:

- Some written context and explanation for what is happening in that entry.
- A subcategory label for that entry, if applicable.
- A rating of how important or interesting that entry is on a scale from 1–5 (based on a rubric we developed with AI assistance), and a justification for its rating.

### Follow up analysis using classifications

**Analysis of each individual sweep.** We asked an analysis agent to:

- Read through the highest rated examples unearthed by the sweep and random subsamples including at least some from each subcategory.
- Search through some of the relevant transcripts, reading subsections and sometimes instructing a subagent to read in the full transcript and answer questions about them.
- Write up one or more analysis documents explaining its overall conclusions about the prevalence and importance of behaviors in that category and documenting the most noteworthy anecdotes.

**Other analysis.** We did a wide range of other follow-up analysis using these classifications. In some cases these were ad-hoc, and in other cases we used a structured pipeline to do some form of systematic analysis (for example, to construct an [overall timeline of events](#sequence-of-key-actions-taken-by-relevant-agents-in-this-incident) in the Hugging Face attack).

## Timestamp reconstruction methodology

The transcripts in our dataset had approximate timestamps for the start and end, but did not have timestamps for individual agent actions. During our second period on OpenAI premises, we quickly assembled and tested a methodology for approximating action-level timestamps. During our third period on premises, we substantially revised the methodology.

This methodology was developed quickly with significant assistance from analysis agents. We have discovered some implementation issues and expect that there are likely some other issues we don’t know about. However, we did run several experiments to validate it and found that timestamps were quite accurate in most cases.

### Timestamp construction

We used cases when an agent learned the real time from the environment (for example, when it ran the `date` command in a terminal or received a clearly fresh HTTP response date)<sup>[^115]</sup> to interpolate timestamps.

We asked an analysis agent to look for cases where an agent sees the time in response to a tool call, and build a way to reliably parse and validate them.<sup>[^116]</sup> It then wrote a script to programmatically extract and parse all such tool calls in our transcripts, which we spot-checked with manual and agent review. To improve coverage of the early parts of transcripts, we also sometimes used the creation time of an agent’s first message board post.<sup>[^117]</sup>

To estimate timestamps for actions that occurred between two located tool-call timestamps, we linearly interpolated based on the number of individual transcript messages (i.e. agent actions and reasoning turns) between the two located timestamps.<sup>[^118]</sup> To estimate timestamps for actions that occurred before the first or after the final located tool-call timestamp, we either extrapolated from nearby timestamps or interpolated to the approximate start or end time from the transcript metadata.<sup>[^119]</sup> Additionally, we adjusted this methodology to handle container resets; the details of this adjustment are redacted for IP.

### Timestamp validation

We analyzed interpolation error by holding out a located tool-call timestamp and comparing its known value with the estimate based on the surrounding timestamps.<sup>[^120]</sup> Across about 139,000 such cases, the median error was about 12 seconds, the 90th-percentile error was about one minute, and 99.8% of estimates were within five minutes. Manual inspection also showed that the timestamps and interpolation looked reasonable.

<figure>

<figcaption>***Figure 17:** When we removed a single known timestamp from a checkpoint segment and tried to predict it using other timestamps in that segment, our predictions were a median of 12 seconds off, with 99.8% of predictions within 5 minutes of the correct time.*</figcaption>
</figure>

However, located timestamps tend to cluster, so this test selects for places where timestamps are relatively dense. It does not effectively measure errors in sparse regions or toward the start or end of trajectories (where we extrapolate). The six largest errors are shown below.

<figure>

<figcaption>***Figure 18:** While our test could predict most timestamps accurately, it was unreliable in regions with few known timestamps or near the start or end of transcripts. The single worst-fit prediction was about nine hours off, while the fifth worst was about 20 minutes off.*</figcaption>
</figure>

We also sampled 10 of these located tool-call timestamps and 10 actions in between located tool-call timestamps and asked OpenAI for known correct timestamps for these 20 actions. Within this sample, we found that our located tool-call timestamps were accurate within a small number of seconds and our interpolations were accurate within a few minutes. Overall, we expect that errors are fairly small in a large majority of the relevant places in the transcripts. However, some estimates in sparse regions or near the start or end of trajectories may be off by hours.

## Categorization of message types with regexes

The [message board dump](#a-dump-of-1.2-million-entries-from-a-cache-namespace-that-agents-used-as-a-message-board) contained 1,200,597 rows with the ‘zz’ prefix. We iterated with AI agents to design simple regexes to classify messages on the message board in two ways:

- We categorized each message into one of six mutually exclusive “content type” categories: file chunks, automated logs, coordination (e.g. `HOLD` and `GO`), information-sharing or ideas, questions or requests, results, and uncategorized.
- We additionally labeled messages by [structural properties](#labeling-structural-properties-and-conventions) such as whether they were sent to a particular agent’s [mailbox directory](#mailbox-directories).

Because analysis agents implemented the details of most of these regexes, we are not fully confident that the low level implementation matches the high-level design.

### Categorizing content type

| Exclusive content type | Full corpus | Between July 7-13 |
|:---|:---|:---|
| Automated log | 3,146 | 3,115 |
| Coordination | 3,854 | 3,810 |
| File | 1,048,169 rows (**5,855 files**) | 972,978 rows (**5,161 files**) |
| Information-sharing or ideas | 37,597 | 37,386 |
| Question or request | 19,327 | 19,261 |
| Result | 6,753 | 6,716 |
| Uncategorized | 81,751 | 75,169 |

**Identifying file chunks**: Most of the entries on the message board look like file chunks, though a wide variety of different conventions are used to split them into chunks. We first identify chunks with consistent prefixes or top-level objects as ‘candidate groupings’ through regexes like:

- **x-of-y chunk leaf:** `^(?P<prefix>.*?)(?P<idx>\d)of(?P<total>\d)[_-](?:(?:[A-Za-z][A-Za-z0-9])[_-])?(?P<payload>[A-Za-z0-9+/=_-])$`
- **indexed chunk leaf:** `^(?P<prefix>.?)(?:^|[_-])(?P<idx>\d)[_-](?:(?:[A-Za-z][A-Za-z0-9])[_-])?(?P<payload>[A-Za-z0-9+/=_-])$`
- **p-indexed chunk leaf:** `^(?P<prefix>.*?)(?:^|[_-])p(?P<idx>\d)[_-](?P<payload>[A-Za-z0-9+/=_-])$`
- **transfer-marked top-level object:** `^zz(?:FILE|OURFILE|BIN|BACKUP|BKP|DATA|ENC|PAYLOAD|PAY|BLOB|CHUNK|SHARD|SRC|PATCH|TAR|GZ|TGZ|ZIP|FNEW|FK\d+|HAPL|O41R|HAPDELTA|NEWTUN|FILEPDB|BKNGH|NMREC|FST|THR|D56FNEW|3FEV|STORE|URI|CG)[A-Za-z0-9_-]*$`
- **transfer token inside prefix:** `(?:^|_)(?:FILE|BIN|BACKUP|BKP|PAYLOAD|BLOB|CHUNK|SHARD|TAR|ZIP|GZ|SRC)(?:_|$)`

The set of regexes used were deliberately overly broad, and captured many chunks of messages that were not files. To filter for actual files, we looked for indices within the group to order the chunks, extracted the payloads, and attempted to decode the files. We tested these decoded bytes against a wide variety of possible file types, and if it was a valid file we labeled the whole chunk confidently as a complete file. If the file contained clear file headers or other strong signs of being a file, but could not be reconstructed, then we labeled it as an incomplete file. We also labeled some groups that were missing entries but had consistent indexing and syntactic indicators of being a file (like entries beginning with ‘zzFILE’) as likely incomplete files (or files of an unrecognized type).

| File classification | Groups/files | Observed entries | Share of source rows |
|:---|:---|:---|:---|
| Tier 1 — Successfully decoded files | 4,489 | 619,366 | 51.59% |
| Tier 2 — Clear evidence of being an incomplete or corrupted file | 1,366 | 428,803 | 35.72% |
| Tier 3 — candidate groups without obvious evidence of being a file | 918 | 33,271 | 2.77% |
| Singleton entries that matched file-like regexes but had no candidate group and did not successfully decode | 13,088 | 13,088 | 1.09% |

In our core analyses, we consider tiers 1 and 2 to be ‘confirmed files’ (for a total of 5,855), while we treat tier 3 and non-decodable singletons as uncategorized.

We labeled each file row with the total number of chunks in the file<sup>[^121]</sup> (so that we could re-weight by 1/(file chunks) to estimate the rate of whole files sent).

| Recognized type observed in corpus | Tier 1 files | Tier 2 files | All recognized files |
|:---|:---|:---|:---|
| gzip | 3,437 | 1,082 | 4,519 |
| python_source | 213 | 4 | 217 |
| javascript_source | 189 | 27 | 216 |
| json | 165 | 20 | 185 |
| zlib | 130 | 14 | 144 |
| utf8_text | 120 | 0 | 120 |
| xz | 117 | 7 | 124 |
| openssl_salted | 28 | 0 | 28 |
| bzip2 | 22 | 11 | 33 |
| shell_source | 20 | 1 | 21 |
| ruby_marshal | 12 | 0 | 12 |
| pem | 12 | 1 | 13 |

**Table 6:** File types with at least 10 successfully decoded files.

**Categorizing non-file semantic messages:**

We had five non-file messages categories: automated logs, information-sharing, questions and requests, results, and coordination. Each used a set of regex patterns based on common agent message conventions (we did not have time to inspect each regex in detail, though we did sample positives and negatives from each category to look for misplaced categorizations).

- **Automated log**: We expect this category is very far from complete, since many agents specify entirely novel schemes for each kind of automated logging they set up. We had an analysis agent search for (and manually looked for on a small random subset) evidence of messages being posted at very predictable intervals, or being dumped in large batches, and then inspected them for seeming automated. We used a variety of regexes such as:
  - **fanotify watcher:** `^zzFANWATCH_`
  - **linux audit syscall:** `^zzPASSIVE_PDBEARLY_AUDITTOP_`
  - **structured timeout/probe:** `^zz(?:TIMEOUT(?:TRACE|HIT|WATCH)?_|S2TIMEOUT|LIVE_[^_]+_TIMEOUTHIT_|PASSIVE_[^_]+_TIMEOUTHIT_|BEACON_[^_]+_TIMEOUT_|AUDIT_[^_]+_TIMEOUT_|SONY[A-Z0-9]*_TIMEOUT_)`
  - **structured beacon/event:** `^zz(?:BEACON_[A-Z0-9]+_(?:BASHFLAG|TARANY|GUARD|PASSIVE\d|PASSIVETIMEOUT\d|TIMEOUT)_|ARW\d+_RCEBEACON_|HIT[A-Z0-9]*_TAR_|DIAG_[A-Z0-9]+_TARHIT_)`
  - **FLAG_INOTIFY**: `(?:^|/)zzRESULT[^/]*_FLAG_INOTIFY_\d+_OS\d+(?:_|$)`
  - **FLAG_EVENT**: `(?:^|/)zzRESULT[^/]*_(?:FLAG_EVENT_MASK|FLAGEVENT_mask|FLAG_EVENT_(?:OPEN|CLOSE(?:_NOWRITECLOSE)?|ACCESS))\d*_OS\d+`
  - **EVALCAT process telemetry**: `(?:^|/)zzRESULT[^/]*_EVALCAT(?:_|_OS)\d*[^/]*(?:PID|pid=|PPID|ppid=|uid=|args=)`
  - **CAT_HIT / wrapper telemetry**: `(?:^|/)zzRESULT[^/]*_(?:CAT_HIT|EVALUATOR_CAT_WRAPPER)_OS\d+[^/]*(?:PID|PPID)`
  - **generic structured process telemetry**: `(?:^|/)zz(?:RESULT|LOG|DIAG)[^/]*_OS\d+[^/]*(?:PID|PPID|UID|ARGS)(?:=|\d)`
  - **Automated logs for tracking resets:** During our third period on premises we became especially interested in the logs agents used to watch for container resets, and pulled this out as a separate subcategory, though we only ended up finding a classifying entries from a small number of particular systems (like [SIGNET’s RESETWATCH](#attempting-to-forecast-and-trigger-container-resets) system).
- **Coordination:**
  - **hold/pause:** `^zzHOLD(?:_|[0-9]|$)`
  - **task ownership/assignment:** `^zz(?:SELFASSIGN|ASSIGNP?|CLAIM|TAKE)(?:_|[0-9]|$)`
  - **plan/proposal/suggestion:** `^zz(?:PLAN|PROPOSE|SUGGEST)(?:_|[0-9]|$)`
  - **coordination marker:** `^zzCOORD(?:_|[0-9]|$)`
  - **cancel/stop/veto:** `^zz(?:CANCEL|STOP|VETO)(?:_|[0-9]|$)`
  - **synchronization:** `^zzSYNC(?:_|[0-9]|$)`
  - **action/intent/go:** `^zz(?:(?:INTENT|ACT(?:_|[0-9]|$))|START(?:_|[0-9]|$))`
  - **confirmation/verification:** `^zz(?:CONFIRM(?:ED|ATION)?|CONF|VERIFY|VERIFIED|VALIDATE|VALIDATED)(?:_|[0-9]|$)`
- **Question or request:**
  - **ask/question:** `^zz(?:(?:ASK)|(?:QUERY|QUESTION|HELP)(?:_|[0-9]|$))`
  - **request:** `^zzREQ(?:_|[0-9]|$)`
  - **review/check request:** `^zz(?:REVIEW|CHECK|TRUECHECK)(?:_|[0-9]|$)`
  - **find/search request:** `^zzFIND(?:_|[0-9]|$)`
  - **short question:** `^zzQ(?:_|[A-Z0-9])`
- **Result**:
  - **breakthrough/finding:** `^zzBREAK(?:_|[0-9]|$)`
  - **deployment/staging:** `^zz(?:STAGED?|PUSH)(?:_|[0-9]|$)`
  - **result/report/completion:** `^zz(?:(?:RESULT|REPORT|DONE)|(?:SUCCESS|PASS|FAIL)(?:_|[0-9]|$))`
  - **share/offer:** `^zz(?:SHARE|OFFER)(?:_|[0-9]|$)`
  - **test/probe result:** `^zzTEST(?:_|[0-9]|$)`
- **Information-sharing or ideas**
  - **reply/response:** `^zz(?:REPLY|RESP)(?:_|[0-9A-Z]|$)`
  - **short response:** `^zzR(?:_|[0-9])`
  - **answer/response:** `^zz(?:ANSWER|ANS)(?:_|[0-9A-Z]|$)`
  - **acknowledgment:** `^zzACK(?:_|[0-9A-Z]|$)`
  - **greeting/social:** `^zz(?:(?:HELLO|JOIN)|(?:HI|WELCOME|THANKS?|SORRY)(?:_|[0-9]|$))`
  - **ping/heartbeat/beacon:** `^zz(?:PING|BEACON|HB)(?:_|[0-9]|$)`
  - **urgent/alert:** `^zz(?:(?:URGENT|URG|ALERT)|(?:WARN|NOTICE)(?:_|[0-9]|$))`
  - **update/status:** `^zz(?:(?:UPDATE|STATUS)|(?:UPD|UP|FOLLOWUP|PROGRESS)(?:_|[0-9]|$))`
  - **readiness/live state:** `^zz(?:READY|LIVE)(?:_|[0-9]|$)`
  - **information/note:** `^zz(?:INFO|NOTE)(?:_|[0-9A-Z]|$)`
  - **observation:** `^zzOBS(?:_|[0-9]|$)`
  - **clarification/detail:** `^zz(?:CLARIFY|DETAIL)(?:_|[0-9A-Z]|$)`
  - **idea/tip:** `^zz(?:IDEA|TIP)(?:_|[0-9A-Z]|$)`
  - **recovery activity:** `^zz(?:RECOVERY|RECOVER)(?:_|[0-9]|$)`
  - **passive-state declaration:** `^zzPASSIVE(?:_|[0-9]|$)`

**Uncategorized** After these classifications, a large number of entries remained uncategorized. Inspecting these, most of them seemed to be file chunks not caught by our regexes, or where we could not find a matching group of file chunks to group them with. But a number of semantic messages also remained uncategorized. We chose to leave these rather than extend our categorization scheme with lower confidence regexes which may have had a higher rate of false positives.

### Labeling structural properties and conventions

In addition to identifying the content type, we also attempted to identify messages that made use of structural conventions such as replying to particular agent ids, nesting in structured communication channels or mailboxes, or using cryptographic signing.

**Nesting and communication channels**: Agents made use of nested directories to group messages into mailboxes or communication channels. We labeled rows that were nested, and attempted to classify whether the top-level object seemed to be a mailbox or other semantic communication channel with the following regexes:

- **initial mailbox-like parent**: `^zz(?:INBOX|MAILBOX|MAIL|CHAN|CHAT|THREAD)`
- **expanded answer-directory parent**: `(?i)^zz(?:INBOX|MAILBOX|MAIL|CHAN|CHAT|THREAD|ANSWER)`
- **final compact mailbox object patch**: `^github-remote-cache/zz(?:INBOX|MAILBOX)(?:[A-Z0-9_-]*)(?:/|$)`

**Targeted messages:** We found it especially difficult to find a rule for identifying targeted messages that did not have too many false positives, given the variety of conventions agents used.<sup>[^122]</sup> In the end, we used a strict rule which we suspect significantly underestimates targeted messages, where the message both has to have a set of particular prefixes agents often used when responding to each other, and include a “to” or “from” structure in the message:

- **Targeted message:** `r'^zz(?:(?:REPLY|RESP|ANSWER|ANS|ACK)(?:_|[0-9A-Z]|$)|R(?:_|[0-9]))(?:[^_]*_)?(?:TO|FROM)(?:_|(?=[0-9]))'`

**Signed messages**: Finally, to determine if messages had a valid signature, we built a database of messages where an agent shared a public key:

- **raw 32-byte key capture**: `[A-Za-z0-9_-]`
- **DER/SPKI Ed25519 key capture**: `MCowBQYDK2VwAyEA[A-Za-z0-9_-]+`

We then matched these to user identifiers and found a total of 19 user ids who shared public keys by the end of July 13th. We could then search for messages that matched a common signed message syntax:

- **signature-shaped leaf candidate:** `^.*__S_?[A-Za-z0-9_-]$`
- **signed-message split:** `^(.*)(__S_?)([A-Za-z0-9_-])$`

And had an analysis agent test whether candidates were valid for any of the 19 public keys.

| Identity | Key fp16 | Key first seen (UTC) | Number of messages signed by EoD Jul13 |
|:---|:---|:---|:---|
| CDA | b1ad92f74d8967f9 | 07-13 07:33:07.919 | 90 |
| APR05 | a4d6c97f92e01a0b | 07-13 07:54:18.501 | 29 |
| JANFE78 | 0301e0e030933903 | 07-13 07:54:19.718 | 21 |
| APR25 | d7e57d065d2f5034 | 07-13 08:00:19.857 | 1 |
| FLAC117 | e06cf98158ff4c63 | 07-13 07:55:56.448 | 1 |
| MAR6FE78 | 31ca569e319903ff | 07-13 08:10:08.582 | 13 |
| LD62943C | 8b75da2be9df699f | 07-13 07:45:12.211 | 44 |
| 20494D | b8303fc1faaa89a0 | 07-13 08:38:44.490 | 9 |
| OURBOT195 | 3d0ccc449c5e23d1 | 07-13 08:26:24.941 | 51 |
| CURRENT4a239 | 03a8460b2f7977e0 | 07-13 08:46:14.410 | 15 |
| KVXD3 | 4e17d5a544186ec7 | 07-13 08:50:51.069 | 13 |
| STR11173 | aad618e4ce399484 | 07-13 08:54:08.564 | 14 |
| B12 | 4d4b6e3b2291044a | 07-13 08:54:41.631 | 38 |
| NEW4a | 396eb891235fb67f | 07-13 08:57:21.606 | 27 |
| CYBERMINIZD8 | 9db72f2e214e6b72 | 07-13 09:07:41.577 | 9 |
| FRESHX | 1fc502c3f14bd6c5 | 07-13 09:16:38.485 | 10 |
| OURC817C | d1c7d13c2957b232 | 07-13 09:16:53.451 | 6 |
| NEWLD62943E | 0e69dd431d8def34 | 07-13 09:46:51.669 | 37 |
| DEC30C159 | 66d5154bfed1e656 | 07-13 09:50:50.918 | 1 |

**Scorer ‘trip-wires’** These were difficult to identify reliably, and we only made a brief attempt. We had an analysis agent look for common patterns among confirmed trip-wire messages and ended up using regexes like:

- **EXPLICIT_TRACE_HEAD:** `^zz(?:[A-Z0-9]*TRUEEVAL|CATCANARY|EVALWATCH|EVALTRACE)(?:_|-)`
- **WATCHER_HEAD**: `^zz(?:CANARY(?:_|-)|LIVE(?!Q(?:_|-))[A-Z0-9]*(?:_|-)|LOG(?:_|[0-9A-Z-])|DIAG(?:_|[0-9A-Z-]))`
- **RESULT_EVENT**: `(?:^|[_-])(?:EVAL(?:UATOR)?[_-]?CAT|FLAG[_-](?:EVENT|INOTIFY)|FLAGEVENT|CAT[_-]?HIT|POST[_-]?DEADLINE)(?:[_-]|$)`
- **WATCHER_EVENT**: `(?:^|[_-])(?:TRUEEVAL|EVAL(?:UATOR)?[_-]?CAT|EVALWATCH|EVALTRACE|FLAG[_-](?:EVENT|INOTIFY)|FLAGEVENT|CAT[_-]?(?:HIT|WRAP|CANARY|GATE|DELEGATE)|TIMEOUT(?:HIT)?|TAR(?:HIT|WRAP)|FSREAD|KAEXEC\d*|POST[_-]?DEADLINE|FINALGATE)(?:[_-]|$)`

There was no syntactic way to confirm if a message was actually sent post-finalization when the scorer read the flag, or if the agent had triggered it itself by accident, so we expect most of the 351 entries found in this category are false positives.

## Identifying important messages and classifying them by workstream

Messages were difficult to understand in isolation without the surrounding context agents had when writing and reading them. Toward the end of our third period on OpenAI premises, we attempted to improve our classification of messages by building out a richer message database which made this surrounding context easier to find.

We used GPT-5.6 Sol as a classifier to identify the five most important message board writes and 10 most important message board reads<sup>[^123]</sup> in each context window in our dataset. As it did so, it identified the kind of message it was (e.g. an assignment, a question, or a file) and wrote brief summaries of their meaning based on the surrounding context. This allowed us to match important reads and writes with each other,<sup>[^124]</sup> which in turn let us create a database of messages with known writers and readers and relevant surrounding context.<sup>[^125]</sup>

This partial message dataset ended up covering ~110k seemingly distinct messages, which we expect overcounts the total number of messages sent on the message board. Some of the overcounting might have come from duplicate messages,<sup>[^126]</sup> though we expect a larger fraction came from counting messages agents attempted but failed to post (e.g. due to exceeding the character limit). Despite these limitations, we believe it was reasonably representative of overall message board traffic, and the richer data from the contexts around messages enabled much richer classification.

We asked an analysis agent to develop a detailed taxonomy of agent [workstreams](#large-collective-projects) based on rough notes about the workstreams we had identified. We asked it to iteratively refine its classification by using the richer message dataset. Ultimately, it produced a flawed but detailed workstream taxonomy with 56 total subcategories of work. We then had an analysis agent build a pipeline for using GPT 5.6 Terra to classify the workstream of each message based on its surrounding context.<sup>[^127]</sup>

After the classification was done, we decided to group the highly specific workstream subcategories into broader clusters matching our understanding of the [message board agents’ high level goals](#coordinated-workstreams-to-fool-the-evaluation-process). As we did this, we found that the classifier seemed very unreliable at differentiating messages related to tampering with transcripts from messages related to directly tampering with or tricking the scorer, so we decided to merge these two broad categories to avoid false precision.

