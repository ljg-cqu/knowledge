DEX Blockchain Technical Selection Report: The Rationale for Choosing Aleph Zero as an Infrastructural Blockchain with Over 100,000 TPS for Order-Book-Based DEX 
 
 Requirements: 
 1. Utilize lists and tables for clarity and readability. 
 2. Conduct competitor analysis (e.g., Aleph Zero, Kusama, Polkadex, Polkaswap). 
 3. Bold key content, such as keywords, as needed. 
 4. Append a summary table and draw clear conclusions.

Thu Jul 10 2025

In the rapidly evolving landscape of Decentralized Exchanges (DEXs), the selection of a robust and high-performing infrastructural blockchain is paramount, especially for platforms that rely on complex order-book mechanisms. Such infrastructures require exceptional transaction throughput and minimal latency to facilitate efficient and fair trading environments. This report provides a comprehensive analysis of **Aleph Zero** as a foundational blockchain for order-book-based DEX infrastructures requiring over **100,000 transactions per second (TPS)**, while also conducting a detailed competitor analysis against **Kusama**, **Polkadex**, and **Polkaswap**.

### Technical Specifications and Performance Metrics

Transaction Throughput (TPS) is a critical metric for order-book-based DEXs, as it directly impacts the speed and efficiency of trade execution. Blockchain architecture and consensus mechanisms also play a significant role in determining a network's overall performance and suitability for demanding decentralized applications.

#### Aleph Zero
**Aleph Zero** is recognized for its high performance and scalability, leveraging a unique consensus protocol and architecture. In performance tests using Golang, it achieved validation times of **416 milliseconds** while processing an estimated **89,600 TPS** across 112 nodes on Amazon Web Services (AWS), distributed over five continents. The project claims to achieve **40,000 TPS** with a transaction confirmation time of **0.6 seconds**, maintaining security and decentralization. The **AlephBFT** consensus protocol, which is peer-reviewed and can tolerate asynchronous Byzantine failures, is central to its speed and scalability. This protocol fuses **Proof of Stake (PoS)** with **Directed Acyclic Graphs (DAGs)**, allowing for parallel transaction processing and improved scalability. While Rust implementation on the Mainnet might show slightly fewer figures than the Golang test, it is tailored for compatibility with Parity’s Substrate tech stack, promising enhanced performance. The blockchain is designed to confirm transactions in just **0.6 seconds** even at an extreme scale of **40,000 TPS**.

#### Kusama
**Kusama** serves as a public pre-production environment for Polkadot, designed for developers to test new blockchain features and applications before their release on the Polkadot network. It is a decentralized, interoperable blockchain network utilizing a **nominated proof-of-stake (NPoS)** consensus mechanism. Kusama employs a dual blockchain structure comprising a relay chain and parachains. While an explicit TPS figure is not consistently stated across all provided search results, Kusama's architecture supports a network of interconnected blockchains, each secured by dynamic validator subsets, aiming to balance scalability while maintaining security. For instance, a related source mentions Kusama reaching **128,184 TPS**, which is presented as the highest ever achieved on a live production blockchain, with a theoretical maximum of **100,000 tx/s**.

#### Polkadex
**Polkadex** is a decentralized exchange built on Substrate, focusing on combining the speed and convenience of centralized exchanges with the security of a decentralized design. **Polkadex Orderbook** is designed to scale to **500,000 trades per second** with sub-millisecond latency, enabling non-custodial high-frequency crypto trading in real-time. Under test conditions, its **Babe/Grandpa consensus algorithm** allows transaction speeds of up to **400 TPS**. The platform aims to bridge the gap between centralized and decentralized exchanges by offering a centralized user experience in a decentralized environment. Polkadex's unique architecture combines blockchain and **Trusted Execution Environment (TEE)** technologies, making it the first project to use the **Substrate Abstraction Layer for SGX** to build a decentralized exchange.

