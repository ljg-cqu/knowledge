# Audit Transparency and Reproducible Builds in MPC Wallet Ecosystem – Nine-Aspects Analysis

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Security Audit & Transparency Team

---

## Context Recap

- **Problem title**: Audit Transparency and Reproducible Builds in MPC Wallet Ecosystem.
- **Current state**:
  - Most production MPC wallet providers ship closed-source implementations with limited public security information, despite collectively securing more than 50B USD in digital assets for over 100M users. [Source: Problem statement synthesis; market scan of MPC custody providers, 2025]
  - Published audits tend to focus on protocol correctness and high level architecture, while leaving implementation bugs, software supply chain risk, and operational security only partially covered. [Source: Public portfolios of Trail of Bits, NCC Group, Kudelski Security, Least Authority, 2018–2024]
  - Mobile apps and backend services rarely provide reproducible builds or public attestation for deployed binaries, so users cannot verify that audited source code matches what is actually running. [Source: Reproducible Builds documentation, Reproducible Builds Project, 2024; AWS Web3 blogs on reproducible builds and Nitro Enclaves, 2023–2024]
- **Pain points**:
  - Users and institutions must trust opaque vendors and point in time audits for systems that have large unilateral loss potential and complex attack surfaces.
  - Competitive pressure and IP concerns are used as justification for closed source models even for core cryptographic implementations.
  - Lack of standardised disclosure makes it almost impossible to compare providers on objective security posture.
- **Goals** (from problem statement):
  - Increase open source adoption to at least 40 percent of major MPC wallet providers by Q4 2027.
  - Achieve 100 percent publication of mobile app source code for MPC wallets by Q4 2026, at least for core cryptographic, key storage, and signing logic.
  - Raise comprehensive audit coverage to at least 60 percent of audits by Q4 2027, including protocol, implementation, supply chain, and operations.
  - Reach 50 percent reproducible build coverage for mobile wallet apps by Q4 2027.
  - Reach 70 percent adoption of software supply chain attestation frameworks such as Sigstore, in-toto, and SLSA by Q4 2027.
  - Ensure all major providers run continuous security programs including scanning, annual penetration tests, and public bug bounties by Q4 2026. [Source: Problem file goals; Safeheron open-source MPC wallet blog, 2024; AWS reproducible build guidance for Web3 workloads, 2024]
- **Hard constraints**:
  - Legal and IP concerns around open-sourcing commercial MPC implementations.
  - Limited budgets for comprehensive audits and reproducible build infrastructure.
  - Technical friction for deterministic builds across heterogeneous stacks, mobile platforms, and vendor SDKs.
  - Security risk of disclosing sensitive architectural or operational details before mitigations are deployed. [Source: Coinbase MPC incident and cb-mpc open-sourcing blog, 2024; Fireblocks disclosure of GG18/GG20 issues, 2023]
- **Key facts**:
  - Hardware wallets such as Trezor and the open firmware evolution of Ledger show that gradual increases in transparency are possible without destroying business value. [Source: Trezor documentation on open-source firmware and hardware, 2014–2023; Ledger firmware open-sourcing announcements, 2018–2020]
  - DeFi and smart contract wallets such as Safe routinely publish source code and detailed audit reports plus bug bounty programs, setting a high bar for transparency that MPC wallets have not matched. [Source: Safe documentation and audit reports, 2020–2024; Immunefi bug bounty statistics, 2021–2024]

## 1. Problem Definition

### 1.1 Problem and contradictions

- **Core contradiction**: MPC wallets claim higher security than traditional single-key or multisig wallets, but hide most of the implementation details, build pipeline, and operational controls that would allow independent verification of those claims.
- **Tensions**:
  - Security through transparency versus perceived protection of intellectual property and competitive edge.
  - Cost and complexity of comprehensive audits versus risk of catastrophic security failures and regulatory backlash.
  - Need for deterministic, verifiable builds versus convenience of existing heterogeneous CI/CD pipelines and app-store tooling.
