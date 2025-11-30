# Quantum Computing and Post-Quantum Cryptography Resistance in MPC Wallets (Problem Analysis)

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Cryptography & Security Research Team

---

## Context Recap

- **Problem title**: Quantum Computing and Post-Quantum Cryptography Resistance in MPC Wallets
- **Current state**:
  - 15+ major MPC wallet providers collectively secure **>$50B** in digital assets, all relying on quantum-vulnerable schemes (ECDSA/EdDSA-based threshold signatures, classical hash functions) [Source: Market observation of leading custodial/MPC providers, 2025].
  - No major MPC wallet provider has deployed NIST-standardized post-quantum cryptography (PQC) in production as of late 2025 [Source: Market observation, 2025].
  - NIST finalized first three PQC standards in August 2024 (ML-KEM, ML-DSA/CRYSTALS-Dilithium, SLH-DSA/SPHINCS+) [Source: NIST Releases First 3 Finalized Post-Quantum Encryption Standards, NIST, 2024].
  - Research consensus places cryptographically relevant quantum computers (CRQC) capable of breaking 256-bit ECDSA in roughly the **2030–2040** window, with high uncertainty [Source: The quantum threat to blockchain: summary and timeline analysis, Schärer & Comuzzi, Quantum Machine Intelligence, 2023].
- **Pain points**:
  - **Existential cryptographic break risk**: Shor’s algorithm will break ECDSA/EdDSA once large-scale quantum computers exist, enabling private key extraction and signature forgery for MPC wallets and underlying blockchains [Source: Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer, Shor, SIAM Review, 1999].
  - **Zero PQC deployment** among production MPC wallets despite 5–15 year lead time before likely CRQC, creating a compressed migration window [Source: Market observation, 2025; The quantum threat to blockchain, Schärer & Comuzzi, 2023].
  - **Blockchain protocol dependency**: Even if MPC wallets adopt PQC, Bitcoin and Ethereum remain vulnerable until they add quantum-resistant signature schemes at protocol level [Source: The quantum threat to blockchain, Schärer & Comuzzi, 2023; Fireblocks Blog – How Blockchains Will Evolve for the Quantum Era, Fireblocks, 2025].
  - **Migration complexity and performance overhead**: PQC signatures are larger (e.g., ~2.4KB for Dilithium vs. 64–72B for ECDSA) and slower, stressing MPC protocols, network bandwidth, block space, and mobile devices [Source: NIST PQC Standards Overview, NIST, 2024].
  - **Timeline uncertainty and coordination risk**: Quantum hardware roadmaps show steady progress (e.g., Google’s 53‑qubit Sycamore, IBM’s >100‑qubit processors), but exact timing of CRQC remains uncertain, complicating when to invest heavily in migration [Source: Quantum supremacy using a programmable superconducting processor, Arute et al., Nature, 2019; IBM Quantum breaks the 100-qubit processor barrier, IBM Research Blog, 2021; Forecasting timelines of quantum computing, Sevilla & Riedel, arXiv, 2020].
- **Goals** (aggregated from the problem statement):
  - Deliver **post-quantum MPC wallet architectures** using NIST-standard algorithms and threshold variants.
  - Achieve **testnet PQC MPC wallets** by ~2026 and **production deployments** by ~2027–2028 for ≥50–80% of major providers.
  - Coordinate with Bitcoin/Ethereum communities for **PQC-supporting soft/hard forks** by ~2027–2028.
  - Ensure **zero asset loss** and high user adoption (>60–80% of value) before conservative CRQC arrival (2030–2040).
- **Hard constraints**:
  - Time window **Q4 2025–Q4 2030** to complete research, standardization, implementations, blockchain upgrades, and mass migration [Source: The quantum threat to blockchain, Schärer & Comuzzi, 2023].
  - Budget envelope roughly **$10M–$50M per major provider** plus **$500M–$2B** ecosystem cost for large blockchain upgrades [Source: Market observation and upgrade cost extrapolations from Ethereum Merge and Bitcoin Taproot upgrade histories].
  - Dependence on **NIST threshold cryptography** standardization progress for PQC threshold signatures [Source: Multi-Party Threshold Cryptography project, NIST, 2024].
