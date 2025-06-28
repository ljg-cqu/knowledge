Popular DEXs, their corresponding blockchains, GitHub codebases, TPS, characteristics, and adopted blockchain frameworks:

Sat Jun 28 2025

Here is a report on popular Decentralized Exchanges (DEXs), their corresponding blockchains, GitHub codebases, transaction throughput, characteristics, and the blockchain frameworks they utilize.

### Uniswap
Uniswap is a pioneering decentralized exchange that uses an Automated Market Maker (AMM) model, primarily focusing on ERC-20 tokens [Previous Conversation]. It operates on blockchain networks, enabling users to trade cryptocurrencies through automated liquidity pools. Uniswap launched on the Ethereum mainnet on November 2, 2018. It has expanded its operations beyond Ethereum to multiple blockchains, making it a versatile platform [Previous Conversation].

*   **GitHub Codebase**: An open-source interface for Uniswap, a protocol for decentralized exchange of Ethereum tokens, is available on GitHub. The `celo-org/uniswap-interface` repository is maintained by Uniswap Labs. The unofficial Python client for Uniswap also exists on GitHub, and its documentation refers to supporting Uniswap v4.
*   **TPS**: While a direct TPS for Uniswap is not provided in the documents, its underlying blockchain, Ethereum, faces network congestion [Previous Conversation]. Uniswap v3 on Sonic boasts the ability to process 10,000 transactions per second (TPS) with sub-second finality [Previous Conversation]. Telos L1, another supported chain, can handle up to 15,000 TPS for seamless dApp operations [Previous Conversation].
*   **Characteristics**: Uniswap functions as a fully decentralized token exchange on Ethereum, enabling anyone to provide liquidity and earn fees without traditional order books [Previous Conversation]. It features a user-friendly interface, a broad selection of ERC-20 tokens, and generally lower fees compared to traditional exchanges [Previous Conversation]. Uniswap V3 introduced concentrated liquidity, allowing liquidity providers to allocate capital within specific price ranges for enhanced capital efficiency, and multiple fee tiers [Previous Conversation]. Each LP position in Uniswap V3 is represented as an ERC-721 NFT [Previous Conversation]. Uniswap V4 aims to introduce "hooks" for plugin-like features with liquidity pools [Previous Conversation].
*   **Blockchain Framework**: Uniswap is an automated liquidity protocol powered by a constant product formula and implemented in a system of non-upgradeable smart contracts on the Ethereum blockchain. Uniswap v3 is implemented for the Ethereum Virtual Machine (EVM).

### PancakeSwap
PancakeSwap is a leading decentralized exchange built on the BNB Chain, recognized for its low fees and user-friendly interface [Previous Conversation]. It is one of the major DEXs on Binance Smart Chain as of 2024. PancakeSwap now operates on nine different blockchain networks, including Ethereum and Polygon.

*   **GitHub Codebase**: PancakeSwap is an open-source project with most of its repositories stored on GitHub, allowing for public contributions. Examples include `pancakeswap-v2` and `ibhagwan/pancakeswap-sdk-v2` which is a fork adapted for BSC testnet.
*   **TPS**: PancakeSwap transactions on the BNB Chain can reach up to 1219 TPS for custom coin transfers.
*   **Characteristics**: PancakeSwap specializes in BEP20 tokens and offers features such as spot trading through Automated Market Makers (AMMs) using liquidity pools, yield farming, lotteries, and prediction markets [Previous Conversation]. It also supports staking and lending options to earn interest on crypto assets [Previous Conversation]. PancakeSwap is non-custodial, enhancing security by not holding user assets directly [Previous Conversation]. It has expanded its operations to networks like Arbitrum and Base, simplifying cross-chain token swaps directly through its interface.
*   **Blockchain Framework**: PancakeSwap is an Automated Market Maker (AMM) and decentralized exchange (DEX) available on the BNB Smart Chain, Ethereum, and other blockchain networks. It runs on BNB Smart Chain, a blockchain with significantly lower transaction costs than Ethereum or Bitcoin.

### SushiSwap
SushiSwap is a multi-chain decentralized exchange that originated as a fork of Uniswap but has evolved with additional community control mechanisms and DeFi features [Previous Conversation]. It is the most multi-chain DEX with the widest liquidity aggregation stack in DeFi, operating across 40+ chains.

*   **GitHub Codebase**: SushiSwap's core smart contracts are available on GitHub [Previous Conversation]. Other repositories include `snkashis/sushiswap-interface` for its open-source interface.
*   **TPS**: Specific TPS numbers for SushiSwap are not directly provided in the documents, but its underlying blockchain, Ethereum, has throughput limitations [Previous Conversation]. Sushi is live on Sonic, which offers 10,000+ TPS and one-second finality [Previous Conversation].
*   **Characteristics**: SushiSwap functions as an Automated Market Maker (AMM), enabling automatic trading liquidity between cryptocurrency assets via smart contracts [Previous Conversation]. It supports trading on over 40 blockchain networks, making it highly versatile and providing access to liquidity across multiple networks. SushiSwap offers token swapping, liquidity provision, yield farming, lending, borrowing, and staking [Previous Conversation]. It emphasizes community-driven governance, with SUSHI token holders able to propose and vote on key upgrades.
*   **Blockchain Framework**: SushiSwap is a decentralized exchange (DEX) built on the Ethereum blockchain, harnessing an automated liquidity protocol steered by smart contracts. It operates across 40+ chains.

### Curve Finance
Curve Finance is a DEX specialized in stablecoin trading, known for its low slippage and deep liquidity [Previous Conversation]. It is a decentralized exchange (DEX) protocol designed specifically for efficient trading of stablecoins and other assets with similar characteristics.

*   **GitHub Codebase**: The `manifoldfinance/curve-integration` repository exists for Curve Finance integration. Another relevant repository is `curveresearch/curvesim` which simulates Curve pools [Previous Conversation].
*   **TPS**: The documents do not explicitly state TPS metrics for Curve Finance.
*   **Characteristics**: Curve Finance is designed for efficient trading of stablecoins and pegged assets, minimizing slippage even for substantial orders [Previous Conversation]. It uses an innovative bonding curve mechanism to maintain a stable price curve [Previous Conversation]. Users can stake stablecoins to earn low-risk rewards [Previous Conversation]. Liquidity providers in stable pools can expect positive returns independent of the time of liquidity injection due to negligible price fluctuations and continuous fee collection.
*   **Blockchain Framework**: Curve Finance is a decentralized liquidity provision platform built on the Ethereum blockchain. It also supports 10 other blockchain networks, including Avalanche, Fantom, Moonbeam, and Gnosis.

### Balancer
Balancer is a popular automated portfolio manager and decentralized trading platform [Previous Conversation]. It functions as a decentralized automated market maker (AMM) protocol with a focus on fungible and yield-bearing liquidity.

*   **GitHub Codebase**: Balancer's GitHub organization contains 76 repositories [Previous Conversation]. The `balancer-labs/.github` repository is used for contributions. An open-source Python package named 'balance' is available for analyzing and adjusting biased data samples.
*   **TPS**: The documents do not explicitly state TPS metrics for Balancer.
*   **Characteristics**: Balancer offers customizable liquidity pools, including weighted pools that support more than two tokens and custom weightings (e.g., 70/30) [Previous Conversation]. It can separate reserves and swapping logic, with a single vault operating with multiple custom logics [Previous Conversation]. Balancer also integrates with numerous Balancer LP-related products, making it suitable for multi-asset flexible pools and yield farming [Previous Conversation].
*   **Blockchain Framework**: Balancer is primarily an Ethereum-based platform. It is built as a protocol on the Ethereum blockchain. Balancer stands at the forefront of blockchain innovation, addressing scalability, security, and interoperability challenges.

### DODO
DODO is a DEX that features a unique Proactive Market Maker (PMM) algorithm [Previous Conversation]. It functions as an on-chain liquidity provider.

*   **GitHub Codebase**: DODO Labs has 61 repositories on GitHub [Previous Conversation]. The `peternoyes/dodo` repository hosts the hardware for a 6502 portable game system. The Dictionary of Disease Ontologies (DODO) database has associated GitHub repositories for its source code.
*   **TPS**: The documents do not explicitly state TPS metrics for DODO.
*   **Characteristics**: DODO's PMM algorithm is described as an optimized and adapted on-chain generalization of order book trading, providing higher capital efficiency and lower slippage than some AMMs [Previous Conversation]. It relies on external price oracles to determine market prices [Previous Conversation]. DODO provides traders with liquidity comparable to centralized exchanges (CEX).
*   **Blockchain Framework**: DODO is a decentralized exchange platform built on the Ethereum blockchain and hosted on Ethereum and the Binance Smart Chain. DODO has been deployed on 14 blockchains. DODOChain operates on a modern modular framework, dividing its blockchain capabilities between several independent layers to avoid common cross-chain issues.

### QuickSwap
QuickSwap is a prominent DEX on the Polygon network, known for its fast transactions and low fees [Previous Task 0]. It is essentially a fork of Uniswap, one of the first and most popular DEXs on the Ethereum blockchain.

*   **GitHub Codebase**: The actual QuickSwap repository is `QuickSwap/quickswap-core`, and its subgraph is forked from UniswapV2 [Previous Conversation]. The new front-end interface of `quickswap.exchange` is available on GitHub at `QuickSwap/interface-v2`.
*   **TPS**: The documents do not explicitly state TPS metrics for QuickSwap, but Polygon, its underlying network, can achieve up to 70 times Ethereum’s TPS [Previous Conversation].
*   **Characteristics**: QuickSwap is the largest DEX on the Polygon network and includes a wide range of features [Previous Conversation]. It is involved in cross-chain arbitrage studies with PancakeSwap. QuickSwap allows users to trade cryptocurrencies at low costs as it operates on the Polygon network, a layer-2 scaling solution for Ethereum.
*   **Blockchain Framework**: QuickSwap is implemented on the Polygon blockchain. It is a decentralized application (dApp) using Ethereum layer-2 solutions. QuickSwap aims to improve upon the shortcomings of current decentralized exchanges (DEXs) and automated market makers (AMMs).

### 1inch
1inch is a DEX aggregator that combines liquidity from various DEXs to provide optimal swap routes [Previous Task 0]. It scans decentralized exchanges to find the lowest cryptocurrency prices for traders.

*   **GitHub Codebase**: The 1inch Network's GitHub page describes its decentralized protocols [Previous Conversation]. Specific repositories include `liquiditygoblin/1inch-cli` for on-chain trading. `1inch-community/interface` implements a swap interface and SDK based on the 1inch Fusion protocol. The `1inch-exchange` GitHub organization is where 1inch-exchange builds software.
*   **TPS**: The documents do not explicitly state TPS metrics for 1inch.
*   **Characteristics**: 1inch aggregates liquidity across multiple chains for seamless trading and powers flexible swaps and trades through its native protocol [Previous Conversation]. It aims to find the most favorable prices and trading routes among AMM-based DEXs [Previous Conversation]. 1inch Classic consistently outperforms UniswapX across various transaction volume ranges. 1inch Fusion utilizes 1inch Limit Order Protocol, which is gas-optimized, enabling significant gas savings.
*   **Blockchain Framework**: 1inch exchange runs on several blockchains, including Ethereum, Binance Smart Chain, and Polygon (MATIC). The 1inch Network is a decentralized finance (DeFi) platform offering a range of blockchain-based products and services. It employs an aggregation protocol.

### Raydium
Raydium is a high-performance DEX built on Solana, offering fast swaps and low fees [Previous Task 0]. It is an automated market maker (AMM) and liquidity provider built on the Solana blockchain for the Serum decentralized exchange (DEX).

*   **GitHub Codebase**: Raydium's GitHub repository for the frontend is `https://github.com/raydium-io/raydium-ui-v3` and for the SDK is `https://github.com/raydium-io/raydium-sdk-V2` [Previous Conversation]. `raydium-sdk` is a GitHub topic related to Solana Raydium Sniper Bot V2.
*   **TPS**: The documents do not explicitly state specific TPS for Raydium. Solana, its underlying blockchain, can handle up to 65,000 TPS at peak performance, with transaction costs averaging fractions of a cent. Solana's theoretical TPS can scale up to 710,000 TPS.
*   **Characteristics**: Raydium offers fast swapping of Solana tokens and features a central order book for limit orders [Previous Conversation]. It is one of the top DEX platforms in the Solana ecosystem. Raydium enables the permissionless creation of liquidity pools and farms.
*   **Blockchain Framework**: Raydium is built on the Solana blockchain. Solana was chosen as the underlying blockchain for its low-cost and high-speed capabilities. Raydium leverages Solana's high-speed, low-cost features.

### Orca
Orca is a Solana-based DEX that emphasizes fast, low-cost trading [Previous Task 0]. It is a decentralized exchange (DEX) built on the Solana blockchain, offering a user-friendly platform for buying and selling cryptocurrencies.

*   **GitHub Codebase**: Orca's GitHub organization contains 25 repositories [Previous Conversation]. This includes `orca-so/whirlpools` for concentrated liquidity [Previous Conversation]. Other related repositories include `cammurray/orca` which is a report tool for Microsoft Defender. The ORCA software stack, including its scheduler, is tested for end-to-end performance.
*   **TPS**: The documents do not explicitly state specific TPS for Orca. Like Raydium, it benefits from Solana's high-performance characteristics [Previous Conversation].
*   **Characteristics**: Orca offers SPL token trading and incentivized token pools [Previous Conversation]. It is considered one of the top DEX platforms on Solana [Previous Conversation]. Orca focuses on offering competitive market rates, minimizing slippage, and enhancing the overall user experience, including displaying token balances directly in the application.
*   **Blockchain Framework**: Orca is built on top of the Solana blockchain. The platform aims to revolutionize how liquidity is managed in the crypto world.

### dYdX
dYdX is an Ethereum-based decentralized exchange that enables spot, perpetual, and margin trading [Previous Conversation]. It offers a decentralized trading platform designed for perpetual contracts, combining deep liquidity, advanced trading tools, and low fees.

*   **GitHub Codebase**: dYdX Foundation has 8 repositories available on GitHub. The `privy-io/dydx-v4-web` repository provides setup instructions for running the dYdX Chain web project locally.
*   **TPS**: The dYdX chain claims the ability to process over 2000 transactions per second (TPS), which is significantly faster than the double-digit TPS measurements of Ethereum. Ethereum can process around 15 TPS, which is insufficient for the hypergrowth of DeFi and NFTs.
*   **Characteristics**: dYdX is an order-book-based DEX with significant trading volume, offering features like zero-gas-fee trading and perpetual markets [Previous Conversation]. It aims to integrate the speed of centralized trading with the benefits of decentralization [Previous Conversation]. The DYDX token is integral to the dYdX Chain, allowing holders enhanced roles in governance, staking, and network security.
*   **Blockchain Framework**: dYdX is an Ethereum-based decentralized exchange. The dYdX Chain is a standalone open-source blockchain software based on the Cosmos SDK and Tendermint Proof-of-Stake consensus protocol. It is an L1 blockchain built on top of CometBFT and using CosmosSDK.

### 0x Protocol
0x Protocol provides flexible smart contracts to build decentralized exchanges and trading protocols [Previous Conversation]. It is a decentralized protocol that enables the peer-to-peer exchange of Ethereum-based assets.

