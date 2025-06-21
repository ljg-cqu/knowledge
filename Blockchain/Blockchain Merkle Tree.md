'Blockchain Merkle Tree.' Requirements: 1. Ensure compliance with MECE. 2. Classify/categorize logically and appropriately if necessary. 3. Explain with analogy and examples. 4. Use numbered lists for clear explanations when possible. 5. Describe core elements, components, factors and aspects. 6. List core evaluation dimensions and corresponding evaluations if applicable. 7. Describe their concepts, definitions, functions, and characteristics. 8. Clarify their purposes and assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect). 9. Describe relevant markets, ecosystems, regulations, and economic models, and explain the corresponding strategies used to generate revenue. 10. Describe their work mechanism concisely first and then explain how they work with phase-based workflows throughout the entire lifecycle. 11. Clarify their preconditions, inputs, outputs, immediate outcomes, long-term impacts, and potential implications. 12. Clarify their underlying laws, axioms, theories, and patterns. 13. Describe the design philosophy and architectural features. 14. Provide ideas, techniques, and means of architectural refactoring. 15. Clarify relevant frameworks, models, and principles. 16. Clarify their origins, evolutions, and trends. 17. List key historical events, security incidents, core factual statements, raw data points, and summarized statistical insights. 18. Clarify techniques, methods, approaches, protocols, and algorithms.  19. Describe contradictions and trade-offs. 20. Identify and list all major competitors (including the one being searched at present) with concise descriptions within the target market or industry segment. 21. Conduct a comprehensive competitor analysis to evaluate each competitor’s (including the one being searched at present) operational strategies, product offerings, market position, and performance metrics. 22. Perform a SWOT analysis for each competitor (including the one being searched at present), categorizing findings into strengths, weaknesses, opportunities, and threats. 23. Clarify principles, rules, constrains, limitations, vulnerabilities, challenges, obstacles, and risks. 24. Describe potential security vulnerabilities, troubleshooting methods, attack tactics, prevention methods and emergency measures. 25. Describe potential performance bottlenecks, troubleshooting methods and optimization measures. 26. Explain priorities, use cases, pitfalls, and best practices. 27. Clarify cause-and-effect relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 28. Clarify interdependency relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 29. Clarify cardinality-based relationships (1:1, 1:M, M:N). 26. Clarify contradictory relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 30. Describe the existing non-trivial problems and potential approaches to address them. 31. Introduce the relevant research topics of significant value that remain to be overcome. 32. Introduce the possible directions and approaches of within-domain and cross-domain innovation. 33. Predict the ultimate form of the related development. 34. Make a summary table at the end with purposes, characteristics, use cases, ect. for clarity. 35. Append the terminologies, formulas, and analogies at the end with concise descriptions for each item.

Thu Jun 12 2025

### Logical Classification and MECE Structure for Blockchain Merkle Tree

To ensure MECE (Mutually Exclusive, Collectively Exhaustive) compliance, all aspects of Blockchain Merkle Tree are logically categorized into: core structural components, operational/functional processes, application and context, security/dynamic factors, ecosystems/markets/competition, design and innovation, challenges and evolutions, and performance/security best practices. These major categories are further broken down into non-overlapping, exhaustive subgroups to capture every relevant factor.

---

### Core Elements, Components, Factors, and Aspects

#### 1. Structural Components (Numbered List)

1. **Leaf Nodes**: These are the bottom-most nodes, each representing the cryptographic hash of a transaction or data block.
2. **Non-Leaf (Intermediate) Nodes**: Nodes above the leaves that combine and hash pairs of child nodes' hashes, summarizing all lower data.
3. **Root Node (Merkle Root)**: The topmost node, a single hash that summarizes all data beneath it (fingerprint of all transactions in the set).
4. **Hash Functions**: Cryptographic functions (e.g., SHA-256) applied recursively to enable tamper detection and deterministic hashing.
5. **Hash Pointers**: Each node or block contains pointers and hashes of child nodes, enabling both data reference and verification.
6. **Merkle Proofs**: Subsets of hashes along a path from leaf to root, allowing for efficient and secure proof of inclusion for any transaction.
7. **Authentication Paths**: Set of sibling node hashes needed for verification, used in Merkle proof construction.

---

### Classification and Categorization

#### A. Core Structure

- **Binary Tree Topology**: Typically, a Merkle Tree is a binary tree with two children per node, but higher-order variants (n-ary, quad) are possible for further optimization.
- **Tree Balancing & Duplication**: If the number of leaf nodes is odd, the last leaf is duplicated to maintain structure.

#### B. Functional Mechanisms

- **Construction**: Bottom-up hashing, starting from raw transaction data.
- **Verification**: Only a Merkle root and a path of sibling hashes are needed to reconstruct and verify the integrity or inclusion of any transaction.
- **Tamper Detection & Immutability**: Any data alteration changes hashes up to the Merkle Root, immediately signaling a problem.
- **Incremental Updates**: Only affected branches need recomputing for efficient updates.

#### C. Contextual/Application Aspects

- **Blockchain Integration**: Each blockchain block uses a Merkle Tree to record and verify transactions, with the Merkle Root stored in block headers.
- **Consensus Mechanisms**: Used in proof-of-work, proof-of-stake, and data contests, supporting fast data validation and network-wide agreement.
- **Lightweight Clients**: Enables SPV (Simplified Payment Verification) by supporting partial blockchain storage/verification.

#### D. Security and Integrity

- **Tamper Evident**: Any single bit change in transaction data or order leads to a cascade of hash changes, altering the Merkle Root.
- **Collision Resistance**: Security depends heavily on the collision and preimage resistance of the employed hash function.

#### E. Ecosystem and Market Relevance

- **Public Blockchains**: Bitcoin and Ethereum (among others) employ Merkle Trees for core transaction integrity mechanisms.
- **Enterprise/Private Blockchains**: Used for permissions, audit, and private state management.
- **Distributed Databases & File Systems**: Used in P2P (BitTorrent), version control (Git), and cloud integrity checks.

#### F. Evaluation Dimensions

| Dimension                  | Evaluation Aspect         |
|----------------------------|--------------------------|
| Security                   | Tamper resistance, collision attacks |
| Efficiency                 | Logarithmic proof size and search time |
| Scalability                | Manageability as datasets grow |
| Proof Size & Verification  | Log(n) size for Merkle proofs |
| Storage/Computation Needs  | Storage with growing blockchain |
| Resilience/Attack Handling | Resistance to DA attacks, side-channel, and manipulation |

