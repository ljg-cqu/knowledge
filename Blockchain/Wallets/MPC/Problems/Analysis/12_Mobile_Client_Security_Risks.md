# Mobile Client Security Risks in Consumer MPC Wallet Implementations – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Mobile Security Team  
**Related Problem**: `/Blockchain/Wallets/MPC/Problems/12_Mobile_Client_Security_Risks.md`

---

## Context Recap

- **Problem title**: Mobile Client Security Risks in Consumer MPC Wallet Implementations
- **Current state**:
  - Consumer MPC wallets (ZenGo, Web3Auth, Privy, Magic, others) widely use 2-of-2 threshold schemes where Share A lives on the user’s mobile device and Share B on the provider’s server [Source: MPC Wallets – A Complete Technical Guide, Stackup, 2025, https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide].
  - Mobile shares are typically stored via iOS Keychain (often with Secure Enclave support) or Android Keystore/StrongBox where available, but many deployments still fall back to software-only keystores on fragmented Android hardware [Source: Android Keystore System, Android Developers, 2024, https://developer.android.com/privacy-and-security/keystore].
  - Mobile threat landscape shows increasing prevalence of banking trojans, spyware, and supply-chain attacks that specifically target financial apps and credential stores [Source: 2024 Annual Mobile Threat Report, Lookout, 2024, https://www.lookout.com/threat-intelligence/report/2024-annual-mobile-threat-report].
- **Pain points**:
  - Device compromise (malware, OS exploits, physical theft + forensic extraction) can expose the local MPC share, turning “2-of-2” into “1.5-of-2” in practice when combined with a server breach.
  - Rooting/jailbreaking, sideloaded apps, and insecure networks (public WiFi, hostile routers) dramatically expand the attack surface for mobile MPC clients [Source: 2025 Q1 Mobile Threat Landscape Report, Lookout, 2025, https://www.lookout.com/threat-intelligence/report/2025-q1-mobile-threat-landscape-report].
  - Backup, screenshot, and debug-interface leakage can expose encrypted shares, partial signatures, or sensitive recovery flows even without full device compromise [Source: OWASP MASVS v2.0.0, OWASP, 2023, MASVS-STORAGE & MASVS-RESILIENCE controls, https://github.com/OWASP/masvs].
- **Goals (from problem file)**:
  - ≥95% of shares stored using hardware-backed secure storage (Secure Enclave / StrongBox) by Q4 2026.
  - 100% of major providers blocking operation on rooted/jailbroken devices by Q2 2026.
  - Forensic resistance: shares unextractable via mainstream forensic tools (Cellebrite UFED, GrayKey) on locked devices, validated via independent testing [Source: Cellebrite Inseyets Powered by UFED, Cellebrite, 2024, https://cellebrite.com/en/ufed/].
  - Eliminate unencrypted backup exposure by Q2 2026; universal TLS 1.3 + certificate pinning; robust memory/screenshot protections; ≥60% coverage for mobile threat defense (MTD) integrations by Q4 2026.
- **Hard constraints**:
  - 24‑month security hardening and rollout window (Q1 2026–Q4 2027) with per‑provider budgets ≈$0.5–2M.
  - Cannot control all OS/cloud backup behavior or user choices for device PIN/biometrics.
  - Hardware capabilities (Secure Enclave, StrongBox) absent on part of the installed base.
- **Key facts**:
  - Secure enclave and StrongBox keep keys inside hardware-isolated coprocessors with dedicated key hierarchies and anti‑tampering protections [Source: Apple Platform Security Guide, Apple, 2024, section "Secure Enclave", https://support.apple.com/guide/security/welcome/web; Source: Android 9 Features – Hardware Security Module / StrongBox, Android Developers, 2024, https://developer.android.com/about/versions/pie/android-9.0].
  - Forensic tools can extract rich data sets, including keychain/keystore artifacts and app sandboxes, on a wide range of iOS/Android versions given physical access and, in some cases, a weak passcode or jailbreak/root [Source: "Extractions of iOS Devices", Cellebrite Glossary, Cellebrite, 2023, https://cellebrite.com/en/glossary/extractions-of-ios-devices-mobile-device-forensics/; Source: Mobile Cyber Forensic Investigations of Web3 Wallets on Android, Alharbi et al., Applied Sciences (MDPI), 2022, https://doi.org/10.3390/app122111180].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

1. **Core contradiction**
   - Marketing claim: "No single point of failure" because keys are split between mobile and server.
   - Reality: Mobile clients are often the *softest* target in the MPC stack; once the on‑device share is extracted, a subsequent server breach or insider attack can reconstruct the full key.
   - Thus, the system behaves more like "single point of *compromise*" in practice when mobile security is weak.

2. **Security vs. usability**
   - Strong device security (Secure Enclave, strict root detection, blocking screenshots, disabling operation on older/unsupported devices) improves share protection but increases friction, reduces compatibility, and risks churn among power users on rooted devices [Source: OWASP MASVS-RESILIENCE, OWASP, 2023, https://github.com/OWASP/masvs].
   - Providers are incentivized to prioritize growth and UX; security controls that block sign‑in or transactions on compromised devices may be down‑scoped unless mandated by incidents or regulation.

3. **Endpoint vs. server-centric mindset**
   - Many MPC providers invest heavily in server-side HSM/KMS security, audits, and certifications, but treat mobile app hardening as "nice to have" rather than a first‑class security domain.
   - However, forensic evidence shows that poorly hardened mobile wallets leak seeds, private keys, and transaction metadata that can be reconstructed post‑incident [Source: Mobile Cyber Forensic Investigations of Web3 Wallets on Android, Alharbi et al., MDPI Applied Sciences, 2022].

### 1.2 Goals & conditions

- **Security outcome goals** (restated and refined):
  - **Hardware‑backed storage**: ≥95% of active users’ on‑device shares generated and stored in Secure Enclave (iOS) or StrongBox-backed keystores (Android) by Q4 2026.
  - **Compromised-device refusal**: 100% of major providers ship root/jailbreak/resigning detection that blocks sensitive operations (key generation, signing, recovery) on compromised devices by Q2 2026.
  - **Forensic robustness**: Independent labs fail to recover usable MPC shares from locked, non‑rooted devices using current commercial tools (UFED, GrayKey) in ≥95% of test cases [Estimate: based on target resilience profile; validation via commissioned assessments].
  - **Backup & memory hygiene**: 0% of MPC shares or recovery materials stored in unencrypted or cloud‑synced backups; secrets in memory are zeroized immediately after use and never appear in log/screenshot/debug channels [Source: OWASP MASVS-STORAGE, OWASP, 2023].
  - **Network integrity**: 100% of providers enforce TLS 1.3 with strong cipher suites plus certificate pinning for MPC sessions, with no known downgrade paths [Source: MASVS-NETWORK-1, OWASP, 2023, https://github.com/OWASP/masvs/blob/master/controls/MASVS-NETWORK-1.md].

- **Conditions / constraints**:
  - **Time**: 24 months to design, implement, test, and roll out across heterogeneous mobile platforms.
  - **Budget**: $0.5–2M per provider, covering engineering, audits, threat‑defense SDK licenses, and red‑teaming.
  - **Coverage gap**: Long tail of low‑end Android devices lacking StrongBox; must define acceptable fallbacks and possibly risk‑tiered support.

### 1.3 Extensibility & reframing

- **Attribute reframing**:
  - From "key share location" to **"attack cost to obtain each share"**: objective is maximizing attacker cost for *each* share independently, not merely distributing storage.
  - From "mobile app security" to **"device state + app hardening + user behavior"**: risk is a function of all three.

- **Structural reframing**:
  - Treat the mobile client as part of an **end‑to‑end cryptographic system** with hardware, OS, app, and backend; view weaknesses as compositional rather than isolated.
  - Consider additional factors beyond 2‑of‑2 (e.g., introducing a third factor such as hardware security keys, secure desktop client, or recovery service) for high‑value users to reduce dependence on a single mobile endpoint [Source: MPC Wallets – A Complete Technical Guide, Stackup, 2025].

- **Problem expansion**:
  - Rather than “How do we secure mobile MPC wallets?”, reframe as: **“How do we ensure the marginal risk added by mobile endpoints is within acceptable bounds versus server‑only custody and self‑custody alternatives?”** This enables explicit risk‑/value comparison across custody models.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Roles**:
  - End users (retail + prosumers).
  - Mobile app (iOS, Android, possibly React Native/Flutter shell).
  - Secure storage & hardware (Secure Enclave, StrongBox, TEE, software keystore).
  - MPC protocol engine (client + server components).
  - Security controls: root/jailbreak checks, MTD SDK, certificate pinning, anti‑debugging, screenshot blocking.
  - Provider backend (MPC server, risk engine, observability).

- **Resources**:
  - Engineering headcount and security expertise.
  - Vendor products (MTD, anti‑debugging/obfuscation, device attestation).
  - Forensic and penetration‑testing partners.

- **Processes**:
  - Key generation and share distribution.
  - Transaction authorization, MPC signing flows.
  - Backup and recovery flows (including cross‑device migration).
  - Release and incident‑response processes.

### 2.2 Balance & "degree"

- **Security friction vs. activation/churn**:
  - Blocking rooted/jailbroken devices, requiring strong passcodes/biometrics, and disabling screenshots in recovery flows improve security but reduce compatibility and developer ergonomics [Source: MASVS-RESILIENCE, OWASP, 2023].
  - Over‑strict policies (e.g., refusing all devices without hardware‑backed keystore) may cut off users on budget Android phones; under‑strict policies increase tail‑risk.

- **Forensic resistance vs. recoverability**:
  - Excluding sensitive data from backups and binding keys to hardware can make account recovery harder (e.g., if user loses device and cannot access backup).
  - Must balance **irrecoverable loss** risk against **theft/forensic extraction** risk.

- **Detection depth vs. performance and battery**:
  - Deep runtime integrity checks, attestation, and continuous MTD scans consume CPU, memory, and battery, and can degrade UX.

### 2.3 Causal chains (examples)

1. **Compromised device → share exfiltration → key reconstruction**
   - User installs malware (e.g., trojanized wallet or banking trojan with accessibility abuse) → malware acquires overlay/Accessibility privileges → intercepts wallet PIN/biometrics proxy, dumps process memory or keystore handles → attacker retrieves on‑device share.
   - Separately, provider suffers server breach exposing server share database (or insider extracts shares from HSM exports) → attacker combines mobile share + server share → reconstructs private key and drains funds [Source: 2024 Annual Mobile Threat Report, Lookout, 2024].

2. **Weak backup configuration → cloud breach → historical share exposure**
   - App data (including encrypted share or derived key material) is included in iCloud/Google Drive backups → attacker compromises user’s cloud account or cloud provider → obtains encrypted material; if per‑device keys are not hardware‑bound or properly derived, offline cracking or future crypto weaknesses may expose the share [Source: Apple Platform Security – Data Protection, Apple, 2024].

3. **Disabled certificate pinning → MITM → protocol compromise**
   - Wallet app trusts system CAs only, no pinning → attacker controls local network or installs malicious root CA via MDM/malware → intercepts TLS traffic between mobile and MPC server, potentially manipulating protocol messages, downgrading ciphers, or harvesting partial signature data for side‑channel analysis [Source: MASVS-NETWORK-1, OWASP, 2023].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholder table

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | Mobile OS vendors (Apple, Google), OEMs | Provide secure hardware/OS primitives; maintain ecosystem viability | Backward compatibility, device cost, ecosystem politics | Wallets may demand stronger controls than OS can enforce globally |
| Upstream | MTD / security SDK vendors | Detect device compromise, malware, risky networks | Must run within app/OS performance budget; limited by OS APIs | Aggressive scanning can hurt UX or conflict with privacy expectations |
| Downstream | dApps / integrators using embedded MPC wallets | Smooth onboarding, minimal friction | Limited visibility into wallet’s security posture | Extra security prompts may reduce conversion for dApps |
| Downstream | Regulators & auditors | Ensure consumer asset protection & compliance | Technical expertise, evolving standards | May push for stricter rules than market is ready to adopt |
| Sideline | Law enforcement / forensics vendors | Access devices for investigations | Encrypted hardware and strong biometrics limit access | Providers aim to protect user privacy vs lawful access pressure |
| Sideline | Attackers (malware developers, fraud rings) | Monetize wallet compromises | Need scalable exploits, monetization channels | Strong hardware security + MTD increase attack cost and lower ROI |

### 3.2 Environment

- **Regulatory pressure**: As MPC wallets manage billions in consumer assets, regulators are likely to demand controls analogous to mobile banking, referencing OWASP MASVS or similar standards [Source: OWASP MASVS, OWASP, 2023].
- **Threat evolution**: Mobile malware increasingly targets crypto wallets specifically, leveraging overlays, keylogging, and clipboard hijacking [Source: 2024 Annual Mobile Threat Report, Lookout, 2024].
- **Device diversity**: Android fragmentation produces varying security baselines; not all OEMs ship StrongBox or timely security patches [Source: Android Security & Privacy Year in Review, Google, 2023, https://source.android.com/docs/security].

### 3.3 Responsibility & room

- **Wallet providers must own**:
  - App‑level controls (root/jailbreak detection, memory hygiene, backup policies, pinning, UI hardening, MTD integration).
  - Clear security posture disclosure and risk segmentation (e.g., limits for high‑risk devices).

- **OS vendors must own**:
  - Strong secure elements, attestation frameworks, and consistent APIs for keystores.

- **Users must own** (with guidance):
  - Device lock strength, update hygiene, avoidance of dangerous behaviors (rooting/jailbreaking, sideloading untrusted apps, using public WiFi without protection).

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2018–2020: Early MPC wallet experiments**
   - Focus on UX and differentiation; reliance on basic Keychain/Keystore; minimal root/jailbreak detection or pinning [Source: MPC Wallets – Stackup Guide, Stackup, 2025].

2. **2020–2022: Platform security maturation**
   - Apple hardens Secure Enclave and data‑protection classes; Android introduces and expands StrongBox; yet adoption in crypto wallets lags mainstream banking [Source: Apple Platform Security, Apple, 2022–2024; Android 9–13 security docs, Google, 2018–2023].

3. **2023–2024: Forensics and threats catching up**
   - Commercial tools add support for newer iOS/Android versions and chipsets, including full file‑system extractions under specific conditions [Source: UFED Ultimate Product Updates, Cellebrite, 2022–2024].
   - Research highlights recoverable artifacts from Web3 wallets on Android even without root in some cases [Source: Mobile Cyber Forensic Investigations of Web3 Wallets on Android, Alharbi et al., MDPI, 2022].

4. **2024–2025: Scale without proportionate hardening**
   - User counts and AUM grow rapidly; security controls evolve incrementally, leading to mismatch between risk surface and defenses.

### 4.2 Background vs. direct causes

- **Background causes**:
  - Market priority on frictionless onboarding and cross‑platform reach.
  - Underestimation of mobile forensic capabilities and malware sophistication.
  - Confusion between "cryptographic security" (MPC math) and "system security" (endpoints, OS, users).

- **Direct triggers**:
  - Practical incidents or demonstration attacks where mobile shares were exposed during forensic investigation or runtime compromise (often disclosed privately via bug bounties or research reports) [Estimate: based on pattern of mobile banking and crypto wallet disclosures].

### 4.3 Root issues

- Lack of **secure engineering culture** for mobile clients compared with backend.
- Insufficient **standardization**: few explicit industry baselines tailored to MPC wallets, beyond generic mobile app standards (e.g., MASVS).
- **Economic misalignment**: catastrophic tail risks (large multi‑user drain) are underweighted relative to short‑term growth metrics.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- **Growing AUM on mobile wallets** with similar or slower growth in endpoint security investment → increasing expected loss from combined mobile + server compromises [Estimate: extrapolation from user and AUM growth trends reported by consumer MPC providers].
- **Adversary tooling improving faster than defenses**: UFED/GrayKey roadmaps show rapid support for new devices/OS; malware authors quickly weaponize new exploits [Source: UFED Ultimate 7.27 Release Notes, Cellebrite, 2022; Source: GrayKey Product Overview, Grayshift, 2024, https://www.grayshift.com/graykey/].
- **Regulation lagging practice**: incidents may occur before clear mobile wallet security standards are codified.

### 5.2 Early signals

- Increase in mobile malware families targeting crypto wallets and exchanges as documented by major MTD vendors [Source: 2024 Annual Mobile Threat Report, Lookout, 2024].
- Growth of published forensic case studies recovering wallet artifacts on seized Android devices [Source: Alharbi et al., MDPI, 2022].
- More providers adding superficial controls (e.g., simple root checks, basic pinning) without comprehensive hardening.

### 5.3 Scenarios (6–24 months)

1. **Optimistic**
   - Industry adopts strong baselines (Secure Enclave/StrongBox, MASVS alignment, MTD integration); regulators incentivize compliance via guidance rather than punitive actions.
   - Outcome: Few major consumer incidents; MPC wallets gain reputation as safer than traditional self‑custody.

2. **Baseline**
   - Mixed adoption; several providers fully harden, others partially; one or two medium‑scale incidents involving compromised mobile shares + server breach drive late adoption.

3. **Pessimistic**
   - Major coordinated attack or forensic leak drains funds across multiple MPC wallet providers by exploiting weak endpoint security and/or misconfigured backups.
   - Result: Regulatory backlash, user trust shock, and migration to more conservative custody models.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- Many providers already employ **cryptographic experts** familiar with MPC protocols.
- Some have **DevSecOps** practices, including security reviews for backend changes and regular penetration testing.
- iOS ecosystem provides **relatively uniform, strong hardware security** when properly leveraged [Source: Apple Platform Security Guide, Apple, 2024].

### 6.2 Capability gaps

- Limited **mobile security engineering depth** (secure enclave APIs, Keychain/Keystore pitfalls, anti‑frida/anti‑debugging, obfuscation strategies).
- Insufficient **threat intelligence integration** specific to mobile malware targeting wallets.
- Lack of **red‑teaming** that includes realistic mobile compromise + forensic scenarios.

### 6.3 Buildable capabilities (1–6 months)

- Upskill existing mobile engineers on secure enclave/StrongBox patterns and MASVS requirements via focused training and playbooks.
- Partner with MTD vendors and forensic labs to design **joint test programs** and continuous validation.
- Build internal **security champions** within mobile teams to own threat modeling and secure coding standards.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline (for implementation docs)

- **Background**: 2‑of‑2 MPC wallets, mobile client role, threat landscape.
- **Problem**: Mobile endpoint compromises undermine MPC security guarantees.
- **Analysis**: Attack surfaces (storage, memory, backup, network, UI), stakeholder dynamics, capability gaps.
- **Options**: Baseline hardening package vs. risk‑tiered security vs. high‑assurance profile.
- **Risks**: UX friction, device exclusion, implementation complexity, residual threat from novel exploits.

### 7.2 Key judgments (needing validation)

1. 【P0】 Hardware‑backed secure storage + strong passcodes/biometrics are sufficient to defeat most forensic tools for practical time horizons.
2. 【P0】 Disallowing rooted/jailbroken devices for high‑value actions materially reduces real‑world compromise rates.
3. 【P1】 MTD integration significantly improves detection of malware and risky networks in this domain compared to OS‑only signals.
4. 【P1】 Risk‑tiered controls (e.g., stricter for large balances/limits) are acceptable to regulators and users if transparently communicated.
5. 【P2】 Adding a third factor (e.g., hardware security key) is justified only for top‑tier users due to complexity.

### 7.3 Alternative paths (one‑line positioning)

- **Option A – Strict baseline for all users**: Uniform strong controls, including blocking compromised devices and requiring hardware‑backed storage where available.
- **Option B – Risk‑tiered security**: Minimal baseline for all; stronger controls required as asset value, transaction volume, or risk indicators increase.
- **Option C – High‑assurance tier only**: Keep current baseline for most; offer high‑assurance mode with additional factors for security‑sensitive segments.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Security‑maximizing bias**: Overweighting worst‑case catastrophic loss vs. usability and market realities.
- **Vendor bias**: Overreliance on MTD or obfuscation vendors’ claims without independent testing.
- **Platform bias**: Assuming iOS devices are always secure enough and underestimating jailbroken or older iOS variants.

### 8.2 Required intelligence

- Empirical data on:
  - Percentage of active devices with Secure Enclave / StrongBox available *and* enabled by the wallet.
  - Incidence of rooted/jailbroken devices among active users (via telemetry and attestation).
  - Time and success rate of forensic extraction of shares under different configurations (device models, OS versions, passcode strengths).
  - Effectiveness of MTD alerts in stopping real‑world incidents (precision/recall).

### 8.3 Validation plan

- Commission **independent forensic assessments** covering representative device/OS combinations, focusing on share extractability under realistic constraints.
- Run **controlled pilots** with stricter policies (e.g., blocking rooted devices, enforcing hardware‑backed storage) for subsets of users and measure incident rates vs. churn.
- Implement **attack simulations** (tabletop + technical red‑team) combining mobile compromise and server breach to test incident playbooks.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Strength of recommended controls may be adjusted as data on user behavior, incident frequency, and forensic capabilities is gathered.
- Device eligibility policies may change as hardware security becomes more prevalent on low‑end Android.

### 9.2 Incremental approach

- Start with **non‑disruptive controls** (pinning, screenshot blocking in critical flows, backup exclusions, basic root/jailbreak detection).
- Then phase in **gating controls** (blocking rooted/jailbroken devices, requiring hardware‑backed keys for larger transactions).
- Finally, introduce **optional high‑assurance tiers** for users who opt into stronger controls.

### 9.3 "Good enough" criteria

- Verified inability to extract shares from non‑rooted, locked devices in independent tests for top N device/OS combinations.
- Demonstrated reduction in mobile endpoint–driven incidents over 12–18 months.
- Acceptable user‑level metrics (e.g., activation and retention) within agreed bounds after security changes.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. The primary risk is **mobile endpoint compromise collapsing MPC’s distributed trust model**, especially when combined with server breaches.
2. **Hardware‑backed storage, uncompromised OS state, and secure network channels** form the non‑negotiable tripod for mobile MPC client security.
3. **Backups, debugging, and UX features** (screenshots, overlays) are frequent weak points and must be explicitly controlled.
4. A **phased, risk‑tiered hardening program** aligns better with reality than a one‑size‑fits‑all approach, provided enforcement for high‑value flows is strict.

### 10.2 Near‑term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

1. **【P0】 Baseline hardening blueprint** → Security Architecture Lead → Design doc approved by cross‑functional security and product forums → 2026‑01‑31.
2. **【P0】 Implement TLS 1.3 + certificate pinning** for all MPC endpoints → Mobile & Backend Teams → % of endpoints pinned: 0% → 100% → 2026‑03‑31 [Source: MASVS-NETWORK-1, OWASP, 2023].
3. **【P0】 Root/jailbreak detection & gating for high‑risk actions** → Mobile Team → % of high‑risk flows blocked on compromised devices: 0% → ≥95% → 2026‑03‑31.
4. **【P1】 Hardware‑backed key storage rollout (iOS Secure Enclave, Android StrongBox)** → Mobile Team → % of active devices using hardware‑backed keys: baseline (TBD) → +40pp → 2026‑06‑30 [Source: Android Keystore System, Android Developers, 2024; Apple Platform Security, Apple, 2024].
5. **【P1】 Backup and screenshot policy enforcement** → Mobile Team → % of sensitive flows with screenshots disabled and backups excluded: baseline (TBD) → 100% → 2026‑06‑30 [Source: OWASP MASVS-STORAGE, 2023].
6. **【P2】 MTD integration pilot** → Security Engineering → MTD‑protected MAU: 0 → 10–20% pilot cohort; incident detection uplift measured → 2026‑09‑30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| User churn due to blocked rooted/jailbroken devices | Medium | Medium | Spike in support tickets and uninstalls after rollout | Phase‑in with communication and grace periods; provide alternatives for low‑value users | Product Lead |
| False sense of security from incomplete hardening | High | Medium | Partial implementation (e.g., pinning without proper root detection) | Explicit risk register; security sign‑off criteria before marketing claims | CISO |
| Vendor lock‑in to MTD/obfuscation tools | Medium | Medium | Single vendor used without exit plan | Multi‑vendor evaluation; avoid proprietary hooks that inhibit migration | Security Architecture |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Strict baseline for all users** | Simple mental model; easier to audit; strong protection against mobile + server compromise | Higher churn on unsupported/compromised devices; engineering cost; more support load | Market share loss on low‑end Android; potential regulatory pushback if users locked out of funds | Highly regulated markets; high average balances; limited device diversity | When targeting global retail markets with many legacy/low‑end devices |
| **B. Risk‑tiered security** | Aligns control strength with asset value; preserves UX for low‑risk users | Requires high‑quality risk telemetry and policy engine; more complex to explain | Misconfiguration could leave high‑value users under‑protected; compliance complexity | Mixed user base (retail + higher‑value); mature risk infrastructure | When org lacks telemetry or governance to manage dynamic policies |
| **C. High‑assurance tier only** | Concentrates complexity on small, high‑value group; fast time‑to‑market for rest | Leaves majority of users on weaker baseline; may create two‑class perception | Public incidents in baseline tier could still damage brand; slower migration of users to safer tier | When time‑to‑market is critical and most balances are low; used as interim strategy | As long‑term default if AUM in baseline tier keeps growing significantly |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **MPC (Multi‑Party Computation)** | Cryptographic technique enabling multiple parties to compute a function (e.g., signature) without revealing their private inputs; in wallets, used to avoid reconstructing full private keys in one place | N/A | [Source: MPC Wallets – Stackup Guide, Stackup, 2025] |
| **2‑of‑2 Threshold Scheme** | Key is split into two shares; both must participate to sign; compromise of either share alone should be insufficient | N/A | MPC wallets architecture |
| **Secure Enclave** | Hardware‑isolated coprocessor in Apple devices providing secure key storage and cryptographic operations; keys never leave the enclave | N/A | [Source: Apple Platform Security Guide, Apple, 2024] |
| **Android Keystore / StrongBox** | Android’s secure key storage, with StrongBox providing hardware‑backed keystore on supported devices | N/A | [Source: Android Keystore System, Android Developers, 2024] |
| **MTD (Mobile Threat Defense)** | Class of security solutions detecting malware, risky configurations, and network threats on mobile devices | N/A | [Source: Lookout Mobile Threat Reports, Lookout, 2024–2025] |
| **Rooting / Jailbreaking** | Gaining elevated privileges on Android (root) or iOS (jailbreak), bypassing OS security controls and app sandbox boundaries | N/A | [Source: Lookout Mobile Threat Reports, 2024–2025] |
| **Certificate Pinning** | Technique where an app validates server certificates against embedded public keys or certificates to prevent MITM, even with compromised CAs | N/A | [Source: MASVS-NETWORK-1, OWASP, 2023] |
| **Forensic Extraction Tools (UFED, GrayKey)** | Commercial tools used by law enforcement and forensic analysts to unlock devices and extract data under various conditions | N/A | [Source: UFED Product Page, Cellebrite, 2024; GrayKey Product Overview, Grayshift, 2024] |
| **MASVS (Mobile Application Security Verification Standard)** | Industry standard baseline for mobile app security requirements; includes storage, network, code, and resilience controls | N/A | [Source: OWASP MASVS v2.0.0, OWASP, 2023] |
| **Mobile Endpoint Compromise** | Situation where attacker gains sufficient control over a mobile device to bypass app security assumptions (e.g., via malware, root/jailbreak, forensic access) | N/A | Defined for this analysis |

---

## 12. References

### Tier 1 Sources (Primary: Official Docs, Standards, Peer‑Reviewed Research)

1. **Apple**. (2024). *Apple Platform Security Guide*. https://support.apple.com/guide/security/welcome/web **[Cited in: Context Recap, 2.3, 4.1, 5.1, 6.1, 10.2, 11]**
2. **Google / Android Developers**. (2024). *Android Keystore System*. https://developer.android.com/privacy-and-security/keystore **[Cited in: Context Recap, 1.2, 5.1, 10.2, 11]**
3. **Google / Android Developers**. (2018–2023). *Android 9 Features & Hardware Security Module / StrongBox*. https://developer.android.com/about/versions/pie/android-9.0 **[Cited in: Context Recap, 2.3, 4.1, 5.1]**
4. **Alharbi, A., et al.** (2022). *Mobile Cyber Forensic Investigations of Web3 Wallets on Android*. Applied Sciences (MDPI), 12(21), 11180. https://doi.org/10.3390/app122111180 **[Cited in: Context Recap, 1.1, 4.1, 5.2]**
5. **OWASP**. (2023). *Mobile Application Security Verification Standard (MASVS) v2.0.0*. https://github.com/OWASP/masvs **[Cited in: Context Recap, 1.1, 1.2, 2.2, 3.2, 10.2, 11]**

### Tier 2 Sources (Industry Reports, Technical Guides)

6. **Stackup**. (2025). *MPC Wallets: A Complete Technical Guide*. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide **[Cited in: Context Recap, 1.1, 4.1, 11]**
7. **Lookout**. (2024). *2024 Annual Mobile Threat Report*. https://www.lookout.com/threat-intelligence/report/2024-annual-mobile-threat-report **[Cited in: Context Recap, 1.1, 2.3, 3.2, 5.1, 5.2, 11]**
8. **Lookout**. (2025). *Q1 2025 Mobile Threat Landscape Report*. https://www.lookout.com/threat-intelligence/report/2025-q1-mobile-threat-landscape-report **[Cited in: Context Recap, 3.2, 5.1, 11]**
9. **Cellebrite**. (2024). *Cellebrite Inseyets Powered by UFED*. https://cellebrite.com/en/ufed/ **[Cited in: Context Recap, 2.3, 4.1, 5.1, 11]**
10. **Cellebrite**. (2023). *Extractions of iOS Devices – Mobile Device Forensics Glossary*. https://cellebrite.com/en/glossary/extractions-of-ios-devices-mobile-device-forensics/ **[Cited in: Context Recap, 2.3, 5.1]**
11. **Grayshift**. (2024). *GrayKey – Mobile Forensic Access Tool*. https://www.grayshift.com/graykey/ **[Cited in: 5.1, 11]**

### Estimates & Assumptions (Not citations)

12. **User behavior & device distribution estimates**. Method: Combined provider disclosures, public market share stats for rooted/jailbroken devices, and typical wallet demographics. Confidence: Medium. Validation: Telemetry once root/jailbreak and hardware‑capability checks are instrumented in production. **[Used in: 1.2, 2.2, 5.1, 7.2]**
13. **Incident frequency projections**. Method: Scenario analysis extrapolating from mobile banking and crypto wallet incident histories; assumes similar attacker economics. Confidence: Low‑to‑Medium. Validation: Track real incidents and near‑misses over 24 months. **[Used in: 5.1–5.3, 9.1]**
