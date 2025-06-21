'Blockchain Overlays.' Requirements: 1. Ensure compliance with MECE. 2. Classify/categorize logically and appropriately if necessary. 3. Explain with analogy and examples. 4. Use numbered lists for clear explanations when possible. 5. Describe core elements, components, factors and aspects. 6. List core evaluation dimensions and corresponding evaluations if applicable. 7. Describe their concepts, definitions, functions, and characteristics. 8. Clarify their purposes and assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect). 9. Describe relevant markets, ecosystems, regulations, and economic models, and explain the corresponding strategies used to generate revenue. 10. Describe their work mechanism concisely first and then explain how they work with phase-based workflows throughout the entire lifecycle. 11. Clarify their preconditions, inputs, outputs, immediate outcomes, long-term impacts, and potential implications. 12. Clarify their underlying laws, axioms, theories, and patterns. 13. Describe the design philosophy and architectural features. 14. Provide ideas, techniques, and means of architectural refactoring. 15. Clarify relevant frameworks, models, and principles. 16. Clarify their origins, evolutions, and trends. 17. List key historical events, security incidents, core factual statements, raw data points, and summarized statistical insights. 18. Clarify techniques, methods, approaches, protocols, and algorithms.  19. Describe contradictions and trade-offs. 20. Identify and list all major competitors (including the one being searched at present) with concise descriptions within the target market or industry segment. 21. Conduct a comprehensive competitor analysis to evaluate each competitor’s (including the one being searched at present) operational strategies, product offerings, market position, and performance metrics. 22. Perform a SWOT analysis for each competitor (including the one being searched at present), categorizing findings into strengths, weaknesses, opportunities, and threats. 23. Clarify principles, rules, constrains, limitations, vulnerabilities, challenges, obstacles, and risks. 24. Describe potential security vulnerabilities, troubleshooting methods, attack tactics, prevention methods and emergency measures. 25. Describe potential performance bottlenecks, troubleshooting methods and optimization measures. 26. Explain priorities, use cases, pitfalls, and best practices. 27. Clarify cause-and-effect relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 28. Clarify interdependency relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 29. Clarify cardinality-based relationships (1:1, 1:M, M:N). 26. Clarify contradictory relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 30. Describe the existing non-trivial problems and potential approaches to address them. 31. Introduce the relevant research topics of significant value that remain to be overcome. 32. Introduce the possible directions and approaches of within-domain and cross-domain innovation. 33. Predict the ultimate form of the related development. 34. Make a summary table at the end with purposes, characteristics, use cases, ect. for clarity. 35. Append the terminologies, formulas, and analogies at the end with concise descriptions for each item.

Thu Jun 12 2025

### Classification and Categorization of Blockchain Overlays (MECE Compliance)
Blockchain overlays can be classified systematically based on their network structure, operational context, and deployment model to ensure mutually exclusive and collectively exhaustive (MECE) categorization:

1. **Structural Classification**
   1. Unstructured Overlays: Nodes connect randomly (e.g., Bitcoin’s P2P network).
   2. Structured Overlays: Nodes are connected using fixed topologies or algorithms, such as Distributed Hash Tables (DHTs) like Kademlia (e.g., Ethereum).
   3. Semi-Structured Overlays: Hybrid approaches adding randomness to structured overlays for better security (e.g., overlays with Flexible Routing Tables).

2. **Deployment Context**
   1. Public/Permissionless Overlays: Open to all participants (Bitcoin, Ethereum P2P networks).
   2. Private/Consortium Overlays: Restricted access (Hyperledger, enterprise overlays).
   3. Application-Specific Overlays: Specialized for IoT, supply chains, etc.

3. **Topological Segmentation**
   1. Flat Overlays: Nodes operate on an equal level.
   2. Hierarchical Overlays: Nodes are organized in layers or domains (e.g., sovereign overlay domains in PODS).

This structure ensures all known types are captured without overlap.

---

### Analogy and Real-World Examples

1. **Analogy**: A blockchain overlay is like a social network where messages (transactions/blocks) are spread to friends (peers), some of whom are part of tightly knit communities (structured overlays/committees), while others are part of a looser network (unstructured overlays). Structured overlays resemble neighborhood committees efficiently coordinating information, but vulnerable if someone manipulates invitations. Unstructured overlays are akin to community bulletin boards—less efficient, but harder to manipulate.
2. **Real-World Examples**:
   - Bitcoin’s network: Unstructured overlay, highly resilient, decentralized.
   - Ethereum’s overlay: Structured via Kademlia for efficient information propagation.
   - Kadcast: Efficient block propagation using a structured overlay.

---

### Core Elements, Components, Factors, and Aspects

1. **Dynamic Peer-to-Peer Topology**: Overlay forms a web of nodes (peers) for decentralized communication.
2. **Routing Mechanisms/Tables**: Structures like DHTs, Flexible Routing Tables, or randomized neighbor lists.
3. **Bootstrapping Services**: On-chain or external mechanisms for new nodes to discover peers and join overlays.
4. **Data Propagation Protocols**: Broadcast, multicast, and gossiping strategies for efficient dissemination.
5. **Security Features**: Peer randomization, reputation mechanisms, domain restrictions, resilience to attacks like eclipse or partitioning.
6. **Hierarchical/Sovereign Domains**: Subdivision of overlays to manage node heterogeneity.

---

### Core Evaluation Dimensions and Evaluation Criteria

1. **Resilience**: Resistance to network partitioning, eclipse attacks, and node isolation.
2. **Efficiency**: Transaction/block propagation delay, bandwidth consumption, and message complexity.
3. **Security**: Exposure to vulnerabilities (eclipse attacks, Sybil attacks).
4. **Scalability**: Overlay’s adaptability to increasing number of nodes and high churn.
5. **Maintainability**: Ease of updating routing tables, handling churn, and integrating new protocols.

---

### Concepts, Definitions, Functions, and Characteristics

- **Concepts/Definition**: Blockchain overlays are dynamic, decentralized P2P networks sitting above the base blockchain protocol, responsible for node discovery, transaction/block propagation, and sometimes consensus facilitation.
- **Functions**:
   1. Enables fast, robust data dissemination among nodes.
   2. Provides structural resilience under adversarial conditions.
   3. Supports expansion through dynamic handling of peer churn.
