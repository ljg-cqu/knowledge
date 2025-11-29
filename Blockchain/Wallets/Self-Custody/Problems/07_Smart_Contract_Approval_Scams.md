# Smart Contract Approval Scams and Drainer Attacks

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Documentation Team

## Problem Statement

**[CRITICAL]** Q: Self-custody wallet users face sophisticated approval scams and drainer attacks exploiting smart contract permissions, resulting in $500 million in losses during 2024 alone and $3.1 billion in total H1 2025 scam losses. Formulate a structured problem statement using the following [Input] fields.

A:
- **Brief description of the problem to be analyzed**: 
  Self-custody wallet users lose funds through malicious smart contract approval scams and drainer attacks, with $500M in wallet drainer losses in 2024 [Web: Infosecurity Magazine, 2024] and $3.1B total H1 2025 scam losses [Web: Ledger, 2025]. Attackers exploit unlimited token approvals, ERC-20 permit signatures, and legitimate DeFi protocols to drain user wallets, with phishing responsible for 31% of all attacks [Web: Turnkey, 2024].

- **Background and current situation**: 
  Self-custody wallets interact with DeFi protocols via smart contract approvals, granting permission to transfer tokens on the user's behalf. Current approval model allows unlimited token access (e.g., `approve(spender, uint256(-1))` grants infinite allowance) creating persistent vulnerability [Web: Gate.io, 2024]. ERC-20 permit signatures (EIP-2612) enable gas-free approvals via off-chain signatures but are exploited in phishing attacks [Web: Medium Triathon, 2024]. Wallet drainer attacks use: (1) malicious DApps requesting approvals, (2) phishing sites mimicking legitimate protocols (Uniswap, OpenSea), (3) social engineering via Discord/Telegram/Twitter, (4) permit signature phishing for gas-free token theft [Web: Medium Neptune Mutual, 2024]. Users lack visibility into existing approvals across wallets, with 80%+ unaware of approval risks [Assumption: based on user survey reports]. Once approval is granted, attackers can drain funds at any time until revoked. Wallet drainers responsible for $500M losses in 2024 [Web: Infosecurity Magazine, 2024], with phishing accounting for 31% of all crypto attacks in 2024 [Web: Turnkey, 2024].

- **Goals and success criteria**: 
  Approval scam incident rate: $500M losses in 2024 [Web: Infosecurity Magazine, 2024] → <$200M/yr (min) / <$100M/yr (target) / <$30M/yr (ideal) by Q4 2025; User approval awareness: current est. <20% → 60% (min) / 80% (target) / 95% (ideal) by Q3 2025; Unlimited approval usage: current est. 70% of approvals unlimited [Assumption: based on on-chain analysis] → <30% (min) / <15% (target) / <5% (ideal) by Q4 2025; Approval management tool adoption: current est. 10% of users → 50% (min) / 70% (target) / 90% (ideal) by Q2 2026; Average time to detect malicious approval: current est. hours to days → <5min (min) / <1min (target) / real-time (ideal) by Q3 2025

- **Key constraints and resources**: 
  Timeline Q1 2025 - Q2 2026 (18mo); Budget varies by solution: wallet UI improvements $200K-$500K, approval monitoring infrastructure $500K-$1M, user education campaigns $300K-$600K; Technical constraint: backward compatibility with existing ERC-20 and DeFi protocols; User education challenge: explaining complex approval concepts to non-technical users; Development constraint: integrate approval management without degrading UX; Security audit requirements ($100K-$250K for approval monitoring systems); Network constraint: approval revocation requires gas fees (creates user friction)

- **Stakeholders and roles**: 
  Self-custody wallet users (520M+ users globally [Web: CoinLaw, 2025], need protection with <5min approval review time, constraint: varying technical literacy, est. 80%+ unaware of risks); Wallet providers (MetaMask, Trust Wallet, Rainbow, need built-in approval management, constraint: UX simplicity vs security tradeoff); DeFi protocol developers (Uniswap, Aave, Curve, need secure approval patterns, constraint: gas efficiency vs granular permissions); Security researchers (need approval monitoring tools, constraint: cross-chain approval tracking complexity); Approval management services (Revoke.cash, Etherscan token approvals, need user adoption, constraint: require user initiative to check)

- **Time scale and impact scope**: 
  Timeline Q1 2025 - Q2 2026 (18mo); Systems: smart contract approval mechanisms, wallet interfaces, approval monitoring tools, DeFi protocol integrations; Scale: 520M+ wallet users [Web: CoinLaw, 2025], billions in approved token allowances on Ethereum alone, thousands of DeFi protocols requiring approvals; Financial impact: $500M wallet drainer losses in 2024 [Web: Infosecurity Magazine, 2024], $3.1B total H1 2025 scam losses [Web: Ledger, 2025], phishing 31% of attacks [Web: Turnkey, 2024]; Global reach: all EVM-compatible chains (Ethereum, BSC, Polygon, Arbitrum, etc.)

- **Historical attempts and existing solutions (if any)**: 
  Existing solutions: (1) Revoke.cash and similar approval checkers - require manual checking, low adoption est. 10% of users [Assumption: based on tool usage metrics]; (2) Wallet warnings for unlimited approvals - often ignored or dismissed by users; (3) Limited approval patterns (approve exact amounts) - rarely implemented due to UX friction and gas costs; (4) EIP-2612 permit signatures - created new attack vector via off-chain signature phishing [Web: Medium Triathon, 2024]; (5) Time-limited approvals (EIP-1613) - minimal adoption; (6) MetaMask and other wallets added approval simulation - improves visibility but doesn't prevent user error. Key lesson: solutions requiring user initiative (manual checking, setting limits) see low adoption; automated protection needed.