- **Key facts**:
  - ~3M BTC (~$150B at $50k/BTC) in legacy P2PK addresses are immediately vulnerable once CRQC exists [Source: Committing to quantum resistance: a slow defence for bitcoin, Stewart et al., Royal Society Open Science, 2018].
  - Bitcoin P2PKH and Ethereum account-based models leak public keys at spend/transaction time, enabling quantum key extraction in the broadcast-to-confirmation window [Source: Quantum attacks on Bitcoin, and how to protect against them, Aggarwal et al., Ledger, 2018; Fireblocks Blog – Quantum Era, Fireblocks, 2025].
  - Ethereum’s Account Abstraction (e.g., ERC‑4337) provides a path to per-account cryptographic upgrades, which is highly relevant for PQC migration [Source: Fireblocks Blog – How Blockchains Will Evolve for the Quantum Era, Fireblocks, 2025].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

- **Core problem**: MPC wallet ecosystems today rely on cryptographic primitives (ECDSA/EdDSA threshold signatures, classical hash functions) that will be vulnerable to large-scale quantum computers implementing Shor’s algorithm, yet industry-wide migration to PQC is not underway at sufficient pace.
- **Key contradictions**:
  1. **Security vs. performance**: Post-quantum algorithms (e.g., Dilithium, SPHINCS+) significantly increase key and signature sizes and computational overhead, degrading user experience and throughput, while staying on ECDSA/EdDSA preserves performance but exposes catastrophic quantum risk [Source: NIST PQC Standards Overview, NIST, 2024].
  2. **Urgency vs. uncertainty**: Quantum threat timelines suggest a 5–15 year window before CRQC, yet uncertainty around hardware progress causes many stakeholders to delay investment until signals are clearer, risking a “too late to migrate safely” scenario [Source: Forecasting timelines of quantum computing, Sevilla & Riedel, arXiv, 2020].
  3. **Wallet-level vs. protocol-level fixes**: MPC wallets can adopt PQC internally, but full security depends on base-layer blockchain upgrading its signature schemes; wallets cannot unilaterally eliminate quantum risk if Bitcoin/Ethereum remain classical [Source: The quantum threat to blockchain, Schärer & Comuzzi, 2023].
  4. **Institutional risk mandates vs. cost**: Institutional custodians and regulators will eventually demand quantum resistance, but budget, complexity, and uncertain standards slow down decision-making [Source: Blockdaemon Blog – How AI Agents, MCP, and Post-Quantum Security Are Reshaping DeFi, Blockdaemon, 2024].

### 1.2 Goals & conditions

- **Security goals**:
  - Ensure MPC wallets **remain secure against CRQC-class adversaries** through adoption of PQC-based threshold signatures and quantum-resistant key management.
  - Reduce the fraction of assets on quantum-vulnerable key schemes (ECDSA/EdDSA-only) from ~100% (2025) to **≤10% by 2030**, focusing on high-value institutional holdings first [Estimate: based on staged migration scenarios across major custodians].
- **Operational goals**:
  - Maintain user signing latency **<5 seconds** for threshold PQC signatures in typical MPC wallets (vs. current ~2–3 seconds for ECDSA MPC) [Estimate: based on current Dilithium performance benchmarks with MPC overhead].
  - Keep transaction size overhead manageable (e.g., PQC signature size **≤5KB** for everyday use cases) to avoid unsustainable blockspace and gas costs [Source: NIST PQC Standards Overview, NIST, 2024].
- **Coordination goals**:
  - Achieve **at least 3 major MPC providers’ PQC testnets** by 2026 and **≥50% mainnet PQC support** by 2028.
  - Coordinate with Bitcoin/Ethereum and key L1/L2 ecosystems for **PQC support in protocol and account models** within similar timelines [Source: The quantum threat to blockchain, Schärer & Comuzzi, 2023; Fireblocks Quantum Era Blog, 2025].

### 1.3 Extensibility & reframing

- **By attributes (one object, many attributes)**:
  - Object: *MPC wallet security under quantum threat*.
  - Attributes: signature scheme (ECDSA vs. Dilithium/Falcon/SPHINCS+), key management (single vs. hybrid classical+PQC), blockchain protocol (P2PK/P2PKH/account-based vs. PQC-capable), performance (latency, throughput), user UX (device capability, migration friction), regulatory stance (explicit PQC requirements vs. silence).
