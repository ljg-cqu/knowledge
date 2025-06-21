'Blockchain Signature Schemes.' Requirements: 1. Ensure compliance with MECE. 2. Classify/categorize logically and appropriately if necessary. 3. Explain with analogy and examples. 4. Use numbered lists for clear explanations when possible. 5. Describe core elements, components, factors and aspects. 6. List core evaluation dimensions and corresponding evaluations if applicable. 7. Describe their concepts, definitions, functions, and characteristics. 8. Clarify their purposes and assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect). 9. Describe relevant markets, ecosystems, regulations, and economic models, and explain the corresponding strategies used to generate revenue. 10. Describe their work mechanism concisely first and then explain how they work with phase-based workflows throughout the entire lifecycle. 11. Clarify their preconditions, inputs, outputs, immediate outcomes, long-term impacts, and potential implications. 12. Clarify their underlying laws, axioms, theories, and patterns. 13. Describe the design philosophy and architectural features. 14. Provide ideas, techniques, and means of architectural refactoring. 15. Clarify relevant frameworks, models, and principles. 16. Clarify their origins, evolutions, and trends. 17. List key historical events, core factual statements, raw data points, and summarized statistical insights. 18. Clarify techniques, methods, approaches, protocols, and algorithms.  19. Describe contradictions and trade-offs. 20. Identify and list all major competitors (including the one being searched at present) with concise descriptions within the target market or industry segment. 21. Conduct a comprehensive competitor analysis to evaluate each competitor’s (including the one being searched at present) operational strategies, product offerings, market position, and performance metrics. 22. Perform a SWOT analysis for each competitor (including the one being searched at present), categorizing findings into strengths, weaknesses, opportunities, and threats. 23. Clarify principles, rules, constrains, limitations, vulnerabilities, challenges, obstacles, and risks. 24. Describe potential security vulnerabilities, troubleshooting methods, attack tactics, prevention methods and emergency measures. 25. Describe potential performance bottlenecks, troubleshooting methods and optimization measures. 26. Explain priorities, use cases, pitfalls, and best practices. 27. Clarify cause-and-effect relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 28. Clarify interdependency relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 29. Clarify cardinality-based relationships (1:1, 1:M, M:N). 26. Clarify contradictory relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 30. Describe the existing non-trivial problems and potential approaches to address them. 31. Introduce the relevant research topics of significant value that remain to be overcome. 32. Introduce the possible directions and approaches of within-domain and cross-domain innovation. 33. Predict the ultimate form of the related development. 34. Make a summary table at the end with purposes, characteristics, use cases, ect. for clarity. 35. Append the terminologies, formulas, and analogies at the end with concise descriptions for each item.

Thu Jun 12 2025

### 1. MECE-Compliant Classification of Blockchain Signature Schemes

To achieve Mutual Exclusivity and Collective Exhaustiveness (MECE), blockchain signature schemes are categorized by their cryptographic principles and functional purposes, thereby ensuring each scheme is distinct with no overlaps and that all essential scheme types are included:

1. **Classical Digital Signature Schemes**
   - ECDSA, RSA, and EdDSA, foundational in securing blockchain transactions using mature, well-understood cryptographic principles.
2. **Post-Quantum Signature Schemes**
   - Hash-based (e.g., XMSS), lattice-based, and other innovative constructions designed to withstand quantum attacks.
3. **Group Signature Schemes**
   - Enable a group member to sign a message anonymously, with accountability maintained via a group manager or decentralized protocols.
4. **Multi-Signature/Multi-Party Schemes**
   - Aggregate, threshold, and multi-signature protocols that allow multiple parties to authorize a transaction.
5. **Adaptor Signature Schemes**
   - Conditional, scriptless signatures for atomic swaps and advanced smart contract interactions.
6. **Homomorphic Signature Schemes**
   - Allow computation on signed data to yield valid signatures for computed results.
7. **Blind Signature Schemes**
   - Support for privacy through signing messages without knowledge of their content.
8. **Identity-Based and Certificateless Schemes**
   - Use unique identities as the basis for key generation and management.
9. **Expander Signature Schemes**
   - Recently introduced schemes with phased/gradual verification features.

This structure ensures the list is MECE: each scheme aligns exclusively with a principle, and all relevant types are covered.

---

### 2. Classification, Analogy, and Examples

#### 2.1 Numbered Explanations with Analogies

1. **Classical Digital Signatures**
   - *Analogy*: Like a handwritten signature on a contract, unique to the signer and verifiable by anyone with the correct "signature sample" (the public key).
   - *Example*: Bitcoin's use of ECDSA to sign transactions ensures transfer authenticity.
2. **Post-Quantum Signatures**
   - *Analogy*: Like a futuristic lock that cannot be picked even with tomorrow's advanced tools (quantum computers).
   - *Example*: XMSS for quantum-resistant blockchain, offering stronger protection but with longer keys/signatures.
3. **Group Signatures**
   - *Analogy*: Imagine a group’s official stamp; any member can use it but only the group leader can reveal which member signed.
   - *Example*: Used in privacy coins or organization voting on blockchains.
4. **Multi-Signature Schemes**
   - *Analogy*: A bank safe requiring two or more keys to open—cooperation is mandatory.
   - *Example*: Corporate wallets that need approval from multiple executives.
5. **Adaptor Signatures**
   - *Analogy*: An envelope that is "almost" sealed but becomes fully sealed only when a certain event occurs.
   - *Example*: Atomic swaps where finalizing a signature releases funds only once both parties have acted.
6. **Homomorphic Signatures**
   - *Analogy*: A contract that remains valid even after authorized adjustments.
   - *Example*: Data aggregation on-chain where computations do not invalidate original signatures.
7. **Blind Signatures**
   - *Analogy*: Signing a folded letter—blindly approving the content without seeing it.
   - *Example*: Used in privacy-enhanced voting on chain.
8. **Identity-Based/Certificateless**
   - *Analogy*: Your phone number becoming your public key for signatures.
   - *Example*: Used in IoT networks for seamless device authentication.
9. **Expander Signatures**
   - *Analogy*: A time-locked box where each key can unlock contents only after a certain period.
   - *Example*: Payment installments, where signatures become progressively verifiable.

---

### 3. Core Elements, Components, Factors, and Aspects

- **Key Elements**: Private key (for signing), public key (for verification), cryptographic algorithm (for signature generation and validation), message or transaction data, and often a hash function.
- **Critical Components**: Signature generation algorithm, signature verification algorithm, key management infrastructure, and interface protocols for integration within blockchain systems.
- **Factors and Aspects**: Security level (resistance to forgery and attacks), signature size, verification speed, privacy features, scalability, and compliance with architectural decentralization.

---

### 4. Core Evaluation Dimensions and Corresponding Evaluations

1. **Security**: Unforgeability, resistance to quantum or adaptive attacks.
2. **Efficiency**: Signature size, computational speed for signing and verification.
3. **Scalability**: Support for aggregation, batch verification, resource constraints.
4. **Privacy Preservation**: Level of identity protection, unlinkability.
5. **Practicality/Deployment**: Ease of integration, key management, cross-chain compatibility.

Aggregated signatures and threshold schemes generally score higher on scalability and efficiency, while post-quantum and privacy-focused schemes may incur trade-offs in size or speed.

---

### 5. Concepts, Definitions, Functions, and Characteristics

- **Concepts**: Digital signatures provide proof that a transaction or message was authorized by the private key holder, enforcing authenticity, integrity, and non-repudiation.
- **Definitions**: A digital signature is a mathematical construct involving a private key to create a verifiable string for a message, proven valid by a public key.
- **Functions**: Authenticate sender, validate integrity, prevent repudiation, and (for advanced schemes) anonymize or aggregate authorization.
- **Characteristics**: Deterministic or probabilistic, interactive or non-interactive, support for anonymity, potential for multi-party operation, and scalable verification.

---

### 6. Purposes and Assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect)

- **Value**: Provide trust, authenticity, and enforceability in decentralized, trust-minimized environments.
- **Descriptive**: Define transaction and identity authenticity protocols in blockchains.
- **Prescriptive**: Mandate use of cryptographic signatures for all transaction validation and consensus-related operations.
- **Worldview**: Decentralization is paramount; trust is established cryptographically rather than institutionally.
- **Cause-and-Effect**: Security assumptions <-ensure-> transaction integrity; failure in key management <-leads-to-> exposure/fraud.

---

### 7. Relevant Markets, Ecosystems, Regulations, and Economic Models

