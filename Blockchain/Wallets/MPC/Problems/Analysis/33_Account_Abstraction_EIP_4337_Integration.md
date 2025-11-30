# Account Abstraction (EIP-4337) Integration with MPC Wallets – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Blockchain Engineering & Product Team

---

## Pre-Section: Context Recap

- **Problem title**: Production-grade integration of EIP-4337 Account Abstraction with MPC wallets (AA+MPC) for gasless onboarding and advanced UX
- **Current state**:
  - EIP-4337 introduces UserOperation objects, an alternative mempool, bundlers, an EntryPoint contract, and paymasters to enable smart contract wallets without consensus changes [Source: ERC-4337: Account Abstraction Using Alt Mempool, Buterin et al., Ethereum Foundation, 2023, Abstract & Specification].
  - Smart contract wallets built on ERC-4337 support programmable authorization, batched calls, fee sponsorship, and flexible recovery mechanisms [Source: ERC-4337 Documentation – What is ERC-4337?, eth-infinitism, 2024].
  - Early AA+MPC proofs of concept (POCs) using third-party bundlers and paymasters suffer from 5–15% UserOperation submission failures due to bundler outages, paymaster funding/policy rejections, and MPC signature packing mismatches with account validation logic [Source: Problem statement – Background and current situation; Supplementary Analysis, GPT5.md, 2025-11-28].
- **Pain points**:
  - UserOperation failures degrade UX for gasless onboarding and small-value transactions, undermining the business case for AA-powered flows.
  - Dependence on a small set of third-party bundler and paymaster providers introduces availability and vendor-lock risks.
  - MPC-generated signatures (ECDSA/EdDSA) must be packed exactly as expected by different smart account implementations (e.g., SimpleAccount, Safe, Kernel), increasing integration complexity and CI fragility [Source: Problem statement – Background and current situation].
- **Goals**:
  - Achieve ≥99% UserOperation submission success across supported EVM chains (Ethereum, Polygon, Arbitrum, Optimism, Base).
  - Limit additional AA-induced latency overhead to ≤300 ms p95 compared to direct EOA transactions.
  - Maintain seamless fallback for existing EOA users (no address changes) while enabling AA features for new and opted-in users.
  - Provide gas sponsorship for ≥80% of onboarding transactions and most sub‑$50 flows via paymasters.
  - Ensure bundler availability ≥99.5% with automated failover across at least two providers per chain.
  - Reach production readiness for AA+MPC in 4–6 months (Q1–Q2 2025) [Source: Problem statement – Goals and success criteria].
- **Hard constraints**:
  - Bundler and paymaster infrastructure is still maturing; SLAs vary and vendor concentration is high [Source: ERC-4337 Documentation – Introduction & Resources, eth-infinitism, 2024; QuickNode – Account Abstraction and ERC‑4337, 2024].
  - Backward compatibility: existing EOA addresses for users and partners (e.g., exchanges) cannot be changed without high operational risk.
  - Engineering capacity: ~2 FTE blockchain engineers + 0.5 FTE smart contract engineer for 4–6 months; budget ≈$80k implementation + $10k–20k/month for bundler/paymaster services and gas sponsorship [Source: Problem statement – Key constraints and resources].
