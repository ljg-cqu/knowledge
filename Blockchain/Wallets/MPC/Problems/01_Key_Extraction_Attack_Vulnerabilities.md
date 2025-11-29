# Key-Extraction Attack Vulnerabilities in MPC Wallet Implementations

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Security Team

## Problem Statement

1. **[CRITICAL]** Q: MPC wallet providers face critical key-extraction vulnerabilities in threshold ECDSA implementations, exposing hundreds of millions of users and billions in digital assets to private key compromise. Formulate a structured problem statement using the following [Input] fields.
   
   A:
   - **Brief description of the problem to be analyzed**: 
     Implementation flaws in widely-deployed threshold ECDSA protocols (Lindell17, GG18/20) enable attackers to extract complete private keys through 16-256 malicious signing requests, affecting major wallet providers (Coinbase WaaS, ZenGo, Binance, BitGo) serving est. 100M+ users. Private key compromises accounted for 43.8% of $2.2B crypto losses in 2024, with MPC wallets representing critical infrastructure requiring immediate remediation.
   
   - **Background and current situation**: 
     Major MPC wallet providers deployed threshold ECDSA implementations (2018-2023) based on Lindell17 (2-of-2) and GG18/20 (n-of-n) protocols [Research: Fireblocks, 2023]. Lindell17 vulnerability allows key extraction via 256 test messages when servers fail to abort after invalid signatures [Paper: Makriyannis & Yomtov, 2023]. GG18/20 vulnerability exploits weak Paillier public key validation, enabling attackers to recover key shares modulo small primes through 16 malicious signing ceremonies [Paper: Makriyannis & Yomtov, 2023]. Affected providers include ZenGo, Coinbase WaaS (Lindell17), Binance bnb-chain, ING Bank, BitGo (GG18/20) [Paper: Fireblocks, 2023]. Industry-wide private key compromises totaled $964M in 2024 (43.8% of $2.2B crypto theft) [Report: Chainalysis, 2024].
   
   - **Goals and success criteria**: 
     Security: Eliminate key-extraction vulnerabilities → 0 exploitable implementations (current: 5+ major providers affected) by Q2 2025. Detection: Implement attack detection → <100ms detection latency, 100% identification rate for test message patterns. Remediation: Deploy fixes across all providers → 100% vulnerable implementations patched within 3 months of disclosure. User protection: Zero successful key extractions → 0 private key compromises via this attack vector (compared to est. $964M annual private key losses). Validation: Achieve third-party security audits → ≥2 independent audits confirming vulnerability closure by Q2 2025.
   
   - **Key constraints and resources**: 
     Timeline: Q4 2024 - Q2 2025 (6 months); Budget: $200K-$500K per provider for security audit + remediation (est. $2M-$5M industry-wide); Team: 2-3 cryptography engineers + 1-2 security auditors per provider; Technology: CGGMP20 zero-knowledge proofs for Paillier key validation, protocol abort mechanisms for invalid signature detection; Policy: Coordinated vulnerability disclosure completed (Fireblocks → affected providers, July-September 2023); Dependencies: Cannot force immediate user key rotation due to UX impact; Limitations: Backward compatibility required for existing key shares.
   
   - **Stakeholders and roles**: 
     MPC Wallet Providers (5+ companies, need 0 exploitable implementations, constraint: <6 month remediation window + maintain 99.9% uptime); End Users (est. 100M+ digital asset holders, need asset security guarantees, constraint: no forced key migration); Security Researchers (Fireblocks team + auditors, need reproducible attack demonstrations, constraint: responsible disclosure timelines); Cryptocurrency Exchanges (integrate with MPC wallets, need security certifications, constraint: cannot suspend services during fixes); Regulators (financial authorities, need compliance with custody requirements, constraint: must maintain audit trails during remediation).
   
   - **Time scale and impact scope**: 
     Timeline: Q4 2024 - Q2 2025 (6 months remediation); Systems: Threshold ECDSA signing protocols (Lindell17, GG18/20), Paillier homomorphic encryption validation, signature generation services, key management infrastructure; Scale: 5+ major providers, est. 100M+ users, est. $50B+ assets under custody; Risk: Potential $964M+ annual losses from private key compromise (43.8% of $2.2B 2024 crypto theft); Regions: Global (providers operate worldwide); Industry: Cryptocurrency custody, digital asset wallets, institutional crypto services.
   
   - **Historical attempts and existing solutions (if any)**: 
     2020: CGGMP20 protocol published with enhanced Paillier key validation proofs, adopted by newer implementations but not retrofitted to GG18/20 deployments [Paper: Canetti et al., 2020]. 2023: Fireblocks discovered vulnerabilities, performed coordinated disclosure to affected providers (July-September 2023) [Paper: Makriyannis & Yomtov, 2023]. Post-disclosure: ZenGo, Coinbase, Safeheron implemented fixes (Q3-Q4 2023) adding zero-knowledge proofs for Paillier keys and abort mechanisms for invalid signatures [Blog: Fireblocks, 2023]. Key lesson: Protocol security proofs assume prerequisites (abort-on-failure, valid public keys) that implementations must strictly enforce; gap between theoretical security and practical deployment creates critical vulnerabilities.
   
   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: Lindell17 vulnerability requires 256 signing requests to extract 256-bit key [Paper: Makriyannis & Yomtov, 2023]; GG18/20 vulnerability requires 16 signing requests with malicious Paillier keys [Paper: Makriyannis & Yomtov, 2023]; 43.8% of $2.2B crypto theft in 2024 from private key compromises [Report: Chainalysis, 2024]; Major providers (ZenGo, Coinbase WaaS, Binance, BitGo, ING Bank) confirmed affected [Paper: Fireblocks, 2023]; CGGMP20 provides necessary zero-knowledge proofs for mitigation [Paper: Canetti et al., 2020].
     - **Assumptions**: est. 100M+ users affected (inferred from major provider market share: Coinbase 108M users Q3 2023, ZenGo est. 1M+ users, extrapolated to affected provider base [Report: Coinbase Q3 2023]); est. $50B+ assets under custody (inferred from Coinbase institutional custody $130B as market benchmark [Report: Coinbase, 2023]); $200K-$500K remediation cost per provider (based on typical security audit $50K-$100K + engineering effort 2-3 engineers × 3 months × $150K annual salary / 12).
     - **Uncertainties**: Actual exploitation in the wild unknown (no public reports of successful attacks, but detection difficulty makes silent exploitation possible); Complete list of affected implementations unknown (only disclosed providers confirmed); Timeline for smaller providers to implement fixes unknown; User impact if forced key rotation required (UX degradation, potential lockout scenarios).

