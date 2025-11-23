# Stance & Certainty Language for Natural English

**Type**: Dual-purpose - Supporting reference AND standalone post-check/improvement tool

**Task**: Enhance English content with precise stance and certainty markers to achieve appropriate academic hedging, accurate claim strength, and native-like fluency in technical/academic contexts.

**Definition**: Systematically calibrate the strength of claims, assertions, and statements using hedging, modals, and qualifiers to achieve the appropriate balance between confidence and caution.

## Precision Principle

**Critical**: Stance markers express **degree of certainty** without changing **factual content**.

**Rules**:
- **Preserve all factual content** from the original text
- Never add ungrounded claims or exaggerate certainty
- Match claim strength to evidence level
- Avoid over-claiming (too strong) and over-hedging (too weak)
- Balance confidence with academic humility

**Example**:
```
Before: The system is faster. [too absolute without evidence]
After:  The system appears faster. [appropriate hedging]
        The system is 30% faster. [evidence-backed, can be absolute]
```

---

## Quick Reference: Top 12 Patterns (80% Coverage)

**Most frequent patterns covering 80% of academic hedging needs. Percentages = usage frequency in technical/academic writing.**

1. **Modal: Possibility** (90%) | *may, might, could, can* - uncertain outcomes | [→ I.A]
2. **Modal: Necessity** (85%) | *should, must, need to* - obligation/recommendation | [→ I.B]
3. **Modal: Hypothetical** (75%) | *would, could* - conditional scenarios | [→ I.C]
4. **Hedging Verbs** (80%) | *appears, seems, tends to, suggests* - softening claims | [→ II.A]
5. **Probability Adverbs** (70%) | *probably, possibly, likely, presumably* - likelihood | [→ II.B]
6. **Degree Qualifiers** (75%) | *relatively, fairly, reasonably* - moderate degree | [→ III.A]
7. **Extent Limiters** (65%) | *generally, typically, in some cases* - partial scope | [→ III.B]
8. **Intensifiers** (70%) | *significantly, substantially, notably* - strengthening | [→ IV.A]
9. **Certainty Expressions** (60%) | *clearly, evidently, consistently* - high confidence | [→ IV.B]
10. **Attribution** (65%) | *according to, research shows, based on* - sourcing | [→ V]
11. **Approximators** (70%) | *approximately, roughly, about, around* - imprecise values | [→ VI.A]
12. **Negative Hedging** (60%) | *not necessarily, rarely, seldom* - negating absolutes | [→ VI.B]

**→ 80% complete above. Continue for: Certainty Spectrum, comprehensive patterns (I-VI), post-check workflow.**

---

## Priority System

**Universal application order:**

- **P0 (Must fix)**: Over-claiming without evidence
  - ~~X is better~~ → X appears better / X is 30% better
  - ~~You can do this~~ (impossible) → You cannot / should not
  
