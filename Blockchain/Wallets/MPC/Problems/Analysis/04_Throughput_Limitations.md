# Network Throughput Limitations in MPC Signing

---

## Context Recap

- **Problem title**: Network Throughput Limitations in MPC Signing
- **Current state**:
  - Consumer MPC wallets: ~10–20 transactions per minute (TPM) on typical mobile/consumer setups [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Throughput Constraints"].
  - Enterprise MPC deployments: ~50–100 TPM under optimized server infrastructure [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Throughput Constraints"].
  - Highly optimized specialized setups: rarely exceed ~500 TPM due to multi-round coordination and network overhead [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Throughput Constraints"].
  - By contrast, EOAs and hot wallets can sign essentially CPU‑bound at thousands of TPS, and hardware wallets typically sign within 1–2 seconds per transaction once connected [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Signing Speed Reality"].
- **Pain points**:
  - Inability to support high‑frequency trading (HFT), MEV extraction, automated market making (AMM), and mass payment workloads that require thousands of transactions per minute and sub‑second latency [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025, "High-Frequency Trading"; Source: Low-Latency Trading, Hasbrouck & Saar, 2013, Journal of Financial Markets].
  - Institutional users either fall back to less secure hot wallets or abandon MPC, limiting MPC’s share of institutional crypto infrastructure.
  - Queue buildup and unpredictable tail latency during traffic spikes (market volatility, airdrops, payroll windows) create operational risk and missed revenue.
- **Goals** (from problem statement, refined):
  - **Consumer MPC**: 10–20 TPM → 100 TPM (min) / 300 TPM (target) / 600 TPM (ideal) by Q4 2025.
  - **Enterprise MPC**: 50–100 TPM → 500 TPM (min) / 1,500 TPM (target) / 3,000 TPM (ideal) by Q4 2025.
  - **High-performance institutional / HFT**: 500 TPM → 3,000 TPM (min) / 6,000 TPM (target) / 10,000+ TPM (ideal) by Q1 2026.
  - **Adoption**: Enable ≥20% (min) / ≥40% (target) / ≥60% (ideal) of HFT and AMM flows to run on MPC wallets by Q4 2025 (from current ≈0%).
- **Hard constraints**:
  - Cannot remove multi‑round interaction and threshold security from MPC / TSS protocols [Source: Threshold ECDSA Documentation, DFINITY Foundation, 2024, Internet Computer Docs; Source: Threshold ECDSA in Three Rounds, Doerner et al., 2023, IACR ePrint 2023/765].
  - Network latency and bandwidth (1–10 Gbps typical DC links; 50–200 ms RTT across continents) impose hard lower bounds on per‑round communication time [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024; Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025].
  - CPU cost of ECDSA/EdDSA signing and precomputation remains significant even with elliptic‑curve optimizations [Source: Multiparty Computation from Somewhat Homomorphic Encryption (SPDZ), Damgård et al., 2012, ePrint 2012/642; Source: Fast Two-Party Threshold ECDSA with Proactive Security, ePrint 2024/1831].
  - Budget: roughly $0.8M–$2M across cryptography R&D, infra scaling, and benchmarking (per problem statement, treated as an internal constraint) [Source: Network Throughput Limitations in MPC Signing, Infrastructure Team, 2025-11-29].
- **Key facts from inputs**:
  - Today’s MPC throughput (10–500 TPM, i.e., ~0.17–8.33 TPS) is 1–3 orders of magnitude below HFT and AMM needs (1,000–10,000 TPS) [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025].
  - Past attempts (parallelization via more shares, batching, TEEs, offline/online splitting) have produced incremental (20–60%) but not order‑of‑magnitude improvements [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].

---

## 1. Problem Definition

### 1.1 Problem & contradictions

**Core contradiction**: We want **institutional‑grade, threshold‑secure MPC signing** and **HFT‑grade throughput/latency** at the same time. The very properties that make MPC secure (multi‑round, multi‑party interaction, geographic distribution, threshold access) directly erode throughput and latency.

- **Security vs. speed**
  - MPC / TSS protocols require several rounds of interaction between t‑of‑n parties; each round incurs at least one WAN RTT [Source: Threshold ECDSA in Three Rounds, Doerner et al., 2023, IACR ePrint 2023/765].
  - HFT and AMM strategies operate on millisecond scales and thousands of orders per second; every additional 10–100 ms of latency degrades edge and reduces captured alpha [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025; Source: Low-Latency Trading, Hasbrouck & Saar, 2013, Journal of Financial Markets].

- **Distributed resilience vs. coordination overhead**
  - More key shares and more geographically diverse nodes improve censorship resistance and fault tolerance, but increase network complexity and coordination failures.
  - Some threshold protocols are O(n²) in communication per round, making scaling out signers more expensive than linear [Source: Multiparty Computation from Somewhat Homomorphic Encryption (SPDZ), Damgård et al., 2012, ePrint 2012/642].

- **Cost ceiling vs. infra scale**
  - Enterprise MPC pricing around ~$0.02/signature constrains how much CPU, GPU/FPGA, and network bandwidth providers can dedicate per transaction [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Popular MPC Wallet Providers"].
  - HFT‑grade infra often justifies far higher per‑trade spend, but that cost is borne by traders, not custody providers; incentives are misaligned.

### 1.2 Goals & conditions

- **Throughput targets** (reframed as capacity per signing cluster):
  - Consumer: ≥300 TPM mid‑term (5×–15× over baseline).
  - Enterprise: ≥1,500 TPM mid‑term (15×–30× over baseline).
  - HFT / specialized: ≥6,000–10,000+ TPM (12×–20× over current 500 TPM ceiling) [Source: Network Throughput Limitations in MPC Signing, Infrastructure Team, 2025-11-29; Estimate: extrapolating from current 500 TPM upper bound, Medium confidence].

- **Latency envelopes** (for typical and tail):
  - DeFi market making & AMM routing: p95 signing latency ≤500–1,000 ms; p99 ≤2,000 ms [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025; Estimate: mapping DeFi strategies to traditional MM/arb latency expectations].
  - HFT & MEV: p95 ≤100–200 ms; p99 ≤500 ms end‑to‑end signing + submission, which is extremely aggressive for multi‑round MPC and likely requires hybrid designs [Source: Low-Latency Trading, Hasbrouck & Saar, 2013, Journal of Financial Markets].

- **Non‑functional constraints**:
  - Maintain at least current security margins of state‑of‑the‑art threshold ECDSA / EdDSA protocols (no downgrade to weaker assumptions) [Source: Fast Two-Party Threshold ECDSA with Proactive Security, ePrint 2024/1831].
  - Preserve compatibility with existing blockchains that expect ECDSA/EdDSA signatures (Bitcoin, Ethereum, EVM L2s) [Source: Threshold ECDSA Documentation, DFINITY Foundation, 2024].
  - Delivery window: meaningful production improvements within 12 months (Q1 2025–Q1 2026).

### 1.3 Extensibility & reframing

To expand solution space, we can reframe the problem along several axes:

- **Throughput per key vs. throughput per system**
  - Instead of “one MPC key must handle 10,000+ TPM”, consider architectures where workloads are sharded across many MPC keys / signing clusters, and routing hides this from users.
  - This shifts part of the challenge from cryptography to load‑balancing and key management [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].

- **Actual vs. perceived throughput**
  - Users and strategies often care about **when a trade is locked in**, not when MPC computation *finishes*. Optimistic execution, pre‑signed intents, and batching can make throughput *appear* higher to users while MPC runs in the background [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].

- **Virtual vs. physical constraints**
  - Physical constraints: WAN latency, datacenter bandwidth, single‑thread crypto performance.
  - Virtual constraints: conservative protocol round structure, suboptimal precomputation, non‑pipelined orchestration.
  - Many virtual constraints can be relaxed without touching core cryptography.

- **Hard vs. soft requirements**
  - Hard: cryptographic thresholds, correctness, and safety (no key reconstruction, no single‑point compromise).
  - Soft: exact placement of shares, implementation details, orchestration patterns—these are open to optimization and innovation.

---

## 2. Internal Logical Relations

### 2.1 Key elements inside the system

- **Roles**
  - **Key‑share nodes**: hold secret shares and participate in online/offline phases.
  - **MPC coordinator / orchestrator**: schedules sessions, manages queues, retries failures.
  - **Client gateway**: exposes signing APIs to exchanges, DeFi protocols, trading engines.
  - **Monitoring / telemetry**: collects p50/p95/p99 latency, TPM, error rates [Source: Site Reliability Engineering, Beyer et al., 2016, O’Reilly, ch. 4].

- **Resources**
  - CPU and memory for scalar multiplications, Paillier operations, and precomputation [Source: Multiparty Computation from Somewhat Homomorphic Encryption (SPDZ), Damgård et al., 2012, ePrint 2012/642].
  - Network bandwidth and latency across signers (intra‑DC, cross‑region, cross‑cloud) [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Geographic Impact on Performance"].
  - Specialized hardware such as TEEs, GPUs, and FPGAs where deployed [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].

- **Processes**
  1. Request arrives at gateway; placed into per‑tenant or global queues.
  2. Coordinator assigns session to a signing cluster/party set.
  3. Protocol executes offline (precomputation) and online rounds; communication fan‑out across parties.
  4. Signature aggregated and returned; transaction broadcast to blockchain.

### 2.2 Balance & “degree”

Key trade‑offs where “too much of a good thing becomes bad”:

- **Number of shares and threshold t**
  - Higher n and t increase security against single‑node compromise, but each additional signer adds CPU cost and network messages; at some point marginal security gains are outweighed by latency and throughput loss [Source: Threshold ECDSA Documentation, DFINITY Foundation, 2024].

- **Geographic distribution**
  - Wider distribution reduces correlated outage risk and regulatory capture but adds 1–10 seconds per transaction at global scales [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Geographic Impact on Performance"].

- **Batch window length**
  - Longer batch windows dramatically improve throughput (amortizing setup cost) but delay individual transactions, which is unacceptable for latency‑sensitive strategies [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024; Estimate: batching impact based on typical MPC offline/online splits].

### 2.3 Causal chains

- **Chain 1: Per‑session cost → Capacity → Queueing**
  1. Each MPC signing session consumes `C_ms` milliseconds of effective processing time across the cluster (CPU + network round effects).
  2. Theoretical capacity per cluster is `Capacity_TPM ≈ 60,000 / C_ms` (ignoring overhead).
  3. If average incoming arrival rate λ exceeds ~70–80% of capacity, queues grow, p95/p99 latency explodes, and effective throughput collapses [Source: Site Reliability Engineering, Beyer et al., 2016, ch. 6].

- **Chain 2: Number of participants → Failure probability → Effective throughput**
  1. Adding more parties increases probability that at least one is slow/unavailable.
  2. Each failed round triggers retries or aborts, wasting compute and time.
  3. Effective throughput (successful TPM) can be significantly below theoretical capacity.

- **Chain 3: Precomputation coverage → Online latency → Strategy viability**
  1. With high precomputation coverage (many pre‑signatures ready), online signing can be almost non‑interactive and very fast [Source: Fast Two-Party Threshold ECDSA with Proactive Security, ePrint 2024/1831].
  2. If precomputation lags behind demand, online sessions fall back to slower full protocols.
  3. For HFT/MEV flows, any lapse in precomputation coverage directly translates into lost opportunities.

---

## 3. External Connections

### 3.1 Stakeholders and conflicts

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| **Upstream: Network & cloud providers** | Provide low‑latency, high‑bandwidth links and compute | Sell capacity while meeting SLAs | Physical latency limits, cost of premium connectivity | MPC providers want sub‑ms latency that may require costly colocation |
| **Upstream: Protocol designers / cryptographers** | Design MPC / TSS schemes | Maximize security, minimize rounds, maintain proofs | Research cycles long; conservative about trade‑offs | Traders push for more aggressive performance than cryptographers are comfortable with [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024] |
| **Downstream: HFT firms & market makers** | Run latency‑sensitive strategies on MPC wallets | Sub‑100ms latency, thousands of TPS, strong security | Existing strategies benchmarked on hot wallets; switching costs high [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025] | Reject MPC if it degrades P&L, even if more secure |
| **Downstream: DeFi protocols & aggregators** | Integrate MPC custodians into routing | Reliable, fast signing for complex multi‑step flows | Heterogeneous infra and varying support for MPC address types | Will default to EOAs/smart‑contract wallets if MPC lags |
| **Downstream: Exchanges, payroll/airdrop platforms** | Bulk withdrawals and payouts | High aggregate TPM during bursts, predictable SLAs | Batch windows tied to cut‑off times; regulatory settlement rules | May avoid MPC for hot paths, retain only for cold custody |
| **Sideline: Regulators & auditors** | Oversee custody risk | Prefer strong key management (MPC) but also orderly markets | Limited understanding of latency/throughput trade‑offs | Could pressure providers to maintain MPC even if uncompetitive |
| **Sideline: Competing wallet architectures** | Smart‑contract wallets, TEEs, custodial models | Capture market share via better UX/perf | May lack MPC‑level decentralization | Compete on speed and cost rather than security purity [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "The Emergence of Hybrid Approaches"] |

### 3.2 Environment and institutions

- **Market & technology environment**
  - DeFi and centralized exchanges are converging on sub‑second execution expectations for active strategies [Source: Low-Latency Trading, Hasbrouck & Saar, 2013, Journal of Financial Markets].
  - Layer‑2 networks and app‑chains reduce on‑chain latency, making wallet signing latency a more visible bottleneck.
  - Threshold ECDSA/EdDSA is now widely deployed (e.g., Internet Computer’s chain‑key signatures) demonstrating viability for large‑scale use, but not yet tuned for HFT‑like workloads [Source: Threshold ECDSA Documentation, DFINITY Foundation, 2024].

- **Regulatory and institutional environment**
  - Institutional mandates often require strong key management and segregation of duties, pushing toward MPC even when it’s slower.
  - However, best‑execution and market‑fairness regulations can penalize systematically worse execution quality due to latency.

### 3.3 Responsibility & room to maneuver

- **MPC wallet providers must**:
  - Treat throughput/latency as first‑class product metrics alongside security, not as an afterthought.
  - Invest in dedicated performance teams and cross‑disciplinary work between cryptography and distributed‑systems engineers.

- **Enterprise customers and trading firms must**:
  - Share realistic latency and throughput requirements and be willing to adapt strategies (e.g., separating ultra‑latency‑sensitive flows from bulk flows).
  - Consider hybrid custody models (e.g., MPC for control plane, fast smart‑contract wallets for specific on‑chain operations) [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "The Emergence of Hybrid Approaches"].

- **Room for others**:
  - Cloud and network providers can offer MPC‑friendly low‑latency regions and colocation options for MPC clusters.
  - Protocol designers can explore protocols explicitly optimized for high‑volume signing while preserving strong security proofs [Source: Fast Two-Party Threshold ECDSA with Proactive Security, ePrint 2024/1831].

---

## 4. Origins of the Problem

### 4.1 Historical nodes

1. **1980s–2000s: MPC as academic theory**  
   - Focus on correctness and security in adversarial models; performance and throughput considered secondary [Source: Multiparty Computation from Somewhat Homomorphic Encryption (SPDZ), Damgård et al., 2012].

2. **2015–2020: First‑generation blockchain MPC wallets**  
   - Threshold ECDSA protocols (e.g., GG18/GG20) become practical for institutional custody but with high round complexity and overhead.
   - Latency and throughput are acceptable for cold/warm storage but unsuitable for trading desks.

3. **2020–2023: Optimizations and TSS focus**  
   - Dedicated TSS protocols and SPDZ‑style optimizations reduce communication rounds and improve online latency [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].
   - Precomputation and offline/online splitting become common practice.

4. **2023–2025: Performance crisis in DeFi and HFT**  
   - HFT and AMM volumes surge; expectations align with microsecond to millisecond order‑routing latencies [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025].
   - MPC wallets increasingly perceived as “too slow” for anything beyond cold custody.

### 4.2 Background vs. direct causes

- **Deep background factors**
  - Internet architecture was not designed for synchronous multi‑party crypto involving many WAN round‑trips.
  - Academic incentives historically favored new cryptographic constructions over large‑scale performance engineering.

- **Direct near‑term triggers**
  - DeFi composability and MEV intensify competition for execution speed.
  - Exchanges and DeFi platforms measure and compare wallet integration performance, exposing MPC laggards.
  - Competing architectures (smart‑contract wallets, TEEs) demonstrate much higher throughput with acceptable—though different—risk models [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].

### 4.3 Root structural issues

- **Security maximalism without clear performance SLOs**  
  Teams often statically choose high thresholds and globally distributed shares without quantifying their impact on throughput or defining formal latency SLOs.

- **Fragmented responsibility**  
  Cryptography teams, infra teams, and product owners may each assume someone else is handling performance trade‑offs.

- **Under‑investment in measurement**  
  Many MPC deployments lack granular telemetry for per‑round timing, queueing behavior, and p95/p99 latency, making it hard to diagnose bottlenecks [Source: Site Reliability Engineering, Beyer et al., 2016, ch. 6].

---

## 5. Problem Trends

### 5.1 Current trajectory if nothing changes

- **MPC relegated to low‑frequency custody**  
  Without major throughput improvements, MPC wallets are likely to be used mostly for cold/warm storage and slow operational flows, not for active trading.

- **Declining share in institutional trading stack**  
  As faster smart‑contract wallets and custodial models improve, MPC’s share of active flows could stagnate or shrink even if underlying protocols advance [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Conclusion"].

- **Growing competitive gap**  
  Every year that alternative architectures deliver faster execution deepens path dependence toward those models.

### 5.2 Early signals and “spots”

- Exchanges and DeFi protocols often caution that MPC wallets are not recommended for active HFT/arb flows, citing latency and rate limits (industry observation; Estimate: based on public integration docs and anecdotal reports, Medium confidence).
- Articles from providers emphasize hybrid architectures and TEEs to compensate for MPC performance rather than pure protocol breakthroughs [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].
- Traders increasingly co‑locate infra near exchanges and focus on micro‑optimizations at the microsecond level, leaving little room for multi‑second wallet overhead [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025].

### 5.3 Scenarios (6–24 months)

- **Optimistic (≈20%)**  
  - Aggressive precomputation, network optimization, and sharded key architectures lift throughput into the 3,000–10,000 TPM range for specialized setups.
  - HFT desks adopt MPC for at least some strategies where a modest latency penalty is acceptable.

- **Baseline (≈60%)**  
  - Engineering work yields 3–5× improvements (e.g., consumer 100–300 TPM, enterprise ~500–1,000 TPM), but falls short of HFT requirements.
  - MPC becomes standard for secure custody and mid‑frequency execution; HFT remains dominated by hot wallets and other solutions.

- **Pessimistic (≈20%)**  
  - No significant protocol or infra breakthroughs; real‑world throughput stays under ~500 TPM.
  - MPC is seen as a niche security technology; institutional trading stacks standardize on non‑MPC custodial / smart‑contract wallets for active flows.

---

## 6. Capability Reserves

### 6.1 Existing strengths

- **Cryptography expertise**  
  - Many MPC providers already employ researchers familiar with SPDZ, GG18/GG20, and modern TSS protocols [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].

- **Established infrastructure**  
  - Production‑grade APIs, SDKs, monitoring, and deployment pipelines are already in place for many providers [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].

- **Ecosystem momentum**  
  - MPC is well‑understood by regulators and auditors as a robust key‑management pattern.
  - There is strong demand for secure custody from institutions who would prefer not to return to single‑key models.

### 6.2 Capability gaps

- **High‑performance networking and distributed systems skills**  
  Many teams are crypto‑heavy but lack HFT‑style low‑latency engineering experience (kernel‑bypass networking, NUMA awareness, colocation, etc.) [Source: Low-Latency Trading, Hasbrouck & Saar, 2013].

- **Performance product thinking**  
  - Throughput and latency SLOs are often not defined as product requirements with clear financial value attached.
  - Limited systematic A/B testing of architecture changes versus P&L outcomes for trading clients.

- **Operational playbooks**  
  - Few teams have mature playbooks for dynamically shedding load, prioritizing flows, and routing to multiple MPC clusters under stress.

### 6.3 Buildable capabilities (1–6 months)

- **Telemetry and benchmarking framework**  
  - Deploy fine‑grained metrics for per‑phase timing (offline, online, per round) and queueing behavior [Source: Site Reliability Engineering, Beyer et al., 2016].

- **Precomputation infrastructure**  
  - Build always‑on precomputation services sized to forecast demand, with clear backpressure signals and failure modes [Source: Fast Two-Party Threshold ECDSA with Proactive Security, ePrint 2024/1831].

- **Network and placement optimization**  
  - Move critical signing clusters closer to major exchanges and DeFi infra (colocation); optimize transport (persistent connections, efficient framing) [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025].

---

## 7. Analysis Outline

### 7.1 Structured outline (Background → Problem → Analysis → Options → Risks)

- **Background**: MPC emerged from academic cryptography and is now a standard tool for key management.
- **Problem**: Current MPC throughput (10–500 TPM) blocks HFT/DeFi use cases that need thousands of TPM and sub‑second latency.
- **Analysis**: Root causes lie in multi‑round interaction, network placement, limited precomputation, and conservative security configurations.
- **Options**: Pure protocol optimization, infra‑level tuning, hybrid architectures (MPC + smart‑contract wallets + TEEs), or strategic repositioning.
- **Risks**: Security regressions, over‑engineering with marginal benefit, misalignment between provider investments and client willingness to pay.

### 7.2 Key judgments (need validation)

1. **【Critical】** Pure protocol improvements alone (e.g., 3‑round TSS) are unlikely to yield the 10–20× throughput boost needed without parallel infra and architectural changes [Source: Threshold ECDSA in Three Rounds, Doerner et al., 2023].
2. **【Critical】** HFT‑grade latency (<100 ms p95) is probably unattainable for globally distributed MPC without hybrid patterns or localized clusters [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025].
3. **【Important】** For many institutional strategies, reaching p95 ~500–1,000 ms and 1,000–3,000 TPM would already unlock substantial new revenue, even if the system never reaches full HFT parity [Estimate: based on mapping of trading strategy latency sensitivity tiers, Medium confidence].

### 7.3 Alternative paths (high‑level)

- **Path A – Protocol‑centric**: Invest heavily in cutting‑edge MPC / TSS research to reduce rounds and optimize precomputation.
- **Path B – Infra‑centric**: Keep current protocols but aggressively optimize infra, placement, and orchestration.
- **Path C – Hybrid architectures**: Combine MPC with faster smart‑contract wallets, TEEs, and optimistic execution to hide MPC latency from users [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "The Emergence of Hybrid Approaches"].
- **Path D – Repositioning**: Accept limited throughput, position MPC as “gold standard” for high‑value, low‑frequency flows only.

---

## 8. Validating the Answer

### 8.1 Potential biases and blind spots

- **Security‑first bias**: Overweighting theoretical security properties while underestimating the business impact of latency/throughput shortfalls.
- **Optimistic engineering bias**: Underestimating time and complexity of low‑latency infra work, especially for global deployments.
- **Data blind spots**: Lack of real‑world P&L data tying latency improvements to trading outcomes can distort prioritization.

### 8.2 Required intelligence and data

- **Detailed performance baselines**  
  - p50, p95, p99 signing latency broken down by region, protocol, key configuration [Source: Site Reliability Engineering, Beyer et al., 2016].
  - Actual per‑cluster TPM under representative HFT/DeFi loads.

- **Client strategy profiles**  
  - Distribution of trading strategies by latency sensitivity (e.g., ultra‑HFT vs. intraday vs. bulk operations) [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025].

- **Comparative benchmarks**  
  - Measurements vs. hot wallets, hardware wallets, and non‑MPC custodial systems under identical workloads [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].

### 8.3 Validation plan

1. **Month 1–2: Baseline measurement & modeling**  
   - Instrument all signing paths; model capacity and queueing behavior under stress.

2. **Month 2–4: Prototype infra and precomputation improvements**  
   - Run controlled pilots with select HFT/DeFi clients; measure realized TPM and P&L impact.

3. **Month 4–6: Compare architectural options**  
   - Evaluate pure MPC optimizations vs. hybrid approaches vs. repositioning using quantified risk/benefit tables.

---

## 9. Revising the Answer

### 9.1 Parts likely to be revised

- Feasibility of achieving 10,000+ TPM per cluster with current or near‑term MPC protocols.
- Client willingness to accept hybrid custody arrangements where some flows bypass MPC.
- Cost assumptions for deploying TEEs, GPUs, FPGAs, or colocation at exchange data centers.

### 9.2 Incremental approach vs. big‑bang

- **Incremental path**
  - Phase 1: Measurement + quick infra wins (connection pooling, better placement).
  - Phase 2: Precomputation build‑out and basic hybrid flows for select use cases.
  - Phase 3: Evaluate deeper protocol changes and more aggressive hybridization.

- **Avoid**:
  - Multi‑year, protocol‑only rewrite without intermediate deliverables.
  - Deployment of experimental schemes into production without strong audits.

### 9.3 “Good enough” criteria

- Achieve ≥3× throughput increase over baseline and p95 latency <1 second for main institutional flows.
- Demonstrate at least one production HFT/AMM client using MPC‑based flow without significant P&L degradation compared to their hot‑wallet baseline (as measured over several months).
- Maintain or improve security posture (no new critical vulnerabilities; independent audit sign‑off).

---

## 10. Summary & Action Recommendations

### 10.1 Core insights

1. Current MPC throughput (10–500 TPM) is fundamentally misaligned with HFT and many DeFi use cases that require thousands of transactions per minute and sub‑second latency [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025].
2. The bottleneck is not a single factor but the combination of multi‑round protocols, WAN latency, conservative configurations, and limited precomputation and orchestration.
3. Order‑of‑magnitude gains are unlikely from protocol improvements alone; infra, architecture, and workload shaping must all be leveraged.
4. Hybrid architectures can make MPC more viable for active flows by hiding latency and sharding workloads, but they introduce new complexity and require careful risk management [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024].

### 10.2 Near‑term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric (baseline → target) → Date**

1. **【P0 – Critical】 Implement full performance telemetry and capacity modeling** → Infra Lead  
   → Metric: coverage of p50/p95/p99 latency & TPM across all clusters: 0% → 100% → by 2025‑02‑28  
   [Source: Site Reliability Engineering, Beyer et al., 2016, ch. 6].

2. **【P0 – Critical】 Deploy always‑on precomputation for top 3 institutional clients** → Cryptography Lead  
   → Metric: share of signatures using precomputed material: 0% → ≥80% for selected flows → by 2025‑03‑31  
   [Source: Fast Two-Party Threshold ECDSA with Proactive Security, ePrint 2024/1831].

3. **【P1 – Important】 Optimize network placement and connectivity** → Infra & Partnerships  
   → Metric: median RTT between signers in critical clusters: baseline → −30% → by 2025‑03‑31  
   [Source: Latency in Trading: Why Every Millisecond Matters, Lares Algotech, 2025].

4. **【P1 – Important】 Design and prototype a hybrid MPC + smart‑contract wallet architecture** → Chief Architect  
   → Metric: pilot flow achieving p95 signing‑plus‑execution latency <500 ms for one DeFi use case → by 2025‑04‑30  
   [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "The Emergence of Hybrid Approaches"].

5. **【P2 – Optional】 Launch internal R&D track on next‑generation high‑throughput TSS** → Research Lead  
   → Metric: prototype protocol with ≥2× reduction in online rounds compared to current baseline → by 2025‑06‑30  
   [Source: Threshold ECDSA in Three Rounds, Doerner et al., 2023].

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Security regression from aggressive optimization | High | Medium | New protocol/infra change fails audit or faces incident | Stage‑gated reviews, external audits, rollback plans | CISO & Crypto Lead |
| Underestimated infra & engineering cost | High | Medium | Burn rate exceeds budget, milestones slip by >2 sprints | Scope reductions, focus on infra quick wins first, explicit ROI modeling | CTO |
| Client adoption slower than expected | Medium | Medium | Few HFT/DeFi desks opt into MPC‑accelerated flows | Co‑design with anchor clients, incentive pilots, iterate UX/integration | Head of Product |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Protocol‑centric optimization** | Long‑term structural gains; potential academic differentiation | High R&D cost; delayed payoff | Breakthrough may not materialize in timeframe | Strong cryptography team & runway; infra mostly optimized already | Immediate business pressure; limited R&D budget |
| **B. Infra‑centric tuning** | Fast improvements using known techniques; easier to iterate | Ceiling reached after 3–5× gains | Can mask need for deeper changes | Current protocols reasonably efficient; infra under‑optimized | Protocol is the dominant bottleneck; infra already best‑in‑class |
| **C. Hybrid architectures** | Can achieve near‑instant UX for many flows; flexible | Complexity, new failure modes, educational burden | Misconfiguration and misunderstood guarantees | Clients open to hybrid custody and clear risk disclosure | Regulatory constraints prohibit hybrid custody; org risk appetite low |
| **D. Repositioning to low‑freq custody** | Clear focus; no over‑investment in performance | Cedes HFT/DeFi market; lower growth | Competitive disadvantage vs. faster custodial models | Org focuses on long‑term storage & compliance | Strategic goal is to win active‑trading workflows |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **AMM (Automated Market Maker)** | DeFi protocol that provides liquidity via algorithmic pricing, often requiring high transaction throughput to update pools and manage positions. | N/A | [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "When to Use MPC Wallets"] |
| **Batching** | Combining multiple transactions into a single MPC signing session to amortize fixed coordination and crypto costs. | Transactions per batch | [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024] |
| **HFT (High‑Frequency Trading)** | Trading strategies that place and cancel large numbers of orders in milliseconds to capture tiny price discrepancies. | Thousands of orders per second | [Source: Low-Latency Trading, Hasbrouck & Saar, 2013] |
| **MPC (Multi‑Party Computation)** | Cryptographic approach where multiple parties jointly compute a function while keeping their inputs private; used for distributed signing without reconstructing keys. | N/A | [Source: The Evolution of MPC: From Secure but Slow to Fast and Scalable, Dynamic, 2024] |
| **TSS (Threshold Signature Scheme)** | Specialized MPC protocol for generating digital signatures (e.g., ECDSA) such that any t‑of‑n parties can sign without reconstructing the private key. | N/A | [Source: Threshold ECDSA Documentation, DFINITY Foundation, 2024] |
| **TPM (Transactions Per Minute)** | Number of signing operations completed per minute; primary throughput metric in this analysis. | 10–10,000+ TPM | [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Throughput Constraints"] |
| **TPS (Transactions Per Second)** | Signing throughput normalized per second; `TPS = TPM / 60`. | ~0.17–8.33 TPS for current MPC | [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025] |
| **Offline/online phases** | Splitting MPC protocols into heavy offline precomputation (generating randomness and pre‑signatures) and lighter online signing to reduce latency. | N/A | [Source: Fast Two-Party Threshold ECDSA with Proactive Security, ePrint 2024/1831] |
| **Precomputation** | Preparing cryptographic material (e.g., pre‑signatures) ahead of time so online signing can be faster and less interactive. | Pre‑signatures in pool | [Source: Fast Two-Party Threshold ECDSA with Proactive Security, ePrint 2024/1831] |
| **p95 latency** | 95th percentile latency; 95% of operations finish within this time. | ms or seconds | [Source: Site Reliability Engineering, Beyer et al., 2016] |
| **Chain‑key signatures** | An architecture where a blockchain subnet collectively holds key shares and produces threshold signatures, as in Internet Computer’s threshold ECDSA. | N/A | [Source: Threshold ECDSA Documentation, DFINITY Foundation, 2024] |

---

## 12. References

### Tier 1 Sources (Primary / Official / Peer‑Reviewed)

1. **Damgård, I., Pastro, V., Smart, N., & Zakarias, S.** (2012). *Multiparty Computation from Somewhat Homomorphic Encryption (SPDZ).* IACR ePrint 2012/642. https://eprint.iacr.org/2012/642 **[Cited in: 2.1, 2.2, 4.1, 6.1]**
2. **Doerner, J., et al.** (2023). *Threshold ECDSA in Three Rounds.* IACR ePrint 2023/765. https://eprint.iacr.org/2023/765 **[Cited in: Context Recap, 1.1, 1.2, 7.2, 10.2]**
3. **Unknown authors (ePrint 2024/1831).** (2024). *Fast Two-Party Threshold ECDSA with Proactive Security.* IACR ePrint 2024/1831. https://eprint.iacr.org/2024/1831 **[Cited in: 1.2, 2.3, 6.3, 10.2, 11]**
4. **Beyer, B., Jones, C., Petoff, J., & Murphy, N.** (2016). *Site Reliability Engineering: How Google Runs Production Systems.* O’Reilly Media. **[Cited in: 2.1, 2.3, 4.3, 6.3, 8.2, 10.2, 11]**
5. **Hasbrouck, J., & Saar, G.** (2013). *Low-Latency Trading.* Journal of Financial Markets, 16(4), 646–679. **[Cited in: 3.2, 5.2, 6.2, 10.1, 11]**

### Tier 2 Sources (Industry Reports / Technical Articles)

6. **Stackup Team.** (2025). *MPC Wallets: A Complete Technical Guide.* Stackup. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide **[Cited in: Context Recap, 1.1, 2.1, 2.2, 3.2, 4.1, 5.1, 6.1, 7.3, 10.1, 10.4, 11]**
7. **Dynamic.** (2024). *The Evolution of MPC: From Secure but Slow to Fast and Scalable.* Dynamic Blog. https://www.dynamic.xyz/blog/the-evolution-of-mpc **[Cited in: Context Recap, 1.1, 1.3, 3.1, 4.1, 5.2, 6.1, 7.3, 10.1, 11]**
8. **Lares Algotech.** (2025). *Latency in Trading: Why Every Millisecond Matters.* Lares Algotech Blog. https://laresalgotech.com/latency-in-trading-why-every-millisecond-matters/ **[Cited in: Context Recap, 1.1, 1.2, 3.1, 3.2, 5.2, 6.2, 7.2, 10.1, 10.2]**
9. **DFINITY Foundation.** (2024). *Threshold ECDSA Documentation (Chain-Key Signatures).* Internet Computer Docs. https://internetcomputer.org/docs/building-apps/network-features/signatures/t-ecdsa **[Cited in: Context Recap, 1.2, 2.2, 3.2, 4.3, 11]**

### Internal Sources

10. **Infrastructure Team.** (2025-11-29). *Network Throughput Limitations in MPC Signing.* Internal problem statement, Blockchain MPC Wallets repository. **[Cited in: Context Recap, 1.2, 3.3]**
11. **Knowledge Repository.** (2025-11-29). *Nine Aspects for Analyzing Problems.* Internal analysis framework. **[Cited in: Structure of sections 1–10]**

### Estimates & Assumptions (Not Citations)

- **Throughput and adoption projections**: Derived from current 10–500 TPM benchmarks, HFT/DeFi strategy requirements, and internal targets. Confidence: Medium. Validation: telemetry, client pilots, and comparative benchmarks vs. hot‑wallet baselines.
