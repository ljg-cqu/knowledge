# Cryptographic Library Supply Chain Attacks on MPC Wallet Infrastructure – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Security Team

---

## Pre-Section: Context Recap

- **Problem title**: Cryptographic library supply chain attacks on MPC wallet infrastructure
- **Current state**:
  - Modern MPC wallets depend on large trees of open-source cryptographic and Web3 libraries from npm, PyPI, Maven, Cargo and other registries; a typical production stack pulls 50–200 direct dependencies and 500–2000+ transitive dependencies for cryptography, serialization, networking and tooling  
    [Estimate: Based on typical JavaScript/TypeScript and Python Web3 application dependency graphs reported in industry blogs and package registry statistics, Medium confidence, validate via SBOM generation for 3–5 representative MPC providers].
  - Recent high‑impact incidents (Solana `@solana/web3.js` backdoor in December 2024; npm compromise of `debug`, `chalk`, `ansi-styles` and 15 other packages in September 2025; Shai‑Hulud campaign compromising 500+ npm packages) show attackers increasingly weaponizing popular libraries used in crypto ecosystems to exfiltrate keys and hijack transactions  
    [Source: The Hacker News, 2024; Secure Blink, 2024; Palo Alto Networks, 2025; Sygnia, 2025; CISA, 2025].
  - MPC architecture removes single-device key custody but **does not** eliminate risk from malicious code running inside each party’s execution environment; a compromised cryptographic or Web3 library can exfiltrate key shares or tamper with transactions before or after MPC protocols execute  
    [Source: Coincover, 2024, discussion of crypto wallet attack surfaces; AWS, 2025, analysis of malicious packages].
- **Pain points**:
  - Upstream library account compromise or targeted malicious updates can silently propagate into production builds through legitimate CI/CD pipelines without any single catastrophic local breach  
    [Source: Palo Alto Networks, 2025; Sygnia, 2025].
  - Detection latency for malicious packages is often 5–72 hours, while the September 2025 npm attack deployed a crypto drainer within 16 minutes of compromise, leaving a large unprotected window  
    [Source: Sygnia, 2025; Palo Alto Networks, 2025].
  - Many MPC providers lack comprehensive SBOMs, real‑time dependency monitoring and registry‑level attestations, making it difficult to know whether production systems have pulled compromised versions at all  
    [Estimate: Based on general industry adoption rates for SBOM and supply chain tools; Problem statement assumptions, Medium confidence].
- **Goals**:
  - Reduce major supply chain compromises affecting MPC wallet stacks from an estimated 10–20 significant crypto‑related attacks/year to <5/year (minimum), <2/year (target) and ideally 0/year by Q4 2025  
    [Estimate: Based on aggregation of public supply chain incidents 2023–2025 and attribution to crypto/web3 ecosystems, Medium confidence].
  - Achieve <1 hour (minimum), <15 minutes (target), <5 minutes (ideal) end‑to‑end detection latency from malicious package publication to internal alert, with automated blocking for high‑risk packages  
    [Source: Qualys, 2025, incident‑response guidance for dependency attacks; AWS, 2025].
  - Increase SBOM coverage for MPC providers from <20% to ≥80% (minimum) / ≥95% (target) of production systems by Q2 2025, and ensure ≥90% of production dependencies are continuously scanned for vulnerabilities and indicators of compromise  
    [Estimate: Based on Problem statement goals and typical enterprise adoption curves, Medium confidence].
- **Hard constraints**:
  - 12‑month window (Q1–Q4 2025) to design, roll out and operationalize supply chain defenses while attacks are already active in the ecosystem  
    [Source: Problem statement – Time scale and impact scope].
  - Budget envelope roughly USD 300k–800k per medium‑to‑large MPC provider for SBOM tooling, dependency scanning, security audits and incident‑response automation  
    [Source: Problem statement – Key constraints and resources].
  - Multi‑ecosystem support (npm + PyPI + Maven + Cargo) and low additional CI/CD latency (<10 minutes per pipeline) are required; false‑positive rates must remain <5% to avoid alert fatigue  
    [Source: Problem statement – Key constraints and resources].
