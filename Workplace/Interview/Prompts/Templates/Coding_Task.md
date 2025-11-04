# Coding Task

Framework for generating high-quality coding task assessments with proper structure, citations, and multi-dimensional evaluation.

---

# Part I: Specifications

Define quality requirements, standards, and constraints.

## Specifications

### Scope and Structure

- **Scope**: 18–28 tasks for senior/expert level
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Problem**: Self-contained with I/O spec, signatures, constraints (time/memory, libs)
- **Tests**: 6–10 unit tests (3–5 public, 3–5 hidden)
- **Reference**: Working solution with complexity analysis
- **Grading**: Correctness 70%, Edge cases 20%, Style 10%
- **Conflict Handling**: Document alternative valid algorithms with trade-offs (time vs space, readability vs performance)

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH], etc.)
- **Source Types**: (1) Official docs (language specs, vendor docs, RFCs); (2) Standards/peer-reviewed (ISO, IEEE, academic journals, conference papers); (3) Audits/reports (security audits, industry analyses, regulatory guidance); (4) Vetted code (production repos with stable releases)
- **Format**: APA 7th with language tags
- **Distribution**: Codebase/libraries (repos, maturity, benchmarks); Literature/Reports
- **Inline Citation**: Use [Ref: ID] in problem descriptions and reference solutions when referencing algorithms, complexity analysis, and best practices. Code comments may include citations.

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, domain-specific jargon, localized terminology |
| Codebase & Library References | ≥5 entries | Primary stack components, SDKs, supporting tooling |
| Authoritative Literature & Reports | ≥6 entries | Standards, peer-reviewed work, regulatory/industry analyses |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception handling:** If a section cannot meet the floor count, explicitly state the shortfall, provide rationale, and outline a plan to source additional materials.

### Quality Gates

- Recency: ≥50% of citations from the last 3 years; for fast-moving domains (AI, security), target ≥70% from the last 2 years.
- Source diversity: Include at least 3 source types (official docs, standards/peer-reviewed, audits/reports); no single source >25% of total citations.
- Evidence coverage: ≥70% of tasks include ≥1 inline citation in problem/solution; ≥30% include ≥2 citations tied to distinct claims.
- Codebase maturity: Each codebase/library entry includes license, last commit ≤12 months, latest stable release, and security audit status (if available).
- Deduplication: Canonicalize and avoid duplicate entries; prefer persistent links (DOIs, standards bodies, archived URLs).
- Link validity: Validate that links resolve (or provide archived link) at time of delivery.
- Cross-reference binding: Use reference IDs and link task descriptions to specific items in the Reference Sections.

> Scaling guidance: For sets >35 tasks or regulated domains, increase floor counts by ~1.5× (round up) instead of unlimited growth. Prioritize meeting the Quality Gates first.

### Pre-Submission Validation

Execute ALL steps below. Present results in a validation report table. Fix any failures and re-run validation until all checks pass.

**Step 1 – Count Audit**
- Count: Glossary entries, Codebase entries, Literature entries, APA citations, Tasks (total + by difficulty level)
- Report: `Glossary: X (target ≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Tasks: N total (F foundational, I intermediate, A advanced)`
- Pass if: All counts meet minimums AND difficulty ratio ≈20/40/40

**Step 2 – Citation Coverage Scan**
- For EACH task (problem + solution): Count inline `[Ref: ...]` occurrences
- Report: `X of Y tasks have ≥1 citation (Z%); W of Y have ≥2 citations (V%)`
- Pass if: ≥70% have ≥1 citation AND ≥30% have ≥2 citations

**Step 3 – Language Distribution Check**
- Count citations with `[EN]`, `[ZH]`, and other language tags
- Report: `EN: X (Y%) | ZH: A (B%) | Other: C (D%)`
- Pass if: EN ≈50-70%, ZH ≈20-40%, Other ≈5-15%

**Step 4 – Recency Verification**
- Extract publication year from EACH citation
- Report: `X of Y citations (Z%) from 2022-2025 (last 3 years)`
- Pass if: ≥50% from last 3 years (≥70% for AI/security domains)

**Step 5 – Source Type Diversity**
- Classify EACH citation: (1) Official docs, (2) Standards/peer-reviewed, (3) Audits/reports, (4) Vetted code
- Report: `Type 1: X | Type 2: Y | Type 3: Z | Type 4: W | Types present: N | Max single source: M citations (P%)`
- Pass if: ≥3 types present AND no single source >25%

