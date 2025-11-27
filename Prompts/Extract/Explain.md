# Extract Explanation Questions

**Task**: Create explanation questions that test conceptual understanding of mechanisms, relationships, principles, and implications from decision-critical content.

**Definition**: Each question asks "Explain X", "What is Y", "How does Z work conceptually", or "What are the implications of..." and expects clear conceptual understanding rather than procedural steps or factual recall.

**Rules**:

**Prioritization (80/20):**
- Focus first on decision-critical mechanisms and foundational principles that unlock understanding
- Extract concepts that enable comprehension of the most important 20% of content
- Depth over breadth: thoroughly cover vital concepts rather than superficially covering everything
- Identify concepts where understanding unlocks multiple dependent ideas

**Fidelity:**
- Ground all explanations in concepts, mechanisms, and relationships explicitly stated or logically implied in source
- Never invent concepts, mechanisms, or relationships beyond source content
- Maintain accurate representation of how things work, why they matter, and what they imply

**Focus (MECE Categories):**
1. **Mechanisms & Principles**: How systems/protocols/algorithms work conceptually; fundamental rules/laws/theories governing behavior
2. **Structure & Relationships**: Component interactions, dependencies, influences; definitions with structural rationale
3. **Implications & Significance**: Consequences, impacts, and importance of concepts or decisions

**Format**:

Markdown ordered list only:
1. Q: [context + "Explain..." or "What is..." or "How does... work"]
   A: 
   - **Definition**: [Core concept in 1-2 sentences]
   - **Mechanism**: [How it works conceptually, key components, relationships]
   - **Significance**: [Why it matters, implications, consequences]
   - **Example**: [Concrete example or analogy if helpful]

**Instructions**:
- Output list only—no headings, comments, or explanations
- Focus on conceptual understanding, not procedural execution (that's How.md)
- Distinguish from: Cloze (recall), How (procedures), Why (causation), Compare (comparisons)
- Make self-contained with minimal context; use clear pedagogical language