- **Characteristics**:
   - Topological diversity: unstructured, structured, semi-structured.
   - Modular, adaptable design.
   - Balances efficiency, security, and scalability.

---

### Purposes and Assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect)

1. **Purposes**:
   - Facilitate decentralized, efficient, and robust communication among nodes.
   - Enhance scalability and attack resilience.
   - Enable interoperability and specialized application domains (IoT, supply chain).
2. **Assumptions**:
   - **Value**: Prioritize decentralization, security, censorship-resistance.
   - **Descriptive**: Nodes join/leave randomly, are resource heterogeneous, and can be adversarial.
   - **Prescriptive**: Enforce protocols to randomize neighbor selection, bootstrap securely, and balance performance.
   - **Worldview**: Trustless, open systems that assume threat presence.
   - **Cause-and-Effect**: Well-structured overlays -reduce-> propagation delay -improve-> consensus finality.

---

### Relevant Markets, Ecosystems, Regulations, and Economic Models

- **Markets**: Cryptocurrencies (Bitcoin, Ethereum), DeFi, IoT, supply chain, creative industries.
- **Ecosystems**: Nodes, miners, validators, users, infrastructure providers.
- **Regulations**: Focus on competition, privacy, ledger transparency, anti-money laundering; evolving compliance frameworks.
- **Economic Models**:
   1. Transaction fees and mining/staking rewards.
   2. Asset tokenization (NFTs, fractional ownership).
   3. Token offerings (ICOs) for financing and incentive alignment.
   4. Institutional overlays create platform revenue via licensing and service fees.

---

### Work Mechanism and Phase-Based Workflows

**Concise Mechanism**:  
Blockchain overlays establish dynamic, decentralized P2P networks that handle node discovery, secure bootstrapping, and efficient data propagation, adapting to ongoing churn and security threats.

**Lifecycle Phases**:
1. **Bootstrapping**: New node discovers and verifies peers, often from on-chain data.
2. **Connectivity Formation**: Nodes establish structured or random connections; routing tables are set up.
3. **Dissemination**: Transactions/blocks are propagated across network using broadcast, multicast, or gossip.
4. **Maintenance**: Ongoing health checks, randomized neighbor updates, and recovery from failures/churn.
5. **Security & Attack Mitigation**: Randomization, peer diversity, and real-time auditing to detect and counteract attacks.

---

### Preconditions, Inputs, Outputs, Immediate Outcomes, Long-Term Impacts, and Potential Implications

1. **Preconditions**: Operational underlying blockchain, accessible network, protocol definitions, ready nodes.
2. **Inputs**: Node join/leave events, transactions, block data, peer discovery information, protocol messages, random seeds.
3. **Outputs**: Efficient dissemination of data, updated routing topologies, resilience events (e.g., successful defense against an eclipse attack), consensus communications.
4. **Immediate Outcomes**: Improved propagation speed, attack resistance, dynamic adaptation.
5. **Long-Term Impacts**: Enhanced network scalability, trust, and system evolution; new cross-domain business models.

---

### Underlying Laws, Axioms, Theories, and Patterns

1. **Graph Theory**: Defines overlay topology, connectivity, and route optimization.
2. **Distributed Systems**: Principles for fault-tolerance, dynamic membership, bootstrap protocols.
3. **Game Theory**: Underpins economic incentives, rational adversary models.
4. **Pattern Recognition**: Efficiency-security tradeoff patterns in overlay structure.
5. **Decentralization Axiom**: All overlays aim to avoid single points of failure.

---

### Design Philosophy and Architectural Features

- **Philosophy**: Combine decentralization and modular adaptability with resilient and secure routing to handle churn and adversarial conditions.
- **Architectural Features**:
   - Routing Flexibility: Support for both fixed and random neighbor selection.
   - Ledger-Assisted Peer Discovery: Bootstrap using on-chain peer data.
   - Hierarchical Segmentation: Overlay domains for node heterogeneity.
   - Reputation Security: Peer validation and reputation layers where needed.

---

### Architectural Refactoring: Ideas, Techniques, and Means

1. Replacing rigid overlays with modular or microservice-based overlay components for scalability.
2. Introduce or enhance flexible routing tables and semi-structured overlays to improve both performance and resistance to attacks.
3. Hierarchical/segmented overlays (domain sovereignty) for managing heterogeneous resources.
4. Integrating overlay refactoring automation for API and component interface upgrades.

---

### Relevant Frameworks, Models, and Principles

- Structured overlays (e.g., DHTs: Kademlia, Chord) for deterministic routing.
- Semi-structured models using randomness and reputation.
- Hypercubic, hyperclique, or geographically-aware topologies for broadcast optimization and resilience.
- Security and resilience frameworks based on cross-domain segmentation.

---

### Origins, Evolution, and Trends

- **Origins**: Early blockchains like Bitcoin used unstructured overlays.
- **Evolution**: Movement toward structured (Ethereum/Kademlia), then semi-structured overlays for balancing efficiency/security.
- **Trends**: Integration of on-chain data for overlay maintenance, multi-layer hierarchical overlays for improved robustness, and AI-driven adaptive routing.

---

### Key Historical Events, Security Incidents, and Core Data

- Emergence of unstructured overlays in Bitcoin (2009).
- Risks of network partition and eclipse attacks leading to development of semi-structured overlays.
- Notable security incidents: DAO hack, Mt.Gox collapse—highlighting overlay and consensus vulnerabilities.
- Statistical evidence: Seven overlays studied, showing partitioning risk if few highly connected peers are attacked.

---

### Techniques, Methods, Protocols, and Algorithms

- Kadcast/Kademlia: Structured overlay protocols for block broadcast.
- Flexible Routing Tables: Allow partial randomization for security.
- Blockchain-based Bootstrapping: On-chain peer discovery.
- Overlay multicast trees, committee-based overlays, and churn-management protocols.

---

### Contradictions and Trade-offs

- Structured overlays → high efficiency but ↓ security (eclipse attacks).
- Unstructured overlays → high security but ↓ propagation efficiency.
- Decentralization vs. performance: More decentralized overlays are robust but slower; centralized elements improve speed but may compromise trust.
- On-chain data storage vs. cost: Full immutability ↑ costs, off-chain ↑ risk.

---

### Competitors, Analysis, and SWOT