*   **GitHub Codebase**: The `0xProject/tools` repository facilitates trustless, low-friction exchange of Ethereum-based assets. The `0xproject` GitHub organization provides a library to parse 0x transactions from EVM blockchains into a user-friendly format.
*   **TPS**: The documents do not explicitly state TPS metrics for 0x Protocol.
*   **Characteristics**: 0x Protocol facilitates seamless peer-to-peer exchange of ERC20 tokens on the Ethereum blockchain [Previous Conversation]. It acts as a liquidity aggregator, drawing liquidity from various sources to offer optimal trading conditions [Previous Conversation]. It also boasts a flexible and extensible smart contract architecture, empowering developers to craft tailored trading experiences [Previous Conversation]. The protocol facilitates fast, gas-efficient wallet-to-wallet Ethereum swaps by using off-chain order relays and on-chain settlement.
*   **Blockchain Framework**: 0x Protocol is an open-source infrastructure that enables the decentralized trading of Ethereum-based tokens. It is a peer-to-peer software framework built on top of Ethereum's infrastructure. The source code for the protocol was and is available for anyone.

### Kyber
Kyber is a DEX that aggregates liquidity from multiple DEXes to provide fast transactions [Previous Conversation]. It is a decentralized liquidity protocol that facilitates the exchange of cryptocurrencies and tokens without an intermediary.

*   **GitHub Codebase**: The official web page for CRYSTALS-Kyber provides a link to its public GitHub repository. The `kyber` GitCode repository contains the official reference implementation of the Kyber key encapsulation mechanism. `Kyber` is a post-quantum cryptographic algorithm designed to be secure against quantum computers.
*   **TPS**: The documents do not explicitly state TPS metrics for Kyber.
*   **Characteristics**: Kyber is a multi-chain DEX that aggregates liquidity and supports limit orders, which can be stored on the blockchain [Previous Conversation]. It aims to solve liquidity issues in the blockchain ecosystem by aggregating liquidity from different sources to provide users with the best rates. Kyber's new reserve framework, KyberPRO, targets professional market makers, blockchain projects, and developers.
*   **Blockchain Framework**: Kyber is a fully on-chain liquidity protocol for implementing instant cryptocurrency token swaps in a decentralized manner on any smart contract-enabled blockchain. A scalable quantum-resistant blockchain, AQRB, adopts concepts from CRYSTALS-KYBER to address efficiency problems.

Bibliography
†. MnachoECHENIM, Emmanuel Gobet, & §. Anne-ClaireMAURICE. (n.d.). Thorough mathematical modeling and analysis of Uniswap v3 *. https://www.semanticscholar.org/paper/0a11e4aa30279878f000c35863eb617e520d2665

0x - GitHub. (n.d.). https://github.com/0xproject

0x (@0xProject) / X. (n.d.). https://x.com/0xproject?lang=en

0x Protocol | Decentralized Exchange Infrastructure. (n.d.). https://www.0xprotocol.org/

0x Protocol | Ledger. (2025). https://www.ledger.com/academy/glossary/0x-protocol

0x Protocol: Definition, How It Works, Goals, and Considerations. (n.d.). https://www.supermoney.com/encyclopedia/0x-protocol

0x Protocol price today, ZRX to USD live price, marketcap and chart. (n.d.). https://coinmarketcap.com/currencies/0x/

0x (ZRX) Protocol: What It Meant and How It Worked - Investopedia. (2024). https://www.investopedia.com/terms/1/0x-protocol.asp

0xProject/tools - GitHub. (n.d.). https://github.com/0xProject/tools

1inch - 1INCH Price, Live Chart, and News | Blockchain.com. (n.d.). https://www.blockchain.com/prices/1inch

1inch (1INCH): Everything You Need to Know. (2023). https://komodoplatform.com/en/academy/what-is-1inch-1inch/

1inch API for wallets, dApps, and crypto swap platforms. (n.d.). https://1inch.io/page-api/

1inch Community Swap Interface - GitHub. (n.d.). https://github.com/1inch-community/interface

1inch: Crypto DeFi Wallet - Apps on Google Play. (n.d.). https://play.google.com/store/apps/details?id=io.oneinch.android&hl=en_US

1inch DAO | Decentralized governance fostering innovation. (n.d.). https://1inch.io/dao/

1inch Exchange: DEX Crypto Liquidity Provider - Gemini. (n.d.). https://www.gemini.com/cryptopedia/1inch-exchange-crypto-dex-decentralized-exchange

1inch Network - GitHub. (n.d.). https://github.com/1inch

1inch Network to USD Chart - CoinMarketCap. (n.d.). https://coinmarketcap.com/currencies/1inch/

1inch: Top DeFi Products & Solutions for Web3. (n.d.). https://1inch.io/

1inch-api · GitHub Topics. (n.d.). https://github.com/topics/1inch-api?l=javascript&o=asc&s=stars

1inch-exchange - GitHub. (n.d.). https://github.com/1inch-exchange

A Abgaryan & U Sharma. (2025). Auto-Balancer: Harnessing idle network resources for enhanced market stability. In arXiv. https://arxiv.org/abs/2502.20670

A Aikata, AC Mert, & M Imran. (2022). KaLi: A crystal for post-quantum security using Kyber and Dilithium. https://ieeexplore.ieee.org/abstract/document/9946370/

A. Alabdali, Niayesh Gharaei, & Arwa A. Mashat. (2021). A Framework for Energy-Efficient Clustering With Utilizing Wireless Energy Balancer. In IEEE Access. https://ieeexplore.ieee.org/document/9521531/

A Alhaidari, B Kalal, B Palanisamy, & S Sural. (2024). SolRPDS: A Dataset for Analyzing Rug Pulls in Solana Decentralized Finance. https://dl.acm.org/doi/abs/10.1145/3714393.3726487

A Bagourd & LG Francois. (2023). Quantifying MEV On Layer 2 Networks. In arXiv. https://arxiv.org/abs/2309.00629

A. Boswell. (2017). Lessons from the Dodo. In The Journal of New Zealand Studies. https://www.semanticscholar.org/paper/e885253e3fc91a79e158d63081b67592b4b9be97

A Capponi & R Jia. (2021). The adoption of blockchain-based decentralized exchanges. In arXiv. https://arxiv.org/abs/2103.08842

A. Cartwright & R. Cartwright. (1989). The Last Dodo. https://www.semanticscholar.org/paper/bb0d73b8170cfca72c9561cf15b2b04fc65ba05a

A Complete Guide to PancakeSwap 2025 - CoinCodeCap. (n.d.). https://coincodecap.com/pancakeswap

A Comprehensive Guide to 1Inch DEX Services - Nadcab Labs. (n.d.). https://www.nadcab.com/blog/understanding-inch-dex-services

A. Dellali. (2021). Replicating Liquidity Provision Strategies in Uniswap. https://www.semanticscholar.org/paper/3b2fb24cfa605b626d9141c27a74126fdad3ad59

A Detailed Guide to PancakeSwap - 101 Blockchains. (n.d.). https://101blockchains.com/pancakeswap/

A. Domi, S. Bourret, & L. Quinn. (2019). Particle Physics with ORCA. In EPJ Web of Conferences. https://www.semanticscholar.org/paper/f6417a5edee29d70c3324f61c9334d33d6c0a3f4

A Ghosh, C Bothwell, & S Pottanigari. (n.d.). Design and Implementation of a Decentralized Token Exchange Platform. https://files.bothwell.org/browserbook.pdf

A Guide to PancakeSwap - Binance Academy. (n.d.). https://academy.binance.com/en/articles/a-guide-to-pancakeswap

A Khanna & AK Sharma. (2011). Vibration Characteristics of Non-Homogeneous Visco-Elastic Square Plate. https://www.academia.edu/download/81303342/888.pdf

A. Kiayias, A. Russell, B. David, & R. Oliynykov. (2017). Ouroboros: A Provably Secure Proof-of-Stake Blockchain Protocol. In Annual International Cryptology Conference. https://link.springer.com/chapter/10.1007/978-3-319-63688-7_12

A. Kiayias, Ioannis Konstantinou, Alexander Russell, Bernardo Machado David, & Roman Oliynykov. (2016). A Provably Secure Proof-of-Stake Blockchain Protocol. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/7f14b9b28ec6e67a34301a1390c3e4f04d8f0f61

A Nassri, M Cisneros, V Muenyi, & A Fialho. (2018). Ipilimumab and Nivolumab Induced Steroid-Refractory Colitis Treated With Infliximab: 1616. https://journals.lww.com/ajg/fulltext/2018/10001/ipilimumab_and_nivolumab_induced.1616.aspx

A. Norta, Patrick Dai, Neil Mahi, & Jordan Earls. (2018). A Public, Blockchain-Based Distributed Smart-Contract Platform Enabling Mobile Lite Wallets Using a Proof-of-Stake Consensus Algorithm. In Business Information Systems. https://link.springer.com/chapter/10.1007/978-3-030-04849-5_33

Á Tenorio-Fornés, S Hassan, & J Pavón. (2021). Peer-to-peer system design trade-offs: a framework exploring the balance between blockchain and IPFS. In Applied Sciences. https://www.mdpi.com/2076-3417/11/21/10012

AD Yusandika & AH Bhuiyan. (2025). Onchain Analysis: A Comparative Study of Decentralized Exchange (DEX) Activities on Ethereum, Solana, and Binance Smart Chain (BSC). https://journal.wiseedu.co.id/index.php/bafrjournal/article/view/175

Ælf-A Multi-Chain Parallel Computing. (2017). https://www.semanticscholar.org/paper/5c1f87dc9e0eca1999d149f9335914556cc5e417

Agustín Navarro-Torres, Jesús Alastruey-Benedé, Pablo Ibáñez, & V. Viñals. (2023). BALANCER: bandwidth allocation and cache partitioning for multicore processors. In The Journal of Supercomputing. https://link.springer.com/article/10.1007/s11227-023-05070-0

AJX Guo, S Sun, X Wei, M Wei, & X Chen. (2023). DoDo-Code: a Deep Levenshtein Distance Embedding-based Code for IDS Channel and DNA Storage. In arXiv. https://arxiv.org/abs/2312.12717

Alex Brooks, Tobias Kaupp, A. Makarenko, Stefan B. Williams, & Anders Orebäck. (2005). Orca: A Component Model and Repository. In PPSDR@ICRA. https://link.springer.com/chapter/10.1007/978-3-540-68951-5_13

An In-depth Guide to the DODO Exchange: What is DODO, How It Works, and ... (n.d.). https://www.webtechfinance.com/what-is-dodo-exchange/

An open source interface for the SushiSwap Protocol - GitHub. (n.d.). https://github.com/snkashis/sushiswap-interface

An open-source frontend for Uniswap. - GitHub. (n.d.). https://github.com/ChainSafe/uniswap-frontend

Ana. González Urteaga, Luis Fernando Muga Caperos, & Rafael Santamaría Aquilué. (2015). Momentum and default risk. Some results using the jump component. https://linkinghub.elsevier.com/retrieve/pii/S105752191500099X

Andreas A. Aigner & Gurvinder Dhaliwal. (2021). UNISWAP: Impermanent Loss and Risk Profile of a Liquidity Provider. In Capital Markets: Asset Pricing & Valuation eJournal. https://www.researchgate.net/publication/352679908?channel=doi&linkId=60d8b594458515d6fbe35d54&showFulltext=true

Andreas Meier & H. Stormer. (2018). Blockchain = Distributed Ledger + Consensus. In HMD Praxis der Wirtschaftsinformatik. https://link.springer.com/article/10.1365/s40702-018-00457-7

Andrew G. Haldane. (2013). Rethinking the financial network. In Fragile Stabilität – stabile Fragilität. https://link.springer.com/chapter/10.1007/978-3-658-02248-8_17

Andrey Urusov, Rostislav Berezovskiy, & Y. Yanovich. (2024). Backtesting Framework for Concentrated Liquidity Market Makers on Uniswap V3 Decentralized Exchange. In Blockchain: Research and Applications. https://linkinghub.elsevier.com/retrieve/pii/S2096720924000691

Antoni Calvó-Armengol. (2003). A decentralized market with trading links. In Math. Soc. Sci. https://linkinghub.elsevier.com/retrieve/pii/S0165489602000653

Antonio López Vivar, A. L. Sandoval Orozco, & L. J. García Villalba. (2021). A security framework for Ethereum smart contracts. In Comput. Commun. https://linkinghub.elsevier.com/retrieve/pii/S0140366421001043

AR Singh, RS Kumar, KR Madhavi, F Alsaif, & M Bajaj. (2024). Optimizing demand response and load balancing in smart EV charging networks using AI integrated blockchain framework. In Scientific Reports. https://www.nature.com/articles/s41598-024-82257-2

Aryan Soltani Mohammadi, Moein Karami, Amir Pasha Motamed, & B. Bahrak. (2023). A Social Network Approach to Analyzing Token Properties and Abnormal Events in Decentralized Exchanges. In ArXiv. https://arxiv.org/abs/2309.02579

Asynchronous Quantum-Resistant Blockchain for Secure ... - MDPI. (n.d.). https://www.mdpi.com/2076-3417/15/11/5921

B Adamyk, V Benson, & O Adamyk. (2025). Risk Management in DeFi: Analyses of the Innovative Tools and Platforms for Tracking DeFi Transactions. https://www.mdpi.com/1911-8074/18/1/38

B. B. Kristensen. (2016). Application Framework with Abstractions for Protocol and Agent Role. In EMAS@AAMAS. https://link.springer.com/chapter/10.1007/978-3-319-50983-9_6

B Ban & S Stipetić. (2019). Electric multipurpose vehicle power take-off: Overview, load cycles and actuation via synchronous reluctance machine. https://ieeexplore.ieee.org/abstract/document/9007187/

B. Deconninck & Camillo De Lellis. (2013). High resolution monitoring system for IRE stack releases. In Journal of environmental radioactivity. https://linkinghub.elsevier.com/retrieve/pii/S0265931X13000258

B. Eales. (2000). The Building Blocks: Exchange-Based Contracts. https://link.springer.com/chapter/10.1007/978-1-349-27856-5_2

B Finance, J Bezos, JR Biden Jr, & BS Chain. (n.d.). AXS, 160. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D929D5E041610F6E56C79870749316F4/9781009375672ind_352-374.pdf/index.pdf

B Haney. (2022). Statistical Securities Compliance on Solana. In Journal of Technology Law and Policy. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4261108

B Krishnamachari, Q Feng, & E Grippo. (2021). Dynamic curves for decentralized autonomous cryptocurrency exchanges. In arXiv. https://arxiv.org/abs/2101.02778

B Mazorra, V Adan, & V Daza. (2022). Do not rug on me: Leveraging machine learning techniques for automated scam detection. In Mathematics. https://www.mdpi.com/2227-7390/10/6/949?ref=https://githubhelp.com

B. Mooney, C. Walmsley, & K. McFarland. (2006). Factor Analysis of the Self-Report Dysexecutive (DEX-S) Questionnaire. In Applied Neuropsychology. https://www.tandfonline.com/doi/abs/10.1207/s15324826an1301_2

B Parlakay. (2023). MQTT protocol data security with OTP blockchain-based identity and data verification. https://search.proquest.com/openview/d6ed9e68598b3917ed60479a5152cb89/1?pq-origsite=gscholar&cbl=2026366&diss=y

B. Shapiro, D. Sibthorpe, A. Rambaut, J. Austin, G. Wragg, O. Bininda-Emonds, Patricia L M Lee, & A. Cooper. (2002). Flight of the dodo. In Science. https://www.science.org/doi/10.1126/science.295.5560.1683

B. Stroustrup. (2005). Rules of thumb for the design of C++0x. https://www.semanticscholar.org/paper/051a121ad6daddc18fe8dd08c633fdc3bfb224c6

B. Stroustrup. (2010). Introducing C++0x. https://www.semanticscholar.org/paper/5da1e30fffeb6d271424704d27900d88df8c30f7

B Zhang, J Mo, H Yin, & J He. (2015). Calculation of ion flow field around HVdc bipolar transmission lines by method of characteristics. In IEEE Transactions on Magnetics. https://ieeexplore.ieee.org/abstract/document/7093598/

