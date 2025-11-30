# Computational Cost and Transaction Overhead in MPC Wallet Operations (Nine-Aspects Analysis)

**Document Metadata**

- **Created**: 2025-11-30  
- **Analysis Framework**: Nine Aspects for Analyzing Problems  
- **Source Problem**: `13_Computational_Cost_Transaction_Overhead.md`  
- **Domain**: Blockchain MPC wallets – performance, cost, scalability, energy
- **Status**: Draft

---

## Table of Contents

1. [Context Recap](#context-recap)
2. [1. Problem Definition (Aspect 1)](#1-problem-definition-aspect-1)
3. [2. Internal Logical Relations (Aspect 2)](#2-internal-logical-relations-aspect-2)
4. [3. External Connections (Aspect 3)](#3-external-connections-aspect-3)
5. [4. Origins of the Problem (Aspect 4)](#4-origins-of-the-problem-aspect-4)
6. [5. Problem Trends (Aspect 5)](#5-problem-trends-aspect-5)
7. [6. Capability Reserves (Aspect 6)](#6-capability-reserves-aspect-6)
8. [7. Analysis Outline (Aspect 7)](#7-analysis-outline-aspect-7)
9. [8. Validating the Answer (Aspect 8)](#8-validating-the-answer-aspect-8)
10. [9. Revising the Answer (Aspect 9)](#9-revising-the-answer-aspect-9)
11. [10. Summary & Action Recommendations](#10-summary--action-recommendations)
12. [11. Glossary](#11-glossary)
13. [12. References](#12-references)

---

## Context Recap

- **Problem title**: Computational cost and transaction overhead in MPC wallet operations.
- **Current state**:
  - Threshold ECDSA and related MPC protocols (e.g., GG18, GG20, CGGMP21) introduce roughly 10–100× more CPU work than single ECDSA signatures due to Paillier-based homomorphic multiplications, zero-knowledge proofs, and multiple communication rounds.  
    [Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide]  
    [Source: "A Compute Perspective of MPC-TSS: Paillier in ECDSA Revisited", Silence Laboratories, 2023, https://silencelaboratories.com/blog-posts/a-compute-perspective-of-mpc-tss-paillier-in-ecdsa-revisited-2]
  - Secure MPC wallet signing flows typically show end-to-end latencies of ~2–15 seconds, compared with sub-second latency for EOAs and hardware wallets (cryptography usually <100 ms, user IO dominant).  
    [Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide]  
    [Source: "MPC does have a single point of failure", Cubist, 2024, https://cubist.dev/blog/mpc-does-have-a-single-point-of-failure]
  - Throughput per MPC signing cluster is typically ~50–100 transactions/minute for secure configurations, versus thousands/minute for traditional hot-wallet architectures.  
    [Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide]
  - High-volume providers may spend on the order of USD 5K–50K/month on compute and HSM capacity dedicated to MPC signing, depending on volume, redundancy, and security posture.  
    [Estimate: Derived from AWS c5/r5 instance pricing, dedicated HSM SKUs, and typical 10–100 instance clusters for high-volume custody workloads; Medium confidence, validate via provider interviews, cost benchmarking, and AWS/GCP calculators]
  - Energy consumption and mobile battery drain are substantially higher than for EOA or simple multisig wallets, especially when proofs or heavy big-integer arithmetic are executed on constrained devices.  
    [Source: "A Compute Perspective of MPC-TSS: Paillier in ECDSA Revisited", Silence Laboratories, 2023, https://silencelaboratories.com/blog-posts/a-compute-perspective-of-mpc-tss-paillier-in-ecdsa-revisited-2]  
    [Estimate: Based on CPU power draw for large-integer cryptography and prolonged high-CPU intervals on mobile ARM cores; Medium confidence, validate via controlled power profiling]

- **Pain points**:
  - Profitability pressure for MPC wallet providers operating free/freemium consumer products when per-transaction compute and HSM costs are high and unpredictable.  
    [Source: Problem specification "Computational Cost and Transaction Overhead in MPC Wallet Operations", Operations & Cost Optimization Team, 2025-11-29]
  - Poor UX for latency-sensitive use cases (trading, gaming, real-time payments) when users experience 5–10 second signing delays and abandon flows.  
    [Source: "MPC does have a single point of failure", Cubist, 2024, https://cubist.dev/blog/mpc-does-have-a-single-point-of-failure]
  - Scalability ceiling for serving 100M+ users on current protocols and naive infra architectures without prohibitive cost or degraded security.  
    [Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide]
  - Environmental and regulatory pressure about data center energy use and carbon footprint associated with MPC-heavy workloads.  
    [Source: Data center PUE and renewable energy reporting, major cloud providers, 2023–2024]

- **Goals and success criteria (summarized)**:
  - Latency: Achieve p90 signing latency <3 seconds and p99 <5 seconds by Q4 2026 (from current 5–15 seconds typical).  
    [Source: Problem specification; Supported by latency expectations from Web2 UX benchmarks]
  - Cost: Reduce server/HSM infrastructure costs by ~50% (USD 5K–50K/month → 2.5K–25K/month range) via efficiency improvements and procurement optimization by Q4 2027.  
    [Estimate: Based on mix of protocol optimization, instance rightsizing, spot usage, and hardware acceleration; Medium confidence]
  - Throughput: Increase throughput from ~50–100 tx/min per cluster to 200–500 tx/min via batching, protocol upgrades, and parallelization by Q4 2027.  
    [Source: Problem specification; Assumption: Batching and acceleration can deliver 2–5× improvement]
  - Energy: Establish and track kWh/1000 tx as a standard metric and reduce it by ~40% by Q4 2027 through hardware acceleration and algorithmic improvements.  
    [Estimate: Based on GPU/FPGA acceleration efficiency profiles; Medium confidence]
  - Mobile battery: Reduce mobile battery drain per heavy user day (10–20 tx) by ~60% by offloading and optimized libraries by Q4 2026.  
    [Estimate: Derived from current 15–25% drain estimates vs. <10% target; Low–Medium confidence]
  - Protocol modernization: Migrate ≥80% of production deployments to more efficient protocols (e.g., CGGMP21, optimized Ed25519 threshold) by Q4 2027.  
    [Source: "UC Non-Interactive, Proactive, Threshold ECDSA", Canetti et al., 2021, https://eprint.iacr.org/2021/060]

- **Hard constraints**:
  - Cannot weaken cryptographic parameters (key sizes, security levels) below accepted thresholds for institutional custody.
  - For institutional flows, must maintain malicious security; honest-but-curious MPC is only acceptable for well-scoped, low-risk, or explicitly opt-in scenarios.  
    [Source: "MPC does have a single point of failure", Cubist, 2024, https://cubist.dev/blog/mpc-does-have-a-single-point-of-failure]
  - Network topology must preserve geographic dispersion of key shares required for resilience and compliance; aggressive colocation introduces correlated failure risk.  
    [Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide]
  - Budget window per provider ≈ USD 1–5M over 24 months with limited specialized cryptographic and infra engineers.

- **Key facts**:
  - Paillier-based zero-knowledge proofs and large integer arithmetic dominate CPU time in many threshold ECDSA stacks; Paillier operations are 100–1000× slower than native field arithmetic.  
    [Source: "A Compute Perspective of MPC-TSS: Paillier in ECDSA Revisited", Silence Laboratories, 2023, https://silencelaboratories.com/blog-posts/a-compute-perspective-of-mpc-tss-paillier-in-ecdsa-revisited-2]
  - Newer protocols like CGGMP21 reduce signing rounds (4 vs. 9 in GG18) but migration is incomplete across the ecosystem.  
    [Source: "UC Non-Interactive, Proactive, Threshold ECDSA", Canetti et al., 2021, https://eprint.iacr.org/2021/060]
  - Traders sometimes disable MPC features entirely in popular wallets to achieve sub-second latency.  
    [Source: "MPC does have a single point of failure", Cubist, 2024, https://cubist.dev/blog/mpc-does-have-a-single-point-of-failure]

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

- **Core problem**: MPC wallets deliver stronger key security and flexible access control but at significantly higher
  computational cost, latency, and energy usage than EOAs or simple multisig. This threatens profitability, user
  experience, and scalability for mass-market adoption.
- **Key contradictions**:
  - **Security vs. performance/cost**: Achieving malicious security with full ZKPs and robust network dispersion drives
    both latency (2–15 s) and cost (extra CPU, memory, and bandwidth) upward.  
    [Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025]  
    [Source: "MPC does have a single point of failure", Cubist, 2024]
  - **Distribution vs. coordination overhead**: Splitting keys across more parties increases resilience but multiplies
    communication rounds, failures, and operational complexity.
  - **Mobile UX vs. cryptographic complexity**: Running heavy big-int or ZKP workloads on mobile leads to noticeable
    battery drain and thermal issues, yet offloading everything to servers raises trust and privacy concerns.  
    [Estimate: Based on ARM CPU power/thermals during continuous cryptographic workloads; Medium confidence]
  - **Free-to-use UX vs. real compute cost**: Consumer wallets are often expected to be free, but MPC compute is not;
    providers struggle to map real cryptographic cost to sustainable pricing models.

- **Stakeholder conflicts**:
  - **End users** want near-instant UX at low or zero fees.
  - **Wallet providers** need to recover infrastructure and engineering cost while remaining competitive.
  - **Institutions and regulators** mandate strong security and auditability, often preferring more conservative
    configurations.
  - **Cloud and hardware vendors** benefit from higher compute demand but have limited incentives to optimize for this
    niche without critical mass.

### 1.2 Goals and conditions

- **Quantified goals (summarized)**:
  - p90 latency <3 s, p99 <5 s by Q4 2026.
  - Per-cluster throughput ≥200–500 tx/min by Q4 2027.
  - 50% reduction in monthly MPC infra cost (compute + HSMs + bandwidth) by Q4 2027.
  - 40% reduction in kWh/1000 tx and 60% reduction in mobile battery drain for heavy users.
  - ≥80% deployments on modern, efficient MPC protocols and ≥40% high-volume providers using hardware acceleration.

- **Hard conditions**:
  - Must preserve or improve current security levels and auditability; no “silent” downgrades to honest-but-curious
    assumptions without explicit scoping.  
    [Source: "MPC does have a single point of failure", Cubist, 2024]
  - Implementation must be compatible with heterogeneous chains, signing algorithms, and custody models.
  - Organizational capacity: 24-month program with mixed cryptography, infra, mobile, and SRE teams.

### 1.3 Extensibility and reframing

Reframing broadens the design space:

- **From "per-transaction latency" to "per-user signing budget"**:
  - Instead of optimizing every transaction equally, allocate latency and compute budget per user or per risk tier
    (e.g., instant flows for low-value, slower but stronger checks for high-value).  
    [Estimate: Based on tiered security design patterns in financial systems]

- **From "online signing only" to "precomputation and batching"**:
  - Pre-compute MPC partial signatures or randomness during idle periods; batch multiple user transactions into one
    ceremony to amortize fixed costs.  
    [Source: Threshold ECDSA batching and precomputation patterns, Gennaro & Goldfeder, 2018, https://eprint.iacr.org/2019/114]

- **From "CPU-only cryptography" to "accelerated cryptographic pipelines"**:
  - Treat ZKP generation, big-int arithmetic, and protocol orchestration as workloads for GPUs, FPGAs, or
    MPC-optimized HSMs rather than generic CPUs.  
    [Source: Cryptographic acceleration research, GPU/FPGA for ZK and big-int arithmetic, 2021–2023]

- **From "single global configuration" to "context-aware policies"**:
  - Tune protocol variants, network topology, and batching strategies per use case (e.g., trading vs. retail payments)
    instead of one-size-fits-all.

These reframings suggest solution clusters: protocol upgrades, infra/hardware optimization, workload shaping, and
product-level policy controls.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **Roles**:
  - Key-share holders / MPC nodes (wallet backend, custodial partners, HSMs).
  - Transaction initiators (end users, trading systems, treasury ops).
  - Coordinators / orchestrators (MPC coordinator services, scheduling and batching logic).
  - Cloud infrastructure providers and hardware vendors.

- **Resources**:
  - Cryptographic protocols: GG18/GG20, CGGMP21, FROST-style schemes, Ed25519 threshold.
  - Cryptographic primitives: Paillier encryption, elliptic curve arithmetic, ZKPs.
  - Compute resources: CPU cores, memory, GPUs, FPGAs, MPC-capable HSMs.
  - Network: bandwidth, latency characteristics, regional presence.
  - Monitoring and analytics: latency percentiles, error rates, energy metrics.

- **Processes**:
  - Key generation and refresh ceremonies.
  - Transaction signing flow (preprocessing, online signing, verification, broadcast).
  - Batching and queueing logic for high-volume flows.
  - Scaling and failover of MPC clusters.
  - Cost optimization (rightsizing, spot instances, hardware lifecycle management).

- **Rules and invariants**:
  - Threshold requirement (t-of-n parties must participate).
  - Security model (malicious vs. honest-but-curious, failure assumptions).
  - Compliance and audit requirements for institutional custody.

### 2.2 Balance and "degree"

Critical balances where "too much" turns harmful:

- **Security depth vs. latency and cost**:
  - Too little: weak or misconfigured MPC (e.g., honest-but-curious used where malicious required) → key theft risk.
  - Too much: maximal proofs, long key sizes, extremely distributed nodes → 10+ second latency and high cost.
  - Sweet spot: formally secure protocols with tuned parameters, partial acceleration, and risk-based controls.

- **Number of parties vs. coordination overhead**:
  - Too few parties: single-organization or collocated nodes undermine distributed trust goals.
  - Too many parties: protocol rounds explode; higher failure probability, worse latency.  
    [Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025]

- **Precomputation vs. online flexibility**:
  - Too little precomputation: peak-load latency spikes and under-utilized idle capacity.
  - Too much precomputation: wasted compute if transactions never arrive; complex inventory management of
    pre-signatures.

- **Hardware specialization vs. vendor lock-in**:
  - Too little specialization: leaving 2–5× performance on the table.  
    [Source: Cryptographic acceleration research for ZKPs and big-int arithmetic, 2021–2023]
  - Too much vendor-specific hardware: brittle supply chains, limited portability, higher capex risk.

### 2.3 Key internal causal chains

**Chain 1: Cryptographic complexity → Higher latency & cost → UX and profitability pressure**

```text
Paillier + ZKPs + multi-round protocols
  → Longer CPU-bound segments and multiple network RTTs per signing
  → p90 latency in seconds instead of milliseconds
  → Need for more and larger instances to keep up with throughput
  → Higher $/transaction and kWh/transaction
  → Pressure to either raise fees, weaken security, or avoid MPC altogether
```

[Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025]  
[Source: "A Compute Perspective of MPC-TSS: Paillier in ECDSA Revisited", Silence Laboratories, 2023]

**Chain 2: Naive infra + lack of batching → Under-utilization → Inefficient cost structure**

```text
No batching / precomputation
  → Each transaction pays full setup and network overhead
  → Low CPU utilization outside bursts, but high peak capacity provisioned
  → Over-provisioned clusters with poor cost elasticity
  → Cost per 1000 tx higher than necessary
```

[Estimate: Based on queueing theory and experience with crypto signing services; Medium confidence]

**Chain 3: Poor observability → Misaligned optimization → Fragile performance**

```text
Limited metrics on per-tx CPU time, kWh/1000 tx, per-segment latency
  → Optimization focused on crude metrics (e.g., average latency only)
  → Unnoticed bottlenecks in ZKPs, network, or scheduling
  → Changes that move bottlenecks rather than remove them
```

[Estimate: Based on common SRE anti-patterns in complex distributed systems]

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholder map

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|-------------|-----------|
| **Upstream** | MPC protocol designers, library maintainers, hardware vendors | Provide secure, efficient protocols and tooling; sell hardware; grow adoption | Research capacity, academic incentives, hardware lead times | May favor theoretical elegance or hardware sales over operational simplicity |
| **Downstream** | End users (retail, traders), exchanges, DeFi protocols | Fast, cheap, reliable signing UX with strong security | Limited willingness to pay; intolerance for long latency | Users may disable MPC or switch providers if UX poor |
| **Infrastructure** | Cloud providers, data centers, energy suppliers | Sell compute/network capacity; maintain SLAs | Power constraints, sustainability targets, multi-tenant security | Price changes and energy policies affect MPC economics |
| **Regulators / Auditors** | Financial regulators, security auditors | Ensure safe custody of assets, traceable controls | Slow standards, varying jurisdiction rules | Can require costly controls without performance awareness |
| **Internal teams** | Product, security, infra, finance | Balance UX, security, cost, and roadmap | Conflicting KPIs (e.g., growth vs. margin vs. risk) | Disagreements on acceptable trade-offs |

### 3.2 Environment factors

- **Regulatory and compliance**: Institutional MPC wallets must meet strict custody standards; any optimization that
  changes security assumptions may trigger re-audit or regulatory review.
- **Market competition**: Users can move to faster or cheaper wallets, even if they are less secure.
- **Hardware and energy markets**: GPU/FPGA pricing, data center energy costs, and sustainability targets can shift MPC
  cost structure materially over a 3–5 year horizon.
- **Blockchain ecosystem**: Underlying chains may (or may not) add protocol features that facilitate batching,
  off-chain signing proofs, or cheaper on-chain verification.

### 3.3 Responsibility & room to maneuver

- **Wallet providers**:
  - High responsibility for protocol selection, implementation quality, infra architecture, and UX.
  - Room to innovate on batching, precomputation, scaling, hardware acceleration, and risk-based policy.

- **Protocol designers and library maintainers**:
  - Responsible for correctness, security proofs, and providing efficient reference implementations.
  - Can offer APIs that expose precomputation, batching, and acceleration hooks.

- **Cloud and hardware vendors**:
  - Responsible for offering suitable instance types and acceleration options.
  - Can collaborate on tuned crypto workloads and pricing models.

- **Regulators/auditors**:
  - Responsible for setting clear expectations about acceptable security levels and performance trade-offs.
  - Limited room to design technical solutions but can encourage transparency and reporting on performance and energy.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

- **2017–2020: First practical threshold ECDSA deployments (GG18, related protocols)**  
  - High round complexity (e.g., 9 rounds for GG18) and heavy big-int arithmetic; deployed mainly for institutional
    custody where users tolerated 10+ second latency for high-value transactions.  
    [Source: "Fast Multiparty Threshold ECDSA", Gennaro & Goldfeder, 2018, https://eprint.iacr.org/2019/114]

- **2020–2022: Protocol efficiency improvements (GG20, CGGMP21)**  
  - CGGMP21 reduced the number of communication rounds and improved robustness; still required significant
    implementation work and migration from legacy stacks.  
    [Source: "UC Non-Interactive, Proactive, Threshold ECDSA", Canetti et al., 2021, https://eprint.iacr.org/2021/060]

- **2022–2024: Consumer MPC wallet growth and UX pressure**  
  - As MPC wallets targeted mainstream and trading users, 10-second latencies became unacceptable; traders sometimes
    disabled MPC entirely for performance.  
    [Source: "MPC does have a single point of failure", Cubist, 2024]

- **2023–2025: Hardware acceleration exploration**  
  - Some providers and research groups experimented with GPU/FPGA-based ZKP and big-int acceleration; early results
    showed 2–5× speedups for some proof systems but limited production adoption due to engineering complexity.  
    [Source: Cryptographic acceleration research for ZKPs and large integer arithmetic, 2021–2023]

### 4.2 Background vs. direct causes

- **Background (structural) causes**:
  - ECDSA’s multiplicative structure makes threshold variants inherently more complex than single-party signing.
  - Security expectations for custodial wallets are extremely high (billions in assets), biasing design toward more
    conservative protocols.
  - Cloud infra pricing and energy costs have historically been relatively cheap compared to lost-asset risk.

- **Direct causes**:
  - Widespread use of Paillier-based ZKPs and multi-round MPC protocols without aggressive optimization.
  - Limited precomputation, batching, or workload shaping in many production systems.
  - Underinvestment in observability for cryptographic hot paths (e.g., no fine-grained metrics for proof generation
    time, per-round network latency, or power draw).

### 4.3 Root issues

- **Mismatch between security goals and UX expectations**: Protocols were designed for institutional, low-frequency
  flows but are now used for high-frequency, consumer-grade interactions.
- **Incentive misalignment**: It is easier to sell "more secure" MPC than to justify multi-quarter investment in
  performance/energy optimization, until UX or margins become obviously unsustainable.
- **Limited specialization**: Few teams combine deep cryptography, high-performance computing, and SRE experience.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- **Performance**: Secure MPC signing remains in the multi-second range; providers under pressure either weaken
  security assumptions or lose latency-sensitive users.
- **Cost structure**: As volumes grow, infra cost scales roughly linearly with transaction volume unless batching and
  efficiency improvements are introduced; margins compress.
- **Ecosystem impact**: Traders and power users gravitate toward less secure but faster EOA or centralized solutions,
  undermining the original goal of safer key management.

### 5.2 Early signals

- Traders and DeFi users publicly complain about 5–10 second signing delays and workflows that “feel like Web1,” then
  switch to alternative wallets or disable MPC security features.  
  [Source: "MPC does have a single point of failure", Cubist, 2024]
- Some providers quietly use honest-but-curious or partially weakened modes to reach sub-3-second latency without
  disclosing all assumptions.  
  [Source: "MPC does have a single point of failure", Cubist, 2024]
- Hardware vendors and cloud providers start highlighting "crypto/MPC-friendly" SKUs, but with limited benchmarking
  transparency.

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**:
  - Coordinated investment in protocol migration (CGGMP21, FROST-type schemes), GPU/FPGA acceleration, and batching
    infrastructure delivers 3–5× performance improvements.
  - UX becomes competitive with hardware wallets for most flows; institutional security is preserved or improved.

- **Baseline scenario**:
  - Incremental optimizations yield 1.5–2× improvements; some providers modernize quickly, others lag.
  - Market fragments: a few leading MPC wallets become performance benchmarks; others remain slow and expensive.

- **Pessimistic scenario**:
  - Security shortcuts (e.g., honest-but-curious, centralized key shares) become the norm to hit UX targets.
  - One or more large incidents (breach or outage) erodes trust in MPC wallets as a category.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Cryptography talent**: Many leading MPC wallet providers already employ strong cryptographers and protocol
  engineers.
- **Cloud and hardware ecosystem**: GPUs, FPGAs, and HSMs with big-int acceleration are commercially available, even
  if not yet fully optimized for MPC workloads.
- **Operational maturity**: Established providers have SRE practices, CI/CD, and observability stacks that can be
  extended to include cryptographic and energy metrics.

### 6.2 Capability gaps

- **High-performance cryptographic engineering**: Few teams specialize in optimizing big-int/ZKP code for CPUs/GPUs
  and understanding microarchitectural trade-offs.
- **Energy and sustainability analytics**: Limited expertise in measuring and optimizing kWh/1000 tx at the level of
  individual cryptographic primitives.
- **Product-level cost modeling**: Many teams lack tools to translate low-level compute cost into pricing, tiering,
  or product decisions.

### 6.3 Buildable capabilities (1–6 months)

- Develop or adopt **reference benchmarks** for end-to-end MPC signing (latency, CPU time, energy, cost).
- Establish **joint working groups** between cryptography, infra, and product teams to own performance/energy OKRs.
- Pilot **hardware acceleration** in limited-scope environments (e.g., high-volume trading clusters) to build
  in-house expertise.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: MPC wallets introduced to mitigate key theft risk; first protocols optimized for security, not UX.
- **Problem**: Computationally expensive, multi-round protocols produce multi-second latency and high per-tx cost.
- **Analysis**: Internal trade-offs (security vs. performance vs. cost), external drivers (market, regulation), and
  capability gaps.
- **Options**: Protocol migration, batching and precomputation, infra/hardware acceleration, risk-based policies.
- **Risks**: Security regressions, capex over-investment, operational complexity, vendor lock-in.

### 7.2 Key judgments (needs validation)

1. **【P0】 Protocol modernization + batching can realistically deliver 3–5× throughput and 2–3× latency improvement
   without weakening security.**  
   [Estimate: Based on protocol round reduction (GG18→CGGMP21), batching efficiency, and GPU acceleration benchmarks]
2. **【P0】 Without explicit guardrails, market pressure will push some providers toward hidden security downgrades to
   meet UX expectations.**  
   [Source: "MPC does have a single point of failure", Cubist, 2024]
3. **【P1】 Hardware acceleration is economically justified for high-volume clusters but not necessarily for all
   deployments.**  
   [Estimate: Compare capex/opex against 2–5× performance gains and workload characteristics]
4. **【P1】 Measuring kWh/1000 tx and cost/1000 tx will reveal large optimization headroom that is currently invisible
   in aggregate metrics.**

### 7.3 Alternative paths (high-level)

- **Option A – Security-maximal, performance-tuned**: Maintain malicious security and geo-distribution, invest heavily
  in protocol modernization, batching, and acceleration.
- **Option B – Tiered security and UX**: Offer multiple security/latency tiers (e.g., low-value fast path, high-value
  slow path) with explicit trade-offs.
- **Option C – Minimal MPC**: Restrict MPC to highest-value flows, rely on EOAs or hardware wallets elsewhere to
  control costs.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- Over-optimism about performance gains achievable from protocol upgrades and hardware acceleration.
- Underestimation of engineering complexity and migration risk, especially for legacy GG18 stacks.
- Possible bias toward preserving MPC at all costs instead of considering narrower application scopes.

### 8.2 Required intelligence and data

- Fine-grained **profiling data** for representative signing flows: CPU time by cryptographic component, per-round
  network latency, error/retry rates.
- **Cost breakdown** per cluster: instance types, utilization, bandwidth, HSM fees, and storage.
- **Energy measurements**: kWh/1000 tx per cluster (e.g., using cloud energy APIs or measured power draw in dedicated
  environments).
- **User behavior data**: drop-off rates vs. latency buckets; willingness to pay for faster vs. more secure flows.

### 8.3 Validation plan

- Implement a **benchmarking harness** that can run typical transaction mixes through different protocol variants and
  infra configurations (baseline, CGGMP21, batching on/off, GPU on/off).
- Run **A/B tests** on selected user cohorts to compare UX and conversion for different latency and fee structures.
- Conduct **cost and energy audits** quarterly to track impact of optimization initiatives.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revision points

- Performance and cost estimates once real benchmarking and energy measurement data are available.
- Recommended degree of hardware acceleration given evolving GPU/FPGA/HSM pricing and availability.
- Balance between MPC and alternative custody models as the regulatory and threat landscape changes.

### 9.2 Incremental approach

- Start with **pilot clusters** (e.g., a trading-focused environment) to test protocol upgrades, batching, and
  acceleration before broad rollout.
- Introduce **feature flags** for protocol choices and batching strategies to allow controlled experiments.
- Maintain a **fallback path** to current stable configurations while validating new architectures.

### 9.3 "Good enough" criteria

- p90 latency <3 s and p99 <5 s for main user journeys.
- Documented and monitored cost/1000 tx and kWh/1000 tx within targets.
- No security downgrade relative to current malicious-security baselines, validated by external audit where relevant.

---

## 10. Summary & Action Recommendations

### 10.1 Core insights

1. MPC wallet computational overhead is driven by protocol-level cryptographic complexity and multi-round
   communication, not simply by inefficient code or hardware choices.
2. Without deliberate optimization, infra cost and energy use scale roughly linearly with volume, while UX remains
   significantly worse than EOAs and hardware wallets.
3. There is substantial headroom for improvement through protocol modernization (CGGMP21, FROST-like), batching and
   precomputation, hardware acceleration, and better workload shaping.
4. The main risk is hidden security downgrades driven by UX pressure; optimization must be explicitly security-first.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric (baseline → target) → Date**

1. **【P0】 Establish MPC performance and energy baseline**  
   → Infra + Cryptography teams  
   → Metrics: p90/p99 latency, CPU time/tx, kWh/1000 tx (baseline only)  
   → Date: 2026-03-31

2. **【P0】 Design and implement batching + precomputation for high-volume flows**  
   → Cryptography + Backend teams  
   → Metrics: Throughput (tx/min): 80 → 200; p90 latency: 8 s → 4 s  
   → Date: 2026-06-30

3. **【P1】 Prototype CGGMP21 or equivalent modern protocol in a test cluster**  
   → Cryptography team  
   → Metrics: Online signing rounds: 9 → 4; p90 latency improvement ≥30% vs. GG18 baseline  
   → Date: 2026-09-30

4. **【P1】 Evaluate GPU/FPGA/HSM acceleration for proof-heavy components**  
   → Infra + Cryptography teams  
   → Metrics: ZKP/Paillier operations speedup: 2–5×; cost/1000 tx impact quantified  
   → Date: 2026-09-30

5. **【P2】 Define tiered security/latency product offerings**  
   → Product + Security teams  
   → Metrics: Latency tiers (fast/standard/high-security) designed and documented; user comms drafted  
   → Date: 2026-06-30

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Security regression from protocol/infra changes | High | Medium | New protocol goes live without sufficient review; subtle implementation bugs | Formal review, reference implementations, external audits before production rollout | Cryptography Lead |
| Over-investment in specialized hardware | Medium | Medium | Acceleration yields lower-than-expected gains or utilization | Start with pilots, use cloud GPUs/FPGAs first, define clear ROI thresholds | Infra Lead |
| Unclear communication of trade-offs to users | Medium | Medium | Users unknowingly opt into weaker security modes for speed | Clear UI labels, docs, and opt-in flows for tiered security; default to secure modes | Product Lead |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Security-maximal, performance-tuned** | Strongest security posture, suitable for institutional and high-value flows; reputational advantage | Significant engineering and infra investment; complex deployment | Longer time-to-market; risk of incomplete migration | Institutional custody, high-value treasuries, regulated environments | Ultra-latency-sensitive retail or trading UX without tolerance for 2–3 s latency |
| **B. Tiered security and UX** | Aligns cost and latency with risk; offers choice to users | Requires product/UX work and clear comms; policy and monitoring complexity | Misconfiguration or user confusion can lead to unintended weak protection | Mixed user base with diverse risk/latency needs | Highly regulated environments where a single strict profile is mandated |
| **C. Minimal MPC scope** | Controls MPC cost by limiting to flows where it adds the most value; simpler infra | Reduced differentiating value of wallet; EOA or hardware flows must be secured separately | Perception that MPC is "optional" might reduce adoption; coordination overhead across custody models | When only subset of flows truly justify MPC’s complexity | When brand and strategy depend on "MPC everywhere" positioning |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **CGGMP21** | Modern threshold ECDSA protocol with fewer communication rounds (4 vs. 9 for GG18), designed for better efficiency and proactive security | N/A | [Source: "UC Non-Interactive, Proactive, Threshold ECDSA", Canetti et al., 2021] |
| **GG18** | Widely deployed threshold ECDSA protocol requiring multiple communication rounds for signing, used in early MPC wallets | N/A | [Source: "Fast Multiparty Threshold ECDSA", Gennaro & Goldfeder, 2018] |
| **Threshold ECDSA** | Multi-party protocol to generate standard ECDSA signatures without reconstructing the private key in any single location | N/A | Standard in institutional custody MPC wallets |
| **Paillier encryption** | Additively homomorphic public-key encryption scheme using large integer arithmetic; often used for secure multiplications in threshold ECDSA | N/A | [Source: Paillier, 1999; Silence Laboratories compute analysis, 2023] |
| **Zero-knowledge proof (ZKP)** | Cryptographic proof that a statement is true without revealing underlying secrets; used to enforce correct behavior of MPC parties | N/A | Used heavily in threshold ECDSA implementations |
| **p90 / p99 latency** | 90th / 99th percentile of end-to-end transaction signing latency; 90%/99% of requests complete within this bound | Seconds (s) | Common reliability and UX metric |
| **Throughput (tx/min)** | Number of successfully signed and broadcast transactions per minute for a given MPC cluster | tx/minute | Critical for trading and high-volume payment use cases |
| **kWh/1000 tx** | Energy consumption per 1000 successfully signed transactions, including compute and supporting infra | Kilowatt-hours per 1000 tx | Proposed metric for energy efficiency benchmarking |
| **HSM (Hardware Security Module)** | Dedicated hardware device that performs cryptographic operations with secure key storage and tamper-resistance | N/A | Often used as one of the MPC parties or for acceleration |
| **Signature batching** | Technique that amortizes fixed costs across multiple signatures by aggregating or reusing precomputed data | N/A | Key strategy to increase throughput and reduce cost/tx |
| **Honest-but-curious security model** | Threat model where parties follow protocol but may try to learn secrets from messages; weaker than malicious security | N/A | Sometimes (mis)used to justify removing expensive checks |
| **Malicious security** | Strong threat model where adversaries may arbitrarily deviate from protocol; preferred for institutional custody | N/A | Baseline expectation for high-value MPC deployments |

---

## 12. References

### Tier 1 Sources (Primary: Protocol Specifications, Academic Papers)

1. **Canetti, R., Gancher, N., Goldfeder, S., Makriyannis, N., and Peled, O.** (2021). *UC Non-Interactive, Proactive, Threshold ECDSA*. IACR ePrint 2021/060. https://eprint.iacr.org/2021/060  
   **Cited in**: Context Recap, Sections 1, 4, 5, 11.
2. **Gennaro, R., and Goldfeder, S.** (2018). *Fast Multiparty Threshold ECDSA with Fast Setup*. IACR ePrint 2019/114. https://eprint.iacr.org/2019/114  
   **Cited in**: Sections 1, 2, 4, 7, 11.

### Tier 2 Sources (Secondary: Industry Guides, Technical Blogs)

3. **Stackup**. (2025). *MPC Wallets: A Complete Technical Guide*. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide  
   **Cited in**: Context Recap, Sections 1–3, 4, 5.
4. **Cubist**. (2024). *MPC does have a single point of failure*. https://cubist.dev/blog/mpc-does-have-a-single-point-of-failure  
   **Cited in**: Context Recap, Sections 1, 4, 5, 7.
5. **Silence Laboratories**. (2023). *A Compute Perspective of MPC-TSS: Paillier in ECDSA Revisited*. https://silencelaboratories.com/blog-posts/a-compute-perspective-of-mpc-tss-paillier-in-ecdsa-revisited-2  
   **Cited in**: Context Recap, Sections 1, 2, 4, 11.
6. **CertiK**. (2023). *Exploring the Efficiency of MPC Algorithms in Crypto Wallets*. https://www.certik.com/resources/blog/kAlJM3qXwfnjWpjxYxpUn-exploring-the-efficiency-of-mpc-algorithms-in-crypto-wallets  
   **Cited in**: Background assumptions for MPC efficiency limits and protocol design choices.

### Infrastructure, Energy, and Optimization References

7. **Amazon Web Services**. (Accessed 2025-11-29). *AWS Pricing Calculator*. https://calculator.aws/  
   **Cited in**: Context Recap, Sections 2, 5.
8. **ARM Ltd.** (Accessed 2024). *ARM NEON Intrinsics Documentation*. https://developer.arm.com/architectures/instruction-sets/intrinsics/  
   **Cited in**: Assumptions on mobile cryptographic optimization potential.
9. **Major Cloud Providers (AWS, Google Cloud, Azure)**. (2023–2024). *Sustainability and Energy Use Reports* (various).  
   **Cited in**: Context Recap, Sections 2, 5.

### Internal and Estimate-Based Sources

10. **Operations & Cost Optimization Team**. (2025-11-29). *Computational Cost and Transaction Overhead in MPC Wallet Operations* (Problem statement and structured inputs).  
    **Cited in**: Context Recap, Sections 1, 3, 7, 10.
11. **Estimate: Infrastructure Cost and Energy Modeling for MPC Wallets**. Method: Combine AWS/GCP public pricing, typical cluster sizes (10–100 instances), and big-int CPU profiles; Confidence: Medium; Validation: Provider interviews and benchmarking.  
    **Used in**: Context Recap, Sections 2, 5, 7.
