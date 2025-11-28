# Nine-Aspects Analysis – Liner SDR MPC Problems (2025-11-28)

## Problem 1 – Private Key Theft and Key-Extraction Attacks in MPC Wallets

**Context recap**

- Practical key-extraction attacks show that compromising a single MPC party can, in some deployed designs, lead to full private key exfiltration.
- This undermines the core security promise of MPC wallets (no single point of failure) and puts large pools of assets at risk.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - MPC is intended to ensure that compromising one party is insufficient to steal assets, yet real-world systems still allow single-party compromise to leak the full key.
  - Increasing protocol and implementation complexity can simultaneously strengthen theoretical security and create new practical leak channels.
- **1.2 Goals and conditions**
  - Goal: make single-party compromise insufficient for key reconstruction under realistic attacker models.
  - Conditions: preserve sub-second UX for most transactions; keep infra and audit costs within realistic institutional budgets; avoid breaking compatibility with major chains.
- **1.3 Extensibility and common structure**
  - View “key theft” as a family of failures across protocol design, implementation, infra, and operations rather than only a cryptographic issue.
  - Reframe from “never allow exfiltration” to “eliminate single points of failure and sharply limit the blast radius and value of any local compromise”.

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Roles: MPC parties, coordinators, HSMs/TEEs, auditors, incident-response teams.
  - Artifacts: long-lived keys, secret shares, randomness, session state, logs, key-rotation mechanisms.
- **2.2 Balance and degree**
  - More checks, proofs, and monitoring → better assurance but higher complexity and performance cost.
  - More logging → better for forensics but dangerous if logs contain sensitive state or metadata that helps reconstruction.
- **2.3 Key internal causal chains**
  - `implementation_flaw / side_channel → share_state_leakage_over_time → attacker_reconstructs_key → full_asset_theft`.
  - `no_share_refresh + long_lived_keys → compromise_at_any_time_has_permanent_effect → persistent_systemic_risk`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - Users and institutions: risk of catastrophic loss and reputational damage.
  - Wallet providers: responsible for protocol choices, implementation quality, and response.
  - Auditors / regulators: require evidence that a single compromised party cannot trivially steal all assets.
- **3.2 Environment and institutions**
  - Regulatory expectations around custody, segregation of duties, and incident disclosure.
  - Threat landscape: sophisticated attackers, insiders, and nation-state actors.
- **3.3 Responsibility and room to maneuver**
  - MPC vendors must own secure protocol/implementation design and regular third-party reviews.
  - Customers can choose higher-assurance configurations (more parties, hardware isolation) or cheaper profiles with explicitly accepted risk.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Academic MPC focused on abstract models and correctness, less on side channels and system integration.
  - Early commercial MPC wallets optimized for functionality and time-to-market; security models were not always enforced end-to-end.
  - Recent work systematized attacks against deployed wallets, revealing practical key-extraction vectors.
- **4.2 Background vs direct causes**
  - Background: gap between formal protocol proofs and messy real deployments (cloud, multi-tenancy, monitoring agents, dev tooling).
  - Direct causes: unsafe optimizations, reuse of secrets or randomness, insufficient isolation, and inadequate secure-coding practices.
- **4.3 Deep structural issues**
  - Concentrated expertise in a few engineers; limited formal verification and red teaming.
  - Asymmetric information: customers cannot easily compare real security posture across providers.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - Without industry-wide hardening and standards, more key-extraction attacks will be found and may lead to major loss events.
- **5.2 Early signals and “spots”**
  - New academic and industry papers exposing concrete attacks.
  - Silent patches or vague security updates in MPC products without detailed postmortems.
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: hardened protocols, memory-safe implementations, TEEs/HSMs, and regular share refresh become standard; attack surface shrinks.
  - Baseline: mixed ecosystem; some providers invest heavily, others lag; occasional incidents continue.
  - Pessimistic: a multi-billion loss tied to MPC key-extraction triggers harsh regulation and long-lasting distrust.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Strong cryptography teams and some history of independent audits.
  - Operational experience with key ceremonies, rotations, and incident response.
