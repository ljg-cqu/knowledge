# Key-Extraction Attack Vulnerabilities in MPC Wallet Implementations – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Security Team

---

## Pre-Section: Context Recap

- **Problem title**: Key-extraction attack vulnerabilities in threshold ECDSA–based MPC wallet implementations
- **Current state**:
  - Widely deployed threshold ECDSA protocols (Lindell17, GG18/20) underpin major MPC wallets used by Coinbase WaaS, ZenGo, Binance, BitGo, ING and others, securing hundreds of billions of dollars in assets
    [Source: Practical Key-Extraction Attacks in Leading MPC Wallets, Makriyannis et al., 2023, Cryptology ePrint Archive 2023/1234, Abstract].
  - Researchers demonstrated practical key-extraction attacks requiring from 10^6 down to 1 malicious signing session depending on the protocol/implementation
    [Source: Makriyannis et al., 2023, ePrint 2023/1234, Abstract].
  - Some providers have deployed partial mitigations (e.g., ZenGo, Coinbase, Safeheron), but multiple GG18/20-style implementations remain at risk due to weak Paillier key validation and missing abort-on-failure semantics
    [Source: Fireblocks Vulnerability Disclosure Blog, Fireblocks, 2023].
- **Pain points**:
  - Single corrupted signing party can exfiltrate the full private key without triggering obvious alarms in naïvely implemented Lindell17 or GG18/20 flows
    [Source: Makriyannis et al., 2023, ePrint 2023/1234, Sections 1–2].
  - Private key compromise remains the dominant infrastructure failure mode, with infrastructure attacks (private key and seed phrase compromises) accounting for nearly 70% of USD 2.2B stolen in 2024
    [Source: 2025 Crypto Crime Report, TRM Labs, 2025, "USD 2.2 billion was stolen in crypto-related hacks"].
  - Operationally, retrofitting protocols that are already in production (with live key shares) is complex and risky for uptime and UX.
- **Goals**:
  - Eliminate exploitable key-extraction vulnerabilities in deployed MPC wallets (Lindell17 and GG18/20 families) by Q2 2025, targeting 0 known vulnerable production implementations
    [Source: Problem statement – Goals and success criteria].
  - Deploy runtime detection and throttling for malicious signing patterns with <100 ms detection latency and near-100% recall for attack traces.
  - Achieve ≥2 independent security audits per provider confirming closure of the specific key-extraction vectors
    [Source: Problem statement – Goals and success criteria].
- **Hard constraints**:
  - Six‑month remediation window (Q4 2024–Q2 2025) with budget roughly USD 200–500k per provider
    [Source: Problem statement – Key constraints and resources].
  - Must maintain ~99.9% service uptime and avoid forced key rotation for 100M+ end users, except as last resort
    [Estimate based on: provider SLAs and UX constraints in major custodial services, Medium confidence].
  - Backward compatibility with existing key shares and address space is required (no mass migration of assets to new wallets unless critical).
- **Key facts**:
  - Threshold ECDSA protocols Lindell17 and GG18/20 have strong theoretical security proofs, but their real-world security depends on enforcing abort-on-failure and validating Paillier and auxiliary keys with appropriate zero-knowledge proofs
    [Source: UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts, Canetti et al., 2020 CCS / ePrint 2021/060, Abstract].
  - Infrastructure attacks focusing on keys and seeds are the dominant driver of losses, with USD 2.2B stolen in 2024 and infrastructure attacks responsible for nearly 70% of stolen funds
    [Source: 2025 Crypto Crime Report, TRM Labs, 2025, "USD 2.2 billion was stolen in crypto-related hacks"].
  - MPC wallets mitigate single-point-of-failure of conventional EOAs but do not magically remove risks from protocol-level and implementation-level flaws
    [Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025, Sections "What Is an MPC Wallet?" and "Security Benefits and Trade-offs of MPC Wallets"].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

