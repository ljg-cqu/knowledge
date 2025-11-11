# Cloze / Fill-in-the-Blank Prompt

Generate 24–40 senior-level cloze assessment items with complete metadata, evidence-based rationales, and validation compliance.

---

## Task Definition

**Scope**: Create fill-in-the-blank items for [specify domain] targeting senior professionals (5+ years experience).

**Constraints**: 
- Audience level: [senior/architect/expert]
- Excluded topics: [deprecated APIs, out-of-scope areas]
- Time constraint: [if applicable]
- Emerging tech limitations: [limited peer-reviewed sources]

**Success Criteria**:
- 24–40 items (20% Foundational / 40% Intermediate / 40% Advanced)
- References: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA citations
- Language: ~60% EN, ~30% ZH, ~10% other
- Citations: ≥70% items with ≥1 citation; ≥30% items with ≥2 distinct citations
- Recency: ≥50% citations from last 3 years (≥70% for AI/security/blockchain)
- Source diversity: ≥3 types; no single source >25%
- 100% pass all 13 validation checks before submission

---

## Content Requirements

### Item Structure

Each item must include:

**1. Statement**: Sentence with ___ or [blank] placeholder

**2. Difficulty Level**: Foundational/Intermediate/Advanced

**3. Acceptable Answers**: Array of valid answers
- Primary answer (preferred term)
- Valid synonyms and abbreviations
- Regional variants (US/UK spellings, ZH/EN terms)
- All equivalent formulations

**4. Normalization Rules**:
- **Case**: case-insensitive (default) OR case-sensitive (if distinction critical)
- **Whitespace**: trim leading/trailing; normalize internal to single space
- **Punctuation**: strip non-semantic; retain semantic (hyphens, underscores)
- **Numeric**: specify tolerance ("10% ±2%", "5.0 ±0.1")
- **Units**: accept equivalents ("1000ms" = "1s" = "1 second")

**5. Grading**:
- **Full Credit**: conditions for 100%
- **Partial Credit**: scenarios and allocation ("50% for incomplete but directionally correct")
- **Common Incorrect**: frequent misconceptions
- **Borderline Cases**: edge cases requiring human judgment

**6. Rationale**:
- Evidence-based explanation with ≥1 [Ref: ID] citation
- Technical definitions from authoritative sources
- Practical significance and context
- Limitations, trade-offs, counterexamples
- ≥30% of items should have ≥2 distinct citations from different source types

**7. Fairness Notes**:
- **Regional Variants**: terminology/practice variations by jurisdiction
- **Stakeholder Perspectives**: differing priorities (developer vs. operator)
- **Contested Terminology**: multiple valid definitions across schools/regions
- **Risk Flags**: high-risk misconceptions with severity (Low/Medium/High) and mitigation
- **Assumptions**: make implicit assumptions explicit

### Reference Requirements

**Glossary (≥10 entries)**:
```
**Term/Acronym** (ID: G#): Definition [Language Tag]
- Stakeholders: [affected roles]
- Notes: [risks, assumptions, limitations, regional variants]
```

**Codebase (≥5 entries)**:
```
**Project Name** (ID: C#) (GitHub: owner/repo | License: Type)
- Description: [purpose and capabilities]
- Maturity: Production/Beta/Experimental
- Last Update: [date] OR Version [X.Y.Z] ([date])
- Security: [audit status, vulnerabilities, hardening]
- Risks/Mitigations: [limitations] / [suggested fixes]
```

**Literature (≥6 entries)**:
```
**Title** (ID: L#) (Year) [Language Tag]
- Authors: [names/organization]
- Type: Standard/Academic/White Paper/Audit/Industry Report
- Key Findings: [summary]
- Credibility: [peer-reviewed/industry standard/regulatory authority]
- Jurisdiction: [applicable regions/markets]
- Stakeholder Impact: [affected parties] | Risks/Mitigations: [summary]
```

**APA Citations (≥12 entries)**:
```
[APA 7th Citation] [Language Tag]
    Risk notes: [limitations, caveats]
    Applicability: [jurisdictional/contextual boundaries]
    Archive: [archived URL if non-persistent]
```

---

## Execution Workflow

### Step 1: Planning

1. **Define Topic Clusters** (4-6 clusters using MECE principle)
2. **Allocate Items** (4-8 items per cluster, 24-40 total)
3. **Assign Difficulty** (20% Foundational / 40% Intermediate / 40% Advanced)
4. **Document Assumptions**:
   - Audience: seniority, role, experience
   - Prerequisites: required knowledge
   - Regulatory Context: jurisdictions, compliance
   - Exclusions: out-of-scope topics
   - Contested Areas: multiple valid interpretations

**Check**: Items=24-40, distribution≈20%/40%/40% (±5%), clusters are MECE, assumptions documented

### Step 2: Reference Collection

