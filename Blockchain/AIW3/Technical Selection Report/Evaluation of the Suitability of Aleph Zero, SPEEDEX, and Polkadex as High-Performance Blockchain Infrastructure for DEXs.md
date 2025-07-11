Evaluate Polkadex, SPEEDEX, and Aleph Zero with regard to their suitability for serving as infrastructural blockchains capable of supporting over 100,000 TPS (transactions per second) for order-book-based DEXs (decentralized exchanges). Requirements: 
 1. Consider the following aspects: core components, core functions, architectural features, on-chain order-book supportability/customizability, chain development language, smart contract language, major technology stacks, difficulty and cost of customization/development, GitHub stars, level of decentralization, permissioned/permissionless, transparency, scalability, consensus mechanism, fault tolerance, cross-chain capabilities, advantages/disadvantages, constraints, risks, TPS and the conditions under which TPS testing was conducted, latency, maturity, ecosystem, market prospects, and transaction cost, among others. 
 2. Prepare a competitor analysis and a summary table that clearly identifies the optimal choice for a high-performance DEX blockchain. 
 3. Utilize lists and tables as necessary to enhance clarity and readability. 
 4. Provide a list of official materials, including GitHub links, official websites, documents, white papers, etc.

Fri Jul 11 2025

### Polkadex: A Detailed Evaluation for High-Performance DEX Infrastructure

Polkadex is an open-source, decentralized exchange (DEX) platform built using the Substrate blockchain framework within the Polkadot ecosystem. It aims to combine the speed and user experience of centralized exchanges (CEXs) with the security and non-custodial nature of decentralized solutions. Polkadex specifically supports order-book-based trading for high-performance scenarios.

#### Core Components, Functions, and Architectural Features
Polkadex's core components include the **Polkadex Network**, which is its native blockchain with integrated liquidity pools (Polkapool) and an orderbook engine. A key architectural feature is the use of a **Layer 2 Trusted Execution Environment (TEE)**, specifically a SubstraTEE solution, which calculates the balance state of users in the orderbook without requiring on-chain balance transfers for every operation, enabling high-frequency and feeless transactions. The **Orderbook Engine** efficiently matches trades, while the **Interplanetary File System (IPFS)** functions as an insurance mechanism for instant fund recovery if balance transfers are rejected. Polkadex offers core DEX functions such as decentralized **limit and market orders**, features typically found in centralized exchanges. It supports **high-frequency trading** and **trading bots** through APIs that observe market changes and submit trades. The platform also aims to provide fiat integration through decentralized KYC capabilities.

#### On-Chain Order-Book Supportability and Customizability
Polkadex primarily supports its order book operations through a Layer 2 TEE where off-chain execution is performed, with settlement occurring on-chain via the Polkadex Network. This architecture aims to deliver low latency and feeless order placement. Polkadex is highly customizable for trading features, order types, and market-making bots, particularly due to its Substrate-based design that allows for flexible execution logic and the presence of off-chain workers and TEEs. It supports Ethereum and Substrate-based assets, with plans for advanced cross-chain bridges. The transparency of trade matching can be limited as some execution happens off-chain in the TEE.

#### Chain Development Language and Smart Contract Language
Polkadex is developed primarily using the **Rust programming language** within the **Substrate blockchain framework**. Smart contracts on Polkadex are supported through Rust/ink!, an embedded domain-specific language that compiles to WebAssembly (Wasm). Additionally, Polkadex supports Ethereum-compatible languages like Solidity or Vyper, allowing a broad range of developers to build on the platform.

#### Major Technology Stacks
The major technology stacks utilized by Polkadex include the **Substrate blockchain framework**, **Rust programming language**, and **WebAssembly (Wasm)** for runtime execution. It integrates a **Layer 2 Trusted Execution Environment (TEE)** (specifically SubstraTEE) for off-chain order book computations, and **IPFS** for decentralized storage functionalities. Polkadex employs the **BABE and GRANDPA consensus algorithms** within Polkadot's Nominated Proof-of-Stake (NPoS) framework.

#### Difficulty and Cost of Customization/Development
While Polkadex benefits from Substrate's modularity, the integration of advanced features like TEEs introduces moderate to high complexity. This complexity implies a significant investment in development and requires specialized expertise for customization. The extensive security audits conducted by Hacken suggest a substantial commitment to development and security.

#### GitHub Stars and Transparency
The primary Polkadex repository on GitHub has approximately 291 stars. As an open-source project, its codebase is publicly available, fostering transparency in development. Polkadex also incorporates **on-chain governance**, where token holders can propose and vote on changes to the network, contributing to its decentralized nature and ensuring transparency in decision-making.

#### Level of Decentralization and Permissioning
Polkadex is positioned as a **fully decentralized, peer-to-peer, order-book-based cryptocurrency exchange**. It emphasizes **non-custodial trading**, meaning users retain full control over their funds. The platform’s decentralization is further supported by its aim to be a parachain in Polkadot, enabling trustless liquidity from other blockchains via the Polkadot relay chain network. Polkadex is a **permissionless blockchain**, allowing open participation in network validation and governance.

#### Scalability, TPS, and Latency
Polkadex is designed for high scalability, leveraging Polkadot's multi-core architecture and sharding mechanisms to process many transactions concurrently. It claims a capability of supporting up to **500,000 trades per second (TPS)** with **sub-millisecond latency** in its order book operations, which is crucial for high-frequency and algorithmic trading. However, under test conditions, the Babe/Grandpa consensus algorithm allows transaction speeds of up to **400 TPS**.

#### Consensus Mechanism and Fault Tolerance
Polkadex utilizes a hybrid consensus mechanism, integrating **Nominated Proof-of-Stake (NPoS)** along with **BABE for block production** and **GRANDPA for finality**. This combination ensures both probabilistic and provable finality, enhancing network security and scalability. For fault tolerance, Polkadex validators can run on globally distributed, fault-tolerant server clusters (e.g., AWS, Digital Ocean) and employ snapshot failover mechanisms for quick restoration and data integrity. The system is designed to recover from hardware and software malfunctions and maintain continuous operation.

#### Cross-Chain Capabilities
Polkadex aims for robust cross-chain capabilities. It intends to connect directly to the Ethereum network using the ChainBridge protocol and become a parachain in Polkadot to bring liquidity from other blockchains. The **THEA interoperability layer** is designed to enable seamless deposits and withdrawals between Polkadex and other blockchains like Ethereum.

#### Advantages and Disadvantages
**Advantages** include high theoretical throughput (up to 500,000 TPS claimed) and low latency (~20 ms) for order book operations, a non-custodial and decentralized order-book model, support for advanced trading features like bots and high-frequency trading, and zero gas fees on its network. **Disadvantages** include the fact that its ambitious TPS claims are largely architectural targets rather than fully demonstrated on-chain performance. Its reliance on Layer 2 TEEs introduces specific trust assumptions regarding enclave security, and it faces inherent liquidity challenges common in early DEXes.

#### Constraints and Risks
A primary constraint is the gap between claimed theoretical TPS and tested on-chain throughput, which relies on off-chain components. While claiming to solve **front-running** through its custom blockchain and feeless transactions, the risk of such manipulations remains a general concern in decentralized finance. Security audits have revealed and fixed vulnerabilities like SQL injection and DoS attacks, highlighting the continuous need for security vigilance.

