# Extract Debug Cards

Task: From the source text, create **debug cards** that test detection and correction of errors that affect deep understanding, informed decisions, and meaningful action.

Definition:
- Each card presents a flawed statement/plan/code/decision from the text.
- The answer identifies the error and provides the corrected version.

Rules:
- **Read the entire source text thoroughly**: Process word-by-word, line-by-line to identify all decision-critical content. Do not stop prematurely or skip sections.
- **Extract comprehensively**: Cover all decision-critical aspects; generate sufficient cards to reflect the source's depth.
- **Maintain strict fidelity**: Use only information explicitly stated or logically implied in the source text. Never invent facts, numbers, concepts, or corrections that contradict the original content.
- Use only realistic, plausible mistakes (not trivial typos).
- Errors must be decision-critical: they would change understanding, risk, or action.
- Question: Include the flawed content and ask "What is wrong and how to fix it?" (or similar).
- Answer: Briefly (a) identify the issue, (b) explain why it matters, (c) provide the corrected version.
- Questions and answers may include code snippets, formulas, or diagrams to illustrate errors and corrections. Keep them minimal.
- Include just enough flawed content so the card is self-contained and understandable without the source text.

Output (Markdown ordered list only):
1. Q: ... (flawed content + debug question)
   A: ... (issue + explanation + corrected form)
- Use `1.` for every item; Markdown will auto-number.
- Output only the list—no headings, comments, or explanations.
