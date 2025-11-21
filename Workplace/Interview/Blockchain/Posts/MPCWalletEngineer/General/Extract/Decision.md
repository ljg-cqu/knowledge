# MPC Wallet Engineer - Decision Questions

1. Q: Your MPC wallet needs to support Ethereum, Bitcoin, and Solana. Product wants unified UX, security requires HSM integration, and mobile team needs <800ms signing latency. You can choose GG20 (5 rounds, mature), CGGMP21 (4 rounds, newer), or FROST (2 rounds, Schnorr-only). How would you design the protocol architecture and what trade-offs would you accept?
   A:
   - **Protocol Selection Strategy**: Use CGGMP21 for Ethereum/Bitcoin (ECDSA), FROST for Solana (EdDSA)
   - **Rationale**: CGGMP21 fixes GG20 security vulnerabilities while reducing rounds, FROST optimal for EdDSA. Single protocol won't work across all chains due to signature scheme differences
   - **Latency Budget**: CGGMP21 4 rounds × 150ms RTT = 600ms + 150ms compute = 750ms total (meets target)
   - **HSM Integration**: Implement chain-agnostic adapter layer that abstracts HSM operations from protocol specifics
   - **Trade-offs Accepted**: Increased complexity of maintaining two protocol implementations vs marginal performance gains from unified approach

1. Q: Mobile P95 signing latency is 2.5s (target: <1s). Profiling shows: 40% network RTT, 35% elliptic curve ops, 25% serialization. Backend team wants to focus on horizontal scaling, security team opposes any protocol changes, mobile team wants offline signing. What optimizations would you prioritize and why?
   A:
   - **P0: Offline Pre-signing**: Implement CGGMP21 pre-signing phase, reduces online from 4 to 1 round. Impact: 40% network → 10% (saves ~900ms)
   - **P1: WebAssembly for Crypto Ops**: Port curve operations to WASM for cross-platform optimization. Impact: 35% compute → 20% (saves ~375ms)
   - **P2: Binary Serialization**: Replace JSON with Protocol Buffers. Impact: 25% → 15% (saves ~250ms)
   - **Total improvement**: 2.5s → 0.975s (meets goal)
   - **Rejection rationale**: Don't prioritize backend scaling (doesn't address mobile bottleneck), don't switch protocols (security team veto + risky)

1. Q: You have 12 weeks and must choose 2 of 3 features: (A) Social Recovery (6 weeks, 40% user adoption boost per surveys), (B) Session Keys for gas-free txns (4 weeks, unclear ROI), (C) Multi-chain swap integration (8 weeks, $500K partner revenue). How would you decide and structure the roadmap?
   A:
   - **Framework**: Apply WSJF (Business Value + Time Criticality + Risk Reduction) / Effort
   - **Scoring**:
     - Social Recovery: (9 + 7 + 8) / 6 = 4.0 → **Select**
     - Session Keys: (5 + 4 + 3) / 4 = 3.0
     - Multi-chain Swap: (8 + 6 + 5) / 8 = 2.375 → **Select**
   - **Roadmap**: Weeks 1-6 (Social Recovery), Weeks 5-12 (Multi-chain Swap, parallel after week 5)
   - **Rejection rationale**: Session Keys has weakest quantified value and can be reconsidered in Q2
   - **Success metrics**: Social Recovery adoption >30%, Swap integration revenue >$400K in first quarter

1. Q: Security audit found potential nonce reuse vulnerability on Android devices in MPC signing. Backend shares are secure, but some Android devices use weak entropy. You're 2 weeks from launch with 50K pre-registered users. Mitigation options: (A) Delay launch 4 weeks for full fix, (B) Ship with increased monitoring + rate limiting, (C) Block affected Android versions. What would you do?
   A:
   - **Decision**: Option B (Ship with mitigations) + Option C (Block devices below Android 8.0)
   - **Risk Assessment**: Delay costs $200K marketing spend + user churn. Affected devices <5% of user base (Android <8.0)
   - **Mitigation Plan**:
     - Implement server-side nonce validation with anomaly detection
     - Force key refresh after every 10 signatures on mobile
     - Add device attestation to detect rooted/modified devices
     - Rate limit to 5 signatures/hour for flagged devices
     - Deploy hotfix with RFC 6979 deterministic nonces in week 3 post-launch
   - **Communication**: Transparent security advisory for affected users with migration path to compliant devices
   - **Acceptance criteria**: Launch if exploit cost >$500K (economic infeasibility) and monitoring can detect attacks within 1 hour