#### Maturity and Market Prospects
Polkadex officially launched its mainnet in late 2021. Subsequent components like the Polkadex Orderbook and Polkapool were rolled out gradually. The project prioritizes stability and thorough auditing, indicating a matured deployment approach. Its market prospects are favorable as it leverages the growing Polkadot ecosystem and aims to address DEX liquidity and scalability challenges.

#### Transaction Cost
Polkadex aims to offer **feeless transactions** and **zero gas fees** for placing and removing orders, making it attractive for high-frequency trading. There is a small trading fee for market taking orders, while market-making orders are completely free.

### SPEEDEX: A Detailed Evaluation for High-Performance DEX Infrastructure

SPEEDEX is a decentralized exchange (DEX) protocol designed for scalability, parallelization, and economic efficiency, allowing participants to trade assets securely without any single party exerting undue control over the market. It is primarily a research prototype with significant theoretical advantages for high-performance DEX operations.

#### Core Components, Functions, and Architectural Features
SPEEDEX operates entirely within a **Layer-1 blockchain**. Its core innovation lies in using an **Arrow-Debreu exchange market structure**, which fixes asset valuations for all trades within a given block of transactions. This structure eliminates internal arbitrage opportunities and helps prevent certain front-running attacks by ensuring that a direct trade from asset A to asset B always receives as good a price as trading through some third asset. Trades are processed in batches, making operations commutative and highly parallelizable. SPEEDEX supports traditional **limit orders** where users can specify a minimum price for their trades.

#### On-Chain Order-Book Supportability and Customizability
SPEEDEX is designed as a fully on-chain order book decentralized exchange, where all trade offers and matching occur entirely on-chain within the Layer-1 blockchain environment. It employs an Arrow-Debreu market structure that fixes asset valuations for all trades within a block, preventing internal arbitrage and certain front-running attacks. Customizability is high due to its fully on-chain architecture with commutative batch processing, allowing protocol-level adjustments. As a fully on-chain model, SPEEDEX offers maximum transparency in trade execution and order book state.

#### Chain Development Language and Smart Contract Language
The standalone implementation of SPEEDEX is available on GitHub. While specific core development language for its underlying blockchain is not universally stated across documents, its core algorithmic components have been implemented using performant languages. The underlying consensus layer can use protocols like HotStuff, which are typically implemented in well-supported languages like C++. SPEEDEX's core logic is implemented natively within the blockchain’s protocol rather than as smart contracts; therefore, there is no established smart contract language support intrinsic to SPEEDEX at this stage.

#### Major Technology Stacks
SPEEDEX operates as a **Layer-1 blockchain protocol** designed around an **Arrow-Debreu exchange market structure**. Its implementation involves high-performance languages (inferred C++) for its core market algorithms. It utilizes **Byzantine Fault Tolerant (BFT) consensus mechanisms** such as HotStuff to ensure security. It emphasizes batch processing and parallelizable transaction execution for scalability.

#### Difficulty and Cost of Customization/Development
Direct information on the difficulty and cost of customization for SPEEDEX is limited, but its novel design, involving complex algorithms for batch price computation and parallel execution, suggests significant development complexity. Achieving its high throughput necessitates powerful hardware, such as 48-core servers, which implies considerable infrastructure costs.

#### GitHub Stars and Transparency
The `scslab/speedex` GitHub repository contains its standalone implementation. The number of GitHub stars is stated as 24. As a research-driven prototype, the project's transparency is primarily seen through its academic papers and open-source implementation rather than established governance structures. There is minimal public information on governance frameworks or broader community involvement beyond the academic sphere.

#### Level of Decentralization and Permissioning
SPEEDEX is designed to be a **fully on-chain decentralized exchange** that runs entirely within a Layer-1 blockchain, aiming to achieve its scalability without fragmenting market liquidity. It ensures decentralization by allowing participants to securely trade assets without giving any single party undue control over the market. This design prevents risk-free front-running by processing transactions at a shared set of exchange rates within a block, thereby eliminating transaction ordering within the block as a source of miner extractable value (MEV). SPEEDEX is a **permissionless blockchain**, suitable for open, decentralized operation without requiring access authorization.

#### Scalability, TPS, and Latency
SPEEDEX achieves high scalability through its unique market structure that makes trade operations **commutative and parallelizable**. It has demonstrated high throughput, specifically **over 200,000 transactions per second (TPS)** on 48-core servers, even with tens of millions of open offers. This performance is achieved by executing every order at the same price as every other order in the same block and processing blocks of limit orders as a unified batch. However, its Layer-1 batch processing implies higher latency, likely in the order of seconds for full finality.

#### Consensus Mechanism and Fault Tolerance
SPEEDEX itself is not a blockchain but is designed to be integrated into any blockchain. It benefits from underlying blockchain consensus protocols. Implementations of SPEEDEX have used the **HotStuff consensus protocol**, which is a Byzantine Fault Tolerant (BFT) protocol offering strong security guarantees. The BFT consensus ensures that even if some nodes are malicious (up to approximately one-third), the network can still reach agreement and maintain integrity.

#### Cross-Chain Capabilities
The available documents primarily focus on SPEEDEX's high-throughput capabilities within a single Layer-1 blockchain. Its design emphasizes achieving scalability without fragmenting market liquidity between multiple blockchains or rollups. Therefore, native cross-chain bridging capabilities are not explicitly highlighted as a core feature of SPEEDEX itself, implying a focus on deep single-chain efficiency rather than multi-chain interoperability.

#### Advantages and Disadvantages
**Advantages** include its unique design for high throughput (over 200,000 TPS) and parallelization, its ability to eliminate internal arbitrage and risk-free front-running, and its full on-chain operation that avoids liquidity fragmentation. **Disadvantages** are its current status as a prototype not yet fully deployed in a production blockchain, its reliance on powerful hardware for peak performance, and the potential complexity of its underlying economic model. It also has limited or absent cross-chain capabilities.

#### Constraints and Risks
A primary constraint is its **prototyped status**, meaning it has not yet undergone widespread real-world decentralized deployment, leaving practical risks potentially untested. Its high performance is dependent on **high computational resources** like 48-core servers. While designed to prevent certain types of front-running, it does not eliminate every type, such as delaying victim transactions to a future block.

#### Maturity and Market Prospects
SPEEDEX is currently at a prototyping or pre-mainnet stage. While its theoretical advantages for scalability and fairness are significant, its market presence is nascent, and adoption trends are still early. Its design holds potential for high-frequency trading infrastructure, but successful practical deployment is essential for broader market prospects.

#### Transaction Cost
The documents do not provide explicit figures for transaction fees. However, SPEEDEX processes transactions in large batches, which, by design, implies an aim for economically efficient and low per-transaction costs when scaled.

### Aleph Zero: A Detailed Evaluation for High-Performance DEX Infrastructure

Aleph Zero is a Layer 1 blockchain platform that aims to solve the scalability, security, and privacy challenges faced by traditional blockchain technologies. It distinguishes itself with a novel consensus protocol and modular privacy features, making it suitable for high-performance decentralized exchange (DEX) infrastructure.

