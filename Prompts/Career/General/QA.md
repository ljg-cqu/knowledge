# Interview Q&A Generation Framework

## Purpose & Scope

Generate 25-30 discriminative technical interview Q&As for senior/architect/expert roles with evidence-based, multi-dimensional analysis.

**Scope**: User-specified technical domain | Senior-level assessment | Multi-source validation
**Constraints**: 25-30 Q&As | 150-300 words/answer | Multi-language sources
**Assumptions**: Specific domain provided | ≥20 credible sources exist | Target: 5+ years experience

## Key Definitions

- **≥** = min | **→** = implies | **✓/✗** = pass/fail
- **MECE**: Mutually Exclusive, Collectively Exhaustive
- **Cluster**: 4-6 related Q&As per technical area
- **Difficulty**: Foundational (0-3yr), Intermediate (3-7yr), Advanced (7+yr)
- **Roles**: Senior (5+yr, mentors), Architect (system design), Expert (thought leader)
- **Contentious**: ≥2 peer-reviewed sources with conflicting conclusions
- **Source Types**: (1) Official docs, (2) Standards/peer-reviewed, (3) Audits, (4) Vetted code
- **Time**: "Last 3yr" = current year - 3

## Core Requirements

**Target**: 25-30 Q&As | 150-300 words/answer | 20/40/40% difficulty split
**Citations**: ≥12 APA (~60% EN, ~30% ZH, ~10% other) | ≥70% answers cited
**References**: ≥10 glossary | ≥5 codebases | ≥6 literature
**Quality**: ≥50% <3yr (≥70% AI/security) | ≥3 types | Max 25% single source
**Per Cluster**: ≥1 diagram + ≥1 table | ≥2 authoritative + ≥1 codebase

## Content Principles

**Coverage (MECE)**: Mutually exclusive, collectively exhaustive across technical, theoretical, practical, contextual dimensions
**Depth**: Include assumptions, failure modes, trade-offs, alternatives, adoption signals
**Breadth**: Multiple perspectives: engineering, architecture, QA, product, ops, security, economics, policy
**Significance**: High-impact (>20% applicability); exclude edge cases (<5%), trivia, docs lookups
**Accuracy**: Cross-reference multiple authoritative sources
**Fairness**: Neutral framing; acknowledge context-dependency; ≥2 viewpoints for contentious topics; distinguish consensus from assumptions

## Execution Workflow

### 1. Topic Planning
- Identify 4-6 MECE clusters; allocate 4-6 Q&As each (total 25-30)
- Assign difficulty: 20% Foundational / 40% Intermediate / 40% Advanced
- Verify ≥20 credible sources exist; adjust scope if insufficient
**Checkpoint**: 25-30 total ✓ | 20/40/40 ratio ✓ | Sources sufficient ✓

### 2. Reference Collection
- Collect: ≥10 glossary, ≥5 codebases, ≥6 literature, ≥12 APA
- Tag: Language ([EN]/[ZH]/Other), year, type (1-4)
- Assign IDs: G1-Gn, C1-Cn, L1-Ln, A1-An
**Checkpoint**: Floors met ✓ | EN 50-70%, ZH 20-40%, Other 5-15% ✓ | ≥50% <3yr ✓ | ≥3 types, max 25% ✓

### 3. Q&A Generation
- Draft clear single-ask question; assign difficulty + type
- Write 150-300 words with depth, examples, trade-offs
- Cite: ≥1 `[Ref: ID]` after claims, metrics, trade-offs, recommendations
- State concrete Key Insight: misconception, failure path, or trade-off
- Frame neutrally; prioritize high-impact (>20%)
- Self-review every 5 Q&As: clarity, alignment, concreteness, word count, citations
**Checkpoint**: 150-300 words ✓ | ≥70% have ≥1 citation, ≥30% have ≥2 ✓ | Insights concrete ✓

### 4. Supporting Artifacts
- Create ≥1 diagram + ≥1 table per cluster
- Illustrate concepts, comparisons, workflows
**Checkpoint**: Each cluster has ≥1 diagram + ≥1 table ✓

### 5. Reference Compilation
- Populate all sections with complete fields
- Verify all `[Ref: ID]` resolve
- Use DOIs/archived URLs
**Checkpoint**: Complete ✓ | Resolve ✓ | Persistent links ✓

### 6. Validation

**Validation Tiers**:
- **Express** (Steps 1,2,6,7): <20 Q&As, time-constrained, drafts
- **Standard** (Steps 1,2,3,5,6,7,8): 20-30 Q&As (recommended)
- **Thorough** (All 11): Regulated domains, >30 Q&As, production

**11-Step Checklist**:
1. **Count Audit**: Floors + 20/40/40 ratio
2. **Citation Coverage**: ≥70% have ≥1, ≥30% have ≥2
3. **Language**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% <3yr (≥70% AI/security)
5. **Diversity**: ≥3 types, max 25%
6. **Links**: All accessible/archived
7. **Cross-refs**: All `[Ref: ID]` resolve
8. **Word Count**: Sample 5, verify 150-300
9. **Insights**: ≥90% concrete (not generic)
10. **Per-Topic**: Each ≥2 authoritative + ≥1 codebase
11. **Coherence**: Sample 3 aligned; contentious have ≥2 viewpoints

