# Debugging / Code-Reading Prompt Template

Purpose: Provide a short buggy code snippet plus failing output; ask students to fix the bug, explain the root cause, and supply minimal passing tests.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 5–8 debugging tasks per topic cluster. Difficulty distribution: Foundational (20%), Intermediate (50%), Advanced (30%).
- **Bloom Taxonomy:** Target Analyze/Evaluate levels. Foundational tasks involve identifying obvious bugs with clear error messages; intermediate tasks require tracing logic flow and understanding API contracts; advanced tasks demand evaluating subtle concurrency issues or security vulnerabilities.
- **Bug Scope:** Provide a single, realistic, focused bug in a 10–50 line snippet. Avoid multi-bug puzzles unless explicitly testing triage skills.
- **Bug Types:** Cover common categories: off-by-one errors, type mismatches, incorrect API usage, concurrency issues, edge-case handling, logic errors, or security flaws (e.g., missing validation).
- **Context:** Include minimal surrounding context (imports, data structures, function calls) to make the bug reproducible without extraneous code.

### 2. Content Design

- **Target Level:** Analyze/Evaluate (Bloom). Test ability to read code, diagnose root causes, and propose correct fixes.
- **Deliverables:** Require three outputs:
  1. **Corrected code:** Fixed version with minimal changes (annotate changes with comments if helpful).
  2. **Root-cause explanation:** 2–4 sentence explanation identifying the bug, why it occurs, and what principle/pattern was violated.
  3. **Passing tests:** Minimal test cases that now pass (previously failed) to demonstrate the fix.
- **Failing Output:** Provide realistic failing test output (stderr, assertion errors, unexpected behavior) to guide diagnosis.

### 3. Evaluation & Grading

- **Rubric:** Recommended scoring: Fix correctness (0–6 pts), Explanation quality (0–3 pts), Tests provided (0–1 pt). Adjust per difficulty.
- **Partial Credit:** Award partial credit for correct diagnosis even if fix is incomplete, or correct fix with weak explanation.
- **Grader Notes:** Document common incorrect approaches (e.g., treating symptom instead of root cause) and alternative valid fixes. List edge cases where fixes might fail.

### 4. Execution & Format

- **Format:** Markdown with fenced code blocks for buggy code, failing output, and corrected code. Include instructions to run tests and verify the fix.
- **Clarity Aids:** When helpful, include a small mermaid diagram or table showing expected vs actual behavior, or a flowchart highlighting where logic diverges.
- **Tags:** Label each task with Difficulty, Bloom level, and language.
- **Citations:** Include APA 7 citations only if the bug references external APIs, standards, or protocol-specific behavior.

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

- [2–4 bullets: assessment goals, bug type coverage, evaluation approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Tasks |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

## Glossary & Acronym Index

- [Key concepts, APIs, patterns relevant to debugging tasks]

## How to Use

- Evaluate fix correctness, root-cause depth, and test coverage
- Scoring: Fix (0–6), Explanation (0–3), Tests (0–1)

---

## Task X: [Title]

**Language:** python  
**Difficulty:** medium  
**Bloom:** Analyze|Evaluate

### Buggy Code

\`\`\`python
# buggy.py
def process_transactions(txs):
    total = 0
    for tx in txs:
        total += tx['amount']
    return total / len(txs)  # Bug: division by zero if txs is empty
\`\`\`

### Failing Test Output

```
AssertionError: Expected 0, got ZeroDivisionError
```

### Tasks

1. Fix the bug
2. Explain root cause (2–4 sentences)
3. Provide tests that now pass

### Solution Notes (for graders)

**Corrected code:**

\`\`\`python
def process_transactions(txs):
    if not txs:
        return 0
    total = 0
    for tx in txs:
        total += tx['amount']
    return total / len(txs)
\`\`\`

**Root cause explanation:** The function fails when the input list is empty because it attempts division by zero. The fix adds a guard clause to return 0 for empty inputs.

**Tests:**
- `process_transactions([])` -> `0` (now passes)
- `process_transactions([{"amount": 100}])` -> `100` (now passes)

**Grader Notes:**
- Partial credit: Correct diagnosis but incomplete fix → 60%
- Common mistakes: catching exception instead of preventing it, incorrect edge-case handling
```
