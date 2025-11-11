# Gap Analysis: QA.md vs. Guidelines for LLM-Friendly Prompts

## Summary

This document analyzes `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Market/QA.md` against the 20 guidelines in `../Guidelines_for_LLM-Friendly_Prompts.md`.

---

## Guideline-by-Guideline Assessment

| # | Guideline | Current State | Gap | Proposed Fix | Section to Edit |
|---|-----------|---------------|-----|--------------|-----------------|
| **1** | **Context** (scope, constraints, assumptions) | Partial. Has Context and Constraints subsections but buried in Task Definition. Assumptions exist but not comprehensive. | Missing: LLM role clarification, explicit operational assumptions (e.g., access to tools, ability to verify sources). | Add **Purpose** section stating "This is a reusable prompt template for LLMs." Add **Roles** section distinguishing LLM instructions vs. output requirements. Expand **Assumptions** section. | Top of document, before Task Definition |
| **2** | **Clarity** (clear explanations, avoid undefined jargon) | Good overall. Uses "Floor", "Quality gate", "Difficulty" but defines them in Terminology subsection. Some nested criteria (e.g., "20% F / 40% I / 40% A (±5%)") could be clearer. | Minor. Some compact notation (±5%, ≥, \\|) may confuse. MUST vs. SHOULD not consistently applied. | Replace symbols with plain language ("at least" instead of ≥). Use **must** for hard requirements, **should** for recommendations. Expand Terminology section with more examples. | Throughout; Terminology section |
| **3** | **Precision** (specific terms, avoid ambiguity, consistent terminology) | Mostly good. Uses Q&A, pairs, clusters, MECE, difficulty levels. Some inconsistencies: "Q&A pairs" vs "Q&A" vs "questions". ±5% is ambiguous (absolute vs. relative percentage points). | Moderate. Terminology variations. Range tolerances not explicitly defined as absolute or relative. | Standardize: "Q&A pair" (singular), "Q&A pairs" (plural), "topic cluster", "marketing domain". Define ±5% as "±5 percentage points (absolute)". Create **Terminology Key** section. | Throughout; new Terminology Key section |
| **4** | **Relevance** (stay on topic, exclude tangential info) | Good. Document is focused on interview Q&A generation for marketing roles. Some redundancy across sections (citation rules repeated). | Minor. Redundancy creates noise. | Consolidate repeated content. Remove duplicate citation requirements. Use section cross-references. | Multiple sections (Requirements, Instructions, Reference Sections) |
| **5** | **MECE** (complete, non-overlapping coverage) | Uses MECE explicitly for 6 marketing domains. Does not justify why these 6 are MECE or provide boundary definitions. | Moderate. MECE declared but not validated or explained. | Add **MECE Rationale** subsection explaining how 6 domains cover all senior marketing competencies. Include boundary table with example inclusions/exclusions per domain. | Scope section |
| **6** | **Sufficiency** (comprehensive coverage of necessary aspects) | Good breadth (6 domains, 4 evaluation dimensions, 25-30 Q&A). Does not specify theory-to-practice balance or scenario complexity guidance. | Moderate. Lacks guidance on mixing conceptual and applied content. | Add **Theory-Practice Balance** guidance: for each difficulty level, specify ratio of framework explanation to actionable steps. Add **Scenario Complexity** guidance per seniority level. | Requirements or Instructions section |
| **7** | **Breadth** (multiple perspectives where appropriate) | Mentions cross-functional audience (Product, Sales, Finance). Does not explicitly request multiple marketing schools of thought (brand building vs. performance, B2B vs. B2C, etc.). | Moderate. Single-perspective risk. | Add **Breadth Requirements** subsection requesting coverage of: brand building vs. performance marketing, B2B vs. B2C, DTC vs. marketplace, global vs. local. | Requirements section |
| **8** | **Depth** (thorough treatment with sufficient detail) | Has difficulty levels (F/I/A) and word count (150-300). Does not provide depth expectations per level or examples of insufficient vs. sufficient answers. | Moderate. Insufficient guidance on what depth means per level. | Add **Depth by Difficulty Level** table specifying: knowledge depth, analytical expectations, scenario complexity, data usage, frameworks, minimum elements. Provide worked examples for each level. | Requirements section |
| **9** | **Accuracy** (verify factual correctness, cross-check) | Mentions "Cross-check all claims" in Quality Standards. Not prominently placed. Verification instructions are brief. | Moderate. Accuracy is important but not foregrounded. | Add **Accuracy & Verification** section near top, requiring: verification of statistics, frameworks, definitions, tool specs. Require at least 2 independent sources for critical claims. | After Task Definition, before Scope |
| **10** | **Credibility & Reliability** (authoritative, high-quality sources) | Good. Has source quality expectations: "Peer-reviewed research, established frameworks, proven tools". Does not provide explicit source hierarchy. | Moderate. Source quality mentioned but not structured. | Expand to **Source Quality Hierarchy** in new **Evidence & References** section: (1) Peer-reviewed/standards, (2) Government/official stats, (3) Top-tier industry research, (4) Vendor docs, (5) Trade publications, (6) Blogs/community. Define "authoritative" in marketing context. | New Evidence & References section |
| **11** | **Significance** (prioritize important info, exclude trivial) | Has "Key Insight" field requiring "opportunity/trade-off/conflict/challenge". Does not explicitly prioritize strategic over tactical questions. | Minor. Implicit but not explicit. | Add **Question Prioritization** guidance: prioritize strategic, high-impact questions over purely tactical items. Clarify Key Insight should be "non-obvious, decision-useful, and falsifiable". | Instructions section (Q&A Generation) |
| **12** | **Logic** (coherent reasoning, sound structure) | Good checkpoint structure. Answer structure is implicit ("Analysis", "Reasoning", "Recommendations", "Limitations") but not formalized. | Moderate. Answer flow is demonstrated but not mandated. | Add **Required Answer Structure** section enforcing: (1) Context & problem framing, (2) Analysis & assumptions, (3) Reasoning chain, (4) Recommendations & alternatives, (5) Implementation steps, (6) Metrics & expected impact, (7) Risks & limitations, (8) Evidence & citations, (9) Key insight. Provide filled example. | Instructions section (Q&A Generation) |
| **13** | **Fairness** (balanced perspectives, acknowledge assumptions, limitations, biases, alternatives) | Requires "Limitations" subsection in answers and "≥50% acknowledge limitations/trade-offs". Does not explicitly request alternative frameworks, biases, or counterarguments. | Moderate. Limitations are required but not alternatives or bias acknowledgment. | Add **Fairness Requirements** subsection: (1) Acknowledge alternative frameworks/approaches, (2) State when an approach might not be best and why, (3) Note potential biases from sources or frameworks. Update answer template to include "When NOT to use this approach". | Requirements section; Q&A Generation |
| **14** | **Concision** (remove redundancy, include only essential info) | Some redundancy: citation requirements appear in multiple sections (Requirements, Instructions, Reference Sections). Some verbose sentences. | Moderate. Redundancy across sections. | Consolidate citation requirements into single **Evidence & References** section. Replace repeated content with cross-references. Tighten verbose phrasing while preserving all numeric requirements. | Throughout |
| **15** | **Structure** (use lists, tables, diagrams, formulas, code blocks) | Good use of tables and markdown. No comprehensive TOC with working anchors at top. Some complex criteria could be tabulated. | Moderate. Missing navigable TOC. Some prose could be tables. | Add comprehensive **Table of Contents** near top with anchors to all major sections. Convert nested criteria (e.g., difficulty distribution, reference floors) into clean tables. | Top of document; throughout |
| **16** | **Output Format** (request structured format with TOC linking to sections) | Has detailed Output Format section with structure and example. Could be clearer with a copy-pasteable template block. | Minor. Format is clear but could be more actionable. | Add fenced code block with copy-pasteable template. Ensure TOC pattern is demonstrated in example. Verify all anchors work. | Output Format section |
| **17** | **Evidence** (cite credible sources, flag uncertainty) | Strong citation requirements (≥10 G#, ≥5 T#, ≥6 L#, ≥12 A#). Has language and recency requirements. Does not explicitly require flagging uncertainty or confidence levels. | Minor. Uncertainty flagging not mentioned. | Add requirement to flag uncertain claims with confidence qualifiers (e.g., "likely", "emerging evidence suggests"). Emphasize cross-checking. | Evidence & References section |
| **18** | **Validation** (request reasoning, self-review, error checks) | Excellent 17-step validation checklist with PASS/FAIL. Does not explain WHY each check matters. No per-cluster self-review prompts. | Moderate. Checklist is good but could be more actionable. | For each validation check, add "Why this matters" note. Add **Cluster Self-Review** checklist to run after generating each topic cluster (5-7 Q&A). | Validation section |
| **19** | **Practicality** (ensure actionable, implementable guidance) | Has checkpoints at key steps. Question Design Criteria table shows Good vs. Bad. Could add **Common Pitfalls** with fixes. | Moderate. Good/Bad examples exist but common errors not catalogued. | Add **Common Pitfalls** section showing typical failures for questions (e.g., too broad, recall-based, not scenario-based) and answers (e.g., no citations, vague recommendations, missing limitations) with quick fixes. | After Validation or in Instructions |
| **20** | **Success Criteria** (define measurable, concrete outcomes) | Has Success Criteria subsection in Task Definition with 5 metrics. Scattered additional criteria elsewhere (validation, word count, floors). | Moderate. Success criteria exist but are scattered. | Create single **Success Criteria Summary** near top consolidating all measurable requirements. Use **must** for hard floors, **should** for targets. Ensure no conflicting thresholds elsewhere. | Near top, after Purpose/Context |

---

## Numeric Requirements Inventory (to preserve)

All of these MUST be preserved in optimized version:

### Counts
- **Q&A pairs**: 25–30 total
- **Difficulty distribution**: 20% F / 40% I / 40% A (±5 percentage points)
- **Word count per answer**: 150–300 words

### Reference Floors
- **Glossary (G#)**: ≥10 entries (at least 10)
- **Tools (T#)**: ≥5 entries (at least 5)
- **Literature (L#)**: ≥6 entries (at least 6)
- **APA Citations (A#)**: ≥12 entries (at least 12)
- **Scaling rule**: For >30 Q&A, multiply all floors by 1.5

### Citation Coverage
- **≥70% of answers** include ≥1 citation
- **≥30% of answers** include ≥2 citations
- **≥50% of answers** acknowledge limitations or trade-offs
- **≥60% of answers** include logical explanation
- **≥70% of questions** are scenario-based (test judgment, not recall)
- **≥80% of frameworks** cited correctly with limitations

### Language Distribution
- **English**: 50–70%
- **Chinese (ZH)**: 20–40%
- **Other**: 5–15%

### Recency
- **≥50% of sources** published <3 years ago
- **≥70% of digital/social sources** published <3 years ago

### Diversity
- **≥3 reference types** (Glossary, Tools, Literature, APA)
- **No single source** represents >25% of citations
- **Per topic cluster**: ≥2 authoritative sources + ≥1 tool

### Artifacts
- **Each topic cluster**: ≥1 diagram + ≥1 table

### Validation
- **17 validation checks**: All must PASS before submission
- **FAIL → stop, fix, re-validate**

### Topic Coverage (MECE)
1. Market Research & Analysis
2. Marketing Strategy & Planning
3. Brand Positioning & Messaging
4. Customer Segmentation & Targeting
5. Marketing Channels & Campaign Management
6. Marketing Metrics & Analytics

### Evaluation Dimensions
- Market: Insights, competition, trends, opportunities
- Business: Revenue, CAC, LTV, ROI, market share
- Strategic: Brand equity, positioning, competitive advantage, growth
- Operational: Execution, channels, resources, optimization

---

## Implementation Priority

### High Priority (Foundation + Critical Gaps)
1. ✅ Create backup (DONE)
2. Add Purpose, Roles, Assumptions (Guideline 1)
3. Add Success Criteria Summary (Guideline 20)
4. Add comprehensive TOC (Guideline 15)
5. Standardize terminology (Guideline 3)
6. Add Accuracy & Verification section (Guideline 9)
7. Consolidate Evidence & References (Guidelines 10, 17)

### Medium Priority (Clarity + Structure)
8. Add MECE rationale (Guideline 5)
9. Add Depth by Difficulty Level table (Guideline 8)
10. Add Required Answer Structure (Guideline 12)
11. Add Fairness Requirements (Guideline 13)
12. Add Breadth Requirements (Guideline 7)
13. Add Theory-Practice Balance (Guideline 6)
14. Enhance Validation with rationales (Guideline 18)

### Lower Priority (Polish + Practicality)
15. Add Common Pitfalls (Guideline 19)
16. Add Cluster Self-Review prompts (Guideline 18)
17. Add Question Prioritization (Guideline 11)
18. Remove redundancy (Guideline 14)
19. Clarify numeric specifications (Guideline 2, 3)
20. Improve Output Format (Guideline 16)
21. Polish for repo conventions (line length, links)
22. Test all anchors
23. Optional lint/format

---

## Next Steps

1. ✅ Backup created: `QA.md.bak`
2. Mark todos 1–2 complete
3. Begin High Priority edits (Purpose, Success Criteria, TOC, Terminology)
4. Proceed through Medium and Lower Priority systematically
5. Final validation pass
6. Commit with message: "Optimize Market/QA.md per 20 LLM-friendly prompt guidelines"
