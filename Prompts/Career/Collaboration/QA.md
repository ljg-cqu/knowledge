# Cross-Functional Collaboration Interview Q&A Generator

Generate 25-30 senior/leadership interview Q&As demonstrating cross-functional collaboration across software lifecycle.

**Audience**: EM, Director, VP, CTO, Arch, TL, TPM  
**Context**: Distributed systems (>10K rps, >1TB data), teams (10-100), remote/multi-TZ, cloud-native, regulated  
**Success**: 21/21 validation PASS

**8 Phases**: Requirements & Discovery | Architecture & Design | Development | Testing & Quality | Deployment & Release | Operations & Observability | Maintenance & Support | Evolution & Governance

**10 Stakeholders**: BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead

---

# Core Requirements

## Question Specs

| Aspect | Requirement |
|--------|-------------|
| **Count** | 25-30 (6 dimensions × 4-6) |
| **Difficulty** | 20% F / 40% I / 40% A |
| **Answer** | 200-350 words: Context → Strategy → Framework → Metrics → Trade-offs |
| **Citations** | ≥1 (≥2 for complex) |
| **Cluster** | Diagram + framework + table + metric |
| **Coverage** | 8 phases ≥2 each; 10 stakeholders ≥2 each |

## 6 Dimensions (4-6 Each)

| Dimension | Topics |
|-----------|--------|
| **Communication** | Sync/async, docs, API contracts, runbooks, ADRs, meetings, radiators |
| **Decision-Making** | RFC/ADR, consensus, conflict, escalation, RACI/DACI/RAPID |
| **Knowledge Transfer** | Docs culture, pair/mob, reviews, tech talks, wikis, onboarding |
| **Coordination** | Dependency mgmt, interfaces, integration, handoffs, ceremonies |
| **Stakeholder** | Biz-tech align, customer collab, partnerships, vendor mgmt |
| **Distributed/Remote** | TZ mgmt, async workflows, virtual tools, facilitation, culture |

## Content Standards

- **Traceability**: Need → Strategy → Pattern → Mechanism → Metrics
- **Quantified**: Use numbers (✅ "40% ↓ meetings, +2h latency" ❌ "better")
- **Context**: Team <10/10-50/50-200/>200; Dist colocated/multi/remote/distributed; TZ <3h/3-8h/8-12h/>12h; Sync >80%/50-80%/20-50%/<20%
- **Balance**: ≥2 approaches + table + assumptions/limits + [Consensus]/[Context]/[Emerging] tag
- **Precision**: Define jargon once inline (e.g., "RFC: Request for Comments"); concrete metrics ("SLA <24h" not "fast")

## Artifacts

| Dimension | Diagram | Framework | Metric |
|-----------|---------|-----------|--------|
| Communication | Flow, C4 | DACI, Charter | `Async Ratio = Async/Total × 100%` |
| Decision-Making | Tree, RACI | RFC/ADR, RAPID, Cynefin | `Velocity = Days RFC→Approval` |
| Knowledge Transfer | Map, Path | Docs-as-Code, Second Brain | `Coverage = Documented/Total APIs × 100%` |
| Coordination | Dependency, Interaction | Team Topologies, Contract Test | `Integration Time = Avg Hours` |
| Stakeholder | Stakeholder, Value Stream | Matrix, Impact Mapping | `Satisfaction = NPS/CSAT` |
| Distributed/Remote | Timezone, Workflow | Remote Playbook, Async Manifesto | `Overlap = Common Hours/24 × 100%` |

**Format**: Mermaid <120 nodes; cite frameworks; quantitative tables; metrics = formula/vars/target/source

**Frameworks**: RACI/DACI/RAPID, RFC/ADR, Docs-as-Code, Team Topologies, Comms Charter, Stakeholder Matrix, Cynefin, Async Manifesto, Code Review, Pair/Mob, Impact/Wardley Map, C4, Contract Testing

## Lifecycle-Stakeholder Coverage

| Phase | Focus | RACI |
|-------|-------|------|
| 1. Requirements & Discovery | Align, comm, decisions, docs | BA(R), PM(A), Arch(C) |
| 2. Architecture & Design | RFC/ADR, review, contracts, align | Arch(R/A), Dev(C), Sec(C), SRE(C) |
| 3. Development | Review SLA, pair/mob, knowledge, deps | Dev(R/A), QA(C) |
| 4. Testing & Quality | Ownership, Dev-QA, triage, feedback | QA(R/A), Dev(C) |
| 5. Deployment & Release | Coord, rollback, approvals, notifs | DevOps(R/A), SRE(C) |
| 6. Operations & Observability | Incidents, on-call, postmortems, escalations | SRE(R/A), DevOps(C) |
| 7. Maintenance & Support | Transfer, runbooks, security, docs | SRE(R), Sec(R), Data(C) |
| 8. Evolution & Governance | RFC, roadmap, deprecation, engage | PM(R), Arch(R), Lead(A) |

