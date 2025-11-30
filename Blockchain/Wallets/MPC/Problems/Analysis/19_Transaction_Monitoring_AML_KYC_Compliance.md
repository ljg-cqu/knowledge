# Transaction Monitoring AML/KYC Compliance Requirements for MPC Wallets – Nine-Aspects Analysis

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Compliance & Regulatory Analysis Team  
**Related Problem**: `../19_Transaction_Monitoring_AML_KYC_Compliance.md`

---

## Context Recap

- **Problem title**: Transaction Monitoring AML/KYC Compliance Requirements for MPC Wallets
- **Current state**:
  - Global regulators (EU, US, UK, FATF members) are tightening AML/KYC expectations for crypto platforms, explicitly including MPC wallet providers as VASPs that must implement CDD, transaction monitoring, Travel Rule, SAR processes, and long-term audit trails [Source: FATF Guidance on Virtual Assets and VASPs, FATF, 2019; EU MiCA Regulation, 2023/2025].
  - Many MPC wallets were designed as "non-custodial" with minimal identity collection and limited monitoring, creating a structural gap vs. new expectations [Source: "Multi-Party Computation (MPC) Wallets and the Evolving Regulatory Landscape in the United States", S. Horowitz, 2024].
  - Compliance platform vendors (Chainalysis, Elliptic, TRM Labs, CipherTrace, Notabene, Sygna) offer transaction monitoring and Travel Rule services, but integration with distributed MPC key architectures and multi-chain support remains incomplete and costly [Source: Chainalysis Exchange Compliance Guide, Chainalysis, 2024; TRM Labs product documentation, TRM Labs, 2024].
- **Pain points** (quantified where possible):
  - **Latency & UX**: Adding real-time sanctions screening and behavioral analytics introduces ~200–500 ms per transaction, pushing total perceived approval time toward or beyond the <3 s user tolerance when combined with MPC signing (2–15 s in some implementations) [Estimate based on: screening against 10k+ sanctions entries + ML scoring latency, Medium confidence].
  - **Privacy vs. transparency**: Regulators require observability into suspicious flows and counterparty identities, while privacy-focused MPC architectures and users expect minimal data centralization and no broad surveillance [Source: FATF Guidance, FATF, 2019; RIF Technology onboarding barriers report, RIF Technology, 2024].
  - **Cross-jurisdiction complexity**: A single MPC wallet may serve users across US, EU, UK, and other regions, each with different thresholds (e.g., $3k/€1k/£1k Travel Rule triggers), reporting obligations, and data residency rules [Source: "Maintaining KYC, AML & CTF Compliance across Multiple Jurisdictions for Crypto Firms", KYC Chain, 2024].
  - **Retroactive KYC burden**: Tens of millions of legacy users must be upgraded to stronger KYC or risk suspension; historical campaigns at major exchanges triggered user backlash and churn [Source: Case summaries in KYC Chain, 2024; major exchange public notices, 2021–2023].
- **Goals**:
  - Achieve full AML/KYC and Travel Rule compliance in priority jurisdictions (EU MiCA by Q3 2025; US FinCEN; UK MLR 2024), while:
    - Maintaining end-to-end transaction approval within ~3 s in user perception for typical retail flows.
    - Keeping false positive rates near 1–3% and false negatives sufficiently low to satisfy regulators and banking partners [Source: Vendor performance ranges in Chainalysis / Elliptic / TRM Labs marketing materials, 2023–2024].
    - Keeping per-transaction compliance cost at or below ~$0.02 (target) and ideally <$0.01 for scalability to small-value payments.
- **Hard constraints**:
  - EU MiCA goes live Q3 2025 with enforcement powers (license suspension, fines up to 5% of annual turnover or €5M, whichever is higher) [Source: EU MiCA Regulation text, EU, 2023].
  - FinCEN Travel Rule enforcement is active; non-compliance can be fined $25k–$100k per violation [Source: FinCEN Travel Rule guidance, FinCEN, 2020].
  - Data protection and residency rules (GDPR in EU, local storage rules in several jurisdictions) restrict where identity and transaction data can be stored and processed [Source: GDPR Regulation (EU) 2016/679].
  - MPC architecture decisions (thresholds, key share locations, custody models) are not easily changed within months without large engineering refactors.
