Substrate Blockchain

Wed Jun 25 2025

### Introduction to Substrate Blockchain

Substrate is an open-source, Rust-based framework for building custom blockchain networks, developed by Parity Technologies. It functions as a comprehensive Software Development Kit (SDK) that provides developers with the foundational elements necessary to create specialized blockchains without starting from scratch. Substrate is not a blockchain itself, but rather a robust set of tools that enables the creation of unique and powerful blockchain solutions tailored to specific needs and desires. This framework aims to simplify the development and administration of decentralized digital ledgers, making it a game-changing innovation in the blockchain space.

### Origin and Evolution

Substrate was created by Parity Technologies, a blockchain technology company founded by Gavin Wood, who is also a co-founder of Ethereum and the founder of Polkadot. The team at Parity Technologies designed Substrate to overcome the limitations and challenges encountered during the development of Polkadot, a multi-chain blockchain platform. Historically, building a blockchain typically involved either forking an existing chain like Ethereum or writing one entirely from scratch, both of which are resource-intensive, costly, time-consuming, and require specialized knowledge. Recognizing that many core blockchain components such as networking, storage, transaction queues, and consensus mechanisms are common across most blockchains, Parity Technologies developed Substrate to allow these components to be reused. This foresight led to Substrate becoming a stack of tooling that distills lessons learned from building Ethereum and Polkadot, offering developers significant benefits without the need to rebuild fundamentals. Substrate was initially unveiled in 2018 as a more extensible framework to address issues like scalability and governance limitations in earlier blockchains such as Ethereum.

### Core Concepts and Architecture

Substrate's architecture is designed for innovation and flexibility, streamlining the blockchain creation process. Its design is notable for its modularity, which enables developers to select, customize, and upgrade various blockchain network components as needed.

#### Modular Architecture and FRAME
Substrate is characterized by its **modular architecture**, resembling building blocks that developers can easily put together and customize. This design allows developers to customize or swap out almost any part of the blockchain, including consensus algorithms, networking layers, runtime environments, and storage modules. This modularity significantly reduces the complexities associated with traditional blockchain development, enabling developers to focus on unique business logic rather than foundational infrastructure. The **FRAME (Framework for Runtime Aggregation of Modularized Entities)** is Substrate’s modular architecture for building blockchain runtimes. FRAME consists of modules with business logic, known as pallets, and support libraries that facilitate development.

#### Runtime and WebAssembly (Wasm)
At the core of any Substrate-based blockchain is its **runtime**, which defines the blockchain's logic and rules. The runtime is responsible for establishing state transition functions, dictating how the blockchain's state changes with each new block. A key distinction of Substrate's runtime is its compilation to **WebAssembly (Wasm)** bytecode. This allows the blockchain logic to run efficiently across different platforms and hardware, ensuring multi-platform compatibility and future-proofing. The runtime ensures that data integrity and consistency are maintained as transactions are processed, and it manages the blockchain's on-chain storage via defined storage items within pallets.

#### Pallets
**Pallets** are modular and composable runtime modules that form the building blocks of a Substrate blockchain’s runtime. Developers use pallets to incorporate specific features and capabilities into their chains, such as governance for stakeholder voting, token transfers, smart contracts, identity management, oracles, and more. Pallets are composable, meaning they can be "stacked" to create more complex blockchain logic, simplifying the building process without sacrificing innovation. Pre-built, audited pallets are available in the Polkadot SDK repository, allowing developers to quickly integrate common functionalities.

#### Networking and Storage
Substrate includes fundamental components such as a robust **networking layer** and an efficient **storage mechanism**. The networking layer, often utilizing libp2p, enables secure and efficient peer-to-peer communication among nodes, supporting node discovery, transaction gossiping, and block propagation. For storage, Substrate employs an efficient database, typically a simple key-value storage with a modified Patricia Merkle tree, which is crucial for light clients and quick data retrieval. Substrate also provides complete control over **transaction queue** management processes, allowing developers to define transaction dependencies and priorities.

### Key Features and Capabilities

Substrate's design incorporates several key features that make it a powerful and flexible framework for blockchain development.

