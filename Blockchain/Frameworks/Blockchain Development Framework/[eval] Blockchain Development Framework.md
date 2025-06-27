'Blockchain Development Framework'. Requirements: 1. Ensure MECE compliance. 2. Group related ideas into clear, hierarchical sections to avoid lengthy paragraphs. 3. Use numbered lists for clarity when suitable. 4. Clarify phase-based core evaluation dimensions, their corresponding measurements, evaluation conclusions, and supporting evidence. 5. Conduct a comprehensive competitor (including the one being searched at present) analysis of operational strategies, product offerings, market position, and performance metrics. 6. Conduct a SWOT analysis for every competitor.

Fri Jun 27 2025

### 1. Main Components of a Blockchain Development Framework

1.1 Network Layer  
   1.1.1 Peer-to-Peer Nodes: A decentralized set of nodes that communicate directly to propagate transactions and blocks without central coordination.  
   1.1.2 Data Propagation: Gossip or broadcast protocols ensuring reliable block and transaction distribution across peers.

1.2 Distributed Ledger  
   1.2.1 Immutable Ledger: An append-only chain of blocks that records all validated transactions in chronological order.  
   1.2.2 State Database: A key-value store maintaining the latest application state for quick queries.

1.3 Consensus Mechanism  
   1.3.1 Agreement Protocols: Algorithms (e.g., PoW, PoS, BFT) that enable network-wide agreement on block validity.  
   1.3.2 Pluggable Consensus: Modular design allowing selection or replacement of consensus engines to suit trust models.

1.4 Smart Contracts  
   1.4.1 Chaincode/Contracts: Self-executing programs encapsulating business logic and running in isolated environments.  
   1.4.2 Endorsement Policies: Rules specifying which peers must approve a transaction before it can be committed.

1.5 Execution Environment (Virtual Machine)  
   1.5.1 Runtime Support: Virtual machines (e.g., EVM, WASM) that execute smart contract code in a deterministic manner.  
   1.5.2 Language Agnosticism: Ability to support multiple programming languages through containerized or VM-based execution.

1.6 Cryptographic Security  
   1.6.1 Hash Functions: Ensure data integrity and link blocks cryptographically.  
   1.6.2 Digital Signatures: Authenticate transaction origin and prevent forgery.

1.7 Application Layer  
   1.7.1 Decentralized Applications (DApps): User-facing interfaces interacting with smart contracts.  
   1.7.2 APIs and SDKs: Libraries and tools facilitating integration with external systems and front-ends.

1.8 Auxiliary Components  
   1.8.1 Oracles: Services providing real-world data to smart contracts in a trust-minimized manner.  
   1.8.2 Wallets and Key Management: Tools for secure storage and management of private keys and assets.  

---

### 2. Phases of the Blockchain Development Framework

#### 2.1 Ideation and Feasibility Analysis  
Core Dimensions: Project definition, use-case suitability, stakeholder alignment, technical, economic, and market feasibility.  
Measurements:  
  1. Concept documents and white papers outlining objectives and target audience.  
  2. SWOT and PEST analyses evaluating strategic fit and external factors.  
  3. Cost–benefit and ROI projections for development and maintenance.  
Evaluation Conclusion: This phase validates whether blockchain adds unique value beyond conventional systems, ensuring projects proceed only when blockchain’s decentralization, transparency, or immutability are indispensable.  

Supporting Evidence: Feasibility frameworks reduce the risk of misapplication, guiding practitioners to avoid unnecessary blockchain deployments.

#### 2.2 Design and Architecture  
Core Dimensions: Network topology, consensus selection, security model, data schema, smart contract architecture, and interface design.  
Measurements:  
  1. Architectural blueprints and component diagrams.  
  2. Security compliance checklists covering encryption, identity management, and access control.  
  3. Prototype validation tests verifying modular consensus and endorsement logic.  
Evaluation Conclusion: A well-defined architecture ensures system resilience, abiding by the chosen trust model and performance requirements, while preventing costly redesigns during implementation.  

Supporting Evidence: Modular frameworks like Hyperledger Fabric demonstrate that pluggable consensus and endorsement policies directly impact security and throughput.

#### 2.3 Development and Implementation  
Core Dimensions: Code correctness, smart contract logic fidelity, integration robustness, test coverage, and performance under load.  
Measurements:  
  1. Code reviews and static analysis metrics, including cyclomatic complexity.  
  2. Unit, integration, and system testing reports with pass/fail rates.  
  3. Performance benchmarks capturing throughput (TPS) and latency under varying workloads.  
Evaluation Conclusion: Rigorous testing and iterative code validation confirm that the system meets functional and non-functional requirements, delivering expected performance and security before deployment.  

Supporting Evidence: Empirical studies show that chaincode performance and consensus configurations significantly affect transaction throughput and latency.

#### 2.4 Deployment and Network Launch  
Core Dimensions: Environment provisioning, node deployment accuracy, initial network health, documentation, and user onboarding.  
Measurements:  
  1. Deployment checklists ensuring correct configuration of peers, orderers, and membership services.  
  2. Post-deployment stability tests measuring error rates and resource consumption.  
  3. User training feedback and documentation completeness surveys.  
Evaluation Conclusion: This phase ensures a controlled, repeatable network launch, reducing operational risks and enabling smooth user adoption.  

Supporting Evidence: Controlled pilot deployments and rollback mechanisms mitigate downtime during network genesis and upgrades.

#### 2.5 Maintenance and Upgrades  
Core Dimensions: Network monitoring, incident response, feature enhancements, scalability, and compliance updates.  
Measurements:  
  1. Real-time performance dashboards (TPS, latency, resource metrics).  
  2. Incident and bug tracking logs with resolution SLAs.  
  3. Audit and compliance reports ensuring regulatory adherence.  
Evaluation Conclusion: Continuous monitoring and timely patching sustain network reliability, scale operations, and adapt to evolving requirements, safeguarding long-term viability.  

Supporting Evidence: Performance measurement frameworks like BlockMeter enable proactive detection of throughput degradations and inform optimization strategies.

---

### 3. Competitive Landscape Overview

Based on industry surveys and market data, the leading blockchain development frameworks include Ethereum, Hyperledger Fabric, R3 Corda, Polkadot (Substrate), Avalanche, Solana, Cardano, Cosmos (Tendermint), and Algorand. Each platform distinguishes itself through unique operational strategies, product offerings, market position, and performance characteristics.

---

### 4. Competitor Analyses

#### 4.1 Ethereum  
Operational Strategy: Public, permissionless network evolving from Proof of Work to Proof of Stake to improve scalability and energy efficiency.  
Product Offerings: EVM, Solidity, extensive DeFi and NFT tooling, Layer 2 integration (Optimism, Arbitrum).  
Market Position: Largest smart contract ecosystem, second-highest market capitalization among cryptocurrencies.  
Performance Metrics: Historically ~15 TPS for PoW, transitioning to anticipated hundreds of TPS with PoS and sharding.  