- **Contradiction example**:
  - Providers market institutional-grade security with terms such as bank-level custody while simultaneously shipping closed mobile apps whose binaries cannot be tied back to any published source. [Source: Safeheron MPC wallet blog, 2024; AWS MPC wallet architecture guidance using Nitro Enclaves, 2023; Fireblocks MPC wallet marketing materials, 2023]

### 1.2 Goals and conditions

- **Quantified goals**:
  - Open source: at least 40 percent of major MPC wallet providers have production-grade open-source implementations or substantial open cryptographic core libraries by Q4 2027. Baseline is estimated below 10 percent. [Estimate based on: market scan of named providers, 2025, medium confidence]
  - Comprehensive audits: at least 60 percent of audits, counted by provider–year pairs, cover protocol, implementation, supply chain, and operational security. Baseline is assumed to be below 20 percent. [Estimate based on: sampling of public audit reports from Trail of Bits, Least Authority, Kudelski, 2018–2024]
  - Reproducible builds: at least 50 percent of mobile apps for MPC wallets offer reproducible build instructions and verification scripts plus signed attestations by Q4 2027. Baseline effectively zero. [Source: Reproducible Builds documentation, 2024; AWS reproducible build examples for Nitro Enclaves, 2023]
  - Supply chain attestation: 70 percent of providers reach at least SLSA level 2 for build provenance and use Sigstore or equivalent for artifact signing and transparency logs by Q4 2027. [Source: SLSA v1 documentation, OpenSSF, 2023; Sigstore project documentation, 2024]
- **Hard conditions**:
  - No relaxation of core MPC security requirements or threshold guarantees when opening code or making builds reproducible.
  - Regulatory and contractual confidentiality constraints must be preserved while still enabling independent verification by appropriate third parties.
  - Reproducible build approach must integrate with app-store signing models and HSM- or enclave-based server deployments. [Source: AWS reproducible builds and attestation for Nitro Enclaves, 2023; Reproducible Builds project guidance for proprietary platforms, 2024]

### 1.3 Extensibility and reframing

- **Reframing axes**:
  - From binary open versus closed source, to layered transparency: cryptographic libraries, reference implementations, mobile apps, orchestration servers, and infrastructure each can have different visibility and licensing models.
  - From audits as point-in-time checklists, to a continuous assurance pipeline combining reproducible builds, ongoing scanning, penetration testing, and bug bounties.
  - From transparency as a cost centre, to transparency as a competitive differentiator and regulatory risk hedge.
- **Alternative problem definitions**:
  - How can MPC wallet providers create a verifiable security story that regulators, institutional clients, and technical users can independently check at reasonable cost?
  - How to adopt reproducible build and supply chain attestation techniques from broader software ecosystems into the specific constraints of MPC wallets and Web3 infrastructure. [Source: Reproducible Builds documentation, 2024; Sigstore design docs, 2022; SLSA security levels paper, 2021]

## 2. Internal Logical Relations

### 2.1 Key elements inside the problem

- **Roles**:
  - MPC wallet engineering teams implementing protocols and integrating with blockchain networks.
  - Security teams and external auditors reviewing protocols, code, and operations.
  - DevOps and platform teams maintaining CI/CD, signing keys, and deployment pipelines.
  - Legal, compliance, and business stakeholders controlling disclosure policies and IP strategy.
- **Resources**:
  - Source-code repositories, build artifacts, infrastructure-as-code, deployment manifests.
  - Audit reports, threat models, incident postmortems, internal security documentation.
  - Budget and headcount for security engineering, audits, and community engagement.
- **Processes**:
  - Protocol design and implementation.
  - Build and release management for mobile and backend components.
  - Audit scoping, execution, reporting, and remediation.
  - Vulnerability management, disclosure, and bug bounty triage.

### 2.2 Balance and degree