- **Key facts from input**:
  - ~50+ MPC wallet providers, 200M+ users, $500B+ annual volume, with <50% currently operating comprehensive monitoring and Travel Rule support.
  - Sanctions lists comprise 10k+ OFAC entries, 1k+ UN entries, ~1.5k+ EU entries, updated frequently.
  - False positive rates of tuned systems generally in the 1–5% range; higher rates are operationally and commercially unacceptable.

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

- **Core problem**: How can MPC wallet providers implement robust, real-time transaction monitoring, AML, and KYC/Travel Rule controls by end of 2025 across multiple jurisdictions **without** breaking MPC performance, privacy promises, or economic viability?
- **Key contradictions**:
  - **Compliance observability vs. user privacy**: Regulators expect granular visibility into counterparties, flows, and suspicious patterns, while MPC architectures are marketed as trust-minimized and privacy-preserving with distributed key shares and minimized central data stores [Source: "MPC Wallet as a Service: Revolutionizing Digital Asset Security", Vocal Media, 2024].
  - **Real-time monitoring vs. latency/throughput**: Sanctions checks, Travel Rule lookups, and behavioral scoring must run synchronously or near-synchronously with MPC signing, yet institutional traders and end users expect sub-second or few-second approvals.
  - **Global standardization vs. jurisdictional divergence**: FATF provides high-level recommendations, but MiCA, FinCEN, FCA, MAS, and others interpret and implement them differently, leading to inconsistent thresholds, data fields, and reporting pipelines [Source: FATF VASP guidance, FATF, 2019; KYC Chain, 2024].
  - **Retroactive fixes vs. user tolerance**: Forcing existing users through intensive KYC and Travel Rule disclosures in a compressed timeframe risks significant churn, negative publicity, and migration to non-compliant offshore alternatives.

### 1.2 Goals & conditions

- **Regulatory outcomes**:
  - Reach 100% coverage of MiCA AML/KYC requirements by Q3 2025 and key US/UK expectations by Q4 2025.
  - Achieve near-100% Travel Rule coverage for eligible transactions (≥$3k/€1k/£1k) between participating VASPs.
- **Operational and UX outcomes**:
  - Maintain typical transaction experience so that **perceived** delay added by compliance is ≤500 ms for mainstream flows (sanctions-only, low-risk heuristics), with heavier behavioral analytics possibly running asynchronously post-authorization, where safe.
  - Achieve ≥95% KYC completion among active users by Q4 2025 via staged campaigns and just-in-time verification triggers.
  - Keep false positives close to 1–3% and design workflows to resolve them within hours, not days, for legitimate users.
- **Economic constraints**:
  - Total compliance platform + engineering + operations spend per provider roughly $500k–$2M over the first year, with per-transaction marginal cost below ~$0.02 at steady state.

### 1.3 Extensibility & reframing

- **Reframing 1 – From "compliance layer" to "risk orchestration fabric"**:
  - View compliance not as a blocking bolt-on, but as a **risk orchestration fabric** integrated at multiple stages: onboarding, pre-transaction risk scoring, in-flight screening, and post-trade surveillance.
  - This enables load-shedding (more expensive checks only when risk justified) and decouples some monitoring from strict real-time paths.
- **Reframing 2 – From "central identity registry" to "selective disclosure and attestations"**:
  - Instead of a single global identity DB, use **attested attributes** (e.g., KYC level, risk band, jurisdiction) plus selective disclosure to regulators or counterparties when thresholds are crossed.
  - Zero-knowledge or selective disclosure proofs can be layered gradually as technology and regulatory comfort evolve [Source: Regulatory compliance of multi-chain wallet tracking solutions, Mondaq, 2024].
- **Reframing 3 – From "one-size global product" to "jurisdiction-aware products"**:
  - Accept that feature sets and data flows will differ by jurisdiction or user profile; implement a dynamic policy engine that configures screening, Travel Rule data, and storage locations per region.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Core functional components**:
  - MPC orchestration and signing services.
  - KYC onboarding and lifecycle management (documents, liveness, ongoing monitoring).
  - Transaction monitoring engine (sanctions lists, address risk scores, behavioral analytics).
  - Travel Rule gateway (inter-VASP identity data exchange protocols like TRISA, TRP, OpenVASP).
  - Policy and rules engine (per jurisdiction, per product, per risk tier).
  - Case management and SAR pipeline for compliance analysts.
