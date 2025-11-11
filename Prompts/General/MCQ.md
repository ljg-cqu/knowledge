# Multiple-Choice Questions

LLM-friendly, self-contained framework for generating high-quality MCQ assessments for senior/architect/expert roles.

---

## Contents

- [Part 0: Task Definition & Inputs](#part-0-task-definition--inputs)
- [Part I: Specifications & Quality Gates](#part-i-specifications--quality-gates)
- [Part II: Process & Instructions](#part-ii-process--instructions)
- [Part III: Output Format](#part-iii-output-format)
- [Success Criteria](#success-criteria)
- [Validation Report Template](#validation-report-template)
- [Traceability: Guidelines 1–21](#traceability-guidelines-121)
- [Changelog](#changelog)

---

# Part 0: Task Definition & Inputs

Purpose: Define scope, assumptions, parameters, inputs, and outputs to satisfy Guidelines 1–4 (Context, Clarity, Precision, Relevance).

- Audience/levels: Senior engineer, architect, expert practitioners.
- Scope: Domain-agnostic template; parameterize specifics via config.
- Non-goals: Do not generate a concrete MCQ bank in this doc; this is the prompt template.
- Assumptions: Ethical use only; avoid harmful/unsafe content; cite authoritative sources.
- Inputs (required):
  - Subject/topic and intended audience
  - Any must-include sources/standards
  - Language and difficulty preferences (or defaults)
- Outputs: A complete MCQ bank plus validation artifacts, following the schema in Part III.

Parameters (override as needed; defaults chosen for general use):

```yaml
config:
  subject: "General"
  question_count: 60
  difficulty_mix: { foundational: 0.2, intermediate: 0.4, advanced: 0.4 }
  language_distribution: { en: 0.6, zh: 0.3, other: 0.1 }
  other_languages: []
  recency_threshold_months: 36
  allowed_evidence_types: [ "official_docs", "standards_peer_reviewed", "audits_reports", "vetted_code" ]
  evidence_required_ratio: 0.7   # ≥70% with ≥1 citation; ≥30% with ≥2 (see Part I)
  citation_style: "APA7"
  controversial_flag_required: true
  seed: 42
```

Terminology: stem, options, distractors, key (correct option), rationale, misconception, evidence, confidence.

Clarity & Concision: Use precise terminology; avoid undefined jargon; exclude tangential content; remove redundancy.

---

# Part I: Specifications & Quality Gates

## Scope and Structure

- Quantity: 40–80 questions (use config.question_count)
- Format: 1–2 sentence stems; 4 options; exactly one correct
- Difficulty: Foundational/Intermediate/Advanced per config.difficulty_mix
- Topic design: Organize topic clusters using MECE; state assumptions and exclusions
- Distractors: Map to specific misconceptions or outdated practices
- Rationale: 1–2 sentences with inline citations [Ref: ID]
- Grading: Machine-gradable; no partial credit
- Contentious topics: Represent competing views; rationale clarifies consensus

## Citation Standards

- Languages: Target distribution per config.language_distribution (tag items [EN], [ZH], or specific language tags)
- Source types (prioritized):
  1) Official docs (specs, RFCs, vendor docs)
  2) Standards/peer-reviewed (ISO, IEEE, journals, conferences)
  3) Audits/reports (security, industry, regulatory)
  4) Vetted code (stable production repos)
- Format: APA 7th with language tags; include working URLs and access dates
- Inline: Use [Ref: ID] in rationales for specs/standards/research
- Uncertainty: Flag contested claims; include confidence score per item

## Quality & Reasoning Requirements

- Significance & Value: Explain why each question matters to real practice
- Risk & Mitigation: Note common failure modes and mitigations or acceptance criteria
- Fairness & Bias: Call out assumptions, limits, or potential biases; include counterpoints for contentious topics
- Logic & Verification: Provide explicit reasoning chains; add self-review notes where ambiguity may exist
- Practicality: Assess actionable knowledge with clear success criteria

## Minimums (single source of truth)

- Glossary & Terminology: ≥10
- Codebase & Libraries: ≥5
- Literature & Reports: ≥6
- APA Citations: ≥12 (≈60% EN, ≈30% ZH, ≈10% other)
- Recency: ≥50% within last 36 months (≥70% for AI/security)
- Source diversity: ≥3 types; no single source >25%
- Evidence coverage: ≥70% questions with ≥1 citation; ≥30% with ≥2
- Codebase maturity: License, last commit ≤12 months, stable release, audit status
- Deduplication: Use persistent links (DOI, archived URLs); avoid duplicates
- Link validity: All links resolve or archived alternative provided
- Cross-references: All [Ref: ID] link to Reference Sections

> Scaling: For >80 questions or regulated domains, increase minimums by 1.5×.

## Pre-Submission Validation

Execute all steps. Present validation report. Fix failures and re-validate until all pass.

1) Count Audit
- Report: `G:X (≥10) | C:Y (≥5) | L:Z (≥6) | A:W (≥12) | Q:N (F/I/A)`
- Pass: All minimums met AND difficulty ≈20/40/40

2) Citation Coverage
- Report: `X/Y ≥1 citation (Z%); W/Y ≥2 (V%)`
- Pass: ≥70% with ≥1; ≥30% with ≥2

3) Language Distribution
- Report: `EN:X (Y%) | ZH:A (B%) | Other:C (D%)`
- Pass: EN 50–70%, ZH 20–40%, Other 5–15%

4) Recency
- Report: `X/Y (Z%) from last 36 months`
- Pass: ≥50% (≥70% AI/security)