- **Too much of a good thing**:
  - Over-indexing on secrecy can increase risk by preventing external review and hiding systemic weaknesses until after an incident.
  - Over-sharing detailed operational runbooks may expose legitimate attack paths before mitigations or detection capabilities are in place.
  - Excessive focus on protocol-level proofs without matching implementation hardening can lead to paper-secure but exploit-vulnerable systems. [Source: Fireblocks paper on key-extraction attacks against GG18/GG20-based MPC wallets, 2023; Coinbase cb-mpc disclosure, 2024]
- **Trade-off examples**:
  - Choosing fully deterministic builds may require constraining toolchains, compilers, and third-party SDK versions, which has opportunity cost versus rapid feature development.
  - Publishing full audit reports publicly may require more careful scoping and redaction to avoid handing low-effort exploits to attackers.

### 2.3 Core internal causal chains

- **Chain 1: Transparency level to external review quality to vulnerability discovery**:
  - Higher code and pipeline transparency plus reproducible builds increase the number and diversity of reviewers.
  - More reviewers plus public bug bounties generally increase the rate of vulnerability discovery before exploitation. [Source: Immunefi critical bounty statistics, 2021–2024; Ethereum Foundation bug bounty program results, 2016–2024]
- **Chain 2: Supply chain controls to build integrity to user trust**:
  - Implementing Sigstore signing, SLSA-style provenance, and deterministic builds reduces risk of unnoticed supply chain attacks.
  - Verifiable attestations can be surfaced in user-facing trust indicators or institutional due diligence, increasing adoption by risk-conscious clients. [Source: Sigstore project whitepapers, 2021–2023; SLSA v1 reference, OpenSSF, 2023]
- **Chain 3: Audit scope to residual risk**:
  - Narrow protocol-only audits leave entire classes of vulnerabilities undetected in implementation, dependencies, and operations.
  - Comprehensive audits with clear disclosure and follow-up reduce unknown unknowns but cost more and require deeper collaboration between provider and auditors.

## 3. External Connections

### 3.1 Stakeholders and interests

| Stakeholder type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| MPC wallet providers | Design, build, and operate MPC custody and wallets | Grow AUM, ship features, avoid incidents, maintain IP moat | Budget, time to market, IP and legal risk, hiring market | Tension between transparency and secrecy, cost of audits and build hardening |
| Institutional users | Custody large assets via MPC providers or SaaS wallets | Demonstrable security, regulatory compliance, audit trails | Limited in-house cryptography and supply-chain expertise | Depend on provider disclosures, may distrust opaque models |
| Retail users | Use consumer MPC wallets | Simple UX, safety of funds, privacy | Limited ability to verify technical claims | Must rely on brands, app-store ratings, and community reputation |
| Security auditors and researchers | Review protocols, code, and operations | Access to source, artifacts, and environments, publish research | Contract scope, NDAs, liability | May want more disclosure than providers are comfortable with |
| Regulators and policymakers | Oversee custody, consumer protection, systemic risk | Clarity on technical controls, incident reporting | Limited deep technical expertise, slow standard-setting | May mandate transparency levels that clash with existing business models |

### 3.2 Environment

- **Technology environment**:
  - Rapid evolution of threshold signature schemes, secure enclaves, and Web3 infrastructure.
  - Emergence of standard supply-chain security frameworks such as Sigstore, in-toto, and SLSA that can be reused by MPC providers. [Source: Sigstore docs, 2022–2024; SLSA reference, 2023; in-toto specification, 2020]
- **Market environment**:
  - Growing institutional allocation to digital assets increases scrutiny on custody models.
  - Competition from hardware wallets, smart contract wallets, and fully on-chain solutions that can credibly claim stronger transparency properties.
- **Policy and regulatory environment**:
  - Evolving regulations such as MiCA in the EU and custody guidance in the US likely to emphasise operational resilience and transparency.
  - Potential future requirements for verifiable controls over key management and software supply chain.

### 3.3 Responsibility and room to manoeuvre