**Major Competitors**:
1. Bitcoin Overlay: Highly decentralized, unstructured, robust but less efficient.
2. Ethereum Overlay: Structured, efficient, supports smart contracts, but more vulnerable.
3. Kadcast: Focused on broadcast efficiency, uses structure for rapid propagation.
4. Semi-Structured Overlays: Combine structure and randomness for trade-off balance.
5. Hyperclique/Hypercube: Academic overlays focusing on network diameter and density.
6. Permissioned Enterprise Overlays (Hyperledger): Governed networks, controlled access, high compliance.

**Competitor Analysis Table**:

| Competitor        | Strategy            | Position                | Product Offering                          | Performance Metrics        |
|-------------------|--------------------|-------------------------|-------------------------------------------|---------------------------|
| Bitcoin Overlay   | Full decentralization| Dominant cryptocurrency | Unstructured P2P for BTC                  | High robustness, slower   |
| Ethereum Overlay  | Structured overlays | DApp platform           | Smart contract support, Kademlia routing  | Efficient, some risks     |
| Kadcast           | Efficient broadcast | Protocol for blockchains| Structured overlay, low-latency broadcast | Low latency, efficient    |
| Semi-Structured   | Hybrid approaches   | Niche, innovation       | FRT, mix of resilience and speed          | Balanced                  |
| Hyperclique       | Short diameter      | Research/innovation     | Dense overlay, adaptable topology         | Superior routing/latency  |
| Hyperledger       | Consortium control  | Enterprise/permissioned | Governance, access controls, compliance   | Enterprise grade, scalable|

**SWOT Example—Semi-Structured Overlays**:

- Strengths: Balances security and efficiency, adaptable.
- Weaknesses: Increased complexity, design overhead.
- Opportunities: Adoption in IoT, regulated industries.
- Threats: Evolving attack methods, competing overlay protocols.

---

### Principles, Rules, Constraints, Limitations, Vulnerabilities, Challenges, and Risks

- Principles: Decentralization, randomness in routing, modularity, and defense-in-depth.
- Rules: Structured overlays must avoid deterministic neighbor selection; ensure IP diversity among neighbors.
- Constraints: Resource limitations (bandwidth, computational power), node churn, dynamic topologies.
- Limitations: Trade-off between structure and security, scalability bottlenecks.
- Vulnerabilities: Eclipse/Sybil attacks, DDoS, peer table poisoning.
- Challenges: Overlay maintenance, efficient bootstrapping, real-time attack mitigation.

---

### Security Vulnerabilities, Troubleshooting, Attacks, and Prevention

- Vulnerabilities: Peer table poisoning, lack of redundancy, predictable structure.
- Troubleshooting: Auditing peer connections, cross-verification of blockchain views.
- Attack Tactics: Eclipse (isolation via peer domination), Sybil, routing manipulation.
- Prevention: Random neighbor selection, subnet restrictions, resilient peer discovery.
- Emergency Measures: Rapid reconnection, use of trusted oracles, network partition alerts.

---

### Performance Bottlenecks, Troubleshooting, and Optimization

- Bottlenecks: Routing inefficiencies, overlay churn, broadcast congestion.
- Troubleshooting: Profiling network delays, adaptive routing protocol updates.
- Optimization: Use semi-structured overlays, broadcast trees, adaptive dimensioning.

---

### Priorities, Use Cases, Pitfalls, Best Practices

1. **Priorities**: Security, efficiency, scalability, adaptability.
2. **Use Cases**: Cryptocurrency (BTC, ETH), receipt networks, supply chain, IoT access.
3. **Pitfalls**: Overly deterministic overlays susceptible to targeted attacks, insufficient bootstrapping, ignoring churn.
4. **Best Practices**: Semi-structured overlays, on-chain bootstrap, regular maintenance, randomized connections.

---

### Cause-and-Effect Relationships

- Structured overlays <-increase-> propagation speed -but-increase-> eclipse risk.
- Randomized routing -reduces-> attack surface -but-may-increase-> path length.
- Churn/peer leave -causes-> topology updates -affects-> resilience, delay.
- Economic incentives -motivate-> node honesty -increase-> security.
- Excessive centralization -raises-> performance -but-decreases-> resiliency.

---

### Interdependency Relationships

- Node churn and overlay maintenance <-are interdependent-> network resilience and efficiency.
- Economic incentives among overlays -drive-> cross-platform Sybil attack risk.
- Bootstrapping dependent on blockchain state; chain health affects overlay.

---

### Cardinality-Based Relationships (1:1, 1:M, M:N)

- 1:1: Rare, used for direct or control connections.
- 1:M: Miner broadcasting blocks to multiple peers (1 node -> many nodes).
- M:N: Typical for large overlays—each node links to multiple others (many-to-many).

---

### Contradictory Relationships

- Structured overlays -boost-> efficiency <-but-increase-> attack risk.
- Decentralization <-champions-> trustless operation -but-may-lower-> propagation speed.
- Security via randomness -raises-> resilience -but-may-reduce-> deterministic optimization.

---

### Non-Trivial Problems and Approaches

- Non-trivial problems: Partition resistance under attack/churn, balancing security and efficiency, measuring overlay quality.
- Approaches: Ledger-based overlay maintenance, semi-structured overlays, resilient bootstrap protocols, dynamic adaptation.

---

### Open Research Topics

Significant outstanding research challenges include:

1. Resilient overlay algorithms supporting dynamic churn and adversarial presence.
2. Topology mapping and underlay-aware overlays.
3. Overlay-application interoperability and security models.
4. Multilayer, adaptive, and AI-driven overlays for future blockchains.

---

### Within-Domain and Cross-Domain Innovation

- **Within-domain**: Flexible routing, committee-based security, semi-structured topologies.
- **Cross-domain**: Federated overlays, cross-chain authentication/authorization, blockchain-integrated IoT overlays.
- **Techniques**: Ledger-based cross-domain access, dynamic accumulators, decentralized identifiers.

---

### Ultimate Form of Blockchain Overlay Development

The ultimate blockchain overlay will be modular, multi-domain, and AI-enhanced, integrating blockchain-native trust mechanisms, adaptive routing, cross-domain interoperability, and dynamic topology management to maximize efficiency, security, and resilience across heterogeneous environments.

---

### Summary Table: Blockchain Overlays

