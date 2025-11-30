# Nine-Aspects Analysis – Single Vendor Software Dependency Creating De Facto Single Point of Failure

**Document Metadata**
- **Related Problem File**: `09_Single_Vendor_Software_Dependency.md`
- **Domain**: Blockchain MPC wallets – software supply chain & implementation risk
- **Framework**: Nine Aspects for Analyzing Problems (Liu Run) – plus Glossary & References

---

## Context Recap

- **Problem title**: Single vendor MPC wallet software creating de facto single point of failure
- **Current state**:
  - MPC wallets distribute private key shares across multiple parties, but in practice most deployments run *identical vendor-supplied software* on all parties (mobile app, server, co-signer) [Blog: Cubist, 2024; Paper: Fireblocks, 2023].
  - First‑generation threshold ECDSA deployments (Lindell17, GG18/20, CGGMP20) were implemented by a small set of vendors and reused widely across exchanges, custodians, and wallet providers [Paper: Fireblocks, 2023].
  - Key‑extraction vulnerabilities and misconfigurations have affected multiple large providers simultaneously (e.g., ZenGo, Coinbase WaaS, Binance, BitGo, ING) due to shared implementations [Paper: Fireblocks, 2023].
- **Pain points**:
  - Single compromise of the vendor (malicious update, CI/CD breach, insider) can undermine all parties and all customer deployments at once – recreating a centralized point of failure despite distributed keys [Blog: Cubist, 2024].
  - Implementation bugs in complex MPC protocols can allow key extraction or transaction forgery even when the underlying protocol is theoretically secure [Blog: Cubist, 2024; Paper: Lindell, 2017].
  - Performance pressure (demand for <1s latency) pushes vendors toward insecure protocol variants (e.g., honest‑but‑curious assumptions, disabled proofs) [Blog: Cubist, 2024].
- **Goals** (from problem file):
  - Achieve ≥2 independent implementations per deployment for ≥50% of MPC wallets by Q4 2026.
  - Reduce single‑vendor deployments from ~90% → ≤30% by Q4 2026.
  - Reach ≥50% machine‑checked protocol implementations by Q4 2027.
  - Reduce vulnerability discovery time from 2–5 years → <6 months.
- **Hard constraints**:
  - Users, especially traders, expect <1–3s signature latency; 10s+ latencies are widely considered unacceptable [Blog: Cubist, 2024].
  - Limited global pool of formal‑methods and MPC experts (10–20 people capable of fully verifying protocols, per problem assumptions).
  - Backward compatibility with already‑deployed keys; cannot simply force ecosystem‑wide key rotation.
- **Key facts**:
  - Threshold MPC protocols (Lindell17, GG18/20, CGGMP20) are widely deployed in production and have had serious implementation vulnerabilities discovered years after rollout [Paper: Fireblocks, 2023; Paper: Lindell, 2017; Paper: Gennaro & Goldfeder, 2018/2020; Paper: Canetti et al., 2020].
  - Crypto theft in 2024 exceeded $2.2B, with part of the loss attributed to attacks that bypassed MPC key protections at transaction and infrastructure layers [Report: Chainalysis, 2025].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

- **Core contradiction**:
  - Theory: MPC eliminates single points of failure by distributing key shares; attacker must compromise ≥threshold parties.
  - Practice: If *all* parties run identical software from one vendor, a single vendor‑side compromise (malware in build system, malicious update, shared logic bug) can break the entire system. The “distributed” architecture hides a *logical* single point of failure in the software supply chain [Blog: Cubist, 2024].
- **Key conflicts**:
  - **Security vs. cost**: Independent implementations and formal verification multiply engineering cost 2–3× versus one shared codebase.
  - **Security vs. performance**: Full zero‑knowledge proofs and hardened protocols yield ~10s signature latency; market expectations push toward <1–3s [Blog: Cubist, 2024].
  - **Vendor convenience vs. systemic resilience**: Centralized control simplifies support and feature rollout but increases correlated failure risk [Blog: Cubist, 2024; Report: Chainalysis, 2025].

### 1.2 Goals & conditions

- **Security & diversity targets**:
  - ≥2 mutually independent implementations of the same protocol (different teams, languages, and supply chains) for at least client vs. server roles across ≥50% of deployments by Q4 2026.
  - Machine‑checked protocol and/or implementation proofs for ≥50% of deployed MPC stacks by Q4 2027 [Blog: Cubist, 2024].
  - Time‑to‑detection for critical bugs reduced from 2–5 years (Lindell17/GG18/20 history) to <6 months via continuous auditing and verification pipelines [Paper: Fireblocks, 2023].