- **Where MPC providers should take proactive responsibility**:
  - Define and adopt a baseline transparency standard, including open-sourcing cryptographic libraries, publishing detailed audit reports, and implementing reproducible builds for critical components.
  - Educate customers and regulators about what specific controls are in place, in verifiable rather than purely narrative terms.
- **Where to leave room for others**:
  - Allow regulators, independent foundations, or industry groups to define certification schemes instead of self-marking compliance.
  - Support independent open-source reference implementations without forcing every commercial variation to be fully open from day one.

## 4. Origins of the Problem

### 4.1 Historical nodes

- 2017–2020: First commercial MPC custody platforms prioritise speed to market and enterprise sales over transparency, following the traditional banking technology model rather than the open-source ethos of public blockchains. [Source: Market history of Fireblocks, Unbound Security, ZenGo, 2017–2020]
- 2020–2022: DeFi and smart contract ecosystems normalise open-source contracts, public audits, and large bug bounties, but MPC wallets lag behind because much logic lives off chain and does not benefit from on-chain verifiability. [Source: Safe audit reports and bug bounties, 2020–2023; Immunefi statistics, 2021–2024]
- 2023–2024: Public disclosures of vulnerabilities in MPC implementations and libraries, plus isolated open-source initiatives such as Safeheron and Coinbase cb-mpc, start to shift expectations but do not yet transform the overall ecosystem. [Source: Fireblocks paper on key extraction in GG18/GG20 implementations, 2023; Coinbase cb-mpc blog, 2024; Safeheron open-source MPC wallet blog, 2024]

### 4.2 Background versus direct causes

- **Background causes**:
  - Cultural inheritance from traditional custody and HSM vendors where secrecy is normal and IP is guarded.
  - Lack of standard-setting bodies or widely adopted reference architectures for MPC wallet transparency.
  - Historical assumption that audits and compliance reports are sufficient for institutional comfort even without code-level visibility.
- **Direct triggers**:
  - Specific vulnerability disclosures in MPC protocols and implementations highlighting the gap between protocol proofs and real-world deployments.
  - Increasing regulatory interest and due diligence demands from institutional clients regarding software supply chain and secure development lifecycle. [Source: Public statements from major regulators on cloud and software supply-chain risk, 2021–2024]

### 4.3 Root issues

- Misaligned incentives: providers bear the cost of transparency but perceive most benefits as accruing to users, regulators, and the broader ecosystem.
- Lack of off-the-shelf, sector-tailored patterns and tooling for reproducible builds and attestations in Web3 and MPC contexts.
- Absence of shared quantitative metrics for transparency and verifiability that buyers can easily use in RFPs and evaluations.

## 5. Problem Trends

### 5.1 Current trajectory

- If no major changes occur:
  - Closed-source MPC wallets will continue to grow assets under management, increasing systemic risk in case of latent vulnerabilities.
  - Incidents will likely surface through isolated breaches or research publications rather than structured continuous assurance.
  - Fragmented transparency practices will persist, with some providers publishing narrow audits and others remaining almost entirely opaque.

### 5.2 Early signals

- Growing number of open-source MPC libraries and reference implementations published by both startups and large exchanges. [Source: Safeheron MPC library on GitHub, 2024; Coinbase cb-mpc repository, 2024]
- Web3-focused AWS guidance explicitly promoting reproducible builds and attestation for Nitro Enclave-based MPC signing services. [Source: AWS Web3 blogs on reproducible builds and Nitro Enclaves, 2023–2024]
- Increased investor and regulator questions about supply-chain risk after major software supply-chain attacks in other industries.

### 5.3 Scenarios for 2026–2028

- **Optimistic scenario**:
  - Industry agrees on a transparency baseline: open cryptographic cores, public comprehensive audits, reproducible builds for mobile and server components, bug bounties, and SLSA level 2 or higher for all major providers.
  - Regulators and large clients prefer or even mandate providers that meet this baseline, creating positive feedback.
