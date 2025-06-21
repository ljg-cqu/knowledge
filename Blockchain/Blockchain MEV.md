'Blockchain MEV.' Requirements: 1. Ensure compliance with MECE. 2. Classify/categorize logically and appropriately if necessary. 3. Explain with analogy and examples. 4. Use numbered lists for clear explanations when possible. 5. Describe core elements, components, factors and aspects. 6. List core evaluation dimensions and corresponding evaluations if applicable. 7. Describe their concepts, definitions, functions, and characteristics. 8. Clarify their purposes and assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect). 9. Describe relevant markets, ecosystems, regulations, and economic models, and explain the corresponding strategies used to generate revenue. 10. Describe their work mechanism concisely first and then explain how they work with phase-based workflows throughout the entire lifecycle. 11. Clarify their preconditions, inputs, outputs, immediate outcomes, long-term impacts, and potential implications. 12. Clarify their underlying laws, axioms, theories, and patterns. 13. Describe the design philosophy and architectural features. 14. Provide ideas, techniques, and means of architectural refactoring. 15. Clarify relevant frameworks, models, and principles. 16. Clarify their origins, evolutions, and trends. 17. List key historical events, security incidents, core factual statements, raw data points, and summarized statistical insights. 18. Clarify techniques, methods, approaches, protocols, and algorithms.  19. Describe contradictions and trade-offs. 20. Identify and list all major competitors (including the one being searched at present) with concise descriptions within the target market or industry segment. 21. Conduct a comprehensive competitor analysis to evaluate each competitor’s (including the one being searched at present) operational strategies, product offerings, market position, and performance metrics. 22. Perform a SWOT analysis for each competitor (including the one being searched at present), categorizing findings into strengths, weaknesses, opportunities, and threats. 23. Clarify principles, rules, constrains, limitations, vulnerabilities, challenges, obstacles, and risks. 24. Describe potential security vulnerabilities, troubleshooting methods, attack tactics, prevention methods and emergency measures. 25. Describe potential performance bottlenecks, troubleshooting methods and optimization measures. 26. Explain priorities, use cases, pitfalls, and best practices. 27. Clarify cause-and-effect relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 28. Clarify interdependency relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 29. Clarify cardinality-based relationships (1:1, 1:M, M:N). 26. Clarify contradictory relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 30. Describe the existing non-trivial problems and potential approaches to address them. 31. Introduce the relevant research topics of significant value that remain to be overcome. 32. Introduce the possible directions and approaches of within-domain and cross-domain innovation. 33. Predict the ultimate form of the related development. 34. Make a summary table at the end with purposes, characteristics, use cases, ect. for clarity. 35. Append the terminologies, formulas, and analogies at the end with concise descriptions for each item.

Thu Jun 12 2025

### Introduction to Blockchain MEV: Definition and Conceptual Framework

Maximal Extractable Value (MEV) in blockchain represents the maximum value that block producers, such as miners or validators, can extract over and above the standard block rewards and transaction fees by strategically determining the order, inclusion, or exclusion of transactions within a block. Originally described as "Miner Extractable Value" in proof-of-work (PoW) systems, the concept expanded in proof-of-stake (PoS) systems to encompass all block-producing entities, thus the term "Maximal Extractable Value". MEV encompasses practices such as front-running, sandwich attacks, and arbitrage, which may either harm (value-diverting) or enhance (value-creating) the broader ecosystem.

### Logical MECE-Classifications of Blockchain MEV

To comply with the MECE (Mutually Exclusive, Collectively Exhaustive) principle, MEV can be structured along the following axes:

1. **MEV Types**  
   a. Value-Diverting MEV (e.g., front-running, sandwich attacks)  
   b. Value-Creating MEV (e.g., arbitrage, liquidations)  

2. **Role and Actor-Based Classification**  
   a. Block Producers (miners/validators)  
   b. Searchers (bots scanning for opportunities)  
   c. Builders/Relays (entities optimizing blocks for MEV extraction)  

3. **Mechanisms and Strategies**  
   a. Transaction reordering  
   b. Inclusion/Exclusion manipulations  
   c. Bundle auctions and sealed-bid systems  

4. **Architectural and Economic Models**  
   a. Direct extraction (by miners/validators)  
   b. Auction-based mechanisms (e.g., Flashbots, Execution Tickets)  

These categories are mutually exclusive and collectively exhaustive, offering a comprehensive lens to view MEV's dynamics.

### Analogy and Real-World Examples

- **Analogy to Traditional Finance**: MEV is akin to high-frequency traders or brokers front-running retail orders in financial markets. This analogy highlights the ability of block producers to profit by observing and acting ahead of users in a manner similar to unethical trading practices.
- **Real-World Example**: On Ethereum, suppose user A submits a swap transaction on a decentralized exchange. A searcher bot spots this in the public mempool and submits its own transactions that are strategically ordered before and after user A's transaction (a "sandwich attack") to manipulate the trade price and capture profit.
- **Auction Analogy**: Transaction ordering is similar to an auction where different parties bid for priority access, and the winner derives surplus value by dictating execution sequence.

### Core Elements, Components, Factors, and Aspects

**Core Elements**
1. Block Producers (privileged organizers of blocks)
2. Transactions (user-submitted with latent value)
3. Searchers (bots exploiting MEV opportunities)
4. Relays/Builders (optimizing and submitting bundles)
5. Auctions/Protocols (configuring blockspace allocation)

