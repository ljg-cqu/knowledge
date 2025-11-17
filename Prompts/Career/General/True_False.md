# True/False Statements

Generate 18-32 senior/expert-level true/false statements testing deep technical understanding with authoritative evidence.

**Domain**: Technical fields (blockchain, AI, software architecture) with established standards/research/codebases.

**Requirements**: Objectively verifiable via authoritative sources. Opinion-based claims require context and alternatives.

---

## Workflow

### 1. Plan (MECE Coverage)

Identify **4-6 topic clusters** (mutually exclusive, collectively exhaustive):
- 3-6 statements per cluster (total: 18-32)
- Difficulty: 20% Foundational / 40% Intermediate / 40% Advanced

**Verify**: Total 18-32? Difficulty ≈20/40/40? Non-overlapping? Critical areas covered?

### 2. Collect References (Credibility)

**Minimums**: ≥10 Glossary | ≥5 Codebase | ≥6 Literature | ≥12 APA

**Source Hierarchy**:
1. Official docs (specs, RFCs, protocol docs)
2. Standards/peer-reviewed (ISO, IEEE, journals, conferences)
3. Audits/reports
4. Vetted code (production repos: license, commits ≤12mo, release ≥1.0.0)

**Exclude**: Blogs/tutorials (unless domain experts), unmaintained repos (>12mo), pre-release code

**Quality Gates**:
- Recency: ≥50% last 3yr (≥70% for AI/security/cloud)
- Diversity: ≥3 types, no single >25%
- Language: ~60% EN / ~30% ZH / ~10% other (tag all)
- Links: All accessible or archived

**IDs**: G1-Gn (Glossary) | C1-Cn (Codebase) | L1-Ln (Literature) | A1-An (APA)

**Verify**: Floors met? Language ≈60/30/10? Recency ≥50%? Types ≥3? Links valid?

### 3. Write Statements (Clarity & Logic)

**Statement** (≤2 lines, declarative, unambiguous):
- No double negatives
- Define jargon in Glossary
- Assign: Difficulty (Foundational/Intermediate/Advanced) | Answer (A=True / B=False)

**Rationale** (1-2 sentences):
- Explain WHY (not just restate)
- Cite ≥1 `[Ref: ID]` (≥2 for critical claims)
- Context-dependent: clarify assumptions, conditions, boundaries
- Controversial: acknowledge alternatives, limitations, trade-offs

**Verify every 5**: ≤2 lines? No double negatives? Unambiguous? Jargon defined? Rationale + citation complete? Context clear?

### 4. Balance (Fairness)

- True/False ratio: 45-55%
- No patterns (avoid TFTFTF, clustering)

**Verify**: Ratio 45-55%? No sequences? Distributed across topics/difficulty?

### 5. Compile References

**Glossary**: `**G#: Term**: Definition [Lang]`  
**Codebase**: `**C#: Name** ([lang])` — Stack, Maturity (license, update, release), Benchmarks  
**Literature**: `**L#: Title** (Year) ([lang])` — Findings, Methodology, Impact  
**APA**: APA 7th + language tags, grouped by language, persistent links

**Verify**: All `[Ref: ID]` resolve? Required fields present? No unused refs? APA + tags + links valid?

### 6. Validate (13 Checks)

Execute sequentially, fix failures, re-validate until all PASS:

1. **Floors**: G≥10, C≥5, L≥6, APA≥12, S:18-32, Difficulty ≈20/40/40
2. **Citations**: ≥70% with ≥1 cite, ≥30% with ≥2
3. **Language**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% last 3yr (≥70% for AI/security/cloud)
5. **Diversity**: ≥3 types, no single >25%
6. **Links**: 100% accessible/archived
7. **Cross-refs**: All `[Ref: ID]` resolve
8. **Clarity**: ≤2 lines, unambiguous
9. **Negatives**: No double negatives
10. **Rationales**: 1-2 sentences + citation
11. **Context**: ≥80% clarify assumptions
12. **Fairness**: True/False ratio 45-55%, no answer patterns
13. **Jargon**: 100% defined

**Report**:
```
| Check       | Result                      | Status    |
|-------------|------------------------------|-----------|
| Floors      | G:X C:Y L:Z APA:W S:N (F/I/A)| PASS/FAIL |
| Citations   | X% ≥1, Y% ≥2                 | PASS/FAIL |
| Language    | EN:X% ZH:Y% Other:Z%         | PASS/FAIL |
| Recency     | X% last 3yr                  | PASS/FAIL |
| Diversity   | N types, max P%              | PASS/FAIL |
| Links       | Y/X accessible               | PASS/FAIL |
| Cross-refs  | Y/X resolved                 | PASS/FAIL |
| Clarity     | Y/X clear                    | PASS/FAIL |
| Negatives   | Y/X free                     | PASS/FAIL |
| Rationales  | Y/X complete                 | PASS/FAIL |
| Context     | Y/X (Z%)                     | PASS/FAIL |
| Fairness    | Y/X (Z%)                     | PASS/FAIL |
| Jargon      | Y/X (Z%)                     | PASS/FAIL |
```

### 7. Final Check

- [ ] All 13 checks PASS
- [ ] Statements challenging yet fair
- [ ] Rationales provide learning value
- [ ] References accessible
- [ ] True/False balance 45-55%
- [ ] No answer patterns
- [ ] Output follows format exactly

---

## Output Format

```markdown
## Contents
- [Statement Bank](#statement-bank)
  - [Topic 1: Title](#topic-1-title)
- [References](#references)
  - [Glossary](#glossary-terminology--acronyms)
  - [Codebase](#codebase--library-references)
  - [Literature](#authoritative-literature--reports)
  - [APA Citations](#apa-style-source-citations)

---

## Statement Bank

### Topic 1: [Title]

#### S1: [Brief Description]

**Difficulty**: [Foundational/Intermediate/Advanced]

**Statement**: [Declarative claim ≤2 lines]

**Answer**: [A (True) / B (False)]

**Rationale**: [1-2 sentences with `[Ref: ID]`]

---

## References

**Usage**: `[Ref: G3]` (Glossary), `[Ref: C1]` (Codebase), `[Ref: L2]` (Literature), `[Ref: A7]` (APA)

**Minimums**: G≥10 | C≥5 | L≥6 | APA≥12 (target ~60% EN / ~30% ZH / ~10% other)

### Glossary, Terminology & Acronyms

**G#: Term**: Definition [Lang]  
**G#: Acronym** (Expansion): Definition [Lang]

### Codebase & Library References

**C#: Project/Library** ([lang])  
**Stack**: Components/SDKs  
**Maturity**: License, last commit ≤12mo, release ≥1.0.0  
**Benchmarks**: Performance, adoption  
**URL**: https://...

### Authoritative Literature & Reports

**L#: Title** (Year) ([lang])  
**Findings**: Main claims, standards  
**Methodology**: Sample size, scope  
**Impact**: Citations, adoption  
**URL**: DOI or archived link

### APA Style Source Citations

**English [EN]**  
Author, A. (Year). Title. *Journal*, vol(issue), pages. https://doi.org/... [EN]

**Chinese [ZH]**  
作者. (年份). 标题. *期刊*, 卷(期), 页码. [ZH]

**Other**  
[APA 7th + language tags]
```