- **Baseline scenario**:
  - Mixed adoption: some leaders adopt deep transparency and gain a reputation premium; many others remain partially opaque.
  - Open-source projects serve as reference and pressure but do not fully displace proprietary stacks.
- **Pessimistic scenario**:
  - One or more high-profile incidents in opaque MPC wallets lead to large losses and reactive regulation.
  - Providers respond with compliance-heavy but still opaque processes, and innovation slows.

## 6. Capability Reserves

### 6.1 Existing strengths

- Many MPC providers already have mature security engineering, DevOps, and cryptography teams that can in principle implement transparency initiatives.
- Web3 ecosystems are familiar with public bug bounty programs, security audits, and open-source governance.
- Cloud vendors provide building blocks for attested execution, key management, and secure build pipelines. [Source: AWS Nitro Enclaves documentation, 2023; GCP Confidential Computing docs, 2022]

### 6.2 Capability gaps

- Limited in-house expertise on reproducible builds across mobile, backend, and cross-platform toolchains.
- Few teams have experience designing disclosure policies that balance transparency, IP, and safety.
- Many providers lack product and marketing capabilities to frame transparency as a feature rather than a liability.

### 6.3 Buildable capabilities within 1–3 years

- Train existing DevOps and security teams on reproducible build practices and supply-chain frameworks, using open documentation and vendor guidance.
- Hire or contract experienced open-source maintainers to help structure repositories, contribution processes, and community engagement.
- Develop internal playbooks for coordinated vulnerability disclosure and public audit report publication, drawing on established patterns from DeFi and open-source security.

## 7. Analysis Outline

### 7.1 Structured outline

- Background and stakes: assets under management, user base, and current opacity.
- Problem definition: trust and verification gap, lack of reproducible builds, limited audits.
- Internal and external drivers: incentives, regulatory and competitive environment.
- Options: layered transparency, full open-source, certification without open source, status quo.
- Risks and benefits: security, IP, cost, market differentiation, regulatory exposure.
- Recommended pathway: staged roadmap combining open-source components, comprehensive audits, reproducible builds, and attestation.
- Validation and iteration: pilots with selected products and clients, third-party assessments, incident-driven adjustments.

### 7.2 Key judgments

- Transparency at the cryptographic and build-pipeline level improves security in expectation by increasing independent review, despite short-term exposure to more bug discovery.
- Reproducible builds and supply-chain attestation are becoming table stakes in high-assurance software and will be expected for MPC wallets within the next 3–5 years.
- Providers that move early on transparency will be better positioned with regulators and institutional clients, and can shape standards rather than merely comply.

### 7.3 Alternative paths

- **Path A: Minimum viable transparency**:
  - Publish limited whitepapers and protocol audits while keeping most implementation and pipeline details closed.
- **Path B: Layered open source and attestations**:
  - Open cryptographic libraries and selected components, adopt reproducible builds for mobile apps and server binaries, and publish comprehensive audits and attestations.
- **Path C: Full open implementation**:
  - Open-source nearly all components including orchestration and infrastructure-as-code, with community governance and extensive public documentation.

## 8. Validating the Answer

### 8.1 Potential biases

- Security community bias toward open source as a universal good may under-weigh legitimate IP and threat-model considerations.
- Vendor bias toward protecting short-term revenue and valuation may under-weigh systemic risk and long-term regulatory exposure.
- Analyst bias from focusing on high-profile incidents may overlook the silent evidence of systems that are secure but closed.

### 8.2 Required intelligence

- Empirical comparison of incident rates and vulnerability discovery for open versus closed MPC or cryptographic systems with similar usage.
- Cost benchmarks for comprehensive audits and reproducible-build implementations across different provider sizes.
- Survey data on institutional buyer preferences regarding transparency features in custody RFPs.

### 8.3 Validation plan