#### Forkless Upgrades
One of Substrate’s most significant capabilities is its support for **forkless upgrades**. Traditional blockchains often require hard forks for upgrades, which can lead to network splits or substantial downtime. Substrate, however, enables seamless, live upgrades of a chain's logic by compiling the runtime to WebAssembly (Wasm) and storing it on-chain. When an upgrade is approved through an on-chain governance process, the new Wasm blob is simply swapped, and all connected nodes automatically synchronize with the new logic without interruption. This feature allows blockchain projects to adapt quickly to changing requirements, security updates, or new functionalities.

#### Consensus Flexibility
Substrate provides developers with the flexibility to choose and implement their own consensus mechanisms rather than being tied to a specific one. This allows projects to select algorithms that align with their specific use cases, prioritizing factors like transaction throughput, energy efficiency, or security. Substrate supports popular consensus algorithms such as Proof of Authority (PoA), Proof of Stake (PoS), and Proof of Work (PoW). It also allows for the implementation of custom consensus protocols. The framework decouples block authoring (the process of creating new blocks) from block finalization (resolving forks and choosing the canonical chain), allowing for hybrid consensus models like those used in Polkadot (BABE for authoring and GRANDPA for finality).

#### Interoperability and Cross-Chain Communication
Substrate is designed with a strong emphasis on **interoperability**. Blockchains built with Substrate can natively connect to the Polkadot network as parachains, enabling secure data transfer and inter-chain communication. This connectivity facilitates a wide range of possibilities for multi-chain ecosystems, including cross-chain value transfer, shared security, and decentralized application (dApp) collaboration. Cross-chain bridges, often built using Substrate, are essential for transferring tokens, digital assets, and data between different blockchains, even those operating under disparate protocols or governance structures. Polkadot's XCM (Cross-Consensus Messaging) protocol further enables communication and interaction between parachains and other connected blockchains within the ecosystem.

#### Development Tooling and Ecosystem
Substrate provides a robust tooling ecosystem, offering developers access to resources such as the Substrate Developer Hub, Substrate Playground, and various plugins for popular IDEs. Extensive documentation, SDKs, and tutorials are also available to help reduce the learning curve for both new and experienced blockchain developers. The framework's compatibility with Rust ensures strong community support and a growing talent pool. The broader Substrate ecosystem includes a vibrant community that collaborates on improving the framework, shares knowledge, and provides feedback, fostering continuous innovation.

#### Security
Security is a high priority in Substrate development, with the framework incorporating features to safeguard against vulnerabilities and potential threats. It offers a secure runtime environment and a sandboxed execution environment for smart contracts. By leveraging the Polkadot network, Substrate-based chains can benefit from a shared security model, where the security of all parachains is interconnected with the Polkadot Relay Chain, enhancing overall safety and resilience against attacks.

### Advantages of Substrate Blockchain

Substrate offers numerous advantages that make it an appealing choice for blockchain developers and businesses. Its modular and flexible toolkit simplifies the creation of customized chains, making it accessible even to those new to blockchain development. Substrate provides the flexibility to build purpose-built blockchains tailored to specific use cases, whether public, enterprise, or permissioned networks. This significantly reduces the time and resources required for development and deployment compared to building from scratch.

Substrate's compilation to WebAssembly (Wasm) enhances cross-platform compatibility and enables seamless, live (forkless) upgrades of the blockchain logic without network disruptions or hard forks, ensuring long-term adaptability. It also supports various consensus mechanisms, allowing developers to choose the most suitable algorithm for their project’s performance, security, and scalability needs.

Interoperability is a core benefit, as Substrate-built chains can natively connect to the Polkadot network as parachains, facilitating secure cross-chain communication and data transfer. This enables the creation of multi-chain ecosystems and DApp collaboration. The Framework for Runtime Aggregation of Modularized Entities (FRAME) provides an extensive library of pre-built, audited modules (pallets) for common functionalities like governance, staking, and asset management, which accelerates development and reduces redundant work. Furthermore, Substrate fosters an open-source environment, promoting collaboration and innovation within the blockchain community.

The economic efficiency of Substrate is notable, as its modular design and lightweight architecture lead to lower resource requirements for running blockchain nodes, thus reducing barriers to entry for developers and validators. This framework is designed to be future-proof, allowing developers to keep pace with the rapidly evolving blockchain landscape through its upgradability and composable nature. Substrate’s robust tooling, comprehensive documentation, and active community also provide significant support throughout the development process.

### Limitations and Challenges