- **By structure (virtual vs. physical; latent vs. manifest)**:
  - **Virtual/latent**: cryptographic assumptions (discrete log hardness), error-corrected qubit counts, algorithmic complexity of Shor’s/Grover’s algorithms.
  - **Physical/manifest**: qubit hardware, public key exposure in blockchains, transaction size, MPC protocol round-trips, incident reports.
- **Reframed problem statements**:
  1. From “how to secure MPC wallets against quantum attacks” to **“how to orchestrate a multi-year, multi-stakeholder PQC migration across wallets, blockchains, and infrastructure under uncertainty”**.
  2. From “which algorithm to choose” to **“how to design a hybrid classical+PQC architecture that permits safe iteration as standards and research evolve”**.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Technical components**:
  - Signature schemes: ECDSA/EdDSA vs. PQC (Dilithium, Falcon, SPHINCS+).
  - MPC protocols: distributed key generation, threshold signing, key share storage.
  - Wallet clients: mobile, web, hardware devices handling larger signatures.
  - Infrastructure: HSMs, key management services, node software, analytics.
- **Organizational components**:
  - Crypto research teams designing PQC threshold schemes.
  - Engineering teams implementing and integrating new primitives.
  - Security and compliance teams validating claims and meeting regulatory expectations.
  - Product/UX teams managing user migration flows.

### 2.2 Balance & “degree”

- **Security vs. performance vs. cost**:
  - Over-optimizing for **security** (e.g., using SPHINCS+ exclusively) risks untenable signature sizes (8–49KB) and gas costs on Ethereum-like chains [Source: NIST PQC Standards Overview, NIST, 2024].
  - Over-optimizing for **performance** (staying on ECDSA/EdDSA) ignores quantum risk and could cause complete fund compromise once Q‑Day arrives [Source: The quantum threat to blockchain, Schärer & Comuzzi, 2023].
- **Speed vs. safety of migration**:
  - Aggressive “big bang” migration may reduce exposure window but increases probability of catastrophic implementation bugs in new cryptography.
  - Overly cautious delay reduces near-term cost but increases the chance that CRQC appears before migration is complete.

### 2.3 Causal chains

1. **Research & standards lag → implementation lag → exposure window**:
   - Slow threshold PQC standardization at NIST → wallet providers lack stable, recommended schemes → hesitant to invest → 0% PQC deployment by 2025 → long tail of ECDSA-dependent assets by 2030 [Source: Multi-Party Threshold Cryptography project, NIST, 2024].
2. **Public key exposure → quantum attack surface**:
   - Bitcoin P2PK/P2PKH and Ethereum account-based models expose public keys before or at time of spending → CRQC can derive private keys → attacker forges signatures and sweeps funds → post-factum wallet improvements cannot recover lost assets [Source: Stewart et al., 2018; Aggarwal et al., 2018; Fireblocks Quantum Era Blog, 2025].
3. **Cost and complexity → organizational inertia**:
   - High projected cost ($10M–$50M/provider) + lack of immediate incidents → boards de-prioritize PQC projects → cryptography teams remain understaffed → research and prototypes delayed → further increases migration risk [Estimate: based on aggregate cost structures and historical security upgrade prioritization].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholder matrix

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| **Upstream – Cryptography Researchers / NIST** | Design and standardize PQC + threshold schemes | Secure, efficient, well-analyzed algorithms | Research time, peer review, standardization cycles | Providers push for speed; researchers push for rigor |
| **Upstream – Blockchain Core Devs (BTC/ETH)** | Maintain protocol security and consensus | Add PQC support without fragmenting community | Hard/soft fork coordination, governance politics | Wallets want faster PQC forks; core devs careful about risk |
| **Downstream – MPC Wallet Providers** | Implement and operate MPC wallets | Offer quantum-resistant custody with acceptable UX | Budget, engineering capacity, dependency on NIST/chain decisions | Institutions demand PQC; providers fear cost and performance hit |
| **Downstream – Institutional Users / Custodians** | Hold and manage large asset pools | Protect AUM vs. quantum theft, maintain compliance | Operational risk, migration downtime, internal governance | Pressure providers for PQC; resist disruptive migrations |
| **Sideline – Regulators** | Set security and resilience standards | Ensure systemic stability, investor protection | Limited quantum expertise, slow policy cycles | Too-early mandates vs. innovation chill; too-late mandates vs. systemic risk |
| **Sideline – Quantum Computing Vendors** | Build quantum hardware | Demonstrate capability, capture funding | Hardware scaling, error correction | Their progress shifts threat timeline; disclosures may lag reality |

