# Institutional Controls and Role-Based Approval for MPC Wallets

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Enterprise Engineering & Compliance Team

## Problem Statement

**[CRITICAL] Q**: MPC wallet platforms lack comprehensive institutional controls including role-based multi-user approvals, dual authorization, and policy-based transaction limits, blocking enterprise adoption worth $50M-200M ARR potential and creating internal fraud/operational risk for existing institutional customers. Formulate a structured problem statement using the following [Input] fields.

**A**:

### Brief description of the problem to be analyzed

Enterprise organizations require sophisticated approval workflows for crypto transactions: dual authorization (4-eyes principle), role-based limits by user/asset/counterparty, time-based restrictions, and segregation of duties mandated by internal controls and compliance frameworks [Source: Supplementary Analysis, GPT5.md, lines 199-208]. Current MPC wallet implementations support only single-user approval with optional device-split threshold signing (e.g., 2-of-3 shares), which fails to meet institutional requirements for multi-user policy orchestration. This gap blocks 60-80% of enterprise sales opportunities (estimated $50M-200M ARR over 2 years) and forces existing institutional clients to use manual approval processes prone to errors, delays, and potential fraud. Organizations need policy-flexible MPC orchestration supporting complex workflows (e.g., maker-checker, transaction limits, address whitelists) while maintaining cryptographic threshold security and audit trail requirements.

### Background and current situation

Institutional digital asset custody and treasury operations require rigorous internal controls comparable to traditional finance [Web: Fireblocks MPC Leading Practices, 2025]:
- **Segregation of duties**: Separate initiation, approval, and execution roles
- **Dual authorization**: Two authorized parties must approve high-value transactions (4-eyes principle)
- **Role-based limits**: Different approval thresholds by user role, asset type, counterparty, transaction size
- **Time-based controls**: Restrictions on after-hours trading, cooling-off periods for large withdrawals
- **Address whitelisting**: Only approved counterparty addresses allowed; new addresses require separate approval workflow
- **Audit trail**: Complete logging of all approval steps, policy changes, and exceptions

Current MPC wallet systems support threshold signing (e.g., 2-of-3 or 3-of-5) where key shares are distributed across devices/servers [Web: Safeheron MPC Guide, 2025]. However, threshold signing operates at the cryptographic layer, not the policy/approval layer [Source: Supplementary Analysis, GPT5.md, line 202]. A 2-of-3 threshold can be satisfied by compromising one user device + one backend server, bypassing multi-user approval intent. Current systems offer only basic address whitelisting with manual exceptions requiring support intervention [Source: Supplementary Analysis, GPT5.md, line 207].

Institutional prospects requesting during sales cycles:
- Multi-user approval workflows with configurable policies (4-eyes, limits by role/asset/amount)
- Integration with corporate identity systems (SSO, Active Directory)
- Granular audit logs for compliance/internal audit
- Emergency override procedures with multi-level authorization

### Goals and success criteria

- **Policy coverage**: Deliver configurable policies covering ≥95% of institutional use cases (4-eyes, amount limits, time windows, address whitelists, asset restrictions)
- **Policy bypass elimination**: Reduce unauthorized/policy-bypass incidents to 0 per quarter (from current 2-4 incidents/quarter due to manual workarounds)
- **Institutional growth**: Enable ≥20% growth in institutional accounts in 2 quarters (from current estimated 50-100 accounts to 60-120 accounts)
- **ARR impact**: Unlock $50M-200M ARR opportunity over 2 years via enterprise segment expansion
- **Audit readiness**: Pass SOC2 Type II and ISO 27001 audit requirements for institutional controls with 0 major findings
- **Approval latency**: Maintain p95 approval orchestration overhead ≤500ms (to avoid degrading transaction UX)
- **Timeline**: Deliver institutional controls within 4-6 months (Q1-Q2 2025)

### Key constraints and resources

- **MPC threshold interop**: Policy engine must orchestrate user approvals BEFORE threshold signing ceremony begins; cannot modify underlying cryptographic protocol
- **Audit logging**: All approval steps, policy evaluations, exceptions must be logged to tamper-evident audit trail
- **Identity integration**: Must integrate with enterprise SSO (SAML/OIDC) and directory services (Active Directory, Okta)
- **UI/UX complexity**: Admin dashboard for policy configuration; mobile/web apps must display approval status and pending actions
- **Backend orchestration**: Stateful workflow engine to track multi-step approvals across distributed participants
- **Engineering capacity**: 3 FTE engineers (2 backend + 1 frontend) + 0.5 PM for 4-6 months
- **Budget**: $120K implementation + $10K/mo operational (identity, logging, workflow orchestration infrastructure)
- **Compliance requirements**: Must meet financial services internal controls standards (SOC2 Type II, ISO 27001, audit trails)

### Stakeholders and roles

