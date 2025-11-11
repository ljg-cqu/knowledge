# True/False Statements

Generate high-quality true/false assessments with validated structure, authoritative citations, and multi-dimensional evaluation.

## Purpose & Scope

**Context**: This template generates senior/architect/expert-level true/false assessments for technical domains (blockchain, AI, software architecture, etc.). Statements test deep understanding through precise claims requiring nuanced evaluation.

**Assumptions**:
- Target audience: Senior engineers, architects, domain experts
- Domain: Technical fields with established standards, research, and production codebases
- Assessment goal: Evaluate conceptual understanding, not memorization

**Constraints**:
- Statements must be objectively verifiable through authoritative sources
- Avoid opinion-based or context-dependent claims without explicit qualification
- Exclude rapidly changing facts (e.g., "Latest version is X.Y.Z") unless dated

---

# Part I: Specifications

## Specifications

### Scope and Structure

**Statement Requirements** (MECE Coverage):
- **Count**: 18–32 statements covering 4-6 topic clusters (ensures comprehensive domain coverage)
- **Format**: Declarative, unambiguous (≤2 lines); no double negatives, no jargon without definition
- **Difficulty Distribution**: 20/40/40 (Foundational/Intermediate/Advanced) to balance accessibility and depth
  - *Foundational*: Core concepts, widely accepted principles
  - *Intermediate*: Implementation details, trade-offs, common patterns
  - *Advanced*: Edge cases, performance characteristics, security implications
- **Answer Format**: Machine-gradable (A/True or B/False)
- **Rationale**: 1–2 sentences explaining why statement is true/false, with authoritative citations
- **Conflict Handling**: For context-dependent statements, rationale MUST clarify assumptions, conditions, and boundaries

**Coverage Principles** (MECE):
- Each topic cluster addresses distinct aspect (mutually exclusive)
- All critical domain areas covered (collectively exhaustive)
- No overlap between statements (avoid testing same concept multiple times)

### Citation Standards (Credibility & Reliability)

**Source Quality Hierarchy** (prioritize high-quality, authoritative sources):
1. **Official docs**: Specifications, RFCs, protocol documentation (highest authority)
2. **Standards/peer-reviewed**: ISO, IEEE, academic journals, top-tier conferences (rigorous validation)
3. **Audits/reports**: Security audits from reputable firms, industry analyses from established organizations (tested in practice)
4. **Vetted code**: Production repositories with stable releases, active maintenance, security audits (proven reliability)

**Exclusions** (avoid low-quality sources):
- Blog posts, tutorials, unverified content (unless from recognized domain experts)
- Unmaintained repositories (last commit >12 months)
- Pre-release/experimental code without production validation
- Sources with known biases or conflicts of interest

**Language Distribution**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH], etc.)
- Reflects global technical discourse while including regional expertise

**Format**: APA 7th edition with language tags for clarity

**Inline Citation**: Use `[Ref: ID]` in rationales when referencing specifications, standards, research findings, or implementation details

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 | Core concepts, domain jargon, localized terms |
| Codebase & Library References | ≥5 | Primary stack, SDKs, tooling |
| Authoritative Literature & Reports | ≥6 | Standards, peer-reviewed work, industry analyses |
| APA Style Source Citations | ≥12 | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception:** If floor count unmet, state shortfall, rationale, and sourcing plan.

### Quality Gates (Accuracy, Credibility, Logic)

**Recency** (ensure current knowledge):
- ≥50% citations from last 3 years (general domains)
- ≥70% from last 2 years (fast-moving: AI, security, cloud-native)
- *Rationale*: Balance foundational knowledge with current best practices

**Source Diversity** (avoid bias, ensure balanced perspective):
- ≥3 source types (official docs, standards, audits, code)
- No single source >25% of total citations
- *Rationale*: Multiple perspectives reduce single-source bias

**Evidence Coverage** (verify claims):
- ≥70% statements with ≥1 authoritative citation
- ≥30% statements with ≥2 distinct citations (cross-validation)
- *Rationale*: Claims require evidence; critical claims need corroboration

**Codebase Maturity** (proven reliability):
- License: OSI-approved or clearly documented
- Last commit: ≤12 months (active maintenance)
- Stable release: Semantic versioning ≥1.0.0 or production-ready tag
- Audit status: Security audits from reputable firms (if applicable)
- *Rationale*: Production-ready code demonstrates practical viability

