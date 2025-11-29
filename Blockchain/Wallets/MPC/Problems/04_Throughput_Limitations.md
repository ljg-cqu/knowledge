# Network Throughput Limitations in MPC Signing

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Infrastructure Team

## Problem Statement

1. **[Important]** Q: MPC wallet signing infrastructure faces severe throughput constraints with maximum 10-500 transactions per minute, blocking high-frequency trading, mass payment processing, and DeFi market maker applications requiring thousands of transactions per minute. Formulate a structured problem statement using the following [Input] fields.
   
   A:
   - **Brief description of the problem to be analyzed**: 
     MPC multi-round communication protocols limit signing throughput to 10-20 TPS for consumer implementations and 50-100 TPS for enterprise solutions, with highly optimized deployments reaching maximum 500 TPS. This blocks use cases requiring >1000 TPS (high-frequency trading, automated market making, mass payment distribution, MEV extraction), forcing institutional traders and DeFi protocols to use less secure hot wallet alternatives or abandon MPC entirely.
   
   - **Background and current situation**: 
     Consumer MPC implementations (ZenGo, Coinbase WaaS) handle 10-20 transactions per minute (0.17-0.33 TPS) due to mobile device constraints and network latency [Guide: Stackup, 2024]. Enterprise solutions (Fireblocks, Copper) achieve 50-100 transactions per minute (0.83-1.67 TPS) with optimized server infrastructure [Guide: Stackup, 2024]. Highly optimized deployments reach maximum 500 transactions per minute (8.33 TPS) but rarely exceed this due to coordination overhead [Guide: Stackup, 2024]. By comparison, hot wallets (single-key EOAs) can sign 10,000+ TPS limited only by CPU, and hardware wallets handle 100-200 TPS [Guide: Stackup, 2024]. Blocked use cases include: high-frequency trading (needs 1000-10,000 TPS for arbitrage strategies), automated market making (needs 500-2000 TPS for liquidity provision), mass payments (payroll, airdrops need 1000+ TPS for timely distribution), MEV extraction (needs <100ms latency + 1000+ TPS for competitive block building).
   
   - **Goals and success criteria**: 
     Consumer throughput: 10-20 TPM (current) → 100 TPM (min) / 300 TPM (target) / 600 TPM (ideal) by Q4 2025. Enterprise throughput: 50-100 TPM (current) → 500 TPM (min) / 1500 TPM (target) / 3000 TPM (ideal) by Q4 2025. High-performance specialized: 500 TPM (current max) → 3000 TPM (min) / 6000 TPM (target) / 10,000+ TPM (ideal) for institutional HFT use cases by Q1 2026. Use case enablement: Currently 0% of HFT and AMM use MPC → ≥20% adoption (min) / ≥40% (target) / ≥60% (ideal) by Q4 2025. Cost efficiency: Maintain <$0.02 per signature (current enterprise pricing) while scaling throughput.
   
   - **Key constraints and resources**: 
     Timeline: Q1 2025 - Q1 2026 (12 months research + deployment); Budget: $800K-$2M for protocol optimization + infrastructure scaling + benchmarking; Team: 2-3 cryptography researchers + 4-5 infrastructure engineers + 1-2 performance engineers; Technology: Cannot eliminate multi-round communication (fundamental MPC security requirement), limited by network bandwidth (1-10 Gbps typical datacenter), CPU-bound cryptographic operations (ECDSA signing ~1ms per operation), coordination overhead scales with concurrent signing sessions; Trade-offs: Parallelization requires more key shares (increased attack surface), batching increases latency for individual transactions, specialized hardware (TPUs, FPGAs) adds cost and complexity; Compatibility: Must support existing protocols (ECDSA, EdDSA for blockchain compatibility).
   
   - **Stakeholders and roles**: 
     High-Frequency Trading Firms (est. 200+ institutional, need 1000-10,000 TPS, constraint: currently cannot use MPC wallets, losing $50M-$200M annual revenue opportunities); DeFi Market Makers (est. 50+ major protocols, need 500-2000 TPS for liquidity provision, constraint: forced to use hot wallets risking key compromise); Cryptocurrency Exchanges (20+ major platforms, need 1000+ TPS for withdrawal processing, constraint: MPC throughput limits batch processing windows); Payroll & Airdrop Platforms (100+ services, need 1000+ TPS for timely mass distributions, constraint: must split payouts across 6-12 hour windows); MPC Wallet Providers (10+ companies, need competitive throughput vs hot wallets, constraint: $0.02 per signature pricing ceiling limits infrastructure investment); Enterprise Customers (500+ institutions, need predictable throughput SLAs, constraint: cannot deploy if peak load exceeds capacity).
   
   - **Time scale and impact scope**: 
     Timeline: Q1 2025 - Q1 2026 (12 months); Systems: MPC signing servers, network communication layer, cryptographic computation pipeline, request queuing and load balancing, key share coordination services; Scale: 10+ MPC wallet providers, 200+ HFT firms, 50+ DeFi protocols, 100+ payment platforms, est. $500M-$2B annual revenue blocked by throughput limitations; Current state: 10-500 TPM (0.17-8.33 TPS) blocks >90% of high-throughput use cases; Target: 3000-10,000+ TPM (50-167+ TPS) enables 60-80% of blocked use cases; Industry impact: MPC currently <5% of institutional crypto infrastructure, throughput improvements could increase to 20-40% by enabling HFT and AMM adoption.
   
   - **Historical attempts and existing solutions (if any)**: 
     2019-2021: Parallelization explored via multiple independent key shares, achieving 2-5x throughput but increasing attack surface and key management complexity; abandoned due to security concerns [implied from Guide: Stackup, 2024]. 2022: Batching multiple transactions into single signing ceremony tested, reducing per-transaction overhead by 40-60% but increasing latency for individual transactions from 2s to 5-10s; unsuitable for time-sensitive use cases [Blog: Dynamic, 2024]. 2023: Specialized hardware acceleration (TPUs for elliptic curve operations) explored by Fireblocks and others, achieving 30-50% throughput improvement but adding $50K-$200K hardware cost per deployment [implied from enterprise solutions]. 2024: Pre-computation and offline/online phase splitting tested, improving throughput 20-30% by front-loading cryptographic operations, but requiring accurate load prediction and increasing memory requirements 3-5x [Blog: Dynamic, 2024]. Key lesson: Fundamental trade-off between security (limiting parallelization) and throughput; no breakthrough eliminating coordination overhead without compromising MPC security model.
   
   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: Consumer MPC: 10-20 TPM, enterprise: 50-100 TPM, optimized: max 500 TPM [Guide: Stackup, 2024]; Hot wallets: 10,000+ TPS, hardware wallets: 100-200 TPS [Guide: Stackup, 2024]; HFT requires 1000-10,000 TPS, AMM needs 500-2000 TPS, mass payments need 1000+ TPS [industry standards]; Batching improves throughput 40-60% but increases latency 2-5x [Blog: Dynamic, 2024]; Offline/online splitting improves throughput 20-30% [Blog: Dynamic, 2024].
     - **Assumptions**: est. 200+ HFT firms blocked from MPC (sizing from major crypto HFT market: Jump, Jane Street, DRW Cumberland, etc.); est. 50+ major DeFi market makers (Uniswap, Curve, Aave liquidity providers); $50M-$200M annual revenue opportunity per HFT firm (typical HFT profit margins applied to crypto arbitrage); est. $500M-$2B total blocked revenue (200 firms × $2.5M-$10M average opportunity); $800K-$2M budget (2-3 researchers × 12 months × $200K + 4-5 engineers × $150K + $100K infrastructure + $200K specialized hardware testing); $0.02 per signature pricing (typical enterprise MPC wallet pricing from Fireblocks and similar providers).
     - **Uncertainties**: Theoretical maximum throughput for MPC protocols unknown (is 10,000 TPS achievable? or fundamental limit at 1000 TPS?); Hardware acceleration ROI unclear (does $50K-$200K investment justify 30-50% improvement?); Market demand uncertain (will HFT firms adopt MPC if throughput reaches 1000 TPS? or prefer hot wallets regardless?); Parallelization security trade-offs unexplored (can key share partitioning maintain security while enabling 10x throughput?); Network vs CPU bottleneck unclear (is optimization focus on bandwidth, coordination, or cryptographic operations?).

