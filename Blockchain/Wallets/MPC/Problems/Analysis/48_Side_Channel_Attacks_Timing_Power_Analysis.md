# Side-Channel Attacks on MPC Wallet Implementations – Timing and Power Analysis – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Security & Cryptography Team

---

## Pre-Section: Context Recap

- **Problem title**: Side-channel attacks on MPC wallet implementations: timing and power analysis vulnerabilities
- **Current state**:
  - MPC wallets based on threshold ECDSA/EdDSA/Schnorr secure >$50B in digital assets across custodians, WaaS platforms, and retail/mobile wallets, with 100M+ end users estimated globally  
    [Estimate: Extrapolated from Coinbase institutional AUM, major MPC provider market share, and user counts; Medium confidence, validate via provider disclosures].
  - Academic work and industry analysis show that timing, power, electromagnetic (EM), and cache-timing side-channels can leak key-dependent information from cryptographic implementations, including MPC protocols, even when the underlying math is secure  
    [Source: "Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems", Kocher, 1996; "Differential Power Analysis", Kocher et al., 1999; "Reading It like an Open Book: Single-trace Blind Side-channel Attacks on Garbled Circuit Frameworks", IACR ePrint 2024/1035].
  - Real-world incidents such as the Trezor hardware wallet side-channel vulnerability and lab attacks against smartcards demonstrate that physical side-channels are practical, not theoretical, given modest equipment and local access  
    [Source: Kraken Security Labs Trezor disclosure, 2020; Side-channel attack history surveys in academic cryptography, 2001–2020].
  - MPC wallets add distributed trust but often run on general-purpose hardware (mobile phones, cloud VMs, browser JavaScript) that was not designed for side-channel resistance, and many implementations are not fully constant-time  
    [Source: Stackup "MPC Wallets: A Complete Technical Guide", 2024–2025; Aqtive Guard timing-attack knowledge base, 2024].
- **Pain points**:
  - Vulnerabilities span **multiple layers** (MPC protocol implementation, cryptographic libraries, runtime/platform, hardware), making it difficult to reason about overall side-channel risk and prioritize mitigations.
  - Countermeasures such as constant-time code, masking, and hardware isolation add non-trivial performance and engineering cost (15–30% latency overhead for constant-time, 2–3× cost for masking)  
    [Source: Constant-time implementation benchmarks in BearSSL and libsodium documentation; NIST PQC candidate masking guidance, 2020–2023].
  - Providers lack standardized side-channel threat models, benchmarks, and certification schemes for MPC wallets, leading to inconsistent and sometimes purely marketing-driven security claims  
    [Source: Industry MPC wallet guides and provider marketing materials, 2023–2025; Aqtive Guard timing-attack KB, 2024].
- **Goals** (from problem statement):
  - Achieve ≥90% of major MPC wallet implementations deploying constant-time cryptographic operations by Q4 2026 (est. baseline <30%).
  - Increase attack cost so that ≥10,000 (min) / ≥100,000 (target) / ≥1,000,000 (ideal) signing operations are needed for successful timing/power/EM key extraction.
  - Keep side-channel countermeasure latency overhead ≤30% (max), ≤20% (target), ≤10% (ideal) relative to unprotected implementations.
  - Deploy hardware-isolated execution (secure enclaves / TEEs) for ≥50% (min) / ≥70% (target) / ≥90% (ideal) of mobile and hardware wallet MPC implementations by Q4 2027.
  - Formally verify ≥50% (min) / ≥70% (target) / ≥90% (ideal) of cryptographic MPC libraries as constant-time by Q4 2027.
  - Ensure zero confirmed side-channel key-extraction incidents with fund loss among major MPC providers from Q4 2025–Q4 2027.
  - Train ≥500 (min) / ≥1,000 (target) MPC wallet developers in side-channel-resistant implementation.
- **Hard constraints** (from problem statement):
  - **Timeline**: Q1 2026–Q4 2027 (~24 months) for countermeasure deployment, verification, audits, training.
  - **Budget**: Roughly $500K–$2M per major provider to harden MPC stacks against side-channels (engineering, audits, lab testing, hardware, tools).
  - **Talent**: Estimated <500 engineers globally with strong side-channel + cryptography + systems expertise; <200 formal verification specialists  
    [Estimate: Based on conference participation, publication records, and specialized hiring data, Medium confidence].
  - **Platform constraints**: Mobile devices and browsers offer limited or fragmented hardware security features; cloud TEEs (e.g., AWS Nitro Enclaves) incur cost and operational complexity  
    [Source: AWS Nitro Enclaves documentation and MPC blog; Android/iOS security guides; cloud confidential computing docs].
