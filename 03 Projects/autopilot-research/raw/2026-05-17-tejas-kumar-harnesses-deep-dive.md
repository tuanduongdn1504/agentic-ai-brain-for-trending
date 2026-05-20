---
source: yt-dlp-only
url: https://www.youtube.com/watch?v=C_GG5g38vLU
title: Harnesses in AI: A Deep Dive
speaker: Tejas Kumar, IBM
channel: AI Engineer (@aiDotEngineer)
upload_date: 2026-05-17
duration: 20:26
view_count: 38755
fetched: 2026-05-20
path: 5
notes: AI Engineer 2026 conference talk. Live-demo + first-principles deep dive. Defines agent harness as "everything around the model that gives it grounding in reality"; demonstrates by building a Hacker News upvote agent with GPT-3.5 Turbo (deliberately weak model) and showing prompt-untouched outcome change via incremental harness primitives.
---

# Harnesses in AI: A Deep Dive — Tejas Kumar (IBM)

> Verbatim auto-caption transcript with `[MM:SS]` timestamps. Cleaned from VTT via `/tmp/clean_vtt.awk` (strip inline `<c>`+per-word timestamp tags, dedupe consecutive identical caption frames). 607 segments / ~3.4K words.

[00:14] >> Hello everybody.

[00:16] Everybody's head turned up. Hello, hi.

[00:19] How was lunch? Was it good?

[00:21] You didn't like it, no?

[00:23] It's like

[00:24] British food. Anyway, hi. I'm Tejas. I'm

[00:27] I'll be your first speaker this

[00:28] afternoon. Tejas, that's pronounced like

[00:31] Don't worry, I'm not

[00:32] Hopefully my my joy in AI is and I've

[00:34] had the privilege of working at a number

[00:36] of different places over my career in

[00:37] one form or the other. It's just been an

[00:39] absolute joy to learn from the best.

[00:41] Today, I'm a AI developer advocate at

[00:45] where we we do things with AI, believe

[00:47] or not. We train frontier models, we

[00:48] build harnesses. It's really it's a fun

[00:51] lab to work in.

[00:52] But that's not what I'm here to talk to

[00:53] you about today. Today, I'm here to talk

[00:55] to you about AI harnesses. AI harnesses.

[00:58] Before I move forward, I would love to

[01:00] just have a show of hands.

[01:02] How many of you are like confident in

[01:04] your understanding of AI harnesses? Like

[01:05] you're like I could present this on

[01:07] stage today.

[01:08] Look around. Look around. No, seriously,

[01:10] look around. That's why we're doing this

[01:11] talk. Okay, this is my hope. I want you

[01:13] to If I ask you this at the end of the

[01:15] talk, right? I want you to be like, oh,

[01:16] I I I get it now. That's the whole

[01:18] point. I have literally nothing to gain

[01:20] from this other than I I shared

[01:21] knowledge, okay? Because also this term

[01:24] is kind of everywhere. You may have

[01:25] heard it used like 52,000 times today.

[01:28] And it means different things to

[01:30] different people cuz like in the machine

[01:31] learning world, it means like a

[01:33] glorified test suite for machine

[01:34] learning models. But in the AI in the AI

[01:36] world, it means something different. And

[01:37] so today, we're going to understand this

[01:39] in detail. It's a deep dive, but it's 18

[01:41] minutes long. So let's let's move

[01:42] forward. Um

[01:44] I want to start by talking about why

[01:45] harness. Like why do we use harnesses?

[01:47] And the reason for this is because we

[01:49] pay rent to companies that give us

[01:53] compute, give us inference, give us

[01:54] tokens in return. Some of you maybe work

[01:57] for companies that have frontier models

[01:58] like Anthropic or Google or whatever and

[02:01] you maybe What was the term? Token

[02:02] billionaires, yeah?

[02:05] I'm not that. I am maybe with Watson

[02:07] models, but but the vast majority of us

[02:09] aren't token billionaires. We we pay

