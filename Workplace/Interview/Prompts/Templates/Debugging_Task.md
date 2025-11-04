# Debugging Task

Framework for generating high-quality debugging task assessments with proper structure, citations, and multi-dimensional evaluation.

---

# Part I: Specifications

Define quality requirements, standards, and constraints.

## Specifications

### Scope and Structure

- **Scope**: 15–22 tasks for senior/expert level
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Bug Types**: Single focused bug (10–50 lines): off-by-one, type mismatch, API, concurrency, edge cases, logic, security, performance
- **Deliverables**: Buggy code, failing tests, corrected code (minimal fix), root-cause explanation (2–4 sentences)
- **Grading**: Fix 0–6 pts, Explanation 0–3 pts, Tests 0–1 pt; partial credit for correct diagnosis

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH], etc.)
- **Source Types**: (1) Official docs (language specs, vendor docs, RFCs); (2) Standards/peer-reviewed (ISO, IEEE, academic journals, conference papers); (3) Audits/reports (security audits, industry analyses, regulatory guidance); (4) Vetted code (production repos with stable releases)
- **Format**: APA 7th with language tags
- **Distribution**: Codebase/libraries (repos, maturity, benchmarks); Literature/Reports
- **Inline Citation**: Use [Ref: ID] in root-cause explanations when referencing language specifications, API documentation, and common bug patterns. Code comments may include citations.

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
- Evidence coverage: ≥70% of tasks include ≥1 inline citation in root-cause explanation; ≥30% include ≥2 citations tied to distinct claims.
- Codebase maturity: Each codebase/library entry includes license, last commit ≤12 months, latest stable release, and security audit status (if available).
- Deduplication: Canonicalize and avoid duplicate entries; prefer persistent links (DOIs, standards bodies, archived URLs).
- Link validity: Validate that links resolve (or provide archived link) at time of delivery.
- Cross-reference binding: Use reference IDs and link task explanations to specific items in the Reference Sections.

> Scaling guidance: For sets >30 tasks or regulated domains, increase floor counts by ~1.5× (round up) instead of unlimited growth. Prioritize meeting the Quality Gates first.

### Pre-Submission Validation

Execute ALL steps below. Present results in a validation report table. Fix any failures and re-run validation until all checks pass.

**Step 1 – Count Audit**
- Count: Glossary entries, Codebase entries, Literature entries, APA citations, Tasks (total + by difficulty level)
- Report: `Glossary: X (target ≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Tasks: N total (F foundational, I intermediate, A advanced)`
- Pass if: All counts meet minimums AND difficulty ratio ≈20/40/40