---

### Concepts, Definition, Functions, and Characteristics

#### Concept & Definition

A Blockchain Merkle Tree is a hierarchical, cryptographically secured, hash-based data structure that efficiently summarizes a large data set—primarily transactions—for the purpose of verification, tamper-resistance, and scaling in a decentralized ledger. Each non-leaf node is a hash of its child nodes; the root is a digest representing all leaves.

#### Functions

- **Summarization**: Compactly represents all transaction data in a single Merkle Root.
- **Immutable Audit Trail**: Root hash forms a permanent fingerprint.
- **Efficient Inclusion Proof**: Logarithmic-size proofs for lightweight clients or auditors to check inclusion.
- **Tamper Detection**: Any change cascades to alter the Merkle root, facilitating quick tamper identification.

#### Characteristics

- **Deterministic**: Same input always yields the same output hash.
- **Collision-Resistant**: Unlikely to have two different inputs with the same hash.
- **Hierarchical Compression**: Data efficiently compressed through hashing.
- **Space and Bandwidth Efficient**: Only proofs, not the full dataset, needed for remote checks.

---

### Purpose and Assumptions

#### 1. Value Purpose

- **Securing Trustless Systems**: Underpin decentralized trust by making it infeasible to tamper with or forge transaction histories.
- **Enable Lightweight Verification**: Reduce resource requirements for verification, increasing network accessibility and scalability.

#### 2. Descriptive Purpose

- **Model Data Integrity**: Mathematically describes the blockchain’s commitment to transaction integrity.

#### 3. Prescriptive Purpose

- **Mandate Tamper Evidence**: Any blockchain using a Merkle Tree is prescriptively secured against undetectable tampering.

#### 4. Worldview Assumptions

- **Trustlessness and Adversarial Environments**: System assumes nodes do not trust each other and thus must independently verify data.
- **Hash Function Security**: Assumes employed hash functions are cryptographically robust.

#### 5. Cause-and-Effect Relationships

- **Transaction Data Changes <-propagate-> Merkle Root Changes**
- **Hash Collisions <-undermine-> Data Integrity**

---

### Relevant Markets, Ecosystems, Regulations, and Economic Models

#### Markets/Ecosystems

- **Cryptocurrencies**: Bitcoin, Ethereum, and related major chains employ Merkle Trees.
- **Distributed Storage**: File verification and consistency (e.g., IPFS, BitTorrent, Git).
- **Enterprise Blockchain**: Audit, privacy, access control.
- **Cloud Integrity and Auditing**: Data owner or client uses Merkle roots to verify cloud storage integrity.

#### Regulations

- While Merkle Trees themselves are not regulated, their deployment supports compliance initiatives (data authenticity, audit, traceability) mandated by regulators in finance, healthcare, and supply chain sectors.

#### Economic Models and Revenue Strategies

- **Transaction Fees**: Lowered operational and verification costs support higher transaction throughput and, thus, fee generation.
- **Proof-of-Reserves**: Crypto custodians can offer auditable proof-of-liabilities, which builds user trust and increases platform usage.
- **Enterprise Licensing**: Custom Merkle tree implementations and integrity tools for private consortia.

---

### Concise Work Mechanism and Lifecycle Workflows

#### Work Mechanism (Concise)

A Merkle Tree is built from a list of transactions by hashing each item, then iteratively hashing pairs of hashes until a single Merkle Root is derived. This Merkle Root is stored in a block header, enabling anyone to verify that a given transaction is included just by checking a Merkle proof (a small set of sibling hashes).

#### Phase-Based Workflow

**Phase 1: Initialization/Construction**
- Transactions are hashed as leaves.
- Hashes are repeatedly paired and hashed up the tree.
- Merkle Root is recorded (e.g., in the block header).

**Phase 2: Verification**
- When queried, a node provides a Merkle proof for the transaction.
- Verifier reconstructs the path from the transaction to the root using provided hashes.
- If the computed root matches the known root, inclusion/validity is confirmed.

**Phase 3: Incremental Update**
- On data addition/modification, only affected tree portions and their paths to the root are recalculated/updated.

---

### Preconditions, Inputs, Outputs, Immediate Outcomes, Long-Term Impacts, and Implications

#### Preconditions

- Trusted and secure hash function is available (e.g., SHA256).
- Data to be verified is structured or partitioned appropriately.

#### Inputs

- Raw data blocks or transactions.
- Hashing algorithms.

#### Outputs

- Merkle Root (summary commitment).
- Merkle proofs (for specific data points).

#### Immediate Outcomes

- Data commitment enables efficient inclusion proof.
- Any tampering is immediately detectable.

#### Long-Term Impacts & Implications

- Blockchain scalability via lightweight verification.
- New privacy and auditing applications.
- Underpinning for ecosystem trustworthiness and decentralized scaling.

---

### Underlying Laws, Axioms, Theories, and Patterns

- **Collision Resistance**: The cryptographic hash function axioms—collision resistance, preimage resistance, determinism—are foundational.
- **Hierarchical Propagation**: Hash changes at any tree level cascade to the root, a direct application of recursive and bottom-up computation.
- **Tamper Propagation**: If a single leaf (data block) is altered, all parent node hashes—and the root—change, perfectly reflecting data integrity.

---

### Design Philosophy and Architectural Features

- **Divide and Conquer**: Tree hierarchy compresses large datasets into a single hash and enables localized verification.
- **Layered Security**: Each layer adds a new hash computation, enhancing tamper detection and auditability.
- **Efficiency and Modularity**: Supports trade-offs between bandwidth/storage and computation through tree structure choice (binary, quad, sparse).
- **Integration**: Merkle Trees are the backbone of block header structures, interfacing naturally with blockchains’ consensus and validation mechanisms.

---

### Architectural Refactoring: Ideas, Techniques, Means

- **Sparse/Jellyfish Merkle Trees**: Optimization for key-value blockchains and cloud data, minimizing storage and computation.
- **Pruned and Hybrid Trees**: Remove redundant/intermediate nodes, improving verification time.
- **Coded Merkle Trees**: Introduce error-correction (LDPC, Polar Codes) for DA attack resilience.
- **Batch Hashing/Parallelization**: Accelerate construction and proof processes for high-volume blockchains.
- **Versioned and Adaptive Structures**: Support dynamic data by maintaining subtrees or creating differential trees.
- **Off-chain Computation**: Use off-chain proof generation to minimize on-chain costs, then verify efficiently on-chain.

