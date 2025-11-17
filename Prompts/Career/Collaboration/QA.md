# Cross-Functional Collaboration Interview Q&A Generator

Generate 8-15 decision-critical Q&As on cross-functional collaboration for senior interviews. Each must impact decisions, risk, stakeholders, or require near-term action.

**Audience**: Engineering Managers, Directors, VPs, CTOs, Architects, Tech Leads, Product Managers
**Context**: Medium to large teams, potentially distributed/remote
**Success Criteria**: Actionable insights with frameworks and metrics

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Count** | 8-15 (balanced across dimensions) |
| **Difficulty** | Mix of fundamental, intermediate, advanced |
| **Answer Length** | 100-250 words: Context → Strategy → Framework → Metrics → Trade-offs |
| **Citations** | ≥1 per Q&A |
| **Artifacts** | Diagram, framework, table, metric per dimension |
| **Coverage** | Multiple phases and stakeholders; all decision-critical |

## Decision-Critical Dimensions

Include Q&A if it blocks decisions (roadmap, release, resourcing), creates risk (delivery, quality, compliance), affects multiple stakeholders, or requires action within 1-6 months. Exclude niche, optional, redundant, or marketing-focused.

| Dimension | Criticality | Topics |
|-----------|-------------|--------|
| **Decision-Making** | Blocks decisions | RFC/ADR, consensus, conflict resolution |
| **Communication** | Creates risk | Async communication, documentation, contracts |
| **Knowledge Transfer** | Affects velocity | Code reviews, pairing, onboarding |
| **Coordination** | Blocks releases | Dependencies, handoffs, approvals |

## Content Standards

- **Traceability**: Need → Strategy → Pattern → Mechanism → Metrics
- **Quantification**: Use specific numbers (e.g., "40% fewer meetings")
- **Context Awareness**: Consider team size, distribution, timezones
- **Balance**: ≥2 approaches with pros/cons table
- **Precision**: Define jargon; use concrete metrics

## Artifacts

| Cluster | Diagram | Framework | Metric |
|-----------|---------|-----------|--------|
| Communication | Flow | DACI, Charter | Async Ratio (%) |
| Decision-Making | Tree | RFC/ADR, RAPID | Approval Velocity (days) |
| Knowledge Transfer | Map | Docs-as-Code | Documentation Coverage (%) |
| Coordination | Dependency | Team Topologies | Integration Time (hours) |

**Format**: Mermaid diagram + framework + table (≥2 approaches: Pros/Cons/When) + metric per dimension.

**Frameworks**: RACI/DACI/RAPID, RFC/ADR, Docs-as-Code, Team Topologies, Cynefin, Async Manifesto

## Lifecycle-Stakeholder Coverage

| Phase | Focus | Key Stakeholders |
|-------|-------|------------------|
| Requirements | Alignment, decisions | PM, BA, Architect |
| Design | RFC, contracts | Architect, Dev, Security |
| Development | Reviews, knowledge | Dev, QA |
| Testing | Handoffs, feedback | QA, Dev |
| Deployment | Coordination, approvals | DevOps, SRE |
| Operations | Incidents, escalations | SRE, DevOps |
| Maintenance | Runbooks, docs | SRE, Security |
| Governance | Roadmap, engagement | PM, Architect, Lead |

**Requirements**: Cover ≥5 phases and ≥6 stakeholders

## References

| Component | Minimum | Specifications |
|-----------|---------|---------------|
| **Glossary** | ≥6 | Terms used + relations + phases |
| **Tools** | ≥3 | Current tools with adoption metrics |
| **Literature** | ≥4 | Canonical + recent sources |
| **Citations** | ≥6 | APA 7th, diverse sources |

**Quality**: ≥50% sources <5 years old; valid URLs

---

# Generation Process

