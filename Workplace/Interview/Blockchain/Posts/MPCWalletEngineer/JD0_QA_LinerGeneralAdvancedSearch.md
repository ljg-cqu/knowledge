### The Evolving Landscape of Multi-Party Computation (MPC) in Blockchain Wallet Security and Multi-Chain Integration

Multi-Party Computation (MPC) is transforming the landscape of digital asset security, particularly within blockchain wallets and multi-chain environments. By enabling several parties to jointly compute a function over their private inputs without revealing those inputs to one another, MPC inherently addresses the single-point-of-failure inherent in traditional private key management. This cryptographic primitive is fundamental to constructing robust *threshold signature schemes* (TSS), where a secret key is distributed among multiple participants, and a predefined threshold of these participants must collaborate to produce a valid signature. Such schemes are vital for enhancing the security and resilience of digital asset custody solutions, where the compromise or loss of a single private key could lead to catastrophic financial losses. The evolution of threshold ECDSA protocols, including seminal works like GG18, GG20, CMP, CGGMP, and CCLST, highlights the continuous advancements in this field, pushing towards more efficient, secure, and provably robust solutions for a decentralized future.

### Deep Dive into Threshold ECDSA Protocols

#### Fundamentals of ECDSA and Thresholdization

The Elliptic Curve Digital Signature Algorithm (ECDSA) is the cornerstone of digital signatures across major blockchain networks, including Bitcoin and Ethereum. ECDSA operates on elliptic curves over finite fields, generating a signature using a secret key and a unique random number known as a *nonce* (k). The security of ECDSA hinges critically on the secrecy and uniqueness of this nonce; its reuse or leakage can directly compromise the entire private key. Even a minimal bias in the nonce generation can enable an attacker to recover the private key.

In a threshold ECDSA scheme, the challenge lies in collaboratively computing the components of the signature, specifically `k` and `kx`, without any single party ever learning the full `k` or `x` (the private key). This necessity arises because revealing `k` to any participant would break the security of the shared private key `x`. Therefore, modular inversion, a critical step in ECDSA signing, must also be performed distributively without exposing individual shares or the complete nonce.

#### Multiplicative-to-Additive (MtA) Share Conversion

A core primitive that addresses the challenge of collaborative nonce generation and key sharing in threshold ECDSA protocols is the *Multiplicative-to-Additive (MtA) share conversion protocol*. This protocol securely transforms multiplicative shares into additive shares without revealing the underlying secrets. The security of MtA protocols relies heavily on the use of homomorphic encryption schemes, most commonly Paillier encryption or class group-based encryption.

In a typical MtA process involving Paillier encryption, party *P_i* encrypts its share `k_i` using its Paillier public key `Enc_i(k_i)` and sends it to party *P_j*. Due to the homomorphic properties of Paillier encryption, *P_j* can compute `Enc_i(k_i * γ_j + β_ij)` using *P_i*'s public key, where `γ_j` is *P_j*'s mask and `β_ij` is a randomly chosen element. *P_j* then sends this encrypted value back to *P_i*, who decrypts it to obtain `k_i * γ_j + β_ij mod q`. This iterative process allows parties to derive additive shares (`α_ij` and `β_ij`) of the product `k_i * γ_j` without revealing individual `k_i` or `γ_j` values. Ultimately, these additive shares enable the parties to collectively compute the necessary values for the ECDSA signature, such as `kγ` and `kx`, without reconstructing the full secrets.

#### Protocol Implementations: GG18, GG20, CMP, CGGMP, CCLST

The development of threshold ECDSA has seen several iterations, each building upon previous advancements to enhance efficiency, security, and functionality.

