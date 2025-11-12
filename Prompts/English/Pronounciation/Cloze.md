# Cloze / Fill-in-the-Blank Prompt

Generate 30–50 cloze items for **English Pronunciation** covering phonetics, accent variations (American, British, Indian, Australian), and pronunciation patterns.

## Scope

- **Audience**: Intermediate-advanced learners, teachers, accent coaches
- **Excluded**: Regional dialects (Southern American, Cockney), singing/theatrical speech, historical evolution
- **Focus**: Standard accents (General American, RP, General Indian/Australian)

## Success Criteria

- **Items**: 30–50 (20% Foundational / 45% Intermediate / 35% Advanced)
- **References**: G≥12, R≥3, L≥8, A≥15
- **Language**: ~70%EN / ~25%ZH / ~5%other
- **Citations**: ≥75% items ≥1; ≥35% items ≥2 distinct types
- **Recency**: ≥40% last 5yr
- **Diversity**: ≥3 types; single<30%
- **Validation**: 13 checks PASS
- **Accent Coverage**: ≥8 AmE vs BrE; ≥4 other (IndE/AusE/CanE)

---

## Item Structure

**1. Statement**: Sentence with ___ or [blank]

**2. Difficulty**: Foundational/Intermediate/Advanced

**3. Acceptable Answers**: [primary, synonyms, abbreviations, regional variants]

**4. Normalization**:
- Case: insensitive (default) / sensitive
- Whitespace: trim, normalize
- Punctuation: strip non-semantic; retain semantic
- Numeric: tolerance (e.g., "10% ±2%")
- Units: equivalents (e.g., "1000ms" = "1s")

**5. Grading**:
- Full: 100% conditions
- Partial: scenarios + %
- Incorrect: common errors
- Borderline: edge cases

**6. Rationale**: Evidence-based with ≥1 [Ref: ID] (≥30% items ≥2 distinct types); include definitions, significance, limitations, trade-offs

**7. Fairness**:
- Regional: accent variations
- Contested: multiple valid pronunciations
- Risks: severity (L/M/H) + mitigation
- Assumptions: explicit

## Reference Formats

**Glossary (≥12)**:
```
**Term** (ID: G#): Definition [Lang]
- Stakeholders, Notes (risks, assumptions, variants)
```

**Resources (≥3)**:
```
**Resource** (ID: R#) (Type: Dictionary/Corpus/Audio/Tool | Access: URL/Platform)
- Description, Coverage, IPA System, Quality, Update, Accessibility
```

**Literature (≥8)**:
```
**Title** (ID: L#) (Year) [Lang]
- Authors, Type, Findings, Accent Focus, IPA Usage, Credibility, Pedagogical Value
```

**APA (≥15)**:
```
[APA 7th] [Lang]
- Accent variety, IPA system, Applicability, Archive
```

---

## Workflow

### 1. Planning
- Define 5-8 MECE clusters: IPA symbols, vowel/consonant sounds, stress/intonation, accent comparisons (AmE/BrE/IndE/AusE), connected speech, pronunciation errors
- Allocate 4-10 items/cluster (30-50 total), difficulty 20%/45%/35%
- Document: audience, prerequisites (basic phonetics), exclusions (dialectal sub-varieties), contested areas

**Check**: Items=30-50, distribution≈20%/45%/35% (±5%), MECE clusters, documented assumptions

### 2. References
- Gather: G≥12 (phonetic terms), R≥3 (audio/dictionaries/corpora), L≥8 (journals/textbooks), A≥15 (papers/guides)
- Assign IDs: G1-Gn, R1-Rn, L1-Ln, A1-An
- Record: credibility, accent variety, IPA system, audio quality, region, pedagogy

**Check**: G≥12, R≥3, L≥8, A≥15; language≈70%/25%/5% (±10%); recency≥40% last 5yr; diversity≥3 types, single<30%; accent coverage ≥8 AmE/BrE, ≥4 others

### 3. Generation
Per item: statement, difficulty, answer array (variants), normalization, rationale (≥1 [Ref: ID], ≥30% ≥2 types), fairness

**Check every 6**: Blanks clear, ≥70% ≥1 citation, ≥30% ≥2, 100% answer arrays, 100% normalization

### 4. Grading
Per item: common errors, borderline cases + partial credit, high-risk flags (severity + mitigation)

**Check**: 100% acceptance criteria, ≥50% common errors, partial credit defined, risks flagged

### 5. Compilation
Populate references, verify cross-refs, document shortfalls

**Check**: Floors met OR documented, zero broken refs, all fields complete

---

## Validation (13 Checks)

Execute sequentially. If ANY fails, fix and re-validate ALL.

1. **Counts**: G≥12, R≥3, L≥8, A≥15, Items=30-50, difficulty=20%/45%/35% (±5%)
2. **Citations**: ≥75% items ≥1, ≥35% items ≥2 distinct
3. **Language**: EN=60-80%, ZH=15-35%, Other=0-10%
4. **Recency**: ≥40% last 5yr
5. **Diversity**: ≥3 types, single<30%
6. **Links**: 100% accessible OR archived
7. **Cross-refs**: 100% [Ref: ID] resolve
8. **Answers**: 100% complete arrays with accent variants (AmE/BrE/IndE/AusE where applicable)
9. **Clarity**: 100% unambiguous blanks, IPA correctly formatted
10. **Normalization**: 100% rules specified, IPA conventions documented
11. **Conflicts**: ≥80% contested pronunciations have ≥2 accent variants
12. **Fairness**: Accent biases acknowledged, multiple variants accepted, regional differences documented, learner misconceptions addressed
13. **Self-check**: 1-12 PASS, topics covered (IPA/vowels/consonants/stress/intonation/accents/connected), accent comparisons (≥8 AmE/BrE, ≥4 others), rationales pedagogically valuable

