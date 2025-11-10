# True/False Statements

Generate high-quality true/false assessments with validated structure, citations, and multi-dimensional evaluation.

---

# Part I: Specifications

## Specifications

### Scope and Structure

- **Scope**: 18–32 statements (senior/architect/expert level)
- **Format**: Declarative (≤2 lines); no double negatives
- **Difficulty Distribution**: 20/40/40 (Foundational/Intermediate/Advanced)
- **Rationale**: 1–2 sentences with sources
- **Grading**: Machine-gradable (A/True or B/False)
- **Conflict Handling**: Rationale clarifies assumptions and conditions for context-dependent statements

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH])
- **Source Types**: (1) Official docs (specs, RFCs); (2) Standards/peer-reviewed (ISO, IEEE, journals, conferences); (3) Audits/reports (security audits, industry analyses); (4) Vetted code (production repos, stable releases)
- **Format**: APA 7th with language tags
- **Inline Citation**: Use [Ref: ID] in rationales for specifications, standards, research findings

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 | Core concepts, domain jargon, localized terms |
| Codebase & Library References | ≥5 | Primary stack, SDKs, tooling |
| Authoritative Literature & Reports | ≥6 | Standards, peer-reviewed work, industry analyses |
| APA Style Source Citations | ≥12 | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception:** If floor count unmet, state shortfall, rationale, and sourcing plan.

### Quality Gates

- **Recency**: ≥50% citations from last 3 years; fast-moving domains (AI, security): ≥70% from last 2 years
- **Source diversity**: ≥3 source types; no single source >25% of total
- **Evidence coverage**: ≥70% statements with ≥1 citation; ≥30% with ≥2 distinct citations
- **Codebase maturity**: Each entry includes license, last commit ≤12 months, stable release, audit status (if available)
- **Deduplication**: Canonicalize entries; prefer persistent links (DOIs, archived URLs)
- **Link validity**: All links resolve or archived alternative provided
- **Cross-reference binding**: Reference IDs link rationales to Reference Sections

> **Scaling**: For >32 statements or regulated domains, increase floor counts by ~1.5× (round up). Prioritize Quality Gates.

### Pre-Submission Validation

Execute ALL steps. Present validation report table. Fix failures and re-validate until all checks pass.

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
```

> **MANDATORY:** If ANY check fails, fix issues, regenerate affected sections, and re-validate. Proceed only when ALL checks pass.

### Submission Checklist

- [ ] Floors met (G≥10, C≥5, L≥6, APA≥12)
- [ ] Difficulty: 20/40/40 (Foundational/Intermediate/Advanced)
- [ ] Language: ~60% EN, ~30% ZH, ~10% other
- [ ] Recency: ≥50% last 3yr (≥70% AI/security)
- [ ] Diversity: ≥3 types, no source >25%
- [ ] Evidence: ≥70% with ≥1 citation; ≥30% with ≥2
- [ ] Statement quality: ≤2 lines, no double negatives, complete rationales (1-2 sentences)
- [ ] Codebase maturity: license, update ≤12mo, stable release, audit status
- [ ] Links: all resolve or archived
- [ ] Cross-refs: IDs in rationales and Reference Sections
- [ ] Answer format: A/True or B/False
- [ ] Validation: all checks pass

---

# Part II: Instructions

Execute generation workflow with inline quality checks.

## Instructions

### Step 1: Topic Identification & Planning
1. Identify 4-6 topic clusters
2. Allocate 3-6 statements per cluster (18-32 total)
3. Assign difficulty levels (20/40/40 balance)
4. **Check**: Total = 18-32 AND ratio ≈20/40/40

### Step 2: Reference Collection
1. Gather: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA citations
2. For each: tag language ([EN], [ZH]), note year, classify type (1-4)
3. Assign IDs: G1-Gn, C1-Cn, L1-Ln, A1-An
4. **Check**: Counts (≥10/5/6/12?), language (≈60/30/10?), recency (≥50% 3yr?), diversity (≥3 types?)

### Step 3: Statement Generation
1. Write each statement: declarative, ≤2 lines, no double negatives, assign difficulty + answer
2. Write each rationale: 1-2 sentences, ≥1 `[Ref: ID]` citation
3. **Check** (every 5 statements): ≤2 lines, no double negatives, ≥1 citation, complete rationale

### Step 4: Balance Verification
1. Count True vs False; ensure ≈50/50
2. Verify no answer patterns (e.g., TFTFTF)
3. **Check**: Ratio ≈50/50? No patterns?

### Step 5: Reference Section Compilation
1. Populate Glossary, Codebase, Literature, APA sections
2. Include required fields per format
3. Match Reference IDs to inline citations
4. **Check**: All [Ref: ID] resolve? Required fields present?

### Step 6: Pre-Submission Validation
Execute all 11 validation steps (Part I). Present validation report. Fix failures and re-validate.

### Step 7: Final Review
Check Submission Checklist (Part I). Submit when all checks pass.

---

# Part III: Output Format

## Output Format

Start the output with a TOC (e.g., '## Contents') linking to all top-level headings and list items.

- Use lists tables diagrams formulas code blocks; diagrams in Mermaid; code with language-tagged fences.

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


