# Liner GDR – Nine-Aspects Analysis of Blockchain MPC Wallet Problems

## Problem 1 – High Transaction Signing Latency and Limited Throughput in Blockchain MPC Wallets

### 1. Problem Definition (Aspect 1)

**1.1 Problem and contradictions**

- MPC wallets introduce **multi-round, network-dependent signing**, which conflicts with:
  - The need for **low latency** and **high throughput** in high-frequency trading and time-sensitive operations.
  - User expectations formed by **near-instant hardware wallets** and centralized exchanges.
- Core contradictions:
  - **Security vs. speed**: Stronger thresholds / more parties vs. higher latency.
  - **Geo-distributed resilience vs. network delay**: Distributing shares across regions for resilience vs. added RTT and jitter.
  - **Protocol complexity vs. operational simplicity**: Advanced protocols (GG18/20, CGGMP21) vs. operational overhead and implementation risk.

**1.2 Goals and conditions**

- Target outcomes (from the problem statement):
  - **Latency**: <2s for 90% of operations end-to-end for typical thresholds (e.g., 2-of-2, 3-of-5).
  - **Throughput**: ≥50–100 transactions/minute per enterprise tenant under normal load, with graceful degradation under peaks.
- Hard constraints:
  - Must **not weaken cryptographic guarantees** or introduce insecure shortcuts (e.g., reusing nonces incorrectly).
  - Must maintain **correctness under partial failures** (node dropout, packet loss, reordering).
  - Must remain **compatible with existing chains and signature schemes** (ECDSA / EdDSA in most cases).

**1.3 Extensibility and common structure**

- One object, many attributes – signing pipeline can be varied by:
  - Protocol family (GG18/20, CGGMP, DKLS, FROST-style optimizations).
  - Network topology (star/coordinator vs. mesh, regional aggregators).
  - Precomputation depth, batching strategy, parallelism level.
- Virtual vs. physical:
  - Physical: servers, HSMs, network links.
  - Virtual: protocol parameters, retry policies, queueing models, SLAs.
- Hard vs. soft:
  - Hard: number of rounds, cryptographic operations per round.
  - Soft: scheduling, timeouts, backpressure, load balancing.
- Latent vs. manifest:
  - Manifest: user-visible 5–15s signing times, timeouts, failed orders.
  - Latent: poorly tuned timeouts, uneven shard placement, lack of precomputation capacity.

---

### 2. Internal Logical Relations (Aspect 2)

**2.1 Key elements**

- Parties: client(s), MPC nodes, optional coordinator, monitoring/ops systems.
- Resources: CPU for big-int/elliptic-curve ops, network bandwidth/RTT, precomputation storage.
- Processes:
  - Key generation → precomputation → online signing → submission to chain → confirmation.
- Rules:
  - Threshold t-of-n policy, retry/backoff logic, rate limits, queueing and prioritization.

**2.2 Balance and "degree"**

- More parties (higher n) or higher threshold (t) → better compromise resistance but worse latency.
- Aggressive timeouts → fewer stuck sessions but more spurious failures / retries.
- Large precomputation pools → better online latency but more storage and background CPU cost.

**2.3 Key internal causal chains**

- C1: `more signing sessions in parallel` → higher CPU & I/O load → queueing delay → tail latency spikes.
- C2: `greater geo-distribution` → higher RTT + variance → longer per-round completion → multiplied across rounds.

---

### 3. External Connections (Aspect 3)

**3.1 Stakeholders**

- **Institutional traders / market makers**: care about p50/p95 signing latency and order success rate.
- **Retail users**: perceive latency as wallet “slowness”, impacting trust and retention.
- **Wallet providers**: juggle SLA commitments, infra costs, security guarantees.
- **Exchanges / DeFi protocols**: require predictable signing windows to meet order/cancellation cutoffs.

**3.2 Environment and institutions**

- Chain-level constraints: block times, mempool congestion, gas price dynamics.
- Infra environment: cloud regions, cross-region bandwidth/RTT, peering quality.
- Competitive pressure: faster smart-contract or custodial solutions set **user expectations**.

