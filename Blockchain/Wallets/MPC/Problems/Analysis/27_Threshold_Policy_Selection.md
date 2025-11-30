# Threshold Policy Selection for MPC Wallets

**Last Updated**: 2025-11-30  
**Status**: Draft – Nine-Aspects Analysis  
**Owner**: Security & Product Team / Architecture & Research

---

## Context Recap

- **Problem title**: Threshold Policy Selection for MPC Wallets (t-of-n signing across mobile, web, and backend cosigners)
- **Current state**:
  - MPC wallets use threshold signature schemes (TSS) where any *t* of *n* key-share holders cooperatively produce a standard ECDSA/EdDSA signature without reconstructing the private key on a single device [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Threshold Signatures & Multi-Party Computation (MPC), TokenToolHub, 2024].
  - Common real-world topologies include **2-of-2**, **2-of-3**, and **3-of-5** policies, often mixing user devices, guardians, and backend nodes [Source: MPC Wallets: A Complete Technical Guide – Technical Foundation & Real-World Implementations, Stackup, 2025].
  - Existing deployments in this organization rely primarily on an **informal 2-of-3 policy** (mobile device + backup device + backend server) chosen without formal availability modeling. Pilot runs have seen **2–4 hour signing outages** when maintenance or device unavailability breaks quorum [Source: Supplementary Analysis, GPT5.md, 2025-11-28].
  - Mobile devices can be offline 10–40% of the time due to OS updates, battery drain, and intermittent connectivity, while backend quorum nodes target 99.5–99.9% uptime but still need maintenance windows [Estimate: based on typical mobile connectivity studies and SRE uptime targets; Stackup, 2025].
- **Pain points**:
  - **Availability risk**: Current threshold policy leads to **5–15% failed signing attempts** due to quorum unavailability, causing "cannot sign" errors and blocking user flows [Source: Supplementary Analysis, GPT5.md, 2025-11-28].
  - **Support overhead**: "Cannot sign" tickets consume **15–25%** of support capacity, driving operational cost and user frustration [Source: Supplementary Analysis, GPT5.md, 2025-11-28].
  - **Security vs UX tension**: Lower thresholds (e.g., 1-of-3) improve availability but expose users to compromise of a single device or server; higher thresholds (e.g., 3-of-5) improve compromise tolerance but risk more frequent quorum failures when multiple parties are offline [Source: Threshold Signatures & MPC – Threats & Mitigations, TokenToolHub, 2024].
- **Goals**:
  - Achieve **≥99.95% monthly signing availability (SLO)** across mobile, web, and backend cosigners.
  - Reduce failed signing attempts due to quorum unavailability from **5–15% → ≤1%**.
  - Maintain or improve **compromise tolerance**, surviving loss or compromise of **1–2 shares** without halting operations or triggering emergency recovery.
  - Reduce "cannot sign" support tickets by **≥50%** within 3 months of rollout and maintain NPS ≥40 on signing flows.
- **Hard constraints**:
  - Total share count limited to **3–5 shares** for UX and cost reasons (more shares increase setup friction and infra overhead) [Source: MPC Wallets: A Complete Technical Guide – When to Use MPC Wallets, Stackup, 2025].
  - Cryptographic stack fixed to modern threshold ECDSA/EdDSA protocols (e.g., GG20/CGGMP21, FROST-like schemes) already deployed in production [Source: CGGMP21 – UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020; FROST, Komlo & Goldberg, 2020].
  - Must preserve **non-custodial positioning**: no single backend operator may be able to sign unilaterally, consistent with emerging regulatory interpretations of MPC custody [Source: MPC Wallets: A Complete Technical Guide – Regulatory Landscape & Compliance, Stackup, 2025].
  - Budget capped at **$50K implementation** and **$10K/month** incremental run cost; implementation window **6 months (Q1–Q2 2025)**.

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

