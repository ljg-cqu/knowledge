# Short Answer / Calculation

Generate senior/architect/expert-level short answer/calculation assessments (25–40 problems) with worked solutions, citations, and validation.

## Context

This template creates technical assessment problem banks for senior-level positions requiring precise calculations, throughput analysis, latency optimization, gas cost estimation, consensus mechanisms, unit conversions, and technical justifications. Each problem includes worked solutions with proper citations and follows MECE principles for comprehensive coverage.

## Scope

- **Target Audience**: Senior developers, architects, technical experts
- **Problem Types**: Throughput calculations, latency analysis, gas costs, consensus mechanisms, unit conversions, technical justifications (2–3 sentences)
- **Output**: 25–40 problems with worked solutions, citations, and validation reports
- **Languages**: ~60% English, ~30% Chinese, ~10% other sources
- **Quality Standards**: Peer-reviewed sources, official documentation, audited codebases

---

# Part I: Specifications

Define quality requirements, standards, and constraints.

## Specifications

### Clarity and Precision

- **Clear Explanations**: Each problem provides unambiguous statements with all necessary values and units
- **Consistent Terminology**: Use standardized technical terms; define jargon in glossary
- **Specific Requirements**: Exact tolerance specifications (±%), unit requirements, and expected answer formats
- **Relevance**: Problems align with senior-level technical responsibilities and real-world scenarios

- **Assumptions & Constraints**: Explicitly state assumptions, preconditions, and constraints for each problem
- **Exclusions**: Exclude tangential information; keep scope tight and on-topic

### MECE Coverage and Sufficiency

- **Complete Coverage**: Ensure all problem types (throughput, latency, gas costs, consensus, conversions, justifications) are represented
- **Non-overlapping Categories**: Each problem fits clearly into one type without ambiguity
- **Comprehensive Treatment**: Each topic area includes foundational, intermediate, and advanced problems
- **Multiple Perspectives**: Include various calculation methods, optimization strategies, and implementation approaches

| Aspect | Requirement |
|--------|-------------|
| Scope | 25–40 problems (senior/architect/expert level) |
| Difficulty | 20% Foundational / 40% Intermediate / 40% Advanced |
| Problem Types | Throughput, latency, gas costs, consensus, conversions, justifications (2–3 sentences) |
| Answers | Exact values + units + tolerances (±%); worked solutions (2–4 steps); LaTeX/KaTeX supported |
| Grading | Normalize input; apply tolerances; Partial credit: 70% (correct method), 50% (setup only) |
| Conflicts | Document alternative methods; specify when each is acceptable |

### Quality Excellence and Credibility

- **Significant Information**: Focus on practically important calculations and scenarios used in real systems
- **Concise Presentation**: Remove redundant steps; include only essential calculations and reasoning
- **Accuracy Verification**: Cross-check all formulas, conversion factors, and benchmark values
- **Authoritative Sources**: Prioritize official documentation, peer-reviewed papers, audited codebases, and industry standards
- **Logical Coherence**: Ensure worked solutions follow clear, step-by-step reasoning
- **Risk/Value Assessment**: Include realistic constraints and practical considerations in problem design
- **Fairness and Balance**: Acknowledge alternative valid methods, assumptions, and trade-offs

- **Uncertainty Handling**: Flag uncertainty and limitations; state data ranges or confidence where applicable

### Citation Standards

| Aspect | Requirement |
|--------|-------------|
| Languages | ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH]) |
| Source Types | (1) Official docs (specs, RFCs); (2) Standards/peer-reviewed (ISO, IEEE, journals); (3) Audits/reports; (4) Vetted code (stable releases) |
| Format | APA 7th + language tags |
| Inline Citation | Use `[Ref: ID]` in worked solutions for formulas, standards, conversion factors |

### Structure and Format Standards

- **Organized Structure**: Use tables for specifications, lists for requirements, numbered steps for solutions
- **Visual Elements**: Include formulas in LaTeX/KaTeX, code blocks for calculations, diagrams where appropriate
- **Structured Output**: Table of Contents linking to all sections and individual problems
- **TOC Placement**: Place the full Table of Contents at the top, before the Problem Bank
- **Evidence-Based Content**: All formulas and benchmarks cited with reliable sources
- **Validation Requirements**: Include self-check steps and error verification procedures
- **Practical Application**: Ensure all problems relate to real-world technical scenarios
- **Success Criteria**: Define measurable outcomes through validation reports and quality gates

