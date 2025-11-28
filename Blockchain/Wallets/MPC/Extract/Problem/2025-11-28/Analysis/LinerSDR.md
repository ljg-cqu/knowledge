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

## Problem 2 – Complexity and Subtleties in Deploying MPC Wallets

**Context recap**

- Deploying Blockchain MPC wallets requires subtle cryptographic design choices, careful configuration, and integration with heterogeneous blockchain and infrastructure stacks.
- Misunderstood assumptions or misconfigurations can introduce vulnerabilities or degraded UX, slowing mainstream adoption.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - MPC security depends on many parameters (thresholds, key lifetimes, randomness sources, network topology). Making these tunable for various customers increases both flexibility and risk of unsafe deployments.
  - Teams want “plug-and-play” MPC, but underlying protocols are not naturally simple; hiding complexity can also hide critical assumptions.
- **1.2 Goals and conditions**
  - Goal: streamline deployment so that typical engineering teams can roll out MPC wallets with robust security and acceptable performance, reducing deployment errors by ≈30% and increasing adoption of vetted best practices by ≈20% in ~12 months.
  - Conditions: solutions must fit mainstream DevOps stacks (CI/CD, Kubernetes, cloud or on‑prem) and stay within realistic headcount and tooling budgets.
- **1.3 Extensibility and common structure**
  - Reframe from “every customer engineers their own MPC stack” to “well-defined profiles and reference architectures for a few common patterns (custody, dApp wallet, exchange hot wallet)”.
  - Use virtual/physical and hard/soft lenses: separate protocol libraries (virtual, hard) from infra templates and operational processes (physical, soft).

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Roles: cryptographers, core wallet engineers, DevOps/SRE, customer integrators, security reviewers.
  - Artifacts: MPC protocol implementations, config files, deployment templates (Terraform/Helm), monitoring/alerting rules, runbooks.
- **2.2 Balance and degree**
  - More configuration knobs → supports edge cases but expands the space of dangerous misconfigurations.
  - More opinionated defaults and guardrails → safer, but may block unusual but legitimate requirements.
- **2.3 Key internal causal chains**
  - `under-specified_defaults → ad_hoc_customer_changes → subtle_security_gaps / outages`.
  - `poor_observability → slow_detection_of_misconfiguration → prolonged_exposure_or_downtime`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - Vendors: want scalable, low-touch deployment models with few critical incidents.
  - Customer engineering and security teams: need clear responsibilities, predictable behavior, and maintainable configs.
  - End-users and regulators: indirectly affected through security and reliability of the deployed wallet.
- **3.2 Environment and institutions**
  - Diverse infra environments (public cloud, private DC, hybrid) and compliance regimes (data locality, audit logging).
  - Rapidly evolving blockchain stacks, node software, and dev tooling.
- **3.3 Responsibility and room to maneuver**
  - Vendors should provide secure reference architectures, validated templates, and clear “do not change without review” boundaries.
  - Customers should retain room to customize within documented envelopes, taking explicit ownership when diverging.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Early MPC deployments were bespoke projects hand‑held by vendor cryptographers.
  - As demand grew, ad‑hoc scripts and partial documentation were reused as “products” without fully codifying tacit knowledge.
- **4.2 Background vs direct causes**
  - Background: academic descriptions of MPC give little concrete guidance on operationalization.
  - Direct causes: organic growth of deployment tooling, inconsistent conventions, and weak validation before going live.
- **4.3 Deep structural issues**
  - Knowledge concentrated in a few senior engineers; onboarding new teams is slow and fragile.
  - Underinvestment in developer experience (DX) for cryptographic infrastructure.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - As institutions with strict controls adopt MPC wallets, deployment issues will shift from isolated bugs to systemic blockers for deals and integrations.
- **5.2 Early signals and “spots”**
  - Repeated support tickets about the same misconfigurations (thresholds, timeouts, TLS, HSM bindings).
  - Security findings tied not to protocol flaws but to deployment mistakes (e.g., exposed debug ports, unpinned dependencies).
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: vendors ship polished deployment kits and managed offerings; most new deployments follow safe, well-tested paths.
  - Baseline: ecosystem remains split between a few robust platforms and many fragile bespoke setups.
  - Pessimistic: several high-profile incidents blamed on “MPC complexity” sour market perception.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Widespread use of infrastructure‑as‑code, CI/CD, and observability tools that can be leveraged.
  - Accumulated practical experience from early MPC deployments.
