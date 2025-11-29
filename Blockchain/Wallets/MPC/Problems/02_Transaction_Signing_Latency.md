# Transaction Signing Latency in MPC Wallets

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Engineering Team

## Problem Statement

1. **[Important]** Q: MPC wallet providers face significant transaction signing latency due to multi-round communication protocols, causing 10-30 second delays that degrade user experience and block high-frequency trading use cases. Formulate a structured problem statement using the following [Input] fields.
   
   A:
   - **Brief description of the problem to be analyzed**: 
     MPC wallet signing requires 4-9 communication rounds between distributed parties, resulting in 2-5 second latency on good connections and 10-30 seconds on poor connections, compared to <1 second for hardware wallets. This affects est. 50M+ users across DeFi, trading, and consumer wallet applications, causing 15-25% cart abandonment in crypto payments and blocking time-sensitive trading strategies requiring <100ms execution.
   
   - **Background and current situation**: 
     MPC threshold signature protocols require multiple communication rounds: GG18 uses 9 rounds, GG20 uses 6 rounds, CGGMP21 uses 4 rounds for signing [Guide: Stackup, 2024]. Network latency directly impacts signing speed: 2-5 seconds on good connections (50-100ms inter-party latency), 10-30 seconds on poor connections (200-500ms latency) or mobile networks [Guide: Stackup, 2024]. Hardware wallets sign in 1-2 seconds once connected, software EOA wallets sign instantly (<100ms) [Guide: Stackup, 2024]. Geographic distribution of key shares increases latency: same-region adds 1-2s overhead, cross-continental adds 3-5s, global distribution adds 5-10s [Guide: Stackup, 2024]. DeFi applications require <1s response for competitive trades, high-frequency trading needs <100ms, consumer payments expect <3s for acceptable UX [Blog: Dynamic, 2024].
   
   - **Goals and success criteria**: 
     Signing latency: 2-5s (current good connection) → <1s (min acceptable) / <500ms (target) / <200ms (ideal) for same-region deployments by Q3 2025. Poor connection performance: 10-30s (current) → <3s (min) / <2s (target) / <1s (ideal) for mobile/high-latency networks. Protocol efficiency: 4-9 rounds (current: GG18/GG20/CGGMP21) → 2-3 rounds (target) / 1-2 rounds (ideal) through protocol optimization. User experience: reduce crypto payment cart abandonment from est. 15-25% → <10% (min) / <5% (target) by improving transaction confirmation time. High-frequency use cases: enable trading strategies requiring <100ms execution (currently blocked).
   
   - **Key constraints and resources**: 
     Timeline: Q1 2025 - Q3 2025 (6 months); Budget: $300K-$800K for protocol research + implementation + testing; Team: 2-3 cryptography researchers + 3-4 protocol engineers + 1-2 network optimization specialists; Technology: Cannot eliminate multi-round communication (fundamental to MPC security), limited by network speed of light (40-80ms cross-continental RTT), must maintain security proofs equivalent to current protocols; Compatibility: Must support existing key shares (no forced migration), backward compatibility with current wallet deployments; Trade-offs: Security vs speed (reducing rounds may weaken security proofs), geographic distribution for security vs latency (collocation improves speed but reduces separation).
   
   - **Stakeholders and roles**: 
     End Users - DeFi Traders (est. 5M+ active, need <1s signing for competitive trading, constraint: will switch to hot wallets if latency >3s); End Users - Consumer Payment (est. 30M+, need <3s checkout experience, constraint: 15-25% abandon if >5s); Wallet Providers (10+ companies, need competitive performance vs hardware wallets, constraint: maintain 99.9% uptime during upgrades); DeFi Protocols (100+ applications, need fast transaction confirmation, constraint: cannot modify smart contracts to accommodate slow signing); High-Frequency Traders (est. 1000+ institutional, need <100ms execution, constraint: currently cannot use MPC wallets); Developers (500+ integrating MPC wallets, need predictable latency SLAs, constraint: limited ability to optimize network infrastructure).
   
   - **Time scale and impact scope**: 
     Timeline: Q1 2025 - Q3 2025 (6 months research + implementation); Systems: Threshold signature protocols (ECDSA, EdDSA), network communication layer, key share coordination services, signing request queues; Scale: est. 50M+ users across consumer wallets + DeFi + institutional custody, 10+ major MPC wallet providers, 100+ DeFi protocol integrations; Performance Impact: 2-30s current latency → target <1s (50-95% improvement); Use Cases: DeFi trading, crypto payments, institutional custody, cross-chain bridges, NFT marketplaces; Regions: Global (latency particularly problematic for cross-continental deployments).
   
   - **Historical attempts and existing solutions (if any)**: 
     2018-2020: Protocol evolution reduced rounds: GG18 (9 rounds) → GG20 (6 rounds) → CGGMP21 (4 rounds), achieving 30-50% latency reduction but still 2-5s minimum [Guide: Stackup, 2024]. 2023: DKLs19 for ECDSA and FROST for EdDSA deployed by Dynamic, optimizing round efficiency [Blog: Dynamic, 2024]. 2024: Offline/online phase splitting explored, moving heavy computation to offline phase to reduce online signing latency by 40-60%, but adds complexity and requires pre-computation [Blog: Dynamic, 2024]. 2024: Network optimization via CDN-style key share placement reduces same-region latency to 1-2s, but cross-region remains 3-5s [Guide: Stackup, 2024]. Key lesson: Fundamental trade-off between security (requires multiple rounds) and speed (each round adds RTT latency); cannot eliminate multi-round communication without compromising MPC security model.
   
   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: CGGMP21 requires 4 signing rounds (minimum for current security proofs) [Guide: Stackup, 2024]; Good connections: 2-5s signing latency, poor connections: 10-30s [Guide: Stackup, 2024]; Hardware wallets: 1-2s, software EOA: <100ms [Guide: Stackup, 2024]; Same-region: 1-2s overhead, cross-continental: 3-5s, global: 5-10s [Guide: Stackup, 2024]; DKLs19 and FROST used by Dynamic for round optimization [Blog: Dynamic, 2024].
     - **Assumptions**: est. 50M+ users affected (inferred from major provider user bases: Coinbase 108M users, extrapolated to MPC wallet subset ~30-50% adoption); 15-25% payment cart abandonment (typical e-commerce benchmark for >5s checkout delays, applied to crypto payments); est. 5M DeFi traders, 30M consumer payment users, 1000+ HFT firms (market sizing based on DeFi TVL $80B → est. 5-10% active traders); $300K-$800K budget (2-3 researchers × 6 months × $200K salary + 3-4 engineers × 6 months × $150K salary + $50K testing infrastructure).
     - **Uncertainties**: Minimum achievable rounds without compromising security unknown (theoretical limit may be 2-3 rounds, but security proofs TBD); Offline/online phase splitting impact on real-world performance unknown (requires load testing); User tolerance threshold for latency unknown (3s? 5s? varies by use case); Network optimization potential unexplored (CDN, edge computing, dedicated fiber may reduce latency 20-40%); Quantum-resistant MPC protocols may require additional rounds (future compatibility concern).

