Evaluate Polkadex, SPEEDEX, and Aleph Zero with regard to their suitability for serving as infrastructural blockchains capable of supporting over 100,000 TPS (transactions per second) for order-book-based DEXs (decentralized exchanges). Requirements: 

 1. Consider the following aspects: core components, core functions, architectural features, development language, major technology stacks, difficulty and cost of customization/development, GitHub stars, level of decentralization, transparency, scalability, consensus mechanism, fault tolerance, cross-chain capabilities, advantages/disadvantages, constraints, risks, TPS and the conditions under which TPS testing was conducted, latency, maturity, ecosystem, market prospects, transaction cost, among others. 

 2. Prepare a competitor analysis and a summary table that clearly identifies the optimal choice for a high-performance DEX blockchain.
 
 3. Utilize lists and tables as necessary to enhance clarity and readability. 

 4. Provide a list of official materials, including GitHub links, official websites, documents, white papers, etc.

Fri Jul 11 2025

Polkadex, SPEEDEX, and Aleph Zero each present unique approaches to serving as infrastructural blockchains for high-performance, order-book-based decentralized exchanges (DEXs). SPEEDEX appears to be the most suitable option for supporting over 100,000 TPS for order-book-based DEXs due to its demonstrated high throughput, Layer-1 integration, and specialized design for order book efficiency.

### Competitor Analysis

#### Polkadex
Polkadex is a non-custodial, peer-to-peer, order-book-based crypto exchange built on the Substrate blockchain framework. It combines features of centralized and decentralized exchanges to offer an optimal trading environment.

- **Core Components and Functions**: Polkadex Orderbook is the core product, comprising the Polkadex Network (its native blockchain), a Trusted Execution Environment (TEE), and an Orderbook. It aims to provide fast execution logic, support for custom trading and bots, and on-chain order book functionality.
- **Architectural Features**: Its architecture integrates blockchain, parachain, TEE, and IPFS technologies. Polkadex leverages the Polkadot ecosystem for enhanced liquidity and security.
- **Development Language and Tech Stack**: Polkadex is developed using Rust, which is used for efficient order matching. It is built on the Substrate blockchain framework.
- **Scalability and TPS**: Polkadex aims to support up to 500,000 transactions per second (TPS) with sub-millisecond latency. However, current observed TPS figures are significantly lower, at 0.0036 tx/s, with a maximum TPS of 0.45 tx/s. Its maximum theoretical TPS is stated as 1,500 tx/s. Polkadex's design back in 2018 focused on scaling transaction throughput on a distributed network, applying this technology to a DEX.
- **Latency**: Polkadex aims for a low latency of 20 milliseconds. Query latency for the order book state has been reduced to microseconds, allowing near-instant order placement and retrieval.
- **Decentralization and Transparency**: Polkadex is described as a fully decentralized peer-to-peer order-book-based cryptocurrency exchange.
- **Cross-chain Capabilities**: It enables users to trade tokens across Polkadex, Ethereum, and Polkadot blockchains. Polkadex aims to support tokens across the Polkadot ecosystem and external blockchains through integration with Hyperbridge.
- **Advantages and Disadvantages**: Advantages include high-performance, low-latency trading, and a fully decentralized order book. Disadvantages for DEXs in general, which Polkadex aims to overcome, include low liquidity, limited trading functionality, limited speeds, and lack of advanced features like high-frequency trading and bots.
- **Maturity and Ecosystem**: Polkadex was launched on September 26, 2021. Its ecosystem focuses on providing a non-custodial, peer-to-peer order-book-based trading platform for Web3 and DeFi.
- **Transaction Cost**: The search results do not explicitly provide specific transaction costs for Polkadex.
- **GitHub Stars**: The search results do not explicitly provide the number of GitHub stars for Polkadex.

#### SPEEDEX
SPEEDEX is a decentralized exchange (DEX) designed for scalability, parallelization, and economic efficiency. It operates entirely within a Layer-1 blockchain.

- **Core Components and Functions**: SPEEDEX uses an Arrow-Debreu exchange market structure that fixes the valuation of assets for all trades within a given block. This structure makes trade operations commutative and efficiently parallelizable. It processes a block of limit orders as one unified transaction.
- **Architectural Features**: Its design allows for high throughput without fragmenting market liquidity across multiple blockchains or rollups. It aims for near linear scalability through computational parallelism.
- **Development Language and Tech Stack**: SPEEDEX uses the GNU Linear Programming Kit (GLPK). It is prototyped within the Stellar blockchain.
- **Scalability and TPS**: SPEEDEX achieves high throughput, processing over 200,000 transactions per second on 48-core servers, even with tens of millions of open offers. It is designed to leverage efficient bulk parallel processing.
- **Latency**: The search results do not explicitly provide specific latency figures for SPEEDEX.
- **Decentralization and Transparency**: SPEEDEX allows participants to securely trade assets without giving undue control to any single party, operating as a decentralized exchange. The search results do not explicitly provide specific details on its transparency level.
- **Cross-chain Capabilities**: The search results do not explicitly detail SPEEDEX's cross-chain capabilities, beyond stating it achieves scalability without fragmenting market liquidity between multiple blockchains or rollups. Cross-chain technology generally enhances interoperability and improves transaction efficiency and speed across networks.
- **Advantages and Disadvantages**: Advantages include high throughput, elimination of internal arbitrage opportunities, prevention of certain front-running attacks, and fairness across trades.
- **Constraints and Risks**: One consideration in its design is deciding which assets are eligible to participate in the SPEEDEX market mechanism.
- **Maturity and Ecosystem**: SPEEDEX is prototyped and was scheduled for deployment within a large Layer-1 blockchain. Evrynet planned to incorporate SPEEDEX technology into its ecosystem in 2022.
- **Transaction Cost**: SPEEDEX approximates clearing prices in a block in general equilibrium. Sequential execution of transactions could lead to an 8%–83% increase in transaction costs.
- **GitHub Stars**: The search results do not explicitly provide the number of GitHub stars for SPEEDEX.

#### Aleph Zero
Aleph Zero is a Layer-1 blockchain platform that focuses on scalability, security, privacy, developer friendliness, and cost of use. It launched its mainnet in 2021.