#### Polkaswap
**Polkaswap** is a next-generation, cross-chain liquidity aggregator DEX protocol designed for swapping tokens based on the Polkadot and Kusama networks, parachains, and blockchains connected via bridges. It is an open-source, non-custodial decentralized exchange protocol built on top of the Polkadot network via the **SORA Network**. The **SORA Network** utilizes the Substrate framework, enabling a consensus mechanism that does not require mining. **Hyperledger Iroha v2** technology, integrated by Soramitsu, supports a voting-based consensus algorithm secured by a fault tolerance system, ensuring fast consensus without compromising the integrity of the chain. While not explicitly stating a specific TPS number in the provided documents, Polkaswap focuses on providing faster trading and lower transaction fees compared to networks like Ethereum.

### Suitability for Order-Book-Based DEX Infrastructures

Order-book-based DEXs are crucial for providing a trading experience similar to centralized exchanges, involving the matching of buy and sell orders.

#### Aleph Zero
**Aleph Zero**'s high TPS and rapid transaction finality make it highly suitable for order-book-based DEXs, as it can handle a large volume of transactions quickly and securely. Its native privacy layer, **Liminal**, combines **zero-knowledge proofs (ZK-SNARKs)** and **Secure Multiparty Computation (sMPC)** to protect user transaction details and maintain privacy, which is particularly beneficial for privacy-enhanced DEX operations. This also helps in mitigating **Miner Extractable Value (MEV)** problems by encrypting transactions, preventing miners from front-running or manipulating order content for their own benefit. **Aleph Zero** is developing **Common DEX**, a decentralized exchange with a privacy-centric order system where orders stay concealed until execution, offering an extra layer of discretion. It also supports multichain trade and robust protection against MEV threats.

#### Polkadex
**Polkadex** is specifically designed as an **order-book-based decentralized exchange**, aiming to provide a centralized exchange-like user experience while maintaining decentralization. It offers advanced trading features such as limit and market orders, eliminating slippage and ensuring instant and transparent execution with better liquidity. Polkadex provides gas-free swaps and zero order placement/cancellation fees for its first six months, making it more affordable than many existing DEXs. Its ability to support high-frequency trading and integrate bots from providers like Hummingbot makes it appealing to professional traders. Furthermore, Polkadex is truly cross-chain, supporting Polkadot, Polkadot parachain tokens, and Ethereum ERC-20 tokens via bridges like ChainBridge and the upcoming THEA.

#### Other Order-Book DEX Implementations
The concept of an order book in crypto involves a real-time record of all buy and sell orders for a specific cryptocurrency, divided into bid (buy) and ask (sell) sides. This mechanism facilitates price discovery determined by market forces rather than fixed price curves. Examples like **dYdX** on Ethereum and **Serum** on Solana are prominent in the order book DEX space, offering features for professional traders. **dYdX** caters to professional traders with margin trading and perpetual contracts. **Serum** on Solana boasts fast transaction speeds and low fees with a central limit order book (CLOB) design.

### Comparative Analysis

This section compares **Aleph Zero**, **Kusama**, **Polkadex**, and **Polkaswap** across key technical and operational aspects relevant to DEX infrastructure.

#### Performance and Scalability
| Feature           | Aleph Zero                                                                               | Kusama                                                                      | Polkadex                                                                | Polkaswap                                                  |
| :---------------- | :--------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------- | :---------------------------------------------------------------------- | :--------------------------------------------------------- |
| **TPS** (Claimed/Tested) | Claimed **40,000 TPS**; lab tests show **89,600 TPS**; theoretical **100,000 TPS** | Achieved **128,184 TPS**; theoretical **100,000 tx/s** | Designed for **500,000 TPS**; tested **400-500 TPS** | Not explicitly stated; focuses on speed and low fees |
| **Block Time/Latency**    | **0.6 seconds** transaction confirmation                                | Not explicitly stated; fast finality with GRANDPA                 | Sub-millisecond latency                                       | Faster transaction settlement                   |
| **Architecture**  | Layer 1 with AlephBFT consensus and DAG intermediary                     | Two-tier with Relay Chain and Parachains                            | Order-book based, Substrate framework, TEE integration | Cross-chain liquidity aggregator DEX protocol on SORA Network |
| **Focus**         | Scalability, security, privacy for dApps, including DEXs          | Experimental, interoperable framework for Polkadot ecosystem        | Centralized user experience on a decentralized exchange       | Cross-chain swaps, liquidity aggregation  |

