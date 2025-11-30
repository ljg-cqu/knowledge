# Regulatory Custody Control Classification Ambiguity for MPC Wallets – Nine-Aspects Analysis

**Document Metadata**  
- **Created**: 2025-11-30  
- **Status**: Draft  
- **Analysis Framework**: Nine Aspects for Analyzing Problems  
- **Source Problem**: `08_Regulatory_Custody_Control_Classification.md` (MPC Wallets – Problems)

---

## Table of Contents

1. [Context Recap](#context-recap)
2. [1. Problem Definition (Aspect 1)](#1-problem-definition-aspect-1)
3. [2. Internal Logical Relations (Aspect 2)](#2-internal-logical-relations-aspect-2)
4. [3. External Connections (Aspect 3)](#3-external-connections-aspect-3)
5. [4. Origins of the Problem (Aspect 4)](#4-origins-of-the-problem-aspect-4)
6. [5. Problem Trends (Aspect 5)](#5-problem-trends-aspect-5)
7. [6. Capability Reserves (Aspect 6)](#6-capability-reserves-aspect-6)
8. [7. Analysis Outline (Aspect 7)](#7-analysis-outline-aspect-7)
9. [8. Validating the Answer (Aspect 8)](#8-validating-the-answer-aspect-8)
10. [9. Revising the Answer (Aspect 9)](#9-revising-the-answer-aspect-9)
11. [10. Summary & Action Recommendations](#10-summary--action-recommendations)
12. [11. Glossary](#11-glossary)
13. [12. References](#12-references)

---

## Context Recap

- **Problem title**: Regulatory Custody Control Classification Ambiguity for MPC Wallets
- **Current state**:
  - U.S. federal and state money transmission regimes use **different tests for "control" of virtual currency**. FinCEN’s 2019 guidance focuses on whether an intermediary has "total independent control" over value, i.e., unilateral ability to move funds without user consent [Source: *Application of FinCEN’s Regulations to Certain Business Models Involving Convertible Virtual Currencies*, FinCEN, FIN-2019-G001, 2019].  
  - The CSBS **Money Transmission Modernization Act (MTMA)** Article XIII instead defines control as the **"power to execute unilaterally, or prevent indefinitely, a virtual currency transaction"**, broadening the concept to functional control even without full key possession [Source: *CSBS Money Transmission Modernization Act, Article XIII – Virtual Currency*, CSBS, 2020].  
  - Several key states (e.g., California via the **Digital Financial Assets Law (DFAL)**, Minnesota, North Dakota, and guidance in Florida and Rhode Island) have adopted or converged on MTMA-style control language, while others still rely on pre‑MTMA formulations [Source: *CSBS MTMA Legislative Update 2024*, CSBS, 2024; Source: *Multi-Party Computation (MPC) Wallets and the Evolving Regulatory Landscape in the United States*, S. Horowitz Law Firm, 2025].
- **Pain points**:
  - MPC wallet providers historically relied on the view that because **no single party holds the full private key**, they lack "total independent control" and thus are non‑custodial under FinCEN’s 2019 framework [Source: *FinCEN CVC Guidance*, FinCEN, 2019; Source: S. Horowitz blog on MPC wallets, 2025].  
  - Under MTMA’s broader test, if a provider can **unilaterally execute or indefinitely block a transaction**, this may constitute control, pushing many MPC designs into money transmitter licensing even without key possession [Source: CSBS MTMA Article XIII, 2020; Source: California DFAL bill analyses, CA Legislature, 2023].  
  - Institutional investors, exchanges, and custody clients cannot obtain **clear, consistent classification** across 50 states, creating legal risk and blocking large pools of capital from using MPC-based custody [Source: *The Future of Digital Asset Custody: Building Trust at Scale*, State Street, 2025].
- **Goals** (from problem statement, refined):
  - Achieve **clear, harmonized classification** of MPC wallet providers under FinCEN + state regimes by **Q4 2025**, or at least a small number (≤5) of recognizable regulatory archetypes instead of 50 bespoke positions.  
  - Reduce **industry-wide licensing and legal uncertainty costs** from an estimated ＞$100M (if treated as full money transmitters in all states) to ＜$20M via targeted licensing and/or safe harbors [Estimate: based on typical multi‑state licensing and legal costs for MSBs; see problem statement].  
  - Unlock institutional adoption, growing MPC-based custody AUM from ＜$10B to ≥$50–100B by 2026 if classification risk is resolved [Source: Intel Market Research MPC wallet market report, 2024; Source: State Street digital asset custody survey, 2025].
- **Hard constraints**:
  - FinCEN and state regulators cannot be forced to issue guidance on a specific timetable; industry can only influence via **comment processes, no‑action letter requests, and engagement** [Source: FinCEN administrative practice overview, U.S. Treasury, 2019].  
  - State adoption of MTMA (or similar) is **voluntary and political**; each legislature has its own calendar and priorities [Source: CSBS MTMA legislative tracker, 2024].  
  - Providers must **keep operating during uncertainty**, avoiding both over‑licensing (costly) and under‑licensing (enforcement risk).
- **Key facts from inputs**:
  - Global MPC wallet development market ≈ **USD 61.4M in 2024**, with strong growth potential once regulatory ambiguity is reduced [Source: *MPC Wallet Development Market Growth 2025–2032*, Intel Market Research, 2024].  
  - Digital asset market overall is already **＞USD 3T**, and institutional adoption is constrained by custody/regulatory questions rather than pure technology [Source: State Street digital asset custody report, 2025].  
  - Problem timescale: **Q1 2025 – Q4 2025** for regulatory advocacy, with downstream impact over 1–3 years.

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

**Core problem**  
MPC wallet providers sit in a grey zone between **custodial** and **non‑custodial** models. Under traditional analysis, absence of unilateral key control meant many MPC setups were treated as non‑custodial and outside money transmitter licensing. Under MTMA-style functional control tests, however, **operational power over transaction execution or veto** can be sufficient for classification as a money transmitter, even if no party holds the full private key [Source: FinCEN CVC Guidance, 2019; Source: CSBS MTMA Article XIII – Virtual Currency, 2020; Source: S. Horowitz MPC wallets blog, 2025].

This creates a **three-way contradiction**:

1. **Technical architecture vs. legal definition**  
   - Technically, MPC splits a key into shares and uses threshold signing; no actor can reconstruct the full key in the normal case.  
   - Legally, regulators care about who can **cause** or **block** transfers, not just who has mathematical key material.  
   - Result: MPC providers can be perceived as both non‑custodial (no full key) and custodial (can unilaterally approve/block) depending on which notion of "control" dominates [Source: FinCEN 2019 guidance multi‑sig analysis; Source: CSBS MTMA commentary, 2023].

2. **Federal vs. state interpretations**  
   - FinCEN’s 2019 guidance provides a relatively narrow notion of control ("total independent control"), under which many unhosted multi‑sig/MPC wallets are not money transmitters if the user remains in effective control [Source: FinCEN FIN‑2019‑G001, 2019].  
   - MTMA and MTMA-inspired state statutes define control more broadly as the **"power to execute unilaterally, or prevent indefinitely"** virtual currency transactions [Source: CSBS MTMA Article XIII §13.06, 2020].  
   - Providers serving the whole U.S. must navigate the **more stringent state standard** where adopted, even if federal guidance is more lenient.

3. **Innovation vs. compliance risk**  
   - MPC architectures are promoted as **safer than single-key or basic multi-sig** for institutional custody [Source: Intel Market Research MPC report, 2024; Source: State Street custody report, 2025].  
   - But if MPC providers are forced into **full money transmitter regimes** in dozens of states, compliance costs (licensing, audits, bonding, examinations) can easily exceed **USD 2–5M per provider** for initial rollout, plus significant ongoing overhead [Estimate: based on multi‑state MSB licensing cost benchmarks from U.S. compliance consultancies, 2023–2024].  
   - Result: Risk‑averse institutions delay MPC adoption until **classification is predictable**, slowing security upgrades in custody.

### 1.2 Goals & conditions

**Primary regulatory goals** (restating and sharpening from the problem statement):

- **G1 – Classification clarity (Critical)**:  
  Obtain explicit written guidance or repeatable patterns indicating when MPC wallet arrangements **do or do not** constitute money transmission and/or custody under:  
  - FinCEN CVC guidance (federal MSB registration lens), and  
  - MTMA-style state money transmission statutes and rules.  
  Target: by **Q2 2025**, at least one of: (a) FinCEN public statement on MPC; (b) a widely adopted CSBS interpretive note; or (c) a cluster of state-level bulletins converging on the same tests [Source: FinCEN prior guidance timelines 2013–2019; Source: CSBS model law practice, 2020–2024].

- **G2 – State harmonization (Critical)**:  
  Reduce the effective variety of MPC classifications from **≈50 independent state positions** to **≤5 standard archetypes** (e.g., "pure non‑custodial", "MPC as money transmitter", "limited MPC support provider").  
  Measurement: mapping exercise by trade associations and law firms; goal by **Q4 2025** [Source: CSBS MTMA legislative tracker, 2024; Source: S. Horowitz state-by-state MPC survey, 2025].

- **G3 – Compliance cost optimization (Important)**:  
  Move from the current worst‑case **"license everywhere or geofence"** posture (est. industry-wide licensing/legal burden ＞USD 100M if every major MPC provider took all 50 state licenses) to a **targeted licensing or safe-harbor model** costing ＜USD 20M aggregate by 2026 [Estimate: based on standard MSB licensing costs × number of MPC providers in problem statement].

- **G4 – Institutional adoption and market growth (Important)**:  
  Enable institutional MPC custody AUM to grow from **＜USD 10B** today to **≥USD 50–100B by Q4 2026**, assuming custody classification and fiduciary standards are clarified [Source: Intel Market Research MPC wallet market report, 2024; Source: State Street digital asset custody survey, 2025].

**Hard constraints and boundary conditions** (re‑emphasized):

- Regulatory timelines (6–18 months for major guidance) and legislative cycles are outside industry control [Source: FinCEN guidance history, 2013–2019; Source: state legislative calendars, NCSL, 2024].
- Industry advocacy budgets (USD 2–5M jointly + USD 0.5–1M per provider for internal work) limit the total **volume and depth of engagements** feasible within a year [Estimate: based on typical costs for national regulatory initiatives in fintech].

### 1.3 Extensibility & reframing

**Attribute-based reframing**

- **One object, many attributes – "control"**  
  The object is **"control over customer digital assets"**. Attributes include:  
  - Legal control (right and duty to safeguard assets under contract/regulation)  
  - Operational control (ability to sign or block transactions)  
  - Technical control (possession of key material or ability to reconstruct it)  
  - Economic control (ability to redirect benefit of assets)  
  - Risk control (ability to mitigate or cause loss).

  Reframing: Instead of a binary "custodial vs. non‑custodial" label, regulators could distinguish **sub‑types of control** and tailor obligations accordingly (e.g., full custody vs. co‑custody vs. non‑custodial support) [Source: SEC Custody Rule 206(4)-2 interpretive guidance, SEC, 2017; Source: EU MiCA custody provisions, EU Regulation 2023/1114].

- **Virtual vs. physical**  
  - *Physical layer*: key shares, HSMs, MPC nodes, signing infrastructure.  
  - *Virtual layer*: rights, veto powers, service-level obligations.  
  In many MPC setups, the **virtual power to veto or schedule transactions** is more determinative for regulators than literal possession of the physical key bits [Source: CSBS MTMA commentary on control, 2020; Source: S. Horowitz MPC wallets blog, 2025].

**Reframing opportunities**

1. From "Is MPC custodial or non-custodial?" → **"Which risk and control profiles do different MPC architectures create, and what obligations attach to each profile?"**  
2. From "Avoid money transmitter status" → **"Obtain predictable, right‑sized obligations for each MPC role (operator, signer, coordinator)."**  
3. From "one-size-fits-all U.S. classification" → **"interoperable, tiered classification that aligns U.S. standards with EU MiCA and other major regimes to reduce cross‑border friction"** [Source: MiCA Title V, EU, 2023; Source: MAS Guidelines for DPT service providers, MAS, 2021].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

**Roles inside the problem**

- **MPC wallet providers** – design and operate MPC signing infrastructure; may host some or all parties; often market themselves as non‑custodial but offer operational vetoes or policy controls.  
- **Institutional clients** – investment managers, exchanges, corporates needing compliant custody solutions; sensitive to both classification and operational resilience [Source: State Street custody survey, 2025].  
- **Retail users (indirectly)** – may be end beneficiaries of institutional assets or directly use MPC-based wallets.  
- **Federal regulator (FinCEN)** – defines who is a money transmitter at the federal level and sets AML program expectations [Source: FinCEN CVC Guidance, 2019].  
- **State regulators (50+)** – banking/financial services departments granting or denying money transmitter licenses and adopting MTMA [Source: CSBS MTMA overview, 2020].  
- **Trade associations** – e.g., Blockchain Association, Chamber of Digital Commerce, that coordinate comment letters and advocacy.

**Resources**

- **Legal and compliance budgets** of MPC providers and industry groups.  
- **Technical artifacts**: architecture diagrams, threat models, and formal MPC protocol descriptions used to explain control properties to regulators.  
- **Precedents**: FinCEN’s multi‑sig analysis, prior state guidance on virtual currency, DFAL materials, no‑action letters [Source: FinCEN FIN-2019-G001 examples; Source: CA DFAL legislative reports, 2023].

**Processes and rules**

- Money transmitter licensing application, examination, and renewal processes at state level.  
- Federal MSB registration, AML program implementation, and SAR reporting at FinCEN.  
- Internal provider processes: policy engines that can block or require approvals for certain transactions (e.g., risk-based rules, whitelists).  
- MPC signing flows: threshold participation, fallback mechanisms if a party is offline, and incident response flows.

### 2.2 Balance & "degree"

**Security vs. regulatory "control"**

- MPC providers add policy engines to reduce fraud/AML risk (e.g., blocking transactions to sanctioned addresses) [Source: FATF Virtual Assets Guidance, FATF, 2021].  
- The more **effective veto power** the provider has, the more regulators may see them as having control.  
- Balance point: **enough policy control to satisfy AML/OFAC expectations without giving providers unconstrained unilateral veto/execute powers**; design choices (e.g., designating some veto rights to independent compliance trustees) can shift this degree.

**Centralization of MPC roles vs. distribution**

- If a single corporate group hosts all MPC parties and orchestrates signing, regulators are more likely to treat it as a **single controlled enterprise**.  
- If distinct, independently governed parties participate (e.g., client-controlled node, independent trustee, and managed MPC provider), classification may tilt away from single money transmitter status and toward **shared or non‑custodial control** [Source: S. Horowitz MPC wallets blog, 2025; Source: institutional MPC custody whitepapers, BitGo/Fireblocks, 2023–2024].

### 2.3 Causal chains

**Chain 1: Functional veto power → Perceived control → Money transmitter classification**

```text
MPC provider can unilaterally veto or defer transactions
→ Regulator applies MTMA-style "execute or prevent indefinitely" test
→ Provider deemed to have control of virtual currency
→ State money transmitter license required (plus MSB duties)
→ Higher fixed compliance cost + supervisory expectations
→ Smaller providers exit market or geofence high-MTMA states
```

[Source: CSBS MTMA Article XIII – definition of control, 2020; Source: CA DFAL coverage of virtual currency, 2023; Source: Florida and Rhode Island MTMA-style control guidance, 2022–2023].

**Chain 2: Ambiguous classification → Legal opinions & no-action letters → Uneven playing field**

```text
No explicit MPC guidance from FinCEN or harmonized state approach
→ Providers commission bespoke legal opinions and seek state-by-state comfort
→ Some obtain informal or no-action comfort (non-binding, expensive)
→ Others operate cautiously or over-license
→ Institutions favor providers with perceived regulatory advantage
→ Industry-wide uncertainty persists; systemic clarity does not improve
```

[Source: S. Horowitz MPC wallets blog (discussion of state no-action letters), 2025; Source: U.S. MSB legal practice notes, 2022–2024].

**Chain 3: Overly broad control definition → Innovation chilling effect**

```text
MTMA-style control adopted widely without clear carve-outs for non-custodial MPC
→ Many MPC roles presumptively classified as money transmitters
→ Compliance costs and liability rise sharply
→ New entrants and open-source MPC experiments decline
→ Fewer secure alternatives to traditional custodial models
→ Overall systemic custody risk may increase despite intent to protect consumers
```

[Source: CSBS MTMA commentary, 2020; Source: comparative innovation vs. regulation studies in fintech, BIS/IMF, 2022–2023].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders table

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| **Upstream – Federal regulator (FinCEN)** | Defines MSB/money transmitter status & AML obligations | Maintain effective AML/CFT controls, avoid regulatory gaps [Source: FinCEN mission statement, 2018] | Limited bandwidth to issue tech‑specific guidance; must preserve consistency across CVC models | May favor conservative classification if risks unclear, creating friction with innovation goals |
| **Upstream – State regulators (MTMA adopters)** | License money transmitters; implement MTMA | Harmonize standards, prevent consumer harm, coordinate via CSBS [Source: CSBS MTMA overview, 2020] | Political processes; uneven technical expertise on MPC; pressure to avoid being "crypto‑friendly outlier" | Broad control definition can overreach, but narrow one invites criticism after incidents |
| **Downstream – Institutional investors** | Allocate capital using MPC custodian services | Need clear custody classification to satisfy fiduciary and audit requirements [Source: State Street custody report, 2025] | Restricted by internal risk policies and regulators; cannot rely on ambiguous non‑custodial claims | Want robust security (MPC) but not at cost of regulatory uncertainty |
| **Downstream – Exchanges & trading venues** | Safeguard customer assets, integrate MPC providers | Need scalable, compliant custody rails, often multi‑jurisdictional | Need 24/7 operations; regulatory capital and licensing costs affect unit economics | May choose simpler custodial models if MPC classification too uncertain |
| **Sideline – Traditional custodians & banks** | Compete with MPC-native providers | Prefer clear rules that they can satisfy with existing infrastructure | Legacy systems and slower innovation cycles; may resist models they cannot control | Might lobby for interpretations that favor their existing custodial model |
| **Sideline – Trade associations** | Aggregate industry position, draft proposals | Aim for calibrated regulation supporting innovation & consumer protection | Member interests differ (retail vs. institutional, U.S.-only vs. global) | Must balance calls for clarity with fear of triggering overly strict rules |

### 3.2 Environment – policy, market, technology

- **Policy/legal environment**  
  - FinCEN virtual currency guidance (2013, 2019) defines broad money transmitter categories but **does not yet address MPC explicitly** [Source: FinCEN CVC guidance FIN-2019-G001, 2019].  
  - MTMA provides a **model state framework** emphasizing functional control, with growing adoption across states [Source: CSBS MTMA, 2020; Source: CSBS MTMA legislative tracker, 2024].  
  - Internationally, the **EU’s MiCA**, the **UK FCA**’s custody expectations, **Singapore MAS** DPT rules, and **Japan FSA** guidance all move toward **risk‑based crypto custody regulation**, setting useful comparators for U.S. policy [Source: EU MiCA Regulation 2023/1114; Source: UK FCA Policy Statement PS23/10; Source: MAS DPT Guidelines, 2021].

- **Market environment**  
  - Rapid growth in institutional interest for digital assets and demand for **bank‑like custody quality** [Source: State Street custody report, 2025].  
  - Competition among MPC infrastructure providers (Fireblocks, BitGo, Coinbase WaaS, etc.) to win institutional mandates by demonstrating both **security and regulatory readiness** [Source: vendor whitepapers, 2023–2024].  
  - Uncertainty pushes some institutions **back to traditional custodians or simpler hot‑wallet architectures**, slowing migration to safer MPC models.

- **Technology environment**  
  - Production-grade MPC and threshold signature schemes (e.g., GG18, CGGMP21, DKLS23) are increasingly mature [Source: ACM CCS / Crypto conference papers 2018–2023].  
  - Architecture choices (e.g., where veto logic sits, who can pause flows, whether any party can rebuild keys) directly affect **whether functional control exists** under MTMA-style tests [Source: S. Horowitz MPC wallets blog, 2025].

### 3.3 Responsibility & room to maneuver

- **Where MPC providers should assume responsibility**  
  - Provide **transparent architecture descriptions** clearly mapping each MPC role to specific rights (execute, veto, view, configure), enabling regulators to apply control tests accurately.  
  - Avoid marketing that over‑simplifies MPC as "always non‑custodial"; instead, align customer messaging with realistic regulatory positions.  
  - Proactively build **compliance features** (audit trails, sanction screening hooks) that make regulators more comfortable recognizing limited-control tiers.

- **Where to leave room for others**  
  - Allow **independent trustees or client‑controlled nodes** to hold critical veto powers where feasible, so the provider is not the sole gatekeeper.  
  - Collaborate with **standard‑setting bodies and trade associations** rather than creating proprietary definitions of "non‑custodial".

- **Keeping future options open**  
  - Design MPC architectures that can **change control allocation over time** (e.g., moving veto rights from provider to client as regulators clarify expectations).  
  - Maintain optionality between **licensing as a money transmitter** vs. operating under a non‑custodial or limited‑custody framework, depending on the jurisdiction.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2013 – Initial FinCEN virtual currency guidance**  
   - FinCEN’s first major statement on virtual currencies established that administrators and exchangers of convertible virtual currency are money transmitters, but treated users as non‑MSBs [Source: *Application of FinCEN’s Regulations to Persons Administering, Exchanging, or Using Virtual Currencies*, FinCEN, 2013].  
   - Wallet models were early and simple; MPC was not a consideration.

2. **2019 – FinCEN CVC guidance with multi-sig analysis**  
   - FinCEN issued comprehensive guidance applying existing BSA rules to a wide array of CVC business models, including hosted and unhosted wallets and multi-sig arrangements [Source: FinCEN FIN‑2019‑G001, 2019].  
   - Crucially, FinCEN analyzed multi‑sig wallets and suggested that an entity that cannot on its own move customer funds (no "total independent control") may not be a money transmitter. This planted the **"no unilateral control → non‑custodial"** intuition many MPC providers adopted.

3. **2020–2021 – CSBS develops MTMA**  
   - CSBS drafted the Money Transmission Modernization Act as a **model state law** to harmonize licensing and supervision of money transmitters, including explicit virtual currency provisions [Source: CSBS MTMA, 2020].  
   - MTMA Article XIII defined control in terms of the **power to execute or prevent** transactions, broadening beyond key possession.

4. **2022–2024 – State adoption and divergence**  
   - States such as **California (DFAL)**, Minnesota, and North Dakota adopt MTMA or MTMA-inspired standards; Florida and Rhode Island issue guidance or laws with similar control concepts [Source: CSBS MTMA legislative tracker, 2024; Source: CA DFAL statutory text, 2023].  
   - MPC providers discover that **state-level functional control tests** may classify them differently from their prior FinCEN‑centric assumptions.

5. **2023–2025 – MPC-specific legal commentary and industry concern**  
   - Law firms and trade associations publish analyses highlighting the ambiguity for MPC architectures under broadened control definitions [Source: S. Horowitz MPC wallets blog, 2025; Source: Blockchain Association comment letters on state virtual currency bills, 2023–2024].  
   - Providers face increasing pressure from institutional clients to prove that their arrangements are either **fully licensed** or comfortably **non‑custodial**.

### 4.2 Background vs. direct causes

- **Deep background factors**  
  - Dual U.S. system (federal + state) ensures **classification is fragmented by design**, even for non‑crypto activities [Source: CSBS overview of state money transmitter laws, 2019].  
  - Virtual currency technology evolves faster than statutory language; statutes must use technology‑neutral concepts like "control" that are **hard to interpret for novel architectures**.  
  - MPC is conceptually complex; regulators and generalist lawyers have a steep learning curve.

- **Immediate triggers**  
  - Adoption of MTMA language and DFAL-style statutes that explicitly **codify functional control tests**.  
  - Concrete institutional RFPs asking, "Is this MPC provider a money transmitter? Are they a qualified custodian?" and receiving **divergent legal answers**.  
  - Emerging enforcement signals and examination questions where regulators probe veto powers, emergency pause rights, and governance structures.

### 4.3 Root issues

1. **Conceptual gap between cryptography and legal control**  
   Legal frameworks think in terms of **rights and powers**, not key shares and protocols. MPC solves cryptographic single‑point‑of‑failure problems but does not map neatly onto "control" tests baked into money transmitter statutes.

2. **Lack of MPC-specific safe harbors or interpretive examples**  
   FinCEN’s 2019 examples focus on multi-sig but **do not directly address MPC**, leaving regulators to analogize or improvise [Source: FinCEN FIN‑2019‑G001, 2019].

3. **Incentive misalignment**  
   - Providers want flexible architectures and marketing freedom.  
   - Regulators want bright lines and enforceable obligations.  
   - Without **shared design patterns** and safe harbors, each side optimizes separately, producing friction.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

If the industry continues with **ad‑hoc legal opinions, bespoke no-action requests, and uncoordinated advocacy**:

- More states are likely to **adopt MTMA or similar control language** because it is the only widely available modern template [Source: CSBS MTMA legislative tracker, 2024].  
- MPC providers face growing pressure to either:  
  - **Obtain full money transmitter licenses** in MTMA states, or  
  - **Geofence** those states and limit service, fragmenting their U.S. footprint.  
- Institutional clients may **delay or scale back MPC adoption**, preferring custodians whose regulatory posture is familiar (e.g., bank trust departments, long‑standing qualified custodians) [Source: State Street custody report, 2025].

Quantitatively, over a 1–3 year horizon, absent coordinated action:

- Number of MTMA or MTMA-like states could easily exceed **25–30**, given current adoption pace [Source: CSBS MTMA updates, 2024].  
- Industry licensing/legal spend likely remains in the **USD 50–100M range**, with significant duplication as each provider repeats analysis [Estimate: scaling current spend patterns from problem statement].  
- MPC wallet market may underperform forecast growth, staying closer to **single‑digit CAGR** instead of the higher growth potential implied by security benefits [Source: Intel Market Research MPC report, 2024].

### 5.2 Early signals

- **Regulatory signals**  
  - Increasing mention of **"control" and "operational ability to prevent transactions"** in state bills and bulletins (DFAL, Rhode Island guidance) [Source: CA DFAL debates, 2023; Source: Rhode Island Banking Bulletin 2022‑2].  
  - FinCEN examinations raising questions about **how MPC providers monitor and control transactions** in practice.

- **Market signals**  
  - Institutional RFPs and DDQs explicitly ask for **state licensing maps** and explanations of how MPC providers interpret control tests.  
  - Some large providers start **over‑licensing** (taking more state MT licenses than they strictly believe necessary) to ease institutional concerns, a sign of classification anxiety.

- **Behavioral signals**  
  - Legal and compliance conferences begin hosting **panels on MPC custody classification**, suggesting rising concern.  
  - Providers adjust product roadmaps to reduce or modularize veto powers in ways that can be **assigned to clients or third parties**.

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario (≈25%)**  
  - FinCEN issues **clarifying MPC guidance** or FAQs building on the 2019 document, distinguishing clearly between MPC models that are and are not money transmitters.  
  - CSBS publishes practical **MPC case studies** for MTMA, and several states incorporate them into supervisory guidance.  
  - Result: ≤5 standard classification patterns; MPC adoption by institutions accelerates; industry spend focused on **implementation, not litigation** [Source: extrapolation from prior guidance cycles, e.g., FinCEN prepaid card guidance timeline, 2011–2013].

- **Baseline scenario (≈50%)**  
  - No single federal MPC guidance; instead, **patchwork of state interpretations** emerges, partially harmonized via CSBS forums.  
  - Larger providers secure informal or state‑specific comfort; smaller providers face greater barriers.  
  - Institutional adoption grows, but slower and concentrated among a few **regulatory front‑runners**.

- **Pessimistic scenario (≈25%)**  
  - One or more MPC‑linked incidents (e.g., loss, fraud, or AML failures) prompt **reactive enforcement and restrictive interpretations** of control.  
  - Multiple states move quickly to classify most MPC providers as money transmitters by default, with limited nuance.  
  - Result: Many providers exit or geofence the U.S.; institutional custody consolidates among a few highly capitalized players.

(Probabilities are rough expert estimates and should be treated as **hypotheses requiring validation**, not measured forecasts.)

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Technical & analytical capability**  
  - Major MPC providers employ strong cryptography and security teams and already produce **detailed technical whitepapers and SOC reports** to win institutional mandates [Source: Fireblocks/BitGo technical whitepapers, 2023–2024].  
  - Many have experience engaging with regulators in other contexts (e.g., exchange licensing, trust charters).

- **Collective industry voice**  
  - Trade associations have **proven ability to coordinate comment letters** and testify on digital asset bills at both state and federal levels [Source: Blockchain Association comment letters, 2022–2024].  
  - CSBS provides an existing venue for **state supervisors to coordinate**, creating a natural counterpart for industry proposals.

- **Regulatory precedent base**  
  - There is already a written body of guidance (FinCEN 2013, 2019; MTMA text; DFAL) that can be reused to build **concrete examples and safe harbors** rather than starting from scratch.

### 6.2 Capability gaps

- **Shared taxonomy and patterns**  
  - No **standardized taxonomy** of MPC control patterns (e.g., "client‑only veto", "provider veto", "shared veto", "no veto") mapped to likely regulatory outcomes. Each provider explains its own model differently, increasing regulator confusion.

- **Legal-technical translation**  
  - Many engineering teams cannot easily translate MPC details into **plain-language explanations** of who has what power in regulatory terms, and many lawyers cannot interpret MPC protocols [Source: S. Horowitz MPC wallets blog, 2025].

- **State‑by‑state intelligence**  
  - Providers and trade associations lack a **continuously maintained, public mapping** of which states treat which MPC patterns as money transmission vs. non‑custodial.

### 6.3 Buildable capabilities (1–6 months)

- **MPC control pattern catalog (P0/P1)**  
  - Create a **shared playbook** describing standard MPC architectures and mapping them to potential regulatory classifications, with both technical diagrams and legal analysis.  
  - Could be built in 3–4 months by a working group of 5–10 providers plus 2–3 law firms.

- **Regulatory engagement templates (P1)**  
  - Develop **standard briefing packs** (one‑pagers, slide decks) explaining MPC control allocation and proposing **tiered obligations**.  
  - These can significantly reduce marginal effort per state or federal meeting.

- **Industry data room (P1)**  
  - Aggregate and anonymize **incident, near‑miss, and exam question data** related to MPC custody, to give regulators a clearer evidence base.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

**Background**

- Dual U.S. federal/state system; FinCEN CVC guidance defines MSB scope but does not explicitly address MPC.  
- CSBS MTMA introduces a **functional control test** that some states adopt wholesale.  
- MPC architectures distribute key material but often centralize operational veto/execute power in the provider’s platform.

**Problem**

- Ambiguity whether MPC providers are **money transmitters and/or custodians** under different regimes.  
- Inconsistent classification across states → high legal costs, risk of retroactive enforcement, and lost institutional opportunities.

**Analysis**

- Internal logic: tradeoffs among security, operational control, and regulatory classification.  
- External connections: interplay of FinCEN, CSBS, individual states, and international regimes (MiCA, MAS, FCA).  
- Origins: path from early multi‑sig guidance to MTMA to current MPC concerns.

**Options**

- Accept broad control definitions and **license widely**.  
- Argue for **narrow safe harbors** (no unilateral control → non‑custodial).  
- Propose **tiered classification** tied to architecture patterns and operational rights.  
- Modify MPC designs to **minimize provider veto power** and share or shift control to clients/independent trustees.

**Risks & follow‑ups**

- Overly restrictive interpretations that chill innovation and centralize custody.  
- Insufficient regulatory clarity leading to enforcement risk.  
- Coordination failure among providers delaying guidance.

### 7.2 Key judgments (requiring validation)

1. **Judgment 1 – Veto rights are the primary regulatory control signal**  
   Hypothesis: For MPC architectures, regulators care **more about who can block/approve transactions** than about who holds key material.  
   - If true, design patterns that allocate veto power away from providers enable non‑custodial classifications under MTMA tests.  
   - Needs validation via **direct dialogues with multiple state regulators** using concrete MPC examples.

2. **Judgment 2 – Tiered classification is feasible**  
   Hypothesis: States and FinCEN will accept a **tiered model** (e.g., support‑only vs. co‑custody vs. full custody) instead of binary custodial/non‑custodial splits.  
   - Requires evidence from other jurisdictions (e.g., MiCA, MAS) where such tiering is in practice.  
   - Needs validation through policy consultations and pilot supervisory cases.

3. **Judgment 3 – Industry coordination can significantly cut cost and time**  
   Hypothesis: A coordinated working group can **halve the aggregate cost and time** to secure clarity vs. each provider acting alone.  
   - Validate by comparing prior joint initiatives (e.g., travel rule standards, stablecoin comment efforts) with fragmented approaches.

### 7.3 Alternative paths (preview)

- **Path A – Broad licensing**: treat MPC providers as money transmitters/custodians in most jurisdictions and build compliance infrastructure accordingly.  
- **Path B – Pattern‑based safe harbors**: define MPC patterns that clearly fall outside money transmission or qualify as limited custodians.  
- **Path C – Hybrid**: license certain roles (e.g., central orchestrator) while carving out purely client‑controlled MPC nodes.  
- **Path D – Design‑first**: redesign MPC products to minimize or eliminate provider unilateral control, aiming to fit comfortably into non‑custodial categories.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Technology optimism bias** – Assuming regulators will readily understand and accept nuanced MPC patterns once explained. In reality, simpler bright lines may be preferred [Source: comparative experiences with complex derivatives and shadow banking regulation, BIS, 2015–2020].
- **Coordination optimism bias** – Overestimating industry’s ability to maintain a unified position when some providers profit from ambiguity (e.g., by marketing "non‑custodial" aggressively).
- **U.S.-centric bias** – Underweighting the influence of **MiCA and other major frameworks** that could eventually shape U.S. thinking via global harmonization pressure.

### 8.2 Required intelligence

Key information gaps that should be filled before finalizing a strategy:

1. **Regulator stance mapping**  
   - For ≥15 key states (by market size), gather documented or interview-based views on:  
     - Whether MPC providers with unilateral veto rights are money transmitters.  
     - Whether shared veto among independent parties changes classification.  
   - Method: targeted meetings and follow‑up memoranda.

2. **Comparative law analysis**  
   - Deep dive into **MiCA, MAS, UK FCA, and Japan FSA** custody classifications to identify patterns (e.g., risk-based tiering, operational vs. legal control) [Source: MiCA; MAS DPT Guidelines; UK FCA PS23/10].

3. **Market sensitivity**  
   - Surveys/interviews with institutional clients quantifying:  
     - How much regulatory certainty they require (e.g., licenses vs. opinions vs. no-action letters).  
     - Relative priority of control classification vs. other factors (operational resilience, cybersecurity, service quality).

### 8.3 Validation plan

- **Phase 1 (0–3 months)**  
  - Conduct **state regulator soundings** (5–8 states including at least two MTMA adopters) using example MPC diagrams.  
  - Commission **comparative law memo** on custody/control concepts across U.S., EU, UK, and Singapore.  
  - Run **institutional client survey** via trade association.

- **Phase 2 (3–9 months)**  
  - Use insights to draft **pattern‑based classification proposals** (Path B/C) and socialize them with CSBS and FinCEN.  
  - Pilot at least one **"low-control MPC" architecture** with a willing regulator via sandbox or innovation hub.

- **Phase 3 (9–18 months)**  
  - Seek formal recognition of either **safe harbor patterns** or **tiered classifications** in at least two key states and, ideally, in a FinCEN FAQ or guidance update.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revision areas

- **Timelines** – 6–18 month estimates for guidance may slip if other regulatory priorities intervene (e.g., stablecoins or DeFi enforcement waves).  
- **Feasibility of safe harbors** – Regulators may instead favor **case‑by‑case no-action letters** rather than published, general safe harbors.

### 9.2 Incremental approach

- Start with **low‑risk, low‑control MPC patterns** (e.g., client‑controlled veto, provider as stateless co‑signer) when engaging regulators, then expand to more complex architectures.  
- Pilot **state-level recognition** before aiming for federal-level MPC guidance.

### 9.3 "Good enough" criteria

The strategy is good enough to act on if:

1. At least **3–5 major states** (including 2 MTMA adopters) explicitly accept a **pattern‑based classification** for one or more MPC architectures.  
2. Institutional clients treat these recognitions as sufficient to proceed with deployments (evidenced by RFP outcomes).  
3. Aggregate legal/compliance cost is demonstrably **lower** than full 50‑state licensing while keeping enforcement risk within acceptable bounds.

---

## 10. Summary & Action Recommendations

### 10.1 Core insights

1. The core classification issue is not whether MPC providers hold full private keys but **who has functional veto/execute power over transactions** under MTMA-style control tests.  
2. Existing guidance (FinCEN 2019, MTMA, DFAL) provides building blocks, but **no MPC-specific safe harbors or patterns** – leaving a vacuum filled by expensive bespoke opinions and uneven state practice.  
3. A **pattern‑based, tiered classification** for MPC roles can reconcile security innovation with consumer protection and AML objectives, but requires coordinated industry engagement and comparative law evidence.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric (baseline → target) → Date**

1. **【P0 – Critical】 Map state & federal views on MPC control**  
   → Trade association + 3–5 lead MPC providers  
   → **Metric**: 0 public mappings → ≥10 states + FinCEN summarized in an internal matrix  
   → **Target date**: 2025‑03‑31.

2. **【P0 – Critical】 Design MPC control pattern catalog**  
   → Joint working group (providers + law firms)  
   → **Metric**: 0 standardized patterns → ≥5 well‑specified MPC control archetypes with legal analysis  
   → **Target date**: 2025‑04‑30.

3. **【P1 – Important】 Launch comparative custody/control study across U.S./EU/UK/SG**  
   → External counsel / academic partner  
   → **Metric**: no cross‑regime view → 1 consolidated report citing at least 8–12 primary regulatory sources  
   → **Target date**: 2025‑05‑31.

4. **【P1 – Important】 Engage CSBS and at least two state regulators on pattern-based guidance**  
   → Trade associations + select providers  
   → **Metric**: 0 formal engagements → ≥3 structured meetings with follow‑up minutes  
   → **Target date**: 2025‑06‑30.

5. **【P2 – Optional】 Prepare draft MPC-specific FAQ requests for FinCEN**  
   → Legal working group  
   → **Metric**: 0 drafts → 1–2 well‑supported FAQ request packages referencing 2019 guidance and MTMA  
   → **Target date**: 2025‑06‑30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Overly restrictive state interpretations classify most MPC providers as money transmitters by default | High | Medium | Multiple states issue bulletins explicitly stating that any MPC veto power = control | Propose **tiered obligations** and **limited-control categories**; highlight security benefits of MPC vs. legacy models | Trade associations |
| Coordination failure among providers (no common position) | Medium | Medium | Working group fails to agree on pattern catalog or advocacy priorities | Use **neutral facilitator**; start with narrow consensus (low‑control patterns) and iterate | Industry working group |
| Institutional clients deem state-level clarity insufficient without federal clarification | High | Medium | RFPs or DDQs insist on FinCEN‑level MPC recognition | Prepare **FinCEN FAQ proposals** backed by state examples and cross‑regime analysis; explore **bank/trust charters** as alternative route | Large MPC providers |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Broad licensing** | Maximizes legal certainty; simple story for institutions | High upfront & ongoing licensing/compliance costs; raises entry barriers | Consolidates market; may stifle smaller innovators | Provider has large balance sheet and prefers conservative posture | Budget‑constrained providers; rapidly evolving product features |
| **B. Pattern-based safe harbors** | Aligns obligations with actual control risks; preserves innovation; scalable across providers | Requires heavy initial legal and advocacy investment; depends on regulator openness | Regulators may prefer bright‑line rules; risk of patchwork adoption | Regulators are willing to experiment; strong trade association support | Fragmented industry with no shared view; regulators in crisis mode |
| **C. Hybrid licensing (role-specific)** | Targets obligations on the roles that truly control assets; flexible across architectures | Complexity in explaining roles; potential gray areas remain | Misclassification of some roles; client confusion | Providers can cleanly separate orchestration from client/trustee roles | Architectures tightly coupled with provider‑controlled vetoes |
| **D. Design-first minimization of provider control** | Reduces likelihood that provider is deemed to have control; may fit existing non‑custodial precedents | May reduce operational flexibility (e.g., emergency freezes); implementation complexity | Security or resilience tradeoffs if design rushed | New products still in design phase; clients willing to hold more control | Legacy platforms where provider veto is crucial operational safeguard |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **AML (Anti-Money Laundering)** | Regulatory framework requiring financial institutions and MSBs to detect, prevent, and report money laundering and related crimes | N/A | Based on BSA and FinCEN regulations [Source: FinCEN, BSA regulations overview, 2020] |
| **Control (FinCEN 2019)** | For CVC money transmitter analysis, whether an intermediary has **"total independent control"** over value, i.e., unilateral ability to access and move customer funds without consent | N/A | Summarized from FinCEN FIN‑2019‑G001 multi-sig discussion [Source: FinCEN CVC Guidance, 2019] |
| **Control (MTMA Article XIII)** | "Power to execute unilaterally, or prevent indefinitely, a virtual currency transaction"; functional test used to determine money transmission status under MTMA | N/A | Statutory language in MTMA Article XIII §13.06 [Source: CSBS MTMA, 2020] |
| **Custodial wallet** | Wallet or arrangement where a third party has control over the user’s assets and is responsible for safekeeping and often regulatory compliance | N/A | Common across custody regulations [Source: SEC Custody Rule interpretations, 2017] |
| **DFAL (Digital Financial Assets Law)** | California law regulating digital financial asset businesses, incorporating MTMA concepts for virtual currency supervision | N/A | [Source: California DFAL statutory text and analyses, 2023] |
| **MPC (Multi-Party Computation) wallet** | Wallet architecture where private keys are replaced by distributed secret shares; transactions are signed via threshold protocols without reconstructing the full key in one place | N/A | [Source: MPC threshold signature literature, ACM CCS/Crypto 2018–2023] |
| **Money transmitter (U.S.)** | Person engaged in the business of accepting and transmitting currency, funds, or value that substitutes for currency, typically requiring AML program, registration, and often state licenses | N/A | [Source: FinCEN regulations 31 CFR §1010.100(ff), 2011] |
| **MTMA (Money Transmission Modernization Act)** | Model state law created by CSBS to harmonize money transmitter regulation; includes Article XIII on virtual currency | N/A | [Source: CSBS MTMA documentation, 2020] |
| **Non-custodial service** | Service where the user retains primary control over private keys or equivalent control rights, and the provider cannot unilaterally move or indefinitely block user assets | N/A | Synthesized from FinCEN 2019 multi-sig analysis and industry practice |
| **Qualified custodian** | Entity meeting specific regulatory requirements to hold client assets (e.g., under SEC Custody Rule 206(4)-2 for investment advisers), often a bank, registered broker-dealer, or certain foreign financial institutions | N/A | [Source: SEC Custody Rule 206(4)-2, 17 CFR §275.206(4)-2] |

---

## 12. References

### Tier 1 – Primary legal and regulatory sources

1. **FinCEN**. (2013). *Application of FinCEN’s Regulations to Persons Administering, Exchanging, or Using Virtual Currencies*. U.S. Department of the Treasury.  
2. **FinCEN**. (2019). *Application of FinCEN’s Regulations to Certain Business Models Involving Convertible Virtual Currencies* (FIN‑2019‑G001).  
3. **CSBS**. (2020). *Money Transmission Modernization Act (MTMA)* – Article XIII: Virtual Currency.  
4. **California Legislature**. (2023). *Digital Financial Assets Law (DFAL)* – Statutory text and committee analyses.  
5. **European Union**. (2023). *Regulation (EU) 2023/1114 on Markets in Crypto‑assets (MiCA)*.  
6. **SEC**. (2017). *Custody of Funds or Securities by Investment Advisers* (Rule 206(4)-2) and related guidance.  
7. **FinCEN**. (2020). *Bank Secrecy Act Regulations – Overview of Money Services Business Requirements*.  

### Tier 2 – Secondary analyses and industry reports

8. **S. Horowitz Law Firm**. (2025). *Multi-Party Computation (MPC) Wallets and the Evolving Regulatory Landscape in the United States*.  
9. **Intel Market Research**. (2024). *MPC (Multi-Party Computation) Wallet Development Market Growth 2025–2032*.  
10. **State Street**. (2025). *The Future of Digital Asset Custody: Building Trust at Scale*.  
11. **Blockchain Association & Industry Comment Letters**. (2022–2024). Various submissions on state virtual currency and custody bills.  

### Tier 2 – International guidance (custody & virtual assets)

12. **Monetary Authority of Singapore (MAS)**. (2021). *Guidelines on Provision of Digital Payment Token Services to the Public*.  
13. **UK Financial Conduct Authority (FCA)**. (2023). *Policy Statement PS23/10: Financial Promotion Rules for Cryptoassets* (including custody‑related expectations).  
14. **Japan Financial Services Agency (FSA)**. (2020–2023). *Guidelines for Crypto‑Asset Service Providers* (custody and segregation provisions).  

### Estimates & assumptions (not authoritative citations)

15. **Industry compliance cost estimates and scenario probabilities**.  
    - Method: scaling typical MSB licensing and legal expenses from public and practitioner sources across ≈15 providers and 50 states; applying expert judgment for scenario probabilities; to be validated via targeted cost surveys and regulatory engagement outcomes.

(Each section’s inline citations correspond to the above sources by descriptive title; numbers here are for convenience and do not change the inline format requirement.)
