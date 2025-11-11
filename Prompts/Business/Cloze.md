# Cloze: Business-Architecture Mapping

Generate fill-in-the-blank assessments (24–40 items) testing how senior technical leaders (5+ years) translate business concepts to architectural decisions.

---

## Task

**Context**: Create unambiguous cloze items with `___` blanks testing business-to-architecture terminology across 4–6 mutually exclusive, collectively exhaustive topic clusters.

**Clusters**: Strategic Modeling | Value & Risk Analysis | Organizational Dynamics | Architectural Translation | Evolution & Adaptation

**Constraints**: 
- Case-insensitive matching; trim whitespace; strip punctuation
- Each item: 1 blank = 1 primary answer + variants (synonyms, regional spellings, abbreviations)
- Rationale format: [Concept] + [Architectural implication] + [≥1 citation as [Ref: ID]]

**Difficulty** (mutually exclusive, collectively exhaustive):
- Foundational (20%): Industry-standard terms (Business Model Canvas, Conway's Law)
- Intermediate (40%): Framework application, pattern recognition  
- Advanced (40%): Strategic trade-offs, context-specific adaptations

---

## Requirements

### References (4 sections with inline citations [Ref: ID])

| Section | Min | Criteria |
|---------|-----|----------|
| **Glossary** (G#) | 10 | Industry terms + architectural implications; [Language Tag] |
| **Tools** (T#) | 5 | ≥10K users; URL + adoption metrics |
| **Literature** (L#) | 6 | Books/journals/reports; peer-reviewed or practitioner-recognized |
| **APA Citations** (A#) | 12 | APA 7th + [Language Tag]; ~60% EN, ~30% ZH, ~10% other |

### Quality Gates (100% compliance required)

| Gate | Target |
|------|--------|
| Citation Coverage | ≥70% items have ≥1 citation; ≥30% have ≥2 |
| Recency | ≥50% published ≤3 years (≥70% for cloud-native/AI/microservices) |
| Source Diversity | ≥3 types; no single source >25%; ≥3 geographic regions |
| Business-Arch Mapping | ≥70% items test business-to-architecture translation |
| Link/Reference Integrity | 100% URLs accessible/archived; all [Ref: ID] resolve to G#/T#/L#/A# |
| MECE | Zero cluster overlap; complete domain coverage |

### Answer Validation

**Primary**: Canonical terms from authoritative sources  
**Variants**: Regional (US/UK English), historical terms, abbreviations  
**Borderline**: Include if ≥2 authoritative sources use within 5 years; document rationale  
**Conflicts**: Include all recognized variants; specify framework version if terminology changed significantly

---

## Process

### 1. Plan (MECE topology)
Select 4–6 clusters; allocate 4–8 items/cluster; apply 20/40/40 difficulty distribution per cluster.

### 2. Collect References
Gather authoritative, diverse, recent sources meeting minimums and quality gates above.

### 3. Generate Items
For each:
- **Draft**: Single unambiguous blank with sufficient expert context
- **Acceptance List**: Primary + variants from ≥2 authoritative sources (5-year window)
- **Rationale**: Concept + architectural link + ≥1 [Ref: ID]
- **Review** every 5 items: ambiguity, acceptance completeness, citations, difficulty tier

### 4. Compile References
Populate sections with consistent IDs; verify all [Ref: ID] resolve; archive unstable URLs (Wayback Machine).

### 5. Validate
Self-review 100% checklist compliance before delivery.

---

## Output Structure

```markdown
## Table of Contents
- [Item Bank](#item-bank): [Topic 1](#topic-1-strategic-modeling) | [Topic 2](#topic-2-value--risk-analysis) | ...
- [References](#references): [Glossary](#glossary) | [Tools](#tools) | [Literature](#literature) | [APA](#apa-citations)
- [Validation](#validation-summary)

---

## Item Bank

### Topic 1: Strategic Modeling

#### Item 1: The ___ framework uses 9 building blocks to map business models to technical requirements.

**Difficulty:** Foundational

**Acceptable Answers:**
- Business Model Canvas
- BMC

**Rationale:** Business Model Canvas [Ref: G1] analyzes business model changes through 9 building blocks (Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure), enabling architects to trace business decisions to technical requirements [Ref: A1].

---

#### Item 2: When shifting from perpetual licensing to SaaS, the ___ building block changing from upfront to recurring drives multi-tenancy requirements.

**Difficulty:** Intermediate

**Acceptable Answers:**
- Revenue Streams
- Revenue Stream
- Revenue

**Rationale:** Revenue Streams [Ref: G1] defines income generation. Recurring revenue creates cost pressure for infrastructure efficiency, driving multi-tenancy for shared infrastructure with data isolation [Ref: A7].

---

### Topic 2: Value & Risk Analysis

...

---

## References

### Glossary

**G1. Business Model Canvas (BMC)**: 9-block framework (Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure) mapping business models to technical requirements. [EN]

**G2. Conway's Law**: Organizations design systems mirroring their communication structures; functional silos produce layered monoliths, cross-functional teams produce microservices. [EN]

...

---

### Tools

**T1. Miro**: Visual collaboration for Business Model Canvas; 80M+ users; https://miro.com [EN]

...

---

### Literature

**L1. Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.** Business model analysis framework. [EN]

...

---

### APA Citations

**A1. Osterwalder, A., & Pigneur, Y. (2010). *Business model generation: A handbook for visionaries, game changers, and challengers*. John Wiley & Sons. [EN]**

...

---

## Validation Summary

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Items | 24–40 | [N] | ✅/❌ |
| Foundational | 20% (±5%) | [%] | ✅/❌ |
| Intermediate | 40% (±5%) | [%] | ✅/❌ |
| Advanced | 40% (±5%) | [%] | ✅/❌ |
| Glossary | ≥10 | [N] | ✅/❌ |
| Tools | ≥5 | [N] | ✅/❌ |
| Literature | ≥6 | [N] | ✅/❌ |
| APA | ≥12 | [N] | ✅/❌ |
| Citation Coverage (≥1) | ≥70% | [%] | ✅/❌ |
| Citation Coverage (≥2) | ≥30% | [%] | ✅/❌ |
| Language EN | 50–70% | [%] | ✅/❌ |
| Language ZH | 20–40% | [%] | ✅/❌ |
| Recency ≤3yr | ≥50% | [%] | ✅/❌ |
| Source Types | ≥3 | [N] | ✅/❌ |
| Business-Arch Mapping | ≥70% | [%] | ✅/❌ |
| URLs Accessible | 100% | [%] | ✅/❌ |
| References Resolve | 100% | [%] | ✅/❌ |
| MECE | Pass | [Pass/Fail] | ✅/❌ |

**Notes**: [Deviations, borderline cases, recommendations]
```

---

## Examples

**Foundational**: The ___ framework uses 9 building blocks to map business models to technical requirements.  
Answers: Business Model Canvas | BMC  
Rationale: BMC [Ref: G1] analyzes business changes through 9 blocks [Ref: A1], tracing business decisions to technical requirements.

**Intermediate**: When shifting from perpetual licensing to SaaS, the ___ building block changing from upfront to recurring drives multi-tenancy.  
Answers: Revenue Streams | Revenue Stream | Revenue  
Rationale: Recurring Revenue Streams [Ref: G1] create cost pressure, driving multi-tenancy for shared infrastructure [Ref: A7].

**Advanced**: Per Conway's Law, restructuring from functional silos to cross-functional teams shifts architecture from ___ to microservices.  
Answers: monolithic architecture | monolith | monolithic system | layered monolith | modular monolith  
Rationale: Conway's Law [Ref: G4]: functional silos produce layered monoliths (horizontal layers) [Ref: L4]; cross-functional teams produce microservices (vertical capabilities) [Ref: A6], showing organizational structure driving architecture [Ref: L5].
