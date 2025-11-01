# True / False (T/F) Prompt Template

Purpose: Produce declarative statements that students judge as True or False. This file provides an authoring and grading template separate from multi-option MCQs.

## Requirements

- Coverage & Organization: Statements must be precise and unambiguous (avoid double negatives). Use the MECE principle when selecting statements across an exam bank to avoid overlapping claims.
- Content Design: Target Remember/Understand/Apply Bloom levels. Prefer factual or definitional statements for lower levels and scenario-based judgement statements for higher levels.
- Evaluation: Machine-gradable by option letter (A/True, B/False). If justification is required, specify whether it's optional or required for full credit.
- Execution & Format: Markdown output. If a statement references external facts, include an APA citation. Include difficulty and Bloom tags.

## Output template (Markdown — for LLM or exam-generator)

Example output (Markdown):

```markdown
Statement: <declarative statement to judge>

Options:
- A. True
- B. False

Answer: A  # or B

Rationale:
- Correct: <1–2 sentence explanation>
- Common misconception: <why the opposite may look plausible>

Difficulty: easy|medium|hard
Bloom: Remember|Understand|Apply
Citation: <APA if sourced>
```

Template (to give to an LLM):
"Create 10 True/False statements on [topic]. Requirements:
- Provide a clear declarative statement per item.
- Indicate the correct answer (True or False) and a 1–2 sentence rationale for correctness and one-sentence note on common misconception.
- Tag each item with difficulty and Bloom level.

Output format (Markdown): follow the Example output block above."

Example:
- Statement: "Proof of Stake requires validators to expend computational work to create blocks."
- Options: A. True, B. False
- Answer: B
- Rationale: "False — Proof of Stake requires validators to lock tokens as stake; Proof of Work requires computational work."

Grading notes:
- Machine-gradable by exact answer letter.
- If justification required, award partial credit for correct letter and additional credit for valid rationale (e.g., 70% + 30%).

Use when: you need quick binary-check facts or to test conceptual clarity with low authoring overhead.