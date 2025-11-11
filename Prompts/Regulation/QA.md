# Regulatory Compliance Interview Q&A Generator

Generates 25-30 interview Q&As mapping regulatory obligations to implementation across 7 stakeholder perspectives: Legal, Compliance, Security, Architecture, Product, Executive, Audit.

---

## Specifications

### Scope
- **Count**: 25-30 Q&As (20% Foundational, 40% Intermediate, 40% Advanced)
- **Answer Length**: 150-300 words
- **Coverage**: 6 topic clusters × 7 stakeholder perspectives (MECE)
- **Visuals**: Per cluster: ≥1 diagram + ≥1 table + ≥1 metric
- **Analysis**: Trace legal obligations → policy → controls → design → UX; assess risks; coordinate cross-functionally

### Content Requirements
- **Regulatory Scope**: Privacy laws (GDPR, CCPA, PIPL, LGPD), sector regulations (HIPAA, PCI-DSS, SOX), standards (ISO 27001/27701, SOC2, NIST CSF), data rights, breach notification, cross-border transfer, vendor risk
- **Framework Comparisons**: Compare by jurisdiction (EU/US/APAC) and sector (financial/healthcare); distinguish mandatory vs recommended
- **Stakeholder Perspectives**: Legal (laws, penalties), Compliance (audit, certification), Security (threats, controls), Architecture (technical mapping), Product (UX, rights), Executive (risk, budget), Audit (trails, evidence)

### Visual Standards

| Analysis Type | Diagram | Metric Formula | Standard |
|---------------|---------|----------------|----------|
| **Compliance Modeling** | Control matrix, Gap analysis | `Implemented / Required × 100%` | NIST, ISO 27001 |
| **Risk & Threat** | Threat model, Risk matrix | `Likelihood × Impact × Asset Value` | STRIDE, DREAD |
| **Privacy** | Data flow, Consent flow | `Explicit Consent / Total × 100%` | GDPR, Privacy-by-Design |
| **Audit** | Audit trail, Evidence mapping | `Auditable / Critical Events × 100%` | SOC2, ISO 19011 |
| **Architecture** | Regulation→Control, Security arch | `Remediation / System Cost × 100%` | C4, UML |
| **Remediation** | Roadmap, Timeline | `TCO = Initial + Ongoing + Penalty Risk` | Gantt, NIST |
| **Coordination** | RACI, Decision flow | `Aligned / Total Stakeholders × 100%` | Custom |

**Diagram Standards**: BPMN (process), UML (structure), C4 (software), ERD/DFD (data), ArchiMate (enterprise)

**Rendering**: Mermaid (GitHub-native), inline math `$formula$`, block `$$formula$$`

**Anti-patterns**: Mega-diagrams (>120 nodes), mixed abstraction, missing rationale

### References & Quality Gates

| Section | Minimum | Requirements |
|---------|---------|--------------|
| **Glossary** | ≥18 | Privacy laws (GDPR, CCPA, PIPL, LGPD), sector regs (HIPAA, PCI-DSS, SOX), standards (ISO 27001/27701, SOC2, NIST CSF), concepts (Privacy-by-Design, Zero Trust), rights (Erasure, Access), data types (PHI, PII), controls (Encryption, Audit Trail), cross-border (SCCs, BCRs), vendor (BAA, DPA) |
| **Tools** | ≥6 | Compliance (OneTrust, TrustArc), GRC (ServiceNow, Archer), SIEM (Splunk), scanning (Nessus, Qualys), policy (Vanta, Drata) |
| **Literature** | ≥8 | Regulatory texts (GDPR, HIPAA, PCI-DSS), standards (NIST SP 800-53, ISO 27001), frameworks (SOC2, NIST CSF), guidance (CIS, OWASP) |
| **Citations** | ≥12 | APA 7th, ~60% EN / ~30% ZH / ~10% other, inline [Ref: ID] |

**Quality Gates**:
- Recency: ≥50% last 3yr (≥80% privacy laws)
- Diversity: ≥3 source types, max 25% single type
- Citation Coverage: ≥70% answers with ≥1, ≥30% with ≥2
- Links: Validate accessibility, prefer official
- Per Cluster: ≥1 diagram + ≥1 table + ≥1 metric + ≥2 regulatory sources + ≥1 tool

### Validation Checklist

Execute all checks. Fix failures before submission.

