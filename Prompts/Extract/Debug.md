# Extract Debug Cards

Task: From the source text, create **debug cards** that test detection and correction of errors that matter for deep understanding, informed decisions, and meaningful action.

Definition:
- Each card shows a flawed statement/plan/code/decision related to the text.
- The answer explains what is wrong and gives a better version.

Rules:
- Use only realistic, plausible mistakes (not trivial typos).
- Keep them decision‑critical: errors that would change understanding, risk, or action.
- Question: include the wrong statement and ask "What is wrong and how to fix it?" (or similar).
- Answer: briefly (a) identify the issue, (b) explain why, (c) show the corrected version.
 - Questions and answers may include short code/config snippets, formulas, or small tables/diagrams when needed to illustrate and correct the error; keep them minimal.
 - Include only the minimal portion of the flawed content needed so the card is self-contained and understandable without the source text.

Output (Markdown list only):
- `Q: ...`  (contains the flawed content + debug question)
- `A: ...`  (issue + explanation + corrected form)
 - Do not output any other text (no headings, comments, or explanations).

