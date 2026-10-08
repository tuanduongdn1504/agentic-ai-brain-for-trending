# GSV Mobile Engineer — Interview Prep

> **Role:** Mobile Engineer · **Glory Software Vietnam** (Vietnam arm of **GLORY Ltd.**, Japanese, HQ Himeji) · 2nd Floor, Tan Cuong Building, 47 Núi Thành St, Hòa Cường Ward, Đà Nẵng.
> **Product domain:** software for **Cash Handling Machines** — cash recyclers/counters for banks and retail.
> **Hours:** 8:00–12:00 / 13:00–17:00, Mon–Fri *(early, fixed, Japanese-style — with a real lunch break)*.
> **Benefits:** "attractive income package", 13th month, annual review, insurance, health checks, **company-sponsored English and Japanese classes**, sponsored L&D, some international travel.
> **Apply:** `careers@glory-software.vn` — **resume in PDF format** (they say so explicitly).
> **Companion file:** `(C) GSV Mobile Engineer — Technical Study Pack.md` — the technical depth. **Read this file first.**

---

## ⭐ The headline: this is your best-fit application of all seven

Not a stretch, not a pivot. They ask for **3+ years with strong JavaScript/TypeScript and solid React Native + Expo** — you have **5 years, two shipped Expo apps on both stores**, and you currently lead mobile delivery. Then their last two responsibilities are *"mentor engineers through code reviews, technical guidance, and knowledge sharing"* and *"help establish engineering standards and contribute to scaling the mobile engineering team"* — which is **PSM II, L&D Executive, an internship program you ran end-to-end, a colleague you coached to PSM II, and the methodology manuals you wrote.** Very few mobile engineers bring that half.

**And it is a genuinely stable employer:** a Japanese manufacturer's software arm, building for regulated financial hardware — long product lifetimes, conservative release practices, real benefits. That is exactly the "stable team where I can go deep and mentor" you said you wanted.

### The fit map — be clear-eyed about all three columns

| Their requirement | You | Verdict |
|---|---|---|
| Bachelor's in SE / IT | Kỹ sư CNTT – Software Engineering (PFIEV) | ✅ |
| **3+ yrs professional SWE, strong JS/TS** | 5 years | ✅✅ **exceeds** |
| **Solid React Native** | Core skill, 5 years, 2 shipped products | ✅✅✅ |
| **Expo + modern practices** | Expo Router, prebuild, EAS Build/Submit, OTA | ✅✅✅ |
| PostgreSQL · Docker · containerized dev | Express+PostgreSQL role, Supabase Postgres, thesis, Docker | ✅ |
| CI/CD + DevOps practices | Jenkins, SonarQube, EAS pipelines, conventional commits | ✅ |
| Scalable system architecture design | Own the RN architecture; integrate across microservices | ✅ / ⚠️ *mobile-side strong, distributed-systems side lighter* |
| Product-focused / startup environment | CVTOT product company, 2 shipped products | ✅✅ |
| **Mentoring, code review, knowledge sharing** | PSM II · L&D Executive · internship program · coached a colleague to PSM II | ✅✅ **your standout** |
| **Establish standards, scale the team** | Wrote the methodology manuals; introduced Agile delivery | ✅✅ |
| OAuth 2.0 / OIDC / certificate-based | OAuth2 + multi-social SSO + JWT + the refresh-token/HttpOnly investigation | ✅ OAuth2 strong · ⚠️ **OIDC and mTLS conceptual only** |
| App security fundamentals incl. **OWASP** | ISO/IEC 27001:2022 ×3 + ISO 19011 — rare and real | ⚠️ **but ISMS ≠ OWASP.** Don't conflate them (see §2) |
| Monitoring/debugging **cloud-native** apps | Mobile + API-boundary troubleshooting: yes. Cloud infra: no | ⚠️ partial |
| **Node.js, preferably NestJS** | Express + HapiJS. **NestJS: never used** | ❌ **real gap** |
| **Cloud-native on AWS or GCP** | Supabase, Firebase, Heroku, AWS-via-LocalStack. No production AWS/GCP | ❌ **real gap** |
| **Serverless (Lambda / Cloud Functions)** | None | ❌ **real gap** |
| **Excellent written *and spoken* English** | Written strong. **Spoken: working level, improving** | ⚠️⚠️ **THE GATE** |

**Strong on nine. Partial on four. Genuinely absent on three.** For a job posting, that is a good application — nobody hits 16/16, and you dominate the three requirements that define the role.

---

## §0 — The two conversations that decide this

### A. Spoken English ⚠️ your #1 risk (same as HBG)

The JD says *"Excellent written and spoken English communication skills, with experience collaborating through chat and video conferencing."* With a Japanese parent company and distributed teams, that is not decoration — **you will be on video calls with people whose common language with you is English.**