**Deduplication & Persistence** (maintain quality):
- Canonicalize entries (prefer official sources over mirrors)
- Use persistent links: DOIs, archived URLs (archive.org), official repositories
- *Rationale*: Prevent link rot, ensure long-term accessibility

**Link Validity** (practicality):
- All links must resolve OR archived alternative provided
- Test links before submission
- *Rationale*: Broken links undermine credibility

**Cross-Reference Integrity** (logic, coherence):
- Every `[Ref: ID]` in rationales must exist in Reference Sections
- IDs follow convention: G# (Glossary), C# (Codebase), L# (Literature), A# (APA)
- *Rationale*: Broken references indicate incomplete validation

**Conflict Resolution** (fairness, acknowledge limitations):
- For controversial/context-dependent statements, rationale MUST:
  - State assumptions explicitly
  - Acknowledge alternative perspectives
  - Cite sources for competing viewpoints
  - Clarify conditions under which statement is true/false
- *Rationale*: Technical truth often depends on context; transparency builds trust

> **Scaling**: For >32 statements or regulated domains (finance, healthcare), increase floor counts by ~1.5× (round up). Prioritize Quality Gates.

### Pre-Submission Validation (Self-Review, Error Checks)

**Purpose**: Ensure output meets all quality standards before submission. This is a mandatory self-review process.

**Process**: Execute ALL steps sequentially. Present validation report table. Fix failures and re-validate until all checks pass.

**Validation Steps**:

**Step 1 – Count Audit**
- Count: Glossary, Codebase, Literature, APA citations, Statements (total + by difficulty)
- Report: `G:X (≥10) | C:Y (≥5) | L:Z (≥6) | A:W (≥12) | S:N (F/I/A)`
- Pass: All counts meet minimums AND difficulty ratio ≈20/40/40

**Step 2 – Citation Coverage**
- Count inline `[Ref: ...]` in each rationale
- Report: `X of Y statements: ≥1 citation (Z%); W of Y: ≥2 citations (V%)`
- Pass: ≥70% have ≥1; ≥30% have ≥2

**Step 3 – Language Distribution**
- Count `[EN]`, `[ZH]`, other tags
- Report: `EN:X (Y%) | ZH:A (B%) | Other:C (D%)`
- Pass: EN ≈50-70%, ZH ≈20-40%, Other ≈5-15%

**Step 4 – Recency**
- Extract publication year from each citation
- Report: `X of Y citations (Z%) from last 3 years`
- Pass: ≥50% (≥70% for AI/security)

**Step 5 – Source Type Diversity**
- Classify each citation: (1) Official docs, (2) Standards/peer-reviewed, (3) Audits/reports, (4) Vetted code
- Report: `Types 1:X 2:Y 3:Z 4:W | Present:N | Max single:M (P%)`
- Pass: ≥3 types AND no single source >25%

**Step 6 – Link Validation**
- Test each URL or verify archived link
- Report: `X links: Y accessible, Z broken` (list broken)
- Pass: All accessible OR archived alternatives provided