### 3.2 Environment

- **Technology environment**: Rapid growth in qubit counts, improved coherence times, and more efficient implementations of Shor/Grover drive uncertainty around CRQC arrival [Source: Arute et al., Nature, 2019; IBM Research Blog, 2021].
- **Market environment**: Institutional adoption of crypto assets and DeFi increases the absolute value at risk; leading infrastructure providers market “future-proof security” yet have not shipped PQC in production [Source: Blockdaemon PQC & AI Agents Blog, 2024; Market observation, 2025].
- **Policy environment**: Cryptographic agility and post-quantum readiness are emerging topics in governmental cybersecurity guidance, but explicit mandates for crypto custody are still nascent [Estimate: based on public PQC guidance by NIST and national cyber agencies].

### 3.3 Responsibility & room

- **Where MPC providers must act** (proactive responsibility):
  - Develop PQC-capable MPC architectures, hybrid key schemes, migration tooling, and user education.
- **Where reliance on others is necessary**:
  - On NIST and cryptography community for robust PQC threshold standards.
  - On Bitcoin/Ethereum communities for protocol-level PQC support and safe migration paths.
- **Flexibility**:
  - Providers can design **crypto-agile APIs** now (ability to swap algorithms) even before committing to a specific PQC scheme, preserving room for future adjustments.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **1990s–2000s – Classical assumptions dominate**: Public-key cryptography and elliptic-curve schemes became standard with little practical quantum threat [Source: Shor, 1999].
2. **2016 – NIST PQC competition launched**: Recognition that RSA/ECDSA will be broken by future quantum computers, but focus remained on general internet infrastructure, not blockchains [Source: NIST PQC Competition, NIST, 2016].
3. **2018–2019 – Early blockchain quantum threat analyses**: Academic work quantified Bitcoin exposure and proposed soft forks for quantum resistance, but community urgency remained low [Source: Stewart et al., 2018; Aggarwal et al., 2018].
4. **2023–2024 – PQC standards finalized, quantum hardware milestones**: NIST released ML-KEM and ML-DSA/SLH-DSA standards; Google and IBM announced quantum milestones; blockchain threat analyses highlighted 2030–2040 CRQC window [Source: NIST PQC Standards, 2024; Arute et al., 2019; Schärer & Comuzzi, 2023].

### 4.2 Background vs. direct causes

- **Background causes**:
  - Long lifecycle of cryptographic standards and conservative upgrade patterns.
  - Underestimation of cross-ecosystem coordination complexity (wallets, blockchains, exchanges, regulators).
- **Direct causes**:
  - Lack of production-ready threshold PQC standards.
  - No immediate economic incentive or regulatory mandate for MPC providers to prioritize PQC over nearer-term features.

### 4.3 Root issues

- Structural underinvestment in **cryptographic agility** (systems designed assuming fixed algorithms).
- Misalignment between **short-term revenue goals** and **long-term systemic security**.
- Fragmented responsibility across wallets, blockchains, and regulators, leading to “everyone waits for everyone else” dynamics.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- If migration remains slow and uncoordinated:
  - A large fraction of Bitcoin/Ethereum-based assets will still sit behind ECDSA/EdDSA-only addresses by 2030 [Source: Schärer & Comuzzi, 2023].
  - MPC providers will continue to market “institutional-grade security” that is silently quantum-vulnerable, creating reputational and legal risk once CRQC is demonstrated.
  - In a worst case, early CRQC capability could be exploited secretly by well-resourced actors before public disclosure, leading to unexplained fund drains.

### 5.2 Early signals

