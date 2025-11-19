# MPC Wallet Engineer Interview Guide (LinerGDR)

## Executive Summary

**Domain**: Career (Cross-Domain Interview Front Page)  
**Role**: Blockchain Security Cryptographic Development Engineer + Blockchain Architect - Multi-chain MPC Integration  
**Time Budget**: 75 minutes  
**Coverage**: 6 Q&As (1 per essential domain)  
**Success Criteria**: Achieve ≥80% hiring consensus with clear strengths/risks identified per domain

## Glossary

**Core Cryptographic Terms**:
- **MPC**: Multi-Party Computation - distributed key management protocol
- **TSS**: Threshold Signature Scheme
- **ECDSA**: Elliptic Curve Digital Signature Algorithm
- **EdDSA**: Edwards-curve Digital Signature Algorithm
- **GG18/GG20**: Gennaro & Goldfeder threshold ECDSA protocols (2018/2020)
- **FROST**: Flexible Round-Optimized Schnorr Threshold signatures
- **CGGMP21**: Canetti-Gennaro-Goldfeder-Makriyannis-Peled threshold ECDSA (2021)
- **DKG**: Distributed Key Generation

**Security & Architecture**:
- **AA**: Account Abstraction
- **ADR**: Architecture Decision Record
- **TEE**: Trusted Execution Environment
- **STRIDE**: Threat modeling (Spoofing/Tampering/Repudiation/Information Disclosure/Denial of Service/Elevation of Privilege)
- **CVSS**: Common Vulnerability Scoring System
- **NIST CSF**: NIST Cybersecurity Framework (Identify/Protect/Detect/Respond/Recover)
- **FIDO2**: Fast Identity Online 2 (passwordless authentication standard)

**Engineering Frameworks**:
- **DORA**: DevOps Research and Assessment
- **SOLID**: Software design principles (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)
- **RACI**: Responsibility Assignment Matrix (Responsible/Accountable/Consulted/Informed)
- **OKR**: Objectives and Key Results

**Prioritization Methods**:
- **WSJF**: Weighted Shortest Job First
- **MoSCoW**: Must-have/Should-have/Could-have/Won't-have (prioritization)

**Blockchain Standards**:
- **EVM**: Ethereum Virtual Machine
- **L2**: Layer 2 scaling solutions
- **DeFi**: Decentralized Finance

## Table of Contents

