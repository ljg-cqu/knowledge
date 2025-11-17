# Cross-Functional Collaboration Interview Q&A Generator (Decision-Critical)

Generate 8-12 decision-critical senior/leadership interview Q&As demonstrating cross-functional collaboration that blocks decisions or creates material risk.

**Audience**: EM, Director, VP, CTO, Arch, TL, TPM  
**Context**: Distributed systems (>10K rps, >1TB data), teams (10-100), remote/multi-TZ, cloud-native, regulated  
**Success**: 12/12 validation PASS + decision-critical insights

**8 Phases**: Requirements & Discovery | Architecture & Design | Development | Testing & Quality | Deployment & Release | Operations & Observability | Maintenance & Support | Evolution & Governance

**10 Stakeholders**: BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead

---

# Core Requirements

## Question Specs (Decision-Critical Only)

| Aspect | Requirement |
|--------|-------------|
| **Count** | 8-12 (4 dimensions × 2-3 each) |
| **Difficulty** | 25% F / 50% I / 25% A |
| **Answer** | 200-350 words: Context → Strategy → Framework → Metrics → Trade-offs |
| **Citations** | ≥1 (≥2 for complex) |
| **Cluster** | Diagram + framework + table + metric |
| **Coverage** | 5-6 phases ≥1 each; 6-8 stakeholders ≥1 each; 100% decision-critical |

## 4 Decision-Critical Dimensions (2-3 Q&As Each)

| Dimension | Decision Criticality | Topics |
|-----------|---------------------|--------|
| **Decision-Making** | Blocks decisions | RFC/ADR, consensus, conflict resolution, escalation |
| **Communication** | Creates risk | Async-first, docs, API contracts, runbooks |
| **Knowledge Transfer** | Affects team velocity | Code review SLA, pair/mob, onboarding, tech debt |
| **Coordination** | Blocks releases | Dependency mgmt, integration handoffs, deployment approval |

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

**Req**: 5-6 of 8 phases (≥1 each); 6-8 of 10 stakeholders (≥1 each); explicit lifecycle link

## References (Minimal Viable - 60% Reduction)

| Component | Min | Spec |
|-----------|-----|------|
| **Glossary** | ≥8 | Only terms used in Q&As + relations + lifecycle |
| **Tools** | ≥4 | URL, update ≤18mo, pricing, adoption (decision-critical only) |
| **Literature** | ≥8 | Brooks, DeMarco, Kim, Skelton, Patton, Forsgren, HBR, Kobalia (canonical + recent) |
| **Citations** | ≥11 | APA 7th, 60/30/10% EN/ZH/Other |

**Quality**: ≥50% <5yr (≥60% collab); ≥3 types; <25% single; 100% valid URLs

---

# Generation Process

## 1. Plan (Decision-Critical)
4 dimensions × 2-3 Q&As → 8-12; 25/50/25% F/I/A; map 5-6 phases + 6-8 stakeholders; 100% decision-critical
**✓**: 8-12; 25/50/25% F/I/A; 4 dimensions; 5-6 phases ≥1; 6-8 stakeholders ≥1; 100% decision-critical

## 2. References (Minimal)
G≥8 (only terms used) → T≥4 (URL, ≤18mo, pricing, adoption) → L≥8 → A≥11 (APA 7th)
**✓**: Counts; 60/30/10% EN/ZH/Other; ≥50% <5yr (≥60% collab); ≥3 types; <25% single; 100% valid URLs

## 3. Q&As (Decision-Critical)
≥70% judgment; 200-350 words: Context → Strategy → Framework → Metrics → Trade-offs; ≥1 cite (≥2 advanced); quantified; ≥2 alternatives + table; assumptions; lifecycle + stakeholder; **Decision Criticality criterion**
**✓ Every 5**: Words, cites, trace, type, quantified, coverage, decision-critical

## 4. Artifacts
Per cluster: Mermaid (<120) + framework (cited) + table (≥2: Approach/Pros/Cons/When) + metric (formula/vars/target/source)
**✓**: 4/4; renders; cited; formatted; valid

## 5. Link
Populate → extract [Ref: ID] → verify → remove orphans → validate URLs
**✓**: Counts; 100% resolved; 0 broken; 60/30/10%; no orphans

## 6. Validate (12 → 12/12)

