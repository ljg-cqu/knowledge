# Debugging / Code-Reading Prompt Template

Purpose: Supply buggy code plus failing test output and ask students to fix the bug and explain the root cause.

## Requirements

- Coverage & Organization: Provide minimal reproducible buggy code and a clear failing test or error output; avoid multi-bug puzzles when assessing a single concept.
- Content Design: Target Analyze/Evaluate levels. Ask for corrected code, root-cause explanation (concise), and tests that now pass.
- Evaluation: Score on correctness of fix, correctness of explanation, and test coverage. Allow partial credit for correct diagnosis even if fix is incomplete.
- Execution & Format: Markdown with code fences for buggy code and failing output. Provide tester instructions and expected corrected behavior.

## Output template (Markdown — for LLM or exam-generator)

Example output (Markdown):

```markdown
Buggy file: buggy.py

Failing test output:
<stderr or assertion here>

Tasks:
1. Fix the bug
2. Explain root cause (2–4 sentences)
3. Provide tests that now pass

Solution notes:
<corrected code and explanation>

Difficulty: medium|hard
Bloom: Analyze|Evaluate
```

Template (LLM):
"Create a debugging exercise. Requirements:
- Provide a short code snippet (10–50 lines) with one or two realistic bugs.
- Provide the failing test or runtime error message.
- Tasks: 1) Fix the bug(s) and provide corrected code. 2) Explain root cause in 2–4 sentences. 3) Provide minimal tests that now pass.
- Provide the corrected solution and brief explanation for graders.

Output format (files):
- `buggy.py` (or equivalent)
- `tests.py` with failing test and then passing tests
- `solution.md` with corrected code and explanation

Example (brief):
- Buggy code: off-by-one in block height calculation causes index error.
- Failing output: "IndexError: list index out of range"
- Expected student output: fix loop boundary, add defensive checks, and explain root cause.

Grading notes:
- Score for correct fix (0–6), explanation quality (0–3), and tests (0–1).
- Allow partial credit if the fix handles most but not all edge cases.

Use when: assessing debugging skills, code reading, and explanation.