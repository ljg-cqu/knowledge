# Gas Fee Estimation Across Heterogeneous Chains

**Last Updated**: 2025-11-30  
**Status**: Draft – Nine-Aspects Analysis  
**Owner**: Engineering & Product Team / Architecture & Research

---

## Context Recap

- **Problem title**: Gas Fee Estimation Across Heterogeneous Chains
- **Current state**:
  - Multi-chain MPC wallet supports EVM (EIP-1559), Bitcoin, and Solana, but fee estimation is driven by simple, chain-specific multipliers on external oracle estimates with minimal mempool analytics. [Source: Blockchain MPC Wallet Problem Extraction, Supplementary Analysis GPT5, 2025-11-28]
  - On EVM chains, fees follow EIP-1559 (base fee burned + priority fee to validators, with `maxFeePerGas` and `maxPriorityFeePerGas` parameters). [Source: EIP-1559 Gas Fees: Base Fee, Priority Fee, & Max Fee, Blocknative, accessed 2025-11-30, https://www.blocknative.com/blog/eip-1559-fees]
  - On Bitcoin, users bid using sat/vbyte; stuck transactions can sometimes be replaced by higher-fee versions via Opt-in Replace-By-Fee (RBF) or unblocked via Child-Pays-For-Parent (CPFP). [Source: Opt-in RBF FAQ, Bitcoin Core, accessed 2025-11-30, https://bitcoincore.org/en/faq/optin_rbf/; Source: FAQ, mempool.space, accessed 2025-11-30, https://mempool.space/docs/faq]
  - On Solana, transaction cost is composed of a base fee plus optional priority fees specified as micro-lamports per compute unit, used as a tip to influence scheduling. [Source: Transaction Fees, Solana Docs, accessed 2025-11-30, https://solana.com/docs/core/fees; Source: Understand Solana Priority Fees: Land Transactions Faster, QuickNode, accessed 2025-11-30, https://www.quicknode.com/guides/solana-development/transactions/how-to-use-priority-fees]
  - Current implementation leads to 10–20% of transactions failing to confirm within target windows or getting stuck, and 30–50% average overpayment during congestion. [Source: Blockchain MPC Wallet Problem Extraction, Supplementary Analysis GPT5, 2025-11-28]
- **Pain points**:
  - “Stuck” transactions that require manual support or user resubmission, contributing to ~35% of ticket volume (300–500 tickets/month). [Source: Blockchain MPC Wallet Problem Extraction, Supplementary Analysis GPT5, 2025-11-28]
  - Overpayment of 30–50% vs achievable confirmation-fee trade-offs during volatile periods, causing avoidable user costs and competitive disadvantage versus wallets with more advanced fee logic. [Source: Blockchain MPC Wallet Problem Extraction, Supplementary Analysis GPT5, 2025-11-28]
  - Lack of unified cross-chain abstraction for fees; engineering teams maintain fragmented, chain-specific logic with limited observability.
- **Goals**:
  - **Confirmation reliability**: ≥99% of transactions confirm within target windows: EVM ≤2 blocks p95, Bitcoin ≤3 blocks p95, Solana ≤2 slots p95.
  - **Fee efficiency**: Reduce average overpayment from 30–50% to 10–20% (20–40% improvement).
  - **Support & UX**: Cut stuck-transaction support tickets by ≥60% (from ~35% of volume to ≤15%) and provide clearer “pending vs stuck” signals in UX.
  - **Replacement success**: Automated replacement/bump flows succeed ≥95% of the time when triggered.
  - **Latency**: Keep fee estimation overhead ≤100 ms p95 so signing UX remains responsive.
- **Hard constraints**:
  - Limited direct mempool access; heavy reliance on third-party RPCs and fee oracles (Blocknative, Etherscan, Mempool.space, Solana RPC `getRecentPrioritizationFees`, etc.). [Source: Gas Price API | Gas Platform, Blocknative Docs, accessed 2025-11-30, https://docs.blocknative.com/gas-prediction/gas-platform]
  - Third-party APIs introduce rate limits and recurring costs (≈$50–$500/month for higher-volume tiers) and may degrade under peak load. [Source: Estimate transaction fee (API Reference), Cobo Developers, accessed 2025-11-30, https://www.cobo.com/developers/v2/api-references/transactions/estimate-transaction-fee]
  - Backward compatibility with existing transaction submission flows and manual fee overrides is mandatory.
  - Engineering capacity: ~2 FTE blockchain engineers and 0.5 PM for ~3–5 months; budget ≈$30K implementation + $5K/month services (as per problem statement).
- **Key facts**:
  - Cobo and similar MPC providers expose unified fee estimation endpoints that adapt to chain-specific fee models but still require integrators to set tolerance and speed vs cost profiles. [Source: How to Estimate and Optimize Transaction Fees for MPC Wallets, Cobo Developers, accessed 2025-11-30, https://www.cobo.com/developers/v1/guides/howtos/estimate-transaction-fees]
  - EVM fee markets exhibit highly volatile base fees and tips around congestion, making static multipliers fragile. [Source: EIP-1559 Gas Fees: Base Fee, Priority Fee, & Max Fee, Blocknative, accessed 2025-11-30]
  - Solana priority fees vary by program and depend on local contention patterns, so global heuristics often misprice high-contention DeFi programs. [Source: How to use Priority Fees on Solana, Solana Developers, accessed 2025-11-30, https://solana.com/developers/guides/advanced/how-to-use-priority-fees; Source: Understand Solana Priority Fees: Land Transactions Faster, QuickNode, accessed 2025-11-30]

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

- **Core problem**: The wallet lacks a robust, unified mechanism for estimating and adjusting transaction fees across fundamentally different chain fee models (EVM EIP-1559, Bitcoin sat/vbyte with RBF/CPFP, Solana compute-unit priority fees), leading to a mix of underpriced transactions that stall and overpriced transactions that waste user funds. [Source: Blockchain MPC Wallet Problem Extraction, Supplementary Analysis GPT5, 2025-11-28; Source: How to Estimate and Optimize Transaction Fees for MPC Wallets, Cobo Developers, accessed 2025-11-30]
- **Key contradictions**:
  - **Speed vs. cost**: Users want fast, predictable confirmations but are sensitive to overpaying; conservative policies reduce failure but overspend, while aggressive policies save fees but increase stuck risk.
  - **Abstraction vs. specificity**: Product wants a simple “slow/normal/fast” UX that works across chains, but each chain’s fee model behaves differently under congestion, demanding chain- and even program-specific tuning. [Source: Transaction Fees, Solana Docs, accessed 2025-11-30; Source: Gas Price API | Gas Platform, Blocknative Docs, accessed 2025-11-30]
  - **Automation vs. transparency**: Strong automation (automatic bumping, re-broadcasting) reduces manual work but can confuse users who don’t understand why fees changed post-signing, or who need auditability.
- **Stakeholder tensions**:
  - End users want “just works” behavior and fair fees.
  - Trading/exchange partners require predictable deposit confirmation times to honor SLAs.
  - Finance wants to minimize aggregate fee overspend.
  - Engineers want maintainable abstractions rather than one-off scripts per chain.

### 1.2 Goals & conditions

- **Reliability targets**:
  - EVM: ≥99% of transactions confirmed within ≤2 blocks p95 under normal conditions; under heavy congestion, explicit UX messaging and optional “turbo” mode. [Source: EIP-1559 Gas Fees, Blocknative, accessed 2025-11-30]
  - Bitcoin: ≥99% of transactions confirmed within ≤3 blocks p95 for standard priority, with RBF/CPFP used to rescue outliers. [Source: Opt-in RBF FAQ, Bitcoin Core, accessed 2025-11-30]
  - Solana: ≥99% of transactions landed within ≤2 slots p95 for standard DeFi transfers and swaps, using dynamic compute-unit pricing. [Source: How to use Priority Fees on Solana, Solana Developers, accessed 2025-11-30]
- **Efficiency targets**:
  - Reduce average fee overpayment from 30–50% to 10–20% relative to empirical “just-in-time” fee levels during typical and moderately congested conditions. [Estimate: Based on benchmarking target from problem statement; Medium confidence, validate via before/after on-chain fee analysis]
- **Project constraints**:
  - Timeline: 3–5 months for design, implementation, experimentation, and phased rollout.
  - Backward compatibility: No breaking changes to existing transaction APIs; manual fee overrides remain available for power users.
  - Observability: Must introduce new telemetry (fee estimate vs paid vs required, confirmation delay) to avoid operating blind.

### 1.3 Extensibility & reframing

- **Reframing 1 – From “gas price guessing” to “confirmation risk management”**:
  - Treat fee selection as a risk decision: minimize expected cost of `(overpayment + re-submission + user churn)` subject to confirmation-SLA constraints.
- **Reframing 2 – From “per-chain scripts” to “fee policy engine”**:
  - Instead of separate ad hoc heuristics, design a policy engine with pluggable chain adapters and shared risk/utility framework.
- **Reframing 3 – From “single-shot estimation” to “lifecycle management”**:
  - Include initial fee choice, monitoring, and potential bump/replace/resubmit as one lifecycle, not isolated steps.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Fee policy engine**: Core service that receives transaction context (chain, urgency, tx type, size/complexity) and outputs fee parameters + strategy (e.g., initial tip, bump thresholds). [Source: Estimate transaction fee (API Reference), Cobo Developers, accessed 2025-11-30]
- **Chain adapters**:
  - **EVM adapter**: Maps policy outputs into `maxFeePerGas`, `maxPriorityFeePerGas`, potentially considers base-fee growth bounds and next-block predictions. [Source: Gas Price API | Gas Platform, Blocknative Docs, accessed 2025-11-30]
  - **Bitcoin adapter**: Expresses choices as sat/vbyte, sets RBF flags, and, when needed, constructs CPFP child transactions.
  - **Solana adapter**: Sets compute-unit limits and compute-unit price, and may adjust for specific programs (AMMs, NFT marketplaces). [Source: Transaction Fees, Solana Docs, accessed 2025-11-30]
- **Data sources**:
  - External gas oracles (e.g., Blocknative, Etherscan, Mempool.space, Solana RPC) and internal historical confirmation metrics. [Source: FAQ, mempool.space, accessed 2025-11-30]
- **Monitoring & replacement**:
  - Watchers that track mempool state or RPC status for submitted txs; trigger threshold-based replacements or bumps when delays exceed SLA.
- **UX and API layer**:
  - Exposes simple modes (economy/standard/fast) while logging underlying numeric decisions for auditability.

### 2.2 Balance & “degree”

- **Safety margin vs. cost**:
  - Higher multipliers above oracle estimates reduce non-confirmation but induce quadratic cost growth in volatile markets (base fee + high tip on many transactions). [Source: EIP-1559 Gas Fees, Blocknative, accessed 2025-11-30]
- **Freshness vs. stability**:
  - Very frequent oracle polling captures spikes quickly but risks oscillations and rate limiting; coarser windows are cheaper but may lag congestion events. [Source: Gas Price API | Gas Platform, Blocknative Docs, accessed 2025-11-30]
- **Automation vs. complexity**:
  - Rich per-chain strategies (e.g., CPFP templates, per-program Solana tips) improve outcomes but increase implementation and maintenance complexity.

### 2.3 Causal chains (simplified)

1. **Inadequate inputs → Mispriced fees → Stuck or overpriced transactions**:
   - If the engine only sees coarse oracle tiers (slow/avg/fast) without mempool context, it cannot adapt to sudden demand spikes, leading to underpriced txs that lag many blocks or require manual resubmission. [Source: FAQ, mempool.space, accessed 2025-11-30]
2. **No lifecycle management → “Zombie” transactions**:
   - Lacking automated monitoring and bumping mechanics, underpriced txs remain in mempools for hours or days, creating support load and user frustration.
3. **Fragmented logic → High maintenance cost and bugs**:
   - Divergent chain-specific scripts increase the probability of silent failures when a chain’s fee rules evolve or new L2s are added.

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders & interactions

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream – End users (retail, prosumers) | Initiate transfers/swaps via MPC wallet | Fast, predictable confirmations at “fair” fees | Limited fee literacy; mobile UX; occasional manual overrides | Want simplicity while advanced users may want more control |
| Upstream – Institutional clients & exchanges | Use MPC wallet for treasury, deposits/withdrawals | SLA-grade confirmations, predictability for operational processes | Batch flows, strict risk policies | May demand stricter confirmation guarantees than retail |
| Downstream – RPC & oracle providers | Supply gas/fee estimates, mempool data | Monetize APIs, ensure reliability | Rate limits, regional latency, outage risk | Their degradations directly affect wallet performance |
| Downstream – Blockchains & validators | Execute transactions, reorder by fee | Maximize revenue while honoring protocol rules | Capacity & congestion vary; MEV strategies | Fee markets can become highly spiky, challenging stable UX |
| Sideline – Support, Finance, Compliance | Handle incidents, cost control, policy | Reduce stuck-tx tickets, keep fee spend within budget, maintain compliance | Limited engineering bandwidth; must justify vendor spend | Push for lower fees vs reliability tension with product |

### 3.2 Environment factors

- **Market volatility**:
  - NFT mints, airdrops, and liquidations generate sudden fee spikes on EVM and Solana, stressing naïve heuristics. [Source: EIP-1559 Adoption Analysis, Blocknative, accessed 2025-11-30, https://www.blocknative.com/blog/eip-1559-adoption]
- **Protocol evolution**:
  - Ethereum L2s and EIP roadmaps (e.g., proto-danksharding) change baseline gas dynamics; Solana’s fee and prioritization mechanisms continue to evolve. [Source: Ethereum Improvement Proposal 1559, Buterin et al., 2019, https://eips.ethereum.org/EIPS/eip-1559; Source: Transaction Fees, Solana Docs, accessed 2025-11-30]
- **Competitive landscape**:
  - Leading non-custodial wallets and exchanges highlight “smart fee” features and stuck-tx recovery, raising user expectations.

### 3.3 Responsibility & room for maneuver

- **Wallet provider responsibilities**:
  - Design and operate robust, observable fee policies and lifecycle management; clearly communicate trade-offs and known limitations.
  - Choose vendors (oracles/RPCs) and redundancy patterns; own fallbacks and incident response.
- **Areas where others retain flexibility**:
  - Users may opt into manual fees or high-priority modes for time-sensitive flows.
  - Exchanges can adapt deposit-crediting policies (e.g., credit after fewer confirmations for small amounts) based on improved reliability.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **EVM-first heuristics**:
   - Early versions focused on EVM chains with simple `gasPrice` multipliers before EIP-1559, later adapted to base+tip but still using mostly static factors. [Source: EIP-1559 Gas Fees, Blocknative, accessed 2025-11-30]
2. **Gradual expansion to Bitcoin & Solana**:
   - Bitcoin and Solana support added as POCs with minimal fee-tuning and limited monitoring; fee logic largely copy-pasted from EVM approaches. [Source: Blockchain MPC Wallet Problem Extraction, Supplementary Analysis GPT5, 2025-11-28]
3. **Lack of dedicated fee ownership**:
   - Fee logic treated as a peripheral detail rather than a product surface with KPIs, leading to underinvestment in analytics and experimentation.

### 4.2 Background vs. direct causes

- **Background causes**:
  - Complexity and heterogeneity of fee markets across chains.
  - Dependency on external providers without strong SLAs or redundancy.
- **Direct triggers**:
  - Onboarding of Solana and additional EVM L2s increased variance and exposed the fragility of one-size-fits-all heuristics.
  - Volatile market events (e.g., NFT mints, major price moves) produced visible spikes in stuck transactions and user complaints.

### 4.3 Root issues

- No single owner accountable for “fee experience” (confirmation reliability + cost efficiency) across chains.
- Limited instrumentation: lack of granular metrics such as `fee_paid / median_fee_in_block`, confirmation-block distance, and success rate of replacements.
- Over-reliance on simple multipliers instead of explicit models of confirmation probability vs fee level per chain and tx-type.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory if unchanged

- As transaction volume and chain count grow, static fee heuristics will likely drive:
  - Increasing aggregate overspend, as conservative settings are used to avoid public incidents.
  - User migration toward competitors advertising smarter fee optimization and stuck-tx rescue.
  - Persistent support burden around stuck or delayed transactions.

### 5.2 Early signals

- Support tickets explicitly referencing “stuck” or “never confirmed” transactions across multiple chains.
- Product requests for “priority mode” or “auto unstick” features, indicating unmet needs.
- Ad-hoc scripts and manual interventions (bumping Bitcoin txs, resubmitting EVM txs with higher tips) by engineers and support.

### 5.3 6–24 month scenarios

- **Optimistic (with intervention)**:
  - Unified fee engine with per-chain models and lifecycle management cuts stuck-tx rate by ≥60% and overpayment by 20–40%; wallet markets itself on “predictable confirmations at fair fees,” supporting institutional SLAs.
- **Baseline (partial fixes)**:
  - Some heuristics improved for main EVM chains, but Bitcoin/Solana and new L2s remain flaky; support burden falls modestly, and competitive gap persists.
- **Pessimistic (no material change)**:
  - Fee experience becomes a key weakness; advanced users migrate to competitors, and institutional partners reduce reliance on the MPC wallet for time-sensitive flows.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- Strong blockchain engineering team already maintains integrations with multiple chains and RPC providers.
- Access to historical transaction and support data (failures, delays, ticket logs) that can guide modeling and experimentation.
- Commercial relationships with at least one or two fee-oracle/RPC vendors, providing starting points for deeper integrations. [Source: Estimate transaction fee (API Reference), Cobo Developers, accessed 2025-11-30]

### 6.2 Capability gaps

- Limited in-house expertise in statistical modeling of fee markets and confirmation probabilities.
- No dedicated observability stack for fee performance (e.g., dashboards showing `confirmation_delay` vs `fee_percentile` per chain).
- Lack of formal product ownership over “fee UX,” leading to diffuse responsibility.

### 6.3 Buildable capabilities (1–6 months)

- Assign a cross-functional “fee experience” pod (PM + lead engineer + data/analytics) with explicit KPIs (confirmation reliability, overpayment, stuck-tx tickets).
- Stand up initial fee telemetry pipelines that log fee levels, oracle recommendations, and confirmation outcomes by chain and tx type.
- Partner with key oracle/RPC vendors (e.g., Blocknative, Mempool.space, Solana RPC providers) to access richer signals or tailored APIs. [Source: Gas Price API | Gas Platform, Blocknative Docs, accessed 2025-11-30; Source: FAQ, mempool.space, accessed 2025-11-30]

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline (summary)

1. **Background**: Heterogeneous fee models across EVM, Bitcoin, and Solana; current wallet relies on static multipliers and basic oracles.
2. **Problem**: 10–20% of transactions fail to confirm promptly or get stuck; 30–50% overpayment during congestion; fragmented logic and limited observability.
3. **Analysis**: A unified fee policy engine with per-chain adapters, better data, and lifecycle management can materially improve both reliability and cost.
4. **Options**:
   - **Option A**: Deep integration with external fee oracles and mempool analytics.
   - **Option B**: Build internal empirical models using historical data + lightweight signals.
   - **Option C**: Hybrid of external oracles plus internal learning, with explicit SLAs and “fee modes”.
5. **Risks**: Overfitting to historical data, dependence on vendors, complexity of replacement logic, and UX confusion around dynamic fees.

### 7.2 Key judgments (to validate)

- **【P0】** Richer, chain-specific fee modeling will reduce stuck-tx rates by ≥60% vs simple multipliers at similar average cost. [Estimate: Based on gap between current 10–20% failure and desired ≥99% reliability; Medium confidence]
- **【P0】** Adding automated EVM bumping, Bitcoin RBF/CPFP flows, and Solana priority-fee adjustments will materially reduce manual interventions and tickets. [Source: Opt-in RBF FAQ, Bitcoin Core, accessed 2025-11-30; Source: How to use Priority Fees on Solana, Solana Developers, accessed 2025-11-30]
- **【P1】** A modest increase in estimation latency (≤100 ms p95) is acceptable to users if clearly communicated and yields better confirmations. [Estimate: Based on general UX tolerance for sub-200 ms additional latency; Medium confidence]

### 7.3 Alternative high-level paths

- **Option A – Oracle-centric strategy**:
  - Rely heavily on specialized providers (e.g., Blocknative for EVM, Mempool.space for Bitcoin, tailored Solana RPCs) with redundancy.
- **Option B – Data-driven in-house models**:
  - Build internal models of confirmation probability vs fee using stored transaction histories.
- **Option C – Hybrid policy engine**:
  - Combine external signals with internal learning and guardrails; treat vendor feeds as features, not truth.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Vendor bias**: Over-trusting marketing claims of oracle providers without validating performance in the wallet’s specific traffic patterns.
- **Engineering optimism**: Underestimating complexity of cross-chain replacement logic and corner cases (e.g., chained unconfirmed Bitcoin txs, Solana local program congestion). [Source: FAQ, mempool.space, accessed 2025-11-30]
- **Recency bias**: Overfocusing on recent congestion events while underweighting rare but extreme fee spikes.

### 8.2 Required intelligence

- Per-chain distributions of confirmation delay vs. fee percentile (e.g., what tip percentile is needed for next-block, 3-block, etc.). [Source: Gas Price API | Gas Platform, Blocknative Docs, accessed 2025-11-30]
- Correlation between fee policies and support tickets (before/after changes).
- Comparative evaluation of multiple oracle providers along latency, accuracy, uptime, and cost dimensions.
- User research on acceptable ranges of fee variability and transparency preferences.

### 8.3 Validation plan

1. **Baseline measurement (Month 1)**:
   - Instrument end-to-end fee and confirmation metrics by chain, tx size, urgency level.
2. **Pilot improved policy on one or two chains (Months 2–3)**:
   - For example, roll out enhanced EIP-1559 logic (using richer Blocknative data) and automated Bitcoin RBF for a subset of users; compare stuck-tx rate and overpayment vs control. [Source: EIP-1559 Gas Fees, Blocknative, accessed 2025-11-30; Source: Opt-in RBF FAQ, Bitcoin Core, accessed 2025-11-30]
3. **Cross-chain generalization (Months 3–5)**:
   - Extend learnings to Solana and additional EVM L2s, adjusting models per chain.
4. **Continuous learning**:
   - Periodically retrain or recalibrate models and thresholds based on new data.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Estimated gains in overpayment reduction or stuck-tx rate may need adjustment after observing real-world behavior under extreme congestion.
- Relative value of external vs internal signals might shift if vendor performance or pricing changes.

### 9.2 Incremental approach

- Start with **instrumentation and reporting** without changing user-visible behavior.
- Introduce **conservative improvements first** (e.g., better EIP-1559 parameterization using Blocknative data) before enabling aggressive bumping strategies.
- Gradually **expand automation scope** (Bitcoin RBF, Solana priority adjustments) with kill switches and per-cohort rollouts.

### 9.3 “Good enough” criteria

- For each chain, at least **95–99%** of standard-priority txs confirming within target block/slot windows.
- Overpayment reduced by ≥20% relative to current baselines while keeping failure rates within targets.
- Support-ticket share for fee-related/stuck-tx issues reduced by ≥60%.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. The main issue is not just “guessing gas” but managing **confirmation risk and cost** across heterogeneous fee markets.
2. Relying on static, chain-specific multipliers and basic oracles is structurally inadequate for volatile EVM, Bitcoin, and Solana environments. [Source: How to Estimate and Optimize Transaction Fees for MPC Wallets, Cobo Developers, accessed 2025-11-30; Source: FAQ, mempool.space, accessed 2025-11-30]
3. A unified fee policy engine with **per-chain adapters**, richer data, and **lifecycle management** (monitoring + bumping/replacement) can materially improve reliability and fee efficiency.
4. Success requires **dedicated ownership, observability, and staged experiments**, not only adding another oracle.

### 10.2 Near-term action list (0–3 months)

1. **【P0 – Critical】 Establish fee experience ownership and KPIs** → Product & Eng Leads → Metric: formal owner and KPI dashboard in place (confirmation reliability, overpayment, stuck-tx tickets) → by 2025-01-31.
2. **【P0 – Critical】 Implement fee telemetry baseline** → Data/Infra Lead → Metric: ≥95% of outbound txs log chain, fee parameters, oracle recommendations, confirmation delay → by 2025-02-15.
3. **【P1 – Important】 Integrate richer EVM gas data (e.g., Blocknative) and refine EIP-1559 policy** → Blockchain Eng → Metric: EVM stuck-tx rate reduced by ≥40% in pilot cohort without ≥10% fee increase → by 2025-03-31. [Source: Gas Price API | Gas Platform, Blocknative Docs, accessed 2025-11-30]
4. **【P1 – Important】 Design and pilot automated Bitcoin RBF and Solana priority-fee bumping** → Blockchain Eng → Metric: ≥80% reduction in manual “unstick” interventions in pilot cohorts → by 2025-04-30. [Source: Opt-in RBF FAQ, Bitcoin Core, accessed 2025-11-30; Source: How to use Priority Fees on Solana, Solana Developers, accessed 2025-11-30]
5. **【P2 – Optional】 Explore internal modeling of confirmation probability** → Data Science / Eng → Metric: Prototype model that predicts required fee percentile for target confirmation windows with calibration error <10% on holdout data → by 2025-05-31.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Overfitting policies to recent data, failing under new congestion patterns | High | Medium | Surge of stuck txs in new market event despite recent improvements | Use rolling windows, stress-testing, and backtesting across historical spikes; maintain manual override options | Data & Eng Leads |
| Excessive dependence on a single oracle/RPC vendor | High | Medium | Vendor outage or degraded accuracy significantly impacts confirmations | Multi-vendor strategy, health checks, automatic failover, and periodic vendor benchmarking | Infra Lead |
| UX confusion about dynamic fee changes and replacements | Medium | Medium | Users complain about unexpected fee amounts or multiple on-chain txs per action | Clear UX copy, activity logs showing replacements, opt-in “advanced details” view | Product & UX |
| Implementation bugs in replacement logic causing double-spends or unexpected failures | High | Low–Medium | Incidents involving malformed replacements or rejected txs | Rigorous test suites, canary deployments, on-chain monitoring, and external review when touching Bitcoin/EVM low-level logic | Blockchain Eng Lead |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Oracle-centric (deep vendor integration)** | Fastest path to richer signals; offloads modeling complexity to specialists | Ongoing vendor fees; strong vendor lock-in | Outage or model changes outside of control | When budget is available and strong vendors cover key chains | When risk appetite for vendor lock-in is low or chains lack strong vendors |
| **B. In-house modeling (data-driven)** | Maximum control and adaptability; can be tuned to wallet’s specific traffic | Requires data science capacity and ongoing maintenance | Mis-specified models; higher initial complexity | When sufficient data & analytics skills exist | When data volume or expertise is insufficient |
| **C. Hybrid policy engine (oracles + models)** | Balanced resilience and performance; can blend multiple sources | Highest design complexity; more moving parts | Coordination overhead; harder debugging | When scale and importance justify sophisticated fee management | Very early-stage or resource-constrained situations |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **Gas fee (EVM)** | Total amount paid for executing a transaction on an EVM chain, consisting of burned base fee and priority fee (tip) within `maxFeePerGas` bounds | gwei × gas units | [Source: EIP-1559 Gas Fees: Base Fee, Priority Fee, & Max Fee, Blocknative, accessed 2025-11-30] |
| **Base fee (EVM)** | Protocol-set minimum fee per gas burned in each block, adjusted up/down based on block utilization | gwei | [Source: Ethereum Improvement Proposal 1559, Buterin et al., 2019] |
| **Max fee / MaxFeePerGas** | User-specified maximum total fee per gas they are willing to pay under EIP-1559 | gwei | [Source: EIP-1559 Gas Fees, Blocknative, accessed 2025-11-30] |
| **Priority fee / MaxPriorityFeePerGas** | Portion of the fee per gas paid to validators/miners as an inclusion tip under EIP-1559 | gwei | [Source: EIP-1559 Gas Fees, Blocknative, accessed 2025-11-30] |
| **sat/vbyte** | Satoshis per virtual byte; standard fee-rate unit for Bitcoin transactions | sat/vB | [Source: FAQ, mempool.space, accessed 2025-11-30] |
| **Replace-By-Fee (RBF)** | Mechanism allowing a Bitcoin transaction flagged as replaceable to be superseded by a new version with higher fee rate | N/A | [Source: Opt-in RBF FAQ, Bitcoin Core, accessed 2025-11-30] |
| **Child-Pays-For-Parent (CPFP)** | Technique where a new Bitcoin transaction with high fee rate confirms together with its low-fee parent, effectively boosting the parent’s effective fee | N/A | [Source: FAQ, mempool.space, accessed 2025-11-30] |
| **Compute unit (Solana)** | Abstract unit representing computational cost of executing instructions in a Solana transaction | CU | [Source: Transaction Fees, Solana Docs, accessed 2025-11-30] |
| **Priority fee (Solana)** | Optional fee per compute unit (in micro-lamports per CU) used to prioritize Solana transactions | micro-lamports/CU | [Source: How to use Priority Fees on Solana, Solana Developers, accessed 2025-11-30; Source: Understand Solana Priority Fees, QuickNode, accessed 2025-11-30] |
| **Gas oracle** | Service providing recommended fee levels based on recent blocks and mempool state | N/A | [Source: Gas Price API | Gas Platform, Blocknative Docs, accessed 2025-11-30; Source: Estimate transaction fee (API Reference), Cobo Developers, accessed 2025-11-30] |
| **p95 confirmation latency** | Time by which 95% of transactions have been confirmed on-chain, measured from submission to inclusion | blocks/slots or seconds | Defined for this analysis as a core reliability KPI |
| **Mempool** | Set of unconfirmed transactions known to a node; basis for estimating required fees for timely confirmation | N/A | [Source: FAQ, mempool.space, accessed 2025-11-30] |

---

## 12. References

### Tier 1 – Protocols & Official Documentation

1. **Buterin, V. et al.** (2019). *EIP-1559: Fee market change for ETH 1.0 chain*. Ethereum Improvement Proposal 1559. https://eips.ethereum.org/EIPS/eip-1559 **[Cited in: Context Recap, 3.2, 11]**
2. **Bitcoin Core Developers.** (n.d.). *Opt-in RBF FAQ*. Bitcoin Core Project. https://bitcoincore.org/en/faq/optin_rbf/ **[Cited in: Context Recap, 2.1, 7.2, 8.3, 10.2, 10.3, 11]**
3. **Solana Foundation.** (n.d.). *Transaction Fees*. Solana Documentation. https://solana.com/docs/core/fees **[Cited in: Context Recap, 2.1, 3.2, 6.3, 11]**

### Tier 2 – Industry Guides & Platforms

4. **Blocknative.** (n.d.). *EIP-1559 Gas Fees: Base Fee, Priority Fee, & Max Fee*. https://www.blocknative.com/blog/eip-1559-fees **[Cited in: Context Recap, 1.1, 2.1, 2.2, 3.2, 7.1, 8.3, 10.1, 11]**
5. **Blocknative.** (n.d.). *Gas Price API | Gas Platform*. https://docs.blocknative.com/gas-prediction/gas-platform **[Cited in: Context Recap, 2.1, 2.2, 3.2, 6.3, 7.2, 8.2, 8.3, 10.2, 11]**
6. **Cobo.** (n.d.). *How to Estimate and Optimize Transaction Fees for MPC Wallets*. Cobo Developers Guide. https://www.cobo.com/developers/v1/guides/howtos/estimate-transaction-fees **[Cited in: Context Recap, 1.1, 6.1, 10.1]**
7. **Cobo.** (n.d.). *Estimate transaction fee – API Reference*. Cobo Developer Hub. https://www.cobo.com/developers/v2/api-references/transactions/estimate-transaction-fee **[Cited in: Context Recap, 2.1, 6.1, 6.3, 11]**
8. **mempool.space.** (n.d.). *FAQ – mempool explorer*. https://mempool.space/docs/faq **[Cited in: Context Recap, 2.1, 2.3, 6.3, 7.1, 8.1, 11]**
9. **Solana Foundation.** (n.d.). *How to use Priority Fees on Solana*. https://solana.com/developers/guides/advanced/how-to-use-priority-fees **[Cited in: Context Recap, 2.1, 3.2, 6.3, 7.2, 10.2, 11]**
10. **QuickNode.** (n.d.). *Understand Solana Priority Fees: Land Transactions Faster*. https://www.quicknode.com/guides/solana-development/transactions/how-to-use-priority-fees **[Cited in: Context Recap, 2.1, 3.2, 11]**

### Internal / Supplementary Sources

11. **Blockchain MPC Wallet Problem Extraction.** (2025-11-28). *Supplementary Analysis GPT5*. Internal document. **[Cited in: Context Recap, 1.1, 2.1]**
12. **Internal fee-performance dashboards & ticket analytics.** (2024–2025). *Stuck transaction rates, fee overpayment estimates, support ticket breakdowns*. Engineering & Support teams. **[Planned for: 1.1, 5.1, 6.1, 8.2]**

### Estimates & Assumptions

13. **Fee efficiency and reliability improvement projections.** Method: Extrapolation from current metrics, general behavior of fee markets, and capabilities of oracle platforms. Confidence: Medium. Validation: A/B tests comparing current vs new fee policies across chains. **[Used in: 1.2, 5.3, 7.2, 9.1]**
