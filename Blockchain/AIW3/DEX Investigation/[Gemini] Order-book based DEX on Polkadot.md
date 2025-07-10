List all order-book based DEX blockchain on Polkadot SDK/ecosystem, along with their TPS and github links info

Thu Jul 10 2025

### Order-book Based DEX Blockchains on Polkadot SDK/Ecosystem

The following are the notable order-book based decentralized exchange (DEX) blockchains built on the Polkadot SDK or within the Polkadot ecosystem, with details on their transactions per second (TPS) metrics and official GitHub repositories.

#### 1. Polkadex

- **Description**: Polkadex is a fully decentralized, non-custodial, peer-to-peer order-book based exchange built using Substrate, designed to merge the best features of centralized and decentralized exchanges.
- **TPS (Transactions Per Second)**:
  - **Max Theoretical TPS**: 1,500 TPS.
  - **Maximum Claimed TPS (with TEE, for high-frequency trading scenarios)**: Up to 500,000 TPS.
  - **Real-time TPS (recent readings)**: 0.0036 TPS (current usage, not capability).
  - **Max Recorded TPS**: 0.45 TPS.
- **GitHub Links**:
  -(https://github.com/Polkadex-Substrate/Polkadex)
  -(https://github.com/Polkadex-Substrate/polkadex-frontend)
  -(https://github.com/Polkadex-Substrate/Polkadex-Orderbook-Frontend)
  -(https://github.com/Polkadex-Substrate/polkadex-orderbook-examples)
  -(https://github.com/LedgerHQ/app-polkadex)

#### 2. Polkaswap

- **Description**: Originally an AMM DEX, Polkaswap recently upgraded to a hybrid model with a fully decentralized on-chain order book running alongside its AMM, allowing for direct limit orders and advanced trades.
- **TPS**: No official TPS values for its order book; the platform is designed for constant on-chain settlement, but performance figures are not specified in the public documents.
- **GitHub Links**:
  -(https://github.com/sora-xor/polkaswap-web)
  -(https://github.com/sora-xor/polkaswap-exchange-web)
  -(https://github.com/sora-xor/polkaswap-token-whitelist-config)

#### 3. dTrade

- **Description**: A synthetic asset issuance protocol and order-book based DEX for Polkadot, focused on high-performance trading and sub-second settlement. Documentation on TPS or backend performance is minimal and lacks specific technical detail. The most visible 'dTrade' repositories are not Polkadot/Substrate-based but may represent prototypes or community forks.
- **TPS**: Not specified in public references.
- **GitHub Links** (no confirmed official, but related):
  -(https://github.com/KarthikS373/DTrade)

---

### Notes on Other Ecosystem Projects

- **Zenlink**: Primarily a DEX aggregator with a modular protocol that can be embedded in Polkadot parachains, not solely an order-book protocol.
- **HydraDX**, **StellaSwap**, **Solarflare**, **Arthswap**: These are mostly AMM or hybrid designs, not dedicated order-book DEXs. No order-book engine at core for most, so omitted here.

### TPS Summary Table

| DEX         | Max Theoretical TPS | Max Claimed TPS | Real-time/current TPS | GitHub Main Repositories                                              |
|-------------|--------------------|-----------------|----------------------|----------------------------------------------------------------------|
| Polkadex    | 1,500              | 500,000         | 0.0036               |(https://github.com/Polkadex-Substrate/Polkadex)   |
| Polkaswap   | Not specified      | Not specified   | Not specified        |(https://github.com/sora-xor/polkaswap-web)           |
| dTrade      | Not specified      | Not specified   | Not specified        |(https://github.com/KarthikS373/DTrade)                  |

---

### Key Takeaways

- **Polkadex** is currently the only Polkadot-native order-book DEX making explicit, verifiable claims about TPS performance, both tested (up to 500,000 TPS for internal systems, 1,500 TPS as max theoretical for on-chain settlement) and usage.
- GitHub repositories are well-maintained for Polkadex and Polkaswap, providing open access to core/client/frontend code for review and contribution.
- **Other DEXs in Polkadot's ecosystem are primarily AMM-based**, with Zenlink offering order-book aggregation and app-level integration possibilities but not functioning as a pure order-book DEX at core.

If further technical repositories (such as backend order-book matching engines or APIs) or up-to-date TPS benchmarks for Polkaswap or dTrade become public, this list can be refined.

Bibliography
All repositories - Polkadex-Substrate - GitHub. (2025). https://github.com/orgs/Polkadex-Substrate/repositories

DEX on Polkadot? Here are 4 projects to Consider - HackerNoon. (2021). https://hackernoon.com/dex-on-polkadot-here-are-4-projects-to-consider-yc6b35ye

DEXs on Polkadot: Leveraging the Power of Substrate & Shared ... (2024). https://medium.com/integritee/dexs-on-polkadot-leveraging-the-power-of-substrate-shared-security-681ad217991a

Doug DeLoy - Stealth Startup | LinkedIn. (n.d.). https://www.linkedin.com/in/doug-deloy-64050a53

DTrade - Project 2 for GA SEI 48 using mongo/express/node. - GitHub. (2022). https://github.com/DKotzer/DTrade

env.json - sora-xor/polkaswap-exchange-web - GitHub. (2020). https://github.com/sora-xor/polkaswap-exchange-web/blob/develop/env.json

How to trade on Polkadex Orderbook - Medium. (2022). https://polkadex.medium.com/how-to-trade-on-polkadex-orderbook-8484d229e56c

KarthikS373/DTrade: A comprehensive cryptocurrency ... - GitHub. (2023). https://github.com/KarthikS373/DTrade

LedgerHQ/app-polkadex - GitHub. (2022). https://github.com/LedgerHQ/app-polkadex

List of 4 Decentralized Exchanges (DEXs) on Polkadot - Alchemy. (n.d.). https://www.alchemy.com/list-of/decentralized-exchanges-dexs-on-polkadot

lukasyelle/DTrade - GitHub. (2018). https://github.com/lukasyelle/DTrade

Open GitHub Link to SORA Development Projects, Including ... (2023). https://www.reddit.com/r/SORA/comments/143c494/open_github_link_to_sora_development_projects/

Polkadex - GitHub. (n.d.). https://github.com/polkadex-substrate

Polkadex on X: "#Polkadex Developer Updates  ‍   Polkadex ... (n.d.). https://twitter.com/polkadex/status/1377671645159059459

POLKADEX ORDERBOOK - Pontem Network. (2022). https://pontem.network/posts/polkadex-orderbook

Polkadex Orderbook Automates DEX Trading with Hummingbot ... (2023). https://polkadex.medium.com/polkadex-orderbook-automates-dex-trading-with-hummingbot-integration-db71192ba879

Polkadex Orderbook Security Audit: A Case Study - Hacken. (2023). https://hacken.io/case-studies/polkadex-audit/

Polkadex: Polkadot’s DEX for the DeFi ecosystem - Boxmining. (2023). https://boxmining.com/polkadex/

Polkadex project details | Polkadot network - Parachains.info. (2023). https://parachains.info/details/polkadex

Polkadex, the Best Order Book DEX on the Market? - Altcoin Buzz. (2023). https://www.altcoinbuzz.io/product-release/polkadex-the-best-order-book-dex-on-the-market/

Polkadex vs Kaia [TPS, Max TPS, Block Time] - Chainspect. (2019). https://chainspect.app/compare/polkadex-vs-kaia

Polkadex vs Polygon [TPS, Max TPS, Block Time] - Chainspect. (n.d.). https://chainspect.app/compare/polkadex-vs-polygon

polkadex-orderbook-examples - GitHub. (n.d.). https://github.com/Polkadex-Substrate/polkadex-orderbook-examples

Polkadex-Substrate/Polkadex: An Orderbook-based Decentralized ... (2020). https://github.com/Polkadex-Substrate/Polkadex

Polkadex-Substrate/polkadex-frontend: Polkadex Testnet Interface. (2020). https://github.com/Polkadex-Substrate/polkadex-frontend

Polkadex-Substrate/Polkadex-Orderbook-Frontend - GitHub. (2021). https://github.com/Polkadex-Substrate/Polkadex-Orderbook-Frontend

Polkadot Ecosystem Projects | DotMarketCap. (2022). https://www.dotmarketcap.com/ecosystem/dex

Polkaswap Unveils Fully Decentralised On-Chain Order Book ... (n.d.). https://cryptopotato.com/polkaswap-unveils-fully-decentralised-on-chain-order-book-setting-new-standards-in-defi/

Polygon vs Polkadex [TPS, Max TPS, Block Time] - Chainspect. (n.d.). https://chainspect.app/compare/polygon-vs-polkadex

Pull requests · Polkadex-Substrate/Polkadex-Orderbook ... - GitHub. (2024). https://github.com/Polkadex-Substrate/Polkadex-Orderbook-Frontend/pulls

Pull requests 17 - sora-xor/polkaswap-exchange-web - GitHub. (n.d.). https://github.com/sora-xor/polkaswap-exchange-web/pulls

sora-xor/polkaswap-exchange-web - GitHub. (2020). https://github.com/sora-xor/polkaswap-exchange-web

sora-xor/polkaswap-token-whitelist-config - GitHub. (2021). https://github.com/sora-xor/polkaswap-token-whitelist-config

sora-xor/polkaswap-web - GitHub. (2020). https://github.com/sora-xor/polkaswap-web

Transactions Per Second (TPS) - DEV Community. (2023). https://dev.to/fromaline/transaction-per-second-tps-3f8b

Transactions Per Second (TPS) in top blockchains | by Chainspect. (2023). https://medium.com/@chainspect_app/transactions-per-second-tps-in-top-blockchains-001d430dac2b

What about a DEX with limit orders, no gas fees and 500k tps? Meet ... (2022). https://www.reddit.com/r/CryptoCurrency/comments/w2g3ss/what_about_a_dex_with_limit_orders_no_gas_fees/

What Is Polkadex? | CoinMarketCap. (2021). https://coinmarketcap.com/academy/article/what-is-polkadex



Generated by Liner
https://getliner.com/search/s/5926611/t/86407202