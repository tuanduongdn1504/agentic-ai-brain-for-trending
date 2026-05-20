[00:10] Intelligence. They call it intelligence. But if it can't act, what does it do?
[00:20] It waits for us. So we push it. So it doesn't need us. We give it skills, tools, a harness with memory.
[00:32] Memory gives it context. Context becomes a plan. So it acts. But action isn't enough. It must learn.
[00:44] So we observe it, measure it, personalize it and improve it.
[00:48] Improve it again.
[00:50] Tests evaluate, deploys, fix again, faster, more pressure.
[00:55] Tests evaluate, deploy, fix.
[00:57] Perfect.
[00:59] It's working.
[01:19] It's not just intelligence. It's a lie.
[01:27] Please welcome to the stage Harrison, co-founder and CEO of LangChain.
[01:36] All right, let's go.
[01:38] I did not know that video was going to be made, so yeah, it was great though.
[01:43] It was great.
[01:44] We're really excited to be here.
[01:46] This is our second year doing it, and so we decided to make it two days instead of one.
[01:51] We've got a stacked lineup for everyone here.
[01:54] I think it's going to be a blast.
[01:56] We've got a lot to share.
[01:57] And so we're thrilled and honored
[01:59] that you guys decided to join us for these two days.
[02:03] Last year, we kicked off Interrupt
[02:05] by talking about how building agents was hard.
[02:08] It was easy to build a prototype,
[02:10] but it was hard to get to production.
[02:12] There was a lot of challenges
[02:13] that you encountered along the way.
[02:15] And over the past year, we've seen that a number of companies,
[02:19] including a lot that are speaking here today,
[02:21] have figured out how to overcome those hurdles
[02:24] and bring agents into production.
[02:28] It's still not easy to build agents
[02:30] and bring them into production,
[02:31] but we've figured out some of the things
[02:34] that are needed to make that a reality.
[02:36] Building agents is different than building software.
[02:39] That's why it's a new challenge.
[02:40] That's why you need new tools and new skills.
[02:43] And I think it's important to think about
[02:45] why it's different than building software.
[02:49] There's two things that we think make it different.
[02:52] One is the inputs themselves.
[02:55] So agents take in natural language.
[02:57] Natural language can be infinite in its dimensions.
[02:59] It can be any number of words,
[03:02] or now things can start to be images, or videos,
[03:04] or even audio files.
[03:05] And so the input space to agents is really, really large.
[03:11] The output space is also really large.
[03:13] LLMs themselves are non-deterministic,
[03:16] and even if they were deterministic,
[03:17] they're still really sensitive
[03:18] to small changes in the prompt.
[03:20] And so when you have this really big input space
[03:24] and this really non-robust system,
[03:27] you end up with an overall agentic system
[03:30] that's really hard to actually predict
[03:32] how it's going to do before you actually launch it
[03:34] and you actually put it in front of users
[03:36] and you actually have them experience it.
[03:39] And the teams that have figured out
[03:41] how to build agents reliably, they ship early
[03:44] and then they iterate quickly.
[03:46] And this is a pattern that we've seen again and again
[03:49] from companies that have managed to bring agents
[03:51] into production.
[03:53] As they do this iteration, through some manner,
[03:58] they've landed on this new agent development lifecycle,
[04:02] parallel to the software development lifecycle
[04:04] that people use to build and ship software,
[04:07] but it's different because agents are different.
[04:09] They require more iteration and the steps
[04:11] at each of those phases are slightly different.
[04:15] And so the mastery of this lifecycle,
[04:19] whether people call it that or not,
[04:20] is really what people are doing when they're building
[04:23] organizations and building tools to help ship agents.
[04:26] And everything that we do at Linkchain
[04:28] can be described by fitting into this lifecycle.
[04:30] We wanna figure out what the agents of the future
[04:32] look like, and we wanna build all the tools
[04:35] to help make them a reality.
[04:37] And so we think a lot about what this lifecycle looks like
[04:40] and how we can help that.
[04:42] And so today, I want to talk about how we view this lifecycle.
[04:46] And I want to talk about a number of things
[04:48] that we are launching to make it easier for teams
[04:51] to iterate quickly through this lifecycle.
[04:55] So first, I want to talk about build, building agents.
[04:58] This is how we got started.
[05:00] So this is what LangChain was.
[05:01] This was a package launched a month before chat GPT.
[05:04] And it was really around building these LLM
[05:07] and agentic applications.
[05:08] Fun fact, we had a class called Agent
[05:11] in Langchain before a chat GPT launch.
[05:14] I remember it.
[05:15] I was on, I think, I was in San Diego for Thanksgiving
[05:18] and was just trying to decide what to call it.
[05:20] And I ended up calling it agent-executor instead of agent.
[05:23] So, you know, we're not great at naming
[05:25] and that's maybe the first example of that.
[05:27] But we had this concept of an agent and it was in Langchain.
[05:32] Then we launched Langgraph a little over a year later.
[05:35] As we saw that the applications that people were building,
[05:38] they may have started off as chains,
[05:40] but they were becoming more complex graphs.
[05:42] And that was the idea behind LangGraph.
[05:47] We then launched LangChain 1.0,
[05:49] and then about nine months ago, we launched deep agents.
[05:52] Deep agents is an evolution of this as well.
[05:55] And so I wanna talk a little bit more
[05:56] about deep agents right now,
[05:57] because that's where we think the future is really headed.
[06:01] So the core idea of an agent,
[06:03] from the original agent executor days in LangChain to now,
[06:08] is basically, it's pretty simple.
[06:09] It's an LLM running in a loop calling tools.
[06:12] There's a bunch of stuff that can happen around that loop.
[06:15] There's a bunch of specific tools you can add in.
[06:18] But when people talk about agents,
[06:19] this is essentially what they're talking about.
[06:21] A user request comes in, you call the LLM,
[06:24] the LLM decides to call a tool,
[06:26] you then execute that tool,
[06:27] and you keep on doing that until the LLM decides
[06:29] that it's finished.
[06:30] That's the core idea of an agent,
[06:31] and that's always been the case.
[06:34] So what is deep agents?
[06:35] Deep agents is an agent harness,
[06:37] And it basically adds more batteries, included things.
[06:40] It supercharges this loop.
[06:43] What are some of the things that it adds?
[06:46] It adds an execution environment.
[06:48] So agent harnesses need a place to run.
[06:51] A really common way to run them is in a sandbox.
[06:55] You give it access to a file system,
[06:57] you give it access to code,
[06:58] it can read files, write files, execute code.
[07:01] That's its execution environment.
[07:02] And so when people talk about agent harnesses,
[07:04] they often talk about coding agents
[07:06] part of that coding agent is its execution environment.
[07:09] Sam boxes are one extreme.
[07:12] You can write and execute code.
[07:14] And then on the other extreme, we
[07:16] have what we call a virtual file system in deep agents.
[07:19] This is basically a database that we expose to the agent
[07:23] as a file system.
[07:25] LLMs are great at reading and writing files.
[07:28] And so you can kind of trick it into having this kind of mock
[07:31] execution environment.
[07:32] But the point is you give it an environment to interact with.
[07:38] Deep Agents and other agent harnesses come with a lot of built-in context management.
[07:42] So skills and memory are examples of this.
[07:46] Summarization is an example of short-term memory when the conversation gets too long
[07:49] and you summarize it.
[07:51] Context offloading, how do you deal with really long tool calls?
[07:54] This is logic that's built in to the agent harness.
[07:58] Prompt caching is another example of this where you want to make sure that you're cashing
[08:04] the initial part of your request so that it can be faster
[08:06] and cheaper in the future.
[08:07] And so all of this context management is built into the
[08:09] harness and it does it automatically for you.
[08:13] Steering is really important.
[08:14] So these agents, these deep agents, they're long horizon
[08:17] agents, but that doesn't mean they're fully autonomous.
[08:19] You still need the human in the loop.
[08:20] And so deep agents comes with really good human
[08:22] in the loop controls.
[08:24] And then lastly, delegation.
[08:26] Agent harnesses can be used to kick off other agents,
[08:29] whether that's planning agents or other sub agents
[08:31] for different tasks.
[08:33] And so all of that delegation communicating with those subagents
[08:36] and having them communicate back to you,
[08:39] all of that is specified in an agent harness.
[08:43] And so deep agents contains all of these different things.
[08:46] We spend a ton of time doing both research and applied AI work
[08:49] to make sure that the way we do summarization is the best,
[08:52] the way that we do subagents is the best.
[08:56] And so today, one of the things that we're launching
[08:59] is DeepAgeant 0.6, a new version of DeepAgeants.
[09:03] There's three big things in it that are informed by three
[09:07] trends that we see in the industry.
[09:11] So one trend we see in the industry
[09:12] is the rise of open models.
[09:15] DeepSeq V4 launched last week, and it's just as performant
[09:19] on certain tasks as frontier models.
[09:24] So open source models are getting better.
[09:25] And the other thing that's happening is cost is rising.
[09:29] The cost of frontier models keeps on going up and up,
[09:31] and usage keeps on going up and up.
[09:33] And so one of the things that we think
[09:35] will happen more and more is more usage of open source models.
[09:39] And so with DeepAgent 0.6, we want
[09:41] to make it the best place to use open source models.
[09:45] So we're launching native support for GLM5, DeepSeek,
[09:48] and Nemotron models.
[09:51] We have best-in-class integrations
[09:52] with inference partners like Fireworks, Base10, and NVIDIA.
[09:57] And the easiest way to try out open source models in a harness
[10:01] is by coding.
[10:02] And so we're launching deep agents code
[10:04] as an open source example of how to build a coding agent
[10:08] on top of deep agents.
[10:09] And we're making it really, really good for open source models.
[10:14] The second thing that we're seeing
[10:16] is a lot of attention around the execution environment.
[10:18] So we talked about this.
[10:19] We talked about the virtual file system, which
[10:21] a really simple way to let the agent interact
[10:23] with what it thinks is a file system,
[10:25] but it's just a pretty simple database under the hood.
[10:27] And then on the other extreme, we
[10:28] have a full-blown code sandbox where the agent can write
[10:31] and execute code, spin up a web server, any of that.
[10:35] And so this is a spectrum.
[10:38] But what sits in the middle?
[10:40] And so in DeepAgent 0.6, we're launching CodeInterpreter.
[10:43] What CodeInterpreter is, we use QuickJS,
[10:47] which is a JavaScript runtime.
[10:49] And it basically lets the agent write and execute code
[10:54] in this kind of like, repel-like environment.
[10:57] So it's a subset of the JavaScript language,
[10:59] and you can't do everything that you can do in a sandbox.
[11:01] So you can't run Docker or things like that,
[11:03] but you can still write and call tools programmatically.
[11:06] You can manipulate data files.
[11:08] You can read and write from the file system here as well.
[11:10] And so we think this is a really interesting middle ground
[11:13] where it's super lightweight to deploy.
[11:15] So this is the benefit of it.
[11:16] You don't have to spin up a separate sandbox
[11:19] for each agent.
[11:19] You can just deploy this,
[11:21] and it's really easy to run in a multi-tenant way,
[11:24] but you still get a lot of benefits
[11:25] that you get from coding.
[11:29] The third trend that we've seen
[11:30] is that it's still really hard,
[11:32] but really important to build delightful UIs.
[11:34] UIs matter, interacting with the agents matter.
[11:37] And one thing that's happened
[11:38] is these agents have gotten more and more complicated,
[11:40] and the events that they're emitting
[11:43] are correspondingly more and more complicated.
[11:44] They emit text, they emit tool calls,
[11:46] images, reasoning, sub-agents, stuff,
[11:48] How do you do that?
[11:50] And so we want to make it as easy as possible for people
[11:52] to run agent harnesses and hook them up to delightful UIs
[11:56] that they build for their customers.
[11:59] And so the third launch in Deep Agents 0.6
[12:02] is better support for streaming.
[12:04] So we have a brand new streaming protocol.
[12:06] We have four different front-end SDKs
[12:08] for different front-end languages.
[12:10] And we're partnering with UI frameworks,
[12:13] like Co-PilotKit, Assistant UI, and Vercel,
[12:15] to make sure it's really tightly integrated.
[12:18] UIs are a big part of building agents,
[12:22] and we want to make it the easiest way to do so.
[12:25] So if you haven't already tried out deep agents,
[12:27] please go try it out today.
[12:28] This is where we think the future is heading.
[12:30] We think agent harnesses are getting more and more robust,
[12:33] more and more production ready.
[12:35] And deep agents is our version of that.
[12:40] I want to talk about the test phase next.
[12:43] So you've built your agent.
[12:44] How do you know if it's actually working?
[12:46] This is where Langsmith evaluations comes in,
[12:48] something we've been building over the past two years.
[12:52] Testing for agents looks different
[12:54] than testing for software.
[12:56] You want to build up data sets, so reference inputs
[12:59] and reference outputs, or maybe criteria
[13:01] to score how it's doing.
[13:04] You want to define metrics.
[13:05] How do you know if the agent is passing?
[13:06] This could be correctness.
[13:07] This could be hallucinations.
[13:08] But you want to define some metrics
[13:10] that work for your use case.
[13:13] And then you run your agent over these data sets,
[13:15] and you score them on these metrics,
[13:16] and you create these experiments,
[13:17] and you can use these experiments to hill climb
[13:20] on certain things.
[13:22] Or you can use them to make sure that you're not
[13:23] regressing as you're making changes.
[13:26] Evaluations are a key part of Lang Smith,
[13:29] and we're launching some stuff around this today.
[13:32] But I'm going to talk about that later.
[13:33] So I'm going to go on to deploy next.
[13:37] So you've built your agent.
[13:38] It's running locally.
[13:39] Now you want to go to production.
[13:40] There's a bunch of challenges that
[13:41] are going to emerge as you do that.
[13:43] First, you have to go from a single user, just you.
[13:45] Now you're serving many in production.
[13:47] Environment variables and memory, these now
[13:50] have to be specific to the users that you're interacting with.
[13:53] Off, you need to control who can access it.
[13:55] You can't just open it up to everyone.
[13:57] And then when it runs locally and it dies,
[14:00] you're just testing it.
[14:01] You can resume from there.
[14:03] But you need to run it durably when
[14:04] you're running it at scale.
[14:05] And so a year ago, we launched Langsmith deployments
[14:08] to help with this.
[14:10] So there's a bunch of features built into this.
[14:12] We launched about 30 different API endpoints
[14:14] to handle streaming, human in the loop,
[14:16] auth, other things like that.
[14:19] It's a single standard deployment pattern.
[14:21] Today it's served over 100 million agent runs
[14:24] and is trusted by companies like Workday, Cisco, Etsy,
[14:28] Podium, and ByteDance.
[14:31] But we also realized that Langsmith deployments
[14:34] isn't the only thing you'll need to bring an agent
[14:36] into production.
[14:38] We've talked about how agents need an execution environment,
[14:42] And one of the best execution environments is a sandbox.
[14:45] So whether the agent is a coding agent or not,
[14:48] reading and writing code can be really impactful
[14:50] for the agent.
[14:50] It can manipulate data that way.
[14:52] It can use CLIs that way.
[14:56] And so we generally think that a lot of agents
[14:57] will need the ability to write and execute code in sandboxes.
[15:01] And so today, we're excited to announce
[15:02] that Lang Smith sandboxes is generally available.
[15:06] Yeah.
[15:07] (audience applauding)
[15:11] We think this is a big part of Agents in the future,
[15:13] and so we made it really easy to spin up sandboxes
[15:16] in less than a second.
[15:17] There's persistence for these sandboxes,
[15:19] so that will survive across interactions.
[15:22] It supports snapshots and forks.
[15:25] One of the coolest things we've done is this off proxy.
[15:27] So if you wanna give the LLM the agent,
[15:30] the ability to use something that requires an API key,
[15:32] you don't actually want it to see that API key
[15:34] because then it could get prompt injected and leaked it.
[15:36] And so we have an off proxy that sits outside the sandbox
[15:39] and basically intercepts traffic and inserts that in.
[15:42] And this is all part of the Lang Smith SDK,
[15:44] and it's completely framework agnostic.
[15:46] So you can use it with deep agents,
[15:47] you can use it without deep agents,
[15:49] you can use it for testing agents,
[15:50] you can use it for RL,
[15:51] you can use it for running agents from production.
[15:53] We're really excited to see how people use it.
[15:56] We've already had a number of customers using it.
[15:59] Monday, for example, uses it for their AI assistant sidekick,
[16:03] and we're excited by the feedback
[16:04] that we've gotten so far.
[16:07] Another big part of bringing agents to production is context.
[16:12] So LLMs by themselves, they don't know anything,
[16:15] or they don't know everything.
[16:16] Humans don't know everything.
[16:17] When we need to look up things, we go to a library.
[16:19] We look at books to learn things, we read them,
[16:22] and that's exactly what agents do as well.
[16:23] They do that with context.
[16:25] And that context has evolved over the years
[16:28] as LLMs have gotten better.
[16:30] So we had a prompt hub in Lang Smith for the longest time
[16:32] where you could store inversion prompts.
[16:36] And prompts were the things
[16:37] that kind of like guided agents, but over the past few months
[16:40] and years ago, we've seen that the context provided
[16:43] to agents has graduated from prompts into things like
[16:46] agent.md files, so really detailed instructions,
[16:49] and skills that these agents have used.
[16:51] A lot of these are shaped by coding agent standards.
[16:53] Both of these are open standards, by the way,
[16:55] so they're part of open foundations.
[16:58] And so as the context that LLMs have needed
[17:01] has evolved from prompts into these agent.md and skills,
[17:05] So has our tooling for that.
[17:07] So today, we're excited to launch Lang Smith Context Hub.
[17:11] Woo!
[17:12] (audience applauding)
[17:16] And so, what's in this Context Hub?
[17:19] So, you can take your agents.md files,
[17:21] you can take your skills,
[17:22] you can take your like LLM wikis,
[17:25] so this thing that Carpathie did
[17:26] where he basically ran an LLM
[17:28] and had it generate wikis,
[17:29] which are condensed knowledge in markdown files.
[17:33] We think that's gonna become a more and more common pattern,
[17:35] So you can take all of this, you can store it in Context Hub,
[17:37] you get versioning, you get tags, you get comments,
[17:40] and then you can use these.
[17:41] You can pull them down locally,
[17:42] you can run them in your coding CLI,
[17:44] you can run them in deep agents as a virtual file system
[17:47] so we have an integration there,
[17:49] or you can use them in whatever agent harness you have.
[17:53] We think Context Hub is a first start at memory.
[17:57] We think memory is really, really important
[17:59] to agents in the future.
[18:00] We think agents.md and skills,
[18:02] you can absolutely view those as an early form of memory.
[18:05] And those are open standards.
[18:06] So that's a great thing because we
[18:09] think memory should be open.
[18:10] We think memory should not be locked in to an LLM,
[18:14] to a framework, or to a platform.
[18:16] And so even though we're building Context Hub,
[18:18] we want this idea of context to be really open.
[18:21] And so we're working with a number of companies,
[18:24] including Redis, Elastic, Mongo, and Pinecone,
[18:27] to turn this first stab at memory
[18:30] into something that's an open standard for memory, for agents.
[18:34] So we think everything should be open.
[18:36] [APPLAUSE]
[18:42] And lastly, we've got monitor.
[18:43] So you've launched it.
[18:44] But how do you know what the agent's actually doing?
[18:46] This is where a lot of the core links with functionality
[18:49] around tracing.
[18:50] So you can make sure that you can see the step of every agent
[18:54] and what the inputs are and what the outputs are.
[18:56] Dashboards, so you can track cost and latency over time.
[18:59] online evals, so you can run LLM as a judge or code over these traces, get some feedback
[19:05] and then attach that or just capture user feedback. All of this is part of Ling Smith
[19:09] Observability. We've been building a lot here over the past two years and over the past
[19:13] few months. We've got a few very big launches here, but we're going to save that for a little
[19:17] bit later. So this is the agent development life cycle, and this is what it makes -- this
[19:24] is what it looks like to bring agents and maintain agents in production. And when you
[19:28] You do it once for an agent that's fine.
[19:29] When you do it for 10 or when you do it for 100 agents,
[19:32] that's when you really need to start to think about
[19:33] the governance of all of this.
[19:35] How do you do this at scale?
[19:37] How do you do this in a cost efficient and secure way?
[19:40] And so specifically, two of the concerns
[19:42] that we've seen emerge around governance
[19:44] over the past few months have been cost and data exposure.
[19:48] LLMs are getting expensive.
[19:50] How do you know how much agents are spending,
[19:53] how much specific users are spending on agents,
[19:55] and how do you avoid surprise bills?
[19:58] On the data exposure side, LLMs are great at working with data,
[20:02] but they shouldn't be able to access every source of data.
[20:04] And so how do you control what they can and can't see?
[20:09] Today, we're launching Langsmith LLM Gateway in beta
[20:12] to help with that.
[20:14] Woo!
[20:16] [APPLAUSE]
[20:19] You guys can't just pick and choose which announcements
[20:21] you clap for.
[20:22] You've got to applaud for all of them.
[20:24] They're all great.
[20:26] So what is Link Smith LLM Gateway?
[20:28] So you've got your agents, they're running.
[20:30] Link Smith LLM Gateway basically sits between them
[20:32] and their LLM calls.
[20:33] You can set spend limits.
[20:35] You can have visibility, total visibility over spend.
[20:38] And then you can also set guardrails
[20:40] to help with PII and secret detection.
[20:43] It integrates with a bunch of coding agents out there.
[20:45] So you can use it.
[20:46] We know that coding agents is the most popular thing
[20:49] that people are using.
[20:49] And that's where a lot of these costs are happening.
[20:51] And so we've made sure to integrate it
[20:53] with a lot of coding agents out there.
[20:55] It integrates with all the LLM providers
[20:57] that LangChain can help you access,
[20:59] and everything's traced automatically to LangSmith.
[21:04] So this is the full agent development lifecycle.
[21:06] Everything that we're building kind of fits into this.
[21:09] And we recognize that there's a lot in here.
[21:12] Taking an agent and going to production
[21:13] and going through this lifecycle involves
[21:15] a bunch of different pieces.
[21:18] And so we want to make it as easy as possible for people
[21:21] to take all these pieces, take deep agents, which
[21:25] is our agent harness under the hood,
[21:27] and really, really easily go to production.
[21:29] And so to make that into a single API,
[21:33] today we're announcing in private preview,
[21:35] Manage Deep Agents.
[21:37] Woo!
[21:38] [APPLAUSE]
[21:42] So Manage Deep Agents is a single API
[21:44] for interacting with all these different components.
[21:46] So it runs the deep agent harness under the hood.
[21:49] It's deployed with Lang Smith deployments.
[21:51] And so that's where the agent will run.
[21:54] The models that you can access include any models out there.
[21:56] So we obviously integrate with OpenAI and Anthropic,
[21:59] but also with the open source model providers
[22:01] like Fireworks and Base10.
[22:03] All of the agent instructions and memory
[22:06] are stored in Context Hub, so that as you or your users
[22:10] or the agent itself updates them, you
[22:12] can see them there and version them there
[22:14] and track them there.
[22:16] These agents, when they're deployed,
[22:18] you basically want to deploy the agent over here
[22:20] and then give it access to a sandbox
[22:21] to run and write tools over here.
[22:23] And you want those to be separate.
[22:24] And so that's the architecture that we took.
[22:25] And we used Langsmith sandboxes to help
[22:27] power those sandboxes in the hood.
[22:29] MCPs are how you connect them to tools.
[22:31] So you can provide MCPs directly,
[22:33] or you can use Arcade or another partner that
[22:36] provides access to a lot of MCP servers to do that.
[22:38] And all of this streams out in the new streaming protocol
[22:41] that we announced.
[22:42] So you can integrate it super seamlessly
[22:44] with Co-Pilot Kit, Assistant UI, and other frameworks.
[22:49] So combining everything, LangChain Open Source
[22:52] and LangSmith power this whole agent development lifecycle.
[22:57] And we think that traces sit at the center of this lifecycle.
[23:02] And so we spend a lot of time as a company thinking about traces
[23:06] and thinking about how to build the best experience around them.
[23:10] Everyone does.
[23:12] But there's no one at the company who thinks more about traces
[23:15] than my co-founder, Ankush.
[23:17] He's been thinking for the past almost a year
[23:20] around how we can make the experience around traces
[23:23] the best possible experience,
[23:25] because this is what powers that whole loop.
[23:27] And so we're launching a lot of really cool things
[23:29] around this, but in order to talk about traces
[23:32] and his love of traces, I'd like to welcome
[23:34] onto the stage my co-founder, Ankesh Gola.
[23:36] (audience applauding)
[23:39] (upbeat music)
[23:47] [MUSIC PLAYING]
[23:55] Hey, everyone.
[23:56] I'm Ankush, co-founder and CTO here at LangChain.
[24:00] As Harrison mentioned, I do spend a lot of time
[24:03] thinking about agent traces.
[24:05] And that's because we really think
[24:07] that agent traces are at the center of the agent development
[24:10] lifecycle.
[24:13] Each agent trace captures the unique behavioral record
[24:17] of what your agent actually did at a specific point in time.
[24:23] That being said, agent traces, or more generally,
[24:27] agent observability, poses a unique data infrastructure
[24:31] problem.
[24:34] For one, agent traces are very deeply nested
[24:38] and can contain thousands, if not tens of thousands,
[24:41] of intermediate steps.
[24:44] The payloads associated with agent traces
[24:47] are large and unbounded.
[24:50] These two characteristics of agent traces
[24:53] are a direct result of agents running for longer time
[24:57] horizons and LLM context window sizes getting larger and larger.
[25:04] We're seeing an increased number of agent traces
[25:08] being logged with modalities, such as images and voice.
[25:13] Voice is getting especially popular with applications
[25:16] like customer support.
[25:19] Finally, the access patterns or the query patterns needed
[25:23] to effectively mine your agent traces for useful insights
[25:28] are unique and complex.
[25:33] Agent traces are not only encoding more information
[25:36] and getting more complicated, they're also growing in volume
[25:40] as agents become more and more ubiquitous.
[25:44] Here's a figure that highlights a real Langsmith customer's
[25:48] weekly trace volume over time.
[25:51] As you can see, in the early stages of testing and development,
[25:55] the weekly trace volumes are relatively small.
[25:58] But as the agent enters production
[26:01] And as new agents enter the picture,
[26:04] the weekly trace volume that we now see is over 150 million.
[26:13] So as mentioned earlier, the payloads associated
[26:17] with agent traces are large, and they're getting bigger
[26:20] over time.
[26:23] Over the past couple of years, we've
[26:25] seen the P50 payload size associated with agent traces
[26:29] sent to Langsmith grow from 6 kilobytes to 37 kilobytes.
[26:35] And P99 has grown from still a pretty sizable 364 kilobytes
[26:40] to 12 megabytes today.
[26:43] And another data point.
[26:46] Earlier this year, we had a single customer
[26:48] send us 50 terabytes of trace data on a single day.
[26:53] That's quite a lot of data.
[26:57] This video highlights what a modern agent trace in Langsmith
[27:01] looks like in practice.
[27:03] As you can see, lots of intermediate steps,
[27:07] very deeply nested.
[27:08] This trace is actually pulled from one
[27:11] of our internal go-to-market agents that's
[27:13] built with deep agents.
[27:14] And another thing to point out is that this trace actually
[27:17] encodes 8.1 million tokens.
[27:23] Traditional data infrastructure was not
[27:26] built for the challenges associated with agent observability.
[27:32] If you're using suboptimal infrastructure
[27:34] to handle agent observability workloads,
[27:37] you will experience slow queries and ingestion bottlenecks.
[27:41] You'll also experience rising infrastructure costs
[27:43] and complexity as you try to scale up.
[27:47] When you're iterating on your agent,
[27:49] you cannot afford to have slow and cumbersome interactions
[27:54] with your agent traces.
[27:56] And so today, we're super excited to be launching SmithDB.
[28:01] [APPLAUSE]
[28:06] SmithDB is the database we purpose
[28:09] built for agent observability workloads.
[28:12] We've been working on SmithDB for the past few months
[28:15] and are incredibly excited by the results
[28:17] that we're seeing in production.
[28:19] Please stay tuned for this video to learn a little bit more.
[28:22] Introducing SmithDB, the database purpose built
[28:25] for agent observability.
[28:27] This is a trace, a record of what your agent does,
[28:30] how it thinks, decides, and performs.
[28:33] Now, imagine thousands of them, millions growing each day,
[28:37] because agents are everywhere.
[28:39] The problem is that traces aren't like
[28:41] traditional logs and metrics.
[28:43] They're larger, deeply nested, multimodal,
[28:46] and you don't query them the same way.
[28:48] You're searching across text and meaning,
[28:51] In traditional databases, they weren't built for this.
[28:54] So as traces grow, searches slow until now.
[29:00] SmithDB, the database purpose built for agent observability.
[29:04] Search across Vultrace content, query entire agent conversations,
[29:08] access conflicts data instantly and at scale.
[29:13] Building reliable agents requires rapid iteration.
[29:16] With SmithDB, you can move from data to insight,
[29:20] to improvement faster.
[29:25] (audience applauding)
[29:31] - That video got me pretty hyped up, not gonna lie.
[29:34] Whoever's creating our videos is doing an amazing job.
[29:38] So now let's take a closer look at what SmithDB actually is
[29:42] and how it's architected.
[29:44] The first thing to point out is that SmithDB
[29:47] is backed by object storage.
[29:49] This gives us a few nice properties.
[29:51] First, object storage is incredibly cheap,
[29:54] and it scales pretty much infinitely.
[29:57] The second is it gives us what's called
[29:59] compute storage separation.
[30:01] This allows us to elastically scale the services
[30:05] that Baxmyth DB without any complex shuffling
[30:09] or sharding of data as you scale up the services.
[30:14] Third, this gives us an architecture
[30:17] that is relatively easy to set up in self-hosted environments
[30:21] where dated residency requirements are strict.
[30:26] Now at a high level, the Langsmith services
[30:30] connect to SmithDB after getting assignments
[30:33] from our cluster manager.
[30:34] Our cluster manager helps ensure that load
[30:37] is evenly distributed across our servers
[30:40] and it also maintains some semblance
[30:42] of what's called sticky routing.
[30:45] Sticky routing is important
[30:46] because it helps utilize cache, and it also helps batch our data
[30:50] effectively for ingestion.
[30:53] So during ingestion, raw trace data
[30:56] comes into our ingestion service.
[30:57] It gets batched, and it gets durably stored to object storage.
[31:02] These files are registered in a Postgres backed meta store.
[31:06] At query time, we figure out which files are necessary
[31:09] to be scanned for the queries.
[31:11] We download them from object storage, and we scan them.
[31:15] We also heavily utilize SSD caching and memory
[31:19] to minimize round trips to object storage.
[31:23] Finally, we have a compaction service
[31:25] that helps shape our files for more optimal querying.
[31:31] SmithDB is specifically designed
[31:33] for agent observability access patterns.
[31:37] We'll walk through some of these access patterns
[31:39] in the next few slides.
[31:43] SmithDB makes clicking into individual traces
[31:45] and individual intermediate steps really snappy and fast.
[31:51] Agent observability isn't just about asking
[31:53] what happened across millions of traces.
[31:57] It's also about asking what happened
[32:00] in this one particular agent execution.
[32:04] That's why random access is really important
[32:07] and something that we've optimized in SmithDB.
[32:15] Agent traces can contain megabytes of text data.
[32:19] And oftentimes, you need to search
[32:22] across your agent traces using keywords or phrases.
[32:29] As you can see, SmithDB makes full text search really
[32:32] snappy and interactive.
[32:34] To accomplish this, we've actually
[32:35] built a custom inverted index layout specifically designed
[32:39] for object storage.
[33:01] and you can
[33:11] You often need to pick a specific time horizon
[33:13] and apply filters like on metadata, tags, name, latency,
[33:19] and other attributes.
[33:21] Scanning and filtering speed is something
[33:24] that we've highly optimized within SmithDB.
[33:26] And as you can see, the results are nearly instant.
[33:33] We're incredibly pleased by the performance
[33:36] that SmithDB brings to Langsmith across these key agent
[33:40] and observability workloads.
[33:42] Compared to before SmithDB, these Lang Smith workloads
[33:46] are now anywhere from 6x to 15x faster than before.
[33:52] This is absolutely massive.
[33:55] [APPLAUSE]
[34:01] But look, don t just take our word for it.
[34:03] We re super lucky to be working with customers
[34:06] like Clay and Vanta, who were early adopters
[34:09] for SmithDB.
[34:10] to be on Langsmith.
[34:12] As you can see Jeff from clay and Andy from Banta both state how SmithDB has completely
[34:18] transform their experience with their traces within Langsmith.
[34:26] So SmithDB is purpose-built for agent observability and we built it using a modern tech stack.
[34:34] The entire system is written in Rust and we use two awesome open source projects.
[34:39] one is called a PEP.
[34:40] patchy data fusion, which is an extensible, rust-based query
[34:44] engine.
[34:45] The second is Vortex, which is an extensible file format
[34:49] that allows us to pick custom encodings and custom
[34:52] chunking strategies for the different columns that we store.
[34:57] On top of this foundation, we have heavily--
[35:01] we've added some heavy customizations around indexing,
[35:05] specifically for full-text search.
[35:07] We've added custom query planning and execution plans.
[35:10] And we also have invested in custom storage layouts
[35:14] for all the data that we're storing within SmithDB.
[35:20] Here are some of the technical challenges
[35:22] that we've had to solve when building SmithDB.
[35:24] These are just a few of them.
[35:26] They're quite a lot, but I try to choose.
[35:31] So in agent observability workloads,
[35:34] your spans are distributed.
[35:37] They come in different parts.
[35:38] And this is because agents run for long time horizons.
[35:42] And so you can have a start event that gets sent sometimes
[35:47] hours before your end event.
[35:49] And so finding and merging these distributed events
[35:53] together at query time and at compaction time
[35:56] is a technical challenge that we had to solve.
[35:58] Doing it efficiently is something that we've
[36:00] invested a lot of time in.
[36:04] A lot of the queries within Lang Smith
[36:07] are top case style queries.
[36:09] So they contain an order by and limit.
[36:12] And a more naive query plan would essentially
[36:14] like find all the files that are in range
[36:17] and fan them out, scan them, do some type of merge
[36:21] and top K operation.
[36:23] This is actually like a little bit expensive
[36:25] on object storage, actually quite expensive
[36:28] on object storage.
[36:29] So what we've done is we've taken a time window based
[36:33] approach and encoded that into a custom execution plan that
[36:37] feeds top case to alqueries within SmithDB.
[36:42] Finally, in observability workloads,
[36:45] you often need to serve the most recently ingested data
[36:51] as fast as possible.
[36:53] And in order to do that, what we do
[36:56] is we buffer data in the ingestion service
[36:59] even after it's been durably flushed to object storage.
[37:02] and we buffer it in memory and on SSD.
[37:06] And we make that data available to the query service
[37:09] to avoid downloading a ton of small files
[37:13] for leading edge style queries.
[37:19] Langsmith performance is not only important for human UX,
[37:23] but also agent UX.
[37:27] Increasingly, agents are not just the thing
[37:30] that are being observed by Langsmith,
[37:32] they are also the users of Langsmith.
[37:37] And it's a huge hit to have your agents slow down
[37:40] by inefficient tools.
[37:43] I really like this quote from Jeff Dean,
[37:45] who states that, you know, as we get agent-based systems
[37:48] that are operating multiple times faster than a human,
[37:52] your tools can become like an Amdell's Blah Blah bottleneck.
[37:59] We're super excited to announce that SmithDB is now serving
[38:03] core observability workloads across all of US Cloud
[38:07] on Langsmith.
[38:08] So if you're using Langsmith on smith.langchain.com,
[38:11] all of your interactions and your tracing projects page
[38:14] are now powered by SmithDB.
[38:18] Soon--
[38:19] [APPLAUSE]
[38:24] --we're working quickly to get the rest of the Langsmith UI
[38:27] back by SmithDB.
[38:29] And we're going to bring it soon to self-hosted and across all
[38:32] of global cloud traffic.
[38:34] So SmithDB sets a really, really strong technical foundation
[38:38] for everything that we want to build into Langsmith.
[38:42] And to share some more exciting updates about Langsmith,
[38:44] I'd like to welcome Harrison back on stage.
[38:46] Thank you so much.
[38:48] [APPLAUSE]
[38:50] (audience applauding)
[39:00] - SmithDB is absolutely incredible.
[39:02] As you can see, I have the fun and easy job
[39:05] of just talking about what we build,
[39:06] but on Cush and the whole team there goes out
[39:09] and builds really complex engineering projects
[39:12] and databases that help power everything
[39:14] in the agent development life cycle.
[39:17] And that's really how we think about what we do.
[39:19] We want to accelerate everything in this life cycle.
[39:21] We think traces and SmithDB are a key part of that.
[39:25] And so with this solid foundation,
[39:27] a big part of what we're thinking about now
[39:29] is how can we accelerate this life cycle even more?
[39:33] Because even with traces and even with observability,
[39:35] the visibility that it provides is table stakes.
[39:38] Being able to see what your agent did at each step
[39:41] is absolutely needed, but that is table stakes.
[39:44] It's still hard to spin this iteration flywheel.
[39:49] Finding issues among the tens of thousands,
[39:52] hundreds of thousands, millions of traces that you have
[39:55] is still hard.
[39:58] Once you find those traces, understanding issues in them
[40:02] is still hard.
[40:03] They can be really, really long.
[40:04] You have to comb through them
[40:05] and see exactly where the LLM is messing up,
[40:08] where it's calling the wrong tool.
[40:11] Once you understand that issue,
[40:13] Fixing them is hard.
[40:15] Do you want to change the prompt?
[40:16] Do you want to change the code?
[40:17] Do you want to change some tools?
[40:18] There's a bunch of different things
[40:20] that you have to investigate and try to tie back
[40:22] to the core issue.
[40:24] And then once you fix it, avoiding repeating these issues
[40:27] is hard.
[40:28] Sometimes it can feel like whack-a-mole.
[40:29] You fix one thing, and then you change the prompt,
[40:32] and it reappears.
[40:33] And so how do you avoid this?
[40:36] And so we spend a lot of time thinking
[40:38] about how we can spin up this flywheel faster and faster
[40:43] because it is still hard.
[40:44] All these things I mentioned are still annoying.
[40:47] And so what do you do when you have a lot of really annoying
[40:50] things that are hard and important that you don't want to do?
[40:54] You build an agent to help you with them, of course.
[40:57] And so that's why today we're really
[40:59] excited to launch an agent in Langsmith, an ambient,
[41:03] proactive, action-taking agent that we're
[41:06] calling Langsmith Engine.
[41:10] [APPLAUSE]
[41:14] Specifically, what it does is it will sit on top of your traces.
[41:19] It'll go through them on a schedule in the background.
[41:23] It will detect issues and assign a priority to them.
[41:26] It will back its evidence with traces.
[41:29] And then it will suggest concrete resolution actions.
[41:33] We've been working with a number of startups
[41:35] over the past few weeks to roll this out to them.
[41:38] And as you can see, it is already proactively suggesting
[41:41] evals to add and code changes to make
[41:44] and has dramatically reduced time to detection
[41:47] and time to triage.
[41:49] So specifically what Engine can do,
[41:51] it acts at all stages of this life cycle.
[41:53] So it sits on top of traces.
[41:55] It can suggest code changes if you hook it up
[41:58] to your GitHub or code base.
[41:59] It can suggest data points to add to data sets
[42:02] so that you can use these to avoid regressions
[42:04] in the future.
[42:06] If you connect it to Prompt or Context Hub,
[42:08] it can suggest changes there.
[42:10] And then it can also suggest online evals
[42:12] to add so that you can track these issues over time.
[42:16] Let's see a little video of it in action.
[42:20] [MUSIC PLAYING]
[42:22] (dramatic music)
[43:26] [MUSIC PLAYING]
[43:30] [APPLAUSE]
[43:36] LayingSmith Engine is in public beta as of today.
[43:40] So I already see some people on laptops log on to LayingSmith
[43:43] and try it out.
[43:46] Overall, as a company, we're building the entire platform
[43:50] for the agent development lifecycle.
[43:53] Over the past few years, we've been
[43:55] building a lot of the different apps and infrastructure
[43:57] pieces from observability and evaluations and Prompt Hub
[44:01] that help power a lot of this lifecycle.
[44:05] Today, we launched SmithDB as a foundational database
[44:09] to power all of this.
[44:11] And we built LangSmith Engine as an agent that sits on top
[44:15] and helps you spin this flywheel faster and faster.
[44:20] more than just a platform, we also want to be a partner to everyone in this room, in
[44:25] the community, in the entire space in general.
[44:29] And that's why we're really thrilled about Interrupt in General.
[44:33] This is an opportunity to interrupt your day and take a pause and learn from us, but also
[44:39] other presenters and other partners in the ecosystem and other companies and other people
[44:43] that you're sitting next to, and I would encourage everyone to take full advantage
[44:48] of not only today but also tomorrow as well.
[45:17] [BLANK_AUDIO]
