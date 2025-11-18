---
last_updated: 2025-11-18
status: Reviewed
owner: ljg-cqu
---

# Statistics Q&A Guide

Generate scenario-based questions testing statistical reasoning in decision-critical contexts. Focus on methodological choices impacting conclusions, risks, or stakeholders.

**Scope**: Practical scenarios requiring judgment; exclude pure theory, proofs, trivia, or niche methods.

**Purpose**: Develop reasoning through application and interpretation.

**Assumptions**: Basic statistical knowledge.

**Key Elements**:
- **Difficulty Levels**:
  - **F** = Foundational (execution-level tasks)
  - **I** = Intermediate (strategy/trade-offs)
  - **A** = Advanced (portfolio/vision/P&L)
- Dimensions: Mathematical, Applied, Interpretive, Computational.

**Decision-Criticality** (include if ≥1 criterion satisfied):
- **Blocks Decision**: Prevents drawing valid conclusions or choosing appropriate methods
- **Creates Risk**: Material threat (incorrect inference, invalid assumptions, misleading conclusions)
- **Affects ≥2 Stakeholder Roles**: Multi-team impact (Analysts, Researchers, Data Scientists, PMs)
- **Requires Action**: 1-6mo implementation or analysis window
- **Quantified Impact**: Measurable metrics (power %, confidence intervals, effect sizes, p-values)

## Structure

**Q&A Pairs**: 3–5, 20% F / 40% I / 40% A across difficulty and topics (Inference, Experimental Design, Modeling, Interpretation).

**Topics Coverage**: Inference, experimental design, modeling, interpretation.

**References**: Glossary of key terms, tools, textbooks, citations (APA format).

**Visuals**: Diagrams and tables to illustrate concepts and processes.

## Generation Process

1. **Plan**: Select real-world scenarios with varying difficulty.
2. **Questions**: Scenario-based; focus on assumptions, choices, interpretations.
3. **Answers**: 150–250 words; include framework, steps, examples, trade-offs, pitfalls; cite references.
4. **Artifacts**: Include plots, tables, or flowcharts.
5. **Validation**: Ensure application focus, concrete insights, explicit assumptions.

## Output Format

### Overview
- Difficulty mix: 20% F / 40% I / 40% A
- Topics: 4 areas covered

### Q&A Format

**QX: Question**

**Difficulty**: F/I/A | **Topic**: Area | **Criticality**: Reason

**Insight**: Key takeaway.

**Answer**: Framework, analysis, example, trade-offs, pitfalls, software/tools, citations.

**Artifact**: Visual or table.

**Justification**: Why decision-critical.

### References
- **Glossary**: Key terms with definitions, intuition, uses.
- **Tools**: Software with descriptions, capabilities.
- **Textbooks**: Recommended resources.
- **Citations**: Evidence-based sources.

### Evaluation
Include practice questions, checklists, guides for assessment.

## Example (Illustrative)

**Q1: Clinical trial n=45: treatment μ=12 (SD=8) vs. control μ=8 (SD=7). t-test p=0.04, d=0.53. Power assumed d=0.8, n=40. Interpret and suggest analyses.**

**Difficulty**: I | **Topic**: Inference | **Criticality**: Blocks decision

**Insight**: Significance ≠ practical importance; study underpowered.

**Answer**:

Framework: Evaluate p-value, effect size, confidence interval, power [Ref: L2].

Dimensions (Interpretive/Applied):

1. Significance: p=0.04 marginal; d=0.53 medium but <0.8 expected. 95% CI ≈ (−0.6,8.6) includes 0.

2. Power: ~45% at d=0.53; original assumption optimistic.

Assumptions: Normality (CLT applies), equal variance, independence.

Trade-offs: Strict α protects Type I error but may miss effects; consider Bayesian alternatives.

Software: R (`t.test`, `pwr` package).

Recommendation: Results suggest moderate effect but uncertainty high; replicate with larger n for adequate power.

**Pitfalls**: Over-relying on p-value; post-hoc power calculations.

**Justification**: Misinterpretation blocks valid decisions on treatment efficacy.

**Artifact**:

| Component | Result | Interpretation |
|-----------|--------|----------------|
| p-value | 0.04 | Marginal significance |
| Effect size d | 0.53 | Medium, below expected |
| 95% CI | (−0.6,8.6) | Includes 0, wide range |
| Power | ~0.45 | Underpowered |

