# Cross-Functional Collaboration Interview Q&A Generator

Generate 25-30 interview Q&As for senior/leadership roles demonstrating cross-functional collaboration across software lifecycle.

**Audience**: Engineering Managers, Directors, VPs, CTOs, Architects, Team Leads, TPMs  
**Context**: Distributed systems >10K rps, >1TB data; teams 10-100 engineers; remote/multi-timezone; cloud-native; regulated  
**Success**: 21/21 validation PASS

**Lifecycle Phases (8)**: Requirements & Discovery | Architecture & Design | Development | Testing & Quality | Deployment & Release | Operations & Observability | Maintenance & Support | Evolution & Governance

**Stakeholders (10)**: BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Count** | 25-30 Q&As (6 dimensions × 4-6 each) |
| **Difficulty** | 20% F / 40% I / 40% A |
| **Answer** | 200-350 words: Context → Strategy → Framework → Metrics → Trade-offs |
| **Citations** | ≥1 each; ≥2 complex |
| **Cluster** | Diagram + framework + table + metric |
| **Coverage** | All 8 phases ≥2 Q&As; all 10 stakeholders ≥2 Q&As |

## 6 Collaboration Dimensions (4-6 Q&As Each)

| Dimension | Topics |
|-----------|--------|
| **Cross-Functional Communication** | Sync/async patterns, documentation, API contracts, runbooks, ADRs, meetings, radiators |
| **Collaborative Decision-Making** | RFC/ADR, consensus, conflict resolution, escalation, RACI/DACI/RAPID |
| **Knowledge Sharing & Transfer** | Docs culture, pair/mob programming, code reviews, tech talks, wikis, onboarding |
| **Coordination & Synchronization** | Dependency mgmt, interfaces, integration, handoffs, ceremonies, alignment |
| **Stakeholder Engagement** | Business-tech alignment, customer collaboration, partnerships, vendor mgmt, expectations |
| **Distributed & Remote** | Timezone mgmt, async workflows, virtual tools, facilitation, cultural awareness, trust |

## Content Standards

- **Traceability**: Need → Strategy → Pattern → Mechanism → Metrics
- **Quantified Trade-offs**: Numeric impacts (✅ "40% ↓ meetings, +2h latency" ❌ "better")
- **Context Thresholds**: Team <10/10-50/50-200/>200; Distribution colocated/multi-site/remote/distributed; Timezone <3h/3-8h/8-12h/>12h; Sync/async >80%/50-80%/20-50%/<20%
- **Balance**: ≥2 approaches + table; assumptions/limitations; tag [Consensus]/[Context-dependent]/[Emerging]
- **Precision**: Define jargon inline once (e.g., "RFC: Request for Comments"); concrete metrics ("SLA <24h" not "fast")

## Artifacts

| Dimension | Diagram | Framework | Metric |
|-----------|---------|-----------|--------|
| Cross-Functional Communication | Flow, C4 | DACI, Charter | `Async Ratio = Async/Total × 100%` |
| Decision-Making | Tree, RACI | RFC/ADR, RAPID, Cynefin | `Velocity = Days RFC→Approval` |
| Knowledge Sharing | Map, Path | Docs-as-Code, Second Brain | `Coverage = Documented/Total APIs × 100%` |
| Coordination | Dependency, Interaction | Team Topologies, Contract Test | `Integration Time = Avg Hours` |
| Stakeholder Engagement | Stakeholder, Value Stream | Matrix, Impact Mapping | `Satisfaction = NPS/CSAT` |
| Distributed & Remote | Timezone, Workflow | Remote Playbook, Async Manifesto | `Overlap = Common Hours/24 × 100%` |

**Format**: Mermaid <120 nodes; frameworks cited; tables quantitative; metrics with formula/vars/target/source

**Frameworks**: RACI/DACI/RAPID, RFC/ADR, Docs-as-Code, Team Topologies, Communication Charter, Stakeholder Matrix, Cynefin, Async Manifesto, Code Review, Pair/Mob Programming, Impact/Wardley Mapping, C4, Contract Testing

## Lifecycle-Stakeholder Coverage