- **Key facts** (from problem statement & literature):
  - Timing attacks typically need 1,000–10,000 signing operations on vulnerable implementations; unprotected ECDSA DPA can succeed with 100–1,000 traces under good lab conditions  
    [Source: IACR ePrint 2023/001 "Time Is Money, Friend! Timing Side-channel Attack against Garbled Circuit"; DPA tutorials on ECDSA; Aqtive Guard timing-attack KB].
  - Constant-time implementations add ~15–30% latency; masking-based countermeasures often incur 2–3× computational overhead  
    [Source: BearSSL constant-time verification case study; NIST PQC candidate evaluations for masked implementations].
  - TEEs and secure enclaves reduce certain side-channels but do not eliminate all leakage (e.g., network timing, microarchitectural attacks); they also introduce supply-chain and trust assumptions  
    [Source: AWS Nitro Enclaves MPC wallet blog, 2023; hardware security literature on TEEs and side-channels].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

1. **Core problem**  
   MPC wallet implementations that are mathematically secure at the protocol level (threshold ECDSA/EdDSA/Schnorr) leak key-dependent information through timing, power, EM, and cache-timing side-channels in real deployments (mobile, hardware wallets, cloud VMs, browser wallets). Attackers with local or co-located access can exploit these leakages to recover key shares or entire private keys, despite correct protocol design  
   [Source: IACR ePrint 2024/1035 on garbled-circuit side-channels; IACR ePrint 2023/001 on timing attacks; Kraken Labs Trezor attack report, 2020].

2. **Contradictions**
   - **Security vs. performance**: Constant-time and masked implementations significantly reduce leakage but introduce 15–30% latency overhead for constant-time and 2–3× cost for masking; providers running high-volume signing workloads are reluctant to absorb this cost without clear benchmarks and user-acceptance data  
     [Source: BearSSL constant-time analysis; NIST PQC Raccoon masking spec; Stackup MPC performance discussions, 2024].
   - **Mathematical guarantees vs. physical reality**: Protocol proofs assume black-box computations with no side-channels; real hardware and runtimes (CPUs, caches, schedulers, JIT compilers) violate these assumptions, creating a gap between "provably secure" and "actually secure"  
     [Source: MPC security model literature; side-channel history papers; IACR garbled-circuit timing attacks].
   - **Ease of deployment vs. hardware security**: Running MPC nodes in generic cloud VMs or standard mobile apps is easy and cheap; deploying secure enclaves, EM shielding, and side-channel labs is complex and expensive  
     [Source: AWS Nitro Enclaves MPC wallet blog; mobile secure enclave documentation].

3. **Who is in conflict?**
   - **Security and cryptography engineers** pushing for constant-time, masking, TEEs, and formal verification.
   - **Product and operations teams** prioritizing UX (fast signing), uptime, device compatibility, and cost.
   - **Regulators and institutional clients** demanding demonstrable resistance to sophisticated attacks, but lacking deep technical tools to evaluate claims.

### 1.2 Goals & conditions

- **Security goal**: Make practical timing/power/EM/cache side-channel key-extraction from MPC wallet implementations economically and operationally infeasible under realistic attacker models.
- **Implementation goal**: Ensure ≥90% of major MPC implementations use constant-time cryptographic primitives and side-channel-hardened protocol code paths by Q4 2026.
- **Performance goal**: Keep signing latency overhead from countermeasures ≤30% (max), ideally ≤10–20%, relative to current unprotected baselines, while maintaining acceptable UX for mobile and web wallets.
- **Deployment goal**: Achieve hardware-isolated (TEE/secure enclave) MPC execution for ≥70% of mobile and hardware wallet flows by Q4 2027, with clearly documented threat models and residual risks.
- **Verification goal**: Formally verify constant-time properties and side-channel resistance for ≥70% of core cryptographic libraries using tools like `ct-verif` and `dudect` by Q4 2027  
  [Source: Verification tool documentation and case studies such as BearSSL constant-time proofs].

### 1.3 Extensibility & reframing

- **Attribute reframing – from "side-channel" to "signal leakage budget"**:  
  Instead of treating timing/power/EM as binary (secure vs insecure), treat each implementation as having a **signal leakage budget**: acceptable leakage under defined attack models (remote vs. local, lab vs. field). This enables graded, risk-based decisions (e.g., higher budget allowed for low-value retail vs. institutional custody).
- **Scope reframing – from "crypto code problem" to "system-level observability problem"**:  
  Side-channel risk is not only about inner loops; it also involves scheduling, network protocols, retries, logging, and hardware configuration. Framing the problem as **"secure the full path from device/hardware to protocol"** expands solution space beyond just rewriting cryptographic kernels.
- **Threat-model reframing – from "no physical attacker" to "realistic physical + co-location"**:  
  Many deployments implicitly assume no physical access or co-location. Reframing to include **local attackers (mobile theft, evil maid, lab extraction) and co-located cloud tenants** as first-class adversaries aligns with known attacks and high-value custody scenarios  
  [Source: Side-channel attack history; AWS Nitro Enclaves threat model; IACR timing attacks].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **Cryptographic primitives and libraries**: Scalar multiplication, modular inversion, hash functions, PRNGs, implemented in C/Rust/Go/JavaScript with varying levels of constant-timeness  
  [Source: libsodium and OpenSSL constant-time discussions; BearSSL case study].
