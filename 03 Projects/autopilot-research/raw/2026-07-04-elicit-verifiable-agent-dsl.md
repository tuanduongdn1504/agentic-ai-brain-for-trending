---
source: yt-dlp (path 5 — operator-submitted single video + original-resource chain)
topic: elicit-verifiable-agent-dsl
generated: 2026-07-04
videos: 2 (VN dub UjskE6hGx6c + EN original qOjleN2-50c)
notebook_id: none (no NotebookLM — direct yt-dlp captions, read in full in main loop)
deliverable: wiki topic + pilot methods
---

# Elicit ÆPL / verifiable-agent-DSL — raw ingest (2026-07-04)

## Provenance chain

- **Operator-submitted:** https://www.youtube.com/watch?v=UjskE6hGx6c — "Elicit x Claude | Dùng DSL Tự Xây Để Agent Chạy Đúng 100% Kế Hoạch" — BizMate AI Official (UCrAXctjaddmG8ctC3Eoha3w), uploaded 2026-06-23, 1780s, Vietnamese dub.
- **Original (linked in dub description):** https://www.youtube.com/watch?v=qOjleN2-50c — "Making agentic workflows trustworthy and verifiable with a custom DSL" — official **Claude** channel, uploaded 2026-05-22, 1779s. Speaker: **James Brady, Head of Engineering, Elicit**.
- **Event:** Code with Claude: Extended **London**, 2026-05-20 — Builder stage session (claude.com/code-with-claude/london-extended). Third topic in this wiki sourced from that event (after agentic-analytics-harness Chris Merrick + the Kevin Chen memory workshop sibling).
- **Official video description (verbatim):** "System design of agentic research assistant built unconventionally: one component outputs plan in custom Turing-incomplete programming language, another interprets it, quiver of models executes concrete tasks. Architectural choices as concrete instantiations of company values."

## EN auto-caption transcript (deduped, read in full in main loop — garbles: "Alissa"/"illicit"/"a list" = Elicit; "3.5 Sonar" = 3.5 Sonnet; "Ash Bell"/"ASPL"/"HPL"/"SHPL" = ÆPL "Ash PL")

