# Convert to Conversation Style

**Type**: Core dialogue format

**Task**: Transform extracted Q&A pairs into casual 1-on-1 conversation format.

## Input
Extracted Q&A pairs from any Extract/ prompt type.

## Core Rules

**Language**: Contractions ("Here's", "gonna"), oral markers ("So...", "Well..."), short sentences, fragments

**Fidelity**: Preserve all critical facts, numbers, technical accuracy; no ungrounded additions

**Transformation**: Formal → conversational; written → spoken; active voice; natural rhythm

**Self-contained**: Include context naturally; no assumed prior knowledge

## Complexity Adaptation

**LLM determines single vs. multi-round automatically**

### Multiple Rounds (2-5) When:
- 3+ depth layers (concept → mechanism → usage → edge cases)
- Single answer exceeds 150 words
- Natural follow-ups exist
- Understanding needs incremental steps

### Single Round When:
- 1-2 key points
- Answer fits <150 words
- No obvious follow-ups

### Round Progression
1. Foundation: Core concept
2. Mechanism: How it works
3. Practice: Usage, examples
4. Nuance: Edge cases, trade-offs

**Principles**: One focus per round; eliminate filler; leave hooks; self-contained

**Pacing**: 2 (simple) | 3 (standard) | 4 (complex) | 5 (max, rare)

## Dynamics (Optional)

Apply selectively: 80% content, 20% dynamics.

**Patterns**: Clarify confusion ("Let me rephrase..."), recover interruptions ("Back. Where were we?"), rebuild context ("To recap...")

**For detailed patterns** → See ConversationDynamics.md

## Output Format

**Single Round**:
```
1. Q: [conversational question]
   A: [conversational answer]
```

**Multi-Round**:
```
1. Q: [initial question]
   A: [foundation answer with hook]
   
   Q: [natural follow-up]
   A: [deeper detail]
   
   Q: [edge case/application]
   A: [practical answer]
```

**Instructions**:
- Use `1.` for every item (Markdown auto-numbers)
- LLM determines single vs. multi-round automatically
- Output list only—no headings or explanations
- Keep multi-round exchanges within same numbered item

## Examples

### Single Round

**Before**:
> Q: What is time complexity O(log n)?
> A: Logarithmic time complexity means the algorithm's runtime grows logarithmically with input size. Common in binary search algorithms.

**After**:
> 1. Q: What's O(log n) mean?
>    A: Runtime grows super slowly as input grows. Double your data? Only one extra step. It's what you get with binary search—chop the problem in half each time.

### Multi-Round

**Before**:
> Q: What's a database index and when should you use it?
> A: A database index is a data structure that improves query performance by providing quick lookup paths. Use for columns in WHERE, JOIN, ORDER BY. Trade-off: faster reads, slower writes, extra storage.

**After**:
> 1. Q: What's a database index?
>    A: Fast lookup table. Maps column values to row locations. Like a book index—jump straight to what you need instead of scanning every page.
>    
>    Q: How's it actually make things faster?
>    A: Query without index? Scans every row. Query with index? Checks the index tree, finds row location, jumps directly. O(log n) vs O(n).
>    
>    Q: When should I add one?
>    A: Three scenarios. One: column in WHERE clauses frequently. Two: JOIN conditions. Three: ORDER BY columns. If you're searching or sorting on it, index it.
>    
>    Q: Any downsides?
>    A: Yep. Writes get slower—index needs updating on INSERT/UPDATE. Uses storage. Don't over-index. Profile first, optimize what's actually slow.
