# True/False Statements

Generate senior/expert-level true/false assessments with authoritative evidence and comprehensive validation.

## Context & Scope

**Purpose**: Create 18-32 technical true/false statements testing deep conceptual understanding (not memorization) for senior engineers, architects, and domain experts.

**Domain**: Technical fields (blockchain, AI, software architecture) with established standards, research, and production codebases.

**Requirements**: Statements must be objectively verifiable through authoritative sources. Avoid opinion-based claims unless explicitly qualified with context and alternative perspectives.

---

## Workflow

### 1. Plan (MECE Coverage)

Identify **4-6 topic clusters** (mutually exclusive, collectively exhaustive):
- Each cluster addresses distinct domain aspect
- Allocate 3-6 statements per cluster (total: 18-32)
- Assign difficulty: 20% Foundational / 40% Intermediate / 40% Advanced

**Verify**: Total 18-32? Difficulty ≈20/40/40? Clusters non-overlapping? Critical areas covered?

### 2. Collect References (Credibility)

**Minimums**: ≥10 Glossary | ≥5 Codebase | ≥6 Literature | ≥12 APA Citations

**Source Hierarchy** (prioritize top):
1. Official docs (specs, RFCs, protocol docs)
2. Standards/peer-reviewed (ISO, IEEE, journals, conferences)
3. Audits/reports (security audits, industry analyses)
4. Vetted code (production repos: license, commits ≤12mo, stable release ≥1.0.0, audits)

**Exclude**: Blogs/tutorials (unless domain experts), unmaintained repos (>12mo), pre-release code, biased sources

**Quality Gates**:
- Recency: ≥50% last 3yr (≥70% for AI/security/cloud)
- Diversity: ≥3 source types, no single source >25%
- Language: ~60% EN / ~30% ZH / ~10% other (tag all: [EN], [ZH])
- Links: All accessible or archived (DOIs, archive.org)

**Assign IDs**: G1-Gn (Glossary) | C1-Cn (Codebase) | L1-Ln (Literature) | A1-An (APA)

**Verify**: Floors met? Language ≈60/30/10? Recency ≥50%? Types ≥3? Links valid?

### 3. Write Statements (Clarity & Logic)

**Statement** (≤2 lines, declarative, unambiguous):
- No double negatives ("not impossible" → "possible")
- Define technical jargon in Glossary
- Assign: Difficulty (Foundational/Intermediate/Advanced) | Answer (A=True / B=False)

**Rationale** (1-2 sentences):
- Explain WHY true/false (not just restate)
- Cite ≥1 `[Ref: ID]` per rationale (≥2 for critical claims)
- For context-dependent: clarify assumptions, conditions, boundaries
- For controversial: acknowledge alternatives, limitations, trade-offs

**Verify every 5 statements**: ≤2 lines? No double negatives? Unambiguous? Jargon defined? Rationale complete? ≥1 citation? Context clarified?

### 4. Balance (Fairness)

- True/False ratio: 45-55%
- No patterns (avoid TFTFTF, clustering by topic/difficulty)

**Verify**: Ratio 45-55%? No detectable sequences? Distributed across topics/difficulty?

### 5. Compile References

**Glossary**: `**G#: Term**: Definition [Lang]`  
**Codebase**: `**C#: Name** ([lang])` — Stack/Modules, Maturity (license, update, release), Benchmarks  
**Literature**: `**L#: Title** (Year) ([lang])` — Core Findings, Methodology, Impact  
**APA**: APA 7th + language tags, grouped by language, persistent links

**Verify**: All `[Ref: ID]` resolve? Required fields present? No unused refs? APA correct? Language tags? Links valid?

### 6. Validate (13 Checks)

Execute sequentially, fix failures, re-validate until all PASS:

1. **Floors**: G≥10, C≥5, L≥6, APA≥12, Statements 18-32, Difficulty ≈20/40/40
2. **Citations**: ≥70% statements with ≥1 cite, ≥30% with ≥2
3. **Language**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% last 3yr (≥70% AI/security)
5. **Diversity**: ≥3 types, no single >25%
6. **Links**: 100% accessible or archived
7. **Cross-refs**: All `[Ref: ID]` resolve (G#→Glossary, C#→Codebase, L#→Literature, A#→APA)
8. **Clarity**: All statements ≤2 lines, unambiguous
9. **Negatives**: No double negatives
10. **Rationales**: All 1-2 sentences with citation
11. **Context**: Context-dependent statements clarify assumptions (≥80%)
12. **Fairness**: Controversial statements balanced (≥90%)
13. **Jargon**: 100% defined in Glossary

**Report**:
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X C:Y L:Z APA:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Clarity | Y/X clear | PASS/FAIL |
| Negatives | Y/X free | PASS/FAIL |
| Rationales | Y/X complete | PASS/FAIL |
| Context | Y/X (Z%) | PASS/FAIL |
| Fairness | Y/X (Z%) | PASS/FAIL |
| Jargon | Y/X (Z%) | PASS/FAIL |
```

### 7. Final Check

- [ ] All validation checks PASS
- [ ] Statements challenging yet fair
- [ ] Rationales provide learning value
- [ ] References accessible (not paywalled when possible)
- [ ] True/False balance 45-55%
- [ ] No answer patterns
- [ ] Output follows format below exactly

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

**Rationale**: [1-2 sentences with `[Ref: ID]` citations]

---

## References

**Usage**: `[Ref: G3]` (Glossary), `[Ref: C1]` (Codebase), `[Ref: L2]` (Literature), `[Ref: A7]` (APA)

**Minimums**: G≥10 | C≥5 | L≥6 | APA≥12 (60% EN / 30% ZH / 10% other)

### Glossary, Terminology & Acronyms

**G1: Term**: Definition [Lang]  
**G2: Acronym** (Expansion): Definition [Lang]

### Codebase & Library References

**C1: Project/Library** ([lang])  
**Stack**: Components/SDKs  
**Maturity**: License, last commit ≤12mo, release ≥1.0.0, audit status  
**Benchmarks**: Performance, adoption  
**URL**: https://github.com/owner/repo

### Authoritative Literature & Reports

**L1: Title** (Year) ([lang])  
**Findings**: Main claims, standards, best practices  
**Methodology**: Sample size, scope  
**Impact**: Citations, adoption  
**URL**: DOI or archived link

### APA Style Source Citations

**English [EN]**  
Author, A. (Year). Title. *Journal*, vol(issue), pages. https://doi.org/... [EN]

**Chinese [ZH]**  
作者. (年份). 标题. *期刊*, 卷(期), 页码. [ZH]

**Other**  
[Follow APA 7th with language tags]
```