- [Executive Summary](#executive-summary)
- [Glossary](#glossary)
- [Key Signals](#key-signals)
- [Dashboard](#dashboard)
- [Q1: Designing a Secure and Extensible Multi-Chain MPC Wallet Core](#q1-designing-a-secure-and-extensible-multi-chain-mpc-wallet-core)
- [Q2: Optimizing Transaction Signing Latency and Reliability for MPC Wallets](#q2-optimizing-transaction-signing-latency-and-reliability-for-mpc-wallets)
- [Q3: Prioritizing MPC Wallet Infrastructure Features with Resource Constraints](#q3-prioritizing-mpc-wallet-infrastructure-features-with-resource-constraints)
- [Q4: Responding to a Novel Attack Vector in MPC Signature Protocols](#q4-responding-to-a-novel-attack-vector-in-mpc-signature-protocols)
- [Q5: Leading Cross-Functional Effort for Device Verification and MFA Productization](#q5-leading-cross-functional-effort-for-device-verification-and-mfa-productization)
- [Q6: Strategic Evolution of Multi-Chain MPC Wallet for Emerging Standards](#q6-strategic-evolution-of-multi-chain-mpc-wallet-for-emerging-standards)
- [Sources](#sources)

## Key Signals
- Structural & design judgment for secure, modular, multi-chain MPC wallets
- Performance/quality trade-offs in cryptographic signing for diverse environments
- Value & prioritization for security features like AA and social recovery
- Threat modeling, incident response, and regulatory compliance in advanced crypto systems
- Cross-functional collaboration and leadership in productizing security
- Strategic thinking for evolving blockchain standards and ecosystem integration

## Dashboard
| # | EssentialDomainTag | Domain | Difficulty | Criticality | Target Signal | EstimatedTime |
|---|--------------------|--------|------------|-------------|---------------|---------------|
| 1 | TechArch | Technical Architecture & Design | A | Blocks, Risk | System & API design judgment | ~10–15 min |
| 2 | PerfQual | Performance & Quality Engineering | I | Quantified, Risk | Performance/quality trade-offs | ~10–15 min |
| 3 | ProdBiz | Product & Business Value | I | Roles, Action | Value & prioritization judgment | ~10–15 min |
| 4 | SecReg | Security & Regulation | A | Blocks, Risk, Action | Threat, risk, compliance mindset | ~10–15 min |
| 5 | OrgLead | Organization & Leadership | I | Roles, Action | Collaboration/leadership style | ~10–15 min |
| 6 | RoadmapEco | Roadmap & Ecosystem Strategy | A | Action, Quantified, Risk | Long-term thinking & evolution | ~10–15 min |

---

### Q1: Designing a Secure and Extensible Multi-Chain MPC Wallet Core

**Domain**: Technical Architecture & Design | **CareerStage**: Architect | **RoleFocus**: IC |
**Difficulty**: A | **Criticality**: Blocks, Risk | **Stakeholders**: Backend Engineers, Security Engineers, Protocol Developers | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:
You are tasked with designing the core module for a new multi-chain MPC wallet. This module must support various threshold signature schemes (e.g., GG18, GG20, FROST, Threshold ECDSA/EdDSA) and ensure compatibility with major public chains like Ethereum, BTC, and Solana, including their respective transaction structures. The design needs to be highly modular, easily upgradable, and minimize a single point of failure. How would you architect this core module, considering the interplay between cryptographic complexity, multi-chain specific adaptations, and the need for maintainability and security? What architectural patterns and principles would you prioritize?

**Answer Key (~150–250 words)**:
**Key Insight**: A strong candidate will propose a layered, modular architecture that clearly separates cryptographic logic from blockchain-specific integration and transaction serialization. This allows for pluggability of different MPC protocols and easier adaptation to new chains without refactoring the entire core. They would emphasize abstraction layers to manage complexity and maintain strong security boundaries, ensuring that cryptographic operations are isolated and robust.
**Frameworks/Tools**: The candidate should reference architectural patterns like `Clean Architecture` or `Ports and Adapters (Hexagonal Architecture)` to promote modularity and testability. `SOLID principles` (especially Interface Segregation and Dependency Inversion) are crucial for pluggable protocol implementations. They might mention `ADRs (Architectural Decision Records)` for documenting critical design choices and their trade-offs.
**Trade-offs & Metrics**: Discussion should include trade-offs between abstraction complexity (for flexibility) and performance overhead. Chain-specific adapters add maintenance complexity but are necessary for compatibility. Key metrics would include `code cohesion`, `coupling`, `test coverage` for cryptographic primitives, and `auditing frequency` for security-critical components.
**Stakeholder Handling**: They would engage backend engineers for seamless integration and API design, security engineers for thorough threat modeling of each protocol, and protocol developers for understanding specific cryptographic nuances and future evolutions. Clear APIs and SDKs are vital for cross-team collaboration.
**Signals**:
- **Strong**: Provides a clear modular design blueprint with specific architectural patterns, acknowledges protocol-specific nuances (e.g., ECDSA vs EdDSA requirements), references security best practices like TEE integration, and discusses versioning strategies for upgradability.
- **Weak**: Vaguely suggests modularity without concrete patterns, overlooks chain-specific challenges beyond basic RPC, or ignores the security implications of architectural choices.

---

### Q2: Optimizing Transaction Signing Latency and Reliability for MPC Wallets

**Domain**: Performance & Quality Engineering | **CareerStage**: Senior | **RoleFocus**: IC |
**Difficulty**: I | **Criticality**: Quantified, Risk | **Stakeholders**: Frontend Engineers, Backend Engineers, DevOps | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:
Your team is facing challenges with transaction signing latency and reliability in your multi-party computation (MPC) wallet across mobile, web, and backend environments. Users report slow transaction approvals, especially on suboptimal network conditions, leading to poor user experience and potential transaction failures. How would you approach identifying bottlenecks and optimizing the signing process to ensure low latency and high reliability, while strictly adhering to cryptographic security? What performance metrics and quality assurance strategies would you implement?

**Answer Key (~150–250 words)**:
**Key Insight**: A strong candidate recognizes that MPC signing latency is heavily influenced by multi-round communication and cryptographic computation. Optimization requires a multi-pronged approach: leveraging efficient threshold signature schemes, optimizing network interactions, and distributing computation effectively across client-side (mobile/web) and server-side environments. Reliability involves robust error handling, retry mechanisms, and clear status feedback.
**Frameworks/Tools**: They would use `Prometheus` or similar monitoring tools to track `signing latency` (e.g., p95, p99 latencies), `error rates`, and `CPU/memory utilization` on different platforms. `Fuzz testing` and `property-based testing` (e.g., `QuickCheck`) are crucial QA strategies for cryptographic protocol robustness. `DORA metrics` can measure deployment frequency and change failure rates.
**Trade-offs & Metrics**: Key trade-offs include cryptographic strength vs. computational overhead (e.g., choosing `CGGMP21` for fewer rounds), network latency vs. share geographic distribution, and resource consumption vs. offloading computation. Metrics would focus on reducing average and tail latencies, minimizing `timeout errors`, and ensuring `transaction success rates`.
**Stakeholder Handling**: Collaboration with frontend engineers to optimize local cryptographic operations and UI feedback, backend engineers for efficient server-side processing and network protocols, and DevOps for infrastructure scaling and monitoring. Clear communication with product managers on acceptable latency thresholds and trade-offs is essential.
**Signals**:
- **Strong**: Articulates concrete performance metrics, discusses MPC-specific communication overhead, proposes specific algorithmic (e.g., latest TSS protocols) and engineering optimizations, and outlines systematic QA and monitoring strategies.
- **Weak**: Focuses only on generic network optimization, ignores cryptographic computation costs, or lacks a structured approach to performance bottleneck identification and resolution across diverse platforms.

---

### Q3: Prioritizing MPC Wallet Infrastructure Features with Resource Constraints

**Domain**: Product & Business Value | **CareerStage**: Senior | **RoleFocus**: Mixed |
**Difficulty**: I | **Criticality**: Roles, Action | **Stakeholders**: Product Manager, Engineering Lead, Business Development | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:
Your team is building out the next generation of MPC wallet infrastructure, including features like Account Abstraction (AA), Session Keys, and Social Recovery, alongside operational features like spending limits and approval flows. However, you face significant resource constraints (limited engineering time, budget). How would you prioritize the development and integration of these features to maximize business value and user adoption for both internal products and external partners, while maintaining robust security? How would you communicate these prioritization decisions to diverse stakeholders?

**Answer Key (~150–250 words)**:
**Key Insight**: A strong candidate will employ a structured prioritization framework to objectively evaluate features based on business value, user impact, technical feasibility, and security implications, especially under resource constraints. They understand that balancing security (fundamental to a wallet) with usability and strategic growth requires careful stakeholder alignment and transparent decision-making.
**Frameworks/Tools**: The candidate might use `WSJF (Weighted Shortest Job First)` to prioritize by considering business value, time criticality, risk reduction, and job size. `MoSCoW (Must-have, Should-have, Could-have, Won't-have)` can categorize features for clear communication. A simple `cost-benefit analysis` for each feature can also be used.
**Trade-offs & Metrics**: They should discuss trade-offs such as faster time-to-market for a subset of features versus delivering a comprehensive, fully-featured wallet later. Prioritizing `Social Recovery` could significantly boost user retention but requires careful security implementation. `Account Abstraction` offers long-term flexibility but is technically complex. Metrics would include `user adoption rates`, `churn reduction`, `partner integration velocity`, and `security incident rates` as indicators of value and risk mitigation.
**Stakeholder Handling**: They would engage product managers to define business goals and user needs, engineering leads for technical feasibility and implementation costs, security teams for threat modeling each feature, and business development for external partner requirements. Transparent communication of the rationale behind prioritization, using data and chosen frameworks, is key to managing expectations.
**Signals**:
- **Strong**: Uses concrete prioritization methods (e.g., WSJF), quantifies value and risk, integrates multi-stakeholder viewpoints into decision-making, and clearly articulates trade-offs.
- **Weak**: Prioritizes features based on personal preference or vague "industry trends," ignores resource constraints, or fails to engage or align diverse stakeholders effectively.

---

### Q4: Responding to a Novel Attack Vector in MPC Signature Protocols

**Domain**: Security & Regulation | **CareerStage**: Architect | **RoleFocus**: IC |
**Difficulty**: A | **Criticality**: Blocks, Risk, Action | **Stakeholders**: Security Team, Compliance Officer, Engineering Lead | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:
Your security research team has identified a novel side-channel attack affecting the GG20 threshold ECDSA implementation used in your MPC wallet, potentially allowing an attacker with privileged access to a single compromised node to infer partial key shares under specific transaction patterns. This is a severe vulnerability. Outline your immediate and long-term response plan, covering risk assessment, mitigation strategies (balancing urgency and stability), and clear communication protocols for the security, compliance, and engineering teams.

**Answer Key (~150–250 words)**:
**Key Insight**: A strong response prioritizes immediate containment and assessment, followed by a structured mitigation plan that balances the urgency of the security fix with system stability. It highlights the importance of thorough risk quantification and transparent, multi-stakeholder communication, especially given the cryptographic nature of the vulnerability.
**Frameworks/Tools**: The candidate should initiate a `STRIDE threat modeling` review specifically for Spoofing, Tampering, and Information Disclosure related to this attack. `CVSS (Common Vulnerability Scoring System)` would be used to quantify the vulnerability's severity and prioritize the response. The `NIST Cybersecurity Framework (CSF)` (Identify, Protect, Detect, Respond, Recover) can guide the overall incident response.
**Trade-offs & Metrics**: Immediate mitigation might involve temporarily disabling affected transaction types or increasing monitoring, balancing service availability against security exposure. Long-term, patching requires careful testing to ensure the fix doesn't introduce regressions. Metrics include `time-to-detection`, `time-to-containment`, `time-to-patch`, and `residual risk score`.
**Stakeholder Handling**: Communicate immediately with the `security team` for detailed analysis and validation. Engage the `engineering lead` to plan and execute patches, ensuring a rollback strategy. Inform the `compliance officer` about the regulatory implications and reporting obligations. Product managers need to be aware of any user-facing impacts or downtime. All communication must be factual, clear, and actionable.
**Signals**:
- **Strong**: Presents a clear, structured incident response plan, quantifies risk using established frameworks, proposes multi-layered mitigation (short-term containment, long-term fix), and details structured communication to all relevant stakeholders.
- **Weak**: Vague on immediate actions, underplays the severity, lacks a clear process for mitigation planning, or fails to consider the compliance and reputational impact of a cryptographic vulnerability.

---

### Q5: Leading Cross-Functional Effort for Device Verification and MFA Productization

**Domain**: Organization & Leadership | **CareerStage**: Senior | **RoleFocus**: Mixed |
**Difficulty**: I | **Criticality**: Roles, Action | **Stakeholders**: Backend, Security, Product Teams | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:
You need to lead the productization of a new security feature—advanced device verification and multi-factor authentication (MFA)—for your MPC wallet. This project requires close collaboration between backend, security, and product teams, each with distinct priorities (e.g., performance, hardening, user experience). How would you organize and lead this cross-functional initiative to ensure a secure, usable, and well-integrated solution is delivered on time, within six months? How would you foster alignment, resolve conflicts, and ensure clear accountability?

**Answer Key (~150–250 words)**:
**Key Insight**: A strong candidate will demonstrate the ability to orchestrate a complex cross-functional project by establishing clear roles, fostering open communication, and proactively managing conflicts. They understand that successfully productizing security features requires aligning technical implementation with product usability, ensuring all teams contribute effectively towards a shared goal.
**Frameworks/Tools**: They might propose using a `RACI matrix` to clarify responsibilities (Responsible, Accountable, Consulted, Informed) across the backend, security, and product teams for each component of the MFA feature. Concepts from `Team Topologies` could inform how teams interact and minimize cognitive load. Regular `Agile ceremonies` (stand-ups, sprint reviews, demos) would maintain synchronization.
**Trade-offs & Metrics**: Discussions should highlight balancing the need for strong security controls (e.g., FIDO2, biometric attestation) against potential user friction and implementation complexity. Key metrics would include `feature completion rate`, `defect escape rate`, `user adoption of MFA`, and `time-to-resolve cross-team blockers`.
**Stakeholder Handling**: They would initiate with a joint kick-off to establish a shared vision and success criteria. Facilitate regular syncs to address technical dependencies (backend), security implications (security), and user experience design (product). Conflicts (e.g., security strictness vs. UX simplicity) would be resolved through facilitated discussions focusing on trade-offs and agreed-upon risk appetite. Accountability would be maintained through clear ownership and regular progress reporting.
**Signals**:
- **Strong**: Clearly defines roles and responsibilities, outlines a structured communication plan, proposes specific conflict resolution tactics, and demonstrates an understanding of balancing security, UX, and delivery timelines.
- **Weak**: Provides a generic project management overview, fails to address the specific challenges of cross-functional security productization, or lacks strategies for aligning diverse team objectives.

---

### Q6: Strategic Evolution of Multi-Chain MPC Wallet for Emerging Standards

**Domain**: Roadmap & Ecosystem Strategy | **CareerStage**: Architect | **RoleFocus**: Mixed |
**Difficulty**: A | **Criticality**: Action, Quantified, Risk | **Stakeholders**: Product Manager, Business Development, Blockchain Core Developers | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:
As a Blockchain Architect for a multi-chain MPC wallet platform, you are responsible for defining its 12-18 month technical roadmap. The landscape is rapidly evolving with new EVM L2s, potential post-quantum signature algorithms, and deeper integration requirements from DeFi and custody partners. How would you design a roadmap that strategically positions the wallet for future compatibility and ecosystem leadership, balancing the pressures of early adoption against the critical need for stability, security, and sustained engineering focus?

**Answer Key (~150–250 words)**:
**Key Insight**: A strong candidate demonstrates strategic foresight, understanding that a flexible roadmap is essential for navigating the volatile blockchain ecosystem. They prioritize modularity and adaptable architecture to embrace emerging standards, while rigorously assessing risks and making data-driven decisions about when and how to adopt new technologies.
**Frameworks/Tools**: The candidate should propose using `OKRs (Objectives and Key Results)` to align the roadmap with high-level business goals (e.g., market share, partner growth). A `Technology Radar` approach would be used to continuously monitor and assess the maturity of new EVM L2s, signature protocols, and DeFi trends. `Risk matrices` can help quantify the trade-offs of early adoption (e.g., immature tech) versus waiting for stability.
**Trade-offs & Metrics**: Key trade-offs include being an early mover on a new chain/protocol (gaining competitive advantage) versus waiting for market validation (reducing integration risk). Metrics would track `time-to-integrate new chains`, `protocol upgrade success rates`, `partner satisfaction`, and `total addressable market expansion`.
**Stakeholder Handling**: They would actively engage product managers to understand market opportunities, business development to align with partner integration needs, and blockchain core developers to anticipate protocol changes. Regular reviews of the roadmap with these stakeholders, adapting based on market signals and competitive analysis, are crucial.
**Signals**:
- **Strong**: Articulates a flexible, iterative roadmap process, leverages explicit frameworks for technology assessment and prioritization, demonstrates an understanding of both technical and business risks/opportunities, and details proactive engagement with the broader ecosystem.
- **Weak**: Presents a rigid, linear roadmap without consideration for market dynamics, focuses solely on technical features without business justification, or overlooks the importance of external partnerships and emerging standards.

## Sources

[1] ATLAS: Efficient and Scalable MPC in the Honest Majority Setting, https://www.semanticscholar.org/paper/abcd2e67d685b76487687bd9aee5569c9e741d92
[2] Arcula: A Secure Hierarchical Deterministic Wallet for Multi-asset Blockchains, https://arxiv.org/abs/1906.05919
[3] Securing blockchain transactions using quantum teleportation and quantum digital signature, https://link.springer.com/article/10.1007/s11063-020-10272-1
[4] A panoramic survey of the advanced encryption standard: from architecture to security analysis, key management, real-world applications, and post-quantum …, https://link.springer.com/article/10.1007/s10207-025-01116-x
[5] SECURE SOFTWARE DEVELOPMENT: INTEGRATING ENCRYPTION PROTOCOLS FROM DESIGN TO DEPLOYMENT, https://ijamjournal.org/ijam/publication/index.php/ijam/article/view/714
[6] Blockchain-Based Decentralized Identity Management for Secure Digital Transactions, https://www.macawpublications.com/Journals/index.php/SMRJ/article/view/33
[7] EthVault: A Secure and Resource-Conscious FPGA-Based Ethereum Cold Wallet, https://arxiv.org/abs/2510.23847
[8] The impact of quantum computing on cryptographic systems: Urgency of quantum-resistant algorithms and practical applications in cryptography, https://ej-compute.org/index.php/compute/article/view/146
[9] Distributed systems and trusted execution environments: Trade-offs and challenges, https://arxiv.org/abs/2001.09670
[10] MPC Wallets: A Complete Technical Guide (2025) - Stackup, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide
[11] Exploring the Efficiency of MPC Algorithms in Crypto Wallets - CertiK, https://www.certik.com/resources/blog/exploring-the-efficiency-of-mpc-algorithms-in-crypto-wallets
[12] What Is an MPC Wallet and How Does It Work - Safeheron, https://safeheron.com/blog/what-is-an-mpc-wallet-and-how-does-an-mpc-wallet-work/
[13] Fireblocks' Multi-Layer Digital Asset Security, https://www.fireblocks.com/report/fireblocks-multi-layer-digital-asset-security
[14] Cryptocurrency Wallets A to Z. Exploring Design, Vulnerability &…, https://medium.com/exponential-science-foundation/cryptocurrency-wallets-a-to-z-da60c6d9fd9d
[15] Decentralized Cryptocurrency Wallet, https://www.semanticscholar.org/paper/7eb5a185a8f3e2b1d81d991c7843c88d8c397e20
[16] On the Computational Overhead of MPC with Dishonest Majority, https://www.semanticscholar.org/paper/a2612643ce357e1e4ae5b6d04a972cfdbf11fbe0
[17] Stakeholders' Blockchain Engagement: An Interdependence Theory's Principle of Interaction's Framework, https://www.semanticscholar.org/paper/35c450d15f0df06f90456e0108649903f0876986
[18] Security Challenges, https://link.springer.com/chapter/10.1007/978-3-032-03413-7_2
[19] Multichain DeFi draws near with Chain Signatures - Blockworks, https://blockworks.co/news/near-protocol-chain-signatures-multichain-defi
[20] MPC Wallets vs Multisig: Security & Control Comparison | Squads Blog, https://squads.xyz/blog/mpc-wallets-risks-vs-multisig
[21] About the Cisco UCS Director REST API SDK Bundle, https://www.semanticscholar.org/paper/f1a77339f2977f39c6bcafbdd4170ee5357dfc68
[22] Gaza Wallet: A Simple and Efficient Blockchain Application, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3660325
[23] Design and Implementation of Time-lock Wallet using Blockchain Technology, https://www.semanticscholar.org/paper/8cedb49e9f85021c08ddb6f4536a8f87a599ddae
[24] Understanding MPC Wallets: Enhancing Security and Privacy in ..., https://dev.to/parth51199/understanding-mpc-wallets-enhancing-security-and-privacy-in-cryptocurrency-management-4oa
[25] (PDF) Software Quality Assurance in Network Security using ..., https://www.researchgate.net/publication/351841770_Software_Quality_Assurance_in_Network_Security_using_Cryptographic_Techniques
[26] Achieving Maximum Efficiency in Schnorr-based Multi-signature and Applications in Blockchain, https://arxiv.org/abs/2305.13699
[27] MPC Wallet Security Risks: Four Attack Vectors and Fixes - LinkedIn, https://www.linkedin.com/posts/daniel-campbell-536310252_practical-key-extraction-attacks-in-leading-activity-7379619482874355712-cH7_
[28] Incident Response - Security operations and threat response, https://console.settlemint.com/documentation/blockchain-platform/security/incident-response
[29] What Is the STRIDE Threat Model? Beginner's Guide - 2025, https://www.practical-devsecops.com/what-is-stride-threat-model/
[30] Enterprise Blockchain Security: Strategic Guide for CISOs and CTOs, https://hacken.io/discover/enterprise-blockchain-security/
[31] Understanding CVSS Base Scores - Balbix, https://www.balbix.com/insights/base-cvss-scores/
