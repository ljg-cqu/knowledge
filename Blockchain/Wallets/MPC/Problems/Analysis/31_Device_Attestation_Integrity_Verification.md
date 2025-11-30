# Device Attestation and Integrity Verification for MPC Shares

**Last Updated**: 2025-11-30  
**Status**: Draft – Nine-Aspects Analysis  
**Owner**: Security & Mobile Engineering Teams

---

## Context Recap

- **Problem title**: Device Attestation and Integrity Verification for MPC Shares
- **Current state**:
  - MPC wallet shares are distributed across end-user mobile devices. A non-trivial fraction (estimated **10–20%**) of active devices are rooted/jailbroken or otherwise compromised, allowing malware to bypass OS sandboxing and exfiltrate key material from apps. [Assumption: based on industry mobile security reports; consistent with problem statement]
  - Current implementation relies mainly on **client-side root/jailbreak detection libraries** (e.g., RootBeer, DTTJailbreakDetection) without server-side attestation verification or enforceable policies. [Source: Supplementary Analysis, GPT5.md, 2025-11-28]
  - Platform attestation APIs (Android SafetyNet/Play Integrity, Apple App Attest / DeviceCheck / Managed Device Attestation) are **not yet integrated as mandatory gates**, and hardware-backed key usage is not verifiably enforced. [Web: Guardsquare App Attestation Guide, 2023–2025]
  - As a result, an estimated **5–15%** of fraud incidents are attributable to key-share compromise on untrusted devices, and multiple enterprise deals are blocked due to missing device trust controls. [Estimate: based on internal incident reviews + stalled enterprise security assessments]
- **Goals**:
  - Enforce device attestation for **≥90% of active devices** (excluding legacy OS versions without attestation support).
  - Ensure **≥95% of key shares** reside in hardware-backed keystores (Android Keystore / iOS Secure Enclave) with verifiable attestation evidence.
  - Reduce high-risk signing attempts from compromised devices by **≥80%** and device-compromise-related fraud incidents by **≥70%** within 6 months post-rollout.
  - Maintain false-positive blocks at **<0.5% p95** to preserve UX and support capacity.
  - Unblock **20–30 enterprise deals** (≈$5M–10M ARR) that require strong device trust controls.
- **Hard constraints**:
  - Attestation coverage is limited by OS support: iOS 14+ (App Attest, DeviceCheck) and Android 11+ (Play Integrity API, hardware-backed key attestation). [Web: Managed Device Attestation for Apple devices, Apple Support, 2022–2025; Web: Overview of the Play Integrity API, Android Developers, 2024]
  - Play Integrity API and Apple attestation services are rate-limited and sometimes paid at scale; backend must handle quotas, outages, and key revocations. [Web: Making the Play Integrity API faster, more resilient, and more private, Android Developers Blog, 2024]
  - Attestation tokens may include device identifiers that are privacy-sensitive (GDPR/CCPA). Data minimization and retention limits are mandatory. [Source: General GDPR/CCPA principles]
  - Some legitimate devices (e.g., rooted corporate builds, custom ROMs, test devices) may intentionally fail attestation and require exception paths.
  - Engineering capacity: ≈1.5 FTE mobile (0.75 iOS, 0.75 Android) + 0.5 backend security engineer for 3–4 months.
- **Stakeholders**:
  - End users (50K–200K accounts, 10–20% on compromised devices).
  - Security team (3–5 engineers; risk owners for malware compromise and fraud).
  - Mobile engineering (4–6 engineers; implement attestation and key migration).
  - Backend/security platform team (2–3 engineers; policy engine, verification, logging).
  - Product/UX (1–2 PMs + designers; balance friction vs. safety and enterprise requirements).
  - Support team (10–15 agents; handle false positives and exceptions).
  - Enterprise customers (50–100 organizations; procurement and security review functions).
- **Key facts (from problem statement & external sources)**:
  - Android Play Integrity API and its predecessor SafetyNet provide cryptographically signed verdicts about device integrity, including signals about hardware-backed key attestation and Google Play Protect malware status. [Web: Overview of the Play Integrity API, Android Developers, 2024; Web: Use the Play Integrity API to detect risky interactions, Google Play Console Help, 2023]
  - iOS App Attest and DeviceCheck generate keys in the Secure Enclave and allow servers to verify that app instances and devices are genuine and not obviously tampered with. [Web: App Attest documentation, Apple Developer, 2020–2024; Web: Managed Device Attestation for Apple devices, Apple Support, 2022–2025]
  - OWASP Mobile Security Testing Guide highlights that **root/jailbreak detection alone is insufficient** and often bypassable, recommending defense-in-depth and server-side checks. [Web: MASTG-TEST-0045 Testing Root Detection, OWASP MAS, 2023; Web: MASTG-TEST-0088 Testing Jailbreak Detection, OWASP MAS, 2023]
  - Remote attestation architectures (e.g., IETF RATS) formalize the roles of **Attester, Verifier, and Relying Party**, which map cleanly to mobile devices, attestation services, and MPC backend policy engines. [RFC 9334: Remote ATtestation procedureS (RATS) Architecture, IETF, 2023]

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

