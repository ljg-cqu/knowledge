# Weak Randomness and Entropy in MPC Wallet Key Generation and Signing – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Security & Cryptography Team

---

## Pre-Section: Context Recap

- **Problem title**: Weak randomness and entropy in MPC wallet key generation and signing
- **Current state**:
  - Modern MPC wallets (e.g., GG18/GG20/CGGMP20/CGGMP21, FROST-style schemes) rely on high-entropy randomness for distributed key generation (DKG) and per-signature nonces, often drawing from OS PRNGs, cloud VMs, browser APIs, secure elements, TEEs, or HSMs. [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025]
  - Historical non-MPC incidents (Android SecureRandom bug, Profanity vanity address generator, Trust Wallet browser extension flaw, "Blockchain Bandit" weak keys) show that low-entropy seeds or nonces alone can enable private key recovery and large-scale theft. [Source: Android bug batters Bitcoin wallets, Bitcoin.org Alert, 2013; Source: Ethercombing: Finding Secrets in Popular Places, ISE, 2019; Source: Explained: The Profanity Address Generator Hack, Halborn, 2022; Source: Funds of Every Wallet Created with the Trust Wallet Browser Extension Could Have Been Stolen, Ledger, 2023]
  - NIST SP 800‑90A/B and FIPS 140‑2/140‑3 define requirements for entropy sources and DRBGs, but most MPC deployments do not yet provide explicit, audit-ready guarantees about effective entropy per key/nonce or continuous RNG health monitoring. [Source: NIST SP 800‑90B, NIST, 2018; Source: Entropy Validation in FIPS 140‑3, Lightship Security, 2021]
- **Pain points**:
  - **Silent systemic compromise risk**: Keys and nonces generated with insufficient entropy may be retrospectively brute-forced; compromises can look like generic "hacks" rather than entropy failures. [Source: Tangem – Old Wallets, Weak Keys, 2024; Source: Ethercombing, ISE, 2019]
  - **Low observability**: RNG misconfiguration (wrong API, bad seeding, entropy starvation) is rarely surfaced in wallet metrics or logs; many incidents emerge only after fund loss. [Source: NIST SP 800‑90B, 2018]
  - **Fragmented responsibility**: OS vendors, cloud providers, hardware vendors, library maintainers, and wallet teams each own part of the RNG chain; no single party currently guarantees end-to-end entropy quality for MPC wallets. [Source: AWS Web3 Blog – Build secure MPC wallets using AWS Nitro Enclaves, 2024; Source: Stackup, 2025]
- **Goals (from problem statement, quantified)**:
  - **Randomness quality**: Verifiably strong entropy sources with ≥128‑bit (min) / ≥192‑bit (target) / ≥256‑bit (ideal) effective entropy per key and nonce; use standardized estimation and, where possible, certified HRNGs. [Source: NIST SP 800‑90B, 2018]
  - **Coverage**: 100% of MPC cosigners and key-generation endpoints under hardware-backed or formally validated RNG (no unverified OS-only or browser-only entropy paths in production). [Source: Stackup, 2025]
  - **Incident reduction**: Drive randomness-related custody incidents to 0/year internally and ≤1 serious public incident/decade ecosystem-wide, as identified by root-cause analyses. [Source: Tangem, 2024]
  - **Detection capability**: Continuous RNG health monitoring with alerting and automatic signing halt for affected cosigners within <1 hour (min) / <15 minutes (target). [Source: NIST SP 800‑90B, 2018]
  - **Key generation assurance & legacy risk reduction**: By Q4 2026, 100% of new keys have documented entropy provenance; by end-2027, ≥80–95% of assets held under keys with verified entropy, with legacy keys systematically migrated. [Estimate: Based on typical key-migration and regulatory timelines, Medium confidence]
- **Hard constraints**:
  - Long migration horizon (2025–2027), limited RNG experts, diverse hardware (mobile secure elements, TEEs, older HSMs, browsers), and signing-latency SLOs (2–15s) constrain how aggressively entropy checks can be added. [Source: Stackup, 2025; Source: AWS Web3 Blog, 2024]
  - Many legacy keys were created under unknown RNG conditions; mass rotation is operationally disruptive and may require client consent and regulatory approvals. [Source: Ledger, 2023; Source: Tangem, 2024]

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

