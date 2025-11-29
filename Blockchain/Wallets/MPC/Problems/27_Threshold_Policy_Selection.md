# Threshold Policy Selection for MPC Wallets

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Security & Product Team

## Problem Statement

**[Important] Q**: Blockchain MPC wallet program must choose an optimal threshold (t-of-n) signing scheme that balances security against availability across mobile, web, and backend cosigners, impacting transaction reliability and user satisfaction. Formulate a structured problem statement using the following [Input] fields.

**A**:

### Brief description of the problem to be analyzed

MPC wallet operators face critical trade-offs when selecting threshold signing policies (e.g., 2-of-3, 3-of-5) that determine how many shares are required to authorize transactions. Inadequate threshold policies cause 5-15% of signing attempts to fail due to unavailable cosigners during device offline periods, service maintenance, or network issues [Source: Supplementary Analysis, 2025-11-28]. Meanwhile, overly permissive thresholds (e.g., 1-of-3) reduce security resilience to device compromise. Organizations need data-driven frameworks to optimize availability (target ≥99.95% monthly signing success) while maintaining compromise tolerance (survive loss of 1-2 shares without halting operations).

### Background and current situation

Current MPC wallet deployments split private key shares across user devices (mobile/web clients) and backend coordinator nodes [Web: Stackup MPC Guide, 2025]. Common configurations include 2-of-3 (one user device, one backup device, one server) or 3-of-5 (two user devices, one guardian, two backend nodes) [Web: Stackup MPC Guide, 2025]. However, threshold policies are often selected ad hoc without formal availability modeling. Mobile devices frequently go offline during OS updates, battery drain, or network switching, while backend maintenance windows create predictable unavailability. Current informal 2-of-3 implementations have experienced 2-4 hour signing outages during maintenance windows when one device was offline [Source: Supplementary Analysis, GPT5.md, line 9]. No formal SLOs exist for signing availability, and helpdesk tickets for "cannot sign" failures consume 15-25% of support capacity [Source: Supplementary Analysis, GPT5.md, line 5].

### Goals and success criteria

- **Signing availability**: Achieve ≥99.95% monthly signing availability (SLO), measured as successful signatures / total signing attempts
- **Failed-sign rate**: Reduce failed signing attempts due to quorum unavailability from current 5-15% to ≤1%
- **Compromise tolerance**: Tolerate loss of up to 1-2 shares without halting operations or requiring emergency recovery
- **Support ticket reduction**: Reduce "cannot sign" helpdesk tickets by ≥50% within 3 months post-implementation
- **User satisfaction**: Maintain user satisfaction (NPS) ≥40 for signing flows (from current estimated 20-30)
- **Timeline**: Define and implement optimized threshold policy within 6 months (Q1-Q2 2025)

### Key constraints and resources

- **Share count limits**: Total shares limited to 3-5 due to UX complexity (more shares = longer setup) and infrastructure cost
- **Mobile offline patterns**: User mobile devices can be offline 10-40% of time depending on usage patterns [Assumption: based on typical mobile connectivity]
- **Backend capacity**: Backend quorum nodes capped at 2-3 for budget constraints (~$5K-10K/mo per region)
- **Cryptographic protocol**: Fixed to ECDSA/EdDSA MPC protocols supported by current library (e.g., GG20, FROST variants)
- **Budget**: Limited to $50K implementation cost + $10K/mo ongoing operational cost
- **Timeline**: 6-month implementation window (Q1-Q2 2025)
- **Compliance**: Must meet non-custodial regulatory positioning (no unilateral server control)

### Stakeholders and roles

