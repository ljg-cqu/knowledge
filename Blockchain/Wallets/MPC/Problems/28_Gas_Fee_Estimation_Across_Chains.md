# Gas Fee Estimation Across Heterogeneous Chains

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Engineering & Product Team

## Problem Statement

**[CRITICAL] Q**: MPC wallet providers face inconsistent gas/fee estimation and transaction replacement across heterogeneous chains (EVM EIP-1559, Bitcoin RBF/CPFP, Solana priority fees), causing 10-20% of transactions to fail confirmation, get stuck in mempool, or overpay by 30-50%, resulting in user churn and support burden. Formulate a structured problem statement using the following [Input] fields.

**A**:

### Brief description of the problem to be analyzed

Multi-chain MPC wallets must accurately estimate transaction fees and implement robust replacement strategies across fundamentally different fee mechanisms: EVM EIP-1559 (base fee + priority fee), Bitcoin RBF/CPFP (fee rate bidding), and Solana (base fee + compute unit pricing). Current implementations use ad hoc, chain-specific logic tuned primarily for EVM base cases, leading to 10-20% of transactions failing to confirm within target windows or overpaying by 30-50% during volatility [Source: Supplementary Analysis, GPT5.md, lines 177-186]. This creates poor user experience, increased support load (30-40% of tickets related to "stuck transactions"), and competitive disadvantage versus wallets with sophisticated fee management.

### Background and current situation

MPC wallets supporting multi-chain operations must estimate fees for each blockchain's unique mechanism [Web: Cobo Fee Estimation Guide, 2025]:
- **EVM chains**: EIP-1559 introduced base fee (burned) + priority fee (to validator) model [Web: Blocknative EIP-1559 Guide, 2025]. Base fee adjusts dynamically per block based on network congestion.
- **Bitcoin**: Fee estimation based on satoshis/vbyte; replacement via RBF (Replace-By-Fee) or CPFP (Child-Pays-For-Parent) when transactions get stuck
- **Solana**: Base fee per signature + optional priority fee per compute unit [Web: Solana Fee Documentation, 2025; Web: QuickNode Priority Fees Guide, 2025]

Current wallet implementations use simple multipliers on oracle estimates, with limited adaptation to volatility. During congestion (e.g., NFT mints, market crashes), transactions either fail to confirm within user expectations (2-3 blocks for EVM, 3-6 blocks for Bitcoin, 2-5 slots for Solana) or overpay significantly [Source: Supplementary Analysis, GPT5.md, line 180]. Bitcoin and Solana support are recent additions with minimal production tuning. No automated replacement/bump strategies exist for stuck transactions, requiring manual support intervention [Source: Supplementary Analysis, GPT5.md, lines 184-185].

### Goals and success criteria

- **Confirmation reliability**: Achieve ≥99% confirmation within target windows: EVM ≤2 blocks p95, Bitcoin ≤3 blocks p95, Solana ≤2 slots p95
- **Fee efficiency**: Reduce average overpayment by 20-40% vs current estimates (from 30-50% overpay to 10-20% overpay)
- **Stuck transaction rate**: Cut "stuck transaction" support tickets by ≥60% (from ~35% of ticket volume to ≤15%)
- **Replacement success**: Automated fee bumps/replacements succeed ≥95% when triggered for stuck transactions
- **Latency overhead**: Keep fee estimation and policy logic overhead ≤100ms p95 (to avoid impacting signing UX)
- **Timeline**: Implement robust multi-chain fee estimation within 3-5 months (Q1-Q2 2025)

### Key constraints and resources

- **Mempool visibility**: Limited direct mempool access; rely on third-party RPC providers and fee oracle APIs (e.g., Blocknative, Etherscan, Mempool.space)
- **Third-party rate limits**: Gas oracle APIs have rate limits (e.g., 100-1000 req/min) and costs ($50-500/mo depending on volume)
- **Chain-specific differences**: Replacement policies differ materially (EVM allows nonce reuse, Bitcoin requires higher fee, Solana has no direct replacement)
- **Mobile responsiveness**: Mobile app must remain responsive; cannot add >1 additional RTT during signing flow
- **Budget**: Limited to $30K implementation cost + $5K/mo for third-party oracle services
- **Engineering capacity**: 2 FTE blockchain engineers + 0.5 PM for 3-5 months
- **Backward compatibility**: Cannot break existing transaction submission flows; must maintain support for manual fee override

### Stakeholders and roles

