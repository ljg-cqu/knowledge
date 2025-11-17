# Cross-Functional Collaboration Interview Q&A Generator

Generate 8-12 decision-critical Q&As on cross-functional collaboration for senior/leadership interviews. Each Q&A must block decisions, create material risk, affect multiple stakeholders, or require near-term action.

**Audience**: Engineering Managers, Directors, VPs, CTOs, Architects, Tech Leads, Product Managers
**Context**: Distributed systems, medium to large teams, remote/multi-timezone, cloud-native environments
**Success Criteria**: All validation checks pass with decision-critical insights

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Count** | 8-12 (2-3 per dimension) |
| **Difficulty** | ~25% Fundamental / ~50% Intermediate / ~25% Advanced |
| **Answer Length** | 100-250 words: Context → Strategy → Framework → Metrics → Trade-offs |
| **Citations** | ≥1 (≥2 for complex topics) |
| **Artifacts** | Diagram + framework + table + metric per dimension/cluster |
| **Coverage** | 5-6 phases (≥1 each); 6-8 stakeholders (≥1 each); explicit lifecycle links; 100% decision-critical |

## 4 Decision-Critical Dimensions

| Dimension | Criticality | Topics |
|-----------|-------------|--------|
| **Decision-Making** | Blocks decisions | RFC/ADR, consensus, conflict resolution, escalation |
| **Communication** | Creates risk | Async-first, documentation, API contracts, runbooks |
| **Knowledge Transfer** | Affects velocity | Code review SLA, pair/mob programming, onboarding, tech debt |
| **Coordination** | Blocks releases | Dependency management, integration handoffs, deployment approval |

## Decision Criticality Framework

Include a Q&A if ≥1 of the following is true:

- Blocks a key decision (roadmap, release, resourcing).
- Creates material risk (delivery, quality, compliance, trust).
- Affects ≥2 stakeholder roles.
- Requires action in 1–6 months (not speculative).

Exclude a Q&A if it is niche/legacy, orthogonal/nice-to-have, already covered, or primarily marketing.

## Content Standards

- **Traceability**: Need → Strategy → Pattern → Mechanism → Metrics
- **Quantification**: Use specific numbers (e.g., "40% ↓ meetings, +2h focus time")
- **Context Awareness**: Consider team size, distribution, timezones, and sync preferences
- **Balance**: ≥2 approaches with pros/cons table, assumptions, and tags ([Consensus]/[Context]/[Emerging])
- **Precision**: Define jargon inline (e.g., "RFC: Request for Comments"); use concrete metrics

## Artifacts

| Cluster | Diagram | Framework | Metric |
|-----------|---------|-----------|--------|
| Communication | Flow, C4 | DACI, Charter | `Async Ratio = Async/Total × 100%` |
| Decision-Making | Tree, RACI | RFC/ADR, RAPID, Cynefin | `Velocity = Days RFC→Approval` |
| Knowledge Transfer | Map, Path | Docs-as-Code, Second Brain | `Coverage = Documented/Total APIs × 100%` |
| Coordination | Dependency, Interaction | Team Topologies, Contract Test | `Integration Time = Avg Hours` |
| Stakeholder | Stakeholder, Value Stream | Matrix, Impact Mapping | `Satisfaction = NPS/CSAT` |
| Distributed/Remote | Timezone, Workflow | Remote Playbook, Async Manifesto | `Overlap = Common Hours/24 × 100%` |

**Format**: One Mermaid diagram + cited framework + quantitative table (≥2 approaches: Approach/Pros/Cons/When) + metric (formula/vars/target/source) per dimension/cluster.

**Frameworks**: RACI/DACI/RAPID, RFC/ADR, Docs-as-Code, Team Topologies, Comms Charter, Stakeholder Matrix, Cynefin, Async Manifesto, Code Review, Pair/Mob, Impact/Wardley Map, C4, Contract Testing

## Lifecycle-Stakeholder Coverage

