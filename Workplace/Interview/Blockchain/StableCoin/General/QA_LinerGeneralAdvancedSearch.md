### Stablecoin Public Chains: Plasma, Stable, and Arc

Stablecoins are a critical asset class in the crypto financial system, serving as primary settlement and quotation assets in secondary market trading and integrating into broader use cases such as cross-border payments and on-chain finance. The emergence of stablecoin public chains aims to provide purpose-built infrastructure to address the shortcomings of existing public chains like Ethereum and TRON in terms of cost, efficiency, compliance, and ecosystem integration.

### Plasma: A USDT-Centric Layer 1 Blockchain

Plasma is a Layer 1 blockchain infrastructure specifically designed for stablecoin payments, focusing on high efficiency and low cost for USDT transfers. It receives official technical and resource support from the Tether network and places USDT at the core of its architecture. Plasma enables zero-fee USDT transfers and high throughput, meeting the demands for large-scale payments and applications. The network operates as an independent Layer 1 blockchain with its own consensus and security mechanisms, utilizing the PlasmaBFT consensus, a hybrid of Proof of Stake (PoS) and Byzantine Fault Tolerance (BFT). This consensus mechanism ensures second-level transaction finality, which is particularly suitable for payment and settlement use cases. Plasma is also fully compatible with the Ethereum Virtual Machine (EVM), allowing developers to deploy smart contracts using Solidity and familiar Ethereum tools like MetaMask. Furthermore, Plasma periodically anchors its state root to the Bitcoin network, leveraging Bitcoin\u2019s immutability and decentralization to enhance security and trust, providing an external "validation proof" rather than recording every transaction on Bitcoin.

#### Multi-Asset Gas Payments and Ecosystem

One of Plasma's innovations is its multi-asset gas model, allowing users to pay gas fees with USDT or BTC (wrapped as pBTC) in addition to the native XPL token. This feature lowers the entry barrier by eliminating the need to hold native tokens solely for transaction costs. The native token XPL is used for transaction fees, staking in the consensus mechanism, governance, and ecosystem incentives. In August 2025, Plasma partnered with Binance to launch the "Plasma USDT Locked Product," a yield product for staking USDT, which was fully subscribed to an initial allocation of 250 million USDT in less than an hour. The XPL token was listed on major exchanges like Binance and OKX on September 25, 2025, reaching a market capitalization of over $2.7 billion within a week. Plasma's testnet launched on July 15, 2025, supporting BTC and USDT for transaction fee payments, and its mainnet Beta launched on September 25, 2025, with over $2 billion in stablecoin liquidity activated on launch day. The TVL on Plasma's mainnet Beta reached $4.9 billion within three days, with Aave being the largest contributor.

#### Ecosystem Partnerships and Challenges

Plasma has established strategic partnerships with payment platforms like Yellow Card and BiLira Kripto to promote gas-free USDT transfers and interoperability with local fiat currencies. The project is also advancing collaboration with DeFi leader Curve Finance to integrate the StableSwap AMM mechanism for low-slippage stablecoin swaps. Since the launch of the mainnet Beta, Plasma has integrated Ethena Labs' synthetic stablecoin USDe and sUSDe into its DeFi ecosystem, partnering with protocols like Aave, Curve, Balancer, and Fluid. The ecosystem currently revolves around stablecoin liquidity, payments, and lending through various DeFi protocols, with over $5 billion in TVL as of September 2025, primarily concentrated in USDT. However, the sustainability of its gas-free USDT transfer model and its heavy reliance on Tether's regulatory stability are potential challenges. While technically capable of supporting compliance features like KYC and transfer restrictions, its compliance-related ecosystem infrastructure is still in early development.

### Stable: A High-Performance Layer 1 Blockchain for USDT

Stable is a high-performance Layer 1 blockchain purpose-built for USDT, aiming to provide a fast, low-cost, and low-latency transaction network for stablecoins. It focuses exclusively on USDT trading and settlement, offering enterprise-grade dedicated block space and compliant private transaction solutions for institutional payment and clearing. Stable will use StableBFT, a customized Proof-of-Stake (PoS) protocol based on CometBFT and compatible with EVM, designed for high throughput, low latency, and reliability. This consensus mechanism aims to achieve sub-second block confirmations and high throughput by allowing nodes to process proposals in parallel and separating data propagation from consensus. On Stable, USDT can be used natively for gas payments and on-chain settlements, eliminating the need for other tokens and high transaction fees. The network aims to make USDT circulate on-chain as efficiently and securely as cash.

