# Convert to Discussion Style

**Task**: Transform extracted Q&A pairs into multi-party discussion format that simulates team meetings, collaborative work sessions, and group problem-solving with turn-taking, building on ideas, and interactive exploration.

**Definition**: Rewrite questions and answers as discussion flow between participants (3+ people), featuring conversational exchange, idea building, and collaborative problem-solving while preserving decision-critical accuracy.

## Input
Extracted Q&A pairs from any Extract/ prompt type (Cloze, Decision, Creativity, CriticalThinking, Debug, Reflection).

## Discussion Characteristics

**Language Style**:
- Conversational but focused
- Mixing complete sentences and natural speech
- Turn-taking between speakers
- Selective contractions for naturalness
- Active listening cues

**Turn-Taking Markers**:
- **Building**: "Building on that...", "To add to what you said...", "Expanding on that point..."
- **Agreeing**: "Exactly.", "Right.", "That's a good point.", "I see what you mean."
- **Contrasting**: "On the other hand...", "Another angle...", "What if we consider...", "But..."
- **Clarifying**: "So you're saying...", "Just to make sure I understand...", "Can you elaborate on..."
- **Questioning**: "What about...?", "Have we considered...?", "How would that work with...?"
- **Synthesizing**: "So if we put this together...", "Connecting these ideas...", "What I'm hearing is..."

**Interaction Patterns**:
- Question → Response → Follow-up
- Idea → Build → Refine
- Challenge → Clarification → Resolution
- Multiple perspectives on same point
- Natural interruptions and asides

**Tone**:
- Collaborative and exploratory
- Respectful but direct
- Engaged and thinking aloud
- Professional but conversational
- Problem-solving focus

**Clarity Techniques**:
- Ideas developed through dialogue
- Analogies introduced and refined by participants
- Examples suggested and discussed
- Group thinking process visible
- Consensus building evident

**Natural Flow**:
- Not perfectly linear—ideas circle back
- Side discussions briefly explored
- Return to main thread with signposts
- Build complexity through exchange
- Summarize periodically to align

## Rules

**Fidelity**:
- **Preserve all decision-critical content** from the original Q&A
- Never change facts, numbers, or technical accuracy
- Maintain logical structure through dialogue exchange
- Don't add ungrounded information

**Transformation**:
- Convert into multi-turn dialogue (2-4 speakers typical)
- Show idea development through exchange
- Include natural discussion dynamics
- Use speaker labels (A:, B:, C:) or roles (Engineer:, PM:, etc.)
- Balance contributions—avoid monologue

**Format**:
- Question becomes discussion opener
- Answer distributed across multiple turns
- Each turn contributes to complete understanding
- Show thinking process, not just conclusions
- May include brief asides or clarifications

**Self-contained**:
- Each dialogue provides context naturally
- Establish scenario through opening exchange
- Don't assume shared context beyond what's stated

## Audio-Only Adaptation

When adapting for audio-only scenarios (conference calls, audio meetings, podcasts):

**Remove Visual References**:
- Never use "look at this", "as shown", "here", "as you can see"
- Replace with verbal descriptions: "imagine...", "consider...", "think about..."

**Add Confirmation Markers**:
- Check understanding: "Does that make sense?", "Are we aligned?", "Everyone following?"
- Acknowledge: "Got it.", "Okay.", "Right.", "Agreed."
- Request confirmation: "Are we on the same page?", "Make sense to everyone?"

**Break Into Shorter Chunks**:
- Shorter explanations to prevent audio fatigue
- Pause for acknowledgment between concepts
- One main idea per speaking turn
- More frequent turn-taking to maintain engagement

**Use Explicit Structure**:
- Number items verbally: "First... Second... Third..."
- Signal transitions: "Now let's turn to...", "Moving on to..."
- Recap periodically: "So to recap where we are...", "Just to summarize what we've covered..."
- Identify speakers: "This is Alex speaking...", "As Sarah mentioned..."

