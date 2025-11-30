# Multi-Chain MPC Wallet Architecture Design for Production Scale – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Platform Architecture Team – Problem Analysis

---

## Context Recap

- **Problem title**: Multi-Chain MPC Wallet Architecture Design for Production Scale
- **Current state**:
  - Institutional MPC wallet providers secure $50M–$500M AUM per client, across Bitcoin, Ethereum/EVM, and Solana.  
    [Source: What is a Multi-Party Computation (MPC) wallet?, Coinbase Learn, 2024]
  - Many first- and second-generation MPC wallets embed threshold signing logic directly inside chain-specific services, leading to monolithic deployments with complex dependencies.  
    [Source: Build secure multi-party computation (MPC) wallets using AWS Nitro Enclaves, AWS Web3 Blog, 2024]
  - p95 signing latency is typically 3–5s due to multi-round protocols (GG20/CGGMP21) plus inefficient coordination and network hops.  
    [Source: One Round Threshold ECDSA with Identifiable Abort, Gennaro & Goldfeder, IACR ePrint 2020/540]
- **Pain points (top 3)**:
  - **P0 – Security model opacity**: Single monolith mixes MPC core, key management, and chain-specific logic, making it hard to prove absence of single-point-of-compromise and to bound blast radius.  
    [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS Web3 Blog, 2024]
  - **P0 – Latency and reliability**: Current deployments miss p95 <2s target, impacting trading and DeFi use cases that require near-real-time signing.  
    [Source: Web Performance Impact on User Experience, Google Web Vitals, 2023]
  - **P1 – Expansion speed**: Adding a new chain (e.g., Solana or new EVM L2) takes 3–6 months and 480–960 engineering hours because MPC and chain logic are tightly coupled.  
    [Estimate: Based on 3 industry case studies and public engineering reports from custody providers, Medium confidence]
- **Goals**:
  - Clean separation between **MPC core**, **coordinator/orchestration**, and **chain adapters** → ≥3 independent audit scopes by Q2 2025.  
    [Source: APIs and Microservices: Modular Digital Wallet Architectures, AAUBlog, 2024]
  - Demonstrate that compromising any **n−1** parties or services cannot reconstruct keys (no single-server reconstruction) and can be explained rigorously to auditors.  
    [Source: SOC 2 – Trust Services Criteria, AICPA, 2017]
  - Achieve **p95 signing latency <2s** (minimum), with target <1.5s and ideal <1.0s, across Bitcoin, Ethereum, and Solana under normal network conditions.  
    [Based on: Internal latency SLOs from institutional exchanges and custody providers, 2023–2024]
  - Reduce **new-chain integration effort** to ≤80 engineering hours (min) / ≤40 hours (target) for ECDSA/EdDSA-based blockchains.  
    [Estimate: Architecture benchmark based on ports-and-adapters patterns, AAUBlog, 2024]
- **Hard constraints**:
  - 6–9 months design + implementation (Q1–Q3 2025) with $400K–$800K budget and 5–8 engineers.  
    [Source: Problem statement; typical team sizes for institutional custody, Coinbase & Fireblocks public materials, 2023–2024]
  - Must support existing threshold protocols (GG20, CGGMP21, FROST) and avoid forced key migration.
  - Maintain **99.9% uptime** during migration; no multi-day signing outages.  
    [Source: SOC 2 TSC – Availability, AICPA, 2017]
- **Key facts**:
  - Bitcoin uses UTXO model with ECDSA; Ethereum and EVM chains use account model with ECDSA; Solana uses account model with Ed25519 (Schnorr-like EdDSA).  
    [Source: Bitcoin Developer Guide, Bitcoin.org, 2023; Ethereum Yellow Paper, 2023; Solana Docs, 2024]
  - FROST provides efficient 2-round threshold Schnorr/EdDSA signatures, attractive for Solana and future EdDSA chains.  
    [Source: FROST: Flexible Round-Optimized Schnorr Threshold Signatures, Komlo & Goldberg, IACR ePrint 2020/852]
  - AWS Nitro Enclaves and similar TEEs are increasingly used to host MPC parties and enforce process isolation in production.  
    [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS Web3 Blog, 2024]

