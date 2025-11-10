# Case Study / Scenario

Generate case study/scenario assessments with structured citations and multi-dimensional evaluation.

---

# Part I: Specifications

## Scope and Structure

- **Scenarios**: 16–22 (senior/architect/expert level)
- **Difficulty**: 20% Foundational / 40% Intermediate / 40% Advanced
- **Context**: 200–400 words (constraints, stakeholders, technical details)
- **Tasks**: 3–4 MECE tasks per scenario
- **Deliverables**: Issue lists, memos (≤300 words), matrices, communications
- **Trade-offs**: Privacy vs transparency, throughput vs consistency, cost vs resilience
- **Grading**: Partial-credit rubrics; document evidence, omissions, alternatives
- **Conflict Handling**: Acknowledge competing approaches; clarify consensus vs dissent

## Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH])
- **Source Types**: 
  1. Official docs (specs, vendor docs, RFCs)
  2. Standards/peer-reviewed (ISO, IEEE, journals, conferences)
  3. Audits/reports (security, industry, regulatory)
  4. Vetted code (production repos, stable releases)
- **Format**: APA 7th with language tags
- **Inline Citation**: `[Ref: ID]` for factual claims, metrics, comparisons, trade-offs, best practices

## Reference Minimums

| Section | Count | Content |
| --- | --- | --- |
| Glossary | ≥10 | Core concepts, domain jargon, localized terms |
| Codebase & Libraries | ≥5 | Stack components, SDKs, tooling |
| Literature & Reports | ≥6 | Standards, peer-reviewed, regulatory/industry |
| APA Citations | ≥12 | ~60% EN, ~30% ZH, ~10% other |

> If unable to meet minimums: state shortfall, rationale, and sourcing plan.

## Quality Gates

- **Recency**: ≥50% from last 3 years (≥70% for AI/security)
- **Diversity**: ≥3 source types; no single source >25%
- **Evidence**: ≥70% scenarios with ≥1 citation; ≥30% with ≥2 citations
- **Maturity**: License, last commit ≤12 months, stable release, audit status
- **Deduplication**: Canonicalize entries; use persistent links (DOIs, archived URLs)
- **Links**: All URLs resolve or archived alternatives provided
- **Cross-refs**: Reference IDs link scenarios to Reference Sections

> For >25 scenarios or regulated domains: increase minimums by 1.5× (round up). Prioritize Quality Gates over unlimited growth.

## Pre-Submission Validation

Execute all steps. Fix failures and re-validate until all pass.

| Step | Check | Pass Criteria |
| --- | --- | --- |
| 1 | Count Audit | All minimums met; difficulty ratio ≈20/40/40 |
| 2 | Citation Coverage | ≥70% scenarios with ≥1 citation; ≥30% with ≥2 |
| 3 | Language Distribution | EN ≈50-70%, ZH ≈20-40%, Other ≈5-15% |
| 4 | Recency | ≥50% from last 3 years (≥70% for AI/security) |
| 5 | Source Diversity | ≥3 types; no single source >25% |
| 6 | Link Validation | All URLs accessible or archived |
| 7 | Cross-Reference | All `[Ref: ID]` resolve to Reference Sections |
| 8 | Context Length | All contexts 200–400 words |
| 9 | MECE Tasks | All scenarios have mutually exclusive, exhaustive tasks |
| 10 | Grading Rubrics | All tasks have complete rubrics with points |
| 11 | Conflict Handling | ≥80% acknowledge alternatives; clarify consensus vs dissent |

**Report Format:**
```
| Check | Result | Status |
|-------|--------|--------|
| Minimums | G:X C:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Languages | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Lengths | Y/X in 200-400 | PASS/FAIL |
| MECE | Y/X verified | PASS/FAIL |
| Rubrics | Y/X complete | PASS/FAIL |
| Conflicts | Y/X comply | PASS/FAIL |
```

> If any check fails: stop, fix, regenerate, re-validate. Submit only when all pass.

## Submission Checklist

- [ ] Minimums: G≥10, C≥5, L≥6, APA≥12
- [ ] Difficulty: 20/40/40 (F/I/A)
- [ ] Languages: ~60% EN, ~30% ZH, ~10% other
- [ ] Recency: ≥50% last 3yr (≥70% AI/security)
- [ ] Diversity: ≥3 types, max 25% single source
- [ ] Coverage: ≥70% with ≥1 cite; ≥30% with ≥2
- [ ] Contexts: 200–400 words with citations
- [ ] Maturity: License, update ≤12mo, release, audit
- [ ] Links: All resolve or archived
- [ ] Cross-refs: IDs in scenarios match Reference Sections
- [ ] MECE: All tasks verified
- [ ] Rubrics: Complete with points
- [ ] Validation: All checks pass