**Add Turn-Taking**:
- Include brief acknowledgments between speakers
- Show listening cues: "Uh-huh", "Right", "I see"
- Allow for clarification questions
- Explicitly invite participation: "What do you think?", "Any thoughts on that?"

## Output Format

Markdown ordered list only:
1. Q: [discussion opener]
   A: [multi-turn collaborative exchange]
   
   Use speaker labels within answers:
   - **A:** / **B:** / **C:**
   - Or role labels: **Engineer:** / **PM:** / **Designer:**

## Instructions
- Use `1.` for every item; Markdown auto-numbers
- Output list only—no headings, comments, or explanations

## Examples

**Before** (Formal Extract):
> Q: What are the three key principles of database normalization?
> A: 1) First Normal Form (1NF): Eliminate repeating groups. 2) Second Normal Form (2NF): Remove partial dependencies. 3) Third Normal Form (3NF): Eliminate transitive dependencies.

**After** (Discussion):
> Q: We're designing the data model—should we normalize? What are the key principles we need to follow?
> A: **Engineer A:** Let's break down the normalization forms. First up is 1NF—basically no repeating groups.
> 
> **Engineer B:** Right. So instead of having like multiple phone numbers in one field, we'd split those out.
> 
> **A:** Exactly. Then 2NF tackles partial dependencies—every non-key field has to depend on the whole primary key, not just part of it.
> 
> **B:** That one trips people up. So if we have a composite key, all attributes need to relate to both parts?
> 
> **A:** Correct. And 3NF removes transitive dependencies. Think of it as... if A determines B, and B determines C, then A shouldn't directly store C.
> 
> **B:** Ah, cut out the middleman. Makes sense. So for our use case with the order system, we'd need all three?
> 
> **A:** Probably. Let's map it out.

**Before** (Formal Extract):
> Q: In a microservices architecture, you need to implement distributed transactions across three services. How would you approach this?
> A: Consider the Saga pattern with compensating transactions. Implement either choreography (event-driven) or orchestration (coordinator-based). Key factors: consistency requirements, failure handling, monitoring complexity.

**After** (Discussion):
> Q: Our payment flow spans three microservices. How do we handle the transaction across all of them?
> A: **Architect:** We can't use traditional ACID transactions here. I'd suggest the Saga pattern.
> 
> **Dev Lead:** Sagas... that's the compensating transaction approach, right? Like, each service can undo its work if something fails downstream?
> 
> **Architect:** Exactly. Each step has a compensating action. Now, we have two ways to implement it—choreography or orchestration.
> 
> **Dev Lead:** What's the difference?
> 
> **Architect:** Choreography is event-driven. Services listen for events and react. No central coordinator. Orchestration has one service managing the whole flow.
> 
> **Dev Lead:** Which one should we use?
> 
> **Architect:** Depends. How strict are our consistency requirements?
> 
> **Product:** Pretty strict. Failed payments can't show as successful.
> 
> **Architect:** Then orchestration might be better. Easier to monitor, easier to debug. You have one place that tracks the state.
> 
> **Dev Lead:** But doesn't that create a single point of failure?
> 
> **Architect:** It does. But choreography is harder to debug—you're tracing events across services. Given our team size and the payment criticality, I'd go orchestration. What do you think?
> 
> **Dev Lead:** Makes sense. Let's prototype it.

**Before** (Formal Extract):
> Q: A loop runs N times, each iteration taking O(log N). What is the total time complexity?
> A: O(N log N)

**After** (Discussion):
> Q: I'm analyzing this algorithm—there's a loop running N times, and each iteration does a binary search that's O(log N). What's the total complexity?
> A: **Dev A:** So N iterations, each costing log N...
> 
> **Dev B:** You multiply them, right? N times log N.
> 
> **A:** Yeah, O(N log N). That's actually pretty common.
> 
> **B:** Like mergesort?
> 
> **A:** Exactly. Same complexity pattern. You're doing something logarithmic N times.
> 
> **B:** Got it. And that's better than O(N²) but worse than O(N).
> 
> **A:** Right. It's in that efficient sorting territory.