#### Core Components, Functions, and Architectural Features
Aleph Zero is built as an independent Layer 1 blockchain integrated with the **Substrate framework**. Its core components include the **AlephBFT consensus protocol**, which combines Proof-of-Stake (PoS) with a Directed Acyclic Graph (DAG) as an auxiliary data structure for rapid finality. The architecture supports **modular zero-knowledge (ZK) data confidentiality features**, including Liminal, a software-based privacy layer built on zero-knowledge proofs (ZKPs) and secure multi-party computation (sMPC). It also integrates a decentralized file storage system and an Oracle bridge for expanded functionality. Aleph Zero offers enterprise-grade functionalities such as **private smart contracts**, cross-chain interoperability, and the hosting of decentralized applications (dApps). The platform supports decentralized exchanges like 'Common', a DEX built on Aleph Zero. Aleph Zero also addresses Maximal Extractable Value (MEV) by encrypting transactions and revealing them to validators only after a set period, preventing manipulation.

#### On-Chain Order-Book Supportability and Customizability
Aleph Zero is primarily a Layer 1 blockchain with a DAG-based aBFT consensus, and while not solely an order-book DEX infrastructure, projects like Common are targeting order-book models with privacy enhancements. It supports Turing-complete smart contracts via its ink! language and is evolving EVM compatibility with Layer 2 support, enabling the development of custom order book implementations. The platform is highly modular and supports private and public order books, with privacy options being opt-in. Its smart contract environment allows creation of complex order-book logic and the possibility to run privacy-preserving pools.

#### Chain Development Language and Smart Contract Language
Aleph Zero's core is developed in **Rust**, allowing integration with Parity's Substrate technology stack. It utilizes **ink!**, a Rust-based embedded domain-specific language (eDSL) for smart contracts, which compiles to WebAssembly (Wasm). Furthermore, Aleph Zero is expanding its compatibility with the **Ethereum Virtual Machine (EVM)**, with plans to allow Solidity and Yul for smart contracts.

#### Major Technology Stacks
Aleph Zero is developed on the **Substrate framework** using the **Rust programming language**. Its core consensus is **AlephBFT**, an asynchronous Byzantine Fault Tolerant (aBFT) protocol integrating Directed Acyclic Graph (DAG) structures. It uses **ink!** (a Rust DSL) for smart contract development, with WebAssembly (Wasm) compilation. Aleph Zero features modular privacy components like Liminal, leveraging **zero-knowledge proofs (ZK-proofs)** and **secure multi-party computation (sMPC)**.

#### Difficulty and Cost of Customization/Development
Aleph Zero aims to provide a developer-friendly experience by leveraging familiar technologies like Rust and Substrate, and by supporting EVM compatibility. While deep customization, especially for enterprise applications, can be time and capital-intensive, the platform's efficient design and ecosystem support help mitigate some barriers. The project has secured significant funding for its development efforts.

#### GitHub Stars and Transparency
Aleph Zero maintains an active presence on GitHub, with its main node repository, `Cardinal-Cryptography/aleph-node`, having approximately 92 stars. The `alephzero/alephzero` repository has 84 stars. The project is open-source, promoting transparency in its development. Aleph Zero is committed to transparency, actively engaging in peer-reviewed protocols and public documentation. Its governance framework, developed with Syncra, includes on-chain voting with undisclosed features for privacy and transparent treasury management, ensuring community influence over network parameters and funds.

#### Level of Decentralization and Permissioning
Aleph Zero is designed for a high level of decentralization. Its **AlephBFT consensus protocol** is leaderless and asynchronous, making it resilient to malicious nodes and network disruptions. The network employs a **rotating committee of validators**, ensuring no single entity has undue control. Deutsche Telekom MMS has also joined its network of validators, contributing to security and decentralization. The project is gradually moving towards full community-driven governance, with a foundation nomination program to further decentralize the network. Aleph Zero is explicitly identified as a **permissionless blockchain**, allowing anyone to participate securely in the network.

#### Scalability, TPS, and Latency
Aleph Zero is designed for high scalability, leveraging its DAG-based AlephBFT consensus protocol for parallel transaction ordering and sub-second finality. In lab tests, Aleph Zero achieved approximately **89,600 transactions per second (TPS)** with a **416-millisecond validation time** using 112 AWS nodes globally. The platform claims to be able to handle 100,000 TPS in a fully decentralized system.

#### Consensus Mechanism and Fault Tolerance
Aleph Zero employs its proprietary **AlephBFT consensus mechanism**, a peer-reviewed asynchronous Byzantine Fault Tolerant (aBFT) protocol. This protocol is designed to tolerate up to **33% malicious committee members** without affecting the validation process, ensuring robust security and resilience even during periods of total asynchrony. The rotating committee structure further enhances its fault tolerance and decentralization.

#### Cross-Chain Capabilities
Aleph Zero has a comprehensive cross-chain strategy. The **MOST bridge** connects Aleph Zero with Ethereum, facilitating asset transfers and smart contract interoperability. It also integrates with **Router Protocol** to expand connectivity across various blockchains. Additionally, Aleph Zero's integration with **Across Protocol** enables rapid (2-second) cross-chain bridging across 14 other EVM-compatible chains with reduced fees. A **zParachain bridge** connects Aleph Zero with Polkadot without it being a parachain itself.

#### Advantages and Disadvantages
**Advantages** include high performance with near 90,000 TPS and sub-second finality, a unique AlephBFT consensus, strong emphasis on privacy with ZK-proofs and sMPC, modular Substrate-based architecture, and robust security. It also boasts a clear roadmap, a maturing ecosystem, and a focus on enterprise readiness. **Disadvantages** include the inflationary tokenomics, which need careful management, and while decentralizing, some centralized control remains, such as the Aleph Zero Foundation retaining a majority in the block finalization process in early stages.

#### Constraints and Risks
One risk is regulatory scrutiny due to its advanced privacy-enhancing features. While AlephBFT offers robust fault tolerance, any undiscovered vulnerabilities in its complex cryptographic components could pose risks. The platform also faces the challenge of managing dynamic fee adjustments to prevent spam.

#### Maturity and Market Prospects
Aleph Zero launched its mainnet in late 2021. Smart contracts were launched on the mainnet in 2023. It has an active and growing ecosystem, with numerous projects building on it, including DEXs like Common. The platform is gaining increasing interest from institutional players and has strategic partnerships, such as with Deutsche Telekom. Its market capitalization and daily volume suggest growing market interest.

#### Transaction Cost
Aleph Zero is noted for very low transaction fees, with an average cost of approximately \\(\$0.0003\\) per transaction. This translates to a very minimal cost, making it highly suitable for high-frequency trading where transaction fees can significantly impact profitability.

### Competitor Analysis and Optimal Choice

This section provides a comparative analysis of Polkadex, SPEEDEX, and Aleph Zero concerning their suitability for supporting high-performance, order-book-based decentralized exchanges requiring over 100,000 TPS.

#### Comparative Analysis

**Performance (TPS & Latency)**
Polkadex makes strong claims of up to 500,000 TPS with sub-millisecond latency for its order book operations, enabled by a Layer-2 TEE. However, its tested on-chain consensus layer speeds are around 400 TPS. SPEEDEX has demonstrated over 200,000 TPS in controlled 48-core server environments, but its Layer-1 operation may lead to latencies in the order of seconds for full block finalization. Aleph Zero has validated impressive figures of approximately 89,600 TPS with sub-second finality (416ms) in globally distributed AWS node tests.