**3.3 Responsibility and room to maneuver**

- Provider responsibility: protocol choice, infra design, SLOs, monitoring, incident response.
- Limited control over: public internet quality between client and nodes, on-chain congestion.

---

### 4. Origins of the Problem (Aspect 4)

**4.1 Key historical nodes**

- Early TSS protocols with **many rounds** and no precomputation.
- First production MPC wallets optimized primarily for **security and correctness**, not HFT.
- Gradual addition of performance features (fewer rounds, pre-signing) without full-stack performance engineering.

**4.2 Background vs. direct causes**

- Background: academic protocols prioritize security proofs over operational latency; security teams risk-averse to “aggressive” optimizations.
- Direct: growth in institutional volume and DeFi activity pushing workloads beyond initial design capacity.

**4.3 Deep structural issues**

- Architectural: treating MPC signing as a **blocking per-transaction RPC** instead of a throughput-oriented service.
- Organizational: unclear ownership of **performance SLOs** vs. security SLOs.

---

### 5. Problem Trends (Aspect 5)

**5.1 Current trend judgment**

- If unchanged, MPC wallets remain **unsuitable for high-frequency cases** and get limited to cold/semi-cold custody and low-frequency treasury ops.

**5.2 Early signals and "spots"**

- Prospect clients choosing smart-contract or custodial solutions citing “too slow”.
- Support tickets on “stuck” or “very slow” transactions.

**5.3 Possible scenarios (6–24 months)**

- Optimistic: Protocol+infra tuning achieves <2s p95 latency; MPC wallets compete for more active use-cases.
- Baseline: Partial improvements; MPC remains niche for medium-frequency, higher-value flows.
- Pessimistic: Latency gap widens vs. alternatives; MPC perceived as “secure but impractical” for trading.

---

### 6. Capability Reserves (Aspect 6)

**6.1 Existing capabilities**

- Strong cryptography and security engineering.
- Experience operating multi-region infra and handling key ceremonies.

**6.2 Capability gaps**

- System performance engineering (profiling, capacity modeling) under cryptographic workloads.
- User-centric SLO design and benchmarking per use-case (HFT vs. treasury vs. retail).

**6.3 Buildable capabilities (1–6 months)**

- Establish a **performance engineering squad** with clear latency/throughput OKRs.
- Invest in **load-testing harnesses** that simulate realistic trading patterns.

---

### 7. Analysis Outline (Aspect 7)

**7.1 Structured outline (bullets only)**

- Background: security-first MPC protocol design, multi-round communication.
- Problem: high latency / limited throughput vs. market expectations.
- Analysis: protocol, network, infra, and operations as key levers.
- Options: protocol upgrades, precomputation, topology changes, client-side adaptations.
- Risks & follow-ups: security regressions, implementation bugs, cost overruns.

**7.2 Key judgments (to validate)**

- Latest TSS protocols and precomputation can reach sub-2s p95 latency in realistic settings.
- Network path optimization yields meaningful gains vs. protocol-internal limits.

**7.3 Alternative paths (high level)**

- Path A – **Protocol-centric optimization**.
- Path B – **Infra/network-centric optimization**.
- Path C – **Product scoping**: constrain MPC to suitable use-cases and pair with other wallet types.

---

### 8. Validating the Answer (Aspect 8)

**8.1 Potential biases**

- Security-centric teams may underestimate user impatience.
- Performance optimists may underestimate cryptographic lower bounds.

**8.2 Required intelligence and feedback**

- Full latency distribution (p50/p90/p95/p99) across client geos, thresholds, and chains.
- Competitive benchmarks vs. smart-contract and custodial solutions for similar use-cases.

**8.3 Validation plan**

- Run controlled load tests before/after protocol & infra changes.
- Pilot optimized configuration with a small set of institutional clients and compare KPIs.

---

### 9. Revising the Answer (Aspect 9)

**9.1 Parts likely to be revised**

- Feasible latency targets for global vs. regional setups.
- Cost/benefit ratio of adopting cutting-edge protocols in production.

**9.2 Incremental adjustment approach**