- **Markets**: Cryptocurrency, enterprise blockchains (finance, energy, supply chain, IoT, healthcare).
- **Ecosystems**: Public (permissionless, e.g., Bitcoin), private (permissioned, e.g., Hyperledger), and hybrid models.
- **Regulation**: Data protection laws (e.g., GDPR), eIDAS for digital signatures, industry-specific compliance.
- **Economic Models**: Transaction fees, consensus rewards (proof-of-work/stake), staking rewards, service monetization via security/non-repudiation guarantees.
- **Revenue Strategies**: Direct user transaction fees, licensing signature infrastructure, service-layer fees for advanced cryptography, regulatory compliance contracts.

---

### 8. Work Mechanism and Lifecycle Workflow

#### 8.1 Concise Mechanism

A signer uses their private key to create a digital signature over a transaction or data, which is then verified by others (nodes, validators) using the corresponding public key before the transaction is accepted to the blockchain.

#### 8.2 Phase-Based Lifecycle

1. **Key Generation**: Parties generate cryptographic key pairs (private/public).
2. **Signing**: The private key holder signs the transaction or message.
3. **Verification**: Other network participants use the public key to validate the signature.
4. **Consensus and Recording**: Validated transactions are bundled and recorded in a block.
5. **Audit/Trace**: The transaction and signature are stored immutably for verification and audit.

---

### 9. Preconditions, Inputs, Outputs, Outcomes, and Implications

- **Preconditions**: Secure key pair generation and storage; blockchain infrastructure prepared for digital signature verification.
- **Inputs**: Message/transaction data, private key.
- **Outputs**: Valid/invalid signature, broadcast transaction.
- **Immediate Outcomes**: Confirmed transaction authenticity and integrity.
- **Long-Term Impacts**: Immutable, trustless record-keeping and fraud resistance.
- **Potential Implications**: Ecosystem scalability, regulatory compliance dependencies, or vulnerability to cryptographic advancements.

---

### 10. Underlying Laws, Axioms, Theories, and Patterns

- **Hardness Assumptions**: Discrete logarithm, integer factorization, lattice problems for quantum resistance.
- **Security Axioms**: Existential unforgeability, strong unforgeability, non-repudiation.
- **Design Patterns**: Multi-party signature aggregation, homomorphic computation, privacy-preserving constructs.

---

### 11. Design Philosophy and Architectural Features

- **Philosophy**: Decentralization, cryptographic trust, scalability, and privacy-preservation are paramount.
- **Features**: Modular signature algorithms, multi-curve backdoor resistance (in MECDSA), keyless signature architectures (in some advanced systems), support for aggregation and threshold signatures.

---

### 12. Ideas, Techniques, and Architectural Refactoring

- **Modularization**: Decoupling signature schemes for easy upgrades (e.g., quantum-resistant migration).
- **Batch/Aggregate Verification**: Optimizing multi-signature verification.
- **Decentralized Management**: Distributing group manager roles (in group signatures).
- **Quantum-Resistant Integration**: Layering post-quantum algorithms alongside classical.
- **Automated Refactoring**: Employing formal models and verification for architectural changes.

---

### 13. Relevant Frameworks, Models, and Principles

- **EUF-CMA**: Existential unforgeability under chosen message attack as a security baseline.
- **Quantum-Ready Models**: Incorporation of hash-based or lattice-based constructs.
- **Composability**: Signature schemes as modular, upgradable components.
- **Permission Models**: Identity-based access protocols, decentralized identity management.

---

### 14. Origins, Evolutions, and Trends

- **Origins**: Classical cryptographic research (e.g., Chaum’s vault system, Merkle hash trees), then Bitcoin’s adoption of ECDSA.
- **Evolution**: Advancements from classical to aggregate, privacy-preserving, and post-quantum schemes, with cross-chain and smart contract integration.
- **Trends**: Post-quantum readiness, privacy-by-design, scalability via aggregation, and cross-domain interoperability.

---

### 15. Key Historical Events, Factual Data, and Statistical Insights

- Introduction of Bitcoin with ECDSA in 2008 revolutionized blockchain signatures.
- Current quantum-resistant schemes balance security and practicality but tend to have larger signature sizes.
- Aggregate and multi-signature adoption is growing for efficiency in enterprise use.

---

### 16. Techniques, Methods, Approaches, Protocols, and Algorithms

- **ECDSA, EdDSA**: Elliptic curve-based signatures.
- **BLS Aggregate Signatures**: Bilinear pairings for compact multi-signature.
- **Hash-based/Lattice-based**: Quantum resistance.
- **MECDSA**: Multi-curve defense against backdoors.
- **Group/Blind/Ring**: Privacy preserving.
- **Batch/Aggregate Verification**: Efficiency for high-throughput blockchains.

---

### 17. Contradictions and Trade-Offs

- **Security vs. Efficiency**: Enhanced security (e.g., post-quantum) leads to larger signatures/keys or more computation.
- **Privacy vs. Accountability**: More anonymity (group/ring signatures) often means greater difficulty in regulation or auditing.
- **Scalability vs. Complexity**: Aggregate/multi-signature increases efficiency but adds coordination and potential for new attacks.
- **Transparency vs. Confidentiality**: Blockchains’ openness can conflict with transaction privacy requirements.

---

### 18. Major Competitors and Concise Descriptions

| Scheme            | Core Principle             | Key Competitor Features                         |
|-------------------|---------------------------|-------------------------------------------------|
| ECDSA/EdDSA       | Classical ECC              | Efficiency and historic adoption                |
| MECDSA            | Multi-ECC (backdoor avoid) | Security vs. cost balance                       |
| BLS Aggregate     | Aggregation/Pairings       | Batch verification and small size               |
| Hash-based        | Quantum resistance         | Larger signatures, strong security              |
| Lattice-based     | Quantum resistance         | Balanced size, speed, and quantum security      |
| Group/Ring        | Privacy-preservation       | Anonymity, traceability in some builds          |
| Adaptor/Expander  | Conditional/Phased sign    | Advanced contract flexibility                   |

---

### 19. Competitor Analysis: Operational Strategies, Offerings, Position, and Metrics

- **ECDSA/EdDSA**: Ubiquitous, high-speed, but classical—dominant in Bitcoin/Ethereum.
- **MECDSA**: Targets security-conscious organizations wary of backdoors; offers customizable security.
- **BLS Aggregate**: Gaining ground for scalability in PoS chains; outcompetes ECDSA in aggregate verification scenarios.
- **Post-Quantum**: Usually in pilot or hybrid deployments; crucial for future proofing.
- **Group/Ring**: Niche for privacy coins or regulated environments; competitive on privacy features.

---

### 20. SWOT Analysis for Major Schemes

| Scheme           | Strengths                                  | Weaknesses                    | Opportunities                | Threats                      |
|------------------|--------------------------------------------|-------------------------------|------------------------------|------------------------------|
| ECDSA/EdDSA      | Efficient, established, wide support        | Quantum-vulnerable            | Mass adoption                | Quantum breakthroughs        |
| MECDSA           | Resists backdoors, flexible                 | More resource-hungry           | Security-focused blockchains | Complexity, new vulnerabilities|
| BLS Aggregate    | Efficient aggregation, scalable             | Requires special infrastructure| Enterprise/PoS blockchains   | Unproven resistance in attack |
| Hash-based       | Quantum-safe, provably secure               | Large signature/key size       | Long-term archival           | Storage/scaling constraints  |
| Lattice-based    | Quantum-resistant, better size/balance      | Still maturing                 | IoT and constrained devices  | New attack forms             |
| Group/Ring       | Strong privacy/anonymity                    | Less efficient, traceability issues| Privacy coins/regulatory coins| Regulatory risk, abuse       |

---

### 21. Principles, Constraints, and Risks

- **Principles**: Unforgeability, non-repudiation, decentralization.
- **Constraints**: Key management complexity, computational load, signature size, interoperability.
- **Risks**: Private key loss, implementation bugs, cryptanalytic attacks, regulatory compliance failure.

---

### 22. Security Vulnerabilities, Troubleshooting, and Emergency Measures

- **Vulnerabilities**: Weak randomness, quantum attacks, linkability, side-channel attacks.
- **Troubleshooting**: Cryptographic audits, formal proofs, diligent randomness sources, batch testing.
- **Prevention/Emergency**: Patch deployment, quantum upgrade plans, key rotation, anomaly detection, community response protocols.

---

### 23. Performance Bottlenecks, Troubleshooting, Optimization

- **Bottlenecks**: Signature verification, large signature sizes, communication overhead for multi-sig.
- **Troubleshooting**: Profiling and benchmarking verification/signing times.
- **Optimization**: Batch verification, aggregate signatures, leader rotation in consensus, hardware acceleration.

---

### 24. Priorities, Use Cases, Pitfalls, and Best Practices

- **Priorities**: Security, efficiency, scalability, privacy, regulatory compliance.
- **Use Cases**: Payments (Bitcoin), enterprise (consortium wallets), privacy (Monero), IoT authentication.
- **Pitfalls**: Poor key management, underestimating quantum threats, overly complex integration.
- **Best Practices**: Vetted cryptography, quantum readiness, batch aggregation, formal audits, modular design.