- **End users** (50K-200K active): Need predictable confirmations and fair fees; experience frustration with stuck transactions; expect transparency on fee estimates
- **Support team** (10-15 agents): Handle 300-500 "stuck transaction" tickets/month (35% of total volume); need ≥60% reduction; require self-service tools for users
- **Engineering team** (5-8 blockchain engineers): Manage chain-specific logic across 10+ chains; need maintainable abstraction layer; require comprehensive testing for edge cases
- **Finance/Operations** (2-3 analysts): Monitor fee overpayment cost; current overspend estimated $20K-50K/mo across user base; need 30-50% reduction
- **Product management** (1-2 PMs): Balance UX (instant confirmation expectations) vs cost efficiency; need data-driven policy recommendations
- **Partnership/Exchange integrations** (3-5 partners): Rely on predictable deposit confirmations; require SLAs for deposit availability

### Time scale and impact scope

- **Timeline**: 3-5 months (Q1-Q2 2025) for design, implementation, testing, and gradual rollout
- **Affected systems**: All outbound transaction flows across EVM (Ethereum, Polygon, Arbitrum, Optimism, Base), Bitcoin, and Solana networks
- **User impact**: 100% of active users performing transactions (~50K-200K accounts); disproportionate impact on power traders during volatility
- **Transaction volume**: Affects 500K-2M transactions/month across all chains
- **Support impact**: Reduce 300-500 stuck-tx tickets/month by 60% = 180-300 ticket reduction
- **Cost impact**: Current overpayment $20K-50K/mo; target 30-50% reduction = $6K-25K/mo savings
- **Peak behavior**: Most critical during market volatility (10x normal volume) and network congestion events

### Historical attempts and existing solutions (if any)

EVM EIP-1559 support was implemented with simple base fee + priority fee multipliers (1.2x base, 2 gwei priority) [Source: Supplementary Analysis, GPT5.md, line 185]. This approach worked adequately during normal conditions but underperformed during congestion:
- During NFT mint events, 15-25% of transactions failed to confirm within 5 blocks
- During market crashes, conservative estimates led to 40-60% overpayment vs optimal fees

Bitcoin RBF and Solana priority fee logic were added as POCs with minimal production tuning [Source: Supplementary Analysis, GPT5.md, line 185]. No automated replacement strategies were implemented; support manually advised users to wait or re-submit. Key lessons learned:
- Static multipliers fail during volatility and changing network conditions
- Lack of mempool analytics causes blind estimation
- Users cannot distinguish between "transaction pending" vs "transaction stuck" without better tooling

### Known facts, assumptions, and uncertainties

**Facts**:
- EVM EIP-1559 uses dynamic base fee + priority fee mechanism [Web: Blocknative EIP-1559 Guide, 2025]
- Solana uses base fee per signature + priority fee per compute unit [Web: Solana Fee Documentation, 2025; Web: QuickNode Priority Fees Guide, 2025]
- Bitcoin fee estimation traditionally based on satoshis/vbyte with RBF for replacement
- Current implementation overpays by 30-50% during congestion [Source: Supplementary Analysis, GPT5.md, line 180]
- Stuck transaction tickets represent ~35% of support volume (300-500 tickets/month) [Source: Supplementary Analysis, GPT5.md, line 181]
- Multiple fee oracle providers exist (Blocknative, Etherscan API, Mempool.space, Solana RPC `getRecentPrioritizationFees`)

**Assumptions**:
- Mempool analytics and adaptive fee estimation can reduce failures materially [Source: Supplementary Analysis, GPT5.md, line 186]
- Historical fee patterns can inform predictive models for congestion periods
- Users will accept slight delays (100-200ms) for improved fee accuracy
- Third-party oracle reliability is ≥99.5% (requires monitoring and fallback providers)

**Uncertainties**:
- Exact optimal fee thresholds per chain under different congestion scenarios
- Impact of improved estimation on overall transaction confirmation latency (may increase by 50-100ms)
- Reliability of third-party fee oracles during extreme events (e.g., oracle API downtime during peak congestion)
- User behavior response to fee transparency (will users accept higher fees during congestion, or abandon transactions?)
- MEV impact on transaction inclusion beyond fee considerations (sandwich attacks, frontrunning)

## Reference

### Web Sources
- [Web: Cobo Fee Estimation Guide, 2025] - How to Estimate and Optimize Transaction Fees for MPC Wallets. Cobo Developers. https://www.cobo.com/developers/v1/guides/howtos/estimate-transaction-fees
- [Web: Blocknative EIP-1559 Guide, 2025] - EIP-1559 Gas Fees: Base Fee, Priority Fee, & Max Fee. Blocknative. https://www.blocknative.com/blog/eip-1559-fees
- [Web: Solana Fee Documentation, 2025] - Transaction Fees. Solana Documentation. https://solana.com/docs/core/fees
- [Web: QuickNode Priority Fees Guide, 2025] - Understand Solana Priority Fees: Land Transactions Faster. QuickNode. https://www.quicknode.com/guides/solana-development/transactions/how-to-use-priority-fees

### Supplementary Sources
- [Source: Supplementary Analysis, GPT5.md, 2025-11-28] - Blockchain MPC Wallet Problem Extraction. Lines 177-186. Internal analysis document.