**Step 7 – Cross-Reference Integrity**
- Verify each `[Ref: ID]` exists in Reference Sections (G#→Glossary, C#→Codebase, L#→Literature, A#→APA)
- Report: `X inline refs: Y resolve, Z broken` (list broken)
- Pass: All resolve (Z=0)

**Step 8 – Statement Clarity**
- Verify each statement: unambiguous, ≤2 lines
- Report: `X of Y clear; Z unclear/verbose` (list issues)
- Pass: All clear (Z=0)

**Step 9 – Double Negative Check**
- Verify no double negatives in each statement
- Report: `X of Y free; Z with double negatives` (list issues)
- Pass: All free (Z=0)

**Step 10 – Rationale Completeness**
- Verify each rationale: 1-2 sentences with citation
- Report: `X of Y complete; Z incomplete` (list issues)
- Pass: All complete (Z=0)

**Step 11 – Conflict Handling**
- Identify context-dependent statements; verify rationale clarifies assumptions/conditions
- Report: `X applicable; Y comply (Z%)`
- Pass: ≥80% comply

**Step 12 – Fairness & Balance**
- Verify controversial statements acknowledge alternative perspectives, limitations, or trade-offs
- Report: `X controversial; Y balanced (Z%)`
- Pass: ≥90% balanced

**Step 13 – Jargon Definition**
- Verify technical terms are defined in Glossary or explained in context
- Report: `X jargon terms; Y defined (Z%)`
- Pass: 100% defined

**Validation Report:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X C:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language dist | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Statement clarity | Y/X clear | PASS/FAIL |
| Double negatives | Y/X free | PASS/FAIL |
| Rationale completeness | Y/X complete | PASS/FAIL |
| Conflict handling | Y/X comply (Z%) | PASS/FAIL |
| Fairness & balance | Y/X balanced (Z%) | PASS/FAIL |
| Jargon definition | Y/X defined (Z%) | PASS/FAIL |
```

> **MANDATORY:** If ANY check fails, fix issues, regenerate affected sections, and re-validate. Proceed only when ALL checks pass.

### Submission Checklist (Success Criteria)

**Quantitative Criteria** (measurable outcomes):
- [ ] Floors met: G≥10, C≥5, L≥6, APA≥12
- [ ] Statement count: 18-32 total
- [ ] Difficulty distribution: 20/40/40 (Foundational/Intermediate/Advanced) ±5%
- [ ] Language distribution: ~60% EN, ~30% ZH, ~10% other ±10%
- [ ] Recency: ≥50% last 3yr (≥70% AI/security)
- [ ] Source diversity: ≥3 types, no single source >25%
- [ ] Evidence coverage: ≥70% with ≥1 citation; ≥30% with ≥2
- [ ] True/False balance: 45-55% True statements
- [ ] Citation coverage: 100% of rationales have ≥1 citation
- [ ] Link validity: 100% accessible or archived
- [ ] Cross-reference integrity: 100% resolved
- [ ] Jargon definition: 100% defined

**Qualitative Criteria** (actionable, implementable):
- [ ] Statement quality: ≤2 lines, unambiguous, no double negatives
- [ ] Rationale completeness: 1-2 sentences with clear reasoning
- [ ] Codebase maturity: license, update ≤12mo, stable release, audit status
- [ ] Conflict handling: Context-dependent statements clarify assumptions
- [ ] Fairness: Controversial statements acknowledge alternatives/limitations
- [ ] Answer format: A/True or B/False (machine-gradable)
- [ ] MECE coverage: Topics mutually exclusive, collectively exhaustive
- [ ] No answer patterns: Avoid TFTFTF or other detectable sequences

**Validation** (error checks):
- [ ] All 13 validation steps executed
- [ ] Validation report generated
- [ ] All checks show PASS status
- [ ] Failures fixed and re-validated

**Practicality** (implementable guidance):
- [ ] Statements testable by target audience (senior/architect/expert)
- [ ] Rationales provide learning value (not just "correct answer")
- [ ] References accessible to practitioners (not paywalled when possible)
- [ ] Glossary aids comprehension (defines domain-specific terms)

---

# Part II: Instructions

**Purpose**: Step-by-step workflow for generating high-quality true/false assessments with inline quality checks.

**Approach**: Execute steps sequentially. Perform inline checks after each step to catch issues early. Fix problems immediately before proceeding.

## Instructions

### Step 1: Topic Identification & Planning (MECE Coverage)

**Objective**: Identify comprehensive, non-overlapping topic clusters covering all critical domain areas.

**Actions**:
1. **Identify 4-6 topic clusters** (mutually exclusive):
   - Each cluster addresses distinct aspect of domain
   - No conceptual overlap between clusters
   - Examples: "Consensus Mechanisms", "Smart Contract Security", "Scalability Solutions"

2. **Allocate 3-6 statements per cluster** (collectively exhaustive):
   - Total: 18-32 statements
   - Ensure all critical concepts covered within each cluster
   - Prioritize high-value topics (frequently used, commonly misunderstood, security-critical)

3. **Assign difficulty levels** (balanced depth):
   - 20% Foundational: Core concepts, definitions, widely accepted principles
   - 40% Intermediate: Implementation details, trade-offs, common patterns
   - 40% Advanced: Edge cases, performance characteristics, security implications

4. **Inline Check**:
   - Total count = 18-32? ✓
   - Difficulty ratio ≈20/40/40 (±5%)? ✓
   - Clusters mutually exclusive? ✓
   - All critical areas covered? ✓
   - If any check fails, revise plan before proceeding

### Step 2: Reference Collection (Credibility & Reliability)

**Objective**: Gather authoritative, high-quality sources from diverse types.

**Actions**:
1. **Gather references** (prioritize quality over quantity):
   - ≥10 glossary entries: Core concepts, domain jargon, acronyms
   - ≥5 codebase references: Production repos, stable releases, audited code
   - ≥6 literature references: Standards, peer-reviewed papers, industry reports
   - ≥12 APA citations: Mix of official docs, research, audits, code

2. **For each reference, document**:
   - Language tag: [EN], [ZH], [JA], etc.
   - Publication year: For recency validation
   - Source type: (1) Official docs, (2) Standards/peer-reviewed, (3) Audits/reports, (4) Vetted code
   - Quality indicators: Citations, adoption, audit status, maintenance activity

3. **Assign unique IDs**:
   - G1-Gn: Glossary entries
   - C1-Cn: Codebase references
   - L1-Ln: Literature references
   - A1-An: APA citations

4. **Inline Check**:
   - Counts meet floors (≥10/5/6/12)? ✓
   - Language distribution (≈60/30/10)? ✓
   - Recency (≥50% last 3yr)? ✓
   - Source diversity (≥3 types, no single >25%)? ✓
   - All sources authoritative (no low-quality content)? ✓
   - Links valid or archived? ✓
   - If any check fails, gather additional/replacement sources

### Step 3: Statement Generation (Clarity, Precision, Logic)

**Objective**: Write clear, unambiguous statements with well-reasoned rationales.

**Actions**:
1. **Write each statement**:
   - **Declarative form**: Assert a specific claim (not a question)
   - **Unambiguous**: Single interpretation possible
   - **Concise**: ≤2 lines (avoid verbosity)
   - **No double negatives**: "X is not impossible" → "X is possible"
   - **No undefined jargon**: Define technical terms in Glossary
   - **Assign difficulty**: Foundational/Intermediate/Advanced
   - **Assign answer**: A (True) or B (False)

2. **Write each rationale**:
   - **Length**: 1-2 sentences (concise explanation)
   - **Content**: Explain WHY statement is true/false (not just restate)
   - **Citations**: ≥1 `[Ref: ID]` to authoritative source
   - **For context-dependent statements**: Clarify assumptions, conditions, boundaries
   - **For controversial statements**: Acknowledge alternatives, limitations, trade-offs

3. **Inline Check** (every 5 statements):
   - Statement ≤2 lines? ✓
   - No double negatives? ✓
   - Unambiguous (single interpretation)? ✓
   - Jargon defined? ✓
   - Rationale complete (1-2 sentences)? ✓
   - ≥1 citation per rationale? ✓
   - Context/alternatives acknowledged (if applicable)? ✓
   - If any check fails, revise statement/rationale immediately

### Step 4: Balance Verification (Fairness, Avoid Bias)

**Objective**: Ensure balanced distribution of True/False answers without detectable patterns.

**Actions**:
1. **Count True vs False answers**:
   - Target: 45-55% True statements (approximately balanced)
   - Rationale: Prevents test-taker from guessing strategy

2. **Verify no answer patterns**:
   - Check for sequences: TFTFTF, TTFFTTFF, etc.
   - Check for clustering: All True in Topic 1, all False in Topic 2
   - Randomize answer distribution across topics and difficulty levels

3. **Inline Check**:
   - True/False ratio = 45-55%? ✓
   - No detectable patterns (visual inspection)? ✓
   - Answers distributed across topics? ✓
   - Answers distributed across difficulty levels? ✓
   - If any check fails, reorder statements or revise answers (ensure correctness maintained)

### Step 5: Reference Section Compilation (Accuracy, Completeness)

**Objective**: Compile complete, well-formatted reference sections with all required fields.

**Actions**:
1. **Populate Glossary section**:
   - Format: `**G#: Term/Acronym**: Definition [Language Tag]`
   - Include: All technical terms used in statements
   - Ensure: Clear, concise definitions

2. **Populate Codebase section**:
   - Format: `**C#: Project/Library Name** ([lang])`
   - Required fields: Stack/Modules, Maturity (license, last update, stable release), Benchmarks
   - Optional fields: Integration hooks, reliability, language support, vulnerabilities

3. **Populate Literature section**:
   - Format: `**L#: Title** (Year) ([lang])`
   - Required fields: Core Findings, Methodology, Impact
   - Optional fields: Limitations, replication status, follow-up studies

4. **Populate APA Citations section**:
   - Format: APA 7th edition with language tags
   - Group by language: EN, ZH, Other
   - Include: Persistent links (DOIs, archived URLs)

5. **Match Reference IDs to inline citations**:
   - Every `[Ref: ID]` in rationales must have corresponding entry
   - Every reference entry should be cited at least once (remove unused)

6. **Inline Check**:
   - All `[Ref: ID]` resolve to Reference Sections? ✓
   - All required fields present? ✓
   - No unused references? ✓
   - APA format correct? ✓
   - Language tags present? ✓
   - Links valid or archived? ✓
   - If any check fails, fix references immediately

### Step 6: Pre-Submission Validation (Self-Review, Error Checks)

**Objective**: Comprehensive validation of all quality standards.

**Actions**:
1. Execute all 13 validation steps (Part I, Pre-Submission Validation section)
2. Generate validation report table with results for each check
3. For each FAIL status:
   - Identify root cause
   - Fix issue (revise statements, add references, correct formatting)
   - Re-run affected validation steps
4. Repeat until all checks show PASS status
5. Include final validation report in output

### Step 7: Final Review (Success Criteria Verification)

**Objective**: Verify all success criteria met before submission.

**Actions**:
1. Review Submission Checklist (Part I, Submission Checklist section)
2. Verify each checkbox item:
   - Quantitative criteria: Counts, ratios, percentages
   - Qualitative criteria: Clarity, completeness, fairness
   - Validation criteria: All checks passed
   - Practicality criteria: Testable, valuable, accessible
3. If any item unchecked, return to relevant step and fix
4. Submit only when all checkboxes checked

**Final Quality Assurance**:
- Read through complete output as if you were the target audience
- Verify statements are challenging but fair
- Verify rationales provide learning value
- Verify references are accessible and authoritative
- Verify output follows template format exactly

---

# Part III: Output Format

## Output Format

**Structure Requirements**:
- Start with Table of Contents (TOC) linking to all sections
- Use Markdown formatting: lists, tables, diagrams (Mermaid), formulas (LaTeX), code blocks (language-tagged)
- Follow template structure exactly (Contents → Statement Bank → Reference Sections)
- Use clear headings and consistent formatting

**Visual Elements** (when applicable):
- **Diagrams**: Use Mermaid for architecture, flows, relationships
- **Tables**: Use for comparisons, benchmarks, maturity indicators
- **Formulas**: Use LaTeX for mathematical expressions, performance calculations
- **Code blocks**: Use language-tagged fences for code examples, configurations

```markdown
## Contents

- [Statement Bank](#statement-bank-statements-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [S1: [Brief description]](#s1-brief-description)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [S2: [Brief description]](#s2-brief-description)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Statement Bank (Statements 1–N)

### Topic 1: [Topic title]

#### S1: [Brief description]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Statement:** [Declarative statement; may include [Ref: ID] citations for claims]

**Answer:** [A (True) / B (False)]

**Rationale:** [1–2 sentence explanation; include [Ref: ID] citations when referencing specifications, standards, research findings]

---

## Reference Sections

Use Reference IDs in rationales: `[Ref: G3]` (Glossary), `[Ref: C1]` (Codebase), `[Ref: L2]` (Literature), `[Ref: A7]` (APA). Example: "True: Byzantine fault tolerance [Ref: G4] requires >2/3 honest nodes per protocol specs [Ref: L2]."

### Minimum Entry Requirements

| Reference section | Floor count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 | Core concepts, domain jargon, localized terms |
| Codebase & Library References | ≥5 | Primary stack, SDKs, tooling |
| Authoritative Literature & Reports | ≥6 | Standards, peer-reviewed work, industry analyses |
| APA Style Source Citations | ≥12 | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception:** If floor count unmet, state shortfall, rationale, and sourcing plan.

### Glossary, Terminology & Acronyms

**Format:** `**G1: Term/Acronym**: Definition [Language Tag]`

**Example:** `**G1: MECE** (Mutually Exclusive, Collectively Exhaustive): Framework ensuring categories don't overlap and cover all possibilities [EN]`

### Codebase & Library References

**C1: [Project/Library Name]** ([lang])

**Must include:**
- Stack/Modules: Core SDK or components
- Maturity: License, last update ≤12mo, stable release
- Benchmarks: Performance, audit status, adoption

**Optional:**
- Integration hooks, reliability/HA, language support, vulnerability disclosures

**Format:** Repository URL (GitHub: owner/repo | License: Type), docs URL, maturity details

### Authoritative Literature & Reports

**L1: [Title]** (Year) ([lang])

**Must include:**
- Core Findings: Main claims, best practices, standards
- Methodology: Sample size, temporal scope
- Impact: Citations, industry adoption

**Optional:**
- Limitations, replication status, follow-up studies, regional applicability

**Format:** APA citation with language tag, persistent link (DOI or archived URL)

### APA Style Source Citations

List by language (~60% EN, ~30% ZH, ~10% other). Follow APA 7th with language tags.

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


