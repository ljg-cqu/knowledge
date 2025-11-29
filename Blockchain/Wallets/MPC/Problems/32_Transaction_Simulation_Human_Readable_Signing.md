# Transaction Simulation and Human-Readable Signing

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Security & Product Engineering Team

## Problem Statement

**[CRITICAL] Q**: MPC wallet users blindly sign opaque transaction payloads due to inadequate decoding and simulation capabilities, enabling 20-40% of phishing/scam losses via malicious permit approvals, proxy calls, and misleading transaction data, costing estimated $500K-2M annually in user losses and reputational damage. Formulate a structured problem statement using the following [Input] fields.

**A**:

### Brief description of the problem to be analyzed

Blockchain transactions often contain complex, opaque bytecode that users cannot interpret without sophisticated decoding and simulation [Source: Supplementary Analysis, GPT5.md, lines 221-230]. Attackers exploit this "blind signing" vulnerability to trick users into approving malicious transactions: unlimited ERC-20 Permit approvals draining wallets, proxy contract calls redirecting funds, or complex DeFi interactions with hidden outcomes [Web: Hypernative MPC Blind Signing Report, 2025]. Current MPC wallet implementations provide basic ABI decoding for common ERC-20 transfers but lack comprehensive coverage for Permit/Permit2, multisend batches, and non-EVM payloads [Source: Supplementary Analysis, GPT5.md, line 224]. Without transaction simulation showing predicted balance changes and risk warnings, users approve malicious transactions causing 20-40% of total fraud losses (estimated $500K-2M annually). Organizations need high-coverage decode/simulation (≥95% of transactions) with <200ms latency overhead to reduce fraud incidents by ≥50% while maintaining signing UX.

### Background and current situation

Blockchain transactions consist of:
- **EVM**: Contract calls encoded as function selectors + ABI-encoded parameters; may include delegate calls, proxy upgrades, or complex DeFi interactions
- **ERC-20 Permit/Permit2**: Off-chain signature schemes allowing token approvals without separate transaction; frequently exploited in phishing [Source: Supplementary Analysis, GPT5.md, line 224]
- **Non-EVM chains**: Different encoding schemes (Solana instructions, Cosmos Amino/Proto messages) with chain-specific semantics

Current wallet implementations [Source: Supplementary Analysis, GPT5.md, lines 221-230]:
- Basic ABI decoding for common functions (ERC-20 `transfer`, `approve`, NFT `safeTransferFrom`)
- Limited support for complex calls: multisend batches, proxy contracts, Permit/Permit2 signatures
- No on-device simulation showing predicted outcomes (balance changes, approval grants, contract interactions)
- No risk scoring or red-flag detection (unlimited approvals, known malicious contracts, unusual patterns)

Attack patterns exploiting blind signing:
- **Unlimited Permit approvals**: User thinks approving $100 USDC but signs Permit for `uint256.max` allowing full wallet drain
- **Proxy contract attacks**: User approves interaction with legitimate-looking address that delegates to malicious implementation
- **Hidden multicalls**: Batch transaction containing benign operation + malicious fund transfer in same batch

Results in:
- 20-40% of fraud losses attributable to blind signing [Assumption: based on wallet fraud post-mortems]
- Post-sign regret: users realize transaction intent only after on-chain execution
- Support tickets: 100-200/month users reporting "didn't expect this transaction to do that"

### Goals and success criteria

- **Decode coverage**: Provide accurate decode/simulation for ≥95% of transactions by monthly active user volume across supported chains
- **Fraud reduction**: Reduce post-sign regret/fraud tickets by ≥50% (from current ~150-250/month to <75-125/month)
- **Latency overhead**: Keep simulation + decode added latency ≤200ms p95 (to avoid impacting signing UX)
- **Risk detection**: Flag ≥90% of known malicious patterns (unlimited approvals, known scam contracts, unusual delegate calls)
- **False positive rate**: Keep false-positive warnings <5% (avoid warning fatigue)
- **User loss reduction**: Reduce blind-signing-attributable user losses by ≥60% (from estimated $500K-2M/year to <$200K-800K/year)
- **Timeline**: Implement comprehensive simulation within 3-5 months (Q1-Q2 2025)

### Key constraints and resources

- **ABI/IDL fragmentation**: EVM contracts often lack verified source/ABI; non-EVM chains use different interface definitions (IDLs)
- **Third-party simulation APIs**: Services like Tenderly, Blocknative, or Alchemy Simulation API have cost/latency constraints ($500-5K/mo, 100-500ms latency)
- **On-device compute limits**: Complex simulation requires EVM execution; mobile devices constrained by CPU/battery
- **Fast-evolving protocols**: New DeFi protocols and token standards emerge constantly; decode logic requires continuous updates
- **Chain heterogeneity**: Different simulation approaches for EVM vs Solana vs Bitcoin; limited tooling for non-EVM chains
- **Engineering capacity**: 2 FTE engineers (security + blockchain) for 3-5 months
- **Budget**: $60K implementation + $5K-10K/mo operational (simulation APIs, ABI indexing)