1. **Core problem**  
   Implementations of Lindell17 (2-of-2) and GG18/20 (n-of-n) threshold ECDSA in production MPC wallets allow a malicious party participating in signing ceremonies to extract the complete private key after a relatively small number of signing sessions (16–256 in the typical vulnerable variants), due to missing abort logic and insufficient Paillier key validation
   [Source: Makriyannis et al., 2023, ePrint 2023/1234, Attack Overview].

2. **Contradictions**
   - **Security vs. latency/complexity**: Providers optimized for low-signing latency and simpler key management, but skipped or weakened heavy zero-knowledge proofs and strict validation flows that are necessary to achieve the proven security bounds
     [Source: Canetti et al., 2020 CCS / ePrint 2021/060, Protocol Properties].
   - **Theoretical vs. implemented guarantees**: Protocol proofs assume honest-abort and validated keys; implementations often treat these as optional engineering details, creating a gap between "proven secure" and "actually secure"
     [Source: Makriyannis et al., 2023, ePrint 2023/1234, Discussion of assumptions].
   - **Custody scale vs. change risk**: Providers secure tens of billions of dollars and millions of users; any disruptive protocol or key migration incurs substantial operational and regulatory risk
     [Source: Coinbase Q3 2023 Earnings and Institutional AUM reports; Problem statement – Impact scope].

3. **Who is in conflict?**
   - Security engineers demanding strict key validation, abort logic, and aggressive monitoring.
   - Product/operations teams prioritizing UX, uptime, and minimal user-visible changes.
   - Regulators pushing for demonstrable control of custody risk versus providers wary of publicizing vulnerabilities.

### 1.2 Goals and conditions

- **Security goal**: Reduce exploitable key-extraction attack surface to zero for production MPC wallets based on Lindell17/GG18/20, while maintaining non-custodial or shared-custody guarantees.
- **Detection goal**: Real-time or near-real-time detection of anomalous signing patterns (e.g., repeated failed signatures, unusual message distribution, abnormal request rates per counterparty) with <100 ms additional latency at P95
  [Estimate based on: typical MPC signing latency budgets of 100–300 ms, Stackup 2025, "Performance Benchmarks and Limitations"].
- **Remediation goal**: Patch all affected production systems within 3 months of confirmed vulnerability, including library upgrades, configuration changes, and new monitoring dashboards
  [Source: Problem statement – Goals and success criteria].
- **Validation goal**: Achieve ≥2 independent third-party audits per major provider confirming absence of the specific key-extraction vectors and soundness of new controls 
  [Source: Problem statement – Goals and success criteria].

### 1.3 Extensibility and reframing

- **Attribute reframing – "one object, many attributes"**:  
  The "object" is the MPC wallet infrastructure; critical attributes include (1) protocol choice (Lindell17, GG18/20, CGGMP20), (2) key lifecycle management, (3) runtime controls, and (4) forensics/observability. Framing the problem as "secure the combined protocol–implementation–operations system" avoids tunnel vision on protocol design alone
  [Source: Canetti et al., 2020 / ePrint 2021/060; Stackup 2025, "Security Benefits and Trade-offs"].

- **Scope reframing – internal vs. external threat models**:  
  Instead of only "honest majority" or "single compromised endpoint" assumptions, treat "single malicious signing party with repeated access" as a **first-class adversary**, including insider threats at providers or compromised user devices
  [Source: Makriyannis et al., 2023, ePrint 2023/1234, Threat Model].

- **Risk reframing – from "single bug" to "class of mis-implementations"**:  
  The vulnerability is better framed as a class of mis-implementations where **prerequisite checks for security reductions are not enforced** (abort behavior, Paillier key proof-of-structure, parameter validation), which generalizes to future MPC protocols as well
  [Source: Makriyannis et al., 2023; Canetti et al., 2020].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **Protocols**: Lindell17 (2PC ECDSA) and GG18/20 (multi-party ECDSA) provide the mathematical backbone for MPC wallets
  [Source: Lindell, 2017, "Fast Secure Two-Party ECDSA Signing"; Gennaro & Goldfeder, 2018, "Fast Multi-Party Threshold ECDSA"].
