# Multiple-Choice Questions

Framework for generating high-quality MCQ assessments for senior/architect/expert level roles.

---

# Part I: Specifications

## Specifications

### Scope and Structure

- **Quantity**: 40–80 questions
- **Format**: 1–2 sentence stems, 4 options (exactly one correct)
- **Difficulty**: 20% Foundational, 40% Intermediate, 40% Advanced
- **Distractors**: Map to specific misconceptions or outdated practices
- **Rationale**: 1–2 sentences with inline citations [Ref: ID]
- **Grading**: Machine-gradable, no partial credit
- **Contentious topics**: Distractors reflect competing views; rationale clarifies consensus

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH])
- **Source Types**: 
  1. Official docs (specs, RFCs, vendor docs)
  2. Standards/peer-reviewed (ISO, IEEE, journals, conferences)
  3. Audits/reports (security, industry, regulatory)
  4. Vetted code (stable production repos)
- **Format**: APA 7th edition with language tags
- **Inline**: [Ref: ID] in rationales for specs, standards, research

### Reference Minimums

| Section | Minimum | Notes |
| --- | --- | --- |
| Glossary & Terminology | ≥10 | Core concepts, jargon, acronyms |
| Codebase & Libraries | ≥5 | SDKs, frameworks, tools |
| Literature & Reports | ≥6 | Standards, peer-reviewed, audits |
| APA Citations | ≥12 | 60% EN, 30% ZH, 10% other |

> **Exception**: If minimums not met, state shortfall and sourcing plan.

### Quality Gates

- **Recency**: ≥50% from last 3 years (≥70% for AI/security)
- **Source diversity**: ≥3 types; no single source >25%
- **Evidence coverage**: ≥70% questions with ≥1 citation; ≥30% with ≥2 citations
- **Codebase maturity**: License, last commit ≤12 months, stable release, audit status
- **Deduplication**: Use persistent links (DOI, archived URLs); avoid duplicates
- **Link validity**: All links resolve or provide archived alternative
- **Cross-references**: All [Ref: ID] link to Reference Sections

> **Scaling**: For >80 questions or regulated domains, increase minimums by 1.5×.

### Pre-Submission Validation

Execute all steps. Present validation report. Fix failures and re-validate until all pass.

**1. Count Audit**
- Count: Glossary, Codebase, Literature, APA, Questions (by difficulty)
- Report: `G:X (≥10) | C:Y (≥5) | L:Z (≥6) | A:W (≥12) | Q:N (F/I/A)`
- Pass: All minimums met AND difficulty ≈20/40/40

**2. Citation Coverage**
- Count `[Ref: ...]` per rationale
- Report: `X/Y questions ≥1 citation (Z%); W/Y ≥2 citations (V%)`
- Pass: ≥70% with ≥1, ≥30% with ≥2

**3. Language Distribution**
- Count language tags: [EN], [ZH], other
- Report: `EN:X (Y%) | ZH:A (B%) | Other:C (D%)`
- Pass: EN 50-70%, ZH 20-40%, Other 5-15%

**4. Recency**
- Extract year from each citation
- Report: `X/Y (Z%) from last 3 years`
- Pass: ≥50% (≥70% for AI/security)

**5. Source Diversity**
- Classify: (1) Official, (2) Peer-reviewed, (3) Audits, (4) Code
- Report: `Type1:X Type2:Y Type3:Z Type4:W | Types:N | Max:M (P%)`
- Pass: ≥3 types AND max ≤25%

**6. Link Validation**
- Test each URL
- Report: `X links: Y accessible, Z broken` (list broken)
- Pass: All accessible OR archived provided

