---
source: yt-dlp (path 5 — operator-submitted single video)
topic: pocock-writing-great-skills
video_id: UNzCG3lw6O0
url: https://www.youtube.com/watch?v=UNzCG3lw6O0
title: "Building Great Agent Skills: The Missing Manual"
speaker: Matt Pocock
channel: AI Engineer (@aiDotEngineer)
event: AI Engineer World's Fair 2026 (June 29 – July 2, Moscone West, San Francisco) — pre-recorded/remote (speaker could not attend in person)
upload_date: 2026-06-29
duration: "20:43"
views_at_ingest: 102847
likes_at_ingest: 3556
captions: en (auto) → VTT dedupe → timestamped plain text
notebook_id: none
ingested: 2026-07-15
deliverable: report (wiki compile)
skill_repo: https://github.com/mattpocock/skills (Pattern #52; 170,613★ at ingest)
encoded_skill: skills/productivity/writing-great-skills/SKILL.md
---

# Building Great Agent Skills: The Missing Manual — Matt Pocock (AI Engineer World's Fair 2026)

**The talk's own description (from YouTube):**

> Let's discuss how to navigate "skill hell" by providing a structured framework for building high-quality agent skills. The Skill Checklist Framework:
> - **Trigger** (3:16–7:25): user-invoked vs model-invoked. Model-invoked = more flexible but more context load + unpredictability. User-invoked = more control but more cognitive load on the pilot.
> - **Structure** (7:29–11:53): two units — steps (procedures) + reference (supporting info). Keep SKILL.md minimal; move branching reference behind context pointers.
> - **Steering** (11:54–16:47): leading words (dense-meaning terms that guide reasoning traces); increase "legwork" per step by splitting complex processes into smaller skills that hide future steps.
> - **Pruning** (16:48–19:05): single source of truth; remove "sediment" (stale legacy material) + "no-ops" (instructions that don't change behavior).
>
> Skill: https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md

---

## Full transcript (auto-captions, deduped, [mm:ss])

[0:00] Hello friends, I was dearly hoping to be
[0:01] able to come to the Air Engineer World's
[0:03] Fair, but family matters have intruded
[0:06] and I'm not able to make it. However, I
[0:08] will not be leaving you empty-handed.
[0:09] I'm going to give you the talk that I
[0:11] would have given in San Francisco. This
[0:13] talk is called The Missing Manual, How
[0:15] to Write Great Skills, and I think that
[0:18] the ability to distinguish good skills
[0:20] from bad skills is only getting more
[0:22] important. As developers, we seem to be
[0:24] pretty talented at finding different
[0:25] forms of hell for us to go to. In like a
[0:29] few years ago, we had tutorial hell,
[0:31] which is where you would go into a bunch
[0:32] of tutorials trying to learn something,
[0:34] not be able to piece it together, and
[0:36] sort of just get into this cycle you
[0:38] couldn't get out of. We had framework
[0:41] hell, where every other 10 minutes there
[0:43] was a JavaScript framework being
[0:44] announced, and you know, you had to
[0:45] learn the hot new thing all the time.
[0:47] And now, I think we have another version
[0:49] of hell, which is skill hell. Skill hell
[0:52] is where you have all of these skills
[0:54] available, freely available, that you
[0:55] can download, contribute to, you can
[0:57] figure out on your own, but you don't
[0:59] really know how the pieces all work
[1:01] together. You can't tell a good skill
[1:03] from a bad skill. And this means that
[1:04] people are trying to piece together
[1:06] these frameworks, trying to try
[1:07] everything that's out there all at once.
[1:10] And they sort of can't, or rather, they
[1:12] don't get the results that the skills
[1:14] themselves promise. This is true at an
[1:15] individual level, but it's also true at
[1:17] an organization level, too.
[1:19] Organizations have no way or no
[1:21] understanding on how to build good
[1:23] skills, how to take their operating
[1:25] procedures and turn them into things
[1:27] that an agent can do. you don't do that,
[1:29] then it's hard to get the bounty that
[1:31] skills can offer. Just one more skill,
[1:34] bro. That's kind of seems like what
[1:36] we're saying. And I feel a bit of guilt
[1:38] here, too, because we have Matt Pocock
[1:40] skills, which is my skills repo, which
[1:42] is one of the most popular engineering
[1:44] skill sets out there. And so, I feel
[1:46] like I want to help the people who use
[1:48] my skills get out of skill hell. So, how
[1:50] do we do it? How do we get out of this?
[1:51] Well, what is actually missing here?
[1:54] Well, in my opinion, the thing that
[1:55] we're missing is we don't know what
[1:57] makes a skill great. We can't yet look
[1:59] at a skill and go, "Okay, this skill is
[2:01] doing these good things and these bad
[2:03] things." There's no shared rubric, no
[2:06] framework for looking at a skill and
[2:07] making it better. And so, that's what
[2:09] I'm going to give you in this talk. I'm
[2:10] going to give you a skill checklist, a
[2:12] checklist of things you can look at
[2:14] inside the skill to make sure that it's
[2:16] doing what it says it's doing and ways
[2:18] you can improve it, ways you can write
[2:20] skills. This checklist looks like this.
[2:22] We start with the trigger of the skill,
[2:24] how the skill is invoked, and the
[2:26] decisions that you need to design there.
[2:29] Then the internal structure of the
[2:31] skill, how the skill is actually
[2:32] composed and laid out internally. Then
[2:35] number three is how do you actually
[2:36] steer using the skill? How do you get
[2:39] the skill to tell the agent what to do?
[2:42] Then four, how do you make the skill as
[2:44] small as possible? Because once we've
[2:46] got a working skill, we then need to
[2:49] basically maximize it, prune out all of
[2:51] the irrelevant stuff, prune out all of
[2:52] the no ops. There's one handy advantage
[2:54] of me not being in the room with you,
[2:56] which is you can immediately go and try
[2:57] this out because I've encoded all of
[2:59] this into a new skill in my repo called
[3:01] writing great skills. So, if you've got
[3:03] an immediate use case for this, then
[3:05] just go to this my skills repo, you
[3:06] know, just close this browser, get out
[3:08] of here, and go and use this skill to
[3:11] either improve your skills or write
[3:13] great new ones. But, let's now go
[3:14] through the checklist then. We have
[3:16] number one, the trigger, the way the
[3:18] skill is invoked. And in order to talk
[3:19] about this, I'm actually going to do a
[3:21] bit of comparison here, which is that my
[3:23] skills are often compared to another set
[3:25] of extremely popular engineering skills
[3:27] called superpowers. And I'm really often
[3:29] asked the question, "How do your skills
[3:31] compare to superpowers? What's the
[3:33] difference between them?" To understand
[3:34] that, we need to understand the
[3:35] difference between user invoked and
[3:37] model invoked skills. Anytime you have a
[3:40] skill, you can always invoke it
[3:42] manually. So, the skill sits on your
[3:44] file system, the agent will just be able
[3:46] to pull up the skill and understand
[3:48] what's in there. And you can always do
[3:50] that by communicating that to the agent.
[3:52] Doesn't always look like this forward
[3:53] slash depending on the harness, but that
[3:55] you can always use or invoke your
[3:57] skills. Another way that skills can be
[3:59] invoked is by the agent itself. These
[4:01] are called model invocable skills or
[4:03] model invoked skills. You can take a
[4:05] description, so the description of the
[4:08] skill always ends up in the agent's
[4:10] context, and the agent can look in that
[4:13] and go, "Okay, based on that
[4:14] description, I'm going to invoke the
[4:16] skill and I end up reading the skill.md
[4:19] file, which is where the meat of the
[4:21] skill is, into my context window. That's
[4:23] how you invoke a skill. That's what
[4:24] happens when a skill is invoked. So,
[4:26] this description serves as a kind of
[4:28] context pointer. It sits in the agent's
[4:30] context pointing to another file where
[4:33] the agent can go if it wants more
[4:35] context. But, that context pointer, you
[4:36] don't need to put it into the agent's
[4:39] context. It can just be invisible from
[4:42] the agent, and that is what we call a
[4:43] user invocable skill. So, some skills
[4:46] can only be invoked by the user because
[4:48] they don't have this context pointer.
[4:50] It's optional. For instance, we can see
[4:52] in my code base design here, this is a
[4:54] model invocable skill. It has a
[4:56] description that ends up in the agent's
[4:57] context window. But, if we look at my
[4:59] grill me skill instead, we can see it
[5:01] has disable model invocation true. This
[5:04] means that this little description here
[5:05] will only show to the user. It won't be
[5:08] visible to the agent. So, this then is
[5:09] tip number one. Decide if your skill is
[5:12] user invoked or model invoked. Now, you
[5:14] might think that model invoked skills
[5:16] are better, right? Because either the
[5:17] model can invoke it itself or the user
[5:20] can invoke it. It's more flexible. But,
[5:22] every time you add a model invoked skill
[5:24] into your agent's environment, it
[5:27] increases what I'm going to call the
[5:28] context load on that agent. It adds a
[5:31] new description, which is costing you
[5:34] tokens on every request, but also adding
[5:36] a different thing for the agent to think
[5:39] about. So, if you have a hundred model
[5:41] invoked skills, that's going to be a
[5:42] hundred descriptions inside the context
[5:45] for your agent. So, it seems to make
[5:46] sense then to either tamp down the
[5:48] number of model invoked skills or to
[5:50] just use all user invoked skills. But,
[5:53] user invoked skills have a different
[5:54] load, which is the more user invoked
[5:57] skills you have, the higher cognitive
[5:59] load on the user. In other words, the
[6:00] more things the user needs to keep in
[6:03] their head, the more skill you require
[6:05] from the pilot. And so, if we compare
[6:07] Matt Percot skills to Superpowers,
[6:10] Superpowers is primarily model invoked
[6:12] skills. It gives the agent superpowers.
[6:16] Whereas my skills, I much prefer to be
[6:18] in full control. That means I get to
[6:20] keep the context load on the agent as
[6:22] small as possible, but it does impose
[6:25] more of a cognitive load on me. So, I
[6:27] need to understand the skills really
[6:29] deeply in order to get the most use out.
[6:31] So, why have I done this? Why did I
[6:33] prefer user invoked skills? Well, every
[6:36] time you have a model invoked skill, it
[6:38] basically you get a cost in
[6:40] unpredictability. Because every time you
[6:42] have a context pointer pointing from one
[6:44] resource to another, the model may just
[6:46] choose not to follow it, you know, even
[6:49] if it's absolutely perfect for the task,
[6:51] it may just choose not to invoke the
[6:54] skill. I much prefer removing that level
[6:57] of unpredictability, imposing a bit more
[6:59] cognitive load on the user, and what you
[7:01] get is just you're removing a class of
[7:04] problem from even being a problem.
[7:06] Because this unpredictability leaves
[7:07] people to need to eval their skills to
[7:10] make sure they're being called at the
[7:11] right time, which is really nasty and
[7:14] it's a problem I prefer to avoid. But,
[7:16] what I'm hoping to show you here is that
[7:17] model invoked skills and user invoked
[7:19] skills both have their same costs. So,
[7:22] it's not an easy decision which one you
[7:24] choose. So, that then is the trigger,
[7:26] how the skill gets invoked. Now, let's
[7:28] talk about the structure, the internal
[7:31] layout of the skill. I think of there as
[7:32] being two main units that you need to
[7:34] put into most skills. These two units
[7:37] are the steps and the reference. The
[7:40] steps are the step-by-step procedure
[7:42] that the skill is going to walk through
[7:45] and the reference is any supporting
[7:46] information that helps it walk through
[7:48] those steps. You can have skills that
[7:51] have no steps and are only reference and
[7:53] you can have skills that are no
[7:55] reference and only a set of simple steps
[7:57] to walk through. But if you start
[7:58] thinking of skills as composed of these
[8:00] two units, it really helps just break
[8:02] them down a lot more. If we look at an
[8:04] example, one of my skills called 2 PRD
[8:06] creates a product requirements document
[8:09] out of the current context window. It's
[8:10] got three steps in it. So it finds the
[8:13] relevant context, it confirms the test
[8:16] seams with the user. So there's like a
[8:18] little human in the loop checkpoint
[8:19] there just to make sure we're not doing
[8:21] anything weird with the testing, which I
[8:22] find really important. And then we write
[8:25] the product requirements document. To
[8:26] handle those three steps, we've got two
[8:29] bits of reference material. We've got a
[8:31] little bit of reference on what is a
[8:33] test seam and then we've got a product
[8:36] requirements document template. So just
[8:38] a literal markdown template which is
[8:41] used to write the PRD. So this is a
[8:42] great way to write a skill from scratch.
[8:45] You work out if you need some steps,
[8:47] then you write those steps and you work
[8:49] out what reference material those steps
[8:50] need and you put it in a separate little
[8:52] spot in the skill, which is for
[8:54] reference material. However, there's a
[8:55] really important constraint that we need
[8:57] to think about, which is tip number
[8:59] three, we want to make the main skill.md
[9:02] file as small as possible. Every skill
[9:05] is composed of its description and then
[9:07] a skill.md file and then any reference
[9:09] material that branches off that. And
[9:11] this skill.md file, if we make it small,
[9:14] then we're saving in a bunch of
[9:15] different ways. Smaller skills are just
[9:17] easier to maintain, easier to audit,
[9:19] fewer words to think about. And every
[9:22] time you shave off a word, that is a
[9:24] token shaved, that multiple tokens
[9:26] shaved from your skills cost. So I do
[9:28] believe that small skills are really
[9:31] important both for maintainers and for
[9:33] users. One really useful way you can
[9:35] make your skill smaller is by thinking
[9:37] about the different branches of the
[9:39] skill, the different ways the skill can
[9:41] be used. Because if you have reference
[9:43] material that's only used in one branch,
[9:45] then that's a candidate for being
[9:46] removed from the main skill.md. For
[9:49] instance, if we look at my 2PRD here, we
[9:51] have two pieces of reference material,
[9:53] what is a test seam and the PRD
[9:55] template. Well, we need the PRD template
[9:57] every single time because we are always
[10:00] creating a PRD and we probably also need
[10:02] the what is a test seam information
[10:04] every time because we're always asking
[10:06] about the test seams. So, 2PRD, there's
[10:08] only one branch and all the reference
[10:10] material belongs on that branch, so it
[10:12] probably also belongs in the skill.md
[10:15] file. However, if we look at a different
[10:16] skill of mine, which is domain modeling,
[10:19] domain modeling does two things. It
[10:21] updates a local glossary called
[10:23] context.md and then it also creates
[10:25] architectural decision records. In other
[10:27] words, it's doing two different things
[10:30] or it might actually choose to do
[10:31] neither of these, in which case it
[10:33] doesn't need the template and it doesn't
[10:34] need the ADR template, either. So, in
[10:37] other words, domain modeling has two or
[10:39] maybe three branches and this means that
[10:41] we don't need to include the ADR
[10:43] template or the context.md template into
[10:46] the main skill. They can be moved into
[10:49] separate zones. The way you do that is
[10:51] you have the skill.md file, then you put
[10:54] it behind a context pointer and you
[10:56] point the context template to a separate
[10:59] markdown file inside the skills folder.
[11:01] That context pointer literally just
[11:03] says, "If you need the template or if
[11:04] you need to update the context.md file,
[11:07] go to this file." And I call that an
[11:09] external reference. It's a reference
[11:12] that's external to the skill.md that you
[11:14] can just easily reference the agent can
[11:16] pull in very easily because it's bundled
[11:18] along with the skill. So, this is a
[11:19] technique you can use for making the
[11:22] skill.md as small as possible, which is
[11:24] has so many benefits.
[11:26] Hide branching reference material behind
[11:28] context pointers. In other words, if you
[11:30] feel like your skill is going to be used
[11:32] in lots of different ways, then take the
[11:34] reference material that's relevant for
[11:35] those branches and hide them behind
[11:37] context pointers. So, that is structure.
[11:39] We need to think about making the
[11:41] skill.md super duper small. We need to
[11:43] think about the branches in our skill
[11:45] moving material out behind context
[11:47] pointers. And we need to think about
[11:49] steps and reference, which are the two
[11:51] main units inside a skill. Let's go next
[11:54] to steering, the actual ways we get the
[11:57] agent to do what we want it to do. And
[11:58] for me, steering comes down to one
[12:01] really cool technique, which is the kind
[12:03] of main thing I want you to get from
[12:05] this talk. This technique fixes this
[12:07] issue, which is the agent doesn't do
[12:10] what I want. In other words, I specify
[12:12] something in the skill, I think that
[12:14] I've been clear, and then it just
[12:15] doesn't do the thing. Now, I think the
[12:17] main reason this happens is because
[12:19] you're not using a technique called
[12:21] leading words. The idea of leading
[12:23] words, or light vert if you like
[12:26] literary theory, I suppose, is that
[12:28] there are certain words that pack in a
[12:30] bunch of meaning into a very small
[12:32] space. These leading words are really
[12:35] powerful with agents because you put the
[12:37] leading word in the skill itself in the
[12:40] text, and then the agent will repeat the
[12:42] leading word back to itself as part of
[12:44] its operations, as part of its thinking
[12:46] tokens, and as part of its output to
[12:48] you. And then, because it's
[12:50] re-emphasizing that word and that word
[12:52] hopefully describes what you want from
[12:54] the agent, that then goes and changes
[12:56] its behavior. Let's make this more
[12:58] concrete with an example. So, let's
[13:00] imagine that we have a problem, which is
[13:02] a classic problem with agents, which is
[13:03] that they code layer by layer. In other
[13:06] words, if you give them a big tranche of
[13:07] work to do, they will generally code up
[13:09] all of the database layer, then all of
[13:11] the schemas, then all of the API
[13:13] endpoints, then all of the front end.
[13:15] They don't do the sort of typical um
[13:18] human thing, which is to seek feedback
[13:20] early on, get something small working,
[13:23] and then expand out from there. Now, we
[13:25] can try to encourage the agent to do
[13:26] that by just saying, you know, don't
[13:28] code layer by layer, Um make sure that
[13:30] you create a small slice first and then
[13:32] go from there. But what if instead we
[13:34] use the leading word? We said, "vertical
[13:36] slice" is our leading word. We want to
[13:39] slice up the work instead of horizontal
[13:41] slices into vertical slices. A vertical
[13:44] slice is a pretty well-known terminology
[13:46] in development, and so this will
[13:48] hopefully trigger the agent's priors and
[13:50] it will understand what we mean. We
[13:52] don't just have to like have a two-word
[13:54] skill where it just says vertical slice.
[13:56] What we're doing is we're packing lots
[13:57] of meaning into a relatively short
[14:00] phrase that we then repeat throughout
[14:02] the skill. The cool thing about this
[14:03] technique is you can know if it's worked
[14:05] because you say vertical slice in your
[14:07] skill, and then you'll notice in the
[14:09] reasoning traces that it's saying,
[14:10] "Okay, we're going to do this as a thin
[14:12] vertical slice." Then you should get
[14:14] better implementation plans. Everyone
[14:15] I've explained this technique to sort of
[14:17] feels like, "Oh yeah, I've been doing
[14:19] that for a while. I've been using these
[14:21] little phrases to try to encourage the
[14:23] agent to do what I want." All I'm asking
[14:26] you now is to use those consistently
[14:28] within your skills and watch in the
[14:31] thinking traces as the agent adopts your
[14:33] way of doing it. So often if the agent
[14:35] isn't doing what you want, you need to
[14:37] make your leading words more consistent,
[14:40] more powerful, and look for others
[14:42] because, you know, English is a pretty
[14:45] wide API in terms of different functions
[14:47] you can call, different things you can
[14:49] experiment with, and there are many
[14:50] leading word candidates out there. And
[14:52] agents are actually pretty good at
[14:53] helping you think of them. Another
[14:55] little lever you can use with agents is
[14:58] sometimes the agent just doesn't do
[15:00] enough legwork. What I mean by this is
[15:02] that, okay, we're on a step, let's say,
[15:05] and maybe the step is to ask clarifying
[15:07] questions or to explore the code base,
[15:09] and the agent just doesn't do enough of
[15:12] it. It doesn't put enough effort into
[15:14] that particular step. A real classic
[15:16] case of this and something that I have
[15:18] found almost everywhere it
[15:20] is plan mode. Because in plan mode, we
[15:23] have two steps. We have ask clarifying
[15:25] questions and then create a plan. And
[15:28] what I have found in every single
[15:29] implementation of plan mode I've tried
[15:31] is that ask clarifying questions just,
[15:34] you know, it doesn't ever do enough
[15:36] legwork. It sees that its ultimate goal
[15:38] is to create a plan and so it just does
[15:40] a small amount of legwork with ask
[15:42] clarifying questions, ask you a couple
[15:43] of things, and then eagerly creates the
[15:46] plan. So, what was my solution here?
[15:48] Instead of doing plan mode, I instead
[15:50] have a skill called grill with docs,
[15:52] which is kind of my ask clarifying
[15:54] questions phase. And then, I split that
[15:57] up into a separate skill. So, I split
[15:59] the planning into its own skill. So,
[16:02] grill with docs now is its own skill
[16:04] where the agent only sees that part of
[16:07] the process. And then, after grill with
[16:09] docs completes, we then go and do 2 PRD.
[16:12] In other words, we have step one and
[16:14] step two, but the agent only sees one
[16:16] step at a time. So, this is a really
[16:18] cool technique for increasing legwork on
[16:21] the step that you're on by hiding the
[16:23] future goal, hiding the future steps.
[16:25] It's not always necessary to split
[16:27] skills into individual steps, but in
[16:31] particular cases where you really want
[16:33] an extra chunk of legwork, it really
[16:36] there's no technique like it. It works
[16:37] very, very well. So, that is steering
[16:39] using leading words to capture what you
[16:41] want in small reusable tokens and then
[16:44] making sure that it's doing the right
[16:46] amount of legwork per step. So, let's
[16:48] head now into pruning. Now, pruning
[16:50] really is just a quick fire set of
[16:52] failure modes, different things that you
[16:54] can get wrong. And the first is fairly
[16:56] obvious is we do not want massive
[16:59] skills. Massive skills are usually a
[17:02] kind of symptom of something else going
[17:04] wrong. So, a symptom of one of these
[17:05] other failure modes. And the first one
[17:07] is pretty simple. Don't repeat yourself.
[17:10] You need to make sure you're watching
[17:12] out for duplication. And in general, I
[17:14] like to have every part of the skill to
[17:17] have a single source of truth. In other
[17:19] words, if you have a piece of reference
[17:21] material like the PRD template, let's
[17:22] say, or something even smaller like what
[17:25] is a test seam, you make sure that you
[17:27] don't repeat that in several places or
[17:29] like cover multiple steps in multiple
[17:31] places. Just make sure each part has a
[17:34] single source of truth and you're not
[17:35] repeating yourself even across reference
[17:38] material, too. The next way that skills
[17:39] get big is via sediment. And sediment is
[17:43] just a classic thing when people are
[17:46] working on the same set of docs, really,
[17:48] which is that everyone starts
[17:50] contributing to a shared markdown file.
[17:52] People add their own stuff. They don't
[17:54] feel brave enough to delete and modify
[17:56] anyone else's. And so you just end up
[17:57] with this huge amount of sediment with
[18:00] often irrelevant material for the skill,
[18:02] especially stuff that hasn't been laid
[18:04] out properly. With a skill with a lot of
[18:06] sediments, you really need to look at
[18:07] structure. That's the first thing you
[18:09] need to do. You need to make sure that
[18:10] the stuff that's been added is relevant
[18:12] for all branches. If it's not, then move
[18:15] it into the correct branches. Or if it's
[18:16] just totally irrelevant, maybe just
[18:18] remove it or kill it. Or maybe there's
[18:21] stuff in there that's totally stale, in
[18:22] which case you just need to kill it
[18:24] dead. The next failure mode is really
[18:25] common when an agent writes your skills,
[18:28] which are no-ops. So things inside the
[18:31] skill that appear to do something but
[18:34] don't actually influence the agent's
[18:36] behavior inside the context of the
[18:37] skill. Let's imagine we have an
[18:38] implement skill and we have an entire
[18:40] paragraph of the skill that tells the
[18:42] agent to write a long detailed commit
[18:44] message. What would happen if you just
[18:46] deleted that paragraph? Well, the agent
[18:49] would probably still write a decent like
[18:51] long commit message. People ask me a lot
[18:53] how I get my skills so small, and it's
[18:56] just using these techniques, using
[18:58] deletion tests, using um making sure
[19:00] that I compact things into leading
[19:02] words, I don't have anything irrelevant
[19:04] in there, and I don't have any sediment.
[19:06] And that finally brings us to the full
[19:08] sweep of things. Number one, we check
[19:10] the trigger. We make sure that it's
[19:12] firing at the right times. We check
[19:14] whether we're imposing context load or
[19:16] cognitive load. With structure, we think
[19:18] about branches. We think about
[19:21] structuring things into steps and
[19:23] reference. And we make sure that
[19:25] material that's only relevant for one
[19:26] branch is outside of the main skill.md.
[19:29] With steering, we're thinking about
[19:30] condensing text down into leading words
[19:33] and watching those leading words appear
[19:35] in the reasoning traces. And we're also
[19:37] thinking about legwork. Should we break
[19:39] this skill down further to increase its
[19:42] focus on the current phase by hiding the
[19:44] future phase phase from it. And with
[19:46] pruning, we're doing a final pruning
[19:48] pass over the entire skill, watching out
[19:50] for sediments, watching out for crud,
[19:52] and watching out especially for no-ops.
[19:54] Now, all of this stuff, the best way to
[19:57] get started with this framework is
[19:58] inside this skill, inside the writing
[20:00] great skills skill. You can check it out
[20:03] from my papago skills, download it, use
[20:05] it to improve your own skills, and maybe
[20:07] even use it to run over some community
[20:10] authored skills so you can check that
[20:12] the skills that you're actually pulling
[20:14] in are any good. If you want to follow
[20:15] along with my stuff, then I have a
[20:17] newsletter up on aihero.dev. And my
[20:20] plans for the next few months are to
[20:21] release an AI coding crash course, which
[20:23] is an intro to a lot of the stuff I've
[20:25] been talking about and how you get off
[20:27] the ground working with engineering and
[20:29] AI. I hope that what I've given you is
[20:32] enough to help you escape from skill
[20:34] hell or at least try to make the bitter
[20:36] journey out of there. I'm so sorry not
[20:38] to be able to attend in person, but
[20:40] thanks for watching. I'll see you very
[20:42] soon.
