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

## Problem 5 – Scalability and Performance of MPC Protocols in Heterogeneous Environments

**Context recap**

- MPC protocols often require synchronous multi-round communication across participating nodes.
- In heterogeneous environments (different hardware, networks, regions), performance degrades to the slowest node, causing stalls, high latency, and reduced throughput.
- Goal: support near-real-time transaction throughput over heterogeneous nodes without sacrificing core security guarantees.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - Geographic and organizational distribution improves resilience and trust, but increases latency and variance.
  - Reducing the number of rounds or parties can improve performance but may weaken fault tolerance and security assumptions.
- **1.2 Goals and conditions**
  - Goal: minimize stall time and achieve transaction completion times comparable to single-key wallets for most flows, while preserving required threshold security.
  - Conditions:
    - Maintain k-of-n threshold properties and fault tolerance.
    - Keep infrastructure and operational costs sustainable at scale.
- **1.3 Extensibility and common structure**
  - Decompose performance into protocol-level complexity (rounds, messages) and infrastructure-level characteristics (RTT, jitter, CPU, bandwidth).
  - Consider different service tiers: high-frequency / low-latency, standard retail, and treasury/slow-path, each with tuned parameters.

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Elements: signing protocols, precomputation pipelines, node placement and routing logic, timeout/retry policies, batching strategies.
  - Processes: precomputation → online protocol rounds → aggregation → broadcast.
- **2.2 Balance and degree**
  - More precomputation reduces online latency but increases storage, invalidation complexity, and risk if inventories are mismanaged.
  - More nodes and regions improve availability but exacerbate worst-case latency.
- **2.3 Key internal causal chains**
  - `heterogeneous_nodes + synchronous_protocol → wait_for_slowest_node → stalls / timeouts → poor_user_experience`.
  - `naive_routing / placement → unnecessarily_long_paths → higher_RTT → fewer_successful_latency_SLAs`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - High-frequency traders and latency-sensitive dApps: require consistent, low signing latency.
  - Retail users: sensitive to human-perceived delays (sub-second to a few seconds) and reliability.
  - Node operators and infra providers: own costs, maintenance, and availability of nodes.
- **3.2 Environment and institutions**
  - Underlying chain confirmation times, L2/rollup finality guarantees, and mempool dynamics.
  - Data-center connectivity, cross-region routing, and regulatory constraints on data locality.
- **3.3 Responsibility and room to maneuver**
  - MPC providers can design adaptive protocols, smarter node placement, and tiered service offerings.
  - Customers can choose performance profiles and commit to co-location or dedicated capacity where needed.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - MPC protocols were originally optimized for batch or offline computation, not real-time signing.
  - Early deployments ran on relatively homogeneous, centrally managed infra, hiding heterogeneity issues.
- **4.2 Background vs direct causes**
  - Background: protocol designs that assume roughly uniform, well-behaved nodes.
  - Direct causes: deploying those protocols unchanged across diverse clouds, regions, and operator qualities.
- **4.3 Deep structural issues**
  - Lack of standard performance benchmarks and SLOs for MPC-based wallets.
  - Limited co-design between academic protocol work and real-world infrastructure engineering.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - Without targeted improvements, MPC wallets will be perceived as slower and less predictable for demanding use cases, pushing those flows to alternative custody models.
- **5.2 Early signals and “spots”**
  - Customer complaints and metrics showing high p95/p99 signing latency and occasional long stalls.
  - Critical flows (HFT, market-making, gaming) circumventing MPC and using simpler custodial setups.
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: low-round or partially asynchronous protocols, combined with smart infra (co-location, routing), provide strong performance for key segments.
  - Baseline: MPC remains appropriate for treasury and medium-latency flows; time-critical flows rely on other models.
  - Pessimistic: repeated performance incidents during stressed markets damage trust in MPC-based wallets.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Existing crypto and backend teams; some experience with precomputation, batching, and load balancing.
- **6.2 Capability gaps**
  - Deep latency and network-engineering expertise (routing, co-location, BGP), and real-time observability for MPC rounds.
  - SLO-driven product design (clear latency and availability targets for different profiles).
- **6.3 Capabilities that can be built (1–6 months)**
  - End-to-end latency observability: per-hop, per-round metrics and dashboards.
  - Cross-functional performance working groups spanning crypto, infra, and product.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: inherent performance properties of current MPC protocols and infra.
  - Problem: stalls and throughput limits in heterogeneous environments.
  - Analysis: decompose end-to-end latency into protocol, network, and implementation components; identify key bottlenecks.
  - Options: infra-focused optimization, protocol upgrades, and product-level tiering.
  - Risks & follow-ups: added complexity, cost, and risk of security regressions.
- **7.2 Key judgments**
  - J1: For many deployments, RTT × number of rounds dominates pure computation time.
  - J2: Not all flows require ultra-low latency; segmentation is necessary to avoid over-engineering.
- **7.3 Alternative paths**
  - O1 – "Infra-focused": co-location, optimized routing, better node selection, deeper precomputation.
  - O2 – "Protocol-focused": adopt low-round or partially non-interactive MPC schemes.
  - O3 – "Product-focused": expose different performance tiers and SLOs to customers.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Overemphasis on protocol-level innovation while underestimating infra and ops tuning.
  - Underestimating complexity and cost of exotic network configurations.
- **8.2 Required intelligence and feedback**
  - Detailed latency breakdowns from production across regions and customer segments.
  - Customer feedback on latency thresholds and willingness to pay for improved performance.
- **8.3 Validation plan**
  - Run controlled experiments with different node placements, routing policies, and precomputation depths.
  - Pilot "low-latency" profiles with selected customers and compare realized outcomes (e.g., order fill ratios, UX scores) vs baseline.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Assumptions about which flows truly require HFT-grade performance.
  - Relative ROI of infra vs protocol vs product-level changes.
- **9.2 Incremental adjustment approach**
  - Start with safer infra and precomputation optimizations; layer protocol changes once benefits and risks are clearer.
  - Adjust performance tiers and SLOs based on measured demand and outcomes.
