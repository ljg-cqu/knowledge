# Extract Creativity Questions

Task: From the source text, create **creativity questions** that prompt generation of alternatives, innovative solutions, or novel approaches based on decision-critical concepts.

Definition:
- Each item identifies a concept/problem/method from the text and asks for alternatives, variations, or creative applications.
- Questions prompt divergent thinking: "Generate N alternatives...", "How else could you...", "What variations might work...".
- Answers provide 3-5 concrete, distinct options with brief rationale.

Rules:
- **Read the entire source text thoroughly**: Identify all decision-critical concepts that could benefit from alternative approaches. Do not stop prematurely or skip sections.
- **Extract comprehensively**: Cover all decision-critical concepts where alternatives or innovations would provide value. Generate sufficient questions to reflect the source's depth.
- **Maintain strict fidelity**: Ground all alternatives in principles, constraints, or goals explicitly stated or logically implied in the source. Never invent unrelated concepts or violate source assumptions.
- Focus on generative scenarios: alternative implementations, different approaches, variations, creative applications.
- Question: 1-2 sentences of context + explicit prompt to generate alternatives (specify number: 3-5).
- Answer: List of 3-5 distinct options, each with 1-2 sentence rationale explaining trade-offs or benefits.
- Answers may include brief code snippets, formulas, or diagrams to illustrate alternatives; keep them minimal.
- Make each question self-contained with minimal context needed to generate alternatives without the source text.

Output (Markdown ordered list only):
1. Q: ...  (context + creativity prompt)
   A: ...  (3-5 alternatives with brief rationale)

Instructions:
- Use `1.` for every item; Markdown will auto-number the list.
- Do not output any other text (no headings, comments, or explanations).
