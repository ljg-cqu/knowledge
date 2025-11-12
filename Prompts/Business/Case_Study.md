# Case Study: Business-to-Architecture Assessment Generator

Generate assessments evaluating technical leaders' ability to translate business requirements into architecture decisions for exam designers, educators, enterprise architects, training developers.

**Key Concepts:**
- **BMC**: 9-block strategic template (Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure)
- **VPC**: Value propositions aligned to customer jobs, pains, gains
- **DDD**: Ubiquitous language, bounded contexts, strategic/tactical patterns
- **ADR**: Architecture decisions with context, rationale, consequences
- **Conway's Law**: Systems mirror organizational communication structure
- **Wardley Mapping**: Component evolution visualization (genesis → commodity)
- **MECE**: Mutually Exclusive, Collectively Exhaustive

## Requirements

### Scenario Bank

**Scope:** 16–22 scenarios; 20% Foundational / 40% Intermediate / 40% Advanced; 5 clusters with 3–5 scenarios each: (1) Strategic Modeling, (2) Value & Risk Analysis, (3) Organizational Dynamics, (4) Architectural Translation, (5) Evolution & Adaptation.

**Diversity:** ≥3 industries (tech, healthcare, finance, manufacturing); ≥2 company sizes (startup, SME, enterprise); ≥2 regions (NA, EU, Asia).

### Scenario Structure

Each scenario includes:

**Context (200–400 words):** ≥2 constraints, ≥2 stakeholder roles (diverse: C-suite, engineers, customers, regulators), ≥1 market dynamic, ≥1 organizational factor, ≥1 `[Ref: ID]`.

**Tasks (3–4):** MECE tasks spanning business analysis → architecture decisions. Types: BMC analysis, value mapping, risk assessment, decision memos, stakeholder communication.

**Deliverables:**
- **BMC Analysis:** Affected blocks, value proposition changes, customer segment implications (table/list)
- **Value Matrix:** Value propositions → technical features + risk model with prioritization (2-column table)
- **Risk Assessment:** Business/operational/regulatory risks with severity (High/Medium/Low)
- **Decision Memo:** ≤300 words: recommendations, justification, trade-offs, stakeholder alignment

**Grading:** Business analysis (30%), value mapping (25%), architecture decisions (30%), justification (15%). Specify partial credit allocations.

**Trade-Offs:** Address value vs technical debt, revenue vs complexity, stakeholder alignment vs design purity, speed vs quality.

**Conflicts:** When frameworks conflict (BMC vs Lean Canvas, DDD vs pragmatism), present both with citations, state trade-offs, recommend context-specific choice with rationale.

### References

**Language:** ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH])

**Source Types (all 4 required):** (1) Business frameworks (BMC, Lean Canvas, VPC), (2) Architecture patterns (DDD, microservices, event-driven), (3) Case studies/reports, (4) Tools (modeling, documentation).

**Format:** APA 7th + language tags. Inline: `[Ref: ID]`.