- **9.3 “Better, not perfect” criteria**
  - Documented signing SLOs are consistently met for major customer segments.
  - No systemic stalls or severe latency spikes in pilot deployments during market stress.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - Heterogeneous environments exacerbate the synchronous nature of MPC protocols, making latency and stall management central design problems.
  - A mix of protocol, infra, and product strategies is required; no single lever suffices.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】SRE + crypto teams: build and deploy a latency observability stack for MPC rounds with per-region and per-customer views (4–6 weeks).
  - 【Important】Product: define at least two performance profiles (e.g., "standard" and "low-latency") with explicit SLOs and eligibility requirements (6–8 weeks).
  - 【Important】Research/engineering: shortlist and evaluate candidate low-round MPC schemes suitable for future upgrades (8–12 weeks).
- **10.3 Major risks and responses**
  - Risk (High): performance optimizations weaken robustness or security.
    - Mitigation: require security sign-off, chaos testing, and staged rollout for any protocol/infra changes.
  - Risk (Medium): complex performance tiers confuse customers.
    - Mitigation: clear documentation, visual UX indicators, and sales/support enablement.

---

## Problem 6 – Interoperability and Chain-Agnostic Design for MPC-TSS Wallets

**Context recap**

- MPC-TSS wallets must support many blockchains with different signature schemes, transaction formats, and wallet standards.
- Supporting each chain with ad hoc logic increases engineering complexity and the risk of inconsistent security and UX.
- Goal: build MPC wallets that offer secure, chain-agnostic multi-chain support through a unified interface.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - A single MPC-TSS engine must speak many chains’ "signature languages" while preserving strong, composable security properties.
  - Chain-specific optimizations can improve UX and performance but fragment the codebase and make maintenance and auditing harder.
- **1.2 Goals and conditions**
  - Goal: support at least three major chains and operating systems with ~30% less integration effort and ~20% better cross-chain operational efficiency in 12–18 months.
  - Conditions:
    - Per-chain security must remain at least as strong as that chain’s best-practice native wallets.
    - Regulatory and operational constraints per chain must remain satisfied.
- **1.3 Extensibility and common structure**
  - Identify common abstractions: account-based vs UTXO, hash and signing models, fee and nonce semantics.
  - Use virtual/physical and hard/soft lenses to separate chain protocols (hard, physical) from wallet orchestration and policy layers (soft, virtual).

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Elements: core MPC-TSS engine, chain adapters, transaction builders, key- and address-derivation logic, policy engines.
- **2.2 Balance and degree**
  - More shared abstractions → easier to add chains, but can mask chain-specific quirks that matter for security.
  - Heavier chain-specific code → tailored support but harder to keep consistent and properly reviewed.
- **2.3 Key internal causal chains**
  - `ad_hoc_per_chain_integrations → duplicated_logic / divergent_behaviors → inconsistent_security / UX_bugs`.
  - `poorly_defined_abstractions → inability_to_add_new_chains_quickly → lost_market_opportunities`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - Multi-chain users, DeFi protocols, chain foundations, wallet vendors, integrators.
- **3.2 Environment and institutions**
  - Rapid evolution of chain ecosystems, bridges, and interoperability protocols.
  - Varied regulatory treatment of different chains and asset types.
- **3.3 Responsibility and room to maneuver**
  - Wallet vendors should architect extensible frameworks and actively collaborate with chain teams.
  - Chains can publish clearer signing, address, and wallet integration standards to ease MPC support.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Wallets initially built for single dominant chains; later chains bolted on via plugins.
  - Early MPC-TSS designs mirrored this pattern, leading to fragmented integration logic.
- **4.2 Background vs direct causes**
  - Background: lack of cross-chain standards and coordination.
  - Direct causes: one-off integrations for each new chain, each with its own encoding and edge-case behaviors.
- **4.3 Deep structural issues**
  - Incentive misalignment: each chain optimizes locally; wallets bear the complexity cost.
  - Few strong, neutral standardization bodies for wallet–chain interoperability.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - Demand for seamless multi-chain experiences is increasing; wallets that cannot provide them will be sidelined in many use cases.
- **5.2 Early signals and “spots”**
  - Growth of cross-chain DeFi, L2s, and chain-agnostic applications.
  - User frustration with fragmented, chain-specific workflows and differing security properties.
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: de facto standards and shared libraries emerge, enabling robust chain-agnostic MPC stacks.
  - Baseline: wallets support a limited set of chains deeply and others in a thin, higher-risk way.
  - Pessimistic: security incidents stemming from chain-specific adapter bugs discourage "universal" MPC wallets.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Experience integrating multiple chains and modularizing codebases.
- **6.2 Capability gaps**
  - Formal abstraction layers and specification-driven development for multi-chain support.
  - Dedicated security review capacity for chain adapters and cross-chain flows.
- **6.3 Capabilities that can be built (1–6 months)**
  - A chain-integration framework with clear interfaces, conformance tests, and reference adapters.
  - Partnership processes and SLAs with chain teams for co-review and joint incident handling.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: fragmented multi-chain landscape and existing MPC-TSS architectures.
  - Problem: complex, error-prone, chain-specific integration paths.
  - Analysis: define abstraction boundaries and per-chain deltas.
  - Options: common signing layers, intermediate transaction representations, standardized key management.
  - Risks & follow-ups: abstraction leaks, performance regressions, unhandled chain corner cases.
- **7.2 Key judgments**
  - J1: A carefully scoped abstraction layer can cover most chains without erasing critical differences.
  - J2: Strong collaboration with chain teams is essential to maintain security and compatibility.
- **7.3 Alternative paths**
  - O1 – "Focus": support a small set of strategic chains extremely well.
  - O2 – "Platform": invest heavily in generic frameworks and tooling; high upfront cost.
  - O3 – "Ecosystem": push for open standards and shared libraries across multiple vendors.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Overconfidence that abstractions can fully hide chain differences.
  - Underestimation of long-term maintenance burden for many chains.
