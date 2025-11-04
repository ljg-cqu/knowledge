# Multiple-Choice Questions

Framework for generating high-quality multiple-choice question assessments with proper structure, citations, and multi-dimensional evaluation.

---

# Part I: Specifications

Define quality requirements, standards, and constraints.

## Specifications

### Scope and Structure

- **Scope**: 40–80 MCQs for senior/expert level
- **Format**: Concise stems (1–2 sentences), 4 options, exactly one correct
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Distractors**: Map to misconceptions or outdated practices; flag rationale alignment
- **Rationale**: 1–2 sentences with citation when applicable
- **Grading**: Machine-gradable; no partial credit
- **Conflict Handling**: For contentious topics, distractors should reflect legitimate competing views; rationale clarifies consensus vs dissent

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH], etc.)
- **Source Types**: (1) Official docs (language specs, vendor docs, RFCs); (2) Standards/peer-reviewed (ISO, IEEE, academic journals, conference papers); (3) Audits/reports (security audits, industry analyses, regulatory guidance); (4) Vetted code (production repos with stable releases)
- **Format**: APA 7th with language tags
- **Distribution**: Codebase/libraries (repos, maturity, benchmarks); Literature/Reports
- **Inline Citation**: Use [Ref: ID] in rationales when referencing specifications, standards, research findings. Distractors may reference common misconceptions with citations.

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
- Evidence coverage: ≥70% of questions include ≥1 inline citation in rationale; ≥30% include ≥2 citations tied to distinct claims.
- Codebase maturity: Each codebase/library entry includes license, last commit ≤12 months, latest stable release, and security audit status (if available).
- Deduplication: Canonicalize and avoid duplicate entries; prefer persistent links (DOIs, standards bodies, archived URLs).
- Link validity: Validate that links resolve (or provide archived link) at time of delivery.
- Cross-reference binding: Use reference IDs and link question rationales to specific items in the Reference Sections.

> Scaling guidance: For sets >80 questions or regulated domains, increase floor counts by ~1.5× (round up) instead of unlimited growth. Prioritize meeting the Quality Gates first.

### Pre-Submission Validation

Execute ALL steps below. Present results in a validation report table. Fix any failures and re-run validation until all checks pass.

**Step 1 – Count Audit**
- Count: Glossary entries, Codebase entries, Literature entries, APA citations, Questions (total + by difficulty level)
- Report: `Glossary: X (target ≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Questions: N total (F foundational, I intermediate, A advanced)`
- Pass if: All counts meet minimums AND difficulty ratio ≈20/40/40

