# Convert to Discussion Style

**Type**: Core dialogue format

**Task**: Transform extracted Q&A pairs into multi-party discussion format that simulates team meetings, collaborative work sessions, and group problem-solving with turn-taking, building on ideas, and interactive exploration.

**Definition**: Rewrite questions and answers as discussion flow between participants (3+ people), featuring conversational exchange, idea building, and collaborative problem-solving while preserving decision-critical accuracy.

## Input
Extracted Q&A pairs from any Extract/ prompt type (Cloze, Decision, Creativity, CriticalThinking, Debug, Reflection).

## Discussion Characteristics

**Language**: Conversational, focused, turn-taking, selective contractions, active listening cues

**Turn-Taking**: Building ("Building on that..."), Agreeing ("Exactly"), Contrasting ("On the other hand..."), Clarifying ("So you're saying..."), Questioning ("What about...?"), Synthesizing ("Connecting these ideas...")

**Interaction**: Question → Response → Follow-up; Idea → Build → Refine; Challenge → Clarification → Resolution

**Tone**: Collaborative, respectful but direct, thinking aloud, problem-solving focus

**Clarity**: Ideas developed through dialogue, analogies refined by group, visible thinking process

**Flow**: Non-linear, side discussions, signposted returns, periodic summaries

## Rules

**Fidelity**: Preserve all decision-critical content, facts, numbers, technical accuracy; maintain logical structure; no ungrounded additions

**Transformation**: Multi-turn dialogue (2-4 speakers), show idea development, natural dynamics, speaker labels, balanced contributions

**Format**: Question → opener; answer distributed across turns; show thinking process; may include asides

**Self-contained**: Provides context naturally, establishes scenario in opening, no assumed shared context

## Intelligent Complexity Adaptation

**LLM: Automatically determine single vs. multi-phase based on content complexity**

### When to Use Multiple Phases (2-5)

Expand when content exhibits:
- **Depth layers**: 3+ distinct levels requiring exploration
- **Length threshold**: Single exchange would exceed 200 words total
- **Natural topic shifts**: Predictable phase transitions (overview → deep dive → application → trade-offs)
- **Progressive building**: Group needs to align on basics before tackling complexity

### When to Keep Single Phase

Use single discussion when:
- Topic straightforward, resolvable in one exchange
- Discussion naturally fits in <200 words total across speakers
- No obvious phase transitions

### Multi-Phase Structure

**Phase Progression** (adapt to content):
1. Initial Discussion: Framing the problem, initial perspectives
2. Deep Dive: Technical details, mechanism exploration
3. Application Debate: How to use, implementation approaches
4. Trade-off Analysis: Pros/cons, when to use/avoid

**Phase Labels**: Use discussion markers like "(Opening)", "(Digging Deeper)" or natural transitions without labels

**Key Principles**:
- Concise turns per speaker
- One topic per phase
- Build through dialogue, not monologue
- Distribute speaking across participants
- Natural phase transitions
- Maintain momentum

**Phase Distribution**: 2 phases (simple + pivot) | 3 phases (standard complex) | 4 phases (complex + trade-offs) | 5 phases (max, rare)

## Discussion Management

**Common Patterns**:
- **Redirect drift**: "Good tangent, but let's refocus on...", "Related, but let's stick with..."
- **Recover disruption**: "Before we dropped, we were discussing...", "Back—quick recap..."
- **Align understanding**: "Are we all on the same page?", "Let me check everyone's following..."
- **Navigate disagreement**: "Both valid. Let's explore...", "Different contexts maybe?"
- **Manage participation**: "What do others think?", "Let's hear from...", "Any other perspectives?"

## Essential Dynamics for Group Discussions

Apply selectively (not to every dialogue). Balance: 80% content, 20% dynamics.

### Off-Topic Drift and Redirection

**Recognition**: Tangential questions, related but non-essential topics, scope creep

**Redirection**: "Good point. Let's bookmark that and get back to...", "That's off our main thread. Back to...", "Let's note that for later. Right now..."

**Example**:
> A: So anyway, this reminds me of blockchain consensus...
> B: Related, but different problem space. Sticking with microservices: when you...

### Disagreement and Constructive Debate

**Constructive patterns**: "I see it differently. What if...", "My experience says X. Why Y in your case?", "Valid. Let's look at both angles...", "We agree on X. Disagree on Y. Let's focus on..."

**Example**:
> A: Always normalize to 3NF.
> B: Disagree. Performance sometimes needs denormalization.
> A: Fair. Let me rephrase: start normalized, denormalize only when measured performance demands it.

### Managing Participation

**Balance techniques**: "What do others think?", "Let's hear from...", "Are we all on the same page?", "Before we continue, any other perspectives?"

**Example**:
> A: [Extended monologue on architecture]
> B: Good analysis. Before we decide, what does everyone else think?
> C: I was thinking...

### Context Recovery in Groups

**When needed**: After disruptions, when late joiners arrive, after tangents

**Recovery**: "To recap: covered X, Y. Now on Z.", "Let's realign. Main question was...", "Catching up—we're discussing [topic]. Question on the table: [current focus]"

**Example**:
> [After interruption]
> A: Back. Quick recap: we're debating choreography vs orchestration for Sagas. Pros and cons so far...

**For comprehensive patterns** → See ConversationDynamics.md

## Audio-Only Adaptation

**Visual → Verbal**: Replace "look at this", "as shown" with "imagine...", "consider..."  
**Confirmation**: Add "Are we aligned?", "Everyone following?", "Got it.", "Agreed."  
**Shorter chunks**: One idea per turn, frequent turn-taking, pause for acknowledgment  
**Explicit structure**: Number verbally, signal transitions, recap periodically, identify speakers  
**Turn-taking**: Brief acknowledgments, allow clarification, invite participation explicitly

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

**Speaker Labels**: **A:** / **B:** / **C:** or role labels: **Engineer:** / **PM:** / **Designer:**

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

---

### Example 3: Multi-Phase (High Complexity with Debate)

**Before** (Formal Extract):
> Q: In a microservices architecture, you need to implement distributed transactions across three services. How would you approach this?
> A: Consider the Saga pattern with compensating transactions. Implement either choreography (event-driven) or orchestration (coordinator-based). Key factors: consistency requirements, failure handling, monitoring complexity.

**After** (Discussion - Multi-Phase):
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