**7. Cross-Reference Integrity**
- Verify each [Ref: ID] exists (G#, C#, L#, A#)
- Report: `X refs: Y resolve, Z broken` (list broken)
- Pass: Z=0

**8. Answer Correctness**
- Verify exactly one correct per question
- Report: `X/Y exactly one; Z issues` (list)
- Pass: Z=0

**9. Distractor Quality**
- Verify distractors map to misconceptions
- Report: `X/Y quality; Z weak` (list)
- Pass: Z=0

**10. Option Clarity**
- Verify mutually exclusive, unambiguous options
- Report: `X/Y clear; Z vague` (list)
- Pass: Z=0

**11. Conflict Handling**
- Identify contentious topics; verify competing views represented
- Report: `X applicable; Y comply (Z%)`
- Pass: ≥80% comply

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

- [ ] Minimums: G≥10, C≥5, L≥6, A≥12
- [ ] Difficulty: 20/40/40 (F/I/A)
- [ ] Languages: 60% EN, 30% ZH, 10% other
- [ ] Recency: ≥50% last 3yr (≥70% AI/security)
- [ ] Diversity: ≥3 types, max 25%
- [ ] Citations: ≥70% questions ≥1, ≥30% ≥2
- [ ] Questions: One correct, quality distractors, clear options
- [ ] Codebase: License, update ≤12mo, release, audit
- [ ] Links: Resolve or archived
- [ ] Cross-refs: [Ref: ID] used and present
- [ ] Rationales: 1-2 sentences with citations
- [ ] Validation: All checks PASS

---

# Part II: Instructions

Execute steps sequentially with inline checks before proceeding.

### Step 1: Topic Planning
1. Identify 4-8 topic clusters
2. Allocate 5-10 questions per cluster (total 40-80)
3. Assign difficulty: 20/40/40 (F/I/A)
4. **Check**: Total=40-80, ratio≈20/40/40

### Step 2: Reference Collection
1. Gather: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA
2. Tag each: Language [EN]/[ZH], year, type (1-4)
3. Assign IDs: G1-Gn, C1-Cn, L1-Ln, A1-An
4. **Check**: Counts (10/5/6/12), languages (60/30/10), recency (≥50% 3yr), types (≥3)

### Step 3: Question Generation
1. Write: stem (1-2 sentences), 4 options (one correct), difficulty + language
2. Rationale: ≥1 [Ref: ID] for specs/standards/research
3. Distractors: Map to specific misconceptions
4. **Check** (every 10): One correct, quality distractors, ≥1 citation, clear options

### Step 4: Distractor Documentation
1. Document: Why incorrect, which misconception
2. Include common mistake patterns
3. **Check**: All distractors documented, misconceptions mapped

### Step 5: Reference Compilation
1. Populate: Glossary, Codebase, Literature, APA
2. Include required fields per format
3. Match Reference IDs to inline citations
4. **Check**: All [Ref: ID] resolve, all fields present

### Step 6: Validation
Execute all 11 validation steps (Part I). Present report. Fix failures, re-validate.

### Step 7: Final Review
Verify Submission Checklist (Part I). Submit when all pass.

---

# Part III: Output Format

Start the output with a TOC (e.g., '## Contents') linking to all top-level headings and list items.

- Use lists tables diagrams formulas code blocks; diagrams in Mermaid; code with language-tagged fences.

```markdown
## Contents

- [Question Bank](#question-bank-questions-1-n)
  - [Topic 1](#topic-1-topic-title)
  - [Topic 2](#topic-2-topic-title)
- [Reference Sections](#reference-sections)
  - [Glossary & Terminology](#glossary-terminology--acronyms)
  - [Codebase & Libraries](#codebase--library-references)
  - [Literature & Reports](#authoritative-literature--reports)
  - [APA Citations](#apa-style-source-citations)

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

**Rationale:** [1–2 sentences; use [Ref: ID] for specs/standards/research]

**Distractor notes:** [Why incorrect; map to specific misconception]

---

## Reference Sections

Use [Ref: ID] to cite sources: G# (Glossary), C# (Codebase), L# (Literature), A# (APA).

Example: "Answer B is correct because consensus algorithms require Byzantine fault tolerance [Ref: G2] per protocol design [Ref: L5]."

### Minimums

| Section | Minimum | Notes |
| --- | --- | --- |
| Glossary & Terminology | ≥10 | Core concepts, jargon, acronyms |
| Codebase & Libraries | ≥5 | SDKs, frameworks, tools |
| Literature & Reports | ≥6 | Standards, peer-reviewed, audits |
| APA Citations | ≥12 | 60% EN, 30% ZH, 10% other |

> **Exception**: If minimums not met, state shortfall and sourcing plan.

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

**C1: [Name]** ([lang])

Required:
- Stack: Core SDK/components
- Maturity: License, update ≤12mo, stable release
- Benchmarks: Performance, audit, adoption

Optional:
- Integration hooks, HA, language support, CVEs

Format: Repo URL (GitHub: owner/repo | License), docs, maturity.

### Authoritative Literature & Reports

**L1: [Title]** (Year) ([lang])

Required:
- Findings: Claims, practices, standards
- Methodology: Sample size, scope
- Impact: Citations, adoption

Optional:
- Limitations, replication, follow-ups, jurisdiction

Format: APA citation with tag, persistent link (DOI/archived).

### APA Style Source Citations

Group by language (60% EN, 30% ZH, 10% other). Use APA 7th with tags.

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