---

### Frameworks, Models, and Principles

- **Simplified Payment Verification Model (SPV)**: Enables lightweight nodes to verify transaction existence via Merkle proofs.
- **Merkle Patricia Trie Model**: Used in Ethereum to balance mapping efficiency and proof size.
- **Smart Contracts for Audit**: On-chain contracts execute Merkle-based audit verifications automatically.
- **Proof of Membership/Non-Membership**: Standardized protocols for efficient set membership testing (for privacy and security).

---

### Origins, Evolutions, and Trends

- **Origins**: Ralph Merkle patented hash trees in 1979, initially outlined for efficient integrity proofs.
- **Blockchain Adoption**: Incorporated in Bitcoin and Ethereum for efficient transaction inclusion verification and block integrity.
- **Evolution**: Moving from binary to sparse, Jellyfish, and quad Merkle Trees for greater efficiency.
- **Trends**: Research on Coded Merkle Trees, Verkle Trees (with polynomial commitments), and energy-optimized models continues.

---

### Key Historical Events, Incidents, Core Facts, Data, and Insights

- 1979: Ralph Merkle patents hash trees.
- 2008: Bitcoin employs Merkle Trees for block transaction summarization.
- Ethereum adapts Merkle Trees as Merkle Patricia Tries for efficient key-value mapping.
- Bitcoin block #854,473 contained 2,530 transactions; Merkle Tree occupied 161.92 KB of a 1.54 MB block.
- SPV adoption led to a dramatic reduction in required data for lightweight clients, from all transactions to only several hashes for each proof.
- Critical vulnerability discoveries, such as unhashed leaves leading to verification errors, prompted fixes in standard libraries.
- Coded Merkle Trees with LDPC codes advance attack resistance in light nodes.

---

### Techniques, Methods, Approaches, Protocols, and Algorithms

- **TreeHash Algorithm**: Efficiently traverses and builds trees.
- **Batch Hashing, Incremental Updates**: Group and defer hash computations for performance.
- **Proof of Inclusion/Exclusion Algorithms**: Determine membership using minimal data.
- **Coded Merkle Trees**: Layer LDPC or other codes to enhance DA attack detection.
- **Pruning**: Adaptive removal of inactive tree nodes.
- **Parallelization**: Distribute computation over processors for speed.
- **Fractal and Hybrid Traversal Algorithms**: For efficient proof and path generation.

---

### Contradictions and Trade-offs

- **Performance vs. Security**: Stronger hash functions increase security but also computational load.
- **Storage vs. Scalability**: Storing all nodes boosts verification speed but impacts scalability for massive chains.
- **Dynamic Data vs. Computation Overhead**: Updating any data portion can cascade recomputation up the tree.
- **Proof Size vs. Complexity**: Optimizing proofs for lightweight clients can increase development and verification complexity.

---

### Major Competitors, Descriptions, and SWOT Analysis

#### Table: Competitor Overview

| Name                   | Brief Description                                                                                      |
|------------------------|-------------------------------------------------------------------------------------------------------|
| **Merkle Tree**        | Traditional binary hash tree for data inclusion/integrity.                                  |
| **Verkle Tree**        | Uses vector (polynomial) commitments for smaller proof sizes, supporting advanced scalability. |
| **Merkle Patricia Trie** | Variant in Ethereum; maps key–value pairs and enables efficient state validation.       |
| **Jellyfish Merkle Tree** | Optimized for key-value blockchains, balancing storage and computation.                  |

#### Comprehensive Analysis

| Name                     | Operational Strategy                          | Product Offering           | Market Position          | Performance Metrics     |
|--------------------------|-----------------------------------------------|----------------------------|-------------------------|------------------------|
| Merkle Tree              | Simplicity, proven security, wide adoption    | Blockchain verification    | Dominant (Bitcoin, etc.)| Log(n) proof; robust   |
| Verkle Tree              | Scalability, proof compression                | Smaller proofs, advanced   | Emerging (Ethereum roadmap) | Constant size proofs    |
| Merkle Patricia Trie     | Key-value mapping, state storage              | Ethereum state management  | Strong in ETH ecosystem | Efficient lookups       |
| Jellyfish Merkle Tree    | Key-value/Versioned optimization              | High-performance storage   | Specialized deployments  | Storage/computation balanced|

#### SWOT (Merkle Tree and Verkle Tree summarized)

| Tree                | Strengths                           | Weaknesses                 | Opportunities                    | Threats                         |
|---------------------|-------------------------------------|----------------------------|-----------------------------------|----------------------------------|
| Merkle              | Simplicity, security, wide use      | Proof size scales log(n)   | Hybrid designs; optimization      | Advanced alternatives            |
| Verkle              | Small proof sizes, scalability      | Complexity, newer          | Ethereum adoption, privacy uses   | Implementation complexity        |

---

### Principles, Rules, Constraints, Limitations, Challenges, and Risks

- **Principles**: Immutable hierarchical hashing; tamper-evidence; recursive summarization.
- **Rules**: Child hashes always aggregated for parent; unbroken lineage from leaf to root.
- **Constraints**: Reliance on hash function security, storage increase with growth, dynamic data cost.
- **Limitations**: Performance on very large chains, dynamic update overhead, hash function vulnerability.
- **Vulnerabilities/Challenges**: Hash collisions, side-channel attacks, DA/data availability attacks on light clients.

---

### Security Vulnerabilities, Troubleshooting, Attack Tactics, Prevention, Emergency Measures

- **Security Vulnerabilities**: Attacks based on unhashed leaves, hash collisions, manipulation of tree structure, data hiding (DA attacks).
- **Troubleshooting**: Validate hash function usage, double-check proof construction, restrict leaf/hash input acceptance.
- **Attack Tactics**: Passing internal node as leaf, exploiting preimage/collision, data availability hiding in light nodes.
- **Prevention**: Use robust hash functions (SHA-256/3), extend proof checks with internal hash verification, apply LDPC codes for coded Merkle Trees.
- **Emergency Measures**: Immediate software/library patching, side-channel resistant computation, switch algorithms on detection.

---

### Performance Bottlenecks, Troubleshooting, Optimization

