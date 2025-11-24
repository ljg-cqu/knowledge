# Convert to Discussion Style (Formal)

**Purpose**: Transform Q&A pairs into professional multi-party discussion (3+ speakers) with formal turn-taking, idea building, and collaborative analysis.

**Input**: Extracted Q&A pairs from any Extract/ prompt type.

## Core Rules

**Fidelity**: Preserve all decision-critical content, facts, numbers, technical accuracy; no ungrounded additions

**Conflict Resolution**: When fluency enhancements conflict with factual accuracy, always preserve accuracy

**Format**: 
- 2-4 speakers with balanced contributions
- Professional conversational language with structured turn-taking
- Q becomes discussion opener; A distributed across collaborative exchange
- Self-contained: establish context in opening, no assumed shared knowledge

**Language Style**:
- Minimal contractions (acceptable: "that's", "it's"; avoid: "we're", "can't")
- Professional markers ("Let us examine", "As I understand", "Indeed")
- Complete sentences with formal phrasing
- Measured, thoughtful responses

**Dynamics** (apply selectively):
- Building/agreeing: "Indeed", "Building on that point...", "Additionally..."
- Contrasting/clarifying: "However, consider...", "To clarify...", "From another perspective..."
- Managing: "Let us refocus on...", "What are your thoughts?", "Perhaps we should..."

## Complexity Adaptation

**Single Phase** (<200 words, straightforward topic):
- One continuous exchange, no phase breaks
- Topic resolvable in structured dialogue

**Multi-Phase** (200+ words, 3+ depth layers, natural topic shifts):
- 2-5 phases with formal transitions (e.g., "Let us examine...", "Regarding...", "In the context of...")
- Common progression: Frame → Analysis → Application → Trade-offs
- Thoughtful turns, one topic per phase, distributed speaking

## Output Format

**Structure**:
```
1. Q: [professional discussion opener]
   A: **Speaker A:** [turn]
   
   **Speaker B:** [turn]
   
   [For multi-phase: formal transition like "Let us examine..."]
   
   **A:** [turn]
```

**Guidelines**:
- Use `1.` for every item; Markdown auto-numbers
- Speaker labels: **A:** / **B:** / **C:** or **Moderator:** / **Panelist 1:** / **Expert:**
- Multi-phase: keep all phases within same numbered item, separate with blank lines
- Output list only—no headings or meta-commentary

## Examples

### Single Phase Example

**Before**: Q: A loop runs N times, each iteration taking O(log N). What is the total time complexity? A: O(N log N)

**After**:
> 1. Q: Consider a loop that executes N times, where each iteration performs an operation with O(log N) complexity. What is the resulting time complexity?
>    A: **A:** We have N iterations, with each iteration incurring a cost of log N.
>    
>    **B:** The total complexity is the product: N multiplied by log N.
>    
>    **A:** Correct. O(N log N). This pattern appears in efficient sorting algorithms such as mergesort.
>    
>    **B:** Indeed. It represents a middle ground—more efficient than O(N²), though less than linear O(N).

### Multi-Phase Example

**Before**: Q: What are the three key principles of database normalization? A: 1NF: Eliminate repeating groups. 2NF: Remove partial dependencies. 3NF: Eliminate transitive dependencies.

**After**:
> 1. Q: What are the fundamental principles of database normalization that we should understand?
>    A: **A:** There are three primary normal forms. First Normal Form, or 1NF, requires the elimination of repeating groups.
>    
>    **B:** To clarify, if an entity contains multiple values for an attribute—such as multiple phone numbers—we must decompose this into separate records?
>    
>    **A:** Precisely.
>    
>    **Examining the remaining forms:**
>    
>    **A:** Second Normal Form addresses partial dependencies—each non-key attribute must depend on the entire primary key. Third Normal Form eliminates transitive dependencies.
>    
>    **B:** Regarding transitive dependencies—if attribute A determines B, and B determines C, we should not maintain a direct A-to-C relationship?
>    
>    **A:** That is correct. We eliminate the intermediate relationship.
>    
>    **In the context of our order management system:**
>    
>    **B:** Should we implement all three normal forms?
>    
>    **A:** It would be advisable. Let us map our current schema and identify where we may be violating these principles.
