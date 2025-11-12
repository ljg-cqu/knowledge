# Coding Task

Generate senior/architect-level coding assessments with MECE coverage, evidence-based design, and validation.

## Contents
- [Standards](#standards)
- [Workflow](#workflow)
- [Output Template](#output-template)
- [Validation](#validation)

---

## Standards

### Task Structure
- **Scope**: 18-28 tasks, 4-6 clusters (3-5 tasks/cluster), 20/40/40 difficulty split (Foundational/Intermediate/Advanced)
- **Components**: Problem (I/O, signature, constraints), 6-10 tests (3-5 public, 3-5 hidden), solution (complexity, alternatives), rubric (70% correctness, 20% edges, 10% style)
- **Language**: Specific terms; define jargon inline/glossary; avoid ambiguity
- **Context**: State assumptions, scope, constraints, exclusions

### Citations & Evidence
- **IDs**: G# (Glossary), C# (Codebase), L# (Literature), A# (APA); use `[Ref: ID]` inline
- **Sources**: Official docs, standards/peer-reviewed, audits, vetted code
- **Mix**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH])
- **Minimums**: ≥10 G, ≥5 C, ≥6 L, ≥12 A
- **Quality**:
  - Recency: ≥50% <3yr (≥70% AI/security)
  - Diversity: ≥3 types, <25% single source
  - Coverage: ≥70% tasks ≥1 citation, ≥30% ≥2
  - Maturity: License, commit ≤12mo, stable, audit
  - Validity: Test URLs or archive
- **Uncertainty**: Flag unverified claims

### Quality Requirements
- **MECE**: Complete, non-overlapping coverage
- **Significance**: Why it matters, outcomes, value
- **Risk/Value**: Risks, costs, failures, mitigations, criteria
- **Fairness**: Assumptions, limits, biases, alternatives, trade-offs
- **Logic**: Reasoning (invariants, proofs)
- **Alternatives**: Multiple approaches + trade-offs
- **Practicality**: Actionable, measurable criteria
- **Concision**: Essential only; no redundancy

---

## Workflow

Execute sequentially; check before proceeding.

### 1. Topic Planning
1. Identify 4-6 clusters, 3-5 tasks/cluster (18-28 total)
2. Assign 20/40/40 difficulty split
3. **Check**: Total 18-28? Ratio ≈20/40/40?

### 2. Reference Collection
1. Gather: ≥10 G, ≥5 C, ≥6 L, ≥12 A
2. Tag language, year, type, ID
3. **Check**: Minimums met? Mix ≈60/30/10? Recency ≥50% <3yr? ≥3 types?

### 3. Task Design
1. Write problem (I/O, signature, difficulty, language)
2. Include ≥1 `[Ref: ID]` for algorithms/patterns
3. State significance, fairness, assumptions/exclusions
4. Create 6-10 tests (3-5 public, 3-5 hidden)
5. **Check** (every 4): Self-contained? Citations? Fairness? Tests complete?

### 4. Solutions
1. Write solution with time/space complexity
2. Document alternatives, trade-offs, mitigations
3. Provide reasoning (invariants, proofs)
4. **Check**: Solutions present? Complexity + reasoning? Alternatives?

### 5. References
1. Populate G, C, L, A sections
2. Include required fields (see [Output Template](#output-template))
3. Verify IDs match citations
4. **Check**: All `[Ref: ID]` resolve? Fields present?

### 6. Final Validation
Run all checks; fix failures; re-validate until pass (see [Validation](#validation)).

---

## Output Template

Start with TOC linking sections. Use lists, tables, code blocks (language-tagged), Mermaid diagrams.

### Structure

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

**Problem:** [Description with `[Ref: ID]`]

**Signature:** `function(params)` | **Constraints:** Time O(?), Memory O(?), Libs: [allowed]

**Starter:**
```[lang]
[Skeleton]
```

**Assumptions/Exclusions:** [Scope, out-of-scope]

**Public Tests:**
```[lang]
[3-5 cases]
```

**Hidden Tests:** [3-5 categories]

**Success Criteria:** [Measurable outcomes]

**Solution:**
```[lang]
[Implementation]
```
**Complexity:** Time O(?), Space O(?) | **Alternatives:** [Approaches + trade-offs] | **Reasoning:** [Invariants/proofs]

**Evidence:** [Tie to `[Ref: ID]`; flag uncertainty]

**Value/Risk:** [Importance, risks/costs, mitigations]

**Fairness:** [Assumptions, limits, counterarguments]

**Grading:** 70% correctness, 20% edges, 10% style | **Mistakes:** [Common] | **Misconceptions:** [List]

---

## References

### Glossary
**G1. Term/Acronym**: Definition [Lang]

### Codebase
**C1. [Name]** (GitHub: owner/repo | License) [Lang]
- **Description:** Overview
- **Stack:** Tech
- **Maturity:** Production/Beta/Experimental | **Update:** YYYY-MM
- **Performance:** Metrics | **Security:** Audit

### Literature
**L1. [Title]** (Year) [Lang]
- **Authors:** Names/Org | **Type:** Standard/Paper/Report
- **Findings:** Summary | **Credibility:** Peer-reviewed/Standard/Regulatory
- **Jurisdiction:** Regions

### APA Citations
Group by language (~60% EN, ~30% ZH, ~10% other). APA 7th + tags.

**A1.** Author, A. (Year). Title. *Journal*, vol(issue), pages. DOI/URL [Lang]
```

---

## Validation

Execute all; present in table; fix; re-validate until pass.

### Checks
1. **Counts**: G≥10, C≥5, L≥6, A≥12, Tasks 18-28 (20/40/40)
2. **Citations**: ≥70% tasks ≥1, ≥30% ≥2
3. **Language**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% <3yr (≥70% AI/security)
5. **Diversity**: ≥3 types, <25% single source
6. **Links**: URLs accessible/archived
7. **Cross-refs**: All `[Ref: ID]` resolve
8. **Tests**: All tasks 6-10 (3-5 public, 3-5 hidden)
9. **Solutions**: All have complexity
10. **Constraints**: All specify time/memory/libs
11. **Alternatives**: ≥80% document trade-offs
12. **Quality**: ≥90% have significance, risk, fairness, reasoning
13. **Practicality**: ≥90% have criteria
14. **Concision**: No redundancy, consistent terms, relevant only

### Report
| Check | Result | Status |
|-------|--------|--------|
| Counts | G:X C:Y L:Z A:W T:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% <3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Tests | Y/X complete | PASS/FAIL |
| Solutions | Y/X present | PASS/FAIL |
| Constraints | Y/X specified | PASS/FAIL |
| Quality | Sig:X/Y Risk:W/Y Fair:V/Y Reason:U/Y | PASS/FAIL |
| Practicality | Y/X criteria | PASS/FAIL |
| Concision | Reviewed | PASS/FAIL |

**MANDATORY**: Fix failures; re-validate until all pass.


