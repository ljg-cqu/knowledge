'ZenGo-X [ ].' Requirements: 1. Ensure compliance with MECE. 2. Classify/categorize logically and appropriately if necessary. 3. Explain with analogy and examples. 4. Use numbered lists for clear explanations when possible. 5. Describe core elements, components, factors and aspects. 6. List core evaluation dimensions and corresponding evaluations if applicable. 7. Describe their concepts, definitions, functions, and characteristics. 8. Clarify their purposes and assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect). 9. Describe relevant markets, ecosystems, regulations, and economic models, and explain the corresponding strategies used to generate revenue. 10. Describe their work mechanism concisely first and then explain how they work with phase-based workflows throughout the entire lifecycle. 11. Clarify their preconditions, inputs, outputs, immediate outcomes, long-term impacts, and potential implications. 12. Clarify their underlying laws, axioms, theories, and patterns. 13. Describe the design philosophy and architectural features. 14. Provide ideas, techniques, and means of architectural refactoring. 15. Clarify relevant frameworks, models, and principles. 16. Clarify their origins, evolutions, and trends. 17. List key historical events, core factual statements, raw data points, and summarized statistical insights. 18. Clarify techniques, methods, approaches, protocols, and algorithms.  19. Describe contradictions and trade-offs. 20. Identify and list all major competitors (including the one being searched at present) with concise descriptions within the target market or industry segment. 21. Conduct a comprehensive competitor analysis to evaluate each competitor’s (including the one being searched at present) operational strategies, product offerings, market position, and performance metrics. 22. Perform a SWOT analysis for each competitor (including the one being searched at present), categorizing findings into strengths, weaknesses, opportunities, and threats. 23. Clarify principles, rules, constrains, limitations, vulnerabilities, challenges, obstacles, and risks. 24. Describe potential security vulnerabilities, troubleshooting methods, attack tactics, prevention methods and emergency measures. 25. Describe potential performance bottlenecks, troubleshooting methods and optimization measures. 26. Explain priorities, use cases, pitfalls, and best practices. 27. Clarify cause-and-effect relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 28. Clarify interdependency relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 29. Clarify cardinality-based relationships (1:1, 1:M, M:N). 26. Clarify contradictory relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 30. Describe the existing non-trivial problems and potential approaches to address them. 31. Introduce the relevant research topics of significant value that remain to be overcome. 32. Introduce the possible directions and approaches of within-domain and cross-domain innovation. 33. Predict the ultimate form of the related development. 34. Make a summary table at the end with purposes, characteristics, use cases, ect. for clarity. 35. Append the terminologies, formulas, and analogies at the end with concise descriptions for each item.

Thu Jun 12 2025

### Logical Classification and MECE Compliance

To ensure clarity and coverage, all features and aspects of the ZenGo-X multi-party Ed25519 scheme are organized into mutually exclusive, collectively exhaustive (MECE) categories. These include technical components, operational workflow, security models, design philosophy, market context, evaluation, and innovation pathways. This structure prevents overlaps and gaps, enhancing both logical rigor and practical utility.

---

### Core Elements, Components, Factors, and Aspects

1. **Distributed Key Generation (DKG)**: Enables parties to collectively create key shares without any party knowing the full private key.
2. **Threshold EdDSA**: Implements a (t, n)-threshold model requiring collaboration among t out of n participants for signing.
3. **Aggregated Signatures**: Allows multiple signers to produce a single, compact signature.
4. **Accountable-Subgroup Multisignatures**: Provides attribution for which subsets participated in signing.
5. **Security Fail-safes**: Protocol halts if malicious parties are detected during key generation or signing.
6. **Alignment with Ed25519 and RFC8032**: Ensures standards compliance, facilitating interoperability.
7. **Use of Rust Programming Language**: Chosen for safety and performance.

---

### Concepts, Definitions, Functions, and Characteristics

- **Concept**: Secure and efficient multi-party digital signatures over Ed25519, distributing trust among multiple participants.
- **Definition**: A signature scheme where key shares are held by distinct parties, preventing any single entity from forging signatures.
- **Functions**:
  1. Key generation (DKG)
  2. Threshold signing
  3. Verification (identical to standard Ed25519)
  4. Subgroup accountability