**Step 2 – Citation Coverage Scan**
- For EACH rationale: Count inline `[Ref: ...]` occurrences
- Report: `X of Y questions have ≥1 citation (Z%); W of Y have ≥2 citations (V%)`
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
- For EACH `[Ref: ID]` in rationales: Verify ID exists in Reference Sections (G#→Glossary, C#→Codebase, L#→Literature, A#→APA)
- Report: `Found X inline refs; Y resolve correctly, Z broken` (list broken refs)
- Pass if: All refs resolve (Z=0)

**Step 8 – Answer Correctness**
- For EACH question: Verify exactly one correct answer marked
- Report: `X of Y questions have exactly one correct; Z have multiple/zero correct` (list issues)
- Pass if: All questions have exactly one correct (Z=0)

**Step 9 – Distractor Quality**
- For EACH question: Verify distractors map to misconceptions/outdated practices (not random)
- Report: `X of Y questions have quality distractors; Z have weak distractors` (list issues)
- Pass if: All questions have quality distractors (Z=0)

**Step 10 – Option Unambiguity**
- For EACH question: Verify options are mutually exclusive and unambiguous
- Report: `X of Y questions have unambiguous options; Z have overlapping/vague options` (list issues)
- Pass if: All questions have unambiguous options (Z=0)

**Step 11 – Perspective Balance**
- Identify contentious topics; verify ≥2 perspectives cited where applicable
- Report: `X contentious; Y balanced (Z%)`
- Pass if: ≥80% balanced OR rationale provided

**Validation Report Template:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X C:Y L:Z A:W Q:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language dist | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Answer correctness | Y/X exactly one | PASS/FAIL |
| Distractor quality | Y/X quality | PASS/FAIL |
| Option unambiguity | Y/X unambiguous | PASS/FAIL |
```

> **MANDATORY:** If ANY check shows FAIL, stop, fix issues, regenerate affected sections, and re-run full validation. Only proceed to submission when ALL checks show PASS.

### Submission Checklist

- [ ] Floors met (Glossary ≥10, Codebase ≥5, Literature ≥6, APA citations ≥12)
- [ ] Difficulty distribution verified (20/40/40: Foundational/Intermediate/Advanced)
- [ ] Language distribution verified (~60% EN, ~30% ZH, ~10% other)
- [ ] Recency: ≥50% citations last 3 years (≥70% for AI/security)
- [ ] Diversity: ≥3 source types, no single source >25%
- [ ] Evidence coverage: ≥70% questions with ≥1 citation; ≥30% with ≥2 distinct citations
- [ ] Question quality: Exactly one correct answer per question, quality distractors, unambiguous options
- [ ] Codebase maturity noted (license, last update ≤12 months, stable release, audit status)
- [ ] Links resolve or archived URLs provided
- [ ] Cross-references present (IDs used in rationales and in Reference Sections)
- [ ] Rationales complete (1-2 sentences with citations when applicable)
- [ ] Pre-submission validation completed with passing results

---

# Part II: Instructions

Execute generation workflow with inline quality checks at each step.

## Instructions

Follow these steps in order. Execute inline quality checks at each step before proceeding.

### Step 1: Topic Identification & Planning
1. Identify 4-8 topic clusters (e.g., algorithms, security, APIs, concurrency)
2. Allocate 5-10 questions per cluster (total 40-80)
3. Assign difficulty levels to ensure 20/40/40 balance
4. **Inline Check**: Verify total questions = 40-80 AND difficulty ratio ≈20/40/40 before proceeding

### Step 2: Reference Collection
1. Gather ≥10 glossary terms, ≥5 codebase/libraries, ≥6 literature sources, ≥12 APA citations
2. For EACH source: Tag language ([EN], [ZH], etc.), note publication year, classify source type (1-4)
3. Assign Reference IDs: G1-Gn (Glossary), C1-Cn (Codebase), L1-Ln (Literature), A1-An (APA)
4. **Inline Check**: Count sources (≥10/5/6/12?), language split (≈60/30/10?), recency (≥50% last 3yr?), diversity (≥3 types?) before proceeding

### Step 3: Question Generation
1. For EACH question: Write stem (1-2 sentences), create 4 options (exactly one correct), assign difficulty + language
2. In EACH rationale: Include ≥1 inline `[Ref: ID]` when referencing specs, standards, research
3. For EACH distractor: Map to specific misconception or outdated practice
4. **Inline Check**: After every 10 questions, verify: exactly one correct, quality distractors, ≥1 citation in rationale, options unambiguous

### Step 4: Distractor Documentation
1. For EACH question: Document why each distractor is incorrect and what misconception it represents
2. Include common mistake patterns
3. **Inline Check**: All distractors documented? Misconceptions clearly mapped?

### Step 5: Reference Section Compilation
1. Populate Glossary, Codebase, Literature, APA sections with collected sources
2. Include all required information (must-include fields per format)
3. Ensure Reference IDs match inline citations
4. **Inline Check**: Every [Ref: ID] in rationales resolves to an entry? All sources have required fields?

### Step 6: Pre-Submission Validation
Execute all 10 validation steps (see Part I > Pre-Submission Validation). Present validation report table. Fix any FAIL results and re-validate.

### Step 7: Final Review
Check Submission Checklist (see Part I). Submit only when all checks pass.

---

# Part III: Output Format

Template structure for generated question banks.

## Output Format

```markdown
## Contents

- [Question Bank](#question-bank-questions-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Q1: [Question text]](#q1-question-text)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Q2: [Question text]](#q2-question-text)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Question Bank (Questions 1–N)

### Topic 1: [Topic title]

#### Q1: [Question text]

**Language:** [python/javascript/solidity/N/A] | **Difficulty:** [Foundational/Intermediate/Advanced]

**Options:**
- A. [Option]
- B. [Option]
- C. [Option]
- D. [Option]

**Answer:** [A/B/C/D]

**Rationale:** [1–2 sentence explanation; include [Ref: ID] citations when referencing specifications, standards, research findings]

**Distractor notes:** [Why other options are incorrect; map each to specific misconception or outdated practice]

---

## Reference Sections

Use Reference IDs in your rationales to tie claims to sources: `[Ref: G3]` (Glossary entry 3), `[Ref: C1]` (Codebase entry 1), `[Ref: L2]` (Literature entry 2), `[Ref: A7]` (APA citation 7). Inline example: "The correct answer is B because consensus algorithms require Byzantine fault tolerance [Ref: G2] as specified in the protocol design [Ref: L5]."

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
- Stack/Modules: Core SDK or components relevant to questions
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
- Core Findings: Main claims, best practices, or standards referenced in questions
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