- **Core problem**: Design an MPC wallet threshold policy (t-of-n) and share placement strategy that delivers **≥99.95% signing availability** while ensuring no single party (e.g., backend operator) can sign alone, under **3–5 total shares** and realistic device/backend reliability profiles.
- **Key contradictions**:
  - **Security vs availability**:
    - Higher thresholds (e.g., **3-of-5**) increase resilience to single-share compromise or loss but require more independent cosigners to be online simultaneously, increasing the chance of quorum failure [Source: Threshold Signatures & MPC – Policies and Approvals, TokenToolHub, 2024].
    - Lower thresholds (e.g., **1-of-3**, **2-of-3**) improve availability but reduce collusion resistance; a subset of compromised devices or insiders may reach quorum alone [Source: MPC Wallets: A Complete Technical Guide – Security Benefits & Trade-offs, Stackup, 2025].
  - **Non-custodial stance vs operational simplicity**:
    - Regulators increasingly scrutinize whether MPC operators can unilaterally move funds (effective custody) [Source: MPC Wallets: A Complete Technical Guide – Regulatory Landscape, Stackup, 2025].
    - Operational teams push for backend-heavy policies (e.g., 2 backend + 1 user share) to simplify incident handling, which may edge toward de facto custody if users become optional.
  - **Redundancy vs correlated failures**:
    - Adding multiple mobile shares does not help if both devices follow the same OS update pattern and go offline together.
    - Backend nodes across the same cloud provider/region share common failure modes (network partitions, control-plane incidents), so extra shares don’t linearly improve availability [Source: Site Reliability Engineering, Beyer et al., 2016].
- **Stakeholder tensions**:
  - End users want **reliable, near-instant signing** and simple recovery; they rarely understand quorum policies.
  - Security and compliance teams want **high compromise tolerance**, strict separation of powers, and provable non-custodial guarantees.
  - SRE teams want **operable quorum topologies** with clear maintenance procedures and monitoring; they resist fragile configurations that frequently break under routine maintenance.
  - Product and support want **fewer support tickets** and predictable UX, even if that requires more sophisticated policy logic.

### 1.2 Goals & conditions

- **Availability & reliability targets**:
  - **SLO**: ≥99.95% monthly signing availability (≈22 minutes max downtime/month) for the majority of production flows.
  - **Failed-sign rate**: Reduce failed attempts due to quorum unavailability from **5–15% → ≤1%** over a rolling 30-day period.
  - **Resilience**: Survive loss of **any 1 share** without service interruption; degrade gracefully (recovery path) for loss/compromise of **2 shares**.
- **Security & custody conditions**:
  - No single backend operator or vendor may independently satisfy quorum under any supported policy mode (including emergency/DR paths) [Source: Threshold Signatures & MPC – Threats & Mitigations, TokenToolHub, 2024].
  - Policies must align with non-custodial positioning in major jurisdictions (US, EU, APAC), recognizing that regulators now explicitly consider MPC arrangements under custody rules [Source: MPC Wallets: A Complete Technical Guide – Regulatory Landscape and Compliance, Stackup, 2025].
- **Operational conditions**:
  - Total shares: **3–5** per wallet; more than 5 materially harms UX and ops.
  - Policy complexity must remain explainable in **≤3 setup steps** for typical users and manageable in runbooks for SRE/support.
  - Implementation window: **≤6 months** including telemetry, modeling, pilot, and rollout.

### 1.3 Extensibility & reframing

- **Alternative framings**:
  - From **“Which t-of-n threshold should we pick?”** → **“Which combination of threshold, share placement, and policy logic delivers target SLO and security posture for each risk tier of account?”**
  - From **“One-size-fits-all global policy”** → **“Tiered threshold policies per account class (retail, pro, institutional) with different trade-off curves.”**
- **Attribute-based expansion**:
  - **Object**: MPC wallet signing policy.
  - **Attributes**: threshold `t`, total shares `n`, share types (mobile/web/backend/guardian/HSM), geographic spread, independence of administrative domains, DR/emergency overrides.
  - **Comparable objects**: multisig smart-contract policies, hardware wallet co-sign flows, enterprise approval matrices [Source: Threshold Signatures & MPC – Reference Architectures, TokenToolHub, 2024].