SWOT Analysis:   
  • Strengths: Largest developer community; mature DeFi and NFT ecosystems.  
  • Weaknesses: Legacy scalability and high transaction costs.  
  • Opportunities: Layer 2 rollups and sharding; institutional adoption.  
  • Threats: Competing high-performance chains; regulatory scrutiny.

#### 4.2 Hyperledger Fabric  
Operational Strategy: Permissioned, modular design enabling enterprise consortia with customizable consensus and privacy via channels.  
Product Offerings: Chaincode support in Go, Java, Node.js; Kafka/Raft ordering; Membership Service Provider.  
Market Position: Leading enterprise blockchain framework with adoption by over 400 production networks.  
Performance Metrics: >3500 TPS in optimal configurations with sub-second latency; performance tunable via block size and endorsement policy.  

SWOT Analysis:  
  • Strengths: High throughput; enterprise-grade privacy; pluggable consensus.  
  • Weaknesses: Complex setup; resource-intensive.  
  • Opportunities: Supply chain digitization; cross-industry consortia.  
  • Threats: Alternative DLT platforms targeting enterprises.

#### 4.3 R3 Corda  
Operational Strategy: Permissioned DLT focusing on regulated financial workflows, leveraging legal-state smart contracts and privacy by design.  
Product Offerings: Ricardian contracts, flows API, network map services for peer discovery.  
Market Position: Dominant in tokenized real-world asset markets with over $10 billion on-chain and 1 million daily transactions.  
Performance Metrics: Processes thousands of transactions per second in consortium settings; low latency for bilateral transactions.  

SWOT Analysis:  
  • Strengths: Financial sector focus; strong privacy; legal integration.  
  • Weaknesses: Limited to permissioned consortia; narrow use cases.  
  • Opportunities: Expansion into supply chain finance; central bank digital currencies.  
  • Threats: Regulatory changes; shifting tech standards.

#### 4.4 Polkadot (Substrate)  
Operational Strategy: Heterogeneous multi-chain with a Relay Chain securing parachains, employing NPoS and hybrid consensus (BABE + GRANDPA).  
Product Offerings: Substrate framework for custom chains, parachain slots via on-chain governance and candle auctions.  
Market Position: Top 20 cryptocurrency by market cap; viewed as long-term interoperability solution.  
Performance Metrics: ~6 second block times; scalability via parachains; limited slots (max 100) constrain expansion.  

SWOT Analysis:  
  • Strengths: Interoperability; pooled security; forkless upgrades.  
  • Weaknesses: High stake requirement for validators; slot scarcity.  
  • Opportunities: Cross-chain DeFi; governance-driven evolution.  
  • Threats: Governance centralization; competitor multi-chain solutions.

#### 4.5 Avalanche  
Operational Strategy: Permissionless platform using Snowman consensus variant for high throughput and sub-second finality.  
Product Offerings: Customizable subnets, Unterstützung for EVM, AvalancheGo client.  
Market Position: Top 20 cryptocurrency; favored for DeFi and enterprise subnets.  
Performance Metrics: Sub-second finality; thousands of TPS; energy-efficient PoS.  

SWOT Analysis:  
  • Strengths: Rapid finality; EVM compatibility; subnet customization.  
  • Weaknesses: Emerging ecosystem; complexity in subnet management.  
  • Opportunities: Enterprise blockchain deployment; cross-chain bridges.  
  • Threats: Competition from Solana and Polkadot in high-performance niches.

#### 4.6 Solana  
Operational Strategy: Public PoH+PoS network optimized for low latency and high throughput.  
Product Offerings: Rust, C, C++ smart contract development; liquid staking; NFT marketplaces.  
Market Position: Top 10 cryptocurrency by market cap; leading in NFT and DeFi transaction volumes.  
Performance Metrics: Tens of thousands TPS under ideal conditions; ~400 ms block times.  

SWOT Analysis:  
  • Strengths: Exceptional throughput; low fees; thriving DeFi/NFT apps.  
  • Weaknesses: Hardware requirements; network outages.  
  • Opportunities: Gaming and microtransaction markets.  
  • Threats: Reliability concerns; rising competition.

#### 4.7 Cardano  
Operational Strategy: Research-driven PoS with formal verification and a layered architecture.  
Product Offerings: Plutus smart contract framework; on-chain governance (Voltaire).  
Market Position: Top 15 cryptocurrency; academic-focused ecosystem.  
Performance Metrics: Hundreds of TPS; energy-efficient PoS; formal audits.  

SWOT Analysis:  
  • Strengths: Security via formal methods; sustainable PoS.  
  • Weaknesses: Slower dApp growth; complex development tools.  
  • Opportunities: Identity management; academic credentialing.  
  • Threats: Faster-moving ecosystems like Ethereum and Solana.

#### 4.8 Cosmos (Tendermint)  
Operational Strategy: “Internet of Blockchains” using IBC for interoperability, backed by high-performance BFT consensus.  
Product Offerings: Cosmos SDK, Tendermint Core, IBC protocol.  
Market Position: Top 30 cryptocurrency; strong position in cross-chain infrastructure.  
Performance Metrics: Thousands TPS; sub-second block times; predictable finality.  

SWOT Analysis:  
  • Strengths: Inter-blockchain communication; modular SDK.  
  • Weaknesses: Complexity of IBC implementation.  
  • Opportunities: Cross-chain DeFi; infrastructure services.  
  • Threats: Alternative cross-chain solutions and security risks.

#### 4.9 Algorand  
Operational Strategy: Pure PoS with immediate finality, focus on decentralization and efficiency.  
Product Offerings: Smart contract platforms (ASC1), tokenization toolkit, atomic transfers, various wallets (Algorand Core, Pera).  
Market Position: Mid-range market cap; growing DeFi and stablecoin use cases.  
Performance Metrics: Instant finality; ~1,000 TPS; low energy consumption.  

SWOT Analysis:  
  • Strengths: Energy-efficient; instant finality; strong governance.  
  • Weaknesses: Smaller ecosystem; lesser developer engagement.  
  • Opportunities: Tokenization of real-world assets; institutional adoption.  
  • Threats: Competition from Ethereum 2.0 and Solana in DeFi.

#### 4.10 Quorum  
Operational Strategy: Permissioned enterprise Ethereum variant with voting-based consensus.  
Product Offerings: Public/private transaction support, high-performance ledger, integration with enterprise systems.  
Market Position: Niche market in finance and private consortia; moderate adoption.  
Performance Metrics: Hundreds to thousands TPS depending on consensus and network size.  

SWOT Analysis:  
  • Strengths: Familiar Ethereum toolset; privacy enhancements.  
  • Weaknesses: Dependent on enterprise demand; less public network activity.  
  • Opportunities: Regulatory-compliant financial networks.  
  • Threats: Evolving enterprise blockchain offerings from big tech.

---

**Conclusion**  
This MECE-compliant framework outlines the essential components, phased evaluation dimensions, and a structured competitor landscape with SWOT analyses, enabling organizations to systematically plan, assess, and select appropriate blockchain development frameworks for their specific use cases.

Bibliography
A. Averin & O. Averina. (2020). Review of Blockchain Frameworks and Platforms. In 2020 International Multi-Conference on Industrial Engineering and Modern Technologies (FarEastCon). https://ieeexplore.ieee.org/document/9271217/

