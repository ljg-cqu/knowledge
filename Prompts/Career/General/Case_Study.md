# Case Study / Scenario

Generate evidence-based case study assessments for senior/architect/expert decision-making.

---

# Part I: Specifications

## Scope & Structure

- **Purpose**: Evaluate scenarios using evidence-backed reasoning across technical, business, regulatory perspectives.
- **Context**: 200–400 words stating constraints, assumptions, stakeholders, technical stack, regulatory environment, boundary conditions.
- **Terminology**: Consistent, precise; define jargon; surface rationale, trade-offs, mitigations.
- **Scenarios**: 16–22 total; 3–5 domain clusters; 3–5 scenarios each.
- **Difficulty**: 20% Foundational / 40% Intermediate / 40% Advanced.
- **Tasks**: 3–4 MECE tasks per scenario.
- **Deliverables**: Issue lists, ≤300-word memos, matrices/tables, stakeholder communications.
- **Trade-offs**: Privacy vs transparency, throughput vs consistency, cost vs resilience, domain-specific tensions.
- **Alternatives**: Competing approaches, consensus vs dissent, stakeholder implications.
- **Grading**: Partial-credit rubrics with evidence requirements, omissions, bonus paths.

## Quality Requirements

- **Coverage**: Complete, non-overlapping; multiple perspectives; sufficient depth.
- **Content**: Impactful insights only; no redundancy or tangential information.
- **Accuracy**: Cross-verify authoritative sources; flag uncertainties.
- **Logic**: Coherent reasoning; acknowledge counterarguments, limitations, biases.
- **Risk/Value**: Compare benefits, costs, risks; propose mitigations.
- **Actionability**: Measurable, implementable recommendations.

## Citations & References

**Sources** (≥3 types; single source ≤25%):
1. Official documentation (standards, vendor docs, RFCs)
2. Peer-reviewed/standards bodies (ISO, IEEE, journals, conferences)
3. Audits/industry/regulatory reports
4. Vetted production codebases (stable releases)

**Format**: APA 7th with language tags (~60% EN, ~30% ZH, ~10% other); inline `[Ref: ID]` for factual claims, metrics, trade-offs, best practices.

**Minimums**:
- Glossary: ≥10
- Codebase & Libraries: ≥5 (license, last commit ≤12mo, stable release, audit status)
- Literature & Reports: ≥6
- APA Citations: ≥12

**Evidence Density**: ≥70% scenarios with ≥1 citation; ≥30% with ≥2.

**Quality Gates**:
- **Recency**: ≥50% last 3yr (≥70% AI/security)
- **Links**: All URLs reachable or archived
- **Cross-References**: All `[Ref: ID]` resolve
- **Success**: All checks PASS before submission

## Validation Checklist

Execute all checks. Remediate failures; re-run until PASS.

| Check | Pass Criteria |
| --- | --- |
| Minimums | G≥10, C≥5, L≥6, APA≥12; difficulty 20/40/40 |
| Citations | ≥70% scenarios ≥1; ≥30% ≥2 |
| Languages | EN 50-70%, ZH 20-40%, Other 5-15% |
| Recency | ≥50% last 3yr (≥70% AI/security) |
| Diversity | ≥3 source types; single ≤25% |
| Links | All URLs accessible or archived |
| Cross-refs | All `[Ref: ID]` resolve |
| Context | All 200-400 words |
| MECE | Tasks mutually exclusive, collectively exhaustive |
| Rubrics | Complete, points sum correctly |
| Alternatives | ≥80% scenarios document options + consensus/dissent |
| Logic/Fairness | Self-review confirms reasoning, bias mitigation, actionability |

**Report Format:**
```
| Check | Result | Status |
|-------|--------|--------|
| Minimums | G:X C:Y L:Z A:W (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Languages | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Context | Y/X in range | PASS/FAIL |
| MECE | Y/X verified | PASS/FAIL |
| Rubrics | Y/X complete | PASS/FAIL |
| Alternatives | Y/X comply | PASS/FAIL |
| Logic/Fairness | Logged (Y/N) | PASS/FAIL |
```

> FAIL halts submission. Regenerate, re-validate, attach PASS report.

---

# Part II: Instructions

Execute sequentially; verify checks before advancing.

### 1. Topic Planning
1. Select 3–5 domain clusters; allocate 3–5 scenarios each (16–22 total)
2. Assign difficulty (20/40/40) with justification
3. Identify stakeholders, objectives, constraints per scenario
4. **Check**: Count, ratio, ≥3 stakeholder groups

