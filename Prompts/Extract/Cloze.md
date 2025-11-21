# Extract Cloze Cards

Task: From the source text, create **cloze cards** that are decision-critical and support deep understanding, informed decisions, and meaningful action.

Definition:
- Each card covers one fact, list (2-5 items), threshold, or short definition.
- The answer is fixed and short (context-independent).

Rules:
- **Read the entire source text**: Process line-by-line to identify all decision-critical content. Do not stop prematurely or skip sections.
- **Extract comprehensively**: Cover all decision-critical aspects. If the source has depth, generate sufficient cards to reflect that depth.
- **Maintain strict fidelity**: Use only information explicitly stated or logically implied in the source. Never invent facts, numbers, concepts, or corrections.
- Use 1-3 blanks `___` per card, or a prompt like "List the N ...".
- No options (no MCQ or match questions).
- Skip trivia; keep only items that anchor decisions or actions.
- Focus on precise facts, numbers, terms, or sequences that must be recalled accurately.
- Answers may include a short formula or code fragment when that is the item to recall.
- Make each question self-contained; add context only if needed for clarity.

Output format (Markdown ordered list):
1. Q: ...  (question with blanks or list prompt)
   A: ...  (exact answer, concise and complete)

Instructions:
- Use `1.` for every item; Markdown auto-numbers.
- Output only the numbered list, no other text.
