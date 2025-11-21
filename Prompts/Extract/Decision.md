# Extract Decision Questions

Task: From the source text, create **open decision questions** with short model answers that drive deep understanding, informed decisions, and meaningful action.

Definition:
- Each item describes a concrete situation and asks "What would you do and why?" or "How would you choose between X and Y?" (or similar).
- No candidate answer is given in the question.
- Answers are flexible in format but concise.

Rules:
- **Read the entire source text thoroughly**: Identify all decision-critical content. Do not stop prematurely or skip sections.
- **Extract comprehensively**: Cover all decision-critical scenarios without omission. If the source has depth, generate sufficient questions to reflect that depth.
- **Maintain strict fidelity**: Use only information explicitly stated or logically implied in the source text. Never invent facts, numbers, concepts, or ideas that contradict or extend beyond the original material.
- Focus only on decision-critical scenarios: actions, choices between alternatives, trade-offs, priorities, resource allocation, planning, execution choices.
- Scenario: 1-3 short sentences of context.
- Question: 1 line, ask for action + rationale or comparison + selection criteria.
- Answer: 3-5 bullets or 3-5 short sentences covering key model, steps, trade-offs, comparison factors.
- Answers may use short lists, tiny tables, or compact code/formula/mermaid blocks to clarify decisions or trade-offs; keep them minimal.
- Make each question self-contained with only the minimal context needed to understand the situation without the source text.

Output (Markdown ordered list only):
1. Q: ...  (scenario + decision question)
   A: ...  (short, high-leverage answer)

Instructions:
- Use `1.` for every item; Markdown will auto-number the list.
- Do not output any other text (no headings, comments, or explanations).