---

### 25. Cause-and-Effect Relationships

- Enhanced key management -improves-> overall security.
- Quantum-resistance -increases-> signature size/cost.
- Multi-signature -distributes-> authorization power -enhances-> security -but-adds-> complexity.

---

### 26. Interdependency/Contradictory Relationships

- Post-quantum adoption <-requires-> new infrastructure -possibly breaks-> legacy compatibility.
- Aggregate signatures -improve-> scalability -but-depend→ batch verification support in protocol.

---

### 27. Cardinality-Based Relationships

- 1:1: Individual signature (standard blockchain transaction).
- 1:M: Broadcast to multiple verifiers (public key as recipient group).
- M:N: Multi-signature/threshold (many signers, many verifiers), e.g., threshold wallet approval.

---

### 28. Non-Trivial Problems and Approaches

- Migrating from classical to quantum-resistant schemes with backward compatibility.
- Achieving privacy with traceability for regulation.
- Managing performance/scalability as transaction volumes increase (aggregate/batch signatures).
- New attack vectors for novel signature schemes.

---

### 29. Research Topics and Innovation Directions

- Hybrid (cross-domain, cross-chain) identity and signature management.
- Quantum-optimized scheme development.
- Privacy-preserving signatures with regulatory traceability.
- Lightweight post-quantum signatures for IoT/blockchain.

---

### 30. Ultimate Form of Blockchain Signature Schemes

Future schemes will integrate modular, post-quantum primitives, allow dynamic composition (e.g., smart contract-controlled phasing via expander signatures), scale via native multi-sig/aggregate mechanisms, be adaptable for cross-chain and cross-domain operations, support privacy by default but enable flexible traceability, and remain seamlessly upgradable as cryptographic standards evolve.

---

### 31. Summary Table

| Type         | Purpose                    | Key Characteristics           | Prime Use Cases                  | Example                      |
|--------------|----------------------------|-------------------------------|----------------------------------|------------------------------|
| ECDSA/EdDSA  | Auth, Integrity            | Efficient, standard           | General blockchain, Bitcoin      | Bitcoin                      |
| MECDSA       | Auth, Backdoor-resist      | Multi-curve, secure/efficient | Custom blockchains               | Proposed for new chains      |
| BLS Aggregate| Scalability, Multi-party   | Short, aggregate, efficient   | Enterprise, DeFi, PoS            | BLS-aggregate in PoS         |
| Quantum-Resist| Future-proofing           | Larger size, robust           | Archival, high-security ledgers  | XMSS, Falcon                 |
| Multi-sig    | Multi-party authorization  | Aggregate, multi-key          | Corporate, consortium wallets    | Bitcoin multisig             |
| Group/Ring   | Anonymity, privacy         | Hidden signers, unlinkability | Privacy coins, e-voting          | Monero, privacy chains       |
| Adaptor      | Conditional/Atomic         | Scriptless, conditional       | Atomic swaps, payment channels   | Lightning Network            |
| Expander     | Scalable, phased           | Precomputed, controlled verify| Payment installments             | Expander signature           |

---

### 32. Terminologies, Formulas, and Analogies

| Term                | Description                                                    | Analogy                                                        |
|---------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Private Key         | Secret, for signing                                            | Your home’s only key                                           |
| Public Key          | Shared, for verification                                       | Your home address for visitors to check                         |
| Signature           | Proof of authenticity/integrity                                | Wax seal on an envelope                                        |
| Aggregate Signature | Combination of many into one                                   | Bundle letters in single envelope                              |
| Multi-signature     | Multiple keys must sign                                        | Opening a safe with several keys simultaneously                 |
| Expander Key        | Controls phased verification                                   | Timed key for a lockbox to release content gradually           |
| Adaptor Signature   | Conditional signature completion                               | Unlocked safe but only opens with recipient’s secret            |
| Homomorphic Sig     | Sign-then-compute support                                      | Valid contract after legal, authorized amendments               |
| Group/Ring Sig      | Anonymous group authorization                                  | Official group stamp; identity only known to leader/manager     |
| Hash Function       | Data fingerprinting tool                                       | Barcode unique per item                                        |
| Batch Verification  | Checking many at once                                          | Express lane at supermarket                                    |
| Post-Quantum        | Resistant to quantum threats                                   | Future-proof armored lock                                      |

**Formula (ECDSA Signing):**
- Private key: \\( d \\)
- Public key: \\( Q = d \cdot G \\) (where \\( G \\) is curve generator)
- Given message hash \\( z \\), random \\( k \\), signature \\( (r, s) \\):
- \\( r = (k \cdot G)_x \mod n \\)
- \\( s = k^{-1}(z + r \cdot d) \mod n \\)

---

By drawing on credible, MECE-compliant sources and logical structuring, this report offers a complete, systematic understanding of blockchain signature schemes across technical, operational, and business domains.

Bibliography
A Anjum, M Sporny, & A Sill. (2017). Blockchain standards for compliance and trust. In IEEE Cloud Computing. https://ieeexplore.ieee.org/abstract/document/8066010/

A Ghosh, S Gupta, A Dua, & N Kumar. (2020). Security of Cryptocurrencies in blockchain technology: State-of-art, challenges and future prospects. https://www.sciencedirect.com/science/article/pii/S1084804520301090

A Gorkhali, L Li, & A Shrestha. (2020). Blockchain: A literature review. In Journal of Management Analytics. https://www.tandfonline.com/doi/abs/10.1080/23270012.2020.1801529

A Kaushik, A Choudhary, & C Ektare. (2017). Blockchain—literature survey. https://ieeexplore.ieee.org/abstract/document/8256979/

A Lysyanskaya. (2002). Signature schemes and applications to cryptographic protocol design. https://dspace.mit.edu/handle/1721.1/29271

A. Sherman, Farid Javani, Haibin Zhang, & Enis Golaszewski. (2018). On the Origins and Variations of Blockchain Technologies. In IEEE Security & Privacy. https://ieeexplore.ieee.org/document/8674176/

A Singh, RM Parizi, Q Zhang, & KKR Choo. (2020). Blockchain smart contracts formalization: Approaches and challenges to address vulnerabilities. https://www.sciencedirect.com/science/article/pii/S0167404818310927

AA Monrat, O Schelén, & K Andersson. (2019). A survey of blockchain from the perspectives of applications, challenges, and opportunities. In Ieee Access. https://ieeexplore.ieee.org/abstract/document/8805074/

AH Mohsin, AA Zaidan, BB Zaidan, & OS Albahri. (2019). Blockchain authentication of network applications: Taxonomy, classification, capabilities, open challenges, motivations, recommendations and future directions. https://www.sciencedirect.com/science/article/pii/S0920548918303477

Ahsan Umar & Muhammad Zeeshan Zafar. (2025). Blockchain Security: Vulnerabilities and Protective Measures. In World Journal of Advanced Research and Reviews. https://www.semanticscholar.org/paper/f99fdf112d898217ce4c4f6d640c1389df12eda9

AS Yadav, N Singh, & DS Kushwaha. (2023). Evolution of Blockchain and consensus mechanisms & its real-world applications. In Multimedia Tools and Applications. https://link.springer.com/article/10.1007/s11042-023-14624-6

Astrid Carolina Ordoñez-Guerrero, Juan David Muñoz-Garzon, E. Villarreal, A. Bandi, & J. Hurtado. (2022). Blockchain Architectural Concerns: A Systematic Mapping Study. In 2022 IEEE 19th International Conference on Software Architecture Companion (ICSA-C). https://ieeexplore.ieee.org/document/9779841/

Austin Draper, Aryan Familrouhani, D. Cao, Tevisophea Heng, & Wenlin Han. (2019). Security Applications and Challenges in Blockchain. In 2019 IEEE International Conference on Consumer Electronics (ICCE). https://ieeexplore.ieee.org/document/8661914/

Ayman Alkhalifah, Alex Ng, A. Kayes, Jabed Chowdhury, M. Alazab, & P. Watters. (2019). A Taxonomy of Blockchain Threats and Vulnerabilities. In Blockchain for Cybersecurity and Privacy. https://www.semanticscholar.org/paper/118bf20d8c77fddf586e5f8815a27d8c21b1cebd

Aysha Alfaw, Wael Elmedany, & M. S. Sharif. (2022). Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper. In 2022 International Conference on Data Analytics for Business and Industry (ICDABI). https://www.semanticscholar.org/paper/2eb752aa663ea25a2c10e9192d56351d2d9109c5

B Lashkari & P Musilek. (2021). A comprehensive review of blockchain consensus mechanisms. In IEEE access. https://ieeexplore.ieee.org/abstract/document/9376868/

