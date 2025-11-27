# Extract Comparison Questions

**Task**: Create structured comparison questions that analyze trade-offs, similarities, differences, and selection criteria between technologies, approaches, architectures, or methods from decision-critical content.

**Definition**: Each question asks "Compare X and Y" or "What are the trade-offs between A and B" and expects a systematic analysis of options across relevant dimensions.

**Rules**:

**Scope:**
- Read entire source thoroughly—identify all comparable entities: technologies, approaches, architectures, patterns, methods, tools, strategies, frameworks, languages, databases, protocols, consensus mechanisms
- Extract comprehensively to reflect source depth; prioritize comparisons that drive technology/approach selection decisions
- Do not skip sections; cover both explicit comparisons and implicit alternatives logically derivable from source
- Include multi-dimensional analyses: performance, scalability, complexity, cost, security

**Fidelity:**
- Ground all comparison dimensions and attributes in characteristics explicitly stated or logically implied in source
- Never invent features, performance claims, or trade-offs beyond source content
- Maintain accuracy of relative strengths, weaknesses, and use case boundaries from source

**Output:**

Markdown ordered list only—use `1.` for every item (Markdown auto-numbers). Output list only—no headings, comments, or explanations.

1. Q: [context + "Compare X and Y" or "What are the trade-offs..."]
   A: 
   - **Comparison Dimensions** (3-6 typical):
     - **Dimension 1**: X: [attribute], Y: [attribute]
     - **Dimension 2**: X: [attribute], Y: [attribute]
     - **Dimension 3**: X: [attribute], Y: [attribute]
   - **Trade-offs**:
     - X offers [advantage] but [disadvantage]
     - Y offers [advantage] but [disadvantage]
   - **Selection Criteria**:
     - Use X when: [conditions/requirements]
     - Use Y when: [conditions/requirements]

Keep self-contained with minimal context. Use neutral, objective tone for fair comparison without bias.