- **Key facts**:
  - Solana `@solana/web3.js` versions 1.95.6–1.95.7 were compromised for ~5 hours on 2024‑12‑02 due to phishing of a publish‑access account, with malicious code exfiltrating private keys via Cloudflare headers and causing estimated losses of USD 130k–160k  
    [Source: The Hacker News, 2024; Secure Blink, 2024; Cyfrin, 2024; Infosecurity Magazine, 2024].
  - On 2025‑09‑08, attackers used a compromised maintainer account to push malicious versions of 18 npm packages including `debug@4.4.2`, `chalk@5.6.1` and `ansi-styles@6.2.2`, affecting ~2.6B weekly downloads and deploying a Web3 wallet hijacker/crypto drainer within 16 minutes  
    [Source: Palo Alto Networks, 2025; Sygnia, 2025; Mend.io, 2025].
  - The Shai‑Hulud campaign compromised 500+ npm packages used to exfiltrate GitHub PATs and cloud API keys, prompting a CISA alert on 2025‑09‑23 and demonstrating attackers’ ability to operate at ecosystem scale  
    [Source: CISA, 2025; OX Security, 2025].
  - 2024 crypto theft reached ~USD 2.2B, up 21% from 2023; a substantial share of losses is attributable to infrastructure and supply chain vectors  
    [Source: Coincover, 2024, "Developing resilient crypto wallets: security best practices for developers"].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

1. **Core problem**  
   MPC wallet providers rely on complex dependency trees of cryptographic and Web3 libraries whose integrity they do not directly control; when attackers compromise upstream packages or publisher accounts, malicious code can silently propagate into MPC signing infrastructure, enabling key‑share exfiltration and transaction manipulation despite theoretically strong multi‑party security guarantees  
   [Source: The Hacker News, 2024; Palo Alto Networks, 2025; Coincover, 2024].

2. **Contradictions**
   - **Security vs. developer velocity**: Teams want fast iteration with auto‑updating dependencies (e.g., `^1.95.0` ranges in npm) and minimal friction in CI/CD, but strong supply chain security requires pinned versions, approval workflows and sometimes blocking builds when suspicious updates appear  
     [Source: Qualys, 2025, recommendations for responding to npm attacks].
   - **Open ecosystem vs. curated trust**: Public registries maximize reuse and innovation but allow anyone to publish or take over packages; MPC providers need a smaller, vetted subset with strict controls, which conflicts with the default open model  
     [Source: CISA, 2025; AWS, 2025].
   - **Distributed cryptography vs. centralized chokepoints**: MPC distributes key shares across parties, yet a single upstream library or compromised CI job can cut across that distribution and re‑centralize risk at the software supply chain layer  
     [Source: Coincover, 2024; AWS, 2025].

3. **Who is in conflict?**
   - Security and compliance teams pushing for SBOMs, strict pinning, attestations and slower update cadences.
   - Product and engineering teams prioritizing feature delivery, developer experience and time‑to‑market.
   - Open‑source maintainers and registries balancing usability and contributor freedom against stricter identity, signing and review requirements.

### 1.2 Goals and conditions

- **Security goal**: Reduce the probability that a compromised cryptographic/Web3 library leads to undetected key‑share exfiltration or large‑scale wallet draining across MPC providers to near‑zero, by enforcing integrity verification, runtime monitoring and rapid response playbooks  
  [Source: Problem statement – Goals and success criteria; Coincover, 2024].
- **Detection goal**: Achieve <15‑minute (target) end‑to‑end detection from suspicious package publish to internal alert, with automatic blocklisting and build‑pipeline failure for known malicious versions  
  [Source: Sygnia, 2025; Qualys, 2025].
- **Resilience goal**: Ensure that even if malicious code is briefly imported, layered controls (sandboxing, least privilege, outbound egress controls) prevent large‑scale theft and enable forensic reconstruction  
  [Source: AWS, 2025; Qualys, 2025].

### 1.3 Extensibility and reframing

- **Attribute reframing – "one object, many attributes"**:  
  Treat "MPC wallet infrastructure" as a composite of **cryptographic correctness**, **software supply chain integrity**, **operational controls** and **ecosystem governance**. Reframing from "MPC protocol security" to "end‑to‑end trust chain from registry to runtime" broadens solution space to include SBOMs, attestations, registry‑level policies and insurance  
  [Source: CISA, 2025; AWS, 2025].