**Key Components and Factors**
- Transaction order power
- Public vs. private mempool design
- Searcher competition and bundling
- Economic incentives and fee structures
- Protocol-level market constructs (e.g., Flashbots, Execution Tickets)

### Numbered Classification and Workflow

1. User submits transactions to mempool
2. Searchers analyze the mempool for MEV opportunities
3. Searchers submit bundles or prioritized transactions
4. Builders/relays aggregate and optimize bundles for maximal payoff
5. Auctions or proposers choose the most profitable payload/block
6. Block is produced and MEV is realized

### Core Evaluation Dimensions & Corresponding Criteria

1. **Economic Impact**: MEV extracted, total value transferred, distribution of profits, miner/validator revenue spikes.
2. **Network Security & Decentralization**: Incidence of centralization, concentration of MEV extraction, changes in decentralization metrics.
3. **Fairness**: Impact on user experience, prevalence of value-diverting vs. value-creating MEV.
4. **Performance**: Transaction latency, network congestion, scalability.
5. **Effectiveness of Mitigation**: Measured reduction in adverse MEV incidents, protocol resilience.
6. **Regulatory and Compliance**: Alignment with legal frameworks, transparency, auditability.

### Concepts, Definitions, Functions, and Characteristics

**Concepts and Definitions**:  
- MEV quantifies the maximum profit achievable through arbitrary transaction reordering, including, or excluding within a block.
- Adversarial MEV is the supremum attainable regardless of actor identity or current token holding.

**Functions and Characteristics**:  
- MEV can drive both efficiency (e.g., arbitrage) and market manipulation (e.g., sandwich attacks).
- It incentivizes both innovation and harmful centralization.
- Plays a dual role: revenue source and source of instability.

### Purposes and Underlying Assumptions

**Value/Prescriptive**: To capture or redistribute value in a way that either maximizes profit (for producers/searchers) or aligns with overall network health (protocol designers).

**Descriptive**: MEV arises inevitably in non-trivial blockchains and shapes the economics of transaction execution.

**Worldview and Cause-and-Effect**: MEV is a product of decentralized systems granting temporary monopoly to block producers, producing secondary markets for ordering rights.

### Markets, Ecosystems, Regulatory Models, Revenue Strategies

**Markets & Ecosystems**:  
- MEV extraction forms its own sub-market within blockchains, with major actors such as Flashbots, MEV Protection RPCs, and protocol-level auction systems.

**Regulatory and Economic Models**:  
- Transaction fee markets, sealed-bid auctions, and PBS models define how value is distributed.
- Regulatory frameworks are emergent, focusing on transparency and user protection.

**Revenue Strategies**:  
- Direct extraction via transaction selection
- Auctioning blockspace and transaction ordering rights
- Selling MEV protection/private relays to users or searchers

### Work Mechanism: Summary and Phase-Based Lifecycle

**Concise Mechanism**:  
Block producers (directly or via relays/builders) obtain a set of pending transactions; by optimizing order and inclusion, they capture surplus value, often realized as profit from manipulated pricing or arbitrage.

**Phase-Based Workflow:**
1. **Preparation**: Transactions broadcast into mempool
2. **Detection**: Searchers analyze mempool for MEV setups
3. **Bundling**: Searchers craft transaction bundles for profit
4. **Auction/Relay**: Bundles submitted to builders/relays, who optimally slot and sequence
5. **Block Proposal**: Validators select block/package with optimal MEV value
6. **Validation/Execution**: Network validates block, transactions execute in finalized order, MEV is extracted and revenues distributed

### Preconditions, Inputs, Outputs, Outcomes, and Implications

- **Preconditions**: Existence of a mempool, block producer control of ordering, transaction fee mechanisms, and DeFi/smart contract applications with exploitable logic.
- **Inputs**: Pending transactions, network state, private searcher bundles.
- **Outputs**: Finalized blocks with profitable transaction arrangements, MEV revenue.
- **Immediate Outcomes**: Profit to block creators/searchers, possible user losses, fee escalations.
- **Long-term Impacts**: Incentivized centralization, evolving protocol designs, changes in market structure, and potential regulatory responses.

### Laws, Axioms, Theories, and Patterns

- **Information-Theoretic Law**: All non-trivial blockchains generate MEV; minimizing MEV comes at the expense of transaction expressibility or system utility.
- **Invariance Properties**: Certain MEV forms, especially arbitrage, are invariant under different transaction ordering mechanisms, implying limits to block-level mitigations.
- **Game-Theoretical Models**: MEV extraction is modeled as a game between rational agents (producers, searchers, users).

### Design Philosophy and Architectural Features

- **Design Philosophy**: Emphasis on minimizing harmful MEV, decentralizing extraction opportunities, and embedding fair and transparent mechanisms such as PBS.
- **Architectural Features**: Separation of block-building from proposing, introduction of relays/auctions, modular privacy/protection components, and cryptographic transaction concealment.

### Architectural Refactoring: Ideas and Techniques

- **Separation of Roles**: Introducing builder/proposer roles (as in PBS).
- **Modular Relays and Auctions**: Enable replaceability and competitiveness in bundle construction/selection.
- **Private Transaction Pools**: Secure private order flows to reduce front-running.
- **Protocol Upgrades**: Iterative, modular enhancements incorporating cryptographic privacy and auction-based mechanisms.

### Relevant Frameworks, Models, and Principles