- **Cryptographic components**: Paillier encryption for homomorphic computations, zero-knowledge proofs of correct key generation, range proofs, and commitment schemes
  [Source: Canetti et al., 2020 / ePrint 2021/060, Protocol Overview].
- **Implementation behaviors**: Error handling (abort vs. continue), parameter validation, logging, retries, latency timeouts.
- **Operational controls**: Rate limiting for signing, anomaly detection, key refresh policy, incident response playbooks.

### 2.2 Balance and "degree" issues

- **Performance vs. validation depth**: Deeper Paillier and auxiliary key proofs (as in CGGMP20) add CPU and latency overhead, especially for large key sizes and multi-party ceremonies
  [Source: Canetti et al., 2020, Performance Discussion].
- **Availability vs. strict aborts**: Aborting on any invalid signature or ZK proof failure improves security but may increase user-visible failures in noisy networks or partially buggy clients
  [Estimate based on: MPC operational practices in Stackup 2025, "Performance Benchmarks and Limitations"].
- **Simplicity vs. defense in depth**: Minimalistic implementations reduce code surface but can omit layered checks (input validation, secondary checksums, telemetry), weakening detection and forensics capabilities.

### 2.3 Causal chains

1. **GG18/20-style chain**:  
   Weak or missing public-key validation for Paillier modulus N ⇒ attacker crafts malicious modulus with small prime factors ⇒ repeated signing ceremonies leak information about victim share modulo these small primes ⇒ Chinese Remainder reconstruction of full key after ~16 ceremonies
   [Source: Makriyannis et al., 2023, ePrint 2023/1234, GG18/20 Attacks].

2. **Lindell17-style chain**:  
   Implementation continues after invalid signatures instead of aborting ⇒ attacker repeatedly induces protocol instances with specially chosen messages ⇒ leakage over up to 256 signatures enables full private-key recovery
   [Source: Makriyannis et al., 2023, ePrint 2023/1234, Lindell17 Attacks].

3. **System-level chain**:  
   High signing throughput with minimal anomaly detection + permissive retry policies + long-lived keys with infrequent rotation ⇒ attacker can accumulate required malicious signing sessions within realistic time windows without triggering alarms
   [Source: Stackup 2025, Sections on "Performance" and "Security Incidents and Lessons Learned"].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and conflicts

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | MPC protocol designers, open-source library maintainers | Strong theoretical security, wide adoption, minimal misuse | Limited control over downstream implementations, performance constraints | Tension when implementers deviate from reference security assumptions |
| Downstream | Wallet providers, custodians, exchanges integrating MPC | High security, low latency, seamless UX, regulatory compliance | Uptime SLAs, migration risk, budget limits, legacy code | May deprioritize "invisible" security hardening vs. features and UX |
| Sideline / External | End users, regulators, incident responders, chain analytics | Asset protection, clear accountability, recoverability, transparent risk posture | Limited visibility into internal architectures; regulatory timelines; legal constraints | Regulators may demand rapid remediation or disclosure; users resist disruptive changes |

[Source: Stackup 2025, "Popular MPC Wallet Providers"; TRM Labs 2025 Crypto Crime Report; Problem statement – Stakeholders].

### 3.2 Environmental factors

- **Macro threat environment**: North Korean and other state-linked actors continue to focus on infrastructure-level compromises, with North Korea alone responsible for nearly USD 800M (≈35%) of stolen cryptocurrency in 2024, primarily via key and seed theft
  [Source: 2025 Crypto Crime Report, TRM Labs, 2025, "North Korea stole nearly USD 800 million"].
- **Regulatory pressure**: Custodial and quasi-custodial providers face increasing scrutiny under financial services and custody regulations, requiring demonstrable control over keys, segregation of duties, and robust incident response
  [Source: Various global custody guidance summarized in Stackup 2025, "Regulatory Landscape and Compliance"].
- **Competitive landscape**: Smart contract–based account abstraction and hardware-backed solutions (HSMs, hardware wallets) compete with MPC wallets, making security posture a differentiator
  [Source: Stackup 2025, Sections "MPC vs Other Wallet Types" and "Hybrid Approaches"].

