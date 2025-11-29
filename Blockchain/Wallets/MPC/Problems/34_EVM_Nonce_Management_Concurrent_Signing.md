# EVM Nonce Management for Concurrent MPC Signing

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Blockchain Engineering Team

## Problem Statement

**[Important] Q**: MPC wallets allowing parallel signing sessions from multiple devices/services face EVM nonce collisions and gaps, causing 5-10% of concurrent transactions to become stuck, replaced unintentionally, or fail with "nonce too low" errors, particularly during peak trading periods, degrading UX and increasing support burden. Formulate a structured problem statement using the following [Input] fields.

**A**:

### Brief description of the problem to be analyzed

Ethereum and EVM-compatible chains require sequential transaction nonces to prevent replay attacks and ensure ordering [Web: Circle Wallet Nonce Management, 2025]. MPC wallets enabling concurrent transaction initiation (e.g., simultaneous swap on mobile + transfer on web) create nonce coordination challenges when multiple participants independently allocate nonces [Source: Supplementary Analysis, GPT5.md, lines 397-406]. Current implementations use per-client optimistic nonce tracking with eventual consistency, leading to nonce collisions (two transactions assigned same nonce = unintended replacement), nonce gaps (skipped nonce blocks subsequent transactions), and retry/RBF logic targeting wrong nonce during fee bumping [Source: Supplementary Analysis, GPT5.md, line 405]. This causes 5-10% of concurrent transactions during peak periods to get stuck, replaced, or fail, increasing user confusion and support tickets (estimated 10-15% of EVM transaction issues). Organizations need centralized nonce allocation or per-account locking achieving <0.1% nonce-related failures with <50ms p95 allocation latency.

### Background and current situation

**EVM nonce mechanism** [Web: Circle Wallet Nonce Management, 2025]:
- Each account maintains a sequential nonce counter starting at 0
- Transactions must be mined in nonce order; gaps block subsequent transactions
- Nonce reuse with higher gas price replaces pending transaction (Replace-By-Fee/RBF)
- "Nonce too low" error indicates transaction already mined or replaced

**MPC concurrent signing scenarios**:
- User initiates swap on mobile app while web session submits transfer (2 devices, 2 signing sessions)
- Backend batch processing submits multiple withdrawals concurrently (e.g., exchange cold wallet sweeps)
- DeFi arbitrage bots using MPC wallets executing multiple trades simultaneously

**Current nonce management approaches** [Source: Supplementary Analysis, GPT5.md, lines 397-406]:
- **Optimistic per-client allocation**: Each client queries current nonce from RPC (`eth_getTransactionCount`), increments locally, submits transaction. Prone to race conditions when 2+ clients query simultaneously before any transaction mines.
- **Last-known-nonce cache**: Maintain in-memory cache of last assigned nonce; increment on each submission. Fails during crashes/restarts (cache lost) or cross-client concurrency (cache per client).
- **Eventual consistency**: Retry failed transactions with nonce adjustment. Creates cascading failures during peak load.

**Problems observed**:
- **Nonce collisions**: Two concurrent transactions assigned same nonce; second transaction replaces first unintentionally, confusing users ("my swap got replaced by transfer?")
- **Nonce gaps**: Optimistic allocation assigns nonce N+2 before N+1 mines; subsequent transactions stuck until N+1 confirmed
- **RBF targeting wrong nonce**: Fee bump logic may target nonce N when user intended to bump nonce N+1, causing further confusion
- **Peak load amplification**: Concurrent activity during market volatility (10x normal volume) increases collision rate from <1% to 5-10%

### Goals and success criteria

- **Nonce failure rate**: Limit nonce-related failures to <0.1% of EVM transactions (down from current 5-10% during peak concurrency)
- **Allocation latency**: Ensure deterministic single-writer nonce allocation with p95 latency <50ms (cannot add significant signing delay)
- **Concurrency support**: Support ≥10 concurrent signing sessions per account without collisions (handle peak power-user activity)
- **RBF correctness**: Fee replacement logic targets correct nonce with 100% accuracy (no unintended replacements)
- **Support ticket reduction**: Reduce "nonce mismatch" / "stuck transaction" tickets by ≥70% within 2 months (from current ~80-120/month to <25-35/month)
- **Timeline**: Implement production-grade nonce allocator within 2-3 months (Q1 2025)

### Key constraints and resources

- **RPC visibility limits**: Mempool visibility varies by RPC provider; pending nonce tracking requires reliable RPC or direct node access
- **Multi-chain complexity**: Must support 10+ EVM chains (Ethereum, Polygon, Arbitrum, Optimism, Base, BSC, Avalanche) with varying RPC quality
- **Latency budget**: Cannot add >1 extra round-trip during signing flow; target <50ms p95 allocation overhead
- **Backend refactor limits**: Current MPC signing coordinator may require architectural changes for centralized allocator; limited to $40K refactor budget
- **State management**: Centralized allocator must be stateful, highly available (99.95% uptime), and fault-tolerant (persist state across restarts)
- **Engineering capacity**: 1.5 FTE blockchain engineers for 2-3 months
- **Budget**: $40K implementation + $2K/mo operational (infrastructure for allocator service)

### Stakeholders and roles

