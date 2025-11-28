 # Nine-Aspects Analysis – Perplexity MPC Problems (2025-11-28)

 ## Problem 1 – MPC Latency for High-Frequency / Real-Time Use Cases

 **Context recap**

 - MPC signing today introduces 100–500 ms (or more) extra latency due to multiple interactive network rounds between geographically distributed nodes.
 - High-frequency trading (HFT), arbitrage, gaming, and high-volume payout scenarios often require near-instant signing and submission; even hundreds of milliseconds can erase edge or break UX.
 - Goal is to approach single-sig UX (<100 ms ideal, ~1 s acceptable upper bound) without sacrificing distributed security.

 ### 1. Problem Definition (Aspect 1)

 - **1.1 Problem and contradictions**
   - Need *both* strong distributed security (geo-distributed MPC nodes, threshold signing) **and** very low end-to-end latency for time-sensitive flows.
   - Contradiction A: More rounds / more nodes → higher security & robustness, but also higher latency and failure probability.
   - Contradiction B: Co-locating or centralizing nodes reduces latency but increases correlated failure and custodial risk.
   - Contradiction C: Precomputation reduces online latency but shifts complexity to storage, invalidation, and DoS surfaces.
 - **1.2 Goals and conditions**
   - Targets (illustrative):
     - p50 signing latency ≤100 ms, p95 ≤150 ms, p99 ≤200 ms from user click to signed transaction (excluding chain confirmation).
     - Throughput ≥500 TPM sustained, elastic to spikes (e.g., 10× for a few minutes).
     - No increase in key compromise risk vs current MPC baseline; fault tolerance at least k-of-n with n ≥3.
   - Conditions:
     - Cannot regress on regulatory posture (e.g., must remain non-custodial if that is the current stance).
     - Hardware budgets: realistic for institutional setups (tens of nodes, not thousands) and mobile end-users.
 - **1.3 Extensibility and reframing**
   - Reframe from “make all MPC as fast as single-sig” → “segment flows where single-sig-like latency is critical, and apply tailored MPC patterns there”.
   - Consider virtual/physical decomposition:
     - Physical: nodes, links, CPU, memory.
     - Virtual: protocol round complexity, precomputation stock, QoS policies, routing topology.
   - Consider positive/negative trade: allow slightly higher infrastructure cost / complexity to unlock new high-value use cases (HFT, options AMMs, market makers).

 ### 2. Internal Logical Relations (Aspect 2)

 - **2.1 Key elements**
   - Roles: trader / dApp user, MPC wallet backend, node operators, exchanges or on-chain venues.
   - Resources: network bandwidth and RTT between nodes, CPU for crypto primitives, precomputation storage, monitoring.
   - Processes: precomputation → online signing rounds → result aggregation → broadcast.
   - Rules: threshold t-of-n, timeout and retry policies, routing / region selection.
 - **2.2 Balance and degree**
   - More precomputation: reduces online latency, but too much increases storage, invalidation complexity, and risk if inventory is drained or corrupted.
   - More nodes / geo-distribution: reduces single-point failure, but beyond a point, added latency between far regions dominates benefits.
   - Aggressive timeouts and retries: improve perceived responsiveness for healthy networks, but can overload systems during partial outages.
 - **2.3 Key internal causal chains**
   - Causal chain 1: `geo-spread ↑ → RTT ↑ → number_of_rounds × RTT ↑ → signing_latency ↑ → failed-arb-opportunities & order_rejections ↑`.
   - Causal chain 2: `precomputation_depth ↑ → online_rounds ↓ → user_latency ↓ → competitiveness ↑`, but also `precomputation_depth ↑ → storage & management burden ↑ → operational risk ↑`.

 ### 3. External Connections (Aspect 3)

 - **3.1 Stakeholders**
   - HFT market makers: care primarily about latency, jitter, and determinism; willing to pay more for dedicated infra.
   - Retail / casual users: latency-sensitive at human-perception scale (~<1 s); care more about reliability and simplicity.
   - Exchanges / DeFi protocols: want predictable signing latency to align with order books and on-chain MEV conditions.
 - **3.2 Environment and institutions**
   - Underlying chain congestion and base-layer confirmation times; L2 / rollup confirmation guarantees.
   - Data-center and cross-region network routing policies; regulatory localization constraints (data residency).
   - Competitive environment: single-sig custodians or HSM-based solutions setting UX expectations.
 - **3.3 Responsibility and room to maneuver**
   - MPC provider is directly responsible for protocol choice, infra design, and exposing clear SLOs.
   - They should leave integration patterns open (e.g., allow trading firms to run co-located signing nodes or gateways) instead of hard-coding all coordination into vendor infra.

 ### 4. Origins of the Problem (Aspect 4)

 - **4.1 Key historical nodes**
   - Phase 1: Cold storage & simple hot wallets – security vs convenience, but no multi-party primitives.
   - Phase 2: HSM-based custody – faster than cold storage, but still centralized keys.
   - Phase 3: MPC custody – focus on security and regulatory narratives; latency was secondary for most early institutions.
   - Phase 4: On-chain HFT and real-time dApps emerge – existing MPC designs show their latency limits.
 - **4.2 Background vs direct causes**
   - Background: academic MPC protocols prioritize correctness and security properties; performance optimized for batch/offline scenarios.
   - Direct causes: using multi-round protocols over long-distance public networks with no specific optimization for low-latency routing.
 - **4.3 Deep structural issues**
   - Product/market fit gap: MPC architectures designed for “secure custody” are reused for “real-time trading” without redesign.
   - Lack of standard performance benchmarks → vendors market security features more than concrete P95/P99 latency numbers.

 ### 5. Problem Trends (Aspect 5)

 - **5.1 Current trend judgment**
   - Without targeted redesign, MPC wallets will be perceived as unsuitable for HFT-like use cases; HFT flows may migrate to alternative custodial or semi-custodial solutions.
 - **5.2 Early signals and spots**
   - Traders bypassing MPC for “fast paths” (e.g., keeping a subset of funds in single-sig or exchange hot wallets).
   - Deals lost to competitors emphasizing “sub-100 ms signing” or co-located infra.
 - **5.3 Possible scenarios (6–24 months)**
   - Optimistic: low-round or partially non-interactive MPC variants plus smart infra (regional routing, co-location) close most of the gap for key customers.
   - Baseline: split market – MPC remains for treasury and larger, slower flows; HFT uses different custody models.
   - Pessimistic: a major incident involving degraded performance during volatile markets tarnishes MPC’s reputation for real-time use.

 ### 6. Capability Reserves (Aspect 6)

 - **6.1 Existing capabilities**
   - Strong cryptography and security expertise; existing MPC implementation and ops experience.
   - Some experience with precomputation and batching.
 - **6.2 Capability gaps**
   - Deep network-level optimization (BGP routing control, co-location strategies) and quantitative latency engineering.
   - Product segmentation and SLO-driven design (clear profiles for HFT vs retail vs treasury).
 - **6.3 Capabilities to build (1–6 months)**
   - Hire / assign dedicated performance engineering function to own latency budgets and benchmarking.
   - Build an internal latency observability stack (per-hop RTT, per-round timing, SLO dashboards).

 ### 7. Analysis Outline (Aspect 7)

 - **7.1 Structured outline**
   - Background: MPC security benefits, current latency profile, target use cases (HFT, gaming, payouts).
   - Problem: protocol round complexity + geo-distribution → latency and jitter incompatible with target SLOs.
   - Analysis: decompose latency (client → node → coordinator → peers), trade-offs among protocol families, infra topologies, and precomputation depths.
   - Options:
     - O1: Optimize existing protocol and infra (co-location, tuned timeouts, better routing, deeper precomputation).
     - O2: Migrate to or add a low-round / partially non-interactive MPC scheme for latency-critical flows.
     - O3: Segment products and provide a “HFT tier” with bespoke infra and possibly adjusted threat model.
   - Risks & follow-ups: protocol migration risk, complexity of tiered offerings, potential security regression.
 - **7.2 Key judgments (to validate)**
   - J1: Network RTT and number of rounds dominate latency more than raw crypto computation time.
   - J2: For a subset of flows, slightly weaker threat models may be acceptable if properly compartmentalized.
   - J3: Traders will pay materially more for a verifiable sub-150 ms signing SLO.
 - **7.3 Alternative paths (positioning)**
   - O1 – "Infra-first": keep protocol, push infra and precomputation to limits; lower risk, moderate latency gains.
   - O2 – "Protocol-first": adopt new MPC schemes; higher R&D and audit cost, bigger potential step-change.
   - O3 – "Segmentation-first": accept that not all flows need the same MPC profile; complicated to communicate but pragmatic.

 ### 8. Validating the Answer (Aspect 8)

 - **8.1 Potential biases**
   - Crypto-engineering bias: overestimating protocol-level gains while underestimating network and systems engineering work.
   - Vendor bias: preferring options that do not require disruptive product repositioning.
 - **8.2 Required intelligence and feedback**
   - Latency decomposition measurements for current production flows (p50/p95/p99 by hop and by region pair).
   - Customer interviews: what latency thresholds truly change trading strategies or UX satisfaction?
 - **8.3 Validation plan**
   - Run controlled experiments with co-located nodes and deeper precomputation to measure best-case latency.
   - A/B test a “low-latency profile” with a pilot HFT customer and compare realized PnL or slippage vs baseline.

 ### 9. Revising the Answer (Aspect 9)

 - **9.1 Parts likely to be revised**
   - Assumed latency budgets HFT desks truly need vs what is “good enough”.
   - The relative importance of protocol vs infra improvements once real measurements are collected.
 - **9.2 Incremental adjustment approach**
   - Start with infra and precomputation optimizations (lower risk) while prototyping new protocols in parallel.
   - Iterate on tier definitions and SLOs based on pilot feedback.
 - **9.3 “Better, not perfect” criteria**
   - For HFT: achieving consistent p95 latency <150 ms and clear, enforced SLOs.
   - For mainstream users: sub-second, highly reliable signing with clear fallbacks during partial outages.

 ### 10. Summary & Action Recommendations (Aspect 10)

 - **10.1 Core insights**
   - The core contradiction is between high-assurance distributed security and the ultra-low latency expectations of HFT and real-time apps.
   - Latency is dominated by round trips and topology; protocol choice, infra design, and product segmentation must be co-designed.
   - Not all transactions need the same latency or threat model; a tiered offering can reconcile conflicting demands.
 - **10.2 Near-term action list (0–3 months)**
   - 【P0】Performance lead + SRE team: instrument full latency breakdown and publish baseline SLOs for key regions (target: complete in 4 weeks).
   - 【P0】Product + eng: define at least two signing profiles (e.g., "standard", "low-latency") with explicit SLOs and threat assumptions (4–6 weeks).
   - 【P1】Crypto + infra teams: prototype deeper precomputation and regional co-location for 1–2 pilot customers; measure gains (6–8 weeks).
   - 【P2】Research: evaluate 1–2 candidate low-round MPC protocols and estimate migration cost and audit scope (concept note in 8 weeks).
 - **10.3 Major risks and responses**
   - Risk (High): security regression or implementation bugs when optimizing for performance.
     - Mitigation: independent audits, staged rollouts, and hard kill-switches to revert to conservative profile.
   - Risk (Medium): confusing customers about threat models across tiers.
     - Mitigation: clear documentation, visual UX labels, and internal training.

 ---

 ## Problem 2 – Vendor Lock-In and MPC Share Portability

 **Context recap**

 - MPC key shares are currently encoded and managed in proprietary ways, with no widely adopted standard akin to BIP-39/44 for seeds.
 - Migrating away from one MPC provider often requires on-chain transfers of all assets, incurring fees, operational risk, and deanonymization.

 ### 1. Problem Definition (Aspect 1)

 - **1.1 Problem and contradictions**
   - Institutions want strong custody controls *and* credible exit options; current proprietary MPC designs effectively trap them.
   - Vendors want stickiness and revenue stability, which conflicts with customer demand for portability and bargaining power.
 - **1.2 Goals and conditions**
   - Goal: enable "custody portability"—moving large portfolios between providers or in-house setups without forced on-chain migration.
   - Conditions:
     - No moment where the full private key exists in one place in usable form.
     - Migration completed in <24 h for large portfolios with minimal service disruption.
 - **1.3 Extensibility and reframing**
   - Reframe from “one universal export format” to a spectrum: protocol-level interoperability, mediated migrations, shared derivation ceremonies, escrowed standards.
   - Consider regulatory angle: portability can be framed as a consumer-protection and resilience feature, creating external pressure on vendors.

 ### 2. Internal Logical Relations (Aspect 2)

 - **2.1 Key elements**
   - Elements: MPC schemes, share encoding formats, key metadata (roles, policies), migration tooling, legal contracts.
   - Processes: key generation, share storage, rotation, and in rare cases, migration or termination.
 - **2.2 Balance and degree**
   - More standardization: increases portability and ecosystem health but may reduce vendor differentiation and IP defensibility.
   - Tighter integration: better UX and feature depth with a given vendor, but higher switching costs and systemic risk.
 - **2.3 Key causal chains**
   - Chain: `proprietary_shares → high_switching_costs → weak customer bargaining power → higher prices / slower innovation`.
   - Chain: `lack_of_exit_plan → compliance & board concerns → slower adoption of MPC custody in risk-averse institutions`.

 ### 3. External Connections (Aspect 3)

 - **3.1 Stakeholders**
   - CIOs, asset managers: need credible exit options and business-continuity plans.
   - Compliance / risk teams: must show regulators that vendor failure or geo-shocks do not irreversibly trap assets.
   - Vendors: face trade-off between openness and revenue predictability.
 - **3.2 Environment and institutions**
   - Regulatory moves on data and service portability in adjacent sectors (e.g., open banking) may set precedents.
   - Industry associations and custodial standards bodies could drive common specifications.
 - **3.3 Responsibility and manoeuvre**
   - Large customers can embed portability requirements into RFPs and contracts.
   - Vendors can pre-emptively design interoperability hooks to differentiate on trust and long-term alignment.

 ### 4. Origins of the Problem (Aspect 4)

 - **4.1 Key historical nodes**
   - Early MPC vendors optimized for speed-to-market and security, not portability.
   - Each built bespoke schemes and tooling, leading to protocol and implementation fragmentation.
   - Only after significant AUM accumulated did portability emerge as a business-risk topic.
 - **4.2 Background vs direct causes**
   - Background: absence of de facto or de jure standards; economic incentives for lock-in.
   - Direct: proprietary cryptographic constructions and non-standard share representations.
 - **4.3 Deep structural issues**
   - Information asymmetry: customers often cannot judge the real cost/feasibility of exit when signing contracts.
   - Lack of collective action: each institution negotiates alone; no strong consortium to demand standards.

 ### 5. Problem Trends (Aspect 5)

 - **5.1 Current trend judgment**
   - As institutional adoption grows and regulators focus more on operational resilience, pressure for portability will increase.
 - **5.2 Early signals and spots**
   - RFPs that explicitly ask for exit plans and key-derivation ceremony documentation.
   - Legal opinions discussing whether inability to exit constitutes an undue risk.
 - **5.3 Possible scenarios**
   - Optimistic: industry coalesces on 1–2 open standards for share formats or migration ceremonies; early adopters of openness gain market share.
   - Baseline: hybrid world where a few alliances (vendor + partners) define semi-open ecosystems; full portability still rare.
   - Pessimistic: a high-profile vendor failure exposes trapped assets, triggering regulatory backlash and forcing rushed, imperfect standards.

 ### 6. Capability Reserves (Aspect 6)

 - **6.1 Existing capabilities**
   - Cryptography and protocol design skills inside vendors and some large customers.
   - Existing open-source threshold signature libraries that could anchor standards.
 - **6.2 Capability gaps**
   - Governance and standardization experience (working with standards bodies, regulators, and competitors).
   - Formal modelling of migration ceremonies to avoid security regressions.
 - **6.3 Capabilities to build**
   - Forming or joining working groups focused on MPC interoperability.
   - Building in-house security review capacity for any migration mechanisms.

 ### 7. Analysis Outline (Aspect 7)

 - **7.1 Structured outline**
   - Background: current vendor-specific MPC landscape, no portable shares.
   - Problem: severe vendor lock-in, high-cost exits, operational and compliance risks.
   - Analysis: incentives of vendors vs customers; technical space of interoperability options.
   - Options:
     - O1: Contractual / legal exit mechanisms without protocol-level portability.
     - O2: Protocol-level standardization of share formats and/or key-derivation ceremonies.
     - O3: Layered model where a neutral “interoperability layer” handles migrations.
   - Risks & follow-ups: security of migration, coordination failure, regulatory lag.
 - **7.2 Key judgments**
   - J1: For large institutions, inability to exit is a board-level and regulatory concern.
   - J2: Vendors that embrace controlled portability can still maintain differentiation on UX, coverage, and service.
   - J3: Overly rigid standardization may slow protocol innovation if not carefully scoped.
 - **7.3 Alternative paths**
   - O1 – "Legal-first": focus on strong SLAs, escrow clauses, and continuity plans; quicker to implement but still technically brittle.
   - O2 – "Standard-first": push for technical standards; higher coordination cost but more durable.
   - O3 – "Intermediary-first": create specialized migration providers; adds a new party but may accelerate adoption.

 ### 8. Validating the Answer (Aspect 8)

 - **8.1 Potential biases**
   - Underestimating vendors' resistance to any standard that reduces lock-in.
   - Overestimating regulators' appetite to intervene proactively rather than after crises.
 - **8.2 Required intelligence and feedback**
   - Survey of existing contracts regarding exit options.
   - Legal / regulatory views on expected continuity and portability in digital asset custody.
 - **8.3 Validation plan**
   - Conduct 5–10 confidential interviews with institutional clients about their willingness to pay / switch for portability.
   - Prototype a safe migration ceremony in a lab and red-team it to quantify risks.

 ### 9. Revising the Answer (Aspect 9)

 - **9.1 Parts likely to be revised**
   - Assumptions about how quickly industry can converge on standards.
   - Appetite of large incumbents to support interoperability.
 - **9.2 Incremental adjustment approach**
   - Start by improving transparency and contractual exit provisions while preparing technical options.
   - Adjust roadmap based on initial feedback from key regulators and customers.
 - **9.3 “Better, not perfect” criteria**
   - At least one credible, tested migration path that avoids full key reconstruction.
   - Clear, audited exit procedures embedded in all major contracts.

 ### 10. Summary & Action Recommendations (Aspect 10)

 - **10.1 Core insights**
   - Vendor lock-in in MPC is not just a commercial annoyance; it is an operational and compliance risk.
   - Solving portability requires both technical mechanisms and contractual / governance innovations.
 - **10.2 Near-term action list (0–3 months)**
   - 【P0】Risk / legal team: inventory existing contracts for exit and portability clauses (4 weeks).
   - 【P1】Crypto + product: map feasible migration patterns (with / without key reconstruction) and rank by risk (6 weeks).
   - 【P1】Business / partnerships: sound out 3–5 peers about appetite for a portability working group (8 weeks).
 - **10.3 Major risks and responses**
   - Risk (High): poorly designed migration ceremony introduces new theft vector.
     - Mitigation: multi-party review, staged rollout, strict limits on scope and timing of use.
   - Risk (Medium): standards efforts stall due to misaligned incentives.
     - Mitigation: align with regulatory expectations and major clients' demands to create external pressure.

 ---

 ## Problem 3 – Permanent Loss of MPC Shares and Asset Recoverability

 **Context recap**

 - In threshold MPC, losing ≥t shares makes key reconstruction mathematically impossible.
 - Self-custodial setups where users control some or all shares are vulnerable to everyday user errors (lost devices, lost backups, account loss).

 ### 1. Problem Definition (Aspect 1)

 - **1.1 Problem and contradictions**
   - Users want "no single point of failure" against theft *and* a forgiving recovery path if they lose devices.
   - Cryptography enforces hard thresholds; relaxed recovery introduces new attack surfaces and potential backdoors.
 - **1.2 Goals and conditions**
   - Goal: achieve near-100% recoverability for legitimate users while preserving strong resistance to theft and coercion.
   - Conditions:
     - Provider must not unilaterally reconstruct keys or transfer funds.
     - Recovery flow must remain usable for non-expert users.
 - **1.3 Extensibility and reframing**
   - Move from binary "recoverable vs not" framing to layered recoverability: short-term incidents (lost phone), medium-term identity recovery, long-term disaster recovery.
   - Consider social, hardware, and institutional guardians as separate dimensions.

 ### 2. Internal Logical Relations (Aspect 2)

 - **2.1 Key elements**
   - Elements: user-controlled shares, provider-controlled shares, guardians, recovery servers, identity verification mechanisms.
   - Processes: enrollment, rotation, backup, recovery ceremony, revocation.
 - **2.2 Balance and degree**
   - More guardians / backup mechanisms: higher robustness, but also more endpoints that attackers can target.
   - Stronger identity checks: more security but potentially worse UX and longer lockout periods.
 - **2.3 Key causal chains**
   - Chain: `weak_backup_practices → share_loss → below_threshold_shares → permanent asset loss`.
   - Chain: `overly_easy_recovery → attacker_social_engineering_success → fraudulent_recovery → theft`.

 ### 3. External Connections (Aspect 3)

 - **3.1 Stakeholders**
   - Retail users: prone to error; need simple, guided flows.
   - Institutions: need formal governance, audit trails, and clearly defined responsibilities for recovery failures.
   - Support teams: caught between "we cannot help" and user expectations.
 - **3.2 Environment and institutions**
   - Consumer-protection norms may increasingly frown upon irreversible loss from common user mistakes.
   - Legal regimes may assign partial liability to providers if recovery is unreasonably hard or poorly explained.
 - **3.3 Responsibility and manoeuvre**
   - Providers can design opinionated recovery policies, defaults, and education.
   - They can also offer differentiated products: ultra-secure, low-recoverability vs more forgiving everyday wallets.

 ### 4. Origins of the Problem (Aspect 4)

 - **4.1 Key historical nodes**
   - Early crypto culture celebrated "be your own bank" and irreversible loss as a feature, not a bug.
   - MPC aimed to remove single key risks but inherited the irreversibility of losing enough components.
 - **4.2 Background vs direct causes**
   - Background: cryptographic hardness of discrete log / related problems; no way to "guess" missing shares.
   - Direct: insufficient attention to UX and lifecycle management of shares and backups.
 - **4.3 Deep structural issues**
   - Cultural bias toward hardcore self-sovereignty vs mainstream expectations for recoverability.
   - Lack of widely-accepted identity and recovery standards in Web3.

 ### 5. Problem Trends (Aspect 5)

 - **5.1 Current trend judgment**
   - As retail adoption grows, high-profile permanent losses will increasingly be seen as product design failures.
 - **5.2 Early signals and spots**
   - Support tickets and social media posts about unrecoverable MPC wallets.
   - Emerging regulatory scrutiny on consumer-asset protection.
 - **5.3 Possible scenarios**
   - Optimistic: robust, privacy-preserving recovery standards emerge (e.g., multi-factor social + institutional guardians) that balance risk well.
   - Baseline: providers converge on a few pragmatic patterns with trade-offs; some incidents continue but at lower rate.
   - Pessimistic: scandals around fraudulent recovery or mass loss lead to over-regulation or reputational damage.

 ### 6. Capability Reserves (Aspect 6)

 - **6.1 Existing capabilities**
   - MPC vendors have cryptography and backend infrastructure expertise.
   - Some have experimented with social recovery and cloud backups.
 - **6.2 Capability gaps**
   - Human-centered design for recovery flows and long-term key lifecycle.
   - Risk modelling for combined social, biometric, and institutional recovery.
 - **6.3 Capabilities to build**
   - Collaborations with UX researchers and security usability experts.
   - Internal red-team exercises focused specifically on recovery attack surfaces.

 ### 7. Analysis Outline (Aspect 7)

 - **7.1 Structured outline**
   - Background: threshold MPC, irreversible loss if below threshold, user behavior patterns.
   - Problem: tension between robust anti-theft guarantees and forgiving recovery for errors.
   - Analysis: categorize failure modes (device loss, account loss, mass guardian collusion) and map to possible mitigations.
   - Options:
     - O1: Pure self-custody with strong education and optional social recovery.
     - O2: Hybrid custody where provider or regulated third party holds an emergency share with strict controls.
     - O3: Multi-tiered identity and guardian-based recovery with time delays and risk scoring.
   - Risks & follow-ups: attack vectors on recovery, user confusion, regulatory interpretation.
 - **7.2 Key judgments**
   - J1: Most mainstream users cannot reliably manage more than 1–2 secrets.
   - J2: Time-delayed recovery with multiple factors provides a good compromise between security and recoverability.
   - J3: Providers can differentiate by making recovery both safer and clearer rather than by avoiding responsibility.
 - **7.3 Alternative paths**
   - O1 – "Max-sovereignty": minimal recovery; suits sophisticated users; high risk for mass market.
   - O2 – "Safety-first": strong institutional backstops; better for retail, but must guard against custodial drift.
   - O3 – "Adaptive": configurable policies with clear defaults; more complex to implement but more flexible.

 ### 8. Validating the Answer (Aspect 8)

 - **8.1 Potential biases**
   - Technologist bias: overemphasis on cryptographic elegance vs practical user behavior.
   - Security bias: over-weighting theft risk vs everyday loss risk.
 - **8.2 Required intelligence and feedback**
   - Empirical data on device loss and account loss rates for current user base.
   - User research on how people understand and act on backup / recovery instructions.
 - **8.3 Validation plan**
   - Run usability tests for candidate recovery flows with non-expert participants.
   - Simulate recovery under stress (lost phone, time pressure) and measure success rates and error types.

 ### 9. Revising the Answer (Aspect 9)

 - **9.1 Parts likely to be revised**
   - Exact thresholds for when to involve institutional guardians or require extra checks.
   - The number and nature of default guardians.
 - **9.2 Incremental adjustment approach**
   - Start with conservative recovery mechanisms and gradually reduce friction where data shows low risk.
   - Introduce configurable policies for advanced users as an opt-in.
 - **9.3 “Better, not perfect” criteria**
   - Target: ≥99% recovery success for legitimate users in test cohorts; no observed fraudulent recoveries in pilot.
   - Clear, simple mental model explained to users in <1 minute.

 ### 10. Summary & Action Recommendations (Aspect 10)

 - **10.1 Core insights**
   - Permanent asset loss from everyday mistakes is a design and policy problem, not just a cryptographic inevitability.
   - Recovery must be treated as a first-class feature with its own threat models and UX, not an afterthought.
 - **10.2 Near-term action list (0–3 months)**
   - 【P0】Product + security: inventory all current recovery-related mechanisms and failure modes; produce risk register (4 weeks).
   - 【P1】UX + research: prototype 1–2 multi-factor recovery flows and run small usability studies (6–8 weeks).
   - 【P1】Security: conduct focused threat modelling on recovery ceremonies and guardian compromise (6 weeks).
 - **10.3 Major risks and responses**
   - Risk (High): new recovery path becomes the primary theft vector.
     - Mitigation: time delays, out-of-band confirmations, anomaly detection, limited daily recovery quotas.
   - Risk (Medium): complexity overwhelms users and support staff.
     - Mitigation: opinionated defaults, clear playbooks, and training material.

 ---

 ## Problem 4 – Regulatory Ambiguity Around “Control” and Custody for MPC Providers

 **Context recap**

 - Traditional regulation ties “custody” to control over private keys and ability to block or execute transactions.
 - In MPC, no single party holds a full key, but vendors may still run coordination servers and hold key shares.

 ### 1. Problem Definition (Aspect 1)

 - **1.1 Problem and contradictions**
   - Vendors wish to position as non-custodial software providers while regulators may view them as de facto custodians if they can block usage.
   - Customers and investors want regulatory certainty; over-compliance may be costly, but non-compliance can be existential.
 - **1.2 Goals and conditions**
   - Goal: achieve a technical and legal architecture that is robust under likely future interpretations of custody regulations.
   - Conditions:
     - Business remains viable across major jurisdictions (US, EU) without constantly pivoting models.
     - Architecture choices are transparent and auditable.
 - **1.3 Extensibility and reframing**
   - View "control" not just as key possession but as a continuum: power to initiate, veto, censor, or surveil transactions.
   - Consider multiple levers: technical design, governance, contractual representations, and geographic structuring.

 ### 2. Internal Logical Relations (Aspect 2)

 - **2.1 Key elements**
   - Elements: key shares, coordination servers, policy engines, admin controls, fail-safes, logging.
   - Processes: onboarding, transaction policy evaluation, signing, incident handling, service shutdown.
 - **2.2 Balance and degree**
   - More central power (e.g., kill switches, global policy enforcement) can mitigate risk and please some regulators but also strengthens the argument that the provider is a custodian.
   - More decentralization reduces single points of control but may reduce ability to comply with some regulatory demands.
 - **2.3 Key causal chains**
   - Chain: `coordination_server_can_block_tx → de_facto_control ↑ → regulator_may_label_as_custodian`.
   - Chain: `opaque_architecture + marketing_claims_mismatch → enforcement_risk ↑`.

 ### 3. External Connections (Aspect 3)

 - **3.1 Stakeholders**
   - Regulators (SEC, FinCEN, EU supervisors): aim to prevent unregulated custody and systemic risk.
   - Vendors: seek scalable, global businesses.
   - Customers: want clarity on who holds responsibility and what happens in edge cases.
 - **3.2 Environment and institutions**
   - Ongoing evolution of digital asset rules (e.g., MiCA, SAB 121 interpretations, travel rule guidance).
   - Case law and enforcement actions against pseudo-non-custodial providers in adjacent sectors.
 - **3.3 Responsibility and manoeuvre**
   - Vendors can proactively engage regulators, disclose architectures, and seek no-action letters or rulings.
   - They can redesign coordination / key share placement to limit unilateral control.

 ### 4. Origins of the Problem (Aspect 4)

 - **4.1 Key historical nodes**
   - Early emphasis on "not your keys, not your coins" pushed industry toward self-custody language.
   - MPC vendors marketed "non-custodial" without fully aligning legal and technical meanings.
 - **4.2 Background vs direct causes**
   - Background: regulators slow to understand MPC specifics; broad principles like "substance over form" guide decisions.
   - Direct: architectures where vendors both hold shares and operate central coordinators, allowing them to block or delay user actions.
 - **4.3 Deep structural issues**
   - Misalignment between marketing narratives and legal risk assessments.
   - Lack of standardized reference architectures vetted by regulators.

 ### 5. Problem Trends (Aspect 5)

 - **5.1 Current trend judgment**
   - Regulatory scrutiny is increasing; ambiguity will be resolved, likely in a more conservative direction.
 - **5.2 Early signals and spots**
   - Public company accounting guidance treating crypto held for others as balance-sheet liabilities.
   - Policy papers specifically mentioning MPC in the context of custody.
 - **5.3 Possible scenarios**
   - Optimistic: clear guidance that certain MPC patterns with user-majority control and decentralized coordination are non-custodial.
   - Baseline: mixed environment where some jurisdictions treat typical vendor models as custody, requiring licenses; others are more flexible.
   - Pessimistic: broad definition of custody that effectively classifies most MPC providers as custodians.

 ### 6. Capability Reserves (Aspect 6)

 - **6.1 Existing capabilities**
   - Legal and compliance teams with initial understanding of digital asset rules.
   - Technical teams able to redesign architectures in response to guidance.
 - **6.2 Capability gaps**
   - Deep, ongoing regulatory affairs capacity and participation in policy discussions.
   - Internal alignment between product, marketing, and legal narratives.
 - **6.3 Capabilities to build**
   - Formal regulatory engagement function and external counsel relationships.
   - Internal governance processes for approving architecture and policy changes through a regulatory lens.

 ### 7. Analysis Outline (Aspect 7)

 - **7.1 Structured outline**
   - Background: current definition of custody, typical MPC vendor architectures.
   - Problem: ambiguity about whether holding a share + running coordination constitutes custody.
   - Analysis: map degrees of control vs legal interpretations.
   - Options:
     - O1: Embrace custodian status and obtain necessary licenses.
     - O2: Redesign architecture and governance to minimize de facto control.
     - O3: Hybrid approach where regulated entities handle some parts and vendors others.
   - Risks & follow-ups: regulatory arbitrage, complexity, cost.
 - **7.2 Key judgments**
   - J1: Ignoring ambiguity is the highest-risk path.
   - J2: Transparent engagement and documented design rationales will be viewed more favorably than opaque claims.
   - J3: There is room for multiple viable models depending on client base and jurisdictions.
 - **7.3 Alternative paths**
   - O1 – "Full-custody": accept being a custodian; higher cost but potentially simpler narrative.
   - O2 – "Hard non-custodial": strict technical measures to avoid unilateral control; may reduce product flexibility.
   - O3 – "Split-stack": partner with licensed custodians while providing MPC technology.

 ### 8. Validating the Answer (Aspect 8)

 - **8.1 Potential biases**
   - Commercial bias toward minimizing regulatory burden.
   - Optimism bias about regulators accepting nuanced technical arguments.
 - **8.2 Required intelligence and feedback**
   - Comparative analysis of enforcement actions and guidance across jurisdictions.
   - Feedback from regulators and external counsel on specific architectures.
 - **8.3 Validation plan**
   - Prepare detailed technical whitepaper describing control surfaces and present it in structured regulator discussions.
   - Run tabletop exercises simulating regulator challenges and prepare responses.

 ### 9. Revising the Answer (Aspect 9)

 - **9.1 Parts likely to be revised**
   - Which combination of architectural and governance changes regulators consider sufficient.
   - The cost/benefit calculus of pursuing licenses vs redesign.
 - **9.2 Incremental adjustment approach**
   - Prioritize changes that reduce de facto control and improve transparency, then reassess licensing needs.
   - Maintain flexible architecture so future tightening can be accommodated.
 - **9.3 “Better, not perfect” criteria**
   - Regulator feedback indicating low enforcement priority or explicit comfort with chosen model.
   - Internally consistent story between legal, technical, and marketing artifacts.

 ### 10. Summary & Action Recommendations (Aspect 10)

 - **10.1 Core insights**
   - Regulatory ambiguity around MPC control is a strategic, not just legal, issue.
   - Choices made today about coordination, key share placement, and admin controls strongly influence future regulatory classification.
 - **10.2 Near-term action list (0–3 months)**
   - 【P0】Legal + architecture: map all control surfaces (who can block, delay, or force transactions) and produce an internal briefing (4 weeks).
   - 【P0】Leadership: decide on target regulatory posture (aim for custodian vs non-custodial vs hybrid) and align roadmap (6 weeks).
   - 【P1】Regulatory affairs: schedule exploratory consultations with at least one key regulator / supervisor (8–12 weeks).
 - **10.3 Major risks and responses**
   - Risk (High): adverse ruling forces emergency changes or shutdown.
     - Mitigation: contingency plans for rapid license pursuit or architecture switch; conservative scaling in high-risk jurisdictions.
   - Risk (Medium): over-engineering non-custodial guarantees that customers do not value.
     - Mitigation: segment client needs and match them to appropriate models.

 ---

 ## Problem 5 – Centralization Risk in MPC Coordination Servers

 **Context recap**

 - Many MPC wallets rely on a vendor-hosted coordination server to relay messages among key-share holders during signing.
 - This server can be a single point of failure and censorship, undermining the decentralization narrative and introducing existential availability risk.

 ### 1. Problem Definition (Aspect 1)

 - **1.1 Problem and contradictions**
   - Desire for seamless UX and simple connectivity pushes toward central coordination.
   - Desire for censorship resistance and business continuity pushes toward decentralized or user-controlled coordination.
 - **1.2 Goals and conditions**
   - Goal: enable users to sign as long as enough key shares exist and can communicate, even if the original vendor is offline or hostile.
   - Conditions:
     - Practical for typical user devices (mobiles, browsers).
     - Does not explode complexity or latency beyond acceptable bounds.
 - **1.3 Extensibility and reframing**
   - Reframe coordinator from “one server” to “coordination layer”: could be centralized, federated, or peer-to-peer.
   - Split dimensions: liveness (can I sign?) vs policy control (who decides what is allowed?).

 ### 2. Internal Logical Relations (Aspect 2)

 - **2.1 Key elements**
   - Elements: user clients, key-share nodes, coordination relays, discovery mechanisms, failover configurations.
   - Processes: peer discovery, message routing, session establishment, error handling.
 - **2.2 Balance and degree**
   - More decentralization (p2p relays, multiple coordinators): better resilience and censorship resistance, but more complex network behavior and potential performance variability.
   - Simplicity and centralization: easier debugging and support, but higher platform risk.
 - **2.3 Key causal chains**
   - Chain: `single_central_coordinator → outage_or_censorship → total_signing_failure_for_all_users`.
   - Chain: `p2p_or_federated_layer → attack_surface ↑ → need_for_better_monitoring_and_abuse_controls ↑`.

 ### 3. External Connections (Aspect 3)

 - **3.1 Stakeholders**
   - DeFi and censorship-sensitive users: demand independence from any single corporate API.
   - Enterprise customers: emphasize uptime and SLAs; more tolerant of controlled centralization if reliability is proven.
   - Security auditors: concerned about single points of failure and covert control channels.
 - **3.2 Environment and institutions**
   - Cloud provider concentration: many coordinators run on a small number of hyperscalers, amplifying correlated risk.
   - Regulatory / political pressures that may compel service blocking in jurisdictions.
 - **3.3 Responsibility and manoeuvre**
   - Vendors can design multi-coordinator or coordinator-of-last-resort architectures and publish escape hatches.
   - They can give users the ability to self-host coordinators or plug into neutral relay networks.

 ### 4. Origins of the Problem (Aspect 4)

 - **4.1 Key historical nodes**
   - Initial MPC prototypes used straightforward client–server topologies for ease of implementation.
   - As products moved to production, focus stayed on scaling central services rather than rethinking topology.
 - **4.2 Background vs direct causes**
   - Background: web and mobile development norms (API-centric architectures) and operations practices.
   - Direct: business models that assume always-on vendor APIs and treat independence as a secondary concern.
 - **4.3 Deep structural issues**
   - Tension between SaaS economics (central control, monitoring, billing) and protocol-level decentralization ideals.
   - Lack of economic incentives for vendors to make it easy to bypass their infra.

 ### 5. Problem Trends (Aspect 5)

 - **5.1 Current trend judgment**
   - With growing DeFi and regulatory risk, scrutiny of hidden centralization points is increasing.
 - **5.2 Early signals and spots**
   - Community criticism of "web2 in front, web3 at the back" architectures.
   - Security reviews flagging centralized coordination as a major risk.
 - **5.3 Possible scenarios**
   - Optimistic: new coordination layers emerge (federated or p2p) that balance UX and decentralization.
   - Baseline: most mainstream products remain centralized but provide documented, tested emergency escape paths.
   - Pessimistic: a vendor outage or shutdown locks users out of funds, leading to reputational and possibly legal consequences.

 ### 6. Capability Reserves (Aspect 6)

 - **6.1 Existing capabilities**
   - Vendors have strong server-side engineering and cloud operations capabilities.
   - Existing p2p and decentralized relay protocols (e.g., gossip-based networks, pub-sub overlays) can be leveraged.
 - **6.2 Capability gaps**
   - Experience building user-friendly p2p systems on constrained devices.
   - Threat modelling for open coordination layers (spam, DDoS, metadata leakage).
 - **6.3 Capabilities to build**
   - Prototype teams focused on networking and distributed systems beyond standard client–server.
   - Partnerships with existing decentralized messaging / relay projects.

 ### 7. Analysis Outline (Aspect 7)

 - **7.1 Structured outline**
   - Background: typical central coordinator design in MPC wallets.
   - Problem: single point of failure and censorship undermining trustless claims and BC/DR plans.
   - Analysis: map control and failure modes, evaluate alternatives.
   - Options:
     - O1: Harden central coordinator (geo-redundancy, multi-cloud, strict SLAs).
     - O2: Introduce federated coordinators operated by multiple independent parties.
     - O3: Move to or add a p2p coordination option using neutral relay networks.
   - Risks & follow-ups: complexity, abuse, attack surfaces.
 - **7.2 Key judgments**
   - J1: Pure centralization is incompatible with strong trustless and censorship-resistance claims.
   - J2: Most enterprises will accept some centralization if BC/DR is demonstrably strong.
   - J3: A hybrid architecture (central by default, decentralized escape) may be the most practical.
 - **7.3 Alternative paths**
   - O1 – "Central-strong": accept centralization but invest heavily in robustness and transparency.
   - O2 – "Federated": distribute coordinators among partners; improves resilience but needs governance.
   - O3 – "P2P-capable": provide a p2p coordination mode as a safety valve and for high-sovereignty users.

 ### 8. Validating the Answer (Aspect 8)

 - **8.1 Potential biases**
   - Decentralization idealism may overvalue complex p2p designs over simpler, robust central models.
   - Conversely, SaaS commercial bias may downplay long-tail but catastrophic risks.
 - **8.2 Required intelligence and feedback**
   - Reliability data of current coordinators (uptime, incident reports).
   - Customer appetite for self-hosted / federated options vs willingness to pay for them.
 - **8.3 Validation plan**
   - Conduct tabletop BC/DR exercises: simulate cloud provider ban, regulator injunction, or massive DDoS.
   - Run limited pilots of federated or p2p coordination with advanced users and measure performance.

 ### 9. Revising the Answer (Aspect 9)

 - **9.1 Parts likely to be revised**
   - Extent to which users will actually self-host or join federated coordination.
   - Optimal balance between central and decentralized modes.
 - **9.2 Incremental adjustment approach**
   - Start by hardening existing central infra and documenting escape hatches.
   - Gradually expose more decentralized options to advanced users, then integrate into mainstream offerings if demand exists.
 - **9.3 “Better, not perfect” criteria**
   - Demonstrable ability for users to continue signing even if the main vendor API is offline.
   - Acceptable performance degradation (<2× latency) in decentralized modes for most flows.

 ### 10. Summary & Action Recommendations (Aspect 10)

 - **10.1 Core insights**
   - Coordination centralization is a hidden but critical risk in many MPC architectures.
   - Business continuity, censorship resistance, and user trust depend on having viable alternatives to a single vendor API.
 - **10.2 Near-term action list (0–3 months)**
   - 【P0】SRE + security: perform a structured single-point-of-failure analysis of current coordination layer and publish internal report (4 weeks).
   - 【P1】Architecture: design and document at least one emergency escape mechanism (e.g., self-hosted coordinator option) and test it with internal users (6–8 weeks).
   - 【P2】Product: survey key customer segments on interest in federated or p2p coordination options and acceptable trade-offs (8 weeks).
 - **10.3 Major risks and responses**
   - Risk (High): misconfigured decentralized coordination introduces new vulnerabilities or degraded UX.
     - Mitigation: strict scoping, progressive rollout, and robust monitoring.
   - Risk (Medium): customers ignore escape options until a crisis, then struggle to use them.
     - Mitigation: regular drills, clear documentation, and automated activation flows.