**Step 6 – Link Validation**
- Test EACH URL or verify archived link exists
- Report: `Tested X links: Y accessible, Z broken` (list broken URLs)
- Pass if: All links accessible OR archived alternatives provided

**Step 7 – Cross-Reference Integrity**
- For EACH `[Ref: ID]` in tasks: Verify ID exists in Reference Sections (G#→Glossary, C#→Codebase, L#→Literature, A#→APA)
- Report: `Found X inline refs; Y resolve correctly, Z broken` (list broken refs)
- Pass if: All refs resolve (Z=0)

**Step 8 – Test Coverage Completeness**
- For EACH task: Verify public tests (3-5) and hidden test description present
- Report: `X of Y tasks have complete test suites; Z incomplete` (list issues)
- Pass if: All tasks have complete tests (Z=0)

**Step 9 – Solution Verification**
- For EACH task: Verify reference solution with complexity analysis present
- Report: `X of Y tasks have reference solutions; Z missing` (list issues)
- Pass if: All tasks have solutions (Z=0)

**Step 10 – Constraint Specification**
- For EACH task: Verify time/memory/library constraints specified
- Report: `X of Y tasks have constraints; Z missing` (list issues)
- Pass if: All tasks have constraints (Z=0)

**Step 11 – Conflict Handling Compliance**
- Identify tasks with multiple valid algorithmic approaches
- For EACH: Verify alternative algorithms documented with trade-offs (time vs space, readability vs performance)
- Report: `X applicable tasks; Y comply (Z%)`
- Pass if: ≥80% comply OR rationale provided

**Validation Report Template:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X C:Y L:Z A:W T:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language dist | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Test coverage | Y/X complete | PASS/FAIL |
| Solutions | Y/X present | PASS/FAIL |
| Constraints | Y/X specified | PASS/FAIL |
```

> **MANDATORY:** If ANY check shows FAIL, stop, fix issues, regenerate affected sections, and re-run full validation. Only proceed to submission when ALL checks show PASS.

### Submission Checklist

- [ ] Floors met (Glossary ≥10, Codebase ≥5, Literature ≥6, APA citations ≥12)
- [ ] Difficulty distribution verified (20/40/40: Foundational/Intermediate/Advanced)
- [ ] Language distribution verified (~60% EN, ~30% ZH, ~10% other)
- [ ] Recency: ≥50% citations last 3 years (≥70% for AI/security)
- [ ] Diversity: ≥3 source types, no single source >25%
- [ ] Evidence coverage: ≥70% tasks with ≥1 citation; ≥30% with ≥2 distinct citations
- [ ] Task quality: Self-contained problems, complete test suites, reference solutions with complexity analysis
- [ ] Codebase maturity noted (license, last update ≤12 months, stable release, audit status)
- [ ] Links resolve or archived URLs provided
- [ ] Cross-references present (IDs used in tasks and in Reference Sections)
- [ ] Constraints specified (time/memory/library limits)
- [ ] Pre-submission validation completed with passing results

---

# Part II: Instructions

Execute generation workflow with inline quality checks at each step.

## Instructions

Follow these steps in order. Execute inline quality checks at each step before proceeding.

### Step 1: Topic Identification & Planning
1. Identify 4-6 topic clusters (e.g., algorithms, data structures, system design)
2. Allocate 3-5 tasks per cluster (total 18-28)
3. Assign difficulty levels to ensure 20/40/40 balance
4. **Inline Check**: Verify total tasks = 18-28 AND difficulty ratio ≈20/40/40 before proceeding

### Step 2: Reference Collection
1. Gather ≥10 glossary terms, ≥5 codebase/libraries, ≥6 literature sources, ≥12 APA citations
2. For EACH source: Tag language ([EN], [ZH], etc.), note publication year, classify source type (1-4)
3. Assign Reference IDs: G1-Gn (Glossary), C1-Cn (Codebase), L1-Ln (Literature), A1-An (APA)
4. **Inline Check**: Count sources (≥10/5/6/12?), language split (≈60/30/10?), recency (≥50% last 3yr?), diversity (≥3 types?) before proceeding

### Step 3: Task Generation
1. For EACH task: Write self-contained problem with I/O spec, signatures, assign difficulty + language
2. In EACH problem description: Include ≥1 inline `[Ref: ID]` when referencing algorithms, patterns, complexity requirements
3. For EACH task: Create 6-10 unit tests (3-5 public, 3-5 hidden descriptions)
4. **Inline Check**: After every 4 tasks, verify: problems self-contained, ≥1 citation where applicable, test suites complete

### Step 4: Reference Solutions
1. For EACH task: Write working solution with complexity analysis
2. Document alternative approaches and trade-offs
3. **Inline Check**: All tasks have solutions? Complexity analysis present? Common mistakes documented?

### Step 5: Reference Section Compilation
1. Populate Glossary, Codebase, Literature, APA sections with collected sources
2. Include all required information (must-include fields per format)
3. Ensure Reference IDs match inline citations
4. **Inline Check**: Every [Ref: ID] in tasks resolves to an entry? All sources have required fields?

### Step 6: Pre-Submission Validation
Execute all 10 validation steps (see Part I > Pre-Submission Validation). Present validation report table. Fix any FAIL results and re-validate.

### Step 7: Final Review
Check Submission Checklist (see Part I). Submit only when all checks pass.

---

# Part III: Output Format

Template structure for generated task banks.

## Output Format

Use this structure when generating task banks:

```markdown
## Contents

- [Task Bank](#task-bank-tasks-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Task 1: [Task title]](#task-1-task-title)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Task 2: [Task title]](#task-2-task-title)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Task Bank (Tasks 1–N)

### Topic 1: [Topic title]

#### Task 1: [Task title]

**Language:** [python/javascript/go/rust/solidity] | **Difficulty:** [Foundational/Intermediate/Advanced]

**Problem:** [Description with constraints; include [Ref: ID] citations for algorithms/patterns]

**Signature:** `[function signature]` | **Constraints:** time=[limit], memory=[limit], libs: [allowed]

**Starter Code:**
```[language]
[Code with signature, docstrings, placeholders]
```

**Public Tests:**
```[language]
[Test cases]
```

**Hidden Tests:** [Description of additional test categories]

**Reference Solution:**
```[language]
[Working implementation]
```
**Complexity:** [Time/space] | **Alternatives:** [Other approaches]

**Grading:** [Rubric] | **Common mistakes:** [List] | **Misconceptions:** [List]

---

## Reference Sections

Assign Reference IDs and reuse them inline in problem descriptions and solutions: Glossary (G1…Gn), Codebase (C1…Cn), Literature (L1…Ln), APA Citations (A1…An). Example inline: [Ref: G2, L4].

| Reference section | Floor count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, domain-specific jargon, localized terminology |
| Codebase & Library References | ≥5 entries | Primary stack components, SDKs, supporting tooling |
| Authoritative Literature & Reports | ≥6 entries | Standards, peer-reviewed work, regulatory/industry analyses |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception handling:** If a section cannot meet the floor count, explicitly state the shortfall, provide rationale, and outline a plan to source additional materials.

### Glossary, Terminology & Acronyms

**Format:**

```text
**Term/Acronym**: Definition [Language Tag]
```

**Example:**

```text
**MECE** (Mutually Exclusive, Collectively Exhaustive): Framework ensuring categories don't overlap and cover all possibilities [EN]
```

### Codebase & Library References

**Required Information:**
- Must include: License, last update (last commit ≤12 months) or latest stable version/date, supported languages, integration surface (API/SDK)
- Recommended: Performance/Security benchmarks, consistency guarantees, reliability/HA notes, security audit status

**Format:**

```text
**[Project/Library Name]** (GitHub: owner/repo | License: Type)
- Description: Brief overview
- Stack: Technologies used
- Maturity: Production/Beta/Experimental
- Performance: Key metrics
- Security: Audit status, vulnerability notes
```

### Authoritative Literature & Reports

**Required Information:**
- Must include: Type, year, key findings, credibility (peer-reviewed/standard/regulatory), jurisdiction
- Recommended: Methodology/dataset, limitations/assumptions

**Format:**

```text
**[Title]** (Year) [Language Tag]
- Authors: Names/Organization
- Type: Standard/White Paper/Academic Paper/Regulatory Report
- Key Findings: Summary
- Credibility: Peer-reviewed/Industry standard/Regulatory authority
- Jurisdiction: Applicable regions/markets
```

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
```