- **Scope reframing – from local to ecosystem risk**:  
  Instead of "protect my CI pipeline", frame the problem as "prevent systemic compromise across 50+ MPC providers and 100M+ users when a single core library is backdoored". This highlights needs for cross‑provider information sharing, coordinated incident response and possibly regulatory standards  
  [Source: Coincover, 2024; CISA, 2025].
- **Risk reframing – from vulnerability management to integrity assurance**:  
  Traditional vulnerability management focuses on known CVEs, but supply chain backdoors are often zero‑day. The core problem becomes **continuous integrity and provenance assurance** for code artifacts rather than just patching disclosed bugs  
  [Source: AWS, 2025; Qualys, 2025].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **Dependency graph**: Direct cryptographic and Web3 libraries plus deep transitive dependencies pulled from npm, PyPI, Maven, Cargo and OS package managers  
  [Source: Palo Alto Networks, 2025; AWS, 2025].
- **Build and release pipelines**: CI/CD configuration (version constraints, lockfiles, artifact repositories), signing of builds, deployment automation  
  [Source: Qualys, 2025].
- **Runtime environment**: Node.js/TypeScript services, browser extensions, mobile clients and backend services where MPC protocols and wallet logic execute.
- **Observability and security tooling**: SBOM generators (SPDX/CycloneDX), scanners, EDR/IDS, log aggregation and anomaly detection focused on package behaviors  
  [Source: AWS, 2025].

### 2.2 Balance and "degree" issues

- **Update frequency vs. review depth**: Updating dependencies weekly reduces known‑vulnerability exposure but makes it harder to thoroughly review each change; infrequent updates reduce churn but let vulnerabilities and backdoors linger longer  
  [Source: Qualys, 2025].
- **Automation vs. human oversight**: Fully automated dependency updates (e.g., Dependabot auto‑merge) improve velocity but can propagate malicious versions; excessive manual gates slow delivery and increase toil  
  [Source: Dependabot product docs, inferred usage patterns].
- **Instrumentation vs. performance/noise**: Deep runtime monitoring and egress filtering improve detection of exfiltration but may add latency and false positives if not tuned  
  [Source: AWS, 2025].

### 2.3 Causal chains

1. **Registry compromise chain**:  
   Maintainer account phished → malicious version of critical crypto/Web3 library published → MPC provider’s CI picks up new version due to loose version ranges → production deployment within hours → malicious code exfiltrates key shares or signs attacker‑controlled transactions → funds drained before detection  
   [Source: The Hacker News, 2024; Palo Alto Networks, 2025; Sygnia, 2025].

2. **Transitive dependency blind‑spot chain**:  
   Provider audits only direct dependencies → attacker compromises low‑level utility or logging library (`debug`, `ansi-styles`) with 2.6B weekly downloads → malicious code executes inside higher‑level crypto wallet applications even though top‑level libraries appeared safe → incident responders struggle to trace root cause without SBOMs  
   [Source: Palo Alto Networks, 2025; Mend.io, 2025].

3. **Detection lag chain**:  
   No real‑time registry monitoring + limited anomaly detection → external researchers or vendors discover backdoor hours later → advisories and blocklists published after attackers have already drained multiple wallets → incident response becomes reactive and damage‑limitation only  
   [Source: The Hacker News, 2024; CISA, 2025].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and conflicts

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | Open‑source maintainers; npm/PyPI/Maven/Cargo registry operators; security researchers | Secure ecosystem, maintain adoption, minimize friction for legitimate publishers | Limited resources; volunteer maintainers; cannot manually vet all updates; global user base | Pressure to tighten controls (2FA, signing, scanning) vs. community resistance and usability issues |
| Downstream | MPC wallet providers, custodians, exchanges integrating MPC SDKs | Strong security, low latency, fast feature delivery, regulatory compliance | Budget and staffing; legacy code; multi‑cloud, multi‑language stacks | Security teams vs. product/engineering over update speed and strictness of policies |
| Sideline / External | End users, institutional clients, regulators, insurers, incident response vendors | Asset protection, clear accountability, predictable risk, insurability | Limited visibility into internal dependencies; technical complexity of supply chain risk | Regulators and insurers may demand higher controls or premiums; users resist UX friction from security measures |

