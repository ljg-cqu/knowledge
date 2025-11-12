# Cloze / Fill-in-the-Blank Prompt

Generate 24–40 senior-level cloze items for [domain] targeting professionals with 5+ years experience.

## Scope & Constraints

- **Audience**: [senior/architect/expert]
- **Excluded**: [deprecated APIs, out-of-scope topics]
- **Limitations**: [emerging tech, time constraints]

## Success Criteria

- **Items**: 24–40 (20% Foundational / 40% Intermediate / 40% Advanced)
- **References**: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA
- **Language**: ~60% EN, ~30% ZH, ~10% other
- **Citations**: ≥70% items ≥1; ≥30% items ≥2 distinct types
- **Recency**: ≥50% from last 3yr (≥70% for AI/security/blockchain)
- **Diversity**: ≥3 source types; single type <25%
- **Validation**: 100% pass all 13 checks

---

## Item Structure

Each item requires:

**1. Statement**: Sentence with ___ or [blank]

**2. Difficulty**: Foundational/Intermediate/Advanced

**3. Acceptable Answers**: Array with primary term, synonyms, abbreviations, regional variants, equivalent formulations

**4. Normalization**:
- **Case**: insensitive (default) / sensitive (if critical)
- **Whitespace**: trim, normalize to single space
- **Punctuation**: strip non-semantic; retain semantic
- **Numeric**: tolerance ("10% ±2%")
- **Units**: equivalents ("1000ms" = "1s")

**5. Grading**:
- **Full**: 100% conditions
- **Partial**: scenarios + allocation
- **Incorrect**: common errors
- **Borderline**: edge cases

**6. Rationale**: Evidence-based with ≥1 [Ref: ID] (≥30% items need ≥2 distinct types); include definitions, significance, limitations, trade-offs

**7. Fairness**:
- **Regional**: jurisdiction variations
- **Stakeholder**: differing priorities
- **Contested**: multiple valid definitions
- **Risks**: severity (Low/Medium/High) + mitigation
- **Assumptions**: explicit

## Reference Formats

**Glossary (≥10)**:
```
**Term** (ID: G#): Definition [Lang]
- Stakeholders: [roles]
- Notes: [risks, assumptions, variants]
```

**Codebase (≥5)**:
```
**Project** (ID: C#) (GitHub: owner/repo | License: Type)
- Description, Maturity, Last Update, Security, Risks/Mitigations
```

**Literature (≥6)**:
```
**Title** (ID: L#) (Year) [Lang]
- Authors, Type, Key Findings, Credibility, Jurisdiction, Impact, Risks
```

**APA (≥12)**:
```
[APA 7th] [Lang]
    Risk notes, Applicability, Archive
```

---

## Workflow

### 1. Planning
- Define 4-6 MECE clusters, allocate 4-8 items/cluster (24-40 total)
- Assign difficulty: 20%/40%/40%
- Document: audience, prerequisites, regulatory context, exclusions, contested areas

**Check**: Items=24-40, distribution≈20%/40%/40% (±5%), MECE clusters, documented assumptions

### 2. References
- Gather: G≥10, C≥5, L≥6, A≥12; tag language; classify type; record year
- Assign IDs: G1-Gn, C1-Cn, L1-Ln, A1-An
- Record metadata: credibility, jurisdiction, risks, gaps

**Check**: Floors met, language≈60%/30%/10% (±10%), recency≥50% (≥70% AI/security/blockchain), diversity≥3 types, single<25%

### 3. Generation
Per item: statement, difficulty, answer array with variants, normalization rules, rationale with ≥1 [Ref: ID] (≥30% need ≥2 distinct types), fairness notes

**Check every 6**: Blanks clear, ≥70% with ≥1 citation, ≥30% with ≥2, 100% answer arrays, 100% normalization

### 4. Grading
Per item: common errors, borderline cases + partial credit, high-risk flags (severity + mitigation), stakeholder notes

**Check**: 100% acceptance criteria, ≥50% common errors, partial credit defined, risks flagged

### 5. Compilation
Populate reference sections, verify cross-refs, document shortfalls

**Check**: Floors met OR documented, zero broken refs, all fields complete

---

## Validation (13 Checks)

Execute sequentially. If ANY fails, fix and re-validate ALL.

1. **Counts**: G≥10, C≥5, L≥6, A≥12, Items=24-40, difficulty=20%/40%/40% (±5%)
2. **Citations**: ≥70% items ≥1, ≥30% items ≥2 distinct
3. **Language**: EN=50-70%, ZH=20-40%, Other=5-15%
4. **Recency**: ≥50% last 3yr (≥70% AI/security/blockchain)
5. **Diversity**: ≥3 types, single<25%
6. **Links**: 100% accessible OR archived
7. **Cross-refs**: 100% [Ref: ID] resolve
8. **Answers**: 100% complete arrays
9. **Clarity**: 100% unambiguous blanks
10. **Normalization**: 100% rules specified
11. **Conflicts**: ≥80% contested terms have ≥2 variants
12. **Fairness**: Medium/High risks mitigated, stakeholders represented, regional variants acknowledged, assumptions documented
13. **Self-check**: 1-12 PASS, items implementable, rationales valuable, criteria met

