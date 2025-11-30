# Transaction Signing Latency in MPC Wallets

**Last Updated**: 2025-11-30  
**Status**: Draft – Nine-Aspects Analysis  
**Owner**: Engineering Team / Architecture & Research

---

## Context Recap

- **Problem title**: Transaction Signing Latency in MPC Wallets
- **Current state**:
  - Threshold ECDSA/EdDSA protocols (GG18, GG20, CGGMP21, DKLs19, FROST, etc.) require multiple network rounds between key-share holders.
  - Real-world MPC wallets see **2–5 s** signing on good links and **10–30 s** on poor/mobile networks for multi-party configurations [Source: MPC Wallets: A Complete Technical Guide – Performance Benchmarks, Stackup, 2025].
  - Hardware wallets typically sign in **1–2 s** once connected; software EOAs complete signatures in **<100 ms** [Source: MPC Wallets: A Complete Technical Guide – Signing Speed Reality, Stackup, 2025].
  - Geographic distribution of key shares adds **1–2 s (same region)**, **3–5 s (cross-continent)**, **5–10 s (global)** of additional latency per transaction [Source: MPC Wallets: A Complete Technical Guide – Geographic Impact, Stackup, 2025].
- **Pain points**:
  - UX: 10–30 s confirmation windows are perceived as “broken” flows for consumer payments; users abandon or retry, causing **15–25% cart abandonment** for crypto payments (estimate based on general e-commerce latency benchmarks).
  - Throughput: Typical MPC deployments handle **10–20 tx/min (consumer)** and **50–100 tx/min (enterprise)**; this is insufficient for high-frequency trading (HFT), MEV extraction, or market-making that need hundreds–thousands of tx/min [Source: MPC Wallets: A Complete Technical Guide – Throughput Constraints, Stackup, 2025].
  - Market fit: HFT strategies often require total path latencies below **100 ms**; even optimized 2–3-round MPC is hard to fit into that budget over non-local networks [Estimate: based on common colocation/HFT latency budgets in traditional finance].
- **Goals**:
  - Reduce MPC signing latency from **2–5 s → <1 s (min)** / **<500 ms (target)** / **<200 ms (ideal)** on good networks for same-region deployments.
  - Reduce poor-network latency from **10–30 s → <3 s (min)** / **<2 s (target)** / **<1 s (ideal)**.
  - Reduce signing rounds from **4–9 → 2–3 (target)** / **1–2 (ideal)** via protocol and architecture changes.
  - Lower cart abandonment from estimated **15–25% → <10% (min)** / **<5% (target)** for payment flows.
- **Hard constraints**:
  - Cannot remove multi-round communication entirely without undermining MPC security [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020].
  - Must maintain security guarantees comparable to CGGMP21/FROST, including resistance to adaptive corruptions and threshold attacks [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020; FROST, Komlo & Goldberg, 2020].
  - Must preserve existing key-share material and be backward-compatible with production MPC wallet deployments.
  - Budget: **$300K–$800K** over ~6 months; team: **2–3 cryptographers, 3–4 protocol engineers, 1–2 network specialists**.
- **Key facts**:
  - CGGMP21 achieves **4-round** threshold ECDSA signing, with **3 rounds movable to preprocessing**, enabling an effectively non-interactive online phase in some settings [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020].
  - FROST supports **2-round** and even effectively **1-round** Schnorr-style threshold signatures given preprocessing, specifically designed to minimize network rounds [Source: FROST: Flexible Round-Optimized Schnorr Threshold Signatures, Komlo & Goldberg, 2020].
  - Modern TSS/MPC deployments (e.g., Dynamic) already achieve dozens–hundreds of signatures per second in optimized environments, showing that the bottleneck is often network RTT and architecture more than raw cryptographic cost [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].
  - Google/SOASTA research shows that mobile page complexity and performance strongly correlate with conversions; slower or heavier pages lead to significantly lower conversion rates [Source: Why marketers should care about mobile page speed, Google/SOASTA Research, 2016].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