- **Economic and Auction Theory Models**: Dynamic extraction rates, knapsack auctions, second-price/first-price auctions.
- **Information-Theory and Entropy Reduction**: Classify and quantify MEV by its impact on system disorder.
- **Dynamic Participation Models**: Incentivize both users and extractors by calibrating rewards dynamically.

### Origins, Evolution, and Trends

- **Origins**: Emerged concurrently with Ethereum and the proliferation of programmable DeFi apps, initially exploiting public mempools via PoW mining.
- **Evolution**: Transition from PoW to PoS prompted role diversification, expansion of MEV markets, and the creation of private relays and execution tickets.
- **Trends**: Sophistication of searchers/bots, use of PBS, cross-domain MEV, and future protocol-level MEV integration.

### Key Historical Events and Statistical Insights

- Flashbots' introduction streamlined MEV bundle markets, reducing network congestion but raising centralization questions.
- Pre-Merge Ethereum: $675 million extracted as MEV up to Sep 2022.
- DeFi Total Value Locked (TVL): Exceeded $109B in May 2024, MEV a persistent byproduct.
- Sandwich and arbitrage attacks make up over 99% of MEV identified between 2020-2022.

### Techniques, Protocols, and Algorithms

- **Transaction Reordering/Bundling**
- **Priority Gas and Sealed Bid Auctions**
- **Relay-based Block Proposals (e.g., Flashbots, PBS)**
- **Cryptographic Concealment and Randomized Ordering**
- **First-Come-First-Served Blockchains (e.g., Algorand), with latency optimization**

### Contradictions and Trade-Offs

- Centralization for efficiency vs. network decentralization
- Transparency (open mempools) vs. privacy/user protection
- Revenue maximization (for block producers) vs. fair user experience
- Performance (throughput, latency) vs. mitigation complexity

### Major Competitors and Concise Descriptions

1. **Flashbots**: Dominant auction-style private relay for efficient MEV capture; mitigates mempool-related attacks but centralizes order flow.
2. **MEV Protection RPCs**: Providers offering user protection against front-running/sandwiching, routing transactions via private paths.
3. **Proposer-Builder Separation (PBS)**: Protocol-level reforms separating block construction from proposal; foundation for open MEV markets.
4. **Execution Tickets**: Auctions block proposal rights at protocol level, aiming for equitable and native MEV redistribution.
5. **FairFlow**: Advanced protocol leveraging auctions and randomized ordering to mitigate MEV, enhance privacy/fairness.

### Comprehensive Competitor Analysis

| Name           | Operational Strategies                | Product Offerings           | Market Position           | Performance            |
|----------------|--------------------------------------|-----------------------------|---------------------------|------------------------|
| Flashbots      | Private relay, sealed-bid bundle auctions                          | Off-chain bidding; MEV extraction coordination | Market leader; sets industry standard | High adoption; major revenue generator |
| MEV-RPCs       | Filtering, private routing            | User-privacy endpoints      | Growing; privacy niche    | Effective for retail use|
| PBS            | Protocol-level separation, open roles | Auction-based block building| Increasing post-Merge adoption | robust, decentralized  |
| Execution Tickets | Native auctioning, on-chain MEV capture | Transferable tickets for block proposal | Emerging, protocol-integrated | Projected to improve fairness |
| FairFlow       | Multi-party cryptography, randomization| Privacy/Fairness layer      | Innovative, experimental  | Promising; not widespread |

### SWOT Analysis for Core Competitors

**Flashbots**:  
- Strengths: Widespread adoption, reduces network spam, efficient MEV extraction  
- Weaknesses: Centralization and censorship risk, relay trust assumptions  
- Opportunities: Expansion to cross-chain, protocol-level integration  
- Threats: Protocol innovations obviating need for relays; regulatory scrutiny

**MEV Protection RPCs**:  
- Strengths: Empowers users, privacy-centric  
- Weaknesses: Reduces MEV profit potential, limited by adoption  
- Opportunities: Partnerships, user growth  
- Threats: Adoption of native protocol mitigations, evolving attack vectors

**PBS**:  
- Strengths: Reinforces decentralization, native fairness  
- Weaknesses: Increased complexity, latency
- Opportunities: Widespread protocol upgrade adoption
- Threats: Stakeholder resistance, emergence of alternative models

**Execution Tickets**:  
- Strengths: Protocol-integrated, aligns incentives  
- Weaknesses: Market acceptance and pricing challenges  
- Opportunities: Deflationary pressure on native tokens, strengthened network security  
- Threats: Valuation instability, secondary market dominance

**FairFlow**:  
- Strengths: Advanced mitigation, privacy, and equity  
- Weaknesses: Complexity, potential learning curve  
- Opportunities: Research partnerships, ecosystem expansion  
- Threats: Adoption barriers, scalability tests

### Principles, Rules, Constraints, Vulnerabilities, and Challenges

- **Rules/Principles**: Temporary monopoly enables MEV; Transaction ordering power must be balanced for network welfare.
- **Constraints**: Protocol, economic, and computational limitations, user experience.
- **Vulnerabilities/Challenges**: Smart contract flaws, unencrypted mempools, detection complexity, regulatory uncertainty.

### Security, Troubleshooting, and Prevention

**Vulnerabilities**: Transaction ordering; front-running; relay attacks; contract exploits.

**Troubleshooting**: Network/transaction monitoring; detection tools for bundle/prioritization anomalies; audits.

