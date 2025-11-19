### Multi-Chain MPC Wallet Architecture: A Deep Dive into Security, Performance, and Integration

Multi-Party Computation (MPC) wallets represent a significant advancement in digital asset security and management, moving beyond traditional single-key and multi-signature approaches to address critical vulnerabilities and enhance user experience. These wallets leverage cryptographic techniques to split a private key into multiple encrypted shares, which are then distributed among different parties or devices. This distributed architecture ensures that no single entity ever possesses the complete private key, even during transaction signing, effectively eliminating single points of failure that plague conventional wallet solutions. The global MPC Wallet market reached USD 1.8 billion in 2024 and is projected to grow to over USD 12.6 billion by 2033, driven by increasing cyber threats and the demand for robust digital asset management solutions across diverse industries.

### Core Architecture and Cryptographic Foundations

The fundamental design of an MPC wallet hinges on sophisticated cryptographic protocols that enable collaborative key management and transaction signing. These protocols ensure that cryptographic operations can be performed jointly by multiple parties without any single party ever exposing its individual secret share. This approach fundamentally improves security by distributing trust and creating a higher barrier for attackers who would need to compromise multiple independent entities to access funds.

#### Distributed Key Generation (DKG)

At the heart of an MPC wallet is the Distributed Key Generation (DKG) process, which securely creates cryptographic shares without a trusted third party. Instead of one entity generating a private key and then splitting it, DKG protocols allow multiple participants to jointly compute and establish their respective key shares from the outset, ensuring no single party ever sees the complete key. This technique relies on principles like Shamir's Secret Sharing, where a secret is divided into 'n' shares, and any 'k' shares (where 'k' is the predefined threshold) can reconstruct the original secret, but 'k-1' shares yield no information. Robust DKG schemes are provably secure against adaptive malicious adversaries, preventing collusion during the key generation phase itself.

#### Key Share Management and Storage

Once generated, key shares must be managed and stored with utmost care to maintain the integrity and availability of the wallet. Shares are often encrypted and distributed across various devices or services, providing redundancy and preventing a single compromised device from leading to asset loss. For instance, a common consumer model is the 2-of-3 threshold, where shares are held by the user's device, the service provider, and a backup recovery service, allowing any two shares to authorize transactions. Enterprise deployments typically use more complex arrangements like 3-of-5 models, distributing shares across multiple user devices, service providers, and hardware security modules (HSMs) to achieve granular control and redundancy. Fireblocks, for example, utilizes GG18-based protocols and stores key shares in secure HSMs, enforcing t-of-n approvals for institutional clients.

#### Threshold Signature Schemes (TSS)

Threshold Signature Schemes (TSS) are a specific application of MPC that enable multiple parties to collectively sign a transaction without reconstructing the full private key. These schemes define the cryptographic protocols for this collaborative signing process, ensuring that the final signature is valid on the blockchain. A comprehensive survey of threshold signatures covers conventional and post-quantum cryptography settings, including custom-design and standard approaches.

##### Threshold ECDSA

The Elliptic Curve Digital Signature Algorithm (ECDSA) is a cornerstone for many cryptocurrencies like Bitcoin and Ethereum. Implementing threshold ECDSA has been a significant challenge due to its complexity. The *GG18 protocol*, developed by Gennaro and Goldfeder in 2018, was the first practical threshold ECDSA implementation, though it required nine rounds of communication for signing. This was improved by *GG20*, which reduced communication complexity and addressed security vulnerabilities. The state-of-the-art *CGGMP21 protocol* further refined this, requiring only four signing rounds, making it efficient enough for practical use while enhancing security proofs. However, even modern protocols like GG18, GG20, and CGGMP21 have been subject to vulnerabilities like TSSHOCK, highlighting the continuous need for vigilance and auditing in their implementations.

##### Threshold EdDSA

Threshold EdDSA (Edwards-curve Digital Signature Algorithm) offers an alternative to ECDSA. Research has presented EdDSA-compatible multi-party digital signature schemes that support an offline participant during the key-generation phase without relying on a trusted third party. These schemes are proven secure against adaptive malicious adversaries under standard assumptions, often requiring only two communication rounds in the signature generation phase and avoiding expensive multi-party evaluation of cryptographic hash functions. This makes EdDSA attractive for custodial solutions requiring high resiliency, where a third party can be brought online after key generation if one of the primary parties becomes unavailable.

##### FROST