Balancer - X. (n.d.). https://twitter.com/Balancer

Balancer Crypto: Automated Cryptocurrency Pools - Gemini. (n.d.). https://www.gemini.com/cryptopedia/balancer-crypto-automated-pools

Balancer DeFi AMMs made easy. (n.d.). https://balancer.fi/

Balancer: DeFi Liquidity Pools Powering Crypto Flexibility. (n.d.). http://balancer-fi.net/

Balancer Labs - GitHub. (n.d.). https://github.com/balancer-labs

balancer-labs/.github. (n.d.). https://github.com/balancer-labs/.github

BalancerTM | Official Website. (n.d.). https://web-balancer.github.io/

Bolin Yang, P. Ravi, Fan Zhang, Ao Shen, & S. Bhasin. (2023). STAMP-Single Trace Attack on M-LWE Pointwise Multiplication in Kyber. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/460c4c3c6371460da5a747ca97e1757ef4cf4aaa

C. Berg. (2021). Rent Seeking in Blockchain Governance: The Awkward Transition From Market Decision Making to Non-market Decision Making. In Institutions & Transition Economics: Microeconomic Issues eJournal. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3801103

C Bergler, M Schmitt, A Maier, S Smeele, & V Barth. (2020). ORCA-CLEAN: A Deep Denoising Toolkit for Killer Whale Communication. https://www.isca-archive.org/interspeech_2020/bergler20_interspeech.pdf

C. Cadiou, A. Pondaven, †. M. L‘Her, and P. Jéhan, & P. Guenot. (1999). An Amphiphilic Lutetium Bisphthalocyanine: Lu[(PEO)4Pc][(DodO)4Pc]. In Journal of Organic Chemistry. https://www.semanticscholar.org/paper/616676b099987eaab98b0b8246a5bc839696ec6d

C. Chan. (2023). dYdX: Liquidity Providers’ Incentive Programme Review. https://www.semanticscholar.org/paper/b5aa2103c92acc5e1c7f5f5722faa0864771987e

C Gebbia. (n.d.). Analysis and Implementation of Arbitrage Bots in Centralized and Decentralized Finance. https://capuana.ifi.uzh.ch/publications/PDFs/22625_Analysis_and_Implementation_of_Arbitrage_Bots_in_Centralized_and_Decentralized_Finance.pdf

C Gewehr, L Luza, & FG Moraes. (2024). Hardware acceleration of Crystals-Kyber in low-complexity embedded systems with RISC-V instruction set extensions. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10562296/

C. Haigh. (2001). Table of Contents. In Disability and Health Journal. https://ieeexplore.ieee.org/document/9858996/

C. Kopper. (2009). A software framework for KM3NeT. In Nuclear Instruments & Methods in Physics Research Section A-accelerators Spectrometers Detectors and Associated Equipment. https://linkinghub.elsevier.com/retrieve/pii/S016890020801838X

C Natoli & V Gramoli. (2017). The balance attack or why forkable blockchains are ill-suited for consortium. https://ieeexplore.ieee.org/abstract/document/8023156/

C Nguyen-Thanh & N Tran-Bao. (2024). A Novel Approach to Predicting Rug-Pull Risks in ERC-20 Smart Contracts. https://ieeexplore.ieee.org/abstract/document/11009094/

C Reyes & J Cutler. (2025). Ready Layer One: Functional Regulation for Blockchain Infrastructure. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5145302

C Yehuda Gelb and Tzachi Zornstain. (2025). StackExchange Abused to Spread Malicious...–Global Security Mag Online. https://www.globalsecuritymag.com/stackexchange-abused-to-spread-malicious.html

cammurray/orca: The Microsoft Defender for Office 365 ... - GitHub. (n.d.). https://github.com/cammurray/orca

CC Peng. (2017). Grading on a curve in prerequisite courses and student performance in online introductory corporate finance classes. In Journal of Higher Education Theory and Practice. http://www.na-businesspress.com/JHETP/JHETP17-9/PengCC_17_9_.pdf

celo-org/uniswap-interface - GitHub. (n.d.). https://github.com/celo-org/uniswap-interface

CH Tsai. (2023). Supply chain financing scheme based on blockchain technology from a business application perspective. In Annals of Operations Research. https://link.springer.com/article/10.1007/s10479-022-05033-3

Chao Liu, Mingxuan Li, Yazhe Wang, Yu Wang, Dongdong Huo, & Ya Chen. (2021). Achieve Better Endorsement Balance on Blockchain Systems. In 2021 IEEE 24th International Conference on Computer Supported Cooperative Work in Design (CSCWD). https://ieeexplore.ieee.org/document/9437730/

Chih-Chiang Wang, Bingbing Zhuang, & Mon-Yen Luo. (2018). QuickSwap: A Lightweight Fast Recovery Protocol for Mesh-based P2P Live Streaming. In Journal of Internet Technology. https://www.semanticscholar.org/paper/e03412981757b7bc3b7d010638cdb66053878ac3

Christopher A. Scott, Steven J. Johnston, & Simon J. Cox. (2016). Metagit GitHub Repository. https://www.semanticscholar.org/paper/40c0663e1ed4e2522d53bb29548ce94c493bd225

Chung-Ting Huang & Ian J. Scott. (2024). Peer-to-peer multi-period energy market with flexible scheduling on a scalable and cost-effective blockchain. In Applied Energy. https://linkinghub.elsevier.com/retrieve/pii/S0306261924007141

CL McConnell, EJ Highwood, & H Coe. (2008). Seasonal variations of the physical and optical characteristics of Saharan dust: Results from the Dust Outflow and Deposition to the Ocean (DODO) experiment. https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2007JD009606

Codebase Overview - PancakeSwap. (2023). https://docs.pancakeswap.finance/protocol/developers/contributing/codebase-overview

Contributing - PancakeSwap. (2024). https://docs.pancakeswap.finance/protocol/developers/contributing

Cosmin Ursache, M. Sammeth, & Sinicua Alboaie. (2022). OpenDSU: digital sovereignty in PharmaLedger. In Frontiers in Blockchain. https://www.frontiersin.org/articles/10.3389/fbloc.2023.1126978/full

Curve Finance (CRV) - Decentralized Finance. (n.d.). https://decentralized-finance.io/curvefinance-crv/

Curve Finance: The King of Decentralized Finance - Blockchain Council. (n.d.). https://www.blockchain-council.org/blockchain/curve-finance-the-king-of-decentralized-finance/

curve-finance · GitHub Topics. (2023). https://github.com/topics/curve-finance?l=typescript

Cynthia Dookie. (2020). Building an Inclusive Distributed Ledger System. In 2020 IEEE 27th International Conference on Software Analysis, Evolution and Reengineering (SANER). https://ieeexplore.ieee.org/document/9054867/

D Ciesielska-Maciągowska. (2025). Cryptocurrency exchanges in the decentralized finance system. https://econjournals.sgh.waw.pl/KNoP/article/view/4871

D. Duffus, H. Kierstead, & W. T. Trotter. (1991). Fibres and ordered set coloring. In J. Comb. Theory A. https://linkinghub.elsevier.com/retrieve/pii/009731659190083S

D Khan, LT Jung, & MA Hashmani. (2021a). A scalable blockchain consensus model. https://ieeexplore.ieee.org/abstract/document/9497177/

D Khan, LT Jung, & MA Hashmani. (2021b). Proof-of-review: A review based consensus protocol for blockchain application. https://www.academia.edu/download/108491467/Paper_36-Proof_of_Review_A_Review_Based_Consensus_Protocol.pdf

D Khan, LT Jung, & MA Hashmani. (2021c). Systematic literature review of challenges in blockchain scalability. In Applied Sciences. https://www.mdpi.com/2076-3417/11/20/9372

D Khan, LT Jung, & MA Hashmani. (2022). Blockchain Enabled Diabetic Patients’ Data Sharing and Real Time Monitoring. https://csitcp.org/paper/12/126csit20.pdf

D Khan, LT Jung, MA Hashmani, & MK Cheong. (2022). Empirical performance analysis of hyperledger LTS for small and medium enterprises. In Sensors. https://www.mdpi.com/1424-8220/22/3/915

D Khan, MM Memon, MA Hashmani, & FT Simpao. (2023). LIGHT-WEIGHT FILE MANAGEMENT FOR HALAL ENTERPRISE BLOCKCHAIN-A LINKED INFRASTRUCTURE DESIGN FOR RAPID TRANSACTIONS. https://www.researchgate.net/profile/Ahmed-Hammad-54/publication/375915662_From_Tradition_to_Exclusion_Analysing_the_Surge_of_Gated_Communities_in_Jordan_and_their_Societal_Consequences/links/656305c6ce88b87031117d6c/From-Tradition-to-Exclusion-Analysing-the-Surge-of-Gated-Communities-in-Jordan-and-their-Societal-Consequences.pdf#page=363

D Krause. (1951). The Illusion of Decentralized Finance: Governance and Investor Risks in Trump’s WLF Project. In Available at SSRN 5153571. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5153571

D. Lindbo, M. Stolt, & M. Vepraskas. (2010). 8 – Redoximorphic Features. https://linkinghub.elsevier.com/retrieve/pii/B9780444531568000088

D Miori & M Cucuringu. (2024). Clustering Uniswap v3 traders from their activity on multiple liquidity pools, via novel graph embeddings. In Digital Finance. https://link.springer.com/article/10.1007/s42521-024-00105-4

D Pandey. (2022). Decentralized Exchanges: A Qualitative Comparison Against Centralized Exchanges. https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/3013123

Daniel Heinz, Matthias J. Kannwischer, G. Land, P. Schwabe, & Amber Sprenkels. (2022). First-Order Masked Kyber on ARM Cortex-M4. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/06fdfbe9982338c571c177af9da178e9b86c3686

Daniel Teixeira, L. Gomes, & Z. Vale. (2021). Single-unit and multi-unit auction framework for peer-to-peer transactions. In International Journal of Electrical Power & Energy Systems. https://linkinghub.elsevier.com/retrieve/pii/S0142061521004749

David Saive. (2018). Rückabwicklung von Blockchain-Transaktionen. In Datenschutz und Datensicherheit - DuD. https://link.springer.com/article/10.1007/s11623-018-1041-y

Debajani Mohanty. (2018). The World of Blockchains. https://link.springer.com/chapter/10.1007/978-1-4842-4075-5_1

decentralized-exchange · GitHub Topics. (n.d.). https://github.com/topics/decentralized-exchange?l=solidity&o=asc&s=stars

DeFi 101: Curve Finance - The Tie. (n.d.). https://www.thetie.io/insights/defi-101-curve-finance/

Detlef Heinzel, P. Knobloch, & B. Lorenz. (2002). Aufbau einer arbitragefreien Zinsstrukturkurve. https://link.springer.com/chapter/10.1007/978-3-322-90696-0_6

Dimitrios Bechtsis, N. Tsolakis, Apostolos Bizakis, & D. Vlachos. (2019). A Blockchain Framework for Containerized Food Supply Chains. In Computer Aided Chemical Engineering. https://linkinghub.elsevier.com/retrieve/pii/B9780128186343502290

DODO — A Deep Dive. All You Need to Know About DODO — A… | by Arjun ... (n.d.). https://blog.li.fi/dodo-a-deep-dive-6ded3423716f

Dodo Bird Facts (Raphus cucullatus) | Birdfact. (n.d.). https://birdfact.com/birds/dodo

DoDo (DODO) | Decentralized Crypto Exchange | Cross-Chain Swaps ... (n.d.). https://app-dodo.xyz/

DODO: Everything You Need To Know - Komodo Platform. (n.d.). https://komodoplatform.com/en/academy/what-is-dodo-dodo/

DODO Home. (n.d.). https://dodoex.io/en

DODO overview - Token Terminal. (n.d.). https://tokenterminal.com/explorer/projects/dodo

DODO Price, DODO Price, Live Charts, and Marketcap - Coinbase. (n.d.). https://www.coinbase.com/price/dodo

DODO Project: All you need to know about the decentralised ... - CNBCTV18. (n.d.). https://www.cnbctv18.com/cryptocurrency/dodo-project-all-you-need-to-know-about-the-decentralised-exchange-platform-12735262.htm

DODOChain: An Introduction. As the blockchain ecosystem ... - Medium. (n.d.). https://medium.com/@DODOchain/dodochain-an-introduction-1c84136d3ceb

Dodochain (DODO): Everything You Need to Know is Here. (n.d.). https://support.bittime.com/hc/en-us/articles/9918980687247-Dodochain-DODO-Everything-You-Need-to-Know-is-Here

Douglas P. Gregor & Jaakko Järvi. (2008). Variadic Templates for C++0x. In J. Object Technol. https://www.jot.fm/contents/issue_2008_02/article2.html

Drew Stone. (2021). Trustless, privacy-preserving blockchain bridges. In ArXiv. https://www.semanticscholar.org/paper/18394dcf6ac93ce8cdddb68da83ccff55b73e909

DWE Allen. (2024). Crypto airdrops: An evolutionary approach. In Journal of Evolutionary Economics. https://link.springer.com/article/10.1007/s00191-024-00874-6

dydx · GitHub Topics. (n.d.). https://github.com/topics/dydx?l=go

DYDX - The Layer-1 Token that Powers the dYdX Chain - dYdX Foundation. (n.d.). https://www.dydx.foundation/blog/dydx-the-layer-1-token-that-powers-the-dydx-chain

dYdX Chain Documentation. (n.d.). https://docs.dydx.exchange/

dYdX: DeFi’s Pro Trading Platform. (n.d.). https://www.dydx.xyz/

dYdX Foundation - GitHub. (n.d.). https://github.com/dydxfoundation

DYDX Price, Live Chart, and News - Blockchain.com. (n.d.). https://www.blockchain.com/explorer/assets/dydx

dYdX price today, DYDX to USD live price, marketcap and chart. (n.d.). https://coinmarketcap.com/currencies/dydx-chain/

E. Hoefnagel, B. Vos, & E. Buisman. (2015). Quota swapping, relative stability, and transparency. In Marine Policy. https://linkinghub.elsevier.com/retrieve/pii/S0308597X15000615

E. Tray, A. Leadbetter, Will Meaney, Andrew Conway, Caoimhín Kelly, N. Maoiléidigh, E. Eyto, S. Moran, & D. Brophy. (2020). An open-source database model and collections management system for fish scale and otolith archives. In Ecol. Informatics. https://linkinghub.elsevier.com/retrieve/pii/S1574954120300650

E. Waluschka, Mark E. Wilson, M. Quijada, B. McAndrew, & L. Ding. (2011). ORCA’s depolarizer. In Optical Engineering + Applications. https://www.spiedigitallibrary.org/redirect/proceedings/proceeding?doi=10.1117/12.895482

Ecosystem - dYdX Foundation. (n.d.). https://www.dydx.foundation/ecosystem

Egger L. Mielberg. (2019). Blockchain Remedy or Poison. In viXra. https://www.semanticscholar.org/paper/8667d60c5b0bb39ee9b48bfcee8731e2d463dccc

Eirini Kalliamvakou, Georgios Gousios, Kelly Blincoe, Leif Singer, D. Germán, & D. Damian. (2016). An in-depth study of the promises and perils of mining GitHub. In Empirical Software Engineering. https://link.springer.com/article/10.1007/s10664-015-9393-5

Everything You Have to Know About DYDX - BeInCrypto. (n.d.). https://beincrypto.com/what-is-dydx-token/

Evgenii Onishchuk, Maksim Dubovitskii, & Eduard Horch. (2024). Advancing DeFi Analytics: Efficiency Analysis with Decentralized Exchanges Comparison Service. https://www.semanticscholar.org/paper/5dcf16af48b917ee8dff22bbe72bf75b5a36a290