1. **Gather Sources**:
   - Glossary ≥10, Codebase ≥5, Literature ≥6, APA ≥12
   - Tag language: [EN], [ZH], [JA], [KO], [DE], etc.
   - Classify type: (1) Official Docs, (2) Standards/Peer-Reviewed, (3) Audits/Reports, (4) Vetted Code
   - Record publication year

2. **Assign IDs**: G1-Gn, C1-Cn, L1-Ln, A1-An

3. **Record Metadata**: credibility, jurisdiction, risk notes, gaps

**Check**: Floor counts met, language≈60%/30%/10% (±10%), recency≥50% (≥70% for AI/security/blockchain), diversity≥3 types with no single type>25%

### Step 3: Item Generation

For each item:
1. Write statement with unambiguous blank placement
2. Assign difficulty level
3. Define complete acceptable answer array with all variants
4. Specify normalization rules (case, whitespace, punctuation, numeric, units)
5. Write rationale with ≥1 [Ref: ID] citation (≥30% of items need ≥2 citations from different source types)
6. Document fairness considerations (regional, stakeholder, contested terms, risks, assumptions)

**Check every 6 items**: Blanks unambiguous, ≥70% cumulative with ≥1 citation, ≥30% cumulative with ≥2 citations, 100% complete answer arrays, 100% normalization rules specified

### Step 4: Grading Framework

For each item:
1. List common incorrect answers with explanations
2. Define borderline cases with partial credit allocation
3. Flag high-risk misconceptions (severity + mitigation)
4. Note stakeholder-specific considerations

**Check**: All items have acceptance criteria, normalization rules, ≥50% have common incorrect answers documented, borderline cases with partial credit defined, high-risk misconceptions flagged with mitigation

### Step 5: Reference Compilation

1. Populate all reference sections with complete metadata
2. Verify cross-reference integrity: all [Ref: ID] inline citations resolve to reference entries
3. Document shortfalls if any section fails floor count (gap + rationale + mitigation plan)

**Check**: Floors met OR shortfalls documented, zero broken references, all required fields populated, codebase entries include license/update/risks, literature includes type/year/credibility/jurisdiction

---

## Validation Protocol (13 Mandatory Checks)

Execute ALL steps sequentially. Document results. If ANY fails, fix and re-validate ALL steps.

**1. Count Audit**: Verify G≥10, C≥5, L≥6, A≥12, Items=24-40, difficulty=20%/40%/40% (±5%)

**2. Citation Coverage**: ≥70% items with ≥1 citation, ≥30% items with ≥2 distinct citations

**3. Language Distribution**: EN=50-70%, ZH=20-40%, Other=5-15%

**4. Recency**: ≥50% from last 3 years (≥70% for AI/security/blockchain)

**5. Source Diversity**: ≥3 types used, no single type>25%

**6. Link Validation**: 100% URLs accessible OR archived alternative provided

**7. Cross-Reference Integrity**: 100% inline [Ref: ID] resolve to reference entries

**8. Answer Completeness**: 100% items have complete, non-empty answer arrays

**9. Blank Clarity**: 100% items have unambiguous blank placement with sufficient context

**10. Normalization Rules**: 100% items specify case/whitespace/punctuation/numeric/unit handling

**11. Conflict Handling**: ≥80% of items with contested terminology include ≥2 valid variants

**12. Fairness & Risk Review**: All Medium/High risks have mitigation strategies, multiple stakeholder perspectives represented, regional variations acknowledged, assumptions documented

**13. Self-Check**: Steps 1-12 all PASS, items implementable by target audience, rationales provide learning value, success criteria met, zero outstanding issues

**Validation Report Template**:
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

**Submission Requirement**: ALL 13 checks must show PASS before submission.

---

## Output Format