**Decentralization and Permissioning**
Polkadex maintains decentralization through non-custodial trading and on-chain governance, building on Polkadot's shared security model. SPEEDEX operates fully on-chain with commutative semantics to ensure fairness and prevent centralized control, and it is designed to be permissionless. Aleph Zero showcases robust decentralization with a leaderless, asynchronous AlephBFT consensus and a rotating committee of over 100 active validators, actively transitioning to full community governance. All three are permissionless blockchains.

**Cross-Chain Capabilities**
Polkadex relies on being a Polkadot parachain and uses bridges like Thea for interoperability with Ethereum. SPEEDEX focuses on high throughput within a single Layer-1 chain; explicit cross-chain features are not a primary highlight. Aleph Zero has the most comprehensive cross-chain strategy, with MOST (Ethereum bridge), Router Protocol integration, Across Protocol for 14+ EVM chains (2-second transfers), and a zParachain bridge to Polkadot.

**Maturity and Ecosystem**
Polkadex is a mature project with its mainnet launched in late 2021 and components rolling out, benefiting from the broader Polkadot ecosystem. SPEEDEX is primarily a prototype from academic research, not yet deployed on a mainnet, implying an earlier stage of ecosystem and community development. Aleph Zero launched its mainnet in late 2021 and has a rapidly expanding ecosystem with smart contracts, privacy features, and institutional partnerships.

**Privacy Features and Transaction Costs**
Polkadex uses TEEs for secure off-chain computation but doesn't emphasize broader privacy beyond that. SPEEDEX doesn't explicitly focus on privacy features beyond preventing front-running. Aleph Zero has a strong privacy focus with Liminal, leveraging ZK-proofs and sMPC for confidential transactions and smart contracts, aiming for regulatory compliance. Polkadex aims for zero gas fees for order placement. While SPEEDEX's transaction costs are not explicitly detailed, its batch processing implies economic efficiency. Aleph Zero boasts extremely low transaction fees, averaging approximately \\(\$0.0003\\) per transaction.

#### Summary Table: DEX Blockchain Suitability

| Feature                       | Polkadex                                                        | SPEEDEX                                                         | Aleph Zero                                                     |
|:------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------|:---------------------------------------------------------------|
| **Core Components**           | Network, TEE, Orderbook Engine, IPFS                   | Layer-1 blockchain, Arrow-Debreu Market Structure | AlephBFT (PoS+DAG), Liminal (ZK/sMPC), IPFS      |
| **Core Functions**            | Orderbook (limit/market), HFT, bots, Fiat support | Batch processing, internal arbitrage/front-running prevention | Private smart contracts, MEV resistance, DEX support |
| **Architectural Features**    | Substrate-based Parachain, Layer 2 TEE         | Layer-1, Commutative/Parallelizable Trades       | Layer-1, DAG-based aBFT, Substrate, EVM Layer 2   |
| **On-Chain Order-Book Support** | Layer 2 TEE off-chain execution, on-chain settlement   | Fully on-chain at Layer 1                              | Smart contracts support, privacy-enhanced possible |
| **Customizability**           | High via Substrate and TEEs                            | High due to fully on-chain architecture                  | High via ink! contracts & EVM compatibility   |
| **Chain Dev. Language**       | Rust (Substrate Framework)                    | C++ (inferred for core algorithms)                     | Rust (Substrate + AlephBFT)                  |
| **Smart Contract Language**   | Rust (ink!), EVM compatible (Solidity)       | N/A (protocol-level implementation)                      | Rust (ink! for Wasm), EVM compatible (Solidity) |
| **Major Tech Stacks**         | Substrate, Rust, Wasm, TEE, IPFS               | HotStuff BFT, C++ (prototyped)                         | Substrate, Rust, ink!, AlephBFT, ZK-proofs, sMPC |
| **Difficulty/Cost Dev.**      | Moderate to High (TEE complexity)                    | High (novel design, hardware req.)                       | High for deep customization; low tx fees offset |
| **GitHub Stars**              | ~291                                                  | 24                                                    | ~92 (main repo)                                      |
| **Level of Decentralization** | Fully P2P orderbook, on-chain governance         | Fully on-chain, equal participant control        | Leaderless aBFT, rotating committee (>100 validators) |
| **Permissioned/Permissionless** | Permissionless                                         | Permissionless                                           | Permissionless                                        |
| **Transparency**              | Open-source, community governance              | Academic research, open prototype                | Open-source, peer-reviewed, active on-chain governance |
| **Scalability (TPS)**         | Claim 500k TPS (arch. target), 400 TPS (test)   | >200k TPS (48-core servers test)                 | ~89.6k TPS (AWS nodes test), 100k TPS (claim) |
| **Latency**                   | ~20 ms (Orderbook), 3-12s block time             | Seconds (Layer-1 batch processing)                     | Sub-second (416ms test)                          |
| **Consensus Mechanism**       | NPoS, BABE, GRANDPA                                    | HotStuff BFT                                           | AlephBFT (aBFT, PoS+DAG)                         |
| **Fault Tolerance**           | Fault-tolerant clusters, snapshot failover             | BFT consensus (HotStuff), 1/3 malicious nodes  | Asynchronous BFT (AlephBFT), 1/3 malicious nodes |
| **Cross-Chain**               | Polkadot parachain, Thea Bridge (Ethereum)      | Single-chain focus                               | MOST (Ethereum), Router, Across (14+ EVM), zParachain (Polkadot) |
| **Advantages**                | High theoretical TPS, feeless trading, open governance | Exceptional raw throughput, fully on-chain fairness | High tested TPS, sub-second finality, strong decentralization, privacy |
| **Disadvantages**             | TEE trust assumptions, development complexity, liquidity | Prototype status, high hardware requirements, limited ecosystem | Inflationary tokenomics, regulatory scrutiny for privacy, complex tech |
| **Constraints & Risks**       | Trust in TEE, unproven sustained high on-chain TPS | Costly hardware, limited community engagement    | Market adoption & inflation management, regulatory scrutiny |
| **TPS & Testing Conditions**  | 400 TPS (on-chain test), 500k TPS (TEE target)  | >200k TPS (48-core servers, prototype)           | 89.6k TPS (112 AWS nodes)                        |
| **Maturity**                  | Mainnet launched (2021), ongoing rollout               | Prototype stage, not mainnet deployed                  | Mainnet launched (2021), smart contracts live (2023) |
| **Ecosystem**                 | Active Polkadot ecosystem, growing community      | Academic/research-focused, limited community             | Vibrant, rapidly growing, diverse projects, large community |
| **Market Prospects**          | Growing, competitive niche, price growth potential     | Early stage, promising tech, niche advantage              | Strong, enterprise focus, increasing institutional interest |
| **Transaction Cost**          | Feeless order placement, small market taker fee | Not explicitly detailed, aims for economic efficiency  | ~\\(\$0.0003\\) AZERO/tx                               |

#### Optimal Choice for a High-Performance DEX Blockchain

Considering the requirement to support over 100,000 TPS for order-book-based DEXs, **Aleph Zero** emerges as the optimal choice. While Polkadex presents high theoretical TPS, its currently tested on-chain throughput is lower, and its reliance on Layer 2 TEEs introduces a specific trust assumption that might be a concern for some. SPEEDEX demonstrates impressive raw TPS in a prototype environment, but its lack of broad ecosystem adoption, mainnet deployment, and comprehensive cross-chain capabilities limit its immediate practical suitability for production-grade DEX infrastructure.