A Castro Jiménez. (2021). Development of a distributed application over R3 Corda. https://upcommons.upc.edu/handle/2117/357130

A Complete Guide to Blockchain Development Process | LeewayHertz. (n.d.). https://www.leewayhertz.com/guide-to-blockchain-development-process/

A Comprehensive Hyperledger Fabric Performance Evaluation based on ... (n.d.). https://arxiv.org/html/2502.10509v1

A Framework to Evaluate Readiness for Blockchain Technology ... (n.d.). https://www.researchgate.net/publication/361142318_A_Framework_to_Evaluate_Readiness_for_Blockchain_Technology_Implementation

A. Langer. (2020). Blockchain Analysis and Design. https://www.semanticscholar.org/paper/15af42f1cd490a1d156a893a4daa07a314255806

A Mahboub-Ahari & S Hajebrahimi. (2016). EOS imaging versus current radiography: A health technology assessment study. https://pmc.ncbi.nlm.nih.gov/articles/PMC4898869/

A Mannberg, J Hendrikx, & J Johnson. (2021). Risky positioning–social aspirations and risk-taking behaviour in avalanche terrain. In Leisure Studies. https://www.tandfonline.com/doi/abs/10.1080/02614367.2020.1831046

A Rehman, T Qunyi, HR Sharif, & SA Korma. (2021). Biopolymer based nanoemulsion delivery system: An effective approach to boost the antioxidant potential of essential oil in food products. https://www.sciencedirect.com/science/article/pii/S2666893921000505

A step-by-step framework for evaluating crypto projects. (2022). https://cointelegraph.com/news/a-step-by-step-framework-to-evaluating-crypto-projects

Ahaan Dabholkar & V. Saraswat. (2019). Ripping the Fabric: Attacks and Mitigations on Hyperledger Fabric. In International Conference on Applications and Techniques in Information Security. https://link.springer.com/chapter/10.1007/978-981-15-0871-4_24

Alex De Vries. (2022). Cryptocurrencies on the road to sustainability: Ethereum paving the way for Bitcoin. In Patterns. https://linkinghub.elsevier.com/retrieve/pii/S2666389922002653

Algorand transaction performance - Nodely. (2023). https://nodely.io/blog/algorand-transaction-performance/

Answering your questions on Hyperledger Fabric performance and scale - IBM. (2019). https://www.ibm.com/think/insights/answering-your-questions-on-hyperledger-fabric-performance-and-scale

Ashok U. Mallya & Munindar P. Singh. (2005). Incorporating Commitment Protocols into Tropos. In International Workshop on Agent-Oriented Software Engineering. https://link.springer.com/chapter/10.1007/11752660_6

B Buchholz, L Ménard, & D Mayer. (2020). Avalanche server: always up-to-date market overview of PV modules on the Internet www. ret-market. org. https://www.taylorfrancis.com/chapters/edit/10.4324/9781315074405-213/avalanche-server-always-date-market-overview-pv-modules-internet-www-ret-market-org-britta-buchholz-lionel-m%C3%A9nard-didier-mayer-murray-cameron-amy-francis-bernard-mcnelis

Blockchain components and concepts - ScienceDirect.com. (n.d.). https://www.sciencedirect.com/science/article/pii/S0065245820300747

Blockchain Development Life Cycle - LCX. (2023). https://www.lcx.com/blockchain-development-life-cycle/

Blockchain Frameworks: How to Choose Yours? - Tatum.io. (2023). https://tatum.io/blog/blockchain-frameworks

Blockchain SWOT analysis Unleashing the Power of ... - FasterCapital. (2025). https://fastercapital.com/content/Blockchain-SWOT-analysis-Unleashing-the-Power-of-Blockchain--A-SWOT-Analysis.html

Business Strategy — Case Study 001: TEZOS Part 1/5 - Medium. (2023). https://medium.com/@sdante/business-strategy-case-study-001-tezos-part-1-5-3bd6f43633ff

C. Bowman & D. Asch. (1987). Making the strategy operational. https://www.semanticscholar.org/paper/b79f0e6f21798fea53aba3ab30537b6be1b3068a

Carlos Melo, Felipe Oliveira, J. Dantas, J. Araujo, Paulo Pereira, Ronierison Maciel, & P. Maciel. (2022). Performance and availability evaluation of the blockchain platform hyperledger fabric. In The Journal of Supercomputing. https://link.springer.com/article/10.1007/s11227-022-04361-2

Complete Analysis of Cosmos (ATOM)/Functioning, Use Cases, and Potential. (n.d.). https://cointobuy.io/cosmos-crypto/

D. Bernhardt, Kostas Koufopoulos, & G. Trigilia. (2021). Separating equilibria, underpricing and security design. In Journal of Financial Economics. https://linkinghub.elsevier.com/retrieve/pii/S0304405X21004062

D. Broome. (1985). The Earth Observing System - A multidisciplinary system for the long-term acquisition of earth science data from space. https://www.semanticscholar.org/paper/6de30392402159cebb8bc8304792480c12ac576b

D. Carstens & Gary L. Richardson. (2019). Performance Metrics. In Encyclopedia of Biometrics. https://link.springer.com/rwe/10.1007/978-0-387-73003-5_2380

D Haryadi, AR Hakim, DMU Atmaja, & SN Yutia. (2022). Implementation of support vector regression for polkadot cryptocurrency price prediction. https://joiv.org/index.php/joiv/article/view/945

D. Maesa & P. Mori. (2020). Blockchain 3.0 applications survey. In J. Parallel Distributed Comput. https://linkinghub.elsevier.com/retrieve/pii/S0743731519308664

D Pavithran, K Shaalan, JN Al-Karaki, & A Gawanmeh. (2020). Towards building a blockchain framework for IoT. In Cluster Computing. https://link.springer.com/article/10.1007/s10586-020-03059-5

D. Peleg & A. Wool. (1995). The Availability of Quorum Systems. In Inf. Comput. https://linkinghub.elsevier.com/retrieve/pii/S0890540185711698

Daniele Scarpi. (2020). Comparison of the Distribution Channels. https://www.semanticscholar.org/paper/08b086f77a8b1ac135fff687d6e92042a29fe40b

Danijel Radulović. (2021). IMPLEMENTACIJA KONCEPTA DECENTRALIZOVANIH FINANSIJA ZASNOVANA NA PRIMENI POLKADOT ARHITEKTURE. In Zbornik radova Fakulteta tehničkih nauka u Novom Sadu. https://www.semanticscholar.org/paper/ae14c271ee7f3bb1faef0487675dae40134154bb

Dennis P. Nolan & Eric T. Anderson. (2015). What Is Operational Excellence (OE). https://linkinghub.elsevier.com/retrieve/pii/B9780128027882000014

Devanshu Tyagi, Soumi Ghosh, A. Rana, & Vineet Kansal. (2020). A Comparative Analysis of Potential Factors and Impacts that Affect Blockchain Technology in Software: Based Applications. In 2020 9th International Conference System Modeling and Advancement in Research Trends (SMART). https://ieeexplore.ieee.org/document/9337156/