Bakhtiyor Yokubov & Lu Gan. (2021). Comprehensive Comparison of Post-Quantum Digital Signature Schemes in Blockchain. In 2021 International Conference on Electronic Communications, Internet of Things and Big Data (ICEIB). https://ieeexplore.ieee.org/document/9686427/

Bo Mi, Yuan Weng, Darong Huang, Yang Liu, & Yuqing Gan. (2021). A Novel PoW Scheme Implemented by Probabilistic Signature for Blockchain. In Comput. Syst. Sci. Eng. https://www.semanticscholar.org/paper/66eb68ed0ea74fa8344674b9a8791ac2cd2a9e34

Book Review: Blockchain Technologies, Applications and Cryptocurrencies: Current Practice and Future Trends. (2022). In Journal of Economic Literature. https://pubs.aeaweb.org/doi/10.1257/jel.60.1.279.r3

C Guo, P Zhang, B Lin, & J Song. (2022). A dual incentive value-based paradigm for improving the business market profitability in blockchain token economy. In Mathematics. https://www.mdpi.com/2227-7390/10/3/439

C Stathakopoulou & C Cachin. (2017). Threshold signatures for blockchain systems. In Swiss Federal Institute of Technology. https://cachin.com/cc/papers/hlftsig.pdf

Chao Yuan, Mi-xue Xu, & Xueming Si. (2017). Research on a New Signature Scheme on Blockchain. In Secur. Commun. Networks. https://www.hindawi.com/journals/scn/2017/4746586/

Chekkala Gayathri Sai Swarupa. (2024). Innovative Digital Signature Paradigm and its Blockchain Applications. In International Journal for Research in Applied Science and Engineering Technology. https://www.semanticscholar.org/paper/f8dd64ac874216f73c11b0fff0a7a76cd171186b

Chen Wang, Jian Shen, Qingru Ma, & HongGuo Dai. (2023). Aggregate Signature with Single-Transaction Verification for Blockchain. In 2023 IEEE Smart World Congress (SWC). https://ieeexplore.ieee.org/document/10448838/

Chenhuang Wu, Rui Guo, & Zhixiong Chen. (2013). Public Key Replacement Attack on Two Certificateless Blind Signature Schemes. In The Journal of Information and Computational Science. https://www.semanticscholar.org/paper/d77c0f896a2b71fa8a7cd9d8be338561cfbb4648

D Aggarwal, GK Brennen, T Lee, & M Santha. (2017). Quantum attacks on Bitcoin, and how to protect against them. https://arxiv.org/abs/1710.10377

D. Bisztray, R. Heckel, & H. Ehrig. (2008). Veriflcation of Architectural Refactoring Rules. https://www.semanticscholar.org/paper/eeea18b6ff44bdf3fcc12870d5b94e8c1b7134eb

D Boneh, C Gentry, B Lynn, & H Shacham. (2003). A survey of two signature aggregation techniques. https://networkdls.com/Articles/crypto6n2.pdf#page=2

D Boneh, M Drijvers, & G Neven. (2018). Compact multi-signatures for smaller blockchains. https://link.springer.com/chapter/10.1007/978-3-030-03329-3_15

D Maldonado-Ruiz, J Torres, & N El Madhoun. (2022). Current trends in blockchain implementations on the paradigm of public key infrastructure: a survey. https://ieeexplore.ieee.org/abstract/document/9687536/

DA Freund. (2018). Economic incentives and blockchain security. In Journal of Securities Operations & Custody. https://www.ingentaconnect.com/content/hsp/jsoc/2018/00000010/00000001/art00009

Daria A. Snegireva. (2021). Review of Modern Vulnerabilities in Blockchain Systems. In 2021 International Conference on Quality Management, Transport and Information Security, Information Technologies (IT&QM&IS). https://www.semanticscholar.org/paper/0543c4c2b7b32a7cfc054dcd5138a1360afbf28a

Denis Butin. (2017). Physical Attack Vulnerability of Hash-Based Signature Schemes. https://www.semanticscholar.org/paper/3967777b5e13b4fb04577f07bdadc6349d1dc09f

Dimitris Karakostas, A. Kiayias, & T. Zacharias. (2022). Blockchain Nash Dynamics and the Pursuit of Compliance. In Proceedings of the 4th ACM Conference on Advances in Financial Technologies. https://www.semanticscholar.org/paper/58e77f333a6b64644685e586bce5109cbfdc85b5

E Fathalla & M Azab. (2024). Beyond Classical Cryptography: A Systematic Review of Post-Quantum Hash-Based Signature Schemes, Security, and Optimizations. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10731676/

E Politou, F Casino, & E Alepis. (2019). Blockchain mutability: Challenges and proposed solutions. https://ieeexplore.ieee.org/abstract/document/8883080/

Fangguo Zhang, Byoungcheon Lee, & Kwangjo Kim. (2003). Exploring Signature Schemes with Subliminal Channel. https://www.semanticscholar.org/paper/cb64b47afdcba077853ab1f40f93718a138c3f47

Fco. Javier Vázquez-Pantaleon, Gabriel Nava-Fombona, & Ma. Rosalina Gonzalez-Chavez. (2024). Security and privacy challenges in advanced electronic signature: a systematic review on invulnerability and user trust in Mexico. In Revista de Computo Aplicado. https://www.semanticscholar.org/paper/8c6116fd43fddaa54e1ffca9c4479e069770680d

Felix Irresberger, Kose John, Peter Mueller, & Fahad Saleh. (2020). The Public Blockchain Ecosystem: An Empirical Analysis. In Other Information Systems & eBusiness eJournal. https://www.semanticscholar.org/paper/7bcaa5525e5d52704d7595d706ef05864d23a8e3

Feri Fahrianto, Waki Ats Tsaqofi, Siti Ummi Masruroh, Ahmad Fadlan Ramadlan, Dewi Khairani, & Saepul Aripiyanto. (2024). Blockchain in Digital Document: A Review of Trends and Future Directions. In 2024 12th International Conference on Cyber and IT Service Management (CITSM). https://ieeexplore.ieee.org/document/10775530/

FF Alhabardi, A Beckmann, & B Lazar. (2022). Verification of Bitcoin Script in Agda using weakest preconditions for access control. https://arxiv.org/abs/2203.03054

Francesca Fallucchi & Marco Gerardi. (2021). Blockchain, State-of-the-Art and Future Trends World. In System (Linköping). https://www.semanticscholar.org/paper/421599384d77dcc1cf46d85dcdd129f72d992176

G Wu & J Zhou. (2024). Optimization scheme of the blockchain digital signature algorithm. https://dl.acm.org/doi/abs/10.1145/3708036.3708072

Gerrit Muller. (2013). From Legacy to State-of-the-art; Architectural Refactoring. https://www.semanticscholar.org/paper/31e3e7af466c0fd17435bb16c171ded88d691070

Giulia Traverso, Denise Demirel, & J. Buchmann. (2016). Homomorphic Signature Schemes - A survey. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/0d25419e80fff2599c47d5c86f77ebe717feb534

GK Verma, N Kumar, & P Gope. (2021). SCBS: a short certificate-based signature scheme with efficient aggregation for industrial-internet-of-things environment. https://ieeexplore.ieee.org/abstract/document/9343265/

H Hasanova, U Baek, M Shin, & K Cho. (2019). A survey on blockchain cybersecurity vulnerabilities and possible countermeasures. https://onlinelibrary.wiley.com/doi/abs/10.1002/nem.2060

H Lee, K Sung, K Lee, & J Lee. (2018). Economic analysis of blockchain technology on digital platform market. https://ieeexplore.ieee.org/abstract/document/8639624/

H. Meijer & S. Akl. (1982). Digital Signature Schemes. In Cryptologia. https://www.semanticscholar.org/paper/9ca5a8248388d4ffe1cc8e0fe7512be529b1c80f

H Zhang, J Wang, & Y Ding. (2019). Blockchain-based decentralized and secure keyless signature scheme for smart grid. In Energy. https://www.sciencedirect.com/science/article/pii/S0360544219310096

Haifeng Ma & Yuxia Li. (2023). Blockchain privacy protection scheme based on ring signature. In 2023 8th International Conference on Intelligent Informatics and Biomedical Sciences (ICIIBMS). https://ieeexplore.ieee.org/document/10347629/

Hongzhi Yang, L. Yuan, & Shu Wang. (2021). Design of Blockchain Smart Contract Based on Ring Signature. In Proceedings of the 2021 9th International Conference on Communications and Broadband Networking. https://dl.acm.org/doi/10.1145/3456415.3457223

Hourieh Alsadat Hosseini, Alireza Hedayati, & Smart Contracts. (n.d.). A Survey on Blockchain: Challenges, Attacks, Security, and Privacy. https://www.semanticscholar.org/paper/840b72915c5d89e1276572aa4ef79b069cc898a2