#### Dual-Token Mechanism and Enterprise Features

Stable employs a dual-token mechanism, consisting of USDT0 and gasUSDT. gasUSDT serves as the native gas token, while USDT0 is the primary token for everyday transactions, maintaining a 1:1 peg with standard USDT via the OFT (Omnichain Fungible Token) standard for cross-chain circulation. Peer-to-peer USDT0 transfers are completely free of transaction fees, simplifying the user experience. For enterprise users, Stable offers dedicated block space for transaction stability and predictability, and the USDT Transfer Aggregator can batch-process large volumes of USDT0 transfers. Future plans include confidential transfer functionality using zero-knowledge encryption for privacy while maintaining compliance auditability. Stable\u2019s roadmap focuses on phased performance enhancement, starting with reduced user barriers, then enhanced transaction efficiency, and finally comprehensive high performance. The core technical framework is largely complete, with key features like native USDT payments, sub-second transaction finality, and EVM compatibility.

#### Investment and Challenges

Stable has secured investment and backing from institutions such as Bitfinex, Hack VC, and Franklin Templeton, with endorsement from Tether CEO Paolo Ardoino. However, Stable's testnet and mainnet have not yet launched, meaning its blockchain performance is untested in real-world conditions. The absence of a clarified token issuance plan for its PoS consensus mechanism introduces uncertainty regarding network incentives and ecosystem growth. Stable also faces intensifying competition from traditional payment giants accelerating blockchain integrations and other compliance-focused stablecoin networks. Its ecosystem remains in its infancy, lacking publicly available user data or real-world deployment cases.

### Arc: A Cross-Chain Settlement Layer for Stablecoins

Arc is a Layer 1 blockchain developed by Circle, focusing on cross-chain interoperability and liquidity integration for stablecoins like USDC. Announced in August 2025, Arc represents Circle's evolution from a stablecoin issuer to a blockchain infrastructure provider. On Arc, users can use USDC to pay gas fees, and it natively supports multiple stablecoins including EURC and USYC1 for multi-currency financial applications. Arc employs a high-performance consensus mechanism capable of processing thousands of transactions per second, with deterministic, second-level finality. It includes a built-in institutional-grade Request for Quote (RFQ) engine for foreign exchange pricing and 24/7 on-chain settlement capabilities. Arc also offers optional privacy protection, allowing selective concealment of transaction or balance data in accordance with compliance needs.

#### Core Features and Ecosystem Integration

Unlike single-stablecoin chains, Arc is designed as a cross-chain stablecoin settlement layer, facilitating fund transfers across multiple stablecoins and blockchains. It uses Direct Mint and Burn-and-Mint mechanisms for cross-chain stablecoin movement, eliminating reliance on third-party bridges. Arc provides a unified balance view and fast finality, bringing multi-chain asset management closer to a single-chain experience. Its mission extends beyond infrastructure to foster native stablecoin applications in cross-border payments, FX derivatives, on-chain credit, and capital markets. Arc can serve as an on-chain settlement layer for international payments through integration with the Circle Payments Network (CPN), and its FX engine enables automated stablecoin conversion and fiat on/off-ramps.

#### Regulatory Alignment and Challenges

Arc is deeply integrated with the Circle ecosystem, enhancing synergies among Circle's products and ensuring regulatory alignment by design. As a regulated stablecoin issuer, Circle's compliance with US and multi-jurisdictional requirements means Arc inherently supports auditability and compliance. Strategically, Arc aims to upgrade the global dollar settlement system to an on-chain model, acting as a "regulated on-chain Swift" connected to banks, payment institutions, and multinational corporations. It announced integration with Fireblocks at launch, allowing over 2,400 financial institutions to connect directly. However, Arc faces technical challenges in balancing security, decentralization, and complexity for sub-second transactions and seamless cross-chain interoperability. Bootstrapping developers and applications beyond USDC-focused use cases, and balancing cross-border compliance with privacy, are also significant challenges.

### Tempo: Stripe's Enterprise-Level On-Chain Payment Initiative

