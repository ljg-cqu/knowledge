# QA Prompt Guideline Audit [crit]

Systematic evaluation of [QA.md](./QA.md) against the 20 guidelines defined in
[Guidelines for LLM-Friendly Prompts](../Guidelines_for_LLM-Friendly_Prompts.md).

## Audit Summary

| # | Guideline | Status | Priority |
|---|-----------|--------|----------|
| 1 | Context | Needs improvement | High |
| 2 | Clarity | Needs improvement | High |
| 3 | Precision | Needs improvement | High |
| 4 | Relevance | Compliant | - |
| 5 | MECE | Compliant | - |
| 6 | Sufficiency | Compliant | - |
| 7 | Breadth | Compliant | - |
| 8 | Depth | Compliant | - |
| 9 | Accuracy | Compliant | - |
| 10 | Credibility & Reliability | Compliant | - |
| 11 | Significance | Needs improvement | Medium |
| 12 | Logic | Needs improvement | Medium |
| 13 | Fairness | Needs improvement | High |
| 14 | Concision | Needs improvement | High |
| 15 | Structure | Needs improvement | Critical |
| 16 | Output Format | Needs improvement | Critical |
| 17 | Evidence | Compliant | - |
| 18 | Validation | Needs improvement | High |
| 19 | Practicality | Needs improvement | High |
| 20 | Success Criteria | Needs improvement | Critical |

**Summary**: 9 compliant, 11 need improvement. Priority improvements: Structure (15), Output Format (16),
Success Criteria (20), Context (1), Clarity (2), Precision (3), Fairness (13), Validation (18),
Practicality (19).

---

## Foundation: Define the Task

### Guideline 1: Context

> State scope, constraints, assumptions.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - No clear statement of scope upfront<br>- Assumptions embedded throughout rather than stated clearly<br>- Constraints scattered across multiple sections<br>- User doesn't know immediately what the prompt does vs. what it doesn't do |
| **Proposed improvements** | - Add explicit **Scope** subsection in Part I before Specifications<br>- State: "This framework generates interview Q&As for technical roles. It does NOT: (1) generate role-specific job descriptions, (2) evaluate candidate responses, (3) create recruitment pipelines."<br>- Add **Assumptions** subsection: "Assumes user provides topic/domain; assumes access to citation sources; assumes output language mix acceptable to audience."<br>- Move all constraints to consolidated **Constraints** subsection |
| **Evidence from QA.md** | Line 3: "Generates structured, evidence-based interview question banks..." (describes function but not scope boundaries)<br>Lines 75-169: Constraints scattered across Quality Gates, Validation, Checklist sections |
| **Notes** | Current prompt functional but forces reader to infer scope; explicit boundaries reduce misuse |

### Guideline 2: Clarity

> Request clear, understandable explanations; avoid jargon without definition.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - Jargon used without upfront definition: "MECE," "APA 7th," "DOIs," "archived URLs," "canonicalize"<br>- Instructions assume familiarity with validation terminology (e.g., "Cross-reference binding," "Deduplication")<br>- Section titles inconsistent voice: some imperative ("Execute all steps"), some declarative ("Quality Gates")<br>- Mixed use of symbols (≥, →, ✓, ✗) without legend |
| **Proposed improvements** | - Add **Terminology** section at start defining: MECE, APA, DOI, canonical URL, floor count, difficulty tiers<br>- Define symbols in a legend: "≥ = minimum threshold, → = implies, ✓ = pass, ✗ = fail"<br>- Standardize section voice to imperative for instructions, declarative for reference material<br>- Replace "floor counts" with "minimum required counts" for non-technical clarity |
| **Evidence from QA.md** | Line 14: "MECE Coverage" (no definition until line 20 in different context)<br>Line 48: "APA Style Source Citations ≥12 total" (format not explained until line 308)<br>Line 69: "Canonicalize entries" (no definition) |
| **Notes** | Target audience is LLMs, but clarity benefits model instruction-following |

