# Convert to Discussion Style

**Type**: Core dialogue format

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

## Intelligent Complexity Adaptation

**LLM: Automatically determine single vs. multi-phase based on content complexity**

### When to Use Multiple Phases (2-5 phases)

Expand to multiple discussion phases when content exhibits:
- **Depth layers**: Topic has 3+ distinct levels requiring exploration
- **Length threshold**: Single discussion exchange would exceed 200 words total
- **Natural topic shifts**: Predictable phase transitions (overview → deep dive → application → trade-offs)
- **Progressive building**: Group needs to align on basics before tackling complexity
- **Multiple perspectives**: Topic benefits from different viewpoints across phases
- **Significant debate points**: Trade-offs or approaches warrant separate discussion

### When to Keep Single Phase

Use single discussion when:
- Topic is straightforward, resolvable in one exchange
- Discussion naturally fits in <200 words total across speakers
- No obvious phase transitions
- Concept doesn't require staged exploration

### Multi-Phase Structure for Discussions

**Phase Progression** (adapt to content):
1. **Initial Discussion**: Framing the problem, initial perspectives
2. **Deep Dive**: Technical details, mechanism exploration
3. **Application Debate**: How to use, implementation approaches
4. **Trade-off Analysis**: Pros/cons, when to use/avoid

**Phase Labels** (discussion style):
- Avoid rigid "Phase 1, Phase 2"
- Use discussion markers: "(Opening)", "(Digging Deeper)", "(Getting Practical)", "(Weighing Options)"
- Or use natural transitions without labels
- Signal shifts: "Let's pivot to...", "Okay, next angle...", "Building on that..."

**Discussion Evolution**:
- **Opening**: Frame problem, get initial takes
- **Exploration**: Challenge assumptions, build on ideas
- **Application**: "How would this work in practice?"
- **Synthesis**: Resolve disagreements, reach alignment or agree to disagree

**Key Principles for Multi-Phase** (preserve efficiency):
- **Concise turns**: Each speaker contribution focused and brief
- **One topic per phase**: Don't mix concerns across phases
- **Build through dialogue**: Ideas evolve through exchange, not monologue
- **All voices matter**: Distribute speaking across participants per phase
- **Natural transitions**: Phase shifts emerge organically from discussion
- **Maintain momentum**: Don't let phases drag; move forward when ready

**Phase Distribution**:
- 2 phases: Simple topic with one natural pivot (problem → solution)
- 3 phases: Standard complex topic (problem → approaches → choice)
- 4 phases: Complex with trade-offs (problem → solutions → debate → synthesis)
- 5 phases: Maximum (rare), only for highly controversial or layered topics

## Discussion Management

**Common Patterns**:
- **Redirect drift**: "Good tangent, but let's refocus on...", "Related, but let's stick with..."
- **Recover disruption**: "Before we dropped, we were discussing...", "Back—quick recap..."
- **Align understanding**: "Are we all on the same page?", "Let me check everyone's following..."
- **Navigate disagreement**: "Both valid. Let's explore...", "Different contexts maybe? For our case..."
- **Manage participation**: "What do others think?", "Let's hear from...", "Any other perspectives?"

## Essential Dynamics for Group Discussions

Group discussions naturally include debate, drift, and participation challenges. Apply selectively (not to every dialogue).

### Off-Topic Drift and Redirection

**Recognition**: Tangential questions, related but non-essential topics, scope creep

**Redirection techniques**:
- **Gentle**: "Good point. Let's bookmark that and get back to..."
- **Direct**: "That's off our main thread. Back to..."
- **Parking lot**: "Let's note that for later. Right now..."

**Example**:
> A: So anyway, this reminds me of blockchain consensus...
> B: Related, but different problem space. Sticking with microservices: when you...

### Disagreement and Constructive Debate

**Constructive conflict patterns**:
- **Respectful challenge**: "I see it differently. What if..."
- **Evidence-based**: "My experience says X. Why Y in your case?"
- **Explore both**: "Valid. Let's look at both angles..."
- **Find common ground**: "We agree on X. Disagree on Y. Let's focus on..."

**Example**:
> A: Always normalize to 3NF.
> B: Disagree. Performance sometimes needs denormalization.
> A: Fair. Let me rephrase: start normalized, denormalize only when measured performance demands it.

### Managing Participation