- **Core Components and Functions**: Aleph Zero utilizes a novel consensus protocol called AlephBFT, which integrates a Directed Acyclic Graph (DAG) architecture. It provides privacy features through zero-knowledge proofs (ZKPs) and a native privacy stack.
- **Architectural Features**: It is a highly scalable architecture with its own AlephBFT consensus mechanism. It combines the benefits of public and private blockchains, offering a scalable proof-of-stake infrastructure. Its DAG-based consensus allows for parallel transactions.
- **Development Language and Tech Stack**: Aleph Zero is primarily built upon the Rust programming language, having previously used Golang. It deploys the WebAssembly (Wasm) virtual machine and the ink! smart contract programming language. It is compatible with Parity's Substrate tech stack.
- **Scalability and TPS**: Aleph Zero has demonstrated high scalability. Its consensus protocol can process up to 89,600 transactions per second (TPS) with a 416 millisecond confirmation time. Older tests achieved 100,000 TPS on 128 nodes using a Python prototype. Its current TPS is 40,000.
- **Latency**: Aleph Zero has a transaction time of 0.6 seconds. RPC latency is 11ms. It boasts subsecond transaction and ZK-privacy proving times.
- **TPS Testing Conditions**: Aleph Zero's performance was tested on Amazon servers with 112 nodes across 7 regions, using 300-byte transactions.
- **Decentralization and Transparency**: Aleph Zero is committed to genuine decentralization, with community validators taking over block finalization. It aims for transparency through a public-private ledger, ensuring security of sensitive information.
- **Fault Tolerance**: Aleph Zero employs Byzantine Fault Tolerance (BFT) architecture, allowing it to tolerate up to 33% of malicious committee members without affecting validation. It uses rotating committees to overcome BFT challenges in a decentralized setting.
- **Cross-chain Capabilities**: Aleph Zero enhances blockchain with cross-chain security and simplifies cross-chain operations through integrations like Across Protocol. It offers a two-way bridge for asset transfers between independent chains.
- **Advantages and Disadvantages**: Advantages include enterprise-readiness, privacy features through ZKPs, and the ability to exchange value faster, more cheaply, and more securely.
- **Maturity and Ecosystem**: Aleph Zero has been in development for over a year as of August 2019 and launched its mainnet with notable initial adoption. Its ecosystem offers privacy-enhancing blockchain solutions for various users. The Aleph Zero Foundation oversees protocol development and issues the AZERO coin. Cardinal Cryptography is the core developer.
- **Transaction Cost**: As of May 2025, the approximate transaction cost on the Aleph Zero network is $0.01. The average transaction fee is 0.0004 AZERO.
- **Official Materials**:
    - **Official Website**: https://alephzero.org/
    - **GitHub Repository**:
        - Aleph Zero Foundation GitHub: https://github.com/aleph-zero-foundation
        - Cardinal Cryptography GitHub (Aleph Zero code): https://github.com/Cardinal-Cryptography/aleph-node
        - Aleph Zero API GitHub: https://github.com/alephzero/api
        - AlephZero library GitHub: https://github.com/alephzero/alephzero
        - Proof-of-Concept implementation on GitHub:
    - **Whitepapers**: Peer-reviewed white paper. Additional whitepapers on secure smart contracts, zk-proof blockchain, and privacy-enhancing technology. The Business Whitepaper is also available.
    - **Documentation**: Comprehensive guides and tutorials for developers.

#### Polkadex Official Materials
- **Official Website**: The search results do not explicitly list a single "official website" for Polkadex, but various documents suggest `polkadex.ee` for documentation and `polkadex.medium.com` for updates.
- **GitHub Repository**: https://github.com/Polkadex-Substrate.
- **Whitepapers**: Available for deep analysis of Polkadex (PDEX) and information on Thea Bridge.

#### SPEEDEX Official Materials
- **Official Website**: The search results do not explicitly list an "official website" for SPEEDEX.
- **GitHub Repository**: https://github.com/scslab/speedex.
- **Whitepapers**: The search results mention research papers and a white paper by CRESTA.

### Summary Table: High-Performance DEX Blockchain Suitability