### Reference Minimum Requirements

| Reference Section | Floor | Notes |
|-------------------|-------|-------|
| Glossary, Terminology & Acronyms | ≥10 | Core concepts, domain jargon, localized terms |
| Codebase & Library References | ≥5 | Primary stack, SDKs, tooling |
| Authoritative Literature & Reports | ≥6 | Standards, peer-reviewed, regulatory/industry analyses |
| APA Style Source Citations | ≥12 | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception**: If floor count unmet, state shortfall + rationale + sourcing plan.

### Quality Gates

| Gate | Requirement |
|------|-------------|
| Recency | ≥50% from last 3 years; ≥70% from last 2 years (AI/security domains) |
| Source Diversity | ≥3 source types; no single source >25% |
| Evidence Coverage | ≥70% problems with ≥1 citation; ≥30% with ≥2 distinct citations |
| Codebase Maturity | License + last commit ≤12 months + stable release + audit status (if available) |
| Deduplication | Canonicalize entries; prefer persistent links (DOIs, archived URLs) |
| Link Validity | All links resolve or archived alternative provided |
| Cross-Reference | All `[Ref: ID]` in solutions resolve to Reference Sections |

> **Scaling**: For >40 problems or regulated domains, increase floors by 1.5× (round up). Prioritize Quality Gates.

### Pre-Submission Validation

Execute ALL steps. Present validation report. Fix failures; re-run until all pass.

**Step 1 – Count Audit**
- Count: Glossary, Codebase, Literature, APA citations, Problems (total + by difficulty)
- Report: `Glossary: X (≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Problems: N (F foundational, I intermediate, A advanced)`
- Pass: All minimums met AND difficulty ≈20/40/40

**Step 2 – Citation Coverage**
- Count `[Ref: ...]` in each worked solution
- Report: `X of Y problems with ≥1 citation (Z%); W with ≥2 (V%)`
- Pass: ≥70% with ≥1 AND ≥30% with ≥2

**Step 3 – Language Distribution**
- Count `[EN]`, `[ZH]`, other tags
- Report: `EN: X (Y%) | ZH: A (B%) | Other: C (D%)`
- Pass: EN ≈50-70%, ZH ≈20-40%, Other ≈5-15%

**Step 4 – Recency**
- Extract publication year from each citation
- Report: `X of Y (Z%) from 2022-2025`
- Pass: ≥50% from last 3 years (≥70% for AI/security)

**Step 5 – Source Diversity**
- Classify: (1) Official docs, (2) Standards/peer-reviewed, (3) Audits/reports, (4) Vetted code
- Report: `Type 1: X | Type 2: Y | Type 3: Z | Type 4: W | Present: N | Max source: M (P%)`
- Pass: ≥3 types AND no source >25%

**Step 6 – Link Validation**
- Test each URL or verify archived link
- Report: `Tested X: Y accessible, Z broken` (list broken)
- Pass: All accessible OR archived alternatives provided