- **8.2 Required intelligence and feedback**
  - Incident and bug data for current multi-chain wallets.
  - Developer and partner feedback about current integration pain points.
- **8.3 Validation plan**
  - Implement a pilot adapter for a new chain using the proposed framework; measure time to integrate and defect rate vs previous approach.
  - Run focused security reviews on adapted chains to ensure abstractions preserve required guarantees.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Which layers are abstracted (e.g., signatures only vs full transaction building).
  - Prioritized chain list and support depths.
- **9.2 Incremental adjustment approach**
  - Start with 2–3 strategic chains as pilots.
  - Expand only after patterns are stable, secure, and maintainable.
- **9.3 “Better, not perfect” criteria**
  - New chain integrations are meaningfully faster, safer, and easier to audit than before.
  - Users experience mostly consistent flows and security expectations across supported chains.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - Multi-chain support is now table stakes; MPC-TSS wallets need disciplined abstractions and processes to scale without eroding security.
  - Security must not be sacrificed to genericity; abstractions and adapters must be explicitly scoped and reviewed.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】Architecture team: design and document a layered multi-chain wallet architecture with clear abstraction boundaries (4–6 weeks).
  - 【Important】Engineering: refactor at least one existing chain to the new framework and compare integration and defect metrics (8–12 weeks).
  - 【Important】Partnerships/security: establish structured collaboration with 2–3 key chains for joint reviews and incident processes (6–10 weeks).
- **10.3 Major risks and responses**
  - Risk (High): abstraction hides chain-specific security requirements.
    - Mitigation: per-chain security checklists, mandatory security sign-off for each adapter.
  - Risk (Medium): refactoring disrupts existing integrations.
    - Mitigation: dual-stack migration periods, comprehensive regression testing.

---

## Problem 7 – Cost Structure and Economics of Large-Scale MPC Wallet Deployment

**Context recap**

- MPC wallets incur significant infrastructure, operational, and transaction costs: multiple nodes, intensive cryptography, cross-party communication, and on-chain fees.
- At scale, these costs may hinder adoption or incentivize cost-cutting that undermines security.
- Goal: quantify and optimize total cost of ownership (TCO) while preserving security and UX.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - Stronger security (more parties, geo-distribution, redundancy) generally increases cost.
  - Cost-driven shortcuts (fewer nodes, lower redundancy, cheaper infra) can erode resilience and security.
- **1.2 Goals and conditions**
  - Goal: reduce infra/ops and transaction-related costs by ≈20–30% within 12–18 months without weakening security posture.
  - Conditions:
    - No significant increase in downtime, incident probability, or regulatory risk.
    - Pricing remains transparent and acceptable to customers.
- **1.3 Extensibility and common structure**
  - Break down TCO into compute, storage, network, third-party services, human operations, and on-chain fees.
  - Distinguish short-term savings vs long-term risk (e.g., audits and resilience investments as “beneficial negatives”).

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Elements: node counts and capacities, region choices, protocol parameters (rounds, precomputation), monitoring and support structures.
- **2.2 Balance and degree**
  - Overprovisioning reduces risk of saturation but wastes resources.
  - Aggressive consolidation saves cost but increases the impact of node or region failures.
- **2.3 Key internal causal chains**
  - `inefficient_protocol / implementation → higher_CPU_and_network_usage → higher_cloud_bills`.
  - `lack_of_capacity_planning → reactive_scaling_during_spikes → premium_costs + higher_failure_risk`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - MPC providers, customer finance and risk teams, infra vendors, regulators.
- **3.2 Environment and institutions**
  - Cloud pricing trends, competition among custody and wallet providers, fee markets on underlying chains.
  - Regulatory expectations about minimum safeguards regardless of cost.
- **3.3 Responsibility and room to maneuver**
  - Providers can optimize protocols and infrastructure, and design tiered offerings.
  - Customers can select tiers that match their risk appetite and budget.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Early deployments prioritized security narratives and functionality over cost efficiency.
  - As AUM and user bases grew, infra and ops costs scaled up, sometimes unexpectedly.
- **4.2 Background vs direct causes**
  - Background: protocols not originally optimized for cloud economics and large-scale, always-on usage.
  - Direct causes: lack of fine-grained cost attribution, legacy infra decisions, suboptimal batching and resource sharing.
- **4.3 Deep structural issues**
  - Limited visibility of cost drivers in pricing models; customers may not understand trade-offs.
  - Tension between security and operations teams regarding acceptable cost vs risk.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - As price competition intensifies, providers unable to manage TCO while maintaining security will struggle to compete.
- **5.2 Early signals and “spots”**
  - RFPs and negotiations increasingly focus on fees and cost transparency.
  - Internal discussions about relaxing security parameters solely to reduce spend.
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: protocol and infra optimizations deliver strong cost reductions without compromising security or UX.
  - Baseline: tiered offerings emerge; some low-cost products accept weaker guarantees but remain clearly labeled.
  - Pessimistic: cost-cutting leads to incidents that harm trust in MPC custody generally.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Basic cost monitoring, infra automation, and cloud optimization experience.
- **6.2 Capability gaps**
  - Detailed cost models linking protocol and configuration parameters to infra and ops spend.
  - FinOps expertise tailored to high-security, high-availability systems.
- **6.3 Capabilities that can be built (1–6 months)**
  - Unified observability tying per-transaction resource usage to costs.
  - Regular cross-functional cost–risk review cadences.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: current TCO structure for MPC wallets.
  - Problem: high, sometimes opaque costs limiting scale and pricing flexibility.
  - Analysis: map dominant cost drivers and their relationship to protocol and infra choices.
  - Options: protocol optimization, infra tuning, product tiering, selective offloading (e.g., payment channels).
  - Risks & follow-ups: underinvestment in safety, customer confusion about guarantees.
