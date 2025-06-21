'Blockchain Attacks, Defends, and Emergency Measures.' Requirements: 1. Ensure compliance with MECE. 2. Classify/categorize logically and appropriately if necessary. 3. Explain with analogy and examples. 4. Use numbered lists for clear explanations when possible. 5. Describe core elements, components, factors and aspects. 6. List core evaluation dimensions and corresponding evaluations if applicable. 7. Describe their concepts, definitions, functions, and characteristics. 8. Clarify their purposes and assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect). 9. Describe relevant markets, ecosystems, regulations, and economic models, and explain the corresponding strategies used to generate revenue. 10. Describe their work mechanism concisely first and then explain how they work with phase-based workflows throughout the entire lifecycle. 11. Clarify their preconditions, inputs, outputs, immediate outcomes, long-term impacts, and potential implications. 12. Clarify their underlying laws, axioms, theories, and patterns. 13. Describe the design philosophy and architectural features. 14. Provide ideas, techniques, and means of architectural refactoring. 15. Clarify relevant frameworks, models, and principles. 16. Clarify their origins, evolutions, and trends. 17. List key historical events, security incidents, core factual statements, raw data points, and summarized statistical insights. 18. Clarify techniques, methods, approaches, protocols, and algorithms.  19. Describe contradictions and trade-offs. 20. Identify and list all major competitors (including the one being searched at present) with concise descriptions within the target market or industry segment. 21. Conduct a comprehensive competitor analysis to evaluate each competitor’s (including the one being searched at present) operational strategies, product offerings, market position, and performance metrics. 22. Perform a SWOT analysis for each competitor (including the one being searched at present), categorizing findings into strengths, weaknesses, opportunities, and threats. 23. Clarify principles, rules, constrains, limitations, vulnerabilities, challenges, obstacles, and risks. 24. Describe potential security vulnerabilities, troubleshooting methods, attack tactics, prevention methods and emergency measures. 25. Describe potential performance bottlenecks, troubleshooting methods and optimization measures. 26. Explain priorities, use cases, pitfalls, and best practices. 27. Clarify cause-and-effect relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 28. Clarify interdependency relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 29. Clarify cardinality-based relationships (1:1, 1:M, M:N). 26. Clarify contradictory relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 30. Describe the existing non-trivial problems and potential approaches to address them. 31. Introduce the relevant research topics of significant value that remain to be overcome. 32. Introduce the possible directions and approaches of within-domain and cross-domain innovation. 33. Predict the ultimate form of the related development. 34. Make a summary table at the end with purposes, characteristics, use cases, ect. for clarity. 35. Append the terminologies, formulas, and analogies at the end with concise descriptions for each item.

Thu Jun 12 2025

### MECE-Compliant Classification of Blockchain Attacks, Defenses, and Emergency Measures

A robust analysis of blockchain security requires a framework that is Mutually Exclusive and Collectively Exhaustive (MECE), logically categorizing attacks, defenses, and emergency measures across the core functional layers of blockchain systems: Network, Consensus, Application, and Meta-Application. This structure ensures every threat and response is appropriately placed and no overlaps occur, facilitating targeted control and evaluation.

1. **Network Layer**  
   - Attacks: Sybil, Eclipse, Distributed Denial of Service (DDoS)  
   - Defenses: Peer authentication, random peer selection, encryption, bandwidth rate limiting  
   - Emergency Measures: Node isolation, traffic filtering, connection reconfiguration

2. **Consensus Layer**  
   - Attacks: 51% Attack, Selfish mining, Long-Range Attack in PoS  
   - Defenses: Byzantine Fault Tolerant (BFT) protocols, stake/economic penalties, consensus adjustments  
   - Emergency Measures: Protocol upgrades/hard forks, slashing, real-time monitoring

3. **Application Layer**  
   - Attacks: Smart contract bugs (e.g., reentrancy), replay attack, wallet theft  
   - Defenses: Formal contract verification, multisig wallets, replay protection  
   - Emergency Measures: Contract suspension, patching, key rotation

4. **Meta-Application Layer**  
   - Attacks: Oracle manipulation, cross-chain bridge exploits  
   - Defenses: Decentralized oracles, validated bridge protocols, anomaly detection  
   - Emergency Measures: Oracle/bridge suspension, failover to backup nodes 

---

### Analogies and Examples by Category

- **Network Layer**:  
  - *Sybil attack*: Like stuffing a ballot box with fake votes to unfairly influence an election.
  - *Eclipse attack*: Trapping someone in a room so all incoming mail is intercepted and filtered.
- **Consensus Layer**:  
  - *51% attack*: A group secretly buys majority voting shares in a company to rewrite its official history.
- **Application Layer**:  
  - *Replay attack*: A duplicated signed check is cashed at a second bank after a policy change.
  - *Smart contract bug*: A vending machine dispenses infinite goods due to a coding oversight.
- **Meta-Application Layer**:  
  - *Oracle manipulation*: Faking a weather report to a smart farm, making it water at the wrong time.

---

### Numbered Explanations of Categories

1. **Network Layer**
   1. Attacks: Sybil (multiple fake nodes), Eclipse (node isolation), DDoS (resource overwhelming).
   2. Defenses: Encrypted, authenticated communications, random peer selection, network monitoring.
   3. Emergency Measures: Immediate node quarantine, peer blacklist, dynamic topology changes.

2. **Consensus Layer**
   1. Attacks: 51% attack (majority control), selfish mining (withholding blocks), long-range PoS attacks (past stake manipulation).
   2. Defenses: BFT protocols (e.g., PBFT, HotStuff), staking and slashing, reward penalization.
   3. Emergency Measures: Protocol hard forks, chain reorganizations, stake forfeiture.

3. **Application Layer**
   1. Attacks: Reentrancy, replay, faulty logic in contracts, phishing/key theft.
   2. Defenses: Formal verification, code audits, multi-factor authentication.
   3. Emergency Measures: Contract pausing, patch deployments, wallet freezes.

4. **Meta-Application Layer**
   1. Attacks: Oracle price manipulation, cross-chain relay hacks.
   2. Defenses: Multiparty oracles, threshold signatures, multi-layer validation.
   3. Emergency Measures: Oracle/bridge cut-off, automated rollback.

---

### Core Elements, Components, Factors, and Aspects

**Elements and Components**  
- Nodes/Peers, consensus participants, smart contract infrastructure, external data agents, cross-chain gateways.

**Factors and Aspects**  
- Degree of decentralization, economic incentives, vulnerability of participant interfaces (wallets, smart contracts), composability with other networks/applications.

---

### Core Evaluation Dimensions and Criteria

| Evaluation Dimension | Criteria for Assessment                                     |
|----------------------|------------------------------------------------------------|
| Impact Layer         | Network, Consensus, Application, Meta-Application          |
| Attack Complexity    | Technical difficulty, resource needs, stealth              |
| Economic Incentive   | Potential gain vs. exploitation cost                       |
| Scope and Scale      | Number of nodes/users affected, chain-wide or limited      |
| Detection Speed      | Time to identification and response                        |
| Resilience           | Ability to recover/maintain correct state                  |
| Regulatory Impact    | Compliance with AML/KYC, privacy, reporting                |
| Performance Impact   | Transactions/second, latency, scalability post-attack      |

---

### Concepts, Definitions, Functions, and Characteristics

- **Concepts**: Blockchain attacks leverage protocol or implementation weaknesses to undermine network integrity, disrupt service, or steal funds. Defenses are built into protocol and operational practices to deter, detect, and mitigate such threats. Emergency measures are rapid, planned responses to limit damage, restore service, and prevent recurrence.
- **Definitions**:  
  - *Sybil attack*: Multiple fake identities in a network.  
  - *51% attack*: Majority control for history rewriting.