1. **Core problem**  
   MPC theoretically prevents any single device from holding the full private key, but this security model assumes strong, independent randomness at each participant during DKG and signing. In reality, many cosigners share the same OS/library RNGs, lack explicit entropy validation, or run in environments (browser, startup-starved VMs) known to have entropy weaknesses. A single class of entropy failure can therefore undermine threshold guarantees across many keys and wallets. [Source: Stackup, 2025; Source: Tangem, 2024; Source: NIST SP 800‑90B, 2018]

2. **Contradictions**
   - **Distributed cryptography vs. centralized entropy risk**: MPC removes key-centralization at the protocol level, yet centralizes risk in a small number of RNG implementations and entropy sources. [Source: Ethercombing, ISE, 2019]
   - **Performance/portability vs. rigorous RNG design**: Using default OS PRNGs or browser APIs minimizes engineering effort but rarely comes with NIST-style entropy models, tests, or attestations. [Source: NIST SP 800‑90A/B, 2015/2018]
   - **External trust claims vs. internal uncertainty**: Marketing and audits often claim "no single point of failure" while internal teams cannot quantitatively state effective entropy for keys and nonces. [Source: Tangem, 2024]

3. **Who is in conflict?**
   - Product teams optimizing UX and launch timelines vs. cryptography engineers insisting on HRNGs, more logging, and validation.
   - Wallet vendors wanting to treat RNG as a black box vs. institutional clients and regulators demanding transparency and attestations. [Source: Ledger, 2023]

### 1.2 Goals and conditions

- **Entropy sufficiency**: Establish organization-wide minimums (e.g., ≥128 bits effective entropy for all production keys/nonces, higher for high-value accounts) and map RNG designs against these targets. [Source: NIST SP 800‑90B, 2018]
- **Coverage and monitoring**: Ensure all cosigners use approved RNGs with startup and online health tests; integrate alerts with existing incident-response processes.
- **Legacy remediation**: Prioritize migration of high-value and high-risk key cohorts (e.g., keys from browser-based generation, old SDKs) under constrained operational and regulatory windows. [Source: Ledger, 2023]

### 1.3 Extensibility and reframing

- **From "randomness bug" to "entropy supply chain"**: View entropy as a supply chain spanning hardware, firmware, OS, libraries, and application code, each with its own guarantees and failure modes. [Source: NIST SP 800‑90B, 2018]
- **From "implementation detail" to "first-class control"**: Treat RNG design like key storage or HSM policy—visible in threat models, audits, and SLAs.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- Entropy sources (HRNGs in secure elements/HSMs/TEEs, OS entropy pools, timing/user input, cloud entropy services). [Source: NIST SP 800‑90B, 2018; Source: Tangem, 2024]
- DRBGs (CTR_DRBG, Hash_DRBG, etc.) that expand entropy into pseudorandom streams used by MPC protocols. [Source: NIST SP 800‑90A, 2015]
- MPC components (DKG, signing cosigners, orchestration) that request randomness.
- Configuration, seeding, reseeding intervals, and fallback behavior.
- Monitoring, logging, and attestation of RNG state.

### 2.2 Balance and "degree" issues

- More aggressive health tests and reseeding improve assurance but cost CPU and may add latency to signing. [Source: NIST SP 800‑90B, 2018]
- Strong dependence on hardware RNGs raises assurance but increases coupling to specific devices and vendors.

### 2.3 Causal chains

- **Nonce predictability chain**: Weak or reused nonces (faulty RNG or seeding) → signatures on-chain → attacker runs lattice/analytic attacks to recover keys → full-key compromise (Android SecureRandom, repeated-nonce studies). [Source: Bitcoin.org Android Alert, 2013; Source: Biased Nonce Sense, IACR ePrint 2019/023]
- **Library/tool failure chain**: Popular tool uses 32-bit or otherwise weak seeds (Profanity, Trust Wallet bug) → thousands of keys share tiny keyspace → attacker brute-forces keys → large thefts (Wintermute, others). [Source: Halborn, 2022; Source: CVE‑2023‑31290, 2023]

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and conflicts

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| MPC wallet providers | Design/operate MPC infra | Strong security, low latency, differentiated features | Limited RNG expertise, legacy code, vendor dependencies | Security teams vs. product/ops on complexity and timelines |
| Institutional clients | Hold large assets via MPC | Proof that keys/nonces are unguessable; auditability | Little visibility into RNG internals; costly key rotations | Demand attestations vs. vendor reluctance to expose details |
| Hardware/secure-element/HSM vendors | Provide HRNGs and certified modules | Sell chips, pass FIPS/CC; promote HRNG | Slow silicon/cert cycles; generic docs | Wallet vendors need wallet-specific guarantees |
| Cloud & TEE providers | Expose RNG/HRNG APIs | Secure multi-tenant RNG, maintain uptime | Shared infra, broad customer base | Wallets want strong assurances; clouds provide generic ones |
| Regulators/auditors | Oversee custody risk | Simple, testable RNG requirements | Limited cryptography depth | Want prescriptive rules; industry prefers flexible guidance |

