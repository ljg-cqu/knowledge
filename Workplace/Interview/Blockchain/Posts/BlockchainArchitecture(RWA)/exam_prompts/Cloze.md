# Cloze / Fill-in-the-Blank Prompt Template

Purpose: Create cloze tests that assess recall and comprehension. Good for vocabulary, definitions, or equation completion.

## Requirements

- Coverage & Organization: Use MECE when selecting target terms/phrases; avoid overlapping blanks that cause ambiguous answers.
- Content Design: Target recall/understand levels (Foundational/Intermediate). Provide canonical answers (with synonyms) and normalization rules. State partial-credit policy.
- Evaluation: Provide an acceptance list per blank; list tolerances for numeric blanks and provide grading guidance for partial credit.
- Execution & Format: Markdown output; include ALT text for any inline images. Provide citations when blanks rely on sourced definitions.

## Output template (Markdown — for LLM or exam-generator)

Example output (Markdown):

```markdown
Text: The blockchain trilemma consists of ___, ___, and ___.

Answers:
- Blank 1: scalability (accept: scalability, scale)
- Blank 2: security (accept: security)
- Blank 3: decentralization (accept: decentralization, decentralised)

Normalization: case-insensitive, trim whitespace
Partial credit: per-blank or none
Difficulty: easy|medium|hard
Bloom: Remember|Understand
```

Template (LLM):
"Create a cloze item based on the following sentence or paragraph: `[text with blanks indicated as ___]`. Requirements:
- Provide the canonical answer(s) for each blank as an array (accept synonyms).
- Provide normalization rules (case-insensitive, strip punctuation, allow numeric equivalence where applicable).
- Provide one distractor explanation per blank (why a common wrong answer is wrong).
- Provide difficulty and Bloom level.

Output format (Markdown):

```markdown
Text: The blockchain trilemma consists of ___, ___, and ___.

Answers: ["scalability","security","decentralization"]

Normalization: case-insensitive, trim whitespace

Distractor notes: confusion between decentralization and distribution
```
"

Example:
- Text: "A smart contract is ___ that runs on a blockchain and executes ___ when conditions are met."
- Answers: ["a program","actions"]

Grading tips:
- Use normalization and a small synonym list for each blank.
- Consider partial credit: one correct blank out of two = 50%.
- For numeric blanks provide tolerance (±%) or canonical rounding rules.

Use when: assessing recall of specific facts or filling missing technical terms.