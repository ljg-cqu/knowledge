List all order-book based DEX blockchain on Polkadot SDK/ecosystem, along with their TPS and github links info

Thu Jul 10 2025

### Order-book Based DEX Blockchains on Polkadot SDK/Ecosystem

The following are notable order-book based decentralized exchange (DEX) blockchains built on the Polkadot SDK or within the Polkadot ecosystem, with details on their transactions per second (TPS) metrics and official GitHub repositories.

#### 1. Polkadex

- **Description**: Polkadex is a fully decentralized, non-custodial, peer-to-peer order-book based exchange built using Substrate, designed to merge the best features of centralized and decentralized exchanges. It offers high-performance, low-latency trading with a fully decentralized order book. Users can trade assets across different parachains within the Polkadot ecosystem and external blockchains connected via bridges. Polkadex also utilizes Layer 2 scaling solutions for efficient trading and operates on a non-custodial model, allowing users to retain control of their funds.
- **TPS (Transactions Per Second)**:
  - **Max Theoretical TPS**: Polkadex has a max theoretical TPS of 1,500 transactions per second.
  - **Maximum Claimed TPS (with TEE, for high-frequency trading scenarios)**: It is capable of up to 500,000 transactions per second (TPS) with sub-millisecond latency.
  - **Testnet Speed**: Polkadex was operating in a testnet capable of reaching a speed of 300 transactions per second (tps) as of January 2023, with a target throughput of 20,000 tps.
  - **Real-time TPS (recent readings)**: Polkadex TPS is 0.0011 transactions per second.
  - **Max Recorded TPS**: Polkadex Max TPS is 0.79 transactions per second.