Donald Beaver. (2004). Secure multiparty protocols and zero-knowledge proof systems tolerating a faulty minority. In Journal of Cryptology. https://link.springer.com/article/10.1007/BF00196771

Dušan Morháč, Viktor Valaštín, & Kristián Košfál. (2022). Sharing Fungible Assets Across Polkadot Paraverse. In 2022 International Conference on Electrical, Computer and Energy Technologies (ICECET). https://ieeexplore.ieee.org/document/9872938/

Elli Androulaki, Artem Barger, V. Bortnikov, C. Cachin, K. Christidis, Angelo De Caro, David Enyeart, Christopher Ferris, Gennady Laventman, Yacov Manevich, S. Muralidharan, Chet Murthy, Binh Nguyen, Manish Sethi, Gari Singh, Keith A. Smith, A. Sorniotti, C. Stathakopoulou, M. Vukolic, … Jason Yellick. (2018). Hyperledger fabric: a distributed operating system for permissioned blockchains. In Proceedings of the Thirteenth EuroSys Conference. https://dl.acm.org/doi/10.1145/3190508.3190538

EOS® Scorecard: Make Data Your Superpower - EOS Worldwide. (n.d.). https://www.eosworldwide.com/guest-blog/eos-scorecard-make-data-your-superpower

EOS ScorecardTM: Make Data Your Superpower - Ninety. (2025). https://www.ninety.io/eos/blog/eos-scorecard-make-data-your-superpower

EP Noman & DB Setyohadi. (2023). A survey of blockchain in governance: framework selection and future implementation in Indonesian government. In IAIC International Conference Series. https://www.aptikom-journal.id/conferenceseries/article/view/623

Ethereum Cryptocurrency – Marketplace - Google Cloud Console. (n.d.). https://console.cloud.google.com/marketplace/product/ethereum/crypto-ethereum-blockchain

Ethereum Foundation rolls out new treasury policy - Cointelegraph. (n.d.). https://cointelegraph.com/news/ethereum-foundation-new-treasury-policy-18-months-pivotal

Ethereum Foundation Unveils Conservative Treasury Strategy Amid Major R ... (n.d.). https://www.blockhead.co/2025/06/05/ethereum-foundation-unveils-conservative-treasury-strategy-amid-major-r-d-restructuring/

Ethereum Price Prediction, News, and Analysis (ETH) - MarketBeat. (n.d.). https://www.marketbeat.com/cryptocurrencies/ethereum/

Ethereum Price Today, ETH to USD Live Price, Market Cap & Chart. (n.d.). https://cointelegraph.com/ethereum-price

F Hosseinpouli Mamaghani & S Elahi. (2022). A framework to evaluate readiness for blockchain technology implementation. https://www.academia.edu/download/98857366/6.pdf

F Vlasov. (2025). Blockchain-based membership and incentive systems on Solana. https://www.theseus.fi/bitstream/handle/10024/890458/Vlasov_Fedor.pdf?sequence=2

Felix Lissåker & J. Sjöberg. (2019). Architecture Framework for Blockchain Implementation. https://www.semanticscholar.org/paper/c97472de51b0b5cacf85ecb4b32cd8d65ec1de28

GB Blocks. (2021). An Introduction to Solana. In no. December. https://i-invdn-com.akamaized.net/content/1f10f3c10b415718b94909eab6d10059.pdf

Growth Strategy and Future Prospects of Polkadot. (n.d.). https://canvasbusinessmodel.com/blogs/growth-strategy/polkadot-growth-strategy

H Liu, Y Mao, & X Li. (2025). An Empirical Analysis of EOS Blockchain: Architecture, Contract, and Security. In arXiv. https://arxiv.org/abs/2505.15051

H Mubarak Al‐Mubaraki & M Busler. (2010). Business incubators models of the USA and UK: A SWOT analysis. https://www.emerald.com/insight/content/doi/10.1108/20425961201000025/full/html

H. Sukhwani. (2019). Performance Modeling & Analysis of Hyperledger Fabric (Permissioned Blockchain Network). https://www.semanticscholar.org/paper/6baca8bc27d50f894627db94f53985a4ab96a3be

Hagar Meir, Artem Barger, & Yacov Manevich. (2019). Increasing concurrency in hyperledger fabric. In Proceedings of the 12th ACM International Conference on Systems and Storage. https://dl.acm.org/doi/10.1145/3319647.3325841

Hanaa Abbas, Maurantonio Caprolu, & R. D. Pietro. (2022). Analysis of Polkadot: Architecture, Internals, and Contradictions. In 2022 IEEE International Conference on Blockchain (Blockchain). https://ieeexplore.ieee.org/document/9881859/

Hermann. Simon. (2015). Price Positioning: High or Low. https://www.semanticscholar.org/paper/dad6e6419328497586339b767cb83e0bc8f56d43

HK Ramapriyan, J Behnke, & E Sofinowski. (2009). Evolution of the earth observing system (EOS) data and information system (EOSDIS). https://link.springer.com/chapter/10.1007/978-3-540-88264-0_5

Hongdan Han, Radha K. Shiwakoti, & Weifeng Chen. (2024). Unlocking enterprise blockchain adoption: A R3 Corda case study. In Journal of General Management. https://www.semanticscholar.org/paper/4558e84fe1f856da0ec619e018dc71eb1603b84e

Hyperledger Fabric in Blockchain - ChainCode Consulting LLP. (n.d.). https://chaincodeconsulting.com/insights/blog/hyperledger-fabric-in-blockchain-a-comprehensive-overview

I Muda, K Santosh, M Aarif, & L Natrayan. (2024). Innovative Blockchain Protocol for Enhancing Transaction Security and Integrity in Decentralized Financial Ecosystems. https://ieeexplore.ieee.org/abstract/document/10691288/

Ifteher Alom, M. Ferdous, & M. Chowdhury. (2022). BlockMeter: An Application Agnostic Performance Measurement Framework for Private Blockchain Platforms. In IEEE Transactions on Services Computing. https://ieeexplore.ieee.org/document/10183358/

Infn Laboratori. (1986). A Position Sensitive Parallel Plate Avalanche Counter. In Nuclear Electronics and Detection Technology. https://www.semanticscholar.org/paper/33f11cd037d066c02d3981512e79de340f85ede3

Ioannis Koulizakis & E. Loukis. (2020). A development framework for blockchain technologies in digital government. In Proceedings of the 13th International Conference on Theory and Practice of Electronic Governance. https://dl.acm.org/doi/10.1145/3428502.3428519

J Bou Abdo & S Zeadally. (2022). Multi-utility framework: blockchain exchange platform for sustainable development. https://www.emerald.com/insight/content/doi/10.1108/IJPCC-06-2020-0059/full/html

J. Ferguson & P. Bell. (2008). Tron Lennon discuss collaborative practice. https://www.semanticscholar.org/paper/f3aa9c8a82b5fb3d78e83004cf76bf6a4d46334c

J Kwon & E Buchman. (2018). A network of distributed ledgers. In Cosmos. https://cdn4.bitturk.com/whitepaper/atom.pdf

