# Institutional Controls and Role-Based Approval for MPC Wallets – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Enterprise Engineering & Compliance Team

---

## Pre-Section: Context Recap

- **Problem title**: Institutional controls and role-based approval for MPC wallet platforms
- **Current state**:
  - Leading institutional MPC wallet platforms (e.g., Fireblocks, Copper, Safeheron) provide policy engines that support role-based approvals, transaction limits, and whitelists tightly integrated with enterprise identity systems [Source: Fireblocks Digital Asset Custody and Transaction Processing Leading Practices, Fireblocks, 2025; Source: Safeheron – What Is an MPC Wallet and How Does It Work, Safeheron, 2025; Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025].
  - Many mid-market and emerging MPC wallet providers still expose only cryptographic threshold signing (e.g., 2-of-3 shares) without full institutional policy orchestration, leading to reliance on manual approvals and out-of-band checks [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, sections "Security Benefits and Trade-offs" and "Operational Considerations"].
  - The target platform currently supports device- or server-split MPC signing but lacks enterprise-grade role-based workflows, dual authorization, fine-grained limits, and integrated audit trails, resulting in 60–80% of institutional deals being lost during evaluation [Source: Problem statement – Institutional Controls and Role-Based Approval for MPC Wallets, 2025].
- **Pain points**:
  - **Control gap**: Threshold signing protects keys but not *who* can approve *which* transaction under *what* conditions; this leaves institutions without mandated segregation of duties and dual control [Source: COSO Internal Control – Integrated Framework, COSO, 2013; Source: What Is the Four-Eyes Principle?, UNIDO, accessed 2025; Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025].
  - **Manual workflows**: Enterprises resort to emails, chat approvals, and spreadsheets to track “who approved what”, creating audit gaps and policy bypass opportunities [Source: Problem statement – Background and current situation].
  - **Deal loss and ARR impact**: Lack of institutional controls causes 60–80% of enterprise opportunities to be lost and blocks $50M–200M ARR potential over two years [Source: Problem statement – Goals and success criteria].
  - **Operational risk**: Single power users with broad permissions and weak approval schemes can push high-value transfers with limited oversight, increasing insider-fraud and operational error risk [Source: Is the Four Eyes Principle the Most Effective Way to Block Fraud?, Trustpair, 2024; Source: COSO Internal Control – Integrated Framework, COSO, 2013].
- **Goals**:
  - Achieve policy coverage for ≥95% of institutional use cases (4‑eyes, role- and asset-based limits, time windows, whitelists) and eliminate policy-bypass incidents (target: 0 per quarter) [Source: Problem statement – Goals and success criteria].
  - Unlock $50M–200M ARR opportunity from the enterprise segment while enabling ≥20% growth in institutional accounts within two quarters [Source: Problem statement – Goals and success criteria].
  - Meet SOC 2 Type II and ISO 27001 internal control expectations for transaction authorization and logging with 0 major findings in external audits [Source: SOC 2® Trust Services Criteria, AICPA, 2018; Source: ISO/IEC 27001:2022 Information Security, Cybersecurity and Privacy Protection – Information Security Management Systems, ISO, 2022].
  - Maintain acceptable UX by keeping policy engine overhead ≤500 ms at p95 for approval orchestration [Estimate: Based on typical MPC signing budgets of 100–300 ms and enterprise UX expectations in treasury/payment systems, Medium confidence].
- **Hard constraints**:
  - Cannot fundamentally change the underlying MPC threshold protocol; orchestration must sit *above* signing and coordinate which users/roles can trigger the signing ceremony [Source: Problem statement – Key constraints and resources].
  - Must integrate with enterprise identity providers (SAML/OIDC, Active Directory, Okta) and respect existing role catalogs and approval chains [Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks’ MPC Solution, Fireblocks, 2025].
  - Engineering capacity limited to ~3 FTE (2 backend, 1 frontend) + 0.5 PM for 4–6 months with ~$120K implementation budget and $10K/month operational budget [Source: Problem statement – Key constraints and resources].
  - Need to roll out with minimal disruption to live institutional flows and maintain high availability (target ≥99.9% uptime for transaction services) [Estimate: Based on typical SLAs for institutional custody platforms and WaaS offerings, Medium confidence].