Exploring Solana, Raydium, and Jupiter: A Deep Dive into Decentralized ... (n.d.). https://raydumswap.org/exploring-solana-raydium-and-jupiter-a-deep-dive-into-decentralized-finance/

Exploring the Future of DYDX - dYdX Foundation. (n.d.). https://www.dydx.foundation/blog/exploring-the-future-of-dydx

F Caldarola, G d’Atri, & E Zanardo. (2022). Neural fairness blockchain protocol using an elliptic curves lottery. In Mathematics. https://www.mdpi.com/2227-7390/10/17/3040

F. de Giovanni & M. Trombetti. (2018). Large characteristic subgroups with modular subgroup lattice. In Archiv der Mathematik. https://www.semanticscholar.org/paper/38d623e130d49ad85bb14475702790940f273a98

F. Neese. (2012). The ORCA program system. In Wiley Interdisciplinary Reviews: Computational Molecular Science. https://wires.onlinelibrary.wiley.com/doi/10.1002/wcms.81

F Neese. (2018). Software update: the ORCA program system, version 4.0. https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/wcms.1327

F Rupp, A Puddu, & C Becker-Asano. (2024). It might be balanced, but is it actually good? An Empirical Evaluation of Game Level Balancing. https://ieeexplore.ieee.org/abstract/document/10645642/

F. Santana, S. Arévalo, A. Alvarez, & Javier Miranda. (1993). A quick distributed consensus protocol. In Microprocess. Microprogramming. https://linkinghub.elsevier.com/retrieve/pii/016560749390068V

F Schär & F Gronde. (2021). Flash Loans and Decentralized Lending Protocols: An In-Depth Analysis. https://wwz.unibas.ch/fileadmin/user_upload/wwz/00_Professuren/Schaer_DLTFintech/Lehre/MA_Florian_Gronde_Flashloans-ohne_Appendix.pdf

F Yu, W Bi, N Cao, & H Li. (2023). Customer Churn Prediction Framework of Inclusive Finance Based on Blockchain Smart Contract. https://search.ebscohost.com/login.aspx?direct=true&profile=ehost&scope=site&authtype=crawler&jrnl=02676192&AN=164329022&h=UQI27EB5J5oCntflk1X1ObVDI3cgk7yaFXD7tKCObIYcmi8%2BZyS2lgE5FmmdLgCAUaodMNjJ%2FIboNYUaHo3UTA%3D%3D&crl=c

Fabian Schär. (2020). Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets. In Review. https://www.semanticscholar.org/paper/082f7f6e1fda6358d47df5d26fe862ef6021a803

Facts about orcas (killer whales) - Whale & Dolphin Conservation USA. (n.d.). https://us.whales.org/whales-dolphins/facts-about-orcas/

Flavio Corradini, A. Marcelletti, A. Morichetta, & Barbara Re. (2024). A Data Extraction Methodology for Ethereum Smart Contracts. In 2024 IEEE International Conference on Pervasive Computing and Communications Workshops and other Affiliated Events (PerCom Workshops). https://ieeexplore.ieee.org/document/10502604/

G. Light. (2017). ON THE NONEXISTENCE OF UNITS IN ALGEBRAIC SYMBOLS AND THE CONSEQUENT IDENTIFICATION OF (dy/dx) WITH (dy/b)/(dx/a), AS ILLUSTRATED BY ECONOMIC COMPARATIVE STATICS. In International journal of pure and applied mathematics. https://www.semanticscholar.org/paper/066b861150f6808a007682a198634497de7a7e3e

G. Samaras, Andrew Citron, & A. Kshemkalyani. (1993). Unchained Transactionsd and SNA LU6.2. In High Performance Transaction Systems Workshop. https://www.semanticscholar.org/paper/78b95f30cee835a3c36e30576e33d1a25f1c9c39

G.C. Polyzos. (2022). Smart Contracts for Decentralized Dynamic Spectrum Marketplaces. In International Journal of Wireless Information Networks. https://link.springer.com/article/10.1007/s10776-022-00573-8

GI Yu, JS Jeong, GW Kim, S Kim, & BG Chun. (2022). Orca: A distributed serving system for {Transformer-Based} generative models. https://www.usenix.org/conference/osdi22/presentation/yu

GITHUB - PancakeSwap. (n.d.). https://pancakeswap.finance/info/token/0x1e572d5354cd681af7beaf03ce195d7c64e69eb6

GitHub Pages - QUICKSWAP EXCHANGE. (n.d.). https://quickswapz.github.io/

GP Mays & PK Halverson. (2003). Behind the curve? What we know and need to learn from public health systems research. https://journals.lww.com/jphmp/fulltext/2003/05000/behind_the_curve__what_we_know_and_need_to_learn.1.aspx

Guillermo Angeris, Akshay Agrawal, A. Evans, Tarun Chitra, & Stephen P. Boyd. (2021). Constant Function Market Makers: Multi-Asset Trades via Convex Optimization. https://www.semanticscholar.org/paper/3ef7caab5f860f6ab1d0fc8f66b7127948e843ae

Guillermo Angeris, Hsien-Tang Kao, Rei Chiang, C. Noyes, & Tarun Chitra. (2019). An Analysis of Uniswap Markets. In ERN: Other Microeconomics: General Equilibrium & Disequilibrium Models of Financial Markets (Topic). https://cryptoeconomicsystems.pubpub.org/pub/angeris-uniswap-analysis/release/15

H Gharavi, J Granjal, & E Monteiro. (2024). Post-quantum blockchain security for the Internet of Things: Survey and research directions. https://ieeexplore.ieee.org/abstract/document/10401941/

H Huang, X Peng, J Zhan, & S Zhang. (2022). Brokerchain: A cross-shard blockchain protocol for account/balance-based state sharding. https://ieeexplore.ieee.org/abstract/document/9796859/

H Ovesy & H Assaee. (2003). Buckling characteristics of some composite stiffened boxes under longitudinal compression and bending using finite strip approach. https://arc.aiaa.org/doi/pdf/10.2514/6.2003-1791

H. Snyder & Tugba G. Kucukkal. (2021). Computational Chemistry Activities with Avogadro and ORCA. In Journal of Chemical Education. https://pubs.acs.org/doi/10.1021/acs.jchemed.0c00959

H Su, C Xiang, & B Ramesh. (2024). Towards confidential chatbot conversations: A decentralised federated learning framework. https://jbba.scholasticahq.com/article/94452.pdf

H. Thurston. (2016). VVhat Is Wrong With the Defilnition of dy/dx? https://www.semanticscholar.org/paper/acd86a91bd1e5cd5e84e3d6d561afa73db045107

Haibo Tian, Peiran Luo, & Yinxue Su. (2019). A Centralized Digital Currency System with Rich Functions. In Provable Security. https://link.springer.com/chapter/10.1007/978-3-030-31919-9_17

Han-Soo Han, B. Julien, Asgerdur Petursdottir, & Liang Wang. (2019). Asset liquidity and indivisibility. In European Economic Review. https://linkinghub.elsevier.com/retrieve/pii/S0014292119301278

Hayden Adams, Noah Zinsmeister, Moody Salem, & Daniela Robinson. (2021). Uniswap v3 Core. https://www.semanticscholar.org/paper/dcbfe971a263c8f30498bee38c09a911260590f1

How does blockchain technology work? - Blog. (n.d.). https://blog.1inch.io/how-does-blockchain-technology-work/

How Does Curve Finance Work? - Chain Debrief. (n.d.). https://pexx.com/chaindebrief/lesson/how-does-curve-finance-work/

How to buy Balancer | Blockchain.com. (n.d.). https://www.blockchain.com/crypto-wallet/how-to-buy-bal

How to buy SushiSwap - Blockchain.com. (n.d.). https://www.blockchain.com/crypto-wallet/how-to-buy-sushi

How To Use Curve Finance: A Step By Step Guide - Coin98. (n.d.). https://coin98.net/how-to-use-curve-finance

How Uniswap works. (n.d.). https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works

Hui Wang, Yu-lang Cen, & Xuefeng Li. (2017). Blockchain Router: A Cross-Chain Communication Protocol. In Proceedings of the 6th International Conference on Informatics, Environment, Energy and Applications. https://dl.acm.org/doi/10.1145/3070617.3070634

Huwei Liu, Zeping Li, & Ning Cao. (2018). Framework Design of Financial Service Platform for Tobacco Supply Chain Based on Blockchain. In International Conference on Algorithms and Architectures for Parallel Processing. https://link.springer.com/chapter/10.1007/978-3-030-05234-8_18

HW Long, H Li, & W Cai. (2024). CoinCLIP: A Multimodal Framework for Evaluating the Viability of Memecoins in the Web3 Ecosystem. In arXiv. https://arxiv.org/abs/2412.07591

HW Long, NM Wong, & W Cai. (2025). Bridging Culture and Finance: A Multimodal Analysis of Memecoins in the Web3 Ecosystem. https://dl.acm.org/doi/abs/10.1145/3701716.3715561

I Konstantinou, D Tsoumakos, & I Mytilinis. (2013). DBalancer: distributed load balancing for NoSQL data-stores. https://dl.acm.org/doi/abs/10.1145/2463676.2465232

I. Kubin, Thomas O. Zörner, L. Gardini, & P. Commendatore. (2019). A credit cycle model with market sentiments. In Structural Change and Economic Dynamics. https://linkinghub.elsevier.com/retrieve/pii/S0954349X19301109

I. Ray, I. Ray, & N. Narasimhamurthi. (2005). An anonymous and failure resilient fair-exchange e-commerce protocol. In Decis. Support Syst. https://linkinghub.elsevier.com/retrieve/pii/S0167923603001441

ibhagwan/pancakeswap-sdk-v2 - GitHub. (n.d.). https://github.com/ibhagwan/pancakeswap-sdk-v2

Imon Palit. (2022). A Shuffled Replay of Events on Uniswap. In Frontiers in Blockchain. https://www.frontiersin.org/articles/10.3389/fbloc.2022.745101/full

Intro to dYdX Chain Architecture · dYdX · v4. (n.d.). https://docs.dydx.exchange/concepts-architecture/architectural_overview

Introduction - Balancer. (n.d.). https://docs.balancer.fi/concepts/core-concepts/introduction.html

Introduction and Overview | dYdX Chain Help Center. (n.d.). https://help.dydx.trade/en/articles/166976-introduction-and-overview

J Bos, L Ducas, E Kiltz, & T Lepoint. (2018). CRYSTALS-Kyber: a CCA-secure module-lattice-based KEM. https://ieeexplore.ieee.org/abstract/document/8406610/

J. Burns & G. Neiger. (1994). Fast and simple distributed consensus. In Distributed Computing. https://www.semanticscholar.org/paper/7334eb87e4a19eabb9af1f6547a7a2c7548df6bb

J Durham. (2023). Regulatory sandboxes enable pragmatic blockchain regulation. In Wash. JL Tech. & Arts. https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/washjolta18&section=4

J. Gardner. (1978). The dancing dodo. https://www.semanticscholar.org/paper/0175d979c1593bcb2243fb8f2725fdd249842419

J. H. Ziegeldorf, Roman Matzutt, Martin Henze, Fred Grossmann, & Klaus Wehrle. (2018). Secure and anonymous decentralized Bitcoin mixing. In Future Gener. Comput. Syst. https://linkinghub.elsevier.com/retrieve/pii/S0167739X16301297

J. Heyning & M. Dahlheim. (2022). Orcinus orca. In CABI Compendium. https://academic.oup.com/mspecies/article-lookup/doi/10.2307/3504225

J Liu & Y Ishida. (2009). Vibration suppression of rotating machinery utilizing an automatic ball balancer and discontinuous spring characteristics. https://asmedigitalcollection.asme.org/vibrationacoustics/article-abstract/131/4/041004/471039

J Overdahl & CM Lewis. (2025). Solana and the SOL Market. In Available at SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5117683

J. Parish. (2012). The Dodo and the Solitaire: A Natural History. https://www.semanticscholar.org/paper/ba62c8a84b97eed514d6498e30a59cf7b70797a9

J. Schaller. (2005). Balancer / Balancers / neu / gebraucht. https://www.semanticscholar.org/paper/7ab2922d1f8ac357dac2da3a8b33c1eaf15cf728

J. Skovira, W. Chan, Honbo Zhou, & D. Lifka. (1996). The EASY - LoadLeveler API Project. In Job Scheduling Strategies for Parallel Processing. https://link.springer.com/chapter/10.1007/BFb0022286

J. V. Ruth, M. Fokkinga, & M. V. Keulen. (2004). The Dodo query flattening system. In CTIT technical report series. https://www.semanticscholar.org/paper/44f72f8e6aca33209e26b19c9013a30deb4b084a

J. Weber. (1991). A Forward-Chaining Information Framework. In The Next Generation of Information Systems. https://link.springer.com/chapter/10.1007/3-540-55616-8_51

J. Wu, Mu-En Wu, Pang-Jen Hung, Mohammad Mehedi Hassan, & G. Fortino. (2020). Convert index trading to option strategies via LSTM architecture. In Neural Computing and Applications. https://link.springer.com/article/10.1007/s00521-020-05377-6

J Xu & Y Feng. (2022). Reap the harvest on blockchain: A survey of yield farming protocols. https://ieeexplore.ieee.org/abstract/document/9953979/

J. Yin & Mac Ren. (2021). On Liquidity Mining for Uniswap v3. In ArXiv. https://www.semanticscholar.org/paper/a882a6a18b40ce625cd025ecc3fd285b3a5cf89f

Jailton Coelho, M. T. Valente, Luciano O. Milen, & L. L. Silva. (2020). Is this GitHub Project Maintained? Measuring the Level of Maintenance Activity of Open-Source Projects. In Inf. Softw. Technol. https://arxiv.org/abs/2003.04755

Jane Thomason, Sonja Bernhardt, T. Kansara, & Nichola Cooper. (2021). Blockchain Introduced. In Research Anthology on Blockchain Technology in Business, Healthcare, Education, and Government. http://services.igi-global.com/resolvedoi/resolve.aspx?doi=10.4018/978-1-7998-5351-0.ch003

Janine Berg, Robin Fritsch, Lioba Heimbach, & R. Wattenhofer. (2022). An Empirical Study of Market Inefficiencies in Uniswap and SushiSwap. In Financial Cryptography Workshops. https://arxiv.org/abs/2203.07774

Jannice Käll. (2018). Blockchain Control. In Law and Critique. https://link.springer.com/article/10.1007/s10978-018-9227-x

Jeffy Yu. (2024). Memes, Markets, and Machines: The Evolution of On Chain Autonomy through Hyperstition. In ArXiv. https://arxiv.org/abs/2410.23794

Ji Zhang, Xunfei Jiang, Yun Tian, X. Qin, Mohammed I. Alghamdi, M. A. Assaf, & Meikang Qiu. (2012). ORCA: An offloading framework for I/O-intensive applications on clusters. In 2012 IEEE 31st International Performance Computing and Communications Conference (IPCCC). https://ieeexplore.ieee.org/document/6407741/

Jianjian Yu, Lei Fan, & Gongliang Chen. (2019). A New Structure of Blockchain to Simplify the Verification. In International Conference on Blockchain and Trustworthy Systems. https://www.semanticscholar.org/paper/8cb6e3ba5bf6dc404acb01c43a0d124dd29eee76

JIE Pablos, ME Marriaga, & ÁLP del Pozo. (2022). … -Quantum Group Authenticated Key Exchange protocol with the LibOQS library: a comparative performance analysis from Classic McEliece, Kyber, NTRU, and Saber. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/9950501/

JL Caton. (2020). Cryptoliquidity: the blockchain and monetary stability. In Journal of Entrepreneurship and Public Policy. https://www.emerald.com/insight/content/doi/10.1108/jepp-03-2019-0011/full/html

