# Legacy Infrastructure Integration Compatibility Challenges for MPC Wallets – Problem Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Enterprise Integration Team

---

## Context Recap

- **Problem title**: Legacy Infrastructure Integration Compatibility Challenges for MPC Wallets.
- **Current state**: Institutional MPC wallets promise stronger key security through distributed threshold signatures, but most enterprise and exchange stacks were built 2015–2020 around single-key HSM custody or on-chain multisig, with synchronous signing APIs and key-centric accounting and compliance models. Integration currently costs around 200K–1M USD per organization and takes 6–12 months, blocking mid-market adoption and slowing large deployments [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024, https://www.intelmarketresearch.com/mpc-wallet-development-2025-2032-75-4980].
- **Pain points**: 
  - API incompatibility between synchronous POST sign endpoints and multi-round MPC protocols with 2–15 second latency.  
  - HSMs and cold storage workflows assume a complete private key, not secret shares.  
  - Transaction pipelines cannot maintain 10K transactions per hour when signatures require multi-second interactive protocols.  
  - Accounting, audit, and regulatory frameworks are key-centric and struggle to reason about share-based custody and off-chain threshold coordination [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide] [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024, https://www.blockdaemon.com/blog/what-are-mpc-wallets-and-why-should-every-institution-have-one] [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023, https://learn.anchorage.com/Finding-End-to-End-Security-in-Crypto-Custody.pdf].
- **Goals**: Reduce per-customer integration cost from 200K–1M USD to under 50K USD minimum and ideally under 5K USD; cut deployment time from 6–12 months to under 1–3 months; preserve or approach legacy throughput of about 10K transactions per hour while benefiting from MPC security; reuse existing HSM and cold-storage investments; achieve regulatory clarity across major jurisdictions by 2026 [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024] [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024, https://www.fireblocks.com/report/digital-asset-custody-and-transaction-processing-leading-practices-using-fireblocks-mpc-solution] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024, https://s-horowitz.com/multi-party-computation-mpc-wallets-and-the-evolving-regulatory-landscape-in-the-united-states].
- **Hard constraints**: Cannot change layer 1 consensus rules or signature verification; MPC latency stems from cryptographic protocol rounds and cannot be eliminated, only hidden or amortized; many enterprises cannot discard 2M–5M USD of sunk HSM and cold-storage investment; regulators typically need 6–12 months to evaluate new custody models; backward compatibility with existing MPC deployments and APIs is required [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024, https://whitepaper.secubit.io/hsm-workflows/mpc-threshold-signature-protocol.html] [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025] [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024, https://www.mpcalliance.org/blog/an-introduction-to-secure-multiparty-computation-for-digital-asset-custody-wallets].
- **Key facts**: Market analyses estimate more than 100 institutional custody providers, 50 major exchanges, and around 1000 enterprises managing digital assets with roughly 500B USD under custody, yet integration cost and complexity limit MPC adoption to a small fraction of this market today [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024] [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

- **Security vs compatibility**: Enterprises want MPCs no single point of key compromise and resilient threshold signing, but their infrastructure (HSMs, cold wallets, accounting, monitoring) assumes monolithic keys and single-step signing. The contradiction is between a share-based, off-chain threshold model and key-centric, on-chain or HSM-centric infrastructure [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025] [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024].
- **Latency vs throughput**: MPC introduces 4–9 protocol rounds and 2–15 second signing latency, while existing transaction pipelines and exchanges are engineered for around 100 millisecond signing and batching thousands of transactions per hour. Sequential MPC signing can reduce throughput from about 10K transactions per hour to as low as roughly 240 per hour without architectural changes [Estimate: Derived from 2–15 second per-signature latency, worst case 3600 seconds per hour divided by 15 seconds equals 240 transactions per hour, Medium confidence] [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
- **Vendor lock-in vs interoperability**: Each MPC provider historically deployed proprietary middleware and APIs, creating tight coupling and high professional-services revenue per integration, but this conflicts with customers demand for standard APIs, portable risk models, and multi-vendor strategies [Source: deBridge Chooses Fordefi MPC Wallet API to Scale Cross-Chain Liquidity, Fordefi, 2024, https://fordefi.com/customer-stories/debridge-chooses-fordefi-mpc-wallet-api-to-scale-cross-chain-liquidity] [Source: Building Full DeFi Connectivity for Market Makers and Asset Managers With an Institutional MPC Wallet, Fordefi, 2023, https://medium.com/fordefi/building-full-defi-connectivity-for-market-makers-and-asset-managers-with-an-institutional-mpc-2702716cff69].
- **Regulatory certainty vs novel cryptography**: Regulators and auditors are accustomed to custody models where a key, signing device, and control processes can be inspected and attested; MPCs no single complete key and its distributed control are conceptually harder to audit, so institutions hesitate to deploy at scale until frameworks clearly define responsibility, segregation of duties, and recovery [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

### 1.2 Goals and conditions

- **Cost and time targets**: Reduce integration cost per enterprise or exchange from 200K–1M USD to less than 50K USD minimum and ideally below 20K USD, and compress deployment from 6–12 months to less than 1–3 months through standardized APIs, reference middleware, and ready-made connectors [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
- **Performance and reliability**: Achieve at least 5000 transactions per hour for MPC-backed signing without compromising security, through parallel sessions, batching, and pre-signing; keep apparent API latency within under 100 milliseconds for common operations and under about 3 seconds for uncached fresh signatures [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024] [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
- **Compatibility and reuse**: Allow enterprises to reuse existing HSMs as share storage or signing participants instead of discarding multimillion-dollar hardware, and maintain cold storage and air-gapped policies for high-security assets [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024] [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024].
- **Compliance and governance**: Produce regulatory and audit frameworks that explain how distributed shares map to custody obligations, sign-off workflows, and disaster recovery so that regulators in major jurisdictions (for example US, EU, UK) can approve MPC-based custody operations [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

### 1.3 Extensibility and reframing

- **API-centric reframing**: Instead of treating MPC purely as a cryptographic change, frame the problem as designing a drop-in signing API that emulates existing sign endpoints while hiding asynchronous multi-round complexity behind stateful sessions, caching, and pre-signing. This makes middleware architecture and developer experience the primary design surface [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025] [Source: deBridge Chooses Fordefi MPC Wallet API to Scale Cross-Chain Liquidity, Fordefi, 2024].
- **Custody-model reframing**: Reframe from key storage to control policy and transaction authorization. Under this view, MPC is a way to implement robust multi-party policy enforcement independent of where keys or shares live, making compatibility discussions about policy mapping rather than pure cryptographic format [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024] [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024].
- **Market-structure reframing**: The problem can also be seen as building an industry utility layer for MPC integration (standards, connectors, sample architectures) so that integration costs become shared infrastructure rather than bespoke projects, similar to how payment gateways or custody protocols evolved [Estimate: Analogy based on historical evolution of payment and custody standards, Medium confidence] [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Legacy components**: Single-key hot wallets backed by HSMs, on-chain multisig smart contracts, cold storage and air-gapped signing devices, transaction batching and queuing layers, monitoring and alerting systems, accounting ledgers, and compliance reporting pipelines [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025] [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024].
- **MPC components**: Distributed key generation, key share storage, multi-party signing coordinators, pre-signing caches, policy engines for threshold and role-based approvals, and health monitoring across multiple parties and sites [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024] [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024].
- **Interfaces and contracts**: REST or gRPC signing APIs, PKCS11 or similar HSM interfaces, transaction pipelines that expect synchronous signing results, batch processing jobs, and audit events pushed to logging or SIEM systems [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025] [Source: Building Full DeFi Connectivity for Market Makers and Asset Managers With an Institutional MPC Wallet, Fordefi, 2023].

### 2.2 Balance and degree

- **Security vs performance**: Higher thresholds and more parties per signing session increase resilience against key compromise but also add protocol rounds and communication overhead, which can degrade throughput unless heavily parallelized [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024] [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
- **Reuse vs redesign**: Maximizing reuse of HSMs and cold-storage devices lowers capital expenditure and change-management risk but often forces complex compatibility layers that may be fragile or performance-limiting. Aggressive redesign improves long-term fit at the cost of higher up-front migration risk [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024] [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023].
- **Standardization vs differentiation**: Common APIs and reference architectures reduce integration cost for everyone but may limit individual vendors ability to differentiate on UX or advanced features. The right degree of standardization should focus on lowest common denominator primitives (for example, sign, key refresh, policy introspection) while letting vendors innovate above that layer [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024] [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].

### 2.3 Causal chains

- **Throughput degradation chain**: 
  1. Introduce MPC with interactive 2–15 second signing latency.  
  2. Keep legacy sequential sign pipeline expecting under 100 millisecond responses.  
  3. Queue depth increases, batches stall, and hourly throughput falls from around 10K to a few hundred transactions.  
  4. Operations teams see missed settlement SLAs and degrade trust in MPC-based custody [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
- **Compliance uncertainty chain**: 
  1. Custody teams propose MPC wallet migration to reduce single-key risk.  
  2. Auditors ask which device or role owns the key; the answer involves distributed shares and off-chain coordination.  
  3. Lack of explicit regulatory guidance forces case-by-case legal opinions, increasing project risk and timeline.  
  4. Decision-makers delay or scale down MPC adoption, perpetuating legacy operational and security risk [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and relationships

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | MPC wallet providers and HSM vendors | Sell secure, high-margin custody platforms and hardware; scale to many customers via standard APIs and connectors | Limited engineering capacity, long hardware firmware cycles, need to maintain competitive advantage | May resist deep standardization that commoditizes differentiation [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024] [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024] |
| Downstream | Exchanges, custody providers, enterprises | Achieve strong security and regulatory compliance with predictable integration cost, latency, and throughput | Cannot accept downtime for core trading or custody; heavy change-management constraints; must satisfy regulators | Want optionality across MPC vendors while minimizing re-integration work [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024] [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024] |
| Sidelineexternal | Regulators, auditors, accounting vendors, DeFi protocols | Ensure systemic stability, investor protection, and reliable accounting of digital assets | Typically conservative toward novel cryptography, rely on clear frameworks and precedents | Can block or delay MPC deployments if models are not well explained or tested [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024] |

### 3.2 Environment

- **Regulatory landscape**: Jurisdictions like the United States, European Union, and United Kingdom are actively clarifying crypto custody expectations but rarely mention MPC explicitly, forcing interpretation and negotiation for each deployment [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].
- **Technology evolution**: Protocols for threshold ECDSA and threshold EdDSA are maturing, and vendors are optimizing multi-party signing and key refresh workflows, but coordination with existing standards such as PKCS11 and enterprise key management remains incomplete [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024] [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].
- **Market pressure**: Institutional clients expect institutional-grade security, fast onboarding, and deep DeFi and exchange connectivity, pushing custodians to adopt MPC but penalizing long integration projects and degraded performance [Source: deBridge Chooses Fordefi MPC Wallet API to Scale Cross-Chain Liquidity, Fordefi, 2024] [Source: Building Full DeFi Connectivity for Market Makers and Asset Managers With an Institutional MPC Wallet, Fordefi, 2023].

### 3.3 Responsibility and room for maneuver

- **MPC vendors**: Take primary responsibility for designing integration-friendly APIs, middleware, and reference architectures, and for coordinating with HSM vendors and regulators. They must leave room for enterprises to tailor policies and network topologies [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024] [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
- **Enterprises and exchanges**: Own decisions around which systems to refactor vs wrap with adapters, and must invest in integration engineers who understand both cryptography and production operations. They should avoid over-customization that undermines future upgrades [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
- **Regulators and auditors**: Define minimum acceptable patterns and documentation; they should avoid endorsing specific vendors but can clarify principles for segregation of duties, recovery, and incident response under MPC models [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

- **2015–2020 single-key and multisig era**: Custody and exchange stacks standardized on HSM-backed single keys and on-chain multisig contracts, with well-understood security and regulatory models [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025] [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024].
- **2018–2020 first MPC deployments**: First-generation MPC custodians built bespoke integrations per large institutional client, relying heavily on custom middleware and professional services, making deployments expensive and slow [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024] [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].
- **2020–2024 middleware and DeFi connectivity**: Vendors like Fordefi, Fireblocks, and others built rich APIs and DeFi connectivity layers on top of MPC engines, but each with proprietary contracts and limited standardization [Source: deBridge Chooses Fordefi MPC Wallet API to Scale Cross-Chain Liquidity, Fordefi, 2024] [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
- **Early standardization attempts**: Industry groups proposed MPC standards, but lack of strong incentives and fear of commoditization limited adoption; HSM vendor support for threshold schemes remained experimental and slow [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024] [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024].

### 4.2 Background vs direct causes

- **Background causes**: 
  - Legacy infrastructure designed before MPC was practical for production custody.  
  - Regulatory frameworks written for single-key custody and on-chain multisig, not distributed shares.  
  - HSM vendors optimized for storing and using full keys, not shares or threshold protocols [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024] [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023].
- **Direct causes**: 
  - First MPC deployments prioritized shipping secure systems over clean integration patterns.  
  - Each vendor implemented unique APIs, key management abstractions, and signing flows without a common reference.  
  - Enterprises integrated via custom middleware that tightly coupled to legacy systems, increasing technical debt [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024] [Source: Building Full DeFi Connectivity for Market Makers and Asset Managers With an Institutional MPC Wallet, Fordefi, 2023].

### 4.3 Root issues

- **Lack of shared architecture language**: MPC experts, HSM vendors, and enterprise architects do not yet share a common vocabulary around threshold custody patterns, leading to misaligned expectations and designs [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].
- **Incentive misalignment**: Vendors gain short-term revenue from bespoke integrations but the ecosystem needs standardized, reusable patterns to reduce barriers for mid-market customers [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
- **Conservative regulatory posture**: Without widely accepted reference architectures and threat models, regulators have limited incentives to endorse MPC-specific patterns, reinforcing caution among institutions [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory if unchanged

- **High integration costs persist**: If each enterprise continues to build custom middleware for MPC, integration costs likely remain in the 200K–1M USD range, limiting adoption mainly to large institutions [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
- **Operational friction**: Without API and pipeline adaptations, MPC-induced latency will keep degrading throughput and operational predictability, causing some organizations to restrict MPC to low-volume or cold-storage use cases [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
- **Fragmented standards**: Multiple competing quasi-standards may emerge (per vendor or per consortium) without achieving the network effects needed to materially reduce integration costs [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].

### 5.2 Early signals

- **Interest from HSM vendors**: Vendors like Thales and others are exploring MPC share storage and threshold operations, indicating recognition that hardware security modules must evolve to remain relevant [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024].
- **DeFi and cross-chain connectivity**: Partnerships such as MPC wallet APIs chosen for cross-chain liquidity providers show that well-designed APIs can become de facto standards for specific ecosystems [Source: deBridge Chooses Fordefi MPC Wallet API to Scale Cross-Chain Liquidity, Fordefi, 2024].
- **Regulatory attention**: Whitepapers and legal analyses dedicated to MPC custody suggest that regulators and legal practitioners are beginning to internalize these models, creating a foundation for more formal guidance [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

### 5.3 Scenarios over 6–24 months

- **Optimistic scenario**: An industry consortium of MPC vendors, HSM providers, custodians, and exchanges defines a minimal common signing and policy API, publishes reference middleware and integration blueprints, and earns early regulatory acknowledgement, cutting integration cost by over 70 percent and reducing timelines to 1–3 months for typical deployments [Estimate: Based on observed effects of standard APIs in payments and cloud services, Medium confidence] [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
- **Baseline scenario**: A few quasi-standards emerge around major vendors, with some interoperability but continued need for custom adapters per institution. Integration costs fall modestly (for example 30–40 percent), and mid-market adoption improves but remains below full potential [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024] [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
- **Pessimistic scenario**: No credible standardization emerges; regulators remain vague; a security incident in an MPC-based system triggers heightened scrutiny, causing institutions to slow or reverse deployments and reinforcing reliance on legacy models despite their known weaknesses [Estimate: Risk scenario constructed from historical reactions to security incidents in financial infrastructure, Medium confidence] [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Cryptography and security expertise**: Leading MPC vendors and some large custodians have deep expertise in threshold cryptography, secure protocol implementation, and formal security analysis [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025] [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].
- **Operational maturity**: Exchanges and custodians already operate 24x7, high-throughput infrastructures with strong incident response and change-management practices, which can absorb complex migrations if well planned [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024] [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023].
- **Ecosystem collaboration**: Existing industry groups and alliances around MPC and digital asset custody provide forums for multi-stakeholder coordination and knowledge sharing [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].

### 6.2 Capability gaps

- **Integration engineering**: Many enterprises lack engineers who understand both production crypto custody and complex distributed protocols, increasing the risk of fragile middleware and misconfigurations [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
- **Architecture communication**: MPC, HSM, and compliance teams often use different conceptual models and vocabulary, making it hard to co-design robust end-to-end architectures [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].
- **Regulatory translation**: Few practitioners can translate technical guarantees of MPC into language and artifacts (for example control descriptions, audit procedures) that regulators and auditors can confidently approve [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

### 6.3 Buildable capabilities (1–6 months)

- **Reference integration squads**: Create cross-functional teams (cryptography, infrastructure, compliance, product) focused on designing and maintaining standard integration patterns and middleware components that can be reused across clients [Estimate: Based on typical cross-functional platform teams in financial institutions, Medium confidence].
- **Documentation and blueprints**: Develop detailed reference architectures for common deployment archetypes (for example high-frequency exchange, institutional cold storage, mid-market enterprise treasury) with diagrams, failure modes, and configuration guidance [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024] [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
- **Regulatory playbooks**: Codify templates for MPC custody descriptions, risk assessments, and audit evidence packages that can be adapted per jurisdiction, shortening legal review cycles [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Legacy single-key and multisig infrastructures, high integration cost and complexity for MPC, regulatory uncertainty.
- **Core problem**: Making MPC a drop-in compatible, cost-effective, and compliant replacement for existing signing and custody stacks.
- **Analysis dimensions**: Internal architecture tradeoffs, stakeholder incentives, historical evolution, future adoption scenarios, capability gaps.
- **Options**: Proprietary vendor-specific integrations, partial standardization around de facto APIs, or formal industry standards with reference implementations.
- **Risks**: Operational regressions, lock-in, regulatory delays, security misconfigurations.
- **Recommendations**: Establish minimal common API and data models, co-design HSM and MPC integrations, publish reference architectures and regulatory playbooks.

### 7.2 Key judgments needing validation

1. **Standard APIs can reduce integration cost by more than half** for typical institutions by 2026 if backed by credible reference implementations and vendor commitments [Estimate: Derived from analogies with payment and cloud API standardization, Medium confidence] [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
2. **Throughput targets of roughly 5000 transactions per hour are sufficient** for most institutional MPC use cases, with higher-throughput scenarios handled via pre-signing and batching [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
3. **Regulators will accept MPC custody models** once controls are mapped clearly to familiar concepts (for example segregation of duties, dual control, incident response) and demonstrated via pilots and audits [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

### 7.3 Alternative paths

- **Path A – Vendor-centric evolution**: Let a few large MPC vendors define de facto API patterns and invest heavily in their ecosystems; accept some lock-in but gain speed.
- **Path B – Consortium standardization**: Formally define minimal APIs and reference architectures under a neutral body; slower to coordinate but better for broad adoption and interoperability.
- **Path C – Incremental wrappers around legacy systems**: Focus on pragmatic adapters for existing HSM and cold-storage setups per institution, accepting continued bespoke work but minimizing disruption.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Vendor optimism bias**: Analyses may overestimate willingness of competitors to cooperate on standards and underestimate commercial incentives for lock-in [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
- **Technology-solution bias**: There is a risk of focusing on elegant cryptographic integration patterns while underweighting organizational and regulatory constraints [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].
- **Risk aversion bias**: Institutions and regulators may over-index on worst-case security incidents, slowing adoption even when overall risk decreases versus legacy models [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023].

### 8.2 Required intelligence

- **Empirical integration metrics**: Data on actual integration timelines, engineering effort, incident rates, and performance before and after MPC deployments across a representative set of institutions [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
- **Performance benchmarks**: Standardized benchmarks for MPC signing latency and throughput across different architectures (with and without pre-signing and batching) [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
- **Regulatory feedback**: Explicit written feedback from regulators and auditors on proposed MPC architectures and controls, including conditions for approval and residual concerns [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024] [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023].

### 8.3 Validation plan

- **Pilot integrations**: Run 3–5 pilot projects across different archetypes (for example exchange, global custodian, mid-market enterprise) using a shared reference API and middleware; measure integration cost, time, and operational metrics against baselines [Estimate: Standard approach for validating platform changes in financial infrastructure, Medium confidence].
- **Benchmark suite**: Develop an open benchmarking harness that can run representative signing workloads (single and batch) against MPC engines and legacy HSM stacks, publishing results to build trust and guide optimization [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024] [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
- **Regulatory sandbox**: Work with regulators to establish sandbox environments where MPC custody models can be tested under supervision, with clear documentation of findings and conditions for scaling to production [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- **Throughput and latency targets** may be adjusted once benchmark data across multiple vendors is available.
- **Standard API scope** may expand or shrink depending on adoption; some functions could remain vendor-specific if standardization benefit is low.
- **Regulatory assumptions** will need updating as new guidance, enforcement actions, or precedent-setting approvals appear [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

### 9.2 Incremental approach

- Start with **low-risk, low-volume flows** (for example internal treasury, testnets, or limited-asset subsets) to validate MPC integrations and gradually expand to high-volume trading and retail flows.
- Use **feature flags and phased rollouts** so that legacy signing paths remain available as fallback until MPC performance and stability meet targets [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
- Iterate on **reference architectures and documentation** after each pilot, capturing lessons and anti-patterns to improve future integrations [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].

### 9.3 Good-enough criteria

- **Integration cost** consistently under 50K USD and 3 months for typical mid-market customers.
- **Performance** at or above 5000 transactions per hour for relevant use cases with acceptable latency for end users.
- **Regulatory acceptance** in at least three major jurisdictions with no material qualifications on MPC-based custody.
- **Operational stability** comparable to or better than legacy systems over a 6–12 month observation period [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024] [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023].

---

## 10. Summary and Action Recommendations (Aspect 10)

### 10.1 Core insights

1. The main blocker for MPC wallet adoption in enterprises is not raw cryptography but integration friction with legacy HSM-centric, key-centric, and latency-sensitive infrastructures; solving this requires standardized APIs, reference middleware, and regulatory translation, not just better protocols [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025] [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
2. Without coordinated effort, integration costs will stay in the hundreds of thousands of dollars per customer and limit MPC to large institutions, leaving mid-market enterprises on weaker custody models [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
3. Carefully designed asynchronous signing APIs, batching, and pre-signing can restore much of the lost throughput and user-perceived latency without changing blockchain consensus, but they require changes in transaction pipelines and monitoring [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
4. Regulatory clarity is both a constraint and an opportunity: early movers who help shape MPC custody frameworks can gain trust and influence, while laggards may face higher barriers later [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

### 10.2 Near-term action list (0–3 months)

**P0 – Critical**

1. **Define minimal MPC signing and policy API** → Industry working group of MPC vendors and custodians → Metric: initial spec covering at least sign, key refresh, policy introspection adopted by at least 3 vendors → Date: within 3 months [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].
2. **Design reference middleware for asynchronous signing** that wraps legacy sign endpoints while handling MPC session management, pre-signing, and retries → Joint architecture team of MPC vendors and 2–3 pilot institutions → Metric: end-to-end throughput of at least 5000 transactions per hour with under 3 second p95 latency for uncached signatures in pilot → Date: within 3–6 months [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].

**P1 – Important**

3. **Establish HSM–MPC integration patterns** (for example storing one share in HSM, using HSM as signing participant) → HSM and MPC vendor partnership teams → Metric: documented patterns and prototypes for at least 3 major HSM vendors → Date: within 6–12 months [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024] [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024].
4. **Create regulatory and audit playbooks** for MPC custody describing control frameworks, incident handling, and recovery models → Legal, risk, and security teams at leading custodians → Metric: playbooks accepted by auditors in at least 3 pilot institutions → Date: within 6–12 months [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024].

**P2 – Optional but valuable**

5. **Develop open benchmark suite and public results** for MPC vs legacy signing throughput and latency across common workloads → Community-led technical task force → Metric: benchmarks adopted by at least 5 vendors and cited in at least 2 industry reports → Date: within 12–18 months [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024] [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
6. **Standardize key refresh and address stability patterns** so enterprises can rotate keys and shares without disrupting account addressing or on-chain references → Working group of protocol and custody engineers → Metric: documented patterns and implementations aligned with key-refresh best practices → Date: within 12 months [Source: Refresh Keys With Static Account Addresses, Blockdaemon, 2024, https://www.blockdaemon.com/blog/key-refresh-with-static-account-addressess].

### 10.3 Key risks and mitigations

| Risk | Impact | Probability | Trigger | Mitigation | Owner |
|------|--------|-------------|---------|-----------|-------|
| Standardization stalls due to vendor competition | High | Medium | Working groups fail to converge on API spec | Narrow scope to minimal common primitives; use neutral governance; highlight mutual cost savings | MPC vendors and custodians [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024] |
| Performance targets not met in production | High | Medium | Benchmarks show persistent throughput or latency gaps | Optimize batching, pre-signing, parallelization; adjust thresholds; refine hardware deployment patterns | MPC engineering teams [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024] |
| Regulators reject or delay MPC custody models | High | Medium | Negative feedback or lack of guidance | Engage early via sandboxes; provide clear documentation and third-party assessments; start with low-risk assets | Legal and compliance teams [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023] [Source: Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States, S Horowitz, 2024] |

---

## 11. Glossary

- **MPC (Multi-Party Computation)**: A cryptographic technique that allows multiple parties to jointly compute a function over their inputs while keeping those inputs private; in wallets it is used to compute signatures without reconstructing a full private key in any single location [Source: An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets, MPC Alliance, 2024].
- **MPC wallet**: A custody architecture where private key material is split into shares and managed by multiple parties or devices, enabling threshold signatures and reducing single points of failure [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024].
- **Threshold signature**: A digital signature produced when at least k out of n parties participate in a protocol, without reconstructing the full private key, typically used for ECDSA or EdDSA in blockchain systems [Source: MPC Threshold Signature Protocol With HSM Workflows, Secubit, 2024].
- **Share-based architecture**: A key management approach where no complete key exists; instead, secret shares are stored across devices or services, and cryptographic protocols use these shares directly [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
- **HSM (Hardware Security Module)**: A tamper-resistant hardware device that stores cryptographic keys and executes signing operations, widely used in institutional custody and key management [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024].
- **Cold storage**: An offline storage method where signing keys or key shares reside in air-gapped devices, minimizing exposure to remote attacks but complicating multi-round coordination [Source: Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023].
- **Hot wallet**: An online wallet connected to networks for frequent transactions, prioritizing availability and latency while requiring strong operational controls to manage risk [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
- **Warm wallet**: An intermediate architecture between hot and cold storage, often online with additional access controls and monitoring to balance security and convenience [Source: What are MPC Wallets and Why Should Every Institution Have One, Blockdaemon, 2024].
- **Pre-signing**: The practice of generating signatures or signature components in advance, caching them so that final transaction signing appears fast even if underlying MPC protocols are slower [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution, Fireblocks, 2024].
- **Drop-in replacement**: A component or system that can substitute an existing one without requiring surrounding systems to change, here referring to MPC signing services that present APIs identical or very similar to legacy sign endpoints [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
- **On-chain multisig**: A wallet or smart-contract model on the blockchain that requires multiple independent signatures validated by the chain itself, distinct from MPC where the chain typically sees a single aggregated signature [Source: MPC Wallets a Complete Technical Guide, Stackup, 2025].
- **Key refresh with static address**: A key management pattern where cryptographic keys or shares are rotated while keeping blockchain addresses stable, often using protocol-specific constructions or derivation schemes [Source: Refresh Keys With Static Account Addresses, Blockdaemon, 2024].

---

## 12. References

### Tier 1 and Tier 2 External Sources

1. Intel Market Research. 2024. MPC Wallet Development Market Growth 2025–2032. Intel Market Research. https://www.intelmarketresearch.com/mpc-wallet-development-2025-2032-75-4980  
   - Cited in: Context Recap, 1.2, 1.3, 4.1, 4.2, 5.1, 5.3, 6.2, 7.2, 7.3, 8.2, 9.2, 9.3, 10.1, 10.3.
2. Stackup. 2025. MPC Wallets a Complete Technical Guide. Stackup Resources. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide  
   - Cited in: Context Recap, 1.1, 1.2, 1.3, 2.1, 2.2, 3.2, 6.1, 8.3, 10.1, 10.2, 11.
3. Fireblocks. 2024. Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks MPC Solution. Fireblocks Report. https://www.fireblocks.com/report/digital-asset-custody-and-transaction-processing-leading-practices-using-fireblocks-mpc-solution  
   - Cited in: Context Recap, 1.2, 2.1, 2.2, 3.1, 4.1, 5.1, 5.3, 6.3, 7.2, 8.2, 8.3, 9.2, 10.1, 10.2, 10.3.
4. Fordefi. 2024. deBridge Chooses Fordefi MPC Wallet API to Scale Cross-Chain Liquidity. Customer Story. https://fordefi.com/customer-stories/debridge-chooses-fordefi-mpc-wallet-api-to-scale-cross-chain-liquidity  
   - Cited in: 1.1, 1.3, 3.2, 4.1, 5.2.
5. Fordefi. 2023. Building Full DeFi Connectivity for Market Makers and Asset Managers With an Institutional MPC Wallet. Medium Article. https://medium.com/fordefi/building-full-defi-connectivity-for-market-makers-and-asset-managers-with-an-institutional-mpc-2702716cff69  
   - Cited in: 1.1, 2.1, 4.2, 5.2.
6. Blockdaemon. 2024. What are MPC Wallets and Why Should Every Institution Have One. Blockdaemon Blog. https://www.blockdaemon.com/blog/what-are-mpc-wallets-and-why-should-every-institution-have-one  
   - Cited in: Context Recap, 1.1, 1.2, 2.1, 2.2, 4.1, 6.1, 6.2, 10.2, 11.
7. Secubit. 2024. MPC Threshold Signature Protocol With HSM Workflows. Secubit Whitepaper. https://whitepaper.secubit.io/hsm-workflows/mpc-threshold-signature-protocol.html  
   - Cited in: Context Recap, 2.1, 2.2, 3.2, 4.1, 5.2, 8.3, 10.2, 10.3, 11.
8. Anchorage Digital. 2023. Finding End-to-End Security in Crypto Custody. Anchorage Digital Whitepaper. https://learn.anchorage.com/Finding-End-to-End-Security-in-Crypto-Custody.pdf  
   - Cited in: Context Recap, 1.1, 1.2, 2.2, 3.2, 3.3, 4.2, 4.3, 5.2, 6.1, 6.2, 6.3, 8.1, 8.2, 8.3, 9.3, 10.1, 10.2, 10.3, 11.
9. S Horowitz. 2024. Multi-Party Computation Wallets and the Evolving Regulatory Landscape in the United States. S Horowitz and Co. https://s-horowitz.com/multi-party-computation-mpc-wallets-and-the-evolving-regulatory-landscape-in-the-united-states  
   - Cited in: Context Recap, 1.2, 1.3, 3.2, 3.3, 4.3, 5.2, 5.3, 6.2, 6.3, 7.2, 8.2, 8.3, 9.1, 10.1, 10.2, 10.3, 11.
10. MPC Alliance. 2024. An Introduction to Secure Multiparty Computation For Digital Asset Custody Wallets. MPC Alliance Blog. https://www.mpcalliance.org/blog/an-introduction-to-secure-multiparty-computation-for-digital-asset-custody-wallets  
   - Cited in: Context Recap, 1.1, 1.3, 2.2, 3.2, 4.1, 4.3, 5.1, 6.1, 6.2, 7.2, 8.1, 11.
11. Blockdaemon. 2024. Refresh Keys With Static Account Addresses. Blockdaemon Blog. https://www.blockdaemon.com/blog/key-refresh-with-static-account-addressess  
   - Cited in: 10.2, 11.

### Estimates and assumptions (not formal references)

- Scenario projections, integration cost-reduction estimates, and adoption curves marked as Estimate in the main text are based on analogies with prior standardization efforts in payments and cloud APIs and should be validated with empirical data and controlled pilots.