---

## Glossary

- **CGGMP20**: UC Non-Interactive, Proactive, Threshold ECDSA protocol by Canetti, Gennaro, Goldfeder, Makriyannis, Peled (2020) with enhanced zero-knowledge proofs for secure distributed key generation and signing.
- **ECDSA**: Elliptic Curve Digital Signature Algorithm, widely used in cryptocurrencies (Bitcoin, Ethereum) for transaction signing.
- **GG18/GG20**: Threshold ECDSA protocols by Gennaro and Goldfeder (2018, 2020) enabling multi-party signing without reconstructing private keys.
- **Key extraction attack**: Cryptographic attack that recovers complete private key by exploiting protocol implementation weaknesses through malicious signing requests.
- **Lindell17**: Two-party ECDSA protocol by Yehuda Lindell (2017) used for 2-of-2 threshold signatures in consumer MPC wallets.
- **MPC (Multi-Party Computation)**: Cryptographic technique enabling parties to jointly compute functions over inputs while keeping inputs private; used in wallets to distribute private key shares.
- **Paillier encryption**: Homomorphic encryption scheme used in threshold ECDSA protocols, requiring public key N = pq where p, q are large primes.
- **Private key compromise**: Unauthorized access to cryptographic keys controlling digital assets, representing 43.8% of cryptocurrency theft in 2024.
- **Threshold signature**: Digital signature scheme requiring k-of-n parties to cooperate for signing, preventing single point of failure.
- **Zero-knowledge proof**: Cryptographic proof allowing one party to prove statement correctness (e.g., N = pq with p, q prime) without revealing underlying secrets.

---

## Reference

### Research Papers & Technical Reports
- [Paper: Makriyannis & Yomtov, 2023] - "Practical Key-Extraction Attacks in Leading MPC Wallets", Fireblocks (https://eprint.iacr.org/2023/1234)
- [Paper: Canetti et al., 2020] - "UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts" (CGGMP20) (https://eprint.iacr.org/2021/060)
- [Paper: Lindell, 2017] - "Fast Secure Two-Party ECDSA Signing" (https://eprint.iacr.org/2017/552)
- [Paper: Gennaro & Goldfeder, 2018] - "Fast Multiparty Threshold ECDSA with Fast Trustless Setup" (GG18) (https://eprint.iacr.org/2019/114)

### Industry Reports & Statistics
- [Report: Chainalysis, 2024] - "Crypto Crime Report 2025: $2.2 Billion Stolen in 2024, 43.8% from Private Key Compromises" (https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2025)
- [Report: Coinbase Q3 2023] - Quarterly earnings report citing 108M verified users
- [Report: Coinbase, 2023] - Institutional custody assets under management $130B

### Blog Posts & Disclosures
- [Blog: Fireblocks, 2023] - Vulnerability disclosure and remediation guidance for affected MPC wallet providers
- [Blog: ZAN, 2023] - "Attacks and Remediation for MPC Wallets" technical analysis (https://medium.com/@zan.top/attacks-and-remediation-for-mpc-wallets-8a462be49c63)

### Technical Guides
- [Guide: Stackup, 2024] - "MPC Wallets: A Complete Technical Guide" (https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide)
