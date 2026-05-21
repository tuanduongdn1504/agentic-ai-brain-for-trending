---
source: yt-dlp-only
url: https://www.youtube.com/watch?v=efRIrLXoOVA
title: "Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)"
speaker: Cole Medin
channel: Cole Medin (@ColeMedin)
upload_date: 2026-05-21
duration: 28:10
view_count: 2091
fetched: 2026-05-21
path: 5-yt-dlp-only
notes: Practitioner walkthrough of the Anthropic 2026-05-14 large-codebases blog. Each of the 7 components is demoed against companion repo coleam00/helpline. Cole's term for "harness" is "AI Layer." Distributes a plugin (helpline-ai-layer) for one-command install of portable pieces (Stop hook + explorer subagent + codebase-search MCP + scoped-tests skill).
---

# Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases) — Cole Medin

> Verbatim auto-caption transcript with `[MM:SS]` timestamps. Cleaned from VTT via `/tmp/clean_vtt3.awk`. 808 segments / ~6.6K words.

[00:00] Claude and AI coding tutorials are a
[00:02] dime a dozen these days. But what people
[00:04] are not really covering nearly enough is
[00:07] how to use these tools to work in large
[00:10] code bases. That's what I want to cover
[00:12] with you right now. Because you probably
[00:15] already have a complex codebase or two
[00:17] or three. You've got the apps and
[00:19] platforms that you're building your
[00:20] second brain. You have these code bases
[00:22] that are tens or even hundreds of
[00:24] thousands of lines long. And it can be
[00:26] tough to get these coding agents to
[00:28] navigate those larger code bases and
[00:30] work in them effectively. And even if
[00:32] you don't have a complex codebase yet,
[00:35] you'll get there, my friend. You start
[00:36] with a simple idea, a simple codebase.
[00:39] But as you evolve that codebase, the
[00:42] coding agent strategies that work
[00:43] before, they fall flat on their face.
[00:45] That's why I'm excited to get into this.
[00:47] Enthropic put out this article just a
[00:50] few days ago, how to use cloud code to
[00:52] work in large code bases. And really
[00:54] these ideas apply no matter the coding
[00:56] agent that you are using. And there's a
[00:58] lot of gold in this blog post. So I want
[01:01] to get into all of this. They do stay
[01:02] pretty high level in the blog post
[01:04] though. And so I also took all of their
[01:07] strategies and I built them into a demo
[01:10] codebase for this video. So not only are
[01:12] we covering the article, but we're also
[01:14] going to see concrete examples of all
[01:16] the strategies in action. And I even
[01:18] have a claude plugin that makes it super
[01:21] easy for you in two commands to take a
[01:24] lot of the strategies that we're
[01:25] covering here and immediately bring them
[01:27] into any codebase that you are working
[01:29] on. And so we'll get to that, but I want
[01:31] to start pretty high level, share these
[01:33] strategies, and let's see them in action
[01:35] as well. So, Enthropic starts by talking
[01:37] about all of the pretty impressive
[01:39] places where cloud code is currently
[01:41] being used at an enterprise level across
[01:43] multi-million line model repos, decades
[01:46] old legacy systems, distributed
[01:47] architecture spanning dozens of
[01:49] repositories. Basically, they're just
[01:51] making the point here that if you think
[01:53] your codebase is too complex for cloud
[01:56] code, you are wrong. And then they go
[01:58] into how cloud code navigates a
[02:01] codebase, at least before we have more
[02:03] of an AI layer. So the tool out of the
[02:05] box, it uses something called a gentic
[02:08] search. So we're not performing
[02:10] traditional rag or semantic search.
[02:12] There's no codebase indexing with cloud
[02:14] code. Instead, it's going to navigate a
[02:17] codebase more as an engineer would with
[02:19] command line tools like GP, just looking
[02:21] at the folder structure, using all of
[02:23] the command line tools at its disposal
[02:25] to identify the places for especially a
[02:28] larger codebase to pay attention to and
[02:30] where it needs to edit. And so this is
[02:32] really powerful because then there's no
[02:34] index that you have to keep in sync. But
[02:36] the tradeoff is that claude works best
[02:38] when it has enough starting context to
[02:41] know where to look. And so this really
[02:43] gets us into a lot of the strategies
[02:45] that we'll cover here. It's all about
[02:46] how do we curate that context up front
[02:49] so Claude can navigate a more complex
[02:51] codebase effectively knowing where to
[02:54] actually look based on the requests that
[02:56] we have for it. So that then brings us
[02:58] to the main point of this blog post that
[03:00] really sets the stage for all the
[03:02] strategies. The harness matters as much
[03:04] as the model. A lot of people get really
[03:07] hyperfixated on model benchmarks and
[03:10] they think that tools like cloud code
[03:11] and codeex the power really comes from
[03:14] how good the underlying large language
[03:15] model is. And yes, that matters. But
[03:17] honestly, what matters even more is the
[03:19] ecosystem built around the model, the
[03:22] harness. And I like to call it the AI
[03:24] layer. I think that's more descriptive.
[03:26] It's really everything that they lay out
[03:27] right here with quite a few paragraphs.
[03:29] I also have a nice diagram to make this
[03:32] even simpler. The AI layer is the set of
[03:34] context and tools that you give your
[03:36] coding agent to work on a codebase. And
[03:39] so, traditionally, a codebase would have
[03:41] two main parts. It would have the code
[03:42] and then it would have the tests. And so
[03:45] now with the AI layer, we have a third
[03:47] component of every codebase introduced.
[03:50] This is everything like your global
[03:52] rules, your skills, your MCP servers and
[03:55] sub agents. Really, every single
[03:57] individual feature of cloud code that
[03:59] gives tools or context that is a part of
[04:02] your AI layer. And so there's seven
[04:04] things that we have here. Couple you
[04:06] might not be as familiar with like LSP
[04:08] and hooks, but we'll talk about all of
[04:10] that because really each of these seven
[04:12] map to one of the strategies that Claude
[04:15] Code covers. This is where I have a
[04:17] concrete example for each of them. Let's
[04:19] get into this. So, the initial
[04:20] strategies that Enthropic covers are all
[04:22] about making it as easy as possible for
[04:25] Claude Code to navigate your codebase at
[04:27] scale. And a lot of it centers around
[04:30] the first and maybe even most important
[04:32] part of your entire AI layer, which is
[04:34] your global rules. So, take a look at
[04:37] this. They have this visual
[04:38] representation for how often the each
[04:42] part of the AI layer is used throughout
[04:44] a cloud code session. You can see that
[04:46] most of them are sporadic like your
[04:48] hooks and skills and the LSP for
[04:50] navigation. We'll talk about all these
[04:51] as well. But your global rules as your
[04:54] foundation, it is dictating the behavior
[04:56] of cloud code the entire time. So you
[04:59] better spend a good amount of time
[05:01] strategizing around your context
[05:04] curation here. And so their first tip is
[05:06] to keep your global rules lean and
[05:08] layered. Something that I see a lot of
[05:10] people do unfortunately is create these
[05:12] global rule files that are thousands of
[05:14] lines long. That is not a good idea.
[05:16] There are actually studies out there
[05:17] that prove that that can hurt your
[05:19] coding agent performance. Even if you
[05:21] think that being really specific and
[05:23] comprehensive helps, you're just going
[05:24] to overwhelm your LLM with context. You
[05:26] just need core information. What is the
[05:28] codebase about? Give it a little bit of
[05:30] an idea of the tech stack or
[05:32] architecture, for example. I mean, this
[05:33] is just an example that I have in this
[05:35] repo. Um, then your general conventions
[05:37] and gotas like what I have right here.
[05:39] Commands to run for things like testing
[05:41] and getting the dev server spun up. Like
[05:44] that's all you really need. So keeping
[05:46] it lean. And what Enthropic means by
[05:49] layered is you can actually have claw.md
[05:52] files in subdirectories. And so I have
[05:55] the main claw. MD at the root of my
[05:57] repository here. That means that
[05:59] whenever I start a clawed session like
[06:01] this, it is always going to have these
[06:05] rules loaded. But then as soon as I
[06:08] navigate in and start editing files in
[06:10] one of these subdirectories, it's also
[06:12] going to load in that claw.md
[06:14] automatically. So if I start working in
[06:16] the API service, for example, I'm going
[06:19] to load in my core rules or I should say
[06:21] those are already loaded. But then I'm
[06:23] also going to load in the API service
[06:25] rules that I have in the separate
[06:27] claw.md. So I'm building up the list of
[06:30] conventions based on where I'm actually
[06:32] operating in the codebase. It's like the
[06:34] idea of progressive disclosure that we
[06:36] have with claude code skills. This is
[06:38] really powerful because if you have a
[06:40] massive codebase, you're going to have a
[06:41] ton of conventions, but most of them are
[06:44] going to be specific to certain slices
[06:45] of the codebase. So, let's just load in
[06:47] the conventions we need depending on
[06:49] where we're working because whenever you
[06:51] have some kind of GitHub issue or GR
[06:53] ticket or whatever, hopefully it's
[06:55] scoped to a very specific part of your
[06:57] codebase. And then another thing you can
[06:59] do if you're really confident where you
[07:02] need to work in a codebase is you can
[07:03] actually initialize cloud code in that
[07:06] subdirectory. So if I know for example
[07:08] that based on a Jira ticket or GitHub
[07:10] issue I'm only going to be working in
[07:12] the API service then I can you know
[07:14] rightclick in VS code copy my path and
[07:17] then within here just for the sake of
[07:18] example I guess I'm already there but I
[07:20] can change my directory to that path and
[07:23] then I can open up claude here. And the
[07:25] power of this is now this is the current
[07:28] working directory for clawed code. So
[07:30] unless I tell it to, it's really going
[07:31] to stick to editing files in just this
[07:34] directory. So it'll load the claw.md
[07:36] here. And then it still will load the
[07:38] rootclaw.md. So you can see that it does
[07:41] automatically walk up the directory tree
[07:43] and load every claw.md. So the root
[07:46] context isn't lost, but we're just
[07:48] honing claw code in on that part of the
[07:50] codebase. And so basically you're doing
[07:53] the navigation here. So the rest of
[07:55] their strategies are like you know how
[07:56] can you help Claude navigate things
[07:57] effectively but most of the time
[08:00] especially if you are an engineer you
[08:02] know where to start. Now if you don't
[08:04] know where to start that's where this
[08:06] strategy comes in building up some kind
[08:08] of codebased map when the directory
[08:10] structure doesn't do the work and this
[08:13] usually I put in my global rule. So, I
[08:15] don't have it in this example here, but
[08:17] often what I'll do is I'll have a
[08:18] section that outlines the directory
[08:20] structure, like all the subdirectories,
[08:22] maybe like a brief description of each
[08:24] of them. That way, Claude can help me do
[08:26] the discovery, help me figure out what
[08:29] slice of the larger codebase to focus on
[08:31] based on the work that I have. So,
[08:33] usually it comes down to Claude's going
[08:35] to help you figure that out or you're
[08:37] just going to immediately know and
[08:38] initialize Claude code there. The
[08:40] sponsor of today's video is Jet Brains
[08:42] Academy. Now, I've tried a lot of AI
[08:45] courses in the past, and most of them
[08:47] have this problem. The way that I'd put
[08:49] it is that the course ends where the
[08:51] real work actually begins. And what I
[08:53] mean by that is you'll go through some
[08:55] material and some really basic
[08:56] exercises, but then you don't get to
[08:58] really deploy anything. And Jet Brains
[09:01] Academy is different with their skill
[09:03] paths. Here, when you learn a concept,
[09:06] you get to apply it to a real project
[09:08] immediately. And so you do your work and
[09:10] go through the lessons in the IDE and
[09:12] then you get to right away deploy what
[09:14] you've built in AWS sandboxes. So you
[09:18] start by picking a path. Let's say we
[09:20] want to do build and deploy custom LLMs
[09:21] with Python and AWS. It seems very
[09:24] relevant right now. And so we have the
[09:26] course layout here. This is the
[09:27] syllabus. And you can see that each of
[09:29] the sections, it'll open the course in
[09:31] your PyCharm IDE. So we get to go
[09:34] through the material where we're doing
[09:35] all of our coding already. The AI
[09:37] assistance is built right into the IDE.
[09:39] I can navigate through the lessons and
[09:41] go through all the material right here
[09:42] really easily. And then as I'm doing my
[09:44] exercises, it's just right here in the
[09:46] IDE. So, I get to code as I normally do.
[09:49] And then when it comes time to run and
[09:51] deploy things like the fine-tune model
[09:53] that we have in this lesson, we get to
[09:55] do it in an AWS sandbox. This is not a
[09:58] mock. It is running in the cloud, but
[10:00] it's fully prepaid. You don't need an
[10:02] AWS account. This is what I wish I had
[10:05] when I was learning how to build and
[10:06] fine-tune models. So, when you finish a
[10:09] skill path, you have real projects
[10:10] deployed live that you can host on
[10:12] GitHub, talk about interviews, and get
[10:14] hired for, and you have certificates
[10:16] both from Jetrains and AWS to back it
[10:18] up. So, if you're looking to build
[10:20] proficiency and credibility with
[10:22] Generative AI and LLM engineering, I
[10:24] would highly recommend checking out
[10:26] Jetrain Academyy's skill pads. I'll have
[10:28] a link to them in the description. Cool.
[10:30] So there are some more strategies to
[10:31] cover here like scoping your tests and
[10:33] lint commands per subdirectory, ignoring
[10:35] certain files like build artifacts so
[10:37] your coding agent never reads them. But
[10:39] I want to move on now to talk about the
[10:41] next part of the AI layer and that is
[10:44] hooks. And you'll see in a second why I
[10:46] want to cover this right after global
[10:48] rules. So you can use hooks to make your
[10:51] entire AI layer, your entire setup
[10:54] self-improving. This is really, really
[10:56] cool. This is part of the goal that I
[10:57] was talking about. So most teams think
[10:59] of hooks as scripts that prevent Claude
[11:01] from doing something wrong. So a lot of
[11:03] people use hooks like a pre-tool use
[11:05] hook to stop Claude from editing in
[11:08] certain directories, removing files or
[11:09] folders, that kind of thing. But their
[11:12] more valuable use is continuous
[11:14] improvement. And so take a look at this.
[11:16] A stop hook can reflect on what happened
[11:19] during a session and propose claw.md
[11:23] updates while the context is fresh.
[11:25] Right? so that the hook runs at the end
[11:27] of the session. And I have a live demo
[11:29] of this. I'll show you. I actually built
[11:31] out both of these hooks here. And then a
[11:33] start hook can load team specific
[11:35] contexts dynamically. So every dev gets
[11:37] the right setup without manual
[11:39] configuration. So based on the role or
[11:41] the part of the codebase they're
[11:42] editing, we can have a hook that will
[11:44] even go out to confluence for example
[11:46] and pull documentation for that team,
[11:49] that function, that part of the
[11:50] codebase, whatever. So I have actually a
[11:53] pretty basic example of that here. And
[11:56] so I have a hook. And so you can see in
[11:57] my settings.json, this is where I have
[11:59] the start and end hooks defined. So
[12:02] propose claw.md updates for the stop
[12:04] hook. And then the session start context
[12:06] for the start hook. And so what this
[12:10] hook does, this is just more of a basic
[12:12] example, is it's going to load context
[12:14] around git. And so any kind of unstaged
[12:17] changes that I have like a change to
[12:19] this file here looking at the git
[12:21] history as well. So take a look at this.
[12:23] If I go into claude and I start a new
[12:25] session and then I say what did the
[12:26] start session hook tell you about this
[12:28] session. Obviously it's a little cheesy
[12:30] but just to show you that it loaded the
[12:32] context. We have this orientation here.
[12:34] The working tree is clean. Here are our
[12:37] recent commits, right? And so like this
[12:39] is just giving it some context going
[12:41] into like here is what we're currently
[12:42] working on and here is what we worked on
[12:44] recently. And you could extend this like
[12:46] I said to pull things from Confluence
[12:48] based on the developer that is starting
[12:50] Cloud Code. There's a lot that you can
[12:52] do here. And then take a look at this to
[12:54] demo the stop hook for you. I'm going to
[12:56] give a really simple request for
[12:59] something that I want to change.
[13:00] Obviously if I was doing work for real I
[13:02] go through more extensive process of
[13:04] planning and implementing and
[13:05] validating. But here I'm just asking it
[13:07] to make a simple change so that I have
[13:09] something to then propose a change to
[13:12] the global rules because something
[13:13] really important that you need to do and
[13:15] you can see that the process actually
[13:17] ran here in order to propose some
[13:19] changes. Something that's really
[13:21] important to do is as you're evolving
[13:22] your codebase you need to make sure that
[13:25] your rules are evolving as well. It's
[13:27] really really bad when your claw.md goes
[13:30] stale because you made some changes in
[13:33] the codebase where it kind of you know
[13:35] dictates something needs to be added to
[13:36] the global rules or something has to be
[13:38] updated. And so that's why it's really
[13:40] powerful to have this kind of process
[13:42] that automatically proposes these
[13:44] changes. So take a look at this. This
[13:46] hook runs whenever Claude stops. So
[13:49] whenever it's done with its turn. So you
[13:52] saw that terminal pop up for a little
[13:54] bit. It runs a separate cloud session in
[13:56] headless mode to look at these changes,
[13:58] look at the global rules and propose if
[14:00] anything needs to be tweaked. And so it
[14:02] outputs that in a markdown document.
[14:05] Take a look at this. I have my claude
[14:06] markdown review. And so we have the
[14:09] reflection that just ran right now. Here
[14:11] are the two areas that were touched. So
[14:13] it's going to look at those subdirectory
[14:15] global rules as well. And here it
[14:16] decided no changes needed. Adding a
[14:18] trial enum value follows the existing
[14:20] model only convention. So the thing that
[14:22] we really care about at a high level
[14:24] still holds up based on these changes.
[14:26] And so maybe it's not the best example
[14:28] because it didn't decide to change
[14:29] anything, but I think that's also really
[14:31] powerful because usually we don't need
[14:33] to change our claw code or claw.md
[14:35] conventions. That's especially why we
[14:37] keep these files so lean. But maybe for
[14:39] example, I could say, you know, make a
[14:41] change that would require updating the
[14:44] claude.md. So I'll come back and see
[14:46] what it does with this. And so there we
[14:48] go. We had it change something bigger in
[14:50] the billing service. And now in our
[14:52] markdown review, it is recommending
[14:54] making an update to the second bullet in
[14:57] the claw.md for our billing service
[14:59] subdirectory. Pretty neat. So now we can
[15:01] take these recommendations and we can
[15:03] action on it ourselves. We can have a
[15:05] conversation with a separate claude
[15:07] session to make these changes. It's up
[15:09] to you how you want to take this
[15:10] forward. The power I'm just trying to
[15:12] show you here is we can have this
[15:14] self-reflection process constantly
[15:16] running in the background making these
[15:18] suggestions that we can a you know just
[15:20] action on when we're actually ready to.
[15:22] So the next part of the AI layer that
[15:24] Anthropic focuses on here is skills. And
[15:27] you probably know what a skill is.
[15:29] They've been blowing up all over the
[15:30] internet the past few months. It's
[15:32] really like the main way to extend cloud
[15:34] code right now with new workflows and
[15:36] capabilities. And so like this is an
[15:39] example of a skill right here for adding
[15:40] API routes in this codebase. Really a
[15:43] skill is some kind of set of steps, some
[15:45] kind of process reusable prompt that you
[15:48] have for clawed code. And these are
[15:50] really important in large code bases
[15:52] because you're going to have dozens or
[15:54] maybe even hundreds of task types. Like
[15:56] this would apply to a task type of
[15:58] building an API endpoint. And so not all
[16:02] expertise needs to be present in every
[16:04] session which is the same reason why we
[16:06] have different claw. MD files in
[16:08] subdirectories which there is definitely
[16:10] some overlap here that I'll talk about
[16:11] in a second. And so skill solve this
[16:14] through progressive disclosure. So we're
[16:15] offloading specialized workflows and
[16:18] domain knowledge and we load it when we
[16:20] actually need it. So that way we're not
[16:22] bringing in prompting and workflows for
[16:24] things that don't apply to the current
[16:26] task at hand. And so when we define a
[16:30] skill we have the name and the
[16:31] description. The description is what is
[16:33] given to the coding agent right away.
[16:34] And if it decides like, okay, based on
[16:36] the description, I should use this
[16:38] skill, then it'll read the full skill.md
[16:41] file. I've talked about skills a lot on
[16:43] my channel already. But the parameter
[16:45] that most people don't know about, and
[16:47] this is what Anthropic talks about right
[16:49] here, we can make it so that skills can
[16:52] be scoped to specific paths. So they
[16:55] only activate in relevant parts of the
[16:57] codebase. Like we know that this process
[17:00] for adding API routes that we want to be
[17:02] very repeatable. It only applies when
[17:04] we're going to be reading and editing
[17:05] files in the API services directory. And
[17:08] so we can scope it there. Really, really
[17:10] powerful. It's a way to basically
[17:12] enforce that like when we touch this
[17:14] part of the codebase, we're going to
[17:16] bring this convention, this workflow
[17:18] into the session context. And so like I
[17:21] said, there is a little bit of overlap
[17:23] here with that and the subdirectory
[17:25] claw. MD files, right? like we're
[17:27] loading this in only when we work here.
[17:29] Same thing when we operate in here,
[17:31] we're also going to read this claw.md.
[17:34] The distinction that I like to make is
[17:35] that global rules are your conventions.
[17:38] It's the rules that you need to follow.
[17:39] Like every route is registered here, for
[17:42] example. Your skills are the workflows.
[17:45] So, we have rules and we have workflows.
[17:48] So, that distinguishment kind of helps
[17:50] me understand the overlap. But really
[17:52] for a lot of these sorts of conventions,
[17:55] you can kind of do it as a skill or a
[17:56] claw.md. The more important thing here
[17:58] is we just want to scope these
[18:00] conventions and rules to the part of the
[18:02] codebase where they actually matter. So
[18:04] we're not overwhelming our coding agent
[18:06] with context it doesn't care about. So
[18:08] Anthropic talks about plugins next, but
[18:10] I'm going to cover that at the end
[18:11] because I'll show you how to use my
[18:13] plugin to incorporate all these ideas in
[18:15] your own codebase. So let's move on to
[18:17] talk about language server protocols.
[18:20] I'm excited for this because I just
[18:22] started incorporating this into my own
[18:24] cloud code ecosystem. It's really
[18:26] powerful. Essentially, you give Claude
[18:28] the same navigation that a developer has
[18:31] in their IDE. And a lot of bigger
[18:33] companies especially build own custom
[18:35] LSPs to really help Claude navigate
[18:37] through their codebase effectively. And
[18:39] so an LSP is something that is really
[18:42] built into any IDE by default. It's the
[18:44] kind of thing that allows you to know
[18:46] like in VS Code, I can control-click
[18:48] here to immediately navigate to the
[18:50] definition for the class that I used in
[18:52] this other file. So that kind of like
[18:54] type hinting and navigation and
[18:56] highlighting like all that is an LSP.
[18:59] And so essentially with an MCP server,
[19:03] we can give cloud code this exact
[19:05] functionality that we as the engineers
[19:07] have in our IDE to make it so that we
[19:10] have better search capabilities than
[19:12] just GP by itself or can complement some
[19:14] of the tools like GP that are built into
[19:16] cloud code natively just through the CLI
[19:19] commands that it has. And so what I
[19:22] built here, I'm actually kind of
[19:22] knocking two birds with one stone
[19:24] because they talk about LSP and then
[19:26] talk about MCP servers as a way to
[19:28] extend everything is I built a local MCP
[19:32] server that comes with this codebase. It
[19:34] comes with the plugin that I'll cover in
[19:36] a little bit as well that gives Cloud
[19:38] Code some new codebase search
[19:40] capabilities. And so take a look at
[19:42] this. I'm going to go into a new Cloud
[19:45] session here. If I do SLMCP, you can see
[19:47] that I have the codebase search enabled.
[19:49] There are three tools here to complement
[19:52] the search capabilities that I already
[19:53] have. And so I'm going to paste in a
[19:55] prompt find every place that monthly
[19:57] total sense is referenced in this repo.
[19:59] And I know that's like oddly specific,
[20:01] but that's the point is we need
[20:02] something very specific to search for
[20:04] here. And I'm telling it not to use GP
[20:06] just for the sake of the demo. I'm
[20:08] telling it to use a symbol level
[20:10] approach. And that's going to key in
[20:11] that it needs to leverage the MCP server
[20:14] that I built here that leverages the
[20:16] language server protocol. So, it's able
[20:18] to do more intelligent searches that it
[20:20] might figure out it needs to if I don't
[20:22] tell it to not use GP or you could just,
[20:24] you know, build in some instructions in
[20:25] your global rules for how you want to
[20:27] use these searches. But you can see here
[20:29] that it used my whereas and find
[20:31] references tools in my custom MCP
[20:34] server. And so here are the results. We
[20:36] have one definition and two references.
[20:38] Pretty cool. So I I know that like I'm
[20:40] talking about complex code bases here,
[20:42] but my demo is kind of simple in the
[20:44] end, but I kind of have to have that
[20:46] balance there of like a somewhat
[20:48] complicated codebase, but still it has
[20:50] to be easy to like parse through and
[20:52] show the results here. But that's an
[20:54] example of using an MCP server to expose
[20:57] a language server protocol. And really
[21:00] for massive code bases once you get like
[21:02] into the six digits for lines of code
[21:05] you need something like this because
[21:07] Grep by itself is going to be slow and
[21:09] really token inefficient as you're
[21:11] trying to navigate through a codebase.
[21:13] This is a lot more of a directed search
[21:16] looking for things like the definitions
[21:18] and references for things like classes
[21:20] and variables. So that's a quick
[21:22] overview of LSP and MCP and how I use
[21:25] them together. You got to have some kind
[21:27] of harness to give better search
[21:29] capability to cla code when you're
[21:31] working in larger code bases. And really
[21:33] they operate like skills just use
[21:35] sporadically throughout your session. So
[21:37] like with skills we're loading in
[21:38] instructions when we need those
[21:40] conventions or workflows whatever LSP
[21:42] whenever we need to perform those
[21:44] searches to find definitions references
[21:46] things like that we'll call upon the
[21:47] tools. MCP pretty similar, right? Like
[21:50] we need to perform a search, take some
[21:51] kind of external action. We call upon
[21:54] one or multiple tools for an MCP server
[21:56] at that time. Now, the last part of the
[21:59] AI layer that we still have to cover is
[22:01] sub aents. But this one's nice and
[22:02] simple. The the advice anthropic has
[22:04] here is simple, but still really
[22:06] powerful. We want to use sub aents to
[22:08] split exploration from editing. So the
[22:12] idea with a sub agent is that we send in
[22:15] a task like we wanted to search the web
[22:17] for you know best practices for this
[22:19] kind of architecture or maybe to do some
[22:22] kind of codebase exploration to find the
[22:24] part of the codebase to focus on. We
[22:26] send in a task and it runs with its own
[22:29] context window. It does all the analysis
[22:32] it needs to and then it returns a
[22:34] summary back to our primary cloud code
[22:37] session to reason about an action on.
[22:40] And these kind of exploration tasks that
[22:43] we want to give to a sub agent, you can
[22:45] imagine them getting to hundreds of
[22:46] thousands of tokens. So if we're not
[22:48] using a sub agent and we have our
[22:50] primary cloud code session do that web
[22:52] research or codebase exploration, by the
[22:54] time we get to the actual editing, we're
[22:56] already going to have this extremely
[22:57] bloated context window. That's why we
[22:59] want to dispatch the work to the sub
[23:02] agents. Especially because with
[23:03] exploration, usually all we need is that
[23:05] summary back, right? Like here are the
[23:07] recommendations for the tech stack.
[23:08] here's a part of the codebase we're
[23:10] going to have to address based on this
[23:11] Jira ticket. Like that's the kind of
[23:13] thing that you task a sub agent with.
[23:15] And so I don't actually have that much
[23:16] of a demo here for sub agents because I
[23:18] use them liberally like all the time
[23:20] especially at start of the conversation.
[23:22] I'll say something like I want you to
[23:24] spin up three sub agents here. One to
[23:26] research the database, one the back end,
[23:28] one the front end. Help me figure out
[23:30] how I can add in authentication. I don't
[23:32] know. I'm just kind of throwing off
[23:34] something off the cuff here. But you
[23:35] have sub agents built into a lot of
[23:37] these coding agents now like cloud code
[23:39] and codeex. And so you don't even have
[23:40] to define your own custom sub aents like
[23:43] a lot of people did before. You just
[23:44] send off a request like this. And now
[23:45] it's just going to use the explorer sub
[23:48] agent that we have built into cloud
[23:50] code. And so it takes care of that whole
[23:52] like dispatch getting the summary back
[23:53] and everything. All right. So the rest
[23:56] of the article that we haven't covered
[23:57] yet is really covering a lot of the
[23:59] strategies that I already hit on like
[24:01] writing LSP servers so cloud can search
[24:03] by symbol not by string. talking about
[24:05] actively maintaining the claw.md file.
[24:07] So this is where the stop hook comes in
[24:09] to make those recommendations as we're
[24:11] operating with claude code. The other
[24:14] thing that I want to hit on here is the
[24:16] plugin that I have for you. So if you go
[24:18] to the read me for this demo repo that
[24:21] I'll link to in the description, I have
[24:23] instructions for taking this to your own
[24:25] codebase. Now, obviously, some of the
[24:27] things like the claw.mds and the
[24:29] subdirectories are specific to me, but
[24:31] this plugin is going to give you the
[24:32] self-improving stop hook, the explorer
[24:35] sub aent, so it's more of like a custom
[24:36] sub agent that I built that you can use,
[24:38] and it's going to give you the codebase
[24:40] search MCP server with that LSP. So, you
[24:43] have that whole searching harness. And
[24:45] then I'm going to give you a more
[24:46] generic skill that you can use in as an
[24:48] example that shows what it looks like to
[24:51] use that path parameter to scope a skill
[24:54] to a certain subdirectory. So just kind
[24:56] of consider this plugin a starting point
[24:58] if you want to like really quickly pull
[25:00] in these things to experiment on your
[25:01] own codebase. You can install this
[25:03] plugin on any codebase, even one that
[25:05] you already have built out with its own
[25:07] AI layer already. So all you have to do
[25:09] is slash in cloud code /plugin
[25:12] marketplace add and then give the path
[25:14] to the repository. So you still have to
[25:16] clone this repo locally because I don't
[25:18] have this hosted in npm. So you give the
[25:20] path and then make sure you add the
[25:21] tooling folder at the end. And then you
[25:23] just do plug-in install helpline AI
[25:25] layer at helpline tooling. Then you go
[25:27] through the whole installation process
[25:29] here and then boom, it'll install all
[25:30] these things for you to start playing
[25:32] around with. So that's one way to do it.
[25:34] I just wanted to add a plugin to make it
[25:35] really convenient. The other way to get
[25:37] started with a lot of the ideas that I
[25:39] have here, aside from, you know, reading
[25:41] the anthropic blog post, is just to
[25:43] clone this repository, point your Claude
[25:46] code at it, you know, like copy this
[25:48] directory, you know, rightclick, copy
[25:50] path, give this to Claude Code, and say,
[25:52] "Hey, these are a bunch of cool
[25:53] strategies Cole shared with me for
[25:55] working with complex code bases. Help me
[25:57] understand how they work and how I can
[25:59] incorporate it for my codebase." That's
[26:01] always the easiest way to really take
[26:03] any repo these days is just give it to
[26:04] cloud code and have it uh help you
[26:07] understand it and apply it. So that'd be
[26:09] my recommendation for getting started
[26:11] here. So I hope that you found these
[26:12] strategies really useful that you can
[26:14] apply them right away to your larger
[26:16] code bases. Even if you had some of
[26:18] these things incorporated already, I
[26:20] hope there are some good golden nuggets
[26:21] for you. And so the last thing that I
[26:23] want to end on is talking about some
[26:25] really good advice that Enthropic also
[26:27] gives at the bottom of their article
[26:29] here. It's all about assigning ownership
[26:31] for cloud code management and adoption.
[26:34] And I've been around a lot of companies
[26:36] as I've done my consultings and
[26:37] trainings. I know this is really good
[26:39] advice. Essentially, what they're saying
[26:40] here is to have a an individual or more
[26:43] likely a smaller team to champion the
[26:46] initial buildout of the AI layer for
[26:48] your organization.
[26:50] And so what that looks like is you start
[26:52] with a quiet investment period. you have
[26:54] a couple of people that build out the
[26:56] the rules and skills and the LSP and the
[26:59] MCP servers, the whole AI layer for the
[27:01] organization and then roll it out to
[27:03] people over time. And the power of this
[27:06] is you get to create something that's
[27:09] really foundational for everyone to
[27:11] adopt together and then people can get
[27:13] more consistent results with Cloud Code
[27:15] or whatever coding agent faster so that
[27:17] they're not disappointed when they first
[27:19] use the tool. You want to avoid people
[27:21] being really disappointed when they
[27:22] first use it because they don't have an
[27:23] AI layer and you want to avoid everyone
[27:26] evolving their own separate AI layers
[27:28] when really you want a standard for the
[27:30] organization. So really really good
[27:31] advice that they have here. This is also
[27:33] something that I help with and so I do
[27:36] offer enterprise trainings where I help
[27:38] you build up the AI layer, understand
[27:40] the core methodologies for AI coding and
[27:42] create that standard for your adoption
[27:45] of coding agent tools like cloud code.
[27:47] So definitely I got my email in my bio.
[27:50] Reach out to me if you're interested in
[27:51] that. Otherwise, I hope that these
[27:52] strategies were useful for you. I
[27:55] appreciate you going through everything
[27:56] here. Let me know if you have any
[27:58] questions in the comments below.
[27:59] Otherwise, if you appreciate this video
[28:01] and you're looking forward to more
[28:02] things on AI coding and cloud code, I
[28:05] would really appreciate a like and a
[28:06] subscribe. And with that, I will see you
[28:08] in the next video.