- **P1 (High value)**: Excessive/insufficient hedging (#1-7, #10, #12)
  - Too weak: ~~might possibly perhaps~~ → possibly
  - Too strong: ~~definitely works~~ → works well / tends to work

- **P2 (Polish)**: Precise qualifiers and intensifiers (#6, #8-9, #11)
  - *significantly* vs *slightly* vs *substantially*
  - *arguably* vs *maybe*

---

## Certainty Spectrum

**Match language to evidence level:**

```
[No Evidence / Speculation]
   might, could possibly, may potentially
   ↓
[Weak Evidence / Observed Pattern]  
   seems to, appears to, tends to, suggests
   ↓
[Moderate Evidence / Qualified Claim]
   likely, probably, generally, typically
   ↓
[Strong Evidence / High Confidence]
   clearly, evidently, consistently, regularly
   ↓
[Definitive Evidence / Established Fact]
   is, does, will (use sparingly for absolutes)
```

**Calibration Examples**:
```
✗ Caching is always better. [too strong]
✓ Caching typically improves performance. [qualified]
✓ Caching reduced latency by 40% in tests. [evidence-backed]

✗ The approach might possibly work. [over-hedged]
✓ The approach could work. [appropriately hedged]

✗ The system appears to have 99.9% uptime. [don't hedge facts]
✓ The system has 99.9% uptime. [fact with evidence]
```

---

## Standalone Usage: Post-Check Workflow

**Purpose**: Audit existing content and calibrate claim strength after writing.

**Step 1: Scan** — Identify issues by priority
- **P0**: Absolute claims without evidence (*is, always, never, must*)
- **P1**: Missing hedges or double hedges (*might possibly*)
- **P2**: Imprecise qualifiers (*very* → *significantly*)

**Step 2: Fix** — Calibrate using Certainty Spectrum
- Add hedges to unqualified claims
- Remove excessive hedging
- Match intensity to evidence

**Step 3: Validate** — Quality checks
- ✓ Claims match evidence? ✓ Appropriate confidence? ✓ No over-claiming?

**→ For comprehensive patterns, continue to I-VI.**

---

## I. Modal Verbs

### A. Current Possibility/Ability
[← Quick Reference #1 | Priority: P0/P1]

**Weak Possibility** (20-50% confidence):
- *might* - speculation | *could* - possibility exists | *may* - formal possibility

**Strong Possibility/Ability** (60-80% confidence):
- *can* - general ability, current possibility | *should* - expected outcome

**Usage**:
```
✓ Optimization might improve performance. [untested speculation]
✓ Optimization should improve performance. [expected based on evidence]
✓ Caching can reduce latency. [demonstrated capability]

✗ System may potentially work. [redundant]
✓ System may work.
```

**Distinctions**:
- **can vs could**: can = current ability; could = hypothetical (see I.C)
- **may vs might**: may = formal (~50%); might = tentative (~30%)

---

### B. Necessity/Obligation
[← Quick Reference #2 | Priority: P0]

**Strong Obligation**: *must* - no alternative | *need to* - practical necessity

**Recommendation**: *should* - best practice | *ought to* - formal recommendation

**Weak Suggestion**: *could* - one option | *might want to* - gentle

**Usage**:
```
✓ You must validate input to prevent injection. [security requirement]
✓ You should add error handling. [best practice]
✓ You could consider Redis. [one option]

✗ You must consider optimization. [too strong for suggestion]
✓ You should consider optimization.
```

**must vs should**: must = absolute requirement; should = strong recommendation with flexibility

---

### C. Hypothetical/Conditional
[← Quick Reference #3 | Priority: P1]

**would** - hypothetical result | **could** - hypothetical possibility | **might/may** - uncertain outcome

**Usage**:
```
✓ If we added caching, latency would decrease. [hypothetical]
✓ Without optimization, the query would timeout. [counterfactual]
✓ We could use Redis, but PostgreSQL suffices. [option considered]
✓ A distributed approach might introduce consistency issues. [possible problem]

✗ This would improve performance. [needs condition]
✓ This would improve performance if implemented correctly.
```

---

## II. Hedging Devices

### A. Hedging Verbs
[← Quick Reference #4 | Priority: P1]

**Appearance**: *appears to, seems to* - observation needing confirmation

**Tendency**: *tends to, is prone to* - usual behavior

**Indication**: *suggests, indicates, implies* - evidence-based inference

**Belief**: *we believe, we assume, arguably, presumably* - judgment

**Usage**:
```
✓ System appears to have memory leaks. [needs confirmation]
✓ System has memory leaks. [confirmed with evidence]

✓ Redis tends to outperform Memcached for complex data. [general pattern]
✓ Data suggests correlation between X and Y. [evidence-based]

✗ It seems possibly related. [double hedge]
✓ It seems related.
```

---

### B. Probability Adverbs
[← Quick Reference #5 | Priority: P1]

**High** (70-90%): *probably, likely, presumably*

**Moderate** (40-60%): *possibly, perhaps, potentially*

**Low** (10-30%): *unlikely, improbably*

**Usage**:
```
✓ Optimization will probably improve performance. [expected]
✓ Refactoring could possibly introduce bugs. [acknowledging risk]
✓ Horizontal scaling is unlikely to solve this. [low probability]

✗ System is probably possibly slow. [redundant]
✓ System is probably slow.
```

**Positioning**: Before verb or sentence-initial with comma
```
✓ System probably needs optimization.
✓ Probably, the system needs optimization.
✗ System needs probably optimization. [wrong]
```

---

## III. Qualifiers

### A. Degree Qualifiers
[← Quick Reference #6 | Priority: P2]

**Moderate Degree** (50-75%): *relatively, fairly, reasonably, moderately*

**Note**: *quite* = "very" (British) or "fairly" (American) - avoid ambiguity in academic writing

**Usage**:
```
✓ System is relatively fast compared to alternatives. [explicit comparison]
✓ Approach is fairly effective. [moderately effective]
✓ System responds in 50ms. [best - quantified]

✗ System is very fast. [vague]
✓ System is reasonably fast.
```

**relatively vs fairly**: relatively requires explicit comparison; fairly = absolute moderate degree

---

### B. Extent Limiters
[← Quick Reference #7 | Priority: P1]

**Partial Extent**: *to some extent, partially, in part*

**Conditional Scope**: *in some cases, under certain conditions, in specific situations*

**Frequency**: *generally, typically, usually, often, frequently, for the most part*

**Exceptions**: *with exceptions, not always, not necessarily*

**Usage**:
```
✓ Approach works in most cases. [acknowledging exceptions]
✓ Caching improves performance in many scenarios. [qualified scope]
✓ Generally, NoSQL databases scale horizontally. [allows exceptions]

✗ NoSQL always scales horizontally. [too absolute]

✗ Criticism is valid to some extent partially. [redundant]
✓ Criticism is partially valid.
```

**generally vs usually vs typically**: generally = broad statement; usually = frequency (>50%); typically = characteristic behavior

---

## IV. Intensifiers & Certainty

### A. Intensifiers
[← Quick Reference #8 | Priority: P2]

**Precision Spectrum**:
```
Small:      slightly, marginally, minimally
Moderate:   moderately, reasonably, fairly
Large:      significantly, substantially, considerably
Very Large: dramatically, drastically, remarkably, notably
```

**Usage**:
```
✓ Latency decreased slightly (5%). [small]
✓ Latency decreased significantly (40%). [large]
✓ Latency decreased dramatically (80%). [very large]
✓ Latency decreased by 40%. [best - quantified]

✗ System is very fast. [vague]
✓ System is significantly faster. [better]
✓ System is 3x faster. [best]
```

---

### B. Certainty Expressions
[← Quick Reference #9 | Priority: P0/P2]

**High Certainty**: *clearly, evidently, undoubtedly, certainly* - use sparingly, risks arrogance

**Established Fact**: *it is well-known, research has shown, consistently, reliably*

**Warning**: High-certainty markers risk arrogance, over-claiming, condescension

**Usage**:
```
✓ Data clearly shows correlation. [evident from data]
✗ Clearly, this is best. [arrogant]
✓ Evidence suggests this is effective. [better]

✓ Algorithm clearly runs in O(n log n). [proven fact]
✗ Obviously, React is better. [opinion stated as fact]
✓ React may be better suited for large apps. [qualified]
```

**When appropriate**: Established facts, mathematical truth, cited evidence
**When inappropriate**: Subjective judgment, opinions, unsupported claims

---

## V. Attribution & Sourcing

[← Quick Reference #10 | Priority: P1]

**Source Attribution**: *according to X, as X states, X suggests/indicates/shows*

**Research**: *research shows, studies demonstrate, evidence suggests*

**Team/Experience**: *we believe, based on our analysis, in our experience*

**Qualified Scope**: *as far as we know, to the best of our knowledge, preliminary results suggest*

**Usage**:
```
✓ According to documentation, Redis supports clustering. [cited]
✓ Research indicates caching reduces latency 30-50%. [sourced]
✓ Based on our benchmarks, PostgreSQL outperforms MySQL. [qualified]

✗ PostgreSQL is better. [unsupported]

✗ Studies show caching works. [vague]
✓ Multiple studies demonstrate caching reduces load [1][2][3]. [specific]
```

**Strength Spectrum**:
- Strong: *demonstrates, proves, shows* [empirical]
- Moderate: *suggests, indicates, implies* [interpretive]
- Weak: *hints at, raises questions, may point to* [speculative]

---

## VI. Additional Patterns

### A. Approximators
[← Quick Reference #11 | Priority: P2]

**Core Patterns**: *approximately, roughly, about, around, circa*

**Usage**:
```
✓ System handles approximately 1000 QPS. [~±5%]
✓ Response time is roughly 50ms. [imprecise measurement]
✓ Database contains about 10M records. [rounded estimate]
✓ Architecture dates to circa 2015. [historical approximation]

✗ System handles about approximately 1000 QPS. [redundant]
✓ System handles approximately 1000 QPS.
```

**When to use**: Measurements with uncertainty, rounded figures, estimates, historical dates

---

### B. Negative Hedging
[← Quick Reference #12 | Priority: P1]

**Negating Absolutes**: *not necessarily, not always, rarely, seldom, infrequently*

**Usage**:
```
✓ Caching does not necessarily improve performance. [conditions apply]
✓ NoSQL is not always the best choice. [context-dependent]
✓ Denormalization rarely solves scalability issues. [uncommon]

✗ Caching never improves performance. [too absolute]
✓ Caching rarely helps in this scenario. [qualified negative]
```

**not necessarily vs not always**: not necessarily = conditional/logical; not always = temporal/frequency

---

### C. Time-Based Hedging

**Temporal Qualifiers**: *currently, at present, traditionally, historically, recently*

**Usage**:
```
✓ System currently supports 1000 QPS. [may change]
✓ Microservices are currently popular. [trend-based]
✓ Waterfall was traditionally used. [past practice]

✗ System supports 1000 QPS. [implies permanent if capacity may change]
```

---

## Application Guidelines

**Common Over-Claiming**:
```
✗ X is always/never Y [use "typically" or "rarely"]
✗ X is the best/worst [use "most effective" with criteria]
✗ Everyone knows [cite source or use "well-established"]
✗ Obviously/clearly X [risks condescension - use "evidently" with care]
```

**Common Over-Hedging**:
```
✗ might possibly perhaps [use one]
✗ seems to appear to suggest [use one verb]
✗ could potentially maybe [use one modal]
```

**Evidence-Based Calibration**:
```
NO evidence:       might, could, possibly
WEAK evidence:     appears, seems, suggests, may
GOOD evidence:     likely, probably, typically
STRONG evidence:   shows, demonstrates, consistently
DEFINITIVE:        is, does, always (use sparingly)
```

---

## Examples

**Over-Claiming (P0)**:
```
✗ Caching is always faster. Everyone knows this works.
✓ Caching typically improves performance. It is well-established that caching reduces latency.
```

**Under-Hedging (P1)**:
```
✗ Algorithm is O(n²). Implementation is faster.
✓ Algorithm appears O(n²). Implementation tends to be faster for small inputs.
```

**Over-Hedging (P1)**:
```
✗ System might possibly perhaps work to some extent.
✓ System could work in many cases.
```

**Evidence-Based (P2)**:
```
✗ Optimization helps. It's faster.
✓ Optimization significantly improved performance—reducing latency from 500ms to 50ms in benchmarks. Based on results, this approach appears promising for similar workloads.
```

**Academic Stance (Comprehensive)**:
```
✗ Obviously caching fixes everything. It's the best solution. You must use Redis.

✓ Caching appears effective for this use case. Based on our analysis, Redis may be well-suited. We recommend evaluating caching as it typically improves performance 30-50% in similar scenarios. Results may vary by workload.
```

---

## Summary

**Framework**: 6 categories covering ~90% of stance/certainty patterns

**Categories**:
- **I. Modals**: Possibility, necessity, hypothetical (*may, should, would*)
- **II. Hedging**: Softening devices (*appears, probably, arguably*)
- **III. Qualifiers**: Degree and scope (*relatively, generally, in some cases*)
- **IV. Intensifiers**: Strengthening (*significantly, clearly, substantially*)
- **V. Attribution**: Sourcing (*research shows, based on, according to*)
- **VI. Additional**: Approximators, negative hedging, time-based (*roughly, not necessarily, currently*)

**80/20**: Quick Reference (12 patterns) + Certainty Spectrum = 80% coverage

**Priority**: P0 (accuracy) → P1 (appropriateness) → P2 (precision)

**Principle**: Calibrate certainty to evidence; avoid over-claiming and over-hedging