Jonas Bertels, Quinten Norga, & Ingrid Verbauwhede. (2024). A Better Kyber Butterfly for FPGAs. In 2024 34th International Conference on Field-Programmable Logic and Applications (FPL). https://ieeexplore.ieee.org/document/10705545/

José Bacelar Almeida, Santiago Arranz Olmos, Manuel Barbosa, Gilles Barthe, François Dupressoir, Benjamin Grégoire, Vincent Laporte, Jean-Christophe Léchenet, Cameron Low, Tiago Oliveira, Hugo Pacheco, Miguel Quaresma, Peter Schwabe, & Pierre-Yves Strub. (n.d.). Formally verifying Kyber. https://www.semanticscholar.org/paper/bb72cb4e685c80798c0e8e7e7ec43b4320b96af7

Joseph Bonneau, Izaak Meckler, V. Rao, & Evan Shapiro. (2020). Coda: Decentralized Cryptocurrency at Scale. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/b89a56250994ea77e8e100d4a7bf87199d28a1cd

JR Varma. (2019). Blockchain in finance. In Vikalpa. https://journals.sagepub.com/doi/abs/10.1177/0256090919839897

Juntao Gao, Tong Wu, & Xuelian Li. (2020). Secure, fair and instant data trading scheme based on bitcoin. In J. Inf. Secur. Appl. https://linkinghub.elsevier.com/retrieve/pii/S2214212619309688

Junwei Yu, Yepeng Ding, Yuheng Guo, Kentaro Kotani, & Hiroyuki Sato. (2023). Inj-Kyber: Enhancing CRYSTALS-Kyber with Information Injection within a Bio-KEM Framework. In 2023 IEEE 22nd International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom). https://ieeexplore.ieee.org/document/10538951/

JVA Silveira. (2024). Historical Loss-versus-Rebalancing (LVR) Data for Blockchain Automated Market Makers (AMMs). https://repositorio.ufsc.br/handle/123456789/256868

JW Bos, M Gourjon, J Renes, & T Schneider. (2021). Masking kyber: First-and higher-order implementations. https://incs.ub.rub.de/index.php/TCHES/article/view/9064

JZH Wong. (2022). Characterising cryptocurrency project networks using graph-based analysis. https://search.proquest.com/openview/9b675e4df0dd77654c330bc317d61694/1?pq-origsite=gscholar&cbl=18750&diss=y

K Chin, C Majidi, & A Gupta. (2024). 1 Modular Parallel Manipulator for Long-Term Soft Robotic Data Collection. In arXiv. https://arxiv.org/abs/2409.03614

K Coutinho, P Clark, F Azis, N Lip, & J Hunt. (2021). Enabling Blockchain Scalability and Interoperability with Mobile Computing through LayerOne. X. https://arxiv.org/abs/2110.01398

K. G. Dastidar & T. Herman. (2009). Separation of circulating tokens. In Theor. Comput. Sci. https://link.springer.com/chapter/10.1007/978-3-642-05118-0_25

K Hupman, IN Visser, & E Martinez. (2015). Using platforms of opportunity to determine the occurrence and group characteristics of orca (Orcinus orca) in the Hauraki Gulf, New Zealand. https://www.tandfonline.com/doi/abs/10.1080/00288330.2014.980278

K. Zhuang. (2007). The Risk Characteristics and Control of Development Finance. In Journal of Chongqing University. https://www.semanticscholar.org/paper/38349cebaa0b90406dd9a898b4326e85928dd264

Karnika Padia, Vennis Shah, Devi Desai, & Purnima Kubde. (2020). Trade Finance Using Blockchain. In Social Science Research Network. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3565328

Kevin Liao & Jonathan Katz. (2017). Incentivizing Blockchain Forks via Whale Transactions. In Financial Cryptography Workshops. https://www.semanticscholar.org/paper/6d818bf1b05a07b79e73f5b29b4c5a34ad2bc456

Kezhen Zhang. (2024). The Application of Blockchain Technology in Supply Chain Finance. In Frontiers in Business, Economics and Management. https://drpress.org/ojs/index.php/fbem/article/view/16440

Ky b e r : An O n -Ch a i n L i q u i d i ty P r o to c o l. (n.d.). https://www.allcryptowhitepapers.com/wp-content/uploads/2018/05/Kyber-network-whitepaper.pdf

kyber - GitCode. (n.d.). https://gitcode.com/gh_mirrors/ky/kyber/overview

Kyber - Open Quantum Safe. (n.d.). https://openquantumsafe.org/liboqs/algorithms/kem/kyber.html

Kyber – Software - CRYSTALS. (n.d.). https://pq-crystals.org/kyber/software.shtml

Kyber Network Releases Critical Infrastructure To Bring TradFi ... - Forbes. (n.d.). https://www.forbes.com/sites/rorymurray/2020/10/22/kyber-network-releases-critical-infrastructure-to-bring-tradfi-to-defi/

L François, J van Eyll, & P Godard. (2010). Dictionary of disease ontologies (DODO): a graph database to facilitate access and interaction with disease and phenotype ontologies. In F1000Research. https://f1000research.com/articles/9-942

L François, J van Eyll, & P Godard. (2020). Dictionary of disease ontologies (DODO): a graph database to facilitate access and interaction with disease and phenotyp e ontologies [version 1; peer review …. https://pdfs.semanticscholar.org/3dfd/f75a25829bcfe3e11738fec39e11276e7895.pdf

L. Harrington. (2015). ORCA quick guide. https://www.semanticscholar.org/paper/b6eb38d119084013f7c1ddc962979d50fa2cc3f7

L. Lys, Arthur Micoulet, & M. Potop-Butucaru. (2021). R-SWAP: Relay based atomic cross-chain swap protocol. In IACR Cryptol. ePrint Arch. https://link.springer.com/chapter/10.1007/978-3-030-93043-1_2

L Montgomery, D Sharma, & S Dodos. (2018). How angry are your customers? Sentiment analysis of support tickets that escalate. https://ieeexplore.ieee.org/abstract/document/8498104/

L. Sliwko, V. Getov, & A. Bolotov. (2015). Distributed Agent-Based Load Balancer for Cloud Computing. https://www.semanticscholar.org/paper/196e95276b0a51c3dec798e2c011363ff9eeeaf5

L. Thamsen. (2011). Object Collaboration in the Orca Web Framework. https://www.semanticscholar.org/paper/73e8acb4df53fb64de7702c1c7afc2936e7c50c6

L. Thamsen, Anton Gulenko, M. Perscheid, R. Krahn, R. Hirschfeld, & David A. Thomas. (2012). Orca: A Single-Language Web Framework for Collaborative Development. In 2012 10th International Conference on Creating, Connecting and Collaborating through Computing. https://ieeexplore.ieee.org/document/6195221/

L Wan, F Zheng, G Fan, R Wei, L Gao, & Y Wang. (2022). A novel high-performance implementation of CRYSTALS-Kyber with AI accelerator. https://link.springer.com/chapter/10.1007/978-3-031-17143-7_25

L Yuxian. (2025). Blockchain interoperability for decentralized finance. https://www.sciencedirect.com/science/article/pii/B9780443347177000106

LA Maghrabi, M Altwijri, SS Binyamin, & FS Alallah. (2024). Secure biometric identification using orca predators algorithm with deep learning: Retinal iris image analysis. https://ieeexplore.ieee.org/abstract/document/10418121/

Li Si. (2006). Characteristics of Public Finance in a Modern Market Economy. https://www.semanticscholar.org/paper/26402aae4064307462df70c85c5b555b9d5c401e

Lili Cheng, Zhiying Lv, Osama Alfarraj, Amr Tolba, X. Yu, & Yongjun Ren. (2024). Secure cross-chain interaction solution in multi-blockchain environment. In Heliyon. https://linkinghub.elsevier.com/retrieve/pii/S2405844024048928

Lin Zhong, Huili Wang, Jan Xie, Bo Qin, Joseph K. Liu, & Qianhong Wu. (2019). A Flexible Instant Payment System Based on Blockchain. In Australasian Conference on Information Security and Privacy. https://link.springer.com/chapter/10.1007/978-3-030-21548-4_16

Lioba Heimbach, Eric Schertenleib, & R. Wattenhofer. (2022). Exploring Price Accuracy on Uniswap V3 in Times of Distress. In Proceedings of the 2022 ACM CCS Workshop on Decentralized Finance and Security. https://arxiv.org/abs/2208.09642

Lioba Heimbach, Ye Wang, & R. Wattenhofer. (2021). Behavior of Liquidity Providers in Decentralized Exchanges. https://www.semanticscholar.org/paper/96e41bd96cf382931feb58b5deee8fde20342fd0

liquiditygoblin/1inch-cli: On-chain trading cli, supporting ... - GitHub. (n.d.). https://github.com/liquiditygoblin/1inch-cli

Liyuan Ma, Xiulong Liu, Yuhan Li, Chenyu Zhang, Gaowei Shi, & Keqiu Li. (2024). GFBE: A Generalized and Fine-Grained Blockchain Evaluation Framework. In IEEE Transactions on Computers. https://ieeexplore.ieee.org/document/10384477/

Luke Tchang. (2020). Reentrancy Detector for Solidity Smart Contracts. https://www.semanticscholar.org/paper/6be5325177575a67746f11a83c4c5ea891aa8dec

M. Azouaoui, Olivier Bronchain, Clément Hoffmann, Yulia Kuzovkova, Tobias Schneider, & François-Xavier Standaert. (2022). Systematic Study of Decryption and Re-Encryption Leakage: the Case of Kyber. In IACR Cryptol. ePrint Arch. https://link.springer.com/chapter/10.1007/978-3-030-99766-3_11

M. Barbosa & Andreas Hülsing. (2023). The security of Kyber’s FO-transform. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/54a83a2900904066458e50db7bd5eb585bee4261

M. Behar, P. Fichtner, P. L. Grande, & F. C. Zawislak. (1995). Ranges in Si and lighter mono and multi-element targets. In Materials Science & Engineering R-reports. https://www.semanticscholar.org/paper/ca5b81eba8c26c53b92290810be50a0661ffe389

M. Bettio, Fabian Bruse, A. Franke, T. Jakoby, & Daniel Schärf. (2019). Hyperledger Fabric as a Blockchain Framework in the Financial Industry. In The Impact of Digital Transformation and FinTech on the Finance Professional. https://link.springer.com/chapter/10.1007/978-3-030-23719-6_3

M Jin, R Liu, & M Monperrus. (2025). On-Chain Analysis of Smart Contract Dependency Risks on Ethereum. In arXiv. https://arxiv.org/abs/2503.19548

M. Kabuye. (2018). Technology and Financial Disintermediation with a Special Reference to Blockchain and Islamic Finance. In ERN: Technology (Topic). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3436923

M Khan, MA Al-Mansour, & AA Mousa. (2014). Compositional characteristics of the essential oil of Myrtus communis grown in the central part of Saudi Arabia. https://www.tandfonline.com/doi/abs/10.1080/10412905.2013.820671

M. Klee. (2007). Analysis of PCBs in Waste Oil Using the Backflush Capability of the Agilent QuickSwap Accessory. https://www.semanticscholar.org/paper/a01a8a42a4197e565d34f6d307ccc905d85fb964

M Labadie. (1940). Impermanent loss and slippage in Automated Market Makers (AMMs) with constant-product formula. In Available at SSRN 4053924. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4053924

M Minilal & M Meena. (2025). SIOPA-DLMUC: A Self-Improved Orca Predation Algorithm with Deep Learning for Enhancing 5G Enabled Cognitive Radio Network Security. https://search.ebscohost.com/login.aspx?direct=true&profile=ehost&scope=site&authtype=crawler&jrnl=20419031&AN=185369232&h=cIzEs5ajz0wWHtXdMKJ1I2ceCKzQC%2BV8FJC6dz5cFXTFTPRdNWyjP3b2QkrJu2yg36ofOysCnvXr0tf2crXtOA%3D%3D&crl=c

M Rüetschi, C Campajola, & CJ Tessone. (2024). How Do Decentralized Finance Protocols Compare to Traditional Financial Products? A Taxonomic Approach. In Ledger. https://ledgerjournal.org/ojs/ledger/article/view/360

M Sheehan. (1989). The place of the balancer in balance of power theory. In Review of International Studies. https://www.cambridge.org/core/journals/review-of-international-studies/article/place-of-the-balancer-in-balance-of-power-theory/E65596504150B377F4D74FA39AAEAFCD

M. Taniguchi, Tomoyuki Amano, Hiroaki Ogata, & Hiroyuki Taniai. (2014). Features of Financial Data. https://www.semanticscholar.org/paper/9639805482ef532c4a0c9d97b115b0fe59f767c9

M. Toulouse, H. K. Dai, & Q. Nguyen. (2022). A Consensus-Based Load-Balancing Algorithm for Sharded Blockchains. In International Conference on Future Data and Security Engineering. https://link.springer.com/chapter/10.1007/978-3-030-91387-8_16

MA Asef & SMH Bamakan. (2024). From x* y= k to Uniswap Hooks: A Comparative Review of Decentralized Exchanges (DEX). In arXiv. https://arxiv.org/abs/2410.10162

manifoldfinance/curve-integration: Curve Finance Integration Kit. (n.d.). https://github.com/manifoldfinance/curve-integration

Manuel Barbosa & P. Schwabe. (2024). Kyber terminates. In IACR Cryptol. ePrint Arch. https://polyjmath.org/volumes/polyjmath-1-6.html

Maximilian Schiedermeier, Omar Hasan, T. Mayer, L. Brunie, & H. Kosch. (2019). A transparent referendum protocol with immutable proceedings and verifiable outcome for trustless networks. In International Workshop on Complex Networks & Their Applications. https://arxiv.org/abs/1909.06462

Md Fahad Monir & Dan Pan. (2021). Exploiting a Virtual Load Balancer with SDN-NFV Framework. In 2021 IEEE International Black Sea Conference on Communications and Networking (BlackSeaCom). https://ieeexplore.ieee.org/document/9527807/

Meng Qingshu, Hou Shubing, Li Zhenxiong, & Lu Songfeng. (2019). A Uniform Payment System for Hyperledger Fabric Blockchain. https://link.springer.com/chapter/10.1007/978-981-15-3278-8_8

MF Stoelen & R de Azambuja. (2022). The GummiArm project: a replicable and variable-stiffness robot arm for experiments on embodied AI. https://www.frontiersin.org/articles/10.3389/fnbot.2022.836772/full

Michael Abrahams. (2018). Estimating yield curve noise. https://www.semanticscholar.org/paper/5368e25e9857aec12e619a7f2bc040c2a933877d

Michael Sober, M. Sigwart, Philipp Frauenthaler, Christof Spanring, Max Kobelt, & Stefan Schulte. (2022). Decentralized cross-blockchain asset transfers with transfer confirmation. In Cluster Computing. https://link.springer.com/article/10.1007/s10586-022-03737-6

Minghong Fang, Zifan Zhang, Hairi, Prashant Khanduri, Jia Liu, Songtao Lu, Yuchen Liu, & N. Gong. (2024). Byzantine-Robust Decentralized Federated Learning. In Conference on Computer and Communications Security. https://arxiv.org/abs/2406.10416

ML Edgley, DL Baillie, DL Riddle, & AM Rose. (1995). Genetic balancers. In Methods in cell biology. https://www.sciencedirect.com/science/article/pii/S0091679X08613874

Mohammad Etemad & Alptekin Küpçü. (2013). Transparent, Distributed, and Replicated Dynamic Provable Data Possession. In IACR Cryptol. ePrint Arch. https://link.springer.com/chapter/10.1007/978-3-642-38980-1_1

N Chemaya, D Liu, R McLaughlin, & N Ruaro. (2024). The power of default: Measuring the effect of slippage tolerance in decentralized exchanges. https://link.springer.com/chapter/10.1007/978-3-031-78676-1_11

N Chemaya, LW Cong, E Jorgensen, & D Liu. (2023). Uniswap daily transaction indices by network. https://osf.io/ube2z/download

N Chemaya, LW Cong, E Jorgensen, D Liu, & L Zhang. (2025). A dataset of Uniswap daily transaction indices by network. In Scientific Data. https://www.nature.com/articles/s41597-024-04042-0

N. Dehouche & R. Blythman. (2022). A Blockchain Protocol for Human-in-the-Loop AI. In ArXiv. https://arxiv.org/abs/2211.10859

N Jawalkar, K Gupta, & A Basu. (2024). Orca: FSS-based secure training and inference with GPUs. https://ieeexplore.ieee.org/abstract/document/10646833/

N McKibben, Y Zhang, S Li, L Kong, & L Tan. (2025). Smartphone-Based Fundus Imaging and Computer Vision Analysis for Monitoring Retinopathy of Prematurity in Neonatal Rats With and Without Lutein Treatment. In Experimental Eye Research. https://www.sciencedirect.com/science/article/pii/S0014483525002313

Nanxin Zhou & R. Mamon. (2012). An accessible implementation of interest rate models with Markov-switching. In Expert Syst. Appl. https://linkinghub.elsevier.com/retrieve/pii/S0957417411013625

Navigating the Complex Regulatory Framework for Uniswap in the US. (2024). https://rr2.capital/navigating-the-complex-regulatory-framework-for-uniswap-in-the-us/

New front-end interface of quickswap.exchange - GitHub. (n.d.). https://github.com/QuickSwap/interface-v2

NF Samreen & MH Alalfi. (2023). An empirical study on the complexity, security and maintainability of Ethereum-based decentralized applications (DApps). In Blockchain: Research and Applications. https://www.sciencedirect.com/science/article/pii/S2096720922000616

nhancv/pancake-swap-testnet - GitHub. (n.d.). https://github.com/nhancv/pancake-swap-testnet

Nikolajs Koroļkovs & S. Kodors. (2023). UNISWAP - A CASE STUDY OF DECENTRALIZED EXCHANGES ON THE BLOCKCHAIN. In HUMAN. ENVIRONMENT. TECHNOLOGIES. Proceedings of the Students International Scientific and Practical Conference. https://www.semanticscholar.org/paper/ac8577670750921c320bfb08e8b69f7f51fa42a7

Nitin Upadhyay. (2019). UnBlock the Blockchain. In UnBlock the Blockchain. https://link.springer.com/book/10.1007/978-981-15-0177-7

NP Essien, GG James, & VU Ufford. (2024). Technological impact assessment of Blockchain Technology on the synergism of decentralized exchange and pooled trading platform. https://journals.iapaar.com/index.php/ijcarn/article/view/201

O. Litt. (2004). ORCA User’s Manual Glossary. https://www.semanticscholar.org/paper/77b81b4078041878e36e5d46b16e7f3a6c76e297

O Wesamaa. (2024). Market entry and differentiation strategies in blockchain-based business. https://aaltodoc.aalto.fi/items/cf6a1f51-88bb-4fcd-a946-0c9082cbdf59

Olaf Owe & Elahe Fazeldehkordi. (2022). A lightweight approach to smart contracts supporting safety, security, and privacy. In J. Log. Algebraic Methods Program. https://linkinghub.elsevier.com/retrieve/pii/S2352220822000256

Omer Shlomovits & Oded Leiba. (2020). JugglingSwap: Scriptless Atomic Cross-Chain Swaps. In ArXiv. https://www.semanticscholar.org/paper/cc58f30756a269fdabb750d09bce720b0c51c9b9

ORCA | Orca SolanaTM | Home Official Site. (n.d.). https://orca-so-lana.github.io/

ORCA Protocol (ORCA): Revolutionizing LP 2024 | Coin-Labs. (n.d.). https://coin-labs.com/en/guide/orca-protocol-orca/

Ori Mazor & Ori Rottenstreich. (2024). An Empirical Study of Cross-Chain Arbitrage in Decentralized Exchanges. In 2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS). https://ieeexplore.ieee.org/document/10426894/

