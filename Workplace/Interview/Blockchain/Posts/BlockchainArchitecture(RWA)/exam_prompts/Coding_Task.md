# Coding Task (Machine-Gradable) Prompt Template

Purpose: Create programming tasks with clear specs and unit tests so submissions can be auto-graded.

## Requirements

- Coverage & Organization: Tasks should be narrowly scoped and self-contained. Avoid ambiguous I/O formats; specify edge cases and complexity expectations.
- Content Design: Target Apply/Create levels. Provide function signature, constraints (time/memory), allowed libraries, starter code, and public/hidden tests.
- Evaluation: Auto-grade via unit tests; include hidden tests for robustness. Provide scoring breakdown (correctness, edge cases, style/tests).
- Execution & Format: Markdown with code fences for starter code and tests. Include instructions for running tests locally and expected outputs. Cite third-party libs used.

## Output template (Markdown — for LLM or exam-generator)

Example output (Markdown):

```markdown
Task: <short description>

Language: python

Function signature: def foo(args):

Constraints: time=1s, memory=256MB, allowed libs: stdlib

Starter code: `starter.py` (path)

Public tests:
- input: ... -> output: ...
- input: ... -> output: ...

Hidden tests: (not shown to students)

Reference solution: (short description or path to solution file)

Difficulty: medium|hard
Bloom: Apply|Create
```

Template (LLM):
"Create a coding task in [language] on [topic]. Requirements:
- Provide a concise problem description and function signature.
- Provide constraints (time/memory, allowed libraries).
- Provide a starter file skeleton and 6–10 unit tests (include edge cases and hidden tests suggestion).
- Provide one correct solution and brief explanation.

Output format (JSON or file bundle):
{
  "task":"Implement function `validate_transfer(tx)` that checks signature, balance, and asset type.",
  "language":"python",
  "starter_code":"def validate_transfer(tx):\n    # implement\n    pass\n",
  "public_tests":[{"input":...,"output":...},...],
  "hidden_tests":[...],
  "solution":"..."
}
"

Example (sketch):
- Problem: Write `is_valid_signature(message, signature, pubkey)` that verifies ECDSA secp256k1 signatures (use provided helper `ecdsa_verify`).
- Starter code: minimal stub.
- Tests: valid signature, altered message, wrong pubkey, malformed signature.

Grading/automation notes:
- Provide both public and hidden tests. Auto-grade by running unit tests in an isolated environment.
- For security-related tasks, avoid shipping private keys in examples; use generated ephemeral keys.

Use when: you need code solutions that can be validated automatically.