# Case Study / Scenario

Generate case study and scenario assessments that follow the "Guidelines for LLM-Friendly Prompts": define the task unambiguously, ensure comprehensive-yet-focused coverage, uphold high quality and fairness standards, present information in navigable formats, and mandate explicit validation and success criteria.

---

# Part I: Specifications

## Task Definition & Context Framework

- **Purpose**: Evaluate senior/architect/expert level decision-making across complex scenarios with evidence-backed reasoning.
- **Scope Declaration**: State constraints, assumptions, stakeholders, technical stack, regulatory environment, and boundary conditions up front.
- **Clarity & Precision**: Use consistent terminology, avoid undefined jargon, and request explanations that surface rationale, trade-offs, and mitigation strategies.
- **Context Length**: 200–400 words per scenario, balancing critical facts with concise delivery.
- **Relevance**: Exclude tangential details; tie every element to scenario objectives and evaluation criteria.

## Scenario Inventory Parameters

- **Scenario Count**: 16–22.
- **Domain Clusters**: 3–5 thematic clusters (e.g., DeFi, infrastructure, RWA) with 3–5 scenarios each.
- **Difficulty Mix**: 20% Foundational / 40% Intermediate / 40% Advanced; document rationale for each assignment.
- **Task Design**: 3–4 MECE tasks per scenario; ensure coverage is mutually exclusive and collectively exhaustive.
- **Deliverables**: Issue lists, ≤300-word memos, matrices/comparison tables, stakeholder communications.
- **Trade-off Coverage**: Explicitly assess privacy vs transparency, throughput vs consistency, cost vs resilience, and any domain-specific tensions.
- **Conflict Handling**: Surface alternative approaches, highlight consensus vs dissent, and capture stakeholder implications.
- **Grading Model**: Provide partial-credit rubrics with documented evidence requirements, common omissions, and optional extensions.

## Coverage & Quality Standards

- **MECE & Sufficiency**: Confirm every aspect needed for evaluation is covered without overlap.
- **Breadth & Depth**: Present multiple perspectives (technical, business, regulatory) and probe deeply enough to expose risks and value levers.
- **Significance & Concision**: Prioritize impactful insights; eliminate redundancy.
- **Accuracy & Credibility**: Cross-verify claims with authoritative sources; flag uncertainties.
- **Logic & Fairness**: Require coherent reasoning, counterarguments, known limitations, and acknowledgement of bias.
- **Risk/Value Analysis**: Compare benefits, costs, and risks; propose mitigations for high-risk paths.
- **Practicality**: Emphasize actionable recommendations with measurable outcomes.

## Citation & Evidence Requirements

- **Languages**: ~60% English, ~30% Chinese, ~10% other; tag each citation (e.g., [EN], [ZH]).
- **Source Types**:
  1. Official documentation (standards, vendor docs, RFCs)
  2. Peer-reviewed/standards bodies (ISO, IEEE, journals, conferences)
  3. Audits and industry/regulatory reports
  4. Vetted production codebases (stable releases)
- **Format**: APA 7th with language tags; inline use `[Ref: ID]` for every factual claim, metric, trade-off, or best practice.
- **Evidence Density**: ≥70% scenarios carry ≥1 citation; ≥30% have ≥2. Provide reasoning when evidence is scarce and outline sourcing plans.

## Reference Minimums

| Section | Count | Content |
| --- | --- | --- |
| Glossary | ≥10 | Core concepts, domain jargon, localized terms |
| Codebase & Libraries | ≥5 | Stack components, SDKs, tooling |
| Literature & Reports | ≥6 | Standards, peer-reviewed, regulatory/industry |
| APA Citations | ≥12 | ~60% EN, ~30% ZH, ~10% other |

> If minimums are unmet, document the shortfall, justify it, and provide a remediation plan with timelines.

## Quality Gates & Success Criteria

- **Recency**: ≥50% of sources from last 3 years (≥70% for AI/security topics).
- **Diversity**: ≥3 source types; no single source provides >25% of total citations.
- **Maturity Proof**: Capture license, last commit (≤12 months), stable release tag, and audit status for codebases.
- **Deduplication**: Canonicalize entries; prefer persistent links (DOIs, archived copies).
- **Link Health**: All URLs reachable or paired with archives.
- **Cross-References**: Force alignment between inline `[Ref: ID]` and Reference Sections.
- **Logic Review**: Require self-audit notes confirming coherence, bias checks, and validation of calculations.
- **Success Criteria**: Submission is acceptable only when every checklist item below is satisfied and validation reports show PASS across all checks.

## Pre-Submission Validation

Execute all steps. Remediate failures and re-run validation until complete compliance.

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
| 9 | MECE Tasks | Tasks are mutually exclusive, collectively exhaustive |
|10 | Grading Rubrics | Rubrics complete, points sum correctly |
|11 | Conflict Handling | ≥80% scenarios document alternatives and consensus vs dissent |
|12 | Logic & Fairness Review | Self-check notes confirm reasoning soundness, bias mitigation, and actionability |