- **Performance & UX conditions**:
  - Keep p95 signature latency within <3s for mainstream consumer use; institutional trading may demand <1s but with explicit opt‑in to higher risk levels [Blog: Cubist, 2024].
- **Economic conditions**:
  - Budget of roughly $5M–$15M industry‑wide for independent implementations, plus $3M–$8M for formal verification toolchains and research (per problem file estimates).

### 1.3 Extensibility & reframing

- **Virtual vs. physical**:
  - *Physical*: servers, HSMs, mobile devices, network links.
  - *Virtual*: software supply chains, vendor trust relationships, protocol specifications, legal contracts.
  - Reframing from “key distribution problem” to “software supply chain and trust‑graph problem” widens option space to include procurement standards, regulation, and open‑source diversity [Blog: Cubist, 2024; SLSA, 2024].
- **Hard vs. soft**:
  - *Hard*: cryptographic protocols, implementation languages, CI/CD pipelines.
  - *Soft*: vendor incentives, regulatory expectations, user tolerance for latency, industry norms.
- **Latent vs. manifest**:
  - *Latent*: undiscovered protocol bugs, backdoors in shared libraries, dormant CI/CD compromises.
  - *Manifest*: disclosed key‑extraction attacks against real deployments; public outages and reported thefts [Paper: Fireblocks, 2023; Report: Chainalysis, 2025].
- **Reframing options**:
  - From “avoid single vendor” → “manage correlated failure risk with explicit diversity and isolation budgets”.
  - From “one MPC wallet vendor” → “ecosystem of interoperable MPC stacks governed by minimum diversity and verification baselines”.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **Roles**:
  - MPC wallet vendors (protocol implementers, platform providers).
  - End‑user organizations (exchanges, custodians, enterprises, DeFi protocols).
  - End users (consumers, traders, custody clients).
  - Security researchers and auditors.
  - Regulators and standard‑setting bodies.
- **Resources & assets**:
  - Protocol specifications (Lindell17, GG18/20, CGGMP20, FROST, etc.).
  - Implementation codebases (Rust, Go, TypeScript, C++).
  - CI/CD pipelines and build systems.
  - Monitoring, logging, audit tooling, and incident response workflows.
- **Rules & processes**:
  - Vendor release processes (versioning, rollout patterns, rollback mechanisms).
  - Audit and disclosure processes (who reviews what, how often, under which incentives).
  - Key generation ceremonies and signing flows in production.

### 2.2 Balance & “degree”

- **Security vs. latency**:
  - Too little security (disabled proofs, relaxed threat models) → practical breakage despite theoretical guarantees [Blog: Cubist, 2024].
  - Too much security with no UX consideration (10–20s per signature) → users bypass protections (e.g., turning off MPC or migrating to less secure wallets) [Blog: Cubist, 2024].
- **Code reuse vs. diversity**:
  - High reuse of one implementation lowers cost and improves interoperability but maximizes correlated risk.
  - Extreme diversity without shared standards raises integration cost and implementation bug surface.
  - Balanced design: a small set of well‑specified protocols, each with 2–3 independently developed and verified implementations [Paper: Fireblocks, 2023].
- **Centralization of control vs. ease of operations**:
  - Centralized vendor control simplifies patch rollouts and incident response but also allows a single malicious or compromised update to drain all wallets simultaneously.

### 2.3 Key internal causal chains

- **Chain A – Vendor compromise → systemic failure**:
  1. Single vendor controls client and server implementations and signing workflows.
  2. Attacker compromises vendor build system, signing key, or key developer account [Blog: Cubist, 2024; Sigstore docs, 2023].
  3. Malicious update shipped to all parties; all parties accept due to auto‑update or trust in vendor signing keys.
  4. Attacker abuses capabilities (silent key export, transaction rewriting) → large‑scale coordinated theft [Report: Chainalysis, 2025].