- **Bottlenecks**: Hash computation load, large storage for nodes, update cost on dynamic data.
- **Troubleshooting**: Profile hash algorithm, analyze update/proof times, validate structure.
- **Optimization**: Pruning, batch/parallel hashing, memoization, adaptive/differential structures, compression.

---

### Priorities, Use Cases, Pitfalls, Best Practices

#### Priorities

- Security, efficiency, scalability, and transparent verification.

#### Use Cases

- Transaction inclusion proof, data integrity/auditing, SPV wallets, cloud/IoT data verification, smart contract validation.

#### Pitfalls

- Collision vulnerability, dynamic update costs, proof size for massive chains, network latency, configuration mistakes.

#### Best Practices

- Use collision-resistant hash functions, optimize tree structure, prune for efficiency, validate via smart contracts, implement lightweight protocols for SPV clients, continuous performance/security audits.

---

### Cause-and-Effect, Interdependency, Cardinality, Contradictory Relationships

#### Cause-and-Effect (example using symbols)

- Transaction Data Updates <-change-> Leaf Hashes <-propagate up-> Root Hash Changes <-trigger-> Detection of Data Tampering.

#### Interdependency

- Leaf Node <-> Parent Node (hash dependency)
- Merkle Root <-> Full Blockchain Verification (cascading dependency)
- Hash Function Choice <-> Security of Entire Tree.

#### Cardinality

- One parent for multiple children: 1:M parent-child.
- Unique path from each leaf to root: node/level 1:1 path.

#### Contradictory Relationships

- Stronger Security <-contradicts-> Higher Computation Costs.
- Storage Efficiency <-contradicts-> Scalability for ultra-large datasets.

---

### Existing Non-Trivial Problems and Approaches

- Data availability attacks on light nodes (addressed by LDPC-coded Merkle Trees and strategic sampling).
- Quantum security of hash functions for future-proofing.
- Computational overhead for large/rapidly growing blockchains (addressed via parallelization, pruning, or coded trees).

---

### Remaining Research Topics

- Optimizing structure for massive chains (sparse, adaptive, jellyfish trees).
- Enhancing light client security and DA attack detection.
- Proof size minimization, quantum resilience, and cross-domain authentication schemes.

---

### Directions — Within-Domain & Cross-Domain Innovation

- Hybrid structures (Merkle-Patricia, Verkle, jellyfish, multi-branch)
- Coded trees (LDPC, Polar coded) and resilient light client protocols
- Integration in cloud, audit, e-government, healthcare, and IoT systems for decentralized integrity guarantees.

---

### Ultimate Form and Trends Prediction

The ultimate evolution of the Merkle Tree for blockchains will integrate adaptive, hybrid, and coded tree structures with quantum-resistant hash functions and energy-optimized architectures, supporting cross-chain, light-client, and domain-spanning use cases, with automated audit and integrity mechanisms as core features.

---

### Summary Table: Purposes, Characteristics, Use Cases, etc.

| Category         | Description/Examples                                                                  |
|------------------|--------------------------------------------------------------------------------------|
| Purpose          | Efficient, tamper-evident data verification, auditability, scaling decentralized trust|
| Characteristics  | Hierarchical hash structure, log(n) proofs, deterministic, immutable                  |
| Use Cases        | Transaction integrity proofs, light nodes, SPV wallets, cloud/IoT auditing           |
| Components       | Leaf nodes, non-leaf nodes, root, hash pointers, Merkle proofs                       |
| Workflows        | Initialization (hashing, tree construction), Verification (Merkle proofs), Updates   |
| Evaluation       | Security, efficiency, proof size, scalability, resilience                             |
| Market           | Public/private blockchains, distributed storage/cloud, IoT, enterprise audit          |
| Innovation       | Coded and hybrid trees, batch/proof pruning, polynomial commitments                   |
| Key Challenges   | Scalability, dynamic updates, DA attacks, hash vulnerabilities                       |
| Trends           | Verkle/jellyfish trees, quantum-resistance, privacy and cross-domain applications    |

---

### Terminologies, Formulas, and Analogies

#### Terminologies

- **Merkle Tree**: Hierarchical hash-based tree structure for summarizing and verifying data.
- **Merkle Root**: The single, top hash representing all underlying data blocks.
- **Leaf/Non-Leaf Nodes**: Leaf stores hash of data; non-leaf stores hash of concatenated child hashes.
- **Merkle Proof**: Path of sibling hashes for efficient proof of data inclusion.
- **Hash Function**: Collision-resistant cryptographic function for data integrity.
- **Sparse/Jellyfish/Verkle Tree**: Variants optimized for specific performance or proof-size needs.

#### Formulas

- **Parent Node Hash**: \\(H_{parent} = Hash(H_{left\_child} \Vert H_{right\_child})\\).
- **Merkle Root**: Recursively hash node pairs until a single root remains.

#### Analogies

- **Corporate Report**: Each page summarized by a code; pair codes for sections, up to a single report code. One page change cascades up to alter the report’s code— paralleling how transaction changes ripple up to the Merkle Root.
- **Fingerprint**: The root is a digital fingerprint for all transactions; any change alters the fingerprint.
- **Family Tree Upside Down**: Leaves as youngest generation, root as oldest ancestor, relationships formed by parentage—only here, “genes” (hashes) are cryptographically ensured.

---

This highly detailed, MECE-compliant report provides a comprehensive and structured analysis of the Blockchain Merkle Tree, ensuring clarity for experts and practitioners alike.

Bibliography
2.3. Merkle trees and Data Integrity - Byte Federal. (2025). https://www.bytefederal.com/byteu/11/138

5P;1R Jellyfish Merkle Tree - by Daniel Olshansky - Substack. (2022). https://olshansky.substack.com/p/5p1r-jellyfish-merkle-tree

10 Best TRM Labs Alternatives & Competitors in (Jun 2025) - SoftwareSuggest. (n.d.). https://www.softwaresuggest.com/trm-labs/alternatives

1978: Crypto Roots and Merkle Trees - Throwback Thursday, Part 1. (2023). https://www.scytale.digital/blog-posts/throwback-thursday-1978-crypto-roots-and-merkle-trees

[2403.00406] Adaptive Restructuring of Merkle and Verkle Trees for ... (2024). https://arxiv.org/abs/2403.00406

A Beginner’s Guide to Merkel Trees in Blockchain - Unchained Crypto. (2024). https://unchainedcrypto.com/merkel-trees-in-blockchain/