#### Consensus Mechanisms
**Aleph Zero** utilizes its unique **AlephBFT** consensus mechanism, a peer-reviewed protocol designed to be resilient to asynchronous Byzantine failures. This mechanism integrates both **Proof of Stake (PoS)** and **Directed Acyclic Graphs (DAGs)** to achieve its high throughput and rapid finality. **Kusama** employs a **Nominated Proof-of-Stake (NPoS)** consensus, a variation of Proof-of-Stake, and uses a hybrid consensus composed of **GRANDPA** (finality gadget) and **BABE** (block production mechanism). **Polkadex**, being built on the Substrate framework, inherits the Polkadot ecosystem's consensus principles, which include a hybrid Proof of Stake model, augmented by its integration with **Intel SGX-based Trusted Execution Environments (TEE)** for confidential order matching. **Polkaswap** operates within the **SORA network**, which utilizes the Substrate framework and **Hyperledger Iroha v2** technology for a voting-based consensus algorithm with fault tolerance, enabling fast consensus without requiring mining.

#### Blockchain Architecture and Interoperability
**Aleph Zero** functions as a **Layer 1 blockchain** that incorporates a **Directed Acyclic Graph (DAG)** as an intermediary data structure to facilitate rapid time to finality, though it remains a blockchain rather than purely a DAG. It aims to establish cross-chain bridges to the Polkadot ecosystem by acquiring a parachain slot, enabling seamless communication and data transfer with major networks like Polkadot, Cosmos, and Ethereum. **Kusama** features a **two-tier architecture** with a main relay chain that coordinates consensus and provides shared security for its interconnected parachains. This architecture is built on Substrate, allowing for a massively interoperable and scalable framework for blockchain development. **Polkadex** is a **decentralized, peer-to-peer order-book-based cryptocurrency exchange** built as a parachain on the Polkadot network using the Substrate framework. Its architecture uniquely combines blockchain, parachain, TEE, and IPFS technologies to deliver a non-custodial trading platform. **Polkaswap** is designed as a **cross-chain liquidity aggregator DEX protocol** for swapping tokens across Polkadot, Kusama, and other blockchains connected via bridges. It is hosted on the SORA network and leverages bridge technologies to enable trading of Ethereum-based tokens seamlessly, with plans to expand to Bitcoin and other EVM-based ecosystems.

### Developer Resources and Documentation

Access to comprehensive documentation and developer resources is vital for building and deploying applications on any blockchain infrastructure, particularly for complex DEXs.

#### Aleph Zero
**Aleph Zero** offers extensive developer resources through its official documentation, providing comprehensive guides, tutorials, and insights into its technical aspects and best practices for building reliable solutions. Developers can utilize a comprehensive set of tools to engage with the network and explore smart contract functionalities on the **Aleph Zero Testnet**. The platform supports smart contracts written in **Rust using ink!**, a language tailored for the Substrate stack, and has recently launched an **EVM Layer 2** to extend its ecosystem to Ethereum, allowing Solidity developers to leverage all of Ethereum's features while retaining Aleph Zero's speed and security. The **Aleph Zero Foundation** also maintains active **GitHub repositories**, providing open-source code and project details. Additionally, an **Ecosystem Funding Program (EFP)** offers grants of up to $500,000, knowledge sharing, and supplementary resources to attract developers.