**Step 7 – Cross-Reference Integrity**
- Verify each `[Ref: ID]` exists (G#→Glossary, C#→Codebase, L#→Literature, A#→APA)
- Report: `Found X refs: Y resolve, Z broken` (list broken)
- Pass: Z=0

**Step 8 – Solution Completeness**
- Verify worked solution (2-4 steps) with formulas/calculations
- Report: `X of Y complete; Z incomplete` (list issues)
- Pass: Z=0

**Step 9 – Tolerance Specification**
- Verify tolerance (±%) for each numerical problem
- Report: `X of Y with tolerances; Z missing` (list)
- Pass: Z=0

**Step 10 – Unit Consistency**
- Verify units consistent throughout
- Report: `X of Y consistent; Z inconsistent` (list)
- Pass: Z=0

**Step 11 – Conflict Handling**
- Identify problems with multiple valid methods
- Verify alternatives documented with acceptance criteria
- Report: `X applicable; Y comply (Z%)`
- Pass: ≥80% OR rationale provided

**Step 12 – Assumptions & Uncertainty**
- Verify each problem lists Assumptions & Constraints and notes any uncertainty/limitations
- Report: `X of Y with assumptions/constraints; Z missing` (list)
- Pass: Z=0

> **MANDATORY:** If any check fails, stop → fix → regenerate → re-validate. Proceed only when all pass.

### Submission Checklist

- [ ] Floors: Glossary ≥10, Codebase ≥5, Literature ≥6, APA ≥12
- [ ] Difficulty: 20/40/40 (Foundational/Intermediate/Advanced)
- [ ] Language: ~60% EN, ~30% ZH, ~10% other
- [ ] Recency: ≥50% last 3yr (≥70% AI/security)
- [ ] Diversity: ≥3 source types, no source >25%
- [ ] Coverage: ≥70% with ≥1 citation; ≥30% with ≥2
- [ ] Quality: Worked solutions (2-4 steps), tolerances, units
- [ ] Assumptions: Assumptions & Constraints + Uncertainty/Limitations present per problem
- [ ] Maturity: License, update ≤12mo, stable release, audit status
- [ ] Links: Resolve or archived
- [ ] Cross-refs: IDs match solutions ↔ Reference Sections
- [ ] Alternatives: Answer forms documented
- [ ] Validation: All 12 steps pass

---

# Part II: Instructions

Execute generation workflow with inline quality checks at each step.

## Instructions

Execute steps sequentially. Perform inline checks before proceeding.

### Step 1: Topic Identification & Planning
1. **Context Analysis**: Identify 4-6 technical clusters relevant to senior-level assessment (e.g., throughput optimization, latency analysis, gas cost calculation, consensus mechanisms)
2. **MECE Allocation**: Distribute 4-7 problems per cluster for total 25-40 problems
3. **Difficulty Balance**: Assign difficulties to achieve 20% foundational, 40% intermediate, 40% advanced distribution
4. **Validation Check**: Verify total count = 25-40 AND difficulty ratio ≈20/40/40

### Step 2: Reference Collection
1. **Source Gathering**: Collect authoritative sources meeting minimum requirements (≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA)
2. **Quality Classification**: Tag each source with language ([EN], [ZH]), publication year, and type (1-4 based on credibility hierarchy)
3. **ID Assignment**: Assign systematic IDs: G1-Gn (Glossary), C1-Cn (Codebase), L1-Ln (Literature), A1-An (APA citations)
4. **Quality Verification**: Check counts (≥10/5/6/12), language distribution (≈60/30/10), recency (≥50% last 3 years), source diversity (≥3 types)

### Step 3: Problem Generation
1. **Clear Problem Statement**: Write unambiguous descriptions with all required values, units, and assigned difficulty/type
   and an explicit Assumptions & Constraints list
2. **Citation Integration**: Include ≥1 `[Ref: ID]` in worked solutions for formulas, standards, benchmarks, or conversion factors
3. **Complete Solution**: Provide exact answer with units, tolerance specification (±%), worked solution (2-4 logical steps),
   and note uncertainty/limitations where applicable
4. **Inline Quality Check**: Every 5 problems, verify solution completeness, tolerance presence, unit consistency, citation inclusion,
   and presence of assumptions/uncertainty fields

5. **Risk/Value Note**: Include brief trade-offs, cost/benefit, and mitigation steps where relevant

### Step 4: Alternative Forms & Grading
1. **Acceptable Variations**: Document valid alternative answer forms (different units, equivalent expressions, normalized values)
2. **Grading Rubrics**: Include partial credit criteria (70% for correct method, 50% for correct setup only)
3. **Common Mistakes**: List typical calculation errors or misunderstandings for each problem type
4. **Compliance Check**: Ensure all problems include grading rubrics and alternative form documentation

### Step 5: Reference Section Compilation
1. **Section Population**: Populate all reference sections with collected sources following specified formats
2. **Field Completeness**: Include all required fields for each reference type (maturity indicators, methodology, impact metrics)
3. **Cross-Reference Matching**: Verify all inline `[Ref: ID]` citations resolve to corresponding reference entries
4. **Format Validation**: Check that all sources follow APA 7th edition with proper language tags and persistent links

### Step 6: Pre-Submission Validation
Execute all 12 validation steps from Part I. Present comprehensive validation report. Fix any failures; re-run validation until all steps pass.

### Step 7: Final Review
Verify all items in Submission Checklist (Part I) are complete. Submit only when all validation steps pass and quality gates are met.

---

# Part III: Output Format

Template structure for generated problem banks.

## Output Format

### Structure Overview

Generate well-structured technical assessment with clear navigation and comprehensive coverage. Start with a detailed Table of Contents linking to all sections and individual problems.

### Content Requirements

- **Visual Elements**: Use tables for specifications, lists for requirements, numbered steps for solutions, formulas in LaTeX/KaTeX
- **Diagrams**: Include Mermaid diagrams for complex workflows or system architectures where applicable
- **Code Blocks**: Use language-tagged fences for calculations and algorithm examples
- **Mathematical Notation**: Support inline and block LaTeX for formulas and equations

### Navigation Standards

Create comprehensive TOC with links to:
- All problem bank sections and topic areas
- Each individual problem (P1, P2, etc.)
- All reference sections (Glossary, Codebase, Literature, APA citations)
- Validation reports and quality gate summaries

```markdown
## Contents

- [Problem Bank](#problem-bank-problems-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [P1: [Problem title]](#p1-problem-title)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [P2: [Problem title]](#p2-problem-title)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

- [Quality Gates](#quality-gates)
- [Pre-Submission Validation](#pre-submission-validation)
- [Submission Checklist](#submission-checklist)
```

---

## Problem Bank (Problems 1–N)

### Topic 1: [Topic title]

#### P1: [Problem title]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Type:** [Calculation/Conversion/Justification]

**Problem:** [Description with all given values; may include [Ref: ID] citations for specifications or benchmarks]

**Given:** [List values with units]

**Assumptions & Constraints:** [List assumptions, preconditions, constraints; include [Ref: ID] when standards inform assumptions]

**Answer:** [Value with units] | **Tolerance:** [±%] | **Units:** [unit]

**Worked Solution:**
1. [Step with formula; include [Ref: ID] citations when referencing formulas, standards, conversion factors]
2. [Calculation]

**Uncertainty & Limitations:** [Note uncertainty, data ranges, caveats]

**Risk/Value & Mitigations:** [Trade-offs, cost/benefit, mitigations]

**Alternative Forms:** [Acceptable variations]

**Grading:** [Rubric] | **Common Mistakes:** [List]

---

## Reference Sections

Use IDs to link solutions to sources: `[Ref: G3]` (Glossary), `[Ref: C1]` (Codebase), `[Ref: L2]` (Literature), `[Ref: A7]` (APA).

**Example**: "Using throughput formula [Ref: L4]: TPS = block_size / block_time [Ref: G8]."

### Minimum Entry Requirements

| Reference Section | Floor | Notes |
|-------------------|-------|-------|
| Glossary, Terminology & Acronyms | ≥10 | Core concepts, domain jargon, localized terms |
| Codebase & Library References | ≥5 | Primary stack, SDKs, tooling |
| Authoritative Literature & Reports | ≥6 | Standards, peer-reviewed, regulatory/industry analyses |
| APA Style Source Citations | ≥12 | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception**: If floor unmet, state shortfall + rationale + sourcing plan.

### Glossary, Terminology & Acronyms

**Format:**

```text
**G1: Term/Acronym**: Definition [Language Tag]
```

**Example:**

```text
**G1: MECE** (Mutually Exclusive, Collectively Exhaustive): Framework ensuring categories don't overlap and cover all possibilities [EN]
```

### Codebase & Library References

**C1: [Project/Library Name]** ([lang])

**Must include:**
- Stack/Modules: Core SDK/components
- Maturity: License, update ≤12mo, stable release
- Benchmarks: Performance, audit status, adoption

**Recommended:**
- Integration hooks, Reliability/HA, Language support, Vulnerability disclosures

**Format**: Repository URL (GitHub: owner/repo | License: Type), docs URL, maturity details.

### Authoritative Literature & Reports

**L1: [Title]** (Year) ([lang])

**Must include:**
- Core Findings: Formulas, benchmarks, standards
- Methodology: Sample size, temporal scope
- Impact: Citations, industry adoption

**Recommended:**
- Limitations, replication status, follow-ups, jurisdiction

**Format**: APA citation + language tag + persistent link (DOI/archived URL).

### APA Style Source Citations

List sources grouped by language (~60% EN, ~30% ZH, ~10% other). Follow APA 7th edition with language tags.

**Example:**

```text
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms: A comparative analysis.
    Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究.
    计算机科学, 51(2), 88-95. [ZH]

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system.
    https://bitcoin.org/bitcoin.pdf [EN]
```


