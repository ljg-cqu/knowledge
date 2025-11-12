# Short Answer / Calculation

Generate 25–40 senior-level problems with worked solutions, citations, validation.

## Requirements

| Parameter | Specification |
|-----------|---------------|
| **Scope** | 25–40 problems; difficulty 20/40/40 (foundational/intermediate/advanced) |
| **Types** | Throughput, latency, gas costs, consensus, conversions, justifications (2–3 sentences) |
| **Answers** | Value + units + tolerance (±%); 2–4 step solution; LaTeX/KaTeX supported |
| **Sources** | ~60% EN, ~30% ZH, ~10% other; APA 7th; authoritative + peer-reviewed + audited |
| **Grading** | Normalize input; tolerances; partial credit: 70% (method), 50% (setup) |
| **Quality** | Real-world scenarios; explicit assumptions/constraints; flag uncertainty; alternatives |

## Reference Floors

| Section | Min | Requirements |
|---------|-----|--------------|
| Glossary | ≥10 | Core concepts; `**G#: Term**: Definition [Lang]` |
| Codebase | ≥5 | License + updated ≤12mo + stable + audit status |
| Literature | ≥6 | Standards, peer-reviewed; formulas, benchmarks, methodology |
| APA | ≥12 | Language ~60/30/10; persistent links (DOIs, archived URLs) |

