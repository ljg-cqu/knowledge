# Short Answer / Calculation

Generate 25–40 senior-level short answer/calculation problems with worked solutions, citations, and validation.

## Task

Create technical assessment problem banks (throughput, latency, gas costs, consensus, conversions, justifications). Include worked solutions (2–4 steps), citations, MECE coverage, and comprehensive validation. Target senior developers/architects/experts.

| Parameter | Requirement |
|-----------|-------------|
| **Scope** | 25–40 problems; 20% foundational, 40% intermediate, 40% advanced |
| **Problem Types** | Throughput, latency, gas costs, consensus, conversions, justifications (2–3 sentences) |
| **Answers** | Exact values + units + tolerance (±%); worked solutions (2–4 steps); LaTeX/KaTeX supported |
| **Sources** | ~60% EN, ~30% ZH, ~10% other; APA 7th; official docs, peer-reviewed, audited code |
| **Grading** | Normalize input; apply tolerances; partial credit: 70% (correct method), 50% (setup only) |
| **Quality** | Real-world scenarios; clear assumptions/constraints; flag uncertainty; document alternative methods |

## Reference Minimums

| Section | Floor | Content |
|---------|-------|---------|
| Glossary | ≥10 | Core concepts, domain jargon, localized terms; **Format**: `**G1: Term**: Definition [Lang]` |
| Codebase | ≥5 | Primary stack, SDKs, tooling; License, update ≤12mo, stable release, audit status |
| Literature | ≥6 | Standards, peer-reviewed, regulatory analyses; formulas, benchmarks, methodology |
| APA Citations | ≥12 | Language mix (~60% EN / ~30% ZH / ~10% other); persistent links (DOIs, archived URLs) |