Despite its numerous advantages, Substrate blockchain development presents certain limitations and challenges that developers should consider. One significant hurdle is the **learning curve**, especially for developers who are new to blockchain technology or the Rust programming language, which Substrate primarily uses. Mastering Rust's syntax, paradigms, and Substrate's advanced features requires a substantial investment of time and effort.

The **complexity of blockchain development** itself remains a challenge, as it involves understanding and integrating various components like consensus mechanisms, governance models, and runtime logic. Ensuring scalability, interoperability, and upgradability adds to this complexity. While Substrate aims to simplify this, developers still need to navigate these intricacies. The fast-paced evolution of the blockchain ecosystem also demands continuous learning to keep up with the latest trends, tools, and best practices within the Substrate ecosystem.

From a technical standpoint, resources available to Substrate chains, such as **memory usage, storage I/O, and computation**, are limited. Improper configuration or design can lead to performance issues and potential vulnerabilities. For instance, failing to set a depth limit for decoding can break the system, allowing attackers to disrupt network functionality. Additionally, smart contract vulnerabilities, network security (e.g., against Sybil, DDoS, or Eclipse attacks), and user privacy (requiring techniques like encryption and zero-knowledge proofs) remain critical concerns for developers.

While Substrate offers extensive customization, it does have certain **architectural decisions** that might not be easily altered, presenting tradeoffs between technical freedom and ease of development. For example, smart contracts on Substrate cannot natively trigger new transactions directly from on-chain events without external intervention, which can limit certain automated workflows. Scalability, despite features like sharding and parallel execution, can still be a challenge depending on the specific implementation and network demands. Efficient resource management, balancing optimal storage and computational power, is crucial for maintaining performance.

### Supported Consensus Mechanisms

Substrate's modular architecture offers developers significant flexibility in choosing and implementing consensus mechanisms that align with their blockchain's specific requirements. This approach separates block authoring (who produces a block) from finality (which chain is canonical), allowing for tailored consensus solutions.

*   **Aura (Authority Round)**: Aura is a slot-based, round-robin block production algorithm commonly used in permissioned networks with a predetermined set of authorities. In this mechanism, a known set of authorities is selected before block production begins, and they take turns producing blocks in a fixed order during fixed-length time slots. Aura is considered a simple and deterministic consensus mechanism suitable for smaller to medium-sized networks. The `pallet_aura` is a runtime extension of Aura that manages authority rotation and validation.

*   **BABE (Blind Assignment for Blockchain Extension)**: BABE is a slot-based block production mechanism that uses a Verifiable Random Function (VRF) for slot allocation. In each slot, all authorities generate a pseudorandom number, and if it falls below a certain threshold proportional to their weight or stake, they gain the right to produce a block. Other peers validate the legitimacy of a slot claim using the VRF proof. BABE is designed for larger networks and is central to Polkadot's block production, enhancing security and scalability by introducing randomness. The `pallet_babe` is the runtime extension that manages on-chain randomness from VRF and handles epoch transitions.

*   **Proof of Work (PoW)**: Substrate also supports Proof of Work, a computation-based scheduling algorithm where anyone can produce a block by solving a computationally challenging problem. The difficulty of this problem can be adjusted to meet a statistical target. While supported, it is less commonly emphasized compared to other mechanisms in the Substrate ecosystem.

*   **GRANDPA (GHOST-based Recursive ANcestor Deriving Prefix Agreement)**: GRANDPA functions as a **finality gadget** rather than a block authoring mechanism. Its primary role is to provide finality guarantees for blocks, resolving forks and ensuring that only the canonical chain exists. In the GRANDPA protocol, validators vote on chains rather than individual blocks, and their votes transitively apply to all previous blocks. A block is considered finalized once two-thirds of the GRANDPA authorities have voted for it. This mechanism complements block production algorithms like BABE to achieve secure and irreversible consensus.

Substrate's ability to "hot-swap" consensus engines, even after a chain has gone live, underscores its adaptability. This flexibility allows developers to select the most suitable consensus algorithm for their network's objectives, whether they prioritize speed, energy efficiency, or security.

### Use Cases and Applications

The Substrate Blockchain framework's versatility and modularity enable a wide array of use cases and applications across various industries.

*   **Customizable Blockchains**: Substrate empowers developers to create application-specific blockchains precisely tailored to unique industry requirements, such as decentralized finance (DeFi), supply chain management, identity verification, and gaming. This allows for bespoke governance models, consensus mechanisms, and tokenomics.

