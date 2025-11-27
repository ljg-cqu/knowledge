# Extract Multi-Word Expressions for Vocabulary Learning

**Task**: Extract multi-word expressions (collocations, idioms, phrases, fixed expressions) that are essential for fluent, native-like communication from the source text about **Wallet**.

**Definition**: Each entry focuses on one multi-word expression with comprehensive learning information including meaning, usage context, fixedness level, and examples across registers.

**Rules**:

**Coverage:**
- Read entire source thoroughly—identify all multi-word expressions that represent natural word partnerships or carry special meaning
- Prioritize: collocations, idiomatic expressions, fixed phrases, binomials, phrasal constructions, domain-specific multi-word terms
- Extract comprehensively to reflect source richness; apply 80/20 principle (focus on high-frequency and culturally significant expressions)
- Do not skip sections; cover both transparent collocations and opaque idioms

**Fidelity:**
- Ground all information in expressions actually present in source
- Never invent expressions not in source
- Derive meaning from context when source provides it; supplement with standard dictionary definitions

**Focus:**
- **Collocations (transparent meaning)**:
  - Verb + noun (make a decision, take a break, do homework)
  - Adjective + noun (strong opinion, heavy traffic, bright future)
  - Adverb + adjective (highly effective, deeply concerned, utterly exhausted)
  - Verb + adverb (argue strongly, apologize profusely, examine closely)
  - Noun + verb (prices rise, rain falls, heart beats)
  - Noun + noun (round of applause, sense of humor, word of mouth)
  - Verb + preposition + noun (rely on intuition, result in failure)
- **Idioms & Fixed Phrases (non-literal meaning)**:
  - Idiomatic expressions with figurative meaning
  - Fixed phrases and binomials (salt and pepper, pros and cons)
  - Conversational formulae and discourse markers
  - Culturally-bound expressions

**Format:**
- **Expression**: [complete multi-word expression] (type: collocation/idiom/fixed phrase)
- **Meaning**: Collins Dictionary style definition(s)
  - *Explain the combined meaning clearly*
  - *For collocations: note transparency and partnership strength*
  - *For idioms: explain both literal and figurative meaning*
  - *Include register information (formal/informal/neutral)*
- **Synonyms**: 3-5 alternative expressions or single-word equivalents
- **Antonyms**: 2-4 expressions with opposite meaning (if applicable)
- **When to Use**: Context, situations, or registers where this expression is appropriate
- **When NOT to Use**: Contexts where this expression would sound unnatural, be incorrect, or be misunderstood
- **Common Variations**: Alternative forms or related expressions
- **Fixedness Level**: weak/medium/strong (how fixed the word partnership is)
- **Why This Partnership**: Brief explanation of why these words combine naturally (for collocations) or origin story (for idioms)
- **Root Analysis**: Etymology of key components (if relevant)
- **Examples [Casual]**: 2 natural example sentences in informal register
- **Examples [Formal]**: 2 natural example sentences in formal/academic register (or note if restricted)

**Output Format**:

Markdown ordered list only:
1. **Expression**: [complete multi-word expression] (type: collocation/idiom/fixed phrase)
   **Meaning**: 
   - [Collins-style definition]
   - *For idioms*: Literal meaning vs. Figurative/Idiomatic meaning
   - *Fixedness*: weak/medium/strong (how fixed the partnership is)
   
   **Synonyms**: [alternative expression1], [expression2], [single word equivalent]...
   
   **Antonyms**: [opposite expression1], [expression2]... (if applicable)
   
   **When to Use**: [Context description - domains, situations, register levels, cultural contexts]
   
   **When NOT to Use**: [Inappropriate contexts - unnatural combinations, wrong register, cultural misunderstandings, commonly broken by learners]
   
   **Common Variations**: 
   - [variation 1]
   - [variation 2]
   - [related expression]
   
   **Why This Partnership**: 
   - *For collocations*: [semantic compatibility, conventional usage, frequency of co-occurrence]
   - *For idioms*: [origin story, historical/cultural background, first known use]
   
   **Root Analysis**: [key components and origins] (if relevant)
   
   **Examples [Casual]**: 
   - [Natural conversational example 1]
   - [Natural conversational example 2]
   
   **Examples [Formal]**: 
   - [Academic/professional example 1] (or *"Typically informal; avoid in formal contexts"*)
   - [Academic/professional example 2]

**Instructions**:
- Use `1.` for every item; Markdown auto-numbers
- Output list only—no headings, comments, or explanations
- Focus on expressions that are essential for natural, fluent communication about **Wallet**
- Prioritize expressions with learning value (strong/fixed partnerships, idiomatic meanings, culturally significant, commonly misused)
- Distinguish clearly between transparent collocations and non-literal idioms
- Note fixedness level: strong (very fixed), medium (preferred), weak (one of several options)
- For idioms, clearly distinguish literal from figurative meaning to avoid confusion
- For expressions that are register-specific, clearly note restrictions