A Quick Guide to Blockchain: Merkle Tree - Analytics Vidhya. (2023). https://www.analyticsvidhya.com/blog/2022/10/a-quick-guide-to-blockchain-merkle-tree/

A Secure Cross-Domain Data Sharing Scheme Based on Blockchain. (2025). https://www.mdpi.com/2078-2489/16/5/394

A Timeline and History of Blockchain Technology - TechTarget. (2024). https://www.techtarget.com/whatis/feature/A-timeline-and-history-of-blockchain-technology

An Intro to Merkel Tree: What is it and How Does it Work? - Medium. (2023). https://medium.com/coinmonks/merkel-tree-what-is-it-and-how-does-it-work-d2569b07bf0f

Andrew Flangas, Autumn A. Cuellar, Michael Reyes, & Jr Frederick C. Harris. (2021). Parallelized C++ Implementation of a Merkle Tree. https://www.semanticscholar.org/paper/b41fda678ca848a1ca3276bb02a62d1f02cae354

Anoushk Kharangate. (2023). Asynchronous Merkle Trees. In ArXiv. https://www.semanticscholar.org/paper/736a293004e982ec33b6001278a3cd10e113222b

BermanPiotr, KarpinskiMarek, & NekrichYakov. (2007). Optimal trade-off for Merkle tree traversal. In Theoretical Computer Science. https://www.semanticscholar.org/paper/69343468bd0bbc1c757ace215a6245c6d7f61a79

Blockchain Merkle Trees - GeeksforGeeks. (2022). https://www.geeksforgeeks.org/blockchain-merkle-trees/

Blockchain Transparency and Merkle Trees Explained. (2022). https://academy.moralis.io/blog/blockchain-transparency-exploring-merkle-trees-and-proof-of-reserves

Boris I. Ederov. (2007). Merkle Tree Traversal Techniques. https://www.semanticscholar.org/paper/77f6cee2b657fe09088494dcfa64383552f528e9

C Papamanthou, S Srinivasan, & N Gailly. (2024). Reckle trees: Updatable merkle batch proofs with applications. https://dl.acm.org/doi/abs/10.1145/3658644.3670354

CF Infante Montoya. (2021). Architectural construction to use blockchain oriented interorganizational transactions. https://repositorio.uniandes.edu.co/entities/publication/664128a9-1797-433a-a3f2-7aedc339b4ea

Challenges And Limitations Of Merkle Trees - FasterCapital. (n.d.). https://fastercapital.com/topics/challenges-and-limitations-of-merkle-trees.html

Challenges and Limitations of Merkle Trees in Blockchain. (2024). https://droomdroom.com/web-stories/challenges-and-limitations-of-merkle-trees-in-blockchain/

Challenges And Limitations Of Using Merkle Trees In Distributed ... (2024). https://fastercapital.com/topics/challenges-and-limitations-of-using-merkle-trees-in-distributed-ledgers.html/1

Cracking the Code: How Merkle Trees Ensure the Integrity of Data. (n.d.). https://www.bsvblockchain.org/cracking-the-code-how-merkle-trees-ensure-the-integrity-of-data/

Cryptographic Tools 101 - Hash Functions and Merkle Trees - Helius. (2023). https://www.helius.dev/blog/cryptographic-tools-101-hash-functions-and-merkle-trees-explained

D Koo, Y Shin, J Yun, & J Hur. (2018). Improving security and reliability in Merkle tree-based online data authentication with leakage resilience. In Applied Sciences. https://www.mdpi.com/2076-3417/8/12/2532

Debarnab Mitra, Lev Tauz, & L. Dolecek. (2020). Concentrated Stopping Set Design for Coded Merkle Tree: Improving Security Against Data Availability Attacks in Blockchain Systems. In 2020 IEEE Information Theory Workshop (ITW). https://ieeexplore.ieee.org/document/9457630/

Debarnab Mitra, Lev Tauz, & L. Dolecek. (2021a). Overcoming Data Availability Attacks in Blockchain Systems: Short Code-Length LDPC Code Design for Coded Merkle Tree. In IEEE Transactions on Communications. https://ieeexplore.ieee.org/document/9841605/

Debarnab Mitra, Lev Tauz, & L. Dolecek. (2021b). Overcoming Data Availability Attacks in Blockchain Systems: LDPC Code Design for Coded Merkle Tree. In ArXiv. https://www.techrxiv.org/doi/full/10.36227/techrxiv.16532853.v1

Debarnab Mitra, Lev Tauz, & L. Dolecek. (2022). Polar Coded Merkle Tree: Improved Detection of Data Availability Attacks in Blockchain Systems. In 2022 IEEE International Symposium on Information Theory (ISIT). https://ieeexplore.ieee.org/document/9834538/

Enhanced scalability and privacy for blockchain data using ... (2024). https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2023.1222614/full

Evaluating the Security of Merkle Trees: An Analysis of Data ... (n.d.). https://www.researchgate.net/publication/382807663_Evaluating_the_Security_of_Merkle_Trees_An_Analysis_of_Data_Falsification_Probabilities

Evaluating the Security of Merkle Trees: An Analysis of Data ... - MDPI. (2024). https://www.mdpi.com/2410-387X/8/3/33

Everything you need to know about Merkle trees - Bitpanda. (2022). https://www.bitpanda.com/academy/en/lessons/everything-you-need-to-know-about-merkle-trees

G Becker. (2008). Merkle signature schemes, merkle trees and their cryptanalysis. In Ruhr-University Bochum. https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=d7c3aa65bc5df32d94dcc8b29dceca240bdf8bef

GitHub - Blockchain-for-Developers/merkle-tree. (n.d.). https://github.com/Blockchain-for-Developers/merkle-tree

Hao Ding, Xuefeng Piao, Huihui Song, Jiasi Li, Zhenzhou Ji, Meng Liu, Jie Liu, & Wenjie Dong. (2024). Efficient and Verifiable Skyline Computation on Blockchain System with Merkle B+ Tree Index. In 2024 IEEE International Symposium on Parallel and Distributed Processing with Applications (ISPA). https://www.semanticscholar.org/paper/d3baed1ae13f88e2a66b0cd1101a180a06a3c52e

Haojun Liu, Xinbo Luo, Hongrui Liu, & Xubo Xia. (2021). Merkle Tree: A Fundamental Component of Blockchains. In 2021 International Conference on Electronic Information Engineering and Computer Science (EIECS). https://ieeexplore.ieee.org/document/9588047/