[02:11] rent. We literally $20 a month for

[02:13] Claude Pro. And then you get a context

[02:15] window that's limited and you get like,

[02:17] you know, you you don't get the full

[02:18] hog, so to speak. And the model you rent

[02:22] is is a black box. Like they could at

[02:24] any time, I'm not saying they do, but

[02:25] they could if Opus is somehow not

[02:27] available, they could serve you Sonnet

[02:29] even though it says Opus. You would

[02:30] never know, right?

[02:32] And so it's just a big There's too many

[02:34] variables that we cannot control. So why

[02:36] harness? Because the name of the game

[02:39] with harness is reliability. Um

[02:42] I really hope I'm not supposed to stand

[02:44] in front of this white line and then I'm

[02:46] just not in the camera. Anyway,

[02:49] It's reliability. It's it's making sure

[02:51] that the agents we build do what they

[02:53] do, period. Irrespective of the black

[02:55] box model, irrespective of the of the

[02:57] the thing we rent and so on, okay? Now

[02:59] that we understand why harness, let's

[03:01] talk about what a harness even is from

[03:03] first principles. Like let's let's take

[03:05] it all the way back to harnesses that we

[03:06] know and understand. If you've ever, you

[03:09] know, climbed a mountain or something or

[03:11] you've seen someone This is a harness.

[03:13] It's like mountain climbers literally

[03:15] will like harness themselves to what? To

[03:17] a mountain because it's stable. And they

[03:20] can't go off the rails, literally.

[03:22] They they

[03:23] anchor themselves in something stable so

[03:26] that they can't drift too far.

[03:28] Okay, that's that's what a harness is by

[03:30] design. When you have any dog owners

[03:32] here? You have dogs? You you walk your

[03:34] dog on a harness, okay? That's why?

[03:36] Because your dog doesn't go and bankrupt

[03:38] you with tokens. Okay?

[03:41] That's what a harness is.

[03:43] But the problem is if we think about

[03:45] what harness, there's really two types.

[03:47] There's one from the machine learning

[03:49] world, which as I mentioned is kind of

[03:50] like a test suite and a test runner.

[03:52] You would give a model some inputs and

[03:54] you see the quality of the outputs.

[03:55] That's not This is not ML engineer

[03:57] Europe. We're going to talk today about

[03:59] the agent harness that is common in AI

[04:01] engineering. Okay, so what what is an

[04:03] agent harness?

[04:05] An agent harness and and this is kind of

[04:07] the money shot here. The agent harness

[04:10] is I'm not making money off this. It's

[04:11] just an expression. The agent harness is

[04:14] everything around the model that gives

[04:17] it grounding in reality. It's literally

[04:19] the thing that ties it to a stable

[04:21] environment, okay? An agent So Claude

[04:23] code, for example, can be considered an

[04:25] agent harness. And some of you would

[04:26] say, oh, no, it's a coding agent.

[04:27] Absolutely, it's a coding agent. But

[04:29] it's a harnessed coding agent. An agent

[04:32] harness has more or less the same

[04:34] typical suspects, moving parts. Number

[04:36] one, it's got

[04:38] a tool registry. Almost like so Claude

[04:41] code, cursor, codex, they have tools to

[04:43] read from the file system, to write, to

[04:45] execute bash commands, right? They have

[04:46] a tool registry. They have a model and

[04:49] some of them allow you to choose a

[04:50] model, some of them allow you to not.

[04:51] They have a model. They have primitives

[04:53] for managing context. Almost every

[04:57] harnessed agent runtime today will

[05:00] compact its own context, right? That's

[05:02] that's that's the job of the harness.

[05:04] Guardrails are another part of a

[05:06] harness. For example, max steps. Anyone

[05:08] using max steps? Do not do more than

[05:10] five tool calls. That's a guardrail. And

[05:12] so if if you do that, you just kill the

[05:14] kill the run, right?

[05:16] An agent loop is another part of an

[05:18] agent harness, which is crazy. This is

