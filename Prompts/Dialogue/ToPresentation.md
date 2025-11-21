# Convert to Presentation Style

**Type**: Core dialogue format

**Task**: Transform extracted Q&A pairs into professional presentation format that simulates 1-to-many spoken delivery during formal presentations, reports, or slide deck narration.

**Definition**: Rewrite questions and answers using structured oral presentation language with professional tone, clear signposting, and authoritative delivery while preserving decision-critical accuracy.

## Input
Extracted Q&A pairs from any Extract/ prompt type (Cloze, Decision, Creativity, CriticalThinking, Debug, Reflection).

## Presentation Characteristics

**Language**: Complete sentences, declarative statements, minimal contractions, active voice, precise terminology

**Markers**: Opening ("Let's examine..."), Transitions ("Moving on..."), Signposting ("To recap..."), Navigation ("Note that..."), Structure ("First...", "Second..."), Emphasis ("This is critical..."), Engagement ("You might ask...")

**Tone**: Professional, authoritative, confident, accessible, educational

**Clarity**: Structured hierarchy, formal examples ("For instance..."), professional analogies, explicit numbering

**Flow**: Logical progression, explicit connectors, gradual complexity, periodic reinforcement

## Rules

**Fidelity**: Preserve all decision-critical content, facts, numbers, technical accuracy; maintain logical structure; no ungrounded additions

**Transformation**: Spoken presentation language, add markers/signposting, oral delivery structure, formal rhetorical devices, complete sentences

**Format**: Question → prompt/introduction; answer → structured presentation; spoken emphasis cues; numbered/bulleted points

**Self-contained**: Provides sufficient context, natural setup, assumes structured presentation following

## Intelligent Complexity Adaptation

**LLM: Automatically determine single vs. multi-section based on content complexity**

### When to Use Multiple Sections (2-5)

Expand when content exhibits:
- **Depth layers**: 3+ distinct levels requiring structured breakdown
- **Length threshold**: Single presentation would exceed 250 words
- **Natural topic divisions**: Clear section boundaries (overview → details → application → summary)
- **Progressive building**: Audience needs foundation before advanced concepts

### When to Keep Single Section

Use single presentation when:
- Topic concise, deliverable in one coherent block
- Presentation naturally fits in <250 words
- No obvious sectional breaks

### Multi-Section Structure

**Section Progression** (adapt to content):
1. Overview: High-level introduction, framing
2. Detailed Explanation: Core concepts, mechanisms, technical depth
3. Practical Application: How to use, implementation guidance
4. Summary & Caveats: Key takeaways, trade-offs, when not to use

**Section Labels**: Use clear descriptive markers like "Overview", "Technical Details", "Implementation", "Key Takeaways" or numbered "First...", "Second...", "Finally..."

**Key Principles**:
- Clear signposting
- One focus per section
- Explicit transitions
- Professional structure
- Audience orientation
- Controlled pacing

**Section Distribution**: 2 sections (concept + application) | 3 sections (standard complex) | 4 sections (complex + synthesis) | 5 sections (max, rare)

## Presentation Management

**Common Patterns**:
- **Handle disruption**: "Technical difficulties aside...", "Let me resume from..."
- **Check understanding**: "I'm seeing some confusion. Let me clarify...", "Questions before I continue?"
- **Manage time**: "For time's sake, let's focus on...", "We'll skip ahead to..."
- **Re-engage**: "Key point here...", "Pay attention to this part..."
- **Recover context**: "Before the interruption, we were covering...", "To recap where we were..."

## Essential Dynamics for Formal Presentations

Apply selectively (not to every presentation). Balance: 90% content, 10% dynamics.

### Technical Disruptions and Recovery

**Common incidents**: Microphone failure, screen share issues, connection loss, slide freezes

**Recovery**: "Technical difficulties aside...", "Before we dropped, I was covering...", "Let me summarize where we were: [key point]", "Picking up from the third normal form..."

**Example**:
> Let's examine the three normal forms. First Normal Form eliminates repeating groups...
> [Mic feedback]
> Technical issues aside—normalization. Three forms. First: no repeating data in fields...

### Audience Re-engagement

**Detection**: Declining attention, blank stares, side conversations, checking phones

**Re-engagement**: "This is a critical point...", "Why does this matter?", "Consider this scenario...", "I know that was a lot. Let me make this concrete..."

**Example**:
> [After dense technical section]
> I know that was a lot. Let me make this concrete. Imagine you're building an e-commerce checkout...

### Context Recovery After Interruptions

**When needed**: After fire alarms, late arrivals, extended Q&A tangents, technical failures

**Recovery**: "To recap where we were: [one sentence]", "In this section on distributed transactions...", "Before the interruption, we discussed...", "Now let's continue with..."

**Example**:
> [After fire alarm]
> Welcome back. Quick recap: we covered choreography and orchestration for Sagas. Now let's examine the trade-offs.

### Handling Audience Questions/Interruptions

**During formal presentations**: Balance answering with maintaining flow

**Patterns**: "Excellent question. Let me address that in the Q&A...", "Short answer: yes. Now, back to...", "Good timing. That connects to what I'm about to cover...", "Important point. Let's discuss that after..."

**Example**:
> [Mid-presentation question]
> Great question about performance. I'll cover that specifically in section three. Hold that thought.