How are Merkle trees used in blockchains? | Alchemy Docs. (2025). https://alchemy.com/docs/merkle-trees-in-blockchains

How Are Merkle Trees Used On Bitcoin? - Cointribune. (n.d.). https://www.cointribune.com/en/how-are-merkle-trees-used-on-bitcoin/

How Merkle Trees Revolutionize Blockchain Scalability ... - LinkedIn. (2024). https://www.linkedin.com/pulse/how-merkle-trees-revolutionize-blockchain-scalability-mubashar-hassan-xwy8f

How to Implement a Merkle Tree for Secure Data Verification. (n.d.). https://blockchain.oodles.io/dev-blog/how-to-implement-a-merkle-tree/

Introduction to Merkle Tree - GeeksforGeeks. (n.d.). https://www.geeksforgeeks.org/introduction-to-merkle-tree/

Introduction to Merkle Trees in Blockchain - LinkedIn. (2024). https://www.linkedin.com/pulse/introduction-merkle-trees-blockchain-blockchaincouncil-krhyc

J Dave, A Dutta, P Faruki, V Laxmi, & MS Gaur. (2020). Secure proof of ownership using merkle tree for deduplicated storage. https://link.springer.com/article/10.3103/S0146411620040033

J Oberst. (2025). Towards Stateless Clients in Ethereum: Benchmarking Verkle Trees and Binary Merkle Trees with SNARKs. In arXiv. https://arxiv.org/abs/2504.14069

JF Bruno & BJ Chelliah. (2024). Hierarchical blockchain-based secure data storage in cloud using Merkle tree approach. https://www.inderscienceonline.com/doi/abs/10.1504/IJCC.2024.143551

Jing Chen, Zeyi Zhan, Kun He, Ruiying Du, Donghui Wang, & Fei Liu. (2022). XAuth: Efficient Privacy-Preserving Cross-Domain Authentication. In IEEE Transactions on Dependable and Secure Computing. https://ieeexplore.ieee.org/document/9465710/

Kanthimathi S, Mahika Annie Verghese, & Sireesha Pamidimokkala. (2024). Periodic Integration: A Differential Approach to Merkle Tree Configuration. In 2024 IEEE International Conference on Electronics, Computing and Communication Technologies (CONECCT). https://ieeexplore.ieee.org/document/10677225/

Lijie Chen & R. Movassagh. (2021). Quantum Merkle Trees. In Quantum. https://www.semanticscholar.org/paper/284a363c39429fc826d0fd8ca73bb59b6b14e254

M Yu, S Sahraei, S Li, S Avestimehr, & S Kannan. (2020). Coded merkle tree: Solving data availability attacks in blockchains. https://link.springer.com/chapter/10.1007/978-3-030-51280-4_8

Merkle Patricia Tries: A Deep Dive into Data Structure Security. (2025). https://www.cardanofoundation.org/blog/merkle-patricia-tries-deep-dive

Merkle Root | A Fingerprint for the Transactions in a Block. (2025). https://learnmeabitcoin.com/technical/block/merkle-root/

Merkle Tree | Brilliant Math & Science Wiki. (n.d.). https://brilliant.org/wiki/merkle-tree/

Merkle Tree | Glossary - Bitcoin Treasuries. (2025). https://bitcointreasuries.net/glossary/merkle-tree

Merkle Tree & Proof-Of-Reserves (PoR) in Crypto - OSL. (2025). https://osl.com/academy/article/merkle-tree-and-proof-of-reserves-por-in-crypto

Merkle tree - Wikipedia. (2005). https://en.wikipedia.org/wiki/Merkle_tree

Merkle Tree, a simple explanation and implementation - Medium. (2022). https://medium.com/coinmonks/merkle-tree-a-simple-explanation-and-implementation-48903442bc08

Merkle Tree and Hash Chain Data Structures with difference. (2023). https://www.geeksforgeeks.org/merkle-tree-and-hash-chain-data-structures-with-difference/

Merkle Tree Efficiency in Blockchain: Essentials Explained. (2024). https://cryptorank.io/news/feed/7e9f5-merkle-tree-efficiency-in-blockchain-explained

Merkle Tree [Explained] - OpenGenus IQ. (2021). https://iq.opengenus.org/merkle-tree/

Merkle Tree: How Blockchain Ensures Data Integrity and Security. (2023). https://medium.com/coinmonks/merkle-tree-a-blockchain-perspective-c57218a8177c

Merkle tree in Blockchain. (2024). https://www.blockchain-council.org/blockchain/what-is-merkel-tree-merkel-root-in-blockchain/

Merkle Tree in Blockchain - Topcoder. (2022). https://www.topcoder.com/thrive/articles/merkle-tree-in-blockchain

Merkle Tree in Blockchain: Understanding Crypto Data Storage - dYdX. (2024). https://dydx.exchange/crypto-learning/merkle-tree

Merkle Tree in Blockchain: What Is It and How Does It Work? - Medium. (2023). https://medium.com/@Jenovation/merkle-tree-in-blockchain-what-is-it-and-how-does-it-work-f77cd361ca32

Merkle Tree in Blockchain: What is it, How does it work and Benefits. (n.d.). https://www.simplilearn.com/tutorials/blockchain-tutorial/merkle-tree-in-blockchain

Merkle Tree in Blockchain: What It Is and How It Works - Investopedia. (2017). https://www.investopedia.com/terms/m/merkle-tree.asp

Merkle Tree in Blockchain: Working, Examples, & Advantages. (2025). https://intellipaat.com/blog/merkle-tree-in-blockchain/

Merkle Tree: Powering Blockchain Integrity & Efficiency - Shardeum. (2023). https://shardeum.org/blog/merkle-tree-in-blockchain/

Merkle Tree Security And Vulnerabilities - FasterCapital. (2024). https://fastercapital.com/topics/merkle-tree-security-and-vulnerabilities.html

Merkle Tree vs Verkle Tree: Comparison & Analysis - CronJ. (2023). https://www.cronj.com/blog/merkle-tree-vs-verkle-tree-comparison-analysis/

Merkle tree vulnerabilities | Bitcoin Optech. (2019). https://bitcoinops.org/en/topics/merkle-tree-vulnerabilities/

Merkle Trees | Cryptocurrency & Blockchain Technology. (2023). https://freemanlaw.com/merkle-trees-2/