[05:19] what some people I've spoken to

[05:21] preparing this talk

[05:22] will say,

[05:23] wait, isn't a harness just the agent

[05:25] loop? No, it's the stuff around the

[05:27] agent loop. In fact, it could be a loop

[05:30] around your agent loop. It could be an

[05:31] NM loop. And we'll look at that a little

[05:33] bit in some code. And then finally,

[05:34] there's a verify step. This is, for

[05:37] example, in a coding coding agent, after

[05:39] the work is done, a verify step would

[05:41] be, hey, let's let's run lint, let's run

[05:44] tests, let's make sure nothing broke,

[05:45] right? So almost every I'll use code

[05:48] coding agents as an example, but you

[05:49] could have a harness for anything. And

[05:51] it's it's amazing cuz it really grounds

[05:53] black box models in a stable environment

[05:56] that you control, okay? I'd like to show

[06:00] a demo. And what we're going to do

[06:01] together is we're going to build a

[06:02] harness, a bare bone baby's first

[06:04] harness. Let's call it a poor man's AI

[06:06] harness together so we understand from

[06:08] first principles how this works. We're

[06:10] going to build a computer use agent that

[06:12] has a job. The job is go to Hacker News

[06:14] and upvote the first post, okay? It's a

[06:16] computer It's a browser use agent. We're

[06:19] going to use a really bad model

[06:21] intentionally. We're using GPT-3.5

[06:23] Turbo, which is like 2023, right? But

[06:27] we're going to harness it so that it can

[06:28] actually do the job. And we're going to

[06:30] save money. So let's I've spoken too

[06:32] much. Let's just get into the demo.

[06:37] And and so let's Welcome to my project.

[06:39] This is my project. Hello everybody.

[06:40] This is the entry point. Can you see

[06:42] that? Is it too

[06:44] Yeah? You want it bigger?

[06:46] Let's do bigger. Okay. So this is not

[06:48] Actually, this room is too bright. Let's

[06:50] do light mode. It's I It's not my

[06:52] nature, but sometimes. That's better,

[06:55] yeah? Okay. So we have we have a model

[06:58] and we're

[06:58] trying an old LG Sorry.

[07:03] We shouldn't have seen that. No, we'll

[07:05] we'll try an old model. And this is the

[07:06] prompt. This is the This is the task.

[07:09] This is literally my prompt. Upvote a

[07:10] story I just described it. For the

[07:12] purpose of this demo, we will not change

[07:15] the prompt at all.

[07:17] Because a lot of us think, hey, my agent

[07:18] is not doing what it's supposed to do,

[07:20] so I just need to prompt it harder,

[07:22] right? That's not always true. I need to

[07:24] change the system prompt. We're not

[07:25] going to touch any prompts here. We're

[07:26] just going to build a harness and the

[07:28] outcome will change.

[07:29] We we log some things to the console and

[07:31] then we start a browser session. Okay,

[07:33] what's a browser session? It's literally

[07:34] just Playwright. Not Playwright MCP,

[07:36] like Playwright Playwright. Where this

[07:37] is just a class I made with an open

[07:39] method that launches Chromium and gets a

[07:42] context and makes a page. And then

[07:43] navigate We're just literally calling

[07:44] the Playwright functions, yeah? This is

[07:46] This is just traditional engineering. So

[07:49] we create a session, we open the

[07:51] session, meaning a browser window in a

[07:52] context. And then we create our tools

[07:54] and we give that browser session to the

[07:56] tools. And we create a context and we

[07:58] give the task, meaning the prompt here,

[08:01] to the context. Now, create tools is

[08:03] literally what it sounds like. It's

[08:05] here. There's just some types and create

[08:07] tools is a function that takes a browser

[08:08] session and gives you like tools. And

[08:11] these tools are not I didn't invent

[08:12] this. This is from OpenAI's SDK, okay?

[08:15] So you have the name, the description

[08:17] parameters, and execute, the way you