- Start with **per-region optimizations and precomputation**, then consider protocol changes.
- Roll out improvements to a small traffic slice first, measure, then expand.

**9.3 "Better, not perfect" criteria**

- For HFT-critical users: p95 signing <2s and error rate <0.5% over 90 days.
- For retail users: perceived signing latency similar to major competing wallets.

---

### 10. Summary & Action Recommendations (Aspect 10)

**10.1 Core insights**

- The latency/throughput problem is primarily a **system design** and **SLO alignment** issue around an inherently slower primitive.
- Significant improvements are possible by combining protocol advances, precomputation, and infra tuning, without sacrificing security.

**10.2 Near-term action list (0–3 months)**

- 【P0】Define target SLOs per use-case (HFT, retail, treasury) and instrument full signing pipeline to measure them.
- 【P0】Build a repeatable performance test harness covering typical thresholds and geos.
- 【P1】Increase and tune precomputation pools for hot accounts / tenants; monitor impact on p95 latency.
- 【P1】Pilot regional clustering of MPC nodes for latency-sensitive tenants.

**10.3 Risks and responses**

- Risk: Protocol optimization introduces subtle security bugs.
  - Mitigation: Formal review, staged rollout, independent audits.
- Risk: Infra upgrades increase TCO beyond acceptable limits.
  - Mitigation: Tie investments to clear SLO/ROI metrics; prioritize high-value tenants first.

---

## Problem 2 – Insider Threats and Collusion Risks in Blockchain MPC Wallets

### 1. Problem Definition (Aspect 1)

**1.1 Problem and contradictions**

- While MPC removes a **single key holder**, it still relies on **trust assumptions** about multiple key-share holders.
- Core contradictions:
  - **Decentralized control vs. coordinated governance**: more independent parties reduce single-point compromise but increase collusion surface.
  - **Operational access vs. least-privilege**: staff need sufficient access for operations, but every privilege increases insider threat risk.

**1.2 Goals and conditions**

- Target: **zero incidents** of asset loss due to insider threats or collusion per year.
- Conditions:
  - Maintain usable operations (no endless approvals for trivial transactions).
  - Align with legal / regulatory expectations for fiduciary standards.

**1.3 Extensibility and common structure**

- Virtual vs. physical:
  - Physical: servers, HSMs, devices hosting shares.
  - Virtual: policies, role definitions, approval workflows, monitoring rules.
- Hard vs. soft:
  - Hard: threshold parameters, org structure (independent legal entities vs. one company).
  - Soft: culture, ethics, incentives, whistleblowing channels.

---

### 2. Internal Logical Relations (Aspect 2)

**2.1 Key elements**

- Key share holders: internal teams, external custodians, automated services.
- Policy engine: who can request, approve, and finalize transactions.
- Audit/logging: immutable records, anomaly detection.

**2.2 Balance and "degree"**

- Too strict policies → friction, workarounds (shadow processes), frustrated users.
- Too lax policies → easy abuse with low detection probability.

**2.3 Key internal causal chains**

- Poor segregation of duties + weak logging → easier undetected collusion.
- Strong, independent audit + robust logging → higher deterrence and earlier detection.

---

### 3. External Connections (Aspect 3)

**3.1 Stakeholders**

- Institutional clients, end users, regulators, external auditors, insurance providers.

**3.2 Environment and institutions**

- Regulatory frameworks (custody, AML, fiduciary duty).
- Insurance underwriting standards for digital asset custody.

**3.3 Responsibility and room to maneuver**

- Provider must design robust governance; some risk remains at the **client organization** side (their internal controls).

---

### 4. Origins of the Problem (Aspect 4)

**4.1 Key historical nodes**

- Crypto custody historically relied on trusted individuals, then HSMs, then MPC.
- MPC adoption sometimes assumed “math solves trust”, underinvesting in governance design.

**4.2 Background vs. direct causes**

- Background: human incentives, opaque organizations, lack of mature standards.
- Direct: inadequate role separation, over-privileged accounts, missing independent oversight.

**4.3 Deep structural issues**

- Concentration of control within a **single legal entity** despite cryptographic distribution.

---

### 5. Problem Trends (Aspect 5)

