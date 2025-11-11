# Guideline Implementation Mapping: QA.md Optimization

## Summary

This document maps each of the 20 guidelines from `../Guidelines_for_LLM-Friendly_Prompts.md` to specific implementations in the optimized `QA.md`.

**Optimization Date**: 2025-11-11  
**Original File**: `QA.md.bak` (backup preserved)  
**Optimized File**: `QA.md` (812 lines)  
**Gap Analysis**: `QA_optimization_gap_analysis.md`

---

## Guideline-by-Guideline Implementation

### Guideline 1: Context (scope, constraints, assumptions)

**Requirement**: State scope, constraints, assumptions.

**Implementation**:
- ✅ Added **Purpose and Scope** section (lines 40–69)
  - **Document Role** subsection clearly distinguishes LLM instructions vs. output requirements
  - **Target Audience** defines who will use the generated output
  - **Operational Assumptions** lists 4 explicit assumptions for LLM (access to data, verification capability, anonymized scenarios, standard tools)
  - **Constraints** lists word count, language distribution, recency, and MECE coverage

**Evidence**: Lines 40–69

---

### Guideline 2: Clarity (clear explanations, avoid undefined jargon)

**Requirement**: Request clear, understandable explanations; avoid jargon without definition.

**Implementation**:
- ✅ Replaced mathematical symbols (≥, ±, |) with plain language ("at least", "±5 percentage points absolute")
- ✅ Used **must** for hard requirements, **should** for recommendations (line 74)
- ✅ Created **Terminology Key** section (lines 148–178) defining all specialized terms
- ✅ Added **Marketing Terminology** table (lines 164–178) with acronyms, full terms, and usage context

**Evidence**: Lines 74, 148–178; throughout document for "at least" instead of ≥

---

### Guideline 3: Precision (specific terms, avoid ambiguity, consistent terminology)

**Requirement**: Use specific terms; avoid ambiguity; maintain consistent terminology.

**Implementation**:
- ✅ Standardized terminology:
  - "Q&A pair" (singular), "Q&A pairs" (plural)
  - "Topic cluster" for grouped questions
  - "Marketing domain" for the six MECE categories
  - "Difficulty level F/I/A" with full names
- ✅ Defined ±5% as "±5 percentage points absolute" (line 82)
- ✅ Specified scope for all percentages (e.g., "across entire set" line 82, "per topic cluster" line 90)
- ✅ Created **Terminology Key** table (lines 152–178) with precise definitions

**Evidence**: Lines 82, 90, 152–178

---

### Guideline 4: Relevance (stay on topic, exclude tangential info)

**Requirement**: Stay on topic; exclude tangential information.

**Implementation**:
- ✅ Consolidated redundant citation requirements into single **Evidence and References** section (lines 209–273)
- ✅ Removed duplicate mentions of validation commands—now centralized in **Validation Checklist** (lines 548–571)
- ✅ Used cross-references instead of repetition (e.g., "See **Success Criteria** section above" line 251)
- ✅ Eliminated verbose phrasing while preserving all numeric requirements

**Evidence**: Lines 209–273, 548–571; cross-references at lines 144, 251

---

### Guideline 5: MECE (complete, non-overlapping coverage)

**Requirement**: Ensure complete, non-overlapping coverage.

**Implementation**:
- ✅ Added **Marketing Domains (MECE)** section (lines 181–206)
- ✅ **Declaration** explicitly states the six domains are "Mutually Exclusive and Collectively Exhaustive" (line 183)
- ✅ **MECE Rationale** table (lines 187–194) explains how six domains cover all senior marketing competencies
- ✅ **Domain Boundaries** table (lines 198–205) provides:
  - What each domain **includes**
  - What each domain **excludes**
  - Example questions with ✅ markers

**Evidence**: Lines 181–206

---

### Guideline 6: Sufficiency (comprehensive coverage of necessary aspects)

**Requirement**: Ensure comprehensive coverage of all necessary aspects.

**Implementation**:
- ✅ Added **Theory:Practice Ratio** column in **Depth by Difficulty Level** table (line 291)
  - F: 60% theory, 40% practice
  - I: 40% theory, 60% practice
  - A: 20% theory, 80% practice
