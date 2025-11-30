# Protocol Fragmentation and Lack of Standardization in MPC Wallet Ecosystem – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Protocol Standards Team  
**Related Problem**: `../10_Protocol_Fragmentation_Standardization.md`

---

## Context Recap

- **Problem title**: Protocol Fragmentation and Lack of Standardization in MPC Wallet Ecosystem
- **Current state**:
  - Multiple incompatible MPC threshold signature schemes (Lindell17, GG18/GG20, CGGMP21, FROST) are deployed in production without common standards for key share formats, APIs, or security disclosures [Source: Fast Secure Two-Party ECDSA Signing, Lindell, 2017, ePrint 2017/552; Source: Fast Multiparty Threshold ECDSA with Fast Trustless Setup, Gennaro & Goldfeder, 2019, ePrint 2019/114; Source: UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts, Canetti et al., 2021, ePrint 2021/060].
  - 15+ MPC wallet providers expose proprietary APIs and protocol variants, forcing exchanges and protocols to integrate each provider separately [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].
  - No portable encrypted key share format exists; switching providers typically requires generating new keys and migrating assets on-chain [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].
- **Pain points (quantified where possible)**:
  - **Vendor lock-in**: Users and institutions cannot migrate MPC key shares between providers; migration requires new keys and on-chain transfers with gas costs estimated at $100–$500 per institution depending on portfolio size [Estimate: based on 10–50 transactions × $10–$50 gas each].
  - **Integration overhead**: Each exchange/protocol spends ~200–500 engineering hours per provider integration; supporting 15+ providers can cost 3,000–7,500 hours ecosystem-wide [Estimate: based on typical complex API/security integrations].
  - **Security opacity**: GG18/GG20 vulnerabilities and different abort models across protocols are hard for customers to compare without standardized disclosures [Source: Practical Key-Extraction Attacks in Leading MPC Wallets, Fireblocks, 2023; Source: MPC does have a single point of failure, Cubist, 2024].
- **Goals**:
  - Establish a protocol-agnostic standardization layer (interfaces, key formats, migration flows, security disclosure) with meaningful adoption by major providers and integrators.
  - Enable safe, low-friction key share portability, reduce integration effort, and improve security transparency.
- **Hard constraints**:
  - Time window roughly Q1 2026–Q4 2027 for consortium formation and first widely adopted standard.
  - Budget envelope ~$3M–$8M ecosystem-wide for standards work and implementation.
  - Backward compatibility: existing deployed keys and custody setups must remain functional; migration cannot force mass key regeneration.
- **Key facts from problem statement**:
  - Threshold ECDSA/Schnorr schemes are well-studied but currently deployed in incompatible ways [Source: Lindell, 2017; Source: Gennaro & Goldfeder, 2019; Source: Canetti et al., 2021].
  - Protocol fragmentation affects ~100M+ users and ~$50B+ assets across consumer and institutional segments [Estimate: extrapolated from large custodians’ public AUM and user counts].

---

## 1. Problem Definition (Aspect 1) 【Core】

### 1.1 Problem & contradictions

1. **Core contradiction**
   - The ecosystem wants **high-assurance, cutting-edge MPC protocols** while simultaneously requiring **interoperability, portability, and low integration cost**. Today, protocol and implementation diversity are achieved via proprietary designs that **directly block interoperability**.
   - Providers differentiate through protocol choice and implementation optimizations, but customers and integrators demand a commodity-like interface and migration path similar to WebAuthn or ERC standards [Source: W3C WebAuthn Level 2, W3C, 2021; Source: Ethereum Improvement Proposals (ERC standards), Ethereum Foundation, accessed 2025].

2. **Key tensions**
   - **Differentiation vs. standardization**: Vendors fear losing competitive edge if APIs and key formats are standardized, yet customers and regulators push for portability and risk transparency.
   - **Security vs. interoperability**: Some providers worry that shared formats or migration protocols could introduce new attack surfaces; however, lack of standards already enables insecure legacy protocols to persist (e.g., vulnerable GG18/GG20 deployments) [Source: Fireblocks key-extraction disclosure, 2023].
   - **Short-term cost vs. long-term efficiency**: Implementing standards requires near-term engineering and audit investment, whereas the benefits (reduced integration cost, easier migration, better security coordination) accrue across the entire ecosystem over several years [Estimate: based on historical adoption of TLS and WebAuthn-style standards].

### 1.2 Goals & conditions