Merkle Trees — An Introduction to Concepts and Components. (2021). https://medium.com/umbrella-network/merkle-trees-an-introduction-to-concepts-and-components-5d2ff2b939e2

Merkle Trees & Merkle Roots: Bitcoin & Blockchain | Gemini. (n.d.). https://www.gemini.com/cryptopedia/merkle-tree-blockchain-merkle-root

Merkle Trees: A Comprehensive Guide with Real-World Use Cases. (n.d.). https://codiin.com/merkle-trees-a-comprehensive-guide-with-real-world-use-cases/

Merkle Trees: All You Need to Know - UEEx Technology. (2024). https://blog.ueex.com/merkle-trees/

Merkle Trees and Patricia Trees: Pioneering Ethereum’s State ... - Unvest. (2023). https://www.unvest.io/blog/merkle-trees-and-patricia-trees-pioneering-ethereums-state-representation

Merkle Trees and Verkle Trees - TradeDog. (n.d.). https://tradedog.io/a-comprehensive-comparison-of-merkle-trees-and-verkle-trees/

Merkle Trees in Blockchain: A Comprehensive Guide - CronJ. (2023). https://www.cronj.com/blog/merkle-trees-in-blockchain-a-comprehensive-guide/

Merkle Trees in Blockchain: A Study of Collision Probability and ... (2024). https://arxiv.org/abs/2402.04367

Merkle Trees: Key to Blockchain Data Integrity - cryptovate.io. (2025). https://www.cryptovate.io/understanding-merkle-trees-blockchain/

Merkle Trees vs. Verkle Trees: All You Need To Know. (2022). https://www.blockchain-council.org/blockchain/merkle-trees-vs-verkle-trees/

Merkle Trees vs. Verkle Trees: Blockchain Data Structures - Shardeum. (2024). https://shardeum.org/blog/merkle-trees-vs-verkle-trees-blockchain/

Merkle trees vs. Verkle trees, Explained - Cointelegraph. (2022). https://cointelegraph.com/explained/merkle-trees-vs-verkle-trees-explained

M.GRACY, B. Jeyavadhanam, S. Albert, & Antony Raj. (n.d.). ENHANCING TRANSACTION VERIFICATION THROUGH PRUNED MERKLE TREE IN BLOCKCHAIN. https://www.semanticscholar.org/paper/7baf40bfd0b72b2a0a3bd08350ba8ca4ea292c25

Mo Si-quan. (2010). The Research of Traverse of Merkle Tree. In Microcomputer Information. https://www.semanticscholar.org/paper/02245ceac28e1aa98669b10aea29a5b6d94dab0c

Mr. Vinay, Kumar Saini, Dr. Sachin Gupta, & Dr. Bhoomi Gupta. (2020). “Traceability and Optimization over Merkle Tree.” https://www.semanticscholar.org/paper/a6a449eadb66164738c7990cb0651bf112e5a500

My Introduction to the Blockchain and Merkle Tree - Medium. (2022). https://medium.com/better-programming/my-introduction-to-the-blockchain-and-merkle-tree-6fba6ee853c

N Ambika. (2025). Securing Business Transactions Using Merkle Tree. https://onlinelibrary.wiley.com/doi/abs/10.1002/9781394234028.ch9

O Kuznetsov, A Rusnak, A Yezhov, & K Kuznetsova. (2024). Merkle trees in blockchain: A study of collision probability and security implications. In Internet of Things. https://www.sciencedirect.com/science/article/pii/S2542660524001343

O Kuznetsov, D Kanonik, A Rusnak, & A Yezhov. (2024). Adaptive Merkle trees for enhanced blockchain scalability. In Internet of Things. https://www.sciencedirect.com/science/article/pii/S2542660524002567

On Merkle Trees - Craig Wright. (n.d.). https://craigwright.net/wp-content/uploads/2019/11/On-Merkle-Trees_CSW.pdf

Optimization Methods for Merkle Tree in Blockchain. (n.d.). https://link.springer.com/chapter/10.1007/978-981-96-0695-5_11

Optimizing Merkle Tree Structure for Blockchain Transactions by a DC ... (n.d.). https://dl.acm.org/doi/10.1007/978-3-031-41456-5_31

[PDF] Lecture 10: Accounts Model and Merkle Trees. (2022). https://web.stanford.edu/class/ee374/lec_notes/lec10.pdf

[PDF] Merkle Trees in Blockchain: A Study of Collision Probability ... - arXiv. (n.d.). https://arxiv.org/pdf/2402.04367

[PDF] Pros and Cons of Merkle Tree. (n.d.). https://www.publications.scrs.in/chapter/pdf/view/404

[PDF] Refactoring for Enhanced Reliability: Methods and Tools in ... - SSRN. (n.d.). https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4822971_code6728851.pdf?abstractid=4822971&mirid=1

[PDF] REVIEW ON VERKLE TREE IN BLOCKCHAIN TECHNOLOGY - RJPN. (2024). https://rjpn.org/ijnti/papers/IJNTI2407008.pdf

Q Deng. (2019). Blockchain economical models, delegated proof of economic value and delegated adaptive Byzantine fault tolerance and their implementation in artificial intelligence …. In Journal of Risk and Financial Management. https://www.mdpi.com/1911-8074/12/4/177

Qing Li. (2019). Research on E-Commerce User Information Encryption Technology Based on Merkle Hash Tree. In 2019 International Conference on Robots & Intelligent System (ICRIS). https://ieeexplore.ieee.org/document/8806443/

R Di Pietro & F Martinelli. (2012). Broadcast authentication for resource constrained devices: a major pitfall and some solutions. https://ieeexplore.ieee.org/abstract/document/6424856/

R Nygaard & V Estrada-Galiñanes. (2021). Snarl: Entangled merkle trees for improved file availability and storage utilization. https://dl.acm.org/doi/abs/10.1145/3464298.3493397

S Goncharov & A Nechesov. (2023). Axiomatization of Blockchain Theory. In Mathematics. https://www.mdpi.com/2227-7390/11/13/2966

S Jing, X Zheng, & Z Chen. (2021). Review and investigation of merkle tree’s technical principles and related application fields. https://ieeexplore.ieee.org/abstract/document/9545917/

Securing Merkle Tree in OpenZeppelin’s MerkleProof.sol Library. (2024). https://hacken.io/insights/merkleproof-library/

