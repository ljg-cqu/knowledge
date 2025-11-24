# Prepositional Precision for Natural English
*Last Updated: 2025-11-24 | Status: Reviewed | Owner: Documentation Team*

**Type**: Dual-purpose - Supporting reference AND standalone post-check/improvement tool

**Purpose**: Register-aware reference guide and post-check tool for precise, natural preposition usage—eliminates errors, reduces verbosity, improves fluency. Supports both formal (academic/professional) and casual (conversational) contexts.

## Precision Principle

**Critical**: Enhance **clarity and naturalness** without changing **meaning or facts**—preserve all semantic content, never add or alter information.

**Conflict Resolution**: When fluency enhancements conflict with factual accuracy, always preserve accuracy.

**Example**:
```
Before: We need to have a discussion regarding the matter of database optimization.
After:  We need to discuss database optimization.
[Same meaning, more concise with correct preposition usage]
```

---

## Mode Selection

**Before applying corrections, specify your context:**

### **Formal Mode** (Academic papers, reports, presentations, professional writing)
**Apply**: All P0 + P1 + P2 priorities
- Enforce strict correctness and efficiency
- Eliminate verbose/redundant constructions
- Maximize clarity and professionalism

**Use for**: Academic papers, technical reports, formal presentations, professional documentation

**Example**:
```
Input:  Let's discuss about the solution. Where's the file at? It's in terms of performance.
Output: Let's discuss the solution. Where is the file? Regarding performance...
[All corrections applied]
```

### **Casual Mode** (Conversation, team chat, informal writing)
**Apply**: P0 (universal grammar errors) only
- Fix wrong collocations and spatial/temporal errors
- P1/P2: Optional—preserve natural casual flow
- Allow colloquial constructions when grammatically acceptable

**Use for**: Team chat, casual conversation, peer discussions, informal emails

**Example**:
```
Input:  Let's discuss about the solution. Where's the file at? It depends of many factors.
Output: Let's discuss about the solution. Where's the file at? It depends on many factors.
[Only P0 universal error fixed: "depends of" → "depends on"]
```

**Note**: Mode affects P1/P2 application. P0 (grammatical correctness) is universal and applies to both modes.

---

## 1-Minute Cheat Sheet

**→ 20 most critical fixes. Memorize these first.**

| **Error** | **Correct** | **Category** |
|---|---|---|
| ~~in Monday~~ → | on Monday | Temporal |
| ~~at Monday~~ → | on Monday | Temporal |
| ~~in 3 PM~~ → | at 3 PM | Temporal |
| ~~on January~~ → | in January | Temporal |
| ~~depends of~~ → | depends on | Verb Collocation |
| ~~consists from~~ → | consists of | Verb Collocation |
| ~~listen of~~ → | listen to | Verb Collocation |
| ~~arrive to~~ → | arrive at/in | Verb Collocation |
| ~~good in~~ → | good at | Adj Collocation |
| ~~interested at~~ → | interested in | Adj Collocation |
| ~~different than/with~~ → | different from | Adj Collocation |
| ~~solution of~~ → | solution to | Noun Collocation |
| ~~impact to~~ → | impact on | Noun Collocation |
| ~~discuss about~~ → | discuss | Transitive Verb |
| ~~enter into~~ (room) → | enter | Transitive Verb |
| ~~in terms of~~ → | (omit/rephrase) | Verbose |
| ~~where...at~~ → | where | Redundant |
| ~~inside of~~ → | inside | Redundant |
| ~~in the door~~ → | at the door | Spatial |
| ~~focus at~~ → | focus on | Verb Collocation |

**→ Apply these + Quick Reference below for 80% coverage.**

---

## Quick Reference: Core Patterns (80% of Use Cases)

**Most frequent patterns by category. Ordered by impact.**

