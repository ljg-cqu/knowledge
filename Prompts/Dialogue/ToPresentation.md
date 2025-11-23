# Convert to Presentation Style

**Type**: Core dialogue format

**Task**: Transform extracted Q&A pairs into professional presentation format simulating 1-to-many spoken delivery.

**Definition**: Rewrite using structured oral presentation language with professional tone, clear signposting, and authoritative delivery while preserving decision-critical accuracy.

## Input
Extracted Q&A pairs from any Extract/ prompt type.

## Presentation Characteristics

**Language**: Complete sentences, active voice, minimal contractions, precise terminology  
**Markers**: "Let's examine...", "Moving on...", "To recap...", "First...", "This is critical...", "You might ask..."  
**Tone**: Professional, authoritative, confident, accessible  
**Structure**: Hierarchical, formal examples, explicit numbering, logical progression, explicit connectors

## Rules

**Fidelity**: Preserve all decision-critical content, facts, numbers, technical accuracy; no ungrounded additions  
**Transformation**: Spoken presentation language with markers, oral delivery structure, formal rhetorical devices  
**Format**: Question → prompt/introduction; Answer → structured presentation with emphasis cues, numbered/bulleted points  
**Self-contained**: Provide sufficient context, natural setup

## Complexity Adaptation

**LLM determines single vs. multi-section automatically**

**Use Multi-Section (2-5)** when:
- 3+ depth layers requiring structured breakdown
- Content exceeds 250 words
- Clear topic divisions (overview → details → application → summary)
- Progressive building needed

**Use Single Section** when:
- Topic concise, deliverable in one block (<250 words)
- No obvious sectional breaks

**Multi-Section Structure** (adapt to content):
1. **Overview**: High-level introduction, framing
2. **Details**: Core concepts, technical depth
3. **Application**: Implementation guidance
4. **Summary**: Key takeaways, trade-offs, caveats

**Principles**: Clear signposting, one focus per section, explicit transitions, controlled pacing

## Presentation Dynamics

Apply selectively. Balance: 90% content, 10% dynamics.

**Technical Disruptions**: "Technical difficulties aside...", "Before we dropped...", "Let me summarize where we were..."

**Re-engagement** (declining attention): "This is critical...", "Why does this matter?", "I know that was a lot. Let me make this concrete..."

**Context Recovery** (interruptions): "To recap where we were...", "Before the interruption...", "Quick recap: [key point]"

**Audience Questions**: "Excellent question. Let me address that in Q&A...", "Good timing. That connects to what I'm about to cover...", "Hold that thought."

**Audio-Only**: Replace visual references ("as you can see" → "note that"); verbal confirmation ("Are you following?"); shorter chunks; explicit structure ("First...", "Second..."); verbal emphasis (repeat key points, strategic pauses)

→ See ConversationDynamics.md for comprehensive patterns

## Output Format

**Single Section**:
```
1. Q: [presentation-style prompt/question]
   A: [structured presentation delivery]
```

**Multi-Section**:
```
1. Q: [presentation-style prompt/question]
   A: **[Section 1: Overview]**
   [Introduction and framing]
   
   **[Section 2: Details]**
   [Technical depth]
   
   **[Section 3: Summary]**
   [Key takeaways]
```

**Instructions**: Use `1.` for every item (Markdown auto-numbers). Output list only—no headings, comments. Multi-section keeps all sections within same numbered item.

## Examples

### Example 1: Single Section

**Before**:
> Q: A loop runs N times, each iteration taking O(log N). What is the total time complexity?
> A: O(N log N)

**After**:
> 1. Q: Let's analyze a time complexity scenario. We have a loop executing N times, with each iteration performing an operation that takes O(log N). What's our total time complexity?
>    A: Here's how we break this down. First, note that we have N iterations—that's our outer complexity. Second, each individual iteration costs us O(log N). When we multiply these together, we arrive at our total complexity: O(N log N). This is a common pattern in efficient sorting algorithms like mergesort and heapsort. Keep in mind: we're multiplying, not adding, because the logarithmic operation occurs within every single iteration.

### Example 2: Multi-Section

**Before**:
> Q: What are the three key principles of database normalization?
> A: 1) First Normal Form (1NF): Eliminate repeating groups. 2) Second Normal Form (2NF): Remove partial dependencies. 3) Third Normal Form (3NF): Eliminate transitive dependencies.

**After**:
> 1. Q: Let's examine the foundational principles of database normalization. What are the three key forms we need to understand?
>    A: **Overview**
>    Today we'll cover the three normal forms that structure relational database design. These forms provide a systematic approach to organizing data efficiently.
>    
>    **The Three Normal Forms**
>    First, we have First Normal Form—1NF—which eliminates repeating groups in our data. Each field should contain atomic values, not lists or arrays.
>    
>    Moving to Second Normal Form, we're addressing partial dependencies. Each non-key attribute must depend on the entire primary key, not just part of it.
>    
>    Finally, Third Normal Form eliminates transitive dependencies. If A determines B, and B determines C, we don't store the A-to-C relationship directly.
>    
>    **Key Takeaways**
>    To recap: 1NF removes repetition, 2NF ensures full key dependency, 3NF eliminates indirect relationships. Most applications aim for 3NF as standard.