Aleph Zero strikes a strong balance between high performance, robust decentralization, and comprehensive features. Its verified ~89,600 TPS in a decentralized test environment, combined with sub-second finality, positions it very close to the 100,000 TPS target with proven technology. Furthermore, its native privacy features (ZK-proofs and sMPC) are a significant differentiator for advanced DEX use cases requiring confidentiality, which is a growing demand in the financial sector. The platform's active and well-funded ecosystem provides strong developer support and future growth potential. The extremely low transaction costs also make Aleph Zero highly attractive for high-frequency trading scenarios, ensuring cost-efficiency even at high volumes. Aleph Zero's extensive cross-chain strategy further solidifies its position by ensuring broad interoperability, crucial for liquidity and user access in a multi-chain environment.

### Official Materials

#### Polkadex
*   **Official Website**: polkadex.ee
*   **GitHub Repositories**: github.com/Polkadex-Substrate/Polkadex, github.com/Polkadex-Substrate.
*   **Documentation**: docs.polkadex.ee, github.com/Polkadex-Substrate/Documentation.
*   **Whitepapers/Technical Papers**: Information about Polkadex Whitepaper can be found via official sources.

#### SPEEDEX
*   **GitHub Repositories**: github.com/scslab/speedex.
*   **Whitepapers/Technical Papers**: "SPEEDEX: A Scalable, Parallelizable, and Economically Efficient Decentralized EXchange", available on platforms like usenix.org and semanticscholar.org.

#### Aleph Zero
*   **Official Website**: alephzero.org.
*   **GitHub Repositories**: github.com/Cardinal-Cryptography/aleph-node, github.com/alephzero/alephzero, github.com/aleph-zero-foundation.
*   **Documentation**: docs.alephzero.org, alephzero.org/developers.
*   **Whitepapers/Technical Papers**: Research papers on AlephBFT consensus, and information on Common DEX whitepaper.
*   **Official Blogs/Social**: alephzero.org/blog, twitter.com/Aleph__Zero.

Bibliography
5 Polkadot Ecosystem Tokens Below $1M Market Cap To Watch... (n.d.). https://themerkle.com/5-polkadot-ecosystem-tokens-below-1m-market-cap-to-watch-in-july-2025/

[2111.02719] SPEEDEX: A Scalable, Parallelizable, and ... - ar5iv. (n.d.). https://ar5iv.labs.arxiv.org/html/2111.02719

[2111.02719v5] SPEEDEX: A Scalable, Parallelizable, and Economically ... (n.d.). https://arxiv.org/abs/2111.02719v5

A. Akansu & Mustafa U. TorunTorun. (2015). Order Execution and Limit Order Book. https://www.semanticscholar.org/paper/762bf47db767c86f42b999849aee4749f2af53e5

A Capponi & R Jia. (3805). Liquidity provision on blockchain-based decentralized exchanges. In Available at SSRN 3805095. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4694683

A. Chepurnoy & A. Saxena. (2020). ZeroJoin: Combining ZeroCoin and CoinJoin. In IACR Cryptology ePrint Archive. https://www.semanticscholar.org/paper/94892ef19910d9d239a135c0b40604818a0634c4

A. G. Galieva & D. Palchunov. (2022). Automation of the Smart Contract Development Using Situation Models. In 2022 IEEE 23rd International Conference of Young Professionals in Electron Devices and Materials (EDM). https://www.semanticscholar.org/paper/86c35113dfe024262dfc176b64cb348a3859a160

A Garreta, A Gągol, AP Stouka, & D Straszak. (2023). COMMON: Order Book with Privacy. https://eprint.iacr.org/2023/1868

A Pradesh. (2003). India. https://search.proquest.com/openview/89db7b2330e8ef590d07c0a5325ce4f9/1?pq-origsite=gscholar&cbl=2028820

A Todorov. (2024). Creditcoin 3.0. In Testing the Creditcoin Blockchain. https://link.springer.com/chapter/10.1007/979-8-8688-0873-9_7

About Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/explore/about-aleph-zero

About SpeedX: Fast, Reliable Last-Mile Delivery Solutions. (n.d.). https://speedx.io/about-us/

Aleph Zero. (n.d.). https://docs.alephzero.org/documentation

Aleph Zero | Blazingly fast blockchain with modular ZK. (n.d.). https://alephzero.org/

Aleph Zero | New Layer 1 game changer? - Medium. (n.d.). https://medium.com/coinmonks/aleph-zero-the-new-layer-1-game-changer-4a328475c4a

Aleph Zero | Polkadot Ecosystem. (n.d.). https://polkadotecosystem.com/dapps/smart-contracts/aleph-zero/

Aleph Zero - HackMD. (n.d.). https://hackmd.io/eiAxVR_HRPyZz8aKRHWpPw

Aleph Zero: A Guide to Zero-Knowledge Public Blockchain. (n.d.). https://www.integrate.network/aleph-zero-a-guide-to-zero-knowledge-public/

Aleph Zero (AZERO) Price Prediction 2025, 2026, 2027, 2028 ... - crypto. (n.d.). https://crypto.ro/en/predictions/aleph-zero-azero-price-prediction/

Aleph Zero: Balancing Security, Scalability and Decentralization in ... (2023). https://www.binance.com/en/square/post/267220

Aleph Zero Bridges: Interoperability with Ethereum - Nextrope. (2024). https://nextrope.com/aleph-zero-bridges-interoperability-with-ethereum/

Aleph Zero Community - Aleph Zero: Public Blockchain with Private ... (2025). https://alephzero.org/community

Aleph Zero Ecosystem - Aleph Zero: Public Blockchain with Private Smart ... (n.d.). https://alephzero.org/ecosystem

Aleph Zero Ecosystem Integrations: Driving Growth with Across Protocol ... (n.d.). https://genfinity.io/2024/12/06/aleph-zero-ecosystem-integrations/

Aleph Zero: Enterprise-grade Public Blockchain, Private Smart Contracts. (2025). https://campaign.alephzero.org/intro

Aleph Zero: Examining its DAG-based Consensus Algorithm and ... - Medium. (n.d.). https://medium.com/@bitcofun/aleph-zero-examining-its-dag-based-consensus-algorithm-and-subnets-model-87d087c6ca35

Aleph Zero is a gem in the Polkadot Ecosystem!! - Medium. (2023). https://medium.com/@polkanotes/aleph-zero-is-a-gem-in-the-polkadot-ecosystem-92e5369a62da

Aleph Zero Launches Mainnet, Raises $14.8M for Platform ... - Medium. (n.d.). https://medium.com/aleph-zero-foundation/aleph-zero-launches-mainnet-raises-14-8m-for-platform-development-8c92f67b621e

Aleph Zero: Learn Everything from its Detailed Working to Unique Features. (n.d.). https://www.antiersolutions.com/blogs/demystifying-aleph-zero-working-benefits-native-currency-unique-features/

ALEPH ZERO. New blockchain system — Solution for… | by Wings Ventures ... (n.d.). https://wings-ventures.medium.com/aleph-zero-c4e80350969f

Aleph Zero Overview. (n.d.). https://assets-global.website-files.com/64f99c50f4c866dee943e165/65246741c40f9147e3e83a2a_Aleph%20Zero%201.pdf

Aleph Zero Overview - Reflexivity Research. (2022). https://www.reflexivityresearch.com/free-reports/aleph-zero-overview

Aleph Zero project details | Polkadot network | Parachains.info. (2023). https://parachains.info/details/aleph_zero