**Citation**: `[Ref: ID]` (G#/C#/L#/A#). **Exception**: State shortfall + rationale + plan.

## Quality Gates

| Gate | Pass Criteria |
|------|---------------|
| Recency | ≥50% last 3yr (≥70% AI/security) |
| Diversity | ≥3 types; no source >25% |
| Coverage | ≥70% problems cite ≥1; ≥30% cite ≥2 |
| Links | All resolve or archived |
| Cross-Refs | All `[Ref: ID]` resolve |

**Scaling**: >40 problems or regulated → floors ×1.5

## Workflow

### 1. Plan Topics
- 4–6 clusters; 4–7 problems/cluster → 25–40 total; difficulty 20/40/40
- **Verify**: Total = 25–40, difficulty ≈20/40/40

### 2. Collect References
- Gather ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA
- Tag language ([EN]/[ZH]), year, type; assign IDs (G#/C#/L#/A#)
- **Verify**: Floors met, language ≈60/30/10, recency ≥50% 3yr, diversity ≥3 types

### 3. Generate Problems
- Clear statement (values, units, difficulty, type, assumptions/constraints)
- ≥1 `[Ref: ID]` in solution; answer + units + tolerance + 2–4 steps + uncertainty + risk/value
- **Verify every 5**: Completeness, tolerances, units, citations, assumptions

### 4. Document Grading
- Alternative forms (units, expressions, normalized values)
- Partial credit (70% method, 50% setup); common mistakes
- **Verify**: All have rubrics + alternatives

### 5. Compile References
- Populate Glossary, Codebase, Literature, APA
- Required fields (maturity, methodology, impact); verify `[Ref: ID]` resolve
- Check APA 7th + language tags + persistent links

### 6. Validate (ALL 12 steps)

1. **Counts**: `G: X (≥10) | C: Y (≥5) | L: Z (≥6) | A: W (≥12) | Problems: N (F/I/A)` → Pass: Floors met, difficulty ≈20/40/40
2. **Coverage**: `X of Y cite ≥1 (Z%); W cite ≥2 (V%)` → Pass: ≥70% cite ≥1, ≥30% cite ≥2
3. **Language**: `EN: X (Y%) | ZH: A (B%) | Other: C (D%)` → Pass: EN ≈50-70%, ZH ≈20-40%, Other ≈5-15%
4. **Recency**: `X of Y (Z%) from 2022-2025` → Pass: ≥50% (≥70% AI/security)
5. **Diversity**: `T1: X | T2: Y | T3: Z | T4: W | Types: N | Max: M (P%)` → Pass: ≥3 types, no source >25%
6. **Links**: `Tested X: Y ok, Z broken` → Pass: All ok OR archived
7. **Cross-Refs**: `X refs: Y ok, Z broken` → Pass: Z=0
8. **Solutions**: `X of Y complete; Z incomplete` → Pass: Z=0
9. **Tolerances**: `X of Y have; Z missing` → Pass: Z=0
10. **Units**: `X of Y consistent; Z inconsistent` → Pass: Z=0
11. **Conflicts**: `X apply; Y comply (Z%)` → Pass: ≥80% OR rationale
12. **Assumptions**: `X of Y have; Z missing` → Pass: Z=0

**MANDATORY**: If fail → fix → regenerate → re-validate. Proceed only when all pass.

### 7. Checklist

- [ ] Floors: G≥10, C≥5, L≥6, A≥12; Difficulty 20/40/40; Language ~60/30/10
- [ ] Recency ≥50% 3yr (≥70% AI/security); Diversity ≥3 types, no source >25%
- [ ] Coverage ≥70% cite ≥1, ≥30% cite ≥2
- [ ] Quality: 2-4 steps, tolerances, units, assumptions, uncertainty, risk/value
- [ ] Maturity: License, update ≤12mo, stable, audit; Links/cross-refs resolve; Alternatives
- [ ] Validation: All 12 pass

## Output Format

### Structure

TOC linking to sections and problems (P1, P2, ...).

```markdown
## Contents
- [Problems](#problems)
  - [Topic 1](#topic-1): [P1](#p1), [P2](#p2)
- [References](#references): [Glossary](#glossary), [Codebase](#codebase), [Literature](#literature), [APA](#apa)
- [Validation](#validation)
```

### Problem Template

```markdown
#### P#: [Title]
**Difficulty**: [F/I/A] | **Type**: [Calculation/Conversion/Justification]

**Problem**: [Statement with values/units; may cite [Ref: ID]]
**Given**: [Values + units]
**Assumptions/Constraints**: [List; cite [Ref: ID] when applicable]

**Answer**: [Value + units] | **Tolerance**: [±%]

**Solution**:
1. [Formula [Ref: ID]]
2. [Calculation]

**Uncertainty/Limitations**: [Caveats, ranges]
**Risk/Value**: [Trade-offs, mitigations]
**Alternatives**: [Valid variations]
**Grading**: [Rubric] | **Common Errors**: [List]
```

### Visual Elements

- **Tables**: Specs, requirements
- **Lists**: Numbered (steps), bulleted (items)
- **Formulas**: `$inline$`, `$$block$$`
- **Code**: Tagged fences
- **Diagrams**: Mermaid

### Reference Formats

**Glossary**: `**G#: Term**: Definition [Lang]`

**Codebase**: `**C#: Name** ([lang])` + Stack, Maturity (license, update ≤12mo, stable), Benchmarks (perf, audit, adoption)

**Literature**: `**L#: Title** (Year) ([lang])` + Core (formulas, benchmarks), Methodology (sample, scope), Impact (citations, adoption), Limitations, APA + link

**APA**: Group by language; APA 7th + tag + link

**Example**:
```text
**G1: TPS**: Transactions Per Second [EN]

**C1: Ethereum** ([EN])
Stack: EVM, Solidity, Web3.js
Maturity: MIT, 2024-11, v1.14.11
Benchmarks: ~15 TPS, ConsenSys audit

**L1: Ethereum Yellow Paper** (2024) ([EN])
Core: gas_cost = base_fee + priority_fee
Methodology: Formal spec
Impact: 50K+ citations
Buterin, V. (2024). Ethereum: A secure decentralised generalised transaction ledger. https://ethereum.github.io/yellowpaper/paper.pdf [EN]
```

**Inline**: "Throughput [Ref: L4]: TPS = block_size / block_time [Ref: G8]"