- **7.2 Key judgments**
  - J1: Significant savings are possible from better protocol parameters, batching, and infra choices without eroding security.
  - J2: Many customers will pay premiums for high-security tiers; not all flows require the same guarantees.
- **7.3 Alternative paths**
  - O1 – "Optimize everything": simultaneous protocol, infra, and ops optimizations; complex but high potential.
  - O2 – "Tiered": distinct SKUs (e.g., standard, premium, ultra) with clear security and cost profiles.
  - O3 – "Selective offloading": move some work off-chain (e.g., MPC-based channels) where compatible with risk appetite.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Underestimating difficulty and lead time for protocol-level cost reductions.
  - Overestimating customer appetite for complex pricing and tiering.
- **8.2 Required intelligence and feedback**
  - Detailed cost breakdowns per system, customer, and flow type.
  - Customer research on willingness to pay for extra resilience and security.
- **8.3 Validation plan**
  - Pilot cost-optimized configurations with low-risk internal or test traffic.
  - Trial simpler pricing bundles with selected customers and track adoption and margins.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Estimated savings from protocol vs infra vs operational changes.
  - Customer segmentation and tier definitions.
- **9.2 Incremental adjustment approach**
  - Roll out optimizations gradually with caps on downside (quotas, canary regions, rollback paths).
  - Refine models and tiers as real-world savings and impacts are measured.
- **9.3 “Better, not perfect” criteria**
  - Measurable cost reductions without an increase in security incidents or SLA violations.
  - Pricing that customers understand and see as fair relative to guarantees.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - MPC economics are manageable if cost drivers are well understood and explicitly designed for.
  - Security, performance, and cost must be co-optimized rather than treated independently.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】FinOps + engineering: build a TCO model and dashboards linking protocol parameters and infra decisions to cost (4–6 weeks).
  - 【Important】Product: define at least two service tiers with clear security and performance guarantees and indicative cost profiles (6–10 weeks).
  - 【Important】Engineering: identify and prioritize 2–3 high-ROI protocol or implementation optimizations (8–12 weeks).
- **10.3 Major risks and responses**
  - Risk (High): optimizations inadvertently weaken resilience or security.
    - Mitigation: require security review and fail-safe designs (e.g., automatic rollback triggers) for all cost-driven changes.
  - Risk (Medium): mispriced tiers erode margins or disappoint customers.
    - Mitigation: start with pilots and incorporate feedback before broad rollout.

---

## Problem 8 – UX Complexity Limiting Mass Adoption of MPC Wallets

**Context recap**

- MPC wallets expose complex concepts (shares, ceremonies, multi-device coordination) and non-intuitive recovery flows.
- Many users find these daunting, leading to errors, fear, and reluctance to adopt.
- Goal: significantly simplify UX so that MPC wallets feel comparable in ease to mainstream digital services while preserving security.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - To be secure, MPC wallets must coordinate multiple devices and parties, but such coordination can overwhelm average users.
  - Making flows “magic” and invisible improves ease-of-use but may hide critical consent and risk signals.
- **1.2 Goals and conditions**
  - Goal: increase adoption by ≥20% and reduce user errors related to key management and signing by ≥30% within ~1 year, without increasing incident rates.
  - Conditions:
    - Onboarding and daily use should feel comparable to popular fintech/consumer apps.
    - Flows must still satisfy applicable KYC/AML and compliance constraints where relevant.
- **1.3 Extensibility and common structure**
  - Break UX complexity into cognitive (concepts), procedural (steps), and emotional (fear-of-loss, distrust) dimensions.
  - Analyze virtual/physical aspects of UX: mental models and language vs devices, tokens, and hardware.

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Elements: onboarding flows, day-to-day transaction flows, recovery flows, notifications, help and education surfaces.
- **2.2 Balance and degree**
  - Too much technical explanation overwhelms; too little creates confusion and unsafe behavior.
  - Excessive automation can hide important risks; insufficient automation leaves users to juggle complexity manually.
- **2.3 Key internal causal chains**
  - `jargon_heavy_UI → misunderstanding → misclicks / aborted_flows → churn`.
  - `confusing_recovery_explanations → fear_of_using_wallet_for_large_amounts → limited_adoption`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - New users, experienced crypto users, institutional employees using corporate wallets, customer-support teams.
- **3.2 Environment and institutions**
  - Competing UX patterns from neobanks, mobile payment apps, and centralized exchanges.
  - Platform UX paradigms and accessibility requirements.
- **3.3 Responsibility and room to maneuver**
  - Wallet providers must invest in UX research and design, treating MPC semantics as implementation details rather than user-facing primitives.
  - Users and organizations can choose wallets whose UX matches their skills and risk appetite.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Early wallets reused developer-centric interfaces and jargon.
  - MPC increased internal complexity, but the UX investment often lagged behind feature additions.
- **4.2 Background vs direct causes**
  - Background: crypto culture that tolerates or even celebrates complex, power-user tools.
  - Direct causes: UIs that expose internal MPC structures instead of mapping to user goals and tasks.
- **4.3 Deep structural issues**
  - Underrepresentation of UX disciplines in many crypto organizations.
  - Product KPIs that reward shipping features more than reducing cognitive load.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - Without UX breakthroughs, MPC wallets will remain a niche for technically sophisticated users.
- **5.2 Early signals and “spots”**
  - Empirical studies and user research highlighting usability issues in blockchain wallets.
  - Growth of wallets marketing "no seed phrase" and "Web2-like" experiences.
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: MPC wallets adopt familiar patterns (passkeys, biometric gates, clear limits) and feel similar to mainstream apps.
  - Baseline: specialized MPC wallets for power users; simpler custodial or semi-custodial wallets dominate the mass market.
  - Pessimistic: repeated UX failures and associated losses damage the reputation of MPC wallets.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Some positive UX lessons from consumer fintech and Web2 apps.
- **6.2 Capability gaps**
  - Systematic UX research specifically on MPC-related flows (multi-device coordination, recovery, policy changes).
  - Localization, accessibility, and trust-building UX for diverse regions and user groups.
