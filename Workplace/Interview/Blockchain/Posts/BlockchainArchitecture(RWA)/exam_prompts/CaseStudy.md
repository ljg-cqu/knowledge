# Case Study / Scenario-Based Prompt Template

Purpose: Multi-part scenario questions that require problem identification, analysis, trade-off discussion, and a concise recommendation.

## Requirements

- Coverage & Organization: Provide sufficient scenario context and constraints; ensure problems are MECE across tasks and avoid hidden assumptions.
- Content Design: Target Analyze/Evaluate levels. Include 3–4 tasks (issue identification, solutions, trade-offs, recommendation) and expected evidence/key points for each.
- Evaluation: Provide scoring band and checklists for partial credit. Include artifacts to compare (sample memos, timelines, or decision matrices).
- Execution & Format: Markdown with clear task headings, example checklist, and citations where necessary. Include required assets (logs, configs) in `assets/` when applicable.

## Output template (Markdown — for LLM or exam-generator)

Example output (Markdown):

```markdown
Scenario: <200–400 word scenario text>

Tasks:
1. Identify top 3 issues
2. Propose 2 solutions with trade-offs
3. Draft recommendation memo (≤300 words)

Expected key points:
- Task 1: ...
- Task 2: ...
- Task 3: ...

Grading breakdown:
- Task1 max: 8
- Task2 max: 10
- Task3 max: 6

Difficulty: medium|hard
Bloom: Analyze|Evaluate
```

Template (LLM):
"Create a case-study scenario related to [domain]. Requirements:
- Provide a 200–400 word scenario describing an operational or design challenge.
- Provide 3–4 tasks (e.g., identify issues, propose solutions, list trade-offs, draft a recommendation memo ≤300 words).
- Provide an answer key: expected issues, evidence to cite, and a checklist for partial credit.

Output format (JSON):
{
  "scenario":"...",
  "tasks":["Identify top 3 issues","Propose 2 solutions with trade-offs","Draft recommendation memo ≤300 words"],
  "expected_key_points":{ "task1":[...], "task2":[...], "task3":[...] }
}
"

Example (brief):
- Scenario: A tokenized property platform sees inconsistent oracle prices due to unreliable data feeds, causing mispricing and failed settlements.
- Tasks: identify root causes, propose mitigation strategies, draft a short remediation plan.

Grading notes:
- Score each task separately (e.g., task1: 0–8, task2: 0–10, task3: 0–6).
- Use checklists for partial credit: mention of oracles, data validation, fallbacks, economic incentives, and deployment/testing plan.

Use when: you want to evaluate real-world problem solving and justification skills.