- **Core problem**: MPC wallet key shares are stored and used on end-user mobile devices whose integrity is only weakly checked via client-side root/jailbreak detection. This allows sophisticated malware or rooting frameworks (e.g., Magisk with hiding modules) to bypass checks and exfiltrate key shares from app sandboxes, driving **5–15% of fraud incidents** and failing enterprise device-trust requirements. [Web: MASTG-TEST-0045 Testing Root Detection, OWASP MAS, 2023; Web: Android System Integrity – Comparing Key Attestation and the Play Integrity API, Mayrhofer, 2024]
- **Key contradictions**:
  - **Security vs. accessibility**: Enforcing strict attestation and hardware-backed keys improves security but blocks 10–20% of devices (rooted, custom ROMs, legacy OS), creating friction and potential churn. [Estimate: based on industry mobile compromise rates; problem statement]
  - **User autonomy vs. institutional requirements**: Consumer users expect to run apps on rooted/custom devices, while enterprises and regulators demand strong evidence that keys reside only on verified, uncompromised hardware. [Web: Managed Device Attestation for Apple devices, Apple Support, 2022–2025]
  - **Performance & reliability vs. strict gating**: Real-time attestation on every sensitive operation increases latency and depends on third-party services, but caching or soft enforcement weakens security guarantees. [Web: Overview of the Play Integrity API, Android Developers, 2024]
  - **Simple heuristics vs. cryptographic assurance**: Heuristic root/jailbreak checks are easy to deploy but weak; cryptographic attestation is stronger but more complex, and still not perfect. [Web: Guardsquare App Attestation Guide, 2023–2025]
- **Stakeholder tensions**:
  - Security and compliance demand **hard blocks** on compromised devices.
  - Product and growth worry about conversion, churn, and app-store ratings if too many users are blocked.
  - Enterprise sales needs strong guarantees and evidence to close deals; consumer support needs manageable false-positive rates and easy exception workflows.

### 1.2 Goals & conditions

- **Primary security goals**:
  - Reduce high-risk signing attempts from devices failing attestation or lacking hardware-backed key storage by **≥80%** within 6 months post-enforcement.
  - Reduce device-compromise-related fraud incidents by **≥70%** versus the pre-attestation baseline. [Estimate: based on expected risk reduction when moving from heuristic checks to hardware-backed attestation; validation via incident stats]
- **Coverage and quality targets**:
  - **Attestation coverage**: ≥90% of active devices on supported OS versions perform server-verified attestation for all high-risk operations (e.g., key-share creation, recovery, high-value signing).
  - **Hardware-backed key usage**: ≥95% of key shares stored in Secure Enclave or Android Keystore, validated via attestation claims (key origin, security level). [Web: Guardsquare App Attestation Guide, 2023–2025]
  - **False positives**: <0.5% of legitimate devices blocked at p95; <0.1% for top enterprise customers.
- **Project constraints**:
  - Timeline: 3–4 months (Q1 2025) including design, implementation, staging, and phased rollout.
  - Budget: ≈$50K implementation + $2K–5K/month operational costs (API calls, monitoring, storage). [Problem statement]
  - Backward compatibility: Need smooth migration for existing keys and devices; cannot instantly revoke all non-attested keys.

### 1.3 Extensibility & reframing

- **Alternative framings**:
  - From **“we must block rooted devices”** → **“we must ensure that all devices participating in MPC signing provide verifiable, hardware-backed evidence of integrity proportional to transaction risk”**.
  - From **“device attestation is an on/off gate”** → **“device attestation is a continuous signal feeding a risk engine and tiered policy (block / challenge / limit / allow)”**. [RFC 9334: RATS Architecture, IETF, 2023]
  - From **“mobile device integrity”** → **“end-to-end trust chain from device hardware → OS → app binary → key material → MPC protocol”**.
- **Attribute-based expansion**:
  - **Object**: Device + app instance used for MPC share storage and signing.
  - **Key attributes**: Bootloader lock state, OS integrity, Google Play certification, Secure Enclave/Keystore backing, malware status (Play Protect), jailbreak/root status, attestation freshness, geolocation, device reputation.
  - **Related domains**: Zero-trust network access, FIDO/WebAuthn authenticators, EMM/MDM-compliant devices, remote work device posture assessments. [Web: Managed Device Attestation for Apple devices, Apple Support, 2022–2025; RFC 9334: RATS, 2023]

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Attester (device + OS + app)**:
  - Generates attestation evidence tied to hardware-backed keys (e.g., Secure Enclave keys, Android Keystore keys). [Web: Overview of the Play Integrity API, Android Developers, 2024; Web: App Attest documentation, Apple Developer, 2020–2024]