5) Source Diversity
- Report: `Type1:X Type2:Y Type3:Z Type4:W | Types:N | Max:M (P%)`
- Pass: ≥3 types AND max ≤25%

6) Link Validation
- Report: `X links: Y accessible, Z broken` (list broken)
- Pass: All accessible OR archived provided

7) Cross-Reference Integrity
- Report: `X refs: Y resolve, Z broken` (list broken)
- Pass: Z=0

8) Answer Correctness
- Report: `X/Y exactly one; Z issues` (list)
- Pass: Z=0

9) Distractor Quality
- Report: `X/Y quality; Z weak` (list)
- Pass: Z=0

10) Option Clarity
- Report: `X/Y clear; Z vague` (list)
- Pass: Z=0

11) Conflict Handling
- Report: `X applicable; Y comply (Z%)`
- Pass: ≥80% comply

12) Fairness, Risk & Logic Review
- Report: `Significance: X/Y | Risk: W/Y | Fairness: V/Y | Reasoning: U/Y`
- Pass: All four ≥90% (or document shortfalls with remediation plan)

> MANDATORY: If ANY check shows FAIL, stop, fix, regenerate affected sections, and re-run full validation. Only proceed when ALL checks PASS.

## Submission Checklist (summary)

- [ ] Minimums met (G≥10, C≥5, L≥6, A≥12)
- [ ] Difficulty 20/40/40 (F/I/A)
- [ ] Languages ≈60% EN, ≈30% ZH, ≈10% other
- [ ] Recency ≥50% last 36 months (≥70% AI/security)
- [ ] Diversity ≥3 types, max 25%
- [ ] Citations coverage (≥70% ≥1, ≥30% ≥2)
- [ ] One correct, quality distractors, unambiguous options
- [ ] Significance, risk/mitigation, fairness noted per question
- [ ] Reasoning chains or validation notes in rationales
- [ ] Codebase maturity criteria logged
- [ ] Links resolve or archived
- [ ] Cross-refs present and resolve
- [ ] Rationales concise with citations
- [ ] Validation report shows all PASS

---

# Part II: Process & Instructions

Execute sequentially with self-checks and failure handling at each step.

### Step 1: Topic Planning (Guidelines 5–8)
1) Identify 4–8 MECE topic clusters
2) Allocate 5–10 questions per cluster (total per config.question_count)
3) Assign difficulty per config.difficulty_mix
4) Self-check: Total, MECE compliance, difficulty ratio; fix gaps before proceeding

### Step 2: Reference Collection (Guidelines 11–12, 18)
1) Gather: ≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 APA
2) Tag: language [EN]/[ZH]/other, year, type (1–4)
3) Assign IDs: G#, C#, L#, A#
4) Self-check: Counts, language distribution, recency window, ≥3 source types

### Step 3: Question Generation (Guidelines 9–10, 13–15)
1) Write: stem (1–2 sentences), 4 options (one correct), difficulty + language
2) Add: significance and fairness notes for each item
3) Rationale: ≥1 [Ref: ID] (prefer standards/peer-reviewed for claims)
4) Distractors: Map to specific misconceptions
5) Self-check (every 10): one correct, quality distractors, ≥1 citation, fairness notes, clear options

### Step 4: Distractor Documentation (Guidelines 14–15)
1) For every distractor: why incorrect; which misconception
2) Note common mistake patterns; include risk/mitigation where applicable
3) Self-check: all mapped and documented

### Step 5: Reference Compilation (Guidelines 16–18)
1) Populate: Glossary, Codebase, Literature, APA
2) Include required fields; ensure persistent links
3) Match [Ref: ID] to entries
4) Self-check: all refs resolve; fields present; fairness/risk notes trace to references when applicable

### Step 6: Validation (Guidelines 19–21)
Run all 12 checks from Part I; present the report; fix failures; re-validate.

### Step 7: Final Review
Verify Submission Checklist; ensure coherence, clarity, and no tangents remain.

---

# Part III: Output Format

Start the output with a TOC linking to all top-level headings and list items. Use lists, tables, Mermaid diagrams if needed, and language-tagged code fences.

## Primary schema (JSONL)

```json
{"id":"Q001","language":"en","topic":"...","difficulty":"intermediate","stem":"...","options":["...","...","...","..."],"key":"B","rationale":"... [Ref: L3]","misconceptions":["..."],"evidence":[{"title":"...","url":"...","accessed":"2025-10-20","citation":"... [EN]"}],"confidence":0.82}
```