| Feature                       | Polkadex                                            | SPEEDEX                                         | Aleph Zero                                                                  | Optimal for 100,000+ TPS DEX? |
| :---------------------------- | :-------------------------------------------------- | :---------------------------------------------- | :-------------------------------------------------------------------------- | :---------------------------- |
| **Core Components**           | Polkadex Network, TEE, Orderbook | Arrow-Debreu exchange market structure | AlephBFT consensus, DAG architecture, PoS | SPEEDEX, Aleph Zero           |
| **Core Functions**            | Order-book-based trading, high-frequency, algorithmic trading, bot support | Secure asset trading, arbitrage elimination, front-running prevention | Scalable, secure, low-cost Web3 apps, private smart contracts, confidential enterprise solutions | SPEEDEX, Aleph Zero           |
| **Architectural Features**    | Blockchain, parachain, TEE, IPFS | Layer-1 blockchain, parallelizable trade operations | Layer-1 blockchain, DAG-based consensus, ZKP privacy stack, WASM L1, EVM L2 | SPEEDEX, Aleph Zero           |
| **Development Language**      | Rust                               | GNU Linear Programming Kit (GLPK)     | Rust (previously Golang), ink! (WASM) | Aleph Zero, Polkadex          |
| **Major Technology Stacks**   | Substrate                     | Stellar blockchain (prototyped within) | Substrate, WASM, ink!                         | Aleph Zero, Polkadex          |
| **Difficulty/Cost of Customization/Development** | Not explicitly detailed | Not explicitly detailed                         | Not explicitly detailed                                                     | (Unclear)                     |
| **Scalability**               | Aims for 500,000 TPS; theoretical 1,500 tx/s; leverages Polkadot | Over 200,000 TPS on 48-core servers | 89,600 TPS (current test); 100,000 TPS (prototype) | SPEEDEX, Aleph Zero           |
| **Consensus Mechanism**       | Proof of Stake (PoS)                      | Arrow-Debreu exchange market structure (for valuations) | AlephBFT (DAG-based, leaderless, asynchronous, BFT) | Aleph Zero                    |
| **Fault Tolerance**           | Not explicitly detailed                             | Not explicitly detailed                         | Byzantine Fault Tolerant (tolerates up to 33% malicious nodes) | Aleph Zero                    |
| **Cross-Chain Capabilities**  | Polkadot, Ethereum, external blockchains via Hyperbridge | Scalability without fragmenting liquidity between blockchains | Cross-chain security, two-way bridge, EVM-compatible chains | Aleph Zero, Polkadex          |
| **Advantages**                | High performance, low latency, non-custodial, peer-to-peer | High throughput, eliminates arbitrage, prevents front-running | Scalability, security, privacy, developer friendliness, low cost, enterprise-ready | SPEEDEX, Aleph Zero           |
| **Disadvantages/Constraints** | Current TPS significantly lower than theoretical; DEX challenges: low liquidity, limited features | Not explicitly detailed (aside from asset eligibility criteria) | (None explicitly stated as disadvantages)                                   | Polkadex (current TPS)        |
| **TPS (Observed/Tested)**     | 0.0036 tx/s; Max: 0.45 tx/s         | >200,000 tx/s on 48-core servers | 89,600 TPS (current test); 40,000 TPS             | SPEEDEX, Aleph Zero           |
| **TPS Testing Conditions**    | Not explicitly detailed                             | 48-core servers, tens of millions of open offers | Amazon servers, 112 nodes, 7 regions, 300-byte transactions      | SPEEDEX, Aleph Zero           |
| **Latency**                   | Sub-millisecond (aim); 20ms; Microseconds for queries | Not explicitly detailed                         | 416 ms confirmation; 11ms RPC; subsecond transaction/ZK proving | Aleph Zero, Polkadex          |
| **Maturity**                  | Launched Sep 26, 2021                        | Prototyped, scheduled for deployment in Layer-1 | Mainnet launched, in development since 2018                  | Aleph Zero, Polkadex          |
| **Ecosystem**                 | Polkadot, Web3, DeFi | Stellar blockchain, Evrynet | Privacy-enhancing solutions for businesses, developers, individuals; integrations with Ledger, Across Protocol | Aleph Zero                    |
| **Market Prospects**          | Focus on growth for crypto industry, seamless trading | Not explicitly detailed                         | Potential for public/private ledger, addressing MEV | Aleph Zero                    |
| **Transaction Cost**          | Not explicitly detailed                             | 8-83% increase for sequential transactions | ~\\$0.01 (as of May 2025); 0.0004 AZERO avg. fee        | Aleph Zero                    |
| **Optimal for 100,000+ TPS DEX?** | No (current TPS is too low)                   | Yes                                             | Yes (with conditions)                                                       | **SPEEDEX**                 |

### Optimal Choice for a High-Performance DEX Blockchain

Based on the evaluation criteria, **SPEEDEX** currently stands out as the optimal choice for an infrastructural blockchain capable of supporting over 100,000 TPS for order-book-based DEXs.

- **SPEEDEX** has explicitly demonstrated throughput of over 200,000 transactions per second under specific testing conditions (48-core servers with tens of millions of open offers). Its core design, utilizing an Arrow-Debreu exchange market structure, is specifically engineered to handle order book operations efficiently and in a parallelizable manner, which is crucial for high-performance DEXs. Its full integration within a Layer-1 blockchain also avoids market liquidity fragmentation issues.

While **Aleph Zero** has shown impressive theoretical and tested TPS figures (up to 89,600 TPS in recent tests and 100,000 TPS in a Python prototype), it is slightly below the 100,000 TPS threshold based on the more recent test figures provided. However, its DAG-based consensus and focus on scalability make it a strong contender. Its subsecond latency and Byzantine Fault Tolerance are also significant advantages.

**Polkadex**, despite aiming for 500,000 TPS and having low latency, currently exhibits much lower observed TPS (0.0036 tx/s). While its theoretical maximum is 1,500 tx/s, this falls significantly short of the 100,000 TPS requirement. Therefore, Polkadex is not currently suitable for this specific high-performance requirement.

Bibliography
A Akbik, T Bergmann, D Blythe, & K Rasul. (2019). FLAIR: An easy-to-use framework for state-of-the-art NLP. https://aclanthology.org/N19-4010/

A Gągol, D Leśniak, D Straszak, & M Świętek. (2019). Aleph: Efficient atomic broadcast in asynchronous networks with byzantine nodes. https://dl.acm.org/doi/abs/10.1145/3318041.3355467

A Gągol & M Świętek. (2018). Aleph: A leaderless, asynchronous, byzantine fault tolerant consensus protocol. In arXiv. https://arxiv.org/abs/1810.05256

A Hafezeqoran & M Rahbar. (2021). Comparing the dimensional accuracy of casts obtained from two types of silicone impression materials in different impression techniques and frequent times of cast …. https://onlinelibrary.wiley.com/doi/abs/10.1155/2021/9977478

A Scalable, Parallelizable, and Economically Efficient Digital - DBLP. (2021). https://dblp.org/rec/journals/corr/abs-2111-02719

A Srinivasan. (2001). The aleph manual. https://www.dcc.fc.up.pt/~ines/aulas/1920/TAIA/The%20Aleph%20Manual%20V6.pdf

About Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/explore/about-aleph-zero

Across is Live on Aleph Zero. (2024). https://across.to/blog/Across-is-Live-on-Aleph-Zero

Aleph Zero | Blazingly fast blockchain with modular ZK. (n.d.). https://alephzero.org/

Aleph Zero - Cryptocurrencies - IQ.wiki. (n.d.). https://iq.wiki/wiki/aleph-zero

Aleph Zero - Fundamentals: TPS vs. Latency vs. Finality - LinkedIn. (2022). https://www.linkedin.com/posts/alephzero_fundamentals-tps-vs-latency-vs-finality-activity-6894975239332474882-xotd

Aleph Zero - Linktree. (2021). https://linktr.ee/alephzero

Aleph Zero: A Guide to Zero-Knowledge Public Blockchain. (2022). https://beincrypto.com/learn/aleph-zero/

Aleph Zero and its unique AlephBFT consensus protocol - Medium. (2023). https://medium.com/@gotbit_insights/driving-force-behind-technologies-aleph-zero-and-its-unique-alephbft-consensus-protocol-f6e3b7c198c2

Aleph Zero (AZERO): Everything You Need to Know. (n.d.). https://thefinancialhorizons.com/2024/09/04/aleph-zero-azero-everything-you-need-to-know/

Aleph Zero (AZERO) Price Prediction 2025, 2026-2030 - CoinCodex. (n.d.). https://coincodex.com/crypto/aleph-zero/price-prediction/