The Cross-Domain Thesis Part 2: Storage Proofs, Computation, and ... (2024). https://www.maven11.com/publication/the-cross-domain-thesis-part-2-storage-proofs-computation-and-bloat

The History of Merkle Trees - Medium. (2024). https://medium.com/@kootie73/the-history-of-merkle-trees-996b84b30fa1

The Nearly Optimal Merkle Tree (NOMT) - Spicenet Docs. (2024). https://docs.spicenet.io/core-technical-architecture/the-nearly-optimal-merkle-tree-nomt

The Ultimate Merkle Tree Guide in Solidity. (2022). https://soliditydeveloper.com/merkle-tree

Top 10 Merkle Tree For Data Storage In Blockchain PowerPoint ... (n.d.). https://www.slideteam.net/top-10-merkle-tree-for-data-storage-in-blockchain-powerpoint-presentation-templates

Top 23 papers published in the topic of Merkle tree in 2024 - SciSpace. (n.d.). https://scispace.com/topics/merkle-tree-3ls705h7/2024

TTT Nguyen, HA Le Thi, & XV Doan. (2023). Optimizing Merkle tree structure for Blockchain transactions by a DC Programming approach. https://link.springer.com/chapter/10.1007/978-3-031-41456-5_31

Understanding Merkle Trees | Space and Time. (n.d.). https://spaceandtime.io/blog/understanding-merkle-trees

Understanding Merkle Trees - Medium. (2023). https://medium.com/@SpaceandTimeDB/understanding-merkle-trees-252f83aa6e51

Understanding Merkle Trees: A Practical Guide to Hashing - Daisie Blog. (2023). https://blog.daisie.com/understanding-merkle-trees-a-practical-guide-to-hashing/

Understanding Merkle Trees and Proofs | by Mike Dyne | Evendyne. (2023). https://medium.com/evendyne/understanding-merkle-trees-and-proofs-5eca62ba3e83

Use Cases Of Merkle Trees In Blockchain Applications - FasterCapital. (2024). https://fastercapital.com/topics/use-cases-of-merkle-trees-in-blockchain-applications.html

Useful Analogies for Understanding Blockchain | by Tiong Woon ... - Medium. (n.d.). https://medium.com/superficial-intelligence/useful-analogies-for-understanding-blockchain-eecd3dbce08f

Utkarsh Srivastava. (2025). Voter Verification in an Election Using Merkle Tree. In International Journal for Research in Applied Science and Engineering Technology. https://www.semanticscholar.org/paper/8d522ae9453e09e905a673079fd268b3b051ab33

V Capocasale & F Pedone. (2024). Parallel transaction execution in blockchain and the ambiguous state representation problem. https://ieeexplore.ieee.org/abstract/document/10533313/

V Cheval, J Moreira, & M Ryan. (2023). Automatic verification of transparency protocols. https://ieeexplore.ieee.org/abstract/document/10190509/

W Posdorfer, H Bornholdt, & W Lamersdorf. (2020). Transaction Dependency Model for Block Minimization in Arbitrary Blockchains. https://dl.acm.org/doi/abs/10.1145/3409934.3409935

What Is a Merkle Root (Cryptocurrency)? How It Works in Blockchain. (2018). https://www.investopedia.com/terms/m/merkle-root-cryptocurrency.asp

What is A Merkle Tree? - Blockchain Council. (n.d.). https://www.blockchain-council.org/blockchain/what-is-a-merkle-tree/

What is a Merkle Tree? - Decentralized Thoughts. (2020). https://decentralizedthoughts.github.io/2020-12-22-what-is-a-merkle-tree/

What Is a Merkle Tree & What Is Its Role in Blockchain? - OSL. (2025). https://osl.com/academy/article/what-is-a-merkle-tree-and-what-is-its-role-in-blockchain

What is a Merkle Tree? Beginner’s Guide to this Blockchain Component. (n.d.). https://blockonomi.com/merkle-tree/

What Is a Merkle Tree in Blockchain? - HeLa. (n.d.). https://helalabs.com/blog/what-is-a-merkle-tree-an-essential-concept-for-data-integrity/

What Is A Merkle Tree In Blockchain - Robots.net. (2023). https://robots.net/ai/what-is-a-merkle-tree-in-blockchain/

What is a Merkle Tree? The Cryptographic Backbone of Blockchain ... (2025). https://dev.to/mysteryminusplus/what-is-a-merkle-tree-the-cryptographic-backbone-of-blockchain-integrity-4n2o

What is Merkle Tree in Blockchain? - Analytics Steps. (2022). https://www.analyticssteps.com/blogs/what-merkle-tree-blockchain

What’s A Merkle Tree? A Simple Guide To Merkle Trees. (2024). https://komodoplatform.com/en/academy/whats-merkle-tree/

Why are Merkle Trees Important in Blockchain? // AgilePhD. (n.d.). https://blog.agilephd.com/posts/blockchain_merkle_tree/

Widya Wirachantika, A. Barmawi, & Bambang Ari Wahyudi. (2019). Strengthening fawkescoin against double spending attack using merkle tree. In Proceedings of the 3rd International Conference on Cryptography, Security and Privacy. https://www.semanticscholar.org/paper/6b1a9d9458f86db4a27e8ccc904bfaecd7dabccb

Y Liu, A Liu, Y Xia, B Hu, J Liu, & Q Wu. (2023). A blockchain-based cross-domain authentication management system for IoT devices. https://ieeexplore.ieee.org/abstract/document/10175630/

Z Zhang, H Li, D Li, & KC Li. (2025). AAMB: a cross-domain identity authentication scheme based on multilayered blockchains in IoMT. In The Journal of Supercomputing. https://link.springer.com/article/10.1007/s11227-025-07309-4

Zhenhuan Gao, Yuxuan Hu, & Qinfan Wu. (n.d.). Jellyfish Merkle Tree. https://www.semanticscholar.org/paper/a43fd556b2bdc03995efe620e885817b31590d38

Zhenpeng Liu, Lele Ren, Yongjiang Feng, Shuo Wang, & Jianhang Wei. (2023). Data Integrity Audit Scheme Based on Quad Merkle Tree and Blockchain. In IEEE Access. https://www.semanticscholar.org/paper/fba6807ad8218a52573215d7ce548f417ab9b0f7



Generated by Liner
https://getliner.com/search/s/5926611/t/85557243