- **Chain B – Complexity → implementation bugs → key extraction**:
  1. Threshold ECDSA protocols require careful handling of randomness, zero‑knowledge proofs, and error cases [Paper: Lindell, 2017; Paper: Gennaro & Goldfeder, 2018/2020].
  2. Vendor implements protocol once and reuses across many customers; subtle mistakes remain undetected for years.
  3. Security research later reveals key‑extraction attacks exploitable with limited queries [Paper: Fireblocks, 2023].
  4. Because the same codebase underpins many large deployments, patching becomes urgent and globally coordinated, with high operational risk.

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders & interests

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream – Protocol authors & open‑source projects | Design cryptographic protocols and reference implementations | Correctness, academic impact, adoption | Limited engineering resources, incentive misalignment with commercialization | May prefer simpler assumptions; vendors may extend or modify protocols unsafely |
| Upstream – Cloud & infra providers | Provide HSMs, KMS, network, compute | Reliability, revenue, compliance | Shared‑custody models, multi‑tenant risk, hardware constraints | Diversity requirements may push for heterogeneous infra that is harder to manage |
| Downstream – Exchanges & custodians | Integrate MPC wallets to hold and move assets | Security, regulatory compliance, UX, low latency | Cost constraints, migration risk, integration complexity | Resist multi‑vendor setups that raise integration and support cost |
| Downstream – End users (traders, institutions) | Use wallets for trading and custody | Asset safety and predictable UX | Limited technical understanding of MPC details | Demand <1s latency may indirectly incentivize insecure shortcuts |
| Sideline – Regulators & insurers | Supervise custody practices; price risk | Reduce systemic risk and concentration | Limited cryptographic expertise, slow rulemaking cycles | May over‑ or under‑regulate diversity/verification, affecting incentives |

### 3.2 Environment

- **Regulatory trends**:
  - Custody regulations increasingly reference “sound cryptographic controls” and “operational resilience,” opening room to codify diversity and verification as best practice [Report: Chainalysis, 2025].
- **Technology trends**:
  - Formal verification tools (Coq, F*, EasyCrypt) increasingly applied to cryptographic protocols and low‑level implementations [Coq docs, 2023].
  - Supply‑chain‑security frameworks (Sigstore, SLSA, in‑toto) are gaining adoption in mainstream software and can be ported to crypto vendors [Sigstore, 2023; SLSA, 2024].

### 3.3 Responsibility & room for maneuver

- Vendors can:
  - Adopt supply‑chain hardening and reproducible builds.
  - Sponsor or commission at least one independent re‑implementation of their chosen protocol.
- Institutional customers can:
  - Make procurement conditional on vendor diversity and verification guarantees.
  - Run fixed “diversity budgets” (e.g., never concentrate >40% of managed assets on a single software stack).
- Regulators can:
  - Require disclosure of implementation diversity and verification status in custodial license applications.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2017–2020 – First‑generation MPC wallet deployments**: Early adopters prioritized time‑to‑market and usability, reusing a small set of threshold ECDSA protocols and implementations (Lindell17, GG18/20, CGGMP20) across exchanges and custodians [Paper: Lindell, 2017; Paper: Gennaro & Goldfeder, 2018/2020; Paper: Canetti et al., 2020].
2. **2018–2023 – Latent vulnerabilities**: Implementation bugs remained undiscovered while assets under management and user counts grew rapidly [Paper: Fireblocks, 2023].
3. **2023 – Key‑extraction disclosures**: Research published practical key‑extraction attacks against multiple leading MPC wallet implementations, revealing the extent of software homogeneity [Paper: Fireblocks, 2023].
4. **2024–2025 – Supply‑chain awareness**: Broader industry discussion framed MPC wallets as still having single points of failure in their software supply chains [Blog: Cubist, 2024; Report: Chainalysis, 2025].

### 4.2 Background vs. direct causes

- **Background causes**:
  - Economic incentives for fast, centralized product delivery.
  - Scarcity of teams capable of implementing and verifying complex MPC stacks.
  - Lack of explicit non‑functional requirements around diversity in early procurement.
- **Direct causes**:
  - Specific implementation flaws in randomness generation, proof checks, or error‑handling that allow key extraction or protocol subversion [Paper: Fireblocks, 2023].
  - Inadequate supply‑chain protections (unsigned dependencies, weak CI/CD controls, limited auditing) [Sigstore, 2023; SLSA, 2024].

### 4.3 Root issues

- Over‑centralization of trust in a single vendor’s engineering competence and operational integrity.
- Absence of clear industry norms or regulatory pressure requiring diversity and formal verification.
- Misalignment between marketing narratives (“no single point of failure”) and real threat models, leading to complacency [Blog: Cubist, 2024].

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- Growing asset volumes under custody compound the blast radius of any single‑vendor compromise.
- Attackers increasingly target software supply chains and CI/CD rather than only runtime endpoints [Sigstore, 2023].
- Without structural changes, future vulnerabilities in widely‑used protocols or libraries will again propagate instantly across much of the ecosystem.