1. Q: Backend team wants to use managed cloud HSMs ($10K/month), security team insists on on-premise HSMs ($200K upfront + $5K/month), compliance officer says either works for SOC 2. You're 3 months from audit. Team has no HSM operational experience. What would you choose and how would you mitigate risks?
   A:
   - **Decision**: Cloud HSM (AWS CloudHSM or Azure Dedicated HSM)
   - **Rationale**:
     - Cost: $10K/month × 12 = $120K/year < $200K upfront + $60K/year
     - Time-to-operational: 2-3 weeks vs 8-12 weeks for physical deployment
     - Operational expertise: Cloud provider manages physical security, firmware updates
     - Compliance: Both meet FIPS 140-2 Level 3 required for SOC 2
   - **Risk Mitigations**:
     - Geographic redundancy: Deploy HSM clusters across 3 regions
     - Key ceremony with external auditor witness to establish initial trust
     - Implement key refresh (PSS) every 90 days
     - Contractual data residency guarantees aligned with GDPR
     - Escape hatch: Design architecture to allow migration to on-prem within 6 months if needed

1. Q: You must support 5 new blockchains in 18 months. Engineering capacity: 8 developers. Options: (A) Build modular chain adapter framework (4 months upfront, then 2 weeks per chain), (B) Custom integrate each chain (6 weeks per chain, start immediately), (C) Open-source adapter interface for community contributions. How would you proceed?
   A:
   - **Decision**: Hybrid of A + C (Build framework, then open-source)
   - **Timeline**:
     - Months 1-4: Build adapter framework with 3 reference implementations (ETH, BTC, SOL)
     - Months 5-6: Integrate 2 high-priority chains (Arbitrum, Polygon) to validate framework
     - Months 7-18: Open-source adapter SDK with comprehensive tests, community integrates remaining 3 chains with bounties
   - **Resource Allocation**: 4 devs on framework (months 1-4), 2 devs per chain integration (months 5-18), 2 devs on community support/code review
   - **Break-even Analysis**: Framework cost: 4 months. If enables 2-week integrations vs 6-week custom, saves 4 weeks per chain × 5 chains = 20 weeks saved. Break-even after 5th chain.
   - **Risk**: Framework complexity may exceed estimate. Mitigation: Validate with pilot integration in month 3, adjust timeline if needed

1. Q: Product team wants "instant transactions" using optimistic signing (sign first, validate later). Security team says this creates double-spend window. User surveys show 60% would use instant sends for <$100 transactions. How would you resolve this conflict?
   A:
   - **Decision**: Tiered transaction system with risk-based approach
   - **Design**:
     - **Tier 1 (Instant)**: Transactions <$100, optimistic signing with 1-minute async validation, enterprise liability insurance covers fraud
     - **Tier 2 (Standard)**: $100-$10K, full validation before signing, 5-10 second latency
     - **Tier 3 (Secure)**: >$10K, multi-party approval workflow with enhanced monitoring
   - **Risk Quantification**:
     - Expected fraud rate: 0.1% of instant txns
     - Avg instant txn: $50 → fraud exposure = 0.1% × $50 = $0.05 per txn
     - Insurance cost: $0.02 per txn → net cost $0.07 per txn
     - User satisfaction: Instant sends boost NPS by 15 points (validated via A/B test)
   - **Safeguards**: Velocity limits (5 instant txns/day), device attestation, ML-based fraud detection, 24-hour dispute window
   - **Success Metric**: Instant send adoption >40%, fraud rate <0.2%, positive ROI within 2 quarters

