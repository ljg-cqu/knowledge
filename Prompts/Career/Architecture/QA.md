# Software Architecture Interview Q&A Generator

**Problem**: Candidates struggle translating architecture concepts to practical code, reducing hiring quality due to hallucinations.

**Scope**: Generate 5 Q&A pairs for senior/architect roles, focusing on architecture-to-code translation.

**Constraints**: Idiomatic code in common languages.

**Assumptions**: Familiarity with software architecture concepts.

**Audience**: Senior developers, architects.

**Output**: 5 Q&As across 5 dimensions with code, quantified trade-offs, ≥2 alternatives, citations.

**Success**: All validation checks pass.

---

## Requirements

### Specifications
- **Count**: 5 (1 per dimension)
- **Difficulty**: 50% Foundational / 50% Advanced
- **Answer Length**: 150-300 words (code excluded)
- **Components**: Pattern, rationale, code, trade-offs, metrics
- **Citations**: ≥1 each; ≥2 for advanced

### Dimensions (5, 1 Q&A Each)
1. **Structural**: Decomposition, modularity (hexagonal, layers)
2. **Behavioral**: Events, orchestration (saga, circuit breaker)
3. **Quality**: Performance, scalability (rate limiting, encryption)
4. **Data**: Persistence, consistency (CQRS, sharding)
5. **Integration**: APIs, protocols (REST, gRPC)

### Standards
- **Trade-offs**: Quantified, e.g., "CQRS: 10x read, +20-40ms write"
- **Perspectives**: ≥2 alternatives with table; assumptions/limitations; tags `[Consensus]`/`[Context-dependent]`
- **Language**: Define terms; concrete metrics; minimal jargon

### Artifacts
- **Diagram**: Mermaid (<120 nodes)
- **Code**: 10-30 lines, production-ready
- **Table**: ≥2 alternatives (Approach/Pros/Cons/Use When/Consensus)
- **Metric**: Formula + variables + target

### References
- **Glossary**: ≥5 terms
- **Tools**: ≥3 (valid URLs, recent updates)
- **Literature**: ≥3 books
- **Citations**: ≥6 APA 7th, ≥2 languages

---

## Process

1. Select 5 dimensions, 50/50 difficulty mix
2. Build references meeting thresholds
3. Write Q&As with required components
4. Create artifacts per dimension
5. Validate counts, citations, recency, links

**Failure**: Fix and re-validate until pass

---

## Output Template

```markdown
## Contents
[TOC]

## Topic Areas
| Dimension | Count | Difficulty |
| [Type] | 1 | F/A |
[5 total]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences]

### Q1: [Question]
**Difficulty**: [F/A] | **Dimension**: [Type]

**Key Insight**: [Quantified trade-off]

**Answer**: [150-300 words: Context, pattern, trade-offs, metrics] [Citation]

**Implementation** ([Language]):
```[language]
// Code
```

**Diagram**:
```mermaid
[Diagram]
```

**Metrics**:
| Metric | Formula | Variables | Target |

**Trade-offs**:
| Approach | Pros | Cons | Use When | Consensus |
[≥2 rows]

---

## References

### Glossary (≥5)
**G1. [Term]** – [Definition]. Related: [Terms]

### Tools (≥3)
**T1. [Tool]** – [Purpose]. Updated: [Date]. URL: [Link]

### Literature (≥3)
**L1. Author. (Year). *Title*.** – [Relevance]

### Citations (≥6)
**A1.** Author. (Year). *Title*. [Language]

---

## Validation
| Check | Target | Status |
| Counts | G≥5, T≥3, L≥3, A≥6, Q=5 | PASS/FAIL |

**Overall**: [Pass rate]
```

## Limitations
- Trade-offs: Rigor vs. speed
- Skip for: Low-stakes decisions
- Exclude: Pure theory, speculation