J Wilkes, P Goldsack, GJ Janakiraman, & L Russell. (2001). EOS-The Dawn of the Resource Economy. In hotos. https://shiftleft.com/mirrors/www.hpl.hp.com/research/ssp/papers/HotOS-2001-eOS-full.pdf

JA Asewe. (2022). Effect of Strategic Planning Practices on Organizational Performance of Firms in Pharmaceutical Industry in Kenya: A Case of Cosmos Limited. https://repository.daystar.ac.ke/bitstream/handle/123456789/4077/Effect%20of%20Strategic%20Planning%20Practices%20on%20Organizational%20Performance%20of%20Firms%20in%20Pharmaceutical%20Industry%20in%20Kenya%20A%20Case%20of%20Cosmos%20Limited.pdf?sequence=1&isAllowed=y

Jeffrey Burdges, Alfonso Cevallos, Peter Czaban, Rob Habermeier, S. Hosseini, F. Lama, Handan Kilinç Alper, X. Luo, Fatemeh Shirazi, Alistair Stewart, & G. Wood. (2020). Overview of Polkadot and its Design Considerations. In ArXiv. https://www.semanticscholar.org/paper/58a0b6c20a148bbeb7ecb0212b4e28f4868a89b6

JN Flores Gálvez & JM Mata Hernández. (2023). CBDC-MXN: Challenges and Perspectives in The Implementation as a Mexican Digital Currency. In Mercados y negocios. https://www.scielo.org.mx/scielo.php?pid=S2594-01632023000200003&script=sci_arttext&tlng=en

Joachim Rossberg. (2014). Development Processes and Frameworks. https://www.semanticscholar.org/paper/a4ee2829a99a940a1c72aca5da7c5d9da9844c7f

John M. Medellin & Mitchell A. Thornton. (2019). Consideration of Quality Attribute Tradeoffs of the Blockchain Pattern in the Software Development Process. In Annals of Emerging Technologies in Computing. https://www.semanticscholar.org/paper/8d400a97160c8b72d622a3bc6fec9102f27878f6

Jonas Schlund & R. German. (2019). A distributed ledger based platform for community-driven flexibility provision. In Energy Informatics. https://energyinformatics.springeropen.com/articles/10.1186/s42162-019-0068-0

JW Markhamt. (n.d.). LITIGATING INTERNATIONAL COMMERCIAL DISPUTES. Lawrence W. Newman & David Zaslowsky. Connecticut, USA: Quorum Books, 1996. Pp. xliii, 383. $50.00 …. https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/ncjint22&section=21

K. Burr, A. Iván, J. Leblanc, S. Zelakiewicz, D. McDaniel, C. Kim, A. Ganin, K. Shah, R. Grazioso, R. Farrell, & J. Glodo. (2003). Evaluation of a position sensitive avalanche photodiode for PET. In IEEE Transactions on Nuclear Science. https://www.semanticscholar.org/paper/338fff898fc701421595c12d559e6896f5106c53

K Lee, H Yu, X Zhang, & KH Choo. (2018). Quorum sensing and quenching in membrane bioreactors: opportunities and challenges for biofouling control. In Bioresource technology. https://www.sciencedirect.com/science/article/pii/S0960852418312641

Key Metrics for Evaluating Blockchain Development Success. (2024). https://sdlccorp.com/post/key-metrics-for-evaluating-blockchain-development-success/

Kui Gao, Yang Liu, Heyang Xu, & Tingting Han. (2019). Hyper-FTT: A Food Supply-Chain Trading and Traceability System Based on Hyperledger Fabric. In International Conference on Blockchain and Trustworthy Systems. https://www.semanticscholar.org/paper/ee5fac6ccbf344303f296c7409a2ea92da4a00ec

L Alakwaa, R Alkunaidri, & S Alhothli. (2025). Blockchain Technology Implementation in Telemedicine—A Case Study on Sehhaty Platform in Saudi Arabia. https://ieeexplore.ieee.org/abstract/document/10959563/

L Diego Solana. (2020). Factors that influence european consumer´ s satisfaction or dissastisfaction with different goods and services markets performance. https://repositorio.unican.es/xmlui/handle/10902/19967

L. Goodman, Laissez Faire, Les Propriétaires, & P. Proudhon. (2014). Tezos : A Self-Amending Crypto-Ledger Position Paper. https://www.semanticscholar.org/paper/f7907be464ef4c8aa74aacb6b4f4b043be5bb123

L. Olivieri, T. Jensen, L. Negrini, & F. Spoto. (2023). MichelsonLiSA: A Static Analyzer for Tezos. In 2023 IEEE International Conference on Pervasive Computing and Communications Workshops and other Affiliated Events (PerCom Workshops). https://ieeexplore.ieee.org/document/10150247/

L Wei, J Hu, F Li, J Song, & R Su. (2020). Comparative analysis and prediction of quorum-sensing peptides using feature representation learning and machine learning algorithms. https://academic.oup.com/bib/article-abstract/21/1/106/5152318

M Anson. (2018). Initial coin offerings: economic reality or virtual economics? In The Journal of Private Equity. https://www.jstor.org/stable/26497442

M Bonini. (n.d.). Proof of Location through a Blockchain Agnostic Smart Contract Language: Design and Evaluation over Algorand and Ethereum. https://amslaurea.unibo.it/id/eprint/27599/

M. Farooq & U. Ali. (2023). Harnessing the Potential of Blockchain in DevOps: A Framework for Distributed Integration and Development. In ArXiv. https://www.semanticscholar.org/paper/df668aa6843b1cf315641918e4bc435b361d913a

M. M. Adnan. (2023). Design and Development of Healthcare System Using Blockchain. In Journal of Smart Internet of Things. https://www.semanticscholar.org/paper/433b0c145878efdf88a3d24f86d1eab9fa3c6060

M Mazzoni, A Corradi, & V Di Nicola. (2022). Performance evaluation of permissioned blockchains for financial applications: The ConsenSys Quorum case study. In Blockchain: Research and applications. https://www.sciencedirect.com/science/article/pii/S209672092100021X

M. Morawietz. (1994). Empirischer Ausgangspunkt der Performancemessung. https://www.semanticscholar.org/paper/d3abbc54ce16e15dc8af71687b02e5f8abf5ca8d

M. Moreno & R. Brandão. (2023). A Knowledge-Oriented Approach to Enhance Integration and Communicability in the Polkadot Ecosystem. In ArXiv. https://www.semanticscholar.org/paper/bcda6bd21d4cfef4e0bb5d67eddc3ef13dae13e7

M. Raynal. (2018). Quorum, Signatures, and Overlays. https://link.springer.com/chapter/10.1007/978-3-319-94141-7_20

Maintain a Cosmos SDK Blockchain - HackMD. (n.d.). https://hackmd.io/@tendermint-devx/r1BtKtHHa

Mario Büsch. (2019). Analyse des Marktumfelds. In Fahrplan zur Transformation des Einkaufs. https://link.springer.com/chapter/10.1007/978-3-658-25637-1_5

