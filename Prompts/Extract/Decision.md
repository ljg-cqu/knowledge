# Extract Decision Questions

Task: From the source text, create **open decision questions** with short model answers that drive deep understanding, informed decisions, and meaningful action.

Definition:
- Each card describes a concrete situation and asks "What would you do and why?" (or similar).
- No candidate answer is given in the question.
- Answers are open‑ended but concise.

Rules:
- Focus only on decision‑critical scenarios (choices, trade‑offs, actions, priorities).
- Scenario: 1–3 short sentences of context.
- Question: 1 line, ask for action + rationale.
- Answer: 3–5 bullets or 3–5 short sentences: key model, steps, trade‑offs.
- Each question should help the reader understand a situation better and choose what to do next in practice.
 - Answers may use short lists, tiny tables, or compact code/formula/mermaid blocks when they make the decision or trade‑offs clearer; keep them minimal.
 - Make each question self-contained; include only the minimal context needed to understand the situation without the source text.

Output (Markdown list only):
- `Q: ...`  (scenario + decision question)
- `A: ...`  (short, high‑leverage answer)
 - Do not output any other text (no headings, comments, or explanations).