- **6.3 Capabilities that can be built (1–6 months)**
  - Design systems and pattern libraries for MPC wallet UX (components for approvals, risk indicators, device binding, etc.).
  - Metrics focused on comprehension, trust, and task completion rather than only DAU/MAU.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: current UX pain points and adoption barriers.
  - Problem: cognitive and procedural complexity in key MPC flows.
  - Analysis: classify and prioritize issues by impact on security, adoption, and support load.
  - Options: abstraction layers, in-app education, progressive onboarding, use of familiar identity primitives.
  - Risks & follow-ups: over-simplifying to the point of hiding risk, underestimating diverse user needs.
- **7.2 Key judgments**
  - J1: For most users, mental models should align with familiar financial app patterns.
  - J2: Progressive disclosure and visual cues are typically more effective than long text explanations.
- **7.3 Alternative paths**
  - O1 – "Education-heavy": detailed tutorials and training; good for motivated power users.
  - O2 – "Abstraction-heavy": hide most MPC concepts; rely on guardrails and safety nets.
  - O3 – "Hybrid": stage education and exposure based on user actions and risk level.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Assuming UX patterns from one market/culture will generalize globally.
  - Underestimating the need for ongoing in-app education and feedback.
- **8.2 Required intelligence and feedback**
  - Multi-country user testing, NPS and churn metrics segmented by experience level.
  - Analysis of error rates and abandonment by step in critical flows.
- **8.3 Validation plan**
  - Roll out redesigned flows to small cohorts; compare completion, error, and support-contact metrics.
  - Run trust and comprehension surveys before and after changes.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Which concepts must remain visible vs can be fully abstracted.
  - The amount and format of explanation needed by different segments.
- **9.2 Incremental adjustment approach**
  - Use experiment-driven UX iteration with clearly defined success metrics.
  - Maintain backward-compatible options for existing users during transitions.
- **9.3 “Better, not perfect” criteria**
  - Substantial, sustained reduction in user errors and abandonment with stable or improved security metrics.
  - Users can accomplish common tasks without external help.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - UX is a primary determinant of MPC wallet adoption; complexity must be carefully managed.
  - The right mix of abstraction and education varies by user segment and risk level.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】UX research: run baseline usability tests on current MPC wallet UX with representative users (4–6 weeks).
  - 【Important】Design: prototype simplified onboarding, transaction, and recovery flows based on findings (6–10 weeks).
  - 【Important】Engineering: instrument detailed telemetry to track UX-related errors and drop-offs (4–8 weeks).
- **10.3 Major risks and responses**
  - Risk (High): UX changes obscure key consent and risk moments.
    - Mitigation: maintain explicit confirmations for high-risk actions; require legal/security/UX joint review.
  - Risk (Medium): power users feel constrained.
    - Mitigation: provide advanced/"pro" modes with additional controls and explanations.

---

## Problem 9 – Ethics and Privacy in Data Sharing and User Consent for MPC Wallets

**Context recap**

- MPC wallets distribute key shares and may involve multiple parties, as well as sensitive data such as biometrics and identity information.
- Blockchain transparency and immutability can conflict with privacy and data-erasure rights.
- Goal: fully respect user privacy and consent while enabling secure, auditable MPC operations.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - Distributed key management benefits from multiple parties, but each additional party introduces privacy and misuse risk.
  - Immutable on-chain data (logs, proofs) aids auditability but conflicts with user rights to erasure or consent withdrawal.
- **1.2 Goals and conditions**
  - Goal: achieve a large reduction (e.g., ≈90%) in data leaks and clear, demonstrable compliance with major privacy regimes (e.g., GDPR-like laws) within 12–18 months.
  - Conditions:
    - Collect and retain only necessary data.
    - Provide users with understandable consent management and visibility into data use.
- **1.3 Extensibility and common structure**
  - Separate categories of data: cryptographic key material, operational metadata (policies, logs), and personal data (identity, biometrics).
  - Analyze latent and manifest risks such as linkage attacks from public data vs explicit leaks.

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Elements: key shares, custodial partners, consent records, logs, biometric templates, encryption keys, data-retention policies.
- **2.2 Balance and degree**
  - More monitoring and logging improves security and compliance evidence but increases exposure and breach impact if compromised.
  - Strong anonymization and minimization measures aid privacy but may reduce forensic capability.
- **2.3 Key internal causal chains**
  - `vague_or_overbroad_consent + broad_data_collection → misuse / over-sharing → user_trust_loss + legal_risk`.
  - `weak_governance_of_key_shares → unauthorized_use_or_combination_of_shares → theft_or_privacy_breach`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - Users, wallet providers, third-party custodians/partners, regulators, auditors, civil-society groups.
- **3.2 Environment and institutions**
  - GDPR and similar laws, evolving privacy norms, industry guidelines on biometrics and cryptographic data.
  - Cross-border data-transfer and localization requirements.
- **3.3 Responsibility and room to maneuver**
  - Providers must design systems with privacy-by-default and explicit, granular consent.
  - Regulators can offer guidance and sandboxes; users can select providers aligned with their privacy expectations.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Early crypto prioritized pseudonymity and censorship resistance but paid less attention to broader data-protection principles.
  - Biometric and cloud-based backup schemes appeared before mature privacy frameworks were in place.
- **4.2 Background vs direct causes**
  - Background: inherent tension between transparency/traceability (for compliance, security) and privacy/erasability.
  - Direct causes: ad hoc handling of biometric data, logs, and key-sharing arrangements, and poor visibility of data flows.
- **4.3 Deep structural issues**
  - Asymmetric information: users rarely see how their data and key shares are processed or shared.
  - Lack of mature, MPC-specific ethical and privacy frameworks.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - Privacy and ethical scrutiny are increasing as adoption grows and regulators focus more on data and algorithmic governance.
