# (C) Feynman Philosophy Applied to Learning

> Entity page — Learning concept
> Sources: README opening quote + philosophy section
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Feynman Philosophy** = "What I cannot create, I do not understand" — Richard Feynman's famous maxim. build-your-own-x operationalizes this: **to truly understand X, build X from scratch.** Foundational framing for the entire repo.

## 2. Why it matters / Sao quan trọng

### Passive learning vs active creation

**Passive learning:**
- Read docs / watch videos / use library
- Feel "understanding" without testing it
- Knowledge evaporates when library updates

**Active creation (Feynman approach):**
- Build minimal version from scratch
- Forces confrontation với every assumption
- Understanding persists because it's wired into muscle memory + code

### Why building teaches more

1. **Every abstraction exposes** — can't skip details when writing from scratch
2. **Edge cases forced** — can't ignore "what about empty input?"
3. **Trade-offs revealed** — why did the real implementation choose X? You'll hit the same choices
4. **Failure modes experienced** — code that "sometimes works" teaches fragility
5. **Mental model becomes operational** — not just "DB indexes are fast"; you know why B-trees vs hash maps

### Why Feynman specifically?

Feynman was famous for:
- **First-principles thinking** — derive understanding from fundamentals
- **Accessible explanation** — test understanding by explaining simply
- **Physical intuition** — can't fake knowing why something works

**build-your-own-x applies this to software.** Can't fake implementing a compiler.

## 3. Feynman in the build-your-own-x ethos

### Opening tagline
> "What I cannot create, I do not understand" — Richard Feynman

Appears prominently. Not just decoration — guides inclusion criteria.

### Inclusion criterion (implicit)
Tutorials that teach **building**, not using:
- "How to use PostgreSQL" → ❌ rejected
- "Build your own database from scratch" → ✅ included
- "Tutorial on React library" → ❌ rejected
- "Build your own React" → ✅ included

### Audience contract
User who reads tutorials + builds = user who learned.
User who reads only = user who feels learned but didn't.

**Feynman test:** Can you explain X simply, from scratch, without references? If yes, you understand.

## 4. Philosophy vs marketing

### Not all "build your own X" framed Feynman-style
- Tutorials can be marketing bait ("subscribe to my newsletter + get free build-your-own-X eBook")
- build-your-own-x curates toward actual learning content vs surface framing

### Quality signals that align with Feynman
- **Exposes internals** — doesn't hide behind libraries
- **Linear progression** — simplest version first, then features
- **Teaches reasoning** — explains why, not just how
- **Shows failures** — common mistakes discussed
- **Honest scope** — acknowledges simplified version isn't production-ready

## 5. Pedagogical patterns observed in curated tutorials

### Pattern 1: Nano version
Build minimum viable X in <200 lines.
Examples:
- "Redis in 100 lines of Python"
- "Ray tracer in 500 lines of C++"

### Pattern 2: Progressive elaboration
Start simple, add features iteratively.
Examples:
- "Build your own database" — chapters adding: storage, indexes, query parser, transactions
- "Build a compiler" — lexer → parser → semantic → code gen

### Pattern 3: Classic simplification
Take complex real system, strip to teaching version.
Examples:
- "Build your own Git" — just commits + branches, no rebase
- "Build your own Docker" — just namespaces + cgroups, no orchestration

### Pattern 4: Anti-abstraction
No frameworks / libraries allowed for core.
Examples:
- "Build your own neural network" — numpy only, no TensorFlow
- "Build your own shell" — raw syscalls only

## 6. Limits of Feynman approach

### Can't build everything
- 50-year-old OS codebases can't be replicated in tutorial form
- Production databases have decades of edge-case fixes unreachable by solo learner
- AI models (LLM) require GPU clusters + billions of tokens

### Simplified != accurate
- "Build your own X" version = teaching tool, not actual X
- Real X handles concurrency, distributed systems, security audits, 24/7 uptime
- **Learners risk thinking simplified X = real X**

### Time constraint
- Feynman approach is SLOW
- 40-hour work week + "build your own OS" = months of learning
- Professional pressure often incompatible with deep-build learning

### Prerequisites compound
- "Build your own neural network" assumes math + Python + linear algebra basics
- "Build your own OS" assumes C + assembly + x86 knowledge
- Learners without prereqs hit walls

## 7. Feynman vs LLM-era learning

### Traditional Feynman
1. Read tutorial
2. Type code yourself
3. Experience errors
4. Understanding builds

