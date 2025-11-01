# Multiple-Choice (MCQ) Prompt Template

Purpose: Generate single-best-answer multiple-choice questions (3+ options) with plausible distractors and a concise rationale for the correct option. For binary True/False items use `TrueFalse.md`.

## Requirements

- Coverage & Organization: follow MECE principle for topic selection; ensure distractors cover common misconceptions and non-overlapping concepts.
- Content Design: Target senior/intermediate candidates. Each item must include a clear stem, four options (A–D), exactly one correct answer, and a 1–2 sentence rationale for the correct option and brief notes on distractors.
- Evaluation: Machine-gradable by option letter; include difficulty tag (easy/medium/hard) and Bloom level.
- Execution & Format: Markdown output; include a compact Contents link if used within a larger exam. Provide authoritative references if a fact needs sourcing.
- Assets & Citations: If code snippets or diagrams are used, include them as fenced blocks and cite sources (APA) where needed.

## Output template (Markdown — for LLM or exam-generator)

Example output (Markdown):

```markdown
Stem: <question text>

Options:
- A. Option A
- B. Option B
- C. Option C
- D. Option D

Answer: A

Rationale:
- Correct: <short explanation>
- Distractors:
  - B: <why wrong>
  - C: <why wrong>
  - D: <why wrong>

Difficulty: easy|medium|hard
Bloom: Remember|Apply|Analyze
```

Template (to give to an LLM):

"Create a multiple-choice question on [topic]. Requirements:
- Provide a clear question stem (1–2 sentences).
- Provide 4 options labeled A–D. Exactly one option must be correct.
- Make three distractors plausible and common misconceptions.
- Mark the correct option and provide a 1–2 sentence rationale explaining why it's correct and why each distractor is wrong.
- Indicate difficulty (easy/medium/hard) and Bloom level (Remember/Apply/Analyze/etc.).

Output format (Markdown):

```markdown
Stem: ...

Options:
- A. ...
- B. ...
- C. ...
- D. ...

Answer: A

Rationale: ...

Difficulty: medium
Bloom: Apply
```
"

Example:
- Stem: "Which consensus mechanism requires validators to stake tokens to participate in block validation?"
- Options: A) Proof of Work, B) Proof of Stake, C) Practical Byzantine Fault Tolerance, D) Proof of Capacity
- Answer: B
- Rationale: "Proof of Stake requires validators to lock up tokens as collateral; Proof of Work relies on computational work..."

Grading/automation notes:
- Machine-gradable: yes (exact-match of the correct option letter).
- To randomize, shuffle options client-side but track the correct index.
- For variants, ask the LLM to produce N unique items with non-overlapping stems.

Use when: you need quick objective items that are easily auto-scored or used in LMSs.