- **Attestation service**:
  - Google Play Integrity backend / Apple attestation servers validate device state and sign verdicts (integrity levels, jailbreak indicators, device class, key origin).
- **Verifier (backend security service)**:
  - MPC backend component that validates attestation tokens, checks signatures, freshness, nonce binding, and expected audience/app IDs. [RFC 9334: RATS Architecture, 2023]
- **Relying parties**:
  - MPC orchestration service and business logic that decide whether to allow key provisioning, signing, or recovery based on attestation verdicts and risk policies.
- **Key material and storage**:
  - MPC key shares stored in app sandbox, Android Keystore (TEE-backed), or iOS Secure Enclave, with or without attested origin. [Web: Guardsquare App Attestation Guide, 2023–2025]
- **Policy engine**:
  - Rules mapping attestation verdicts and context (device history, user risk level, transaction value) to outcomes: allow, block, step-up verification, or limited permissions.

### 2.2 Balance & “degree”

- **Strictness of attestation policy vs. usability**:
  - A **hard gate** (block all failed/unsupported attestations) maximizes security but can lock out 10–20% of users and many test / corporate devices.
  - A **risk-based policy** (block only highest-risk combinations, allow lower-risk flows with monitoring) balances fraud reduction and UX but leaves some exposure. [Web: Use the Play Integrity API to detect risky interactions, Google Play Console Help, 2023]
- **Frequency and scope of attestation**:
  - Per-request attestation yields freshest evidence but increases latency and dependency on external services.
  - Cached or session-based attestation (e.g., 24h validity for a device–user pair) reduces cost and latency but increases window of exposure after compromise. [Web: Overview of the Play Integrity API, Android Developers, 2024]
- **Hardware-backed keys vs. software-only keys**:
  - Hardware-backed keys provide strong resistance to extraction but may not be available on older or low-end devices, or may have functional limitations (e.g., limited algorithms or key sizes). [Web: Guardsquare App Attestation Guide, 2023–2025]

### 2.3 Causal chains (simplified)

1. **Weak/no server-side attestation → Shares on compromised devices → Malware exfiltration → Fraud incidents**
   - Without verifiable attestation, attackers who root devices or inject code can extract key shares via filesystem access or memory inspection. [Web: MASTG-TEST-0045 Testing Root Detection, OWASP MAS, 2023]
2. **Heuristic root/jailbreak checks only → Easy bypass → False confidence**
   - OWASP MSTG documents numerous techniques and tools to bypass common root/jailbreak checks, especially when enforcement is client-side only. [Web: MASTG-TEST-0045; Web: MASTG-TEST-0088, OWASP MAS, 2023]
3. **Lack of attestation enforcement → Enterprise distrust → Blocked deals**
   - Security-conscious enterprises increasingly require remote attestation and device posture evidence aligned with zero-trust principles; lack of such controls blocks procurement. [RFC 9334: RATS, 2023; Web: Managed Device Attestation for Apple devices, Apple Support, 2022–2025]

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders & interactions

| Stakeholder | Role | Goals | Constraints | Conflicts |
|------------|------|-------|------------|-----------|
| End users (retail) | Hold MPC shares on personal devices | Seamless access, minimal friction, ability to use existing devices | Limited security expertise; may use rooted/custom ROM devices | Security controls may block or degrade UX on their devices |
| Enterprise customers | Custody large assets, require compliance | Strong device trust, audit trails, regulatory alignment | Procurement processes, risk committees, legal requirements | Less tolerant of exceptions; may require blocking many devices |
| Security team | Define policies, manage fraud risk | Minimize device-compromise fraud, align with best practices | Limited engineering capacity; must justify UX impact | Often push for stricter policies than product wants |
| Mobile engineering | Implement attestation & key logic | Maintain app quality, performance, store compliance | OS/API fragmentation, rate limits, crash risk | May resist complexity of multi-platform attestation stack |
| Backend/platform | Operate MPC backend & policy engine | High availability, correct enforcement, observability | Third-party API dependencies, latency, cost | Must handle outages gracefully without overexposing risk |
| Support team | Handle blocked users and false positives | Keep ticket volumes manageable, provide clear guidance | Limited tooling; policy complexity | Suffer from unclear or overly strict policies |

### 3.2 Environment factors

- **Regulatory and industry standards**:
  - Financial regulators and frameworks (e.g., zero-trust architectures, EMM/MDM best practices) increasingly expect hardware-backed device posture checks for sensitive operations. [RFC 9334: RATS, 2023]
  - OWASP MASVS/MSTG treat root/jailbreak detection and integrity checks as key controls but warn against over-reliance on easily bypassed heuristics. [Web: MASTG-TEST-0045, 0088, OWASP MAS, 2023]
