# Case Study / Scenario-Based Prompt Template

Purpose: Multi-part scenario questions that assess systems thinking, trade-off analysis, and concise recommendations.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 3–5 case study scenarios per topic cluster. Difficulty distribution: Foundational (20%), Intermediate (40%), Advanced (40%).
- **Numbering:** Number all scenarios sequentially (Scenario 1, Scenario 2, etc.) for easy tracking and reference. Include scenario numbers in Contents links.
- **Bloom Taxonomy:** Target Analyze/Evaluate levels primarily. Foundational scenarios test analysis of straightforward issues; intermediate scenarios require comparing alternatives and discussing trade-offs; advanced scenarios demand evaluation of complex system interactions and synthesis of multi-faceted recommendations.
- **Scenario Design:** Provide 200–400 words with explicit constraints, assumed facts, and self-contained context. Ensure scenario reflects real-world complexity (technical debt, resource limits, stakeholder conflicts).
- **Task Structure:** 3–4 MECE tasks covering: issue identification, solution proposals with trade-offs, remediation plans, stakeholder communication, and decision recommendations.
- **Context:** Include relevant historical/regulatory context, key metrics, and system interactions. Surface technical (protocols, patterns, performance) and business (cost, impact, risk) dimensions. For RWA contexts, incorporate tokenization standards, custody requirements, regulatory compliance, or asset lifecycle considerations.

### 2. Content Design

- **Target Level:** Analyze/Evaluate (Bloom). Expect candidates to synthesize information, compare alternatives, and justify recommendations.
- **Deliverables:** Require outputs such as issue lists, solution memos (≤300 words), decision matrices, stakeholder communication drafts, and remediation timelines.
- **Trade-offs:** Explicitly test understanding of essential trade-offs (e.g., privacy vs transparency, throughput vs consistency, centralization vs decentralization, cost vs resilience).
- **Evaluation Dimensions:** Assess technical depth (correctness, feasibility, scalability), business acumen (cost-benefit, risk management), and communication clarity.

### 3. Evaluation & Grading

- **Rubric:** Provide scoring bands and breakdown per task (e.g., Task 1: 8 pts, Task 2: 10 pts, Task 3: 6 pts).
- **Partial Credit:** Supply checklists for partial credit (e.g., correct diagnosis + incomplete solution = 60%). Document expected evidence and common omissions.
- **Grader Notes:** List key points, acceptable alternative approaches, and edge cases that deserve bonus credit.

### 4. Execution & Format

- **Format:** Markdown with clear task headings, fenced code blocks, and tables. Include assets in `assets/` folder (logs, configs, diagrams) when needed.
- **Clarity Aids:** Use decision matrices (criteria vs options), mermaid diagrams (sequence/flow charts), and comparison tables to clarify system interactions.
- **Tags:** Label each item with Difficulty (Foundational/Intermediate/Advanced) and Bloom level.
- **Citations:** Include APA 7 citations for standards, frameworks, or regulatory references used in scenarios.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use](#how-to-use)
- [Scenario 1: Title](#scenario-1-title)
- [Scenario 2: Title](#scenario-2-title)

## Executive Summary

- [2–4 bullets: assessment goals, topic scope, key trade-offs tested]

## Coverage & Difficulty Summary

| Difficulty | Count | Scenarios |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

## Glossary & Acronym Index

- [Key terms and acronyms used across scenarios]

## How to Use

- Allow 45–60 min per scenario; evaluate depth of analysis, trade-off reasoning, and communication clarity
- Use rubrics for consistent grading; award partial credit per task checklist

---

## Scenario 1: [Title]

**Language:** python  
**Difficulty:** Intermediate  
**Bloom:** Apply/Create

### Scenario Context

<200–400 word scenario text with constraints, metrics, stakeholder details>

### Tasks

1. Identify top 3 issues
2. Propose 2 solutions and discuss trade-offs
3. Draft a recommendation memo (≤300 words)

### Expected Key Points

- **Task 1:** [List expected issues and evidence to cite]
- **Task 2:** [List expected solutions, trade-offs, and decision criteria]
- **Task 3:** [List key elements of a strong memo: clarity, justification, stakeholder framing]

### Grading Rubric

| Task | Max Points | Criteria |
|---|---:|---|
| Task 1 | 8 | Correctness, completeness, evidence |
| Task 2 | 10 | Feasibility, trade-off depth, alternatives |
| Task 3 | 6 | Clarity, structure, decision justification |

### Grader Notes

- Partial credit: Correct diagnosis + incomplete solution = 60%
- Bonus: Novel insights, consideration of edge cases, stakeholder impact analysis
- Common omissions: [List typical gaps]
```