*   **Decentralized Finance (DeFi)**: Substrate is widely used for building various DeFi applications, including decentralized exchanges (DEXs), lending platforms, stablecoins, and asset management tools. Its modular architecture supports composable financial primitives, fostering innovative and complex financial products.

*   **Supply Chain Management**: The framework facilitates the creation of transparent and traceable supply chain solutions, where every step is recorded on the blockchain. This enhances product authenticity, reduces counterfeiting, improves transparency, and streamlines logistics.

*   **Identity Management**: Substrate can power decentralized identity solutions, giving users control over their personal data and allowing selective sharing with trusted parties. This is applicable for self-sovereign identity, KYC/AML compliance, and secure access management.

*   **Gaming and NFTs**: Substrate supports the development of blockchain-based gaming platforms and marketplaces for non-fungible tokens (NFTs). Developers can create and enable secure trading of unique digital assets such as in-game items, collectibles, and artwork.

*   **Governance and DAOs**: Tools provided by Substrate enable the creation of decentralized autonomous organizations (DAOs) and the implementation of on-chain governance mechanisms. This allows communities to collectively make decisions, manage protocol upgrades, and allocate funding in a transparent and decentralized manner.

*   **IoT and Edge Computing**: Substrate can be used to build decentralized IoT networks where devices interact and transact autonomously without relying on centralized intermediaries. Combining blockchain with edge computing leads to secure and scalable IoT solutions for smart cities or environmental sensing.

*   **Tokenization of Real-World Assets**: The framework facilitates the tokenization of tangible assets like real estate, stocks, commodities, and intellectual property rights. Representing these assets as digital tokens on a blockchain enables easy transfer, fractionalization, and transparent trading.

*   **Decentralized Social Networks**: Substrate can power decentralized social networks where users maintain full control over their data and interactions. Features like content moderation, reputation systems, and micro-payments can be implemented for censorship-resistant social platforms.

*   **Cross-Chain Bridges**: A significant use case involves building cross-chain bridges that enable the transfer of tokens, digital assets, smart contract instructions, or data between different blockchains. These bridges are crucial for enhancing collaboration and resource sharing across diverse blockchain ecosystems. Moonbeam, for instance, uses Substrate to bridge the Ethereum and Polkadot ecosystems.

*   **Parachains and Parathreads**: Substrate is integral to the development of parachains within the Polkadot ecosystem. Parachains are customizable, specialized blockchains that operate in parallel to the Polkadot Relay Chain, benefiting from shared security and efficient payment settlement. Substrate simplifies deploying customized parachains for specific use cases. Parathreads extend this concept, allowing Substrate projects to gain shared security and connectivity benefits without a dedicated parachain slot, offering a more cost-effective entry point into Polkadot.

*   **Relay Chains**: Substrate also enables developers to create their own Polkadot-like relay chains, which serve as the core of a network, managing consensus, security, and cross-chain interoperability for connected parachains.

### Prominent Projects Built on Substrate

Numerous notable projects and networks have chosen Substrate as their foundational framework, demonstrating its widespread adoption and versatility.

*   **Polkadot**: This is the flagship network built on Substrate, serving as a multi-chain protocol that connects independent blockchains and provides shared security and interoperability. Polkadot has a market capitalization of over $60 billion as of February 2023.
*   **Kusama**: Often referred to as Polkadot’s "canary network," Kusama is also built on Substrate and serves as a live testing ground for new features and upgrades before their deployment on Polkadot.
*   **Acala Network**: Acala is a decentralized finance (DeFi) platform built as a parachain on Polkadot, offering functionalities like a decentralized stablecoin and a multi-collateralized lending platform.
*   **Moonbeam**: This is a smart contract platform built on Substrate that facilitates seamless interactions between the Ethereum and Polkadot ecosystems, enabling cross-chain token and asset transfers. Moonbeam's flexibility allows it to adapt to evolving blockchain standards while being EVM compatible.
*   **ChainX**: A Substrate-based network focused on cross-chain asset management, enabling users to swap, transfer, and manage assets across different blockchain networks.
*   **Darwinia Network**: This Substrate-based network provides a platform for building and deploying decentralized applications (DApps) across different blockchain networks, ensuring interoperability and a seamless user experience.
*   **Litentry**: A decentralized identity assembly system that leverages the Substrate Blockchain Framework to enhance digital identity in terms of self-governance, allowing users to control their data and privacy across various platforms.
*   **Energy Web Chain (EWC)**: A public blockchain with a proof-of-authority consensus, based on Ethereum technology but adaptable using Substrate, functioning as a core trust layer for decentralized identities and smart contract execution in the energy sector.
*   **Centrifuge**: Utilizes parathreads built with Substrate to connect real-world assets to the Polkadot network, facilitating asset-backed lending in DeFi.
*   **Parity Signer**: A product by Parity Technologies that allows users to convert an unused mobile phone into an air-gapped hardware wallet for enhanced security.

