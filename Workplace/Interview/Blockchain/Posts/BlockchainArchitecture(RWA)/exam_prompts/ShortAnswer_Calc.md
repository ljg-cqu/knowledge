# Short Answer / Numeric Calculation Prompt Template

Purpose: Short constructed-response items requiring concise numeric or short-text answers (calculations, conversions, brief justification).

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 8–12 short-answer/calculation problems per topic cluster. Difficulty distribution: Foundational (25%), Intermediate (50%), Advanced (25%).
- **Bloom Taxonomy:** Target Apply/Analyze levels. Foundational problems test direct formula application; intermediate problems require multi-step calculations and unit conversions; advanced problems demand analysis of results, selection of appropriate methods, or justification of assumptions.
- **Problem Scope:** Self-contained problems with all necessary data. Use MECE to avoid overlapping question types across a bank.
- **Units & Conventions:** Explicitly state units and conventions (e.g., MB = 10^6 bytes vs 2^20 bytes; percentages vs decimals; rounding rules). Provide alternate acceptable answers when ambiguity exists.
- **Problem Types:** Cover calculations (e.g., throughput, latency, gas costs), unit conversions, formula applications, and short justifications (2–3 sentences).

### 2. Content Design

- **Target Level:** Apply/Analyze (Bloom). Test ability to apply formulas, perform multi-step calculations, interpret results, and justify reasoning.
- **Answer Format:** Provide exact expected answer, units, and acceptable tolerance (e.g., ±2% for percentages, ±0.5 for small integers).
- **Worked Solution:** Supply a 2–4 step worked solution showing method and intermediate results. Use clear mathematical notation or pseudocode where appropriate.
- **Partial Credit:** Define rules for method vs arithmetic credit (e.g., correct method with arithmetic error = 70%; correct setup but incomplete = 50%).

### 3. Evaluation & Grading

- **Normalization:** Define numeric normalization rules: strip commas, accept scientific notation, case-insensitive for units (e.g., "KB" vs "kb").
- **Tolerance:** Specify acceptable ranges per question type. Use percentage tolerance for large numbers, absolute tolerance for small values.
- **Human Check:** Include grader notes for questions requiring short justification or interpretation (e.g., "Explain why X is more efficient than Y"). Provide model answers and acceptable variations.

### 4. Execution & Format

- **Format:** Markdown with fenced calculation steps. Clearly label the final answer line (e.g., "**Answer:** 42.5 ms").
- **Clarity Aids:** Use tables to organize data (e.g., inputs, parameters), and include formulas in LaTeX/KaTeX notation when helpful (e.g., `$T = N / R$`).
- **Tags:** Label each item with Difficulty, Bloom level, and question type (calculation/conversion/justification).
- **Citations:** Include APA 7 citations when formulas reference standards, protocol specifications, or published benchmarks.

## Output Template

```markdown
Problem: <problem statement with numeric data>

Answer: <numeric or short text>

Units: <units or none>

Tolerance: <±percentage or ±units>

Worked solution:
- Step 1: ...
- Step 2: ...

Partial credit rules: <description>
Difficulty: medium
Bloom: Apply|Analyze
```
