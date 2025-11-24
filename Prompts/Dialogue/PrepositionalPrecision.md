# Prepositional Precision for Natural English
*Last Updated: 2025-11-24 | Status: Reviewed | Owner: Documentation Team*

**Type**: Dual-purpose reference and post-check tool

**Purpose**: Register-aware guide for precise preposition usage—eliminates errors, reduces verbosity, improves fluency. Supports formal and casual contexts.

## Core Principle

**Enhance clarity and naturalness without changing meaning or facts. Preserve accuracy over fluency.**

```
Before: We need to have a discussion regarding the matter of database optimization.
After:  We need to discuss database optimization.
```

---

## Philosophy: Prepositional Preference

**Two goals**:
1. **Correct errors**: Fix wrong prepositions (e.g., "depends of" → "depends on")
2. **Prefer concise forms**: Choose prepositional constructions when more natural and structured

**Why prepositional forms?** More concise, structured, natural, and precise.

**Examples**:
```
Verbose → Concise (Prepositional)
────────────────────────────────────────────────
Users can authenticate by using OAuth. → Users authenticate through OAuth.
System had problems when there was heavy load. → System had problems under heavy load.
We made changes because of user feedback. → We made changes based on user feedback.
The API works when you have valid credentials. → The API works with valid credentials.
Error occurred while system was processing data. → Error occurred during data processing.
```

**When to use prepositional forms**: Shorter, clearer, more natural, especially in formal writing

**When to keep non-prepositional forms**: Provides necessary emphasis, avoids ambiguity, improves rhythm

---

## Mode Selection *(Default: Casual)*

### Formal Mode
**Apply**: P0 + P1 + P2
- Strict correctness, eliminate verbose/redundant constructions
- **Use for**: Academic papers, technical reports, formal documentation

```
Input:  Let's discuss about the solution. Where's the file at? It's in terms of performance.
Output: Let's discuss the solution. Where is the file? Regarding performance...
```

### Casual Mode
**Apply**: P0 only (universal grammar errors)
- Fix wrong collocations and spatial/temporal errors only
- Preserve colloquial constructions if grammatically acceptable
- **Use for**: Team chat, casual conversation, informal emails

```
Input:  Let's discuss about the solution. Where's the file at? It depends of many factors.
Output: Let's discuss about the solution. Where's the file at? It depends on many factors.
[Only P0 fixed: "depends of" → "depends on"]
```

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

## Quick Reference: Core Patterns (80% Coverage)

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
| **Prepositional Preference** | P3 (Style) | 65% | fails **under** heavy load | authenticates **via** OAuth | Prefer concise prepositional forms | [→ Section VIII] |

**Legend**: P0 (Universal) = Both modes | P1 (Formal) = Formal only | P2 (Polish) = Formal sophistication | P3 (Style) = Optional prepositional preference

---

## Priority System

- **P0 (Universal)**: Fixed collocations, spatial/temporal errors — Apply in ALL modes
  - ~~depends of~~ → depends on, ~~in Monday~~ → on Monday
  
- **P1 (Formal only)**: Conciseness, redundancy
  - ~~in terms of~~ → (omit), ~~where...at~~ → where, ~~discuss about~~ → discuss

- **P2 (Formal preferred)**: Direction/abstract, idioms
  - toward vs to, *on time* vs *in time*

- **P3 (Optional)**: Prepositional preference for concise, natural forms
  - "fails under heavy load" vs "fails when there is heavy load"

**Application**: Formal (P0→P1→P2→P3 optional) | Casual (P0 only, P3 when beneficial)

---

## Standalone Usage: Post-Check Workflow

**Mode 1**: Reference during writing (use Quick Reference + Cheat Sheet)  
**Mode 2**: Post-check after writing (audit systematically)

### Review Workflow

**Step 0: Select Mode** *(Default: Casual)*
- **Formal**: Academic papers, reports → Apply P0+P1+P2
- **Casual**: Conversation, team chat → Apply P0 only

**Step 1: Scan by Priority**

**Formal Path**:
- **P0**: Fixed collocations, spatial/temporal (Cheat Sheet, Quick Reference)
- **P1**: Verbose phrases, redundant prepositions (Section VII)
- **P2**: Direction, idioms (Sections III, VI)
- **P3 (optional)**: Prepositional preference (Section VIII)

**Casual Path**:
- **P0**: Fixed collocations, spatial/temporal only
- Skip P1/P2/P3 (preserve casual flow)
- **P3 exception**: Apply when significantly clearer

**Step 2: Fix**
- **Formal**: Replace errors, simplify, remove redundancies, prefer prepositional forms (P3 optional)
- **Casual**: Fix P0 only, preserve colloquial constructions
- Preserve semantic content