### Guideline 3: Precision

> Use specific terms; avoid ambiguity; maintain consistent terminology.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - Inconsistent terms: "Q&As" vs "Q&A" vs "questions" vs "answers"<br>- Ambiguous thresholds: "≥70% from last 2yr" for AI/security—unclear if calendar years or rolling 24mo<br>- "Senior/architect/expert level" used interchangeably without defining distinction<br>- "Topic cluster" undefined—is it semantic grouping, category, or theme?<br>- "Contentious topics" (line 131) subjective without criteria |
| **Proposed improvements** | - Use consistent term: "Q&A" (singular), "Q&As" (plural) throughout<br>- Define time windows: "last 3 years = 2022-2025 (from current year); rolling window if year changes mid-generation"<br>- Define roles: "Senior = 5+ yrs; Architect = system design authority; Expert = domain thought leader"<br>- Define "topic cluster" in Terminology: "A semantic grouping of 4-6 related Q&As covering one technical area"<br>- Define "contentious": "Topics with ≥2 peer-reviewed sources presenting conflicting conclusions" |
| **Evidence from QA.md** | Line 13: "25–30 Q&As"<br>Line 56: "~60% EN, ~30% ZH" (tilde indicates approximation but ranges not specified)<br>Line 131: "Identify contentious topics" (no definition)<br>Line 66: "≥70% for AI/security from last 2yr" |
| **Notes** | Precision especially critical for validation thresholds |

### Guideline 4: Relevance

> Stay on topic; exclude tangential information.

| Field | Content |
|-------|---------|
| **Status** | Compliant |
| **Specific issues** | None identified |
| **Proposed improvements** | - Consider adding explicit "Out of Scope" note if users commonly request off-topic features |
| **Evidence from QA.md** | All content directly supports interview Q&A generation; no tangents detected |
| **Notes** | Strong topical coherence maintained throughout |

---

## Scope: What to Cover

### Guideline 5: MECE

> Ensure complete, non-overlapping coverage.

| Field | Content |
|-------|---------|
| **Status** | Compliant |
| **Specific issues** | None identified |
| **Proposed improvements** | None needed |
| **Evidence from QA.md** | Line 20: "MECE Coverage: Technical, theoretical, practical, contextual dimensions"<br>Lines 27-32: Evaluation dimensions table (non-overlapping categories)<br>Lines 41-48: Reference sections mutually exclusive |
| **Notes** | Prompt explicitly enforces MECE and demonstrates it in structure |

### Guideline 6: Sufficiency

> Ensure comprehensive coverage of all necessary aspects.

| Field | Content |
|-------|---------|
| **Status** | Compliant |
| **Specific issues** | None identified |
| **Proposed improvements** | None needed |
| **Evidence from QA.md** | Lines 41-48: Comprehensive reference minimum requirements<br>Lines 63-73: Quality Gates covering recency, diversity, evidence, maturity, validation<br>Lines 77-152: 11-step validation ensuring completeness |
| **Notes** | Exceptionally thorough coverage |

### Guideline 7: Breadth

> Request multiple perspectives where appropriate.

| Field | Content |
|-------|---------|
| **Status** | Compliant |
| **Specific issues** | None identified |
| **Proposed improvements** | None needed |
| **Evidence from QA.md** | Line 22: "Perspectives: Engineering, architecture, QA, product, operations, security, economics, policy"<br>Lines 131-134: Conflict Handling ensures competing viewpoints cited |
| **Notes** | Strong multi-perspective requirement |

### Guideline 8: Depth

> Request thorough treatment with sufficient detail.

| Field | Content |
|-------|---------|
| **Status** | Compliant |
| **Specific issues** | None identified |
| **Proposed improvements** | None needed |
| **Evidence from QA.md** | Line 14: "150–300 words (misconceptions, failure paths, trade-offs, decision criteria)"<br>Line 21: "Analysis Depth: Assumptions, failure paths, comparisons, trade-offs, adoption signals" |
| **Notes** | Depth requirements clearly specified |