- **Data flows**:
  - User identity data ↔ KYC provider ↔ wallet account metadata.
  - On-chain transaction data ↔ blockchain analytics platforms ↔ risk scores.
  - VASP↔VASP Travel Rule messages ↔ chain transactions.

### 2.2 Balance & "degree" issues

- **Detection sensitivity vs. false positives**:
  - Aggressive thresholds reduce missed suspicious activity but drive false positive rates upwards, overwhelming compliance teams and frustrating legitimate users.
  - Balanced tuning requires continuous calibration using case resolutions and regulator feedback.
- **Synchronous vs. asynchronous checks**:
  - If all heavy analytics run before signature, latency explodes; if too much is deferred, risk of executing and later freezing legitimate user funds or missing fast-moving laundering patterns increases.
- **Centralization vs. decentralization of data**:
  - Centralizing KYC and monitoring data simplifies analytics and reporting but increases breach risk and undermines privacy promises.
  - Excessive decentralization (e.g., local-only storage per jurisdiction) complicates global risk detection and auditability.

### 2.3 Causal chains

- **Chain A – Weak KYC → Compliance gaps → Enforcement risk**:
  - Minimal onboarding checks → High share of pseudonymous high-risk users → Elevated exposure to sanctioned entities and mixers → Detection failures or late detection → Regulatory penalties, banking partner de-risking, and potential license suspension.
- **Chain B – Overly strict rules → False positives → Churn**:
  - Extremely low tolerance thresholds + poorly tuned models → 3–10% of legitimate transactions blocked or delayed → Exploding support queues, slow case closure → User abandonment and migration to competitors or to unregulated alternatives [Source: Vendor false-positive ranges summarized in Chainalysis and TRM Labs reports, 2023–2024].
- **Chain C – Architecture misalignment → Cost & timeline blowup**:
  - Ignoring MPC-specific constraints in initial compliance design → Needing deep rework of signing flows, data schemas, and key distribution → Project delays that miss MiCA and Travel Rule deadlines → Forced emergency measures and higher integration cost.

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholder matrix

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| **Upstream – Regulators & Standard Setters** | FATF, EU authorities, FinCEN, FCA, others | Reduce money laundering / terrorism financing; ensure traceability | Limited technical bandwidth; older frameworks built for custodial banking | May over-apply custodial assumptions to MPC/self-custodial models |
| **Upstream – Banking Partners** | Correspondent banks, payment rails | Comfort that crypto flows meet AML standards; low SAR noise | Low risk appetite; pressure from supervisors | May refuse relationships with perceived non-compliant MPC providers |
| **Downstream – MPC Wallet Providers** | Build and operate wallets & APIs | Maintain licenses; grow user base; minimize cost & latency | Limited compliance engineering capacity; budget caps | Tension between regulatory expectations and product UX/positioning |
| **Downstream – End Users (Verified)** | Retail/institutional users willing to KYC | Fast, reliable, trusted service with minimal friction | Data protection expectations; limited patience for delays | Can switch providers if compliance UX is bad |
| **Downstream – End Users (Privacy-focused)** | Users who chose MPC for privacy/self-custody | Minimize identity disclosure; avoid surveillance | Growing regulatory pressure; offboarding risk to unregulated venues | Strong resistance to expanded KYC/monitoring; may churn |
| **Sideline – Compliance Vendors** | Chainalysis, Elliptic, TRM Labs, CipherTrace, Notabene, Sygna | Sell SaaS products and integrations; high detection performance | Must adapt products to MPC and multi-chain contexts | Lock-in vs. interoperability tension with providers |
| **Sideline – Privacy Advocates & Civil Society** | EFF, Coin Center, NGOs | Prevent overbroad surveillance and data collection | Limited influence on detailed regulation drafting | Can create reputational risk if solutions over-collect data |

### 3.2 Environment: policy, markets, tech

