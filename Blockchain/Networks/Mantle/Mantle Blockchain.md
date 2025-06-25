Mantle Blockchain

Wed Jun 25 2025

### Introduction to Mantle Blockchain

Mantle is an innovative blockchain platform engineered to optimize decentralized applications (DApps) and smart contracts. It functions as a modular Layer-2 blockchain solution built on Ethereum, aiming to enhance scalability, security, and overall performance for decentralized applications. Mantle addresses the challenges of high transaction fees and slow processing times often encountered on main networks like Ethereum. By processing transactions off-chain and settling them securely on Ethereum, Mantle provides a faster and more cost-effective environment for blockchain operations. Its design focuses on creating a secure, efficient, and low-cost transaction environment ideal for various decentralized finance (DeFi) and enterprise applications.

### History and Development of Mantle

Mantle was established in 2019 with the strategic objective of resolving scalability and interoperability challenges prevalent in blockchain technology. Key milestones in its growth include the launch of the Mantle Mainnet in 2020 and significant updates in 2022 that bolstered its smart contract capabilities. The project originated as a product of BitDAO, a decentralized autonomous organization (DAO). In a significant development in May 2023, the BitDAO community voted to merge BitDAO and Mantle Network ecosystems, leading to the rebranding of BitDAO to Mantle and the conversion of the BIT token to MNT. This merger streamlined the project's identity and governance. The Mantle mainnet officially launched in July 2023, following a six-month testnet period during which it processed over 14 million transactions and deployed more than 140,000 smart contracts. Since its mainnet launch, Mantle has rapidly ascended to become a top-ranked Layer 2 network by Total Value Locked (TVL), demonstrating rapid adoption and growth.

### Core Features and Technical Specifications

Mantle Network is built upon a unique modular architecture that distinguishes it from monolithic blockchains. This design separates fundamental blockchain functions—execution, consensus, settlement, and data availability (DA)—into distinct layers. This modularity allows each layer to specialize, leading to enhanced efficiency, lower fees, and improved performance for DApps.

Mantle leverages **Optimistic Rollup technology** to scale Ethereum transactions. This technology processes transactions off-chain in batches, assuming their validity by default, which drastically reduces gas fees and accelerates transaction times. A challenge period is implemented, during which users can submit fraud proofs if they suspect an invalid transaction. If a fraud is proven, the validator's bond is slashed, incentivizing honest behavior. Mantle is also transitioning to a **Zero-Knowledge (ZK) validity rollup** using Succinct's SP1, which will further reduce transaction finality times from seven days to as low as one hour. This ZK transition aims to bring institutional-grade asset settlements to the network.

For **data availability**, Mantle uniquely employs **EigenDA**, a product developed from EigenLayer, moving the data availability layer off Ethereum. This significantly reduces costs and increases bandwidth compared to posting data directly on Ethereum's Layer 1 blockchain. Mantle's data availability nodes, powered by EigenDA, store rollup transaction records and make them accessible for retrieval during fraud-proof challenges.

Mantle maintains **EVM compatibility**, allowing developers to seamlessly migrate existing Ethereum applications and smart contracts with minimal modifications. The network aims for a throughput of 1,000 transactions per second and a latency for L2 transaction confirmation of 3 seconds. Actual reported block time is around 10 milliseconds, and transaction speed is 500 TPS, which is approximately 20 times faster than Ethereum's 32 TPS. Mantle claims an over 80% reduction in gas fees compared to Ethereum mainnet.

### Consensus Mechanism

Mantle Blockchain integrates a hybrid consensus mechanism that combines elements of Proof of Stake (PoS) and Delegated Proof of Stake (DPoS) to ensure high throughput and security. As a Layer-2 solution built on Ethereum, Mantle inherits security from the underlying Ethereum PoS consensus algorithm.

A key innovation in Mantle's consensus approach involves the use of **Multi-Party Computation (MPC) nodes**. These MPC nodes independently compute state roots from transaction data and provide signatures for valid state transitions. As more nodes sign a block, the collective confidence in the block's validity increases, which creates a viable path for significantly reducing the optimistic rollup's challenge period—from the standard 7 days to as low as 1-2 days, and potentially even 1 hour with the upcoming ZK validity rollup transition. This mechanism transforms optimistic rollups from "default optimistic" to "verifiably optimistic" by providing cryptographic evidence to support network optimism.