- ✅ Added **Scenario Complexity** column specifying constraints and stakeholder considerations per level
- ✅ Added **Min Elements** column detailing minimum components per difficulty level

**Evidence**: Lines 289–295

---

### Guideline 7: Breadth (multiple perspectives where appropriate)

**Requirement**: Request multiple perspectives where appropriate.

**Implementation**:
- ✅ Added **Breadth and Fairness** section (lines 354–378)
- ✅ **Breadth Requirements** subsection (lines 358–365) explicitly requests coverage of:
  - Brand building vs. Performance marketing
  - B2B vs. B2C
  - DTC vs. Marketplace
  - Global vs. Local
- ✅ Added to **Cluster Self-Review Checklist** (line 503): "Did I include multiple marketing schools of thought?"

**Evidence**: Lines 354–365, 503

---

### Guideline 8: Depth (thorough treatment with sufficient detail)

**Requirement**: Request thorough treatment with sufficient detail.

**Implementation**:
- ✅ Created comprehensive **Depth by Difficulty Level** table (lines 289–295) with 8 dimensions:
  1. % distribution
  2. Knowledge Depth
  3. Analytical Expectations
  4. Scenario Complexity
  5. Data Usage
  6. Frameworks
  7. Theory:Practice Ratio
  8. Min Elements
- ✅ Added **Examples by Difficulty Level** section (lines 297–352) with:
  - Insufficient answer examples (❌)
  - Sufficient answer examples (✅)
  - Worked examples for F, I, and A levels

**Evidence**: Lines 289–352

---

### Guideline 9: Accuracy (verify factual correctness, cross-check)

**Requirement**: Verify factual correctness; cross-check information.

**Implementation**:
- ✅ Created prominent **Accuracy and Verification** section near top (lines 124–145)
- ✅ **Mandatory Verification** subsection (lines 128–133) requires verification of:
  - Statistics (cross-check with ≥2 sources)
  - Frameworks (verify against original sources)
  - Tool specifications (confirm from vendor docs)
  - Definitions (match industry-standard usage)
- ✅ **Cross-Checking Requirements** subsection (lines 135–140) details flagging uncertain information

**Evidence**: Lines 124–145

---

### Guideline 10: Credibility & Reliability (authoritative, high-quality sources)

**Requirement**: Prioritize authoritative, high-quality, tested sources.

**Implementation**:
- ✅ Created **Source Quality Hierarchy** in **Evidence and References** section (lines 211–237)
- ✅ Six-tier hierarchy from highest to lowest authority:
  1. Peer-reviewed and standards
  2. Government and official statistics
  3. Top-tier industry research
  4. Vendor primary documentation
  5. Reputable trade publications
  6. Blogs and community
- ✅ **Authority Criteria for Marketing** subsection (lines 239–247) defines what makes a source authoritative

**Evidence**: Lines 211–247

---

### Guideline 11: Significance (prioritize important info, exclude trivial)

**Requirement**: Prioritize important information; exclude trivial details.

**Implementation**:
- ✅ Added **Question Prioritization** section (lines 379–397)
- ✅ Three-tier priority system:
  - **High priority**: Judgment, trade-offs, conflicting goals, resource allocation, multi-variate scenarios
  - **Medium priority**: Framework application, diagnosis, comparison
  - **Low priority**: Recall-based, single-step tactics
- ✅ **Key Insight requirements** (lines 387–397) mandate non-obvious, decision-useful, falsifiable, concrete insights
- ✅ Good vs. Bad examples provided

**Evidence**: Lines 379–397

---

### Guideline 12: Logic (coherent reasoning, sound structure)

**Requirement**: Demand coherent reasoning and sound structure.

**Implementation**:
- ✅ Created **Required Answer Structure** section (lines 399–437) enforcing 9-part logical flow:
  1. Context and Problem Framing
  2. Analysis and Assumptions
  3. Reasoning Chain
  4. Recommendations and Alternatives
  5. Implementation Steps and Dependencies
  6. Metrics and Expected Impact
  7. Risks and Limitations
  8. Evidence and Citations
  9. Key Insight