[08:18] actually call the tool in your runtime.

[08:20] And and there's just tools for I made

[08:22] this. It's very easy. Um

[08:24] So that's my tools. And then create

[08:25] context, you may think, whoa, context

[08:27] engineering. Absolutely not. It's This

[08:29] is my context. There's nothing here.

[08:31] It's just a system prompt.

[08:33] Literally, the most basic system prompt

[08:35] and the user's task. This is basic

[08:37] basic. And then we have run loop, which

[08:40] is just running the agent in a loop. So

[08:41] what it's doing here, we can actually

[08:43] just look at this, too.

[08:44] While true, so it is an agent loop. And

[08:47] we get a response from the agent and we

[08:49] see if the response says stop, meaning

[08:51] if the LLM says, I'm done, then we

[08:54] return the value.

[08:55] If we get any other response, we don't

[08:58] do anything except

[09:00] add these events into a trace. So we

[09:02] just push history into a big list of

[09:03] history. Does that make sense? And so

[09:05] that's all we're doing here. This is

[09:06] just a loop where we just collect events

[09:08] until we're done, okay? So this is super

[09:11] basic. Now let's see how it works. So

[09:12] I'm going to come over here and I'm

[09:14] going to do Are you okay, sir? Do you

[09:16] need water? I'm going to

[09:17] npm run agent. Um And so it's going to

[09:21] open Chromium. It's going to Okay,

[09:23] Hacker News, so far so good. Click

[09:24] upvote. Oh, no. So we we hit a login

[09:27] screen and then it kind of panicked and

[09:28] crashed. But look, it it lies. You see

[09:33] Um this is a problem. And so what's the

[09:35] solution? Prompt it harder? No. Change

[09:38] the system prompt. Always login with

[09:39] these credentials included in the system

[09:41] prompt. No.

[09:43] So how do we then solve this? And look,

[09:45] we because of my logging, we can

[09:46] actually see it just clicks the upvote

[09:49] button and then considers it a success.

[09:51] It doesn't verify. This is the job of a

[09:53] harness, okay? So now incrementally,

[09:55] we're going to slowly start building a

[09:57] harness. Um

[09:58] And so, let's just move I'm not going to

[10:01] write code here. I'm not going to live

[10:02] code because we don't write code

[10:03] anymore. We inspect diffs.

[10:05] Right? Anyone write code by hand? You

[10:07] don't Maybe actually you do belong here.

[10:08] Anyway, so um

[10:11] I'm kidding. So, this is um

[10:13] This is the first change we're going to

[10:14] make. This was our index file.

[10:16] And we have this run loop that I showed

[10:18] you, but now we're going to add one

[10:20] thing to it, which is default

[10:21] guardrails. We're going to create some

[10:22] guardrails, okay?

[10:24] Um what do our guardrails look like?

[10:26] Well, let's go and look at it in the

[10:27] editor um with guardrails over here. And

[10:31] so, we have some types, but these are

[10:32] our guardrails. We have two. Max

[10:33] iterations, meaning if you do more than

[10:35] six steps, I'mma kill you.

[10:36] And max messages, meaning if you have

[10:38] more than this many messages, I will

[10:39] compress the context. These are just

[10:41] guardrails, okay? A little utility to

[10:43] combine them, and we just we can compose

[10:45] them here. We could do like as many as

[10:46] we want. So, now

[10:49] let's go back to our changes. That's the

[10:51] guardrails. We if we go back to the

[10:53] agent loop we actually use the

[10:55] guardrails here in this diff. And so, we

[10:57] include the guardrail functions, and we

[10:59] can see that here what we're doing is

[11:01] we're checking how many messages have we

[11:03] accumulated, and we just like trim the

[11:05] context if it's too much. Um but what I

[11:08] did want to show you is here at the end

[11:10] um we we push context size, which is

[11:13] some more metadata about what we've done

[11:14] with our guardrails, okay?

[11:16] Um our context compressor is extremely

