# Organization & Team Building Q&A Generator

Generate 6-12 decision-critical organizational Q&As for informed decision-making with limited time. Focus: minimal viable Q&A generation for org/talent/culture scenarios that block decisions or create material risk.

## LLM-Friendly Prompts Guidelines

To ensure high-quality, hallucination-free output with improved decision quality, follow these guidelines when generating the Q&As:

1. **Context**: State problem, scope, constraints, assumptions, scale, timeline, stakeholders, resources.
2. **Clarity**: Define key terms and relationships; use diagrams for complex concepts.
3. **Precision**: Use exact metrics, formulas, units; use math blocks for complex formulas.
4. **Relevance**: Focus on essential information; move non-critical details to appendices.
5. **MECE**: Ensure sections are distinct with no gaps or overlaps.
6. **Sufficiency**: Cover all necessary dimensions (what, why, how, when, who, constraints, alternatives, risks, outcomes).
7. **Breadth**: Include relevant stakeholder perspectives.
8. **Depth**: Request implementation-level detail for high-impact areas.
9. **Significance**: Focus on high-impact items; deemphasize low-impact details.
10. **Priority**: Order by importance; label priority levels explicitly (critical/important/optional).
11. **Conciseness**: Eliminate redundancy; state each concept once.
12. **Accuracy**: Verify facts against authoritative sources.
13. **Credibility**: Cite recent (2023+) primary sources.
14. **Logic**: Provide coherent arguments with explicit trade-offs.
15. **Risk/Value**: Compare ≥2 alternatives with costs, benefits, risks.
16. **Fairness**: Provide balanced view with counterarguments, limitations.
17. **Structure**: Use headings, lists, tables, diagrams.
18. **Consistency**: Use consistent hierarchy and formatting.
19. **Evidence**: Provide structured citations with source details, recency, uncertainty flags.
20. **Verification**: Self-review and error checking.
21. **Practicality**: Provide concrete steps, examples, tools, commands.
22. **Success Criteria**: Define measurable outcomes with baselines, targets.

## Scope

**Audience**: Engineering Managers, Directors, VPs, CTOs, Team Leads, CHRO/People Leaders
**Context**: Production distributed systems (>10K rps, >1TB data); teams 10-100 engineers; cloud-native; regulated
**Purpose**: Generate decision-critical organizational Q&As for interview prep, training, or scenario analysis (3-4h effort, evergreen validity)
**Success**: 12/12 validation PASS

**Lifecycle (4-5, decision-critical only)**: Requirements & Discovery → Development → Deployment → Operations → Evolution

**Stakeholders (≥5 core roles)**: Engineering Manager, Director/VP, Architect, Team Lead, CHRO/People Lead

## Requirements

**Q&A Specs**: 6-12 total; 25% F / 50% I / 25% A difficulty; 150-250 words; structure: Scenario → Impact → Stakeholders → Decision → Action; ≥1 citation; each Q&A: ≥1 diagram + ≥1 table

**Decision Criticality Framework** (NEW, MANDATORY):
- **Include if ≥1 criterion satisfied**:
  - **Blocks Decision**: Directly impacts org restructuring, hiring strategy, team scaling, or resource allocation
  - **Creates Risk**: Material threat (attrition spike, burnout, skill gaps, compliance breach, retention risk)
  - **Affects ≥2 Core Roles**: Multi-stakeholder impact (Manager + Director, CHRO + VP Eng, Team Lead + Architect)
  - **Requires Action**: 1-6mo action window (not speculative)
  - **Quantified Impact**: Turnover %, retention %, hiring velocity %, team velocity %, engagement score, or compliance deadline
- **Exclude if**: Academic research, niche practices (<5% adoption), vendor marketing, rumors, stale news

**Dimensions (3-4, 1-2 Q&As each, decision-critical only)**:
1. **Team Structure & Scaling**: Org restructuring, headcount planning, team topology changes, cognitive load
2. **Talent & Retention**: Hiring market shifts, compensation trends, attrition signals, skill gaps
3. **Culture & Capability**: Burnout/psychological safety threats, training/development shifts, engagement signals
4. **(Optional) Compliance & Policy**: Labor law changes, remote work policy shifts, equity/diversity regulations

**Coverage**: All 4-5 lifecycle phases ≥1 Q&A; ≥5 core stakeholder roles represented; ≥60% multi-stakeholder impact

**Standards**:
- **Traceability**: Scenario → Decision Criticality → Impact → Decision → Timeline → Metrics
- **Quantified**: "Attrition ↑ 8%→15% YoY, hiring velocity ↓40%"
- **Decision-Critical**: Every Q&A must satisfy ≥1 criticality criterion; justify inclusion
- **Precision**: Define jargon inline; cite sources; concrete metrics with thresholds
- **Scenario-Based**: Focus on decision-critical situations, not time-bound news