- **6.2 Capability gaps**
  - Systematic side-channel analysis, formal verification, and secure-systems engineering for MPC stacks.
  - Productized defense-in-depth patterns (secure enclaves, hardened OS images, safe logging pipelines).
- **6.3 Capabilities that can be built (1–6 months)**
  - Dedicated MPC security engineering function with clear mandate and roadmap.
  - Standardized threat models and red-team playbooks focused on key-extraction.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: MPC’s promise vs observed attacks; asset and stakeholder impact.
  - Problem: effective single points of failure via compromised parties and state leakage.
  - Analysis: map protocol, implementation, infra, and operational attack surfaces; quantify risk concentration.
  - Options: protocol redesign, implementation hardening, hardware isolation, insurance/compensation layers.
  - Risks & follow-ups: regressions, performance impacts, communication and trust-management challenges.
- **7.2 Key judgments**
  - J1: A small set of high-impact key-extraction vectors likely dominates overall theft risk.
  - J2: Lifecycle controls (share refresh, rotation, compartmentalization) can substantially limit blast radius.
  - J3: Transparent disclosure plus credible remediation may be reputationally safer than silence.
- **7.3 Alternative paths**
  - O1 – Minimal patching: fix known issues, add monitoring; cheap but fragile.
  - O2 – Defense-in-depth: combine protocol hardening, hardware isolation, and rigorous audits; higher cost, higher assurance.
  - O3 – Radical redesign: migrate to fundamentally different, perhaps UC-secure or PQ-safe schemes; long horizon, high R&D cost.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Overweighting academic attack models vs real adversary incentives and capabilities.
  - Underestimating customer willingness to tolerate moderate performance overhead for clearly better security.
- **8.2 Required intelligence and feedback**
  - Comparative experiments of different MPC stacks under realistic attack simulations.
  - Customer input on their security vs latency vs cost trade-off preferences.
- **8.3 Validation plan**
  - Commission third-party red-team exercises targeting key-extraction against production-like deployments.
  - Measure effect of mitigations on both attack success probability and latency/availability metrics.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Estimated prevalence and impact of different classes of attacks as more incidents and studies surface.
  - Relative ROI of protocol-level vs infra-level vs operational mitigations.
- **9.2 Incremental adjustment approach**
  - Prioritize low-regret, high-yield improvements (memory safety, secrets management, safe logging) before deeper protocol changes.
  - Iterate based on audit/red-team results and live incident data.
- **9.3 “Better, not perfect” criteria**
  - No known single-party compromise path to full key reconstruction under current best-practice threat models.
  - Independent reviews repeatedly fail to extract keys within realistic attacker budgets.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - The key contradiction is between MPC’s theoretical guarantee of no single point of failure and real deployments where single-party compromise can still leak full keys.
  - A small number of high-impact attack vectors dominate risk; addressing them requires end-to-end design, not just crypto tweaks.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】Security lead + crypto team: complete a structured threat model and attack-surface inventory for key-extraction scenarios, ranking top 5 risks by impact and likelihood (4–6 weeks).
  - 【Important】Engineering: harden secrets-in-memory and logging (zeroization, isolation, access control) and roll out with careful testing (6–10 weeks).
  - 【Important】Leadership: schedule and fund an external security review focused on key-extraction, with a summarized assurance report for key clients (8–12 weeks).
- **10.3 Major risks and responses**
  - Risk (High): new mitigations introduce subtle bugs that open fresh attack paths.
    - Mitigation: staged rollouts, strong regression testing, and independent reviews before full deployment.
  - Risk (Medium): public discussion of vulnerabilities harms brand in the short term.
    - Mitigation: pair disclosure with clear remediation, timelines, and client communication to build long-term trust.
