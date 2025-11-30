# Backend Server Infrastructure Operational Security Bypassing MPC Protection – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Infrastructure Security & Operations Team

---

## Pre-Section: Context Recap

- **Problem title**: Backend server infrastructure operational security weaknesses allowing attackers to bypass MPC wallet protections and steal assets.
- **Current state**:
  - Centralized exchanges and MPC wallet providers have deployed cryptographically strong MPC key management (e.g., threshold ECDSA with distributed key shares), but backend infrastructure (application servers, hot wallet logic, internal networks, access systems, employee endpoints, third-party software) often remains only partially hardened [Source: Build secure multi-party computation (MPC) wallets using AWS Nitro Enclaves, AWS, 2024, Architecture Overview; Security - Coinbase Developer Documentation, Coinbase, 2024].
  - July 2025 incidents showed that compromising backend servers or supply-chain components can fully bypass MPC protections: CoinDCX lost ~$44M via a "server breach" tied to compromised employee workstation access, and BigONE lost ~$27M after attackers manipulated hot wallet logic through third-party software [Source: Explained: The CoinDCX Hack (July 2025), Halborn, 2025; CoinDCX CEO blames 'server breach' for $44 million exploit, The Block, 2025; Real-time lessons from BigONE Exchange $27M supply chain attack, Guardrail, 2025].
  - Blockaid’s analysis (reported by The Defiant) indicates that about 65% of Q2 2024 crypto losses (~$500M of $770M) were due to centralized infrastructure compromises rather than on-chain protocol bugs, confirming a structural shift in attack focus [Source: "MPC Alone Can't Stop Multi-Million Dollar Exchange Hacks, Experts Warn", The Defiant, 2025].
