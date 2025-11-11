# Debugging Assessment Generator

Generate senior/architect/expert-level debugging assessments: 15-22 tasks with buggy code, tests, fixes, root-cause analysis, and authoritative citations.

---

## I. Core Requirements

### Scope
- **Tasks**: 15-22 single-bug scenarios (10-50 lines each)
- **Difficulty**: 20% Foundational / 40% Intermediate / 40% Advanced (±5%)
- **Bug Types**: Off-by-one, type mismatches, API misuse, concurrency, edge cases, logic errors, security, performance
- **Deliverables** (per task): Buggy code + failing test + fix + root-cause (2-4 sentences) + passing tests
- **Grading**: Code (0-6pts) + Explanation (0-3pts) + Tests (0-1pt) | Partial credit for correct diagnosis

### References (Minimums)
| Type | Count | Purpose | Requirements |
|------|-------|---------|--------------|
| **Glossary** | ≥10 | Define jargon, acronyms | Clear definitions |
| **Codebase/Libraries** | ≥5 | Tools, SDKs, frameworks | License, update ≤12mo, stable release, audit status |
| **Literature/Reports** | ≥6 | Standards, peer-reviewed, audits | Persistent links (DOI/archived) |
| **APA Citations** | ≥12 | All authoritative sources | EN 50-70% / ZH 20-40% / Other 5-15% |

**Scaling**: For >30 tasks, multiply minimums by 1.5×

### Citation Standards
- **Format**: APA 7th + language tags ([EN], [ZH], etc.)
- **IDs**: G# (Glossary), C# (Codebase), L# (Literature), A# (APA)
- **Inline Usage**: `[Ref: ID]` in root-cause explanations (≥1 per task required, 2+ for complex bugs)
- **Source Hierarchy**: (1) Official docs → (2) Standards/peer-reviewed → (3) Security audits → (4) Vetted codebases

### Quality Gates
1. **Recency**: ≥50% sources from last 3yr (≥70% for AI/security)
2. **Source Diversity**: ≥3 types, no single type >25%
3. **Citation Coverage**: ≥70% tasks have ≥1 citation; ≥30% tasks have ≥2 citations
4. **Codebase Maturity**: Open-source license + update ≤12mo + stable + audit status
5. **Link Validation**: 100% URLs accessible or archived (DOI preferred)
6. **Cross-Reference Integrity**: Every `[Ref: ID]` maps to exactly one entry; no orphans
7. **Deduplication**: Merge duplicates, use canonical URLs, standardize names

---

## II. Execution Steps

### 1. Planning
- **Identify** 4-6 bug clusters aligned with role (select from bug types above)
- **Allocate** 2-4 tasks per cluster; total 15-22; no cluster >30%
- **Assign** difficulty per 20/40/40 ratio; balance within clusters
- **Select** languages/frameworks matching role; use production-quality patterns

**Output**: Task allocation matrix (Cluster | Bug Type | Count | Difficulty | Language)

### 2. References
- **Gather** references meeting minimums (G≥10, C≥5, L≥6, A≥12)
- **Tag** with language ([EN], [ZH], etc.), year, source type
- **Assign** unique IDs (G1-Gn, C1-Cn, L1-Ln, A1-An)
- **Validate** all URLs (HTTP 200 or archived)
- **Verify** language distribution (60/30/10), recency (≥50% last 3yr), diversity (≥3 types, max 25% single)

**Output**: Reference inventory (ID | Title | Year | Lang | Type | Status)

### 3. Tasks (for each)
- **Buggy Code**: 10-50 lines, single bug, production-quality, realistic context
- **Metadata**: ID, difficulty, language, bug category
- **Root Cause**: 2-4 sentences (symptom + mechanism + `[Ref: ID]` + optional impact)
- **Failing Test**: Standard framework, demonstrates bug, clear assertion message
- **Fix**: Minimal surgical changes, annotated, follows best practices
- **Passing Tests**: Validate fix + edge cases