[Source: Coincover, 2024; CISA, 2025; AWS, 2025].

### 3.2 Environmental factors

- **Threat actor sophistication**: Crypto remains a high‑value target; campaigns such as Shai‑Hulud and large‑scale npm compromises show attackers capable of compromising hundreds of packages and quickly monetizing access  
  [Source: CISA, 2025; OX Security, 2025].
- **Regulatory pressure**: MiCA, SEC custody rules and other financial regulations increasingly expect demonstrable control over third‑party risk and software supply chains, especially for custodians securing large institutional assets  
  [Source: Coincover, 2024].
- **Tooling evolution**: Cloud providers and security vendors now offer large‑scale behavioral analysis for malicious packages (e.g., Amazon Inspector detecting >150k malicious packages linked to token‑farming campaigns)  
  [Source: AWS, 2025].

### 3.3 Responsibility and room for maneuver

- **Registries** can enforce stronger publisher identity verification, mandatory 2FA, package signing and anomaly detection on new versions of high‑impact packages  
  [Source: CISA, 2025; Palo Alto Networks, 2025].
- **MPC providers** remain responsible for:
  - Maintaining accurate SBOMs and internal mirrors of vetted packages.
  - Enforcing version pinning, lockfiles, and approval workflows for dependency updates.
  - Deploying runtime monitoring for suspicious network egress and crypto operations.
- **Institutions and insurers** can demand independent attestations of supply chain controls and make coverage conditional on adopting best practices  
  [Source: Coincover, 2024].

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2010s–early 2020s – explosive growth of package ecosystems**: npm/PyPI/Maven become default distribution channels for nearly all modern software, including crypto applications, with minimal mandatory security controls  
   [Source: CISA, 2025; AWS, 2025].
2. **2020–2023 – early supply chain wake‑up calls**: Incidents such as `event-stream`, `ua-parser-js` and `colors`/`faker` raise awareness of npm compromise potential, but many crypto projects still rely on default settings and manual vigilance  
   [Source: CISA, 2025].
3. **2024 – Solana web3.js compromise**: Targeted backdoor in `@solana/web3.js` demonstrates that crypto‑specific libraries are high‑value entry points for wallet theft  
   [Source: The Hacker News, 2024; Secure Blink, 2024; Cyfrin, 2024].
4. **2025 – Large‑scale npm campaigns**: The September 2025 attack on `debug`, `chalk` and related packages plus the Shai‑Hulud campaign show attackers pivoting to ecosystem‑wide compromises and crypto‑drainer payloads  
   [Source: Palo Alto Networks, 2025; Sygnia, 2025; CISA, 2025; OX Security, 2025].

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - Default trust model of public registries (anyone can publish; limited identity verification).
  - Economic under‑incentivization of open‑source maintainers to invest in security hardening and operational controls  
    [Source: CISA, 2025].
- **Direct technical causes**:
  - Compromised maintainer credentials enabling attackers to publish backdoored versions under legitimate package names  
    [Source: The Hacker News, 2024; Palo Alto Networks, 2025].
  - Lack of SBOMs and automated alerting so affected consumers do not know which environments include the malicious versions  
    [Source: Qualys, 2025].

### 4.3 Root issues

- **Trust without verification**: Ecosystem norms often assume that popular packages and maintainers are safe, without systematic verification or continuous integrity monitoring  
  [Source: CISA, 2025].
- **Under‑investment in supply chain engineering**: Security budgets historically focused on perimeter/network/app testing, not dependency provenance, leaving a gap that attackers now exploit  
  [Source: Coincover, 2024].
- **Misalignment between risk and control**: Registries, maintainers and consumers each control part of the chain, but incentives and responsibilities are fragmented.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- The number and sophistication of malicious packages is growing, with services like Amazon Inspector already flagging >150k such packages  
  [Source: AWS, 2025].
- As MPC adoption widens (50+ providers, 100M+ users, USD 500B+ assets, per problem statement), the payoff for compromising a single widely‑used cryptographic or Web3 library increases, incentivizing more targeted attacks  
  [Estimate: Based on problem‑statement assumptions, Medium confidence].
- Without SBOMs and automated monitoring, many providers may remain unaware of transient compromises, allowing attackers to harvest keys for later exploitation.