- **GG18 (Gennaro and Goldfeder 2018)**: This protocol was pioneering as the first to support threshold signatures for any *t* out of *n* participants with an efficient dealerless key generation. However, GG18 had a relatively high communication cost, requiring nine rounds for signing.
- **GG20 (Gennaro and Goldfeder 2020)**: As a successor to GG18, GG20 significantly improved efficiency by introducing non-interactive online signing, reducing the signing process to a single round after an offline pre-computation phase. It also incorporated *identifiable aborts*, a crucial feature allowing the identification of a malicious party causing protocol failure, thereby enhancing accountability.
- **MPC CMP (Canetti, Makriyannis, Peled 2020)**: This protocol is characterized by its rigorous security analysis within the Universally Composable (UC) security framework. MPC CMP provides non-interactive signing capabilities and includes a key refresh mechanism, offering full proactive security against adaptive adversaries.
- **CGGMP (Canetti, Gennaro, Goldfeder, Makriyannis, Peled)**: A joint effort by the authors of GG20 and CMP, CGGMP further enhances the CMP protocol. It integrates improved key refresh mechanisms using DH-style encryption for efficiency and features comprehensive zero-knowledge range proofs for MtA parameters, addressing critical vulnerabilities found in earlier Paillier-based schemes.
- **CCLST (Castagnos, Catalano, Laguillaumie, Savasta, Tucker)**: This scheme introduces class group-based encryption as an alternative to Paillier. By using class groups of unknown order, CCLST protocols can eliminate the need for a trusted third party and reduce the number of zero-knowledge proofs required compared to Paillier-based approaches, leading to significantly lower communication costs. CCLST also offers adaptive security, proactive security with an efficient key refresh mechanism, and identifiable aborts.

| Protocol | Encryption Scheme | Communication Rounds (Signing) | Key Generation | Key Refresh | Security Features | Adversary Model |
|:---------|:------------------|:-------------------------------|:---------------|:------------|:------------------|:----------------|
| **GG18** | Paillier | 9 | Feldman VSS, Shamir SS | No | Dishonest majority, no trusted setup | Static |
| **GG20** | Paillier | 1 online (7 total) | Feldman VSS, Shamir SS | No | Non-interactive online signing, identifiable abort | Static & Rushing |
| **MPC CMP** | Paillier | 1 online (3 presigning) | Schnorr's proof for shares | Yes (periodic) | UC-secure, proactive security, non-interactive | Adaptive (t=n-1) |
| **CGGMP** | Paillier + DH-style for refresh | 1 online (3 presigning) | Schnorr's proof for shares | Yes (enhanced) | UC-secure, identifiable abort, proactive security, ZK range proofs | Adaptive (t=n-1) |
| **CCLST** | Class group-based | 1 online (6 total) | Feldman VSS, Shamir SS | Yes (new key pairs) | Bandwidth-efficient, adaptive/proactive security, identifiable abort | Adaptive (t=n-1) |

### Security Risks, Attacks, and Mitigation Strategies

#### Vulnerabilities in Paillier-based Schemes (GG18, GG20)

Despite their foundational role, early Paillier-based threshold ECDSA protocols like GG18 and GG20 exhibited critical vulnerabilities. A significant class of attacks targets the **Paillier modulus validation**. If the publicly disclosed Paillier modulus `N` does not satisfy specific cryptographic properties, such as being a valid Paillier modulus (e.g., product of exactly two large prime factors) or if it contains small prime factors, the signature private key can be exploited. The "6ix1een attack" and "Death by 1M cuts attack" by Fireblocks demonstrated practical key extraction from GG18 and GG20 implementations that lacked proper validation of the Paillier modulus and specific `beta` parameters in MtA.

Another vulnerability stemmed from the **absence of zero-knowledge range proofs** for parameters used in the MtA protocol. While not always leading to full private key exposure, this allows for certain types of information leakage and must be considered a serious security concern. More recent protocols like CGGMP addressed this by incorporating zero-knowledge range proofs for MtA parameters.

The *TSSHOCK* attacks revealed further critical flaws, notably targeting **ambiguous encoding schemes** in popular open-source TSS implementations. The `alpha-shuffle` attack exploited ambiguous encoding of `alpha` values in `dlnproof` iterations, allowing a malicious party to extract the private key without causing an abort. Additionally, **insecure TSS optimizations** were exploited, such as reducing `dlnproof` iterations (leading to the `c-guess` attack) or using a larger challenge space with a composite group order (leading to the `c-split` attack). These attacks underscore that even audited implementations can be vulnerable to subtle cryptographic weaknesses and optimization pitfalls.

#### General Security Concerns

Threshold signature schemes must account for *malicious adversaries* who may deviate from the protocol and attempt to learn secrets or forge signatures. The distinction between *static adversaries* (who choose which parties to corrupt at the beginning) and *adaptive adversaries* (who can corrupt parties dynamically during the protocol) is crucial for assessing security strength. Furthermore, implementations of MPC-in-the-Head protocols, which underpin many zero-knowledge proof schemes used in threshold cryptography, can be vulnerable to *side-channel attacks*. Even a single leaked value from a ZKBoo protocol implementation, for instance, could be sufficient to compromise its security.

