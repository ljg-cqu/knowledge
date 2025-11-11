# Interview Q&A Generation Framework

Generate discriminative technical interview Q&As (25-30) for senior/architect/expert roles with evidence-based answers, multi-dimensional analysis, and comprehensive validation.

## Core Requirements

**Target**: 25-30 Q&As | 150-300 words/answer | 20% Foundational / 40% Intermediate / 40% Advanced
**Citations**: ≥12 APA sources (~60% EN, ~30% ZH, ~10% other) | ≥70% answers cited
**References**: ≥10 glossary | ≥5 codebases | ≥6 literature reports
**Quality**: ≥50% sources <3yr old (≥70% for AI/security) | ≥3 source types | No single source >25%
**Per Cluster**: ≥1 diagram + ≥1 table | ≥2 authoritative sources + ≥1 codebase

## Key Definitions

- **≥** = minimum threshold | **→** = implies | **✓/✗** = pass/fail
- **MECE**: Mutually Exclusive, Collectively Exhaustive coverage
- **Topic Cluster**: 4-6 related Q&As covering one technical area
- **Difficulty Tiers**: Foundational (0-3yr), Intermediate (3-7yr), Advanced (7+yr)
- **Role Levels**: Senior (5+yr, mentors), Architect (system design, standards), Expert (thought leader)
- **Contentious Topic**: ≥2 peer-reviewed sources with conflicting conclusions
- **Source Types**: (1) Official docs, (2) Standards/peer-reviewed, (3) Audits/reports, (4) Vetted code
- **Time Windows**: "Last 3yr" = current year minus 3 (e.g., 2022-2025 if 2025)

## Content Principles

**Coverage (MECE)**: Technical, theoretical, practical, contextual; no gaps/overlaps
**Analysis Depth**: Assumptions, failure modes, trade-offs, alternatives, adoption signals
**Perspectives**: Engineering, architecture, QA, product, ops, security, economics, policy
**Fairness**: Neutral framing; acknowledge context-dependency (org size, region, budget); present ≥2 competing viewpoints for contentious topics; distinguish consensus from assumption-dependent conclusions
**Significance**: High-impact concepts (>20% practitioners); omit edge cases (<5%), trivia, simple docs lookups

## Execution Workflow

### 1. Topic Planning
- Identify 4-6 MECE topic clusters from user domain
- Allocate 4-6 Q&As per cluster (total 25-30)
- Assign difficulty: 20% Foundational / 40% Intermediate / 40% Advanced
- **Feasibility**: Verify ≥20 credible sources exist; adjust scope if needed
- **Checkpoint**: Total 25-30 ✓ | Difficulty 20/40/40 ✓ | Literature sufficient ✓

### 2. Reference Collection
- Collect: ≥10 glossary, ≥5 codebases, ≥6 literature, ≥12 APA citations
- Tag language ([EN]/[ZH]/Other), year, source type (1-4)
- Assign IDs: G1-Gn (Glossary), C1-Cn (Codebase), L1-Ln (Literature), A1-An (APA)
- **Checkpoint**: Floor counts met ✓ | Language mix EN 50-70%, ZH 20-40%, Other 5-15% ✓ | ≥50% <3yr old ✓ | ≥3 source types, max ≤25% ✓

### 3. Q&A Generation
- Draft question, assign difficulty + type (Theoretical/Practical/Scenario), write 150-300 word answer
- Include ≥1 `[Ref: ID]` after factual claims, metrics, trade-offs, recommendations
- State concrete Key Insight: misconception / failure path / trade-off
- Frame neutrally; prioritize high-impact concepts (>20% applicability)
- **Self-Review (every 5 Q&As)**: Clarity | Alignment | Concreteness | Word count 150-300 | ≥1 citation
- **Checkpoint**: 150-300 words ✓ | ≥70% with ≥1 citation, ≥30% with ≥2 ✓ | Insights concrete ✓

### 4. Supporting Artifacts
- Create ≥1 Mermaid diagram + ≥1 table per cluster
- Illustrate key concepts, comparisons, workflows
- **Checkpoint**: Each cluster has ≥1 diagram + ≥1 table ✓

### 5. Reference Compilation
- Populate Glossary, Codebase, Literature, APA sections with required fields
- Ensure all `[Ref: ID]` resolve to Reference Sections
- Use DOIs/archived URLs where available
- **Checkpoint**: Sections complete ✓ | Citations resolve ✓ | DOIs/archived URLs used ✓

### 6. Validation
**Select Tier**:
- **Express** (Steps 1,2,6,7): <20 Q&As, time-constrained, drafts
- **Standard** (Steps 1,2,3,5,6,7,8): 20-30 Q&As (recommended)
- **Thorough** (All 11): Regulated domains, >30 Q&As, production