- **Characteristics**: Protocol is efficient, uses standard-compliant Ed25519 signatures, operates under a strict abort-on-malicious-detection model, and uses distributed Schnorr-based primitives.

---

### Purpose and Assumptions

1. **Value Assumption**: Multi-party computation enhances security and trust by removing single points of failure.
2. **Descriptive Assumption**: Ed25519 is fast, secure, and widely adopted; multi-party signatures extend these benefits to collaborative environments.
3. **Prescriptive Assumption**: Collaborative authentication is essential for high-security systems (blockchain, wallets, etc.).
4. **Worldview**: Decentralization and cryptographic guarantees are superior to traditional key custody.
5. **Cause-and-Effect**: Distributing keys <-reduces-> risk of compromise; threshold enforcement <-prevents-> single-point failures.

**Analogy:**  
Imagine a secure vault that can only be opened when a certain number of trusted managers each provide their unique key fragment. No single manager can open the vault alone, making theft or fraud extremely difficult.

---

### Work Mechanism and Phase-Based Workflow

**Concise Mechanism:** Parties run a distributed key generation protocol, splitting the secret key among themselves. When a signature is needed, a qualifying subset (threshold) of parties cooperates to create a valid Ed25519 signature, with neither party ever possessing the entire key.

**Lifecycle Phases:**
1. **Setup & Key Generation**:
   - All n parties participate in DKG to create private key shares and a shared public key.
   - Abort if any party acts maliciously.
2. **Signature Generation**:
   - Threshold t parties cooperate using their key shares to compute partial signatures, which are combined.
   - Protocol halts on detection of misbehavior.
3. **Verification**:
   - Anyone can verify the signature with the standard Ed25519 algorithm; verification is transparent to the fact that a multiparty process was used.

**Example Analogy:**  
Like a council vote where a subset quorum produces a seal (signature) that is indistinguishable from one produced by a single leader, but only with quorum consent.

---

### Preconditions, Inputs, Outputs, Outcomes, and Implications

1. **Preconditions**:
   - All parties agree on protocol parameters and trust the initial communication.
   - Secure, authenticated channels for DKG and signing rounds.
2. **Inputs**:
   - Elliptic curve parameters
   - Hash function specification
   - Random seed for each party
   - Message to be signed
3. **Outputs**:
   - Valid Ed25519 signature
   - Public key verifiable by anyone
4. **Immediate Outcomes**:
   - Key shares distributed, joint signatures generated, and aborts detected.
5. **Long-term Impacts**:
   - Enhanced security for wallets, blockchains, and authentication systems.
   - Foundation for future distributed cryptographic protocols.
6. **Implications**:
   - Improved user trust in distributed systems; increases resilience but adds protocol complexity.

---

### Underlying Laws, Axioms, Theories, and Patterns

- **Elliptic Curve Discrete Logarithm Problem (ECDLP):** Core to Ed25519’s security.
- **EdDSA and Schnorr Signatures**: Protocol leverages deterministic and threshold-friendly characteristics of these schemes.
- **Shamir Secret Sharing:** Used for securely distributing private key fragments.
- **Zero-Knowledge Proofs & Non-Malleable Commitments:** Used to prevent cheating during key generation and signing.
- **Random Oracle Model:** Hash functions are assumed secure pseudo-random generators.

---

### Design Philosophy and Architectural Features

- **Philosophy**: Favor security and transparency over operational robustness—protocol halts at any sign of malicious activity, preferring “fail-safe” to “fail-open”.
- **Architecture**:
   1. Modular, separating cryptographic primitives from protocol logic.
   2. Written in Rust for safety and performance.

---

### Architectural Refactoring: Ideas and Techniques

1. **Module Separation**: Isolate key generation, signing, and communication layers.
2. **Layered Security**: Refactor protocols to independently update zero-knowledge, encryption, or hashing routines.
3. **Communication Optimization**: Reduce rounds, add async processing, and minimize message payloads.
4. **Upgradability**: Design with plug-and-play primitives for easier upgrades as new cryptographic techniques emerge.
5. **Robust Recovery**: Modularize recovery and abort handling for easier maintenance.

---

### Relevant Frameworks, Models, and Principles