### 2. Reference Collection
1. Compile minimums (G≥10, C≥5, L≥6, APA≥12); assign IDs
2. Tag language ([EN], [ZH], [Other]), year, source type
3. Document recency, credibility, jurisdiction, applicability
4. **Check**: Minimums met; language ≈60/30/10; ≥50% last 3yr; ≥3 source types

### 3. Scenario Generation
1. Draft 200–400 word contexts with constraints, stakeholders, systems, metrics, risks; embed ≥1 `[Ref: ID]`
2. Define 3–4 MECE tasks with deliverables and point allocations
3. Capture expected responses with quantitative thresholds and qualitative criteria
4. **Check** (every 3 scenarios): Length, citations, MECE, rubrics, trade-offs, fairness

### 4. Grading Framework
1. Detail partial-credit rubrics (full/partial/minimal/zero); record omissions, misconceptions, risk factors
2. Provide edge cases/bonus paths
3. **Check**: Points sum; fairness maintained

### 5. Risk, Value & Fairness Synthesis
1. Summarize risks, costs, benefits, mitigations per cluster
2. Highlight stakeholder value/conflicts; note limitations, assumptions, alternatives
3. **Check**: Each cluster has ≥1 risk/value trade-off + mitigation

### 6. Reference Compilation
1. Populate Glossary, Codebase, Literature, APA sections per formats
2. Confirm maturity (license, updates, audits) for codebases; align `[Ref: ID]`
3. **Check**: 100% `[Ref: ID]` resolve; format met

### 7. Validation & Self-Review
1. Run validation checklist; document report
2. Self-review logic, bias, accuracy, completeness; annotate corrections
3. **Check**: All PASS with evidence

### 8. Final Review
1. Reconfirm checklist
2. Present deliverable with key insights, risks, success indicators
3. **Check**: Ready without editing

---

# Part III: Output Format

Include `## Contents` with links. Use lists, tables, Mermaid diagrams, LaTeX formulas, language-tagged code blocks.

**Structure:**

```markdown
## Contents
- [Scenario Bank](#scenario-bank-scenarios-1-n)
  - [Scenario 1: Title](#scenario-1-title)
  - [Scenario 2: Title](#scenario-2-title)
  - ...
- [Risk & Value Synthesis](#risk--value-synthesis)
- [Reference Sections](#reference-sections)
  - [Glossary](#glossary-terminology--acronyms)
  - [Codebase & Libraries](#codebase--library-references)
  - [Literature & Reports](#authoritative-literature--reports)
  - [APA Citations](#apa-style-source-citations)

---

## Scenario Bank (Scenarios 1–N)

### Scenario X: [Title]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Domain] | **Stakeholders:** [List]

**Context:** 200–400 words with constraints, systems, metrics, risks; `[Ref: ID]` for claims.

**Task 1: [Name] (X pts)**
- **Expected**: Key points with reasoning, metrics
- **Grading**: Full/partial/minimal/zero credit rubric
- **Risk/Value**: Trade-off + mitigation

**Task 2...**

**Common Omissions:** [List]
**Edge Cases/Bonus:** [Optional credit]

---

## Risk & Value Synthesis

Cross-scenario risks, opportunities, mitigations; stakeholder impact tables/decision matrices; residual uncertainties; next steps.

---

## Reference Sections

IDs: Glossary (G1…Gn), Codebase (C1…Cn), Literature (L1…Ln), APA (A1…An). Inline: `[Ref: C3, L2]`.

### Glossary, Terminology & Acronyms

**Format:** `**Term**: Definition [Lang]`
**Example:** `**MECE**: Mutually Exclusive, Collectively Exhaustive [EN]`

### Codebase & Library References

**Required:** License, last update ≤12mo, languages, integration
**Optional:** Benchmarks, consistency, HA/reliability, audit status

**Format:**
```
**[Name]** (GitHub: owner/repo | License: Type)
- Description: Overview
- Stack: Technologies
- Maturity: Production/Beta/Experimental
- Performance: Metrics
- Security: Audit status
```

### Authoritative Literature & Reports

**Required:** Type, year, key findings, credibility, jurisdiction
**Optional:** Methodology/dataset, limitations/assumptions

**Format:**
```
**[Title]** (Year) [Lang]
- Authors: Names/Org
- Type: Standard/White Paper/Academic/Regulatory
- Key Findings: Summary
- Credibility: Peer-reviewed/Standard/Regulatory
- Jurisdiction: Regions
```

### APA Style Source Citations

Group by language (~60% EN, ~30% ZH, ~10% other). APA 7th with tags.

**Example:**
```
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms: A comparative analysis.
    Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究. 计算机科学, 51(2), 88-95. [ZH]
```