### 3.3 Responsibility and room for maneuver

- **Protocol designers**: Provide clear, explicit lists of **required** vs. **optional** security checks (and reference implementations) to minimize mis-implementation risk.
- **Wallet providers**: Own the responsibility for:
  - Hardening existing deployments (patching libraries, enabling CGGMP20-style proofs, enforcing aborts).
  - Operating monitoring and incident response lines.
  - Communicating risk and mitigation timelines to regulators and key institutional clients.
- **Users and institutions**: Can pressure providers for independent audit reports and transparent remediation milestones; can diversify custody across providers to reduce concentration risk.

[Source: Fireblocks Disclosure Blog 2023; Stackup 2025; TRM Labs 2025].

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2017** – Lindell17 introduces an efficient 2-party ECDSA signing protocol enabling practical consumer MPC wallets
   [Source: Lindell, 2017, "Fast Secure Two-Party ECDSA Signing", ePrint 2017/552].
2. **2018–2020** – GG18/GG20 provide scalable threshold ECDSA for n-of-n and k-of-n signing, adopted by institutional MPC providers
   [Source: Gennaro & Goldfeder, 2018, "Fast Multi-Party Threshold ECDSA"; related GG20 work].
3. **2018–2023** – Wallet providers deploy these protocols at scale, often reusing open-source or internal implementations without fully formalizing all validation and abort conditions.
4. **2020** – CGGMP20 (Canetti et al.) publishes a strengthened threshold ECDSA protocol with proactive refresh and identifiable aborts, but many legacy deployments remain on GG18/20 or partial upgrades
   [Source: Canetti et al., 2020 CCS / ePrint 2021/060].
5. **2023** – Fireblocks and co-authors publish practical key-extraction attacks and coordinate disclosure with affected providers, prompting first wave of patches
   [Source: Makriyannis et al., 2023, ePrint 2023/1234; Fireblocks Blog 2023].

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - Rapid growth of crypto markets and MPC adoption outpaced formal security engineering and standardization processes.
  - Lack of widely accepted implementation guidelines and certification schemes for threshold ECDSA implementations.

- **Direct technical causes**:
  - Failure to implement required Paillier modulus structure proofs and range proofs in GG18/20 variants
    [Source: Makriyannis et al., 2023, GG18/20 Attacks].
  - Failure to abort on invalid signatures or protocol deviations in Lindell17 implementations, allowing attackers to repeatedly probe the system
    [Source: Makriyannis et al., 2023, Lindell17 Attacks].

### 4.3 Root issues

- **Misalignment between academic proofs and engineering practices**: Protocol papers clearly state assumptions, but these are not consistently translated into "non-negotiable" implementation requirements.
- **Inadequate threat modeling**: Many deployments optimized against key loss and endpoint compromise but underestimated **malicious co-signer** and **insider** threat models.
- **Insufficient observability**: Telemetry around signing patterns, error rates, and counterparty behavior often lacks the granularity needed to detect slow key-extraction attacks.

[Source: Makriyannis et al., 2023; Canetti et al., 2020; Stackup 2025].

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- As MPC wallets continue to grow in institutional and retail adoption, the attack surface represented by legacy Lindell17 and GG18/20 implementations persists.
- Given that infrastructure attacks already account for nearly 70% of stolen crypto value and are trending upward, persistent key-extraction vectors in widely used custody infrastructure will likely be targeted more aggressively
  [Source: TRM Labs, 2025 Crypto Crime Report, "USD 2.2 billion was stolen in crypto-related hacks"].
- If no systematic remediation and certification emerge, exploitation may remain under-reported due to difficult attribution and rapid laundering, while successful attacks could result in outsized, sudden losses.

### 5.2 Early signals

- Public academic work demonstrating highly practical, low-interaction key-extraction attacks on concrete implementations
  [Source: Makriyannis et al., 2023, ePrint 2023/1234].