- **MPC Model**: Secure Multi-party Computation for collaborative key management and signing.
- **Threshold Cryptography**: Any t of n validates actions; supports both availability and confidentiality.
- **RFC8032 Compliance**: Ensures interoperability and standards-based signature format.

---

### Origins, Evolution, and Trends

- **Origins**: Descends from Ed25519 and Schnorr signature innovation due to demand for secure, fast digital signatures.
- **Evolution**: Shift from single-party control to threshold and multi-party architectures for distributed trust in wallets and blockchains.
- **Trends**: Integration with DeFi, cross-chain bridges, and custodial services, emphasis on efficient, deterministic, and stateless multi-party protocols.

---

### Key Historical Events, Facts, and Data Points

1. **Ed25519 & EdDSA adoption**: Rapid integration into DNSSEC, TLS, blockchain, and decentralized systems.
2. **Threshold/multi-party signatures**: Now increasingly proposed for cryptocurrency wallet custody.
3. **Empirical advances**: Demonstrated compatibility with embedded and cloud systems.
4. **Performance data**: Efficient FPGA designs can produce thousands of signatures per second.

---

### Techniques, Methods, Protocols, and Algorithms

1. **Distributed Key Generation (DKG) based on Shamir Secret Sharing**.
2. **Threshold EdDSA (t,n) signing with additive secret sharing**.
3. **Verifiable random nonce generation** via elliptic curve PRFs.
4. **Zero-Knowledge Proofs for commitments and correctness**.
5. **Standard EdDSA verification for output signatures**.

---

### Contradictions and Trade-Offs

1. **Efficiency vs. Security**: Secure multi-party hash computation is complex; ZenGo-X sidesteps with output-indistinguishable variants.
2. **Determinism vs. Collaborative Nonce Generation**: EdDSA's deterministic design is at odds with the multi-party necessity for randomizable, verifiable nonces.
3. **Malicious Abort vs. Fault Tolerance**: Protocol prefers aborting over risk, limiting robustness.
4. **Compatibility vs. Flexibility**: Adapting threshold logic without altering Ed25519 signature output restricts protocol design leeway.

---

### Major Competitors

| Name                                      | Description                                                                                             |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------|
| ZenGo-X Multi-Party Ed25519                | Rust-based open-source scheme emphasizing efficiency, threshold security, and accountability            |
| Threshold EdDSA with Offline Recovery      | (2,3) threshold scheme supporting offline participants and strong security proofs               |
| Efficient Multi-party EdDSA (Q Feng et al.)| Focuses on low communication, identifiable aborts, and fault tolerance for blockchains            |
| Stateless Deterministic Multi-party EdDSA  | Optimized for minimal rounds and state, strong for embedded/smartcard use                         |
| Threshold EdDSA for Blockchain (Y Shi et al.)| Arbitrary (t, n) threshold, performance tuned for cloud/embedded/DeFi                          |

---

### Competitor Analysis

| Competitor                             | Strategies                  | Offerings                            | Market Position             | Performance Metrics      |
|----------------------------------------|-----------------------------|--------------------------------------|----------------------------|--------------------------|
| ZenGo-X                               | MPC, Open-source, Rust      | Threshold & aggregated signatures    | Blockchain wallets          | Efficient, abort on fault|
| Q Feng Efficient EdDSA                 | Identifiable aborts         | Blockchain-friendly protocols        | Academic to practical       | Low comm., fault-tolerance|
| Battagliola et al. Threshold EdDSA     | Offline recovery, strong proofs| Custody with recovery              | Custody, DeFi               | Security over speed      |
| Stateless Deterministic EdDSA          | Stateless, deterministic    | Embeddable protocols                 | IoT, smartcards             | Ultra-low comm.          |
| Y Shi Blockchain Threshold EdDSA       | Arbitrary threshold         | DeFi, cross-chain           | Blockchain platforms         | High compatibility       |

---

### SWOT Analysis

#### ZenGo-X Multi-Party Ed25519
- **Strengths**: Standards compliance, strong security, accountability, open-source
- **Weaknesses**: Halts on malicious activity, limited robustness
- **Opportunities**: Blockchain, wallet custody, smart authentication
- **Threats**: Increasing protocol complexity and competing threshold schemes