- **MPC protocol implementations**: Lindell17, GG18/20, CGGMP-style protocols for threshold ECDSA/EdDSA that orchestrate multiple rounds of network and local computation, each potentially leaking signals  
  [Source: Lindell 2017; Gennaro & Goldfeder 2018; CGGMP20].
- **Platforms**: 
  - Mobile devices (iOS/Android) with secure enclaves/TEEs of varying availability and APIs.
  - Hardware wallets with secure elements and physical countermeasures.
  - Cloud VMs and TEEs (AWS Nitro, GCP Confidential VMs) with microarchitectural side-channel considerations.
  - Browser-based wallets (JavaScript/WebAssembly) with highly timing-leaky runtimes.
- **Operational controls**: Rate limits, throttling of signing requests, device posture checks, logging and alerting for anomalous patterns.
- **Testing and verification**: Side-channel labs, DPA/timing analysis tools, formal verification, open-source tools like `dudect`.

### 2.2 Balance & "degree" issues

- **Constant-timeness vs. throughput**: Aggressively eliminating all data-dependent branches and memory access can degrade throughput and increase CPU cost; over-optimizing for performance risks reintroducing leaks  
  [Source: BearSSL constant-time evaluation; performance vs. leakage trade-off discussions in crypto engineering forums].
- **Masking depth vs. complexity**: High-order masking (to resist higher-order DPA) dramatically increases code and state complexity; insufficient testing can introduce functional bugs or security regressions  
  [Source: NIST PQC masking guidelines; masked lattice-scheme implementations].
- **TEE reliance vs. portability**: Deep reliance on TEEs improves isolation on platforms that support them but can fragment codebases and leave less-protected fallback paths on unsupported devices, creating uneven risk.

### 2.3 Causal chains

1. **Timing chain**:  
   Secret-dependent branches or table lookups in scalar multiplication → microsecond to millisecond timing variations per signing operation → attacker collects 1,000–10,000 timing measurements over network or local interface → statistical correlation recovers bits of private scalar → full key reconstructed with sufficient samples  
   [Source: "Time Is Money, Friend!" IACR ePrint 2023/001; classic Kocher timing attacks].

2. **Power/EM chain**:  
   Unmasked scalar arithmetic on mobile/hardware devices → distinguishable power/EM patterns for operations (add vs. double) → attacker with oscilloscope/ChipWhisperer collects 100–1,000 traces → correlation or template attacks recover key bits  
   [Source: Differential Power Analysis, Kocher et al., 1999; DPA methodology tutorials; Trezor/Kraken Labs side-channel disclosure].

3. **System-level chain**:  
   High-volume signing + weak side-channel hardening + lack of anomaly detection (no caps on signing requests per device/tenant) → attacker can gather required number of traces within realistic time without being throttled → key extraction and undetectable fund drain (no protocol violation on-chain)  
   [Source: Problem statement – Goals and constraints; TRM Labs crypto crime reports summarizing infrastructure attacks].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and conflicts

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | Protocol designers, cryptographic library authors, hardware/TEE vendors | Strong security proofs; practical, reusable primitives; hardware that resists side-channels | Limited control over downstream integration; performance and cost constraints; hardware design lead times | Pressure to ship performant features vs. rigorous side-channel hardening; ambiguity in how strongly to recommend constant-time/masking |
| Downstream | MPC wallet providers, exchanges, custodians, WaaS platforms | Protect user assets; low latency; broad device support; regulatory compliance | Uptime SLAs; cost and talent constraints; legacy deployments; fragmented device landscape | Security engineers vs. product/ops on performance and rollout risk; differing appetite for TEEs and hardware changes |
| Sideline / External | End users, regulators, institutional clients, auditors, side-channel labs | Asset safety; understandable guarantees; independent verification; clear incident response | Limited observability into internal implementations; complexity of side-channel topic; budget and time to run deep audits | Regulators and large clients may demand strong guarantees that are costly or slow to implement; users resist UX degradation (slow signing, limited device support) |

[Source: Problem statement – Stakeholders and roles; Stackup MPC wallet market overview; TRM Labs custody risk analysis].

### 3.2 Environment

- **Threat actors**: State-linked APTs and well-funded criminal groups target key and infrastructure-level weaknesses for large payoffs; side-channel labs can be acquired or rented by such actors  
  [Source: TRM Labs crypto crime reports; public attributions of North Korean groups targeting crypto infrastructure].
