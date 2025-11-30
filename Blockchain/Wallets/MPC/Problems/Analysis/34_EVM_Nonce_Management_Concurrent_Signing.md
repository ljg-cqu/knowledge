# EVM Nonce Management for Concurrent MPC Signing – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Blockchain Engineering Team

---

## Pre-Section: Context Recap

- **Problem title**: EVM nonce management for concurrent MPC signing sessions
- **Current state**:
  - Ethereum and EVM-compatible chains use a strictly increasing account nonce (starting from 0) to order transactions and prevent replay; transactions must be mined in nonce order, and gaps block later transactions [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].
  - In the current MPC wallet implementation, multiple frontend clients and backend services can initiate transactions in parallel (mobile, web, batch withdrawals, bots), each independently querying `eth_getTransactionCount` and assigning nonces optimistically, with only eventual consistency.
  - Under peak periods, this leads to 5–10% of concurrent transactions becoming stuck, unintentionally replaced, or failing with `nonce too low` errors, especially when retries and Replace-By-Fee (RBF) logic are layered on top of inconsistent nonce views [Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].
- **Pain points**:
  - **Nonce collisions**: Two different transactions are assigned the same nonce; the later one with higher effective gas price replaces the earlier one, leading to confusing UX (e.g., swap “disappears” and is replaced by a transfer) [Source: Wallet Nonce Management, Circle Developer Docs, 2025].
  - **Nonce gaps**: Transactions are submitted with nonce `N+2` before `N+1` has mined; all later transactions are blocked in the mempool until the missing nonce is resolved, causing stuck queues and support tickets [Source: Wallet Nonce Management, Circle Developer Docs, 2025].
  - **Incorrect RBF targeting**: Fee-bump flows sometimes reference the wrong nonce (e.g., bumping `N` while user intended to bump `N+1`), increasing confusion and wasting gas [Estimate based on: internal incident reviews and support tickets sampling, Medium confidence].
- **Goals**:
  - Reduce nonce-related failures from 5–10% of concurrent transactions to **<0.1% of all EVM submissions**, including during peak market volatility [Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].
  - Achieve **p95 nonce allocation latency <50 ms** per account, so centralized allocation does not materially increase end-to-end signing latency [Estimate based on: typical signing budgets of 100–300 ms; see also nonces/throughput discussion in QuickNode & Openfort docs, Medium confidence].
  - Support **≥10 concurrent signing sessions per account** without collisions or stuck queues, suitable for power traders and high-throughput backends.
  - Ensure RBF and cancellation flows reliably target the intended transaction/nonce with near-100% correctness.
- **Hard constraints**:
  - Must support **10+ EVM chains** (Ethereum, Polygon, Arbitrum, Optimism, Base, BSC, Avalanche, etc.) with heterogeneous RPC latency and mempool visibility [Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].
  - Limited to **1.5 FTE blockchain engineers for 2–3 months** and **$40k implementation budget + ~$2k/month infra** for the allocator service.
  - Allocator service must be **highly available (≈99.95%)**, stateful across restarts, and tolerate RPC variance and reorgs.