---

## Quality: Ensure Excellence

### Guideline 9: Accuracy

> Verify factual correctness; cross-check information.

| Field | Content |
|-------|---------|
| **Status** | Compliant |
| **Specific issues** | None identified |
| **Proposed improvements** | None needed |
| **Evidence from QA.md** | Lines 63-73: Quality Gates include recency, source diversity, codebase maturity checks<br>Lines 105-108: Link validation step<br>Line 37: Citation Standards prioritize authoritative sources |
| **Notes** | Strong accuracy enforcement through multi-layered validation |

### Guideline 10: Credibility & Reliability

> Prioritize authoritative, high-quality, tested sources; avoid low-quality or unproven content.

| Field | Content |
|-------|---------|
| **Status** | Compliant |
| **Specific issues** | None identified |
| **Proposed improvements** | None needed |
| **Evidence from QA.md** | Lines 37-38: "Source Types: (1) Official docs; (2) Standards/peer-reviewed; (3) Audits/reports; (4) Vetted code"<br>Line 67: Source diversity requirement prevents over-reliance on single source<br>Line 69: Codebase maturity criteria (license, recency, stability, audit) |
| **Notes** | Excellent credibility standards |

### Guideline 11: Significance

> Prioritize important information; exclude trivial details.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - No explicit instruction to prioritize significance in Q&A content<br>- Validation focuses on format compliance but not content significance<br>- Risk: LLM could generate formally compliant but trivial Q&As |
| **Proposed improvements** | - Add to Question Design & Critique (line 214): "Significance: Addresses high-impact concepts; avoids edge cases relevant to <5% of practitioners"<br>- Add to Step 3 (line 188): "Prioritize questions that distinguish senior from junior practitioners; omit trivia answerable via simple documentation lookup"<br>- Add validation check: "Significance check: Sample 3 Q&As; verify each addresses concepts with broad applicability or high impact" |
| **Evidence from QA.md** | Line 221: "Signal: Tests reasoning/decision criteria, not trivia" (implicit significance, not explicit)<br>Line 224: "Discriminative power" (related but doesn't define significance threshold) |
| **Notes** | Current prompt mitigates via "not trivia" language but could be more explicit |

### Guideline 12: Logic

> Demand coherent reasoning and sound structure.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - Instructions scattered across three parts without clear logical flow<br>- Part I (Specifications) mixes reference material with constraints<br>- Part II (Instructions) references Part I elements without clear sequencing<br>- Validation section (Part I) separated from execution (Part II Step 6)<br>- Reader must mentally reconstruct workflow from non-linear presentation |
| **Proposed improvements** | - Restructure to: (1) Overview, (2) Input requirements, (3) Output specifications, (4) Execution steps, (5) Validation, (6) Reference formats<br>- Move Reference Section formats (lines 269-323) to appendix<br>- Move Pre-Submission Validation (lines 77-152) immediately after Step 6 instruction (line 205)<br>- Add workflow diagram showing: Planning → Collection → Generation → Artifacts → Compilation → Validation → Review |
| **Evidence from QA.md** | Lines 7-169: Part I mixes specifications, constraints, validation procedures<br>Lines 171-208: Part II jumps between concepts without clear dependency chain<br>Line 205: "Execute all 11 validation steps (Part I)" forces backward reference |
| **Notes** | Content is sound but presentation interrupts logical flow |

### Guideline 13: Fairness

> Request balanced perspectives; acknowledge assumptions, limitations, biases, alternatives, counterarguments, trade-offs, misconceptions.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - Strong trade-off and debate requirements, but no guidance on bias mitigation in Q&A framing<br>- No instruction to avoid loaded language in questions<br>- No guidance on handling culturally-specific assumptions (despite bilingual requirements)<br>- Missing instruction to acknowledge limitations of cited sources<br>- "Debate Handling" addresses competing viewpoints but not inherent biases in source selection |
| **Proposed improvements** | - Add to Content Principles: "Bias Mitigation: Frame questions neutrally; avoid language presupposing 'best' practices; acknowledge when practices are context-dependent (org size, region, budget)"<br>- Add to Citation Standards: "Source Limitations: When citing, note methodological constraints, sample size, or geographic scope if they limit generalizability"<br>- Add to Question Design & Critique: "Neutrality: Question avoids implicit endorsement; presents architectural choices as trade-off decisions rather than correctness judgments"<br>- Add validation check: "Fairness check: Sample 3 Q&As with competing approaches; verify balanced treatment without favoring specific vendors/methodologies" |
| **Evidence from QA.md** | Line 23: "Debate Handling: Present competing viewpoints with counter-evidence" (good but insufficient)<br>Line 131: Conflict handling requires ≥2 perspectives (structural fairness)<br>Missing: Explicit bias mitigation in question framing |
| **Notes** | Structural fairness strong; content-level fairness guidance needed |

---

## Format: How to Present

### Guideline 14: Concision

> Remove redundancy; include only essential information.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - Redundancy across Submission Checklist (lines 154-167) and Quality Gates (lines 63-73)<br>- Validation Report Template (lines 136-150) repeats information from Pre-Submission Validation steps (lines 77-134)<br>- Output Format section (lines 212-324) repeats formatting rules already stated in Citation Standards (lines 34-48)<br>- Three separate mentions of difficulty distribution (lines 15, 54, 82, 157) |
| **Proposed improvements** | - Consolidate Quality Gates and Submission Checklist into single "Requirements Summary" table<br>- Replace Validation Report Template with reference: "Execute Steps 1-11; document pass/fail status"<br>- In Output Format, reference Citation Standards rather than repeating: "See Citation Standards (Part I) for format details"<br>- Establish single source of truth for each requirement; use references elsewhere |
| **Evidence from QA.md** | Lines 154-167 (Checklist) duplicates lines 63-73 (Quality Gates) with 80%+ overlap<br>Lines 136-150 (Template) reformats lines 77-134 (Steps) without new information<br>Lines 276-323 (Format examples) repeat lines 37-48 (Standards) |
| **Notes** | Redundancy likely intended for emphasis but reduces scanability |

### Guideline 15: Structure

> Use lists, tables, diagrams, formulas, code blocks.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - Strong use of tables and code blocks; weak on diagrams<br>- No visual workflow showing Part II step dependencies<br>- Validation steps (lines 77-134) presented as linear text; would benefit from flowchart<br>- Relationship between Reference Sections and inline citations not visualized<br>- Quality Gates table (lines 63-73) mixes metrics without grouping (recency vs. diversity vs. validation) |
| **Proposed improvements** | - Add Mermaid workflow diagram in Part II introduction showing: `Plan → Collect → Generate → Create Artifacts → Compile → Validate → Review`<br>- Add Mermaid diagram showing citation flow: `Inline [Ref: ID] → Reference Section Entry → External Source`<br>- Restructure Quality Gates table with row grouping: "Source Quality (recency, diversity, maturity)" vs. "Structural Quality (evidence coverage, deduplication, cross-refs)"<br>- Convert Validation steps to flowchart with decision diamonds: "Count floors met? → Yes: Proceed → No: Fix & re-validate" |
| **Evidence from QA.md** | Lines 27-32, 43-48, 63-73: Good table usage<br>Lines 237-323: Good code block examples<br>Missing: Workflow diagrams for complex processes |
| **Notes** | Text-heavy sections would benefit from visual structure |

### Guideline 16: Output Format

> Request structured format with TOC linking to sections.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - Output format template provided (lines 237-251) but not required for the prompt itself<br>- Part III (Output Format) is reference material but no meta-instruction requires LLM to produce structured output when USING this prompt<br>- Missing: Explicit instruction for LLM to structure its execution progress when following Part II steps<br>- TOC required in generated Q&As (line 231) but prompt itself lacks TOC for reader navigation |
| **Proposed improvements** | - Add TOC at start of QA.md: "## Contents" linking to Part I, II, III and major subsections<br>- Add to Part II introduction: "When executing these steps, structure your output as: ## Step N: [Title] / ### Checkpoint / ### Next Actions"<br>- Add meta-instruction: "If generating multiple Q&A batches, provide progress report after each cluster: Cluster N/M complete; X Q&As generated; Y citations added; validation status: [pending/passed]"<br>- Add Output Format subsection in Part II (not just Part III): "Structure your workflow outputs using H2 for steps, H3 for checkpoints, code blocks for validation reports" |
| **Evidence from QA.md** | Lines 230-251: Strong output format for final Q&A product<br>Missing: Output format requirements for intermediate workflow steps<br>Missing: TOC for prompt document itself |
| **Notes** | Format requirements for final product clear; intermediate output format undefined |

---

## Validation: Ensure Correctness

### Guideline 17: Evidence

> Cite credible sources; flag uncertainty.

| Field | Content |
|-------|---------|
| **Status** | Compliant |
| **Specific issues** | None identified |
| **Proposed improvements** | - Consider adding: "If source reliability uncertain, note in Reference Section: 'Limited peer review' or 'Single-source claim—cross-check recommended'" (enhancement, not deficiency) |
| **Evidence from QA.md** | Lines 34-48: Comprehensive citation requirements<br>Line 39: "Inline Citation: `[Ref: ID]` after factual claims, metrics, comparisons..."<br>Lines 63-73: Quality Gates ensure source credibility and diversity |
| **Notes** | Exceptionally strong evidence requirements |

### Guideline 18: Validation

> Request reasoning, self-review, error checks.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - Extensive post-generation validation (11 steps, lines 77-134) but no in-process validation<br>- No instruction for LLM to self-review during generation (e.g., after each Q&A, after each cluster)<br>- No instruction to explain reasoning when making trade-off decisions (e.g., if floor counts unmet, why?)<br>- Error checks are mechanical (counts, links) but no semantic checks (e.g., "Does this answer actually address the question?") |
| **Proposed improvements** | - Add to Step 3 (line 188): "After every 5 Q&As: Self-review—verify each question is unambiguous, each answer directly addresses the question, and Key Insight is specific (not generic)"<br>- Add to Step 2 (line 182): "If unable to meet floor counts, document reasoning: insufficient authoritative sources, topic too nascent, or language constraints"<br>- Add validation step: "Semantic coherence check: Sample 3 Q&As; verify answer substance aligns with question ask and stated difficulty level"<br>- Add to Part II introduction: "For each step, state assumptions and constraints encountered; flag uncertainties rather than guessing" |
| **Evidence from QA.md** | Lines 77-134: Strong mechanical validation<br>Line 152: "MANDATORY: If ANY check fails, stop, fix, regenerate" (good enforcement)<br>Missing: In-process self-review, semantic validation, reasoning transparency |
| **Notes** | Validation scope is thorough but timing and type could improve |

### Guideline 19: Practicality

> Ensure actionable, implementable guidance.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - High floor counts (≥10/5/6/12) may be impractical for niche topics with limited literature<br>- Language distribution (~60/30/10 EN/ZH/Other) impractical if topic has monolingual literature<br>- No guidance on what to do when constraints conflict (e.g., recency vs. credibility for stable domains)<br>- Scaling guidance (line 74: "increase floors by 1.5×") may compound impracticality<br>- 11-step validation may be prohibitively time-consuming; no express/standard/thorough tiers |
| **Proposed improvements** | - Add to Specifications: "Practicality Escape Hatches: If topic has <20 total credible sources, reduce floor counts proportionally; document in Exception note (line 50). If monolingual domain (e.g., regional regulation), adjust language distribution; document rationale."<br>- Add to Quality Gates: "Constraint Prioritization: If conflict arises (e.g., only old source available for stable standard), prioritize credibility > recency; flag in Reference Section: '[1998 source; latest available for ISO XYZ]'"<br>- Add to Pre-Submission Validation: "Validation Tiers: Express (Steps 1,2,6,7), Standard (add 3,5,8), Thorough (all 11). Select based on Q&A count and domain maturity."<br>- Add to Step 1 (line 176): "Verify topic has sufficient literature before committing to floor counts; adjust if needed" |
| **Evidence from QA.md** | Line 50: "Exception: If floor counts unmet, document shortfall + rationale" (acknowledges issue but doesn't prevent)<br>Line 74: Scaling guidance may exacerbate impracticality<br>Missing: Proactive feasibility check before generation |
| **Notes** | Requirements rigorous; pragmatic flexibility would improve adoption |

### Guideline 20: Success Criteria

> Define measurable, concrete outcomes.

| Field | Content |
|-------|---------|
| **Status** | Needs improvement |
| **Specific issues** | - Success implicitly defined via validation checklist but never explicitly stated<br>- No upfront statement: "Success = [outcome]"<br>- User doesn't know success until reaching validation (line 77+)<br>- Missing qualitative success criteria (e.g., "Q&As distinguish senior from mid-level candidates")<br>- Submission Checklist (lines 154-167) is compliance checklist, not success criteria |
| **Proposed improvements** | - Add **Success Criteria** section in Part I before Specifications: "This framework succeeds when: (1) Generated Q&As pass all 11 validation steps; (2) Questions discriminate expertise levels per Question Design criteria; (3) Answers provide actionable depth (not just definitions); (4) Citations enable reader to verify claims; (5) Output is ready for interview use without further editing"<br>- Add to Step 7 (line 207): "Success Check: Before submission, verify output meets success criteria (Part I). If qualitative criteria not met, revise even if validation passed."<br>- Add measurable threshold to existing checks: e.g., "Key Insights concrete = ≥90% state specific misconception/failure/trade-off, not generic observation" |
| **Evidence from QA.md** | Lines 154-167: Compliance checklist (necessary but not sufficient for success)<br>Line 208: "Submit only when all checks pass" (defines failure boundary, not success state)<br>Missing: Explicit, upfront success definition |
| **Notes** | Validation is thorough but success criteria should be stated proactively, not discovered through validation |

---

## Summary of Findings

**High-Priority Improvements (Critical/High)**:
1. **Structure (Guideline 15)**: Add workflow diagrams; improve logical flow; consolidate scattered content
2. **Output Format (Guideline 16)**: Add TOC to prompt; define intermediate output format; clarify meta-structure
3. **Success Criteria (Guideline 20)**: Add explicit Success Criteria section upfront with measurable outcomes
4. **Context (Guideline 1)**: Add Scope, Assumptions, Constraints subsections
5. **Clarity (Guideline 2)**: Define jargon upfront; standardize terminology and voice
6. **Precision (Guideline 3)**: Eliminate ambiguity in terms, thresholds, roles
7. **Fairness (Guideline 13)**: Add bias mitigation guidance; require neutral question framing
8. **Validation (Guideline 18)**: Add in-process self-review; include semantic checks
9. **Practicality (Guideline 19)**: Add escape hatches; tiered validation; proactive feasibility checks
10. **Concision (Guideline 14)**: Eliminate redundancy between Checklist/Quality Gates and Template/Steps

**Medium-Priority Improvements**:
11. **Significance (Guideline 11)**: Explicit instruction to prioritize high-impact content
12. **Logic (Guideline 12)**: Restructure for linear flow; move reference material to appendix

**Compliant Areas** (maintain):
- Relevance (4), MECE (5), Sufficiency (6), Breadth (7), Depth (8), Accuracy (9),
  Credibility & Reliability (10), Evidence (17)

**Next Steps**:
1. Proceed to synthesize prioritized change list (TODO #6)
2. Design optimized outline addressing top 10 priority improvements (TODO #7)
3. Implement rewrite with systematic improvements (TODO #8)