- First wave of responsible disclosures and patches by providers such as ZenGo, Coinbase, Safeheron, indicating both awareness and non-trivial remediation complexity
  [Source: Fireblocks Blog, 2023, Vulnerability Disclosure and Remediation Guidance].
- Growing focus of regulators and chain analytics firms (e.g., TRM Labs) on private-key compromise as a main driver of losses, creating pressure for more robust wallet architectures
  [Source: TRM Labs 2025 Crypto Crime Report].

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**:  
  All major providers migrate to CGGMP20-like protocols with full key validation, identifiable aborts, proactive refresh, and strong monitoring. Industry develops a light-weight certification scheme for threshold ECDSA libraries. Key-extraction incidents from MPC wallets become negligible.

- **Baseline scenario**:  
  Top-tier providers remediate; smaller or slower-moving providers continue using partially vulnerable implementations. Attacks remain rare but possible, causing occasional high-profile losses and reputational damage.

- **Pessimistic scenario**:  
  Adversaries weaponize key-extraction techniques against one or more large custodians or WaaS offerings, extracting keys across multiple accounts and leading to catastrophic losses (hundreds of millions) before detection. Regulatory backlash accelerates a shift away from MPC wallets toward hardware-backed and smart contract–based solutions.

[Scenarios estimated based on: current disclosure status, typical remediation timelines in financial infrastructure, and threat actor behavior patterns described in TRM Labs 2025 Crypto Crime Report, Medium confidence].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Cryptography expertise**: Major MPC providers already employ specialized cryptography engineers capable of understanding and implementing CGGMP20-style proofs and advanced key validation
  [Source: Fireblocks, ZenGo, Coinbase technical hiring and research publications].
- **Operational maturity**: Established providers operate 24/7 monitoring, incident response, and change-management processes that can be leveraged for secure rollout of protocol updates.
- **Ecosystem collaboration**: Prior coordinated disclosure between Fireblocks and affected providers shows willingness to cooperate on security issues
  [Source: Fireblocks Disclosure Blog, 2023].

### 6.2 Capability gaps

- **Formal verification and secure coding practices**: Not all wallet codebases adopt formal verification, side-channel analysis, or structured code review frameworks suited to high-assurance cryptographic software.
- **Security productization**: Some providers lack productized, reusable libraries and validation modules, leading to one-off implementations that are harder to audit and patch.
- **Cross-functional risk communication**: Translating complex cryptographic risks into actionable business and regulatory language is still difficult, hampering rapid decision-making.

[Source: Stackup 2025, "Security Incidents and Lessons Learned"; Makriyannis et al., 2023].

### 6.3 Buildable capabilities (1–6 months)

- Develop or adopt a **shared reference library** for hardened threshold ECDSA with CGGMP20-style proofs and clearly specified security-relevant flags.
- Establish **internal red teams** focused on MPC attack simulation, including key-extraction attempts and protocol-deviation fuzzing.
- Enhance **observability and anomaly detection pipelines** dedicated to signing ceremonies (e.g., per-counterparty error rates, message distributions, protocol deviations).

[Estimate based on: typical engineering timelines for library refactors and monitoring stack enhancements, Medium confidence].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Threshold ECDSA protocols underpinning MPC wallets; rapid adoption by major providers; current loss landscape dominated by key compromises.
- **Problem**: Practical key-extraction attacks on mis-implemented Lindell17/GG18/20 allow a malicious participant to recover full private keys.
- **Analysis**: Internal and external factors, root causes, trends, capability reserves.
- **Options**: Protocol migration to CGGMP20-style schemes; hardening current implementations; runtime monitoring and kill switches; diversification to hardware and smart contracts.
- **Risks**: Migration failures, residual vulnerabilities, performance regressions, regulatory and reputational impacts.

### 7.2 Key judgments (for validation)

1. Key-extraction attacks are **practically feasible** against unpatched implementations and not merely theoretical.
2. A combination of protocol-level migration (e.g., CGGMP20) and implementation hardening can reduce exploitability to negligible levels without prohibitive performance cost.
3. Observability and anomaly detection are necessary complements; protocol correctness alone is insufficient in adversarial environments.