| Aspect             | Description / Examples                                            |
|--------------------|-------------------------------------------------------------------|
| Purposes           | Decentralized data propagation, robustness, scalability            |
| Structure          | Unstructured, structured, semi-structured                         |
| Key Elements       | Topology, routing, bootstrapping, maintenance                     |
| Evaluation         | Resilience, Efficiency, Security, Scalability, Maintainability     |
| Use Cases          | Cryptocurrency, smart contracts, IoT, supply chains               |
| Markets            | Crypto, enterprise DLT, IoT, creative industries                  |
| Economics          | Fees, mining/staking, tokenization, licensing, incentives         |
| Lifecycle          | Bootstrapping → Connectivity → Dissemination → Maintenance        |
| Laws/Axioms        | Graph theory, distributed systems, game theory, decentralization  |
| Security           | Eclipse, Sybil, DDoS, privacy attacks, bootstrapping attacks      |
| Design             | Modular, hierarchical, flexible routing, on-chain bootstrap       |
| Contradictions     | Efficiency vs. security, scalability vs. maintainability          |
| Major Competitors  | Bitcoin overlay, Ethereum, Kadcast, semi-structured, Hyperledger  |

---

### Terminologies, Formulas, and Analogies (Concise Descriptions)

- **Blockchain Overlay Network**: P2P network above Layer 1, manages node communication and data.
- **Structured Overlay**: Topology like DHT (Kademlia), efficient, may be vulnerable.
- **Unstructured Overlay**: Random links, robust, less efficient.
- **Semi-structured Overlay**: Blend of structure and randomness for balance.
- **Bootstrapping**: Peer discovery, often via on-chain data.
- **Churn**: Dynamic node change, requires robust maintenance.
- **Committee/Domain**: Subset for governance/maintenance; used in forexample PODS.
- **Eclipse Attack**: Isolation of nodes by controlling connections.
- **Formulas**: Randomness ratio ≈ 2^r / 2^m for flexible routing; broadcast delay, average path length for assessment.
- **Analogy**: Overlay as a community or social network—structured like a 'neighborhood committee'; unstructured as 'community bulletin board'.

This deep and structured overview provides factual, categorized, and comprehensive insights into blockchain overlays as currently understood in research and practice.

Bibliography
A. Averin & O. Averina. (2019). Review of Blockchain Technology Vulnerabilities and Blockchain-System Attacks. In 2019 International Multi-Conference on Industrial Engineering and Modern Technologies (FarEastCon). https://www.semanticscholar.org/paper/38da8ab62e28ab294847b9a3d9e36e477651a322

A Howell, T Saber, & M Bendechache. (2023). Measuring node decentralisation in blockchain peer to peer networks. https://www.sciencedirect.com/science/article/pii/S2096720922000501

A. Kim, Meryam Essaid, & Hongtaek Ju. (2023). Survey on Blockchain P2P Network. In 2023 24st Asia-Pacific Network Operations and Management Symposium (APNOMS). https://www.semanticscholar.org/paper/fe09378e93bb106fa351109c93751e2947b0a088

A Malatras. (2015). State-of-the-art survey on P2P overlay networks in pervasive computing environments. In Journal of Network and Computer Applications. https://www.sciencedirect.com/science/article/pii/S1084804515000879

A Paphitis. (2023). A Unified Approach to Assessing the Structural Resilience of Blockchain Overlay Networks. https://ktisis.cut.ac.cy/handle/20.500.14279/31965

A Paphitis, N Kourtellis, & M Sirivianos. (2021). A first look into the structural properties and resilience of blockchain overlays. In arXiv. https://arxiv.org/abs/2104.03044

A Paphitis, N Kourtellis, & M Sirivianos. (2023a). Graph analysis of blockchain p2p overlays and their security implications. https://link.springer.com/chapter/10.1007/978-981-99-5177-2_10

A Paphitis, N Kourtellis, & M Sirivianos. (2023b). Resilience of blockchain overlay networks. https://link.springer.com/chapter/10.1007/978-3-031-39828-5_6

A Pasdar, YC Lee, & Z Dong. (2023). Connect API with blockchain: A survey on blockchain oracle implementation. In ACM Computing Surveys. https://dl.acm.org/doi/abs/10.1145/3567582

Ahmed Alketbi, Q. Nasir, & M. A. Talib. (2018). Blockchain for government services — Use cases, security benefits and challenges. In 2018 15th Learning and Technology Conference (L&T). https://ieeexplore.ieee.org/document/8368494/

Ahsan Umar & Muhammad Zeeshan Zafar. (2025). Blockchain Security: Vulnerabilities and Protective Measures. In World Journal of Advanced Research and Reviews. https://journalwjarr.com/node/911

Ámbar Tenorio-Fornés, Samer Hassan, & J. Pavón. (2021). Peer-to-Peer System Design Trade-Offs: A Framework Exploring the Balance between Blockchain and IPFS. In Applied Sciences. https://www.mdpi.com/2076-3417/11/21/10012

Astrid Carolina Ordoñez-Guerrero, Juan David Muñoz-Garzon, E. Villarreal, A. Bandi, & J. Hurtado. (2022). Blockchain Architectural Concerns: A Systematic Mapping Study. In 2022 IEEE 19th International Conference on Software Architecture Companion (ICSA-C). https://ieeexplore.ieee.org/document/9779841/

Ayman Alkhalifah, Alex Ng, A. Kayes, Jabed Chowdhury, M. Alazab, & P. Watters. (2019). A Taxonomy of Blockchain Threats and Vulnerabilities. In Blockchain for Cybersecurity and Privacy. http://www.preprints.org/manuscript/201909.0117/v1

B Bellaj, A Ouaddah, E Bertin, & N Crespi. (2024). Drawing the boundaries between blockchain and blockchain-like systems: A comprehensive survey on distributed ledger technologies. https://ieeexplore.ieee.org/abstract/document/10517413/

B Xu, H Li, X Zhang, & TB Alejandro. (2023). Equilibrium blockchain adoption strategies for duopolistic competitive platforms with network effects. In Journal of Business Research. https://www.sciencedirect.com/science/article/pii/S0148296323003119

C Bai & J Sarkis. (2022). A critical review of formal analytical modeling for blockchain technology in production, operations, and supply chains: Harnessing progress for future potential. In International Journal of Production Economics. https://www.sciencedirect.com/science/article/pii/S0925527322002183