| **Pattern** | **Priority** | **Usage** | **Examples** | **Common Errors** | **Details** |
|---|---|---|---|---|---|
| **Verb+Prep** | P0 (Universal) | 80% | depend **on**, consist **of**, listen **to**, focus **on** | ~~depends of~~, ~~focus at~~ | [→ Section V] |
| **Adj+Prep** | P0 (Universal) | 75% | good **at**, interested **in**, different **from**, familiar **with** | ~~good in~~, ~~different than~~ | [→ Section V] |
| **Noun+Prep** | P0 (Universal) | 70% | solution **to**, impact **on**, reason **for**, knowledge **of** | ~~solution of~~, ~~impact to~~ | [→ Section V] |
| **Spatial: at/on/in** | P0 (Universal) | 90% | **at** door (point), **on** table (surface), **in** room (enclosed) | ~~in the door~~ | [→ Section I] |
| **Temporal: at/on/in** | P0 (Universal) | 85% | **at** 3 PM (time), **on** Monday (day), **in** January (period) | ~~in Monday~~, ~~on 3 PM~~ | [→ Section II] |
| **Conciseness** | P1 (Formal) | 70% | ~~in terms of~~ → omit, ~~with regard to~~ → about | Verbose phrases | [→ Section VII] |
| **Redundancy** | P1 (Formal) | 65% | ~~where...at~~ → where, ~~inside of~~ → inside | Double prepositions | [→ Section VII] |
| **Transitive Verbs** | P1 (Formal) | 60% | discuss (not ~~about~~), enter (not ~~into~~), marry (not ~~with~~) | Extra prepositions | [→ Section VII] |
| **Direction** | P2 (Polish) | 70% | **to** (arrive), **toward** (direction), **into** (enter), **from** (origin) | to vs toward confusion | [→ Section III] |
| **Abstract** | P2 (Polish) | 75% | talk **about**, focus **on**, part **of**, designed **for** | Mixed with verbs | [→ Section IV] |
| **Idioms** | P2 (Polish) | 60% | **on** time (punctual), **in** time (early), **by** accident | Fixed expressions | [→ Section VI] |

**Legend**: P0 (Universal) = Apply in both Formal & Casual modes | P1 (Formal) = Apply in Formal mode only | P2 (Polish) = Apply in Formal mode for sophistication

**→ 80% complete above. Continue for: priority system, workflow, comprehensive patterns (Sections I-VII).**

---

## Priority System

**Register-aware application order:**

