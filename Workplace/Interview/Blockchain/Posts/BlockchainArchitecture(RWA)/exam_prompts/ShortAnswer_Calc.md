# Short Answer / Numeric Calculation Prompt Template

Purpose: Short constructed-response items requiring concise numeric or short-text answers (calculations, conversions, brief justification).

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 8–12 short-answer/calculation problems per topic cluster. Difficulty distribution: Foundational (25%), Intermediate (50%), Advanced (25%).
- **Numbering:** Number all problems sequentially (P1, P2, etc.) for easy tracking and reference. Include problem numbers in Contents links.
- **Bloom Taxonomy:** Target Apply/Analyze levels. Foundational problems test direct formula application; intermediate problems require multi-step calculations and unit conversions; advanced problems demand analysis of results, selection of appropriate methods, or justification of assumptions.
- **Problem Scope:** Self-contained problems with all necessary data. Use MECE to avoid overlapping question types across a bank.
- **Units & Conventions:** Explicitly state units and conventions (e.g., MB = 10^6 bytes vs 2^20 bytes; percentages vs decimals; rounding rules). Provide alternate acceptable answers when ambiguity exists.
- **Problem Types:** Cover calculations (e.g., throughput, latency, gas costs, tokenization ratios, collateralization rates), unit conversions, formula applications, and short justifications (2–3 sentences). For RWA contexts, include asset valuation, transaction fee modeling, or compliance threshold calculations.

### 2. Content Design

- **Target Level:** Apply/Analyze (Bloom). Test ability to apply formulas, perform multi-step calculations, interpret results, and justify reasoning.
- **Answer Format:** Provide exact expected answer, units, and acceptable tolerance (e.g., ±2% for percentages, ±0.5 for small integers).
- **Worked Solution:** Supply a 2–4 step worked solution showing method and intermediate results. Use clear mathematical notation or pseudocode where appropriate.
- **Partial Credit:** Define rules for method vs arithmetic credit (e.g., correct method with arithmetic error = 70%; correct setup but incomplete = 50%).

### 3. Evaluation & Grading

- **Normalization:** Define numeric normalization rules: strip commas, accept scientific notation, case-insensitive for units (e.g., "KB" vs "kb").
- **Tolerance:** Specify acceptable ranges per question type. Use percentage tolerance (e.g., ±2%) for large numbers or ratios, absolute tolerance (e.g., ±0.5) for small integer values.
- **Human Check:** Include grader notes for questions requiring short justification or interpretation (e.g., "Explain why X is more efficient than Y"). Provide model answers and acceptable variations.

### 4. Execution & Format

- **Format:** Markdown with fenced calculation steps. Clearly label the final answer line (e.g., "**Answer:** 42.5 ms").
- **Clarity Aids:** Use tables to organize data (e.g., inputs, parameters), and include formulas in LaTeX/KaTeX notation when helpful (e.g., `$T = N / R$`).
- **Tags:** Label each item with Difficulty, Bloom level, and question type (calculation/conversion/justification).
- **Citations:** Include APA 7 citations for formulas referencing standards, protocol specifications, or published benchmarks.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use](#how-to-use)
- [Problems 1–12](#problems-112)

## Executive Summary

- [2–3 bullets: assessment goals, calculation scope, grading approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Problems |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

## Glossary & Acronym Index

- [Key formulas, units, and conventions]

## How to Use

- Machine-gradable with tolerance checks; manual review for justification questions
- Scoring: Method credit + arithmetic credit; store worked solutions for feedback

---

## Problems 1–12

### P1: Calculate blockchain throughput

**Problem:** A blockchain processes 500 transactions per block with an average block time of 6 seconds. Calculate the throughput in transactions per second (TPS).

**Answer:** 83.33 TPS

**Units:** transactions per second (TPS)

**Tolerance:** ±2%

**Worked solution:**
1. Transactions per block: 500
2. Block time: 6 seconds
3. TPS = 500 / 6 = 83.33 TPS

**Partial credit rules:**
- Correct formula with arithmetic error: 70% of question points
- Correct setup but incomplete: 50% of question points

**Difficulty:** Foundational  
**Bloom:** Apply
```