- **Functions**: Disruption, manipulation, unauthorized gain for attacks; prevention, resilience, and recovery for defenses; rapid containment for emergency measures.
- **Characteristics**: Multi-layered, evolving, economically incentivized, exploitative of system openness.

---

### Purposes and Assumptions

- **Purpose**:  
  - Attacks: Steal, alter history, disrupt trust, manipulate outcomes.  
  - Defenses: Preserve network honesty, maintain data integrity, deter malicious behavior.  
  - Emergency Measures: Minimize impact, restore trust, document incidents.
- **Assumptions**:
  - Honest majority, secure cryptography, rational adversaries, open participation.
- **Worldview**: Adversarial, game-theoretic, economic alignment of behavior.
- **Cause-and-Effect**: Vulnerability exploited -leads to-> loss or disruption -triggers-> defense/emergency mitigation.

---

### Markets, Ecosystems, Regulations, and Economic Models

- **Markets**: Cryptocurrencies, DeFi, IoT, enterprise blockchains.
- **Ecosystems**: Public (permissionless), private (consortium/permissioned), cross-chain bridges, layered DApps/platforms.
- **Regulations**: Jurisdiction-dependent, AML, KYC, data privacy laws, incident disclosure.
- **Economic Models**: PoW/PoS mining, staking, transaction fees, security auditing services, DeFi insurance, marketplace fees.

---

### Work Mechanisms and Lifecycle

1. **Concise Mechanisms**
   - Attacks: Insert fake nodes, manipulate consensus, exploit contracts/oracles.
   - Defenses: Authenticate, monitor, align incentives, enforce economic slashing.
   - Emergency: Patch, upgrade, isolate, rotate keys, incident record.
2. **Phase-Based Lifecycle**
   1. Reconnaissance and preparation
   2. Execution (attack/defense deployment)
   3. Impact (system/asset compromise)
   4. Detection and containment (emergency begins)
   5. Recovery and patch (return to normal/forensic analysis).

---

### Preconditions, Inputs, Outputs, Outcomes, Long-term Impacts

- **Preconditions**: Open peer participation, smart contract programmability, off-chain data reliance.
- **Inputs**: Network traffic, economic stake, contract code, oracle feeds.
- **Outputs**: Transaction rewrites, asset theft, service degradation, fake data propagation.
- **Immediate Outcomes**: Financial loss, chain forks, DoS, smart contract drains.
- **Long-Term Impacts**: Trust erosion, regulatory response, ecosystem evolution, changed incentive structures.
- **Implications**: Higher security demand, increased insurance, AI-driven monitoring.

---

### Underlying Laws, Axioms, Theories, Patterns

- **Byzantine Fault Tolerance**: Security holds until a threshold of bad actors is reached (often ≤1/3).
- **Honest Majority**: PoW, PoS depend on more than half of miners/stakers acting honestly.
- **Cryptographic Assumptions**: Hash and signature schemes are unbroken.
- **Game Theory**: Rewards/punishments align behavior (Nash equilibrium applied).
- **Immutability/Cascading**: A block's tampering breaks every child, ensuring integrity.

---

### Design Philosophy and Architectural Features

- **Layered and Modular**: Isolation of vulnerabilities for targeted defenses.
- **Decentralization**: No single point of failure, permissionless participation.
- **Incentive Structures**: Economic gains for behaving honestly, slashing/penalties for misbehavior.
- **Programmable Resilience**: Automated monitoring and incident logging.
- **Upgradeability**: Ability to patch via hard forks, upgradable contracts, or modular consensus.

---

### Architectural Refactoring Ideas

- Decompose monolithic code into network, consensus, and application modules.
- Introduce cryptographic peer verification for onboarding.
- Implement upgradeable, modular consensus protocols.
- Use formal verification for critical smart contract logic.
- Embed real-time monitoring and AI-driven analytics for intrusion/anomaly detection.

---

### Frameworks, Models, and Principles

- **Layer-based Security Models**: Data, Network, Consensus, Application.
- **Attack Graphs**: Map attack paths and dependencies.
- **Game-Theoretic Models**: Analyze incentive alignment.
- **Cross-Chain Security Frameworks**: Address bridge and oracle vulnerabilities.
- **Incident Response Taxonomies**: Classify and structure emergency actions.

---

### Origins, Evolutions, and Trends

- **Origins**: Derived from cryptographic timestamping and digital currency research culminating in Bitcoin.
- **Evolution**: From basic network/consensus attacks to sophisticated, layered, multi-vector exploits (e.g., cross-chain bridges, DeFi smart contracts).
- **Trends**: Increasing automation in detection and defense, AI/ML integration, focus on cross-domain and quantum-resistant cryptography.

---

### Key Historical Events, Security Incidents, Core Facts, and Data

- **2014 Mt. Gox hack**: $474 million stolen, nearly bankrupting the largest exchange at the time.
- **2016 DAO Hack**: Reentrancy flaw in Ethereum smart contract resulted in $60 million theft.
- **2021-2024 Cross-chain bridge hacks**: Ronin, Poly, BNB—all over $600 million each due to bridge/contract flaws.
- **Projected annual blockchain losses**: Anticipated to reach $30 billion by 2025.
- **Detection tool advancement**: BridgeGuard achieves attack detection TPS of 65, exceeding Ethereum’s typical 12.4 TPS.

---

### Techniques, Methods, Protocols, and Algorithms

- **Attacks**: Sybil flooding, Eclipse isolation, selfish mining strategies, contract exploits, replay injection, oracle manipulation.
- **Defenses**: Byzantine consensus, cryptographic authentication, economic slashing, monitoring, formal verification, multisig, decentralized oracles.
- **Emergency**: Incident reporting (BISCUIT process), chain rollback, patching, key revocation, upgrade mechanisms.

---

### Contradictions and Trade-offs

- **Scalability vs. Security vs. Decentralization (Trilemma)**: Cannot maximize all three—improving one reduces the others.
- **Immutability vs. Flexibility**: Permanent records limit agility in crisis response.
- **Privacy vs. Transparency**: Strong privacy weakens audit, but open ledgers threaten confidentiality.

---

### Competitors and SWOT Analyses

- **Network Defense Solution Providers**
  - *Description*: Offer peer/authentication, Sybil/Eclipse resistance.
  - *SWOT*: Strong technical control, may add latency/costs, opportunity as DDoS escalates, risk from attacker sophistication.
- **Application Security Auditors**
  - *Description*: Contract audit/formal verification specialists.
  - *SWOT*: Reduces contract risk, costly/time-consuming, demand from DeFi growth, risk of new exploit classes emerging.
- **Collaborative Defense Platforms (e.g., Defensechain)**
  - *Description*: Share threat intelligence, block global attacks.
  - *SWOT*: Resilient communities, interoperability hurdles, opportunity for global integration, risk of slow adaptation.
- **Consortium Blockchain Providers**
  - *Description*: Vertical/enterprise-permissioned blockchains.
  - *SWOT*: Efficient governance and access, but can be a single point of failure, strong in regulated industries, may face public trust issues.

---

### Principles, Constraints, Vulnerabilities, Challenges, and Risks

- **Principles**: Decentralization, immutability, consensus, cryptographic security.
- **Constraints**: Throughput limits, energy/resource requirements, need for compliance and standardization.
- **Vulnerabilities**: Coding bugs, protocol design flaws, network openness.
- **Challenges**: Fast-evolving attacks, complexity, human factors, cross-chain scalability.
- **Risks**: Capital loss, system instability, regulatory intervention, reputational damage.

---

### Security Vulnerabilities, Troubleshooting, Attack Tactics, Prevention, and Emergency

- **Vulnerabilities**: Smart contract bugs, peer identity weaknesses, external data feeds, bridge flaws.
- **Troubleshooting**: Network monitoring, contract audits, anomaly detection, traffic analysis, forensic postmortems.
- **Attack Tactics**: Rapid resource assembly (DDoS), slow/targeted code exploitation, phishing, multi-stage persistence.
- **Prevention**: Formal verification, dynamic monitoring, randomized peer connections, slashing, insurance, audits.
- **Emergency Measures**: Node/contract quarantine, incident reporting, patching, network reconfiguration, chain rollback, rapid forensics.