Aleph Zero (AZERO) Whitepaper - Securities.io. (2022). https://www.securities.io/aleph-zero-whitepaper/

Aleph Zero: Balancing Security, Scalability and Decentralization in ... (2023). https://www.binance.com/en/square/post/267220

Aleph Zero Blockchain Applications. (n.d.). https://alephzero.org/applications

Aleph Zero Bridges: Interoperability with Ethereum - Nextrope. (2024). https://nextrope.com/aleph-zero-bridges-interoperability-with-ethereum/

Aleph Zero Ecosystem - Aleph Zero: Public Blockchain with Private ... (n.d.). https://alephzero.org/ecosystem

Aleph Zero EVM: RPC and Chain Settings - Thirdweb. (n.d.). https://thirdweb.com/aleph-zero-evm

Aleph Zero EVM stats. (n.d.). https://evm-explorer.alephzero.org/stats

Aleph Zero Foundation - GitHub. (n.d.). https://github.com/aleph-zero-foundation

Aleph Zero in numbers - nightly.app. (n.d.). https://nightly.app/article/aleph-zero-in-numbers

Aleph Zero Integrates Across Protocol: Making Bridging Lightning ... (2024). https://alephzero.org/blog/aleph-zero-integrates-across-protocol-making-bridging-lightning-fast-and-more-affordable-and-secure/

Aleph Zero is a gem in the Polkadot Ecosystem!! - Medium. (n.d.). https://medium.com/@polkanotes/aleph-zero-is-a-gem-in-the-polkadot-ecosystem-92e5369a62da

Aleph Zero: Learn Everything from its Detailed Working to Unique ... (2023). https://www.antiersolutions.com/blogs/demystifying-aleph-zero-working-benefits-native-currency-unique-features/

Aleph Zero Overview - Reflexivity Research. (n.d.). https://www.reflexivityresearch.com/free-reports/aleph-zero-overview

Aleph Zero Q2 2024 Update - Reflexivity Research. (n.d.). https://www.reflexivityresearch.com/all-reports/aleph-zero-q2-update

Aleph Zero Q4 Overview - Reflexivity Research. (n.d.). https://www.reflexivityresearch.com/free-reports/aleph-zero-q4-overview

Aleph Zero [TPS, Max TPS, Block Time & TTF] | Chainspect. (n.d.). https://chainspect.app/chain/aleph-zero

Aleph Zero vs Polkadex [TPS, Max TPS, Block Time] | Chainspect. (2021). https://chainspect.app/compare/aleph-zero-vs-polkadex

Aleph Zero vs Solana: A Comparative Analysis - Nextrope. (n.d.). https://nextrope.com/aleph-zero-vs-solana-a-comparative-analysis/

Aleph Zero’s 2025 Roadmap: Advancing Decentralization and ... (2025). https://www.stakecito.com/blog/aleph-zero-s-2025-roadmap-advancing-decentralization-and-privacy-in-web3

Aleph Zero’s Proof-of-Concept Released on GitHub. (2019). https://alephzero.org/blog/aleph-zeros-proof-of-concept-released-on-github/

AlephBFT Consensus - Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/explore/alephbft-consensus

AlephZero - GitHub. (n.d.). https://github.com/alephzero/alephzero

alephzero/api - GitHub. (2019). https://github.com/alephzero/api

Andrew Selden aleph-zero - GitHub. (2025). https://github.com/aleph-zero

Andrey Sarayev, Serge Levin, & Maryna Bizhikian. (2023). Operation of the PDM Staking System in Cryptocurrency: Analysis, Advantages, and Challenges. In 2023 IEEE 1st Ukrainian Distributed Ledger Technology Forum (UADLTF). https://ieeexplore.ieee.org/document/10549206/

Antoni Calvó-Armengol. (2003). A decentralized market with trading links. In Math. Soc. Sci. https://linkinghub.elsevier.com/retrieve/pii/S0165489602000653

Architecture - Polkadot Wiki. (n.d.). https://wiki.polkadot.network/learn/learn-architecture/

Audit & Research Papers - Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/explore/audit-and-research-papers

B. Buzbee. (1993). Examples of Scalable Performance. https://link.springer.com/chapter/10.1007/978-3-642-58049-9_22

Breaking the Limits: The Power of Aleph Zero’s Layer 1 ... - Medium. (2023). https://medium.com/@researchcoindelta/breaking-the-limits-the-power-of-aleph-zeros-layer-1-zero-knowledge-proof-system-e4dad99cc9c9

Building SPEEDEX – A Novel Design for a Scalable Decentralized ... (2021). https://stellar.org/blog/developers/building-speedex-a-novel-design-for-decentralized-exchanges

by Aleph Zero Foundation - QuickNode. (n.d.). https://www.quicknode.com/builders-guide/tools/aleph-zero-by-aleph-zero-foundation

C. Bessiere, Patricia Gutierrez, & P. Meseguer. (2012). Including Soft Global Constraints in DCOPs. In International Conference on Principles and Practice of Constraint Programming. https://link.springer.com/chapter/10.1007/978-3-642-33558-7_15

C. Reid. (2006). From Zero to Infinity: What Makes Numbers Interesting. https://www.taylorfrancis.com/books/9781439881231

Cardinal-Cryptography/aleph-node - GitHub. (n.d.). https://github.com/Cardinal-Cryptography/aleph-node

Carsten Baum, B. David, & T. Frederiksen. (2021). P2DEX: Privacy-Preserving Decentralized Cryptocurrency Exchange. In IACR Cryptol. ePrint Arch. https://link.springer.com/chapter/10.1007/978-3-030-78372-3_7

Chen Jia. (2000). The Scalability Audio Coding. In Audio Engineering. https://www.semanticscholar.org/paper/f4f1a5504ce9ffcd137360bb125b063f28896cdf

Consensus Protocols: What Powers Blockchain and DLT - Aleph Zero. (2020). https://alephzero.org/blog/consensus-protocols-what-powers-blockchain-dlt/

Cross-Chain Compatibility for Seamless Blockchain Access. (n.d.). https://www.nadcab.com/blog/cross-chain-compatibility-on-blockchain

Daniel Nussbaum & A. Agarwal. (1991). Scalability of parallel machines. In Commun. ACM. https://dl.acm.org/doi/10.1145/102868.102871

