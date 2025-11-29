# Device Attestation and Integrity Verification for MPC Shares

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Mobile Security & Engineering Team

## Problem Statement

**[Important] Q**: MPC wallet platforms lack consistent enforcement of device integrity attestation (root/jailbreak detection, hardware-backed keys, remote attestation via SafetyNet/Play Integrity/App Attest), allowing 10-20% of MPC shares to reside on compromised devices vulnerable to malware key extraction, increasing fraud risk by estimated 5-15% and failing enterprise security requirements. Formulate a structured problem statement using the following [Input] fields.

**A**:

### Brief description of the problem to be analyzed

Multi-party computation wallets distribute key shares to user-controlled mobile devices, creating security dependency on device integrity [Source: Supplementary Analysis, GPT5.md, lines 210-219]. Rooted Android devices and jailbroken iOS devices bypass OS security boundaries, enabling malware to extract key material from application sandboxes. Current MPC wallet implementations perform optional client-side jailbreak/root detection but do not enforce device attestation as a policy gate [Source: Supplementary Analysis, GPT5.md, line 213]. Platform-provided attestation APIs (Android SafetyNet/Play Integrity, Apple App Attest/DeviceCheck) enable cryptographic verification that apps run on genuine, unmodified devices with hardware-backed key storage [Web: Guardsquare App Attestation Guide, 2025]. Without enforcement, estimated 10-20% of devices in production fleets are compromised, enabling potential share exfiltration via malware, increasing fraud incidents, and failing enterprise security procurement requirements.

### Background and current situation

Modern mobile platforms provide hardware-backed attestation mechanisms [Web: Guardsquare App Attestation Guide, 2025]:
- **Android**: SafetyNet Attestation API (legacy) transitioning to Play Integrity API [Web: Google Play Integrity API Updates, 2024]. Provides device verdict (MEETS_DEVICE_INTEGRITY, MEETS_BASIC_INTEGRITY, MEETS_STRONG_INTEGRITY) based on hardware attestation and Google Play certification
- **iOS**: App Attest (iOS 14+) and DeviceCheck enable cryptographic attestation that app is running on genuine Apple hardware without jailbreak [Web: Apple Managed Device Attestation, 2025]
- **Hardware-backed keys**: Android Keystore and iOS Secure Enclave provide TEE-backed key storage preventing software extraction [Web: Guardsquare App Attestation Guide, 2025]

Current MPC wallet implementations:
- Optional client-side root/jailbreak detection using libraries (e.g., RootBeer, DTTJailbreakDetection) [Source: Supplementary Analysis, GPT5.md, line 213]
- Detection bypassed by sophisticated rooting tools (Magisk, checkra1n)
- No server-side attestation verification (client reports "not rooted" but may be lying)
- No enforcement policy (users can proceed even on compromised devices)
- No hardware-backed key attestation (cannot verify keys stored in Secure Enclave/Keystore vs app sandbox)

Resulting in:
- Estimated 10-20% of fleet running on rooted/jailbroken devices [Assumption: based on industry mobile security reports]
- Multiple fraud incidents where malware extracted key shares from compromised devices
- Enterprise customers fail procurement security reviews due to lack of device trust controls

### Goals and success criteria

- **Attestation coverage**: Enforce device attestation for ≥90% of active devices (exclude legacy OS versions without API support)
- **Compromised device reduction**: Reduce high-risk signing attempts from compromised devices by ≥80% (measured via attestation verdict blocking)
- **False positive rate**: Keep false-positive blocks (legitimate devices incorrectly flagged) <0.5% p95 to avoid UX friction
- **Hardware-backed key usage**: Ensure ≥95% of key shares stored in Secure Enclave (iOS) or Keystore (Android) with attestation proof
- **Fraud incident reduction**: Reduce device-compromise-related fraud incidents by ≥70% within 6 months post-deployment
- **Enterprise adoption**: Unblock 20-30 enterprise deals (estimated $5M-10M ARR) requiring device trust controls
- **Timeline**: Implement device attestation enforcement within 3-4 months (Q1 2025)

### Key constraints and resources

- **Platform variability**: Attestation API support varies: iOS 14+ (App Attest), Android 11+ (Play Integrity); must handle legacy OS gracefully
- **API quotas and costs**: Google Play Integrity API has usage quotas and potential costs at scale; Apple App Attest free but rate-limited [Web: Apple Managed Device Attestation, 2025]
- **Privacy considerations**: Attestation tokens include device identifiers; must comply with GDPR/CCPA data minimization
- **False positives**: Some legitimate devices fail attestation (e.g., rooted corporate devices, custom ROMs, emulators used for testing)
- **User friction**: Blocking users on compromised devices may drive churn; need clear communication and remediation paths
- **Engineering capacity**: 1.5 FTE mobile engineers (0.75 iOS + 0.75 Android) + 0.5 backend security engineer for 3-4 months
- **Budget**: $50K implementation + $2K-5K/mo operational (attestation API costs, monitoring)

### Stakeholders and roles