- **GitHub Links**:
  - **Main Repository**: (https://github.com/Polkadex-Substrate/Polkadex). This repository focuses on the order-book based decentralized exchange using the Substrate Blockchain Framework.
  - **Organization Page**: (https://github.com/polkadex-substrate). Polkadex-Substrate has 126 repositories available.
  - **Ethereum Relayer**: (https://github.com/Polkadex-Substrate/eth-relayer). This relayer service streams transactions from blockchain networks and sends packets to the correlated bridge component, used for migrating ERC20 PDEX to Native PDEX.
  - **Ledger App**: (https://github.com/LedgerHQ/app-polkadex). This project contains the Polkadex app for Ledger Nano S and X.

#### 2. Polkaswap

- **Description**: Originally an Automated Market Maker (AMM) DEX, Polkaswap has evolved into a hybrid model, incorporating a fully decentralized on-chain order book alongside its AMM. It functions as a cross-chain liquidity aggregator DEX protocol for swapping tokens based on Polkadot and Kusama networks.
- **TPS**: Specific TPS figures for its order book are not explicitly provided in the public documents. The platform is designed for constant on-chain settlement.
- **GitHub Links**:
  - **Web Frontend**: (https://github.com/sora-xor/polkaswap-web).
  - **Exchange Web**: (https://github.com/sora-xor/polkaswap-exchange-web).
  - **Token Whitelist Configuration**: (https://github.com/sora-xor/polkaswap-token-whitelist-config). This repository contains the file where all whitelisted (safe) tokens are presented.
  - **Pricing Server**: (https://github.com/sora-xor/pricing-server). This is an analytics server for Polkaswap.
  - **Organization Page**: (https://github.com/orgs/sora-xor/repositories). The sora-xor organization has 80 repositories.

#### 3. dTrade

- **Description**: dTrade is a synthetic asset issuance protocol and an order-book based DEX for Polkadot, emphasizing high-performance trading and sub-second settlement. Documentation on its TPS or backend performance is minimal and lacks specific technical details.
- **TPS**: No explicit TPS values have been specified in the publicly available references.
- **GitHub Links** (related, but official Polkadot/Substrate-based DEX status unconfirmed in documents):
  - **Community Fork**: (https://github.com/KarthikS373/DTrade). This repository describes itself as a comprehensive cryptocurrency trading platform with real-time market data, spot and limit order trading, portfolio management, and profile customization.
  - **Another Project with "DTrade" in Name**: (https://github.com/DKotzer/DTrade) and (https://github.com/lukasyelle/DTrade). These may represent prototypes or community forks not directly confirmed as the Polkadot-native dTrade. One such project allows users to buy/sell cryptocurrencies based on current prices on the Kraken trading platform. Another analyzes trends from external sources to provide indicators and targets for buy/sell points.

### TPS Summary Table

| DEX | Max Theoretical TPS | Max Claimed TPS | Real-time/Current TPS | GitHub Main Repositories |
| :---------- | :------------------ | :---------------- | :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Polkadex | 1,500 | 500,000 | 0.0011 | (https://github.com/Polkadex-Substrate/Polkadex) |
| Polkaswap | Not specified | Not specified | Not specified | (https://github.com/sora-xor/polkaswap-web) |
| dTrade | Not specified | Not specified | Not specified | (https://github.com/KarthikS373/DTrade) |

### Key Takeaways

- Polkadex is a prominent order-book based DEX within the Polkadot ecosystem, actively developing and making specific claims about high TPS capabilities, especially for high-frequency trading scenarios.
- Both Polkadex and Polkaswap maintain well-documented GitHub repositories, providing transparency and access to their codebase.
- While other DEXs exist in the Polkadot ecosystem, many are primarily AMM-based, or their order-book functionalities and performance metrics are not extensively detailed in public documentation.

Bibliography
All repositories - Polkadex-Substrate - GitHub. (2025). https://github.com/orgs/Polkadex-Substrate/repositories

Build on Polkadex with our RPC API and Fast Nodes - OnFinality. (n.d.). https://onfinality.io/networks/polkadex

Cross-Chain Bridging is Now Integrated into Polkadex Orderbook. (2024). https://polkadex.medium.com/cross-chain-bridging-is-now-integrated-into-polkadex-orderbook-ab04db7fd1e7

dTrade - All information about dTrade ICO (Token Sale) - ICO Drops. (2021). https://icodrops.com/dtrade/

DTrade - Project 2 for GA SEI 48 using mongo/express/node. - GitHub. (2022). https://github.com/DKotzer/DTrade

@dtradeorg/dtrade-ts - npm. (2022). https://www.npmjs.com/package/%40dtradeorg%2Fdtrade-ts

Dynatrace/easytrade - GitHub. (n.d.). https://github.com/Dynatrace/easytrade

Exploring Order Book DEXs: Why Polkadex and D5 Exchange Will ... (2023). https://blog.rockx.com/order-book-dex-crypto-trading/

github.com/polkadex-substrate/chainbridge-utils | Go. (2021). https://deps.dev/go/github.com%2Fpolkadex-substrate%2Fchainbridge-utils/v1.0.9

How to trade on Polkadex Orderbook - Medium. (2022). https://polkadex.medium.com/how-to-trade-on-polkadex-orderbook-8484d229e56c

I bring to you a legit moonshot - Polkadex. : r/CryptoCurrency - Reddit. (2022). https://www.reddit.com/r/CryptoCurrency/comments/txmrmx/i_bring_to_you_a_legit_moonshot_polkadex/

Introducing the Polkaswap Testnet - Medium. (2020). https://medium.com/polkaswap/introducing-the-polkaswap-testnet-fa85dd8582c0

Issues · sora-xor/polkaswap-exchange-web - GitHub. (2025). https://github.com/sora-xor/polkaswap-exchange-web/issues

KarthikS373/DTrade: A comprehensive cryptocurrency ... - GitHub. (2023). https://github.com/KarthikS373/DTrade

LedgerHQ/app-polkadex - GitHub. (2022). https://github.com/LedgerHQ/app-polkadex

List of 4 Decentralized Exchanges (DEXs) on Polkadot - Alchemy. (n.d.). https://www.alchemy.com/list-of/decentralized-exchanges-dexs-on-polkadot

lukasyelle/DTrade - GitHub. (2018). https://github.com/lukasyelle/DTrade

man-group/dtale: Visualizer for pandas data structures - GitHub. (2019). https://github.com/man-group/dtale

POLKADEX | TVL, Protocols,Tokens - Coinpedia Market. (2024). https://markets.coinpedia.org/blockchain/polkadex/

Polkadex - GitHub. (n.d.). https://github.com/polkadex-substrate

Polkadex - Golden. (n.d.). https://golden.com/wiki/Polkadex-K3E4ZDE

Polkadex - RadiumBlock. (2024). https://www.radiumblock.com/polkadex.html

Polkadex is struggling! - Reddit. (2021). https://www.reddit.com/r/polkadex/comments/r75q7j/polkadex_is_struggling/

Polkadex on X: "#Polkadex Developer Updates  ‍   Polkadex ... (2025). https://twitter.com/polkadex/status/1377671645159059459

POLKADEX ORDERBOOK - Pontem Network. (2022). https://pontem.network/posts/polkadex-orderbook

Polkadex Orderbook Automates DEX Trading with Hummingbot ... (2023). https://polkadex.medium.com/polkadex-orderbook-automates-dex-trading-with-hummingbot-integration-db71192ba879

Polkadex Orderbook Security Audit: A Case Study - Hacken. (2023). https://hacken.io/case-studies/polkadex-audit/

Polkadex: Polkadot’s DEX for the DeFi ecosystem - Boxmining. (2023). https://boxmining.com/polkadex/

Polkadex project details | Polkadot network - Parachains.info. (2023). https://parachains.info/details/polkadex

Polkadex, the Best Order Book DEX on the Market? - Altcoin Buzz. (2023). https://www.altcoinbuzz.io/product-release/polkadex-the-best-order-book-dex-on-the-market/

Polkadex [TPS, Max TPS, Block Time & TTF] | Chainspect. (2021). https://chainspect.app/chain/polkadex

Polkadex vs Polygon [TPS, Max TPS, Block Time] - Chainspect. (2020). https://chainspect.app/compare/polkadex-vs-polygon

Polkadex: Why We Invested - GD10 Capital. (n.d.). https://gd10.capital/insights/polkadex-why-we-invested

Polkadex-Substrate/eth-relayer: Relays Ethereum Block ... - GitHub. (2021). https://github.com/Polkadex-Substrate/eth-relayer

Polkadex-Substrate/Polkadex: An Orderbook-based Decentralized ... (2020). https://github.com/Polkadex-Substrate/Polkadex

Polkaswap | Trade with Style and Freedom - X. (n.d.). https://x.com/polkaswap?lang=en

Polkaswap — The DEX for the Interoperable Future. (n.d.). https://polkaswap.io/

Polkaswap Price Prediction｜PSWAP Price Forecast & Trends - BingX. (2024). https://bingx.com/en/price/Polkaswap/price-prediction

Polkaswap Price, PSWAP Price, Live Charts, and Marketcap. (2021). https://www.coinbase.com/price/polkaswap

Polkaswap (PSWAP) Price Today, News & Live Chart - Forbes. (2025). https://www.forbes.com/digital-assets/assets/polkaswap-pswap/

polkaswap-web/index.html at master - GitHub. (2020). https://github.com/sora-xor/polkaswap-web/blob/master/index.html

Polygon vs Polkadex [TPS, Max TPS, Block Time] - Chainspect. (2020). https://chainspect.app/compare/polygon-vs-polkadex

Pull requests 17 - sora-xor/polkaswap-exchange-web - GitHub. (2025). https://github.com/sora-xor/polkaswap-exchange-web/pulls

Releases · Polkadex-Substrate/Polkadex - GitHub. (2024). https://github.com/Polkadex-Substrate/Polkadex/releases

Releases · sora-xor/polkaswap-exchange-web - GitHub. (2025). https://github.com/sora-xor/polkaswap-exchange-web/releases

Repositories - sora-xor - GitHub. (2025). https://github.com/orgs/sora-xor/repositories

r/Polkaswap - Reddit. (2020). https://www.reddit.com/r/Polkaswap/

sora-xor/polkaswap-exchange-web - GitHub. (2020). https://github.com/sora-xor/polkaswap-exchange-web

sora-xor/polkaswap-token-whitelist-config - GitHub. (2021). https://github.com/sora-xor/polkaswap-token-whitelist-config

sora-xor/polkaswap-web - GitHub. (2020). https://github.com/sora-xor/polkaswap-web

sora-xor/pricing-server: Analytics server for Polkaswap - GitHub. (2021). https://github.com/sora-xor/pricing-server

What about a DEX with limit orders, no gas fees and 500k tps? Meet ... (2022). https://www.reddit.com/r/CryptoCurrency/comments/w2g3ss/what_about_a_dex_with_limit_orders_no_gas_fees/

What Is Polkadex? | CoinMarketCap. (2021). https://coinmarketcap.com/academy/article/what-is-polkadex



Generated by Liner
https://getliner.com/search/s/5926611/t/86407202