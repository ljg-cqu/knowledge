# Case Study / Scenario

Framework for generating high-quality case study/scenario assessments with proper structure, citations, and multi-dimensional evaluation.

---

# Part I: Specifications

Define quality requirements, standards, and constraints.

## Specifications

### Scope and Structure

- **Scope**: 16–22 scenarios for senior/expert level
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Context**: 200–400 words with constraints, stakeholders, technical details
- **Tasks**: 3–4 MECE tasks per scenario
- **Deliverables**: Issue lists, memos (≤300 words), matrices, communications
- **Trade-offs**: Privacy vs transparency, throughput vs consistency, cost vs resilience, decentralization
- **Grading**: Partial-credit checklists; document evidence, omissions, alternatives
- **Conflict Handling**: Solutions acknowledge competing approaches; clarify where experts agree vs disagree on framework choices

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH], etc.)
- **Source Types**: (1) Official docs (language specs, vendor docs, RFCs); (2) Standards/peer-reviewed (ISO, IEEE, academic journals, conference papers); (3) Audits/reports (security audits, industry analyses, regulatory guidance); (4) Vetted code (production repos with stable releases)
- **Format**: APA 7th with language tags
- **Distribution**: Codebase/libraries (repos, maturity, benchmarks); Literature/Reports
- **Inline Citation**: Use [Ref: ID] in context descriptions and rationales when referencing factual claims, metrics, comparisons, trade-offs, and best practices. Narrative/connective sentences may remain uncited.

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
- Evidence coverage: ≥70% of scenarios include ≥1 inline citation in context; ≥30% include ≥2 citations tied to distinct claims.
- Codebase maturity: Each codebase/library entry includes license, last commit ≤12 months, latest stable release, and security audit status (if available).
- Deduplication: Canonicalize and avoid duplicate entries; prefer persistent links (DOIs, standards bodies, archived URLs).
- Link validity: Validate that links resolve (or provide archived link) at time of delivery.
- Cross-reference binding: Use reference IDs and link scenarios to specific items in the Reference Sections.

> Scaling guidance: For sets >25 scenarios or regulated domains, increase floor counts by ~1.5× (round up) instead of unlimited growth. Prioritize meeting the Quality Gates first.

### Pre-Submission Validation

Execute ALL steps below. Present results in a validation report table. Fix any failures and re-run validation until all checks pass.

**Step 1 – Count Audit**
- Count: Glossary entries, Codebase entries, Literature entries, APA citations, Scenarios (total + by difficulty level)
- Report: `Glossary: X (target ≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Scenarios: N total (F foundational, I intermediate, A advanced)`
- Pass if: All counts meet minimums AND difficulty ratio ≈20/40/40