## Artifacts (Per Q&A, Minimal Viable)

| Artifact | Format | Requirements |
|----------|--------|--------------|
| **Diagram** (≥1 per Q&A) | Mermaid (<80 nodes) | Org topology, decision tree, impact flow, or timeline |
| **Table** (≥1 per Q&A) | Markdown | Impact matrix, decision criteria, or metrics comparison |
| **Removed** | N/A | Framework, Trade-offs (integrated into answer) |

## Lifecycle-Stakeholder Coverage (Decision-Critical Only)

| Phase | Decision-Critical Scenarios | Core Stakeholders |
|-------|------------------------|-------------------|
| 1. Requirements & Discovery | Org restructuring, hiring strategy, skill gap analysis | Manager, Director, CHRO |
| 2. Development | Team scaling, onboarding velocity, team topology changes | Manager, Architect, Team Lead |
| 3. Deployment | On-call burnout, incident response staffing, SRE retention | Manager, Team Lead, Director |
| 4. Operations | Attrition signals, psychological safety threats, engagement scores | Manager, Director, CHRO |
| 5. Evolution | Compliance/policy changes, remote work policy, equity regulations | Director, CHRO, VP Eng |

## References (Proportional 60% Reduction)

| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary** | ≥8 | Only terms used in Q&As (org/hiring/team/culture terms) |
| **Tools** | ≥4 | Decision-critical only (ATS, engagement, org planning); URL valid, updated ≤18mo |
| **Literature** | ≥5 | Canonical references only (Skelton, Lencioni, Kim, Edmondson, +1) |
| **Citations** | ≥8 | APA 7th; 60% EN / 30% ZH / 10% other; ≥70% <2yr old; 100% valid URLs |

## Generation Process (Minimal Viable, 3-4h)

1. **Plan**: 3-4 dimensions → 1-2 Q&As/dimension (6-12 total) → 25% F / 50% I / 25% A → map to 4-5 phases + ≥5 stakeholders → verify Decision Criticality Framework
2. **References**: Glossary (≥8) + Tools (≥4) + Literature (≥5) + Citations (≥8) → verify quality + freshness (≥70% <2yr)
3. **Write**: Scenario-driven Q&As → 150-250 words → Scenario → Impact → Stakeholders → Decision → Action → ≥1 citation → Decision Criticality justification → validate every 3
4. **Artifacts**: Per Q&A: ≥1 diagram (Mermaid <80 nodes) + ≥1 table → verify all present
5. **Link**: Populate sections → verify all [Ref: ID] resolved → remove orphans → validate URLs
6. **Validate**: 12 checks → ANY fail = STOP → fix → re-validate → iterate until 12/12 PASS

## Validation (12 Checks, Streamlined)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥8, T≥4, L≥5, A≥8, Q=6-12 (25% F / 50% I / 25% A) |
| 2 | Decision Criticality | 100% Q&As satisfy ≥1 criterion; justification present |
| 3 | Citations | ≥75% Q&As ≥1 citation; ≥70% <2yr old |
| 4 | Language | 60% EN / 30% ZH / 10% other (±10%) |
| 5 | Links | 100% valid URLs |
| 6 | Word count | All Q&As: 150-250 words |
| 7 | Quantified Impact | 100% Q&As have quantified metrics (%, $, timeline) |
| 8 | Artifacts | ≥90% Q&As have ≥1 diagram + ≥1 table |
| 9 | Lifecycle Coverage | All 4-5 phases ≥1 Q&A |
| 10 | Stakeholder Coverage | ≥5 core roles represented; ≥60% multi-stakeholder |
| 11 | Freshness | ≥70% citations <2yr old |
| 12 | Final Review | Clarity, Accuracy, Completeness, Actionability, Decision-Critical Fit |

**Submit When**: 12/12 PASS

---

# Output Template