**Req**: 8 phases ≥2 each; 10 stakeholders ≥2 each; explicit lifecycle link

## References

| Component | Min | Spec |
|-----------|-----|------|
| **Glossary** | ≥12 | Terms + relations + lifecycle |
| **Tools** | ≥6 | URL, update ≤18mo, pricing, adoption |
| **Literature** | ≥8 | Brooks, DeMarco, Kim, Evans, Skelton, Meyer, Gothelf, Patton |
| **Citations** | ≥15 | APA 7th, 60/30/10% EN/ZH/Other |

**Quality**: ≥50% <5yr (≥60% collab); ≥3 types; <25% single; 100% valid URLs

---

# Generation Process

## 1. Plan
5-6 clusters × 4-6 Q&As → 25-30; 1F/2I/2A per cluster; map 8 phases + 10 stakeholders
**✓**: 25-30; 20/40/40% F/I/A; 6 dimensions; 8 phases ≥2; 10 stakeholders ≥2; no overlap

## 2. References
G≥12 (terms+relations+lifecycle) → T≥6 (URL, ≤18mo, pricing, adoption) → L≥8 → A≥15 (APA 7th)
**✓**: Counts; 60/30/10% EN/ZH/Other; ≥50% <5yr (≥60% collab); ≥3 types; <25% single; 100% valid URLs

## 3. Q&As
≥70% judgment; 200-350 words: Context → Strategy → Framework → Metrics → Trade-offs; ≥1 cite (≥2 advanced); quantified; ≥2 alternatives + table; assumptions; lifecycle + stakeholder
**✓ Every 5**: Words, cites, trace, type, quantified, coverage

## 4. Artifacts
Per cluster: Mermaid (<120) + framework (cited) + table (≥2: Approach/Pros/Cons/When) + metric (formula/vars/target/source)
**✓**: 4/4; renders; cited; formatted; valid

## 5. Link
Populate → extract [Ref: ID] → verify → remove orphans → validate URLs
**✓**: Counts; 100% resolved; 0 broken; 60/30/10%; no orphans

## 6. Validate (21 → 21/21)

| # | Check | Target | # | Check | Target |
|---|-------|--------|---|-------|--------|
| 1 | Counts | G≥12, T≥6, L≥8, A≥15, Q=25-30 | 12 | Type | ≥70% judgment |
| 2 | Citations | ≥70% ≥1; ≥30% ≥2 | 13 | Artifacts | ≥90% 4/4 |
| 3 | Language | 60/30/10% | 14 | Frameworks | ≥80% used |
| 4 | Recency | ≥50% <5yr (≥60% collab) | 15 | Metrics | ≥60% have |
| 5 | Diversity | ≥3 types; <25% single | 16 | Diagrams | ≥80% have |
| 6 | Links | 100% valid | 17 | Syntax | 100% valid |
| 7 | Cross-refs | 100% resolved | 18 | Formulas | 100% valid |
| 8 | Word count | 5 samples: 200-350 | 19 | Lifecycle | 8 phases ≥2 |
| 9 | Quantified | 100% | 20 | Stakeholders | 10 roles ≥2 |
| 10 | Per-topic | ≥2 sources + ≥1 tool | 21 | Review | 6/6 |
| 11 | Trace | ≥80% need→metrics | | | |

**Failure**: ANY fail → STOP → fix → re-validate

## 7. Review (6/6)

1. **Clarity**: Logical; consistent; jargon defined
2. **Accuracy**: Verifiable; cited; sound metrics; correct mappings
3. **Completeness**: 6 dimensions (4-6); 8 phases ≥2; 10 stakeholders ≥2; 21/21
4. **Balance**: ≥2 alternatives + table; assumptions/limits; tags
5. **Practicality**: Actionable; established frameworks; measurable
6. **Correctness**: No redundancy/inconsistency/gaps/orphans

**Submit**: 21/21 + 6/6 | **Risk**: Lifecycle-stakeholder matrix, URLs, cross-refs

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | Lifecycle-Stakeholder | References | Validation]

## Topic Areas
| Cluster | Dimension | Range | Count | Difficulty |
[6 dimensions, 25-30, 20/40/40%]

## Lifecycle-Stakeholder Coverage
| Phase | Q# | Stakeholders |
[8 phases ≥2, 10 stakeholders ≥2]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences] | **Phase**: [1-8] | **Stakeholders**: [RACI]