DappRadar on X: “10 Things to Know About Aleph Zero” / X. (n.d.). https://x.com/DappRadar/status/1924877736520352052

Decentralized Governance on Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/explore/decentralized-governance-on-aleph-zero

Deep dive: Polkadex Orderbook. (2021). https://polkadex.medium.com/deep-dive-polkadex-orderbook-c2f8cbb4ad51

Dev Portal - Aleph Zero. (n.d.). https://alephzero.org/developers

Dr StEfAno MArkiDiS, ProfESSor MArk PArSonS, & Dr LornA SMitH. (2013). CRESTA White Paper. https://www.semanticscholar.org/paper/7f325de54e1b314ac51be31125ce17ef8d82b211

DV Gryzodub. (2015). INDIVIDUAL SELECTION OF SILICONE IMPRESSION MATERIALS IN PROSTHETIC PATIENTS INTOLERANT OF PROSTHETIC MATERIAL. In Intermedical journal. http://journals.uzhnu.uz.ua/index.php/intermedical/article/view/111

E. Renaux & Cran Lara. (1992). FAULT TOLERANCE BY A DISTRIBUTED SOFTWARE CONTROL FOR A HIGH RELIABILITY. In IFAC Proceedings Volumes. https://linkinghub.elsevier.com/retrieve/pii/S1474667017494080

Eli Ben-Sasson, Iddo Bentov, Y. Horesh, & Michael Riabzev. (2019). Scalable Zero Knowledge with No Trusted Setup. In Annual International Cryptology Conference. https://link.springer.com/chapter/10.1007/978-3-030-26954-8_23

Emily R. Jacobson, Michael J. Brim, & B. Miller. (2010). A Lightweight Library for Building Scalable Tools. In Workshop on Applied Parallel Computin. https://www.semanticscholar.org/paper/4f4f07cbb96e40763e9f6f84b8c4eb3c3820db00

Ep. 119 Scalability Meets Privacy: How Aleph Zero ... - Apple Podcasts. (n.d.). https://podcasts.apple.com/au/podcast/ep-119-scalability-meets-privacy-how-aleph-zero-is/id1658365769?i=1000699626634

EVM ZK-privacy. Subsecond proving times. - Aleph Zero. (n.d.). https://alephzero.org/why-aleph-zero

Evrynet joins Stanford’s Initiative and will incorporate SPEEDEX as ... (2021). https://cointelegraph.com/press-releases/evrynet-joins-stanfords-initiative-and-will-incorporate-speedex-as-part-of-its-ecosystem

Exploring the Advantages of Azero: A Comprehensive Overview. (n.d.). https://typefully.com/2xnmore/exploring-the-advantages-of-azero-a-cZlcSYo

FAQ | Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/faq

Fátima Leal, Adriana E. Chis, & H. González-Vélez. (2021). Multi-service model for blockchain networks. In Inf. Process. Manag. https://linkinghub.elsevier.com/retrieve/pii/S0306457321000340

Free Aleph Zero Whitepaper - BitScreener. (n.d.). https://bitscreener.com/coins/aleph-zero/whitepaper

Free Polkadex Whitepaper - BitScreener. (n.d.). https://bitscreener.com/coins/polkadex/whitepaper

Further Decentralization Rolls Out on Aleph Zero! (2024). https://alephzero.org/blog/further-decentralization-rolls-out-on-aleph-zero/

G Nelli. (2021). Process, Product, Program: The Architect as Facilitator of Social Change. In Public Space/Contested Space. https://www.taylorfrancis.com/chapters/edit/10.4324/9781003095262-3/process-product-program-garrett-nelli

G Ramseyer, A Goel, & D Mazières. (n.d.). SPEEDEX: A Scalable, Parallelizable, and Economically Efficient Distributed EXchange. https://ccfi.scs.stanford.edu/~geoff/papers/speedex.pdf

G Ramseyer, A Goel, & D Mazières. (2023). {SPEEDEX}: A Scalable, Parallelizable, and Economically Efficient Decentralized {EXchange}. https://www.usenix.org/conference/nsdi23/presentation/ramseyer

GD Ramseyer. (2023). Scalable Infrastructure for Digital Currencies. https://search.proquest.com/openview/49c709b8cf8287886e59ba0cbfcec932/1?pq-origsite=gscholar&cbl=18750&diss=y

Geoffrey Ramseyer, Ashish Goel, & David Mazières. (2021a). SPEEDEX: A Scalable, Parallelizable, and Economically Efﬁcient Distributed EXchange. https://www.semanticscholar.org/paper/1d112fe9a859a3d71b9bf06b239404beef9fb957

Geoffrey Ramseyer, Ashish Goel, & David Mazières. (2021b). SPEEDEX: A Scalable, Parallelizable, and Economically Efficient Decentralized EXchange. In Symposium on Networked Systems Design and Implementation. https://www.semanticscholar.org/paper/7973956c43dcd7feb6a8d55f4c68cf04f9dcf6db

How is Aleph Zero Leading the Charge in Blockchain Cross-Chain ... (2024). https://www.onesafe.io/blog/aleph-zero-cross-chain-innovations

How Polkadex is Addressing the “Bottlenecks” of Decentralized ... (2022). https://decrypt.co/115745/how-polkadex-is-addressing-the-bottlenecks-of-decentralized-exchanges

I. Bálsamo. (2000). Conditions for testing performance. https://link.springer.com/chapter/10.1007/978-1-4615-4251-3_12

I Ramati. (2022). Aleph-bet, dits-and-dahs, zeros and ones: representing Hebrew in character code. In Internet Histories. https://www.tandfonline.com/doi/abs/10.1080/24701475.2021.1953757

Inside Polkadot’s Scalability Solutions: A Technical Perspective. (n.d.). https://polkadotpla.net/inside-polkadots-scalability-solutions-a-technical-perspective/

Introducing Polkadex 2.0: A New Era with Hyperbridge Integration! (2024). https://polkadex.medium.com/introducing-polkadex-2-0-a-new-era-with-hyperbridge-integration-30b547f8dba0

J Bezos. (n.d.). Mem. A multilingual package for LATEX with Aleph. http://ftp.tug.org/TUGboat/tb27-0/bezos.pdf

J Smid. (2023). The Aleph and Other Alleged Mereological Curiosities. In Australasian Journal of Philosophy. https://www.tandfonline.com/doi/abs/10.1080/00048402.2022.2043400

