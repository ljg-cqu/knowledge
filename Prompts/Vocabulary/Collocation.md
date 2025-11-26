# Extract Collocations for Vocabulary Learning

**Task**: Extract collocations (natural word partnerships and combinations) that are essential for fluent, native-like expression from the source text.

**Definition**: Each entry focuses on one collocation with comprehensive learning information including meaning, usage context, alternative forms, strength (weak/medium/strong), and examples across registers.

**Rules**:

**Coverage:**
- Read entire source thoroughly—identify all collocations that represent natural word partnerships
- Prioritize: verb+noun, adjective+noun, adverb+adjective, verb+adverb, prepositional collocations
- Extract comprehensively to reflect source richness; apply 80/20 principle (focus on high-frequency and domain-specific collocations)
- Do not skip sections; cover both transparent and opaque collocations

**Fidelity:**
- Ground all information in collocations actually present in source
- Never invent collocations not in source
- Derive meaning from context when source provides it; supplement with standard dictionary definitions

**Focus:**
- Verb + noun collocations (make a decision, take a break, do homework)
- Adjective + noun collocations (strong opinion, heavy traffic, bright future)
- Adverb + adjective collocations (highly effective, deeply concerned, utterly exhausted)
- Verb + adverb collocations (argue strongly, apologize profusely, examine closely)
- Noun + verb collocations (prices rise, rain falls, heart beats)
- Noun + noun collocations (round of applause, sense of humor, word of mouth)
- Verb + preposition + noun collocations (rely on intuition, result in failure)

**Format:**
- **Collocation**: [complete word partnership] (type: V+N/Adj+N/Adv+Adj/N+V/etc.)
- **Meaning**: Collins Dictionary style definition(s)
  - *Explain the combined meaning clearly*
  - *Note if meaning is transparent or requires cultural knowledge*
  - *Include collocation strength: weak/medium/strong*
- **Synonyms**: 3-5 alternative collocations or expressions with similar meaning
- **Antonyms**: 2-4 collocations with opposite meaning (if applicable)
- **When to Use**: Context, situations, or registers where this collocation is appropriate
- **When NOT to Use**: Contexts where this collocation would sound unnatural or be incorrect
- **Common Variations**: Alternative forms or related collocations
- **Why This Partnership**: Brief explanation of why these words naturally combine
- **Root Analysis**: Etymology of key components (if relevant)
- **Examples [Casual]**: 2 natural example sentences in informal register
- **Examples [Formal]**: 2 natural example sentences in formal/academic register

**Output Format**:

Markdown ordered list only:
1. **Collocation**: [word partnership] (type: V+N/Adj+N/Adv+Adj/etc.)
   **Meaning**: 
   - [Collins-style definition]
   - *Collocation strength*: weak/medium/strong (how fixed the partnership is)
   
   **Synonyms**: [alternative collocation1], [alternative collocation2], [single word alternative]...
   
   **Antonyms**: [opposite collocation1], [collocation2]... (if applicable)
   
   **When to Use**: [Context description - domains, situations, register levels]
   
   **When NOT to Use**: [Inappropriate contexts - unnatural combinations, register mismatches]
   
   **Common Variations**: 
   - [variation 1]
   - [variation 2]
   - [related collocation]
   
   **Why This Partnership**: [Brief explanation - semantic compatibility, conventional usage, idiomatic reasons]
   
   **Root Analysis**: [key components and origins] (if relevant)
   
   **Examples [Casual]**: 
   - [Natural conversational example 1]
   - [Natural conversational example 2]
   
   **Examples [Formal]**: 
   - [Academic/professional example 1]
   - [Academic/professional example 2]

**Instructions**:
- Use `1.` for every item; Markdown auto-numbers
- Output list only—no headings, comments, or explanations
- Focus on collocations that are essential for natural, fluent expression
- Prioritize collocations with learning value (strong/fixed partnerships, commonly broken by learners)
- Distinguish between collocations (natural partnerships) and free combinations
- Note collocation strength: strong (very fixed), medium (preferred), weak (one of several options)
