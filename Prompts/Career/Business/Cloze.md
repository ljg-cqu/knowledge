# Cloze: Business-Architecture Mapping

Generate 24–40 cloze items testing business-to-architecture translation for senior technical leaders (5+ years).

---

## Task

**Scope**: 4–6 MECE clusters testing business-to-architecture terminology.

**Clusters**: Strategic Modeling | Value & Risk Analysis | Organizational Dynamics | Architectural Translation | Evolution & Adaptation

**Format**: 
- 1 blank (`___`) = primary + variants (synonyms, spellings, abbreviations); case-insensitive, trimmed
- Rationale: [Concept] + [Architectural impact] + [≥1 citation: [Ref: ID]]

**Difficulty** (MECE):
- Foundational (20%): Standard terms (Business Model Canvas, Conway's Law)
- Intermediate (40%): Framework application, pattern recognition  
- Advanced (40%): Trade-offs, context adaptations

---

## Requirements

### References (4 sections, cite as [Ref: ID])

| Section | Min | Criteria |
|---------|-----|----------|
| **Glossary** (G#) | 10 | Terms + architectural impacts; [Language Tag] |
| **Tools** (T#) | 5 | ≥10K users; URL + metrics |
| **Literature** (L#) | 6 | Peer-reviewed or practitioner-recognized |
| **APA Citations** (A#) | 12 | APA 7th + [Tag]; ~60% EN, ~30% ZH, ~10% other |

### Quality Gates (100% compliance)

| Gate | Target |
|------|--------|
| Citation Coverage | ≥70% items: ≥1 citation; ≥30% items: ≥2 citations |
| Recency | ≥50% ≤3 years (≥70% for cloud/AI/microservices) |
| Source Diversity | ≥3 types; <25% from single source; ≥3 regions |
| Business-Architecture Mapping | ≥70% items |
| Link Integrity | 100% URLs accessible/archived; all [Ref: ID] resolve |
| MECE | Zero overlap; complete coverage |

### Answer Validation

**Primary**: Canonical terms from authoritative sources  
**Variants**: Regional spellings, historical terms, abbreviations  
**Borderline**: Include if ≥2 sources (5-year window); document rationale  
**Conflicts**: Include all recognized variants; note version if terminology changed

---

## Process

### 1. Plan
Select 4–6 MECE clusters; 4–8 items/cluster; 20/40/40 difficulty per cluster; ensure total items 24–40.

### 2. Collect References
Gather sources meeting minimums and quality gates.

### 3. Generate Items
Per item:
- **Draft**: Unambiguous blank with expert context
- **Answers**: Primary + variants (≥2 sources, 5-year window)
- **Rationale**: Concept + architectural link + ≥1 [Ref: ID]
- **Review** (every 5): ambiguity, completeness, citations, difficulty

### 4. Compile References
Populate sections; verify [Ref: ID] resolution; archive unstable URLs.

### 5. Validate
100% checklist compliance before delivery.

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

**Rationale:** Business Model Canvas [Ref: G1] uses 9 blocks (Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure) to trace business decisions to technical requirements [Ref: A1].

---

#### Item 2: When shifting from perpetual licensing to SaaS, the ___ building block changing from upfront to recurring drives multi-tenancy requirements.

**Difficulty:** Intermediate

**Acceptable Answers:**
- Revenue Streams
- Revenue Stream
- Revenue

**Rationale:** Recurring Revenue Streams [Ref: G1] create cost pressure for efficiency, driving multi-tenancy for shared infrastructure with data isolation [Ref: A7].

---

### Topic 2: Value & Risk Analysis

...

---

## References

### Glossary

**G1. Business Model Canvas (BMC)**: 9-block framework mapping business models to technical requirements. [EN]

**G2. Conway's Law**: Organizations design systems mirroring communication structures; silos → monoliths, cross-functional teams → microservices. [EN]

...

---

### Tools

**T1. Miro**: Visual collaboration for BMC; 80M+ users; https://miro.com [EN]

...

---

### Literature

**L1. Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.** [EN]

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
| Citations (≥1) | ≥70% | [%] | ✅/❌ |
| Citations (≥2) | ≥30% | [%] | ✅/❌ |
| Language EN | 50–70% | [%] | ✅/❌ |
| Language ZH | 20–40% | [%] | ✅/❌ |
| Recency ≤3yr | ≥50% | [%] | ✅/❌ |
| Source Types | ≥3 | [N] | ✅/❌ |
| Business-Architecture Mapping | ≥70% | [%] | ✅/❌ |
| URLs Accessible | 100% | [%] | ✅/❌ |
| Refs Resolve | 100% | [%] | ✅/❌ |
| MECE | Pass | [Pass/Fail] | ✅/❌ |

**Notes**: [Deviations, borderline cases, recommendations]

---

## Examples

**Foundational**: The ___ framework uses 9 building blocks to map business models to technical requirements.  
Answers: Business Model Canvas | BMC  
Rationale: BMC [Ref: G1] uses 9 blocks [Ref: A1] to trace business to technical requirements.

**Intermediate**: When shifting from perpetual licensing to SaaS, the ___ building block changing from upfront to recurring drives multi-tenancy.  
Answers: Revenue Streams | Revenue Stream | Revenue  
Rationale: Recurring Revenue Streams [Ref: G1] create cost pressure, driving multi-tenancy [Ref: A7].

**Advanced**: Per Conway's Law, restructuring from functional silos to cross-functional teams shifts architecture from ___ to microservices.  
Answers: monolithic architecture | monolith | monolithic system | layered monolith | modular monolith  
Rationale: Conway's Law [Ref: G2]: silos → layered monoliths [Ref: L4]; cross-functional teams → microservices [Ref: A6], showing org structure driving architecture [Ref: L5].