---

### Performance Bottlenecks, Troubleshooting, Optimization

- **Bottlenecks**: Consensus overhead (PBFT communication), bandwidth/resource limits, smart contract execution slowness.
- **Troubleshooting**: Throughput latency monitoring, resource profiling, node status tracking.
- **Optimization**: Sharding, batch verification, randomized leader election, AI-based resource scaling.

---

### Priorities, Use Cases, Pitfalls, Best Practices

- **Priorities**: Layered security, user education, real-time monitoring, cross-domain coordination.
- **Use Cases**: Crypto exchange, DeFi, emergency logistics, anonymous voting, authenticated communications.
- **Pitfalls**: Over-complexity, under-audited code, centralization risks, AI overreliance.
- **Best Practices**: Holistic lifelong auditing, layered defenses, consensus modularity, rapid incident communication, transparency.

---

### Cause-and-Effect, Interdependency, Cardinality, Contradictory Relationships

- *Sybil attack* <-enables-> *51% attack* (1:M).
- *Eclipse attack* <-facilitates-> *Replay attack* (1:1 or M:N, depending on context).
- *Formal verification improvement* <-reduces-> *Smart contract exploitation* (direct opposition).
- Stronger decentralization <-reduces-> attack feasibility but <-increases-> consensus complexity (contradiction).

---

### Existing Non-trivial Problems and Approaches

- Cross-chain interoperability flaws (e.g., bridges), rapid DApp innovation introducing new bugs, trouble reconciling GDPR-like privacy with blockchain immutability.
- Approaches: Post-quantum crypto, multi-domain formal verification, AI-powered detection, modular access/reconfiguration, insurance frameworks.

---

### High-Value Research Topics

1. AI/ML-driven anomaly and attack detection.
2. Formal verification at scale for smart contracts.
3. Quantum-resistant consensus and signatures.
4. Secure cross-chain bridge and oracle design.
5. Blockchain-based emergency logistics and healthcare.
6. Automated incident reporting and response coordination.

---

### Innovation Directions

- **Within-domain**: Adaptive layered security, post-quantum readiness, modular upgradability.
- **Cross-domain**: Federated AI/blockchain integration, secure digital ID across blockchains, inter-consortium collaboration.

---

### Ultimate Development Form

Blockchain defenses will become modular, AI-enhanced, and quantum-resistant, with real-time, collaborative, cross-domain incident response, dynamic adaptation to new threats, and strong formal verification and incentive-alignment frameworks, supporting full trust and resilience at global scale.

---

### Summary Table: Blockchain Attacks, Defenses, and Emergency Measures

| Category          | Purpose                              | Characteristics                | Use Cases                | Defenses/Mitigations   | Emergency Measures     |
|-------------------|--------------------------------------|--------------------------------|--------------------------|------------------------|-----------------------|
| Network Layer     | Disrupt communication, isolate nodes | Sybil, Eclipse, DDoS           | Node onboarding, relay   | Authentication, random peers, rate limiting | Node isolation, traffic filtering |
| Consensus Layer   | Manipulate block validation/history   | 51% attack, selfish mining     | Transaction finality     | BFT, stake slashing    | Hard forks, patching  |
| Application Layer | Exploit contract/wallet logic         | Smart contract bug, replay     | DeFi, DApps, wallets     | Audits, formal verification, multisig     | Pause/freeze contracts, patch deployments |
| Meta-App Layer    | Corrupt external data, cross-chain   | Oracle, bridge manipulation    | Price feeds, asset swaps | Decentralized oracles, validated bridges   | Failover, oracle suspension   |

---

### Terminologies, Formulas, and Analogies

- **Sybil Attack**: Fake node identities; “stuffing the ballot box”.
- **Eclipse Attack**: Node isolation; “locked in a room with filtered mail”.
- **51% Attack**: Majority control to rewrite history; “hostile corporate takeover”.
- **Selfish Mining**: Withholding blocks for gain; “hiding your hand until the best time”.
- **Replay Attack**: Duplicate check after a policy change; “photocopying and cashing the same check twice”.
- **Verifiable Delay Functions (VDFs)**: “Time-locked safe” ensuring orderly transaction ordering.
- **Byzantine Fault Tolerance**: Security until fraction threshold is breached.
- **Blockchain Trilemma**: Security, scalability, decentralization—only two can be maximized at once.

Formulas:
- **Double Spend Probability**: \\[ Q_z = \left( \\frac{q}{p} \\right)^z \\], with \\(q\\) attacker power, \\(p\\) honest miner power, \\(z\\) block confirmations.
- **Chain Growth/Quality Axioms**: Expected honest block ratio over time.

This comprehensive analysis aligns with MECE principles and provides a structured, cross-layer, and multi-dimensional view of blockchain security, offering actionable insight and reference for both technical practitioners and ecosystem stakeholders.

Bibliography
A Abdollahi, F Sadeghvaziri, & A Rejeb. (2023). Exploring the role of blockchain technology in value creation: a multiple case study approach. In Quality & Quantity. https://link.springer.com/article/10.1007/s11135-022-01348-2

A Alkhalifah, A Ng, & MJM Chowdhury. (2019). An empirical analysis of blockchain cybersecurity incidents. https://ieeexplore.ieee.org/abstract/document/9162381/

A. Averin & O. Averina. (2019). Review of Blockchain Technology Vulnerabilities and Blockchain-System Attacks. In 2019 International Multi-Conference on Industrial Engineering and Modern Technologies (FarEastCon). https://ieeexplore.ieee.org/document/8934243/

A. Farion, O. Dluhopolskyi, S. Banakh, Nadiia Moskaliuk, Mykhailyna Farion, & Yuryi Ivashuk. (2019). Using blockchain Technology for Boost Cyber Security. In 2019 9th International Conference on Advanced Computer Information Technologies (ACIT). https://ieeexplore.ieee.org/document/8780019/

A Malhotra, H O’Neill, & P Stowell. (2022). Thinking strategically about blockchain adoption and risk mitigation. In Business Horizons. https://www.sciencedirect.com/science/article/pii/S0007681321000355

A Sharma, D Upadhyay, & S Sharma. (2024). Enhancing blockchain security: A novel approach to integrated malware defence mechanisms. https://iopscience.iop.org/article/10.1088/2631-8695/ad4ba7/meta

Abhishek Guru, Bhabendu Kumar Mohanta, Hitesh Mohapatra, Fadi M. Al-Turjman, Chadi Altrjman, & Arvind Yadav. (2023). A Survey on Consensus Protocols and Attacks on Blockchain Technology. In Applied Sciences. https://www.mdpi.com/2076-3417/13/4/2604

Ahmed Said Abdel-Sattar & Marianne A. Azer. (2022). Using Blockchain Technology in MANETs Security. In 2022 2nd International Mobile, Intelligent, and Ubiquitous Computing Conference (MIUCC). https://ieeexplore.ieee.org/document/9781696/

Ahsan Umar & Muhammad Zeeshan Zafar. (2025). Blockchain Security: Vulnerabilities and Protective Measures. In World Journal of Advanced Research and Reviews. https://www.semanticscholar.org/paper/f99fdf112d898217ce4c4f6d640c1389df12eda9

AKE Onjewu, N Walton, & I Koliousis. (2023). Blockchain agency theory. https://www.sciencedirect.com/science/article/pii/S0040162523001671

Amit Chaurasia. (2020). IIoT Benefits and Challenges with BlockChain. In 2020 International Conference on Decision Aid Sciences and Application (DASA). https://ieeexplore.ieee.org/document/9317171/

