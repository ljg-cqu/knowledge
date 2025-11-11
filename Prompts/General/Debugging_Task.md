# Debugging Task Assessment Generator

Generate comprehensive debugging task assessments for senior/architect/expert-level positions with structured citations, multi-dimensional evaluation, and validation protocols.

## Contents

- [Part I: Specifications](#part-i-specifications)
  - [Scope and Structure](#scope-and-structure)
  - [Citation Standards](#citation-standards)
  - [Reference Minimum Requirements](#reference-minimum-requirements)
  - [Quality Gates](#quality-gates)
  - [Pre-Submission Validation](#pre-submission-validation)
  - [Submission Checklist](#submission-checklist)
- [Part II: Instructions](#part-ii-instructions)
  - [Step 1: Planning](#step-1-planning)
  - [Step 2: References](#step-2-references)
  - [Step 3: Tasks](#step-3-tasks)
  - [Step 4: Alternatives](#step-4-alternatives)
  - [Step 5: Compile References](#step-5-compile-references)
  - [Step 6: Validate](#step-6-validate)
  - [Step 7: Submit](#step-7-submit)
- [Part III: Output Format](#part-iii-output-format)
  - [Task Bank Structure](#task-bank-structure)
  - [Reference Sections Structure](#reference-sections-structure)

---

# Part I: Specifications

### Scope and Structure

**Context**: This prompt generates debugging assessments for senior/architect/expert-level technical positions requiring deep understanding of bug patterns, root-cause analysis, and systematic problem-solving.

**Task Scope**:
- **Quantity**: 15–22 tasks per assessment
- **Target Level**: Senior, Architect, Expert roles
- **Code Length**: 10–50 lines per task (focused, single-bug scenarios)

**Difficulty Distribution** (MECE principle):
- **Foundational**: 20% (3–4 tasks) - Basic syntax, type errors, simple logic
- **Intermediate**: 40% (6–9 tasks) - API misuse, edge cases, moderate complexity
- **Advanced**: 40% (6–9 tasks) - Concurrency, security, performance, architectural issues

**Bug Type Categories** (single focused bug per task):
1. Off-by-one errors
2. Type mismatches and coercion
3. API contract violations
4. Concurrency and race conditions
5. Edge case handling failures
6. Logic flow errors
7. Security vulnerabilities
8. Performance bottlenecks

**Required Deliverables** (all must be present):
- Buggy code with inline comments
- Failing test cases demonstrating the bug
- Corrected code with minimal, surgical fixes
- Root-cause explanation (2–4 sentences with citations)
- Passing test cases validating the fix

**Grading Rubric**:
- Code Fix: 0–6 points (correctness, minimalism, best practices)
- Explanation: 0–3 points (accuracy, clarity, citation quality)
- Tests: 0–1 point (comprehensiveness)
- **Partial Credit**: Award points for correct diagnosis even if implementation incomplete

**Alternative Solutions**:
- Document multiple valid approaches with explicit trade-offs
- Compare minimal fixes vs. comprehensive refactoring
- Include common mistake patterns for instructional value

### Citation Standards

**Purpose**: Ensure credibility, reliability, and verifiability of all technical claims through authoritative sources.

**Language Distribution** (diversity requirement):
- **English**: ~60% (50-70% acceptable range) - Tag: [EN]
- **Chinese**: ~30% (20-40% acceptable range) - Tag: [ZH]
- **Other**: ~10% (5-15% acceptable range) - Tag language code

**Source Type Hierarchy** (prioritized by reliability):
1. **Official Documentation**: Language specs, framework docs, API references
2. **Standards & Peer-Reviewed**: IEEE, ACM, RFC, academic journals
3. **Security Audits & Reports**: CVE, OWASP, professional security assessments
4. **Vetted Codebases**: Open-source projects with active maintenance, audit history

**Citation Format**:
- **Style**: APA 7th edition with language tags
- **Inline References**: Use `[Ref: ID]` in root-cause explanations and code comments
- **Reference IDs**: G# (Glossary), C# (Codebase), L# (Literature), A# (APA)

**Inline Citation Requirements**:
- Minimum 1 citation per root-cause explanation
- Recommended 2+ citations for complex or contentious issues
- Place citations immediately after claims requiring evidence

### Reference Minimum Requirements

**Sufficiency Thresholds** (ensure comprehensive coverage):

| Reference Section | Minimum Count | Content Type | Purpose |
| --- | --- | --- | --- |
| Glossary | ≥10 | Core concepts, jargon, acronyms | Terminology clarity |
| Codebase & Libraries | ≥5 | Stack components, SDKs, tools | Technical context |
| Literature & Reports | ≥6 | Standards, peer-reviewed, audits | Authoritative evidence |
| APA Citations | ≥12 | Language mix (60% EN / 30% ZH / 10% other) | Source diversity |

**Scaling Rule**: For assessments >30 tasks, multiply minimums by 1.5× (round up).

**Exception Handling**:
- If minimums cannot be met, explicitly document:
  - Shortfall quantity and section
  - Root cause (domain scarcity, language constraints)
  - Sourcing plan with timeline
  - Alternative validation approach
- Submit only when plan is approved or minimums are met

### Quality Gates

**Accuracy & Credibility Standards**:

**1. Recency Requirements** (prevent outdated information):
- **General Topics**: ≥50% sources from last 3 years
- **AI/Security Topics**: ≥70% sources from last 3 years (rapid evolution domains)
- **Rationale**: Ensure current best practices, avoid deprecated patterns

**2. Source Diversity** (avoid bias, ensure balanced perspective):
- **Minimum Types**: ≥3 distinct source categories (official docs, academic, industry, code)
- **Maximum Concentration**: No single source type >25% of total citations
- **Rationale**: Prevent vendor lock-in, echo chambers, single-point-of-failure

**3. Evidence Coverage** (ensure substantiated claims):
- **Minimum Coverage**: ≥70% tasks include ≥1 citation in root-cause explanation
- **Deep Analysis**: ≥30% tasks include ≥2 distinct citations (multiple perspectives)
- **Rationale**: Balance thoroughness with efficiency

**4. Codebase Maturity Indicators** (reliability assessment):
- **License**: Open-source with permissive or copyleft license
- **Activity**: Last commit ≤12 months (active maintenance)
- **Stability**: Stable release version (not alpha/beta)
- **Security**: Audit status, vulnerability history (if available)
- **Rationale**: Avoid abandoned, untested, or vulnerable dependencies

**5. Link Validation** (ensure accessibility):
- **Primary**: All URLs must resolve (HTTP 200)
- **Fallback**: Provide archived alternatives (Wayback Machine, archive.is)
- **Persistent IDs**: Use DOIs for academic sources when available
- **Rationale**: Prevent broken references, ensure long-term accessibility

**6. Cross-Reference Integrity** (validation requirement):
- **Binding**: Every `[Ref: ID]` must map to exactly one Reference Section entry
- **Uniqueness**: No duplicate IDs across sections
- **Completeness**: All cited IDs must be defined; no orphaned definitions
- **Rationale**: Enable verification, prevent confusion

**7. Deduplication** (canonicalization requirement):
- Merge duplicate entries with different URLs/versions
- Use canonical URLs (redirect to final destination)
- Standardize author names, publication titles
- **Rationale**: Maintain clean, navigable reference list

### Pre-Submission Validation

**Validation Protocol** (mandatory execution before submission):

**Process**:
1. Execute all 11 validation steps in sequence
2. Generate validation report using standard format
3. Fix all failures (no partial passes allowed)
4. Re-validate until ALL checks PASS
5. Attach final validation report to submission

**Validation Steps** (success criteria):

| Step | Verification Target | Pass Criteria | Rationale |
| --- | --- | --- | --- |
| 1. Count Audit | Reference minimums + task count | G≥10, C≥5, L≥6, A≥12; Tasks 15-22; Ratio 20/40/40 (±5%) | Sufficiency |
| 2. Citation Coverage | Inline `[Ref: ID]` presence | ≥70% tasks ≥1 citation; ≥30% tasks ≥2 citations | Evidence |
| 3. Language Distribution | Language tag counts | EN 50-70%, ZH 20-40%, Other 5-15% | Diversity |
| 4. Recency | Publication years | ≥50% last 3yr (general); ≥70% last 3yr (AI/security) | Currency |
| 5. Source Diversity | Citation type distribution | ≥3 types; max single type ≤25% | Bias prevention |
| 6. Link Validation | URL resolution | 100% accessible or archived | Accessibility |
| 7. Cross-Reference Integrity | `[Ref: ID]` → definitions | 100% resolve; no orphans | Completeness |
| 8. Bug Focus | Single bug per task | 100% tasks = 1 bug only | Clarity |
| 9. Fix Completeness | Code + explanation presence | 100% have fix + 2-4 sentence explanation | Deliverables |
| 10. Test Coverage | Failing + passing tests | 100% have both test types | Validation |
| 11. Alternative Documentation | Multiple approaches | ≥80% tasks document alternatives + trade-offs | Fairness |

**Validation Report Format** (structured output):

```markdown
## Validation Report

| Check | Result | Status |
|-------|--------|--------|
| Count Audit | G:X C:Y L:Z A:W T:N (F/I/A: P%/Q%/R%) | PASS/FAIL |
| Citation Coverage | X% ≥1, Y% ≥2 citations | PASS/FAIL |
| Language Distribution | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr (Topic: general/AI/security) | PASS/FAIL |
| Source Diversity | N types, max P% single type | PASS/FAIL |
| Link Validation | Y/X accessible (Z archived) | PASS/FAIL |
| Cross-Reference Integrity | Y/X resolved, Z orphans | PASS/FAIL |
| Bug Focus | Y/X single-bug tasks | PASS/FAIL |
| Fix Completeness | Y/X complete (fix + explanation) | PASS/FAIL |
| Test Coverage | Y/X have both test types | PASS/FAIL |
| Alternative Documentation | Y/X documented (Z%) | PASS/FAIL |

**Overall Status**: PASS/FAIL  
**Failed Checks**: [List or "None"]  
**Action Required**: [Fix plan or "Ready for submission"]
```

**MANDATORY REQUIREMENT**:
- **Zero Tolerance**: ALL 11 checks must show PASS status
- **No Submission**: Do not submit until validation report shows 100% PASS
- **Iteration**: Re-validate after each fix cycle until clean pass achieved

### Submission Checklist

**Pre-Flight Verification** (tick all boxes before submission):

**Reference Quantity** (sufficiency):
- [ ] Glossary: ≥10 entries with clear definitions
- [ ] Codebase & Libraries: ≥5 entries with maturity indicators
- [ ] Literature & Reports: ≥6 entries with persistent links
- [ ] APA Citations: ≥12 entries with language tags

**Task Structure** (scope + quality):
- [ ] Total tasks: 15-22 count
- [ ] Difficulty distribution: 20/40/40 (Foundational/Intermediate/Advanced, ±5%)
- [ ] Bug focus: Every task = single, well-defined bug
- [ ] Code length: All tasks 10-50 lines
- [ ] Deliverables: All tasks have buggy code + failing test + fix + explanation + passing test

**Citation Quality** (credibility + diversity):
- [ ] Language mix: EN 50-70%, ZH 20-40%, Other 5-15%
- [ ] Recency: ≥50% last 3yr (or ≥70% for AI/security)
- [ ] Source diversity: ≥3 types, no single type >25%
- [ ] Coverage: ≥70% tasks ≥1 citation, ≥30% tasks ≥2 citations
- [ ] Root-cause explanations: All 2-4 sentences with inline `[Ref: ID]`

**Technical Rigor** (maturity + validation):
- [ ] Codebase maturity: License + last update ≤12mo + stable release + audit status
- [ ] Link validation: 100% URLs resolve or have archived alternatives
- [ ] Cross-reference integrity: All `[Ref: ID]` map to Reference Section entries
- [ ] Test coverage: All tasks include failing tests + passing tests
- [ ] Alternative solutions: ≥80% tasks document multiple approaches with trade-offs

**Validation Compliance** (mandatory gate):
- [ ] Validation report: Generated and attached
- [ ] Validation status: ALL 11 checks show PASS
- [ ] Failed checks: Zero (no failures allowed)

**Success Criteria** (measurable outcomes):
- [ ] Assessment is immediately usable for technical interviews
- [ ] All citations are verifiable and accessible
- [ ] Grading rubrics enable consistent, fair evaluation
- [ ] Alternative solutions demonstrate deep technical understanding

**Final Confirmation**:
- [ ] I have reviewed all sections for accuracy, clarity, and completeness
- [ ] I confirm all checklist items are verified as complete
- [ ] I am ready to submit for review

---

# Part II: Instructions

**Execution Protocol**: Follow all steps sequentially. Complete inline validation checks before proceeding to next step. Do not skip or reorder steps.

### Step 1: Planning

**Objective**: Design task distribution ensuring MECE coverage, balanced difficulty, and alignment with target role requirements.

**Actions**:

1. **Identify Bug Clusters** (4-6 categories):
   - Select from: Off-by-one errors, Type mismatches, API misuse, Concurrency issues, Edge cases, Logic errors, Security vulnerabilities, Performance bottlenecks
   - Ensure clusters align with target role's domain (e.g., security for security engineer, concurrency for backend architect)
   - Document rationale for cluster selection

2. **Allocate Tasks** (2-4 per cluster):
   - Total: 15-22 tasks
   - Distribution: Spread evenly across clusters
   - Avoid concentration: No cluster >30% of total tasks

3. **Assign Difficulty Levels**:
   - **Foundational** (20%): 3-4 tasks - Basic syntax, simple type errors, straightforward logic
   - **Intermediate** (40%): 6-9 tasks - API contract violations, edge cases, moderate complexity
   - **Advanced** (40%): 6-9 tasks - Race conditions, security flaws, performance optimization, architectural issues
   - Balance difficulty within each cluster

4. **Select Languages/Frameworks**:
   - Match target role requirements (e.g., Python/Django for web backend, Solidity for blockchain)
   - Use realistic, production-quality code patterns
   - Avoid toy examples; simulate real-world scenarios

**Validation Check** (before proceeding):
- [ ] Total tasks = 15-22
- [ ] Difficulty ratio ≈ 20/40/40 (±5% tolerance)
- [ ] 4-6 distinct bug clusters identified
- [ ] 2-4 tasks per cluster
- [ ] Languages match target role
- [ ] Clusters cover diverse bug types (no redundancy)

**Output**: Task allocation matrix

```markdown
| Cluster | Bug Type | Task Count | Difficulty (F/I/A) | Language |
|---------|----------|------------|-------------------|----------|
| 1 | Off-by-one | 3 | 1/1/1 | Python |
| 2 | Concurrency | 4 | 0/2/2 | Go |
| ... | ... | ... | ... | ... |
| **Total** | - | **18** | **3/7/8** | - |
```

### Step 2: References

**Objective**: Build authoritative, diverse, accessible reference foundation meeting all quality gates.

**Actions**:

1. **Gather References** (meet minimums + quality gates):
   
   **Glossary (≥10)**:
   - Define core concepts, technical jargon, acronyms used in tasks
   - Prioritize terms candidates might misunderstand
   - Include language tag for each definition source
   
   **Codebase & Libraries (≥5)**:
   - Select stack components, SDKs, tools relevant to bug clusters
   - Verify maturity: license, last commit ≤12mo, stable release, audit status
   - Include official documentation links
   
   **Literature & Reports (≥6)**:
   - Gather standards (IEEE, RFC), peer-reviewed papers, security audits
   - Prioritize sources discussing bug patterns in your clusters
   - Use persistent links (DOIs, archived URLs)
   
   **APA Citations (≥12)**:
   - Compile all authoritative sources in APA 7th format
   - Ensure language diversity: ~60% EN, ~30% ZH, ~10% other
   - Include publication year for recency tracking

2. **Tag and Classify**:
   - **Language Tags**: Add [EN], [ZH], or other language codes to every reference
   - **Publication Year**: Extract or note year for recency validation
   - **Source Type**: Classify as (1) Official docs, (2) Standards/peer-reviewed, (3) Audits/reports, (4) Vetted code

3. **Assign Reference IDs**:
   - **G1-Gn**: Glossary entries (sequential numbering)
   - **C1-Cn**: Codebase & library entries
   - **L1-Ln**: Literature & report entries
   - **A1-An**: APA citation entries
   - Ensure IDs are unique across all sections

4. **Validate Links**:
   - Test all URLs (HTTP 200 response)
   - Create archived versions for non-persistent URLs
   - Add DOIs for academic sources when available

**Validation Check** (before proceeding):
- [ ] Minimums met: G≥10, C≥5, L≥6, A≥12
- [ ] Language distribution: EN 50-70%, ZH 20-40%, Other 5-15%
- [ ] Recency: ≥50% from last 3yr (or ≥70% for AI/security topics)
- [ ] Source diversity: ≥3 types represented, no type >25%
- [ ] All URLs validated or archived
- [ ] All codebase entries include maturity indicators
- [ ] All reference IDs are unique

**Output**: Reference inventory table

```markdown
| ID | Title/Term | Year | Lang | Type | Status |
|----|------------|------|------|------|--------|
| G1 | Race condition | N/A | [EN] | Glossary | ✓ |
| C1 | golang.org/sync | 2024 | [EN] | Official | ✓ |
| L1 | IEEE Std 1012-2016 | 2016 | [EN] | Standard | ✓ |
| A1 | Smith et al. (2024) | 2024 | [EN] | Academic | ✓ |
| ... | ... | ... | ... | ... | ... |
```

### Step 3: Tasks

**Objective**: Generate realistic, well-documented debugging tasks with complete deliverables and authoritative citations.

**Actions** (for each task):

1. **Create Buggy Code**:
   - **Length**: 10-50 lines (focused, single-bug scenario)
   - **Realism**: Use production-quality patterns, realistic variable names, authentic context
   - **Bug Type**: Single, well-defined bug from planned clusters
   - **Clarity**: Bug should be non-obvious but discoverable through systematic analysis
   - **Comments**: Add inline comments to provide context (may include `[Ref: ID]` for API patterns)
   - **Language**: Match assigned language/framework from Step 1 plan

2. **Assign Metadata**:
   - **Task ID**: Sequential numbering (Task 1, Task 2, ...)
   - **Difficulty**: Foundational, Intermediate, or Advanced (per Step 1 allocation)
   - **Language/Framework**: Tag clearly (e.g., "Python 3.11" or "Solidity 0.8.x")
   - **Bug Category**: Link to cluster from Step 1

3. **Write Root-Cause Explanation** (2-4 sentences):
   - **Sentence 1**: Describe what the bug is (symptom)
   - **Sentence 2**: Explain why it occurs (mechanism)
   - **Sentence 3**: Reference authoritative source with `[Ref: ID]` (specification, known pattern, best practice)
   - **Sentence 4** (optional): Note impact or common misconception
   - **Citation Requirement**: Include ≥1 `[Ref: ID]` (preferably 2+ for complex bugs)
   - **Clarity**: Use precise terminology from Glossary; avoid jargon without definition

4. **Provide Failing Test**:
   - **Framework**: Use standard testing framework for the language (pytest, Jest, go test, etc.)
   - **Demonstration**: Test must fail with buggy code, demonstrating the issue
   - **Coverage**: Test the specific bug scenario, not peripheral functionality
   - **Clarity**: Include assertion message explaining expected vs. actual behavior

5. **Provide Corrected Code**:
   - **Minimalism**: Make surgical, minimal changes (not comprehensive refactor)
   - **Comments**: Annotate the fix with brief explanation
   - **Best Practices**: Follow language idioms and conventions
   - **Completeness**: Code must pass the failing test and all edge cases

6. **Provide Passing Tests**:
   - **Validation**: Tests must pass with corrected code
   - **Coverage**: Include edge cases, boundary conditions
   - **Comprehensiveness**: Beyond just the failing test, demonstrate robustness

**Incremental Validation** (every 3 tasks):
- [ ] All tasks have single, focused bug (no multi-bug scenarios)
- [ ] All root-cause explanations include ≥1 citation
- [ ] All tasks have complete deliverables (buggy code, failing test, fix, explanation, passing tests)
- [ ] All citations use valid `[Ref: ID]` from Step 2
- [ ] Code lengths are 10-50 lines
- [ ] Difficulty distribution tracks to plan

**Output**: Completed task entries following Part III format

### Step 4: Alternatives

**Objective**: Provide fair, comprehensive grading guidance acknowledging multiple valid approaches and common pitfalls.

**Actions** (for each task):

1. **Document Alternative Valid Fixes**:
   - Identify 2-3 acceptable solutions (if multiple approaches exist)
   - Describe each approach concisely (1-2 sentences)
   - Compare trade-offs explicitly:
     - **Minimal fix**: Surgical change, preserves structure, quick
     - **Refactor**: Improves design, more maintainable, higher effort
     - **Alternative pattern**: Different algorithm/data structure, different performance characteristics
   - Assign point values: Full credit for any valid approach meeting correctness + best practices

2. **List Common Mistakes**:
   - Identify 3-5 typical wrong approaches candidates might try
   - Explain why each is incorrect or suboptimal
   - Link to misconceptions from Glossary or Literature (use `[Ref: ID]`)
   - Assign partial credit where diagnosis is correct but implementation flawed

3. **Create Grading Rubric**:
   - **Code Fix** (0-6 points):
     - 6 pts: Correct, minimal, follows best practices
     - 4-5 pts: Correct but over-engineered or style issues
     - 2-3 pts: Partially correct (fixes symptom, not root cause) or has edge case bugs
     - 1 pt: Incorrect but demonstrates understanding
     - 0 pts: No attempt or completely wrong
   
   - **Root-Cause Explanation** (0-3 points):
     - 3 pts: Accurate, clear, well-cited (≥1 authoritative source)
     - 2 pts: Accurate but lacks citation or clarity
     - 1 pt: Partially correct or incomplete
     - 0 pts: Incorrect or missing
   
   - **Tests** (0-1 point):
     - 1 pt: Tests present and validate fix
     - 0 pts: Tests missing, incorrect, or don't validate fix

4. **Flag Edge Cases**:
   - Note boundary conditions candidates might miss
   - Highlight assumptions that could lead to alternative interpretations
   - Document when to award partial credit for reasonable alternative assumptions

**Validation Check** (before proceeding):
- [ ] All tasks (100%) have documented grading rubrics
- [ ] ≥80% of tasks document alternative valid approaches
- [ ] All tasks list 3-5 common mistakes
- [ ] Rubrics enable consistent, objective scoring
- [ ] Trade-offs between alternatives are explicit

**Output**: Enhanced task entries with grading guidance

### Step 5: Compile References

**Objective**: Assemble complete, validated Reference Sections ensuring all inline citations resolve correctly.

**Actions**:

1. **Populate Glossary Section**:
   - Format: `**G#: Term/Acronym**: Definition [Lang]`
   - Sort: Alphabetical or by first usage
   - Content: All terms used in tasks requiring definition
   - Example: `**G1: Race Condition**: Flaw where behavior depends on timing of uncontrollable events [EN]`

2. **Populate Codebase & Library References**:
   - Format: `**C#: Project/Library** ([lang])`
   - Required fields: Repo URL, license, last update, stable release, audit status
   - Optional fields: Integration hooks, reliability metrics, vulnerability history
   - Link to official documentation
   - Example: `**C1: Go sync package** ([EN]) - Official concurrency primitives | License: BSD-3-Clause | Updated: 2024-10 | Stable: 1.21 | Docs: https://pkg.go.dev/sync`

3. **Populate Literature & Reports**:
   - Format: `**L#: Title** (Year) ([lang])`
   - Required fields: APA citation, persistent link (DOI/archived), key findings
   - Optional fields: Methodology, limitations, follow-up studies
   - Example: `**L1: IEEE Std 1012-2016** (2016) ([EN]) - Software Verification and Validation standard | DOI: 10.1109/IEEESTD.2016.7460968`

4. **Populate APA Citations**:
   - Format: APA 7th edition with language tags
   - Group by language: English section, Chinese section, Other languages section
   - Alphabetize within each language group
   - Include all sources cited as A# references

5. **Cross-Reference Validation**:
   - Extract all `[Ref: ID]` from task explanations and code comments
   - Verify each ID exists in Reference Sections
   - Check for orphaned references (defined but not cited)
   - Ensure ID uniqueness (no duplicates)

6. **Completeness Audit**:
   - Verify all required fields present for each reference type
   - Validate URL accessibility (manual spot-check or automated validation)
   - Confirm language tags present on all entries
   - Check publication years for recency requirements

**Validation Check** (before proceeding):
- [ ] All sections populated: Glossary ≥10, Codebase ≥5, Literature ≥6, APA ≥12
- [ ] Every `[Ref: ID]` from tasks resolves to exactly one Reference Section entry
- [ ] No orphaned references (all defined IDs are cited at least once)
- [ ] All required fields complete for each reference type
- [ ] All URLs validated or archived
- [ ] Language tags present on all entries
- [ ] ID numbering is sequential with no gaps

**Output**: Complete Reference Sections (Part III format)

### Step 6: Validate

**Objective**: Execute comprehensive validation protocol ensuring all quality gates pass before submission.

**Actions**:

1. **Execute Validation Steps** (all 11 checks from Part I, Pre-Submission Validation):
   - Work through validation table sequentially
   - Document results for each check in standard report format
   - Calculate percentages, counts, ratios as specified
   - Flag any failures with specific details (which tasks, which references, etc.)

2. **Generate Validation Report**:
   - Use standard format from Part I
   - Include actual counts, percentages, ratios
   - Mark each check as PASS or FAIL
   - List specific failures if any
   - Calculate overall status (PASS only if all 11 checks PASS)

3. **Fix Failures** (if any):
   - Prioritize fixes by impact (blocking issues first)
   - Common fixes:
     - **Count shortfalls**: Add missing references, tasks
     - **Citation coverage**: Add citations to under-cited explanations
     - **Language imbalance**: Replace or add references to achieve target distribution
     - **Recency issues**: Replace outdated sources with current alternatives
     - **Diversity problems**: Add underrepresented source types
     - **Broken links**: Update URLs or add archived versions
     - **Cross-ref errors**: Fix typos in IDs, add missing definitions
     - **Multi-bug tasks**: Split into separate focused tasks
     - **Incomplete deliverables**: Add missing tests, explanations, fixes
     - **Missing alternatives**: Document additional valid approaches

4. **Re-Validate** (iterate until clean pass):
   - After each fix cycle, re-run full 11-step validation
   - Update validation report
   - Continue iteration until ALL checks show PASS
   - Track iteration count (should converge within 2-3 cycles)

5. **Document Validation History** (for audit trail):
   - Note how many validation iterations required
   - Summarize major fixes applied
   - Confirm final status: ALL PASS

**Validation Check** (before proceeding):
- [ ] Validation report generated using standard format
- [ ] ALL 11 validation checks show PASS status
- [ ] Zero failures remaining
- [ ] Validation report attached to submission package

**Output**: 
- Final validation report (PASS status)
- Updated assessment with all fixes applied

### Step 7: Submit

**Objective**: Final verification and submission of validated, complete debugging assessment.

**Actions**:

1. **Complete Submission Checklist**:
   - Work through entire checklist from Part I, Submission Checklist
   - Tick each box only when verified complete
   - Do not skip or assume any items
   - Double-check success criteria and final confirmation items

2. **Assemble Submission Package**:
   - **Main Assessment**: Complete document following Part III format
   - **Validation Report**: Final report showing all PASS status
   - **Metadata**: Task count, difficulty distribution, language distribution, reference counts
   - **Execution Notes** (optional): Any special considerations, domain-specific context, usage recommendations

3. **Final Quality Review**:
   - Read through entire assessment for coherence
   - Spot-check random tasks for completeness
   - Verify formatting consistency (markdown, code blocks, links)
   - Confirm table of contents links work
   - Test random reference citations resolve correctly

4. **Submit for Review**:
   - Include submission checklist (all boxes ticked)
   - Attach validation report
   - Note any exceptional circumstances or clarifications
   - Request specific feedback if needed

**Pre-Submission Gate** (mandatory verification):
- [ ] Submission Checklist: ALL boxes ticked
- [ ] Validation Report: ALL checks PASS
- [ ] Format: Follows Part III structure exactly
- [ ] Table of Contents: Links to all sections work
- [ ] References: All citations resolve, all links accessible
- [ ] Tasks: All deliverables complete and correct
- [ ] No placeholders, TODOs, or incomplete sections remain

**Success Criteria** (outcomes achieved):
- Assessment is immediately usable for technical interviews
- Grading can be performed consistently by any reviewer using provided rubrics
- All technical claims are verifiable through citations
- Assessment demonstrates both breadth and depth appropriate for target role level

**MANDATORY**: Do not submit until ALL pre-submission gate items verified. Submission with failures will be rejected and require complete re-validation cycle.

---

# Part III: Output Format

**Structure Requirements**: Generate assessment using this exact format with complete table of contents and structured sections.

**Formatting Standards**:
- **Table of Contents**: Required at document start; links to all major sections and individual tasks
- **Lists**: Use for enumeration, checklists, multi-item content
- **Tables**: Use for structured data (reference inventories, grading rubrics, validation reports)
- **Diagrams**: Use Mermaid for architecture, flow diagrams (if needed for complex bugs)
- **Code Blocks**: Use language-tagged fences (```python, ```javascript, etc.)
- **Formulas**: Use LaTeX math notation if presenting algorithmic complexity
- **Links**: Use markdown link syntax `[text](#anchor)` for navigation

---

## Task Bank Structure

**Example Output Template**:

```markdown
## Contents

- [Task Bank](#task-bank-tasks-1-n)
  - [Topic 1: [Bug Cluster Name]](#topic-1-bug-cluster-name)
    - [Task 1: [Bug Description]](#task-1-bug-description)
    - [Task 2: [Bug Description]](#task-2-bug-description)
  - [Topic 2: [Bug Cluster Name]](#topic-2-bug-cluster-name)
    - [Task 3: [Bug Description]](#task-3-bug-description)
    - [Task 4: [Bug Description]](#task-4-bug-description)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Codebase & Library References](#codebase--library-references)
  - [Authoritative Literature & Reports](#authoritative-literature--reports)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Task Bank (Tasks 1–N)

### Topic 1: [Bug Cluster Name]

**Cluster Description**: [1-2 sentence overview of this bug category]

#### Task 1: [Concise Bug Description]

**Language:** [python/javascript/go/rust/solidity/etc.] | **Difficulty:** [Foundational/Intermediate/Advanced]

**Buggy Code:**
```[language]
# [Context comment if needed]
# [Code may include [Ref: ID] citations in comments for API patterns]
[Code with single, focused bug - 10 to 50 lines]
```

**Failing Output:** 
```
[Error message, stack trace, or unexpected behavior description]
```

**Failing Test:**
```[language]
# Test demonstrating the bug
[Test case that fails with buggy code]
```

**Corrected Code:**
```[language]
# [Comment explaining the fix]
[Fixed code with minimal, surgical changes]
```

**Root Cause:** 
[Sentence 1: What the bug is] [Sentence 2: Why it occurs] [Sentence 3: Reference to authoritative source [Ref: ID]] [Sentence 4 (optional): Impact or misconception]

**Passing Tests:**
```[language]
# Tests validating fix including edge cases
[Comprehensive test cases that pass with corrected code]
```

**Grading Rubric:**
- **Code Fix (0-6 pts)**:
  - 6 pts: Correct, minimal, best practices
  - 4-5 pts: Correct but over-engineered or style issues
  - 2-3 pts: Partially correct or edge case bugs
  - 1 pt: Incorrect but shows understanding
  - 0 pts: No attempt or completely wrong
- **Explanation (0-3 pts)**:
  - 3 pts: Accurate, clear, well-cited
  - 2 pts: Accurate but lacks citation/clarity
  - 1 pt: Partially correct
  - 0 pts: Incorrect or missing
- **Tests (0-1 pt)**:
  - 1 pt: Present and validates fix
  - 0 pts: Missing or incorrect

**Common Mistakes:**
1. [Mistake 1]: [Why it's wrong] [Ref: ID if applicable]
2. [Mistake 2]: [Why it's wrong]
3. [Mistake 3]: [Why it's wrong]
4. [Mistake 4]: [Why it's wrong]
5. [Mistake 5]: [Why it's wrong]

**Alternative Valid Fixes:**
- **Approach 1** (Minimal fix): [Description] | Trade-off: [Quick but preserves technical debt]
- **Approach 2** (Refactor): [Description] | Trade-off: [Better design but higher effort]
- **Approach 3** (Alternative pattern): [Description] | Trade-off: [Different performance characteristics]

---

[Repeat task structure for all 15-22 tasks]

---

## Reference Sections Structure

**Purpose**: Provide authoritative foundation for all technical claims, enable verification, support self-study.

**Usage Pattern**: 
- Inline citations: `[Ref: ID]` in root-cause explanations and code comments
- Reference mapping: G# (Glossary), C# (Codebase), L# (Literature), A# (APA)
- Example: "Bug stems from type coercion [Ref: G5] as defined in ECMAScript specification [Ref: A3], causing unexpected behavior documented in [Ref: L3]."

**Minimum Requirements**:

| Section | Count | Content Type | Quality Gate |
| --- | --- | --- | --- |
| Glossary | ≥10 | Core concepts, jargon, acronyms | Clear, concise definitions |
| Codebase & Libraries | ≥5 | Stack components, SDKs, tools | Maturity indicators required |
| Literature & Reports | ≥6 | Standards, peer-reviewed, audits | Persistent links required |
| APA Citations | ≥12 | Mixed sources | Language diversity (60/30/10) |

**Exception Handling**: 
If minimums cannot be met, document:
- **Shortfall**: "Literature: 4/6 (2 short)"
- **Reason**: "Limited peer-reviewed research on [specific technology]"
- **Plan**: "Will substitute with 2 additional official documentation sources"
- **Timeline**: "Pending approval by [date]"

---

### Glossary, Terminology & Acronyms

**Format**: `**G#: Term/Acronym**: Definition [Lang]`

**Content**: Core technical terms, domain jargon, acronyms requiring definition for clarity.

**Examples**:
- `**G1: Race Condition**: Behavior flaw where output depends on timing of uncontrollable events, leading to non-deterministic results [EN]`
- `**G2: MECE**: Mutually Exclusive, Collectively Exhaustive - framework ensuring categories don't overlap yet cover all possibilities [EN]`
- `**G3: 类型强制转换**: Automatic or explicit conversion between data types that may cause unexpected behavior [ZH]`

**Quality Standards**:
- Definitions are precise, complete, understandable
- Technical accuracy verified against authoritative sources
- Avoid circular definitions
- Include language tag for multilingual terms

---

### Codebase & Library References

**Format**: `**C#: Project/Library** ([lang])`

**Required Fields**:
- Repository URL (GitHub: owner/repo, GitLab, etc.)
- License type (MIT, Apache-2.0, BSD, GPL, etc.)
- Last update date (must be ≤12 months for passing quality gate)
- Stable release version
- Audit status (if applicable: "Audited by [firm] on [date]" or "No public audit")

**Optional Fields**:
- Integration patterns, hooks, middleware support
- Reliability metrics (uptime, issue resolution time)
- Language/platform support matrix
- Known vulnerabilities (CVE numbers if applicable)

**Example**:
```markdown
**C1: Go sync Package** ([EN])
- **Repository**: https://go.googlesource.com/go/+/refs/heads/master/src/sync
- **License**: BSD-3-Clause
- **Last Update**: 2024-10
- **Stable Release**: Go 1.21+
- **Documentation**: https://pkg.go.dev/sync
- **Maturity**: Core Go standard library, extensively tested
- **Audit**: Part of Go security audit program
```

---

### Authoritative Literature & Reports

**Format**: `**L#: Title** (Year) ([lang])`

**Required Fields**:
- Full APA citation with language tag
- Persistent link (DOI preferred, or archived URL)
- Key findings (relevant bug patterns, vulnerabilities, best practices)
- Methodology (sample size, scope, approach)
- Impact (citation count, adoption in standards)

**Optional Fields**:
- Limitations acknowledged by authors
- Replication studies
- Follow-up research
- Jurisdiction or domain constraints

**Example**:
```markdown
**L1: IEEE Std 1012-2016 - System, Software, and Hardware Verification and Validation** (2016) ([EN])
- **Citation**: IEEE. (2016). IEEE Standard for System, Software, and Hardware Verification and Validation (IEEE Std 1012-2016). IEEE. https://doi.org/10.1109/IEEESTD.2016.7460968
- **Key Findings**: Defines V&V processes for detecting defects across lifecycle; emphasizes systematic testing of edge cases and concurrency bugs
- **Methodology**: Industry consensus standard developed by working group
- **Impact**: Widely adopted in safety-critical systems; referenced in >500 publications
- **Scope**: Applies to all system complexity levels
```

---

### APA Style Source Citations

**Format**: APA 7th edition, grouped by language, with language tags

**Language Grouping** (required):
1. **English Sources** (~60%)
2. **Chinese Sources** (~30%)
3. **Other Languages** (~10%)

**Within Each Group**: Alphabetize by author surname

**Quality Requirements**:
- Complete APA 7th format (author, year, title, publication, DOI/URL)
- Language tag at end of each entry: [EN], [ZH], [JA], [KO], etc.
- Recency: ≥50% from last 3 years (≥70% for AI/security topics)
- Diversity: Mix of academic, industry, official documentation

**Examples**:

**English Sources [EN]**

```
Dijkstra, E. W. (1965). Solution of a problem in concurrent programming control. Communications of the ACM, 8(9), 569. https://doi.org/10.1145/365559.365617 [EN]

Smith, J. P., & Johnson, M. K. (2024). Modern debugging techniques for distributed systems. ACM Transactions on Software Engineering, 15(3), 245-267. https://doi.org/10.1145/xxxxxxx [EN]

Mozilla Developer Network. (2024). JavaScript type coercion. https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion [EN]
```

**Chinese Sources [ZH]**

```
张伟, & 李娜. (2024). 并发编程中的常见错误模式. 计算机科学, 51(2), 88-95. https://doi.org/10.xxxx [ZH]

王强, 刘洋, & 陈晨. (2023). 区块链智能合约安全审计方法研究. 软件学报, 34(5), 2103-2120. https://doi.org/10.xxxx [ZH]
```

**Other Languages**

```
Sato, T., & Yamamoto, K. (2024). ソフトウェアデバッグの体系的手法. 情報処理学会論文誌, 65(4), 512-528. [JA]
```

---

## Validation

**Before finalizing output, execute Pre-Submission Validation (Part I) and attach validation report showing ALL PASS status.**