- **Primary goals (from problem file)**:
  - **Standardization**: Create at least one recognized MPC wallet standards consortium with ≥10 major providers by Q4 2026.
  - **Interoperability**: Achieve encrypted key share portability with ≥50% of major providers supporting a common migration format by Q4 2027.
  - **API consistency**: Reach ≥60% of exchanges/protocols using a standardized MPC wallet integration interface by Q4 2027.
  - **Integration efficiency**: Reduce combined integration effort from 3,000–7,500 hours to <1,000 hours for multi-provider support.
  - **Security transparency**: Ensure 100% of participating providers disclose protocol choice, round complexity, vulnerability history, and certification status.

- **Conditions / non-negotiables**:
  - No degradation in cryptographic security guarantees relative to best-practice protocols (e.g., CGGMP21-class security for ECDSA) [Source: Canetti et al., 2021, ePrint 2021/060].
  - Migration flows must preserve confidentiality and integrity of key shares (e.g., end-to-end encrypted transfer, rigorous authentication between providers).
  - Standards must be neutral regarding specific threshold protocols; they should support Lindell17, CGGMP21, FROST, and future schemes via capability negotiation.

### 1.3 Extensibility & reframing

- **Reframing along attributes**
  - Instead of “which MPC protocol is best,” reframe as **“how to define portable abstractions and assurance levels across protocols”**.
  - Treat protocol as a pluggable attribute behind a standard interface, with declared properties (rounds, security assumptions, known issues).

- **Reframing along structure**
  - **Virtual vs. physical**: Physical key shares never leave provider HSM/MPC clusters; “virtual portability” is achieved through standardized encrypted re-sharing or re-keying protocols.
  - **Positive vs. negative framing**: From “fragmentation problem” to “interoperability opportunity” that unlocks multi-provider resilience, lower systemic risk, and better regulatory alignment [Source: FIDO Alliance mission statement, accessed 2025].

---

## 2. Internal Logical Relations (Aspect 2) 【Core】

### 2.1 Key elements

- **Roles**:
  - MPC wallet providers (custody, SDK vendors).
  - Integrators (exchanges, DeFi protocols, payment processors).
  - End users (retail, institutional).
  - Standards/certification bodies and security auditors.
- **Resources**:
  - Deployed threshold signature protocols and implementations.
  - Provider APIs, SDKs, key management backends.
  - Cryptographic expertise and audit capacity.
- **Processes**:
  - Key generation and share distribution.
  - Signing workflows (online/offline parties, quorum policies).
  - Incident response and vulnerability patching.
  - Migration or sunsetting of protocols.
- **Rules**:
  - Provider-specific operational and security policies.
  - Regulatory requirements for custody, KYC, and operational risk.

### 2.2 Balance & “degree”

- **Protocol diversity vs. standardization**:
  - Too little diversity → systemic risk if one protocol or implementation is compromised (software monoculture) [Source: MPC does have a single point of failure, Cubist, 2024].
  - Too much diversity without standards → extreme integration overhead and vendor lock-in.
  - **Desired degree**: Diversity at **implementation/protocol level**, standardization at **interface, migration, and assurance reporting level**.

- **Security vs. usability**:
  - Stronger security (e.g., more signing rounds, advanced protections) can increase latency and complexity.
  - Standards must allow expressing latency and security trade-offs to integrators in a comparable way, not force a single “best” protocol.

### 2.3 Causal chains

1. **Fragmentation → Higher integration cost → Reduced competition**
   - Proprietary APIs and key formats → each new provider costs 200–500 hours to integrate → smaller exchanges support fewer providers → providers with early integrations gain disproportionate market power.

2. **Lack of migration paths → Vendor lock-in → Slower security upgrades**
   - No portable key share format → switching requires new keys and on-chain asset migration → institutions avoid switching even when better protocols (e.g., CGGMP21) exist → vulnerable or suboptimal protocols persist longer [Source: Fireblocks key-extraction disclosure, 2023; Source: Canetti et al., 2021].

3. **No shared disclosure standard → Inconsistent risk understanding**
   - Each provider describes security model differently → customers cannot compare guarantees (e.g., round complexity, abort behavior, side-channel resistance) → purchasing decisions based on marketing, not verifiable properties.

---

## 3. External Connections (Aspect 3) 【Core】