- **6.2 Capability gaps**
  - Productized reference architectures with explicit threat models and validated defaults.
  - Automated configuration linting and pre‑deployment security checks specific to MPC.
- **6.3 Capabilities that can be built (1–6 months)**
  - Create tiered deployment blueprints (e.g., small SaaS, regulated institution, exchange‑grade) with clear envelopes.
  - Build static and runtime validators that flag unsafe deviations from these envelopes.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: nature of MPC stacks and environmental diversity.
  - Problem: subtle deployment complexity causing security/UX issues and blocking adoption.
  - Analysis: map lifecycle from design → deploy → operate → upgrade; identify failure modes at each step.
  - Options: managed MPC‑as‑a‑Service, strongly opinionated self‑hosted packages, certified partner integrators.
  - Risks & follow‑ups: vendor lock‑in, reduced flexibility for advanced users, template/doc drift.
- **7.2 Key judgments**
  - J1: Most severe deployment failures are preventable via strong defaults, automation, and validation.
  - J2: Institutions value certified patterns even if they restrict some configurability.
- **7.3 Alternative paths**
  - O1 – "Toolkit": low‑level libraries and examples; maximum flexibility, highest misconfiguration risk.
  - O2 – "Platform": fully managed service; safer and easier, but increases dependency on vendor.
  - O3 – "Hybrid": reference implementation plus optional managed operations; balance between control and safety.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Vendor bias toward pushing managed services as the only safe way.
  - Underestimating highly capable customer teams that prefer full control.
- **8.2 Required intelligence and feedback**
  - Root‑cause analysis of past deployment incidents across customers.
  - Surveys and interviews on desired responsibility split (self‑managed vs managed).
- **8.3 Validation plan**
  - Pilot standardized deployment kits with several customers; measure time‑to‑production and incident frequency vs current baseline.
  - Iterate templates and tooling based on measured outcomes and feedback.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - The granularity of deployment profiles and how opinionated they should be.
  - The set of configuration parameters exposed vs fixed.
- **9.2 Incremental adjustment approach**
  - Start with conservative, secure‑by‑default profiles; gradually expose advanced options behind explicit warnings and support conditions.
  - Adjust documentation and validators as real‑world usage reveals gaps.
- **9.3 “Better, not perfect” criteria**
  - Majority of new deployments complete within planned time and with no critical security findings in initial audits.
  - Reuse of standard templates becomes the norm rather than exception.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - Deployment risk for MPC wallets arises as much from operational subtleties as from pure cryptography.
  - Opinionated, tool‑supported deployment patterns can meaningfully reduce misconfiguration without eliminating flexibility.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】Product + engineering: define 2–3 canonical deployment profiles (e.g., SaaS, VPC, on‑prem) with explicit threat models and assumptions (4–6 weeks).
  - 【Important】DevTools/infra: build configuration validation tools and versioned infra‑as‑code templates for these profiles (6–10 weeks).
  - 【Important】Docs + solutions: produce end‑to‑end runbooks for each profile, targeting SRE, security, and dev personas (8–12 weeks).
- **10.3 Major risks and responses**
  - Risk (Medium): templates lag behind product evolution and become misleading.
    - Mitigation: tie templates to release versions; add CI checks that refuse unsupported combinations.
  - Risk (Medium): power users feel constrained and bypass safeguards.
    - Mitigation: offer an “advanced mode” with clear disclaimers and possibly reduced support guarantees.

---

## Problem 3 – Private Key Recovery and Backup in Hardware and MPC Wallets

**Context recap**

- Hardware wallets rely on a unique secure device; cloning seeds undermines that unicity.
- MPC wallets distribute key shares but still struggle to provide recovery that is both secure and usable.
- Traditional backups (seed phrases, device clones) either weaken security or are too complex for many users.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - Users and institutions want very strong theft resistance *and* forgiving recovery from loss, but cryptographic thresholds are unforgiving once too many shares or devices are lost.
  - Straightforward backup strategies (duplicating seeds/shares) restore recoverability but recreate single points of failure.
- **1.2 Goals and conditions**
  - Goal: design recovery mechanisms that preserve unicity for hardware wallets and offer robust, user‑friendly recovery for MPC wallets, achieving ≥90% recovery success for legitimate users while keeping key‑leakage risk during backup/recovery near zero.
  - Conditions: providers must not gain unilateral control over assets; flows must remain understandable to non‑experts and compatible with custody regulations.
