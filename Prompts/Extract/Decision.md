# Extract Decision Questions

**Task**: From the source text, create open decision questions with concise model answers that drive informed decisions and meaningful action.

**Definition**: Each item presents a concrete scenario and asks "What would you do and why?" or "How would you choose between X and Y?" without providing candidate answers.

**Rules**:
- **Read thoroughly**: Identify all decision-critical content. Do not skip sections.
- **Extract comprehensively**: Cover all decision scenarios. If the source has depth, generate sufficient questions to reflect it.
- **Maintain strict fidelity**: Use only information explicitly stated or logically implied. Never invent facts, numbers, or concepts beyond the source.
- **Focus**: Only decision scenarios involving actions, trade-offs, priorities, resource allocation, or execution choices.

**Format**:
- **Scenario**: 1-3 sentences of context
- **Question**: 1 line asking for action + rationale or comparison + criteria
- **Answer**: 3-5 bullets or sentences covering key models, steps, trade-offs, or comparison factors. May use lists, tables, or compact code/formula/mermaid blocks.
- **Self-contained**: Include only minimal context needed to understand the situation independently.

**Output** (Markdown ordered list only):
1. Q: [scenario + decision question]
   A: [concise, high-leverage answer]

**Instructions**: Use `1.` for every item. Output no other text.