### LLM-era risk
1. Ask Claude to "build me an X"
2. LLM generates working code
3. Learner copies without understanding
4. Feels productive; actually didn't learn

### build-your-own-x's counter-positioning
- Feynman quote = implicit rejection of copy-paste-from-AI approach
- Tutorial-driven approach forces typing + thinking
- **Still valid in LLM era** if learner commits to Feynman discipline

### Hybrid LLM + Feynman (new approach)
- Use LLM as explanation + error-debug tutor
- Still type code yourself
- Ask "why" questions, not "do it for me"
- **Works, but requires discipline.**

## 8. Trade-offs / Limitations

### Strengths of Feynman framing
- **Anti-superficial** — rejects surface learning
- **Enduring understanding** — knowledge sticks
- **Character-building** — develops grit
- **Respect-building** — appreciation for real systems' complexity

### Weaknesses of Feynman framing
- **Slow** — not scalable for fast-changing tech
- **Intimidating** — barrier to entry
- **Doesn't match daily work** — most devs use abstractions, rightly
- **Selection bias** — filters for already-patient learners

## 9. Comparison to sibling wiki learning approaches

### Storm Bear's 7 agent wikis

| Wiki | Learning approach |
|------|-------------------|
| ECC | Reference docs (use tool) |
| Superpowers | Pattern-based (apply patterns) |
| gstack | Role-based (adopt roles) |
| GSD | Command-based (use commands) |
| goclaw | Platform-based (deploy service) |
| course (MS) | Curriculum (linear lessons) |
| notebooklm-py | Integration-based (invoke operations) |
| **build-your-own-x** | **Feynman "build to understand"** |

→ **build-your-own-x uniquely targets "understanding"** vs siblings targeting "productivity."

Storm Bear's 7 agent wikis assume learner wants to BE productive fast. build-your-own-x assumes learner wants to UNDERSTAND deeply, slow.

**Both valid.** Different stages of learning journey.

## 10. Common pitfalls with Feynman approach

1. **"Not invented here" syndrome** — after build-your-own-X, learner refuses to use real X ("I'll build mine better")
2. **Yak-shaving** — spend 6 months on "build your own Git" never shipping real product
3. **Cargo-culting tutorials** — copy tutorial code without thinking; same mistake as LLM era
4. **Over-claiming learning** — "I built a compiler" from 500-line toy → overstates understanding of real compilers
5. **Ignoring LLM era** — refusing AI tools out of Feynman purity; real-world dev benefits from both

## 11. When NOT to apply Feynman strictly

- **Production pressure** — ship now, learn later
- **Commodity tasks** — don't build your own HTTP lib; use `requests`
- **Pre-existing expertise** — seasoned dev doesn't need to rebuild to understand
- **Team standards** — company uses Django; don't build from scratch in workplace
- **Time-to-market** — startups can't afford deep-build culture

## 12. Storm Bear vault relevance

### Scrum coaching context

Storm Bear operator (Cvtot) coaches Scrum teams. Teams learn via:
- **Kata pattern** — small exercises, iteratively harder (Feynman-aligned)
- **Retrospectives** — reflect on what happened, extract lessons (Feynman-aligned)
- **Spike stories** — time-boxed exploration to de-risk (Feynman-aligned)

**build-your-own-x = Scrum-adjacent in spirit.** Both emphasize learning-by-doing over learning-by-reading.

### Application to Storm Bear wiki building

Storm Bear's 8 wikis = demonstration của LLM Wiki pattern (Karpathy's insight).

**Feynman tie-in:** Cvtot + Claude **built** these wikis by hand (with routine automation). Now Cvtot understands LLM Wiki pattern at Feynman level — could build custom variants, knows failure modes, anticipates scale issues.

→ **Storm Bear vault = Feynman philosophy applied to knowledge management.**

### Future Storm Bear Feynman-style deliverables

- **Build your own LLM Wiki routine** (extract routine pattern, publish as OSS)
- **Build your own Scrum knowledge vault** (template for other Scrum coaches)
- **Build your own agent framework comparison** (taxonomy methodology)

## 13. References / Nguồn

- Source: [[(C) README positioning summary]] (philosophy section)
- Related entities:
  - [[(C) 29 Categories Taxonomy]]
  - [[(C) Curation Model]]
  - [[(C) Storm Bear Vault — Knowledge Architecture Lessons]]
- External:
  - Richard Feynman biography (public domain)
  - Feynman Lectures on Physics (his pedagogical approach)
  - Anders Ericsson — "Peak" (deliberate practice, Feynman-adjacent)