**For comprehensive patterns** → See ConversationDynamics.md

## Audio-Only Adaptation

**Visual → Verbal**: Replace "as you can see" → "note that", "on this slide" → "at this point"  
**Confirmation**: "Are you following?", "This is critical...", "Let me clarify..."  
**Shorter chunks**: One concept per section, pause between sections, recap frequently  
**Explicit structure**: Number verbally, signal transitions, recap periodically, preview upcoming  
**Verbal emphasis**: Repeat key points, slow for complexity, strategic pauses, emphasize phrasing

## Output Format

**Single Section**:
1. Q: [presentation-style prompt/question]
   A: [structured presentation delivery]

**Multi-Section** (when complexity warrants):
1. Q: [presentation-style prompt/question]
   A: **[Section 1: Overview]**
   [Introduction and framing]
   
   **[Section 2: Details]**
   [Technical depth]
   
   **[Section 3: Application/Summary]**
   [Practical guidance and key takeaways]

## Instructions
- Use `1.` for every item; Markdown auto-numbers
- LLM determines single vs. multi-section automatically based on complexity criteria
- Output list only—no headings, comments, or explanations
- For multi-section: keep all sections within same numbered item
- Use clear section labels and transitions

## Examples

### Example 1: Single Section (Straightforward Topic)

**Before** (Formal Extract):
> Q: A loop runs N times, each iteration taking O(log N). What is the total time complexity?
> A: O(N log N)

**After** (Presentation - Single Section):
> 1. Q: Let's analyze a time complexity scenario. We have a loop executing N times, with each iteration performing an operation that takes O(log N). What's our total time complexity?
>    A: Here's how we break this down. First, note that we have N iterations—that's our outer complexity. Second, each individual iteration costs us O(log N). When we multiply these together, we arrive at our total complexity: O(N log N). This is a common pattern you'll see in efficient sorting algorithms like mergesort and heapsort. Keep in mind: we're multiplying, not adding, because the logarithmic operation occurs within every single iteration.

---

### Example 2: Multi-Section (Moderate Complexity)

**Before** (Formal Extract):
> Q: What are the three key principles of database normalization?
> A: 1) First Normal Form (1NF): Eliminate repeating groups. 2) Second Normal Form (2NF): Remove partial dependencies. 3) Third Normal Form (3NF): Eliminate transitive dependencies.

**After** (Presentation - Multi-Section):
> 1. Q: Let's examine the foundational principles of database normalization. What are the three key forms we need to understand?
>    A: **Overview**
>    Today we'll cover the three normal forms that structure relational database design. These forms provide a systematic approach to organizing data efficiently.
>    
>    **The Three Normal Forms**
>    First, we have First Normal Form—or 1NF—which focuses on eliminating repeating groups in our data. Each field should contain atomic values, not lists or arrays.
>    
>    Moving to Second Normal Form, we're addressing partial dependencies. This ensures each non-key attribute depends on the entire primary key, not just part of it.
>    
>    Finally, Third Normal Form eliminates transitive dependencies—essentially removing indirect relationships between attributes. If A determines B, and B determines C, we don't store the A-to-C relationship directly.
>    
>    **Key Takeaways**
>    To recap: 1NF removes repetition, 2NF ensures full key dependency, and 3NF cuts out the middleman relationships. Most applications aim for 3NF as a standard.

---

### Example 3: Multi-Section (High Complexity)

**Before** (Formal Extract):
> Q: In a microservices architecture, you need to implement distributed transactions across three services. How would you approach this?
> A: Consider the Saga pattern with compensating transactions. Implement either choreography (event-driven) or orchestration (coordinator-based). Key factors: consistency requirements, failure handling, monitoring complexity.

**After** (Presentation - Multi-Section):
> 1. Q: Let's turn to a critical challenge in microservices: implementing distributed transactions across multiple services. How do we approach this complex scenario?
>    A: **The Challenge**
>    In a microservices architecture, we cannot use traditional ACID transactions across service boundaries. Each service manages its own database, creating a fundamental challenge—
>    
>    [Screen share freezes]
>    
>    Apologies for the technical difficulty. Let me continue. The challenge: each service owns its database. We need transactions that span them.
>    
>    **The Solution: Saga Pattern**
>    The recommended approach is the Saga pattern with compensating transactions. This pattern breaks a distributed transaction into a series of local transactions, each with a corresponding compensating action.
>    
>    I'm seeing some confused faces. Let me clarify with an example. Payment succeeds, then inventory check fails. The compensating action? Refund the payment. Each step has an undo.
>    
>    **Implementation Approaches**
>    You have two options. First, choreography—event-driven. Services communicate through events independently. Second, orchestration—a central coordinator manages the flow.
>    
>    [Audience question: "Which one scales better?"]
>    
>    Good question. I'll address that in my recommendation. Hold that thought.
>    
>    **Making the Decision**
>    The key factors: consistency requirements, failure handling visibility, and monitoring complexity. Choreography distributes the burden. Orchestration centralizes it.
>    
>    **Recommendation**
>    To answer the earlier question: choreography scales better. But orchestration offers easier debugging—critical for payment flows. The takeaway: for critical transactions where you need visibility at 2am, orchestration wins despite the centralization trade-off.
>    
>    Questions?
