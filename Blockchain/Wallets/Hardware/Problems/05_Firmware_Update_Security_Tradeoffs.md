# Firmware Update Security Tradeoffs

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Engineering and Security Team

## Problem Statement

1. **[Important]** Q: Hardware wallet manufacturers face critical trade-offs between updatable firmware (enables security patches but introduces attack surface for malicious updates, insider threats, and supply chain compromise) versus non-updatable firmware (eliminates update risks but leaves devices vulnerable to newly discovered exploits), impacting long-term device security and user asset protection. Formulate a structured problem statement using the following [Input] fields.
   
   A:
   - **Brief description of the problem to be analyzed**: 
     Firmware update strategy creates security trade-off: updatable firmware enables critical patches (e.g., CVE-2025-27840) but risks malicious updates from compromised infrastructure, insider attacks, social engineering; non-updatable firmware eliminates update attack surface but leaves devices permanently vulnerable to future exploits. Need to define optimal firmware update security model achieving >99.9% patch delivery integrity while maintaining <0.01% malicious update risk by Q2 2025.
   
   - **Background and current situation**: 
     Updatable firmware carries risks: malicious updates from insider attacks, social engineering, insufficient quality control, lack of independent audits per update [Web: Tangem, 2025]. Non-updatable firmware offers advantages: no risk of interference, no forced updates, one-time security audits [Web: Tangem, 2025]. Firmware updates provide security patches addressing vulnerabilities and protecting against cyber threats [Web: NinjaOne, 2025]. Ledger devices use updatable firmware to benefit from optimal security and UX [Web: Ledger Support, 2025]. ESP32 vulnerability (CVE-2025-27840) demonstrated need for update capability to patch critical flaws affecting deployed devices. Industry divided: Ledger/Trezor (updatable), Tangem (non-updatable), each with different security models.
   
   - **Goals and success criteria**: 
     Patch delivery integrity: 99% → >99.9% (target) / >99.99% (ideal); Malicious update risk: current baseline TBD → <0.01% (target) / <0.001% (ideal); Patch deployment speed: critical CVEs patched within 30 days for >90% devices (target); User update adoption: est. 40% → >70% (min) / >85% (target) / >95% (ideal); Security audit coverage: 100% updates independently audited before release (target); Rollback capability: <24h to revert compromised update (target).
   
   - **Key constraints and resources**: 
     Timeline: Q1 2025-Q2 2025 (6 months); Budget: $300K-$600K for secure update infrastructure (signing keys, audit process, rollback systems, monitoring); Team: 3-4 firmware engineers + 2 security auditors + 1 infrastructure engineer + 1 PM; Tech: secure boot chain, cryptographic signing, multi-party key management (HSM), update verification, rollback mechanisms; Security: air-gapped signing infrastructure, multi-signature approval, independent audit requirement; Regulatory: maintain security certifications (Common Criteria, FIPS) during update process.
   
   - **Stakeholders and roles**: 
     Hardware Wallet Users (10M+ globally, need security patches <30 days for critical CVEs, zero malicious update exposure), Firmware Engineers (3-4 per manufacturer, need rapid patch development, secure deployment pipeline), Security Auditors (independent firms, need 5-7 days per update review, comprehensive audit scope), Product Security Teams (need vulnerability response process, coordinated disclosure), Regulatory Bodies (certifications like Common Criteria EAL5+, need update integrity guarantees), Competitors (different firmware models: Tangem non-updatable vs. Ledger/Trezor updatable, need market differentiation).
   
   - **Time scale and impact scope**: 
     Timeline: Q1 2025-Q2 2025 (6 months for initial security model implementation); Long-term: 5-10 year device lifespan; Affected systems: firmware, bootloader, update infrastructure (signing, distribution), companion apps (update delivery); Device scope: all hardware wallets in market (new and existing 10M+ devices); Security impact: balance patching newly discovered vulnerabilities vs. preventing malicious update injection.
   
   - **Historical attempts and existing solutions (if any)**: 
     Ledger approach: updatable firmware with cryptographic signing and secure enclave [Web: Ledger Support, 2025]. Trezor approach: updatable firmware with open-source transparency and community review. Tangem approach: non-updatable firmware with one-time audit, eliminating update attack surface [Web: Tangem, 2025]. Coldcard: updatable with additional user verification (checksums, source code review). Industry incidents: 2020 Trezor firmware signing key speculation (unfounded), 2023 Ledger Recover backlash over firmware update introducing cloud backup (design controversy, not security breach). Key lessons: users distrust automatic updates, independent audits critical for trust, update rollback capability essential.
   
   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: Updatable firmware risks: insider attacks, social engineering, quality control gaps, audit limitations [Web: Tangem, 2025]; Non-updatable firmware advantages: no interference risk, no forced updates, one-time audits [Web: Tangem, 2025]; Firmware updates include security patches for vulnerabilities [Web: NinjaOne, 2025]; Ledger uses updatable firmware [Web: Ledger Support, 2025]; ESP32 CVE-2025-27840 requires firmware patch for deployed devices
     - **Assumptions**: User update adoption est. 40% (inferred from IoT/consumer electronics industry data on voluntary firmware update rates, no hardware wallet-specific statistics published); Current patch delivery integrity est. 99% (standard for consumer electronics with signing infrastructure); Malicious update risk baseline unknown (zero confirmed incidents in major manufacturers, but theoretical risk from insider threats/compromise)
     - **Uncertainties**: Optimal update frequency (quarterly, ad-hoc for CVEs, continuous) undefined; User tolerance for mandatory vs. optional updates unclear; Ideal multi-signature threshold (2-of-3, 3-of-5, 5-of-7 key holders) not validated; Independent audit turnaround time (5-7 days estimate) may delay critical patches; Cost-benefit analysis of non-updatable firmware + device replacement program vs. updatable with attack surface not quantified; Insurance/liability implications of each model not established

---

## Glossary

- **Air-Gapped Infrastructure**: Computer system physically isolated from network connections, used for highly sensitive operations like firmware signing key management.
- **Common Criteria EAL (Evaluation Assurance Level)**: International security certification standard with levels 1-7, where EAL5+ requires rigorous design verification and testing.
- **CVE (Common Vulnerabilities and Exposures)**: Standardized identifier for publicly known security vulnerabilities, enabling coordinated disclosure and patching.
- **HSM (Hardware Security Module)**: Tamper-resistant device for secure cryptographic key storage and operations, used for firmware signing keys.
- **Multi-Signature (Multi-Sig)**: Cryptographic scheme requiring M-of-N signatures to authorize operation, distributing control to prevent single point of compromise.
- **Rollback Capability**: Ability to revert device to previous firmware version if updated version contains bugs or malicious code.
- **Secure Boot Chain**: Cryptographic verification of each component in boot process (bootloader, firmware, applications) before execution, ensuring integrity.

---

## Reference

### Web Sources
- [Web: Tangem, 2025] - Updatable vs. non-updatable firmware in hardware wallets: security trade-offs (https://tangem.com/en/blog/post/updatable-vs-non-updatable-firmware-hardware-wallets)
- [Web: NinjaOne, 2025] - What is a firmware update and why is it important: security patches and vulnerability mitigation (https://www.ninjaone.com/blog/what-is-a-firmware-update)
- [Web: Ledger Support, 2025] - Ledger Device OS™ (Operating System) update guide: maintaining optimal security and UX (https://support.ledger.com/article/360013349800-zd)
- [Web: Coldcard Docs, 2025] - Upgrade firmware process and verification procedures (https://coldcard.com/docs/upgrade)
