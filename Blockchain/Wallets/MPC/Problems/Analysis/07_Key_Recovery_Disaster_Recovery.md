# Key Recovery and Disaster Recovery Complexity in MPC Wallets — Nine-Aspects Problem Analysis

## Pre-Section: Context Recap

- **Problem title**: Key Recovery and Disaster Recovery Complexity in MPC Wallets
- **Current state**:
  - Institutional and enterprise users are increasingly adopting MPC wallets that distribute private key shares across multiple parties (e.g., 2-of-3, 3-of-5) so that a full private key never materializes in one place. [Source (from problem statement): "MPC Wallets: A Complete Technical Guide", Stackup, 2024, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide]
  - Disaster recovery remains fragile: loss or inaccessibility of a subset of distributed key shares (hardware failures, cloud outages, employee departures, regional disasters) can render assets effectively unrecoverable if backup design and procedures are weak.
  - Unlike traditional seed-phrase wallets, there is no simple "write 24 words on steel" backup; instead, providers rely on redundancy, third-party recovery services, geographically distributed backup shares, or social recovery designs, all of which add trust and operational complexity. [Source (from problem statement): CoinCover blog "Why Disaster Recovery for private keys is essential", 2023, https://www.coincover.com/blog/why-disaster-recovery-for-private-keys-is-essential]
- **Pain points**:
  - Recovery times of 3–7 days for complex MPC deployments versus regulatory expectations of 24–48h Recovery Time Objective (RTO) for regulated custody. [Source (from problem statement): CoinCover blog, 2023]
  - Non-trivial probability of permanent asset loss when multiple shares become inaccessible or when recovery procedures fail in practice, contributing to industry-wide losses linked to private key compromise and loss. [Source (from problem statement): Chainalysis "Crypto Crime Report 2025", 2025]
  - Operational stress and coordination burden across multiple infrastructure teams, third-party vendors, and compliance stakeholders during disaster events.
- **Goals**:
  - Reduce RTO to ≤24h (minimum), with 12h (target) and 4h (ideal) for institutional MPC wallet recovery.
  - Achieve 100% recovery success for supported disaster classes (no permanent asset loss due purely to share unavailability), while maintaining MPC security guarantees (no cleartext private key exposure).
  - Reduce human coordination overhead and third-party trust dependencies, and ensure regulatory compliance is demonstrable to auditors.
- **Hard constraints**:
  - The full private key must never be materialized during backup or recovery; all operations must respect MPC and/or threshold cryptography security models. [Source: Cobo Docs "Disaster Recovery | Cobo MPC Co-Managed Custody", accessed 2025, https://docs.cobo.com]
  - Budget envelope of roughly $500K–$1.5M per major provider for design, deployment, and operation of robust recovery infrastructure over the next 9–12 months.
  - Backward compatibility with existing MPC schemes and key ceremonies (e.g., Shamir Secret Sharing, GG20/CGGMP-style protocols) already deployed in production. [Source: Stackup technical guide, 2024]
- **Key facts (from problem statement)**:
  - 43.8% of $2.2B crypto theft in 2024 is attributed to private key compromises, including failures during recovery procedures. [Source (from problem statement): Chainalysis "Crypto Crime Report 2025", 2025]
  - Backup and geographic distribution strategies typically add 10–15% to operational budgets for custodians. [Source (from problem statement): CoinCover blog, 2023]
  - Many institutional custody providers cannot yet demonstrate 24–48h MPC recovery capability to regulators in a repeatable, auditable way.

---

## 1. Problem Definition (Aspect 1) — Clarity & Precision 【Core】

### 1.1 Problem & Contradictions

- **Core contradiction**:
  - MPC wallets are designed to *eliminate* single-point-of-failure keys by distributing shares, but this very distribution makes **recovery** harder when multiple shares are lost or inaccessible.
  - Security and decentralization push for more independent parties and jurisdictions, while operational resilience and RTO demands push for fast, centralized coordination and clear runbooks.
- **Key conflicts**:
  - **Security vs. Recoverability**: Fewer backup copies and tighter controls ↓ attack surface but ↑ chance of unrecoverable loss; more redundancy and backup channels ↑ survivability but ↑ attack surface and complexity. [Source: Blockworks "MPC Wallets Have a Trade Off. Is It Worth It?", 2023, https://blockworks.co/news/mpc-wallets-security]
  - **Decentralization vs. Operational Control**: Multi-party, multi-region MPC is harder to orchestrate quickly during emergencies than single-operator HSM-based custody, but regulators still expect bank-grade DR behavior.
  - **Trusted-third-party avoidance vs. Practicality**: Many users adopted MPC to avoid trusting one central custodian, yet third-party recovery services reintroduce exactly such trust anchors. [Source: Cobo blog "Cobo Expands MPC Key Recovery Partnership with Nemean Services", 2024, https://www.cobo.com/post/cobo-expands-mpc-key-recovery-partnership-with-nemean-services]

### 1.2 Goals & Conditions

- **Primary goals (quantified)**:
  - RTO: 3–7 days → **≤24h (min) / ≤12h (target) / ≤4h (ideal)** for MPC wallet recovery across major disaster scenarios.
  - Recovery success: **100% success rate** for supported failure modes (e.g., loss of up to n–k parties, regional outages), with zero permanent asset loss due purely to DR design flaws.
  - Procedure complexity: reduce coordination from "≥5 organizations/teams over several days" to "≤3 main actors with mostly automated workflows" for the majority of incidents.
  - Third-party dependency: minimize or eliminate reliance on opaque external recovery services unless they provide verifiable security guarantees and clear SLAs.
- **Boundary conditions**:
  - No design is allowed to reconstitute a full private key in one place, even temporarily.
  - Recovery paths must remain usable by operations staff without specialist cryptography expertise.
  - Regulatory expectations for 24–48h recovery must be satisfied with audit-ready evidence.

### 1.3 Extensibility & Reframing

- **By attributes ("one object, many attributes")**:
  - View DR not only as *key* recovery but also as **service continuity**: capacity to rotate keys, move assets, or switch signing backends under stress.
  - Consider **confidentiality, integrity, availability, and auditability** as separate axes rather than a single "security" attribute.
- **By structure (virtual vs. physical; hard vs. soft)**:
  - Physical level: HSMs, secure vaults, data centers, hardware tokens.
  - Logical level: threshold parameters (k-of-n), quorum policies, and workflows.
  - Organizational level: who approves DR invocations, who holds which shares, which jurisdictions.
- **Reframed problem statement**:
  - Instead of "how to restore lost MPC keys", frame as **"how to design MPC custody architectures whose signing capability can be re-established within 24h under defined disaster models, without violating non-custodial and non-single-trustee guarantees"**. This framing surfaces design levers beyond raw key reconstruction (e.g., pre-authorized migration, hot-standby clusters, and hierarchical key structures).  

---

## 2. Internal Logical Relations (Aspect 2) — Logic & Balance 【Core】

### 2.1 Key Elements Inside the System

- **Roles**:
  - MPC wallet provider engineering teams (protocol and infra).
  - Institutional custody operators (24/7 NOC, runbooks).
  - Compliance and risk management teams.
  - Third-party recovery service providers (optional).
- **Resources & artifacts**:
  - Key shares and backup shares (in HSMs, secure vaults, cloud KMS, hardware devices).
  - DR orchestration platform(s): scripts, services, dashboards for triggering and monitoring recovery.
  - Identity and access-control systems for operators and approvers.
- **Rules and constraints**:
  - Threshold rules (k-of-n) for both normal signing and DR flows.
  - Policy rules for when DR can be invoked (incident severity, consensus conditions, multi-role approvals).

### 2.2 Balance & "Degree"

- **Redundancy degree**:
  - Too few parties (n close to k): **low** resilience to failures.
  - Too many parties (large n): higher chance some are offline, more complex coordination, and more attack surface. [Source: CoinCover disaster recovery blog, 2023]
- **Backup frequency and strictness**:
  - Overly frequent backup rotations and checks can be operationally expensive and error-prone.
  - Too infrequent checks cause DR paths to rot (stale contacts, revoked credentials, expired certificates).
- **Access control strictness**:
  - Excessively strict policies (e.g., requiring many C-level approvals in multiple time zones) can make timely DR impossible during real incidents.
  - Overly permissive DR triggers increase risk of insider abuse or coercion.

### 2.3 Causal Chains

- **Chain A: Share unavailability → extended outage → regulatory risk**:
  1. Hardware or regional failure removes access to some MPC parties.
  2. Remaining parties are insufficient to satisfy k-of-n threshold.
  3. DR process requires manual coordination across multiple organizations.
  4. Actual RTO is several days, exceeding regulatory expectations.
  5. Custodian faces both reputational damage and formal regulatory consequences.
- **Chain B: Complexity → misconfiguration → permanent loss**:
  1. Complex backup architecture (multi-region, multi-vendor, social recovery) is hard to keep consistent.
  2. At least one backup channel fails silently (e.g., misconfigured encryption keys or expired credentials).
  3. During real disaster, multiple assumptions prove false, and k-of-n cannot be reached via any path.
  4. Assets in affected wallets become permanently inaccessible.

---

## 3. External Connections (Aspect 3) — Breadth & Fairness 【Core】

### 3.1 Stakeholder Map

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|-------------|-----------|
| Upstream | MPC protocol developers, cryptography researchers | Strong security proofs, robust implementations, acceptable performance | Limited insight into each custodian's operational DR reality | May design schemes difficult to operationalize in harsh DR conditions |
| Downstream | Institutional clients (pension funds, funds, corporates) and end users | Asset safety, predictable access, clear SLAs, regulatory compliance | Limited technical knowledge of MPC internals; rely on provider assurances | Demand strong guarantees but may resist higher fees for robust DR |
| Sidelineexternal | Regulators, insurers, auditors, third-party DR vendors | Systemic stability, minimized consumer harm, clear standards | Cannot mandate one specific technical design; limited transparency into proprietary MPC stacks | May push for conservative, centralized controls that conflict with decentralization goals |

### 3.2 Environment Factors

- **Regulatory**: Emerging regulations (e.g., EU MiCA, SEC custody rules, MAS guidance) increasingly treat crypto custodians like traditional financial institutions in terms of DR expectations. [Source: Official regulatory communications summarized in Cobo and CoinCover documentation, 2023–2024]
- **Market & competition**: Custodians compete on security reputation; a well-publicized recovery failure can be existential. Conversely, a robust, audited DR story can be a differentiator.
- **Technology trends**:
  - More advanced **threshold ECDSA/EdDSA** protocols and hardened HSM/KMS integration are becoming standard.
  - Cloud providers offer richer primitives (confidential computing, KMS, cross-region failover), enabling new DR architectures but also increasing complexity.

### 3.3 Responsibility & Room

- **Custody providers & MPC vendors**: Must take primary responsibility for designing and testing DR; cannot externalize all risk to clients or third parties.
- **Regulators**: Define outcomes (e.g., RTO windows, evidence requirements) while leaving design freedom; this gives room for innovation but also ambiguity.
- **Third-party DR services**: Provide specialized backup and orchestration, but they should be transparent about security assumptions and allow clients to control keys to the extent possible.

---

## 4. Origins of the Problem (Aspect 4) — Historical Formation 【Advanced】

### 4.1 Historical Nodes

1. **Pre-MPC era**: Seed phrase–based self-custody and single-HSM custody dominate; DR is conceptually simple but security is fragile (single secret, single point of compromise).
2. **Early MPC adoption (2018–2020)**: Custodians adopt basic threshold schemes (e.g., 2-of-3, 3-of-5) without deeply redesigning DR; redundancy (n+2 parties) is the main mitigation. [Source (from problem statement): early MPC wallet industry practices]
3. **First wave of DR-focused services (2020–2022)**: Companies like Cobo, Nemean Services, CoinCover begin offering encoded backup share storage and DR orchestration as services. [Source: Cobo partnership announcement, 2024]
4. **Operational complexity recognized (2022–2024)**: Incidents, tests, and audits show that multi-party, multi-region coordination is much harder than anticipated; providers recognize DR as a separate engineering domain rather than an afterthought.

### 4.2 Background vs. Direct Causes

- **Background (structural) causes**:
  - High complexity of distributed key management versus simple mental models of "backup" carried over from traditional wallets.
  - Lack of widely adopted standards for MPC DR in early years, leading to bespoke, fragile implementations.
- **Direct triggers**:
  - Cloud outages, HSM malfunctions, and staff changes expose missing or broken recovery paths.
  - Regulatory scrutiny forces providers to document DR and reveals gaps during audits.

### 4.3 Root Issues

- **Conceptual misalignment**: Many organizations treated MPC as a drop-in replacement for single keys, underestimating the need to redesign the entire DR lifecycle.
- **Underinvestment in DR**: DR often perceived as "insurance" and deprioritized against growth features; the resulting technical debt accumulates.
- **Limited shared best practices**: Few public case studies and no unified standard leave each provider to reinvent partial solutions.

---

## 5. Problem Trends (Aspect 5) — Future Trajectory 【Core】

### 5.1 Current Trajectory (If Nothing Changes)

- **Incident frequency**: As more assets move into MPC custody, absolute number of DR-relevant incidents (outages, key-share losses) will rise, even if relative rates remain low.
- **Regulatory pressure**: Expectation of 24–48h RTO will become explicit and enforced. Providers unable to meet it may lose licenses or face restrictions.
- **Trust dynamics**: Institutional clients will increasingly ask pointed questions about DR architecture, testing, and previous incidents as part of due diligence.

### 5.2 Early Signals

- RFPs and due-diligence questionnaires already include detailed DR sections asking for RTO metrics, test frequency, and documented runbooks.
- Third-party DR vendors marketing specifically to MPC custodians indicates a recognized market pain.
- Technical blog posts and docs (e.g., Cobo DR guides, CoinCover DR articles, Stackup MPC primers) are dedicating more space to disaster recovery rather than just normal signing flows.

### 5.3 6–24 Month Scenarios

- **Optimistic scenario**:
  - Industry converges on reference architectures combining multi-region redundancy, automated orchestration, and clearly scoped third-party roles.
  - Standardized DR certifications emerge, and most major custodians consistently achieve <12h RTO in drills.
- **Baseline scenario**:
  - Mixed landscape: leading providers invest heavily and achieve strong DR, while long tail remains ad-hoc.
  - A few high-profile incidents drive incremental improvement but not uniform standards.
- **Pessimistic scenario**:
  - One or more catastrophic, widely publicized DR failures cause multi-billion-dollar asset losses.
  - Regulators react with heavy-handed rules (e.g., mandatory centralized DR providers or specific architectures) that conflict with decentralization guiding principles.

---

## 6. Capability Reserves (Aspect 6) — People & Organization 【Advanced】

### 6.1 Existing Strengths

- Many custody providers already operate 24/7 NOCs and have mature incident-management practices (on-call rotations, runbooks, postmortems).
- Top-tier MPC vendors have strong cryptography and security engineering talent, capable of designing and reviewing complex DR protocols.
- Some organizations have experience with traditional financial DR drills (e.g., data-center failover, BCP testing), which can be adapted for MPC.

### 6.2 Capability Gaps

- **Operational cryptography literacy**: Frontline operators often lack intuition for threshold systems, adversary models, and side-channel risks.
- **Cross-organizational DR rehearsal**: Few teams have practiced end-to-end, multi-party MPC recovery exercises that include third-party DR vendors and clients.
- **Runbook quality and automation**: Existing documentation may be high level, with many manual steps, relying on a small number of experts.

### 6.3 Buildable Capabilities (1–6 Months)

- Targeted **training** for NOC and operations teams on specific DR playbooks for MPC.
- Building a dedicated **DR engineering squad** responsible for orchestration tooling, simulations, and continuous improvement.
- Implementing **game-day exercises** (quarterly or semi-annual) that run full DR scenarios end to end and feed improvements back into architecture and runbooks.

---

## 7. Analysis Outline (Aspect 7) — Structure & Judgments 【Advanced】

### 7.1 Structured Outline

1. Recap problem and constraints (Sections 1–3).
2. Analyze historical formation and future trajectory (Sections 4–5).
3. Assess organizational capabilities and gaps (Section 6).
4. Define critical judgments and assumptions about DR design (this section).
5. Compare alternative recovery architectures and trade-offs.
6. Propose prioritized action plan with metrics and timelines.

### 7.2 Key Judgments (to Validate)

1. **Judgment 1 (P0)**: It is feasible to reach ≤24h RTO for most MPC wallets without reintroducing a single trusted third party as the ultimate recovery key holder.
2. **Judgment 2 (P0)**: Automated orchestration and monitoring can reduce human coordination overhead by ≥80% for standard DR cases.
3. **Judgment 3 (P1)**: A hybrid approach (redundancy + geographic distribution + limited, transparent third-party involvement) offers the best risk/benefit trade-off compared with purely self-managed or purely outsourced DR.
4. **Judgment 4 (P2)**: Social recovery will remain niche for institutional use due to legal and governance complexity.

### 7.3 Alternative Paths (One-Line Positioning)

- **Option A — Self-managed, fully redundant MPC DR**: All redundancy and DR flows are operated in-house, with strong multi-region design and automation.
- **Option B — Third-party–anchored DR**: External specialist DR providers store encrypted backup shares and orchestrate recovery on behalf of custodians.
- **Option C — Hybrid, layered DR**: Custodian manages primary redundancy and orchestration but uses third-party services as backstop under tightly controlled conditions.

---

## 8. Validating the Answer (Aspect 8) — Evidence & Experiments 【Advanced】

### 8.1 Potential Biases

- **Security-conservative bias**: Overweighting risk of key compromise can lead to designs that are theoretically safe but practically unrecoverable.
- **Provider self-interest**: Third-party DR vendors may overstate the necessity of outsourcing to justify their role.
- **Underestimation of operational complexity**: Engineering teams may be optimistic about runbook clarity and staff readiness.

### 8.2 Required Intelligence

- Empirical data on **actual MPC DR incidents**: frequency, root causes, RTO distribution, success vs. failure rates.
- Comparative benchmarks of different DR architectures (A/B experiments in controlled testnets or sandboxes).
- Regulatory interpretations and guidance documents clarifying acceptable patterns for delegation and third-party involvement.

### 8.3 Validation Plan

- **Short-term (0–3 months)**:
  - Run internal DR drills simulating loss of one or more MPC parties in production-like staging environments.
  - Measure actual RTO and number of manual steps and actors involved.
- **Medium-term (3–9 months)**:
  - Implement a **pilot hybrid DR architecture** for a subset of wallets; compare RTO, complexity, and risk profile against existing setup.
  - Collect feedback from auditors and regulators on DR documentation and evidence.
- **Metrics**:
  - RTO (median, 90th percentile) per scenario.
  - Number of manual human approvals/steps.
  - Observed failure rate in recovery drills.

---

## 9. Revising the Answer (Aspect 9) — Iteration & Practicality 【Advanced】

### 9.1 Likely Revisions

- As more **real-world incident data** emerges, assumptions about feasible RTO targets may adjust (e.g., certain cross-jurisdictional scenarios may have higher irreducible latency).
- Regulatory and insurance requirements may push towards more standardized DR patterns, narrowing the design space.

### 9.2 Incremental Approach

- Start with **low-risk pilots** on non-critical wallets and gradually expand DR improvements across the portfolio.
- Use **feature flags and configuration profiles** to toggle between DR modes (e.g., degree of redundancy, automated vs. manual flows) for controlled experiments.

### 9.3 "Good Enough" Criteria

- Demonstrated (via drills) median RTO ≤12h and p90 RTO ≤24h for defined incident classes.
- At least two fully tested and documented independent recovery paths for each critical wallet cluster.
- Clear, up-to-date runbooks and ownership assignments for DR actions.

---

## 10. Summary & Action Recommendations — Priority & Practicality 【Core】

### 10.1 Core Insights

1. MPC wallets convert key management into a distributed system problem; DR must be treated as a first-class design dimension, not an afterthought.
2. The main tension is between strong decentralization/zero-trust ideals and the need for tightly orchestrated, fast recovery across organizations and regions.
3. A layered approach—combining redundancy, geographic distribution, limited and transparent third-party involvement, and strong automation—appears most promising for institutional contexts.
4. Organizational capabilities (training, drills, clear ownership) are as critical as cryptographic protocol choices in achieving reliable DR.

### 10.2 Near-Term Action List (0–3 Months)

**【P0 - Critical】**

1. **Map and classify wallets by criticality and DR posture** → Owner: Head of Custody Engineering → Metric: 100% of MPC wallets assigned DR tier and recovery playbook within 8 weeks → Date: YYYY-MM-DD.
2. **Design and execute at least one DR drill per tier** (e.g., loss of one region, loss of one MPC party, correlated vendor outage) → Owner: DR Engineering Lead → Metric: at least 2 successful drills per tier with measured RTO → Date: YYYY-MM-DD.

**【P1 - Important】**

3. **Prototype hybrid DR architecture** (redundant self-managed plus backstop third-party) for a subset of wallets → Owner: MPC Architecture Team → Metric: pilot covering ≥10% of AUM with documented RTO <24h in drills → Date: YYYY-MM-DD.
4. **Enhance runbooks and operator training** with MPC-specific DR procedures and checklists → Owner: NOC Manager → Metric: 90%+ operators certified on updated DR procedures → Date: YYYY-MM-DD.

**【P2 - Optional】**

5. **Explore social or community-based recovery models** for non-institutional or lower-risk segments → Owner: Product & Risk Teams → Metric: one documented experiment with clear risk analysis → Date: YYYY-MM-DD.

### 10.3 Risks & Mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Overcentralization of DR control in one entity | High | Medium | DR design defaults to one vendor or one ops team holding decisive power | Enforce multi-party approvals, transparent governance, and periodic audits of DR flows | CISO |
| Operational failure during real incident despite passing drills | High | Medium | Unexpected combination of failures not covered by scenarios | Increase scenario coverage, employ chaos-engineering style tests, maintain secondary DR paths | DR Engineering Lead |
| Regulatory backlash against innovative DR designs | Medium | Low–Medium | Regulator interprets certain DR patterns as non-compliant | Engage regulators early with design documents; seek pre-approval or guidance | Head of Compliance |

### 10.4 Alternative Paths Comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Fully self-managed redundant MPC DR** | Maximum control, no additional trusted third party, custom-tailored to infra | High engineering and operational cost; need deep in-house expertise | Risk of internal mistakes; harder to meet aggressive RTO if global staff coverage is limited | Large, mature custodians with strong infra and security teams | Small teams lacking 24/7 global coverage or DR expertise |
| **B. Third-party–anchored DR** | Outsources complexity; can leverage specialist expertise and tested platforms | Ongoing vendor fees; new trust dependency; possible vendor lock-in | Vendor compromise or failure may jeopardize recovery; regulatory concerns | Custodians with limited infra resources and strong vendor due-diligence processes | Contexts where non-custodial guarantees are critical or regulators resist heavy outsourcing |
| **C. Hybrid layered DR (recommended)** | Balances control and resilience; primary self-managed redundancy with vendor as backstop; can be tuned per wallet tier | Architectural complexity; need careful design of roles and triggers | Misconfigured interactions between self-managed and vendor paths; potential ambiguity in responsibility | Institutions needing both high assurance and fast RTO, with capacity to manage at least moderate complexity | Organizations unwilling to maintain coordination between internal team and external vendors |

---

## 11. Glossary — Terms & Definitions 【Core】

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **MPC (Multi-Party Computation)** | Cryptographic technique allowing multiple parties to jointly compute a function (e.g., a digital signature) over their inputs while keeping those inputs private | N/A | Used for distributed key signing in wallets [Source: Stackup MPC guide, 2024] |
| **Key share** | A fragment of a private key used in an MPC or threshold scheme; individually useless, but jointly enable signing or reconstruction under protocol rules | N/A | Central object of MPC DR problem [Source: Stackup guide, 2024] |
| **k-of-n threshold scheme** | Cryptographic scheme where any k out of n shares can jointly perform a cryptographic operation; fewer than k shares reveal nothing useful | k, n integers | Generic threshold cryptography concept |
| **Disaster Recovery (DR)** | Organized set of processes, infrastructure, and procedures for recovering systems and access after disruptive events (outages, disasters, attacks) | N/A | Focus of this analysis [Source: CoinCover blog, 2023] |
| **Recovery Time Objective (RTO)** | Target maximum time allowed to restore operations after an incident | Hours | Regulatory DR metric [Source: financial sector DR guidance summarized in Cobo docs] |
| **Redundancy (in MPC)** | Practice of deploying more MPC parties or backup shares than minimally required to tolerate some failures | N/A | Example: 3-of-5 setup tolerates two party failures |
| **Third-party recovery service** | External provider that stores encrypted backup shares and/or orchestrates recovery workflows for clients | N/A | Examples: Cobo, Nemean Services, CoinCover |
| **Geographic distribution** | Storing key shares and backup shares in multiple physical locations/regions to survive regional disasters | N/A | Typical DR pattern in institutional custody |
| **Social recovery** | Recovery strategy where key shares or secrets are split among trusted individuals (friends/family/colleagues) who can cooperate to restore access | N/A | More relevant to consumer wallets; mentioned as high-risk for institutions |
| **HSM (Hardware Security Module)** | Specialized tamper-resistant hardware device for secure key storage and cryptographic operations | N/A | Standard hardware for storing key shares in institutional custody |
| **BCP (Business Continuity Plan)** | Organizational plan to keep critical business operations running or to recover quickly during and after disruptions | N/A | DR is usually one component of BCP |
| **Orchestration platform (for DR)** | Software system that automates steps, approvals, and monitoring during recovery scenarios | N/A | Key enabler of reduced RTO |

---

## 12. References — Evidence & Sources 【Core】

> Note: Many sources below are taken directly from the problem statement and are treated as given inputs rather than newly asserted facts.

### Tier 1–2 External Sources

1. **Chainalysis**. (2025). *Crypto Crime Report 2025: $2.2 Billion Stolen in 2024, 43.8% from Private Key Compromises*. https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2025. **[Cited in: Context Recap, 1.1]**
2. **CoinCover**. (2023). *Why Disaster Recovery for private keys is essential*. https://www.coincover.com/blog/why-disaster-recovery-for-private-keys-is-essential. **[Cited in: Context Recap, 2.2, 5.2]**
3. **Stackup**. (2024). *MPC Wallets: A Complete Technical Guide*. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide. **[Cited in: Context Recap, 1.1, 11]**
4. **Blockworks**. (2023). *MPC Wallets Have a Trade Off. Is It Worth It?* https://blockworks.co/news/mpc-wallets-security. **[Cited in: 1.1, 2.2]**
5. **Cobo**. (2024). *Cobo Expands MPC Key Recovery Partnership with Nemean Services*. https://www.cobo.com/post/cobo-expands-mpc-key-recovery-partnership-with-nemean-services. **[Cited in: 1.1, 4.1]**
6. **Cobo Docs**. *Disaster Recovery | Cobo MPC Co-Managed Custody* and *Hard Key Recovery*. https://docs.cobo.com/cobo-mpc-waas/cobo-mpc-co-managed-custody/mpc-key-share-user-guide/disaster-recovery. **[Cited in: Context Recap, 3.2, 11]**

### Internal/Problem-Provided Data & Assumptions

7. **MPC DR problem statement for institutional wallets**. (2025). Internal specification provided by Infrastructure Team (this document). **[Cited throughout]**
8. **Industry regulatory expectations** (EU MiCA, SEC custody rule, MAS, FSA). Summaries as included in problem statement. **[Cited in: 3.2, 5.1]**

### Estimates & Assumptions (Explicitly Flagged)

9. **RTO ranges and cost percentages**. Method: Derived from ranges in problem statement (3–7 day current RTO; 10–15% operational budget for DR) and generalized for architectural comparison. Confidence: Medium. Validation: future benchmarking across multiple custodians.