- **Core problem**: MPC wallets incur **multi-second signing latency** due to multi-round, network-bound protocols, degrading UX and preventing latency-sensitive use cases like HFT and certain DeFi strategies [Source: MPC Wallets: A Complete Technical Guide – Performance Benchmarks, Stackup, 2025].
- **Key contradictions**:
  - **Security vs. latency**: Increasing rounds and geographic separation improves security (more robust threshold, better fault tolerance) but adds RTT-bound latency. Reducing rounds or collocating shares improves speed but can erode security assumptions [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020].
  - **Global resilience vs. UX**: Globally distributed shares protect against correlated failures and jurisdictional risk, but add **3–10 s** of overhead compared with same-region deployments [Source: MPC Wallets: A Complete Technical Guide – Geographic Impact, Stackup, 2025].
  - **Abstraction vs. control**: Many integrators treat MPC wallets as black-box signing services, limiting their ability to optimize routing, concurrency, or precomputation.
- **Stakeholder tensions**:
  - Traders and payment users demand near-instant signing.
  - Risk/compliance/legal functions prefer more separation and redundancy.
  - Wallet providers must maintain high uptime and safety across heterogeneous client networks.

### 1.2 Goals & conditions

- **Latency targets** (same-region, typical network):
  - Baseline: 2–5 s signing.
  - Minimum acceptable: **<1 s** end-to-end (95th percentile) for standard DeFi/payments.
  - Target: **<500 ms** p95 for same-region MPC clusters.
  - Ideal: **<200 ms** p95 for high-value flows, enabling some near-real-time strategies.
- **Latency targets (high-latency/mobile)**:
  - Baseline: 10–30 s signing.
  - Minimum acceptable: **<3 s** p95.
  - Target: **<2 s**; ideal: **<1 s** p95.
- **Project constraints**:
  - Timeline: Q1–Q3 2025 (6 months).
  - Budget: $300K–$800K (includes research, prototyping, infra, and validation).
  - Backward compatibility: No forced key migration; changes must work with existing shares and keys.

### 1.3 Extensibility & reframing

- **Alternative framings**:
  - From **“MPC signing latency is too high”** → **“End-to-end confirmation latency is too high”**. This reframing includes: app-side queuing, transaction construction, relay, network routing, and user interface feedback.
  - From **“MPC cannot support HFT”** → **“Which subset of HFT-like strategies can be supported with <200–500 ms MPC latency in regional clusters?”**
  - From **“global MPC is slow”** → **“Where do we actually need global distribution vs. regional clusters plus disaster recovery procedures?”**