- **Your CV and application email are the written half, and they are strong.** That half is already won.
- **The spoken half is what you must practise.** The good news: unlike HBG (where facilitation *is* the job), here English is a *collaboration* requirement, not the core competency — a technically excellent engineer with working-level spoken English can still land this. But it is the single highest-value thing you can rehearse.
- ⭐ **The drills are in the Study Pack's "company" section** — video-call English specifically: clarifying, confirming understanding, narrating a screen-share, asking someone to repeat without losing face.
- **Honest self-assessment line** *(don't claim "excellent")*:
  > *"My written English is strong — I work in English documentation and tooling every day. My spoken English is at a solid working level and actively improving; I'm comfortable in technical discussions, and I'll ask for clarification rather than guess."*
- ⭐ **The benefits list includes company-sponsored English and Japanese classes.** That is a gift: it tells you they *expect* to invest in language, which makes your honest "working level and improving" far less disqualifying. **You may reference it** — *"I saw you sponsor English classes, which is one of the things that attracted me."*

### B. The NestJS / AWS / serverless gap — say it first, and make it the reason you want the job

Three of their qualification bullets you genuinely do not have. **Do not bluff any of them** — a NestJS question from a real NestJS developer will expose a bluff in two follow-ups, and then everything else you said becomes suspect.

**The frame that works:**
> *"On the mobile side I'm bringing five years and two shipped Expo products, and I can own that surface completely. On the backend side I want to be precise with you: I've worked with Node in Express and HapiJS, with PostgreSQL, and I integrate against microservices daily — but I have not used NestJS, and my cloud experience is Supabase, Firebase and Heroku rather than production AWS or GCP. That's honestly part of why this role interests me: it's the direction I want to grow, next to the mobile work I'm already strong at."*

- ⭐ **Study the Study Pack's `nestjs` and `cloud` sections anyway.** The goal is not to claim experience — it is to *hold the conversation*: know what DI and the IoC container are, why NestJS is structured the way it is, what "cloud-native" means, what Lambda is and when it's the wrong choice. **Understanding without experience is a completely respectable answer. Ignorance is not.**
- ⚠️ **Never say "I can learn it quickly" and stop there.** Everybody says that. Say instead: *"Here's what I already know about it, here's what transfers from my Express work, and here's the part I'd need to learn on the job."* Specificity is what makes "I learn fast" believable.

### C. ⚠️ The GSV double-application decision

You have a **Project Manager** application to GSV drafted to this same address, unsent. **My recommendation: send the Mobile Engineer application only.** The full reasoning is at the bottom of `(C) Application Email (GSV, Mobile Engineer).md` — read it before you send anything. If you already sent the PM one, tell me and I'll adjust this email's opening.

---

## §1 — ⭐ Priority study order (this is the most useful section in the file)

You have limited hours. Spend them in this order — it is ranked by **(likelihood they ask) × (damage if you fumble)**:

| Priority | What | Why | Where |
|---|---|---|---|
| **1** | **Spoken English drills** | The one requirement that can fail you regardless of technical strength | Study Pack → `company` |
| **2** | **Your own RN/Expo depth, said out loud at senior level** | Their #1 requirement and your #1 strength — *you must not be merely competent here, you must be impressive* | Study Pack → `rn-expo` |
| **3** | **NestJS concepts** (DI/IoC, modules, controllers/services, DTOs, guards vs interceptors vs middleware) | Their most-named gap; they will probe it. Understanding ≠ claiming | Study Pack → `nestjs` |
| **4** | **OAuth 2.0 / OIDC / PKCE / token storage** | Explicitly listed, and **your strongest gap-to-strength** — you have a real war story | Study Pack → `security` |
| **5** | **The GLORY domain** (cash handling, why they need mobile apps, Japanese work culture) | Cheap to learn, disproportionate impression, and generates your best questions | Study Pack → `company` |
| **6** | **Cloud/serverless concepts** | A real gap, but they're less likely to interrogate deeply for a *mobile* role — know the vocabulary and be honest | Study Pack → `cloud` |
| **7** | **PostgreSQL / Docker / CI/CD / incident triage** | You mostly have this; skim to sharpen the wording | Study Pack → `platform` |

⭐ **If you only get two hours:** do **1 and 2**. Being unmistakably excellent at the thing they're hiring for, in intelligible spoken English, beats being mediocre across seven dimensions.

---

## §2 — The honest lines: what to say when you don't have it

Delivered confidently, these are *strengths* — they show calibration, which is exactly what a Japanese engineering culture values over self-promotion. Pick the ones that fit and rehearse them until they sound relaxed rather than defensive.

⚠️ **Two things never to conflate**, because a security-minded interviewer will catch it:
1. **ISO/IEC 27001 ISMS ≠ OWASP.** ISO 27001 is an *information-security management system* — governance, policy, risk treatment, auditing. OWASP is *application security* — concrete vulnerability classes and testing. You hold the former. Saying "I know OWASP because I have ISO 27001" would be wrong and would cost you credibility. The correct line: *"My formal security training is ISO 27001 ISMS, which is governance rather than application-level testing. On the application side my hands-on work is authentication — OAuth 2.0, SSO, JWT, token storage and a refresh-token flow I debugged in production. OWASP's mobile risk list I know as a checklist rather than from formal practice."*
2. **OAuth 2.0 ≠ OIDC.** OAuth 2.0 is authorization; OIDC is an authentication/identity layer built on top of it, adding the ID token. You have implemented social sign-in over OAuth 2.0 — that touches OIDC in practice, but do not claim you have deliberately implemented an OIDC relying party unless you did.


**NestJS & Backend Contributions for Mobile Engineers**
- *"I haven't built a NestJS project yet, but I've studied the framework and understand the core architecture—modules, controllers, services, dependency injection, and guards. I'm confident adding endpoints, fixing queries, and implementing features following existing patterns."*
- *"My security foundation is ISO 27001 governance and OAuth 2.0 / JWT authentication on the mobile side. I haven't formally implemented OIDC or certificate-based security, but I understand the concepts and can learn quickly when pairing with your backend team."*
- *"I have no production experience with AWS Lambda or Google Cloud Functions. I've used LocalStack and Firebase, which taught me the concepts, but I'm not the expert on your cloud infrastructure. I'm ready to learn and contribute."*
- *"Dependency injection is new to me as a first-class framework feature, but the concept is clear. In Express, you manually create instances; in NestJS, the IoC container does it. I understand why it matters—testability, decoupling, lifecycle management."*
- *"If you asked me to architect a new NestJS system from scratch today, I'd need guidance. But for typical contributions—adding an endpoint, writing a DTO, implementing a guard, fixing a slow query—I can do that by reading the existing code and following the established pattern."*
- *"I know TypeScript well from React Native work, so NestJS's TypeScript-first approach is natural to me. The biggest mental shift is the module system and DI, not the language."*
- *"I've reviewed OWASP concepts in code but haven't done formal penetration testing or comprehensive security audits. I understand injection, XSS, and CSRF as code defects and can spot them in reviews. I'd pair with your security owner on the first full code review."*


**AWS/GCP Cloud-Native & Serverless for Mobile Engineers**
- *"I haven't built production systems on AWS or GCP, but I've worked with managed services locally and understand the patterns."*
- *"NestJS is new to me, but I've built Node.js APIs with Express and HapiJS, so I understand the underlying concepts. I'd ramp up in the first sprint with team code reviews."*
- *"I don't have hands-on OWASP penetration testing experience, but my ISO 27001 background means I think about risk and access control. I apply OWASP principles in code review — parameterized queries, managed auth, input validation."*
- *"I'd choose ECS/Fargate for the main API, not Lambda, because cold starts aren't acceptable for a cash-handling app. Lambda is better for async background jobs."*
- *"I haven't worked with Cognito specifically, but I've built OAuth 2.0 multi-social login and JWT-based auth. Cognito is the managed version; it saves me from building sign-up validation, MFA, and password reset."*
- *"Pre-signed URLs are how I'd handle file uploads: backend generates a time-limited URL, mobile app uploads directly to S3, no AWS credentials in the app. I've done similar patterns with Firebase Storage."*
- *"My security grounding is ISO 27001 ISMS (governance, access control, incident response), not OWASP penetration testing. They're complementary — I'd work with your security team on threat modeling and OWASP-specific testing."*
- *"I'd start with single-region, multi-AZ RDS and add multi-region complexity only when data shows we need it. First sprint: get the basics right."*
- *"I don't have Secrets Manager experience, but I understand the pattern: encrypted vault, IAM roles, automatic rotation. I'd never commit a password to git."*
- *"I haven't deployed a scheduled Lambda or S3-triggered Lambda to production, but I understand the pattern and the 15-minute timeout limit. I'd use it for receipt processing, not the main API."*
- *"My experience integrating mobile apps with backends is hands-on — I own the client-side logic and debug the seams, but I don't author the backend services. That's the collaboration I'd bring."*


**OAuth 2.0, OIDC, Certificate Security & OWASP — Mobile Engineer Interview Prep**
- *"I've shipped OAuth 2.0 with social SSO and JWT validation in production, including a detailed investigation of refresh-token rotation. I understand OIDC conceptually—identity layer on OAuth, ID token as a JWT, JWKS key rotation—but I haven't built an OIDC flow from scratch. I'm confident I could implement it with reference to the OIDC spec."*
- *"I store tokens securely in Keychain/Keystore and have prevented AsyncStorage breaches in code review. I haven't implemented certificate pinning in a shipping app, but I understand the mechanics and the operational risk of certificate rotation. I'd coordinate with GLORY's ops team on rotation schedules before implementing pinning."*
- *"My security background is ISO/IEC 27001 ISMS—governance, risk management, audit trails. I haven't done formal OWASP penetration testing or vulnerability scanning. I apply OWASP Mobile Top 10 principles in code review: insecure storage, weak communication, insufficient authorization. For a formal security audit, GLORY would want a dedicated penetration tester."*
- *"I understand mTLS and certificate-based security at the conceptual level. I haven't implemented mTLS in a React Native app, but I know the implementation requires a custom HTTP client (react-native-ssl-pinning or similar) and close coordination with backend engineers and ops on certificate lifecycle."*
- *"I've used Node.js with Express and HapiJS in production. I don't have NestJS experience yet. I'm fluent in TypeScript, and NestJS patterns (decorators, dependency injection, modules) are familiar from Express. I'd be productive on a NestJS project within a few weeks of ramp-up."*
- *"I've worked with managed cloud services (Supabase, Firebase, Heroku) and local AWS emulation (LocalStack). I don't have production experience deploying or managing AWS Lambda, DynamoDB, or cloud-native infrastructure at scale. I'm prepared to learn this on the job with GLORY's cloud team."*
- *"I'm fluent in written English and at a working level in spoken English, with ongoing improvement. I'm comfortable in chat-based collaboration and confident in video calls with technical teams. I may occasionally need to clarify complex topics, and I prefer to ask questions over making assumptions."*
- *"My mobile experience is React Native + Expo. I also know Flutter/Dart, but my primary stack is React Native. For this role at GLORY, React Native is the match. I'm prepared to contribute to backend services (Node.js) and cloud infrastructure, but my deepest expertise is on the mobile side."*


**React Native + Expo: Senior Architecture & Performance Deep Dive**
- *"I've built React Native apps with Express and HapiJS for the backend, handling authentication, database queries, and API design. NestJS is a different pattern on Node.js — more structured with decorators and dependency injection — but the fundamentals (async/await, error handling, middleware, data persistence) are the same. I'm confident ramping up on NestJS quickly."*
- *"I've worked with managed cloud services (Supabase, Firebase, Heroku) and emulated AWS services locally using LocalStack for testing. I haven't deployed Lambda or a production serverless function, but I understand the stateless model and cost-per-invocation billing. I'm ready to implement serverless architecture in a production setting."*
- *"I've implemented OAuth 2.0 social login and JWT-based authentication, including debugging a production issue with token refresh over HttpOnly cookies. OIDC is a standardized profile on top of OAuth 2.0 (ID tokens vs access tokens, OpenID discovery). I haven't built a dedicated OIDC flow, but I'm comfortable learning it in context."*
- *"My security background is ISO/IEC 27001 ISMS (governance, risk management, internal auditing), which is different from OWASP application-security testing. I understand defense-in-depth principles, but I haven't hands-on practiced OWASP vulnerability testing (SQL injection, XSS, CSRF exploitation). I'm ready to integrate OWASP best practices into our development workflow."*
- *"I speak and write English at a working level and improving. I've collaborated with distributed teams via video and chat. For this role's requirement of 'excellent spoken English,' I'm committed to practicing and continuing to improve."*


**Mobile Engineer Interview Prep: PostgreSQL, Docker, CI/CD, Monitoring (GSV Job)**
- *"I haven't used NestJS specifically — my backend experience is Express.js and HapiJS. I'd expect to learn NestJS quickly because HTTP fundamentals are similar."*
- *"I don't have production experience with AWS or GCP serverless. I've used Supabase and LocalStack for adjacent work, and I understand the concepts. I'd be confident setting up Lambda or Cloud Functions with documentation."*
- *"I don't have hands-on OWASP application security testing experience. My security background is ISO/IEC 27001 ISMS (governance), not application-level attack vectors. I know OWASP Top 10 at a conceptual level."*
- *"I haven't implemented OIDC or certificate-based mTLS in production. I've done OAuth 2.0 and JWT; OIDC is OAuth + identity layer. I'd approach it by reading the spec and framework docs."*
- *"My spoken English is improving. I communicate effectively in writing and technical discussions, but I may speak carefully in a live interview. I'm comfortable asking clarifying questions."*
- *"I haven't set up ELK Stack or Datadog in production. I understand structured logging — fields as JSON so logs are queryable. I've used Sentry for mobile crash reporting with source maps."*
- *"I haven't managed Gitflow with develop and release branches. I've worked with trunk-based workflows — feature branch, code review, merge to main. I understand both."*
- *"I haven't deployed to Docker Swarm or Kubernetes. I'm comfortable with docker-compose for local development and Docker image best practices. Orchestration would require learning, but the fundamentals are clear."*


**GLORY Software Vietnam: Mobile Engineer Interview Study Guide**
- *"I don't have NestJS experience, but I'm fluent in Express and HapiJS — I understand Node.js fundamentals, and NestJS is TypeScript with structure on top of that. I've read the docs and I'm ready to pick it up quickly."*
- *"I haven't shipped production code on AWS Lambda or Google Cloud Functions. I have used Firebase, Heroku, and Supabase. I understand the serverless model — event-driven, pay-per-invocation — and I'm confident I can learn the AWS-specific patterns on the job."*
- *"I've implemented OAuth 2.0 and JWT. I haven't built OIDC flows or mTLS endpoints myself, but I understand the PKI fundamentals and the conceptual model. I'm ready to learn."*
- *"My spoken English is at working level and improving. I'm comfortable in technical video calls and I ask for clarification when I need it. I'm reliable in written communication, which is important for documentation and async collaboration."*
- *"I haven't worked in cash-handling or regulated financial systems before, but I have ISO 27001 training, which taught me how to think about compliance and auditability. I'm ready to learn the domain."*
- *"I've debugged production issues and investigated security problems methodically. I use a structured approach: isolate, test, document, escalate. I'm comfortable working in a quality-focused environment where reliability matters."*


---

## §3 — Question bank (72 questions with model answers)

> Grouped by dimension. These came from six specialist agents and were technically fact-checked; the five corrected facts are listed at the top of the Study Pack. **Work through them in the §1 priority order, not top to bottom.**

### NestJS & Backend Contributions for Mobile Engineers

**Q. You've never used NestJS before. Walk me through how you'd add a new endpoint to an existing NestJS module.**

I'd first study the existing module—look at the controller, service, and DTO structure. Let's say I'm adding a bulk-delete endpoint to users. I'd add a @Delete('bulk') method to the controller that calls a bulkDelete() service method. The service talks to the repository, which handles the database delete query. I'd write a DTO for the request if needed, add a guard if authorization is required, and write a unit test for the service. The pattern is clear from the existing code.

**Q. What's the difference between middleware, guards, and interceptors in NestJS? When would you use each?**

Middleware runs first, globally or per-route, before the controller is even reached. Use it for CORS, body parsing, global logging. Guards run next and make a yes/no decision—can this user access this route? Use guards for authentication (JWT check) and authorization (role check). Interceptors wrap the controller and service, running before and after. Use them for request/response transformation, timing, caching. The order matters: middleware → guards → interceptors (pre) → controller/service → interceptors (post). Middleware can't throw 403; guards can. Interceptors can modify both request and response.

**Q. Explain dependency injection in NestJS. Why is it different from Express?**

In Express, you manually create and pass instances: `const service = new MyService(db)`. In NestJS, you declare a dependency in the constructor, and the IoC container creates and injects it automatically. The service is a singleton—one instance for the entire app. This makes testing easier (you mock the service), decouples classes (the controller doesn't know how to create a service), and lets NestJS manage lifetimes. It's a shift in mindset, but it's cleaner than Express's manual wiring.

**Q. You're reviewing a NestJS service that's doing N+1 queries. How would you fix it?**

I'd check the TypeORM query. By default, relations aren't loaded, so each user fetch triggers a new query for roles or posts. I'd add `leftJoinAndSelect()` to the find call to eager-load the related data in one query. Or I'd use the `relations` option: `find({ relations: ['posts', 'roles'] })`. If it's a specific query, I'd write a custom query builder with all joins included. The fix depends on whether you always need the relations or only sometimes.

**Q. How do you handle validation in NestJS? Is it automatic?**

Yes, if you set up the ValidationPipe. In the main.ts file, I'd add `app.useGlobalPipes(new ValidationPipe({...}))`. Then, in the DTO, I'd decorate properties with class-validator rules: `@IsEmail()`, `@MinLength(3)`, etc. When a request comes in, NestJS validates the body against the DTO. If it fails, it returns a 400 with error details. You don't need to manually check types or ranges—it's automatic and type-safe.

**Q. What's the repository pattern, and why would you use it in a NestJS service?**

The repository is a class that wraps database queries. Instead of calling `repository.find()` directly in the service, you create a UsersRepository class with methods like `findById()`, `findByEmail()`, and `save()`. The service calls the repository, not the ORM. This decouples the service from the ORM (easier to swap ORMs later), centralizes query logic, and makes tests simpler (you mock the repository). It's optional, but good practice in larger systems.

**Q. How would you write a test for a NestJS service that depends on a database repository?**

I'd use `@nestjs/testing` to create a test module. I'd mock the repository by providing a Jest mock in the Test.createTestingModule() call. For example: `{ provide: getRepositoryToken(User), useValue: { find: jest.fn(), save: jest.fn() } }`. Then, in the test, I'd spy on the mock and verify it was called with the right arguments. This isolates the service from the database, making tests fast and reliable.

**Q. You need to add OAuth 2.0 authentication to a NestJS endpoint. Where would you put that logic?**

I'd create an `auth.guard.ts` that implements CanActivate. The guard extracts the token from the Authorization header, verifies it (by calling an auth service), and returns true or throws UnauthorizedException. Then, I'd decorate the controller method with `@UseGuards(AuthGuard)`. If I need to attach the user object to the request, I'd do that in the guard's `request.user = ...`. The guard runs before the controller, so by the time the endpoint runs, I know the user is authenticated.

**Q. What's the IoC container, and how does it help you?**

The Inversion of Control container is NestJS's dependency injection engine. It reads your @Module() declarations, builds a dependency graph, creates instances of providers (services, guards, etc.), and injects them where needed. You don't call `new` in your code. The container handles creation and cleanup. It helps by making code testable (swap real services for mocks), decoupled (classes don't know how to create dependencies), and managed (NestJS controls lifetimes). It's the core idea behind NestJS.

**Q. You've worked with Express and HapiJS. How does NestJS differ in handling errors?**

In Express, you'd use middleware: `try/catch` in routes, then `app.use((err, req, res, next) => {...})` for the global handler. In NestJS, you throw exceptions from services—`throw new NotFoundException()`, `throw new BadRequestException()`—and the framework maps them to HTTP responses. Filters catch exceptions if you need custom handling. It's cleaner than Express's manual error plumbing. The concept is the same, but NestJS automates it.

**Q. What does `@Injectable()` do?**

`@Injectable()` marks a class as a provider that can be injected into other classes. It tells NestJS, 'Create one instance of this class and make it available via dependency injection.' Services, guards, interceptors, and repositories all need it. Without it, NestJS won't recognize the class as injectable. It's metadata that feeds into the IoC container.

**Q. You've never built a full NestJS project. How confident are you contributing to one?**

Very confident for typical mobile-engineer tasks—adding endpoints, fixing queries, writing DTOs, implementing guards. I'd read the existing module structure first to understand the pattern, then follow it. For architectural decisions or debugging complex interceptor chains, I'd pair with someone. I've studied NestJS and understand the core patterns. The gap is hands-on experience, not conceptual understanding. I learn fast by reading code.


### AWS/GCP Cloud-Native & Serverless for Mobile Engineers

**Q. Tell us about your cloud-native experience. Have you deployed to AWS or GCP?**

I haven't built production systems on AWS or GCP, but I've worked with managed services locally and in projects: LocalStack for SQS/DynamoDB emulation, Supabase for managed Postgres and storage, Heroku and Firebase for deployment. I understand the pattern — managed services handle operations, I focus on application logic. For Glory, I'd ramp up on AWS-specific tools in the first sprint with the team: CloudWatch for monitoring, IAM for access control, Secrets Manager for credentials. My Express and HapiJS experience transfers directly — Node.js APIs are Node.js APIs; the deployment surface just changes.

**Q. Which compute option would you choose for Glory's main API: Lambda, ECS/Fargate, or EC2? Why?**

ECS/Fargate. Here's my reasoning: Glory's mobile app and backend need low, predictable latency (<1s) for every user-facing operation. Lambda has cold starts of 1-3 seconds, which is unacceptable for a cash-handling app where users expect instant feedback. Lambda is better for async work — processing receipts in the background, running scheduled cleanup jobs. ECS/Fargate keeps a container warm 24/7, so every request is <100ms. Cost-wise, ECS/Fargate is ~$60/month minimum for two tasks; Lambda would be cheaper if Glory only got 100 requests/day, but at scale (thousands of transactions/day), Fargate is more economical and predictable.

**Q. How would you design the file-upload flow for receipts, knowing the mobile app can't store AWS credentials?**

Pre-signed URLs. Backend exposes a `/receipt-upload-url` endpoint that (1) validates the user is authenticated, (2) generates a time-limited pre-signed URL from AWS SDK, (3) returns the URL to the mobile app. The mobile app then PUTs the receipt PDF directly to S3 using that URL. After 1 hour, the URL expires and becomes useless. This way: AWS credentials never touch the mobile app, the backend isn't a bottleneck for the upload, and S3 handles the heavy lifting. I've done similar patterns with Firebase Storage; AWS pre-signed URLs are the same concept.

**Q. What's the difference between Lambda and ECS/Fargate? When would you use Lambda?**

Lambda is for short-lived, event-driven work. Use it for: webhooks (respond to GitHub pushes), background jobs (process receipts after S3 upload, under 15 minutes), scheduled tasks (cron jobs like cleanup). ECS/Fargate is for long-running services — your main API server that's always available. Lambda has a hard 15-minute timeout; if you need longer, you need Fargate. Lambda is billed per 100ms of execution; Fargate is billed per second of running time. At Glory, I'd use Lambda for async receipt processing triggered by S3 events, and Fargate for the always-on API.

**Q. You mentioned ISO 27001 experience but no OWASP hands-on testing. How does that affect your security approach?**

ISO 27001 is governance and risk management — access control policies, incident response plans, data classification. OWASP is application-level security testing — SQL injection, XSS, broken auth. They're complementary, not competitive. My ISO 27001 background means I think about risk, least-privilege access, and incident response. I haven't done formal penetration testing with Burp Suite or OWASP ZAP, but I apply the top 10 in code review: parameterized queries (no SQL injection), use managed auth like Cognito (no broken auth), escape user input (no XSS), validate IAM policies (no misconfiguration). I'd pair with your security team for threat-modeling sessions and penetration testing.

**Q. You haven't used NestJS, but the team uses it. How would you ramp up?**

I've built Node.js APIs with Express and HapiJS, so I understand routing, middleware, error handling, TypeScript, async patterns. NestJS is a structured framework on top of Express that enforces dependency injection and controller/service separation. I'd start with the NestJS tutorial (2-3 hours), then do code reviews with the team in the first sprint. My Express experience means I understand what NestJS is *doing* under the hood; it's just more opinionated. I'd be productive within the first week.

**Q. Walk us through the architecture of a cash-handling app at scale: 100K users, global deployment.**

First sprint: single region (ap-southeast-1), multi-AZ RDS for automatic failover, ECS/Fargate for the API (2-3 tasks behind an ALB), S3 for receipts. API Gateway sits in front, handles CORS and rate limiting. Cognito handles user auth; mobile app gets a JWT token. Mobile app uploads receipts via pre-signed URLs directly to S3. S3 triggers Lambda on new uploads; Lambda processes and updates RDS. CloudWatch logs and metrics go to the ops team. Cost: ~$300/month. At 10M users, we'd shard the database, add read replicas, and consider multi-region failover. But we'd build for single-region first and add complexity when data says we need it.

**Q. What would you do if production RDS goes down?**

If it's a multi-AZ RDS setup: AWS automatically fails over to the standby in another availability zone within 1-2 minutes. The mobile app would see a brief blip in latency or a connection timeout, then recover. If it's not multi-AZ: the app is down until we restore from a snapshot (minutes to hours). I'd ensure multi-AZ is enabled from day one — it's ~$0.50/hour overhead and saves the company from a production outage. Long-term: read replicas in other regions for analytics queries, so the primary focus on writes.

**Q. How do you handle secrets like database passwords and API keys in a production deployment?**

AWS Secrets Manager. The password is stored encrypted; my ECS task has an IAM role that allows it to read Secrets Manager. At startup, the task fetches the password, connects to RDS, then never logs it. If the password needs to rotate: Secrets Manager does it automatically (monthly by default), and Lambda hooks update the RDS master password without downtime. The mobile app doesn't need the password; it talks to the backend via HTTPS, and the backend holds the secrets. I'd never commit a password to git or set it in a Dockerfile.

**Q. Describe a recent project where you integrated a mobile app with a backend. What was your role?**

[This is about TalentAxis or Space360.] I built the React Native mobile app and worked with the backend team. I didn't write the Django/FastAPI services, but I owned the client-side logic: state management with Redux/Zustand, API integration (OAuth 2.0 login, REST calls), handling network timeouts and retries, local caching with React Query. I debugged integration issues — e.g., a backend token-refresh bug that broke OAuth flow; I isolated it with a curl matrix, reported it, and worked with the backend to fix it. That's the kind of collaboration I'd bring to Glory: not siloing mobile from backend, but owning the seams.

**Q. What's your approach to mobile app performance and monitoring?**

On the mobile side: React Native Testing Library for unit tests, network throttling in the simulator to catch latency issues early, lazy-loading screens to avoid a big bundle. On the backend: CloudWatch metrics for API latency and error rates, CloudWatch logs for debugging, CloudWatch alarms if error rate spikes (page on-call engineer). I'd also use a tool like Sentry (or New Relic) to track crashes on the mobile app, so we catch bugs users find before the team does. In production: monitor not just the happy path, but the 99th-percentile latency — that's where users feel pain.

**Q. Tell us about your mentoring experience. How would you help junior engineers ramp up on cloud-native development?**

[He was L&D at Enouvo, coached colleagues to PSM II, mentored via code review.] I'd do it the way I learned: hands-on code review, pair programming, and the occasional whiteboard session. I'd start a junior with a small Lambda function (easier to understand than ECS) to learn the deployment flow, then move to ECS. For cloud-native concepts, I'd relate them to what they already know — 'Fargate is like Heroku but with more control; RDS is like the PostgreSQL you've used locally but AWS handles the backups.' I'd document common patterns in a wiki so the knowledge stays in the team, not in my head. And I'd celebrate wins — shipping a feature to AWS production for the first time is a big deal.


### OAuth 2.0, OIDC, Certificate Security & OWASP — Mobile Engineer Interview Prep

**Q. Walk us through your OAuth 2.0 implementation. Why did you choose Authorization Code + PKCE over Implicit or Password grant?**

Authorization Code + PKCE is the modern standard for mobile native apps (iOS/Android and React Native). It's secure because the authorization code is never exposed to the JavaScript layer—the redirect happens natively. PKCE binds the code to the device via a code_verifier that only the app knows, so if an attacker intercepts the code, they can't exchange it without the verifier. Implicit is deprecated because tokens appear in the URL fragment (easily leakable). Password grant exposes the user's credentials to the app, which we don't want. For a cash-handling machine company, the extra security is critical.

**Q. How do you store tokens on mobile? Why not AsyncStorage?**

I store access and refresh tokens in Keychain (iOS) or Keystore (Android), not AsyncStorage. AsyncStorage is unencrypted and readable by any app on a compromised device. Keychain/Keystore provide device-level encryption and are resistant to tampering. I use `react-native-keychain` or `expo-secure-store` to abstract the platform differences. If I see tokens in AsyncStorage in a codebase, I flag it as a critical bug.

**Q. What's the difference between an access token and a refresh token? How do you handle refresh-token rotation?**

Access tokens are short-lived (5–15 min) and used to authenticate API requests. Refresh tokens are longer-lived (days to months) and used only to obtain a new access token when the old one expires. I implement rotation: on every refresh, the server issues a new refresh token and invalidates the old one. This way, if a token is stolen, it's only valid for one exchange—after that, it's useless. Optionally, I implement reuse detection: if the client submits an old token again, it indicates the token was leaked and used by an attacker, so I revoke the entire session and force re-login.

**Q. Explain JWT validation. What happens if you skip validation or if the algorithm is set to 'none'?**

A JWT has three parts: header, payload (claims), signature. To validate: (1) Fetch the Authorization Server's public key from JWKS (using the 'kid' in the JWT header). (2) Verify the signature using RS256 (or the server's algorithm). (3) Check the claims: iss (issuer), aud (audience, must match my client ID), exp (expiration), nonce (if OIDC). If you skip validation, you're trusting untrusted data. If the algorithm is 'none' or you don't check it, an attacker can forge a token. I always whitelist `algorithms: ['RS256']` and reject 'none' and 'HS256' (which would require a shared secret I don't have).

**Q. What is OIDC and how does it differ from OAuth 2.0?**

OAuth 2.0 is authorization (does this user have permission to access resource X?). OIDC is authentication + identity—who is this user? OIDC is a thin layer on top of OAuth: it adds an ID token (a JWT with claims about the user), a UserInfo endpoint, and a discovery document (listing all the endpoints). The ID token is signed by the Authorization Server and contains claims like 'sub' (user ID), 'name', 'email', 'nonce' (replay protection). With OAuth alone, you can get an access token but don't know who the user is. With OIDC, you get both.

**Q. You mentioned investigating an OAuth refresh-token flow that was broken. What was the problem and how did you fix it?**

We were using HttpOnly cookies for session tokens. The problem: React Native's Fetch doesn't automatically track cookies like a browser does. I built a curl test matrix to replicate the RN client's requests and discovered the auth server was issuing a 5-minute session cookie, but the RN client wasn't refreshing it in time. We switched to bearer tokens: short-lived access token (15 min) + longer-lived refresh token (7 days) stored in Keychain. Every refresh issues a new refresh token (rotation), so if an attacker steals a token, it's only good for one use. This eliminated the cookie complexity and aligned with OAuth 2.0 mobile best practices. Session handling is now auditable and secure.

**Q. What's certificate pinning and why does GLORY care about it?**

Certificate pinning means the app trusts only specific certificates, not all CA-signed certs. For a cash-handling machine, each device has a certificate issued by GLORY. The backend pins that certificate, so even if an attacker intercepts HTTPS traffic with a valid CA-signed cert, the pin check fails and they can't communicate. It's an extra layer: normal TLS validates the domain; pinning validates that it's GLORY's specific cert. The operational risk: if the cert expires and you don't update the app fast enough, users are blocked. Mitigation: pin multiple certs (current + next rotation), communicate with ops on rotation schedules.

**Q. You have ISO/IEC 27001 training. How does that complement application security (OWASP)?**

ISO 27001 is governance and risk management—how to run an ISMS (set policy, audit access, log incidents, manage third-party risk). OWASP is tactical—specific attacks on code (SQL injection, XSS, insecure storage). My ISO training teaches me to ask: Is sensitive data classified? Is access logged? Can we detect a breach? Those questions inform code review. But I'm not a penetration tester. For a formal OWASP security audit, GLORY would want a dedicated security engineer. My role is applying both lenses: think about data sensitivity and audit trails (ISMS), AND avoid AsyncStorage for tokens and validate JWTs (OWASP).

**Q. What are the top security risks for React Native apps? How do you mitigate them?**

Top risks from OWASP Mobile Top 10: (1) Insecure data storage—tokens in AsyncStorage or unencrypted. Mitigation: Keychain/Keystore. (2) Insecure communication—HTTP or TLS without validation. Mitigation: HTTPS TLS 1.3, certificate pinning. (3) Insecure authentication—weak token validation, no rotation. Mitigation: JWT signature/aud/iss/exp checks, refresh-token rotation. (4) Insufficient cryptography—home-rolled encryption. Mitigation: native Keychain/Keystore. (5) Insecure authorization—permissions checked on the client. Mitigation: all auth decisions on the backend; client-side checks are UX only. (6) Hardcoded secrets—API keys in JS bundle. Mitigation: minify/obfuscate, never embed secrets, load from secure backend. (7) Reverse engineering—attackers decompile the app. Mitigation: obfuscate, remove source maps in prod.

**Q. NestJS is mentioned in the JD but you have Express/HapiJS experience. How would you approach learning NestJS?**

Express and HapiJS taught me routing, middleware, RESTful API design, and JWT validation. NestJS is a TypeScript framework built on top of Express (or Fastify). The core concepts—decorators (@Controller, @Get), dependency injection, middleware—are familiar from Express. The learning curve is TypeScript syntax and NestJS patterns (decorators, modules, services). I'd study the NestJS docs, build a few test projects, and review GLORY's codebase. Given my Express foundation and TypeScript fluency, I'm confident I could be productive on a NestJS project within a few weeks.

**Q. You don't have AWS or serverless experience. How would you approach that gap?**

I've worked with adjacent services: Supabase (managed PostgreSQL), Firebase (managed auth/database), Heroku (managed containers), LocalStack (local AWS emulation). I understand cloud concepts—databases, functions, networking. I haven't deployed a production serverless Lambda or built cloud-native infrastructure from scratch. I'd be learning on the job, but I'm comfortable with that. I'd study AWS documentation, work through tutorials, and pair with GLORY's cloud team on real projects. Given the role includes mentoring and architecture discussions, I'd want to understand GLORY's current cloud setup and ask questions to learn.


### React Native + Expo: Senior Architecture & Performance Deep Dive

**Q. What's the difference between the old React Native bridge and JSI? Why does it matter?**

The old bridge serialized every JS-to-native call to JSON, crossing a separate thread boundary, which was slow and synchronous. JSI gives direct memory pointers between JS and native via C++, so calls are fast and can be synchronous. This enables high-frequency updates (scroll events, animations) to run on the native UI thread without blocking JS. Reanimated 2 uses JSI to run worklets directly on the UI thread, so animations are smooth even when JS is busy.

**Q. What's Fabric? How does it change rendering?**

Fabric is a new C++ rendering engine that RN talks to via JSI, not the old serializing bridge. Instead of the UIManager sending style diffs across the bridge, Fabric builds a committed shadow tree on the JS thread, then pushes a diff to the UI thread. This is faster, enables concurrent rendering, and means animations don't drop frames when JS is computing. Fabric is opt-in as of RN 0.76; not all third-party libraries support it yet, but core components are stable.

**Q. How do TurboModules and Codegen work? What's the workflow?**

You write a TypeScript Spec defining your native module's API (methods, parameter types, return types). Codegen (part of the RN build) reads the Spec and generates platform-specific boilerplate (Java/Kotlin for Android, Objective-C++ for iOS) that links the Spec to your native code. You implement the native side; the generated code handles JSI serialization and type checking. No more manual @ReactMethod annotations or serialization. The build runs Codegen automatically.

**Q. Explain Expo Prebuild and Continuous Native Generation. Why is the old 'Managed vs Bare' distinction obsolete?**

Prebuild generates the native android/ and ios/ folders from your config (app.json, config plugins) on EAS servers, producing a signed APK/IPA. CNG does the same but the generated code is ephemeral — you don't commit it; the config is the source of truth. Both approaches use the same tooling and codebase now. The old Managed/Bare split (Expo hosts builds vs you own native folders) doesn't matter anymore because config plugins let you customize native code without forking.

**Q. We have a large list (3000+ items) that users scroll through frequently. FlatList or FlashList?**

FlashList. For lists >1000 items, FlashList's more aggressive virtualization and autosizing for variable-height items gives smoother scrolling. FlatList works for small-to-medium lists. FlashList is not in RN core, but Expo has a config plugin to add it. Trade-off: you manage FlashList as a separate dependency, but the performance gain is worth it for large lists.

**Q. Your app has a form that saves data to the backend. User goes offline, posts the form, comes back online. How do you handle it?**

Optimistically update the UI immediately (show the new data as if it posted), then queue the mutation for retry. When connectivity returns, React Query retries automatically (refetchOnReconnect: true). If the retry fails, show a retry button in the UI. For critical data (payments), you'd also want a persistent queue (AsyncStorage or SQLite) so the data survives app restart.

**Q. When would you use a TurboModule vs. a React Native library from npm?**

First, check if an Expo plugin or npm library already exists (e.g., expo-camera, expo-audio). Only write a TurboModule if: (1) it's performance-critical or real-time (e.g., custom audio processing), (2) it needs hardware access not exposed by existing libraries, or (3) you've confirmed no existing solution fits. Most integrations (payments, analytics, ads) have off-the-shelf libraries. Custom TurboModules are the exception.

**Q. You're ready to push an update to production. Bug in the backend affecting some users. Do you push an OTA update or wait for store review?**

If the bug is in your JavaScript code (validation, display logic), push an OTA update immediately (~15 min to users). If it requires new permissions, new native code, or an Expo SDK version bump, go through store review (48 hours). For critical bugs (users can't log in), OTA is justified. Always have a rollback plan — EAS lets you roll back an OTA update in minutes, but there's a gap where some users see the buggy version.

**Q. What's runtimeVersion? Why does it matter for OTA updates?**

runtimeVersion is a label (e.g., '1.0.0') that groups app versions that can accept the same OTA updates. When you upgrade Expo SDK or a native dependency, you bump runtimeVersion and rebuild. Old apps with a different runtimeVersion don't download the new OTA update, so they don't break. Example: App v1 has runtimeVersion '1.0.0'. You push 5 JS fixes as OTA updates. You then upgrade Expo SDK and bump runtimeVersion to '1.1.0', releasing a new build. Only the new build gets '1.1.0' OTA updates; old app versions stay on '1.0.0' updates.

**Q. Your team uses Redux for both server state and UI state. You're seeing a lot of boilerplate (actions, reducers, selectors). What's the modern alternative?**

Separate concerns: React Query for server state (automatic caching, invalidation, sync), Zustand for client state (lightweight, minimal boilerplate). Example: user profile comes from React Query (useQuery), form UI state comes from Zustand (useStore). Redux is overkill unless you have deeply nested state mutations or legacy constraints. React Query + Zustand is much lighter and easier to reason about.

**Q. Your app startup is slow (>4 sec on Android). What's the first thing you'd measure?**

Use Xcode Instruments (iOS) or Android Studio Profiler (Android) to see where the time is spent: JS parsing, requiring modules, or rendering the first screen. Common wins: (1) Hermes bytecode (50% faster on Android if not already enabled), (2) lazy require (don't load heavy modules upfront), (3) code-split the first screen, (4) async initialization of expensive services. Profile first; optimization is pointless without data.

**Q. Reanimated worklets: what are they, and why do you need them?**

A worklet is a function marked with the `worklet` directive that runs on the native UI thread via JSI, not on the JS thread. Why: JavaScript is single-threaded; if JS is busy (computing, fetching data), animations stutter. Worklets run on the UI thread independently, so animations stay smooth. Example: scroll position changing updates a scale transform via a worklet; no bridge crossing, no frame drop even if JS is busy.

**Q. Config plugins: what are they, and when would you write one?**

Config plugins are JavaScript functions that run during Expo prebuild and modify the native configuration (AndroidManifest.xml, Info.plist) before compilation. When: you need native setup (permissions, library initialization) that isn't covered by existing plugins. Example: you're integrating a custom SDK that requires specific manifest entries. Instead of managing android/ and ios/ manually, write a plugin that adds those entries automatically.

**Q. You need to test a component that integrates with the backend. How do you approach it?**

Use React Native Testing Library to render the component and test behavior (form submission, error display) against a mocked API. Don't hit the real backend in tests. Example: mock the fetch call, trigger user interactions (fireEvent.changeText, fireEvent.press), and assert that the UI updates correctly. For critical flows, add an E2E test that hits the real backend in a staging environment.

**Q. Deep link to a specific order in your app. The app is killed (not in memory). What should happen?**

Expo Router reconstructs the navigation stack from the deep link. Example: deep link myapp://order/123 → routes to the orders/[id] screen with params { id: '123' }. The screen loads the order data (from cache or fetch). This works because Expo Router's file-based routing is agnostic to whether the app is in memory or cold-started; the route structure is static.


### Mobile Engineer Interview Prep: PostgreSQL, Docker, CI/CD, Monitoring (GSV Job)

**Q. Tell us about your PostgreSQL experience. How would you optimize a slow query?**

I've designed schemas for the Space360 app with users, properties, and bookings tables; used SERIAL keys, foreign keys with ON DELETE CASCADE, and check constraints. For slow queries, I run EXPLAIN ANALYZE to see if indexes are being used and where the planner estimate is wrong. A typical fix: if a WHERE clause on created_at isn't using an index, I create `CREATE INDEX idx_users_created ON users(created_at);` Cache hit rate matters too — I check Postgres stats. I understand the N+1 problem from my app code: instead of querying bookings for each user in a loop, I use a single JOIN with GROUP BY to let the database do it efficiently.

**Q. Explain Docker container images and multi-stage builds. Why do they matter in a CI/CD pipeline?**

A Docker image is a blueprint (like a class); a container is a running instance. Layer caching is crucial: I order Dockerfile from least-changing to most-changing — dependencies first, source code last — so changes don't invalidate the cache. Multi-stage builds separate build and runtime: the builder stage compiles TypeScript; the runtime stage copies only the compiled output, reducing final image from 500MB to 150MB. Smaller images deploy faster and consume less disk. In a pipeline, smaller images mean quicker builds and pulls to production.

**Q. You have Express.js experience but the role requires NestJS. How would you approach that?**

I haven't used NestJS specifically, but I've built RESTful APIs with Express and HapiJS — routing, middleware, error handling. NestJS is a TypeScript framework built on Express, so HTTP fundamentals are the same. I'd expect to learn NestJS quickly by reading the docs and working through tutorials. The new concepts would be dependency injection, decorators, and NestJS modules — standard patterns in mature frameworks. I'm comfortable picking up new frameworks fast because I understand the underlying principles.

**Q. Walk me through how you'd debug a production incident where the mobile app crashes for users in Vietnam but not in the US.**

First, I'd check Sentry for crash reports: spike timing, affected versions, stack traces. If minified, I'd upload source maps to see real line numbers. Second, I'd search logs using the user's correlation ID to trace their request flow. Third, I'd check metrics: did API latency spike or error rate increase at the time? Fourth, I'd check if a feature flag was changed or a new version deployed — if so, I'd flip the flag off or rollback the app. Fifth, I'd check the backend: database connection pool exhausted? Slow queries? Sixth, I'd check cloud infrastructure: is Vietnam in a different region? Is there network latency? Once I've narrowed the layer, I'd reproduce locally with the same data and debug systematically.

**Q. Describe your experience with CI/CD pipelines. What tools have you used?**

I've used Jenkins for continuous integration: tests run on every commit, then SonarQube scans for code quality and security issues. If coverage drops or a security issue is found, the pipeline fails and we can't merge. For mobile (Expo), I use EAS Build to compile iOS and Android binaries in the cloud; EAS Submit queues them for App Store and Play Store review. I've managed releases by tagging commits, triggering builds, and monitoring deployments. I haven't set up GitHub Actions, but I'm familiar with the concept: YAML workflows that automate testing and deployment.

**Q. What's your experience with cloud platforms like AWS or GCP?**

I don't have production experience deploying to AWS or GCP. I've used LocalStack to emulate AWS services locally (SQS, DynamoDB), and I've used Supabase as a managed Postgres service. I understand serverless concepts: Lambda functions are stateless and scale automatically, but connection pooling to databases is tricky — AWS RDS Proxy solves it. I'd be confident setting up a cloud-native stack with good documentation and mentoring. My security training included AWS architecture patterns, so I'm familiar with the concepts even if I haven't deployed at scale.

**Q. Explain the difference between logs, metrics, and traces. Why do we need all three?**

Logs are event records (text): 'User 123 booked property 456.' Metrics are numeric aggregates: 'API response time 250ms average.' Traces show the full request flow: 'Mobile → API (200ms) → Postgres (50ms) + Redis (10ms).' You need all three because logs tell you what happened, metrics tell you how often and how fast, and traces show where time is spent. If the API response time is slow, metrics alert you; traces show you it's the database query taking 50ms. Without traces, you're debugging blind.

**Q. How would you use structured logging and correlation IDs to debug a multi-service system?**

Instead of `console.log('User booked')`, I use structured JSON: `logger.info('booking_created', { user_id: 123, property_id: 456, request_id: uuid-abc })`. The request_id (correlation ID) flows through every service: mobile → API → database. When a user reports a problem, I search logs for their correlation ID and see the entire request flow: where it succeeded, where it failed. Without correlation IDs, logs from different services are disconnected. With them, I can trace one user's request through all layers and pinpoint the failure exactly.

**Q. Tell us about your security background. Have you worked with OWASP or OAuth?**

I've implemented OAuth 2.0 social login on TalentAxis — Facebook, Google, GitHub — with JWT tokens and refresh flows. I've also debugged a production issue in the refresh-token flow delivered over HttpOnly cookies — I built a curl test matrix to isolate the root cause. My security training is ISO/IEC 27001 ISMS (governance and management systems), not OWASP application testing. I know OWASP Top 10 conceptually — injection, broken auth, XSS — but I haven't done hands-on security audits. I'd study OWASP methodology to conduct application security reviews.


### GLORY Software Vietnam: Mobile Engineer Interview Study Guide

**Q. Walk us through your most complex React Native project. What were the challenges?**

I built the TalentAxis recruitment app — a React Native client that recruiters and candidates use to track job matches and interviews. The complexity was integrating with a microservices backend: Django user service, FastAPI matching service, Celery async queue, and real-time notifications. The hardest part was handling network resilience — if the backend is slow or offline, the app queues actions locally and syncs when connection returns. I used Redux for state, React Query for server-state caching, and a sync engine persisting to AsyncStorage. I also debugged an OAuth refresh-token issue where tokens expired mid-session — I built a curl test matrix to isolate whether it was client-side or backend, and found the backend wasn't rotating refresh tokens properly. That taught me the importance of end-to-end auth testing.

**Q. You've used Express and HapiJS, but the role requires NestJS. How would you approach learning it?**

I'd start with the NestJS documentation to understand the module system — it's different from Express's flat middleware setup. Key concepts are Modules, Controllers, Services, and Dependency Injection. I'd build a small CRUD API (e.g., a Device entity) to get hands-on with decorators and routing. Then I'd map NestJS patterns to what I already know: a Controller is like an Express route handler, a Service is business logic, and a Guard/Pipe is middleware with a cleaner API. I've already read the docs as prep, so I'm confident I can ramp up in the first week or two on the job.

**Q. How would you design the backend API for a mobile app collecting telemetry from 10,000 cash recyclers?**

I'd use an event-driven architecture. Each device sends telemetry to an API endpoint, but instead of writing directly to the database, the API puts the message on a queue (SQS or RabbitMQ). A backend worker processes the queue asynchronously, writing to a time-series database like InfluxDB for fast queries and PostgreSQL for relational data. I'd implement a circuit breaker on the API — if the database is overloaded, the API queues the request and returns success to the device. This prevents device timeouts. On the mobile side, I'd implement polling with exponential backoff: start at 30 seconds, if we get a 5xx, back off to 1 minute, then 2 minutes. If we get 2xx, reset to 30 seconds. This reduces load during outages and caches responses with React Query.

**Q. Tell us about your experience with authentication and security — OAuth, JWT, etc.**

I've implemented OAuth 2.0 social login (Google, Facebook) where the app delegates authentication to a third party. The flow is: user taps 'Login with Google', the app opens a web view, Google authenticates and returns an auth code, the app sends the code to my backend, the backend exchanges it for tokens, and we store the access token in AsyncStorage using HttpOnly cookies for session management — the cookie is only sent over HTTPS and is inaccessible to JavaScript, preventing XSS theft. I implemented refresh-token rotation: when the access token expires, the client sends a refresh token, the backend validates it, revokes the old refresh token, and issues a new pair. I once debugged a production issue where tokens were expiring mid-session. I built a curl test matrix to isolate the problem and found the backend was issuing short-lived tokens without proper refresh-token rotation. For mTLS and OIDC, I haven't built these yet, but I understand the PKI model and the identity-layer concepts. I'm ready to learn.

**Q. You've worked with PostgreSQL, DynamoDB, and Elasticsearch. How would you choose which one for a given problem?**

It depends on access patterns and consistency requirements. PostgreSQL is best for relational data with strong consistency — user accounts, permissions, audit logs. You need ACID guarantees and complex queries (JOINs, aggregations). DynamoDB is good for high-throughput, eventually-consistent data — device telemetry, user sessions. You're doing simple lookups (device ID → latest status), not complex queries. Elasticsearch is good for full-text search and time-series analysis — searching device error logs, finding patterns in telemetry. For cash-handling, I'd use PostgreSQL for core financial data (reconciliation logs, device inventory, user access), DynamoDB for real-time device status (fast writes from 10,000 devices), and Elasticsearch for searching error logs.

**Q. You don't have AWS or GCP production experience. How would you ramp up quickly?**

Honestly, I haven't shipped production code on AWS Lambda or Google Cloud Functions. I have adjacent experience — Firebase, Heroku, Supabase. But I understand the conceptual model: a function responds to an event, you pay per invocation, state is ephemeral. I learn by doing, so I'd want to start with a small project — maybe a scheduled Lambda for device alerts or a background worker for reconciliation jobs. I'd pair with the backend team to understand naming conventions and IAM. I'd read the AWS docs and possibly take a hands-on course. This isn't a blocker — it's a tool I haven't used, but the fundamentals (event-driven architecture, cloud deployment) are ones I understand.

**Q. Tell us about a time you mentored a junior engineer or helped them solve a problem.**

At Enouvo, I was an L&D Executive and coached engineers. One junior was stuck on Redux state management — the component wasn't re-rendering when the store updated. Instead of giving him the answer, I asked him to trace through the Redux flow: action → reducer → store update → component selector. He realized he wasn't using useSelector correctly — he was reading the whole store object instead of selecting a slice. Once he saw the problem, he fixed it. I documented this pattern in the team's technical manual so others wouldn't repeat the mistake. I think the best mentoring is teaching someone to debug, not just giving them the answer. I also coached a colleague to PSM II certification — we studied together and he passed.

**Q. Describe a time you disagreed with a technical decision. How did you handle it?**

At TalentAxis, the team wanted to use Redux for state management, but I thought Zustand would be simpler for our use case — we didn't need the middleware ecosystem, just simple state-sharing between components. I wrote a one-page comparison: Redux (pros: predictable, time-travel debugging; cons: boilerplate, learning curve) vs. Zustand (pros: minimal API, less code; cons: fewer tools for complex scenarios). I presented it in a team sync and we discussed trade-offs. The team decided to stick with Redux because they were already comfortable with it and wanted consistency. I aligned with that decision — it's not my decision alone. But because I'd written it down, we had a clear record. If we hit performance issues later, we'd know why we chose Redux. That's how I see good technical decision-making — proposal, discussion, alignment, documentation.

**Q. Why are you interested in cash-handling systems and working with Japanese teams?**

I'm attracted to the reliability and compliance aspects. Cash-handling is a domain where downtime has real consequences — a bank can't process deposits, a retail chain can't reconcile cash. Software has to be rock-solid, auditable, and secure. It's different from a consumer app where you can iterate fast. I've worked in regulated environments before — my ISO 27001 training — so I understand the compliance mindset. I'm also interested in working with Japanese teams. Japan has a reputation for quality and long-term thinking. This role is an opportunity to learn that mindset and bring it back to Vietnam. And technically, integrating a mobile app with complex backend systems, handling offline scenarios, and managing 10,000 devices in the field is substantial work that excites me.

**Q. How do you stay current with technology? What have you learned recently?**

I use Claude Code daily for my work — it's changed how I approach mobile development. I read documentation for libraries I'm using and follow Expo's releases closely since we deploy via Expo Submit. I've been reading about LLM applications and how to structure prompts for reliable outputs. I also read architectural articles on Hacker News and CSS-Tricks. I don't chase every new framework, but I stay aware of ecosystem shifts. For this role specifically, I've been reading NestJS and AWS Lambda because the JD listed them. I also watch internal tech talks where backend engineers share patterns. Learning is continuous — you can't know everything, but you have to know how to learn.

**Q. In a team coordinating with Japan, how would you handle time zone differences and communication challenges?**

I understand the overlap is only 2 hours between Vietnam (UTC+7) and Japan (UTC+9). I'd make those hours count by preparing an agenda beforehand — no surprise discussions. I'd write clear summaries of issues or decisions and send them before the meeting so the Japan team has time to review. For async communication, I'd document decisions in writing — not just Slack mentions. I'd respect the fixed 8:00-17:00 hours — that signals they value work-life balance. I've worked in remote teams before, so I know the discipline of written communication and meeting preparation matters. I'd also make an effort to understand Japanese work culture — punctuality, thorough documentation, consensus-building. Those aren't just nice-to-haves; they're the foundation of how we'd work together.

**Q. What would you do if you discovered a security vulnerability in production code — something that could expose device credentials?**

First, I'd isolate the issue: reproduce it locally, document the exact conditions, and estimate the impact (how many devices affected? what data is exposed?). Second, I'd escalate immediately to the tech lead and security team — not waiting for a meeting, pulling them in Slack or phone if needed. Third, I'd work with them to decide: do we patch and deploy urgently, or do we take it down temporarily? In the cash-handling domain, both are bad, but one might be less bad. Fourth, I'd help prepare the post-incident report: what happened, why, how we fix it, how we prevent it in the future. Fifth, I'd document the finding — add a test case or a code comment to prevent the same mistake later. In an auditable domain like this, transparency and speed are critical.

**Q. Tell us about your ISO 27001 training. How is that relevant to this role?**

ISO 27001 is an Information Security Management System framework. It teaches governance, risk assessment, controls, and compliance architecture — not just technical security. My training covered how to design systems that satisfy regulatory auditors, how to document risk, and what non-repudiation means (every action must be provable and immutable). OWASP, on the other hand, is application-level security testing (injection, XSS, broken auth). Both are needed in regulated domains like cash-handling. My ISO 27001 background gives me the governance layer — how to structure systems for auditability and compliance. OWASP is the technical layer — the specific attack vectors I need to prevent. I don't have formal OWASP hands-on practice yet, but I understand it's about identifying those vulnerabilities in code. I've been reading OWASP Top 10 guides and I'm ready to deepen that knowledge.


---

## §4 — Your real anchors, mapped to their JD bullets

Rehearse these three until they come out in 60 seconds each. Between them they cover most of the JD.

| Your anchor | The JD bullets it answers |
|---|---|
| ⭐ **The OAuth refresh-token / HttpOnly-cookie investigation** — built a request test matrix by hand, changed one variable at a time, eliminated causes until one root cause remained | *"Troubleshoot production issues across mobile, backend, and cloud infrastructure"* · *"Knowledge of authentication and authorization protocols such as OAuth 2.0..."* · *"Ensure application performance, reliability, security"* |
| ⭐ **Release engineering** — EAS Build/Submit, store submissions and review responses, staged rollout, OTA via Stallion, plus setting up the Apple/Google developer accounts and the company D-U-N-S registration | *"Implement best practices for testing, CI/CD, monitoring, and release management"* · *"Design, build, and maintain high-quality mobile applications using React Native and Expo"* |
| ⭐ **Standards & mentoring** — introduced Agile delivery, wrote the methodology manuals the team worked from, ran the internship program, coached a colleague to PSM II, mentored juniors through code review | *"Mentor engineers through code reviews, technical guidance, and knowledge sharing"* · *"Help establish engineering standards and contribute to scaling the mobile engineering team"* |

**Plus, on demand:** the two shipped products (architecture, Expo, store links) for *"design, build, maintain"* and *"product-focused environment"*; the crash-reduction work from 2018–2020 for *"reliability"*; Jenkins/SonarQube for *"CI/CD and DevOps"*.

---

## §5 — Questions to ask them *(these are unusually good here — use them)*

**About the product — nobody else will ask these, and they reveal you did the homework:**
1. Who actually uses the mobile app — field service technicians maintaining the machines, retail back-office staff, cash-in-transit crews, or bank operations? *(Ask it as a question, not a guess.)*
2. Does the app talk to the machines directly — over Bluetooth, local network, or device certificates — or only to cloud services?
3. How do you handle release cadence and support lifetime for an app that ships alongside regulated financial hardware? I'd expect it to be far more conservative than consumer mobile.
4. Is there an offline requirement — do technicians work in places without connectivity?

**About the role and team:**
5. How is the mobile team structured today, and how large do you want it to become? *(Their JD mentions scaling it — this is your opening to talk about mentoring.)*
6. How much of this role is React Native versus contributing to the NestJS backend? What split do you actually expect in the first six months?
7. What does the interaction with the Japan-based teams look like day to day — written, or regular video calls?
8. Is there an onboarding or training path for the cloud side, given you sponsor professional development?
9. What does success look like for this role at six months?

**About engineering practice:**
10. What does your CI/CD and release pipeline look like for the mobile app today, and what would you want improved?
11. How do you approach testing on mobile — and what would you want the standard to be?

---

## §6 — Drill list *(rehearse out loud, in English, ~60–90s each)*

1. **"Tell me about yourself."** — 5 years, RN/Expo, two shipped products, currently leading mobile delivery, plus the mentoring/standards half. **In English. This is the one you cannot afford to fumble.**
2. **"Why do you want to leave your current company, and why us?"** — forward-looking: a stable product team, depth, mentoring, and the backend/cloud growth. *Never say "my company is going bankrupt"* — say it is restructuring and you're seeking long-term stability.
3. **"Walk me through the architecture of one of your apps."** — pick Space360 or TalentAxis; cover Expo Router, state management (server-state vs client-state), the API boundary, auth, release path.
4. **"Why Expo?"** — answer it to a skeptic: prebuild/CNG, config plugins, EAS, and what you'd do if you needed something Expo doesn't support.
5. **"What is the New Architecture and what does it change?"** — JSI, Fabric, TurboModules, Codegen, Hermes. ⚠️ **Default-on since RN 0.76** — get this right.
6. **The NestJS honesty answer** (§0B) — then demonstrate you understand DI, modules, DTOs, guards.
7. **The cloud honesty answer** — plus what "cloud-native" means and when serverless is wrong.
8. **The OAuth debugging story** — 60 seconds, structured: symptom → hypothesis → test matrix → root cause → fix.
9. **"How do you approach mentoring / code review?"** — your strongest differentiator. Use the internship program and the PSM II coaching.
10. **"How would you debug a production issue affecting only some users?"** — triage narrative across mobile, API, and infrastructure.
11. **The ISO 27001 vs OWASP distinction** (§2) — precise, not conflated.
12. **Your English self-assessment** (§0A) — honest, calm, and reference their sponsored classes.

---

*Bottom line: **this is the application to put your best hours into.** You clear their headline bar rather than reaching for it, you bring a mentoring-and-standards record that most mobile engineers simply don't have, and the employer is stable in exactly the way you said you needed. Three real gaps — NestJS, AWS/GCP, serverless — and the right move on all three is the same: **study the concepts, claim none of the experience, and make them the reason you want the job.** The thing most likely to decide it is not any of those gaps; it is **spoken English on a video call.** Prioritize accordingly: §1 says drill English and your own RN/Expo depth first, and if you only get two hours, do only those two.*

*One last honest word on sequencing: of your seven applications, this and the Đà Nẵng RN startup are the two where you are clearly the strong candidate rather than the hopeful one. **Send both, prep both hardest, and treat FPT Telecom and Lutech as the backstops they are.***