- **End users** (50K-500K accounts): Need reliable signing for all on-chain transactions; frustrated by "cannot sign" errors; require p95 signing time ≤30s
- **Security team** (3-5 engineers): Requires compromise tolerance (survive loss of ≥1 share without fund loss); need formal threat model validation
- **SRE/Operations** (2-3 engineers): Need manageable quorum orchestration; require <2h/week maintenance overhead; need clear runbooks for node maintenance
- **Product/UX team** (2 PM + 3 designers): Need low-friction user experience; require ≤3 setup steps for share provisioning; target <5% onboarding abandonment
- **Customer Support** (10-15 agents): Handle 200-400 "cannot sign" tickets/month currently; need ≥50% reduction in signing-related tickets
- **Compliance/Legal** (2-3 officers): Monitor custodial implications; require documentation that no single party can unilaterally sign

### Time scale and impact scope

- **Timeline**: 6-month program (Q1-Q2 2025) for policy selection, implementation, testing, and rollout
- **Affected systems**: All production wallet infrastructure across iOS, Android, web clients, and backend coordinator services
- **User impact**: 100% of active accounts (estimated 50K-500K accounts) will be affected across all transaction types
- **Geographic scope**: Global deployment across all supported regions (US, EU, APAC)
- **Transaction scope**: Affects all on-chain transactions (transfers, swaps, smart contract interactions) and authentication workflows
- **Revenue impact**: Failed signatures directly impact transaction volume; estimated $50K-200K/mo revenue at risk from failed transactions

### Historical attempts and existing solutions (if any)

An informal 2-of-3 threshold policy was piloted with one mobile device, one backup device, and one backend server share [Source: Supplementary Analysis, GPT5.md, line 9]. During pilot phase, mobile OS updates (iOS 17, Android 14 releases) and backend maintenance windows led to 2-4 hour signing outages when one device was unavailable [Source: Supplementary Analysis, GPT5.md, line 9]. No formal availability SLOs were defined during pilot. Key lessons learned:
- Mobile device availability is unpredictable (OS updates, battery drain, app backgrounding)
- Backend maintenance requires coordination to avoid breaking quorum
- Users expect instant signing; 30s+ delays cause abandonment
- 2-of-3 may be too tight for real-world device reliability

### Known facts, assumptions, and uncertainties

**Facts**:
- MPC wallets commonly use 2-of-3 or 3-of-5 threshold schemes [Web: Stackup MPC Guide, 2025; Web: Safeheron MPC vs Multisig, 2025]
- Mobile devices experience intermittent offline periods during OS updates, low battery, or network switching
- Backend maintenance windows create predictable unavailability (estimated 2-4 hours/month per node)
- Current pilot experienced 2-4 hour outages during maintenance [Source: Supplementary Analysis, GPT5.md, line 9]
- Helpdesk "cannot sign" tickets consume 15-25% of support capacity [Source: Supplementary Analysis, GPT5.md, line 5]

**Assumptions**:
- 3-of-5 threshold may provide better resilience with acceptable UX overhead [Source: Supplementary Analysis, GPT5.md, line 10]
- Device online rates estimated at 60-90% based on typical mobile usage patterns (requires validation with telemetry)
- Backend nodes can achieve 99.5-99.9% uptime per node with proper SRE practices
- Users will tolerate ≤3 share setup steps during onboarding

**Uncertainties**:
- Exact distribution of device-online rates across user segments (power users vs casual users, iOS vs Android)
- Real-world quorum availability under peak load (holiday shopping, market volatility)
- Optimal number of backend quorum nodes to balance cost vs availability
- User tolerance for guardian-based recovery flows (social recovery complexity)
- Impact of threshold choice on regulatory custody classification (does 3-of-5 with 3 backend shares imply custody?)

## Reference

### Web Sources
- [Web: Stackup MPC Guide, 2025] - MPC Wallets: A Complete Technical Guide. Stackup. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide
- [Web: Safeheron MPC vs Multisig, 2025] - MPC or Multisig Wallets Which Offers Better Security. Safeheron. https://safeheron.com/blog/mpc-vs-multisig-wallets-security-differences-similarities

### Supplementary Sources
- [Source: Supplementary Analysis, GPT5.md, 2025-11-28] - Blockchain MPC Wallet Problem Extraction. Lines 1-11. Internal analysis document.