- Increasing **PQC coverage in standards and government guidance** (e.g., NIST PQC standards released; national agencies publishing migration guidelines) [Source: NIST PQC Standards, 2024].
- Growing number of **industry whitepapers and blogs** discussing blockchain quantum risk (Fireblocks, Blockdaemon, custodians), even if concrete deployments are not yet live [Source: Fireblocks Quantum Era Blog, 2025; Blockdaemon PQC Blog, 2024].
- Emergence of **crypto-agile wallet architectures** and experimental PQC chains and L2s, indicating a shift toward agility.

### 5.3 Scenarios (2026–2035)

- **Optimistic scenario**:
  - NIST threshold PQC standards mature by 2026; Bitcoin/Ethereum agree on PQC upgrade plans by 2027; leading MPC providers roll out hybrid classical+PQC wallets on testnets (2026) then mainnet (2027–2028). By 2030, >90% of institutional assets are on PQC-capable paths, and CRQC appears closer to 2040 than 2030 [Source: Schärer & Comuzzi, 2023; NIST Threshold Cryptography Project, 2024].
- **Baseline scenario**:
  - Threshold PQC standards take slightly longer; major forks slip to 2028–2029; MPC deployments are partial and heterogeneous. By 2030, 50–70% of high-value assets are PQC-protected, but long tail remains exposed. CRQC appears in mid-2030s, giving just enough time but leaving several high-profile incidents.
- **Pessimistic scenario**:
  - Quantum hardware progress accelerates; practical CRQC appears around 2028–2030 [Source: Sevilla & Riedel, 2020, low-probability but high-impact forecasts].
  - Bitcoin/Ethereum communities remain divided on PQC algorithm choice; forks stall; MPC providers focus on features over infrastructure. Result: systemic loss events and emergency forks under crisis conditions.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- Many MPC providers already have:
  - Strong expertise in **threshold cryptography**, distributed systems, and HSM integration.
  - Established **security review pipelines**, including formal verification and third-party audits.
  - **Institutional relationships** with clients who can co-fund or pilot PQC migration.

### 6.2 Capability gaps

- Limited internal expertise in:
  - PQC algorithm internals (lattice, hash-based, and multivariate schemes).
  - PQC **threshold constructions** and formal security proofs.
  - Performance engineering for **large-signature, high-latency** cryptography on constrained devices.
- Organizational gaps:
  - No dedicated **PQC migration program offices** or cross-team steering committees.
  - Weak integration with **blockchain core developer communities** on PQC roadmap alignment.

### 6.3 Buildable capabilities (1–6 months)

- Short-term investments could build:
  - Small in-house **PQC research squads** to track NIST/academic progress and run prototypes.
  - Partnerships with academia or specialized cryptography consultancies for independent review.
  - Internal **crypto-agility frameworks** (pluggable crypto modules, unified signing APIs) so all products can switch schemes with minimal code changes.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Classical cryptography assumptions, quantum algorithmic breakthroughs (Shor, Grover), blockchain dependence on ECDSA/EdDSA.
- **Problem**: MPC wallets and underlying blockchains are jointly exposed to quantum attacks; migration is complex and multi-stakeholder.
- **Analysis**: Internal structure (protocols, organizations), external environment (quantum hardware, standards, regulation), historical evolution, and future scenarios.
- **Options**: Crypto-agile architecture + hybrid deployment; early PQC pilot with high-value clients; wait-and-see with minimal investment.
- **Risks**: Early CRQC, implementation bugs, fragmented ecosystem standards, user migration failures.

### 7.2 Key judgments (to validate)

1. **P0** – CRQC arrives between 2030–2040 with non-negligible probability earlier than 2035.
2. **P0** – NIST’s chosen PQC schemes (especially Dilithium, SPHINCS+) remain unbroken by classical or quantum cryptanalysis over the next 10–15 years.
3. **P1** – Hybrid classical+PQC architectures can deliver acceptable UX (≤5s signing) for most institutional users.
4. **P1** – Bitcoin/Ethereum governance can agree on PQC upgrade paths in time.
5. **P2** – Significant regulatory pressure for PQC in crypto custody will emerge before Q‑Day.

### 7.3 Alternative paths (one-line positioning)

