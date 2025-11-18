# Organization & Team Building Q&A Generator

Generate 4-8 decision-critical Q&As for organizational scenarios blocking decisions or creating risk.

## LLM-Friendly Prompts Guidelines

Ensure quality: define terms, use metrics, cite sources, compare trade-offs, include steps.

## Scope

**Audience**: Managers, Team Leads, Directors, VPs, CTOs, CHRO, HR professionals.

**Purpose**: Generate 4-8 decision-critical Q&As for interviews, training, or organizational analysis.

**Scale**: 4-8 Q&As; 10-15min/question.

**Timeline**: Interview (60-90min) or workshop (3-4h); evergreen.

**Lifecycle**: Requirements & Discovery → Development → Deployment → Operations → Evolution (5 phases).

**Stakeholders**: Manager, Team Lead, Director/VP, CTO, Architect, CHRO/People Lead (≥5 core roles).

## Requirements
**Q&A Specs**: 4-8 Q&As (25% F, 50% I, 25% A); 150-250 words each; structure: Scenario → Impact → Stakeholders → Decision → Action; ≥1 citation and artifact per Q&A.

**Difficulty Levels**:
- **F** = Foundational (execution-level tasks)
- **I** = Intermediate (strategy/trade-offs)
- **A** = Advanced (portfolio/vision/P&L)

**Decision Criticality Framework** (MANDATORY):
- Include if ≥1 criterion: Blocks Decision (org restructuring, hiring, scaling), Creates Risk (attrition, burnout, gaps), Affects ≥2 Roles, Requires Action (1-6mo), Quantified Impact (turnover %, retention %, etc.).
- Exclude: Academic, marketing, or speculative content.

**Dimensions (3-4, 1-2 Q&As each)**:
1. **Team Structure & Scaling**: Restructuring, headcount, topology, cognitive load
2. **Talent & Retention**: Hiring shifts, compensation, attrition, skill gaps
3. **Culture & Capability**: Burnout, safety, training, engagement
4. **(Optional) Compliance & Policy**: Law changes, remote work, diversity

**Coverage**: All 5 phases ≥1 Q&A; ≥5 roles represented; ≥60% multi-stakeholder.

**Standards**: Traceable, quantified, decision-critical (justify), precise (define jargon, cite), scenario-based.

## Artifacts (Per Q&A)

| Artifact | Format | Requirements |
|----------|--------|--------------|
| **Diagram** | Mermaid (<80 nodes) | ≥1 per Q&A (≥90% coverage): topology, decision tree, flow, timeline. |
| **Table** | Markdown | ≥1 per Q&A (≥90% coverage): impact matrix, criteria, metrics. |

## References

| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary** | ≥8 | Terms used in Q&As (org/hiring/team/culture) |
| **Tools** | ≥4 | Decision-critical (ATS, engagement, planning); valid URLs, <2yr old |
| **Literature** | ≥5 | Canonical (Skelton, Lencioni, Kim, Edmondson, +1) |
| **Citations** | ≥8 | APA 7th; ≥70% <2yr old |

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
| 1. Requirements & Discovery | Q1 | Manager, Director, CHRO | Org restructuring, hiring strategy |
| 2. Development | Q2 | Manager, Architect, Team Lead | Team scaling, onboarding velocity |
| 3. Deployment | Q3 | Manager, Team Lead, Director | On-call burnout, SRE retention |
| 4. Operations | Q4 | Manager, Director, CHRO | Attrition signals, engagement scores |
| 5. Evolution | Q5 | Director, CHRO, VP Eng | Compliance/policy changes |

---

## Dimension 1: [Title]
**Overview**: [1-2 sentences] | **Phase**: [1-5] | **Stakeholders**: [Roles] | **Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified]

### Q1: [What/How/When question - scenario-driven]
**Difficulty**: [F/I/A] | **Dimension**: [Type] | **Phase**: [1-5] | **Stakeholders**: [Roles]

**Decision Criticality Justification**: [Why this Q&A satisfies ≥1 criterion]

**Answer**: [150-250 words: Scenario → Impact → Stakeholders → Decision → Action] [≥1 citation [Ref: A1]]

**Diagram** (Mermaid, <80 nodes):
```mermaid
[Org topology / Decision tree / Impact flow / Timeline]
```

**Impact Matrix**:
| Stakeholder | Impact | Metric | Timeline | Action |
| [Role] | [Effect] | [Quantified] | [1-6mo] | [Go/No-go] |

---

## References (Minimal Viable)

### Glossary (≥8, decision-critical only)
**G1. [Term]** [EN/ZH/Other] – [Definition]. **Related**: [Terms].

### Tools (≥4, decision-critical only)
**T1. [Tool]** [Tag] – **Purpose**: [Desc]. **Updated**: [YYYY-MM]. **URL**: [Link]

### Literature (≥5, canonical only)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – **Relevance**: [Why]

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
| 7 | Quantified Impact | 100% have quantified metrics (%,$, or timeline) | [Count] | PASS/FAIL |
| 8 | Artifacts | ≥90% have diagram+table | [Count] | PASS/FAIL |
| 9 | Lifecycle | All 5 phases ≥1 Q | [Coverage] | PASS/FAIL |
| 10 | Stakeholders | ≥5 roles; ≥60% multi | [Coverage] | PASS/FAIL |
| 11 | Freshness | ≥70% citations <2yr old | [Distribution] | PASS/FAIL |
| 12 | Final Review | Clarity, Accuracy, Completeness, Actionability | [Notes] | PASS/FAIL |

**Overall**: [X/12 PASS] | **Issues**: [Failures] | **Remediation**: [Actions]
```