[Source: Stackup, 2025; Source: Ledger, 2023; Source: Tangem, 2024]

### 3.2 Environment

- Increasing regulatory focus on custody and key-management controls.
- More public case studies synthesizing entropy-related failures (Tangem, security blogs).
- FIPS 140‑3 and NIST publications giving concrete entropy validation frameworks.

### 3.3 Responsibility & room for maneuver

- Wallet providers: choose and validate RNG designs, implement monitoring, and lead key migrations.
- Hardware/cloud vendors: document RNG properties and expose attestable APIs.
- Clients and regulators: set expectations (e.g., "keys must be generated under NIST-aligned entropy sources").

---

## 4. Origins of the Problem (Aspect 4)

- Early reliance on platform PRNGs without entropy modeling.
- Android SecureRandom and later incidents showing real-world exploitation.
- Tooling and SDK ecosystems (vanity generators, browser extensions) prioritizing convenience and speed over entropy.
- Slow diffusion of NIST/FIPS entropy guidance into wallet development practices. [Source: NIST SP 800‑90B, 2018; Source: Ethercombing, ISE, 2019; Source: Halborn, 2022]

---

## 5. Problem Trends (Aspect 5)

- Assets under MPC custody are growing rapidly; the blast radius of any systemic RNG design flaw increases accordingly. [Source: Stackup, 2025]
- Attackers have demonstrated patience and automation in scanning for weak keys/nonces (Blockchain Bandit, vanity exploits). [Source: Ethercombing, ISE, 2019]
- Standards and lab capability for entropy validation are improving, but adoption in wallets is uneven and mostly concentrated among top-tier providers. [Source: Lightship Security, 2021; Source: SafeLogic, 2020]

Scenarios (6–36 months):
- **Optimistic**: Wide adoption of NIST-aligned entropy validation, hardware RNG usage, and per-key attestations; incidents become rare and localized.
- **Baseline**: Leading providers implement strong RNG controls; others lag; occasional large entropy-related incidents drive incremental regulation.
- **Pessimistic**: A major MPC SDK or environment is found to have low effective entropy for years, leading to multi-institutional compromise and forced, rapid migrations.

---

## 6. Capability Reserves (Aspect 6)

- Existing strengths: mature standards (NIST SP 800‑90A/B, FIPS 140‑3), hardware RNGs in secure elements/HSMs/TEEs, security teams at major custodians.
- Gaps: lack of end-to-end RNG inventories, limited entropy expertise, weak runtime monitoring, and minimal per-key provenance.
- Buildable capabilities (1–12 months):
  - Define an internal RNG architecture standard (approved entropy sources, DRBGs, health tests).
  - Implement RNG health monitoring for MPC cosigners.
  - Add entropy provenance fields to key ceremonies and signing logs.

---

## 7. Analysis Outline (Aspect 7)

- **Background**: Historical entropy failures, current MPC randomness dependencies.
- **Problem**: Single-class entropy failure can undermine MPC guarantees at scale.
- **Analysis**: Internal structure (sources, DRBGs, cosigners), external stakeholders and standards, historical roots and trend scenarios.
- **Options**: Hardware-centric RNG, hybrid RNG architectures, entropy provenance/attestation, legacy key migration.
- **Risks**: Operational disruption during migrations, performance impact, partial adoption, residual blind spots.

Key judgments (to validate):
- Entropy risk in MPC is material and under-addressed.
- NIST/FIPS approaches can be adapted to wallets without unacceptable performance impact.
- Combining hardware RNGs, validation, and monitoring is more robust than any single technique. [Source: NIST SP 800‑90B, 2018; Source: Tangem, 2024]

---