C Ipert & R Mauer. (2023). Infrastructural or organizational decentralization? Developing a typology of blockchain ventures. In Technological Forecasting and Social Change. https://www.sciencedirect.com/science/article/pii/S0040162523005334

C. Rottondi, A. Panzeri, Constantin Yagne, & G. Verticale. (2016). Detection and mitigation of the eclipse attack in chord overlays. In Int. J. Comput. Sci. Eng. https://www.inderscienceonline.com/doi/abs/10.1504/IJCSE.2016.078440

C. Worley & A. Skjellum. (2018). Blockchain Tradeoffs and Challenges for Current and Emerging Applications: Generalization, Fragmentation, Sidechains, and Scalability. In 2018 IEEE International Conference on Internet of Things (iThings) and IEEE Green Computing and Communications (GreenCom) and IEEE Cyber, Physical and Social Computing (CPSCom) and IEEE Smart Data (SmartData). https://ieeexplore.ieee.org/document/8726513/

Cory Cherven. (2024). The Societal Implications of Blockchain Proliferation. In ArXiv. https://arxiv.org/abs/2404.02451

Dongmei Li & Guo Hui. (2024). Blockchain Technology in International Trade: A Catalyst for Efficiency and Revenue Generation. In International Journal of Sociologies and Anthropologies Science Reviews. https://www.semanticscholar.org/paper/df68dc60d2952dde35fa44d463c6063b65c65bb7

Dylan Yaga, P. Mell, N. Roby, & K. Scarfone. (2018). Blockchain Technology Overview. In ArXiv. https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8202.pdf

E. Zamani, Ying He, & M.L.F. Phillips. (2018). On the Security Risks of the Blockchain. In Journal of Computer Information Systems. https://www.tandfonline.com/doi/full/10.1080/08874417.2018.1538709

EK Lua, J Crowcroft, & M Pias. (2005). A survey and comparison of peer-to-peer overlay network schemes. https://ieeexplore.ieee.org/abstract/document/1610546/

Elena Viţelaru & Luca Persia. (2023). Fractional Vehicle Ownership and Revenue Generation Through Blockchain Asset Tokenization. In Transport and Telecommunication Journal. https://sciendo.com/article/10.2478/ttj-2023-0011

Elias Rohrer & Florian Tschorsch. (2019). Kadcast: A Structured Approach to Broadcast in Blockchain Networks. In Proceedings of the 1st ACM Conference on Advances in Financial Technologies. https://dl.acm.org/doi/10.1145/3318041.3355469

Elias Rohrer & Florian Tschorsch. (2023). Kadcast-NG: A Structured Broadcast Protocol for Blockchain Networks. In IEEE/ACM Transactions on Networking. https://ieeexplore.ieee.org/document/10144414/

F Badalov. (1948). Refactoring for Enhanced Reliability: Methods and Tools in Blockchain Development. In Available at SSRN 4822971. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4822971

F. Montesi, Marco Peressotti, Valentino Picotti, & Olaf Zimmermann. (2024). A Conceptual Framework for API Refactoring in Enterprise Application Architectures. In ArXiv. https://arxiv.org/abs/2407.07428

G Caldarelli. (2023). Before ethereum. the origin and evolution of blockchain oracles. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10131932/

G. Quattrocchi, Filippo Scaramuzza, & D. Tamburri. (2024). The Blockchain Trilemma: An Evaluation Framework. In IEEE Software. https://ieeexplore.ieee.org/document/10572260/

Guzmán Llambías, Laura González, & R. Ruggia. (2023). Blockchain Interoperability: a Feature-based Classification Framework and Challenges Ahead. In CLEI Electron. J. https://www.semanticscholar.org/paper/ea33414c8c6a4976937462776d6647074e63c7d4

H. Ijaz, M. Welzl, & Bushra Jamil. (2018). A survey and comparison on overlay‐underlay mapping techniques in peer‐to‐peer overlay networks. In International Journal of Communication Systems. https://onlinelibrary.wiley.com/doi/10.1002/dac.3872

H Qiu, T Ji, S Zhao, X Chen, & J Qi. (2022). A geography-based p2p overlay network for fast and robust blockchain systems. https://ieeexplore.ieee.org/abstract/document/9826458/

Horst Treiblmaier & A. Tumasjan. (2022). Editorial: Economic and Business Implications of Blockchain Technology. In Frontiers in Blockchain. https://www.frontiersin.org/articles/10.3389/fbloc.2022.857247/full

I Aviv, A Barger, A Kofman, & R Weisfeld. (2023). Reference architecture for blockchain-native distributed information system. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10014995/

I Homoliak & S Venugopalan. (2020). The security reference architecture for blockchains: Toward a standardized model for studying vulnerabilities, threats, and defenses. https://ieeexplore.ieee.org/abstract/document/9239372/

I. Kautsar, M. Maika, Thi-Hong-Van Hoang, Zhenzhen Zhu, Abdelbari El Khamlichi, Wing-Keung Wong, Elizabeth Bucher-Edwards, Louise Grimmer, Martin Grimmer, Prabal Shrestha, Özgür Arslan-Ayaydin, J. Thewissen, Giancarlo Giudici, & Giancarlo Giuffra. (2019). Blockchain Technology: Revenue Streams of Long Tail Business Model. In Proceedings of the Proceedings of the 1st Sampoerna University-AFBE International Conference, SU-AFBE 2018, 6-7 December 2018, Jakarta Indonesia. https://www.semanticscholar.org/paper/0013866d6d739789299aa517c583a4b7f488c156

Inês Faria. (2021). The market, the regulator, and the government: Making a blockchain ecosystem in the Netherlands. https://www.semanticscholar.org/paper/d99fedf8771f036ac3ded5126488341ca355b30b

J. Burnett & Calvin Blackwell. (2023). Graphical causal modelling: an application to identify and estimate cause-and-effect relationships. In Applied Economics. https://www.tandfonline.com/doi/full/10.1080/00036846.2023.2208856

J Ding, I Balasingham, & P Bouvry. (2009). Management of overlay networks: A survey. https://ieeexplore.ieee.org/abstract/document/5361643/

J Paillissé Vilanova. (2021). Next generation overlay networks: security, trust, and deployment challenges. https://upcommons.upc.edu/handle/2117/351110

J. Potts, Darcy W. E. Allen, C. Berg, S. Davidson, & T. MacDonald. (2021). An economic theory of blockchain foundations. In Social Science Research Network. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3842281

