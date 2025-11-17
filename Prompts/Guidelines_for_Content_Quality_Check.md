# Guidelines for Content Quality Check

**Purpose:** Improve content quality so readers (including future you and LLMs) can make reliable decisions with minimal clarification cycles and rework.

**When to apply:** Apply all guidelines for decision-critical content that meets ≥1 of the following:
- Blocks a decision or action
- Risk of significant impact on important outcomes
- Time-sensitive (days to months)
- Multiple stakeholders or readers
- Significant effort required for adoption or implementation

Apply them selectively for other content requiring high quality.

**Expected impact:** ↓30-60% misunderstandings, ↓30-60% avoidable questions, ↑60-80% decision quality.

## Guidelines (21 Total)

### Foundation: Define the Document's Task

**1. Context** [↓30-40% clarification and guessing]: The document explicitly states scope, constraints, assumptions, scale, timeline, domain, stakeholders, resources (where relevant). ❌ Bad: Only title and one line: "Design system". ✅ Good: Introduction states: "This document describes [the solution/approach/analysis] for [specific problem], covering [scope], targeting [scale/audience], to be completed within [timeline], involving [stakeholders], with [key constraints and assumptions]."

**2. Clarity** [↓25-35% ambiguity in meaning]: The document defines key terms and explains important relationships. ❌ Bad: Uses jargon or specialized terms without explanation. ✅ Good: Defines key terms explicitly, explains relationships between concepts, and clarifies any domain-specific terminology.

**3. Precision** [↓40-50% ambiguity in specifications]: The document uses quantified requirements with exact metrics, formulas, and units where relevant. ❌ Bad: Vague qualifiers like "fast", "scalable", "high-quality", "soon". ✅ Good: Specific, measurable criteria with numbers, ranges, thresholds, or explicit definitions of quality levels.

**4. Relevance** [↓30-40% noise]: The document focuses on decision-critical aspects and pushes non-essential detail to appendices or references. ❌ Bad: Includes extensive background or history without clear connection to current decisions. ✅ Good: Focuses on information directly relevant to the decision or task at hand; background context is brief or linked.

### Scope: What the Document Should Cover

**5. MECE** [↑40-50% completeness]: Sections are mutually exclusive and collectively exhaustive for the document's purpose. ❌ Bad: Topic coverage has gaps or overlaps. ✅ Good: Organizes content into distinct, non-overlapping sections that together cover all relevant aspects of the topic.

**6. Sufficiency** [↑35-45% comprehensiveness]: The document covers all necessary aspects for its purpose. ❌ Bad: Addresses only part of what's needed for complete understanding or action. ✅ Good: Covers all dimensions relevant to the topic (what, why, how, when, who, constraints, alternatives, risks, outcomes).

**7. Breadth** [↑30-40% perspective diversity]: The document reflects multiple stakeholder perspectives where appropriate. ❌ Bad: Addresses only one viewpoint or role. ✅ Good: Acknowledges and addresses concerns from all relevant stakeholders or perspectives.

**8. Depth** [↑25-35% thoroughness]: High-impact areas include implementation-level detail, not just high-level principles. ❌ Bad: States principles or recommendations without supporting detail. ✅ Good: Provides actionable specifics including options, trade-offs, parameters, and concrete examples.

### Quality: Ensure Excellence

**9. Significance** [↓40-60% reading time]: The document highlights what really matters and deemphasizes low-impact details. ❌ Bad: Includes exhaustive lists of low-relevance items. ✅ Good: Focuses on critical elements; links to comprehensive references for completeness.

**10. Concision** [↓35-45% word count]: The document avoids redundancy and unnecessary filler. ❌ Bad: Repeats the same concept across multiple sections. ✅ Good: States each principle once, then references it; focuses on concrete details and examples in subsequent sections.

**11. Accuracy** [↓20-30% factual errors]: Factual statements are checked against up-to-date, authoritative sources. ❌ Bad: Makes claims without verification or uses outdated information. ✅ Good: Verifies facts against current, authoritative sources; flags version-specific or time-sensitive information.

**12. Credibility** [↑50-60% trust]: Important claims and recommendations cite primary, authoritative sources, preferably recent. ❌ Bad: "Best practices say..." with no reference. ✅ Good: Cites specific, authoritative sources (official documentation, peer-reviewed research, recognized standards, expert publications).