**11-Step Validation**:
1. **Count Audit**: Meet floors + difficulty ratio 20/40/40
2. **Citation Coverage**: ≥70% with ≥1, ≥30% with ≥2
3. **Language Distribution**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% <3yr (≥70% AI/security)
5. **Source Diversity**: ≥3 types, max ≤25%
6. **Link Validation**: All accessible or archived
7. **Cross-Reference Integrity**: All `[Ref: ID]` resolve
8. **Word Count**: Sample 5 answers in 150-300 range
9. **Key Insight Concreteness**: ≥90% specific (not generic)
10. **Per-Topic Minimums**: Each cluster ≥2 authoritative + ≥1 codebase
11. **Semantic Coherence**: Sample 3 Q&As aligned; contentious topics have ≥2 viewpoints

**Validation Report**:
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X C:Y L:Z A:W Q:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language dist | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Word counts | 5/5 compliant | PASS/FAIL |
| Key Insights | Y/X concrete | PASS/FAIL |
| Per-topic mins | X/Y topics meet | PASS/FAIL |
| Coherence & Fairness | Coherence: X/3 | Fairness: Y% | PASS/FAIL |
```
> **MANDATORY**: If ANY check fails, stop, fix, regenerate, re-validate. Proceed only when ALL pass.

### 7. Final Review
- Review Question Design Criteria (8 criteria below)
- Verify Success Criteria: Validation passed | Discriminative | Actionable | Verifiable | Production-ready | Significant
- Semantic coherence: Sample 3 Q&As align
- Fairness: Balanced, no vendor bias
- **Final Checklist**: 8/8 design criteria ✓ | 6/6 success criteria ✓ | 3/3 coherence ✓ | Fairness ✓ | Production-ready ✓

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

**Structure**: TOC with links | H2 for topics | H4 for questions | Mermaid diagrams, tables, code blocks | Reference Sections at end

**Q&A Template**:
```markdown
## Topic 1: [Title]

#### Q1: [Question text]
**Difficulty:** [Foundational/Intermediate/Advanced] | **Type:** [Theoretical/Practical/Scenario]
**Answer:** (150-300 words with depth, examples, trade-offs)
**Key Insight:** [Misconception | Failure Path | Trade-offs] - *Core insight*
**Supporting Artifacts:** [Diagram/table/code]
```

**Citation Format**: Inline `[Ref: G3]` (Glossary), `[Ref: C1]` (Codebase), `[Ref: L2]` (Literature), `[Ref: A7]` (APA)

## Reference Section Formats

### Glossary, Terminology & Acronyms
`**G#: Term**: Definition [Language Tag]`

**Example**: `**G1: MECE**: Mutually Exclusive, Collectively Exhaustive [EN]`

### Codebase & Library References
`**C#: [Project]** ([lang])`
- **Stack/Modules**: Core components
- **Maturity**: License, last update ≤12mo, stable release
- **Benchmarks**: Performance, audits, adoption
- **Repository**: URL | **Docs**: URL

**Example**:
```markdown
**C1: Kubernetes** (Go)
- Stack: Orchestration, scheduler, API server, etcd
- Maturity: Apache 2.0, v1.28 (2024-08), CNCF graduated
- Benchmarks: 5000+ nodes tested; CNCF audits
- Repository: https://github.com/kubernetes/kubernetes
- Docs: https://kubernetes.io/docs/
```

### Authoritative Literature & Reports
`**L#: [Title]** (Year) ([lang])`
- **Core Findings**: Claims, practices, standards
- **Methodology**: Sample size, scope
- **Impact**: Citations, adoption
- **DOI/URL**: Link [archived: URL]

**Example**:
```markdown
**L1: State of DevOps Report 2023** (2023) ([EN])
- Core Findings: High performers deploy 973× more, 6570× faster
- Methodology: 36K professionals, 9yr global survey
- Impact: Industry benchmark; 500+ citations
- DOI/URL: https://dora.dev/research/2023/dora-report/
```

### APA Style Source Citations
Group by language (EN ≈ 60%, ZH ≈ 30%, Other ≈ 10%). APA 7th edition + language tags.

**Examples**:
```
Smith, J., & Wang, L. (2024). Blockchain consensus: Comparative analysis.
    Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究.
    计算机科学, 51(2), 88-95. [ZH]
```

## Scaling & Exceptions

**Scaling**: >30 Q&As or regulated domains → 1.5× floor counts (round up) | Resource-constrained → 0.8× minimum
**Priority Rule**: Quality Gates > floor counts
**Shortfalls**: Document reasoning (insufficient sources, monolingual domain, nascent topic) + remediation plan

## Progress Reporting

After each cluster: `Cluster 3/5 complete | 15/25 Q&As | 23 citations | Validation: Step 2 pending`

**Reasoning Transparency**: State assumptions/constraints | Document inability to meet requirements with alternative approaches | Flag uncertainties with confidence (High/Medium/Low) | Self-review: Distinguishes senior from junior? Claims verifiable? Trade-offs stated?