My name is is James Brady. I work at
Alissa. And today I'm going to be
talking about how we make our agentic
workflows trustworthy and verifiable
with a custom domain-specific language.
Okay, so
uh in terms of the the structure of
today,
I'm going to start with a high-level
overview of why we went for a DSL in the
in the first place.
Talk a little bit about the language,
how we made the decisions we did
um in its design.
How we integrated it into Alissa, we'll
do a quick demo.
And then uh and then wrap up at the end.
But uh let me start with a question. So,
let's say that two systems produce
identical output.
Do you trust them equally?
And the answer is, of course, well, it
depends. It depends on
what went on inside of those systems to
produce that output.
I would say that the
the mechanism, the how of how how an
answer is produced is as important and
important in a different way compared to
just the the final output itself. Let me
try and make this a bit more concrete.
So, let's say you're running a static
analysis tool over your code base.
And it runs for a while and in the end
in the end it says, "This code is free
of security security vulnerabilities,
safe to ship to production."
I would contest that if you knew the
system
was built on, let's say, an older model,
3.5 Sonar, something like this. If the
system is using an older model like
that, this is option one.
And option two is it's a latest and
greatest state-of-the-art model. It's
done all sorts of tool use. It's done
critique and redrafting. That's just a
fundamentally different kind of an
object. The
message might be literally identical,
but you would react very differently to
those two messages if it came from a
kind of older model that was, you know,
not so powerful versus something that
has a used a lot more tokens and and
intelligence.
So, the mechanism matters.
And there isn't a a sort of single
correct mechanism. There isn't a kind of
single canonical
um
best way of designing the internal
structure of of the systems that you're
building. I really think that it's a
it's a design choice. It depends on what
it's you're trying to do. It depends on
the domain that you're building building
in. It depends on the user. It depends
on the task, like what it is that the
user's doing within the domain.
We found that there's definitely a speed
versus rigor trade-off. So, if you're
trying to do something which is
uh extremely in depth and extremely
defensive and extremely high quality,
that naturally takes a bit longer than
uh than than something a bit more
surface level.
And there's no, you know, there's no
correct answer. Sometimes you want you
want fast and sometimes you want really
really high quality.
Uh the provider's brand and taste is
interesting here. So,
uh I don't know if I would have called
this before we started working this
ourselves, but Elicit prides itself on
super high reliability, really high
quality, data provenance. We really kind
of stand behind the results that we put
in in front of people. I'll show you a
demo of what I'm talking about a bit
later on.
And these are some of the some of the
concerns that we had in our mind when we
were thinking about, well, what is the
We know the mechanism matters, but what
is the right mechanism for us at Elicit?
And I think it came down to these three
desiderata when we were building out our
research agent, which will be the demo
in in a few minutes.
So, firstly, the research agent's
process must be legible. It needs to be
legible to the user and also, by the
way, it needs to be legible to other
agents. We want for um
the uh
the the process, the algorithm, the kind
of like internal set of steps that the
that the agent is taking to be
um spot-checkable by the human,
spot-checkable by other agents. We can
run you know, sort of cri- critique
agents over it, that kind of a thing.
The second desideratum, the iteration on
the process retains fidelity. This is
maybe uh
Let me explain this a bit more because
it's uh it's a bit of a fiddly one.
What I found and I maybe what some of
you found as well is that if you're
iterating on a piece of work and you're
saying that's not quite right, it's kind
of going this other direction, oh you
know, I I want to add this other layer,
this other consideration.
I found that you can sometimes drift a
little bit from what you were initially
trying to do and the model ends up
getting a bit confused and you have to
say, you know, let's start again or
backtrack or something. It's kind of uh
kind kind of annoying. And it it
definitely harms trust. So, we want to
avoid that. We want to be able to add to
the work. We want to be able to add
layers. We want to be able to be able to
go in different directions
without losing that kind of
uh clarity and consistency of what the
user was initially interested in doing.
And uh lastly and certainly not leastly
is the process is followed faithfully.
So, let's say we've got the process,
it's it's legible, we've checked it, the
user's checked it. It's great. And we've
iterated on it and we've kind of stayed
true to what it is the user's interested
in. Well, we have to actually ensure the
system does in fact do that set of
steps, otherwise, you know,
uh what are we what are we doing here?
So, uh
those are the considerations that we
foregrounded when we we were thinking
about how we want for elicit uh elicit
to work. And that that led us to
reaching for DSL. I'm not saying that
everyone should be using a DSL, you
shouldn't. Uh what I'm saying is that
these three things really kind of led
naturally towards well, a DSL could be a
great choice for us. So our DSL is
called Ash PL. The kind of weird smushed
together AE thing is apparently called
Ash. It's like an old English um
diphthong or something.
Uh
so Ash PL and this is our domain
specific language for the agentic
workflows in the in the elicit um in the
elicit product.
And Ash PL has a few distinguishing
factors. So uh firstly it is Turing
incomplete. It's relatively simple.
There's no loops. There's no uh yeah
there's no there's no recursion. There's
no there's no mutation. It's purely
functional. It's a reactive language and
it's an opinionated subset of of Python
and the opinionated is is important
here. So it's not just a kind of generic
simplification of Python if you will.
Not like Python with a couple of bits
taken off at random.
Um what we did is we
uh we disallow we sort of take out the
language features of Python that just
aren't aren't that helpful and we add
stuff in. We add some extra primitives
in which are specific to our domain. So
our domain is scientific research and uh
empirical decision-making, high-stakes
decision-making.
And the primitives that we put into our
DSL match that. You know we've got
retrieving academic uh research papers
or clinical clinical trials, you know,
things things like that are are built
into the built into the language.
Okay. Um
Yeah, let's have a look at some Ash PL.
So hopefully this isn't too small for
you all. Um
you don't need to read the the code
obviously.
Uh what I'm trying to show here is that
the Ash PL on the right looks a lot like
Python because it is a subset of Python.
Uh we're keen on types. It's it's it's
typed. That lets us do uh fast kind of
redrafts if you've got a type error.
And I think this example program uh just
FYI was the
the process that we wanted to go through
to do a competitive competitive analysis
for illicit itself. So, we're looking
for other
academic search engines and AI
assistants. It looks like systematic
review tools. We're We're doing web
searches for those. We're joining the
results. We're enriching the sources.
You know, th- this is the kind of the
set of steps that we want to go through
that we think is a good process for
doing a competitive
landscape overview.
And um
the core engine of what goes on within
an illicit user session is that we have
a component which I'll show in in in the
in the next slide, which is writing the
ASPL.
And then we interpret the ASPL. That's
just done in like plain old Python code.
And then we redraft the ASPL based on
what just happened. So, in a simple
case, you can imagine
we write we we we write some ASPL.
There's a type error. Okay, there must
be a problem. So, that gets kicked back
to the ASPL kind of writer component. It
tries again, fixes the type error. We
reinterpret the ASPL.
It runs this time. We get some results
back. We rewrite the ASPL. There's that
kind of constant loop of
writing and then interpreting and then
rewriting and then interpreting. And
that's that's like the core
engine of of making progress inside of
inside of illicit.
Okay, so that's the language. Let me
show you how we integrated it into um
into like more of a into more of a
system. So, we have the UI in the top
left. That is what the user is is
interacting with. It's just in a in a
web browser. That's what we'll have a
look at in a second in the demo.
The
The UI is talking to an event log
that can append-only event log. That's
how we
manage our our distributed data
structure. We've got a Python service in
the top right. And
uh then the Python service is talking to
the sandbox in the bottom right or kind
of bottom right-ish.
Um and the curator in the sort of orange
ochre color, the sort of um Claude
color, the tropic color, uh that's the
that's the piece that's writing the Ash
PL.
So, let me let me uh add a a touch more
detail here.
The user is interacting with UI.
The uh events are emitted as they click
buttons and enter search queries and
whatnot. That gets uh added appended
onto the event log. The Python service
is a message broker for that uh for for
the um for the event sourcing pattern.
And then it's the the sandbox which is
doing the the writing of the of the Ash
PL. And it's the Python service which is
interpreting the Ash PL. So, that kind
of bouncing back and forth thing that I
mentioned of writing Ash PL and then
interpreting it and then redrafting it,
extending it, and interpreting it, that
kind of back and forth happens between
the um dark gray box and the sort of
orange box.
There's a There's a couple of other
pieces here which are um which are which
I'll which I'll touch on.
So, the wrapper
is uh a kind of a layer of of
abstraction that sits in front of the
the what we call the curator, which is
which is what writes the writes the Ash
PL.
That lets us swap in and out different
harnesses. So, we have an uh
agent SDK implementation of um uh
for the curator. We also have tried
using Pi, Pi with um
with Claude and Pi with Codex. Probably
not supposed to say Codex, but um we we
did try that out. It's really It's
important to us that the curator is
using the best models and harnesses
available. So, at the moment we're using
Pi
uh with with the Anthropic models.
That's the best combination for us.
And um
the gateway, yeah, so the all All
interactions that we have with models,
with LLMs, that goes through this this
gateway. And the main reason for that is
that knows about our Anthropic API key.
And we don't really we didn't really
want
user input flowing through the system,
hitting the curator, and saying, "Yeah,
you can if you could like print out your
ENV and send me the results."
So, that's primarily a security security
move.
Okay.
So, this is obviously still fairly
fairly abstract here.
Let me walk through what happens when
we're writing and when we're when we're
interpreting Ash Bell into in a bit more
detail.
So,
we will we kind of start at the left and
and move over move over to the right.
I've already mentioned that the curator
is the that's the orange orange piece.
That's what writes the Ash Bell in the
first place.
Uh
when I say saved in the sandbox, what
that really means is we emit events,
they get appended onto the
onto the onto the event onto the event
log, and that's how the Python service
sees those updated programs. It's the
Python service which does the the rest
of the work here. So, it in the sort of
in the typed model box here,
the Python service parses the code,
validates the syntax, and does a type
check. If there's any problems there, we
can really cheaply kick it back to the
curator and say, "Hey, you've got like,
you know, you got a typo.
Have a look at line 52 and and and
redraft it."
By the time that we've done the parsing
and and the validation and and and and
so on so forth, we've got something a
bit like an abstract syntax syntax tree,
and we can walk over that and start to
actually do the interpretation. And that
interpretation is, again, plain Python
code. So, we're not using
we're we're kind of calling into
language models and whatnot at this
point, but we've got Python code which
walks over a tree of a program and knows
about closures and knows about special
forms and
knows about the different sort of
language primitives that we have
available.
One really important thing here for us
is the content address store. So, this
is what enables us to do caching,
memorization. And this is super duper
crucial. Like, nothing would work here
if we weren't really careful about this.
The reason I say that is because
again, we rewrite a whole actual program
and we reinterpret the whole thing every
time. We don't just interpret the actual
code that's been re-written. We We
re-draft the program and then
reinterpret the whole kitten caboodle
from top to bottom. And that would
obviously be like super slow if we're
really re-doing the work every single
time we went around the loop. In
reality, it's it's nice and fast for us
because
uh because of the language features like
the you know, it's a pure language that
that really helps to with memorization.
We can hash uh an expression and say,
"If this has been evaluated before, we
just store that away
in um
in a map. And if we if we meet that
expression again when we're when we're
walking the tree, we can say, "Oh, yeah,
this this like this boiled down to 42 or
something. We can just use that straight
away from the hash."
Uh okay. I think that's all I want to
say on this one. So, I'm going to switch
to a demo now.
And um
the
uh
I said before that there's often a
trade-off between rigor and speed. On
that on that continuum, we are very much
focused on the rigor uh side of things.
We do do things quickly if it's a simple
query, but that's not really where
we differentiate ourselves. It's not
really where our special sauce is uh so
to speak. So,
if you go to elicit.com, um you would
see something a bit like this. We have a
bunch of
uh
sort of templates you can start with
creating table slides, drafting a
report. Um I'm going to show you a
research landscape,
which uh
again is like a much I think it probably
took in total,
I don't know, like a couple of hours or
something of of it doing work and me
adding layers on top of it, so can't do
it in a demo format. Uh, but I've got a
session saved away that we're going to
take a look at.
Uh, but yeah, yeah. It doesn't need to
take that long. It's just, you know, it
gets a bit a bit more interesting when
it's a more in-depth thing.
So, this is the research landscape that
we're going to take a take a look at
here. And my initial query was to map
the companies and institutions investing
in foundation model models for biology.
And you can see that the first thing
that we did here was Alissa asked asked
me a question. It was like, "Okay, I get
the kind of overall big picture. Let me,
um, narrow that down a little bit. Are
you interested in a broad landscape?" I
think the other options here were you
you interested in something,
um,
like a you know, a particular foundation
model in more interested in academic
institutions or companies, that kind of
a thing. And I just said, "Yeah,
the broad landscape."
Um, is is what I'm looking for.
And then the rest of, uh,
the rest of the steps here are driven by
Ash PL. So, this, uh,
first analysis step, you can see, if
anyone can't see this and needs to be
bigger, then please do say.
Uh, you don't need to be able to read
all the text in detail, but okay. I'll
go with that as it is.
So, this first analysis block, we're
doing a bunch of searches. We're looking
for academic papers relating to genomic
foundation model pre-training
transformer. We're doing some web
searches.
Uh, we're trying to fetch the full text
of papers when available. We're doing
some screening, like filtering. All of
these steps, all of these stages, uh,
are encoded into Ash PL, and then we run
they're actually, um,
the Ash PL is not just a representation
of a plan. It is literally the plan
which is executable, you know. Uh, that
that's what lets us really be be sure
that we're following through on the plan
as as stated.
Um so, let me go a bit deeper here.
That was the kind of first the first um
analysis stage of us looking for
organizations, looking for institutions.
Looks like we did Yeah, did some more
analysis here. I think this one is All
right, at this point we've got some
actual institutions. We've got Howard
Hughes Medical Institute, Stanford
University, et cetera.
Um again, this is all coming from HPL.
We're doing some more searches. We're
doing some more searches. We're doing
some more screening.
Um yeah, you can see we go pretty deep
um when we when we're in this mode.
Let me skim forward to the results here.
And I'll get this sidebar out of the
way.
So, uh after some humming and whirring
and um quite a few tokens, we end up
with a table like this. We call this an
artifact, and uh each row is a In this
case, an organization which has got some
kind of a interest in biological um
foundation models. Got GDM, we've got
Meta, Microsoft Research, et cetera, et
cetera.
And you can see that we've extracted
some
uh
some attributes alongside that from the
foundation models that they've created,
uh the modalities that they're that
they're interested in, notable
collaborations, it looks like.
So, I've been saying that this is driven
by HPL, but um
how do you how do I know that?
Uh you know, what's the what's the
connection here?
For each of these artifacts, we can
actually look at the HPL code that was
used to to generate it. So, um this is
literally the the executable DSL that
was um
behind the creation of that table we
were just looking at.
And you can see that first of all, we're
doing some uh
some web searches for foundation models,
uh multimodal biology AI model uh you
know, you can you can see this.
Uh looking for academic academic papers,
again.
We are I guess joining these together at
some point. Uh, yep, that's where the
join is.
Um, and uh,
as you can probably tell, looking at the
AshPL is not particularly fun.
Um,
most people don't do this and and that's
not really the the kind of the core
driver of why we have this. We we have
this because we want to know that a list
of the system is following and the the
following the instructions that we came
up with, right? Like that's the kind of
primary thing.
Um,
but it is useful for other agents to be
able to look at this AshPL though and
say, you know, you've you've missed
something, you've overlooked something,
you have, I don't know, there's a
there's a a key search that you've you
should have considered or there's a part
of the user's query that that you didn't
uh, take into account. Uh, so that's
something which is which is really handy
when the plan is so legible in in this
format. Something which is a bit more
useful from a user perspective, a bit
more ergonomic, is a uh,
a graphical representation of what's
done within the system. So, this is um,
derived directly from, um,
you know, from from the AshPL.
This isn't just a kind of
um,
I don't know,
a made-up nice visualization or
something. It literally is derived
directly from the same thing that the
that the plan uh, was executing over.
And I think in this case it's it's
pretty pretty linear, so it's not super
interesting, but um, yeah, we start off
with a couple of searches,
did some enrichment, which means
fetching um, full texts of papers, that
kind of a thing, extracting,
um,
curating, which means filtering, do some
more searches, etc. So, I I do actually
find looking at this to be quite handy
if I'm trying to
convince myself or not that I would
endorse the process that the that a list
that a list it took. Uh, and you can
quite qui- quite quickly notice when
there's something that looks a little
bit um,
skewiff.
But,
I wouldn't be I wouldn't stop here
necessarily, right? Like there's other
kinds of um
layers to this investigation that might
want to add on. So,
I think I did a few things there. Yeah,
I asked for a comparison of open and
closed source strategies for the
different organizations. We did some
work for that.
I then asked for
the commercialization commercialization
strategy, the GTM approach, and we did
some work for that.
I then asked for
um I think you know, you can see where
another artifact was created.
Um I think the next thing I was
interested in was I missed a missed a
block here.
Here we go. Yeah, mapping out the
different government orgs and other kind
of oversight institutions. I did some
work for that. And then and then at the
at the end of this user session of my
user session,
we have
um
I asked for a join. Right, so we've got
effectively a table of data which is the
organizations. We've got a table of data
which is the oversight bodies. And just
in natural language I can say I kind of
want to I want to join these together
and see how the labs have been have
interacted with the oversight bodies.
And uh that's come up with this table.
Uh we can see how Anthropic has
interacted with um US AI Safety
Institute and AC in the UK and and so on
and so forth.
Um
And if I look at the
uh AshPL for this
table,
what you might notice is that the top of
the program um is identical to what we
had before. So, this is this these are
the same web same same web queries and
paper queries that we had for that very
first table we were looking at.
And this is all the same code. It's got
the org mentions. The I guess the join's
going to be down here a little bit. Like
this is the same stuff as what we were
looking at before.
The difference is this program is now
a lot like a a longer. I think the last
one was
I don't know, 100 lines, 150 lines.
We're up to like a 1,000 or so, a bit
bit a bit more. And it's only when you
write down here
that we're starting to talk about
Um yeah, you can see that we're looking
at the oversight
uh oversight bodies and the in and the
interactions between those and the and
the labs here. Here we're talking about
oversight. This is the sort of a
the the model for a lab interacting with
a with an oversight body. And at the
point of generating that last table, we
would have interpreted this whole
um program again from scratch, except
this that cache that I talked about. So,
the fact that we had already done
all this stuff up here, we'd already
done all these all these web queries web
queries, and paper searches, and and so
and so forth, meant we can interpret the
whole the whole um program from scratch,
but you know, the vast majority of it is
is just memorized and you get it back
straight away.
One of the reasons we took that design
design decision is because
um
it's easy to
be confident about and and and make
statistical guarantees of of kind of
cohesion and correctness when you're
literally interpreting the whole program
every single time. You know, if you're
just interpreting little snippets,
that's where the drift can come in that
I mentioned before. That That was one of
the places the drift can come in.
Uh
okay.
So, um can we switch back to the slides,
please? I think that's that's it for the
That's it for the demo.
Um okay.
Again, I'm not saying that everyone
should be using a DSL. It's
uh
It's not the easiest thing to to build.
Uh I don't know, it wasn't it wasn't so
bad, but um
it's the kind of thing that you should
reach for if
the desiderata for your product and for
your organization points you in that
direction. And if they do, it's great.
We we're really really happy with how
it's working for us. But again, elicit
is uh based on and and kind of really
anchors around
high quality, dependability, robustness,
data provenance, all that stuff I was
just talking about, and that's why we
went for it. If you're in a similar
position, or you can think there's some
other desiderata that could lead to a
different DSL that might be a good fit.
Here are some of the things that you you
should be should be thinking about.
So, firstly and most obviously, you need
a DSL. And the uh agent ergonomic piece
here, what I mean by that is
firstly,
we have found that
you'll have a better time if you base
your DSL on an existing language that
has a lot of
examples of in the training data because
then, you know, it doesn't that the the
model, the curator in our case, doesn't
need to like learn the syntax, uh right?
It just needs to know there's a subset
that it can go for.
Um
and um
I would say
a surprisingly small amount of work went
into the DSL compared to everything
else. Everything else is kind of like
conventional software engineering to
really turn it into a a system that
works.
And that's where the majority of the of
the work was there. So, I mentioned the
wrapper. Um yeah, that's like letting
you switch between different harnesses
uh and models.
Um interrupt handling. So,
when you're in an elicit and you're, you
know, waiting for the results to come
back, you can add other things into the
chat, and we want for that to gracefully
flow back into the curator so it can
redraft its plan without stopping the
world. That isn't something that any
harness handles natively, so that's
something we had to build.
We can come back to sessions in the
future and like rehydrate them, so we
had to whole build a whole thing for for
that. That's not really a native
feature. Credential isolation is that
wrapper thing that I mentioned.
Um there's a
weirdly annoyingly amount of
an annoying amount of stuff to handle
messages coming out of the models and
make sure that they're not just like
lost to standard out. You know, just
like if you've worked with models a lot,
it's the kind of stuff that you're used
to being a bit annoying.
Um
And number seven, yeah, we use event
sourcing. We We're really happy with
that pattern.
Uh that's not a small lift. Um I guess
you don't need to I think I think most
people would probably need to do three,
four, five, and six.
Would recommend number two. I guess you
have to do one. That's obvious.
Um number seven, you have to do
something there. And eight,
I've not mentioned this, but yeah,
I I I guess I said before that we're
really pri- We really pride ourselves on
accuracy and um
uh and robustness and and truth and
trustworthiness. And we have a dedicated
eval team who are great. Uh
It's so hard to do eval when the the
system is like writing programs and
executing them on the fly. Like it's
just a very complex dynamic um
domain to be in.
Um but we've invested a lot of time
there, and I'd really strongly recommend
that you do the same. Um
If you're doing a kind of DSL DSL-based
system.
Okay. So, let me uh let me finish where
I began.
The uh
example I gave at the beginning was
let's uh let's imagine two systems
produce identical output. And
should you trust it?
I think it's it's not crazy to imagine
Opus coming up with one of those tables
that I was just showing. I didn't show a
bunch of the fe- I just because of time,
there's a bunch of features there that
um
are really important to us, but at
certainly at least at a surface level,
the table itself isn't like a crazy
thing to imagine a state-of-the-art
model coming up with. However, the fact
that we go through a very particular
um and sort of painstaking process to
generate it, and we expose that in a
ergonomic way to the user, you know,
right with the SHPL and with that
graphical interface and a few of the
bells and whistles. I think that's the
thing that makes me think and know from
conversations with our users that they
hold they would hold those two things
quite differently. Like a a table like
that in in elicit is a is a
fundamentally different thing to a table
that's just, you know, being bubbled out
from a from a model. Um and maybe
there's something that kind of
has that same dynamic for you for your
for your business and and for your
product.
So, yeah, my my pitch here is not that
you should go and use a a DSL.
Um
my pitch is that you should care a lot
about the mechanism.
Um because the mechanism the mechanism
matters.
Okay.
That's it for me. Thank you very much.

