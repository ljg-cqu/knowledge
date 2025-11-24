# Convert to Discussion Style (Casual)

**Purpose**: Transform Q&A pairs into informal multi-party discussion (3+ speakers) with casual turn-taking, idea building, and collaborative problem-solving.

**Input**: Extracted Q&A pairs from any Extract/ prompt type.

## Core Rules

**Fidelity**: Preserve all decision-critical content, facts, numbers, technical accuracy; no ungrounded additions

**Conflict Resolution**: When fluency enhancements conflict with factual accuracy, always preserve accuracy

**Format**: 
- 2-4 speakers with balanced contributions
- Casual conversational language with natural turn-taking
- Q becomes discussion opener; A distributed across collaborative exchange
- Self-contained: establish context in opening, no assumed shared knowledge

**Language Style**:
- Contractions ("That's", "We're", "Can't")
- Casual markers ("So...", "Yeah", "Right", "Got it")
- Informal phrasing ("Let's check out", "Okay, so", "Makes sense")
- Fragments and short responses

**Dynamics** (apply selectively):
- Building/agreeing: "Yeah, exactly", "Building on that...", "Plus..."
- Clarifying: "Wait, so...", "You mean...?", "So basically..."
- Managing: "Let's get back to...", "What do you guys think?"

## Complexity Adaptation

**Single Phase** (<200 words, straightforward topic):
- One continuous exchange, no phase breaks
- Topic resolvable in direct dialogue

**Multi-Phase** (200+ words, 3+ depth layers, natural topic shifts):
- 2-5 phases with casual transitions (e.g., "Okay, so...", "What about...", "For our thing:")
- Common progression: Frame → Deep dive → Application → Trade-offs
- Short turns, one topic per phase, distributed speaking

## Output Format

**Structure**:
```
1. Q: [casual discussion opener]
   A: **Speaker A:** [turn]
   
   **Speaker B:** [turn]
   
   [For multi-phase: casual transition like "Okay, so..."]
   
   **A:** [turn]
```

**Guidelines**:
- Use `1.` for every item; Markdown auto-numbers
- Speaker labels: **A:** / **B:** / **C:** or **Dev1:** / **Dev2:** / **Dev3:**
- Multi-phase: keep all phases within same numbered item, separate with blank lines
- Output list only—no headings or meta-commentary

## Examples

### Single Phase Example

**Before**: Q: A loop runs N times, each iteration taking O(log N). What is the total time complexity? A: O(N log N)

**After**:
> 1. Q: So we've got a loop that runs N times, and each time it does a binary search which is O(log N). What's the total?
>    A: **A:** Okay, so N iterations, and each one costs log N...
>    
>    **B:** Yeah, you just multiply them. N times log N.
>    
>    **A:** Right, O(N log N). It's like mergesort—same deal.
>    
>    **B:** Got it. Better than O(N²), but not as good as O(N).

### Multi-Phase Example

**Before**: Q: What are the three key principles of database normalization? A: 1NF: Eliminate repeating groups. 2NF: Remove partial dependencies. 3NF: Eliminate transitive dependencies.

**After**:
> 1. Q: What's the deal with normalization? Like, what are the key things we need to know?
>    A: **A:** There's three forms. First one's 1NF—basically no repeating groups.
>    
>    **B:** So like, if someone has multiple phone numbers, you split that out?
>    
>    **A:** Exactly.
>    
>    **Okay, what about the other ones:**
>    
>    **A:** 2NF—every field that's not the key has to depend on the whole primary key. And 3NF removes transitive dependencies.
>    
>    **B:** Wait, transitive? So if A determines B, and B determines C, you don't store A→C directly?
>    
>    **A:** Yeah, exactly. Cut out the middleman.
>    
>    **For our order system:**
>    
>    **B:** Do we need all three?
>    
>    **A:** Probably, yeah. Let's map it out and see where we're violating them.
