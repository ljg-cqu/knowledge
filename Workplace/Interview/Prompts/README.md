# Interview Prompt Templates

A comprehensive collection of interview question templates for technical assessments across multiple formats.

## Overview

This directory contains standardized templates for creating interview questions and assessments at senior/architect/expert levels. All templates follow consistent formatting, citation standards, and evaluation frameworks.

## Template Types

### 1. [Templates/QA.md](Templates/QA.md) - Question & Answer
**Use when:** Assessing deep conceptual understanding, trade-off analysis, and decision-making capabilities.

- **Scope:** 25–30 Q&A pairs
- **Answer Length:** 150–300 words with technical depth
- **Difficulty Distribution:** Maintain 20/40/40 balance across foundational, intermediate, and advanced questions
- **Best for:** Senior/architect/expert technical interviews, architectural discussions
- **Includes:** Diagrams, tables, misconception analysis, failure paths

### 2. [Templates/MCQ.md](Templates/MCQ.md) - Multiple Choice Questions
**Use when:** Testing foundational knowledge, identifying misconceptions, or conducting rapid screening.

- **Scope:** 40–80 questions
- **Format:** 4 options, exactly one correct
- **Difficulty Distribution:** Maintain 20/40/40 balance across foundational, intermediate, and advanced questions
- **Best for:** Initial screening, knowledge verification, online assessments
- **Grading:** Machine-gradable, no partial credit

### 3. [Templates/Short_Answer.md](Templates/Short_Answer.md) - Short Answer / Calculation
**Use when:** Evaluating quantitative skills, formula application, and technical justifications.

- **Scope:** 25–40 problems
- **Difficulty Distribution:** Maintain 20/40/40 balance across foundational, intermediate, and advanced problems
- **Types:** Throughput, latency, gas costs, conversions, performance calculations
- **Best for:** Technical depth assessment, engineering positions
- **Grading:** Partial credit available (method 70%, setup 50%)

### 4. [Templates/True_False.md](Templates/True_False.md) - True/False Statements
**Use when:** Quickly validating understanding of factual information and common misconceptions.

- **Scope:** 18–32 statements
- **Format:** Concise declaratives with rationale
- **Difficulty Distribution:** Maintain 20/40/40 balance across foundational, intermediate, and advanced statements
- **Best for:** Knowledge verification, misconception identification
- **Grading:** Machine-gradable with optional justification (70% answer + 30% rationale)

### 5. [Templates/Cloze.md](Templates/Cloze.md) - Fill-in-the-Blank
**Use when:** Testing specific terminology, formulas, or technical vocabulary recall.

- **Scope:** 24–40 items
- **Format:** Unambiguous blanks with acceptance lists
- **Difficulty Distribution:** Maintain 20/40/40 balance across foundational, intermediate, and advanced items
- **Best for:** API knowledge, command syntax, terminology verification
- **Grading:** Case-insensitive with tolerance ranges

### 6. [Templates/Coding_Task.md](Templates/Coding_Task.md) - Coding Tasks
**Use when:** Evaluating programming skills, algorithm design, and code quality.

- **Scope:** 18–28 tasks
- **Difficulty Distribution:** Maintain 20/40/40 balance across foundational, intermediate, and advanced tasks
- **Components:** Problem statement, test cases, reference solution
- **Best for:** Software engineering roles, algorithm positions
- **Grading:** Correctness 70%, Edge cases 20%, Style 10%

### 7. [Templates/Debugging_Task.md](Templates/Debugging_Task.md) - Debugging Tasks
**Use when:** Assessing problem diagnosis, debugging skills, and code comprehension.

- **Scope:** 15–22 tasks
- **Difficulty Distribution:** Maintain 20/40/40 balance across foundational, intermediate, and advanced tasks
- **Bug Types:** Off-by-one, type mismatch, concurrency, security, performance
- **Best for:** Senior developer roles, code review skills
- **Grading:** Fix 0–6 pts, Explanation 0–3 pts, Tests 0–1 pt

### 8. [Templates/Case_Study.md](Templates/Case_Study.md) - Case Studies
**Use when:** Evaluating system design, stakeholder management, and holistic problem-solving.

- **Scope:** 16–22 scenarios
- **Difficulty Distribution:** Maintain 20/40/40 balance across foundational, intermediate, and advanced scenarios
- **Context:** 200–400 words with constraints and stakeholders
- **Best for:** Architect roles, team lead positions, strategic thinking
- **Components:** Issue identification, solution proposals, communication

## Common Framework

All templates follow consistent standards embedded within each file. Each template is self-contained with complete specifications and formatting guidelines.

### Difficulty Distribution
- Maintain the 20% / 40% / 40% mix across foundational, intermediate, and advanced items.

### Content Principles
- Apply MECE coverage and analysis requirements, ensuring technical, theoretical, practical, and contextual depth.
- Represent multiple viewpoints—engineering, architecture, QA, product, ops, security, economics, and policy.
- For contentious topics, present competing perspectives with citations; acknowledge where experts disagree vs. consensus exists.

### Citation Standards
- Follow language mix (~60% EN, ~30% ZH, ~10% other), source quality standards, and APA 7th edition formatting.

### Evaluation Dimensions
- Calibrate scoring against technical, business, strategic, and actionable dimensions.

### Reference Sections
- Each template includes embedded reference formatting guidelines covering glossary entries, codebase & libraries, literature & reports, and APA citations.

## Usage Guide

### Quick Start
1. Choose the appropriate template based on assessment goals
2. Review the template's Specifications section for standards
3. Follow the template structure in the chosen file
4. Populate content following difficulty distribution (20/40/40)
5. Use the embedded reference formatting guidelines in the Output Format section

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
├── README.md                    # This file - Overview and usage guide
└── Templates/
    ├── Case_Study.md            # Case study scenarios
    ├── Cloze.md                 # Fill-in-the-blank questions
    ├── Coding_Task.md           # Programming challenges
    ├── Debugging_Task.md        # Code debugging tasks
    ├── MCQ.md                   # Multiple choice questions
    ├── QA.md                    # Question & Answer framework template
    ├── Short_Answer.md          # Short answer and calculation problems
    └── True_False.md            # True/false statements
```

## Maintenance

- **Updating Standards:** Each template is self-contained; update individual files as needed
- **Reference Formats:** Citation guidelines are embedded within each template's Output Format section
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