- **Option A – Proactive hybrid PQC strategy**: Build crypto-agility and hybrid ECDSA+PQC schemes now, migrate high-value clients early.
- **Option B – Standards-following conservative strategy**: Wait for NIST threshold PQC and major blockchain forks, then implement with minimal customization.
- **Option C – Minimalist/defensive strategy**: Focus only on monitoring and contingency, deferring large investments until strong regulatory or market pressure appears.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Security-first bias**: Tendency to over-weight low-probability catastrophic quantum risk vs. near-term opportunity cost.
- **Innovation optimism bias**: Assuming PQC schemes and tools will be straightforward to integrate into MPC without unexpected complexities.
- **Governance optimism bias**: Assuming contentious communities (e.g., Bitcoin) will converge on PQC upgrades faster than historic precedent suggests.

### 8.2 Required intelligence

- Hard data on:
  - **PQC performance benchmarks** in threshold/MPC settings on mobile and server hardware.
  - **User tolerance** for increased signing latency and transaction size.
  - Detailed **governance roadmaps** from Bitcoin/Ethereum communities regarding PQC discussions and proposals.
  - **Regulatory signals** about timelines for expecting PQC in critical financial infrastructure.

### 8.3 Validation plan

- Run **controlled prototypes** of MPC threshold Dilithium/Falcon on representative hardware; benchmark latency, throughput, gas costs.
- Conduct **client interviews** (institutions, custodians) to assess risk appetite, timelines, and willingness to pay for PQC upgrades.
- Monitor **NIST PQC and threshold cryptography publications**, as well as core-dev mailing lists and EIPs/BIPs for explicit PQC proposals.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Timeline estimates for CRQC (earlier or later than 2030–2040) as new hardware results emerge.
- Preferred PQC algorithm mix (e.g., Dilithium vs. Falcon vs. SPHINCS+) as more implementation and attack data become available.
- Migration strategy (e.g., rate of moving retail users) as UX and performance data are gathered.

### 9.2 Incremental approach

- Begin with **low-risk testnets and internal wallets**, then small institutional pilots.
- Expand to **production hybrid deployments** for large institutional clients.
- Only when performance and reliability are proven, roll out to broader retail user bases.

### 9.3 “Good enough” criteria

- Clear, well-supported **hybrid MPC+PQC reference architecture**.
- Demonstrated performance meeting agreed SLOs (e.g., `<5s` signing, acceptable gas fees) on main target platforms.
- Documented and tested **migration runbooks**, including rollback procedures.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. MPC wallets are **structurally dependent** on cryptographic assumptions (ECDSA/EdDSA) that will be invalidated by CRQC, with realistic but uncertain timelines (2030–2040).
2. Security of MPC wallets cannot be fully quantum-resistant without **coordinated upgrades** at the blockchain protocol level (Bitcoin/Ethereum PQC support).
3. NIST’s PQC standards provide a credible starting point, but **threshold/MPC variants** and performance engineering remain open work streams.
4. The economically rational approach is a **phased, hybrid crypto-agile strategy**: early investment in architectures and pilots, not a last-minute emergency migration.

### 10.2 Near-term action list (0–3 months)

**【P0 – Critical】**

1. Establish **PQC migration task force** → CISO / Head of Crypto Research → Milestone: cross-functional roadmap (wallet, infra, product, legal) approved → 2026-02-15.

**【P1 – Important】**

2. Build **crypto-agility layer** in MPC stack (pluggable signature schemes, config-driven algorithms) → Head of Engineering → Metric: 100% of new signing code paths use crypto-agile interfaces → 2026-03-31.
3. Launch **threshold PQC lab prototypes** (Dilithium/Falcon/SPHINCS+) on testnet with synthetic load tests → Research Lead → Metric: benchmark report with latency/throughput vs. ECDSA baseline → 2026-03-31.

**【P2 – Optional】**

