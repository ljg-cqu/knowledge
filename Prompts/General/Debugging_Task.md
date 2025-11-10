# Debugging Task

Generate debugging task assessments with structured citations and multi-dimensional evaluation.

---

# Part I: Specifications

### Scope and Structure

- **Scope**: 15–22 tasks for senior/architect/expert level
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Bug Types**: Single focused bug (10–50 lines): off-by-one, type mismatch, API, concurrency, edge cases, logic, security, performance
- **Deliverables**: Buggy code, failing tests, corrected code (minimal fix), root-cause explanation (2–4 sentences)
- **Grading**: Fix 0–6 pts, Explanation 0–3 pts, Tests 0–1 pt; partial credit for correct diagnosis
- **Conflict Handling**: Document alternative valid fixes with trade-offs (minimal change vs comprehensive refactor)

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH])
- **Source Types**: (1) Official docs; (2) Standards/peer-reviewed; (3) Audits/reports; (4) Vetted code
- **Format**: APA 7th with language tags
- **Inline**: [Ref: ID] in root-cause explanations and code comments

### Reference Minimum Requirements

| Reference Section | Minimum | Content |
| --- | --- | --- |
| Glossary | ≥10 | Core concepts, jargon, acronyms |
| Codebase & Libraries | ≥5 | Stack components, SDKs, tools |
| Literature & Reports | ≥6 | Standards, peer-reviewed, audits |
| APA Citations | ≥12 | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception**: If minimum unmet, state shortfall and sourcing plan.

### Quality Gates

- **Recency**: ≥50% from last 3 years (≥70% for AI/security)
- **Diversity**: ≥3 source types; no single source >25%
- **Evidence**: ≥70% tasks have ≥1 citation; ≥30% have ≥2 distinct citations
- **Maturity**: Include license, last commit ≤12 months, stable release, audit status (if available)
- **Deduplication**: Canonicalize entries; use persistent links (DOIs, archived URLs)
- **Links**: Validate all URLs resolve or provide archived alternatives
- **Cross-refs**: Bind [Ref: ID] to Reference Sections entries

> **Scaling**: For >30 tasks, increase minimums by ~1.5× (round up).

### Pre-Submission Validation

Execute all steps. Present validation report. Fix failures and re-validate.

| Step | Verify | Pass Criteria |
| --- | --- | --- |
| 1. Count Audit | Glossary, Codebase, Literature, APA, Tasks | Meet minimums; 20/40/40 difficulty ratio |
| 2. Citation Coverage | Inline [Ref: ...] in explanations | ≥70% tasks have ≥1; ≥30% have ≥2 |
| 3. Language Distribution | [EN], [ZH], other tags | EN 50-70%, ZH 20-40%, Other 5-15% |
| 4. Recency | Publication years | ≥50% last 3yr (≥70% AI/security) |
| 5. Source Diversity | Citation types 1-4 | ≥3 types; no source >25% |
| 6. Links | URL resolution | All accessible or archived |
| 7. Cross-refs | [Ref: ID] → Reference Sections | All resolve |
| 8. Bug Focus | Single bug per task | No multi-bug tasks |
| 9. Fix Completeness | Corrected code + 2-4 sentence explanation | All complete |
| 10. Test Coverage | Failing + passing tests | All present |
| 11. Alternatives | Multiple valid approaches documented | ≥80% compliance |

**Report Format:**
```
| Check | Result | Status |
| Floors | G:X C:Y L:Z A:W T:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Languages | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Focus | Y/X single bugs | PASS/FAIL |
| Fixes | Y/X complete | PASS/FAIL |
| Tests | Y/X present | PASS/FAIL |
| Alternatives | Y/X documented | PASS/FAIL |
```

> **MANDATORY:** ALL checks must PASS before submission.

### Submission Checklist

- [ ] Minimums: Glossary ≥10, Codebase ≥5, Literature ≥6, APA ≥12
- [ ] Difficulty: 20/40/40 (Foundational/Intermediate/Advanced)
- [ ] Languages: ~60% EN, ~30% ZH, ~10% other
- [ ] Recency: ≥50% last 3yr (≥70% AI/security)
- [ ] Diversity: ≥3 types, no source >25%
- [ ] Citations: ≥70% tasks ≥1, ≥30% tasks ≥2
- [ ] Tasks: Single bugs, fixes, 2-4 sentence explanations
- [ ] Maturity: License, update ≤12mo, stable release, audit status
- [ ] Links: All resolve or archived
- [ ] Cross-refs: IDs in explanations → Reference Sections
- [ ] Tests: Failing + passing
- [ ] Validation: All checks PASS

---

