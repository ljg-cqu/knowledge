# Short Answer / Numeric Calculation Prompt Template

Purpose: Short constructed-response items that require a concise answer, often numeric. Ideal for calculations, unit conversions, and short justification.

## Requirements

- Coverage & Organization: Problems should be self-contained and avoid ambiguous assumptions; specify units and conventions (binary vs decimal MB, etc.).
- Content Design: Target Apply/Analyze Bloom levels. Provide exact answer, units, tolerance, and a worked solution (2–4 steps). State partial-credit rules (method vs arithmetic).
- Evaluation: Machine-gradable numeric checks with tolerance; include human-check notes when justifications are required.
- Execution & Format: Markdown output with fenced calculation steps and final answer clearly labeled. Cite formulas or reference tables if used.

## Output template (Markdown — for LLM or exam-generator)

Example output (Markdown):

```markdown
Problem: <problem statement with numeric data>

Answer: <numeric or short text>

Units: <units or none>

Tolerance: <±percentage or ±units>

Worked solution:
- Step 1: ...
- Step 2: ...

Partial credit rules: <description>
Difficulty: easy|medium|hard
Bloom: Apply|Analyze
```

Template (LLM):
"Create a short-answer numeric problem on [topic]. Requirements:
- Provide the problem statement with all numerical data.
- Provide the exact answer, units, and acceptable tolerance (e.g., ±2% or ±0.5 units).
- Provide a step-by-step worked solution (2–4 steps).
- Provide grading notes for partial credit (e.g., correct method but arithmetic error = 75%).

Output format (Markdown):

```markdown
Problem: Given a block size of 2 MB and an average transaction size of 250 bytes, how many transactions fit in a block?

Answer: 8,192 (or note conventions: 8,000 depending on decimal MB assumption)

Units: transactions

Worked solution: 2 MB = 2*1024*1024 = 2,097,152 bytes; 2,097,152 / 250 ≈ 8,388 → depending on MB definition use 2,000,000/250=8,000.

Partial credit rules: Correct method but different byte/MB assumptions: 75%
```
"

Example:
- Problem: "If a node has 8 GB RAM and the blockchain index uses 1.2 GB, what percentage of RAM is used?"
- Answer: 15% (approx)

Grading/automation tips:
- For numeric answers use normalization and tolerance checks.
- Store worked solutions alongside answers to enable automated feedback.

Use when: evaluating calculation skills and application of formulas.