- **Policy**: Rapid convergence on FATF-style virtual asset rules, but with uneven enforcement and different thresholds. MiCA is a strong driver in the EU; the US relies on BSA/FinCEN rules, and the UK via Money Laundering Regulations [Source: FATF, 2019; EU MiCA, 2023; UK MLR 2024].
- **Market**: Institutional adoption of MPC custody is rising, making robust compliance a prerequisite for bank partnerships and large clients.
- **Technology**: Ongoing improvements in blockchain analytics, graph-based risk scoring, and privacy-preserving techniques (e.g., zero-knowledge proofs, secure enclaves) create space for more nuanced solutions.

### 3.3 Responsibility & room for maneuver

- **Where MPC providers must comply strictly**:
  - Implementing sanctions screening, Travel Rule support, KYC procedures, SAR filings in alignment with local rules.
  - Maintaining verifiable audit trails and cooperating with law enforcement when legally obliged.
- **Where providers have design flexibility**:
  - Distribution of checks across pre/on/post-transaction stages.
  - Selection of vendors vs. in-house build, and model architectures.
  - Degree of centralization of personal data, subject to satisfying regulators.
  - Experience design for KYC flows (e.g., just-in-time KYC, risk-tiered flows).

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2017–2020: Exchange-first compliance**
   - Major centralized exchanges implemented basic KYC and sanctions checks but limited behavioral analytics; MPC wallets were niche and treated as more "self-custodial" [Source: Chainalysis compliance overview, 2020–2021].
2. **2019–2021: FATF Travel Rule & VASP classification**
   - FATF clarified that many virtual asset services, including wallet-as-a-service providers, fall under VASP definitions and should implement AML/KYC/Travel Rule requirements [Source: FATF Guidance, 2019].
3. **2021–2023: Regulatory clarification and early enforcement**
   - More jurisdictions interpreted MPC custodial and WaaS models as subject to regulation; institutions demanded higher assurance for crypto custody and transfer.
4. **2023–2025: MiCA and global tightening**
   - EU MiCA finalization and implementation, plus increased emphasis from regulators and banks on standardized AML controls for all crypto intermediaries, including MPC.

### 4.2 Background vs. direct causes

- **Background causes**:
  - Crypto culture of pseudonymity and minimal identity collection.
  - Fragmented and fast-evolving regulatory landscape with lagging guidance for non-traditional architectures.
  - Rapid proliferation of chains, assets, and cross-chain bridges, complicating risk visibility.
- **Direct triggers**:
  - MiCA enforcement timelines and similar national legislation.
  - Banking partners and institutional clients making comprehensive monitoring and Travel Rule support contractual preconditions.
  - Publicized enforcement actions against non-compliant crypto firms, raising perceived risk.

### 4.3 Root issues

- Regulatory frameworks were written primarily for **centralized custodians**, not distributed MPC architectures and self-custodial models.
- Many MPC providers optimized for **security and UX** ahead of compliance, leading to architectures that now require retrofitting.
- Industry fragmentation in Travel Rule protocols and monitoring tools led to **interoperability gaps** and inconsistent implementations.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory

- Without significant investment and architectural changes, a material portion of MPC providers will **miss MiCA and enhanced Travel Rule expectations**, risking license suspensions or losing access to key markets and banking partners.
- Transaction monitoring coverage and quality are improving overall as more providers integrate top-tier vendors, but many deployments remain in early stages or operate with suboptimal tuning.
- Privacy-preserving compliance techniques (e.g., selective disclosure, zero-knowledge proofs) are maturing in research and early pilots but are not yet widely adopted in production [Source: Regulatory compliance of multi-chain tracking solutions, Mondaq, 2024].

### 5.2 Early signals

- **Supervisory statements** from EU, UK, and US bodies explicitly mentioning crypto-asset service providers and Travel Rule enforcement.
- Increased due diligence by banks on crypto clients’ AML programs, including detailed questionnaires about monitoring coverage and Travel Rule interoperability.
- Growing number of high-profile enforcement actions and settlements related to AML deficiencies in crypto.

### 5.3 Scenarios (6–24 months)

