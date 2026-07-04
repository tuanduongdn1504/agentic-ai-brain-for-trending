---
source: path 5 yt-dlp (operator-submitted URL)
topic: agent-memory-architecture (DEEPEN — Anthropic Memory Stores + Dreaming first-party workshop)
generated: 2026-07-04
videos: 2 (VN dub b1qgIGwBUEI BizMate AI Official 2026-06-30 28:34 1,467 views 7,320 subs | EN original geUv4CjPpxI Claude channel 2026-05-23 28:42 22,035 views 472K subs)
provenance: BizMate video description links the Anthropic original and states full-course VN localization; attribution explicit, authorization not independently verified
speaker: Kevin, engineer at Anthropic (Code with Claude workshop: Agents that remember)
---

# Anthropic Memory Stores + Dreaming — Code with Claude workshop (VN dub + EN original transcripts)

## BizMate video description (verbatim)

WARNING: ffmpeg not found. The downloaded format may not be the best available. Installing ffmpeg is strongly recommended: https://github.com/yt-dlp/yt-dlp#dependencies
🧠 AGENTS THAT REMEMBER: KIẾN TẠO TRÍ NHỚ BỀN VỮNG CHO AI AGENT

Kevin, kỹ sư tại Anthropic, dẫn dắt buổi workshop chuyên sâu về cách xây dựng các AI Agent có khả năng ghi nhớ liên tục. Bài học này giới thiệu tính năng Memory Store và Dreaming mới, giúp các agent vượt qua giới hạn của phiên làm việc biệt lập để trở nên thông minh và hữu ích hơn trong quy trình thực tế.

📌 Nội dung chính:
🧩 Giới thiệu vấn đề Agent biệt lập
✅ Các agent hiện tại hoạt động độc lập, không lưu giữ thông tin giữa các phiên làm việc.
✅ Hạn chế lớn trong các quy trình làm việc dài hạn và phức tạp.
✅ Ví dụ thực tế: Agent không thể nhớ nội dung buổi thuyết trình CMA hôm qua khi gặp lại người dùng hôm nay.

💾 Giải pháp Memory Store (Kho lưu trữ bộ nhớ)
✅ Memory Store hoạt động như một hệ thống tệp tin bền vững gắn vào phiên làm việc.
✅ Agent có thể đọc và ghi dữ liệu qua nhiều phiên khác nhau, lưu trữ dưới dạng file (ví dụ: sessions.md).
✅ Hỗ trợ truy xuất mạnh mẽ thông qua các lệnh như grep để tìm kiếm từ khóa cụ thể.
✅ Cho phép tùy chỉnh quyền truy cập: chỉ đọc (read-only) hoặc đọc ghi (read/write).

🌙 Tính năng Dreaming (Tối ưu hóa bộ nhớ)
✅ Dreaming là tác vụ bất đồng bộ chạy ngầm để tổng hợp và làm sạch kho lưu trữ.
✅ Tự động kiểm tra tính xác thực, loại bỏ dữ liệu trùng lặp và bổ sung chi tiết bị thiếu.
✅ Tạo ra file index giúp agent truy xuất thông tin nhanh hơn thay vì quét toàn bộ dữ liệu.
✅ Quy trình không phá hủy: tạo ra kho lưu trữ đầu ra mới mà không xóa dữ liệu gốc.

🛠️ Hướng dẫn thực hành trên Console và CLI
✅ Tạo Memory Store mới và gắn vào phiên làm việc qua lệnh CLI.
✅ Theo dõi trạng thái Dream Job và xem chi tiết quá trình xử lý trên bảng điều khiển.
✅ Kiểm tra kết quả: Agent sử dụng output memory store để trả lời chính xác các câu hỏi về lịch sử.
✅ Quản lý phiên bản: Mỗi thay đổi trong memory store đều được lưu lại để dễ dàng theo dõi.

🚀 Lợi ích khi áp dụng cho doanh nghiệp
✅ Tăng hiệu quả làm việc của agent trong các dự án dài hạn và đa phiên.
✅ Giảm thiểu chi phí token nhờ cơ chế cache thông minh trong quá trình Dreaming.
✅ Khả năng mở rộng quy mô: Xử lý hàng trăm phiên làm việc mà không làm bộ nhớ bị quá tải.

---

🔗 Video gốc từ Anthropic (Tiếng Anh):
👉 https://www.youtube.com/watch?v=geUv4CjPpxI

📢 Tại sao có video lồng tiếng và Vietsub này?
Video gốc của Anthropic được thực hiện hoàn toàn bằng tiếng Anh. BizMate Việt hóa toàn bộ khóa học với lồng tiếng và phụ đề tiếng Việt để cộng đồng Việt Nam tiếp cận AI một cách bình đẳng, không bị rào cản ngôn ngữ. Tất cả hoàn toàn miễn phí 🇻🇳

📚 Học toàn bộ khóa học miễn phí trên Skool:
👉 https://www.skool.com/bizmate-ai-community-9131

🏅 Thi chứng chỉ quốc tế từ Anthropic:
👉 https://anthropic.skilljar.com/

---

⏱ Timestamps:
00:00 — Giới thiệu Kevin và chủ đề Agents có khả năng ghi nhớ
01:15 — Vấn đề của các agent hoạt động biệt lập hiện nay
02:45 — Giới thiệu khái niệm Memory Store và cách hoạt động
04:30 — Demo tạo phiên làm việc không có bộ nhớ
06:10 — Cách tạo và cấu hình Memory Store mới
08:20 — Tích hợp Memory Store vào phiên làm việc qua CLI
10:45 — Demo agent truy xuất thông tin từ Memory Store
13:00 — Giới thiệu tính năng Dreaming và mục đích
15:30 — Cách khởi tạo Dream Job và cấu hình tham số
18:10 — Quá trình Dreaming hoạt động và tạo file index
21:00 — So sánh kết quả giữa input và output memory store
23:45 — Lợi ích của việc tổ chức lại dữ liệu cho agent
26:10 — Câu hỏi về chi phí token và tối ưu hóa
28:30 — Tổng kết và lời khuyên cho người dùng

💡 Quote đáng nhớ:
"Agent cần một nơi để lưu trữ thông tin bền vững, giống như con người có trí nhớ dài hạn, thay vì chỉ tồn tại trong một phiên làm việc ngắn ngủi." — Kevin, Kỹ sư tại Anthropic

"Đừng để kho lưu trữ bộ nhớ phát triển vô hạn; hãy để Dreaming tự động làm sạch, tổ chức và làm giàu dữ liệu để agent thông minh hơn theo thời gian." — Kevin, Kỹ sư tại Anthropic

🎯 3 Takeaway lớn nhất:
1️⃣ Memory Store là nền tảng: Giúp agent lưu trữ và truy xuất dữ liệu xuyên suốt nhiều phiên làm việc khác nhau.
2️⃣ Dreaming là bộ não tổ chức: Tự động tinh lọc, loại bỏ trùng lặp và bổ sung chi tiết để tối ưu hóa hiệu suất truy xuất.
3️⃣ Kết hợp CLI và Console: Dễ dàng quản lý, theo dõi và kiểm soát quy trình ghi nhớ thông qua cả giao diện dòng lệnh và bảng điều khiển trực quan.

🏷️ Tags: #Claude #AnthropicClaude #Bizmate #AITiengViet #CodeWithClaude #HocMienPhi #AI Agents #MemoryStore #Dreaming #Anthropic #AIVietnam #TechEducation #CloudManagedAgents

## EN original transcript (geUv4CjPpxI, deduped auto-captions, read in full 2026-07-04)