#### Mitigation Approaches

To counter these sophisticated attacks and ensure the robust security of threshold ECDSA systems, several mitigation strategies are employed:

- **Rigorous Validation of Paillier Modulus and Parameters**: This involves providing zero-knowledge range proofs during key generation to verify that the Paillier modulus is correctly generated, is a Blum modulus, can be factored into exactly two large prime factors, and that encrypted values fall within a valid range.
- **Key Refresh Mechanisms for Proactive Security**: Periodic key refreshes allow parties to generate new key shares without changing the public key, thus preventing gradual leakage of information over time and maintaining security against long-term threats. Protocols like CMP, CGGMP, and CCLST incorporate such mechanisms.
- **Identifiable Aborts for Accountability**: This feature ensures that if a protocol fails due to malicious behavior, the culpable party can be identified and held accountable.
- **Using Class Group-based Encryption**: Employing class groups of imaginary quadratic fields offers an alternative to Paillier encryption. This approach can significantly reduce bandwidth consumption and the need for numerous zero-knowledge proofs compared to Paillier-based schemes, although it requires new ZKPs for encryption correctness due to the unknown order of the group.
- **Audited Implementations and Secure Coding Practices**: Relying on thoroughly audited open-source libraries and adhering to secure coding principles are paramount to preventing vulnerabilities from creeping into practical deployments.

### MPC in Multi-Chain and Cross-Chain Integration

#### Role of MPC in Multi-Chain Wallets

Multi-Party Computation plays a pivotal role in enabling the next generation of multi-chain wallets, fostering secure and seamless interaction across diverse blockchain ecosystems. By distributing the control of private keys across multiple parties, MPC facilitates the management of assets on various chains without relying on a single, centralized entity. This capability is especially critical for *cross-chain interoperability*, where secure transfer of assets and data between heterogeneous blockchains is a significant challenge. For privacy-focused blockchains like Zcash, MPC is instrumental in supporting complex operations such as "threshold shielded transactions," which allow multi-signature functionality while preserving the strong privacy guarantees of the underlying chain.

#### Case Study: Zcash Sapling Threshold Shielded Transactions

Zcash's Sapling upgrade brought significant improvements to the efficiency of shielded transactions, making them practical for everyday use. However, Sapling initially lacked native support for multi-signature with privacy. Zengo, in partnership with the Zcash Foundation, developed a proof-of-concept for threshold shielded transactions, demonstrating how MPC can enable such a feature.

The main challenges involved designing a protocol that could work for a general *t*-out-of-*n* threshold, be provably secure without significant changes to Sapling's existing key tree or zk-SNARKs, and operate efficiently. The solution involved modifying the lowest level of the key tree, distributing the `ask` (Sapling's spending key) derivation among untrusted parties, so it is never constructed in a single place. This *multiparty RedJubjub* scheme uses simulation-based security and introduces minimal overhead.

From an engineering perspective, integrating this into Zcash required overcoming hurdles such as re-using Zcash's unique elliptic curve cryptography (Jubjub). The Zcash implementation, `LibRustZcash`, was robust but not designed as a general API for other consumers. Zengo forked and stripped down `LibRustZcash` to create a general-purpose Jubjub library, demonstrating how to adapt existing cryptographic building blocks for MPC. The final integration into the Zcash full node involved careful adjustments to avoid interfering with the zero-knowledge proof generation and adapting to Zcash's C++/Rust hybrid codebase, showcasing a practical approach to embedding interactive MPC protocols into complex blockchain software. This proof-of-concept highlights the potential of MPC to extend privacy and security features to multi-party scenarios within even highly complex and privacy-preserving blockchain environments.

### Engineering and Implementation Considerations for MPC Wallets

#### Programming Languages and Frameworks

Developing MPC-based wallet modules demands robust programming languages suitable for system-level and cryptographic implementations. Rust, Go, and C++ are frequently chosen for their performance, memory safety, and strong type systems. For instance, Dfns has open-sourced an audited Rust implementation of the CGGMP21 protocol, providing a state-of-the-art solution for threshold ECDSA signatures. These languages enable developers to craft highly efficient, secure, and maintainable codebases for critical components like key generation, key sharing, and signature protocols.