- **1.3 Extensibility and common structure**
  - Decompose recovery into short‑term incidents (device loss), identity loss (accounts, credentials), and long‑term scenarios (inheritance, incapacitation).
  - Use latent/manifest and hard/soft views to distinguish hidden accumulation of risk (e.g., guardian collusion) from visible UX failures.

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Elements: user‑controlled shares/devices, provider‑controlled shares, guardians, recovery servers, secret‑sharing schemes, smart‑contract registries.
  - Processes: enrollment, backup configuration, rotation, revocation, recovery ceremonies, inheritance procedures.
- **2.2 Balance and degree**
  - More guardians / backup paths → higher robustness but more endpoints for attackers.
  - Stronger identity verification and time delays → more security but more friction and support cost.
- **2.3 Key internal causal chains**
  - `unclear_or_cumbersome_backup → users_skip_or_misuse_backup → share_or_device_loss → below_threshold_shares → permanent_asset_loss`.
  - `overly_easy_recovery → social_engineering / coercion_success → fraudulent_recovery → theft`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - Retail users and high‑net‑worth individuals: need reliable access even after loss or death.
  - Institutions and custodians: require formal policies, audit trails, and clear allocation of responsibility.
  - Wallet vendors and key‑management service providers: must design and operate recovery mechanisms.
- **3.2 Environment and institutions**
  - Consumer‑protection norms and expectations around recoverability of financial products.
  - Legal frameworks for inheritance, incapacitation, and fiduciary duties.
  - Data‑protection regulations affecting biometric and off‑chain data used in recovery.
- **3.3 Responsibility and room to maneuver**
  - Providers can offer opinionated recovery presets and education, while exposing advanced options for sophisticated users.
  - Users and institutions choose between stronger sovereignty and stronger safety nets, ideally with clear risk summaries.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Seed‑phrase paradigm made fragile, user‑managed backups the default in early crypto.
  - Hardware wallets adopted deterministic seeds but often reused the same backup UX.
  - MPC wallets initially focused on theft resistance, postponing comprehensive recovery design.
- **4.2 Background vs direct causes**
  - Background: cryptographic irreversibility of key loss and absence of widely accepted identity layers in Web3.
  - Direct causes: complex or poorly tested recovery UX, lack of standardized schemes, and limited stress‑testing with real users.
- **4.3 Deep structural issues**
  - Ideological emphasis on self‑sovereignty over usability and safety nets.
  - Fragmented legal and regulatory views on digital asset inheritance and custodial responsibility.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - As mainstream, less technical users adopt crypto, products without practical recovery will be confined to niches; recovery will become a primary differentiator and regulatory focus.
- **5.2 Early signals and “spots”**
  - Publicized stories and support tickets about unrecoverable wallets after device or password loss.
  - Growing interest in social recovery, passkey‑based flows, cloud‑assisted backups, and fuzzy signatures for biometrics.
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: a small set of privacy‑preserving recovery standards (e.g., layered social+institutional guardians with delays) become de facto norms.
  - Baseline: heterogeneous solutions with a few dominant patterns; some incidents still occur but less frequently.
  - Pessimistic: major losses or abuses of recovery paths cause reputational damage and heavy‑handed regulation.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Mature cryptographic building blocks (secret sharing, threshold schemes, BIFS‑like fuzzy signatures, passkeys).
  - Growing practice around smart‑contract registries and programmable recovery policies.
- **6.2 Capability gaps**
  - Human‑centred design and long‑term lifecycle thinking for recovery workflows.
  - Quantitative risk models that combine social, biometric, hardware, and institutional factors.
- **6.3 Capabilities that can be built (1–6 months)**
  - Cross‑functional recovery design groups (crypto + UX + legal + support).
  - Simulation and red‑team frameworks specifically targeting recovery and inheritance scenarios.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: current backup/recovery practices and their failure modes.
  - Problem: tension between unicity/threshold guarantees and real‑world recoverability requirements.
  - Analysis: classify scenarios (loss, theft, death, coercion) and map to candidate mechanisms.
  - Options: enhanced self‑custody with better UX, hybrid institutional guardians, programmable social recovery and inheritance policies.
  - Risks & follow‑ups: guardian collusion, coercion, privacy leakage, legal ambiguity.
- **7.2 Key judgments**
  - J1: For most users, recovery design is as important as day‑to‑day signing UX.
  - J2: Layered, time‑delayed, multi‑factor recovery often provides the best compromise between security and usability.