FROST (Flexible Round-Optimized Schnorr Threshold) is another significant threshold signature scheme, often preferred for Schnorr-based signatures. While GG18 and GG20 build upon previous work in threshold cryptography, FROST often offers advantages in terms of efficiency and simplicity, particularly when compared to the complexity of threshold ECDSA. The performance of different threshold signature schemes like FROST is a critical consideration, especially in leader-based consensus systems.

### Transaction Signing and Operational Flow

The process of signing a transaction with an MPC wallet requires a coordinated effort from multiple parties holding key shares. This multi-round communication protocol involves the exchange of cryptographic proofs, where each party contributes to the signature without ever revealing its secret share.

#### Signing Process and Performance

During transaction signing, parties engage in multiple communication rounds: generating and broadcasting commitments, exchanging revealed values, computing partial signatures, and finally combining them into the final signature. Each round necessitates all participating parties to be online and responsive. Network latency significantly impacts signing speed; a transaction might complete in 2-5 seconds on good connections but extend to 10-30 seconds on poor ones. This is a key reason why MPC wallets can sometimes feel slower than hardware wallets, which sign almost instantly once connected. The geographical distribution of shares, while beneficial for security, can also increase signing latency. For example, cross-continental distribution can add 3-5 seconds, and truly global distribution 5-10 seconds per transaction.

#### Throughput and Optimization

MPC wallets face inherent throughput limitations, typically handling 10-20 transactions per minute for consumer implementations and 50-100 transactions per minute for enterprise solutions. Even highly optimized deployments rarely exceed 500 transactions per minute. These constraints make MPC unsuitable for high-frequency trading, MEV extraction, or mass payment processing that demands thousands of rapid transactions. To mitigate these performance challenges, advanced MPC protocols incorporate techniques such as precomputation (performing parts of the cryptographic computation offline before the actual signing request) and batch signing (signing multiple transactions in a single MPC ceremony).

### Security Engineering and Risk Mitigation

While MPC wallets eliminate single points of failure by design, they are not inherently "unhackable" and introduce their own set of security considerations and attack vectors. Robust security engineering is paramount to protect digital assets.

#### Attack Vectors and Vulnerabilities

Potential vulnerabilities in MPC wallets can arise from several sources:
-   **Compromised Key Generation Ceremonies**: If the initial randomness or protocol execution during DKG is subverted, the security of the entire key can be compromised.
-   **Side-Channel Attacks**: During the signing process, information about individual shares could leak through side-channel attacks (e.g., timing, power consumption).
-   **Social Engineering**: Attackers might target multiple share holders simultaneously through social engineering tactics.
-   **Implementation Bugs**: Discovered and patched bugs in MPC protocols, such as the TSSHOCK vulnerabilities affecting GG18, GG20, and CGG+21 protocols in August 2023, underscore the importance of robust implementation and auditing. An unnamed exchange discovered and patched a vulnerability in their custom MPC implementation in 2024, emphasizing the need to use audited, standard protocols.
-   **Dependency on Providers**: Most consumer MPC wallets rely on trusting the wallet provider with one or more key shares, making the provider a critical dependency for wallet access and recovery.

#### Mitigation Strategies and Best Practices

Mitigating these risks requires a multi-layered approach:
-   **Secure Implementation**: Adhering to audited, standard cryptographic protocols is crucial, avoiding custom or untested implementations. Regular share refresh ceremonies reduce the risk of long-term share compromise.
-   **Hardware Security Modules (HSMs)**: Integrating HSMs for key share storage provides tamper-resistant environments, particularly favored by enterprises for large asset portfolios.
-   **Zero-Knowledge Proofs**: MPC leverages zero-knowledge proofs to allow parties to prove correct calculations without revealing their inputs, ensuring that even if some shares below the threshold are compromised, the private key remains unknown.
-   **Device Attestation and Multi-Factor Authentication (MFA)**: Enhancing security for individual users involves enabling all available authentication factors and testing recovery procedures regularly. Device attestation can confirm the integrity of the device holding a share.
-   **Anomaly Detection and Approval Workflows**: For organizations, monitoring signing patterns for anomalies can indicate compromise. Implementing robust approval and limit management flows for high-value transactions provides additional safeguards.
-   **Recovery Planning**: Thorough recovery planning is critical, involving understanding share distribution, securely maintaining recovery shares, and following specific recovery procedures which vary by provider. Regular testing of recovery processes on a second device is highly recommended. The 2023 Multichain bridge incident, where $126 million was locked due to a missing CEO holding critical shares, highlights the danger of single-person dependencies in share distribution.
-   **Key Rotation**: Unlike traditional wallets, MPC systems can refresh key shares periodically without changing the wallet address, preserving transaction history and eliminating the need to update deposit addresses.

