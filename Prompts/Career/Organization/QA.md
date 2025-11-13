# Organization & Team Building Interview Q&A Generator

Generate 25-30 interview Q&As for senior/leadership roles demonstrating org design, talent acquisition, team building across full software lifecycle.

## Scope

**Audience**: Engineering Managers, Directors, VPs, CTOs, Architects, Team Leads  
**Context**: Production distributed systems (>10K rps, >1TB data); teams 10-100 engineers; cloud-native; regulated  
**Success**: 21/21 validation PASS

**Lifecycle (8)**: Requirements & Discovery → Architecture & Design → Development → Testing & Quality → Deployment & Release → Operations & Observability → Maintenance & Support → Evolution & Governance

**Stakeholders (10)**: BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead

## Requirements

**Q&A Specs**: 25-30 total; 20/40/40% F/I/A difficulty; 200-350 words; structure: Context → Strategy → Framework → Metrics → Trade-offs; ≥1 citation (≥2 complex); each cluster: diagram + framework + table + formula

**Dimensions (6, 4-6 Q&As each)**:
1. **Team Structure**: Topologies, Conway's Law, cognitive load
2. **Talent Acquisition**: Sourcing, interviewing, competency frameworks, diversity
3. **Team Development**: Onboarding, ladders, mentoring, retention
4. **Culture & Process**: Psychological safety, blameless culture, Agile/DevOps
5. **Resource Management**: Capacity, budget, ROI, headcount
6. **Change & Scaling**: Restructuring, scaling patterns, migrations

**Coverage**: All 8 lifecycle phases ≥2 Q&As; all 10 stakeholders ≥2 Q&As

**Standards**:
- **Traceability**: Business Need → Org Strategy → Team Design → Hiring Plan → Metrics
- **Quantified**: ✅ "7±2 people, 30% autonomy ↑, 20% overhead ↑" ❌ "Small teams work"
- **Context Thresholds**: Team Size: <10/10-50/50-200/>200; Growth: <20%/20-100%/>100% YoY; Turnover: <10%/10-20%/>20%; Stage: Seed-A/B-D/IPO+/Mature
- **Balance**: ≥2 approaches + table; assumptions/limitations; tag [Consensus]/[Context-dependent]/[Emerging]
- **Precision**: Define jargon inline; consistent terms; concrete metrics

## Artifacts (Per Dimension)

| Artifact | Format | Requirements |
|----------|--------|--------------|
| **Diagram** | Mermaid (<120 nodes) | Org chart/topology/funnel/roadmap |
| **Framework** | Established model + citation | Team Topologies, RACI, DORA, Spotify, Two-Pizza, Tuckman, OKRs, 70-20-10 |
| **Metrics** | Formula + variables + target + source | `Cognitive Load = Dependencies / Team Size` |
| **Trade-offs** | Table (≥2 approaches) | Approach/Pros/Cons/Use When/Consensus |

## Lifecycle-Stakeholder Matrix

| Phase | Key Questions | RACI |
|-------|---------------|------|
| 1. Requirements | Validation structure? Skills? | BA (R), PM (A), Arch (C) |
| 2. Architecture | Architect capacity? Review? Collaboration? | Arch (R/A), Dev (C), Sec (C), SRE (C) |
| 3. Development | Team size? Pairing? Review SLAs? Onboarding? | Dev (R/A), QA (C) |
| 4. Testing | QA structure? Automation? Ownership? Career? | QA (R/A), Dev (C) |
| 5. Deployment | DevOps topology? On-call? Windows? Burnout? | DevOps (R/A), SRE (C) |
| 6. Operations | SRE sizing? Incident response? Compensation? | SRE (R/A), DevOps (C) |
| 7. Maintenance | Support tiers? Knowledge transfer? Staffing? | SRE (R), Sec (R), Data (C) |
| 8. Evolution | Change approval? Steering? Roadmap? Succession? | PM (R), Arch (R), Lead (A) |

## References

| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary** | ≥12 | Org/hiring/team terms + relationships + lifecycle phases |
| **Tools** | ≥6 | URL (valid), updated ≤18mo, pricing, adoption |
| **Literature** | ≥8 | Authoritative books (Skelton, Lencioni, Kim, McChrystal, Adkins, Fournier, Edmondson) |
| **Citations** | ≥15 | APA 7th; 60/30/10% EN/ZH/Other (±10%); ≥50% last 5yr (≥60% org); 100% valid URLs |

## Generation Process

1. **Plan**: 5-6 clusters → 4-6 Q&As/cluster (25-30 total) → 1F/2I/2A each → map to 8 phases + 10 stakeholders → verify totals
2. **References**: Glossary (≥12) + Tools (≥6) + Literature (≥8) + Citations (≥15) → verify quality
3. **Write**: ≥70% judgment questions → 200-350 words → Context → Strategy → Framework → Metrics → Trade-offs → ≥1 citation → lifecycle/stakeholder linkage → validate every 5
4. **Artifacts**: Per cluster: Mermaid + Framework + Table + Formula → verify all 4/4
5. **Link**: Populate sections → verify all [Ref: ID] resolved → remove orphans → validate URLs
6. **Validate**: 21 checks → ANY fail = STOP → fix → re-validate → iterate until 21/21 PASS