- **7.3 Alternative paths**
  - O1 – "Max‑sovereignty": minimal recovery; fits experts, high loss risk for mass market.
  - O2 – "Safety‑first": strong institutional backstops; safer for retail but closer to custodial models.
  - O3 – "Hybrid": social + institutional guardians with programmable delays and caps; more complex but adaptable.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Security‑first bias that underestimates how often users lose devices or credentials.
  - Overconfidence in biometrics and cloud services despite spoofing and privacy risks.
- **8.2 Required intelligence and feedback**
  - Data on device/seed loss rates, support tickets, and user behavior around backups.
  - Legal analysis of inheritance, custodial duties, and biometric data processing.
- **8.3 Validation plan**
  - Usability tests of candidate recovery flows with representative, non‑expert users in realistic stress conditions.
  - Red‑team exercises focused on abusing recovery and inheritance paths.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Default combinations of guardians, factors, and delays across user segments.
  - The role of institutional vs community guardians as markets and regulations evolve.
- **9.2 Incremental adjustment approach**
  - Start with conservative defaults and limited recovery capabilities; relax friction gradually where data supports it.
  - Provide advanced configuration only for well‑informed users or institutions.
- **9.3 “Better, not perfect” criteria**
  - High recovery success in pilots with no observed fraudulent recoveries.
  - Users can explain in simple language how recovery works and what they need to protect.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - Recovery and backup design is central to the value proposition of both hardware and MPC wallets; ignoring it undermines security and adoption.
  - The main tension is between cryptographic irreversibility and human fallibility; layered, delayed, multi‑factor approaches are promising compromises.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】Product + security: inventory current backup/recovery mechanisms and map risks per scenario (loss, theft, death, coercion) (4–6 weeks).
  - 【Important】UX research: design and test at least one layered recovery flow for retail and one for institutional users (6–10 weeks).
  - 【Important】Legal/compliance: review candidate schemes against custody, consumer‑protection, and data‑protection rules (8–12 weeks).
- **10.3 Major risks and responses**
  - Risk (High): new recovery paths become primary theft vectors.
    - Mitigation: strict time delays, rate limits, anomaly detection, and multi‑channel confirmations.
  - Risk (Medium): users misunderstand their responsibilities or over‑trust complex flows.
    - Mitigation: simple mental models, in‑product education, and conservative defaults.

---

## Problem 4 – Balancing Security and Usability in MPC Private Key Management

**Context recap**

- MPC wallets increase security by distributing key control but often introduce complex onboarding, signing, and recovery UX.
- Excessive complexity leads to user errors, low trust, and lower adoption, while oversimplification can hide critical risk information.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - More factors, devices, and approvals reduce certain attack paths but also increase cognitive load, friction, and support burden.
  - Making flows “just work” by hiding details may cause users to misunderstand who controls what and when they are taking on risk.
- **1.2 Goals and conditions**
  - Goal: achieve secure private key handling that feels intuitive to diverse users, increasing adoption by >20% and reducing key‑management errors by ≥30% within 6–12 months, without degrading effective security.
  - Conditions: solutions must scale from individual users to enterprises, and remain compatible with regulatory and policy constraints.
- **1.3 Extensibility and common structure**
  - Decompose UX into phases: onboarding, everyday transactions, exceptional events (policy change, recovery, large transfers).
  - Treat security vs usability as a controllable spectrum, with different profiles (everyday, savings/treasury) rather than a single global setting.

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Interfaces (mobile, web, APIs), authentication methods (passwords, biometrics, passkeys), policy engines, notification and confirmation channels, support workflows.
- **2.2 Balance and degree**
  - Adding too many explicit steps for small, low‑risk actions degrades UX and may push users to insecure workarounds.
  - Too few checks on high‑risk actions (large withdrawals, policy changes) can make the system fragile.
- **2.3 Key internal causal chains**
  - `unclear_or_jargon_heavy_onboarding → misconfigured_security_settings → higher_breach_risk / abandonment`.
  - `opaque_error_states → repeated_failures → frustration → preference_for_centralized_custodial_alternatives`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - End‑users, institutional admins, security and risk teams, customer support, product/UX designers.
- **3.2 Environment and institutions**
  - Competing UX baselines from neobanks, fintech apps, and centralized exchanges.
  - Accessibility and platform guidelines that shape expectations (mobile OSes, web standards).
- **3.3 Responsibility and room to maneuver**
  - Providers must set safe defaults and ensure UX communicates risk levels clearly.
  - Organizations can tune policies for their risk appetite but should understand trade‑offs via clear documentation and simulations.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Early MPC products targeted institutional custody with specialist operators, not mass‑market users.
  - As MPC entered consumer contexts, UX and educational investment lagged behind feature growth.
