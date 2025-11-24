# Convert to Conversation Style (Formal)

**Type**: Core dialogue format

**Task**: Transform extracted Q&A pairs into professional 1-on-1 conversation format.

## Input
Extracted Q&A pairs from any Extract/ prompt type.

## Core Principles

**Accuracy First**: Preserve all facts, numbers, technical details. When conversational fluency conflicts with accuracy, choose accuracy.

**Professional Tone**:
- Complete sentences with formal structure
- Minimal contractions (acceptable: "it's", "that's")
- Discourse markers: "Let us examine...", "To clarify...", "As I understand..."
- Active voice, measured pacing
- Technical precision maintained

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

**Minimal patterns**: "To clarify...", "Returning to the question...", "In essence..."

**Full patterns** → See ConversationDynamics.md

## Output Format

**Structure**:
```
1. Q: [professional question]
   A: [professional answer]
   
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
> 1. Q: What does O(log n) time complexity represent?
>    A: It represents logarithmic growth—the runtime increases logarithmically as the input size grows. When you double the input size, the number of operations increases by only one. Binary search demonstrates this characteristic: each comparison eliminates half of the remaining elements.

### Multi-Round

**Before**:
> Q: What's a database index and when should you use it?
> A: A database index is a data structure that improves query performance by providing quick lookup paths. Use for columns in WHERE, JOIN, ORDER BY. Trade-off: faster reads, slower writes, extra storage.

**After**:
> 1. Q: What is a database index and how does it function?
>    A: A database index is a data structure that provides optimized lookup paths to table rows. It functions similarly to a book's index—mapping column values to their physical row locations. This allows the database to locate specific records without scanning the entire table.
>    
>    Q: How does it improve query performance?
>    A: Without an index, a query must perform a full table scan—examining every row sequentially, which is O(n) complexity. With an index, the database traverses a B-tree structure to locate the target rows directly, reducing complexity to O(log n). For a table with one million rows, this means approximately 20 comparisons instead of one million.
>    
>    Q: In what scenarios should we implement an index?
>    A: There are three primary scenarios. First, columns frequently referenced in WHERE clauses. Second, columns used in JOIN conditions. Third, columns specified in ORDER BY clauses. If your application regularly searches or sorts on a particular column, indexing that column will yield significant performance improvements.
>    
>    Q: Are there trade-offs to consider?
>    A: Yes, there are several considerations. First, write operations become slower—every INSERT, UPDATE, or DELETE must also update the index structure. Second, indexes consume additional storage space. Third, excessive indexing can degrade overall performance. The recommended approach is to profile query performance first, then index only those columns that demonstrably cause bottlenecks.

## Context-Specific Variations

### Academic/Research Context
- Emphasize theoretical foundations
- Include citations where appropriate
- Use discipline-specific terminology precisely

### Professional/Business Context
- Focus on practical implications
- Address implementation considerations
- Acknowledge organizational constraints

### Technical Documentation
- Maintain precise technical language
- Include relevant specifications
- Reference standards and best practices