### Cross-Chain Compatibility and Integration

The proliferation of diverse blockchain ecosystems necessitates that modern wallets, particularly MPC-based ones, offer robust cross-chain compatibility. This involves navigating different consensus models, transaction structures, and signature standards across various chains.

#### Supporting Multiple Blockchain Ecosystems

MPC wallets are designed to support a wide array of blockchains, including Ethereum, EVM Layer 2s, Bitcoin, and Solana. The ability of MPC to generate standard transactions indistinguishable from single-signature transactions, and its cryptographic layer operation, allows it to work across all blockchains, including Bitcoin, which multisig cannot natively do without specific smart contract implementations. For instance, Fireblocks supports direct custody for over 50 blockchains. Cross-chain functionality is crucial for facilitating the free flow of value and information in the Web3.0 era, acting as a bridge connecting "blockchain islands". Wanchain is an example of a platform that supports cross-chain transactions using MPC protocols to reduce signing time.

#### Challenges in Cross-Chain Integration

Each blockchain has unique characteristics that pose integration challenges:
-   **Signature Schemes**: Bitcoin uses ECDSA, Solana uses EdDSA, and Ethereum uses ECDSA, which requires the MPC protocol to adapt to different underlying elliptic curves and hash functions.
-   **Transaction Models**: The structure of transactions varies significantly across chains, requiring specialized parsing, construction, and signing logic for each.
-   **RPC Interactions**: Interacting with different chain nodes requires understanding their specific Remote Procedure Call (RPC) interfaces and data formats.
-   **Replay Attacks and Key Reuse**: When supporting multiple chains, care must be taken to prevent replay attacks where a transaction signed for one chain is valid and executed on another. Using domain separators and chain-specific signing contexts, such as EIP-712 for Ethereum, helps prevent such issues.

### Software Engineering and SDK Development

Developing MPC wallet solutions requires strong software engineering principles to encapsulate complex cryptography into usable and secure components.

#### Modular Design and Language Choices

Cryptographic libraries and SDKs must be designed with modularity, maintainability, and testability in mind. Languages like Rust, Go, and C++ are favored for their performance characteristics and memory safety, which are critical for security-sensitive cryptographic operations. For example, the frost-dalek library is written in Rust, indicating its suitability for high-performance and secure cryptographic implementations. Robust code abstraction ensures that the underlying cryptographic complexities are hidden from application developers, allowing for easier integration and reducing the chance of misuse.

#### API and SDK Development

Encapsulating MPC capabilities into well-documented SDKs and APIs is essential for enabling internal product teams and external partners to integrate wallet functionality seamlessly. These SDKs must provide clear interfaces for distributed key generation, transaction signing, and key recovery, while abstracting away the multi-round communication protocols and cryptographic details. Examples include Lit Protocol, which offers programmable MPC for DApp developers, and Coinbase Smart Wallet SDK, which supports integration across multiple networks.

#### Maintenance and Versioning

Managing dependencies, versioning, and cryptographic policy updates is a continuous challenge in production SDKs. Regular audits, vulnerability disclosures, and a clear update roadmap are vital to ensure long-term security and compatibility. The cryptographic community constantly evolves, and SDKs must be agile enough to incorporate new protocols (e.g., from GG18 to GG20 to CGGMP21) and patch security vulnerabilities promptly.

### Emerging Trends and Future Directions

The digital asset landscape is rapidly evolving, with new wallet architectures and regulatory considerations continuously shaping the future of MPC and related technologies.

#### Account Abstraction (AA) and Smart Contract Wallets

Account Abstraction (AA), particularly through ERC-4337, is revolutionizing user interaction with blockchain networks by introducing smart contract wallets that can bypass the need for an Externally Owned Account (EOA) to initiate transactions. This enables advanced features like two-factor authentication, flexible recovery, transaction batching, and gas sponsorship. EIP-7702 and EIP-7212 are further enhancing AA capabilities. EIP-7702 allows EOAs to temporarily convert into smart contract wallets for features like batching and gas sponsorship, and offers privilege de-escalation by enabling users to sign sub-keys with specific permissions. EIP-7212 introduces support for the "secp256r1" elliptic curve standard, enabling Web2 authentication methods like Apple's Secure Enclave, WebAuthn, Android Keystore, and Passkeys for secure, seed-phrase-less wallet access. Coinbase Smart Wallet, for instance, utilizes passkeys for user authentication and sponsored gas transactions.