```markdown
## Contents
[TOC: Topics | Q&As | Lifecycle-Stakeholder Matrix | References | Validation]

## Dimension Areas (Decision-Critical Only)

| Dimension | Range | Count | Difficulty | Decision Criticality |
|-----------|-------|-------|------------|---------------------|
| [Title] | Q1-Q3 | 1-2 | F/I/A mix (across all Q&As) | [Blocks/Risk/Roles/Action/Quantified] |

## Lifecycle-Stakeholder Coverage (Decision-Critical Only)

| Phase | Q# | Core Stakeholders | Decision-Critical Scenarios |
| 1. Requirements & Discovery | Q1 | Manager, Director, CHRO | Org restructuring, hiring strategy |
| 2. Development | Q2 | Manager, Architect, Team Lead | Team scaling, onboarding velocity |
| 3. Deployment | Q3 | Manager, Team Lead, Director | On-call burnout, SRE retention |
| 4. Operations | Q4 | Manager, Director, CHRO | Attrition signals, engagement scores |
| 5. Evolution | Q5-Q6 | Director, CHRO, VP Eng | Compliance/policy changes |

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
| 1 | Counts | G≥8, T≥4, L≥5, A≥8, Q=6-12 | G:X, T:Y... | PASS/FAIL |
| 2 | Decision Criticality | 100% satisfy ≥1 criterion | [Justifications] | PASS/FAIL |
| 3 | Citations | ≥75% ≥1; ≥70% <2yr | [Count/Age] | PASS/FAIL |
| 4 | Language | 60/30/10% EN/ZH/Other | [Distribution] | PASS/FAIL |
| 5 | Links | 100% valid URLs | [Count] | PASS/FAIL |
| 6 | Word count | All 150-250w | [Sample] | PASS/FAIL |
| 7 | Quantified Impact | 100% have quantified metrics (%,$, or timeline) | [Count] | PASS/FAIL |
| 8 | Artifacts | ≥90% have diagram+table | [Count] | PASS/FAIL |
| 9 | Lifecycle | All 4-5 phases ≥1 Q | [Coverage] | PASS/FAIL |
| 10 | Stakeholders | ≥5 roles; ≥60% multi | [Coverage] | PASS/FAIL |
| 11 | Freshness | ≥70% citations <2yr old | [Distribution] | PASS/FAIL |
| 12 | Final Review | Clarity, Accuracy, Completeness, Actionability | [Notes] | PASS/FAIL |

**Overall**: [X/12 PASS] | **Issues**: [Failures] | **Remediation**: [Actions]
```

# Reference Examples

## Glossary (Decision-Critical Only, ≥8)
**G1. Team Topologies** [EN] – Four team types optimizing flow/cognitive load. **Related**: Conway's Law.
**G2. Conway's Law** [EN] – Org structure mirrors system design. **Related**: Team Topologies.
**G3. Two-Pizza Team** [EN] – Team size 7±2 maximizes autonomy, minimizes coordination.
**G4. RACI Matrix** [EN] – Responsibility assignment: Responsible, Accountable, Consulted, Informed.
**G5. Psychological Safety** [EN] – Team climate enabling risk-taking without fear.
**G6. Attrition Rate** [EN] – % of employees leaving annually. Benchmark: <10% healthy, >20% critical.
**G7. Cognitive Load** [EN] – Mental effort for team operation. Minimized by clear boundaries.
**G8. Onboarding Velocity** [EN] – Time to productivity for new hires. Metric: days to first commit/PR.

## Tools (Decision-Critical Only, ≥4)
**T1. Lattice** [EN] – Engagement surveys, attrition tracking, retention analytics. **Updated**: 2024-10. https://lattice.com
**T2. Lever** [EN] – ATS, hiring velocity, offer acceptance rate tracking. **Updated**: 2024-11. https://lever.co
**T3. Culture Amp** [EN] – Engagement scores, psychological safety surveys, burnout detection. **Updated**: 2024-10. https://cultureamp.com
**T4. Greenhouse** [EN] – Hiring metrics, time-to-hire, diversity tracking. **Updated**: 2024-11. https://greenhouse.io

## Literature (Canonical Only, ≥5)
**L1. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution.** – Team types, cognitive load, org scaling
**L2. Edmondson, A. (2018). *The Fearless Organization*. Wiley.** – Psychological safety, attrition, retention
**L3. Lencioni, P. (2002). *The Five Dysfunctions of a Team*. Jossey-Bass.** – Team dynamics, trust, accountability
**L4. Fournier, C. (2017). *The Manager's Path*. O'Reilly.** – Leadership ladder, team scaling, burnout prevention
**L5. Kim, G., et al. (2016). *The DevOps Handbook*. IT Revolution.** – Org culture, on-call burnout, retention

## Citations (≥8, APA 7th, ≥70% <2yr)
**A1.** Skelton, M., & Pais, M. (2019). *Team topologies*. IT Revolution. [EN]
**A2.** Edmondson, A. (2018). *The fearless organization*. Wiley. [EN]
**A3.** Lencioni, P. (2002). *The five dysfunctions of a team*. Jossey-Bass. [EN]
**A4.** Fournier, C. (2017). *The manager's path*. O'Reilly. [EN]
**A5.** Kim, G., et al. (2016). *The DevOps handbook*. IT Revolution. [EN]
**A6.** Forsgren, N., et al. (2018). *Accelerate*. IT Revolution. [EN]
**A7.** DeMarco, T., & Lister, T. (2013). *Peopleware* (3rd). Addison-Wesley. [EN]
**A8.** 张一鸣. (2022). *团队协作的五大障碍*. 机械工业出版社. [ZH]