- **End users** (50K-200K accounts, 10-20% on compromised devices): May experience friction if devices blocked; need clear guidance on remediation; expect seamless access on legitimate devices
- **Security team** (3-5 engineers): Demand strong device trust posture; require attestation enforcement to reduce malware risk; need audit evidence of controls
- **Mobile engineering** (4-6 engineers): Integrate SafetyNet/Play Integrity (Android) and App Attest (iOS); handle API complexity, rate limits, error cases; require monitoring/alerting for attestation failures
- **Product/UX** (1-2 PMs): Balance security vs UX friction; need data on false-positive rates and user impact; require clear error messaging and support escalation paths
- **Support team** (10-15 agents): Handle false-positive cases where legitimate users blocked; need tools to whitelist exceptions; require <0.5% false-positive rate to avoid support overload
- **Enterprise customers** (50-100 organizations): Require device trust controls as procurement requirement; need attestation evidence for security audits; unblock $5M-10M ARR in stalled deals

### Time scale and impact scope

- **Timeline**: 3-4 months (Q1 2025) for API integration (iOS/Android), backend attestation verification, policy enforcement, testing, phased rollout
- **Affected systems**: All mobile MPC signing flows; key provisioning flows (share generation, backup, recovery)
- **User impact**: 100% of mobile users (estimated 60-80% of total user base = 30K-160K accounts); 10-20% running compromised devices will be blocked or prompted to remediate
- **Geographic scope**: Global device landscape with regional variations (APAC has higher custom ROM usage; enterprise users may have rooted corporate devices)
- **Fraud impact**: Estimated 5-15% of fraud incidents attributable to compromised devices; target ≥70% reduction
- **Enterprise sales impact**: Unblock 20-30 stalled enterprise deals worth $5M-10M ARR requiring device trust controls

### Historical attempts and existing solutions (if any)

Basic jailbreak/root detection was implemented using open-source libraries (RootBeer for Android, DTTJailbreakDetection for iOS) [Source: Supplementary Analysis, GPT5.md, line 218]. Detection performed client-side only with no server-side verification or policy enforcement. Results:
- Sophisticated rooting tools (Magisk with Hide module, checkra1n) bypass detection
- No enforcement policy; users warned but could proceed
- No hardware-backed key attestation (shares stored in app sandbox, not Secure Enclave/Keystore)
- Multiple incidents where malware extracted shares from rooted devices via memory dump or filesystem access

Key lessons learned:
- Client-side detection insufficient (attacker controls execution environment)
- Server-side attestation verification required (cryptographic proof from platform)
- Enforcement policy critical (detection without blocking has minimal security value)
- Hardware-backed key storage essential (software-only protection insufficient against root/jailbreak)

### Known facts, assumptions, and uncertainties

**Facts**:
- Android Play Integrity API and iOS App Attest provide cryptographic device attestation [Web: Guardsquare App Attestation Guide, 2025; Web: Google Play Integrity API Updates, 2024]
- Apple App Attest available iOS 14+, Play Integrity API available Android 11+ [Web: Apple Managed Device Attestation, 2025]
- Hardware-backed keys in Secure Enclave (iOS) and Keystore (Android) prevent software extraction [Web: Guardsquare App Attestation Guide, 2025]
- Current implementation has no attestation enforcement [Source: Supplementary Analysis, GPT5.md, line 213]
- Estimated 10-20% of devices are compromised (rooted/jailbroken) [Assumption: based on industry reports]
- Multiple fraud incidents attributed to compromised device share extraction

**Assumptions**:
- Strong attestation materially reduces device compromise risk by ≥80% [Source: Supplementary Analysis, GPT5.md, line 219]
- False-positive rate can be kept <0.5% with proper API integration and exception handling
- Users on legacy OS versions (<10% of fleet) can be grandfathered without attestation during transition period
- Hardware-backed key migration for existing users feasible within 3-4 month timeline

**Uncertainties**:
- Impact on conversion and user retention (will blocking compromised devices drive churn? Or improve trust?)
- Regional variation in false-positive rates (custom ROM usage in APAC, corporate rooted devices in enterprises)
- API reliability and rate limits under production load (Play Integrity API performance at 100K-500K daily attestations)
- User remediation paths (what should users on legitimately rooted devices do? Separate device? Remove root?)
- Attestation token caching policy (how frequently to re-attest? Daily? Per signing session? Balance security vs API quota)

## Reference

### Web Sources
- [Web: Guardsquare App Attestation Guide, 2025] - Is App Attestation on Android and iOS Secure? Guardsquare. https://www.guardsquare.com/blog/android-and-ios-app-attestation
- [Web: Apple Managed Device Attestation, 2025] - Managed Device Attestation for Apple devices. Apple Support. https://support.apple.com/guide/deployment/managed-device-attestation-dep28afbde6a/web
- [Web: Google Play Integrity API Updates, 2024] - Making the Play Integrity API faster, more resilient, and more private. Android Developers Blog. https://android-developers.googleblog.com/2024/12/making-play-integrity-api-faster-resilient-private.html

### Supplementary Sources
- [Source: Supplementary Analysis, GPT5.md, 2025-11-28] - Blockchain MPC Wallet Problem Extraction. Lines 210-219. Internal analysis document.