Amrita Jyoti, Vikash Yadav, & M. Rahul. (2023). Blockchain Security Attacks, Difficulty, and Prevention. In Recent Advances in Electrical &amp; Electronic Engineering (Formerly Recent Patents on Electrical &amp; Electronic Engineering). https://www.eurekaselect.com/article/135169

Ang Jia. (2024). Research on Emergency Logistics Optimization Strategy  Based on Blockchain Technology. In Artificial Intelligence Technology Research. https://www.semanticscholar.org/paper/8504c620172e515e61dff9a5b575375cd04d3609

Anjee Gorkhali & Rajib Chowdhury. (2021). Blockchain and the Evolving Financial Market: A Literature Review. In Journal of Industrial Integration and Management. https://www.worldscientific.com/doi/10.1142/S242486222150024X

AO Efuntade & FCA FCIB. (2023). SWOT Analysis of Blockchain Funding, Platform Finance, Financial Big Data and Financial Engineering Under the Background of Financial Innovation and …. https://www.iiardjournals.org/get/IJEFM/VOL.%208%20NO.%204%202023/SWOT%20ANALYSIS%20OF%20BLOCKCHAIN.pdf

Austin Draper, Aryan Familrouhani, D. Cao, Tevisophea Heng, & Wenlin Han. (2019). Security Applications and Challenges in Blockchain. In 2019 IEEE International Conference on Consumer Electronics (ICCE). https://ieeexplore.ieee.org/document/8661914/

B. Gupta, Amrita Dahiya, Chivesh Upneja, Aditi Garg, & Ruby Choudhary. (2020). A Comprehensive Survey on DDoS Attacks and Recent Defense Mechanisms. https://www.semanticscholar.org/paper/d2b759a5b1b5a5dcd9eeb19dbb3574debdf5d585

B. Putz, Manfred Vielberth, & G. Pernul. (2022). BISCUIT - Blockchain Security Incident Reporting based on Human Observations. In Proceedings of the 17th International Conference on Availability, Reliability and Security. https://dl.acm.org/doi/10.1145/3538969.3538984

B Rodrigues, L Eisenring, & E Scheid. (2019). Evaluating a blockchain-based cooperative defense. https://ieeexplore.ieee.org/abstract/document/8717792/

Bhawana, S Kumar, RS Rathore, & M Mahmud. (2022). BEST—blockchain-enabled secure and trusted public emergency services for smart cities environment. In Sensors. https://www.mdpi.com/1424-8220/22/15/5733

C Fan, S Ghaemi, H Khazaei, & P Musilek. (2020). Performance evaluation of blockchain systems: A systematic survey. In Ieee Access. https://ieeexplore.ieee.org/abstract/document/9129732/

C Killer, B Rodrigues, & B Stiller. (2019). Security management and visualization in a blockchain-based collaborative defense. https://ieeexplore.ieee.org/abstract/document/8751272/

C L’Hermitte & NKC Nair. (2021). A blockchain‐enabled framework for sharing logistics resources during emergency operations. In Disasters. https://onlinelibrary.wiley.com/doi/abs/10.1111/disa.12436

C Siemon, D Rueckel, & B Krumay. (2020). Blockchain technology for emergency response. https://scholarspace.manoa.hawaii.edu/bitstream/10125/63814/1/0061.pdf

Chuansheng Wang, Zixian Guo, Fulei Shi, Mingyue Chen, Xinyu Wang, & Jia Liu. (2024). Research on emergency logistics information traceability model and resource optimization allocation strategies based on consortium blockchain. In PLOS ONE. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0303143

D Dasgupta, JM Shrein, & KD Gupta. (2019). A survey of blockchain from security perspective. https://link.springer.com/article/10.1007/s42786-018-00002-6

D Marletta, A Midolo, & E Tramontana. (2025). A Blockchain-Based Strategy for Certifying Timestamps in a Distributed Healthcare Emergency Response Systems. In Future Internet. https://www.mdpi.com/1999-5903/17/5/210

D Mishra & S Phansalkar. (2025). Blockchain Security in Focus: A Comprehensive Investigation into Threats, Smart Contract Security, Cross-Chain Bridges, Vulnerabilities Detection Tools & …. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10946113/

D. Rafferty & K. Curran. (2021). The Role of Blockchain in Cyber Security. In Semiconductor Science and Information Devices. https://www.semanticscholar.org/paper/516767cb27ce95b4c54062be1c6fa29cf5e7176a

Da Ning, Chu Li, Lin Xu, & Fang Xiong. (2022). Research on Intelligent Security Management Architecture of Military Blockchain. In 2022 IEEE 20th International Conference on Embedded and Ubiquitous Computing (EUC). https://ieeexplore.ieee.org/document/10086336/

Deepanshu Garg, Anu Kaushik, R. S. Bali, & Maninderpal Singh. (2024). AEMT: Blockchain Based Authenticated Emergency Message Transmission in SDVN. In 2024 IEEE International Conference on Communications Workshops (ICC Workshops). https://ieeexplore.ieee.org/document/10615627/

Dr Sarwar Sayeed. (2020). Security of Blockchain Consensus Protocols. https://www.semanticscholar.org/paper/e5350ec93d3170abbea5022df0d89f3e8fac66a6

Duwenkai Hou. (2024). The Importance of Corporate Culture, Governance Structure, and Laws and Regulations in the Fintech Ecosystem. In Advances in Economics, Management and Political Sciences. https://www.ewadirect.com/proceedings/aemps/article/view/14801

E Zamani, Y He, & M Phillips. (2020). On the security risks of the blockchain. https://www.tandfonline.com/doi/abs/10.1080/08874417.2018.1538709

Eric Cooper, Eric Weese, Alex Fortson, D. Lo, & Yong Shi. (2023). Cyber Security in Blockchain. In 2023 IEEE Conference on Dependable and Secure Computing (DSC). https://ieeexplore.ieee.org/document/10354161/

F Nadezda & A Josef. (2021). Economic perspectives of the Blockchain technology: Application of a SWOT analysis. In Terra Economicus. https://cyberleninka.ru/article/n/economic-perspectives-of-the-blockchain-technology-application-of-a-swot-analysis

FAN Zhongqi & DAI Lin. (2023). Application of blockchain technology in emergency management: hotspots, challenges and prospects. In China Safety Science Journal. http://www.cssjj.com.cn/EN/10.16265/j.cnki.issn1003-3033.2023.05.1377

Felix Irresberger, Kose John, & Fahad Saleh. (2020). The Public Blockchain Ecosystem: An Empirical Analysis. In Organizations & Markets: Policies & Processes eJournal. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3478264

Fouzia Alzhrani, Kawther Saeedi, & Liping Zhao. (2023). Architectural Patterns for Blockchain Systems and Application Design. In Applied Sciences. https://www.mdpi.com/2076-3417/13/20/11533

G. Spasova & Mihaela Todorova. (2023). Address Generation and Transaction Simulation in Blockchain. In 2023 4th International Conference on Communications, Information, Electronic and Energy Systems (CIEES). https://ieeexplore.ieee.org/document/10378791/

Georgy Ishmaev. (2019). Open Sourcing Normative Assumptions on Privacy and Other Moral Values in Blockchain Applications. https://www.semanticscholar.org/paper/841a6ec10349f2c5c25b4fde0550449d4c992c6a

Ghassan O. Karame & Elli Audroulaki. (2016). Bitcoin and Blockchain Security. https://www.semanticscholar.org/paper/e6c3af91b191a496506b947c77fd28c836a5b31b

Ghassan O. Karame & Srdjan Capkun. (2018). Blockchain Security and Privacy. In IEEE Secur. Priv. https://ieeexplore.ieee.org/document/8425621/

Guorong Chen. (2022). Discussion on Blockchain System Attack and Defense Technology. In Academic Journal of Computing &amp; Information Science. https://francis-press.com/papers/5994