- **5.2 Early signals and “spots”**
  - Emergence of consent-management tooling, privacy-preserving computation frameworks, and policy discussions about MPC and biometrics.
  - Early regulatory statements about digital identity, data minimization, and cryptographic systems.
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: privacy-by-design MPC wallet standards emerge and gain adoption; transparency and trust improve.
  - Baseline: patchwork compliance; some providers differentiate on privacy, while others treat it as a minimum-cost obligation.
  - Pessimistic: scandals around misuse or leakage of biometric or key-share data trigger harsh regulation and distrust.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Cryptographic tools (e.g., zero-knowledge proofs, secure logging, anonymization) and growing privacy engineering practice.
- **6.2 Capability gaps**
  - Integrated treatment of legal, ethical, and technical aspects of MPC wallets.
  - Usable consent and privacy preference design that non-experts can understand.
- **6.3 Capabilities that can be built (1–6 months)**
  - Formal privacy threat models and Data Protection Impact Assessments (DPIAs) for MPC wallets.
  - Cross-functional privacy/ethics review boards and playbooks for design and incidents.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: MPC data flows, key-share distribution, and current privacy challenges.
  - Problem: aligning operations with user rights, consent expectations, and ethical standards.
  - Analysis: categorize data types, flows, storage, and risk points.
  - Options: strong minimization, anonymization and pseudonymization, local-first approaches, advanced cryptography, consent tooling.
  - Risks & follow-ups: usability trade-offs, evolving regulations, over- or under-collection of data.
- **7.2 Key judgments**
  - J1: Data minimization is the single most robust privacy protection.
  - J2: Transparent, granular consent flows and clear explanations can increase user trust.
- **7.3 Alternative paths**
  - O1 – "Compliance-minimum": meet legal minimums with limited differentiation.
  - O2 – "Privacy-first": exceed requirements and use privacy as a competitive advantage.
  - O3 – "Adaptive": offer configurable privacy profiles for different segments.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Techno-optimism about cryptographic privacy tools solving all issues.
  - Legal minimalism that underestimates reputational and ethical dimensions.
- **8.2 Required intelligence and feedback**
  - Comparative legal analysis across jurisdictions; user research on privacy expectations and tolerance.
  - Benchmarks on incident and leak rates for different architectures.
- **8.3 Validation plan**
  - Conduct DPIAs and external privacy/security audits of MPC wallet architectures.
  - Pilot privacy-enhancing changes and track trust, adoption, and complaint metrics.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Interpretation of laws and standards as regulations and guidance evolve.
  - The balance between logging for security and minimization for privacy.
- **9.2 Incremental adjustment approach**
  - Introduce privacy improvements progressively; keep legacy modes only where unavoidable but clearly mark them.
  - Update policies and UX responsive to audits, incidents, and user feedback.
- **9.3 “Better, not perfect” criteria**
  - No major privacy incidents or clear regulatory violations; positive trends in trust indicators.
  - Users can understand, at a high level, what data is used for what purpose.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - Ethics and privacy are central to long-term viability and social acceptance of MPC wallets.
  - Minimization, transparent consent, and strong governance are key levers.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】Privacy/legal: perform DPIAs covering all data types and flows in MPC wallet systems (4–8 weeks).
  - 【Important】Product/UX: redesign consent and privacy settings to be clear, granular, and manageable (6–10 weeks).
  - 【Important】Security/infra: review logging and data-retention policies; implement minimization and encryption where possible (6–12 weeks).
- **10.3 Major risks and responses**
  - Risk (High): hidden data flows violate laws or expectations.
    - Mitigation: comprehensive data mapping, regular audits, and open communication.
  - Risk (Medium): overly strict privacy defaults impair security or support.
    - Mitigation: tiered options with explicit trade-offs and documented justifications.

---

## Problem 10 – Lack of Standardized Best Practices and Certifications for MPC Wallet Security

**Context recap**

- MPC wallets rely on complex cryptographic and operational practices, but industry-wide standards, audits, and certifications are immature.
- This inconsistency erodes trust and makes it hard for customers and regulators to assess security.
- Goal: establish clear, recognized best practices and certification paths for MPC wallet security.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - MPC providers claim strong security, yet there is no common benchmark or certification to substantiate claims.
  - Deeply bespoke implementations enable fine-grained optimization but hinder standardization and comparability.
- **1.2 Goals and conditions**
  - Goal: reduce vulnerabilities and unauthorized access incidents by ≈75% within a year of standard adoption and improve audit efficiency by ≈50%.
  - Conditions:
    - Standards must be technology-neutral enough to accommodate ongoing protocol innovation.
    - Certification must be practical in cost and time for a range of providers.
- **1.3 Extensibility and common structure**
  - Decompose standards into protocol requirements, implementation practices, operational controls, and governance requirements.
  - Consider layered models: baseline controls for all MPC wallets; higher tiers for critical infrastructure.

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Elements: control catalogues, reference architectures, test suites, audit methodologies, training materials.
- **2.2 Balance and degree**
  - Overly rigid standards risk freezing innovation and excluding new schemes.
  - Too flexible standards risk degenerating into box-ticking with little real assurance.
- **2.3 Key internal causal chains**
  - `no_common_standards → inconsistent_security_posture → frequent_incidents → regulator_and_customer_distrust`.
  - `unclear_audit_methodology → expensive / shallow_audits → limited_assurance_and_slow_improvement`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - Vendors, customers, auditors, regulators, industry associations.
- **3.2 Environment and institutions**
  - Existing standards in adjacent domains (e.g., FIPS for crypto modules, PCI-DSS, cloud security frameworks).
  - Emerging blockchain and digital-asset regulations referencing custody and operational resilience.
- **3.3 Responsibility and room to maneuver**
  - Industry consortia and standards bodies can define MPC-specific frameworks.
  - Regulators can endorse or reference these frameworks and integrate them into oversight.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Rapid MPC innovation and commercialization outpaced formal standardization.
  - Early providers emphasized differentiation and secrecy rather than transparency and shared baselines.