1. **Plan and Gather**: Ensure 8-15 Q&As across dimensions, balanced difficulty, covering ≥5 phases/≥6 stakeholders. Compile references meeting minimums and quality criteria.
2. **Create Q&As**: Write answers with structure, citations, quantification, approaches table, lifecycle links. Provide artifacts per dimension.
3. **Validate**: Verify counts, citations, recency, criticality, frameworks, metrics, artifacts, coverage. Fix issues.

---

# Output Template

```markdown
## Contents
[TOC]

## Topic Areas
| Dimension | Count | Difficulty |
[Balanced across 4 dimensions]

## Coverage
| Phase | Stakeholders | Criticality |
[Multiple phases/stakeholders]

## Q&A Section
### Q1: [Question]
**Difficulty**: [Level] | **Dimension**: [Type] | **Phase**: [Phase] | **Stakeholders**: [Roles]  
**Criticality**: [Reason]

**Answer**: [100-250 words: Context → Strategy → Framework → Metrics → Trade-offs] [Citations]

**Diagram**:
```mermaid
[Diagram]
```

**Framework**: [Name/Description]

**Metrics**: | Metric | Formula | Target |

**Trade-offs**: | Approach | Pros | Cons | When |

**Links**: [Lifecycle/Stakeholder impact]

## References

### Glossary
**G1. [Term]** – [Definition]. Related: [Terms]. Phases: [Phases]

### Tools
**T1. [Tool]** – Purpose: [Desc]. Adoption: [Metrics]. URL: [Link]

### Literature
**L1. Author(s). (Year). *Title*.** – Relevance: [Why]

### Citations
**A1.** Author(s). (Year). *Title*. Source.

## Validation
| Check | Target | Status |
|-------|--------|--------|
| Counts | 8-15 Q&As, balanced | PASS/FAIL |
| Citations | ≥1 per Q&A, resolve | PASS/FAIL |
| Recency | ≥50% <5yr | PASS/FAIL |
| Criticality | All meet criteria | PASS/FAIL |
| Artifacts | Complete per dimension | PASS/FAIL |
| Coverage | ≥5 phases, ≥6 stakeholders | PASS/FAIL |
```

# Reference Examples

## Glossary
**G1. RFC** – Structured proposal for decisions. Related: ADR. Phases: All  
**G2. ADR** – Document capturing decisions. Related: RFC. Phases: Design, Governance  
**G3. RACI** – Roles: Responsible, Accountable, Consulted, Informed. Related: DACI. Phases: All  
**G4. Async-First** – Prioritize async comms. Related: Remote. Phases: All  
**G5. Code Review SLA** – Time limit for reviews. Related: PR. Phases: Development  
**G6. Blameless Postmortem** – Incident analysis. Related: Safety. Phases: Operations

## Tools
**T1. Confluence** – Knowledge base. Adoption: 75K+ orgs. https://atlassian.com/software/confluence  
**T2. Linear** – Issue tracking. Adoption: 10K+ orgs. https://linear.app  
**T3. GitHub** – Code collaboration. Adoption: 100M+ users. https://github.com

## Literature
**L1. Brooks, F. (1975). *Mythical Man-Month*.** – Communication complexity  
**L2. DeMarco & Lister. (2013). *Peopleware*.** – Team dynamics  
**L3. Kim et al. (2016). *DevOps Handbook*.** – Cross-functional collaboration  
**L4. Skelton & Pais. (2019). *Team Topologies*.** – Team structures

## Citations
**A1.** Brooks, F. (1975). *Mythical man-month*. Addison-Wesley.  
**A2.** DeMarco, T., & Lister, T. (2013). *Peopleware*. Addison-Wesley.  
**A3.** Kim, G., et al. (2016). *DevOps handbook*. IT Revolution.  
**A4.** Skelton, M., & Pais, M. (2019). *Team topologies*. IT Revolution.  
**A5.** Patton, J. (2014). *User story mapping*. O'Reilly.  
**A6.** Humble, J., & Farley, D. (2010). *Continuous delivery*. Addison-Wesley.  
  
  
  