### Stakeholders and roles

- **End users** (50K-200K active): Need clear understanding of transaction intent before signing; frustrated by post-sign surprises; expect <5s total signing time
- **Security/risk team** (3-5 engineers): Aim to reduce fraud losses by ≥50%; need high-coverage risk detection; require audit trail of warnings shown
- **DApp partners** (50-100 integrations): Benefit from fewer false alarms and user trust; need reliable decode for complex DeFi interactions
- **Product/UX** (1-2 PMs): Balance security warnings vs UX friction; need clear risk scoring thresholds; require <200ms latency overhead
- **Support team** (10-15 agents): Handle 150-250 "unexpected transaction" tickets/month; need ≥50% reduction; require user education materials on risks
- **Compliance/legal** (2-3 officers): Monitor liability for user losses; prefer proactive warnings reducing legal/reputational risk

### Time scale and impact scope

- **Timeline**: 3-5 months (Q1-Q2 2025) for simulation integration (EVM priority, then Solana), ABI indexing, risk scoring, UX design, testing, rollout
- **Affected systems**: All dApp interactions, outbound transaction signing flows across web/mobile clients
- **User impact**: 100% of active users signing transactions (~50K-200K accounts); disproportionate impact on DeFi power users
- **Transaction volume**: Affects 500K-2M transactions/month across all supported chains
- **Fraud impact**: Current blind-signing losses estimated $500K-2M/year; target ≥60% reduction = $300K-1.2M/year savings
- **Support impact**: Reduce "unexpected transaction" tickets from 150-250/month to <75-125/month (≥50% reduction)

### Historical attempts and existing solutions (if any)

Limited heuristics-based decoding was implemented for common ERC-20 functions (`transfer`, `approve`, `transferFrom`) [Source: Supplementary Analysis, GPT5.md, line 229]. This covered ~40-60% of transaction volume but failed on:
- Permit/Permit2 signatures: displayed as opaque hex data, frequent user confusion
- Proxy contracts: showed proxy address, not implementation address or true destination
- Multisend/batches: displayed only first operation in batch, hiding subsequent malicious calls

No formal transaction simulation was implemented; no risk scoring or pattern detection. Multiple incidents:
- Users approved unlimited Permit allowances thinking they approved fixed amounts
- Proxy contract scams where users interacted with contracts delegating to malicious logic
- Multisend batches hiding fund transfers after benign operation

Key lessons learned:
- Basic ABI decoding insufficient for security (covers common cases but misses attack vectors)
- Opaque payloads correlate strongly with user errors and fraud
- Users need predicted balance changes, not just function names/parameters
- High-coverage simulation requires third-party APIs or embedded EVM execution (resource-intensive)

### Known facts, assumptions, and uncertainties

**Facts**:
- Blind signing is a known vulnerability in crypto wallets [Web: Hypernative MPC Blind Signing Report, 2025]
- Permit/Permit2 approvals frequently exploited in phishing campaigns [Source: Supplementary Analysis, GPT5.md, line 224]
- Current decode coverage ~40-60% of transaction volume (ERC-20 only) [Source: Supplementary Analysis, GPT5.md, line 229]
- Post-sign regret tickets: 150-250/month reporting unexpected transaction outcomes
- Third-party simulation APIs available (Tenderly, Blocknative, Alchemy) with 100-500ms latency and $500-5K/mo cost

**Assumptions**:
- High-coverage simulation (≥95%) reduces blind-signing incidents materially by ≥50% [Source: Supplementary Analysis, GPT5.md, line 230]
- Users will accept 100-200ms additional latency for improved transaction clarity
- Third-party simulation API reliability ≥99.5% (requires monitoring and fallback strategies)
- ABI/IDL coverage for top 100 dApps by volume achievable within 3-5 months

**Uncertainties**:
- Coverage achievable for long-tail contracts without verified ABI (may require heuristic decoding or user-submitted ABIs)
- Non-EVM simulation feasibility (Solana, Cosmos) with similar latency/accuracy as EVM
- Optimal UX for risk warnings (red/yellow/green scoring? Detailed explanations? Block vs warn?)
- False-positive rate for complex DeFi interactions (will legitimate complex transactions trigger false alarms?)
- User behavior response to warnings (will users ignore warnings due to fatigue? Or abandon legitimate transactions?)

## Reference

### Web Sources
- [Web: Hypernative MPC Blind Signing Report, 2025] - MPC Wallet Security in 2025: Solving the Blind Signing Gap. Hypernative. https://www.hypernative.io/blog/mpc-wallet-security-in-2025-solving-the-blind-signing-gap

### Supplementary Sources
- [Source: Supplementary Analysis, GPT5.md, 2025-11-28] - Blockchain MPC Wallet Problem Extraction. Lines 221-230. Internal analysis document.