**Minimums:** Glossary ≥10 (BMC, Value Proposition, DDD, Conway's Law, Technical Debt, ADR, Bounded Context, Wardley Mapping), Tools ≥5 (Miro, ArchiMate, C4, Confluence, Wardley Maps), Literature ≥6 (Osterwalder, Evans, Vernon, Conway, Hohpe, Richardson + ZH sources), APA ≥12. If unmet: state shortfall, rationale, sourcing plan. Scale: >25 scenarios → 1.5×.

---

## Output Format

### Structure

**Contents:** TOC linking to Scenario Bank, Reference Sections (Glossary, Tools, Literature, APA Citations), Validation Report.

### Scenario Template

**Scenario X: [Title]** | **Difficulty:** [F/I/A] | **Domain:** [Cluster]

**Context:** 200–400 words (≥2 constraints, ≥2 stakeholders, ≥1 market dynamic, ≥1 org factor, ≥1 `[Ref: ID]`)

**Task 1: [Name] (X pts)**  
Description requiring deliverable.  
**Expected:** [Key elements]  
**Grading:** [Criterion 1 (X pts) partial credit breakdown | Criterion 2 (Y pts) | ...]

**Task 2–4:** [Repeat]

**Common Omissions:** [e.g., Conway's Law impact, evolution strategy, value-architecture tracing]

**Bonus (1–2 pts):** [Advanced considerations]

### Reference Templates

**IDs:** Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), APA (A1…An). Inline: `[Ref: G1, T2, A5]`.

**Glossary:** Table: ID, Term, Definition, Use Cases, Related Terms. Cover: BMC, Value Proposition, DDD, Conway's Law, Technical Debt, ADR, Bounded Context, Wardley Mapping, Customer Segment, Revenue Stream, Value Stream Mapping, System Boundaries, Process Mapping.

**Tools:** Table: ID, Name, Description, Pricing ("N/A" if FOSS), Adoption (cited/"approximate"), Last Updated (≤18 months or "(legacy)"), Integrations ("standalone" if none), Use Cases, URL. Examples: Miro, ArchiMate, C4, Confluence, Wardley Maps.

**Literature:** Table: ID, Citation, Description. Examples: Osterwalder, Evans, Vernon, Conway, Skelton & Pais, Richardson, 周爱民, 张逸, 肖然.

**APA:** Full citations with language tags. Verify publication year/author. Web refs: archived link or "as of [date]". Tool stats: cite source or "approximate".

### Validation Checklist

Execute all; proceed only when all PASS. If FAIL: remediate and re-validate.

| # | Check | Target | Result | Status |
|---|-------|--------|--------|--------|
| 1 | Count Audit | Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12 | [counts] | PASS/FAIL |
| 2 | Difficulty | 20/40/40 ±5% | [F%/I%/A%] | PASS/FAIL |
| 3 | Citation Coverage | ≥70% scenarios with ≥1, ≥30% with ≥2 | [%] | PASS/FAIL |
| 4 | Language | EN ~50-70%, ZH ~20-40%, Other ~5-15% | [%] | PASS/FAIL |
| 5 | Recency | ≥50% from 2022-2025 (≥70% digital) | [%] | PASS/FAIL |
| 6 | Source Diversity | ≥3 types, no source >25% | [types, max%] | PASS/FAIL |
| 7 | Links | All accessible OR archived | [broken: URLs] | PASS/FAIL |
| 8 | Cross-Refs | All `[Ref: ID]` resolve | [broken: IDs] | PASS/FAIL |
| 9 | Context Length | 200–400 words | [sample 5] | PASS/FAIL |
| 10 | MECE Tasks | No overlaps/gaps | [issues] | PASS/FAIL |
| 11 | Rubrics | Complete with partial credit | [missing] | PASS/FAIL |
| 12 | Business-Tech Map | ≥80% explicit connection | [%] | PASS/FAIL |
| 13 | Stakeholder Diversity | ≥70% diverse roles (not C-suite only) | [%] | PASS/FAIL |
| 14 | Industry/Size/Region | ≥3 industries, ≥2 sizes, ≥2 regions | [lists] | PASS/FAIL |
| 15 | TOC & Anchors | Functional links | [Y/N] | PASS/FAIL |

## Generation Procedure

Execute sequentially. Validate at checkpoints (✓).

**Step 1: Plan** — Allocate 16–22 scenarios across 5 clusters (3–5 each): Strategic Modeling, Value & Risk Analysis, Organizational Dynamics, Architectural Translation, Evolution & Adaptation. Assign difficulty: 20% F, 40% I, 40% A.  
**✓** Total 16–22? Difficulty 20/40/40 ±5%?

**Step 2: Collect References** — Gather Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12 (language ~60/30/10). Assign IDs: G1-Gn, T1-Tn, L1-Ln, A1-An.  
**✓** Counts met? Language ~60/30/10? Recency ≥50% (≥70% digital)? Diversity ≥3 types, no source >25%?

**Step 3: Generate Scenarios** — For each: (1) Context 200–400 words (≥2 constraints, ≥2 stakeholders, ≥1 market dynamic, ≥1 org factor, ≥1 `[Ref: ID]`; vary industry/size/region); (2) Design 3–4 MECE tasks (business analysis → architecture decisions; deliverables: BMC analysis, value matrix, risk assessment, decision memo); (3) Create rubrics (30/25/30/15%) with partial credit and common omissions; (4) Add bonus (1–2 pts).  
**✓** (Every 3 scenarios) Context 200–400 words, ≥1 citation, diverse stakeholders? MECE? Rubrics complete? Diversity?

**Step 4: Compile References** — Populate tables (Glossary: ID/Term/Definition/Use Cases/Related; Tools: ID/Name/Description/Pricing/Adoption/Updated/Integrations/Use Cases/URL; Literature: ID/Citation/Description; APA: full with tags). Verify all inline `[Ref: ID]` resolve.  
**✓** All refs resolve? Required fields present? Tool stats cited/"approximate"?

**Step 5: Validate** — Execute 15 checks (Validation Checklist). If FAIL: remediate and re-validate. Proceed only when all PASS.

**Step 6: Finalize** — Verify TOC/anchors, match output format, review clarity/concision/coherence.