J Song, P Zhang, Q Qu, Y Bai, Y Gu, & G Yu. (2023). Why blockchain needs graph: A survey on studies, scenarios, and solutions. https://www.sciencedirect.com/science/article/pii/S0743731523001004

JJ Ryan & SS Smith. (2021). History of blockchain. https://www.emerald.com/insight/content/doi/10.1108/978-1-83982-198-120211004/full/html

Joerg Evermann & Henry M. Kim. (2019). Workflow Management on the Blockchain - Implications and Recommendations. In ArXiv. https://www.semanticscholar.org/paper/de37e2eda9a6a60b42a6e7ba9b61c914b77c5fa4

K Agrawal, M Aggarwal, S Tanwar, & G Sharma. (2022). An extensive blockchain based applications survey: tools, frameworks, opportunities, challenges and solutions. https://ieeexplore.ieee.org/abstract/document/9936616/

K Li, Y Tang, J Chen, Y Wang, & X Liu. (n.d.). Poster: TopoShot: Uncovering Ethereum’s Network Topology Leveraging Replacement Transactions. https://conferences.sigcomm.org/imc/2021/pdf/TopoShot.pdf

L Besancon, CF Da Silva, P Ghodous, & JP Gelas. (2022). A blockchain ontology for DApps development. In Ieee Access. https://ieeexplore.ieee.org/abstract/document/9770809/

L Cheng, H Tan, X Li, W Pan, H Zhao, M Yuan, & X Li. (2024). A hierarchical overlay network optimisation model for enhancing data transmission performance in blockchain systems. In Scientific Reports. https://www.nature.com/articles/s41598-024-83399-z

L Lunardon & A Pagani. (2024). GOvNet: a Blockchain Overlay Network for Governments and Privacy-Oriented Applications. https://ieeexplore.ieee.org/abstract/document/10664372/

Lin Chen, Ping Li, & Qiang Li. (2018). The evolving networks of debtor-creditor relationships with addition and deletion of nodes: a case of P2P lending. In arXiv: General Finance. https://www.semanticscholar.org/paper/6c5e7199b3bb50d79a47611e831bb655aec103ff

Lorenzo Ghiro, Francesco Restuccia, Salvatore D’oro, S. Basagni, T. Melodia, L. Maccari, & R. Cigno. (2021). What is a Blockchain? A Definition to Clarify the Role of the Blockchain in the Internet of Things. In ArXiv. https://www.semanticscholar.org/paper/55a6f3ed604acc529adc19aa7331ad998c143057

M Chase & S Meiklejohn. (2016). Transparency overlays and applications. https://dl.acm.org/doi/abs/10.1145/2976749.2978404

M Dotan, YA Pignolet, S Schmid, & S Tochner. (2021). Survey on blockchain networking: Context, state-of-the-art, challenges. https://dl.acm.org/doi/abs/10.1145/3453161

M Ruta, F Scioscia, S Ieva, G Capurso, & A Pinto. (2018). A Blockchain Infrastructure for the Semantic Web of Things. In SEBD. https://sisinflab.poliba.it/publications/2018/RSICPD18/ruta_et_al_SEBD2018.pdf

M Saad, J Spaulding, & L Njilla. (2020). Exploring the attack surface of blockchain: A comprehensive survey. https://ieeexplore.ieee.org/abstract/document/9019870/

M Swan. (2018). Blockchain economic networks: Economic network theory—Systemic risk and blockchain technology. In Business Transformation through Blockchain: Volume I. https://link.springer.com/chapter/10.1007/978-3-319-98911-2_1

M Xu, Y Guo, C Liu, Q Hu, D Yu, & Z Xiong. (2024). Exploring blockchain technology through a modular lens: A survey. https://dl.acm.org/doi/abs/10.1145/3657288

Maheshwari V. & P. M. (2024). Hierarchical Interdependency Blockchain for Assessing Performance and Modulation Proof of Stake (POS) Security Protocol in Healthcare
Application 5.0. In Recent Advances in Electrical &amp; Electronic Engineering (Formerly Recent Patents on Electrical &amp; Electronic Engineering). https://www.semanticscholar.org/paper/070c6db4f26b4e3d7b17428c250671bdeb220a10

Manpreet Kaur & Shikha Gupta. (2021). Blockchain Consensus Protocols: State-of-the-art and Future Directions. In 2021 International Conference on Technological Advancements and Innovations (ICTAI). https://ieeexplore.ieee.org/document/9673260/

Mengfen Luo & Xiangyan Deng. (2023). Research on the Security Risks of Digital Empowerment and the Participation of “Blockchain+” in RCEP Commerce Strategy. In International Journal of Frontiers in Sociology. https://francis-press.com/papers/13672

Milos Obradović & Pavle V. Vuletic. (2024). Blockchain Programming Languages Vulnerabilities and Error Mitigation Strategies. In 2024 11th International Conference on Electrical, Electronic and Computing Engineering (IcETRAN). https://ieeexplore.ieee.org/document/10645154/

Mohd Azeem Faizi Noor & Khurram Mustafa. (2024). Mitigating Blockchain Endpoint Vulnerabilities: Conceptual Frameworks. In International Journal of Computer Networks and Applications. https://www.ijcna.org/Manuscripts/IJCNA-2024-O-56.pdf

Mubashar Iqbal & Raimundas Matulevičius. (2021). Exploring Sybil and Double-Spending Risks in Blockchain Systems. In IEEE Access. https://ieeexplore.ieee.org/document/9435780/

Muhammad Nasir Mumtaz Bhutta, A. Khwaja, A. Nadeem, H. F. Ahmad, M. Khan, Moataz Hanif, H. Song, Majed A. Alshamari, & Yue Cao. (2021). A Survey on Blockchain Technology: Evolution, Architecture and Security. In IEEE Access. https://ieeexplore.ieee.org/document/9402747/

Mustafa Salih Dakhil, Muyiwa Emmanuel Dagunduro, Faraj Gheni Abbood, & Gbenga Ayodele Falana. (2025). Tax Compliance Strategies and Revenue Generation in Nigeria. In Economy, Business and Development: An International Journal. https://www.semanticscholar.org/paper/f3667cc40810f8d85fde45916b2d44dda7ffe797