Gurupriya M, Dharshan J Y, Rohit K C, & Sridhar Sk. (2025). Efficient Determent of Sybil Attacks in Blockchain. In 2025 International Conference on Multi-Agent Systems for Collaborative Intelligence (ICMSCI). https://ieeexplore.ieee.org/document/10894178/

H Chen, M Pendleton, L Njilla, & S Xu. (2020). A survey on ethereum systems security: Vulnerabilities, attacks, and defenses. In ACM Computing Surveys (CSUR). https://dl.acm.org/doi/abs/10.1145/3391195

H. Eren, Özgür Karaduman, & M. Gençoğlu. (2025). Security Challenges and Performance Trade-Offs in On-Chain and Off-Chain Blockchain Storage: A Comprehensive Review. In Applied Sciences. https://www.mdpi.com/2076-3417/15/6/3225

H Guo & X Yu. (2022). A survey on blockchain technology and its security. In Blockchain: research and applications. https://www.sciencedirect.com/science/article/pii/S2096720922000070

H. Halpin & M. Piekarska. (2017). Introduction to Security and Privacy on the Blockchain. In 2017 IEEE European Symposium on Security and Privacy Workshops (EuroS&PW). https://ieeexplore.ieee.org/document/7966963/

H Hasanova, U Baek, M Shin, & K Cho. (2019). A survey on blockchain cybersecurity vulnerabilities and possible countermeasures. https://onlinelibrary.wiley.com/doi/abs/10.1002/nem.2060

H Honar Pajooh, M Rashid, F Alam, & S Demidenko. (2021). Multi-layer blockchain-based security architecture for internet of things. In Sensors. https://www.mdpi.com/1424-8220/21/3/772

H Huang, W Kong, S Zhou, & Z Zheng. (2021). A survey of state-of-the-art on blockchains: Theories, modelings, and tools. https://dl.acm.org/doi/abs/10.1145/3441692

H Key. (2025). Automated Reasoning in Blockchain: Foundations, Applications, and Frontiers. In arXiv. https://arxiv.org/abs/2503.20461

H Lee, K Sung, K Lee, & J Lee. (2018). Economic analysis of blockchain technology on digital platform market. https://ieeexplore.ieee.org/abstract/document/8639624/

H Wang, Y Wang, Z Cao, & Z Li. (2019). An overview of blockchain security analysis. https://library.oapen.org/bitstream/handle/20.500.12657/23271/1006885.pdf?sequence=1#page=61

Haifeng Liu, Hongsheng Yan, Gang Chen, & Tao Xia. (2022). Research on mission planning and data security of cross-domain dynamic authorization based on blockchain. In Other Conferences. https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12246/2643621/Research-on-mission-planning-and-data-security-of-cross-domain/10.1117/12.2643621.full

Hansa Vaghela & Vivek Khirasaria. (2023). A Review on Detection and Prevention of the DDoS Attacks in the Blockchain. In 2023 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS). https://ieeexplore.ieee.org/document/10425005/

Hao Wang, Chunpeng Ge, & Zhe Liu. (2021). On the Security of Permissionless Blockchain Systems: Challenges and Research Perspective. In 2021 IEEE Conference on Dependable and Secure Computing (DSC). https://ieeexplore.ieee.org/document/9346243/

Hector Roussille, Ö. Gürcan, & F. Michel. (2023). A Taxonomy of Blockchain Incentive Vulnerabilities for Networked Intelligent Systems. In IEEE Communications Magazine. https://ieeexplore.ieee.org/document/10144509/

Hourieh Alsadat Hosseini, Alireza Hedayati, & Smart Contracts. (n.d.). A Survey on Blockchain: Challenges, Attacks, Security, and Privacy. https://www.semanticscholar.org/paper/840b72915c5d89e1276572aa4ef79b069cc898a2

Huaming Du, Junfang Zeng, Yuguo An, Jing Zhang, & Jian Zhao. (2019). Exploration on the Application of Blockchain in the Security System of Smart Park. In Proceedings of the 1st International Electronics Communication Conference. https://dl.acm.org/doi/10.1145/3343147.3343167

I Abrar & JA Sheikh. (2023). Intelligent blockchain technologies for disaster management: challenges, research gap and solutions. https://www.inderscienceonline.com/doi/abs/10.1504/IJBC.2023.138380

I Homoliak & S Venugopalan. (2020). The security reference architecture for blockchains: Toward a standardized model for studying vulnerabilities, threats, and defenses. https://ieeexplore.ieee.org/abstract/document/9239372/

Ilja Moisejevs. (2019). Adversarial Attacks and Defenses in Malware Classification: A Survey. https://www.semanticscholar.org/paper/42dd61047a8c0e733d57ac6f71205cce5a5f4172

J Cai, L Weni, H Fengi, K Fangi, & J Cheni. (2024). An Overview of Security Threats, Attack Detection and Defense for Large-Scale Multi-Agent Systems (LSMAS) in Internet of Things (IoT). https://ieeexplore.ieee.org/abstract/document/10787271/

J Cheng, L Xie, X Tang, N Xiong, & B Liu. (2021). A survey of security threats and defense on Blockchain. https://link.springer.com/article/10.1007/s11042-020-09368-6

J. Garay, A. Kiayias, & Giorgos Panagiotakos. (2019). Iterated Search Problems and Blockchain Security under Falsifiable Assumptions. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/c37eddba85cfb25d2fd2bc61a73c645ee138fefd

J Leng, M Zhou, JL Zhao, & Y Huang. (2020). Blockchain security: A survey of techniques and research directions. https://ieeexplore.ieee.org/abstract/document/9271868/

J Moubarak, E Filiol, & M Chamoun. (2018). On blockchain security and relevant attacks. https://ieeexplore.ieee.org/abstract/document/8371010/

J Zhang & M Wu. (2021). Cooperation mechanism in blockchain by evolutionary game theory. In Complexity. https://onlinelibrary.wiley.com/doi/abs/10.1155/2021/1258730

Jiajing Wu, Kai-Xuan Lin, Dan-yan Lin, Bozhao Zhang, Zhiying Wu, & Jianzhong Su. (2024). Safeguarding Blockchain Ecosystem: Understanding and Detecting Attack Transactions on Cross-chain Bridges. In ArXiv. https://dl.acm.org/doi/10.1145/3696410.3714604

Joydip Das, Syed Ashraf Al Tasin, Md. Forhad Rabbi, & M. Ferdous. (2024). Analysing Attacks on Blockchain Systems in a Layer-based Approach. In ArXiv. https://arxiv.org/abs/2409.10109

Junchuan Liang, Rong Wang, Chaosheng Feng, & C. Chang. (2023). A Survey on Federated Learning Poisoning Attacks and Defenses. In ArXiv. https://arxiv.org/abs/2306.03397

Junjie Hu, Xunzhi Chen, Huan Yan, & Na Ruan. (2024). BM-PAW: A Profitable Mining Attack in the PoW-based Blockchain System. In ArXiv. https://arxiv.org/abs/2411.06187

Junxian Chen. (2024). Securing the Chain: Comprehensive Analysis of Vulnerabilities and Defense Mechanisms in Blockchain Systems. In Applied and Computational Engineering. https://www.ewadirect.com/proceedings/ace/article/view/17465

K Hameed, M Barika, S Garg, & MB Amin. (2022). A taxonomy study on securing Blockchain-based Industrial applications: An overview, application perspectives, requirements, attacks, countermeasures, and open …. https://www.sciencedirect.com/science/article/pii/S2452414X21001060

K Hunt & J Zhuang. (2022). Blockchain for disaster management. https://link.springer.com/chapter/10.1007/978-3-030-87304-2_10

K. Sharma & Deepak Jain. (2019). Consensus Algorithms in Blockchain Technology: A Survey. In 2019 10th International Conference on Computing, Communication and Networking Technologies (ICCCNT). https://ieeexplore.ieee.org/document/8944509/