- Run pilots with 1–2 providers implementing path B layered transparency and measure:
  - Time and cost to reach desired transparency baseline.
  - Number and severity of vulnerabilities found pre- and post-transparency.
  - Client and regulator feedback, including win rate in competitive deals.
- Commission independent studies or meta-analyses of audit scopes and supply-chain controls across MPC providers.

## 9. Revising the Answer

### 9.1 Likely revisions

- Quantitative targets for open-source adoption, reproducible builds, and audit coverage may need adjustment based on early pilot results.
- Some providers may demonstrate credible alternative assurance mechanisms that reduce the marginal value of full open source for specific components.
- Regulatory developments could accelerate or slow down adoption timelines.

### 9.2 Incremental approach

- Start with low-risk, high-impact components such as open-sourcing protocol libraries and establishing reproducible builds for stateless server components.
- Gradually extend reproducible-build coverage to mobile apps, signing services running in enclaves, and orchestration systems.
- Move from private comprehensive audits to public summaries, then to full redacted reports over time.

### 9.3 Good enough criteria

- For a given provider, consider the transparency program good enough to support institutional adoption when:
  - Core cryptographic libraries and protocol implementations are open source or have equivalent independent review.
  - At least one major product line has reproducible builds with published verification instructions and signed attestations.
  - Recent comprehensive audits and continuous monitoring evidence are publicly available or easily accessible under NDA.

## 10. Summary and Action Recommendations

### 10.1 Core insights

- The main risk is not only whether MPC protocols are mathematically sound, but whether real-world implementations, build pipelines, and operations can be independently verified over time.
- Transparency across code, audits, builds, and supply chain is both a security control and a market differentiator for MPC wallets.
- Achieving the proposed goals over 2026–2028 is challenging but feasible if providers adopt a layered transparency strategy and reuse existing open-source tools and standards.

### 10.2 Near-term action list 0–3 months

1. **P0** Establish a transparency baseline and roadmap for each major MPC wallet provider, including target levels for open-source components, audit scope, reproducible builds, and attestations.
2. **P0** Design and pilot a reproducible-build pipeline for at least one mobile app and one backend binary, using deterministic toolchains and artifact signing.
3. **P1** Define a standard comprehensive audit scope template covering protocol, implementation, supply chain, and operations, and align with at least two leading audit firms.
4. **P1** Launch or upgrade bug bounty programs for MPC wallet products, coordinated with disclosure policies.
5. **P2** Engage with regulators and industry groups to socialise transparency goals and explore certification pathways.

### 10.3 Key risks and mitigation

| Risk | Impact | Probability | Trigger condition | Mitigation | Owner |
|------|--------|-------------|------------------|-----------|-------|
| Sensitive details in audits or repo help attackers | High | Medium | Detailed information is published without adequate hardening or monitoring | Apply staged disclosure with redaction; ensure compensating controls are in place before publication | Security team lead |
| Reproducible-build implementation delays feature delivery | Medium | Medium | Build determinism work blocks release pipelines | Start with pilot projects; reserve dedicated capacity; adopt incremental determinism per component | Engineering director |
| Open-sourcing core components erodes competitive advantage | Medium | Low to Medium | Competitors reuse open libraries without contributing back | Focus on differentiating value in UX and integrations; adopt licenses and governance that encourage collaboration | Product and legal leads |
| Underestimation of cost and complexity leads to stalled initiatives | High | Medium | Programs launch without realistic budgets and leadership backing | Build detailed business case; secure multi-year funding and executive sponsorship | Executive sponsor |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best when | Avoid when |
|--------|----------|-------|-------|-----------|-----------|
| A. Minimum viable transparency | Low direct cost; faster to implement; preserves most IP secrecy | Limited assurance for sophisticated users; weak differentiation | Regulatory or incident shock may expose gaps; trust deficit remains | Short-term bridge for small providers with limited resources | When targeting institutional clients or highly regulated markets |
| B. Layered open source and attestations | Stronger assurance; aligns with emerging best practices; balances transparency and IP | Moderate to high implementation cost; requires organisational change | Execution risk; may temporarily expose more bugs | Providers with growth ambitions and regulatory exposure; ecosystems building long-term trust | When leadership is unwilling to commit resources and accept cultural change |
| C. Full open implementation | Maximum transparency and community review; strong brand for security-conscious users | Very high engineering and governance cost; IP moat reduced | Misuse of code by competitors; more complex support expectations | Providers pursuing ecosystem leadership and community-driven innovation | When business model relies heavily on proprietary integration logic or secret algorithms |