I. Makarov & A. Schoar. (2021). Blockchain Analysis of the Bitcoin Market. In FinPlanRN: Investment Strategies (Topic). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3942181

Itisha Jain. (2024). Blockchain Technology and Cryptography. In International Journal of Science and Research (IJSR). https://www.semanticscholar.org/paper/a72330b60d2a275637197cfa2d30218cfde42937

Iuon-Chang Lin & Tzu-Chun Liao. (2017). A Survey of Blockchain Security Issues and Challenges. In Int. J. Netw. Secur. https://www.semanticscholar.org/paper/f61edb500c023c4c4ef665bd7ed2423170773340

J Abadi & M Brunnermeier. (2018). Blockchain economics. https://www.nber.org/papers/w25407

J Camenisch & A Lysyanskaya. (2002). A signature scheme with efficient protocols. https://link.springer.com/chapter/10.1007/3-540-36413-7_20

J Chen, H Xiao, M Hu, & CM Chen. (2023). A blockchain-based signature exchange protocol for metaverse. In Future Generation Computer Systems. https://www.sciencedirect.com/science/article/pii/S0167739X22004356

J. Das, S. Kakoty, & Majidul Ahmed. (2016). A Study on Modern Cryptographic Primitives and Signature Schemes. In IRA-International Journal of Technology & Engineering. https://www.semanticscholar.org/paper/2487aab5f95969ab2d22da9b3640b6fc6596cab1

J. Junfeng. (2008). Two RSA-based Special Digital Signature Schemes. In Computer Knowledge and Technology. https://www.semanticscholar.org/paper/101971c47845f09806add83e55c40c9c313ff149

J Leng, M Zhou, JL Zhao, & Y Huang. (2020). Blockchain security: A survey of techniques and research directions. https://ieeexplore.ieee.org/abstract/document/9271868/

J Samandari & C Gritti. (2025). Online/Offline Digital Signatures: A Systematic Literature Review. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/11006084/

J Zhou, Y Wu, F Liu, Y Tao, & J Gao. (2021). Prospects and obstacles analysis of applying blockchain technology to power trading using a deeply improved model based on the DEMATEL approach. In Sustainable Cities and Society. https://www.sciencedirect.com/science/article/pii/S2210670721001980

JA Tarr. (2018). Distributed ledger technology, blockchain and insurance: Opportunities, risks and challenges. In Insurance Law Journal. https://eprints.qut.edu.au/122862

JB Bernabe, JL Canovas, & JL Hernandez-Ramos. (2019). Privacy-preserving solutions for blockchain: Review and challenges. https://ieeexplore.ieee.org/abstract/document/8888155/

Jian Jiang, Yulong Gao, & Yile Li. (2024). Enhancing Copyright Protection Through Blockchain and Ring Signature Algorithm From Lattice. In IEEE Access. https://ieeexplore.ieee.org/document/10468607/

Jianhong Zhang & Jiancheng Zou. (2006). On the Security of Two Signature Schemes. In 2006 International Conference on Wireless Communications, Networking and Mobile Computing. https://ieeexplore.ieee.org/document/4149471/

Jinhan Li. (2023). A research on digital signature schemes. In Applied and Computational Engineering. https://www.ewadirect.com/proceedings/ace/article/view/4594

Jinmei Yang, Bi Huang, Zhihong Liang, Hua Zhou, & Hongji Yang. (2020). A Survey on Blockchain: Architecture, Applications, Challenges, and Future Trends. In 2020 International Conferences on Internet of Things (iThings) and IEEE Green Computing and Communications (GreenCom) and IEEE Cyber, Physical and Social Computing (CPSCom) and IEEE Smart Data (SmartData) and IEEE Congress on Cybermatics (Cybermatics). https://ieeexplore.ieee.org/document/9291547/

Junke Duan, L. Gu, & Shihui Zheng. (2021). Polymerized RingCT: An Efficient Linkable Ring Signature for Ring Confidential Transactions in Blockchain. In Journal of Physics: Conference Series. https://validate.perfdrive.com/fb803c746e9148689b3984a31fccd902/?ssa=ea333fa8-f8a5-43dd-9fba-46ec37a305c7&ssb=14509265691&ssc=https%3A%2F%2Fiopscience.iop.org%2Farticle%2F10.1088%2F1742-6596%2F1738%2F1%2F012109&ssi=2ad5222a-cnvj-4c12-9e73-8ed5eba0babe&ssk=botmanager_support@radware.com&ssm=972698929128944772351434322837313&ssn=528f18e3dbd5df3d25e39f5a1a77a5586eb827cb887f-d381-45f1-8b2743&sso=4da5dd2f-7454926c8db4430220f13e0c15ace00419ad26a9af37b777&ssp=16456905681749755225174971709885162&ssq=55331440537610436531603884217892735989085&ssr=MzQuNTkuMy4xNTU=&sst=python-httpx/0.27.2&ssu=&ssv=&ssw=&ssx=eyJ1em14IjoiN2Y5MDAwMjM1YTY2Y2MtOTg1Zi00MWM5LWE1NGQtN2Q2MDQ0ZGM2YmExMS0xNzQ5NzAzODg0NDc1MTQ5MTYyMS05MzYxNzg0ZDRiMGIwMGRjMjM1IiwiX191em1mIjoiN2Y2MDAwMThmODk3NjQtZGMyOS00NzA3LWJiM2ItMmMwYzZkNDc4ZmQ3MTc0OTcwMzg4NDQ3NTE0OTE2MjEtYzFkYzYwZGE0YzBkOTQwZjIzNSIsInJkIjoiaW9wLm9yZyJ9

K. Gangadevi & R. Renuga Devi. (2021). A survey on data integrity verification schemes using blockchain technology in Cloud Computing Environment. In IOP Conference Series: Materials Science and Engineering. https://validate.perfdrive.com/fb803c746e9148689b3984a31fccd902/?ssa=0d8178af-fab5-486c-ac8c-a4234ceefce3&ssb=73073258022&ssc=https%3A%2F%2Fiopscience.iop.org%2Farticle%2F10.1088%2F1757-899X%2F1110%2F1%2F012011&ssi=507bfffb-cnvj-481d-8908-ace99a4af8f2&ssk=botmanager_support@radware.com&ssm=044801177094699602329603449014036&ssn=7537f91ab706437ab5e348757416625fa4ac27cb887f-d381-45f1-84d8b6&sso=9244bd2f-7454926c8db45f00be2b7bdb9fdfeb300c2e2170144bd635&ssp=53512594831749781926174978472406769&ssq=69676670537502783080203884311022694809586&ssr=MzQuNTkuMy4xNTU=&sst=python-httpx/0.27.2&ssu=&ssv=&ssw=&ssx=eyJ1em14IjoiN2Y5MDAwMjM1YTY2Y2MtOTg1Zi00MWM5LWE1NGQtN2Q2MDQ0ZGM2YmExMS0xNzQ5NzAzODg0NDc1MTQ5MTA3OS1kMDVmZWUxMThiNzgzZTY4MjMyIiwiX191em1mIjoiN2Y2MDAwMThmODk3NjQtZGMyOS00NzA3LWJiM2ItMmMwYzZkNDc4ZmQ3MTc0OTcwMzg4NDQ3NTE0OTEwNzktYTY5Yzc0ZmM1YzgyZTYxMTIzMiIsInJkIjoiaW9wLm9yZyJ9

KAA Mutlaq, VO Nyangaresi, & MA Omar. (2025). Blockchain assisted signature and certificate based protocol for efficient data protection and transaction management in smart grids. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0318182

Kang Qiao, Hongbo Tang, Wei You, & Yu Zhao. (2019). Blockchain Privacy Protection Scheme Based on Aggregate Signature. In 2019 IEEE 4th International Conference on Cloud Computing and Big Data Analysis (ICCCBDA). https://www.semanticscholar.org/paper/d922d1115e4a786990a30dee8153e982522f54c0

Kunlun Fu, Lianhai Wang, Wei Shao, Wen Wang, Shuhui Zhang, Shujiang Xu, & Shanshan Hu. (2021). Supervisory Scheme for Blockchain Privacy Protection Technique Based on Group Signature. In Proceedings of the 2021 ACM International Conference on Intelligent Computing and its Emerging Applications. https://dl.acm.org/doi/10.1145/3491396.3506528

KW Prewett & GL Prescott. (2020). Blockchain adoption is inevitable—Barriers and risks remain. https://onlinelibrary.wiley.com/doi/abs/10.1002/jcaf.22415

Kyung-Ah Shim. (2018). Security Analysis of Various Authentication Schemes Based on Three Types of Digital Signature Schemes. In IEEE Access. https://ieeexplore.ieee.org/document/8528464/

