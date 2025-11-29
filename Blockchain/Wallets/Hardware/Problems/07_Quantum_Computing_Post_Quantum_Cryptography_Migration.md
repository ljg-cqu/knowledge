# Quantum Computing Post Quantum Cryptography Migration

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Engineering and Security Team

## Problem Statement

1. **[CRITICAL]** Q: Hardware wallet manufacturers face existential quantum computing threat with cryptographically relevant quantum computers (CRQCs) expected by 2030-2035, enabling "harvest now, decrypt later" attacks on billions in cryptocurrency assets secured by current ECDSA/EdDSA cryptography, requiring urgent migration to NIST-standardized post-quantum cryptography (PQC) before quantum capability threshold. Formulate a structured problem statement using the following [Input] fields.
   
   A:
   - **Brief description of the problem to be analyzed**: 
     Quantum computers threaten to break current hardware wallet cryptography (ECDSA, EdDSA) by 2030-2035, exposing billions in cryptocurrency to "harvest now, decrypt later" attacks where adversaries collect encrypted blockchain data today for future decryption. Federal Reserve and NIST warn of strategic urgency, with NIST recommending migration to post-quantum cryptography by 2035. Hardware wallet industry ($582.98M market, 10M+ users) must integrate NIST-standardized PQC algorithms into new devices and provide migration path for existing users by Q2 2030 to prevent catastrophic asset loss.
   
   - **Background and current situation**: 
     Current hardware wallets use quantum-vulnerable cryptography: ECDSA (Bitcoin, Ethereum), EdDSA (Solana, Cardano), Schnorr (Bitcoin Taproot) [Web: Fireblocks, 2025]. Cryptographically relevant quantum computers expected 2030-2035, with some predictions suggesting threat shortly after 2030 [Web: Fortune, 2025; Web: Cointelegraph, 2025]. "Harvest now, decrypt later" (HNDL) attacks enable adversaries to collect blockchain transaction data now and decrypt later when quantum capability achieved [Web: Federal Reserve, 2025; Web: Palo Alto Networks, 2025]. NIST published first 3 post-quantum cryptography standards in 2024, recommending migration by 2035 [Web: Chaincode, 2025; Web: Cointelegraph, 2025]. SEALSQ launched Quantum Shield QS7001 chip with NIST PQC algorithms in November 2025, first hardware implementation [Web: SEALSQ, 2025]. Industry quantum readiness target: 2030 [Web: Fireblocks, 2025]. Current state: zero major hardware wallet manufacturers (Ledger, Trezor, Tangem) have shipped PQC-enabled devices; existing 10M+ devices vulnerable; no standardized blockchain PQC migration protocols.
   
   - **Goals and success criteria**: 
     PQC device availability: 0 models → ≥2 major manufacturers shipping PQC hardware wallets by Q2 2028 (min) / Q4 2027 (target) / Q2 2027 (ideal); User migration: 0% → >50% users on PQC-capable devices by Q2 2030 (min) / >70% by Q4 2029 (target) / >90% by Q2 2029 (ideal); Asset protection: 0 → zero successful quantum attacks on migrated assets (target); Industry readiness: establish PQC migration standards adopted by ≥3 major manufacturers by Q4 2026 (target); Cost: PQC device premium <30% over current models (target) / <15% (ideal); Backward compatibility: maintain access to legacy wallets during migration period (min).
   
   - **Key constraints and resources**: 
     Timeline: Q1 2026-Q2 2030 (4.5 years to NIST deadline, 4-5 years to CRQC threat); Budget: $2M-$5M per manufacturer for PQC R&D (chip integration, firmware development, cryptographic library implementation, security audits, user migration tooling); Team: 5-8 cryptographic engineers + 3-5 firmware engineers + 2-3 hardware engineers + 2 security auditors + 1 PM + 1 blockchain protocol specialist; Tech: NIST-standardized PQC algorithms (ML-KEM, ML-DSA, SLH-DSA), quantum-resistant secure elements (e.g., SEALSQ QS7001, CNSA 2.0 compliant), increased storage/RAM for larger PQC signatures (2-4KB vs. 64-72 bytes ECDSA), backward compatibility with legacy ECDSA wallets; Security: maintain EAL5+ certification, resist side-channel attacks on PQC implementations; Blockchain: coordinate with protocol developers (Bitcoin, Ethereum) for network-level PQC adoption; Regulatory: align with CNSA 2.0 (NSA quantum-resistant standards), NIST migration guidelines.
   
   - **Stakeholders and roles**: 
     Cryptocurrency Users (10M+ hardware wallet users, billions in assets at risk, need PQC migration path by 2029, minimal disruption), Hardware Wallet Manufacturers (Ledger, Trezor, Tangem, KeepKey, need PQC product roadmap, maintain competitive position in $582.98M market), Secure Element Vendors (SEALSQ, NXP, STMicroelectronics, need PQC chip production capacity, NIST/CNSA 2.0 compliance), Blockchain Protocol Developers (Bitcoin Core, Ethereum Foundation, need network PQC upgrade coordination, soft fork/hard fork planning), Cryptography Researchers (NIST, academic institutions, need standardization guidance, implementation best practices), Regulatory Bodies (NSA, NIST, need compliance verification, migration enforcement), Institutional Investors (billions in custody, need quantum-safe storage guarantees, audit trails).
   
   - **Time scale and impact scope**: 
     Timeline: Q1 2026-Q2 2030 (4.5 years); Long-term: 2030-2035 CRQC threat window; Affected systems: hardware wallet secure elements, cryptographic libraries, firmware, blockchain protocols (address formats, transaction signing, consensus), companion apps (Ledger Live, Trezor Suite); Global scope: 10M+ users, $582.98M → $2.06B market (2025-2030), trillions in cryptocurrency market cap; Financial impact: catastrophic if unaddressed (potential loss of billions in harvested private keys post-CRQC), estimated $2M-$5M per manufacturer migration cost vs. existential brand/market risk; Technical debt: existing 10M+ devices require firmware updates or replacement program.
   
   - **Historical attempts and existing solutions (if any)**: 
     2024: NIST published first 3 post-quantum cryptography standards (ML-KEM, ML-DSA, SLH-DSA) after 8-year competition [Web: Cointelegraph, 2025]. November 2025: SEALSQ launched Quantum Shield QS7001, first NIST PQC-compliant secure element chip for Bitcoin wallets [Web: SEALSQ, 2025]. 2025: Federal Reserve published research warning of "harvest now, decrypt later" risks for blockchain networks [Web: Federal Reserve, 2025]. Industry discussions: Chaincode Labs published Bitcoin post-quantum migration analysis [Web: Chaincode, 2025]. No hardware wallet manufacturer has shipped PQC-enabled consumer device as of Nov 2025. Key lessons: PQC algorithms require 10-100x larger signatures/keys than ECDSA (storage/bandwidth challenge); blockchain network upgrades require multi-year coordination; early adopters gain security advantage but face compatibility risks; NIST standardization critical for industry alignment.
   
   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: Quantum computers expected 2030-2035 [Web: Fortune, 2025; Web: Cointelegraph, 2025]; "Harvest now, decrypt later" attacks enable data collection today for future quantum decryption [Web: Federal Reserve, 2025]; NIST recommends PQC migration by 2035 [Web: Chaincode, 2025]; SEALSQ QS7001 launched Nov 2025 with NIST PQC standards [Web: SEALSQ, 2025]; Industry quantum readiness target 2030 [Web: Fireblocks, 2025]; Hardware wallet market $582.98M (2025) → $2.06B (2030) [Web: CoinLaw, 2025]; Current wallets use ECDSA, EdDSA, Schnorr (all quantum-vulnerable) [Web: Fireblocks, 2025]
     - **Assumptions**: CRQC timeline 2030-2035 (based on expert consensus, but breakthrough could accelerate); Migration cost $2M-$5M per manufacturer (estimated from PQC R&D requirements: chip integration, cryptographic library development, firmware updates, security audits); User migration rate target >70% by 2029 (assumes 4-year adoption curve similar to SegWit/Taproot Bitcoin upgrades); Existing device count 10M+ (from market size $582.98M / avg price $50-$100); PQC signature size 2-4KB (NIST ML-DSA standard, vs. 64-72 bytes ECDSA, requires increased storage)
     - **Uncertainties**: Exact CRQC capability timeline (could arrive earlier or later than 2030-2035 window); Quantum computing cost/accessibility (will CRQCs be limited to nation-states, or commercially available?); Blockchain protocol PQC adoption timeline (Bitcoin/Ethereum network upgrades require years of consensus, coordination uncertain); User migration compliance rate (will users proactively upgrade, or require forced deprecation of legacy devices?); PQC algorithm longevity (NIST standards published 2024, but future cryptanalysis may reveal weaknesses); Cost of PQC secure elements at scale (SEALSQ QS7001 pricing not public, volume production economics unclear); Backward compatibility solutions (dual-mode devices supporting both ECDSA and PQC, or clean break requiring asset migration?); "Harvest now, decrypt later" attack prevalence (unknown if adversaries actively collecting blockchain data at scale)