## Validation (21 Checks)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥12, T≥6, L≥8, A≥15, Q=25-30 (20/40/40%) |
| 2 | Citations | ≥70% Q&As ≥1; ≥30% ≥2 |
| 3 | Language | 60/30/10% EN/ZH/Other (±10%) |
| 4 | Recency | ≥50% last 5yr (≥60% org) |
| 5 | Diversity | ≥3 types; <25% single |
| 6 | Links | 100% valid |
| 7 | Cross-refs | 100% resolved |
| 8 | Word count | Sample 5: 200-350 |
| 9 | Insights | 100% quantified |
| 10 | Per-topic | ≥2 sources + ≥1 tool |
| 11 | Traceability | ≥80% need→strategy→metrics |
| 12 | Question type | ≥70% judgment |
| 13 | Artifacts | ≥90% clusters 4/4 |
| 14 | Frameworks | ≥80% use frameworks |
| 15 | Metrics | ≥60% have metrics |
| 16 | Diagrams | ≥80% have diagrams |
| 17 | Syntax | 100% valid |
| 18 | Formulas | 100% valid |
| 19 | Lifecycle | All 8 phases ≥2 Q&As |
| 20 | Stakeholders | All 10 roles ≥2 Q&As |
| 21 | Review | 6/6: Clarity, Accuracy, Completeness, Balance, Practicality, Self-Correction |

**Submit When**: 21/21 PASS + 6/6 review criteria

---

# Output Template

```markdown
## Contents
[TOC: Topics | Q&As | Lifecycle-Stakeholder Matrix | References | Validation]

## Topic Areas
| Cluster | Dimension | Range | Count | Difficulty |
| [Title] | [Type] | Q1-Q5 | 5 | 1F/2I/2A |

## Lifecycle-Stakeholder Coverage
| Phase | Q# | Stakeholders |
| 1. Requirements & Discovery | Q1, Q5 | BA, PM, Arch |
[All 8 phases ≥2 Q&As, all 10 stakeholders ≥2 Q&As]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences] | **Phase**: [1-8] | **Stakeholders**: [Roles]

### Q1: [How/When/Compare question]
**Difficulty**: [F/I/A] | **Dimension**: [Type] | **Phase**: [1-8] | **Stakeholders**: [Roles]

**Key Insight**: [Quantified trade-off in one sentence]

**Answer**: [200-350 words: Context → Strategy → Framework → Metrics → Trade-offs → Lifecycle linkage] [≥1 citation [Ref: A1]]

**Framework**:
```mermaid
[Org chart / Topology / Funnel / Roadmap, <120 nodes]
```

**Metrics**:
| Metric | Formula | Variables | Target | Source |
| [Name] | [Expression] | [Definitions] | [Threshold] | [Where] |

**Trade-offs**:
| Approach | Pros (Quantified) | Cons (Quantified) | Use When | Consensus |
| [Option] | [Metrics] | [Metrics] | [Context] | [Tag] |

**Lifecycle Integration**: [How this affects phases]
**Stakeholder Impact**: [How this affects roles]

---

## References

### Glossary (≥12)
**G1. [Term]** [EN/ZH/Other] – [Definition]. **Related**: [Terms]. **Lifecycle**: [Phases]

### Tools (≥6)
**T1. [Tool]** [Tag] – **Purpose**: [Desc]. **Updated**: [YYYY-MM]. **Pricing**: [Type]. **Adoption**: [Metrics]. **URL**: [Link]

### Literature (≥8)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – **Relevance**: [Why]

### Citations (≥15, APA 7th)
**A1.** Author(s). (Year). *Title*. Source. [EN/ZH/Other]

---

## Validation Report
| # | Check | Target | Result | Status |
| 1 | Counts | G≥12, T≥6, L≥8, A≥15, Q=25-30 | G:X, T:Y... | PASS/FAIL |
[All 21]

**Overall**: [X/21 PASS] | **Issues**: [Failures] | **Remediation**: [Actions]
```

# Reference Examples

