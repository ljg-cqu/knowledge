# Coding Task (Machine-Gradable) Prompt Template

Purpose: Narrow, self-contained programming tasks designed for automated grading with unit tests.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 5–8 coding tasks per topic cluster. Difficulty distribution: Foundational (20%), Intermediate (50%), Advanced (30%).
- **Bloom Taxonomy:** Target Apply/Create levels. Foundational tasks test basic implementation of known algorithms; intermediate tasks require applying patterns to solve multi-step problems; advanced tasks demand creating novel solutions or optimizing for complex constraints.
- **Task Scope:** Keep tasks narrowly scoped and self-contained. Use MECE when building a question bank to avoid overlapping concepts.
- **Specification:** Provide complete problem description including input/output formats, function signature, data structures, allowed libraries, and all edge cases.
- **Constraints:** State explicit constraints: time limits (e.g., 1s per test), memory limits (e.g., 256MB), allowed standard libraries, and prohibited approaches (if any).
- **Complexity:** Specify expected algorithm complexity (time/space) when relevant to the learning objective.

### 2. Content Design

- **Target Level:** Apply/Create (Bloom). Test ability to implement algorithms, manipulate data structures, handle edge cases, and write clean, idiomatic code.
- **Starter Code:** Provide a skeleton with function signature, docstrings, and placeholder comments to guide implementation. Include necessary imports and data structure definitions.
- **Test Coverage:** Supply 6–10 unit tests covering:
  - **Public tests (3–5):** Shown to students for immediate feedback; include basic cases and one edge case.
  - **Hidden tests (3–5):** Not shown; test robustness, performance, and additional edge cases (e.g., empty inputs, large inputs, boundary values).
- **Reference Solution:** Provide a correct, well-commented implementation and brief explanation of approach/complexity.

### 3. Evaluation & Grading

- **Scoring Breakdown:** Recommended: Correctness (60–80%), Edge-case handling (10–25%), Code style/tests (5–10%). Adjust per difficulty.
- **Grader Notes:** Document common implementation mistakes, performance pitfalls, and partial-credit guidance (e.g., correct logic but inefficient → 70%).
- **Auto-Grading:** Use an isolated test runner (e.g., pytest, unittest, jest). Public tests provide feedback; hidden tests ensure robustness without over-fitting.

### 4. Execution & Format

- **Format:** Markdown with fenced code blocks. Specify language (e.g., `python`, `javascript`) and include instructions to run tests locally.
- **Security:** Avoid shipping secrets (private keys, API tokens). Use ephemeral/generated keys or mock credentials where blockchain/crypto interactions are needed.
- **Clarity Aids:** Include a small flowchart (mermaid) showing input→processing→output flow when helpful. Use tables to summarize test cases or constraints.
- **Tags:** Label each task with Difficulty, Bloom level, and language.
- **Citations:** Include APA 7 citations when tasks reference external protocols, algorithms, or standards.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use](#how-to-use)
- [Task 1: Title](#task-1-title)
- [Task 2: Title](#task-2-title)

## Executive Summary

- [2–4 bullets: assessment goals, programming scope, auto-grading approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Tasks |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

## Glossary & Acronym Index

- [Key algorithms, data structures, protocol concepts tested]

## How to Use

- Auto-grade via isolated test runner; public tests for feedback, hidden tests for robustness
- Scoring: Correctness (60–80%), Edge cases (10–25%), Style/tests (5–10%)

---

## Task X: [Title]

**Language:** python  
**Difficulty:** medium  
**Bloom:** Apply|Create

### Problem Description

Implement `validate_transfer(tx)` that checks signature, balance, and asset type.

**Function signature:** `def validate_transfer(tx):`

**Constraints:** time=1s, memory=256MB, allowed libs: stdlib

### Starter Code

\`\`\`python
def validate_transfer(tx):
    """
    Validate a blockchain transfer transaction.
    Args: tx (dict) - transaction with keys: from, to, amount, signature, asset_type
    Returns: bool - True if valid, False otherwise
    """
    # TODO: Implement validation logic
    pass
\`\`\`

### Public Tests

- input: `{"from": "alice", "to": "bob", "amount": 100, ...}` -> output: `True`
- input: `{"from": "alice", "to": "bob", "amount": -10, ...}` -> output: `False`

### Hidden Tests

(Not shown to students; test edge cases, large inputs, boundary values)

### Reference Solution

[Path to solution or brief description of approach and complexity]

### Grader Notes

- Common mistakes: missing edge-case checks, inefficient algorithms, incorrect signature validation
- Partial credit: Correct logic but inefficient → 70%
```