### 3.1 Stakeholder map

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream (cryptography researchers, standards bodies) | Design protocols and potential standards | Maximize security, formal guarantees, and adoption | Limited insight into production constraints; volunteer-driven processes | May push for ideal but hard-to-implement standards that vendors resist |
| Downstream (exchanges, DeFi protocols, custodians) | Integrate MPC wallets and manage assets | Reduce integration cost, ensure security, avoid lock-in | Limited security expertise; regulatory pressure; time-to-market | Want interoperability that vendors may resist; may under-invest in due diligence |
| Sideline/external (regulators, auditors, insurers) | Oversee systemic risk, consumer protection | Clear, comparable security information; migration safety | Lack deep MPC expertise; evolving regulations | May mandate standards faster than ecosystem can adopt |

### 3.2 Environment factors

- **Regulatory**:
  - Increasing scrutiny on digital asset custody and operational resilience; regulators often favor standardized controls and auditable certification schemes [Source: Emerging digital asset custody guidelines, multiple financial regulators, 2023–2024].
- **Market**:
  - Growing institutional participation and AUM push for vendor optionality and risk diversification.
  - Competitive landscape among MPC vendors incentivizes innovation but discourages open standards without clear incentives.
- **Technology**:
  - Active research in threshold ECDSA/Schnorr and post-quantum MPC; standards must adapt over time.
  - Hybrid architectures (MPC + smart contracts) are emerging, which further complicates interoperability [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].

### 3.3 Responsibility & room

- **Where to take proactive responsibility**:
  - Large providers and major exchanges should seed a working group, contribute reference implementations, and co-fund audits.
  - Early adopters should pilot portable key formats and migration flows.

- **Where to leave flexibility**:
  - Allow providers to choose internal MPC protocols as long as they publish minimum required disclosures and pass certification.
  - Support optional advanced features (e.g., proactive refresh, post-quantum schemes) as extensions rather than requirements.

---

## 4. Origins of the Problem (Aspect 4) 【Advanced】

### 4.1 Historical nodes

1. **2017–2019: First production MPC deployments**
   - Lindell17 and GG18 introduced practical threshold ECDSA schemes and were rapidly adopted by early MPC wallet vendors without coordination on interoperability [Source: Lindell, 2017, ePrint 2017/552; Source: Gennaro & Goldfeder, 2019, ePrint 2019/114].
2. **2020–2022: Protocol evolution without migration paths**
   - GG20 and CGGMP21 improved security and performance but required non-trivial reimplementation; no common migration format existed, locking early adopters into older protocols [Source: Gennaro & Goldfeder, 2020; Source: Canetti et al., 2021].
3. **2023: Public disclosure of GG18/GG20 issues**
   - Key-extraction vulnerabilities showed the cost of heterogeneous, opaque implementations and lack of coordinated update mechanisms [Source: Fireblocks key-extraction disclosure, 2023].
4. **2024–2025: Hybrid wallets and social recovery**
   - Hybrid architectures and diverse recovery schemes further fragmented the ecosystem, each with proprietary formats and no portability [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].

### 4.2 Background vs. direct causes

- **Background causes**:
  - Crypto markets prioritized **speed to market** and differentiation over standardization, especially pre-2020.
  - No widely recognized MPC-specific standards body emerged to coordinate research and industry.

- **Direct causes**:
  - Providers implemented protocols in isolation with custom APIs and storage formats.
  - Lack of migration-focused research and product design (e.g., encrypted re-sharing across providers) in early stages.

### 4.3 Root issues

- Misaligned incentives: Vendors benefit short-term from lock-in; ecosystem benefits long-term from interoperability.
- Coordination failure: No neutral forum combining researchers, vendors, and regulators to align on requirements and migration strategies.
- Underinvestment in “boring plumbing”: Migration formats, assurance schemas, and test harnesses are non-differentiating but critical.

---

## 5. Problem Trends (Aspect 5) 【Core】

### 5.1 Current trajectory (if unchanged)

- **Fragmentation persists**: More vendors and protocol variants enter the market, each adding their own APIs.
- **Security risk**: Legacy schemes remain in production because migration is costly and risky; coordinated vulnerability response remains ad-hoc [Source: Fireblocks key-extraction disclosure, 2023].
- **Regulatory pressure grows**: Regulators may eventually impose standards or certification, but potentially in a way misaligned with technical best practice if industry does not self-organize.

### 5.2 Early signals