| Phase | Focus | RACI |
|-------|-------|------|
| 1. Requirements & Discovery | Alignment, communication, decisions, docs | BA(R), PM(A), Arch(C) |
| 2. Architecture & Design | RFC/ADR, review, contracts, alignment | Arch(R/A), Dev(C), Sec(C), SRE(C) |
| 3. Development | Review SLA, pair/mob, knowledge, dependencies | Dev(R/A), QA(C) |
| 4. Testing & Quality | Ownership, Dev-QA handoffs, triage, feedback | QA(R/A), Dev(C) |
| 5. Deployment & Release | Coordination, rollback, approvals, notifications | DevOps(R/A), SRE(C) |
| 6. Operations & Observability | Incidents, on-call, postmortems, escalations | SRE(R/A), DevOps(C) |
| 7. Maintenance & Support | Knowledge transfer, runbooks, security, docs | SRE(R), Sec(R), Data(C) |
| 8. Evolution & Governance | RFC, roadmap, deprecation, stakeholder engagement | PM(R), Arch(R), Lead(A) |

**Requirements**: Cover 5-6 phases (≥1 each); 6-8 stakeholders (≥1 each); explicit lifecycle links

## References (Minimal Viable)

| Component | Minimum | Specifications |
|-----------|---------|---------------|
| **Glossary** | ≥6 | Only terms used in Q&As + relations + lifecycle phases |
| **Tools** | ≥3 | URL, updated ≤18 months, adoption (decision-critical only) |
| **Literature** | ≥4 | Canonical + recent sources on collaboration |
| **Citations** | ≥6 | APA 7th edition, balanced language distribution |

**Quality**: ≥50% sources <5 years old (≥60% collaboration-focused); ≥3 source types; <25% single-author; 100% valid URLs

---

# Generation Process

## 1. Plan and Gather References
Ensure 8-12 Q&As across 4 dimensions with ~25/50/25% difficulty distribution, covering 5-6 phases and 6-8 stakeholders, all decision-critical. Compile references meeting minimum counts (G≥6, T≥3, L≥4, A≥6) and quality criteria.

## 2. Create Q&As and Artifacts
Create Q&As with 100-250 word answers following Context → Strategy → Framework → Metrics → Trade-offs structure. Include ≥1 citation, quantification, ≥2 approaches with table, and lifecycle/stakeholder links. Provide artifacts per cluster.

## 3. Validate and Finalize
Verify all reference links resolve. Run validation checks for counts, citations, recency, criticality, frameworks, metrics, artifacts, lifecycle, and stakeholders. Ensure no redundancy and all are decision-critical.

**Failure Handling**: Fix any failures and re-validate.

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | Lifecycle-Stakeholder | References | Validation]

## Topic Areas
| Cluster | Dimension | Criticality | Range | Count | Difficulty |
[4 dimensions, 8-12 total, 25/50/25% distribution]

## Lifecycle-Stakeholder Coverage
| Phase | Q# | Stakeholders | Criticality |
[5-6 phases ≥1 each, 6-8 stakeholders ≥1 each, 100% decision-critical]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences] | **Phase**: [1-8] | **Stakeholders**: [RACI]

### Q1: [Question]
**Difficulty**: [F/I/A] | **Dimension**: [Type] | **Phase**: [1-8] | **Stakeholders**: [Roles]  
**Criticality**: [Blocks/Risk/Stakeholders/Evolving] | **Justification**: [Why decision-critical]

**Key Trade-off**: [Quantified]

**Answer**: [120-200 words: Context → Strategy → Framework → Metrics → Trade-offs] [≥1 citation]

**Framework**:
```mermaid
[Diagram, <120 nodes]
```

**Metrics**: | Metric | Formula | Variables | Target | Source |

**Trade-offs**: | Approach | Pros (Quantified) | Cons (Quantified) | When | Tag | [≥2]

**Lifecycle**: [Integration] | **Stakeholder**: [Impact]

---

## References