P Aggarwal & T Thamaraimanalan. (2024). Exploring the Synergy between Network Security and Blockchain Technology. https://ieeexplore.ieee.org/abstract/document/10522287/

P. Diviacco. (2005). An open source, web based, simple solution for seismic data dissemination and collaborative research. In Comput. Geosci. https://linkinghub.elsevier.com/retrieve/pii/S0098300404002328

P Dylan-Ennis. (2024). Hash, Bash, Cash: How Change Happens in Decentralized Web3 Cultures. https://www.emerald.com/insight/content/doi/10.1108/S0733-558X20240000089007/full/html

P. Hoenisch, Subhra Mazumdar, Pedro A. Moreno-Sánchez, & S. Ruj. (2022). LightSwap: An Atomic Swap Does Not Require Timeouts At Both Blockchains. In IACR Cryptology ePrint Archive. https://link.springer.com/chapter/10.1007/978-3-031-25734-6_14

P Lambert & D Gavrilova. (2022). Management Report The Impact of Altrucoin on Innovation Within DeFi on the Binance Smart Chain. https://paullambert.org/wp-content/uploads/2023/03/Paul-Lambert-Masters-Thesis.pdf

P Li, T Miyazaki, & W Zhou. (2020). Secure balance planning of off-blockchain payment channel networks. https://ieeexplore.ieee.org/abstract/document/9155375/

P. Urien. (2000). Blockchain Transaction Protocol for Constraint Nodes. https://www.semanticscholar.org/paper/f16840f52fcdf4e71b5e58897a1bd69839a23982

Pancake Swap Review 2025: Everything You NEED To Know!! (n.d.). https://coinbureau.com/review/pancakeswap-cake/

PancakeSwap - Wikipedia. (n.d.). https://en.wikipedia.org/wiki/PancakeSwap

PancakeSwap launches one-click crosschain swaps to simplify DeFi ... (2025). https://cointelegraph.com/news/pancakeswap-one-click-crosschain-swaps-simplify-defi-ux

pancakeswap-v2 - GitHub. (n.d.). https://github.com/pancakeswap-v2

Paulo da, Silva Lima, Leonardo A. D. S. Ribeiro, R. D. Queiroz, J. Quintino, F. Q. Silva, André L. M. Santos, & José Roberto. (2021). Evaluating Kyber post-quantum KEM in a mobile application. https://www.semanticscholar.org/paper/0e30f9dcbb19e1e1005e5c6467653777d2815243

peternoyes/dodo: 6502 Portable Game System - GitHub. (n.d.). https://github.com/peternoyes/dodo

Peterson K. Ozili. (2019). Blockchain Finance: Questions Regulators Ask. In Behavioral & Experimental Finance eJournal. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3243817

Phuong Duy Huynh, Son Hoang Dau, Hong Yen Tran, Nick Huppert, Hoonie Sun, Joshua Cervenjak, Xiaodong Li, & Emanuele Viterbo. (2024). Serial Scammers and Attack of the Clones: How Scammers Coordinate Multiple Rug Pulls on Decentralized Exchanges. In ArXiv. https://www.semanticscholar.org/paper/c41645184b27ac276f4a60d52d9c91fac379ce66

Pietro Danzi, Marko Angjelichinoski, Č. Stefanović, & P. Popovski. (2017). Distributed proportional-fairness control in microgrids via blockchain smart contracts. In 2017 IEEE International Conference on Smart Grid Communications (SmartGridComm). https://arxiv.org/abs/1705.01453.pdf

Portfolio - Raydium. (n.d.). https://raydium.io/portfolio/

Post-quantum cryptography — Kyber | by Kris | Medium. (n.d.). https://medium.com/@krisinfosec/post-quantum-cryptography-38bcbad95284

privy-io/dydx-v4-web - GitHub. (n.d.). https://github.com/privy-io/dydx-v4-web

Product Overview | PancakeSwap. (n.d.). https://docs.pancakeswap.finance/

ProgrammingLanguageGregory V. Wilson & Henri E. BalVersion. (2007). Experiences with the Orca. https://www.semanticscholar.org/paper/4bc06dbe7bb24c2631bc2134048030bff7a33342

Qiong Zhang, P. Palacharla, M. Sekiya, Junichi Suga, & T. Katagiri. (2020). Demo: A Blockchain Based Protocol for Federated Learning. In 2020 IEEE 28th International Conference on Network Protocols (ICNP). https://ieeexplore.ieee.org/document/9259388/

Quang Tung Thai, Jong-Chul Yim, & Sunme Kim. (2019). A scalable semi-permissionless blockchain framework. In 2019 International Conference on Information and Communication Technology Convergence (ICTC). https://ieeexplore.ieee.org/document/8939962/

R Allafi & IR Alzahrani. (2024). Enhancing Cybersecurity in the Internet of Things Environment Using Artificial Orca Algorithm and Ensemble Learning Model. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10504276/

R Avanzi, J Bos, L Ducas, E Kiltz, & T Lepoint. (2019). CRYSTALS-Kyber algorithm specifications and supporting documentation. https://www.pq-crystals.org/kyber/data/kyber-specification-round3-20210804.pdf

R Team. (2021). Raydium protocol litepaper. https://crebaco.com/planner/admin/uploads/whitepapers/1912452Raydium-Litepaper.pdf

R. V. Glabbeek, Vincent Gramoli, & Pierre Tholoniat. (2019). Cross-chain payment protocols with success guarantees. In Distributed Computing. https://link.springer.com/article/10.1007/s00446-023-00446-0

RA Tănase & C Carabaş. (2023). Limit order for decentralized exchanges on blockchain. https://ieeexplore.ieee.org/abstract/document/10274924/

Raphael Maas, E. Maehle, & K. Großpietsch. (2012). Applying the Organic Robot Control Architecture ORCA to Cyber-Physical Systems. In 2012 38th Euromicro Conference on Software Engineering and Advanced Applications. https://ieeexplore.ieee.org/document/6328158/

raydium · GitHub Topics. (n.d.). https://github.com/topics/raydium

Raydium Price Chart (RAY) - CoinGecko. (n.d.). https://www.coingecko.com/en/coins/raydium

Raydium price today, RAY to USD live price, marketcap and chart. (n.d.). https://coinmarketcap.com/currencies/raydium/

Raydium: Solana’s Leading AMM and Liquidity Provider. (n.d.). https://solanacompass.com/projects/raydium

raydium-sdk · GitHub Topics. (n.d.). https://github.com/topics/raydium-sdk

RaydiumTM | Home Official Site. (n.d.). https://raydium-raydium-io.github.io/

RaydiumTM | Home Official Website. (n.d.). https://raydium-app.github.io/

RC Ogliore. (2021). Acquisition and Online Display of High‐Resolution Backscattered Electron and X‐Ray Maps of Meteorite Sections. In Earth and Space Science. https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2021EA001747

RJ Hartfield & JE Burkhalter. (2015). A complete and robust approach to axisymmetric method of characteristics for nozzle design. https://arc.aiaa.org/doi/pdf/10.2514/6.2015-4217

S. Dolev & Matan Liber. (2020). Toward Self-stabilizing Blockchain, Reconstructing Totally Erased Blockchain (Preliminary Version). In International Conference on Cyber Security Cryptography and Machine Learning. https://link.springer.com/chapter/10.1007/978-3-030-49785-9_12

S. Easterbrook. (2014). Open code for open science. In Nature Geoscience. https://www.nature.com/articles/ngeo2283

S Kumar. (2022). Central clearing of crypto-derivatives in a decentralized finance (defi) framework: An exploratory review. In International Journal of Business & Economics (IJBE). https://ielas.org/ijbe/index.php/ijbe/article/view/21

S. Loosmore & D. Armstrong. (1990). Do-Do Abuse. In British Journal of Psychiatry. https://www.semanticscholar.org/paper/acc371ccb58125d6fb99d6f9d1ff6111a91d262f

S Mazumdar. (2022). Towards faster settlement in HTLC-based cross-chain atomic swaps. https://ieeexplore.ieee.org/abstract/document/10063460/

S Mazumdar & A Sinha. (2023). Quick Swap: Faster Settlement in Cross-Chain Atomic Swaps. In Authorea Preprints. https://www.techrxiv.org/doi/full/10.36227/techrxiv.20355183

S. Ness, Alexander Lerch, & G. Tzanetakis. (2011). Strategies for orca call retrieval to support collaborative annotation of a large archive. In 2011 IEEE 13th International Workshop on Multimedia Signal Processing. https://ieeexplore.ieee.org/document/6093798/

S. Ntalampiras. (2017). A Deep Learning Framework for Classifying Sounds of Mysticete Whales. https://linkinghub.elsevier.com/retrieve/pii/B9780128113189000223

S. Ray. (2023). “Dead as a Dodo.” In TDR: The Drama Review. https://www.cambridge.org/core/journals/the-drama-review/article/dead-as-a-dodo/5529A8D8C86D9B575042C0C957912303

S. Selberherr. (1984). Some Fundamental Properties. https://link.springer.com/chapter/10.1007/978-3-7091-8752-4_2

S Subramaniam, D Gabauer, & R Gupta. (2018). On the Transmission Mechanism of Asia-Pacific Yield Curve Characteristics. https://www.up.ac.za/media/shared/61/WP/wp_2018_64.zp163960.pdf

S Subramanian, A Augusto, & R Belchior. (2024). Benchmarking blockchain bridge aggregators. https://ieeexplore.ieee.org/abstract/document/10664224/

S. Underwood. (2016). Blockchain beyond bitcoin. In Communications of the ACM. https://dl.acm.org/doi/10.1145/2994581

Saleh Hashemseresht & Mohsen Pourpouneh. (2022). Concentrated Liquidity Analysis in Uniswap V3. In Proceedings of the 2022 ACM CCS Workshop on Decentralized Finance and Security. https://dl.acm.org/doi/10.1145/3560832.3563438

Santiago Palladino. (2019). A Sample DApp. In Ethereum for Web Developers. https://link.springer.com/chapter/10.1007/978-1-4842-5278-9_2

Sara Lundström & S. Öhman. (2019). Generating Value Through Blockchain Technology : The Case of Trade Finance. https://www.semanticscholar.org/paper/f5f804e4060ff88f3c43ba7861f5128837a1d43b

Say Hello to Raydium |. (2025). https://docs.raydium.io/raydium

Scholarly Commons. (2017). LibGuides: Introduction to GitHub: Creating Repositories. https://www.semanticscholar.org/paper/1b827d06e5378e60534c05ba8563695e3ac1023c

Shingo Sato & Junji Shikata. (n.d.). Bounded CCA 2 Secure Proxy Re-encryption Based on Kyber ∗. https://www.semanticscholar.org/paper/cd7f8c5ef58d49ee725a24f68cb040dc7b6d31c1

shuhuiluo/uniswap-v3-sdk-rs: Opinionated Rust implementation of ... (n.d.). https://github.com/shuhuiluo/uniswap-v3-sdk-rs

SK Behfar, F Théodoloz, & C Schranz. (2023). Blockchain-based data sharing platform customization with on/off-chain data balancing. https://ieeexplore.ieee.org/abstract/document/10338850/

Songlin He, Eric Ficke, M. M. A. Pritom, Huashan Chen, Qiang Tang, Qian Chen, Marcus Pendleton, Laurent L. Njilla, & Shouhuai Xu. (2022). Blockchain-based automated and robust cyber security management. In J. Parallel Distributed Comput. https://linkinghub.elsevier.com/retrieve/pii/S0743731522000089