Aleph Zero Q4 Overview - reflexivityresearch.com. (2022). https://www.reflexivityresearch.com/free-reports/aleph-zero-q4-overview

Aleph Zero: Revolutionizing Blockchain with Advanced Privacy and ... (n.d.). https://cryptocatguru.com/aleph-zero-revolutionizing-blockchain-with-advanced-privacy-and-scalability/

Aleph Zero vs Polkadex [TPS, Max TPS, Block Time] | Chainspect. (n.d.). https://chainspect.app/compare/aleph-zero-vs-polkadex

Aleph Zero Wins a Parachain Slot, Connects to the Polkadot Ecosystem ... (n.d.). https://alephzero.org/blog/aleph-zero-polkadot-bridge-parachain/

Aleph Zero’s on-chain governance is getting closer. (2024). https://alephzero.org/blog/on-chain-governance-with-syncra/

AlephBFT Consensus - Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/explore/alephbft-consensus

AlephZero - GitHub. (n.d.). https://github.com/alephzero/alephzero

aleph-zero-foundation/aleph-node: Mirror of development ... - GitHub. (n.d.). https://github.com/aleph-zero-foundation/aleph-node

arXiv:2111.02719v1 [cs.DC] 4 Nov 2021. (n.d.). https://arxiv.org/pdf/2111.02719v1

Aurélien Roux. (2014). Reaching a consensus on the mechanism of dynamin? In F1000Prime Reports. https://www.semanticscholar.org/paper/b8b3c49485515a1898ed6b64be4c88bfff789979

B. Buzbee. (1993). Examples of Scalable Performance. https://www.semanticscholar.org/paper/dda81fcd2c634cc57352cfaaf6c38d2b0cbc1f52

Best Cross-Chain DEXs: Top Platforms for Multi-Network Trading. (2024). https://spayzelabs.com/best-cross-chain-dexs/

Breaking the Limits: The Power of Aleph Zero’s Layer 1 Zero ... - Medium. (n.d.). https://medium.com/@researchcoindelta/breaking-the-limits-the-power-of-aleph-zeros-layer-1-zero-knowledge-proof-system-e4dad99cc9c9

Byungil Kim & Junghee Lee. (2025). Automated Orderbook for Decentralized On-Chain Environment. In KIISE Transactions on Computing Practices. https://www.semanticscholar.org/paper/1d14b1163cb0cdb31166026a2c49f8286c61132e

Cardinal-Cryptography/aleph-node - GitHub. (2021). https://github.com/Cardinal-Cryptography/aleph-node

Chen-Liang Fang, Deron Liang, Fengyi Lin, & Chien-Cheng Lin. (2007). Fault tolerant Web Services. In J. Syst. Archit. https://www.semanticscholar.org/paper/1d063c0b18bd7c8e50271c46a8ac3bddd639f4d1

Common AMM launches on Aleph Zero: The First Step ... - CryptoPotato. (n.d.). https://chainwire.org/2024/05/21/common-amm-launches-on-aleph-zero-the-first-step-towards-releasing-the-ultimate-zk-defi-suite/

Common Whitepaper - Differences - Aleph Zero. (n.d.). https://docs.alephzero.org/aleph-zero/protocol-details/common-dex/common-whitepaper-differences

Community - Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/explore/community

Community - Aleph Zero: Public Blockchain with Private Smart ... (n.d.). https://alephzero.org/events/category/community

Contains tutorials and documentation on how to use Polkadex - GitHub. (n.d.). https://github.com/Polkadex-Substrate/Documentation

D. Bauso, L. Giarré, & R. Pesenti. (2006). Mechanism Design for Optimal Consensus Problems. In Proceedings of the 45th IEEE Conference on Decision and Control. https://www.semanticscholar.org/paper/450390189b6da39659b4d115d1b87cc6522bbc34

D Coleman & R Rowthorn. (2011). Who’s afraid of population decline? A critical examination of its consequences. In PoPulation and develoPment review. https://www.jstor.org/stable/41762406

Danny Lo & A. Hall. (2015). Resiliency of the limit order book. In Journal of Economic Dynamics and Control. https://www.semanticscholar.org/paper/0d3db09296b6ee9d4a4b83a1b5e39b2a2b4673cc

Deutsche Telekom to validate the privacy-enhanced Aleph Zero ... (2023). https://www.telecomtv.com/content/digital-platforms-services/deutsche-telekom-to-validate-the-privacy-enhanced-aleph-zero-blockchain-48882/

Dev Portal - Aleph Zero. (n.d.). https://alephzero.org/developers

DS Kurian, VM Pillai, & J Gautham. (2023). Data-driven imitation learning-based approach for order size determination in supply chains. https://www.inderscienceonline.com/doi/abs/10.1504/EJIE.2023.130601

E. Stacchetti. (1985). Analysis of a dynamic, decentralized exchange economy☆. In Journal of Mathematical Economics. https://www.semanticscholar.org/paper/8b21a11056078eaa4d2d205a02af135ff78bb001

F. Santana, S. Arévalo, A. Alvarez, & Javier Miranda. (1993). A quick distributed consensus protocol. In Microprocess. Microprogramming. https://www.semanticscholar.org/paper/65a8e43db2341edf687b63c3d68a025568d10f38

FAQ | Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/faq

Fault tolerance - Wikipedia. (n.d.). https://en.wikipedia.org/wiki/Fault_tolerance

Fault Tolerance Explored. Navigating Systems Resilience, Security ... (2024). https://www.zenarmor.com/docs/network-security-tutorials/what-is-fault-tolerance

Fundamentals: Aleph Zero and its DAG Implementation - Medium. (n.d.). https://medium.com/aleph-zero-foundation/fundamentals-aleph-zero-and-its-dag-implementation-a8f99afe965

Further Decentralization Rolls Out on Aleph Zero! (2024). https://alephzero.org/blog/further-decentralization-rolls-out-on-aleph-zero/

G. Gilbert, M. Hamrick, Y. Weinstein, V. Aggarwal, & A. Calderbank. (2008). Operator Quantum Fault Tolerance. https://www.semanticscholar.org/paper/dd8827a8148bf2997610439a6de13bba4b93aa5c

G Ramseyer, A Goel, & D Mazières. (n.d.). SPEEDEX: A Scalable, Parallelizable, and Economically Efficient Distributed EXchange. https://ccfi.scs.stanford.edu/~geoff/papers/speedex.pdf

G Ramseyer, A Goel, & D Mazières. (2023). {SPEEDEX}: A Scalable, Parallelizable, and Economically Efficient Decentralized {EXchange}. https://www.usenix.org/conference/nsdi23/presentation/ramseyer

G.C. Polyzos. (2022). Smart Contracts for Decentralized Dynamic Spectrum Marketplaces. In International Journal of Wireless Information Networks. https://www.semanticscholar.org/paper/b3a2ca74db1479575f3eb723d8f30b11c3027f66

Geoffrey Ramseyer, Ashish Goel, & David Mazières. (2021a). SPEEDEX: A Scalable, Parallelizable, and Economically Efﬁcient Distributed EXchange. https://www.semanticscholar.org/paper/1d112fe9a859a3d71b9bf06b239404beef9fb957

Geoffrey Ramseyer, Ashish Goel, & David Mazières. (2021b). SPEEDEX: A Scalable, Parallelizable, and Economically Efficient Decentralized EXchange. In Symposium on Networked Systems Design and Implementation. https://www.semanticscholar.org/paper/7973956c43dcd7feb6a8d55f4c68cf04f9dcf6db