Kyung-Ah Shim. (2020). Security Vulnerabilities of Four Signature Schemes From NTRU Lattices and Pairings. In IEEE Access. https://ieeexplore.ieee.org/document/9078790/

Kyung-Ah Shim. (2022a). Design Principles of Secure Certificateless Signature and Aggregate Signature Schemes for IoT Environments. In IEEE Access. https://ieeexplore.ieee.org/document/9964199/

Kyung-Ah Shim. (2022b). A Survey on Post-Quantum Public-Key Signature Schemes for Secure Vehicular Communications. In IEEE Transactions on Intelligent Transportation Systems. https://ieeexplore.ieee.org/document/9646494/

L. Xian. (2001). Efficient Authentication Signature Schemes for Dynamic Multicast Groups. In Journal of Software. https://www.semanticscholar.org/paper/39119c4480328169cfc73c77e662945d279ada49

Lijun Wei, Jing Wu, C. Long, & Yi-Bing Lin. (2019). The Convergence of IoE and Blockchain: Security Challenges. In IT Professional. https://www.semanticscholar.org/paper/a904fba6d203748a1686ef08b42540f93cf61afa

Lin Wang, Changgen Peng, & Weijie Tan. (2023). Secure Ring Signature Scheme for Privacy-Preserving Blockchain. In Entropy. https://www.mdpi.com/1099-4300/25/9/1334

Lipeng Wang, Mingsheng Hu, Zhijuan Jia, Bei Gong, & Yanfang Lei. (2018). A Signature Scheme Applying on Blockchain Voting Scene Based on the Asmuth-Bloom Algorithm. In 2018 IEEE 4th International Conference on Computer and Communications (ICCC). https://ieeexplore.ieee.org/document/8780775/

Luca Rizzi, F. Fontana, & Riccardo Roveda. (2018). Support for architectural smell refactoring. In Proceedings of the 2nd International Workshop on Refactoring. https://dl.acm.org/doi/10.1145/3242163.3242165

M Buser, R Dowsley, M Esgin, & C Gritti. (2023). A survey on exotic signatures for post-quantum blockchain: Challenges and research directions. https://dl.acm.org/doi/abs/10.1145/3572771

M. Jurkiewicz. (2020). Improving Security of Existentially Unforgeable Signature Schemes. In International Journal of Electronics and Telecommunications. https://www.semanticscholar.org/paper/5d98d6eafae5bb6e184d928600fc25179ef96b11

M Kara, A Laouid, & M Hammoudeh. (2023). An efficient multi-signature scheme for blockchain. In Cryptology ePrint Archive. https://iacr.steepath.eu/2023/078-AnEfficientMultiSignatureSchemeforBlockchain.pdf

M Khan, F den Hartog, & J Hu. (2022). A survey and ontology of blockchain consensus algorithms for resource-constrained IoT systems. In Sensors. https://www.mdpi.com/1424-8220/22/21/8188

M. Mylrea, Sri Nikhil Gupta Gourisetti, R. Bishop, & Matt Johnson. (2018). Keyless Signature Blockchain Infrastructure: Facilitating NERC CIP Compliance and Responding to Evolving Cyber Threats and Vulnerabilities to Energy Infrastructure. In 2018 IEEE/PES Transmission and Distribution Conference and Exposition (T&D). https://www.semanticscholar.org/paper/ca66374f7329c99b05fe0594bfbe1ca06ec5103d

M. Passarelli, Alfio Cariola, & G. Bongiorno. (2022). Trends in Blockchain Technologies. In Advances in Data Mining and Database Management. https://www.semanticscholar.org/paper/75d70966ec29bb2cb5f5070aa8a7c2b0f05ff738

M. R. Deore & S. M. Handore. (2015). A survey on offline signature recognition and verification schemes. In 2015 International Conference on Industrial Instrumentation and Control (ICIC). https://ieeexplore.ieee.org/document/7150731/

M Sheikh & C Kalita. (2025). A Review of Signature Schemes for Enhanced Information Retrieval and Privacy in Blockchain Systems. https://ieeexplore.ieee.org/abstract/document/10969412/

M Staples, S Chen, S Falamaki, & A Ponomarev. (2017). Risks and opportunities for systems using blockchain and smart contracts. Data61. https://www.academia.edu/download/102517822/Blockchains_20and_20Smart_20Contracts.pdf

M Swan. (2017). Anticipating the economic benefits of blockchain. In Technology innovation management review. https://timreview.ca/sites/default/files/article_PDF/Swan_TIMReview_October2017.pdf

MA Ferrag & L Shu. (2021). The performance evaluation of blockchain-based security and privacy systems for the Internet of Things: A tutorial. In IEEE Internet of Things Journal. https://ieeexplore.ieee.org/abstract/document/9424688/

Manoj Kumar. (2009). Linkability of Blind Signature Schemes over Braid Groups. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/352781144fe96f02f4239a0f475ed1529155e873

Masashi Sato & Shin’ichiro Matsuo. (2017). Long-Term Public Blockchain: Resilience against Compromise of Underlying Cryptography. In 2017 26th International Conference on Computer Communication and Networks (ICCCN). https://www.semanticscholar.org/paper/0383d7dc6e7d78e00216affa760fabd3d776398b

Maxime Buser, Rafael Dowsley, Muhammed F. Esgin, Clémentine Gritti, S. K. Kermanshahi, Veronika Kuchta, Jason Legrow, Joseph K. Liu, Raphael C.-W. Phan, A. Sakzad, Ron Steinfeld, & Jiangshan Yu. (2022). A Survey on Exotic Signatures for Post-Quantum Blockchain: Challenges & Research Directions. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/db12e41b60718c36dfca120ffe8dd1a39b066971

Mayank Raikwar, D. Gligoroski, & Katina Kralevska. (2019). SoK of Used Cryptography in Blockchain. In IEEE Access. https://www.semanticscholar.org/paper/bb7bf57de5320d32cce2b49ba212b21d0cb32868

ML Di Silvestre, P Gallo, JM Guerrero, & R Musca. (2020). Blockchain for power systems: Current trends and future applications. https://www.sciencedirect.com/science/article/pii/S1364032119307932

MM Nair & AK Tyagi. (2023). Blockchain technology for next-generation society: current trends and future opportunities for smart era. https://ak-tyagi.com/publicationPdf/129.pdf

MNM Bhutta, AA Khwaja, A Nadeem, & HF Ahmad. (2021). A survey on blockchain technology: Evolution, architecture and security. https://ieeexplore.ieee.org/abstract/document/9402747/

Mohamed Abdelrahman. (2022). Blockchain Cryptography and Security Issues. In International Journal of Computer Science &amp; Engineering Survey. https://aircconline.com/ijcses/V13N6/13622ijcses01.pdf

Monira M. Khater, Ayman Al-ahwal, M. Selim, & H. Zayed. (2018). Blind Signature Schemes based on ElGamal Signature for Electronic Voting: A Survey. In International Journal of Computer Applications. https://www.ijcaonline.org/archives/volume180/number30/khater-2018-ijca-916766.pdf

MP Sindhu & V Ebenezer. (2024). Fortifying Blockchain: Streamlined Lattice Signatures Amid Quantum Threats to Blockchain. https://ieeexplore.ieee.org/abstract/document/10493932/

Mr. Dattaprasad Patil & Mrs. Vijaya Bhosale. (2023). An Overview of Blockchain Technology: Architecture, Consensus, and Future Trends. In International Journal of Advanced Research in Science, Communication and Technology. https://www.semanticscholar.org/paper/553850c1075ca4dd78736c0a39dd969b6b1d52fb

MR Islam, MM Rahman, & M Mahmud. (2021). A review on blockchain security issues and challenges. https://ieeexplore.ieee.org/abstract/document/9515276/

Mu-Ting Lin. (2011). Analysis and design of proxy signature schemes over braid groups. In Application Research of Computers. https://www.semanticscholar.org/paper/96f6fb7b1ec0d7706adbb6c93afe56b2b2bd8d9d

N Alnahawi, N Schmitt, & A Wiesmaier. (2023). On the state of crypto-agility. https://eprint.iacr.org/2023/487

N Chalaemwongwan. (2018). Notice of Violation of IEEE Publication Principles: State of the art and challenges facing consensus protocols on blockchain. https://ieeexplore.ieee.org/abstract/document/8343266/

N Eltayieb, R Elhabob, A Hassan, & F Li. (2020). A blockchain-based attribute-based signcryption scheme to secure data sharing in the cloud. In Journal of Systems Architecture. https://www.sciencedirect.com/science/article/pii/S1383762119304606

N Kannengießer, S Lins, & T Dehling. (2020). Trade-offs between distributed ledger technology characteristics. https://dl.acm.org/doi/abs/10.1145/3379463

