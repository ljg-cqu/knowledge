# Interview Prompt Templates

A comprehensive collection of interview question templates for technical assessments across multiple formats.

## Overview

This directory contains standardized templates for creating interview questions and assessments at senior/expert levels. All templates follow consistent formatting, citation standards, and evaluation frameworks.

## Template Types

### 1. [QA.md](QA.md) - Question & Answer
**Use when:** Assessing deep conceptual understanding, trade-off analysis, and decision-making capabilities.

- **Scope:** 25–30 Q&A pairs
- **Answer Length:** 150–300 words with technical depth
- **Best for:** Senior/expert technical interviews, architectural discussions
- **Includes:** Diagrams, tables, misconception analysis, failure paths

### 2. [Templates/MCQ.md](Templates/MCQ.md) - Multiple Choice Questions
**Use when:** Testing foundational knowledge, identifying misconceptions, or conducting rapid screening.

- **Scope:** 40–80 questions
- **Format:** 4 options, exactly one correct
- **Difficulty Tags:** Label each stem to maintain the 20/40/40 distribution from [Requirements.md](Requirements.md)
- **Best for:** Initial screening, knowledge verification, online assessments
- **Grading:** Machine-gradable, no partial credit

### 3. [Templates/Short_Answer.md](Templates/Short_Answer.md) - Short Answer / Calculation
**Use when:** Evaluating quantitative skills, formula application, and technical justifications.

- **Scope:** 25–40 problems
- **Types:** Throughput, latency, gas costs, conversions, performance calculations
- **Best for:** Technical depth assessment, engineering positions
- **Grading:** Partial credit available (method 70%, setup 50%)

### 4. [Templates/True_False.md](Templates/True_False.md) - True/False Statements
**Use when:** Quickly validating understanding of factual information and common misconceptions.

- **Scope:** 18–32 statements
- **Format:** Concise declaratives with rationale
- **Difficulty Tags:** Track difficulty to balance misconception coverage across levels
- **Best for:** Knowledge verification, misconception identification
- **Grading:** Machine-gradable with optional justification (70% answer + 30% rationale)

### 5. [Templates/Cloze.md](Templates/Cloze.md) - Fill-in-the-Blank
**Use when:** Testing specific terminology, formulas, or technical vocabulary recall.

- **Scope:** 24–40 items
- **Format:** Unambiguous blanks with acceptance lists
- **Difficulty Tags:** Maintain coverage balance and document mastery progression
- **Best for:** API knowledge, command syntax, terminology verification
- **Grading:** Case-insensitive with tolerance ranges

### 6. [Templates/Coding_Task.md](Templates/Coding_Task.md) - Coding Tasks
**Use when:** Evaluating programming skills, algorithm design, and code quality.

- **Scope:** 18–28 tasks
- **Components:** Problem statement, test cases, reference solution
- **Best for:** Software engineering roles, algorithm positions
- **Grading:** Correctness 70%, Edge cases 20%, Style 10%

### 7. [Templates/Debugging_Task.md](Templates/Debugging_Task.md) - Debugging Tasks
**Use when:** Assessing problem diagnosis, debugging skills, and code comprehension.

- **Scope:** 15–22 tasks
- **Bug Types:** Off-by-one, type mismatch, concurrency, security, performance
- **Best for:** Senior developer roles, code review skills
- **Grading:** Fix 0–6 pts, Explanation 0–3 pts, Tests 0–1 pt

### 8. [Templates/Case_Study.md](Templates/Case_Study.md) - Case Studies
**Use when:** Evaluating system design, stakeholder management, and holistic problem-solving.

- **Scope:** 16–22 scenarios
- **Context:** 200–400 words with constraints and stakeholders
- **Best for:** Architect roles, team lead positions, strategic thinking
- **Components:** Issue identification, solution proposals, communication

## Common Framework

All templates are governed by the shared standards in [Requirements.md](Requirements.md) and [Shared_References.md](Shared_References.md). Use the checklist below as a quick navigation aid.

### Difficulty Distribution
- Maintain the [20% / 40% / 40% mix](Requirements.md#difficulty-distribution) across foundational, intermediate, and advanced items.

### Content Principles
- Apply the [MECE coverage and analysis requirements](Requirements.md#content-principles), ensuring technical, theoretical, practical, and contextual depth.
- Represent multiple viewpoints—engineering, architecture, QA, product, ops, security, economics, and policy.

### Citation Standards
- Follow the [language mix, source quality, and APA formatting rules](Requirements.md#citation-standards).

### Evaluation Dimensions
- Calibrate scoring against the [technical, business, strategic, and actionable dimensions](Requirements.md#evaluation-dimensions).

### Reference Sections
- Populate the shared reference blocks defined in [Shared_References.md](Shared_References.md), covering glossary entries, codebase & libraries, literature & reports, and APA citations.

## Usage Guide

### Quick Start
1. Choose the appropriate template based on assessment goals
2. Review [Requirements.md](Requirements.md) for common standards
3. Follow the template structure in the chosen file
4. Populate content following difficulty distribution
5. Reference [Shared_References.md](Shared_References.md) for citation formatting

### Combining Templates
For comprehensive assessments, combine multiple formats:
- **Junior Level:** MCQ (60%) + Coding Task (40%)
- **Mid Level:** Short Answer (30%) + Coding Task (40%) + Debugging Task (30%)
- **Senior Level:** Q&A (40%) + Case Study (30%) + Coding Task (30%)
- **Expert/Architect Level:** Q&A (50%) + Case Study (50%)

### Customization
Each template includes:
- Scope recommendations (adjustable based on role)
- Grading rubrics (adapt to organizational needs)
- Content structure (maintain for consistency)

## File Structure

```
Prompts/
├── README.md                    # This file
├── Requirements.md              # Common standards & principles
├── Shared_References.md         # Reference formatting guidelines
├── QA.md                        # Q&A template
└── Templates/
    ├── Case_Study.md
    ├── Cloze.md
    ├── Coding_Task.md
    ├── Debugging_Task.md
    ├── MCQ.md
    ├── Short_Answer.md
    └── True_False.md
```

## Maintenance

- **Updating Standards:** Modify [Requirements.md](Requirements.md) for framework-wide changes
- **Reference Formats:** Update [Shared_References.md](Shared_References.md) for citation changes
- **Template Evolution:** Maintain backward compatibility when updating individual templates
- **Version Control:** Document significant changes in commit messages

## Best Practices

1. **Calibrate Difficulty:** Test questions internally before deployment
2. **Validate References:** Ensure all citations are credible and current
3. **Review Grading:** Pilot rubrics with sample responses
4. **Maintain Balance:** Follow MECE principles and difficulty distribution
5. **Update Regularly:** Refresh content to reflect current best practices and technologies

---

*For questions or contributions, refer to the main knowledge base structure at `/home/zealy/nas/github/ljg-cqu/knowledge/`.*