#### Competitor Examples
- *Q Feng*: Strong abort detection, could be slower in large n
- *Battagliola*: Unique recovery, extra protocol steps may reduce efficiency
- *Shi et al.*: Highly tunable for DeFi, but complexity increases for custom thresholds

---

### Principles, Rules, Constraints, Limitations, and Risks

- **Principle**: Distribute trust, resist single-party failure
- **Rule**: Abort protocol on malicious detection
- **Constraint**: Needs secure communication and reliable party behavior during DKG/signing
- **Limitation**: Not robust against persistent or coordinated faults
- **Risk**: Vulnerability to nonce reuse, side-channel, or protocol implementation bugs
- **Challenge**: Efficient, secure, concurrent signing with minimal comm.

---

### Security Vulnerabilities and Emergency Measures

- **Vulnerabilities**: Rogue-key, nonce, and fault attacks
- **Troubleshooting**: Sequential signing, protocol audits, ZKPs for commitments
- **Prevention**: Secure nonce protocols, abort on error, formal implementation reviews
- **Emergency Response**: Key revocation, protocol halt, forensic logging

---

### Performance Bottlenecks and Optimization

- **Bottlenecks**: DKG complexity, network round-trips
- **Troubleshooting**: Profile rounds, optimize modular arithmetic, reduce comm.
- **Optimization**: Precompute nonces, async rounds, hardware acceleration

---

### Priorities, Use Cases, Pitfalls, Best Practices

1. **Priorities**: Security, interoperability, efficiency
2. **Use Cases**: Multi-signature wallets, DeFi custody, cross-chain authentication
3. **Pitfalls**: Poor nonce management, insufficient side-channel defense
4. **Best Practices**: Use tested primitives, ensure sequential signing, audit trails

---

### Cause-and-Effect Relationships

- Distributed trust <-removes-> single-point vulnerabilities
- Malicious behavior <-triggers-> protocol abort
- Efficient DKG <-reduces-> setup overhead
- Key compromise <-mitigated by-> threshold enforcement
- Extra rounds <-increase-> security but <-increase-> communication delay

---

### Interdependency Relationships

- Parties <-> MPC protocol <-> Key shares
- Nonce agreement <-> Security <-> Interoperability
- DKG <-> Commitment/Proof <-> Signing phase

---

### Cardinality-Based Relationships

- (t, n)-threshold: t of n parties required for signing; fewer cannot act
- 1:M: One public key, multiple key shares
- M:N: Any M-out-of-N signers can produce signatures

---

### Contradictory Relationships

- Determinism <-conflicts with-> collaborative nonce management
- Security against aborts <-opposes-> continuous availability

---

### Existing Non-Trivial Problems and Potential Approaches

- **Nonce handling in multi-party**: Use PRF-based verifiable random generators.
- **Complex hash computations**: Employ output-indistinguishable variants and avoid full MPC over hash.
- **Online/offline party participation**: Refine recovery mechanisms and ZKP support.

---

### Significant Research Challenges

- Efficient, secure, and robust comm. protocols for DKG and signing.
- Nonce agreement and concurrency safety in practical deployments.
- Interoperability between disparate multi-party schemes.

---

### Innovation Pathways

- Stateless, deterministic, and post-quantum hybrid multi-party schemes.
- Hardware-supported acceleration for embedded/IoT use.
- Cross-protocol interoperability by mediated coordination or standardization.

---

### Ultimate Development Trajectory

Future schemes will balance robust security, low communication, and post-quantum readiness. We anticipate stateless, efficient, and highly modular multi-party signature stacks with provable security, hardware-friendly primitives, and hybrid cryptography for maximized interoperability in decentralized and blockchain-based ecosystems.

---

### Summary Table

| Aspect                     | Description/Value                                                                  |
|----------------------------|------------------------------------------------------------------------------------|
| **Purpose**                | Secure, decentralized signing for blockchains, wallets, authentication systems      |
| **Characteristics**        | Threshold, DKG, aggregated/accountable signatures, abort-on-malicious, Rust-based  |
| **Key Use Cases**          | Cryptocurrency wallets, DeFi custody, secure enterprise authorization              |
| **Inputs/Outputs**         | Inputs: {n parties, DKG, messages}; Outputs: Valid Ed25519 signatures              |
| **Security Model**         | Provably secure, non-interactive threshold, abort if misbehavior detected          |
| **Preconditions**          | Agreement on parameters, secure comms, honest majority for DKG                     |
| **Immediate Outcomes**     | Key shares, signatures, or abort                                                   |
| **Long-term Effects**      | Improved trust, reduced compromise risk, foundation for future distributed crypto   |
| **Design/Evaluation**      | Modular, compliant, efficient, open source; Strong in security, less robust on fault|
| **Market/Economics**       | Blockchain, DeFi, secure wallets; Revenue via licensing, SaaS, value-add solutions |
| **Competitors**            | ZenGo-X, Feng’s, Battagliola's, Shi et al., Stateless EdDSA                       |