[Source: Makriyannis et al., 2023; Canetti et al., 2020; TRM Labs 2025; Stackup 2025].

### 7.3 Alternative high-level paths

- **Path A – Protocol upgrade first**: Prioritize migration to CGGMP20-style protocols with identifiable aborts and proactive refresh, then layer on monitoring.
- **Path B – Hardening + monitoring first**: Quickly add abort-on-failure, stricter validation, and anomaly detection to existing implementations, then plan longer-term protocol upgrades.
- **Path C – Hybrid diversification**: Gradually shift some assets or user segments to hardware-backed or smart contract wallets while hardening remaining MPC infrastructure.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- **Protocol-centric bias**: Overemphasis on protocol migration may underweight operational controls and incident response.
- **Provider-centric data**: Public information is richer for large providers; small or opaque custodians may have different constraints.
- **Publication bias**: Successful undetected key-extraction attacks may not appear in public reports; risk could be underestimated.

[Source: TRM Labs 2025, discussion on data limitations; Makriyannis et al., 2023].

### 8.2 Required intelligence

- Comprehensive **inventory of deployed MPC protocol versions**, parameter sets, and libraries for each provider.
- **Empirical measurement** of performance impact for full CGGMP20-style validation and abort logic under production traffic.
- **Threat intelligence** on attempted or suspected key-extraction campaigns (e.g., repeated small withdrawals, clustered anomalies across tenants).

### 8.3 Validation plan

- Run **red-team exercises** that reproduce Makriyannis et al. attacks against staging environments for each implementation and confirm inability to extract keys.
- Conduct **performance benchmarks** comparing current implementation vs. hardened CGGMP20-style implementation under realistic load.
- Implement a **pilot deployment** of enhanced monitoring and rate limiting for a subset of traffic, measuring false-positive rates and operational friction.

[Source: Makriyannis et al., 2023; Canetti et al., 2020; industry best practices for crypto custody testing].

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Quantitative risk estimates (probability of exploitation, expected loss) may change as more telemetry and incident data become available.
- Preferred migration strategy may shift if smart contract–based account abstraction or hardware-backed solutions achieve significantly better security–cost trade-offs.

### 9.2 Incremental approach

- Start with **defense-in-depth hardening** that is low risk and reversible (e.g., stricter validation, logging, monitoring, throttling).
- Follow with **protocol upgrades** for new key material and high-value accounts.
- Plan for **phased re-sharding or key refresh** with proactive testing and rollback mechanisms.

### 9.3 "Good enough" criteria

- All production MPC signing flows enforce **abort-on-failure** and strong parameter validation.
- Independent red-team attempts and academic-style attack reproductions **fail to extract keys** within realistic interaction budgets.
- Monitoring shows **no unexplained patterns** consistent with key-extraction attempts, and incident response is well-rehearsed.

[Estimate based on: security engineering maturity models and crypto custody practices, Medium confidence].

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. Practical key-extraction attacks exploit **implementation gaps** rather than fundamental protocol flaws; enforcing assumptions (abort behavior, key validation) restores the intended security guarantees
   [Source: Makriyannis et al., 2023; Canetti et al., 2020].
2. Given that infrastructure attacks already dominate loss categories, leaving MPC key-extraction vectors open represents an unacceptable systemic risk
   [Source: TRM Labs 2025 Crypto Crime Report].
3. A combined program of **protocol migration, implementation hardening, monitoring, and independent audits** can materially reduce risk within a 6–12 month window.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

- **【P0 – Critical】**
  1. Complete inventory and security review of all Lindell17 and GG18/20 implementations → Crypto Engineering Lead → Coverage: 0% → 100% of MPC signing flows reviewed → 2025-01-31.
  2. Implement mandatory abort-on-failure and strict parameter validation in all MPC signing code paths → Protocol Engineering Team → Vulnerable flows: >0 → 0 known vulnerable flows → 2025-02-28.