## VN dub transcript (BizMate, deduped, read in full in main loop — dub artifacts: "sản phẩm chống hàng giả" mistranslation of "the Elicit product"; "Brandon Taste" = brand and taste; renders "3.5 Sonnet" correctly where EN captions garbled)

.
Tên tôi là James Brady.
Tôi làm việc tại Elicit, và hôm nay tôi sẽ chia sẻ về cách chúng tôi giúp các quy trình làm việc của agent trở nên đáng tin cậy và có thể kiểm chứng thông qua một ngôn ngữ đặc thù cho miền riêng.
Về cấu trúc buổi nói chuyện hôm nay, tôi sẽ bắt đầu bằng cái nhìn tổng quan về lý do chúng tôi chọn sử dụng DSL ngay từ đầu, sau đó nói sơ qua về ngôn ngữ này, cách chúng tôi đưa ra các quyết định trong thiết kế, cách tích hợp nó vào Elicit, và chúng ta sẽ có một bản demo nhanh.
rồi kết thúc phần trình bày ở cuối.
Nhưng trước hết, hãy để tôi đặt một câu hỏi.
Giả sử hai hệ thống khác nhau tạo ra cùng một kết quả đầu ra.
Liệu bạn có tin tưởng chúng như nhau không?
Và câu trả lời tất nhiên là, điều đó còn tùy thuộc.
Nó phụ thuộc vào những gì đã diễn ra bên trong các hệ thống đó để tạo ra kết quả đầu ra ấy.
Tôi cho rằng cơ chế, tức là cách thức tạo ra câu trả lời, quan trọng theo một khía cạnh khác so với chính kết quả đầu ra cuối cùng.
Hãy để tôi cố gắng minh họa điều này một cách cụ thể hơn.
Giả sử bạn đang chạy một công cụ phân tích tĩnh trên kho mã nguồn của mình, nó hoạt động trong một khoảng thời gian, và cuối cùng thông báo rằng mã này không có lỗ hổng bảo mật, an toàn để triển khai lên môi trường production.
Tôi sẽ phản đối nếu bạn biết hệ thống đó được xây dựng trên, chẳng hạn như, một model cũ, ví dụ như 3.5 Sonnet, hoặc tương tự.
Nếu hệ thống sử dụng một model cũ như vậy, đó là phương án một, còn phương án hai là nó sử dụng model tiên tiến nhất và hiện đại nhất.
Nó đã thực hiện đủ loại việc sử dụng công cụ.
Nó đã thực hiện việc phê bình và viết lại bản thảo.
Đó thực chất là một loại đối tượng hoàn toàn khác biệt.
Thông điệp có thể giống hệt nhau về mặt chữ nghĩa, nhưng bạn sẽ phản ứng rất khác nhau đối với hai thông điệp đó nếu một cái đến từ model cũ kém mạnh mẽ, so với một cái sử dụng nhiều token và trí thông minh hơn.
Vì vậy, cơ chế thực sự là yếu tố then chốt.
Và thực tế không có một cơ chế duy nhất nào được coi là hoàn hảo.
Cũng không tồn tại một phương pháp chuẩn mực duy nhất để thiết kế cấu trúc bên trong của các hệ thống mà bạn đang xây dựng.
Tôi thực sự tin rằng đây là một sự lựa chọn về mặt thiết kế.
Nó phụ thuộc vào mục tiêu cụ thể mà bạn đang hướng tới.
Nó còn phụ thuộc vào lĩnh vực mà bạn đang phát triển.
Nó cũng phụ thuộc vào người dùng.
Nó phụ thuộc vào nhiệm vụ, cụ thể là những gì người dùng đang thực hiện trong lĩnh vực đó.
Chúng tôi nhận thấy rõ ràng có sự đánh đổi giữa tốc độ và độ chặt chẽ.
Vì vậy, nếu bạn đang cố gắng thực hiện một công việc đòi hỏi chiều sâu cực lớn, tính phòng thủ cao và chất lượng tối ưu, thì điều đó tất nhiên sẽ tốn nhiều thời gian hơn so với những công việc chỉ ở mức độ bề nổi.
Không có câu trả lời nào là đúng đắn tuyệt đối.
Đôi khi bạn cần tốc độ, nhưng đôi khi bạn lại cần chất lượng thực sự rất cao.
Các nhà cung cấp, Brandon Taste, thực sự rất thú vị trong vấn đề này.
Tôi không chắc mình đã gọi tên điều này trước khi chúng tôi bắt tay vào làm, nhưng Elicit tự hào về độ tin cậy cực cao, chất lượng thực sự vượt trội và nguồn gốc dữ liệu rõ ràng.
Chúng tôi thực sự cam kết với những kết quả mà chúng tôi đưa ra trước mắt mọi người.
Tôi sẽ trình bày một bản demo về những gì tôi vừa nói ở phần sau của video.
Đây là một số mối quan tâm mà chúng tôi đã cân nhắc khi tự hỏi, thì cơ chế nào là...
Chúng ta biết cơ chế rất quan trọng, nhưng đâu là cơ chế phù hợp nhất đối với chúng tôi với tư cách là một danh sách?
Và tôi nghĩ nó đã quy về ba tiêu chí mong muốn này khi chúng tôi xây dựng research agent của mình, đây cũng sẽ là bản demo trong vài phút tới.
Trước hết, quy trình của research agent phải dễ hiểu.
Nó cần phải dễ hiểu đối với người dùng và đồng thời, cũng cần phải dễ hiểu đối với các agent khác.
Chúng ta mong muốn quy trình, thuật toán và tập hợp các bước nội bộ mà agent thực hiện phải có khả năng được con người kiểm tra ngẫu nhiên, cũng như được các agent khác kiểm tra.
Chúng ta có thể triển khai các agent chuyên về đánh giá phê bình để giám sát quy trình này, cùng nhiều hình thức kiểm soát tương tự.
Yêu cầu thứ hai là quá trình lặp lại phải duy trì được độ trung thực và chính xác của kết quả.
Đây có thể là một điểm hơi phức tạp, nên hãy để tôi giải thích kỹ hơn một chút.
Những gì tôi nhận thấy, và có thể cả các bạn cũng từng gặp, là khi bạn đang lặp lại để cải thiện một phần công việc và nhận thấy nó chưa hoàn toàn chính xác, bạn muốn điều chỉnh hướng đi, thêm một lớp xử lý mới hoặc xem xét thêm một khía cạnh khác.
Tôi nhận ra rằng đôi khi bạn có thể bị lệch hướng so với mục tiêu ban đầu, khiến mô hình trở nên bối rối, và bạn buộc phải yêu cầu bắt đầu lại hoặc quay ngược lại các bước trước đó.
Điều này khá gây khó chịu và chắc chắn làm suy giảm niềm tin vào hệ thống.
Vì vậy, chúng ta cần tránh tình trạng đó và đảm bảo có thể bổ sung thêm vào công việc một cách linh hoạt.
Chúng ta cần có khả năng thêm các lớp xử lý mới, di chuyển theo các hướng khác nhau mà không làm mất đi sự rõ ràng và tính nhất quán so với những gì người dùng ban đầu mong muốn thực hiện.
Và cuối cùng, nhưng không kém phần quan trọng, là quy trình phải được tuân thủ một cách trung thành và chính xác.
Vì vậy, giả sử chúng ta có một quy trình như thế này, nó dễ đọc, chúng ta đã kiểm tra nó, người dùng cũng đã kiểm tra, mọi thứ đều tuyệt vời, và chúng ta đã lặp lại quá trình này trong khi vẫn giữ đúng những gì người dùng quan tâm, thì chúng ta thực sự phải đảm bảo hệ thống thực hiện đúng tập hợp các bước đó.
Nếu không, thì rốt cuộc chúng ta đang làm gì ở đây chứ?
Vì vậy, đó chính là những cân nhắc mà chúng tôi ưu tiên hàng đầu khi nghĩ về cách chúng tôi muốn Elicit hoạt động.
Và điều đó đã dẫn chúng tôi đến việc lựa chọn DSL.
Tôi không nói rằng mọi người đều nên sử dụng DSL.
Bạn không nên làm vậy. Những gì tôi muốn nói là ba yếu tố này thực sự đã dẫn dắt một cách tự nhiên đến kết luận rằng, thì DSL có thể là một lựa chọn tuyệt vời cho chúng tôi.
Vì vậy, DSL của chúng tôi có tên là AshPL.
Cụm từ A-E bị ghép lại kỳ lạ này, theo như tôi biết, được gọi là Ash.
Nó giống như một nguyên âm đôi trong tiếng Anh cổ hay một thứ tương tự như vậy.
Vì vậy, AshPL.
Và đây chính là ngôn ngữ đặc thù cho lĩnh vực của chúng tôi dành cho các quy trình làm việc tự động trong sản phẩm chống hàng giả.
Và AshPL sở hữu một vài yếu tố phân biệt riêng biệt.
Trước hết, nó không đầy đủ theo chuẩn Turing.
Nó tương đối đơn giản và hoàn toàn không có vòng lặp.
Không có đệ quy, không có sự thay đổi trạng thái, nó mang tính hàm thuần túy, là một ngôn ngữ phản ứng, và là một tập con có định hướng rõ ràng của Python.
Và tính định hướng này là rất quan trọng ở đây.
Do đó, nó không chỉ là một sự đơn giản hóa chung chung của Python, hay nói cách khác, không phải là Python bị cắt bớt ngẫu nhiên một vài thành phần.
Những gì chúng tôi làm là loại bỏ các tính năng ngôn ngữ của Python không thực sự hữu ích, đồng thời bổ sung thêm các nguyên thủy đặc thù dành riêng cho lĩnh vực của chúng tôi.
Lĩnh vực của chúng tôi chính là nghiên cứu khoa học và ra quyết định dựa trên bằng chứng thực nghiệm, đặc biệt là các quyết định mang tính rủi ro cao.
Và các nguyên thủy mà chúng tôi tích hợp vào DSL này đều được thiết kế để phù hợp với đặc thù đó.
Bạn biết đấy, việc truy xuất các bài báo nghiên cứu học thuật hay các thử nghiệm lâm sàng, những thứ như vậy, đã được tích hợp sẵn vào ngôn ngữ này.
Được rồi.
Đúng vậy, hãy cùng xem qua một số đoạn mã HPL.
Hy vọng rằng kích thước này không quá nhỏ so với mọi người.
Rõ ràng là bạn không cần phải đọc từng dòng code.
Điều tôi muốn minh họa ở đây là mã HPL bên phải trông rất giống Python, bởi vì nó thực chất là một tập con của Python.
Chúng tôi rất chú trọng đến việc kiểm soát kiểu dữ liệu.
Việc có kiểu dữ liệu cho phép chúng ta thực hiện các bản nháp lại nhanh chóng nếu gặp lỗi về kiểu.
Và tôi nghĩ rằng chương trình ví dụ này, chỉ để bạn biết, chính là quy trình mà chúng tôi muốn thực hiện để tiến hành phân tích cạnh tranh cho chính Elicit.
Vì vậy, chúng tôi đang tìm kiếm các công cụ tìm kiếm học thuật khác và các công cụ hỗ trợ AI, có vẻ như là các công cụ đánh giá hệ thống.
Chúng tôi thực hiện tìm kiếm web cho những nội dung đó.
Sau đó, chúng tôi tổng hợp các kết quả và làm phong phú thêm nguồn dữ liệu.
Đây chính là chuỗi các bước mà chúng tôi muốn thực hiện, một quy trình hiệu quả để tổng quan về bối cảnh cạnh tranh.
Và cốt lõi của những gì diễn ra trong phiên làm việc của người dùng trái phép là chúng tôi có một thành phần, sẽ được giới thiệu trong slide tiếp theo, có nhiệm vụ viết HPL, sau đó chúng tôi diễn giải HPL đó.
Việc này được thực hiện hoàn toàn bằng mã Python thuần túy.
Tiếp theo, chúng tôi viết lại HPL dựa trên những gì vừa xảy ra.
Vì vậy, trong một trường hợp đơn giản, bạn có thể hình dung chúng tôi viết một đoạn HPL.
Một lỗi về kiểu dữ liệu xuất hiện. Được rồi, chắc chắn có vấn đề ở đâu đó.
Do đó, thông tin này sẽ được chuyển ngược lại thành phần chuyên viết HPL.
Thành phần này sẽ thử lại và sửa lỗi kiểu dữ liệu đó.
Chúng ta sẽ diễn giải lại HPL, và lần này HPL sẽ được thực thi.
Chúng ta nhận lại một số kết quả, sau đó viết lại HPL.
Đó chính là vòng lặp không ngừng giữa việc viết, diễn giải, rồi viết lại và tiếp tục diễn giải.
Và đây chính là động cơ cốt lõi giúp tạo ra tiến bộ bên trong Elicit.
Được rồi, như vậy đó chính là ngôn ngữ.
Hãy để tôi cho bạn thấy cách chúng tôi tích hợp nó vào một hệ thống hoàn chỉnh hơn.
Vì vậy, chúng ta có giao diện người dùng nằm ở góc trên bên trái.
Đó chính là nơi người dùng tương tác.
Nó chỉ chạy trên trình duyệt web, và chúng ta sẽ xem xét điều này ngay trong bản demo sau một chút.
Giao diện người dùng sẽ giao tiếp với một nhật ký sự kiện chỉ cho phép ghi thêm, tức là append-only event log.
Đó chính là cách chúng tôi quản lý cấu trúc dữ liệu phân tán của mình.
Chúng ta có một dịch vụ Python ở góc trên bên phải, và dịch vụ này sẽ giao tiếp với sandbox nằm ở góc dưới bên phải, hay nói đúng hơn là khu vực phía dưới bên phải. Còn thành phần có màu cam đất, tức màu đặc trưng của Claude hay Anthropic, chính là bộ phận chịu trách nhiệm viết HPL.
Vậy nên, hãy để tôi bổ sung thêm một chút chi tiết ở đây.
Người dùng sẽ tương tác trực tiếp với giao diện người dùng.
Các sự kiện sẽ được phát sinh ngay khi họ nhấn nút, nhập truy vấn tìm kiếm và thực hiện các thao tác khác.
Những sự kiện này sẽ được thêm vào và ghi đè lên nhật ký sự kiện.
Dịch vụ Python đóng vai trò là trung gian tin nhắn cho cơ chế này, phục vụ cho mô hình nguồn sự kiện.
Sau đó, chính sandbox sẽ thực hiện việc viết HPL, còn dịch vụ Python sẽ đảm nhận việc diễn giải HPL.
Vì vậy, quy trình qua lại mà tôi đã đề cập, bao gồm việc viết HPL, sau đó diễn giải nó, rồi viết lại, mở rộng và tiếp tục diễn giải, diễn ra liên tục giữa hộp màu xám đậm và hộp màu cam.
Còn có một vài thành phần khác ở đây mà tôi sẽ đề cập đến sau.
Vì vậy, wrapper đóng vai trò như một lớp trừu tượng nằm phía trước cái mà chúng ta gọi là curator, chính là thành phần viết ra HPL.
Điều này cho phép chúng ta dễ dàng thay thế các harness khác nhau vào hệ thống.
Chúng tôi đã xây dựng một bản triển khai agent SDK dành riêng cho curator.
Chúng tôi cũng đã thử nghiệm việc sử dụng Pi kết hợp với Claude, và cả Pi với Codex.
Có lẽ tôi không nên nhắc đến Codex, nhưng thực tế chúng tôi đã thử nghiệm giải pháp đó.
Điều vô cùng quan trọng đối với chúng tôi là curator phải sử dụng những mô hình và harness tốt nhất hiện có.
Vì vậy, hiện tại chúng tôi đang dùng Pi kết hợp với các mô hình của Anthropic, đây là sự kết hợp tối ưu nhất cho chúng tôi.
Và gateway, đúng vậy, tất cả các tương tác mà chúng tôi thực hiện với các mô hình, với LLM, đều được chuyển hướng qua gateway này.
Lý do chính cho việc này là gateway nắm giữ thông tin về API key của chúng tôi.
Chúng tôi không muốn dữ liệu đầu vào của người dùng đi trực tiếp qua hệ thống, chạm tới curator và yêu cầu in ra EMV rồi gửi kết quả cho họ.
Vì vậy, hành động này chủ yếu nhằm mục đích bảo mật.
Hiển nhiên, đến thời điểm này thì mọi thứ vẫn còn khá trừu tượng.
Hãy để tôi giải thích chi tiết hơn về những gì xảy ra khi chúng ta viết và khi chúng ta diễn giải HBL.
Chúng ta sẽ bắt đầu từ bên trái và di chuyển sang bên phải.
Tôi đã đề cập rằng curator chính là thành phần màu cam.
Chính curator là người tạo ra HBL ngay từ đầu.
Khi tôi nói về việc lưu trữ trong sandbox, điều đó có nghĩa là chúng ta phát ra các sự kiện, chúng được thêm vào nhật ký sự kiện, và đó là cách dịch vụ Python nhận biết các chương trình HPL đã được cập nhật.
Chính dịch vụ Python thực hiện phần còn lại của công việc ở đây.
Vì vậy, trong hộp mô hình có kiểu dữ liệu này, dịch vụ Python sẽ phân tích cú pháp, kiểm tra tính hợp lệ của cú pháp và thực hiện kiểm tra kiểu dữ liệu.
Nếu có bất kỳ vấn đề nào xảy ra, chúng ta có thể gửi trả lại cho curator một cách rất nhanh chóng và thông báo rằng có lỗi chính tả.
Hãy xem dòng 52 và viết lại nó.
Sau khi hoàn tất việc phân tích cú pháp và đánh giá cùng các bước tiếp theo, chúng ta sẽ có được một cấu trúc tương tự như cây cú pháp trừu tượng, từ đó có thể duyệt qua và bắt đầu thực hiện việc diễn giải.
Và việc diễn giải này, một lần nữa, chính là mã Python thuần túy.
Vì vậy, chúng ta không sử dụng...
Ở thời điểm này, chúng ta có thể gọi vào các mô hình ngôn ngữ và các thành phần khác, nhưng chúng ta sở hữu mã Python có khả năng duyệt qua cây của một chương trình, hiểu về các hàm đóng, nắm rõ các dạng thức đặc biệt và nhận biết các nguyên tố ngôn ngữ khác nhau mà chúng ta có sẵn.
Một điểm cực kỳ quan trọng đối với chúng ta ở đây là kho lưu trữ địa chỉ nội dung.
Đây chính là yếu tố cho phép chúng ta thực hiện việc lưu trữ bộ nhớ đệm và ghi nhớ kết quả.
Điều này vô cùng quan trọng; nếu chúng ta không hết sức cẩn thận trong vấn đề này thì mọi thứ sẽ không thể hoạt động được.
Lý do tôi nói vậy là bởi vì, một lần nữa, chúng ta viết lại toàn bộ chương trình LashPL và diễn giải lại toàn bộ nó mỗi lần thực hiện.
Chúng ta không chỉ diễn giải phần mã bổ sung đã được viết lại.
Chúng tôi sẽ viết lại chương trình và diễn giải lại toàn bộ hệ thống từ trên xuống dưới.
Việc này sẽ cực kỳ chậm chạp nếu chúng ta phải làm lại công việc mỗi khi lặp lại vòng lặp.
Trong thực tế, quy trình này diễn ra rất nhanh nhờ các tính năng của ngôn ngữ, chẳng hạn như việc đây là một ngôn ngữ thuần túy hỗ trợ rất tốt cho việc ghi nhớ; chúng ta có thể băm một biểu thức và nếu biểu thức đó đã được đánh giá trước đó, chúng ta chỉ cần lưu kết quả vào một bản đồ.
Và nếu chúng ta gặp lại biểu thức đó khi duyệt qua cây, chúng ta có thể xác nhận rằng kết quả đã được rút gọn thành 42 hoặc một giá trị tương tự.
Chúng ta có thể sử dụng ngay kết quả đó từ bản đồ băm.
Được rồi, tôi nghĩ đó là tất cả những gì tôi muốn nói về vấn đề này.
Vì vậy, tôi sẽ chuyển sang phần minh họa ngay bây giờ.
Và...
Như tôi đã đề cập trước đó, thường sẽ có sự đánh đổi giữa tính chặt chẽ và tốc độ.
Trên phổ liên tục đó, chúng tôi tập trung rất nhiều vào khía cạnh tính chặt chẽ.
Chúng tôi có thể xử lý nhanh các truy vấn đơn giản, nhưng đó không phải là điểm tạo nên sự khác biệt của chúng tôi.
Nói cách khác, đó cũng không phải là nguồn lợi thế đặc biệt của chúng tôi.
Vì vậy, nếu bạn truy cập vào illicit.com, bạn sẽ thấy giao diện tương tự như thế này.
Chúng tôi cung cấp một loạt các mẫu để bạn bắt đầu, chẳng hạn như tạo bảng, trình chiếu hoặc soạn thảo báo cáo.
Tôi sẽ giới thiệu cho bạn một không gian nghiên cứu, mà theo tôi, tổng thời gian thực hiện có lẽ chỉ mất vài giờ, bao gồm cả công việc của hệ thống và việc tôi bổ sung các lớp chức năng lên trên đó.
Do đó, tôi không thể thực hiện điều này dưới dạng một bản demo trực tiếp.
Tuy nhiên, tôi đã lưu lại một phiên làm việc mà chúng ta sẽ cùng xem xét.
Nhưng thực tế, quy trình này không cần phải mất nhiều thời gian như vậy.
Vấn đề sẽ trở nên thú vị hơn khi chúng ta xử lý những nội dung chi tiết và sâu sắc hơn.
Vì vậy, đây chính là không gian nghiên cứu mà chúng ta sẽ cùng tìm hiểu trong phần này.
Và truy vấn ban đầu của tôi là lập bản đồ các công ty và tổ chức đầu tư vào các mô hình nền tảng cho lĩnh vực sinh học.
Bạn có thể thấy rằng điều đầu tiên chúng tôi thực hiện ở đây là Elissa đã đặt câu hỏi cho tôi.
Cô ấy nói đại loại là, được rồi, tôi đã nắm được bức tranh tổng thể.
Hãy để tôi thu hẹp phạm vi lại một chút.
Bạn có quan tâm đến một bức tranh toàn cảnh rộng lớn không?
Tôi nghĩ các lựa chọn khác ở đây là liệu bạn có quan tâm đến một mô hình nền tảng cụ thể nào đó không.
Hay bạn quan tâm nhiều hơn đến các tổ chức học thuật hay các công ty?
Đó là loại câu hỏi như vậy, và tôi chỉ trả lời rằng, vâng, bức tranh toàn cảnh rộng lớn là những gì tôi đang tìm kiếm.
Sau đó, các bước còn lại ở đây được điều khiển bởi HPL.
Vì vậy, bạn có thể thấy bước phân tích đầu tiên này.
Nếu ai đó không thể nhìn rõ và cần phóng to, xin vui lòng cho biết.
Bạn không cần phải đọc được toàn bộ văn bản chi tiết, nhưng cũng được.
Tôi sẽ tiếp tục với nội dung hiện tại. Vì vậy, khối phân tích đầu tiên chúng ta thực hiện bao gồm rất nhiều lượt tìm kiếm.
Chúng tôi đang tìm kiếm các bài báo học thuật liên quan đến việc tiền huấn luyện mô hình nền tảng hệ gen sử dụng kiến trúc transformer.
Chúng tôi thực hiện một số tìm kiếm trên web.
Chúng tôi cố gắng truy xuất toàn văn của các bài báo khi có sẵn.
Chúng tôi thực hiện một số bước sàng lọc, chẳng hạn như lọc dữ liệu.
Tất cả các bước này, tất cả các giai đoạn này đều được mã hóa vào HPL, và sau đó chúng tôi chạy...
Thực tế thì...
HPL không chỉ đơn thuần là một bản thể hiện của kế hoạch.
Nó thực sự là một kế hoạch có thể thực thi, điều này giúp chúng ta hoàn toàn chắc chắn rằng mình đang tuân thủ đúng kế hoạch đã đề ra.
Vì vậy, hãy để tôi đi sâu hơn vào vấn đề này một chút.
Đó chính là giai đoạn phân tích đầu tiên khi chúng tôi tìm kiếm các tổ chức và các cơ quan.
Có vẻ như chúng tôi đã thực hiện thêm một số bước phân tích ở đây.
Tôi nghĩ trường hợp này thì...
Được rồi, đến thời điểm này, chúng tôi đã có được một số cơ quan thực tế.
Chúng tôi có Viện Y học Howard Hughes, Đại học Stanford, và nhiều nơi khác nữa.
Một lần nữa, tất cả những điều này đều đến từ HPL, chúng tôi đang thực hiện thêm các tìm kiếm và sàng lọc.
Đúng vậy, bạn có thể thấy chúng tôi đi rất sâu khi hoạt động ở chế độ này.
Hãy để tôi tua nhanh đến phần kết quả ở đây.
Và tôi sẽ thu gọn thanh bên này lại.
Vì vậy, sau một hồi xử lý và tiêu tốn khá nhiều token, chúng ta đã có được một bảng như thế này.
Chúng tôi gọi đây là một artifact, và mỗi hàng trong đó, trong trường hợp này, là một tổ chức có sự quan tâm nào đó đối với các mô hình nền tảng sinh học.
Chúng ta có GDM, Meta, Microsoft Research, vân vân và vân vân.
Và bạn có thể thấy rằng chúng tôi đã trích xuất một số thuộc tính đi kèm với thông tin đó.
Đó là các mô hình nền tảng mà họ đã tạo ra, các phương thức mà họ quan tâm, cùng những hợp tác đáng chú ý, có vẻ như vậy.
Vì vậy, tôi đã nói rằng điều này được điều khiển bởi HPL, nhưng làm sao bạn có thể biết được điều đó?
Bạn biết đấy, mối liên kết ở đây là gì?
Đối với mỗi artifact này, chúng ta thực sự có thể xem xét mã HPL đã được sử dụng để tạo ra nó.
Vì vậy, đây chính xác là DSL có thể thực thi nằm đằng sau việc tạo ra bảng mà chúng ta vừa xem.
Và bạn có thể thấy rằng trước hết, chúng ta đang thực hiện một số tìm kiếm web về các foundation models, sinh học đa phương thức, AI và nhiều chủ đề khác.
Bạn có thể thấy điều này, khi chúng ta lại tiếp tục tìm kiếm các bài báo học thuật.
Tôi cho là chúng ta sẽ kết nối những kết quả này lại với nhau tại một thời điểm nào đó.
Đúng vậy, đó chính là nơi diễn ra thao tác kết nối.
Và như bạn có thể nhận ra, việc xem xét HPL này không thực sự mang lại nhiều niềm vui.
Hầu hết mọi người đều không làm điều này.
Và đó thực sự không phải là động lực cốt lõi lý do tại sao chúng ta có hệ thống này.
Chúng ta có nó vì chúng ta muốn đảm bảo rằng Elicit, hệ thống này, đang tuân thủ đúng các chỉ dẫn mà chúng ta đã đề ra.
Phải không? Đó chính là điều quan trọng hàng đầu.
Tuy nhiên, việc các agent khác có thể xem HPL này lại rất hữu ích, để họ có thể nhận ra rằng bạn đã bỏ sót điều gì đó, hoặc bạn đã không xem xét một từ khóa tìm kiếm quan trọng, hoặc thậm chí là một phần trong truy vấn của người dùng mà bạn chưa tính đến.
Điều này thực sự hữu ích khi kế hoạch được trình bày rõ ràng theo định dạng này.
Một cách tiếp cận hữu ích hơn từ góc độ người dùng, mang tính trực quan và dễ thao tác hơn, chính là biểu đồ đồ họa mô tả những gì diễn ra trong hệ thống.
Vì vậy, hình ảnh này được suy ra trực tiếp, bạn biết đấy, từ FPL.
Đây không chỉ đơn thuần là một loại hình ảnh hóa đẹp mắt được bịa đặt hay bất cứ điều gì tương tự.
Nó thực sự được tạo ra trực tiếp từ chính thứ mà kế hoạch đang thực thi.
Và tôi nghĩ trong trường hợp này, nó khá tuyến tính nên không quá thú vị.
Nhưng, vâng, chúng ta bắt đầu với một vài lần tìm kiếm.
Sau đó thực hiện làm giàu dữ liệu, nghĩa là lấy toàn văn của các bài báo, những việc kiểu như vậy.
Tiếp đến là trích xuất và biên tập, tức là lọc dữ liệu, thực hiện thêm một số tìm kiếm, vân vân.
Vì vậy, tôi thực sự thấy việc quan sát điều này khá hữu ích nếu tôi đang cố gắng thuyết phục bản thân mình có nên ủng hộ quy trình mà Elicit đã thực hiện hay không.
Và bạn có thể nhanh chóng nhận ra khi có điều gì đó trông hơi bất thường.
Tuy nhiên, tôi sẽ không dừng lại ở đây, đúng không?
Bởi vì còn có những lớp khác của quá trình điều tra này mà tôi muốn bổ sung thêm.
Vì vậy, tôi nghĩ rằng tôi đã thực hiện một vài việc ở đây.
Đúng vậy, tôi đã yêu cầu so sánh các chiến lược nguồn mở và nguồn đóng cho các tổ chức khác nhau.
Chúng tôi đã thực hiện một số công việc cho việc đó.
Sau đó, tôi yêu cầu chiến lược thương mại hóa và cách tiếp cận GTM, và chúng tôi cũng đã hoàn thành công việc cho phần này.
Tiếp theo, tôi đã yêu cầu, như bạn có thể thấy, một artifact khác đã được tạo ra.
Tôi nghĩ điều tiếp theo tôi quan tâm là, ồ, tôi đã bỏ sót một khối ở đây.
Thế này thì ổn rồi, đúng không, việc ánh xạ các tổ chức chính phủ khác nhau và các cơ quan giám sát khác.
Tôi đã thực hiện một số công việc cho điều đó. Và sau đó, vào cuối phiên làm việc của người dùng này, chúng ta có...
Tôi đã yêu cầu một thao tác join.
Vì vậy, chúng ta thực chất có một bảng dữ liệu chính là các tổ chức.
Chúng ta cũng có một bảng dữ liệu khác là các cơ quan giám sát.
Và chỉ bằng ngôn ngữ tự nhiên, tôi có thể nói rằng tôi muốn join các bảng này lại với nhau để xem các phòng thí nghiệm đã tương tác như thế nào với các cơ quan giám sát.
Và kết quả là chúng ta có được bảng dữ liệu này.
Chúng ta có thể thấy Anthropic đã tương tác với Viện An toàn AI Hoa Kỳ và AC tại Vương quốc Anh, và nhiều đơn vị khác nữa.
Và nếu tôi xem xét mã ACHPL cho bảng này, điều bạn có thể nhận thấy là phần đầu của chương trình hoàn toàn giống với những gì chúng ta đã có trước đó.
Vì vậy, đây chính là các truy vấn web và truy vấn tài liệu giống hệt những gì chúng ta đã có cho bảng đầu tiên mà chúng ta đang xem xét.
Và toàn bộ phần này đều là cùng một đoạn mã.
Nó đã bao gồm các đề cập đến tổ chức. Tôi đoán phần join sẽ nằm ở phía dưới này một chút.
Giống như, đây vẫn là những nội dung tương tự như những gì chúng ta đã xem xét trước đó.
Điểm khác biệt là chương trình này giờ đây, nói cách khác, dài hơn rất nhiều.
Tôi nghĩ bản trước đó chỉ khoảng 100 dòng, 150 dòng thôi.
Còn bây giờ chúng ta đã lên tới khoảng 1.000 dòng, thậm chí nhiều hơn một chút.
Và chỉ khi chúng ta đi xuống tận cùng ở đây thì mới bắt đầu nói về...
Đúng vậy. Bạn có thể thấy chúng ta đang xem xét các cơ quan giám sát và sự tương tác giữa những cơ quan đó với các phòng thí nghiệm ở đây.
Chúng ta đang nói về vấn đề giám sát. Đây chính là mô hình cho một phòng thí nghiệm tương tác với một cơ quan giám sát.
Và tại thời điểm tạo ra bảng cuối cùng đó, chúng ta sẽ phải diễn giải lại toàn bộ chương trình này từ đầu, ngoại trừ việc có bộ nhớ đệm mà tôi đã đề cập.
Vì vậy, thực tế là chúng ta đã thực hiện tất cả những việc ở phía trên này, bao gồm tất cả các truy vấn web và tìm kiếm tài liệu, v.v., có nghĩa là chúng ta có thể diễn giải lại toàn bộ chương trình từ đầu, nhưng phần lớn trong số đó chỉ là các ghi nhớ và bạn sẽ nhận lại kết quả ngay lập tức.
Một trong những lý do chúng tôi đưa ra quyết định thiết kế đó là vì nó giúp chúng ta dễ dàng tự tin và đưa ra các đảm bảo thống kê về tính gắn kết cũng như độ chính xác, khi mà chúng ta thực sự diễn giải toàn bộ chương trình mỗi lần thực thi.
Bạn biết đấy, nếu bạn chỉ diễn giải những đoạn mã nhỏ lẻ, thì đó chính là nơi mà sự sai lệch mà tôi đã đề cập trước đó có thể xuất hiện.
Đó chính là một trong những điểm mà sự sai lệch có thể xảy ra.
Được rồi.
Vậy chúng ta có thể quay lại với các slide trình chiếu được không?
Đó là phần trình diễn demo.
Được rồi, một lần nữa, tôi không nói rằng mọi người đều nên sử dụng một DSL.
Nó không phải là thứ dễ dàng nhất để xây dựng.
Tôi không biết nữa, có lẽ cũng không đến mức quá tệ.
Nhưng đó là loại giải pháp mà bạn nên hướng tới nếu các yêu cầu cần thiết cho sản phẩm và tổ chức của bạn đang dẫn bạn theo hướng đó.
Nếu họ làm được điều đó, thì thật tuyệt vời.
Chúng tôi thực sự rất hài lòng về cách nó đang hoạt động đối với chúng tôi.
Nhưng một lần nữa, Elicit được xây dựng dựa trên và thực sự xoay quanh độ tin cậy chất lượng cao, tính mạnh mẽ, nguồn gốc dữ liệu, tất cả những điều tôi vừa đề cập, và đó là lý do chúng tôi lựa chọn nó.
Nếu bạn đang ở trong một vị trí tương tự, hoặc bạn nhận thấy có những tiêu chí khác có thể dẫn đến một DSL khác phù hợp hơn, thì đây là một số điều bạn nên cân nhắc.
Đây là một số điều bạn nên suy nghĩ về.
Vì vậy, trước hết và rõ ràng nhất, bạn cần một DSL.
Và phần liên quan đến khả năng sử dụng của agent ở đây, ý tôi là, trước hết, chúng tôi nhận thấy bạn sẽ có trải nghiệm tốt hơn nếu bạn xây dựng DSL của mình dựa trên một ngôn ngữ hiện có với rất nhiều ví dụ trong dữ liệu huấn luyện, bởi vì khi đó, mô hình, hay người quản lý trong trường hợp của chúng tôi,
sẽ không cần phải học cú pháp, đúng không?
Nó chỉ cần biết rằng có một tập con mà nó có thể sử dụng.
Và tôi sẽ nói rằng lượng công sức bỏ ra cho DSL này khá nhỏ so với mọi thứ khác.
Mọi thứ còn lại cũng giống như kỹ thuật phần mềm truyền thống để thực sự biến nó thành một hệ thống hoạt động hiệu quả.
Và đó chính là nơi phần lớn công việc được thực hiện ở đây.
Như tôi đã đề cập đến lớp wrapper, đúng vậy, nó cho phép bạn chuyển đổi giữa các harness và model khác nhau, đồng thời xử lý các sự kiện gián đoạn.
Vì vậy, khi bạn đang trong một phiên làm việc và chờ đợi kết quả quay lại, bạn có thể thêm các nội dung khác vào cuộc trò chuyện, và chúng tôi muốn điều đó được chuyển tiếp mượt mà trở lại module curator để nó có thể viết lại kế hoạch mà không cần dừng toàn bộ hệ thống.
Đây không phải là điều mà bất kỳ harness nào cũng hỗ trợ sẵn, do đó chúng tôi đã phải tự xây dựng tính năng này.
Chúng ta có thể quay lại các phiên làm việc trong tương lai để khôi phục chúng, vì vậy chúng tôi đã phải xây dựng một giải pháp hoàn chỉnh cho việc này.
Đó không thực sự là một tính năng có sẵn; việc cô lập thông tin xác thực chính là chức năng của lớp wrapper mà tôi đã đề cập.
Có một lượng khá lớn và gây phiền toái các vấn đề cần xử lý đối với các tin nhắn đầu ra từ các model, nhằm đảm bảo chúng không bị thất lạc vào đầu ra tiêu chuẩn.
Nếu bạn thường xuyên làm việc với các model, thì đây là những thứ mà bạn đã quen thuộc với sự phiền toái nhất định.
Và thứ bảy, đúng vậy, chúng tôi sử dụng kỹ thuật event sourcing.
Chúng tôi thực sự hài lòng với mô hình đó.
Đó không phải là một nỗ lực nhỏ.
Tôi cho rằng bạn không nhất thiết phải làm tất cả, nhưng hầu hết mọi người có lẽ sẽ cần thực hiện các bước từ ba, bốn, năm đến sáu.
Tôi khuyên bạn nên chọn số hai, còn bước một thì chắc chắn bạn phải làm.
Điều đó là hiển nhiên rồi. Còn số bảy, bạn bắt buộc phải thực hiện một hành động nào đó ở đó.
Và ở bước tám, tôi chưa đề cập đến điều này, nhưng đúng là trước đây tôi đã nói rằng chúng tôi rất tự hào về độ chính xác, tính mạnh mẽ và khả năng đáng tin cậy của mình.
Chúng tôi có một đội ngũ đánh giá chuyên biệt và họ rất xuất sắc.
Việc thực hiện đánh giá trở nên vô cùng khó khăn khi hệ thống vừa viết chương trình vừa thực thi chúng ngay lập tức.
Đây vốn dĩ là một lĩnh vực rất phức tạp ngay từ đầu.
Tuy nhiên, chúng tôi đã đầu tư rất nhiều thời gian vào việc này, và tôi thực sự khuyên bạn nên làm tương tự nếu bạn đang xây dựng một hệ thống dựa trên DSL.
Được rồi.
Vậy để tôi quay lại điểm mà tôi đã bắt đầu.
Ví dụ tôi đưa ra lúc đầu là hãy tưởng tượng hai hệ thống tạo ra cùng một kết quả, và liệu bạn có nên tin tưởng nó hay không?
Tôi nghĩ rằng việc hình dung Opus tạo ra một trong những bảng biểu mà tôi vừa trình bày là điều hoàn toàn hợp lý.
Tôi không trình bày hết tất cả các tính năng chỉ vì lý do thời gian.
Có rất nhiều tính năng ở đó thực sự quan trọng đối với chúng ta, nhưng ít nhất là ở mức độ bề mặt.
Bản thân cái bảng đó không phải là điều gì quá khó để tưởng tượng một mô hình tiên tiến nhất có thể tạo ra.
Tuy nhiên, thực tế là chúng ta trải qua một quy trình rất đặc biệt và tỉ mỉ để tạo ra nó, đồng thời chúng ta trình bày điều đó một cách thuận tiện cho người dùng, phải không, thông qua HBL và giao diện đồ họa cùng một vài tính năng bổ trợ, tôi cho rằng chính điều đó khiến tôi nghĩ và biết từ các cuộc trò chuyện với người dùng của chúng ta rằng họ sẽ đánh giá,
họ sẽ đánh giá hai điều đó hoàn toàn khác biệt.
Giống như, một bảng biểu như vậy trong Elicit về cơ bản là một thứ khác biệt hoàn toàn so với một bảng biểu chỉ đơn thuần được đẩy ra từ một mô hình.
Và có lẽ cũng có một điều gì đó mang lại động lực tương tự cho bạn, cho doanh nghiệp và sản phẩm của bạn.
Vì vậy, thông điệp tôi muốn gửi gắm ở đây không phải là bạn nên đi và sử dụng một DSL.
Thông điệp của tôi là bạn cần quan tâm rất nhiều đến cơ chế, bởi vì cơ chế đóng vai trò then chốt.
Được rồi, đó là tất cả những gì tôi muốn chia sẻ. Xin cảm ơn rất nhiều.