## 8. Validating the Answer (Aspect 8)

Potential biases:
- Over-reliance on published incident reports (under-reporting likely).
- Vendor-documentation bias for RNG implementations.

Required intelligence:
- Inventory of RNG architectures across all MPC components and vendors.
- Empirical entropy estimates and health-test results for production RNGs.
- Performance benchmarks for stronger RNG designs under realistic MPC workloads.

Validation plan:
- Conduct architecture/RNG reviews with each MPC provider.
- Run pilot deployments of HRNG-backed MPC cosigners with monitoring and measure latency/throughput.
- Simulate key-migration campaigns on a subset of clients to quantify operational impact.

---

## 9. Revising the Answer (Aspect 9)

Likely revision points:
- Estimated prevalence of weak-entropy keys in existing deployments.
- Performance overhead of more rigorous RNG designs.
- Regulatory expectations and insurance requirements as they evolve.

Incremental approach:
- Start with explicit RNG documentation and inventories.
- Introduce monitoring and provenance for new keys and high-value flows first.
- Gradually extend standards and migrations across the portfolio.

"Good enough" criteria:
- No new keys generated without approved RNG and basic monitoring.
- Clear view of the highest-risk legacy key cohorts and a concrete remediation plan.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

- Weak or poorly engineered entropy can silently collapse MPC’s security model by making keys and nonces guessable despite correct protocol implementation.
- Real-world incidents demonstrate that entropy failures are exploitable at scale and often go undetected for long periods.
- Applying NIST/FIPS-style entropy validation, leveraging hardware RNGs, and adding monitoring/provenance can materially reduce systemic risk.

### 10.2 Near-term action list (0–12 months)

Format: **[Priority] Action → Owner → Metric (baseline → target) → Date**

1. **【P0】 Establish RNG architecture standard and inventory → Crypto Engineering Lead → Coverage of components with documented RNG design: 0% → 100% → 2026-03-31**
2. **【P0】 Implement RNG health monitoring for all MPC cosigners → Security/SRE → Cosigners with startup + online RNG tests: 0% → ≥80% → 2026-06-30**
3. **【P1】 Add entropy provenance to new key ceremonies → Wallet Backend Team → New keys with recorded RNG/entropy metadata: 0% → 100% → 2026-09-30**
4. **【P1】 Define legacy key risk tiers and migration roadmap → Risk & Product → Share of assets under "high-risk entropy" keys: unknown → quantified + plan approved → 2026-09-30**

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Migration causes downtime or user friction | High | Medium | Large-scale key rotations | Phase migrations; strong comms; dual-key periods | Product & Ops |
| Undiscovered RNG dependencies remain | High | Medium | Post-incident forensics reveal hidden RNG usage | Comprehensive inventories; mandatory architecture reviews | Architecture Board |
| Performance degradation from stronger RNGs | Medium | Medium | Signing latency regressions | Benchmark; optimize hot paths; prioritize HRNG for high-value flows | SRE |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A: Minimal uplift (fix known bugs, ensure CSPRNG APIs)** | Low engineering cost, fast rollout | No quantitative entropy guarantees | Latent systemic risk remains | For low-value test environments | For institutional custody or high-value wallets |
| **B: Standards-aligned RNG (NIST 800‑90B style)** | Strong assurance, aligns with regulators | Medium engineering/testing effort | Partial adoption if not enforced org-wide | When organization can allocate RNG experts | When team lacks capacity even for basic validation |
| **C: End-to-end entropy governance (B + provenance/migration)** | Maximum long-term resilience and auditability | High upfront effort, complex migrations | Short-term disruption if rushed | For major custodians and systemically important providers | For small teams without regulatory pressure |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **Entropy (cryptographic)** | Measure of unpredictability in random values used for keys and nonces; higher entropy means harder to guess or brute-force. | bits | [Source: NIST SP 800‑90B, 2018] |
| **Hardware Random Number Generator (HRNG)** | RNG implemented in hardware (secure elements, HSMs, TEEs) drawing entropy from physical noise sources and usually including built-in health tests. | N/A | [Source: Tangem, 2024] |
| **Deterministic Random Bit Generator (DRBG)** | Algorithm that expands a seed of true entropy into a longer pseudorandom sequence for cryptographic use. | N/A | [Source: NIST SP 800‑90A, 2015] |
| **Distributed Key Generation (DKG)** | MPC protocol where multiple parties jointly generate shares of a private key without ever reconstructing the full key. | N/A | [Source: Stackup, 2025] |
| **Nonce (ECDSA/Schnorr)** | One-time random value used per signature; reuse or predictability can leak the private key. | N/A | [Source: Biased Nonce Sense, IACR ePrint 2019/023] |
| **Blockchain Bandit** | Pseudonymous attacker identified for systematically draining Ethereum addresses created with weak keys. | N/A | [Source: Ethercombing, ISE, 2019] |
| **Profanity** | Ethereum vanity address tool that used only 32 bits of entropy for seeds, enabling brute-force of keys and large thefts. | N/A | [Source: Halborn, 2022] |
| **RNG health monitoring** | Continuous or periodic checks on RNG output (statistical tests, self-tests) to detect failures or degradation. | N/A | [Source: NIST SP 800‑90B, 2018] |
| **Entropy provenance** | Recorded information about RNG sources, configuration, and tests used when generating a key or nonce. | N/A | Defined in this analysis |
| **FIPS 140‑3 entropy validation** | Validation process ensuring entropy sources in cryptographic modules meet NIST requirements; often indicated by ENT/ESV designations. | N/A | [Source: Lightship Security, 2021] |

