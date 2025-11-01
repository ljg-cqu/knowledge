# Data-Interpretation / Graph / Table Prompt Template

Purpose: Questions that provide a dataset, figure, or table and ask for extraction, calculation, and interpretation.

## Requirements

- Coverage & Organization: Provide clean, well-documented datasets or figures; ensure tasks are MECE (extraction, calculation, interpretation separated clearly).
- Content Design: Target Apply/Analyze levels. Include clear question prompts (compute, identify, interpret) and expected numeric answers with tolerances.
- Evaluation: Provide grading guidance and tolerances for numeric answers; use keyword lists for interpretive answers and partial-credit rubrics.
- Execution & Format: Markdown with dataset links in `assets/`; include sample code snippets for loading and plotting where useful. Cite data sources.

## Output template (Markdown — for LLM or exam-generator)

Example output (Markdown):

```markdown
Dataset: assets/block_times.csv

Questions:
1. Compute average block time (numeric)
2. Identify outliers (interpretive)

Answers:
- Q1: <numeric answer> (tolerance ±%)
- Q2: <list of outlier indices>

Plots:
- expected_plot_1.png

Difficulty: medium
Bloom: Apply|Analyze
```

Template (LLM):
"Create a data-interpretation item. Requirements:
- Provide a small dataset (CSV or inline table) or a figure (image path).
- Provide 3–5 questions: extraction (e.g., compute mean), calculation (e.g., compute correlation), and interpretation (e.g., explain an observed pattern).
- Provide expected numeric answers, plots (if required), and interpretive key points.

Output format (folder or JSON):
{
  "dataset":"...",
  "questions":[{"q":"Compute average block time"...}],
  "answers":[...],
  "plots":["expected_plot_1.png"]
}
"

Example:
- Dataset: timestamped block times for 100 blocks.
- Questions: compute average block time, identify outliers, suggest reason for spikes.

Grading tips:
- For numeric answers provide tolerance. For interpretation, use a short rubric: correct observation (0–2), plausible explanation (0–3).
- For automated grading, compare submitted numeric outputs and compute similarity for textual interpretations against expected keywords.

Use when: assessing data literacy and ability to draw evidence-based conclusions.