Hello everyone. Thank you all for
joining us today.
Um my name is Kevin.
Uh I'm an engineer here at Anthropic and
today we'll be learning about how to
build agents that remember. Um so uh
today we're going to talk a little bit
about the base case with agents today,
uh which is that they're isolated and
this kind of limits their usefulness in
a lot of real-world workflows.
Uh we'll look at how we can actually
solve this problem uh with our new agent
memory stores feature that we've
launched. Uh this will give agents
access to a live memory store that they
can read and write to over multiple
sessions.
And then we'll look at how we can
improve these memory stores over time uh
using a new feature that we call
dreaming.
Uh and then finally we'll get to see how
all of this ties together with both our
CLI and also our awesome console
interface.
Um so in the previous uh workshops, I
think we've learned a little bit about
how Claude managed agents has these
concepts called an agent, environment,
and a session.
Uh in this workshop, we're going to add
two additional concepts here. The first
one here is a memory store. Uh so a
memory store is a persistent file system
like store that gives uh that it
attaches as a resource to sessions that
you create and it gives agents access to
uh it gives agents the ability to read
and write information across sessions.
A dream uh is what is is a asynchronous
job that runs in the background. Uh it
looks over an input memory store and a
bunch of your previous sessions that are
represented as transcripts and then we
run a harness over them to distill new
information that maybe the original
agents missed. We do things like
fact-checking.
Uh we also organize and consolidate and
deduplicate information so that your
memory stores don't grow unbounded over
time.
So uh also in case anyone in this room
has not already uh downloaded the
workshop repository you'll need for
this, uh here is the URL.
I'll give a few seconds for folks to
just grab that. Okay.
Um so, let's kind of like talk a little
bit about the problem today. So, when
you when you create agents on Cloud AI
today and sessions,
um most of the time you're creating one
session at a time and these are
isolated, right? The agent doesn't
remember information from the past and
it doesn't transfer information to
future sessions. Um so, I want to kind
of like take us through this this base
case today.
Uh so, if I switch over to my computer,
um I'm in our workshop repository here.
Uh hopefully everyone can see this uh in
the back, but I've just run the
bootstrap script that we've uh included
in the repository.
Uh and what this has done is basically
created uh some seed information for us.
So, we have an agent,
uh we have an environment, we have a few
like previous sessions that talk about
things like the keynotes uh from day one
as well as you know uh a previous
workshop.
And so, uh what I'm going to do from
here
is actually go ahead and start walking
through this guide with you guys. Feel
free to follow along on your computers.
Uh I'll be using the CLI and then also
showing kind of the console interface uh
for each of these steps.
So, first we're going to create uh a
session that basically tells it some
some new information. Uh
So, I'm going to copy this command here.
And as you can see, we are creating a
session with the agents that we've
created before
uh with the environment ID.
Uh and we've given it a title here of
just like write test with no memory.
Great. Uh so, now that we created this
session, uh I'm going to quickly switch
over to my console here.
Um and you'll see that
uh let me just move this over. You'll
see that the session shows up in
console. Uh it doesn't it has a status
of idle, nothing running yet.
Uh so then we're going to switch back
and then I'm going to send
this session some new information.
Uh so once I copy this,
and what I'm doing here is sending a
first user message here with information
about the CMA talk yesterday, uh
naming a few keywords like multi-agent
orchestration multi-agent orchestration
outcomes and memory. And I've also just
given it this URL, you know, example
that I took notes and uploaded them
here.
So if I switch back over to my console,
uh we should see this event pop up.
And what we sort of expect the the agent
or the model will do here is it'll just
respond say like, "Great. Thanks for the
information.
Not sure what else you want me to do
here." Uh so we'll give it a sec
and maybe folks to catch up.
Let's see if we get a little refresh.
Ah, sorry.
Yeah, so it looks like the model
responded here.
Uh let's collapse this. Yeah, it's
basically saying, "Okay, great. Thanks
for telling me this information."
Uh so then if we go
Sorry?
Uh this is using, I believe, Sonnet, the
agent that was created at the beginning.
Yeah.
Um
Cool. So if I go back here uh
to my workshop here, we're going to
create basically a second section that's
kind of the retest. So I'll go through
these steps a little bit faster.
Uh and then again, I'll send it a
message here that's this time I'm going
to ask it for information about the
stuff that I just told it.
And if I go back to our console here and
check out the other session that should
have been created,
we would expect the agent to basically
um say something like, "Yeah, I don't
really have access information. I can
help you in these various ways."
Great. So, that's effectively the base
case today. Uh so, if I go back to the
slides
real quick, this is a quick recap of
what we did. We told it something, asked
another session about it later, no
information is transferred between the
sessions.
So, how do we solve this problem, right?
Um
just like in humans, uh we've introduced
the sort of concept of memory. And
again, a memory store here in the Cloud
Managed Agents platform is a file
system-like store. Uh under the hood,
you can or you can create as many memory
stores as you like here, so you don't
have to necessarily restrict a memory
store to one organization. You can
create it per user, per workspace, etc.
It's up to you to kind of define what
the boundaries of the memory store are.
Uh and then under the hood, this memory
store gets attached as a file system to
the the session container, and the model
has tools to read and write to it. Uh
the actual interesting thing here is
that we've actually
mounted it as a file system because it's
such a powerful interface for the model.
Uh you can use things like bash to like
uh like explore the file system. It can
use grep to kind of search for keywords.
Uh it can also read files and do a bunch
of like really powerful things um that
make it much more useful for the agent.
Um so, I'll switch back to my computer
here and we'll walk through kind of how
to create a a memory store.
Um so, first things first is actually
creating it. So, I'm going to copy this
uh command here. Feel free again to
follow along on your computers.
Um and the kind of parameters that you
need here are mainly just like a name.
Uh so, I'm calling mine CWC memory. You
can give it a quick description. Uh and
then I'll show you also in console later
that there are two additional parameters
that you can set here, but let me just
follow through with the simple example.
Uh once I create this memory store, you
can actually see it in console
under manage agents, memory stores.
And you'll see that it's active. Uh you
can actually click into it and view uh
essentially a file system viewer of
what's currently in it. Of course,
there's nothing in it right now.
Additionally, uh we offer functionality
uh we offer the ability for you to like
add manually add memories, so you can
create like a file under a specific
path, add some content, etc.
If I go back just a brief second and
talk about uh creating a new memory
store, there's actually two sort of
additional parameters that you can uh
set on the memory store
uh when we actually mount it. So, if I
go back to the repository here,
um the next step once you create a
memory store is to actually use it with
your sessions.
So, I'm going to again copy a few of
these commands. So, the first one here
is basically just
giving us the shape that we need to pass
the sessions API requests. I'll paste it
in our terminal here so we can see it
better.
Um so again, the memory store here, you
just pass in a memory store ID.
Uh and you can also give it a prompt
around uh that will steer the agent to
read and write specific information. So,
you might want it to focus on maybe like
a specific um link or a specific like
area of focus on. Let's say you're
baking making like a investment agent,
right? Uh and you want to focus on
specific things to remember for the
future.
Uh so, you can do that with the prompt
parameter.
Uh additionally, there is an access
field uh that defaults to read or write.
Um you can change that to read only,
which will make it so that the session
and the agent will only be able to read
from that memory store, cannot update
it.
So, once I run this,
um you'll see I have created a new
session in console.
Uh and this time it'll have a memory
store attached.
And then if I send it events here, this
time we'll just basically repeat the
test that we did just before. So, let me
grab this.
Again, same text as before, we're
telling it new information.
Uh and hopefully we'll be able to
observe a different behavior this time.
Yeah, so clicking into uh if you click
into the session details, you'll see the
the information that I just gave it.
And now the model is like first looking
at memory to see, okay, was there
anything that like I need to remember
for this conversation?
Uh and now it's going to actually like
Of course, there's nothing in our memory
store. So, now what it's going to do is
actually save the content that I told it
to that memory store directly.
And it saved it under this like
sessions.md file.
And it's great telling me that uh what
it did.
Um so, then if I go back and do that
same test that we did before, this time
I'll just copy both.
Uh sorry, just
Again, where this time we're going to
create a new session with the same
memory store that we were just using.
Uh and we will send it
an event here
asking it what are the things that it
found uh or learned from the CMA talk.
Once again, going back to our console
UI, we can see the recall test running.
And as we would expect, the model is now
first looking at its memory store to see
if there's any information.
And again, it's now using grep to find
uh any sort of keywords here. It's
looking for CMA.
And great, it found like a lot of
information that we just told it from
the from our previous session.
And it now it's able to answer my
question, right? Um and this is like of
course a very simple example, but this
illustrates kind of the power of of
memory and this is like something that
was kind of difficult to do before,
right?
I'll give quick pause in case anyone's
straggling.
Um okay, great. So, what what else kind
of can you can you do with the memory
store here? Well, we actually offer uh
additional sort of endpoints that allow
you to manually inspect the store
itself. Uh so, I'll use the CLI here,
but for instance, you can list all of
the memory files that are in the memory
store.
We can like
do that.
Um there's also each um memory a memory
store's a memory files in a memory store
are also versioned. Uh so, anytime you
make a change to a file, etc., there's a
new version that's created and we offer
a set of endpoints for that.
And then I can also kind of take you
through the memory store UI.
So, each memory store you create again
is here. And if we go back to our like
kind of file system view, you can
actually see the files that it created.
Uh there will be like a directory
structure here if Claude is creating
kind of subdirectories to organize
memory files.
You can actually edit these memory files
directly if you wanted to. So, for
instance, if Claude wrote something um
that was incorrect or maybe you just
wanted to add more information, you can
do that. And again, as we saw before,
you can add additional memories to a
memory store.
Uh okay, so
I'm going to go back to the slides real
quick.
And as we just talked about, uh, this is
how you create a memory store and then
mount it on a session that you want to
use it on. Again, it's up to you to kind
of decide which of your sessions will
use memory, which ones will not.
Uh, we also saw how you can like list
memories and see what's currently in a
memory store.
And let's move on to talk a little bit
about dreaming now. Um, so
when you have agents that are reading
and writing to this memory store over
time, uh, we've noticed that often times
they can start just kind of dumping
information to that memory store. So,
it'll start writing maybe every every
task you ask it to do it'll maybe record
its information, right? And over time
your memory store is going to grow,
right? And there's no real process, uh,
before that would allow you to sort of
organize that memory, maybe check to see
if anything was stale, and and
consolidate any duplicates, right? And
so, this is where dreaming comes in.
Uh, dreaming is a is a batch process
that runs again asynchronously. You
launch it, uh, using uh, our API or
through console, and it'll run a a new
dreaming harness that we built that is a
multi-agent setup. It will look over
each of the input sessions that you've
given it. So, you specify like an input
memory store that you want it to dream
over along with like a group of
transcripts that you think might help or
enrich that memory store. It'll look
through each one, do again
fact-checking, enriching with additional
details, maybe dates, specific
identifiers, uh, and then it will also
organize those memory files and see if
there's any duplicates, anything that it
can help uh, fix so that when you and
it'll produce an output memory store
such that in the future, when you attach
that output to additional sessions, it
will hopefully increase efficiency,
uh, efficiency of like information
retrieval, and also hopefully increase
the intelligence of the agent.
So, let's take a look at how this works.
I'll again switch back to my computer
and we'll walk through it together.
Uh so, what you to to get get started
with dreaming, basically, you'll need to
actually create the dream job.
And I'll I'll go through a little bit of
the parameters here. So, the model uh
here that we're choosing is Claude Opus
47. You can choose between or Sonnet 46,
depending on kind of the level of
quality you want, as well as maybe like
token costs.
Uh it takes in two inputs. So, you'll
need the memory store that you want it
to dream over, as well as a list of
session IDs. Uh so, this is up to you to
decide. You can,
you know, maybe dream over daily and
dream over maybe like 10 sessions at a
time or 20, right? It could go, you
know, all the way up to like 100. We're
also looking to scale it further uh
beyond that.
I Optionally, you can also provide the
dream job some additional instructions
that you might add. So, we provide it
with a default prompt that does a bunch
of things. If you wanted dreaming to,
for instance, specifically fix a few
things, like maybe you're working in a
domain that requires like very specific
details, right? You might ask a dream
job to really focus on, "Hey, make sure
you backfill these details so I remember
for the future, right?" You can also get
it to You can also steer it to maybe
like organize files a bit more, like I
want the specific structure in my memory
store, please do that.
Uh so, let's actually go and run this
command here.
Great. We'll get We'll get back a dream
ID.
And then, once again, I'll go back to
our console here.
And so, dreams are under, again, manage
agents, dreams.
And once I create the dream job, it'll
start pen- it'll start with pending, but
it'll start running pretty shortly
after.
And you can actually see the status of
the job both in console and through the
API. I'll show both. But in console
here, you'll see the input memory store,
as well as a token count.
And generally, like uh dream job can
take, you know, depending on the size or
the number of transcripts that you give
it, it could take anywhere from, you
know, a couple minutes to hours at a
time.
And that's really the benefit of doing
it asynchronously, right? Like this is
not something that you want to do live
while your agents are working.
And we'll just give it a a minute here
to to run. As you guys can see,
as it's running, as agents or as the
harness itself is running, we're
updating the token count for you, so you
can track its progress over time.
The other really cool thing here is that
Dreamings actually built directly on top
of Cloud Managed Agents primitives.
So you can actually see that we are
creating a session for the dream job
itself. And you can actually click into
it to see exactly what the dream is
doing. This offers a really nice amount
of like observability as you can like
diagnose issues potentially. And so you
can see the prompt that we give it.
There's a lot of details here that I'll
kind of that you can explore on your own
time. But the under the hood, the the
Dreaming harness itself is launching sub
agents to look over all of the
transcripts that you've given it.
And each sub agent essentially has a
system prompt that tells it what to do,
look over it. And the orchestrator is
responsible for just like making sure
all the agents are running and kicking
them off as they go.
So we'll give it another minute for to
let this run.
Another thing to call out here is that
while
we don't actually touch the input memory
store at all that you create. So this is
a non-destructive process. What we
actually do is we will clone your input
memory store into what's called an
output memory store. And the dream job
will be writing basically to a new
memory store such that any edits that
are made are non-destructive and then
we'll see down the line how you can
utilize this output memory store in your
future sessions.
Generally this takes about a minute or
so depending on
how fast the job runs.
Uh one other thing is that you'll see
that I'm sort of checking on the job
periodically as it's running in console.
When you do this programmatically we
offer an API that allows you to just
essentially query
for the dream job and it'll have a
status so you can pull for the status.
Great. So looks like it just completed
and the cool thing here is that in
console we actually show you a diff of
what it did. So you can see dreaming
here
it created an index file. This index
file has sort of these slugs that
reference the various like memory files
that
a future agent might need. And the main
goal of this is really just that future
agents it's a lot more efficient to kind
of look at an index file and quickly
grok like what it needs to go look for
instead of maybe doing a a wider grep.
Additionally it's actually adding like
additional information that was not
present in the in the first couple of
sessions that I created. So it's
creating this event logistics file that
gives the whole schedule of Code with
Claud.
Um a bunch of names as well.
Uh and again schedule for day two.
Uh and you'll also see that it actually
kind of reformatted the memory file that
I created in a previous session. So this
time it is adding again a slug, a
description of the event, some
additional metadata.
And again adding more details. And
generally we find that like
more information actually really does
help future sessions. And if you think
about it intuitively, um while an
agent's working on a task currently,
it's kind of hard to predict down the
line what it might need, right? That's
just generally a harder prediction
problem. So, it's actually good to kind
of write additional details down that a
future agent might remember. And
Dreaming can always like go back and
like remove stuff that is no longer
needed.
Uh and if I go to the output memory
store here,
I'll just click on it.
Um
again, you can see all the files that I
created. It's another good way to sort
of see what's going uh what dream
Dreaming did. Uh and if you wanted like
a human in the loop kind of review
process, this is kind of where uh this
is super helpful. Uh human can kind of
go in and see if the
Dreaming harness made any mistakes.
Okay, great. Um just going to switch
back to the slides real quick cuz I want
to show a diagram.
Um
yeah. So, again, under the hood, this is
sort of what how Dreaming works, right?
This is a multi-agent harness.
Uh we have an orchestrator that is
mainly responsible for spinning up
sub-agents. And again, we spawn one
sub-agent per input session that you
give it.
Um and kind of the the reasons behind
this are we actually kind of want
Dreaming to be exhaustive by design. Uh
if you give it 100 chances, you want to
make sure like Claude is looking over
all the information to make sure it's
not missing anything, right? Um
great. So, let me let me switch back to
my computer again.
Uh and this time I'm going to actually
like walk through how we might use this
in a future session.
So,
uh once the dream uh is done, you can
actually go and grab the output memory
store using this. So, again, we're we're
just retrieving the dream resource uh
with the dream ID that we created and
then
uh querying or just grabbing the the
JSON memory store ID.
Great. So, this is the memory store.
And again, you can
look through what memories it created.
Uh and then now we'll do this sort of
test again that we did before with the
two sessions. So, I will create a new
session here.
And you'll notice that this is now using
the output memory store from dreaming.
Once again, we'll send it an event here.
We're just asking it
what sessions I attended, what resources
do I have links for, and what follow-ups
did I flag.
Once again, going back to the console,
it's really a great way to, you know,
visualize what's going on here.
And you'll see that this time when it's
reading from memory, you'll see all the
stuff that dreaming did, right? So, the
index, the event logistics.
And it's now reading kind of it's
starting to read the index first.
Okay, great. Now it knows I'm going to
go straight to the sessions file.
It's being a little exhaustive here,
just checking for, you know, event
logistics.
Okay, great. Let's see what it came up
with. So, as you can see, I
I'd have to go back and show you the the
previous session, but this time I think
there's a lot actually a lot more
information here. So, it gave me a recap
of all the sessions I I attended. Uh
it's giving me timestamps now about like
all the sessions that were that were
planned for day two, as well as like the
resource links, right? I think this kind
of showcases again like how dreaming can
really enrich information that is
transferred between sessions.
And then optionally um at the end, you
know, if you're really happy with the
output memory store here, you can go
ahead and actually retire the old memory
store.
Um so this won't affect like your
previous sessions. It just means that
you know it will it will keep you the
number of memory stores in your
organization down to a reasonable level.
Um great. So I'm going to kind of switch
back to the slides here.
Uh and talk a little bit how you can
kind of view sessions, memory stores in
dreaming as three composable layers
here, right? If you think of a session
as a as an isolated instance of an agent
running, uh it's one usually typically
one conversation thread, typically
ephemeral, right? A memory store
augments that. So now you can connect
information between your sessions across
multiple sessions, right?
And then finally with dreaming, uh
you're now organizing, enriching,
and improving your memory stores over
time, so that as you scale up the number
of sessions you have, and as you scale
up the information that is being
processed through those sessions, your
memory stays at a reasonable level. It's
manageable. It doesn't blow up. Also, it
checks for things like staleness to make
sure all the information is most is
up-to-date. Okay?
I wanted to highlight some of the maybe
good questions that I got from the
audience here. So one of them was around
uh generally like sort of what is the
like token usage of this feature like?
Um so as I said before like I think by
design we actually do want it to be
exhaustive, so we do expect it to use a
lot of tokens.
Um
the the nice thing here is that because
most of the processing is agentic, uh
most of the tokens are actually cached.
So we're expecting like about a 95%
cache rate cash hit rate on um um
like most dream sessions, right? And
additionally, we are exploring like
other ways of offering this at lower
costs to you. So, uh example of this
would be like similar to our batch API,
we could offer things at a 50% discount
by scheduling at a different times. Uh
other additional like token usage
controls include like switching the
model, steering the prompt a little bit
more, also providing more like just
general budgeting of tokens.
Great. Um so, I think we're just about
winding down. So, I'm going to quickly
kind of go over again for the folks
remaining in the room uh like what we
went over today.
Uh so, again, we talked about the
problem that most agents face today,
which is like how do you remember
information across sessions? I think
this is
a pretty like well-established kind of
problem now.
And we talked about how memory is kind
of the first step to addressing this,
right? You give agents access to
something where they can dump the
information, read from it, etc.
Uh but we also saw how this creates a
problem where memory stores are can grow
unbounded over time. They can grow
disorganized, information can grow
stale, etc. And then we saw how dreaming
can be used as a way to mitigate this
problem, right? So, we we take another
set of agents that their entire job is
to improve that memory store for future
use.
Um and with that, I'd like to thank
everyone for for coming to today's
workshop. Um hopefully, it was helpful.
And hopefully, by the end, you'll learn
how to uh or you'll you'll know how to
like integrate maybe memory into your
own use cases.

