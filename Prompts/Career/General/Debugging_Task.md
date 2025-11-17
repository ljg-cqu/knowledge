# Debugging Assessment Generator

Generate 15-22 debugging tasks with buggy code, tests, fixes, root-cause analysis, and citations.

---

## I. Requirements

### Scope
| Element | Specification |
|---------|---------------|
| **Tasks** | 15-22 single-bug scenarios, 10-50 lines each |
| **Difficulty** | 20% Foundational / 40% Intermediate / 40% Advanced (±5%) |
| **Bug Types** | Off-by-one, type errors, API misuse, concurrency, edge cases, logic, security, performance |
| **Deliverables** | Buggy code + failing test + fix + root-cause (2-4 sentences) + passing tests |
| **Grading** | Code (0-6) + Explanation (0-3) + Tests (0-1) \| Partial credit for diagnosis |

### References
| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary (G#)** | 10 | Clear definitions + [Lang] tags |
| **Codebase (C#)** | 5 | License + update ≤12mo + stable + audit + docs |
| **Literature (L#)** | 6 | Persistent links (DOI/archived) |
| **APA (A#)** | 12 | APA 7th + [Lang]: EN 50-70% / ZH 20-40% / Other 5-15% |

**Scaling**: If you later expand the task bank beyond 30 tasks, multiply all reference minimums (G, C, L, A) by 1.5×
**Format**: APA 7th + language tags
**Inline**: `[Ref: ID]` (≥1 per task, 2+ for complex)
**Hierarchy**: Official docs → Standards/peer-reviewed → Security audits → Vetted codebases

### Quality Gates
| Gate | Criteria |
|------|----------|
| **Recency** | ≥50% last 3yr (≥70% for AI/security) |
| **Diversity** | ≥3 source types, max 25% single |
| **Coverage** | ≥70% tasks ≥1 cite; ≥30% tasks ≥2 cites |
| **Links** | 100% accessible/archived |
| **Cross-refs** | All `[Ref: ID]` resolve; no orphans |
| **Deduplication** | Canonical URLs, standardized names |

---

## II. Execution

### 1. Plan
- Identify 4-6 bug clusters (2-4 tasks each, max 30% per cluster)
- Assign difficulty per 20/40/40 ratio
- Select production-quality languages/frameworks

**Output**: Task allocation matrix (Cluster | Bug Type | Count | Difficulty | Language)

### 2. Gather References
- Collect: G≥10, C≥5, L≥6, A≥12
- Tag: [Lang], year, type
- Assign IDs: G#, C#, L#, A#
- Validate URLs (accessible/archived)
- Verify: Language distribution, recency, diversity

**Output**: Reference inventory (ID | Title | Year | Lang | Type | Status)

### 3. Create Tasks
**Per task**:
- Buggy code (10-50 lines, single bug, production-quality)
- Metadata (ID, difficulty, language, bug category)
- Root cause (2-4 sentences: symptom + mechanism + `[Ref: ID]` + impact)
- Failing test (standard framework, clear assertion)
- Fix (minimal, annotated, best practices)
- Passing tests (validate fix + edge cases)

**Validate every 3 tasks**: Single bug? Citations? Complete? Valid IDs? 10-50 lines? Difficulty tracking?

### 4. Add Alternatives
**Per task**:
- 2-3 valid approaches with trade-offs
- 3-5 common mistakes with `[Ref: ID]`
- Grading rubric (0-6-3-1 scale, partial credit)
- Edge cases and boundaries

**Target**: 100% rubrics; ≥80% alternatives; 100% list 3-5 mistakes

### 5. Compile References
- **Glossary**: `**G#: Term**: Definition [Lang]` (alphabetical)
- **Codebase**: `**C#: Library** ([Lang])` | Repo + license + update + version + audit + docs
- **Literature**: `**L#: Title** (Year) ([Lang])` | Citation + DOI + findings + methodology + impact
- **APA**: Grouped by language (EN / ZH / Other), alphabetized

**Validate**: All IDs cited? No orphans? Fields complete? URLs accessible? Tags present? Sequential?

### 6. Validate (11 Checks)
1. Count audit (G≥10, C≥5, L≥6, A≥12, Tasks 15-22, Ratio 20/40/40 (±5%))
2. Citation coverage (≥70% ≥1 cite, ≥30% ≥2 cites)
3. Language distribution (EN 50-70%, ZH 20-40%, Other 5-15%)
4. Recency (≥50% last 3yr, ≥70% for AI/security)
5. Source diversity (≥3 types, max 25% single)
6. Link validation (100% accessible/archived)
7. Cross-reference integrity (100% resolve, no orphans)
8. Bug focus (100% single-bug)
9. Fix completeness (100% fix + 2-4 sentences)
10. Test coverage (100% failing + passing)
11. Alternative documentation (≥80% alternatives + trade-offs)

Generate report (Check | Result | Status). Fix failures, re-validate until ALL PASS. Attach final report.

### 7. Submit
**Checklist**: References + Tasks + Citations + Technical rigor + Validation (ALL PASS)
**Review**: Coherence, spot-checks, formatting, TOC links, citations
**Submit when**: Checklist complete + ALL PASS + no placeholders

---

## III. Output Format

```markdown
## Contents
- [Task Bank](#task-bank) → [Topic 1](#topic-1) → [Task 1](#task-1) / [Task 2](#task-2) / ...
- [References](#references) → [Glossary](#glossary) / [Codebase](#codebase) / [Literature](#literature) / [APA](#apa)

---

## Task Bank

### Topic 1: [Bug Cluster Name]
[1-2 sentence description]

#### Task 1: [Bug Description]
**Language**: [lang] | **Difficulty**: [F/I/A]

**Buggy Code**:
```[lang]
[10-50 lines, single bug]
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

**Root Cause**: [Symptom]. [Mechanism]. [Source [Ref: ID]]. [Impact].

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

### Codebase & Libraries
**C#: Library** ([Lang])  
Repo: [URL] | License: [Type] | Updated: [YYYY-MM] | Stable: [Version] | Docs: [URL] | Audit: [Status]

### Literature & Reports
**L#: Title** (Year) ([Lang])  
Citation: [APA] | DOI: [Link] | Findings: [Key patterns] | Methodology: [Approach] | Impact: [Citations, adoption]

### APA Citations
**English [EN]** | **Chinese [ZH]** | **Other [Lang]**  
[Alphabetized APA 7th format entries]

---

## Validation Report
[11-check table: ALL PASS required]
```

---

## IV. Validation Protocol

Generate validation report before submission. ALL 11 checks must PASS.

| # | Check | Criteria |
|---|-------|----------|
| 1 | **Counts** | G≥10, C≥5, L≥6, A≥12, Tasks 15-22, Ratio 20/40/40 (±5%) |
| 2 | **Citations** | ≥70% tasks ≥1 cite; ≥30% tasks ≥2 cites |
| 3 | **Languages** | EN 50-70%, ZH 20-40%, Other 5-15% |
| 4 | **Recency** | ≥50% last 3yr (≥70% AI/security) |
| 5 | **Diversity** | ≥3 types; max 25% single |
| 6 | **Links** | 100% accessible/archived |
| 7 | **Cross-refs** | 100% resolve; no orphans |
| 8 | **Bug Focus** | 100% single-bug |
| 9 | **Fixes** | 100% fix + 2-4 sentences |
| 10 | **Tests** | 100% failing + passing |
| 11 | **Alternatives** | ≥80% alternatives + trade-offs |

**Report Format**:
```
| Check | Result | Status |
|-------|--------|--------|
| Count Audit | G:X C:Y L:Z A:W T:N (F/I/A: P%/Q%/R%) | PASS/FAIL |
...
**Overall**: PASS/FAIL | **Failed**: [List or None]
```

Re-validate after fixes until ALL PASS.