- Public disclosure of GG18/GG20 vulnerabilities highlighted cross-vendor dependencies and communication gaps.
- Increasing institutional RFPs that ask about vendor lock-in, portability, and third-party audits suggest demand for standardization [Estimate: based on pattern of enterprise RFP evolution in other security domains].
- WebAuthn/FIDO-style initiatives in adjacent authentication domains demonstrate regulators’ and enterprises’ preference for interoperable security [Source: W3C WebAuthn Level 2, W3C, 2021; Source: FIDO Alliance overview, accessed 2025].

### 5.3 Scenarios (6–24 months)

- **Optimistic**:
  - 10–15 major vendors and 5–10 exchanges form an MPC Wallet Standards Working Group.
  - A v1 spec for portable key formats and minimal security disclosures is published and piloted.
  - 30–50% of new integrations adopt the common interface.

- **Baseline**:
  - A de facto standard emerges around 2–3 major providers’ APIs without formal consortium backing.
  - Some bilateral migration agreements appear, but remain proprietary and non-generalizable.

- **Pessimistic**:
  - Fragmentation deepens; no shared standards or migration formats.
  - One or more major incidents (e.g., protocol vulnerability or migration failure) triggers reactive regulatory intervention, potentially imposing heavy-handed requirements misaligned with cryptographic best practices.

---

## 6. Capability Reserves (Aspect 6) 【Advanced】

### 6.1 Existing strengths

- **Technical expertise**: Multiple vendors employ cryptographers familiar with threshold schemes and secure implementations [Source: vendor technical blogs and hiring patterns, 2023–2025].
- **Precedent standards**: WebAuthn, FIDO, and ERC standards provide blueprints for multi-stakeholder standardization.
- **Audit ecosystem**: Established security firms already audit MPC implementations and can contribute to certification criteria.

### 6.2 Capability gaps

- **Standards engineering**: Few teams have experience turning research protocols into stable, widely adopted interface and migration standards.
- **Formal threat modeling for migration**: The ecosystem lacks widely accepted models for threats during inter-provider key share migration (e.g., MITM, downgrade attacks).
- **Incentive design**: Limited capability to design economic and governance mechanisms that make participation in standards attractive.

### 6.3 Buildable capabilities (1–6 months)

- Secondment of cryptographers and security engineers from major vendors into a neutral working group.
- Engagement with experienced standards contributors from W3C/FIDO-style communities as advisors.
- Commissioning of threat modeling and reference migration protocol designs from expert security consultancies.

---

## 7. Analysis Outline (Aspect 7) 【Advanced】

### 7.1 Structured outline

- **Background**: Rapid adoption of diverse MPC protocols without interoperability planning.
- **Problem**: Fragmentation causing lock-in, integration overhead, and opaque security postures.
- **Analysis**: Stakeholder incentives, causal chains, risk scenarios, and capability gaps.
- **Options**: Do nothing; vendor-led bilateral agreements; formal consortium and open standards.
- **Risks**: Coordination failure, security regression, partial adoption, regulatory misalignment.

### 7.2 Key judgments (need validation)

1. Standardization can be achieved without materially weakening security if scoped to interfaces, formats, and disclosures.
2. At least 10 major vendors and several exchanges have enough aligned incentives to invest in a consortium.
3. Institutions will reward vendors that support portability (e.g., via RFP preferences), offsetting the fear of commoditization.

### 7.3 Alternative paths (one-line positioning)

- **Option A – Status quo**: Preserve maximum vendor freedom; accept fragmentation and lock-in.
- **Option B – De facto standard via few large vendors**: Allow top providers’ APIs to become informal standards.
- **Option C – Formal standards consortium**: Create protocol-agnostic standards and certification with broad participation.

---

## 8. Validating the Answer (Aspect 8) 【Advanced】

### 8.1 Potential biases

- **Ecosystem-optimistic bias**: Assuming vendors will cooperate when incentives may be weaker than expected.
- **Standards-overconfidence bias**: Overestimating the benefits of standardization while underestimating governance and implementation complexity.

### 8.2 Required intelligence

- Empirical data on **integration cost per provider** across a representative sample of exchanges.
- Survey or interview data on **vendor attitudes toward portability and lock-in**.
- Regulator feedback on **likely requirements** for digital asset custody standards in the next 3–5 years.

### 8.3 Validation plan

- Conduct 8–12 stakeholder interviews (providers, exchanges, regulators, auditors) to validate incentives and constraints.
- Commission a small proof-of-concept for **encrypted key share migration** between two cooperating vendors and measure complexity, performance, and security review effort.
- Run an RFP-style pilot where portability support is explicitly scored to test whether it meaningfully affects vendor selection.

