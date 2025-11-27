# Universal Decision-Critical Q&A Generator

Generate 4-8 decision-critical Q&As for organizational scenarios blocking decisions or creating risk across any industry or domain.

## Adaptation Guide

**For Any Domain**: Replace examples with industry-specific terms (e.g., Healthcare: patient outcomes, compliance, clinical staff; Manufacturing: production efficiency, supply chain, safety; Education: student outcomes, curriculum, faculty; Finance: risk management, regulatory compliance, portfolio).

**Customize**: Lifecycle phases, stakeholder titles, dimensions, metrics, tools, and literature based on your specific industry context.

## LLM-Friendly Prompts Guidelines

Ensure quality: define terms, use metrics, cite sources, compare trade-offs, include steps.

## Scope

**Audience**: Leaders, Managers, Directors, Executives, Specialists, HR professionals across all industries (healthcare, finance, manufacturing, education, retail, government, tech, non-profit, etc.).

**Purpose**: Generate 4-8 decision-critical Q&As for interviews, training, assessment, or organizational analysis.

**Scale**: 4-8 Q&As; 10-15min/question.

**Timeline**: Interview (60-90min) or workshop (3-4h); evergreen.

**Lifecycle**: Planning & Discovery → Implementation → Launch & Integration → Operations & Maintenance → Adaptation & Evolution (5 universal phases).

**Stakeholders**: Front-line Manager, Specialist/Expert, Mid-level Manager, Senior Leader, Executive, HR/People Lead (≥5 core roles from relevant domain).

## Requirements
**Q&A Specs**: 4-8 Q&As (25% F, 50% I, 25% A); 150-250 words each; structure: Scenario → Impact → Stakeholders → Decision → Action; ≥1 citation and artifact per Q&A.

**Difficulty Levels**:
- **F** = Foundational (execution-level tasks)
- **I** = Intermediate (strategy/trade-offs)
- **A** = Advanced (portfolio/vision/P&L)

**Decision Criticality Framework** (MANDATORY):
- Include if ≥1 criterion: Blocks Decision (restructuring, investments, strategic initiatives), Creates Risk (compliance, safety, financial, reputational), Affects ≥2 Roles, Requires Action (1-6mo), Quantified Impact (%, $, time, quality metrics).
- Exclude: Purely academic, theoretical, marketing, or speculative content without actionable decisions.

**Dimensions (3-4, 1-2 Q&As each)** - Select relevant dimensions for your domain:
1. **Organization Structure & Scaling**: Restructuring, resource allocation, workflow design, capacity planning
2. **Talent & Retention**: Recruitment strategy, compensation, turnover, skill development, succession
3. **Culture & Capability**: Engagement, psychological safety, training, performance, wellbeing
4. **Operations & Process**: Efficiency, quality, risk management, innovation, change management
5. **Compliance & Governance**: Regulatory changes, policy, ethics, diversity, sustainability
6. **(Domain-Specific)**: Industry-specific challenges (e.g., patient care, supply chain, curriculum design, customer service)

**Coverage**: All 5 phases ≥1 Q&A; ≥5 roles represented; ≥60% multi-stakeholder.

**Standards**: Traceable, quantified, decision-critical (justify), precise (define jargon, cite), scenario-based.

## Artifacts (Per Q&A)

| Artifact | Format | Requirements |
|----------|--------|--------------|
| **Diagram** | Mermaid (<80 nodes) | ≥1 per Q&A (≥90% coverage): org structure, decision tree, process flow, timeline, stakeholder map, value chain. |
| **Table** | Markdown | ≥1 per Q&A (≥90% coverage): impact matrix, comparison criteria, metrics dashboard, risk assessment. |

## References

| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary** | ≥8 | Domain-specific terms used in Q&As (org, operations, compliance, industry jargon) |
| **Tools** | ≥4 | Decision-critical tools/systems relevant to domain; valid URLs, <2yr old |
| **Literature** | ≥5 | Canonical works in relevant field (leadership, domain experts, industry standards, research) |
| **Citations** | ≥8 | APA 7th; ≥70% <2yr old; mix of academic, industry, regulatory sources |

## Generation Process (3-4h)

1. **Plan**: 3-4 dimensions → 1-2 Q&As/dimension (4-8 total) → balanced difficulty → map to phases/roles → verify criticality.
2. **References**: Collect glossary/tools/literature/citations → verify quality/freshness/links.
3. **Write**: Scenario-driven Q&As → 150-250 words → structure → ≥1 citation → justify criticality → validate.
4. **Artifacts**: ≥1 diagram + table per Q&A → verify coverage.
5. **Link**: Populate sections → resolve refs → validate URLs.
6. **Validate**: Run 12 checks; fix until all pass.