## Glossary
**G1. Team Topologies** [EN] – Four team types: stream-aligned, platform, enabling, complicated-subsystem. Optimizes flow/cognitive load. **Related**: Conway's Law, Cognitive Load. **Lifecycle**: All  
**G2. Conway's Law** [EN] – Organizations design systems mirroring communication structure. **Related**: Team Topologies. **Lifecycle**: Architecture, Development  
**G3. Two-Pizza Team** [EN] – Team size 7±2 people. Maximizes autonomy, minimizes coordination. **Related**: Cognitive Load. **Lifecycle**: Development, Operations  
**G4. RACI Matrix** [EN] – Responsibility assignment: Responsible, Accountable, Consulted, Informed. **Related**: Decision Rights. **Lifecycle**: All  
**G5. Psychological Safety** [EN] – Team climate enabling risk-taking without fear. **Related**: Blameless Culture. **Lifecycle**: Culture, Operations  
**G6. Blameless Postmortem** [EN] – Incident review focusing on systems, not individuals. **Related**: Psychological Safety. **Lifecycle**: Operations, Maintenance  
**G7. DORA Metrics** [EN] – Deployment frequency, lead time, MTTR, change failure rate. **Lifecycle**: Deployment, Operations  
**G8. Cognitive Load** [EN] – Mental effort required for team to operate. Minimized by clear boundaries. **Related**: Team Topologies. **Lifecycle**: Architecture, Development  
**G9. Career Ladder** [EN] – Structured progression framework defining levels, competencies, expectations. **Lifecycle**: Team Development  
**G10. 70-20-10 Model** [EN] – Learning distribution: 70% on-job, 20% coaching, 10% training. **Lifecycle**: Team Development  
**G11. Topgrading** [EN] – Hiring method using chronological interviews, reference checks. Increases hire quality 75%+. **Lifecycle**: Talent Acquisition  
**G12. STAR Method** [EN] – Interview framework: Situation, Task, Action, Result. **Related**: Topgrading. **Lifecycle**: Talent Acquisition

## Tools
**T1. Lattice** [EN] – Performance management, career development, engagement surveys. **Updated**: 2024-10. **Pricing**: $11-15/user/mo. **Adoption**: 5K+ companies. https://lattice.com  
**T2. Lever** [EN] – ATS and recruiting platform. Candidate tracking, analytics. **Updated**: 2024-11. **Pricing**: Custom. **Adoption**: 4K+ companies. https://lever.co  
**T3. Culture Amp** [EN] – Employee engagement, performance, development. **Updated**: 2024-10. **Pricing**: Custom. **Adoption**: 6K+ companies. https://cultureamp.com  
**T4. 15Five** [EN] – Continuous performance management, OKRs, 1-on-1s. **Updated**: 2024-09. **Pricing**: $4-16/user/mo. **Adoption**: 3K+ companies. https://15five.com  
**T5. Greenhouse** [EN] – Hiring software with structured interviewing. **Updated**: 2024-11. **Pricing**: Custom. **Adoption**: 7K+ companies. https://greenhouse.io  
**T6. TeamOps by GitLab** [EN] – Operating model framework, async work practices. **Updated**: 2024-08. **Pricing**: Free/OSS. **Adoption**: GitLab model. https://about.gitlab.com/teamops

## Literature
**L1. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution.** – Four team types, interaction modes, cognitive load  
**L2. Lencioni, P. (2002). *The Five Dysfunctions of a Team*. Jossey-Bass.** – Trust, conflict, commitment, accountability, results  
**L3. Kim, G., et al. (2016). *The DevOps Handbook*. IT Revolution.** – Culture, automation, lean, measurement  
**L4. McChrystal, S., et al. (2015). *Team of Teams*. Portfolio.** – Network org, empowered execution, information sharing  
**L5. Adkins, L. (2010). *Coaching Agile Teams*. Addison-Wesley.** – Scrum Master, team facilitation, conflict resolution  
**L6. Fournier, C. (2017). *The Manager's Path*. O'Reilly.** – Tech leadership ladder: IC → TL → Manager → Director → VP → CTO  
**L7. Edmondson, A. (2018). *The Fearless Organization*. Wiley.** – Psychological safety research, practices, measurement  
**L8. Smart, G., & Street, R. (2008). *Who: The A Method for Hiring*. Ballantine.** – Topgrading scorecard, chronological interview, reference checks

## Citations
**A1.** Skelton, M., & Pais, M. (2019). *Team topologies*. IT Revolution. [EN]  
**A2.** Lencioni, P. (2002). *The five dysfunctions of a team*. Jossey-Bass. [EN]  
**A3.** Kim, G., et al. (2016). *The DevOps handbook*. IT Revolution. [EN]  
**A4.** McChrystal, S., et al. (2015). *Team of teams*. Portfolio. [EN]  
**A5.** Adkins, L. (2010). *Coaching agile teams*. Addison-Wesley. [EN]  
**A6.** Fournier, C. (2017). *The manager's path*. O'Reilly. [EN]  
**A7.** Edmondson, A. (2018). *The fearless organization*. Wiley. [EN]  
**A8.** Smart, G., & Street, R. (2008). *Who: The A method for hiring*. Ballantine. [EN]  
**A9.** 张一鸣. (2022). *团队协作的五大障碍*. 机械工业出版社. [ZH]  
**A10.** Forsgren, N., et al. (2018). *Accelerate*. IT Revolution. [EN]  
**A11.** 马云. (2020). *阿里巴巴组织管理*. 中信出版社. [ZH]  
**A12.** Brook, F. (1975). *The mythical man-month*. Addison-Wesley. [EN]  
**A13.** DeMarco, T., & Lister, T. (2013). *Peopleware* (3rd). Addison-Wesley. [EN]  
**A14.** 周志明. (2021). *团队拓扑实践指南*. 电子工业出版社. [ZH]  
**A15.** Patton, J., et al. (2014). *User story mapping*. O'Reilly. [EN]