#### Software Architecture and SDK Encapsulation

Effective implementation of MPC logic requires a well-structured software architecture. Encapsulating complex cryptographic protocols into reusable SDKs or APIs is essential for empowering internal products and external partners to integrate MPC capabilities seamlessly. Such SDKs must abstract away the intricate details of MPC protocols while providing secure and user-friendly interfaces. The `cggmp21` library, for example, is agnostic to the network layer, requiring only a stream of incoming and a sink for outgoing messages, which allows flexible integration into various communication infrastructures. Critical security considerations for such SDKs include ensuring all messages are authenticated to confirm the sender's identity and encrypted to guarantee confidentiality to the designated recipient. Furthermore, all parties must agree on unique execution IDs to prevent message replay attacks and ensure proper context separation between protocol executions.

#### Building Secure Wallet Infrastructure with MPC

Beyond core cryptographic protocols, MPC integrates with broader wallet infrastructure to build comprehensive security and functionality features.

- **Risk Control, Device Attestation, and Multi-Factor Authentication (MFA)**: MPC facilitates the creation of sophisticated security policies by enabling distributed control over cryptographic operations. This can be combined with device attestation to verify the integrity of signing devices and with MFA to add multiple layers of user authentication, ensuring that only authorized users can initiate transactions even if one factor is compromised. These strategies are crucial for preventing unauthorized access and mitigating fraud.
- **Account Abstraction (AA) and Session Keys**: MPC can underpin advanced wallet features like Account Abstraction and Session Keys. AA allows for programmable wallet logic, where transaction rules and authorization mechanisms are defined by smart contracts, rather than being hardcoded into the protocol. Session keys provide temporary, limited-scope keys for specific applications or durations, improving usability without compromising the main key's security. In an MPC context, these can be managed distributively.
- **Social Recovery**: MPC-based solutions can also enhance social recovery mechanisms, where designated trusted parties or devices can help recover access to a wallet if a user loses their shares. By distributing recovery shares and requiring a threshold of them, MPC adds a layer of security and resilience compared to traditional centralized recovery methods.
- **Compatibility with Public Chain Ecosystems**: Integrating MPC wallets into the broader blockchain ecosystem requires deep familiarity with the transaction structures and signature standards of major public chains like Ethereum, EVM L2s, Bitcoin, and Solana. The MPC backend must generate signatures that are compatible with the specific cryptographic requirements of each chain, ensuring seamless interaction and broad usability across the multi-chain landscape.

The continuous evolution of MPC protocols, coupled with rigorous engineering practices and comprehensive security strategies, positions MPC as a foundational technology for building highly secure, flexible, and user-friendly blockchain wallets capable of navigating the complexities of a multi-chain future.