N. Lee & T. Hwang. (1995). The security of He and Kiesler’s signature schemes. https://www.semanticscholar.org/paper/d9e036fc8b6184d2dea7d7a24db3441a7216aca6

N Six, N Herbaut, & C Salinesi. (2022). Blockchain software patterns for the design of decentralized applications: A systematic literature review. In Blockchain: Research and Applications. https://www.sciencedirect.com/science/article/pii/S209672092200001X

Nacha Chondamrongkul & Jing Sun. (2022). Architectural Refactoring for Functional Properties in Evolutionary Architecture. In 2022 IEEE 19th International Conference on Software Architecture (ICSA). https://ieeexplore.ieee.org/document/9779700/

Namya Aankur Gupta, M. Bansal, Seema Sharma, D. Mehrotra, & Misha Kakkar. (2023). Detection of Vulnerabilities in Blockchain Smart Contracts: A Review. In 2023 International Conference on Computational Intelligence, Communication Technology and Networking (CICTN). https://www.semanticscholar.org/paper/090174664702851f20b5cc732b15cdbaddaa7835

Navid Khoshavi, William Francois, A. Sargolzaei, & H. Chintakunta. (2019). A Survey on Blockchain Security. In 2019 SoutheastCon. https://ieeexplore.ieee.org/document/9020646/

Neha Arora & R. K. Sharma. (2022). Multi-signer Strong Designated Multi-verifier Signature Schemes based on Multiple Cryptographic Algorithms. In ArXiv. https://www.semanticscholar.org/paper/acdace8e5487be368bcf48cfe481f1f8ad67223d

Nils Amiet. (2021). Blockchain Vulnerabilities in Practice. In Digital Threats: Research and Practice. https://www.semanticscholar.org/paper/95469b16cc4595a2c20107710c6acbffa5f206cd

Nitin Kumar Tyagi & M. Goyal. (2023). Investigating Security Vulnerabilities and Tools of Blockchain Smart Contract: A Review. In Proceedings of the 2023 Fifteenth International Conference on Contemporary Computing. https://dl.acm.org/doi/10.1145/3607947.3608069

O. Zimmermann. (2015). Architectural Refactoring: A Task-Centric View on Software Evolution. In IEEE Software. https://ieeexplore.ieee.org/document/7057560/

P Mukherjee & C Pradhan. (2021). Blockchain 1.0 to blockchain 4.0—The evolutionary transformation of blockchain technology. https://link.springer.com/chapter/10.1007/978-3-030-69395-4_3

P. Roy, Kirill Morozov, Kazuhide Fukushima, S. Kiyomoto, & T. Takagi. (2019). Security Analysis and Efficient Implementation of Code-based Signature Schemes. In International Conference on Information Systems Security and Privacy. https://www.semanticscholar.org/paper/ef9aa728ce48e5047c4f0745018f29af7630d9a7

P Yeoh. (2017). Regulatory issues in blockchain technology. In Journal of Financial Regulation and Compliance. https://www.emerald.com/insight/content/doi/10.1108/JFRC-08-2016-0068/full/html

Pierre-Alain Fouque, Delphine Masgana, & F. Valette. (2009). Fault Attack on Schnorr Based Identification and Signature Schemes. In 2009 Workshop on Fault Diagnosis and Tolerance in Cryptography (FDTC). https://ieeexplore.ieee.org/document/5412861/

Prof M ShanmugamShoba & Dr. Rekha B Venkatapur. (n.d.). Enhancement of Signature Schemes for Heightening Security in Blockchain. https://www.semanticscholar.org/paper/9374d13351c5c2492189a0541919e21742250f3f

Q Lu, X Xu, HMND Bandara, & S Chen. (2021). Patterns for blockchain-based payment applications. https://dl.acm.org/doi/abs/10.1145/3489449.3490006

QAAS Mohammed & M Joudah. (2024). A survey on digital signature schemes. https://pubs.aip.org/aip/acp/article-abstract/3232/1/020057/3316644

Qun Lin, Hongyang Yan, Zhengan Huang, Wenbin Chen, Jian Shen, & Yi Tang. (2018). An ID-Based Linearly Homomorphic Signature Scheme and Its Application in Blockchain. In IEEE Access. https://ieeexplore.ieee.org/document/8302552/

R Belchior, A Vasconcelos, & S Guerreiro. (2021). A survey on blockchain interoperability: Past, present, and future trends. https://dl.acm.org/doi/abs/10.1145/3471140

R Guo, H Shi, Q Zhao, & D Zheng. (2018). Secure attribute-based signature scheme with multiple authorities for blockchain in electronic health records systems. In IEEE access. https://ieeexplore.ieee.org/abstract/document/8279429/

R Halim. (2022). Decentralization, Scalability, and Security Trade-off in Blockchain System: Comparison on Different Approaches. http://essay.utwente.nl/91994/

R Paulavičius, S Grigaitis, & A Igumenov. (2019). A decade of blockchain: Review of the current status, challenges, and future directions. In Informatica. https://journals.sagepub.com/doi/abs/10.3233/INF-2019-1245

Revatthy Krishnamurthy & K. Kaliyamurthie. (2015). Survey of One Time Signature Schemes onCloud Computing. In International Journal of Innovative Research in Computer and Communication Engineering. https://doi.org/10.15680/IJIRCCE.2015.0304159

S Al-Farsi, MM Rathore, & S Bakiras. (2021). Security of blockchain-based supply chain management systems: challenges and opportunities. In Applied Sciences. https://www.mdpi.com/2076-3417/11/12/5585

S. Alqahtani & M. Demirbas. (2021). Bottlenecks in Blockchain Consensus Protocols. In 2021 IEEE International Conference on Omni-Layer Intelligent Systems (COINS). https://ieeexplore.ieee.org/document/9524210/

S. Babu, Razan Abdulhammed, K. Elleithy, & S. Suparshya Babu. (2017). Blind Digital Signature schemes with four particle entanglement states. In 2017 IEEE Long Island Systems, Applications and Technology Conference (LISAT). https://ieeexplore.ieee.org/document/8001970/

S. Devidas, Subba Rao Y.V., & Rukma Rekha. (2021). A decentralized group signature scheme for privacy protection in a blockchain. In International Journal of Applied Mathematics and Computer Science. https://sciendo.com/article/10.34768/amcs-2021-0024

S Janin, K Qin, & A Mamageishvili. (2020). Filebounty: Fair data exchange. https://ieeexplore.ieee.org/abstract/document/9229692/

S. Kavitha, J. Srinivasan, P. Ramachandran, & I. Nasurulla. (2024). Enhanced cryptographic performance and security using optimized edward-elgamal signature scheme for IoT and blockchain applications. In International Journal on Smart Sensing and Intelligent Systems. https://sciendo.com/article/10.2478/ijssis-2024-0032

S. Mishra & T. Sahoo. (2014). A survey on group signature schemes. https://www.semanticscholar.org/paper/f5b2d3259e59e9defd256824f109a68ca8390ecb

S Singh, ASMS Hosen, & B Yoon. (2021). Blockchain security attacks, challenges, and solutions for the future distributed iot network. In Ieee Access. https://ieeexplore.ieee.org/abstract/document/9323061/

S. Zeadally & Jacques Bou Abdo. (2019). Blockchain: Trends and future opportunities. In Internet Technology Letters. https://onlinelibrary.wiley.com/doi/10.1002/itl2.130

SAK Thyagarajan & G Malavolta. (2021). Lockable signatures for blockchains: Scriptless scripts for all signatures. https://ieeexplore.ieee.org/abstract/document/9519419/

SB Sadkhan & RSB Sadkhan. (2022). Analysis of different types of digital signature. https://ieeexplore.ieee.org/abstract/document/9807502/

Silas Mutie Nzuva. (2024). Revisiting Blockchain Technologies and Smart Contracts Security: A Pragmatic Exploration of Vulnerabilities, Threats, and Challenges. In Asian Journal of Research in Computer Science. https://www.semanticscholar.org/paper/4b1c756977aa08faf1c95156561111212aae3916

Sinan Ergezer, Holger Kinkelin, & Filip Rezabek. (2020). A Survey on Threshold Signature Schemes. https://www.semanticscholar.org/paper/edd1462577215c63865321a75d11091990edb6e0

Sirine Sayadi, S. Rejeb, & Z. Choukair. (2018). Blockchain Challenges and Security Schemes: A Survey. In 2018 Seventh International Conference on Communications and Networking (ComNet). https://ieeexplore.ieee.org/document/8621944/

SJ Basha, VS Veesam, & T Ammannamma. (2021). Security enhancement of digital signatures for blockchain using EdDSA algorithm. https://ieeexplore.ieee.org/abstract/document/9388411/