**5.1 Current trend judgment**

- Without deliberate design, MPC systems risk becoming **centralized in practice**, with high-impact insider risks.

**5.2 Early signals and "spots"**

- Shared admin accounts, manual overrides, missing peer reviews of high-value transactions.

**5.3 Possible scenarios**

- Optimistic: standardized governance and auditor scrutiny make MPC custody safer than legacy models.
- Pessimistic: high-profile insider/ collusion incident erodes trust in MPC.

---

### 6. Capability Reserves (Aspect 6)

**6.1 Existing capabilities**

- Cryptographic separation of knowledge; ability to require multiple cosigners.

**6.2 Capability gaps**

- Governance design, behavioral monitoring, red-teaming of collusion scenarios.

**6.3 Buildable capabilities**

- Introduce **policy-as-code** with independent review and regular control testing.

---

### 7. Analysis Outline (Aspect 7)

- Background: MPC eliminates single private keys but not human collusion.
- Problem: insider and collusion risks remain material.
- Analysis: distribution of shares, roles, incentives, logging, audit.
- Options: multi-organization split, independent trustees, insurance-linked controls.
- Risks: usability degradation, false positives in monitoring.

---

### 8. Validating the Answer (Aspect 8)

- Needed data: incident statistics, red-team results, internal audit findings.
- Plan: run tabletop exercises, simulate rogue insider scenarios, measure detection/response.

---

### 9. Revising the Answer (Aspect 9)

- Most likely to change: optimal balance between operational efficiency and control strength.
- Approach: iteratively tighten controls where evidence of abuse or near-miss appears.

---

### 10. Summary & Action Recommendations (Aspect 10)

- **Core insight**: MPC is a **necessary but not sufficient** control; human and organizational design remain decisive.
- Actions (0–3 months):
  - 【P0】Map all privileged roles and enforce least privilege + 4-eyes for high-value flows.
  - 【P0】Deploy immutable logging and independent log review for signing operations.
  - 【P1】Engage external auditors to review governance and threat models.
  - 【P2】Design and run red-team exercises focusing on collusion attacks.

---

## Problem 3 – Complex and Non-Standardized Backup and Recovery Mechanisms

### 1. Problem Definition (Aspect 1)

**1.1 Problem and contradictions**

- Users want **simple, reliable recovery** (like a single seed phrase), but MPC recovery is **multi-party and protocol-specific**.

**1.2 Goals and conditions**

- Restore wallets within ~1 hour with ≥80% reduction in failure rates, while keeping strong security.

**1.3 Extensibility and common structure**

- One attribute, many objects: "recovery" can mean device loss, share loss, custodian exit, legal dispute.
- Virtual vs. physical: physical devices vs. virtual recovery workflows and credentials.

---

### 2. Internal Logical Relations (Aspect 2)

**2.1 Key elements**

- Recovery shares, backup locations, identity verification, support processes.

**2.2 Balance and "degree"**

- Too many backup shares → easier recovery but increased leak surface.
- Too few / too complex → increased risk of permanent loss.

**2.3 Key causal chains**

- Poor UX + complex instructions → user errors → failed recovery → support burden and asset loss.

---

### 3. External Connections (Aspect 3)

- Stakeholders: retail users, institutions, support teams, regulators (re duty of care).
- Environment: competing wallets offering smoother recovery experiences.

---

### 4. Origins (Aspect 4)

- Early MPC solutions aimed at **institutional operators**; UX was secondary.
- Consumerization brought current friction into focus.

---

### 5. Trends (Aspect 5)

- If unresolved, MPC will be perceived as "too risky" for mainstream users due to recovery fears.

---

### 6. Capability Reserves (Aspect 6)

- Strong cryptographic building blocks; growing experience with social recovery and biometrics.

---

### 7. Analysis Outline (Aspect 7)

- Background: distributed shares vs. single seed.
- Problem: non-standard, complex flows.
- Options: standardization, abstraction via UX layers, social/biometric hybrid schemes.

---

### 8. Validating the Answer (Aspect 8)

- Collect metrics on recovery success, time, and satisfaction across providers.