- **Key facts**:
  - Every Ethereum account maintains a single scalar nonce; transactions with reused nonces are rejected as `nonce too low`, and pending transactions can be replaced by sending another transaction with the **same nonce and higher gas fee** [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].
  - If a transaction with nonce `N` fails or is dropped and nonce `N+1` is already in the mempool, the account will be blocked until either `N` is successfully mined or explicitly replaced/canceled [Source: Wallet Nonce Management, Circle Developer Docs, 2025].
  - Modern smart-account stacks are starting to introduce **2D nonces** (nonce key + nonce value) to allow safe parallelization, but this is not yet widely available on EOAs and many MPC wallets still rely on one-dimensional nonces [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

1. **Core problem**  
   The MPC wallet platform allows multiple devices and backend services to initiate EVM transactions concurrently for the same account, while the underlying chains enforce a **single, strictly sequential nonce** per account. Without a centralized nonce allocator or per-account lock, concurrent clients compete for nonces using stale `eth_getTransactionCount` reads, leading to nonce collisions, gaps, stuck queues, and confusing RBF behavior [Source: Wallet Nonce Management, Circle Developer Docs, 2025; Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].

2. **Key contradictions**
   - **Concurrency vs. sequential semantics**: Product demands parallel signing from multiple devices and services (better UX and throughput), but the EVM nonce model is inherently **one-dimensional and sequential**, making naïve concurrency hazardous [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].
   - **Latency vs. coordination**: Users expect near-instant signing (sub‑second), yet safe nonce allocation normally requires a **single source of truth** and possibly extra round trips, which teams are reluctant to add for fear of latency regressions [Estimate based on: internal latency SLOs and QuickNode performance discussions, Medium confidence].
   - **Simplicity vs. robustness**: Simple “each client increments locally” designs are easy to ship but fragile at scale; robust designs (centralized allocator, locks, 2D nonces) increase architectural complexity and require cross-team changes [Source: Sending more than one transaction at a time is easy, right?, thirdweb Blog, 2023].

3. **Who is in conflict?**
   - **Wallet UX/product**: Favors seamless multi-device usage and parallel actions (“swap while sending a transfer”).
   - **Backend & infra teams**: Need deterministic, safe nonce allocation with strong invariants, often preferring single-writer queues and strict locking.
   - **Power users & partners**: Want maximum throughput and flexible automation from multiple services (bots, exchanges, treasury systems).

### 1.2 Goals and conditions

- **Reliability goal**: Achieve **<0.1% nonce-related failure rate** across all EVM chains, including collisions, gaps, and mis-targeted RBFs [Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].
- **Performance goal**: Keep **p95 nonce allocation latency <50 ms** and keep end-to-end signing latency within existing UX budgets (~<10 s perceived by users) [Estimate based on: current MPC signing pipeline metrics, Medium confidence].
- **Scalability goal**: Support at least **10 concurrent sessions per account** and thousands of accounts active at once without allocator hot spots.
- **Correctness goal**: Ensure nonce selection, RBF, and cancellation behavior are **fully deterministic and auditable**, with logs sufficient for post‑mortems.
- **Conditions/constraints**:
  - 1.5 FTE engineers; 2–3 month window; limited appetite for deep refactors of the existing MPC coordinator.
  - Must support **10+ heterogeneous EVM chains** and handle RPC differences in pending nonce semantics [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].

### 1.3 Extensibility and reframing

- **Reframing as a sequencing service**: Instead of seeing nonce handling as an incidental detail in each client, treat it as a **shared “transaction sequencing & nonce allocator service”** responsible for per-account ordering across chains [Source: Wallet Nonce Management, Circle Developer Docs, 2025].
- **Attribute reframing – one object, many attributes**:  
  The “object” is an account on a given chain; key attributes include: chain, address, current confirmed nonce, highest pending nonce, queue of planned operations, risk profile (retail vs. institutional), and allocation latency target. Optimizing these together yields better decisions than focusing solely on `currentNonce` [Estimate based on: internal architecture discussions, Medium confidence].
- **Scope reframing – towards 2D nonces**:  
  Even though EOAs use one-dimensional nonces today, smart accounts and 2D nonce models (nonce key + nonce value) show where the ecosystem is heading; designs should **not block future migration** toward 2D semantics for parallel flows [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **EVM nonce state**: Per-account scalar nonce, with confirmed, pending, and queued states that depend on both local node mempool and chain consensus [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].
- **MPC signing coordinator**: Orchestrates approval flows, collects partial signatures, and submits final signed transactions to RPC endpoints for multiple chains.
- **Nonce allocator (current)**: Distributed across clients; each client calls `eth_getTransactionCount`, computes `nonce = onChainNonce + k`, and submits, leading to races.
- **Future centralized allocator**: A stateful service backed by a durable store (e.g., Postgres or Redis with persistence) that owns per-account nonce assignment and may expose simple APIs like `allocateNonce(chain, account)` [Source: Wallet Nonce Management, Circle Developer Docs, 2025].
- **Retry & RBF logic**: Client libraries or backend tasks that resubmit transactions with higher gas or alternate parameters using the same nonce [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].

### 2.2 Balance and “degree” issues

- **Concurrency vs. safety**: Allowing unbounded concurrency per account increases the risk of collisions and gaps; a safe design imposes **controlled parallelism** (e.g., at most K in‑flight nonces per account, explicit state machine) [Estimate based on: throughput vs. failure trade-off modeling, Medium confidence].
- **Centralization vs. resilience**: A single global allocator simplifies invariants but introduces a new critical dependency; sharding by chain or region reduces blast radius but complicates global ordering.
- **Optimism vs. conservatism**: Purely optimistic off-chain tracking (incrementing in Redis without strong recovery logic) is fast but fragile; purely conservative designs (waiting for confirmations before issuing new nonces) sacrifice throughput unnecessarily [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].

### 2.3 Causal chains

1. **Collision chain**:  
   Two clients read the same on-chain nonce `N` concurrently → both propose transactions with nonce `N` → one transaction is eventually mined; the other is rejected or stuck as `nonce too low` → user perceives “random” failures and double-submission attempts [Source: Sending more than one transaction at a time is easy, right?, thirdweb Blog, 2023].

2. **Gap chain**:  
   Client A assigns nonce `N` but the transaction fails or is rejected; client B, unaware, assigns `N+1` and sends successfully → mempool now expects `N` before `N+1` executes → later transactions are queued until `N` is replaced or mined, effectively freezing the wallet [Source: Wallet Nonce Management, Circle Developer Docs, 2025].

3. **RBF confusion chain**:  
   User attempts to speed up a pending transaction by resubmitting with a higher gas price; due to stale local nonce views, the bump is sent for `N` while the user actually meant `N+1` → wrong transaction is replaced or an unrelated one is bumped, causing UX and reconciliation issues [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and conflicts

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | L1/L2 node operators, RPC providers | Stable nonce semantics, predictable mempool behavior, high availability | Need to serve many clients fairly, cannot special-case one wallet | Wallet desires for aggressive retries/RBF may conflict with RPC rate limits or mempool policies |
| Downstream | Exchanges, DeFi protocols, payment partners using the MPC wallet | Predictable settlement times, low rate of stuck or replaced transactions | Depend on our wallet’s sequencing; limited visibility into internal nonce logic | Suffer when nonce issues cause delayed deposits/withdrawals |
| Sideline / External | End users, support teams, compliance & risk | Simple mental model (“click sign, see tx mined”), low error rates, clear audit trails | Limited understanding of nonce mechanics; bound by regulatory and SLA expectations | Support load spikes and potential compliance incidents when nonce bugs cause large backlogs |

[Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].

### 3.2 Environmental factors

- **Market volatility**: Spikes in trading volume (10× normal) cause many concurrent signing sessions per account, amplifying race conditions and stressing RPC/mempool capacity [Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].
- **Multi-chain heterogeneity**: Different chains and providers expose pending nonces and mempool states differently, making it risky to rely solely on `eth_getTransactionCount(pending)` semantics [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].
- **Ecosystem shift towards smart accounts**: Account abstraction and 2D nonce mechanisms are gaining traction, which may create new expectations about parallelizability and could reduce pressure on EOAs over a 1–3 year horizon [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].

### 3.3 Responsibility and room for maneuver

- **Wallet provider (this team)**:
  - Owns design and operation of centralized nonce allocator and integration into MPC flows.
  - Can implement internal SLAs, observability, and safeguards (e.g., per-account queues, limits, admin override tools).
- **RPC providers**:
  - Provide reliable transaction count and mempool probes; can expose better observability APIs but cannot solve client-side coordination.
- **Partners & power users**:
  - Can adapt integration patterns (e.g., funnel transactions through recommended APIs rather than direct raw sends) and help validate concurrency behavior via staged pilots.

[Source: Wallet Nonce Management, Circle Developer Docs, 2025].

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **Early Ethereum wallets (pre‑MPC)**: Single-device EOAs with simple, sequential transaction flows rarely hit complex concurrency issues; nonce was usually hidden from users and managed locally by the wallet [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].
2. **Rise of backend wallets and bots**: Custodial and semi‑custodial services began submitting many automated transactions from the same address (exchanges, market makers), discovering that naïve parallel submission quickly triggers `nonce too low` and stuck queues [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].
3. **MPC wallet adoption**: Multi‑device and multi‑party MPC wallets added more concurrent actors (multiple devices per user, multiple services per organization) without always introducing a robust, centralized nonce allocator.
4. **Scaling to multi-chain, multi-region deployments**: As the product expanded to 10+ chains and multiple regions, the combination of higher latency, inconsistent mempool semantics, and more concurrent flows exacerbated nonce coordination issues [Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - The one-dimensional account nonce model was not originally designed with **highly parallel, multi-service automation** in mind, making concurrency a client-side concern [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].
  - Early wallet patterns normalized optimistic local nonce incrementation without strong centralization or locking.

- **Direct causes in current system**:
  - Multiple independent components (mobile app, web app, backend batch jobs) each compute nonces from RPC on their own, with no single source of truth.
  - The MPC coordinator lacks a dedicated per-account state machine and instead treats nonce selection as a thin pre-submission concern.
  - Error handling and RBF flows are implemented differently across clients and services, often with incomplete understanding of pending vs. queued states [Source: Wallet Nonce Management, Circle Developer Docs, 2025].

### 4.3 Root issues

- **Nonce management not treated as core infrastructure**: It is implicitly “everyone’s problem and no one’s ownership,” leading to duplicated, inconsistent logic.
- **Underestimation of concurrency complexity**: It is easy to reason about two transactions, but production systems regularly generate dozens of nearly simultaneous transactions per account.
- **Limited observability of nonce state transitions**: Logs and metrics focus on high-level errors rather than detailed per-account nonce timelines, making it hard to diagnose and fix systemic patterns.

[Estimate based on: internal incident analysis and industry case studies, Medium confidence].

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- As user base and integrated partners grow, concurrent transaction initiation per account will continue to increase, especially during market volatility windows.
- Nonce-related failure rates (5–10% for concurrent traffic today) will likely increase in absolute volume, leading to more stuck funds, delayed execution, and reputational risk [Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].
- Support ticket volume related to “stuck transactions” and “nonce too low” errors will remain high or grow, consuming support and engineering time.

### 5.2 Early signals

- External developer docs such as thirdweb’s concurrency article explicitly warn that simply relying on SDK-provided “next nonce” is unsafe when multiple backend processes send transactions concurrently [Source: Sending more than one transaction at a time is easy, right?, thirdweb Blog, 2023].
- Circle’s Wallet Nonce Management docs recommend centralizing nonce assignment and actively handling gaps and failed transactions, indicating that more mature providers treat nonce management as its own subsystem [Source: Wallet Nonce Management, Circle Developer Docs, 2025].
- Smart account platforms are investing in generalized 2D nonce schemes to solve structural limitations of one-dimensional nonces [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**:  
  Centralized nonce allocator is deployed across all EVM chains with strong observability and operational playbooks; nonce-related failure rate drops below **0.1%**, and support tickets fall by ≥70%. The design anticipates future adoption of 2D nonces for smart accounts.

- **Baseline scenario**:  
  Allocator is deployed but only partially integrated (e.g., some legacy services still bypass it). Nonce failures fall but remain noticeable during spikes (e.g., 0.5–1%). Technical debt accumulates in dual-path behavior.

- **Pessimistic scenario**:  
  Allocator is not fully implemented or is unreliable; teams introduce ad‑hoc fixes per service. During a period of extreme volatility, large volumes of transactions become stuck or mis-ordered, triggering partner complaints, potential legal exposure, and emergency patches.

[Estimate based on: prior incidents in wallet and exchange infrastructure, Medium confidence].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Strong blockchain engineering expertise**: The team already operates MPC signing infrastructure across many chains with tight latency budgets, indicating competence to design and maintain a nonce allocator [Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].
- **Existing observability stack**: There is already infrastructure for dashboards, logs, and alerts on transaction success rates, which can be extended to track nonce-level metrics.
- **Partner relationships**: Exchanges and institutional clients are accustomed to joint incident reviews and can provide feedback during rollout of new nonce semantics.

### 6.2 Capability gaps

- **Stateful multi-chain coordination**: Running a highly available, strongly consistent per-account state machine across regions and chains is non-trivial and not yet part of the core platform.
- **Nonce-centric analytics and tooling**: Current tools are ticket- and transaction-centric rather than nonce-centric; investigators lack simple ways to visualize account nonce timelines and queue state.
- **Knowledge diffusion**: Understanding of nonce, RBF, and mempool semantics is uneven across frontend, backend, and support teams, leading to inconsistent handling and miscommunication [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].

### 6.3 Buildable capabilities (1–6 months)

- Build a **centralized nonce allocator service** backed by a transactional datastore (e.g., Postgres with row-level locks per `(chain, account)`), exposing simple APIs (allocate, peek, mark-mined, repair-gap).
- Enhance observability with dashboards showing per-account nonce history, gap detection, and in‑flight queue depth.
- Document **integration guidelines** and run internal training to align all teams on correct nonce and RBF practices, referencing Circle/QuickNode/Openfort materials [Source: Wallet Nonce Management, Circle Developer Docs, 2025; Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].

[Estimate based on: scope vs. available engineering capacity, Medium confidence].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: EVM accounts use one-dimensional sequential nonces; concurrency from MPC multi-device flows and backend automation stresses this model.
- **Problem**: Optimistic, distributed nonce management leads to collisions, gaps, and mis-ordered RBF behavior.
- **Analysis**: Internal dependencies, external ecosystem signals, historical causes, and capability gaps highlight nonce management as an under‑engineered subsystem.
- **Options**:
  - A: Centralized per-account nonce allocator with strict locking.
  - B: Hybrid allocator with bounded optimistic concurrency and gap repair.
  - C: Strategic migration of some flows to smart accounts with 2D nonces.
- **Risks**: Allocator becoming a reliability bottleneck, complex migrations, misconfiguration across chains.

### 7.2 Key judgments (for validation)

1. Centralized nonce allocation with proper locking and recovery can reduce nonce failures to **<0.1%** without breaching latency budgets [Estimate based on: read/write cost modeling and DB benchmarks, Medium confidence].
2. Most nonce incidents stem from architectural design (distributed allocation) rather than rare RPC edge cases; fixing architecture delivers the largest impact.
3. Supporting future 2D nonce and smart account patterns is strategically important; designs that hard‑code EOA semantics only will age poorly [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].

### 7.3 Alternative high-level paths

- **Path A – Strong central allocator**: Immediately build a single logical nonce allocator with strict per-account locking and complete coverage across services.
- **Path B – Incremental hybrid**: Start with a best-effort centralized allocator for high‑value flows and new services, while tightening local safeguards elsewhere.
- **Path C – Smart-account first for high-throughput users**: For certain segments, move to smart accounts with 2D nonces while keeping EOAs for simpler users.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- **Infrastructure bias**: Emphasis on centralized infrastructure may underweight simpler mitigations at the client layer (e.g., per-device throttling, UX nudges).
- **EVM-only bias**: Focus on EVM chains may not generalize to UTXO or other models if the product expands.
- **Under-reporting of issues**: Some nonce-related incidents may be misclassified (e.g., as generic “transaction failed”), underestimating the problem size.

[Estimate based on: internal incident classification patterns, Medium confidence].

### 8.2 Required intelligence

- **Empirical failure data**: Per-chain, per-account statistics of nonce-related failures (collisions, gaps, `nonce too low` errors) over the last 3–6 months.
- **Latency benchmarks**: Measured latency for a prototype allocator service under realistic load and regional RTTs.
- **Partner integration mapping**: Which partners send raw transactions vs. using higher-level APIs, and how they manage nonces today.

### 8.3 Validation plan

- Implement a **shadow allocator** that computes intended nonces alongside existing flows (without enforcing them) for a subset of accounts; compare shadow vs. actual nonces to quantify misallocation.
- Run **load tests** on a staged allocator deployment, verifying p95 allocation latency and behavior during node failures and reorg simulations.
- Conduct **partner pilots** where selected partners route all EVM transactions through the allocator API and jointly review reliability and latency metrics after 4–6 weeks.

[Source: Wallet Nonce Management, Circle Developer Docs, 2025; Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Quantitative targets (e.g., 0.1% failure) may be adjusted once baseline metrics are accurately measured.
- The chosen architecture may tilt more towards **hybrid models** (per-region allocators, partial smart-account adoption) depending on observed hot spots.
- Over time, if smart account adoption accelerates, priority may shift from EOA-specific nonce optimizations toward robust AA infrastructure [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].

### 9.2 Incremental approach

- Phase 1: Instrumentation and shadow allocator; no user-visible changes but gather precise data.
- Phase 2: Limited rollout of centralized allocator for new or low-risk flows, with fast rollback capability.
- Phase 3: Expansion to all critical EVM flows; deprecate legacy local nonce logic.
- Phase 4: Evaluate and, where appropriate, adopt smart-account or 2D nonce architectures for high-throughput power users.

### 9.3 "Good enough" criteria

- Measured nonce-related failures below **0.1%** over at least one month across major chains.
- All production services route EVM transactions through the allocator (or documented, justified exceptions).
- Support ticket volume and MTTR for nonce issues reduced by ≥70% relative to baseline [Source: Problem Statement – EVM Nonce Management for Concurrent MPC Signing, 2025].

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. EVM’s one-dimensional nonce model is fundamentally sequential and incompatible with naïve concurrent transaction initiation; robust operation requires treating nonce management as a **first-class infrastructure concern** [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024].
2. Most current issues stem from **distributed, optimistic nonce assignment** without shared state, leading to collisions, gaps, and confusing RBF outcomes [Source: Wallet Nonce Management, Circle Developer Docs, 2025].
3. A centralized or well-coordinated nonce allocator, combined with better observability and clear integration patterns, can materially reduce incident rates while remaining compatible with future smart-account and 2D nonce schemes [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024].

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

- **【P0 – Critical】**
  1. Design and implement a minimal **centralized nonce allocator API** for all EVM chains (allocate, peek, mark-mined, repair-gap) → Blockchain Engineering Lead → Coverage of EVM submission paths via allocator: 0% → ≥80% → 2025-02-15.
  2. Integrate allocator with MPC coordinator and main backend services; disable local ad‑hoc nonce incrementation → MPC Engineering Team → Number of services using local nonce logic: >5 → 0 (or explicitly approved exceptions) → 2025-03-01.

- **【P1 – Important】**
  3. Build **nonce observability dashboards** (per-account timelines, stuck/gap detection, RBF histories) and alerting → SRE / Observability Team → Accounts with detectable nonce gaps >N minutes: baseline → −80% → 2025-03-15.
  4. Publish **internal integration guidelines** and run training for engineering and support on nonce semantics, allocator usage, and RBF flows → Developer Experience & Support Enablement → Completion of training: 0% → ≥90% of relevant staff trained → 2025-03-31.

- **【P2 – Optional】**
  5. Prototype **smart-account / 2D nonce** support for a subset of high-throughput or institutional users, evaluating throughput and complexity trade-offs → Architecture & Strategy → Pilot accounts migrated: 0 → ≥5 institutional test accounts → 2025-06-30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Allocator outages block all EVM submissions | High | Medium | Allocator DB or service down; elevated timeout rate | Design for high availability (multi‑AZ, failover); implement degraded mode allowing safe sequential fallback; thorough load and DR tests | SRE Lead |
| Mis-integration leaves shadow local allocators active | Medium | High | Incident shows conflicting nonces from legacy path | Strict change management; configuration linting to detect direct RPC submissions; deprecate old libraries | Engineering Leads |
| Latency regression from additional round trips | Medium | Medium | p95 signing latency exceeds UX SLOs | Co-locate allocator near MPC coordinator; cache per-account state carefully; tune DB; avoid extra cross-region hops | Performance Team |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A: Strong centralized allocator (EOA-focused)** | Clear single source of truth; largest immediate reduction in failures; compatible with today’s stack | Engineering effort to integrate all services; new HA dependency | Over‑centralization; complex migrations across regions | Short–medium term focus on EOAs and existing MPC infra | Organization unwilling to invest in infra-level changes |
| **B: Hybrid allocator + guardrails** | Faster initial rollout; allows legacy paths to coexist with strong monitoring and throttling | Ongoing complexity of dual paths; some residual risk | Inconsistent behavior; difficult debugging | When full migration is risky but improvements are urgently needed | Long-term, as technical debt will accumulate |
| **C: Smart-account / 2D nonce shift for key segments** | Structurally better parallelization; future-proof; may unlock richer UX | Requires protocol support, contract audits, different key management | New attack surfaces; user education and integration changes | High-value or power users can tolerate change and complexity | Short-term for broad user base lacking AA support |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **Nonce (EVM)** | Per-account transaction counter that must increase by 1 for each new transaction and is used to enforce ordering and prevent replay | Integer ≥0 | [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024] |
| **`nonce too low` error** | RPC error indicating a transaction’s nonce has already been used or is below the node’s expected nonce for that account | N/A | [Source: EVM RPC error references summarized in QuickNode Guides and Ethereum client docs, 2024, Medium confidence] |
| **Replace-By-Fee (RBF)** | Behavior where a pending transaction can be replaced by a new one with the same nonce and a higher gas fee | N/A | [Source: What is a Nonce? Management Techniques for Your Ethereum Transactions, QuickNode Guides, 2024] |
| **Mempool** | Set of pending and queued transactions held by nodes before inclusion in blocks; ordering is influenced by nonce and gas price | N/A | [Source: Pending and Queued Transactions Explained, QuickNode Guides, 2023] |
| **MPC wallet** | Wallet where private key material is split across multiple parties/devices and signatures are produced via multi-party computation | N/A | [Source: Internal MPC Wallet Architecture Docs, 2024, and general MPC wallet literature] |
| **Centralized nonce allocator** | Stateful service responsible for assigning nonces per `(chain, account)` according to strict rules, replacing ad‑hoc local computation | N/A | Defined for this analysis, informed by Wallet Nonce Management, Circle Developer Docs, 2025 |
| **2D nonce** | Two-dimensional nonce scheme where a `nonce key` defines a logical stream and a `nonce value` is sequential within that stream, enabling safe parallelization | N/A | [Source: 2D Nonce: Transaction Parallelization, Openfort Blog, 2024] |
| **EOA (Externally Owned Account)** | Ethereum account controlled by a private key, as opposed to a smart contract account | N/A | [Source: Ethereum.org, Transactions and Accounts Docs, 2024] |
| **Account abstraction / smart account** | Architecture where a smart contract, not an EOA, defines account behavior (including custom nonces, validation rules, and sponsorship) | N/A | [Source: Ethereum account abstraction EIPs and ecosystem documentation, 2023–2024] |
| **p95 latency** | 95th percentile latency; 95% of requests complete within this duration | Milliseconds (ms) | [Source: Google SRE Book and common latency SLO practices, 2016+] |
| **Gap (nonce gap)** | State where nonce `N+1` or higher is pending while nonce `N` has failed or not yet been mined, blocking later transactions | N/A | [Source: Wallet Nonce Management, Circle Developer Docs, 2025] |

---

## 12. References

### Tier 1 – Primary Protocol and Official Documentation

1. **Wood, G.** (2014, updated 2023). *Ethereum: A Secure Decentralised Generalised Transaction Ledger (Yellow Paper)*. Ethereum Foundation. https://ethereum.github.io/yellowpaper/  
   **[Cited in**: Background assumptions on EVM nonce behavior, Sections 1–3, 11 **]**

2. **Ethereum Foundation.** (2024). *Transactions – Ethereum Developer Docs*. https://ethereum.org/en/developers/docs/transactions/  
   **[Cited in**: Sections 1–3, 11 **]**

3. **Ethereum Improvement Proposal 1559.** (2021). *EIP-1559: Fee market change for ETH 1.0 chain*. https://eips.ethereum.org/EIPS/eip-1559  
   **[Cited in**: Discussion of RBF and gas behavior, Sections 2, 5, 10, 11 **]**

### Tier 2 – Industry Guides and Provider Documentation

4. **QuickNode.** (2024). *What is a Nonce? Management Techniques for Your Ethereum Transactions*. QuickNode Guides. https://www.quicknode.com/guides/ethereum-development/transactions/how-to-manage-nonces-with-ethereum-transactions  
   **[Cited in**: Sections 1–3, 4, 6–8, 10, 11 **]**

5. **Circle.** (2025). *Wallet Nonce Management*. Circle CPN Developer Docs. https://developers.circle.com/cpn/concepts/wallet-nonce-management  
   **[Cited in**: Sections 1–3, 4–5, 6, 8, 10, 11 **]**

6. **Openfort.** (2024). *2D Nonce: Transaction Parallelization*. Openfort Blog. https://www.openfort.io/blog/parallalization-of-transactions-2d-nonce  
   **[Cited in**: Sections 1, 2, 4, 5, 7, 9–11 **]**

7. **thirdweb.** (2023). *Sending more than one transaction at a time is easy, right?* thirdweb Blog. https://blog.thirdweb.com/sending-more-than-one-transaction-at-a-time/  
   **[Cited in**: Sections 1–3, 5, 10 **]**

8. **QuickNode.** (2023). *Pending and Queued Transactions Explained*. QuickNode Guides. https://www.quicknode.com/guides/ethereum-development/transactions/pending-and-queued-transactions-explained  
   **[Cited in**: Sections 1–3, 10, 11 **]**

### Internal Sources and Estimates

9. **Problem Statement – EVM Nonce Management for Concurrent MPC Signing.** (2025). Internal engineering document describing current pain points, constraints, and goals for nonce management in MPC wallets.  
   **[Cited in**: Context Recap; Sections 1–3, 4, 5, 6, 9, 10 **]**

10. **Supplementary Analysis – Blockchain MPC Wallet Problem Extraction (GPT5).** (2025). Internal analysis document (lines 397–406) summarizing concurrency and nonce issues across MPC wallets.  
   **[Cited in**: Background reasoning in Sections 1, 4, 6, 9 **]**

11. **Internal metrics and incident reviews.** (2024–2025). Aggregated support tickets, incident post‑mortems, and engineering dashboards related to EVM transaction failures.  
   Method: sampling ticket categories, querying error codes, and manual correlation with nonce patterns. Confidence: Medium; to be refined with better nonce‑aware observability.  
   **[Used in**: Sections 1, 2, 5–7, 9–10 **]**