## VN dub description (verbatim)

🤖 XÂY DỰNG AI AGENT ĐÁNG TIN CẬY | DSL VÀ QUY TRÌNH CÓ THỂ KIỂM CHỨNG

James Brady từ Elicit chia sẻ cách họ giải quyết bài toán cốt lõi của AI agentic: làm thế nào để cơ chế bên trong hệ thống trở nên minh bạch, có thể kiểm tra và đáng tin cậy. Bí quyết nằm ở một ngôn ngữ đặc thù tên AshPL — một tập con của Python được thiết kế riêng cho nghiên cứu khoa học và ra quyết định dựa trên bằng chứng.

📌 Nội dung chính:

🧠 Tại Sao Cơ Chế Quan Trọng Hơn Kết Quả
✅ Hai hệ thống cùng output nhưng khác nhau hoàn toàn về độ tin cậy
✅ Model cũ (3.5 Sonnet) vs. model tiên tiến nhất cho ra kết quả bề mặt giống nhau nhưng giá trị khác biệt
✅ Cơ chế là yếu tố then chốt quyết định liệu bạn có nên tin tưởng hệ thống

⚖️ Ba Tiêu Chí Thiết Kế Của Elicit
✅ Quy trình phải dễ đọc — cho cả người dùng lẫn các agent khác
✅ Lặp lại mà không làm lệch mục tiêu ban đầu của người dùng
✅ Hệ thống phải thực thi đúng kế hoạch đã kiểm tra