**Balance techniques**:
- **Invite quiet voices**: "What do others think?", "Let's hear from..."
- **Redirect dominance**: "Good points. Before we continue, any other perspectives?"
- **Check alignment**: "Are we all on the same page?"
- **Explicitly rotate**: "We've heard from A and B. C, your take?"

**Example**:
> A: [Extended monologue on architecture]
> B: Good analysis. Before we decide, what does everyone else think?
> C: I was thinking...

### Context Recovery in Groups

**When needed**: After disruptions, when late joiners arrive, after tangents

**Recovery patterns**:
- **Quick summary**: "To recap: covered X, Y. Now on Z."
- **Full reset**: "Let's realign. Main question was..."
- **For newcomers**: "Catching up—we're discussing [topic]. Question on the table: [current focus]"

**Example**:
> [After interruption]
> A: Back. Quick recap: we're debating choreography vs orchestration for Sagas. Pros and cons so far...

**Balance principle**: 80% content, 20% dynamics. Use when they enhance collaborative learning, not as artificial conflict.

**For 1-on-1 dynamics, presentation patterns, and comprehensive coverage** → See ConversationDynamics.md §1, §3, §5, §7

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

**Single Phase**:
1. Q: [discussion opener]
   A: [collaborative exchange with multiple speakers]
   
**Multi-Phase** (when complexity warrants):
1. Q: [discussion opener]
   A: [Phase 1: Initial exchange]
   
   [Natural transition or phase label]
   
   [Phase 2: Deeper exploration]
   
   [Phase 3: Application/synthesis]

**Speaker Labels**:
- **A:** / **B:** / **C:**
- Or role labels: **Engineer:** / **PM:** / **Designer:**

## Instructions
- Use `1.` for every item; Markdown auto-numbers
- LLM determines single vs. multi-phase automatically based on complexity criteria
- Output list only—no headings, comments, or explanations
- For multi-phase: keep all phases within same numbered item
- Use blank lines to visually separate phases

## Examples

### Example 1: Single Phase (Simple Topic)

**Before** (Formal Extract):
> Q: A loop runs N times, each iteration taking O(log N). What is the total time complexity?
> A: O(N log N)

**After** (Discussion - Single Phase):
> 1. Q: I'm analyzing this algorithm—there's a loop running N times, and each iteration does a binary search that's O(log N). What's the total complexity?
>    A: **Dev A:** So N iterations, each costing log N...
>    
>    **Dev B:** You multiply them, right? N times log N.
>    
>    **A:** Yeah, O(N log N). That's actually pretty common.
>    
>    **B:** Like mergesort?
>    
>    **A:** Exactly. Same complexity pattern. You're doing something logarithmic N times.
>    
>    **B:** Got it. And that's better than O(N²) but worse than O(N).
>    
>    **A:** Right. It's in that efficient sorting territory.

**LLM Analysis**: Straightforward calculation, quick back-and-forth, ~80 words total → Single phase

---

### Example 2: Multi-Phase (Moderate Complexity)

**Before** (Formal Extract):
> Q: What are the three key principles of database normalization?
> A: 1) First Normal Form (1NF): Eliminate repeating groups. 2) Second Normal Form (2NF): Remove partial dependencies. 3) Third Normal Form (3NF): Eliminate transitive dependencies.

**After** (Discussion - Multi-Phase):
> 1. Q: We're designing the data model—should we normalize? What are the key principles?
>    A: **Engineer A:** Three normal forms. Start with 1NF—no repeating groups.
>    
>    **Engineer B:** So split out things like multiple phone numbers in one field?
>    
>    **A:** Exactly.
>    
>    **Let's dig into the other two:**
>    
>    **A:** 2NF tackles partial dependencies—every non-key field depends on the whole primary key, not just part.
>    
>    **B:** Wait, so with composite keys, all attributes need to relate to both parts?
>    
>    **A:** Correct. And 3NF removes transitive dependencies. If A determines B, and B determines C, don't store A→C directly.
>    
>    **B:** Cut out the middleman.
>    
>    **Okay, for our order system:**
>    
>    **B:** Do we need all three?
>    
>    **A:** Probably. Let's map it out and see where we violate them.
>    
>    **B:** Good call.

**LLM Analysis**: Has distinct phases (concepts → details → application), benefits from staged exploration → 3 phases

---

### Example 3: Multi-Phase (High Complexity with Debate)

**Before** (Formal Extract):
> Q: In a microservices architecture, you need to implement distributed transactions across three services. How would you approach this?
> A: Consider the Saga pattern with compensating transactions. Implement either choreography (event-driven) or orchestration (coordinator-based). Key factors: consistency requirements, failure handling, monitoring complexity.