## 11. Glossary

| Term | Definition | Unit or range | Source or context |
|------|------------|---------------|-------------------|
| MPC wallet | Wallet or custody system that uses secure multi-party computation to protect private keys by splitting them across multiple parties or devices | N/A | Problem statement and industry usage |
| Reproducible build | Build process where the same source and environment deterministically produce identical binaries, enabling independent verification that deployed artifacts match the source | N/A | Reproducible Builds Project documentation, 2024 |
| Audit transparency | Degree to which security audits, scope, findings, and follow-up are publicly disclosed or at least accessible to relying parties | N/A | Adapted from security audit firm practices |
| Supply chain attestation | Cryptographic evidence about the origin and build process of software artifacts, typically including who built them, from which source, and in which environment | N/A | Sigstore and SLSA documentation |
| Sigstore | Open-source project providing keyless signing and transparency logs for software artifacts and build outputs | N/A | Sigstore documentation, 2024 |
| SLSA | Supply chain Levels for Software Artifacts, a framework that defines maturity levels for build provenance and supply chain integrity | Levels 0–4 | SLSA v1 docs, OpenSSF, 2023 |
| Nitro Enclave | AWS technology for isolated compute environments that can run sensitive workloads such as MPC signing, with attestation capabilities | N/A | AWS Nitro Enclaves documentation, 2023 |
| Bug bounty program | Structured program where external researchers are rewarded for responsibly disclosing vulnerabilities | Hundreds to millions of USD per critical bug | Immunefi and HackerOne program docs |
| Comprehensive audit | Audit that covers protocol correctness, implementation security, software supply chain, and operational security, not just one of these dimensions | N/A | Problem statement definition; Trail of Bits and NCC Group service descriptions |
| Deterministic toolchain | Compiler, linker, and packaging configuration that ensure builds are reproducible given the same inputs | N/A | Reproducible Builds docs |

## 12. References

- Open-Source MPC Wallet: Secure Your Digital Assets, Safeheron, 2024, blog post and GitHub repository.
- Practical Key-Extraction Attacks in Leading MPC Wallets, Fireblocks research team, 2023, cryptographic research paper and disclosure.
- The Subtleties of Error Handling Flaws in MPC, Coinbase, 2024, engineering blog and cb-mpc open-source announcement.
- Verify enclave counterparties with reproducible builds and cryptographic attestation using AWS Nitro Enclaves, AWS Web3 blog, 2024.
- Establishing verifiable security: Reproducible builds and AWS Nitro Enclaves, AWS Web3 blog, 2023.
- Reproducible Builds documentation and case studies, Reproducible Builds Project, accessed 2024, https://reproducible-builds.org/.
- Sigstore project documentation and design docs, Sigstore community, 2021–2024, https://sigstore.dev/.
- Supply chain Levels for Software Artifacts v1, OpenSSF, 2023, https://slsa.dev/.
- Public audit reports from Trail of Bits, Least Authority, NCC Group, Kudelski Security, 2018–2024.
- Safe documentation and audit reports for Safe smart contract wallet, 2020–2024.
- Trezor open-source firmware and hardware documentation, SatoshiLabs, 2014–2023.
- Ledger firmware open-sourcing announcements and transparency documentation, Ledger, 2018–2020.
- Immunefi bug bounty platform statistics and case studies, Immunefi, 2021–2024.
- Ethereum Foundation bug bounty program documentation and reports, 2016–2024.
