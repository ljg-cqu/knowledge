# Extract Linking Words & Discourse Markers for Vocabulary Learning

**Task**: Extract linking words (conjunctions, connectors, discourse markers, transition expressions) that are essential for constructing complex sentences and expressing logical relationships from the source text.

**Definition**: Each entry focuses on one linking word or discourse marker with comprehensive learning information including meaning, usage context, grammatical function, and examples across registers.

**Rules**:

**Coverage:**
- Read entire source thoroughly—identify all linking words that connect clauses, phrases, words, or ideas
- Prioritize: subordinating conjunctions, coordinating conjunctions, correlative pairs, logical connectors, discourse markers, transition phrases
- Extract comprehensively to reflect source richness; apply 80/20 principle (focus on high-impact linking expressions)
- Do not skip sections; cover both grammatical conjunctions and discourse-level connectors

**Fidelity:**
- Ground all information in linking words actually present in source
- Never invent linking words not in source
- Derive meaning from context when source provides it; supplement with standard dictionary definitions

**Focus:**
- **Coordinating conjunctions** (FANBOYS: for, and, nor, but, or, yet, so)
- **Subordinating conjunctions** (because, although, if, when, while, since, etc.)
- **Correlative conjunctions** (either...or, neither...nor, both...and, not only...but also)
- **Logical connectors** (cause/effect, contrast, addition, sequence)
- **Discourse markers** (organize discourse, signal shifts, manage turns)
- **Transition phrases** (between topics, ideas, paragraphs)
- **Cohesive devices** (reference, substitution markers)

**Format:**
- **Linking Word**: [word/phrase] (type: coordinating/subordinating/correlative/connector/discourse marker)
- **Meaning**: Collins Dictionary style definition(s)
  - *Explain grammatical or discourse function clearly*
  - *Describe logical relationship created*
  - *Include clause patterns and register information*
- **Synonyms**: 3-5 alternative linking words with same function
- **Antonyms**: 2-4 linking words expressing opposite logical relationship (if applicable)
- **When to Use**: Context, situations, or registers where this linking word is appropriate
- **When NOT to Use**: Contexts where this linking word would be inappropriate or create grammatical/logical errors
- **Common Patterns**: Grammatical structures, punctuation rules, sentence positions
- **Root Analysis**: Break down word components (if applicable)
- **Etymology**: Language origin and historical development (brief)
- **Examples [Casual]**: 2 natural example sentences in informal register
- **Examples [Formal]**: 2 natural example sentences in formal/academic register

**Output Format**:

Markdown ordered list only:
1. **Linking Word**: among other things (type: discourse marker / transition phrase)
   **Meaning**: 
   - Functions as a discourse marker indicating that the mentioned item(s) are part of a larger, non-exhaustive list
   - *Function*: signals non-exhaustive enumeration; manages information flow by explicitly indicating selective presentation
   
   **Synonyms**: inter alia, additionally, also, furthermore, including, to name a few
   
   **Antonyms**: exclusively, specifically, only, solely (signals exhaustive rather than selective enumeration)
   
   **When to Use**: Use when presenting selective examples from a larger set; appropriate in both formal and informal contexts; common in academic writing for hedging and in casual conversation for brevity; helps manage scope of statements
   
   **When NOT to Use**: Avoid when complete enumeration is required; inappropriate in legal or technical writing requiring precision; can sound vague when overused; not appropriate when the list should be comprehensive
   
   **Common Patterns**: 
   - [Clause structure]: [List item 1], [item 2], and [item 3], among other things, [continuing clause]
   - [Position]: typically follows the list it references; can also begin a new clause
   - [Punctuation]: usually set off by commas when mid-sentence; can follow a comma when ending a list
   - [Common errors to avoid]: overuse leading to vagueness; using when precision is required; unclear antecedent for "things"
   
   **Root Analysis**: among (within a group) + other (additional) + things (unspecified items)
   
   **Etymology**: Middle English phrase combining "among" (from Old English "ongemang") with "other things"; evolved from literal spatial meaning to abstract discourse function
   
   **Examples [Casual]**: 
   - I need to call my mom, finish my homework, and clean my room, among other things, before I can go out tonight.
   - The restaurant has great food, friendly staff, and reasonable prices, among other things.
   
   **Examples [Formal]**: 
   - The policy addresses environmental sustainability, economic viability, and social equity, among other things.
   - Factors considered in the analysis included market trends, consumer behavior, and regulatory frameworks, among other things.

1. **Linking Word**: among others (type: discourse marker / connector)
   **Meaning**: 
   - Functions as a discourse marker indicating that additional unmentioned entities exist beyond those listed
   - *Function*: signals non-exhaustive list; creates logical connection between stated examples and implied larger set
   
   **Synonyms**: inter alia, including, and more, et cetera, to name a few, for example
   
   **Antonyms**: only, exclusively, specifically, namely (signals exhaustive identification)
   
   **When to Use**: Use after naming specific entities to indicate more exist; appropriate in all registers from casual to formal; common in academic citations, business reports, and casual enumeration; helps maintain brevity while acknowledging completeness
   
   **When NOT to Use**: Avoid when all members must be named; inappropriate in contexts requiring full accountability or attribution; less appropriate in legal documents; can weaken arguments if overused
   
   **Common Patterns**: 
   - [Clause structure]: [Entity 1], [Entity 2], and [Entity 3], among others, [verb phrase]
   - [Position]: typically follows a noun phrase listing examples; occasionally begins a new clause
   - [Punctuation]: usually set off by commas; sometimes follows a period as sentence fragment for emphasis
   - [Common errors to avoid]: unclear antecedent; using with only one example (needs at least two for "among"); confusing with "between others"
   
   **Root Analysis**: among (in the company of) + others (additional members/entities)
   
   **Etymology**: Phrase combining "among" (Old English "ongemang") with "others"; evolved from spatial meaning to discourse function marking non-exhaustive enumeration
   
   **Examples [Casual]**: 
   - I invited Sarah, Mike, and Jessica, among others, so there should be a good crowd.
   - The band played hits like "Yesterday," "Hey Jude," and "Let It Be," among others.
   
   **Examples [Formal]**: 
   - Contributors to the research included Harvard University, MIT, and Stanford, among others.
   - The committee comprises representatives from government agencies, nonprofit organizations, and private corporations, among others.

**Instructions**:
- Use `1.` for every item; Markdown auto-numbers
- Output list only—no headings, comments, or explanations
- Focus on linking words that are essential for complex sentences and coherent communication
- Prioritize linking words with learning value (subordinating conjunctions, formal connectors, subtle distinctions)
- Clearly indicate grammatical patterns, punctuation rules, and register restrictions
- Distinguish between grammatical conjunctions (sentence-level) and discourse markers (text-level)