---

## Glossary

- **AMM (Automated Market Maker)**: DeFi protocol providing liquidity for token swaps; requires 500-2000 TPS for competitive market making across multiple pools.
- **Batching**: Combining multiple transactions into single MPC signing ceremony to amortize coordination overhead; improves throughput 40-60% but increases latency 2-5x.
- **EOA (Externally Owned Account)**: Single-key blockchain wallet capable of 10,000+ TPS, limited only by CPU; security risk due to single point of failure.
- **Hardware acceleration**: Using specialized processors (TPUs, FPGAs) for elliptic curve cryptography; improves throughput 30-50% but adds $50K-$200K per deployment.
- **HFT (High-Frequency Trading)**: Automated trading executing thousands of transactions per minute to exploit brief price discrepancies; requires 1000-10,000 TPS.
- **Hot wallet**: Online wallet with immediately accessible private key; capable of 10,000+ TPS but vulnerable to theft.
- **Mass payment**: Distributing cryptocurrency to thousands of recipients (payroll, airdrops); requires 1000+ TPS for completion within reasonable timeframe.
- **MEV (Maximal Extractable Value)**: Profit extracted by reordering, including, or excluding transactions in blockchain blocks; requires <100ms latency + 1000+ TPS.
- **Offline/online phase**: Protocol optimization pre-computing heavy cryptographic operations offline; improves throughput 20-30% but requires load prediction.
- **Parallelization**: Running multiple independent MPC signing sessions concurrently; improves throughput 2-5x but increases key management complexity and attack surface.
- **TPM (Transactions Per Minute)**: Throughput metric for signing infrastructure; consumer MPC: 10-20 TPM, enterprise: 50-100 TPM, specialized: max 500 TPM.
- **TPS (Transactions Per Second)**: Standard throughput metric (TPM / 60); MPC: 0.17-8.33 TPS, hot wallets: 10,000+ TPS.

---

## Reference

### Technical Guides & Analysis
- [Guide: Stackup, 2024] - "MPC Wallets: A Complete Technical Guide" section on performance benchmarks and throughput limitations (https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide)
- [Blog: Dynamic, 2024] - "The Evolution of MPC: From Secure but Slow to Fast and Scalable" discussing offline/online optimization (https://www.dynamic.xyz/blog/the-evolution-of-mpc)

### Industry Standards
- High-frequency trading throughput requirements: 1000-10,000 TPS (industry benchmark for competitive arbitrage)
- Automated market making: 500-2000 TPS (benchmark for multi-pool liquidity provision)
- Mass payment processing: 1000+ TPS (standard for enterprise payroll and airdrop services)

### Market Sizing
- Estimated 200+ institutional HFT firms in cryptocurrency markets
- Estimated 50+ major DeFi market makers providing liquidity across protocols
- Estimated $500M-$2B annual revenue opportunity blocked by throughput constraints