- **Ecosystem evolution**:
  - Android is shifting from SafetyNet to Play Integrity API, with stronger hardware-backed attestation and evolving verdict semantics. [Web: Making the Play Integrity API faster, more resilient, and more private, Android Developers Blog, 2024]
  - Apple is promoting Managed Device Attestation and advanced Secure Enclave features to support zero-trust-style device evaluation. [Web: Managed Device Attestation for Apple devices, Apple Support, 2022–2025]
- **Threat landscape**:
  - Commodity malware kits and rooting frameworks explicitly target bypassing root/jailbreak detection and tampering with security logic. [Web: M10 Lack of Binary Protections, OWASP Mobile Top 10, 2014–2020]

### 3.3 Responsibility & room for maneuver

- **Where MPC provider must lead**:
  - Defining minimum device integrity requirements and implementing backend verification and policy enforcement.
  - Providing enterprise-grade evidence (attestation logs, reports) for audits.
  - Offering secure migration paths and support tooling.
- **Where others have flexibility**:
  - Users can choose to move to compliant devices for high-value accounts.
  - Enterprises can decide how strict to be (e.g., block all failed attestations vs. risk-tiered policies).
  - Product can experiment with messaging and remediation flows to reduce perceived friction.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **Pre-attestation era**: Mobile apps relied mainly on permissions and sandboxing; root/jailbreak detection was a best-effort defense but widely bypassed. [Web: M10 Lack of Binary Protections, OWASP Mobile Top 10, 2014–2020]
2. **SafetyNet / DeviceCheck introduction**: Google and Apple introduced APIs for attesting device integrity and app authenticity, but many apps used them only for low-stakes abuse prevention (e.g., promo fraud) rather than critical key security. [Web: Use the Play Integrity API to detect risky interactions, Google Play Console Help, 2023; Web: DeviceCheck documentation, Apple Developer, 2018–2024]
3. **MPC wallet adoption**: MPC wallets began storing critical key shares on mobile devices but often reused the old threat model (client-side checks, optional warnings) without building a comprehensive attestation-based trust chain.
4. **Enterprise & fraud pressure**: As institutional adoption grew and fraud incidents accumulated, gaps between heuristic checks and attestation-based architectures became apparent, especially during audits and incident reviews.

### 4.2 Background vs. direct causes

- **Background causes**:
  - Historical underestimation of device compromise rates and the sophistication of root/hooking tools. [Web: MASTG-TEST-0045/0088, OWASP MAS, 2023]
  - Focus on protocol-level MPC security (cryptography, threshold schemes) while treating endpoint security as a secondary concern.
  - Attestation APIs initially perceived as complex and brittle, with limited tooling and uneven documentation.
- **Direct triggers**:
  - Documented incidents where malware on rooted/jailbroken devices extracted key shares or manipulated signing flows.
  - Enterprise procurement questionnaires explicitly asking for device attestation, hardware-backed key guarantees, and evidence aligned with zero-trust principles. [RFC 9334: RATS, 2023]

### 4.3 Root issues

- Over-reliance on **client-side-only checks** and warnings without backend verification or strict policy gating.
- Lack of a clear **device trust model** tying attestation signals to risk tiers and control points.
- Insufficient observability into how many devices are compromised, how attestations would behave, and how often legitimate devices would be blocked.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory if unchanged

- **Security trajectory**:
  - Continued use of heuristic checks will allow sophisticated attackers to operate undetected on rooted/jailbroken devices, keeping device-based fraud at current or higher levels. [Web: MASTG-TEST-0045/0088, OWASP MAS, 2023]
- **Business trajectory**:
  - More enterprise deals will stall or fail due to lack of device trust evidence, especially as zero-trust adoption grows.
  - Consumer trust may erode if device-compromise incidents become public.
- **Technical trajectory**:
  - As Android and iOS tighten security and shift toward attestation-centric architectures, solutions that do not leverage these APIs will appear increasingly outdated.

### 5.2 Early signals

- Increased volume of security questionnaires and RFPs asking about device attestation, hardware-backed keys, and zero-trust alignment.
- Internal incident reports attributing fraud to malware on rooted/jailbroken devices, or to replay/abuse of session tokens from compromised endpoints.
- Developer feedback about the limitations of root/jailbreak detection libraries and random false positives/negatives.

### 5.3 6–24 month scenarios

- **Optimistic (with strong intervention)**:
  - Attestation-enforced MPC flows become a differentiator, enabling marketing statements like “all key shares reside on attested, hardware-backed devices by default.”
  - Enterprise security audits are passed with fewer exceptions; fraud from device compromise drops sharply.