K Sienkiewicz-Małyjurek. (2022). Benefits, challenges, and perspectives of using the blockchain technology in emergency management. In Bezpieczeństwo. Teoria i Praktyka. https://www.ceeol.com/search/article-detail?id=1097732

Kai Otsuki, Ryuya Nakamura, & Kazuyuki Shudo. (2021). Impact of Saving Attacks on Blockchain Consensus. In IEEE Access. https://ieeexplore.ieee.org/document/9547320/

Kameswara Rao Kesavarapu, V. P. Venkatesan, Alyssa Hertig, T. Koens, Coen Ramaekers, C. V. Wijk, & Ehab Zaghloul. (2019). Security Attacks on Blockchain. In International Journal of Computer Applications. https://www.ijcaonline.org/archives/volume178/number16/kesavarapu-2019-ijca-918942.pdf

Kaustubh Dwivedi, Ankit Agrawal, Ashutosh Bhatia, & Kamlesh Tiwari. (2024). A Novel Classification of Attacks on Blockchain Layers: Vulnerabilities, Attacks, Mitigations, and Research Directions. In ArXiv. https://www.semanticscholar.org/paper/f3731921fb5eda40d288266224822c5451b7720c

KM Saylaubaevna. (2019). SWOT-analysis of Blockchain technology. In European science. https://cyberleninka.ru/article/n/swot-analysis-of-blockchain-technology

L Duan, Y Sun, W Ni, W Ding, & J Liu. (2023). Attacks against cross-chain systems and defense approaches: A contemporary survey. https://ieeexplore.ieee.org/abstract/document/10194241/

L. Fu & J. Su. (2021). Research on Technical Innovation of Emergency Supply Chain Management Based on Blockchain Technology. In 2021 International Conference on Electronic Information Engineering and Computer Science (EIECS). https://ieeexplore.ieee.org/document/9588108/

L. König, S. Unger, Peter Kieseberg, & S. Tjoa. (2020). The Risks of the Blockchain A Review on Current Vulnerabilities and Attacks. In J. Internet Serv. Inf. Secur. https://isyou.info/jisis/vol10/no3/jisis-2020-vol10-no3-06.pdf

Liehuang Zhu, Baokun Zheng, Meng Shen, Shui Yu, Feng Gao, Hongyu Li, Kexin Shi, & Keke Gai. (2018). Research on the Security of Blockchain Data: A Survey. In ArXiv. https://www.semanticscholar.org/paper/d79f579736124e856d113f27d9c0c327e890a6b3

M Baboi. (2023). Security of consensus mechanisms in blockchain. In Romanian Cyber Security Journal. https://rocys.ici.ro/documents/107/Art._5_ROCYS_2_2023.pdf

M Conklin, B Elzweig, & LJ Trautman. (2023). Legal Recourse for Victims of Blockchain and Cyber Breach Attacks. In UC Davis Bus. LJ. https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/ucdbulj23&section=6

M Dabbagh, KKR Choo, A Beheshti, & M Tahir. (2021). A survey of empirical performance evaluation of permissioned blockchain platforms: Challenges and opportunities. In computers & security. https://www.sciencedirect.com/science/article/pii/S0167404820303515

M Krichen, M Ammi, A Mihoub, & M Almutiq. (2022). Blockchain for modern applications: A survey. In Sensors. https://www.mdpi.com/1424-8220/22/14/5274

M. Mostafa. (2020). Bitcoin’s Blockchain Peer-to-Peer Network Security Attacks and Countermeasures. In Indian journal of science and technology. https://indjst.org/articles/bitcoins-blockchain-peer-to-peer-network-security-attacks-and-countermeasures

M Saad & D Mohaisen. (2023). Three birds with one stone: Efficient partitioning attacks on interdependent cryptocurrency networks. https://ieeexplore.ieee.org/abstract/document/10179456/

M Saad, J Spaulding, & L Njilla. (2020). Exploring the attack surface of blockchain: A comprehensive survey. https://ieeexplore.ieee.org/abstract/document/9019870/

M Saad, J Spaulding, L Njilla, & C Kamhoua. (2019). Exploring the attack surface of blockchain: A systematic overview. https://arxiv.org/abs/1904.03487

MA AlAfnan & SF MohdZuki. (2024). Malaysia‟ s National Blockchain Roadmap: A Critical Discourse Analysis of Focus, Goals, and Challenges. In World. https://www.researchgate.net/profile/Mohammad-Alafnan/publication/381551864_Malaysia’s_National_Blockchain_Roadmap_A_Critical_Discourse_Analysis_of_Focus_Goals_and_Challenges/links/67026e5e906bca2ac3e8c33e/Malaysias-National-Blockchain-Roadmap-A-Critical-Discourse-Analysis-of-Focus-Goals-and-Challenges.pdf

Mani Asgari Rouzbahani & Hossein Gharaee Garakani. (2024). Blockchain Security Threats: Survey. In 2024 11th International Symposium on Telecommunications (IST). https://ieeexplore.ieee.org/document/10843593/

Maria Letizia Perugini & M. Spada. (2020). Blockchain Security, a Multilayer Paradigm. In ERN: Technology (Topic). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3121534

Masashi Sato & Shin’ichiro Matsuo. (2017). Long-Term Public Blockchain: Resilience against Compromise of Underlying Cryptography. In 2017 26th International Conference on Computer Communication and Networks (ICCCN). https://ieeexplore.ieee.org/document/7966969/

Mayank Raikwar & D. Gligoroski. (2022). DoS Attacks on Blockchain Ecosystem. In Euro-Par Workshops. https://arxiv.org/abs/2205.13322

Michael Mirkin. (2020). BDoS: Blockchain Denial-of-Service Attacks. https://www.semanticscholar.org/paper/8ec653a8b6661b5c9cd6b19a87a5c3b53851b765

Mingzhe Li, You Lin, Wei Wang, & Jin Zhang. (2024). SP-Chain: Boosting Intra-Shard and Cross-Shard Security and Performance in Blockchain Sharding. In ArXiv. https://arxiv.org/abs/2407.06953

Mital Panchal, Pranav Zambre, & Ankit Chouhan. (2022). Network Security Issues in Blockchain Architectures. In 2022 5th International Conference on Advances in Science and Technology (ICAST). https://ieeexplore.ieee.org/document/10039532/

MNM Bhutta, AA Khwaja, A Nadeem, & HF Ahmad. (2021). A survey on blockchain technology: Evolution, architecture and security. https://ieeexplore.ieee.org/abstract/document/9402747/

Mohamad Arsalan Sheikh, Gul Zameen Khan, & F. Hussain. (2022). Systematic Analysis of DDoS Attacks in Blockchain. In 2022 24th International Conference on Advanced Communication Technology (ICACT). https://ieeexplore.ieee.org/document/9728816/

Mohd Azeem Faizi Noor & Khurram Mustafa. (2024). Mitigating Blockchain Endpoint Vulnerabilities: Conceptual Frameworks. In International Journal of Computer Networks and Applications. https://www.semanticscholar.org/paper/6990a056e98b7804ceabfc5acae980fefbce5abf

Mwrwan Abubakar, Belinda I. Onyeashie, Isam Wadhaj, Petra Leimich, Hisham Ali, & William J. Buchanan. (2024). A Systematic Review of the Blockchain Technology Security Challenges and Threats Classification. In 2024 6th International Conference on Blockchain Computing and Applications (BCCA). https://ieeexplore.ieee.org/document/10844455/

N. Anita & V. Murugesan. (2019). Blockchain Security Attack: A Brief Survey. In 2019 10th International Conference on Computing, Communication and Networking Technologies (ICCCNT). https://ieeexplore.ieee.org/document/8944615/

N Dong, Z Wang, J Sun, & M Kampffmeyer. (2024). Defending against poisoning attacks in federated learning with blockchain. https://ieeexplore.ieee.org/abstract/document/10471193/