GitHub Search API: Get the number of stars for a repository. (n.d.). https://gist.github.com/jasonrudolph/6057563

“GitHub Stars” is a very useful metric. But for *what. (2017). https://opensource.stackexchange.com/questions/5110/github-stars-is-a-very-useful-metric-but-for-what

Günther Blaschek. (1994). The Programming Language Omega. https://www.semanticscholar.org/paper/2ee5fcd4d5d6fd5a4ef4f269ca9fae11db3697d5

Hello, Polkadex:). Polkadex is a cross-chain… | by Alfatestnods | Medium. (n.d.). https://medium.com/@alfatestnods/hello-polkadex-bba1a5135001

Hongyuan Xu, Yuan‐Hua Ni, Zhongxin Liu, & Zengqiang Chen. (2020). Privacy-Preserving Leader-Following Consensus via Node-Augment Mechanism. In IEEE Transactions on Circuits and Systems II: Express Briefs. https://www.semanticscholar.org/paper/8c2427437c1a8113f10084758085939e131ae77f

How is Aleph Zero Leading the Charge in Blockchain Cross-Chain ... (n.d.). https://www.onesafe.io/blog/aleph-zero-cross-chain-innovations

How to engage with Polkadex Community | Polkadex Docs. (n.d.). https://docs.polkadex.ee/polkadexCommunity/

ink! begins new journey with R0GUE, Aleph Zero and Scio Labs. (2024). https://www.parity.io/blog/ink-new-journey

Interoperability in Blockchain: Exploring Polkadot’s Cross-Chain ... (n.d.). https://www.linkedin.com/pulse/interoperability-blockchain-exploring-polkadots-umesh-dhasmana

Introducing Polkadex Orderbook: A Revolution in Decentralized ... - Medium. (2023). https://medium.com/@dekachi17/introducing-polkadex-orderbook-a-revolution-in-decentralized-trading-b4fd138a4d8f

Introduction - Aleph Zero - coq-of-rust and coq-of-solidity. (2024). https://formal.land/reports/aleph-zero/book/

J. Bezos. (2006). Mem. A multilingual package for LTEX with Aleph. https://www.semanticscholar.org/paper/4dc23383707838794dc5ef7dd3e6b4d3d9bc0d83

Lili Cheng, Zhiying Lv, Osama Alfarraj, Amr Tolba, X. Yu, & Yongjun Ren. (2024). Secure cross-chain interaction solution in multi-blockchain environment. In Heliyon. https://www.semanticscholar.org/paper/83e147348f9a55469893f9ca8d45cfd710126a5b

Lingwei Wei. (2004). Aleph and Aleph Act. https://www.semanticscholar.org/paper/768d04158205ad72719c17cccc4129482309a1ad

M. Krebs, H. Reichardt, Reiner Sojka, & P. Stevens. (2021). Applications and markets. In Electrochemical Power Sources: Fundamentals, Systems, and Applications. https://www.semanticscholar.org/paper/5e9ec13585bcefe56ab2cf9df014d4ddc321a2fd

M Moosavi & J Clark. (2022). Lissy: Experimenting with on-chain order books. https://link.springer.com/chapter/10.1007/978-3-031-32415-4_36

Mark Moir. (1997). Transparent Support for Wait-Free Transactions. In International Workshop on Distributed Algorithms. https://www.semanticscholar.org/paper/d05a9e25f42380b6d731e5b5f41f13925ceb2aea

Michele Ciampi, M. Ishaq, M. Magdon-Ismail, R. Ostrovsky, & Vassilis Zikas. (2021). FairMM: A Fast and Frontrunning-Resistant Crypto Market-Maker. In IACR Cryptology ePrint Archive. https://www.semanticscholar.org/paper/d6bc1a8986b0dcd24d9ffe68142f6e15a64f2961

P Greitbauer. (2023). Exploring interoperability and scalability in dag-based distributed ledger technologies: A case study of relay implementation. https://repositum.tuwien.at/handle/20.500.12708/189441

Papers with Code - SPEEDEX: A Scalable, Parallelizable, and ... (n.d.). https://cs.paperswithcode.com/paper/speedex-a-scalable-parallelizable-and

[PDF] Aleph Zero Overview. (n.d.). https://cdn.prod.website-files.com/64f99c50f4c866dee943e165/65246741c40f9147e3e83a2a_Aleph%20Zero%201.pdf

[PDF] SPEEDEX: A Scalable, Parallelizable, and Economically Efficient ... (2021). https://www.scs.stanford.edu/~geoff/papers/speedex.pdf

Polkadex - GitHub. (n.d.). https://github.com/polkadex-substrate

Polkadex - RadiumBlock. (2024). https://www.radiumblock.com/polkadex.html

Polkadex is Launching the First Cross-Chain Orderbook ... - HackerNoon. (n.d.). https://hackernoon.com/polkadex-is-launching-the-first-cross-chain-orderbook-based-dex-with-the-release-of-thea

POLKADEX ORDERBOOK - pontem.network. (n.d.). https://pontem.network/posts/polkadex-orderbook

Polkadex Orderbook Crypto Currency Exchange. (n.d.). https://polkadex.ee/orderbook

Polkadex Orderbook is live. (n.d.). https://polkadex.medium.com/polkadex-orderbook-is-live-92749206d465

Polkadex Orderbook Security Audit: A Case Study - Hacken. (n.d.). https://hacken.io/case-studies/polkadex-audit/

Polkadex (PDEX) Price, Investors & Funding, Charts, Market Cap | Chain ... (2021). https://chainbroker.io/projects/polkadex/

Polkadex project details | Polkadot network - Parachains.info. (n.d.). https://parachains.info/details/polkadex

Polkadex Review: A Substrate-based Decentralized Exchange with a ... (2020). https://www.publish0x.com/analysis-from-moon/polkadex-review-a-substrate-based-decentralized-exchange-wit-xwnxqyr

Polkadex Testnet Phases Timeline - Medium. (n.d.). https://medium.com/polkadex/polkadex-testnet-phases-timeline-39404571a931

Polkadex [TPS, Max TPS, Block Time & TTF] | Chainspect. (n.d.). https://chainspect.app/chain/polkadex

Polkadex-Substrate/Polkadex: An Orderbook-based Decentralized ... (2020). https://github.com/Polkadex-Substrate/Polkadex

Polkadot’s Consensus Protocols - Polkadot Wiki. (n.d.). https://wiki.polkadot.network/learn/learn-consensus/

Polkassembly. (n.d.). https://polkassembly.io/

Polkassembly · Polkassembly. (2025). https://docs.polkassembly.io/

Put a “Spotlight” on Polkadex — The Trading Engine for ... - KuCoin. (n.d.). https://www.kucoin.com/blog/put-a-spotlight-on-polkadex

R. Schraft & Hansjörg Volz. (1996). Marktpotential und Nutzwert. https://www.semanticscholar.org/paper/239d012c69190191f4817f42126094493b2ddb05

R. Stewart. (1970). How Much Decentralization. https://www.semanticscholar.org/paper/f47362319155173dd2d8b9842027c6a0b810336f

RD Neumann & L Webster. (1991). The wind tunnel test’system’of 1995; cost effective experimentation through a fusion of related technologies. https://ieeexplore.ieee.org/abstract/document/186259/