| Phase | Focus | RACI |
|-------|-------|------|
| 1. Requirements & Discovery | Align stakeholders, communication, decisions, docs | BA(R), PM(A), Arch(C) |
| 2. Architecture & Design | RFC/ADR, design review, API contracts, alignment | Arch(R/A), Dev(C), Sec(C), SRE(C) |
| 3. Development | Code review SLA, pair/mob, knowledge, dependencies | Dev(R/A), QA(C) |
| 4. Testing & Quality | Test ownership, Dev-QA, triage, feedback | QA(R/A), Dev(C) |
| 5. Deployment & Release | Coordination, rollback, approvals, notifications | DevOps(R/A), SRE(C) |
| 6. Operations & Observability | Incidents, on-call, postmortems, escalations | SRE(R/A), DevOps(C) |
| 7. Maintenance & Support | Knowledge transfer, runbooks, security, docs | SRE(R), Sec(R), Data(C) |
| 8. Evolution & Governance | RFC, roadmap, deprecation, engagement | PM(R), Arch(R), Lead(A) |

**Requirement**: Each phase ≥2 Q&As; each stakeholder ≥2 Q&As; explicit lifecycle link in answers

## References

| Component | Min | Spec |
|-----------|-----|------|
| **Glossary** | ≥12 | Terms + relationships + lifecycle |
| **Tools** | ≥6 | URL, update ≤18mo, pricing, adoption |
| **Literature** | ≥8 | Authoritative (Brooks, DeMarco, Kim, Evans, Skelton, Meyer, Gothelf, Patton) |
| **Citations** | ≥15 | APA 7th, 60/30/10% EN/ZH/Other |

**Quality**: ≥50% last 5yr (≥60% collab); ≥3 types; <25% single source; 100% valid URLs

---

# Generation Process

## 1. Plan: 5-6 clusters × 4-6 Q&As → 25-30 total; 1F/2I/2A per cluster; map 8 phases + 10 stakeholders
**Verify**: 25-30 total; 20/40/40% F/I/A; 6 dimensions; 8 phases ≥2; 10 stakeholders ≥2; no overlap

## 2. References: G≥12 (terms+relations+lifecycle) → T≥6 (URL, ≤18mo, pricing, adoption) → L≥8 (Brooks, DeMarco, Kim, Evans, Skelton, Meyer, Gothelf, Patton) → A≥15 (APA 7th)
**Verify**: Counts met; 60/30/10% EN/ZH/Other; ≥50% <5yr (≥60% collab); ≥3 types; <25% single; 100% valid URLs

## 3. Q&As: ≥70% judgment ("How/When/Compare..."); 200-350 words: Context → Strategy → Framework → Metrics → Trade-offs; ≥1 cite (≥2 advanced); quantified; ≥2 alternatives + table; assumptions; lifecycle + stakeholder link
**Validate Every 5**: Words, cites, trace, type, quantified, coverage

## 4. Artifacts: Per cluster: Mermaid (<120 nodes) + framework (cited) + table (≥2: Approach/Pros/Cons/When) + metric (formula/vars/target/source)
**Verify**: All 4/4; renders; cited; formatted; valid

## 5. Link: Populate → extract [Ref: ID] → verify exist → remove orphans → validate URLs
**Verify**: Counts; 100% resolved; 0 broken; 60/30/10%; no orphans

## 6. Validate (21 Checks → 21/21 PASS)

| # | Check | Target | # | Check | Target |
|---|-------|--------|---|-------|--------|
| 1 | Counts | G≥12, T≥6, L≥8, A≥15, Q=25-30 | 12 | Question type | ≥70% judgment |
| 2 | Citations | ≥70% ≥1; ≥30% ≥2 | 13 | Artifacts | ≥90% 4/4 |
| 3 | Language | 60/30/10% EN/ZH/Other | 14 | Frameworks | ≥80% used |
| 4 | Recency | ≥50% <5yr (≥60% collab) | 15 | Metrics | ≥60% have |
| 5 | Diversity | ≥3 types; <25% single | 16 | Diagrams | ≥80% have |
| 6 | Links | 100% valid | 17 | Syntax | 100% valid |
| 7 | Cross-refs | 100% resolved | 18 | Formulas | 100% valid |
| 8 | Word count | Sample 5: 200-350 | 19 | Lifecycle | 8 phases ≥2 |
| 9 | Insights | 100% quantified | 20 | Stakeholders | 10 roles ≥2 |
| 10 | Per-topic | ≥2 sources + ≥1 tool | 21 | Review | 6/6 criteria |
| 11 | Traceability | ≥80% need→metrics | | | |

