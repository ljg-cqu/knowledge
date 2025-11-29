# Account Abstraction (EIP-4337) Integration with MPC Wallets

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Blockchain Engineering & Product Team

## Problem Statement

**[Important] Q**: MPC wallet integration with EIP-4337 Account Abstraction is immature, causing 5-15% UserOperation submission failures, unpredictable bundler/paymaster dependencies, and complex signature compatibility issues, blocking adoption of gasless transactions and advanced UX features critical for mainstream user onboarding. Formulate a structured problem statement using the following [Input] fields.

**A**:

### Brief description of the problem to be analyzed

EIP-4337 Account Abstraction enables smart contract wallets to bypass externally-owned account (EOA) limitations, offering gasless transactions, social recovery, and flexible authorization logic [Web: ERC-4337 Documentation, 2025]. However, integrating Account Abstraction with MPC threshold signing introduces technical challenges: MPC signature formats must match AA validation logic, bundler availability varies by network, paymaster gas sponsorship policies are inconsistent, and fallback to EOA complicates address continuity [Source: Supplementary Analysis, GPT5.md, lines 243-252]. Current early-stage integrations experience 5-15% UserOperation submission failures due to bundler outages, signature packing issues, and sponsor policy rejections. Organizations need production-grade AA+MPC implementation achieving ≥99% submission success, <300ms added latency, and seamless fallback to EOA for existing addresses to unlock gasless onboarding and institutional adoption.

### Background and current situation

**EIP-4337 Account Abstraction overview** [Web: ERC-4337 Documentation, 2025; Web: Alchemy ERC-4337 Guide, 2025]:
- **UserOperation objects**: Pseudo-transactions submitted to AA mempool (separate from standard mempool)
- **Bundlers**: Off-chain services aggregating UserOperations into single transactions submitted to EntryPoint contract
- **EntryPoint contract**: On-chain coordinator validating and executing batched UserOperations
- **Paymasters**: Contracts sponsoring gas fees, enabling gasless transactions or ERC-20 fee payment [Web: Alchemy Paymaster Guide, 2025]

**MPC integration challenges**:
- **Signature compatibility**: MPC ECDSA/EdDSA signatures must be packed correctly for AA validation; signature format varies by smart account implementation (SimpleAccount, Kernel, Safe, Biconomy) [Source: Supplementary Analysis, GPT5.md, line 246]
- **Bundler dependency**: Reliance on third-party bundlers (e.g., Stackup, Alchemy, Pimlico) introduces availability risk; bundler outages cause 100% UserOperation failures
- **Paymaster policies**: Gas sponsorship policies inconsistent across networks; paymasters may reject UserOperations based on risk scoring, rate limits, or funding depletion [Source: Supplementary Analysis, GPT5.md, line 250]
- **Multi-chain fragmentation**: AA support varies (Ethereum mainnet, Polygon, Arbitrum, Optimism have bundlers; other chains limited)
- **Fallback complexity**: Maintaining backward compatibility with EOA addresses while migrating to AA requires complex dual-path logic

**Current state**: Early POC implementations using third-party bundler/paymaster services demonstrated:
- 5-15% submission failures during bundler maintenance or sponsor outages
- Signature packing issues causing validation failures (MPC signature format mismatch with account validation logic)
- No production rollout due to reliability concerns

### Goals and success criteria

- **Submission success**: Achieve ≥99% UserOperation submission success across supported networks (Ethereum, Polygon, Arbitrum, Optimism, Base)
- **Latency overhead**: Keep AA-related added latency ≤300ms p95 vs direct EOA submission
- **Fallback reliability**: Maintain fallback to EOA with 0 address changes for existing users (dual-path support)
- **Gas sponsorship coverage**: Enable gasless transactions for ≥80% of onboarding flows and <$50 transactions
- **Bundler SLA**: Bundler availability ≥99.5% with automated failover across ≥2 bundler providers per chain
- **Signature compatibility**: Support top 3 smart account implementations (SimpleAccount, Safe, Kernel) with 99.99% validation success in CI
- **Timeline**: Production-ready AA+MPC integration within 4-6 months (Q1-Q2 2025)

### Key constraints and resources

- **Bundler availability**: Third-party bundlers have varying SLAs (Stackup, Alchemy, Pimlico claim 99-99.9% uptime but outages observed)
- **Paymaster funding risk**: Sponsorship budgets deplete; paymasters may reject UserOps when funding low or risk score high
- **Multi-chain AA maturity**: AA infrastructure mature on Ethereum L2s (Arbitrum, Optimism, Base) but limited on other chains (Solana, Bitcoin N/A)
- **MPC signature format**: ECDSA/EdDSA signatures from MPC protocol must match exact packing expected by smart account validation logic [Source: Supplementary Analysis, GPT5.md, line 246]
- **Backward compatibility**: Existing users with EOA addresses cannot migrate to AA without address change (breaks deposit addresses for exchanges/partners)
- **Engineering capacity**: 2 FTE blockchain engineers + 0.5 smart contract engineer for 4-6 months
- **Budget**: $80K implementation + $10K-20K/mo operational (bundler/paymaster services, gas sponsorship)

### Stakeholders and roles