These projects illustrate Substrate's ability to power diverse and innovative blockchain solutions across various sectors, benefiting from its core features such as modularity, interoperability, and upgradeability. As of recent statistics, the number of projects built on Substrate has increased by over 400% in the past two years, with more than 150 active projects in various stages of development, and over 200 total projects built on the framework.

### Development Resources and Documentation

For developers looking to engage with Substrate, a wealth of resources and documentation is available to facilitate the building process. The primary and most comprehensive resource is the **Polkadot Developer Docs**, accessible at docs.polkadot.com. This platform provides essential tools, guides, and resources for building custom chains, deploying smart contracts, and creating decentralized applications (dApps).

Key areas covered in the documentation include:
*   **Building Custom Chains**: Guides on how to get started with the Polkadot SDK to build and deploy custom blockchains, including fast-tracking development with preconfigured templates and customizing business logic.
*   **Smart Contract Development**: Information on writing, testing, and deploying smart contracts using `ink!`, a Rust-based smart contract language tailored for Substrate chains. It also covers other languages like AssemblyScript (ask!) and Solidity (via Solang compiler) that compile to WebAssembly (Wasm) for execution on Substrate’s `pallet-contracts`.
*   **Core Concepts**: Detailed explanations of fundamental Substrate concepts such as pallets (modular runtime components), the runtime (the state transition function), consensus mechanisms, accounts, extrinsics (transactions), and the mechanism of forkless runtime upgrades.
*   **Developer Tools**: Access to libraries such as the Python Substrate Interface, which enables interaction with Polkadot SDK-based chains for querying data, submitting transactions, and managing blockchain interactions.
*   **Community Resources**: An active community contributes to and supports the Substrate ecosystem, with platforms for collaboration, knowledge sharing, and feedback. This includes GitHub repositories like `awesome-substrate` which curates a list of projects and resources.
*   **Tutorials and How-to Guides**: Guided exercises and workflows are available to help developers achieve specific goals and reduce the learning curve.
*   **Reference Documentation**: Versioned API documentation provides in-depth technical details.

Overall, the Polkadot Developer Docs serve as the primary entry point for Substrate development, supplemented by a rich ecosystem of community-driven resources, libraries, and tools that support building scalable and secure blockchain solutions.

Bibliography
A dive into Substrate’s Consensus Mechanism | Coinmonks | - Medium. (2023). https://medium.com/coinmonks/a-dive-into-substrates-consensus-mechanism-30366a4a4213

Blockchain security – Six common mistakes found in Substrate chains. (2021). https://www.srlabs.de/blog-post/blockchain-security-six-common-mistakes-found-in-substate-chains

Build Scalable Chains with Substrate Blockchain - Webisoft. (2025). https://webisoft.com/articles/substrate-blockchain/

Common Vulnerabilities in Substrate/Polkadot Development. (2023). https://forum.polkadot.network/t/common-vulnerabilities-in-substrate-polkadot-development/3938

Comparing Cosmos vs Substrate: 10 Key Differences - Webisoft Blog. (2025). https://webisoft.com/articles/cosmos-vs-substrate/

Cosmos vs Substrate: A Comparison - LeewayHertz. (n.d.). https://www.leewayhertz.com/cosmos-vs-substrate/

Deep dive into Substrate consensus - part 1 - Polkadot Study. (2024). https://polkadot.study/tutorials/substrate-in-bits/docs/deep-dive-into-substrate-consensus-part-1

Exploring 10 Must-know Substrate-based Projects - Zeeve. (2023). https://www.zeeve.io/blog/exploring-10-must-know-substrate-based-projects/