### 5.2 Early signals

- Growing cadence of advisories from CISA and vendors about malicious packages and repository campaigns  
  [Source: CISA, 2025; AWS, 2025].
- Increasing use of crypto‑drainer payloads and Web3‑specific hijackers in npm attacks  
  [Source: Sygnia, 2025; Mend.io, 2025].
- More guidance documents and best‑practice reports targeting wallet developers and custodians, e.g., Coincover’s 2024 wallet security guidance  
  [Source: Coincover, 2024].

### 5.3 Scenarios (6–24 months)

- **Optimistic**:  
  Registries roll out strong identity verification and package signing for high‑impact projects; MPC providers widely adopt SBOMs, internal mirrors and real‑time monitoring; supply chain attacks shift to smaller targets and become less profitable for large‑scale theft.
- **Baseline**:  
  Leading providers and major libraries adopt best practices, but long tail of smaller projects and providers remain vulnerable; periodic high‑profile incidents continue, but systemic catastrophe is avoided.
- **Pessimistic**:  
  Adversaries compromise a core crypto or MPC library used by multiple major custodians, exfiltrating keys or draining wallets at scale before detection; losses reach hundreds of millions, triggering regulatory backlash and aggressive restrictions on dependency usage.

[Scenarios estimated based on recent attack trends and adoption of supply chain security tools reported by CISA, 2025; AWS, 2025; Coincover, 2024, Medium confidence].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Security vendor ecosystem**: Mature commercial tools exist for SBOM generation, vulnerability scanning and behavioral analysis of packages (including cloud‑native services like Amazon Inspector)  
  [Source: AWS, 2025; Qualys, 2025].
- **Industry awareness**: High‑profile Solana and npm incidents have already raised awareness among wallet developers and custodians  
  [Source: The Hacker News, 2024; Palo Alto Networks, 2025].
- **Existing governance frameworks**: Many MPC providers already operate change‑management, incident‑response and audit programs that can be extended to cover supply chain risks  
  [Source: Coincover, 2024].

### 6.2 Capability gaps

- Lack of dedicated supply chain engineering teams and playbooks in many MPC organizations.
- Incomplete observability into which services use which libraries and versions across multi‑cloud, multi‑language deployments.
- Limited red‑teaming focused on simulated supply chain compromises (e.g., inserting benign test backdoors in staging registries).

### 6.3 Buildable capabilities (1–6 months)

- Establish **centralized SBOM and dependency‑risk programs** covering all MPC components and client SDKs.
- Deploy **registry and Git monitoring** for key maintainers and packages (e.g., watch for sudden ownership changes, unusual publish patterns)  
  [Source: CISA, 2025].
- Integrate **automatic blocklisting and quarantine workflows** into CI/CD for known malicious versions based on vendor/intelligence feeds  
  [Source: AWS, 2025; Qualys, 2025].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Open‑source dependency ecosystems; rise of supply chain attacks; MPC wallets’ dependence on cryptographic libraries.
- **Problem**: Upstream package compromise enables key‑share exfiltration and wallet draining despite MPC security properties.
- **Analysis**: Internal dependency graphs, external stakeholders, historical evolution, threat trends and organizational capabilities.
- **Options**: Strengthen dependency governance, adopt SBOMs and monitoring, collaborate with registries and vendors, diversify architectures.
- **Risks**: Residual zero‑day exposure, tool misconfiguration, performance and DX impacts, governance failure.

### 7.2 Key judgments (for validation)

1. Implementing SBOMs, strict pinning and real‑time registry monitoring can reduce the window of exposure for malicious packages from hours to minutes for most MPC providers  
   [Estimate: Based on Qualys, 2025, and AWS, 2025, Medium confidence].
2. Runtime egress controls and anomaly detection can materially limit blast radius even when a malicious package is briefly imported.
3. Cross‑provider coordination (e.g., shared blocklists, industry ISAC‑style groups) is necessary to prevent repeated exploitation across different MPC vendors.

### 7.3 Alternative high‑level paths