## Validation (12 Checks)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥8, T≥4, L≥5, A≥8, Q=4-8 (balanced) |
| 2 | Criticality | 100% satisfy ≥1 criterion; justifications |
| 3 | Citations | ≥75% Q&As ≥1 citation |
| 4 | Language | Flexible distribution (e.g., 60% EN/30% ZH/10% other) |
| 5 | Links | 100% valid URLs |
| 6 | Word count | All 150-250 words |
| 7 | Quantified | 100% have metrics (%, $, timeline) |
| 8 | Artifacts | ≥90% have diagram + table |
| 9 | Lifecycle | All 5 phases ≥1 Q&A |
| 10 | Stakeholders | ≥5 roles; ≥60% multi |
| 11 | Freshness | ≥70% citations <2yr |
| 12 | Review | Clarity, accuracy, completeness, actionability |

**Submit When**: All 12 pass.

---

# Output Template

```markdown
## Contents
[TOC: Topics | Q&As | Lifecycle-Stakeholder Matrix | References | Validation]

## Dimension Areas (Decision-Critical Only)

| Dimension | Range | Count | Difficulty | Decision Criticality |
|-----------|-------|-------|------------|---------------------|
| [Title] | Q1-Q2 | 1-2 | F/I/A mix (across all Q&As) | [Blocks/Risk/Roles/Action/Quantified] |

## Lifecycle-Stakeholder Coverage (Decision-Critical Only)

| Phase | Q# | Core Stakeholders | Decision-Critical Scenarios |
| 1. Planning & Discovery | Q1 | Manager, Director, HR/People Lead | Org restructuring, strategic planning, resource allocation |
| 2. Implementation | Q2 | Manager, Specialist, Mid-level Manager | Process change, capability building, training rollout |
| 3. Launch & Integration | Q3 | Manager, Specialist, Director | Adoption challenges, transition risks, quality assurance |
| 4. Operations & Maintenance | Q4 | Manager, Director, HR/People Lead | Performance gaps, retention issues, operational efficiency |
| 5. Adaptation & Evolution | Q5 | Director, Senior Leader, Executive | Strategic pivots, regulatory compliance, innovation |

---

## Dimension 1: [Title]
**Overview**: [1-2 sentences] | **Phase**: [1-5] | **Stakeholders**: [Roles] | **Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified]

### Q1: [What/How/When question - scenario-driven]
**Difficulty**: [F/I/A] | **Dimension**: [Type] | **Phase**: [1-5] | **Stakeholders**: [Roles]

**Decision Criticality Justification**: [Why this Q&A satisfies ≥1 criterion]

**Answer**: [150-250 words: Scenario → Impact → Stakeholders → Decision → Action] [≥1 citation [Ref: A1]]

**Diagram** (Mermaid, <80 nodes):
```mermaid
[Org structure / Decision tree / Process flow / Timeline / Stakeholder map / Value chain]
```

**Impact Matrix**:
| Stakeholder | Impact | Metric | Timeline | Action |
| [Role] | [Effect] | [Quantified] | [1-6mo] | [Go/No-go] |

---

## References (Minimal Viable)

### Glossary (≥8, decision-critical domain terms)
**G1. [Term]** [EN/ZH/Other] – [Definition applicable to context]. **Related**: [Terms]. **Domain**: [Industry/Field].

### Tools (≥4, decision-critical domain tools)
**T1. [Tool/System]** [Tag] – **Purpose**: [Description]. **Domain**: [Industry]. **Updated**: [YYYY-MM]. **URL**: [Link]

### Literature (≥5, canonical works in relevant field)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – **Relevance**: [Why applicable]. **Domain**: [Field/Industry].

### Citations (≥8, APA 7th, ≥70% <2yr)
**A1.** Author(s). (Year). *Title*. Source. [EN/ZH/Other]

---

## Validation Report (12 Checks)

| # | Check | Target | Result | Status |
|---|-------|--------|--------|--------|
| 1 | Counts | G≥8, T≥4, L≥5, A≥8, Q=4-8 | G:X, T:Y... | PASS/FAIL |
| 2 | Decision Criticality | 100% satisfy ≥1 criterion | [Justifications] | PASS/FAIL |
| 3 | Citations | ≥75% ≥1 citation | [Count] | PASS/FAIL |
| 4 | Language | Flexible distribution | [Distribution] | PASS/FAIL |
| 5 | Links | 100% valid URLs | [Count] | PASS/FAIL |
| 6 | Word count | All 150-250w | [Sample] | PASS/FAIL |
| 7 | Quantified Impact | 100% have quantified metrics (%, $, time, volume, quality scores) | [Count] | PASS/FAIL |
| 8 | Artifacts | ≥90% have diagram+table | [Count] | PASS/FAIL |
| 9 | Lifecycle | All 5 phases ≥1 Q | [Coverage] | PASS/FAIL |
| 10 | Stakeholders | ≥5 roles; ≥60% multi | [Coverage] | PASS/FAIL |
| 11 | Freshness | ≥70% citations <2yr old | [Distribution] | PASS/FAIL |
| 12 | Final Review | Clarity, Accuracy, Completeness, Actionability | [Notes] | PASS/FAIL |

**Overall**: [X/12 PASS] | **Issues**: [Failures] | **Remediation**: [Actions]
```