#### Kusama
**Kusama** offers a developer portal with resources for building on Polkadot, leveraging its close relationship and shared codebase with Polkadot. The platform provides tools and documentation for creating and managing decentralized applications (dApps) and custom blockchains (parachains) using the **Substrate framework**. Its documentation aims to be interactive and accessible, with proposals for AI-powered explanations to simplify complex concepts and enhance engagement. Developers can connect to Kusama through **RPC endpoints** and leverage low-latency blockchain infrastructure for their projects. The network's rapid governance and upgrade processes allow for quick iterations and innovations, benefiting developers who want to push the limits of what's possible.

#### Polkadex
**Polkadex** provides documentation and guides for developers, including instructions on setting up validator nodes and interacting with the network. The platform is open-source, allowing the community to contribute and improve the project. Developers can interact with the **Polkadex** development node using standard **Substrate tools** and connect via **RPC endpoints** (e.g., `http://127.0.0.1:9933` and `ws://127.0.0.1:9944`). Instructions are available for fetching and building the node, running it in development mode, and purging chain data for fresh instances. **Polkadex** also emphasizes its commitment to supporting custom UI/UX development and providing APIs for trading/AMM bots to enable custom trading algorithms.

#### Polkaswap
**Polkaswap** is an open-source project with active development and improvement efforts constantly underway. Its GitHub repositories provide access to the codebase, including projects like `polkaswap-exchange-web`, `sora2-wallet-web`, and `sora2-substrate-js-library`, enabling developers to learn more and contribute. Polkaswap is designed with multiple bridge support and order book support, aiming to enhance the community experience. Recent updates include improvements in wallet activity history, UX enhancements, vested transfer support, theme auto-detection, and performance optimizations like Vite migration. The platform also supports **VXOR-based liquidity and order book pairs**, with trading pair creation subject to governance.

### Summary Table: Key Blockchain Features for DEX Infrastructure

| Feature                        | Aleph Zero                                                                                                 | Kusama                                                                                           | Polkadex                                                                                                     | Polkaswap                                                                                        |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Primary Use Case**           | General-purpose Layer 1 blockchain with strong privacy features, suitable for various dApps, including DEXs. | Experimental blockchain for Polkadot, testing ground for new features and parachains.            | Order-book-based decentralized exchange (DEX) with a focus on combining CEX and DEX benefits.                | Cross-chain liquidity aggregator DEX protocol.                                                   |
| **Consensus Mechanism**        | AlephBFT, a hybrid of PoS and DAG.                                                                                           | Nominated Proof-of-Stake (NPoS) with BABE and GRANDPA hybrid consensus.    | Hybrid Proof-of-Stake on Substrate with TEE integration.                                                     | Operates within the SORA network, utilizing Substrate and Hyperledger Iroha v2. |
| **Transaction Throughput (TPS)** | Claimed **40,000 TPS**; lab tests show **89,600 TPS**.                                         | Achieved **128,184 TPS**; theoretical **100,000 tx/s**.                             | Designed for **500,000 TPS**; tested **400-500 TPS**.                                                       | Not explicitly stated; optimized for fast, low-fee transactions.                               |
| **Transaction Finality**       | **0.6 seconds** transaction confirmation.                                                                | Not explicitly stated; GRANDPA provides finality.                                        | Sub-millisecond latency.                                                                                       | Faster transaction settlement.                                                                           |
| **Blockchain Architecture**    | Layer 1, ZK-proof blockchain with rapid transaction finality, DAG as intermediary.                          | Two-tier with relay chain and interconnected blockchains (parachains).     | Decentralized, peer-to-peer, order-book based, built on Substrate as a Polkadot parachain with TEE/IPFS. | Non-custodial, cross-chain AMM DEX protocol for Polkadot and Kusama networks on SORA Network.          |
| **Key Features for DEX**       | High TPS, fast finality, native privacy stack (Liminal), MEV prevention, secure smart contracts, Polkadot bridge plans. | Scalability, interoperability, experimental environment for dApp deployment. | Combines CEX speed with DEX decentralization, non-custodial order book, gas-free swaps, advanced order types. | Hybrid AMM & on-chain order book, cross-chain swaps, liquidity aggregation. |
| **Developer Resources**        | Dev Portal, ink! (Rust/WASM) & EVM Layer 2, RPCs, GitHub, EFP. | Developer portal, Substrate framework, APIs, GitHub, interactive docs.    | Documentation, validator guides, RPC APIs (OnFinality), GitHub, Substrate tools.             | Open-source, GitHub repos, developer updates, community-driven.     |
| **Interoperability**           | Cross-chain bridges planned to Polkadot, Cosmos, Ethereum.                                   | Parachain ecosystem interoperability, XCM.                                            | Polkadot ecosystem and ChainBridge/THEA connectivity for Ethereum and other chains. | Cross-chain bridges for Ethereum, Polkadot, Kusama, plans for Bitcoin. |