Sound Transit. (2018). ORCA Card Retailer Locations. https://www.semanticscholar.org/paper/ce0dce96041746c261fa536743cc435d6ab96251

SR Alotaibi, H Alfraihi, N Alruwais, & M Maray. (2025). Two-Tiered Privacy Preserving Framework for Software-Defined Networking Driven Defence Mechanism for Consumer Platforms. https://ieeexplore.ieee.org/abstract/document/10870212/

SS Gill, H Wu, P Patros, C Ottaviani, P Arora, & VC Pujol. (n.d.). ORCA–Online Research@ Cardiff. https://core.ac.uk/download/pdf/597054287.pdf

Stefan Loesch, N. Hindman, Mark Richardson, & N. Welch. (2021). Impermanent Loss in Uniswap v3. https://www.semanticscholar.org/paper/07b2a3144e534d8f8b575c6bed21f6473c9efe77

Supatsara Wattanakriengkrai, Bodin Chinthanet, Hideaki Hata, R. Kula, Christoph Treude, Jin L. C. Guo, & Kenichi Matsumoto. (2020). GitHub repositories with links to academic papers: Public access, traceability, and evolution. In J. Syst. Softw. https://linkinghub.elsevier.com/retrieve/pii/S0164121221002144

Sushi. (n.d.). https://www.sushi.com/faq/general/about-sushi

Sushi is Live on Sonic - Sushi Swap. (2024). https://www.sushi.com/blog/sushi-is-live-on-sonic

SushiSwap price today, SUSHI to USD live price, marketcap and chart. (n.d.). https://coinmarketcap.com/currencies/sushiswap/

SushiSwap Review: Pros, Cons, and How to Get Started. (n.d.). https://www.bitdegree.org/crypto/sushiswap-review

SushiSwapTM | Official Website. (n.d.). https://v3-sushiswap.github.io/

Swap Raydium. (n.d.). https://raydium.io/

T Berkman. (2023). The impact of decentralised market design on liquidity and prices: an empirical analysis of Uniswap protocol upgrades. https://www.um.edu.mt/library/oar/handle/123456789/121943

T Przybylski, P Froehle, & C McDonald. (2015). Wearable wireless body area network for aeronautical applications. https://ieeexplore.ieee.org/abstract/document/7293398/

T Sarig, T Galili, & R Eilat. (2023). balance--a Python package for balancing biased data samples. In arXiv. https://arxiv.org/abs/2307.06024

T Sharma, GK Kaur, HK Mahto, & G Kumar. (2024). Exploring ApexWolf: A Study of a Cryptocurrency Exchange Website. https://ieeexplore.ieee.org/abstract/document/10664090/

T. Tejaswini, Tanaraj Krishna, S.Teja Reddy, & A. Pranay. (2018). A Novel Block Chain Technology. In International Journal of Research. https://www.semanticscholar.org/paper/16788c11c992c2aeec3b6440bfaac16408b8a9b3

T Uysal & H Ünözkan. (2024). Transaction Types in Cryptocurrencies. https://ieeexplore.ieee.org/abstract/document/10711051/

T Xia, M Wang, J He, G Yang, L Fan, & G Wei. (2024). A Quantum-Resistant Identity Authentication and Key Agreement Scheme for UAV Networks Based on Kyber Algorithm. In Drones. https://search.proquest.com/openview/4ce8317ab2579859eff081e3c5e819e2/1?pq-origsite=gscholar&cbl=5046906

Tendayi Kamucheka, Alexander Nelson, David Andrews, & Miaoqing Huang. (2022). A Masked Pure-Hardware Implementation of Kyber Cryptographic Algorithm. In 2022 International Conference on Field-Programmable Technology (ICFPT). https://ieeexplore.ieee.org/document/9974404/

The 1inch Network Identifies Hundreds of High-risk Addresses. (n.d.). https://www.trmlabs.com/resources/case-studies/1inch-network-identifies-hundreds-of-high-risk-addresses

The story of PancakeSwap(CAKE). The forgotten heroes. - Reddit. (2025). https://www.reddit.com/r/CryptoCurrency/comments/1klyxbz/the_story_of_pancakeswapcake_the_forgotten_heroes/

The Ultimate Guide to QuickSwap - Moralis Academy. (n.d.). https://academy.moralis.io/blog/the-ultimate-guide-to-quickswap

The Uniswap Protocol. (n.d.). https://docs.uniswap.org/concepts/uniswap-protocol

The unofficial Python client for the Uniswap exchange. - GitHub. (n.d.). https://github.com/uniswap-python/uniswap-python

Thi Thu Huong Doan & Peter Thiemann. (2021). A Typed Programmatic Interface to Contracts on the Blockchain. In ArXiv. https://link.springer.com/chapter/10.1007/978-3-030-89051-3_13

Thomas Corbat. (2010). C3P0 C-Plus-Plus-Parser-for-C++0x. https://www.semanticscholar.org/paper/e43fba6758a4c92f31e6f7fac4fabfe2824a85f9

Thomas N. Cintra & Maxwell P. Holloway. (2023). Detecting Depegs: Towards Safer Passive Liquidity Provision on Curve Finance. https://www.semanticscholar.org/paper/2b4ce2d05110587352d88fdcf00121ac02fda600

Tobias Kaupp, Alex Brooks, B. Upcroft, & A. Makarenko. (2007). Building a Software Architecture for a Human-Robot Team Using the Orca Framework. In Proceedings 2007 IEEE International Conference on Robotics and Automation. https://ieeexplore.ieee.org/document/4209669/

Top 10 Decentralized Exchanges (DEXs) - QuickNode. (2025). https://www.quicknode.com/builders-guide/top-10-decentralized-exchanges-dexs

Top Cryptocurrency Decentralized Exchanges - CoinMarketCap. (2020). https://coinmarketcap.com/rankings/exchanges/dex/

Top Decentralized Exchange Coins by Market Cap - Kraken. (2023). https://www.kraken.com/categories/decentralized-exchange

Tzong-Chen Wu & Tzong-Sun Wu. (1995). Group commitment protocol based on zero knowledge proofs. In Comput. Commun. https://linkinghub.elsevier.com/retrieve/pii/014036649599815T

U Hacioglu. (2020). Blockchain economics and financial market innovation. In Switzerland: Springer. https://link.springer.com/content/pdf/10.1007/978-3-030-25275-5.pdf

Understanding Curve Finance and Its Mechanisms - LinkedIn Perú. (n.d.). https://pe.linkedin.com/pulse/understanding-curve-finance-its-mechanisms-agustin-cortes-kzufc

Understanding Curve Finance: Earn, Trade, and Farm with DeFi. (n.d.). https://return.finance/blog/what-is-curve/

Understanding dYdX: A Guide to the Decentralized Perpetual Exchange. (n.d.). https://beincrypto.com/learn/dydx-exchange/

Uniswap - Wikipedia. (n.d.). https://en.wikipedia.org/wiki/Uniswap

Uniswap: Crypto & NFT Wallet - Apps on Google Play. (n.d.). https://play.google.com/store/apps/details?id=com.uniswap.mobile&hl=en_US

Uniswap Overview. (n.d.). https://docs.uniswap.org/concepts/overview

Uniswap (UNI): A Decentralized Crypto Exchange - DeFi - Gemini. (n.d.). https://www.gemini.com/cryptopedia/uniswap-decentralized-exchange-crypto-defi

Uniswap (UNI): What It Is, Uses, Pros and Cons - Investopedia. (n.d.). https://www.investopedia.com/uniswap-uni-definition-5217463

Uniswap V3 Architecture, Functionalities & Governance Mechanism. (n.d.). https://www.linkedin.com/pulse/deep-dive-uniswap-v3-architecture-functionalities-governance-singh-krrnf

Uniswap v4. (n.d.). https://docs.uniswap.org/contracts/v4/overview

V. Carro. (2008). Raydium (II): tus aplicaciones 3D fácilmente, 2a parte. In Linux magazine. https://www.semanticscholar.org/paper/9fbbd258400b922c3b20851bd932fac844c4513d

V Hwang, J Liu, G Seiler, X Shi, & MH Tsai. (2022). Verified NTT multiplications for NISTPQC KEM lattice finalists: Kyber, SABER, and NTRU. https://er.ceres.rub.de/index.php/TCHES/article/view/9838

V. Killer, A. E. Borshevnikov, & K. S. Soldatov. (2021). A version of the voting protocol based on blockchain technology. In IOP Conference Series: Materials Science and Engineering. https://validate.perfdrive.com/fb803c746e9148689b3984a31fccd902/?ssa=fc60d9d0-2f0f-4989-accc-c5b02edca7b1&ssb=94218282698&ssc=https%3A%2F%2Fiopscience.iop.org%2Farticle%2F10.1088%2F1757-899X%2F1069%2F1%2F012024&ssi=ca61d943-cnvj-4e6c-ac3d-481a69370150&ssk=botmanager_support@radware.com&ssm=76632716044323403461647422031795&ssn=f99506ebea423a913b15713a44eb8b7cc7d895a8e944-ddc5-4452-832cc4&sso=e038106b-56961b8777e3c4dff6ae064886caf166aea2191c5cb45aa7&ssp=48229182321751035532175109278356477&ssq=44802828629550896299276736901713450690304&ssr=MzQuNTkuMy4xNTU=&sst=python-httpx/0.27.2&ssu=&ssv=&ssw=&ssx=eyJ1em14IjoiN2Y5MDAwYjI5ZWNjNmEtZjgxZC00MjYxLTljOGItZmExNzE3ZDA2MTA0MS0xNzUxMDc2NzM2NjQwOTU1ODUxMy1mNjlkZmQyNDliNmUzZjgxNDYiLCJfX3V6bWYiOiI3ZjkwMDA5NWE4ZTk0NC1kZGM1LTQ0NTItODA2Yi01Njk2MWI4Nzc3ZTMxLTE3NTEwNzY3MzY2NDA5NTU4NTEzLTAwMGE0NTllMDg5ZmYwNDhmMDQ0NiIsInJkIjoiaW9wLm9yZyJ9

V NEKRIACH, SM BELLIAHI, C LI, & P LI. (2025). HEMVM: a Heterogeneous Blockchain Framework for Interoperable Virtual Machines. https://www.eecg.utoronto.ca/~veneris/OOPSLA25.pdf

V. Ostrerov. (2015). Hot Swap solution meets AMC and MicroTCA standards. https://linkinghub.elsevier.com/retrieve/pii/B9780128000014002489

V. Sureshkumar, A. Ramalingam, N. Rajamanickam, & Ruhul Amin. (2017). A lightweight two-gateway based payment protocol ensuring accountability and unlinkable anonymity with dynamic identity. In Comput. Electr. Eng. https://linkinghub.elsevier.com/retrieve/pii/S0045790616301938

Vadim Lyubashevsky & D. Stehlé. (2021). Non-applicability of the Gaborit&Aguilar-Melchor patent to Kyber and Saber. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/08b2e0c4d098807c5aacf67a55b1415b76f5c5ec

Valentin David. (2008). Preparing for C++0x. In Companion to the 23rd ACM SIGPLAN conference on Object-oriented programming systems languages and applications. https://dl.acm.org/doi/10.1145/1449814.1449853

Varun Maram & Keita Xagawa. (2022). Post-Quantum Anonymity of Kyber. In IACR Cryptology ePrint Archive. https://www.semanticscholar.org/paper/999dd0d59cd74fa0a5150301599118700710b8af

Vincent Lammers & Justin Cone. (2023). What is Github? Brand Film. In ACM SIGGRAPH 2023 Electronic Theater. https://dl.acm.org/doi/10.1145/3577024.3589016

VS Golovko & KV Oriekhova. (2023). Investment in stock market and cryptocurrencies. https://dspace.khadi.kharkov.ua/bitstreams/b3aec257-4b4b-4ecb-8322-ec89a93df0f6/download

W. Lees. (1984). Protocol implementation for Universe. In Comput. Commun. https://linkinghub.elsevier.com/retrieve/pii/0140366484900318

W. Pennington. (2018). The Collateral-Linked Currency Forward (CLCF) Contract: Blockchain-Enabled OTC Currency Forward Market Infrastructure. In The Journal of Index Investing. https://www.semanticscholar.org/paper/e49c07cbebf943a4d7e415ee391b953148931a3b

Wai Kok Chan, Ji-Jian Chin, & V. Goh. (2021). Simple and scalable blockchain with privacy. In J. Inf. Secur. Appl. https://linkinghub.elsevier.com/retrieve/pii/S2214212620308474

Wang Shuguang. (2013). Negative Investment of Rural Finance and Rural Economic Growth: Empirical Study and Improvement Framework of Kuznets Curve Effect. In Finance & Trade Economics. https://www.semanticscholar.org/paper/1f46893b0bf34de4e34400b67d0a6e05bd3b2c9b

Wang Xin. (2001). Improvement of the Kinetic Balancer Machine. In Laboratory Research and Exploration. https://www.semanticscholar.org/paper/c371b676220bafee3e0f7d531971dda9b7db3377

Wenhui Jiang, Qiuhua Xu, & Ruige Zhang. (2021). Tail-event driven network of cryptocurrencies and conventional assets. In Finance Research Letters. https://linkinghub.elsevier.com/retrieve/pii/S154461232100413X

What is 0x? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/0x

What is 0x Protocol? - Paxful. (n.d.). https://paxful.com/university/what-is-0x-protocol

What Is 0x Protocol? - “The Defiant.” (n.d.). https://thedefiant.io/education/infrastructure/what-is-0x-protocol

What is 1inch Network? - Messari. (n.d.). https://messari.io/project/1inch-network/profile

What Is Balancer? | CoinMarketCap. (n.d.). https://coinmarketcap.com/academy/article/what-is-balancer

What is Balancer & the BAL Token? A Beginner’s Guide | Hodlin. (n.d.). https://www.hodlin.com/blog/what-is-balancer

What is Balancer (BAL)? A Complete Guide - Blockchain Works. (n.d.). https://blockchain.works-hub.com/learn/what-is-balancer-a-complete-guide-0a854

What Is Balancer? The Complete Guide - Medium. (n.d.). https://medium.com/balancer-protocol/what-is-balancer-the-complete-guide-762ee230a9d4

What Is Curve DAO Token (CRV)? A Rising Star in the World of DeFi. (n.d.). https://cryptodataspace.com/what-is-curve-dao-token-crv/

What is Curve Finance: An In-Depth Explanation + Examples. (n.d.). https://www.bitdegree.org/crypto/tutorials/what-is-curve-finance

What is Curve Finance [Deep Dive Into the Stablecoin DEX]. (n.d.). https://medium.com/coinstats/what-is-curve-finance-deep-dive-into-the-stablecoin-dex-251e726e53b

What is Curve Finance? Pros and Cons of the DeFi Platform - Coinweb. (n.d.). https://coinweb.com/what-is-curve-finance/

What Is DODO? - Binance Academy. (n.d.). https://academy.binance.com/en/articles/what-is-dodo

What is DODO? Is It a Defi Protocol? - Cryptoforce Blogs. (n.d.). https://blog.cryptoforce.in/post/what-is-dodo

What is dYdX? | Messari. (n.d.). https://messari.io/project/dydx/profile

What Is dYdX (DYDX)? Features, Tokenomics, and Price Prediction. (n.d.). https://coinmarketcap.com/academy/article/what-is-dydx-dydx-features-tokenomics-and-price-prediction

What Is dYdX Exchange? - Ledger. (n.d.). https://www.ledger.com/academy/what-is-dydx-exchange

What Is Kyber Network and How Does It Work? - Shrimpy Blog. (n.d.). https://blog.shrimpy.io/blog/what-is-kyber-network-and-how-does-it-work

