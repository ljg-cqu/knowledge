# Multiple-Choice Questions Generator

Generate senior/architect/expert-level MCQ assessments: 40-80 questions with stems, options, rationales, misconception-mapped distractors, and authoritative citations.

---

## I. Configuration

**Scope**: Domain-agnostic template for ethical use; cite authoritative sources.

**Inputs Required**: Subject/topic, audience level, must-include sources, language/difficulty preferences.

**Output**: MCQ bank (JSONL + optional Markdown) + validation report.

**Parameters** (defaults):
```yaml
question_count: 60
difficulty_mix: { foundational: 20%, intermediate: 40%, advanced: 40% }
language_distribution: { en: 60%, zh: 30%, other: 10% }
recency_threshold: 36 months
citation_style: APA7
```

**Terminology**: Stem (question text), options (4 choices), key (correct answer), distractors (wrong options), rationale (1-2 sentence explanation with citations), misconception (error pattern mapped to distractor).

**Scaling**: For >80 questions or regulated domains, multiply reference minimums by 1.5×.

---

## II. Requirements

### Question Structure
- **Format**: 1-2 sentence stem + 4 options (exactly one correct)
- **Difficulty**: Per config mix (20/40/40)
- **Topics**: 4-8 clusters organized using MECE (Mutually Exclusive, Collectively Exhaustive); state assumptions
- **Distractors**: Each maps to specific misconception or outdated practice
- **Rationale**: 1-2 sentences with ≥1 `[Ref: ID]` citation
- **Grading**: Machine-gradable; no partial credit
- **Quality per question**: Significance (why it matters), risk/mitigation, fairness (assumptions/bias/counterpoints)

### References (Minimums)
| Type | Count | Purpose | Requirements |
|------|-------|---------|--------------|
| **Glossary** | ≥10 | Define terms, acronyms | Clear definitions with language tags |
| **Codebase/Libraries** | ≥5 | Tools, SDKs, frameworks | License, update ≤12mo, stable release, audit status |
| **Literature/Reports** | ≥6 | Standards, peer-reviewed, audits | Persistent links (DOI/archived), findings, methodology |
| **APA Citations** | ≥12 | All sources | EN 50-70% / ZH 20-40% / Other 5-15% |

### Citation Standards
- **Format**: APA 7th + language tags ([EN], [ZH], etc.)
- **IDs**: G# (Glossary), C# (Codebase), L# (Literature), A# (APA)
- **Inline Usage**: `[Ref: ID]` in rationales
- **Source Hierarchy**: (1) Official docs (specs, RFCs) → (2) Standards/peer-reviewed (ISO, IEEE, journals) → (3) Security audits/reports → (4) Vetted codebases (stable repos)
- **Confidence**: Include score [0-1] for contested claims

### Quality Gates
1. **Recency**: ≥50% sources from last 36mo (≥70% for AI/security)
2. **Source Diversity**: ≥3 types; no single type >25%
3. **Citation Coverage**: ≥70% questions have ≥1 citation; ≥30% have ≥2
4. **Codebase Maturity**: License + update ≤12mo + stable + audit status documented
5. **Link Validation**: 100% URLs accessible or archived (DOI preferred)
6. **Cross-Reference Integrity**: Every `[Ref: ID]` maps to exactly one entry; no orphans
7. **Deduplication**: Merge duplicates; use canonical URLs

---

## III. Execution Steps

### 1. Planning
- **Identify** 4-8 MECE topic clusters
- **Allocate** 5-10 questions per cluster (total per config)
- **Assign** difficulty per 20/40/40 ratio; balance within clusters
- **Self-check**: Total count, MECE compliance, difficulty ratio

### 2. References
- **Gather** references meeting minimums (G≥10, C≥5, L≥6, A≥12)
- **Tag** with language ([EN], [ZH], etc.), year, source type (1-4)
- **Assign** unique IDs (G1-Gn, C1-Cn, L1-Ln, A1-An)
- **Validate** URLs (HTTP 200 or archived)
- **Self-check**: Counts, language distribution (60/30/10), recency (≥50% last 36mo), diversity (≥3 types, max 25%)

### 3. Questions (for each)
- **Write**: Stem (1-2 sentences) + 4 options (one correct)
- **Add**: Difficulty tag, language tag, significance/risk/fairness notes
- **Rationale**: ≥1 `[Ref: ID]` (prefer standards/peer-reviewed)
- **Distractors**: Map each to specific misconception
- **Self-check** (every 10): One correct? Quality distractors? ≥1 citation? Fairness notes? Clear options?

### 4. Distractor Documentation (for each)
- **Document**: Why incorrect + which misconception
- **Note**: Common mistake patterns + risk/mitigation
- **Self-check**: All distractors mapped and explained

### 5. Compile References
- **Populate**: Glossary, Codebase, Literature, APA sections
- **Include**: All required fields (see Output Format)
- **Match**: All `[Ref: ID]` to entries
- **Self-check**: All IDs resolve? Fields complete? Persistent links? Language tags present?

### 6. Validate
- **Execute** 12 validation checks (see Validation Protocol)
- **Generate** report (see template)
- **Fix** failures; **re-validate** until ALL PASS (2-3 cycles expected)
- **Attach** final ALL PASS report

### 7. Submit
- **Review**: Coherence, clarity, no tangents
- **Verify**: All checklist items complete
- **Submit** only when: Validation ALL PASS + format correct + schema-valid

---

## IV. Output Format

