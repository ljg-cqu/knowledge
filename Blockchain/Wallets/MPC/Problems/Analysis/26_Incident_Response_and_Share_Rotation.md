# Incident Response and Share Rotation for Compromised MPC Infrastructure – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Security Operations Team  
**Related Problem**: `../26_Incident_Response_and_Share_Rotation.md`

---

## Context Recap

- **Problem title**: Incident Response and Share Rotation for Compromised MPC Infrastructure
- **Current state**:
  - MPC custodians operate 3–5 node clusters across multiple environments with threshold schemes (e.g., k-of-n TSS for ECDSA/Schnorr) protecting $10M–$1B+ per institutional client [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "How MPC Wallets Actually Work"].
  - Detection of node compromise or key-share exfiltration often takes **hours–days**, driven by generic infra monitoring rather than MPC-specific indicators of compromise (IOCs) [Estimate: extrapolated from general breach detection timelines and current tooling maturity].
  - Share refresh/rotation is supported by proactive secret sharing (PSS) but is typically run in scheduled maintenance windows and can require **6–24+ hours** of coordination across parties [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Security Incidents and Lessons Learned"; Source: Offline Proactive Refresh: Strengthening Threshold Signature Wallets, Silence Laboratories, 2024].
  - 2024 blockchain incidents highlight that compromised accounts and keys (including signatures) account for **>80% of value stolen**, with ~$2.2B lost as of Dec 2024 [Source: 2024 Blockchain Security in Review: Key Lessons Learned, Halborn, 2024].
- **Pain points**:
  - **Slow detection** of partial compromise: memory/disk exfiltration on one node may not trigger fraud; detection often happens only after anomalous signing or infra alerts.
  - **Slow, coordination-heavy share rotation**: refresh protocols require multi-round interaction; requiring all parties online turns refresh into an operationally fragile ceremony [Source: Offline Proactive Refresh: Strengthening Threshold Signature Wallets, Silence Laboratories, 2024].
  - **Service disruption risk**: conservative containment (shutting down whole clusters) can cause full custodial outages and missed SLAs.
  - **Regulatory/contractual pressure**: GDPR requires data breach notification to authorities within **72 hours of awareness** [Source: 72 hours – how to respond to a personal data breach, ICO, 2024]; SOC 2 guidance expects timely incident detection, logging, and reporting [Source: SOC Incident Reporting: What are SOC 2 Security Reporting Requirements?, Linford & Co, 2018].
- **Goals** (from problem file):
  - Detection <1h (min) / <30min (target) / <15min (ideal) from intrusion to alert.
  - Containment (node isolation) <1h (target <30min).
  - Share rotation completion <8h (min) / <4h (target) / <2h (ideal).
  - Maintain >95–99.9% signing availability for unaffected tiers during incidents.
  - Achieve 0 unauthorized signing events from compromised shares.
  - Meet GDPR/SOC 2 notification timelines with accurate scope.
- **Hard constraints**:
  - Time window: Q1–Q3 2025 for building runbooks, automation, monitoring, and exercising.
  - Budget: $400K–$800K; staffing: 2–3 security ops, 2–3 crypto engineers, 1–2 forensics, 1 compliance specialist.
  - Rotation must preserve threshold security: no full key reconstruction; use PSS/refresh extensions compatible with deployed MPC protocols [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025; Source: Offline Proactive Refresh, Silence Laboratories, 2024].
  - Regulatory reporting must be evidence-backed and consistent with NIST-style incident handling best practices [Source: NIST SP 800-61 Rev. 2, Computer Security Incident Handling Guide, Cichonski et al., 2012].

---

## 1. Problem Definition (Aspect 1) 【Core】

### 1.1 Problem & contradictions

1. **Core problem**
   - When one or more MPC key-share servers are compromised or suspected compromised, organizations must **rapidly detect, analyze, contain, and rotate shares** before attackers accumulate k-of-n shares, **without** causing unnecessary service outages or violating regulatory timelines.

2. **Key contradictions**
   - **Speed vs. certainty**: Fast containment (e.g., immediate node shutdown) protects assets but may destroy volatile forensic evidence needed for root-cause analysis and regulatory reporting [Source: NIST SP 800-61 Rev. 2, Cichonski et al., 2012].
   - **Security vs. availability**: Aggressive isolation and full signing suspension reduce theft risk but disrupt institutional operations and may breach SLAs; overly cautious actions keep services running but extend the attacker's window to aggregate shares [Source: 2024 Blockchain Security in Review, Halborn, 2024].
   - **Centralization vs. distribution**: Operational simplicity suggests central decision-making and automation, while MPC’s security model depends on distribution of control and independent failure domains [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025].
   - **One-time response vs. continuous hygiene**: Treating share rotation as a rare emergency ceremony is operationally fragile; but fully continuous refresh (e.g., daily) may be costly without automation and offline refresh mechanisms [Source: Offline Proactive Refresh, Silence Laboratories, 2024].

### 1.2 Goals & conditions

- **Primary goals** (refined):
  - **Detection**: Achieve automated MPC-specific compromise detection (e.g., anomalous memory access, suspicious process/network patterns on MPC nodes) with median detection time <30min.
  - **Containment**: Implement circuit-breaker logic that can **selectively disable signing** for keys whose quorum includes compromised nodes while keeping unaffected flows operational.
  - **Rotation**: Complete cryptographically sound share refresh for all keys tied to compromised nodes within <4h (target) from containment decision; <2h for top-tier institutional clusters.
  - **Loss prevention**: Ensure **0 unauthorized signing events** resulting from share compromise in ≥99% of incidents (remaining cases require proof of minimization and root cause).
  - **Compliance**: Deliver initial incident notifications (regulators, auditors, major clients) within required windows – typically ≤72h for GDPR-reportable breaches and as defined by SOC 2 commitments [Source: ICO 72h guidance, 2024; Source: SOC 2 incident reporting guidance, Linford & Co, 2018].

- **Conditions / non-negotiables**:
  - No reconstruction of full private keys in any rotation workflow.
  - Refresh protocols must maintain security properties of deployed MPC schemes (e.g., threshold, robustness, identifiable aborts) [Source: MPC TSS literature summarized in Stackup, 2025].
  - Evidence preservation sufficient for audit and forensic review.
  - Incident workflows must be executable by 24/7 on-call engineers without deep cryptography knowledge (runbook-driven, tool-supported).

### 1.3 Extensibility & reframing

- **From “incident” to “lifecycle”**:
  - Reframe from a rare emergency to designing a **continuous key-share hygiene lifecycle**: periodic refresh, continuous monitoring, and rehearsed incident playbooks.
- **From “node compromise” to “share-exposure risk budget”**:
  - Instead of binary "compromised vs. safe", model **exposure risk per share over time** (age of share, environment risk, threat intel) and allocate refresh frequency accordingly [Estimate: based on risk-based key management practices].
- **From “security-only problem” to “joint security–operations–compliance”**:
  - Make incident response and rotation a cross-functional optimization problem balancing **risk, uptime, and regulatory posture**, not just crypto protocol behavior.

---

## 2. Internal Logical Relations (Aspect 2) 【Core】

### 2.1 Key elements

- **Roles**:
  - Security Operations (SOC/CSIRT): monitoring, triage, containment, coordination with infra teams [Source: NIST SP 800-61 Rev. 2, 2012].
  - MPC / cryptography engineers: design and validate refresh/rotation protocols, sign-off on tooling.
  - SRE/infra engineers: operate clusters, implement isolation, enforce circuit breakers.
  - Compliance & legal: interpret thresholds for notification, coordinate with regulators and auditors.
  - Institutional clients: consume incident communications, adjust their own risk posture.

- **Resources**:
  - MPC signing clusters (VMs, containers, HSMs, secure enclaves).
  - Monitoring stack (SIEM, EDR, IDS/IPS, cloud-native threat detection) [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Security Best Practices"].
  - Rotation tooling (PSS/refresh implementations, orchestration platform, audit logging).

- **Processes**:
  - Detection → analysis → containment → eradication → recovery → post-incident review [Source: NIST SP 800-61 Rev. 2, 2012].
  - Key-share refresh (scheduled hygiene) vs. emergency rotation.
  - Regulatory and client notification workflows (drafting, approvals, delivery).

- **Rules**:
  - Access-control and least-privilege policies on MPC nodes.
  - Approval thresholds for triggering rotation and disabling signing.
  - SLAs/SLIs for incident handling (RTO, RPO, max outage windows).

### 2.2 Balance & “degree”

- **Detection sensitivity vs. alert fatigue**:
  - Highly sensitive rules detect subtle exfiltration attempts but increase false positives and engineer fatigue; too strict thresholds miss attacks [Source: Halborn 2024 review of compromised accounts].
- **Forensics thoroughness vs. rotation speed**:
  - Deep memory and disk forensics can take days; a minimal-viable evidence package (logs, snapshots) may be enough to satisfy regulators if trade-offs are documented [Source: ICO 72h guidance, 2024; Source: SOC 2 incident reporting guidance, 2018].
- **Automation vs. human oversight**:
  - Full automation minimizes reaction times but risks over-triggering disruptive rotations; pure manual handling is too slow in worst-case incidents. A **human-in-the-loop model** (SOC approves high-confidence automated suggestions) is usually optimal.

### 2.3 Causal chains

1. **Weak MPC-specific monitoring → slow detection → higher threshold compromise risk**
   - Generic infra alerts (CPU, disk) rarely signal targeted memory scraping or key-share exfiltration.
   - Longer dwell time allows attackers to compromise additional nodes, crossing the k-of-n threshold.

2. **Manual, coordination-heavy rotation → extended exposure window**
   - If refresh requires all n parties online simultaneously, a single unavailable party can block the rotation, effectively giving attackers more time [Source: Offline Proactive Refresh, Silence Laboratories, 2024].

3. **Ambiguous incident ownership → delayed containment and notifications**
   - If it’s unclear whether SOC, crypto engineering, or compliance "owns" key decisions (e.g., shutting down a cluster, notifying regulators), decisions stall, widening the gap to the 72h GDPR clock and SOC 2 expectations [Source: ICO 72h guidance, 2024; Source: Linford & Co SOC 2 incident reporting, 2018].

---

## 3. External Connections (Aspect 3) 【Core】

### 3.1 Stakeholder map

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream (MPC protocol vendors, cloud providers, monitoring vendors) | Supply MPC SDKs/protocols, infra, and security tooling | Provide secure, high-availability services and libraries | Limited visibility into each custodian’s incident processes; competing product roadmaps | May under-prioritize incident-response features vs. performance/UX |
| Downstream (exchanges, institutions, DeFi protocols) | Rely on MPC custodians for key management and signing | Preserve asset safety, continuity, and regulatory compliance | Limited crypto/security expertise; depend heavily on custodian disclosures | May pressure providers to keep signing active even under suspicion |
| Sideline/external (regulators, auditors, insurers) | Evaluate custody risk and control effectiveness | Require timely, accurate incident reporting and evidence | Varying jurisdictions, limited MPC-specific expertise | May demand conservative controls that impact availability |

### 3.2 Environment factors

- **Regulatory**:
  - MiCA and other frameworks increasingly treat MPC-based custodians comparably to traditional custodians, demanding robust incident management and reporting [Source: MPC Wallets: A Complete Technical Guide, Stackup, 2025, "Regulatory Landscape"].
  - GDPR’s 72h reporting clock starts at **awareness**, not full forensic certainty, incentivizing well-defined detection and triage [Source: ICO 72h guidance, 2024].
  - SOC 2 and similar frameworks expect documented incident detection, escalation, and remediation procedures, with evidence in audits [Source: Linford & Co SOC 2 incident reporting, 2018].

- **Market**:
  - Institutional clients increasingly include **incident-response SLAs** and detailed IR questions in RFPs.
  - Insurance coverage (e.g., $10M–$150M crime/cyber policies) often requires proof of incident-handling capabilities [Source: Stackup MPC guide, 2025, "Compliance Considerations"].

- **Technology**:
  - Offline proactive refresh and PSS variants reduce coordination overhead for rotation, enabling more frequent refresh and faster emergency response [Source: Offline Proactive Refresh, Silence Laboratories, 2024].
  - Cloud-native observability and EDR provide fine-grained telemetry but require MPC-specific detections.

### 3.3 Responsibility & room

- **Where to take proactive responsibility**:
  - MPC custodians should own design and testing of **end-to-end incident and rotation runbooks**, not defer to vendors.
  - Major providers should collaborate on sector-wide guidelines for MPC incident handling to avoid inconsistent practices.

- **Where to leave flexibility**:
  - Allow client-specific choices around **risk appetite** (e.g., how aggressively to disable signing) as long as baseline controls meet regulatory and audit standards.
  - Permit multiple rotation protocols (e.g., online vs. offline refresh) provided they meet defined security and latency requirements.

---

## 4. Origins of the Problem (Aspect 4) 【Advanced】

### 4.1 Historical nodes

1. **2017–2020: Early MPC adoption without standardized IR**
   - Early MPC wallets focused on removing single points of failure vs. EOAs/multisig, with limited attention to node-specific IR and share rotation under compromise [Source: Stackup MPC guide, 2025, "What Is an MPC Wallet?"]; incident processes often copied from generic infra playbooks.

2. **2021–2023: Security incidents and near-misses**
   - Broader crypto incidents showed that compromised keys and signatures dominated losses, but guidance for MPC-specific incidents remained scarce [Source: Halborn 2024 security review].
   - Some providers discovered vulnerabilities during internal reviews, underscoring the need for audited protocols and structured IR [Source: Stackup MPC guide, 2025, "Security Incidents and Lessons Learned"].

3. **2023–2024: Proactive refresh research matures**
   - Offline proactive refresh and related PSS enhancements made **frequent, asynchronous share rotation** practical, but operational integration lagged [Source: Offline Proactive Refresh, Silence Laboratories, 2024].

4. **2024–2025: Regulatory clarity increases pressure**
   - SOC 2 incident-reporting guidance clarifies expectations; GDPR enforcement continues to highlight timing and documentation quality [Source: ICO 72h guidance, 2024; Source: Linford & Co SOC 2 incident reporting, 2018].

### 4.2 Background vs. direct causes

- **Background causes**:
  - Focus on cryptographic soundness and business features outpaced investment in **operational playbooks** and IR automation.
  - Underestimation of **partial-share compromise scenarios** (e.g., memory exfiltration without immediate fraud).

- **Direct causes**:
  - Lack of MPC-specific detections in SIEM/EDR (e.g., patterns tied to key-share processes).
  - Manual, ad hoc share rotation triggered only after clear fraud or severe infra compromise.
  - Fragmented ownership between security, infra, and crypto teams.

### 4.3 Root issues

- **Cultural**: IR and share hygiene treated as secondary to protocol design and product features.
- **Organizational**: No single, empowered owner accountable for MPC incident readiness across detection, rotation, and reporting.
- **Technical**: Limited productization of PSS/refresh into easy-to-use rotation tooling.

---

## 5. Problem Trends (Aspect 5) 【Core】

### 5.1 Current trajectory (if unchanged)

- **Incidents more frequent, more complex**:
  - As assets and adversary sophistication grow, attacks on MPC infrastructure (cloud workloads, supply chain, insiders) become more attractive [Source: Halborn 2024 security review].
- **Partial compromises accumulate silently**:
  - Without specific detections for share exfiltration and suspicious MPC node behavior, organizations may accumulate multiple undetected partial compromises.
- **Regulatory expectations harden**:
  - Auditors increasingly benchmark IR practices against NIST-style lifecycles and expect rehearsed playbooks for key compromise [Source: NIST SP 800-61 Rev. 2, 2012; Source: Linford & Co SOC 2 incident reporting, 2018].

### 5.2 Early signals

- Growing RFP questions about **key-loss scenarios, rotation times, and IR drills** from institutions.
- Security consultancies and insurers explicitly asking for **MPC-specific runbooks** and tabletop exercises.
- Research and vendor content highlighting proactive refresh and incident stories (e.g., Stackup’s incident section, Silence Labs offline refresh blog) show the topic’s rising prominence [Source: Stackup MPC guide, 2025; Source: Offline Proactive Refresh, 2024].

### 5.3 Scenarios (6–24 months)

- **Optimistic**:
  - Providers implement **automated MPC incident pipelines** with <30min detection, <4h rotation, and near-zero unauthorized signing events.
  - Sector-level best-practice documents for MPC IR become de facto standards.

- **Baseline**:
  - Leading custodians improve IR and rotation; smaller players lag, creating a **two-tier safety landscape**.
  - Most serious incidents are contained without large losses, but regulatory scrutiny intensifies after a few high-profile mishandled events.

- **Pessimistic**:
  - One or more large custodians suffer **threshold-level compromise** before rotation, leading to hundreds of millions in losses; regulators respond with stringent rules that may be misaligned with MPC operational realities [Source: Halborn 2024, lessons from major hacks].

---

## 6. Capability Reserves (Aspect 6) 【Advanced】

### 6.1 Existing strengths

- **Established SOC and IR practices**:
  - Many MPC custodians already operate 24/7 SOCs, with SIEM/EDR, playbooks, and on-call rotations aligned with standards like NIST SP 800-61 [Source: NIST SP 800-61 Rev. 2, 2012].
- **Cryptography expertise**:
  - Internal or vendor crypto teams understand PSS and threshold schemes, enabling design of safe rotation mechanisms.
- **Regulatory frameworks as guidance**:
  - GDPR and SOC 2 provide concrete timelines and documentation expectations; MiCA and similar regimes specify high-level custody control requirements [Source: ICO 72h guidance, 2024; Source: Stackup MPC guide, 2025].

### 6.2 Capability gaps

- **MPC-specific detection engineering**: Few organizations have custom detection content for MPC node behaviors and share exfiltration patterns.
- **Rotation orchestration**: Rotation often relies on scripts and manual coordination rather than robust, audited orchestration services.
- **Forensics readiness**: Lack of pre-defined logging baselines (e.g., what must be retained to reconstruct a key-share compromise timeline) hampers fast, defensible reporting.

### 6.3 Buildable capabilities (1–6 months)

- Develop and deploy **MPC-focused SIEM rules and EDR detections**, iteratively tuned using red-team exercises.
- Productize PSS/refresh into an internal **rotation service** with authenticated APIs, audit trails, and support for emergency and scheduled refresh.
- Establish a **forensics-and-compliance playbook** specifying what data to preserve, who signs off reports, and how to interface with regulators and clients.

---

## 7. Analysis Outline (Aspect 7) 【Advanced】

### 7.1 Structured outline

- **Background**: MPC wallets remove single points of failure but introduce distributed operational risk; current IR processes are mostly generic.
- **Problem**: Slow/uncertain detection of partial share compromise; slow and coordination-heavy rotation; risk of both asset loss and service disruption.
- **Analysis**: Stakeholder incentives, internal trade-offs (speed vs. certainty), protocol capabilities (PSS/offline refresh), and regulatory pressures.
- **Options**: Minimal uplift (tune existing IR), MPC-specific IR program with automated rotation, or full sector alignment on standardized MPC IR best practices.
- **Risks**: Misconfigured automation, over-rotation, under-notification or over-notification, and coordination failure in cross-org setups.

### 7.2 Key judgments (need validation)

1. **Automated, MPC-specific detection** can realistically achieve <30min median time-to-detect without unmanageable false positives.
2. **Offline proactive refresh** (or similar) can bring emergency rotation down to <4h end-to-end for most keys.
3. Regulators and auditors will accept **partial forensics** at time of initial notification if clearly documented and followed by full post-incident reports.

### 7.3 Alternative paths (one-line positioning)

- **Option A – Minimal uplift**: Reuse generic IR approaches, add a few manual runbooks.
- **Option B – MPC-specific IR program**: Build dedicated monitoring, rotation tooling, and drills for MPC incidents.
- **Option C – Sector collaboration**: Co-develop standardized MPC IR patterns and benchmarks with peers.

---

## 8. Validating the Answer (Aspect 8) 【Advanced】

### 8.1 Potential biases

- **Security-optimistic bias**: Overestimating how quickly new detections and rotation tooling can be rolled out across all environments.
- **Regulatory-tolerance bias**: Assuming regulators will be forgiving if timelines slip, even when clear guidance exists (e.g., 72h GDPR rule) [Source: ICO 72h guidance, 2024].
- **Automation overconfidence**: Underestimating edge cases where automation misfires (e.g., false compromise detection leading to unnecessary rotation).

### 8.2 Required intelligence

- Baseline **current detection and rotation times** from incident drills or historical events across representative clusters.
- Data on **false-positive/false-negative rates** for candidate MPC-specific detections.
- Legal/compliance interpretation of **breach-reportability thresholds** for partial key-share exposure vs. confirmed signing abuse.
- Vendor capabilities for **offline refresh and rotation orchestration** (what SLAs, what limits?).

### 8.3 Validation plan

- Run **tabletop exercises** and limited-scope technical drills simulating single-node compromise; measure detection, containment, and rotation times for top-tier keys [Source: NIST SP 800-61 Rev. 2, recommendations on exercises].
- Conduct a **red team** engagement focusing on MPC node compromise paths and share exfiltration; refine detections based on findings.
- Coordinate with legal/compliance and external counsel to **pre-approve notification templates and decision trees**, then review against actual incident rehearsals.

---

## 9. Revising the Answer (Aspect 9) 【Advanced】

### 9.1 Likely revisions

- **Detection feasibility**: As telemetry and red-team data accumulate, assumptions about achievable detection latency and signal quality may change.
- **Rotation SLAs**: Practical constraints (e.g., cross-region latency, external parties) may force revising <2h stretch goals for some clusters.
- **Notification practices**: Empirical experience with regulators and clients may suggest more conservative or more proactive communication patterns.

### 9.2 Incremental approach

- Phase 1 (0–3 months): Instrumentation and **MPC-specific detection content**, minimal emergency rotation tooling, initial tabletop exercises.
- Phase 2 (3–6 months): Hardened rotation orchestration with offline refresh support for critical keys, expanded drills, integration into SOC workflows.
- Phase 3 (6–12 months): Sector collaboration, cross-org exercises with key partners, refinement of metrics and governance.

### 9.3 “Good enough” criteria

- Median detection time <30min for critical MPC clusters, 90th percentile <60min.
- Verified emergency rotation for critical keys can complete <4h end-to-end in ≥2 rehearsed scenarios.
- All major regulators and auditors have received at least one satisfactory incident notification or simulation report demonstrating capability.

---

## 10. Summary & Action Recommendations (Aspect 10) 【Core】

### 10.1 Core insights

1. Key-share compromise in MPC environments is primarily an **operational and detection problem**, not a purely cryptographic one: current protocols already support safe rotation, but processes and tooling are lagging.
2. Without MPC-specific monitoring and rehearsed rotation workflows, organizations risk both **threshold compromise** and **regulatory breaches**, even when no immediate theft occurs.
3. Offline proactive refresh and NIST-style incident lifecycles provide a **practical blueprint** for reducing detection and rotation times while preserving evidence.
4. A phased program with clear metrics (detection, containment, rotation, notification) is essential to make progress measurable and auditable.

### 10.2 Near-term action list (0–3 months)

1. **【P0 – Critical】 Define and implement MPC-specific incident runbooks**  
   → Owner: Head of Security Operations  
   → Metric: Runbooks covering ≥90% of MPC incident scenarios (single-node compromise, multi-node suspicion, cloud account breach) approved and published; at least 1 tabletop exercise executed per scenario  
   → Date: 2025-03-31

2. **【P0 – Critical】 Instrument MPC clusters with dedicated detections and circuit breakers**  
   → Owner: SOC Lead + SRE Lead  
   → Metric: ≥10 high-quality MPC-focused SIEM/EDR rules deployed; automated circuit-breaker for compromised-node keys available in staging and one production environment; median detection time in tests <30min  
   → Date: 2025-04-30

3. **【P1 – Important】 Deploy rotation orchestration with offline proactive refresh for critical keys**  
   → Owner: Cryptography Engineering Lead  
   → Metric: Emergency rotation path for top 20% highest-value MPC keys can be executed <4h door-to-door in rehearsal; offline refresh available for at least one production cluster  
   → Date: 2025-06-30

4. **【P1 – Important】 Align notification workflows with GDPR and SOC 2 expectations**  
   → Owner: Compliance Lead  
   → Metric: Decision tree and templates for regulator, auditor, and client notifications prepared and legally reviewed; dry-run completed; documented mapping to GDPR Article 33 and SOC 2 criteria  
   → Date: 2025-05-31

5. **【P2 – Optional】 Engage peers and vendors on MPC IR best practices**  
   → Owner: CISO or Head of Risk  
   → Metric: Participation in ≥1 industry working group or informal roundtable on MPC incident response and key rotation; shared anonymized metrics with at least 2 peers  
   → Date: 2025-09-30

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Detection rules generate high false positives | Medium–High | Medium | SOC overwhelmed by MPC alerts; frequent "false" incidents | Iteratively tune rules with red-team input; prioritize high-confidence signals; adopt tiered alerting | SOC Lead |
| Rotation tooling introduces new vulnerabilities | High | Medium | Security review finds flaws in refresh orchestration or offline refresh integration | Commission independent crypto/security reviews; use defense-in-depth (rate limits, strong auth, audit trails); gradual rollout | Cryptography Engineering Lead |
| Regulatory misalignment on partial share exposure | High | Low–Medium | Regulator deems late or insufficient notification for partial compromise | Pre-brief regulators and auditors on approach; document decision criteria; err on side of earlier notifications when in doubt | Compliance Lead |
| Operational overload during major incident | High | Medium | Multiple incidents or infra issues coincide with MPC compromise | Establish cross-functional incident command structure; pre-assign roles; run large-scale simulations; maintain surge capacity | Incident Commander (CISO delegate) |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Minimal uplift (tune generic IR)** | Low upfront cost; quick to implement | Limited MPC-specific coverage; rotation remains manual and slow | High risk of threshold compromise and regulatory shortfalls | Very small custodians with low AUM, short time horizon | Institutional-scale custodians with regulatory exposure |
| **B. MPC-specific IR program (recommended)** | Balanced improvement in detection, rotation, and reporting; measurable metrics | Moderate investment in tooling, training, and exercises | Implementation complexity; requires cross-team buy-in | Mid–large custodians aiming for strong risk posture and auditor confidence | Organizations unwilling to invest in SOC and crypto collaboration |
| **C. Aggressive full automation** | Fastest reaction times; minimal human latency | High engineering cost; complex safety mechanisms | Over-rotation, outages due to false positives; difficult regulator explanations | Environments with extreme risk tolerance for security events and strong SRE maturity | Regulated environments where explainability and human oversight are required |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **MPC (Secure Multi-Party Computation)** | Cryptographic techniques enabling multiple parties to jointly compute a function (e.g., a digital signature) without revealing their private inputs | N/A | Used as core architecture for MPC wallets [Source: Stackup MPC guide, 2025] |
| **Threshold property** | Requirement that at least k-of-n parties cooperate to produce a valid signature or reconstruct a secret | N/A | Fundamental security property for MPC/TSS wallets |
| **Key share** | A fragment of a private key held by an MPC party; individually useless for signing but jointly usable under threshold protocols | N/A | Compromise of multiple shares can enable unauthorized signing |
| **Share rotation / refresh** | Process of cryptographically updating key shares (often via PSS) so old shares become invalid, without reconstructing the full private key | N/A | Mitigates risk from historical share compromise [Source: Stackup MPC guide, 2025] |
| **Proactive Secret Sharing (PSS)** | Class of protocols that periodically refresh secret shares while preserving the underlying secret, invalidating old share material | N/A | Basis for share rotation in MPC infrastructures |
| **Offline proactive refresh** | Variant of PSS where only a quorum of parties must be online for refresh, and others can catch up later using refresh packets | N/A | Reduces coordination overhead; resists DoS by uncooperative parties [Source: Offline Proactive Refresh, Silence Laboratories, 2024] |
| **RTO (Recovery Time Objective)** | Target time to restore normal or acceptable service after an incident | Time (hours) | Used to define acceptable downtime for signing services |
| **IOC (Indicator of Compromise)** | Observable artifact indicating a potential security breach (e.g., suspicious process, anomalous network connection, unexpected memory scan) | N/A | Key input for SIEM/EDR detections [Source: NIST SP 800-61 Rev. 2, 2012] |
| **SIEM (Security Information and Event Management)** | System aggregating and analyzing logs and security events from multiple sources to detect threats | N/A | Central platform for MPC-specific detection content |
| **EDR (Endpoint Detection and Response)** | Security tooling that monitors endpoints (servers, workstations) for malicious activity and supports investigation and response | N/A | Used to detect suspicious behavior on MPC nodes [Source: general EDR best practices summarized in NIST SP 800-61] |
| **Tabletop exercise** | Discussion-based simulation of an incident where stakeholders walk through response steps without changing live systems | N/A | Recommended by NIST and ICO for testing incident readiness |
| **GDPR (General Data Protection Regulation)** | EU regulation governing personal data protection; includes 72h breach notification requirement to supervisory authorities | N/A | Drives incident notification timelines [Source: ICO 72h guidance, 2024] |
| **SOC 2** | Audit framework for service organizations assessing controls over security, availability, processing integrity, confidentiality, and privacy | N/A | Requires documented incident detection and reporting processes [Source: Linford & Co, SOC 2 guidance, 2018] |

---

## 12. References

### Tier 1 – Standards & Official Guidance

1. **Cichonski, P., Millar, T., Grance, T., & Scarfone, K.** (2012). *NIST Special Publication 800-61 Revision 2: Computer Security Incident Handling Guide*. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r2  **[Cited in: Context, 2.1, 3.2, 6.1, 8.3]**
2. **Information Commissioner’s Office (ICO).** (2024). *72 hours – how to respond to a personal data breach*. https://ico.org.uk/for-organisations/advice-for-small-organisations/personal-data-breaches/72-hours-how-to-respond-to-a-personal-data-breach/  **[Cited in: Context, 2.3, 3.2, 4.1, 5.2, 8.1]**
3. **Information Commissioner’s Office (ICO).** (2024). *Personal data breaches: a guide*. https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/  **[Cited in: 3.2, 4.2, 10.2]**

### Tier 2 – Industry Reports & Technical Guides

4. **Stackup.** (2025). *MPC Wallets: A Complete Technical Guide (2025)*. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide  **[Cited in: Context, 2.1, 3.2, 4.1, 6.1, 11]**
5. **Halborn.** (2024). *2024 Blockchain Security in Review: Key Lessons Learned*. https://www.halborn.com/blog/post/2024-blockchain-security-in-review-key-lessons-learned  **[Cited in: Context, 2.2, 4.1, 5.1, 5.3]**
6. **Silence Laboratories.** (2024). *Offline Proactive Refresh: Strengthening Threshold Signature Wallets*. https://silencelaboratories.com/blog-posts/offline-proactive-refresh-strengthening-threshold-signature-wallets  **[Cited in: Context, 2.2, 3.2, 4.1, 6.2, 10.2, 11]**
7. **Linford & Company LLP.** (2018). *SOC Incident Reporting: What are SOC 2 Security Reporting Requirements?* https://linfordco.com/blog/soc-2-reporting-criteria-cyber-information-security-incidents/  **[Cited in: Context, 2.3, 3.2, 4.1, 5.1, 6.1, 10.2, 11]**

### Estimates & Assumptions

8. **Operational metrics and cost estimates for MPC incidents.** Method: Derived from problem statement baselines, public crypto incident analyses (e.g., Halborn 2024), and typical SOC/IR practice benchmarks (NIST SP 800-61). Confidence: Medium. Validation: Run internal tabletop exercises and collect anonymized metrics across 3–5 incidents or simulations. **[Used in: Context, 1.1, 2.2, 5.1, 9.3]**