N Malik, G Appel, & L Luo. (2023). Blockchain technology for creative industries: Current state and research opportunities. In International Journal of Research in Marketing. https://www.sciencedirect.com/science/article/pii/S0167811622000544

N Upadhyay. (2024). Business models for the Blockchain: An empirical analysis. In Digital Business. https://www.sciencedirect.com/science/article/pii/S2666954424000103

N Zarin, I Sheff, & S Roos. (2023). Blockchain Nodes are Heterogeneous and Your P2P Overlay Should be Too: PODS. In arXiv. https://arxiv.org/abs/2306.16153

Nils Amiet. (2021). Blockchain Vulnerabilities in Practice. In Digital Threats: Research and Practice. https://dl.acm.org/doi/10.1145/3407230

NK Tran, MA Babar, & A Walters. (2022). A framework for automating deployment and evaluation of blockchain networks. https://www.sciencedirect.com/science/article/pii/S1084804522001102

Oghenekome Urefe, Theodore Narku Odonkor, & Edith Ebele Agu. (2024). Innovative financial strategies for achieving cost reduction and revenue growth in non-profit organizations. In International Journal of Scholarly Research and Reviews. https://srrjournals.com/ijsrr/content/innovative-financial-strategies-achieving-cost-reduction-and-revenue-growth-non-profit

Orestis Papageorgiou, Lasse Börtzler, Egor Ermolaev, Jyoti Kumari, & Johannes Sedlmeir. (2024). What Blocks My Blockchain’s Throughput? Developing a Generalizable Approach for Identifying Bottlenecks in Permissioned Blockchains. In ArXiv. https://arxiv.org/abs/2404.02930

P Hegde & G de Veciana. (2022). Performance and efficiency tradeoffs in blockchain overlay networks. https://dl.acm.org/doi/abs/10.1145/3492866.3549730

P Jacobetty & K Orton-Johnson. (2023). Blockchain imaginaries and their metaphors: Organising principles in decentralised digital technologies. In Social Epistemology. https://www.tandfonline.com/doi/abs/10.1080/02691728.2022.2086086

Paolo Bacchiega, Davide Rusconi, Paolo Mereghetti, & F. Fontana. (2024). Refactoring of a Microservices Project Driven by Architectural Smell Detection. In 2024 IEEE 21st International Conference on Software Architecture Companion (ICSA-C). https://ieeexplore.ieee.org/document/10628266/

PG Lopez, A Montresor, & A Datta. (2019). Please, do not decentralize the Internet with (permissionless) blockchains! https://ieeexplore.ieee.org/abstract/document/8885359/

R Belchior, A Vasconcelos, & S Guerreiro. (2021). A survey on blockchain interoperability: Past, present, and future trends. https://dl.acm.org/doi/abs/10.1145/3471140

R. Srivastav, D. Agrawal, & A. Shrivastava. (2020). A Survey on Vulnerabilities and Performance Evaluation Criteria in Blockchain Technology. In ADCAIJ: Advances in Distributed Computing and Artificial Intelligence Journal. https://www.semanticscholar.org/paper/9d0a7a4541331ca4340fb715463e59f19e8584cf

Robert Antwi, J. Gadze, E. T. Tchao, A. Sikora, H. Nunoo‐Mensah, A. S. Agbemenu, K. Agyekum, Justice Owusu Agyemang, Dominik Welte, & Eliel Keelson. (2022). A Survey on Network Optimization Techniques for Blockchain Systems. In Algorithms. https://www.mdpi.com/1999-4893/15/6/193

RV Rosa & CE Rothenberg. (2018). Blockchain-based decentralized applications for multiple administrative domain networking. https://ieeexplore.ieee.org/abstract/document/8515146/

Ryohei Banno, Y. Kitagawa, & Kazuyuki Shudo. (2021). Exploiting semi-structured overlay networks in blockchain systems. In IEICE Communications Express. https://www.semanticscholar.org/paper/cff82ac6b8d3c92a223880ccd90a7cb53e2598ff

S. Alqahtani & M. Demirbas. (2021). Bottlenecks in Blockchain Consensus Protocols. In 2021 IEEE International Conference on Omni-Layer Intelligent Systems (COINS). https://ieeexplore.ieee.org/document/9524210/

S Brotsis, K Limniotis, G Bendiab, & N Kolokotronis. (2021). On the suitability of blockchain platforms for IoT applications: Architectures, security, privacy, and performance. In Computer Networks. https://www.sciencedirect.com/science/article/pii/S1389128621001225

S Janin, K Qin, & A Mamageishvili. (2020). Filebounty: Fair data exchange. https://ieeexplore.ieee.org/abstract/document/9229692/

S Jiang & J Wu. (2023). Approaching an optimal bitcoin mining overlay. In IEEE/ACM Transactions on Networking. https://ieeexplore.ieee.org/abstract/document/10032122/

S Jiang, Y Li, S Wang, & L Zhao. (2022). Blockchain competition: The tradeoff between platform stability and efficiency. In European Journal of Operational Research. https://www.sciencedirect.com/science/article/pii/S0377221721004598

S. Olabanji, O. O. Olaniyi, & O. Olagbaju. (2024). Leveraging Artificial Intelligence (AI) and Blockchain for Enhanced Tax Compliance and Revenue Generation in Public Finance. In Asian Journal of Economics, Business and Accounting. https://www.semanticscholar.org/paper/2b2c9ccc7ba6ca8a63bbb863728f59dd93c83da9

S Onalo, D Gc, & E Pfluegel. (2020). Virtual private blockchains: security overlays for permissioned blockchains. http://eprints.kingston.ac.uk/id/eprint/47782/

S Pattanayak, M Ramkumar, & M Goswami. (2024). Blockchain technology and supply chain performance: The role of trust and relational capabilities. https://www.sciencedirect.com/science/article/pii/S0925527324000550

Sami Ben Mariem. (2019). Master thesis : Vivisecting Blockchain P2P Networks. https://www.semanticscholar.org/paper/8a48c6fa4557c591e3cd742fba594cdd5615d0a1

Shohreh Radrahimi & Reza Tavoli. (2018). The revenue based on the blockchain technology platform. https://www.semanticscholar.org/paper/41d05fe7877a62ec00442429c147048f1859f507

Souhail Mssassi & Anas Abou El Kalam. (2024). The Blockchain Trilemma: A Formal Proof of the Inherent Trade-Offs Among Decentralization, Security, and Scalability. In Applied Sciences. https://www.mdpi.com/2076-3417/15/1/19