- **Regulatory climate**: Financial regulators increasingly treat custody risk (including key compromise) as a licensing and supervision issue; side-channel resistance is beginning to appear in security expectations for hardware wallets and HSMs and will likely extend to MPC  
  [Source: Hardware wallet certification schemes like Common Criteria EAL5+; regulatory guidance on custody controls].
- **Technology trends**: Wider availability of TEEs (e.g., Nitro Enclaves, ARM TrustZone, mobile secure enclaves), but also growing awareness of microarchitectural side-channels (Spectre/Meltdown, cache attacks) that complicate the security story  
  [Source: TEE vendor documentation; academic literature on speculative-execution attacks].

### 3.3 Responsibility & room for maneuver

- **Protocol and library authors** should:
  - Explicitly document side-channel assumptions and required implementation practices (constant-time, masking, fault handling) instead of treating them as optional.
  - Provide reference constant-time, side-channel-hardened implementations and test vectors  
    [Source: CGGMP20-style protocols and BearSSL documentation patterns].
- **MPC wallet providers** should:
  - Take ownership of end-to-end side-channel threat modeling, including realistic attacker capabilities and devices/platforms.
  - Prioritize hardening work in engineering roadmaps and budget for external lab testing and audits.
- **Regulators and large institutional clients** can:
  - Push for independent side-channel audits and transparent disclosure of mitigation coverage.
  - Incentivize adoption of certified hardware and standards via licensing and procurement criteria.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **1990s–2000s – Foundational side-channel research**:  
   Timing attacks (1996), DPA (1999), EM analysis (early 2000s) show that practical cryptosystems on smartcards and servers can leak secrets via physical signals  
   [Source: Kocher 1996; Kocher et al. 1999; EM side-channel literature].
2. **2010s – MPC protocols mature**:  
   Efficient threshold ECDSA protocols (Lindell17, GG18/20, CGGMP20) enable practical MPC wallets, but side-channel considerations are often out-of-scope in theoretical work  
   [Source: Lindell 2017; Gennaro & Goldfeder 2018; Canetti et al. 2020].
3. **2020 – Hardware wallet wake-up call**:  
   Trezor and other hardware wallets are shown vulnerable to timing/power-based key extraction with physical access, highlighting that consumer-grade hardware must consider side-channels  
   [Source: Kraken Security Labs Trezor disclosure, 2020].
4. **2023–2024 – MPC-specific side-channel research**:  
   Garbled circuit frameworks and MPC implementations are shown to leak via timing and cache behavior; single-trace and low-trace-count attacks become plausible  
   [Source: IACR ePrint 2024/1035; IACR ePrint 2023/001].
5. **2023–2025 – Cloud and mobile MPC adoption**:  
   Providers promote MPC wallets running on mobile devices, browsers, and cloud VMs; side-channel security is often summarized in marketing terms without detailed threat models or guarantees  
   [Source: Stackup MPC guide; provider documentation and blogs, 2023–2025].

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - Security proofs traditionally focus on mathematical correctness and protocol-level adversaries, not physical attackers with local access or co-location.
  - Industry incentives reward shipping features and visible UX improvements more than "invisible" side-channel hardening.
  - Lack of standardized **side-channel certification** for MPC wallets (unlike some smartcard and HSM products) leaves providers without clear external benchmarks.

- **Direct technical causes**:
  - Non-constant-time cryptographic primitives (e.g., table-lookup-based scalar mult, variable-time modular reduction).
  - Incomplete masking or poorly implemented randomization (e.g., using low-entropy masks or reusing randomness across operations).
  - Running MPC protocols on platforms without hardware protections or with noisy, shared microarchitectures (multi-tenant cloud, browser JIT engines) without compensating software-level mitigations.

### 4.3 Root issues

- **Misaligned threat models**: Many teams implicitly assume that physical/local attackers are out of scope, despite high-value institutional targets and widespread laptop/mobile theft.
- **Tooling and expertise gap**: Side-channel lab work and formal constant-time verification are niche skills with limited off-the-shelf tooling compared to functional testing.
- **Economic underpricing of rare but catastrophic risk**: Since side-channel incidents are hard to detect and rarely publicized, organizations may underestimate their expected-loss contribution relative to more visible threats  
  [Source: TRM Labs infrastructure attack analysis; general risk-management literature].

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- As MPC wallets expand to more chains and user segments, the **asset base at risk from side-channels** grows proportionally.
- Attackers continue to gain access to cheaper and more powerful measurement equipment (low-cost oscilloscopes, open-source tools like ChipWhisperer), lowering barriers to DPA/EM attacks  
  [Source: ChipWhisperer project documentation and pricing; academic lab setups].
- Without systematic adoption of constant-time and hardware isolation, realistic attackers can target the most vulnerable combinations: high-value keys + unprotected mobile/hardware devices or cloud VMs.
- Side-channel attacks will likely remain **under-detected**, because successful key extraction produces normal-looking on-chain behavior (authorized signatures), complicating attribution compared to smart contract exploits  
  [Source: TRM Labs crypto crime reports discussing infrastructure/key compromise].

