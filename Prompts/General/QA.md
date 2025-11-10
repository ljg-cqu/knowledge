# Interview Q&A Generation Framework

Generates structured, evidence-based interview question banks with multi-dimensional evaluation for senior/architect/expert roles.

---

# Part I: Specifications

## Specifications

### Scope and Structure

- **Target**: 25–30 Q&As (senior/architect/expert level)
- **Answer Length**: 150–300 words (misconceptions, failure paths, trade-offs, decision criteria)
- **Difficulty**: 20% Foundational, 40% Intermediate, 40% Advanced
- **Artifacts**: ≥1 diagram + ≥1 table per topic cluster

### Content Principles

- **MECE Coverage**: Technical, theoretical, practical, contextual dimensions
- **Analysis Depth**: Assumptions, failure paths, comparisons, trade-offs, adoption signals
- **Perspectives**: Engineering, architecture, QA, product, operations, security, economics, policy
- **Debate Handling**: Present competing viewpoints with counter-evidence; distinguish consensus from assumption-dependent conclusions

### Evaluation Dimensions

| Dimension | Elements |
|-----------|----------|
| Technical | Performance, security, scalability, reliability |
| Business | Cost, efficiency, impact, market fit |
| Strategic | Regulatory landscape, adoption barriers, competitive dynamics |
| Actionable | Best practices, mitigations, open questions |

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other ([EN], [ZH] tags)
- **Source Types**: (1) Official docs; (2) Standards/peer-reviewed; (3) Audits/reports; (4) Vetted code
- **Format**: APA 7th with language tags
- **Inline Citation**: `[Ref: ID]` after factual claims, metrics, comparisons, trade-offs, best practices, security/compliance statements, recommendations

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, domain-specific jargon, localized terminology |
| Codebase & Library References | ≥5 entries | Primary stack components, SDKs, supporting tooling |
| Authoritative Literature & Reports | ≥6 entries | Standards, peer-reviewed work, regulatory/industry analyses |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception**: If floor counts unmet, document shortfall + rationale + sourcing plan.

### Usage Guidelines

1. Apply MECE principles; maintain 20/40/40 difficulty distribution
2. Meet floor counts: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 citations
3. Language mix: ~60% EN, ~30% ZH, ~10% other with tags
4. Uniform formatting across reference sections
5. Per topic cluster: ≥1 diagram + ≥1 table, ≥2 authoritative sources + ≥1 codebase reference
6. Address engineering, business, strategic, operational perspectives
7. Document shortfalls with rationale + remediation plan

### Quality Gates

| Gate | Requirement |
|------|-------------|
| Recency | ≥50% from last 3yr (≥70% for AI/security from last 2yr) |
| Source diversity | ≥3 types; no single source >25% |
| Evidence coverage | ≥70% answers with ≥1 citation; ≥30% with ≥2 distinct citations |
| Codebase maturity | License, last commit ≤12mo, stable release, audit status |
| Deduplication | Canonicalize entries; prefer DOIs/archived URLs |
| Link validity | All links resolve or archived |
| Cross-reference binding | All `[Ref: ID]` resolve to Reference Sections |

> **Scaling**: For >30 Q&As or regulated domains, increase floors by 1.5× (round up). Prioritize Quality Gates over higher floors.

### Pre-Submission Validation

Execute all steps; fix failures and re-validate until all pass.

**Step 1 – Count Audit**
- Count: Glossary, Codebase, Literature, APA citations, Q&As (total + by difficulty)
- Report: `Glossary: X (≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Q&As: N (F/I/A)`
- Pass: All minimums met AND difficulty ratio ≈20/40/40

**Step 2 – Citation Coverage Scan**
- Count inline `[Ref: ...]` per answer
- Report: `X of Y with ≥1 citation (Z%); W of Y with ≥2 (V%)`
- Pass: ≥70% have ≥1; ≥30% have ≥2

**Step 3 – Language Distribution Check**
- Count language tags
- Report: `EN: X (Y%) | ZH: A (B%) | Other: C (D%)`
- Pass: EN 50-70%, ZH 20-40%, Other 5-15%