Constraints: language in {en, zh, other}; difficulty in {foundational, intermediate, advanced}; key in {A,B,C,D}; confidence in [0,1].

## Optional human-readable Markdown

```markdown
### Topic 1: [Topic title]

#### Q1: [Question text]

- A. [Option]
- B. [Option]
- C. [Option]
- D. [Option]

Answer: [A/B/C/D]
Rationale: [1–2 sentences; with [Ref: ID]]
Value & Risk: [Why it matters; risks and mitigations]
Fairness & Bias: [Assumptions, limits, counterpoints]
Distractor notes: [Why incorrect; mapped misconception]
```

## Reference Sections

Use [Ref: ID] to cite sources: G# (Glossary), C# (Codebase), L# (Literature), A# (APA).

Example: "Answer B is correct because consensus algorithms require Byzantine fault tolerance [Ref: G2] per protocol design [Ref: L5]."

### Glossary, Terminology & Acronyms

Format:

```text
**G1: Term/Acronym**: Definition [Language Tag]
```

Example:

```text
**G1: MECE** (Mutually Exclusive, Collectively Exhaustive): Categories don't overlap and cover all possibilities [EN]
```

### Codebase & Library References

C1: [Name] ([lang])

Required:
- Stack: Core SDK/components
- Maturity: License, update ≤12mo, stable release
- Benchmarks: Performance, audit, adoption

Optional:
- Integration hooks, HA, language support, CVEs

Format: Repo URL (GitHub: owner/repo | License), docs, maturity.

### Authoritative Literature & Reports

L1: [Title] (Year) ([lang])

Required:
- Findings: Claims, practices, standards
- Methodology: Sample size, scope
- Impact: Citations, adoption

Optional:
- Limitations, replication, follow-ups, jurisdiction

Format: APA citation with tag, persistent link (DOI/archived).

### APA Style Source Citations

Group by language per config.language_distribution. Use APA 7th with tags.

Example:

```text
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms: A comparative analysis.
    Journal of Distributed Systems, 15(3), 245–267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究.
    计算机科学, 51(2), 88–95. [ZH]

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system.
    https://bitcoin.org/bitcoin.pdf [EN]
```

---

# Success Criteria

- All Minimums satisfied; distributions within target ranges
- Evidence coverage and recency met; uncertainties flagged with confidence scores
- No ambiguous or overlapping options; no unjustified all/none-of-the-above
- Each item includes significance, risk/mitigation, fairness notes, and a concise rationale
- Schema-valid JSONL; optional Markdown section consistent with schema
- TOC links and [Ref: ID] cross-references resolve; links accessible or archived
- Code fences balanced; language tags present; lines kept ≤120 chars

---

# Validation Report Template

```text
Inputs: {config summary}

Counts: G:X C:Y L:Z A:W | Q:N (F/I/A)
Languages: EN:X% ZH:Y% Other:Z%
Recency: X/Y last 36 months
Diversity: Types=N, Max=P%
Links: Y/X accessible (list broken)
Cross-refs: Y/X resolved (list broken)
Correctness: Y/X exactly one (list issues)
Distractor Quality: Y/X quality (list weak)
Option Clarity: Y/X unambiguous (list vague)
Conflict Handling: Y applicable; Y comply (Z%)
Fairness/Risk/Reasoning: S:X/Y R:W/Y F:V/Y Logic:U/Y
Status: PASS/FAIL with remediation notes
```

---

# Traceability: Guidelines 1–21

- 1 Context: Part 0 (scope, assumptions)
- 2 Clarity: Part 0 (terminology, concision rules)
- 3 Precision: Part 0 (parameters); Part I (definitions)
- 4 Relevance: Part 0 (relevance filter)
- 5 MECE: Part II Step 1; Part I (topic design)
- 6 Sufficiency: Part I (Minimums); Part II checks
- 7 Breadth: Part I (contentious topics; perspectives)
- 8 Depth: Part I (difficulty); Part II (cognition via rationale depth)
- 9 Significance: Part I; Part II Step 3 (per-item)
- 10 Concision: Part 0 rules; Submission review
- 11 Accuracy: Part I (evidence, validation)
- 12 Credibility/Reliability: Part I (source types, maturity)
- 13 Logic: Part I (reasoning requirements)
- 14 Risk/Value: Part I (risk/mitigation)
- 15 Fairness: Part I; Part II Steps 3–4
- 16 Structure: Parts I–III; schema and sections
- 17 Output Format: Part III; TOC
- 18 Evidence: Part I (citations, recency); Part II Step 5
- 19 Validation: Part I (12 checks); Part II Step 6
- 20 Practicality: Part I (practicality); templates in Part III
- 21 Success Criteria: Success Criteria section; Validation Report Template

---

# Changelog

- Rewrote for LLM-friendliness with explicit Part 0 (context, parameters)
- Consolidated Minimums; added uncertainty/confidence and schema
- Added self-checks, failure handling, and success criteria
- Added full traceability to Guidelines 1–21
- Fixed code fence balance; standardized language tags and anchors


