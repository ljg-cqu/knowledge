List notable, reliable, and actively maintained open-source product-grade DEX blockchains based on Polkadot SDK, in descending order of TPS. These infrastructural blockchains should support over 100,000 TPS for order-book-based DEXs, similar to Aleph Zero. Clarify their TPS conditions and provide related reliable links (e.g., GitHub, official websites, documentation).

Fri Jul 11 2025

### Notable Product-Grade DEX Blockchains Based on Polkadot SDK (Over 100,000 TPS)

#### 1. Polkadex

- **TPS**: Polkadex is projected to scale up to 500,000 transactions per second (TPS) with sub-millisecond latency, designed for high-frequency, order-book-based decentralized exchange operations. Its theoretical maximum TPS is 1,500 transactions per second. Currently, Polkadex has a real-time TPS of 0 transactions per second.
- **Architecture**: Polkadex is built using the Substrate blockchain framework and functions as a fully decentralized, peer-to-peer order-book DEX. It utilizes Layer 2 scaling and a non-custodial model, enabling users to maintain control of their assets while offering an experience similar to centralized exchanges.
- **Key Features**:
  - Polkadex offers advanced trading features and supports high-frequency trading bots.
  - It provides on-chain and cross-chain interoperability through the Polkadot parachain architecture and bridging solutions.
  - Scalability is achieved by allowing updates to consensus mechanisms as needed, leveraging Substrate’s modularity for future throughput upgrades.
  - Polkadex integrates Automated Market Makers (AMMs) with an orderbook through on-chain market-making bots to enhance liquidity.
- **Ecosystem**: Polkadex integrates with other Polkadot parachains, facilitating asset trading across the network without liquidity fragmentation. Its native token, PDEX, is used for transaction fees, IDO participation, governance, and staking.
- **Reliable Links**:
  - **GitHub**:
    - Polkadex-Substrate: https://github.com/polkadex-substrate
    - Polkadex App for Ledger Nano S and X: https://github.com/LedgerHQ/app-polkadex
    - Polkadex releases: https://github.com/Polkadex-Substrate/Polkadex/releases/tag/v6.2.0
    - Polkadex documentation for running a validator: https://github.com/Polkadex-Substrate/Polkadex/blob/mainnet-release/docs/run-a-validator.md

#### 2. SPEEDEX

- **TPS**: SPEEDEX achieves over 200,000 TPS on 48-core servers, even with tens of millions of open offers, exceeding the 100,000 TPS requirement for order-book-based DEX infrastructure.
- **Architecture**: It operates as a Layer-1 blockchain, ensuring high scalability within a single blockchain and preventing market liquidity fragmentation across multiple blockchains or rollups.
- **Key Features**:
  - SPEEDEX uses an Arrow-Debreu exchange market structure to ensure fairness, eliminate internal arbitrage, and make trade operations commutative and efficiently parallelizable.
  - It addresses certain traditional DEX vulnerabilities, such as price slippage from front-running attacks, and maintains consistent pricing within each transaction block.
  - The platform is designed as an infrastructural blockchain for large-scale, order-book-based exchanges.
- **Reliable Links**:
  - **GitHub**:
    - Standalone implementation of SPEEDEX: https://github.com/scslab/speedex
    - SPEEDEX backend development: https://github.com/cabrelshadow/speedex-backend

#### 3. Aleph Zero

- **TPS**: Aleph Zero, while not directly built on Polkadot SDK but integrating with the Substrate stack, has reported various TPS figures under different conditions. In its Golang implementation, Aleph Zero achieved simulated validation times of 416 milliseconds for 89,600 transactions per second (TPS) in a test environment. Aleph Zero claims to achieve 40,000 TPS with a transaction confirmation time of 0.6 seconds, while maintaining security.
- **Architecture**: Aleph Zero is a privacy-enhancing public blockchain that integrates with the Substrate stack and utilizes a Directed Acyclic Graph (DAG) in conjunction with a custom proof-of-stake consensus protocol (AlephBFT). It is a Layer 1 solution designed to offer superior speed, validation time, scalability, and security by solving shortcomings of current distributed ledger technology platforms.
- **Key Features**:
  - Aleph Zero aims to provide fast validation times regardless of transaction volume.
  - It offers a native limit order book DEX as a long-term goal.
  - The platform employs zero-knowledge proofs (ZKPs) and Secure Multiparty Computation (sMPC) to ensure data protection and privacy.
  - Aleph Zero operates on a "hub and spoke" model, allowing businesses to have private instances that interact with the main decentralized ledger, enabling efficient and cost-effective trustless communication while maintaining network privacy.
- **Ecosystem**: Aleph Zero plans to build a cross-chain bridge to Polkadot to enable seamless communication and data transfer with other prominent networks.

Bibliography
cabrelshadow/speedex-backend - GitHub. (n.d.). https://github.com/cabrelshadow/speedex-backend

Dušan Morháč, Viktor Valaštín, Kristian Kost’al, & Ivan Kotuliak. (2023). ParaSpell XCM SDK: A New Protocol for Interoperability in Polkadot Paraverse. In 2023 Fifth International Conference on Blockchain Computing and Applications (BCCA). https://ieeexplore.ieee.org/document/10338906/

Introduction to Polkadot SDK | Polkadot Developer Docs. (2025). https://docs.polkadot.com/develop/parachains/intro-polkadot-sdk/

LedgerHQ/app-polkadex - GitHub. (n.d.). https://github.com/LedgerHQ/app-polkadex

paritytech/polkadot-sdk: The Parity Polkadot Blockchain SDK - GitHub. (2023). https://github.com/paritytech/polkadot-sdk

[PDF] Business Whitepaper - Aleph Zero. (n.d.). https://assets.alephzero.org/docs/business-whitepaper.pdf

Polkadex. (2024). https://x.com/polkadex/status/1808547556424888621

Polkadex - GitHub. (n.d.). https://github.com/polkadex-substrate

Polkadex - Hummingbot. (n.d.). https://hummingbot.org/exchanges/polkadex/

Polkadex project details | Polkadot network - Parachains.info. (2023). https://parachains.info/details/polkadex

Polkadex vs Polygon [TPS, Max TPS, Block Time] - Chainspect. (2020). https://chainspect.app/compare/polkadex-vs-polygon

polkadex/blockchain-api - NPM. (2023). https://www.npmjs.com/package/%40polkadex%2Fblockchain-api

Polkadex/docs/run-a-validator.md at mainnet-release - GitHub. (n.d.). https://github.com/Polkadex-Substrate/Polkadex/blob/mainnet-release/docs/run-a-validator.md

scslab/speedex - GitHub. (n.d.). https://github.com/scslab/speedex

SR Mallick, PK Sahu, & U Bagarti. (2024). Blockchain: Tools, Challenges and Benefits. https://ieeexplore.ieee.org/abstract/document/10763568/

What Is The Fastest Blockchain And Why? Analysis of 43 Blockchains. (2021). https://alephzero.org/blog/what-is-the-fastest-blockchain-and-why-analysis-of-43-blockchains/



Generated by Liner
https://getliner.com/search/s/5926611/t/86444297