### 5.2 Early signals

- Public key‑extraction research and incident reports show attackers already understand threshold ECDSA implementations well [Paper: Fireblocks, 2023].
- Vendors and auditors are publishing more detailed blogs and technical deep‑dives on MPC trade‑offs and supply‑chain risk, indicating a shift in industry discourse [Blog: Cubist, 2024].
- Formal‑methods teams are starting collaborations with wallet vendors, but coverage remains limited.

### 5.3 6–24 month scenarios

- **Optimistic**:
  - Major vendors adopt SLSA‑level build attestation, Sigstore signing, and independent re‑implementations for core protocols.
  - Incidents still occur but are localized; correlated failures shrink dramatically.
- **Baseline**:
  - A mix of best‑in‑class and laggards emerges. Some providers reach 2‑implementation setups with partial verification; others remain single‑vendor.
  - At least one moderate incident demonstrates correlated failure but with smaller impact than 2023–2024 events.
- **Pessimistic**:
  - A high‑value vendor suffers CI/CD compromise or ships a backdoored update that drains multiple custodians simultaneously.
  - Regulatory backlash imposes heavy compliance burdens, slowing innovation while not fully solving diversity.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- Several vendors already employ strong cryptography and security engineering teams and have experience operating large‑scale MPC deployments.
- Academic cryptography and formal‑methods communities have mature tools and theory that can be adapted to production stacks [Coq docs, 2023].

### 6.2 Capability gaps

- Shortage of engineers who are simultaneously fluent in production systems, MPC, and formal verification.
- Limited operational experience with multi‑implementation deployments (e.g., cross‑testing independent stacks, managing divergence in behavior).
- Underdeveloped metrics and dashboards for “implementation diversity” and “supply‑chain risk” compared to classic metrics like latency and throughput.

### 6.3 Buildable capabilities (1–6 months)

- Train existing engineering teams on SLSA, Sigstore, and in‑toto patterns for securing build pipelines.
- Contract specialized formal‑methods groups to verify critical protocol components, starting with key generation and signing cores.
- Establish an internal “resilience engineering” function focusing on correlated failure modeling and diversity strategies.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: MPC wallets promise resilience but rely on homogeneous vendor software.
- **Problem**: Software homogeneity and vendor‑centric supply chains recreate a single point of failure.
- **Analysis**: Map internal logic, external stakeholders, historical evolution, and future trends.
- **Options**: Introduce software diversity, formal verification, and hardened supply chains; adjust procurement and regulation.
- **Risks**: Operational complexity, performance regressions, partial adoption, regulatory over‑reach.

### 7.2 Key judgments (for later validation)

1. Independent multi‑implementation deployments significantly reduce correlated failure probability.
2. Supply‑chain security (SLSA‑style attestation, Sigstore) is mandatory but insufficient without diversity.
3. Traders will accept moderately higher latency or risk‑tiered products if trade‑offs are transparent.
4. Regulators are more likely to endorse outcome‑oriented requirements (resilience metrics) than prescriptive protocol choices.

### 7.3 Alternative paths (high level)

- **Path A – Diversity‑first**: Prioritize 2–3 independent implementations per protocol before deep verification.
- **Path B – Verification‑first**: Focus on formal verification of a small number of implementations, accept vendor concentration.
- **Path C – Hybrid**: Combine minimal diversity (≥2 implementations) with incremental verification on the most security‑critical components.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- Security teams may overweight worst‑case scenarios relative to typical attack capabilities.
- Vendors may downplay software homogeneity risk because it threatens their business model.
- Regulators may overreact after incidents, pushing for prescriptive rules that ossify suboptimal designs.

### 8.2 Required intelligence

- Quantitative data on actual implementation diversity across major vendors (number of distinct codebases, languages, build pipelines).
- Empirical measurements of latency vs. security trade‑offs for fully verified vs. non‑verified implementations.
- Incident and near‑miss data specifically involving software supply‑chain compromise and CI/CD intrusions in the crypto industry.

### 8.3 Validation plan

- **Short‑term (0–6 months)**:
  - Survey top MPC wallet vendors and auditors on implementation diversity and verification status.
  - Collect public incident reports and categorize by root cause (protocol design, implementation bug, supply‑chain compromise, operational misconfiguration).