**Failure**: ANY fail → STOP → fix → re-validate ALL → iterate

## 7. Review (6/6 PASS)

1. **Clarity**: Logical; consistent; jargon defined inline
2. **Accuracy**: Verifiable facts; cited frameworks; sound metrics; correct mappings
3. **Completeness**: 6 dimensions (4-6 each); 8 phases ≥2; 10 stakeholders ≥2; minimums; 21/21
4. **Balance**: ≥2 alternatives + table; assumptions/limits; tagged consensus
5. **Practicality**: Actionable; established frameworks; measurable
6. **Correctness**: No redundancy/inconsistency/gaps/orphans

**Submit When**: 21/21 + 6/6 PASS  
**High-Risk**: Lifecycle-stakeholder matrix, URLs, cross-refs

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | Lifecycle-Stakeholder | References | Validation]

## Topic Areas
| Cluster | Dimension | Range | Count | Difficulty |
| [Title] | [Type] | Q1-Q5 | 5 | 1F/2I/2A |
[6 dimensions, 25-30 total, 20/40/40%]

## Lifecycle-Stakeholder Coverage
| Phase | Q# | Stakeholders |
[All 8 phases ≥2, all 10 stakeholders ≥2]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences] | **Phase**: [1-8] | **Stakeholders**: [RACI roles]

### Q1: [How/When/Compare...]
**Difficulty**: [F/I/A] | **Dimension**: [Type] | **Phase**: [1-8] | **Stakeholders**: [Roles]

**Key Insight**: [Quantified trade-off]

**Answer**: [200-350 words: Context → Strategy → Framework → Metrics → Trade-offs] [≥1 cite]

**Framework**:
```mermaid
[Flow/Tree/Map, <120 nodes]
```

**Metrics**:
| Metric | Formula | Variables | Target | Source |

**Trade-offs**:
| Approach | Pros (Quantified) | Cons (Quantified) | Use When | Tag |
[≥2 alternatives]

**Lifecycle**: [Integration] | **Stakeholder**: [Impact]

---

## References

### Glossary (≥12)
**G1. [Term]** [EN/ZH] – [Def]. **Related**: [Terms]. **Lifecycle**: [Phases]

### Tools (≥6)
**T1. [Tool]** [Tag] – **Purpose**: [Desc]. **Updated**: [YYYY-MM]. **Pricing**: [Type]. **Adoption**: [Metrics]. **URL**: [Link]

### Literature (≥8)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – **Relevance**: [Why]

### Citations (≥15, APA 7th, 60/30/10%)
**A1.** Author(s). (Year). *Title*. Source. [EN]

---

## Validation Report
| # | Check | Target | Result | Status |
[All 21 checks]