- **Optimistic**:
  - MPC providers adopt modular compliance architectures with strong vendor integrations, jurisdiction-aware policy engines, and risk-tiered monitoring.
  - Regulators show flexibility around privacy-preserving techniques and recognize selective disclosure schemes.
  - Result: most providers achieve compliance with manageable cost and modest UX impact; MPC becomes a trusted institutional-grade option.
- **Baseline**:
  - Majority achieve minimal viable compliance using vendor solutions; some architectural friction and elevated false positives persist.
  - A subset of smaller providers struggle with budgets/timelines, exit regulated markets, or focus on less regulated jurisdictions.
- **Pessimistic**:
  - Several high-profile enforcement actions targeting MPC-based services create a chilling effect.
  - Fragmented Travel Rule ecosystems fail to interoperate, causing frequent transaction failures and user frustration.
  - Privacy uproar emerges if implementations centralize large identity databases, driving privacy-focused users to unregulated venues.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Cryptography and infrastructure expertise** in MPC firms is generally high; teams can design secure distributed protocols, key management, and fault-tolerant services.
- Many providers already operate **high-availability, low-latency infrastructure** across multiple regions, giving them a base to host monitoring and Travel Rule services.
- Some large providers have **existing relationships with top-tier compliance vendors** and banking partners, which can be expanded.

### 6.2 Capability gaps

- **Compliance engineering**: Integrating sanctions, behavioral analytics, Travel Rule, and case management into MPC flows requires domain specialists and engineering capacity many teams lack.
- **Regulatory interpretation and policy design**: Translating MiCA, BSA/FinCEN, FCA, and other texts into concrete policies, rules, and audit trails is non-trivial.
- **Data science and model governance**: Tuning AML models, monitoring drift, and explaining decisions to regulators needs skills beyond traditional backend development.

### 6.3 Buildable capabilities (1–6 months)

- **Short term (0–3 months)**:
  - Hire or contract 1–2 senior compliance engineers and a regulatory specialist.
  - Integrate a leading transaction monitoring API in a limited-scope pilot (e.g., for specific chains or jurisdictions).
- **Medium term (3–6 months)**:
  - Build a **central policy engine** that routes transactions to appropriate checks depending on user risk, jurisdiction, asset type, and amount.
  - Stand up a basic **Travel Rule gateway** using an established protocol (TRISA/OpenVASP) and connect with a handful of counterparties.
  - Implement regular calibration and model performance review routines involving compliance and data experts.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Rapid regulatory tightening for crypto AML/KYC/Travel Rule and inclusion of MPC-based services.
- **Problem**: Balancing monitoring depth, performance, privacy, and cost under 2025 deadlines.
- **Analysis**:
  - Internal and external constraints; contradictions (Sections 1–3).
  - Historical causes and forward trends (Sections 4–5).
  - Capability assessment and validation needs (Sections 6 & 8).
- **Options**:
  - Vendor-first modular approach vs. in-house heavy build; centralized vs. selective-disclosure data architectures; jurisdictional product segmentation.
- **Risks and mitigation**:
  - Non-compliance, false positives/negatives, vendor lock-in, privacy backlash.

### 7.2 Key judgments (prioritized)

1. **【P0】MPC wallets will be treated as VASPs in major jurisdictions and must meet full AML/KYC obligations**, not lighter self-custodial regimes.
2. **【P0】A vendor-first modular approach is the fastest viable path to 2025 compliance** for most providers, with optional gradual in-house build-out.
3. **【P1】Selective disclosure and attribute-based identity models will become increasingly acceptable**, but near-term implementations will still require significant data collection and retention.
4. **【P1】Without strong policy engines and risk-tiering, either latency or false positives will become prohibitive**, undermining competitive viability.
5. **【P2】Providers that over-index on privacy at the expense of regulation will be pushed to the regulatory periphery** (offshore, restricted banking access).

### 7.3 Alternative paths (high-level)

- **Option A – Vendor-centric, modular compliance layer**:
  - Use best-of-breed SaaS for monitoring, Travel Rule, and case management; focus internal work on integration, policy engines, and UX.
- **Option B – Heavily in-house compliance stack**:
  - Build analytics, monitoring, and Travel Rule components internally for maximum control and differentiation.
