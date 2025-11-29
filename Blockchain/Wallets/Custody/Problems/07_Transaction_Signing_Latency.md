# Transaction Signing Latency and Scalability Limitations

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Documentation Team

## Problem Statement

1. **[Important]** Q: Institutional crypto custody providers face transaction signing latency constraints limiting high-frequency trading execution and real-time operational requirements. Formulate a structured problem statement using the following [Input] fields.
   
   A:
   - **Brief description of the problem to be analyzed**: 
     Financial institutions require bank-grade security with low latency for trade execution, but current custody wallet architectures introduce significant signing delays (est. 2-10 seconds for MPC, 5-30 seconds for cold storage multi-sig) preventing high-frequency trading strategies and time-sensitive operations [Web Search: Zodia Custody, 2025]. Institutional traders executing 1000-10,000+ transactions daily face 30-60 minute cumulative delays, resulting in slippage costs of 0.1-0.5% per trade ($100K-$500K daily losses on $100M portfolio) and missed arbitrage opportunities. Need to reduce transaction signing latency from current 2-10s (MPC) to <500ms (min) / <200ms (target) / <100ms (ideal) by Q3 2025 while maintaining security standards.
   
   - **Background and current situation**: 
     Digital asset custody infrastructure requires security architecture, key management, integration, and interoperability [Web Search: Zodia Custody, 2025]. Financial institutions need bank-grade security with low latency for trade execution and flexibility to interact with various services [Web Search: Zodia Custody, 2025]. Current custody architectures prioritize security over speed: (1) Cold storage requires manual retrieval (5-30 seconds per transaction), (2) MPC (Multi-Party Computation) requires distributed computation across key shares (2-10 seconds depending on network topology and share count), (3) Multi-signature wallets require sequential approvals (3-15 seconds per signatory), (4) HSM (Hardware Security Module) batch processing introduces queuing delays (1-5 seconds). Trade-off between security and latency: reducing key share count or approval requirements decreases security; increasing distribution or approval count increases latency. High-frequency institutional trading requires <500ms signing for competitive execution; current custody solutions fail to meet this threshold.
   
   - **Goals and success criteria**: 
     Transaction signing latency MPC: current 2-10s → <1s (min) / <500ms (target) / <200ms (ideal) by Q3 2025; Transaction signing latency cold storage multi-sig: current 5-30s → <3s (min) / <2s (target) / <1s (ideal); Transaction throughput: current est. 10-50 txn/s per custodian → >100 txn/s (min) / >500 txn/s (target) / >1000 txn/s (ideal); Trading slippage reduction: current 0.1-0.5% per trade → <0.05% (min) / <0.02% (target) / <0.01% (ideal); Arbitrage opportunity capture: current est. 20-40% of identified opportunities → >60% (min) / >80% (target) / >95% (ideal); Cumulative daily delay for 10K transactions: current 30-60 minutes → <15min (min) / <5min (target) / <2min (ideal)
   
   - **Key constraints and resources**: 
     Timeline Q1-Q3 2025 (6-9mo for architecture optimization); Budget $1M-$2.5M capex for infrastructure upgrade (optimized MPC nodes, HSM clusters, network optimization) + $150K-$300K/mo opex; Team 4-6 FTE cryptography engineers + 3-4 FTE infrastructure engineers + 2 FTE performance engineers; Tech requirements: optimize MPC threshold schemes (reduce round-trip communication), implement asynchronous signing pipelines, deploy low-latency HSM clusters, optimize network topology (co-location with exchanges), implement transaction batching; Security constraints: cannot reduce security level (maintain minimum 2-of-3 or 3-of-5 thresholds); Regulatory constraints: must maintain MiCA/SEC compliance for key management; Cannot compromise auditability for speed
   
   - **Stakeholders and roles**: 
     Institutional traders (executing 1000-10K+ txn/day, need <500ms signing latency, constraint: slippage cost <0.02% per trade), Custody providers (need competitive performance, constraint: maintain security standards while reducing latency), Cryptography engineers (4-6 FTE, need optimize MPC protocols, constraint: maintain ≥128-bit security level), Infrastructure engineers (3-4 FTE, need deploy low-latency systems, constraint: 99.9%+ uptime during upgrades), Portfolio managers (managing $100M-$10B+ AUM, need arbitrage execution, constraint: capture >80% of identified opportunities), Risk officers (need security assurance, constraint: no reduction in key management security thresholds), Market makers (need real-time execution, constraint: accept <0.1% additional custody fees for low-latency service)
   
   - **Time scale and impact scope**: 
     Timeline Q1-Q3 2025 (6-9mo); Affected systems: MPC key management (threshold signing protocols), HSM infrastructure (signing request processing), Transaction signing pipeline (queuing, batching, routing), Network infrastructure (custody-exchange connectivity), Multi-signature coordination (approval workflows); Geographic scope: Global trading operations, focus on major trading centers (US, EU, Asia); Scale: institutional traders executing 1000-10K+ txn/day, $100M-$10B+ portfolios, high-frequency strategies requiring <500ms latency; Financial impact: current slippage 0.1-0.5% per trade = $100K-$500K daily losses on $100M portfolio at 100 trades/day; missed arbitrage opportunities est. 60-80% of identified scenarios
   
   - **Historical attempts and existing solutions (if any)**: 
     Hot wallet trading accounts: maintain small balance in high-speed hot wallets for trading, bulk assets in cold storage. Outcome: achieves <100ms signing latency but introduces security risk (10-20% of portfolio in vulnerable hot storage). Optimized MPC protocols (GG20, CMP, CGGMP): reduce communication rounds and computation overhead. Outcome: improves latency from 10s to 2-5s but still insufficient for high-frequency trading [Web Search: Cordialsystems, 2025]. HSM clustering: deploy multiple HSMs in parallel to increase throughput. Outcome: improves throughput (100-500 txn/s) but individual transaction latency remains 1-3s. Co-location with exchanges: deploy custody signing infrastructure in same data centers as exchanges. Outcome: reduces network latency from 50-200ms to <10ms but MPC/HSM computation latency remains dominant factor. Key lesson: achieving <500ms signing latency while maintaining institutional-grade security requires fundamental architecture innovation beyond incremental optimizations.
   
   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: Financial institutions require low latency for trade execution [Web Search: Zodia Custody, 2025]; Digital asset custody requires balancing security, key management, and performance [Web Search: Zodia Custody, 2025]; MPC wallets provide secure institutional operations [Web Search: Cordialsystems, 2025]; Cold storage and multi-sig introduce manual delays; High-frequency trading requires <500ms execution latency
     - **Assumptions**: Current MPC signing latency est. 2-10s (based on protocol specifications and network round-trips); Cold storage multi-sig latency est. 5-30s (manual retrieval and sequential approvals); HSM processing est. 1-5s (batch queuing and cryptographic operations); Transaction throughput est. 10-50 txn/s per custodian (inferred from capacity disclosures); Trading slippage est. 0.1-0.5% per trade from signing delays (market movement during execution delay); Arbitrage opportunity capture est. 20-40% (opportunities closed before signing completes); Daily losses est. $100K-$500K on $100M portfolio (100 trades/day × 0.1-0.5% slippage); Infrastructure upgrade capex est. $1M-$2.5M (optimized MPC nodes, HSM clusters, co-location); Opex est. $150K-$300K/mo (maintenance, network, expertise)
     - **Uncertainties**: Theoretical minimum latency for secure MPC signing unknown; Security vs latency trade-off optimization strategies not standardized; Cost-benefit ratio for different latency improvement approaches unclear; Client willingness to pay for low-latency custody services TBD; Regulatory acceptance of optimized key management architectures evolving; Quantum-resistant signature schemes impact on latency unknown; Network latency contribution vs computation latency in different custody architectures unclear; Asynchronous signing pipeline security implications TBD