**Step 4 – Recency Verification**
- Extract publication year per citation
- Report: `X of Y (Z%) from last 3yr`
- Pass: ≥50% from last 3yr (≥70% for AI/security)

**Step 5 – Source Type Diversity**
- Classify citations: (1) Official, (2) Standards/peer-reviewed, (3) Audits, (4) Code
- Report: `Type 1: X | Type 2: Y | Type 3: Z | Type 4: W | Types: N | Max source: M (P%)`
- Pass: ≥3 types AND max ≤25%

**Step 6 – Link Validation**
- Test URLs or verify archived links
- Report: `Tested X: Y accessible, Z broken` (list broken)
- Pass: All accessible OR archived alternatives provided

**Step 7 – Cross-Reference Integrity**
- Verify each `[Ref: ID]` exists (G#→Glossary, C#→Codebase, L#→Literature, A#→APA)
- Report: `X inline refs: Y resolve, Z broken` (list broken)
- Pass: All resolve (Z=0)

**Step 8 – Word Count Compliance**
- Sample 5 answers; count words (exclude metadata)
- Report: `Q#: X words | Q#: Y words | ...` (flag <150 or >300)
- Pass: All sampled in 150–300 range

**Step 9 – Key Insight Concreteness**
- Review Key Insight per answer
- Report: `X of Y concrete; Z generic/missing` (list generic)
- Pass: All state specific misconception/failure/trade-off (Z=0)

**Step 10 – Per-Topic Minimums**
- List linked sources per topic (L#/A# authoritative, C# codebase)
- Report: `Topic 1: [L1, A3, C2] → 2 auth + 1 code ✓ | Topic 2: [A5] → 1 auth + 0 code ✗`
- Pass: Every topic has ≥2 authoritative + ≥1 codebase

**Step 11 – Conflict Handling Compliance**
- Identify contentious topics
- Verify ≥2 competing perspectives cited with counter-evidence
- Report: `X applicable Q&As; Y comply (Z%)`
- Pass: ≥80% comply OR rationale provided

**Validation Report Template:**
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
```

> **MANDATORY:** If ANY check fails, stop, fix, regenerate, re-validate. Proceed only when ALL pass.

### Submission Checklist

- [ ] Floors met: Glossary ≥10, Codebase ≥5, Literature ≥6, APA ≥12
- [ ] Difficulty: 20/40/40 (Foundational/Intermediate/Advanced)
- [ ] Language: ~60% EN, ~30% ZH, ~10% other
- [ ] Recency: ≥50% last 3yr (≥70% for AI/security)
- [ ] Diversity: ≥3 source types, max 25%
- [ ] Evidence: ≥70% with ≥1 citation; ≥30% with ≥2
- [ ] Answer quality: 150–300 words, ≥1 `[Ref: ...]`, concrete Key Insight
- [ ] Codebase maturity: license, update ≤12mo, stable release, audit status
- [ ] Links: resolve or archived
- [ ] Cross-references: IDs in answers match Reference Sections
- [ ] Per-topic: ≥2 authoritative + ≥1 codebase per cluster
- [ ] Validation: all checks pass

---

# Part II: Instructions

Follow steps sequentially; execute inline quality checks before proceeding.

### Step 1: Topic Identification & Planning
1. Identify 4-6 topic clusters
2. Allocate 4-6 Q&As per cluster (total 25-30)
3. Assign difficulty for 20/40/40 balance
4. **Check**: Total = 25-30 AND ratio ≈20/40/40

### Step 2: Reference Collection
1. Gather ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA citations
2. Tag language, note year, classify type (1-4)
3. Assign IDs: G1-Gn, C1-Cn, L1-Ln, A1-An
4. **Check**: Counts ≥10/5/6/12, language ≈60/30/10, recency ≥50% last 3yr, diversity ≥3 types

### Step 3: Question & Answer Generation
1. Per Q&A: Write question, assign difficulty + type, draft 150-300 word answer
2. Per answer: Include ≥1 `[Ref: ID]` after factual claims, metrics, trade-offs, recommendations
3. Per answer: State concrete Key Insight (misconception/failure/trade-off)
4. **Check** (every 5 Q&As): Word count 150-300, ≥1 citation, concrete Key Insight

### Step 4: Supporting Artifacts
1. Create ≥1 diagram + ≥1 table per cluster
2. Ensure artifacts support Q&A content
3. **Check**: ≥1 diagram + ≥1 table per cluster

### Step 5: Reference Section Compilation
1. Populate Glossary, Codebase, Literature, APA sections
2. Include all required fields per format
3. Match Reference IDs to inline citations
4. **Check**: All `[Ref: ID]` resolve; all sources have required fields

### Step 6: Pre-Submission Validation
Execute all 11 validation steps (Part I). Present validation report. Fix failures and re-validate.

### Step 7: Final Review
Apply Question Design & Critique criteria. Check Submission Checklist. Submit only when all checks pass.

---

# Part III: Output Format

## Question Design & Critique

Review each question before finalizing:

| Criterion | Requirement |
|-----------|-------------|
| Clarity | Single unambiguous ask; no double-barreled wording |
| Signal | Tests reasoning/decision criteria, not trivia |
| Depth | Enables discussion of failure modes, trade-offs, constraints |
| Realism | Anchored in senior/architect/expert scenarios |
| Discriminative power | Distinguishes shallow recall from practical expertise |
| Alignment | Matches stated seniority and tech stack/context |

---

## Output Format

Use this structure when generating question banks:

```markdown
## Contents

- [Topic Areas](#topic-areas-questions-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Q1: [Question text]](#q1-question-text)
  - [Q2: [Question text]](#q2-question-text)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Q3: [Question text]](#q3-question-text)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Topic Areas (Questions 1–N)

### Topic 1: [Topic title]

#### Q1: [Question text]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Type:** [Theoretical/Practical/Scenario]

**Answer:** (150-300 words with technical depth, examples, trade-offs)

**Key Insight:** [Choose one: Misconception | Failure Path | Trade-offs] - *Briefly state the core insight.*

**Supporting Artifacts:** [Mermaid Diagram/table/code/formula]

---

## Reference Sections

Use Reference IDs to tie claims to sources: `[Ref: G3]` (Glossary), `[Ref: C1]` (Codebase), `[Ref: L2]` (Literature), `[Ref: A7]` (APA).

**Example**: "Byzantine fault tolerance [Ref: G2] requires >2/3 honest nodes in PBFT [Ref: C1], as demonstrated in production [Ref: L4, A8]."

### Glossary, Terminology & Acronyms

**Format**: `**G#: Term/Acronym**: Definition [Language Tag]`

**Example**: `**G1: MECE** (Mutually Exclusive, Collectively Exhaustive): Framework ensuring categories don't overlap and cover all possibilities [EN]`

### Codebase & Library References

**Format**: `**C#: [Project/Library Name]** ([lang])`

**Required**:
- Stack/Modules: Core SDK/components
- Maturity: License, last update ≤12mo, stable release
- Benchmarks: Performance, audit status, adoption

**Optional**: Integration hooks, HA indicators, consistency guarantees, language support, vulnerability disclosures

**Template**: Repository URL (GitHub: owner/repo | License: Type), documentation URL, maturity details.

### Authoritative Literature & Reports

**Format**: `**L#: [Title]** (Year) ([lang])`

**Required**:
- Core Findings: Claims, best practices, standards
- Methodology: Sample size, temporal scope
- Impact: Citations, industry adoption

**Optional**: Limitations, replication status, follow-up studies, jurisdiction applicability

**Template**: APA citation with language tag, persistent link (DOI/archived URL).

### APA Style Source Citations

Group by language (~60% EN, ~30% ZH, ~10% other). Follow APA 7th with language tags.

**Example**:
```text
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms: A comparative analysis.
    Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究.
    计算机科学, 51(2), 88-95. [ZH]

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system.
    https://bitcoin.org/bitcoin.pdf [EN]
```
```


