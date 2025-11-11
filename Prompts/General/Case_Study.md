# Case Study / Scenario

Generate evidence-based case study assessments for senior/architect/expert level decision-making.

---

# Part I: Specifications

## Scope & Structure

- **Purpose**: Evaluate complex scenarios using evidence-backed reasoning across technical, business, and regulatory perspectives.
- **Context**: 200–400 words per scenario stating constraints, assumptions, stakeholders, technical stack, regulatory environment, and boundary conditions.
- **Terminology**: Consistent, precise terms; define all jargon; surface rationale, trade-offs, and mitigation strategies.
- **Scenarios**: 16–22 total across 3–5 domain clusters (e.g., DeFi, infrastructure, RWA) with 3–5 scenarios each.
- **Difficulty**: 20% Foundational / 40% Intermediate / 40% Advanced with documented rationale.
- **Tasks**: 3–4 mutually exclusive, collectively exhaustive (MECE) tasks per scenario.
- **Deliverables**: Issue lists, ≤300-word memos, matrices/tables, stakeholder communications.
- **Trade-offs**: Assess privacy vs transparency, throughput vs consistency, cost vs resilience, and domain-specific tensions.
- **Alternatives**: Document competing approaches, consensus vs dissent, and stakeholder implications.
- **Grading**: Partial-credit rubrics with evidence requirements, common omissions, and bonus paths.

## Quality Requirements

- **Coverage**: Complete, non-overlapping; multiple perspectives; sufficient depth to expose risks and value.
- **Content**: Prioritize impactful insights; eliminate redundancy; exclude tangential information.
- **Accuracy**: Cross-verify with authoritative sources; flag uncertainties.
- **Logic**: Coherent reasoning; acknowledge counterarguments, limitations, biases.
- **Risk/Value**: Compare benefits, costs, risks; propose mitigations.
- **Actionability**: Measurable, implementable recommendations.

## Citations & References

**Sources** (≥3 types; no single source >25%):
1. Official documentation (standards, vendor docs, RFCs)
2. Peer-reviewed/standards bodies (ISO, IEEE, journals, conferences)
3. Audits and industry/regulatory reports
4. Vetted production codebases (stable releases)

**Format**: APA 7th with language tags (~60% EN, ~30% ZH, ~10% other); inline `[Ref: ID]` for all factual claims, metrics, trade-offs, best practices.

**Minimums**:
- Glossary: ≥10 (core concepts, domain jargon, localized terms)
- Codebase & Libraries: ≥5 (stack components, SDKs, tooling with license, last commit ≤12mo, stable release, audit status)
- Literature & Reports: ≥6 (standards, peer-reviewed, regulatory/industry)
- APA Citations: ≥12 total

**Evidence Density**: ≥70% scenarios with ≥1 citation; ≥30% with ≥2.

**Quality Gates**:
- **Recency**: ≥50% from last 3 years (≥70% for AI/security)
- **Links**: All URLs reachable or archived
- **Cross-References**: All inline `[Ref: ID]` resolve to Reference Sections
- **Success**: All validation checks PASS before submission

## Validation Checklist

Execute all checks. Remediate failures and re-run until all PASS.

| Check | Pass Criteria |
| --- | --- |
| Minimums | G≥10, C≥5, L≥6, APA≥12; difficulty 20/40/40 |
| Citations | ≥70% scenarios ≥1 citation; ≥30% ≥2 |
| Languages | EN 50-70%, ZH 20-40%, Other 5-15% |
| Recency | ≥50% last 3yr (≥70% AI/security) |
| Diversity | ≥3 source types; single source ≤25% |
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

> Any FAIL halts submission. Regenerate, re-validate, attach PASS report.

---

# Part II: Instructions

Execute sequentially; verify checks before advancing.

### 1. Topic Planning
1. Select 3–5 domain clusters (business, technical, regulatory angles); allocate 3–5 scenarios per cluster (16–22 total)
2. Assign difficulty (20/40/40 mix) with justification
3. Identify stakeholders, objectives, constraints per scenario
4. **Check**: Count, ratio, ≥3 stakeholder groups covered

### 2. Reference Collection
1. Compile minimums (G≥10, C≥5, L≥6, APA≥12); assign IDs (G1–Gn, C1–Cn, L1–Ln, A1–An)
2. Tag language ([EN], [ZH], [Other]), year, source type (1–4)
3. Document recency, credibility, jurisdiction, applicability
4. **Check**: Minimums met; language ≈60/30/10; ≥50% last 3yr; ≥3 source types; note sourcing risks

### 3. Scenario Generation
1. Draft 200–400 word contexts with constraints, stakeholders, systems, metrics, risks; embed ≥1 `[Ref: ID]`
2. Define 3–4 MECE tasks with deliverables (matrices, memos, plans) and point allocations
3. Capture expected responses with quantitative thresholds and qualitative criteria
4. **Check** (every 3 scenarios): Length, citations, MECE, rubrics, trade-offs, fairness

### 4. Grading Framework
1. Detail partial-credit rubrics (full/partial/minimal/zero); record omissions, misconceptions, risk factors
2. Provide edge cases/bonus paths for exceptional insight
3. **Check**: Points sum; fairness maintained

### 5. Risk, Value & Fairness Synthesis
1. Summarize risks, costs, benefits, mitigations per cluster
2. Highlight stakeholder value and conflicts; note limitations, assumptions, alternative framings
3. **Check**: Each cluster has ≥1 risk/value trade-off + mitigation

### 6. Reference Compilation
1. Populate Glossary, Codebase, Literature, APA sections per specified formats
2. Confirm maturity (license, updates, audits) for codebases; align inline `[Ref: ID]` with entries
3. **Check**: 100% `[Ref: ID]` resolve; format requirements met

### 7. Validation & Self-Review
1. Run validation checklist; document report
2. Self-review logic, bias, accuracy, completeness; annotate corrections
3. **Check**: All PASS with supporting evidence

### 8. Final Review
1. Reconfirm checklist
2. Present deliverable with key insights, risks, success indicators
3. **Check**: Ready for use without editing

---

# Part III: Output Format

Include `## Contents` with links to all sections. Use lists, tables, Mermaid diagrams, LaTeX formulas, language-tagged code blocks.

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

**Context:** 200–400 words with constraints, systems, metrics, risks; `[Ref: ID]` for all claims.

**Task 1: [Name] (X pts)**
- **Expected**: [Key points with reasoning, metrics]
- **Grading**: [Full/partial/minimal/zero credit rubric]
- **Risk/Value**: [Trade-off + mitigation]

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

**Required:** License, last update ≤12mo, languages, integration (API/SDK)
**Optional:** Benchmarks, consistency, HA/reliability, audit status

**Format:**
```
**[Name]** (GitHub: owner/repo | License: Type)
- Description: [Overview]
- Stack: [Technologies]
- Maturity: Production/Beta/Experimental
- Performance: [Metrics]
- Security: [Audit status]
```

### Authoritative Literature & Reports

**Required:** Type, year, key findings, credibility, jurisdiction
**Optional:** Methodology/dataset, limitations/assumptions

**Format:**
```
**[Title]** (Year) [Lang]
- Authors: [Names/Org]
- Type: Standard/White Paper/Academic/Regulatory
- Key Findings: [Summary]
- Credibility: Peer-reviewed/Standard/Regulatory
- Jurisdiction: [Regions]
```

### APA Style Source Citations

Group by language (~60% EN, ~30% ZH, ~10% other). APA 7th with tags.

**Example:**
```
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms: A comparative analysis.
    Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究. 计算机科学, 51(2), 88-95. [ZH]
```