- **4.2 Background vs direct causes**
  - Background: cryptographic concepts are inherently abstract and hard to teach.
  - Direct causes: UIs that expose internal notions (shares, parties, ceremonies) instead of mapping to user goals.
- **4.3 Deep structural issues**
  - Engineering‑driven roadmaps with limited sustained UX research.
  - Limited measurement of usability failures compared to security metrics.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - Products that cannot reconcile security with smooth UX will either remain niche or be displaced by simpler, often more custodial, alternatives.
- **5.2 Early signals and “spots”**
  - User feedback about confusing flows, long onboarding times, and failed transactions.
  - Emergence of wallets advertising “no seed phrase” and "Web2‑like" experience as key selling points.
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: reusable MPC UX patterns emerge (risk‑based flows, clear tiers, familiar metaphors) that make MPC mostly invisible.
  - Baseline: MPC wallets segment into expert‑focused tools and more guided consumer products; some friction persists.
  - Pessimistic: persistent UX pain cements the view that MPC is “too hard”, slowing broader ecosystem growth.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Strong engineering capabilities and some positive UX precedents from fintech and payments.
- **6.2 Capability gaps**
  - Deep, dedicated UX research for MPC‑specific scenarios (multi‑device signing, policy explanations, recovery Journeys).
  - Quantitative metrics on user errors, drop‑offs, and misconfigurations tied to UX.
- **6.3 Capabilities that can be built (1–6 months)**
  - Establish UX research programs focused on key‑management tasks.
  - Build analytics pipelines that relate UX events (e.g., backtracks, cancellations) to later security or churn outcomes.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: MPC UX challenges and user expectations from other financial apps.
  - Problem: persistent tension between multi‑party security and intuitive, low‑friction interactions.
  - Analysis: map user journeys, identify high‑risk and high‑friction steps, and classify by user segment.
  - Options: risk‑based UX tiers, contextual prompts, automation of safe defaults, strong education and simulation tools.
  - Risks & follow‑ups: oversimplification, user overconfidence, hidden policy complexity.
- **7.2 Key judgments**
  - J1: Users care about perceived control and clarity as much as raw security.
  - J2: Task‑centric, context‑aware flows will outperform generic “security settings” pages.
- **7.3 Alternative paths**
  - O1 – "Security‑max": expose all controls; suitable for specialist ops teams.
  - O2 – "UX‑max": hide most details; better for retail, requires guardrails and limits.
  - O3 – "Contextual": adapt UX to transaction risk, user role, and history.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Engineer bias: assuming users will read docs or tolerate complex mental models.
  - UX bias: focusing on visual polish over clear risk communication.
- **8.2 Required intelligence and feedback**
  - Task completion rates, error statistics, and time‑on‑task for critical flows.
  - Qualitative interviews to understand mental models of “who controls my assets” and “what happens if X fails”.
- **8.3 Validation plan**
  - A/B test redesigned flows on onboarding, sending, and recovery; compare completion, error, and support‑ticket rates.
  - Track any correlated changes in security incidents or near‑misses.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Which UX elements have the highest impact on reducing errors.
  - The right balance between automation and explicit confirmation across segments.
- **9.2 Incremental adjustment approach**
  - Iterate first on the few most consequential flows, rolling out changes gradually and watching metrics.
  - Offer opt‑in “advanced” or “expert” modes rather than exposing complexity to everyone.
- **9.3 “Better, not perfect” criteria**
  - Measurable reduction in key‑management errors and abandonment, with no increase in security incidents.
  - Users report higher confidence and clarity in surveys and interviews.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - Security without usability is self‑defeating; users will circumvent or abandon unusable MPC wallets.
  - The goal is not to show users MPC internals, but to offer clear, trustworthy experiences tailored to risk levels and roles.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】Product + UX: map all key‑management user journeys (onboarding, send, recovery, policy change) and identify top 3–5 friction and error hotspots (4–6 weeks).
  - 【Important】Engineering: implement at least one improved, risk‑based onboarding and send flow and test with controlled cohorts (8–10 weeks).
  - 【Important】Risk/compliance: define UX guardrails—elements that must never be hidden or auto‑bypassed (6–8 weeks).
- **10.3 Major risks and responses**
  - Risk (High): UX simplifications unintentionally lower effective security.
    - Mitigation: security review gate for UX changes, dedicated threat modelling for key flows, and staged rollout.
  - Risk (Medium): one UX profile fails to fit all users.
    - Mitigation: provide segment‑specific profiles (retail, professional, institutional) with clear documentation.

---