- **Path A – Strong supply chain hardening**: Heavy investment in SBOMs, internal mirrors, monitoring, and strict governance.
- **Path B – Minimalist hardening + insurance**: Focus on baseline controls, transfer residual risk via cyber insurance.
- **Path C – Architectural diversification**: Combine MPC wallets with hardware wallets and smart‑contract‑based control to mitigate supply chain concentration risk.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- Over‑reliance on documented incidents; undetected or undisclosed attacks may be more frequent than reported  
  [Source: Coincover, 2024].
- Focus on npm and JavaScript ecosystems may under‑weight risks from PyPI, Maven and Cargo.
- Assuming that all providers can quickly afford and adopt advanced tooling may be optimistic.

### 8.2 Required intelligence

- Detailed **dependency inventories and SBOMs** from multiple MPC providers, including transitive dependencies.
- Data on **time‑to‑detection and time‑to‑remediation** for recent supply chain incidents across organizations.
- Comparative studies of different **supply chain security architectures** (e.g., fully mirrored registries vs. direct public‑registry pulls).

### 8.3 Validation plan

- Run **tabletop exercises and red‑team simulations** where benign test backdoors are introduced into internal mirrors to evaluate detection and response speed.
- Conduct **before/after studies** on detection latency and incident count after deploying SBOMs and monitoring.
- Benchmark **CI/CD performance impact** and developer experience metrics after enabling stricter dependency controls.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Quantitative estimates of incident frequency and financial impact will need refinement as more detailed ecosystem‑wide telemetry becomes available.
- Preferred control mix may shift as registries roll out new features (e.g., mandatory signing) or as new attack techniques emerge.

### 9.2 Incremental approach

- Start with **visibility** (SBOMs, inventory, registry monitoring), then add **preventive controls** (pinning, internal mirrors, access controls), followed by **runtime detection** and finally **ecosystem collaboration**.
- Pilot more intrusive measures (e.g., strict egress blocking) on limited traffic segments before global rollout.

### 9.3 "Good enough" criteria

- All MPC wallet components and client SDKs have current SBOMs and version inventories.
- CI/CD pipelines fail fast when encountering known malicious versions from threat‑intel feeds.
- Periodic red‑team simulations and external assessments confirm that realistic supply chain attack scenarios are detected and contained.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. Supply chain attacks on cryptographic and Web3 libraries create a **single‑point‑of‑failure layer** beneath distributed MPC protocols; without strong supply chain controls, MPC’s cryptographic guarantees can be bypassed  
   [Source: The Hacker News, 2024; Palo Alto Networks, 2025; Coincover, 2024].
2. Recent incidents (Solana web3.js, September 2025 npm attack, Shai‑Hulud) show that attackers can compromise widely‑used packages and weaponize them for crypto key and fund theft within minutes to hours  
   [Source: Sygnia, 2025; CISA, 2025].
3. A combination of **SBOM‑driven visibility**, **strict dependency governance**, **real‑time registry/runtime monitoring** and **ecosystem coordination** can significantly reduce both probability and impact of such attacks within a 12‑month horizon  
   [Source: AWS, 2025; Qualys, 2025; Coincover, 2024].

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric: baseline→target → Date**

- **【P0 – Critical】**
  1. Establish end‑to‑end SBOM coverage for all MPC services and client SDKs → Security Engineering Lead → SBOM coverage: <20% → ≥80% of production components with up‑to‑date SBOMs → 2025‑03‑31.
  2. Implement version pinning and lockfiles for all critical cryptographic and Web3 dependencies, with CI enforcing no implicit minor/patch upgrades → Platform Engineering → % of critical deps pinned: <30% → ≥95% → 2025‑03‑31.

- **【P1 – Important】**
  3. Integrate threat‑intel feeds and registry monitoring (including vendor feeds and CISA alerts) into CI/CD to auto‑block known malicious versions → DevSecOps → Detection latency: hours→<30 minutes for feed‑listed packages → 2025‑04‑30.
  4. Deploy runtime egress monitoring and control for MPC signing services to detect and block anomalous outbound traffic from library code paths → Security Operations → Coverage of critical services: pilot→≥90% → 2025‑04‑30.

- **【P2 – Optional】**
  5. Design and roll out an internal "secure dependency" standard (approved crypto/Web3 libraries, review playbooks, deprecation policies) and share non‑sensitive portions with industry peers → Architecture & Security → Formal standard: draft→approved and partially adopted → 2025‑06‑30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Tooling complexity and false positives cause developer backlash, leading to bypasses | High | Medium | Frequent pipeline failures or noisy alerts | Phase rollout; involve developers in tuning; provide clear docs and fast support | DevSecOps Lead |