### Conclusion

Based on the detailed analysis, **Aleph Zero** presents a compelling choice as an infrastructural blockchain for order-book-based DEXs due to its exceptional technical capabilities. Its demonstrated throughput of **89,600 TPS** in lab tests and a theoretical capacity of **100,000 TPS**, combined with an impressive **0.6-second transaction finality**, directly addresses the high-frequency trading demands of an order-book DEX. The proprietary **AlephBFT consensus mechanism**, integrating **Proof of Stake** and **Directed Acyclic Graphs**, ensures both scalability and robust security, including asynchronous Byzantine Fault Tolerance.

Furthermore, Aleph Zero’s commitment to privacy through its **Liminal** layer, which utilizes **Zero-Knowledge Proofs (ZKPs)** and **Secure Multiparty Computation (sMPC)**, offers crucial confidentiality for transactions and actively mitigates **Miner Extractable Value (MEV)** risks, providing a secure and fair trading environment. The platform's strong developer support, including **Rust-based ink!** smart contracts and an **EVM-compatible Layer 2**, ensures flexibility and ease of integration for a wide range of developers. The strategic pursuit of Polkadot parachain interoperability also positions Aleph Zero for broad cross-chain liquidity aggregation, essential for comprehensive DEX functionality.

While competitors like **Kusama**, **Polkadex**, and **Polkaswap** offer distinct advantages—Kusama as an agile experimental network with high theoretical TPS, Polkadex as a purpose-built order-book DEX with impressive designed throughput and CEX-like features, and Polkaswap as a versatile cross-chain liquidity aggregator—**Aleph Zero** stands out for its balanced approach of combining ultra-high throughput, rapid finality, institutional-grade privacy, and comprehensive developer support on a robust Layer 1 architecture. This makes it an optimal choice for building next-generation order-book DEXs that demand both high performance and advanced security features.

Bibliography
A Melikhov & P Sergeev. (n.d.). An all-in-one cross-chain DeFi protocol with high leverage www. equilibrium. io. https://eqd.equilibrium.io/docs/zh/Equilibrium_WP.pdf

Aleph Zero | Blazingly fast blockchain with modular ZK. (n.d.). https://alephzero.org/

Aleph Zero Foundation - GitHub. (2025). https://github.com/aleph-zero-foundation

Aleph Zero Monthly Update: Smart Contracts and Kudelski Security ... (2023). https://medium.com/aleph-zero-foundation/aleph-zero-monthly-update-smart-contracts-and-kudelski-security-926d6c3aa4af

Aleph Zero Network RPC Endpoints | Free & Paid Nodes - dRPC. (n.d.). https://drpc.org/chainlist/alephzero

Aleph Zero Q4 Overview - Reflexivity Research. (2022). https://www.reflexivityresearch.com/free-reports/aleph-zero-q4-overview

Aleph Zero Smart Contract Audit | Cyberscope. (2025). https://www.cyberscope.io/audits/coin-aleph-zero

Architecture · Guide - Kusama Network. (2024). https://guide.kusama.network/docs/learn-architecture

Best Decentralized Exchanges (DEX) in Japan - Page 7. (2025). https://slashdot.org/software/decentralized-exchanges-dex/in-japan/?page=7