Martin Valenta & Philipp G. Sandner. (2017). Comparison of Ethereum, Hyperledger Fabric and Corda. https://www.semanticscholar.org/paper/9f4f80c8e596b70ec8e2324f44ede15c48c147b5

Mary E. Tracy. (1995). Operation Avalanche: Prelude to Stalemate a Case Study in Operational Unit. https://www.semanticscholar.org/paper/a112d847e3c0bdffca99aae63f6bd1fb443576e8

Massimo Bartoletti, J. Chiang, & Alberto Lluch-Lafuente. (2020). SoK: Lending Pools in Decentralized Finance. In Financial Cryptography Workshops. https://www.semanticscholar.org/paper/d102780639e4d91e6549b23f621da00e961447bf

Matija Piškorec, Ben Domenic James Murphy, Florian Rüegsegger, Sina Rafati Niya, & C. Tessone. (2023). Bow-tie structure of the Polkadot transfer network. In 2023 IEEE International Conference on Blockchain and Cryptocurrency (ICBC). https://www.semanticscholar.org/paper/17f3a3cdc91d2bffa0fd066490bf647e89ece8da

Metrics data and monitoring - Enterprise 4.8 - docs.r3.com. (n.d.). https://docs.r3.com/en/platform/corda/4.8/enterprise/operations/monitoring-logging/metrics-monitoring-scenarios.html

MNN Rodrigo, S Perera, & S Senaratne. (2022). Systematic development of a data model for the blockchain-based embodied carbon (BEC) Estimator for construction. https://www.emerald.com/insight/content/doi/10.1108/ecam-02-2021-0130/full/html

MS Peelam, BK Chaurasia, & AK Sharma. (2024). Unlocking the potential of interconnected blockchains: a comprehensive study of cosmos blockchain interoperability. https://ieeexplore.ieee.org/abstract/document/10752501/

MT Alam & K Raza. (2021). Blockchain technology in healthcare: making digital healthcare reliable, more accurate, and revolutionary. https://www.sciencedirect.com/science/article/pii/B9780323898249000070

Nawaz Abdullah Malla, A. Marcelletti, A. Morichetta, & Francesco Tiezzi. (2024). Unveiling Algorand Storage Peculiarities. In International Conference on Developments in Language Theory. https://www.semanticscholar.org/paper/b1f97e255612df4ecc6fa668102cc40f20608ddc

Neelkumar K. Shah, Mayur Bilapate, Sachin Nandurkar, M. A. Maalik, Niteshkumar Harne, Karimullah Shaik, & Ajai Kumar. (2024). Security Assessment Framework and Evaluation for Blockchain Applications (SAFE-Block). In 2024 IEEE International Conference on Blockchain and Distributed Systems Security (ICBDS). https://www.semanticscholar.org/paper/4254cb5b751fb8b116d8a58bcd1ead45e7b43896

O. Bakr & I. Keidar. (2008). On the Performance of Quorum Replication on the Internet. https://www.semanticscholar.org/paper/0d82b5aab99a01dbc7e68f8adf458e364abee7c5

O Labazova. (2019). Towards a framework for evaluation of blockchain implementations. https://core.ac.uk/download/pdf/301384314.pdf

Operations - OpenTezos. (n.d.). https://www.opentezos.com/tezos-basics/operations/

Overview of the TRON Project. (1996). In Proceedings 13th TRON Project International Symposium /TEPS ’96. https://ieeexplore.ieee.org/document/566205/

P. Cunha, Piotr Soja, & Marinos Themistocleous. (2021). Blockchain for development: a guiding framework. In Information Technology for Development. https://www.semanticscholar.org/paper/6a7d26e36c5138e92381966a1971dd2e381ffb94

P Thakkar & S Nathan. (2018). Performance benchmarking and optimizing hyperledger fabric blockchain platform. https://ieeexplore.ieee.org/abstract/document/8526892/

Parachains on Polkadot, best projects, Acala, Monbeam, Clover, and others. (n.d.). https://globalcryptoexpert.com/university/crypto/top-polkadot-projects/

[PDF] AIARE Operational Avalanche Risk Management Plan. (2022). https://avtraining.org/wp-content/uploads/2022/07/AIARE-OARMP-Ver1_2022-07-13.pdf

[PDF] ISAHP Article: An Evaluation Framework for blockchain adoption in ... (n.d.). https://www.isahp.org/uploads/092_003.pdf

Performance considerations — Hyperledger Fabric Docs main documentation. (2023). https://hyperledger-fabric.readthedocs.io/en/release-2.5/performance.html

Phases of Evolution of Blockchain - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/ethical-hacking/phases-of-evolution-of-blockchain/

Polkadot Ecosystem Report - Parity Data Dashboards. (2023). https://dashboards.data.paritytech.io/reports/2023/index.html

Polkadot Price and Chart — DOT to USD — TradingView. (n.d.). https://www.tradingview.com/symbols/DOTUSD/

Polkadot SWOT Analysis – CanvasBusinessModel.com. (n.d.). https://canvasbusinessmodel.com/products/polkadot-swot-analysis?srsltid=AfmBOor_LtT9X_PVKVH1Plkp3WHFN4TPG-58GOdR5JNiBLwbFIyKCBzM

PS Anjana & S Ravi. (2025). Empirical Analysis of Transaction Conflicts in Ethereum and Solana for Parallel Execution. In arXiv. https://arxiv.org/abs/2505.05358

Quorum Health Corporation (NEW) -- Moody’s assigns Caa1 CFR to Quorum ... (2020). https://finance.yahoo.com/news/quorum-health-corporation-moodys-assigns-202507562.html

QUORUM HEALTH SWOT ANALYSIS – CanvasBusinessModel.com. (2025). https://canvasbusinessmodel.com/products/quorumhealth-swot-analysis?srsltid=AfmBOoo6R53GvDBfzGUfCvI0CbiTFZIeJEpUHQIZdCv06i4JPX85UZ9D

R. Pavlov, Olena Zarutska, Tetiana Pavlova, T. Grynko, O. Levkovich, & Liudmyla Hordieieva-Herasymova. (2024). BLOCKCHAIN AS A MANAGEMENT TECHNOLOGY: INSTITUTIONALIZATION OF CRYPTO-ASSETS AND TRANSFORMATION OF ENTREPRENEURIAL MODELS USING THE EXAMPLE OF ETHEREUM. In Financial and credit activity problems of theory and practice. https://www.semanticscholar.org/paper/e9dc0d46c18c1df01d6a0f27530800c3118632fe

R. Puyt, Finn Birger Lie, F. Graaf, & C. Wilderom. (2020). Origins of SWOT Analysis. In Academy of Management Proceedings. https://www.semanticscholar.org/paper/d9f3f6d56ffa768644e92813c0310aa60699fcf3

R3 Corda: A Distributed Ledger Technology for Financial Services. (2024). https://fernfortuniversity.com/essay/entrepreneurship_case/r-corda-distributed-ledger-technology-financial-services-39

R3’s Corda leads tokenized RWA market with over $10 billion in on-chain ... (n.d.). https://r3.com/r3s-corda-leads-tokenized-rwa-market-with-over-10-billion-in-on-chain-assets-and-unrivaled-industry-adoption/