**Inline Citation**: Use `[Ref: ID]` in solutions (G#→Glossary, C#→Codebase, L#→Literature, A#→APA).

**Exception**: If floor unmet, state shortfall + rationale + sourcing plan.

## Quality Gates

| Gate | Requirement |
|------|-------------|
| Recency | ≥50% from last 3yr (≥70% for AI/security) |
| Source Diversity | ≥3 types; no source >25% |
| Citation Coverage | ≥70% problems with ≥1 citation; ≥30% with ≥2 |
| Codebase Maturity | License + update ≤12mo + stable release + audit status |
| Link Validity | All resolve or archived alternative provided |
| Cross-Reference | All `[Ref: ID]` resolve to Reference Sections |

**Scaling**: For >40 problems or regulated domains, increase floors by 1.5×.

## Workflow

### 1. Topic Planning
- Identify 4–6 technical clusters (e.g., throughput optimization, latency analysis)
- Distribute 4–7 problems per cluster → 25–40 total
- Assign difficulties → 20/40/40 (foundational/intermediate/advanced)
- **Verify**: Total = 25–40 AND difficulty ≈20/40/40

### 2. Reference Collection
- Collect authoritative sources (≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA)
- Tag: language ([EN], [ZH]), year, type (1=official docs, 2=peer-reviewed, 3=audits, 4=vetted code)
- Assign IDs: G1-Gn, C1-Cn, L1-Ln, A1-An
- **Verify**: Minimums met, language ≈60/30/10, recency ≥50% last 3yr, diversity ≥3 types

### 3. Problem Generation
- Write clear statements (all values, units, difficulty, type, assumptions/constraints)
- Include ≥1 `[Ref: ID]` in worked solutions (formulas, standards, benchmarks)
- Provide exact answer + units + tolerance (±%) + 2–4 step solution + uncertainty/limitations + risk/value notes
- **Verify every 5 problems**: Completeness, tolerances, units, citations, assumptions/uncertainty

### 4. Grading & Alternatives
- Document valid alternative forms (units, expressions, normalized values)
- Include partial credit rubrics (70% method, 50% setup)
- List common mistakes per problem type
- **Verify**: All problems have rubrics and alternative forms

### 5. Reference Compilation
- Populate all sections (Glossary, Codebase, Literature, APA)
- Include required fields (maturity indicators, methodology, impact metrics)
- Verify all `[Ref: ID]` resolve
- Check APA 7th edition + language tags + persistent links

### 6. Validation (Execute ALL 12 steps)

1. **Count Audit**: `Glossary: X (≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Problems: N (F foundational, I intermediate, A advanced)` → Pass: Minimums met AND difficulty ≈20/40/40
2. **Citation Coverage**: `X of Y with ≥1 (Z%); W with ≥2 (V%)` → Pass: ≥70% with ≥1 AND ≥30% with ≥2
3. **Language**: `EN: X (Y%) | ZH: A (B%) | Other: C (D%)` → Pass: EN ≈50-70%, ZH ≈20-40%, Other ≈5-15%
4. **Recency**: `X of Y (Z%) from 2022-2025` → Pass: ≥50% (≥70% AI/security)
5. **Diversity**: `Type 1: X | Type 2: Y | Type 3: Z | Type 4: W | Present: N | Max: M (P%)` → Pass: ≥3 types AND no source >25%
6. **Links**: `Tested X: Y accessible, Z broken` → Pass: All accessible OR archived alternatives
7. **Cross-Reference**: `Found X refs: Y resolve, Z broken` → Pass: Z=0
8. **Solutions**: `X of Y complete; Z incomplete` → Pass: Z=0
9. **Tolerances**: `X of Y with tolerances; Z missing` → Pass: Z=0
10. **Units**: `X of Y consistent; Z inconsistent` → Pass: Z=0
11. **Conflicts**: `X applicable; Y comply (Z%)` → Pass: ≥80% OR rationale
12. **Assumptions**: `X of Y with assumptions/constraints; Z missing` → Pass: Z=0

**MANDATORY**: If any fails → fix → regenerate → re-validate. Proceed only when all pass.

### 7. Final Checklist

- [ ] Floors: Glossary ≥10, Codebase ≥5, Literature ≥6, APA ≥12
- [ ] Difficulty: 20/40/40; Language: ~60% EN, ~30% ZH, ~10% other
- [ ] Recency: ≥50% last 3yr (≥70% AI/security); Diversity: ≥3 types, no source >25%
- [ ] Coverage: ≥70% with ≥1 citation, ≥30% with ≥2
- [ ] Quality: Worked solutions (2-4 steps), tolerances, units, assumptions/constraints, uncertainty/limitations
- [ ] Maturity: License, update ≤12mo, stable release, audit status
- [ ] Links resolve or archived; Cross-refs resolve; Alternatives documented
- [ ] Validation: All 12 steps pass

## Output Format

### Structure

Start with Table of Contents linking to all sections and individual problems (P1, P2, ...).

```markdown
## Contents
- [Problem Bank](#problem-bank)
  - [Topic 1: [Title]](#topic-1-title)
    - [P1: [Title]](#p1-title)
  - [Topic 2: [Title]](#topic-2-title)
    - [P2: [Title]](#p2-title)
- [References](#references)
  - [Glossary](#glossary)
  - [Codebase](#codebase)
  - [Literature](#literature)
  - [APA Citations](#apa-citations)
- [Validation Report](#validation-report)
```

### Problem Template

```markdown
#### P1: [Problem Title]
**Difficulty**: [Foundational/Intermediate/Advanced] | **Type**: [Calculation/Conversion/Justification]

**Problem**: [Description with values/units; may include [Ref: ID]]

**Given**: [Values with units]

**Assumptions & Constraints**: [List; include [Ref: ID] when applicable]

**Answer**: [Value with units] | **Tolerance**: [±%] | **Units**: [unit]

**Worked Solution**:
1. [Step with formula [Ref: ID]]
2. [Calculation]

**Uncertainty & Limitations**: [Caveats, data ranges]

**Risk/Value & Mitigations**: [Trade-offs, cost/benefit, mitigations]

**Alternative Forms**: [Acceptable variations]

**Grading**: [Rubric] | **Common Mistakes**: [List]
```

### Visual Elements

- **Tables**: Specifications, requirements
- **Lists**: Numbered (solutions), bulleted (requirements)
- **Formulas**: LaTeX/KaTeX inline (`$...$`) and block (`$$...$$`)
- **Code**: Language-tagged fences
- **Diagrams**: Mermaid for workflows/architectures

### Reference Formats

**Glossary**: `**G1: Term**: Definition [EN/ZH]`

**Codebase**: `**C1: [Name]** ([lang])` + Stack/Modules, Maturity (License, update ≤12mo, stable release), Benchmarks (performance, audit, adoption), Integration/Reliability/Language/Vulnerabilities

**Literature**: `**L1: [Title]** (Year) ([lang])` + Core Findings (formulas, benchmarks, standards), Methodology (sample, scope), Impact (citations, adoption), Limitations/Replication/Follow-ups, APA citation + persistent link

**APA Citations**: Group by language; APA 7th + language tag + persistent link

**Example**:
```text
**G1: TPS**: Transactions Per Second - throughput metric [EN]

**C1: Ethereum** ([EN])
Stack: EVM, Solidity, Web3.js
Maturity: License MIT, updated 2024-11, v1.14.11
Benchmarks: ~15 TPS, audited by ConsenSys

**L1: Ethereum Yellow Paper** (2024) ([EN])
Core: EVM gas mechanics, formula: gas_cost = base_fee + priority_fee
Methodology: Formal specification
Impact: 50K+ citations
Buterin, V. (2024). Ethereum: A secure decentralised generalised transaction ledger.
    https://ethereum.github.io/yellowpaper/paper.pdf [EN]
```

**Inline Example**: "Using throughput formula [Ref: L4]: TPS = block_size / block_time [Ref: G8]."