**Mitigations**: Randomized order; proposer-builder separation; cryptographic privacy; auction-based allocation; emergency forks.

### Performance Bottlenecks and Optimization

Potential bottlenecks arise from auction delays, protocol-overhead, network latency, and computational bottlenecks in cryptographic operations. Empirical monitoring, protocol engineering, and modular upgrades support performance troubleshooting and optimization.

### Priorities, Use Cases, Pitfalls, and Best Practices

- **Priorities**: Reduce harmful MEV (e.g., front-running), preserve fair ordering, protocol transparency.
- **Use Cases**: Arbitrage, liquidations, sandwich attacks, priority bidding, cross-chain arbitrage.
- **Pitfalls**: User losses, market manipulation, centralization.
- **Best Practices**: Employ auctioned or randomized ordering, private relay protection, periodic audits.

### Relationships: Cause-and-Effect, Interdependencies, Cardinality, and Contradictions

**Cause-and-effect**:  
Block producer’s ordering power <-creates-> MEV opportunities <-motivates-> Searcher activity <-results in-> Profitable transaction reorderings and user/market impacts.

**Interdependency**:  
Transactions <-depend on-> Producers' order <-affects-> Searchers’ strategies <-influences-> Revenue and network health.

**Cardinality**:  
- 1:1 - Single searcher, single opportunity
- 1:M - Single block producer, many bundles
- M:N - Several searchers, competing bundles to multiple proposers/builders

**Contradictions**:  
Decentralization -contradicts-> Centralized MEV extraction  
Transparency -contradicts-> Privacy  
Throughput -contradicts-> Ordering fairness

### Non-trivial Problems and Potential Solutions

- Persistent centralization and role collusion
- Limited MEV mitigation at protocol layer
- Evolving forms of cross-chain and multi-block MEV attacks

**Potential Approaches**:  
- New economic designs and dynamic extraction models  
- Protocol-level privacy and auction mechanisms  
- Decentralized shared sequencers and cross-domain order validity

### Unsolved Research Topics

- Multi-block and cross-domain MEV quantification
- Privacy-preserving MEV mitigations compatible with composability
- Effective regulatory and legal frameworks for MEV markets

### Innovation Directions (Within/Across Domains)

- **Within-domain**: PBS, dynamic extraction rates, encrypted mempools, new auction designs.
- **Cross-domain**: Shared sequencing infrastructure, cross-chain arbitrage detection, federated relay networks.

### Ultimate Evolution of MEV Ecosystem

A composable, protocol-integrated MEV value chain across multiple blockchains featuring transparent, auction-based extraction, privacy protection, deflationary incentive alignment, and dynamic inter-chain revenue distribution—resulting in a fair, decentralized, and sustainable blockchain economy.

---

### Summary Table: Blockchain MEV

| Aspect                   | Description / Examples                                                                                            |
|--------------------------|-------------------------------------------------------------------------------------------------------------------|
| Purpose                  | To capture, optimize, and (ideally) fairly redistribute maximal value created by privilege in transaction ordering |
| Characteristics          | Dual role of profit and potential harm; driven by temporary monopoly; value-diverting and value-creating effects  |
| Core Elements            | Block producers, searchers, transactions, builders/relays, auctions/protocols                                      |
| Use Cases                | Arbitrage, sandwich attacks, liquidations, priority bidding, privacy services                                     |
| Evaluation Dimensions    | Revenue, network decentralization, fairness, performance, regulatory impact                                       |
| Key Competitors          | Flashbots, MEV Protection RPCs, PBS, Execution Tickets, FairFlow                                                 |
| Contradictions           | Centralization vs. decentralization, transparency vs. privacy, throughput vs. fairness                            |
| Trends                   | Private relays, protocol-level integrations, increased regulation, cross-domain MEV exploration                    |
| Security                 | Sensitive to transaction ordering attacks, exploits in contract logic, relay vulnerabilities                       |
| Open Problems            | Multi-block/cross-domain MEV, regulatory clarity, accurate detection tools                                        |

---

### Terminologies, Formulas, and Analogies