- **Known facts, assumptions, and uncertainties**: 
  - **Facts**: $500M wallet drainer losses in 2024 [Web: Infosecurity Magazine, 2024]; $3.1B total H1 2025 crypto scam losses [Web: Ledger, 2025]; Phishing responsible for 31% of attacks in 2024 [Web: Turnkey, 2024]; Unlimited token approvals create persistent vulnerability [Web: Gate.io, 2024]; ERC-20 permit signatures exploited in phishing [Web: Medium Triathon, 2024]; 520M+ wallet users globally [Web: CoinLaw, 2025]
  - **Assumptions**: User awareness of approval risks est. <20% (inferred from security researcher surveys and user behavior analysis); Unlimited approval usage est. 70% of all approvals (based on on-chain transaction analysis of popular DeFi protocols); Approval management tool adoption est. 10% (inferred from Revoke.cash and similar service usage metrics); Average malicious approval detection time est. hours to days (based on incident reports and user complaints); User abandonment rate est. 30-50% when encountering approval friction (inferred from DApp analytics on limited vs unlimited approval patterns)
  - **Uncertainties**: Optimal approval UX balancing security and usability unknown; User willingness to pay gas for approval revocations TBD (free revoke vs $5-20 gas cost impact); Effectiveness of wallet-level approval warnings vs automatic rejection not determined; Long-term viability of unlimited approvals vs session-based approvals unclear; Regulatory requirements for wallet providers regarding approval risk disclosure unknown; Impact of account abstraction (ERC-4337) on approval security model TBD; Cross-chain approval monitoring scalability for 50+ chains not validated

---

## Glossary

- **Account abstraction (ERC-4337)**: Ethereum standard enabling smart contract wallets with programmable transaction validation and approval logic.
- **Approval**: A smart contract permission allowing a spender address to transfer tokens from the owner's wallet up to a specified amount.
- **DApp (Decentralized Application)**: Applications built on blockchain networks using smart contracts for backend logic.
- **DeFi (Decentralized Finance)**: Financial services built on blockchain networks using smart contracts, eliminating traditional intermediaries.
- **Drainer attack**: A sophisticated phishing attack that tricks users into signing malicious approvals or transactions that drain wallet funds.
- **EIP-2612 (Permit)**: Ethereum Improvement Proposal enabling gas-free token approvals via off-chain signatures instead of on-chain transactions.
- **ERC-20**: Ethereum token standard defining a common interface for fungible tokens.
- **EVM (Ethereum Virtual Machine)**: The runtime environment for executing smart contracts on Ethereum and compatible blockchains.
- **Gas fee**: Transaction fee paid to blockchain validators for processing operations, calculated as gas used × gas price.
- **Permit signature**: An off-chain cryptographic signature granting token approval without requiring a blockchain transaction.
- **Phishing**: A social engineering attack where attackers impersonate legitimate entities to trick users into revealing sensitive information or signing malicious transactions.
- **Smart contract**: Self-executing code deployed on a blockchain that automatically enforces agreement terms without intermediaries.
- **Unlimited approval**: A token approval granting maximum allowance (uint256(-1) or 2^256-1), enabling the spender to transfer any amount of tokens.

---

## Reference

### Web Sources & Research
- [Web: Infosecurity Magazine, 2024] - Scammers Drain $500m from Crypto Wallets in a Year; Wallet drainer attack losses in 2024 (https://www.infosecurity-magazine.com/news/scammers-drain-500m-crypto-wallets)
- [Web: Ledger, 2025] - The State of Crypto Scams in 2025; $3.1B H1 2025 crypto scam and hack losses (https://www.ledger.com/academy/topics/security/the-state-of-crypto-scams-in-2025)
- [Web: Turnkey, 2024] - Crypto phishing isn't a user problem, it's a policy problem; Phishing responsible for 31% of attacks in 2024 (https://www.turnkey.com/blog/crypto-phishing-a-policy-problem)
- [Web: Gate.io, 2024] - A Deep Dive into the ERC-20 Authorization Model; Unlimited token approval risks and permit/permit2 mechanisms (https://www.gate.com/learn/articles/a-deep-dive-into-the-erc-20-authorization-model-how-permit-and-permit2-work-their-risks-and-key-differences/8707)
- [Web: Medium Triathon, 2024] - How to Prevent ERC20 Permit Phishing and Its Principles; ERC-20 permit signature phishing exploitation (https://medium.com/@Triathon/how-to-prevent-erc20-permit-phishing-and-its-principles-7c69e13f5cc4)
- [Web: Medium Neptune Mutual, 2024] - Understanding ERC-20 Permit and Associated Risks; Gas-free approval risks and phishing vectors (https://medium.com/neptune-mutual/understanding-erc-20-permit-and-associated-risks-41c29c969862)
- [Web: CoinLaw, 2025] - Phishing and Wallet Drainer Incidents Statistics 2025; Comprehensive drainer attack statistics and trends (https://coinlaw.io/phishing-and-wallet-drainer-incidents-statistics)
- [Web: CoinLaw, 2025] - Cryptocurrency Wallet Adoption Statistics 2025; 520M+ wallet users globally (https://coinlaw.io/cryptocurrency-wallet-adoption-statistics)
- [Web: Check Point Research, 2025] - Return of the Crypto Inferno Drainer; Deep dive into sophisticated drainer attack techniques (https://research.checkpoint.com/2025/inferno-drainer-reloaded-deep-dive-into-the-return-of-the-most-sophisticated-crypto-drainer)
