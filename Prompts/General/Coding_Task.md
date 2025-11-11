# Coding Task

Generate senior/architect-level coding assessments (18-28 tasks) with MECE coverage, evidence-based design, and comprehensive validation.

---

## Contents
- [Standards](#standards)
- [Workflow](#workflow)
- [Output Template](#output-template)
- [Validation](#validation)

---

## Standards

### Task Structure
- **Scope**: 18-28 tasks across 4-6 topic clusters (3-5 tasks each)
- **Difficulty**: 20% Foundational, 40% Intermediate, 40% Advanced
- **Components**: Self-contained problem (I/O spec, signature, constraints), 6-10 tests (3-5 public, 3-5 hidden), reference solution with complexity analysis, grading rubric (70% correctness, 20% edge cases, 10% style)
- **Language**: Use specific, consistent terms; define jargon inline or in glossary; avoid ambiguity
- **Context**: Explicitly state assumptions, scope boundaries, constraints, exclusions

### Citations & Evidence
- **Reference IDs**: G# (Glossary), C# (Codebase), L# (Literature), A# (APA)
- **Inline Format**: Use `[Ref: ID]` in problems/solutions when citing algorithms, patterns, complexity analysis
- **Source Types**: (1) Official docs (specs, RFCs), (2) Standards/peer-reviewed (ISO, IEEE, journals), (3) Audits/reports (security, industry), (4) Vetted code (production repos)
- **Language Mix**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH])
- **Floors**: ≥10 Glossary, ≥5 Codebase, ≥6 Literature, ≥12 APA citations
- **Quality Gates**:
  - Recency: ≥50% last 3yr (≥70% for AI/security)
  - Diversity: ≥3 source types, no single source >25%
  - Coverage: ≥70% tasks with ≥1 citation, ≥30% with ≥2
  - Maturity: License, last commit ≤12mo, stable release, audit status
  - Validity: Test all URLs or provide archived links
- **Uncertainty**: Flag unverified claims; cross-check facts

### Quality Requirements
- **MECE**: Complete, non-overlapping topic coverage
- **Significance**: State why each task matters, expected outcomes, stakeholder value
- **Risk/Value**: Document risks, costs, failure modes, mitigations, acceptance criteria
- **Fairness**: Acknowledge assumptions, limitations, biases, counterarguments, trade-offs
- **Logic**: Provide reasoning chains (invariants, proofs, decision logs) in solutions
- **Alternatives**: Document multiple valid approaches with trade-offs (time vs space, readability vs performance)
- **Practicality**: Ensure actionable guidance with measurable success criteria
- **Concision**: Include only essential information; remove redundancy

---

## Workflow

Execute steps sequentially with inline checks before proceeding.

### 1. Topic Planning
1. Identify 4-6 topic clusters; allocate 3-5 tasks each (total 18-28)
2. Assign difficulty levels: 20/40/40 distribution
3. **Check**: Total = 18-28? Difficulty ratio ≈20/40/40?

### 2. Reference Collection
1. Gather: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA sources
2. For each: Tag language, note year, classify type (1-4), assign ID
3. **Check**: Counts meet floors? Language ≈60/30/10? Recency ≥50% last 3yr? ≥3 source types?

### 3. Task Design
1. Write self-contained problem (I/O, signature, difficulty, language)
2. Include ≥1 `[Ref: ID]` when citing algorithms/patterns
3. State significance, fairness considerations, assumptions/exclusions
4. Create 6-10 tests (3-5 public, 3-5 hidden)
5. **Check** (every 4 tasks): Self-contained? Citations present? Fairness notes? Complete tests?

### 4. Solutions
1. Write working solution with time/space complexity
2. Document alternatives, trade-offs, risk mitigations
3. Provide reasoning (invariants, proof sketch, validation notes)
4. **Check**: All solutions present? Complexity + reasoning? Alternatives documented?

### 5. References
1. Populate Glossary, Codebase, Literature, APA sections
2. Include required fields (see [Output Template](#output-template))
3. Verify IDs match inline citations
4. **Check**: All `[Ref: ID]` resolve? Required fields present?

### 6. Final Validation
Run all validation checks; fix failures and re-validate until all pass (see [Validation](#validation)).

---

## Output Template

Start with TOC linking to all sections. Use lists, tables, code blocks (with language tags), Mermaid diagrams.

### Task Bank Structure

```markdown
## Contents
- [Task Bank](#task-bank)
  - [Topic 1](#topic-1-title)
    - [Task 1](#task-1-title)
- [References](#references)
  - [Glossary](#glossary-terminology--acronyms)
  - [Codebase](#codebase--library-references)
  - [Literature](#authoritative-literature--reports)
  - [APA Citations](#apa-style-source-citations)

---

## Task Bank

### Topic 1: [Title]

#### Task 1: [Title]
**Language:** [python/js/go/rust] | **Difficulty:** [Foundational/Intermediate/Advanced]

**Problem:** [Description with `[Ref: ID]` citations]

**Signature:** `function(params)` | **Constraints:** Time O(?), Memory O(?), Libs: [allowed]

**Starter Code:**
```[lang]
[Code skeleton]
```

**Assumptions & Exclusions:** [Scope boundaries, out-of-scope items]

**Public Tests:**
```[lang]
[3-5 test cases]
```

**Hidden Tests:** [Description of 3-5 additional test categories]

**Success Criteria:** [Measurable outcomes, pass/fail conditions]

**Reference Solution:**
```[lang]
[Working implementation]
```
**Complexity:** Time O(?), Space O(?) | **Alternatives:** [Other approaches + trade-offs] | **Reasoning:** [Invariants/proofs]

**Evidence & Uncertainty:** [Tie assertions to `[Ref: ID]`; flag unverified claims]

**Value & Risk:** [Why it matters, risks/costs, mitigations]

**Fairness & Bias:** [Assumptions, limitations, counterarguments]

**Grading:** Correctness 70%, Edges 20%, Style 10% | **Mistakes:** [Common errors] | **Misconceptions:** [List]

---

## References

### Glossary, Terminology & Acronyms
**G1. Term/Acronym**: Definition [Lang Tag]

### Codebase & Library References
**C1. [Name]** (GitHub: owner/repo | License: Type) [Lang]
- **Description:** Overview
- **Stack:** Technologies
- **Maturity:** Production/Beta/Experimental | **Last Update:** YYYY-MM
- **Performance:** Key metrics | **Security:** Audit status

### Authoritative Literature & Reports
**L1. [Title]** (Year) [Lang]
- **Authors:** Names/Org | **Type:** Standard/Paper/Report
- **Findings:** Summary | **Credibility:** Peer-reviewed/Standard/Regulatory
- **Jurisdiction:** Regions/markets

### APA Style Source Citations
Group by language (~60% EN, ~30% ZH, ~10% other). APA 7th + language tags.

**A1.** Author, A. (Year). Title. *Journal*, vol(issue), pages. DOI/URL [Lang]
```

---

## Validation

Execute all checks; present results in table; fix failures and re-validate until all pass.

### Validation Checks
1. **Counts**: Glossary ≥10, Codebase ≥5, Literature ≥6, APA ≥12, Tasks 18-28 (20/40/40 difficulty)
2. **Citations**: ≥70% tasks with ≥1, ≥30% with ≥2
3. **Language**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% last 3yr (≥70% AI/security)
5. **Diversity**: ≥3 source types, max 25% single source
6. **Links**: All URLs accessible or archived
7. **Cross-refs**: All `[Ref: ID]` resolve to entries
8. **Tests**: All tasks have 6-10 tests (3-5 public, 3-5 hidden)
9. **Solutions**: All tasks have solutions with complexity
10. **Constraints**: All tasks specify time/memory/libs
11. **Alternatives**: ≥80% multi-approach tasks document trade-offs
12. **Quality**: ≥90% tasks have significance, risk, fairness, reasoning notes
13. **Practicality**: ≥90% tasks have success criteria
14. **Concision**: No redundancy, consistent terminology, relevant content only

### Report Template
| Check | Result | Status |
|-------|--------|--------|
| Counts | G:X C:Y L:Z A:W T:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Tests | Y/X complete | PASS/FAIL |
| Solutions | Y/X present | PASS/FAIL |
| Constraints | Y/X specified | PASS/FAIL |
| Quality | Sig:X/Y Risk:W/Y Fair:V/Y Reason:U/Y | PASS/FAIL |
| Practicality | Y/X criteria | PASS/FAIL |
| Concision | Reviewed | PASS/FAIL |

**MANDATORY**: If any check fails, stop, fix, regenerate, re-validate. Submit only when all pass.


