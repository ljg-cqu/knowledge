# Dialogue Prompts - Quick Reference

Transform extracted Q&A pairs into conversational formats for effective, natural, fluent dialogue practice about decision-critical information.

## File Selection Guide

### Choose Your Format (LLM Handles Complexity Automatically)

| File | Use When | Output Style | Auto-Adapts |
|------|----------|--------------|-------------|
| **ToConversation.md** | 1-on-1, casual learning, mentoring | Friendly, conversational, natural | Single or multi-round |
| **ToDiscussion.md** | Team meetings, group problem-solving, 3+ people | Collaborative, multi-party exchange | Single or multi-phase |
| **ToPresentation.md** | Formal presentations, lectures, 1-to-many | Professional, structured, authoritative | Single or multi-section |

### Real-World Dynamics (Built-in + Optional Reference)

| Approach | Description |
|----------|-------------|
| **Built-in** | Each format includes essential dynamics for its context (confusion handling, interruptions, etc.) |
| **ConversationDynamics.md** | Comprehensive reference for advanced patterns: humor, fatigue management, debate techniques, etc. |

---

## Quick Start

**Simple workflow:**
1. Choose format based on **style/participants** (not complexity)
2. LLM automatically adapts single/multi-round based on content
3. Essential dynamics already built-in (80% use cases)
4. Optionally consult ConversationDynamics.md for advanced patterns
5. Done

---

## Key Principle: Intelligent Complexity Adaptation

**You don't choose complexity—the LLM does automatically**

All three core formats intelligently determine whether to use:
- **Single exchange**: For straightforward topics (<150-250 words)
- **Multiple rounds/phases/sections**: For complex topics requiring progressive building

**Decision criteria built into each format:**
- Content depth layers
- Natural follow-up questions
- Length thresholds
- Progressive building needs

**You focus on:** Style and participants  
**LLM focuses on:** Complexity and round count

---

## Format Selection Decision Tree

```
START: What's your scenario?

├─ 1-on-1 conversation?
│  ├─ Casual tone? → ToConversation.md
│  └─ Formal tone? → ToPresentation.md
│
└─ Multiple people?
   └─ ToDiscussion.md

Add dynamics? → Apply ConversationDynamics.md patterns
```

**That's it.** No need to decide if topic is complex—the format handles that.

---

## File Details

### ToConversation.md
**Purpose**: 1-on-1 conversational style

**Automatically provides:**
- Single Q&A for simple topics
- Multi-round (2-5 rounds) for complex topics
- Natural question evolution
- Minimal essential words
- Essential 1-on-1 dynamics: confusion handling, technical interruptions, context rebuilding

**Best for**: Quick exchanges, mentoring, casual learning

**Complexity handling**: Rounds (Getting Started → Going Deeper → Getting Practical → Edge Cases)

---

### ToDiscussion.md
**Purpose**: Multi-party discussion format (3+ speakers)

**Automatically provides:**
- Single discussion for straightforward topics
- Multi-phase (2-5 phases) for complex topics
- Turn-taking between speakers
- Collaborative idea building
- Essential group dynamics: disagreement/debate, off-topic redirection, participation management, context recovery

**Best for**: Team meetings, brainstorming, collaborative problem-solving

**Complexity handling**: Phases (Opening → Deep Dive → Application → Trade-off Analysis)

---

### ToPresentation.md
**Purpose**: Formal presentation delivery (1-to-many)

**Automatically provides:**
- Single section for concise topics
- Multi-section (2-5 sections) for complex topics
- Clear signposting and transitions
- Professional structure
- Essential presentation dynamics: technical disruption recovery, audience re-engagement, question handling, context recovery

**Best for**: Formal talks, lectures, slide deck narration

**Complexity handling**: Sections (Overview → Details → Application → Summary)

---

### ConversationDynamics.md
**Purpose**: Comprehensive reference for advanced dynamics (supporting file)

**Relationship to core formats**: Core formats include essential dynamics; this file provides complete coverage

**Additional patterns covered:**
1. Advanced off-topic handling variations
2. Extended disruption scenarios
3. Humor & rapport building
4. Attention/energy/fatigue management
5. Complex disagreement resolution
6. Multiple context recovery strategies
7. Integration guidelines and balance principles

**When to use**: When core format dynamics aren't sufficient, practicing advanced conversation management, training scenarios requiring comprehensive realism

---

## Typical Workflows

### Workflow 1: Standard Usage (Most Common - 80% of cases)
```
Extract Q&A → Choose format → LLM adapts complexity automatically (with built-in dynamics) → Practice
```

### Workflow 2: Advanced Dynamics (When needed)
```
Extract Q&A → Choose format → LLM adapts complexity → Consult ConversationDynamics.md for specific patterns → Practice
```

### Workflow 3: Format Comparison
```
Extract Q&A → Generate in ToConversation.md (with 1-on-1 dynamics)
            → Generate in ToDiscussion.md (with group dynamics) → Compare styles
            → Generate in ToPresentation.md (with presentation dynamics)
```

---

## Examples of Automatic Complexity Adaptation