**Step 3: Validate**
✓ Meaning preserved? ✓ Mode-appropriate? ✓ Grammatically correct? ✓ Natural?

### Quick Diagnostics
- Verb/adj/noun + prep combinations? → Section V
- Time or location references? → Sections I, II
- Phrases like "in terms of", "where...at"? → Section VII
- Sounds unnatural or wordy? → Priority System
- Verbose clauses replaceable with prepositional forms? → Section VIII

---

## Pattern Selection Guide

**Error type** → **Section**:
- **VERB + prep** (e.g., "depends of") → Section V (P0): depend on, consist of, listen to, focus on
- **ADJ + prep** (e.g., "good in") → Section V (P0): good at, interested in, different from
- **NOUN + prep** (e.g., "solution of") → Section V (P0): solution to, impact on, reason for
- **LOCATION/PLACE** (e.g., "in the door") → Section I (P0): at (point), on (surface), in (enclosed)
- **TIME/DATE** (e.g., "in Monday") → Section II (P0): at (time), on (day/date), in (period)
- **VERBOSE phrase** (e.g., "in terms of") → Section VII (P1): Omit or rephrase
- **REDUNDANT prep** (e.g., "where...at") → Section VII (P1): Remove unnecessary preposition
- **TRANSITIVE verb** (e.g., "discuss about") → Section VII (P1): Remove preposition
- **FIXED EXPRESSION** (e.g., "on time" vs "in time") → Section VI (P2): Memorize fixed form
- **MOVEMENT/DIRECTION** (e.g., "go toward" vs "go to") → Section III (P2): to (destination), toward (direction), into (entering)
- **CONCISENESS opportunity** → Section VIII (P3): Replace verbose clauses with prepositional phrases

---

## Comprehensive Patterns (Advanced Reference)

**80% covered above. Continue for edge cases.**

### By Pattern Logic (Why/How)
- **I. Spatial** (90%): at/on/in with location
- **II. Temporal** (85%): at/on/in with time
- **III. Directional** (70%): Movement prepositions
- **IV. Abstract** (75%): Concept prepositions

### By Word Type (Most Practical)
- **V. Fixed Collocations** (80%): Verb/adj/noun + prep pairs (covers most errors)

### Special Cases
- **VI. Idiomatic Expressions** (60%): Fixed phrases
- **VII. Efficiency Patterns** (70%): Eliminate verbose/redundant prepositions
- **VIII. Prepositional Preference** (65%): Replace verbose constructions with concise prepositional forms

**Recommendation**: Start with Section V, then I-IV for edge cases, VIII for style enhancement.

---