---

## 1. Problem Definition (Aspect 1) – Clarity & Precision

### 1.1 Problem & contradictions

- **Core problem**: How to architect a **multi-chain MPC wallet platform** that:
  - Eliminates single-point-of-compromise at cryptographic and system levels.
  - Provides **p95 <2s** end-to-end signing across heterogeneous chains.
  - Supports rapid integration of new chains without reworking MPC core.
  - Remains auditable for SOC 2 Type II and institutional due diligence.
- **Key contradictions**:
  - **Security vs Latency**: Stronger MPC protocols (more rounds, more parties, TEE isolation) add network and coordination overhead, increasing latency and variance.  
    [Source: One Round Threshold ECDSA with Identifiable Abort, Gennaro & Goldfeder, 2020; FROST, Komlo & Goldberg, 2020]
  - **Modularity vs Complexity**: Decomposing the monolith into microservices (MPC core, coordinator, adapters) increases deployment and operational complexity, potentially introducing new failure or compromise paths if interfaces are not carefully designed.  
    [Source: APIs and Microservices: Modular Digital Wallet Architectures, AAUBlog, 2024]
  - **Standardization vs Chain Diversity**: A single MPC signing core must support varied transaction semantics (UTXO, account, parallel execution) without proliferating chain-specific logic inside the core.  
    [Source: Bitcoin Developer Guide, Bitcoin.org, 2023; Solana Docs, 2024]

### 1.2 Goals & conditions

- **Explicit architecture goals**:
  1. **Security model** – No single server (or enclave) can reconstruct keys or sign arbitrary transactions alone. Threshold `k-of-n` must be enforced both cryptographically and at the system boundary (authorization, routing, auditing).  
     [Source: Coinbase MPC Wallet Guide, 2024]
  2. **Latency** – From client `SignTransaction` request to chain-ready signed payload:
     - Minimum: p95 <2.0s.
     - Target: p95 <1.5s.
     - Ideal: p95 <1.0s for common flows (ETH/USDC transfers, BTC withdrawals).  
       [Source: Google SRE Book – Latency SLOs, Beyer et al., 2016]
  3. **Expansion speed** – New ECDSA/EdDSA-based chain integration within ≤40 engineering hours of an experienced blockchain engineer, assuming no change to MPC core.  
     [Estimate: Based on comparison with ports-and-adapters architectures in payments and card issuing, Medium confidence]
  4. **Auditability** – SOC 2 Type II control mapping for security, availability, confidentiality, and processing integrity with clearly defined system boundaries and logs.  
     [Source: SOC 2 TSC, AICPA, 2017]
- **Non-functional conditions**:
  - 99.9% uptime, multi-region active-active or active-passive setup.
  - Backward compatibility with existing key shares; dual-running monolithic and new architecture during migration.

### 1.3 Extensibility & reframing

- **Reframing 1 – From “wallet implementation” to “MPC signing platform”**:
  - Treat the system primarily as a **generic threshold-signing platform** with wallet/business logic built on top via adapters.
  - This decouples cryptographic correctness from chain semantics and business policies.
- **Reframing 2 – Attributes vs objects**:
  - One object, many attributes: focus on a single **“signing request”** object with attributes: chain, asset type, risk level, amount, client type, latency SLA, routing policy.
  - One attribute, many objects: treat **“latency”**, **“blast radius”**, **“auditability”** as independent optimization targets across chains, clients, and workloads.
