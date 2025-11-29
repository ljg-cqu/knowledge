# RPC Node Infrastructure Centralization and Reliability Risks

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Documentation Team

## Problem Statement

**[CRITICAL]** Q: Self-custody wallet users face service disruptions and centralization risks due to dependence on centralized RPC node infrastructure, with 70% of Ethereum RPC traffic flowing through Infura and Alchemy hosted on AWS. Formulate a structured problem statement using the following [Input] fields.

A:
- **Brief description of the problem to be analyzed**: 
  Self-custody wallets rely heavily on centralized RPC providers (Infura, Alchemy) for blockchain access, creating single points of failure. The October 2025 AWS outage caused 32% request failure rate for Ethereum RPC endpoints and Infura uptime dropped to 61% [Web: Medium, 2025], affecting millions of wallet users globally and contradicting Web3's decentralization principles.

- **Background and current situation**: 
  RPC providers act as intermediaries between wallets and blockchain networks, handling transaction broadcasting and data queries [Web: Alchemy, 2025]. Approximately 70% of Ethereum RPC traffic flows through Infura and Alchemy [Web: Hackernoon, 2025], with 37% of Ethereum execution-layer nodes hosted on AWS and 42% of L1/L2 nodes in the same cloud environment [Web: Medium, 2025]. Most self-custody wallets (MetaMask, Trust Wallet, Coinbase Wallet) default to centralized RPC providers for convenience. During the October 2025 AWS outage, Ethereum RPC request timeouts exceeded 32%, Infura endpoint uptime fell to 61%, and MetaMask relay operations failed [Web: Medium, 2025]. Alternative solutions like running personal nodes require technical expertise and significant resources (storage, bandwidth, maintenance).

- **Goals and success criteria**: 
  RPC provider downtime: current 39% during AWS outages [Web: Medium, 2025] → <5% (target) / <1% (ideal) by Q4 2025; Wallet transaction success rate: current 68% during outages → >95% (min) / >99% (target) / >99.9% (ideal) by Q4 2025; Decentralized RPC adoption: current <10% [Assumption: based on provider market share] → >30% (min) / >50% (target) / >70% (ideal) by Q2 2026; Multi-RPC fallback implementation: current <20% wallet adoption [Assumption: estimated from wallet features] → >60% (min) / >80% (target) / >95% (ideal) by Q4 2025

- **Key constraints and resources**: 
  Timeline Q1 2025-Q2 2026 (18mo); Budget varies by approach: multi-RPC integration $50K-$150K per wallet, decentralized RPC node deployment $200K-$500K, user self-hosting education $100K-$300K; Technical constraints: latency requirements <500ms for RPC calls, bandwidth costs for decentralized nodes, backward compatibility with existing wallet integrations; Decentralization requirement: maintain trustless blockchain access without introducing new centralized dependencies; User experience: RPC fallback must be transparent with no manual intervention required

- **Stakeholders and roles**: 
  Wallet users (520M+ globally [Web: CoinLaw, 2025], need >99% transaction reliability, constraint: zero tolerance for fund access failures); Wallet developers (MetaMask, Trust Wallet, Coinbase Wallet, etc., need cost-effective infrastructure with <500ms latency, constraint: limited budget for multi-RPC integration); RPC providers (Infura, Alchemy, QuickNode, need revenue from API calls, constraint: AWS infrastructure lock-in); Decentralized RPC projects (Pocket Network, dRPC, need adoption and network effects, constraint: bootstrapping decentralized node network); DApp developers (need reliable wallet connectivity, constraint: cannot control user wallet RPC settings)

- **Time scale and impact scope**: 
  Timeline Q1 2025-Q2 2026 (18mo); Systems: RPC endpoint routing, multi-provider fallback, decentralized node networks, wallet provider integrations; Global scale: 520M+ wallet users [Web: CoinLaw, 2025], all major blockchain networks (Ethereum, Polygon, BSC, Avalanche, Arbitrum, Optimism); Financial impact: est. $50M-$200M in failed transactions during major outages [Assumption: based on transaction volume and average value], user trust and adoption risk