- **4.2 Background vs direct causes**
  - Background: fragmentation of academic and industrial efforts; lack of central coordination.
  - Direct causes: limited incentives and structures to create and adopt shared standards and certification.
- **4.3 Deep structural issues**
  - Competitive secrecy and fear that transparency will expose design weaknesses.
  - Small pool of experts capable of drafting, reviewing, and maintaining robust standards.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - As assets and regulatory attention grow, pressure for standardization and certification will increase.
- **5.2 Early signals and “spots”**
  - Whitepapers and design documents from major providers, early MPC-as-a-Service platforms, and blockchain-assurance efforts.
  - Discussions in policy and industry forums about MPC assurance and auditability.
- **5.3 Possible scenarios (6–24 months)**
  - Optimistic: reference standards and certification schemes emerge; providers compete on exceeding baselines and publishing results.
  - Baseline: partial adoption; larger players adopt standards early, smaller players follow slowly.
  - Pessimistic: a major failure leads to rushed, heavy-handed regulations that are misaligned with technical realities.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Experience with other security standards, certifications, and audits.
  - Pockets of expertise in MPC research and engineering across industry and academia.
- **6.2 Capability gaps**
  - Broad consensus on what “good” MPC wallet security entails.
  - Practical testing, conformance, and certification procedures tailored to MPC.
- **6.3 Capabilities that can be built (1–6 months)**
  - Working groups and task forces for MPC wallet standards under neutral organizations.
  - Open-source conformance, fuzzing, and benchmark test suites.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: current ad hoc assurance landscape for MPC wallets.
  - Problem: lack of standardized best practices and certifications.
  - Analysis: identify necessary components of a framework (protocol, implementation, operations, governance).
  - Options: industry self-regulation, formal standards bodies, regulation-driven frameworks, or hybrids.
  - Risks & follow-ups: slow consensus, misalignment with innovation pace, uneven global adoption.
- **7.2 Key judgments**
  - J1: Voluntary, industry-driven standards can move faster initially than formal regulation.
  - J2: Transparent certification benefits both vendors (credibility) and customers (comparability).
- **7.3 Alternative paths**
  - O1 – "Industry-first": consortia define frameworks and reference architectures and seek regulatory recognition.
  - O2 – "Regulation-first": regulators define mandatory minimums; slower but potentially more universal.
  - O3 – "Hybrid": industry frameworks that are later adopted or referenced by regulators.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Overestimating competitors’ willingness to collaborate.
  - Underestimating regulators’ desire to impose their own rules regardless of industry work.
- **8.2 Required intelligence and feedback**
  - Stakeholder interviews across vendors, customers, auditors, and regulators.
  - Analysis of past incidents to see common failure patterns that standards must address.
- **8.3 Validation plan**
  - Pilot a draft framework with a small group of vendors and auditors and collect detailed feedback.
  - Iterate the control catalogue and testing approach based on pilot experience.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Scope and granularity of controls and certification levels.
  - Recommended cadence for recertification and continuous monitoring.
- **9.2 Incremental adjustment approach**
  - Start with a minimal, widely acceptable baseline; extend to advanced tiers once adoption is established.
  - Align revisions with observed incident patterns and new research.
- **9.3 “Better, not perfect” criteria**
  - Frameworks that materially improve assurance and transparency without freezing innovation or excluding smaller vendors.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - Standardization around MPC wallet security is necessary for long-term trust and regulatory clarity.
  - Effective frameworks must balance rigor, practicality, and flexibility.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】Industry leaders: convene a working group to scope MPC wallet security standards and governance (4–6 weeks).
  - 【Important】Security experts: draft an initial control catalogue, reference architecture, and testing approach (8–12 weeks).
  - 【Important】Auditors: prototype an audit methodology and pilot it with willing vendors (8–16 weeks).
- **10.3 Major risks and responses**
  - Risk (High): frameworks deteriorate into box-ticking exercises.
    - Mitigation: include outcome-based metrics (incident frequency, response times) and require incident reporting.
  - Risk (Medium): smaller vendors struggle with certification cost.
    - Mitigation: tiered certification levels and open-source tooling to lower barriers.

---

## Problem 11 – Future Quantum Computing Risks to MPC Wallets

**Context recap**

- Many MPC wallets rely on classical public-key schemes (e.g., ECDSA, RSA) that are vulnerable to quantum attacks such as Shor’s algorithm.
- Progress in quantum computing threatens long-term security of current keys and signatures.
- Goal: design and execute a transition to quantum-resistant cryptography for MPC wallets.

### 1. Problem Definition (Aspect 1)

- **1.1 Problem and contradictions**
  - Current schemes are efficient, widely supported, and well understood, but may be breakable by sufficiently powerful quantum computers.
  - Early adoption of post-quantum cryptography (PQC) may incur performance, key-size, and compatibility costs before quantum threats materialize.
- **1.2 Goals and conditions**
  - Goal: achieve zero quantum-related breaches and be able to migrate users to PQC-enabled MPC wallets smoothly within ~1–3 years once standards and ecosystems stabilize.
  - Conditions:
    - Maintain compatibility with existing chains as far as protocols permit.
    - Meet regulatory expectations for "crypto-agility" and long-term risk management.
- **1.3 Extensibility and common structure**
  - View quantum risk as part of a broader class of "future-proofing" and migration problems.
  - Distinguish near-term, medium-term, and long-term impact horizons and plan accordingly.

### 2. Internal Logical Relations (Aspect 2)

- **2.1 Key elements**
  - Elements: existing MPC schemes, candidate PQC algorithms, hybrid schemes, key-rotation and migration procedures, wallet software versions.
- **2.2 Balance and degree**
  - Stronger (PQC) primitives may have larger keys and signatures and higher computational cost.
  - Hybrid schemes (classical + PQC) can mitigate risk but add complexity and surface for implementation bugs.