**13. Logic** [↓30-40% reasoning errors]: Arguments are coherent, consistent, and explicitly present trade-offs. ❌ Bad: Makes one-sided claims without acknowledging context or limitations. ✅ Good: Presents balanced analysis with clear reasoning, acknowledges trade-offs, and specifies conditions where recommendations apply.

**14. Risk/Value** [↑60-80% decision quality]: The document compares ≥2 alternatives with costs, benefits, and risks. ❌ Bad: Proposes single solution with no alternatives. ✅ Good: Compares multiple options with explicit costs, benefits, risks, and conditions for choosing each.

**15. Fairness** [↓40-50% bias]: The document presents balanced views, counterarguments, and limitations. ❌ Bad: Advocates for one approach without addressing downsides. ✅ Good: Presents multiple perspectives, acknowledges limitations, includes counterarguments, and specifies when approach is NOT recommended.

### Format: How to Present Content

**16. Structure** [↑30-40% scannability and actionability]: The document uses clear headings, sections, and lists that make it easy to scan and act. ❌ Bad: Long, unstructured text blocks. ✅ Good: Organized with clear headings, bullet lists, comparison tables, and visual aids; key information is scannable.

**17. Format** [↑35-45% readability]: The document follows a consistent hierarchy and repository conventions (e.g., H1 title, H2 sections, bullets, tables). ❌ Bad: Mixed heading levels and inconsistent formatting. ✅ Good: Uses predictable, consistent structure following repository or organizational conventions.

### Validation: Ensure Correctness and Usefulness

**18. Evidence** [↑40-50% trust]: Citations include source details, recency, and explicit uncertainty flags. ❌ Bad: "Studies show..." with no details. ✅ Good: Specific citations with source, date, and page/section; explicitly flags estimates, assumptions, or areas of uncertainty.

**19. Validation** [↓25-35% errors]: The author or reviewer performs structured self-review. ❌ Bad: Document is published without verification. ✅ Good: Verifies calculations, checks for contradictions and inconsistencies, validates examples, confirms assumptions, and explicitly flags open questions.

**20. Practicality** [↑50-60% implementation speed]: The document includes concrete steps, examples, or guidance where appropriate. ❌ Bad: Generic or abstract recommendations only. ✅ Good: Includes actionable steps, specific examples, commands, formulas, checklists, or decision trees where relevant.

**21. Success Criteria** [↑40-50% measurability]: The document defines measurable outcomes and how to validate them. ❌ Bad: Vague success criteria like "better performance". ✅ Good: Specific, measurable targets with baseline values, target values, measurement methods, and validation approach.

## Quick Check (30s)

**Before publishing or committing your content (mandatory for decision-critical documents, recommended for others):**
- ☐ Self-contained enough (key context is present; references include brief summaries and working links)
- ☐ Context
- ☐ Clarity
- ☐ Precision
- ☐ Relevance
- ☐ MECE
- ☐ Sufficiency
- ☐ Breadth
- ☐ Depth
- ☐ Significance
- ☐ Concision
- ☐ Accuracy
- ☐ Credibility
- ☐ Logic
- ☐ Risk/Value
- ☐ Fairness
- ☐ Structure
- ☐ Format
- ☐ Evidence
- ☐ Validation
- ☐ Practicality
- ☐ Success Criteria

**Quality attributes (10):**
- Accurate
- Precise
- Cited
- Complete
- Actionable
- Consistent
- Relevant
- Balanced
- Appropriately recent (for time-sensitive topics)
- Testable/Verifiable

**Exclude or move to references:**
- Extensive background or history (unless essential for context)
- Pure theory (unless central to the topic)
- Edge cases with minimal impact and low severity
- Formal proofs (unless required)
- Trends without supporting data
- Speculation
- Content that only references other sources without summary or working link

**Always specify:** Key context (scope, constraints, assumptions, scale, timeline, domain, stakeholders, resources) so the document stands alone and can be used reliably.

**Impact metrics:**
- ↓30-60% clarification cycles and misunderstandings (Context + Clarity)
- ↓25-50% ambiguity (Precision)
- ↑60-80% decision quality (Risk/Value)
- ↑35-50% completeness (MECE + Sufficiency)
- ↑30-45% scannability (Structure + Format)
- ↑50-60% implementation speed (Practicality)