Neelkumar K. Shah, Mayur Bilapate, Sachin Nandurkar, M. A. Maalik, Niteshkumar Harne, Karimullah Shaik, & Ajai Kumar. (2024). Security Assessment Framework and Evaluation for Blockchain Applications (SAFE-Block). In 2024 IEEE International Conference on Blockchain and Distributed Systems Security (ICBDS). https://ieeexplore.ieee.org/document/10837302/

Nils Amiet. (2021). Blockchain Vulnerabilities in Practice. In Digital Threats: Research and Practice. https://dl.acm.org/doi/10.1145/3407230

Odhran O’Donoghue, Anuraag A. Vazirani, D. Brindley, & E. Meinert. (2018). Design Choices and Trade-Offs in Health Care Blockchain Implementations: Systematic Review (Preprint). https://preprints.jmir.org/preprint/12426

P Hanafizadeh & M Alipour. (2024). Taxonomy of theories for blockchain applications in business and management. In Digital Business. https://www.sciencedirect.com/science/article/pii/S2666954424000085

P Kieseberg, S Tjoa, & JRC Blockchains. (2020). The Risks of the Blockchain A Review on Current Vulnerabilities and Attacks. https://www.researchgate.net/profile/Lukas-Koenig-13/publication/363091448_The_Risks_of_the_Blockchain_A_Review_on_Current_Vulnerabilities_and_Attacks/links/630dd4b6acd814437feb1510/The-Risks-of-the-Blockchain-A-Review-on-Current-Vulnerabilities-and-Attacks.pdf

Paulina Kus, Gregorios Yogas, & Sundara. (2019). BLOCKCHAIN FOR IMPROVEMENT OF EMERGENCY RESPONSE IN HUMANITARIAN LOGISTICS INDONESIA. https://www.semanticscholar.org/paper/16e41f7dab318678bd0216a2c557c6ae06f28891

Priya D. Dozier & C. Saunders. (2020). The Inter-organizational Perspective in Blockchain Adoption within an Ecosystem. In European Conference on Information Systems. https://www.semanticscholar.org/paper/56245f1854977abcf6bb6f5300281ad223bc5cca

R Anandan & BS Deepak. (2022). An overview of blockchain technology: fundamental theories and concepts. https://www.worldscientific.com/doi/pdf/10.1142/11959#page=50

R Chaganti, RV Boppana, V Ravi, & K Munir. (2022). A comprehensive review of denial of service attacks in blockchain ecosystem and open challenges. https://ieeexplore.ieee.org/abstract/document/9881505/

R Halim. (2022). Decentralization, Scalability, and Security Trade-off in Blockchain System: Comparison on Different Approaches. http://essay.utwente.nl/91994/

R. Peng, Di Wu, Mengyao Sun, & Shaomin Wu. (2020). An attack-defense game on interdependent networks. In Journal of the Operational Research Society. https://www.tandfonline.com/doi/full/10.1080/01605682.2020.1784048

R Shevchuk, I Lishchynskyy, M Ciura, & M Lyzun. (2025). Application of Blockchain Technology in Emergency Management Systems: A Bibliometric Analysis. In Applied Sciences. https://www.mdpi.com/2076-3417/15/10/5405

R Singh, S Tanwar, & TP Sharma. (2020). Utilization of blockchain for mitigating the distributed denial of service attacks. In Security and Privacy. https://onlinelibrary.wiley.com/doi/abs/10.1002/spy2.96

S Aggarwal & N Kumar. (2021). Attacks on blockchain. In Advances in computers. https://www.sciencedirect.com/science/article/pii/S0065245820300759

S. Alqahtani & M. Demirbas. (2021). Bottlenecks in Blockchain Consensus Protocols. In 2021 IEEE International Conference on Omni-Layer Intelligent Systems (COINS). https://ieeexplore.ieee.org/document/9524210/

S Goncharov & A Nechesov. (2023). Axiomatization of Blockchain Theory. In Mathematics. https://www.mdpi.com/2227-7390/11/13/2966

S. Hammer. (2018). The Blockchain Ecosystem. In IRPN: Innovation & Entrepreneurship (Topic). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3281020

S. Misra, Anandarup Mukherjee, Arijit Roy, Nishant Saurabh, Y. Rahulamathavan, & M. Rajarajan. (2021). Blockchain at the Edge: Performance of Resource-Constrained IoT Networks. In IEEE Transactions on Parallel and Distributed Systems. https://ieeexplore.ieee.org/document/9158540/

S. Prianga, R. Sagana, & E. Sharon. (2018). Evolutionary Survey On Data Security In Cloud Computing Using Blockchain. In 2018 IEEE International Conference on System, Computation, Automation and Networking (ICSCA). https://ieeexplore.ieee.org/document/8541258/

S Purohit, P Calyam, & S Wang. (2020). Defensechain: Consortium blockchain for cyber threat intelligence sharing and defense. https://ieeexplore.ieee.org/abstract/document/9223313/

S Sayeed & H Marco-Gisbert. (2019). Assessing blockchain consensus and security mechanisms against the 51% attack. In Applied sciences. https://www.mdpi.com/2076-3417/9/9/1788

S Singh, ASMS Hosen, & B Yoon. (2021). Blockchain security attacks, challenges, and solutions for the future distributed iot network. In Ieee Access. https://ieeexplore.ieee.org/abstract/document/9323061/

S Zhou, Z Yang, J Xiang, Y Cao, & Y Zhang. (2020). An ever-evolving game: Evaluation of real-world attacks and defenses in ethereum ecosystem. https://www.usenix.org/conference/usenixsecurity20/presentation/zhou-shunfan

Sabreen AHMADJEE∗, C. Mera-Gómez, & Rami Bahsoon. (n.d.). Security Architectural Approaches and Risk Assessment Methods for Blockchain Systems: A Review and Future Directions. https://www.semanticscholar.org/paper/06db04633c2162cecd069a214da11ce40063420e

Samuel Pierre, M. Srivatsa, Arun Iyengar, Jian Yin, Ling Liu, Alberto Compagno, Mauro Conti, Paolo Gasti, Zhihong Tian, Ritu Maheshwari, A. Sairam, Thomas Dubendorfer, & Matthias Bossardt. (2015). Survey of DOS defense mechanisms. In 2015 International Conference on Innovations in Information, Embedded and Communication Systems (ICIIECS). https://ieeexplore.ieee.org/document/7193058/

Sergey N. Kosnikov, Alexander L. Zolkin, Sergey A. Zhiltsov, & Alexey V. Novikov. (2024). THE ROLE OF BLOCKCHAIN TECHNOLOGIES IN ENSURING TRANSPARENCY AND SECURITY OF ECONOMIC TRANSACTIONS. In EKONOMIKA I UPRAVLENIE: PROBLEMY, RESHENIYA. https://s-lib.com/en/issues/eiu_2024_12_v15_a5/

Shengjun Liu, Ningkang Jiang, & Yuanbin Wu. (2020). Visual Attack and Defense on Text. In ArXiv. https://www.semanticscholar.org/paper/e39dbae97e95dfe7462dba8de69ef0e9658d3da2

Shijie Zhang & Jong‐Hyouk Lee. (2019). Eclipse-based Stake-Bleeding Attacks in PoS Blockchain Systems. In Proceedings of the 2019 ACM International Symposium on Blockchain and Secure Critical Infrastructure. https://dl.acm.org/doi/10.1145/3327960.3332391

Shohreh Radrahimi & Reza Tavoli. (2018). The revenue based on the blockchain technology platform. https://www.semanticscholar.org/paper/41d05fe7877a62ec00442429c147048f1859f507

Sirine Sayadi, S. Rejeb, & Z. Choukair. (2018). Blockchain Challenges and Security Schemes: A Survey. In 2018 Seventh International Conference on Communications and Networking (ComNet). https://ieeexplore.ieee.org/document/8621944/