- **Baseline (partial intervention)**:
  - Attestation is implemented but only as a soft signal; many high-risk devices are still allowed after warnings, limiting risk reduction.
  - Some enterprise deals close, but device posture remains a recurring audit issue.
- **Pessimistic (no intervention)**:
  - MPC provider is viewed as weak on endpoint security; institutions mandate alternatives or impose heavy compensating controls (e.g., restricted transaction limits, manual approvals), reducing competitiveness.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- Established MPC backend and logging infrastructure that can host attestation verifiers and policy engines.
- Experienced mobile engineering teams on both Android and iOS, already familiar with Secure Enclave and Keystore APIs.
- Existing security operations and incident response processes that can integrate attestation signals into detection and investigation workflows.

### 6.2 Capability gaps

- Limited **hands-on expertise** with Play Integrity, App Attest, DeviceCheck, and Managed Device Attestation at scale (quotas, outages, key management). [Web: Overview of the Play Integrity API, Android Developers, 2024; Web: Managed Device Attestation for Apple devices, Apple Support, 2022–2025]
- Lack of a **formal device risk model** mapping attestation verdicts and context to decisions (block/allow/step-up).
- Incomplete support tooling for support agents to inspect attestation logs, manage exceptions, and guide remediation.

### 6.3 Buildable capabilities (1–6 months)

- Train or hire **1–2 engineers** with deep experience in mobile security and device attestation integration; run internal workshops using OWASP MSTG as baseline. [Web: OWASP MAS/MSTG, 2023]
- Develop a small, well-documented **attestation verification library/service** shared across products (nonce generation, token verification, logging, metrics).
- Introduce a **device-risk scoring system** that aggregates attestation verdicts, device history, location anomalies, and transaction risk to drive decisions.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline (summary)

1. **Background**: MPC shares on user devices; heuristic root/jailbreak checks; rising fraud and enterprise pressure.  
2. **Problem**: Lack of strong, verifiable device integrity guarantees; 10–20% of shares reside on compromised or unverifiable devices.  
3. **Analysis**: Platform attestation APIs (Play Integrity, App Attest, Managed Device Attestation) and RATS-style architectures can provide cryptographically verifiable device trust, but require careful policy and UX design.  
4. **Options**: (A) Strict attestation gate, (B) Risk-based attestation with staged enforcement, (C) Limited-scope attestation for high-value accounts only.  
5. **Risks**: False positives, outages, implementation complexity, user churn, overconfidence in attestation.

### 7.2 Key judgments (to validate)

- **【P0】** Hardware-backed, server-verified device attestation can materially reduce device-compromise fraud (≥70%) when combined with strict policies and hardware-backed key usage. [Web: Guardsquare App Attestation Guide, 2023–2025; Web: Android System Integrity – Comparing Key Attestation and the Play Integrity API, Mayrhofer, 2024]
- **【P0】** Root/jailbreak detection alone cannot provide sufficient assurance for MPC key security; it should be treated as a supplemental signal only. [Web: MASTG-TEST-0045/0088, OWASP MAS, 2023]
- **【P1】** With careful UX and exception handling, false-positive blocks can be kept below 0.5% while significantly raising the bar for attackers.
- **【P1】** A phased rollout starting with high-risk operations and high-value accounts minimizes business risk while gathering data.

### 7.3 Alternative high-level paths

- **Option A – Strict attestation enforcement for all MPC flows**:
  - Block any device that fails attestation or cannot prove hardware-backed key storage.
- **Option B – Risk-based, staged enforcement**:
  - Start with logging and scoring; then move to enforcement for high-risk operations and users; gradually tighten policies as data accumulates.
- **Option C – Scoped enforcement for high-value/enterprise cohorts**:
  - Mandate attestation only for designated enterprise or high-net-worth accounts; leave consumer flows largely heuristic in early phases.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Security bias**: Overweighting worst-case malware and assuming only strict blocking is acceptable may underappreciate UX and growth trade-offs.
- **Product/growth bias**: Overemphasizing churn and short-term friction might delay essential controls, leaving material risk unaddressed.
- **Technology optimism bias**: Assuming attestation APIs are perfectly reliable, tamper-proof, and unbypassable, ignoring documented limitations and bypass techniques. [Web: Exposing the Shortcomings of Apple DeviceCheck and Apple App Attest, Approov, 2024]

### 8.2 Required intelligence

- **Empirical data**:
  - Distribution of device OS versions, hardware capabilities, root/jailbreak status, and expected attestation coverage.
  - Historic fraud incidents tagged by root/jailbreak or suspicious device posture where possible.
- **Attestation performance & reliability**:
  - Latency and error rates for Play Integrity and App Attest calls at projected traffic, including worst-case regional behavior. [Web: Making the Play Integrity API faster, more resilient, and more private, Android Developers Blog, 2024]