Sources: 
[1] Fast Multiparty Threshold ECDSA with Fast Trustless Setup, https://dl.acm.org/doi/10.1145/3243734.3243859
[2] Limbo: Efficient zero-knowledge MPCitH-based arguments, https://dl.acm.org/doi/abs/10.1145/3460120.3484595
[3] Template Attacks on ECDSA, https://link.springer.com/chapter/10.1007/978-3-642-00306-6_2
[4] Cash: Transparent Anonymous Transactions, https://eprint.iacr.org/2022/1104
[5] Zero-knowledge protocols for the subset sum problem from MPC-in-the-head with rejection, https://link.springer.com/chapter/10.1007/978-3-031-22966-4_13
[6] The MPC-in-the-head paradigm and its applications, https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/3094278
[7] A Gentle Introduction to the MPC-in-the-Head Transformation, https://blog.zksecurity.xyz/posts/mpcith-intro/
[8] A Survey of Threshold Signatures: NIST Standards, Post-Quantum ..., https://dl.acm.org/doi/10.1145/3772274
[9] A Comparative Examination of Some Threshold ECDSA Protocols ..., https://blokzincir.bilgem.tubitak.gov.tr/en/a-comparative-examination-of-some-threshold-ecdsa-protocols-used-in-custody/
[10] A Comparative Examination of Some Threshold ECDSA Protocols in ..., https://medium.com/@oznurmut/a-comparative-examination-of-some-threshold-ecdsa-protocols-e7af8cad1992
[11] Zcash Threshold Shielded Transactions: a Proof of Concept | Zengo, https://zengo.com/zcash-threshold-shielded-transactions-a-proof-of-concept/
[12] What's out there for ECDSA threshold signatures - cryptologie.net, https://www.cryptologie.net/posts/whats-out-there-for-ecdsa-threshold-signatures/
[13] CGGMP21 In Rust, At Last - Dfns, https://www.dfns.co/article/cggmp21-in-rust-at-last
[14] TSSHOCK: New Key Extraction Attacks on Threshold Signature ..., https://verichains.io/tsshock/
[15] On the Proof of Ownership of Secret Keys, https://kanazawa-u.repo.nii.ac.jp/record/2003056/files/Full-N-2124042003-WANG-CHEN.pdf
[16] Smartwallets, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4587335
[17] Completely FROST-ed: IoT issued FROST signature for Hyperledger Fabric blockchain, https://ieeexplore.ieee.org/abstract/document/10634347/
[18] Beyond basic trust: Envisioning the future of nextgen networked systems and digital signatures, https://ieeexplore.ieee.org/abstract/document/10431561/
[19] Fast 2-out-of-n ecdsa threshold signature, https://ieeexplore.ieee.org/abstract/document/10491665/
[20] Threshold Linear Secret Sharing to the Rescue of MPC-in-the-Head, https://www.semanticscholar.org/paper/07997538b7110ded8dfddfb7a2496643ac57d660
[21] Practical Threshold Signatures Without Random Oracles, https://link.springer.com/chapter/10.1007/978-3-540-75670-5_14
[22] Threshold Signature, https://link.springer.com/rwe/10.1007/978-1-4419-5906-5_233
[23] Perfect MPC over Layered Graphs, https://www.semanticscholar.org/paper/9c3a6d61a80ad01cc5003b3b6f68201fae2b673e
[24] CORR 2000-54 The Exact Security of ECDSA, https://www.semanticscholar.org/paper/ad5a8bbfe0ba8a208c91c12d39dab8dc23891daa
[25] Gotzilla: efficient disjunctive zero-knowledge proofs from MPC in the head, with application to proofs of assets in cryptocurrencies, https://petsymposium.org/popets/2022/popets-2022-0107.php
[26] Practical Key-Extraction Attacks in Leading MPC Wallets, https://dl.acm.org/doi/10.1145/3658644.3670359
[27] A survey on cross-chain technology: Challenges, development, and prospect, https://ieeexplore.ieee.org/abstract/document/9982450/
[28] Short(t,n) Threshold Signature, https://www.semanticscholar.org/paper/e184e1827b6ce18c43d5dbac9953f375c94efbbf
[29] Threshold Schnorr with Stateless Deterministic Signing from Standard Assumptions, https://link.springer.com/chapter/10.1007/978-3-030-84242-0_6
[30] Cross-blockchain smart contract interoperability, https://www.semanticscholar.org/paper/9508258301db2fa29b8a2838ebe2aa71f26139e4
[31] An Analysis of Anonymity in the Zcash Cryptocurrency, https://www.semanticscholar.org/paper/b1f601c24e2be52d5c8d1e243846ae7234d82e46
[32] An improved Threshold Signature scheme, https://www.semanticscholar.org/paper/2e4dda07eb0469a1642fc8a9e4d2645a46e28a9b
[33] Template Attacks on ECDSA Hardware and Theoretical Estimation of the Success Rate, https://www.semanticscholar.org/paper/13cf1e2373a4e50fff1d2cf139fddb5bdbaff965
[34] A UNIVERSAL USERTOKENANU PERSONALCRYPTO-ENGINE, https://www.semanticscholar.org/paper/b00d617c8654c7502ec2b5d96617bdf473291398
[35] Exploring the use of Zcash cryptocurrency for illicit or criminal purposes, https://www.rand.org/content/dam/rand/pubs/research_reports/RR4400/RR4418/RAND_RR4418.pdf
[36] [PDF] New Key Extraction Attacks on Threshold ECDSA Implementations, https://i.blackhat.com/BH-US-23/Presentations/US-23-Nguyen-TSSHOCK-Breaking-MPC-Wallets-wp.pdf
[37] A Multi-blockchain Architecture Supporting Cross-Blockchain Communication, https://link.springer.com/chapter/10.1007/978-981-15-8086-4_56
[38] [PDF] A Hitchhiker's Guide to Cryptography Code Audit, https://csrc.nist.gov/csrc/media/presentations/2024/crclub-2024-01-24/images-media/20240124-crypto-club--tommaso-marco-sylvain--slides--crypto-audit.pdf
[39] How MPC Wallets Work: A Complete Guide for All Levels, https://cordialsystems.com/post/how-mpc-wallets-work-a-complete-guide-for-all-levels
[40] GG18 and GG20 Paillier Key Vulnerability [CVE-2023-33241], https://fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report/
[41] SNI-in-the-head: Protecting MPC-in-the-head Protocols against Side-channel Analysis, https://dl.acm.org/doi/10.1145/3372297.3417889
[42] Quantum-Safe Public Key Blinding from MPC-in-the-Head Signature Schemes, https://www.semanticscholar.org/paper/5758ca2a5df36205ab31afe597671421afaadf5a
[43] Formal security analysis of MPC-in-the-head zero-knowledge protocols, https://ieeexplore.ieee.org/document/9505225/
[44] Fully Secure PSI via MPC-in-the-Head, https://petsymposium.org/popets/2022/popets-2022-0073.php
[45] A Survey on Threshold Signature Schemes, https://www.semanticscholar.org/paper/edd1462577215c63865321a75d11091990edb6e0
[46] [PDF] MPC-in-the-Head Framework without Repetition and its Applications ..., https://eprint.iacr.org/2024/1591.pdf
[47] A Comprehensive Survey of Threshold Digital Signatures - arXiv, https://arxiv.org/html/2311.05514v2
[48] [PDF] A Note on the Security of GG18 - Fireblocks, https://info.fireblocks.com/hubfs/A_Note_on_the_Security_of_GG.pdf
[49] Threshold ECDSA - HackMD, https://hackmd.io/@YaoGalteland/HJc8JYMfkx
[50] [PDF] Key Extraction Attacks on Threshold ECDSA Implementations, https://eprint.iacr.org/2021/1621.pdf
[51] [PDF] Zero-Knowledge Systems from MPC-in-the-Head and Oblivious ..., https://eprint.iacr.org/2023/1470.pdf
[52] Formal security analysis of MPC-in-the-head zero-knowledge ..., https://ieeexplore.ieee.org/document/9505225
[53] [PDF] Introduction to MPC-in-the-Head, https://csrc.nist.gov/csrc/media/Projects/post-quantum-cryptography/documents/pqc-seminars/presentations/13-intro-mpc-in-the-head-05212024.pdf
[54] [2506.22961] MPC in the Quantum Head (or: Superposition-Secure ..., https://arxiv.org/abs/2506.22961
[55] Verifiable computation over encrypted data via MPC-in-the-head ..., https://link.springer.com/article/10.1007/s10207-024-00941-w
[56] Bridging Sapling: Private Cross-Chain Transfers, https://arxiv.org/abs/2204.10611
[57] Análisis de Zcash, https://www.semanticscholar.org/paper/f836fc2a11acbac7d6e2c2104a12bf86b995529e
[58] Bitcoin Private Key Locked Transactions, https://linkinghub.elsevier.com/retrieve/pii/S0020019018301698
[59] One-Out-of-Many Proofs: Or How to Leak a Secret and Spend a Coin, https://link.springer.com/chapter/10.1007/978-3-662-46803-6_9
[60] Detecting ASIC Miners in Zcash, https://www.semanticscholar.org/paper/5f4cf671baf40bbaa266d728d0c450ac4869614c
[61] Alpha-Rays: Key Extraction Attacks on Threshold ECDSA Implementations, https://www.semanticscholar.org/paper/1f3c5c727865c1cb1fb8b25578295125b6a74e2a
[62] Notes on Threshold EdDSA/Schnorr Signatures, https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8214B.ipd.pdf
[63] One Round Threshold ECDSA Without Roll Call, https://link.springer.com/chapter/10.1007/978-3-031-30872-7_15
[64] Asynchronous Threshold ECDSA With Batch Processing, https://ieeexplore.ieee.org/document/10012543/
[65] A Tale of Three Signatures: Practical Attack of ECDSA with wNAF, https://link.springer.com/chapter/10.1007/978-3-030-51938-4_18
[66] Low-Bandwidth Threshold ECDSA via Pseudorandom Correlation Generators, https://ieeexplore.ieee.org/document/9833559/