| # | Check | Target | Status |
|---|-------|--------|--------|
| 1 | Floors | G≥18, T≥6, L≥8, A≥12, Q=25-30 (20/40/40) | ☐ |
| 2 | Citations | ≥70% with ≥1, ≥30% with ≥2 | ☐ |
| 3 | Language | EN 50-70%, ZH 20-40%, Other 5-15% | ☐ |
| 4 | Recency | ≥50% last 3yr (≥80% privacy) | ☐ |
| 5 | Diversity | ≥3 types, max 25% | ☐ |
| 6 | Links | All accessible | ☐ |
| 7 | Cross-refs | All [Ref: ID] resolve | ☐ |
| 8 | Word count | Sample 5, all 150-300 | ☐ |
| 9 | Insights | Concrete (gap/violation/failure) | ☐ |
| 10 | Per-topic | ≥2 regulatory + ≥1 tool | ☐ |
| 11 | Reg-tech | ≥80% explicit mapping | ☐ |
| 12 | Judgment | ≥70% scenario-based | ☐ |
| 13 | Visuals | ≥90% diagram + table + metric | ☐ |
| 14 | Frameworks | ≥80% apply standards | ☐ |
| 15 | Metrics | ≥60% quantitative analysis | ☐ |
| 16 | Coordination | ≥50% cross-functional | ☐ |

---

## Workflow

1. **Plan Topics**: 5-6 clusters (Compliance, Risk, Privacy, Audit, Architecture, Remediation), 4-6 Q&As each, 25-30 total, 20/40/40 difficulty
2. **Collect References**: Meet minimums (G≥18, T≥6, L≥8, A≥12), assign IDs, tag languages
3. **Generate Q&As**: Scenario-based, 150-300 words, trace obligations→UX, cite [Ref: ID], state concrete insight
4. **Create Visuals**: Per cluster: diagram + table + metric (Mermaid format)
5. **Validate**: Execute 16 checks, fix failures, re-run until all pass

---

## Quick Prompts

**Control Matrix**: Map [Frameworks] to [System]. Columns: Framework | Req | Control | Evidence | Owner. Coverage: `Implemented/Required × 100%`

**DPIA**: [Activity]: description, necessity, risks, mitigations, residual risk. Add risk matrix

**ROPA**: Processing | Purpose | Legal Basis | Data | Subjects | Recipients | Transfers | Retention | Security

**Cross-Border**: SCC/TIA for [Flow to Country]: law, safeguards, adequacy, encryption. Cite EDPB/SCCs

**DPA/BAA**: Purpose, confidentiality, sub-processors, security, audits, breach, deletion, liability

**Audit Log**: Control | Evidence | Source | Periodicity | Owner. Schema: who/what/when/where

**Breach Notice**: By jurisdiction (GDPR, CPRA, PIPL, LGPD): thresholds, timelines, contacts, regulators

**Reg→Arch**: Map obligations to controls/components (C4). Output: table + diagram + metrics

**Rights**: Endpoints/UI for consent, access, erasure, portability, rectification. SLAs, verification, evidence

**Retention**: Data classes, periods, deletion workflows, backup exclusions, crypto-erasure schedule

**Metrics**: Control Coverage, Audit Coverage, Consent Rate, MTTR, Compliance Debt, TCO (formulas + examples)

**RACI**: [Program]: Legal, Compliance, Security, Architecture, Product, Executive, Audit. Decision flows

---

## Output Format

### Question Quality Criteria

**Approach**: Regulatory Mapping → Risk & Threat → Audit & Evidence → Stakeholder Coordination → Implementation Trace

**Design Principles**:
- **Clarity**: Single unambiguous ask (✅ "Translate GDPR Art. 17 into SaaS architecture" vs ❌ "Explain GDPR")
- **Signal**: Test translation, not trivia (✅ "SOC2 Type II in 6mo. Arch changes?" vs ❌ "List NIST CSF functions")
- **Depth**: Enable trade-offs (✅ "Encryption layer for HIPAA PHI. Decide how?" vs ❌ "Encrypt data?")
- **Realism**: Senior/expert scenarios (✅ "30-day deletion + append-only logs. Navigate?" vs ❌ "Design payment system")
- **Discriminative**: Judgment over recall (✅ "When data residency > cloud cost?" vs ❌ "What is data residency?")
- **Role Alignment**: Senior (tactical), Arch/Sec (controls), Compliance/Legal (policy), Product (UX), Exec (strategic)

### Template Structure