| # | Check | Criteria |
|---|-------|----------|
| 1 | Ref counts | G≥8, T≥4, L≥8, A≥11 |
| 2 | Q&A counts | 8-12, F:I:A 25:50:25 (±5pp) |
| 3 | Citations | ≥80% ≥1 ref; ≥50% ≥2 refs; all resolve |
| 4 | Language | EN 60-70%, ZH 20-30%, Other 5-10% |
| 5 | Recency | ≥50% <5yr (≥60% collab) |
| 6 | Decision Criticality | 100% satisfy ≥1 criterion: Blocks/Risk/Stakeholders/Evolving |
| 7 | Frameworks | ≥80% RFC/ADR/RACI/DACI/RAPID used |
| 8 | Metrics | ≥70% have quantified metrics |
| 9 | Artifacts | ≥90% have diagram + framework + table + metric |
| 10 | Lifecycle | 5-6 phases ≥1 each; explicit link |
| 11 | Stakeholders | 6-8 roles ≥1 each; RACI clear |
| 12 | **Final Review** | **6 criteria below PASS** |

**Failure**: ANY fail → STOP → fix → re-validate

## 7. Review (6/6 - Decision-Critical)

1. **Decision-Critical**: Every Q&A blocks a decision or creates material risk
2. **Clarity**: Logical; consistent; jargon defined; explicit phase/stakeholder
3. **Quantified**: All trade-offs sized (time, cost, risk, impact)
4. **Actionable**: Clear go/no-go thresholds, alternatives, success criteria
5. **Evidence-Based**: All claims cited, ≥2 sources for key metrics
6. **Minimal Viable**: No redundancy; 8-12 Q&As sufficient for informed action

**Submit**: 12/12 + 6/6 | **Risk**: Decision Criticality, lifecycle-stakeholder matrix, URLs

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | Lifecycle-Stakeholder | References | Validation]

## Topic Areas (Decision-Critical)
| Cluster | Dimension | Decision Criticality | Range | Count | Difficulty |
[4 dimensions, 8-12, 25/50/25%]

## Lifecycle-Stakeholder Coverage (Minimal)
| Phase | Q# | Stakeholders | Decision Criticality |
[5-6 phases ≥1, 6-8 stakeholders ≥1, 100% decision-critical]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences] | **Phase**: [1-8] | **Stakeholders**: [RACI]

### Q1: [How/When/Compare...]
**Difficulty**: [F/I/A] | **Dimension**: [Type] | **Phase**: [1-8] | **Stakeholders**: [Roles]  
**Decision Criticality**: [Blocks/Risk/Stakeholders/Evolving] | **Justification**: [Why this Q&A is decision-critical]

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

## References (Minimal Viable)

### Glossary (≥8 - Only Terms Used)
**G1. [Term]** [EN/ZH] – [Def]. **Related**: [Terms]. **Lifecycle**: [Phases]

### Tools (≥4 - Decision-Critical Only)
**T1. [Tool]** [Tag] – **Purpose**: [Desc]. **Updated**: [YYYY-MM]. **Pricing**: [Type]. **Adoption**: [Metrics]. **URL**: [Link]

### Literature (≥5 - Canonical Only)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – **Relevance**: [Why]

### Citations (≥8, APA 7th, 60/30/10%)
**A1.** Author(s). (Year). *Title*. Source. [EN]

---

## Validation Report (Minimal - 12 Checks)
| # | Check | Target | Result | Status |
|---|-------|--------|--------|--------|
| 1 | Ref counts | G≥8, T≥4, L≥8, A≥11 | | PASS/FAIL |
| 2 | Q&A counts | 8-12, F:I:A 25:50:25 (±5pp) | | PASS/FAIL |
| 3 | Citations | ≥80% ≥1 ref; ≥50% ≥2 refs; all resolve | | PASS/FAIL |
| 4 | Language | EN 60-70%, ZH 20-30%, Other 5-10% | | PASS/FAIL |
| 5 | Recency | ≥50% <5yr (≥60% collab) | | PASS/FAIL |
| 6 | Decision Criticality | 100% satisfy ≥1 criterion (Blocks/Risk/Stakeholders/Evolving) | | PASS/FAIL |
| 7 | Frameworks | ≥80% RFC/ADR/RACI/DACI/RAPID used | | PASS/FAIL |
| 8 | Metrics | ≥70% have quantified metrics | | PASS/FAIL |
| 9 | Artifacts | ≥90% diagram+framework+table+metric | | PASS/FAIL |
| 10 | Lifecycle | 5-6 phases ≥1 each; explicit link | | PASS/FAIL |
| 11 | Stakeholders | 6-8 roles ≥1 each; RACI clear | | PASS/FAIL |
| 12 | Final Review | 6/6 criteria PASS | | PASS/FAIL |