- **Reframing benefits**:
  - Encourages modeling **availability as a function of per-share uptime and correlation**, rather than relying on intuition.
  - Enables different policies for **consumer vs institutional** accounts instead of forcing a single compromise.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Share types**:
  - **User mobile share(s)** – higher variance availability (60–90% online) but strong alignment with user control [Estimate: based on typical mobile connectivity studies and product telemetry benchmarks].
  - **Web/desktop share(s)** – often session-based or browser extension–based; availability tied to active sessions.
  - **Backend quorum node(s)** – high uptime (≥99.5%) but centrally operated; critical for liveness [Source: Site Reliability Engineering, Beyer et al., 2016].
  - **Guardian / recovery share(s)** – held by trusted contacts, organizations, or devices mostly offline, used for recovery and high-risk actions [Source: Threshold Signatures & MPC – Policies and Approvals, TokenToolHub, 2024].
- **Policy engine**:
  - Encodes allowed combinations of signers (e.g., "1 user + 1 backend", "2 users + 1 guardian") and maps them to risk tiers of transactions (small vs large, routine vs admin) [Source: MPC Wallets: A Complete Technical Guide – Policies & Approvals, Stackup, 2025].
- **Reliability parameters**:
  - Per-share online probability `p_i` for each share type.
  - Correlation coefficients `ρ` between shares (e.g., two mobiles on same OS, two backends in same region).
  - Derived quorum availability `P(quorum available) = P(≥ t shares online)` given joint distribution.

### 2.2 Balance & “degree”