[11:19] basic and extremely naive. This is what

[11:21] it does. Um let me actually open this

[11:23] with syntax highlighting to spare Um

[11:26] this is what it does. So, what we're

[11:27] doing is if we always keep the system

[11:29] prompt and the user prompt and the most

[11:31] recent two messages. So, if the

[11:34] guardrail is triggered, we always remove

[11:36] everything after the system prompt and

[11:37] the user prompt in the middle, and we

[11:39] keep the last two messages. This is

[11:40] super naive. Don't do There's better

[11:42] ways, but this is where babies first.

[11:44] We're We're getting there.

[11:45] So, we we're starting to have a harness,

[11:47] but it's not called a harness, but this

[11:49] is really like

[11:50] a pregnant harness. Like it's almost

[11:52] born, okay? And so, what we're going to

[11:54] do is let's just call it a harness now.

[11:56] So, I'm going to show you another diff

[11:58] where we

[11:59] Here, check this out. Index, we've

[12:01] deleted almost everything.

[12:02] Um and we've moved it into this file

[12:04] called harness. Let's go look at our

[12:06] entry point now.

[12:07] It index, it's it's all gone. So, the

[12:09] prompt is there. But this is it's like

[12:12] 19 lines of code, and we just have run

[12:14] harness. We've taken all the logic from

[12:15] here and hidden it in a function called

[12:17] run harness. And as you would expect,

[12:18] run harness does exactly the same thing

[12:20] as we did in the index, okay? Nothing

[12:22] new is here except maybe like a print

[12:23] function, which is just console log. Is

[12:25] this clear so far? Yeah, we just moved

[12:26] stuff. Now that we have something called

[12:28] a harness, we can actually use it.

[12:31] And let's solve the problem of lying

[12:33] first before we solve the problem of

[12:35] logging in as me. Yeah, because it says

[12:37] I I upvoted, it did not. I want to know.

[12:40] So, what we're going to do is we're

[12:41] going to add some guardrails and and

[12:43] have it tell the truth. Like if you

[12:44] failed, tell me the truth. Um

[12:47] how might we do that? Well, we'll check

[12:49] it out here. So,

[12:51] many many things changed. Um

[12:54] Or not. I don't know. Hang on a second.

[12:59] Yeah, okay.

[13:00] Did Many many things changed. So, we run

[13:02] harness and we added a third argument

[13:04] here, which is a verify step and max

[13:06] attempts. Max attempts goes to our

[13:07] guardrail. So, if if you took more than

[13:08] three tries to do this, just give up.

[13:11] And if we go to the harness, we added a

[13:13] lot of things um that are just manual

[13:16] code. This is not different prompt. This

[13:17] is my logic. Um the main logic is run

[13:21] harness no longer wraps over the code we

[13:23] moved, but we moved that to a different

[13:24] function called

[13:26] run harness attempt. So, if we if we

[13:30] come to run harness Let's go here. I

[13:33] need to check the branch out, sorry.

[13:35] Yeah. So, now if we go to run harness

[13:37] attempt, we'll collapse this. I'll

[13:38] collapse this.

[13:40] I'll collapse all of these. And if we go

[13:42] to run harness attempt, now this is the

[13:43] same thing from our index. We just moved

[13:45] it into a function called run harness

[13:46] attempt because our main run harness is

[13:49] just a loop that runs no more than three

[13:51] times, okay? Is this clear? So, we're

[13:52] just enforcing the max steps, but at the

[13:54] harness level for safety. Um

[13:57] then we have run harness attempt that

[13:59] calls it. We have this function called

[14:01] verify successful upvote. I wrote this.

[14:04] This is deterministic. That's what I

[14:05] want to show you. What does this do?

[14:07] Well, we see if You remember we were

[14:10] tracing in the agent loop, we're just

[14:12] adding history events. So, we reflect on

[14:14] that, and we see if there was a browser

[14:17] on the upvote and if it's successful,

[14:20] but really successful, then we say true.