---

## Glossary

- **Cart abandonment**: Percentage of users who initiate but don't complete transactions; typical e-commerce threshold >5s causes 15-25% abandonment.
- **CGGMP21**: Modern threshold ECDSA protocol requiring 4 signing rounds, offering best current balance of security and performance.
- **DeFi (Decentralized Finance)**: Blockchain-based financial applications (lending, trading, liquidity provision) requiring fast transaction signing for competitive execution.
- **DKLs19**: Threshold ECDSA protocol optimized for 2-party signing, used by Dynamic and other providers for consumer wallets.
- **EOA (Externally Owned Account)**: Traditional blockchain wallet controlled by single private key, signing instantly (<100ms) but vulnerable to key loss.
- **FROST (Flexible Round-Optimized Schnorr Threshold)**: Efficient threshold signature protocol for EdDSA (Ed25519), requiring 2 signing rounds.
- **GG18/GG20**: Earlier threshold ECDSA protocols requiring 9 and 6 rounds respectively, superseded by CGGMP21's 4-round design.
- **High-frequency trading (HFT)**: Automated trading strategies executing in <100ms to exploit brief price discrepancies; currently incompatible with MPC wallet latency.
- **Multi-round communication**: MPC protocol requirement where parties exchange messages in sequential rounds; each round adds one network round-trip time (RTT) to latency.
- **Offline/online phase**: Protocol optimization splitting heavy computation (offline, pre-computed) from time-sensitive signing (online, <1s).
- **RTT (Round-Trip Time)**: Network latency for message to travel to recipient and response to return; same-region 10-50ms, cross-continental 80-200ms.
- **Threshold signature**: Distributed signing requiring k-of-n parties to cooperate, fundamental to MPC security but necessitating multi-round protocols.

---

## Reference

### Technical Guides & Documentation
- [Guide: Stackup, 2024] - "MPC Wallets: A Complete Technical Guide" section on performance benchmarks (https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide)
- [Blog: Dynamic, 2024] - "The Evolution of MPC: From Secure but Slow to Fast and Scalable" (https://www.dynamic.xyz/blog/the-evolution-of-mpc)

### Research Papers
- [Paper: Canetti et al., 2020] - "UC Non-Interactive, Proactive, Threshold ECDSA" (CGGMP21) (https://eprint.iacr.org/2021/060)
- [Paper: Gennaro & Goldfeder, 2019] - "One Round Threshold ECDSA" (GG20) (https://eprint.iacr.org/2020/540)
- [Paper: Doerner et al., 2018] - "Threshold ECDSA from ECDSA Assumptions" (DKLs19)
- [Paper: Komlo & Goldberg, 2020] - "FROST: Flexible Round-Optimized Schnorr Threshold Signatures" (https://eprint.iacr.org/2020/852)

### Industry Reports
- [Report: Coinbase Q3 2023] - User base statistics (108M verified users)
- [Report: DeFi Llama, 2024] - Total Value Locked (TVL) statistics for DeFi market sizing