| Attackers shift to currently unmonitored ecosystems (e.g., PyPI, internal package feeds) | Medium–High | Medium | Incident traced to non‑npm sources | Expand scope to all ecosystems; prioritize based on criticality; periodically review coverage | Security Engineering Lead |
| Over‑reliance on third‑party security vendors; single point of failure in threat‑intel feeds | Medium | Low–Medium | Vendor outage or missed campaign | Maintain multi‑vendor feeds; keep minimal independent heuristics and anomaly detection | CISO |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A: Strong internal supply chain program** | High control, tailored to MPC risk profile, strong audit posture | Significant upfront investment; requires specialized staff | Implementation delays; possible misconfigurations | Large MPC providers with substantial AUM and security budgets | Very small teams lacking security capacity |
| **B: Rely primarily on managed security services and registries** | Faster startup; less internal complexity | Dependency on vendors; limited customization | Missed edge cases; lock‑in; visibility gaps | Providers with limited in‑house security teams | High‑value custodians needing fine‑grained control |
| **C: Architectural diversification (MPC + hardware + smart contracts)** | Reduces concentration of risk in any single technology layer | Additional integrations, operational overhead, user education | New attack surfaces in hardware or smart contracts | Institutions comfortable managing multiple custody models | Teams with very limited operational maturity |

[Source: Coincover, 2024; AWS, 2025; CISA, 2025; Qualys, 2025].

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **SBOM (Software Bill of Materials)** | Inventory of all components, libraries and dependencies in a software system, often encoded in SPDX or CycloneDX formats | N/A | [Source: Coincover, 2024; Problem statement] |
| **Supply chain attack** | Cyberattack that targets software dependencies or build infrastructure to compromise downstream users via trusted channels | N/A | [Source: CISA, 2025] |
| **Transitive dependency** | Package indirectly included as a dependency of another dependency, often invisible in manifest files but present at runtime | N/A | [Source: Palo Alto Networks, 2025] |
| **Crypto drainer** | Malicious code that hijacks wallet interactions to redirect or steal cryptocurrency transactions | N/A | [Source: Sygnia, 2025; Mend.io, 2025] |
| **Web3.js** | JavaScript library for interacting with blockchain networks; Solana’s `@solana/web3.js` was compromised in December 2024 | N/A | [Source: The Hacker News, 2024; Secure Blink, 2024] |
| **Debug** | Popular npm package for logging and debugging, compromised in September 2025 attack (version 4.4.2) | N/A | [Source: Palo Alto Networks, 2025] |
| **Chalk** | Widely used npm library for terminal string styling, compromised in September 2025 attack (version 5.6.1) | N/A | [Source: Palo Alto Networks, 2025] |
| **Shai-Hulud** | Named supply chain campaign compromising 500+ npm packages to exfiltrate secrets and tokens | N/A | [Source: CISA, 2025; OX Security, 2025] |
| **Amazon Inspector** | AWS service that analyzes workloads and dependencies for vulnerabilities and malicious packages | N/A | [Source: AWS, 2025] |
| **MPC wallet** | Wallet architecture where private keys are split into shares across parties/devices and signing is performed via secure multi‑party computation | N/A | [Source: Coincover, 2024, high‑level description of wallet models] |

---

## 12. References

### Web and Industry Sources (Tier 2)

1. **The Hacker News.** (2024). *Researchers Uncover Backdoor in Solana's Popular Web3.js npm Library*. The Hacker News, December 2024. https://thehackernews.com/2024/12/researchers-uncover-backdoor-in-solanas.html  
   **[Cited in**: Context Recap; Sections 1, 2, 4, 5, 10 **]**
2. **Secure Blink.** (2024). *Supply Chain Attack on Solana's web3.js Library: What You Need to Know*. Secure Blink, December 2024. https://www.secureblink.com/cyber-security-news/supply-chain-attack-on-solana-s-web3-js-library-what-you-need-to-know  
   **[Cited in**: Context Recap; Sections 1, 4, 10 **]**
