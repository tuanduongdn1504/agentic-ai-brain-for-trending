# Symphony architecture — community-implementation triangulation

> **Created:** 2026-05-09
> **NotebookLM ID:** d772d58b-ff6c-41c5-aec1-7cd83637226e (6 sources after adding 3 Symphony community repos)
> **Pivot rationale:** OpenAI's official Symphony spec page (https://openai.com/index/open-source-codex-orchestration-symphony/) failed Tier 1 + Tier 2 bypass — backend gates Cloudflare-blocked. Community implementations are PUBLIC GitHub repos, no Cloudflare. 3 independent reproductions = stronger evidence than 1 spec.
> **Sources 4-6 (newly added):** ACNoonan/symphony-restate (Elixir+Restate+Linear) · ryanjdillon/symphony (Go, multi-agent) · howardpen9/symphony-rs (Rust)
> **Sources 1-3 (pre-existing):** YouTube talk + Latent Space podcast + OpenAI blog

## Symphony architecture — converging evidence across all 6 sources

Different notebook specified, starting new conversation...
Continuing conversation 4244250a...
Answer:
Across the six sources, Symphony is consistently presented as a **long-running, 
agent-agnostic orchestration layer** designed to move humans out of the 
synchronous development loop. By triangulating Ryan Lopopolo’s claims with 
community implementations in Elixir, Go, and Rust, a clear architectural 
blueprint emerges.

### **What Symphony Does**
Symphony transforms software development into a **durable, automated pipeline** 
where agents are treated as teammates rather than co-pilots [1]. It autonomously
polls issue trackers for work, prepares isolated environments, executes agentic 
reasoning loops, and manages the entire pull request (PR) lifecycle—including 
code review, conflict resolution, and merging [2-4].

### **Core Components**
*   **Orchestrator/Service:** The central "brain" that manages polling 
intervals, issue "claims" to prevent duplicate work, and state reconciliation 
[4, 5].
*   **Agent-Agnostic Runner:** A pluggable interface that allows the system to 
spawn different models, including **Codex**, **Claude Code**, and 
**GPT-5.2/5.4**, as subprocesses [2, 6, 7].
*   **Workspace Manager:** A component responsible for creating isolated git 
worktrees via lifecycle hooks (e.g., `after_create`, `before_run`), ensuring 
that agents operate in clean, sandboxed environments [4-6].
*   **Codex App-Server Client:** Communication between the orchestrator and the 
model is typically handled via a specialized protocol over **stdio** [5, 8].
*   **Real-time Dashboard:** Community versions implement UIs (using React or 
Phoenix LiveView) to visualize running sessions, token usage, and retry queues 
[6, 9].

### **Data Flow and Workflow**
1.  **Ingress:** Symphony polls **Linear** for issues in active states like 
"Todo" or "In Progress" [4].
2.  **Seeding:** It loads a `WORKFLOW.md` file (a prompt template with YAML 
frontmatter) and renders it using engines like Liquid to provide task-specific 
context [5, 10, 11].
3.  **Execution:** The system spawns an agent subprocess and provides it with 
**"Skills"**—repository-embedded scripts that allow the agent to launch the app,
query databases, or drive browsers [12-15].
4.  **The "Ralph Loop":** Agents iterate in a self-correction loop where one 
agent implements a task and another (or the same agent in a new session) reviews
the implementation against the specification until it is high-fidelity [12, 16].
5.  **Egress:** Once the task is complete, the agent uses the **GitHub CLI 
(`gh`)** to open a PR, respond to feedback, and eventually merge the code once 
CI passes [3, 12, 17].

### **Languages and Frameworks**
*   **Internal Reference (OpenAI):** Built on **Elixir** and the **BEAM VM**. 
Lopopolo notes that Elixir’s native **process supervision** and **GenServers** 
are uniquely suited for coordinating hundreds of concurrent agent "daemons" [2, 
18, 19].
*   **Community Implementations:** The architecture has been successfully 
reproduced in **Go** (focusing on SSH remote workers and OpenTelemetry) [4, 6], 
**Rust** (focusing on typed safety and CLI performance) [5, 20], and 
**Restate/Elixir** (providing durable execution to survive node failures) [8, 
21].
*   **Build Systems:** Symphony works best with high-speed build tools like 
**Turbo/NX** to keep the "inner loop" under one minute [22, 23].

### **Integrations**
*   **Issue Trackers:** Primarily **Linear** via its GraphQL API [2, 20, 24].
*   **Version Control:** **GitHub** for repository management and PR automation 
[6, 12, 25].
*   **Observability:** Integrates with local and cloud stacks including 
**OpenTelemetry (OTEL)**, **Prometheus**, **Victoria Stack**, and **Grafana** to
provide agents with logs and metrics [6, 26, 27].
*   **Browser/UI Tools:** **Playwright** and the **Chrome DevTools Protocol** 
allow agents to visually inspect and test the applications they build [28, 29].

Resumed conversation: 4244250a-269f-498f-962c-4c33d26d288b

## Where do community implementations DIVERGE from Lopopolo's claims?

Different notebook specified, starting new conversation...
Continuing conversation 4244250a...
Answer:
A comparison of the community implementations of Symphony against Ryan 
Lopopolo's internal descriptions reveals a shift from a **single-node research 
experiment** to a **distributed, production-hardened architectural pattern**. 
While the community closely follows the core **"SPEC.md"** provided by OpenAI, 
they have introduced significant deviations in state durability and remote 
execution.

### **1. Architectural Choice Differences**
The primary architectural deviation is the transition from **ephemeral in-memory
state** to **durable execution**:

*   **Durable State vs. In-Memory**: Lopopolo’s Symphony describes a system 
where exact in-memory scheduler state is not restored upon restart [1]. The 
**Elixir/Restate** community version (Source 3) explicitly addresses this "gap" 
by using Restate to ensure orchestrator state is durable; if a node dies 
mid-flow, every issue resumes on a different node without losing the 
conversation journal or creating "double-dispatches" [2, 3].
*   **Distributed Remote Workers**: Lopopolo describes agents running in local 
worktrees on a developer box [8, Source 1]. The **Go implementation** (Source 5)
moves to a distributed model, introducing **SSH remote workers** with 
least-loaded host selection and health tracking to execute agent sessions across
a fleet of machines [4].
*   **Language Diversification**: While Lopopolo champions **Elixir and the 
BEAM** for its process supervision [96, Source 2], the community has 
successfully ported these concepts to **Rust** for typed performance (Source 4) 
and **Go** for operational simplicity and integration with the **OpenTelemetry 
(OTLP)** ecosystem [4, 5].

### **2. Lopopolo Features Missing from Community Versions**
Several "high-frontier" capabilities emphasized by Lopopolo are not yet 
represented in the community repositories:

*   **Visual Perception and Rasterization**: Lopopolo places heavy emphasis on 
making the application **UI directly legible** to agents by wiring the **Chrome 
DevTools Protocol** into the runtime and rasterizing images so models can "see" 
layout issues [6-8]. Community versions currently focus on text-based 
integrations like Linear and the filesystem [3, 5, 9].
*   **The "Editor Ban" Culture**: Lopopolo’s vision relies on a strict 
**prohibition of human-written code**, forcing all fixes through the agent 
harness [10]. Community implementations are still primarily tools used by humans
to "manage work" rather than enforcing a total exclusion of manual edits [9].
*   **Post-Merge Human Review**: Lopopolo argues that synchronous pre-merge 
review is the ultimate bottleneck [11, 12]. Community implementations still seem
to operate within standard PR workflows where humans are expected to validate or
"snapshot" work before it is finalized [4, 5].

### **3. Community-Added Capabilities Not Mentioned by Lopopolo**
The community has introduced several operational "quality-of-life" features that
go beyond the original OpenAI descriptions:

*   **Cold-Path Conversation Seeding**: To handle node failures in a distributed
system, the Elixir/Restate version (Source 3) added a **"cold-path seeding"** 
mechanism that allows a fresh agent session on a new node to rehydrate its 
entire thread context from durable state [3, 13].
*   **Embedded Dashboards and Multi-Workflow Management**: The Go implementation
(Source 5) includes a **React dashboard embedded directly in the binary** and a 
"multi-workflow" feature that watches a directory to dynamically add or remove 
`WORKFLOW.md` files without restarting the service [4, 14].
*   **Cloud-Native Deployment Patterns**: While Lopopolo focuses on the local 
developer experience, the community has provided explicit **Kubernetes, FluxCD, 
and Traefik** deployment manifests, treating Symphony as a "single-replica 
Deployment" for enterprise-grade automation [15].
*   **Mutation Guards and Tool Validation**: Source 5 introduced a **ToolHandler
interface** with explicit mutation guards and single-operation validation for 
the `linear_graphql` tool to prevent agents from performing unauthorized 
destructive actions [4, 14].

Resumed conversation: 4244250a-269f-498f-962c-4c33d26d288b

## What does this tell us about claim #4 (Symphony 5-10 PRs/day throughput)?

Different notebook specified, starting new conversation...
Continuing conversation 4244250a...
Answer:
None of the community implementations provide independent evidence to verify 
Lopopolo's claim that Symphony enables **5-10 PRs per engineer per day** [1-3]. 
While Lopopolo explicitly cites an increase from a **3.5 PR baseline** (reported
in February 2026) to **5-10 PRs** (reported in April 2026) following the 
integration of Symphony and reasoning models like GPT-5.2, the community sources
focus on **architectural replication and technical durability** rather than 
operational throughput metrics [1, 4-6].

The current documentation for these community projects reflects early-stage 
development rather than high-velocity production data:

*   **Development Status**: The **Elixir/Restate** implementation is explicitly 
labeled as **"pre-alpha"** as of May 2026 [1]. The **Rust** rewrite describes 
its status through **"local smoke checks"** such as `cargo test` and `cargo run 
-- validate` rather than longitudinal performance data [2].
*   **Performance Characteristics**: The **Go implementation** documents **117 
tests** covering components like workspace sanitization and orchestrator 
scheduling, but it does not list any **real-world throughput benchmarks** [3]. 
It does, however, include **OpenTelemetry metrics** (counters and histograms) as
a feature to allow users to track their own performance, though no sample data 
is provided [7].
*   **Focus on Invariants**: Rather than documenting PR volume, the community 
focuses on **reliability and state survival** [8]. For instance, the Restate 
version includes a **"demo script"** designed to prove architectural invariants 
by killing the orchestrator mid-flow to ensure the **conversation journal and 
claim state** survive node death [9, 10].
*   **Operational Scale**: While Lopopolo emphasizes the scale of the **"Dark 
Factory"**—managing **1,500 merged PRs** over five months—the community 
implementations currently focus on the **"once" or "snapshot"** execution of 
single issues to verify the **SPEC.md** contract [2, 4, 6].

In summary, the community repositories provide a **functional verification** of 
the Symphony specification but do not yet document the **operational data or 
velocity gains** claimed by Lopopolo [1, 2]

Resumed conversation: 4244250a-269f-498f-962c-4c33d26d288b