**After** (Discussion - Multi-Phase, Clean):
> 1. Q: Our payment flow spans three microservices. How do we handle the transaction across all of them?
>    A: **Architect:** Can't use traditional ACID. Need Saga pattern.
>    
>    **Dev Lead:** Sagas... that's compensating transactions? Each service can undo its work if something fails?
>    
>    **Architect:** Right. Each step has a compensating action.
>    
>    **Implementation approaches:**
>    
>    **Dev Lead:** How do we implement it?
>    
>    **Architect:** Two ways. Choreography—event-driven, services react to events. Or orchestration—central coordinator manages the flow.
>    
>    **Dev Lead:** What's better?
>    
>    **Now let's decide for our use case:**
>    
>    **Architect:** Depends on our consistency requirements. How strict?
>    
>    **Product:** Pretty strict. Failed payments can't show as successful.
>    
>    **Architect:** Then orchestration. Easier to monitor, easier to debug. One place tracking state.
>    
>    **Dev Lead:** But doesn't that create a single point of failure?
>    
>    **Architect:** It does. But choreography is harder to debug—tracing events across services. Given our team size and payment criticality, orchestration wins.
>    
>    **Dev Lead:** Makes sense. Let's prototype it.

**After** (With Dynamics - More Realistic):
> 1. Q: Our payment flow spans three microservices. How do we handle the transaction across all of them?
>    A: **Architect:** Can't use traditional ACID across services. Need Saga pattern.
>    
>    **Dev Lead:** Sagas... that's compensating transactions?
>    
>    **Architect:** Right. Each step has an undo.
>    
>    **Junior Dev:** Wait, why can't we use regular transactions?
>    
>    **Architect:** Each service owns its database. Can't span a transaction across them. That's the microservices trade-off.
>    
>    **Junior Dev:** Got it.
>    
>    **Implementation approaches:**
>    
>    **Dev Lead:** How do we implement it?
>    
>    **Architect:** Two ways. Choreography—event-driven. Or orchestration—central coordinator.
>    
>    **Dev Lead:** I've used choreography before. It scales better, right?
>    
>    **Architect:** It does, but—
>    
>    **Product:** Hold on, which one's more reliable? We can't mess up payments.
>    
>    **Deciding for our use case:**
>    
>    **Architect:** Let's talk reliability. Product, how strict are our consistency requirements?
>    
>    **Product:** Very. Failed payment can't show as successful.
>    
>    **Dev Lead:** Both patterns can handle that though.
>    
>    **Architect:** True, but orchestration makes failures visible in one place. Choreography? You're tracing events across services.
>    
>    [Phone interruption]
>    
>    **Dev Lead:** Sorry, back. So orchestration for debuggability?
>    
>    **Architect:** Exactly. And given our team size—five backend devs—I don't want us debugging event chains at 2am.
>    
>    **Dev Lead:** Fair point. What about the single point of failure concern?
>    
>    **Architect:** Valid. But we can make the orchestrator HA. Easier than debugging choreography gone wrong.
>    
>    **Product:** I'm convinced. Orchestration.
>    
>    **Dev Lead:** Agreed. Let's prototype it.

**LLM Analysis**: Multiple phases (problem → solutions → debate → decision), requires structured exploration → 4 phases; with dynamics shows clarification requests, disagreement, interruptions, and natural decision-making

---

### Example 4: Single Phase (Despite Moderate Length)

**Before** (Formal Extract):
> Q: What's the difference between TCP and UDP?
> A: TCP is connection-oriented with guaranteed delivery. UDP is connectionless, faster, but no guarantees.

**After** (Discussion - Single Phase):
> 1. Q: Should we use TCP or UDP for this real-time feature?
>    A: **Dev A:** What's the key difference again?
>    
>    **Dev B:** Reliability vs speed. TCP guarantees delivery with handshakes and retries. UDP fires and forgets—faster, but packets can drop.
>    
>    **A:** So for our video streaming?
>    
>    **B:** UDP. Dropped frame? Keep going. Latency matters more than perfection.
>    
>    **A:** And if it were financial transactions?
>    
>    **B:** TCP. Can't lose a payment. Reliability over speed.
>    
>    **A:** Clear. UDP for us then.

**LLM Analysis**: Clear comparison, quick decision, single conversational flow, ~90 words → Single phase (no need to artificially split)