### 5.2 Early signals

- Growing academic literature on side-channels in MPC frameworks, TEEs, and cryptographic libraries  
  [Source: IACR ePrint series; TEE side-channel papers].
- Security consultancies and specialized labs offering side-channel testing services for hardware wallets and HSMs starting to mention MPC and TEEs as target platforms.
- Provider blogs and marketing increasingly reference "constant-time" and "side-channel resistant" implementations, albeit with varying depth of explanation, signaling at least partial market demand.

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**:  
  Industry converges on best practices: constant-time primitives, masked implementations for high-value keys, TEEs for critical MPC nodes, standardized side-channel audits. MPC wallets achieve side-channel resistance comparable to certified HSMs for institutional deployments.

- **Baseline scenario**:  
  Major providers harden core flows and adopt TEEs where convenient, but long tail of smaller providers and legacy deployments remains partially exposed. Isolated incidents or near-misses occur but do not trigger systemic crisis; regulators gradually tighten expectations.

- **Pessimistic scenario**:  
  A sophisticated attacker combines timing/power analysis with protocol knowledge to extract keys from one or more large custodians or WaaS providers, leading to losses in the hundreds of millions and a wider crisis of confidence in MPC wallets. Regulatory backlash and insurance pressure force rapid, costly retrofits or migration toward hardware-backed and smart contract–based alternatives  
  [Estimate: Scenario based on TRM Labs analysis of concentration risk and historical infrastructure hacks; Medium confidence].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Strong cryptography talent at major providers**: Fireblocks, Coinbase, BitGo, ZenGo, and others already employ teams capable of understanding side-channel research and implementing constant-time primitives  
  [Source: Public research publications and hiring profiles of major providers].
- **Existing hardware security ecosystems**: Secure elements in hardware wallets, mobile secure enclaves, and TEEs in cloud platforms provide starting points for isolated execution, even if not yet fully leveraged for MPC  
  [Source: iOS Secure Enclave and Android TEE docs; AWS Nitro Enclaves blog for MPC wallets].
- **Open-source tooling**: Projects like `dudect` and side-channel testing frameworks allow some level of timing/power analysis without full custom lab setups  
  [Source: `dudect` documentation; side-channel testing toolkits].

### 6.2 Capability gaps

- **Systematic side-channel threat modeling**: Many providers lack a formal threat model that clearly states what types of side-channel attacks (local, co-located, lab-grade) they consider in-scope.
- **Integrated security engineering workflow**: Side-channel concerns are often treated as a one-off audit topic rather than being baked into CI/CD, code review, and release checklists.
- **Limited lab capacity**: Only a few vendors and academic labs offer deep DPA/EM testing; access is expensive and scheduling is constrained.

### 6.3 Buildable capabilities (1–6 months)

- Establish **internal side-channel champions** in cryptography teams to own threat modeling, code review guidelines, and coordination with external labs.
- Integrate **timing-leak tests** (e.g., using `dudect`) into CI for critical primitives, gating releases on stable distributions under synthetic workloads.
- Build or rent **basic side-channel lab capacity** (e.g., ChipWhisperer-based setups) for exploratory internal testing before formal external audits, reducing cost and de-risking surprises.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Long-standing practicality of side-channel attacks; emergence of MPC wallets on general-purpose hardware.
- **Problem**: Timing/power/EM/cache leakage in MPC implementations allows attackers with local or co-located access to extract key shares, despite secure protocols.
- **Analysis**: Internal elements (code, libraries, hardware, runtimes), external context (threat actors, regulators, technology trends), historical origins, trends, and capability reserves.
- **Options**: Software-only hardening (constant-time + masking), TEE-based isolation, hardware wallet/secure element integration, and tiered security policies by asset value.
- **Risks**: Performance degradation, residual leaks, implementation bugs, fragmented platform support, underestimation of sophisticated attackers.

### 7.2 Key judgments

1. **J1 – Practicality of attacks**: Side-channel key extraction is practically feasible against unprotected or partially protected implementations under realistic lab or local-attack conditions  
   [Source: Side-channel history; Trezor attack; IACR timing/power papers].
2. **J2 – Feasibility of mitigation**: A combination of constant-time code, masking for high-value flows, TEEs/secure elements, and rigorous rate limiting can reduce real-world risk to acceptable levels without catastrophic UX impact (≤20–30% latency overhead in most flows)  
   [Estimate: Based on benchmarks from constant-time libraries and TEE usage patterns; Medium confidence].
3. **J3 – Necessity of system-level controls**: Protocol- and code-level mitigations alone are insufficient; observability, throttling, and incident response are critical to catch attempted or partial attacks  
   [Source: TRM Labs on infrastructure attack detection; security engineering best practices].

### 7.3 Alternative paths