S. Ashour. (2018). Measures of Performance. In Airline Network Planning and Scheduling. https://link.springer.com/chapter/10.1007/978-3-642-80693-3_3

S Gruber. (2017). Responsibility versus commerciality: Paradoxical message construction in the case of avalanche airbag producers. https://www.diva-portal.org/smash/record.jsf?pid=diva2:1112810

S. Lawrence. (2005). Mixed results in Q1. In Nature Biotechnology. https://www.semanticscholar.org/paper/d5dcac66bc59f63672ed535b2363d0ac75336fdc

S Ranjan, A Negi, H Jain, & B Pal. (2019). Network system design using hyperledger fabric: permissioned blockchain framework. https://ieeexplore.ieee.org/abstract/document/8844940/

S Saniee Monfared. (2023). Evaluating Blockchain Networks through Real-Time Simulation. https://yorkspace.library.yorku.ca/items/0e30a3c6-072a-42fd-bcca-66654ba816c1

S. Tikhomirov. (2017). Ethereum: State of Knowledge and Research Perspectives. In Foundations and Practice of Security. https://www.semanticscholar.org/paper/4a5135de004ac95cf379e9a4c1372afaee9837c5

S Trivedi. (2024). Blockchain technology and structural change in financial services. https://www.taylorfrancis.com/chapters/edit/10.1201/9781032630946-17/blockchain-technology-structural-change-financial-services-sonal-trivedi

Sin Kuang Lo, Xiwei Xu, Yin Kia Chiam, & Q. Lu. (2017). Evaluating Suitability of Applying Blockchain. In 2017 22nd International Conference on Engineering of Complex Computer Systems (ICECCS). https://www.semanticscholar.org/paper/e2999d3b80d79155755f757e70f1170a0df4187c

SJH Dehshiri, M Amiri, & SMH Bamakan. (2024). Evaluating the blockchain technology strategies for reducing renewable energy development risks using a novel integrated decision framework. In Energy. https://www.sciencedirect.com/science/article/pii/S0360544223033819

Solana Markets - Investing.com. (n.d.). https://www.investing.com/crypto/solana/markets

Solana Network Performance Report: March 2024. (2024). https://solana.com/news/network-performance-report-march-2024

Solana (SOL): Strengths, Weaknesses, Risks | CryptoEQ. (2024). https://www.cryptoeq.io/corereports/solana-abridged

Solana (SOL) to USD Price, Market Cap, Charts & News - Crypto Tracker. (n.d.). https://cryptotracker.com/price/solana

Srinjoy Mahato, Tanmoy Khatua, & Tathagata Roy Chowdhury. (2022). Bitcoin and Ethereum: The Crypto Currencies. In Journal of Intelligent Computing and Mathematics. https://www.semanticscholar.org/paper/c6ff31e724e268c7cdcff88cc04cfe9ee59bcc8e

SWOT analysis of the adoption of blockchain. Positive Negative. (n.d.). https://www.researchgate.net/figure/SWOT-analysis-of-the-adoption-of-blockchain-Positive-Negative_tbl1_323298791

T. Guggenberger, Johannes Sedlmeir, G. Fridgen, & André Luckow. (2021). An In-Depth Investigation of Performance Characteristics of Hyperledger Fabric. In ArXiv. https://www.semanticscholar.org/paper/8be3b581e6a4ead4c7d4e97176c06f2c3337ad5d

T Hiemstra. (2021). Blockchain platforms. https://www.theseus.fi/handle/10024/509455

T. Koens & E. Poll. (2019). Assessing interoperability solutions for distributed ledgers. In Pervasive Mob. Comput. https://linkinghub.elsevier.com/retrieve/pii/S1574119218306266

T Travel & D Mohanty. (n.d.). R3 Corda for Architects and Developers. https://link.springer.com/content/pdf/10.1007/978-1-4842-4529-3.pdf

T. Welch. (2016). Metrics for researchers. In The Journal of pediatrics. https://linkinghub.elsevier.com/retrieve/pii/S0022347615014729

Terrence Sellers-Saidi. (2012). Media Review: Tron. https://www.semanticscholar.org/paper/b9ead0a6491900706f8b301db81cd45c33ee177b

Tezos Price | XTZ Price Today, Live Chart, USD converter, Market ... (n.d.). https://cryptorank.io/price/tezos

Tezos Price, Chart, Market Cap, XTZ Coin Essentials | CoinLore. (n.d.). https://www.coinlore.com/coin/tezos

Tezos Price Today | Live XTZ Price Chart and Market Cap - CoinGape. (n.d.). https://coingape.com/price/tezos/

The 8 Best Blockchain Frameworks for Development - Blaize Tech. (2020). https://blaize.tech/blog/best-platforms-for-blockchain-development/

Thi Thu Huong Doan & Peter Thiemann. (2021). Towards Contract Modules for the Tezos Blockchain (Short Paper). In FMBC@CAV. https://www.semanticscholar.org/paper/2adf5782ddbee197745b2015af86daef8d852d12

Top 5 Blockchain Development Frameworks in 2025. (2024). https://webcomsystems.com.au/blog/top-5-blockchain-development-frameworks-in-2024/

Top 6 blockchain development frameworks - LogRocket Blog. (2021). https://blog.logrocket.com/top-blockchain-development-frameworks/

Top Blockchain Development Frameworks to Watch in 2025. (2025). https://www.codezeros.com/top-blockchain-development-frameworks-to-watch-in-2025

Towards a Performance Evaluation of Private Blockchain ... (n.d.). https://ieeexplore.ieee.org/document/8685888/

Tron analysis. Is Tron capable of becoming the main… | by ... - Medium. (2018). https://medium.com/electus-blog/tron-analysis-197704d4a66f

TRON price today, TRX to USD live price, marketcap and chart ... (n.d.). https://coinmarketcap.com/currencies/tron/

Tron price: TRX to USD, chart & market stats - crypto.news. (2025). https://crypto.news/price/tron/

TTH Doan & P Thiemann. (2024). A Formal Verification Framework for Tezos Smart Contracts Based on Symbolic Execution. https://link.springer.com/chapter/10.1007/978-981-97-8943-6_15

U Nwagwu. (2020). A SWOT analysis on the use of blockchain in supply chains. In Diss. Wichita State University. https://www.academia.edu/download/79072986/t20022_Nwagwu.pdf

Understanding Hyperledger Fabric: A Comprehensive Overview. (n.d.). https://medium.com/blockchain-hacks/understanding-hyperledger-fabric-a-comprehensive-overview-b84c783834c5

Understanding the 7 Stages of Blockchain Development Process. (2024). https://www.rapidinnovation.io/post/7-stages-of-new-blockchain-development-process

V. Allombert, Mathias Bourgoin, & J. Tesson. (2019). Introduction to the Tezos Blockchain. In 2019 International Conference on High Performance Computing & Simulation (HPCS). https://arxiv.org/abs/1909.08458