---

## 12. References

### Tier 1 – Primary Standards, Advisories, and Case Studies

1. **NIST.** (2018). *SP 800‑90B: Recommendation for the Entropy Sources Used for Random Bit Generation*. National Institute of Standards and Technology. https://csrc.nist.gov/pubs/sp/800/90/b/final  
   **[Cited in**: Context Recap; Sections 1–3, 5–8, 10–11 **]**
2. **NIST.** (2015). *SP 800‑90A Rev.1: Recommendation for Random Number Generation Using Deterministic Random Bit Generators*. NIST.  
   **[Cited in**: Sections 2, 6, 7, 11 **]**
3. **Bitcoin.org.** (2013). *Android Security Vulnerability Alert*. https://bitcoin.org/en/alert/2013-08-11-android  
   **[Cited in**: Context Recap; Sections 2, 4, 5 **]**
4. **Independent Security Evaluators (ISE).** (2019). *Ethercombing: Finding Secrets in Popular Places*. ISE. https://www.ise.io/casestudies/ethercombing  
   **[Cited in**: Context Recap; Sections 2–5, 10 **]**
5. **GitHub / CVE‑2023‑31290.** (2023). *Trust Wallet Core entropy vulnerability advisory (GHSA‑pm4f-pggw-8jwc)*.  
   **[Cited in**: Context Recap; Sections 2, 4 **]**

### Tier 2 – Industry Blogs, Technical Guides, and Vendor Documentation

6. **Stackup.** (2025). *MPC Wallets: A Complete Technical Guide*. Stackup.  
   **[Cited in**: Context Recap; Sections 1–3, 5–7, 10–11 **]**
7. **Tangem.** (2024). *Old Wallets, Weak Keys: How Poor Entropy Still Drains Millions in Crypto*; *Why Entropy Source in Private Key Generation is Important*. Tangem Blog.  
   **[Cited in**: Context Recap; Sections 1–3, 5–7, 10–11 **]**
8. **Halborn.** (2022). *Explained: The Profanity Address Generator Hack*. Halborn Blog.  
   **[Cited in**: Context Recap; Sections 2, 4–5, 11 **]**
9. **Ledger.** (2023). *Funds of Every Wallet Created with the Trust Wallet Browser Extension Could Have Been Stolen*. Ledger Blog.  
   **[Cited in**: Context Recap; Sections 1, 3–5, 10 **]**
10. **AWS Web3.** (2024). *Build secure multi-party computation (MPC) wallets using AWS Nitro Enclaves*. Amazon Web Services.  
    **[Cited in**: Context Recap; Sections 2–3, 6–7 **]**

### Tier 2 – Entropy Validation and Certification

11. **Lightship Security.** (2021). *Entropy Validation in FIPS 140‑3 (ENT vs ESV)*. Lightship Security Blog.  
    **[Cited in**: Context Recap; Sections 5–7, 11 **]**
12. **SafeLogic.** (2020). *A Brief History of Entropy Validation in FIPS 140*. SafeLogic Blog.  
    **[Cited in**: Sections 5–7 **]**