# Part II: Instructions

Execute sequentially with inline checks before proceeding.

### Step 1: Planning
1. Identify 4-6 bug clusters (off-by-one, concurrency, API misuse, etc.)
2. Allocate 2-4 tasks per cluster (total 15-22)
3. Assign difficulty: 20/40/40 balance
4. **Check**: Total = 15-22, ratio ≈20/40/40

### Step 2: References
1. Gather minimums: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA
2. Tag language ([EN], [ZH]), note year, classify type (1-4)
3. Assign IDs: G1-Gn, C1-Cn, L1-Ln, A1-An
4. **Check**: Minimums met, language ≈60/30/10, recency ≥50% last 3yr, ≥3 types

### Step 3: Tasks
1. Create buggy code (10-50 lines, single bug), assign difficulty + language
2. Write root-cause explanation (2-4 sentences) with ≥1 [Ref: ID]
3. Provide failing test, corrected code
4. **Check**: Every 3 tasks verify single bugs, ≥1 citation, complete fixes, tests present

### Step 4: Alternatives
1. Document valid fixes, common mistakes, grading rubrics
2. **Check**: All tasks have rubrics and alternatives

### Step 5: Compile References
1. Populate Glossary, Codebase, Literature, APA sections
2. Ensure IDs match inline citations
3. **Check**: All [Ref: ID] resolve, required fields complete

### Step 6: Validate
Execute 11 validation steps (Part I). Present report. Fix failures and re-validate.

### Step 7: Submit
Complete Submission Checklist (Part I). Submit only when all checks PASS.

---

# Part III: Output Format

Start the output with a TOC (e.g., '## Contents') linking to all top-level headings and list items.

- Use lists tables diagrams formulas code blocks; diagrams in Mermaid; code with language-tagged fences.

```markdown
## Contents

- [Task Bank](#task-bank-tasks-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Task 1: [Bug description]](#task-1-bug-description)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Task 2: [Bug description]](#task-2-bug-description)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Task Bank (Tasks 1–N)

### Topic 1: [Topic title]

#### Task 1: [Bug description]

**Language:** [python/javascript/go/rust/solidity] | **Difficulty:** [Foundational/Intermediate/Advanced]

**Buggy Code:**
```[language]
[Code with bug; code comments may include [Ref: ID] citations when referencing API patterns or language specifications]
```

**Failing Output:** [Error or unexpected behavior]

**Failing Test:**
```[language]
[Test case]
```

**Corrected Code:**
```[language]
[Fixed code with comments]
```

**Root Cause:** [2–4 sentence explanation; include [Ref: ID] citations for specifications, patterns, known pitfalls]

**Passing Tests:**
```[language]
[Test cases]
```

**Grading:** [Rubric] | **Common mistakes:** [List] | **Alternatives:** [Other valid fixes]

---

## Reference Sections

**Usage**: [Ref: ID] in explanations/comments → G# (Glossary), C# (Codebase), L# (Literature), A# (APA)  
**Example**: "Bug stems from type coercion [Ref: G5] causing unexpected behavior [Ref: L3]."

| Section | Minimum | Content |
| --- | --- | --- |
| Glossary | ≥10 | Core concepts, jargon, acronyms |
| Codebase & Libraries | ≥5 | Stack components, SDKs, tools |
| Literature & Reports | ≥6 | Standards, peer-reviewed, audits |
| APA Citations | ≥12 | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception**: If minimum unmet, state shortfall and sourcing plan.

### Glossary, Terminology & Acronyms

**Format**: `**G#: Term/Acronym**: Definition [Lang]`  
**Example**: `**G1: MECE**: Framework ensuring non-overlapping, complete categories [EN]`

### Codebase & Library References

**Format**: `**C#: Project/Library** ([lang])`

**Required**: Stack/modules, license, last update ≤12mo, stable release, audit status  
**Optional**: Integration hooks, reliability, language support, vulnerabilities  
**Structure**: Repo URL (GitHub: owner/repo | License), docs URL, maturity

### Authoritative Literature & Reports

**Format**: `**L#: Title** (Year) ([lang])`

**Required**: Findings (bug patterns/vulnerabilities), methodology (sample, scope), impact (citations, standards)  
**Optional**: Limitations, replication, follow-ups, jurisdiction  
**Structure**: APA citation with language tag, persistent link (DOI/archived)

### APA Style Source Citations

**Format**: APA 7th edition, grouped by language (~60% EN, ~30% ZH, ~10% other), language tags

**Example**:
```
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms. Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx [EN]

张伟, & 李娜. (2024). 区块链技术应用研究. 计算机科学, 51(2), 88-95. [ZH]
```


