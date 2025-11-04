# Interview Q&A

Framework for generating high-quality interview question banks with proper structure, citations, and multi-dimensional evaluation.

---

# Part I: Specifications

Define quality requirements, standards, and constraints.

## Specifications

### Scope and Structure

- **Scope**: 25–30 Q&A pairs for senior/expert level
- **Answer Length**: 150–300 words covering misconceptions, failure paths, trade-offs, decision criteria
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Artifacts**: ≥1 diagram + ≥1 table per topic cluster

### Content Principles

- **MECE Coverage**: Technical, theoretical, practical, contextual
- **Analysis Required**: Assumptions, failure paths, comparisons, trade-offs, adoption signals
- **Multi-Perspective**: Engineering, architecture, QA, product, operations, security, economics, policy

### Evaluation Dimensions

- **Technical**: Performance, security, scalability, reliability
- **Business**: Cost, efficiency, impact, market fit
- **Strategic**: Regulatory landscape, adoption barriers, competitive dynamics
- **Actionable**: Best practices, mitigations, open questions

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH], etc.)
- **Source Types**: (1) Official docs (language specs, vendor docs, RFCs); (2) Standards/peer-reviewed (ISO, IEEE, academic journals, conference papers); (3) Audits/reports (security audits, industry analyses, regulatory guidance); (4) Vetted code (production repos with stable releases)
- **Format**: APA 7th with language tags
- **Distribution**: Codebase/libraries (repos, maturity, benchmarks); Literature/Reports
- **Inline Citation**: Use [Ref: ID] immediately after factual claims, metrics, comparisons, trade-offs, best practices, security/compliance statements, and recommendations. Narrative/connective sentences may remain uncited.

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, domain-specific jargon, localized terminology |
| Codebase & Library References | ≥5 entries | Primary stack components, SDKs, supporting tooling |
| Authoritative Literature & Reports | ≥6 entries | Standards, peer-reviewed work, regulatory/industry analyses |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception handling:** If a section cannot meet the floor count, explicitly state the shortfall, provide rationale, and outline a plan to source additional materials.

### Usage Guidelines

1. **Structure & Coverage**: Follow complete framework structure and apply MECE principles
2. **Difficulty Balance**: Maintain 20/40/40 distribution (Foundational/Intermediate/Advanced)
3. **Reference Minimums**: Meet all floor counts (≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 citations)
4. **Language Distribution**: Include multilingual sources with tags (~60% EN, ~30% ZH, ~10% other)
5. **Format Consistency**: Maintain uniform formatting across all reference sections
6. **Visual Support**: Include supporting artifacts (diagrams, tables, code samples) per topic cluster
7. **Multi-Dimensional Analysis**: Address engineering, business, strategic, and operational perspectives
8. **Gap Management**: Document any shortfalls with rationale and remediation plan
9. **Per-Topic Minimums**: For each topic cluster, include ≥2 authoritative sources and ≥1 codebase/library reference tied to the answers.

### Quality Gates (recommend using these before raising floors)

- Recency: ≥50% of citations from the last 3 years; for fast-moving domains (AI, security), target ≥70% from the last 2 years.
- Source diversity: Include at least 3 source types (official docs, standards/peer-reviewed, audits/reports); no single source >25% of total citations.
- Evidence coverage: ≥70% of answers include ≥1 inline citation; ≥30% include ≥2 citations tied to distinct claims.
- Codebase maturity: Each codebase/library entry includes license, last commit ≤12 months, latest stable release, and security audit status (if available).
- Deduplication: Canonicalize and avoid duplicate entries; prefer persistent links (DOIs, standards bodies, archived URLs).
- Link validity: Validate that links resolve (or provide archived link) at time of delivery.
- Cross-reference binding: Use reference IDs and link answers to specific items in the Reference Sections.

> Scaling guidance: For sets >30 Q&A or regulated domains, increase floor counts by ~1.5× (round up) instead of unlimited growth. Prioritize meeting the Quality Gates first; higher floors without these gates rarely improve quality.