**Step 2 – Citation Coverage Scan**
- For EACH scenario context: Count inline `[Ref: ...]` occurrences
- Report: `X of Y scenarios have ≥1 citation (Z%); W of Y have ≥2 citations (V%)`
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
- For EACH `[Ref: ID]` in scenarios: Verify ID exists in Reference Sections (G#→Glossary, C#→Codebase, L#→Literature, A#→APA)
- Report: `Found X inline refs; Y resolve correctly, Z broken` (list broken refs)
- Pass if: All refs resolve (Z=0)

**Step 8 – Context Length Compliance**
- Select 5 random scenario contexts; count words
- Report: `S#: X words | S#: Y words | ...` (flag if <200 or >400)
- Pass if: All sampled contexts in 200–400 range

**Step 9 – Task MECE Verification**
- Review EACH scenario's tasks for mutual exclusivity and collective exhaustiveness
- Report: `X of Y scenarios have MECE tasks; Z have overlaps/gaps` (list issues)
- Pass if: All scenarios have MECE tasks (Z=0)

**Step 10 – Grading Rubric Completeness**
- For EACH scenario: Verify all tasks have rubrics with point allocations
- Report: `X of Y scenarios have complete rubrics; Z missing/incomplete` (list issues)
- Pass if: All scenarios have complete rubrics (Z=0)

**Step 11 – Conflict Handling Compliance**
- Identify scenarios with competing frameworks/approaches
- For EACH: Verify solutions acknowledge alternatives and clarify consensus vs dissent
- Report: `X applicable scenarios; Y comply (Z%)`
- Pass if: ≥80% comply OR rationale provided

**Validation Report Template:**
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
| Context lengths | 5/5 compliant | PASS/FAIL |
| MECE tasks | Y/X verified | PASS/FAIL |
| Grading rubrics | Y/X complete | PASS/FAIL |
```

> **MANDATORY:** If ANY check shows FAIL, stop, fix issues, regenerate affected sections, and re-run full validation. Only proceed to submission when ALL checks show PASS.

### Submission Checklist

- [ ] Floors met (Glossary ≥10, Codebase ≥5, Literature ≥6, APA citations ≥12)
- [ ] Difficulty distribution verified (20/40/40: Foundational/Intermediate/Advanced)
- [ ] Language distribution verified (~60% EN, ~30% ZH, ~10% other)
- [ ] Recency: ≥50% citations last 3 years (≥70% for AI/security)
- [ ] Diversity: ≥3 source types, no single source >25%
- [ ] Evidence coverage: ≥70% scenarios with ≥1 citation; ≥30% with ≥2 distinct citations
- [ ] Scenario quality: Each context 200–400 words, includes relevant citations
- [ ] Codebase maturity noted (license, last update ≤12 months, stable release, audit status)
- [ ] Links resolve or archived URLs provided
- [ ] Cross-references present (IDs used in scenarios and in Reference Sections)
- [ ] MECE tasks verified for all scenarios
- [ ] Grading rubrics complete with point allocations
- [ ] Pre-submission validation completed with passing results

---

# Part II: Instructions

Execute generation workflow with inline quality checks at each step.

## Instructions

Follow these steps in order. Execute inline quality checks at each step before proceeding.

### Step 1: Topic Identification & Planning
1. Identify 3-5 domain clusters (e.g., DeFi, Infrastructure, RWA)
2. Allocate 3-5 scenarios per cluster (total 16-22)
3. Assign difficulty levels to ensure 20/40/40 balance
4. **Inline Check**: Verify total scenarios = 16-22 AND difficulty ratio ≈20/40/40 before proceeding

### Step 2: Reference Collection
1. Gather ≥10 glossary terms, ≥5 codebase/libraries, ≥6 literature sources, ≥12 APA citations
2. For EACH source: Tag language ([EN], [ZH], etc.), note publication year, classify source type (1-4)
3. Assign Reference IDs: G1-Gn (Glossary), C1-Cn (Codebase), L1-Ln (Literature), A1-An (APA)
4. **Inline Check**: Count sources (≥10/5/6/12?), language split (≈60/30/10?), recency (≥50% last 3yr?), diversity (≥3 types?) before proceeding

### Step 3: Scenario Generation
1. For EACH scenario: Write context (200-400 words), assign difficulty + domain
2. In EACH context: Include ≥1 inline `[Ref: ID]` after factual claims, technical details, constraints
3. For EACH scenario: Design 3-4 MECE tasks with rubrics and point allocations
4. **Inline Check**: After every 3 scenarios, verify: context lengths 200-400, ≥1 citation per scenario, MECE tasks, complete rubrics

### Step 4: Grading Framework
1. For EACH task: Define expected responses, grading rubrics with partial credit
2. Document common omissions and edge cases
3. **Inline Check**: All tasks have rubrics? Point allocations sum correctly?

### Step 5: Reference Section Compilation
1. Populate Glossary, Codebase, Literature, APA sections with collected sources
2. Include all required information (must-include fields per format)
3. Ensure Reference IDs match inline citations
4. **Inline Check**: Every [Ref: ID] in scenarios resolves to an entry? All sources have required fields?

### Step 6: Pre-Submission Validation
Execute all 10 validation steps (see Part I > Pre-Submission Validation). Present validation report table. Fix any FAIL results and re-validate.

### Step 7: Final Review
Check Submission Checklist (see Part I). Submit only when all checks pass.

---

# Part III: Output Format

Template structure for generated scenario banks.

## Output Format

Use this structure when generating scenario banks:

```markdown
## Contents

- [Scenario Bank](#scenario-bank-scenarios-1-n)
- [Scenario 1: [Title]](#scenario-1-title)
- [Scenario 2: [Title]](#scenario-2-title)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Scenario Bank (Scenarios 1–N)

### Scenario X: [Title]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [DeFi/Infrastructure/RWA]

**Context:** (200–400 words with constraints, stakeholders, technical details; include [Ref: ID] citations)

**Task 1: Issue Identification (8 pts)**
[Task description]

**Expected Response:** [Key points]

**Grading:** [Rubric with partial credit]

**Task 2: Solution Proposal (10 pts)**
[Task description]

**Expected Response:** [Key points]

**Grading:** [Rubric]

**Task 3: Stakeholder Communication (6 pts)**
[Task description]

**Expected Response:** [Key points]

**Grading:** [Rubric]

**Common Omissions:** [List]

**Edge Cases for Bonus:** [Optional additional points]

---

## Reference Sections

Assign Reference IDs and reuse them inline in scenario contexts: Glossary (G1…Gn), Codebase (C1…Cn), Literature (L1…Ln), APA Citations (A1…An). Example inline: [Ref: C3, L2].

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