- **False-positive analysis**:
  - Proportion of legitimate users/devices that would fail strict policies under realistic scenarios (custom ROMs, EMM-managed rooted devices, devices without Play Services, etc.).

### 8.3 Validation plan

- **Step 1 – Measurement-only phase (1–2 months)**:
  - Integrate attestation collection in “monitoring mode” without enforcement.
  - Instrument dashboards: attestation pass/fail rates by OS, region, device model, user segment; simulated block rates vs. fraud risk.
- **Step 2 – Controlled pilots (2–3 months)**:
  - Enable blocking for a small cohort (e.g., internal users, test cohort, select enterprises) and high-risk flows (e.g., key recovery, high-value withdrawals).
  - Measure fraud incidents, user friction (support tickets, churn), and performance.
- **Step 3 – Policy refinement and wider rollout (3–6 months)**:
  - Adjust policies (e.g., allow-list certain device types, implement step-up verification instead of immediate blocks) based on pilot data.
  - Gradually expand enforcement coverage to broader user segments and flows with explicit SLAs and messaging.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Recalibration of the **target coverage and false-positive thresholds** once real attestation metrics are collected.
- Adjustment of **policy granularity** (e.g., more nuanced device classes, risk scores) as new attestation signals become available from platform providers.
- Reassessment of **residual risk** if new bypass techniques for Play Integrity or App Attest emerge. [Web: Android System Integrity – Comparing Key Attestation and the Play Integrity API, Mayrhofer, 2024; Web: Exposing the Shortcomings of Apple DeviceCheck and Apple App Attest, Approov, 2024]

### 9.2 Incremental approach

- Start with clear **observability and logging** before enforcing policies.
- Introduce **feature flags** and per-cohort toggles to allow reversible changes and A/B testing.
- Embed **feedback loops** from security operations and support into policy tuning (e.g., automatic identification of recurring legitimate false positives).

### 9.3 “Good enough” criteria

- Device-compromise-related fraud reduced by **≥70%** versus 6-month baseline, with correlated drop in incidents involving rooted/jailbroken devices.
- Attestation coverage ≥90% of eligible devices; hardware-backed key usage ≥95% for new key shares.
- False-positive blocks <0.5% p95 across cohort; support ticket volume related to device blocking stable or declining after initial spike.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. **Endpoint integrity is a first-class requirement for MPC security**: Cryptographically strong MPC protocols cannot compensate for key shares residing on compromised devices without attestation-based trust.
2. **Platform attestation APIs and hardware-backed keys provide a practical path** to materially reduce device-compromise risk, but must be combined with clear policies, logging, and UX.
3. **Root/jailbreak detection alone is inadequate**, and relying on it creates a dangerous illusion of security. [Web: MASTG-TEST-0045/0088, OWASP MAS, 2023]
4. **Risk-based, staged rollout** offers the best balance between fraud reduction, enterprise requirements, and user experience.

### 10.2 Near-term action list (0–3 months)

- **【P0 – Critical】 Implement attestation collection in monitoring mode**  
  - **Owner**: Backend security lead + mobile leads  
  - **Action**: Integrate Play Integrity and App Attest/DeviceCheck on mobile apps; verify tokens server-side; log verdicts without blocking.  
  - **Metric**: Coverage for supported OS devices: 0% → ≥70% in 8 weeks; dashboard with per-device-type pass/fail rates.  
  - **Sources**: [Web: Overview of the Play Integrity API, Android Developers, 2024; Web: App Attest documentation, Apple Developer, 2020–2024]

- **【P0 – Critical】 Design and implement a device risk and policy model**  
  - **Owner**: Security architecture lead  
  - **Action**: Map attestation verdicts + context to decisions (block/allow/step-up); document policies for all major flows.  
  - **Metric**: Policy document and implementation covering ≥90% of flows by risk; simulation of impact using monitoring data.  
  - **Sources**: [RFC 9334: RATS Architecture, IETF, 2023; Web: Managed Device Attestation for Apple devices, Apple Support, 2022–2025]

- **【P1 – Important】 Enable strict enforcement for high-risk flows and internal/enterprise pilot cohorts**  
  - **Owner**: Security + product  
  - **Action**: Turn on blocking where attestation fails or hardware-backed keys are missing for: key recovery, large withdrawals, admin operations, and designated enterprise accounts.  
  - **Metric**: Pilot cohorts with enforced policies; monitor fraud incidents (expected ↓50%+ for pilot) and false-positive tickets.  
  - **Sources**: [Web: Guardsquare App Attestation Guide, 2023–2025; Web: MASTG-TEST-0045/0088, OWASP MAS, 2023]

