# Convert to Conversation Style

**Type**: Core dialogue format

**Task**: Transform extracted Q&A pairs into casual 1-on-1 conversation format.

## Input
Extracted Q&A pairs from any Extract/ prompt type.

## Core Principles

**Accuracy First**: Preserve all facts, numbers, technical details. When conversational fluency conflicts with accuracy, choose accuracy.

**Conversational Tone**:
- Contractions: "Here's", "gonna", "that's"
- Oral markers: "So...", "Well...", "Yep"
- Short sentences, fragments OK
- Active voice, natural rhythm

**Self-Contained**: Every exchange includes context. No assumed prior knowledge.

## Format Selection

**Auto-detect**: LLM determines single vs. multi-round based on content complexity.

### Single Round (Default)
Use when:
- Answer ≤150 words
- 1-2 key points
- No natural follow-ups

### Multi-Round (2-5 exchanges)
Use when:
- Answer >150 words OR 3+ depth layers
- Natural follow-ups exist
- Incremental understanding needed

**Progression Pattern**:
1. **Foundation**: Core concept
2. **Mechanism**: How it works
3. **Application**: Usage, examples
4. **Nuance**: Edge cases, trade-offs

**Guidelines**: One focus per round. No filler. Each round self-contained.

## Conversational Dynamics (Use Sparingly)

Apply only when it adds clarity. Aim for 80% content, 20% dynamics max.

**Minimal patterns**: "Let me rephrase...", "Back to...", "So basically..."

**Full patterns** → See ConversationDynamics.md

## Output Format

**Structure**:
```
1. Q: [conversational question]
   A: [conversational answer]
   
   Q: [follow-up, if multi-round]
   A: [next layer]
```

**Rules**:
- Use `1.` for every Q&A pair (Markdown auto-numbers)
- Multi-round exchanges stay within same numbered item
- Output conversation list only—no meta-commentary

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