Breaking the Limits: The Power of Aleph Zero’s Layer 1 ... - Medium. (2023). https://medium.com/@researchcoindelta/breaking-the-limits-the-power-of-aleph-zeros-layer-1-zero-knowledge-proof-system-e4dad99cc9c9

C. Aldrich. (2016). @djsardine I’ve been working on some improved documentation for past couple of weeks. Should have something a bit more comprehensive soon. https://www.semanticscholar.org/paper/d48dafa95e398c4395b9dcc81c97e9b258c2f383

C. Oliveira & Vanderlei Bonato. (2023). A FAST Hardware Decoder Optimized for Template Features to Obtain Order Book Data in Low Latency. In Journal of Signal Processing Systems. https://www.semanticscholar.org/paper/99c092e45645352ace665df42b10a5a3c567ac90

Carsten Baum, J. Chiang, B. David, T. Frederiksen, & Lorenzo Gentile. (2021). SoK: Mitigation of Front-running in Decentralized Finance. In IACR Cryptology ePrint Archive. https://www.semanticscholar.org/paper/8539847cb80bd976159700239448b8b03946ab47

Chris Dai. (2020). DEX: A DApp for the Decentralized Marketplace. In Economics, Law, and Institutions in Asia Pacific. https://link.springer.com/chapter/10.1007/978-981-15-3376-1_6

Christian W. Probst. (2016). Guaranteeing Privacy-Observing Data Exchange. In Leveraging Applications of Formal Methods. https://link.springer.com/chapter/10.1007/978-3-319-47166-2_66

CR Harvey, J Hasbrouck, & F Saleh. (2024). The evolution of decentralized exchange: Risks, benefits, and oversight. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4861942

D Xiang, Y Lin, L Nie, Y Zheng, Z Xu, & Z Ding. (2024). An empirical study of attack-related events in DeFi projects development. https://link.springer.com/article/10.1007/s10664-024-10447-7

Dexalot - Own Your Trade. (n.d.). https://dexalot.com/

E Saltalamacchia. (n.d.). Operational eXcellence by Integrating Learned information into AcTionable Expertise. https://itea3.org/project/workpackage/document/download/7406/OXILATE_Deliverable_D1.3_Overview%20of%20the%20state%20of%20the%20art.pdf

G. Wagner & E. Grundmann. (1983). Zukünftige Erweiterung der Basisdokumentation. https://www.semanticscholar.org/paper/0fd47f112c827c08e8a49a4644fc87c820b79868

Interactive AI-Powered Documentation for Polkadot and Kusama ... (2025). https://forum.polkadot.network/t/interactive-ai-powered-documentation-for-polkadot-and-kusama-enhancing-engagement-and-accessibility/11491

J Burdges, A Cevallos, & HK Alper. (2024). Efficient Execution Auditing for Blockchains under Byzantine Assumptions. https://eprint.iacr.org/2024/961

Jiahua Xu, Nazariy Vavryk, Krzysztof Paruch, Simon, & Cousaert. (2021). SOK: Automated Market Maker (AMM) based Decentralized Exchanges (DEXs). https://www.semanticscholar.org/paper/8db46c57c7cf0714ee40406ece7ebd592b630c53

Jun Aoyagi & Yuki Ito. (2021). Coexisting Exchange Platforms: Limit Order Books and Automated Market Makers. In Entrepreneurship & Economics eJournal. https://www.semanticscholar.org/paper/032049d659b63935da828a762ee50a4ce5e922c2

Karan Doshi. (2014). Proof of the existence of Transfinite Cardinals strictly smaller than Aleph Zero with an ensuing solution to the Twin Prime conjecture. In viXra. https://www.semanticscholar.org/paper/860814a5ee039fd0e3ae63cc440c56c0a4a4419d

Kusama | ChainUp Cloud. (2023). https://docs.chainupcloud.com/blockchain-api/kusama

Kusama RPC Endpoints | Free & Paid Nodes - dRPC. (n.d.). https://drpc.org/chainlist/kusama