## VN dub transcript (b1qgIGwBUEI, deduped auto-captions, read in full 2026-07-04)

[âm nhạc]
&gt;&gt; Cảm ơn quý vị đã tham gia cùng chúng tôi
hôm nay. Tên tôi
&gt;&gt; [âm nhạc]
&gt;&gt; là Kevin.
Tôi là một kỹ sư tại Anthropic và hôm
nay chúng ta sẽ cùng tìm hiểu cách xây
dựng các agent có khả năng ghi nhớ.
Vì vậy, hôm nay chúng ta sẽ thảo luận sơ
lược về trường hợp cơ bản với các agent
hiện nay, đó là chúng hoạt động một cách
biệt lập.
Và điều này phần nào hạn chế tính hữu
dụng của chúng trong rất nhiều quy trình
làm việc thực tế.
Chúng ta sẽ xem xét cách giải quyết vấn
đề này bằng tính năng kho lưu trữ bộ nhớ
mới dành cho agent mà chúng tôi vừa ra
mắt.
Tính năng này sẽ cung cấp cho các agent
quyền truy cập vào một kho lưu trữ bộ
nhớ trực tiếp mà chúng có thể đọc và ghi
qua nhiều phiên làm việc khác nhau.
Sau đó chúng ta sẽ tìm hiểu cách cải
thiện các kho lưu trữ bộ nhớ này theo
thời gian bằng một tính năng mới mà
chúng tôi gọi là Dreaming.
Và cuối cùng chúng ta sẽ thấy cách tất
cả những điều này kết nối với nhau thông
qua cả CLI và giao diện console tuyệt
vời của chúng tôi.
Vì vậy, trong các hội thảo trước, tôi
nghĩ chúng ta đã học được một chút về
cách Cloud Managed Agents sở hữu các
khái niệm gọi là agent, môi trường và
phiên làm việc.
Trong buổi workshop này, chúng ta sẽ
cùng bổ sung thêm hai khái niệm mới.
Khái niệm đầu tiên chính là Memory
Store.
Vậy nên, Memory Store là một kho lưu trữ
dạng hệ thống tệp tin bền vững được gắn
như một tài nguyên vào các phiên làm
việc mà bạn tạo ra, giúp các agent có
khả năng đọc và ghi thông tin xuyên suốt
các phiên khác nhau.
Dream là một tác vụ bất đồng bộ chạy
ngầm trong nền.
Nó sẽ kiểm tra một Memory Store đầu vào
cùng với nhiều phiên làm việc trước đó
của bạn được biểu diễn dưới dạng bản
ghi. Sau đó chúng ta chạy một công cụ
kiểm soát để tinh lọc những thông tin
mới mà có thể các agent ban đầu đã bỏ
sót.
Chúng tôi thực hiện các việc như kiểm
tra tính xác thực của sự kiện. Chúng tôi
cũng tổ chức, tổng hợp và loại bỏ các
thông tin trùng lặp để đảm bảo memory
store của bạn không phát triển vô hạn
theo thời gian. Vì vậy, trong trường hợp
bất kỳ ai trong phòng này chưa tải xuống
kho lưu trữ workshop cần thiết cho buổi
học, đây là đường dẫn URL.
Tôi sẽ dành vài giây để mọi người kịp
lấy đường dẫn đó.
Được rồi, vậy nên chúng ta hãy cùng thảo
luận một chút về vấn đề hôm nay.
Vì vậy, khi bạn tạo các agent trên Cloud
Managed Agents ngày nay, cùng với các
phiên làm việc, phần lớn thời gian bạn
chỉ tạo một phiên tại một thời điểm và
những phiên này hoàn toàn biệt lập, đúng
không? Agent sẽ không ghi nhớ thông tin
từ quá khứ và cũng không chuyển giao
thông tin sang các phiên làm việc trong
tương lai.
Vì vậy, hôm nay tôi muốn dẫn dắt chúng
ta đi qua trường hợp cơ bản này. Vì vậy,
nếu tôi chuyển sang máy tính của mình
Tôi đang ở trong kho lưu trữ workshop
của chúng ta tại đây. Hy vọng mọi người
đều có thể nhìn thấy điều này ở phía
sau. Nhưng tôi vừa chạy tập lệnh khởi
tạo mà chúng ta đã bao gồm trong kho lưu
trữ này.
Và điều mà tập lệnh này đã làm cơ bản là
tạo ra một số thông tin hạt giống dành
cho chúng ta. Vì vậy, chúng ta có một
agent, chúng ta có một môi trường và
chúng ta có một vài phiên làm việc trước
đó thảo luận về những chủ đề như các bài
phát biểu chính trong ngày đầu tiên,
cũng như một workshop trước đó.
Và vì vậy, điều tôi sẽ làm từ đây thực
sự là tiến hành và bắt đầu dẫn dắt các
bạn đi qua hướng dẫn này.
Bạn hoàn toàn có thể làm theo ngay trên
máy tính của mình. Tôi sẽ sử dụng giao
diện dòng lệnh, đồng thời cũng sẽ hiển
thị giao diện bảng điều khiển cho từng
bước thực hiện.
Vì vậy, trước tiên, chúng ta sẽ tạo một
phiên làm việc để cung cấp cho hệ thống
một số thông tin mới.
Tôi sẽ sao chép lệnh này. Như bạn thấy,
chúng ta đang tạo một phiên làm việc với
các agent đã được xây dựng trước đó, kèm
theo định danh môi trường.
Chúng ta cũng đã đặt tiêu đề ở đây là
write test with no memory, tức là viết
kiểm tra mà không có bộ nhớ. Rất tốt.
Bây giờ, sau khi đã tạo xong phiên làm
việc này, tôi sẽ nhanh chóng chuyển sang
bảng điều khiển của mình và bạn sẽ thấy
tôi sẽ di chuyển cửa sổ này sang một
bên.
Bạn sẽ nhận thấy rằng phiên làm việc đã
xuất hiện trên bảng điều khiển. Trạng
thái của nó chưa phải là nhàn rỗi vì
chưa có quy trình nào đang chạy. Vậy là
chúng ta sẽ quay lại và sau đó tôi sẽ
gửi cho phiên làm việc này một số thông
tin mới.
Ngay khi tôi sao chép nội dung này.
Điều tôi đang làm ở đây là gửi một tin
nhắn đầu tiên từ người dùng chứa thông
tin về buổi thuyết trình CMA hôm qua.
Bao gồm một vài từ khóa như multi and
orchestration outcome và memory.
Tôi cũng vừa cung cấp cho nó một ví dụ
về ổ nơi tôi đã ghi chú và tải lên đó.
Vì vậy, nếu tôi quay lại console, chúng
ta sẽ thấy sự kiện này xuất hiện.
Và điều chúng ta mong đợi agent hay
model sẽ làm ở đây là nó sẽ phản hồi và
nói đại loại như tuyệt, cảm ơn vì thông
tin.
Không chắc bạn muốn tôi làm gì thêm ở
đây nữa. Vì vậy, chúng ta sẽ đợi một
chút để mọi người kịp theo kịp. Có vẻ
như model đã phản hồi ở đây.
Chỉ cần thu gọn phần này lại. Đúng vậy,
nó đang xác nhận rằng thông tin này rất
hữu ích. Cảm ơn bạn đã cung cấp cho tôi
những thông tin này. Vậy nên nếu chúng
ta tiếp tục, xin lỗi, bạn nói gì cơ? Tôi
tin rằng đây đang sử dụng Sonnet, chính
là agent đã được tạo ra ngay từ đầu.
Đúng rồi, thật tuyệt.
Tuyệt vời. Vậy nếu tôi quay lại phần
workshop này, chúng ta sẽ tạo ra một
phần thứ hai đóng vai trò như một lần
kiểm tra lại.
Vì vậy, tôi sẽ thực hiện các bước này
nhanh hơn một chút. Sau đó, một lần nữa,
tôi sẽ gửi một tin nhắn ở đây. Lần này,
tôi sẽ yêu cầu nó cung cấp thông tin về
những gì tôi vừa nói với nó.
Và nếu tôi quay lại bảng điều khiển của
chúng ta ở đây để kiểm tra phiên làm
việc khác vừa được tạo ra, chúng ta sẽ
mong đợi agent trả lời đại loại như,
"Vâng, tôi không thực sự có quyền truy
cập vào thông tin đó, nhưng tôi có thể
hỗ trợ bạn theo nhiều cách khác nhau."
Tuyệt vời. Vậy đó chính là trường hợp cơ
bản hiện nay.
Nếu quay lại các slide một chút, đây là
bản tóm tắt nhanh về những gì chúng ta
đã thực hiện.
Chúng ta đã cung cấp thông tin, sau đó
hỏi lại trong một phiên làm việc khác,
nhưng không có dữ liệu nào được chuyển
giao giữa các phiên đó.
Vậy làm thế nào để chúng ta giải quyết
vấn đề này?
Giống như con người, chúng ta đã giới
thiệu khái niệm về bộ nhớ.
Và một lần nữa, kho lưu trữ bộ nhớ trong
nền tảng Cloud Managed Agent này hoạt
động như một hệ thống tập tin.
Về mặt kỹ thuật, bạn có thể tạo ra bao
nhiêu kho lưu trữ bộ nhớ tùy thích ở
đây.
Do đó, bạn không nhất thiết phải giới
hạn một kho lưu trữ bộ nhớ cho một tổ
chức duy nhất. Bạn có thể tạo nó theo
từng người dùng, theo từng không gian
làm việc và tương tự như vậy. Việc xác
ranh giới của kho lưu trữ bộ nhớ thuộc
về quyết định của bạn.
Và ở phía bên trong, kho lưu trữ bộ nhớ
này được gắn vào như một hệ thống tập
tin cho container phiên làm việc. Đồng
thời, mô hình có các công cụ để đọc và
ghi vào đó.
Điều thực sự thú vị ở đây là chúng ta đã
gắn nó dưới dạng hệ thống tập tin, bởi
vì đây là một giao diện cực kỳ mạnh mẽ
dành cho mô hình.
Bạn có thể sử dụng các công cụ như bash
để khám phá hệ thống tập tin đó.
Nó cũng có thể sử dụng lệnh grep để tìm
kiếm các từ khóa. Nó còn có thể đọc các
tập tin và thực hiện nhiều tác vụ rất
mạnh mẽ khác, giúp nó trở nên hữu ích
hơn nhiều đối với agent.
Vì vậy, tôi sẽ quay lại máy tính của
mình ở đây và chúng ta sẽ cùng tìm hiểu
cách tạo ra một kho lưu trữ bộ nhớ.
Việc đầu tiên cần làm chính là tạo ra
kho lưu trữ đó. Vì vậy, tôi sẽ sao chép
lệnh này ở đây. Bạn hoàn toàn có thể làm
theo ngay trên máy tính của mình.
Và các tham số mà bạn cần ở đây chủ yếu
chỉ là một tên gọi. Vì vậy, tôi sẽ đặt
tên cho memory của mình là Ciberry
memory.
Bạn có thể cung cấp một mô tả ngắn gọn
cho nó. Sau đó, tôi sẽ chỉ cho bạn thấy
trên console rằng có hai tham số bổ sung
mà bạn có thể thiết lập ở đây. Nhưng
trước hết, hãy để tôi tiếp tục với một
ví dụ đơn giản.
Ngay sau khi tạo kho lưu trữ memory này,
bạn thực sự có thể nhìn thấy nó trên
console trong mục manage agents memory
stores.
Và bạn sẽ thấy rằng nó đang ở trạng thái
hoạt động. Bạn thực sự có thể nhấp vào
đó và xem, về cơ bản một trình xem hệ
thống tệp những gì đang có trong đó.
Tất nhiên hiện tại không có gì trong đó
cả.
Ngoài ra, chúng tôi cũng có các chức
năng.
Chúng tôi cung cấp khả năng để bạn,
chẳng hạn như thêm hoặc thêm thủ công
các memory. Vì vậy, bạn có thể tạo một
file trên đường dẫn cụ thể của mình,
thêm một số nội dung, vân vân. Nếu tôi
quay lại trong một khoảnh khắc ngắn để
nói về việc tạo một kho lưu trữ memory
mới, thực ra có hai loại tham số bổ sung
mà bạn có thể thiết lập trên kho lưu trữ
memory khi chúng ta thực sự mào nó.
Vì vậy, nếu quay lại kho mã nguồn ở đây,
bước tiếp theo sau khi bạn đã tạo một
memory store chính là tích hợp nó vào
các phiên làm việc của bạn.
Vậy nên tôi sẽ sao chép lại một vài lệnh
trong số này. Lệnh đầu tiên ở đây cơ bản
là cung cấp cho chúng ta cấu trúc dữ
liệu cần thiết để gửi yêu cầu tới
sessions API.
Tôi sẽ dán nó vào terminal ở đây để
chúng ta có thể quan sát rõ hơn. Một lần
nữa, đối với memory store, bạn chỉ cần
truyền vào một ID của memory store và
bạn cũng có thể cung cấp một prompt để
định hướng agent đọc và ghi các thông
tin cụ thể.
Ví dụ, bạn có thể muốn nó tập trung vào
một liên kết cụ thể hoặc một lĩnh vực
trọng tâm nào đó.
Và giả sử bạn đang xây dựng một
investment agent đúng không? Bạn sẽ muốn
tập trung vào những điều cụ thể cần ghi
nhớ cho tương lai. Vì vậy, bạn có thể
thực hiện điều đó thông qua tham số
prompt. Ngoài ra, còn có một trường
access được mặc định thiết lập là read
hoặc write.
Bạn có thể chuyển chế độ thành chỉ đọc.
Điều này sẽ đảm bảo phiên làm việc và
agent chỉ có thể truy xuất dữ liệu từ
kho lưu trữ bộ nhớ đó.
Nó sẽ không thể cập nhật hay thay đổi
bất kỳ nội dung nào. Vì vậy, ngay sau
khi tôi chạy lệnh này, bạn sẽ thấy một
phiên làm việc mới đã được tạo trong
bảng điều khiển.
Và lần này, phiên làm việc đó sẽ được
gắn kèm với một memory store.
Sau đó, nếu tôi gửi một sự kiện ở đây,
chúng ta sẽ thực hiện lại bài kiểm tra
tương tự như vừa rồi. Để tôi sao chép
nội dung này nhé.
Một lần nữa, với cùng đoạn văn bản như
trước, chúng ta đang cung cấp cho nó
những thông tin mới. Hy vọng rằng lần
này chúng ta sẽ quan sát được một hành
biệt.
Đúng vậy, nếu bạn nhấp vào chi tiết
phiên làm việc, bạn sẽ thấy thông tin mà
tôi vừa cung cấp cho nó.
Và bây giờ, mô hình sẽ ưu tiên kiểm tra
bộ nhớ trước để xác định xem có điều gì
cần ghi nhớ cho cuộc hội thoại này hay
không.
Và giờ, tất nhiên, vì trong kho lưu trữ
bộ nhớ của chúng ta chưa có gì, nên điều
nó sẽ làm là lưu trực tiếp nội dung mà
tôi vừa yêu cầu vào kho lưu trữ bộ nhớ
đó.
Và nó đã lưu nội dung này vào tệp
session.mb.
Điều tuyệt vời là nó đã thông báo rõ
ràng cho tôi biết những gì nó đã thực
hiện.
Vì vậy, nếu tôi quay lại và thực hiện
lại bài kiểm tra giống như trước đây,
lần này tôi sẽ sao chép cả hai phần.
Một lần nữa, lần này chúng ta sẽ tạo một
phiên làm việc mới sử dụng cùng một kho
lưu trữ bộ nhớ mà chúng ta vừa dùng. Và
chúng ta sẽ gửi một sự kiện tại đây, yêu
cầu nó liệt kê những điều nó đã tìm thấy
hoặc học được từ buổi nói chuyện CMA.
Một lần nữa, khi quay lại giao diện
người dùng của bảng điều khiển, chúng ta
có thể thấy quá trình kiểm tra truy hồi
đang chạy. Và như chúng ta vẫn mong đợi,
mô hình hiện đang kiểm tra kho lưu trữ
bộ nhớ của nó trước để xem có thông
thông nào không.
Và một lần nữa, nó hiện đang sử dụng
công cụ grep để tìm bất kỳ từ khóa nào ở
đây.
Nó đang tìm kiếm từ khóa CMA. Tuyệt vời,
nó đã tìm thấy rất nhiều thông tin mà
chúng ta vừa cung cấp từ một phiên làm
việc trước đó. Và giờ nó có thể trả lời
câu hỏi của tôi.
Đương nhiên đây chỉ là một ví dụ rất đơn
giản, nhưng nó minh họa rõ ràng sức mạnh
của bộ nhớ. Và điều này trước đây thực
sự khá khó để thực hiện.
Tôi sẽ tạm dừng một chút để mọi người
theo kịp. Anthropic Sonnet of GPT.
Được rồi, tuyệt. Vậy chúng ta còn có thể
làm gì khác với kho lưu trữ bộ nhớ này?
Thực tế, chúng tôi cung cấp thêm các
endpoint cho phép bạn tự kiểm tra kho
lưu trữ đó.
Vì vậy, tôi sẽ sử dụng CLI ở đây, nhưng
ví dụ bạn đã có thể liệt kê tất cả các
tệp bộ nhớ nằm trong kho lưu trữ bộ nhớ.
Chúng ta có thể làm điều đó.
Ngoài ra, mỗi bộ nhớ, các kho lưu trữ bộ
nhớ và các tệp bộ nhớ trong kho lưu trữ
bộ nhớ đều được quản lý phiên bản.
Vì vậy, bất cứ khi nào bạn thực hiện
thay đổi đối với một tệp tin hay các
thao tác tương tự, một phiên bản mới sẽ
được tạo ra. Và chúng tôi cung cấp một
bộ các endpoint cho việc này.
Sau đó, tôi cũng có thể hướng dẫn bạn đi
qua giao diện người dùng của memory
store.
Vì vậy, mỗi memory store mà bạn tạo ra,
một lần nữa sẽ hiển thị ở đây. Và nếu
chúng ta quay lại chế độ xem hệ thống
tệp tin, bạn thực sự có thể nhìn thấy
các tệp tin mà nó đã tạo ra. Sẽ có một
cấu trúc thư mục ở đây nếu Claude tạo ra
các thư mục con nhằm mục đích tổ chức
các tệp tin bộ nhớ.
Bạn thực sự có thể chỉnh sửa trực tiếp
các tệp tin bộ nhớ này nếu bạn muốn. Ví
dụ, nếu Claude viết ra điều gì đó không
chính xác, hoặc có thể bạn chỉ muốn bổ
sung thêm thông tin, bạn hoàn toàn có
thể thực hiện điều đó.
Và một lần nữa, như chúng ta đã thấy
trước đó, bạn có thể thêm các bộ nhớ bổ
sung vào một memory store.
Máy chủ.
Được rồi, vậy tôi sẽ quay lại với các
slide một chút.
Và như chúng ta vừa thảo luận, đây là
cách bạn tạo ra một memory store và sau
đó gắn nó vào một phiên làm việc mà bạn
muốn sử dụng nó. Một lần nữa, việc quyết
định phiên làm việc nào sẽ sử dụng bộ
nhớ và phiên nào thì không hoàn toàn tùy
thuộc vào bạn và Cloud.
Chúng ta cũng đã tìm hiểu cách bạn có
thể liệt kê các ghi nhớ và xem những gì
đang được lưu trữ trong kho bộ nhớ hiện
tại.
Bây giờ, hãy chuyển sang thảo luận một
chút về Dreaming.
Vì vậy, khi các agent đọc và ghi vào kho
bộ nhớ này theo thời gian, chúng tôi
nhận thấy rằng chúng thường bắt đầu chỉ
đơn giản là đổ dồn thông tin vào kho bộ
nhớ đó.
Cụ thể, nó sẽ bắt đầu ghi lại, có thể là
với mọi nhiệm vụ bạn yêu cầu thực hiện,
nó sẽ ghi lại thông tin của mình. Và
theo thời gian, kho bộ nhớ của bạn sẽ
ngày càng mở rộng. Tuy nhiên, hiện chưa
có quy trình thực sự nào cho phép bạn
sắp xếp lại kho bộ nhớ đó, có thể kiểm
tra xem có dữ liệu nào đã lỗi thời hay
không và hợp nhất các bản sao trùng lặp.
Và chính tại đây, chức năng Dreaming sẽ
phát huy tác dụng. Dreaming là một quy
trình xử lý theo lô được thực thi, một
lần nữa, theo chế độ bất đồng bộ. Bạn có
thể khởi chạy nó bằng cách sử dụng API
của chúng tôi hoặc thông qua bảng điều
khiển. Và hệ thống sẽ chạy một cơ chế mơ
mới do chúng tôi xây dựng. Đây là một
thiết lập đa agent.
Nó sẽ rà soát từng phiên làm việc đầu
vào mà bạn đã cung cấp.
Vì vậy, bạn cần chỉ định một kho lưu trữ
bộ nhớ đầu vào để hệ thống thực hiện quá
trình mơ, cùng với một nhóm bản ghi mà
bạn cho rằng có thể hỗ trợ hoặc làm
phong phú thêm kho lưu trữ bộ nhớ đó.
Hệ thống sẽ duyệt qua từng bản ghi, thực
hiện kiểm tra sự thật, bổ sung các chi
tiết như ngày, tháng, mã định danh cụ
thể, sau đó tổ chức các tệp bộ nhớ này,
tìm kiếm các bản sao trùng lặp hoặc bất
kỳ vấn đề nào có thể khắc phục, nhằm đảm
bảo khi bạn tạo ra một kho lưu trữ bộ
nhớ đầu ra thì trong tương lai, khi bạn
gắn kho lưu trữ đó với các phiên làm
việc bổ sung
nó sẽ giúp tăng hiệu quả, cụ thể là hiệu
quả trong việc truy xuất thông tin, đồng
thời cũng nâng cao trí tuệ của agent.
Vì vậy, hãy cùng xem xét cách thức hoạt
động của quy trình này. Một lần nữa,
chúng ta sẽ quay lại màn hình máy tính
của tôi và cùng nhau đi qua từng bước.
Ở đây,
Vì vậy, để bắt đầu quá trình mơ, về cơ
bản, bạn cần tạo một công việc mơ.
Và tôi sẽ giải thích sơ qua một vài tham
số ở đây. Vậy nên mô hình mà chúng ta
đang lựa chọn ở đây là Cloud Opus 4.7.
Bạn có thể chọn giữa Opus 4.7 hoặc Sonic
4.6, tùy thuộc vào mức độ chất lượng bạn
mong muốn cũng như chi phí token.
Nó sẽ nhận vào hai đầu vào. Vì vậy, bạn
sẽ cần một kho lưu trữ bộ nhớ mà bạn
muốn nó tổng hợp lại, cùng với một danh
sách các ID phiên làm việc.
Việc quyết định này hoàn toàn thuộc về
bạn. Bạn có thể tổng hợp lại theo ngày
và xử lý khoảng 10 phiên làm việc cùng
lúc, hoặc có thể là 20 phiên, đúng
không? Nó thậm chí có thể lên tới khoảng
100 phiên. Chúng tôi cũng đang hướng tới
việc mở rộng quy mô vượt xa con số đó.
Tùy chọn, bạn cũng có thể cung cấp thêm
các hướng dẫn bổ sung cho công việc tổng
hợp mà bạn muốn thêm vào.
Và bạn có thể thêm nó bằng một prompt
mặc định thực hiện nhiều tác vụ khác
nhau. Nếu bạn muốn cơ chế dreaming,
chẳng hạn, sửa chữa cụ thể một vài vấn
đề. Ví dụ như bạn đang làm việc trong
một lĩnh vực đòi hỏi những chi tiết rất
đặc thù, đúng không? Bạn có thể yêu cầu
một dream job thực sự tập trung vào
việc, này, hãy đảm bảo điền đầy đủ những
chi tiết này để tôi có thể ghi nhớ cho
tương lai, đúng không? Bạn cũng có thể
điều hướng nó để có lẽ tổ chức các tệp
tin tốt hơn một chút. Ví dụ như tôi muốn
một cấu trúc cụ thể trong kho lưu trữ bộ
nhớ của mình, vui lòng thực hiện điều
đó. Vì vậy, hãy cùng thực thi lệnh này
ngay tại đây.
Tuyệt vời, chúng ta sẽ nhận được một
dream ID. Và sau đó, một lần nữa, tôi sẽ
quay lại bảng điều khiển của chúng ta ở
đây.
Và do đó, các dreams nằm ở mục quản lý
agents dreams một lần nữa. Và một khi
tôi tạo xong dream job, nó sẽ bắt đầu ở
trạng thái pending, nhưng sẽ bắt đầu
chạy rất nhanh sau đó.
Và bạn thực sự có thể xem trạng thái của
job này cả trên console và thông qua
API.
Tôi sẽ hiển thị cả hai, nhưng trên
console ở đây, bạn sẽ thấy kho lưu trữ
bộ nhớ đầu vào cũng như số lượng token.
Nhìn chung, dream job có thể mất từ vài
phút đến vài giờ để xử lý, tùy thuộc vào
kích thước hoặc số lượng bản ghi bạn
cung cấp cho nó.
Và đó chính là lợi ích lớn của việc thực
hiện xử lý bất đồng bộ, đúng không?
Đây không phải là điều bạn muốn thực
hiện trực tiếp. Trong khi các agent của
mình đang hoạt động, chúng ta sẽ để nó
chạy trong khoảng 1 phút ở đây. Như bạn
có thể thấy, trong quá trình nó chạy,
hay khi chính hệ thống điều phối đang
hoạt động, chúng tôi sẽ cập nhật số
lượng token cho bạn để bạn có thể theo
dõi tiến độ theo thời gian. Một điểm thú
vị khác ở đây là dreaming thực chất được
xây dựng trực tiếp trên các nguyên tắc
cơ bản của cloud managed agents.
Vì vậy, bạn có thể thấy rõ ràng chúng
tôi đang tạo một phiên làm việc riêng
cho chính công việc dream này. Và bạn
thực sự có thể nhấp vào đó để xem chính
xác những gì dream đang thực hiện. Điều
này mang lại khả năng quan sát rất tốt,
giúp bạn có thể chẩn đoán các vấn đề nếu
có. Và bạn có thể xem được prompt mà
chúng tôi cung cấp cho nó. Có rất nhiều
chi tiết ở đây mà bạn có thể tự mình
khám phá trong thời gian rảnh.
Tuy nhiên, xét về mặt kỹ thuật, chính
dreaming harness sẽ khởi chạy các sub
agents để rà soát toàn bộ transcript mà
bạn đã cung cấp.
Và mỗi sub agent về cơ bản đều có một
system prompt hướng dẫn nhiệm vụ, cách
rà soát, trong khi orchestrator chịu
trách nhiệm đảm bảo tất cả các agents
đều đang chạy và khởi động chúng khi
cần. Vì vậy, chúng ta sẽ đợi thêm 1 phút
để quá trình này chạy tiếp.
Một điểm quan trọng khác cần lưu ý là
chúng ta hoàn toàn không can thiệp vào
input memory store mà bạn đã tạo.
Do đó, đây là một quy trình không phá
hủy dữ liệu. Thay vào đó, chúng ta sẽ
nhân bản input memory store của bạn
thành một output memory store. Và dream
job sẽ ghi dữ liệu vào một kho lưu trữ
mới, đảm bảo mọi chỉnh sửa đều không làm
mất dữ liệu gốc. Sau đó chúng ta sẽ tìm
hiểu cách tận dụng output memory store
này trong các phiên làm việc tương lai.
Nhìn chung, quá trình này thường mất
khoảng 1 phút, tùy thuộc vào tốc độ chạy
của job.
Một điều nữa là bạn sẽ thấy tôi đang
kiểm tra job định kỳ khi nó đang chạy
trên console.
Khi bạn thực hiện việc này bằng lập
trình, chúng tôi cung cấp một API cho
phép bạn truy vấn trạng thái của dream
job. Từ đó bạn có thể lấy thông tin
trạng thái của nó.
Tuyệt vời, có vẻ như nó vừa hoàn thành.
Điều thú vị ở đây là trong console,
chúng tôi thực sự hiển thị cho bạn sự
khác biệt về những gì nó đã thực hiện,
những gì nó đã làm. Vì vậy bạn có thể
thấy ở đây dreaming đã tạo ra một file
index.
File index này chứa các slug tham chiếu
đến các file bộ nhớ khác nhau mà một
agent trong tương lai có thể cần.
Và mục tiêu chính của việc này thực sự
là để các agent trong tương lai có thể
xem file index một cách hiệu quả hơn,
nhanh chóng nắm bắt những gì cần tìm
kiếm thay vì phải thực hiện một lệnh
grep rộng hơn.
Ngoài ra, nó thực sự đang bổ sung thêm
thông tin mà chưa từng xuất hiện trong
vài phiên làm việc đầu tiên mà tôi đã
tạo. Vì vậy nó đang tạo ra file logistic
sự kiện này.
Nó cung cấp toàn bộ lịch trình code với
code cùng với một loạt tên gọi khác.
Và một lần nữa lịch trình cho ngày thứ
hai.
Bạn cũng sẽ thấy rằng nó thực sự đã định
dạng lại file bộ nhớ mà tôi đã tạo trong
phiên làm việc trước đó. Vì vậy lần này
nó đang bổ sung một slug, một mô tả về
sự kiện, một số siêu dữ liệu bổ sung và
một lần nữa thêm nhiều chi tiết hơn.
Nhìn chung, chúng tôi nhận thấy rằng
nhiều thông tin hơn thực sự sẽ hỗ trợ
rất nhiều cho các phiên làm việc trong
tương lai. Và nếu bạn suy nghĩ một cách
trực quan, khi một agent đang thực hiện
một tác vụ, sẽ rất khó để dự đoán chính
xác những gì nó có thể cần sau này.
Nó đơn giản là một bài toán dự đoán khó
hơn. Vì vậy, việc ghi lại thêm các chi
tiết mà một agent trong tương lai có thể
ghi nhớ thực sự là điều hữu ích. Và
Dreaming luôn có thể quay lại để loại bỏ
những thứ không còn cần thiết nữa.
Và nếu tôi vào output memory store ở
đây, tôi sẽ chỉ cần nhấp vào nó.
Một lần nữa, bạn có thể thấy tất cả các
tệp mà tôi đã tạo. Đây cũng là một cách
tốt để xem Dreaming đã thực hiện những
gì.
Và nếu bạn muốn một quy trình xem xét có
sự tham gia của con người, thì đây chính
là nơi nó thực sự hữu ích.
Con người có thể đi vào và kiểm tra xem
Dreaming có mắc sai lầm nào hay không.
Được rồi, rất tốt. Tôi sẽ chuyển nhanh
lại sang các slide, vì tôi muốn trình
bày một sơ đồ.
Vâng.
Vậy là, xét về mặt kỹ thuật, đây chính
là cách Dreaming hoạt động đúng không?
Đây là một hệ thống kết nối nhiều agent.
Chúng ta có một orchestrator chịu trách
nhiệm chính trong việc khởi chạy các sub
agent. Và một lần nữa, chúng ta sẽ tạo
ra một sub agent cho mỗi phiên làm việc
đầu vào mà bạn cung cấp.
Lý do đằng sau điều này là chúng ta thực
sự muốn Dreaming được thiết kế để hoạt
động một cách toàn diện.
Nếu bạn cung cấp cho nó 100 cơ hội,
chúng ta muốn đảm bảo rằng Claude đã xem
xét tất cả thông tin và chắc chắn rằng
nó không bỏ sót bất cứ điều gì đúng
không?
Tuyệt vời. Vậy bây giờ, hãy để tôi quay
lại máy tính của mình.
Và lần này, tôi sẽ hướng dẫn chi tiết
cách chúng ta có thể sử dụng điều này
trong một phiên làm việc tương lai.
Vậy là khi Dream hoàn thành, bạn có thể
truy xuất output memory store bằng cách
này.
Một lần nữa, chúng ta chỉ đang truy xuất
tài nguyên Dream với Dream ID mà chúng
ta đã tạo, sau đó truy vấn hoặc lấy ID
của JSON memory store.
Tuyệt vời. Đây chính là memory store.
Và bạn có thể xem xét những ghi nhớ mà
nó đã tạo ra.
Bây giờ, chúng ta sẽ thực hiện lại bài
kiểm tra tương tự như trước đây với hai
phiên làm việc.
Vì vậy, tôi sẽ tạo một phiên làm việc
mới tại đây.
Bạn sẽ nhận thấy rằng hệ thống hiện đang
sử dụng output memory store từ Dreaming.
Một lần nữa, chúng ta sẽ gửi một sự kiện
đến đây.
Và chúng ta chỉ đang yêu cầu nó liệt kê
các phiên tôi đã tham dự, những tài
nguyên tôi có liên kết và các công việc
cần theo dõi mà tôi đã đánh dấu.
Một lần nữa, quay lại console thực sự là
một cách tuyệt vời để hình dung những gì
đang diễn ra ở đây.
Và bạn sẽ thấy rằng lần này, khi hệ
thống đọc từ bộ nhớ, bạn sẽ thấy toàn bộ
những gì Dreaming đã thực hiện, đúng
không? Vì vậy, nó đang truy cập chỉ mục
và các thông tin về hậu cần sự kiện.
Và bây giờ nó đang bắt đầu đọc. Theo một
cách nào đó, nó ưu tiên đọc chỉ mục
trước.
Được rồi, tuyệt vời. Bây giờ nó đã biết
tôi sẽ đi thẳng đến tệp các phiên làm
việc.
Nó đang kiểm tra khá kỹ lưỡng ở đây, chỉ
để xác minh các thông tin hậu cần sự
kiện.
Được rồi, thật tuyệt. Hãy xem nó đã tìm
ra điều gì. Nếu bạn có thể thấy, tôi sẽ
phải quay lại để chỉ cho bạn phiên làm
việc trước đó.
Nhưng lần này tôi nghĩ có rất nhiều
thông tin hơn ở đây. Vì vậy, nó đã cung
cấp cho tôi một bản tóm tắt về tất cả
các phiên làm việc mà tôi đã tham dự. Nó
đang cung cấp cho tôi các dấu thời gian
cho tất cả các phiên làm việc được lên
kế hoạch cho ngày thứ hai, cũng như các
liên kết tài nguyên. Tôi cho rằng
điều này một lần nữa chứng minh cách
dreaming thực sự có thể làm giàu thông
tin được chuyển giao giữa các phiên làm
việc.
Và sau đó tùy chọn ở cuối, nếu bạn thực
sự hài lòng với output memory store này,
bạn có thể tiến hành loại bỏ memory
store cũ.
Vì vậy, điều này sẽ không ảnh hưởng đến
các phiên làm việc trước đây của bạn. Nó
chỉ có nghĩa là sẽ giúp duy trì số lượng
memory stores trong tổ chức của bạn ở
mức hợp lý.
Tuyệt vời. Vậy là tôi sẽ quay lại với
các slide ở đây.
Và thảo luận một chút về cách bạn có thể
xem sessions, memory stores và dreaming
như ba lớp [hắng giọng] có thể kết hợp
với nhau, đúng không? Nếu bạn coi một
session là một phiên bản cô lập của một
agent đang chạy, thì nó thường là một
luồng hội thoại duy nhất, thường mang
tính tạm thời, đúng không?
Một memory store sẽ bổ sung cho điều đó.
Vì vậy, giờ đây bạn có thể kết nối thông
tin giữa các phiên của mình trên nhiều
session khác nhau, đúng không?
Và cuối cùng với dreaming, bạn đang tổ
chức làm giàu và cải thiện các memory
stores của mình theo thời gian, để khi
bạn mở rộng quy mô số lượng session,
cũng như tăng lượng thông tin được xử lý
qua các session đó, memory của bạn vẫn ở
mức hợp lý, dễ quản lý.
Nó không bị phình to. Ngoài ra, nó còn
kiểm tra các yếu tố như sự lỗi thời để
đảm bảo mọi thông tin đều được cập nhật.
Tôi muốn làm nổi bật một số câu hỏi hay
mà tôi nhận được từ khán giả ở đây.
Một trong những câu hỏi là về mức độ sử
dụng token của tính năng này nói chung.
Như tôi đã đề cập trước đó, theo thiết
kế, chúng tôi thực sự muốn tính năng này
hoạt động toàn diện. Vì vậy, chúng tôi
kỳ vọng nó sẽ tiêu tốn nhiều token.
Điều tuyệt vời ở đây là vì phần lớn quá
trình xử lý do agent thực hiện, nên phần
lớn token thực tế đã được lưu vào cache.
Do đó, chúng tôi kỳ vọng tỷ lệ hit cache
đạt khoảng 95% trong hầu hầu các phiên
Dream, đúng không?
Ngoài ra, chúng tôi đang tìm kiếm các
cách khác để cung cấp tính năng này với
chi phí thấp hơn cho quý vị.
Một ví dụ về điều này là tương tự như
Batch API của chúng tôi. Chúng tôi có
thể cung cấp các dịch vụ với mức giảm
giá 50% bằng cách lên lịch thực hiện vào
các thời điểm khác nhau. Các biện pháp
kiểm soát việc sử dụng token bổ sung bao
gồm việc chuyển đổi model, điều chỉnh
prompt một chút và cũng cung cấp khả
năng quản lý ngân sách token tổng thể
hơn.
Tuyệt vời.
Vì vậy, tôi nghĩ chúng ta sắp kết thúc
buổi làm việc này.
Tôi sẽ nhanh chóng tóm tắt lại một lần
nữa cho những bạn còn lại trong phòng về
những gì chúng ta đã thảo luận hôm nay.
Như vậy, chúng ta đã thảo luận về vấn đề
mà hầu hết các agent gặp phải hiện nay,
đó là làm thế nào để ghi nhớ thông tin
xuyên suốt các phiên làm việc. Tôi cho
rằng đây đã trở thành một vấn đề khá
được công nhận và hiểu rõ trong ngành.
Và chúng ta cũng đã nói về việc bộ nhớ
chính là bước đầu tiên để giải quyết vấn
đề này, phải không? Bạn cung cấp cho các
agent quyền truy cập vào một nơi nào đó
để họ có thể lưu trữ thông tin, đọc dữ
liệu từ đó và nhiều thao tác khác. Tuy
nhiên, chúng ta cũng thấy rằng điều này
tạo ra một vấn đề khi các kho lưu trữ bộ
nhớ có thể phát triển không giới hạn
theo thời gian. Chúng có thể trở nên lộn
xộn, thông tin có thể bị lỗi thời và
nhiều hệ quả khác.
Sau đó, chúng ta đã thấy cách thức
dreaming có thể được sử dụng như một
giải pháp để giảm thiểu vấn đề này, đúng
không? Và do đó, chúng ta sử dụng một
nhóm agent khác với nhiệm vụ duy nhất là
cải thiện kho lưu trữ bộ nhớ đó cho các
mục đích sử dụng trong tương lai.
Với điều đó, tôi xin gửi lời cảm ơn đến
tất cả mọi người đã tham gia buổi
workshop ngày hôm nay.
Hy vọng buổi học đã hữu ích và hy vọng
rằng khi kết thúc, bạn sẽ biết cách tích
hợp bộ nhớ vào các trường hợp sử dụng
của riêng mình.
