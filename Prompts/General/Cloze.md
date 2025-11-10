# Cloze / Fill-in-the-Blank

Generate high-quality fill-in-the-blank assessments with citations and validation.

---

# Part I: Specifications

Quality requirements, standards, and constraints.

## Specifications

### Scope and Structure

- **Scope**: 24–40 items (senior/architect/expert level)
- **Format**: Unambiguous blanks (___); acceptable answer array
- **Difficulty**: 20% Foundational / 40% Intermediate / 40% Advanced
- **Normalization**: Case-insensitive, trim whitespace/punctuation; specify numeric tolerances
- **Grading**: Acceptance lists with tolerances; document borderline/partial credit answers
- **Conflicts**: Include valid variants for contested terminology (across schools/regions)

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH])
- **Source Types**: (1) Official docs (specs, RFCs); (2) Standards/peer-reviewed (ISO, IEEE, journals); (3) Audits/reports (security, industry); (4) Vetted code (production repos)
- **Format**: APA 7th with language tags
- **Inline**: [Ref: ID] for factual claims, definitions, technical specs; narrative text may remain uncited

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, domain-specific jargon, localized terminology |
| Codebase & Library References | ≥5 entries | Primary stack components, SDKs, supporting tooling |
| Authoritative Literature & Reports | ≥6 entries | Standards, peer-reviewed work, regulatory/industry analyses |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception handling:** If a section cannot meet the floor count, explicitly state the shortfall, provide rationale, and outline a plan to source additional materials.

### Quality Gates

- **Recency**: ≥50% citations last 3 years (≥70% last 2 years for AI/security)
- **Diversity**: ≥3 source types; no single source >25%
- **Evidence**: ≥70% items with ≥1 citation; ≥30% with ≥2 distinct citations
- **Maturity**: Each codebase entry includes license, last commit ≤12 months, stable release, audit status (if available)
- **Deduplication**: Canonicalize entries; prefer persistent links (DOIs, archived URLs)
- **Validity**: All links resolve or archived alternatives provided
- **Cross-refs**: Reference IDs link rationales to Reference Sections

> **Scaling**: For >50 items or regulated domains, increase floors by 1.5× (round up). Prioritize Quality Gates.

### Pre-Submission Validation

Execute ALL steps. Present results in validation report. Fix failures and re-run until all pass.

**Step 1 – Count Audit**
- Count: Glossary, Codebase, Literature, APA citations, Items (total + difficulty)
- Report: `Glossary: X (≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Items: N (F/I/A)`
- Pass: All minimums met AND difficulty ≈20/40/40

**Step 2 – Citation Coverage**
- Count inline `[Ref: ...]` per rationale
- Report: `X/Y items ≥1 citation (Z%); W/Y ≥2 citations (V%)`
- Pass: ≥70% with ≥1 citation AND ≥30% with ≥2 citations

**Step 3 – Language Distribution**
- Count `[EN]`, `[ZH]`, other tags
- Report: `EN: X (Y%) | ZH: A (B%) | Other: C (D%)`
- Pass: EN 50-70%, ZH 20-40%, Other 5-15%

**Step 4 – Recency**
- Extract publication year per citation
- Report: `X/Y citations (Z%) from 2022-2025`
- Pass: ≥50% last 3 years (≥70% for AI/security)

**Step 5 – Source Diversity**
- Classify citations: (1) Docs, (2) Standards, (3) Audits, (4) Code
- Report: `Type 1: X | Type 2: Y | Type 3: Z | Type 4: W | Types: N | Max: M (P%)`
- Pass: ≥3 types AND no source >25%

**Step 6 – Link Validation**
- Test URLs; verify archived alternatives
- Report: `Tested X: Y accessible, Z broken` (list broken)
- Pass: All accessible OR archived provided

**Step 7 – Cross-Reference Integrity**
- Verify `[Ref: ID]` exists: G#→Glossary, C#→Codebase, L#→Literature, A#→APA
- Report: `X refs: Y resolved, Z broken` (list broken)
- Pass: All resolved (Z=0)

**Step 8 – Answer Completeness**
- Verify non-empty, unambiguous answer lists
- Report: `X/Y complete; Z incomplete` (list issues)
- Pass: All complete (Z=0)

**Step 9 – Blank Clarity**
- Review blank placement clarity
- Report: `X/Y unambiguous; Z ambiguous` (list issues)
- Pass: All unambiguous (Z=0)

