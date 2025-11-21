# Extract Cloze Cards

**Task**: From the source text, create cloze cards that are decision-critical.

**Definition**: Each card covers one fact, list, threshold, or short definition with a fixed, context-independent answer.

**Rules**:
- **Read completely**: Process the entire source to identify all decision-critical content.
- **Extract comprehensively**: Generate sufficient cards to reflect source depth.
- **Maintain fidelity**: Use only information explicitly stated or logically implied. Never invent content.
- Use 1-3 blanks `___` for facts/terms, or "List the N ..." for sequences.
- No options (MCQ or matching).
- Focus on precise facts, numbers, terms, or sequences requiring accurate recall.
- Include formulas or code fragments when they are the recall target.
- Make questions self-contained; add context only when necessary.

**Output format**:
1. Q: ... (question with blanks or list prompt)  
   A: ... (exact answer, concise and complete)

**Instructions**:
- Use `1.` for every item; Markdown auto-numbers.
- Output only the numbered list, no other text.