---

### 9. Revising the Answer (Aspect 9)

- Revise as new standards and identity schemes (e.g., DIDs) mature.

---

### 10. Summary & Action Recommendations (Aspect 10)

- **Insight**: Recovery is the **main UX bottleneck** and a key adoption barrier.
- Actions (0–3 months):
  - 【P0】Map all recovery scenarios and failure modes; instrument success-rate metrics.
  - 【P1】Prototype at least one **opinionated, guided recovery flow** optimized for typical users.
  - 【P1】Draft or adopt an internal recovery standard to reduce provider-specific variation.

---

## Problem 4 – Dependence on Centralized Third-Party Providers

### 1. Problem Definition (Aspect 1)

- MPC implementations often store at least one share with a provider, creating **centralization and custody-like risk**.

### 2. Internal Logical Relations (Aspect 2)

- Convenience and recovery simplicity directly increase reliance on provider availability and integrity.
- The more users depend on provider-held shares, the more **systemic impact** of provider failure.

### 3. External Connections (Aspect 3)

- External roles: cloud providers, regulators, end-users, other infra providers.
- Regulatory classification may shift solutions into **custody** regimes.

### 4. Origins (Aspect 4)

- Retail-focused design choices optimized for **ease-of-use**, not strict self-sovereignty.

### 5. Trends (Aspect 5)

- Movement towards **decentralized MPC networks** and multi-provider splits, but early.

### 6. Capability Reserves (Aspect 6)

- Technical capacity to split shares across multiple independent providers.

### 7–9. Outline, Validation, Revision (Aspects 7–9)

- Outline: clarify trade-offs between self-custody purity and mass-market usability.
- Validate: user studies on willingness to manage more complexity; failure drills for provider outage.
- Revise: update stance based on real-world outages and regulatory developments.

### 10. Summary & Action Recommendations (Aspect 10)

- **Insight**: Many "MPC" deployments are **logically centralized**; risk is systemic.
- Actions:
  - 【P0】Review current share allocation models; identify true single-provider dependencies.
  - 【P1】Design multi-provider or user+provider+backup models with graceful degradation.
  - 【P1】Document clearly to users the trust assumptions and failure modes.

---

## Problem 5 – Regulatory Compliance Challenges from Off-Chain Signing and Privacy

### 1. Problem Definition (Aspect 1)

- Off-chain MPC signing reduces on-chain transparency of approval workflows, complicating **KYC/AML and audit**.

### 2. Internal Logical Relations (Aspect 2)

- Strong privacy for signers ↔ weaker direct observability for regulators.
- Rich off-chain logs ↔ risk of data protection obligations (GDPR, etc.).

### 3. External Connections (Aspect 3)

- Key roles: regulators, compliance officers, legal, institutional clients.
- Environment: rapidly evolving crypto regulation, travel rule, MiCA, etc.

### 4. Origins (Aspect 4)

- MPC focused first on technical security; compliance layering came later.

### 5. Trends (Aspect 5)

- Increasing demand for **cryptographically verifiable audit trails** without exposing private data broadly.

### 6. Capability Reserves (Aspect 6)

- Cryptographic tools (ZK proofs, signed logs) can reconcile some privacy vs. transparency tensions.

### 7–9. Outline, Validation, Revision

- Outline: map obligations (who must know what, when) to technical capabilities.
- Validate: legal opinions and regulator feedback on proposed architectures.
- Revise: adapt to new guidance and enforcement patterns.

### 10. Summary & Action Recommendations

- **Insight**: Compliance is a **design dimension**, not an afterthought.
- Actions:
  - 【P0】Map all regulatory requirements per target market and tie them to concrete system artefacts (logs, attestations).
  - 【P1】Prototype **auditable yet privacy-preserving** workflows (e.g., ZK attestations of policy-compliant approvals).

---

## Problem 6 – Scalability and Performance Limitations for High-Frequency and DeFi Use Cases

### 1. Problem Definition (Aspect 1)

- MPC wallets struggle to support high-frequency, programmable interactions compared to smart contract wallets.

### 2. Internal Logical Relations (Aspect 2)