**Validation** (every 3 tasks): Single bug? Citations present? Complete deliverables? Valid IDs? 10-50 lines? Difficulty tracking?

### 4. Alternatives (for each task)
- **Valid Approaches**: 2-3 alternatives (minimal fix / refactor / alternative pattern) with trade-offs
- **Common Mistakes**: 3-5 wrong approaches with explanations + `[Ref: ID]` for misconceptions
- **Grading Rubric**: Apply standard 0-6-3-1 scale; award partial credit for correct diagnosis
- **Edge Cases**: Note boundaries, assumptions, when to award partial credit

**Target**: 100% have rubrics; ≥80% document alternatives; 100% list 3-5 mistakes

### 5. Compile References
- **Glossary**: `**G#: Term**: Definition [Lang]` (alphabetical)
- **Codebase**: `**C#: Library** ([Lang])` | Repo + license + update + version + audit + docs
- **Literature**: `**L#: Title** (Year) ([Lang])` | Citation + DOI + findings + methodology + impact
- **APA**: APA 7th format, grouped by language (EN / ZH / Other), alphabetized within groups

**Validate**: All IDs cited? No orphans? All fields complete? URLs accessible? Language tags present? Sequential numbering?

### 6. Validate
- **Execute** 11 checks:
  1. Count audit (G≥10, C≥5, L≥6, A≥12, Tasks 15-22, Ratio 20/40/40)
  2. Citation coverage (≥70% ≥1 cite, ≥30% ≥2 cites)
  3. Language distribution (EN 50-70%, ZH 20-40%, Other 5-15%)
  4. Recency (≥50% last 3yr, or ≥70% for AI/security)
  5. Source diversity (≥3 types, max 25% single)
  6. Link validation (100% accessible/archived)
  7. Cross-reference integrity (100% resolve, no orphans)
  8. Bug focus (100% single-bug)
  9. Fix completeness (100% have fix + 2-4 sentence explanation)
  10. Test coverage (100% have failing + passing tests)
  11. Alternative documentation (≥80% have alternatives + trade-offs)

- **Generate** report: Table with Check | Result | PASS/FAIL | Overall Status
- **Fix** failures; **re-validate** until ALL PASS (2-3 cycles expected)
- **Attach** final ALL PASS report

### 7. Submit
- **Complete** checklist: References (quantities) + Tasks (15-22, ratio, focus, length, deliverables) + Citations (language, recency, diversity, coverage) + Technical rigor (maturity, links, cross-refs, tests, alternatives) + Validation (report attached, ALL PASS, zero failures) + Success criteria
- **Assemble**: Assessment + validation report + metadata + optional notes
- **Review**: Coherence, spot-check tasks, formatting, TOC links, random citations
- **Submit** only when: Checklist complete + validation ALL PASS + format correct + no placeholders

---

## III. Output Format