- **Path A – Software-hardening-first**: Prioritize constant-time primitives, masking, and CI timing tests across all platforms, then selectively adopt TEEs for high-value flows.
- **Path B – TEE-first for high value**: For institutional and high-value keys, prioritize TEE/secure-element-based execution, while maintaining minimal software hardening for retail/mobile flows.
- **Path C – Tiered architecture**: Combine A and B: TEE/secure-element isolation + strong software hardening for high-value tiers; primarily software hardening and monitoring for lower-value retail tiers.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases & blind spots

- **Crypto-engineering bias**: Overemphasis on constant-time and masking may underweight organizational and operational controls (e.g., rate limits, anomaly detection, user/device risk scoring).
- **Provider-centric data**: Public information skews toward large providers and high-profile hardware-wallet incidents; small providers may have different practices and risks.
- **Publication bias**: Successful side-channel attacks against MPC wallets may remain undisclosed or misattributed, leading to underestimation of real-world incident frequency.

### 8.2 Required intelligence

- Comprehensive **inventory of MPC implementations** by provider, including:
  - Language, libraries, constant-time status, and use of TEEs/secure enclaves.
  - Device/platform distribution for user base (e.g., % iOS vs. Android vs. browser).
- **Empirical performance data** for constant-time and masked implementations under production-like workloads across representative devices.
- **Side-channel test results** from internal and external labs, including worst-case trace counts required for key extraction under realistic noise levels.
- **Threat intelligence** on attempts or suspected side-channel campaigns (patterns of access, device clusters, unusual signing frequency).

### 8.3 Validation plan

- Run **timing and power analysis** against representative implementations in a controlled lab:
  - Select multiple device types (mobile, hardware wallet, cloud VM, TEE environment).
  - Measure impact of enabling/disabling constant-time code and masking on both leakage and performance.
- Design and execute **pilot deployments** of TEEs and hardware-backed MPC flows for a subset of high-value accounts, tracking latency, error rates, and operational overhead.
- Implement **monitoring dashboards** for signing request patterns (per-device, per-tenant, per-region) and validate that simulated attack traces trigger alerts without excessive false positives.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Quantitative estimates of **attack difficulty** (traces/operations required) will be refined as more empirical side-channel data becomes available for specific implementations and devices.
- Preferred **mitigation mix** (software vs. TEEs vs. secure elements) may shift as costs, platform support, and performance profiles evolve.
- Risk assessments for **browser-based MPC** may tighten if new attacks show practical high-resolution timing and cache side-channels in realistic environments.

### 9.2 Incremental approach

- Start with **low-regret hardening**: constant-time primitives, noise-resistant randomness, timing tests in CI, and basic rate limiting.
- Introduce **hardware-backed flows** (TEEs/secure elements) for high-value tiers and new deployments rather than forcing immediate migration of all existing users.
- Plan for **phased rollouts** with canary cohorts and rollback plans to manage performance regressions or unforeseen side effects.

### 9.3 "Good enough" criteria

- No known **high-leakage code paths** (variable-time operations, unmasked key-dependent branches) in critical MPC signing code for major providers.
- Independent side-channel tests and audits fail to extract keys under defined attacker models within economically feasible time and trace counts.
- Observability and monitoring are sufficient to detect suspicious signing patterns consistent with side-channel data collection.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. Side-channel attacks (timing, power, EM, cache) pose a **systemic but under-recognized risk** to MPC wallet implementations that rely on threshold cryptography but run on side-channel-prone hardware and runtimes.
2. Practical attacks have been demonstrated in related contexts (hardware wallets, garbled-circuit frameworks, TEEs), and there is no fundamental barrier preventing similar attacks on MPC wallets given sufficient access and equipment  
   [Source: Kocher 1996; Kocher et al. 1999; IACR ePrint 2024/1035; Trezor/Kraken 2020].
3. A layered mitigation strategy combining **constant-time primitives, masking for high-value flows, hardware isolation (TEEs/secure elements), and robust observability and throttling** can dramatically reduce real-world risk without unacceptable performance or cost, especially when applied in a tiered, risk-based manner.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

- **【P0 – Critical】**
  1. Define and publish an **MPC side-channel threat model** per provider (local, co-located, lab-grade attackers; in-scope platforms) → Crypto Engineering Lead → Coverage: 0% → 100% of MPC products have explicit threat model → 2026-03-31.
  2. Inventory and classify all cryptographic primitives and MPC code paths by **constant-timeness and masking status** → Security Engineering → Coverage: unknown → 100% of signing flows categorized → 2026-03-31.

- **【P1 – Important】**
  3. Integrate **timing-leak testing** (e.g., `dudect` or equivalent) into CI for core primitives → Crypto Tooling Team → CI coverage: 0% → ≥80% of cryptographic primitives tested per release → 2026-06-30.
  4. Launch a **pilot TEE/secure-enclave deployment** for high-value MPC flows (institutional custody or large balances) → Architecture Team → Accounts under TEE-backed MPC: 0% → ≥10% of high-value accounts → 2026-06-30.