4. Draft **external PQC readiness whitepaper** to position provider as forward-looking and attract institutional pilots → Product/Marketing → Metric: whitepaper published and shared with ≥10 key clients → 2026-04-30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| CRQC appears earlier than expected (≤2028) | High | Low–Medium | Rapid quantum hardware breakthroughs, new error-correction results | Accelerate migration, prioritize high-value institutional assets, deploy conservative PQC (e.g., hybrid Dilithium+SPHINCS+) | CISO / PQC Task Force |
| PQC implementations contain critical bugs | High | Medium | New side-channel or implementation attacks against PQC libraries | Use multiple independent implementations, extensive audits, staged rollouts with kill-switches | Head of Security Engineering |
| Ecosystem fragmentation around PQC algorithms | Medium | Medium | Bitcoin/Ethereum choose different schemes; vendors diverge | Design crypto-agility into stack; support multiple PQC schemes where feasible | CTO |
| User resistance to migration / UX degradation | Medium | Medium | Measurable increase in signing times, gas costs, or failure rates | Optimize clients, offload heavy operations to backends, focus PQC on high-value flows first | Head of Product |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Proactive hybrid PQC strategy** | Early risk reduction, reputational leadership, learning curve advantage | High upfront R&D and infra cost; performance engineering effort | Implementation bugs; sunk-cost if standards change | Provider has strong balance sheet, institutional clients, and crypto research team | Cash-constrained, minimal institutional business |
| **B. Standards-following conservative strategy** | Lower early cost; reuses community standards and tooling | Later start, less influence on design; compressed migration window | CRQC arrives before migration completes; customer/regulatory perception of lagging | Provider can rely on others’ research and has low systemic exposure | Provider is systemically important or secures very high-value assets |
| **C. Minimalist/defensive strategy (monitoring only)** | Very low near-term cost; focus on core business | No real preparedness; quantum risk externalized to users/system | High risk of catastrophic loss, legal and reputational damage | Very small providers with negligible systemic impact | Any provider with institutional clients or >$100M AUM |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **BLS Signatures** | Boneh–Lynn–Shacham signature scheme enabling aggregation; used in Ethereum consensus, but vulnerable to quantum hidden-subgroup attacks once CRQC exists. | N/A | [Source: Fireblocks Quantum Era Blog, Fireblocks, 2025] |
| **CRQC (Cryptographically Relevant Quantum Computer)** | Quantum computer with enough logical qubits and low error rates to break widely used public-key schemes (e.g., 256-bit ECDSA) in practical time. | ~3000 logical qubits (order-of-magnitude) | [Source: The quantum threat to blockchain, Schärer & Comuzzi, 2023] |
| **CRYSTALS-Dilithium** | Lattice-based post-quantum digital signature scheme standardized by NIST (ML-DSA). Balances performance and key size (≈2.4KB signatures). | Signature ~2.4KB | [Source: NIST PQC Standards, NIST, 2024] |
| **ECDSA (Elliptic Curve Digital Signature Algorithm)** | Widely used digital signature scheme for Bitcoin, Ethereum, and many MPC wallets; broken by Shor’s algorithm on CRQC. | 256-bit keys, 64–72B signatures | [Source: Shor, 1999; NIST FIPS 186 series] |
| **Falcon** | Lattice-based PQC signature candidate with compact signatures (~0.7KB) but higher implementation complexity than Dilithium. | ≈0.7KB signatures | [Source: NIST PQC Candidate Documentation, NIST, 2024] |
| **Hybrid Cryptography** | Use of both classical and post-quantum schemes in parallel (e.g., ECDSA + Dilithium) so security holds if either remains unbroken. | N/A | [Source: NIST PQC Migration Guidance, NIST, 2024] |
| **MPC (Multi-Party Computation) Wallet** | Wallet architecture where keys are split into shares across multiple parties/devices; signing requires threshold cooperation, reducing single-point-of-failure risk. | N/A | [Source: MPC Wallet Architecture Whitepapers from major custodians, 2020–2024] |
| **P2PK / P2PKH** | Bitcoin script types; P2PK reveals public keys at rest, P2PKH reveals them at spending time, both vulnerable to quantum key extraction once public key is visible. | N/A | [Source: Stewart et al., 2018; Aggarwal et al., 2018] |
| **PQC (Post-Quantum Cryptography)** | Cryptographic schemes believed secure against known quantum attacks, including lattice-based and hash-based constructions. | N/A | [Source: NIST PQC Standards, NIST, 2024] |
| **Q‑Day** | Hypothetical date when practical CRQC becomes available to adversaries, enabling large-scale breaks of classical cryptosystems. | Date (uncertain, ~2030–2040) | [Source: Schärer & Comuzzi, 2023; Sevilla & Riedel, 2020] |
| **SPHINCS+** | Stateless hash-based PQC signature scheme standardized by NIST (SLH-DSA); conservative assumptions but large signatures (8–49KB). | 8–49KB signatures | [Source: NIST PQC Standards, NIST, 2024] |