**Step 2 – Citation Coverage Scan**
- For EACH root-cause explanation: Count inline `[Ref: ...]` occurrences
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
- For EACH `[Ref: ID]` in explanations: Verify ID exists in Reference Sections (G#→Glossary, C#→Codebase, L#→Literature, A#→APA)
- Report: `Found X inline refs; Y resolve correctly, Z broken` (list broken refs)
- Pass if: All refs resolve (Z=0)

**Step 8 – Bug Focus Verification**
- For EACH task: Verify single focused bug (not multiple independent bugs)
- Report: `X of Y tasks have focused bugs; Z have multiple bugs` (list issues)
- Pass if: All tasks have single focused bugs (Z=0)

**Step 9 – Fix Completeness**
- For EACH task: Verify corrected code and root-cause explanation (2-4 sentences) present
- Report: `X of Y tasks have complete fixes; Z incomplete` (list issues)
- Pass if: All tasks have complete fixes (Z=0)

**Step 10 – Test Coverage**
- For EACH task: Verify failing test and passing tests present
- Report: `X of Y tasks have test coverage; Z missing` (list issues)
- Pass if: All tasks have tests (Z=0)

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
| Bug focus | Y/X single bugs | PASS/FAIL |
| Fix completeness | Y/X complete | PASS/FAIL |
| Test coverage | Y/X present | PASS/FAIL |
```

> **MANDATORY:** If ANY check shows FAIL, stop, fix issues, regenerate affected sections, and re-run full validation. Only proceed to submission when ALL checks show PASS.

### Submission Checklist

- [ ] Floors met (Glossary ≥10, Codebase ≥5, Literature ≥6, APA citations ≥12)
- [ ] Difficulty distribution verified (20/40/40: Foundational/Intermediate/Advanced)
- [ ] Language distribution verified (~60% EN, ~30% ZH, ~10% other)
- [ ] Recency: ≥50% citations last 3 years (≥70% for AI/security)
- [ ] Diversity: ≥3 source types, no single source >25%
- [ ] Evidence coverage: ≥70% tasks with ≥1 citation; ≥30% with ≥2 distinct citations
- [ ] Task quality: Single focused bugs, corrected code, root-cause explanations (2-4 sentences)
- [ ] Codebase maturity noted (license, last update ≤12 months, stable release, audit status)
- [ ] Links resolve or archived URLs provided
- [ ] Cross-references present (IDs used in explanations and in Reference Sections)
- [ ] Test coverage complete (failing + passing tests)
- [ ] Pre-submission validation completed with passing results

---

# Part II: Instructions

Execute generation workflow with inline quality checks at each step.

## Instructions

Follow these steps in order. Execute inline quality checks at each step before proceeding.

### Step 1: Topic Identification & Planning
1. Identify 4-6 bug type clusters (e.g., off-by-one, concurrency, API misuse)
2. Allocate 2-4 tasks per cluster (total 15-22)
3. Assign difficulty levels to ensure 20/40/40 balance
4. **Inline Check**: Verify total tasks = 15-22 AND difficulty ratio ≈20/40/40 before proceeding

### Step 2: Reference Collection
1. Gather ≥10 glossary terms, ≥5 codebase/libraries, ≥6 literature sources, ≥12 APA citations
2. For EACH source: Tag language ([EN], [ZH], etc.), note publication year, classify source type (1-4)
3. Assign Reference IDs: G1-Gn (Glossary), C1-Cn (Codebase), L1-Ln (Literature), A1-An (APA)
4. **Inline Check**: Count sources (≥10/5/6/12?), language split (≈60/30/10?), recency (≥50% last 3yr?), diversity (≥3 types?) before proceeding

### Step 3: Task Generation
1. For EACH task: Create buggy code (10-50 lines, single focused bug), assign difficulty + language
2. In EACH root-cause explanation: Include ≥1 inline `[Ref: ID]` when referencing specifications, bug patterns
3. For EACH task: Provide failing test, corrected code, root-cause explanation (2-4 sentences)
4. **Inline Check**: After every 3 tasks, verify: bugs focused, ≥1 citation in explanations, fixes complete, tests present

### Step 4: Alternative Solutions
1. For EACH task: Document alternative valid fixes and common mistakes
2. Include grading rubrics with partial credit guidelines
3. **Inline Check**: All tasks have rubrics? Alternative fixes documented?

### Step 5: Reference Section Compilation
1. Populate Glossary, Codebase, Literature, APA sections with collected sources
2. Include all required information (must-include fields per format)
3. Ensure Reference IDs match inline citations
4. **Inline Check**: Every [Ref: ID] in explanations resolves to an entry? All sources have required fields?

### Step 6: Pre-Submission Validation
Execute all 10 validation steps (see Part I > Pre-Submission Validation). Present validation report table. Fix any FAIL results and re-validate.

### Step 7: Final Review
Check Submission Checklist (see Part I). Submit only when all checks pass.

---

# Part III: Output Format

Template structure for generated task banks.

## Output Format

```markdown
## Contents

- [Task Bank](#task-bank-tasks-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Task 1: [Bug description]](#task-1-bug-description)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Task 2: [Bug description]](#task-2-bug-description)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Task Bank (Tasks 1–N)

### Topic 1: [Topic title]

#### Task 1: [Bug description]

**Language:** [python/javascript/go/rust/solidity] | **Difficulty:** [Foundational/Intermediate/Advanced]

**Buggy Code:**
```[language]
[Code with bug; code comments may include [Ref: ID] citations when referencing API patterns or language specifications]
```

**Failing Output:** [Error or unexpected behavior]

**Failing Test:**
```[language]
[Test case]
```

**Corrected Code:**
```[language]
[Fixed code with comments]
```

**Root Cause:** [2–4 sentence explanation; include [Ref: ID] citations for specifications, patterns, known pitfalls]

**Passing Tests:**
```[language]
[Test cases]
```

**Grading:** [Rubric] | **Common mistakes:** [List] | **Alternatives:** [Other valid fixes]

---

## Reference Sections

Use Reference IDs in your explanations and code comments to tie claims to sources: `[Ref: G3]` (Glossary entry 3), `[Ref: C1]` (Codebase entry 1), `[Ref: L2]` (Literature entry 2), `[Ref: A7]` (APA citation 7). Inline example: "The bug stems from JavaScript's type coercion [Ref: G5] in equality checks, leading to unexpected behavior [Ref: L3]."

### Minimum Entry Requirements

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
**G1: Term/Acronym**: Definition [Language Tag]
```

**Example:**

```text
**G1: MECE** (Mutually Exclusive, Collectively Exhaustive): Framework ensuring categories don't overlap and cover all possibilities [EN]
```

### Codebase & Library References

**C1: [Project/Library Name]** ([lang])

Must include:
- Stack/Modules: Core SDK or components relevant to debugging tasks
- Maturity: License, last update ≤12 months, latest stable release
- Benchmarks: Performance data, security audit status, community adoption

Recommended:
- Integration Hooks
- Reliability/HA indicators
- Language support matrix
- Vulnerability disclosures

Format: Repository URL (GitHub: owner/repo | License: Type), documentation URL, maturity details.

### Authoritative Literature & Reports

**L1: [Title]** (Year) ([lang])

Must include:
- Core Findings: Main bug patterns or security vulnerabilities identified
- Methodology: Sample size, temporal scope
- Impact: Citations, adoption in industry standards

Recommended:
- Limitations/caveats
- Replication status
- Follow-up studies
- Jurisdiction/regional applicability

Format: APA citation with language tag, persistent link (DOI or archived URL).

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