#### Hybrid Wallet Architectures

As the limitations of both MPC and multisig wallets become apparent, hybrid architectures are emerging to combine the best of both worlds. These approaches, such as keystore-based wallets, use cryptographic proofs to maintain privacy while enabling complex access policies that are not exposed on-chain. This allows for advanced features like spending limits, time-based restrictions, or role-based access controls, verified cryptographically, without the higher gas fees or on-chain transparency of traditional multisig solutions. Companies like Stackup are pioneering such hybrid approaches, which are often recommended over pure MPC or multisig for teams seeking more flexibility and privacy.

#### Regulatory Landscape and Control

The regulatory treatment of MPC wallets has seen significant developments. In the United States, the SEC recognizes qualified custodian status for some MPC providers, though FinCEN mandates KYC/AML procedures. The EU's MiCA framework explicitly addresses MPC custody, requiring client asset segregation and proportional capital requirements or insurance. Singapore and Hong Kong have also integrated MPC into their regulatory frameworks. The ongoing regulatory discourse is shifting from broad decentralization to nuanced discussions of "control," impacting how crypto services are classified and regulated. This shift highlights the need for solutions like Trusted Execution Environments (TEEs) that can ensure operational control resides within hardware and software, rather than with service providers, thereby enhancing data privacy and operational security.

#### Trusted Execution Environments (TEEs)

Trusted Execution Environments (TEEs) are secure enclaves within microprocessors where sensitive computations can run with integrity and privacy, supporting isolation and remote attestation. For Web3 wallets, mobile TEEs like Apple's Secure Enclave and Google's Titan M2 can secure smart contract wallet private keys by creating and storing keys on the device, accessible only via biometric authentication or PIN. Fireblocks, for example, utilizes Intel SGX TEEs to isolate cryptographic data and MPC algorithms, preventing unauthorized access by malicious actors. TEEs are poised to be a game-changer for blockchains, enabling secure and private MEV ecosystems (e.g., Flashbots SUAVE) and improving user onboarding for smart contract wallets with Account Abstraction.

### Market Overview and Deployment Considerations

The MPC Wallet market is experiencing robust growth, driven by an increasing reliance on digital currencies, rising cyber threats, and evolving regulatory landscapes.

#### Market Growth and Applications

The global MPC Wallet market size reached USD 1.8 billion in 2024 and is projected to surpass USD 12.6 billion by 2033, with a compound annual growth rate (CAGR) of 22.4% from 2025 to 2033. This growth is fueled by surging demand for secure digital asset management across various industries. Key application segments include cryptocurrency exchanges, individual users, enterprises, and financial institutions. Cryptocurrency exchanges represent the largest segment due to their need for robust security to protect user funds from cyberattacks and insider threats. Enterprises and financial institutions are adopting MPC wallets to secure large-scale digital asset operations and comply with stringent regulatory requirements, leveraging features like customizable access controls and audit trails.

#### Deployment Modes and Provider Landscape

Organizations can choose between on-premises and cloud deployment options for MPC wallets. On-premises deployment is preferred by large enterprises and regulated entities for greater control and customization, while cloud deployment offers scalability and cost-effectiveness for small-to-medium enterprises and startups. Hybrid models are also emerging to balance flexibility and security.

Major players in the MPC wallet market include Fireblocks, ZenGo, Coinbase (through its acquisition of Unbound Security), Sepior, Curv (acquired by PayPal), GK8, and Safeheron. These companies offer diverse solutions, from institutional-grade infrastructure (Fireblocks, Copper) to retail-focused, seed-phrase-less experiences (ZenGo, Coinbase Wallet).

#### Cost and Implementation Considerations

The total cost of ownership for MPC wallets extends beyond subscription fees, including setup fees (zero for consumer, up to $50,000 for enterprise), monthly/annual fees (free to over $200,000), and transaction fees ($0.001 to $0.50 per operation). Hidden costs like integration development (40-200 engineering hours), compliance audits ($10,000-$50,000), and training can significantly add to the overall expense. Consumer MPC wallet setup is quick (5-10 minutes), but enterprise deployments are multi-month projects requiring careful planning, API integration, key ceremony planning, thorough testing, and gradual rollout over 2-4 months.