---

## Glossary

- **CNSA 2.0 (Commercial National Security Algorithm Suite 2.0)**: NSA's updated cryptographic standards requiring quantum-resistant algorithms for national security systems, effective 2025-2030 transition period.
- **CRQC (Cryptographically Relevant Quantum Computer)**: Quantum computer with sufficient qubits and error correction to break current public-key cryptography (ECDSA, RSA), estimated capability 2030-2035.
- **ECDSA (Elliptic Curve Digital Signature Algorithm)**: Widely used signature scheme in Bitcoin, Ethereum, and other blockchains, vulnerable to quantum Shor's algorithm enabling private key derivation from public key.
- **EdDSA (Edwards-curve Digital Signature Algorithm)**: Alternative signature scheme used by Solana, Cardano, Monero, also quantum-vulnerable but offers performance benefits over ECDSA in pre-quantum era.
- **Harvest Now, Decrypt Later (HNDL)**: Attack strategy where adversaries collect encrypted data now and store it for future decryption when quantum computers capable of breaking encryption become available.
- **ML-DSA (Module-Lattice-Based Digital Signature Algorithm)**: NIST-standardized post-quantum signature scheme (formerly CRYSTALS-Dilithium), generates 2-4KB signatures vs. 64-72 bytes ECDSA.
- **ML-KEM (Module-Lattice-Based Key Encapsulation Mechanism)**: NIST-standardized post-quantum key exchange algorithm (formerly CRYSTALS-Kyber), resistant to quantum attacks.
- **NIST (National Institute of Standards and Technology)**: US federal agency standardizing cryptographic algorithms, published first 3 post-quantum cryptography standards in 2024 after 8-year competition.
- **Post-Quantum Cryptography (PQC)**: Cryptographic algorithms designed to resist attacks from both classical and quantum computers, based on mathematical problems (lattices, hash functions) believed quantum-hard.
- **Quantum-Resistant**: Cryptographic scheme designed to withstand attacks from quantum computers, including Shor's algorithm (breaks RSA, ECDSA) and Grover's algorithm (weakens symmetric crypto).
- **SLH-DSA (Stateless Hash-Based Digital Signature Algorithm)**: NIST-standardized post-quantum signature scheme (formerly SPHINCS+), based on hash functions, offers conservative security but larger signatures than ML-DSA.
- **Shor's Algorithm**: Quantum algorithm enabling polynomial-time factorization (breaks RSA) and discrete logarithm solving (breaks ECDSA, EdDSA), rendering current public-key cryptography insecure.