Mantle also intends to deploy a permissionless cluster of decentralized sequencers to execute and authorize transactions. This decentralized sequencer model aims to remove single points of failure, enhance the network's availability, and prevent manipulation or censorship, thereby improving the reliability of network consensus. While MPC nodes and fraud verification mechanisms are critical for security, the future integration of ZK validity proofs (via Succinct's SP1) will offer an even higher tier of security by cryptographically verifying transactions.

### Applications and Use Cases

The Mantle ecosystem supports a comprehensive array of applications, leveraging its high scalability, low fees, and Ethereum-level security.

**Decentralized Finance (DeFi)** is a primary focus for Mantle, hosting numerous projects including Decentralized Exchanges (DEXs) like MantleSwap, which processed $50 million in transactions over one month, and Merchant Moe, designed specifically for the Mantle ecosystem. Other DeFi applications include lending and borrowing protocols such as Liquidity Hook Money Market, MethLab, INIT Capital, Timeswap, and MYSO Finance, enabling users to access yield strategies and manage crypto positions. Mantle also supports liquidity protocols like Fluid and capital efficiency focused DEXs such as Agni Finance. Initiatives like the mETH Protocol, a liquid ETH staking and restaking protocol, and FBTC, a decentralized Bitcoin solution, are core to Mantle's financial offerings, maximizing yields and unlocking new financial opportunities. Mantle's mETH has rapidly grown to be the fourth-largest Ethereum liquid staking derivative (LSD) product, with over 480,000 ETH staked and a TVL of $1.22 billion. The introduction of cmETH as a liquid re-staking token further expands yield opportunities.

**NFT Marketplaces** are well-represented, with platforms like Mantle Marketplace, launched in 2021, and Mintle (powered by Rarible) serving as hubs for digital collectibles and art. These platforms prioritize user-friendly interfaces and robust security measures.

**Gaming dApps** are a significant area of focus for Mantle, with Game7, a prominent Web3 gaming incubator, being a key partner. Successful games like Catizen, a Telegram-based game, and Dungeon Degens demonstrate Mantle's potential in Web3 gaming. Other gaming projects include Aria, Spot Zero, and L3E7, offering immersive experiences and integration of Web2 and Web3 elements. Mantle's gaming division is led by industry veterans to provide substantial support to game developers.

Mantle is also pioneering financial services integration with the launch of **UR**, described as the world's first blockchain-based neobank. UR aims to bridge traditional finance (TradFi) and decentralized finance (DeFi) by offering unified accounts for fiat and crypto assets, Swiss IBAN accounts supporting multiple currencies (EUR, CHF, USD, RMB), and Mastercard debit cards. It integrates traditional banking rails like SWIFT and SEPA with blockchain networks such as Ethereum and Arbitrum, with plans to support Base and Mantle Network in the future.

Beyond these specific applications, Mantle's ecosystem also supports various infrastructure projects, analytics platforms like Arkham Intelligence, and tools for multi-chain trading and liquidity aggregation, such as ODOS and Hyperlane. The platform is continuously expanding, attracting established projects like Pendle and Rarible.

### Tokenomics and Native Token

The native token of the Mantle Network is **MNT**. MNT serves a dual purpose as both a **governance token** and a **utility token** within the Mantle ecosystem.

As a **utility token**, MNT is primarily used to pay for gas fees on the Mantle Network, creating inherent demand as network usage grows. It can also serve as collateral for Mantle Network nodes, incentivizing participation and contributing to network security and stability. Additionally, MNT tokens are used in liquidity mining and other ecosystem incentives across Mantle's dApps and partner protocols. Users can acquire MNT tokens through exchanges, direct transfers, or by staking.

As a **governance token**, each MNT token carries equal voting weight, allowing holders to participate in the decision-making process through DAO voting. This ensures a decentralized and community-driven approach to shaping the future of the Mantle ecosystem. Token holders influence strategic directions, organizational structuring, modifications to tokenomics, and the launch of new initiatives, including the allocation of the Mantle Treasury funds.

