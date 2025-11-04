# Blockchain Security Cryptography Developer Assessment
## Fill-in-the-Blank Item Bank (Items 1–36)

---

## Contents

- [Item Bank](#item-bank-items-1-36)
- [Topic 1: Threshold Signature Schemes & MPC Fundamentals](#topic-1-threshold-signature-schemes--mpc-fundamentals)
- [Topic 2: Cryptographic Protocol Implementation](#topic-2-cryptographic-protocol-implementation)
- [Topic 3: Wallet Key Management & Recovery](#topic-3-wallet-key-management--recovery)
- [Topic 4: Blockchain Transaction Signing & Standards](#topic-4-blockchain-transaction-signing--standards)
- [Topic 5: Account Abstraction & Advanced Features](#topic-5-account-abstraction--advanced-features)
- [Topic 6: Security, Risk Assessment & Attack Vectors](#topic-6-security-risk-assessment--attack-vectors)
- [Reference Sections](#reference-sections)
- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [Codebase & Library References](#codebase--library-references)
- [Authoritative Literature & Reports](#authoritative-literature--reports)
- [APA Style Source Citations](#apa-style-source-citations)

---

## Item Bank (Items 1–36)

### Topic 1: Threshold Signature Schemes & MPC Fundamentals

#### Item 1: Shamir Secret Sharing Reconstruction Formula

**Difficulty:** Foundational

**Statement:** In Shamir Secret Sharing, a secret \(s\) is reconstructed from a threshold set of shares using the formula \(s = \sum_{i \in \mathcal{S}} \lambda_{\mathcal{S}}^{i} \cdot s_i\), where \(\lambda_{\mathcal{S}}^{i}\) is known as the ___ coefficient and \(\mathcal{S}\) is the set of participating shares.

**Acceptable Answers:** ["Lagrange", "Lagrange interpolation"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "Lagrange" or "Lagrange interpolation" | **Common incorrect:** "Shamir", "interpolation coefficient", "recovery"

**Rationale:** The Lagrange coefficient is the mathematical foundation enabling secret reconstruction in Shamir's threshold scheme. [Ref: G2, L1] Lagrange interpolation allows the scheme to achieve perfect secrecy—no information about the secret leaks from any \(t-1\) shares. [Ref: A7]

---

#### Item 2: MPC Wallet Distributed Key Generation

**Difficulty:** Foundational

**Statement:** In MPC wallet implementations, the ___ (DKG) protocol creates shares of the private key among multiple parties without any single party ever seeing the complete key.

**Acceptable Answers:** ["distributed key generation", "DKG"]

**Normalization:** Case-insensitive; trim whitespace; accept both full term and acronym

**Grading:** Accept "distributed key generation" or "DKG" | **Common incorrect:** "key sharing", "distributed secret", "threshold key"

**Rationale:** DKG is the foundational process in MPC wallets. Unlike Shamir Secret Sharing (which requires a trusted dealer), DKG distributes key generation itself, eliminating a single point of failure. [Ref: C1, A1, A9]

---

#### Item 3: GG18/GG20 Threshold ECDSA Communication Rounds

**Difficulty:** Intermediate

**Statement:** The GG18 protocol for threshold ECDSA required ___ rounds of communication for signing, while the improved GG20 protocol reduced this overhead with enhanced security guarantees.

**Acceptable Answers:** ["nine", "9"]

**Normalization:** Case-insensitive; accept both numeric and spelled-out forms

**Grading:** Accept "9" or "nine" (±0 tolerance for numeric answers) | **Common incorrect:** "five", "three", "four", "six"

**Rationale:** GG18 was the first practical threshold ECDSA implementation, requiring nine signing rounds. GG20 reduced communication complexity and fixed vulnerabilities, making it more practical for real-time wallet applications. [Ref: A9] This improvement is critical for mobile wallet responsiveness.

---

#### Item 4: FROST Signing Protocol Rounds

**Difficulty:** Intermediate

**Statement:** FROST (Flexible Round-Optimized Schnorr Threshold Signatures) improves upon earlier Schnorr threshold schemes by performing signing operations in as few as ___ round(s) without limiting concurrency, or optimized to a single-round variant with preprocessing.

**Acceptable Answers:** ["two", "2"]

**Normalization:** Case-insensitive; accept both numeric and spelled-out forms

**Grading:** Accept "2" or "two" (±0 tolerance) | **Common incorrect:** "one", "three", "four"

**Rationale:** FROST's key innovation is reducing network overhead during signing while maintaining security. It supports true t-of-n threshold signing and includes protection against forgery attacks. [Ref: L3, A8]

---

#### Item 5: Threshold Cryptography Secret Reconstruction Threshold

**Difficulty:** Foundational

**Statement:** In a threshold cryptography system with parameters (t, n), at least ___ shares are required to reconstruct the secret, but any subset with fewer shares reveals no information about the secret (perfect secrecy property).

**Acceptable Answers:** ["t", "threshold"]

**Normalization:** Case-insensitive; accept single letter or word form

**Grading:** Accept "t" or "threshold" | **Common incorrect:** "n", "t-1", "n-1", numeric values

**Rationale:** The threshold parameter \(t\) defines the security boundary. Information-theoretic security ensures that \(t-1\) shares provide zero information about the secret. [Ref: G3, A7]

---

### Topic 2: Cryptographic Protocol Implementation

#### Item 6: ECDSA Key Leakage Vulnerability

**Difficulty:** Intermediate

**Statement:** In ECDSA and Schnorr signatures, reusing the same secret nonce value \(k\) on two different messages allows attackers to recover the private key by subtracting the ___ values obtained from each signature.

**Acceptable Answers:** ["s", "signature values", "s values"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "s" or "signature values" | **Common incorrect:** "r values", "k values", "hash values", "commitment"

**Rationale:** Nonce reuse is a critical vulnerability in ECDSA-family signatures. If \(k' = k\) but \(e' \neq e\), then \(s'-s = (k'-k) + x(e'-e) = x(e'-e)\), revealing the private key \(x\). [Ref: A3, A4] Even partial leakage of \(k\) or bias in its generation can enable key recovery through the hidden number problem.

---

#### Item 7: EdDSA Curve Standard

**Difficulty:** Foundational

**Statement:** EdDSA (Edwards-curve Digital Signature Algorithm) uses Curve25519 for ___ and Curve448 for ___ implementations, providing post-quantum considerations and deterministic signature generation.

**Acceptable Answers:** ["Ed25519", "Ed448"]

**Normalization:** Exact case-sensitive match for algorithm names; accept comma-separated or separate responses

**Grading:** Accept either curve name separately | **Common incorrect:** "P-256", "secp256k1", "NIST curves"

**Rationale:** EdDSA differs fundamentally from ECDSA by being deterministic (no random nonce required), eliminating nonce-reuse vulnerabilities. Ed25519 is widely adopted in blockchain (Solana, Polkadot) and cryptographic libraries like RustCrypto. [Ref: C2, A4]

---

#### Item 8: Schnorr Signature Fiat-Shamir Transform

**Difficulty:** Advanced

**Statement:** Schnorr's signature scheme was constructed by applying the ___ transformation to Schnorr's identification protocol, making it secure under the random oracle model with a random-prefix preimage resistant hash function.

**Acceptable Answers:** ["Fiat-Shamir", "Fiat Shamir"]

**Normalization:** Case-insensitive; accept with or without hyphen

**Grading:** Accept "Fiat-Shamir" or "Fiat Shamir" (hyphen flexible) | **Common incorrect:** "Shamir", "interactive to non-interactive", "zero-knowledge proof"

**Rationale:** The Fiat-Shamir heuristic transforms interactive identification protocols into non-interactive signatures. For Schnorr signatures, security proof requires the hash function \(H\) to be random-prefix preimage resistant (but not necessarily collision resistant). [Ref: A3, G4]

---

#### Item 9: Hash Function Role in Commitment Schemes

**Difficulty:** Intermediate

**Statement:** Cryptographic hash functions serve as building blocks for ___ schemes that allow a party to commit to a value without revealing it, while maintaining the binding and hiding properties.

**Acceptable Answers:** ["commitment", "hash commitment"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "commitment" or "hash commitment" | **Common incorrect:** "encryption", "signature", "authentication"

**Rationale:** Commitment schemes use hash functions to create non-interactive commitments. In threshold protocols and MPC, commitments (like Pedersen commitments) enable parties to prove correct behavior without revealing shares. [Ref: A7, L2]

---

#### Item 10: Elliptic Curve Order & Group Operations

**Difficulty:** Intermediate

**Statement:** In elliptic curve cryptography, the ___ of a curve determines the size of the cyclic group used for key generation and signing, and protocol security depends on the discrete logarithm problem being hard within this group.

**Acceptable Answers:** ["order", "curve order", "group order"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "order" or "curve order" or "group order" | **Common incorrect:** "prime", "cofactor", "modulus"

**Rationale:** The order \(n\) of the elliptic curve group defines the size of the keyspace and directly affects security level. Cryptographic strength is approximately \(\log_2(n)\) bits. [Ref: G5, A2]

---

### Topic 3: Wallet Key Management & Recovery

#### Item 11: Soft Recovery vs. Hard Recovery in MPC Wallets

**Difficulty:** Intermediate

**Statement:** In MPC wallet recovery, a ___ recovery regenerates a specific device's key share when one device is lost (with other shares remaining intact), while ___ recovery reconstructs the entire private key seed from backed-up recovery material.

**Acceptable Answers:** ["soft", "hard"]

**Normalization:** Case-insensitive; both terms required as pair

**Grading:** Accept pair: ("soft", "hard") in order | **Common incorrect:** "partial/full", "local/global", "single/multi"

**Rationale:** Soft recovery maintains security by distributing key shares across multiple devices; hard recovery temporarily reintroduces centralization risk if performed insecurely. Institutions must test recovery procedures regularly without compromising key material. [Ref: C1, A10]

---

#### Item 12: Shamir Secret Sharing Polynomial Degree

**Difficulty:** Foundational

**Statement:** In Shamir Secret Sharing with a threshold of \(t\), the secret \(s\) is the constant term in a random polynomial of degree ___, ensuring that exactly \(t\) points uniquely define the polynomial.

**Acceptable Answers:** ["t-1", "t − 1"]

**Normalization:** Case-insensitive; accept both hyphen and minus formats

**Grading:** Accept "t-1" or "t − 1" | **Common incorrect:** "t", "t+1", "n"

**Rationale:** The polynomial \(f(x) = s + a_1 x + \cdots + a_{t-1} x^{t-1}\) has degree \(t-1\). Any \(t\) distinct shares determine \(f\) uniquely via Lagrange interpolation; fewer than \(t\) shares leave infinitely many consistent polynomials. [Ref: A7, L1]

---

#### Item 13: Hardware Security Module Tamper Response

**Difficulty:** Advanced

**Statement:** HSMs (Hardware Security Modules) protect against physical tampering by implementing ___ that detect breach attempts and securely delete sensitive keys when tampering is detected.

**Acceptable Answers:** ["sensors", "tamper sensors"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "sensors" or "tamper sensors" | **Common incorrect:** "encryption", "backup", "logging"

**Rationale:** HSMs use physical and logical sensors to detect tampering (drilling, voltage changes, temperature). Upon detection, the device erases key material in a tamper-proof enclosure. This aligns with FIPS 140-2 Level 3+ standards and ISO 27001 compliance. [Ref: A11, L4]

---

#### Item 14: Key Rotation Schedule in Custody Systems

**Difficulty:** Intermediate

**Statement:** Effective key management requires implementing ___ that regularly changes cryptographic keys to minimize the risk of unauthorized access and limit the exposure window if a key is compromised.

**Acceptable Answers:** ["key rotation", "rotation schedule"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "key rotation" or "rotation schedule" | **Common incorrect:** "backup", "encryption", "redundancy"

**Rationale:** Key rotation limits the damage from a compromised key to transactions within a defined period. MPC wallet operators rotate shares and establish passphrase rotation requirements for recovery access. [Ref: A11, A14]

---

#### Item 15: Social Recovery Guardians in Account Abstraction

**Difficulty:** Intermediate

**Statement:** Social recovery in blockchain wallets allows users to assign ___ (trusted contacts) who can collectively approve account recovery if the primary key is lost, eliminating dependence on single seed phrase backup.

**Acceptable Answers:** ["guardians", "trusted contacts"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "guardians" or "trusted contacts" | **Common incorrect:** "signers", "validators", "operators"

**Rationale:** Social recovery combines multi-signature security with human redundancy. A threshold of guardians (e.g., 3-of-5) must approve recovery, balancing security and accessibility. Implemented in Account Abstraction via smart contract wallets. [Ref: G6, A15, A16]

---

### Topic 4: Blockchain Transaction Signing & Standards

#### Item 16: Bitcoin UTXO Model

**Difficulty:** Foundational

**Statement:** Bitcoin uses the ___ model, where each transaction references one or more unspent outputs as inputs, destroys them, and creates new outputs. The balance of an address is the sum of all its unspent outputs.

**Acceptable Answers:** ["UTXO", "unspent transaction output"]

**Normalization:** Case-insensitive; accept acronym or full term

**Grading:** Accept "UTXO" or "unspent transaction output" | **Common incorrect:** "account model", "balance model", "state model"

**Rationale:** The UTXO model is fundamental to Bitcoin's design. Unlike account-based systems (Ethereum), Bitcoin uses a "cash-like" model: each output is either unspent or consumed. Lightweight nodes validate transactions via Merkle proofs without maintaining full UTXO state. [Ref: A17, A18]

---

#### Item 17: Ethereum Transaction Structure (EOA vs. Smart Contract)

**Difficulty:** Intermediate

**Statement:** Ethereum distinguishes between ___ (externally owned accounts managed by private keys) and contract accounts (managed by deployed code), with all transactions on Ethereum originating from EOAs and paid for via gas in ETH.

**Acceptable Answers:** ["EOA", "externally owned account"]

**Normalization:** Case-insensitive; accept acronym or full term

**Grading:** Accept "EOA" or "externally owned account" | **Common incorrect:** "smart contract", "user account", "validator"

**Rationale:** Before Account Abstraction (ERC-4337), Ethereum required transactions to originate from EOAs using ECDSA signatures. This design constraint created UX friction (seed phrase dependency, need to hold ETH for gas). [Ref: G7, A19, A20]

---

#### Item 18: SegWit (Segregated Witness) Innovation

**Difficulty:** Intermediate

**Statement:** Bitcoin's SegWit upgrade separated transaction signatures into a dedicated ___ area outside the 1MB block size limit, increasing effective block capacity to ~4MB while reducing transaction size for fee calculation.

**Acceptable Answers:** ["witness", "witness data"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "witness" or "witness data" | **Common incorrect:** "signature", "data", "extension"

**Rationale:** SegWit introduced P2WPKH and P2WSH address formats with Bech32 encoding. By segregating witness data, Bitcoin achieved higher throughput without hard fork consensus change. Modern wallets must handle SegWit transaction formats. [Ref: A21]

---

#### Item 19: Solana RPC Commitment Levels

**Difficulty:** Intermediate

**Statement:** Solana's RPC API supports three commitment levels in descending order of finality: ___ (most recent block confirmed by supermajority), confirmed, and processed.

**Acceptable Answers:** ["finalized"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "finalized" | **Common incorrect:** "final", "complete", "settled"

**Rationale:** Commitment levels indicate how finalized a block is. For mission-critical operations (wallet signing), developers choose finalized commitment to ensure no rollback. Processed is fastest but least safe. [Ref: A22]

---

#### Item 20: ERC-4337 EntryPoint Smart Contract

**Difficulty:** Intermediate

**Statement:** ERC-4337 introduces the ___ smart contract that validates and executes UserOperations according to logic defined in each user's smart contract wallet, enabling account abstraction without protocol changes.

**Acceptable Answers:** ["EntryPoint"]

**Normalization:** Case-sensitive; exact match required

**Grading:** Accept "EntryPoint" | **Common incorrect:** "Contract", "Validator", "Router"

**Rationale:** The EntryPoint contract is the core abstraction mechanism. It accepts UserOperations from an alternative mempool, manages bundle execution, and coordinates Paymaster gas sponsorship. [Ref: L5, A16, A20]

---

### Topic 5: Account Abstraction & Advanced Features

#### Item 21: Session Keys in Account Abstraction

**Difficulty:** Intermediate

**Statement:** Session keys are temporary, restricted-access credentials that allow users to pre-authorize a dApp to sign ___ for a limited time period without requiring repetitive signature approvals for each transaction.

**Acceptable Answers:** ["transactions"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "transactions" | **Common incorrect:** "messages", "data", "approvals"

**Rationale:** Session keys strike a balance between Web2 fluency and Web3 security. A game might authorize a session key for in-game transactions only; a DEX might authorize trading within a price slippage bound. Implemented via Account Abstraction logic. [Ref: A15, A23]

---

#### Item 22: Paymaster Contract Function

**Difficulty:** Foundational

**Statement:** In ERC-4337, a ___ contract optionally sponsors UserOperation gas costs, enabling users to pay fees in ERC-20 tokens or allow third parties to cover gas, removing the friction of requiring ETH for transaction submission.

**Acceptable Answers:** ["Paymaster"]

**Normalization:** Case-sensitive; exact match required

**Grading:** Accept "Paymaster" | **Common incorrect:** "Sponsor", "GasManager", "Fee"

**Rationale:** Paymasters decouple gas payment from transaction execution, improving onboarding. Users in emerging markets can interact with dApps without first acquiring ETH, expanding Web3 accessibility. [Ref: A16, A24]

---

#### Item 23: UserOperations in Account Abstraction

**Difficulty:** Foundational

**Statement:** ERC-4337 defines ___ as special transaction-like objects containing user intent, smart contract wallet address, and operations to be performed, held in an alternative mempool separate from regular transactions.

**Acceptable Answers:** ["UserOperation", "UserOperations"]

**Normalization:** Case-sensitive; accept singular or plural

**Grading:** Accept "UserOperation" or "UserOperations" | **Common incorrect:** "Transaction", "Message", "Call"

**Rationale:** UserOperations are the core abstraction primitive. Bundlers collect multiple UserOperations and submit them atomically to the EntryPoint, enabling batch processing and fee aggregation. [Ref: L5, A24]

---

#### Item 24: Zero-Knowledge Proofs in Privacy-Preserving Wallets

**Difficulty:** Advanced

**Statement:** Zero-knowledge proofs allow a prover to prove knowledge of a statement without revealing the statement itself, enabling blockchain applications like ___ to preserve user privacy while maintaining accountability.

**Acceptable Answers:** ["private transactions", "anonymous transactions"]

**Normalization:** Case-insensitive; trim whitespace; accept common variants

**Grading:** Accept "private/anonymous transactions" or similar | **Common incorrect:** "encryption", "signing", "authentication"

**Rationale:** ZKPs use circuits to prove statements cryptographically. In wallets, ZKPs enable proving proof-of-reserves, anonymous authentication (Anon-Aadhaar), and privacy-preserving voting without revealing identity. [Ref: A25, A26]

---

#### Item 25: Bundler Role in ERC-4337

**Difficulty:** Intermediate

**Statement:** A ___ in ERC-4337 collects multiple UserOperations from the alternative mempool, groups them into a single transaction, and submits them to the EntryPoint contract for batch execution and settlement.

**Acceptable Answers:** ["bundler"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "bundler" | **Common incorrect:** "aggregator", "executor", "validator"

**Rationale:** Bundlers earn a fee for aggregating UserOperations, similar to MEV searchers. This mechanism replaces the traditional mempool and enables flexible transaction validation logic. [Ref: L5, A24]

---

### Topic 6: Security, Risk Assessment & Attack Vectors

#### Item 26: Side-Channel Attack Classification

**Difficulty:** Advanced

**Statement:** Side-channel attacks attempt to extract cryptographic secrets not through algorithm weaknesses but by measuring indirect system effects such as ___, electromagnetic radiation, or memory access patterns.

**Acceptable Answers:** ["timing", "power", "timing/power"]

**Normalization:** Case-insensitive; trim whitespace; accept multiple options

**Grading:** Accept "timing" or "power" or both | **Common incorrect:** "encryption", "computation", "algorithm"

**Rationale:** Timing attacks measure how long cryptographic operations take. Simple Power Analysis (SPA) and Differential Power Analysis (DPA) measure power consumption. These attacks have recovered keys from RSA, ECDSA, and AES implementations. [Ref: A27, G8]

---

#### Item 27: Constant-Time Implementation Requirement

**Difficulty:** Advanced

**Statement:** Cryptographic operations must be implemented in ___ to prevent timing attacks, ensuring execution time does not leak information about the secret values being processed.

**Acceptable Answers:** ["constant-time"]

**Normalization:** Case-insensitive; accept with or without hyphen

**Grading:** Accept "constant-time" or "constant time" | **Common incorrect:** "secure time", "fixed time", "optimized time"

**Rationale:** Constant-time implementations use techniques like dummy operations, conditional moves, and eliminating branches dependent on secret data. Critical in cryptographic libraries like RustCrypto (ecdsa, ed25519 crates). [Ref: A27, C2]

---

#### Item 28: Wallet Risk Assessment Security Audit

**Difficulty:** Intermediate

**Statement:** Comprehensive wallet security audits identify potential vulnerabilities by simulating attack scenarios across all application layers, including SDKs, cryptography libraries, chain interactions, and wallet extensions, following standards like ___ and ISO 27001.

**Acceptable Answers:** ["OWASP", "C4"]

**Normalization:** Case-insensitive; accept either standard

**Grading:** Accept "OWASP" or "C4" or both | **Common incorrect:** "PCI-DSS only", "ISO only"

**Rationale:** OWASP (Open Web Application Security Project) provides vulnerability taxonomy. C4 (CryptoConsortium) focuses on blockchain-specific threats. Audits test code, logic, architecture, and runtime behavior. [Ref: A28, G9]

---

#### Item 29: Nonce Reuse Prevention in Random Number Generation

**Difficulty:** Intermediate

**Statement:** To prevent nonce reuse vulnerabilities in ECDSA/Schnorr signatures, implementations must use ___ cryptographically secure random number generators that never repeat sequence states, rather than pseudo-random generators with insufficient entropy.

**Acceptable Answers:** ["cryptographically secure", "CSPRNG"]

**Normalization:** Case-insensitive; trim whitespace; accept both forms

**Grading:** Accept "CSPRNG" or "cryptographically secure" | **Common incorrect:** "secure random", "high entropy", "deterministic"

**Rationale:** RFC 6979 defines deterministic ECDSA (RFC-6979), removing nonce generation entirely. However, Schnorr signatures typically use random nonces—CSPRNG seeding is critical. [Ref: A3, G4]

---

#### Item 30: Double-Spending Attack Prevention

**Difficulty:** Intermediate

**Statement:** In blockchain protocols, consensus ensures that once a transaction is finalized in a block, it cannot be reversed or conflicted with another spending the same input, preventing ___ attacks where an attacker spends the same asset to multiple recipients.

**Acceptable Answers:** ["double-spending"]

**Normalization:** Case-insensitive; accept with or without hyphen

**Grading:** Accept "double-spending" or "double spending" | **Common incorrect:** "replay", "fork", "reentrancy"

**Rationale:** Double-spending requires controlling >50% of hash power (PoW) or majority stake (PoS). Wallet security (private key protection) prevents individual users from initiating double-spends; consensus prevents network-level attacks. [Ref: A1, G10]

---

#### Item 31: Reentrancy Vulnerability in Smart Contracts

**Difficulty:** Intermediate

**Statement:** A reentrancy vulnerability allows an attacker to call the same smart contract function recursively before state updates occur, enabling withdrawal of funds multiple times. The infamous ___ hack of 2016 exploited this vulnerability, resulting in $50M+ loss.

**Acceptable Answers:** ["DAO"]

**Normalization:** Case-insensitive; exact match for acronym

**Grading:** Accept "DAO" | **Common incorrect:** "Parity", "Mt. Gox", "Ronin"

**Rationale:** The DAO hack highlighted the critical need for smart contract auditing before deployment. Reentrancy protection uses checks-effects-interactions pattern and mutex locks. [Ref: A29, L6]

---

#### Item 32: Front-Running Attack Prevention

**Difficulty:** Advanced

**Statement:** Front-running attacks occur when attackers observe pending transactions in a mempool and submit their own transaction with higher gas fees to execute first. Prevention techniques include ___ (committing to actions off-chain) and encrypted mempools.

**Acceptable Answers:** ["commit-reveal", "commit-reveal schemes"]

**Normalization:** Case-insensitive; accept with or without hyphen

**Grading:** Accept "commit-reveal" or "commit-reveal schemes" | **Common incorrect:** "MEV", "slippage", "sandwich"

**Rationale:** Commit-reveal splits transactions into two phases: commit (encrypted) then reveal. Proposer-builder separation and private pools (Flashbots) also mitigate MEV. [Ref: G11]

---

#### Item 33: Key Derivation and HD Wallets

**Difficulty:** Intermediate

**Statement:** Hierarchical Deterministic (HD) wallets use a single master seed and apply ___ (as defined in BIP-32) to derive child keys deterministically, enabling users to manage multiple addresses/chains from one seed phrase.

**Acceptable Answers:** ["key derivation", "derivation path"]

**Normalization:** Case-insensitive; trim whitespace

**Grading:** Accept "key derivation" or "derivation path" | **Common incorrect:** "key generation", "seeding", "stretching"

**Rationale:** BIP-32 hierarchical derivation \(m/44'/0'/0'/0/0\) enables structuring wallets across multiple accounts, change addresses, and external/internal chains. Essential for managing multiple blockchains from single entropy source. [Ref: G12]

---

#### Item 34: Custody Risk: Single Point of Failure

**Difficulty:** Intermediate

**Statement:** Centralized custody introduces a ___ where a single compromised key, stolen HSM, or insider threat can result in permanent loss of all customer funds without recourse.

**Acceptable Answers:** ["single point of failure", "SPOF"]

**Normalization:** Case-insensitive; accept acronym or full form

**Grading:** Accept "SPOF" or "single point of failure" | **Common incorrect:** "vulnerability", "attack vector", "risk"

**Rationale:** MPC and threshold signatures distribute risk across multiple parties/devices, eliminating single-point failures. No individual can unilaterally sign transactions or access funds. [Ref: A1, L2]

---

#### Item 35: Compliance Framework for Digital Asset Custody

**Difficulty:** Advanced

**Statement:** Institutional digital asset custody must comply with regulatory standards including ___ (operational risk frameworks for banks), ISO 27001 (information security), and SOC 2 Type 2 (service organization controls).

**Acceptable Answers:** ["Basel III"]

**Normalization:** Case-insensitive; exact match for standard name

**Grading:** Accept "Basel III" | **Common incorrect:** "Basel II", "Dodd-Frank", "MiFID"

**Rationale:** Basel III sets operational risk capital requirements. Combined with HSM FIPS 140-2 Level 3+ compliance and multi-factor authentication, these frameworks define institutional-grade custody. [Ref: A11, A30]

---

#### Item 36: Attack Surface Modeling in Wallet Development

**Difficulty:** Advanced

**Statement:** Comprehensive security requires modeling the attack surface across all layers: device compromise (malware on phone), transport compromise (man-in-the-middle), consensus compromise (51% attack), and smart contract flaws, with ___ and threat trees documenting exploit paths.

**Acceptable Answers:** ["STRIDE", "threat modeling"]

**Normalization:** Case-insensitive; accept STRIDE acronym or general term

**Grading:** Accept "STRIDE" or "threat modeling" | **Common incorrect:** "penetration testing", "code review", "auditing"

**Rationale:** STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) is a formal threat modeling framework. Wallet developers must document attack vectors at each layer and corresponding mitigations. [Ref: A28, G13]

---

## Reference Sections

---

### Glossary, Terminology & Acronyms

**Multi-Party Computation (MPC)**: Cryptographic protocol allowing multiple parties to jointly compute a function without any party revealing their input. [EN]

**Threshold Signature Scheme (TSS)**: Cryptographic system where a private key is split into shares and a threshold of participants must cooperate to produce a valid signature. [EN]

**Distributed Key Generation (DKG)**: Protocol for generating a shared secret among participants such that no party ever sees the complete key, eliminating trusted dealer. [EN]

**Shamir Secret Sharing (SSS)**: Technique to split a secret into n shares such that any k shares can reconstruct it, but k-1 shares reveal no information (perfect secrecy). [EN]

**Elliptic Curve Digital Signature Algorithm (ECDSA)**: Public-key signature scheme using elliptic curve cryptography, widely adopted in Bitcoin and Ethereum. [EN]

**Edwards-curve Digital Signature Algorithm (EdDSA)**: Deterministic signature scheme using Edwards curves, avoiding nonce-reuse vulnerabilities inherent in ECDSA. [EN]

**Schnorr Signature**: Non-interactive signature scheme based on discrete logarithm problem, used in threshold and MPC protocols (FROST, GG-family). [EN]

**Account Abstraction (AA)**: Blockchain architecture permitting smart contract wallets to serve as primary accounts without requiring private key management by users. [EN]

**ERC-4337**: Ethereum standard implementing account abstraction via UserOperations, EntryPoint contract, and Bundler infrastructure. [EN]

**Hardware Security Module (HSM)**: Tamper-resistant physical device for cryptographic operations, key generation, and secure key storage in institutional custody. [EN]

**Zero-Knowledge Proof (ZKP)**: Cryptographic proof demonstrating knowledge of a value without revealing the value itself, enabling privacy-preserving verification. [EN]

**Unspent Transaction Output (UTXO)**: Bitcoin transaction model where each coin is a discrete output; balance equals sum of all UTXOs controlled by an address. [EN]

---

### Codebase & Library References

**RustCrypto/ECDSA** (GitHub: RustCrypto/signatures | License: Apache 2.0 or MIT)
- Description: Pure Rust implementation of elliptic curve digital signatures (ECDSA) with support for NIST P-256, P-384, secp256k1.
- Stack: Rust, no_std compatible, cryptographic traits
- Maturity: Production (v0.16+)
- Performance: Constant-time ECDSA operations, minimal allocations
- Security: Implements RFC 6979 deterministic signatures, protects against timing attacks

**RustCrypto/Ed25519** (GitHub: RustCrypto/signatures | License: Apache 2.0 or MIT)
- Description: Pure Rust EdDSA implementation for Curve25519, deterministic and immune to nonce-reuse attacks.
- Stack: Rust, no_std, portable
- Maturity: Production
- Performance: Fast signature generation/verification on all platforms
- Security: Audited implementation, resistant to side-channel attacks

**Tendermint/Signatory** (GitHub: tendermint/signatory | License: Apache 2.0)
- Description: Multi-provider digital signature library for Tendermint validators, supporting hardware wallets and KMS backends.
- Stack: Rust, distributed signing
- Maturity: Production
- Integration: RPC interfaces for remote signing, Ledger/YubiHSM support
- Security: Audit status documented in repository

**zcash/frost-rs** (GitHub: zcash/frost-rs | License: MIT)
- Description: Reference implementation of FROST (Flexible Round-Optimized Schnorr Threshold Signatures) in Rust, enabling single-round signing.
- Stack: Rust, generic over curves
- Maturity: Experimental (undergoing IETF standardization)
- Performance: Single-round or two-round signing with preprocessing
- Security: Formal security proofs, threshold parameter flexibility

---

### Authoritative Literature & Reports

**FROST: Flexible Round-Optimized Schnorr Threshold Signatures** (Komlo & Goldberg, 2020) [EN]
- Authors: Chelsea Komlo (Zcash Foundation), Ian Goldberg (University of Waterloo)
- Type: Academic Paper (IEEE Symposium on Security and Privacy)
- Key Findings: FROST reduces Schnorr threshold signature rounds to two (or one with preprocessing), improving practicality for blockchain. Proves security against chosen-message attacks.
- Credibility: Peer-reviewed, now under IETF RFC standardization
- Jurisdiction: International standard

**Threshold ECDSA with an Offline Recovery Party** (Gennaro et al., 2021) [EN]
- Authors: Rosario Gennaro, Steven Goldfeder, et al.
- Type: Academic Paper (Cryptographic Protocols)
- Key Findings: First threshold ECDSA protocol allowing offline participant during key generation; practical for custody where recovery device stays offline.
- Credibility: Academic research, implemented in production MPC wallets
- Jurisdiction: International

**MPC Wallets: A Complete Technical Guide** (Stackup, 2025) [EN]
- Authors: Stackup (Industry)
- Type: Technical Report/Whitepaper
- Key Findings: Comprehensive overview of MPC wallet architecture, DKG protocols, signing rounds (GG18 nine rounds → GG20 → CGGMP21 four rounds). Analysis of security/performance tradeoffs.
- Credibility: Industry standard reference
- Jurisdiction: Global Web3

**Account Abstraction, Analysed** (Academic Paper, 2023) [EN]
- Type: Technical Analysis (IEEE/Academic)
- Key Findings: Comprehensive review of ERC-4337 implementation, security analysis of smart contract wallets, comparison with traditional EOA model.
- Credibility: Peer-reviewed
- Jurisdiction: Ethereum/EVM

**Secure Key Management for Blockchain Applications** (Fortanix, 2023) [EN]
- Authors: Fortanix (Industry/Security)
- Type: Industry White Paper
- Key Findings: Analysis of key management challenges (Mt. Gox, Coincheck hacks), comparison of software KMS vs. HSM vs. MPC. Tiered security model: hot wallets (frequent), cold storage (infrequent).
- Credibility: Industry leader in TEE and HSM
- Jurisdiction: Enterprise custody standards

---

### APA Style Source Citations

Komlo, C., & Goldberg, I. (2020). FROST: Flexible round-optimized Schnorr threshold signatures. In *Proceedings of the ACM CCS 2020 Workshop on Scalable and Resilient Infrastructures for Distributed Ledgers*. [EN]

Gennaro, R., Goldfeder, S., & Narayanan, A. (2016). Threshold-optimal DSS. In *International Cryptology Conference* (pp. 588-612). Springer, Berlin, Heidelberg. [EN]

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system. Retrieved from https://bitcoin.org/bitcoin.pdf [EN]

Yoav Weiss et al. (2023). ERC-4337: Account abstraction via entry point contract specification. Ethereum Improvement Proposals. Retrieved from https://eips.ethereum.org/EIPS/eip-4337 [EN]

Gennaro, R., Goldfeder, S. (2018). Fast multiparty threshold ECDSA with fast trustless setup. In *Proceedings of the 2018 ACM SIGSAC Conference on Computer and Communications Security* (pp. 1179-1194). [EN]

National Institute of Standards and Technology. (2019). FIPS 140-2: Security requirements for cryptographic modules. Retrieved from https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.140-2.pdf [EN]

Cloud Security Alliance. (2024). Hardware Security Module Security Considerations. Retrieved from https://cloudsecurityalliance.org/ [EN]

Fireblocks. (2025). Digital asset custody and transaction processing leading practices using Fireblocks MPC solution. Industry Report. [EN]

Shamir, A. (1979). How to share a secret. *Communications of the ACM*, 22(11), 612-613. [EN]

Blaize.Security. (2024). Crypto wallet security audit services: Best practices. Retrieved from https://security.blaize.tech/wallet-security-audit/ [EN]

Seurin, Y. (2012). On the exact security of Schnorr-type signatures in the random oracle model. In *Annual International Conference on the Theory and Applications of Cryptographic Techniques* (pp. 554-571). Springer, Berlin, Heidelberg. [EN]

The DAO Hack. (2016). DAO Vulnerability Post-Mortem. Retrieved from https://blog.ethereum.org/2016/06/24/security-alert-do-not-send-ether-to-wallet-contracts/ [EN]