- **End users** (50K-200K active): Expect fee-less or sponsored flows for small transactions; require address continuity (no migration friction); expect <5s transaction confirmation
- **New users (onboarding)**: Gasless onboarding critical for mainstream adoption; target 0-friction first transaction within 30s
- **Engineering/blockchain** (5-8 engineers): Integrate AA with MPC signing; manage bundler/paymaster dependencies; handle signature packing complexity; require monitoring/alerting
- **Bundler/paymaster partners** (3-5 providers): Provide infrastructure; SLAs vary; need fallback across multiple providers to ensure reliability
- **Compliance/finance** (2-3 officers): Monitor gas sponsorship spend; require fraud detection on sponsored transactions; cap sponsorship budget at $10K-20K/mo
- **Product/UX** (1-2 PMs): Enable gasless onboarding and improved UX; balance sponsorship costs vs user acquisition; require seamless fallback for existing users

### Time scale and impact scope

- **Timeline**: 4-6 months (Q1-Q2 2025) for AA integration, bundler/paymaster orchestration, signature compatibility testing, fallback logic, phased rollout
- **Affected systems**: EVM transaction submission flows on supported chains (Ethereum, Polygon, Arbitrum, Optimism, Base); onboarding flows for new users
- **User impact**: New users (gasless onboarding) + existing users opting into AA features; estimated 30-50% of new users + 10-20% of existing users over 6 months
- **Transaction volume**: Affects 100K-500K transactions/month initially (onboarding + small-value txs); potential to scale to 50-80% of all transactions as AA matures
- **Cost impact**: Gas sponsorship budget $10K-20K/mo for subsidized onboarding; ROI measured via increased user activation and retention

### Historical attempts and existing solutions (if any)

Early EIP-4337 POC was implemented using third-party bundler (Stackup) and paymaster (Pimlico) [Source: Supplementary Analysis, GPT5.md, line 251]. POC demonstrated gasless onboarding for test users but exposed critical issues:
- **Signature packing failures**: MPC ECDSA signatures required specific encoding (r, s, v components in correct order); initial implementation used wrong packing causing 10-15% validation failures
- **Bundler outages**: During Stackup maintenance window, 100% of UserOperations failed; no automated failover to alternate bundler
- **Paymaster sponsor rejections**: Rate limiting and funding depletion caused intermittent rejections; no visibility into sponsor balance or rejection reasons
- **No production rollout**: Reliability concerns and signature compatibility issues prevented launch

Key lessons learned:
- AA infrastructure still evolving; bundler/paymaster reliability critical
- Dual-path EOA+AA required for backward compatibility (cannot force existing users to migrate)
- Signature format testing essential; MPC signature packing must match smart account validation exactly
- Multi-bundler failover necessary to meet production SLAs

### Known facts, assumptions, and uncertainties

**Facts**:
- EIP-4337 Account Abstraction uses UserOperations, bundlers, and paymasters [Web: ERC-4337 Documentation, 2025; Web: Alchemy ERC-4337 Guide, 2025]
- Paymasters enable gas sponsorship and ERC-20 fee payment [Web: Alchemy Paymaster Guide, 2025]
- MPC signature compatibility with AA validation logic is non-trivial [Source: Supplementary Analysis, GPT5.md, line 246]
- Current POC experienced 5-15% submission failures and signature packing issues [Source: Supplementary Analysis, GPT5.md, lines 250-251]
- AA infrastructure mature on Ethereum L2s (Arbitrum, Optimism, Base) but limited elsewhere

**Assumptions**:
- Dual-path EOA+AA approach reduces migration risk for existing users [Source: Supplementary Analysis, GPT5.md, line 252]
- Multi-bundler failover can achieve ≥99.5% bundler availability
- Gas sponsorship ROI positive (increased user activation outweighs $10K-20K/mo cost)
- Signature compatibility achievable across top smart account implementations (SimpleAccount, Safe, Kernel) within 4-6 months

**Uncertainties**:
- Long-term stability of bundler/paymaster infrastructure (will consolidation occur? Pricing models?)
- User adoption of AA features (will users value gasless transactions enough to offset complexity?)
- Standard convergence (will ERC-7702 replace EIP-4337? Future migration risk?)
- Cross-chain AA expansion timeline (when will non-EVM chains support similar abstractions?)
- Optimal gasless sponsorship policy (sponsor all txs <$50? Only onboarding? Risk of abuse?)

## Reference

### Web Sources
- [Web: ERC-4337 Documentation, 2025] - ERC-4337 Documentation. https://docs.erc4337.io/index.html
- [Web: Alchemy ERC-4337 Guide, 2025] - How do ERC-4337 smart contract wallets work? Alchemy. https://www.alchemy.com/overviews/how-do-smart-contract-wallets-work
- [Web: Alchemy Paymaster Guide, 2025] - What are Paymasters? (ERC-4337). Alchemy. https://www.alchemy.com/overviews/what-is-a-paymaster
- [Web: Coinbase State of Wallets, 2025] - State of Wallets - Part 2: Smart Accounts (Account Abstraction). Coinbase Blog. https://www.coinbase.com/blog/state-of-wallets-2

### Supplementary Sources
- [Source: Supplementary Analysis, GPT5.md, 2025-11-28] - Blockchain MPC Wallet Problem Extraction. Lines 243-252. Internal analysis document.