**Report**:
```
| Check | Result | Status |
|-------|--------|--------|
| 1. Floors | G:X C:Y L:Z A:W I:N (F/I/A) | PASS/FAIL |
| 2. Citation | X% ≥1, Y% ≥2 | PASS/FAIL |
| 3. Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| 4. Recency | X% last 3yr | PASS/FAIL |
| 5. Diversity | N types, max P% | PASS/FAIL |
| 6. Links | Y/X accessible | PASS/FAIL |
| 7. Cross-refs | Y/X resolved | PASS/FAIL |
| 8. Answers | Y/X complete | PASS/FAIL |
| 9. Clarity | Y/X unambiguous | PASS/FAIL |
| 10. Normalization | Y/X specified | PASS/FAIL |
| 11. Conflicts | Y/X compliant (Z%) | PASS/FAIL |
| 12. Fairness | Stakeholders:[...] Risks:[...] | PASS/FAIL |
| 13. Self-check | Issues: Resolved/Outstanding | PASS/FAIL |
```

**Requirement**: ALL 13 PASS before submission.

---

## Output Format

```markdown
## Contents
- [Item Bank](#item-bank)
  - [Topic 1: Title](#topic-1-title)
    - [Item 1: Description](#item-1-description)
- [References](#references)
  - [Glossary](#glossary) | [Codebase](#codebase) | [Literature](#literature) | [APA](#apa-citations)
- [Validation Report](#validation-report)

---

## Item Bank

### Topic 1: [Title]

#### Item 1: [Description]

**Difficulty**: [F/I/A]

**Statement**: [Sentence with ___]

**Acceptable Answers**: ["primary", "synonym", "variant", "abbr"]

**Normalization**:
- Case: [insensitive/sensitive]
- Whitespace: [trim, normalize]
- Punctuation: [strip non-semantic/retain all]
- Numeric: [±X%]
- Units: [equivalents]

**Grading**:
- Full: [conditions]
- Partial: [conditions + %]
- Incorrect: ["error 1", "error 2"]
- Borderline: ["case: explain"]

**Fairness**:
- Misconceptions: [high-risk + mitigation [Ref: ID]]
- Stakeholder: ["differences"]
- Regional: ["US vs UK"]
- Contested: ["varies [Ref: ID]"]

**Rationale**: [Explanation with ≥1 [Ref: ID]: definitions, significance, limitations]

---

## References

### Glossary
**Term** (ID: G#): Definition [Lang]
- Stakeholders: [roles]
- Notes: [risks, variants]

### Codebase
**Project** (ID: C#) (GitHub: owner/repo | License: Type)
- Description, Maturity, Update, Security, Risks/Mitigations

### Literature
**Title** (ID: L#) (Year) [Lang]
- Authors, Type, Findings, Credibility, Jurisdiction, Impact, Risks

### APA Citations
[APA 7th] [Lang]
    Risk notes, Applicability, Archive

---

## Validation Report

**Date**: [YYYY-MM-DD] | **Bank**: [Title] ([N] items) | **Validator**: [Name]

[Validation table: 13 checks PASS]

**Status**: READY

**Notes**: [Summary]
```

---

## Quality Principles

- **Context**: Scope, audience, constraints, assumptions explicit
- **Clarity**: Define jargon; unambiguous blanks
- **Precision**: Specific terms; consistent usage; complete arrays
- **Relevance**: Material concepts only
- **MECE**: Clusters mutually exclusive, collectively exhaustive
- **Sufficiency**: Comprehensive within scope
- **Breadth**: Multiple perspectives (regional, stakeholder)
- **Depth**: Actionable rationales beyond keys
- **Significance**: Prioritize high-value; flag high-risk
- **Concision**: Essential only; no redundancy
- **Accuracy**: Evidence-based with authoritative citations
- **Credibility**: Peer-reviewed, standards, vetted sources
- **Logic**: Coherent sequencing; foundational supports advanced
- **Risk/Value**: Explicit flags with severity + mitigation
- **Fairness**: Balanced; acknowledge assumptions, limitations, alternatives
- **Structure**: TOC, hierarchy, consistent format
- **Evidence**: Inline citations; ≥70% cited
- **Validation**: 13-step protocol; all PASS
- **Practicality**: Implementable grading; appropriate items
- **Success Criteria**: Measurable floors, quality gates

---

## Submission Checklist

**Quantitative**:
- [ ] G≥10, C≥5, L≥6, A≥12
- [ ] Items: 24-40
- [ ] Difficulty: 20%/40%/40% (±5%)
- [ ] Language: ~60%EN/~30%ZH/~10%other (±10%)

**Quality**:
- [ ] Recency: ≥50% last 3yr (≥70% AI/security/blockchain)
- [ ] Diversity: ≥3 types; single<25%
- [ ] Citations: ≥70% ≥1; ≥30% ≥2 distinct

**Items**:
- [ ] 100% unambiguous blanks
- [ ] 100% complete answers with variants
- [ ] 100% normalization rules
- [ ] 100% grading rubrics

**Sources**:
- [ ] Codebase: license, update, maturity, risks
- [ ] 100% links accessible OR archived
- [ ] 100% [Ref: ID] resolve

**Fairness**:
- [ ] High-risk flagged (severity + mitigation)
- [ ] Multiple stakeholder perspectives
- [ ] Regional variations acknowledged
- [ ] Assumptions explicit
- [ ] Contested variants included

**Validation**:
- [ ] All 13 PASS
- [ ] Report with quantitative results

**Deliverables**:
- [ ] Item bank: complete metadata
- [ ] TOC: all sections linked
- [ ] References: 4 sections complete
- [ ] Validation: demonstrates compliance

**ALL CONFIRMED** → READY