```markdown
## Contents
- [Item Bank](#item-bank)
  - [Topic 1: Title](#topic-1-title)
    - [Item 1: Description](#item-1-description)
  - [Topic 2: Title](#topic-2-title)
- [References](#references)
  - [Glossary](#glossary)
  - [Codebase](#codebase)
  - [Literature](#literature)
  - [APA Citations](#apa-citations)
- [Validation Report](#validation-report)

---

## Item Bank

### Topic 1: [Title]

#### Item 1: [Description]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Statement:** [Sentence with ___ or [blank]]

**Acceptable Answers:** ["primary", "synonym", "regional variant", "abbreviation"]

**Normalization & Tolerances:**
- Case: [case-insensitive/case-sensitive]
- Whitespace: [trim and normalize]
- Punctuation: [strip non-semantic/retain all]
- Numeric Tolerance: [N/A / "±X%" or "±X units"]
- Unit Handling: [N/A / "1000ms=1s=1 second"]

**Grading:**
- Full Credit: [conditions]
- Partial Credit: [conditions and allocation]
- Common Incorrect: ["error 1", "error 2"]
- Borderline Cases: ["edge case: explanation"]

**Risk & Fairness Notes:**
- Misconceptions: [high-risk errors with mitigation [Ref: ID]]
- Stakeholder Nuances: ["perspective differences"]
- Regional Variants: ["US vs UK terms"]
- Contested Terminology: ["varies by source [Ref: ID]"]

**Rationale:** [Explanation with ≥1 [Ref: ID] citation covering definitions, significance, context, limitations, counterexamples]

---

## References

### Glossary

**Term** (ID: G#): Definition [Language Tag]
- Stakeholders: [roles]
- Notes: [risks, assumptions, limitations, variants]

### Codebase

**Project** (ID: C#) (GitHub: owner/repo | License: Type)
- Description: [purpose]
- Maturity: [Production/Beta/Experimental]
- Last Update: [date] OR Version [X.Y.Z] ([date])
- Security: [audit status, vulnerabilities]
- Risks/Mitigations: [limitations] / [fixes]

### Literature

**Title** (ID: L#) (Year) [Language Tag]
- Authors: [names/org]
- Type: [classification]
- Key Findings: [summary]
- Credibility: [source]
- Jurisdiction: [regions]
- Stakeholder Impact: [parties] | Risks/Mitigations: [summary]

### APA Citations

[APA 7th Citation] [Language Tag]
    Risk notes: [limitations]
    Applicability: [boundaries]
    Archive: [URL if applicable]

---

## Validation Report

**Date**: [YYYY-MM-DD]
**Item Bank**: [Title] ([N] items)
**Validator**: [Name/Role]

[Insert validation table showing all 13 checks with PASS status]

**Overall Status**: ALL CHECKS PASSED — Ready for submission

**Notes**: [Summary of exceeded minimums, distributions, stakeholder coverage]
```

---

## Quality Principles

**Context**: Scope, audience, constraints, assumptions clearly stated upfront

**Clarity**: Definitions for domain jargon; unambiguous blank placement

**Precision**: Specific terminology; consistent usage; complete answer arrays

**Relevance**: Focus on material concepts; exclude trivial details

**MECE**: Topic clusters mutually exclusive and collectively exhaustive

**Sufficiency**: Comprehensive coverage within defined scope

**Breadth**: Multiple perspectives (regional, stakeholder, methodological) where appropriate

**Depth**: Rationales provide actionable insights beyond answer keys

**Significance**: Prioritize high-value concepts; flag high-risk misconceptions

**Concision**: Essential information only; no redundancy

**Accuracy**: Evidence-based with authoritative citations

**Credibility**: Prefer peer-reviewed, standards-body, and vetted sources

**Logic**: Coherent sequencing; foundational items support advanced

**Risk/Value**: Explicit risk flags with severity and mitigation

**Fairness**: Balanced perspectives; acknowledge assumptions, limitations, alternatives

**Structure**: TOC, hierarchical organization, consistent formatting

**Evidence**: Inline citations for factual claims; ≥70% items cited

**Validation**: 13-step mandatory protocol; all must PASS

**Practicality**: Grading implementable; items appropriate for target audience

**Success Criteria**: Measurable quantitative floors and quality gates

---

## Submission Checklist

Before submission, confirm ALL items:

**Quantitative**:
- [ ] Floors: G≥10, C≥5, L≥6, A≥12
- [ ] Items: 24-40 total
- [ ] Difficulty: 20%/40%/40% (±5%)
- [ ] Language: ~60%EN/~30%ZH/~10%other (±10%)

**Quality**:
- [ ] Recency: ≥50% last 3yr (≥70% for AI/security/blockchain)
- [ ] Diversity: ≥3 types; no single type>25%
- [ ] Citations: ≥70% items with ≥1; ≥30% items with ≥2 distinct

**Items**:
- [ ] Blanks: 100% unambiguous
- [ ] Answers: 100% complete with variants
- [ ] Normalization: 100% rules specified
- [ ] Grading: 100% rubrics defined

**Sources**:
- [ ] Codebase: license, update, maturity, risks documented
- [ ] Links: 100% accessible OR archived
- [ ] Cross-refs: 100% [Ref: ID] resolve

**Fairness**:
- [ ] Risks: High-risk practices flagged with severity and mitigation
- [ ] Stakeholders: Multiple perspectives represented
- [ ] Regional: Geographic variations acknowledged
- [ ] Assumptions: Implicit made explicit
- [ ] Contested: Valid variants included

**Validation**:
- [ ] All 13 checks: PASS status
- [ ] Validation report: Included with quantitative results

**Deliverables**:
- [ ] Item bank: Complete metadata
- [ ] TOC: All sections linked
- [ ] References: All 4 sections complete
- [ ] Validation report: Demonstrates compliance

**ALL ITEMS CONFIRMED** → Ready for submission