- **Attribute-based expansion**:
  - **Object**: MPC signing service.
  - **Attributes**: protocol rounds, RTT, concurrency, precomputation efficiency, colocation strategy, fallback paths, caching of partial computations.
  - **Objects with shared attribute**: any distributed signing or consensus protocol (e.g., multisig, BFT consensus, rollup sequencers) with similar latency–security trade-offs [Source: FROST, Komlo & Goldberg, 2020; UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Cryptographic protocols**: GG18, GG20, CGGMP21 (ECDSA), DKLs19 (2-party ECDSA), FROST (EdDSA/Schnorr) [Source: MPC Wallets: A Complete Technical Guide – Cryptographic Protocols, Stackup, 2025; UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020; FROST, Komlo & Goldberg, 2020].
- **Network fabric**: public internet, mobile networks, VPNs, private links, load balancers.
- **Key-share infrastructure**: HSMs, secure enclaves, TEEs, cloud KMS, or software key stores.
- **Orchestration layer**: coordinators, signing services, routing/selection algorithms, retry and timeout logic.
- **Client applications**: DeFi frontends, trading systems, consumer wallets, custodial platforms.

### 2.2 Balance & “degree”

- **Number of rounds vs. robustness**:
  - Fewer rounds → less surface for abort/failure but sometimes weaker or newer security assumptions.
  - More rounds → stronger robustness properties (e.g., identifiable abort, proactive refresh) but worsen total latency [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020].
- **Geographic distribution vs. latency**:
  - Same-region: +1–2 s overhead, acceptable for many consumer flows.
  - Cross-continental: +3–5 s overhead, borderline for payments.
  - Global: +5–10 s overhead, effectively incompatible with low-latency trading [Source: MPC Wallets: A Complete Technical Guide – Geographic Impact, Stackup, 2025].
- **Precomputation vs. resource usage**:
  - Aggressive offline precomputation (nonces, partial signatures) reduces online latency but consumes CPU/storage and may waste work when transactions don’t materialize [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].

### 2.3 Causal chains (simplified)

1. **Network RTT → Rounds → Latency**:
   - Per-signature latency ≈ `rounds × RTT + local_compute`. With 4–9 rounds and RTT in the 100–200 ms range (mobile or cross-continental), latency naturally falls into multi-second ranges [Estimate: based on CGGMP21/FROST round counts and typical internet RTTs].
2. **Latency & complexity → Conversion & abandonment**:
   - Google/SOASTA models show that heavier, slower mobile sites correlate with significantly lower conversion rates; complexity (page weight, images, scripts) is a key negative driver [Source: Why marketers should care about mobile page speed, Google/SOASTA Research, 2016].
   - By analogy, each extra second of perceived “waiting for signature” increases the probability that users abandon or retry payment flows.
3. **Provider architecture → Throughput limits**:
   - If each MPC cluster handles only 10–20 tx/min, large custody providers require many clusters or must throttle flows [Source: MPC Wallets: A Complete Technical Guide – Throughput Constraints, Stackup, 2025].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders & interactions

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream (Users: traders, payers) | Initiate signing requests via wallets or trading systems | Fast, reliable confirmation (<1–3 s for consumer, sub-second for trading) | Limited control over network quality; limited patience | Demand speed that may conflict with security-driven latency |
| Upstream (Integrating developers) | Integrate MPC wallet SDKs/APIs | Predictable SLAs, simple APIs, clear error modes | Little visibility into MPC internals; must support multiple chains | Need higher-level abstractions while providers want fine-grained control |
| Downstream (Wallet providers) | Operate MPC infrastructure | Maintain security, uptime, and cost efficiency | Regulatory constraints, multi-tenant risk, budget | May prioritize security over latency or infra cost over aggressive optimization |
| Downstream (DeFi protocols & exchanges) | Consume signed transactions | High throughput, low-latency settlement | Cannot easily change contract logic for slow signers | May see MPC users as uncompetitive vs. EOAs/hardware |
| Sideline/External (Regulators, auditors) | Oversee custody/security posture | Robust separation of duties, geographic/jurisdictional diversity | Limited tolerance for simplifying security controls | Prefer strong distribution that increases latency |

### 3.2 Environment factors

- **Market competition**:
  - Smart contract wallets and hardware wallets are improving in UX and security, reducing MPC’s relative advantages for many use cases [Source: MPC Wallets: A Complete Technical Guide – Hybrid Approaches, Stackup, 2025].
  - Exchanges and L2s introduce native features (e.g., account abstraction, session keys) that reduce the need for slow external signing services.
- **Technology trends**:
  - TEEs and hardware acceleration can reduce CPU cost per signature but do not fully remove RTT-bound latency [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].
  - New threshold schemes (e.g., FROST and successors) push toward 1–2 effective network rounds [Source: FROST, Komlo & Goldberg, 2020].
- **UX norms**:
  - Modern mobile UX guidelines often target **<2–3 s** for key interactions; beyond that, bounce and abandonment rates increase sharply [Source: Why marketers should care about mobile page speed, Google/SOASTA Research, 2016].

### 3.3 Responsibility & room for maneuver

- **Where MPC providers should take proactive responsibility**:
  - Selecting and implementing more efficient threshold schemes.
  - Designing region-aware routing and latency-aware signer selection.
  - Providing clear latency SLAs and monitoring tools to integrators.
- **Where others need flexibility**:
  - Traders may choose to bypass MPC for the most latency-sensitive strategies.
  - Compliance functions may choose stricter geodiversity for certain high-risk accounts, accepting slower signing intentionally.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **Pre-2018**: Early threshold ECDSA schemes with high communication cost; MPC mostly academic, not widely deployed in wallets [Source: UC Non-Interactive, Proactive, Threshold ECDSA – Background, Canetti et al., 2020].
2. **2018–2020**: GG18 (9 rounds) and GG20 (6 rounds) become practical foundations for MPC wallets, but still carry noticeable latency overhead [Source: MPC Wallets: A Complete Technical Guide – Cryptographic Protocols, Stackup, 2025].
3. **2020–2021**: CGGMP21 reduces ECDSA signing to 4 rounds with preprocessing; FROST introduces 2-round/1-round options for Schnorr signatures [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020; FROST, Komlo & Goldberg, 2020].
4. **2022–2024**: Providers like Dynamic deploy optimized TSS-MPC stacks using DKLs19/FROST-like schemes, and CPU becomes less of a bottleneck; network and architecture dominate latency [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].

### 4.2 Background vs. direct causes

- **Background causes**:
  - Fundamental complexity of threshold ECDSA/EdDSA.
  - Internet latency and last-mile variability, especially on mobile.
  - Legacy assumptions that signing can be “a little slow” as long as it is safe.
- **Direct triggers**:
  - Growth in **DeFi TVL** and **on-chain trading volume** pushes latency-sensitive use cases into MPC wallets (e.g., sophisticated traders wanting MPC custody) [Source: Total Value Locked – DeFiLlama documentation, DeFiLlama, 2024].
  - User expectations shaped by Web2 and fast L2s; multi-second waits feel unacceptable.

### 4.3 Root issues

- Architectural conflation of **global resilience** with **all-flows default**: even low-risk consumer flows may be routed through globally distributed signers.
- Underinvestment in **precomputation strategies**, **latency-aware routing**, and **application-level feedback**.
- Lack of product-level SLAs and metrics that treat latency as a first-class feature, not an implementation detail.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory if unchanged

- MPC wallets remain the default for high-security custody, but:
  - Latency-sensitive traders and DeFi protocols increasingly avoid MPC or restrict MPC accounts to slow paths only.
  - Smart contract wallets (account abstraction) and hardware wallets gain share by offering superior UX and adequate security for many users [Source: MPC Wallets: A Complete Technical Guide – Hybrid Approaches, Stackup, 2025].
  - Cart abandonment and failed payment flows remain elevated where MPC signing sits in the critical path.

### 5.2 Early signals

- Integrators requesting **“fast mode”** or single-region configurations.
- Traders moving volume from MPC custodial accounts to hot EOAs just to meet latency requirements.
- Support tickets describing “stuck” or “spinning” transaction confirmations corresponding to 10–30 s MPC signing delays.

### 5.3 6–24 month scenarios

- **Optimistic** (with intervention):
  - Adoption of FROST-like protocols and aggressive precomputation yields **<500 ms** p95 in same-region clusters; poor connections are improved to **<2–3 s**.
  - MPC wallets remain competitive for both custody and some active trading use cases.
- **Baseline** (partial fixes):
  - Incremental optimizations shave off **20–40%** latency but many global deployments still see 5–10 s signing; MPC is relegated to slower flows.
- **Pessimistic** (no material change):
  - MPC seen primarily as a slow, “cold storage” technology.
  - Smart contract wallets and hardware dominate active user flows; MPC providers lose high-value segments.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- Deep cryptography expertise in-house or via research partners (existing CGGMP21/FROST/DKLs19 deployments).
- Established infrastructure for secure key management and incident response.
- Relationships with exchanges, DeFi protocols, and institutional clients, enabling controlled pilots.

### 6.2 Capability gaps

- Limited specialization in **network and systems performance engineering** versus cryptography.
- Limited product management focus on latency SLAs and UX instrumentation.
- Limited experience with **geo-routing**, **Anycast**, or edge computing specifically tailored for MPC.

### 6.3 Buildable capabilities (1–6 months)

- Hire/contract **1–2 network performance engineers** to focus on RTT reduction and routing.
- Upskill protocol team on FROST and related low-round threshold schemes via targeted study and prototypes [Source: FROST, Komlo & Goldberg, 2020].
- Build joint taskforce with product & UX to design UX patterns for queued signing, progress indicators, and fallbacks informed by Google/SOASTA conversion research [Source: Why marketers should care about mobile page speed, Google/SOASTA Research, 2016].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline (summary)

1. Background: MPC protocols inherently require multiple rounds.
2. Problem: RTT × rounds cause multi-second signing latency; global distribution exacerbates this.
3. Analysis: Round-minimizing schemes + precomputation + network optimization can materially improve latency.
4. Options: (A) Protocol upgrade + precomputation, (B) Network & routing optimization, (C) UX-layer mitigation and tiered security modes.
5. Risks: Security regressions, implementation complexity, misaligned expectations.

### 7.2 Key judgments (to validate)

- **【P0】** HFT-grade latency (<100 ms) is unattainable for most multi-party MPC over the public internet; such use cases should use alternative architectures.
- **【P0】** Same-region RTT optimization plus 2–3-round protocols and aggressive precomputation can achieve **<500 ms** p95 for many flows.
- **【P1】** User abandonment for payment flows will drop significantly once median confirmation is **<2–3 s** and UX clearly communicates progress [Source: Why marketers should care about mobile page speed, Google/SOASTA Research, 2016].
- **【P1】** Global, fully distributed signer topologies should be restricted to high-risk accounts and cold paths.

### 7.3 Alternative high-level paths

- **Option A – Protocol-First Optimization**: Upgrade signing to FROST/CGGMP21 with offline precomputation and multi-signature batching.
- **Option B – Network & Topology Optimization**: Regional clusters, latency-aware signer selection, Anycast routing, dedicated links for key shares.
- **Option C – UX & Product-Layer Mitigation**: Session keys, batched approvals, and progressive disclosure to hide raw signing latency from users.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Security conservatism bias**: Overweighting worst-case adversaries could block reasonable latency improvements.
- **Engineering optimism bias**: Assuming new schemes and topologies can be implemented flawlessly on tight timelines.
- **Analogy bias**: Over-applying Web2 performance heuristics (web page speed) to on-chain signing without direct measurement.

### 8.2 Required intelligence

- Empirical **latency distributions** by region, device type, and network for current MPC deployments (p50/p95/p99 per flow).
- A/B tests on **UX variants** (e.g., “pre-authorized session keys vs. per-tx signing”) to measure impact on conversion and abandonment.
- Benchmarks comparing GG18/GG20/CGGMP21/FROST implementations under controlled RTT conditions [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020; FROST, Komlo & Goldberg, 2020].

### 8.3 Validation plan

- **Step 1 – Measurement (Month 1)**:
  - Instrument end-to-end latency: client tap → chain inclusion, decomposed into: client, network, MPC, relay, mempool confirmation.
- **Step 2 – Lab Protocol Benchmarking (Months 1–2)**:
  - Implement reference CGGMP21 and FROST signers in a controlled environment and benchmark across synthetic RTT profiles.
- **Step 3 – Pilot Regional Clusters (Months 2–4)**:
  - Deploy same-region signer clusters and measure latency uplift versus global baseline for selected user cohorts.
- **Step 4 – UX A/B Tests (Months 3–5)**:
  - Test different UX patterns and session mechanisms; measure completion and abandonment rates versus latency.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Revised expectations for **HFT suitability** once real-world benchmarks are available.
- Updated **round-minimization strategy** if new protocols (e.g., improved FROST variants) or hardware primitives (new TEEs) become production-ready.

### 9.2 Incremental approach

- Start with **metrics and observability**; avoid redesigning protocols before measuring.
- Roll out changes **region by region** and **cohort by cohort** to isolate impact and reduce blast radius.

### 9.3 “Good enough” criteria

- For consumer payments: **p95 confirmation <3 s**, abandonment reduced below **10%** for crypto checkout.
- For active DeFi users: **p95 <1 s** for at least a subset of flows using regional clusters and/or session keys.
- For custody: clear segmentation between high-latency, high-security paths and faster, constrained-risk paths.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. MPC signing latency is dominated by **network RTT × protocol rounds**, not raw cryptographic computation.
2. Existing schemes (CGGMP21, FROST) and improved architectures can likely reduce same-region latency to **<500 ms** p95 for many flows, but **sub-100 ms HFT** over public networks is unrealistic.
3. Latency-sensitive use cases should be **explicitly segmented** and may require alternative architectures (smart contract wallets, hardware, session keys).
4. UX and product-layer design significantly influence user-perceived latency and conversion, not just underlying MPC speed [Source: Why marketers should care about mobile page speed, Google/SOASTA Research, 2016].

### 10.2 Near-term action list (0–3 months)

- **【P0 – Critical】 Implement detailed latency observability** → Eng Lead  → Metric: % of flows with full latency breakdown captured: 0% → 95% → by 2025-02-15.
- **【P0 – Critical】 Prototype low-round protocol path (CGGMP21/FROST)** → Crypto Lead → Metric: Lab p95 signing latency at 100 ms RTT: 2–5 s → <500 ms → by 2025-03-31 [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020; FROST, Komlo & Goldberg, 2020].
- **【P1 – Important】 Deploy regional signer clusters for selected markets** → Infra Lead → Metric: p95 latency for selected cohort: 2–5 s → <1 s → by 2025-04-30 [Source: MPC Wallets: A Complete Technical Guide – Geographic Impact, Stackup, 2025].
- **【P1 – Important】 Design UX for session-based approvals** → Product & UX → Metric: Payment flow abandonment: 15–25% (est.) → <10% → by 2025-04-30 [Source: Why marketers should care about mobile page speed, Google/SOASTA Research, 2016].
- **【P2 – Optional】 Explore TEEs/accelerators for selective flows** → Research Lead → Metric: CPU cost per signature: baseline → −30% → by 2025-05-31 [Source: The Evolution of MPC, Dynamic, 2024].

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Security regression from new protocols | High | Medium | Vulnerabilities or side-channel concerns discovered in implementation | Keep reference implementation simple; engage external cryptography audits; stage rollout | Crypto Lead |
| Latency improvements insufficient for HFT | Medium | High | Benchmarks show p95 >300–500 ms even after optimizations | Clearly position MPC as unsuitable for most HFT; offer alternative architectures | Product Lead |
| Operational complexity of multi-topology deployments | Medium | Medium | Frequent configuration errors or outages | Standardize deployment templates; automation; clear runbooks | Infra Lead |
| Misaligned stakeholder expectations | Medium | Medium | Clients expect “instant” MPC signing without trade-off understanding | Publish clear SLAs, docs, and reference architectures; include trade-off charts | Product & BD |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Protocol-First Upgrade (CGGMP21/FROST)** | Large latency reduction from fewer rounds; long-term strategic advantage | High R&D, audit, and migration costs | Implementation bugs; security regressions | When cryptography team is strong and budget permits | When team lacks capacity or risk appetite for deep crypto change |
| **B. Network/Topology Optimization** | Faster wins; lower engineering risk; reuses existing protocols | Infra complexity; needs traffic engineering skills | Diminishing returns if RTT floors are high | When infra & SRE team is strong; regions with clear clusters | When users are globally scattered with no dominant region |
| **C. UX & Session-Key Focus** | Improves perceived latency; less invasive on infra | More complex key lifecycle; new UX surfaces | Misuse of session keys; security trade-offs if not carefully scoped | Consumer wallets, checkout flows, moderate-risk accounts | Ultra-high-security custody, institutional accounts with strict policies |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **MPC (Multi-Party Computation)** | Cryptographic technique enabling parties to compute on private inputs without revealing them individually | N/A | Used for distributed key management and signing [Source: The Evolution of MPC, Dynamic, 2024] |
| **Threshold signature** | Signature scheme where any subset of at least *k* out of *n* parties can jointly produce a valid signature | N/A | Core primitive for MPC wallets [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020] |
| **CGGMP21** | 4-round threshold ECDSA protocol with preprocessing for non-interactive online signing | N/A | Proposed by Canetti et al. 2020 [Source: UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020] |
| **FROST** | Flexible Round-Optimized Schnorr Threshold signatures supporting 2-round or 1-round online signing with preprocessing | N/A | Used for EdDSA/Schnorr-style schemes [Source: FROST, Komlo & Goldberg, 2020] |
| **EOA (Externally Owned Account)** | Single-key blockchain account model where one private key controls the account | N/A | Baseline for “instant” signing in many ecosystems |
| **p95 latency** | Time under which 95% of requests complete; common performance metric | ms or s | Used as primary latency KPI in this analysis |
| **RTT (Round-Trip Time)** | Time for a message to go from client to server and back | ms | Each MPC round typically incurs at least one RTT |
| **Signing rounds** | Number of sequential message-exchange steps required by a protocol to produce a signature | Count (integer) | Directly multiplies with RTT to yield latency |
| **Precomputation (offline phase)** | Performing parts of a protocol’s work before the message is known, to reduce later online latency | N/A | Used in CGGMP21 and FROST [Source: UC Non-Interactive, Proactive, Threshold ECDSA, 2020; FROST, 2020] |
| **Throughput** | Number of signatures or transactions a system can process per unit time | tx/min or tx/s | MPC wallets often limited to 10–100 tx/min per cluster [Source: MPC Wallets: A Complete Technical Guide – Throughput Constraints, Stackup, 2025] |
| **Cart abandonment** | Percentage of initiated checkout or payment sessions that are not completed | % | Increases with page weight and slow performance [Source: Why marketers should care about mobile page speed, Google/SOASTA Research, 2016] |
| **Session key** | Short-lived key or authorization token allowing multiple operations without re-running full MPC signing each time | N/A | UX strategy to amortize latency over multiple actions |

---

## 12. References

### Tier 1 – Cryptography & Protocols

1. **Canetti, R., Makriyannis, N., & Peled, U.** (2020). *UC Non-Interactive, Proactive, Threshold ECDSA*. Cryptology ePrint Archive, Paper 2020/492. https://eprint.iacr.org/2020/492 **[Cited in: Context Recap, 1.1, 2.2, 4.1, 8.2, 10.2, 11]**
2. **Komlo, C., & Goldberg, I.** (2020). *FROST: Flexible Round-Optimized Schnorr Threshold Signatures*. Cryptology ePrint Archive, Paper 2020/852. https://eprint.iacr.org/2020/852 **[Cited in: Context Recap, 2.1, 3.2, 4.1, 6.3, 8.2, 10.2, 11]**

### Tier 2 – Industry Guides & Blogs

3. **Stackup.** (2025). *MPC Wallets: A Complete Technical Guide*. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide **[Cited in: Context Recap, 1.1, 2.1–2.3, 3.2, 4.1, 5.1, 10.2, 11]**
4. **Dynamic.** (2024). *The Evolution of MPC: From Secure but Slow to Fast and Scalable*. https://www.dynamic.xyz/blog/the-evolution-of-mpc **[Cited in: Context Recap, 2.3, 3.2, 4.1, 6.3, 10.2, 11]**

### Tier 2 – UX & Conversion Research

5. **Google / SOASTA Research.** (2016). *Why marketers should care about mobile page speed*. Think with Google. https://business.google.com/ca-en/think/marketing-strategies/mobile-page-speed-load-time/ **[Cited in: Context Recap, 2.3, 3.2, 7.2, 10.1–10.2, 11]**

### Tier 2 – Market & Ecosystem Context

6. **DeFiLlama.** (2024). *Total Value Locked – DeFiLlama Wiki*. https://wiki.defillama.com/wiki/Total_value_locked **[Cited in: 4.2]**

### Internal / Estimates

7. **Internal Latency Benchmarks & User Analytics.** (2024–2025). *MPC Wallet Signing Latency and Abandonment Metrics*. Engineering dashboards and logs. **[Planned for: 2.3, 5.1, 8.2]**
8. **Latency & HFT Requirements Estimate.** Method: synthesis of public HFT literature and exchange co-location specs. Confidence: Medium. Validation: Benchmark MPC-based strategies vs. non-MPC in test environments. **[Used in: Context Recap, 1.1, 7.2, 9.1]**