- **Option C – Jurisdictional segmentation and partial retreat**:
  - Fully comply in core markets; de-prioritize or withdraw from jurisdictions where requirements conflict irreconcilably with product ethos.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Tech-centric optimism**: Overestimating speed at which zero-knowledge or advanced privacy-preserving techniques will be regulator-accepted.
- **Vendor bias**: Assuming vendor solutions will perform as advertised without considering edge cases, integration overhead, or lock-in.
- **Conservatism**: Risk of over-engineering compliance controls beyond what is required, harming UX and cost competitiveness.

### 8.2 Required intelligence and data

- **Detection metrics**:
  - Current and target true positive and false positive rates by segment.
  - Case handling times and backlog metrics.
- **Latency and UX metrics**:
  - End-to-end timing distributions with and without compliance checks for typical flows.
- **Regulatory expectations**:
  - Concrete supervisory statements or feedback from leading regulators regarding MPC-specific architectures and selective disclosure schemes.
- **Travel Rule interoperability**:
  - Real-world success/failure rates for counterparty data exchange via chosen protocol(s).

### 8.3 Validation plan

- **Step 1 – Pilot integration**:
  - Integrate a leading monitoring vendor and Travel Rule provider for a subset of chains and a single region.
  - Measure latency, detection rates, and user impact over 4–8 weeks.
- **Step 2 – Tuning and calibration**:
  - Use case outcomes and SAR statistics to adjust thresholds and rules; document rationale.
- **Step 3 – Regulator/banking feedback loop**:
  - Share architecture and pilot outcomes with regulators and key banking partners; collect feedback and adjust design.
- **Step 4 – Scale-out with feature flags**:
  - Gradually expand coverage to additional jurisdictions/assets while monitoring KPIs and user complaints.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- **Thresholds and coverage** will be adjusted as regulators refine interpretations (e.g., Travel Rule amounts, scope of VASP definitions for certain self-custodial features).
- **Data retention and access policies** may need tightening if data breaches or privacy controversies occur.
- **Architecture choices** may evolve as selective disclosure or ZK-based compliance proofs mature and gain regulatory acceptance.

### 9.2 Incremental approach vs. big-bang

- Prefer **incremental rollout**:
  - Start with sanctions screening + simple rules synchronously, then gradually integrate more advanced analytics.
  - Start with the highest-risk corridors (e.g., fiat on/off ramps, large institutional transfers) before expanding to all flows.
  - Use regional toggles and feature flags to enable quick rollback if issues arise.

### 9.3 "Good enough" criteria

- **Regulatory**: No major findings or enforcement actions in early supervisory reviews; satisfactory audit of monitoring and Travel Rule.
- **Operational**: Stable false positive rates in the 1–3% band with manageable case workload.
- **UX**: >90% of transactions complete within user-tolerable latency targets; support tickets about compliance friction remain a small share of total tickets.
- **Security & privacy**: No severe data breaches; privacy impact assessments accepted by regulators.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. **Compliance expectations for MPC wallets are converging toward those for traditional custodial VASPs**, with no broad exemptions for distributed key architectures.
2. **The main challenge is not whether to comply but how to engineer monitoring, KYC, and Travel Rule into MPC flows** without destroying latency, privacy guarantees, or economic viability.
3. **Vendor-centric, modular architectures with jurisdiction-aware policy engines are the most pragmatic near-term path** to 2025 deadlines, while leaving room for later refinement and partial in-house build.
4. **Risk-tiered checks and careful threshold tuning are essential** to avoid either missing suspicious activity or over-blocking legitimate users.
5. **Incremental rollout with continuous validation, regulator engagement, and user feedback** is more robust than a single big-bang compliance release.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric (baseline → target) → Date**