```markdown
## Contents
- [Task Bank](#task-bank)
  - [Topic 1: [Bug Cluster]](#topic-1)
    - [Task 1](#task-1) / [Task 2](#task-2) / ...
- [References](#references)
  - [Glossary](#glossary) / [Codebase](#codebase) / [Literature](#literature) / [APA Citations](#apa)

---

## Task Bank

### Topic 1: [Bug Cluster Name]
[1-2 sentence cluster description]

#### Task 1: [Bug Description]
**Language**: [lang] | **Difficulty**: [F/I/A]

**Buggy Code**:
```[lang]
[10-50 lines, single bug, may include [Ref: ID] in comments]
```

**Failing Output**: `[error/trace/behavior]`

**Failing Test**:
```[lang]
[Test demonstrating bug]
```

**Corrected Code**:
```[lang]
[Minimal fix with annotation]
```

**Root Cause**: [Symptom]. [Mechanism]. [Authoritative source [Ref: ID]]. [Optional impact].

**Passing Tests**:
```[lang]
[Tests validating fix + edge cases]
```

**Grading Rubric**:
- **Code (0-6)**: 6=correct+minimal+best; 4-5=correct+issues; 2-3=partial; 1=wrong+understanding; 0=none/wrong
- **Explanation (0-3)**: 3=accurate+cited; 2=accurate-citation; 1=partial; 0=wrong/missing
- **Tests (0-1)**: 1=present+validates; 0=missing/wrong

**Common Mistakes**:
1-5. [Mistake]: [Why wrong] [Ref: ID]

**Alternative Fixes**:
- **Minimal**: [Desc] | Trade-off: [Quick, preserves debt]
- **Refactor**: [Desc] | Trade-off: [Better design, more effort]
- **Alternative**: [Desc] | Trade-off: [Different performance]

---

[Repeat for 15-22 tasks]

---

## References

### Glossary
**G#: Term**: Definition [Lang]

**Examples**:
- **G1: Race Condition**: Output depends on timing of uncontrollable events [EN]
- **G2: MECE**: Mutually Exclusive, Collectively Exhaustive framework [EN]

---

### Codebase & Libraries
**C#: Library** ([Lang])
- **Repo**: [URL]
- **License**: [Type]
- **Last Update**: [YYYY-MM]
- **Stable Release**: [Version]
- **Docs**: [URL]
- **Audit**: [Status]

**Example**:
**C1: Go sync** ([EN])
- Repo: https://go.googlesource.com/go/+/refs/heads/master/src/sync
- License: BSD-3-Clause | Updated: 2024-10 | Stable: 1.21+ | Docs: https://pkg.go.dev/sync | Audit: Go security program

---

### Authoritative Literature & Reports
**L#: Title** (Year) ([Lang])
- **Citation**: [APA]
- **DOI/Link**: [Persistent]
- **Key Findings**: [Relevant patterns]
- **Methodology**: [Approach]
- **Impact**: [Citations, adoption]

**Example**:
**L1: IEEE Std 1012-2016** (2016) ([EN])
- Citation: IEEE. (2016). IEEE Standard for System, Software, and Hardware V&V. https://doi.org/10.1109/IEEESTD.2016.7460968
- Findings: V&V processes for defect detection; edge case + concurrency emphasis
- Methodology: Industry consensus working group
- Impact: >500 citations, safety-critical systems

---

### APA Citations

**English Sources [EN]**
[Alphabetized APA 7th format entries] [EN]

**Chinese Sources [ZH]**
[Alphabetized APA 7th format entries] [ZH]

**Other Languages**
[Alphabetized APA 7th format entries] [Lang code]

---

## Validation Report
[Attach 11-check validation table showing ALL PASS before submission]
```

---

## Validation Protocol

**Mandatory**: Generate validation report before submission.

| Check | Pass Criteria |
|-------|---------------|
| 1. Counts | G≥10, C≥5, L≥6, A≥12, Tasks 15-22, Ratio 20/40/40 (±5%) |
| 2. Citations | ≥70% tasks ≥1 cite; ≥30% tasks ≥2 cites |
| 3. Languages | EN 50-70%, ZH 20-40%, Other 5-15% |
| 4. Recency | ≥50% last 3yr (≥70% AI/security) |
| 5. Diversity | ≥3 types; max 25% single |
| 6. Links | 100% accessible/archived |
| 7. Cross-refs | 100% resolve; no orphans |
| 8. Bug focus | 100% single-bug |
| 9. Fixes | 100% have fix + 2-4 sentences |
| 10. Tests | 100% failing + passing |
| 11. Alternatives | ≥80% have alternatives + trade-offs |

**Format**:
```
| Check | Result | Status |
|-------|--------|--------|
| Count Audit | G:X C:Y L:Z A:W T:N (F/I/A: P%/Q%/R%) | PASS/FAIL |
...
**Overall**: PASS/FAIL
**Failed**: [List or None]
```

**Requirement**: ALL 11 must show PASS. Re-validate after fixes until clean pass.