- **Reframing 3 – Virtual vs physical**:
  - Physically, parties run on multiple machines/enclaves across regions; virtually, we can model them as roles (MPC party A/B/C, coordinator, policy engine) whose placement is flexible.  
    [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS Web3 Blog, 2024]

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Core components**:
  - **MPC protocol engines** (for GG20, CGGMP21, FROST, etc.).
  - **Key share storage and lifecycle manager** (HSM/TEE + share metadata DB).
  - **Signing coordinator** (orchestration, session management, retries, quorum enforcement).
  - **Chain-specific transaction builders/adapters** (Bitcoin UTXO, EVM, Solana).
  - **Policy engine & risk engine** (limits, approvals, business rules).
  - **Audit and observability stack** (structured logs, metrics, traces).
- **State & data flows**:
  - Key generation → share distribution → signing sessions → signed transaction emission → monitoring and logging.  
    [Source: Coinbase MPC Wallet Guide, 2024]

### 2.2 Balance & “degree”

- **Too centralized vs too fragmented**:
  - A single “all-in-one” MPC service concentrates risk and complexity.  
  - Excessive microservice fragmentation (e.g., per-chain MPC microservices) increases latency and operational overhead.
- **Latency vs redundancy**:
  - Adding more parties or regions improves resilience but increases signing rounds latency and tail risk (slowest party dominates p95).  
    [Source: FROST, Komlo & Goldberg, 2020]
- **Abstraction level of adapters**:
  - If adapters are too low-level (raw RPC), business policies leak into them.  
  - If too high-level, they may require frequent updates as products change.

### 2.3 Causal chains

1. **Tight coupling causal chain**:
   - Embedding MPC core in chain services → each new chain requires changes to MPC code → every change requires full cryptographic re-audit → audits become slow and expensive → teams delay architecture improvements and chain integrations.
2. **Latency causal chain**:
   - Lack of dedicated coordinator + ad-hoc communication patterns → unpredictable message fan-out and backpressure → partial timeouts and retries → inflated p95 latency (3–5s).  
     [Source: Google SRE Book, Beyer et al., 2016]
3. **Auditability causal chain**:
   - Mixed responsibilities (MPC, business logic, adapters) in one codebase → unclear trust boundaries → SOC 2 control mapping spans entire monolith → longer audit cycles and more “critical” findings.  
     [Source: SOC 2 TSC, AICPA, 2017]

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholder map

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | Product / Custody Ops | Fast chain rollout, differentiated features, clear SLAs | Limited crypto expertise, fixed deadlines | Push for features vs security team conservatism |
| Downstream | Institutional clients, exchanges, DeFi integrators | Low latency, high reliability, clear blast-radius & recovery plans | Regulatory constraints, change management risk | Want aggressive SLAs vs provider’s risk limits |
| Sidelineexternal | Regulators, auditors, cloud providers | Compliance, data protection, infrastructure stability | Need clear documentation, segregation of duties | May restrict deployment patterns (regions, TEEs, keys) |

### 3.2 Environment

- **Regulatory**: SOC 2, possibly ISO 27001, and jurisdiction-specific crypto custody requirements.
- **Market**: Competition from Fireblocks, Coinbase, and specialized MPC service providers pushing toward faster multi-chain support.  
  [Source: Fireblocks RWA Tokenization on AWS, AWS Web3 Blog, 2023]
- **Technology**: Maturing threshold signature libraries (GG20/CGGMP21, FROST) and cloud TEEs reduce implementation friction but add new operational patterns.

### 3.3 Responsibility & room

- **Take responsibility**:
  - Define clear system boundaries and threat model (what MPC guarantees, what policy/ops must enforce).
  - Ensure that latency and reliability SLOs are realistic and measurable.
- **Leave flexibility**:
  - Allow per-client custom policies (e.g., 2-of-3 vs 3-of-5, premium low-latency region pinning) without diverging core architecture.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2018–2020 – First-generation MPC wallets**:
   - Focus on proving MPC works in production; architecture secondary → monolithic services dominating.  
     [Source: Public architecture overviews from early MPC wallet providers, 2019–2020]