---

# Part II: Instructions

Execute steps in order with inline checks before proceeding.

## Steps

### 1. Topic Planning
1. Identify 3-5 domain clusters (e.g., DeFi, Infrastructure, RWA)
2. Allocate 3-5 scenarios per cluster (total 16-22)
3. Assign difficulty levels (20/40/40 balance)
4. **Check**: Total = 16-22; ratio ≈20/40/40

### 2. Reference Collection
1. Gather: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA
2. Tag language ([EN], [ZH]), year, type (1-4)
3. Assign IDs: G1-Gn, C1-Cn, L1-Ln, A1-An
4. **Check**: Counts ≥10/5/6/12; languages ≈60/30/10; ≥50% last 3yr; ≥3 types

### 3. Scenario Generation
1. Write context (200-400 words), assign difficulty + domain
2. Include ≥1 `[Ref: ID]` per context
3. Design 3-4 MECE tasks with rubrics and points
4. **Check** (every 3 scenarios): Lengths 200-400; ≥1 citation; MECE; complete rubrics

### 4. Grading Framework
1. Define expected responses with partial credit
2. Document omissions and edge cases
3. **Check**: All rubrics complete; points sum correctly

### 5. Reference Compilation
1. Populate Glossary, Codebase, Literature, APA sections
2. Include required fields per format
3. Match Reference IDs to inline citations
4. **Check**: All `[Ref: ID]` resolve; all fields present

### 6. Validation
Execute all validation steps. Present report. Fix failures and re-validate.

### 7. Final Review
Check Submission Checklist. Submit when all pass.

---

# Part III: Output Format

Use this structure for scenario banks:

```markdown
## Contents

- [Scenario Bank](#scenario-bank-scenarios-1-n)
- [Scenario 1: [Title]](#scenario-1-title)
- [Scenario 2: [Title]](#scenario-2-title)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Scenario Bank (Scenarios 1–N)

### Scenario X: [Title]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Domain]

**Context:** (200–400 words: constraints, stakeholders, technical details; include `[Ref: ID]`)

**Task 1: [Task Name] (X pts)**
[Description]
- **Expected**: [Key points]
- **Grading**: [Rubric with partial credit]

**Task 2: [Task Name] (X pts)**
[Description]
- **Expected**: [Key points]
- **Grading**: [Rubric]

**Task 3: [Task Name] (X pts)**
[Description]
- **Expected**: [Key points]
- **Grading**: [Rubric]

**Common Omissions:** [List]
**Edge Cases:** [Bonus points]

---

## Reference Sections

Reference IDs: Glossary (G1…Gn), Codebase (C1…Cn), Literature (L1…Ln), APA (A1…An). Use inline: `[Ref: C3, L2]`.

### Glossary, Terminology & Acronyms

**Format:** `**Term/Acronym**: Definition [Lang]`

**Example:** `**MECE**: Mutually Exclusive, Collectively Exhaustive—categories don't overlap and cover all possibilities [EN]`

### Codebase & Library References

**Required:** License, last update/version (≤12mo), languages, integration (API/SDK)  
**Recommended:** Benchmarks, consistency, HA/reliability, audit status

**Format:**
```
**[Name]** (GitHub: owner/repo | License: Type)
- Description: [Brief overview]
- Stack: [Technologies]
- Maturity: Production/Beta/Experimental
- Performance: [Key metrics]
- Security: [Audit status, vulnerabilities]
```

### Authoritative Literature & Reports

**Required:** Type, year, key findings, credibility (peer-reviewed/standard/regulatory), jurisdiction  
**Recommended:** Methodology/dataset, limitations/assumptions

**Format:**
```
**[Title]** (Year) [Lang]
- Authors: [Names/Organization]
- Type: Standard/White Paper/Academic/Regulatory
- Key Findings: [Summary]
- Credibility: Peer-reviewed/Standard/Regulatory
- Jurisdiction: [Regions/markets]
```

### APA Style Source Citations

Group by language (~60% EN, ~30% ZH, ~10% other). Follow APA 7th with language tags.

**Example:**
```
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms: A comparative analysis.
    Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究. 计算机科学, 51(2), 88-95. [ZH]

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system. https://bitcoin.org/bitcoin.pdf [EN]
```