---

## 9. Revising the Answer (Aspect 9) 【Advanced】

### 9.1 Likely revisions

- The **scope and pace** of standardization may change once stakeholder interviews clarify incentives.
- The **technical design** of migration formats may be revised as new attack vectors or performance constraints are discovered.

### 9.2 Incremental approach

- Start with **minimal, low-risk standards**:
  - Common terminology and security disclosure templates.
  - A reference schema for describing MPC protocols (rounds, assumptions, known issues).
- Then iterate toward **portable key formats and migration protocols** once trust and experience are built.

### 9.3 “Good enough” criteria

- A v1 standard is acceptable if it:
  - Covers ≥60–70% of current use cases.
  - Has at least 3 independent, production-ready implementations.
  - Passes security review by at least 2 reputable audit firms.
  - Is adoptable with <6 months engineering work for a typical vendor.

---

## 10. Summary & Action Recommendations (Aspect 10) 【Core】

### 10.1 Core insights

1. Protocol fragmentation in MPC wallets is primarily a **coordination and incentive** problem, not a fundamental cryptographic limitation.
2. Lack of standardized interfaces, migration paths, and security disclosures causes significant vendor lock-in, integration overhead, and security opacity.
3. Precedents like WebAuthn, FIDO, and ERC standards demonstrate that **industry-led, protocol-agnostic standardization** is achievable and valued by regulators and enterprises.
4. A phased, low-risk approach (terminology and disclosures → interfaces → migration formats) can unlock benefits while managing risk.

### 10.2 Near-term action list (0–3 months)

1. **【P0 – Critical】 Form exploratory MPC Wallet Standards Working Group**  
   → Owner: Consortium sponsor (e.g., leading provider or neutral foundation)  
   → Metric: ≥8 organizations (3–5 providers, 3–5 exchanges/auditors) sign initial charter by end of Q2 2026  
   → Date: 2026-06-30

2. **【P1 – Important】 Draft common terminology and security disclosure schema**  
   → Owner: Working group editing team  
   → Metric: v0.1 spec covering ≥80% of current MPC wallet use cases; at least 3 providers pilot the schema in public documentation  
   → Date: 2026-09-30

3. **【P1 – Important】 Commission threat model and reference design for encrypted key share migration**  
   → Owner: Technical subcommittee + external security firm  
   → Metric: Threat model document + reference protocol design reviewed by ≥2 independent auditors  
   → Date: 2026-12-31

4. **【P2 – Optional】 Engage regulators and large institutional users in advisory council**  
   → Owner: Consortium governance team  
   → Metric: At least 3 regulators/industry associations and 5 institutional users participate in advisory calls or workshops  
   → Date: 2027-03-31

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Vendor non-participation | High | Medium | Major providers decline to join working group | Design governance with fair voting, IP protection; highlight RFP and regulatory benefits | Consortium steering committee |
| Security regression via poorly designed migration | High | Medium | Vulnerability discovered in migration protocol PoC | Commission independent cryptographic reviews; stage pilots with limited scope; gradual rollout | Technical subcommittee |
| Fragmented or competing standards | Medium | Medium | Multiple groups publish incompatible standards | Seek early alignment with major players; coordinate with existing industry alliances; prefer open, royalty-free specs | Consortium steering committee |
| Regulatory misalignment | High | Low–Medium | New rules mandate incompatible or rigid requirements | Involve regulators early as observers; map standards to regulatory controls; keep documentation transparent | Policy/Regulatory WG |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Status quo (no formal standard)** | Zero coordination overhead; vendors innovate freely | Continued 200–500h/provider integration effort; strong vendor lock-in | Persistent fragmentation; slow coordinated response to vulnerabilities | Short-term, niche markets where a single vendor dominates | When institutional adoption and regulatory scrutiny are growing |
| **B. De facto standard via top vendors** | Faster convergence; reuses existing APIs | Smaller vendors marginalized; limited portability guarantees | Risk of API-level monoculture; opaque governance | When 2–3 vendors already dominate share and are trusted | When ecosystem values neutrality and open participation |
| **C. Formal, open standards consortium** | Vendor-neutral; portable key formats; clear security disclosures; easier regulatory dialogue | Governance overhead; engineering investment for migration and certification | Coordination failure; partial adoption; initial complexity | When ≥10 vendors and major exchanges are willing to collaborate | When ecosystem is too immature or fragmented to agree on baseline |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **MPC (Secure Multi-Party Computation)** | Cryptographic techniques allowing multiple parties to jointly compute functions (e.g., signatures) without revealing their private inputs | N/A | General cryptography concept used in wallet architectures |
| **Threshold Signature Scheme (TSS)** | Signature scheme where any k-of-n parties can jointly sign without reconstructing the full private key | N/A | Foundation of MPC wallets [Source: Gennaro & Goldfeder, 2019] |
| **Lindell17** | Two-party ECDSA MPC protocol commonly used for 2-of-2 MPC wallets | N/A | [Source: Fast Secure Two-Party ECDSA Signing, Lindell, 2017, ePrint 2017/552] |
| **GG18/GG20** | Threshold ECDSA protocols improving scalability and, in GG20, efficiency and abort behavior | N/A | [Source: Gennaro & Goldfeder, 2019; 2020] |
| **CGGMP21** | UC-secure threshold ECDSA protocol with 4-round signing, designed for strong security and practicality | N/A | [Source: Canetti et al., 2021, ePrint 2021/060] |
| **FROST** | Flexible Round-Optimized Schnorr Threshold signatures protocol optimized for Schnorr-based chains | N/A | General description from threshold signature literature |
| **Key share portability** | Ability to securely move encrypted key shares between MPC wallet providers without generating new keys or moving assets on-chain | N/A | Core interoperability goal in this analysis |
| **Vendor lock-in** | Situation where switching providers incurs high cost or risk, effectively binding users to a single vendor | N/A | Observed in current MPC wallet market |
| **WebAuthn** | Web standard that enables interoperable public-key authentication across browsers and authenticators | N/A | [Source: W3C WebAuthn Level 2, W3C, 2021] |
| **FIDO Alliance** | Industry consortium that defines interoperable authentication standards | N/A | Provides precedent for MPC wallet standardization model |

