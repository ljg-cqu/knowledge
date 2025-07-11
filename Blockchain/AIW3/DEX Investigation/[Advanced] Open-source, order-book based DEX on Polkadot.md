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

- **TPS**: SPEEDEX achieves over 200,000 transactions per second (TPS) on 48-core servers, even with tens of millions of open offers, exceeding the 100,000 TPS requirement for order-book-based DEX infrastructure. This performance is achieved while running entirely within a Layer-1 blockchain.
- **Architecture**: It operates as a Layer-1 blockchain, ensuring high scalability within a single blockchain and preventing market liquidity fragmentation across multiple blockchains or rollups. SPEEDEX's key design insight is its use of an Arrow-Debreu exchange market structure.
- **Key Features**:
  - SPEEDEX uses an Arrow-Debreu exchange market structure to ensure fairness, eliminate internal arbitrage, and make trade operations commutative and efficiently parallelizable.
  - This market structure fixes the valuation of assets for all trades in a given block of transactions.
  - It addresses certain traditional DEX vulnerabilities, such as price slippage from front-running attacks, and maintains consistent pricing within each transaction block.
  - The platform is designed as an infrastructural blockchain for large-scale, order-book-based exchanges.
- **Reliable Links**:
  - **GitHub**:
    - Standalone implementation of SPEEDEX: The provided documents show GitHub repositories related to "speedex" but these appear to be for courier tracking and WooCommerce integration rather than the DEX blockchain. The specific standalone implementation of SPEEDEX mentioned in the previous conversation (https://github.com/scslab/speedex) is not directly present in the current documents as a functional link, though there are mentions of "scslab/speedex" development.
    - SPEEDEX backend development: The provided documents do not explicitly list a direct link for "speedex-backend" development on GitHub.
  - **Official Website**: The provided documents do not explicitly include an official website for the SPEEDEX decentralized exchange; the "speedexlogistics.net" domain appears to be for a logistics company.
  - **Documentation**: The provided documents do not explicitly list dedicated documentation for the SPEEDEX decentralized exchange beyond general mentions of documentation within GitHub repository contexts.

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
Akhila Sri Manasa Venigalla & S. Chimalakonda. (2021). What’s in a GitHub Repository? - A Software Documentation Perspective. In ArXiv. https://www.semanticscholar.org/paper/c23c5014583b7fcb96db7abd17e3ab0b39f55b58

Bernadette Royal. (2014). Subject guides: Resources for Academics Guide: Use reliable resource links. https://www.semanticscholar.org/paper/be363af2e3ba31a82b7b058774fbf4a9f5adc534

G Ramseyer, A Goel, & D Mazières. (2023). {SPEEDEX}: A Scalable, Parallelizable, and Economically Efficient Decentralized {EXchange}. https://www.usenix.org/conference/nsdi23/presentation/ramseyer

Geoffrey Ramseyer, Ashish Goel, & David Mazières. (2021a). SPEEDEX: A Scalable, Parallelizable, and Economically Efﬁcient Distributed EXchange. https://www.semanticscholar.org/paper/1d112fe9a859a3d71b9bf06b239404beef9fb957

Geoffrey Ramseyer, Ashish Goel, & David Mazières. (2021b). SPEEDEX: A Scalable, Parallelizable, and Economically Efficient Decentralized EXchange. In Symposium on Networked Systems Design and Implementation. https://www.semanticscholar.org/paper/7973956c43dcd7feb6a8d55f4c68cf04f9dcf6db

J. Schrape. (2018). Open-Source-Projekte zwischen Passion und Kalkül. https://www.semanticscholar.org/paper/fb4dc5b4cc59832094c662eaa1791301b261fdf8

Jailton Coelho, M. T. Valente, Luciano O. Milen, & L. L. Silva. (2020). Is this GitHub Project Maintained? Measuring the Level of Maintenance Activity of Open-Source Projects. In Inf. Softw. Technol. https://arxiv.org/abs/2003.04755

speedex · GitHub Topics · GitHub. (2024). https://github.com/topics/speedex

Speedex Logistics - Safe Fast Reliable. (n.d.). https://www.speedexlogistics.net/

speedex/.gitmodules at master - GitHub. (2021). https://github.com/scslab/speedex/blob/master/.gitmodules

vpant/woocommerce-speedex-integration - GitHub. (2019). https://github.com/vpant/woocommerce-speedex-integration



Generated by Liner
https://getliner.com/search/s/5926611/t/86444297