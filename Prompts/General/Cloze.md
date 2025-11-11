# Cloze / Fill-in-the-Blank Prompt Template

Generate high-quality, verifiable fill-in-the-blank assessments with explicit context, success criteria, and validation safeguards.

---

## Overview

### Task Definition

Produce 24–40 senior-to-expert cloze items organized into topic clusters. Each item must include:
- Precise blanks with unambiguous context
- Complete acceptable answer arrays
- Detailed grading guidance with normalization rules
- Evidence-based rationales citing authoritative sources
- Risk assessment and fairness considerations

### Context & Assumptions

**Scope**: Define domain boundaries, exclusions (e.g., deprecated APIs, out-of-scope technologies), and dependencies before item creation.

**Audience**: Default level is senior professionals (5+ years experience). Adjust based on:
- Domain: Specify technical area, industry sector, regulatory environment
- Prerequisites: List required foundational knowledge, certifications, or experience
- Regional Standards: Note applicable jurisdictions, localization requirements, terminology variants
- Contested Terminology: Flag terms with multiple valid interpretations across schools of thought, regions, or standards bodies

**Constraints**: Document known limitations (time, available sources, emerging technologies with limited literature).

### Success Criteria

Delivery requires ALL of the following:

**Quantitative Floors** (non-negotiable minimums):
- Items: 24–40 total (20% Foundational / 40% Intermediate / 40% Advanced)
- References: ≥10 glossary entries, ≥5 codebase entries, ≥6 literature sources, ≥12 APA citations
- Language Distribution: ~60% EN, ~30% ZH, ~10% other
- Citation Coverage: ≥70% items with ≥1 citation; ≥30% items with ≥2 distinct citations

**Quality Gates** (objective thresholds):
- Recency: ≥50% citations from last 3 years (≥70% for AI/security domains)
- Diversity: ≥3 source types; no single source >25% of total
- Validity: 100% working links or archived alternatives
- Completeness: 100% items with non-empty answer arrays, normalization rules, grading rubrics

**Fairness Standards**:
- Acknowledge multiple valid perspectives (regional, methodological, stakeholder)
- Document assumptions, limitations, biases explicitly
- Flag high-risk misconceptions with mitigation strategies
- Balance trade-offs and counterarguments where applicable

**Validation Requirement**: Pass all 13 pre-submission validation checks (Section: Pre-Submission Validation). Any failure mandates revision and re-validation before delivery.

### Deliverables

1. **Item Bank**: 24–40 cloze items with complete metadata (difficulty, answers, grading, rationales)
2. **Reference Sections**: Glossary (≥10), Codebase (≥5), Literature (≥6), APA Citations (≥12)
3. **Table of Contents**: Linking to all sections and individual items
4. **Validation Report**: Demonstrating compliance with all 13 validation checks

---

---

# Part I: Specifications

## Purpose

Define quality requirements, standards, and constraints using MECE (Mutually Exclusive, Collectively Exhaustive) structure. Prioritize significant, actionable guidance.

## Specifications

### Task Context & Planning Assumptions

**Purpose**: Establish clear boundaries and assumptions before item creation to ensure MECE coverage and reproducibility.

**Required Documentation**:

1. **Scope Definition**:
   - Domain focus: Specify technical area, industry sector, application context
   - Coverage boundaries: Define what IS and IS NOT included
   - Exclusions: List deprecated technologies, out-of-scope topics, future roadmap items
   - Dependencies: Note prerequisite knowledge, required certifications, related domains

2. **Regulatory & Standards Context**:
   - Applicable jurisdictions: Geographic regions, legal frameworks, compliance requirements
   - Industry standards: ISO, IEEE, RFC, domain-specific standards bodies
   - Regional variations: Terminology, practices, regulatory differences

3. **Stakeholder Personas**:
   - Primary audience: Role, seniority level, typical responsibilities
   - Secondary stakeholders: Reviewers, auditors, implementers, operators
   - Perspective diversity: Developer vs. architect, operator vs. auditor, vendor vs. client

4. **Known Constraints**:
   - Resource limitations: Available authoritative sources, time constraints
   - Emerging technology gaps: Limited peer-reviewed literature, evolving best practices
   - Contested areas: Ongoing debates, competing methodologies, unresolved standards

5. **Methodology Choices**:
   - Taxonomy: Classification scheme for topics and difficulty levels
   - Scoring approach: Grading philosophy, partial credit policy, tolerance handling
   - Citation strategy: Source prioritization, recency vs. authority trade-offs

**Validation**: Confirm all planning assumptions are documented before proceeding to item generation.

### Scope and Structure

**Quantitative Requirements**:
- **Item Count**: 24–40 items total
- **Target Audience**: Senior/Architect/Expert level (5+ years domain experience)
- **Difficulty Distribution**: 20% Foundational / 40% Intermediate / 40% Advanced
  - Foundational: Core concepts, standard definitions, widely-accepted practices
  - Intermediate: Integration scenarios, trade-off analysis, common patterns
  - Advanced: Edge cases, optimization strategies, emerging practices, cross-domain synthesis

**Format Standards**:
- **Blank Notation**: Use ___ or [blank] consistently within each item bank
- **Unambiguous Context**: Ensure surrounding text provides sufficient constraints to eliminate incorrect interpretations
- **Answer Arrays**: Provide complete list of acceptable answers, including:
  - Primary answer (preferred terminology)
  - Valid synonyms and variants
  - Regional/school-specific alternatives
  - Abbreviations and acronyms (where applicable)

**Normalization Rules** (specify per item):
- **Case Sensitivity**: Typically case-insensitive unless distinction is critical (e.g., variable names, proper nouns)
- **Whitespace**: Trim leading/trailing spaces; normalize internal whitespace to single spaces
- **Punctuation**: Strip non-semantic punctuation (commas, periods); retain semantic punctuation (hyphens in compound terms)
- **Numeric Tolerances**: Specify acceptable ranges (e.g., "10% ±2%", "5.0 ±0.1")
- **Unit Handling**: Accept variations ("1000ms" = "1s" = "1 second")

**Grading Framework**:
- **Acceptance Criteria**: Define clear conditions for full credit
- **Partial Credit**: Specify scenarios and credit allocation (e.g., 50% for incomplete but directionally correct answers)
- **Common Incorrect Answers**: Document frequent misconceptions to support error analysis
- **Borderline Cases**: List edge cases requiring human judgment

**Conflict Resolution**:
- **Contested Terminology**: When multiple valid variants exist across schools/regions/standards:
  - Include ALL valid variants in acceptable answer array
  - Document source of each variant (e.g., "REST" [EN, ISO] vs "RESTful API" [EN, industry practice])
  - Note which variant is preferred in which context

**Breadth & Depth Requirements**:
- **MECE Coverage**: Topic clusters must be mutually exclusive and collectively exhaustive within defined scope
- **Multiple Perspectives**: Highlight diverse viewpoints where domain expects them:
  - Competing methodologies (Agile vs. Waterfall)
  - Regional practices (GDPR vs. CCPA)
  - Stakeholder priorities (performance vs. security)
- **Sufficient Detail**: Rationales must provide actionable insights, not superficial descriptions

**Logic & Cohesion**:
- **Sequencing**: Order items so foundational knowledge supports intermediate/advanced material
- **Dependencies**: Flag when items build on previous items (e.g., "Item 15 assumes knowledge from Item 8")
- **Cognitive Load**: Avoid clustering multiple advanced items on same complex topic without intermediate scaffolding

### Citation Standards

**Purpose**: Ensure credibility, verifiability, and balanced geographic/linguistic representation.

**Language Distribution Requirements**:
- **English (EN)**: ~60% of total citations
  - Rationale: Dominant language for international standards, peer-reviewed research, open-source projects
- **Chinese (ZH)**: ~30% of total citations
  - Rationale: Significant regional practices, regulatory frameworks, industry reports
- **Other Languages**: ~10% of total citations
  - Examples: Japanese (JA), Korean (KO), German (DE), French (FR), Russian (RU)
  - Rationale: Regional standards, specialized research, localized practices
- **Tagging**: Append language code in square brackets (e.g., [EN], [ZH], [JA])

**Source Type Classification**:

1. **Official Documentation**: Specifications, RFCs, W3C standards, vendor documentation
   - Priority: Primary source for definitions, technical specs, API contracts
   - Examples: RFC 9293 (TCP), OpenAPI Specification, Substrate Documentation

2. **Standards & Peer-Reviewed**: ISO, IEEE, academic journals, conference proceedings
   - Priority: Authoritative for best practices, benchmarks, theoretical foundations
   - Examples: ISO 27001, IEEE 802.11, ACM Digital Library, Springer journals

3. **Audits & Industry Reports**: Security audits, industry analyses, regulatory reports
   - Priority: Real-world evidence, risk assessments, compliance guidance
   - Examples: Trail of Bits audits, Gartner reports, regulatory filings

4. **Vetted Code**: Production repositories, widely-adopted libraries, reference implementations
   - Priority: Implementation patterns, API usage, integration examples
   - Requirements: License specified, last commit ≤12 months, stable release, audit status (if available)
   - Examples: Polkadot SDK, OpenZeppelin Contracts, Substrate Node Template

**Diversity Requirement**: Use ≥3 source types; no single source >25% of total citations.

