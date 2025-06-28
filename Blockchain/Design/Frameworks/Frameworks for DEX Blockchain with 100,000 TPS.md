To build or customize a blockchain for a DEX supporting up to 100,000 TPS, which frameworks should be used: Substrate, Cosmos SDK, or other alternatives?

Sat Jun 28 2025

### Substrate Framework
Substrate is an open-source blockchain framework that offers a modular and extensible foundation for developers to build their own blockchains. It functions similarly to a Software Development Kit (SDK), providing essential tools and fundamental functionalities such as consensus mechanisms, token standards, and governance models as building blocks that developers can customize for their specific project needs. Substrate aims to simplify the blockchain development process, making it safer, cheaper, easier, and faster to create custom, interoperable blockchains. Its key features include a modular architecture for easy component integration, inherent security features to safeguard against vulnerabilities, and strong community support.

Substrate is well-suited for building custom blockchains that require high levels of customization, allowing developers to define token standards, consensus mechanisms, and governance models. It is particularly effective for developing parachains, which operate parallel to a relay chain, leveraging benefits like shared security and payment settlement, and enabling faster transactions at a low cost. The framework uses a WASM runtime engine, ensuring high performance, and its design allows for on-chain upgrades to smart contracts, which is a key advantage over platforms like Ethereum where smart contracts cannot be changed once deployed. Polkaswap, a decentralized exchange, is built using Substrate as Rust pallets on the SORA L1 blockchain network. Polkadex is another open-source decentralized exchange platform developed with the Substrate Blockchain Framework, aiming to provide a centralized user experience. Additionally, Substrate can be used to build various Decentralized Finance (DeFi) applications, including decentralized exchanges and lending platforms.

### Cosmos SDK
The Cosmos SDK is an open-source framework designed to help developers create custom blockchains from scratch that can natively interoperate with other blockchains. It is envisioned as an "npm-like" framework for building secure blockchain applications on top of Tendermint. This SDK streamlines the development process by abstracting complex blockchain functionalities, enabling developers to focus on application logic. Key components include its modular architecture, allowing developers to plug and play various modules for functionalities like governance and staking, and the Tendermint Core, a Byzantine Fault Tolerant (BFT) consensus engine that ensures secure and consistent transaction finality.

Cosmos SDK-based blockchains are designed for enhanced scalability, lower transaction costs, and built-in interoperability through the Inter-Blockchain Communication (IBC) protocol. This modularity means that each chain can operate independently, reducing the impact of congestion on other chains and ensuring high throughput. The SDK provides a comprehensive toolkit for building scalable and interoperable applications, offering flexibility in decentralization and supporting cross-chain interactions. It aims to address the scalability challenges faced by traditional platforms like Ethereum, which often suffer from slow transaction speeds and high gas fees due to network congestion. The Cosmos Hub, built with Cosmos SDK, aims to function as a decentralized exchange for tokens within its ecosystem, emphasizing its suitability for DEXs. While the documents do not provide a specific TPS number for Cosmos SDK, they consistently highlight its focus on achieving high-speed processing and scalability for decentralized applications.

### Other Alternatives for High TPS DEXs
Several alternative blockchain frameworks and technologies exist that aim to support high TPS requirements for Decentralized Exchanges (DEXs). These alternatives often focus on optimizing various aspects of blockchain operation, such as transaction management, consensus mechanisms, and off-chain scaling solutions.

The **Smart Red Belly Blockchain (SRBB)**, for instance, focuses on enhanced transaction management to improve performance. It achieves a peak throughput of 4,000 TPS and an average of 2,000 TPS on a network of 200 nodes distributed across five continents. SRBB also outperformed six other blockchains when running an exchange DApp with a real workload trace from Nasdaq. Its approach includes novel transaction validation reduction and per-sub-block processing to optimize block storage.

**SPEEDEX** is a decentralized exchange that emphasizes scalability and parallelization, achieving a high throughput of over 200,000 transactions per second (TPS) on 48-core servers, even with millions of open offers. It runs entirely within a Layer-1 blockchain, aiming to achieve scalability without fragmenting market liquidity across multiple blockchains or rollups. SPEEDEX also eliminates internal arbitrage opportunities and prevents front-running attacks, making it highly suitable for DEX operations.

**TEX** (Trustless Exchange) proposes a securely scalable, front-running resilient, non-custodial centralized exchange that can operate with a blockchain-based settlement layer. While it centralizes order matching, it enforces the trade order sequence provided by traders, making it resilient against trade sequence alteration by the exchange operator. TEX aims to reach similar scales as traditional exchanges in terms of trading volume and trades per second, despite relying on a potentially slow underlying ledger.

**Plasma** is a Layer 2 scaling solution designed to increase scalability by moving transactions onto faster, less crowded sidechains. It aims to reach thousands of transactions per second by providing off-chain scalability while maintaining the security level of the main chain. Plasma relies on cryptography and game theory to enable reliable transactions on its blockchain, with users able to exit the sidechain and recover funds on the mainnet if malicious validator behavior is detected. Although current Plasma designs often have a single validator, the design incentivizes against censorship, allowing it to scale.

Another proposed method is **Bodyless Block Propagation (BBP)**, which aims to increase TPS without sacrificing decentralization and security. BBP can reduce block propagation time by four times compared to the Ethereum blockchain, showing potential for full TPS scalability where performance is limited by node hardware rather than block propagation. This scheme involves nodes anticipating and pre-validating transactions for upcoming blocks, meaning only the block header needs to be broadcast when a block is mined.