### Same Topic, Different Formats

**Input**: "What's a database index?"

**ToConversation.md** might produce:
- **Simple version**: Single round (if content is basic definition)
- **Complex version**: 4 rounds (what → how → when → trade-offs)

**ToDiscussion.md** might produce:
- **Simple version**: Single phase discussion
- **Complex version**: 3 phases (concept → application → decision)

**ToPresentation.md** might produce:
- **Simple version**: Single section
- **Complex version**: 4 sections (overview → mechanics → usage → caveats)

**You don't decide—the LLM analyzes content and adapts.**

---

## Input Requirements

All formats accept:
- Extracted Q&A pairs from `Extract/` directory:
  - Cloze.md
  - Decision.md
  - Creativity.md
  - CriticalThinking.md
  - Debug.md
  - Reflection.md
- Or any Q&A content in standard format

---

## Output Characteristics

### All Formats Preserve:
- ✅ Decision-critical content accuracy
- ✅ Facts, numbers, technical precision
- ✅ Logical structure

### All Formats Transform:
- Written → Spoken language
- Formal → Appropriate conversational tone
- Dense → Digestible chunks
- Automatic single vs. multi-round adaptation

### All Formats Include:
- Audio-only adaptation guidance
- Real-world dynamics cross-references
- Management pattern quick references
- Multiple examples showing complexity adaptation

---

## Common Patterns Across Files

### Intelligent Complexity Adaptation (All Formats)
Each format includes:
- **Criteria for multi-round/phase/section**: Automatic decision rules
- **Structure guidelines**: How to organize multiple exchanges
- **Pacing guidance**: 2-5 rounds/phases/sections based on content
- **Examples**: Both single and multi-round demonstrations

### Audio-Only Adaptation (All Formats)
- Remove visual references
- Add confirmation markers
- Explicit structure signals
- Shorter chunks for audio fatigue

### Fidelity Rules (All Formats)
- No hallucination
- No added ungrounded information
- Preserve all key points
- Maintain technical accuracy

---

## Tips for Best Results

### Do:
- ✅ Choose format based on style and participants
- ✅ Trust LLM to handle complexity automatically
- ✅ Use built-in dynamics (included in every format)
- ✅ Consult ConversationDynamics.md only when needed for advanced patterns
- ✅ Keep decision-critical info intact
- ✅ Review examples in each format file (including "With Dynamics" versions)

### Don't:
- ❌ Worry about whether topic is "complex enough" for multi-round
- ❌ Try to manually control round/phase count
- ❌ Feel obligated to use every dynamic pattern in every dialogue
- ❌ Mix multiple formats in one output
- ❌ Sacrifice accuracy for naturalness

---

## Quick Reference: Which File When?

**Situation: 1-on-1 casual explanation** → `ToConversation.md` (includes confusion handling, interruptions)

**Situation: Team collaboration meeting** → `ToDiscussion.md` (includes disagreement, participation management)

**Situation: Formal presentation or lecture** → `ToPresentation.md` (includes disruption recovery, re-engagement)

**Situation: Need advanced dynamics (humor, fatigue, complex debates)** → Consult `ConversationDynamics.md`

**Situation: Unsure about complexity** → Don't worry—pick format by style, LLM handles complexity + dynamics

---

## Your Primary Goal
> "Dialogue about decision-critical info confidently, effectively, naturally, concisely, fluently with minimal essential words, simulating real-world scenarios"

**Recommended path:**
1. Choose format by conversation style (Conversation/Discussion/Presentation)
2. LLM adapts complexity + includes essential dynamics automatically
3. Optionally consult ConversationDynamics.md for advanced patterns
4. Practice the output

---

## What Changed (For Existing Users)

**Old workflow:**
- Choose format (Conversation/Discussion/Presentation)
- If complex, choose ToDialogueFlow.md
- Manually decide single vs. multi-round

**New workflow:**
- Choose format (Conversation/Discussion/Presentation)
- LLM automatically adapts single/multi-round
- One less decision, simpler workflow

**Benefits:**
- ✅ Fewer files to choose from
- ✅ Automatic complexity handling
- ✅ No need to assess "is this complex enough"
- ✅ Consistent quality across simple and complex topics

---

## Summary

**Three core formats** (choose by style - self-contained with built-in dynamics):
1. `ToConversation.md` - Casual 1-on-1 (with confusion handling, interruptions, context rebuilding)
2. `ToDiscussion.md` - Group collaboration (with disagreement, participation management, off-topic handling)
3. `ToPresentation.md` - Formal presentation (with disruption recovery, re-engagement, question handling)

**One supporting reference** (for advanced needs):
- `ConversationDynamics.md` - Comprehensive coverage of all dynamics patterns

**Key innovations**: 
- LLM automatically determines single vs. multi-round based on content complexity
- Essential dynamics built into each format (80/20 principle)
- Advanced patterns available via reference file

**Your decisions**: 
1. Style and participants (not complexity)
2. Whether to use advanced dynamics beyond the built-in essentials

**Result**: Self-contained formats, intelligent adaptation, realistic dialogue practice, optional depth