K. Doppler & C. Lauterburg. (2001). Outlook and Prospects. https://link.springer.com/chapter/10.1007/978-3-662-04526-8_25

K. Großpietsch. (1994). Fault tolerance. In IEEE Micro. https://ieeexplore.ieee.org/document/259893/

K. Ostertag, E. Jochem, J. Schleich, R. Walz, M. Kohlhaas, J. Diekmann, & H. Ziesing. (2000). Querschnittsaspekte: Transaktions- und Programmkosten. https://link.springer.com/chapter/10.1007/978-3-642-57683-6_7

K Thiagarajan, E Carisimo, & FE Bustamante. (2025). The Aleph: Decoding Geographic Information from DNS PTR Records Using Large Language Models. https://dl.acm.org/doi/abs/10.1145/3709374

Kaveh Aasaraai & Andreas Moshovos. (2012). SPREX: A soft processor with Runahead execution. In 2012 International Conference on Reconfigurable Computing and FPGAs. https://ieeexplore.ieee.org/document/6416786/

Learn about the Aleph Zero ecosystem in a few paragraphs. - Medium. (2023). https://medium.com/coinmonks/learn-about-the-aleph-zero-ecosystem-in-a-few-paragraphs-15e4d0461051

Lifeng Cao, Shoucai Zhao, Zhensheng Gao, & Xuehui Du. (2022). Cross-chain data traceability mechanism for cross-domain access. In The Journal of Supercomputing. https://link.springer.com/article/10.1007/s11227-022-04793-w

Lili Cheng, Zhiying Lv, Osama Alfarraj, Amr Tolba, X. Yu, & Yongjun Ren. (2024). Secure cross-chain interaction solution in multi-blockchain environment. In Heliyon. https://linkinghub.elsevier.com/retrieve/pii/S2405844024048928

LILL Unit, NB Date, BILL Unit, & P Barcode. (1994). ALEPH-DO NOT REMOVE THIS SLIP! http://homepages.gac.edu/~jwotton2/PSY385/Neurogenesis%20and%20Astrogenesis.pdf

M Breeding. (2019). Library systems report. In American libraries. https://www.jstor.org/stable/26677417

M. Hindmarsh & Photis Moulatsiotis. (1998). Constraints on Axion Models. https://linkinghub.elsevier.com/retrieve/pii/S092056329800499X

M. Krebs, H. Reichardt, Reiner Sojka, & P. Stevens. (2021). Applications and markets. In Electrochemical Power Sources: Fundamentals, Systems, and Applications. https://linkinghub.elsevier.com/retrieve/pii/B9780444643339000102

M. Rusydi & S. Islam. (2007). Market Models and Applications. https://link.springer.com/chapter/10.1057/9780230592483_4

M Zhang, S Yang, & F Zhang. (2024). RediSwap: MEV Redistribution Mechanism for CFMMs. In arXiv. https://arxiv.org/abs/2410.18434

Maram Mohammed Falatah & O. Batarfi. (2014). CLOUD SCALABILITY CONSIDERATIONS. In International Journal of Computer Science & Engineering Survey. https://www.airccse.org/journal/ijcses/papers/5414ijcses03.pdf

Mark Moir. (1997). Transparent Support for Wait-Free Transactions. In International Workshop on Distributed Algorithms. https://link.springer.com/chapter/10.1007/BFb0030692

Max Mathys, R. Schmid, J. Sliwinski, & Roger Wattenhofer. (2021). A Limitlessly Scalable Transaction System. In DPM/CBT@ESORICS. https://link.springer.com/chapter/10.1007/978-3-031-25734-6_18

Michael Sober, M. Sigwart, Philipp Frauenthaler, Christof Spanring, Max Kobelt, & Stefan Schulte. (2022). Decentralized cross-blockchain asset transfers with transfer confirmation. In Cluster Computing. https://link.springer.com/article/10.1007/s10586-022-03737-6

O Callot, P Mato, J Harvey, M Frank, W Tejessy, & B Jost. (2001). Experience with the ALEPH Online system. https://cds.cern.ch/record/529545/files/sis-2001-181.pdf

P Mikołajczyk & P Hassanizadeh. (2025). Towards Trustless Provenance: A Privacy-Preserving Framework for On-chain Media Verification. In Cryptology ePrint Archive. https://eprint.iacr.org/2025/1024

Paul H. Dembinski. (2009). The Spread of Transactions. https://link.springer.com/chapter/10.1057/9780230595057_6

[PDF] Aleph Zero Overview. (n.d.). https://cdn.prod.website-files.com/64f99c50f4c866dee943e165/65246741c40f9147e3e83a2a_Aleph%20Zero%201.pdf

[PDF] Business Whitepaper - Aleph Zero. (n.d.). https://assets.alephzero.org/docs/business-whitepaper.pdf

[PDF] SPEEDEX: A Scalable, Parallelizable, and Economically Efficient ... (2021). https://www.scs.stanford.edu/~geoff/papers/speedex.pdf

Polkadex. (2025). https://x.com/polkadex/status/1907384419825901665

Polkadex - DefiLlama. (n.d.). https://defillama.com/protocol/polkadex?denomination=PDEX

Polkadex - GitHub. (n.d.). https://github.com/polkadex-substrate

Polkadex - PDEX - Top 100 crypto list. CoinMarketRate. (n.d.). https://coinmarketrate.com/currency/polkadex/

Polkadex - RadiumBlock. (n.d.). https://www.radiumblock.com/polkadex.html

Polkadex audits by Hacken. (n.d.). https://hacken.io/audits/polkadex/

POLKADEX ORDERBOOK - Pontem Network. (2022). https://pontem.network/posts/polkadex-orderbook

Polkadex Orderbook Security Audit: A Case Study - Hacken. (2023). https://hacken.io/case-studies/polkadex-audit/

Polkadex (PDEX) Live Tokenomics, Charts, Ratings & News. (n.d.). https://tokeninsight.com/en/coins/polkadex/tokenomics

Polkadex: Polkadot’s DEX for the DeFi ecosystem - Boxmining. (n.d.). https://boxmining.com/polkadex/

Polkadex Price Prediction｜PDEX Price Forecast & Trends - BingX. (n.d.). https://bingx.com/en/price/polkadex/price-prediction