---

### Terminologies, Formulas, and Analogies

- **Ed25519**: EdDSA using Curve25519, well-known for fast, secure digital signatures.
- **(t, n)-threshold**: Any t out of n parties are required for signing.
- **Distributed Key Generation**: All parties construct shares so the full key is never assembled.
- **Aggregated signature**: Many keys, one signature output as if single signer.
- **Zero-Knowledge Proof**: A cryptographic "seal of correctness" without revealing secrets.
- **Analogy—Vault keys**: Like a high-security bank vault needing multiple managers’ keys—no single one suffices.
- **Cause/effect notation**: Malicious detection <-triggers-> protocol abort.

---

This comprehensive analysis provides a logically organized, MECE-compliant structure for understanding ZenGo-X multi-party Ed25519 signature scheme: its concepts, mechanisms, evaluation, market fit, technical details, competitive context, and the direction of ongoing innovation.

Bibliography
A Dufka, V Sedlacek, & P Svenda. (2022). SHINE: Resilience via Practical Interoperability of Multi-party Schnorr Signature Schemes. In SECRYPT. https://www.scitepress.org/PublishedPapers/2022/111456/111456.pdf

A. Dufka, Vladimir Sedlacek, & P. Švenda. (2022). SHINE: Resilience via Practical Interoperability of Multi-party Schnorr Signature Schemes. In International Conference on Security and Cryptography. https://www.semanticscholar.org/paper/b6c0e75e547ad6d3e392065b37e86e8c126e3961

A Zimba & M Chishimba. (2019). On the economic impact of crypto-ransomware attacks: The state of the art on enterprise systems. In European Journal for Security Research. https://link.springer.com/article/10.1007/s41125-019-00039-8

AT Dumitrescu & J Pouwelse. (2025). TrustZero--open, verifiable and scalable zero-trust. In arXiv. https://arxiv.org/abs/2502.10281

BR Kumar, MV Jose, & JR Jeba. (2024). Schnorr Multi-Signatures with Key Aggregation for Privacy and Verifiable Randomness in Blockchain Cloud. https://ieeexplore.ieee.org/abstract/document/10559311/

C Shaik. (2021). Preventing counterfeit products using cryptography, qr code and webservice. In Comput. Sci. Eng. Int. J. https://www.academia.edu/download/79787324/11121cseij01.pdf

D. Bernstein, S. Josefsson, T. Lange, P. Schwabe, & Bo-Yin Yang. (2015). EdDSA for more curves. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/672b16ed99b203e997f50ef0cf7116aff9b2ab6e

D Roszak & Z Jaroucheh. (2023). Secure Multi-Party Computation for Digital Assets Custody Purpose-Analysis of Open-Source Implementations. https://ieeexplore.ieee.org/abstract/document/10338922/

HWH Wong & JPK Ma. (2024). Secure multiparty computation of threshold signatures made more efficient. https://www.ndss-symposium.org/wp-content/uploads/2024-601-paper.pdf

HWH Wong, JPK Ma, HHF Yin, & SSM Chow. (2023). How (Not) to build threshold EdDSA. https://dl.acm.org/doi/abs/10.1145/3607199.3607230

II Protocol, M Doty, V Ihnatiuk, Y Butko, & AY Korchynskyi. (n.d.). Golden Gate. https://ggxchain.io/wp-content/uploads/2023/09/Golden_Gate-v1.0.pdf

J Doerner, Y Kondi, & E Lee. (2019). Threshold ECDSA from ECDSA assumptions: The multiparty case. https://ieeexplore.ieee.org/abstract/document/8835354/