- **End users** (50K-200K active, power traders most affected): Experience frustration with stuck/replaced transactions; need reliable transaction sequencing; expect <10s transaction submission
- **Power traders** (5-10K high-frequency users): Execute 10-50 transactions/hour during volatility; most impacted by nonce collisions; require support for ≥10 concurrent sessions
- **Engineering/blockchain** (5-8 engineers): Own nonce allocator design and implementation; manage state persistence and HA architecture; require monitoring/alerting for allocation failures
- **Support team** (10-15 agents): Handle 80-120 "stuck transaction" / "nonce mismatch" tickets/month related to EVM nonce issues; need ≥70% reduction
- **Partners/exchanges** (20-30 integrations): Rely on predictable deposit confirmations; nonce issues cause deposit delays and reconciliation failures; need >99.9% reliable sequencing

### Time scale and impact scope

- **Timeline**: 2-3 months (Q1 2025) for centralized nonce allocator design, state management, multi-chain support, testing, phased rollout
- **Affected systems**: All EVM transaction submission flows across 10+ chains (Ethereum, Polygon, Arbitrum, Optimism, Base, BSC, Avalanche, Fantom, Cronos, etc.)
- **User impact**: 100% of EVM users (~80-90% of total user base = 40K-180K accounts); highest impact on power traders during peak periods
- **Transaction volume**: Affects 1M-4M EVM transactions/month; peak concurrency during market volatility (10x normal volume = 100K-400K txs/day)
- **Support impact**: Reduce nonce-related tickets from 80-120/month to <25-35/month (≥70% reduction)

### Historical attempts and existing solutions (if any)

Simple optimistic nonce incrementer was implemented with last-known-nonce cache [Source: Supplementary Analysis, GPT5.md, line 405]. Approach:
1. Query `eth_getTransactionCount` from RPC
2. Maintain in-memory cache of last assigned nonce
3. Increment cache on each transaction submission
4. Apply ad hoc exponential backoff on "nonce too low" errors

Results during testing:
- Worked adequately during single-device usage (95%+ success)
- Failed during concurrent sessions: 5-10% collision rate during peak load (2+ concurrent initiations within 1s window)
- Cache lost on service restarts, requiring re-query and potential gaps
- Edge cases during reorgs: RPC returned stale nonce after chain reorganization, causing nonce gaps

Key lessons learned:
- Optimistic per-client allocation insufficient for concurrency (race conditions inevitable)
- Cache-based approaches fragile (state loss on restart, stale during reorgs)
- RPC variability complicates nonce tracking (different providers have different pending-nonce semantics)

**Industry solutions**:
- Centralized nonce allocator with single-writer semantics (e.g., queuing per account) [Web: thirdweb Nonce Management, 2025]
- Per-account locks ensuring only one transaction submitted at a time (sacrifices concurrency)
- 2D nonce schemes (emerging; not widely supported on EVM) [Web: Openfort 2D Nonce, 2025]

### Known facts, assumptions, and uncertainties

**Facts**:
- EVM requires sequential nonces; gaps block subsequent transactions [Web: Circle Wallet Nonce Management, 2025]
- Nonce reuse with higher gas price replaces pending transaction (RBF behavior)
- Current optimistic allocator experiences 5-10% collision rate during peak concurrency [Source: Supplementary Analysis, GPT5.md, line 401]
- Support receives 80-120 nonce-related tickets/month (10-15% of EVM transaction support volume)
- Parallel initiations observed: power traders submit 2-5 concurrent transactions during volatility

**Assumptions**:
- Centralized nonce allocator or per-account locking can reduce collisions to <0.1% [Source: Supplementary Analysis, GPT5.md, line 406]
- Allocation latency <50ms acceptable (does not materially degrade signing UX)
- State persistence (PostgreSQL, Redis) can provide 99.95% availability for allocator service
- RPC quality sufficient for pending-nonce tracking (may require node diversity for accuracy)

**Uncertainties**:
- RPC variance impact on allocator accuracy under reorgs (does pending-nonce tracking remain consistent across providers?)
- Optimal allocation strategy: queue-based (serialize per account)? vs distributed lock? vs hybrid?
- Handling of stuck transactions: when to auto-bump nonce? Risk of prematurely advancing nonce before confirmation?
- Multi-region coordination: how to handle nonce allocation when users span multiple geographic regions with >100ms latency?
- 2D nonce adoption timeline (will EVM chains adopt parallelization-friendly nonce schemes in 1-2 years?)

## Reference

### Web Sources
- [Web: Circle Wallet Nonce Management, 2025] - Wallet Nonce Management. Circle Developer Docs. https://developers.circle.com/cpn/concepts/wallet-nonce-management
- [Web: thirdweb Nonce Management, 2025] - thirdweb's approach to Ethereum nonce Management. thirdweb Blog. https://blog.thirdweb.com/sending-more-than-one-transaction-at-a-time
- [Web: Openfort 2D Nonce, 2025] - 2D Nonce: Transaction Parallelization. Openfort Blog. https://www.openfort.io/blog/parallalization-of-transactions-2d-nonce

### Supplementary Sources
- [Source: Supplementary Analysis, GPT5.md, 2025-11-28] - Blockchain MPC Wallet Problem Extraction. Lines 397-406. Internal analysis document.