3. **Cyfrin.** (2024). *Security Advisory: @solana/web3.js v1.95.6 & v1.95.7 are compromised*. Cyfrin Blog, December 2024. https://www.cyfrin.io/blog/critical-security-alert-solana-web3-js-library-compromise  
   **[Cited in**: Context Recap; Section 4 **]**
4. **Infosecurity Magazine.** (2024). *Solana Library Supply Chain Attack Exposes Cryptocurrency Wallets*. Infosecurity Magazine, December 2024. https://infosecurity-magazine.com/news/solana-library-supply-chain-attack  
   **[Cited in**: Context Recap **]**
5. **Palo Alto Networks.** (2025). *Breakdown: Widespread npm Supply Chain Attack Puts Billions of Downloads at Risk*. Palo Alto Networks Blog, September 2025. https://www.paloaltonetworks.com/blog/cloud-security/npm-supply-chain-attack  
   **[Cited in**: Context Recap; Sections 1–3, 4, 5, 7, 11 **]**
6. **Sygnia.** (2025). *16 Minutes to Impact: npm Supply Chain Abuse Deploys Crypto Drainer*. Sygnia Threat Report, September 2025. https://www.sygnia.co/threat-reports-and-advisories/npm-supply-chain-attack-september-2025  
   **[Cited in**: Context Recap; Sections 1–3, 5, 7, 10, 11 **]**
7. **Mend.io.** (2025). *NPM Supply Chain Attack Hits Popular Packages with Crypto Drainer*. Mend.io Blog, September 2025. https://www.mend.io/blog/npm-supply-chain-attack-infiltrates-popular-packages  
   **[Cited in**: Context Recap; Sections 2, 5, 11 **]**
8. **CISA.** (2025). *Widespread Supply Chain Compromise Impacting npm Ecosystem*. Cybersecurity and Infrastructure Security Agency Alert, September 23, 2025. https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem  
   **[Cited in**: Context Recap; Sections 1, 3–5, 7, 10, 11 **]**
9. **OX Security.** (2025). *19 npm Packages Compromised in Major Supply-Chain Attack*. OX Security Blog, 2025. https://www.ox.security.com/blog/npm-packages-compromised  
   **[Cited in**: Context Recap; Sections 3–5, 11 **]**
10. **Qualys.** (2025). *Responding to the NPM Supply Chain Attack: When Dependencies Turn Dangerous*. Qualys Blog, September 2025. https://blog.qualys.com/vulnerabilities-threat-research/2025/09/10/when-dependencies-turn-dangerous-responding-to-the-npm-supply-chain-attack  
    **[Cited in**: Sections 1–3, 4, 6–8, 10 **]**
11. **Coincover.** (2024). *Developing Resilient Crypto Wallets: Security Best Practices for Developers*. Coincover Blog, 2024. https://www.coincover.com/blog/crypto-wallets-security-best-practices-for-developers  
    **[Cited in**: Context Recap; Sections 1, 3, 4–7, 10, 11 **]**
12. **Amazon Web Services.** (2025). *Amazon Inspector Detects Over 150,000 Malicious Packages Linked to Token Farming Campaign*. AWS Security Blog, 2025. https://aws.amazon.com/blogs/security/amazon-inspector-detects-over-150000-malicious-packages-linked-to-token-farming-campaign  
    **[Cited in**: Context Recap; Sections 1–3, 5–7, 10, 11 **]**

### Estimates & Assumptions (Explicitly Flagged)

13. **MPC provider and asset scale assumptions.** Method: Extrapolate from public user and AUM figures of major custodians and MPC wallet providers; align with problem‑statement values (50+ providers, 100M+ users, USD 500B+ assets). Confidence: Medium. Validation: Compare against industry surveys and regulatory filings.  
    **[Used in**: Context Recap; Sections 3, 5, 7, 9, 10 **]**
14. **Incident frequency and loss share attributable to supply chain attacks.** Method: Infer from proportion of reported crypto thefts linked to infrastructure and dependency attacks relative to total USD 2.2B losses in 2024 (Coincover, 2024). Confidence: Low–Medium. Validation: Cross‑check with specialized crypto crime reports and vendor telemetry.  
    **[Used in**: Context Recap; Sections 1, 5, 7, 9, 10 **]**