The total supply of MNT tokens is approximately 6.219 billion. Approximately 3 billion MNT tokens (around 51%) are currently in circulation, while the remaining 49% (about 3.17 billion MNT) are held in the **Mantle Treasury**. This treasury, with a value of over $4.3 billion in asset reserves as of December 2024, is managed by the Mantle DAO and funds various initiatives such as grants, liquidity mining, R&D, and partnerships. A significant portion of this is the $200 million EcoFund, which is dedicated to supporting projects and builders within the ecosystem. The MNT tokenomics emphasize a fixed supply with no ongoing inflation, which allows for potential deflationary mechanisms like future fee burns. MNT is an ERC-20 token on Ethereum and a standard bridge-wrapped ERC-20 token on Layer 2.

### Governance Structure

Mantle Blockchain implements a hybrid governance model that integrates both on-chain and off-chain components to foster a community-driven approach. At the core of this structure is the **MNT token**, which grants holders equal voting weight in the decision-making processes of the Mantle Decentralized Autonomous Organization (DAO). This allows the community to actively participate in shaping the future of the Mantle ecosystem.

Governance activities are transparent and accessible through various platforms. Community discussions and proposals are typically initiated and debated on the **Discourse Forum**. Voting on these proposals then takes place via **Snapshot**, an off-chain voting platform. All major decisions, from protocol upgrades and funding allocations to changes in tokenomics and the launch of new initiatives, are determined by MNT token holders. The Mantle Governance process, which includes a strict procedure for budgeting, capital calls, and distribution, governs the MNT token's allocation.

The Mantle Treasury, one of the largest community-owned treasuries globally with over $4.3 billion in assets, falls under the authority of Mantle Governance. The interest revenue generated from this treasury can be directed back to users as ecosystem incentives, like EigenLayer's restaking rewards, fostering user engagement. Core contributors propose and execute governance decisions, often advised by specialized committees. Changes to the Mantle ecosystem are formalized through Mantle Improvement Proposals (MIPs), which serve as a structured mechanism for proposing and discussing changes within the community. Mantle emphasizes decentralization as a priority, with plans to decentralize its sequencer to enhance network resilience and security.

### Organizational Background and Team

Mantle Network, a funded company, was founded in 2019 and is based in Panama City, Panama. The project was initially developed by BitDAO, and it evolved to integrate BitDAO's substantial governance and treasury. This transition was formalized in May 2023 when the BitDAO community voted to merge and rebrand under Mantle, consolidating the project's structure and tokenomics.

The core development team behind Mantle includes approximately 25 individuals. Notable figures include Arjun Krishan Kalsy, an expert in Ethereum and Web3 scaling, and Joshua Lapidus. The project benefits from the involvement of key advisors such as Ben Zhou, co-founder of Bybit, which also provides financial support to the project.

Mantle has recently expanded its leadership team with strategic hires from both traditional finance (TradFi) and Web3 sectors to accelerate its vision of bridging conventional finance with blockchain innovation. Key executive appointments include:
*   **Thomas Chen**: CEO of Function, leading the development of 𝑓BTC (FBTC), a standard Bitcoin yield primitive. He previously served as Managing Director and Global Head of Sales at BitGo.
*   **Brian Trunzo**: Chief Growth Officer at Mantle Network, bringing expertise from his role as VP and Global Head of Business Development at Polygon Labs.
*   **Sohan Sen**: Group Head of Structured Products at Mantle, with extensive experience in financial markets from roles at Paradigm, Morgan Stanley, and Goldman Sachs.
*   **Tim Chen**: Group Head of Strategy at Mantle, with significant experience from MSA Novo, a global venture fund.
*   **Jordi Alexander**: Chief Alchemist at Mantle, spearheading MantleX, an AI-augmented division for deploying advanced AI agents within the ecosystem.
*   **Yaxi Zhu**: Co-Founder of Bybit and Founding Partner at Mirana Ventures, guiding the development of Mantle Banking, a full-suite blockchain-based financial services platform.

