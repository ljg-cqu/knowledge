# True/False Assessment Generator: Business-Architecture Alignment

Generate machine-gradable T/F statements testing business strategy → architecture alignment for senior technical leaders.

## Context

**Audience**: Architects, staff+ engineers, technology leaders (enterprise/scale-up)  
**Assumptions**: Understands business strategy frameworks and architecture practices  
**Scope**: Multi-team programs, regulated, cloud-first  

## Requirements

### Statement Structure

| Element | Specification |
|---|---|
| **Count** | 18–32 statements |
| **Clusters** | 4–6 MECE themes (Strategy, Value/Risk, Organization, Architecture, Evolution, Governance) |
| **Difficulty** | 20% foundational, 40% intermediate, 40% advanced |
| **Format** | Declarative, ≤2 lines, single claim, no double negatives |
| **Business→architecture** | ≥70% statements test this linkage |

### Rationale Requirements

Per statement:
- **Answer**: True|False
- **Rationale**: 1–2 sentences, business→architecture linkage, ≥1 citation `[Ref: ID]`
- **Risk/value**: Flag assumptions, trade-offs, dependencies
- **Justification** (optional): 2–3 sentences for nuanced cases

### Evidence Requirements

| Criterion | Specification |
|---|---|
| **Citation format** | APA 7th, language tags (`[EN]`/`[ZH]`/`[ES]`), inline refs `[Ref: ID]` |
| **Language mix** | EN 60%, ZH 30%, Other 10% (±5%) |
| **Source types** | ≥3 types (frameworks, patterns, cases, tools); none >25% |
| **Recency** | ≥50% ≤3yrs (≥70% for cloud/digital) |
| **Coverage** | ≥70% statements: ≥1 citation; ≥30%: ≥2 from different types |

### Reference Minimums

| Section | Min | Content |
|---|---|---|
| **Glossary** | ≥10 | Terms: definition, use case, lang tag |
| **Tools** | ≥5 | Name, purpose, pricing, adoption, URL, lang tag |
| **Literature** | ≥6 | Short citations, focus areas |
| **APA Citations** | ≥12 | Full citations, lang tags |

## Quality Standards

1. **Clarity**: Define jargon; state assumptions
2. **Precision**: Use specific scenarios/metrics/patterns
3. **Relevance**: Test high-impact decisions; exclude trivia
4. **MECE**: No overlap; complete coverage
5. **Depth/breadth**: Balance strategy, organization, technology, operations
6. **Fairness**: Acknowledge limitations, counterexamples, trade-offs
7. **Evidence**: Flag uncertainty; verify authoritative, current sources
8. **Logic**: Unambiguous answers, coherent reasoning
9. **Practicality**: Actionable, implementable guidance

## Execution Steps

**1. Plan clusters**: Select 4–6 MECE themes; allocate statements for 20/40/40 difficulty mix

**2. Build evidence**: Create reference matrix (lang tags, years, types); prioritize recent, authoritative sources

**3. Draft statements**: Link business→architecture; assign difficulty; add rationales+citations  
*Micro-audit per 5 statements*: difficulty mix, MECE, citations, language distribution

**4. Populate references**: Complete all sections; resolve `[Ref: ID]`; verify language/source diversity

**5. Validate**: Execute checklist; document pass/fail; summarize

## Validation Checklist

- [ ] **Counts**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Statements 18–32
- [ ] **Difficulty**: 20/40/40 across clusters
- [ ] **Clusters**: 3–6 statements each, unique focus
- [ ] **Citations**: ≥70%: ≥1; ≥30%: ≥2 from different types
- [ ] **Languages**: EN 50–70%, ZH 20–40%, Other 5–15%
- [ ] **Recency**: ≥50% ≤3yrs (≥70% cloud/digital)
- [ ] **Source diversity**: ≥3 types; none >25%
- [ ] **References**: All `[Ref: ID]` resolve; URLs accessible
- [ ] **Logic**: Unambiguous answers; rationales explain assumptions
- [ ] **Risk/value**: Trade-offs mention mitigation/realization
- [ ] **Formatting**: Correct structure; passes spell/grammar check

## Output Format

TOC with linked sections:

```markdown
## Contents
- [Statement Bank](#statement-bank)
- [References](#references)
- [Validation Summary](#validation-summary)

---

## Statement Bank

### Cluster 1: [Theme]

#### Statement 1: [Business→architecture claim]

**Difficulty:** [Foundational|Intermediate|Advanced]  
**Answer:** [True|False]  
**Rationale:** [1–2 sentences, `[Ref: ID]`, assumptions/trade-offs]

---

## References

### Glossary
**G1. Term**: Definition. Context. [LANG]

### Tools
**T1. Tool**: Purpose. Pricing. Adoption. URL. [LANG]

### Literature
**L1. Author(s) (Year). *Title*. Publisher.** Focus.

### APA Citations
**A1. Author(s). (Year). *Title*. Publisher. [LANG]**

---

## Validation Summary

- **Checklist**: [X/11 passed]
- **Languages**: [EN X%, ZH Y%, Other Z%]
- **Recency**: [X% ≤3yrs; Y% cloud/digital]
- **Risks**: [None|items]
```