- ✅ Added checkpoints throughout **Instructions** (lines 452, 491, 520, 531)

**Evidence**: Lines 399–437, checkpoints at 452, 491, 520, 531

---

### Guideline 13: Fairness (balanced perspectives, acknowledge assumptions, limitations, biases, alternatives)

**Requirement**: Request balanced perspectives; acknowledge assumptions, limitations, biases, alternatives, counterarguments, trade-offs.

**Implementation**:
- ✅ Added **Fairness Requirements** subsection (lines 367–377) mandating:
  1. Acknowledge alternative frameworks/approaches
  2. State when an approach might NOT be best (included in Required Answer Structure)
  3. Note potential biases (source bias, attribution bias, recency bias) with examples
  4. Cite counterarguments
- ✅ Success Criteria requires ≥50% of answers acknowledge limitations/trade-offs (line 87)
- ✅ Added "When NOT to use this approach" to Required Answer Structure (line 429)

**Evidence**: Lines 87, 367–377, 429

---

### Guideline 14: Concision (remove redundancy, include only essential info)

**Requirement**: Remove redundancy; include only essential information.

**Implementation**:
- ✅ Consolidated citation requirements (previously in 3 sections) into single **Evidence and References** section
- ✅ Replaced repeated validation commands with cross-references
- ✅ Tightened verbose sentences while preserving all numeric requirements
- ✅ Used section pointers: "See **Success Criteria** section above" instead of repeating criteria

**Evidence**: Compare original (300 lines) vs. optimized (812 lines with significantly more content but no redundancy)

---

### Guideline 15: Structure (use lists, tables, diagrams, formulas, code blocks)

**Requirement**: Use lists, tables, diagrams, formulas, code blocks.

**Implementation**:
- ✅ Added comprehensive **Table of Contents** with 26 anchor links (lines 11–36)
- ✅ Converted nested criteria into clean tables:
  - **Quantitative Floors** (lines 79–90)
  - **Reference Floors** (lines 94–99)
  - **Quality Gates** (lines 105–113)
  - **Terminology Key** (lines 152–162)
  - **Marketing Terminology** (lines 166–177)
  - **MECE Rationale** (lines 187–194)
  - **Domain Boundaries** (lines 198–205)
  - **Deliverable Specifications** (lines 280–287)
  - **Depth by Difficulty Level** (lines 291–295)
  - **Validation Checklist** (lines 553–570)
  - **Question Pitfalls** (lines 578–584)
  - **Answer Pitfalls** (lines 588–595)

**Evidence**: Lines 11–36 (TOC); 12 comprehensive tables throughout

---

### Guideline 16: Output Format (request structured format with TOC linking to sections)

**Requirement**: Request structured format with TOC linking to sections.

**Implementation**:
- ✅ Comprehensive **Output Format** section (lines 599–738)
- ✅ Includes copy-pasteable markdown template in fenced code block
- ✅ Shows complete structure with TOC, Topic Overview table, Q&A format, Reference Sections, Validation Report
- ✅ Template demonstrates proper anchor linking
- ✅ **Example Q&A Pair** (lines 742–797) shows fully worked example following all requirements

**Evidence**: Lines 599–797

---

### Guideline 17: Evidence (cite credible sources, flag uncertainty)

**Requirement**: Cite credible sources; flag uncertainty.

**Implementation**:
- ✅ Comprehensive **Evidence and References** section (lines 209–273)
- ✅ **Source Quality Hierarchy** (lines 211–237) with 6 tiers
- ✅ **Authority Criteria** (lines 239–247) defining authoritative sources
- ✅ **Reference Floors and Distribution** (lines 249–256) consolidating all citation requirements
- ✅ **Flagging Uncertainty** subsection (lines 258–264) with specific language for uncertain claims:
  - "Preliminary evidence suggests..."
  - "Emerging research indicates..."
  - "This is contested; Source A argues X while Source B argues Y"

**Evidence**: Lines 209–273

---

### Guideline 18: Validation (request reasoning, self-review, error checks)