```markdown
## Contents
- [Topic Areas](#topic-areas) - Topic | Range | Count | Mix
- [Topics 1-6](#topics) - Q&As with artifacts
- [References](#references) - Glossary, Verification, Tools, Literature, Citations

## Topic Areas
| Topic | Range | Count | Mix (F/I/A) |
| Compliance Modeling | Q1-Q5 | 5 | 1/2/2 |
| Risk & Threat | Q6-Q10 | 5 | 1/2/2 |
| Privacy | Q11-Q15 | 5 | 1/2/2 |
| Audit | Q16-Q20 | 5 | 1/2/2 |
| Architecture | Q21-Q25 | 5 | 1/2/2 |
| Remediation | Q26-Q30 | 5 | 1/2/2 |

## Q[N]: [Question]
**Difficulty**: [F/I/A] | **Type**: [Topic] | **Insight**: [Gap/violation/failure]

**Answer**: [150-300 words, [Ref: ID], trace obligations→UX]

**Artifacts**: Diagram (Mermaid) + Table + Metric
```

---

## References

### Glossary (≥18 Terms)

**Laws**: GDPR (EU 2016/679: principles, rights, penalties €20M/4% revenue), CCPA/CPRA (CA privacy), PIPL (China data protection), LGPD (Brazil), HIPAA (US PHI protection), PCI-DSS (cardholder data v4.0), SOX (financial reporting Sec 302/404/802)

**Standards**: ISO 27001/27701 (ISMS, 93 controls), SOC2 (AICPA trust criteria Type I/II), NIST CSF 2.0 (6 functions), NIST SP 800-53 (1100+ controls), FedRAMP (cloud)

**Concepts**: Privacy-by-Design (7 principles), Zero Trust (NIST 800-207), Controller/Processor (GDPR roles), PHI/PII (identifiable data), Encryption at Rest/Transit (AES-256, TLS 1.2+), Audit Trail (who/what/when/where)

**Rights**: Erasure (GDPR Art. 17), Access, Portability, Rectification, Consent

**Controls**: DPIA (Art. 35 impact assessment), ROPA (Art. 30 processing records), DPO (Art. 37-39), SCCs (standard contractual clauses), BCRs (binding corporate rules), DPA/BAA (data processing/business associate agreements)

**Architecture**: Data residency/sovereignty, Multi-region, Pseudonymization, Crypto-erasure, Retention policies, Breach notification

### Verification Sources

**Official**: EUR-Lex, Federal Register, Regulators, ISO/IEC, NIST, PCI SSC, AICPA  
**Tools**: OneTrust DataGuidance, TrustArc, IAPP, NIST Catalog  
**Legal**: LexisNexis, Westlaw, Official gazettes

### Tools (≥6)

**T1. OneTrust**: Privacy/GRC (data mapping, consent, DSR, cookies). GDPR, CCPA, HIPAA. SOC2, ISO 27001. https://www.onetrust.com [EN]

**T2. ServiceNow GRC**: Risk, compliance, audit, policy, vendor. NIST, ISO 27001, SOC2. https://www.servicenow.com [EN]

**T3. Vanta**: Compliance automation (SOC2, ISO 27001, HIPAA, PCI-DSS, GDPR). https://www.vanta.com [EN]

**T4. Splunk**: SIEM (threat, incident, compliance). GDPR Art. 32, HIPAA §164.312(b), PCI-DSS Req 10. https://www.splunk.com [EN]

**T5. Nessus**: Vulnerability scanning (75K+ plugins). PCI-DSS ASV, NIST, CIS. https://www.tenable.com/products/nessus [EN]

**T6. TrustArc**: Privacy platform (assessments, consent, DSR). 100+ laws. https://trustarc.com [EN]

### Literature (≥8)

**L1.** EU. (2016). GDPR (2016/679). 99 articles, penalties €20M/4% [EN]

**L2.** NIST. (2020). SP 800-53 Rev. 5. 1,100+ controls, 20 families [EN]

**L3.** ISO/IEC. (2022). ISO 27001:2022. 93 controls, 4 themes [EN]

**L4.** PCI SSC. (2022). PCI-DSS v4.0. 12 requirements, 6 objectives [EN]

**L5.** HHS. (2013). HIPAA Security Rule (45 CFR 164). Admin, physical, technical safeguards [EN]

**L6.** AICPA. (2017). SOC 2 TSC. 5 principles (security, availability, integrity, confidentiality, privacy) [EN]