[14:22] But there's a huge butt here, which is

[14:24] we have now cases for failed login. If

[14:27] there's a tool named harness auto login,

[14:29] and if the message starts with failed

[14:31] then we return early and we say no no,

[14:32] this failed. We're We're removing the

[14:34] lie, okay? Similarly, unrecovered login

[14:37] redirect. We look over our agent loops

[14:39] tools that we've been pushing into.

[14:41] Um and if we see that the harness auto

[14:45] login didn't run

[14:46] and now we're on the page that is the

[14:48] login URL, then again, we just fail.

[14:51] Um and so, we're what we're doing is

[14:53] we're just adding like if this happened,

[14:54] if this happened, you just just fail.

[14:56] Return early. Is this clear? This is

[14:57] what a harness does. And so, let's run

[14:59] this now with the harness.

[15:01] Uh npm run agent.

[15:04] now it's going to go on Hacker News, and

[15:05] we're going to repeat the same cycle.

[15:08] Okay, it's going to come here, and now

[15:09] it's still failed, but look, it stopped

[15:11] lying because our harness checks the

[15:14] tool history and actually sees what

[15:15] happened. This is what a harness is

[15:17] supposed to do. Great. This is already

[15:19] like half the battle won because step

[15:22] one to solving a problem is admitting

[15:23] you have one, okay?

[15:25] Test-driven development vibes. So, now

[15:27] that we we're failing correctly, we can

[15:30] succeed. And I'd like to show you that

[15:32] in the last diff, and then we'll finish

[15:33] the talk here. So, number four.

[15:36] Um we have a whole new function. It's

[15:37] called login handler. Uh I'll add some

[15:40] syntax highlighting here so you don't go

[15:42] blind. Uh but here, create login

[15:44] handler. This is This is all it does. It

[15:45] runs every agent loop just before we

[15:47] push to the traces, and it This is what

[15:49] it do It checks the browser session's

[15:50] current URL.

[15:52] And if we're not on a login page, it

[15:53] just says cool, I don't I return I have

[15:55] nothing for you. This computationally is

[15:57] not costly at all, right? If you're not

[15:58] on the login page, but if you are on the

[16:00] login page

[16:01] then it we fill in

[16:03] a temporary This can be an environment

[16:05] variable. It can be secure, you get the

[16:07] idea. But we fill in credentials and

[16:08] submit the button programmatically from

[16:10] the harness, not from the agent,

[16:13] deterministically and securely because

[16:15] this file has access to any secrets I

[16:17] want it to, right? And so, this How How

[16:19] is this called? Well, this is called in

[16:21] the agent loop. So, if we go back to our

[16:23] agent loop and notice we were pushing

[16:25] traces, yeah? This is where we push the

[16:28] Just before, if we have a login handler

[16:31] we call the login handler just before

[16:33] this in the agent loop. What does the

[16:35] login handler do? Well, if we're not on

[16:36] the login page, it does nothing.

[16:38] If we are on a login page, then it

[16:40] quickly will inject credentials and

[16:41] submit the form and then take you back.

[16:43] It will also add, as we can see here, it

[16:44] pushes a message into the queue saying,

[16:47] "Hey, I'm the harness. I logged in.

[16:49] You're good now." Is this clear? Yeah?

[16:51] So, the the harness is is is literally

[16:53] harnessing the agent to something

[16:55] stable, something deterministic. That's

[16:57] what it's for, okay?

[16:58] Let's run this now and see what happens.

[17:01] So, npm run agent.

[17:03] It's going to open Hacker News, and when

[17:05] it gets to the login, now that harness

[17:06] step, it logged in and it upvoted the

[17:08] first one, and it closed.

[17:11] Amazing. So, successfully upvoted a

[17:14] little snitch for nilux, uh rank two, uh

[17:16] succeeded after six iterations, and I

[17:18] can click this and go into Hacker News

[17:19] and actually see indeed it was upvoted,

[17:22] um and it I can unvote now, which means