- **Medium‑term (6–18 months)**:
  - Pilot multi‑implementation deployments in at least two institutional setups; track operational complexity and incident rates.
  - Engage independent formal‑methods teams to verify a subset of protocol components and measure engineering cost.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Risk estimates for correlated failure may need adjustment once better data on software diversity and supply‑chain posture becomes available.
- Performance assumptions about fully verified implementations may change as optimization and hardware accelerate cryptography.

### 9.2 Incremental approach

- Start with *bounded diversity* pilots (two implementations for a limited keyset) rather than ecosystem‑wide switchovers.
- Introduce supply‑chain hardening in stages (signing, then attestations, then reproducible builds) to avoid operational overload.

### 9.3 “Good enough” criteria

- At least two independently developed and maintained implementations for any MPC stack securing >$X billion in assets.
- Documented SLSA‑style supply‑chain posture at level N or higher for all critical vendors.
- Clear, versioned threat models and residual risk statements published to institutional customers.

---

## 10. Summary & Action Recommendations

### 10.1 Core insights

- MPC’s theoretical removal of single points of failure is undermined when all parties rely on a single vendor’s software and supply chain.
- The most dangerous risks are *correlated failures* from shared implementations and compromised vendor infrastructure, not just single‑node hacks.
- Achieving genuine resilience requires a combination of software diversity, formal verification, and hardened build pipelines, supported by aligned incentives in procurement and regulation.

### 10.2 Near-term action list (0–3 months)

1. **【P0】 Map software dependency concentration** → Security Architecture Team → Metric: % of assets relying on single‑vendor stacks (baseline ≈90% → target ≤70%) → by 2025‑Q2.
2. **【P0】 Implement minimum supply‑chain controls with Sigstore/SLSA** → Vendor Engineering Leads → Metric: % of critical components with signed, attestable builds (baseline <30% → target ≥70%) → by 2025‑Q3.
3. **【P1】 Launch independent implementation pilots** → Product & Architecture → Metric: # of deployments using ≥2 independent MPC implementations (baseline ~0 → target ≥3) → by 2025‑Q4.
4. **【P1】 Commission external audits and initial formal‑methods assessments** → CISO Organization → Metric: # of components with at least partial machine‑checked proofs (baseline <5% → target ≥20%) → by 2026‑Q1.
5. **【P2】 Develop risk‑tiered product offerings** (e.g., “ultra‑secure” vs. “ultra‑low‑latency”) → Product Management → Metric: share of assets under explicit risk/latency tiering → by 2026‑Q1.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Diversity complexity causes outages or user friction | High | Medium | Increased incidents during rollout of second implementation | Phase rollouts; extensive integration testing; feature flags for fallback | Engineering leads |
| Vendors resist transparency about supply‑chain posture | Medium | High | Delayed or incomplete disclosures | Tie procurement and contracts to disclosure requirements; use third‑party attestations | Procurement & Security |
| Regulatory response is slow or misaligned | Medium | Medium | Major incident without clear regulatory feedback | Proactively engage with regulators; propose outcome‑oriented standards | Legal & Policy |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A – Diversity‑first** | Fast reduction in correlated failure risk; visible to regulators and customers | Higher engineering and ops cost; more complex debugging | Short‑term outages if integration weak; uneven quality across implementations | Multiple qualified vendors or OSS projects exist; strong security mandate | Engineering team is small and already overloaded; no integration budget |
| **B – Verification‑first** | Strong guarantees for one stack; easier operations | Does not reduce dependence on single vendor; long lead time | If that stack is compromised, blast radius remains huge | One implementation already dominates; formal‑methods partners are available | Competitive market with many implementations; need for rapid mitigation |
| **C – Hybrid (recommended)** | Balances resilience and feasibility; supports stepwise adoption | Requires coordination across vendors, auditors, and customers | Governance and incentive alignment are non‑trivial | There is willingness among 2–3 vendors and institutional customers to collaborate | Market is fragmented and adversarial; no partner trust exists |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **MPC (Multi‑Party Computation)** | Cryptographic technique allowing parties to jointly compute a function over their inputs while keeping those inputs private; used for threshold signing in wallets | N/A | [Source: MPC does have a single point of failure, Cubist, 2024] |
| **Threshold ECDSA** | Class of protocols enabling multiple parties to jointly produce an ECDSA signature without reconstructing the private key in one place | N/A | [Paper: Lindell, 2017; Paper: Gennaro & Goldfeder, 2018/2020] |
| **Lindell17** | Two‑party threshold ECDSA protocol widely deployed in early MPC wallets | N/A | [Paper: Lindell, 2017] |
| **GG18/GG20** | Multi‑party threshold ECDSA protocols by Gennaro & Goldfeder used by several MPC wallets | N/A | [Paper: Gennaro & Goldfeder, 2018/2020] |
| **CGGMP20** | UC‑secure non‑interactive proactive threshold ECDSA protocol; basis for some modern MPC wallets | N/A | [Paper: Canetti et al., 2020] |
| **Software supply‑chain attack** | Attack that compromises code, dependencies, or build infrastructure to insert malicious behavior before software is deployed | N/A | [Sigstore, 2023; SLSA, 2024] |
| **SLSA** | Supply‑chain Levels for Software Artifacts – framework defining maturity levels for build integrity and provenance | N/A | [SLSA, 2024] |
| **Sigstore** | Open‑source project providing keyless signing and transparency logs for software artifacts | N/A | [Sigstore, 2023] |
| **Formal verification** | Use of mathematical proof and automated theorem provers to prove properties about protocols or implementations | N/A | [Coq docs, 2023] |
| **Implementation diversity** | Presence of multiple independently developed codebases realizing the same protocol, ideally with distinct languages, teams, and supply chains | N/A | Defined for this analysis |
| **Correlated failure** | Single defect or event causing simultaneous failure across many supposedly independent systems because they share hidden dependencies | N/A | Defined for this analysis |