**Format Requirements**:
- **Primary Standard**: APA 7th edition
- **Language Tags**: Mandatory for all citations (append after URL/DOI)
- **Persistent Identifiers**: Prefer DOIs over URLs where available
- **Archived Links**: Provide archive.org or alternative for non-persistent URLs
- **Access Dates**: Include for web resources without DOIs

**Inline Citation Rules**:
- **Mandatory Citation**: Use [Ref: ID] for:
  - Factual claims requiring verification
  - Technical definitions and specifications
  - Quantitative data and benchmarks
  - Controversial or contested statements
  - Domain-specific jargon or acronyms
- **Optional Citation**: Narrative context, general knowledge, transitional text
- **Multiple References**: Use [Ref: G5, L2, A8] for claims supported by multiple sources
- **Cross-Reference Format**: Match inline IDs to Reference Section IDs (G# = Glossary, C# = Codebase, L# = Literature, A# = APA Citations)

### Reference Minimum Requirements

**Purpose**: Establish quantitative baselines ensuring sufficient depth, breadth, and credibility.

| Reference Section | Floor Count | Purpose & Coverage |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, domain-specific jargon, acronyms, localized terminology variants, contested terms with multiple valid definitions |
| Codebase & Library References | ≥5 entries | Primary stack components, SDKs, frameworks, tooling, reference implementations, production-grade repositories |
| Authoritative Literature & Reports | ≥6 entries | ISO/IEEE standards, peer-reviewed papers, conference proceedings, regulatory reports, industry analyses, security audits |
| APA Style Source Citations | ≥12 total | Complete bibliographic entries covering all sources; Language distribution: ~60% EN / ~30% ZH / ~10% other |

**Sufficiency Validation**:
- **MECE Check**: Ensure references collectively cover all topic clusters without significant gaps
- **Depth Check**: Verify references provide actionable detail, not superficial overviews
- **Recency Check**: Confirm ≥50% of citations are from last 3 years (≥70% for rapidly-evolving domains like AI, security, blockchain)

**Exception Handling Protocol**:

If any section fails to meet floor count:

1. **Document Shortfall**:
   - Specify gap: "Glossary: 8/10 entries (2 short)"
   - Identify missing coverage: "Lack of ZH-specific terminology for regional practices"

2. **Provide Rationale**:
   - Explain constraint: "Limited peer-reviewed literature for technology released <12 months ago"
   - Justify severity: "Existing sources cover 90% of domain; gap is low-priority edge case"

3. **Mitigation Plan**:
   - Immediate: "Supplemented with vendor documentation and industry blog posts from reputable practitioners"
   - Follow-up: "Schedule quarterly review to incorporate peer-reviewed studies as they emerge"

4. **Risk Assessment**:
   - Flag impact: "Missing glossary entries may cause ambiguity for 2-3 items in advanced cluster"
   - Propose alternative: "Added extended rationales with inline definitions for affected items"

**Scaling Rule**: For >50 items or regulated domains (finance, healthcare, defense), increase all floor counts by 1.5× (round up).

### Quality Gates

**Purpose**: Define objective, measurable thresholds ensuring accuracy, credibility, and fairness.

**Recency Requirements**:
- **Standard Domains**: ≥50% of citations published within last 3 years
- **Rapidly-Evolving Domains** (AI, security, blockchain, cloud-native): ≥70% within last 2 years
- **Rationale**: Balance current best practices with established foundational knowledge
- **Exception**: Foundational references (seminal papers, RFCs, standards) exempt from recency requirement

**Source Diversity Requirements**:
- **Type Coverage**: Use ≥3 distinct source types (Official Docs, Standards/Peer-Reviewed, Audits/Reports, Vetted Code)
- **Concentration Limit**: No single source accounts for >25% of total citations
- **Rationale**: Prevent over-reliance on any single perspective or authority; ensure multiple independent validations
- **Validation**: Count citations by source type; flag violations requiring rebalancing

**Evidence Coverage Requirements**:
- **Baseline**: ≥70% of items include ≥1 inline citation [Ref: ID]
- **Enhanced**: ≥30% of items include ≥2 distinct citations from different source types
- **Rationale**: Factual claims require verification; complex/contested topics benefit from multiple independent sources
- **Exemptions**: Purely narrative or transitional items without factual claims

**Codebase Maturity Standards** (all required per entry):
- **License**: Clearly specified and compatible with intended use (MIT, Apache 2.0, GPL, etc.)
- **Activity**: Last commit ≤12 months ago OR explicit statement of stable/maintenance mode
- **Release Status**: Stable version number (≥1.0.0) OR clear beta/experimental designation
- **Audit Status**: Security audit findings (if available); note absence if not applicable
- **Risk Notes**: Known vulnerabilities, deprecated dependencies, breaking changes
- **Rationale**: Avoid recommending abandoned, insecure, or unstable codebases

**Deduplication & Canonicalization**:
- **Identify Duplicates**: Same source cited multiple times under different names/URLs
- **Canonical Form**: Use official name, persistent identifier (DOI), primary URL
- **Cross-References**: Link related sources (e.g., "See also: [Ref: A5] for updated methodology")
- **Version Control**: Specify version numbers for evolving standards/specifications

**Link Validity Requirements**:
- **Accessibility**: 100% of URLs must resolve to intended content
- **Persistence**: Prefer DOIs and permanent identifiers over mutable URLs
- **Archival**: Provide archive.org snapshots for non-persistent links
- **Broken Link Protocol**: If link fails validation:
  1. Search for updated URL or DOI
  2. Use archived version with date notation
  3. If unavailable, replace source or document limitation
- **Validation Timing**: Test all links immediately before final submission

**Cross-Reference Integrity**:
- **ID Matching**: Every inline [Ref: ID] must correspond to entry in Reference Sections
- **Prefix Validation**: G# → Glossary, C# → Codebase, L# → Literature, A# → APA Citations
- **Bidirectional Check**: All Reference Section entries should be cited at least once (orphaned entries indicate potential gaps)

**Risk & Value Assessment**:
- **Risk Flagging**: Explicitly note high-risk practices, controversial recommendations, emerging/unproven techniques
- **Mitigation Strategies**: For each flagged risk, provide:
  - Risk severity (Low/Medium/High)
  - Conditions under which risk is acceptable
  - Concrete mitigation steps (e.g., "Use only with additional authentication layer")
- **High-Value Insights**: Highlight particularly significant findings:
  - Performance improvements >20%
  - Security best practices
  - Cost reduction opportunities
  - Common anti-patterns to avoid

**Fairness & Bias Mitigation**:
- **Geographic Balance**: Acknowledge practices vary by region; avoid presenting single regional approach as universal
- **Stakeholder Perspectives**: Include multiple viewpoints:
  - Developer vs. Operator priorities
  - Security vs. Usability trade-offs
  - Vendor-specific vs. vendor-neutral solutions
- **Assumption Documentation**: Make implicit assumptions explicit (e.g., "Assumes Western regulatory context")
- **Limitation Acknowledgment**: Note boundaries of applicability (e.g., "Best practice for distributed systems; not applicable to single-server deployments")
- **Misconception Correction**: Identify and address common misunderstandings with evidence
- **Alternative Approaches**: Present valid alternatives where multiple approaches exist; explain trade-offs

**Scaling Adjustments**:
- **Trigger**: >50 items OR regulated/safety-critical domains (finance, healthcare, defense, aviation)
- **Adjustment**: Multiply all floor counts by 1.5× (round up)
  - Glossary: ≥10 → ≥15
  - Codebase: ≥5 → ≥8
  - Literature: ≥6 → ≥9
  - APA Citations: ≥12 → ≥18
- **Rationale**: Higher stakes require additional validation and depth
- **Priority**: Quality Gates take precedence over quantity; meeting validation checks is mandatory

### Pre-Submission Validation

**Purpose**: Ensure objective quality standards are met through systematic, reproducible checks.

**Critical Requirement**: Execute ALL 13 steps sequentially. Document results in validation report. If ANY step fails, fix issues and re-validate ALL steps before submission.

---

#### Step 1 – Count Audit (Quantitative Floors)

**Objective**: Verify all minimum reference counts and item distribution requirements are met.

**Procedure**:
1. Count entries in each Reference Section:
   - Glossary entries (G1, G2, ...)
   - Codebase entries (C1, C2, ...)
   - Literature entries (L1, L2, ...)
   - APA citations (A1, A2, ...)
2. Count total items and classify by difficulty (Foundational/Intermediate/Advanced)
3. Calculate difficulty distribution percentages

**Report Format**:
```
Glossary: X (≥10) | Codebase: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Items: N total (F Foundational, I Intermediate, A Advanced)
Difficulty Distribution: F% / I% / A% (Target: 20% / 40% / 40%)
```

**Pass Criteria**:
- Glossary ≥10 AND Codebase ≥5 AND Literature ≥6 AND APA Citations ≥12
- Difficulty distribution within ±5% of target (15-25% / 35-45% / 35-45%)
- Total items between 24-40

**If Failed**: Add missing entries or rebalance difficulty distribution.

---

#### Step 2 – Citation Coverage (Evidence Validation)

**Objective**: Verify factual claims are supported by authoritative sources.

**Procedure**:
1. For each item, count inline `[Ref: ID]` citations in rationale
2. Classify items: 0 citations, 1 citation, 2+ citations
3. Calculate percentages

**Report Format**:
```
Citation Coverage:
- Items with ≥1 citation: X/Y (Z%)
- Items with ≥2 citations: W/Y (V%)
- Items with 0 citations: M/Y (P%)
```

**Pass Criteria**:
- ≥70% of items have ≥1 citation
- ≥30% of items have ≥2 distinct citations

**If Failed**: Add citations to rationales for under-cited items; prioritize factual claims, definitions, technical specs.

---

#### Step 3 – Language Distribution (Geographic Balance)

**Objective**: Ensure balanced representation across linguistic/regional sources.

**Procedure**:
1. Count language tags across all citations: [EN], [ZH], [JA], [KO], [DE], [FR], [RU], etc.
2. Calculate percentages
3. Verify distribution aligns with targets

**Report Format**:
```
Language Distribution:
- English [EN]: X (Y%)
- Chinese [ZH]: A (B%)
- Other: C (D%)
Total Citations: N
```

**Pass Criteria**:
- English: 50-70%
- Chinese: 20-40%
- Other: 5-15%

**If Failed**: Rebalance by adding/replacing citations to meet target distribution; prioritize underrepresented high-quality sources.

---

#### Step 4 – Recency (Currency Validation)

**Objective**: Ensure majority of sources reflect current best practices.

**Procedure**:
1. Extract publication year from each citation
2. Calculate current year minus publication year
3. Count citations from last 3 years (2022-2025 if validating in 2025)
4. For AI/security/blockchain domains, count citations from last 2 years

**Report Format**:
```
Recency Analysis:
- Last 3 years (2022-2025): X/Y citations (Z%)
- Last 2 years (2023-2025): W/Y citations (V%)
- Domain type: [Standard/Rapidly-Evolving]
```

**Pass Criteria**:
- Standard domains: ≥50% from last 3 years
- Rapidly-evolving domains (AI, security, blockchain): ≥70% from last 2 years
- Exception: Foundational/seminal works exempt

**If Failed**: Replace outdated citations with recent sources; retain foundational references only if still authoritative.

---

#### Step 5 – Source Diversity (Perspective Balance)

**Objective**: Prevent over-reliance on single source type or authority.

**Procedure**:
1. Classify each citation by source type:
   - Type 1: Official Documentation (specs, RFCs, vendor docs)
   - Type 2: Standards/Peer-Reviewed (ISO, IEEE, journals)
   - Type 3: Audits/Reports (security audits, industry analyses)
   - Type 4: Vetted Code (production repos, reference implementations)
2. Count citations per type
3. Calculate percentage of largest single type
4. Count distinct source types used

**Report Format**:
```
Source Diversity:
- Type 1 (Official Docs): X citations
- Type 2 (Standards/Peer-Reviewed): Y citations
- Type 3 (Audits/Reports): Z citations
- Type 4 (Vetted Code): W citations
Distinct Types: N
Largest Single Type: M citations (P%)
```

**Pass Criteria**:
- ≥3 distinct source types used
- No single source type accounts for >25% of total citations

**If Failed**: Add citations from underrepresented types; replace over-represented sources with equivalent alternatives.

---

#### Step 6 – Link Validation (Accessibility)

**Objective**: Ensure all URLs resolve to intended content.

**Procedure**:
1. Extract all URLs from APA Citations, Codebase, and Literature sections
2. Test HTTP response (200 OK) for each URL
3. For broken links (404, 500, timeout), check if archived alternative exists
4. List all broken links without archived alternatives

**Report Format**:
```
Link Validation:
- Total URLs tested: X
- Accessible (200 OK): Y
- Broken with archive: Z
- Broken without archive: W
Broken Links: [list URLs]
```

**Pass Criteria**:
- 100% of URLs accessible OR archived alternative provided
- Zero broken links without archived alternatives

**If Failed**: Find updated URLs, use archive.org snapshots, or replace source.

---

#### Step 7 – Cross-Reference Integrity (Internal Consistency)

**Objective**: Verify all inline citations map to Reference Section entries.

**Procedure**:
1. Extract all inline `[Ref: ID]` from item rationales
2. For each ID, verify existence in corresponding Reference Section:
   - G# → Glossary
   - C# → Codebase
   - L# → Literature
   - A# → APA Citations
3. List broken references (ID cited but not found in Reference Section)
4. Optionally, identify orphaned references (Reference Section entry never cited)

**Report Format**:
```
Cross-Reference Integrity:
- Total inline references: X
- Resolved references: Y
- Broken references: Z
Broken: [list IDs]
Orphaned: [list IDs] (optional check)
```

**Pass Criteria**:
- 100% of inline references resolve to Reference Section entries (Z=0)

**If Failed**: Add missing Reference Section entries OR correct typos in inline citations.

---

#### Step 8 – Answer Completeness (Grading Validity)

**Objective**: Ensure all items have non-empty, unambiguous acceptable answer arrays.

**Procedure**:
1. For each item, verify:
   - Acceptable Answers array is non-empty
   - Acceptable Answers array contains at least 1 entry
   - Answers are specific (not placeholders like "TBD", "...")
2. List items with incomplete answer arrays

**Report Format**:
```
Answer Completeness:
- Total items: X
- Complete answer arrays: Y
- Incomplete/missing: Z
Incomplete Items: [list item numbers]
```

**Pass Criteria**:
- 100% of items have complete, non-empty answer arrays (Z=0)

**If Failed**: Populate missing answer arrays; ensure all valid variants included.

---

#### Step 9 – Blank Clarity (Ambiguity Detection)

**Objective**: Ensure blank placement provides sufficient context for unambiguous answers.

**Procedure**:
1. For each item, review statement containing blank(s)
2. Assess: Could surrounding context allow multiple unintended interpretations?
3. Check: Do acceptable answers match blank context?
4. List ambiguous items requiring revision

**Report Format**:
```
Blank Clarity:
- Total items: X
- Unambiguous blanks: Y
- Ambiguous blanks: Z
Ambiguous Items: [list item numbers with issue description]
```

**Pass Criteria**:
- 100% of items have unambiguous blank placement (Z=0)

**If Failed**: Revise item statements to add constraining context OR narrow acceptable answer arrays.

---

#### Step 10 – Normalization Rules (Grading Specification)

**Objective**: Ensure grading can be implemented consistently.

**Procedure**:
1. For each item, verify normalization rules specify:
   - Case sensitivity handling (case-insensitive/case-sensitive)
   - Whitespace handling (trim/normalize)
   - Punctuation handling (strip/retain)
   - Numeric tolerance (if applicable)
   - Unit handling (if applicable)
2. List items missing any normalization rule specification

**Report Format**:
```
Normalization Rules:
- Total items: X
- Complete rule specifications: Y
- Missing/incomplete: Z
Incomplete Items: [list item numbers with missing rules]
```

**Pass Criteria**:
- 100% of items have complete normalization rules specified (Z=0)

**If Failed**: Add normalization specifications to each item's grading section.

---

#### Step 11 – Conflict Handling (Terminology Variants)

**Objective**: Ensure contested terminology includes all valid regional/school variants.

**Procedure**:
1. Identify items involving contested terminology (multiple valid terms across regions/standards/schools)
2. For each applicable item, verify acceptable answers include ≥2 valid variants
3. Calculate compliance percentage

**Report Format**:
```
Conflict Handling:
- Items with contested terminology: X
- Items with ≥2 variants in answers: Y
- Compliance: Z%
Non-compliant Items: [list item numbers]
```

**Pass Criteria**:
- ≥80% of applicable items include multiple valid variants
- OR explicit rationale provided for single-variant answers

**If Failed**: Research regional/school variants; expand acceptable answer arrays; document why single variant is appropriate if applicable.

---

#### Step 12 – Fairness & Risk Review (Bias Mitigation)

**Objective**: Ensure balanced perspectives and transparent risk assessment.

**Procedure**:
1. **Stakeholder Coverage**: List stakeholder perspectives addressed (developer, operator, auditor, vendor, client, etc.)
2. **Regional Nuance**: Verify items acknowledge geographic/jurisdictional variations where applicable
3. **Risk Flagging**: Identify items discussing high-risk practices; verify risks are explicitly flagged
4. **Mitigation Strategies**: For each flagged risk, verify mitigation guidance is provided
5. **Assumption Documentation**: Check that implicit assumptions are made explicit

**Report Format**:
```
Fairness & Risk Review:
- Stakeholders covered: [list perspectives]
- Regional variations noted: X items
- Risks flagged: Y items (severity breakdown: Low X, Medium Y, High Z)
- Mitigations provided: W/Y (percentage)
- Assumptions documented: [count or list]
```

**Pass Criteria**:
- All material risks (Medium/High severity) have mitigation strategies
- Multiple stakeholder perspectives represented across item bank
- Regional/jurisdictional variations acknowledged where applicable
- Explicit assumption documentation for context-dependent guidance

**If Failed**: Add risk flags, mitigation strategies, stakeholder perspectives, or assumption documentation as needed.

---

#### Step 13 – Self-Check & Practicality Audit (Meta-Validation)

**Objective**: Confirm success criteria are met and guidance is actionable.

**Procedure**:
1. Review all previous validation steps for PASS status
2. Verify item bank is implementable:
   - Blanks can be realistically filled by target audience
   - Grading can be automated or consistently applied by humans
   - Rationales provide learning value beyond answer key
3. Check success criteria alignment:
   - Deliverables complete (item bank, references, TOC, validation report)
   - Quantitative floors met
   - Quality gates passed
   - Fairness standards satisfied
4. List any outstanding issues requiring resolution

**Report Format**:
```
Self-Check & Practicality:
- Previous validation steps: X/12 PASS
- Implementability: [Confirmed/Issues identified]
- Success criteria met: [Yes/No]
- Outstanding issues: [list or "None"]
```

**Pass Criteria**:
- All 12 previous validation steps PASS
- Item bank confirmed implementable and actionable
- All success criteria met
- Zero outstanding issues

**If Failed**: Resolve outstanding issues; re-run failed validation steps; confirm success criteria before submission.

---

#### Validation Report Template

**Purpose**: Provide at-a-glance summary of validation status.

**Format**:
```
| Check | Result | Status |
|-------|--------|--------|
| 1. Floors | G:X C:Y L:Z A:W I:N (F/I/A) | PASS/FAIL |
| 2. Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| 3. Language dist | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| 4. Recency | X% last 3yr | PASS/FAIL |
| 5. Source diversity | N types, max P% | PASS/FAIL |
| 6. Links | Y/X accessible | PASS/FAIL |
| 7. Cross-refs | Y/X resolved | PASS/FAIL |
| 8. Answer lists | Y/X complete | PASS/FAIL |
| 9. Blank clarity | Y/X unambiguous | PASS/FAIL |
| 10. Normalization | Y/X specified | PASS/FAIL |
| 11. Conflict handling | Y/X compliant (Z%) | PASS/FAIL |
| 12. Fairness & risk | Stakeholders:[...] Risks:[...] | PASS/FAIL |
| 13. Self-check | Issues: [Resolved/Outstanding] | PASS/FAIL |
```

**Submission Requirement**:
- **MANDATORY**: If ANY check shows FAIL status, fix issues and re-validate ALL steps.
- **Submit ONLY when**: All 13 checks show PASS status.
- **Include**: Validation report with final submission as evidence of compliance.

### Submission Checklist

**Purpose**: Final pre-submission verification ensuring all requirements are met.

**Instructions**: Review each item sequentially. All checkboxes must be confirmed before submission.

**Quantitative Requirements**:
- [ ] **Floors Met**: Glossary ≥10, Codebase ≥5, Literature ≥6, APA citations ≥12
- [ ] **Item Count**: Total items between 24-40
- [ ] **Difficulty Distribution**: Verified 20% Foundational / 40% Intermediate / 40% Advanced (±5% tolerance)
- [ ] **Language Distribution**: Verified ~60% EN, ~30% ZH, ~10% other (±10% tolerance)

**Quality Standards**:
- [ ] **Recency**: ≥50% citations from last 3 years (≥70% for AI/security/blockchain)
- [ ] **Source Diversity**: ≥3 source types used; no single source >25%
- [ ] **Evidence Coverage**: ≥70% items with ≥1 citation; ≥30% items with ≥2 distinct citations

**Item Quality**:
- [ ] **Blank Clarity**: All blanks unambiguous with sufficient context
- [ ] **Answer Completeness**: All items have complete acceptable answer arrays including valid variants
- [ ] **Normalization Rules**: All items specify case, whitespace, punctuation, numeric tolerance handling
- [ ] **Grading Rubrics**: All items include acceptance criteria, partial credit rules, common incorrect answers

**Source Quality**:
- [ ] **Codebase Maturity**: All entries note license, last update (≤12 months), stable release status, audit status
- [ ] **Link Validity**: All URLs resolve OR archived alternatives provided
- [ ] **Cross-Reference Integrity**: All inline [Ref: ID] citations map to Reference Section entries

**Fairness & Risk**:
- [ ] **Risk Documentation**: High-risk practices explicitly flagged with severity assessment
- [ ] **Mitigation Strategies**: All flagged risks include concrete mitigation guidance
- [ ] **Stakeholder Perspectives**: Multiple viewpoints represented (developer, operator, auditor, etc.)
- [ ] **Regional Variations**: Geographic/jurisdictional differences acknowledged where applicable
- [ ] **Assumption Transparency**: Implicit assumptions made explicit
- [ ] **Contested Terminology**: Valid variants included for terms with multiple regional/school interpretations

**Validation**:
- [ ] **Pre-Submission Validation**: All 13 validation steps completed with PASS status
- [ ] **Validation Report**: Included with submission showing all checks passed

**Deliverables Completeness**:
- [ ] **Item Bank**: 24-40 items with complete metadata (difficulty, statements, answers, normalization, grading, rationales)
- [ ] **Table of Contents**: Links to all sections and individual items
- [ ] **Reference Sections**: All four sections complete (Glossary, Codebase, Literature, APA Citations)
- [ ] **Validation Report**: Demonstrates compliance with all 13 checks

**Final Confirmation**:
- [ ] **Success Criteria Met**: All quantitative floors, quality gates, fairness standards satisfied
- [ ] **Actionable Guidance**: Items are implementable; rationales provide learning value
- [ ] **Zero Outstanding Issues**: All validation failures resolved

**Submission Authorization**: Confirmed that ALL checklist items are satisfied. Ready for submission.

---

---

# Part II: Instructions

## Purpose

Define step-by-step generation workflow with inline quality checks ensuring adherence to specifications.

## Instructions

**Execution Model**: Follow steps sequentially. Complete inline checks before proceeding to next step. If any check fails, resolve issues before advancing.

**Quality Philosophy**: Continuous validation prevents compounding errors; early detection reduces rework.

### Step 1: Topic Identification & Planning

**Objective**: Define comprehensive, non-overlapping topic coverage with balanced difficulty distribution.

**Procedure**:

1. **Identify Topic Clusters** (4-6 clusters):
   - Apply MECE principle: Mutually Exclusive (no overlap), Collectively Exhaustive (complete coverage)
   - Align clusters with domain scope defined in Task Context
   - Examples:
     - Blockchain: "Consensus Mechanisms", "Smart Contract Security", "Layer 2 Scaling", "Cryptographic Primitives"
     - Software Architecture: "Design Patterns", "Scalability Strategies", "Resilience Engineering", "Observability"

2. **Allocate Items per Cluster** (4-8 items each):
   - Total allocation: 24-40 items across all clusters
   - Balance breadth vs. depth: More clusters = broader coverage; more items per cluster = deeper coverage
   - Consider: Are some topics foundational (more items) vs. specialized (fewer items)?

3. **Assign Difficulty Levels**:
   - Target distribution: 20% Foundational / 40% Intermediate / 40% Advanced
   - Within each cluster: Mix difficulties to provide scaffolding
   - Foundational: Core definitions, standard practices
   - Intermediate: Integration, trade-offs, common patterns
   - Advanced: Edge cases, optimization, emerging practices

4. **Document Planning Assumptions**:
   - **Audience**: Seniority level, typical role, years of experience
   - **Prerequisites**: Required foundational knowledge ("Assumes understanding of TCP/IP")
   - **Regulatory Context**: Applicable jurisdictions, compliance frameworks ("GDPR context", "US financial regulations")
   - **Exclusions**: Out-of-scope topics ("Excludes deprecated APIs before v2.0", "Focuses on production deployments, not prototypes")
   - **Contested Areas**: Note topics with multiple valid interpretations ("REST vs RESTful terminology varies by source")

**Inline Check**:
- [ ] Total items = 24-40
- [ ] Difficulty ratio ≈ 20% / 40% / 40% (±5% tolerance)
- [ ] Clusters are MECE (no overlap, complete coverage of defined scope)
- [ ] Assumptions documented (audience, prerequisites, context, exclusions)

**If Check Fails**: Adjust item allocation, rebalance difficulty distribution, or refine cluster definitions.

**Output**: Topic matrix showing clusters, item count per cluster, difficulty distribution, documented assumptions.

### Step 2: Reference Collection

**Objective**: Gather high-quality, diverse, current sources meeting all quantitative and qualitative requirements.

**Procedure**:

1. **Gather Minimum Counts**:
   - **Glossary**: ≥10 entries (core terms, acronyms, domain jargon, localized variants)
   - **Codebase**: ≥5 entries (SDKs, frameworks, libraries, tooling, reference implementations)
   - **Literature**: ≥6 entries (ISO/IEEE standards, peer-reviewed papers, audits, industry reports)
   - **APA Citations**: ≥12 total (bibliographic entries for all sources)

2. **Tag Each Source**:
   - **Language**: Append [EN], [ZH], [JA], [KO], [DE], [FR], [RU], etc.
   - **Publication Year**: Extract from metadata (for recency validation)
   - **Source Type**: Classify as (1) Official Docs, (2) Standards/Peer-Reviewed, (3) Audits/Reports, (4) Vetted Code

3. **Assign Reference IDs**:
   - **Glossary**: G1, G2, G3, ..., Gn
   - **Codebase**: C1, C2, C3, ..., Cn
   - **Literature**: L1, L2, L3, ..., Ln
   - **APA Citations**: A1, A2, A3, ..., An
   - Ensure IDs are sequential and unique within each section

4. **Record Metadata per Source**:
   - **Credibility**: Peer-reviewed? Industry standard? Regulatory authority? Practitioner blog?
   - **Jurisdiction**: Applicable regions/markets ("Mainland China", "EU", "Global")
   - **Risk Notes**: Known controversies, methodological limitations, deprecated status
   - **Gaps**: Flag areas lacking authoritative sources; plan follow-up research

5. **Quality Assessment**:
   - **Relevance**: Does source directly support domain scope?
   - **Authority**: Is publisher reputable and domain-expert?
   - **Recency**: Is information current (or foundational/evergreen)?
   - **Accessibility**: Is source publicly accessible or requires institutional access?

**Inline Check**:
- [ ] Counts: Glossary ≥10, Codebase ≥5, Literature ≥6, APA ≥12
- [ ] Language distribution: ≈60% EN, ≈30% ZH, ≈10% other (±10% tolerance)
- [ ] Recency: ≥50% from last 3 years (≥70% for rapidly-evolving domains)
- [ ] Source diversity: ≥3 types used; no single type >25%
- [ ] Risk notes documented for controversial/limited/deprecated sources
- [ ] Gaps identified with mitigation plan ("Will supplement with vendor docs until peer-reviewed studies available")

**If Check Fails**: Add sources to meet floor counts; rebalance language distribution; replace outdated sources; diversify source types.

**Output**: Complete reference database with IDs, metadata, tags, risk notes, and gap documentation.

### Step 3: Item Generation

**Objective**: Create high-quality cloze items with unambiguous blanks, complete answer arrays, evidence-based rationales, and fairness considerations.

**Procedure** (per item):

1. **Write Statement with Blank**:
   - **Context Sufficiency**: Ensure surrounding text constrains answer space to eliminate unintended interpretations
   - **Blank Placement**: Position blank at key concept, not trivial detail
   - **Notation Consistency**: Use ___ or [blank] consistently within item bank
   - **Single vs. Multiple Blanks**: Default to single blank per item for clarity; use multiple only when testing related concepts

2. **Assign Difficulty Level**:
   - **Foundational**: Standard definitions, widely-known concepts ("TCP stands for ___")
   - **Intermediate**: Integration scenarios, trade-offs ("When choosing between REST and GraphQL for ___ use case, consider ___")
   - **Advanced**: Edge cases, optimization, synthesis ("To mitigate ___ attack vector in zero-knowledge proof systems, implement ___")

3. **Define Acceptable Answer Array**:
   - **Primary Answer**: Preferred term ("Transmission Control Protocol")
   - **Valid Synonyms**: Equivalents ("TCP protocol" — note: redundant but commonly used)
   - **Regional Variants**: Geographic terminology differences ("colour" [EN-GB] vs "color" [EN-US])
   - **Abbreviations**: Where applicable ("TCP", "T.C.P.")
   - **Case Variants**: If case-insensitive grading, list canonical form only

4. **Specify Normalization Rules**:
   - **Case**: case-insensitive (default) OR case-sensitive (if distinction matters, e.g., variable names)
   - **Whitespace**: Trim leading/trailing; normalize internal to single space
   - **Punctuation**: Strip non-semantic punctuation (commas, periods); retain semantic (hyphens in "zero-knowledge")
   - **Numeric Tolerance**: If answer is numeric, specify range ("10% ±2%", "5.0 ±0.1")
   - **Unit Handling**: Accept equivalent units ("1000ms" = "1s" = "1 second")

5. **Write Rationale**:
   - **Cite Evidence**: Include ≥1 [Ref: ID] for factual claims, definitions, technical specs
   - **Enhanced Items**: ≥30% of total items should have ≥2 distinct citations from different source types
   - **Address Limitations**: Note when answer has nuances ("While X is standard, Y is emerging practice in [context]")
   - **Provide Counterexample**: Where helpful, show incorrect approach ("Unlike synchronous blocking, asynchronous non-blocking...")
   - **Explain Significance**: Why does this concept matter? What are practical implications?

6. **Document Fairness Considerations**:
   - **Regional Variants**: Note if terminology/practices vary by jurisdiction ("US: 'labor', UK: 'labour'")
   - **Stakeholder Perspectives**: Acknowledge differing priorities ("Developers prioritize ease-of-use; operators prioritize reliability")
   - **Contested Terminology**: Flag when multiple schools/standards bodies define term differently
   - **Assumptions**: Make implicit assumptions explicit ("Assumes Linux environment unless specified")

**Inline Check** (every 6 items):
- [ ] Blanks are clear and unambiguous
- [ ] ≥70% of items (cumulative) have ≥1 citation
- [ ] ≥30% of items (cumulative) have ≥2 distinct citations from different source types
- [ ] 100% of items have complete answer arrays (no empty/placeholder answers)
- [ ] 100% of items have normalization rules specified
- [ ] Fairness notes address regional/stakeholder/terminology variations where applicable

**If Check Fails**: Revise items for clarity; add missing citations; populate answer arrays; specify normalization rules; add fairness documentation.

**Output**: Item bank entries with statements, difficulty labels, answer arrays, normalization rules, rationales with citations, fairness notes.

### Step 4: Grading Framework

**Objective**: Define clear, consistent, implementable grading criteria for each item.

**Procedure** (per item):

1. **Document Common Incorrect Answers**:
   - **Frequent Misconceptions**: List answers examinees commonly provide incorrectly
   - **Rationale**: Understanding error patterns informs teaching and remediation
   - **Examples**:
     - Correct: "Byzantine Fault Tolerance"
     - Incorrect: "Byzantine General Problem" (confuses algorithm with problem it solves)
     - Incorrect: "BFT Protocol" (too vague; multiple BFT protocols exist)

2. **Define Borderline Cases**:
   - **Partial Correctness**: Answers that are directionally correct but incomplete
   - **Context-Dependent**: Answers valid in some contexts but not target context
   - **Examples**:
     - Question: "___ is the minimum number of validators required for BFT consensus."
     - Full credit: "3f+1" OR "three times f plus one" OR "3*f+1 where f is maximum faulty nodes"
     - Partial credit (50%): "3f" (missing +1, but demonstrates understanding of fault tolerance relationship)
     - No credit: "51%" (confuses BFT with simple majority)

3. **Specify Partial Credit Allocation**:
   - **Percentage**: Define credit percentage for borderline cases (0%, 25%, 50%, 75%, 100%)
   - **Conditions**: State when partial credit applies
   - **Justification**: Explain reasoning ("Demonstrates understanding of core concept but lacks precision")

4. **Define Numeric Tolerances**:
   - **Acceptable Range**: For numeric answers, specify tolerance ("42 ±2", "99.9% ±0.1%")
   - **Rounding Rules**: Specify decimal places ("Round to 2 decimal places")
   - **Scientific Notation**: Accept equivalent forms ("1.5e6" = "1,500,000" = "1.5 million")

5. **Document Stakeholder-Specific Considerations**:
   - **Operator vs. Developer**: Different priorities may yield different "best" answers
   - **Example**:
     - Question: "Primary consideration when choosing database replication strategy: ___"
     - Developer answer: "Consistency guarantees"
     - Operator answer: "Operational complexity"
     - Both valid; context determines preference
   - **Grading Approach**: Accept both OR specify context more narrowly

6. **Note High-Risk Misconceptions**:
   - **Flag Dangerous Errors**: Mistakes that could lead to security vulnerabilities, data loss, compliance failures
   - **Provide Mitigation**: Explain why incorrect answer is risky; point to correct practice
   - **Example**:
     - Incorrect: "Use MD5 for password hashing"
     - Risk: "MD5 is cryptographically broken; vulnerable to collision attacks; passwords can be cracked"
     - Mitigation: "Use bcrypt, scrypt, or Argon2 with appropriate work factor" [Ref: L5, A12]

**Inline Check**:
- [ ] All items have grading guidance (acceptance criteria defined)
- [ ] All items specify normalization rules (case, whitespace, punctuation, numeric tolerance)
- [ ] Common incorrect answers documented for ≥50% of items (supports error analysis)
- [ ] Partial credit conditions specified for borderline cases
- [ ] High-risk misconceptions flagged with mitigation strategies
- [ ] Stakeholder perspective variations noted where applicable

**If Check Fails**: Add missing grading guidance; specify normalization rules; document incorrect answers; define partial credit; flag risks.

**Output**: Comprehensive grading rubrics per item including acceptance criteria, incorrect answers, partial credit rules, tolerances, risk notes, stakeholder considerations.

### Step 5: Reference Section Compilation

**Objective**: Populate all reference sections with complete, accurate, well-formatted entries ensuring cross-reference integrity.

**Procedure**:

1. **Populate Glossary, Terminology & Acronyms** (≥10 entries):
   - **Format per entry**:
     ```
     **Term/Acronym** (ID: G#): Definition [Language Tag]
     - Stakeholders affected: [list roles]
     - Notes: [key risks, assumptions, limitations, regional variants]
     ```
   - **Content**: Core concepts, domain jargon, acronyms, contested terms
   - **Example**:
     ```
     **Byzantine Fault Tolerance (BFT)** (ID: G3): Consensus mechanism tolerating arbitrary (Byzantine) failures where nodes may behave maliciously or unpredictably [EN]
     - Stakeholders affected: Distributed systems architects, blockchain developers
     - Notes: Requires ≥3f+1 nodes where f is maximum faulty nodes; higher overhead than crash fault tolerance
     ```

2. **Populate Codebase & Library References** (≥5 entries):
   - **Required Information**:
     - License (MIT, Apache 2.0, GPL, proprietary)
     - Last update: Last commit date OR latest stable version/release date
     - Supported languages/platforms
     - Integration surface (API, SDK, CLI, library)
   - **Recommended Information**:
     - Performance benchmarks
     - Security audit status
     - Consistency guarantees
     - Reliability/HA characteristics
   - **Include**: Known limitations, risk posture, mitigation guidance
   - **Format**:
     ```
     **[Project Name]** (ID: C#) (GitHub: owner/repo | License: Type)
     - Description: [brief overview]
     - Stack: [technologies]
     - Maturity: Production/Beta/Experimental
     - Last Update: [date] OR Version [X.Y.Z] ([date])
     - Performance: [key metrics if available]
     - Security: [audit status, known vulnerabilities]
     - Risks & Mitigations: [limitations] / [suggested hardening steps]
     ```

3. **Populate Authoritative Literature & Reports** (≥6 entries):
   - **Required Information**:
     - Type (Standard, White Paper, Academic Paper, Regulatory Report, Industry Analysis)
     - Publication year
     - Key findings/summary
     - Credibility (peer-reviewed, industry standard, regulatory authority)
     - Jurisdiction (applicable regions/markets)
   - **Recommended Information**:
     - Methodology/dataset
     - Limitations/assumptions
     - Stakeholder impact
   - **Format**:
     ```
     **[Title]** (ID: L#) (Year) [Language Tag]
     - Authors: [names/organization]
     - Type: [classification]
     - Key Findings: [summary]
     - Credibility: [validation source]
     - Jurisdiction: [applicability]
     - Stakeholder Impact: [affected parties] | Risks/Mitigations: [summary]
     ```

4. **Populate APA Style Source Citations** (≥12 entries):
   - **Follow APA 7th Edition**
   - **Append Language Tags**: [EN], [ZH], [JA], etc.
   - **Include**:
     - Persistent identifiers (DOIs preferred)
     - Access dates for web resources without DOIs
     - Archived links (archive.org) for non-persistent URLs
   - **Add Notes**:
     - Risk notes: "Limited sample size; supplement with [Ref: L3]"
     - Applicability: "Mainland China regulatory context"
     - Archive status: "Archive: https://web.archive.org/..."
     - Uncertainty flags: "Preprint; pending peer review"
   - **Group by Language**: Organize EN, then ZH, then other for readability

5. **Verify Cross-Reference Integrity**:
   - **Match IDs**: Every inline [Ref: ID] in item rationales must map to entry in Reference Sections
   - **Prefix Validation**: G# → Glossary, C# → Codebase, L# → Literature, A# → APA Citations
   - **Bidirectional Check**: Identify orphaned references (entries never cited) — may indicate gaps in rationales

6. **Document Shortfalls** (if applicable):
   - **State Gap**: "Glossary: 8/10 entries (2 short)"
   - **Provide Rationale**: "Emerging technology with limited standardized terminology"
   - **Mitigation Plan**: "Supplemented with vendor documentation; will update quarterly as standards emerge"

**Inline Check**:
- [ ] All Reference Section floors met (Glossary ≥10, Codebase ≥5, Literature ≥6, APA ≥12) OR shortfalls documented with mitigation
- [ ] All [Ref: ID] inline citations resolve to Reference Section entries (zero broken references)
- [ ] All Reference Section entries include required fields per format specifications
- [ ] Codebase entries include license, last update, maturity, risks
- [ ] Literature entries include type, year, credibility, jurisdiction
- [ ] APA citations include language tags, DOIs/URLs, archived links where applicable
- [ ] Risk notes, applicability boundaries, uncertainty flags documented

**If Check Fails**: Add missing entries; fix broken cross-references; populate required fields; document shortfalls with mitigation plans.

**Output**: Four complete Reference Sections with all required metadata, cross-reference integrity validated, shortfalls (if any) documented with mitigation.

### Step 6: Pre-Submission Validation

**Objective**: Execute comprehensive validation protocol ensuring all quality standards are met.

**Procedure**:

1. **Execute All 13 Validation Steps** (see Section: Pre-Submission Validation in Part I):
   - Step 1: Count Audit (quantitative floors)
   - Step 2: Citation Coverage (evidence validation)
   - Step 3: Language Distribution (geographic balance)
   - Step 4: Recency (currency validation)
   - Step 5: Source Diversity (perspective balance)
   - Step 6: Link Validation (accessibility)
   - Step 7: Cross-Reference Integrity (internal consistency)
   - Step 8: Answer Completeness (grading validity)
   - Step 9: Blank Clarity (ambiguity detection)
   - Step 10: Normalization Rules (grading specification)
   - Step 11: Conflict Handling (terminology variants)
   - Step 12: Fairness & Risk Review (bias mitigation)
   - Step 13: Self-Check & Practicality Audit (meta-validation)

2. **Document Results** in Validation Report:
   - Use template provided in Part I
   - Show PASS/FAIL status for each check
   - Include quantitative results (counts, percentages)
   - List any issues identified (broken links, missing citations, etc.)

3. **Fix Failures**:
   - For each FAIL status, follow remediation guidance in validation step
   - Re-execute failed checks after fixes
   - Repeat until all checks PASS

4. **Re-Validate After Changes**:
   - If fixes affect multiple sections, re-run ALL 13 validation steps
   - Rationale: Changes may have cascading effects (e.g., adding citation affects Step 2, 3, 4, 5)

**Critical Requirement**: ALL 13 validation steps must show PASS status before proceeding to Step 7.

**Inline Check**:
- [ ] All 13 validation steps executed
- [ ] Validation report completed with results
- [ ] All checks show PASS status (zero FAIL)
- [ ] Any identified issues resolved

**If Check Fails**: Return to relevant generation step (Steps 1-5); fix root cause; re-run full validation protocol.

**Output**: Complete validation report demonstrating compliance with all 13 checks.

### Step 7: Final Review

**Objective**: Perform holistic quality assessment confirming practical applicability, balanced perspectives, and evidence-based content.

**Procedure**:

1. **Review Submission Checklist** (Part I):
   - Verify all checkbox items confirmed
   - Ensure no outstanding items remain unchecked

2. **Assess Practical Applicability**:
   - **Implementability**: Can items be realistically graded by target audience or automated systems?
   - **Learning Value**: Do rationales provide actionable insights beyond mere answer keys?
   - **Relevance**: Do items align with real-world scenarios target audience will encounter?
   - **Difficulty Appropriateness**: Are foundational items accessible? Are advanced items sufficiently challenging?

3. **Verify Balanced Perspectives**:
   - **Stakeholder Diversity**: Are multiple viewpoints represented (developer, operator, auditor, vendor, client)?
   - **Regional Coverage**: Are geographic/jurisdictional variations acknowledged?
   - **Methodological Balance**: When multiple valid approaches exist, are alternatives presented with trade-offs?
   - **Assumption Transparency**: Are implicit assumptions made explicit?

4. **Confirm Cited Evidence**:
   - **No Unsupported Claims**: Verify factual assertions have [Ref: ID] citations
   - **Source Quality**: Confirm citations are authoritative, current, and relevant
   - **Cross-Reference Integrity**: Final check that all inline citations resolve

5. **Check Deliverables Completeness**:
   - [ ] **Item Bank**: 24-40 items with complete metadata
   - [ ] **Table of Contents**: Links to all sections and items
   - [ ] **Reference Sections**: All four sections complete (Glossary, Codebase, Literature, APA)
   - [ ] **Validation Report**: Demonstrating all 13 checks passed

6. **Perform Final Self-Assessment**:
   - **Question**: "Would this item bank provide fair, accurate, actionable assessment of target audience?"
   - **Question**: "Are success criteria fully met without exceptions or compromises?"
   - **Question**: "Is documentation sufficient for independent reviewer to validate quality?"

**Inline Check**:
- [ ] Submission Checklist: All items confirmed
- [ ] Practical applicability: Items are implementable, relevant, appropriately challenging
- [ ] Balanced perspectives: Multiple stakeholders, regions, methodologies represented
- [ ] Cited evidence: All factual claims supported by authoritative sources
- [ ] Deliverables complete: Item bank, TOC, references, validation report
- [ ] Self-assessment: Confident in quality, fairness, accuracy

**If Check Fails**: Identify root cause; return to relevant step; fix issue; re-run affected validation steps; repeat Final Review.

**Output**: Final item bank package ready for submission, with confidence that all quality standards are met.

**Submission Authorization**: Confirmed ready for delivery. All specifications satisfied.

---

---

# Part III: Output Format

## Purpose

Define standard template structure ensuring consistency, navigability, and completeness across all item bank deliverables.

## Template Structure

The following template provides required sections, formatting conventions, and example content.

---

## Contents

**Purpose**: Enable quick navigation to any section or individual item.

**Format**: Markdown table of contents with anchor links.

**Structure**:
- **Item Bank**: Link to main item bank section
  - **Topic Clusters**: Link to each topic cluster
    - **Individual Items**: Link to each item within cluster
- **Reference Sections**: Link to reference section container
  - **Glossary**: Link to glossary section
  - **Codebase**: Link to codebase section
  - **Literature**: Link to literature section
  - **APA Citations**: Link to APA citations section
- **Validation Report**: Link to validation report (if included in same document)

**Example**:
```markdown
## Contents

- [Item Bank](#item-bank-items-1-n)
  - [Topic 1: Consensus Mechanisms](#topic-1-consensus-mechanisms)
    - [Item 1: Byzantine Fault Tolerance](#item-1-byzantine-fault-tolerance)
    - [Item 2: Proof of Stake](#item-2-proof-of-stake)
  - [Topic 2: Smart Contract Security](#topic-2-smart-contract-security)
    - [Item 3: Reentrancy Attacks](#item-3-reentrancy-attacks)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)
- [Validation Report](#validation-report)
```

---

## Item Bank (Items 1–N)

**Purpose**: Present all cloze items organized by topic clusters with complete metadata.

**Organization**: Group items by topic cluster; sequence within cluster by difficulty (Foundational → Intermediate → Advanced) for scaffolding.

### Topic 1: [Topic Title]

**Context**: [Optional: Brief introduction to topic cluster scope, relevance, prerequisites]

#### Item 1: [Brief Description]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Statement:** [Sentence or paragraph containing ___ or [blank] placeholder(s)]

**Acceptable Answers:** ["primary answer", "synonym", "regional variant", "abbreviation", ...]

**Normalization & Tolerances:**
- **Case**: [case-insensitive / case-sensitive]
- **Whitespace**: [trim and normalize to single space / preserve]
- **Punctuation**: [strip non-semantic / retain all]
- **Numeric Tolerance**: [N/A / specify range: "±X%" or "±X units"]
- **Unit Handling**: [N/A / list equivalent units: "ms = milliseconds", "1000ms = 1s"]

**Grading:**
- **Full Credit**: [conditions for 100% credit]
- **Partial Credit**: [conditions and allocation: "50% for incomplete but directionally correct answer"]
- **Common Incorrect Answers**: ["misconception 1", "misconception 2", ...]
- **Borderline Cases**: ["edge case requiring human judgment: explanation"]

**Risk & Fairness Notes:**
- **Misconceptions**: [high-risk errors with mitigation: "Using MD5 for passwords is insecure [Ref: L5]; use bcrypt/Argon2 instead"]
- **Stakeholder Nuances**: ["Operators prioritize reliability; developers prioritize ease-of-implementation"]
- **Regional Variants**: ["US: 'color'; UK: 'colour'; both acceptable"]
- **Contested Terminology**: ["REST vs RESTful varies by source [Ref: G8, A14]"]

**Rationale:** [Explanation supporting correct answer(s) with inline citations [Ref: ID]. Include:
- **Definitions**: Technical terms with authoritative sources
- **Significance**: Why this concept matters
- **Context**: When/where/how applied
- **Limitations**: Boundary conditions, exceptions, trade-offs
- **Counterexamples**: Contrasting incorrect approaches
- **Cross-References**: Related items or concepts]

Example: "Byzantine Fault Tolerance (BFT) enables consensus in distributed systems where nodes may fail arbitrarily or behave maliciously [Ref: G3, L7]. Unlike crash fault tolerance, which assumes nodes fail by stopping, BFT tolerates Byzantine failures including message tampering, incorrect computations, and coordinated attacks [Ref: A22]. BFT consensus requires ≥3f+1 nodes where f is the maximum number of faulty nodes [Ref: L7]. While providing stronger safety guarantees, BFT protocols incur higher communication overhead (O(n²) message complexity) compared to crash fault tolerant alternatives [Ref: A22]. Common BFT implementations include PBFT (Practical Byzantine Fault Tolerance), Tendermint, and HotStuff [Ref: C2, C5]."

---

#### Item 2: [Brief Description]

[Repeat structure for each item...]

---

### Topic 2: [Topic Title]

[Repeat structure for each topic cluster...]

---

## Reference Sections

**Purpose**: Provide authoritative, verifiable sources supporting all factual claims in item rationales.

**Cross-Reference System**: 
- Assign unique IDs per section: G# (Glossary), C# (Codebase), L# (Literature), A# (APA Citations)
- Use inline citations in rationales: [Ref: G5, L2, A8]
- Ensure bidirectional integrity: All inline references resolve; all entries cited at least once (or note orphaned entries)

**Minimum Requirements**:

| Reference Section | Floor Count | Purpose |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, jargon, acronyms, regional variants |
| Codebase & Library References | ≥5 entries | SDKs, frameworks, libraries, tools, reference implementations |
| Authoritative Literature & Reports | ≥6 entries | Standards, peer-reviewed papers, audits, industry reports |
| APA Style Source Citations | ≥12 total | Complete bibliographic entries for all sources |

**Exception Handling**: If any section cannot meet floor count, explicitly state shortfall, provide rationale (e.g., "Emerging technology with limited peer-reviewed literature"), and outline mitigation plan (e.g., "Supplemented with vetted vendor documentation; quarterly review scheduled").

---

### Glossary, Terminology & Acronyms

**Purpose**: Define core concepts, domain-specific jargon, acronyms, and contested terms.

**Format**:
```text
**Term/Acronym** (ID: G#): Definition [Language Tag]
- Stakeholders affected: [roles impacted by this concept]
- Notes: [key risks, assumptions, limitations, regional variants, contested definitions]
```

**Content Requirements**:
- **Definitions**: Clear, concise, technically precise
- **Context**: When term is used, by whom, in what scenarios
- **Variants**: Regional, industry-specific, or school-specific alternatives
- **Risks**: Common misunderstandings, misapplications

**Example**:
```text
**MECE (Mutually Exclusive, Collectively Exhaustive)** (ID: G1): Analytical framework ensuring categories do not overlap (mutually exclusive) and cover all possibilities within defined scope (collectively exhaustive) [EN]
- Stakeholders affected: Business analysts, system architects, auditors
- Notes: Requires clear boundary definition to avoid classification bias; commonly applied in issue trees, process mapping, and taxonomy design

**Byzantine Fault Tolerance (BFT)** (ID: G3): Consensus mechanism enabling distributed systems to reach agreement despite arbitrary (Byzantine) node failures, including malicious behavior, message tampering, or incorrect computations [EN]
- Stakeholders affected: Distributed systems architects, blockchain developers, security engineers
- Notes: Requires ≥3f+1 nodes where f is maximum faulty nodes; higher communication overhead (O(n²)) than crash fault tolerance; critical for permissionless networks

**智能合约 (Smart Contract)** (ID: G8): 自动执行的区块链上程序，当预定条件满足时无需中介即可执行协议条款 [ZH]
- Stakeholders affected: 区块链开发者, DApp 用户, 审计员
- Notes: 不可变性意味着部署后难以修复漏洞；常见平台包括 Ethereum (Solidity), Polkadot (ink!), Solana (Rust)
```

---

### Codebase & Library References

**Purpose**: Document production-grade code repositories, SDKs, frameworks, and tools.

**Required Information**:
- **License**: Type (MIT, Apache 2.0, GPL, proprietary) and implications
- **Last Update**: Last commit date OR latest stable version with release date
- **Maturity**: Production / Beta / Experimental / Maintenance Mode
- **Supported Platforms**: Languages, operating systems, architectures
- **Integration Surface**: API, SDK, CLI, library, framework

**Recommended Information**:
- **Performance**: Benchmarks, throughput, latency characteristics
- **Security**: Audit status, known vulnerabilities, CVEs, hardening guidance
- **Consistency Guarantees**: ACID properties, eventual consistency, strong consistency
- **Reliability**: HA features, fault tolerance, disaster recovery

**Format**:
```text
**[Project/Library Name]** (ID: C#) (GitHub: owner/repo | License: Type)
- Description: [Brief overview of purpose and capabilities]
- Stack: [Technologies, languages, dependencies]
- Maturity: [Production/Beta/Experimental/Maintenance]
- Last Update: [YYYY-MM-DD] OR Version [X.Y.Z] ([YYYY-MM-DD])
- Supported Platforms: [Languages, OS, architectures]
- Integration: [API/SDK/CLI/Library/Framework]
- Performance: [Key metrics if available: throughput, latency, resource usage]
- Security: [Audit status, known vulnerabilities, hardening recommendations]
- Risks & Mitigations: [Known limitations, breaking changes, deprecated features] / [Suggested mitigations, alternative approaches]
```

**Example**:
```text
**Substrate** (ID: C2) (GitHub: paritytech/substrate | License: Apache 2.0)
- Description: Modular blockchain framework for building custom blockchains with composable runtime modules (pallets)
- Stack: Rust, WASM, libp2p
- Maturity: Production (powers Polkadot, Kusama, 100+ parachains)
- Last Update: Version 3.0.0 (2024-01-15)
- Supported Platforms: Linux, macOS, Windows; Rust ≥1.70
- Integration: Framework (runtime development), SDK (client libraries), CLI (node template)
- Performance: 1000+ TPS (single chain), 100,000+ TPS (with parachains); <3s finality (GRANDPA)
- Security: Multiple audits by Trail of Bits, SR Labs; active bug bounty program
- Risks & Mitigations: Complexity requires deep Rust expertise; runtime upgrades can introduce consensus-breaking changes / Use testnet validation; follow runtime upgrade best practices [Ref: L4]

**OpenZeppelin Contracts** (ID: C5) (GitHub: OpenZeppelin/openzeppelin-contracts | License: MIT)
- Description: Audited library of reusable Solidity smart contract components (ERC standards, access control, security patterns)
- Stack: Solidity, Ethereum, EVM-compatible chains
- Maturity: Production (industry standard; used by >50% of audited contracts)
- Last Update: Version 5.0.1 (2024-02-20)
- Supported Platforms: Ethereum, Polygon, Arbitrum, Optimism, BSC, Avalanche C-Chain
- Integration: Library (Solidity imports)
- Security: Continuous audits by OpenZeppelin, Consensys, Trail of Bits; comprehensive test coverage >95%
- Risks & Mitigations: Version upgrades may introduce breaking changes; proxy patterns add complexity / Pin to stable versions; thoroughly test upgrades [Ref: A18]
```

---

### Authoritative Literature & Reports

**Purpose**: Cite standards, peer-reviewed research, industry reports, audits, and regulatory analyses.

**Required Information**:
- **Type**: Standard (ISO/IEEE/RFC), Academic Paper, White Paper, Industry Report, Audit, Regulatory Report
- **Year**: Publication year (for recency validation)
- **Authors/Organization**: Authorship and institutional affiliation
- **Key Findings**: Summary of main contributions, conclusions, recommendations
- **Credibility**: Peer-reviewed, industry standard, regulatory authority, vetted practitioner
- **Jurisdiction**: Applicable geographic regions, regulatory frameworks, markets

**Recommended Information**:
- **Methodology**: Research design, dataset, experimental setup
- **Limitations**: Sample size, generalizability constraints, assumptions
- **Stakeholder Impact**: Affected parties, practical implications
- **Applicability Boundaries**: Contexts where findings apply vs. do not apply

**Format**:
```text
**[Title]** (ID: L#) (Year) [Language Tag]
- Authors: [Names/Organization]
- Type: [Standard/Academic Paper/White Paper/Industry Report/Audit/Regulatory Report]
- Key Findings: [Summary of main contributions, insights, recommendations]
- Credibility: [Peer-reviewed journal / Industry standard body / Regulatory authority / Vetted audit firm]
- Jurisdiction: [Applicable regions, markets, regulatory frameworks]
- Methodology: [Research design, dataset, experimental approach] (optional)
- Limitations: [Sample constraints, generalizability boundaries, assumptions] (optional)
- Stakeholder Impact: [Affected parties] | Risks/Mitigations: [Summary]
```

**Example**:
```text
**Practical Byzantine Fault Tolerance (PBFT)** (ID: L7) (1999) [EN]
- Authors: Castro, M., & Liskov, B. (MIT)
- Type: Academic Paper (USENIX OSDI)
- Key Findings: First practical BFT algorithm with O(n²) message complexity; achieves consensus in asynchronous networks with ≤3f+1 nodes; demonstrates 3% overhead vs. unreplicated system
- Credibility: Seminal peer-reviewed paper; 15,000+ citations; basis for Tendermint, HotStuff
- Jurisdiction: Global (theoretical foundation applicable across jurisdictions)
- Methodology: Theoretical analysis + prototype implementation on modified NFS
- Limitations: Performance degrades with >10 nodes due to quadratic message complexity; assumes partial synchrony
- Stakeholder Impact: Distributed systems architects, blockchain protocol designers | Risks/Mitigations: Not suitable for large validator sets (>100 nodes) / Use optimized variants (HotStuff, Tendermint) for scalability [Ref: C2]

**区块链技术安全通用规范** (ID: L12) (2023) [ZH]
- Authors: 中国电子技术标准化研究院 (CESI)
- Type: 国家标准 (National Standard GB/T 42570-2023)
- Key Findings: 规定区块链系统安全要求、密码算法选型、智能合约审计流程、隐私保护机制
- Credibility: 国家强制性标准 (Mandatory national standard)
- Jurisdiction: 中国大陆 (Mainland China)
- Stakeholder Impact: 中国区块链项目开发者、安全审计员 | Risks/Mitigations: 不符合标准可能导致合规问题 / 项目初期引入安全架构审查
```

---

### APA Style Source Citations

**Purpose**: Provide complete, standardized bibliographic entries for all referenced sources.

**Format Requirements**:
- **Standard**: APA 7th edition
- **Language Tags**: Mandatory for all citations (append after URL/DOI): [EN], [ZH], [JA], [KO], [DE], [FR], [RU]
- **Persistent Identifiers**: Prefer DOIs over URLs
- **Archived Links**: Provide archive.org snapshots for non-persistent URLs
- **Access Dates**: Include for web resources without DOIs
- **Grouping**: Organize by language (EN, then ZH, then other) for readability

**Language Distribution Target**: ~60% EN, ~30% ZH, ~10% other

**Additional Annotations**:
- **Risk Notes**: Flag methodological limitations, small sample sizes, controversial findings
- **Applicability**: Note jurisdictional or contextual constraints
- **Archive Status**: Indicate if archived version provided
- **Uncertainty**: Flag preprints, pending peer review, contested findings

**Format**:
```text
[APA 7th Citation] [Language Tag]
    [Optional] Risk notes: [Limitations, caveats]
    [Optional] Applicability: [Jurisdictional or contextual boundaries]
    [Optional] Archive: [Archived URL]
    [Optional] Notes: [Additional context, uncertainty flags]
```

**Examples**:

**English Sources [EN]:**
```text
Castro, M., & Liskov, B. (1999). Practical Byzantine fault tolerance. Proceedings of the Third Symposium on Operating Systems Design and Implementation (OSDI), 173-186. https://pmg.csail.mit.edu/papers/osdi99.pdf [EN]
    Notes: Seminal work; 15,000+ citations; theoretical foundation for modern BFT protocols

Wood, G. (2014). Ethereum: A secure decentralised generalised transaction ledger. Ethereum Project Yellow Paper, 151(2014), 1-32. https://ethereum.github.io/yellowpaper/paper.pdf [EN]
    Archive: https://web.archive.org/web/20240115000000*/ethereum.github.io/yellowpaper/paper.pdf
    Notes: Foundational reference; verify contemporary relevance as protocol has evolved significantly

OpenZeppelin. (2024). Smart contract security best practices. Retrieved February 20, 2024, from https://docs.openzeppelin.com/contracts/4.x/ [EN]
    Applicability: Ethereum and EVM-compatible chains; Solidity-specific guidance

Trail of Bits. (2023). Substrate security audit report. https://github.com/trailofbits/publications/blob/master/reviews/Substrate.pdf [EN]
    Risk notes: Audit covers core framework; custom pallets require separate review
```

**Chinese Sources [ZH]:**
```text
中国电子技术标准化研究院. (2023). 区块链技术安全通用规范 (GB/T 42570-2023). 中国国家标准化管理委员会. [ZH]
    Applicability: 中国大陆强制性标准 (Mandatory for Mainland China projects)

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究. 计算机科学, 51(2), 88-95. https://doi.org/10.11896/jsjkx.230400123 [ZH]
    Applicability: 中国供应链金融场景 (China supply chain finance context)
    Risk notes: 样本限于长三角地区；需补充其他区域数据 (Sample limited to Yangtze Delta region)
```

**Other Language Sources:**
```text
Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system. https://bitcoin.org/bitcoin.pdf [EN]
    Archive: https://web.archive.org/web/20240101000000*/bitcoin.org/bitcoin.pdf
    Notes: Foundational reference; historical significance; verify contemporary best practices have evolved

Buterin, V. (2017). О масштабируемости блокчейна [On blockchain scalability]. Ethereum Blog. https://blog.ethereum.org/2017/09/14/scalability [RU]
    Notes: Translated version; refer to EN original for authoritative text
```

---

## Validation Report

**Purpose**: Demonstrate compliance with all 13 validation checks (Part I: Pre-Submission Validation).

**Inclusion**: Attach as appendix OR provide as separate document.

**Format**: Use validation report template from Part I.

**Content**: Show PASS status for all 13 checks with supporting quantitative data.

**Example**:
```markdown
## Validation Report

**Date**: 2024-02-25
**Item Bank**: Blockchain Node Development (30 items)
**Validator**: [Name/Role]

| Check | Result | Status |
|-------|--------|--------|
| 1. Floors | G:12 C:6 L:8 A:15 I:30 (6F/12I/12A) | PASS |
| 2. Citation coverage | 85% ≥1, 40% ≥2 | PASS |
| 3. Language dist | EN:60% ZH:30% Other:10% | PASS |
| 4. Recency | 70% last 3yr | PASS |
| 5. Source diversity | 4 types, max 22% | PASS |
| 6. Links | 42/42 accessible | PASS |
| 7. Cross-refs | 78/78 resolved | PASS |
| 8. Answer lists | 30/30 complete | PASS |
| 9. Blank clarity | 30/30 unambiguous | PASS |
| 10. Normalization | 30/30 specified | PASS |
| 11. Conflict handling | 8/8 compliant (100%) | PASS |
| 12. Fairness & risk | Stakeholders:[dev,ops,audit] Risks:[flagged 5, mitigated 5] | PASS |
| 13. Self-check | Issues resolved: Yes | PASS |

**Overall Status**: ALL CHECKS PASSED — Ready for submission

**Notes**:
- Exceeded minimum floors: Glossary +2, Codebase +1, Literature +2, APA +3
- Difficulty distribution: 20%/40%/40% (exact target)
- Language distribution: Balanced across EN/ZH with Japanese (JA) and Russian (RU) sources for diverse perspectives
- All high-risk items (n=5) include mitigation strategies with cited sources
- Stakeholder perspectives cover developers, operators, auditors across 85% of items
```

---

**End of Template**