V. Basili, Adam Trendowicz, Martin Kowalczyk, J. Heidrich, C. Seaman, Jürgen Münch, & Dieter Rombach. (2014). GQM + Strategies in a Nutshell. https://www.semanticscholar.org/paper/cfd6c07787da09a343e27c29c617b1f6a5da53e3

Viktor Valaštín, Dušan Morháč, Kristián Kostál, & Ivan Kotuliak. (2024). Protocol for unifying cross-chain liquidity on polkadot. In Frontiers in Blockchain. https://www.semanticscholar.org/paper/215c51f8aeccbd96f4b6a77c31f0ca470472e5f9

W. Bezerra, Alan Nascimento Gomes, E. Coutinho, Críston P. de Souza, R. P. Magalhães, & David Vasconcelos. (2022). A Performance Analysis of Hyperledger Fabric: A Perspective of the ISO/IEC 25010 Product Quality Model. In Proceedings of the 11th Euro American Conference on Telematics and Information Systems. https://dl.acm.org/doi/10.1145/3544538.3544653

W Mensi, M Gubareva, KH Al-Yahyaee, & T Teplova. (2024). Extreme connectedness between cryptocurrencies and non-fungible tokens: portfolio implications. In Financial Innovation. https://link.springer.com/article/10.1186/s40854-023-00586-z

Welcome to Algorand. (n.d.). https://algorand.co/

Wenshuang Zhao, Kun Liu, & Kun Ma. (2019). Design of Student Capability Evaluation System Merging Blockchain Technology. In Journal of Physics: Conference Series. https://validate.perfdrive.com/fb803c746e9148689b3984a31fccd902/?ssa=2c93b5ed-101c-41bd-b5a7-eab4730a95a0&ssb=29466252974&ssc=https%3A%2F%2Fiopscience.iop.org%2Farticle%2F10.1088%2F1742-6596%2F1168%2F3%2F032123&ssi=a12d7cba-cnvj-4c5b-b34c-ee4c3040a5bd&ssk=botmanager_support@radware.com&ssm=11413125827286433586045995290923&ssn=1c685968d89cc52116e85f973a92c720728dc70a6c8a-a363-420f-abb8c9&sso=92a57880-d7d97fe455ff6a0b5dec3678e5bc9de345b7be8c57cde9ca&ssp=34375209331751099630175100514499180&ssq=92116581716288140311411120368922280833543&ssr=MzQuNTcuNDguMjE3&sst=python-httpx/0.27.2&ssu=&ssv=&ssw=&ssx=eyJyZCI6ImlvcC5vcmciLCJ1em14IjoiN2Y5MDAwYmIyMDhjNjUtMDI4MC00N2U2LWI1OGMtN2Q4YTc2ODdkYzk0MS0xNzUxMDExMTIwODEyNjA0MTY1MS1jMWEyZWY0NDllOTIzNTc5NTgiLCJfX3V6bWYiOiI3ZjYwMDAwZmM1MTRlOC1hMjQyLTRhNDktYmUxMy1kZmZmZjg1MjRiMDMxNzUxMDExMTIwODEyNjA0MTY1MS02NTU1NzFkYjJhY2VjNmI5NTgifQ==

What Big Companies Are Building on Ethereum - Galaxy. (2025). https://www.galaxy.com/insights/research/big-companies-building-on-ethereum

What is Algorand? A Beginner’s Guide to ALGO - 99Bitcoins. (n.d.). https://99bitcoins.com/cryptocurrency/what-is-algorand/

What Is Hyperledger Fabric? - IBM. (n.d.). https://www.ibm.com/think/topics/hyperledger

Wilson Abel Alberto Torres, Veronika Kuchta, Ron Steinfeld, A. Sakzad, Joseph K. Liu, & Jacob Cheng. (2019). Lattice RingCT V2.0 with Multiple Input and Multiple Output Wallets. In Australasian Conference on Information Security and Privacy. https://link.springer.com/chapter/10.1007/978-3-030-21548-4_9

X Li, X Wang, T Kong, J Zheng, & M Luo. (2021). From bitcoin to solana–innovating blockchain towards enterprise applications. https://link.springer.com/chapter/10.1007/978-3-030-96527-3_6

X Wu, J Xing, & X Li. (2025). Exploring Vulnerabilities and Concerns in Solana Smart Contracts. In arXiv. https://arxiv.org/abs/2504.07419

YC Wang, C Wang, MF Han, Z Tong, & YT Lin. (2022). Inhibiting effect of quorum quenching on biomass accumulation: A clogging control strategy in gas biofilters. https://www.sciencedirect.com/science/article/pii/S138589472105885X

Yongge Wang. (2019). Another Look at ALGORAND. In ArXiv. https://www.semanticscholar.org/paper/0c8e3186072491beded9233f6994719e4d508104

Yonghyun Kim, Ki-Hyung Kim, & Jai-hoon Kim. (2020). Power Trading Blockchain using Hyperledger Fabric. In 2020 International Conference on Information Networking (ICOIN). https://ieeexplore.ieee.org/document/9016428/

Yue Zeng & Yue Zhang. (2019). Review of research on blockchain application development method. In Journal of Physics: Conference Series. https://www.semanticscholar.org/paper/b959dacec6cba102974bf33a821ed934a9648391

Ивана Ковачевић. (2022). ПРИМЕНА HYPERLEDGER FABRIC BLOCKCHAIN-A У ПОСЛОВНИМ ПРОЦЕСИМА. In Zbornik radova Fakulteta tehničkih nauka u Novom Sadu. https://zbornik.ftn.uns.ac.rs/index.php/zbornik/article/view/2147

РР Білоскурський. (2023). USING CRYPTOCURRENCIES IN FINANCING SUSTAINABLE DEVELOPMENT GOAL PROJECTS: SWOT ANALYSIS. In Підприємництво і торгівля. http://www.journals-lute.lviv.ua/index.php/pidpr-torgi/article/view/1317

ภูมิพงศ์ จอมหงษ์พิพัฒน์. (2013). รูปแบบการพัฒนาภาวะผู้นำเหนือผู้นำสำหรับการปกครอง ส่วนท้องถิ่น กรณีศึกษา สมาชิกองค์การบริหารส่วนตำบลใน จังหวัดสกลนคร. https://www.semanticscholar.org/paper/82bb5201d4cbe0f08b63c5c895c18f802301b2b1

남미경. (2013). 지속가능발전을 위한 디자인의 역할과 유형 분석. https://www.semanticscholar.org/paper/b8c685d8a0abcb8ac7dd5ac55dded3e1f4b002b4

이장익. (2006). 평생교육기관 경영전략분석에 관한 SWOT 조사연구. In Andragogy Today. https://www.semanticscholar.org/paper/37f451b811d086e9e89597a7db66ae7d5a53e9b4

张熙平. (2003). 新码单反新生代Canon EOS 10D深入评测. https://www.semanticscholar.org/paper/022d2a84ac0040e101ecaa3214d58f24c46fd758

金晓燕. (2015). 杭州金融要素市场：SWOT分析、经验借鉴与政策研究. https://www.semanticscholar.org/paper/9690efa54c49dc9f10d4387287ce7fab7b73794c



Generated by Liner
https://getliner.com/search/s/5926611/t/86046749