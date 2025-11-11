# True/False Statements – Product Manager

Generate senior-level PM true/false assessments (18–32 statements) with citations, difficulty distribution (20/40/40), and validation.

---

# Part I: Specifications

## Context & Scope
**Audience**: Senior/director/VP PMs; digital products (B2B/B2C, platform, marketplace, SaaS).  
**Format**: 18–32 declarative statements (≤2 lines each); binary grading (True/False).  
**Difficulty**: 20% Foundational / 40% Intermediate / 40% Advanced.  
**Coverage**: 4–6 MECE clusters (Strategy, Discovery, Prioritization, Metrics, Stakeholder, GTM); multiple perspectives (B2B/B2C, PLG/SLG, platform/marketplace).  
**Constraints**: No double negatives; avoid undefined jargon; evaluable as true/false only.  
**Assumptions**: Modern product practices; cross-functional collaboration; data-informed decisions.  
**Exclusions**: Trivial UI facts; company-specific processes.

## Quality Standards
- **Clarity & Precision**: Define terms in Glossary; consistent terminology; no ambiguous quantifiers.
- **Significance**: High-leverage product decisions only; exclude trivial details.
- **Concision**: Statements ≤2 lines; rationale ≤2 sentences; remove redundancy.
- **Accuracy**: Verify facts; cite authoritative sources; flag uncertainty with [Uncertain].
- **Credibility**: Prefer DOIs/archives; recency: 50% from last 3yr (70% for AI/platform); diversity: ≥3 source types, max 25% from single source.
- **Logic**: Claim → Evidence → Warrant reasoning in rationales.
- **Fairness**: Acknowledge assumptions, limitations, alternatives, counterarguments, trade-offs.
- **Risk/Value**: Assess risks/costs/benefits; suggest mitigations for advanced claims.

## Reference Requirements

| Section | Min | Content |
|---------|-----|---------|
| Glossary | 10 | RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST |
| Tools | 5 | Analytics, roadmapping, research, collaboration (pricing, users, update ≤18mo, integrations) |
| Literature | 6 | Frameworks, market analyses, launches, case studies |
| Citations | 12 | APA 7th + language tags; 60% EN / 30% ZH / 10% other |

**Citation**: [Ref: ID] inline; 70% statements ≥1 citation; 30% ≥2 citations.  
**Links**: All accessible or archived; all [Ref: ID] cross-references resolve.

## Pre-Submission Validation

Execute sequentially. Fix failures and re-run until all PASS.

1. **Counts**: G≥10, T≥5, L≥6, A≥12, S=18–32 (20/40/40 difficulty)
2. **Citations**: 70% statements ≥1; 30% ≥2
3. **Language**: EN 50–70%, ZH 20–40%, Other 5–15%
4. **Recency**: 50% from last 3yr (70% for AI/platform)
5. **Diversity**: ≥3 types; max 25% single source
6. **Links**: All accessible/archived
7. **Cross-refs**: All [Ref: ID] resolve
8. **Quality**: No double negatives; MECE clusters; on-topic; actionable

**Report:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Quality | MECE/on-topic/actionable | PASS/FAIL |
```
> **MANDATORY:** Stop on ANY FAIL. Fix, regenerate, re-validate. Proceed only when ALL PASS.

---

# Part II: Instructions

Execute sequentially with inline validation.

### Step 1: Plan Topics (4–6 MECE clusters)
1. Select clusters: Strategy | Discovery | Prioritization | Metrics | Stakeholder | GTM.
2. Allocate 3–7 statements/cluster (total 18–32); assign difficulty (20/40/40); include trade-offs and strategic risks in advanced items.
3. **Check**: Total 18–32; ratio 20/40/40; MECE; breadth across B2B/B2C, PLG/SLG, platform/marketplace.

### Step 2: Collect References
1. **Glossary (≥10)**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST.
2. **Tools (≥5)**: Mixpanel/Amplitude, ProductBoard/Aha!, Dovetail/UserTesting, Miro (include pricing, users, update date, integrations).
3. **Literature (≥6)**: Cagan, Olsen, Torres, Perri, Patton, Klement + ZH (俞军, 梁宁, 苏杰).
4. **Citations (≥12)**: APA 7th + language tags; assign IDs (G#/T#/L#/A#).
5. **Check**: Counts met; language 60/30/10%; recency 50% <3yr; ≥3 source types; DOIs/archives; diversity ≤25% per source.

### Step 3: Generate Statements
1. Write declarative claim (≤2 lines); provide answer (T/F).
2. Rationale (1–2 sentences with [Ref: ID]) using Claim → Evidence → Warrant.
3. Optional justification (2–3 sentences): assumptions, limitations, alternatives, trade-offs, risk/mitigation.
4. Use Glossary for terms; consistent terminology; avoid ambiguous quantifiers; stay on-topic.
5. Tag [Uncertain] if uncertainty remains; narrow scope/assumptions.
6. **Check**: Every 5 statements verify length, citations, clarity, logic, fairness, MECE, on-topic.

### Step 4: Populate References
1. Complete all sections (G/T/L/A) with required fields.
2. **Check**: All [Ref: ID] resolve; links accessible/archived.

### Step 5: Validate
Execute all 8 Pre-Submission validation steps. Fix failures; re-run until all PASS.

### Step 6: Submit
Confirm all validation PASS; submit.

---

# Part III: Output Format

Use lists, tables, diagrams (Mermaid), code blocks. Start with TOC linking to sections.

```markdown
## Contents
- [True/False Bank](#truefalse-bank)
- [References](#references)
  - [Glossary](#glossary)
  - [Tools](#tools)
  - [Literature](#literature)
  - [Citations](#citations)
- [Validation Report](#validation-report)

---

## True/False Bank

### Statement X
**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Statement:** (Declarative claim, ≤2 lines)

**Answer:** [True/False]

**Rationale:** (1–2 sentences with [Ref: ID])

**Justification:** (Optional, 2–3 sentences: assumptions, alternatives, trade-offs, risk/mitigation)

---

## References

Assign IDs: G# (Glossary), T# (Tools), L# (Literature), A# (Citations). Inline: [Ref: G2, T3, A5].

### Glossary
**G1. Framework/Term Name**  
Definition. Use cases. Related concepts.

*Example:*  
**G1. RICE Prioritization**  
Reach × Impact × Confidence ÷ Effort. Use: Roadmap planning, backlog ranking. Related: ICE, Value/Effort.

[Continue for ≥10 entries]

---

### Tools
**T1. Tool Name** (Category)  
Features. Pricing. Users. Update date. Integrations. Use cases. URL.

*Example:*  
**T1. Mixpanel** (Analytics)  
Event tracking, funnels, cohorts, A/B tests. Freemium–Enterprise. 8K+ companies. Q3 2024. Integrates: Segment, Salesforce, Jira. Use: Activation, retention. https://mixpanel.com

[Continue for ≥5 entries]

---

### Literature
**L1. Author. (Year). *Title*. Publisher.**  
Key themes. Applications.

*Example:*  
**L1. Cagan, M. (2017). *Inspired* (2nd ed.). Wiley.**  
Discovery vs delivery, empowered teams.

[Continue for ≥6 entries]

---

### Citations
**A1. Full APA 7th citation. [Language tag]**

*Example:*  
**A1. Cagan, M. (2017). *Inspired: How to create tech products customers love* (2nd ed.). Wiley. [EN]**

[Continue for ≥12 entries; ~60% EN, ~30% ZH, ~10% other]

---

## Validation Report
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Quality | MECE/on-topic/actionable | PASS/FAIL |
```
```

---