- **Key facts**:
  - Four-eyes principle and segregation of duties are standard requirements in regulated finance, often mandated explicitly in internal control and payment authorization policies [Source: What Is the Four-Eyes Principle?, UNIDO, accessed 2025; Source: What Is the Four-Eyes Principle That Regulated Companies Need to Adhere To?, MK Fintech Partners, 2024; Source: COSO Internal Control – Integrated Framework, COSO, 2013].
  - MPC wallets separate key protection (cryptography) from authorization (policy); failing to implement robust policy controls negates a core institutional value proposition [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Source: Safeheron – What Is an MPC Wallet and How Does It Work, Safeheron, 2025].
  - Leading custodians market policy engines as a primary differentiator to institutional clients, especially for treasury, OTC trading, and operational wallets [Source: Fireblocks Wallets-as-a-Service – Policy Engine Overview, Fireblocks, 2024; Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

1. **Core problem**  
   The current MPC wallet platform provides strong cryptographic key protection via threshold signing but lacks a comprehensive institutional control layer that enforces role-based approvals, dual authorization, time-based constraints, and granular transaction limits. As a result, enterprises cannot encode their internal control policies directly into the wallet and instead depend on fragile manual processes or external systems to govern high-value transactions [Source: Problem statement – Brief description of the problem; Source: Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks’ MPC Solution, Fireblocks, 2025].

2. **Key contradictions**
   - **Key security vs. governance completeness**: The platform has invested in MPC to remove single private-key risk, yet the absence of multi-user policy orchestration leaves governance gaps similar to traditional single-signer wallets [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].
   - **Enterprise expectations vs. product scope**: Institutional customers expect the same or better control environment than traditional banking (dual control, segregation of duties, approval hierarchies), but the product scope has historically treated “policy engine” as a secondary feature rather than a core capability [Source: COSO Internal Control – Integrated Framework, COSO, 2013; Source: What Is the Four-Eyes Principle?, UNIDO, accessed 2025].
   - **Sales promises vs. operational reality**: Sales teams promote MPC-based security and “enterprise readiness”, yet missing institutional controls cause 60–80% of deals to be lost and force existing customers to bolt on manual approvals, undermining trust and differentiation [Source: Problem statement – Background and current situation].

3. **Who is in conflict?**
   - **Enterprise treasurers/finance vs. product engineering**: Treasurers demand on-ledger enforcement of policies (limits, multi-user approvals), while engineering teams are wary of introducing complex stateful workflows that might affect latency and availability [Source: Problem statement – Stakeholders and roles].
   - **Compliance/audit vs. platform simplicity**: Compliance teams require exhaustive audit trails and segregation of duties, but the platform historically optimized for simple single-admin models and lightweight logging [Source: SOC 2® Trust Services Criteria, AICPA, 2018; Source: ISO/IEC 27001:2022, ISO, 2022].
   - **Security/risk vs. adoption friction**: Security teams advocate stricter controls (e.g., mandatory dual authorization for high-risk flows), while some customers fear friction and slowed operations; the platform must reconcile risk reduction with UX [Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025].

### 1.2 Goals and conditions

- **Control completeness goal**: Cover ≥95% of institutional approval and policy use cases through configurable policies (4‑eyes, amount tiers, asset/counterparty-specific rules, time windows, whitelists/blacklists) [Source: Problem statement – Goals and success criteria; Source: Fireblocks Digital Asset Custody and Transaction Processing Leading Practices, Fireblocks, 2025].
- **Risk reduction goal**: Reduce unauthorized or policy-bypass incidents from the current 2–4 per quarter (due to manual workarounds and weak controls) to 0 per quarter for transactions above defined high-value thresholds [Source: Problem statement – Goals and success criteria].
- **Business impact goal**: Enable ≥20% growth in institutional accounts in two quarters and unlock $50M–200M ARR potential over two years [Source: Problem statement – Goals and success criteria].
- **Compliance goal**: Achieve SOC 2 Type II and ISO 27001 certification for institutional transaction controls with no major findings related to authorization, logging, or segregation of duties [Source: SOC 2® Trust Services Criteria, AICPA, 2018; Source: ISO/IEC 27001:2022, ISO, 2022].
- **Performance goal**: Ensure end-to-end policy evaluation and approval orchestration add ≤500 ms overhead at p95 to signing flows for institutional transactions [Estimate: Based on typical MPC signing budgets and enterprise payment UX expectations, Medium confidence].

### 1.3 Extensibility and reframing

- **Reframing from "MPC wallet" to "institutional transaction control system"**:  
  Treat the MPC wallet not just as a key-management system but as part of a broader institutional control stack that includes identity, policy, approvals, monitoring, and audit. This perspective highlights that cryptography is necessary but not sufficient for institutional-grade safety [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Source: COSO Internal Control – Integrated Framework, COSO, 2013].

- **Attribute reframing – policy engine as a configurable platform**:  
  View the policy engine as a configurable platform with core primitives (roles, thresholds, time windows, whitelists, risk scores) that can compose into many enterprise-specific workflows rather than as a collection of one-off features [Source: Fireblocks Wallets-as-a-Service – Policy Engine Overview, Fireblocks, 2024].

- **Scope reframing – from "security feature" to "sales enabler"**:  
  Institutional controls should be framed not just as a compliance cost, but as a key enabler for winning and retaining high-ACV enterprise accounts; this supports prioritization and investment [Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025; Source: Problem statement – Goals and success criteria].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **MPC signing layer**: Threshold signing protocols and infrastructure responsible for generating valid on-chain signatures without reconstructing private keys [Source: Safeheron – What Is an MPC Wallet and How Does It Work, Safeheron, 2025; Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].
- **Policy engine**: Rule-based system that evaluates each transaction request against configurable policies (who, what, where, when, how much) and determines required approvals or automatic rejection [Source: Fireblocks Digital Asset Custody and Transaction Processing Leading Practices, Fireblocks, 2025].
- **Identity and roles**: Integration layer with SSO/IdP (SAML/OIDC) and directory services (Active Directory, Okta) mapping human users and service accounts to wallet roles and permissions [Source: ISO/IEC 27001:2022, ISO, 2022; Source: SOC 2® Trust Services Criteria, AICPA, 2018].
- **Approval workflows**: Mechanisms for collecting approvals from multiple users (makers/checkers, approver chains) including notifications, escalation, and timeouts.
- **Audit and monitoring**: Tamper-evident logs recording all policy evaluations, approvals, overrides, and configuration changes; real-time monitoring for anomalies (e.g., repeated high-risk transfer attempts).

### 2.2 Balance and "degree" issues

- **Security vs. UX friction**:  
  Strict policies (e.g., mandatory dual authorization for all transactions) maximize control but may slow operations; overly permissive defaults reduce friction but leave systems exposed to insider fraud and operational errors [Source: What Is the Four-Eyes Principle That Regulated Companies Need to Adhere To?, MK Fintech Partners, 2024; Source: Is the Four Eyes Principle the Most Effective Way to Block Fraud?, Trustpair, 2024].

- **Centralization vs. decentralization of control**:  
  Centralized admin roles simplify configuration but risk creating “super-admins” with broad powers; strong segregation of duties requires multiple admin roles, independent reviewers, and robust approval flows for policy changes [Source: COSO Internal Control – Integrated Framework, COSO, 2013; Source: ISO/IEC 27001:2022, ISO, 2022].

- **Policy depth vs. performance**:  
  Deep, multi-dimensional policies (combining user role, asset, counterparty, jurisdiction, time, historical behavior) increase expressivity but may add latency and complexity to policy evaluation [Estimate: Based on design patterns in enterprise policy engines and MPC custody platforms, Medium confidence].

### 2.3 Causal chains

1. **Manual controls chain**:  
   No on-platform policy engine ⇒ approvals handled via email/chat ⇒ incomplete logging and weak enforcement ⇒ higher probability of policy bypass and disputes over “who approved what” ⇒ increased audit findings and lost deals.

2. **Insider risk chain**:  
   Broad admin privileges and single-user approvals ⇒ insider or compromised admin can unilaterally push large transfers ⇒ incident discovered late due to limited real-time monitoring ⇒ material losses and regulatory scrutiny [Source: Is the Four Eyes Principle the Most Effective Way to Block Fraud?, Trustpair, 2024; Source: COSO Internal Control – Integrated Framework, COSO, 2013].

3. **Sales funnel chain**:  
   Enterprise RFP requires dual authorization, role-based limits, and comprehensive audit logs ⇒ platform cannot demonstrate feature parity with leading MPC custodians ⇒ prospect drops vendor from shortlist ⇒ ARR opportunity lost [Source: Fireblocks Wallets-as-a-Service – Policy Engine Overview, Fireblocks, 2024; Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and conflicts

| Stakeholder | Goals | Constraints | Potential Conflicts |
|------------|-------|------------|----------------------|
| **Enterprise admins/IT** | Centralized configuration, seamless SSO, low operational overhead | Limited headcount, existing IAM tooling, change-management processes | Resist overly complex policy UIs; demand robust audit logs and ease of use |
| **Treasury/finance teams** | Strong segregation of duties, four-eyes approvals, real-time visibility into pending approvals | Need to support urgent transfers and trading windows; cannot tolerate long delays | Conflict with traders or product teams who want faster execution and fewer approvals |
| **Compliance/audit officers** | Clear, tamper-evident audit trails; alignment with SOC 2/ISO27001 controls; minimal manual workarounds | Limited technical bandwidth; depend on platform reports | Tension with engineering and product when compliance asks for stricter controls or more evidence |
| **Security/risk teams** | Minimize insider and operational fraud; enforce least privilege and monitoring | Limited authority over sales commitments; must align with business priority | May push for stricter controls than business lines initially accept |
| **Sales/partnerships** | Win institutional deals; show competitive parity with leading providers | Bound by current feature set and roadmap; risk of overselling | May promise controls that engineering cannot deliver in timeframe |
| **MPC wallet provider (platform)** | Grow ARR, maintain uptime, differentiate via security and governance | 3 FTE capacity; 4–6 month timeline; limited infra budget | Trade-offs between feature depth, timeline, and technical risk |

[Source: Problem statement – Stakeholders and roles; Source: SOC 2® Trust Services Criteria, AICPA, 2018; Source: Digital Asset Custody and Transaction Processing Leading Practices, Fireblocks, 2025.]

### 3.2 Environmental factors

- **Regulatory tightening**: Financial regulators increasingly expect bank-like internal controls for digital asset custodians, including dual authorization, segregation of duties, and detailed audit logging [Source: COSO Internal Control – Integrated Framework, COSO, 2013; Source: SOC 2® Trust Services Criteria, AICPA, 2018].
- **Competitive pressure**: Large custodians emphasize policy engines and institutional-grade governance in marketing, raising the baseline expectations for any serious institutional MPC wallet [Source: Fireblocks Wallets-as-a-Service – Policy Engine Overview, Fireblocks, 2024; Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025].
- **Internal IT complexity**: Enterprises already operate complex approval workflows in ERP and payment systems, expecting crypto treasury tools to plug into existing patterns rather than invent entirely new ones [Estimate: Based on common enterprise payment/treasury system designs and vendor RFPs, Medium confidence].

### 3.3 Responsibility and room for maneuver

- **Platform provider**: Owns design and implementation of the policy engine, integration with MPC signing, and exposure of configuration and logs to customers. It can decide prioritization, architecture, and rollout strategy.
- **Enterprise customers**: Define required policies, roles, and approval matrices and must participate in pilots and feedback loops.
- **Regulators and auditors**: Set expectations and evaluate whether implemented controls meet standards; they cannot design details but can drive deadlines and scope.

[Source: COSO Internal Control – Integrated Framework, COSO, 2013; Source: ISO/IEC 27001:2022, ISO, 2022; Source: Problem statement – Time scale and impact scope.]

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **Consumer-first MPC adoption**: Early MPC wallets focused on consumer and retail flows (e.g., non-custodial wallets) where single-user approvals were acceptable; enterprise-grade governance came later [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Source: Safeheron – What Is an MPC Wallet and How Does It Work, Safeheron, 2025].
2. **Key security > governance**: Initial market narrative emphasized “no single private key” and resilience against hacks, overshadowing the need for institutional-grade internal controls on *transaction* approvals [Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025].
3. **Manual workaround phase**: As institutional customers onboarded, they layered email/Slack approvals and spreadsheets on top of single-user MPC flows, treating governance as a process issue rather than a platform design problem [Source: Problem statement – Historical attempts and existing solutions].
4. **Competitive benchmark shift**: Leading custodians introduced full policy engines and promoted them heavily, creating a gap between platform capabilities and buyer expectations [Source: Fireblocks Wallets-as-a-Service – Policy Engine Overview, Fireblocks, 2024].

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - Lack of standardized internal control frameworks specifically tailored for MPC-based custody; providers need to map generic controls (COSO, SOC 2, ISO 27001) to crypto-native workflows [Source: COSO Internal Control – Integrated Framework, COSO, 2013; Source: ISO/IEC 27001:2022, ISO, 2022].
  - Strong early focus on cryptography and key ceremony engineering vs. workflow and policy design.

- **Direct causes**:
  - Product roadmap prioritized key management and integrations over institutional governance features given limited FTE capacity [Estimate: Based on typical startup prioritization in infrastructure products, Medium confidence].
  - Underestimation of institutional requirements; early assumptions that manual approvals or integration with external tools would be “good enough” [Source: Problem statement – Historical attempts and existing solutions].

### 4.3 Root issues

- **Governance under-specification**: The product did not treat institutional controls as a first-class design domain with explicit requirements, patterns, and threat models.
- **IAM and policy expertise gap**: Team expertise is weighted towards MPC cryptography and backend engineering rather than enterprise IAM and internal controls design.
- **Feedback loop delay**: Pain points around manual approvals, audit findings, and lost deals took multiple quarters to coalesce into clear product requirements.

[Source: Problem statement – Historical attempts and existing solutions; Source: COSO Internal Control – Integrated Framework, COSO, 2013; Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025.]

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- Institutional prospects will continue to reject platforms without robust policy engines, capping institutional ARR and weakening credibility in RFP processes [Source: Digital Asset Custody and Transaction Processing Leading Practices, Fireblocks, 2025].
- Existing institutional customers will extend or harden manual approval processes, increasing operational cost and audit complexity while still leaving policy-bypass pathways.
- Regulatory and audit expectations for digital asset custody will likely rise, making the absence of built-in role-based approvals and dual authorization a formal deficiency [Source: SOC 2® Trust Services Criteria, AICPA, 2018; Source: ISO/IEC 27001:2022, ISO, 2022].

### 5.2 Early signals

- Prospects explicitly referencing Fireblocks/Copper policy engines as baseline expectations in RFPs.
- Growth of marketing material from MPC custodians emphasizing granular policy engines, four-eyes authorization, and real-time monitoring [Source: MPC Custody Explained: Why It’s Essential in 2025, IOFinnet, 2025; Source: Fireblocks Wallets-as-a-Service – Policy Engine Overview, Fireblocks, 2024].
- Internal sales feedback and win/loss analyses citing “missing institutional controls” as a recurring deal-breaker [Source: Problem statement – Known facts, assumptions, and uncertainties].

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**:  
  Policy engine and role-based approvals are delivered within 6 months, successfully piloted with anchor institutional customers, and used as a flagship capability in sales. Institutional deals increase, audit findings are clean, and manual workarounds shrink by ≥60%.

- **Baseline scenario**:  
  A partial policy engine is delivered but lacks full expressivity or ease of use; some institutional deals are recovered but gaps remain vs. top-tier competitors. Governance gap narrows but does not fully close.

- **Pessimistic scenario**:  
  Implementation is delayed or under-scoped; regulators or auditors flag internal control weaknesses; a high-profile incident (policy bypass or insider fraud) occurs at a customer, eroding trust. Competitors capture most high-value institutional business.

[Estimate: Based on typical enterprise infrastructure roadmap risks, Medium confidence.]

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **MPC core**: Robust threshold signing infrastructure already in place; this can serve as a strong foundation for policy-dependent transaction execution [Source: Safeheron – What Is an MPC Wallet and How Does It Work, Safeheron, 2025; Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].
- **Institutional customer base**: Existing 50–100 institutional accounts provide a ready cohort for pilots and design partnerships [Source: Problem statement – Time scale and impact scope].
- **Security posture**: Focus on MPC cryptography and secure key management positions the platform as a credible partner for extended governance features.

### 6.2 Capability gaps

- **IAM and policy design**: Limited in-house expertise in enterprise IAM, approval workflows, and formal internal controls design (e.g., mapping to SOC 2/ISO 27001 controls).
- **Admin UX for policy configuration**: No dedicated interface for creating, testing, and auditing complex multi-user policies.
- **Observability specific to governance**: Current telemetry focuses on signing events, not on policy evaluations, approval timelines, or override patterns.

### 6.3 Buildable capabilities (1–6 months)

- **Policy engine MVP**: A rule engine that supports core primitives (roles, thresholds, time windows, whitelists) and integrates with MPC signing and identity providers.
- **Policy simulation and dry-run tooling**: Ability for admins to simulate policies against historical transactions before enabling them in production.
- **Governance analytics**: Dashboards summarizing approval latency, policy violations, overrides, and distribution of approvals by role.

[Estimate: Based on 3 FTE capacity over 4–6 months and scope of similar policy engines in custody platforms, Medium confidence.]

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Rise of institutional MPC wallets; internal controls expectations from traditional finance; current platform gap.
- **Core problem**: No integrated institutional control layer (role-based approvals, dual authorization, policy limits, audit trails).
- **Internal structure**: Relationship between MPC signing, policy engine, IAM integration, and audit.
- **External environment**: Regulatory expectations, competitor capabilities, institutional procurement patterns.
- **Options**: Build full policy engine; incremental controls; rely on external systems; hybrid approaches.
- **Risks**: Implementation complexity, UX friction, performance regression, partial adoption.
- **Recommendations**: Deliver a policy engine MVP with clear prioritization, phased rollout, and strong validation.

### 7.2 Key judgments (for validation)

1. Institutional controls are **necessary** for winning and retaining high-value enterprise customers and cannot be fully substituted by manual processes or external systems.
2. A **policy engine MVP** covering the core 4–5 primitives (roles, thresholds, time windows, whitelists, dual authorization) is feasible within 4–6 months given 3 FTEs, if scope focus and technical risks are managed.
3. Integration with existing MPC signing and IdPs can be achieved without exceeding the 500 ms overhead target for policy evaluation in typical institutional flows.

[Estimate: Synthesized from problem statement constraints, vendor capabilities in public materials, and experience with enterprise policy engines, Medium confidence; validation via detailed design and prototyping is required.]

### 7.3 Alternative high-level paths

- **Path A – Full integrated policy engine**: Build a first-party policy engine deeply integrated into MPC signing and IAM, covering most institutional use cases.
- **Path B – Minimal controls + reliance on external systems**: Implement only basic controls (e.g., transaction limits, address whitelists) and rely on customers’ existing approval systems via APIs or manual controls.
- **Path C – Hybrid approach**: Deliver a focused on-chain/off-chain policy engine for high-risk flows while integrating with external approval systems for low-risk or back-office flows.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- **Feature parity bias**: Overemphasis on matching competitor checklists may ignore unique customer contexts or overbuild complexity.
- **Security-first bias**: Security and compliance perspectives may overweight risk reduction relative to operational agility and UX.
- **Enterprise-centric bias**: Focus on institutional customers might neglect smaller clients whose needs are simpler and who may not want heavy governance.

### 8.2 Required intelligence

- Detailed **win/loss analysis** across enterprise opportunities specifying which control gaps caused losses.
- **Customer requirement baselines**: Survey of existing institutional customers’ current internal control frameworks and how they expect custody tools to integrate.
- **Performance benchmarks**: Prototype policy evaluation combined with MPC signing to measure end-to-end latency impact under realistic workloads.

### 8.3 Validation plan

- Run **design partner workshops** with 5–10 representative institutional customers to validate policy primitives, UI flows, and integration points.
- Implement a **pilot deployment** of the policy engine with a small cohort of customers, monitoring approval latency, error rates, and override patterns for 4–8 weeks.
- Conduct **pre-audit reviews** with external auditors to align implementation with SOC 2 and ISO 27001 controls and pre-empt major findings.

[Source: SOC 2® Trust Services Criteria, AICPA, 2018; Source: ISO/IEC 27001:2022, ISO, 2022; Estimate: Based on standard enterprise product validation practices, Medium confidence.]

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Policy primitives may be expanded (e.g., risk-based scoring, behavior-based rules) once basic approvals and limits are in place.
- Metrics for success may be refined to include more granular indicators (e.g., proportion of transactions auto-approved vs. manual, distribution of approval latency).
- Integration approaches might shift as more customers adopt standardized IAM or workflow tooling.

### 9.2 Incremental approach

- Start with **low-regret controls** that provide strong value with limited UX impact (e.g., minimum dual authorization for transfers above a threshold, mandatory whitelists for withdrawals).
- Expand into **configurable matrices** for roles/assets/counterparties and more sophisticated workflows.
- Introduce **advanced analytics and anomaly detection** only once baseline controls and telemetry are stable.

### 9.3 "Good enough" criteria

- All institutional transactions above defined thresholds require dual authorization with independent approvers.
- No critical transactions (above a defined risk threshold) can be executed by a single user without additional approvals or emergency override procedures.
- Audit logs for approvals and policy evaluations are complete, searchable, and exportable for audits.

[Source: COSO Internal Control – Integrated Framework, COSO, 2013; Source: What Is the Four-Eyes Principle?, UNIDO, accessed 2025; Source: SOC 2® Trust Services Criteria, AICPA, 2018.]

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. **MPC alone is insufficient for institutions**: Without robust policy engines and role-based approvals, MPC wallets solve key theft but not insider fraud or governance deficiencies.
2. **Policy engines are now table stakes** for institutional MPC custodians, driven by regulatory expectations and competitive benchmarks.
3. A focused **policy engine MVP** is feasible within the stated constraints and can materially improve win rates and risk posture if scoped carefully and validated with customers.

### 10.2 Near-term action list (0–6 months)

Format: **[Priority] Action → Owner → Metric (baseline → target) → Date**

- **【P0 – Critical】**
  1. Define institutional policy primitives and data model → Product + Security + Compliance → Coverage of identified institutional use cases: 0% → ≥95% in spec → 2025-01-31.
  2. Design and implement policy engine MVP integrated with MPC signing and IAM → Backend Lead → High-risk institutional flows covered by policy engine: 0% → ≥80% → 2025-04-30.
  3. Implement tamper-evident audit logging for policy evaluations, approvals, and overrides → Platform Lead → Critical flows with full audit coverage: <30% → 100% → 2025-04-30.

- **【P1 – Important】**
  4. Build admin UI for policy configuration, simulation, and audit review → Frontend Lead → Time to configure a standard 4-eyes policy: ad-hoc/manual → <30 minutes → 2025-05-31.
  5. Integrate anomaly detection and alerts for suspicious approval patterns (e.g., repeated overrides, clustered high-value approvals) → Security Engineering → Mean time to detect anomalous approvals: days → <15 minutes → 2025-06-30.

- **【P2 – Optional/Next Wave】**
  6. Extend policies to cover advanced conditions (jurisdiction, risk scores, behavioral analytics) and out-of-the-box templates for regulated verticals → Product + Compliance → Customers using advanced policy templates: 0 → ≥10 institutional accounts → 2025-09-30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger | Mitigation | Owner |
|------|--------|-------------|---------|-----------|-------|
| Policy engine introduces significant latency or instability in signing flows | High | Medium | p95 latency >500 ms or elevated error rates post-rollout | Design with async approvals, caching of policy decisions, canary releases, and clear rollback plans | Backend Lead |
| Over-complex policy UI leads to misconfiguration and low adoption | Medium | Medium | Low usage of policy features; frequent misconfig incidents | Co-design with pilot customers, provide templates, validation checks, and clear defaults | Product + Frontend Lead |
| Incomplete mapping to SOC 2/ISO 27001 controls results in audit findings | High | Medium | Pre-audit review flags gaps in authorization or logging | Involve compliance/audit early; run external pre-assessments; align documentation and evidence collection | Compliance Lead |
| Customers bypass platform controls using off-platform wallets or manual workflows | Medium | Medium | High share of institutional volume remains outside the MPC platform | Offer migration support, integrations, and clear value (auditability, reduced friction) to incentivize full adoption | Sales + Customer Success |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A: Full policy engine (MVP→full)** | Strongest long-term differentiation; direct alignment with enterprise controls; clean audit story | High engineering complexity; requires ongoing maintenance and UX investment | Scope creep; latency regressions; misconfigurations | Platform has clear institutional focus and sufficient engineering capacity | Company strategy pivots away from institutional segment or has extremely constrained engineering budget |
| **B: Minimal controls + external approvals** | Faster time-to-market; lower implementation complexity | Relies on external tools; weaker audit trace; inconsistent UX | Customers may still see major gaps vs. competitors; harder to standardize | Customers already have strong approval tooling and accept integration-centric model | Target customers expect turnkey, on-platform institutional controls |
| **C: Hybrid (policy engine for high-risk flows)** | Balances effort and impact; focuses on highest-risk and highest-value flows | Requires segmentation of flows and some complexity in routing | Possible confusion about which flows are governed where; partial control coverage | Customer base is mixed (some simple, some complex) and engineering capacity is limited | Customer expectations demand uniform control coverage across all flows |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **MPC wallet** | Wallet where a private key is split into multiple shares and signing is performed via secure multi-party computation without reconstructing the full key | N/A | [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025] |
| **Policy engine** | Configurable rules system that evaluates each transaction against policies (e.g., roles, limits, whitelists, time windows) to determine whether it should be allowed and what approvals are required | N/A | [Source: Digital Asset Custody and Transaction Processing Leading Practices, Fireblocks, 2025] |
| **Four-eyes principle** | Internal control requirement that at least two independent people must review and approve a decision or transaction | N/A | [Source: What Is the Four-Eyes Principle?, UNIDO, accessed 2025] |
| **Dual authorization** | Specific implementation of the four-eyes principle requiring two or more authorized users to approve high-risk or high-value actions | N/A | [Source: What Is the Four-Eyes Principle That Regulated Companies Need to Adhere To?, MK Fintech Partners, 2024] |
| **Segregation of duties (SoD)** | Division of critical tasks among multiple people or roles so that no single individual can execute a complete high-risk process end-to-end | N/A | [Source: COSO Internal Control – Integrated Framework, COSO, 2013] |
| **Institutional controls** | Set of policies, processes, and technical mechanisms used by organizations to ensure authorized and auditable behavior for financial and operational activities | N/A | [Source: COSO Internal Control – Integrated Framework, COSO, 2013; Source: SOC 2® Trust Services Criteria, AICPA, 2018] |
| **IdP (Identity Provider)** | System that authenticates users and issues identity assertions used by applications to make access decisions (e.g., SAML, OIDC providers) | N/A | [Source: ISO/IEC 27001:2022, ISO, 2022] |
| **Whitelisting** | Allowing actions (e.g., withdrawals) only toward pre-approved destinations, with additional approvals required to modify the whitelist | N/A | [Source: Digital Asset Custody and Transaction Processing Leading Practices, Fireblocks, 2025] |
| **Approval latency** | Time between transaction initiation and final approval decision (including policy evaluation and human approvals) | ms / minutes / hours | [Estimate: Defined for institutional MPC wallets in this analysis, Medium confidence] |
| **Audit trail** | Tamper-evident record of all relevant events (policy evaluations, approvals, overrides, configuration changes) used for forensic analysis and compliance | N/A | [Source: SOC 2® Trust Services Criteria, AICPA, 2018; Source: ISO/IEC 27001:2022, ISO, 2022] |

---

## 12. References

### Tier 1 – Frameworks and Standards

1. **COSO.** (2013). *Internal Control – Integrated Framework*. Committee of Sponsoring Organizations of the Treadway Commission (COSO).  
   **[Cited in**: Context Recap; Sections 1–4, 5, 9–11 **]**
2. **AICPA.** (2018). *SOC 2® – Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy*. American Institute of CPAs (AICPA).  
   **[Cited in**: Context Recap; Sections 1–3, 5, 8, 9–11 **]**
3. **International Organization for Standardization.** (2022). *ISO/IEC 27001:2022 – Information Security, Cybersecurity and Privacy Protection – Information Security Management Systems*. ISO/IEC.  
   **[Cited in**: Context Recap; Sections 1–3, 5, 8, 9–11 **]**

### Tier 2 – Industry Reports and MPC Custody Guides

4. **Fireblocks.** (2025). *Digital Asset Custody and Transaction Processing Leading Practices Using Fireblocks’ MPC Solution*. Fireblocks.  
   **[Cited in**: Context Recap; Sections 1–3, 5–7, 10–11 **]**
5. **Fireblocks.** (2024). *Wallets-as-a-Service – Policy Engine Overview*. Fireblocks.  
   **[Cited in**: Sections 2–3, 5, 7, 10–11 **]**
6. **Stackup.** (2025). *MPC Wallets: A Complete Technical Guide*. Stackup. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide  
   **[Cited in**: Context Recap; Sections 1–2, 4–6, 10–11 **]**
7. **Safeheron.** (2025). *What Is an MPC Wallet and How Does It Work*. Safeheron. https://safeheron.com/blog/what-is-an-mpc-wallet-and-how-does-an-mpc-wallet-work  
   **[Cited in**: Context Recap; Sections 2, 4, 6, 11 **]**
8. **IOFinnet.** (2025). *MPC Custody Explained: Why It’s Essential in 2025*. IOFinnet.  
   **[Cited in**: Context Recap; Sections 1–3, 4–6, 10 **]**

### Tier 3 – Internal Controls and Four-Eyes Principle

9. **UNIDO.** (n.d.). *What Is the Four-Eyes Principle?* United Nations Industrial Development Organization (UNIDO). Retrieved 2025.  
   **[Cited in**: Context Recap; Sections 1–3, 9–11 **]**
10. **MK Fintech Partners.** (2024). *What Is the Four-Eyes Principle That Regulated Companies Need to Adhere To?* MK Fintech Partners Blog.  
    **[Cited in**: Context Recap; Sections 1–3, 10–11 **]**
11. **Trustpair.** (2024). *Is the Four Eyes Principle the Most Effective Way to Block Fraud?* Trustpair Blog.  
    **[Cited in**: Context Recap; Sections 1–3, 10 **]**

### Tier 3 – Internal & Estimates

12. **Problem Statement – Institutional Controls and Role-Based Approval for MPC Wallets.** (2025). Internal documentation summarizing problem statement, goals, constraints, stakeholders, and reference sources.  
    **[Cited in**: Context Recap; Sections 1–6, 7–10 **]**
13. **Estimates and assumptions.** Various.  
    Method: extrapolation from typical enterprise IAM and treasury system practices, MPC custody platform capabilities in public materials, and internal sales/win–loss data. Confidence: Medium. Validation: to be refined via prototypes, customer workshops, and audits.  
    **[Used in**: Context Recap; Sections 1–3, 5–8, 10–11 **]**