## I. Spatial Prepositions
[← Quick Reference #1 | Priority: P0]

**Core Patterns** (90%):
- **at** (point): *at the door, at 123 Main St, at the conference, at school*
- **on** (surface): *on the table, on the bus, on Elm Street, on the screen*
- **in** (enclosed): *in the room, in Tokyo, in the database, in the system*

```
✓ at the station (point) | on the table (surface) | in Tokyo (area)
✗ in the station (unless inside building)
```

**Advanced**: between (2) vs among (3+) | above (higher) vs over (covering) | below vs under (directly beneath)

---

## II. Temporal Prepositions
[← Quick Reference #2 | Priority: P0]

**Core Patterns** (85%):
- **at** (specific time): *at 3 PM, at noon, at the moment, at 25 (age), **at night***
- **on** (days/dates): *on Monday, on July 4th, on my birthday, on Monday morning*
- **in** (longer periods): *in 2024, in January, in summer, in the morning, in two hours*

```
✓ at 9 AM | on Friday | in March | **at night** (exception)
✗ in 9 AM | in Friday | on March
```

**Duration/Deadline**: for (how long) | during (when) | since (start point) | by (deadline) | until (continuing)

---

## III. Directional Prepositions
[← Quick Reference #3 | Priority: P2]

**Core Patterns** (70%):
- **to** (destination): *go to the office, send to client, from 1 to 10*
- **toward** (direction, not arrival): *walk toward the exit, moving toward a solution*
- **into** (entering/transformation): *step into the room, turn into ice, translate into Chinese*
- **from** (origin): *come from, stem from research, from 9 to 5*
- **through** (passage/means): *drive through tunnel, learn through practice*

```
✓ go to the office | walk toward the door | step into the room | come from Tokyo
✗ go at the office | walk to the door (if not arriving)
```

---

## IV. Abstract Prepositions
[← Quick Reference #4-7 | Priority: P2]

**Purpose**: Understand semantic meaning for non-collocation cases. For fixed pairs, see Section V.

**Semantic Patterns** (75%):
- **about** (topic/approximate): *talk/think/worry about*, *about $100*
- **on** (formal topic/focus): *lecture/presentation/paper on*, *focus/concentrate on*
- **of** (belonging/composition): *CEO of company*, *consist/composed of*, *matter of time*
- **for** (purpose/beneficiary/duration): *designed/built for*, *work for company*, *for two hours*
- **with** (accompaniment/tool/manner): *work with team*, *build with Python*, *agree/consistent with*

```
✓ talk about the project (general) | lecture on AI (formal)
✓ consists of modules (composition) | designed for testing (purpose)
✗ focus at → focus on
```

---

## V. Fixed Collocations
[← Quick Reference #9-11 | Priority: P0]

**Verb+Preposition** (80%):
- depend **on**, consist **of**, listen **to**, focus **on**
- look **at** (observe), look **for** (search), look **after** (care)
- participate **in**, apologize **for**, wait **for**, belong **to**, arrive **at** (place) / **in** (city/country)

**Adjective+Preposition** (75%):
- good/bad **at**, interested **in**, capable **of**, responsible **for**, familiar **with**
- different **from** (US) / **to** (UK), afraid **of**, proud **of**, similar **to**, satisfied **with**

**Noun+Preposition** (70%):
- solution/answer **to**, reason **for**, impact/effect/influence **on**
- difference **between** (2) / **among** (3+), relationship **between/with**, knowledge **of**, expertise **in**

**Common Errors**: ~~depends of~~ → depends on | ~~good in~~ → good at | ~~solution of~~ → solution to | ~~impact to~~ → impact on | ~~arrive to~~ → arrive at/in

---

## VI. Idiomatic Expressions
[← Quick Reference #13-15 | Priority: P2]

**Time** (60%): *at first* (initially), *at last* (finally), *in the end* (outcome), *on time* (punctual), *in time* (before too late), *in advance*, *ahead of time*, *for the time being*, *at the moment*

**Manner**: *by accident*, *on purpose*, *in detail*, *in general*, *by hand*, *by machine*, *in secret*, *in public*

**Degree**: *to some extent*, *by far*, *at least*, *at most*, *on average*

**State**: *in progress*, *in development*, *in production*, *out of order* (broken), *out of service*, *under control* (not ~~in control~~), *in favor of*

---

## VII. Efficiency Patterns
[← Quick Reference #8, #12, #14 | Priority: P1 - Context-dependent]

**Register Note**: Formal (apply all) | Casual (optional, colloquially acceptable)

**A. Verbose → Concise** (70%):
- ~~in terms of~~ → (omit/rephrase) | ~~with regard to~~ → about/regarding | ~~in the event of~~ → if
- ~~for the purpose of~~ → to/for | ~~by means of~~ → by/using | ~~in order to~~ → to
- ~~at this point in time~~ → now/currently | ~~due to the fact that~~ → because/since
- ~~in spite of the fact that~~ → although/despite | ~~during the course of~~ → during
- ~~in the process of~~ → verb+-ing | ~~a large number of~~ → many | ~~in close proximity to~~ → near

**B. Redundant → Eliminate**:
- ~~where...at~~ → where | ~~inside of~~ → inside | ~~off of~~ → off | ~~outside of~~ → outside

**C. Transitive Verbs (no preposition)**:
- *discuss* (not ~~discuss about~~) [Formal: required | Casual: dialectal acceptable]
- *enter* room (not ~~enter into~~) [Universal except "enter into agreement"]
- *reach* conclusion (not ~~reach to~~) [Universal]
- *marry* someone (not ~~marry with~~) [Universal]

---

## VIII. Prepositional Preference Patterns (Style Enhancement)
[Priority: P3 - Optional]

**Purpose**: Replace verbose constructions with concise prepositional forms.

**Application**: Formal (consistently) | Casual (when improves naturalness)

### A. Temporal (During, At, Within, Throughout, Over)
```
...while system was processing → ...during data processing
...when sprint ends → ...at sprint end
...after 24 hours have passed → ...within 24 hours
```

### B. Conditional (Under, With, Without, Given)
```
System fails when there is heavy load → System fails under heavy load
API works if you have valid credentials → API works with valid credentials
Authentication fails if no tokens → Authentication fails without tokens
```

### C. Manner & Means (Through, Via, By, Using)
```
Users authenticate by using OAuth → Users authenticate through/via OAuth
System achieves scalability by means of load balancing → System achieves scalability through load balancing
Data flows by passing through gateway → Data flows through gateway
```

### D. Purpose & Reason (For, Due to, Because of, Based on)
```
Optimized code in order to improve performance → Optimized code for performance improvement
Made changes because users gave feedback → Made changes based on user feedback
Errors increased because load was high → Errors increased due to high load
```

### E. Location & Context (In, At, On, Within, Across)
```
Bug exists in the place where authentication happens → Bug exists in the authentication layer
Data stored in area of database cluster → Data stored within database cluster
Feature available on every platform → Feature available across all platforms
```

### F. Causation & Result (From, Out of)
```
Issue stems from the fact that concurrency was mishandled → Issue stems from concurrency mishandling
Crash resulted from system running out of memory → Crash resulted from memory exhaustion
```

### G. State & Condition (In, Under, At)
```
System is currently being developed → System is in development
Service is not working right now → Service is out of service
Application is controlled properly → Application is under control
```

### H. Comparison & Contrast (Unlike, Compared to, Against, Versus)
```
REST is different from WebSockets in that it's stateless → Unlike WebSockets, REST is stateless
PostgreSQL has better transactions when you compare to MongoDB → PostgreSQL has better transactions compared to MongoDB
```

### Decision Guide

**Evaluation**: Q1: More concise? → Q2: Preserves meaning? → Q3: Sounds natural? → Q4: Equally clear? → Use prepositional

**Quick Rules**:
- **Always prefer**: Shorter, clearer, equally precise
- **Usually prefer**: Formal writing and standard prepositional form
- **Sometimes prefer**: Improves flow without losing emphasis
- **Keep non-prepositional**: Provides necessary detail/emphasis or sounds forced

---

## Examples with Pattern Analysis

**Example 1: Collocation Errors (P0)**
```
✗ The meeting starts in Monday. We'll discuss about features. The team is good in React.
```
**Analysis**: ~~in Monday~~ → on Monday (P0 temporal) | ~~discuss about~~ → discuss (P1) | ~~good in~~ → good at (P0 adj+prep)

**Formal**: The meeting starts on Monday. We'll discuss features. The team is good at React. [2 P0 + 1 P1 fixed]  
**Casual**: The meeting starts on Monday. We'll discuss about features. The team is good at React. [P0 only fixed]

---

**Example 2: Conciseness (P1)**
```
✗ In terms of performance, the system is slow due to the fact that we have many queries.
```
**Analysis**: "In terms of" → verbose (P1) | "due to the fact that" → verbose (P1) | No P0 errors

**Formal**: The system performs poorly because we have many queries. [P1 applied]  
**Casual**: In terms of performance, the system is slow due to the fact that we have many queries. [P1 preserved]

---

**Example 3: Mixed P0 + P1**
```
✗ We need to discuss about the solution of this problem. The issue is different than expected. 
In the event of failure, retry. Where's the file at? Success depends of many factors.
```
**Errors**: 3 P0 (~~solution of~~ → solution to, ~~different than~~ → different from, ~~depends of~~ → depends on) + 3 P1 (~~discuss about~~, ~~In the event of~~, ~~where...at~~)

**Formal**: We need to discuss the solution to this problem. The issue differs from what we expected. If it fails, retry. Where's the file? Success depends on many factors. [All 6 fixed]  
**Casual**: We need to discuss about the solution to this problem. The issue is different from what we expected. In the event of failure, retry. Where's the file at? Success depends on many factors. [P0 only fixed]

---

**Example 4: P0 + P1 + P3**
```
✗ We need to discuss about the solution of performance issues. The system is good in handling requests, 
but it fails when there is heavy load. In terms of optimization, we'll implement caching by using Redis.
```
**Errors**: P0 (~~solution of~~ → solution to, ~~good in~~ → good at) | P1 (~~discuss about~~, ~~In terms of~~) | P3 opportunities (~~when there is heavy load~~ → under heavy load, ~~by using~~ → via)

**Formal**: We need to discuss the solution to performance issues. The system is good at handling requests, but it fails under heavy load. For optimization, we'll implement caching via Redis. [3 P0 + 1 P1 + 2 P3]  
**Casual**: We need to discuss about the solution to performance issues. The system is good at handling requests, but it fails when there is heavy load. In terms of optimization, we'll implement caching by using Redis. [P0 only]

---

## Summary

**Type**: Reference + post-check tool | **Mode** *(Default: Casual)*: Formal (P0+P1+P2) | Casual (P0 only)

**Fast Start**: Mode Selection → Cheat Sheet (20 top errors) → Quick Reference (11 patterns, 80% coverage) → Decision Tree

**Categories**: Spatial • Temporal • Direction • Abstract • Collocations • Idioms • Efficiency • Prepositional Preference

**Structure**: By Logic (Spatial, Temporal, Direction, Abstract) | By Word Type (Fixed Collocations) | Special (Idioms, Efficiency, Prepositional Preference)

**Coverage**: ~90% with Cheat Sheet + Quick Reference

**Priority**: P0 (Universal grammatical correctness) | P1 (Formal clarity/conciseness) | P2 (Formal sophistication) | P3 (Optional prepositional preference)

**Principle**: Preserve meaning, enhance clarity and naturalness

**Usage**: Select mode → Cheat Sheet → Quick Reference → Post-Check Workflow → Sections I-VIII (edge cases)