- **【P2 – Optional】**
  5. Develop a **provider-neutral best-practices guide** for MPC side-channel resistance, including reference configs and checklists → Industry Working Group / Standards Body → Guide: draft → v1.0 published → 2026-12-31.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Performance regressions from constant-time/masking changes | Medium–High | Medium | Increased signing latency, timeouts, or mobile battery complaints post-deployment | Phased rollouts, performance benchmarks before release, device-specific optimizations | SRE Lead / Mobile Lead |
| Residual high-leakage paths in legacy or third-party components | High | Medium | Discovery of unreviewed libraries or platforms during inventory; audit findings | Comprehensive component inventory, deprecation or hardening of high-risk components, contractual security requirements for vendors | Security Lead |
| Over-reliance on TEEs / hardware without software-level hygiene | High | Medium | TEE or hardware-level vulnerability disclosure impacting multiple providers | Maintain baseline constant-timeness and masking even in TEE environments; defense-in-depth strategy; rapid patch/rotation procedures | Crypto Engineering Lead |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A: Software-hardening-first** | Broadly applicable across platforms; improves baseline security even without hardware changes; easier to roll out incrementally | Engineering effort to refactor and verify code; potential performance overhead | May not fully mitigate local/lab-grade attacks on vulnerable hardware | Diverse platform support; limited access to TEEs/secure elements | Assets are extremely high value and concentrated on a few platforms that already support strong TEEs |
| **B: TEE/secure-element-first for high-value flows** | Strong isolation for most critical keys; leverages existing hardware security certifications | Platform fragmentation; extra complexity in deployment and operations; residual microarchitectural risks | Overconfidence in hardware; fallback paths may be less secure | Institutional custody; limited device diversity; strong vendor relationships | Retail/mobile wallets with heterogeneous devices and OS versions |
| **C: Tiered architecture (combined approach)** | Matches security investment to risk; uses TEEs/secure elements for high-value flows and software hardening + monitoring for others | Requires careful policy design and configuration management; more complex architecture | Misconfiguration across tiers; uneven protections; operational overhead | Mixed user base (retail + institutional); need for flexible risk-based approach | Very small teams with limited engineering capacity for multi-tier architectures |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **Side-channel attack (SCA)** | Attack that exploits physical or microarchitectural information leakage (timing, power, EM, cache behavior) from cryptographic implementations rather than breaking the underlying math | N/A | [Source: Side-channel attack history surveys; Aqtive Guard timing-attack KB, 2024] |
| **Timing attack** | Side-channel attack that infers secret data from variations in computation time, often caused by secret-dependent branches or memory accesses | Time (μs–ms differences) | [Source: Kocher, "Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems", 1996] |
| **Differential Power Analysis (DPA)** | Statistical technique that correlates power-consumption traces from multiple cryptographic operations with hypothesized key bits to recover secrets | Number of traces (typically 100–10,000+) | [Source: Kocher et al., "Differential Power Analysis", 1999] |
| **Simple Power Analysis (SPA)** | Side-channel method that examines a single or small number of power traces to visually distinguish different operations and infer key bits | Single/few traces | [Source: DPA/SPA tutorials; hardware security literature] |
| **Electromagnetic (EM) analysis** | Side-channel attack that uses EM probes to capture radiated signals from devices performing cryptographic operations, similar to power analysis but contactless | Frequency bands, trace count | [Source: EM side-channel research papers, early 2000s onwards] |
| **Cache-timing attack** | Attack exploiting timing differences in cache hits/misses (e.g., Prime+Probe, Flush+Reload) to infer secret-dependent memory access patterns | N/A | [Source: Microarchitectural attack literature; Kocher et al.; IACR timing papers] |
| **Constant-time implementation** | Cryptographic implementation designed to perform operations in time independent of secret data (no secret-dependent branches or table indices, fixed memory access patterns) | Overhead: ~15–30% vs. naive | [Source: BearSSL constant-time verification; libsodium docs] |
| **Masking** | Countermeasure that splits sensitive intermediates into random shares to decorrelate side-channel signals from the underlying secrets, often increasing computational cost 2–3× | Overhead: 2–3× for high-order masking | [Source: NIST PQC masking schemes; lattice-based crypto implementations] |
| **Trusted Execution Environment (TEE)** | Hardware-supported isolated execution context (e.g., AWS Nitro Enclaves, ARM TrustZone, Intel SGX legacy) providing stronger protection against certain side-channels and memory attacks | N/A | [Source: AWS Nitro Enclaves documentation; platform security guides] |
| **Secure enclave / secure element** | Dedicated hardware module providing tamper-resistant storage and computation for keys with built-in side-channel protections | N/A | [Source: iOS Secure Enclave docs; hardware wallet secure element data sheets] |
| **MPC wallet** | Wallet architecture where private keys are split into multiple shares among parties/devices and signatures are generated using secure multi-party computation without recombining the key | N/A | [Source: Stackup "MPC Wallets: A Complete Technical Guide"] |
| **Threshold signature** | Digital signature scheme where a subset (k-of-n) of key-share holders can jointly produce a valid signature without any one party knowing the full private key | N/A | [Source: Lindell 2017; Gennaro & Goldfeder 2018] |