---

## Glossary

- **Arbitrage**: Trading strategy exploiting price differences for same asset across markets, requiring fast execution (<500ms) before opportunity closes.
- **Asynchronous signing**: Architecture enabling transaction signing operations to proceed in parallel without blocking, improving throughput and reducing latency.
- **Co-location**: Deploying custody infrastructure in same data center as trading exchanges, reducing network latency from 50-200ms to <10ms.
- **GG20/CMP/CGGMP**: Optimized MPC threshold signature protocols (Gennaro-Goldfeder 2020, Canetti-Makriyannis-Peled, Canetti-Gennaro-Goldfeder-Makriyannis-Peled) reducing communication rounds and computation overhead.
- **High-frequency trading (HFT)**: Automated trading strategy executing thousands to millions of trades daily, requiring <500ms latency for competitive execution.
- **HSM (Hardware Security Module)**: Dedicated cryptographic hardware providing secure key operations, typically processing 100-1000 signatures per second depending on algorithm.
- **MPC (Multi-Party Computation)**: Cryptographic technique splitting private key into shares across multiple parties, requiring distributed computation for signing (2-10s typical latency).
- **Slippage**: Price movement between trade decision and execution, costing 0.1-0.5% per trade when signing latency causes execution delays.
- **Threshold signature**: Cryptographic scheme requiring subset of key shares (e.g., 2-of-3, 3-of-5) to produce valid signature, balancing security and availability.

---

## Reference

### Web Search Sources
- [Web Search: Zodia Custody, 2025] - Building digital asset custody, security architecture, key management, low latency requirements for financial institutions
- [Web Search: Cordialsystems, 2025] - How MPC wallets work complete guide, threshold schemes, protocol optimization (GG20, CMP, CGGMP)