- **Pain points**:
  - Cryptographic MPC controls protect cold storage keys, but hot wallet infrastructure, orchestration servers, and operational tooling remain single points of failure: once compromised, attackers can trigger withdrawals, alter business logic, or abuse internal APIs without defeating MPC itself [Source: Build secure multi-party computation (MPC) wallets using AWS Nitro Enclaves, AWS, 2024; Enterprise Crypto OpSec Guide: Secure Digital Assets 2025, ThreeSigma, 2025].
  - Server hardening and patch management are inconsistent: many production servers still run with default configurations, delayed security updates, overly permissive firewall rules, and broad administrative privileges, giving attackers wide lateral movement after initial foothold [Source: MCP Server Hardening: Best Practices and Tips, ProtocolGuard, 2024; CIS Benchmarks, Center for Internet Security, current].
  - Access controls are fragmented: weak MFA coverage, shared admin accounts, insufficient privileged access management (PAM), and flat internal networks allow phishing or credential theft to escalate into full infrastructure compromise [Source: Enterprise Crypto OpSec Guide: Secure Digital Assets 2025, ThreeSigma, 2025; Crypto Security: Best Practices To Protect Digital Assets, Trakx, 2025].
  - Supply chain and third-party risk remain under-managed: monitoring agents, deployment tools, and vendor libraries may run with high privileges in production, but formal SBOMs, dependency scanning, and vendor security reviews are still rare in many exchanges [Source: Real-time lessons from BigONE Exchange $27M supply chain attack, Guardrail, 2025; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
- **Goals**:
  - Reduce major backend-infrastructure-driven theft incidents affecting exchanges and MPC wallet providers from an estimated 10–15 per year to <3/year (minimum), <1/year (target), ideally 0/year by Q4 2026 [Source: Problem statement – Goals and success criteria, Backend Server Infrastructure Operational Security Bypassing MPC Protection, 2025].
  - Cut infrastructure-driven annual losses from an estimated $500M/year (based on $500M of $770M Q2 2024 annualized) to <$100M/year (minimum), <$50M/year (target), ideally <$10M/year by Q4 2026 [Source: "MPC Alone Can't Stop Multi-Million Dollar Exchange Hacks", The Defiant, 2025].
  - Achieve near-universal server hardening (CIS Benchmarks level 1 baseline, automated configuration management, continuous vulnerability scanning, <7-day patch SLA for critical issues) for 100% of production servers by Q2 2026 [Source: CIS Benchmarks, Center for Internet Security; MCP Server Hardening: Best Practices and Tips, ProtocolGuard, 2024].
  - Implement zero-trust and strong privileged access management (MFA with hardware tokens, just-in-time access, session recording, quarterly reviews) across 100% of privileged access paths by Q3 2026 [Source: Enterprise Crypto OpSec Guide: Secure Digital Assets 2025, ThreeSigma, 2025].
  - Build effective supply chain, monitoring, and training programs plus SOC 2 Type II coverage for key custody infrastructure by 2026–2027 [Source: SOC 2 Type 1: Our commitment to secure Web3 infrastructure, Chainstack, 2024; Quick Guide: SOC 2 Compliance Requirements, Onspring, 2024].
- **Hard constraints**:
  - 24-month main program window (Q1 2026–Q4 2027), with an accelerated 12‑month track (to Q4 2026) for highest-risk components such as hot wallets and signing orchestration [Source: Problem statement – Key constraints and resources].
  - Budget per major provider in the range of $2M–$8M covering server hardening, PAM and identity, supply chain tooling, SIEM/behavioral analytics, training, and compliance/audit costs; many mid-tier exchanges have very limited security budgets [Source: Problem statement – Key constraints and resources; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
  - Need to maintain high availability (often ≥99.9–99.99% uptime) while introducing stricter security controls; disruptive re-architecture or prolonged downtime is not acceptable for trading platforms [Source: Security - Coinbase Developer Documentation, Coinbase, 2024; Web3 infrastructure SLAs from major providers, various].
  - Regulatory, legal, and customer commitments (e.g., SOC 2, licensing) limit how aggressively providers can change custody workflows without clear justifications and evidence [Source: Blockchain Compliance Audits & Regulatory Fines 2025: Complete Guide, Compliancehub.wiki, 2025; SOC 2 Type 1: Our commitment to secure Web3 infrastructure, Chainstack, 2024].
- **Key facts**:
  - CoinDCX incident combined a targeted phishing / malware campaign on an engineer’s workstation with subsequent server-level compromise; the company publicly described it as a "server breach" and committed to covering the $44M loss for users [Source: CoinDCX CEO blames 'server breach' for $44 million exploit, The Block, 2025; CoinDCX Suffers $44M Hack, Ampcus Cyber, 2025].
  - BigONE’s $27M loss was caused by a supply chain attack that compromised third-party software used in hot wallet infrastructure, allowing attackers to inject malicious withdrawal logic that evaded traditional controls [Source: Real-time lessons from BigONE Exchange $27M supply chain attack, Guardrail, 2025; Supply Chain Attacks in Crypto: BigONE Breach and North Korean Threats Shake Industry, OKX Learn, 2025].
  - July 2025 saw over $139M in losses across five major crypto hacks, with CoinDCX and BigONE among the largest cases, reinforcing that infrastructure security—not smart contract bugs—is the dominant failure mode for exchanges [Source: "$139M Gone: The 5 Most Devastating Crypto Hacks of July 2025", Coinmonks, 2025; 2025 Crypto Crime Report, TRM Labs, 2025].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

1. **Core problem**  
   Even when MPC-based key management is correctly implemented, backend server infrastructure, internal access systems, and operational workflows can be compromised, allowing attackers to bypass distributed cryptographic controls and trigger unauthorized withdrawals, configuration changes, or business-logic manipulation without directly breaking MPC [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS, 2024; Enterprise Crypto OpSec Guide: Secure Digital Assets 2025, ThreeSigma, 2025].

2. **Key contradictions**
   - **Cryptographic strength vs. operational weakness**: Providers invest heavily in MPC protocols, HSMs, and key ceremony rigor, but run critical MPC components on cloud VMs or containers with default OS hardening, broad admin rights, and limited network segmentation, making compromise of a single backend node sufficient to subvert the system [Source: MCP Server Hardening: Best Practices and Tips, ProtocolGuard, 2024; CIS Benchmarks, Center for Internet Security].
   - **Security vs. operational convenience**: Operations and engineering teams often favor password- or VPN-based access, shared accounts, and relaxed change windows to keep incident response and deployments fast, directly conflicting with zero-trust, least privilege, and strong-pam principles [Source: Crypto Security: Best Practices To Protect Digital Assets, Trakx, 2025; Secure Cryptocurrency Assets in 2025: Complete Guide, 3Commas, 2025].
   - **Third-party efficiency vs. supply chain risk**: Monitoring agents, CI/CD tooling, and vendor SDKs accelerate delivery and observability but run with broad permissions; insufficient vetting, SBOM management, or update validation creates a single compromised dependency that can control hot wallet behavior, as seen in BigONE [Source: Real-time lessons from BigONE Exchange $27M supply chain attack, Guardrail, 2025; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
   - **Hot-wallet availability vs. strict control**: Exchanges need hot wallets to process withdrawals quickly (minutes or seconds), pushing them to centralize automation and bypass some manual checks, which increases blast radius when backend servers are compromised [Source: Security - Coinbase Developer Documentation, Coinbase, 2024; Wallet Security: Best Practices For Keeping Your Crypto Safe, Hacken, 2024].

3. **Conflicting parties and interests**
   - **Security / infrastructure teams** push for aggressive server hardening, strict access controls, segmentation, and slow, controlled changes.
   - **Product / operations / trading teams** prioritize uptime, feature velocity, and fast incident response, resisting friction from stronger controls.
   - **Vendors and integrators** benefit from deeper integration and high-privilege access, but customers want minimal trust in third parties.
   - **Regulators and institutional clients** demand provable operational security (e.g., SOC 2) and will penalize outages or losses, yet provide limited prescriptive technical guidance [Source: SOC 2 Type 1, Chainstack, 2024; Blockchain Compliance Audits & Regulatory Fines 2025, Compliancehub.wiki, 2025].

### 1.2 Goals and conditions

- **Security outcomes**:
  - Reduce major infrastructure-driven breaches from 10–15/year (2024–2025 baseline estimate) to <3/year by Q4 2026 and <1/year thereafter, across ~500+ exchanges and 50+ institutional MPC providers [Estimate: Extrapolated from public 2024–2025 incidents and Blockaid share of infrastructure losses, Medium confidence; Source: 2025 Crypto Crime Report, TRM Labs, 2025; The Defiant, 2025].
  - Lower annual infrastructure-related theft from ~$500M/year to <$100M/year (minimum), target <$50M/year by Q4 2026, via layered hardening, detection, and incident response [Source: "MPC Alone Can't Stop Multi-Million Dollar Exchange Hacks", The Defiant, 2025].

- **Control maturity targets**:
  - 100% of production servers aligned with CIS Benchmarks level 1 baseline, with infrastructure-as-code (IaC) enforcing secure configurations and automated agents enforcing <7-day patch SLAs for critical CVEs [Source: CIS Benchmarks, Center for Internet Security; MCP Server Hardening: Best Practices and Tips, ProtocolGuard, 2024].
  - 100% privileged access flows protected by MFA (preferably FIDO2 hardware tokens), PAM with vaulted credentials and session recording, network microsegmentation, and just-in-time (JIT) access by Q3 2026 [Source: Enterprise Crypto OpSec Guide: Secure Digital Assets 2025, ThreeSigma, 2025].
  - Detection latency for suspicious infrastructure activity (e.g., abnormal SSH, sudo, configuration or deployment changes, hot-wallet code modifications) reduced from current 5–72 hours to <15 minutes minimum, <5 minutes target by Q3 2026 [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025; 2025 Crypto Crime Report, TRM Labs, 2025].

- **Compliance and trust conditions**:
  - SOC 2 Type II coverage for core custody and wallet infrastructure at 100% of major institutional providers and top-tier exchanges by 2027, with clear mapping between operational controls and MPC-based cryptographic guarantees [Source: SOC 2 Type 1, Chainstack, 2024; Quick Guide: SOC 2 Compliance Requirements, Onspring, 2024].
  - Phishing simulation click rates across critical infrastructure staff reduced below 5% with ≥95% quarterly security training completion by Q2 2026 [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025].

### 1.3 Extensibility and reframing

- **System-of-systems reframing**: Rather than treating "MPC wallet" as a cryptographic component, treat the full custody platform—including servers, CI/CD, monitoring, employee devices, and vendors—as the security object. The relevant attributes become key management, infrastructure posture, identity and access management, supply chain integrity, and human factors [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS, 2024; Wallet Security: Best Practices For Keeping Your Crypto Safe, Hacken, 2024].
- **Threat-model reframing**: Move from a narrow model ("attacker must break MPC math or steal entire key") to an operations-centric model in which any entity that can push code, modify configuration, or exercise privileged access to MPC servers is a first-class risk, including insiders and vendors [Source: 2025 Crypto Crime Report, TRM Labs, 2025; Guardrail BigONE incident analysis, 2025].
- **Control-object reframing**: Instead of thinking "protect MPC" vs. "protect infrastructure", frame the goal as "prevent unauthorized withdrawal and unauthorized control of signing and custody workflows". This encompasses business logic integrity, policy enforcement, and monitoring, not just key secrecy [Source: Security - Coinbase Developer Documentation, Coinbase, 2024; Enterprise Crypto OpSec Guide, ThreeSigma, 2025].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Compute and application layer**: MPC coordinators, signing daemons, hot wallet services, API gateways, backend services for withdrawal processing, admin consoles, and batch jobs [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS, 2024; Security - Coinbase Developer Documentation, Coinbase, 2024].
- **Data and storage**: Databases containing encrypted key shares, transaction histories, balance ledgers, and configuration data; secrets managers storing API keys and service credentials; object stores for logs and backups [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025].
- **Identity and access**: IAM roles, local and domain accounts, SSH keys, VPNs, SSO providers, PAM platforms, and RBAC around deployment and configuration tools [Source: Crypto Security: Best Practices To Protect Digital Assets, Trakx, 2025].
- **Network fabric**: Internal VLANs, firewall rules, microsegmentation policies, bastion hosts, and cross-region links; public exposure via load balancers and CDNs [Source: NIST Cybersecurity Framework, NIST, current; Enterprise Crypto OpSec Guide, ThreeSigma, 2025].
- **Supply chain components**: Vendor-provided monitoring agents, backup systems, CI/CD pipelines, dependency managers, and OS package repositories that run within the trust boundary of the custody infrastructure [Source: Guardrail BigONE incident analysis, 2025; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
- **Security operations**: SIEM, EDR, vulnerability scanners, ticketing systems, incident runbooks, and SOC analyst workflows [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025].
- **Human actors**: SREs, infrastructure engineers, security engineers, developers, vendor support staff, auditors, and operations personnel with varying levels of privileged access.

### 2.2 Balance and "degree" issues

- **Patching and hardening vs. stability**: Over-aggressive hardening or rapid patching can cause performance regressions or outages, leading some teams to delay updates and disable security baselines; conversely, long patch cycles leave exploitable windows for known CVEs [Source: CIS Benchmarks, Center for Internet Security; MCP Server Hardening, ProtocolGuard, 2024].
- **Access restriction vs. operational agility**: Restrictive network segmentation and just-in-time access reduce attack surface but may slow on-call response and debugging; teams sometimes create "backdoor" access paths (shared root credentials, static VPN accounts) that undermine formal controls [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025].
- **Monitoring depth vs. noise and cost**: Deep telemetry (full packet capture, verbose logs, behavioral analytics) improves detection but increases storage and analysis cost and can overwhelm SOC capacity, encouraging teams to tune out noisy alerts and miss subtle attacker behavior [Source: Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
- **Vendor integration depth vs. blast radius**: Tightly integrated third-party agents and services improve observability and automation but, if compromised, provide direct privileged paths into production; shallow integrations reduce risk but may deprive teams of needed capabilities [Source: Guardrail BigONE incident analysis, 2025].

### 2.3 Causal chains

1. **Server breach chain (CoinDCX-style)**:
   - Phishing email or malicious job offer compromises employee workstation → malware harvests VPN and SSO credentials → attacker gains administrative access to backend servers labelled as "operational" rather than "custody critical" → weak server hardening and broad IAM roles allow lateral movement into hot wallet infrastructure or internal wallets → attacker scripts unauthorized withdrawals via internal APIs, bypassing MPC-protected cold storage [Source: CoinDCX employee arrested over malware-based theft, The Block, 2025; CoinDCX Suffers $44M Hack, Ampcus Cyber, 2025].

2. **Supply chain compromise chain (BigONE-style)**:
   - Third-party software used in hot wallet stack (e.g., deployment agent, monitoring plugin, library) is compromised upstream → malicious update is signed or distributed from trusted channel → production agents auto-update and execute malicious code → malicious logic alters withdrawal destinations or bypasses policy checks inside hot wallet services → MPC continues to sign because requests appear legitimate within business logic [Source: Real-time lessons from BigONE Exchange $27M supply chain attack, Guardrail, 2025; Supply Chain Attacks in Crypto: BigONE Breach, OKX Learn, 2025].

3. **Systemic detection-lag chain**:
   - Limited behavioral baselines, under-tuned SIEM rules, and fragmented logging → unusual withdrawals, configuration changes, or admin logins appear as noisy events → attackers operate undetected for hours or days, increasing cumulative losses and complicating forensics [Source: 2025 Crypto Crime Report, TRM Labs, 2025; Enterprise Crypto OpSec Guide, ThreeSigma, 2025].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and relationships

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | Cloud providers, OS vendors, third-party tooling and security vendors | Provide secure-by-default platforms, tools, and updates; grow adoption; minimize their own liability | Shared-responsibility model limits control over customer misconfigurations; update rollouts must balance speed vs. stability | Customers may blame vendors for breaches despite misconfigurations; vendors may resist disclosure of their own security issues [Source: NIST Cybersecurity Framework, NIST; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025] |
| Downstream | Exchanges, custodians, MPC wallet platforms | Protect customer assets, maintain uptime, meet regulatory expectations, and control costs | Legacy infrastructure, constrained security budgets, talent shortages, and regulatory uncertainty | Security vs. product speed; infra teams vs. business demands; tension between investing in hardening vs. visible features [Source: Security - Coinbase Developer Documentation, Coinbase, 2024; MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024] |
| Sideline / External | End users, institutional clients, regulators, auditors, insurers | Asset safety, transparency, legal compliance, predictable risk; reliable attestations like SOC 2 | Limited visibility into backend design; must rely on third-party reports and incidents; conservative risk appetite | Regulators may enforce heavy penalties or restrictions after incidents; clients may rapidly withdraw assets, causing liquidity stress [Source: SOC 2 Type 1, Chainstack, 2024; Blockchain Compliance Audits & Regulatory Fines 2025, Compliancehub.wiki, 2025] |

### 3.2 Environment

- **Threat environment**: State-linked groups (e.g., North Korean clusters) and organized criminal gangs increasingly focus on centralized infrastructure and key theft, not just DeFi protocol exploits, because centralized actors hold large custodial balances and often have weaker opsec [Source: 2025 Crypto Crime Report, TRM Labs, 2025].
- **Regulatory landscape**: Crypto custodians are being held to standards closer to traditional financial institutions, including expectations for segregation of duties, incident reporting, and audited internal controls; regulatory fines averaged ~$426M for blockchain companies in 2024, indicating high enforcement pressure [Source: Blockchain Compliance Audits & Regulatory Fines 2025, Compliancehub.wiki, 2025].
- **Technology trends**: Wider adoption of hardware-based enclaves (e.g., AWS Nitro Enclaves), confidential computing, and microsegmentation provides new tools for isolating MPC components and minimizing blast radius [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS, 2024; NIST Cybersecurity Framework, NIST].

### 3.3 Responsibility and room for maneuver

- **Providers (exchanges and MPC vendors)** bear primary responsibility for end-to-end custody security, including infrastructure posture and vendor risk—not just cryptographic design. They can choose architectures (e.g., enclaves, isolated subnets), invest in PAM, fund red-teaming, and mandate stronger vendor contracts [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025; Security - Coinbase Developer Documentation, Coinbase, 2024].
- **Cloud and tooling vendors** must continue to improve secure defaults (e.g., hardened AMIs, configuration baselines), publish clear shared-responsibility guidance, and respond quickly to vulnerabilities, but cannot fully prevent customer misconfigurations [Source: NIST Cybersecurity Framework, NIST; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
- **Regulators and auditors** can clarify expectations (e.g., including infra posture and supply chain controls in custody assessments), provide safe harbors for transparent incident disclosure, and incentivize early adoption of best practices like SOC 2 Type II and continuous monitoring [Source: SOC 2 Type 1, Chainstack, 2024; Quick Guide: SOC 2 Compliance Requirements, Onspring, 2024].

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2010–2018 – Cold-storage-first mindset**: Early exchanges focused on "cold storage" and simple hot wallets, viewing infrastructure mainly through the lens of key storage rather than end-to-end operational security; Mt. Gox and other incidents highlighted key theft but did not yet produce mature infra-hardening practices [Source: 2025 Crypto Crime Report, TRM Labs, 2025; Wallet Security: Best Practices For Keeping Your Crypto Safe, Hacken, 2024].
2. **2019–2021 – Institutional custody and SOC 2 era**: Institutional custodians and MPC providers emerged, adopting SOC 2 and some cloud-security tooling, but many controls remained focused on logical segregation and key management rather than systematic server, access, and supply chain hardening [Source: SOC 2 Type 1, Chainstack, 2024; Finding End-to-End Security in Crypto Custody, Anchorage Digital, 2023].
3. **2022–2023 – High-profile infrastructure compromises**: Incidents like the Ronin Bridge compromise (validator infrastructure and access controls) showed that infrastructure and social engineering attacks could dwarf smart-contract vulnerabilities, but many exchanges still prioritized feature growth over rigorous opsec [Source: 2025 Crypto Crime Report, TRM Labs, 2025].
4. **2024–2025 – Shift to infrastructure attacks as dominant vector**: By Q2 2024, ~65% of crypto losses were attributed to centralized infrastructure compromises; July 2025 incidents at CoinDCX and BigONE made it clear that MPC alone is not sufficient to prevent large-scale theft if backend servers, CI/CD, or third-party software are compromised [Source: "MPC Alone Can't Stop Multi-Million Dollar Exchange Hacks", The Defiant, 2025; Guardrail BigONE incident analysis, 2025].

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - Rapid expansion of exchanges and MPC vendors outpaced security engineering and governance capacity; many organizations treated security as an add-on, not a core design constraint [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].
  - Legacy architectures with flat internal networks and traditional perimeter security persisted even as attackers adopted phishing, credential theft, and supply chain techniques specifically targeting centralized infra [Source: 2025 Crypto Crime Report, TRM Labs, 2025].
  - Underinvestment in security training and culture left staff vulnerable to social engineering and poor operational hygiene [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025].

- **Direct technical/operational causes**:
  - Insufficient server hardening (default services enabled, weak SSH and sudo policies, lack of baseline enforcement) created easy lateral movement once initial access was gained [Source: MCP Server Hardening, ProtocolGuard, 2024; CIS Benchmarks, Center for Internet Security].
  - Weak identity and access management (shared admin accounts, limited MFA coverage, broad IAM roles) enabled attackers to reuse stolen credentials and escalate privileges quickly [Source: Crypto Security: Best Practices To Protect Digital Assets, Trakx, 2025].
  - Third-party software with deep access (monitoring, deployment, analytics agents) lacked robust vetting, update validation, and sandboxing, allowing a single compromised dependency to manipulate hot wallet logic [Source: Guardrail BigONE incident analysis, 2025; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].

### 4.3 Root issues

- **Misalignment between cryptographic and operational risk models**: Many organizations believed that MPC’s removal of single-key failure points materially solved custody risk, while underestimating the probability and impact of backend infrastructure compromise [Source: "MPC Alone Can't Stop Multi-Million Dollar Exchange Hacks", The Defiant, 2025; Build secure MPC wallets using AWS Nitro Enclaves, AWS, 2024].
- **Incentive and measurement gaps**: Losses caused by operational weaknesses are often socialized or covered by the exchange, creating weaker feedback loops than on-chain exploits where failures are public and directly attributable; infra hardening has historically been hard to quantify for business stakeholders [Source: Blockchain Compliance Audits & Regulatory Fines 2025, Compliancehub.wiki, 2025; Enterprise Crypto OpSec Guide, ThreeSigma, 2025].
- **Fragmented responsibility for third-party risk**: Security ownership for vendor agents, CI/CD tooling, and infrastructure libraries is often diffuse across engineering, procurement, and security teams, leading to blind spots and slow response when supply-chain vulnerabilities arise [Source: Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory if nothing changes

- **Increasing share of infrastructure-driven losses**: If current practices continue, centralized infrastructure compromises are likely to remain the dominant cause of large-value crypto theft, as attackers rationally target centralized custodians with large balances and historically weaker operational controls [Source: 2025 Crypto Crime Report, TRM Labs, 2025; The Defiant, 2025].
- **Growing sophistication of attackers**: Supply chain and CI/CD pipeline attacks are becoming more common across software ecosystems; crypto custody is particularly exposed due to high value per deployment and widespread use of third-party agents [Source: Guardrail BigONE incident analysis, 2025; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
- **Regulatory backlash risk**: Continued large-scale losses may trigger stricter regulations, mandatory insurance, or capital requirements for custodians, increasing operating costs and potentially driving consolidation toward larger, more mature providers [Source: Blockchain Compliance Audits & Regulatory Fines 2025, Compliancehub.wiki, 2025].

### 5.2 Early signals

- **Concentration of losses in infra attacks**: 65% of Q2 2024 losses being infra-related is already a strong signal that the attack frontier has moved from pure on-chain vulnerabilities to operational weaknesses [Source: The Defiant, 2025; 2025 Crypto Crime Report, TRM Labs, 2025].
- **Public focus on supply chain risk**: The BigONE incident, along with broader 2025 discussions about compromised npm packages and tooling, shows that critical infrastructure increasingly depends on complex third-party ecosystems [Source: Guardrail BigONE incident analysis, 2025; SecurityScorecard whitepaper, 2025].
- **Emergence of operational security playbooks**: Guides from Web3 infrastructure providers and auditors are beginning to focus on end-to-end operational security, indicating growing recognition of the problem and availability of best-practice patterns [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025; Security - Coinbase Developer Documentation, Coinbase, 2024].

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**: Top exchanges and MPC vendors implement robust server hardening, zero-trust access, and supply chain controls; state-of-the-art detection and incident response reduce time-to-detect to minutes; major infra breaches drop significantly, and regulators view MPC-based custody as at least as safe as traditional models [Estimate: Based on adoption rates of security controls in mature financial institutions, Medium confidence; Source: NIST Cybersecurity Framework, NIST; Enterprise Crypto OpSec Guide, ThreeSigma, 2025].
- **Baseline scenario**: Large, well-funded providers reach high maturity, while mid-tier exchanges lag due to cost and talent constraints; infra-driven losses decline modestly in aggregate but remain frequent among smaller players; regulators begin to differentiate between "systemically important" well-controlled custodians and the long tail [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024; 2025 Crypto Crime Report, TRM Labs, 2025].
- **Pessimistic scenario**: Another high-profile, nine-figure loss occurs due to infrastructure compromise (e.g., CI/CD or enclave misconfiguration), triggering sharp regulatory and market reactions; some jurisdictions restrict or heavily regulate centralized crypto custody, accelerating a shift to self-custody and alternative architectures while leaving others exposed [Estimate: Risk scenario extrapolated from 2022–2025 incident patterns, Medium confidence; Source: 2025 Crypto Crime Report, TRM Labs, 2025].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Established cryptographic and infrastructure expertise**: Major MPC vendors and top exchanges employ strong cryptography and infrastructure security teams, capable of designing secure architectures using enclaves, microsegmentation, and PAM [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS, 2024; Enterprise Crypto OpSec Guide, ThreeSigma, 2025].
- **Rich tooling ecosystem**: Cloud security platforms, CIS baselines, vulnerability scanners, SIEMs, and modern PAM and EDR solutions provide a strong foundation for implementing best practices if properly configured [Source: CIS Benchmarks, Center for Internet Security; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
- **Growing compliance maturity**: Many institutional custodians already pursue or hold SOC 2 Type II reports and have established change management, incident response, and access review processes that can be extended to cover MPC-specific infrastructure [Source: SOC 2 Type 1, Chainstack, 2024; Quick Guide: SOC 2 Compliance Requirements, Onspring, 2024].

### 6.2 Capability gaps

- **Server and network hardening coverage**: Across the industry, less than half of production servers are likely fully aligned with CIS benchmarks and enforced via automation, leaving large configuration drift and unmanaged attack surface [Estimate: Inferred from incident patterns and typical enterprise baselines, Medium confidence; Source: MCP Server Hardening, ProtocolGuard, 2024].
- **Privileged access management maturity**: Many providers still lack full PAM deployments, rely on static admin credentials, and do not record privileged sessions, limiting both prevention and forensic capabilities [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025].
- **Supply chain governance**: Few exchanges maintain comprehensive SBOMs, continuous dependency scanning, and vendor-risk programs specifically tuned to hot wallet and MPC infrastructure, leading to blind spots similar to BigONE’s [Source: Guardrail BigONE incident analysis, 2025; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
- **Security culture and training**: Social engineering remains a leading initial access vector; many teams still treat quarterly phishing simulations and role-specific secure-operations training as optional rather than mandatory [Source: 2025 Crypto Crime Report, TRM Labs, 2025; Enterprise Crypto OpSec Guide, ThreeSigma, 2025].

### 6.3 Buildable capabilities (1–6 months)

- **Infrastructure security baseline program**: Define and roll out hardened base images (golden AMIs or container baselines), IaC modules, and CI checks enforcing CIS-aligned configurations for all custody-related workloads [Source: CIS Benchmarks, Center for Internet Security; MCP Server Hardening, ProtocolGuard, 2024].
- **Access control modernization**: Deploy PAM for all production admin accounts, enforce hardware-backed MFA for all privileged paths, and establish microsegmented network zones around MPC servers and hot wallet logic [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025; Crypto Security: Best Practices To Protect Digital Assets, Trakx, 2025].
- **Supply chain and CI/CD hardening**: Implement SBOM generation and dependency scanning, signed artifact pipelines, and strict change controls for MCP and hot-wallet code, plus vendor assessments for agents running on production nodes [Source: Guardrail BigONE incident analysis, 2025; Bridging Compliance and Cybersecurity, SecurityScorecard, 2025].
- **Targeted opsec training and simulations**: Launch role-specific phishing simulations and incident-response tabletop exercises focused on server breaches and supply chain intrusions, with clear metrics and improvement targets [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: MPC adoption has increased, but backend infrastructure often remains at inconsistent hardening and monitoring maturity.
- **Core problem**: Attackers bypass MPC cryptographic protections by compromising backend servers, access systems, and supply chains.
- **Internal structure**: Interplay of compute, data, identity, network, supply chain, SOC, and human factors; tradeoffs between hardening, agility, and cost.
- **External forces**: Advanced threat actors, regulatory pressure, and evolving compliance frameworks.
- **Trends**: Infrastructure attacks now dominate loss categories; sophistication and scale are increasing.
- **Capabilities**: Strong cryptography and tooling exist but are unevenly deployed; large maturity gap between top and mid-tier providers.
- **Options**: Comprehensive infra-hardening and zero-trust adoption, enclave-based isolation, supply-chain governance, and differentiated risk tiers by asset class.
- **Risks**: Migration complexity, performance impact, talent shortages, and regulatory uncertainty.

### 7.2 Key judgments needing validation

1. **Operational controls, not cryptography, are now the primary determinant of custody risk** for exchanges and MPC providers [Source: 2025 Crypto Crime Report, TRM Labs, 2025; The Defiant, 2025].
2. **Implementing CIS-level hardening, PAM, and supply-chain controls can reduce successful infrastructure attacks by at least half** over 12–24 months for organizations that adopt them rigorously [Estimate: Based on historical impact of hardening in traditional financial institutions, Medium confidence; Source: NIST Cybersecurity Framework, NIST; SecurityScorecard whitepaper, 2025].
3. **Detection latency is the main driver of loss magnitude** once compromise occurs; reducing detection from hours to minutes can cut realized losses by an order of magnitude [Estimate: Derived from incident postmortems across exchanges and traditional finance, Medium confidence; Source: 2025 Crypto Crime Report, TRM Labs, 2025].
4. **Mid-tier exchanges may struggle to afford full best-practice stacks**, requiring shared-services models, managed security providers, or consolidation to achieve needed maturity [Source: MPC Wallet Development Market Growth 2025–2032, Intel Market Research, 2024].

### 7.3 Alternative paths

- **Path A – Full zero-trust transformation**: Comprehensive program deploying enclaves for MPC, strict microsegmentation, PAM, and deep monitoring for all custody-related systems.
- **Path B – Risk-tiered hardening**: Prioritize highest-value assets and hot-wallet flows for full zero-trust treatment; adopt lighter-weight controls for lower-risk systems.
- **Path C – Outsourced or shared-security model**: Smaller exchanges rely on highly mature custody / wallet-as-a-service providers or managed security services instead of building full internal capabilities.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- **Security-optimist bias**: Assuming that well-designed programs will be funded and executed effectively across the industry, while many organizations may underinvest or cut corners.
- **Centralized-provider bias**: Focus on exchanges and custodians may underweight risk migration to other ecosystems (e.g., DeFi protocols, cross-chain bridges) and interactions between them [Source: 2025 Crypto Crime Report, TRM Labs, 2025].
- **Publication bias**: Public reports primarily cover large incidents; many smaller or near-miss infrastructure compromises are likely never disclosed, potentially underestimating true frequency [Source: Blockchain Compliance Audits & Regulatory Fines 2025, Compliancehub.wiki, 2025].

### 8.2 Required intelligence

- **Industry-wide baseline data**: More precise statistics on server hardening coverage, PAM adoption, and supply chain security practices across exchanges and MPC providers [Source: SecurityScorecard, 2025; Intel Market Research, 2024].
- **Incident analytics**: Aggregated, anonymized data on time-to-detect, time-to-contain, and loss magnitudes for infra-driven breaches, to validate the impact of detection improvements [Source: 2025 Crypto Crime Report, TRM Labs, 2025].
- **Cost-benefit metrics**: Evidence comparing TCO of comprehensive hardening and monitoring vs. expected-loss reduction, especially for mid-tier exchanges [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025].

### 8.3 Validation plan

- **Benchmark study**: Survey a representative sample of exchanges and custodians on infrastructure controls (hardening, IAM, monitoring, supply chain), correlate with incident history, and publish anonymized benchmarks.
- **Pilot programs**: Run zero-trust and PAM pilots in a subset of environments, measuring changes in detected anomalies, incident counts, and time-to-detect over 6–12 months.
- **Regulatory and audit feedback loop**: Engage with auditors and regulators to validate that proposed control sets and metrics meet or exceed expectations for SOC 2 and custody requirements.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Quantitative estimates of incident frequency, loss magnitude, and risk reduction from specific controls will change as more empirical data is collected.
- Recommended architectural patterns may shift as confidential-computing technologies, enclave platforms, and MPC implementations evolve.
- Regulatory expectations and industry norms around acceptable detection latency and mandatory controls may tighten after future incidents.

### 9.2 Incremental approach

- Start with **low-regret, reversible controls** (e.g., improved logging, SIEM tuning, stricter MFA, inventory and classification of infrastructure assets) before large-scale architectural changes.
- Progressively roll out **segmentation, PAM, and supply-chain controls** to the most critical environments first (hot wallets, MPC coordinators), then broaden coverage.
- Use **canary deployments and blue/green rollouts** for OS hardening and configuration changes to minimize operational risk.

### 9.3 "Good enough" criteria

- All custody-critical servers managed via hardened baselines and IaC, with no unmanaged pets.
- All privileged access enforced through MFA + PAM + logging, with quarterly access reviews and no shared admin accounts.
- End-to-end monitoring of withdrawal flows and infrastructure changes in place, with median detection latency <15 minutes and tested incident response runbooks.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. The main systemic risk for exchanges and MPC wallet providers has shifted from cryptographic failure to backend infrastructure, access, and supply-chain compromise; MPC alone cannot prevent losses when attackers control servers executing wallet logic [Source: The Defiant, 2025; Guardrail BigONE incident analysis, 2025].
2. Established best practices for server hardening, zero-trust access, and supply chain governance from broader cybersecurity can substantially reduce risk if applied with rigor to custody infrastructure [Source: CIS Benchmarks, Center for Internet Security; NIST Cybersecurity Framework, NIST].
3. Detection latency and incident response quality are key levers for reducing realized losses once compromise occurs; minutes vs. hours can make the difference between a contained incident and tens of millions in theft [Source: 2025 Crypto Crime Report, TRM Labs, 2025].

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

- **【P0 – Critical】**
  1. Establish custody-infrastructure asset inventory and classification → Security & Infra Leads → Coverage: unknown → 100% of servers, services, and vendor agents in inventory → 2026-03-31.
  2. Enforce hardware-backed MFA on 100% of privileged access paths (SSH, VPN, admin consoles, CI/CD) → Identity & Access Lead → Critical accounts with strong MFA: ~30–50% → 100% → 2026-06-30.
  3. Deploy baseline SIEM rules and dashboards for hot wallet and MPC infrastructure (logins, config changes, deployments, withdrawal patterns) → SOC Lead → Detection latency: 5–72h → <60 min median → 2026-03-31.

- **【P1 – Important】**
  4. Roll out hardened server baselines (CIS-aligned images + IaC modules) for all new custody-critical workloads → Infrastructure Lead → New deployments on hardened baselines: 0% → 100% → 2026-06-30.
  5. Implement PAM for all production admin accounts, including session recording and JIT access for high-risk actions → Security Engineering → Admin accounts integrated: 0% → ≥80% → 2026-09-30.

- **【P2 – Optional】**
  6. Pilot enclave-based isolation (e.g., Nitro Enclaves) for MPC signing servers to constrain blast radius even under host compromise → Architecture Team → Enclave-protected MPC flows: pilot only → production for ≥1 asset tier → 2026-12-31.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Hardening and access changes cause outages or slow incident response | High | Medium | Elevated error rates, deployment failures, or delayed on-call interventions after new controls | Use phased rollouts, robust testing, runbooks for break-glass access consistent with audit requirements | Infrastructure Lead |
| Incomplete coverage leaves critical legacy systems unprotected | High | Medium | Discovery of unmanaged servers or tools during incidents or audits | Enforce asset inventory as gate for production; require sign-off that all custody systems are under baseline management | CISO |
| Supply chain controls lag behind server and IAM improvements | Medium | High | Vendor component compromise or critical CVE in agent/CI/CD tool | Prioritize SBOMs and vendor risk management for agents running on custody-critical nodes; require signed updates and tight scopes | Vendor Risk Lead |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A: Full zero-trust and enclave-centric architecture** | Strong isolation and least privilege; minimal blast radius even under host compromise; strong story for regulators and institutions | High engineering and infra cost; complex migration; may require re-architecting legacy systems | Migration bugs, performance overhead, talent constraints | Large providers with strong infra/security teams and long-term MPC roadmap | Very small teams or legacy-heavy environments unable to support major refactors |
| **B: Incremental hardening + monitoring (risk-tiered)** | Faster time-to-value; focuses resources on highest-risk assets; lower disruption; easier to adopt for mid-tier players | Leaves some lower-tier systems with weaker controls; relies heavily on correct risk-tiering | Attackers pivot through "lower-tier" systems that are still connected to critical environments | Organizations with limited budget/talent but willingness to prioritize and iterate | Cases where regulatory or client expectations require uniform controls across environment |
| **C: Outsource to mature custodians / WaaS providers** | Access to advanced security programs without building everything in-house; economies of scale | Vendor lock-in; dependency on third-party operational resilience; integration and legal complexity | Provider outage or breach; misalignment of risk appetite | Smaller exchanges and enterprises lacking security talent or capital expenditure capacity | Very large exchanges whose scale and risk profile justify owning full stack in-house |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **Backend infrastructure** | Servers, networks, databases, and supporting services that execute MPC protocols, hot wallet logic, and operational workflows, excluding on-chain components | N/A | [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025] |
| **MPC wallet** | Wallet architecture where private key material is split into shares across multiple parties or devices and signatures are generated via secure multi-party computation without reconstructing the key | N/A | [Source: Build secure MPC wallets using AWS Nitro Enclaves, AWS, 2024] |
| **Hot wallet** | Internet-connected wallet holding a small fraction (~3–5%) of assets for operational liquidity (withdrawals, trading), typically with automated or semi-automated signing | N/A | [Source: Security - Coinbase Developer Documentation, Coinbase, 2024] |
| **Cold storage** | Highly restricted custody setup (often air-gapped or with strong physical controls) holding the majority (~95%+) of assets, with manual, multi-party approval processes | N/A | [Source: Wallet Security: Best Practices For Keeping Your Crypto Safe, Hacken, 2024] |
| **Server hardening** | Process of securing servers by disabling unnecessary services, enforcing security baselines, minimizing privileges, and keeping systems patched per benchmarks like CIS | N/A | [Source: CIS Benchmarks, Center for Internet Security; MCP Server Hardening, ProtocolGuard, 2024] |
| **Zero-trust architecture** | Security model that assumes breach and requires continuous verification of user and device identity, enforcing least privilege and microsegmentation for every access request | N/A | [Source: NIST Cybersecurity Framework, NIST] |
| **Privileged Access Management (PAM)** | Set of tools and processes for securing and monitoring high-privilege accounts, typically including credential vaults, approval workflows, JIT access, and session recording | N/A | [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025] |
| **Microsegmentation** | Fine-grained network segmentation technique that restricts east–west traffic between workloads, limiting lateral movement after compromise | N/A | [Source: NIST Cybersecurity Framework, NIST; Enterprise Crypto OpSec Guide, ThreeSigma, 2025] |
| **Supply chain attack** | Compromise delivered through third-party software, libraries, or services that are trusted and integrated into the target’s environment, allowing attackers to bypass direct perimeter defenses | N/A | [Source: Guardrail BigONE incident analysis, 2025; SecurityScorecard whitepaper, 2025] |
| **SOC 2 Type II** | Audit report that assesses the design and operating effectiveness of security and related controls over a defined observation period (typically ≥6 months) | N/A | [Source: Quick Guide: SOC 2 Compliance Requirements, Onspring, 2024] |
| **SIEM** | Security Information and Event Management platform that aggregates logs, applies detection rules, and supports investigations and incident response | N/A | [Source: Enterprise Crypto OpSec Guide, ThreeSigma, 2025] |
| **Detection latency** | Time between an attacker action (e.g., unauthorized login, code change) and the moment the defender detects and begins responding to it | minutes / hours | [Source: 2025 Crypto Crime Report, TRM Labs, 2025] |
| **SBOM (Software Bill of Materials)** | Formal inventory of components (libraries, packages) within a software system, used to manage vulnerabilities and supply chain risk | N/A | [Source: Bridging Compliance and Cybersecurity, SecurityScorecard, 2025] |

---

## 12. References

### Tier 1 – Primary / Technical Sources

1. **AWS**. (2024). *Build secure multi-party computation (MPC) wallets using AWS Nitro Enclaves*. AWS Web3 Blog. https://aws.amazon.com/blogs/web3/build-secure-multi-party-computation-mpc-wallets-using-aws-nitro-enclaves  
   **[Cited in**: Context Recap; Sections 1–3, 4, 6–7, 10–11 **]**
2. **Center for Internet Security (CIS)**. (current). *CIS Benchmarks*. https://www.cisecurity.org/cis-benchmarks  
   **[Cited in**: Context Recap; Sections 1–2, 4, 6–7, 10–11 **]**
3. **NIST**. (current). *NIST Cybersecurity Framework* and supporting publications.  
   **[Cited in**: Sections 2–3, 5–7, 10–11 **]**
4. **Halborn**. (2025). *Explained: The CoinDCX Hack (July 2025)*. https://www.halborn.com/blog/post/explained-the-coindcx-hack-july-2025  
   **[Cited in**: Context Recap; Sections 1–2, 4–5 **]**
5. **Guardrail**. (2025). *Real-time lessons from BigONE Exchange $27M supply chain attack*. https://www.guardrail.ai/blog/real-time-lessons-from-bigone-exchange-27m-supply-chain-attack  
   **[Cited in**: Context Recap; Sections 1–3, 4–7, 10–11 **]**
6. **Coinbase**. (2024). *Security – Coinbase Developer Documentation*. https://docs.cloud.coinbase.com/server-wallets/v2/introduction/security  
   **[Cited in**: Context Recap; Sections 1–3, 5–7, 10 **]**

### Tier 2 – Industry Reports and Analyses

7. **TRM Labs**. (2025). *2025 Crypto Crime Report*. TRM Labs.  
   **[Cited in**: Context Recap; Sections 1–6, 7–10 **]**
8. **The Defiant**. (2025). *"MPC Alone Can't Stop Multi-Million Dollar Exchange Hacks, Experts Warn"*. The Defiant. https://thedefiant.io/news/infrastructure/mpc-alone-can-t-stop-multi-million-dollar-exchange-hacks-experts-warn  
   **[Cited in**: Context Recap; Sections 1, 4–5, 7, 10 **]**
9. **The Block**. (2025). *CoinDCX CEO blames 'server breach' for $44 million exploit; Indian firm will cover losses*. The Block. https://www.theblock.co/post/363479/coindcx-ceo-blames-server-breach-for-44-million-exploit-indian-firm-will-cover-losses  
   **[Cited in**: Context Recap; Sections 2, 4–5 **]**
10. **Ampcus Cyber**. (2025). *CoinDCX Suffers $44M Hack, User Funds Remain Safe*. Ampcus Cyber. https://www.ampcuscyber.com/shadowopsintel/coindcx-suffers-usd-44-million-hack  
    **[Cited in**: Context Recap; Sections 2, 4–5 **]**
11. **OKX**. (2025). *Supply Chain Attacks in Crypto: BigONE Breach and North Korean Threats Shake Industry*. OKX Learn. https://okx.com/learn/supply-chain-attacks-crypto-security-breach  
    **[Cited in**: Context Recap; Sections 2–5 **]**
12. **Coinmonks (Medium)**. (2025). *$139M Gone: The 5 Most Devastating Crypto Hacks of July 2025*. Medium. https://medium.com/coinmonks/139m-gone-the-5-most-devastating-crypto-hacks-of-july-2025-8598393d6e83  
    **[Cited in**: Context Recap; Sections 4–5 **]**
13. **ThreeSigma**. (2025). *Enterprise Crypto OpSec Guide: Secure Digital Assets 2025*. ThreeSigma Blog. https://threesigma.xyz/blog/opsec/enterprise-crypto-opsec-guide-2025  
    **[Cited in**: Context Recap; Sections 1–3, 5–8, 10–11 **]**
14. **ProtocolGuard**. (2024). *MCP Server Hardening: Best Practices and Tips*. ProtocolGuard. https://protocolguard.com/resources/mcp-server-hardening  
    **[Cited in**: Context Recap; Sections 1–2, 4, 6–7, 10–11 **]**
15. **Chainstack**. (2024). *SOC 2 Type 1: Our commitment to secure Web3 infrastructure*. Chainstack. https://chainstack.com/chainstack-commitment-secure-web3-infrastructure  
    **[Cited in**: Context Recap; Sections 1–3, 6–8, 10 **]**
16. **Compliancehub.wiki**. (2025). *Blockchain Compliance Audits & Regulatory Fines 2025: Complete Guide*. Compliancehub.wiki. https://www.compliancehub.wiki/blockchain-compliance-audits-regulatory-fines-2025-complete-guide  
    **[Cited in**: Context Recap; Sections 1, 3–5, 7–8, 10 **]**
17. **Onspring**. (2024). *Quick Guide: SOC 2 Compliance Requirements and How to Meet Them*. Onspring. https://onspring.com/soc-2-compliance-requirements-and-how-to-meet-them  
    **[Cited in**: Context Recap; Sections 1, 3, 6–8, 10 **]**
18. **SecurityScorecard**. (2025). *Bridging Compliance and Cybersecurity*. SecurityScorecard Whitepaper. https://securityscorecard.com/wp-content/uploads/2025/06/RegulatoryCompliance-Whitepaper_060325_05-2.pdf  
    **[Cited in**: Context Recap; Sections 2–3, 4–8, 10–11 **]**
19. **Trakx**. (2025). *Crypto Security: Best Practices To Protect Digital Assets*. Trakx. https://trakx.io/resources/insights/crypto-security  
    **[Cited in**: Sections 1–2, 6–7, 10 **]**
20. **Coinbureau**. (2025). *Is KuCoin Safe in 2025? Security, Legal, Risks*. Coinbureau. https://coinbureau.com/analysis/is-kucoin-safe  
    **[Cited in**: Background reasoning for exchange security models; not used for unique numerical claims.**]
21. **3Commas**. (2025). *Secure Cryptocurrency Assets in 2025: Complete Guide*. 3Commas Blog. https://3commas.io/blog/secure-cryptocurrency-assets-2025  
    **[Cited in**: Sections 1–2, 6–7 **]**
22. **Hacken**. (2024). *Wallet Security: Best Practices For Keeping Your Crypto Safe*. Hacken. https://hacken.io/discover/wallet-security  
    **[Cited in**: Sections 1–2, 4–5, 11 **]**
23. **Intel Market Research**. (2024). *MPC Wallet Development Market Growth 2025–2032*. Intel Market Research.  
    **[Cited in**: Sections 3, 4, 5, 6–8, 10 **]**

### Internal / Problem-Specific Sources and Estimates

24. **Problem Statement – Backend Server Infrastructure Operational Security Bypassing MPC Protection**. (2025). Internal documentation summarizing problem statement, goals, constraints, stakeholders, and known facts.  
    **[Cited in**: Context Recap; Sections 1–2, 4–7, 10 **]**
25. **Estimates and assumptions**. Various.  
    Method: Extrapolation from public incident data, infra security benchmarks in traditional finance, and observed adoption of security controls. Confidence: Medium. Validation: To be refined via provider-specific data, benchmarks, and audits.  
    **[Used in**: Sections 1, 5–7, 9–10 **]**