SN Khan, F Loukil, & C Ghedira-Guegan. (2021). Blockchain smart contracts: Applications, challenges, and future trends. https://link.springer.com/article/10.1007/s12083-021-01127-0

SS Kushwaha, S Joshi, D Singh, M Kaur, & HN Lee. (2022). Systematic review of security vulnerabilities in ethereum blockchain smart contract. In Ieee Access. https://ieeexplore.ieee.org/abstract/document/9667515/

Stefan Arseni, Emil Bureacă, & Iulian Aciobăniței. (2024). Digital Signatures Long-Term Preservation Services, IPFS and Blockchain are a Good Match. In 2024 15th International Conference on Communications (COMM). https://ieeexplore.ieee.org/document/10741494/

T. Hardjono, A. Lipton, & A. Pentland. (2018). Towards a Design Philosophy for Interoperable Blockchain Systems. In ArXiv. https://www.semanticscholar.org/paper/dfc4d6734f64d6e74a8d4cfc5917240554c00b54

T Hyla & J Pejaś. (2020). Long-term verification of signatures based on a blockchain. In Computers & Electrical Engineering. https://www.sciencedirect.com/science/article/pii/S0045790618327381

Tam T. Huynh, T. Nguyen, & Hanh Tan. (2019). A Survey on Security and Privacy Issues of Blockchain Technology. In 2019 International Conference on System Science and Engineering (ICSSE). https://www.semanticscholar.org/paper/ab888aac462edd192d8a17e401294a974a824536

Tinam Sharma & S. Gajbhiye. (2016). A Survey Paper on Various ID Based Proxy Signature Schemes. https://www.semanticscholar.org/paper/252c7c36d175d0aa66ab3c145cd12ef84abba3ce

TM Fernandez-Carames & P Fraga-Lamas. (2020). Towards post-quantum blockchain: A review on blockchain cryptography resistant to quantum computing attacks. In IEEE access. https://ieeexplore.ieee.org/abstract/document/8967098/

Tuan Nguyen Kim, L. H. Dung, & Ho N. Duy. (2024). Construction of Digital Signature Schemes Based on a New Form of the Discrete Logarithm Problem. In 2024 IEEE International Conference on Consumer Electronics-Asia (ICCE-Asia). https://ieeexplore.ieee.org/document/10773853/

V Buterin, J Illum, M Nadler, & F Schär. (2024). Blockchain privacy and regulatory compliance: Towards a practical equilibrium. https://www.sciencedirect.com/science/article/pii/S2096720923000519

V Hassija, G Bansal, & V Chamola. (2019). Blockcom: A blockchain based commerce model for smart communities using auction mechanism. https://ieeexplore.ieee.org/abstract/document/8756808/

V Srivastava, SK Debnath, & B Bera. (2022). Blockchain-envisioned provably secure multivariate identity-based multi-signature scheme for Internet of Vehicles environment. https://ieeexplore.ieee.org/abstract/document/9779932/

W Fang, W Chen, W Zhang, J Pei, & W Gao. (2020). Digital signature scheme for information non-repudiation in blockchain: a state of the art review. https://link.springer.com/article/10.1186/s13638-020-01665-w

W Gao, WG Hatcher, & W Yu. (2018). A survey of blockchain: Techniques, applications, and challenges. https://ieeexplore.ieee.org/abstract/document/8487348/

Wang Ping-shui. (2007). Security Analysis of Two Group Signature Schemes. In Computer Technology and Development. https://www.semanticscholar.org/paper/b1086eac1092e5fb5b661e20586585ee44ac6015

Wang Xin-mei. (2003). Improvement of two ID-based digital signature schemes. In Journal of China Institute of Communications. https://www.semanticscholar.org/paper/887e211a01cd4351ac62097351565d699d0f3de1

Wangze Ni, Han Wu, Peng Cheng, Lei Chen, Xuemin Lin, Lei Chen, Xin Lai, & Xiao Zhang. (2020). CoinMagic: A Differential Privacy Framework for Ring Signature Schemes. In ArXiv. https://www.semanticscholar.org/paper/c0109756c534777cee53c5d3391712fcc230d013

Wei Bi, Xiaoyun Jia, & M. Zheng. (2018). A Secure Multiple Elliptic Curves Digital Signature Algorithm for Blockchain. In ArXiv. https://www.semanticscholar.org/paper/9b39cafa08842f7ffcafe7945ccde95eaa3c865a

Wouter van der Linde. (2018). Post-quantum blockchain using one-time signature chains. https://www.semanticscholar.org/paper/f38c562c21fa1a94871e5f577669f7c4b9520632

X Chen, S Xu, Y Cao, Y He, & K Xiao. (2023). AQRS: Anti-quantum ring signature scheme for secure epidemic control with blockchain. In Computer Networks. https://www.sciencedirect.com/science/article/pii/S1389128623000403

X Xu, C Pautasso, L Zhu, Q Lu, & I Weber. (2018). A pattern collection for blockchain-based applications. https://dl.acm.org/doi/abs/10.1145/3282308.3282312

Xiang Zou & Peng Zeng. (2023). A New Digital Signature Primitive and Its Application in Blockchain. In IEEE Access. https://ieeexplore.ieee.org/document/10138164/

Xiangfu Zou & Daowen Qiu. (2010). Security analysis and improvements of arbitrated quantum signature schemes. In Physical Review A. https://www.semanticscholar.org/paper/630918325349406630fc8056442dd8fb0d478ae8

Xiaodong Liu & Jun Feng. (2021). Trusted Blockchain Oracle Scheme Based on Aggregate Signature. In Journal of Computer and Communications. https://www.scirp.org/journal/paperinformation?paperid=108068

Xiaoying Zheng, Yongxin Zhu, & Xueming Si. (2019). A Survey on Challenges and Progresses in Blockchain Technologies: A Performance and Security Perspective. In Applied Sciences. https://www.mdpi.com/2076-3417/9/22/4731

Xinyu Wang. (2019). Research on ECDSA-Based Signature Algorithm in Blockchain. https://www.semanticscholar.org/paper/e6ccab9d65aff86fd89b2f3c5e86472a0ec799da

Y Merrad, MH Habaebi, EAA Elsheikh, & FEM Suliman. (2022). Blockchain: Consensus algorithm key performance indicators, trade-offs, current trends, common drawbacks, and novel solution proposals. In Mathematics. https://www.mdpi.com/2227-7390/10/15/2754

Y Sun, R Zhang, X Wang, & K Gao. (2018). A decentralizing attribute-based signature for healthcare blockchain. https://ieeexplore.ieee.org/abstract/document/8487349/

Y Xiao, N Zhang, W Lou, & YT Hou. (2020). A survey of distributed consensus protocols for blockchain networks. https://ieeexplore.ieee.org/abstract/document/8972381/

Yongge Wang. (2020). A Review of Threshold Digital Signature Schemes. https://www.semanticscholar.org/paper/8286f186f5e7ff60e56f76a07f523e2ce92161d3

Yue-Lei Xiao, Peng Zhang, & Yuhong Liu. (2022). Secure and Efficient Multi-Signature Schemes for Fabric: An Enterprise Blockchain Platform. In IEEE Transactions on Information Forensics and Security. https://ieeexplore.ieee.org/document/9276422/

Yulong Gao, Xueting Chen, & Wenqian Shang. (2024). A Lattice-based Linkable Ring Signature Scheme for Blockchain Privacy Protection. In 2024 IEEE/ACIS 27th International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD). https://ieeexplore.ieee.org/document/10673921/

Yun Wei, Guo-Hua Xiong, Xinglin Zhang, & Wansu Bao. (2009). Security Analysis and Design of Proxy Signature Schemes over Braid Groups. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/cb19161f5f01d5009ad523eb2129dcf443173872

Z Wenhua, F Qamar, TAN Abdali, R Hassan, & STA Jafri. (2023). Blockchain technology: security issues, healthcare applications, challenges and future trends. In Electronics. https://www.mdpi.com/2079-9292/12/3/546

Zhang Guo. (2007). Survey on Transitive Signature Schemes. In Computer Science. https://www.semanticscholar.org/paper/2332959a457b30bd9a212054228918162a084667

Zhengying Cai, Jing Qu, Pingping Liu, & Jiao Yu. (2019). A Blockchain Smart Contract Based on Light- Weighted Quantum Blind Signature. In IEEE Access. https://ieeexplore.ieee.org/document/8835013/

Zijian Bao, De-biao He, Cong Peng, Min Luo, & K. Choo. (2023). An Identity-Based Adaptor Signature Scheme and its Applications in the Blockchain System. In IEEE Open Journal of the Computer Society. https://ieeexplore.ieee.org/document/10234020/



Generated by Liner
https://getliner.com/search/s/5926611/t/85555004