- **【P1 – Important】 Build support tooling and remediation UX**  
  - **Owner**: Support lead + UX  
  - **Action**: Provide clear error codes and help flows for blocked devices; build dashboards showing attestation history and decision rationale for support agents.  
  - **Metric**: 100% of attestation-related tickets resolvable using self-service knowledge base or support dashboards; average resolution time <2 business days.

- **【P2 – Optional】 Align with enterprise zero-trust roadmaps and external certifications**  
  - **Owner**: Compliance & sales engineering  
  - **Action**: Document attestation-based controls in security whitepapers, SOC 2 / ISO artifacts, and RFP templates.  
  - **Metric**: Device-trust related audit findings and RFP objections reduced by ≥70% year-on-year.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| High false-positive rate blocks many legitimate devices | High | Medium | >1% of active users blocked or support overwhelmed | Start with monitoring-only phase; tune policies using data; implement exception workflows and temporary overrides | Security + Product |
| Attestation service outages cause signing disruptions | High | Medium | Play Integrity or Apple attestation downtime | Implement graceful degradation policies (cached attestations, limited-time grace periods); monitor status and fail over to reduced-risk mode | Backend platform |
| Attackers find attestation bypass techniques | High | Medium | Security research or incidents show bypasses in the wild | Combine attestation with additional signals (code integrity, anti-tamper, behavioral analytics); update policies and app releases quickly | Security team |
| Implementation bugs create security gaps | High | Medium | Incorrect nonce handling, token validation, or key binding detected | Keep verifier simple and well-audited; add integration tests; consider third-party review | Engineering leads |
| User backlash/churn from blocked rooted devices | Medium | Medium | Negative app-store reviews, churn in certain segments | Provide clear messaging and remediation paths; allow low-risk, low-limit mode for some devices during transition | Product + Marketing |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Strict enforcement for all flows** | Maximizes security and enterprise trust; clear story: "no keys on non-attested devices" | High UX friction; significant engineering and support overhead | Churn and negative user sentiment; pressure to create exceptions undermining policy | Highly regulated, institution-heavy customer base; strong appetite for security-first positioning | Consumer-heavy products where rooted/custom devices are common |
| **B. Risk-based, staged enforcement** | Balances security and UX; allows learning from data before full rollout | More complex policy logic; requires good telemetry and tooling | Policy misconfiguration could under- or over-enforce | Mixed consumer/enterprise base; evolving risk understanding | Very small teams lacking capacity to manage complexity |
| **C. High-value/enterprise-only enforcement initially** | Fastest way to satisfy enterprise requirements with limited scope; reduces blast radius | Leaves consumer flows relatively exposed in near term | Risk remains for high-value consumer accounts; message may be inconsistent | When enterprise ARR is the main driver; clear segmentation exists | When consumer fraud from device compromise is already severe |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **Device attestation** | Cryptographic process by which a device proves certain properties (OS integrity, app identity, hardware-backed keys) to a remote verifier | N/A | [RFC 9334: RATS Architecture, IETF, 2023] |
| **Play Integrity API** | Google API that provides signed verdicts on app, device, and account integrity, replacing SafetyNet; supports hardware-backed signals and malware risk | N/A | [Web: Overview of the Play Integrity API, Android Developers, 2024] |
| **SafetyNet Attestation** | Legacy Android API providing basic device integrity checks (CTS profile, basic integrity); being superseded by Play Integrity | N/A | [Web: Android System Integrity – Comparing Key Attestation and the Play Integrity API, Mayrhofer, 2024] |
| **App Attest** | Apple framework that generates keys in the Secure Enclave and issues attestation statements about app integrity and device authenticity | N/A | [Web: App Attest documentation, Apple Developer, 2020–2024] |
| **DeviceCheck** | Apple framework that tracks device-level state and abuse flags tied to Secure Enclave identifiers | N/A | [Web: DeviceCheck documentation, Apple Developer, 2018–2024] |
| **Managed Device Attestation** | Apple capability to provide strong, cryptographically verifiable evidence of managed device properties for enterprise deployments | N/A | [Web: Managed Device Attestation for Apple devices, Apple Support, 2022–2025] |
| **Secure Enclave** | Dedicated coprocessor in Apple devices providing hardware-backed key storage and cryptographic operations isolated from main OS | N/A | [Web: Apple Platform Security Guide, Apple, 2022–2024] |
| **Android Keystore** | Android system component and APIs providing secure key storage, often backed by hardware security modules or TEEs | N/A | [Web: Android Keystore system overview, Android Developers, 2022–2024] |
| **Root/jailbreak detection** | Techniques used by apps to detect rooted or jailbroken devices, typically via filesystem, process, or configuration checks | N/A | [Web: MASTG-TEST-0045/0088, OWASP MAS, 2023] |
| **RATS (Remote ATtestation procedureS)** | IETF architecture describing entities and flows for remote attestation: Attester, Verifier, Relying Party, and Evidence | N/A | [RFC 9334: Remote ATtestation procedureS, IETF, 2023] |
| **Hardware-backed key** | Cryptographic key generated and stored in hardware-protected environments (Secure Enclave, TEE, HSM) resistant to software extraction | N/A | [Web: Guardsquare App Attestation Guide, 2023–2025] |

