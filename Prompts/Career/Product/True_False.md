# True/False Statements – Product Manager

Generate senior-level PM assessments: 18–32 T/F statements, difficulty 20/40/40, with citations and validation.

---

# Part I: Specifications

## Scope
**Audience**: Senior/director/VP PMs; B2B/B2C, platform, marketplace, SaaS.  
**Format**: 18–32 statements (≤2 lines); binary T/F; 20% Foundational / 40% Intermediate / 40% Advanced.  
**Coverage**: 4–6 MECE clusters (Strategy, Discovery, Prioritization, Metrics, Stakeholder, GTM); B2B/B2C, PLG/SLG, platform/marketplace perspectives.  
**Constraints**: No double negatives/undefined jargon; binary-evaluable only.  
**Assumptions**: Modern product practices; cross-functional, data-informed.  
**Exclusions**: Trivial UI; company-specific processes.

## Standards
- **Clarity**: Define terms (Glossary); consistent terminology; no ambiguous quantifiers.
- **Significance**: High-leverage decisions; exclude trivial.
- **Concision**: Statements ≤2 lines; rationale ≤2 sentences.
- **Accuracy**: Verify facts; cite sources; flag [Uncertain].
- **Credibility**: DOIs/archives; 50% <3yr (70% AI/platform); ≥3 types; max 25%/source.
- **Logic**: Claim → Evidence → Warrant.
- **Fairness**: Acknowledge assumptions, limitations, alternatives, trade-offs.
- **Risk**: Assess costs/benefits; suggest mitigations (advanced).

## References

| Section | Min | Requirements |
|---------|-----|--------------|
| Glossary | 10 | RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST |
| Tools | 5 | Pricing, users, update ≤18mo, integrations |
| Literature | 6 | Frameworks, analyses, launches, cases |
| Citations | 12 | APA 7th + lang tags; 60% EN / 30% ZH / 10% other |

**Inline**: [Ref: ID]; 70% statements ≥1 cite; 30% ≥2 cites. All links accessible/archived; all IDs resolve.

## Validation

Execute sequentially; stop on FAIL; fix and re-run.

1. Counts: G≥10, T≥5, L≥6, A≥12, S=18–32 (20/40/40)
2. Citations: 70% ≥1; 30% ≥2
3. Language: EN 50–70%, ZH 20–40%, Other 5–15%
4. Recency: 50% <3yr (70% AI/platform)
5. Diversity: ≥3 types; max 25%/source
6. Links: All accessible/archived
7. Cross-refs: All [Ref: ID] resolve
8. Quality: MECE, on-topic, actionable

**Report:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% <3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Quality | MECE/on-topic/actionable | PASS/FAIL |
```
> **Stop on ANY FAIL. Fix, re-validate. Proceed only when ALL PASS.**

---

# Part II: Instructions

Execute sequentially with inline validation.

### Step 1: Plan (4–6 MECE clusters)
1. Select: Strategy | Discovery | Prioritization | Metrics | Stakeholder | GTM.
2. Allocate 3–7/cluster (total 18–32); assign 20/40/40; include trade-offs/risks (advanced).
3. **Check**: Total 18–32; ratio 20/40/40; MECE; breadth (B2B/B2C, PLG/SLG, platform/marketplace).

### Step 2: References
1. **Glossary (≥10)**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST.
2. **Tools (≥5)**: Mixpanel/Amplitude, ProductBoard/Aha!, Dovetail/UserTesting (pricing, users, date, integrations).
3. **Literature (≥6)**: Cagan, Olsen, Torres, Perri, Patton, Klement + ZH (俞军, 梁宁, 苏杰).
4. **Citations (≥12)**: APA 7th + lang tags; IDs (G#/T#/L#/A#).
5. **Check**: Counts; language 60/30/10%; recency 50% <3yr; ≥3 types; DOIs/archives; ≤25%/source.

### Step 3: Statements
1. Write claim (≤2 lines); answer (T/F).
2. Rationale (1–2 sentences, [Ref: ID]): Claim → Evidence → Warrant.
3. Optional (2–3 sentences): assumptions, limitations, alternatives, trade-offs, risk/mitigation.
4. Use Glossary; consistent terms; avoid ambiguity; stay on-topic.
5. Tag [Uncertain] if needed; narrow scope.
6. **Check**: Every 5 verify length, citations, clarity, logic, fairness, MECE, on-topic.

### Step 4: Populate
1. Complete G/T/L/A with required fields.
2. **Check**: All [Ref: ID] resolve; links accessible/archived.

### Step 5: Validate
Execute all 8 validation checks. Fix; re-run until PASS.

### Step 6: Submit
Confirm all PASS; submit.

---

# Part III: Output

Use lists, tables, Mermaid, code blocks. TOC with section links.

```markdown
## Contents
- [True/False Bank](#truefalse-bank)
- [References](#references)
  - [Glossary](#glossary) | [Tools](#tools) | [Literature](#literature) | [Citations](#citations)
- [Validation Report](#validation-report)

---

## True/False Bank

### Statement X
**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Statement:** (Claim, ≤2 lines)

**Answer:** [True/False]

**Rationale:** (1–2 sentences, [Ref: ID])

**Justification:** (Optional, 2–3 sentences: assumptions, alternatives, trade-offs, risk/mitigation)

---

## References

IDs: G# (Glossary), T# (Tools), L# (Literature), A# (Citations). Inline: [Ref: G2, T3, A5].

### Glossary
**G1. Term**  
Definition. Use cases. Related.

*Example:*  
**G1. RICE**  
Reach × Impact × Confidence ÷ Effort. Use: Roadmap, backlog. Related: ICE, Value/Effort.

[≥10 entries]

---

### Tools
**T1. Name** (Category)  
Features. Pricing. Users. Date. Integrations. Use. URL.

*Example:*  
**T1. Mixpanel** (Analytics)  
Events, funnels, cohorts, A/B. Freemium–Enterprise. 8K+ cos. Q3 2024. Integrates: Segment, Salesforce, Jira. Use: Activation, retention. https://mixpanel.com

[≥5 entries]

---

### Literature
**L1. Author. (Year). *Title*. Publisher.**  
Themes. Applications.

*Example:*  
**L1. Cagan, M. (2017). *Inspired* (2nd ed.). Wiley.**  
Discovery vs delivery, empowered teams.

[≥6 entries]

---

### Citations
**A1. APA 7th. [Lang]**

*Example:*  
**A1. Cagan, M. (2017). *Inspired: How to create tech products customers love* (2nd ed.). Wiley. [EN]**

[≥12; ~60% EN, ~30% ZH, ~10% other]

---

## Validation Report
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% <3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Quality | MECE/on-topic/actionable | PASS/FAIL |
```
---