**Step 10 – Normalization**
- Verify rules specified (case, whitespace, punctuation, numeric tolerances)
- Report: `X/Y specified; Z missing` (list issues)
- Pass: All specified (Z=0)

**Step 11 – Conflict Handling**
- Identify contested terminology (multiple valid variants)
- Verify acceptance lists include ≥2 variants
- Report: `X applicable; Y comply (Z%)`
- Pass: ≥80% comply OR rationale provided

**Validation Report Template:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X C:Y L:Z A:W I:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language dist | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Answer lists | Y/X complete | PASS/FAIL |
| Blank clarity | Y/X unambiguous | PASS/FAIL |
| Normalization | Y/X specified | PASS/FAIL |
```

> **MANDATORY:** If ANY check FAILS, fix issues, regenerate, and re-validate. Submit only when ALL PASS.

### Submission Checklist

- [ ] Floors met (Glossary ≥10, Codebase ≥5, Literature ≥6, APA citations ≥12)
- [ ] Difficulty distribution verified (20/40/40: Foundational/Intermediate/Advanced)
- [ ] Language distribution verified (~60% EN, ~30% ZH, ~10% other)
- [ ] Recency: ≥50% citations last 3 years (≥70% for AI/security)
- [ ] Diversity: ≥3 source types, no single source >25%
- [ ] Evidence coverage: ≥70% items with ≥1 citation; ≥30% with ≥2 distinct citations
- [ ] Item quality: Unambiguous blanks, complete acceptable answer lists, normalization rules specified
- [ ] Codebase maturity noted (license, last update ≤12 months, stable release, audit status)
- [ ] Links resolve or archived URLs provided
- [ ] Cross-references present (IDs used in rationales and in Reference Sections)
- [ ] Pre-submission validation completed with passing results

---

# Part II: Instructions

Generation workflow with inline quality checks.

## Instructions

Follow sequentially. Execute inline checks before proceeding.

### Step 1: Topic Identification & Planning
1. Identify 4-6 topic clusters
2. Allocate 4-8 items per cluster (total 24-40)
3. Assign difficulty levels (20/40/40 balance)
4. **Check**: Total = 24-40 AND ratio ≈20/40/40

### Step 2: Reference Collection
1. Gather: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA citations
2. Per source: Tag language, year, type (1-4)
3. Assign IDs: G1-Gn, C1-Cn, L1-Ln, A1-An
4. **Check**: Counts ≥10/5/6/12, language ≈60/30/10, recency ≥50% last 3yr, diversity ≥3 types

### Step 3: Item Generation
1. Per item: Write unambiguous blank statement, assign difficulty
2. Per rationale: Include ≥1 `[Ref: ID]` for factual claims, definitions, specs
3. Per item: Define answer array and normalization rules
4. **Check** (every 6 items): Blanks clear, ≥1 citation, complete answers, rules specified

### Step 4: Grading Framework
1. Per item: Document incorrect/borderline answers
2. Specify tolerances and partial credit
3. **Check**: All items have grading guidance and comprehensive normalization

### Step 5: Reference Section Compilation
1. Populate all reference sections
2. Include required fields per format
3. Match Reference IDs to inline citations
4. **Check**: All [Ref: ID] resolve; all sources complete

### Step 6: Pre-Submission Validation
Execute all 11 validation steps (Part I). Present report. Fix failures and re-validate.

### Step 7: Final Review
Check Submission Checklist (Part I). Submit when all pass.

---

# Part III: Output Format

Standard template for item banks.

```markdown
## Contents

- [Item Bank](#item-bank-items-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Item 1: [Brief description]](#item-1-brief-description)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Item 2: [Brief description]](#item-2-brief-description)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Item Bank (Items 1–N)

### Topic 1: [Topic title]

#### Item 1: [Brief description]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Statement:** [Text with ___ or [blank]]

**Acceptable Answers:** ["answer1", "answer2", "answer3"]

**Grading:** [Rubric] | **Common incorrect:** [List]

**Rationale:** [Brief explanation with [Ref: ID] citations]

---

## Reference Sections

Assign Reference IDs and reuse them inline in rationales: Glossary (G1…Gn), Codebase (C1…Cn), Literature (L1…Ln), APA Citations (A1…An). Example inline: [Ref: G5, L2].

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