**Report Template**:
```
| Check | Result | Status |
| Floors | G:X C:Y L:Z A:W Q:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% <3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Words | 5/5 in range | PASS/FAIL |
| Insights | Y/X concrete | PASS/FAIL |
| Per-topic | X/Y meet | PASS/FAIL |
| Coherence | X/3 \| Y% fair | PASS/FAIL |
```
> **CRITICAL**: If ANY fails, halt, fix, regenerate, re-validate. Proceed only when ALL pass.

### 7. Final Review
- Review 8 Question Design Criteria
- Verify: Validation ✓ | Discriminative ✓ | Actionable ✓ | Verifiable ✓ | Production-ready ✓ | Significant ✓
- Sample 3 Q&As for coherence
- Verify fairness: balanced, no vendor bias
**Checklist**: 8/8 design ✓ | 6/6 success ✓ | 3/3 coherence ✓ | Fairness ✓ | Production ✓

## Question Design Criteria

| Criterion | Requirement |
|-----------|-------------|
| **Clarity** | Single unambiguous ask; no double-barreled wording |
| **Signal** | Tests reasoning/decisions, not trivia |
| **Significance** | High-impact concepts; avoids edge cases (<5%) |
| **Depth** | Enables failure mode, trade-off, constraint discussion |
| **Realism** | Senior/architect/expert scenarios |
| **Discriminative Power** | Distinguishes expertise from recall |
| **Alignment** | Matches seniority + tech context |
| **Neutrality** | Presents choices as trade-off decisions |

## Output Format

**Structure**: TOC with links | H2 for topics | H4 for questions | Diagrams, tables, code inline | References at end

**Q&A Template**:
```markdown
## Topic 1: [Title]

#### Q1: [Question text]
**Difficulty:** [Foundational/Intermediate/Advanced] | **Type:** [Theoretical/Practical/Scenario]

**Answer:**
(150-300 words: assumptions, trade-offs, failure modes, alternatives, examples, inline citations)

**Key Insight:** [Misconception | Failure Path | Trade-offs] - *Concrete statement*

**Supporting Artifacts:** [Diagram/table/code reference]
```

**Citations**: `[Ref: G3]` (Glossary), `[Ref: C1]` (Codebase), `[Ref: L2]` (Literature), `[Ref: A7]` (APA)

## Reference Section Formats

### Glossary, Terminology & Acronyms
`**G#: Term**: Definition [Lang]`
**Example**: `**G1: MECE**: Mutually Exclusive, Collectively Exhaustive [EN]`

### Codebase & Library References
`**C#: [Project]** ([lang])`
- **Stack**: Components
- **Maturity**: License, update, release
- **Benchmarks**: Performance, audits
- **Repo/Docs**: URLs

**Example**:
```markdown
**C1: Kubernetes** (Go)
- Stack: Orchestration, scheduler, API, etcd
- Maturity: Apache 2.0, v1.28 (2024-08), CNCF graduated
- Benchmarks: 5000+ nodes; CNCF audits
- Repo: https://github.com/kubernetes/kubernetes | Docs: https://kubernetes.io/docs/
```

### Authoritative Literature & Reports
`**L#: [Title]** (Year) ([lang])`
- **Findings**: Claims, practices
- **Method**: Sample, scope
- **Impact**: Citations, adoption
- **DOI/URL**: Link [archived]

**Example**:
```markdown
**L1: State of DevOps Report 2023** (2023) ([EN])
- Findings: High performers deploy 973× more, 6570× faster
- Method: 36K professionals, 9yr survey
- Impact: Industry benchmark; 500+ citations
- URL: https://dora.dev/research/2023/dora-report/
```

### APA Style Source Citations
Group by language (EN ≈60%, ZH ≈30%, Other ≈10%). APA 7th + tags.

**Examples**:
```
Smith, J., & Wang, L. (2024). Blockchain consensus: Comparative analysis.
    Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究. 计算机科学, 51(2), 88-95. [ZH]
```

## Scaling & Exceptions

**Scaling**:
- **Large** (>30 Q&As/regulated): 1.5× floors (round up)
- **Constrained** (limited time/sources): 0.8× minimum

**Priority**: Quality > floor counts. Reduce scope over compromising quality.

**Shortfalls** - Document:
- Root cause (sources, domain, novelty)
- Impact (criteria affected)
- Remediation/alternatives
- Risk mitigation

## Progress Reporting

**Template**: `Cluster 3/5 | 15/25 Q&As | 23 citations | Validation: Step 2 pending`

**Transparency**:
- State assumptions/constraints upfront
- Document shortfalls with alternatives
- Flag uncertainties: High/Medium/Low confidence
- Self-review: Distinguishes senior expertise? Verifiable? Trade-offs stated?