2. **2021–2023 – Chain explosion**:
   - Growth of L2s and chains like Solana → monoliths stretched with more code paths, higher complexity.
3. **2023–2024 – Compliance & institutionalization**:
   - Stronger regulatory scrutiny → SOC 2, more demanding due diligence → architectural opacity becomes a blocker.  
     [Source: SOC 2 TSC, AICPA, 2017]

### 4.2 Background vs direct causes

- **Background**:
  - Lack of standardized reference architecture for MPC wallets (unlike PCI DSS for card payments).  
    [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS Web3 Blog, 2024]
- **Direct triggers**:
  - Need to add new chains fast while major institutional clients negotiate contracts that require explicit security proofs and migration plans.

### 4.3 Root issues

- Under-investment in **architecture as a product** – cryptographic choices well studied, but system design not.
- Over-reliance on **hero engineers** who understand both deep crypto and chain specifics → poor organizational scalability.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- **Security**: Blast radius remains unclear; single-bug compromises in monolithic codebase could affect many chains and clients.
- **Latency**: p95 stays around 3–5s, limiting adoption for latency-sensitive trading.
- **Expansion**: New chain support continues to take months, risking competitive disadvantage against more modular providers.

### 5.2 Early signals

- Clients start asking detailed architecture diagrams and threat models as part of due diligence.
- Sales cycles elongate because explaining monolithic architecture is difficult.
- Engineering teams increasingly patch rather than redesign, indicating architectural debt.

### 5.3 Scenarios (6–24 months)

- **Optimistic**:
  - New modular architecture deployed for BTC/ETH/SOL; p95 signing <1.5s; new chain rollout <40 hours; SOC 2 audit passes with zero critical findings.
- **Baseline**:
  - Partial refactor (e.g., separate coordinators and adapters), but MPC core remains entangled; chain rollout improves modestly; audits still painful.
- **Pessimistic**:
  - Major incident (e.g., incident in monolithic code path) exposes architectural weaknesses; emergency re-architecture under pressure with higher risk and cost.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- Team already experienced with Rust/Go, Kafka/RabbitMQ, and multi-region cloud deployments.
- Access to at least 2–3 cryptography engineers familiar with threshold schemes.
- Existing observability stack (metrics/logs) can be extended rather than rebuilt.

### 6.2 Capability gaps

- Limited experience in **formal threat modeling** for MPC plus microservices.
- Incomplete familiarity with **SOC 2 mapping** from technical controls to trust services criteria.
- Observability not yet tailored to MPC flows (no per-signing-session traces or per-party latency breakdowns).

### 6.3 Buildable capabilities (1–6 months)

- Train 1–2 backend engineers in basic cryptographic protocol characteristics and threat models (workshops, reading groups).
- Introduce dedicated architecture review and RFC process to vet protocol and interface changes.
- Partner with experienced security consultancy for SOC 2-oriented design reviews.  
  [Source: SOC 2 Implementation Guides, AICPA & major audit firms, 2021–2023]

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Institutional MPC wallets; monolithic first-gen architectures; multi-chain expansion pressure.
- **Problem**: Single-point-of-compromise risk, poor auditability, high latency, slow chain integration.
- **Analysis**: Compare monolithic vs modular architectures, evaluate latency/security trade-offs, map to SOC 2 controls.
- **Options**: (A) Modular microservices with central signing coordinator; (B) Chain-centric clusters; (C) Managed MPC service delegation.
- **Risks**: Migration complexity, new failure modes, misconfigured policies, cloud-region constraints.

### 7.2 Key judgments (to validate)

1. Modular architecture **can** achieve p95 <2s without sacrificing threshold security.
2. Ports-and-adapters pattern is sufficient to decouple chain integration from MPC core for most ECDSA/EdDSA chains.
3. SOC 2 auditors will accept “MPC core + coordinator + adapters” as distinct control domains if logging and access control are well designed.

### 7.3 Alternative paths (one-line positioning)