These appointments underscore Mantle's commitment to establishing institutional-grade blockchain infrastructure and sustainable yield products. Mirana Ventures, a venture capital firm, provides continuous funding and resource support to the Mantle ecosystem. The Mantle team is actively engaged with the community, addressing questions and concerns through channels like Discord, Telegram, and Twitter. Mantle also fosters collaboration through initiatives like Mantle Learn (in partnership with HackQuest) and the Mantle Build the State initiative, encouraging developers and community members.

### Recent Developments and Roadmap

Mantle Blockchain continues to evolve, with several significant developments and future plans. A major recent launch is **UR**, the world's first blockchain-based neobank, introduced by Mantle in June 2025. UR aims to seamlessly integrate traditional banking services with crypto and decentralized finance, allowing users to manage fiat and crypto assets in a single, unified account. It offers Swiss IBAN accounts supporting multiple currencies (EUR, CHF, USD, RMB) and Mastercard debit cards, backed by tokenized deposits under Swiss banking licenses. Initially, fund transfers are conducted via SWIFT, SEPA, and Ethereum, with future plans to include Base and Mantle Network. UR plans to expand its services by 2025 to include foreign exchange, fiat-to-crypto on-ramps, and yielding and lending tools. The current launch is for early contributors, with full public access scheduled for Q3 2025.

In terms of technical advancements, Mantle Network is advancing its roadmap by transitioning from an optimistic rollup model to a **zero-knowledge (ZK) validity rollup** using **Succinct's SP1**. This architectural change is expected to drastically reduce transaction finality times from seven days to one hour, enabling faster institutional-grade asset settlements and enhancing security. The testnet launch for this ZK validity rollup is set for Q1 2025, with mainnet upgrade intentions. This move aligns Mantle Network with Ethereum's security ethos while laying the groundwork for cross-rollup interoperability. Key technical benefits of this transition include fast finality, EVM equivalence (allowing developers to leverage existing Ethereum tooling), and cost efficiency through integrated prover fees.

The **MNT token** has also seen positive market reaction, notably with its addition to Coinbase's roadmap in April 2025. This move typically signals increased liquidity and retail investor interest, leading to an 8.3% price surge for MNT within 24 hours of the announcement. Mantle Network is committed to fostering its ecosystem, evidenced by the $200 million EcoFund that supports projects building on Mantle. Future developments also include enhancements to staking with the Mantle Liquidity Staking Protocol (LSP), allowing users to stake ETH for yield-bearing mETH, and continued strategic partnerships to enhance interoperability and ecosystem expansion. Mantle also actively promotes gaming via Telegram-based mini-apps, with titles like Catizen highlighting the platform's capabilities for decentralized games and aiming to lower the barrier to entry for Web3 adoption.

Bibliography
A Beginner’s Guide to Mantle Blockchain | Gem Wallet. (2024). https://gemwallet.com/learn/beginners-guide-to-mantle-blockchain/

Blog - Mantle Network | Building the Liquidity Chain of the Future. (2025). https://www.mantle.xyz/blog

Coinbase Adds Mantle (MNT) to Roadmap: Adam and Eve Pattern ... (2025). https://blockchain.news/flashnews/coinbase-adds-mantle-mnt-to-roadmap-adam-and-eve-pattern-signals-bullish-momentum

Emerging Layer 1 Blockchain: A Deep Dive into Mantle’s Ecosystem. (2024). https://www.gate.com/learn/articles/emerging-layer-1-blockchain-a-deep-dive-into-mantles-ecosystem-from-fundamentals-to-ecosystem/5092

Exploring Use Cases: Mantle for Gaming dApps - Medium. (2023). https://medium.com/0xmantle/exploring-use-cases-mantle-for-gaming-dapps-566af6101010

Get Your Endpoint for Mantle | Ankr Web3 API. (2024). https://www.ankr.com/web3-api/chains-list/mantle/

Investing In Mantle (MNT) - Everything You Need to Know. (2025). https://www.securities.io/investing-in-mantle-mnt/

MANTLE Blockchain Bank Goes Live: What Next For MNT Price? (2025). https://99bitcoins.com/news/mantle-crypto-blockchain-bank-goes-live-what-does-it-mean-for-mnt-price-in-june/

Mantle Expands Global Leadership for Blockchain Growth. (2025). https://group.mantle.xyz/blog/announcements/mantle-strengthens-global-leadership