- **Key facts**:
  - ERC-4337 defines UserOperation structures, the EntryPoint contract, bundler behavior, and an extension for paymasters that can sponsor gas or accept ERC‑20 fees [Source: ERC-4337: Account Abstraction Using Alt Mempool, Ethereum Foundation, 2023, Specification].
  - Smart contract wallets using ERC-4337 are already live on Ethereum mainnet and major L2s, with multiple infrastructure providers (Stackup, Alchemy, Pimlico, etc.) offering bundler and paymaster services [Source: ERC-4337 Documentation – Introduction & Smart Accounts, eth-infinitism, 2024; Crypto.com University – Guide to ERC‑4337, 2023].
  - MPC wallets are widely used by custodians and WaaS providers to split private keys across devices/parties, but AA+MPC integration patterns and best practices are not yet standardized [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

1. **Core problem**  
   The organization wants to combine MPC wallets (for threshold key security) with EIP-4337 Account Abstraction (for UX features like gasless onboarding and programmable authorization), but current AA+MPC integrations show 5–15% UserOperation failure rates, bundler/paymaster fragility, and signature compatibility issues, preventing production rollout [Source: Problem statement – Brief description & Background].

2. **Key contradictions**
   - **Security vs. UX & complexity**: MPC enhances key security via multi-party signing, while AA enables programmability and gas abstraction. Together they create a more complex signing and validation pipeline (MPC protocol → UserOperation signing → smart account validation → paymaster checks) that is harder to reason about and test, yet user expectations for "one-click gasless" UX are high [Source: ERC-4337 Documentation – What is ERC‑4337?, 2024; Stackup – MPC Wallets Guide, 2025].
   - **Decentralization vs. operational guarantees**: ERC‑4337 relies on permissionless bundlers and paymasters to preserve decentralization, but product teams require predictable SLAs and observability comparable to centralized relayers [Source: ERC-4337 Spec – Bundler Behavior, 2023; QuickNode – Account Abstraction and ERC‑4337, 2024].
   - **Backward compatibility vs. innovation speed**: Maintaining existing EOAs and deposit addresses limits how aggressively AA features can be rolled out (e.g., dual-path logic, selective migration), but delaying AA adoption slows UX innovations and competitive positioning.

3. **Who is in conflict?**
   - Blockchain engineers vs. product/UX: engineers push for staged rollout, strict SLAs, and robust monitoring; product pushes for rapid gasless onboarding in as many flows as possible.
   - Internal reliability/SRE teams vs. external providers: SRE requires transparent incident reporting, failover contracts, and deterministic behavior; bundler/paymaster vendors optimize for growth and multi-tenant economics.
   - Compliance/finance vs. growth marketing: compliance wants spend caps, abuse detection, and clear audit trails for sponsored gas; growth wants aggressive subsidies to drive activation.

### 1.2 Goals & conditions

- **Reliability**: ≥99% UserOperation submission success and ≥99.5% effective bundler availability across chains [Estimate based on: typical web and mobile product SLOs for critical flows, Medium confidence].
- **Performance**: AA+MPC pipeline adds ≤300 ms p95 latency compared to direct EOA flow, including MPC signing, UserOperation construction, bundler RPC calls, and EntryPoint validation [Source: Alchemy – How ERC-4337 Smart Contract Wallets Work, 2024; Stackup – MPC Wallets Performance Benchmarks, 2025].
- **Coverage**: Gasless or sponsored flows for ≥80% onboarding transactions and a significant share of sub‑$50 transactions, with clear sponsorship policies.
- **Compatibility**: Support top 3 smart account implementations (e.g., SimpleAccount, Safe-style accounts, Kernel-like modular accounts) and ensure 99.99% validation success in CI test matrix across chains [Estimate based on: CI coverage expectations for core infra, Medium confidence].
- **Timeline & resources**: 4–6 months with limited engineering and budget as described in the context recap.

### 1.3 Extensibility & reframing

- **Attribute reframing – "one object, many attributes"**:  
  The "object" is the transaction pipeline from user intent to on-chain execution. Attributes include (1) key management model (MPC vs. EOA), (2) account model (EOA vs. smart account), (3) gas payment path (user vs. paymaster), (4) infrastructure path (single vs. multi-bundler), and (5) chain selection (mainnet vs. L2). Framing the problem as "optimizing the full pipeline" avoids tunnel vision on only signatures or only bundlers [Source: ERC-4337 Spec – UserOperation & EntryPoint, 2023; Stackup – MPC Wallets Guide, 2025].
- **Scope reframing – AA as feature tier**:  
  Instead of "all users must move to AA+MPC", treat AA features as a configurable tier: high-friction but gasless UX for new retail users and selective opt-in for existing users, while high-value institutional flows may stay on hardened MPC+EOA paths until AA infra matures.
- **Risk reframing – infra dependence vs. internal control**:  
  View bundlers and paymasters as critical external dependencies akin to payment processors, requiring redundancy, contracts, and monitoring, not just as SDK integrations.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **Smart accounts and EntryPoint**: ERC‑4337 smart accounts implement custom validation and execution logic and are orchestrated via the EntryPoint contract, which validates and executes batched UserOperations [Source: ERC‑4337 Spec – EntryPoint Interface, 2023].
- **UserOperation structure**: Each UserOperation encodes sender, nonce, initCode, callData, gas limits, fee parameters, and optional paymasterAndData; the signature must bind chain ID and EntryPoint to prevent replay [Source: ERC‑4337 Spec – UserOperation Structure, 2023].
- **Bundlers**: Off-chain actors that collect UserOperations, validate them, simulate them, and submit handleOps transactions to the EntryPoint; they bear gas cost and are reimbursed by accounts or paymasters [Source: ERC‑4337 Spec – Bundler Behavior, 2023; Alchemy – How ERC‑4337 Smart Contract Wallets Work, 2024].
- **Paymasters**: Contracts that can sponsor gas, implement custom policies, and optionally accept ERC‑20 fees, by implementing validatePaymasterUserOp and postOp [Source: ERC‑4337 Spec – Extension: Paymasters, 2023; Alchemy – What Is a Paymaster?, 2024].
- **MPC signing service**: Off-chain MPC engine that holds key shares and produces signatures compatible with the smart account’s validation logic (e.g., packed ECDSA or aggregated signatures), with its own latency and availability characteristics [Source: Stackup – MPC Wallets Guide, 2025].
- **Fallback paths**: Dual-path logic for EOAs vs. AA accounts, including migration rules, address continuity, and feature detection in clients.

### 2.2 Balance & "degree" issues

- **Gas sponsorship scope**: Sponsoring too many transactions (e.g., all sub‑$100) can lead to unsustainable spend and abuse; sponsoring too few undermines UX gains. A calibrated policy (e.g., onboarding flows + selected low-value actions) balances CAC/ROI vs. fraud risk [Source: Crypto.com University – Advantages of Abstracting Accounts, 2023; Alchemy – Paymaster Guide, 2024].
- **Validation depth vs. latency**: Heavier on-chain validation (signature aggregation, complex paymaster logic, multi-step checks) improves safety but increases gas and execution time; some checks are better offloaded to off-chain risk engines feeding into paymaster decisions.
- **Multi-bundler diversity vs. operational complexity**: Adding multiple bundlers improves resilience but multiplies integration, monitoring, and testing overhead. At small scale, 2–3 providers may be optimal; more may add marginal benefit.

### 2.3 Causal chains

1. **Bundler dependency chain**:  
   Single bundler → maintenance/outage or configuration bug → 100% UserOperation failures for AA flows → sudden UX degradation and support load → erosion of trust in AA features [Source: Problem statement – Historical attempts; ERC‑4337 Spec – Bundler Behavior, 2023].

2. **MPC signature incompatibility chain**:  
   MPC engine outputs ECDSA/EdDSA signatures with non-standard encoding → smart account validateUserOp expects specific r/s/v or aggregator format → validation revert in EntryPoint → UserOperation dropped by bundlers after failed simulation → inflated failure rates and difficult debugging [Source: Problem statement – Background & Known facts].

3. **Paymaster risk & budget chain**:  
   Aggressive sponsorship policy + limited monitoring + volatile gas prices → paymaster deposit depleted or risk engine overreacts → validatePaymasterUserOp reverts, causing widespread sponsored tx failures → degraded UX precisely during high-traffic periods [Source: ERC‑4337 Spec – Paymasters, 2023; Alchemy – Paymaster Overview, 2024].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and conflicts

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | Ethereum protocol researchers, ERC‑4337 spec authors, smart account & wallet library maintainers | Preserve decentralization and security while enabling richer accounts and UX | Cannot guarantee behavior of bundlers/paymasters or every implementation; must keep spec generic | Product teams want opinionated, turnkey patterns; researchers aim for flexible standards |
| Downstream | MPC wallet providers, dApp teams, infrastructure platforms offering AA SDKs | Deliver gasless, secure, low-friction UX; differentiate products | Limited budget, legacy EOAs, vendor SLAs, multi-chain fragmentation | Pressure to ship quickly vs. need for robust failover and monitoring |
| Sideline / External | End users, institutions, regulators, chain analytics, security researchers | Safe, cheap, simple UX; clear accountability for failures; regulatory compliance | Limited visibility into infra, evolving standards, cross-chain complexity | Users may distrust complex flows; regulators may treat AA differently from EOAs |

[Source: ERC‑4337 Documentation – Why This Documentation?, 2024; Stackup – MPC Wallets Guide, 2025; Crypto.com University – ERC‑4337 Standard and Account Abstraction, 2023].

### 3.2 Environmental factors

- **Regulatory and compliance pressure**: Custodial and quasi-custodial services must show strong controls over transaction authorization and spend of sponsored gas; AA+MPC architectures must produce auditable logs and enforce sanctions/compliance rules [Source: Industry custody & compliance guidance summarized in Stackup – MPC Wallets Guide, 2025].
- **Market competition**: Competing wallets emphasize smooth onboarding (email/social login, no seed phrases) and subsidized gas; AA is becoming a differentiator in enterprise WaaS and consumer wallets [Source: Crypto.com University – Future of Account Abstraction, 2023; ERC‑4337 Docs – What is ERC‑4337?, 2024].
- **Standard evolution**: Future proposals (e.g., EIP‑7702) may change how EOAs and smart accounts interact, including temporary delegation and authorization tuples, affecting long-term architecture decisions [Source: ERC‑4337 Spec – Support for EIP‑7702, 2023].

### 3.3 Responsibility & room for maneuver

- **Internal teams** are responsible for AA+MPC architecture, vendor selection, risk policies, and monitoring. They can choose conservative rollout strategies, multi-provider setups, and explicit kill switches for AA flows.
- **Bundler/paymaster providers** own infra reliability and SDK quality; they can publish SLAs, incident reports, and reference integrations tailored for MPC-backed wallets.
- **Standards community** can publish best-practice profiles for AA+MPC (e.g., standardized signature packing, recommended monitoring events) to reduce fragmentation.

[Source: ERC‑4337 Documentation – Resources, 2024; QuickNode – Account Abstraction and ERC‑4337, 2024].

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2017–2020 – Rise of MPC custody**:  
   Major exchanges and custodians deploy MPC wallets to reduce single-key compromise risk, using threshold ECDSA/EdDSA protocols [Source: Stackup – MPC Wallets Guide, 2025].
2. **2023 – ERC‑4337 deployed**:  
   Ethereum community finalizes and deploys ERC‑4337 to production, enabling account abstraction via UserOperations and EntryPoint without consensus changes [Source: ERC‑4337 Spec – Abstract & Motivation, 2023; Crypto.com University – ERC‑4337 Standard, 2023].
3. **2023–2024 – AA infra providers launch**:  
   Bundler and paymaster services (e.g., Stackup, Alchemy, Pimlico) appear, offering SDKs for AA wallets and dApps [Source: ERC‑4337 Docs – Smart Accounts & Ecosystem, 2024; Alchemy – How ERC‑4337 Smart Contract Wallets Work, 2024].
4. **2024–2025 – Early AA+MPC POCs**:  
   Wallet teams integrate MPC backends with AA smart accounts using third-party providers; they uncover failure modes around bundler outages, signature packing mismatches, and opaque paymaster rejections [Source: Problem statement – Historical attempts].

### 4.2 Background vs. direct causes

- **Background causes**:
  - AA and MPC evolved mostly in parallel communities (smart contract UX vs. custody security), leading to integration gaps.
  - AA ecosystem is young; standards around bundler SLAs, paymaster policies, and observability are still emerging.
- **Direct causes**:
  - Tight coupling to individual bundler/paymaster providers without robust failover.
  - Limited end-to-end test coverage that combines MPC signing, UserOperation construction, chain-level simulation, and production-like paymaster policies.
  - Semi-opaque vendor behavior (e.g., rejection reasons encoded in internal metrics but not fully surfaced to clients).

### 4.3 Root issues

- **Architecture treated AA as an "add-on"** rather than a re-architecture of the whole transaction pipeline, leading to partial integration and unmodeled failure modes.
- **Insufficient reliability engineering around external infra**: Bundlers and paymasters are as critical as RPC providers, but historically have not been given the same rigor in SLAs, redundancy, and chaos testing.
- **Gaps in shared standards for AA+MPC**: No widely adopted profiles for signature formats, error codes, or telemetry fields tailored to MPC-backed accounts.

[Source: ERC‑4337 Spec – Bundler & Paymaster sections, 2023; Stackup – MPC Wallets Guide, 2025; Problem statement – Historical attempts & Lessons].

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- AA adoption is expected to grow as more wallets and dApps integrate smart accounts and gasless flows, increasing traffic through bundlers and paymasters [Source: ERC‑4337 Docs – Why This Documentation?, 2024; Crypto.com University – Future of Account Abstraction, 2023].
- If AA+MPC remains fragile (5–15% failure rates, unpredictable behavior), teams may restrict AA usage to non-critical flows or abandon it, losing competitive advantage.
- Reliance on a small set of AA infra providers could create systemic risk: a major outage or policy change could simultaneously affect many wallets.

### 5.2 Early signals

- Growing number of AA SDKs and wallets (e.g., embedded wallets, email/social login products) built on ERC‑4337 [Source: ERC‑4337 Docs – Smart Accounts & Ecosystem, 2024; Alchemy – Smart Contract Wallet Overviews, 2024].
- Infrastructure vendors increasingly advertise high-availability bundlers and configurable paymasters, implying demand for production-level reliability rather than experimental POCs.
- Internal metrics from POCs showing non-trivial UserOperation rejection rates and latency spikes during infra incidents.

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**:  
  Wallet adopts multi-bundler, multi-paymaster architecture, standardized signature formats, and robust observability. AA+MPC achieves ≥99% success and sub‑300 ms overhead; gasless onboarding becomes default for new users. AA infra matures with clearer SLAs and standard telemetry.

- **Baseline scenario**:  
  AA+MPC is rolled out selectively (e.g., to new retail cohorts and specific dApps), with fallbacks to EOA+MPC for institutional and high-value flows. Occasional infra incidents cause short-lived AA degradation but not systemic outages.

- **Pessimistic scenario**:  
  A major bundler/paymaster outage or misconfiguration affects multiple providers or networks simultaneously, causing widespread AA failures. Some wallets disable AA features and revert to EOAs; regulators scrutinize sponsored gas and programmable accounts more heavily.

[Estimate based on: early AA adoption curves, reliability requirements in financial apps, and standardization timelines for new infra components, Medium confidence].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Cryptography and MPC expertise**: The team already operates MPC wallets in production, implying strong skills in threshold signing, key management, and security reviews [Source: Stackup – MPC Wallets Guide, 2025].
- **Smart contract experience**: Existing EVM integrations and internal smart contracts provide a foundation for implementing smart accounts, paymasters, and custom AA logic.
- **Monitoring and SRE practices**: Current infrastructure likely uses observability stacks (metrics, logs, traces) for blockchain operations that can be extended to AA components.

### 6.2 Capability gaps

- **AA-specific reliability engineering**: Limited experience with alt-mempools, multi-bundler routing, and EntryPoint-specific failure patterns (e.g., simulation-only errors, reputational bans) [Source: ERC‑4337 Spec – Bundler Behavior & Reputation, 2023].
- **Policy design for sponsorship**: Need structured frameworks for when to sponsor gas, how to cap costs, and how to detect abuse while preserving UX [Source: Alchemy – Paymaster Overview, 2024; Crypto.com – Advantages of Abstracting Accounts, 2023].
- **Standardized telemetry & error taxonomy**: Currently, error codes and logs for AA components may be ad hoc, complicating cross-provider analysis.

### 6.3 Buildable capabilities (1–6 months)

- Develop an **AA+MPC reference architecture** including:
  - Abstracted routing layer for multiple bundlers.
  - Canonical UserOperation construction library tightly integrated with MPC engine.
  - A standard error taxonomy and structured logging for UserOperation lifecycle events.
- Build a **paymaster policy engine** that evaluates sponsorship decisions using off-chain data and risk scores, with clear configuration and simulation modes.
- Implement **AA-specific observability**: dashboards for UserOperation success rates, rejection reasons, bundler latency, and paymaster balance/usage.

[Estimate based on: typical infra refactor timelines and integration complexity, Medium confidence].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: ERC‑4337 introduces programmable smart accounts via UserOperations, bundlers, EntryPoint, and paymasters. MPC wallets secure keys by splitting them across parties.
- **Problem**: Early AA+MPC integrations show high UserOperation failure rates and infra fragility, blocking rollout of gasless and advanced UX features.
- **Analysis**: Internal logic (pipeline structure, dependencies), external factors (market, regulation, standard evolution), historical origins, trends, and capability gaps.
- **Options**: (A) Minimal AA adoption; (B) Targeted AA+MPC rollout with strong reliability and monitoring; (C) Aggressive AA-first strategy.
- **Risks**: Infra outages, vendor lock-in, cost overruns on gas sponsorship, and long-term standard shifts (e.g., EIP‑7702).

### 7.2 Key judgments (for validation)

1. A **multi-bundler, multi-paymaster architecture** is necessary to reach production-grade reliability for AA+MPC.
2. Carefully scoped gas sponsorship (onboarding, low-value transactions) can yield positive ROI when combined with strong abuse detection.
3. AA+MPC should initially target **retail UX improvements** and low/medium-value flows, while institutional and high-value flows stay on hardened MPC+EOA until AA infra and standards mature.

### 7.3 Alternative high-level paths

- **Path A – Minimal AA**: Use AA only for niche flows or experiments; keep core business on EOA+MPC.
- **Path B – Targeted AA rollout (recommended)**: Prioritize onboarding and selected flows, with multi-provider redundancy and strong observability.
- **Path C – AA-first**: Rapidly migrate most flows to AA+MPC, accepting higher infra and organizational risk.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- **Technology optimism**: Overestimating how quickly AA infra and standards will stabilize.
- **Vendor trust**: Assuming bundler/paymaster providers will always behave predictably and transparently.
- **Retail-centric view**: Focusing on UX for small users while underweighting institutional risk tolerance and regulatory expectations.

[Source: ERC‑4337 Docs – Why This Documentation?, 2024; Stackup – MPC Wallets Guide, 2025].

### 8.2 Required intelligence

- Detailed benchmarking of:
  - AA+MPC latency vs. baseline EOA+MPC across chains.
  - UserOperation success/failure reasons across multiple bundlers.
- Vendor data on historical uptime, incident frequency, and postmortems for bundlers/paymasters.
- Empirical CAC/retention impact of gasless onboarding vs. traditional flows.

### 8.3 Validation plan

- Run **staged pilots**:
  - Pilot 1: Limited user cohort on one L2 with single bundler and restricted sponsorship policies → measure reliability and cost.
  - Pilot 2: Multi-bundler setup with failover tests → validate reliability assumptions.
  - Pilot 3: Expanded user base and chains → validate scalability and business metrics.
- Incorporate **chaos testing** for bundler and paymaster outages to validate fallbacks.

[Estimate based on: standard reliability and product experimentation practices, Medium confidence].

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Relative weighting of AA vs. EOA flow usage may change as AA infra matures and new standards (e.g., EIP‑7702) are adopted.
- Sponsorship policies may be tightened or relaxed based on real-world fraud and abuse patterns.
- Preferred vendors and architecture patterns may shift as more providers enter the market or consolidate.

### 9.2 Incremental approach

- Start with **opt-in AA** for new users on selected chains.
- Introduce **multi-bundler support** behind a feature flag, with canary traffic.
- Gradually expand **AA coverage** and sponsorship budgets based on measured ROI and reliability.

### 9.3 "Good enough" criteria

- AA+MPC flows show ≥99% UserOperation success, with stable error distributions and clear mitigation playbooks.
- Bundler outages or vendor changes can be handled within SLOs using automated failover.
- Sponsored gas spend is within budget and shows positive impact on activation and retention.

[Estimate based on: internal SLO practices and product metrics frameworks, Medium confidence].

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. ERC‑4337 provides a powerful but complex framework for programmable smart accounts; combining it with MPC wallets requires holistic pipeline design rather than ad hoc integration [Source: ERC‑4337 Spec – Abstract & Specification, 2023; Stackup – MPC Wallets Guide, 2025].
2. Single-provider dependencies and opaque failure modes are the main blockers to production AA+MPC adoption; multi-bundler, multi-paymaster setups with strong observability are essential.
3. AA is best introduced as a **targeted UX lever** for onboarding and low/medium-value flows, not yet as a universal replacement for EOA-based infrastructure.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

- **【P0 – Critical】**
  1. Design and implement an **AA+MPC reference architecture** (multi-bundler, paymaster integration, dual-path EOA+AA routing) → Blockchain Architecture Lead → Architecture doc: draft → approved; PoC environments: 0 → 1 per major chain → 2025-01-31.
  2. Build a **canonical UserOperation construction and signing library** integrated with MPC engine → Protocol Engineering → CI validation success across target smart account implementations: <99% → ≥99.99% → 2025-02-15.

- **【P1 – Important】**
  3. Implement **AA-specific observability** (UserOperation success rate dashboards, rejection taxonomy, bundler latency and uptime metrics) → SRE/Platform → Dashboards: none → live for testnet and pilot mainnet → 2025-02-28.
  4. Design and deploy an initial **paymaster policy engine** with configurable sponsorship rules and abuse detection → Product + Risk → Sponsored onboarding coverage: baseline 0% → ≥60% of new user txs in pilot → 2025-03-31.

- **【P2 – Optional】**
  5. Explore **AA-only flows** (e.g., smart-account-native features like batched operations and programmable recovery) for specific segments, to differentiate UX beyond gasless payments → Product Strategy → Number of AA-only features in roadmap: 0 → ≥2 documented → 2025-03-31.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Major bundler outage affecting AA flows | High | Medium | Elevated UserOperation failures across chains; provider status red | Multi-bundler integration with health checks and automatic failover; clear playbook to temporarily disable AA where needed | SRE Lead |
| Sponsorship abuse or unsustainable gas spend | High | Medium | Sudden spikes in sponsored tx volume or abnormal patterns by address/region | Rate limits, per-user and per-device caps, risk scoring, and real-time monitoring; rapid policy adjustment capability | Risk & Compliance Lead |
| Signature compatibility regressions across smart account versions | Medium | Medium | New smart account contract releases break validation of MPC signatures in some environments | Strict version pinning, contract registry, and CI test matrix covering all supported account types and chains | Protocol Engineering Lead |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A: Minimal AA** (EOA+MPC primary) | Low engineering effort; minimal infra risk; leverages existing pipelines | Limited UX improvement; weaker differentiation | Falling behind AA-based competitors; lost learning opportunity | When regulatory or risk posture is highly conservative | When market strongly rewards gasless/AA UX and competitors are moving fast |
| **B: Targeted AA rollout (recommended)** | Balances UX gains with controlled scope; allows learning and iteration; manageable infra complexity | Moderate engineering work; requires new observability and vendor management | Still exposed to AA infra maturity risk on selected flows | When team can pilot AA on specific products and iterate | When there is no capacity to build observability and risk controls |
| **C: AA-first for most flows** | Maximizes UX differentiation and innovation; unified model for future features | High engineering and organizational change cost; deep infra dependence | Outages or standard shifts could cause major disruption | When the organization is highly risk-tolerant and AA is core to strategy | When compliance requirements and institutional clients demand maximum stability |

[Source: ERC‑4337 Spec & Docs, 2023–2024; Stackup – MPC Wallets Guide, 2025; Alchemy – ERC‑4337 Wallet Guides, 2024].

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **Account Abstraction (AA)** | Design pattern that enables smart contract accounts with programmable validation and fee payment, decoupling user wallets from EOAs | N/A | [Source: ERC‑4337 Spec – Abstract & Motivation, 2023] |
| **ERC‑4337** | Ethereum standard that implements account abstraction using UserOperations, bundlers, and an EntryPoint contract without consensus changes | N/A | [Source: ERC‑4337 Spec, Buterin et al., Ethereum Foundation, 2023] |
| **UserOperation** | Pseudo-transaction object that encodes a user’s intended action for a smart account, submitted to an alternative mempool for bundlers to process | N/A | [Source: ERC‑4337 Spec – UserOperation Structure, 2023] |
| **EntryPoint** | Core smart contract that validates and executes packed UserOperations, coordinating account and paymaster verification and charging gas | N/A | [Source: ERC‑4337 Spec – EntryPoint Interface, 2023] |
| **Bundler** | Off-chain actor that collects UserOperations from the alt-mempool, simulates and validates them, and submits handleOps transactions to the EntryPoint | N/A | [Source: ERC‑4337 Spec – Bundler Behavior, 2023; Alchemy – How ERC‑4337 Smart Contract Wallets Work, 2024] |
| **Paymaster** | Smart contract that can sponsor gas fees or accept alternative tokens for payment by validating UserOperations and optionally running postOp logic | N/A | [Source: ERC‑4337 Spec – Extension: Paymasters, 2023; Alchemy – What Is a Paymaster?, 2024] |
| **MPC wallet** | Wallet where private key material is split across multiple parties or devices and signatures are produced via multi-party computation without reconstructing the key | N/A | [Source: Stackup – MPC Wallets: A Complete Technical Guide, 2025] |
| **Smart account / smart contract wallet** | Wallet where control logic is implemented in a smart contract rather than a single EOA key, enabling programmable rules, recovery, and batching | N/A | [Source: ERC‑4337 Docs – Smart Accounts, 2024; Crypto.com – Account Abstracting Wallets, 2023] |
| **Gasless transaction** | Transaction where gas is sponsored by a third party (e.g., paymaster) so the user does not directly pay network fees in ETH | N/A | [Source: ERC‑4337 Docs – What is ERC‑4337?, 2024; Alchemy – Paymaster Overview, 2024] |
| **EIP‑7702** | Proposal enabling EOAs to delegate control to smart contracts via authorization tuples, potentially affecting future AA design patterns | N/A | [Source: ERC‑4337 Spec – Support for EIP‑7702 Authorizations, 2023] |

---

## 12. References

### Tier 1 – Primary Specs and Documentation

1. **Buterin, V., et al.** (2023). *ERC‑4337: Account Abstraction Using Alt Mempool*. Ethereum Improvement Proposal. https://eips.ethereum.org/EIPS/eip-4337  
   **[Cited in**: Context Recap; Sections 1–3, 4, 5, 6, 7, 10, 11 **]**
2. **eth-infinitism.** (2024). *ERC‑4337 Documentation – Introduction & Smart Accounts*. https://docs.erc4337.io/index.html  
   **[Cited in**: Context Recap; Sections 1–3, 5, 6, 7, 10, 11 **]**

### Tier 2 – Industry Guides and Overviews

3. **Alchemy.** (2024). *How do ERC‑4337 smart contract wallets work?* Alchemy Docs & Guides. https://www.alchemy.com/overviews/how-do-smart-contract-wallets-work  
   **[Cited in**: Sections 1–3, 5, 6, 10, 11 **]**
4. **Alchemy.** (2024). *What is a Paymaster? (ERC‑4337)*. Alchemy Overviews. https://www.alchemy.com/overviews/what-is-a-paymaster  
   **[Cited in**: Sections 2, 3, 5, 6, 10, 11 **]**
5. **QuickNode.** (2024). *Account Abstraction and ERC‑4337 – Part 1*. QuickNode Guides. https://www.quicknode.com/guides/ethereum-development/wallets/account-abstraction-and-erc-4337  
   **[Cited in**: Sections 2, 3, 5, 10 **]**
6. **Crypto.com.** (2023). *A Guide to Ethereum’s ERC‑4337 Standard and Account Abstraction*. Crypto.com University. https://crypto.com/us/university/ethereum-erc-4337-standard-account-abstraction  
   **[Cited in**: Context Recap; Sections 3, 4, 5, 6, 10, 11 **]**
7. **Stackup.** (2025). *MPC Wallets: A Complete Technical Guide*. Stackup. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide  
   **[Cited in**: Context Recap; Sections 2–4, 5, 6, 7, 10, 11 **]**

### Tier 3 / Internal & Estimates

8. **Problem Statement – Account Abstraction (EIP‑4337) Integration with MPC Wallets.** (2025). Internal documentation summarizing impact scope, constraints, and stakeholders.  
   **[Cited in**: Context Recap; Sections 1–4, 7, 10 **]**
9. **Supplementary Analysis – GPT5.md.** (2025-11-28). *Blockchain MPC Wallet Problem Extraction*. Internal analysis document, lines 243–252.  
   **[Cited in**: Context Recap; Sections 1–4 **]**
10. **Estimates and assumptions.** Various.  
    Method: extrapolation from public AA and wallet adoption data, internal reliability targets, and comparable infra projects. Confidence: Medium. Validation: pilots and vendor data collection.  
    **[Used in**: Sections 1–2, 5–10 **]**