Soma Prathibha, V. Saiganesh, & S. Lokesh. (2023). Survey on Prevention of DDoS Using Blockchain. In 2023 5th International Conference on Inventive Research in Computing Applications (ICIRCA). https://ieeexplore.ieee.org/document/10220655/

Souhail Mssassi & Anas Abou El Kalam. (2024). The Blockchain Trilemma: A Formal Proof of the Inherent Trade-Offs Among Decentralization, Security, and Scalability. In Applied Sciences. https://www.mdpi.com/2076-3417/15/1/19

Sushama Pawar, Shonal Vaz, Yogita Khandagale, Archana Gopnarayan, & Manisha Pokharkar. (2024). Blockchain and Cryptocurrency Security: Challenges, Innovations, and Future Directions. In International Journal of Advanced Research in Science, Communication and Technology. https://www.semanticscholar.org/paper/519049f34908cf921e359781fcd9f3aac2440100

Swati Jadhav, Vaibhavi Bhosale, Gauri Choudhari, Rishita Bura, & Manasi Bhavik. (2024). DDoS Attack Detection in Blockchain Networks. In 2024 5th International Conference on Data Intelligence and Cognitive Informatics (ICDICI). https://ieeexplore.ieee.org/document/10810961/

T Hristova, P Hristov, & G Mihaylov. (2024). SWOT analysis in building a blockchain data sharing system. https://ieeexplore.ieee.org/abstract/document/10600620/

Tam T. Huynh, T. Nguyen, & Hanh Tan. (2019). A Survey on Security and Privacy Issues of Blockchain Technology. In 2019 International Conference on System Science and Engineering (ICSSE). https://ieeexplore.ieee.org/document/8823094/

Taotao Wang, Chonghe Zhao, Qing Yang, & Shengli Zhang. (2020). Ethna: Analyzing the Underlying Peer-to-Peer Network of the Ethereum Blockchain. In ArXiv. https://www.semanticscholar.org/paper/f238ebf51bcbfdec30086cd5b04e9bccf19b19a1

Taras Bachynskyy & Roman Radeiko. (2019). Legal Regulations of Blockchain and Cryptocurrency in Ukraine. In Hungarian Journal of Legal Studies. https://www.semanticscholar.org/paper/3de57c086aad3676f0562a5beded3433ccbc08bd

Triveni P, Jaikishen, & Sanjana R. (2024). Analysis of blockchain law and regulations. In ITM Web of Conferences. https://www.itm-conferences.org/10.1051/itmconf/20246801010

U Hacioglu. (2020). Digital business strategies in blockchain ecosystems. In Springer International Publishing. https://link.springer.com/content/pdf/10.1007/978-3-030-29739-8.pdf

V Maurya, V Rishiwal, M Yadav, & M Shiblee. (2025). Blockchain-driven security for IoT networks: State-of-the-art, challenges and future directions. https://link.springer.com/article/10.1007/s12083-024-01812-w

Venkata Venugopal Rao Gudlur & Murugan Thangiah. (2024). Cyber Risks and Blockchain Security for Digital Forensics. In 2024 IEEE 14th Symposium on Computer Applications & Industrial Electronics (ISCAIE). https://ieeexplore.ieee.org/document/10576471/

VR Podile, Y Rishika, & KL Manasa. (2023). Blockchain Exploratory Analysis in Strategic Management. https://ieeexplore.ieee.org/abstract/document/10182901/

W Ahmed. (2025). Advanced Persistent Threats and Blockchain Technology: Exploring the Potential of Decentralized Defense Mechanisms. In Science. https://premierscience.com/wp-content/uploads/2025/02/pjs-25-729.pdf

W Song, M Zhu, D Lu, C Zhu, J Zhao, Y Sun, & L Li. (2024). Blockchain Bottleneck Analysis Based on Performance Metrics Causality. In Electronics. https://www.mdpi.com/2079-9292/13/21/4236

Wan Qiquan & Shao Wenpeng. (2020). Application Analysis of Blockchain Technology in the Field of Emergency Management. https://www.semanticscholar.org/paper/f41c192be88c8ec6d1572b0d6f0068de0c7fb97f

Wanqin Cao, Yun-Ping Huang, Dezheng Li, Feng Yang, Xiaofeng Jiang, & Jian Yang. (2021). A Blockchain Based Link-Flooding Attack Detection Scheme. In 2021 IEEE 4th Advanced Information Management, Communicates, Electronic and Automation Control Conference (IMCEC). https://ieeexplore.ieee.org/document/9482363/

Wenqi Wang, Benxiao Tang, Run Wang, Lina Wang, & Aoshuang Ye. (2019). A survey on Adversarial Attacks and Defenses in Text. In ArXiv. https://www.semanticscholar.org/paper/45a06f184092522751d19f93f4297ff678ad1ba7

X Li, J Cheng, Z Shi, J Liu, B Zhang, X Xu, & X Tang. (2023). Blockchain security threats and collaborative defense: A literature review. https://ttu-ir.tdl.org/items/6d101f9e-b889-48a1-a708-310730b53d29

Xinyu Liang. (2025). Security Challenges and Defense Strategies in Blockchain Systems. In Applied and Computational Engineering. https://www.ewadirect.com/proceedings/ace/article/view/21087

Xiong Jin-hua. (2011). The Safety Supervision Measures of Emergency. https://www.semanticscholar.org/paper/0fc20a2cd20f696a3334af95bfd510d4e172fc81

Y Chen, H Chen, Y Zhang, M Han, & M Siddula. (2022). A survey on blockchain systems: Attacks, defenses, and privacy preservation. https://www.sciencedirect.com/science/article/pii/S2667295221000386

Y Wang & H Chen. (2022). Blockchain: A potential technology to improve the performance of collaborative emergency management with multi-agent participation. In International Journal of Disaster Risk Reduction. https://www.sciencedirect.com/science/article/pii/S2212420922000863

Yuguo Li. (n.d.). Exploring the Evolution, Trade-offs, and Applications of Blockchain Technology. https://www.semanticscholar.org/paper/5c012aef9b0987113c704b8c07ee85a4f52f23f9

Z Feng, Y Li, & X Ma. (2023). Blockchain-oriented approach for detecting cyber-attack transactions. In Financial Innovation. https://link.springer.com/article/10.1186/s40854-023-00490-6

Z Ghazaryan. (1951). Blockchain Technology: Transforming Industries and Shaping the Future. In Available at SSRN 5188339. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5188339

Z Li. (2024). The impact of blockchain security breaches. https://open.library.ubc.ca/soa/cIRcle/collections/ubctheses/24/items/1.0440990

Z Liu & X Li. (2025). Sok: Security analysis of blockchain-based cryptocurrency. In arXiv. https://arxiv.org/abs/2503.22156

Z. Mamadiyarov. (2024). SECURITY ISSUES IN BLOCKCHAIN TECHNOLOGY. In International Journal of Artificial Intelligence for Digital Marketing. https://www.semanticscholar.org/paper/48f6fba1197e412dccab407d3722a218f94fcef6

Z Shah, I Ullah, H Li, A Levula, & K Khurshid. (2022). Blockchain based solutions to mitigate distributed denial of service (DDoS) attacks in the Internet of Things (IoT): A survey. In Sensors. https://www.mdpi.com/1424-8220/22/3/1094

Zichao Wang. (2024). A comparative analysis of blockchain attack classifications. In Applied and Computational Engineering. https://www.semanticscholar.org/paper/170d9e558309658021b95080aa02d4c4638bed48

Zubaida Rehman, Mark A. Gregory, I. Gondal, Hai Dong, & Mengmeng Ge. (2025). Eclipse Attacks in Blockchain Networks: Detection, Prevention, and Future Directions. In IEEE Access. https://ieeexplore.ieee.org/document/10872918/



Generated by Liner
https://getliner.com/search/s/5926611/t/85556131