- **MEV**: Maximum value block producers can extract via transaction ordering manipulation.
- **Searcher**: Automated system identifying MEV opportunities.
- **Bundle**: A set of prioritized transactions submitted for inclusion.
- **Proposer-Builder Separation (PBS)**: Design separating block construction from block proposal for fairness.
- **Auction Mechanism**: Processes for blockspace allocation (e.g., priority gas auctions).
- **Execution Tickets**: Protocol-level transferable right to propose blocks and capture MEV.
- **Formula (MEV Calculation)**:  
  \\( MEV(P, s) = \max\{b(P, s') - b(P, s)\} \\)  
  where \\( b(P, s) \\) is a block producer’s balance pre-state, and \\( b(P, s') \\) post-state.
- **Analogy**: MEV as a financial trader front-running market orders; blockspace as an auctioned resource; transaction inclusion as packing a knapsack.

This exhaustive, MECE-compliant framework synthesizes the essential principles, structures, dynamics, and innovations of Blockchain MEV, integrating technical, economic, and strategic insights for comprehensive understanding and rigorous evaluation.

Bibliography
A. Averin & O. Averina. (2019). Review of Blockchain Technology Vulnerabilities and Blockchain-System Attacks. In 2019 International Multi-Conference on Industrial Engineering and Modern Technologies (FarEastCon). https://ieeexplore.ieee.org/document/8934243/

A Judmayer, N Stifter, P Schindler, & E Weippl. (2022). Estimating (miner) extractable value is hard, let’s go shopping! https://link.springer.com/chapter/10.1007/978-3-031-32415-4_6

Ahsan Umar & Muhammad Zeeshan Zafar. (2025). Blockchain Security: Vulnerabilities and Protective Measures. In World Journal of Advanced Research and Reviews. https://www.semanticscholar.org/paper/f99fdf112d898217ce4c4f6d640c1389df12eda9

Alan J. X. Guo. (2023). Invariance properties of maximal extractable value. https://www.semanticscholar.org/paper/a51060b6df194164bd6dd2e849df6938ece9c477

Astrid Carolina Ordoñez-Guerrero, Juan David Muñoz-Garzon, E. Villarreal, A. Bandi, & J. Hurtado. (2022). Blockchain Architectural Concerns: A Systematic Mapping Study. In 2022 IEEE 19th International Conference on Software Architecture Companion (ICSA-C). https://ieeexplore.ieee.org/document/9779841/

Atinkut Alamirrewm & Desalegn Tegabu. (2011). An Introduction to Health Informatics Terminologies. https://www.semanticscholar.org/paper/21ce4afc62f1204dcdfbf74355e452ba7308bdb5

Ayman Alkhalifah, Alex Ng, A. Kayes, Jabed Chowdhury, M. Alazab, & P. Watters. (2019). A Taxonomy of Blockchain Threats and Vulnerabilities. In Blockchain for Cybersecurity and Privacy. http://www.preprints.org/manuscript/201909.0117/v1

B Acilan, A Constantinescu, & L Heimbach. (2025). Transaction Fee Market Design for Parallel Execution. https://arxiv.org/abs/2502.11964

B Mazorra, M Reynolds, & V Daza. (2022). Price of mev: towards a game theoretical approach to mev. https://dl.acm.org/doi/abs/10.1145/3560832.3563433

B Öz, F Rezabek, J Gebele, & F Hoops. (2024). A study of mev extraction techniques on a first-come-first-served blockchain. https://dl.acm.org/doi/abs/10.1145/3605098.3635990

B Pillai. (2023). Blockchain MEV minimisation solution with price guarantee reward. In Authorea Preprints. https://www.techrxiv.org/doi/full/10.36227/techrxiv.21345306

B Weintraub, CF Torres, & C Nita-Rotaru. (2022). A flash (bot) in the pan: measuring maximal extractable value in private pools. https://dl.acm.org/doi/abs/10.1145/3517745.3561448

BS Banaei. (2023). Response to Blockchain Transaction Ordering as Market Manipulation. In Ohio St. Tech. LJ. https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/isjlpsoc20&section=6

BS Wolley. (2024). Analyzing Ethereum Block Builders: Clustering Strategies and Profitability in the MEV-Boost Ecosystem. https://repozitorij.uni-lj.si/IzpisGradiva.php?id=164136

Burak Öz, Benjamin Kraner, Nicoló Vallarano, B. Kruger, F. Matthes, & C. Tessone. (2023). Time Moves Faster When There is Nothing You Anticipate: The Role of Time in MEV Rewards. In Proceedings of the 2023 Workshop on Decentralized Finance and Security. https://arxiv.org/abs/2307.05814

Burak Öz, Jonas Gebele, Parshant Singh, Filip Rezabek, & Florian Matthes. (2024). Playing the MEV Game on a First-Come-First-Served Blockchain. In 2024 IEEE International Conference on Blockchain and Cryptocurrency (ICBC). https://www.semanticscholar.org/paper/af6ba40224a8ec991d5b577e2fb09f9ff79c2572

C McMenamin. (2023). Sok: Cross-domain mev. In arXiv. https://arxiv.org/abs/2308.04159

Caixiang Fan, Sara Ghaemi, Hamzeh Khazaei, & P. Musílek. (2020). Performance Evaluation of Blockchain Systems: A Systematic Survey. In IEEE Access. https://ieeexplore.ieee.org/document/9129732/

Chang Liu. (2023). Trading Security Designs Based on Blockchain Techniques. In BCP Business &amp; Management. https://bcpublication.org/index.php/BM/article/view/4837

Ciaran Hughes. (2023). Reducing Disorder: An Information-Theory Formulation of MEV. In ArXiv. https://www.semanticscholar.org/paper/ba9bc9d346b0e75336f48f2c4eea648761c3d1c2

D Ilisei. (2024). Analyzing the Role of Bridges in Cross-Chain MEV Extraction. https://wwwmatthes.in.tum.de/file/8o5tgvhfgln4/Sebis-Public-Website/-/Master-s-Thesis-Danut-Ilisei/Master_s_Thesis_Danut_Ilisei.pdf

D. Malkhi & Pawel Szalachowski. (2022). Maximal Extractable Value (MEV) Protection on a DAG. In International Conference on Blockchain Economics, Security and Protocols. https://arxiv.org/abs/2208.00940

D Mancino, A Leporati, & M Viviani. (2023). Exploiting ethereum after “the merge”: The interplay between pos and mev strategies. https://boa.unimib.it/handle/10281/440738

Daojing He, Rui Wu, Xinji Li, Sammy Chan, & M. Guizani. (2023). Detection of Vulnerabilities of Blockchain Smart Contracts. In IEEE Internet of Things Journal. https://ieeexplore.ieee.org/document/10034747/

Davide Mancino, Alberto Leporati, Marco Viviani, & Giovanni Denaro. (2024). A Role and Reward Analysis in Off-chain Mechanisms for Executing MEV Strategies in Ethereum Proof-of-Stake. In Distributed Ledger Technologies: Research and Practice. https://dl.acm.org/doi/10.1145/3672405

Dev Churiwala & B. Krishnamachari. (2022). CoMMA Protocol: Towards Complete Mitigation of Maximal Extractable Value (MEV) Attacks. In 2023 Fifth International Conference on Blockchain Computing and Applications (BCCA). https://ieeexplore.ieee.org/document/10338932/

Dipankar Sarkar. (2023). FairFlow Protocol: Equitable Maximal Extractable Value (MEV) mitigation in Ethereum. In ArXiv. https://arxiv.org/abs/2312.12654

E Wen, Z Deng, Y Mo, Y Zhou, & X Shi. (2025). RL-BES: optimizing strategies using reinforcement learning for blockchain economic security. In Blockchain. https://pdf.elspublishing.com/paper/journal/open/BC/2025/blockchain20250005.pdf

E. Zamani, Ying He, & M.L.F. Phillips. (2018). On the Security Risks of the Blockchain. In Journal of Computer Information Systems. https://www.tandfonline.com/doi/full/10.1080/08874417.2018.1538709

F Yusuf, R Widayanti, & SR Putri. (2025). A Comprehensive Framework for Enhancing Blockchain Security and Privacy. https://journal.pandawan.id/b-front/article/view/716

H Materwala, SM Naik, A Taha, & TA Abed. (2024). Maximal Extractable Value in Decentralized Finance: Taxonomy, Detection, and Mitigation. https://arxiv.org/abs/2411.03327

Heesang Kim & Dohoon Kim. (2024). Methodological Advancements in Standardizing Blockchain Assessment. In IEEE Access. https://ieeexplore.ieee.org/document/10458083/

Holger Krahn & Bernhard Rumpe. (2014). Techniques Enabling Generator Refactoring. In ArXiv. https://www.semanticscholar.org/paper/b61f2cd166737352edece8b793819801c9baf67a

I Yitmen, S Alizadehsalehi, & ME Akiner. (2023). Integration of digital twins, blockchain and ai in metaverse: Enabling technologies and challenges. https://www.taylorfrancis.com/chapters/edit/10.1201/9781003230199-3/integration-digital-twins-blockchain-ai-metaverse-ibrahim-yitmen-sepehr-alizadehsalehi-muhammed-ernur-akiner-ilknur-akiner

J Bormet, S Faust, H Othman, & Z Qu. (2024). BEAT-MEV: Epochless Approach to Batched Threshold Encryption for MEV Prevention. In Cryptology ePrint Archive. https://eprint.iacr.org/2024/1533

J Piet, V Nair, & S Subramanian. (2023). Mevade: An mev-resistant blockchain design. https://ieeexplore.ieee.org/abstract/document/10174966/

J Scharfman. (2024). Additional Cases and Trends in Cryptocurrency Fraud. https://link.springer.com/chapter/10.1007/978-3-031-60836-0_12

J Stearn. (2022). ’Cryptographic approaches to complete mempool privacy. In Flashbots Res. https://james-stearn.com/wp-content/uploads/2023/02/Cryptographic_Approaches_to_Complete_Mempool_Privacy-2.pdf

JJ Brachmann. (2024). Towards understanding Multi-block Maximal Extractable Value in Ethereum. https://repositum.tuwien.at/handle/20.500.12708/202226

Johan Hagelskjar Sjursen, W. Meng, & Wei-Yang Chiu. (2023). A Closer Look at Cross-Domain Maximal Extractable Value for Blockchain Decentralisation. In 2023 IEEE International Conference on Blockchain and Cryptocurrency (ICBC). https://ieeexplore.ieee.org/document/10174971/

Jonah Burian. (2024). The Future of MEV. In ArXiv. https://www.semanticscholar.org/paper/ca8c7a9cfd3c9191209c173232a906df2a94a8c4

K Qin, L Zhou, & A Gervais. (2022). Quantifying blockchain extractable value: How dark is the forest? https://ieeexplore.ieee.org/abstract/document/9833734/

Kshitij Kulkarni, Theo Diamandis, & Tarun Chitra. (2022). Towards a Theory of Maximal Extractable Value I: Constant Function Market Makers. In ArXiv. https://arxiv.org/abs/2207.11835

L Chen, L Xu, Z Gao, & AI Sunny. (2024). A game theoretical analysis of non-linear blockchain system. https://dl.acm.org/doi/abs/10.1145/3607195

M Bahrani, P Garimidi, & T Roughgarden. (2024). Transaction fee mechanism design in a post-mev world. In Cryptology ePrint Archive. https://eprint.iacr.org/2024/331

M Bartoletti & R Marchesin. (2024). Secure compilation of rich smart contracts on poor UTXO blockchains. https://ieeexplore.ieee.org/abstract/document/10629031/

M Lomeña-Gelis. (2015). A meta-evaluation of sustainable land management Initiatives in Senegal. https://upcommons.upc.edu/handle/2117/95787

Massimo Bartoletti & R. Zunino. (2023). A theoretical basis for MEV. https://www.semanticscholar.org/paper/519eff3fc11fbf7eb068dc884c0494225ebd67f2

MI Alnajjar, MS Kiraz, A Al-Bayatti, & S Kardas. (2024). Mitigating MEV attacks with a two-tiered architecture utilizing verifiable decryption. https://link.springer.com/article/10.1186/s13638-024-02390-4

Muhammad Nasir Mumtaz Bhutta, A. Khwaja, A. Nadeem, H. F. Ahmad, M. Khan, Moataz Hanif, H. Song, Majed A. Alshamari, & Yue Cao. (2021). A Survey on Blockchain Technology: Evolution, Architecture and Security. In IEEE Access. https://ieeexplore.ieee.org/document/9402747/

N Choi & H Kim. (2024). Decentralized exchange transaction analysis and maximal extractable value attack identification: Focusing on uniswap usdc3. In Electronics. https://www.mdpi.com/2079-9292/13/6/1098

N. S. Cherkas & A. Y. Batyuk. (2023). Maximal extractable value (mev) in blockchain networks and its impact on blockchain ecosystem. In Ukrainian Journal of Information Technology. https://www.semanticscholar.org/paper/ae16e2ccc5edf7d106bebda73afa266d5e683200

Nazarii Cherkas, A. Batyuk, & Maksym Arzubov. (2023). Maximal Extractable Value in Blockchains: Current Trends. In 2023 IEEE 18th International Conference on Computer Science and Information Technologies (CSIT). https://ieeexplore.ieee.org/document/10324040/

O Alpos, I Amores-Sesar, C Cachin, & M Yeo. (2023). Eating sandwiches: Modular and lightweight elimination of transaction reordering attacks. https://arxiv.org/abs/2307.02954

O. Zimmermann. (2015). Architectural Refactoring: A Task-Centric View on Software Evolution. In IEEE Software. https://ieeexplore.ieee.org/document/7057560/

Orestis Papageorgiou, Lasse Börtzler, Egor Ermolaev, Jyoti Kumari, & Johannes Sedlmeir. (2024). What Blocks My Blockchain’s Throughput? Developing a Generalizable Approach for Identifying Bottlenecks in Permissioned Blockchains. In ArXiv. https://arxiv.org/abs/2404.02930

P Braga, G Chionas, P Krysta, & S Leonardos. (2024). MEV Sharing with Dynamic Extraction Rates. https://dl.acm.org/doi/abs/10.1145/3689931.3694910

P Desai, Y Chaurasia, & S Gujar. (2025). Shapley Value-based Approach for Redistributing Revenue of Matchmaking of Private Transactions in Blockchains. In arXiv. https://arxiv.org/abs/2502.15420

P Janicot & A Vinyas. (2025). Private MEV Protection RPCs: Benchmark Stud. In arXiv. https://arxiv.org/abs/2505.19708

P Momeni, S Gorbunov, & B Zhang. (2022). Fairblock: Preventing blockchain front-running with minimal overheads. https://link.springer.com/chapter/10.1007/978-3-031-25538-0_14

P Poux, P De Filippi, & B Deffains. (1941). Maximal extractable value and the blockchain commons. In Available at SSRN 4198139. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4198139

Parshant Singh. (2023). Analytical and Empirical Evaluation of the Feasibility of MEV Extraction Techniques on the Algorand Blockchain. https://www.semanticscholar.org/paper/983f560a2d56b5a84aefb9fc440da48ef869ffc3

Pedro Braga, Georgios Chionas, Piotr Krysta, Stefanos Leonardos, G. Piliouras, & Carmine Ventre. (2024). Who gets the Maximal Extractable Value? A Dynamic Sharing Blockchain Mechanism. In Adaptive Agents and Multi-Agent Systems. https://doi.org/10.5555/3635637.3663097

R Humphry, P Avramovic, F Acevedo, & S Alkhair. (2024). Review of Maximal Extractable Value & Blockchain Oracles. https://www.fca.org.uk/publication/research-notes/research-note-review-and-maximal-extractable-value-blockchain-oracles.pdf

R Rochow, M Aicheler, G D’Auria, & E Gazis. (2019). XLS Deliverable D7. https://www.academia.edu/download/103277229/XLS_D7.1_Global-Integration-1.pdf

Robin Fritsch, Maria Ines Silva, A. Mamageishvili, Benjamin Livshits, & E. Felten. (2024). MEV Capture Through Time-Advantaged Arbitrage. In ArXiv. https://arxiv.org/abs/2410.10797

S Della Negra, D Jacquet, I Ribaud, TL Lai, & F Daubisse. (n.d.). ANDROMEDE (ANR 10-EQPX-23). http://in2p3.cnrs.fr/sites/institut_in2p3/files/page/2020-04/5-DELLANEGRA_0.pdf

S Ramos & J Ellul. (2023). The MEV Saga: Can Regulation Illuminate the Dark Forest? https://link.springer.com/chapter/10.1007/978-3-031-34985-0_19

S Wu, Z Li, H Zhou, X Luo, J Li, & H Wang. (2024). Following the “Thread”: Toward Finding Manipulatable Bottlenecks in Blockchain Clients. https://dl.acm.org/doi/abs/10.1145/3650212.3680372

S Wunderlich. (2023). Current State of MEV in the Ethereum Ecosystem. https://monami.hs-mittweida.de/frontdoor/index/index/docId/14643

S Yang, F Zhang, K Huang, X Chen, & Y Yang. (2022). Sok: Mev countermeasures: Theory and practice. https://arxiv.org/abs/2212.05111

S Yang, F Zhang, K Huang, X Chen, & Y Yang. (2024). SoK: MEV Countermeasures. https://dl.acm.org/doi/abs/10.1145/3689931.3694911

S Yang, K Nayak, & F Zhang. (2024). Decentralization of Ethereum’s Builder Market. In arXiv. https://arxiv.org/abs/2405.01329

Song Ling, Zhang Shaowei, & L. Zhimin. (2011). Reflects on traditional teaching methods of architecture design. In 2011 International Conference on Electric Technology and Civil Engineering (ICETCE). https://ieeexplore.ieee.org/document/5774684/

Surya Prasath, Anugrah Punnakkan, & Sanju Rajan. (2024). Understanding Methods of Top Maximal Extractable Value Searchers. In 2024 2nd International Conference on Sustainable Computing and Smart Systems (ICSCSS). https://ieeexplore.ieee.org/document/10624868/

SW Hassan, F Nawaz, & MZ Haq. (n.d.). ETSE, 2024. http://www.uow.edu.pk/pakturk/content/7th-Pak-Turk-International-Conference-Proceedings.pdf

T Chitra & K Kulkarni. (2022). Improving proof of stake economic security via MEV redistribution. https://dl.acm.org/doi/abs/10.1145/3560832.3564259

T Niedermayer. (2024). Detecting Bot Wallets on the Ethereum Blockchain. https://repositum.tuwien.at/handle/20.500.12708/198225

Tarun Chitra. (2023). Towards a Theory of Maximal Extractable Value II: Uncertainty. In ArXiv. https://arxiv.org/abs/2309.14201

Tianyang Chi, Ningyu He, Xiaohui Hu, & Haoyu Wang. (2024). Remeasuring the Arbitrage and Sandwich Attacks of Maximal Extractable Value in Ethereum. In ArXiv. https://arxiv.org/abs/2405.17944

Tuulikki Hakkarainen, Anatoli Colicev, & T. Pedersen. (2024). A perspective on three trade‐offs of blockchain technology for the global strategy of the MNC. In Global Strategy Journal. https://onlinelibrary.wiley.com/doi/10.1002/gsj.1509

V Gramlich, D Jelito, & J Sedlmeir. (2024). Maximal extractable value: Current understanding, categorization, and open research questions. In Electronic Markets. https://link.springer.com/article/10.1007/s12525-024-00727-x

Vijay Mohan & Peyman Khezr. (2024). Blockchains, MEV and the knapsack problem: a primer. https://www.semanticscholar.org/paper/1bdf8cc87efdb16c9af8356a7d76fe2b718e727c

Weiwei Pang, Kai Wei, Yihui Zhang, Chunyu Jiang, Yang Cheng, Qi Zhang, Bin Liu, Lifeng Zhang, Tingting Liu, & Yinqian Wu. (2023). Research on Assessment System for Blockchain. In 2023 IEEE 22nd International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom). https://ieeexplore.ieee.org/document/10538844/

X Xiong, Z Wang, T Cui, & W Knottenbelt. (2023). Market Misconduct in Decentralized Finance (DeFi): Analysis, Regulatory Challenges and Policy Implications. https://arxiv.org/abs/2311.17715

Xinyu Liang. (2025). Security Challenges and Defense Strategies in Blockchain Systems. In Applied and Computational Engineering. https://www.ewadirect.com/proceedings/ace/article/view/21087

Y Chaurasia, P Desai, & S Gujar. (2024). MEV Ecosystem Evolution From Ethereum 1.0. In arXiv. https://arxiv.org/abs/2406.13585

Y Ji & J Grimmelmann. (2024). Regulatory Implications of MEV Mitigations. https://link.springer.com/chapter/10.1007/978-3-031-69231-4_21

Y Zhang, G Wang, P Li, W Gu, & H Chen. (2025). FRACE: Front-Running Attack Classification on Ethereum using Ensemble Learning. In The Computer Journal. https://academic.oup.com/comjnl/advance-article-abstract/doi/10.1093/comjnl/bxaf027/8108227

Yevhen Kononet. (2018). The Blockchain Technology as a Necessary Tool between Contractual Relationships. In International Scientific Days 2018. Towards Productive, Sustainable and Resilient Global Agriculture and Food Systems: Proceedings. http://www.slpk.sk/eldo/2018/dl/9788075981806/files/10/s10p07.html

Z Alipanahloo, AS Hafid, & K Zhang. (2024a). Maximal extractable value mitigation approaches in ethereum and layer-2 chains: A comprehensive survey. In arXiv. https://arxiv.org/abs/2407.19572

Z Alipanahloo, AS Hafid, & K Zhang. (2024b). Maximum Extractable Value (MEV) mitigation approaches in ethereum and layer-2 chains: A comprehensive survey. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10787131/

Z Stucke & T Constantinides. (2022). Simulation of front-running attacks and privacy mitigations in Ethereum blockchain. https://research-information.bris.ac.uk/en/publications/simulation-of-front-running-attacks-and-privacy-mitigations-in-et

Z Yao, F Huang, Y Li, W Duan, P Qian, & N Yang. (2025). Mecon: A GNN-based graph classification framework for MEV activity detection. https://www.sciencedirect.com/science/article/pii/S0957417425001083



Generated by Liner
https://getliner.com/search/s/5926611/t/85558499