### Glossary (≥6)
**G1. [Term]** [EN/ZH] – [Definition]. **Related**: [Terms]. **Lifecycle**: [Phases]

### Tools (≥3)
**T1. [Tool]** [Tag] – **Purpose**: [Desc]. **Updated**: [YYYY-MM]. **Pricing**: [Type]. **Adoption**: [Metrics]. **URL**: [Link]

### Literature (≥4)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – **Relevance**: [Why]

### Citations (≥6, APA 7th)
**A1.** Author(s). (Year). *Title*. Source. [EN]

---

## Validation Report
| Check | Target | Result | Status |
|-------|--------|--------|--------|
| Reference counts | G≥6, T≥3, L≥4, A≥6 | | PASS/FAIL |
| Q&A counts | 8-12, ~25/50/25% difficulty | | PASS/FAIL |
| Citations | ≥80% ≥1 ref; ≥50% ≥2 refs; all resolve | | PASS/FAIL |
| Recency | ≥50% <5yr (≥60% collab) | | PASS/FAIL |
| Criticality | 100% meet ≥1 criterion | | PASS/FAIL |
| Frameworks | ≥80% use named frameworks | | PASS/FAIL |
| Metrics | ≥70% quantified | | PASS/FAIL |
| Artifacts | ≥90% complete | | PASS/FAIL |
| Coverage | 5-6 phases, 6-8 stakeholders ≥1 each | | PASS/FAIL |

**Overall**: [X/9] | **Issues**: [List] | **Remediation**: [Actions]
```

# Reference Examples

## Glossary (≥6 - Decision-Critical Only)
**G1. RFC** [EN] – Structured proposal for decisions. Related: ADR, Consensus. Lifecycle: All  
**G2. ADR** [EN] – Doc capturing arch decisions, context, consequences. Related: RFC. Lifecycle: Arch, Evolution  
**G3. RACI** [EN] – Responsible, Accountable, Consulted, Informed. Related: DACI, RAPID. Lifecycle: All  
**G4. Async-First** [EN] – Prioritize async. 40% ↓ meetings. Related: Remote-First. Lifecycle: All  
**G5. Code Review SLA** [EN] – Review <24h. Related: PR. Lifecycle: Dev  
**G6. Blameless Postmortem** [EN] – Incident review on systems. Related: Psych Safety. Lifecycle: Ops, Maint

## Tools (≥3 - Decision-Critical Only)
**T1. Confluence** [EN] – Docs, knowledge base. Updated 2024-11. Adoption: 75K+ cos. https://atlassian.com/software/confluence  
**T2. Linear** [EN] – Issues, roadmaps. Updated 2024-11. Adoption: 10K+ cos. https://linear.app  
**T3. GitHub** [EN] – Code, PR, review. Updated 2024-11. Adoption: 100M+ devs. https://github.com

## Literature (≥4 - Canonical + Recent)
**L1. Brooks, F. (1975). *Mythical Man-Month*. Addison-Wesley.** – Comm complexity, coord  
**L2. DeMarco, T., & Lister, T. (2013). *Peopleware*. Addison-Wesley.** – Team dynamics, comm  
**L3. Kim, G., et al. (2016). *DevOps Handbook*. IT Revolution.** – Cross-func collab, feedback  
**L4. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution.** – Interaction modes, contracts

## Citations (≥6, APA 7th)
**A1.** Brooks, F. (1975). *Mythical man-month*. Addison-Wesley. [EN]  
**A2.** DeMarco, T., & Lister, T. (2013). *Peopleware*. Addison-Wesley. [EN]  
**A3.** Kim, G., et al. (2016). *DevOps handbook*. IT Revolution. [EN]  
**A4.** Skelton, M., & Pais, M. (2019). *Team topologies*. IT Revolution. [EN]  
**A5.** Patton, J. (2014). *User story mapping*. O'Reilly. [EN]  
**A6.** Humble, J., & Farley, D. (2010). *Continuous delivery*. Addison-Wesley. [EN]  
  
  
  
  