1. **【P0】Design target-state compliance architecture and policy engine** → Head of Engineering + Head of Compliance → Completion of architecture document reviewed by legal/regulatory advisors (0 → 1) → within 4 weeks.
2. **【P0】Select and contract primary transaction monitoring and Travel Rule vendors** → Compliance Lead → Signed contracts with vendors meeting coverage and SLA requirements (0 → 2) → within 6 weeks.
3. **【P0】Implement pilot sanctions + basic behavioral screening on priority chains/regions** → Compliance Engineering Team → % of transactions through pilot paths (0% → ≥10%) and additional latency (<500 ms) → within 10 weeks.
4. **【P1】Roll out risk-tiered KYC and transaction limits** → Product + Compliance → Share of users with completed KYC (current baseline → target +20 percentage points) → within 12 weeks.
5. **【P1】Implement foundational Travel Rule messaging for high-value transfers** → Compliance Engineering → Share of eligible transfers with successful Travel Rule exchange (0% → ≥70%) → within 12 weeks.
6. **【P2】Prototype selective disclosure / ZK-based compliance proof for one use case** → Research Team → Existence of demo validated by internal legal/compliance (0 → 1 prototype) → within 3–6 months.

### 10.3 Key risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Missing MiCA or Travel Rule deadlines | High | Medium | Slippage in integration milestones; vendor delays | Early, conservative planning; multiple vendor options; regular steering with execs | Head of Compliance |
| Excessive false positives causing churn | High | Medium | False positive rate >5%; surge in blocked legitimate transactions | Continuous model tuning; risk-tiering; user-friendly review and appeal flows | Compliance Engineering Lead |
| Vendor lock-in and cost escalation | Medium | Medium | Single-vendor dependency; sharp price increases | Multi-vendor architecture; open standards; periodic RFPs | CTO |
| Privacy backlash or data breach | High | Low–Medium | Central KYC/monitoring DB compromised; broad data sharing | Strong security controls; data minimization; privacy-by-design reviews; incident response playbooks | CISO |
| Incomplete Travel Rule interoperability | Medium | Medium–High | High failure rate in counterparty data exchange | Support multiple protocols; prioritize counterparties implementing compatible solutions; monitoring and fallback procedures | Compliance Lead |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Vendor-centric, modular stack** | Fastest path to coverage; leverages mature analytics; easier to satisfy regulators with recognized vendors | Recurring SaaS fees; integration complexity; potential lock-in | Over-reliance on vendor roadmaps; limited customization | Tight timelines (MiCA 2025); limited internal compliance engineering capacity | When long-term differentiation requires deep, bespoke analytics or ultra-low per-tx cost |
| **B. Heavy in-house build** | Maximum control; potential long-term cost savings; deep product-compliance integration | High upfront investment in talent, infra, and validation; slower time-to-market | Missing deadlines; weaker early detection performance; difficulty convincing regulators | Large providers with strong data science teams and multi-year runway | Smaller providers with limited budget or urgent deadlines |
| **C. Jurisdictional segmentation / partial retreat** | Allows focus on markets where compliance fit and economics are strongest; reduces burden of most complex regimes | Lost revenue and users in excluded jurisdictions; reputational questions | Perception of regulatory arbitrage; future re-entry may be difficult | When product ethos conflicts with certain regulations; when certain markets are low-revenue but high-complexity | When excluded jurisdictions are strategically critical or drive institutional adoption |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **AML (Anti-Money Laundering)** | Legal and regulatory framework requiring financial institutions and VASPs to detect, prevent, and report suspicious activity related to money laundering and financial crime | N/A | FATF Recommendations and national AML laws |
| **CDD (Customer Due Diligence)** | Processes to identify and verify customers and assess risk, often including document checks, source-of-funds, and ongoing monitoring | N/A | FATF and MiCA customer due diligence requirements |
| **CTF (Counter-Terrorism Financing)** | Legal framework to prevent and disrupt financing of terrorism, overlapping with AML but with distinct obligations | N/A | FATF Recommendations; national CTF legislation |
| **FATF Travel Rule** | Recommendation that VASPs transmit originator and beneficiary information for qualifying virtual asset transfers above specified thresholds | Typical thresholds: ~$1k/€1k; national rules vary | FATF Guidance on Virtual Assets and VASPs, 2019 |
| **KYC (Know Your Customer)** | Identity verification and risk assessment process required for customers of financial institutions and VASPs | N/A | Core component of AML/CTF programs |
| **MiCA (Markets in Crypto-Assets)** | EU regulatory framework governing crypto-asset service providers, including AML, KYC, and Travel Rule obligations | Effective Q3 2025 in EU | EU Regulation (EU) 2023/1114 (MiCA) |
| **MPC (Multi-Party Computation) Wallet** | Wallet architecture where private keys are split across multiple parties or devices, and signatures are generated collaboratively without reconstructing the key | N/A | Security and compliance architecture for custody and wallets |
| **p95 latency** | 95th percentile of observed latency distribution; 95% of operations complete within this time | Milliseconds (ms) or seconds (s) | Used to measure impact of compliance checks on UX |
| **Sanctions screening** | Real-time or near-real-time comparison of counterparties against official sanctions and watch lists (e.g., OFAC, UN, EU) | N/A | Required AML control for VASPs and banks |
| **SAR (Suspicious Activity Report)** | Report filed to a Financial Intelligence Unit when a transaction or pattern appears linked to money laundering, terrorism financing, or other crime | N/A | Mandatory reporting obligation in AML frameworks |
| **Selective disclosure** | Technique that reveals only necessary compliance-relevant information (attributes, proofs) to specific parties (e.g., regulators) while keeping broader data private | N/A | Emerging design pattern for privacy-preserving compliance |
| **VASP (Virtual Asset Service Provider)** | Entity that conducts exchange, transfer, safekeeping, or administration of virtual assets on behalf of others, subject to AML/CTF rules | N/A | Defined by FATF and transposed into national laws |