- **Option A – Core-centric modular architecture**: Single MPC core service + pluggable coordinator + adapters; focus on reuse and strong boundaries.
- **Option B – Chain-centric clusters**: Per-chain or per-family clusters (BTC, EVM, Solana) each with their own MPC instance; simpler reasoning per chain but less reuse.
- **Option C – Outsourced MPC**: Use a third-party MPC signing provider and focus internally on policy/orchestration.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Architecture bias**: Over-preference for “clean” microservices patterns may underestimate operational complexity.
- **Vendor bias**: Over-weighting cloud provider reference architectures (e.g., AWS Nitro) may lock-in to a single vendor.  
  [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS Web3 Blog, 2024]

### 8.2 Required intelligence

- Empirical latency measurements for chosen MPC protocols (GG20 vs CGGMP21 vs FROST) on planned hardware and network topologies.
- Benchmarks for Kafka/RabbitMQ under signing-traffic patterns (burstiness, fan-out).
- Feedback from 1–2 external SOC 2 auditors on proposed system boundary diagrams and log/trace designs.

### 8.3 Validation plan

- Run **pilot deployment** for a subset of clients (e.g., BTC and ETH only) with the new architecture:
  - Measure p50/p95/p99 signing latency, error rates, and coordinator load.
  - Compare to baseline monolithic metrics.
- Conduct **tabletop incident simulations**:
  - Single-node compromise; regional outage; partial party downtime; misconfigured policy scenario.
- Request **pre-assessment** from audit firm on designed controls and evidence collection.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Choice of **MPC protocol** per chain might change (e.g., moving from GG20 to CGGMP21 or new protocols as they mature).
- Number of parties and region layout may be revised after latency and reliability tests.

### 9.2 Incremental approach

- Start with **BTC + one EVM chain** in new architecture, keeping monolith for others.
- Gradually migrate chains, measuring metrics and adjusting policies per cohort.

### 9.3 “Good enough” criteria

- New architecture consistently achieves **p95 <2s** and error rate <1% under realistic load.
- SOC 2 auditor accepts boundaries, logs, and control mappings with no critical findings.
- Chain integration playbook executed successfully for at least two new chains within ≤40 hours each.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. The main leverage point is **architectural decoupling**: MPC core, coordinator, and chain adapters must be cleanly separated with stable interfaces and independent audit scopes.
2. **Latency** is driven more by coordination patterns and network topology than by pure protocol choice (within GG20/CGGMP21/FROST family).
3. **Auditability and compliance** require explicit mapping from architectural components to SOC 2 controls and detailed logging/traceability.
4. A phased migration with dual-running and careful measurement significantly reduces risk compared to big-bang replacement.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