### Pre-Submission Validation

Execute ALL steps below. Present results in a validation report table. Fix any failures and re-run validation until all checks pass.

**Step 1 – Count Audit**
- Count: Glossary entries, Codebase entries, Literature entries, APA citations, Q&As (total + by difficulty level)
- Report: `Glossary: X (target ≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Q&As: N total (F foundational, I intermediate, A advanced)`
- Pass if: All counts meet minimums AND difficulty ratio ≈20/40/40

**Step 2 – Citation Coverage Scan**
- For EACH answer: Count inline `[Ref: ...]` occurrences
- Report: `X of Y answers have ≥1 citation (Z%); W of Y have ≥2 citations (V%)`
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
- For EACH `[Ref: ID]` in answers: Verify ID exists in Reference Sections (G#→Glossary, C#→Codebase, L#→Literature, A#→APA)
- Report: `Found X inline refs; Y resolve correctly, Z broken` (list broken refs)
- Pass if: All refs resolve (Z=0)

**Step 8 – Word Count Compliance**
- Select 5 random answers; count words (exclude metadata)
- Report: `Q#: X words | Q#: Y words | ...` (flag if <150 or >300)
- Pass if: All sampled answers in 150–300 range

**Step 9 – Key Insight Concreteness**
- Review EACH answer's Key Insight field
- Report: `X of Y answers have concrete insights; Z have generic/missing insights` (list generic ones)
- Pass if: All answers state specific misconception/failure/trade-off (Z=0)

**Step 10 – Per-Topic Minimums**
- For EACH topic cluster: List linked authoritative sources (L#/A#) and codebase refs (C#)
- Report: `Topic 1: [L1, A3, C2] → 2 auth + 1 code ✓ | Topic 2: [A5] → 1 auth + 0 code ✗`
- Pass if: EVERY topic has ≥2 authoritative + ≥1 codebase

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
| Word counts | 5/5 compliant | PASS/FAIL |
| Key Insights | Y/X concrete | PASS/FAIL |
| Per-topic mins | X/Y topics meet | PASS/FAIL |
```

> **MANDATORY:** If ANY check shows FAIL, stop, fix issues, regenerate affected sections, and re-run full validation. Only proceed to submission when ALL checks show PASS.

### Submission Checklist

- [ ] Floors met (Glossary ≥10, Codebase ≥5, Literature ≥6, APA citations ≥12)
- [ ] Difficulty distribution verified (20/40/40: Foundational/Intermediate/Advanced)
- [ ] Language distribution verified (~60% EN, ~30% ZH, ~10% other)
- [ ] Recency: ≥50% citations last 3 years (≥70% for AI/security)
- [ ] Diversity: ≥3 source types, no single source >25%
- [ ] Evidence coverage: ≥70% answers with ≥1 citation; ≥30% with ≥2 distinct citations
- [ ] Answer quality: Each answer 150–300 words, includes ≥1 [Ref: …], states concrete Key Insight
- [ ] Codebase maturity noted (license, last update ≤12 months, stable release, audit status)
- [ ] Links resolve or archived URLs provided
- [ ] Cross-references present (IDs used in answers and in Reference Sections)
- [ ] Per-topic minimums satisfied (≥2 authoritative + ≥1 codebase/library per topic)
- [ ] Pre-submission validation completed with passing results

---

# Part II: Instructions

Execute generation workflow with inline quality checks at each step.

## Instructions

Follow these steps in order. Execute inline quality checks at each step before proceeding.

### Step 1: Topic Identification & Planning
1. Identify 4-6 topic clusters covering the domain
2. Allocate 4-6 Q&As per cluster (total 25-30)
3. Assign difficulty levels to ensure 20/40/40 balance
4. **Inline Check**: Verify total Q&As = 25-30 AND difficulty ratio ≈20/40/40 before proceeding

### Step 2: Reference Collection
1. Gather ≥10 glossary terms, ≥5 codebase/libraries, ≥6 literature sources, ≥12 APA citations
2. For EACH source: Tag language ([EN], [ZH], etc.), note publication year, classify source type (1-4)
3. Assign Reference IDs: G1-Gn (Glossary), C1-Cn (Codebase), L1-Ln (Literature), A1-An (APA)
4. **Inline Check**: Count sources (≥10/5/6/12?), language split (≈60/30/10?), recency (≥50% last 3yr?), diversity (≥3 types?) before proceeding

### Step 3: Question & Answer Generation
1. For EACH Q&A: Write question, assign difficulty + type, draft 150-300 word answer
2. In EACH answer: Include ≥1 inline `[Ref: ID]` after factual claims, metrics, trade-offs, recommendations
3. For EACH answer: State one concrete Key Insight (specific misconception/failure/trade-off)
4. **Inline Check**: After every 5 Q&As, verify: word counts 150-300, ≥1 citation per answer, concrete Key Insights stated

### Step 4: Supporting Artifacts
1. Create ≥1 diagram + ≥1 table per topic cluster
2. Ensure artifacts directly support Q&A content
3. **Inline Check**: Count artifacts per cluster (≥1 diagram + ≥1 table each?) before proceeding

### Step 5: Reference Section Compilation
1. Populate Glossary, Codebase, Literature, APA sections with collected sources
2. Include all required information (must-include fields per format)
3. Ensure Reference IDs match inline citations
4. **Inline Check**: Every [Ref: ID] in answers resolves to an entry? All sources have required fields?

### Step 6: Pre-Submission Validation
Execute all 10 validation steps (see Part I > Pre-Submission Validation). Present validation report table. Fix any FAIL results and re-validate.

### Step 7: Final Review
Apply Question Design & Critique criteria (see Part I). Check Submission Checklist (see Part I). Submit only when all checks pass.

---

# Part III: Output Format

Template structure for generated question banks.

## Output Format Template

### Question Design & Critique

Before finalizing, review each question:

- Clarity: Single unambiguous ask; avoid double-barreled wording
- Signal: Tests reasoning/decision criteria, not trivia
- Depth: Enables discussion of failure modes, trade-offs, constraints
- Realism: Anchored in scenarios a senior/expert would face
- Discriminative power: Distinguishes shallow recall from practical expertise
- Alignment: Matches the stated seniority and target tech stack/context

---

## Output Format

Use this structure when generating question banks:

```markdown
## Contents

- [Topic Areas](#topic-areas-questions-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Q1: [Question text]](#q1-question-text)
  - [Q2: [Question text]](#q2-question-text)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Q3: [Question text]](#q3-question-text)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Topic Areas (Questions 1–N)

### Topic 1: [Topic title]

#### Q1: [Question text]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Type:** [Theoretical/Practical/Scenario]

**Answer:** (150-300 words with technical depth, examples, trade-offs)

**Key Insight:** [Choose one: Misconception | Failure Path | Trade-offs] - *Briefly state the core insight.*

**Supporting Artifacts:** [Mermaid Diagram/table/code/formula]

---

## Reference Sections

Use Reference IDs in your answers to tie claims to sources: `[Ref: G3]` (Glossary entry 3), `[Ref: C1]` (Codebase entry 1), `[Ref: L2]` (Literature entry 2), `[Ref: A7]` (APA citation 7). Inline example: "Byzantine fault tolerance [Ref: G2] requires >2/3 honest nodes in PBFT [Ref: C1], as demonstrated in production deployments [Ref: L4, A8]."

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
- Stack/Modules: Core SDK or components relevant to Q&As
- Maturity: License, last update ≤12 months, latest stable release
- Benchmarks: Performance data, security audit status, community adoption

Recommended:
- Integration Hooks
- Reliability/HA indicators
- Consistency guarantees
- Language support matrix
- Vulnerability disclosures

Format: Repository URL (GitHub: owner/repo | License: Type), documentation URL, maturity details.

### Authoritative Literature & Reports

**L1: [Title]** (Year) ([lang])

Must include:
- Core Findings: Main claims, best practices, or standards referenced in Q&As
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