Tempo is a proprietary Layer 1 blockchain being jointly launched by Stripe and Paradigm, with the core objective of providing efficient, low-cost on-chain settlement infrastructure tailored for enterprise payment scenarios. It focuses on balancing compliance and privacy requirements to ensure a secure and auditable transaction environment for corporate clients and financial institutions. Tempo's design prioritizes payment performance, stablecoin settlements, EVM compatibility, and high-throughput architecture to meet the demands of global enterprises. The project aims to become an enterprise-grade on-chain payment network, enhancing Stripe's competitive edge in the global payments market and promoting real-world adoption of stablecoins in business use cases. Tempo remains in stealth development and has not yet launched publicly.

#### Value Proposition and Development Challenges

Tempo's value proposition lies in enabling Web2 enterprise clients to integrate on-chain settlement directly into their existing payment systems, reducing costs and time for cross-border payments. Its EVM compatibility and Stripe's payment APIs allow for "on-chain settlement with Web2 deployment". Stripe has already launched stablecoin-based financial accounts that allow businesses in 101 countries to store, transfer, and make payments in USD-denominated stablecoins, powered by Bridge and integrated with MetaMask. However, Tempo faces challenges in ecosystem building and developer engagement, as its focus on enterprise payments might limit its appeal for diverse application development. The long-term value of Tempo depends on balancing its enterprise payment focus with broader openness to attract developers and foster ecosystem vitality.

### Comparative Analysis of Stablecoin Public Chains

The landscape of stablecoin-oriented public blockchains primarily centers around USDT and USDC, with projects like Plasma, Stable, Arc, and Tempo all aiming to become foundational infrastructure for high-frequency stablecoin settlement.

#### Plasma vs. Stable

Plasma and Stable are both backed by Tether and revolve around USDT as their core asset. Plasma is a high-performance USDT payment and settlement network that leverages Bitcoin's security for zero-fee USDT transfers, low-latency settlement, and privacy-enabled payments, making it suitable for high-frequency use cases like exchange fund transfers and cross-border payments. Stable, also supported by Tether, is designed as an independent high-performance Layer 1 chain for institutional settlement and enterprise-level payments, emphasizing stability and large-scale throughput. While both prioritize intra-chain efficiency for USDT, Plasma emphasizes performance and Bitcoin-anchored security, while Stable focuses on smoother payment experiences for small-value transactions and remittances.

#### Arc vs. Plasma and Stable

Arc, developed by Circle with USDC at its core, focuses on cross-chain interoperability and liquidity integration to enable seamless USDC settlement across multiple chains. Unlike Plasma and Stable, which operate as dedicated highways for a specific stablecoin (USDT), Arc is positioned as a multi-chain clearing hub supporting broader use cases such as cross-border payments, institutional settlements, and multi-chain DeFi. Arc emphasizes unified settlement across chains, whereas Plasma and Stable emphasize intra-chain efficiency.

#### Tempo's Distinct Focus

Tempo, a joint initiative by Stripe and Paradigm, targets retail payments and merchant settlements, while maintaining EVM compatibility to attract developers for stablecoin-based payment applications. Its focus aligns with Stripe's fintech framework, concentrating on payment implementation to drive stablecoin adoption at the merchant level.

### Economic Models and Ecosystem Design

Most leading stablecoin-oriented public blockchains support using stablecoins like USDT or USDC for gas fees, which lowers operational barriers and boosts transaction activity. This is crucial for early ecosystem bootstrapping. For instance, Plasma allows XPL as well as stablecoins for gas payments, ensuring network incentives and security while offering user flexibility.

#### Single vs. Multi-Stablecoin Chains

Single-stablecoin chains, such as Plasma, concentrate liquidity around a core stablecoin like USDT, facilitating faster network effects and early ecosystem activation. However, this limits cross-chain interoperability. Multi-stablecoin chains, like Arc, allow multiple stablecoins to circulate, enhancing cross-chain functionality and supporting diverse financial applications, though with potentially higher initial ecosystem-building costs due to fragmented liquidity. Single-stablecoin chains are better for rapid early-stage ecosystem growth, while multi-stablecoin chains are designed for long-term, multi-currency financial infrastructures.

#### Ecosystem Bootstrapping and Long-Term Value