**Overall**: [X/12] | **Issues**: [Failures] | **Remediation**: [Actions]
```

# Reference Examples

## Glossary (≥8 - Decision-Critical Only)
**G1. RFC** [EN] – Structured proposal for decisions. Related: ADR, Consensus. Lifecycle: All  
**G2. ADR** [EN] – Doc capturing arch decisions, context, consequences. Related: RFC. Lifecycle: Arch, Evolution  
**G3. RACI** [EN] – Responsible, Accountable, Consulted, Informed. Related: DACI, RAPID. Lifecycle: All  
**G4. Async-First** [EN] – Prioritize async. 40% ↓ meetings. Related: Remote-First. Lifecycle: All  
**G5. Code Review SLA** [EN] – Review <24h. Related: PR. Lifecycle: Dev  
**G6. Blameless Postmortem** [EN] – Incident review on systems. Related: Psych Safety. Lifecycle: Ops, Maint  
**G7. Contract Testing** [EN] – Test API contracts (Pact). 95% caught. Related: API Design. Lifecycle: Testing  
**G8. Communication Charter** [EN] – Norms: channels, response times. Related: Async-First. Lifecycle: All

## Tools (≥4 - Decision-Critical Only)
**T1. Confluence** [EN] – Docs, knowledge base. 2024-11. $6-12/user/mo. 75K+ cos. https://atlassian.com/software/confluence  
**T2. Linear** [EN] – Issues, roadmaps. 2024-11. $8-14/user/mo. 10K+ cos. https://linear.app  
**T3. GitHub** [EN] – Code, PR, review. 2024-11. $0-21/user/mo. 100M+ devs. https://github.com  
**T4. ADR Tools** [EN] – ADR mgmt. 2024-08. Free/OSS. 3K+ stars. https://github.com/npryce/adr-tools

## Literature (≥8 - Canonical + Recent)
**L1. Brooks, F. (1975). *Mythical Man-Month*. Addison-Wesley.** – Comm complexity, coord  
**L2. DeMarco, T., & Lister, T. (2013). *Peopleware*. Addison-Wesley.** – Team dynamics, comm  
**L3. Kim, G., et al. (2016). *DevOps Handbook*. IT Revolution.** – Cross-func collab, feedback  
**L4. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution.** – Interaction modes, contracts  
**L5. Patton, J. (2014). *User Story Mapping*. O'Reilly.** – Collab discovery, understanding  
**L6. Forsgren, N., et al. (2024). *Accelerate State of DevOps Report*. Google Cloud.** – DevOps performance, collaboration metrics  
**L7. Harvard Business Review. (2024). Why Cross-Functional Collaboration Stalls, and How to Fix It. https://hbr.org/2024/06/why-cross-functional-collaboration-stalls-and-how-to-fix-it** – Analysis of collaboration challenges  
**L8. Kobalia, L. (2024). Cross-Functional Collaboration: A Real-World Guide. Medium. https://medium.productcoalition.com/cross-functional-collaboration-a-real-world-guide-5357e5eb1c12** – Practical collaboration guide

## Citations (≥11, APA 7th, 60/30/10%)
**A1.** Brooks, F. (1975). *Mythical man-month*. Addison-Wesley. [EN]  
**A2.** DeMarco, T., & Lister, T. (2013). *Peopleware*. Addison-Wesley. [EN]  
**A3.** Kim, G., et al. (2016). *DevOps handbook*. IT Revolution. [EN]  
**A4.** Skelton, M., & Pais, M. (2019). *Team topologies*. IT Revolution. [EN]  
**A5.** Patton, J. (2014). *User story mapping*. O'Reilly. [EN]  
**A6.** Humble, J., & Farley, D. (2010). *Continuous delivery*. Addison-Wesley. [EN]  
**A7.** Forsgren, N., et al. (2018). *Accelerate*. IT Revolution. [EN]  
**A8.** 周志明. (2021). *凤凰架构*. 机械工业. [ZH]  
**A9.** Forsgren, N., et al. (2024). *Accelerate State of DevOps Report*. Google Cloud. [EN]  
**A10.** Harvard Business Review. (2024). Why cross-functional collaboration stalls, and how to fix it. https://hbr.org/2024/06/why-cross-functional-collaboration-stalls-and-how-to-fix-it [EN]  
**A11.** Kobalia, L. (2024). Cross-functional collaboration: A real-world guide. Medium. https://medium.productcoalition.com/cross-functional-collaboration-a-real-world-guide-5357e5eb1c12 [EN]