---

## 12. References

### Tier 1 – Primary Research and Technical Specifications

1. **Kocher, P.** (1996). *Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems*. Advances in Cryptology – CRYPTO'96.  
   **[Cited in**: Context Recap; Sections 2, 4, 5, 10, 11 **]**
2. **Kocher, P., Jaffe, J., & Jun, B.** (1999). *Differential Power Analysis*. Advances in Cryptology – CRYPTO'99.  
   **[Cited in**: Context Recap; Sections 2, 4, 5, 10, 11 **]**
3. **Anonymous / Multiple Authors.** (2024). *Reading It like an Open Book: Single-trace Blind Side-channel Attacks on Garbled Circuit Frameworks*. Cryptology ePrint Archive, Report 2024/1035. https://eprint.iacr.org/2024/1035  
   **[Cited in**: Context Recap; Sections 1, 2, 4, 5 **]**
4. **Anonymous / Multiple Authors.** (2023). *Time Is Money, Friend! Timing Side-channel Attack against Garbled Circuit*. Cryptology ePrint Archive, Report 2023/001. https://eprint.iacr.org/2023/001.pdf  
   **[Cited in**: Context Recap; Sections 2, 5, 10 **]**
5. **Canetti, R., Gennaro, R., Goldfeder, S., Makriyannis, N., & Peled, U.** (2020). *UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts (CGGMP20)*. CCS 2020; Cryptology ePrint Archive, Report 2021/060. https://eprint.iacr.org/2021/060  
   **[Cited in**: Sections 2, 4, 6, 7 **]**
6. **BearSSL Project.** (Year varies). *Constant-time Implementations and Side-channel Countermeasures in BearSSL*. Project documentation and case studies.  
   **[Cited in**: Context Recap; Sections 1, 2, 6, 7, 10, 11 **]**

### Tier 2 – Industry Reports, Guides, and Platform Documentation

7. **Stackup.** (2024–2025). *MPC Wallets: A Complete Technical Guide*. Stackup. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide  
   **[Cited in**: Context Recap; Sections 1, 2, 3, 4, 5, 6, 7, 11 **]**
8. **Aqtive Guard.** (2024). *Timing attacks and broader side-channel attacks*. Aqtive Guard Knowledge Base. https://docs.aqtiveguard.com/kb-articles/timing-attacks-and-broader-side-channel-attacks  
   **[Cited in**: Context Recap; Sections 1, 2, 3, 5, 11 **]**
9. **Amazon Web Services (AWS).** (2023). *Build secure multi-party computation (MPC) wallets using AWS Nitro Enclaves*. AWS Web3 Blog. https://aws.amazon.com/blogs/web3/build-secure-multi-party-computation-mpc-wallets-using-aws-nitro-enclaves  
   **[Cited in**: Context Recap; Sections 1, 3, 4, 6, 7 **]**
10. **NIST PQC Project.** (2020–2023). *Masking Strategies in Post-Quantum Cryptography Candidates (e.g., Raccoon specification)*. NIST PQC documentation.  
    **[Cited in**: Context Recap; Sections 1, 2, 6, 7, 11 **]**

### Tier 3 – Incidents, Tools, and Secondary Sources

11. **Kraken Security Labs.** (2020). *Trezor Hardware Wallet Side-channel Vulnerability Disclosure*. Kraken Security Blog.  
    **[Cited in**: Context Recap; Sections 1, 2, 4, 5, 10 **]**
12. **TRM Labs.** (2025). *2025 Crypto Crime Report – Infrastructure and Key Compromise Trends*. TRM Labs.  
    **[Cited in**: Context Recap; Sections 2, 3, 4, 5, 7, 10 **]**
13. **ChipWhisperer Project.** (Ongoing). *Open-source Side-channel Analysis Platform Documentation*. NewAE Technology Inc.  
    **[Cited in**: Sections 5, 6, 8 **]**
14. **`dudect` Project.** (Ongoing). *A Simple Tool to Detect Timing Leaks*. Open-source repository and documentation.  
    **[Cited in**: Sections 6, 7, 8, 10 **]**

15. **Problem Statement – Side-Channel Attacks on MPC Wallet Implementations: Timing and Power Analysis Vulnerabilities.** (2025). Internal documentation summarizing background, goals, constraints, stakeholders, and existing references.  
    **[Cited in**: Context Recap; Sections 1–8, 10 **]**