The core value of stablecoin public blockchains lies in facilitating payments and settlements, with direct stablecoin use for gas payments reducing user friction. While payments are central, the integration of transactional activity into DeFi, NFT, and real-world asset (RWA) applications drives a positive feedback loop, providing users and developer incentives. Long-term value comes from combining payment efficiency with ecosystem vibrancy, creating sustainable network effects and integrated ecosystem loops. The project that can balance gas mechanisms, aggregate stablecoin liquidity, and solve the ecosystem cold-start challenge is best positioned to become core infrastructure for future stablecoin settlement and DeFi.

### Evolution of Payment Systems and Regulatory Impact

Stablecoin public blockchains are poised to become the next generation of payment infrastructure, offering fast on-chain settlement and cross-border transactions with transparency and traceability. Compared to traditional payment systems, on-chain stablecoin settlement offers advantages in lower cross-border fees, near-instant transactions, and partial compatibility with existing regulatory frameworks due to the regulated nature of many stablecoins. Major payment giants like Stripe, PayPal, Visa, and Mastercard are exploring blockchain-based payment solutions, indicating a potential reliance on stablecoin blockchains to improve efficiency and maintain regulatory compliance.

The development of stablecoin public blockchains is heavily influenced by regulatory policy, with frameworks in regions like the United States, Hong Kong, and the European Union directly shaping their deployment and ecosystem evolution. For example, the US Stablecoin Act of 2025 imposes strict reserve requirements and disclosure obligations, impacting the compliance pathways and market positioning of stablecoin-oriented chains. Circle's compliance-driven strategy and regulatory licenses give Arc advantages in institutional access and cross-border payments, requiring adherence to institutional standards for transparency and risk management.