**Coreum** is a blockchain framework designed for institutional use, which supports 7,000 TPS. While specific details about its suitability for DEXs are not provided, its high TPS and design for regulated finance suggest potential for high-performance trading platforms.

Bibliography
Analyzing Cosmos TPS: Performance, Comparisons, and Alternatives. (2025). https://webisoft.com/articles/cosmos-tps/

Blockchain Scaling Solutions: Cosmos and Plasma - Medium. (2018). https://medium.com/tendermint/blockchain-scaling-solutions-cosmos-and-plasma-b5ee09456f80

Building Scalable Applications with the Cosmos SDK - Medium. (2024). https://medium.com/@jefferyokesamuel1/building-scalable-applications-with-the-cosmos-sdk-6dc56ae28643

Chonghe Zhao, Shengli Zhang, Taotao Wang, & S. Liew. (2022). Bodyless Block Propagation: TPS Fully Scalable Blockchain with Pre-Validation. In ArXiv. https://www.semanticscholar.org/paper/4d3a63b60dbdf45f6169086d64c6f85f0e1f931b

Coreum: How a 7,000 TPS blockchain is shaping the future of ... (2025). https://cointelegraph.com/news/coreum-how-a-7-000-tps-blockchain-is-shaping-the-future-of-regulated-finance

Cosmos SDK: Build Scalable Blockchain Apps Easily - Webisoft. (2025). https://webisoft.com/articles/cosmos-sdk/

cosmos/awesome-cosmos: Collection of Cosmos related resources. (2019). https://github.com/cosmos/awesome-cosmos

Deepal Tennakoon & Vincent Gramoli. (2022). Smart Red Belly Blockchain: Enhanced Transaction Management for Decentralized Applications. In ArXiv. https://arxiv.org/abs/2207.05971

DeX on the Hub discussion - Hub Relations - Cosmos Hub Forum. (2020). https://forum.cosmos.network/t/dex-on-the-hub-discussion/3731

Geoffrey Ramseyer, Ashish Goel, & David Mazières. (2021a). SPEEDEX: A Scalable, Parallelizable, and Economically Efﬁcient Distributed EXchange. https://www.semanticscholar.org/paper/1d112fe9a859a3d71b9bf06b239404beef9fb957

Geoffrey Ramseyer, Ashish Goel, & David Mazières. (2021b). SPEEDEX: A Scalable, Parallelizable, and Economically Efficient Decentralized EXchange. In Symposium on Networked Systems Design and Implementation. https://www.semanticscholar.org/paper/7973956c43dcd7feb6a8d55f4c68cf04f9dcf6db

High-level Overview - Cosmos SDK. (n.d.). https://docs.cosmos.network/v0.46/intro/overview.html

Hyug-Jun Ko & Seong-Soo Han. (2024). TPS Analysis, Performance Indicator of Public Blockchain Scalability. In J. Inf. Process. Syst. https://jips-k.org/digital-library/2024/20/1/85

Interoperable, customizable and scalable: Get To Know The ... (2023). https://blog.cosmos.network/interoperable-customizable-and-scalable-get-to-know-the-cosmos-network-8309063007ff

M Takemiya. (2023). ALT: Aggregate Liquidity Technology. https://ieeexplore.ieee.org/abstract/document/10174911/

philoniare/polkadot-sdk-tutorial-dex - GitHub. (n.d.). https://github.com/philoniare/polkadot-sdk-tutorial-dex

Polkadex-Substrate/Polkadex: An Orderbook-based Decentralized ... (n.d.). https://github.com/Polkadex-Substrate/Polkadex

Rami A. Khalil, Arthur Gervais, & Guillaume Felley. (2019). TEX - A Securely Scalable Trustless Exchange. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/08261626547624d6efbf559d103193d02627e9e8

Scaling Cosmos Blockchains: Putting the Legos together. (2023). https://sgerogia.github.io/Scaling-Chains/

Substrate: a generic Rust-based blockchain framework | Medium. (2024). https://medium.com/@brunopgalvao/substrate-cfeb13333f2c

The Future of Blockchain Development: Why Cosmos SDK Offers a ... (2024). https://dev.to/jonasand/the-future-of-blockchain-development-why-cosmos-sdk-offers-a-superior-alternative-to-evm-chains-17a0

Top Blockchain Development Frameworks to Watch in 2025. (2025). https://www.codezeros.com/top-blockchain-development-frameworks-to-watch-in-2025

Top Use Cases of Substrate Blockchain Framework in 2024. (2023). https://www.antiersolutions.com/blogs/a-deep-dive-into-substrate-blockchain-use-cases/

Use Cases of Substrate Framework- A Complete Guide - SoluLab. (n.d.). https://www.solulab.com/use-cases-of-substrate-framework/

What is transactions per second (TPS)? - CoinTracker. (n.d.). https://www.cointracker.io/learn/transactions-per-second

X Wang, A Shankar, & K Li. (2024). Blockchain-enabled decentralized edge intelligence for trustworthy 6G consumer electronics. https://ieeexplore.ieee.org/abstract/document/10454589/



Generated by Liner
https://getliner.com/search/s/5926611/t/86064745