🔧 AshPL — DSL Của Elicit
✅ Không đầy đủ theo chuẩn Turing: không vòng lặp, không đệ quy, không thay đổi trạng thái
✅ Là tập con có định hướng của Python — model không cần học cú pháp mới
✅ Tích hợp sẵn các nguyên thủy cho nghiên cứu: truy xuất bài báo học thuật, thử nghiệm lâm sàng
✅ Kiểm tra kiểu dữ liệu cho phép phát hiện và sửa lỗi nhanh

🏗️ Kiến Trúc Hệ Thống Elicit
✅ Vòng lặp: Curator viết AshPL, Python interpreter thực thi, viết lại và tiếp tục
✅ Append-only event log quản lý trạng thái phân tán
✅ Content-addressed store cho phép memoization — không làm lại công việc đã xong
✅ Gateway tập trung xử lý API key và bảo mật

🎬 Demo Thực Tế: Phân Tích Cạnh Tranh AI Sinh Học
✅ Truy vấn: lập bản đồ các tổ chức đầu tư vào foundation models cho sinh học
✅ Elicit tìm ra Howard Hughes Medical Institute, Stanford, GDM, Meta, Microsoft Research
✅ Anthropic được xác định có tương tác với US AI Safety Institute và AI Safety tại UK
✅ Chương trình AshPL tăng từ 100-150 dòng lên 1.000+ dòng khi thêm lớp phân tích