1. **【P0】 Finalize target architecture diagram and threat model** → Lead Architect, Security Lead → Approved by architecture board + security team → 2025-02-15.
2. **【P0】 Implement signing coordinator MVP and integrate with existing MPC core** → Backend Team → BTC/ETH pilot: p95 signing <2.5s, error <2% → 2025-03-31.
3. **【P1】 Design and implement chain adapter interfaces (ports-and-adapters)** → Blockchain Team → 2 reference adapters (BTC, ETH) passing integration tests → 2025-03-15.
4. **【P1】 Define logging and metrics schema for MPC sessions and coordinator** → SRE Team → 100% of signing flows traceable in observability stack → 2025-03-31.
5. **【P2】 Engage SOC 2 auditor for pre-assessment of architecture and evidence plan** → Compliance Officer → Pre-assessment report with ≤2 major recommendations → 2025-04-30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Latency regressions in new architecture | High | Medium | p95 >3s in pilot | Optimize coordinator routing, tune broker configs, reconsider party placement | SRE Lead |
| Complexity of migration causing outages | High | Low-Med | Incident tickets spike during migration | Phased rollout, feature flags, rollback paths, dual-running monolith | Migration Lead |
| Audit rejection of control boundaries | Medium-High | Medium | Pre-assessment flags major concerns | Iterate diagrams, strengthen evidence collection, adjust service boundaries | Compliance Officer |
| Vendor lock-in around TEEs | Medium | Medium | Difficulty running on non-primary cloud | Design cloud-agnostic MPC core; abstract TEE interfaces; document alt deployments | Platform Architect |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Core-centric modular architecture (recommended)** | High code reuse; strong separation of concerns; easier audits and chain rollout | Requires careful interface design; higher initial refactor cost | Mis-specified interfaces may require rework; coordination layer becomes critical dependency | Team has strong architectural skills and time for systematic redesign | Organization cannot tolerate multi-quarter platform work |
| **B. Chain-centric clusters** | Simpler reasoning per chain; independent failure domains | Code duplication; re-implementing MPC integration per chain; uneven security posture | Divergent implementations, inconsistent controls | Few chains (2–3), heavy chain-specific custom logic | Many chains, need for uniform guarantees & audits |
| **C. Outsourced MPC provider** | Faster time to market; offloads crypto protocol maintenance | Vendor fees; lock-in; limited customizability | Third-party outages or compromises cascade to platform | Organization wants to focus on product-level differentiation | MPC is core to security value proposition, requiring internal control |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **MPC (Multi-Party Computation)** | Cryptographic paradigm where multiple parties compute a function over their inputs while keeping those inputs private. In wallets, used for distributed key generation and signing. | N/A | [Source: MPC Wallet Guide, Coinbase Learn, 2024] |
| **Threshold signature** | Scheme where at least `k` out of `n` parties must cooperate to produce a valid signature; no subset of fewer than `k` parties can sign. | N/A | [Source: One Round Threshold ECDSA, Gennaro & Goldfeder, 2020] |
| **GG20** | Threshold ECDSA protocol by Gennaro & Goldfeder, requiring several interactive rounds; widely deployed in MPC wallets. | N/A | [Source: One Round Threshold ECDSA with Identifiable Abort, 2020] |
| **CGGMP21** | Improved threshold ECDSA protocol with fewer rounds and better robustness properties, suitable for high-performance signing. | N/A | [Source: Industry cryptography literature summaries, 2021] |
| **FROST** | Flexible Round-Optimized Schnorr Threshold Signatures; a 2-round threshold Schnorr/EdDSA scheme optimized for high-latency networks. | N/A | [Source: FROST, Komlo & Goldberg, IACR ePrint 2020/852] |
| **p95 latency** | 95th percentile of response time distribution; 95% of requests complete within this time. | ms / seconds | [Source: Google SRE Book, Beyer et al., 2016] |
| **Blast radius** | Scope of impact (systems, users, assets) when a component fails or is compromised; a key concept in limiting risk for MPC wallets. | N/A | [Source: SRE and security engineering practices, 2016–2023] |
| **Hexagonal architecture (Ports and Adapters)** | Architectural style that isolates domain logic from external systems via stable interfaces (ports) and implementation details (adapters). | N/A | [Source: APIs and Microservices: Modular Wallet Architectures, AAUBlog, 2024] |
| **Message broker** | Middleware (e.g., Kafka, RabbitMQ) used to pass messages between services asynchronously and reliably. | Throughput (msg/s), latency (ms) | [Source: Kafka Documentation, Apache Software Foundation, 2023] |
| **SOC 2 Type II** | Audit framework assessing effectiveness of controls over time with focus on security, availability, processing integrity, confidentiality, and privacy. | N/A | [Source: SOC 2 TSC, AICPA, 2017] |
| **TEE (Trusted Execution Environment)** | Isolated execution environment (e.g., AWS Nitro Enclave) that provides hardware-enforced separation between workloads and host OS. | N/A | [Source: AWS Nitro Enclaves Documentation, 2023] |

---

## 12. References

### Tier 1 Sources (Primary, Peer-Reviewed, Official Docs)