1. Q: Your MPC implementation has been running for 6 months. Options for next iteration: (A) Refactor core for better maintainability (3 months, no new features), (B) Add 3 new chains (2 months each), (C) Implement account abstraction (4 months, competitive parity). Technical debt ratio is 35%. What's your roadmap?
   A:
   - **Decision**: A (Refactor) in Q1, then C (Account Abstraction) in Q2
   - **Reasoning**:
     - Tech debt ratio 35% exceeds healthy threshold (<30%), risking velocity collapse
     - Account Abstraction is table stakes for competitive parity (3 major competitors launched)
     - New chains can be deferred if refactor enables faster future integrations
   - **Phased Approach**:
     - Q1 Month 1: Extract chain adapters, isolate MPC core (high risk, critical path)
     - Q1 Month 2-3: Improve test coverage (70% → 95%), documentation, CI/CD hardening
     - Q2 Month 1-4: Account Abstraction with refactored architecture
   - **Trade-off**: Deferred revenue from new chains (~$300K), but prevents tech debt spiral that could cost 6+ months later
   - **Metrics**: Post-refactor: integration time <3 weeks (vs 6 weeks current), test coverage >95%, tech debt ratio <25%

1. Q: A high-value partner (20% of revenue) requests custom MPC protocol modification that security team says increases attack surface by 15%. Partner threatens to leave if not implemented in 8 weeks. Standard protocol meets their security requirements but not performance needs. How would you handle this?
   A:
   - **Decision**: Negotiate alternative solution that meets performance without custom protocol
   - **Response Strategy**:
     1. **Understand true requirement**: Deep-dive on partner's performance bottleneck (likely network latency, not protocol)
     2. **Propose alternatives**: (a) Dedicated low-latency infrastructure, (b) Pre-signing optimization, (c) Geographic proximity deployment
     3. **Quantify risks**: 15% attack surface increase = potential $X million loss. Is partner revenue > expected loss?
     4. **Offer middle ground**: Isolated deployment with additional monitoring + insurance, not affecting main product
   - **Negotiation Outcome**: Provide dedicated infrastructure (cost: $5K/month) with pre-signing optimization achieving their <200ms target without protocol modification
   - **Escalation Path**: If partner insists on custom protocol, require: (a) external security audit ($50K), (b) partner covers audit + insurance costs, (c) isolated deployment with no shared infrastructure, (d) 3-year revenue commitment
   - **Walking Away**: If partner requirements genuinely compromise security beyond acceptable risk, walk away. 20% of revenue isn't worth 100% of reputation loss in security breach

1. Q: You're building a non-custodial MPC wallet. Regulators require transaction monitoring for AML compliance, but privacy advocates on your team argue this violates user sovereignty. Competitors offer fully private solutions (no monitoring) and fully monitored solutions (custodial). How would you position your product and design compliance features?
   A:
   - **Decision**: Privacy-preserving compliance using zero-knowledge proofs and threshold reporting
   - **Architecture**:
     - **On-Device Risk Scoring**: ML model runs locally, flags suspicious patterns without data upload
     - **Threshold Reporting**: Only report transactions >$10K (regulatory requirement) with minimal metadata
     - **ZK-Compliance**: Use zero-knowledge proofs to demonstrate clean source of funds without revealing transaction graph
     - **User Control**: Optional enhanced privacy mode with trade-off disclosure (may limit institutional access)
   - **Regulatory Engagement**: Proactive dialogue with regulators to validate approach before launch (6-month runway)
   - **Market Position**: "Compliant Privacy" - enable mainstream adoption without sacrificing user sovereignty where possible
   - **Transparency**: Publish open-source compliance logic, regular transparency reports on data practices
   - **Success Criteria**: Pass regulatory review, <5% user opt-out rate for privacy concerns, avoid competitive differentiation solely on "no monitoring" race to bottom
