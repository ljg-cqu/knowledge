# True/False Assessment Generator: Business-Architecture Alignment

Generate machine-gradable true/false statements testing how senior technical leaders connect business strategy to architectural decisions.

## Context

**Audience**: Architects, staff-plus engineers, product-aligned technology leaders in enterprise/scale-up environments  
**Assumptions**: Participants understand business strategy frameworks and modern architecture practices  
**Scope**: Multi-team programs with regulated, cloud-first considerations  

## Requirements

### Statement Structure

| Element | Specification |
|---|---|
| **Count** | 18–32 statements |
| **Clusters** | 4–6 MECE themes (Strategic Modeling, Value & Risk, Organizational Dynamics, Architectural Translation, Evolution, Governance) |
| **Difficulty** | 20% foundational, 40% intermediate, 40% advanced |
| **Format** | Declarative, ≤2 lines, single claim, no double negatives |
| **Business-architecture linkage** | ≥70% of statements directly test this relationship |

### Rationale Requirements

Each statement must include:
- **Answer**: True or False
- **Rationale**: 1–2 sentences explaining business → architecture linkage with ≥1 citation `[Ref: ID]`
- **Risk/value context**: Flag assumptions, trade-offs, or context dependencies
- **Optional justification**: 2–3 sentences when nuance prevents misinterpretation

### Evidence Requirements

| Criterion | Specification |
|---|---|
| **Citation format** | APA 7th with language tags (`[EN]`, `[ZH]`, `[ES]`) and inline refs `[Ref: ID]` |
| **Language mix** | EN 60%, ZH 30%, Other 10% (±5%) |
| **Source types** | ≥3 types (frameworks, patterns, case studies, tools); none >25% of total |
| **Recency** | ≥50% citations ≤3 years (≥70% for cloud/digital topics) |
| **Statement coverage** | ≥70% statements with ≥1 citation; ≥30% with ≥2 from different source types |

### Reference Minimums

| Section | Minimum | Content |
|---|---|---|
| **Glossary** | ≥10 entries | Terms with definitions, use cases, language tags |
| **Tools** | ≥5 entries | Name, purpose, pricing model, adoption metrics, URL, language tag |
| **Literature** | ≥6 entries | Short citations with focus areas |
| **APA Citations** | ≥12 entries | Full citations with language tags |

## Quality Standards

Apply these principles throughout:

1. **Clarity**: Define all jargon; state assumptions plainly
2. **Precision**: Use specific scenarios/metrics/patterns, not generic terms
3. **Relevance**: Test high-impact decisions; exclude trivia
4. **MECE**: No cluster overlap; complete coverage
5. **Depth & breadth**: Balance strategy, organization, technology, operations
6. **Fairness**: Acknowledge limitations, counterexamples, trade-offs
7. **Evidence**: Flag uncertainty; verify sources are authoritative and current
8. **Logic**: Ensure unambiguous answers with coherent reasoning
9. **Practicality**: Ground statements in actionable reality

## Execution Steps

**1. Plan clusters**  
Select 4–6 MECE themes; allocate statement counts to hit 20/40/40 difficulty mix; document rationale.

**2. Build evidence base**  
Create reference matrix with language tags, years, source types; prioritize recent authoritative sources.

**3. Draft statements**  
Write declarative statements linking business triggers to architectural consequences; assign difficulty; add rationales with citations.  
*Micro-audit every 5 statements*: Check difficulty mix, MECE alignment, citation presence, language distribution.

**4. Populate references**  
Complete glossary, tools, literature, APA sections; ensure all `[Ref: ID]` resolve; verify language mix and source diversity.

**5. Validate**  
Execute checklist below; document pass/fail; summarize validation results.

## Validation Checklist

- [ ] **Counts**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Statements 18–32
- [ ] **Difficulty**: 20/40/40 distribution across all clusters
- [ ] **Clusters**: Each has 3–6 statements with unique focus
- [ ] **Citations**: ≥70% statements have ≥1; ≥30% have ≥2 from different types
- [ ] **Languages**: EN 50–70%, ZH 20–40%, Other 5–15%
- [ ] **Recency**: ≥50% citations ≤3 years (≥70% for cloud/digital)
- [ ] **Source diversity**: ≥3 types; none >25%
- [ ] **References**: All `[Ref: ID]` resolve; URLs accessible
- [ ] **Logic**: Unambiguous answers; rationales explain assumptions
- [ ] **Risk/value**: Trade-off statements mention mitigation or realization
- [ ] **Formatting**: Headings, tables, lists correct; passes spell/grammar check

## Output Format

Structure output with TOC linking to sections:

```markdown
## Contents
- [Statement Bank](#statement-bank)
  - [Cluster 1: Theme Name](#cluster-1-theme-name)
- [References](#references)
  - [Glossary](#glossary)
  - [Tools](#tools)
  - [Literature](#literature)
  - [APA Citations](#apa-citations)
- [Validation Summary](#validation-summary)

---

## Statement Bank

### Cluster 1: Strategic Modeling

#### Statement 1: [Declarative claim about business → architecture relationship]

**Difficulty:** [Foundational|Intermediate|Advanced]  
**Answer:** [True|False]  
**Rationale:** [1–2 sentences with `[Ref: ID]` explaining business → architecture linkage and assumptions/trade-offs]

---

## References

### Glossary

**G1. Term Name**: Definition. Usage context. [LANG]

### Tools

**T1. Tool Name**: Purpose. Pricing model. Adoption metrics. URL. [LANG]

### Literature

**L1. Author(s) (Year). *Title*. Publisher.** Focus area.

### APA Citations

**A1. Author(s). (Year). *Full title*. Publisher. [LANG]**

---

## Validation Summary

- **Checklist**: [X/10 passed]
- **Language mix**: [EN X%, ZH Y%, Other Z%]
- **Citation recency**: [X% ≤3 years; Y% for cloud/digital]
- **Flagged risks**: [None | specific items]
```