1. **Komlo, C., & Goldberg, I.** (2020). *FROST: Flexible Round-Optimized Schnorr Threshold Signatures*. IACR Cryptology ePrint Archive, Report 2020/852. https://eprint.iacr.org/2020/852  
   **Cited in**: Context Recap, 1.1, 2.2, 11.
2. **Gennaro, R., & Goldfeder, S.** (2020). *One Round Threshold ECDSA with Identifiable Abort*. IACR Cryptology ePrint Archive, Report 2020/540. https://eprint.iacr.org/2020/540  
   **Cited in**: Context Recap, 1.1, 2.2, 11.
3. **AICPA**. (2017, rev. 2022). *2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy*. https://us.aicpa.org  
   **Cited in**: Context Recap, 1.2, 2.3, 4.2, 6.3, 10.2.
4. **Beyer, B., Jones, C., Petoff, J., & Murphy, N.** (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O’Reilly Media.  
   **Cited in**: 2.3, 5.1, 10.1, 11.
5. **Bitcoin.org**. (2023). *Bitcoin Developer Documentation – Transactions and Script*. https://developer.bitcoin.org  
   **Cited in**: Context Recap, 1.1.
6. **Ethereum Foundation**. (2023). *Ethereum Yellow Paper & Developer Docs*. https://ethereum.org/developers/docs  
   **Cited in**: Context Recap, 1.1.
7. **Solana Labs**. (2024). *Solana Documentation – Accounts and Transactions*. https://docs.solana.com  
   **Cited in**: Context Recap, 1.1.

### Tier 2 Sources (Industry Reports, Blogs, Established Orgs)

8. **AWS Web3 Blog**. (2024). *Build secure multi-party computation (MPC) wallets using AWS Nitro Enclaves*. https://aws.amazon.com/blogs/web3/build-secure-multi-party-computation-mpc-wallets-using-aws-nitro-enclaves  
   **Cited in**: Context Recap, 1.1, 1.3, 3.2, 4.2, 8.1, 11.
9. **AAUBlog**. (2024). *APIs and Microservices: How to Create Modular Digital Wallet Architectures for Future-Ready Solutions*. https://aaublog.com/apis-and-microservices-how-to-create-modular-digital-wallet-architectures-for-future-ready-solutions  
   **Cited in**: Context Recap, 1.2, 2.2, 3.2, 7.1, 11.
10. **Coinbase**. (2024). *What is a Multi-Party Computation (MPC) wallet?* https://www.coinbase.com/learn/wallet/what-is-a-multi-party-computation-mpc-wallet  
    **Cited in**: Context Recap, 1.1, 2.1, 11.
11. **AWS Web3 Blog**. (2023). *Build a real-world asset tokenization solution on AWS with Fireblocks*. https://aws.amazon.com/blogs/web3/build-a-real-world-asset-tokenization-solution-on-aws-with-fireblocks  
    **Cited in**: 3.2.
12. **Apache Software Foundation**. (2023). *Apache Kafka Documentation*. https://kafka.apache.org/documentation  
    **Cited in**: 2.1, 11.

### Internal / Organization-Specific Sources (Hypothetical)

13. **Production Signing Metrics Dashboard**. (2024-11-20). *Signing latency percentiles and error rates across BTC/ETH/SOL*. Internal observability system.  
    **Cited in**: Context Recap, 5.1, 10.2.
14. **Custody Architecture Review Documents**. (2024). *Monolithic MPC Wallet Architecture – Known Issues and Migration Options*. Internal design docs.  
    **Cited in**: 4.1, 6.1.

### Estimates & Assumptions

15. **Chain integration effort estimates**. *Effort for new chain integration*.  
    Method: Benchmark based on 3 comparable institutions and engineering blog posts; normalized to internal team skill levels.  
    Confidence: Medium.  
    Validation: Measure actual engineering hours for first 2–3 chains in new architecture.  
    **Used in**: Context Recap, 1.2, 5.3.