---

## 12. References

### Tier 1 – Regulatory and Official Sources

1. **FATF**. (2019). *Guidance for a Risk-Based Approach to Virtual Assets and Virtual Asset Service Providers*. Financial Action Task Force. https://www.fatf-gafi.org/  
2. **European Union**. (2023). *Regulation (EU) 2023/1114 on Markets in Crypto-Assets (MiCA)*. Official Journal of the European Union.  
3. **FinCEN**. (2020). *Application of FinCEN's Regulations to Certain Business Models Involving Convertible Virtual Currencies (Travel Rule Guidance)*. Financial Crimes Enforcement Network.  
4. **UK Government / FCA**. (2024). *Money Laundering Regulations 2024 and Cryptoasset Guidance*.  
5. **European Union**. (2016). *General Data Protection Regulation (GDPR) – Regulation (EU) 2016/679*.

### Tier 2 – Industry Reports, Legal and Technical Analyses

6. **Silent Eight**. (2025). *2025 Trends in AML and Financial Crime Compliance: A Data-Centric Perspective and Deep Dive into Transaction Monitoring*. Silent Eight.  
7. **KYC Chain**. (2024). *Maintaining KYC, AML & CTF Compliance across Multiple Jurisdictions for Crypto Firms*. https://kyc-chain.com/  
8. **Vocal Media**. (2024). *MPC Wallet as a Service: Revolutionizing Digital Asset Security*. Vocal Media.  
9. **Chainalysis**. (2024). *Introduction to Cryptocurrency Exchange Compliance: Crypto Businesses 2024*. Chainalysis.  
10. **TRM Labs**. (2024). *Banking on Stablecoins: A Risk Mitigation Blueprint for Financial Institutions*. TRM Labs.  
11. **S. Horowitz & Co.**. (2024). *Multi-Party Computation (MPC) Wallets and the Evolving Regulatory Landscape in the United States*. S. Horowitz.  
12. **Mondaq**. (2024). *Regulatory Compliance of Multi-Chain Wallet Tracking Solutions: Navigating AML/KYC in a Cross-Chain World*. Mondaq.  
13. **Debut Infotech**. (2024). *What is Anti-Money Laundering (AML) in Cryptocurrency?* Debut Infotech.  
14. **RIF Technology**. (2024). *Usability and Difficult Onboarding are Major Entry Barriers for Crypto Users: Research Finds*. RIF Technology.

### Internal / Derived Estimates and Assumptions

15. **Screening and latency estimates**. Method: approximate database lookups against 10k+ sanctions entries and ML scoring for transaction monitoring, calibrated with public vendor benchmarks (Chainalysis, TRM Labs, Elliptic, CipherTrace). Confidence: Medium. Validation: performance measurement in pilot integrations over 4–8 weeks.  
16. **Volume and user base estimates for MPC wallets**. Method: extrapolation from public user and AUM figures for major exchanges and MPC providers plus analyst reports. Confidence: Medium. Validation: cross-check with vendor and industry disclosures.