---

## 12. References

### Tier 1 – Protocols and Vulnerability Research

1. **Lindell, Y.** (2017). *Fast Secure Two‑Party ECDSA Signing*. IACR ePrint. **[Cited in: Context, 2.3, 4.1, Glossary]**. URL as given in problem file.
2. **Gennaro, R., & Goldfeder, S.** (2018/2020). *Threshold ECDSA Protocols (GG18/GG20)*. IACR ePrint. **[Cited in: Context, 2.3, 4.1, Glossary]**. URL as given in problem file.
3. **Canetti, R., Gennaro, R., Goldfeder, S., Makriyannis, N., & Peled, U.** (2020). *UC Non‑Interactive, Proactive, Threshold ECDSA* (CGGMP20). IACR ePrint. **[Cited in: Context, 4.1, Glossary]**.
4. **Makriyannis, N., & Yomtov, A. (Fireblocks).** (2023). *Practical Key‑Extraction Attacks in Leading MPC Wallets*. **[Cited in: Context, 1.1, 2.2, 2.3, 4.1, 4.2, 5.2]**. URL as given in problem file.

### Tier 2 – Industry Reports and Blog Analyses

5. **Cubist**. (2024). *MPC does have a single point of failure*. Cubist Blog. https://cubist.dev/blog/mpc-does-have-a-single-point-of-failure **[Cited in: Context, 1.1, 1.3, 2.2, 2.3, 3.2, 4.3, 5.2]**.
6. **Chainalysis**. (2025). *Crypto Crime Report 2025: $2.2 Billion Stolen in 2024*. Chainalysis. URL as given in problem file. **[Cited in: Context, 1.1, 4.1, 5.1]**.

### Tier 2 – Tooling and Supply Chain Security

7. **Sigstore Project**. (2023). *Sigstore: Software Signing and Transparency Logs*. Project documentation. **[Cited in: 2.3, 3.2, 4.2, 5.1, 6.3, 10.2, Glossary]**.
8. **SLSA Community**. (2024). *Supply‑chain Levels for Software Artifacts (SLSA)*. https://slsa.dev **[Cited in: 1.3, 3.2, 4.2, 5.1, 10.3, Glossary]**.

### Tier 2 – Formal Verification

9. **Coq Development Team**. (2023). *The Coq Proof Assistant Reference Manual*. https://coq.inria.fr **[Cited in: 3.2, 6.1, 6.3, Glossary]**.

### Estimates & Assumptions

10. **Deployment and cost estimates**. As provided in the structured problem statement (engineering headcount, budgets, diversity percentages). Method: synthesis of market sizing, public vendor information, and expert assumptions in the problem file itself. Confidence: Medium. Validation: Surveys and measurement across major MPC wallet vendors. **[Used in: Context Recap, 1.2, 6.3, 10.2]**.