How it Works – Substrate | Documentation - ink! (2025). https://use.ink/docs/v4/how-it-works

Polkadot & Substrate Overview - Dune Docs. (2024). https://docs.dune.com/data-catalog/substrate/overview

Polkadot Developer Docs. (2025). https://docs.polkadot.com/

polkadot-developers/awesome-substrate - GitHub. (2019). https://github.com/polkadot-developers/awesome-substrate

polkadot-developers/substrate-docs - GitHub. (2021). https://github.com/substrate-developer-hub/substrate-docs/

Popular Substrate Projects Building In 2020 And Their Frameworks. (2020). https://certik.medium.com/popular-substrate-projects-building-in-2020-and-their-frameworks-6589d42408ab

Popular Use Cases of Substrate Blockchain Framework. (2024). https://www.rapidinnovation.io/post/top-use-cases-of-substrate-blockchain-framework

Python Substrate Interface | Polkadot Developer Docs. (2024). https://docs.polkadot.com/develop/toolkit/api-libraries/py-substrate-interface/

Substrate | Vara Network Documentation Portal. (n.d.). https://wiki.vara.network/docs/about/technology/substrate

Substrate - HackQuest. (2024). https://www.hackquest.io/en/glossary/Substrate

Substrate: a generic Rust-based blockchain framework | Medium. (2024). https://medium.com/@brunopgalvao/substrate-cfeb13333f2c

Substrate, an overview - Humanode. (2021). https://blog.humanode.io/substrate-an-overview/

Substrate Blockchain Development - Virstack. (2023). https://www.virstack.com/substrate-blockchain-development/

Substrate blockchain development: Core concepts - LogRocket Blog. (2021). https://blog.logrocket.com/substrate-blockchain-framework-core-concepts/

Substrate blockchain development core concepts - Medium. (2022). https://medium.com/nerd-for-tech/substrate-blockchain-development-core-concepts-ce3c7d808e7

Substrate Blockchain Framework | A Suitable And Reliable Option. (2022). https://risingmax.com/blog/substrate-blockchain-framework

Substrate Definition - CoinMarketCap. (2021). https://coinmarketcap.com/academy/glossary/substrate

Substrate Development Services & Solutions - Nadcab Labs. (2025). https://www.nadcab.com/blog/substrate-blockchain-development

Substrate framework introduction - LinkedIn. (2023). https://www.linkedin.com/pulse/substrate-introductions-amit-nadiger

Substrate vs Ethereum: Differences and Similarities - MixBytes. (2025). https://mixbytes.io/blog/substrate-vs-ethereum-differences-and-similarities

The limits of Smart Contracts… - Ramsey Ajram (Decentration). (2024). https://decentration.medium.com/the-limits-of-smart-contracts-5dedf6dfafda

The Polkadot architecture and introduction to the Substrate ... (2023). https://cointelegraph.com/learn/articles/the-polkadot-architecture-and-introduction-to-the-substrate-infrastructure

The Ultimate Guide to Substrate Blockchain Framework - Medium. (2023). https://medium.com/@blockchaindevelopmentco/the-ultimate-guide-to-substrate-blockchain-framework-antier-solutions-f0c13688aa27

Top Use Cases of Substrate Blockchain Framework in 2024. (2023). https://www.antiersolutions.com/blogs/a-deep-dive-into-substrate-blockchain-use-cases/

Use cases of Substrate Framework - LeewayHertz. (n.d.). https://www.leewayhertz.com/use-cases-of-substrate-framework/

Use Cases of Substrate Framework- A Complete Guide - Medium. (2024). https://medium.com/predict/use-cases-of-substrate-framework-a-complete-guide-01004eecc07f

Use Cases of Substrate Framework- A Complete Guide - SoluLab. (2024). https://www.solulab.com/use-cases-of-substrate-framework/

welcome-to-substrate.md - GitHub. (n.d.). https://github.com/substrate-developer-hub/substrate-docs/blob/main/content/md/en/docs/learn/welcome-to-substrate.md

What is Substrate? - Moonbeam network. (2023). https://www.moonbeam.network/news/what-is-substrate

What is Substrate Framework? - Gate.com. (2023). https://www.gate.com/learn/articles/what-is-substrate-framework/1010



Generated by Liner
https://getliner.com/search/s/5926611/t/85975216