- **Threshold `t` vs share count `n`**:
  - For fixed reliability, increasing `t` beyond an optimal point sharply reduces availability without proportionally increasing security (diminishing returns once collusion of 2–3 parties is already highly unlikely) [Source: Threshold Signatures & MPC – Threats & Mitigations, TokenToolHub, 2024].
  - With **3–5 shares**, practical thresholds are **2-of-3**, **2-of-4**, **3-of-4**, or **3-of-5`; more extreme settings (1-of-n, n-of-n) are either insecure or fragile.
- **Backend-heavy vs user-heavy policies**:
  - Backend-heavy (e.g., 2 backend + 1 user) simplifies availability but may risk custody classification if users become optional in most flows [Source: MPC Wallets: A Complete Technical Guide – Regulatory Landscape, Stackup, 2025].
  - User-heavy (2-of-2 or 2-of-3 with predominantly user devices) preserves non-custodial semantics but inherits user device fragility.
- **Static global policy vs dynamic tiered policy**:
  - A single global 2-of-3 policy across all accounts ignores heterogeneity in risk tolerance and transaction patterns.
  - Tiered policies (e.g., 2-of-3 for low-risk flows, 3-of-5 for institutional accounts) better align security with value at risk.

### 2.3 Causal chains (simplified)

1. **Per-share reliability → Quorum availability → Signing success**
   - For a simple independent model with 2-of-3 (one mobile, one backend, one guardian) and rough online probabilities `p_mobile ≈ 0.8`, `p_backend ≈ 0.995`, `p_guardian ≈ 0.7`, the probability of quorum availability is:
   
   ```
   P(quorum) = 1 − P(<2 online)
             = 1 − [P(0 online) + P(1 online)]
   ```
   
   - Even modest drops in `p_mobile` (e.g., during OS rollout weeks) cause visibly higher `P(<2 online)` and thus failed signing attempts. This matches observed 5–15% failure rates in pilots under maintenance and update conditions [Estimate: analytic model calibrated against Supplementary Analysis, GPT5.md, 2025-11-28].
2. **Threshold & placement → Compromise tolerance**
   - With 2-of-3 where 2 shares are backend-operated, compromise of the backend domain alone may be sufficient to sign, undermining non-custodial claims [Source: MPC Wallets: A Complete Technical Guide – Security Trade-offs, Stackup, 2025].
   - A 3-of-5 policy with at least **2 independent user/guardian shares** and **≤2 backend shares** significantly raises the bar for unilateral compromise by any single party.
3. **Policy opacity → Support volume**
   - When users and support staff do not understand which devices or services are part of quorum, outages are misdiagnosed as "app bugs" rather than policy-induced failures, inflating "cannot sign" tickets.

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders & interactions

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream (End users: retail & pro) | Initiate signing from mobile/web clients | High success rate (≥99.95%), simple recovery, intuitive device setup | Limited understanding of quorum, variable device hygiene and uptime | Want maximum convenience; may resist additional devices or approvals |
| Upstream (Institutional clients) | Operate MPC-protected treasuries | Strong internal controls, dual control approvals, auditability | Complex org charts, multi-jurisdiction regulations | Need strict thresholds that can reduce availability |
| Downstream (Security team) | Owns threat model and policy design | High compromise tolerance, clear non-custodial stance | Limited telemetry on device uptime, human resource constraints | May push for high thresholds that hurt UX |
| Downstream (SRE/Operations) | Runs backend quorum nodes | Stable infra, predictable maintenance, low pager load | Budget, on-call fatigue, infra limits | Resists fragile policies that break during routine maintenance |
| Sideline (Customer Support) | Handles "cannot sign" tickets | Reduced volume, clear diagnostics | No direct control over policy or infra | Bears cost of poor policy choices |
| Sideline (Compliance & Legal) | Interpret custody implications | Avoid de facto custody, align with MiCA/SEC guidance | Evolving regulation, multi-region complexity | May oppose backend-heavy policies even if availability is higher |

### 3.2 Environment factors

- **Regulatory environment**:
  - EU MiCA and related guidance explicitly consider MPC custody providers, often requiring clear documentation of who can sign and under what conditions [Source: MPC Wallets: A Complete Technical Guide – Regulatory Landscape, Stackup, 2025].
  - Jurisdictions such as Japan and some US states impose data residency and local-signing requirements that may shape share placement and threshold configuration.
- **Competing architectures**:
  - Smart contract wallets with on-chain policies (multisig, social recovery, session keys) compete with MPC by offering transparent, auditable threshold logic at the cost of higher gas fees and policy leakage [Source: MPC Wallets: A Complete Technical Guide – MPC vs Multisig & Smart Contract Wallets, Stackup, 2025].
  - Hardware wallets plus off-chain approval workflows can deliver strong security but poorer UX in mobile-centric scenarios.
- **Operational norms**:
  - Enterprise custody providers increasingly adopt **tiered controls**: stricter thresholds for high-value treasuries and more permissive ones for low-value hot wallets [Source: Threshold Signatures & MPC – Reference Architectures, TokenToolHub, 2024].

### 3.3 Responsibility & room for maneuver

- **Where the organization must take proactive responsibility**:
  - Selecting formal, model-backed threshold policies per risk tier rather than ad hoc choices.
  - Investing in telemetry (per-share uptime, failure modes) and availability modeling.
  - Documenting policies for regulators and clients, with clear non-custodial reasoning where applicable.
- **Where others need flexibility**:
  - Institutional clients may choose stricter thresholds (e.g., 3-of-5 with multiple internal approvers) and accept lower availability for high-value accounts.
  - Retail users may opt into simpler 2-of-3 configurations with recovery guardians instead of more complex 3-of-5 setups.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **Early MPC deployments (pre-2020)** – Threshold ECDSA was mainly academic; early wallet pilots copied simple multisig-like 2-of-3 policies without rigorous availability modeling [Source: CGGMP21 – UC Non-Interactive, Proactive, Threshold ECDSA, Canetti et al., 2020].
2. **Growth of consumer MPC wallets (2020–2023)** – 2-of-2 and 2-of-3 models (device + server + recovery) became de facto standards, emphasizing UX, but often underestimating device and server correlated downtime [Source: MPC Wallets: A Complete Technical Guide – Real-World Implementations, Stackup, 2025].
3. **Internal pilot with 2-of-3 (2024–2025)** – Organization adopted informal 2-of-3 configuration without SLAs; mobile OS updates and backend maintenance caused 2–4 hour outages and 5–15% failed signs [Source: Supplementary Analysis, GPT5.md, 2025-11-28].
4. **Rising regulatory scrutiny (2023–2025)** – Custody definitions began explicitly referencing MPC; operators recognized that backend-heavy 2-of-3 policies may blur non-custodial claims [Source: MPC Wallets: A Complete Technical Guide – Regulatory Landscape and Compliance, Stackup, 2025].

### 4.2 Background vs direct causes

- **Background causes**:
  - Lack of cross-functional ownership: policy decisions were largely left to engineering or vendor defaults, with limited input from SRE, compliance, or support.
  - No systematic availability modeling or experiments; assumptions about device uptime and maintenance impact remained untested.
- **Direct triggers**:
  - Concrete incidents where simultaneous device OS updates and backend maintenance windows rendered quorum unavailable for hours.
  - Escalating helpdesk complaints and enterprise clients raising concerns about predictable signing reliability.

### 4.3 Root issues

- Treating **threshold policy** as a static configuration, not a living design artifact requiring data-driven iteration.
- Underestimating **correlated risk** (e.g., all mobiles on same OS, all backends in one cloud region).
- Lack of **clear product-level SLOs** for signing availability and explicit mapping from SLOs to policy design.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory if unchanged

- Without intervention, the organization will likely:
  - Continue experiencing **5–15% failed signing attempts** and intermittent multi-hour outages during combined device/backend maintenance.
  - See increased **support volume** and potential churn among high-value users who need reliable execution.
  - Face regulatory and contractual questions from institutional clients about who can sign and under what failure conditions.
  - Lose competitive ground to providers that offer **tiered, well-documented policies** and stronger SLO guarantees [Source: MPC Wallets: A Complete Technical Guide – Provider Comparisons, Stackup, 2025].

### 5.2 Early signals

- Internal telemetry and anecdotal evidence already indicate:
  - Spikes in "cannot sign" tickets correlated with mobile OS update releases and backend maintenance events.
  - Institutional accounts asking for **formal policy documentation** and contingency procedures.
  - Product roadmaps increasingly featuring "availability SLO" and "policy transparency" as selling points.

### 5.3 6–24 month scenarios

- **Optimistic (with structured policy program)**:
  - Organization introduces **tiered threshold policies** (e.g., 2-of-3 retail, 3-of-5 institutional) backed by availability modeling and telemetry.
  - Signing availability meets **≥99.95% SLO** for mainstream flows; failed sign rate drops to **≤1%**.
  - Regulatory and client audits recognize strong controls and clear non-custodial posture where claimed.
- **Baseline (partial fixes)**:
  - Ad hoc adjustments (adding one guardian, moving a backend) yield moderate improvements (e.g., failed signs drop to 2–3%) but still lack formal modeling; outages persist in edge cases.
- **Pessimistic (no material change)**:
  - Repeated outages and lack of formal policy lead institutional clients to favor alternative custodians or smart-contract solutions; internal support and compliance costs continue rising.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- In-house **security and cryptography expertise** capable of understanding and validating threshold protocols (CGGMP21/FROST).
- Established **SRE function** with experience managing high-availability services (99.5–99.9% uptime) and maintenance windows [Source: Site Reliability Engineering, Beyer et al., 2016].
- Access to **supplementary analysis** and prior pilots (e.g., GPT5.md) providing baseline failure and support-ticket data.

### 6.2 Capability gaps

- Limited experience building **formal stochastic availability models** (e.g., Monte Carlo simulations) to compare t-of-n options under correlated failure patterns.
- Insufficient collaboration between **product, security, SRE, and compliance** when setting policies; decisions risk being siloed.
- Lack of user-facing **policy communication** and education (what happens if device is lost, which combinations can sign).

### 6.3 Buildable capabilities (1–6 months)

- Stand up a small **cross-functional taskforce** (security, SRE, product, compliance) to own threshold policy design and iteration.
- Develop **availability modeling tools** (e.g., Python/R notebooks) to compute quorum availability under different t-of-n and placement assumptions.
- Implement **fine-grained telemetry** on share availability (per device type, per region) to calibrate models in real time.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline (summary)

1. Restate business and security requirements for signing availability and compromise tolerance.
2. Model candidate threshold policies (2-of-3, 2-of-4, 3-of-5) with realistic per-share uptime and correlation.
3. Evaluate each candidate on **availability, compromise tolerance, custody posture, and operational complexity**.
4. Recommend **tiered policies by account class**, plus supporting telemetry, runbooks, and documentation.
5. Define implementation roadmap, validation plan, and risk mitigations.

### 7.2 Key judgments (to validate)

- **【P0】** A **2-of-3 policy** with one backend and two user/guardian shares can meet 99.95% availability only if mobile uptime and correlation are better than currently assumed.
- **【P0】** A **3-of-5 policy** with at least two independent user/guardian domains and at most two backend shares offers materially better compromise tolerance for institutional accounts without catastrophic availability loss.
- **【P1】** Availability can be improved more by **better share placement and maintenance coordination** than by simply increasing `n` without modeling.
- **【P1】** Regulatory comfort and client trust will increasingly favor **documented, model-backed policies** over opaque vendor defaults.

### 7.3 Alternative high-level paths

- **Option A – Minimal-change optimization**: Keep 2-of-3 but relocate shares (e.g., 1 mobile, 1 backend, 1 external guardian) and coordinate maintenance windows.
- **Option B – Tiered thresholds**: Adopt 2-of-3 for low/medium-risk flows and 3-of-5 for institutional/high-value accounts, with tailored share placement.
- **Option C – Policy engine upgrade**: Implement a more expressive off-chain policy layer that supports conditional thresholds (e.g., 2-of-3 for small tx, 3-of-5 for large tx or admin actions) [Source: Threshold Signatures & MPC – Policies and Approvals, TokenToolHub, 2024].

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Security conservatism bias**: Overemphasizing worst-case collusion scenarios could push thresholds so high that the system becomes unusable.
- **Availability optimism bias**: Assuming independent per-share uptime when failures are actually correlated (e.g., same cloud provider, same OS release).
- **Regulatory overfitting**: Over-interpreting early regulatory signals and designing overly complex policies that exceed what is practically required.

### 8.2 Required intelligence

- **Telemetry**:
  - Per-share uptime distributions by type (mobile, web, backend, guardian) and region.
  - Joint failure statistics (e.g., how often 2 mobiles are offline together during OS updates).
- **Client input**:
  - Institutional client preferences on security vs availability trade-offs (e.g., whether 3-of-5 is acceptable for daily operations).
- **Regulatory guidance**:
  - Clarified positions from key regulators and legal counsel on when MPC arrangements count as custody vs non-custodial.
- **Benchmarking**:
  - Comparison with public best-practice architectures from leading MPC custodians, smart-contract wallet providers, and hybrid solutions [Source: MPC Wallets: A Complete Technical Guide – Provider Comparisons & Hybrid Approaches, Stackup, 2025].

### 8.3 Validation plan

- **Step 1 – Data collection (Month 1–2)**:
  - Instrument per-share uptime and failed-sign events; build dashboards showing correlations.
- **Step 2 – Modeling (Month 2–3)**:
  - Use collected telemetry to parameterize analytical and Monte Carlo models for 2-of-3, 2-of-4, 3-of-5 candidate policies.
- **Step 3 – Pilot tiered policies (Month 3–5)**:
  - Run pilots with a subset of accounts under 2-of-3 vs 3-of-5; measure availability, support tickets, and user satisfaction.
- **Step 4 – Regulatory/legal review (parallel)**:
  - Present proposed policies and models to legal/compliance and key institutional clients for feedback and formal sign-off.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Threshold choices may change as **empirical uptime data** reveals better or worse-than-expected device reliability.
- Share placement strategies could be revised if **cloud-region or OS-level correlated failures** prove dominant.
- Regulatory interpretations may require adjusting policies to avoid de facto custody in certain jurisdictions.

### 9.2 Incremental approach

- Start with **well-instrumented pilots** and small cohorts before rolling out new thresholds globally.
- Allow **per-account-class overrides** so institutional clients can opt into stricter or more permissive policies under contractual governance.
- Iterate on policy documentation and education based on support feedback.

### 9.3 “Good enough” criteria

- For mainstream retail flows: **p95 signing success ≥99.95%**, failed sign rate ≤1%, and clear recovery paths for lost devices.
- For institutional treasuries: demonstrable ability to withstand **loss/compromise of up to 2 shares** without loss of funds, with acceptable degraded modes.
- For compliance: documented mapping from **policy → custody stance** with legal sign-off.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. Threshold policy selection is a **multi-objective design problem** balancing availability, security, custody posture, and operational complexity—not a simple "pick 2-of-3 vs 3-of-5" toggle.
2. Current ad hoc 2-of-3 configuration likely underperforms both in availability (5–15% failed signs) and in clearly provable non-custodial semantics.
3. A **tiered approach**—2-of-3 for retail and 3-of-5 for institutional/high-value accounts—with carefully chosen share placement offers a better trade-off surface.
4. Success depends on **measurement and modeling** (telemetry + simulations) plus regulatory and client alignment, not just cryptographic protocol choice.

### 10.2 Near-term action list (0–3 months)

- **【P0 – Critical】 Define signing availability SLOs and ownership** → CISO & VP Product → Metric: SLO documented and approved: 0 → 1 global SLO plus per-tier variants → by 2025-01-31.
- **【P0 – Critical】 Implement per-share availability telemetry** → SRE Lead → Metric: % of active wallets with share-uptime telemetry: 0% → 90% → by 2025-02-15.
- **【P0 – Critical】 Build threshold availability model for 2-of-3 and 3-of-5** → Security Architect → Metric: Model reviewed by SRE & Product: 0 → 1 validated model → by 2025-02-28.
- **【P1 – Important】 Design tiered policy catalog (retail vs institutional)** → Security + Product → Metric: Policy catalog approved and documented: 0 → 1 baseline + 1 institutional template → by 2025-03-15.
- **【P1 – Important】 Launch limited pilot of new policies** → Program Manager → Metric: Pilot cohorts onboarded: 0 → ≥2 cohorts (retail + institutional) → by 2025-04-15; measure failed sign rate: 5–15% → ≤2%.
- **【P2 – Optional】 Explore policy-engine enhancements for conditional thresholds** → Architecture Lead → Metric: Prototype design doc: 0 → 1 proposal → by 2025-04-30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Misestimated device/backend uptime leads to wrong threshold choice | High | Medium | Pilot shows higher-than-modeled failed sign rate | Re-run models with updated telemetry; adjust thresholds and share placement; expand guardian usage | Security Architect |
| Regulatory reclassification of policies as custodial | High | Medium | New guidance treats certain backend-heavy MPC setups as custody | Design policies with explicit user/guardian participation; maintain legal review loop; support non-custodial and custodial variants as needed | Head of Compliance |
| Operational complexity of 3-of-5 policies overwhelms SRE/support | Medium | Medium | Frequent misconfigurations or recovery incidents | Introduce opinionated defaults; strong automation and runbooks; reserve 3-of-5 for limited high-value cohorts | SRE Lead |
| Client resistance to more complex setups (additional devices/guardians) | Medium | Medium | Low adoption or negative feedback in pilots | Provide managed guardian services and clearer UX; allow phased opt-in; tailor thresholds per client risk appetite | Product Lead |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Optimized 2-of-3 (status quo+)** | Minimal change; simpler UX; can reach good availability with better share placement and maintenance practices | Limited compromise-tolerance improvement; may not satisfy strict institutional/compliance requirements | Still vulnerable if 2-of-3 includes 2 backend-controlled shares; borderline non-custodial posture | Retail and small-business accounts with moderate balances; environments where mobile uptime is strong | Very high-value treasuries; strict regulators demanding stronger separation of duties |
| **B. Tiered 2-of-3 + 3-of-5 (recommended)** | Aligns policy strictness with account risk; improves institutional security while keeping retail UX reasonable | More complex policy catalog; higher ops overhead; need telemetry and modeling | Risk of misconfiguring tiers or mis-assigning accounts | Organizations with mix of retail and institutional users; teams able to invest in policy tooling | Tiny teams unable to support multiple policy types |
| **C. Advanced conditional policy engine** | Fine-grained control (e.g., 2-of-3 for small tx, 3-of-5 for large/admin); powerful selling point | High implementation complexity; need careful correctness and security reviews | Policy bugs could cause unexpected unavailability or security gaps | Mature teams with strong engineering and audit capabilities; long time horizon | Early-stage teams; situations demanding quick short-term improvements |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **MPC (Multi-Party Computation)** | Cryptographic technique where multiple parties jointly compute a function over their inputs without revealing them, used here for distributed key management and signing | N/A | Basis for MPC wallets [Source: MPC Wallets: A Complete Technical Guide – Technical Foundation, Stackup, 2025] |
| **Threshold signature** | Scheme where any subset of at least *t* of *n* parties can jointly produce a valid signature, with no single party holding the full key | N/A | Core primitive for MPC wallets [Source: Threshold Signatures & MPC, TokenToolHub, 2024] |
| **t-of-n policy** | Threshold configuration where *t* shares out of *n* total are required to authorize a transaction | N/A | Central design variable in this analysis |
| **Quorum** | The set of parties whose combined shares satisfy the threshold *t* and can authorize a signature | N/A | Quorum availability drives signing success |
| **Quorum availability** | Probability that enough independent shares (*≥ t*) are simultaneously online and able to participate in signing | % (0–100%) | Directly determines signing availability SLO |
| **Compromise tolerance** | Ability of the system to withstand loss or compromise of some shares without loss of funds or control | # of shares tolerated | Higher thresholds and diverse share placement increase tolerance |
| **Guardian** | A non-primary share holder (person, organization, or device) designated mainly for recovery or high-risk actions | N/A | Used in 2-of-3 and 3-of-5 patterns to improve resilience |
| **Non-custodial positioning** | Claim that the service provider cannot unilaterally move user funds because it alone cannot satisfy quorum | N/A | Affected by how many shares are under provider control |
| **SLO (Service Level Objective)** | Target reliability metric, such as ≥99.95% signing availability per month | %, time | Drawn from SRE practices [Source: Site Reliability Engineering, Beyer et al., 2016] |
| **Correlated failure** | Situation where multiple shares fail together due to shared dependencies (e.g., same cloud region, OS) | N/A | Key factor in availability modeling |
| **Tiered policy** | Approach where different account classes use different threshold and placement policies based on risk | N/A | Recommended pattern in this analysis |

---

## 12. References

### Tier 1 – Cryptography & Protocol Foundations

1. **Canetti, R., Makriyannis, N., & Peled, U.** (2020). *UC Non-Interactive, Proactive, Threshold ECDSA*. Cryptology ePrint Archive, Paper 2020/492. https://eprint.iacr.org/2020/492 **[Cited in: Context Recap, 4.1, 6.1]**
2. **Komlo, C., & Goldberg, I.** (2020). *FROST: Flexible Round-Optimized Schnorr Threshold Signatures*. Cryptology ePrint Archive, Paper 2020/852. https://eprint.iacr.org/2020/852 **[Cited in: Context Recap, 6.1]**

### Tier 2 – Industry Guides & Technical Overviews

3. **Stackup.** (2025). *MPC Wallets: A Complete Technical Guide*. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide **[Cited in: Context Recap, 1.1–1.3, 2.1–2.2, 3.2, 4.1, 5.1, 8.2, 11]**
4. **TokenToolHub.** (2024). *Threshold Signatures & Multi-Party Computation (MPC): Modern Wallet Security Beyond Multisig*. https://tokentoolhub.com/threshold-signatures-multi-party-computation-mpc/ **[Cited in: 1.1–1.3, 2.1–2.3, 3.2, 7.3, 11]**
5. **Safeheron.** (2025). *MPC or Multisig Wallets: Which Offers Better Security?* Safeheron Blog. https://safeheron.com/blog/mpc-vs-multisig-wallets-security-differences-similarities **[Cited in: 1.1, 3.2]**
6. **Beyer, B., Jones, C., Petoff, J., & Murphy, N.** (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O’Reilly Media. **[Cited in: 2.1, 2.2, 6.1, 10.2, 11]**

### Internal Sources & Estimates

7. **Supplementary Analysis, GPT5.md.** (2025-11-28). *Blockchain MPC Wallet Problem Extraction – Threshold Policy Selection & Outage Incidents*. Internal analysis document. **[Cited in: Context Recap, 2.3, 4.1, 5.1]**
8. **Internal Telemetry & Support Data (Planned).** (2025). *MPC Wallet Signing Availability and “Cannot Sign” Ticket Volumes*. Engineering dashboards and support systems. **[Planned for: 5.2, 8.2]**
9. **Availability & Uptime Estimates.** Method: Synthesis of mobile connectivity studies, SRE uptime targets, and prior deployments. Confidence: Medium. Validation: Compare with measured per-share uptime distributions collected in pilots. **[Used in: Context Recap, 2.1–2.3, 5.1, 8.2]**