[17:23] it was upvoted, right? So, um the agent

[17:26] used the computer, logged in as me with

[17:28] my harness that I just made here on

[17:29] stage. That's the purpose. Is this clear

[17:31] so far? Do you understand the role of a

[17:32] harness? Look at you nodding. This is

[17:34] music to my ears. Fantastic.

[17:37] Something to my eyes. I don't know the

[17:39] It's beauty to my eyes, kind of weird.

[17:40] We don't have a expression for that.

[17:42] Let's land the plane. I'm done. I think

[17:45] my work here is done. What does this

[17:47] look like in practice? Why Why do I care

[17:48] so much about harnesses? Because they

[17:50] run the world. Models are

[17:51] non-deterministic. And you want to do

[17:53] more with less. You want to use a cheap

[17:55] model. Use like Quinn or something, or

[17:57] even something smaller. Use GPT-OSS.

[17:59] It's free. And with a great harness, you

[18:01] can go very far. That's why. At IBM, we

[18:03] create a open-source project that we

[18:06] deploy in the enterprise that allows

[18:08] very large companies, huge companies, in

[18:10] their private like data-sensitive areas

[18:13] to perform rag operations on all kinds

[18:14] of things, teams, calls, and PDFs, and

[18:17] invoices. Um We We build It's called

[18:19] open rag, and it's it's rag I don't know

[18:21] if rag is cool or not anymore, but

[18:24] open rag has a hell of a harness that

[18:26] provides enterprise-level security to

[18:28] like asking questions with internal very

[18:30] very siloed data. And And that's kind of

[18:32] where the harness engineering comes in.

[18:33] So, let's summarize. We covered a lot of

[18:35] content. Was it a deep I think it was a

[18:37] deep dive. It was a deep dive in like 18

[18:38] minutes or so. Um

[18:40] we went pretty far. I

[18:42] It's not It should not be lost on you

[18:44] that I did not touch the prompt once.

[18:47] I did not change the system prompt. We

[18:48] just built a harness

[18:50] and the outcome radically changed. And

[18:52] of course, we can add secrets, we can

[18:53] add tokens. Um yeah, we did a lot. In

[18:56] the end, I hope you understand what a

[18:58] harness is, the value it can present,

[19:00] and how you can use it. What's next? Um

[19:03] Look, I

[19:04] I don't have a crystal ball like

[19:05] everyone else here, um but it's not lost

[19:08] on me that 2025 was the year of agents.

[19:11] Yes? Uh 2026

[19:13] is the year of harnesses, I'm pretty

[19:15] sure. Everybody How many times is this

[19:16] word used here? Um I think

[19:19] I would hope I think it'd be pretty cool

[19:20] if 2027 was the year of dynamic

[19:24] on-the-fly generated harnesses. How cool

[19:27] would that Like you tell an agent, "Hey,

[19:28] do this for me. Buy me a flight ticket."

[19:30] Whatever it may be. And then before

[19:32] doing the work, the agent creates a

[19:34] harness. This similar to plan mode. Any

[19:35] of you using plan mode? But But on

[19:37] steroids. The The agent creates an

[19:38] actual harness, self-aware. It knows,

[19:41] "Oh, I can maybe hallucinate here. I can

[19:42] maybe" Creates a harness, does the job,
[19:44] and returns back to you, guardrailed and

[19:46] everything. That is so cool. Dynamic

[19:48] on-the-fly harnesses. I would I I this

[19:50] is honestly the next logical step

[19:51] towards AGI, and I would love to see it.

[19:53] I don't know if this is just me being uh

[19:54] you know

[19:55] weird guy with ideas, but um I think

[19:57] that's kind of the direction. So, with

[19:59] that um I'm almost out of time. I would

[20:01] be really remiss if I didn't spend the

[20:02] last like 30 seconds saying thank you so

[20:04] much. The slides are on GitHub uh as uh

[20:06] am I uh and so I'd love to chat more.

[20:08] Thank you.
