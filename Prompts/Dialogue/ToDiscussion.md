# Convert to Discussion Style

**Purpose**: Transform Q&A pairs into multi-party discussion (3+ speakers) with conversational turn-taking, idea building, and collaborative problem-solving.

**Input**: Extracted Q&A pairs from any Extract/ prompt type.

## Core Rules

**Fidelity**: Preserve all decision-critical content, facts, numbers, technical accuracy; no ungrounded additions

**Format**: 
- 2-4 speakers with balanced contributions
- Conversational language with natural turn-taking patterns
- Q becomes discussion opener; A distributed across collaborative exchange
- Self-contained: establish context in opening, no assumed shared knowledge

**Dynamics** (apply selectively):
- Building/agreeing: "Exactly", "Building on that..."
- Contrasting/clarifying: "On the other hand...", "So you're saying..."
- Managing: "Let's refocus on...", "What do others think?"

## Complexity Adaptation

**Single Phase** (<200 words, straightforward topic):
- One continuous exchange, no phase breaks
- Topic resolvable in direct dialogue

**Multi-Phase** (200+ words, 3+ depth layers, natural topic shifts):
- 2-5 phases with natural transitions (e.g., "Let's dig into...", "For our use case:")
- Common progression: Frame → Deep dive → Application → Trade-offs
- Concise turns, one topic per phase, distributed speaking

## Output Format

**Structure**:
```
1. Q: [discussion opener]
   A: **Speaker A:** [turn]
   
   **Speaker B:** [turn]
   
   [For multi-phase: natural transition like "Let's dig into..."]
   
   **A:** [turn]
```

**Guidelines**:
- Use `1.` for every item; Markdown auto-numbers
- Speaker labels: **A:** / **B:** / **C:** or **Engineer:** / **PM:** / **Designer:**
- Multi-phase: keep all phases within same numbered item, separate with blank lines
- Output list only—no headings or meta-commentary

## Examples

### Single Phase Example

**Before**: Q: A loop runs N times, each iteration taking O(log N). What is the total time complexity? A: O(N log N)

**After**:
> 1. Q: Loop runs N times, each iteration does binary search O(log N). Total complexity?
>    A: **A:** N iterations, each costing log N...
>    
>    **B:** Multiply them. N times log N.
>    
>    **A:** Right, O(N log N). Like mergesort—same pattern.
>    
>    **B:** Got it. Better than O(N²), worse than O(N).

### Multi-Phase Example

**Before**: Q: What are the three key principles of database normalization? A: 1NF: Eliminate repeating groups. 2NF: Remove partial dependencies. 3NF: Eliminate transitive dependencies.

**After**:
> 1. Q: What are the key normalization principles?
>    A: **A:** Three forms. 1NF—no repeating groups.
>    
>    **B:** So split multiple phone numbers?
>    
>    **A:** Exactly.
>    
>    **Digging deeper:**
>    
>    **A:** 2NF—every non-key field depends on the whole primary key. 3NF—remove transitive dependencies.
>    
>    **B:** So if A determines B, and B determines C, don't store A→C?
>    
>    **A:** Correct. Cut out the middleman.
>    
>    **For our order system:**
>    
>    **B:** Need all three?
>    
>    **A:** Probably. Let's map it out and see where we violate them.
