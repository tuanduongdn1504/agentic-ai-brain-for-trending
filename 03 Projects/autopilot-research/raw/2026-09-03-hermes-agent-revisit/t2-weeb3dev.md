# How to install Hermes Agent and Hermes Desktop with Nous Portal on Ubuntu (weeb3dev)


> Source: t2-weeb3dev.en-orig.vtt
> Converted: vtt-to-md.py
> Format: `[MM:SS] line` — verbatim auto-sub, deduplicated, word-timing tags stripped


**[00:04]** Today, I'm doing a full install of Hermes Agent and its brand new desktop app on Ubuntu 26.04. Then giving the Hermes Agent access to News Portal. Hermes is an open-source AI agent from News Research that grows with you. It runs on your machine. It remembers everything you teach it. It auto generates its own skills from your conversations. And it will run scheduled jobs

**[00:32]** unattended 24/7. The agent works seamlessly across the terminal, the desktop app, and every messaging platform you connect. There's no IDE lock-in nor single model or provider limits. Last week, the desktop app just dropped Step one, open a terminal. The only

**[01:05]** thing you need to pre-install already is Git. The official installer script pulls down everything else itself. Python, Node, UV, all of it. You just have to run this It clones the repo, installs the dependencies, builds the agent, and drops the Hermes command into your path. When it finishes, reload your shell, and &gt;&gt; Now we run the quick setup.

**[02:05]** The setup process guides you to connect a provider. I'm going with the News Portal. It's the official provider that gives you one-click access to 300 plus models, plus the full tool gateway, which includes web search, image generation, TTS, cloud browser, etc. All under a single subscription. So I'm signing in with email. You'll get a

**[02:40]** code in your inbox. Drop it in, pick the plus plan, authorize Hermes, done. And the timing's good. News just joined Nvidia's NeMo Tron coalition, and they partnered together to make NeMo Tron 3 Ultra free on the portal for 2 weeks, June 4th through the 18th. It's a 550 billion parameter model built for long-running agents. So it's a

**[03:06]** strong default to start on and experiment with. Now it asks for a main model. I'm picking Nvidia NeMo Tron 3 Ultra free. One thing to call out, that free tag is what keeps it on the no cost tier. So pick that exact variant, not the paid one. And it works the same in the terminal and the desktop app. So we're set on

**[03:32]** both. Next it offers to wire up messaging, Telegram, Discord, WhatsApp, the rest. But I'm skipping that for now since today's about the desktop app. But, you can add these anytime later.

**[04:01]** Type Hermes to launch the agent right in the terminal. And I'll ask it something simple. Now, in a new terminal tab

**[04:32]** pull in the desktop app by typing in the command Hermes desktop. That downloads and installs the full app Quick note, on Mac or Windows the desktop app is just a download from the Hermes agent page on the News Research website. The desktop app picks up the exact

**[05:12]** session I started in the terminal. A seamless handoff. Let's explore the side panel. First up skills. You'll see roughly 60 curated skills already bundled and ready to go. Everything from creative tools to research, coding, and more. The agent can even auto-generate new skills from your conversations over time. And cron jobs. These are scheduled automations you set

**[05:39]** in natural language. Think daily briefings, backups, reports, or monitoring tasks that run unattended. Just like routines in Claude or automations Let's jump into the settings by clicking the gear icon. In the models panel, you can assign auxiliary models to specific jobs like vision, web extract, MCP, and

**[06:06]** so on. So, your main model isn't doing everything. I'm switching the appearance to dark mode and midnight theme. Down in providers, you can see news portal already connected from the setup we did earlier. And there's a dedicated MCP section for wiring in custom MCP servers if you want to go deeper and create more advanced workflows. Last thing, let's ask the agent itself.

**[06:43]** What can you do in the desktop app that It's going to kick off by researching using browser tools to look up docs plus other sites and start thinking. We're just going to let it run for a bit. &gt;&gt; And that's it. You now have a fully

**[07:50]** featured self-improving AI agent with a beautiful desktop interface running locally on Ubuntu. Links are in the description. Install docs, the desktop app download, and News portal. If you found any of this helpful, drop a like and let me know in the comments what you want to see next. Maybe advanced skills, cron job examples, Thanks for watching. I'm excited to see
