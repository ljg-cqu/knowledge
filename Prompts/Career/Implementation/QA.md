# Software Implementation Interview Q&A Generator

**Goal**: 7-10 Q&As across 7 dimensions (1-2 per dimension, focus on I/A)
**Quality Gate**: Code runs + Tests pass + Metrics quantified

## 7 Dimensions
1. Algorithms & Data Structures
2. Concurrency & Parallelism
3. Performance & Optimization
4. Testing & Quality
5. Debugging & Troubleshooting
6. Code Quality & Refactoring
7. Dependencies & Tech Stack

## Per Q&A: 4 Artifacts
1. **Code** (20-50 lines): Runnable with error handling
2. **Tests** (10-30 lines): Table-driven + edge cases
3. **Benchmarks**: Time/Space/ops/sec/Allocs
4. **Analysis Table**: ≥2 approaches with trade-offs

## Validation Essentials
- Syntax: 100% compiles
- Tests: 100% pass
- Metrics: Quantified (e.g., "O(1), 8B/entry, 75% load" not "fast")

## Template
```markdown
## Q[N]: [Action Verb + Task]
**Difficulty**: [F/I/A] | **Dimension**: [1-7]
**Answer**: Problem → Approach → Code → Metrics → Edge cases
**Code**: [runnable]
**Tests**: [edge cases]
**Benchmarks**: | Approach | Time | Space | ops/sec | Allocs |
**Analysis**: | Approach | Pros | Cons | Context |
```