J Guruprakash & S Koppu. (2022). An Empirical Study to Demonstrate that EdDSA can be used as a Performance Improvement Alternative to ECDSA in Blockchain and IoT. In Informatica. https://www.informatica.si/index.php/informatica/article/view/3807

Jacqueline Brendel, Cas J. F. Cremers, Dennis Jackson, & Mang Zhao. (2021). The Provable Security of Ed25519: Theory and Practice. In 2021 IEEE Symposium on Security and Privacy (SP). https://www.semanticscholar.org/paper/cd7cdb27040cad5ab5eaf8c4b4b6ecae18484064

JL Hall, Y Hertzog, M Loewy, & MP Skerritt. (2023). Manifesting Unobtainable Secrets: Threshold Elliptic Curve Key Generation using Nested Shamir Secret Sharing. https://arxiv.org/abs/2309.00915

JP Aumasson, A Hamelink, & O Shlomovits. (2020). A survey of ECDSA threshold signing. In Cryptology ePrint Archive. https://eprint.iacr.org/2020/1390

K Sedghighadikolaei & AA Yavuz. (2023). A Comprehensive Survey of Threshold Signatures: NIST Standards, Post-Quantum Cryptography, Exotic Techniques, and Real-World Applications. In arXiv. https://arxiv.org/abs/2311.05514

KK Chalkias, J Lindstrøm, D Maram, & B Riva. (2024). Fastcrypto: Pioneering cryptography via continuous benchmarking. https://dl.acm.org/doi/abs/10.1145/3629527.3652266

L Brandão & M Davidson. (2023). Notes on threshold eddsa/schnorr signatures. https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8214B.ipd.pdf

L Brandao & R Peralta. (2023). Nist first call for multi-party threshold schemes. In doi. https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8214C.ipd.pdf

M Battagliola, R Longo, & A Meneghetti. (2023). Provably unforgeable threshold EdDSA with an offline participant and trustless setup. https://link.springer.com/article/10.1007/s00009-023-02452-9

M Polubelova. (2022). Building a formally verified high-performance multi-platform cryptographic library in F. https://inria.hal.science/tel-03981965/

Michele Battagliola, Riccardo Longo, Alessio Meneghetti, & M. Sala. (2020). A Provably-Unforgeable Threshold EdDSA with an Offline Recovery Party. In ArXiv. https://www.semanticscholar.org/paper/4497f519aeca39b595bde266b6432278731f0e5c

MJ Saarinen & D Smith-Tone. (2024). Post Quantum Cryptography. In 15th International Workshop. https://link.springer.com/content/pdf/10.1007/978-3-031-62743-9.pdf

MK Aguilera, C Burgelin, R Guerraoui, & A Murat. (2024). {DSig}: Breaking the Barrier of Signatures in Data Centers. https://www.usenix.org/conference/osdi24/presentation/aguilera

Mojtaba Bisheh-Niasar, R. Azarderakhsh, & Mehran Mozaffari-Kermani. (2021). Cryptographic Accelerators for Digital Signature Based on Ed25519. In IEEE Transactions on Very Large Scale Integration (VLSI) Systems. https://www.semanticscholar.org/paper/8c9f809e4fa81a36ae839d5b6621debd8579aebd

N. Moller & S. Josefsson. (2015). EdDSA and Ed25519. https://www.semanticscholar.org/paper/42c8651a93c7b500bf2938d6e82567214684fb76

O. Sury & R. Edmonds. (2017). Edwards-Curve Digital Security Algorithm (EdDSA) for DNSSEC. In RFC. https://www.semanticscholar.org/paper/5a988eb1b489af71cad1a1b65f25d2083792ea42

O. Zimmermann. (2015). Architectural Refactoring: A Task-Centric View on Software Evolution. In IEEE Software. https://www.semanticscholar.org/paper/f5b804fa467303b721cd33c91e856adeeb4629b8

P. Hallam-Baker. (2020). Threshold Signatures Using Ed25519 and Ed448. https://www.semanticscholar.org/paper/c9041be632aed7a0ac2ff6a4d9c05e760a3aeff7

Q Feng, D He, M Luo, & Z Li. (2020). Practical secure two-party EdDSA signature generation with key protection and applications in cryptocurrency. https://ieeexplore.ieee.org/abstract/document/9343153/