**Validation Report Template:**
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
| Logic/Fairness | Notes logged (Yes/No) | PASS/FAIL |
```

> Any failure halts submission. Regenerate the affected sections, re-run validation, and attach the PASS report.

## Submission Checklist

- [ ] Minimums achieved: G≥10, C≥5, L≥6, APA≥12
- [ ] Difficulty mix: 20/40/40 (Foundational/Intermediate/Advanced)
- [ ] Language mix: ~60% EN, ~30% ZH, ~10% other
- [ ] Recency target met: ≥50% (≥70% for AI/security)
- [ ] Source diversity: ≥3 types, max 25% single source
- [ ] Evidence coverage: ≥70% scenarios with ≥1 citation; ≥30% with ≥2
- [ ] Context discipline: All between 200–400 words with inline citations
- [ ] Maturity proof: License + ≤12mo update + release + audit noted
- [ ] Link health: All URLs resolve or have archives
- [ ] Cross-references: IDs in scenarios match reference sections
- [ ] MECE tasks verified for each scenario
- [ ] Rubrics complete with partial credit and totals
- [ ] Logic/fairness self-review logged; validation report = PASS

---

# Part II: Instructions

Execute steps sequentially, logging inline checks before advancing.

## Steps

### 1. Topic Planning
1. Select 3–5 domain clusters covering business, technical, and regulatory angles.
2. Allocate 3–5 scenarios per cluster to reach 16–22 total.
3. Assign difficulty levels (20/40/40 mix) with brief justification notes.
4. Identify primary stakeholders, objectives, and constraints for each scenario.
5. **Check**: Scenario count and difficulty ratio satisfied; stakeholder coverage spans ≥3 groups (e.g., engineering, compliance, product).

### 2. Reference Collection
1. Compile ≥10 glossary entries, ≥5 codebase/library references, ≥6 literature items, ≥12 APA citations.
2. Tag language ([EN], [ZH], [Other]), publication year, and source type (1–4).
3. Document recency, credibility, jurisdiction, and applicability.
4. Assign IDs: G1–Gn, C1–Cn, L1–Ln, A1–An.
5. **Check**: Count minimums met; language distribution ≈60/30/10; ≥50% latest 3 years; ≥3 source types; note any sourcing risks and mitigation plans.

### 3. Scenario Generation
1. Draft 200–400 word contexts with constraints, stakeholders, systems, metrics, and open risks.
2. Embed ≥1 `[Ref: ID]` per context; highlight contentious assumptions and mitigation options.
3. Define 3–4 MECE tasks with explicit deliverables (matrices, memos, plans) and point allocations.
4. Capture expected responses, including quantitative thresholds and qualitative criteria.
5. **Check** (after every 3 scenarios): Context length, citation presence, MECE compliance, rubric completeness, trade-off analysis, fairness notes.

### 4. Grading Framework
1. Detail partial-credit rubrics: full credit, partial, minimal, zero outcomes.
2. Record common omissions, misconceptions, and risk factors.
3. Provide edge cases/bonus paths that reward exceptional insight.
4. **Check**: Points sum correctly; fairness across stakeholder perspectives maintained.

### 5. Risk, Value & Fairness Synthesis
1. Summarize major risks, costs, benefits, and mitigation strategies per scenario cluster.
2. Highlight stakeholder value propositions and potential conflicts.
3. Note limitations, assumptions, and alternative framings to encourage balanced answers.
4. **Check**: Each cluster includes at least one articulated risk/value trade-off and mitigation.

### 6. Reference Compilation
1. Populate Glossary, Codebase, Literature, APA sections using specified formats.
2. Confirm maturity details (license, updates, audits) for codebases.
3. Align inline citations with reference entries; log any unresolved IDs for remediation.
4. **Check**: 100% of `[Ref: ID]` resolve; presentation format requirements met.

### 7. Validation & Self-Review
1. Run the full validation checklist and document the report.
2. Conduct a self-review for logic, bias, accuracy, and completeness; annotate corrections made.
3. **Check**: Validation report shows all PASS entries with supporting evidence.

### 8. Final Review & Packaging
1. Reconfirm submission checklist.
2. Present final deliverable with summary of key insights, outstanding risks, and success indicators.
3. **Check**: Output is ready for direct use without further editing.

---

# Part III: Output Format

Start with a `## Contents` section linking to all top-level headings and major list items.

- Use lists, tables, diagrams, formulas, and code blocks intentionally; default to Mermaid for diagrams and language-tagged fences for code.
- Provide matrices for comparisons, bullet lists for actions, and formulas (LaTeX inline/block) where quantification is required.
- Include quick navigation for scenario clusters, individual scenarios, and reference sections.

Recommended structure:

```markdown
## Contents

- [Scenario Bank](#scenario-bank-scenarios-1-n)
- [Scenario 1: [Title]](#scenario-1-title)
- [Scenario 2: [Title]](#scenario-2-title)
- ...
- [Risk & Value Synthesis](#risk--value-synthesis)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Scenario Bank (Scenarios 1–N)

### Scenario X: [Title]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Domain] | **Stakeholders:** [List]

**Context:** 200–400 words covering constraints, systems, metrics, and open issues; include `[Ref: ID]` for all factual claims.

**Task 1: [Task Name] (X pts)**
[Description]
- **Expected**: [Key points with reasoning and metrics]
- **Grading**: [Rubric with partial-credit bands]
- **Risk/Value Note**: [Primary trade-off + mitigation]

**Task 2...**

**Common Omissions:** [List]
**Edge Cases & Bonus:** [Optional credit guidance]

---

## Risk & Value Synthesis

- Summarize cross-scenario risks, opportunities, and mitigation plans.
- Provide stakeholder impact tables and decision matrices.
- Flag residual uncertainties and next-step research recommendations.

---

## Reference Sections

Reference IDs: Glossary (G1…Gn), Codebase (C1…Cn), Literature (L1…Ln), APA (A1…An). Use inline: `[Ref: C3, L2]`.

### Glossary, Terminology & Acronyms

**Format:** `**Term/Acronym**: Definition [Lang]`

**Example:** `**MECE**: Mutually Exclusive, Collectively Exhaustive—categories do not overlap and cover all possibilities [EN]`

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