---

## Reference

### Web Sources
- [Web: Federal Reserve, 2025] - "Harvest Now Decrypt Later": Examining Post-Quantum Cryptography and the Data Privacy Risks for Distributed Ledger Networks (https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm)
- [Web: Fortune, 2025] - Quantum computers could be powerful enough to decrypt Bitcoin sometime after 2030, CEO of Nvidia's quantum partner says (https://fortune.com/2025/11/19/quantum-computing-bitcoin-2030-nvidia-theau-peronnin)
- [Web: Cointelegraph, 2025] - Bitcoin vs. the quantum computer threat: Timeline and solutions (2025–2035) (https://cointelegraph.com/magazine/bitcoin-quantum-computer-threat-timeline-solutions-2024-2035)
- [Web: Fireblocks, 2025] - Quantum Computing & Crypto: Real Threat or Hype? Industry quantum readiness target 2030 (https://www.fireblocks.com/blog/quantum-risk-in-crypto-what-institutions-need-to-know)
- [Web: Chaincode, 2025] - Bitcoin Post-Quantum: NIST recommends migration by 2035 (https://chaincode.com/bitcoin-post-quantum.pdf)
- [Web: SEALSQ, 2025] - SEALSQ Unveils Quantum-Resistant Cryptography with QS7001 to Secure Bitcoin Wallets Against Quantum Threat, launched November 2025 (https://www.sealsq.com/investors/news-releases/sealsq-unveils-quantum-resistant-cryptography-with-qs7001-to-secure-bitcoin-wallets-against-quantum-threat)
- [Web: Palo Alto Networks, 2025] - Harvest Now, Decrypt Later (HNDL): The Quantum-Era cybersecurity threat (https://www.paloaltonetworks.com/cyberpedia/harvest-now-decrypt-later-hndl)
- [Web: CoinLaw, 2025] - Hardware wallet market statistics: $582.98M (2025) → $2.06B (2030) (https://coinlaw.io/hardware-wallet-market-statistics)