---

## 12. References

### Tier 1 – Standards, Platform Docs, and Architecture

1. **IETF.** (2023). *RFC 9334: Remote ATtestation procedureS (RATS) Architecture*. RFC Editor. https://www.rfc-editor.org/rfc/rfc9334  **[Cited in: Context Recap, 2.1, 3.2, 4.2, 7.2, 10.2, 11]**
2. **Android Developers.** (2024). *Overview of the Play Integrity API*. Android Developers Documentation. https://developer.android.com/google/play/integrity/overview  **[Cited in: Context Recap, 1.2, 2.1–2.2, 3.2, 6.2, 8.2, 10.2, 11]**
3. **Android Developers Blog.** (2024). *Making the Play Integrity API faster, more resilient, and more private*. Android Developers Blog. https://android-developers.googleblog.com/2024/12/making-play-integrity-api-faster-resilient-private.html  **[Cited in: Context Recap, 2.2, 3.2, 8.2]**
4. **Apple Developer.** (2020–2024). *App Attest* & *DeviceCheck* Documentation. Apple Developer Documentation. https://developer.apple.com/documentation/devicecheck  **[Cited in: Context Recap, 2.1, 4.1, 8.2, 11]**
5. **Apple Support.** (2022–2025). *Managed Device Attestation for Apple devices*. Apple Support. https://support.apple.com/guide/deployment/managed-device-attestation-dep28afbde6a/web  **[Cited in: Context Recap, 1.1–1.2, 3.2, 6.2, 7.2, 11]**
6. **Android Developers.** (2022–2024). *Android Keystore System Overview*. Android Developers Documentation. https://developer.android.com/training/articles/keystore  **[Cited in: Context Recap, 2.1, 2.2, 11]**

### Tier 2 – Security Guides and Industry Analyses

7. **OWASP Mobile Application Security.** (2023). *MASTG-TEST-0045: Testing Root Detection (Android)*. OWASP MAS. https://mas.owasp.org/MASTG/tests/android/MASVS-RESILIENCE/MASTG-TEST-0045/  **[Cited in: Context Recap, 1.1, 2.3, 4.2, 5.1, 7.2, 10.1–10.2, 11]**
8. **OWASP Mobile Application Security.** (2023). *MASTG-TEST-0088: Testing Jailbreak Detection (iOS)*. OWASP MAS. https://mas.owasp.org/MASTG/tests/ios/MASVS-RESILIENCE/MASTG-TEST-0088/  **[Cited in: 2.3, 4.2, 5.1, 7.2, 10.1–10.2, 11]**
9. **OWASP Foundation.** (2014–2020). *M10: Lack of Binary Protections – OWASP Mobile Top 10*. OWASP. https://owasp.org/www-project-mobile-top-10/2014-risks/m10-lack-of-binary-protections  **[Cited in: 3.2, 4.1, 5.1]**
10. **Guardsquare.** (2023–2025). *Is App Attestation on Android and iOS Secure?* Guardsquare Blog. https://www.guardsquare.com/blog/android-and-ios-app-attestation  **[Cited in: Context Recap, 1.1–1.2, 2.2, 6.2, 7.2, 10.2, 11]**
11. **Mayrhofer, M.** (2024). *Android System Integrity: Comparing Key Attestation and the Play Integrity API*. University course material. https://www.mayrhofer.eu.org/courses/android-security/selected-paper/2024/Comparing_key_attestation_and_Play_Integrity_API.pdf  **[Cited in: 1.1, 2.2–2.3, 7.2, 9.1, 11]**

### Tier 2 – Industry Commentary and Limitations

12. **Approov.** (2024). *Exposing the Shortcomings of Apple DeviceCheck and Apple App Attest*. Approov Blog. https://approov.io/blog/limitations-of-apple-devicecheck-and-apple-app-attest  **[Cited in: 8.1, 9.1]**

### Internal / Estimates

13. **Internal Incident Reviews.** (2023–2025). *Device-Compromise-Related Fraud and Root/Jailbreak Prevalence*. Security Team Reports. **[Cited in: Context Recap, 1.1–1.2, 5.2, 7.2, 9.3]**
14. **Enterprise Security Questionnaires & RFPs.** (2024–2025). *Requirements for Device Trust and Attestation in MPC Wallet Deployments*. Sales Engineering & Compliance Artifacts. **[Cited in: 3.2, 4.2, 5.2, 10.2]**