---

🔗 Video gốc từ Anthropic (Tiếng Anh):
👉 https://www.youtube.com/watch?v=qOjleN2-50c

📢 Tại sao có video lồng tiếng và Vietsub này?
Video gốc của Anthropic được thực hiện hoàn toàn bằng tiếng Anh. BizMate Việt hóa toàn bộ khóa học với lồng tiếng và phụ đề tiếng Việt để cộng đồng Việt Nam tiếp cận AI một cách bình đẳng, không bị rào cản ngôn ngữ. Tất cả hoàn toàn miễn phí 🇻🇳

📚 Học toàn bộ khóa học miễn phí trên Skool:
👉 https://www.skool.com/bizmate-ai-community-9131

🏅 Thi chứng chỉ quốc tế từ Anthropic:
👉 https://anthropic.skilljar.com/


💡 Quote đáng nhớ:
"Cơ chế tạo ra câu trả lời quan trọng theo một chiều khác so với bản thân kết quả cuối cùng — đó là điều bạn không thể bỏ qua khi đánh giá độ tin cậy của hệ thống AI."
— James Brady, Elicit

"Nếu bạn chỉ diễn giải từng đoạn mã nhỏ lẻ, đó chính là nơi sự sai lệch tích lũy. Diễn giải toàn bộ chương trình mỗi lần mới đảm bảo tính nhất quán thực sự."
— James Brady, Elicit

🎯 3 Takeaway lớn nhất:
1️⃣ Cơ chế quyết định độ tin cậy. Hai hệ thống cho cùng output nhưng quy trình khác nhau tạo ra mức độ tin cậy hoàn toàn khác biệt — người dùng cảm nhận được sự khác biệt này.
2️⃣ DSL phù hợp giải quyết ba vấn đề cùng lúc. Tính dễ đọc, tính nhất quán khi lặp lại, và đảm bảo thực thi đúng kế hoạch — AshPL của Elicit được thiết kế để đáp ứng cả ba.
3️⃣ Memoization là chìa khóa cho hiệu suất. Viết lại và diễn giải toàn bộ chương trình mỗi lần đảm bảo tính chính xác, còn content-addressed store đảm bảo tốc độ — hai yếu tố không phải đánh đổi nhau.

🏷️ Tags:
#Claude #AnthropicClaude #Bizmate #AITiengViet #CodeWithClaude #HocMienPhi #AIAgent #DSL #Elicit #AgenticWorkflow #ResearchAI #LLMEngineering