Leslie Boni & C. Leach. (2004). Expandable limit order markets. In Journal of Financial Markets. https://linkinghub.elsevier.com/retrieve/pii/S1386418103000417

M. Chlistalla. (2011). From minutes to seconds and beyond: measuring order-book resiliency in fragmented electronic securities markets. In European Conference on Information Systems. https://www.semanticscholar.org/paper/728b0f009e943453ab57c1c438bb4d10bf417c4c

MA Aleisa. (2025). Blockchain-Enabled Zero Trust Architecture for Privacy-Preserving Cybersecurity in IoT Environments. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10839415/

Major Upgrades to the Aleph Zero Ecosystem Bringing Utility to ... (2024). https://genfinity.io/2024/06/20/aleph-zero-ecosystem-upgrades-2024/

Marvin Bertin, Lars Br¨unjes, & H. Wahab. (n.d.). Genius DEX v1: A Parallelizable DEX for a EUTxO-Based Blockchain. https://www.semanticscholar.org/paper/d10a0f25821850f4269c67328bc02c28c3e40130

Monthly Update: August/September - Aleph Zero. (2023). https://alephzero.org/blog/monthly-update-august-september-2023/

MP Fernández, S Gustafsson, & B McCarthy. (2021). Wanderer Above a Sea of FUD: Cultural workforce, crypto anarchism, intellectual rights, and blockchain-based funding models for culture and arts. https://www.academia.edu/download/65576143/Wanderer_Above_a_Sea_of_FUD.pdf

Niraj K. Sharma & Jagannathan Srinivasan. (1989). DEX: A HIGH LEVEL TOOL FOR DISTRIBUTED SYSTEM EXPERIMENTS. https://www.semanticscholar.org/paper/2ab4a9df52d0d770a3b3f4480880994e812425cc

O.A. Ghodake, R.M. Samant, W. Rahane, A.A. Madanepatil, A.M. Patil, & S.M. Makwani. (2023). spryDEX:Decentralized Exchange for Cryptocurrencies using Blockchain. In 2023 7th International Conference On Computing, Communication, Control And Automation (ICCUBEA). https://ieeexplore.ieee.org/document/10392018/

On-chain privacy, confidential data, and compliance in Web3. (2024). https://alephzero.org/blog/onchain-privacy-confidential-data-compliance-in-web3/

P. Handa & R. A. Schwartz. (1996). Dynamic price discovery. In Review of Quantitative Finance and Accounting. https://www.semanticscholar.org/paper/bde29c8e9bfc43b24d53ca15f181f31b12a93f03

P. Hoenisch, Subhra Mazumdar, Pedro A. Moreno-Sánchez, & S. Ruj. (2022). LightSwap: An Atomic Swap Does Not Require Timeouts At Both Blockchains. In IACR Cryptology ePrint Archive. https://www.semanticscholar.org/paper/61d127ac600ddf76101ca8519449ab5d12d31596

POLKADEX ORDERBOOK - Pontem Network. (2022). https://pontem.network/posts/polkadex-orderbook

Polkadex Orderbook is live. The CEXier DEX is here: non-custodial…. (2022). https://polkadex.medium.com/polkadex-orderbook-is-live-92749206d465

Polkadex (PDEX) - Ledger Support. (2025). https://support.ledger.com/article/6856017732637-zd

Polkadex project details | Polkadot network - Parachains.info. (n.d.). https://parachains.info/details/polkadex

Polkadex, the Best Order Book DEX on the Market? - Altcoin Buzz. (2023). https://www.altcoinbuzz.io/product-release/polkadex-the-best-order-book-dex-on-the-market/

Polkadex vs other DEXes: Why we are different - Medium. (2021). https://medium.com/polkadex/polkadex-vs-other-dexes-why-we-are-different-dded31dbd6ca

Polkadex-Substrate/Polkadex: An Orderbook-based Decentralized ... (n.d.). https://github.com/Polkadex-Substrate/Polkadex

