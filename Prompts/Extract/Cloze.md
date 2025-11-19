# Extract Cloze Cards

Task: From the source text, create **closed cloze cards** that are decision‑critical and support deep understanding, informed decisions, and meaningful action.

Definition:
- Each card covers one fact, small list, threshold, or short definition.
- The answer is fixed and short.

Rules:
- Use 1–3 blanks `___` or a prompt like "List the N ...".
- No options (no MCQ or match questions).
- Skip trivia; keep only items that matter for real decisions or actions.
- Each card should capture a key lever, concept, or threshold that changes how you understand, decide, or act.
 - Answers may include a very short formula or code fragment when that is the precise item to recall.
 - Make each question self-contained; add minimal context if needed so it is understandable without the source text.

Output (Markdown list only):
- `Q: ...`  (front with blanks or a list prompt)
- `A: ...`  (exact answer, minimal but complete)
 - Do not output any other text (no headings, comments, or explanations).