- **【P1 – Important】**
  3. Design and deploy anomaly detection for suspicious signing patterns (e.g., repeated failures, abnormal distributions) → Security Engineering → Detection coverage: pilot only → full production → 2025-03-31.
  4. Plan CGGMP20-style migration for new keys and high-value accounts, including performance benchmarks and rollout strategy → Architecture Team → Migration plan: draft → approved and scheduled → 2025-03-31.

- **【P2 – Optional】**
  5. Explore diversification to hardware-backed and smart contract–based custody for specific client segments → Product & Strategy → Share of assets diversified: baseline → +10% → 2025-06-30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Implementation regressions break signing for some users | High | Medium | Elevated error rates or failed signing ceremonies post-deployment | Staged rollouts, canary deployments, robust rollback procedures | Engineering Lead |
| Residual unknown vulnerabilities in legacy or niche implementations | High | Medium | Discovery of unreviewed code paths or third-party integrations | Comprehensive code inventory, require security sign-off for all MPC-related components | Security Lead |
| Performance degradation from heavier proofs and validation | Medium | Medium | Increased signing latency or timeouts in production | Optimize implementations, invest in hardware, tune parameters; prioritize critical flows | SRE Lead |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| A: Full CGGMP20 migration | Strongest theoretical guarantees; identifiable aborts; proactive refresh | High engineering effort; performance overhead; migration complexity | Implementation bugs during migration; longer timelines | Large providers with strong cryptography teams and long-term MPC roadmap | When team lacks cryptography capacity or timelines are extremely tight |
| B: Harden existing implementations + monitoring | Faster risk reduction; lower upfront cost; less disruptive | May leave some structural issues unresolved; reliance on monitoring | Missed edge cases; monitoring blind spots | Need rapid risk reduction under time/budget constraints | When long-term strategy is to rely solely on MPC for all risk tiers |
| C: Diversify to hardware/smart contract custody | Reduces concentration of risk in MPC stack; leverages mature ecosystems | Requires additional integrations and user education; operational overhead | New attack surfaces and operational complexities | Institutions open to multi-modal custody strategies | When regulatory or internal policy mandates single-architecture custody |

[Source: Makriyannis et al., 2023; Canetti et al., 2020; Stackup 2025; TRM Labs 2025].

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **MPC wallet** | Cryptocurrency wallet where private key material is split into multiple shares and distributed across parties/devices; signing is performed via secure multi-party computation without reconstructing the key | N/A | [Source: "MPC Wallets: A Complete Technical Guide", Stackup, 2025, "What Is an MPC Wallet?"] |
| **Threshold ECDSA** | Digital signature scheme where k-of-n parties jointly generate ECDSA signatures without any single party holding the full private key | N/A | [Source: Gennaro & Goldfeder, 2018, "Fast Multi-Party Threshold ECDSA"] |
| **Lindell17** | Two-party ECDSA signing protocol widely used in consumer MPC wallets | N/A | [Source: Lindell, 2017, "Fast Secure Two-Party ECDSA Signing", ePrint 2017/552] |
| **GG18/GG20** | Multi-party threshold ECDSA protocols enabling n-of-n and k-of-n signatures used in institutional MPC wallets | N/A | [Source: Gennaro & Goldfeder, 2018, GG18/20 protocol family] |
| **CGGMP20** | UC-secure, proactive threshold ECDSA protocol with identifiable aborts and improved key validation designed for wallet settings | N/A | [Source: Canetti et al., 2020 CCS / ePrint 2021/060] |
| **Paillier encryption** | Additively homomorphic public-key encryption scheme used in threshold ECDSA protocols to support secure computations on encrypted values | N/A | [Source: Standard descriptions summarized in Makriyannis et al., 2023] |
| **Key-extraction attack** | Attack in which an adversary interacts in multiple signing sessions to gradually recover the full private key from partial leakages | N/A | [Source: Makriyannis et al., 2023, "Practical Key-Extraction Attacks in Leading MPC Wallets"] |
| **Identifiable abort** | Property of a protocol where, if execution fails, honest parties can identify which participant caused the abort | N/A | [Source: Canetti et al., 2020 CCS / ePrint 2021/060] |
| **Infrastructure attack** | Attack that targets underlying keys, seeds, or infrastructure services rather than application-layer logic | N/A | [Source: TRM Labs, 2025 Crypto Crime Report, "USD 2.2 billion was stolen in crypto-related hacks"] |
| **Account abstraction / smart contract wallet** | Wallet architecture where control logic is implemented in a smart contract, enabling programmable access control and recovery without relying solely on MPC | N/A | [Source: Stackup 2025, sections on hybrid approaches] |

