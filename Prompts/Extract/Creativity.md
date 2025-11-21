# Extract Creativity Questions

Task: Create **creativity questions** that prompt generation of alternatives, innovative solutions, or novel approaches for decision-critical concepts in the source text.

Scope:
- Each question identifies a concept/problem/method and asks for alternatives, variations, or creative applications.
- Prompt divergent thinking: "Generate N alternatives...", "How else could you...", "What variations might work...".
- Provide 3-5 concrete, distinct options with rationale.

Rules:
- **Read thoroughly**: Read the entire source completely before extracting.
- **Extract comprehensively**: Cover all decision-critical concepts where alternatives provide value. Generate sufficient questions to reflect the source's depth.
- **Maintain strict fidelity**: Ground all alternatives in principles, constraints, or goals explicitly stated or logically implied. Never invent unrelated concepts or violate source assumptions.
- **Focus on generative scenarios**: Alternative implementations, different approaches, variations, creative applications.
- **Format questions**: 1-2 sentences context + explicit prompt to generate alternatives (specify count: 3-5).
- **Format answers**: 3-5 distinct options, each with 1-2 sentence rationale explaining trade-offs or benefits. Include minimal code snippets, formulas, or diagrams if illustrative.
- **Self-contained**: Each question should be answerable without referring to source text.

Output Format:
1. Q: [context + creativity prompt]
   A: [3-5 alternatives with rationale]

Use `1.` for every item; Markdown auto-numbers.
Output only the list—no headings, comments, or explanations.