### JSONL Schema (Primary)
```json
{"id":"Q001","language":"en","topic":"...","difficulty":"intermediate","stem":"...","options":["A","B","C","D"],"key":"B","rationale":"... [Ref: L3]","misconceptions":["distractor A maps to...","distractor C maps to...","distractor D maps to..."],"significance":"...","risk":"...","fairness":"...","evidence":[{"title":"...","url":"...","accessed":"2025-10-20","citation":"[EN]"}],"confidence":0.95}
```

**Constraints**: `language` in {en, zh, other}; `difficulty` in {foundational, intermediate, advanced}; `key` in {A,B,C,D}; `confidence` in [0,1].

### Markdown (Optional)
```markdown
### Topic 1: [Topic Name]

#### Q1: [Stem text]
**Difficulty**: [F/I/A] | **Language**: [EN/ZH/Other]

- A. [Option]
- B. [Option]
- C. [Option]
- D. [Option]

**Answer**: [A/B/C/D]
**Rationale**: [1-2 sentences with [Ref: ID]]
**Significance**: [Why it matters]
**Risk/Mitigation**: [Failure modes and mitigations]
**Fairness**: [Assumptions, biases, counterpoints]
**Distractors**:
- A: [Why wrong | Misconception: ...]
- C: [Why wrong | Misconception: ...]
- D: [Why wrong | Misconception: ...]
```

### References

**Usage**: `[Ref: ID]` in rationales → G# (Glossary), C# (Codebase), L# (Literature), A# (APA)

**Example**: "Answer B is correct because consensus algorithms require Byzantine fault tolerance [Ref: G2] per protocol design [Ref: L5]."

#### Glossary
**Format**: `**G#: Term**: Definition [Lang]`

**Example**: `**G1: MECE**: Mutually Exclusive, Collectively Exhaustive - categories don't overlap and cover all possibilities [EN]`

#### Codebase & Libraries
**Format**: `**C#: Library** ([Lang])`

**Required**: Repo URL, license, last update (≤12mo), stable release, audit status, docs

**Example**:
```
**C1: React** ([EN])
- Repo: https://github.com/facebook/react
- License: MIT | Updated: 2024-10 | Stable: 18.3.0 | Audit: Third-party reviewed 2024
- Docs: https://react.dev
```

#### Literature & Reports
**Format**: `**L#: Title** (Year) ([Lang])`

**Required**: APA citation, persistent link (DOI/archived), key findings, methodology, impact

**Example**:
```
**L1: IEEE Std 830-1998** (1998) ([EN])
- Citation: IEEE. (1998). IEEE Recommended Practice for Software Requirements Specifications. https://doi.org/10.1109/IEEESTD.1998.88286
- Findings: Defines SRS characteristics; emphasis on verifiability
- Methodology: Industry consensus working group
- Impact: >1000 citations, widely adopted standard
```

#### APA Citations
**Format**: APA 7th, grouped by language (EN / ZH / Other), alphabetized within groups

**Example**:
```
**English [EN]**
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms. Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

**Chinese [ZH]**
张伟, & 李娜. (2024). 区块链技术应用研究. 计算机科学, 51(2), 88-95. [ZH]
```

---

## V. Validation Protocol

**Mandatory**: Generate validation report before submission. ALL 12 checks must PASS. Re-validate after fixes until clean pass.

| Check | Pass Criteria | Report Format |
|-------|---------------|---------------|
| **1. Counts** | G≥10, C≥5, L≥6, A≥12, Q=40-80, Ratio 20/40/40 (±5%) | `G:X C:Y L:Z A:W Q:N (F/I/A: P%/Q%/R%)` |
| **2. Citations** | ≥70% questions ≥1 cite; ≥30% ≥2 cites | `X/Y ≥1 (Z%); W/Y ≥2 (V%)` |
| **3. Languages** | EN 50-70%, ZH 20-40%, Other 5-15% | `EN:X (Y%) ZH:A (B%) Other:C (D%)` |
| **4. Recency** | ≥50% last 36mo (≥70% AI/security) | `X/Y (Z%) last 36mo` |
| **5. Diversity** | ≥3 types; max 25% single | `Types=N; Max=P%` |
| **6. Links** | 100% accessible or archived | `Y/X accessible (list broken)` |
| **7. Cross-refs** | All `[Ref: ID]` resolve; no orphans | `Y/X resolved (list broken)` |
| **8. Correctness** | Exactly one correct per question | `Y/X exactly one (list issues)` |
| **9. Distractors** | All quality (mapped to misconceptions) | `Y/X quality (list weak)` |
| **10. Options** | All unambiguous | `Y/X clear (list vague)` |
| **11. Conflicts** | ≥80% comply with documented perspectives | `X applicable; Y comply (Z%)` |
| **12. Quality** | Significance/Risk/Fairness/Reasoning ≥90% each | `S:X/Y R:W/Y F:V/Y Logic:U/Y` |

**Report Template**:
```
Config: {question_count, difficulty_mix, language_distribution}

Validation Results:
1. Counts: [result] | PASS/FAIL
2. Citations: [result] | PASS/FAIL
3. Languages: [result] | PASS/FAIL
4. Recency: [result] | PASS/FAIL
5. Diversity: [result] | PASS/FAIL
6. Links: [result] | PASS/FAIL
7. Cross-refs: [result] | PASS/FAIL
8. Correctness: [result] | PASS/FAIL
9. Distractors: [result] | PASS/FAIL
10. Options: [result] | PASS/FAIL
11. Conflicts: [result] | PASS/FAIL
12. Quality: [result] | PASS/FAIL

Overall Status: PASS/FAIL
Failed Checks: [List or "None"]
Remediation: [Plan or "Ready for submission"]
```

**Success Criteria**: All minimums satisfied + distributions within ranges + no ambiguous/overlapping options + schema-valid JSONL + all links/cross-refs resolve + validation ALL PASS.