Polkadot’s Consensus Protocols · Guide - Kusama Network. (2025). https://guide.kusama.network/docs/learn-consensus

Polkaswap — A Multichain DEX: An Interview with Lead ... - Medium. (2023). https://medium.com/@soranews/polkaswap-a-multichain-dex-an-interview-with-lead-polkaswap-developer-stefan-7bb6e598dfb1

Polkaswap - Decentralized Exchange on SORA Network. (2023). https://wiki.sora.org/polkaswap.html

Polkaswap - Sora.org. (2025). https://sora.org/polkaswap

Polkaswap — The DEX for the Interoperable Future. (n.d.). https://polkaswap.io/

Polkaswap Ecosystem Updates #79, July 10, 2024 - Medium. (2024). https://medium.com/polkaswap/polkaswap-ecosystem-updates-79-july-10-2024-a614c46b84c4

Polkaswap Unveils Fully Decentralised On-Chain Order Book ... (2024). https://cryptopotato.com/polkaswap-unveils-fully-decentralised-on-chain-order-book-setting-new-standards-in-defi/

Preston So. (2018). Schemas and Generated Documentation. https://www.semanticscholar.org/paper/4351b695a351f3611ca0c742c3cb87d1dffe1bc5

Releases · sora-xor/polkaswap-exchange-web - GitHub. (2025). https://github.com/sora-xor/polkaswap-exchange-web/releases

Sanjana Panicker, V. Patil, Divya D. Kulkarni, & B. E. Student. (2016). An Overview of Blockchain Architecture and it’s Applications. https://www.semanticscholar.org/paper/3b2b9857d88bc7045c83db5fa23360166510a326

Shan Jiang, Jiannong Cao, Juncen Zhu, & Yinfeng Cao. (2021). PolyChain: A Generic Blockchain as a Service Platform. In International Conference on Blockchain and Trustworthy Systems. https://www.semanticscholar.org/paper/b42f84cde651b9216ae567370eb40228bbf5f377

SM Solís. (2023). Zero Trust Chain A Design Pattern for Improved Interoperability and Security in Polkadot. In arXiv. https://arxiv.org/abs/2304.14730

Top Decentralized Exchanges (DEX) for Kusama in 2025 - Slashdot. (2025). https://slashdot.org/software/decentralized-exchanges-dex/for-kusama/

Top Decentralized Exchanges (DEX) for Polkadot in 2025 - Slashdot. (2025). https://slashdot.org/software/decentralized-exchanges-dex/for-polkadot/

WELCOME TO ALEPH ZERO | Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero

What is Aleph Zero? - Messari. (n.d.). https://messari.io/project/aleph-zero/profile

What is Aleph Zero? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/aleph-zero

What is Aleph Zero? All You Need to Know About AZERO - Gate.com. (2023). https://www.gate.com/learn/articles/what-is-aleph-zero/836

What is Aleph Zero: The Advanced ZK Modular Blockchain ... (2024). https://web3.bitget.com/en/academy/what-is-aleph-zero

What is Kusama? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/kusama

What Is Order Book DEX Development? Full Guide - Rock’n’Block. (2024). https://rocknblock.io/blog/what-is-order-book-dex-development-full-guide

What is Polkadex? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/polkadex

What Is Polkaswap? - CoinMarketCap. (2021). https://coinmarketcap.com/academy/article/what-is-polkaswap

What is PolkaSwap? A DEX Designed for PolkaDot. (2020). https://www.asiacryptotoday.com/polkaswap/

What Is The Fastest Blockchain And Why? Analysis of 43 Blockchains. (2021). https://alephzero.org/blog/what-is-the-fastest-blockchain-and-why-analysis-of-43-blockchains/

Zhao Zhi-gao. (2006). Analysis of the development of containership based on order-book. https://www.semanticscholar.org/paper/b7b14a8981834e9a4e1a08382cdd0f1b61bafa90



Generated by Liner
https://getliner.com/search/s/5926611/t/86418463