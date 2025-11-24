# Convert to Discussion Style (Formal)

**Purpose**: Transform Q&A pairs into professional multi-party discussion (3+ speakers) with formal turn-taking, idea building, and collaborative analysis.

**Input**: Extracted Q&A pairs from any Extract/ prompt type.

## Essential Rules (Non-Negotiable)

### 1. Accuracy First
- **Preserve**: All facts, numbers, technical details, decision-critical content
- **Conflict Resolution**: When fluency conflicts with accuracy, always preserve accuracy
- **No Additions**: Zero ungrounded information

### 2. Discussion Structure
- **Speakers**: 2-4 participants with balanced contributions
- **Turn-Taking**: Structured, professional exchanges
- **Content Flow**: Q becomes opener; A distributed across collaborative dialogue
- **Context**: Self-contained—establish context upfront, assume no shared knowledge

### 3. Complexity Adaptation
**Decision Rule**: Word count + topic complexity determines phases

| Criteria | Approach | Implementation |
|----------|----------|----------------|
| <200 words, single concept | **Single Phase** | One continuous exchange, no breaks |
| 200+ words OR 3+ depth layers OR topic shifts | **Multi-Phase** | 2-5 phases with formal transitions |

**Multi-Phase Pattern** (apply flexibly):
- Common progression: Frame → Analysis → Application → Trade-offs
- Transitions: "Let us examine...", "Regarding...", "In the context of..."
- One subtopic per phase

## Style Guidelines (Apply Judiciously)

### Language Formality
- **Tone**: Professional, measured, thoughtful
- **Sentences**: Complete, formal phrasing
- **Contractions**: Minimal (acceptable: "that's", "it's")
- **Markers**: "Let us examine", "Indeed", "As I understand"

### Discussion Dynamics
Use selectively to enhance natural flow:
- **Agreement**: "Indeed", "Building on that point..."
- **Clarification**: "To clarify...", "From another perspective..."
- **Transition**: "Let us refocus on...", "What are your thoughts?"

## Output Format

### Structure Template
```
1. Q: [professional discussion opener]
   A: **Speaker A:** [turn]
   
   **Speaker B:** [turn]
   
   [Multi-phase only: formal transition]
   
   **A:** [turn]
```

### Technical Requirements
- **Numbering**: Use `1.` for each item (Markdown auto-numbers)
- **Labels**: **A:** / **B:** / **C:** or **Moderator:** / **Expert:** / **Panelist 1:**
- **Phases**: Keep within same numbered item, separate with blank lines
- **Output**: List only—no meta-commentary or headings

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