**Requirement**: Request reasoning, self-review, error checks.

**Implementation**:
- ✅ Preserved and enhanced **Validation Checklist** (lines 548–571) with 17 checks
- ✅ Added "Why This Matters" column explaining rationale for each check
- ✅ Added **Cluster Self-Review Checklist** (lines 499–509) with 7 prompts to run after each topic cluster:
  1. Diverse perspectives
  2. Evidence floors
  3. Source quality
  4. Key Insights quality
  5. Limitations stated
  6. Alternatives acknowledged
  7. Bias acknowledgment

**Evidence**: Lines 499–509 (cluster self-review), 548–571 (17-step validation with rationales)

---

### Guideline 19: Practicality (ensure actionable, implementable guidance)

**Requirement**: Ensure actionable, implementable guidance.

**Implementation**:
- ✅ Created **Common Pitfalls** section (lines 574–596) with two tables:
  - **Question Pitfalls** (lines 578–584): 5 pitfalls with ❌ Bad examples, ✅ Good fixes, and "Why It Matters"
  - **Answer Pitfalls** (lines 588–595): 6 pitfalls with ❌ Bad examples, ✅ Good fixes, and "Why It Matters"
- ✅ Added concrete, worked examples for each difficulty level (lines 297–352)
- ✅ Added "Why This Matters" column to Validation Checklist

**Evidence**: Lines 574–596, 297–352

---

### Guideline 20: Success Criteria (define measurable, concrete outcomes)

**Requirement**: Define measurable, concrete outcomes.

**Implementation**:
- ✅ Created comprehensive **Success Criteria** section near top (lines 72–121)
- ✅ Three subsections with all measurable requirements:
  - **Quantitative Floors** table (lines 79–90): 10 measurable criteria with exact thresholds
  - **Reference Floors** table (lines 94–99): 4 reference types with minimum counts
  - **Quality Gates** table (lines 105–113): 7 gates with clear pass/fail criteria
  - **Strategic Quality** (lines 115–120): 4 qualitative requirements
- ✅ Used **must** for hard requirements (line 74)
- ✅ No conflicting thresholds elsewhere (consolidated from scattered mentions in original)

**Evidence**: Lines 72–121

---

## Summary of Major Additions

### New Sections (not in original)
1. **Purpose and Scope** (lines 40–69) — Guidelines 1, 2
2. **Accuracy and Verification** (lines 124–145) — Guideline 9
3. **Terminology Key** (lines 148–178) — Guidelines 2, 3
4. **Marketing Domains (MECE)** (lines 181–206) — Guideline 5
5. **Evidence and References** (lines 209–273) — Guidelines 10, 17
6. **Depth by Difficulty Level** (lines 289–295) — Guideline 8
7. **Examples by Difficulty Level** (lines 297–352) — Guideline 8
8. **Breadth and Fairness** (lines 354–378) — Guidelines 7, 13
9. **Question Prioritization** (lines 379–397) — Guideline 11
10. **Required Answer Structure** (lines 399–437) — Guideline 12
11. **Cluster Self-Review Checklist** (lines 499–509) — Guideline 18
12. **Common Pitfalls** (lines 574–596) — Guideline 19

### Enhanced Sections (from original)
1. **Table of Contents** (lines 11–36) — Guideline 15 (was absent in original)
2. **Success Criteria** (lines 72–121) — Guideline 20 (consolidated from scattered mentions)
3. **Validation Checklist** (lines 548–571) — Guideline 18 (added "Why This Matters" column)
4. **Output Format** (lines 599–738) — Guideline 16 (added copy-pasteable template)
5. **Example Q&A Pair** (lines 742–797) — Guidelines 16, 19 (preserved from original)

---

## Preserved Requirements (from original)

All numeric requirements from the original document were preserved:

✅ **Q&A pairs**: 25–30 total  
✅ **Difficulty distribution**: 20% F / 40% I / 40% A (±5 percentage points)  
✅ **Word count per answer**: 150–300 words  
✅ **Glossary (G#)**: ≥10 entries  
✅ **Tools (T#)**: ≥5 entries  
✅ **Literature (L#)**: ≥6 entries  
✅ **APA Citations (A#)**: ≥12 entries  
✅ **Citation coverage**: ≥70% answers ≥1, ≥30% answers ≥2  
✅ **Language distribution**: EN 50–70%, ZH 20–40%, Other 5–15%  
✅ **Recency**: ≥50% <3 years (≥70% digital/social)  
✅ **Diversity**: ≥3 types, no source >25%  
✅ **Artifacts per cluster**: ≥1 diagram + ≥1 table  
✅ **17-step validation**: All checks must PASS  
✅ **6 marketing domains** (MECE): Market Research, Strategy, Brand, Segmentation, Channels, Metrics  

---

## File Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| **Total lines** | 812 | Well under 5000-line limit |
| **Original lines** | 301 | 2.7× expansion with significantly more guidance |
| **Sections** | 17 major | Improved from 9 in original |
| **Tables** | 12 | Improved from 4 in original |
| **TOC entries** | 26 | New addition (0 in original) |
| **New sections** | 12 | All map to specific guidelines |
| **Guidelines addressed** | 20/20 | 100% coverage |

---

## Verification Checklist

| Guideline | Evidence | Status |
|-----------|----------|--------|
| 1. Context | Lines 40–69: Purpose, Roles, Assumptions | ✅ |
| 2. Clarity | Lines 74, 148–178: must/should, Terminology Key | ✅ |
| 3. Precision | Lines 82, 90, 152–178: standardized terms, absolute tolerances | ✅ |
| 4. Relevance | Lines 209–273, consolidated sections, cross-references | ✅ |
| 5. MECE | Lines 181–206: MECE declaration, rationale, boundaries | ✅ |
| 6. Sufficiency | Lines 289–295: Theory:Practice ratio, scenario complexity | ✅ |
| 7. Breadth | Lines 354–365, 503: multiple schools of thought | ✅ |
| 8. Depth | Lines 289–352: depth table + worked examples | ✅ |
| 9. Accuracy | Lines 124–145: verification section near top | ✅ |
| 10. Credibility | Lines 211–247: source hierarchy, authority criteria | ✅ |
| 11. Significance | Lines 379–397: question prioritization, Key Insight requirements | ✅ |
| 12. Logic | Lines 399–437, checkpoints: required answer structure | ✅ |
| 13. Fairness | Lines 87, 367–377, 429: alternatives, bias, limitations | ✅ |
| 14. Concision | Consolidated sections, removed redundancy | ✅ |
| 15. Structure | Lines 11–36 (TOC), 12 tables throughout | ✅ |
| 16. Output | Lines 599–738: template + example | ✅ |
| 17. Evidence | Lines 209–273: source hierarchy, flagging uncertainty | ✅ |
| 18. Validation | Lines 499–509 (cluster), 548–571 (17-step with rationales) | ✅ |
| 19. Practicality | Lines 574–596, 297–352: pitfalls + examples | ✅ |
| 20. Success | Lines 72–121: consolidated measurable criteria | ✅ |

**Status**: ✅ All 20 guidelines successfully implemented

---

## Files Created

1. ✅ `QA.md.bak` — Backup of original (301 lines)
2. ✅ `QA.md` — Optimized version (812 lines)
3. ✅ `QA_optimization_gap_analysis.md` — Gap analysis with guideline-by-guideline assessment
4. ✅ `QA_guideline_mapping.md` — This document

---

## Recommended Next Steps

1. **Review** the optimized `QA.md` to confirm all requirements meet your needs
2. **Test** the prompt with an LLM to generate a sample Q&A set
3. **Validate** that generated output follows all 17 validation checks
4. **Commit** with message: `"Optimize Market/QA.md per 20 LLM-friendly prompt guidelines (1-20)"`
5. **Archive** gap analysis and mapping documents for reference

---

**Optimization Completed**: 2025-11-11  
**Guideline Coverage**: 20/20 (100%)  
**All Numeric Requirements**: Preserved  
**File Length**: 812 lines (within limits)  
**Ready for Use**: ✅ Yes