**Overall**: [X/21 PASS] | **Issues**: [Failures] | **Remediation**: [Actions]
```

# Reference Examples

## Glossary
**G1. RFC** [EN] – Structured proposal for decisions with review period. Related: ADR, Consensus. Lifecycle: All  
**G2. ADR** [EN] – Document capturing architectural decisions, context, consequences. Related: RFC. Lifecycle: Arch, Evolution  
**G3. RACI** [EN] – Responsibility assignment: Responsible, Accountable, Consulted, Informed. Related: DACI, RAPID. Lifecycle: All  
**G4. DACI** [EN] – Driver, Approver, Contributors, Informed. Related: RACI, RAPID. Lifecycle: All  
**G5. Async-First** [EN] – Prioritize async over sync. 40% ↓ meetings. Related: Remote-First. Lifecycle: All  
**G6. Docs-as-Code** [EN] – Documentation versioned, reviewed, tested like code. Related: ADR. Lifecycle: All  
**G7. Pair Programming** [EN] – Two devs, one workstation. 15-25% ↑ quality. Related: Mob. Lifecycle: Dev  
**G8. Code Review SLA** [EN] – Review turnaround <24h. Related: PR. Lifecycle: Dev  
**G9. Blameless Postmortem** [EN] – Incident review focusing on systems. Related: Psychological Safety. Lifecycle: Ops, Maint  
**G10. Contract Testing** [EN] – Test API contracts (Pact). 95% issues caught. Related: API Design. Lifecycle: Testing  
**G11. Stakeholder Map** [EN] – Visual of influence, interest, impact. Related: Comms Plan. Lifecycle: All  
**G12. Communication Charter** [EN] – Team norms for channels, response times. Related: Async-First. Lifecycle: All

## Tools
**T1. Notion** [EN] – Workspace, docs, wikis. 2024-11. $0-25/user/mo. 30M+ users. https://notion.so  
**T2. Confluence** [EN] – Docs, knowledge base. 2024-11. $6-12/user/mo. 75K+ companies. https://atlassian.com/software/confluence  
**T3. Miro** [EN] – Whiteboard, visual collab. 2024-10. $0-16/user/mo. 50M+ users. https://miro.com  
**T4. Slack** [EN] – Messaging, async comms. 2024-11. $0-15/user/mo. 20M+ daily. https://slack.com  
**T5. Linear** [EN] – Issue tracking, roadmaps. 2024-11. $8-14/user/mo. 10K+ companies. https://linear.app  
**T6. GitHub** [EN] – Code collab, PR, review. 2024-11. $0-21/user/mo. 100M+ devs. https://github.com  
**T7. Loom** [EN] – Async video, recording. 2024-10. $0-15/user/mo. 20M+ users. https://loom.com  
**T8. ADR Tools** [EN] – ADR mgmt. 2024-08. Free/OSS. 3K+ stars. https://github.com/npryce/adr-tools

## Literature
**L1. Brooks, F. (1975). *Mythical Man-Month*. Addison-Wesley.** – Communication complexity, coordination  
**L2. DeMarco, T., & Lister, T. (2013). *Peopleware*. Addison-Wesley.** – Team dynamics, communication  
**L3. Kim, G., et al. (2016). *DevOps Handbook*. IT Revolution.** – Cross-functional collab, feedback  
**L4. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** – Ubiquitous language, modeling  
**L5. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution.** – Interaction modes, contracts  
**L6. Meyer, B. (2014). *Agile! Good, Hype, Ugly*. Springer.** – Collab practices, communication  
**L7. Gothelf, J., & Seiden, J. (2021). *Sense & Respond*. HBR.** – Continuous collab, feedback  
**L8. Patton, J. (2014). *User Story Mapping*. O'Reilly.** – Collaborative discovery, understanding  
**L9. Nygard, M. (2018). *Release It!* Pragmatic.** – Ops collab, incidents, runbooks  
**L10. 周志明. (2021). *凤凰架构*. 机械工业出版社.** – Distributed collab, coordination [ZH]

## Citations (APA 7th)
**A1.** Brooks, F. (1975). *Mythical man-month*. Addison-Wesley. [EN]  
**A2.** DeMarco, T., & Lister, T. (2013). *Peopleware*. Addison-Wesley. [EN]  
**A3.** Kim, G., et al. (2016). *DevOps handbook*. IT Revolution. [EN]  
**A4.** Evans, E. (2003). *Domain-driven design*. Addison-Wesley. [EN]  
**A5.** Skelton, M., & Pais, M. (2019). *Team topologies*. IT Revolution. [EN]  
**A6.** Meyer, B. (2014). *Agile! Good, hype, ugly*. Springer. [EN]  
**A7.** Gothelf, J., & Seiden, J. (2021). *Sense & respond*. HBR. [EN]  
**A8.** Patton, J. (2014). *User story mapping*. O'Reilly. [EN]  
**A9.** Nygard, M. (2018). *Release it!* Pragmatic. [EN]  
**A10.** 周志明. (2021). *凤凰架构*. 机械工业. [ZH]  
**A11.** Humble, J., & Farley, D. (2010). *Continuous delivery*. Addison-Wesley. [EN]  
**A12.** Nygard, M. (2007). *Release it!* Pragmatic. [EN]  
**A13.** Richardson, C. (2018). *Microservices patterns*. Manning. [EN]  
**A14.** 李运华. (2018). *从零开始学架构*. 电子工业. [ZH]  
**A15.** Forsgren, N., et al. (2018). *Accelerate*. IT Revolution. [EN]  
**A16.** Newman, S. (2021). *Building microservices*. O'Reilly. [EN]