- **Historical attempts and existing solutions (if any)**: 
  Some advanced wallets (Rabby Wallet) implemented multi-RPC fallback mechanisms but adoption <5% [Assumption: estimated from wallet market share]. Pocket Network launched decentralized RPC in 2020 but faces network bootstrapping challenges and limited wallet integration. QuickNode and Alchemy offer 99.9% SLA guarantees but remain centralized on AWS/GCP infrastructure [Web: Chainstack, 2025]. The October 2025 AWS outage exposed infrastructure fragility despite provider redundancy claims. Key lesson: multi-region deployment within single cloud provider (AWS) insufficient for true resilience; need true decentralization or multi-cloud + decentralized hybrid approach.

- **Known facts, assumptions, and uncertainties**: 
  - **Facts**: 70% of Ethereum RPC traffic through Infura and Alchemy [Web: Hackernoon, 2025]; 37% of Ethereum nodes on AWS, 42% of L1/L2 nodes in same cloud environment [Web: Medium, 2025]; October 2025 AWS outage caused 32% request failure rate and 61% Infura uptime [Web: Medium, 2025]; 520M+ software wallet users globally [Web: CoinLaw, 2025]
  - **Assumptions**: Decentralized RPC adoption currently <10% (inferred from provider market dominance and wallet defaults); Multi-RPC fallback adoption <20% (estimated from wallet feature analysis); Failed transaction cost during outages est. $50M-$200M (calculated from transaction volume estimates); Latency requirement <500ms for acceptable UX (based on wallet performance standards)
  - **Uncertainties**: Exact market share distribution among RPC providers unknown; User willingness to pay premium for decentralized RPC TBD; Optimal RPC fallback strategy (round-robin vs latency-based vs reputation-based) not determined; Regulatory treatment of RPC providers as infrastructure vs service providers unclear; Cost-benefit tradeoff for wallet providers to integrate multi-RPC vs single provider contracts unknown

---

## Glossary

- **AWS (Amazon Web Services)**: Cloud computing platform hosting significant portion of blockchain infrastructure, creating centralization risks when outages occur.
- **Decentralized RPC**: Remote Procedure Call infrastructure distributed across independent node operators, reducing single points of failure compared to centralized providers.
- **Infura**: Major centralized RPC provider owned by Consensys, handling significant Ethereum network traffic for wallets and dApps.
- **Multi-RPC fallback**: Wallet architecture that automatically switches between multiple RPC providers when primary provider fails, improving reliability.
- **RPC (Remote Procedure Call)**: Protocol enabling wallets to communicate with blockchain networks for reading data and broadcasting transactions without running full nodes.
- **RPC endpoint**: Server URL that wallets connect to for blockchain access; centralized endpoints create dependency on specific infrastructure providers.
- **RPC provider**: Service offering blockchain node access via APIs, eliminating need for users to run personal nodes but introducing centralization risk.
- **Self-custody wallet**: Cryptocurrency wallet where users control private keys, but typically depends on RPC providers for blockchain connectivity.
- **SLA (Service Level Agreement)**: Contract guaranteeing specific uptime percentage (e.g., 99.9%), though enforcement during major outages often limited.

---

## Reference

### Web Sources & Research
- [Web: Medium, 2025] - Infrastructure Stress Test; AWS outage impacts: 32% Ethereum RPC request failure rate, 61% Infura uptime, MetaMask relay failures; 37% Ethereum nodes on AWS, 42% L1/L2 nodes same cloud environment (https://medium.com/@Grace_Nelo/infrastructure-stress-test-5329d45c131f)
- [Web: Hackernoon, 2025] - When Amazon Crashed Decentralized Blockchain Went Down With It; 70% of Ethereum RPC traffic through Infura and Alchemy on AWS (https://hackernoon.com/when-amazon-crashed-decentralized-blockchain-went-down-with-it)
- [Web: CoinLaw, 2025] - Cryptocurrency Wallet Adoption Statistics 2025; 520M+ software wallet downloads globally (https://coinlaw.io/cryptocurrency-wallet-adoption-statistics)
- [Web: Alchemy, 2025] - The 12 Best Blockchain Node Providers 2025; RPC provider overview and functionality (https://www.alchemy.com/overviews/blockchain-node-providers)
- [Web: Chainstack, 2025] - Top Ethereum RPC Providers for 2025; RPC provider comparison including SLA guarantees (https://chainstack.com/top-ethereum-rpc-providers-for-2025)
- [Web: CoinDesk, 2025] - Crypto's Decentralized Illusion Shattered Again by Another AWS Meltdown; AWS outage impact on crypto ecosystem decentralization claims (https://www.coindesk.com/news-analysis/2025/10/21/crypto-s-decentralized-illusion-shattered-again-by-another-aws-meltdown)