Q Feng, K Yang, K Zhang, X Wang, & Y Yu. (2025). Stateless Deterministic Multi-Party EdDSA Signatures with Low Communication. https://link.springer.com/chapter/10.1007/978-3-031-91832-2_9

Q Feng, K Yang, M Ma, & D He. (2023). Efficient multi-party EdDSA signature with identifiable aborts and its applications to blockchain. https://ieeexplore.ieee.org/abstract/document/10068261/

R Annessi & E Fast. (2021). Improving security for users of decentralized exchanges through multiparty computation. https://ieeexplore.ieee.org/abstract/document/9680483/

R. Edmonds & O. Sury. (2015). Ed25519 for DNSSEC. https://www.semanticscholar.org/paper/3aa9bfd5d10f9aaf5f20cdf484c5fb14629aad17

R. Housley. (2018). Use of Edwards-Curve Digital Signature Algorithm (EdDSA) Signatures in the Cryptographic Message Syntax (CMS). In RFC. https://www.semanticscholar.org/paper/fba8f651b3561c56793b81d53b90b42fff4009e8

R Jiang, Y Li, X Pu, X Wang, W Niu, & Z Song. (2025). A fair multi-party contract signing scheme based on off-chain protocols and on-chain smart contracts. https://link.springer.com/article/10.1007/s11227-024-06844-w

R Rokhjavan. (2023). Securing Multi-party Crypto Wallets. https://library-archives.canada.ca/eng/services/services-libraries/theses/Pages/item.aspx?idNumber=1415669719

S Bansod & L Ragha. (2022). Challenges in making blockchain privacy compliant for the digital world: some measures. In Sādhanā. https://link.springer.com/article/10.1007/s12046-022-01931-1

SA Mendrofa, MW Ardyani, & SS Carita. (2024). Unlocking the Future of Digital Currency: A Comparative Study of ECDSA vs. EdDSA Signatures with Oblivious Transfer Protocol. https://ieeexplore.ieee.org/abstract/document/10956318/

Shangping Wang, Lihua Liu, Juanjuan Chen, J. Sun, Xinwen Zhang, & Yaling Zhang. (2013). Lattice-Based Multi-party Concurrent Signatures Scheme. In 2013 5th International Conference on Intelligent Networking and Collaborative Systems. https://www.semanticscholar.org/paper/8fd1a7cad957108d5b28be8d8f127d1fc451ff99

Sinan Ergezer, Holger Kinkelin, & Filip Rezabek. (2020). A Survey on Threshold Signature Schemes. https://www.semanticscholar.org/paper/edd1462577215c63865321a75d11091990edb6e0

TS Schemes, LL Schacher, C Cachin, & M Barbaraci. (2024). ROAST in Rust. https://crypto.unibe.ch/archive/theses/2023.msc.lukas.schacher.pdf

W. Koch. (2016). EdDSA for OpenPGP. https://www.semanticscholar.org/paper/79b1a553789785bc1123264c38595e1ac161e7d9

Y Wang, B Li, J Wu, G Liu, Y Li, & Z Mao. (2025). An efficient multi-party signature for securing blockchain wallet. https://link.springer.com/article/10.1007/s12083-025-01958-1

Y Xie, Q Fan, C Zhang, T Wu, & Y Zhou. (2024). Accountable and secure threshold EdDSA signature and its applications. https://ieeexplore.ieee.org/abstract/document/10605124/

Yang Shi, Junqing Liang, Mianhong Li, Tianchen Ma, G. Ye, Jiangfeng Li, & Qinpei Zhao. (2022). Threshold EdDSA Signature for Blockchain-based Decentralized Finance Applications. In Proceedings of the 25th International Symposium on Research in Attacks, Intrusions and Defenses. https://www.semanticscholar.org/paper/1af850274ef8220699ce9fcb08be0403eb9259c1

Yolan Romailler & Sylvain Pelissier. (2017). Practical Fault Attack against the Ed25519 and EdDSA Signature Schemes. In 2017 Workshop on Fault Diagnosis and Tolerance in Cryptography (FDTC). https://www.semanticscholar.org/paper/8bf3dcb396a6f9494ba2463cf3b80c0fd728eeb3



Generated by Liner
https://getliner.com/search/s/5926611/t/85554255