### Q1: [How/When/Compare...]
**Difficulty**: [F/I/A] | **Dimension**: [Type] | **Phase**: [1-8] | **Stakeholders**: [Roles]

**Key**: [Quantified trade-off]

**Answer**: [200-350 words: Context → Strategy → Framework → Metrics → Trade-offs] [≥1 cite]

**Framework**:
```mermaid
[Flow/Tree/Map, <120]
```

**Metrics**: | Metric | Formula | Variables | Target | Source |

**Trade-offs**: | Approach | Pros (Quantified) | Cons (Quantified) | When | Tag | [≥2]

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
| # | Check | Target | Result | Status | [21]

**Overall**: [X/21] | **Issues**: [Failures] | **Remediation**: [Actions]
```

# Reference Examples

## Glossary
**G1. RFC** [EN] – Structured proposal for decisions. Related: ADR, Consensus. Lifecycle: All  
**G2. ADR** [EN] – Doc capturing arch decisions, context, consequences. Related: RFC. Lifecycle: Arch, Evolution  
**G3. RACI** [EN] – Responsible, Accountable, Consulted, Informed. Related: DACI, RAPID. Lifecycle: All  
**G4. DACI** [EN] – Driver, Approver, Contributors, Informed. Related: RACI, RAPID. Lifecycle: All  
**G5. Async-First** [EN] – Prioritize async. 40% ↓ meetings. Related: Remote-First. Lifecycle: All  
**G6. Docs-as-Code** [EN] – Docs versioned, reviewed, tested like code. Related: ADR. Lifecycle: All  
**G7. Pair Programming** [EN] – Two devs, one workstation. 15-25% ↑ quality. Related: Mob. Lifecycle: Dev  
**G8. Code Review SLA** [EN] – Review <24h. Related: PR. Lifecycle: Dev  
**G9. Blameless Postmortem** [EN] – Incident review on systems. Related: Psych Safety. Lifecycle: Ops, Maint  
**G10. Contract Testing** [EN] – Test API contracts (Pact). 95% caught. Related: API Design. Lifecycle: Testing  
**G11. Stakeholder Map** [EN] – Visual: influence, interest, impact. Related: Comms Plan. Lifecycle: All  
**G12. Communication Charter** [EN] – Norms: channels, response times. Related: Async-First. Lifecycle: All

## Tools
**T1. Notion** [EN] – Workspace, docs, wikis. 2024-11. $0-25/user/mo. 30M+ users. https://notion.so  
**T2. Confluence** [EN] – Docs, knowledge base. 2024-11. $6-12/user/mo. 75K+ cos. https://atlassian.com/software/confluence  
**T3. Miro** [EN] – Whiteboard, visual. 2024-10. $0-16/user/mo. 50M+ users. https://miro.com  
**T4. Slack** [EN] – Messaging, async. 2024-11. $0-15/user/mo. 20M+ daily. https://slack.com  
**T5. Linear** [EN] – Issues, roadmaps. 2024-11. $8-14/user/mo. 10K+ cos. https://linear.app  
**T6. GitHub** [EN] – Code, PR, review. 2024-11. $0-21/user/mo. 100M+ devs. https://github.com  
**T7. Loom** [EN] – Async video. 2024-10. $0-15/user/mo. 20M+ users. https://loom.com  
**T8. ADR Tools** [EN] – ADR mgmt. 2024-08. Free/OSS. 3K+ stars. https://github.com/npryce/adr-tools

## Literature
**L1. Brooks, F. (1975). *Mythical Man-Month*. Addison-Wesley.** – Comm complexity, coord  
**L2. DeMarco, T., & Lister, T. (2013). *Peopleware*. Addison-Wesley.** – Team dynamics, comm  
**L3. Kim, G., et al. (2016). *DevOps Handbook*. IT Revolution.** – Cross-func collab, feedback  
**L4. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** – Ubiquitous language, modeling  
**L5. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution.** – Interaction modes, contracts  
**L6. Meyer, B. (2014). *Agile! Good, Hype, Ugly*. Springer.** – Collab practices, comm  
**L7. Gothelf, J., & Seiden, J. (2021). *Sense & Respond*. HBR.** – Continuous collab, feedback  
**L8. Patton, J. (2014). *User Story Mapping*. O'Reilly.** – Collab discovery, understanding  
**L9. Nygard, M. (2018). *Release It!* Pragmatic.** – Ops collab, incidents, runbooks  
**L10. 周志明. (2021). *凤凰架构*. 机械工业出版社.** – Distributed collab, coord [ZH]

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