#### Migration Strategies

Migrating to an MPC wallet from existing solutions (hardware wallets, EOAs, or multisig wallets) requires careful orchestration. When migrating from hardware wallets, new MPC wallets should be generated, and funds transferred in batches, rather than attempting to import seeds, which would compromise MPC's security model. For EOAs or MetaMask, creating the MPC wallet with the same derivation path can maintain address consistency, and DApp connections must be methodically updated. Multisig migration is the most complex, requiring full approval from all signers and careful documentation of new approval workflows.

### Conclusion

MPC wallets represent a sophisticated evolution in digital asset security, offering robust key management, enhanced fault tolerance, and flexible access control by distributing private key shares across multiple parties. While they address critical vulnerabilities of traditional wallets, they introduce their own set of challenges related to performance, network dependency, and implementation complexity. The ongoing advancements in threshold signature schemes (GG18, GG20, CGGMP21, FROST) and the emergence of hybrid architectures combining MPC with Account Abstraction and TEEs are continually refining the landscape. For institutions and individuals alike, the choice of wallet technology must be a strategic one, carefully balancing security, usability, performance, and regulatory compliance to meet specific operational requirements in the dynamic Web3 ecosystem.

Sources: 
[1] Security, privacy, and decentralized trust management in VANETs: A review of current research and future directions, https://dl.acm.org/doi/abs/10.1145/3656166
[2] Hierarchical Deterministic Bitcoin Wallets that Tolerate Key Leakage, https://link.springer.com/chapter/10.1007/978-3-662-47854-7_31
[3] Arcula: A Secure Hierarchical Deterministic Wallet for Multi-asset Blockchains, https://arxiv.org/abs/1906.05919
[4] A Survey of Threshold Signatures: NIST Standards, Post-Quantum ..., https://dl.acm.org/doi/10.1145/3772274
[5] Provably Unforgeable Threshold EdDSA with an Offline Participant ..., https://link.springer.com/article/10.1007/s00009-023-02452-9
[6] Cross-Chain Overview: Development, Mechanisms, Protocols, Security, and Challenges, https://link.springer.com/chapter/10.1007/978-981-96-1414-1_3
[7] MPC Wallets: A Complete Technical Guide (2025) - Stackup, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide
[8] Wallet security, https://link.springer.com/chapter/10.1007/978-3-031-39288-7_3
[9] MPC Wallet Market Research Report 2033 - Dataintelo, https://dataintelo.com/report/mpc-wallet-market
[10] State of Wallets 2024 | Flashbots Writings, https://writings.flashbots.net/state-of-wallets-2024
[11] Practical escrow protocol for cryptocurrencies, https://theses.lib.polyu.edu.hk/handle/200/11690
[12] SoK: challenges of post-quantum digital signing in real-world applications, https://scholar.archive.org/work/bzhddid6gzepjejxrd2efbszxa/access/wayback/https://eprint.iacr.org/2019/1374.pdf
[13] Smartwallets, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4587335
[14] Fast 2-out-of-n ecdsa threshold signature, https://ieeexplore.ieee.org/abstract/document/10491665/
[15] Efficient Threshold-Optimal ECDSA, https://www.semanticscholar.org/paper/027fde41c5d8501be4461b0a985993989eb00564
[16] CREDENTIAL: Secure Cloud Identity Wallet, https://www.semanticscholar.org/paper/1b8803f537eed12d3a0ab4896399a0cff94b5428
[17] Multisig, Shamir's secret sharing, & MPC compared - Unchained, https://www.unchained.com/blog/mpc-vs-multisig-vs-sss
[18] Decoding Cross-Chain Interoperability, https://www.semanticscholar.org/paper/783b962b85eba95e5222ded0da79d16e14aae5b7
[19] Cross-Chain Collaboration Typology, https://www.semanticscholar.org/paper/492c1cbcdd65d22f72739dd2b3be3f38f403ef10
[20] Thresh-Hold: Assessment of Threshold Cryptography in Leader-Based Consensus, https://ieeexplore.ieee.org/abstract/document/10639786/
[21] Navigating the Blockchain Trilemma: A Review of Recent Advances and Emerging Solutions in Decentralization, Security, and Scalability Optimization., https://cdn.techscience.press/files/cmc/2025/TSP_CMC-84-2/TSP_CMC_66366/TSP_CMC_66366.pdf
[22] Challenges in making blockchain privacy compliant for the digital world: some measures, https://www.academia.edu/download/91069224/s12046-022-01931-1.pdf
[23] A Cross-Chain Protocol based on Quantum Teleportation for Underlying Architecture of Metaverse, https://ieeexplore.ieee.org/document/9845967/
[24] Towards Atomicity and Composability in Cross-Chain NFTs, https://www.semanticscholar.org/paper/0f76ecfaf09f82e9a7175aa9d2f394ac4924cc51
[25] Comparative Analysis of Security Features and Risks in Digital Asset ..., https://www.researchgate.net/publication/392742564_Comparative_Analysis_of_Security_Features_and_Risks_in_Digital_Asset_Wallets
[26] [PDF] A Survey of ECDSA Threshold Signing - Cryptology ePrint Archive, https://eprint.iacr.org/2020/1390.pdf
[27] A Comprehensive Survey of Threshold Digital Signatures: NIST ..., https://www.semanticscholar.org/paper/3485e879caa4f5c4349312d339eac9cf594fe926
[28] A Comprehensive Survey of Threshold Signatures: NIST Standards ..., https://www.researchgate.net/publication/379182214_A_Comprehensive_Survey_of_Threshold_Signatures_NIST_Standards_Post-Quantum_Cryptography_Exotic_Techniques_and_Real-World_Applications
[29] MPC Wallet Architecture Using ECDSA — Complete Guide - Medium, https://medium.com/@garima.miet/mpc-wallet-architecture-using-ecdsa-complete-guide-66584b8a2a65
[30] [PDF] An Extended Hierarchy of Security Notions for Threshold Signature ..., https://eprint.iacr.org/2024/1920.pdf
[31] A Comprehensive Survey of Threshold Digital Signatures - arXiv, https://arxiv.org/html/2311.05514v2
[32] Defi integrated blockchain wallet with automated transactions, https://www.semanticscholar.org/paper/40ece73be00bb0e03506b8176a0d17fbd1a84a5c
[33] Usability and Security Analysis of the KeepKey Wallet, https://ieeexplore.ieee.org/document/8751451/
[34] Threshold Proxy Signature Schemes, https://link.springer.com/chapter/10.1007/BFb0030429
[35] Cryptanalysis of threshold group signature schemes with privilege subsets, https://www.semanticscholar.org/paper/a0e4a9a92d543655de46393c51a306019d72224b
[36] What are Chain Signatures? | NEAR Documentation, https://docs.near.org/chain-abstraction/chain-signatures
[37] What is a Multi-Party Computation (MPC) wallet? - Coinbase, https://www.coinbase.com/learn/wallet/what-is-a-multi-party-computation-mpc-wallet
[38] Mithril: Stake-based Threshold Multisignatures, https://www.semanticscholar.org/paper/56a3d8cbf0f9f4cc61432a4bbb008e04a0461b1d
[39] BUFFing Threshold Signature Schemes, https://www.semanticscholar.org/paper/84fe26781f5d8cea0885ef0cf3368058d728b770
[40] GetMobile, https://dl.acm.org/doi/pdf/10.1145/3665112
[41] A novel Layer 2 framework for breaking the blockchain trilemma problem using MPC-in-the-Head, https://linkinghub.elsevier.com/retrieve/pii/S1389128625001161
[42] Survey on Security Mechanisms for Mobile Wallet, https://www.semanticscholar.org/paper/a891162416296f26098007a32ecc72d882b2f335
[43] A new (t, n) threshold signature scheme withstanding the conspiracy attack, https://link.springer.com/article/10.1007/BF02828628
[44] Cryptanalysis of Threshold Proxy Signature Schemes 1 ), https://www.semanticscholar.org/paper/b7b88f22c04b19f271dca4ec124c00e5777c9929
[45] Nominees for 2023–2024 SEG Board of Directors, https://library.seg.org/doi/10.1190/tle42050367.1
[46] MPC or Multisig Wallets Which Offers Better Security - Safeheron, https://safeheron.com/blog/mpc-vs-multisig-wallets-security-differences-similarities/
[47] MPC Wallet Security in 2025: Solving the Blind Signing Gap, https://www.hypernative.io/blog/mpc-wallet-security-in-2025-solving-the-blind-signing-gap