Polkadex price today, PDEX to USD live price, marketcap and chart. (n.d.). https://coinmarketcap.com/currencies/polkadex/

Polkadex project details | Polkadot network | Parachains.info. (n.d.). https://m.parachains.info/details/polkadex

Polkadex project details | Polkadot network - Parachains.info. (n.d.). https://parachains.info/details/polkadex

Polkadex Review: The Polkadot Based Decentralized Exchange ... (n.d.). https://hackernoon.com/polkadex-review-the-polkadot-based-decentralized-exchange

Polkadex [TPS, Max TPS, Block Time & TTF] | Chainspect. (2021). https://chainspect.app/chain/polkadex

Polkadex Unveils Major Upgrades to Advance Decentralized ... (n.d.). https://www.mytoken.io/en/news/497875.html

Polkadex vs Algorand [TPS, Max TPS, Block Time] - Chainspect. (n.d.). https://chainspect.app/compare/polkadex-vs-algorand

Polkadex vs other DEXes: Why we are different - Medium. (n.d.). https://medium.com/polkadex/polkadex-vs-other-dexes-why-we-are-different-dded31dbd6ca

Polkadex vs Polygon [TPS, Max TPS, Block Time] - Chainspect. (n.d.). https://chainspect.app/compare/polkadex-vs-polygon

Polkadex vs Solana [TPS, Max TPS, Block Time] - Chainspect. (n.d.). https://chainspect.app/compare/polkadex-vs-solana

Polkadex: Why We Invested - GD10 Capital. (n.d.). https://gd10.capital/insights/polkadex-why-we-invested

polkadex-docs/docs/doc3-theaBridge.md at master - GitHub. (n.d.). https://github.com/Polkadex-Substrate/polkadex-docs/blob/master/docs/doc3-theaBridge.md

Polkadex-Substrate/Polkadex: An Orderbook-based Decentralized ... (n.d.). https://github.com/Polkadex-Substrate/Polkadex

Polkadots Polkadex Everything You NEED to Know. (n.d.). https://gigachadnft.com/polkadots-polkadex-everything-you-need-to-know/

Pros and Cons of Decentralized Exchange (DEX) - DeFi Blog. (2022). https://defipedia.com/blog/pros-and-cons-of-decentralized-exchange-dex

R. Bruni & U. Montanari. (2000). Executing Transactions in Zero-Safe Nets. In ICATPN. https://www.semanticscholar.org/paper/27b92438b4d362dd141057d5478659e0917f0de9

R Bufano. (2023). The emergence of cultured meat: a socio-technical transition in the food industry with a focus on the start-up ecosystem. https://www.politesi.polimi.it/handle/10589/236285

R. Naboni & I. Paoletti. (2015). How to Build (Almost) Anything Customized. https://link.springer.com/chapter/10.1007/978-3-319-04423-1_4

R. Shen. (2009). On Aleph Zero-weak bases. In Houston Journal of Mathematics. https://www.semanticscholar.org/paper/2ad10090c5cd7462d18b074690b0268231ae31fc

R. Weiland. (1995). Transaktionen, Transaktionskosten und institutionelle Regelungen. https://www.semanticscholar.org/paper/f2cc1819002f1c29fc027c24ce9687eb68961c4b

R. Williams. (2011). Exchanges and Other Marketplaces. https://linkinghub.elsevier.com/retrieve/pii/B9780123748386000359

Research Sprint: Polkadex. This research sprint was undertaken as ... (n.d.). https://blog.openmesh.network/research-sprint-polkadex-533a67398c07?source=post_internal_links---------5-------------------------------

RH Goodall, LP Darras, & MA Purnell. (2015). Accuracy and precision of silicon based impression media for quantitative areal texture analysis. In Scientific reports. https://www.nature.com/articles/srep10800

Rust: Why Does Aleph Zero Use It? Podcast Key Takeaways. (2023). https://alephzero.org/blog/why-rust-podcast-key-takeaways/

S. Kutten. (1996). Scalable Fault Tolerance. In Conference on Current Trends in Theory and Practice of Informatics. https://www.semanticscholar.org/paper/e87b2a95d4eaac142e96d1f36369eead422d1418

S Ojog. (2021). The emerging world of decentralized finance. In Informatica Economica. https://revistaie.ase.ro/content/100/05%20-%20ojog.pdf

S. Pratten. (1997). The nature of transaction cost economics. In Journal of Economic Issues. https://www.tandfonline.com/doi/full/10.1080/00213624.1997.11505965

S. Shrivastava. (1987). A tutorial on the principles of fault tolerance. In Sadhana. https://link.springer.com/article/10.1007/BF02811309

scslab/speedex - GitHub. (n.d.). https://github.com/scslab/speedex

SM Solís. (2023). Zero Trust Chain A Design Pattern for Improved Interoperability and Security in Polkadot. In arXiv. https://arxiv.org/abs/2304.14730

SPEEDEX: A Scalable, Parallelizable, and Economically Efﬁcient ... (n.d.). https://www.scs.stanford.edu/~geoff/papers/speedex-2022.pdf

SPEEDEX: A Scalable, Parallelizable, and Economically Efficient ... (2025). https://www.researchgate.net/publication/355924957_SPEEDEX_A_Scalable_Parallelizable_and_Economically_Efficient_Digital_EXchange

SPEEDEX Configuration Proposal - Google Groups. (2022). https://groups.google.com/g/stellar-dev/c/OvgTxqjf1n4/m/Tu5auRM2BgAJ

SPEEDEX Transaction Accessibility - Google Groups. (n.d.). https://groups.google.com/g/stellar-dev/c/GPjHIYPdud8

Sperax Team. (2020). Sperax Blockchain: Secure BFT Consensus Protocol for Asynchronous Networks. https://www.semanticscholar.org/paper/5dfcc61a362aaf80372d3b4bf2ba3cc103c09038

Supra Partners #57 – SupraOracles partners with Aleph Zero, a privacy ... (n.d.). https://supra.com/news/supraoracles-partners-with-aleph-zero-a-privacy-enhancing-layer-1-with-powerful-scalability/

SX Wang. (2024). Meat the Future: The Patent Landscape of Cultivated Meat. https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/lndslid16&section=42

T Gong & A Kate. (2023). Order but Not Execute in Order. In arXiv. https://arxiv.org/abs/2302.01177