---

## 12. References

### Tier 1 Sources (Peer-Reviewed, Official Documentation)

1. **NIST**. (2024). *NIST Releases First 3 Finalized Post-Quantum Encryption Standards* (FIPS 203, 204, 205). https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards  
   **Cited in**: Context Recap, Sections 1.1, 2.2, 5.2, 10.1, 11.
2. **Schärer, K., & Comuzzi, M.** (2023). *The quantum threat to blockchain: summary and timeline analysis*. Quantum Machine Intelligence, 5(1). https://doi.org/10.1007/s42484-023-00105-4  
   **Cited in**: Context Recap, Sections 1, 2, 3, 4, 5, 10, 11.
3. **Shor, P.** (1999). *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer*. SIAM Review, 41(2): 303–332.  
   **Cited in**: Context Recap, Sections 1, 4, 11.
4. **Arute, F., et al. (Google)**. (2019). *Quantum supremacy using a programmable superconducting processor*. Nature 574(7779):505–510. https://doi.org/10.1038/s41586-019-1666-5  
   **Cited in**: Context Recap, Sections 3, 5.
5. **Aggarwal, D., et al.** (2018). *Quantum attacks on Bitcoin, and how to protect against them*. Ledger, 3.  
   **Cited in**: Context Recap, Sections 2, 3, 5, 11.
6. **Stewart, K., et al.** (2018). *Committing to quantum resistance: a slow defence for bitcoin against a fast quantum computing attack*. Royal Society Open Science 5(6):180410. https://doi.org/10.1098/rsos.180410  
   **Cited in**: Context Recap, Sections 2, 3, 4, 5, 11.
7. **Sevilla, J., & Riedel, C.** (2020). *Forecasting timelines of quantum computing*. arXiv:2009.05045.  
   **Cited in**: Context Recap, Sections 1, 5, 10.

### Tier 2 Sources (Industry Reports, Established Organizations, Technical Blogs)

8. **IBM Research**. (2021). *IBM Quantum breaks the 100-qubit processor barrier*. https://research.ibm.com/blog/127-qubit-quantum-processor-eagle  
   **Cited in**: Context Recap, Sections 3, 5.
9. **Fireblocks**. (2025). *Part 2: How Blockchains Will Evolve for the Quantum Era*. https://www.fireblocks.com/blog/how-blockchains-will-evolve-for-the-quantum-era  
   **Cited in**: Context Recap, Sections 1, 2, 3, 5.
10. **Blockdaemon**. (2024). *How AI Agents, MCP, and Post-Quantum Security Are Reshaping DeFi*. https://www.blockdaemon.com/blog/how-ai-agents-mcp-and-post-quantum-security-are-reshaping-defi  
    **Cited in**: Sections 1, 3, 5.
11. **NIST**. (Ongoing). *Multi-Party Threshold Cryptography Project*. https://csrc.nist.gov/projects/threshold-cryptography  
    **Cited in**: Sections 1, 2, 5.

### Internal / Market Observation

12. **Market observation – MPC wallet providers**. (2025). Manual scan of major MPC wallet providers (Fireblocks, Coinbase WaaS, ZenGo, BitGo, Web3Auth, Privy, Magic, Turnkey, Fordefi, Dfns, Portal, Torus, Safeheron, Cobo, Qredo).  
    - Description: All rely on classical ECDSA/EdDSA; no production PQC deployment as of Nov 2025.  
    **Cited in**: Context Recap, Sections 1, 3, 5.

13. **Upgrade history – Bitcoin Taproot & Ethereum Merge**. (2019–2022). Public documentation and release notes for Taproot (Bitcoin) and the Merge (Ethereum).  
    - Description: Multi-year coordination timelines for major cryptographic/consensus changes.  
    **Cited in**: Context Recap, Section 5.