**Report**:
```
| Check | Result | Status |
|-------|--------|--------|
| 1. Floors | G:X R:Y L:Z A:W I:N (F/I/A) | PASS/FAIL |
| 2. Citation | X% ≥1, Y% ≥2 | PASS/FAIL |
| 3. Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| 4. Recency | X% last 5yr | PASS/FAIL |
| 5. Diversity | N types, max P% | PASS/FAIL |
| 6. Links | Y/X accessible | PASS/FAIL |
| 7. Cross-refs | Y/X resolved | PASS/FAIL |
| 8. Answers | Y/X complete (accent variants) | PASS/FAIL |
| 9. Clarity | Y/X unambiguous, IPA correct | PASS/FAIL |
| 10. Normalization | Y/X specified, IPA conventions | PASS/FAIL |
| 11. Conflicts | Y/X compliant (Z%) | PASS/FAIL |
| 12. Fairness | Accents:[AmE/BrE/IndE/AusE] Variants:[...] | PASS/FAIL |
| 13. Self-check | Topics:[...] Comparisons:[AmE/BrE:X, Other:Y] Issues:[...] | PASS/FAIL |
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
- Learner Misconceptions: [L1 interference + mitigation [Ref: ID]]
- Accent Variants: ["AmE: /.../, BrE: /.../, IndE: /.../, AusE: /.../"]
- Regional: [AmE/BrE/IndE/AusE differences]
- Contested: [multiple pronunciations [Ref: ID]]
- Pedagogical: [tips, minimal pairs, drills]

**Rationale**: [Explanation with ≥1 [Ref: ID]: definitions, significance, limitations]

---

## References

### Glossary
**Term** (ID: G#): Definition [Lang]
- Stakeholders, Notes (risks, variants)

### Resources
**Resource** (ID: R#) (Type: Dictionary/Corpus/Audio/Tool | Access: URL/Platform)
- Description, Coverage, IPA System, Quality, Update, Accessibility

### Literature
**Title** (ID: L#) (Year) [Lang]
- Authors, Type, Findings, Accent Focus, IPA Usage, Credibility, Pedagogical Value

### APA Citations
[APA 7th] [Lang]
- Accent variety, IPA system, Applicability, Archive

---

## Validation Report

**Date**: [YYYY-MM-DD] | **Bank**: [Title] ([N] items) | **Validator**: [Name]

[Validation table: 13 checks PASS]

**Status**: READY

**Notes**: [Summary]
```

---

## Quality Principles

- **Context**: Explicit scope, audience, constraints, assumptions
- **Clarity**: Define jargon; unambiguous blanks
- **Precision**: Specific terms; consistent usage; complete arrays
- **MECE**: Mutually exclusive, collectively exhaustive clusters
- **Significance**: Prioritize high-value; flag high-risk
- **Concision**: Essential only; no redundancy
- **Accuracy**: Evidence-based with authoritative citations
- **Logic**: Coherent sequencing; foundational→advanced
- **Fairness**: Balanced; acknowledge assumptions, limitations, alternatives
- **Evidence**: Inline citations; ≥70% cited
- **Validation**: 13-step protocol; all PASS

---

## Submission Checklist

**Quantitative**:
- [ ] G≥12, R≥3, L≥8, A≥15
- [ ] Items: 30-50, Difficulty: 20%/45%/35% (±5%)
- [ ] Language: ~70%EN/~25%ZH/~5%other (±10%)
- [ ] Accent Coverage: ≥8 AmE/BrE, ≥4 others (IndE/AusE/CanE)

**Quality**:
- [ ] Recency: ≥40% last 5yr
- [ ] Diversity: ≥3 types; single<30%
- [ ] Citations: ≥75% ≥1; ≥35% ≥2 distinct

**Items**:
- [ ] 100% unambiguous blanks
- [ ] 100% complete answers with accent variants (AmE/BrE/IndE/AusE where applicable)
- [ ] 100% normalization rules (IPA conventions)
- [ ] 100% grading rubrics
- [ ] IPA symbols correctly formatted

**Sources**:
- [ ] Resources: type, coverage, IPA system, quality, accessibility
- [ ] 100% links accessible OR archived
- [ ] 100% [Ref: ID] resolve

**Fairness**:
- [ ] Learner misconceptions (L1 interference + mitigation)
- [ ] Multiple accent variants (AmE/BrE/IndE/AusE)
- [ ] Regional differences documented
- [ ] Pedagogical assumptions explicit
- [ ] Contested pronunciations ≥2 variants

**Validation**:
- [ ] All 13 PASS
- [ ] Report with quantitative results

**Deliverables**:
- [ ] Item bank: complete metadata
- [ ] TOC: sections linked
- [ ] References: 4 sections complete
- [ ] Validation: compliance demonstrated

**ALL CONFIRMED** → READY