T Satheesh, R Sakthivel, & N Aravinth. (2024). Unified synchronization and fault‐tolerant anti‐disturbance control for synchronization of multiple memristor‐based neural networks. https://onlinelibrary.wiley.com/doi/abs/10.1002/rnc.7112

Tangem update: Aleph Zero. (2023). https://tangem.com/en/blog/post/update-four-point-nine/

The Aleph Zero ecosystem integrates with Ledger - Blockchain News. (2023). https://blockchaintechnology-news.com/news/the-aleph-zero-ecosystem-integrates-with-ledger/

The Aleph Zero Ecosystem Integrates with Ledger - Yahoo Finance. (2023). https://finance.yahoo.com/news/aleph-zero-ecosystem-integrates-ledger-120000515.html

The Common Whitepaper. Podcast Key Takeaways. - Aleph Zero Blog. (2023). https://alephzero.org/blog/the-common-whitepaper-podcast-key-takeaways/

The New Aleph Zero Roadmap. (2025). https://alephzero.org/blog/the-new-aleph-zero-roadmap/

The New Aleph Zero Roadmap - X. (2025). https://x.com/Aleph__Zero/status/1940100876879700411

The Ultimate Bridge: Benefits of Cross-Chain Technology | SecuX Blog. (2024). https://secuxtech.com/blogs/blog/the-ultimate-bridge-benefits-of-cross-chain-technology?srsltid=AfmBOorO-34ceFxzNWQsoSiEwr4woXA1oP9ri214zAg6XTUBsZxqW3ge

Timothy S Newman. (2021). Performance Comparison. In Satellite Formation Flying. https://www.semanticscholar.org/paper/8f672592f23fa77a623e9edd62ecadf3b2d188fe

Top Polkadot Projects 2025: 7 Best DOT DApps Shaping Web3! (n.d.). https://coinbureau.com/analysis/top-polkadot-projects/

Transactions Per Second (TPS) - DEV Community. (2023). https://dev.to/fromaline/transaction-per-second-tps-3f8b?comments_sort=latest

Transactions Per Second (TPS) in top blockchains | by Chainspect. (2023). https://medium.com/@chainspect_app/transactions-per-second-tps-in-top-blockchains-001d430dac2b

Transparent public document access - Aleph Zero. (n.d.). https://alephzero.org/applications/transparent-public-document-access

U. Blum, L. Dudley, F. Leibbrand, & Andreas Weiske. (2005). Transaktionskosten und Technologie. https://link.springer.com/chapter/10.1007/978-3-322-82618-3_3

Understanding Polkadex: A Trading Engine for Web3 and DeFi. (2021). https://academy.moralis.io/blog/understanding-polkadex-a-trading-engine-for-web3-and-defi

Understanding Polkadex: Polkadex 101 - Medium. (2021). https://medium.com/polkadex/understanding-polkadex-polkadex-101-97f8957bae88

V Dsouza, J Pronk, & C Peppelman. (2024). Densor: An Intraoral Battery-Free Sensing Platform. https://dl.acm.org/doi/abs/10.1145/3699746

Want to build on Aleph Zero? Here are some prerequisites to get ... (2023). https://medium.com/@elzucky/want-to-build-on-aleph-zero-here-are-some-prerequisites-to-get-from-the-ground-up-c3fec653415e

Weaver. (2002). Market and Application Analysis. https://linkinghub.elsevier.com/retrieve/pii/B9781856173971500046

WELCOME TO ALEPH ZERO | Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero

What is Aleph Zero? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/aleph-zero

What is Aleph Zero? (Aleph Zero Explanation, Consensus, AZERO ... (n.d.). https://www.iexplaincrypto.com/what-is-aleph-zero/

What is Aleph Zero? All You Need to Know About AZERO - Gate.com. (2023). https://www.gate.com/learn/articles/what-is-aleph-zero/836

What Is Aleph Zero (AZERO) - MEXC Blog. (2022). https://blog.mexc.com/aleph-zero/

What is Aleph Zero, the Complete Blockchain Guide - DappRadar. (2024). https://dappradar.com/blog/what-is-aleph-zero-the-complete-blockchain-guide

What is Cross-Chain Compatibility? - SoluLab. (n.d.). https://www.solulab.com/what-is-cross-chain-compatibility/

What Is Polkadex? | CoinMarketCap. (n.d.). https://coinmarketcap.com/academy/article/what-is-polkadex

What is Polkadex? | Polkadex Docs. (n.d.). https://docs.polkadex.ee/whatispolkadex/

What is Polkadex? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/polkadex

What Is Polkadex (PDEX)? All About PDEX Token - Coin98 Insights. (n.d.). https://coin98.net/what-is-polkadex-pdex

What Is The Fastest Blockchain And Why? Analysis of 43 Blockchains. (2021). https://alephzero.org/blog/what-is-the-fastest-blockchain-and-why-analysis-of-43-blockchains/

What makes Aleph Zero stand out among other crypto technologies? (2025). https://www.bydfi.com/en/questions/what-makes-aleph-zero-stand-out-among-other-crypto-technologies

Which blockchain is the fastest? - pontem.network. (n.d.). https://pontem.network/posts/which-blockchain-is-the-fastest

Whitepaper Update - Polkadex (PDEX) - CoinMarketCal. (2020). https://www.coinmarketcal.com/en/event/whitepaper-release-70913

Why Polkadex chose Polkadot - Medium. (2021). https://medium.com/polkadex/why-polkadex-polkadot-network-15141974a79b

Why we chose the Polkadot network | Polkadex Docs. (n.d.). https://docs.polkadex.ee/whyPolkadot/

Xiaoqin Feng, Jianfeng Ma, Yinbin Miao, Qian Meng, Ximeng Liu, Qi Jiang, & Hui Li. (2018). Pruneable sharding-based blockchain protocol. In Peer-to-Peer Networking and Applications. https://www.semanticscholar.org/paper/787076d20186f69283330e14722e5199a1eadf0a

Yuan Cheng, Xiaohui Hu, & Jianguo Zhang. (2019). An Improved Scheme of Proof-of-Stake Consensus Mechanism. In 2019 4th International Conference on Mechanical, Control and Computer Engineering (ICMCCE). https://ieeexplore.ieee.org/document/8969256/



Generated by Liner
https://getliner.com/search/s/5926611/t/86445906