Stefano Ferretti & Gabriele D’Angelo. (n.d.). blockchain structure: A complex networks theory perspective. https://www.semanticscholar.org/paper/5d36b2cde3603c91ed532b6cb11aaf68c2d1d003

Swati Jadhav, Vaibhavi Bhosale, Gauri Choudhari, Rishita Bura, & Manasi Bhavik. (2024). DDoS Attack Detection in Blockchain Networks. In 2024 5th International Conference on Data Intelligence and Cognitive Informatics (ICDICI). https://ieeexplore.ieee.org/document/10810961/

T. Hardjono, A. Lipton, & A. Pentland. (2018). Towards a Design Philosophy for Interoperable Blockchain Systems. In ArXiv. https://www.semanticscholar.org/paper/dfc4d6734f64d6e74a8d4cfc5917240554c00b54

Terje Haugum, Bjorn Hoff, Mohammed Alsadi, & Jingyue Li. (2022). Security and Privacy Challenges in Blockchain Interoperability - A Multivocal Literature Review. In Proceedings of the 26th International Conference on Evaluation and Assessment in Software Engineering. https://www.semanticscholar.org/paper/52e97e6ea6431473c8eecb1fb5aca6b2691da436

Tuulikki Hakkarainen, Anatoli Colicev, & T. Pedersen. (2024). A perspective on three trade‐offs of blockchain technology for the global strategy of the MNC. In Global Strategy Journal. https://www.semanticscholar.org/paper/fc55c89998be553b5b463a09e849db6f888f3907

U Gallersdörfer & F Matthes. (2020). Towards valid use cases: Requirements and supporting characteristics of proper blockchain applications. https://ieeexplore.ieee.org/abstract/document/9143999/

Uwe Roth. (2019). Proof of file access in a private P2P network using blockchain. In ArXiv. https://www.semanticscholar.org/paper/664b22f812dee92f854ddaed1823d228a36e0281

V Aradhya, S Gilbert, & A Hobor. (2022). OverChain: Building a robust overlay with a blockchain. In arXiv. https://arxiv.org/abs/2201.12809

V Aradhya, S Gilbert, & A Hobor. (2023). Robust Overlays Meet Blockchains: On Handling High Churn and Catastrophic Failures. https://link.springer.com/chapter/10.1007/978-3-031-44274-2_15

V. Kustov, Grokhotov Aleksey, Beksaev Nikolay, Selanteva Ekaterina, & Renjith V. Ravi. (2022). Three Sources of Blockchain Technology Vulnerabilities - how to Deal with them? In 2022 Second International Conference on Computer Science, Engineering and Applications (ICCSEA). https://ieeexplore.ieee.org/document/9936330/

Vijeth Aradhya, Seth Gilbert, & Aquinas Hobor. (2021). A Partition Resilient Overlay Network via Blockchain. https://www.semanticscholar.org/paper/2690abac0689d17a647cd6c69a50a20ab95cd08c

Vincent Chia, P. Hartel, Qingze Hum, Sebastian Ma, G. Piliouras, Daniël Reijsbergen, M. V. Staalduinen, & Pawel Szalachowski. (2018). Rethinking Blockchain Security: Position Paper. In 2018 IEEE International Conference on Internet of Things (iThings) and IEEE Green Computing and Communications (GreenCom) and IEEE Cyber, Physical and Social Computing (CPSCom) and IEEE Smart Data (SmartData). https://ieeexplore.ieee.org/document/8726738/

Vivisecting Blockchain P2P Networks. (2019). https://www.semanticscholar.org/paper/6b99ace63c121795fcef6668a222bbd734d79a90

W Gao, WG Hatcher, & W Yu. (2018). A survey of blockchain: Techniques, applications, and challenges. https://ieeexplore.ieee.org/abstract/document/8487348/

W Viriyasitavat, L Da Xu, & Z Bi. (2019). Blockchain technology for applications in internet of things—mapping from system design perspective. https://ieeexplore.ieee.org/abstract/document/8752029/

Wessel Reijers, Fiachra O’Brolcháin, & P. Haynes. (2016). Governance in Blockchain Technologies & Social Contract Theories. In Ledger. https://www.semanticscholar.org/paper/01f08210264ee1f338a86e5c95a00d7531c83fe2

X Xu, C Pautasso, L Zhu, & V Gramoli. (2016). The blockchain as a software connector. https://ieeexplore.ieee.org/abstract/document/7516828/

Xiaonan You, Shengli Zhang, Taotao Wang, & S. Liew. (2024). Hyperclique: A Novel P2P Network Structure for Blockchain Systems. In 2024 International Conference on Computing, Networking and Communications (ICNC). https://ieeexplore.ieee.org/document/10556310/

Y Xiao, N Zhang, W Lou, & YT Hou. (2020). A survey of distributed consensus protocols for blockchain networks. https://ieeexplore.ieee.org/abstract/document/8972381/

Y Zhu, C Hua, D Zhong, & W Xu. (2022). Design of low-latency overlay protocol for blockchain delivery networks. https://ieeexplore.ieee.org/abstract/document/9771715/

Yean-Fu Wen & Ping-Ju Wu. (2019). Blockchain Synchronisation Performance Enhancement Using Forwarder Assignment in an Overlay Network. In 2019 IEEE 5th International Conference on Big Data Intelligence and Computing (DATACOM). https://ieeexplore.ieee.org/document/10669542/

Yongtao Huang, I-Ling Yen, & F. Bastani. (2024). Collaborative Access Control for IoT - A Blockchain Approach. In 2024 IEEE International Conference on Blockchain and Distributed Systems Security (ICBDS). https://ieeexplore.ieee.org/document/10837489/

YY Wang, F Tao, & J Wang. (2022). Information disclosure and blockchain technology adoption strategy for competing platforms. In Information & Management. https://www.sciencedirect.com/science/article/pii/S037872062100080X

Zubaida Rehman, Mark A. Gregory, I. Gondal, Hai Dong, & Mengmeng Ge. (2025). Eclipse Attacks in Blockchain Networks: Detection, Prevention, and Future Directions. In IEEE Access. https://ieeexplore.ieee.org/document/10872918/



Generated by Liner
https://getliner.com/search/s/5926611/t/85557830