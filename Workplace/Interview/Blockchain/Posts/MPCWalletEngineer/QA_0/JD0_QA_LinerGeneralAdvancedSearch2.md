## Contents

-(#topic-areas-questions-1-n)
  -(#topic-1-mpc-based-wallet-core-modules)
    -(#q1-how-do-mpc-protocols-enhance-the-security-of-cryptocurrency-wallets-compared-to-traditional-multi-signature-schemes)
    -(#q2-discuss-the-challenges-and-best-practices-for-implementing-key-generation-and-key-sharding-in-production-grade-mpc-wallets)
    -(#q3-evaluate-the-trade-offs-between-different-threshold-signature-schemes-e.g.-gg18-frost-in-terms-of-performance-security-and-real-world-deployment-complexity-for-blockchain-applications)
    -(#q4-describe-how-session-key-management-and-account-abstraction-aa-in-blockchain-wallets-improve-user-experience-and-security)
    -(#q5-how-can-social-recovery-mechanisms-be-securely-implemented-in-blockchain-wallets-and-what-are-the-key-considerations-for-their-widespread-adoption)
  -(#topic-2-transaction-signing--blockchain-interoperability)
    -(#q6-explain-the-structure-of-an-ethereum-eip-1559-transaction-and-how-it-differs-from-legacy-transactions-particularly-concerning-gas-fee-mechanisms)
    -(#q7-what-are-the-security-and-performance-implications-of-using-different-elliptic-curve-cryptography-schemes-e.g.-ecdsa-ed25519-in-blockchain-signature-standards)
    -(#q8-discuss-best-practices-for-integrating-cryptographic-libraries-e.g.-libsodium-rust-crypto-crates-into-blockchain-wallet-systems-to-ensure-both-security-and-performance)
    -(#q9-how-are-merkle-trees-and-hash-based-commitment-schemes-utilized-in-blockchain-wallets-and-cryptographic-protocols-and-what-security-benefits-do-they-provide)
  -(#topic-3-security--risk-management-in-blockchain-wallets)
    -(#q10-analyze-the-attack-surface-of-crypto-wallet-systems-particularly-focusing-on-the-differences-between-hot-warm-and-cold-wallets-and-propose-mitigation-strategies)
    -(#q11-how-do-hardware-security-modules-hsm-and-key-management-services-kms-contribute-to-the-security-of-blockchain-asset-custody-and-what-are-their-limitations-in-a-multi-cloud-environment)
    -(#q12-discuss-multi-factor-authentication-mfa-and-device-validation-strategies-in-blockchain-wallet-systems-including-modern-approaches-like-fido2/webauthn-and-totp)
  -(#topic-4-advanced-cryptographic-concepts--applications)
    -(#q13-explain-the-concept-of-zero-knowledge-proofs-zkps-and-their-practical-applications-in-enhancing-privacy-and-scalability-within-blockchain-wallets-and-security-systems)
    -(#q14-describe-how-approval-and-limit-flows-can-be-implemented-in-blockchain-wallets-to-enhance-security-and-user-control-over-digital-assets-especially-in-defi-contexts)
    -(#q15-what-are-the-performance-optimization-strategies-for-cryptographic-operations-in-mobile-web-and-backend-environments-within-blockchain-applications)
-(#reference-sections)
  -(#glossary-terminology--acronyms)
  -(#codebase--library-references)
  -(#authoritative-literature--reports)
  -(#apa-style-source-citations)

---

## Topic Areas (Questions 1\u2013N)

### Topic 1: MPC-based Wallet Core Modules

#### Q1: How do MPC protocols enhance the security of cryptocurrency wallets compared to traditional multi-signature schemes?

**Difficulty:** Advanced | **Type:** Theoretical

**Answer:** Multi-Party Computation (MPC) protocols significantly enhance cryptocurrency wallet security by eliminating single points of failure without ever fully reconstructing a private key in one location. Unlike traditional multi-signature (multi-sig) schemes, which require multiple distinct private keys that are each fully formed and stored, MPC wallets fragment a single private key into multiple shares. These shares are distributed among several parties, and a threshold number of these parties must cooperate to sign a transaction, yet no single party ever holds the complete private key. This approach makes MPC wallets resilient against attacks where an adversary might compromise one or even several key shares, as a full key is never assembled. Moreover, MPC protocols can support advanced features like distributed key generation (DKG), where key shares are created individually without any single entity ever knowing the full key. MPC also outputs standard signatures, ensuring compatibility with various blockchain networks like Ethereum, Bitcoin, and Solana. The distributed nature of MPC also simplifies key recovery for consumers and provides fault-tolerant, chain-agnostic signing infrastructure for institutions. This contrasts with multi-sig, where the exposure of any one full key is a critical vulnerability.

**Key Insight:** Trade-offs - *MPC eliminates the single point of failure inherent in traditional multi-signature by never fully reconstructing the private key, instead distributing cryptographic shares.*

---

#### Q2: Discuss the challenges and best practices for implementing key generation and key sharding in production-grade MPC wallets.

**Difficulty:** Advanced | **Type:** Practical

**Answer:** Implementing key generation and key sharding in production-grade MPC wallets involves intricate challenges and requires adherence to best practices to ensure security and reliability. A primary challenge is guaranteeing the "dealerless" or Distributed Key Generation (DKG) process, where no single party computes or knows the full private key at any point. This necessitates robust cryptographic protocols that allow multiple participants to jointly compute a public key and individual secret shares without interaction revealing their inputs. Best practices include using proven DKG schemes that are secure against malicious adversaries and can identify misbehaving parties. For key sharding, a secure threshold scheme ensures that a predefined number of participants (t-of-n) must cooperate to reconstruct the key or sign transactions, but individual shares do not reveal the original key. The secure storage of these key shares is critical, often leveraging secure enclaves like AWS Nitro Enclaves, or Hardware Security Modules (HSMs) to protect against compromise. Regular key refresh mechanisms are also essential to mitigate risks associated with long-term exposure of static shares. Another challenge is maintaining high availability and disaster recovery for key shares across multiple deployments, which can involve multi-cloud strategies.

**Key Insight:** Failure Path - *Improper DKG or key share storage can lead to private key exposure, undermining the core security promise of MPC wallets.*

---

#### Q3: Evaluate the trade-offs between different threshold signature schemes (e.g., GG18, FROST) in terms of performance, security, and real-world deployment complexity for blockchain applications.

**Difficulty:** Advanced | **Type:** Comparison

**Answer:** Threshold signature schemes like GG18, GG20, and FROST offer distinct trade-offs in performance, security, and deployment complexity, making their suitability dependent on the specific blockchain application. GG18, for instance, was an early t-of-n threshold ECDSA protocol with efficient dealerless key generation and improved communication complexity compared to prior solutions. However, some GG18 implementations have been found vulnerable to key extraction attacks, despite undergoing security audits. GG20, an improvement over GG18, reduces the number of required rounds for signing and introduces mechanisms to deal with misbehaving parties, enhancing robustness. It integrates Homomorphic Secret Sharing, Zero-Knowledge Proofs, and Multi-Party Computation (MPC) to secure transactions without revealing sensitive information. FROST (Flexible Round-Optimized Schnorr Threshold) is designed for Schnorr signatures and is notable for its efficiency, security, and privacy-preserving properties, especially in its two-round Schnorr signature protocol. A key feature of FROST is Distributed Key Generation (DKG), which creates key shares individually without the full key ever existing in one place. While FROST is proven to have full adaptive security and supports rerandomized signatures for anonymity in specific blockchain contexts like Zcash, the DKG aspect is often considered out of scope in its IETF specification, leaving secure agreement to the library user. The optimal choice depends on factors such as the specific signature algorithm required (ECDSA vs. Schnorr), tolerance for communication rounds, and the level of robustness needed against malicious participants.

**Key Insight:** Trade-offs - *The choice among GG18, GG20, and FROST involves balancing improved communication complexity and robustness (GG20), with the strong adaptive security and DKG features of FROST for Schnorr signatures, against the known vulnerabilities of early GG18 implementations.*

---

#### Q4: Describe how session key management and account abstraction (AA) in blockchain wallets improve user experience and security.

**Difficulty:** Intermediate | **Type:** Theoretical

**Answer:** Session key management and Account Abstraction (AA) in blockchain wallets significantly enhance both user experience and security by providing more flexible and intuitive ways to interact with decentralized applications (dApps). Session keys are temporary, short-lived keys that allow users to pre-approve specific transactions or sets of actions with custom parameters like frequency, gas limits, or daily spending limits. This eliminates the need for repeated, full wallet signatures for every minor interaction, greatly streamlining user flows and reducing friction, making dApps feel more responsive and akin to Web2 experiences. From a security perspective, session keys can be scoped to specific dApps or transaction types, limiting the potential damage if a session key is compromised, as it cannot be used to drain an entire wallet. Account Abstraction, particularly through standards like ERC-4337, shifts wallet functionality from Externally Owned Accounts (EOAs) to smart contract wallets. This enables programmable features directly within the wallet, such as gasless transactions, social recovery, multi-factor authentication, and batching multiple operations into a single transaction. By allowing smart contracts to initiate transactions and define their own rules for transaction approval and gas payment, AA reduces reliance on private keys and simplifies complex processes for users, making blockchain technology more accessible and secure.

**Key Insight:** Trade-offs - *Session keys and account abstraction improve UX by reducing transaction friction but introduce complexity in defining appropriate scopes and securing smart contract logic.*

---

#### Q5: How can social recovery mechanisms be securely implemented in blockchain wallets, and what are the key considerations for their widespread adoption?

**Difficulty:** Intermediate | **Type:** Practical

**Answer:** Social recovery mechanisms offer a way to regain access to blockchain wallets without relying on a single seed phrase, significantly improving security and usability for many users. Secure implementation typically involves smart contract wallets where a primary signing key is used for daily transactions, but a pre-selected group of "guardians" can help recover or change this key if it's lost or compromised. Key considerations include:
- **Guardian Selection and Management**: Users must carefully choose trusted individuals or entities (guardians) who will hold recovery shares or have authority in the recovery process. The mechanism should allow for easy addition, removal, and replacement of guardians.
- **Security of Recovery Process**: The recovery process itself must be robust against collusion among guardians or attacks on individual guardians. This can involve requiring a threshold number of guardians to approve the recovery, multi-factor authentication for guardians, or time delays for recovery requests to allow the user to intervene.
- **Decentralization and Trustlessness**: Ideally, social recovery should minimize reliance on centralized services. ERC-4337, for example, allows wallets to implement recovery systems without protocol-level changes, enabling more decentralized approaches.
- **User Education**: Users need to understand how to set up their guardians, initiate recovery, and the implications of their choices.
- **Blockchain Platform**: Implementation on established public blockchains like Ethereum provides reliability and smart contract capabilities.
- **Privacy**: The recovery process should ideally reveal minimal information about the user or their assets to the guardians.
Prominent examples include Argent and Loopring wallets, which have implemented social recovery, primarily focusing on the Ethereum ecosystem. Some implementations also integrate with hardware wallets and use smart contracts to manage the recovery logic.

**Key Insight:** Failure Path - *Insufficient security in the guardian selection or recovery process can lead to unauthorized access, compromising the wallet despite its recovery feature.*

---

### Topic 2: Transaction Signing & Blockchain Interoperability

#### Q6: Explain the structure of an Ethereum EIP-1559 transaction and how it differs from legacy transactions, particularly concerning gas fee mechanisms.

**Difficulty:** Foundational | **Type:** Theoretical

**Answer:** Ethereum EIP-1559 transactions fundamentally restructure how gas fees are managed, differing significantly from legacy transactions. A legacy transaction consists of fields like `nonce`, `gas price`, `gas limit`, `to address`, `value`, `data`, `v`, `r`, and `s`, which are RLP-encoded. In this model, users specify a `gasPrice`, and miners prioritize transactions with higher bids, leading to volatile and often overpriced fees. EIP-1559, introduced in Ethereum's London Upgrade (Type 2 transactions), replaces the single `gasPrice` with a more predictable and dynamic fee mechanism. Key components include:
- **`baseFeePerGas`**: This is a dynamically changing protocol-adjusted fee that is burned, not paid to miners. It adjusts block by block based on network congestion, making transaction costs more predictable.
- **`maxPriorityFeePerGas`**: This is an optional "tip" or "bribe" paid directly to the miner to incentivize inclusion of the transaction, especially during periods of high network demand. It specifies the maximum fee the sender is willing to pay *above* the `baseFeePerGas`.
- **`maxFeePerGas`**: This is the maximum total fee the user is willing to pay per unit of gas, encompassing both the `baseFeePerGas` and `maxPriorityFeePerGas`.
If the total `maxFeePerGas` exceeds the sum of the `baseFeePerGas` and `maxPriorityFeePerGas`, the difference is refunded to the user. This new structure aims to reduce gas price volatility and improve user experience by making costs more transparent and predictable.

**Key Insight:** Misconception - *EIP-1559 does not eliminate gas fees; instead, it re-architects the fee market to make it more predictable and includes a burning mechanism for the base fee.*

---

#### Q7: What are the security and performance implications of using different elliptic curve cryptography schemes (e.g., ECDSA, Ed25519) in blockchain signature standards?

**Difficulty:** Advanced | **Type:** Comparison

**Answer:** The choice between elliptic curve cryptography (ECC) schemes like ECDSA and Ed25519 in blockchain signature standards carries significant security and performance implications. ECC is fundamental to blockchain, offering strong security with smaller key sizes compared to traditional algorithms, thereby reducing computational and storage demands.

- **ECDSA (Elliptic Curve Digital Signature Algorithm)**:
  - **Security**: Widely used in Bitcoin and Ethereum, ECDSA's security heavily relies on the proper generation and uniqueness of a random `nonce` (k) for each signature. Reusing a nonce or generating weak nonces can lead to private key recovery and significant vulnerabilities. Threshold ECDSA schemes, like GG18 and GG20, aim to mitigate single points of failure by distributing key control.
  - **Performance**: While generally efficient, ECDSA signatures are non-deterministic, meaning each signature for the same message will be different due to the random nonce. This impacts consistency in certain cryptographic operations.

- **Ed25519 (Edwards-curve Digital Signature Algorithm)**:
  - **Security**: Ed25519 offers strong security based on well-understood properties of hash functions, often being resistant to side-channel attacks that can compromise ECDSA implementations. It provides deterministic signatures, eliminating the nonce-reuse vulnerability inherent in ECDSA.
  - **Performance**: Ed25519 is known for its high performance in signature generation and verification, often outperforming other curves. This makes it suitable for environments requiring faster digital signatures.
  - **Use Cases**: Ed25519 is utilized in protocols like TLS 1.3, SSH, Tor, ZCash, and WhatsApp/Signal. While Ethereum doesn't natively support Ed25519 operations in the EVM, requiring substantial computational resources for implementation, other blockchains like Hedera support both ECDSA and Ed25519. Threshold Ed25519 schemes also exist, leveraging the Schnorr signature scheme for key aggregation.

In summary, Ed25519 generally offers better security against implementation flaws (like nonce reuse) and often superior performance due to its deterministic nature and optimized curve, while ECDSA remains widely adopted, particularly in major cryptocurrencies, but demands meticulous implementation practices.

**Key Insight:** Trade-offs - *ECDSA is widely adopted but vulnerable to nonce-reuse if implemented incorrectly, while Ed25519 offers deterministic signatures and high performance with stronger inherent security against common pitfalls, though its direct EVM support is limited.*

---

#### Q8: Discuss best practices for integrating cryptographic libraries (e.g., Libsodium, Rust crypto crates) into blockchain wallet systems to ensure both security and performance.

**Difficulty:** Advanced | **Type:** Practical

**Answer:** Integrating cryptographic libraries into blockchain wallet systems requires strict adherence to best practices to balance security and performance effectively.
- **Utilize Well-Vetted Libraries**: Prioritize mature, open-source libraries like Libsodium or popular Rust crypto crates (e.g., `dalek-ed25519`, `rust-crypto`) that have undergone extensive peer review and security audits. Avoid implementing cryptographic primitives from scratch, as this is prone to errors.
- **Secure Key Derivation and Storage**: Implement robust key derivation functions (KDFs) to generate cryptographic keys from master secrets or user inputs. Ensure private keys and mnemonic phrases are stored securely, ideally offline in Hardware Security Modules (HSMs) or secure enclaves, or through multi-party computation (MPC) schemes to prevent single points of compromise.
- **Proper Randomness**: Cryptographic operations rely heavily on high-quality random number generation. Ensure the libraries use cryptographically secure pseudorandom number generators (CSPRNGs) for all sensitive operations, such as nonce generation in ECDSA.
- **Avoid Misuse of APIs**: Cryptographic APIs are complex and often misused, leading to vulnerabilities. Developers must thoroughly understand the functions and their correct application, employing tools for static and runtime analysis to detect misuses.
- **Performance Optimization**:
    - **Hardware Acceleration**: Leverage hardware-accelerated cryptographic instructions (e.g., AES-NI) available on modern CPUs for symmetric-key operations, which can drastically improve performance.
    - **Algorithm Choice**: Select algorithms optimized for the target environment (mobile, web, backend). For instance, Ed25519 is often faster for signing and verification than ECDSA in many contexts.
    - **Caching**: Implement intelligent caching strategies to minimize redundant cryptographic computations, especially for frequently accessed data.
    - **Batch Processing**: Where applicable, batch cryptographic operations to reduce overhead and improve throughput.
- **Cross-Platform Adaptability**: For multi-platform wallets, ensure the chosen libraries offer consistent and secure functionality across different operating systems and environments (e.g., WebAssembly for web).
- **Regular Audits and Updates**: Perform continuous security audits and keep cryptographic libraries updated to patch vulnerabilities and incorporate the latest security enhancements.

**Key Insight:** Failure Path - *Misusing cryptographic APIs or failing to ensure proper randomness and secure key storage are common pitfalls that can severely compromise the security of blockchain wallets, even when using robust libraries.*

---

#### Q9: How are Merkle trees and hash-based commitment schemes utilized in blockchain wallets and cryptographic protocols, and what security benefits do they provide?

**Difficulty:** Intermediate | **Type:** Theoretical

**Answer:** Merkle trees and hash-based commitment schemes are fundamental cryptographic primitives extensively used in blockchain wallets and protocols to ensure data integrity, efficiency, and privacy.

- **Merkle Trees**:
  - **Utilization**: Merkle trees organize and encode transaction data through a series of cryptographic hashes, forming a tree-like structure where leaf nodes are hashes of individual transactions, and internal nodes are hashes of their child nodes. The topmost hash is the "Merkle Root". Ethereum utilizes Merkle Patricia Tries for committing to account states, transactions, and receipts, with their roots included in block headers.
  - **Security Benefits**:
    - **Efficient Verification (Merkle Proofs)**: They enable efficient and secure verification that a specific transaction or piece of data is included in a block or dataset without downloading the entire blockchain. A "Merkle proof" consists of the Merkle root, the data element, and the hashes of its siblings up the tree, allowing light clients (SPV wallets) to verify transactions with minimal data.
    - **Data Integrity**: Any alteration to a single transaction will change its hash, propagating up the tree and altering the Merkle root, thus making tampering easily detectable.
    - **Scalability**: By committing to thousands of transactions with a single Merkle root, they keep the blockchain size small and facilitate efficient storage.

- **Hash-Based Commitment Schemes**:
  - **Utilization**: These schemes allow a party (the committer) to commit to a value (a message) without revealing it, and then later reveal the value and prove that it is indeed the committed value. They are used in various cryptographic protocols like zero-knowledge proofs and secure computation. In payment channels, they can conceal transaction amounts between users.
  - **Security Benefits**:
    - **Binding and Hiding Properties**: A commitment scheme is typically "hiding" (the verifier cannot learn the committed value) and "binding" (the committer cannot change the committed value after committing).
    - **Post-Quantum Security**: Hash-based signatures, which often incorporate hash-based commitment principles, are promising candidates for post-quantum cryptography, as their security relies on the well-understood properties of hash functions, making them resistant to quantum computer attacks.

In summary, Merkle trees ensure the integrity and efficient verification of large datasets in public blockchains, while hash-based commitment schemes provide a foundational tool for privacy-preserving protocols by enabling verifiable commitments to secret information.

**Key Insight:** Trade-offs - *While Merkle trees enable efficient transaction verification and data integrity in public blockchains, hash-based commitment schemes provide privacy by allowing parties to commit to values without immediately revealing them, which is crucial for secure multi-party computations.*

---

### Topic 3: Security & Risk Management in Blockchain Wallets

#### Q10: Analyze the attack surface of crypto wallet systems, particularly focusing on the differences between hot, warm, and cold wallets, and propose mitigation strategies.

**Difficulty:** Advanced | **Type:** Security

**Answer:** The attack surface of crypto wallet systems varies significantly across hot, warm, and cold wallet types, each demanding distinct mitigation strategies. The core vulnerability across all types revolves around the private key.

- **Hot Wallets**: These are online wallets (e.g., desktop, mobile, web-based) that are always connected to the internet.
  - **Attack Surface**: High susceptibility to malware, phishing attacks, keyloggers, remote access Trojans, and supply chain attacks. Exploits can occur during key generation, storage (software access), or usage (signing transactions). Exchange hot wallets are frequent targets.
  - **Mitigation**: Multi-factor authentication (MFA), strong password policies, regular security audits, and keeping software updated. For web wallets, secure coding practices and protection against common web vulnerabilities are crucial. MPC wallets can be used for hot key signing mechanisms, distributing key shares to enhance security.

- **Warm Wallets**: These wallets have intermittent or controlled internet connectivity, often used for operational funds requiring frequent access, balancing convenience with security.
  - **Attack Surface**: Lower than hot wallets but still vulnerable during periods of connectivity or through compromised devices used to access them. Can be targets for insider threats if not properly managed.
  - **Mitigation**: Strict access controls, white-listing IP addresses, time-locked transactions, and robust internal audit trails. Combining warm wallets with MPC technology or secure enclaves can reduce the risk during "online" phases.

- **Cold Wallets**: These are offline wallets (e.g., hardware wallets, paper wallets) that store private keys completely disconnected from the internet.
  - **Attack Surface**: Minimal digital attack surface once offline. Vulnerabilities primarily shift to physical theft, damage, or compromise during initial setup or recovery. Social engineering during backup phrase handling is also a risk.
  - **Mitigation**: Secure physical storage, robust backup procedures (e.g., multiple copies of seed phrases stored in geographically dispersed, secure locations), and careful verification during setup and recovery. Hardware wallets like Ledger use secure element chips to isolate private keys.

Overall, a layered security approach incorporating MPC, HSMs, MFA, and sound operational practices is essential for comprehensive crypto wallet security.

**Key Insight:** Failure Path - *The shift from hot to cold wallets reduces digital attack vectors but introduces new physical and social engineering risks, highlighting the need for a comprehensive, multi-layered security strategy.*

---

#### Q11: How do Hardware Security Modules (HSMs) and Key Management Services (KMS) contribute to the security of blockchain asset custody, and what are their limitations in a multi-cloud environment?

**Difficulty:** Advanced | **Type:** Security

**Answer:** Hardware Security Modules (HSMs) and Key Management Services (KMS) are critical components in securing blockchain asset custody, providing robust protection for cryptographic keys.

- **HSMs**: These are tamper-resistant physical devices designed to generate, protect, and manage cryptographic keys within a secure boundary. They ensure keys never leave the module in plaintext and perform cryptographic operations internally. This provides the highest level of physical and logical security for private keys, crucial for blockchain wallets where key compromise is irreversible. HSMs are often FIPS 140-2/3 certified, indicating a high standard of security.
- **KMS**: A KMS is a system designed to manage the lifecycle of cryptographic keys, including generation, storage, usage, rotation, and destruction. It makes encryption enforceable and provides a centralized control plane for key policies. Cloud providers like AWS (KMS) and Azure (Key Vault) offer managed KMS solutions that integrate with their cloud services.

**Contributions to Security**:
- **Secure Key Storage**: Both HSMs and KMS protect keys from unauthorized access, with HSMs providing hardware-level isolation.
- **Lifecycle Management**: KMS ensures keys are managed according to best practices throughout their existence.
- **Compliance**: They help organizations meet stringent regulatory requirements for data protection and key management.
- **Reduced Insider Threat**: Keys never leave the HSM, reducing exposure even to system administrators.

**Limitations in a Multi-Cloud Environment**:
- **Fragmented Policies**: Organizations using multiple cloud providers (AWS, Azure, Google Cloud) often face fragmented key management systems, leading to inconsistent encryption policies and access controls across different clouds.
- **Vendor Lock-in**: Relying solely on platform-native KMS solutions creates strong dependency on a single service provider, limiting flexibility and potentially increasing costs for multi-cloud strategies.
- **Complexity**: Integrating external HSMs or self-managed KMS solutions into a multi-cloud environment adds complexity to governance and system integrations.
- **Cloud-Native Threats**: Despite hardware protection, HSMs and TPMs in cloud environments face challenges from misconfigurations, compromised APIs, and lateral privilege escalations inherent to cloud infrastructure.
- **Interoperability**: Ensuring seamless and secure interoperability for key management across disparate cloud platforms remains a challenge.

To mitigate these limitations, hybrid approaches combining platform-native and external KMSs, or self-hosted KMSs within the cloud, can offer improved resiliency and flexibility, albeit with increased complexity. MPC also offers a decentralized key management approach where no single device holds the full key material, providing an alternative for multi-cloud deployments.

**Key Insight:** Trade-offs - *While HSMs and KMS provide robust key protection, their multi-cloud deployment introduces complexities in maintaining consistent security policies, avoiding vendor lock-in, and mitigating cloud-native threats, necessitating careful architectural design and potentially hybrid solutions.*

---

#### Q12: Discuss multi-factor authentication (MFA) and device validation strategies in blockchain wallet systems, including modern approaches like FIDO2/WebAuthn and TOTP.

**Difficulty:** Intermediate | **Type:** Practical

**Answer:** Multi-factor authentication (MFA) and device validation are crucial for bolstering the security of blockchain wallet systems, guarding against unauthorized access even if a primary credential is compromised.

- **Multi-Factor Authentication (MFA)**:
  - **Purpose**: MFA requires users to provide two or more distinct forms of identification (e.g., something you know, something you have, something you are) to access an account. This adds an extra layer of security beyond just a password or private key.
  - **Traditional Approaches**:
    - **TOTP (Time-based One-Time Password)**: Generates a temporary, unique code on a device (e.g., smartphone app, hardware token) that changes every 30-60 seconds. While better than SMS-based 2FA, TOTP can still be susceptible to phishing if the user enters the code on a malicious site, and has limitations regarding accuracy and time-drift in hardware tokens.
  - **Modern Approaches (FIDO2/WebAuthn)**:
    - **FIDO2/WebAuthn**: These standards offer strong, phishing-resistant authentication by using public-key cryptography and device-bound credentials. Users authenticate locally via a device's unlock mechanism (e.g., biometrics, PIN), and the device then uses public-key cryptography to authenticate to the website. This prevents credential theft from phishing and man-in-the-middle attacks. FIDO2 supports passwordless authentication and multiple factor experiences with embedded or external authenticators.
    - **Benefits**: FIDO2 is considered more secure than TOTP and SMS-based MFA because it cryptographically binds authentication to the originating domain, preventing replay attacks and phishing. It works across major browsers and operating systems.

- **Device Validation Strategies**:
  - **Device Binding**: Ensures that access to a wallet is tied to a specific, trusted device. This can involve cryptographic attestations that verify the device's integrity or secure hardware elements.
  - **Risk Control**: Implementing risk-based authentication, where the authentication validity depends on the context of the transaction (e.g., amount, recipient, unusual activity). This can involve heuristic analysis to detect anomalies or suspicious patterns in cryptocurrency transactions.
  - **Multi-Factor Device Authentication**: Using a combination of device-specific factors, such as biometric data (fingerprint, face recognition) combined with device movement for authentication.
  - **Integration with KMS/HSM**: Leveraging secure hardware for key storage and operations on trusted devices further enhances security.

The implementation of these strategies aims to create a robust defense-in-depth security posture for blockchain wallets, significantly reducing the risk of unauthorized access and asset compromise.

**Key Insight:** Trade-offs - *While TOTP offers a convenient second factor, FIDO2/WebAuthn provides superior phishing resistance by cryptographically binding authentication to the device and domain, addressing a critical vulnerability in many online authentication flows.*

---

### Topic 4: Advanced Cryptographic Concepts & Applications

#### Q13: Explain the concept of zero-knowledge proofs (ZKPs) and their practical applications in enhancing privacy and scalability within blockchain wallets and security systems.

**Difficulty:** Advanced | **Type:** Theoretical

**Answer:** Zero-Knowledge Proofs (ZKPs) are a cryptographic technique allowing one party (the prover) to convince another party (the verifier) that a statement is true, without revealing any information beyond the validity of the statement itself. This "zero-knowledge" property is fundamental for enhancing privacy and scalability in blockchain.

- **How ZKPs Work**: ZKPs rely on three core properties:
  - **Completeness**: If the statement is true, an honest prover can convince an honest verifier.
  - **Soundness**: If the statement is false, a dishonest prover cannot convince an honest verifier (except with a negligible probability).
  - **Zero-knowledge**: The verifier learns nothing about the secret (witness) from the proof beyond the fact that the statement is true.

- **Practical Applications in Blockchain**:
  - **Privacy**:
    - **Anonymous Transactions**: ZKPs enable transactions where details like sender, receiver, and amount can be hidden while still proving the transaction's validity. Zcash is a prime example, using zk-SNARKs to achieve shielded transactions.
    - **Identity Verification**: Users can prove specific attributes (e.g., being over 18) without revealing their exact age or other personal details, facilitating anonymous logins and compliance without exposing sensitive data.
    - **Private Wallets**: ZKPs can be integrated into wallets to enable privacy-preserving operations, allowing users to verify information without disclosing confidential data.
  - **Scalability (ZK-Rollups)**:
    - **Off-chain Computation**: ZKPs are central to ZK-Rollups, a Layer 2 scaling solution for Ethereum. Transactions are processed off-chain in batches, and a concise ZKP (e.g., zk-SNARK or zk-STARK) is generated to prove the correctness of these computations.
    - **Reduced On-chain Data**: Only the ZKP (which is very small) is submitted to the main chain for verification, drastically reducing the data stored and computed on the mainnet, thereby improving transaction throughput and reducing gas fees.
    - **Fast Finality**: Unlike Optimistic Rollups, ZK-Rollups offer fast transaction finality because the validity of off-chain computations is cryptographically proven on-chain, eliminating challenge periods.

- **Types of ZKPs**:
  - **zk-SNARKs (Zero-Knowledge Succinct Non-Interactive Argument of Knowledge)**: Offer small proof sizes and fast verification, but often require a "trusted setup" to generate public parameters.
  - **zk-STARKs (Zero-Knowledge Scalable Transparent Argument of Knowledge)**: Do not require a trusted setup, offer better scalability for large datasets, and are considered quantum-resistant, though proof sizes can be larger.

Overall, ZKPs are transformative for blockchain, enabling a future where transactions and interactions can be private, scalable, and verifiable without compromising trust.

**Key Insight:** Misconception - *ZKPs do not reveal any information to the verifier; they merely confirm the truth of a statement, which is key for privacy-preserving and scalable blockchain solutions.*

---

#### Q14: Describe how approval and limit flows can be implemented in blockchain wallets to enhance security and user control over digital assets, especially in DeFi contexts.

**Difficulty:** Intermediate | **Type:** Practical

**Answer:** Approval and limit flows in blockchain wallets are essential mechanisms to enhance security and user control, particularly in the context of Decentralized Finance (DeFi) where users frequently interact with smart contracts. These flows provide granular control over how dApps or other smart contracts can interact with a user's digital assets.

- **Token Approvals (ERC-20 Standard)**:
  - **Mechanism**: The ERC-20 standard includes `approve`, `allowance`, and `transferFrom` functions that enable a user to grant a smart contract (the "spender") permission to spend a certain amount of their tokens on their behalf. This is commonly required for interacting with DEXs, lending platforms, or yield farms.
  - **Security Enhancement**: Users can set specific approval limits instead of granting "unlimited" approvals, which is a significant security risk. An unlimited approval means the approved contract can transfer *any amount* of tokens at any time, potentially leading to asset drain if the contract is exploited or malicious. Wallets can integrate features to review exact approval parameters on a secure screen before confirming.
  - **User Control**: Users can use "token approval checkers" to view and revoke active permissions granted from their wallets, allowing them to rescind access from suspicious or no-longer-used contracts.

- **Limit Flows (Spending Limits)**:
  - **Mechanism**: Wallets can allow users to set daily, weekly, or per-transaction spending limits for specific tokens or dApps. This means that even if a private key or session key is compromised, the attacker can only spend up to the predefined limit within that timeframe.
  - **Security Enhancement**: Provides a crucial layer of risk control, acting as a circuit breaker for unauthorized transactions. This is particularly valuable in scenarios where a user might accidentally sign a malicious transaction or grant overly broad permissions.
  - **Implementation**: These limits can be enforced at the smart contract level (for smart contract wallets through Account Abstraction) or through client-side wallet logic, ideally with on-chain enforcement for maximum security.
  - **Transaction Approval UX**: Designing clear and intuitive user interfaces for transaction approval is vital. Wallets should clearly display the implications of approvals (e.g., which contract, what amount, duration) and prompt users for confirmation in an easy-to-understand manner.

- **Account Abstraction (AA) Integration**: With AA (ERC-4337), these approval and limit flows can be natively integrated into the smart contract wallet's logic, making them highly customizable and programmable. This allows for more sophisticated policies, such as batch approvals or conditional spending based on specific criteria.

By implementing these features, blockchain wallets empower users to manage their digital assets with greater confidence and significantly reduce exposure to various DeFi-related risks.

**Key Insight:** Failure Path - *Granting unlimited token approvals creates a severe vulnerability where compromised smart contracts can drain all user funds; explicit limit flows are a critical mitigation.*

---

#### Q15: What are the performance optimization strategies for cryptographic operations in mobile, web, and backend environments within blockchain applications?

**Difficulty:** Advanced | **Type:** Performance

**Answer:** Performance optimization strategies for cryptographic operations across mobile, web, and backend environments within blockchain applications are crucial for maintaining responsiveness and scalability.

- **Mobile Environments**:
    - **Hardware Acceleration**: Leverage mobile processors with dedicated cryptographic acceleration (e.g., ARM TrustZone, secure enclaves) to offload intensive operations like AES or elliptic curve computations.
    - **Algorithm Selection**: Choose lightweight cryptographic algorithms that offer sufficient security while having lower computational demands suitable for resource-constrained devices. Ed25519, for instance, is often preferred for its efficiency over ECDSA.
    - **Optimized Implementations**: Use highly optimized cryptographic libraries or ensure the implementation avoids unnecessary overhead, such as explicit padding instead of compiler optimizations.
    - **Batch Processing**: Bundle multiple cryptographic operations where possible to reduce the overhead of context switching or repeated initialization.
    - **Resource Management**: Efficiently manage memory and CPU cycles, especially when dealing with multi-precision arithmetic operations common in public-key cryptography.
- **Web Environments**:
    - **WebAssembly (Wasm)**: Compile cryptographic primitives to WebAssembly for near-native performance in browsers, significantly faster than JavaScript implementations.
    - **Web Workers**: Offload computationally intensive cryptographic tasks to Web Workers to prevent blocking the main UI thread, maintaining a smooth user experience.
    - **Caching**: Implement caching strategies for frequently used cryptographic keys or results of expensive operations to minimize redundant computations and reduce latency.
    - **Lazy Loading**: Load cryptographic libraries or components only when needed to reduce initial page load times.
    - **Backend Offloading**: Delegate complex or computationally intensive cryptographic tasks to a more powerful backend server where resources are less constrained.
- **Backend Environments**:
    - **Hardware Security Modules (HSMs)**: For high-security and high-throughput environments, offload cryptographic key generation, storage, and operations to HSMs. HSMs are optimized for these algorithms and minimize performance hits from asymmetric cryptography.
    - **Cloud KMS**: Utilize cloud-native Key Management Services (KMS) like AWS KMS or Azure Key Vault for managed key lifecycle and cryptographic operations, often with underlying HSMs.
    - **Load Balancing and Distributed Architectures**: Distribute cryptographic workload across multiple servers or nodes using load balancers to handle high request volumes.
    - **Parallel Processing**: Utilize multi-threading or parallel computing frameworks to execute multiple cryptographic operations concurrently.
    - **Optimized Libraries and Compilers**: Ensure that the backend is running highly optimized cryptographic libraries (e.g., OpenSSL, Libsodium) and that compilers are configured for maximum performance.
    - **Asynchronous Operations**: Implement asynchronous programming models for cryptographic tasks to prevent blocking I/O and improve overall system throughput.

Across all environments, continuous performance benchmarking and profiling are essential to identify bottlenecks and validate the effectiveness of optimization strategies.

**Key Insight:** Trade-offs - *Optimizing cryptographic performance across mobile, web, and backend involves a trade-off between client-side responsiveness (WebAssembly, Web Workers for mobile/web) and server-side robustness/security (HSMs, KMS for backend), requiring tailored strategies for each environment.*

---

## Reference Sections

### Glossary, Terminology & Acronyms

**G1: Account Abstraction (AA)**: A feature in blockchain wallets (often smart contract-based) that allows users to customize transaction validation logic, enabling features like social recovery, batch transactions, and gasless payments
**G2: ECDSA** (Elliptic Curve Digital Signature Algorithm): A cryptographic algorithm used by Bitcoin and Ethereum for digital signatures, relying on elliptic curve theory
**G3: Ed25519**: A specific instance of the Edwards-curve Digital Signature Algorithm (EdDSA) known for its high performance and strong security properties
**G4: FROST** (Flexible Round-Optimized Schnorr Threshold): A threshold signature scheme built on Schnorr signatures that allows a threshold number of signers to produce a valid signature
**G5: GG18/GG20**: Threshold ECDSA protocols (Gennaro & Goldfeder 2018/2020) for distributed signing among multiple parties, designed for improved efficiency and robustness
**G6: HSM** (Hardware Security Module): A physical computing device that safeguards and manages digital keys for strong authentication and provides cryptoprocessing
**G7: KMS** (Key Management Service): A centralized system for managing the lifecycle of cryptographic keys, including generation, storage, usage, and rotation
**G8: MPC** (Multi-Party Computation): A cryptographic protocol that enables multiple parties to jointly compute a function over their private inputs without revealing those inputs to each other
**G9: Merkle Tree**: A hash-based data structure used in blockchain to efficiently verify the integrity and inclusion of large sets of data, such as transactions
**G10: Session Key**: A temporary cryptographic key used for a limited duration or for a specific set of operations within a blockchain wallet, enhancing user experience and security
**G11: Threshold Signature Scheme (TSS)**: A cryptographic protocol that distributes the ability to sign digital transactions among multiple parties, requiring a minimum "threshold" number of parties to collectively sign
**G12: ZKP** (Zero-Knowledge Proof): A cryptographic method where one party can prove to another that a given statement is true, without revealing any additional information apart from the truth of the statement itself

### Codebase & Library References

**C1: Safeheron/multi-party-sig-cpp** (C++)
- Stack/Modules: C++ based MPC protocol library implementing GG18.
- Maturity: Unknown license, not explicitly stated last update, stable release status not specified, but it's part of a company's offerings.
- Benchmarks: Not explicitly mentioned performance data or security audit status in the provided passage, but Safeheron has released it as the world's first C++ based MPC protocol library.
- Security audit status: Safeheron's MPC-ECDSA algorithm underwent a security audit in October 2023.
- Repository URL: https://github.com/Safeheron/multi-party-sig-cpp

**C2: ZenGo-X/multi-party-ecdsa** (Rust)
- Stack/Modules: Rust implementation of {t,n}-threshold ECDSA, specifically noted for GG18.
- Maturity: Unknown license, not explicitly stated last update, stable release status not specified.
- Benchmarks: Not explicitly mentioned, but the project is part of ZenGo-X's efforts in multi-party ECDSA.
- Security audit status: ZenGo's multi-party ECDSA underwent a security audit by Kudelski Security in October 2019.
- Repository URL: https://github.com/ZenGo-X/multi-party-ecdsa

**C3: bnb-chain/tss-lib** (Go)
- Stack/Modules: Threshold Signature Scheme library for ECDSA, noted for GG18-like behavior and one-round signing options.
- Maturity: Unknown license, last update not explicitly mentioned but implied to be actively maintained given release statement, stable release status not specified.
- Benchmarks: Not explicitly mentioned.
- Security audit status: Audited by security professionals.
- Repository URL: https://github.com/bnb-chain/tss-lib

**C4: ZcashFoundation/frost** (Rust)
- Stack/Modules: Rust implementation of FROST (Flexible Round-Optimised Schnorr Threshold signatures), including trusted dealer key generation.
- Maturity: MIT License, actively maintained with recent updates related to Zcash's specific needs, stable release status implied through Zcash's adoption.
- Benchmarks: Not explicitly mentioned, but the implementation is designed for Zcash's privacy guarantees and protocol-specific needs.
- Security audit status: Under security audit by NCC Group (Summer 2023).
- Repository URL: https://github.com/ZcashFoundation/frost

**C5: taurushq-io/frost-ed25519** (Go)
- Stack/Modules: Go implementation of FROST threshold signature protocol for Ed25519.
- Maturity: Not explicitly stated license, last update not specified, stable release status not specified but released by Taurus (a crypto custody firm) in 2021.
- Benchmarks: Not explicitly mentioned.
- Security audit status: Not explicitly mentioned, but implemented by a crypto custody firm.
- Repository URL: https://github.com/taurushq-io/frost-ed25519

### Authoritative Literature & Reports

**L1: Fast Multiparty Threshold ECDSA with Fast Trustless Setup** (2018) ()
- Core Findings: Introduced a threshold signature scheme for ECDSA supporting any t <= n players with efficient dealerless key generation, proving security against malicious adversaries with a dishonest majority. Claimed faster performance and reduced communication complexity than previous solutions.
- Methodology: Theoretical cryptographic protocol design and security proof, followed by an implementation to demonstrate efficiency and practical deployability.
- Impact: A foundational paper for threshold ECDSA, inspiring subsequent protocols like GG20 and influencing the design of MPC wallets.
- Persistent Link: https://www.semanticscholar.org/paper/3321190a9c8404f9598c38326a174078d27e6780

**L2: The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol** (2023) ()
- Core Findings: Specifies the FROST signing protocol for Schnorr signatures, enabling threshold number of entities to cooperate and produce a single signature with improved distribution of trust and redundancy. Designed for network performance requirements.
- Methodology: Formal specification document (RFC 9591) by the Crypto Forum Research Group (CFRG) in the IRTF.
- Impact: Provides a standardized, secure, and efficient threshold signature scheme for Schnorr signatures, with implementations like Zcash's FROST built upon it.
- Persistent Link: https://www.rfc-editor.org/rfc/rfc9591.html

**L3: A Survey of ECDSA Threshold Signing** (2020) ()
- Core Findings: Reviews the state-of-the-art threshold signing protocols, highlighting their unique properties, comparing them in terms of security assurance and performance, and identifying open problems relevant to real-world challenges. Emphasizes progress driven by blockchain applications.
- Methodology: Comprehensive survey of academic literature and main open-source implementations.
- Impact: Provides a clear overview for researchers and practitioners on the landscape of threshold ECDSA, particularly for blockchain applications.
- Persistent Link: https://www.semanticscholar.org/paper/6bc96ca829a4759905b521a530b39e93a13c4401

**L4: New Key Extraction Attacks on Threshold ECDSA Implementations** (2023) ()
- Core Findings: Presents a comprehensive analysis of the security of Threshold ECDSA, outlining cryptographic primitives and showing that many implementations of GG18, GG20, and CGGMP21 were found vulnerable to new key extraction attacks despite security audits.
- Methodology: Security analysis of existing implementations and identification of architectural and operational flaws.
- Impact: Highlights critical vulnerabilities in widely used threshold ECDSA protocols, urging for more rigorous security evaluations and careful implementation.
- Persistent Link: https://i.blackhat.com/BH-US-23/Presentations/US-23-Nguyen-TSSHOCK-Breaking-MPC-Wallets-wp.pdf

**L5: Optimizing Web Performance and Computational Efficiency: A Deep Dive into WebAssembly's Technical Advancements and Real-World Applications** (2025) ()
- Core Findings: Provides an in-depth look at WebAssembly's technical details, benchmark implementations, and optimization strategies to improve web performance and computational efficiency.
- Methodology: Technical analysis and benchmark studies.
- Impact: Demonstrates WebAssembly's potential for high-performance applications on the web, including cryptographic operations, by enabling near-native execution speeds.
- Persistent Link: https://www.researchgate.net/profile/Son-Nguyen-386/publication/389517325_Optimizing_Web_Performance_and_Computational_Efficiency_A_Deep_Dive_into_WebAssembly's_Technical_Advancements_and_Real-World_Applications/links/67c62ce1207c0c20faa03019/Optimizing-Web-Performance-and-Computational-Efficiency-A-Deep-Dive-into-WebAssemblys-Technical-Advancements-and-Real-World-Applications.pdf

**L6: \u96f6\u77e5\u8bc6\u8bc1\u660e\u6982\u5ff5\u53ca\u5176\u5bf9\u533a\u5757\u94fe\u7684\u5f71\u54cd** (2023) ()
- Core Findings: Explains the concept of Zero-Knowledge Proofs (ZKPs) and their impact on blockchain, particularly in enabling privacy-preserving transactions and scalability through ZK-Rollups.
- Methodology: Conceptual overview and discussion of applications.
- Impact: Provides foundational understanding of ZKPs for blockchain practitioners and enthusiasts, highlighting their role in future blockchain development.
- Persistent Link: https://www.binance.com/zh-CN/academy/articles/what-is-zero-knowledge-proof-and-how-does-it-impact-blockchain

### APA Style Source Citations

**English Sources**
 A security site. (n.d.). _2-of-2 threshold ECDSA signing algorithm using GG20 with Kryptology_. https://asecuritysite.com/signatures/sss_gg02
 A security site. (n.d.). _Any t-of-n threshold ECDSA signing algorithm using GG20 with Kryptology_. https://asecuritysite.com/kryptology/sss_gg03
 A security site. (n.d.). _Threshold Ed25519 \u2014 It's Just Magical And Fit For A More Resilient And Trusted World_. https://medium.com/asecuritysite-when-bob-met-alice/threshold-ed25519-its-just-magical-and-fit-for-a-more-resilient-and-trusted-world-5431e124942
 Alchemy. (n.d.). _MPC Wallets: Complete Developer Guide 2025_. https://www.alchemy.com/overviews/what-is-a-multi-party-computation-mpc-wallet
 Alchemy. (n.d.). _How do ERC-4337 smart contract wallets work?_ https://www.alchemy.com/overviews/how-do-smart-contract-wallets-work
 Blocknative. (n.d.). _Introductory Guide to Account Abstraction (ERC-4337)_. https://www.blocknative.com/blog/account-abstraction-erc-4337-guide
 CertiK. (n.d.). _Binance tss-lib's 9-Round Threshold ECDSA_. https://www.certik.com/resources/blog/threshold-cryptography-iii-binance-tss-libs-9-round-threshold-ecdsa
 Chair of Cryptography and Security. (n.d.). _UC Non-Interactive, Proactive, Threshold ECDSA_. https://www.semanticscholar.org/paper/afa125a64a723eb7d7fbf02f9c1d6a426ab7e5b8
 Chainalysis. (n.d.). _How Off-Chain and On-Chain Data Can Prevent Crypto Fraud_. https://www.chainalysis.com/blog/preventing-crypto-fraud-with-off-chain-on-chain-data/
 Coinbase. (n.d.). _What is Two-Factor Authentication (2FA) in crypto?_ https://www.coinbase.com/learn/wallet/what-is-two-factor-authentication-2fa-in-crypto
 Crypto APIs. (n.d.). _What Is the Threshold Signature Scheme?_ https://cryptoapis.io/blog/78-what-is-the-threshold-signature-scheme
 CryptoEQ. (n.d.). _Enhancing Cryptocurrency Security with Multi-sig Wallets and ..._. https://www.cryptoeq.io/articles/wallet-multisig-security
 Cube.exchange. (n.d.). _What is MPC (Multi-Party Computation)? Crypto wallets & Web3_. https://www.cube.exchange/what-is/mpc-multi-party-computation
 Dynamic.xyz. (2022, October 11). _An overview of Multi-Signature and Multi-Party Computation_. https://www.dynamic.xyz/blog/the-evolution-of-multi-signature-and-multi-party-computation
 Dynamic.xyz. (n.d.). _A Deep Dive into TSS-MPC: Dynamic's Focus on Security and ..._. https://www.dynamic.xyz/blog/a-deep-dive-into-tss-mpc
 Ethereum.org. (n.d.). _Transactions_. https://ethereum.org/developers/docs/transactions/
 Ethereum.org. (n.d.). _Merkle Patricia Trie_. https://ethereum.org/developers/docs/data-structures-and-encoding/patricia-merkle-trie/
 Fireblocks. (n.d.). _What Is MPC (Multi-Party Computation)?_. https://fireblocks.com/what-is-mpc/
 Fireblocks. (n.d.). _Fireblocks' Multi-Layer Digital Asset Security_. https://fireblocks.com/report/fireblocks-multi-layer-digital-asset-security/
 Fireblocks. (n.d.). _Navigating the Complexities of Transaction Approval and ..._. https://fireblocks.com/blog/navigating-the-complexities-of-transaction-approval-and-validation-flows/
 Gennaro, R., & Goldfeder, S. (2018, October 8). _Fast Multiparty Threshold ECDSA with Fast Trustless Setup_. https://www.semanticscholar.org/paper/3321190a9c8404f9598c38326a174078d27e6780
 Goldfeder, S., Gennaro, R., & Lindell, Y. (2015). _Securing Bitcoin wallets via a new DSA / ECDSA threshold signature scheme_. https://www.semanticscholar.org/paper/8b9b7e1fb101a899b0309ec508ac5912787cc12d
 Least Authority. (n.d.). _Ensuring the Secure Use of the FROST Protocol_. https://leastauthority.com/blog/ensuring-the-secure-use-of-the-frost-protocol/
 Ledger. (n.d.). _An Offline Key is the Only Key: How Ledger Wallets Store Private ..._. https://www.ledger.com/academy/topics/ledgersolutions/an-offline-key-is-the-only-key-how-ledger-wallets-store-private-keys-offline
 Lightspark. (n.d.). _Understanding the Threshold Signature Scheme_. https://lightspark.com/glossary/threshold-signature-scheme
 Loopring Protocol. (2023, May 25). _Loopring Smart Wallet w/ Social Recovery \u2014 Your Ultimate Crypto ..._. https://medium.com/loopring-protocol/loopring-smart-wallet-w-social-recovery-your-ultimate-crypto-security-guide-8f435da646ae
 Metamask. (n.d.). _Ethereum transaction types | MetaMask developer documentation_. https://docs.metamask.io/services/concepts/transaction-types/
 Metamask. (n.d.). _Introducing MetaMask social login_. https://metamask.io/news/introducing-metamask-social-login
 Metamask. (n.d.). _Account Abstraction: Past, Present, Future_. https://metamask.io/news/account-abstraction-past-present-future
 Mmasmoudi. (2023, June 21). _An overview of MPC, TSS and MPC-TSS wallets | Medium_. https://mmasmoudi.medium.com/an-overview-of-multi-party-computation-mpc-threshold-signatures-tss-and-mpc-tss-wallets-4253adacd1b2
 Nguyen, H. G., & Nguyen, A. K. (2023). _New Key Extraction Attacks on Threshold ECDSA Implementations_. https://i.blackhat.com/BH-US-23/Presentations/US-23-Nguyen-TSSHOCK-Breaking-MPC-Wallets-wp.pdf
 NCC Group. (n.d.). _Public Report \u2013 Zcash FROST Security Assessment_. https://www.nccgroup.com/research-blog/public-report-zcash-frost-security-assessment/
 Odaily. (n.d.). _\u89e3\u6790\u4f1a\u8bdd\u5bc6\u94a5\uff1aWeb3\u7248\u201c\u514d\u5bc6\u652f\u4ed8\u201d_. https://www.odaily.news/post/5181328
 OpenZeppelin. (n.d.). _Account Abstraction's Impact on Security and User Experience_. https://www.openzeppelin.com/news/account-abstractions-impact-on-security-and-user-experience
 QuickNode. (n.d.). _How to Send an EIP-1559 Transaction | QuickNode Guides_. https://www.quicknode.com/guides/ethereum-development/transactions/how-to-send-an-eip-1559-transaction
 Schoenwald, D. (2025, February 5). _The Ultimate Guide to WebAuthn & FIDO2 - 0hlov3_. https://schoenwald.aero/posts/2025-02-5_the-ultimate-guide-to-webauthn-fido2/
 Semanticscholar. (n.d.). _Fast Multiparty Threshold ECDSA with Fast Trustless Setup_. https://www.semanticscholar.org/paper/3321190a9c8404f9598c38326a174078d27e6780
 Semanticscholar. (n.d.). _A Survey of ECDSA Threshold Signing_. https://www.semanticscholar.org/paper/6bc96ca829a4759905b521a530b39e93a13c4401
 Semanticscholar. (n.d.). _Asynchronous Threshold ECDSA With Batch Processing_. https://www.semanticscholar.org/paper/03d92f610277ef266d231bb24daa7d6329953bf0
 Semanticscholar. (n.d.). _Threshold ECDSA in Three Rounds_. https://www.semanticscholar.org/paper/b6cd4e7e542e3ca77d79ba63f185281fbe141d82
 Semanticscholar. (n.d.). _UC Non-Interactive, Proactive, Threshold ECDSA_. https://www.semanticscholar.org/paper/afa125a64a723eb7d7fbf02f9c1d6a426ab7e5b8
 Semanticscholar. (n.d.). _Elliptic Curve Cryptography in Blockchain Technology_. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4033934
 Semanticscholar. (n.d.). _Breaking Down ECDSA and Ed25519 Digital Signatures_. https://billatnapier.medium.com/breaking-down-ecdsa-and-ed25519-digital-signatures-0704ddb549ad
 Semanticscholar. (n.d.). _The Provable Security of Ed25519: Theory and Practice_. https://www.semanticscholar.org/paper/cd7cdb27040cad5ab5eaf8c4b4b6ecae18484064
 Semanticscholar. (n.d.). _Design and Implementation of an Ed25519 coprocessor_. https://www.semanticscholar.org/paper/6fbc7d953d0569b1e9a900b69e909029d5a617e6
 Semanticscholar. (n.d.). _What is Merkle Tree? Blockchain hashing, proofs, and Web3 uses_. https://www.cube.exchange/what-is/merkle-tree
 Semanticscholar. (n.d.). _Understanding Merkle Trees: Enhancing Blockchain Efficiency and ..._. https://www.investopedia.com/terms/m/merkle-tree.asp
 Semanticscholar. (n.d.). _Merkle Tree in Crypto: What it is and How it Works?_ https://atomicwallet.io/academy/articles/what-is-merkle-tree
 Semanticscholar. (n.d.). _What Is a Merkle Proof? - NMKR_. https://www.nmkr.io/glossary/merkle-proof
 Semanticscholar. (n.d.). _Merkle Root | A Fingerprint for the Transactions in a Block_. https://learnmeabitcoin.com/technical/block/merkle-root/
 Semanticscholar. (n.d.). _VMware Cloud on AWS: A Guide for Cloud Architects_. https://www.semanticscholar.org/paper/541f5a50787e97491746c87342d8d8cecf2c8e37
 Semanticscholar. (n.d.). _Optimizing Web Performance and Computational Efficiency: A Deep Dive into WebAssembly's Technical Advancements and Real-World Applications_. https://www.researchgate.net/profile/Son-Nguyen-386/publication/389517325_Optimizing_Web_Performance_and_Computational_Efficiency_A_Deep_Dive_into_WebAssembly's_Technical_Advancements_and_Real-World_Applications/links/67c62ce1207c0c20faa03019/Optimizing-Web-Performance-and-Computational-Efficiency-A-Deep-Dive-into-WebAssemblys-Technical-Advancements-and-Real-World-Applications.pdf
 Semanticscholar. (n.d.). _Performance Benchmarking of Cryptographic Algorithms in ..._. https://www.researchgate.net/publication/394876239_Performance_Benchmarking_of_Cryptographic_Algorithms_in_JCA_for_Messaging_Apps
 Semanticscholar. (n.d.). _Performance scaling of cryptography operations in ..._. https://www.researchgate.net/publication/228949776_Performance_scaling_of_cryptography_operations_in_servers_and_mobile_clients
 Semanticscholar. (n.d.). _On Possible Cryptographic Optimization of Mobile Healthcare Application_. https://www.semanticscholar.org/paper/0567dee7dd8583b08ba67ff5ebe21c4dda2a6581
 Semanticscholar. (n.d.). _The impact of mobile processor cryptographic acceleration on data transfer_. https://www.semanticscholar.org/paper/6be54d9cb7e09885a540debf08130864559a1217
 Semanticscholar. (n.d.). _Security and Network Performance Evaluation of KK' Cryptographic Technique in Mobile Adhoc Networks_. https://www.semanticscholar.org/paper/e89ea540fa181fc73b4420a7622da80ef8828beb
 Semanticscholar. (n.d.). _Linux BYTEmark Benchmarks: A Performance Comparison of Embedded Mobile Processors_. https://www.semanticscholar.org/paper/f8a48372d8f37b44f2408f4f15325e248a31ad82
 Semanticscholar. (n.d.). _Performance analysis of cryptographic protocols on handheld devices_. https://www.semanticscholar.org/paper/430ed3ce280eb4c75953503f7ddb2f6efd5137fe
 Semanticscholar. (n.d.). _WebAuthn as part of FIDO2 is a new standard for two-factor and even password-less user authentication to web-services. Leading browsers, like Google Chrome, Microsoft Edge, and Mozilla Firefox, support the WebAuthn API. Unfortunately, the availability of hardware authenticators that support FIDO2 authentication is still focused heavily on desktop computers, while for mobile devices, only a limited choice of suitable authenticators is available to users (few roaming authenticators with wireless connectivity and even fewer built-in platform authenticators on mobile devices). This creates a void for users, in particular users of older device generations that lack platform authenticators and the right connectivity, to authenticate themselves with WebAuthn to web-services. In this poster, we present the idea ofsimFIDO, a FIDO2 setup using a recently developed simTPM as (platform) authenticator for mobile devices and even as roaming authenticator offered by mobile devices to connected computers. The move-ability property of the key storage of simTPM makes the users' lives easier for credential portability between devices. In particular, a seamless integration of simTPM with non-mobile devices through phones will help to create a kind of universal authentication setup using FIDO2. Although we present the concrete design and implementation of a SIM card-based FIDO2 authenticator, we hope this poster will contribute to the discussion about how and in which form hardware authenticators can be made available to users._. https://www.semanticscholar.org/paper/7ee68251acb59237fe215e88a3d0a2d4dd4a75c5
 Semanticscholar. (n.d.). _"It's Stored, Hopefully, on an Encrypted Server": Mitigating Users' Misconceptions About FIDO2 Biometric WebAuthn_. https://www.semanticscholar.org/paper/cecb164c2b22e353a8de94af6314461204a57d15
 Semanticscholar. (n.d.). _Technical Report on a Virtual CTAP2 WebAuthn Authenticator_. https://www.semanticscholar.org/paper/fbeff336eee4f3b34d7ed9b0e49793825cc281b6
 Semanticscholar. (n.d.). _Hardware TOTP tokens with time synchronization_. https://www.semanticscholar.org/paper/1f228578605d6dda3adf484bd38872d7769dc187
 Semanticscholar. (n.d.). _A Social Wallet Scheme with Robust Private Key Recovery_. https://www.semanticscholar.org/paper/7debd53fd6ba124275644443a9928b185ebbcb7b
 StarkNet. (n.d.). _Account Abstraction: Your Crypto Advantage_. https://www.starknet.io/blog/account-abstraction/
 Utila. (2024, July 15). _Multi-Sig vs MPC Wallets: A Guide for Institutions (2024) - Utila_. https://utila.io/blog/multi-sig-vs-mpc-wallets-a-guide-for-institutions/
 Utila. (n.d.). _Understanding Token Approvals on EVM & Tron - Utila_. https://utila.io/blog/understanding-token-approvals-on-evm-tron/
 Vultisig. (n.d.). _How GG20 works - Vultisig_. https://docs.vultisig.com/threshold-signature-scheme/threshold-signature-schemes-used-by-vultisig/how-it-works
 Web3Auth. (n.d.). _Introducing Ed25519 in Web3Auth\u2019s MPC: Secure Signing ..._. https://blog.web3auth.io/introducing-ed25519-in-web3auths-mpc-secure-signing-for-dapps-and-wallets/
 Yellow.com. (2025, September 1). _Social Recovery Wallets: Can They Solve the Seed Phrase Problem ..._. https://yellow.com/learn/social-recovery-wallets-can-they-solve-the-seed-phrase-problem-complete-2025-guide
 Yellow.com. (n.d.). _13 Best Multi-Chain Web3 Wallets: Ultimate Guide - Yellow.com_. https://yellow.com/en-US/learn/13-best-multi-chain-web3-wallets-ultimate-guide
 Zcash Foundation. (n.d.). _The State of FROST for Zcash_. https://zfnd.org/the-state-of-frost-for-zcash/
 Zengo. (n.d.). _Multi-party ECDSA Security Audit_. https://zengo.com/audit/audit-kudelski_october2019.pdf

**Chinese Sources**
 \u5e01\u5b89. (n.d.). _\u4e00\u6587\u8bfb\u61c2\u65b0\u4e0a\u7ebf\u7684\u300cERC-4337\u300d\uff1a\u4e0d\u518d\u9700\u8981\u52a9\u8bb0\u8bcd\uff0cWeb3\u5927\u89c4\u6a21 ..._. https://www.binance.com/zh-CN/square/post/313179
 \u5e01\u5b89. (n.d.). _\u4e3a\u4ec0\u4e48\u7eb3\u74e6\u5c14\u8bf4\uff1aZCash\u662f\u9488\u5bf9\u6bd4\u7279\u5e01\u9690\u79c1\u7684\u4fdd\u9669\uff1f_. https://www.binance.com/zh-CN/square/post/31920323721042
 \u94fe\u8282\u70b9. (n.d.). _\u96f6\u77e5\u8bc6\u8bc1\u660e\uff1a\u4ee5\u592a\u574a\u7684\u672a\u6765| \u767b\u94fe\u793e\u533a| \u533a\u5757\u94fe\u6280\u672f\u793e\u533a_. https://learnblockchain.cn/article/7921
 \u77e5\u4e4e\u4e13\u680f. (n.d.). _\u62bd\u8c61\u8d26\u6237\u5b66\u4e60\u7b14\u8bb0\uff081\uff09\uff1a\u4ece4337\u51fa\u53d1_. https://zhuanlan.zhihu.com/p/667211672
 \u7a00\u571f\u6398\u91d1. (n.d.). _\u6784\u5efa\u5bc6\u94a5\u7ba1\u7406\u63a7\u5236\u5668\uff08KeyringController\uff09keyring-controller - \u7a00\u571f\u6398\u91d1_. https://juejin.cn/post/7537641651209977908
 \u767b\u94fe\u793e\u533a. (n.d.). _\u4ec0\u4e48\u662f\u96f6\u77e5\u8bc6\u8bc1\u660e\uff0c\u5982\u4f55\u5b88\u62a4Web3\u9690\u79c1\uff1f|Tokenview - \u767b\u94fe\u793e\u533a_. https://learnblockchain.cn/article/5233
 \u767b\u94fe\u793e\u533a. (n.d.). _\u96f6\u77e5\u8bc6\u8bc1\u660e\uff1a\u5e94\u7528\u548c\u5177\u4f53\u7528\u4f8b - \u767b\u94fe\u793e\u533a_. https://learnblockchain.cn/article/5786
 \u77e5\u4e4e\u4e13\u680f. (n.d.). _\u96f6\u77e5\u8bc6\u8bc1\u660e\u4e0e\u9690\u79c1\u589e\u5f3a - \u77e5\u4e4e\u4e13\u680f_. https://zhuanlan.zhihu.com/p/1950848293023232716
 \u767b\u94fe\u793e\u533a. (n.d.). _5\u5206\u949f\u4e0a\u624b\uff01libsodium\u8de8\u5e73\u53f0\u52a0\u5bc6\u5f00\u53d1\u5b9e\u6218\u6307\u5357 - CSDN\u535a\u5ba2_. https://blog.csdn.net/gitblog_01124/article/details/151470763
 \u6613\u6e90\u6613\u5f69. (n.d.). _\u6df1\u5165\u6d45\u51faLibsodium\u52a0\u5bc6\u5e93\uff1a\u5b89\u5168\u7f16\u7a0b\u7684\u5229\u5668 - \u6613\u6e90\u6613\u5f69_. https://www.yicaiai.com/news/article/66ece8654ddd79f11a1ee24c

**Other Language Sources**
 fastbull. (n.d.). _\u9690\u79c1\u5e01\u5927\u6da8\u80cc\u540e\uff1a\u6619\u82b1\u4e00\u73b0\u8fd8\u662f\u66d9\u5149\u6765\u4e34\uff1f_. https://m.fastbull.com/cn/news-detail/4352483_1
 FX168\u8d22\u7ecf. (n.d.). _\u96b1\u79c1\u5e63\u5927\u6f32\u80cc\u5f8c\uff1a\u66c7\u82b1\u4e00\u73fe\u9084\u662f\u66d9\u5149\u4f86\u81e8\uff1f_. https://news.fx168news.com/cooperate/2511/7388749.shtml
 \u9245\u4ea8\u7db2. (n.d.). _Zcash\u66b4\u6f32700%\u80cc\u5f8c\uff1a\u96b1\u79c1\u6558\u4e8b\u5982\u4f55\u91cd\u71c3\u52a0\u5bc6\u5e02\u5834_. https://m.cnyes.com/news/id/6217769
 Mr.Market\u5e02\u5834\u5148\u751f. (n.d.). _\u96f6\u77e5\u8b58\u8b49\u660e\u539f\u7406\uff1f\u7279\u6027\u8207\u985e\u578b\u4ecb\u7d39/\u5e38\u898b\u61c9\u7528/\u5132\u5099\u8b49\u660e\u67e5\u8a62\u7bc4\u4f8b_. https://rich01.com/zero-knowledge-proof-zkp/
 TP\u94b1\u5305\u5bc6\u94a5\u4e22\u5931\u540e\u5982\u4f55\u627e\u56de\u4e0e\u533a\u5757\u94fe\u5b89\u5168\u4e0e\u672a\u6765\u5c55\u671b. (n.d.). _TP\u94b1\u5305\u5bc6\u94a5\u4e22\u5931\u540e\u5982\u4f55\u627e\u56de\u4e0e\u533a\u5757\u94fe\u5b89\u5168\u4e0e\u672a\u6765\u5c55\u671b_. https://facegenmedia.com/news/lanmu1/3648.html
 Web3. (n.d.). _Web 3 \u534f\u8bae\u6808\u4e0e\u7528\u6237\u4ea4\u4e92\u5c42 - \u77e5\u4e4e\u4e13\u680f_. https://zhuanlan.zhihu.com/p/1949407841761883232
 \u9ec4\u5efa\u6d9b, & \u5218\u54f2. (2020). \u6297\u8d27\u5e01\u5931\u6548\u7684\u533a\u5757\u94fe\u94b1\u5305\u4fdd\u62a4\u534f\u8bae\u7814\u7a76. _\u8ba1\u7b97\u673a\u5de5\u7a0b\u4e0e\u5e94\u7528_, 56(22), 253-261. https://www.semanticscholar.org/paper/4e34e569c7662c148c34ee27cdf39ce8dfc30ba1
 blocktempo. (n.d.). _\u79d1\u666e\uff5c\u667a\u80fd\u5408\u7d04\u9322\u5305\u4ec0\u9ebc\u6642\u5019\u80fd\u666e\u53ca\uff1f\u4e00\u6587\u770b\u61c2ERC-4337_. https://www.blocktempo.com/erc-4337-wallet-building-and-principles/
 blocktempo. (n.d.). _\u79d1\u666e\uff5czk-SNARKs\u662f\u4ec0\u9ebc\uff1fV\u795e\u5b9a\u8abf\u96f6\u77e5\u8b58\u8b49\u660e\u672a\u4f86\u5341\u5e74\u300c\u975e\u5e38\u91cd\u8981\u300d_. https://www.blocktempo.com/zk-snarks-will-be-important-as-the-blockchain/
 \u5340\u584a\u5ba2. (n.d.). _\u4ee5\u592a\u574a\u9322\u5305\u7684\u8b8a\u9769\uff1a\u5e33\u6236\u62bd\u8c61\u8207ERC-4337 \u7684\u6a5f\u9047\u8207\u6311\u6230 - \u5340\u584a\u5ba2_. https://blockcast.it/2023/01/14/how-erc-4337-account-abstraction-will-evolve-wallets/

---

## Validation Report
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:12 C:5 L:6 A:93 Q:15 (F:1 I:8 A:6) | PASS |
| Citation coverage | 100% \u22651, 100% \u22652 | PASS |
| Language dist | EN:71.0% ZH:29.0% Other:0% | PASS |
| Recency | 97% last 3yr | PASS |
| Source diversity | 3 types, max 10% | PASS |
| Links | 93/93 accessible | PASS |
| Cross-refs | 93/93 resolved | PASS |
| Word counts | 5/5 compliant | PASS |
| Key Insights | 5/5 concrete | PASS |
| Per-topic mins | 4/4 topics meet | PASS |
```

Sources: 
[1] The Elliptic Curve Digital Signature Algorithm (ECDSA), https://www.semanticscholar.org/paper/65ecd5eaec484201c701c4a1508f8d2132c125f0
[2] Fast Multiparty Threshold ECDSA with Fast Trustless Setup, https://www.semanticscholar.org/paper/3321190a9c8404f9598c38326a174078d27e6780
[3] Blockchain-envisioned provably secure multivariate identity-based multi-signature scheme for Internet of Vehicles environment, https://ieeexplore.ieee.org/abstract/document/9779932/
[4] An overview of Multi-Signature and Multi-Party Computation, https://www.dynamic.xyz/blog/the-evolution-of-multi-signature-and-multi-party-computation
[5] How many FIDO protocols are needed? Analysing the technology, security and compliance, https://dl.acm.org/doi/abs/10.1145/3654661
[6] Fido Core for Eid-Wallets, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5009534
[7] SoK: Web Authentication in the Age of End-to-End Encryption, https://arxiv.org/abs/2406.18226
[8] Measuring adoption of phishing-resistant authentication methods on the web, https://hdms.bsz-bw.de/frontdoor/index/index/docId/7038
[9] Gaza Wallet: A Simple and Efficient Blockchain Application, https://www.semanticscholar.org/paper/5f0d064a07a7b33e3bcf834c6a1967a95ea431e6
[10] Cryptography and MPC in the Coinbase Prime Web3 Wallet, https://www.semanticscholar.org/paper/580a4e0eff2c0fed830638cdd3cb2576906def8f
[11] Modernizing key management in the transition to public cloud, https://aaltodoc.aalto.fi/items/de0916a9-cb70-4a8a-85d0-22b3e7b50eb5
[12] Securing digital identities: from the deployment to the analysis of a PKI ecosystem with virtual HSMs leveraging open-source tools, https://webthesis.biblio.polito.it/31741/
[13] Securing Medical Records Using Blockchain with Cryptography, Encryption, and Zero-Knowledge Rollups, https://norma.ncirl.ie/id/eprint/8049
[14] Implementing Blockchain Technology for Secure Data Transactions in Cloud Computing Environments Challenges and Solutions, https://www.itm-conferences.org/articles/itmconf/abs/2025/07/itmconf_icsice2025_02001/itmconf_icsice2025_02001.html
[15] HSM and TPM Failures in Cloud: A Real-World Taxonomy and Emerging Defenses, https://arxiv.org/abs/2507.17655
[16] A panoramic survey of the advanced encryption standard: from architecture to security analysis, key management, real-world applications, and post-quantum�\u2026, https://link.springer.com/article/10.1007/s10207-025-01116-x
[17] Cryptographic Wallet Security and Key Management in Blockchain Financial Systems: A Systematic Literature Review, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5363844
[18] Incentive-Compatible and Privacy-Preserving Data Analytics System enabled by Blockchain and Multiparty Computation, https://webthesis.biblio.polito.it/10921/
[19] Ethereum Blockchain Wallets: A Kotlin-based Implementation Perspective, https://www.semanticscholar.org/paper/433e88a34ab690e0aa237c93fd488275b5ec42c1
[20] Decentralized key management for digital identity wallets, https://link.springer.com/chapter/10.1007/978-3-031-49593-9_3
[21] Xythum Labs, https://www.xythum.io/static/media/xythum-whitepaper.16a75cff20e38b83b11f.pdf
[22] Addressing Centralization, Security and Performance Issues in Real-World Blockchain Systems, https://s-space.snu.ac.kr/bitstream/10371/196483/1/000000178088.pdf
[23] Ethereum Blockchain Wallets, https://www.semanticscholar.org/paper/44eefa2e085c2f8f7ef57dbb62e65d6cba36e6f3
[24] Blockchain Technology in Ethereum Wallets, https://www.semanticscholar.org/paper/ceb6633a958b3ee679ec5770255bd2cfe8e5b04a
[25] Social Recovery Wallets: Can They Solve the Seed Phrase Problem ..., https://yellow.com/learn/social-recovery-wallets-can-they-solve-the-seed-phrase-problem-complete-2025-guide
[26] Threshold Signature Schemes in blockchain: an introduction, https://www.blockstrata.co/threshold-signature-schemes-and-mpc-in-cryptocurrency-an-introduction/
[27] icon-ethereum-111�111, https://www.semanticscholar.org/paper/05a254449cacbf0a38ffc0ccb28da8da5422d201
[28] Proxy multisignature scheme with (t, m) threshold shared verification, https://www.semanticscholar.org/paper/475978967a109ce5ab063f8c4c00daad8b21fd90
[29] Security Analysis of Some Threshold Signature Schemes and Multi-signature Schemes, https://www.semanticscholar.org/paper/fe201aaa18dfad6a9ff3503883536e83f1e860c3
[30] ETH Focus Projects, https://www.semanticscholar.org/paper/0f01846d15c1ba27360886f7e8f7fad81813cdcc
[31] An efficient multi-signature scheme for blockchain, https://iacr.steepath.eu/2023/078-AnEfficientMultiSignatureSchemeforBlockchain.pdf
[32] What is a Social Recovery Wallet? - Gate.com, https://www.gate.com/learn/articles/what-is-a-social-recovery-wallet/676
[33] E-Voting using Ethereum Blockchain, https://www.semanticscholar.org/paper/b0d3b93795079f96999bf69bc095445dae8af38e
[34] Digital inheritance in Web3: a case study of soulbound tokens and the social recovery pallet within the Polkadot and Kusama ecosystems, https://philpapers.org/rec/GOLDII-4
[35] Smart contract-based social recovery wallet management scheme for digital assets, https://dl.acm.org/doi/abs/10.1145/3564746.3587016
[36] Multi-Sig vs MPC Wallets: A Guide for Institutions (2024) - Utila, https://utila.io/blog/multi-sig-vs-mpc-wallets-a-guide-for-institutions/
[37] Web3 Recovery Mechanisms and User Preferences, https://eprint.iacr.org/2025/1687
[38] Some Applications of Threshold Signature Schemes to Distributed Protocols, https://www.semanticscholar.org/paper/a11f64ba8ad8ca52af00ed3a33ba54c187a998a0
[39] Loopring Smart Wallet w/ Social Recovery \u2014 Your Ultimate Crypto ..., https://medium.com/loopring-protocol/loopring-smart-wallet-w-social-recovery-your-ultimate-crypto-security-guide-8f435da646ae
[40] Intro to Social Recovery Wallets: Safe, Argent, and ERC-4337, https://university.mitosis.org/intro-to-social-recovery-wallets-safe-argent-and-erc-4337/
[41] Efficient, Scalable Threshold ML-DSA Signatures: An MPC Approach, https://eprint.iacr.org/2025/1163
[42] A Practical Recovery Mechanism for Blockchain Hardware Wallets, https://ieeexplore.ieee.org/abstract/document/10752638/
[43] A Composability Analysis Framework for Web3 Wallet Recovery Mechanisms, https://ieeexplore.ieee.org/abstract/document/11023254/
[44] Secure and Efficient Multi-Signature Schemes for Fabric: An Enterprise Blockchain Platform, https://www.semanticscholar.org/paper/0329334cad862b79881ba458b81e206454af946a
[45] Blockchain Applications Presentation Commentry, https://www.semanticscholar.org/paper/bbafc04d3685c513db1c389306231c317227f58d
[46] Binance tss-lib's 9-Round Threshold ECDSA - CertiK, https://www.certik.com/resources/blog/threshold-cryptography-iii-binance-tss-libs-9-round-threshold-ecdsa
[47] A Comparative Examination of Some Threshold ECDSA Protocols in ..., https://medium.com/@oznurmut/a-comparative-examination-of-some-threshold-ecdsa-protocols-e7af8cad1992
[48] [PDF] Robustness for Dishonest Majority in Threshold ECDSA, https://csrc.nist.gov/CSRC/media/Events/mpts2020/slides/mpts2020-3c1-brief-damian.pdf
[49] ZenGo-X/multi-party-ecdsa: Rust implementation of {t,n} - GitHub, https://github.com/ZenGo-X/multi-party-ecdsa
[50] 2-of-2 threshold ECDSA signing algorithm using GG20 with Kryptology, https://asecuritysite.com/signatures/sss_gg02
[51] Any t-of-n threshold ECDSA signing algorithm using GG20 with ..., https://asecuritysite.com/kryptology/sss_gg03
[52] How GG20 works - Vultisig, https://docs.vultisig.com/threshold-signature-scheme/threshold-signature-schemes-used-by-vultisig/how-it-works
[53] Two-Round Threshold Schnorr Signatures with FROST, https://datatracker.ietf.org/doc/draft-irtf-cfrg-frost/11/
[54] The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol ..., https://www.rfc-editor.org/rfc/rfc9591.html
[55] Stronger Security for Non-Interactive Threshold Signatures: BLS and ..., https://eprint.iacr.org/2022/833
[56] ICE-FROST: Identifiable Cheating Entity FROST Signature Protocol, https://toposware.com/blog/ice-frost/
[57] [PDF] Dynamic-FROST: Schnorr Threshold Signatures with a Flexible ..., https://eprint.iacr.org/2024/896.pdf
[58] A Comprehensive Survey of Threshold Digital Signatures - arXiv, https://arxiv.org/html/2311.05514v2
[59] Real Threshold ECDSA, https://www.semanticscholar.org/paper/a1b3f39499172f911e9aacca9e75985e97e17bc1
[60] Asynchronous Threshold ECDSA With Batch Processing, https://www.semanticscholar.org/paper/03d92f610277ef266d231bb24daa7d6329953bf0
[61] Fast threshold ECDSA with honest majority, https://www.semanticscholar.org/paper/855cc15be88ca034bd9091d4b4fa4de7a017e002
[62] OptiVersa-ECDSA: Fast Threshold-ECDSA with Cheater Identification for Blockchains, https://ieeexplore.ieee.org/abstract/document/11176970/
[63] Fast two-party threshold ECDSA with proactive security, https://dl.acm.org/doi/abs/10.1145/3658644.3670387
[64] BLS Signature Scheme, https://www.semanticscholar.org/paper/1d85ea6db67e9a3da90efc40c7fde9513124d778
[65] [PDF] Fast Multiparty Threshold ECDSA with Fast Trustless Setup, https://eprint.iacr.org/2019/114.pdf
[66] Introducing The 2-of-3 Threshold Signature Protocol by GG18, https://eigenlab.medium.com/introducing-the-2-of-3-threshold-signature-protocol-by-gg18-7a6c8f2da893
[67] [PDF] A Note on the Security of GG18 - Fireblocks, https://info.fireblocks.com/hubfs/A_Note_on_the_Security_of_GG.pdf
[68] New Paper: On the Adaptive Security of FROST, https://writing.chelseakomlo.com/new-paper-on-the-adaptive-security-of-frost/
[69] RFC 9591: The Flexible Round-Optimized Schnorr Threshold ..., https://dl.acm.org/doi/10.17487/RFC9591
[70] [PDF] FROST: Flexible Round-Optimized Schnorr Threshold signatures ..., https://crysp.uwaterloo.ca/software/frost/frost-extabs.pdf
[71] Flexible Round-Optimized Schnorr Threshold Signatures (FROST), https://developer.blockchaincommons.com/frost/
[72] Threshold ECDSA in Three Rounds, https://www.semanticscholar.org/paper/b6cd4e7e542e3ca77d79ba63f185281fbe141d82
[73] Elliptical Curve Digital Signatures Algorithm, https://www.semanticscholar.org/paper/1959b591d118da65c8ef28a336b3ff13768a1921
[74] One Round Threshold ECDSA Without Roll Call, https://www.semanticscholar.org/paper/0551abbc0f074c2f48d29db29db441be5fe7f9f2
[75] A Survey of ECDSA Threshold Signing, https://www.semanticscholar.org/paper/6bc96ca829a4759905b521a530b39e93a13c4401
[76] One-Up Problem for (EC)DSA, https://www.semanticscholar.org/paper/b9b034ed97f986021c3ce6e7a45fa7d76c23c566
[77] Bandwidth-Efficient Zero-Knowledge Proofs For Threshold ECDSA, https://www.semanticscholar.org/paper/e81c45a6d69a230f84d4d8ff79043374aec9f3c4
[78] Low-Bandwidth Threshold ECDSA via Pseudorandom Correlation Generators, https://www.semanticscholar.org/paper/35911c94b3a7cf4ba3ecf77bd37389d7f9b571ac
[79] UC Non-Interactive, Proactive, Threshold ECDSA, https://www.semanticscholar.org/paper/afa125a64a723eb7d7fbf02f9c1d6a426ab7e5b8
[80] Elliptic curve threshold signature scheme for blockchain, https://www.semanticscholar.org/paper/b769ba2d2b988c1f27082b839bf265513da0d1ec
[81] Weighted threshold ECDSA for securing bitcoin wallet, https://www.semanticscholar.org/paper/534b5c4bb1fa283cf223077b627c855fb7b7f3ec
[82] Fast 2-out-of-n ecdsa threshold signature, https://ieeexplore.ieee.org/abstract/document/10491665/
[83] Threshold ECDSA in Two Rounds, https://eprint.iacr.org/2025/1696
[84] The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures, https://www.semanticscholar.org/paper/750a0f764c162f094526d9ee510ccafa02506894
[85] Identifiable Cheating Entity Flexible Round-Optimized Schnorr Threshold (ICE FROST) Signature Protocol, https://www.semanticscholar.org/paper/fb81d027568c5e45ec948a7f2f495c247ecca534
[86] Re-Randomized FROST, https://www.semanticscholar.org/paper/75304bc4956436a52d8895e78c0e3e095c0ccf14
[87] Abstract of Paper on the Frost of 1895 in Scotland, https://www.semanticscholar.org/paper/ba0a81499da3a585fd098134338c990192bf1fa2
[88] Safeheron Releases World's First C++ Based MPC Protocol Library, https://safeheron.com/blog/safeheron-releases-first-cpp-mpc-protocol-library/
[89] Gitcoin Digest #17 2023 - News and Community, https://gov.gitcoin.co/t/gitcoin-digest-17-2023/16437
[90] [PDF] Threshold ECDSA Performance Analysis - IS MUNI, https://is.muni.cz/th/fuwu0/thesis.pdf
[91] [PDF] Multi-party ECDSA Security Audit - Zengo, https://zengo.com/audit/audit-kudelski_october2019.pdf
[92] TSSHOCK: New Key Extraction Attacks on Threshold Signature ..., https://verichains.io/tsshock/
[93] [PDF] A Survey of ECDSA Threshold Signing - Cryptology ePrint Archive, https://eprint.iacr.org/2020/1390.pdf
[94] Produced by SlowMist: Common-Cryptographic-Risks-in-Blockchain ..., https://slowmist.medium.com/produced-by-slowmist-common-cryptographic-risks-in-blockchain-applications-4a8b36411441
[95] [PDF] Security Audit Report | MPC-ECDSA Algorithm | Safeheron, https://leastauthority.com/wp-content/uploads/2024/06/Annotation_Version_Safeheron_MPC_Algorithm_Updated_Final_Audit_Report_Least_Authority.pdf
[96] Releases � bnb-chain/tss-lib - GitHub, https://github.com/bnb-chain/tss-lib/releases
[97] Ensuring the Secure Use of the FROST Protocol, https://leastauthority.com/blog/ensuring-the-secure-use-of-the-frost-protocol/
[98] Public Report \u2013 Zcash FROST Security Assessment, https://www.nccgroup.com/research-blog/public-report-zcash-frost-security-assessment/
[99] A Chilling Revelation: A Look into FROST Signatures., https://sqrr.xyz/FrostRecap20Sep2023.php
[100] FROST: Flexible Round-Optimized Schnorr Threshold ..., https://medium.com/the-coinbase-blog/frost-flexible-round-optimized-schnorr-threshold-signatures-b2e950164ee1
[101] Multisig for Zcash with FROST - Community Grants, https://forum.zcashcommunity.com/t/multisig-for-zcash-with-frost/38722
[102] Unidentifiability in Decentralized FROST Implementation, https://www.certik.com/resources/blog/threshold-cryptography-ii-unidentifiability-in-decentralized-frost
[103] The State of FROST for Zcash, https://zfnd.org/the-state-of-frost-for-zcash/
[104] ZcashFoundation/frost, https://github.com/ZcashFoundation/frost
[105] Audit of ING's Threshold ECDSA Library - Kudelski Security, https://kudelskisecurity.com/research/audit-of-ings-threshold-ecdsa-library---and-a-dangerous-vulnerability-in-existing-gennaro-goldfeder18-implementations
[106] Unstoppable Wallets: Chain-assisted Threshold ECDSA and its ..., https://dl.acm.org/doi/10.1145/3634737.3637657
[107] Breaking Oblivious Transfer-based Threshold ECDSA - Fordefi Blog, https://blog.fordefi.com/devious-transfer-breaking-oblivious-transfer-based-threshold-ecdsa
[108] Robust Thresholds ECDSA Signatures for Identifying Misbehaving ..., https://www.circle.com/blog/robust-thresholds-ecdsa-signatures-for-identifying-misbehaving-signers-in-real-time
[109] [PDF] New Key Extraction Attacks on Threshold ECDSA Implementations, https://i.blackhat.com/BH-US-23/Presentations/US-23-Nguyen-TSSHOCK-Breaking-MPC-Wallets-wp.pdf
[110] [PDF] Attacking Threshold Wallets - Cryptology ePrint Archive, https://eprint.iacr.org/2020/1052.pdf
[111] What we learned reviewing one of the first DKLs23 libraries from ..., https://blog.trailofbits.com/2025/06/10/what-we-learned-reviewing-one-of-the-first-dkls23-libraries-from-silence-laboratories/
[112] THE SECURITY AUDIT, https://www.semanticscholar.org/paper/d6af6bab2fba8a9577cca27620d2d697b52ff7b1
[113] Optimizing WeBarangay: A Comprehensive Performance and Security Audit, https://www.semanticscholar.org/paper/2fa29100ae8db338023bc7b27978465a1a31d52d
[114] Towards effective performance auditing, https://www.semanticscholar.org/paper/d8ed3bf9b162b0685e7b3b0d6d272b3e631e48b7
[115] The Database Security Based on the Security Audit, https://www.semanticscholar.org/paper/bb15615d53ae09ab6c7ae4d1f92cf73f18656b31
[116] The Application Audit, https://www.semanticscholar.org/paper/7d4f4695ce28b27469bf72b6daf922ae20408610
[117] IT Security and Audit, https://www.semanticscholar.org/paper/057ce22879420b636e97aeb38a44626a25ed52b7
[118] Research on Security Audit in E-government, https://www.semanticscholar.org/paper/c3848b506d64f9e265901b8b0eab03fd8adb6194
[119] Security Audits Revisited, https://www.semanticscholar.org/paper/1ac77ebc65a7d64e406e8e8640f0a72487699d92
[120] Performance Auditing: A Measurement Approach, https://www.semanticscholar.org/paper/109f8d4214d64fd3f3f556e4fb4dcfdbf3da64e3
[121] Attacking threshold wallets, https://eprint.iacr.org/2020/1052
[122] Pragmatic analysis of key management for cryptocurrency custodians, https://ieeexplore.ieee.org/abstract/document/10634356/
[123] Towards threshold key exchange protocols, https://arxiv.org/abs/2101.00084
[124] FROST: Flexible Round-Optimized Schnorr Threshold Signatures, https://www.semanticscholar.org/paper/07793b23f45b46c4a0bd2e57802d143ad8f8ca77
[125] Security of Wang-Li Threshold Signature Scheme, https://www.semanticscholar.org/paper/44a4293f962f87aa258cd46daf76f1766a38324c
[126] On the Adaptive Security of FROST, https://www.semanticscholar.org/paper/dff4bbed29332b6b84ffdd222f69d8f8653949dd
[127] FlexHi: A Flexible Hierarchical Threshold Signature Scheme, https://www.semanticscholar.org/paper/a4a946a2d2f1ece4d4fdcf017cbc2980ee909056
[128] Security Analysis of LHL Threshold Signature Scheme, https://www.semanticscholar.org/paper/15c2de822520829a8b5ea5ac0b0b159d89734961
[129] Identi(cid:28)able Cheating Entity Flexible Round-Optimized Schnorr Threshold (ICE FROST) Signature Protocol, https://www.semanticscholar.org/paper/64ee923fdbb8463733fd78b69c670b4fb09951b5
[130] Short(t,n) Threshold Signature, https://www.semanticscholar.org/paper/e184e1827b6ce18c43d5dbac9953f375c94efbbf
[131] Mithril: Stake-based Threshold Multisignatures, https://www.semanticscholar.org/paper/56a3d8cbf0f9f4cc61432a4bbb008e04a0461b1d
[132] Threshold Digital Signature Scheme Based on ECC and Its Security, https://www.semanticscholar.org/paper/745355eba35d624c3ced63dfc420e5b1a0841a47
[133] Forward-Secure Threshold Signature Schemes, https://www.semanticscholar.org/paper/f64535f706b0b4000b7de50426c01ae29f9e12e0
[134] Forward Security in Threshold Signature Schemes, https://www.semanticscholar.org/paper/382040860c76a06ccdec44810ec7bd4ace202190
[135] Fully Adaptive Schnorr Threshold Signatures, https://www.semanticscholar.org/paper/8fa728bf480d941905bcc0929e3caf5355a36b9e
[136] Safeheron/multi-party-sig-cpp: This project is a C++ ..., https://github.com/Safeheron/multi-party-sig-cpp
[137] gg18 command - github.com/getamis/alice/example ..., https://pkg.go.dev/github.com/getamis/alice/example/gg18
[138] ZenGo-X/awesome-tss: A curated list of distributed key ..., https://github.com/ZenGo-X/awesome-tss
[139] velas/threshold-signatures-small-paillier-attack, https://github.com/velas/threshold-signatures-small-paillier-attack
[140] getamis/alice: Hierarchical Threshold Signature Scheme, https://github.com/getamis/alice
[141] SwingbyProtocol/tss-lib: \u2699\ufe0f Threshold Signature Scheme ..., https://github.com/SwingbyProtocol/tss-lib
[142] wtfrost - Rust, https://docs.rs/wtfrost
[143] frost-p256 - crates.io: Rust Package Registry, https://crates.io/crates/frost-p256/2.2.0/dependencies
[144] Cait-Sith \u2014 Rust crypto library // Lib.rs, https://lib.rs/crates/cait-sith
[145] modular-frost - Rust Package Registry, https://crates.io/crates/modular-frost/0.3.0/dependencies
[146] thresecdsa � PyPI, https://pypi.org/project/thresecdsa/0.1.1/
[147] Implementation of the FROST protocol for threshold Ed25519 signing, https://github.com/taurushq-io/frost-ed25519
[148] bnb-chain/tss-lib: Threshold Signature Scheme, for ECDSA ... - GitHub, https://github.com/bnb-chain/tss-lib
[149] Open Source Projects Recommendation on GitHub, https://www.semanticscholar.org/paper/b9af31e06139279abb6d021e72f2c30118a3c83f
[150] A Data Set of OCL Expressions on GitHub, https://www.semanticscholar.org/paper/0d9faaf7f95d47f029aa2ba950edb9ee0c127f9e
[151] Working with Github.com, https://www.semanticscholar.org/paper/56624f3753cc1fffb235d6c9d7441d6cc03f043e
[152] Github remote and Github, https://www.semanticscholar.org/paper/1ee31f42b5e9d5a4b3023aa57bdcb4ab4a24b6b4
[153] Active Repos: Integrating Generative AI Workflows into GitHub, https://www.semanticscholar.org/paper/3929ec18006f9855a41efd3712e0500923fa4069
[154] Efficient online-friendly two-party ECDSA signature, https://dl.acm.org/doi/abs/10.1145/3460120.3484803
[155] One Round Threshold ECDSA with Identifiable Abort, https://www.semanticscholar.org/paper/8c8c4c9f206c64424237eb9c3cc496567fc03488
[156] [PDF] Threshold ECDSA in Three Rounds\u2217 - Cryptology ePrint Archive, https://eprint.iacr.org/2023/765.pdf
[157] A Comparative Examination of Some Threshold ECDSA Protocols ..., https://blokzincir.bilgem.tubitak.gov.tr/en/a-comparative-examination-of-some-threshold-ecdsa-protocols-used-in-custody/
[158] An Efficient Multiparty Threshold ECDSA Protocol against Malicious ..., https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/2024/2252865
[159] [PDF] Threshold ECDSA Cryptography Review - NCC Group, https://www.nccgroup.com/media/xtff4dth/_ncc_dfinity_thresholdsignature_report_2022-06-14_v12.pdf
[160] [PDF] Real Threshold ECDSA, https://www.ndss-symposium.org/wp-content/uploads/2023-817-paper.pdf
[161] [PDF] Robust Threshold ECDSA with Online-Friendly Design in Three ..., https://eprint.iacr.org/2025/910.pdf
[162] Dynamic threshold ECDSA signature and application to asset ..., https://www.sciencedirect.com/science/article/abs/pii/S2214212621000466
[163] draft-irtf-cfrg-det-sigs-with-noise-02 - IETF Datatracker, https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-det-sigs-with-noise-02
[164] draft-irtf-cfrg-frost-15 - Two-Round Threshold Schnorr Signatures ..., https://datatracker.ietf.org/doc/draft-irtf-cfrg-frost/15/
[165] cfrg/draft-irtf-cfrg-signature-key-blinding - GitHub, https://github.com/cfrg/draft-irtf-cfrg-signature-key-blinding
[166] Key Blinding for Signature Schemes, http://ftp.jaist.ac.jp/pub/RFC/internet-drafts/draft-irtf-cfrg-signature-key-blinding-04.html
[167] Multiparty Computation (MPC) for Agile and Secure Enterprise Key ..., https://www.blockdaemon.com/blog/revisiting-secure-multiparty-computation-mpc-for-agile-enterprise-key-management
[168] An Introduction to Secure Multiparty Computation For Digital Asset ..., https://www.mpcalliance.org/blog/an-introduction-to-secure-multiparty-computation-for-digital-asset-custody-wallets
[169] How Multi-Party Computation Works and Why It Matters for CISOs, https://medium.com/@duokey.com/how-multi-party-computation-mpc-works-and-why-it-matters-for-cisos-544aaef57c07
[170] Secure multi-party computation - Wikipedia, https://en.wikipedia.org/wiki/Secure_multi-party_computation
[171] Secure Multiparty Computation | MPC Cryptography - Duality Tech, https://dualitytech.com/glossary/multiparty-computation/
[172] What Is MPC (Multi-Party Computation)? - Fireblocks, https://fireblocks.com/what-is-mpc/
[173] A Deep Dive into TSS-MPC: Dynamic's Focus on Security and ..., https://www.dynamic.xyz/blog/a-deep-dive-into-tss-mpc
[174] Privacy-Enhancing Cryptography | CSRC, https://csrc.nist.gov/Projects/pec/threshold
[175] CORR 2000-54 The Exact Security of ECDSA, https://www.semanticscholar.org/paper/ad5a8bbfe0ba8a208c91c12d39dab8dc23891daa
[176] Limits in the Provable Security of ECDSA Signatures, https://www.semanticscholar.org/paper/ac4b33d07b4fb3e0647fb02d1e64758c05e600b3
[177] A New Secure Authentication Scheme Based Threshold ECDSA For Wireless Sensor Network, https://www.semanticscholar.org/paper/8d9aef81016fe919736b84dc7d83cbb48f1162ad
[178] A Tale of Three Signatures: Practical Attack of ECDSA with wNAF, https://www.semanticscholar.org/paper/ccc65efdae2f5427f42347f875398b6bc09c7185
[179] Security Level of Cryptography \u2014 ECDSA, https://www.semanticscholar.org/paper/ea1992e942e4225763508a2fccc383dfd56a4e66
[180] Strong Known Related-Key Attacks and the Security of ECDSA, https://www.semanticscholar.org/paper/b24f5a4aa0b9fb9ffbc797a768dac7930f9a28da
[181] Strength in Numbers: Threshold ECDSA to Protect Keys in the Cloud, https://www.semanticscholar.org/paper/bc284845598bdadde73df58ff38b847fb33605d5
[182] The Security of DSA and ECDSA, https://www.semanticscholar.org/paper/238591fe092f8bdbb0b8910ece1289ac3fd421b8
[183] Handle the Traces: Revisiting the Attack on ECDSA with EHNP, https://www.semanticscholar.org/paper/a95bf4889d11cb54d0fb36e7b3dfe57a07fd6e7d
[184] Template Attacks on ECDSA, https://www.semanticscholar.org/paper/b8713430e190a5e11b9de711c8c36d97130115ef
[185] Generalized attack on ECDSA: known bits in arbitrary positions, https://www.semanticscholar.org/paper/08b3e5de9fcf5058231566c77a6bce0c2249c320
[186] Secure two-party threshold ECDSA from ECDSA assumptions, https://ieeexplore.ieee.org/abstract/document/8418649/
[187] Threshold ECDSA from ECDSA assumptions: The multiparty case, https://ieeexplore.ieee.org/abstract/document/8835354/
[188] New Key Extraction Attacks on Threshold ECDSA Implementations, https://conference.hitb.org/hitbsecconf2023hkt/materials/D2T2%20-%20TSSHOCK%20%E2%80%93%20Breaking%20MPC%20Wallets%20and%20Digital%20Custodians%20-%20Huu%20Giap%20Nguyen%20&%20Anh%20Khoa%20Nguyen.pdf
[189] Securing DNSSEC keys via threshold ECDSA from generic MPC, https://link.springer.com/chapter/10.1007/978-3-030-59013-0_32
[190] Efficient Threshold-Optimal ECDSA, https://www.semanticscholar.org/paper/027fde41c5d8501be4461b0a985993989eb00564
[191] Bandwidth-Efficient Robust Threshold ECDSA in Three Rounds, https://www.semanticscholar.org/paper/1486d2ab6c65e908708e02e310c3d8efb43e93ed
[192] RSA Threshold Signature, https://www.semanticscholar.org/paper/50ef099cf5f7265f7f37d57608a5cb32a528e420
[193] Bandwidth-efficient threshold EC-DSA, https://www.semanticscholar.org/paper/253628420969fb0a83f41e2b7dc2b120ddc2c408
[194] TP\u94b1\u5305\u8bef\u8f6c\u4e0e\u6570\u5b57\u8d44\u4ea7\u6cbb\u7406\uff1a\u6062\u590d\u6d41\u7a0b\u4e0e\u4f53\u7cfb\u5316\u7ba1\u7406\u7b56\u7565, https://www.shfuturetech.com.cn/news/lanmu2/12108.html
[195] \u5982\u4f55\u6062\u590d\u4f60\u7684TP\u94b1\u5305\uff1a\u4e00\u6b65\u6b65\u8d70\u5165\u533a\u5757\u94fe\u7684\u4e16\u754c, https://www.dlxcnc.com/news/lanmu2/5569.html
[196] tpwallet\u6700\u65b0\u7248\u5220\u9664\u94b1\u5305\u540e\u8fd8\u80fd\u6062\u590d\u5417, https://www.casafila.com/news/lanmu2/2879.html
[197] TP\u94b1\u5305\u5bc6\u94a5\u4e22\u5931\u540e\u5982\u4f55\u627e\u56de\u4e0e\u533a\u5757\u94fe\u5b89\u5168\u4e0e\u672a\u6765\u5c55\u671b, https://facegenmedia.com/news/lanmu1/3648.html
[198] (PDF) \u5e01\u5b89web3\u94b1\u5305\u79c1\u94a5\u5907\u4efd\u6559\u7a0b\uff1a\u5b89\u5168\u5b58\u50a8\u4e0e\u6062\u590d\u64cd\u4f5c ..., https://www.researchgate.net/publication/397009493_bianweb3qianbaosiyaobeifenjiaochenganquancunchuyuhuifucaozuoxiangjiebianweb3qianbaoyaoqingmaML53KJI
[199] \u6bd4\u7279\u5e01\u94b1\u5305\u627e\u56de\u6307\u5357, https://learnblockchain.cn/article/6778
[200] \u6b27\u6613\u94b1\u5305\u5730\u5740\u4e22\u5931\u600e\u4e48\u529e\uff1f\u522b\u614c\uff01OKX\u5b98\u65b9\u627e\u56de\u65b9\u6cd5\u4e0e\u5b89\u5168 ..., https://www.researchgate.net/publication/397175507_ouyiqianbaodezhidiushizenmebanbiehuangOKXguanfangzhaohuifangfayuanquanbeifenjiqiaofenxiangouyiokxqianbaoyaoqingmaDEX789
[201] Web 3 \u534f\u8bae\u6808\u4e0e\u7528\u6237\u4ea4\u4e92\u5c42 - \u77e5\u4e4e\u4e13\u680f, https://zhuanlan.zhihu.com/p/1949407841761883232
[202] \u89e3\u6790\u4f1a\u8bdd\u5bc6\u94a5\uff1aWeb3\u7248\u201c\u514d\u5bc6\u652f\u4ed8\u201d - Odaily, https://www.odaily.news/post/5181328
[203] (PDF) \u3010\u6b27\u6613\u9080\u8bf7\u7801\uff1aCEX789\u3011\u6b27\u6613API\u5bc6\u94a5\u5982\u4f55\u5b89\u5168\u7ed1\u5b9a\uff1f\u914d\u5408 ..., https://www.researchgate.net/publication/396783462_ouyiyaoqingmaCEX789ouyiAPImiyaoruheanquanbangdingpeihelianghuagongjushiyongzidonghuajiaoyiqishibufuza
[204] \u6784\u5efa\u5bc6\u94a5\u7ba1\u7406\u63a7\u5236\u5668\uff08KeyringController\uff09keyring-controller - \u7a00\u571f\u6398\u91d1, https://juejin.cn/post/7537641651209977908
[205] \u4e00\u6587\u8bfb\u61c2\u65b0\u4e0a\u7ebf\u7684\u300cERC-4337\u300d\uff1a\u4e0d\u518d\u9700\u8981\u52a9\u8bb0\u8bcd\uff0cWeb3\u5927\u89c4\u6a21 ..., https://www.binance.com/zh-CN/square/post/313179
[206] \u79d1\u666e\uff5c\u667a\u80fd\u5408\u7d04\u9322\u5305\u4ec0\u9ebc\u6642\u5019\u80fd\u666e\u53ca\uff1f\u4e00\u6587\u770b\u61c2ERC-4337, https://www.blocktempo.com/erc-4337-wallet-building-and-principles/
[207] \u4ee5\u592a\u574a\u9322\u5305\u7684\u8b8a\u9769\uff1a\u5e33\u6236\u62bd\u8c61\u8207ERC-4337 \u7684\u6a5f\u9047\u8207\u6311\u6230 - \u5340\u584a\u5ba2, https://blockcast.it/2023/01/14/how-erc-4337-account-abstraction-will-evolve-wallets/
[208] Social Recovery Wallet \u793e\u4ea4\u6062\u5fa9\u9322\u5305 - Medium, https://medium.com/taipei-ethereum-meetup/social-recovery-wallet-%E7%A4%BE%E4%BA%A4%E6%81%A2%E5%BE%A9%E9%8C%A2%E5%8C%85-75105c6285b2
[209] \u62bd\u8c61\u8d26\u6237\u5b66\u4e60\u7b14\u8bb0\uff081\uff09\uff1a\u4ece4337\u51fa\u53d1 - \u77e5\u4e4e\u4e13\u680f, https://zhuanlan.zhihu.com/p/667211672
[210] Private Key Backup and Recovery Framework in Blockchain-based Service Environment, https://www.semanticscholar.org/paper/1428248ff03beed1d17fb3569475a47701679286
[211] Multi-Platform Wallet for Privacy Protection and Key Recovery in Decentralized Applications, https://www.semanticscholar.org/paper/effca6b1c29109a71892ba9a7c2f30a2810dd3ce
[212] Crypto Bank: Cryptocurrency Wallet Based on Blockchain, https://www.semanticscholar.org/paper/65574a7e7d1768b67993fd26e90f0f68c69c0fe9
[213] Implementing a blockchain from scratch: why, how, and what we learned, https://www.semanticscholar.org/paper/4f9298f2d43f22f33f44df3f7e816b88bbc7a7a2
[214] Promize - Blockchain and Self Sovereign Identity Empowered Mobile ATM Platform, https://www.semanticscholar.org/paper/c65d42a06aeb2c2fa6b7fb65005ff814293a62cd
[215] Blockchain Control, https://www.semanticscholar.org/paper/e78e19263882661e2c18d5699748e17166d8f3a2
[216] \u5c14\u4f1a\u7528\u201c\u533a\u5757\u94fe\u201d\u8bb0\u8d26\u5417, https://www.semanticscholar.org/paper/99ccd34d0ace7b9e1e56726cdfe198544a7a4f78
[217] Towards a Design Space for Blockchain-Based System Reengineering, https://www.semanticscholar.org/paper/5fc1e208c2198a76dff973c06fa90f32701bae64
[218] __BLOCKCHAIN AND DISTRIBUTED LEDGERS, https://www.semanticscholar.org/paper/cee4c03fb23b5102e2fd27f3a2c5e357c3a7bcd2
[219] \u6297\u8d27\u5e01\u5931\u6548\u7684\u533a\u5757\u94fe\u94b1\u5305\u4fdd\u62a4\u534f\u8bae\u7814\u7a76., https://search.ebscohost.com/login.aspx?direct=true&profile=ehost&scope=site&authtype=crawler&jrnl=16739418&AN=147658096&h=u2TIiHC7fJxoTBgJfwt58yITiQeh72zArckemB0%2FIoRdfhvfUi1VaLEqNQIASQKN2dWPj1H9uTbY%2BMvXXcGZRg%3D%3D&crl=c
[220] \u533a\u5757\u94fe\u4e0e\u53ef\u4fe1\u6570\u636e\u7ba1\u7406: \u95ee\u9898\u4e0e\u65b9\u6cd5, https://html.rhhz.net/rjxb/html/5434.htm
[221] \u533a\u5757\u94fe\u6570\u5b57\u8d27\u5e01\u4ea4\u6613\u7684\u533f\u540d\u6027: \u4fdd\u62a4\u4e0e\u5bf9\u6297, http://cjc.ict.ac.cn/online/onlinepaper/sm-2023112142420.pdf
[222] \u533a\u5757\u94fe\u539f\u7406\u53ca\u5176\u6838\u5fc3\u6280\u672f, http://cjc.ict.ac.cn/online/onlinepaper/cxq-20201230112319.pdf
[223] \u57fa\u4e8e\u4ee5\u592a\u574a\u667a\u80fd\u5408\u7ea6\u7684\u5bc6\u5c01\u5f0f\u533a\u5757\u94fe\u62cd\u5356\u53ef\u4fe1\u65b9\u6848\u7684\u7814\u7a76, https://www.hanspub.org/journal/paperinformation?paperID=35514
[224] Account Abstraction and ERC-4337 - Part 1 | QuickNode Guides, https://www.quicknode.com/guides/ethereum-development/wallets/account-abstraction-and-erc-4337
[225] Introductory Guide to Account Abstraction (ERC-4337) - Blocknative, https://www.blocknative.com/blog/account-abstraction-erc-4337-guide
[226] Gelato's Guide to Account Abstraction: from ERC4337 to EIP7702, https://gelato.cloud/blog/gelato-s-guide-to-account-abstraction-from-erc-4337-to-eip-7702
[227] A complete guide on account abstraction | by asdf - Medium, https://medium.com/@0xasdf_eth/a-complete-guide-on-account-abstraction-b885542e7552
[228] ERC-4337 Documentation, https://docs.erc4337.io/index.html
[229] ERC-4337: Account Abstraction via Entry Point Contract specification, https://ethereum-magicians.org/t/erc-4337-account-abstraction-via-entry-point-contract-specification/7160
[230] How does social login with MetaMask work?, https://support.metamask.io/configure/wallet/social-login/
[231] Introducing MetaMask social login, https://metamask.io/news/introducing-metamask-social-login
[232] Social Recovery Wallets - Web3 Wallet Security Basics, https://updraft.cyfrin.io/courses/web3-wallet-security-basics/signer-basics/social-recovery-wallets
[233] MetaMask Developer Documentation - Build Web3 Apps ..., https://docs.metamask.io/
[234] MetaMask Embedded Wallets, https://docs.metamask.io/embedded-wallets/
[235] Smart Contract-Based Social Recovery Wallet ..., https://dl.acm.org/doi/10.1145/3564746.3587016
[236] Wallet Provider Spec - Flow Developer Portal, https://developers.flow.com/build/tools/wallet-provider-spec
[237] Navigating the Complexities of Transaction Approval and ..., https://fireblocks.com/blog/navigating-the-complexities-of-transaction-approval-and-validation-flows/
[238] Account Abstraction, Analysed, https://www.semanticscholar.org/paper/8897596d1acffbc0de9827bac1e727d299ddbf0a
[239] Account Abstraction on Ethereum, https://www.semanticscholar.org/paper/4b1ca552182f9dff3def1e2cad848c2ccb20d263
[240] Characterizing Erasable Accounts in Ethereum, https://www.semanticscholar.org/paper/200866d105bea167ea39755874d78d8ae631aff1
[241] Metals Engineering: A Technical Guide, https://www.semanticscholar.org/paper/9e6b0f6536f014628e7796ad563bea9254c46e50
[242] Address Clustering Heuristics for Account-Based Blockchain Networks: An Analysis Based on a Decentraland User Set, https://www.semanticscholar.org/paper/e97346b2c138cee038e851b1b4b39f020893d0a6
[243] Conservativeness, Stability, and Abstraction, https://www.semanticscholar.org/paper/772fedc4ccac2ef9977a0f2055a6c696a7e96e20
[244] Understanding the dynamic and microscopic traits of typical Ethereum accounts, https://www.semanticscholar.org/paper/7bdd4f2f3df33d2b04ede8a2ff7d857dbaaad847
[245] Using Genetic Programming with Lambda Abstraction to Find Technical Trading Rule, https://www.semanticscholar.org/paper/69af663fb9addb974a3fae9a6be9637e5d8caa18
[246] An Implementation and Evaluation of Layer 2 for Ethereum with zk-Rollup, https://www.semanticscholar.org/paper/7b797b1e6fdf396f2276da9f3d0d90b55c27d823
[247] Using Genetic Programming with Lambda Abstraction to Find Technical Trading Rules, https://www.semanticscholar.org/paper/013ed69110d63d61cfeb329513d0022b2786f19a
[248] ERC-4337: Account abstraction using alt mempool, https://eip.info/eip/4337
[249] Framework Design and Theoretical Research on Abstract Account Gas Payment Mechanism, https://ieeexplore.ieee.org/abstract/document/10866601/
[250] Picoin Wallet Portfolio Optimization, https://www.semanticscholar.org/paper/18db38aace7a6b4711523c32005cf3a3e572aa6a
[251] Smartwallets, https://www.semanticscholar.org/paper/ac6108d032ea914b44921ae9e9aea324dc3bd5c0
[252] A Social Wallet Scheme with Robust Private Key Recovery, https://www.semanticscholar.org/paper/7debd53fd6ba124275644443a9928b185ebbcb7b
[253] A Decentralized Mnemonic Backup System for Non-custodial Cryptocurrency Wallets, https://www.semanticscholar.org/paper/5c7df4192015e08282c8b9e501a392df53ef5990
[254] Iterative Design of An Accessible Crypto Wallet for Blind Users, https://www.semanticscholar.org/paper/dbebd1b528c73e71f5f39b2803237475d2c6b408
[255] Safeguarding crypto wallet with multi-layered defense system, https://ieeexplore.ieee.org/abstract/document/11088300/
[256] Two-Factor Authentication (2FA) for Crypto Wallets, https://www.debutinfotech.com/blog/two-factor-authentication-for-crypto-wallets
[257] BAuth-ZKP\u2014A Blockchain-Based Multi-Factor ..., https://pmc.ncbi.nlm.nih.gov/articles/PMC10007237/
[258] Safeguarding Your Blockchain Assets with Wallets and Key ..., https://www.softobotics.org/blogs/wallets-and-key-management-safeguarding-your-blockchain-assets/
[259] Crypto Wallet Protection: Security with Cybersecurity as a ..., https://www.micromindercs.com/blog/crypto-wallet-protection
[260] What is Two-Factor Authentication (2FA) in crypto?, https://www.coinbase.com/learn/wallet/what-is-two-factor-authentication-2fa-in-crypto
[261] A systematic review of multi-factor authentication in digital ..., https://www.sciencedirect.com/science/article/pii/S1383762125000748
[262] Is your biometric-protected crypto wallet really secure?, https://facephi.com/en/biometric-protected-crypto-wallet/
[263] Hardware Token Protocols, https://www.packetlabs.net/posts/hardware-token-protocols/
[264] The Ultimate Guide to WebAuthn & FIDO2 - 0hlov3, https://schoenwald.aero/posts/2025-02-5_the-ultimate-guide-to-webauthn-fido2/
[265] User Authentication Specifications Overview, https://fidoalliance.org/specifications/
[266] FIDO2 Security Keys: A Practical Guide, https://frontegg.com/blog/fido2-security-keys
[267] FIDO2.1 Implementation using the Unifyia Platform, https://www.idmanagement.gov/implement/unifyia-guide/
[268] FIDO Authentication Guide: Passkeys & WebAuthn Explained, https://doubleoctopus.com/blog/standards-regulations/your-complete-guide-to-fido-fast-identity-online/
[269] The Passkey Revolution: End Passwords for Good, https://mojoauth.com/white-papers/passkeys-passwordless-authentication-handbook/
[270] Password vs Passwordless Authentication: The Complete ..., https://clerk.com/articles/password-vs-passwordless-authentication-guide
[271] FIDO Standard Security Key: Ultimate Protection, https://www.anonybit.io/blog/fido-standard-security-key/
[272] Authenticators - NIST Pages, https://pages.nist.gov/800-63-4/sp800-63b/authenticators/
[273] Blockchain meets network analytics: a tale of heuristics, location and ..., https://www.researchgate.net/publication/360461256_Blockchain_meets_network_analytics_a_tale_of_heuristics_location_and_fraud_detection
[274] Investigating Blockchain Crimes using Blockchain Forensics, https://blog.merklescience.com/general/investigating-blockchain-crimes-using-blockchain-forensics
[275] Blockchain Analysis in Action: Real-Life Use Cases and Insights, https://www.ulam.io/blog/blockchain-analysis-in-action-real-life-use-cases-and-insights
[276] Enhancing fraud detection in the Ethereum blockchain using ..., https://pmc.ncbi.nlm.nih.gov/articles/PMC11888915/
[277] BlockScan: Detecting Anomalies in Blockchain Transactions - arXiv, https://arxiv.org/html/2410.04039v5
[278] Decoding the Chain: How Data Science-Based Heuristics Reveal ..., https://www.elementus.io/blog-post/decoding-the-chain-how-data-science-based-heuristics-reveal-blockchain-networks
[279] How Off-Chain and On-Chain Data Can Prevent Crypto Fraud, https://www.chainalysis.com/blog/preventing-crypto-fraud-with-off-chain-on-chain-data/
[280] A review on deep anomaly detection in blockchain - ScienceDirect, https://www.sciencedirect.com/science/article/pii/S209672092400040X
[281] A Blockchain Wallet Scheme with Multi-Factor Authentication Based on Distributed System, https://www.semanticscholar.org/paper/f065659808106ac9fc044d4c24df0ba39af016ec
[282] Wallets and Key Management, https://www.semanticscholar.org/paper/82ff2b8a6c5a5d874a466b572aa3f630a85ace32
[283] Implementing a Secure Blockchain-Based Wallet System with Multi-Factor Authentication, https://www.semanticscholar.org/paper/9aaf4ec0d04f9a3c9d920dc910c4d8261bb2695d
[284] Blockchain-based multi-factor authentication: A systematic literature review, https://www.semanticscholar.org/paper/039f0c562689b7923e71392a3298cfdbae5fa85c
[285] A Multi-Factor Authentication Framework for Secure Access to Blockchain, https://www.semanticscholar.org/paper/cf2cd8b4bcb39d7712c1259451274c3ec21f9641
[286] Risk management in blockchain, https://www.semanticscholar.org/paper/0c370503536ec9a6adc5cb6c3f712d676fe46f47
[287] Authentication of Financial Wallet System and Data Protection using BlockChain, https://www.semanticscholar.org/paper/1226bd39daf057ad60dd8b8063dfbb0dc1e6da1a
[288] Blockchain-Based Two-Factor Authentication for Credit Card Validation, https://www.semanticscholar.org/paper/4ea5f6ed1a9cc835989404a6339989dce6708230
[289] A Proposed Mobile Voting Framework Utilizing Blockchain Technology and Multi-Factor Authentication, https://www.semanticscholar.org/paper/aa47f5dfc0b8bb594e77298a96515ff8c44ef76a
[290] Risk monitor system for blockchain-based security issuing system, https://www.semanticscholar.org/paper/1b283e08e1d053d235fbe9e0be6a337cc0946b14
[291] Blockchain-Enhanced Multi-Factor Authentication for Securing IIoT, https://www.semanticscholar.org/paper/625e10376e2b292b2408eabda213d0d5e9b2e93f
[292] Cryptocurrency Wallet, https://www.semanticscholar.org/paper/f1c9cbe3c00bb9b1e040c18d092f358c5c6e82dc
[293] A Blockchain Implementation for Configurable Multi-Factor Challenge-Set Self-Sovereign Identity Authentication, https://www.semanticscholar.org/paper/fdd04ac1e4fd79e630983611e8b09ada6b15b102
[294] Hand-held Crypto Device SEC-36, https://www.semanticscholar.org/paper/3dc419d74433e6d21bb2ca23e9c485c09729e4fa
[295] Multifactor Authentication System on Blockchain Infrastructure, https://www.semanticscholar.org/paper/b8f65c28e28764d885eabe5242aeaf77c07d5630
[296] Secure Data Storage and Exchange with a Private Wallet, https://www.semanticscholar.org/paper/99147bd3da92dbf03638e28519b7fa9404932661
[297] Integrating Blockchain and Multi-Factor Authentication for Enhanced Cloud Security in Certificate Verification Systems, https://www.semanticscholar.org/paper/48071512f8d1dceb3c263a0042ac45eefaa81c38
[298] USING DEVICE MOVEMENT FOR MULTI-FACTOR COMPUTING DEVICE AUTHENTICATION, https://www.semanticscholar.org/paper/5f8736caef6e4db5e491901fa9de33c10ee36050
[299] Enhanced cryptocurrency security by time-based token multi-factor authentication algorithm, https://ieeexplore.ieee.org/abstract/document/8644084/
[300] Enhancing Multi-Signature Cryptocurrency Wallets with Risk-Based Authentication, https://ucalgary.scholaris.ca/items/514037f3-3d69-492f-9902-fd71c47cccf7
[301] Remote WebAuthn: FIDO2 Authentication for Less Accessible Devices, https://www.semanticscholar.org/paper/746594664b9baba969f41cea2290d7ca6e4717d7
[302] FIDO U2F TWO FACTOR AUTHENTICATION PROTOCOL, https://www.semanticscholar.org/paper/302528a5b97104c8154df4374bc20b4fc67d63b4
[303] FIDO2, CTAP 2.1, and WebAuthn 2: Provable Security and Post-Quantum Instantiation, https://www.semanticscholar.org/paper/ae7f808c4e0bd300763799edb7de8f9dd0c76e32
[304] Social Engineering Resistant 2FA, https://www.semanticscholar.org/paper/d7897e23822bad89c0d8a52800515f5559310d9c
[305] Token meets Wallet: Formalizing Privacy and Revocation for FIDO2, https://www.semanticscholar.org/paper/2c5dc75144fe5787dc3a8b1977ac3063024ebb9d
[306] A Formal Treatment of Hardware Wallets, https://www.semanticscholar.org/paper/7184505b9134640a8b9e43f6a5e8791689c7ed0e
[307] Rogue key and impersonation attacks on FIDO2: From theory to practice, https://www.semanticscholar.org/paper/6f2bb2da217ca03b72a6334997251797baeab137
[308] Minimizing Trust in Hardware Wallets with Two Factor Signatures, https://www.semanticscholar.org/paper/277898cc22e6706590f9f95fa956873b64059018
[309] simFIDO: FIDO2 User Authentication with simTPM, https://www.semanticscholar.org/paper/7ee68251acb59237fe215e88a3d0a2d4dd4a75c5
[310] Secure Your Passwords through Safe Wallet with a Smart Key and a Secret Key, https://www.semanticscholar.org/paper/02bf98396a616c883c0db1b7e5da03c5a628da3a
[311] Technical Report on a Virtual CTAP2 WebAuthn Authenticator, https://www.semanticscholar.org/paper/fbeff336eee4f3b34d7ed9b0e49793825cc281b6
[312] InShopnito Secure Storage Module, https://www.semanticscholar.org/paper/d0d8ee439ba8d364418e9f38d1904929265ed36f
[313] Secure Industrial Device Wallet, https://www.semanticscholar.org/paper/3f4261c27185ed06dc1fdbafd12ef5d21eecf4c5
[314] Smartpass Fips Token Fips 140-1 Non-proprietary Cryptographic Module Security Policy Level 1 Validation, https://www.semanticscholar.org/paper/43f8ba59b04cdb8b1eabb4e11d74ee83497a3966
[315] Hardware TOTP tokens with time synchronization, https://www.semanticscholar.org/paper/1f228578605d6dda3adf484bd38872d7769dc187
[316] Shared-Custodial Password-Authenticated Deterministic Wallets, https://www.semanticscholar.org/paper/f3b2b356116c5b1e90cbee2b74ab1af469984c5f
[317] "It's Stored, Hopefully, on an Encrypted Server": Mitigating Users' Misconceptions About FIDO2 Biometric WebAuthn, https://www.semanticscholar.org/paper/cecb164c2b22e353a8de94af6314461204a57d15
[318] Highly Secure Cryptocurrency Hardware Wallet, https://www.semanticscholar.org/paper/3512c1184ecfe609c73e95d899e3f354f2547bbf
[319] CREDENTIAL: Secure Cloud Identity Wallet, https://www.semanticscholar.org/paper/1b8803f537eed12d3a0ab4896399a0cff94b5428
[320] Exploring the Security and Privacy Impacts of Using 2FA Apps, https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-49.pdf
[321] FIDO2 Overview, Use Cases, and Security Considerations, https://www.researchgate.net/profile/Eleftherios-Georgiadis-2/publication/370750978_FIDO2_Overview_Use_Cases_and_Security_Considerations/links/645ff5114353ba3b3b631ea1/FIDO2-Overview-Use-Cases-and-Security-Considerations.pdf
[322] Exploration of the security and usability of the fido2 authentication protocol, https://drum.lib.umd.edu/bitstreams/63e5eace-630f-4a78-8186-5516e94e6d68/download
[323] Asynchronous Remote Key Generation and its Applications in W3C WebAuthn and FIDO, https://openresearch.surrey.ac.uk/view/pdfCoverPage?instCode=44SUR_INST&filePid=13215225400002346&download=true
[324] SoK: Web Authentication and Recovery in the Age of End-to-End Encryption, https://petsymposium.org/popets/2025/popets-2025-0113.php
[325] Machine Learning for Fraud Detection in Blockchain Transaction, https://www.semanticscholar.org/paper/11a3e78bcc88c5f9efd9320655d13bcbf85f152a
[326] A tool capable of tracking cybercrime financial transactions in Bitcoin, https://www.semanticscholar.org/paper/44c599c2748a73e429cda9a168a265e48261e5af
[327] Understanding the Financial Transaction Security through Blockchain and Machine Learning for Fraud Detection in Data Privacy and Security, https://www.semanticscholar.org/paper/94a206414bef27b45fee7399d7f3e010c59aaafd
[328] Wallet Payments Recent Potential Threats and Vulnerabilities with its possible security Measures, https://www.semanticscholar.org/paper/5a748891071107ab9400d759d7224076e44e31b0
[329] Transaction Proximity: A Graph-Based Approach to Blockchain Fraud Prevention, https://www.semanticscholar.org/paper/0a3bae165acb91fb0532355687860fb4e2a3d705
[330] Ethereum Chain Data Structures - IPLD, https://ipld.io/specs/codecs/dag-eth/chain/
[331] New Transaction Types on Ethereum, https://blog.mycrypto.com/new-transaction-types-on-ethereum
[332] An Evaluation of Gas Consumption Prediction on Ethereum based on Transaction History Summarization, https://www.semanticscholar.org/paper/d59da86b38539beca6907d1d80dcb21260138a3c
[333] Transactions, https://ethereum.org/developers/docs/transactions/
[334] JSON-RPC Changes for Type 0x2 EIP-1559 transactions, https://ethereum-magicians.org/t/json-rpc-changes-for-type-0x2-eip-1559-transactions/6101
[335] How to Send an EIP-1559 Transaction | QuickNode Guides, https://www.quicknode.com/guides/ethereum-development/transactions/how-to-send-an-eip-1559-transaction
[336] Ethereum transaction types | MetaMask developer documentation, https://docs.metamask.io/services/concepts/transaction-types/
[337] eth | API - Web3.js, https://docs.web3js.org/api/web3/namespace/eth
[338] Hardware Security Modules (HSM): Best Practices Overview, https://cyberw1ng.medium.com/hardware-security-modules-hsm-best-practices-overview-b122f3e2ff2c
[339] Internal communication security - AWS Key Management Service, https://docs.aws.amazon.com/kms/latest/cryptographic-details/internal-communication-security.html
[340] How to Achieve Enterprise Data Security with KMS & HSM - Fortanix, https://www.fortanix.com/blog/how-to-achieve-enterprise-data-security-with-kms-hsm
[341] [PDF] Finding end-to-end security in crypto custody - Anchorage Digital, https://learn.anchorage.com/Finding-End-to-End-Security-in-Crypto-Custody.pdf
[342] Rethinking HSM and TPM Security in the Cloud: Real-World Attacks ..., https://arxiv.org/html/2507.17655v1
[343] HSM vs KMS - AWS | Azure | Thales | Entrust - Accutive Security, https://accutivesecurity.com/hsm-vs-kms/
[344] Secure your Azure Managed HSM deployment - Microsoft Learn, https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/secure-managed-hsm
[345] [PDF] Best Practices for Cryptographic Key Management, https://www.thalestct.com/wp-content/uploads/2022/09/Best-Practices-for-Cryptographic-Key-Management.pdf
[346] Wallet Security: The 'Non-Custodial' Fallacy - a16z crypto, https://a16zcrypto.com/posts/article/wallet-security-non-custodial-fallacy/
[347] Fireblocks' Multi-Layer Digital Asset Security, https://fireblocks.com/report/fireblocks-multi-layer-digital-asset-security/
[348] Secure Storage of Crypto Wallet Seed Phrase Using ECC and Splitting Technique, https://www.semanticscholar.org/paper/b4f7488db03077dd818927e556e1eda0da1c360b
[349] Improving the Security of a Webservice: Best Practices and Attack Simulations, https://www.semanticscholar.org/paper/c02280cef6fd15f061be977ca62a6bb24abc39df
[350] Overview of Attack Surfaces in Blockchain, https://www.semanticscholar.org/paper/2fef516e31ffb6fd24ef971c3dd8e4605856dba7
[351] Security Analysis of Crypto API, https://www.semanticscholar.org/paper/cfe618cae3e3ee43227841d969c67217762be737
[352] W-Shield: Protection against Cryptocurrency Wallet Credential Stealing, https://www.semanticscholar.org/paper/a0cb820448865aaf62f74c89c319fdc0a56a6c35
[353] G2R Crypto Wallet using Indian language Mnemonics, https://www.semanticscholar.org/paper/037ff70d5ee861e9aeb6f8fcbcccf9fca851d8c1
[354] Analysis of Security Issues in Blockchain Wallet, https://www.semanticscholar.org/paper/bca73593170616b98fd2d9116fc23229e44a4ee3
[355] Usability and Security Analysis of the KeepKey Wallet, https://www.semanticscholar.org/paper/7ed85a09209ae8f3ff2658d860de901cf71ab708
[356] Horus: A Security Assessment Framework for Android Crypto Wallets, https://www.semanticscholar.org/paper/ea289855fefbfb7c22d8c98216b7cb3273044a42
[357] Multisignature Crypto Wallet Paper, https://www.semanticscholar.org/paper/83321bb5a6340ea1dc6616c9c639514d70924b97
[358] Attainable Hacks on Keystore Files in Ethereum Wallets - A Systematic Analysis, https://www.semanticscholar.org/paper/42b9e88bfc52e46dbb5f2243578761d2d21d83b9
[359] Mobile Money Wallet Security against Insider Attack Using ID-Based Cryptographic Primitive with Equality Test, https://www.semanticscholar.org/paper/bed5781ada22ff079d4c4e7da6fcd9d7cddcc254
[360] Security testing of crypto exchanges based on Owasp technology of Web Security Testing Guide, https://www.semanticscholar.org/paper/b7b66e4e82e367225da34738826a84b9ac213430
[361] Security Evaluation of Smart Contract-Based On-chain Ethereum Wallets, https://www.semanticscholar.org/paper/6211896beb38e78b543c2e5c89900d787480c7e3
[362] Identifying the Owner of a Crypto Wallet Address in Law Enforcement Practice, https://www.semanticscholar.org/paper/149059d8f55e837c97ef01bad31d9dcb5de878e0
[363] An Empirical Analysis of Security and Privacy Risks in Android Cryptocurrency Wallet Apps, https://www.semanticscholar.org/paper/d8ec3dabe455c1ea40daf711bb4aaa0e8c019245
[364] Analysis of attack surfaces on blockchain systems, https://openarchive.nure.ua/items/34eda7e7-5bde-4d44-94ab-c8ec3b0def2e
[365] Sok: Design, vulnerabilities, and security measures of cryptocurrency wallets, https://arxiv.org/abs/2307.12874
[366] Attack surface analysis of permissioned blockchain platforms for smart cities, https://ieeexplore.ieee.org/abstract/document/8656983/
[367] Security aspects of cryptocurrency wallets\u2014a systematic literature review, https://dl.acm.org/doi/abs/10.1145/3596906
[368] Endpoint Focused Ideal Attributes of a Cryptocurrency Wallet, https://link.springer.com/chapter/10.1007/978-981-97-9507-9_29
[369] Exploring the attack surface of blockchain: A systematic overview, https://arxiv.org/abs/1904.03487
[370] Wallet security, https://link.springer.com/chapter/10.1007/978-3-031-39288-7_3
[371] Crypto Custody, https://www.semanticscholar.org/paper/1efe39b27a3b8c2a85139ce9cf6b542310198b17
[372] Best Practices to Securely Operate Hardware Security Modules in a High Availability Setup, https://www.semanticscholar.org/paper/78f40fb3b0142c63cfba0a52fa7573a944d8f461
[373] Improving the Security of KMS on a Cloud Platform Using Trusted Hardware, https://www.semanticscholar.org/paper/441735a04a2ba5d562f296185427220a0bfde58a
[374] Best Practices and Challenges in Asset Management Solution Implementation, https://www.semanticscholar.org/paper/daf3fcc30113d9022bb86e390d610dfff283f0e8
[375] Cloud security key management, https://www.semanticscholar.org/paper/2158ddabe0ffcd625275b22b8e755df808e56bfe
[376] Police Custody as a System and Unified Policy : Best Practices for Reducing Officer and Prisoner Risks of Injury and Death, https://www.semanticscholar.org/paper/8d6b4d5873fc4b020f92818d9f0789524f895a50
[377] AWS CloudHSM V2 - API Reference, https://www.semanticscholar.org/paper/1dca721a53dce00d6a139a0fbbbafb3aaba92127
[378] Securing microservices: challenges and best practices, https://www.semanticscholar.org/paper/f92fdec0194c806fec6183c955a655e02c04127b
[379] Hardware Security Modules: Attacks and Secure Configuration, https://www.semanticscholar.org/paper/a42845b09fc23fc2205565072a590160a2810e4b
[380] DTN Security Best Practices, https://www.semanticscholar.org/paper/6868522a4fbca6de65fe3eeb2d00a968a92c439c
[381] Your First Aptos Multisig (Python SDK), https://aptos.dev/build/guides/first-multisig
[382] Multisignature Smart-Contract Wallets - BitGo Developer Portal, https://developers.bitgo.com/docs/multisig-smart-contract
[383] Rivercare: Shaping the Decentralized Identity of Mother Nature on Blockchain through Care Activities of Stewards, https://www.semanticscholar.org/paper/90dbfb50bf78363affe76fddd07a587e06ebc9ac
[384] An overview of MPC, TSS and MPC-TSS wallets | Medium, https://mmasmoudi.medium.com/an-overview-of-multi-party-computation-mpc-threshold-signatures-tss-and-mpc-tss-wallets-4253adacd1b2
[385] IBM/TSS: Threshold signature schemes made simple to use - GitHub, https://github.com/IBM/TSS
[386] Blockchain-based Multisignature Wallet System for Decentralized Autonomous Organization, http://informatika.stei.itb.ac.id/~rinaldi.munir/TA/Makalah_TA_Vincentius.pdf
[387] Web3Auth MPC Core Kit React Native SDK | Documentation, https://web3auth.io/docs/sdk/mpc-core-kit/mpc-core-kit-react-native
[388] Blockchain privacy consensus mechanism based on threshold signature, https://www.semanticscholar.org/paper/2c5b6d002c6f20f48b0f00aed3a54fd0aff3cfcb
[389] [PDF] Research on Elliptic Curve Cryptography in Blockchain of Efficiency ..., https://www.scitepress.org/Papers/2024/135242/135242.pdf
[390] [PDF] A Survey on Elliptic Curve Cryptography - m-hikari.com, https://www.m-hikari.com/ams/ams-2014/ams-153-156-2014/mohamedAMS153-156-2014.pdf
[391] Blockchain - Elliptic Curve Cryptography - GeeksforGeeks, https://www.geeksforgeeks.org/ethical-hacking/blockchain-elliptic-curve-cryptography/
[392] [PDF] A Survey of Elliptic Curve Cryptosystems, Part I: Introductory, https://www.nas.nasa.gov/assets/nas/pdf/techreports/2003/nas-03-012.pdf
[393] (PDF) A Survey Report On Elliptic Curve Cryptography, https://www.researchgate.net/publication/267691095_A_Survey_Report_On_Elliptic_Curve_Cryptography
[394] [PDF] Use of Elliptic Curve Cryptography in Block Chain Technology, https://journalcrd.org/wp-content/uploads/35-CRD2275.pdf
[395] Elliptic curve cryptography: survey and its security applications, https://dl.acm.org/doi/10.1145/2007052.2007073
[396] Elliptic Curve Cryptography in Blockchain Technology - SSRN, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4033934
[397] [PDF] ECDSA Security in Bitcoin and Ethereum: a Research Survey, https://www.coinfabrik.com/wp-content/uploads/2016/06/ECDSA-Security-in-Bitcoin-and-Ethereum-a-Research-Survey.pdf
[398] Verify ed25519 signatures cheaply on Eth using ZK-Snarks, https://ethresear.ch/t/verify-ed25519-signatures-cheaply-on-eth-using-zk-snarks/13139
[399] ED25519 Signature: Upping The Ante, https://blockchainreporter.net/ed25519-signature-upping-the-ante/
[400] Threshold Ed25519 \u2014 It's Just Magical And Fit For A More ..., https://medium.com/asecuritysite-when-bob-met-alice/threshold-ed25519-its-just-magical-and-fit-for-a-more-resilient-and-trusted-world-5431e124942
[401] Accounts, Signature Verification & Keys (ECDSA vs. ..., https://docs.hedera.com/hedera/core-concepts/smart-contracts/understanding-hederas-evm-differences-and-compatibility/for-evm-developers-migrating-to-hedera/accounts-signature-verification-and-keys-ecdsa-vs.-ed25519
[402] Ed25519 in smart contracts - solidity, https://ethereum.stackexchange.com/questions/42771/ed25519-in-smart-contracts
[403] Breaking Down ECDSA and Ed25519 Digital Signatures, https://billatnapier.medium.com/breaking-down-ecdsa-and-ed25519-digital-signatures-0704ddb549ad
[404] What is Merkle Tree? Blockchain hashing, proofs, and Web3 uses, https://www.cube.exchange/what-is/merkle-tree
[405] zhangchiqing/merkle-patricia-trie: A simplified golang ... - GitHub, https://github.com/zhangchiqing/merkle-patricia-trie
[406] Merkle Patricia Trie in Ethereum: A Silhouette -, https://kba.ai/merkle-patricia-trie-in-ethereum-a-silhouette/
[407] Merkle Patricia Trie - Ethereum.org, https://ethereum.org/developers/docs/data-structures-and-encoding/patricia-merkle-trie/
[408] Merkle Trees, Patricia Tries, and How Ethereum Stores Data - Medium, https://medium.com/@anandi.sheladiya/merkle-trees-patricia-tries-and-how-ethereum-stores-data-408e27492245
[409] [PDF] mLSM: Making Authenticated Storage Faster in Ethereum - USENIX, https://www.usenix.org/system/files/conference/hotstorage18/hotstorage18-paper-raju.pdf
[410] What are Patricia Merkle Tries? | Alchemy Docs, https://www.alchemy.com/docs/patricia-merkle-tries
[411] An introduction to Merkle Patricia Trie - LambdaClass Blog, https://blog.lambdaclass.com/an-introduction-to-merkle-patricia-trie/
[412] What are Verkle Trees in Ethereum? - Web3 Labs Blog, https://blog.web3labs.com/what-are-verkle-trees-in-ethereum/
[413] Elliptic curve cryptography, https://www.semanticscholar.org/paper/f48cc7ae95bbd25b1e668cabe6ef4af45186e6f4
[414] Elliptic Curve Cryptography in Blockchain Technology, https://www.semanticscholar.org/paper/97459e0efccb20110ca3a393ad681a6f8b7fa1a0
[415] ELLIPTIC-CURVE CRYPTOGRAPHY, https://www.semanticscholar.org/paper/6f812cd0db7599ecfb21d49c891cfd3176715cb4
[416] A Survey of Latest Trends in Cryptography and Elliptic Curve Cryptography, https://www.semanticscholar.org/paper/890ed3da2522252ed441841a62ea8052ee13087e
[417] Elliptic Curve Cryptograpy, https://www.semanticscholar.org/paper/1a506c12869b12277bf9641032cb9d22a5db5038
[418] Elliptic Curve Cryptography: The Serpentine Course of a Paradigm Shift, https://www.semanticscholar.org/paper/d723bef9fcc0c61f518de126d7ebf66ddc22a111
[419] Elliptic Curve Cryptography: The Next GenerationEncryption Technology for Secure Data Communication, https://www.semanticscholar.org/paper/cc7bd510c83b2e14d455ac0573b3004b29b3be7e
[420] A Survey on Elliptic Curve Cryptography for Pervasive Computing Environment, https://www.semanticscholar.org/paper/06a4387193dde21aac812fec1151113c801c90b8
[421] A Systematic Review of Fast, Scalable, and Efficient Hardware Implementations of Elliptic Curve Cryptography for Blockchain, https://www.semanticscholar.org/paper/d5a3e8e06133d6be24a98855275a8cfc18391399
[422] Overview of Elliptic Curve Cryptography, https://www.semanticscholar.org/paper/0ef580d677d1a8f4d7375d2f459d7b287507bfbc
[423] A SURVEY OF ELLIPTIC CURVE CRYPTOGRAPHY, https://www.semanticscholar.org/paper/95524c068ce1f4bb6dfa73ec9f9c2fb01c74a271
[424] Elliptic Curve Cryptography in Practice, https://www.semanticscholar.org/paper/8174fd9f07c49ea2e19634606965f18c16a72df2
[425] A Study of Elliptic Curve Cryptography and Its Applications, https://www.semanticscholar.org/paper/5c31350a356d0edf875c9db8e026a280e46171e1
[426] Application of Elliptic Curve Crypto System to Secure Multi-Signature Bitcoin Block Chain, https://www.semanticscholar.org/paper/f4114067c719e9621484d43083506c6054eb7769
[427] Elliptic curve lightweight cryptography: A survey, https://ieeexplore.ieee.org/abstract/document/8536394/
[428] A Survey of Security Approaches Based on Elliptic Curve Cryptography, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4817620
[429] A survey of elliptic curves for proof systems, https://link.springer.com/article/10.1007/s10623-022-01135-y
[430] The state of elliptic curve cryptography, https://link.springer.com/article/10.1023/A:1008354106356
[431] A review on elliptic curve cryptography algorithm for Internet of Things: Categorization, application areas, and security, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4683742
[432] EdDSA and Ed25519, https://www.semanticscholar.org/paper/42c8651a93c7b500bf2938d6e82567214684fb76
[433] Size, Speed, and Security: An Ed25519 Case Study, https://www.semanticscholar.org/paper/5a7b238b4b648bb5a7f2b4010c0c90a244099999
[434] Ed25519 for DNSSEC, https://www.semanticscholar.org/paper/3aa9bfd5d10f9aaf5f20cdf484c5fb14629aad17
[435] SommerEngineering/Ed25519: Release 1.0.2, https://www.semanticscholar.org/paper/5b0ff6eb97995f0b61544cd70f684c512b8970a1
[436] Ed25519 public key algorithm for the Secure Shell (SSH) protocol, https://www.semanticscholar.org/paper/fba0d807767af5695d0faf6d36119903b00257c6
[437] Ethereum Use Cases, https://www.semanticscholar.org/paper/51482daec544338374224d37b3173df21eb5db18
[438] Taming the many EdDSAs, https://www.semanticscholar.org/paper/e7092ff079e8780e39981474042aaaaab4964043
[439] poqeth: Efficient, post-quantum signature verification on Ethereum, https://www.semanticscholar.org/paper/8b6857d0aacaae4b61923a5a4a9ef36a3c3dbf37
[440] Using Ed25519 in SSHFP Resource Records, https://www.semanticscholar.org/paper/0f3fdfef58bcb903f6cec8784a0888808f46e32b
[441] A Hierarchical Deterministic Wallet Using Ed25519 Digital Signature Scheme, https://www.semanticscholar.org/paper/f9e2d1ee63dde9ca1c4a534aefb03fa8f4be92ca
[442] Threshold Signatures Using Ed25519 and Ed448, https://www.semanticscholar.org/paper/c9041be632aed7a0ac2ff6a4d9c05e760a3aeff7
[443] Two-Party ECDSA from Hash Proof Systems and Efficient Instantiations, https://www.semanticscholar.org/paper/3c228e72f1a1e4b5c279dc4c0249d51555987add
[444] The Provable Security of Ed25519: Theory and Practice, https://www.semanticscholar.org/paper/cd7cdb27040cad5ab5eaf8c4b4b6ecae18484064
[445] Design and Implementation of an Ed25519 coprocessor, https://www.semanticscholar.org/paper/6fbc7d953d0569b1e9a900b69e909029d5a617e6
[446] Ethereum identity management system, https://www.semanticscholar.org/paper/5416f0e2e48ba85d79f807d36357b2600fde5eb5
[447] Breaking ed25519 in wolfssl, https://link.springer.com/chapter/10.1007/978-3-319-76953-0_1
[448] Implementation of EdDSA in the Ethereum Blockchain, https://link.springer.com/chapter/10.1007/978-3-031-66222-5_16
[449] Compact and flexible FPGA implementation of Ed25519 and X25519, https://dl.acm.org/doi/abs/10.1145/3312742
[450] Fastcrypto: Pioneering cryptography via continuous benchmarking, https://dl.acm.org/doi/abs/10.1145/3629527.3652266
[451] Decentralized digital identity wallet using principles of self-sovereign identity applied to blockchain, https://ieeexplore.ieee.org/abstract/document/10054286/
[452] \u7528\u4e00\u4e2a\u4f8b\u5b50\u8bf4\u8bf4\u96f6\u77e5\u8bc6\u8bc1\u660e - \u77e5\u4e4e\u4e13\u680f, https://zhuanlan.zhihu.com/p/55318827
[453] \u4ec0\u4e48\u662f\u96f6\u77e5\u8bc6\u8bc1\u660e\uff0c\u5982\u4f55\u5b88\u62a4Web3\u9690\u79c1\uff1f|Tokenview - \u767b\u94fe\u793e\u533a, https://learnblockchain.cn/article/5233
[454] \u4ec0\u4e48\u662f\u96f6\u77e5\u8bc6\u8bc1\u660e? (ZKP), https://learn.backpack.exchange/zh/articles/what-are-zero-knowledge-proofs
[455] \u4ec0\u4e48\u662f\u96f6\u77e5\u8bc6\u8bc1\u660e\uff1f - Gate.com, https://www.gate.com/zh/learn/articles/what-are-zero-knowledge-proofs/1229
[456] \u8be6\u7ec6\u8bb2\u89e3\uff1a\u96f6\u77e5\u8bc6\u8bc1\u660e\u4e4bzk-SNARK \u5f00\u7bc7- \u6307\u5c16\u4e0b\u7684\u5e7d\u7075- \u535a\u5ba2\u56ed, https://www.cnblogs.com/linguanh/p/10892344.html
[457] \u533a\u5757\u94fe\uff1a\u96f6\u77e5\u8bc6\u8bc1\u660e\uff0c\u9690\u79c1\u4ea4\u6613\u5b9e\u73b0\uff1f \u539f\u521b - CSDN\u535a\u5ba2, https://blog.csdn.net/weixin_44161914/article/details/153414269
[458] \u96f6\u77e5\u8bc6\u8bc1\u660e\u6982\u8ff0 - MAP Protocol, https://www.mapprotocol.io/zh/article?id=zero-knoeledge-proofs
[459] \u96f6\u77e5\u8b58\u8b49\u660e\u539f\u7406\uff1f\u7279\u6027\u8207\u985e\u578b\u4ecb\u7d39/\u5e38\u898b\u61c9\u7528/\u5132\u5099\u8b49\u660e\u67e5\u8a62\u7bc4\u4f8b, https://rich01.com/zero-knowledge-proof-zkp/
[460] \u96f6\u77e5\u8bc6\u8bc1\u660e\u6982\u5ff5\u53ca\u5176\u5bf9\u533a\u5757\u94fe\u7684\u5f71\u54cd - Binance, https://www.binance.com/zh-CN/academy/articles/what-is-zero-knowledge-proof-and-how-does-it-impact-blockchain
[461] Zcash\u66b4\u6f32700%\u80cc\u5f8c\uff1a\u96b1\u79c1\u6558\u4e8b\u5982\u4f55\u91cd\u71c3\u52a0\u5bc6\u5e02\u5834 - \u9245\u4ea8\u7db2, https://m.cnyes.com/news/id/6217769
[462] 2025\u5e74\u7684L2\u5bf9\u51b3\uff1a\u4e50\u89c2\u5377\u4e0eZK\u5377 - MEXC Blog, https://blog.mexc.com/zh-hans/the-l2-showdown-optimistic-vs-zk-rollups-in-2025/
[463] \u9690\u79c1\u5e01\u5927\u6da8\u80cc\u540e\uff1a\u6619\u82b1\u4e00\u73b0\u8fd8\u662f\u66d9\u5149\u6765\u4e34\uff1f - FastBull, https://m.fastbull.com/cn/news-detail/4352483_1
[464] \u96b1\u79c1\u5e63\u5927\u6f32\u80cc\u5f8c\uff1a\u66c7\u82b1\u4e00\u73fe\u9084\u662f\u66d9\u5149\u4f86\u81e8\uff1f - FX168\u8d22\u7ecf, https://news.fx168news.com/cooperate/2511/7388749.shtml
[465] \u79d1\u666e\uff5czk-SNARKs\u662f\u4ec0\u9ebc\uff1fV\u795e\u5b9a\u8abf\u96f6\u77e5\u8b58\u8b49\u660e\u672a\u4f86\u5341\u5e74\u300c\u975e\u5e38\u91cd\u8981\u300d, https://www.blocktempo.com/zk-snarks-will-be-important-as-the-blockchain/
[466] \u4ec0\u4e48\u662fNamada\uff08NAM\uff09\u4ee5\u53ca\u5b83\u4e3a\u4f55\u6210\u4e3a\u6ce8\u91cd\u9690\u79c1\u7684\u52a0\u5bc6\u8d27\u5e01\u65b0\u661f\uff1f, https://xtsupport.zendesk.com/hc/zh-cn/articles/48238049322265-%E4%BB%80%E4%B9%88%E6%98%AF-Namada-NAM-%E4%BB%A5%E5%8F%8A%E5%AE%83%E4%B8%BA%E4%BD%95%E6%88%90%E4%B8%BA%E6%B3%A8%E9%87%8D%E9%9A%90%E7%A7%81%E7%9A%84%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E6%96%B0%E6%98%9F
[467] \u9690\u79c1\u5e01\u73b0\u5728\u5f88\u70ed\u95e8\uff0c\u4f46\u54ea\u4e00\u4e2a\u4f1a\u6301\u7eed\u4e0b\u53bb\uff1f, https://www.mpost.io/zh-CN/privacy-coins-are-hot-right-now-but-which-one-will-stick-around/
[468] \u4e3a\u4ec0\u4e48\u7eb3\u74e6\u5c14\u8bf4\uff1aZCash\u662f\u9488\u5bf9\u6bd4\u7279\u5e01\u9690\u79c1\u7684\u4fdd\u9669\uff1f - Binance, https://www.binance.com/zh-CN/square/post/31920323721042
[469] \u96f6\u77e5\u8bc6\u8bc1\u660e\uff1a\u4ee5\u592a\u574a\u7684\u672a\u6765| \u767b\u94fe\u793e\u533a| \u533a\u5757\u94fe\u6280\u672f\u793e\u533a, https://learnblockchain.cn/article/7921
[470] \u96f6\u77e5\u8bc6\u8bc1\u660e\u4e0e\u9690\u79c1\u589e\u5f3a - \u77e5\u4e4e\u4e13\u680f, https://zhuanlan.zhihu.com/p/1950848293023232716
[471] \u96f6\u77e5\u8bc6\u8bc1\u660e\uff1a\u5e94\u7528\u548c\u5177\u4f53\u7528\u4f8b - \u767b\u94fe\u793e\u533a, https://learnblockchain.cn/article/5786
[472] \u7814\u62a5\u5fc5\u8bfb\uff1a\u533a\u5757\u94fe\u53d1\u5c55\u53f2\u7684\u7b2c\u4e09\u5927\u6280\u672f\u9769\u65b0\u2014\u2014 \u96f6\u77e5\u8bc6\u8bc1\u660e\u6280\u672f\u5e94\u7528, https://web3caff.com/archives/71780
[473] \u533a\u5757\u94fe\u6280\u672f\u5728\u7f51\u7edc\u5b89\u5168\u9886\u57df\u7684\u521b\u65b0\u5e94\u7528\u539f\u521b - CSDN\u535a\u5ba2, https://blog.csdn.net/m0_71322636/article/details/144806599
[474] \u4e00\u79cd\u57fa\u4e8e\u96f6\u77e5\u8bc6\u8bc1\u660e\u7684\u4eba\u8138\u8bc6\u522b\u9690\u79c1\u4fdd\u62a4\u8eab\u4efd\u8ba4\u8bc1\u65b9\u6cd5 - Google Patents, https://patents.google.com/patent/CN114598479A/zh
[475] 2025.ip \U0001f54a\ufe0f on X: "Humanity Protocol \u662f\u4e00\u4e2a\u57fa\u4e8e\u533a\u5757\u94fe\u7684\u53bb\u4e2d\u5fc3\u5316 ..., https://twitter.com/Darkwjq/status/1926282519424405545
[476] \u533a\u5757\u94fe\u5982\u4f55\u9632\u6b62\u6b3a\u8bc8\u6027\u4ea4\u6613 - \u963f\u91cc\u4e91\u5f00\u53d1\u8005\u793e\u533a, https://developer.aliyun.com/article/1642329
[477] \u6570\u5b57\u8d4b\u80fd\u7b51\u9632\u7ebf\uff1a\u94f6\u884c\u79d1\u6280\u53cd\u8bc8\u5b88\u62a4\u7fa4\u4f17\u201c\u94b1\u888b\u5b50\u201d, https://www.cebnet.com.cn/20251028/102997081.html
[478] \u57fa\u4e8e\u533a\u5757\u94fe\u7684\u96f6\u77e5\u8bc6\u4f4d\u7f6e\u8bc1\u660e\u7cfb\u7edf\u8bbe\u8ba1 - \u5b89\u5168\u5185\u53c2, https://www.secrss.com/articles/19453
[479] \u4ea4\u96a3\u9808\u77e5\uc758 \u8a9e\u5f59\uc640 \u7528\u4f8b \u784f\u7a76, https://www.semanticscholar.org/paper/eff83fd681da8fb7d7d951325bec01f37b0909d9
[480] \u97d3\u570b\uc5d0 \uc788\uc5b4\uc11c \u89c0\u5149\uc758 \u6b77\u53f2\u7684 \u610f\u5473 \ubc0f \u7528\u4f8b, https://www.semanticscholar.org/paper/017f73332bee09b5ffc51ebd692a39619642d02d
[481] Zero Knowledge Proofs and Zero Knowledge Proofs and Protocols Protocols, https://www.semanticscholar.org/paper/ea880a45c9210dc3ac5a9f61905090799b706da6
[482] Frequency Dependent Digital Optimal Servo System and Its Application, https://www.semanticscholar.org/paper/08fe7903bef415df83444a00126f4946328dba1c
[483] 6 Zero Knowledge Proofs, https://www.semanticscholar.org/paper/add9fcc98ab2bebc02229d454a664c758c2e82da
[484] Simulation Technic of Transport Test, https://www.semanticscholar.org/paper/3403085d5c7c41ad5b8c74b3fa1a51ac4cab94b8
[485] Coating of Particles with Thin SiC Film Using Plasma CVD Technique, https://www.semanticscholar.org/paper/9929ca391e05b19fb0fda23475cf0b50de6a32ec
[486] Review on Zero-Knowledge Proof Method, https://www.semanticscholar.org/paper/726cb6fcdbec9e63f9ee2f3002fa39889a593bfd
[487] Electroless Nickel Plating-Assortment of Properties and Industrial Uses, https://www.semanticscholar.org/paper/acc88faf43490d191618b71a38a6ffbec086b6f0
[488] Zero-Knowledge Proofs, https://www.semanticscholar.org/paper/65f8db99fb23955ddb6490b9059669b7588da821
[489] \u533a\u5757\u94fe\u91d1\u878d\u573a\u666f\u5e94\u7528\u5206\u6790\u53ca\u4f01\u4e1a\u7ea7\u67b6\u6784\u63a2\u8ba8, https://xbzrb.gdut.edu.cn/article/doi/10.12052/gdutxb.190152?viewType=HTML
[490] \u533a\u5757\u94fe\u7cfb\u7edf\u5b89\u5168\u9632\u62a4\u6280\u672f\u7814\u7a76\u8fdb\u5c55, http://cjc.ict.ac.cn/online/onlinepaper/lad-20243872140.pdf
[491] \u533a\u5757\u94fe\u5b89\u5168\u95ee\u9898\u7814\u7a76\u7efc\u8ff0, http://joces.nudt.edu.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=17815
[492] \u9762\u5411\u533a\u5757\u94fe\u7f51\u7edc\u7684\u5f02\u5e38\u68c0\u6d4b\u65b9\u6cd5\u7efc\u8ff0., https://search.ebscohost.com/login.aspx?direct=true&profile=ehost&scope=site&authtype=crawler&jrnl=10028331&AN=186408470&h=r4MyxkV3B3jJeEtNsz6OwCd5oJ7%2FpWLMXJlR7EV5Wpn0vMhsvJhfQA7u2eHAwJuoRyh%2BGoS7tOU1jn2mD%2FbnEg%3D%3D&crl=c
[493] \u533a\u5757\u94fe\u751f\u6001\u5171\u6027\u5b89\u5168\u98ce\u9669\u5206\u6790\u7efc\u8ff0., https://search.ebscohost.com/login.aspx?direct=true&profile=ehost&scope=site&authtype=crawler&jrnl=2096109X&AN=185234140&h=HpIhy57cMikvzHBDfLCZuKy3fbSqoaaz%2BHJIFnZrL9cSlz4a%2FQNXY9GWQcNa8za4qnE54ExVVb8CLeUUZYAozw%3D%3D&crl=c
[494] Pascal: \u65e0\u9650\u53ef\u6269\u5c55\u7684\u52a0\u5bc6\u8d27\u5e01, https://www.pascalcoin.org/storage/whitepapers/PascalWhitePaperV5_Chinese.pdf
[495] \u8d8a\u5357\u7edf\u8ba1\u6570\u636e\u5e93\u7684\u516b\u5341\u5e74\u901a\u8fc7 SciMath \u9879\u76ee, https://www.semanticscholar.org/paper/073bbceff303d182208d41beb755c35fbd14a3da
[496] zk-SNARKs Analysis and Implementation on Ethereum, https://www.semanticscholar.org/paper/b1c72c598d9954362605f839f6b71a1a53013d17
[497] Servicifying zk-SNARKs Execution for Verifiable Off-chain Computations, https://www.semanticscholar.org/paper/106aea0930dcdd6e1cf7240cba6b500f6db1cb63
[498] Nominees for 2024\u20132025 SEG Board of Directors, https://www.semanticscholar.org/paper/19e53af7923bcd3d0fd308c353864002f4163300
[499] Influenza vaccine for 2024-2025., https://www.semanticscholar.org/paper/d6a5732bee5a673736f5a1b4fe6b49d53c5879c3
[500] Phantom: An Efficient Privacy Protocol Using zk-SNARKs Based on Smart Contracts, https://www.semanticscholar.org/paper/102c86a0768c979ef0a42fe32cc4570754366aed
[501] zk-SNARKs: A Gentle Introduction, https://www.semanticscholar.org/paper/18a17e5f50c43e694c6d9fce5ec565e61cf544a2
[502] Introduction to SNARK, https://www.semanticscholar.org/paper/82fb67d7eeb163dc30185fef5c8a4a4b448db0fd
[503] A Review of zk-SNARKs, https://www.semanticscholar.org/paper/14e6ad33c9aa367292e07217c7ce0f1a7e4187c7
[504] A Systematic Review on ZKP Algorithms for Blockchain: Methods, Use-cases and Challenges, https://www.semanticscholar.org/paper/6b8de14e9a31360c53353e81dac8cf4764fb56ac
[505] Designated-Verifier zk-SNARKs Made Easy, https://www.semanticscholar.org/paper/56c8b96302dbec465f4c4b2cee828e0c561f29e8
[506] Personal Information Management System with Blockchain Using zk-SNARK, https://www.semanticscholar.org/paper/d7ddefcccd4154502b52c4a314c39d3f13411ee8
[507] \u533a\u5757\u94fe\u9690\u79c1\u4fdd\u62a4\u6280\u672f\u7814\u7a76\u8fdb\u5c55., https://search.ebscohost.com/login.aspx?direct=true&profile=ehost&scope=site&authtype=crawler&jrnl=10028331&AN=182542956&h=m%2FsBZSHmdIpsMDseI6S7WYJaN1JlBaU0iS1JmNeE1sKowrkNKsOSeWqSuTM2CG01DMQArwXC5ouLx6iKFNsXxA%3D%3D&crl=c
[508] 5\u5206\u949f\u4e0a\u624b\uff01libsodium\u8de8\u5e73\u53f0\u52a0\u5bc6\u5f00\u53d1\u5b9e\u6218\u6307\u5357 - CSDN\u535a\u5ba2, https://blog.csdn.net/gitblog_01124/article/details/151470763
[509] \u6df1\u5165\u6d45\u51faLibsodium\u52a0\u5bc6\u5e93\uff1a\u5b89\u5168\u7f16\u7a0b\u7684\u5229\u5668 - \u6613\u6e90\u6613\u5f69, https://www.yicaiai.com/news/article/66ece8654ddd79f11a1ee24c
[510] Linux\u4e0b\u52a0\u5bc6\u5e93Libsodium \u4f7f\u7528\u5b9e\u8df5\uff08ip\u76d1\u542c\u3001\u5c01\u88c5\u7684\u52a0\u5bc6\u6d88\u606f, https://blog.csdn.net/chen1415886044/article/details/127950392
[511] \u767e\u79d1\u6807\u7b7e- \u767b\u94fe\u793e\u533a, https://learnblockchain.cn/tags
[512] Performance Benchmarking of Cryptographic Algorithms in ..., https://www.researchgate.net/publication/394876239_Performance_Benchmarking_of_Cryptographic_Algorithms_in_JCA_for_Messaging_Apps
[513] Analysis of Cryptography Algorithms Implemented in ..., https://itc.ktu.lt/index.php/ITC/article/view/29464/15209
[514] Implementing and Optimizing an Encryption Filesystem on ..., https://ieeexplore.ieee.org/document/6341374/
[515] A Performance Study of Crypto-Hardware in the Low-end IoT, https://eprint.iacr.org/2021/058.pdf
[516] RSA-2048 vs ECC-224 : A Detailed Comparison, https://mojoauth.com/compare-encryption-algorithms/rsa-2048-vs-ecc-224/
[517] Optimized Implementation of SM2 Algorithm Based on ..., https://dl.acm.org/doi/10.1145/3675018.3675776
[518] (PDF) Performance scaling of cryptography operations in ..., https://www.researchgate.net/publication/228949776_Performance_scaling_of_cryptography_operations_in_servers_and_mobile_clients
[519] Understanding Web Crypto APIs: A Guide for Developers and Analysts, https://www.tokenmetrics.com/blog/understanding-web-crypto-apis-guide-developers-analysts?0fad35da_page=2&74e29fd5_page=124
[520] API Performance Optimization: Comprehensive Analysis and ..., https://medium.com/@reddyfull/api-performance-optimization-comprehensive-analysis-and-implementation-guide-ecb4100f113f
[521] [PDF] Performance Analysis of SSL/TLS Crypto Libraries, https://bhu.ac.in/research_pub/jsr/Volumes/JSR_66_02_2022/12.pdf
[522] Speed Benchmarks - BearSSL, https://www.bearssl.org/speed.html
[523] [PDF] Cryptographic Performance and Energy Efficiency on SimpleLink ..., https://www.ti.com/lit/pdf/swra667
[524] Measuring the Impact of Encryption on Cloud Storage Latency and ..., https://mihirpopat.medium.com/measuring-the-impact-of-encryption-on-cloud-storage-latency-and-throughput-917460d76302
[525] Cryptographic File Systems Performance: What You Don't Know ..., https://www.filesystems.org/docs/nc-perf/index.html
[526] A comprehensive test framework for cryptographic accelerators in ..., https://www.sciencedirect.com/science/article/abs/pii/S1383762120301533
[527] On Possible Cryptographic Optimization of Mobile Healthcare Application, https://www.semanticscholar.org/paper/0567dee7dd8583b08ba67ff5ebe21c4dda2a6581
[528] PEARL: A PErformance evaluAtor of cRyptographic aLgorithms for Mobile Devices, https://www.semanticscholar.org/paper/c5724e3489d1ad0ae2d97861542bde6673aea4a9
[529] The impact of mobile processor cryptographic acceleration on data transfer, https://www.semanticscholar.org/paper/6be54d9cb7e09885a540debf08130864559a1217
[530] Is the Performance of Smart Card Cryptographic Functions the Real Bottleneck?, https://www.semanticscholar.org/paper/6099103817bde77a628f30ae1a4cf96f97f6dcc1
[531] Optimizing the performance of block encryption algorithms, https://www.semanticscholar.org/paper/fc6aa2f803dd6a7faae3f2455c1cbc9a77c1f421
[532] Portability Evaluation of Cryptographic Libraries on Android Smartphones, https://www.semanticscholar.org/paper/19b33b3a92453e17d50893f0ced85126caa2fff9
[533] Security and Network Performance Evaluation of KK' Cryptographic Technique in Mobile Adhoc Networks, https://www.semanticscholar.org/paper/e89ea540fa181fc73b4420a7622da80ef8828beb
[534] Evaluation of Static Vulnerability Detection Tools With Java Cryptographic API Benchmarks, https://www.semanticscholar.org/paper/ef3e139418289eafa4eb6ba5671901ab426196e3
[535] Host cryptographic operations: A software implementation, https://www.semanticscholar.org/paper/0cfba203c9baa55cfe53680c46c971846bcb8f29
[536] Linux BYTEmark Benchmarks: A Performance Comparison of Embedded Mobile Processors, https://www.semanticscholar.org/paper/f8a48372d8f37b44f2408f4f15325e248a31ad82
[537] Table 5: The execution time of different cryptographic operations., https://www.semanticscholar.org/paper/15c4b473c1344166749878baab6797be07fe6cda
[538] Performance Analysis of Route Optimization on Proxy Mobile IPv6, https://www.semanticscholar.org/paper/d3fc2426e58b1fa99a4651378c5b4b44b9fe6c3f
[539] High Performance Agile Crypto Modules, https://www.semanticscholar.org/paper/9b834edbc45762b4b1a505496d9d133272e52869
[540] CRYPTRON: CRYptographic Prefixes for Route Optimization in NEMO, https://www.semanticscholar.org/paper/cfa74ffc82fa8242843f78defeea330a7a7f6c2c
[541] Cryptographic algorithm benchmarking in mobile devices, https://oulurepo.oulu.fi/handle/10024/39404
[542] A survey of performance optimization for mobile applications, https://ieeexplore.ieee.org/abstract/document/9397392/
[543] Benchmarking message authentication code functions for mobile computing, https://ieeexplore.ieee.org/abstract/document/6503506/
[544] Performance evaluation of cryptographic algorithms over IoT platforms and operating systems, https://onlinelibrary.wiley.com/doi/abs/10.1155/2017/2046735
[545] Analysis of cryptography algorithms implemented in android mobile application, https://www.itc.ktu.lt/index.php/ITC/article/view/29464
[546] Performance analysis of cryptographic protocols on handheld devices, https://ieeexplore.ieee.org/abstract/document/1347774/
[547] Security Analysis of the W3C Web Cryptography API, https://www.semanticscholar.org/paper/53496f2da138666c0cd3493c8d29a3299e7f8656
[548] Optimization strategies based on algorithm for queue scheduling model and applications of web frontend performance, https://www.semanticscholar.org/paper/69564cf4891d12953f6c81e5a3610d342292b624
[549] Automated Hotfixes for Misuses of Crypto APIs, https://www.semanticscholar.org/paper/05e45859a2258d212cd5f302af5698744ff3984c
[550] JavaScript Web Cryptography API, https://www.semanticscholar.org/paper/d95b1b4d016e2b16034069f3ffafa8abddc6d253
[551] A Performance Analysis of the Web Services Solution and Its Optimization Strategies, https://www.semanticscholar.org/paper/6ef1d45dba867fc09219ef8903799cb42f191390
[552] Improving OpenSSL* performance white paper, https://www.semanticscholar.org/paper/b725016a4e7b7fa0cb4b334f6e185c3479fd3b9b
[553] Inferring crypto API rules from code changes, https://www.semanticscholar.org/paper/bc6b43a07400ca859c824c014cf8af746c644d09
[554] Portable and Efficient Implementation of CRYSTALS-Kyber Based on WebAssembly, https://www.semanticscholar.org/paper/7ffe3d24a778c82043bca3c0a3c0b83d4eebf9f5
[555] Detection method and detection system of crypto module application program interface (API) safety, https://www.semanticscholar.org/paper/e69979115143b2bfa0596fba819c08c34f8f5858
[556] Development and Examination of In-browser GPU Accelerated Cryptography, https://www.semanticscholar.org/paper/978299c04280a78a8c10356057c3cf967d4c38f9
[557] CryptoShield - Automatic On-Device Mitigation for Crypto API Misuse in Android Applications, https://www.semanticscholar.org/paper/cb85be0d36fd907dee3bea7683f4d42278426cd5
[558] Acceleration of cryptographic, https://www.semanticscholar.org/paper/37caab1b56fc2b381dbb4e07d7f872a1d3eb26a6
[559] Accelerating AES Algorithm using WebGPU, https://www.semanticscholar.org/paper/f566052ce01ec81bfdda2c55b28831231a3a32d8
[560] Cryptographic APIs, https://www.semanticscholar.org/paper/2dff0c080eb584ab0daf34c42eaed8ce927e88af
[561] Innovative cryptocurrency trade websites' marketing strategy refinement, via digital behavior, https://ieeexplore.ieee.org/abstract/document/9794782/
[562] Modern web performance optimization, https://link.springer.com/content/pdf/10.1007/978-1-4842-6528-4.pdf
[563] Benchmarking web api quality-revisited, https://ieeexplore.ieee.org/abstract/document/10247284/
[564] Front-End Performance Optimization for Next-Generation Digital Services, https://al-kindipublishers.org/index.php/jcsts/article/view/9723
[565] An analysis of techniques and quality assessment for Web performance optimization, https://drshailesh.in/wp-content/uploads/2020/04/an-analysis-of-techniques.pdf
[566] Performance benchmarking and optimization for blockchain systems: A survey, https://link.springer.com/chapter/10.1007/978-3-030-23404-1_12
[567] The automatic cryptocurrency trading system using a scalping strategy, https://ela.kpi.ua/items/0e4f11a0-e184-4c30-bd36-0d78ade18c85
[568] Assessing WebSocket protocol performance for real-time cryptocurrency algorithmic trading with compiled, intermediate and interpreted programming�\u2026, http://www.praguecityuniversity.cz/hubfs/Students-degree-projects/Martin_Papik_WebSocket_Protocol.pdf
[569] Optimizing Web Performance and Computational Efficiency: A Deep Dive into WebAssembly's Technical Advancements and Real-World Applications, https://www.researchgate.net/profile/Son-Nguyen-386/publication/389517325_Optimizing_Web_Performance_and_Computational_Efficiency_A_Deep_Dive_into_WebAssembly's_Technical_Advancements_and_Real-World_Applications/links/67c62ce1207c0c20faa03019/Optimizing-Web-Performance-and-Computational-Efficiency-A-Deep-Dive-into-WebAssemblys-Technical-Advancements-and-Real-World-Applications.pdf
[570] Runtime verification of crypto apis: an empirical study, https://ieeexplore.ieee.org/abstract/document/10225251/
[571] CMC (Certificate Management over Cryptographic Message Syntax) Extensions: Server-Side Key Generation, https://www.semanticscholar.org/paper/fd7a9f5a6a10c3a83668a213b64d6574824cb506
[572] List of 16 MPC Wallets on Multichain (2025) - Alchemy, https://www.alchemy.com/dapps/list-of/mpc-wallets-on-multichain
[573] MPCVault | MPC-Multisig crypto wallet for teams, https://mpcvault.com/
[574] 13 Best Multi-Chain Web3 Wallets: Ultimate Guide - Yellow.com, https://yellow.com/en-US/learn/13-best-multi-chain-web3-wallets-ultimate-guide
[575] Top Open-Source MPC Wallets You Should Try in 2025 - Safeheron, https://safeheron.com/blog/top-mpc-wallet-open-source-options-2025/
[576] What is MPC (Multi-Party Computation)? Crypto wallets & Web3, https://www.cube.exchange/what-is/mpc-multi-party-computation
[577] Top 10 Bitcoin Wallets - QuickNode, https://www.quicknode.com/builders-guide/best/top-10-bitcoin-wallets
[578] Best Crypto Wallets of November 2025 (Google Ratings) - Tangem, https://tangem.com/en/blog/post/best-crypto-wallets/
[579] MPC vs. Multi-sig: Choosing the Right Wallet Security for Your ..., https://www.cobo.com/post/mpc-vs-multi-sig-choosing-the-right-wallet-security
[580] Best Wallet Aims to Solve Crypto's Multi-Chain Problem With One ..., https://techpoint.africa/cryptoexplorer/2025/10/21/cryptos-multi-chain-chaos-needs-a-solution-best-wallet-says-its-building-the-one-stop-fix/
[581] Architecture for Stablecoins with Cross-Chain Interoperability, https://www.semanticscholar.org/paper/a002bfed1e082e74fc98d57abead724daeb08e56
[582] Towards an information architecture to enable cross chain control centers, https://www.semanticscholar.org/paper/db6099b920a94eeaeab5dff027a295a9733fa350
[583] Cross-chain Architecture of Blockchain Integrating Notary Mechanism and Relay-chain Technology, https://www.semanticscholar.org/paper/6f64224587ef03e9423fa0bdb716148bb389beeb
[584] A review of blockchain cross-chain technology, https://www.semanticscholar.org/paper/5abfa8efc0853d67d18277b125b8f02f77c98a5f
[585] A Cross-Chain Protocol Based on Main-SubChain Architecture, https://www.semanticscholar.org/paper/90e1cd986d004dfc8bb40f755926648ef1588079
[586] Resilient Gateway-Based N-N Cross-Chain Asset Transfers, https://www.semanticscholar.org/paper/6370918fa4e86521e467e560b1114f9da269843b
[587] Atomic Crosschain Transactions for Ethereum Private Sidechains, https://www.semanticscholar.org/paper/9a0889a3fd116595a697a180c852817de5caaa50
[588] A Review of Cross-Blockchain Solutions, https://www.semanticscholar.org/paper/3ed0bc31923b2f81c8f5cd69c59dcb5bd7357d98
[589] The impacts of the cross-chain collaboration center model on transportation performance: A case study of a bulk transportation network in Thailand, https://www.semanticscholar.org/paper/feff2886269022a6da174b934d7c65cf37f61863
[590] Survey of crosschain communications protocols, https://www.semanticscholar.org/paper/2def280e140c4a11975f1772ea01a9797055eb4e
[591] Cross-chain General Message Passing Protocol via Eternal Bridge, https://www.semanticscholar.org/paper/b4e6310f7ae5d23156c959a3b46cda54a2f9197e
[592] HyperLoop: Rationally secure efficient cross-chain bridge, https://www.semanticscholar.org/paper/15a3561b29b3707129d2b64f687f8b15093eb75b
[593] An Empirical Study of Cross-Chain Arbitrage in Decentralized Exchanges, https://www.semanticscholar.org/paper/c614652c268d1a92ef59c4dab6fe1889f435c101
[594] Decoding Cross-Chain Interoperability, https://www.semanticscholar.org/paper/783b962b85eba95e5222ded0da79d16e14aae5b7
[595] Subscription-Based State Access for Cross-Chain Smart Contracts, https://www.semanticscholar.org/paper/22782c610d9c9ddac7fe3d874f17781572d75e21
[596] Towards Blockchain Interoperability: A Comprehensive Survey on Cross-Chain Solutions, https://www.semanticscholar.org/paper/689a524a14554a2e44b71916bad31986d8f2ce3a
[597] Cross-Chain Blockchain Networks, Compatibility Standards, and Interoperability Standards, https://www.semanticscholar.org/paper/a867512a3f1fe92b12b493827f5a9fb199adcdab
[598] An overview on cross-chain: Mechanism, platforms, challenges and advances, https://www.semanticscholar.org/paper/a540736b33c9418a134454d3f434222895585999
[599] A survey on cross-chain technology: Challenges, development, and prospect, https://ieeexplore.ieee.org/abstract/document/9982450/
[600] Omni Vault: A Next-Generation Key Management and Multi-Chain Wallet, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5193783
[601] Cross-chain digital asset system for secure trading and payment, https://ieeexplore.ieee.org/abstract/document/10040561/
[602] CrossChannel: Efficient and scalable cross-chain transactions through cross-and-off-blockchain micropayment channel, https://ieeexplore.ieee.org/abstract/document/10552402/
[603] A study of blockchain-based liquidity cross-chain model, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0302145
[604] Comparison of TON, Solana and Ethereum 2.0, https://www.semanticscholar.org/paper/26fe40cd990f43a7922434e426f87d3d57246172
[605] Universal Wallets, https://www.semanticscholar.org/paper/3d1c75469a2f1e7ac47205e54591dec84ee39cb3
[606] Onchain Analysis: A Comparative Study of Decentralized Exchange (DEX) Activities on Ethereum, Solana, and Binance Smart Chain (BSC), https://www.semanticscholar.org/paper/c8415a97c749a7dcb0f31510a96b269717c7b9c6
[607] POLKADOT: VISION FOR A HETEROGENEOUS MULTI-CHAIN FRAMEWORK, https://www.semanticscholar.org/paper/f76f652385edc7f49563f77c12bbf28a990039cf
[608] A Comprehensive Analysis of Transaction Speeds, Costs, and Real-World Applications of Solana, Ethereum, and SUI, https://www.semanticscholar.org/paper/d049e2cf6d73450a90da44b167e6c4aa5bbd9c37
[609] Defi integrated blockchain wallet with automated transactions, https://www.semanticscholar.org/paper/40ece73be00bb0e03506b8176a0d17fbd1a84a5c
[610] Characteristics of Wallet Contracts on Ethereum, https://www.semanticscholar.org/paper/d12a2b7cc93c96295adf4c9d36bbbbb104b46101
[611] Wallets, https://www.semanticscholar.org/paper/a6d86a5fa0f24e1e5cecdbfc6259cca7adac962a
[612] Ethereum sendtransaciton(EIP-155) - Stack Overflow, https://stackoverflow.com/questions/72267192/ethereum-sendtransacitoneip-155
[613] Signing transactions send to Quorum permissioned blockchain #162, https://github.com/ethers-io/ethers.js/issues/162
[614] EIP idea: eth_signUserOperation RPC - Ethereum Magicians, https://ethereum-magicians.org/t/eip-idea-eth-signuseroperation-rpc/16184
[615] How to sign Ethereum EIP-1559 transactions using AWS KMS, https://aws.amazon.com/blogs/database/how-to-sign-ethereum-eip-1559-transactions-using-aws-kms/
[616] EIP-695: Create `eth_chainId` method for JSON-RPC, https://ethereum-magicians.org/t/eip-695-create-eth-chainid-method-for-json-rpc/1845
[617] only replay-protected (EIP-155) transactions allowed over RPC, https://ethereum.stackexchange.com/questions/136026/getting-error-only-replay-protected-eip-155-transactions-allowed-over-rpc-wh
[618] Transactions - Bitcoin.org, https://developer.bitcoin.org/devguide/transactions.html
[619] Operator roles: Life stages in the saga of a PSBT - Unchained Capital, https://www.unchained.com/blog/operator-roles-life-stages-in-the-saga-of-a-psbt
[620] BIP 174: Partially Signed Bitcoin Transaction Format, https://bips.dev/174/
[621] What Are Partially Signed Bitcoin Transactions (PSBTs)? | River, https://river.com/learn/what-are-partially-signed-bitcoin-transactions-psbts/
[622] BIP 0174 - Bitcoin Wiki, https://en.bitcoin.it/wiki/BIP_0174
[623] Partially signed bitcoin transactions - Bitcoin Optech, https://bitcoinops.org/en/topics/psbt/
[624] Broadcast and confirm signed Solana transaction, https://docs.tatum.io/reference/solanabroadcastconfirm
[625] Signing - Coinbase Developer Documentation, https://docs.cdp.coinbase.com/embedded-wallets/solana-features/signing
[626] Simplifying the Solana Transaction Lifecycle | by Aman Satyawani, https://medium.com/@amansatyawani/simplifying-the-solana-transaction-lifecycle-bad1ade27a22
[627] Transactions | Solana, https://solana.com/docs/core/transactions
[628] How to Send a Transaction On Solana Using JavaScript - QuickNode, https://www.quicknode.com/guides/solana-development/transactions/how-to-send-a-transaction-on-solana-using-javascript
[629] How to Send Solana Transactions - Helius Docs, https://www.helius.dev/docs/sending-transactions/send-manually
[630] Blockchain Nodes, https://www.semanticscholar.org/paper/20df15e4c54cf3bbcb5fb94a7c01a7554279bbb2
[631] Using the Blockchain, https://www.semanticscholar.org/paper/0cb8b348b3ac3dd28b162da60d3701784a2b2cf3
[632] Model-Based Testing Approach for EIP-1559 Ethereum Smart Contracts, https://www.semanticscholar.org/paper/933a453707ec8ec2476e0501c3d963e52e58738f
[633] Attention to the changes in the revised edition of the Standard Conditions of Contract when signing construction contracts, https://www.semanticscholar.org/paper/7b3f626080e71e3159874141e681c2becc91fc43
[634] EthExplorer: A Tool for Forensic Analysis of the Ethereum Blockchain, https://www.semanticscholar.org/paper/1531c6beddc39866143b1342fa5e87253a5e8e1d
[635] Building With Ethereum, https://link.springer.com/content/pdf/10.1007/978-1-4842-9045-3.pdf
[636] Secure High-Rate Transaction Processing in Bitcoin, https://www.semanticscholar.org/paper/728b60c04afb5b87853b59265e49f430dbf631db
[637] BITCOIN \u2013 BENEFITS AND RISKS, https://www.semanticscholar.org/paper/0668bd2b2f0b20f3c3700de1c62a0ea7edd0c1af
[638] Enhancing Bitcoin Security and Performance with Strong Consistency via Collective Signing, https://www.semanticscholar.org/paper/efd99fe3b5b620d89aa03201199c45988c688670
[639] Transaction Characteristics of Bitcoin, https://www.semanticscholar.org/paper/74e0981889aedfdef7d5c389d6fa55bb9809d7b2
[640] Bitcoin Wallets and Transactions, https://www.semanticscholar.org/paper/2db5a940e0d7460871a533ec0a2d675385f7770e
[641] An efficient dynamic transaction storage mechanism for sustainable high-throughput Bitcoin, https://www.semanticscholar.org/paper/cef39000cc8fec8f10ef2eacc59546c4d5e7c104
[642] On the Malleability of Bitcoin Transactions, https://www.semanticscholar.org/paper/c27684f2fe5a85fe2871f693edc46061d0ecb20d
[643] Anatomy and Lifecycle of a Bitcoin Transaction, https://www.semanticscholar.org/paper/cf5bc20d58a75b049d4a74c70a1691410aab50fd
[644] Bitcoin as an Interplanetary Monetary Standard with Proof-of-Transit Timestamping, https://arxiv.org/abs/2508.20591
[645] An analysis of non-standard bitcoin transactions, https://ieeexplore.ieee.org/abstract/document/8525397/
[646] The bitcoin lightning network, https://cryptodeep.ru/doc/The_Bitcoin_Lightning_Network_DRAFT_0.5.pdf
[647] A fair protocol for data trading based on bitcoin transactions, https://www.sciencedirect.com/science/article/pii/S0167739X17318344
[648] The bitcoin lightning network: Scalable off-chain instant payments, https://www.bitcoinlightning.com/wp-content/uploads/2018/03/lightning-network-paper.pdf
[649] Best Protection for Blockchain BIP32 Keys, https://www.fortanix.com/blog/best-protection-for-blockchain-bip32-keys
[650] AWS CloudHSM key management best practices, https://docs.aws.amazon.com/cloudhsm/latest/userguide/bp-hsm-key-management.html
[651] Key Management and use cases for HSMs, https://www.cryptomathic.com/blog/key-management-and-use-cases-for-hsms
[652] 10 Best Practices for Centralized Encryption Key ..., https://cpl.thalesgroup.com/blog/encryption/10-best-practices-for-centralized-encryption-key-management
[653] Best Practices, https://thalesdocs.com/gphsm/luna/7/docs/network/Content/Product_Overview/best_practices_hsms_partitions_clients.htm
[654] Best Practices for Managing Private Keys in Blockchain, https://medium.com/coinmonks/private-key-management-in-blockchain-and-hsm-f74e5c0d5703
[655] Best Practices for Key Wrapping, Storage, and Management, https://dev.ubiqsecurity.com/docs/key-mgmt-best-practices
[656] Cryptographic Key Lifecycle Management 101: Essential ..., https://utimaco.com/news/blog-posts/cryptographic-key-lifecycle-management-101-essential-stages-and-best-practices
[657] Build secure multi-party computation (MPC) wallets using AWS Nitro ..., https://aws.amazon.com/blogs/web3/build-secure-multi-party-computation-mpc-wallets-using-aws-nitro-enclaves/
[658] Blockdaemon Builder Vault Secure MPC Key Management, https://aws.amazon.com/marketplace/pp/prodview-df3uvv72xxtmw
[659] Web3 Wallets | Blockchain Custody And Key Management - Kaleido, https://www.kaleido.io/blockchain-platform/wallets
[660] Secure Digital Assets with Blockdaemon Builder Vault using AWS ..., https://aws.amazon.com/blogs/apn/secure-digital-assets-with-blockdaemon-builder-vault-using-aws-nitro-enclaves/
[661] 10 Examples of Web3 Wallets for Enterprises - Kaleido, https://www.kaleido.io/blockchain-blog/10-examples-of-web3-wallets-for-enterprises
[662] Use Key Management Service (KMS) Etcd Encryption in Azure ..., https://learn.microsoft.com/en-us/azure/aks/use-kms-etcd-encryption
[663] Key Management: The Future of Web3 Security: Podcast Ep. 140, https://www.chainalysis.com/blog/key-management-blockchain-web3-security-ep-140/
[664] Ledger Wallet: The Ultimate Guide to Secure Cryptocurrency Storage, https://www.blog.brightcoding.dev/2025/02/10/ledger-wallet-the-ultimate-guide-to-secure-cryptocurrency-storage/
[665] An Offline Key is the Only Key: How Ledger Wallets Store Private ..., https://www.ledger.com/academy/topics/ledgersolutions/an-offline-key-is-the-only-key-how-ledger-wallets-store-private-keys-offline
[666] What's The Best Way to Store Crypto? - Ledger, https://www.ledger.com/academy/crypto/the-best-way-to-store-your-private-keys-hardware-wallets
[667] Crypto Ledger Wallet: How It Works and Ensuring Security - Gemini, https://www.gemini.com/cryptopedia/crypto-ledger-wallet
[668] How to set up your Ledger hardware wallet, https://www.ledger.com/start
[669] Ledger Nano S Hardware Wallet: Your Guide to Setup & Enhanced ..., https://remitano.com/ke-fa/forum/156167-ledger-nano-s-hardware-wallet-your-guide-to-setup-and-enhanced-security
[670] How Ledger Hardware Wallets Work, https://www.ledger.com/academy/topics/ledgersolutions/how-ledger-hardware-wallets-work
[671] Strengthening Key Management Systems with Dedicated HSM Solution, https://www.semanticscholar.org/paper/b77dffa2181997ac5065f525d5bb69e3b9242164
[672] Private key management: best practice for the enterprise, https://www.semanticscholar.org/paper/ca01a5cf63fb331bc021ce6efc4d7ca739743be9
[673] Demonstration of Secure Key Management Solution with Use Case in Permissioned Blockchain, https://www.semanticscholar.org/paper/0020c46505c0549f12695d4c78b1ca1329ea2ae9
[674] Key management for blockchain technology, https://www.semanticscholar.org/paper/f3afa910e52764005fe93d3b6614106bf0c30746
[675] Recommendation for Key Management - Part 2: Best Practices for Key Management Organization, https://www.semanticscholar.org/paper/b9a1e049e03a46b2797ccedc90f107ddd54256d4
[676] Hardware Security Module (HSM), https://www.semanticscholar.org/paper/73f81b9c6c99de75282d2935f58f15eefd44f569
[677] The Key Functions and Best Practices of Software Product Management, https://www.semanticscholar.org/paper/3eb9d043fc6dc113185427350af242cc0e2f590b
[678] Key Management \u2014 Fundamentals, https://www.semanticscholar.org/paper/60433172a0c200d69a0e7a592b2bbb0e24f4182a
[679] BEST PRACTICES IN PLANT AND VEHICLE MANAGEMENT, https://www.semanticscholar.org/paper/4a6f1f5033bbd22ecc47feb94d8bd21377ccc47c
[680] Best Practices in Business Technology Management, https://www.semanticscholar.org/paper/bd170e0e2aaa0bc14c64e0dee97852dd1f6308e9
[681] Storing and Retrieving Secrets on a Blockchain, https://www.semanticscholar.org/paper/532a0b7bc979f1d116eb1351353675905359147d
[682] Best Practices for Reverse Logistics Management, https://www.semanticscholar.org/paper/4f1bd3d344a9d29b4d1469432535ad2094aa5c56
[683] Management of cyptographic keys, https://www.semanticscholar.org/paper/aba58e19ecd9f05c98aa8e01254a7e19baf8c8a5
[684] A Financial Strategy For Configuration And Management Of A DFSMSHSM Environment, https://www.semanticscholar.org/paper/6121a1d5d2b8f4070c439b4fcc400eace9037d8d
[685] Virtual and Distributed Hardware Security Module for Secure Key Management, https://repositorio.ulisboa.pt/bitstreams/1a726aea-cb11-446f-9fd7-dc1b5eacb4a8/download
[686] A TECHNICAL PAPER ON KEY MANAGEMENT, https://www.researchgate.net/profile/Halimah-Abdul-Azeez/publication/388397607_CRYPTOGRAPHIC_KEY_MANAGEMENT/links/67964c5b207c0c20fa5c51e8/CRYPTOGRAPHIC-KEY-MANAGEMENT.pdf
[687] The study of the HSM as a solution to file encryption and security., https://ceur-ws.org/Vol-3402/paper10.pdf
[688] A Comparative Analysis of AWS and Azure in the Context of Blockchain Technology, https://www.semanticscholar.org/paper/798c8defb9d77a3f8af1d44550fd6f64d99f4b65
[689] Optimized Key Recovery for Blockchain Wallets in Sustainable Supply Chains, https://www.semanticscholar.org/paper/eb7188b29b1af35495248c34afa9d393ae9b535f
[690] Singularity Blockchain Key Management via non-custodial key management, https://www.semanticscholar.org/paper/8277b158df1479083652987e0cd2811f4f9e5d2e
[691] Encryptr - A free, open source password manager and e-wallet. Zero-knowledge. Cloud-based. Private., https://www.semanticscholar.org/paper/6dc0af97460c2d2c992e35dce0a648dcea9dce19
[692] 32GB #AWS #Glacier Vault l�schen. Mit 3rd-Party-Tool ..., https://www.semanticscholar.org/paper/8199ef443e5596af17c56a3e6492635b7b3985a4
[693] Governance for Azure and AWS Cloud Services, https://www.semanticscholar.org/paper/9d49940a9b1beb4a8dc2e8e6729a86aeb0daea76
[694] Blockchain Wallets in Health care systems, https://www.semanticscholar.org/paper/923800f5cf357d48dbb8d54a379fe1a3dd427cf4
[695] Azure Versus AWS: A Deep Dive into Cloud Innovation and Strategy, https://www.semanticscholar.org/paper/76df8cd47ba2b8e7b6edea2ddb2812f0dd7dbe19
[696] A decentralized service for personal data privacy protection, https://scholars.csus.edu/view/pdfCoverPage?instCode=01CALS_USL&filePid=13232657100001671&download=true
[697] DOCKERISED BLOCKCHAIN ARCHITECTURE OVERVIEW, https://repository.kpi.kharkov.ua/server/api/core/bitstreams/08c00bca-e21c-4cfb-bcb7-b8a6e1fb3733/content#page=437
[698] How to Develop MPC Wallet: A Step-by-Step Guide - Safeheron, https://safeheron.com/blog/how-to-develop-mpc-wallet/
[699] MPC Wallets: Complete Developer Guide 2025 - Alchemy, https://www.alchemy.com/overviews/what-is-a-multi-party-computation-mpc-wallet
[700] A Bridge between Blockchain and Decentralized Applications Web3 and Non-Web3 Crypto Wallets, https://www.semanticscholar.org/paper/e23a192da64edefb279c3e021afbc06f66b0baa4
[701] Simple Schnorr multi-signatures with applications to Bitcoin, https://www.semanticscholar.org/paper/a4da14a4329d7bf28e2ecbf9a3e42bf1faba523e
[702] Understanding Merkle Trees: Enhancing Blockchain Efficiency and ..., https://www.investopedia.com/terms/m/merkle-tree.asp
[703] Merkle Tree in Crypto: What it is and How it Works? - Atomic Wallet, https://atomicwallet.io/academy/articles/what-is-merkle-tree
[704] Merkle Trees: Building Blocks of Blockchain Trust - Lightspark, https://lightspark.com/glossary/merkle-tree
[705] How are Merkle trees used in blockchains? | Alchemy Docs, https://www.alchemy.com/docs/merkle-trees-in-blockchains
[706] Merkle Trees | Cryptocurrency & Blockchain Technology, https://freemanlaw.com/merkle-trees-2/
[707] Merkle Tree in Blockchain: What is it, How does it work and Benefits, https://www.simplilearn.com/tutorials/blockchain-tutorial/merkle-tree-in-blockchain
[708] What is Merkle tree in Blockchain? And how it works - CoinTracker, https://www.cointracker.io/learn/merkle-tree
[709] Blockchain Merkle Trees - GeeksforGeeks, https://www.geeksforgeeks.org/software-engineering/blockchain-merkle-trees/
[710] Understanding Merkle Trees and Proofs | by Mike Dyne | Evendyne, https://medium.com/evendyne/understanding-merkle-trees-and-proofs-5eca62ba3e83
[711] What Is a Merkle Tree in Blockchain? - Chiliz, https://www.chiliz.com/what-is-a-merkle-tree-in-blockchain/
[712] BAHS: A Blockchain-Aided Hash-Based Signature Scheme, https://dl.acm.org/doi/10.1007/978-981-99-7032-2_25
[713] [PDF] CAPE: Commitment-based Privacy-Preserving Payment Channel ..., https://orbit.dtu.dk/files/394170270/CAPE_Commitment-based_Privacy-Preserving_Payment_Channel_Scheme_in_Blockchain.pdf
[714] Commitment scheme - Wikipedia, https://en.wikipedia.org/wiki/Commitment_scheme
[715] [PDF] SmallWood: Hash-Based Polynomial Commitments and Zero ..., https://eprint.iacr.org/2025/1085.pdf
[716] Commitment schemes - Medium, https://medium.com/@icostan/commitment-schemes-8b523d48aa1e
[717] Post-Quantum Linkable Hash-Based Ring Signature Scheme for Off ..., https://pmc.ncbi.nlm.nih.gov/articles/PMC12298650/
[718] Hash-Based Signature Schemes for Post-Quantum Bitcoin, https://conduition.io/cryptography/quantum-hbs/
[719] Hash-Based Multi-Signatures for Post-Quantum Ethereum - HackMD, https://hackmd.io/@tcoratger/S1t-qhPFJx
[720] Verifying Zipwire's Merkle Root Attestations for Developers, https://docs.zipwire.io/fundamentals/security/wallet-verification-guide/verifying-zipwires-merkle-root-attestations-for-developers
[721] What is a Merkle Proof? - NMKR, https://www.nmkr.io/glossary/merkle-proof
[722] How is a merkle tree with proofs better than just signing a bunch of ..., https://forum.openzeppelin.com/t/how-is-a-merkle-tree-with-proofs-better-than-just-signing-a-bunch-of-transactions/7894
[723] Merkle proof standardised format - Bitcoin SV Technical Standards, https://tsc.bsvblockchain.org/standards/merkle-proof-standardised-format/
[724] Merkle Root | A Fingerprint for the Transactions in a Block, https://learnmeabitcoin.com/technical/block/merkle-root/
[725] Deep dive into Merkle proofs and eth_getProof - Chainstack, https://docs.chainstack.com/docs/deep-dive-into-merkle-proofs-and-eth-getproof-ethereum-rpc-method
[726] Covers the basic airdrop contract by integratin the merkle trees and ..., https://github.com/anuragShingare30/Merkle_Airdrop_Protocol
[727] The true reason bitcoin needs merkle proof for SPV wallet?, https://bitcoin.stackexchange.com/questions/114078/the-true-reason-bitcoin-needs-merkle-proof-for-spv-wallet
[728] Design and Implementation of Visual Blockchain With Merkle Tree, https://www.semanticscholar.org/paper/f9bec3142ebfd36e8f714843c15aa0959ef851b4
[729] Visual blockchain using Merkle Tree, https://www.semanticscholar.org/paper/cfb01712531a66e51373964aa130fde20060c494
[730] Cartesian Merkle Tree, https://www.semanticscholar.org/paper/51ca4e0113b2009fe672eb73790dec47b56a7258
[731] Merkle Trees, https://www.semanticscholar.org/paper/05f1b578c1d2accea11188f3f52d77f21b1bc2d2
[732] Voter Verification in an Election Using Merkle Tree, https://www.semanticscholar.org/paper/8d522ae9453e09e905a673079fd268b3b051ab33
[733] Data Integrity Audit Scheme Based on Quad Merkle Tree and Blockchain, https://www.semanticscholar.org/paper/fba6807ad8218a52573215d7ce548f417ab9b0f7
[734] Current Trends and Future Implementation Possibilities of the Merkel Tree, https://www.semanticscholar.org/paper/69a6b9611aee207f81e135c30b0bbb5f2dd9fba4
[735] Hashing In Blockchain Using Merkle Tree POW Cosensus Algorithms, https://www.semanticscholar.org/paper/01a7b5b09123eb4fee79b2a4999d28ebb331bdf5
[736] Merkle Hash Trees, https://www.semanticscholar.org/paper/f5d2b325bfa08091f93ef5676ce4112f01712fe4
[737] Jellyfish Merkle Tree, https://www.semanticscholar.org/paper/a43fd556b2bdc03995efe620e885817b31590d38
[738] BlockTree: a nonlinear structured, scalable and distributed ledger scheme for processing digital transactions, https://www.semanticscholar.org/paper/9bec980fda7e986fe4b705ae955eeb317db1ffd2
[739] ENHANCING TRANSACTION VERIFICATION THROUGH PRUNED MERKLE TREE IN BLOCKCHAIN, https://www.semanticscholar.org/paper/7baf40bfd0b72b2a0a3bd08350ba8ca4ea292c25
[740] Optimizing Merkle Tree Structure for Blockchain Transactions by a DC Programming Approach, https://www.semanticscholar.org/paper/5d18179b8da778e695a461abe65fa4af8c71b8c7
[741] MB-PBA: Leveraging Merkle Tree and Blockchain to Enhance User Profile-based Authentication in E-Learning Systems, https://www.semanticscholar.org/paper/1071872fa69551241b9aa2cbc7e9f916cac5b076
[742] Blockchains with Five Merkle Trees to Support Financial Transactions, https://www.semanticscholar.org/paper/32c894ab318541f333778f14e2e02ed5b0b36527
[743] EMT: Extended Merkle Tree Structure for Inserted Data Redaction in Permissioned Blockchain, https://www.semanticscholar.org/paper/9c9e41fc846d03cb382bbe27cdf39ce8dfc30ba1
[744] Fractal Merkle Tree Representation and Traversal, https://www.semanticscholar.org/paper/a616473a13cf6f3a9deba8cf30847dd83d59979b
[745] Polar Coded Merkle Tree: Improved Detection of Data Availability Attacks in Blockchain Systems, https://www.semanticscholar.org/paper/ad606b35d43ab4599a238cb270d995857b63ebc6
[746] Hierarchical blockchain-based secure data storage in cloud using Merkle tree approach, https://www.semanticscholar.org/paper/77159a9d22e0420e26c997fc831c7784e7e4631c
[747] Merkle trees in blockchain: A study of collision probability and security implications, https://www.sciencedirect.com/science/article/pii/S2542660524001343
[748] Toward a green blockchain: Engineering merkle tree and proof of work for energy optimization, https://ieeexplore.ieee.org/abstract/document/9939185/
[749] A peer to peer money transfer using SHA256 and Merkle tree, https://ieeexplore.ieee.org/abstract/document/8691933/
[750] Energy efficient merkle trees for blockchains, https://ieeexplore.ieee.org/abstract/document/9724439/
[751] Blockchain Merkle-Tree Ethereum Approach in Enterprise Multitenant Cloud Environment., https://www.researchgate.net/profile/Santosh-Kumar-Henge/publication/365211046_Blockchain_Merkle-Tree_Ethereum_Approach_in_Enterprise_Multitenant_Cloud_Environment/links/636b290454eb5f547cb78648/Blockchain-Merkle-Tree-Ethereum-Approach-in-Enterprise-Multitenant-Cloud-Environment.pdf
[752] Coded merkle tree: Solving data availability attacks in blockchains, https://link.springer.com/chapter/10.1007/978-3-030-51280-4_8
[753] Tunneling trust into the blockchain: a merkle based proof system for structured documents, https://ieeexplore.ieee.org/abstract/document/9211401/
[754] Recommendation for Stateful Hash-Based Signature Schemes, https://www.semanticscholar.org/paper/ac2796654f472a395fdfed273bcb177a6fb4a586
[755] Synced Hash-Based Signatures: Post-Quantum Authentication in a Blockchain, https://www.semanticscholar.org/paper/0fccca672e5178a4e1d199a9c8f65ecf6fd2149f
[756] Hierarchical Deterministic Bitcoin Wallets that Tolerate Key Leakage, https://www.semanticscholar.org/paper/e92f05bd9f23e17b0d8338625a324a2871ea701a
[757] Post-quantum Hash-based Signatures for Multi-chain Blockchain Technologies, https://www.semanticscholar.org/paper/62453d3a1935cb65f7ad93cf376ac28c1161e67d
[758] KVaC: Key-Value Commitments for Blockchains and Beyond, https://www.semanticscholar.org/paper/58cf22a19e6c7109aae7c5c4d8e250b8670afad4
[759] LMS-SM3 and HSS-SM3: Instantiating Hash-based Post-Quantum Signature Schemes with SM3, https://www.semanticscholar.org/paper/af72bbea0df84beb8b3613bbd93eda3a29c4059a
[760] NEST: Strong Key-Insulated Password-Based Shared-Custodial Blockchain Wallets, https://www.semanticscholar.org/paper/85fbd470332fc68016535d6b46853ad6e50183ad
[761] Hash-Based Cache Distribution and Search Schemes in Content-Centric Networking, https://www.semanticscholar.org/paper/e67fef12eb88018981b524833f2d92aeaf7c862e
[762] Commitment using hash functions, https://www.semanticscholar.org/paper/4cf27c6a81d99c7b425c6683df9b84895b2fe785
[763] Quantum-Accessible Security of Stateless Hash-based Signature Schemes, https://www.semanticscholar.org/paper/a534c87e92db3b9008558e9f2f462f904cc39e17
[764] Practical Cryptography for Blockchains: Secure Protocols with Minimal Trust, https://www.semanticscholar.org/paper/1da55b4c8d91569086649b527190cae99c384c11
[765] High Performance of Hash-based Signature Schemes, https://www.semanticscholar.org/paper/29f36c12d7bb1d4bcf237a7c040131a6509a332d
[766] Unstoppable Wallets: Chain-assisted Threshold ECDSA and its Applications, https://www.semanticscholar.org/paper/a778cdc7064a17f6341a4fe75c65d1bb2757318b
[767] A Lightweight Blockchain for the Internet of Medical Things Using Hash-based Message Authentication Codes, https://www.semanticscholar.org/paper/7dfe36d7287cd7837850ddeda19def0d4333e492
[768] Mercurial Commitments: Minimal Assumptions and Efficient Constructions, https://www.semanticscholar.org/paper/56ef9991f051a5c858b19204125a3a41a51ab8a3
[769] An Analysis of Existing Hash-Based Post-Quantum Signature Schemes, https://www.semanticscholar.org/paper/df75707b5ad9752b6437209c5301b14f0d56d741
[770] Block-hash signature (BHS) for transaction validation in smart contracts for security and privacy using blockchain, https://ieeexplore.ieee.org/abstract/document/10975723/
[771] An overview of hash based signatures, https://eprint.iacr.org/2023/411
[772] Chameleon hash time-lock contract for privacy preserving payment channel networks, https://link.springer.com/chapter/10.1007/978-3-030-31919-9_18
[773] Accelerating Hash-Based Polynomial Commitment Schemes with Linear Prover Time, https://tches.iacr.org/index.php/TCHES/article/view/12413
[774] a Blockchain-Aided Hash-based Signature Scheme, https://openresearch.surrey.ac.uk/view/pdfCoverPage?instCode=44SUR_INST&filePid=13210600450002346&download=true#page=73
[775] Optimizing Merkle Proof Size for Blockchain Transactions, https://www.semanticscholar.org/paper/b5ec82b01a51a1075adea8b0105426c1ea002ed3
[776] Efficient Layered Circuit for Verification of SHA3 Merkle Tree, https://www.semanticscholar.org/paper/7c1f9ae45e039971b3599f560d49f8c0dbcc3c0d
[777] DMSS-Dynamic Merkle Authentication-tree Signature, https://www.semanticscholar.org/paper/d2bf42ab4567acf5f67c8abb7f758bc04c32b17d
[778] Merkle's post-quantum signature based on the modified Lamport algorithm, https://www.semanticscholar.org/paper/2fb40148c07796a2160bc1da0d10db1eccad788b
[779] What Is the Threshold Signature Scheme? - Crypto APIs, https://cryptoapis.io/blog/78-what-is-the-threshold-signature-scheme
[780] How Threshold Signature Scheme (TSS) is Powering the Blockchain ..., https://medium.com/@dodolabs/how-threshold-signature-scheme-tss-is-powering-the-blockchain-revolution-6822970ab8c8
[781] Threshold Signature Scheme (TSS) in Crypto Wallet Security, https://sunandoroy.org/2025/02/05/threshold-signature-scheme-tss-in-crypto-wallet-security/
[782] Explanation of threshold signatures - Binance, https://www.binance.com/en/square/post/17681517589057
[783] Understanding the Threshold Signature Scheme - Lightspark, https://lightspark.com/glossary/threshold-signature-scheme
[784] [PDF] Securing Bitcoin wallets via a new DSA/ECDSA threshold signature ..., http://stevengoldfeder.com/papers/threshold_sigs.pdf
[785] Threshold signatures and Bitcoin wallet security: A menu of options, https://blog.citp.princeton.edu/2014/05/23/threshold-signatures-and-bitcoin-wallet-security-a-menu-of-options/
[786] Threshold Signatures - IEEE Computer Society, https://www.computer.org/csdl/magazine/sp/2024/06/10799187/22EaoD72B7W
[787] [PDF] Threshold-optimal DSA/ECDSA signatures and an application to ..., https://eprint.iacr.org/2016/013.pdf
[788] How MPC Wallets Work: A Complete Guide for All Levels, https://cordialsystems.com/post/how-mpc-wallets-work-a-complete-guide-for-all-levels
[789] Introducing Ed25519 in Web3Auth's MPC: Secure Signing ..., https://blog.web3auth.io/introducing-ed25519-in-web3auths-mpc-secure-signing-for-dapps-and-wallets/
[790] The Key to FROST: What is Distributed Key Generation?, https://blog.blockstream.com/the-key-to-frost-what-is-distributed-key-generation/
[791] bancaditalia/secp256k1-frost: Implementation of Flexible ..., https://github.com/bancaditalia/secp256k1-frost
[792] FROST Research Update, https://hackmd.io/@bc-community/rymgLl7hA
[793] The Evolution of MPC: From Secure but Slow to Fast and ..., https://www.dynamic.xyz/blog/the-evolution-of-mpc
[794] Practical Zero-Trust Threshold Signatures in Large-Scale ..., https://eprint.iacr.org/2025/297.pdf
[795] Blockchain Bookkeeping Optimization Scheme Based on Threshold Ring Signature, https://www.semanticscholar.org/paper/bb37f8d5d39f7eedd07fd74a1b1c1f60bf62334c
[796] Threshold Signature, https://www.semanticscholar.org/paper/b50888f58d10bd9ceefa23a571e890fd2b4ae43d
[797] Securing Blockchain Wallets Efficiently Based on Threshold ECDSA Scheme Without Trusted Center, https://www.semanticscholar.org/paper/9d2fec8df4c9a59aa31e24a4b493450e5ab81ab2
[798] An efficient multi-signature wallet in blockchain using bloom filter, https://www.semanticscholar.org/paper/00ddddf3a02431c847bcfe07db3f6b9afbfe48e0
[799] Threshold Signature for Privacy-Preserving Blockchain, https://www.semanticscholar.org/paper/badd7c0498a6508b0df3fe009eb49d397715b66e
[800] Design and Implementation of Trustzone-Based Blockchain Chip Wallet, https://www.semanticscholar.org/paper/3f4bcafc77a4160befd2e64402ebc37fb028a1cd
[801] Designated confirmer threshold signature and its applications in blockchains, https://www.semanticscholar.org/paper/aaa0205e5f8807e56d980e63e7cdcac0b33db9c0
[802] Lattice-Based Threshold Signature Implementation for Constrained Devices, https://www.semanticscholar.org/paper/e320788fc826fd177651862cb2485804a7d8dc12
[803] Threshold signature scheme without trusted party, https://www.semanticscholar.org/paper/ebcc661748ac50295935a9caa1c868ee89a7370b
[804] Efficient Forward Security Threshold Signature Scheme, https://www.semanticscholar.org/paper/2e9ae04a76f95dd7eeb7243aad17959edb92763a
[805] Threshold DSS Signatures without a Trusted Party, https://www.semanticscholar.org/paper/b88f56b9e360b1c436dd850466dd44aeb57d9c88
[806] Practical Threshold Signatures, https://www.semanticscholar.org/paper/d728243147560dd11960bc30f80a14fe6533a508
[807] An improved Threshold Signature scheme, https://www.semanticscholar.org/paper/2e4dda07eb0469a1642fc8a9e4d2645a46e28a9b
[808] Efficient weighted threshold ECDSA for securing bitcoin wallet, https://www.semanticscholar.org/paper/40b73b613c84b6200c18bd2a98cf79858a5d6281
[809] Threshold-optimal DSA/ECDSA signatures and an application to bitcoin wallet security, https://link.springer.com/chapter/10.1007/978-3-319-39555-5_9
[810] Account abstraction on Ethereum: From ERC-4337 to EIP-7702, https://www.turnkey.com/blog/account-abstraction-erc-4337-eip-7702
[811] Deep Dive into Account Abstraction and EIP-4337 - Medium, https://medium.com/blockchain-at-usc/deep-dive-into-account-abstraction-and-eip-4337-scaling-ethereum-ux-from-0-to-1-c2e6da49d226
[812] 4337Mafia/awesome-account-abstraction: A curated list of ... - GitHub, https://github.com/4337Mafia/awesome-account-abstraction
[813] Account Abstraction's Impact on Security and User Experience, https://www.openzeppelin.com/news/account-abstractions-impact-on-security-and-user-experience
[814] Account Abstraction: A Comprehensive Guide - Halborn, https://www.halborn.com/blog/post/account-abstraction-a-comprehensive-guide
[815] Account Abstraction: Past, Present, Future - MetaMask, https://metamask.io/news/account-abstraction-past-present-future
[816] Account Abstraction - the Future of Wallets? - Dynamic.xyz, https://www.dynamic.xyz/blog/account-abstraction
[817] What are Session Keys? The Complete Guide to Building Invisible ..., https://blog.thirdweb.com/what-are-session-keys-the-complete-guide-to-building-invisible-blockchain-experiences-with-account-abstraction/
[818] Session keys - Abstract, https://docs.abs.xyz/abstract-global-wallet/session-keys/overview
[819] Session Keys: Unlocking Better UX, https://starkware.co/blog/session-keys-unlocking-better-ux/
[820] Account Abstraction 101: ERC-4337 for Rollups - Conduit, https://www.conduit.xyz/blog/account-abstraction-guide/
[821] Account Abstraction (EIP-7702) on Sonic \u2014 The Beginner's ..., https://blog.soniclabs.com/account-abstraction-eip-7702-on-sonic-the-beginners-guide/
[822] Session Key Validation: Revolutionizing Web3 Wallet Security ..., https://olympixai.medium.com/session-key-validation-revolutionizing-web3-wallet-security-without-changing-wallets-6f27a60a4fbd
[823] Account Abstraction: Your Crypto Advantage, https://www.starknet.io/blog/account-abstraction/
[824] EIP-4337 example implementation and source code, https://ethereum.stackexchange.com/questions/147336/eip-4337-example-implementation-and-source-code
[825] A collection of example scripts for working with ERC-4337 - GitHub, https://github.com/mashharuki/erc-4337-examples
[826] How do ERC-4337 smart contract wallets work? - Alchemy, https://www.alchemy.com/overviews/how-do-smart-contract-wallets-work
[827] How to Build an ERC-4337 Account Abstraction Wallet from Scratch, https://egeyag.medium.com/how-to-build-an-erc-4337-account-abstraction-wallet-from-scratch-9ed7abde4cd7
[828] Account Abstraction and ERC-4337 - Part 2 | QuickNode Guides, https://www.quicknode.com/guides/ethereum-development/wallets/account-abstraction-and-erc-4337-pt-2
[829] The key account management practices and effectiveness, https://www.semanticscholar.org/paper/6ac081dfee2475eebd85fe6097fd676395485a12
[830] Securing Cookies/Sessions Through Non-fungible Tokens, https://www.semanticscholar.org/paper/152fb81bf0e4e42870b6040a978b252bd4805d88
[831] Reminisce for Securing Private-Keys in Public, https://www.semanticscholar.org/paper/b582bb3105f3f48d6787285ea5ec50d81779c822
[832] A Research on Session Key Management in Advanced Metering Infrastructure, https://www.semanticscholar.org/paper/545c722e2e4bdefd6ac16dfe58af8c5acf3f7490
[833] Proactive and reactive: drivers for key account management programmes, https://www.semanticscholar.org/paper/48053535d05ab8955cc662b84fdda1289a9b0a00
[834] Session details: Verification and security, https://www.semanticscholar.org/paper/e77c203453b56a1701a73217b3df7831cee362c8
[835] Access Ethereum Proof-of-Authority, https://www.semanticscholar.org/paper/da5e450ea1d23aad68ec3fa3d6a7e78d9d7682ee
[836] DecentralizedVoting Application using theERC-4337 Standard, https://ieeexplore.ieee.org/abstract/document/11015202/
[837] Stealing trust: Unraveling blind message attacks in web3 authentication, https://dl.acm.org/doi/abs/10.1145/3658644.3670323
[838] An Anonymous yet Accountable Contract Wallet System using Account Abstraction, https://www.semanticscholar.org/paper/2c124d21b066939dd3be9a19a3743c07a1ba4e7a
[839] Security Standards and Best Practices for Quantum Key Distribution, https://www.semanticscholar.org/paper/fa4570da7cea6cc912c2b09c2e6dfcb79543d781
[840] Password Security: Best Practices and Management Strategies, https://www.semanticscholar.org/paper/c4ed81b0a799ec8248c04d0c74ee56da5d4e0bd4
[841] Best Practices for Software Security, https://www.semanticscholar.org/paper/0c19545bcc0380d49a96b1fb324d75f8ba3420ff
[842] Watch Out for Your Token Approvals: Don't Become a Hacker's ATM, https://blog.keyst.one/watch-out-for-your-token-approvals-don-t-become-a-hacker-s-atm
[843] A blockchain-based data-driven trustworthy approval process system, https://www.sciencedirect.com/science/article/pii/S2667096823000095
[844] Smart Management of Approval Limits in DApps - CoolWallet, https://www.coolwallet.io/blogs/blog/approval-limits-dapps?srsltid=AfmBOorjzb_4mdqs812Ggk_HeVfyqgA1SvEk-6qc7xIX67ZSBMbca96v
[845] Token Approval Checker \u2013 Deep Dive - Bitbond, https://www.bitbond.com/resources/token-approval-checker-deep-dive/
[846] Permit2: A Next-Generation Token Approval Mechanism - Medium, https://medium.com/@gwrx2005/permit2-a-next-generation-token-approval-mechanism-7603d292ddfc
[847] Understanding Token Approvals on EVM & Tron - Utila, https://utila.io/blog/understanding-token-approvals-on-evm-tron/
[848] MetaMask Batch Approve Payments and Reconciliation, https://blog.cryptoworth.com/batch-approve-transaction-metamask/
[849] Advanced Approaches to Transaction Signing and Approval, https://www.chainalysis.com/blog/transaction-signing-and-approval-hexagate-gatesigner/
[850] Web3 UX Design Patterns that Build Trust - 10 Interface Decisions, https://coinbound.io/web3-ux-design-patterns-that-build-trust-10-interface-decisions-to-reduce-doubt-and-abandonment/
[851] Designing for Blockchain: Try These 8 Best UX Practices, https://procreator.design/blog/designing-for-blockchain-best-ux-practices/
[852] Transaction flows - Web3 UX Design Handbook, https://web3ux.design/transaction-flows
[853] Individual limits, https://www.semanticscholar.org/paper/4382c5ad34304ff4446cf682f7ffeebfc8368fae
[854] Limits, https://www.semanticscholar.org/paper/d65cc6658f2a25e52215f426d9ec1cdbc7c55e83
[855] Wallet Key Generation for a Generic Blockchain based on Speech, https://www.semanticscholar.org/paper/fc687f44622e37b30b7a68f165726300e0f780b6
[856] Three. Limit, https://www.semanticscholar.org/paper/e5769dfb28e1b7c36f203876c8bd7b283475ba76
[857] Biometrics Enhances Blockchain Wallet Governance, https://www.semanticscholar.org/paper/ad4f9f86931dbe9db6df123f182c26400b5ad7ef
[858] Correction to active transfer limits, https://www.semanticscholar.org/paper/458c389fc50c1039632abe92605bc19958b3fb80
[859] A delay-tolerant payment scheme based on the ethereum blockchain, https://ieeexplore.ieee.org/abstract/document/8661611/
[860] Blockchain: Bitcoin wallet cryptography security, challenges and countermeasures, https://www.academia.edu/download/102145235/blockchain-bitcoin-wallet-cryptography-security-challenges-and-countermeasures.pdf
[861] Using Linear Regression to Investigate the Relationship Between User Experience and UX Components in Cryptocurrency Wallets, https://www.semanticscholar.org/paper/1f5ea1fe1422f77892ff5260b07efc132ed59eb3
[862] Improving User Experience of Cryptocurrency Wallets: An Exploratory Study Leading To Design Recommendations, https://www.semanticscholar.org/paper/0c63639bca65c8e0a3b19a3e6b834b5cfe19cd4f
[863] An Efficient and Transparent Financial Transaction System using Decentralized Finance (DeFi) based on Blockchain Technology, https://ieeexplore.ieee.org/abstract/document/10811700/
[864] Optimizing User Experience in Digital Payments: The Case of Finpay Money, https://www.ijie.ir/index.php/ijie/article/view/196
[865] Risk of desirable user experiences: insights from those who create, facilitate and accept mobile payments, https://link.springer.com/article/10.1007/s10660-024-09835-4
[866] The Distribution of Limit Order Execution Time and EMH Test, https://www.semanticscholar.org/paper/fbc9c398be60ef3c52e0e8eb85c4cf9f9e9ff877
[867] A Dynamic Model of Order Execution and the Intraday Cost of Limit Orders, https://www.semanticscholar.org/paper/7723093266ca9c1691dec26b8e4b76c9b984c823
[868] Monitoring and Limit Order Submission Risks, https://www.semanticscholar.org/paper/443824f13579546acaae3f66837455dc38c352f6
[869] MPC Wallet Development: How to Build a Secure Multi ... - SCAND, https://scand.com/company/blog/mpc-wallet-development-guide/
[870] MPC Wallet: Support New and Niche Protocols That Users Require, https://www.blockdaemon.com/blog/mpc-wallet-support-new-and-niche-protocols-that-users-require
[871] Digital Asset Custody and Transaction Processing Leading ..., https://fireblocks.com/report/digital-asset-custody-and-transaction-processing-leading-practices-using-fireblocks-mpc-solution/
[872] MPC Wallets: A Complete Technical Guide (2025) - Stackup, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide
[873] Threshold ECDSA: The Key Ingredient Behind the Internet ... - Medium, https://medium.com/dfinity/threshold-ecdsa-the-key-ingredient-behind-the-internet-computers-bitcoin-and-ethereum-cf22649b98a1
[874] Threshold ECDSA | Internet Computer, https://internetcomputer.org/docs/building-apps/network-features/signatures/t-ecdsa
[875] pier-wallet/mpc-lib - NPM, https://www.npmjs.com/package/%40pier-wallet%2Fmpc-lib
[876] Jahankohan/mpc_wallet - GitHub, https://github.com/Jahankohan/mpc_wallet
[877] MPC on Ethereum - Multiparty Computation, https://ethresear.ch/t/mpc-on-ethereum/311
[878] MPC Snap: Integrating Multi-Factor Authentication Into MetaMask, https://metamask.io/news/mpc-snap-integrating-multi-factor-authentication-into-metamask
[879] Cryptography and MPC in Coinbase Wallet as a Service (WaaS), https://www.semanticscholar.org/paper/1173fd507b52cd123234bd5fa61b4833d4908a65
[880] Blockchain Implementation, https://www.semanticscholar.org/paper/c88cc1c35566a2ed3edc6f15bc67b57ba228d93e
[881] MPC as a service using Ethereum Registry Smart Contracts - dCommon CIP, https://www.semanticscholar.org/paper/59d9a6dd3e985cfb8401dd6f8d8819fd683f5b79
[882] Ratel: Mpc-extensions for smart contracts, https://dl.acm.org/doi/abs/10.1145/3634737.3661142
[883] Fast Secure Two-Party ECDSA Signing, https://www.semanticscholar.org/paper/59cbbb6ccd07dc312d3d0c218d384f004396c370
[884] Securing Bitcoin wallets via a new DSA / ECDSA threshold signature scheme, https://www.semanticscholar.org/paper/8b9b7e1fb101a899b0309ec508ac5912787cc12d
[885] BTOOLS: Trusted Transaction Generation for Bitcoin and Ethereum Blockchain Based on Crypto Currency SmartCard, https://www.semanticscholar.org/paper/512bdae61c3067d87e4d612d238122c5317c1a2f
[886] ECDSA Cracking Methods, https://www.semanticscholar.org/paper/63fc381a25c69b5434c61c26d27f5db62a41c679
[887] Comparison and Analysis of Data and Transaction Structure of Bitcoin and Ethereum, https://www.semanticscholar.org/paper/df9f0284e6a18fff45f1ddee42206ced2d4b4b59
[888] Merkle Proof, https://www.crypto.com/glossary/merkle-proof
[889] Efficient and Universal Merkle Tree Inclusion Proofs via OR Aggregation, https://www.semanticscholar.org/paper/ce918a39861abc7c767f1e02ba18efa9d77651a2
[890] Traffic-Aware Merkle Trees for Shortening Blockchain Transaction Proofs, https://www.semanticscholar.org/paper/45de9c3f80572bdf87c6d813cfaaab3ef548606d
[891] Merkle Tree Traversal in Log Space and Time, https://www.semanticscholar.org/paper/342ca79a0ac2cc726bf31ffb4ce399821d3e2979
[892] An�lise das estruturas de dados verific�veis nas blockchains Ethereum e Neo, https://www.semanticscholar.org/paper/eeb9be2721edb4bb82e430bbd625770310d93211
[893] Enhancing Cryptocurrency Security with Multi-sig Wallets and ..., https://www.cryptoeq.io/articles/wallet-multisig-security
[894] A practical guide to evaluating MPC-TSS Protocols for Crypto custody, https://metabitcoiner.substack.com/p/a-practical-guide-to-evaluating-mpc
[895] Schnorr Signature Scheme with Restricted Signing Capability, https://www.semanticscholar.org/paper/fb04deb4f177e7101d1e3bf5f39402b90b1d73de
[896] What Is Account Abstraction? EIP-4337 Explained - Jarrod Watts, https://blog.jarrodwatts.com/what-is-account-abstraction-and-how-does-eip-4337-work
[897] Account Abstraction Will Evolve Wallets - Amber Labs - Substack, https://amberlabs.substack.com/p/account-abstraction-will-evolve-wallets
[898] Account Abstraction: The Key to Blockchain Reporting, https://revistaie.ase.ro/content/111/06%20-%20ojog,%20miron.pdf
[899] Privacy-Preserving Account-Abstraction for Teams on EVM chains, https://ieeexplore.ieee.org/abstract/document/10634477/
[900] Exploring Account Abstraction: Addressing Challenges in Private Key Management for Mainstream Adoption of Blockchain Technology, https://www.researchgate.net/profile/Sergey-Yurish/publication/375486084_Proceedings_of_the_2nd_Blockchain_and_Cryptocurrency_Conference_B2C'_2023/links/654b9e56b86a1d521bc7887a/Proceedings-of-the-2nd-Blockchain-and-Cryptocurrency-Conference-B2C-2023.pdf#page=11
[901] Enhancing Security in Smart Contract Wallets : An OTP Based 2-Factor Authentication Approach, https://www.semanticscholar.org/paper/f6a9bcbf0ca58352a13edb32f4bb4bc74c53b338
[902] The Risks of Approving Smart Contract Transactions | Binance Blog, https://www.binance.com/en/blog/security/web3-wallet-security-the-risks-of-approving-smart-contract-transactions-4317275693972329667
[903] [PDF] Quantifying the Risk of Unlimited Approval of ERC20 Tokens on ..., https://yajin.org/papers/raid22_approval.pdf
[904] The On-Chain Limit Order Book Protocol On Arbitrum One - Nexera, https://nexera.medium.com/nexera-exchange-the-on-chain-limit-order-book-protocol-on-arbitrum-one-170c400057e7
[905] Introducing dLIMIT - Decentralized Limit Orders for DEXs ... - Orbs, https://www.orbs.com/Introducing-dLIMIT-for-DEXs/
[906] Reporting Limit (RL), https://www.semanticscholar.org/paper/7d6012cfb91f5bb7d7c1000a396697c7aa1aaa33
[907] Blockchain-based payment collection supervision system using pervasive Bitcoin digital wallet, https://ieeexplore.ieee.org/abstract/document/8115844/
[908] A novel cryptocurrency wallet management scheme based on decentralized multi-constrained derangement, https://ieeexplore.ieee.org/abstract/document/8937472/
[909] The Effect of Transaction Experience Using Digital Wallets on User Satisfaction in Millennial Generation, https://www.semanticscholar.org/paper/58993d6faf13aa8da1739f8818b1addc1a76cbef
[910] Gamification Of E-Wallets With The Use Of Defi Technology-A Revisit To Digitization In Fintech, https://www.researchgate.net/profile/Bibhu-Dash-5/publication/368302273_GAMIFICATION_OF_E-WALLETS_WITH_THE_USE_OF_DeFi_TECHNOLOGY-A_REVISIT_TO_DIGITIZATION_IN_FINTECH/links/63e13c59f8cf684fe96ef46f/GAMIFICATION-OF-E-WALLETS-WITH-THE-USE-OF-DeFi-TECHNOLOGY-A-REVISIT-TO-DIGITIZATION-IN-FINTECH.pdf
[911] Secure and Usable Decentralized Web Wallet, https://pub.hcw.ac.at/obvfcwhsacc/content/titleinfo/9634576/full.pdf