Rust: Why Does Aleph Zero Use It? Podcast Key Takeaways. (2023). https://medium.com/aleph-zero-foundation/rust-why-does-aleph-zero-use-it-podcast-key-takeaways-9ecafcb620d3

S. Jacka, A. Berkaoui, & J. Warren. (2006). No arbitrage and closure results for trading cones with transaction costs. In Finance and Stochastics. https://www.semanticscholar.org/paper/5867fc0bbeec32a5dd517e6ac3ebbebb7a047053

S Ojog. (2021). The emerging world of decentralized finance. In Informatica Economica. https://revistaie.ase.ro/content/100/05%20-%20ojog.pdf

scslab/speedex - GitHub. (n.d.). https://github.com/scslab/speedex

SECURITY ANALYSIS POLKADEX ORDERBOOK - wp.hacken.io. (n.d.). https://wp.hacken.io/wp-content/uploads/2023/10/L1-audit-Polkadex-Orderbook-final-report_04082023.pdf

Simply Explained: Aleph Zero (AZERO) - Cryptonary. (n.d.). https://cryptonary.com/cryptoschool/simply-explained-aleph-zero-azero/

Sinopec Shengli. (2003). Seismic acquisition technology of bin stack. https://www.semanticscholar.org/paper/0b48720513ab4814718cf012b2060cd30893e7ff

Smart Contracts | Polkadot Developer Docs. (n.d.). https://docs.polkadot.com/develop/smart-contracts/

Smart Contracts - Polkadot Wiki. (n.d.). https://wiki.polkadot.network/learn/learn-smart-contracts/

Smart contracts are live on the mainnet. - Aleph Zero. (2023). https://alephzero.org/blog/smart-contracts-live-on-mainnet/

Smart Contracts Now Live on Aleph Zero Mainnet: A Major Milestone for ... (n.d.). https://en.btc-pulse.com/smart-contracts-now-live-on-aleph-zero-mainnet-a-major-milestone-for-the-ecosystem/

SPEEDEX: A Scalable, Parallelizable, and Economically Efﬁcient ... (n.d.). https://www.scs.stanford.edu/~geoff/papers/speedex-2022.pdf

SPEEDEX: A Scalable, Parallelizable, and Economically Efficient ... (n.d.). https://www.usenix.org/system/files/nsdi23-ramseyer.pdf

Speedex SPDX whitepapers - whitepaper.io. (n.d.). https://www.whitepaper.io/coin/speedex

Stellar | Building SPEEDEX – A Novel Design for a Scalable ... (n.d.). https://stellar.org/blog/developers/building-speedex-a-novel-design-for-decentralized-exchanges

Suren Machiraju & S. Gaurav. (2018). Key Application Experiences: Latency, Scalability, and Throughput. In Hardening Azure Applications. https://www.semanticscholar.org/paper/eb5ff2581a827c90cb3520cadeddbe0e3eaaa8ed

SX Wang. (2024). Meat the Future: The Patent Landscape of Cultivated Meat. https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/lndslid16&section=42

The Fastest Blockchain Networks of 2023 | by Ubik Capital - Medium. (2023). https://ubikcapital.medium.com/the-fastest-blockchain-networks-of-2023-469d43079192

The New Aleph Zero Roadmap - Aleph Zero Blog. (n.d.). https://alephzero.org/blog/the-new-aleph-zero-roadmap/

The New Aleph Zero Roadmap - X. (2025). https://x.com/Aleph__Zero/status/1940100876879700411

The proof of concept code for the Aleph Zero Protocol. - GitHub. (n.d.). https://github.com/aleph-zero-foundation/Proof-of-Concept

Thomas S. Kim. (2017). On the transaction cost of Bitcoin. In Finance Research Letters. https://www.semanticscholar.org/paper/90e2774478d7e4a037526f8b0172d4e0e2ec37a5

Top Polkadot Projects 2025: 7 Best DOT DApps Shaping Web3! (n.d.). https://coinbureau.com/analysis/top-polkadot-projects/

Understanding Polkadex: A Trading Engine for Web3 and DeFi. (n.d.). https://academy.moralis.io/blog/understanding-polkadex-a-trading-engine-for-web3-and-defi

Understanding Polkadex: Polkadex 101 - Medium. (2021). https://medium.com/polkadex/understanding-polkadex-polkadex-101-97f8957bae88

Unlocking Seamless Interoperability: An In-depth Look at Across ... (n.d.). https://www.publish0x.com/an-in-depth-look-at-across-protocol-by-ch04niverse/unlocking-seamless-interoperability-an-in-depth-look-at-acro-xlgrvjp

V Gramlich, M Principato, & B Schellinger. (2022). Decentralized finance (DeFi): Foundations, applications, potentials, and challenges. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4535868

W. Streeter. (1984). Other Market Segments. https://www.semanticscholar.org/paper/0c96840676f4a2710dbffe341865802c68e93c4e

WASM for Future-Proof Smart Contracts | Aleph Zero. (2023). https://alephzero.org/blog/fundamentals-wasm-evm-aleph-zero-explores-new-frontier/

What is Aleph Zero? - Coinbold. (n.d.). https://coinbold.io/what-is-aleph-zero/

What is Aleph Zero? - Messari. (n.d.). https://messari.io/project/aleph-zero/profile

What is Aleph Zero? All You Need to Know About AZERO - Gate.com. (2023). https://www.gate.com/learn/articles/what-is-aleph-zero/836

What is Aleph Zero: The Advanced ZK Modular Blockchain ... (2024). https://web3.bitget.com/en/academy/what-is-aleph-zero

What is Aleph Zero, the Complete Blockchain Guide - DappRadar. (2024). https://dappradar.com/blog/what-is-aleph-zero-the-complete-blockchain-guide

What is Aleph-Zero? Key Insights - Nextrope. (2024). https://nextrope.com/what-is-aleph-zero-key-insights/

What is blockchain interoperability? A guide to cross-chain solutions ... (n.d.). https://www.moonpay.com/en-ca/learn/blockchain/blockchain-interoperability

What is Polkadex? | Polkadex Docs. (2021). https://docs.polkadex.ee/whatispolkadex/

What Is Polkadex? - CoinMarketCap. (n.d.). https://coinmarketcap.com/academy/article/what-is-polkadex

What is Polkadex? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/polkadex

What is the significance of the number of stars of a github repository? (2016). https://stackoverflow.com/questions/36465756/what-is-the-significance-of-the-number-of-stars-of-a-github-repository

X Hu, X Chen, Z Dong, Y Sun, & Y Guo. (2025). Optimized Cross-Chain Transactions With Aggregated Zero-Knowledge Proofs: Enhancing Efficiency and Security. https://ieeexplore.ieee.org/abstract/document/10829823/

Yonatan Sompolinsky, Yoad Lewenberg, & Aviv Zohar. (2017). SPECTRE : Serialization of Proof-of-work Events : Confirming Transactions via Recursive Elections. https://www.semanticscholar.org/paper/65f1613a4f1b015fc64608b787227de0549f4cec

Zhou Xia. (2007). Fault Tolerance Immune System. In Turbine Technology. https://www.semanticscholar.org/paper/00471ba97b7d45aa0d5dd8fb5d009bfc2f45724b



Generated by Liner
https://getliner.com/search/s/5926611/t/86446099