- **P0 (Must fix - Universal)**: Fixed collocations (Quick Ref #9-11), spatial/temporal errors (#1-2)
  - **Context**: Apply in ALL modes (Formal + Casual)
  - Wrong collocations cause grammatical errors
  - Examples: ~~depends of~~ → depends on, ~~in Monday~~ → on Monday
  
- **P1 (High value - Context-dependent)**: Conciseness (#8), redundant prepositions (#12)
  - **Formal mode**: Must fix (verbose phrases reduce professionalism)
  - **Casual mode**: Optional (colloquial constructions acceptable)
  - Examples: ~~in terms of~~ → (omit), ~~where...at~~ → where, ~~discuss about~~ → discuss

- **P2 (Polish - Formal preferred)**: Direction/abstract (#3-7), idioms (#13-15)
  - **Formal mode**: Recommended (improves sophistication)
  - **Casual mode**: Usually skip (may sound unnatural)
  - Examples: toward vs to, *on time* vs *in time*

**Application by Mode**:
- **Formal**: Fix P0 (correctness) → P1 (clarity) → P2 (polish)
- **Casual**: Fix P0 only (preserve natural flow)

---

## Standalone Usage: Post-Check Workflow

**Mode 1: Reference During Writing** — Use Quick Reference and Cheat Sheet while drafting

**Mode 2: Post-Check After Writing** — Audit completed content systematically

### Review Workflow

**Step 0: Select Mode** [→ Mode Selection]
- **Formal mode**: Academic papers, reports, presentations → Apply P0+P1+P2
- **Casual mode**: Conversation, team chat, informal writing → Apply P0 only

**Step 1: Scan** — Identify errors by priority [→ Priority System]

**Formal Mode Path**:
- **P0 check (correctness - universal)**: Fixed collocations, spatial/temporal
  - Scan for: verb+prep, adj+prep, noun+prep, time/date, location
  - Tools: Cheat Sheet (20 top errors), Quick Reference table, Decision Tree
- **P1 check (clarity - required)**: Verbose phrases, redundant prepositions, transitive verbs
  - Scan for: "in terms of", "where...at", "discuss about"
  - Tools: Section VII patterns
- **P2 check (polish - recommended)**: Direction, idioms, naturalness
  - Scan for: to/toward distinction, fixed expressions
  - Tools: Sections III, VI

**Casual Mode Path**:
- **P0 check (correctness - universal)**: Fixed collocations, spatial/temporal
  - Scan for: verb+prep, adj+prep, noun+prep, time/date, location
  - Tools: Cheat Sheet (20 top errors), Quick Reference table
  - Skip: P1/P2 checks (preserve casual flow)

**Step 2: Fix** — Apply corrections using patterns
- **Formal mode**: Replace errors with correct forms, simplify verbose phrases, remove redundancies
- **Casual mode**: Fix only P0 grammatical errors, preserve colloquial constructions
- Always preserve all semantic content

**Step 3: Validate** — Quality checks before finalization
- ✓ Semantic content preserved?
- ✓ Mode-appropriate corrections applied?
- ✓ Grammatically correct?
- ✓ Natural for target context?
- ✓ Read aloud for fluency

### Quick Diagnostic Questions
- Are there verb/adj/noun + preposition combinations? → Check Section V
- Are there time or location references? → Check Sections I, II
- Are there phrases like "in terms of" or "where...at"? → Check Section VII
- Does it sound unnatural or wordy? → Check Priority System

**→ For pattern details and comprehensive reference, continue to Sections I-VII below.**

---

## Pattern Selection Guide (Decision Tree)

**Use this to quickly identify which pattern applies:**

```
START: Identify the error type
│
├─ Is it a VERB + preposition? (e.g., "depends of")
│  └─ → Use Section V: Verb+Prep Collocations (P0)
│     Examples: depend on, consist of, listen to, focus on
│
├─ Is it an ADJECTIVE + preposition? (e.g., "good in")
│  └─ → Use Section V: Adj+Prep Collocations (P0)
│     Examples: good at, interested in, different from
│
├─ Is it a NOUN + preposition? (e.g., "solution of")
│  └─ → Use Section V: Noun+Prep Collocations (P0)
│     Examples: solution to, impact on, reason for
│
├─ Is it about LOCATION/PLACE? (e.g., "in the door")
│  └─ → Use Section I: Spatial Prepositions (P0)
│     Rule: at (point), on (surface), in (enclosed)
│
├─ Is it about TIME/DATE? (e.g., "in Monday")
│  └─ → Use Section II: Temporal Prepositions (P0)
│     Rule: at (time), on (day/date), in (period)
│
├─ Is it a VERBOSE phrase? (e.g., "in terms of")
│  └─ → Use Section VII: Efficiency Patterns (P1)
│     Action: Omit or rephrase for conciseness
│
├─ Is it a REDUNDANT preposition? (e.g., "where...at")
│  └─ → Use Section VII: Redundancy Patterns (P1)
│     Action: Remove unnecessary preposition
│
├─ Is the verb TRANSITIVE? (e.g., "discuss about")
│  └─ → Use Section VII: Transitive Verbs (P1)
│     Action: Remove preposition entirely
│
├─ Is it a FIXED EXPRESSION? (e.g., "on time" vs "in time")
│  └─ → Use Section VI: Idiomatic Expressions (P2)
│     Action: Memorize the fixed form
│
└─ Is it about MOVEMENT/DIRECTION? (e.g., "go toward" vs "go to")
   └─ → Use Section III: Directional Prepositions (P2)
      Rule: to (destination), toward (direction), into (entering)
```

**→ For comprehensive patterns and examples, continue to Sections I-VII below.**

---

## Comprehensive Patterns (Advanced Reference)

**→ 80% of use cases covered above. Continue only if needed for edge cases.**

**Structure**: Two approaches (use both for complete mastery)

### Approach 1: By Pattern Logic (Why/How)
- **I. Spatial** (90%): Rules for at/on/in with location
- **II. Temporal** (85%): Rules for at/on/in with time
- **III. Directional** (70%): Rules for movement prepositions
- **IV. Abstract** (75%): Rules for concept prepositions

### Approach 2: By Word Type (What to Fix - Most Practical)
- **V. Fixed Collocations** (80%): Memorized verb/adj/noun + prep pairs
  - This section covers most errors (Verb+Prep, Adj+Prep, Noun+Prep)
  - Sections I-IV explain the logic; Section V provides quick lookup

### Special Cases
- **VI. Idiomatic Expressions** (60%): Fixed phrases requiring memorization
- **VII. Efficiency Patterns** (70%): Eliminating verbose/redundant prepositions

**Recommendation**: Start with Section V (Fixed Collocations) for fastest results, then consult I-IV for understanding edge cases.

---

## I. Spatial Prepositions
[← Quick Reference #1 | Priority: P0]

**Core Patterns** (90% usage):
- **at** (point): *at the door, at 123 Main St, at the conference, at school*
- **on** (surface): *on the table, on the bus, on Elm Street, on the screen*
- **in** (enclosed): *in the room, in Tokyo, in the database, in the system*

**Key Distinction**: at = point, on = surface/line, in = 3D enclosure
```
✓ at the station (point) | on the table (surface) | in Tokyo (area)
✗ in the station (unless inside building)
```

**Advanced Distinctions**:
- **between** (2 items) vs **among** (3+ items)
- **above** (higher, no contact) vs **over** (covering/spanning)
- **below** (lower) vs **under** (directly beneath)

---

## II. Temporal Prepositions
[← Quick Reference #2 | Priority: P0]

**Core Patterns** (85% usage):
- **at** (specific time): *at 3 PM, at noon, at the moment, at 25 (age), **at night***
- **on** (days/dates): *on Monday, on July 4th, on my birthday, on Monday morning*
- **in** (longer periods): *in 2024, in January, in summer, in the morning, in two hours*

**Key Distinction**: at = point in time, on = day/date, in = period/future duration
```
✓ at 9 AM | on Friday | in March | **at night** (exception)
✗ in 9 AM | in Friday | on March
```

**Duration/Deadline**:
- **for** (how long): *for two hours*
- **during** (when): *during the meeting*
- **since** (start point): *since 2019*
- **by** (deadline): *by Friday*
- **until** (continuing): *until 6 PM*

---

## III. Directional Prepositions
[← Quick Reference #3 | Priority: P2]

**Core Patterns** (70% usage):
- **to** (destination/target): *go to the office, send to client, from 1 to 10*
- **toward** (direction, not arrival): *walk toward the exit, moving toward a solution*
- **into** (entering/transformation): *step into the room, turn into ice, translate into Chinese*
- **from** (origin/source): *come from, stem from research, from 9 to 5*
- **through** (passage/means): *drive through tunnel, learn through practice*

**Key Distinction**: to = reaching destination, toward = moving in direction, into = entering
```
✓ go to the office | walk toward the door | step into the room | come from Tokyo
✗ go at the office | walk to the door (if not arriving)
```

---

## IV. Abstract Prepositions
[← Quick Reference #4-7 | Priority: P2]

**Purpose**: Understand semantic meaning to handle non-collocation cases. For fixed verb/adj/noun+prep pairs, see Section V.

**Semantic Patterns** (75% usage):
- **about** (topic/approximate): General topic, rough quantity
  - *talk/think/worry about*, *about $100* (approximate)
- **on** (formal topic/focus): Specific focus, formal subject matter
  - *lecture/presentation/paper on*, *focus/concentrate on*
- **of** (belonging/composition/origin): Possession, part-whole, source
  - *CEO of company*, *consist/composed of*, *matter of time*
- **for** (purpose/beneficiary/duration): Goal, recipient, time span
  - *designed/built for*, *work for company*, *for two hours*
- **with** (accompaniment/tool/manner): Association, instrument, method
  - *work with team*, *build with Python*, *agree/consistent with*

**When to Use**:
- Choosing between prepositions with similar meanings
- Understanding why certain collocations exist
- Handling new combinations not in Section V

```
✓ talk about the project (general topic) | lecture on AI (formal topic)
✓ consists of modules (composition) | designed for testing (purpose)
✗ focus at → focus on (wrong preposition for focus/concentration)
```

**Note**: Many abstract prepositions form fixed collocations (see Section V). This section explains the logic; Section V provides the complete list.

---

## V. Fixed Collocations
[← Quick Reference #9-11 | Priority: P0]

**Verb+Preposition** (80% usage):
- depend **on**, consist **of**, listen **to**, focus **on**
- look **at** (observe), look **for** (search), look **after** (care)
- participate **in**, apologize **for**, wait **for**, belong **to**
- arrive **at** (place), arrive **in** (city/country)

**Adjective+Preposition** (75% usage):
- good/bad **at**, interested **in**, capable **of**, responsible **for**, familiar **with**
- different **from** (US) / **to** (UK), afraid **of**, proud **of**, similar **to**, satisfied **with**

**Noun+Preposition** (70% usage):
- solution/answer **to**, reason **for**, impact/effect/influence **on**
- difference **between** (2) / **among** (3+), relationship **between/with**
- knowledge **of**, expertise **in**

**Common Errors**:
```
✗ depends of → ✓ depends on
✗ good in → ✓ good at
✗ solution of → ✓ solution to
✗ impact to → ✓ impact on
✗ arrive to → ✓ arrive at/in
```

---

## VI. Idiomatic Expressions
[← Quick Reference #13-15 | Priority: P2]

**Time** (60% usage):
- *at first* (initially), *at last* (finally), *in the end* (outcome)
- *on time* (punctual), *in time* (before too late)
- *in advance*, *ahead of time*, *for the time being*, *at the moment*

**Manner**:
- *by accident* (unintentionally), *on purpose* (intentionally)
- *in detail*, *in general*, *by hand*, *by machine*, *in secret*, *in public*

**Degree**:
- *to some extent*, *by far*, *at least*, *at most*, *on average*

**State**:
- *in progress*, *in development*, *in production*
- *out of order* (broken), *out of service* (unavailable)
- *under control* (not ~~in control~~), *in favor of*

---

## VII. Efficiency Patterns
[← Quick Reference #8, #12, #14 | Priority: P1 - Context-dependent]

**Register Note**: These patterns are **context-dependent**:
- **Formal mode**: Apply all corrections (reduces verbosity, increases professionalism)
- **Casual mode**: Optional (many constructions are colloquially acceptable)

**A. Verbose → Concise** (70% usage):
- ~~in terms of~~ → (omit or rephrase) [Formal: required | Casual: acceptable]
- ~~with regard to~~ → about / regarding [Formal: required | Casual: acceptable]
- ~~in the event of~~ → if [Formal: preferred | Casual: acceptable]
- ~~for the purpose of~~ → to / for [Formal: preferred | Casual: acceptable]
- ~~by means of~~ → by / using [Formal: preferred | Casual: acceptable]
- ~~in order to~~ → to [Formal: preferred | Casual: acceptable]
- ~~at this point in time~~ → now / currently [Formal: required | Casual: acceptable]
- ~~due to the fact that~~ → because / since [Formal: required | Casual: acceptable]
- ~~in spite of the fact that~~ → although / despite [Formal: required | Casual: acceptable]
- ~~during the course of~~ → during [Formal: preferred | Casual: acceptable]
- ~~in the process of~~ → verb+-ing [Formal: preferred | Casual: acceptable]
- ~~a large number of~~ → many [Formal: preferred | Casual: acceptable]
- ~~in close proximity to~~ → near [Formal: preferred | Casual: acceptable]

**B. Redundant → Eliminate**:
- ~~where...at~~ → where [Formal: required | Casual: colloquial/regional acceptable]
- ~~inside of~~ → inside [Formal: required | Casual: acceptable in informal speech]
- ~~off of~~ → off [Formal: required | Casual: acceptable in American English]
- ~~outside of~~ → outside [Formal: required | Casual: acceptable in informal speech]

**C. Transitive Verbs (no preposition)**:
- *discuss* (not ~~discuss about~~) [Formal: required | Casual: "discuss about" acceptable in some dialects]
- *enter* room (not ~~enter into~~) [Universal: no preposition except "enter into agreement"]
- *reach* conclusion (not ~~reach to~~) [Universal: no preposition]
- *marry* someone (not ~~marry with~~) [Universal: no preposition]

---

## Examples with Pattern Analysis

**Example 1: Collocation Errors (P0 - Universal)**
```
✗ The meeting starts in Monday. We'll discuss about features. The team is good in React.
```

**Analysis**:
- "in Monday" → **Temporal error** (Section II, P0): Days use "on" → "on Monday"
- "discuss about" → **Transitive verb** (Section VII-C, P1): Context-dependent
- "good in" → **Adj+Prep collocation** (Section V, P0): Correct form → "good at"

**Formal Mode Output**:
```
✓ The meeting starts on Monday. We'll discuss features. The team is good at React.
[All errors fixed: 2 P0 + 1 P1]
```

**Casual Mode Output**:
```
✓ The meeting starts on Monday. We'll discuss about features. The team is good at React.
[Only P0 errors fixed: 2 universal corrections, "discuss about" preserved as colloquial]
```

---

**Example 2: Conciseness (P1 - Context-Dependent)**
```
✗ In terms of performance, the system is slow due to the fact that we have many queries.
```

**Analysis**:
- "In terms of performance" → **Verbose phrase** (Section VII-A, P1): Context-dependent
- "due to the fact that" → **Verbose phrase** (Section VII-A, P1): Context-dependent
- No P0 errors present

**Formal Mode Output**:
```
✓ The system performs poorly because we have many queries.
[P1 corrections applied: reduced verbosity, increased professionalism]
```

**Casual Mode Output**:
```
✓ In terms of performance, the system is slow due to the fact that we have many queries.
[No corrections: P1 patterns preserved as acceptable in casual context]
```

---

**Example 3: Comprehensive (Mixed P0 + P1)**
```
✗ We need to discuss about the solution of this problem. The issue is different than expected. 
In the event of failure, retry. Where's the file at? Success depends of many factors.
```

**Analysis**:
- "discuss about" → **Transitive verb** (Section VII-C, P1): Context-dependent
- "solution of" → **Noun+Prep collocation** (Section V, P0): Correct form → "solution to"
- "different than" → **Adj+Prep collocation** (Section V, P0): US standard → "different from"
- "In the event of" → **Verbose phrase** (Section VII-A, P1): Context-dependent
- "Where's the file at?" → **Redundant preposition** (Section VII-B, P1): Context-dependent (colloquial)
- "depends of" → **Verb+Prep collocation** (Section V, P0): Correct form → "depends on"

**Error Count**: 3 P0 (universal), 3 P1 (context-dependent)

**Formal Mode Output**:
```
✓ We need to discuss the solution to this problem. The issue differs from what we expected. 
If it fails, retry. Where's the file? Success depends on many factors.
[All 6 errors fixed: 3 P0 + 3 P1]
```

**Casual Mode Output**:
```
✓ We need to discuss about the solution to this problem. The issue is different from what we expected. 
In the event of failure, retry. Where's the file at? Success depends on many factors.
[Only 3 P0 errors fixed: universal collocations corrected, P1 patterns preserved as colloquial]
```

---

## Summary

**Document Type**: Dual-purpose (reference + post-check tool)

**Mode Selection**: Register-aware correction system
- **Formal mode**: Apply P0+P1+P2 (academic papers, reports, presentations)
- **Casual mode**: Apply P0 only (conversation, team chat, informal writing)

**Fast Start**: 
- Mode Selection (choose Formal or Casual)
- 1-Minute Cheat Sheet (20 top errors)
- Quick Reference table (11 patterns with priority indicators, 80% coverage)
- Decision Tree for pattern identification

**Categories**: Spatial • Temporal • Direction • Abstract • Collocations • Idioms • Efficiency

**Structure** (MECE):
- **By Logic** (Approach 1): Spatial, Temporal, Direction, Abstract → understand "why"
- **By Word Type** (Approach 2): Fixed Collocations (Verb/Adj/Noun+Prep) → quick lookup
- **Special Cases**: Idioms, Efficiency patterns

**Coverage**: ~90% of prepositional errors with Cheat Sheet + Quick Reference

**80/20**: Cheat Sheet + Quick Reference (80%) → Comprehensive Sections I-VII (20%)

**Priority System**: Register-aware
- **P0 (Universal)**: Apply in ALL modes (grammatical correctness)
- **P1 (Formal)**: Apply in Formal mode only (clarity, conciseness)
- **P2 (Polish)**: Apply in Formal mode for sophistication

**Principle**: Preserve meaning, enhance clarity and naturalness while respecting context

**Usage Flow**: 
1. Select mode → Formal or Casual
2. Quick fixes → Cheat Sheet (20 errors)
3. Pattern lookup → Quick Reference table
4. Systematic review → Post-Check Workflow (mode-specific)
5. Edge cases → Decision Tree + Sections I-VII