Mantle Expands Leadership Team With Key Hires from TradFi, Web3. (2025). https://www.blockhead.co/2025/02/13/mantle-expands-leadership-team-with-key-hires-from-tradfi-web3/

Mantle Governance Consensus Mechanisms Proof of Stake (PoS ... (2023). https://bomacodes.hashnode.dev/mastering-mantle-governance-exploring-pos-and-dpos-consensus-mechanisms

Mantle launches UR, world’s first fully blockchain-based neobank. (2025). https://cointelegraph.com/press-releases/mantle-launches-ur-world-s-first-fully-blockchain-based-neobank

Mantle Launches World’s First Blockchain Neobank as MNT Token ... (2025). https://yellow.com/news/mantle-launches-worlds-first-blockchain-neobank-as-mnt-token-gains-2-amid-market-decline

Mantle Launches World’s First Blockchain-Based Neobank UR. (2025). https://www.ainvest.com/news/mantle-launches-world-blockchain-based-neobank-ur-2506/

Mantle (MNT) Live Tokenomics, Charts, Ratings & News | TokenInsight. (2023). https://tokeninsight.com/en/coins/mantle/tokenomics

Mantle Network | Building the Liquidity Chain of the Future. (2024). https://www.mantle.xyz/

Mantle Network - 2025 Company Profile & Team - Tracxn. (n.d.). https://tracxn.com/d/companies/mantle-network/__HSET_Qs1HCkRJXOSew3g0rOkPW2sVGF5_Is8OWUK9To

Mantle Network - Medium. (n.d.). https://medium.com/@mantlenetwork.eth

Mantle Network Advances Technical Roadmap As The First ZK ... (2024). https://bravenewcoin.com/insights/mantle-network-advances-technical-roadmap-as-the-first-zk-validity-rollup-with-succincts-sp1

Mantle Network: An Emerging Modular L2 Ecosystem. (2023). https://research.nansen.ai/articles/mantle-network-an-emerging-modular-l2-ecosystem

Mantle Network dApps. (n.d.). https://www.mantle.xyz/dapp

Mantle Network. Progressive Ethereum Layer 2 Solution | by Satyam. (2023). https://blog.blockmagnates.com/mantle-network-c8e1712b53a8

Mantle: The Future of On-Chain Finance & Banking. (2025). https://group.mantle.xyz/

Mantle: Unlocking the Potential of Modular Blockchain Scaling. (2023). https://www.mantle.xyz/blog/developers/mantle-unlocking-the-potential-of-modular-blockchain-scaling

The Governance of Mantle Network - Lemma Solutions. (2024). https://www.lemma.solutions/insights/the-governance-of-mantle-network

TON and Mantle Set to Reveal 2025 Infrastructure Investments ... (2025). https://www.prnewswire.com/in/news-releases/ton-and-mantle-set-to-reveal-2025-infrastructure-investments--incubation-roadmap-on-bybit-web3-livestream-302370041.html

What is Mantle? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/mantle

What is Mantle? A Complete Guide to Mantle (MNT) - Nansen. (2025). https://www.nansen.ai/post/what-is-mantle-a-complete-guide-to-mantle-mnt

What is Mantle and the MNT Token. Key Takeaways | by XT Exchange. (2025). https://medium.com/@XT_com/what-is-mantle-and-the-mnt-token-3411d1ceb843

What Is Mantle (MNT)? Everything You Need to Know - Coins.ph. (2025). https://coins.ph/academy/what-is-mantle-mnt-everything-you-need-to-know/

What is Mantle? MNT Explained #2643 - LearnCrypto. (2025). https://learncrypto.com/popular-coins/mantle

What Is Mantle Network? Enabling Modular Blockchain Scaling. (2024). https://www.coingecko.com/learn/mantle-modular-blockchain-scaling

What is Mantle Network: Ethereum’s first modular Layer-2 solution. (2024). https://web3.okx.com/learn/what-is-mantle-network

What is Mantle? The Guide to the Modular Blockchain - thirdweb blog. (2024). https://blog.thirdweb.com/mantle-modular-blockchain-ecosystem-expansion-and-developer-support/



Generated by Liner
https://getliner.com/search/s/5926611/t/85975132