What Is Kyber Network (KNC)? - Flipster Blog. (n.d.). https://flipster.io/en/blog/kyber-network-knc-guide

What is Orca? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/orca

What is Orca (ORCA)? Project and Token Analysis. (n.d.). https://solsniffer.com/blog/what-is-orca-orca-project-and-token-analysis

What is Pancakeswap | Beginner’s Guide on How to Use Pancakeswap. (n.d.). https://www.blockchain-council.org/defi/what-is-pancakeswap/

What Is PancakeSwap? - BeInCrypto. (n.d.). https://beincrypto.com/learn/what-is-pancakeswap/

What Is PancakeSwap ($CAKE)? Everything You Need to Know. (n.d.). https://coins.ph/academy/what-is-pancakeswap-cake-everything-you-need-to-know/

What is PancakeSwap and How Does It Work? - Coinary. (n.d.). https://coinary.com/learn/what-is-pancakeswap/

What is PancakeSwap and its CAKE Token? - bsc.news. (n.d.). https://bsc.news/post/pancakeswap-defi-comprehensive-platform-guide

What is PancakeSwap and its CAKE Token? - CoinMarketCap. (n.d.). https://coinmarketcap.com/academy/article/8c2612e6-1a47-4aa2-9ddd-2f31e933e96c

What is QuickSwap? A Guide to the Layer-2 Decentralized Exchange. (n.d.). https://beincrypto.com/learn/quickswap-guide/

What is QuickSwap: A Scalable DEX and AMM - Phemex. (n.d.). https://phemex.com/academy/what-is-quickswap

What is QuickSwap, and how does it work? - Cointelegraph. (n.d.). https://cointelegraph.com/explained/what-is-quickswap-and-how-does-it-work

What is QuickSwap? Definition, Features & How It Works. (n.d.). https://www.techopedia.com/definition/quickswap

What is Raydium? | RAY Token - Kraken. (n.d.). https://www.kraken.com/en-gb/learn/what-is-raydium-ray

What is Raydium? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/raydium

What is raydium cryptocurrency, use cases and technology - OctoBot. (n.d.). https://www.octobot.cloud/what-is-raydium

What is Sushi (SUSHI)? Complete guide to the DeFi protocol and token. (n.d.). https://www.withtap.com/blog/what-is-sushi-sushi-complete-guide-to-the-defi-protocol-and-token

What Is SushiSwap Decentralized Exchange (DEX): A Beginner’s Guide. (n.d.). https://www.kucoin.com/blog/defi-101-what-is-sushiswap-and-how-does-it-work

What is SushiSwap? How the Decentralized Exchange Works. (n.d.). https://www.nansen.ai/post/what-is-sushiswap

What is SushiSwap? (SUSHI) - Kraken. (n.d.). https://www.kraken.com/learn/what-is-sushiswap-sushi

What is SushiSwap (SUSHI) and How Does it Work? - CoinGape. (n.d.). https://coingape.com/education/what-is-sushiswap/

What is the 0x Protocol? | Koinly. (n.d.). https://koinly.io/crypto-glossary/0x-protocol/

What is Uniswap? - Coinbase. (n.d.). https://www.coinbase.com/learn/crypto-basics/what-is-uniswap

What is Uniswap? - Messari. (n.d.). https://messari.io/project/uniswap/profile

What Is Uniswap? A Beginner-Friendly Guide - dYdX. (2024). https://www.dydx.xyz/crypto-learning/what-is-uniswap

What is What is 0x protocol? Exploring decentralized trading ... (n.d.). https://www.cointracker.io/learn/0x-protocol

X Liu. (2023). Market Dynamics and Spillovers on Digital Platforms. https://escholarship.org/uc/item/9k2752fm

X Wang, Y Peng, H Huang, & X Li. (2024). Dodo: A scalable optimistic deterministic concurrency control protocol. In Future Generation Computer Systems. https://www.sciencedirect.com/science/article/pii/S0167739X24002139

X Zhao & S Schwertfeger. (2024). 3dref: 3d dataset and benchmark for reflection detection in rgb and lidar data. https://ieeexplore.ieee.org/abstract/document/10550747/

X Zheng, Z Wan, D Lo, D Xie, & X Yang. (2025). Why Does My Transaction Fail? A First Look at Failed Transactions on the Solana Blockchain. https://dl.acm.org/doi/abs/10.1145/3728943

Xianwen Zhou & V. Abramov. (2019). A Practical Guide to Interest Rate Curve Building Validations (W/ Excel Replica of Bloomberg Libor @ GitHub). In Derivatives eJournal. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3329563

Xiaobing Sun, Wenyuan Xu, Xin Xia, Xiang Chen, & Bin Li. (2018). Personalized project recommendation on GitHub. In Science China Information Sciences. https://link.springer.com/article/10.1007/s11432-017-9419-x

Xiaoqin Feng, Jianfeng Ma, Yinbin Miao, Qian Meng, Ximeng Liu, Qi Jiang, & Hui Li. (2018). Pruneable sharding-based blockchain protocol. In Peer-to-Peer Networking and Applications. https://link.springer.com/article/10.1007/s12083-018-0685-6

Xinda Li, G. Chen, Lin Wei, Y. Wang, & Yilin Li. (2022). Blockchain adoption in supply chain finance: a research model for empirical investigation in the electricity industry. In Proceedings of the 5th International Conference on Information Management and Management Science. https://dl.acm.org/doi/10.1145/3564858.3564888

Xingxiong Zhu & Dong Wang. (2019). Research on Blockchain Application for E-Commerce, Finance and Energy. In IOP Conference Series: Earth and Environmental Science. https://www.semanticscholar.org/paper/955153eb347fbb1b58c342e7585dfd5c881dcb07

Xu Ma, Chen Wang, & Xiaofeng Chen. (2021). Trusted data sharing with flexible access control based on blockchain. In Comput. Stand. Interfaces. https://www.semanticscholar.org/paper/d4af5f19a09a72ccc44d2f86a49df6286958a3b1

Xuan Han, Yamin Liu, & Haixia Xu. (2017). A User-Friendly Centrally Banked Cryptocurrency. In Information Security Practice and Experience. https://link.springer.com/chapter/10.1007/978-3-319-72359-4_2

Xueyan Liu, Linpeng Li, Ruirui Sun, Wenjing Li, & Tao Liu. (2023). Lightweight multi-departmental data sharing scheme based on consortium blockchain. In Peer-to-Peer Networking and Applications. https://www.semanticscholar.org/paper/fc86707505fa9770d3b2fdd842747db4390145ab

Y Cui, L Zhao, Q Zhang, & X Wei. (2014). Design and dynamic simulation analysis of flexible swap device based on Pro/E and ADAMS. https://wseas.com/journals/mechanics/2014/a025711-148.pdf

Y. Komano & Takaaki Mizuki. (2024). Physical Zero-Knowledge Proof Protocols for Topswops and Botdrops. In New Gener. Comput. https://link.springer.com/article/10.1007/s00354-024-00272-3

Y. Kondo, K. Deguchi, Yuichiro Hayashi, & F. Obata. (2003). Reversibility and disassembly time of part connection. In Resources Conservation and Recycling. https://linkinghub.elsevier.com/retrieve/pii/S0921344902001532

Y Xie, X Kang, T Li, CK Chu, & H Wang. (2022). Towards secure and trustworthy flash loans: A blockchain-based trust management approach. https://link.springer.com/chapter/10.1007/978-3-031-23020-2_28

Y Xing & S Li. (2021). A compact hardware implementation of CCA-secure key exchange mechanism CRYSTALS-KYBER on FPGA. https://bmt.ub.rub.de/index.php/TCHES/article/view/8797

Y Yu, G Huang, & X Guo. (2021). Financing strategy analysis for a multi-sided platform with blockchain technology. In International journal of production research. https://www.tandfonline.com/doi/abs/10.1080/00207543.2020.1766718

Y Zhang, Y Li, & C Tessone. (2025). A Line Graph-Based Framework for Identifying Optimal Routing Paths in Decentralized Exchanges. In arXiv. https://arxiv.org/abs/2504.15809

Yan Zhen. (2000). The Physical Paraphrase of Derivative dy/dx. In Journal of Liaoning Institute of Technology On Social Science. https://www.semanticscholar.org/paper/13ee8a5348eb9eb24971d135a68ab3cc1c02615d

Yaru Wang & Jianmei Liu. (2024). Quantum pairwise-parallel mismatch attack on Kyber. In Physica Scripta. https://validate.perfdrive.com/fb803c746e9148689b3984a31fccd902/?ssa=28d2ca66-088b-4918-9f5b-ffa56e41cee4&ssb=78310296683&ssc=https%3A%2F%2Fiopscience.iop.org%2Farticle%2F10.1088%2F1402-4896%2Fad827a&ssi=74fc8854-cnvj-40ac-bd4f-90f6a3bfbfd7&ssk=botmanager_support@radware.com&ssm=41572739796745321580177308646320&ssn=320ad967dc80c54f63086192637adbc33d5695a8e944-ddc5-4452-873846&sso=58d1d06b-56961b8777e3000c5d4d3d2a0b32992725ff5a28f244a403&ssp=00226303271751067859175107912965422&ssq=76126998631132873101076736300649414731141&ssr=MzQuNTkuMy4xNTU=&sst=python-httpx/0.27.2&ssu=&ssv=&ssw=&ssx=eyJyZCI6ImlvcC5vcmciLCJ1em14IjoiN2Y5MDAwYjI5ZWNjNmEtZjgxZC00MjYxLTljOGItZmExNzE3ZDA2MTA0MS0xNzUxMDc2NzM2NjQwOTU3NDUwNC01MGE0ZTRkOWYyOWUzOWZhNTgiLCJfX3V6bWYiOiI3ZjkwMDA5NWE4ZTk0NC1kZGM1LTQ0NTItODA2Yi01Njk2MWI4Nzc3ZTMxLTE3NTEwNzY3MzY2NDA5NTc0NTA0LTAwMGU2NjcyMGE2OTU0OTg4ZmY1OCJ9

Ying Wang, Yifang Chen, & Lenan Wu. (2014). Light Protocols in Chain Network. https://link.springer.com/chapter/10.1007/978-3-319-01766-2_137

Yiqiang Zhao, Shijian Pan, Haocheng Ma, Ya Gao, Xintong Song, Jiaji He, & Yier Jin. (2023). Side Channel Security Oriented Evaluation and Protection on Hardware Implementations of Kyber. In IEEE Transactions on Circuits and Systems I: Regular Papers. https://ieeexplore.ieee.org/document/10175157/

Yogev Bar-On & Y. Mansour. (2023). Uniswap Liquidity Provision: An Online Learning Approach. In ArXiv. https://arxiv.org/abs/2302.00610

Yongrae Jo & Chan-Gook Park. (2024). A Hierarchical Blockchain supporting Dynamic Locality by Extending Execute-Order-Validate Architecture. In Distributed Ledger Technologies: Research and Practice. https://www.semanticscholar.org/paper/7a28349757e4a6f65d4448adab68c9ff823a69d8

You-sheng Zhou, Zongyang Zhang, Haibin Zhang, Sisi Duan, Bin Hu, Licheng Wang, & Jianwei Liu. (2022). Dory: Asynchronous BFT with Reduced Communication and Improved Efficiency. In IACR Cryptol. ePrint Arch. https://www.semanticscholar.org/paper/0d9c5c82e6f807df86e5d59a6b511aca23c65954

Yuan Lu, Qiang Tang, & Guiling Wang. (2020). Generic Superlight Client for Permissionless Blockchains. In ArXiv. https://link.springer.com/chapter/10.1007/978-3-030-59013-0_35

Yuen C Lo & F. Medda. (2020). Uniswap and the Emergence of the Decentralized Exchange. In ERN: Other Microeconomics: General Equilibrium & Disequilibrium Models of Financial Markets (Topic). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3715398

Z Gong, H Yu, C Liao, B Liu, C Chen, & J Li. (2024). CoBa: Convergence Balancer for Multitask Finetuning of Large Language Models. https://arxiv.org/abs/2410.06741

Z Lin, K Wang, Y Wu, & D Li. (2024). Fast payments across heterogeneous blockchains for Internet of Things. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10453562/

Z Xiang, J Li, W Liang, & J Xie. (2024). Secure identity authentication scheme design leveraging zero-knowledge proof technology. https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13228/1322821/Secure-identity-authentication-scheme-design-leveraging-zero-knowledge-proof-technology/10.1117/12.3038017.short

Z Xiao, Z Chen, S Liu, & H Wang. (2023). Fed-grab: Federated long-tailed learning with self-adjusting gradient balancer. https://proceedings.neurips.cc/paper_files/paper/2023/hash/f4b8ddb9b1aa3cb11462d64a70b84db2-Abstract-Conference.html

Zalán Szűgyi, Márk Török, Norbert Pataki, & T. Kozsik. (2011). Multicore C++Standard Template Library with C++0x. https://pubs.aip.org/aip/acp/article/1389/1/857-860/802861

Zeshuo Zhu, Rui Zhang, & Yang Tao. (2024). Atomic cross-chain swap based on private key exchange. In Cybersecur. https://cybersecurity.springeropen.com/articles/10.1186/s42400-023-00202-8

Zhang Zhang & G. Xiao. (2004). New multisignature scheme for specified group of verifiers. In Appl. Math. Comput. https://linkinghub.elsevier.com/retrieve/pii/S0096300303009391

Zhiqiang Liu, Shuyang Tang, Sherman S. M. Chow, Z. Liu, & Yu Long. (2019). Fork-free hybrid consensus with flexible Proof-of-Activity. In Future Gener. Comput. Syst. https://www.semanticscholar.org/paper/62f4d18bc040d6902d62469eec4d3003b16b96d9

Zou Bo. (2002). Characteristics of Microburst. In Journal of Civil Aviation University of China. https://www.semanticscholar.org/paper/da4a54bbdf3ca9a41940b98ff90b3bb5e098f6d4

Zuhua Shao. (2008). Certificate-based fair exchange protocol of signatures from pairings. In Comput. Networks. https://linkinghub.elsevier.com/retrieve/pii/S1389128608002296

Доо Йоунг Риу, Вон Йоунг Дзунг, Йоунг Дзин Чо, & Дзеонг Хоон Канг. (2014). Balancer and spiral machine with such balancer. https://www.semanticscholar.org/paper/6e86d9623e87f6ebc974480091743dddd0d3a5bf

김영철 & 장은호. (2006). A centrifuge with the balancer. https://www.semanticscholar.org/paper/225de7ae3a47889558fa1eb4486d53ff5773f599

송병섭, 황준길, 김창걸, 곽수원, & 류정탁. (2010). 전동휠체어 조이스틱 컨트롤러를 이용한 효율적인 컴퓨터 대체 접근 장치 개발. https://www.semanticscholar.org/paper/27e5d54562c7b515a621761d29821f545cb7dce2

차홍기, 이원석, 최영환, 이주철, & 이강산. (2019). 블록체인 국제표준화 활동 현황. https://www.semanticscholar.org/paper/9dd93ad049f796a0272fdab6d5b8ab07e704a4e7

小西义弘, 罗天赐, & 黄怡硕. (2005). Crystal lattice type battery potential balancer. https://www.semanticscholar.org/paper/837f6e996383fce09a53e3f28eebb8a79705f164

嶌田吉成 & 大八木淳史. (2012). The ball balancer. https://www.semanticscholar.org/paper/f9c66593d4a64398c1a13618a69b1d89e41056d3

洪大永, 金成镇, 高弘锡, & 金铉培. (2010). Washing machine and balancer. https://www.semanticscholar.org/paper/84b51182bfa3eb0f03dfc618268abf2ebddde0e6



Generated by Liner
https://getliner.com/search/s/5926611/t/86064745