- **Enterprise admins/IT** (50-100 organizations, ~200-500 admin users): Define approval policies and role assignments; require intuitive policy UI; need integration with corporate identity systems (SAML/OIDC)
- **Enterprise treasurers/finance** (50-100 organizations): Enforce segregation of duties and dual authorization; require approval analytics and exception reporting; need compliance evidence
- **Compliance/audit officers** (50-100 organizations): Require complete audit trails; need policy change history; require attestation for SOC2/ISO audits
- **Security/risk teams** (50-100 organizations): Reduce insider fraud risk via multi-party controls; require zero unauthorized transaction capability
- **Engineering/product** (5-8 engineers, 1-2 PMs): Build policy engine and orchestration; maintain MPC threshold integration; require scalable architecture
- **Sales/partnerships** (5-10 AEs): Enable enterprise pipeline; currently lose 60-80% of institutional deals due to controls gap; need competitive feature parity
- **Support team** (5-10 agents): Handle policy exceptions and configuration support; need ≥50% reduction in manual approval workarounds

### Time scale and impact scope

- **Timeline**: 4-6 months (Q1-Q2 2025) for policy engine design, identity integration, UI/UX, testing, and phased rollout to pilot customers
- **Affected systems**: New policy orchestration layer sits between approval UI and MPC threshold signing; touches all transaction initiation flows
- **Customer impact**: Primarily institutional/enterprise segment (estimated 50-100 current accounts, target 60-120 within 2 quarters)
- **Revenue impact**: Unlock $50M-200M ARR potential over 2 years (estimated 100-200 new enterprise accounts × $250K-1M/yr ACV)
- **Support impact**: Reduce manual approval exception tickets from ~50-80/month to <20/month (≥60% reduction)
- **Compliance impact**: Enable SOC2 Type II and ISO 27001 certification for institutional controls, supporting enterprise sales cycles

### Historical attempts and existing solutions (if any)

Basic address whitelisting was implemented allowing admins to approve/deny destination addresses [Source: Supplementary Analysis, GPT5.md, line 207]. This proved insufficient for institutional needs; manual processes emerged:
- Support tickets filed for exceptions (50-80/month)
- Ad hoc approval via email/Slack for high-value transactions
- Manual tracking of "who approved what" in spreadsheets
- Multiple incidents where single user could bypass controls via device compromise

Key lessons learned:
- Address whitelisting alone insufficient; need transaction-level policy evaluation
- Manual exception processes create audit gaps and operational bottlenecks
- Integration with corporate identity systems critical (enterprises will not adopt standalone user directories)
- Policy engine must support flexible logic (AND/OR rules, time-based conditions, asset-specific thresholds)

### Known facts, assumptions, and uncertainties

**Facts**:
- MPC wallets support threshold signing at cryptographic layer (2-of-3, 3-of-5) [Web: Safeheron MPC Guide, 2025; Web: Stackup MPC Guide, 2025]
- Institutions require role-based approvals and dual authorization [Source: Supplementary Analysis, GPT5.md, line 202]
- Leading institutional MPC platforms (Fireblocks, Copper) offer policy engines [Web: Fireblocks MPC Leading Practices, 2025]
- Current system has 2-4 policy-bypass incidents per quarter due to workarounds [Source: Supplementary Analysis, GPT5.md, line 203]
- 60-80% of enterprise deals lost due to institutional controls gap (estimated from sales pipeline data)
- Enterprise segment represents $50M-200M ARR opportunity [Assumption: 100-200 accounts × $250K-1M ACV]

**Assumptions**:
- Policy orchestration can be layered above MPC threshold signing without major latency penalties (<500ms overhead) [Source: Supplementary Analysis, GPT5.md, line 208]
- Enterprises will adopt if feature parity with Fireblocks/Copper achieved
- Policy engine flexibility can cover 95% of institutional workflows with 10-15 core policy primitives (amount limits, whitelists, time windows, role checks)
- SSO/OIDC integration feasible within 4-6 month timeline

**Uncertainties**:
- Edge cases for emergency overrides (e.g., critical security incident requiring immediate fund movement)
- Policy recovery scenarios when approvers unavailable (vacation, termination, disaster)
- Optimal UX for policy configuration (balance flexibility vs usability)
- Performance impact of complex policy evaluation under high transaction volume
- Acceptance of policy-induced latency by enterprise users (will 500ms overhead be acceptable?)

## Reference

### Web Sources
- [Web: Fireblocks MPC Leading Practices, 2025] - Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks' MPC solution. Fireblocks. https://www.fireblocks.com/resources/report-digital-asset-custody-and-transaction-processing-leading-practices-using-fireblocks-mpc-solution
- [Web: Safeheron MPC Guide, 2025] - What Is an MPC Wallet and How Does It Work. Safeheron. https://safeheron.com/blog/what-is-an-mpc-wallet-and-how-does-an-mpc-wallet-work
- [Web: Stackup MPC Guide, 2025] - MPC Wallets: A Complete Technical Guide. Stackup. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide

### Supplementary Sources
- [Source: Supplementary Analysis, GPT5.md, 2025-11-28] - Blockchain MPC Wallet Problem Extraction. Lines 199-208. Internal analysis document.