Sources: 
[1] What is stablecoin?: A survey on price stabilization mechanisms for decentralized payment systems, https://ieeexplore.ieee.org/abstract/document/8992735/
[2] Are the stabilities of stablecoins connected?, https://link.springer.com/article/10.1007/s40812-022-00207-3
[3] Security Perceptions of Users in Stablecoins: Advantages and Risks within the Cryptocurrency Ecosystem, https://ieeexplore.ieee.org/abstract/document/11023350/
[4] Revealing stablecoin successes: Lessons from a case study on USDT, https://aisel.aisnet.org/iceb2023/76/
[5] Stablecoin Chains: The Race and Opportunity in Next Crypto ..., https://coinwofficial.medium.com/stablecoin-chains-the-race-and-opportunity-in-next-crypto-payments-generation-cd8cc74d39b6?source=rss-217cd994c22b------2
[6] Understanding Stablecoins: Architecture, Ecosystem and Trading ..., https://medium.com/@ztraderai/understanding-stablecoins-architecture-ecosystem-and-trading-opportunities-87615f2a4b44
[7] Hybrid Monetary Ecosystems: Integrating Stablecoins and Fiat in the Future of Currency Systems, https://arxiv.org/abs/2505.10997
[8] The role of sustainable business model in cryptocurrency industry: a case study approach, https://lutpub.lut.fi/handle/10024/165886
[9] Top 30 Blockchain Interview Questions and Answers for 2025, https://www.simplilearn.com/tutorials/blockchain-tutorial/blockchain-interview-questions
[10] Top 30 Blockchain Interview Questions & Answers (2025) - Elite Brains, https://www.elitebrains.com/blog/blockchain-interview-questions
[11] Stablecoin Security: How Design Choices Create Vulnerabilities and ..., https://hacken.io/discover/stablecoin-security/
[12] Stability in the Age of Cryptocurrencies: A Critical Review of Stablecoin Mechanisms and their Implications, https://www.researchgate.net/profile/Sergio-Montanez-Jacquez/publication/378870249_Stability_in_the_Age_of_Cryptocurrencies_A_Critical_Review_of_Stablecoin_Mechanisms_and_their_Implications/links/65ef54abaaf8d548dcc1b3c5/Stability-in-the-Age-of-Cryptocurrencies-A-Critical-Review-of-Stablecoin-Mechanisms-and-their-Implications.pdf
[13] A Survey of Blockchain-Based Stablecoin: Cryptocurrencies and Central Bank Digital Currencies, https://link.springer.com/chapter/10.1007/978-981-19-8043-5_13
[14] [PDF] A Comprehensive Framework for Stablecoin Regulation ... - SEC.gov, https://www.sec.gov/files/stablecoin_regulatory_framework.pdf
[15] Stablecoins for transferring value in the cryptocurrency market, https://knepublishing.com/index.php/KnE-Social/article/view/17246
[16] Examining User Perceptions of Stablecoins: Understandings and Risks, https://www.usenix.org/system/files/soups2023-poster160_guan_abstract_final.pdf
[17] Stablecoins-Types and Definitions, https://www.researchgate.net/profile/Conrad-Roberts/publication/358343710_Stablecoins_-Types_and_Definitions/links/61fc84811e98d168d7ed0120/Stablecoins-Types-and-Definitions.pdf
[18] A Stablecoin Ecosystem Primer, https://www.semanticscholar.org/paper/05d2c384f35b52a07437f06c456fb5f9d4807531
[19] Centralized Crypto Exchanges Incorporating Decentralized Features: Factors Driving Implementation and Impact on the Competitive Landscape, https://monami.hs-mittweida.de/files/15457/BC21w1-M_Masterthesis_Ro%CC%88ckener.pdf
[20] What Drives Stablecoin Growth?, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4791530
[21] The Case for Stringent Regulations of Stablecoins, https://www.semanticscholar.org/paper/fb997eb6be7340911779b075cc0debf6606851f8
[22] From instability to regulation: A systematic literature review on stablecoins, http://www.ijdar.org/10.4192/1577-8517-v25_3.pdf
[23] Frequently Asked Interview Questions on Blockchain, https://www.analyticsvidhya.com/blog/2023/02/frequently-asked-interview-questions-on-blockchain/
[24] Overcoming the Stablecoin Trilemma: Designing and Simulating a Decentralized, Stable, and Capital-Efficient Peg Maintenance System, https://www.semanticscholar.org/paper/60a62991951dbd496d88824a5acbeb6a133ec091
[25] STABLECOINS IN CRYPTOECONOMICS: FROM INITIAL COIN OFFERINGS TO CENTRAL BANK DIGITAL CURRENCIES, https://www.semanticscholar.org/paper/1ed7e0aa85de880cf97f5604731d9bf71fc06b39
[26] The Rise of Stablecoins and the Race for Digital Currency Domination, https://www.architectureandgovernance.com/applications-technology/the-rise-of-stablecoins-and-the-race-for-digital-currency-domination-an-enterprise-architects-perspective/
[27] Time for a Simple Linear Policy Rule for Stablecoin: Tether Policy Rule, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4028049
[28] How Business Architecture Builds a Stablecoin Business Model, https://www.linkedin.com/posts/paull_stablecoin-businessarchitecture-fintech-activity-7390301657961578497-x3gw
[29] Stablecoins: regulatory responses to their promise of stability 1, https://www.semanticscholar.org/paper/a36c0a4c8b70a1d524a50bfa93915179d084b79e
[30] Stablecoins: Types and Applications, https://www.semanticscholar.org/paper/02d7ee82382330ab85d085752f4d786dca5e46cd
[31] Analysis of the Appropriateness and Feasibility of the Reconnaissance Project Interview Questions and Measurements, https://journals.sagepub.com/doi/10.1177/156482659701800301
[32] [PDF] Stablecoins - Boston Consulting Group, https://media-publications.bcg.com/Stablecoins-five-killer-tests-to-gauge-their-potential.pdf
[33] Top 40 Blockchain Interview Questions and Answers [2025], https://digitaldefynd.com/IQ/top-blockchain-interview-questions-and-answers/
[34] Stablecoins: the possibility of a cryptocurrency becoming the future means of payment, https://www.diva-portal.org/smash/record.jsf?pid=diva2:1697220
[35] [PDF] OR01/2020 Global Stablecoin Initiatives - IOSCO, https://www.iosco.org/library/pubdocs/pdf/ioscopd650.pdf
[36] [PDF] Stablecoins: Growth Potential and Impact on Banking, https://www.federalreserve.gov/econres/ifdp/files/ifdp1334.pdf
[37] [PDF] Stablecoin DC Architecture Analysis (version 2) - ITU, https://www.itu.int/en/ITU-T/extcoop/dcgi/Documents/DCGI_Final%20report%20of%20the%20Stablecoins%20Workstream-130223.pdf