**L7.** NIST. (2024). CSF 2.0. 6 functions, 23 categories, 108 subcategories [EN]

**L8.** OWASP. (2021). Top 10. Web security risks [EN]

### Citations (≥12, APA 7th, Language Tags)

**A1.** EU. (2016). GDPR. https://eur-lex.europa.eu/eli/reg/2016/679/oj [EN]  
**A2.** NIST. (2020). SP 800-53 Rev. 5. https://doi.org/10.6028/NIST.SP.800-53r5 [EN]  
**A3.** ISO/IEC. (2022). ISO 27001:2022 [EN]  
**A4.** PCI SSC. (2022). PCI-DSS v4.0. https://www.pcisecuritystandards.org [EN]  
**A5.** HHS. (2013). HIPAA Security Rule. https://www.hhs.gov/hipaa [EN]  
**A6.** AICPA. (2017). SOC 2 TSC [EN]  
**A7.** NIST. (2024). CSF 2.0. https://doi.org/10.6028/NIST.CSWP.29 [EN]  
**A8.** OWASP. (2021). Top 10. https://owasp.org/Top10/ [EN]  
**A9.** 信标委. (2020). GB/T 35273-2020 [ZH]  
**A10.** Cavoukian, A. (2011). Privacy by Design. https://www.ipc.on.ca [EN]  
**A11.** Rose et al. (2020). NIST SP 800-207 Zero Trust. https://doi.org/10.6028/NIST.SP.800-207 [EN]  
**A12.** CIS. (2021). CIS Controls v8. https://www.cisecurity.org/controls/v8 [EN]  
**A13.** CAC. (2021). Data Security Law [ZH]  
**A14.** EDPB. (2020). Guidelines 4/2019 Art. 25. https://edpb.europa.eu [EN]  
**A15.** Shostack, A. (2014). Threat Modeling. Wiley [EN]  
**A16.** Howard & LeBlanc. (2003). Writing Secure Code. Microsoft Press [EN]  
**A17.** CPPA. (2023). CPRA Regulations. https://cppa.ca.gov [EN]  
**A18.** EU Commission. (2023). EU-US Data Privacy Framework [EN]

---

## Example

### Q1: Translate GDPR right to erasure (Art. 17) into architecture for multi-tenant healthcare SaaS (HIPAA compliant)?

**Difficulty**: Advanced | **Type**: Compliance, Privacy, Architecture | **Insight**: Exposes GDPR deletion vs HIPAA retention conflict

**Answer** (280 words):

**Regulatory Mapping**: GDPR Art. 17 mandates erasure "without delay" [Ref: A1, G1]. HIPAA requires 6yr PHI retention [Ref: A5, G2]. **Resolution**: GDPR Art. 17(3)(b) exempts erasure for legal obligations [Ref: A14].

**Privacy Architecture**: Pseudonymization [Ref: G6]: separate PII from PHI. Erasure deletes PII, retains pseudonymized PHI. Data inventory: classify PII/PHI, map processing, document legal bases [Ref: T1, A10].

**Risk Model**: Legal: €20M GDPR / $1.5M HIPAA fines. Technical: incomplete deletion (backups, logs), propagation delays, proof auditing [Ref: A15]. Sovereignty: EU data residency [Ref: G15].

**Architectural Controls**: (1) Data lifecycle: retention policies, deletion workflows, audit logs [Ref: G9, T4]; (2) Multi-region: EU data isolation; (3) Crypto-erasure: key destruction [Ref: G10]; (4) Audit trail: tamper-evident deletion proof; (5) Minimization: automated purging [Ref: A1, A14].

**Implementation**: PostgreSQL row-level security, event sourcing, Kafka propagation, Vault key mgmt, Terraform IaC [Ref: A16, T2].

**Stakeholder RACI**: Legal (A: policy, interprets 17(3)(b)), Compliance (C: DPAs, evidence [T1]), Security (R: encryption, keys [T4]), Architecture (R: pseudonymization, multi-region [A11]), Product (R: deletion UI), Executive (A: $600K budget, €700K residual risk).

**Artifacts**:
```
GDPR Art. 17 → HIPAA §164.530 → Pseudonymization → Deletion API + Crypto-erasure
Risk: €14M annual → Controls (95% effective) → Residual: €700K
Coverage: 95% PII deletable, 100% PHI retained, 100% EU data isolated
Roadmap: M1-3 (classify), M4-6 (workflows), M7-9 (audit), M10-12 (monitoring)
```

---