- Each MPC signing is an **independent multi-round protocol**, limiting batching and programmability.

### 3. External Connections (Aspect 3)

- DeFi protocols, order routers, account abstraction frameworks (e.g., ERC-4337) define external expectations.

### 4. Origins (Aspect 4)

- MPC designed around "sign standard tx" abstraction, not complex programmable accounts.

### 5. Trends (Aspect 5)

- Hybrid models (MPC + smart contracts) and account abstraction aiming to close the gap.

### 6. Capability Reserves (Aspect 6)

- MPC’s chain-agnostic signatures and emerging hybrid wallet designs.

### 7–9. Outline, Validation, Revision

- Outline: clarify which use-cases are best-fit for MPC vs. smart contracts vs. hybrids.
- Validate: benchmarks on gas, latency, and complexity across architectures.
- Revise: adjust positioning as AA and L2s mature.

### 10. Summary & Action Recommendations

- **Insight**: Pure MPC is ill-suited to some DeFi patterns; hybrids can capture most value.
- Actions:
  - 【P0】Segment use cases into "MPC-suitable" and "hybrid-required" buckets.
  - 【P1】Design and prototype at least one hybrid MPC+AA architecture for key DeFi scenarios.

---

## Problem 7 – High Total Cost of Ownership and Operational Complexity in Enterprise Deployments

### 1. Problem Definition (Aspect 1)

- Enterprise MPC deployments are **costly and complex**, impacting adoption and ROI.

### 2. Internal Logical Relations (Aspect 2)

- More security/compliance features → more engineering, audits, and training → higher TCO.

### 3. External Connections (Aspect 3)

- Competitive landscape: custodians and WaaS vendors, internal build-vs-buy decisions.

### 4. Origins (Aspect 4)

- First-gen systems built as bespoke projects rather than productized platforms.

### 5. Trends (Aspect 5)

- Movement towards **standardized platforms**, "MPC as a service", and better SDKs.

### 6. Capability Reserves (Aspect 6)

- Accumulated implementation experience; room for process standardization.

### 7–9. Outline, Validation, Revision

- Outline: identify main cost drivers (engineering hours, audits, run costs).
- Validate: TCO models across vendors and deployment models.
- Revise: update as tooling and standards mature.

### 10. Summary & Action Recommendations

- **Insight**: TCO is largely a **productization and standardization** problem.
- Actions:
  - 【P0】Quantify TCO across representative clients; publish internal benchmarks.
  - 【P1】Invest in reusable integration patterns, reference architectures, and automation to reduce marginal deployment cost.

---

## Problem 8 – Limited Interoperability with Networks, Wallet Types, and DeFi Protocols

### 1. Problem Definition (Aspect 1)

- Despite signature-level compatibility, MPC wallets face **practical interoperability issues** with diverse chains, wallets, and DeFi protocols.

### 2. Internal Logical Relations (Aspect 2)

- Off-chain operation obscures MPC from on-chain protocols that expect specific contract interfaces or seed-based models.

### 3. External Connections (Aspect 3)

- External systems: hardware wallets, traditional wallets, chain-specific tooling, DeFi dApps.

### 4. Origins (Aspect 4)

- MPC projects optimized for **signature generation**, not broad ecosystem integration.

### 5. Trends (Aspect 5)

- Growth of multi-chain tooling, bridges, and wallet standards may either ease or complicate integration.

### 6. Capability Reserves (Aspect 6)

- MPC’s chain-agnostic nature and ability to support multiple signature schemes.

### 7–9. Outline, Validation, Revision

- Outline: classify interoperability gaps (by chain, by wallet type, by protocol feature).
- Validate: empirical testing across major chains and dApps.
- Revise: prioritize based on user demand and strategic value.

### 10. Summary & Action Recommendations

- **Insight**: Interoperability is less about math and more about **ecosystem alignment and engineering effort**.
- Actions:
  - 【P0】Build and maintain an interoperability matrix across chains, wallet types, and top DeFi protocols.
  - 【P1】Prioritize bridging gaps that block high-value user journeys (e.g., specific L2 + DEX combos).