---

## 12. References

### Tier 1 – Research Papers & Protocol Specifications

1. **Lindell, Y.** (2017). *Fast Secure Two-Party ECDSA Signing*. Cryptology ePrint Archive, Paper 2017/552. https://eprint.iacr.org/2017/552  **[Cited in: Context, 4.1, 11]**
2. **Gennaro, R., & Goldfeder, S.** (2019). *Fast Multiparty Threshold ECDSA with Fast Trustless Setup*. Cryptology ePrint Archive, Paper 2019/114. https://eprint.iacr.org/2019/114  **[Cited in: Context, 4.1, 11]**
3. **Canetti, R., Gennaro, R., Goldfeder, S., Makriyannis, N., & Peled, U.** (2021). *UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts*. Cryptology ePrint Archive, Paper 2021/060. https://eprint.iacr.org/2021/060  **[Cited in: Context, 2.3, 4.1, 11]**

### Tier 2 – Security Research & Industry Reports

4. **Fireblocks Research Team.** (2023). *Practical Key-Extraction Attacks in Leading MPC Wallets* (GG18/GG20 Paillier key vulnerabilities). Cryptology ePrint Archive, Paper 2023/1234.  **[Cited in: Context, 2.3, 4.1, 5.1]**
5. **Cubist.** (2024). *MPC does have a single point of failure*. https://cubist.dev/blog/mpc-does-have-a-single-point-of-failure  **[Cited in: Context, 2.2]**
6. **Stackup.** (2025). *MPC Wallets: A Complete Technical Guide*. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide  **[Cited in: Context, 3.2, 4.1]**

### Tier 2 – Standards & Precedents

7. **World Wide Web Consortium (W3C).** (2021). *Web Authentication: An API for accessing Public Key Credentials – Level 2 (WebAuthn Level 2)*. https://www.w3.org/TR/webauthn/  **[Cited in: 1.1, 3.2, 5.2, 11]**
8. **Ethereum Foundation.** (n.d.). *Ethereum Improvement Proposals (ERC standards)*. https://eips.ethereum.org/  **[Cited in: 1.1]**
9. **FIDO Alliance.** (n.d.). *FIDO Alliance Overview*. https://fidoalliance.org/  **[Cited in: 1.3, 3.2, 11]**

### Estimates & Assumptions

10. **Integration and migration cost estimates.** Method: Derived from typical complex API/security integration projects (documentation, implementation, security review, testing) and typical on-chain migration transaction patterns observed in digital asset operations. Confidence: Medium. Validation: Collect anonymized data from ≥5 exchanges and ≥5 institutions. **[Used in: Context, 2.3, 5.1]**