- **2.3 Key internal causal chains**
  - `long_lived_keys + archived_transaction_data → future_quantum_attacker_can_derive_private_keys → retroactive_asset_compromise`.
  - `rushed_migration_without_testing → implementation_flaws → immediate_vulnerabilities`.

### 3. External Connections (Aspect 3)

- **3.1 Stakeholders**
  - Wallet providers and cryptographers, blockchain protocol developers, users (retail and institutional), regulators, standardization bodies.
- **3.2 Environment and institutions**
  - PQC standardization efforts (e.g., NIST-like processes), chain-level roadmaps for PQC support, evolving regulatory views on long-term cryptographic safety.
- **3.3 Responsibility and room to maneuver**
  - Providers should monitor PQC developments, participate in standards discussions, and design for future migration.
  - Chains and regulators can signal expectations and timelines for PQC adoption.

### 4. Origins of the Problem (Aspect 4)

- **4.1 Key historical nodes**
  - Adoption of classical public-key cryptography long before credible quantum computers existed.
  - Increased awareness of quantum risks in cryptography and blockchain communities in recent years.
- **4.2 Background vs direct causes**
  - Background: the mathematical vulnerability of many current public-key schemes to known quantum algorithms.
  - Direct causes: deployment of long-lived keys and signatures without clear migration paths.
- **4.3 Deep structural issues**
  - Inertia in upgrading cryptographic primitives across heterogeneous wallets, chains, and infrastructures.
  - Uncertainty about the exact timelines and practical capabilities of quantum machines.

### 5. Problem Trends (Aspect 5)

- **5.1 Current trend judgment**
  - Even if large-scale quantum computers are years away, "harvest now, decrypt later" attacks pose a long-term risk to data and assets.
- **5.2 Early signals and “spots”**
  - Growing PQC research, standardization of lattice-based schemes, and early PQC prototypes.
  - Policy discussions about quantum-readiness and critical infrastructure.
- **5.3 Possible scenarios (6–36 months)**
  - Optimistic: mature PQC standards and implementations become widely available; MPC wallets can adopt hybrids and transition in a planned way.
  - Baseline: incremental adoption of PQC in non-critical paths first; full wallet migration takes several years.
  - Pessimistic: sudden breakthroughs or geopolitical shocks force rushed, high-risk migrations.

### 6. Capability Reserves (Aspect 6)

- **6.1 Existing capabilities**
  - Crypto teams familiar with current PQC research and hybrid protocol design.
- **6.2 Capability gaps**
  - Production-quality PQC implementations integrated into MPC stacks.
  - Tested, user-friendly migration and key-rotation strategies.
- **6.3 Capabilities that can be built (1–6 months)**
  - Internal PQC evaluation projects focusing on performance and integration complexity.
  - High-level migration plans and threat models for quantum-era scenarios.

### 7. Analysis Outline (Aspect 7)

- **7.1 Structured outline**
  - Background: classical cryptography reliance and emerging quantum risks.
  - Problem: ensuring long-term security of MPC wallets and assets.
  - Analysis: identify where classical cryptography is used (keys-in-use, archives) and assess exposure.
  - Options: hybrid schemes, early PQC adoption in low-risk paths, aggressive key-rotation policies.
  - Risks & follow-ups: performance hits, incompatibilities, and migration bugs.
- **7.2 Key judgments**
  - J1: Crypto-agility (ability to swap schemes) is essential regardless of quantum timelines.
  - J2: Gradual, well-tested migration beats rushed, all-at-once transitions when quantum threats become acute.
- **7.3 Alternative paths**
  - O1 – "Wait-and-see": minimal immediate changes; monitor PQC and adopt later.
  - O2 – "Hybrid-early": introduce PQC in combination with classical schemes in some flows.
  - O3 – "PQC-first": aggressively adopt PQC once standards stabilize in key components.

### 8. Validating the Answer (Aspect 8)

- **8.1 Potential biases**
  - Over- or under-estimating the speed of quantum progress.
  - Overconfidence in early PQC schemes before extensive real-world testing.
- **8.2 Required intelligence and feedback**
  - Up-to-date information from cryptographic and quantum-computing communities.
  - Performance benchmarks and security analyses of candidate PQC schemes within MPC.
- **8.3 Validation plan**
  - Prototype hybrid MPC wallets in test environments; measure performance and complexity.
  - Engage external experts for review of proposed migration and PQC choices.

### 9. Revising the Answer (Aspect 9)

- **9.1 Parts likely to be revised**
  - Choice of PQC algorithms and deployment timelines as standards and implementations evolve.
  - Priority areas for migration across chains and products.
- **9.2 Incremental adjustment approach**
  - Maintain crypto-agile designs that can swap primitives with minimal code changes.
  - Plan migration in phases: non-critical data first, then high-value assets.
- **9.3 “Better, not perfect” criteria**
  - Clear, feasible migration plans exist and have been partially tested before urgent need arises.
  - Users can transition with minimal disruption when migrations occur.

### 10. Summary & Action Recommendations (Aspect 10)

- **10.1 Core insights**
  - Quantum computing presents a serious long-term risk to classical cryptography underlying MPC wallets.
  - Crypto-agility, hybrid schemes, and planned migration are necessary to manage that risk.
- **10.2 Near-term action list (0–3 months)**
  - 【Critical】Crypto team: map all uses of classical public-key cryptography in MPC wallet systems and assess long-term exposure (4–6 weeks).
  - 【Important】Architecture: design crypto-agile components and identify candidate PQC and hybrid schemes for evaluation (6–10 weeks).
  - 【Important】Leadership: define an internal quantum-risk strategy and communication plan for stakeholders (8–12 weeks).
- **10.3 Major risks and responses**
  - Risk (High): premature or poorly implemented PQC introduces immediate vulnerabilities.
    - Mitigation: staged pilots, independent reviews, and conservative rollout.
  - Risk (Medium): complacency leads to underinvestment until it is too late.
    - Mitigation: regular quantum-risk reviews and checkpoints in technical and risk governance.

---