---

## 12. References

### Tier 1 – Primary Research and Protocol Specifications

1. **Makriyannis, N., Yomtov, O., & Galansky, A.** (2023, revised 2025). *Practical Key-Extraction Attacks in Leading MPC Wallets*. Cryptology ePrint Archive, Paper 2023/1234. https://eprint.iacr.org/2023/1234  
   **[Cited in**: Context Recap; Sections 1–4, 5.2, 6, 7, 8, 10, 11 **]**
2. **Canetti, R., Gennaro, R., Goldfeder, S., Makriyannis, N., & Peled, U.** (2020). *UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts*. In CCS 2020; Cryptology ePrint Archive, Paper 2021/060. https://eprint.iacr.org/2021/060  
   **[Cited in**: Context Recap; Sections 1–4, 5, 6–8, 10, 11 **]**
3. **Lindell, Y.** (2017). *Fast Secure Two-Party ECDSA Signing*. Cryptology ePrint Archive, Paper 2017/552. https://eprint.iacr.org/2017/552  
   **[Cited in**: Sections 2, 4, 11 **]**
4. **Gennaro, R., & Goldfeder, S.** (2018). *Fast Multi-Party Threshold ECDSA with Fast Trustless Setup*. (GG18/GG20 family). Cryptology ePrint Archive and CCS proceedings.  
   **[Cited in**: Sections 2, 4, 11 **]**

### Tier 2 – Industry Reports and Technical Guides

5. **TRM Labs.** (2025). *2025 Crypto Crime Report*. TRM Labs.  
   Key section: "USD 2.2 billion was stolen in crypto-related hacks" and discussion of infrastructure attacks and North Korea.  
   **[Cited in**: Context Recap; Sections 3, 4, 5, 6, 7, 10, 11 **]**
6. **TRM Labs.** (2025). *Category deep-dive: $2.2 billion was stolen in crypto-related hacks in 2024*. TRM Blog.  
   **[Cited in**: Sections 3, 5 **]**
7. **Stackup.** (2025). *MPC Wallets: A Complete Technical Guide*. Stackup. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide  
   **[Cited in**: Context Recap; Sections 2, 3, 4, 5, 6, 7, 10, 11 **]**
8. **Fireblocks.** (2023). *Vulnerability disclosure and remediation guidance for MPC wallet providers*. Fireblocks Blog.  
   **[Cited in**: Context Recap; Sections 3, 4, 5, 6, 7, 10 **]**
9. **ZAN.** (2023). *Attacks and Remediation for MPC Wallets*. Medium Blog.  
   (Used as a secondary synthesis of Fireblocks research and industry remediation practices.)  
   **[Cited in**: Background reasoning only; not used for unique numerical claims.**]

### Tier 3 / Internal & Estimates

10. **Problem Statement – Key-Extraction Attack Vulnerabilities in MPC Wallet Implementations.** (2025). Internal documentation summarizing impact scope, constraints, and stakeholders.  
    **[Cited in**: Context Recap; Sections 1, 3, 5, 6, 7, 10 **]**
11. **Coinbase, Inc.** (2023). *Q3 2023 Shareholder Letter and Institutional AUM Data*. Coinbase Investor Relations.  
    **[Cited in**: Context Recap; Sections 1, 3 **]**
12. **Estimates and assumptions.** Various.  
    Method: extrapolation from public user counts, AUM figures, and typical security program costs (audit + engineering). Confidence: Medium. Validation: to be refined via provider-specific data and audits.  
    **[Used in**: Context Recap; Sections 1, 5, 6, 9, 10 **]**
