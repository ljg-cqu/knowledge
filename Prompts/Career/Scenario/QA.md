# PM Scenario Generator (Minimal Viable)

**Purpose**: Generate 6–8 decision-critical PM scenarios to validate PM capabilities under time pressure with limited resources.

**Context**: For PM teams, training, capability validation, executive alignment. Assumes PM framework knowledge (RICE, JTBD, OKR, AARRR).

**Constraints**: 150–250 words/scenario; ≥70% cited; decision-critical conflicts only (revenue impact, strategic pivot, market risk); 5–10min/scenario.

**Cadence**: Per training cycle | 4–6h effort | Reusable across sessions

**Terms**: **B/I/A** = Basic (execution) / Intermediate (trade-offs) / Advanced (portfolio/P&L/vision) | **UC** = Use Case (scenario) | **MECE** = Mutually Exclusive, Collectively Exhaustive | **RICE** = Reach, Impact, Confidence, Effort | **JTBD** = Jobs-To-Be-Done | **PMF** = Product-Market Fit | **North Star** = Key value metric | **Decision Criticality** = Blocks decision, Creates risk, Affects ≥2 stakeholders, Actively evolving, Quantified impact (revenue $, pipeline $, adoption %, retention %, or market share)

## Table of Contents
1. [Requirements](#requirements)
2. [Execution](#execution)
3. [Validation](#validation)
4. [Output Format](#output-format)
5. [Example](#example)

## Requirements

### Quantitative Floors (60% reduction)

| Component | Requirements |
|-----------|--------------|
| **Scenarios** | 6–8 \| 25/50/25% B/I/A (±5%) \| 150–250 words \| ≥70% ≥1 cite, ≥30% ≥2 cites |
| **Capabilities** (Decision-Critical) | Strategy & Prioritization (2–3) \| Metrics & Decision-Making (2–3) \| Stakeholder Alignment (1–2) \| (Optional) GTM (1) |
| **References** | Glossary ≥8 \| Tools ≥3 \| Literature ≥4 (≥1 Chinese) \| Citations ≥8 APA 7th + [EN]/[ZH] |
| **Visuals** | ≥1 diagram + ≥1 table per capability (total: ≥3 diagrams + ≥3 tables) |
| **Scaling** | >8 scenarios: multiply floors by 1.25× |

**Outcomes**: Capability validation (85%+ alignment, 30% faster planning), maturity assessment, executive alignment (1 session vs. 6+ months).

**Scope**: Decision-blocking conflicts (revenue >$1M, strategic pivot, market risk), multi-stakeholder impact, resource constraints, data ambiguity.  
**Excluded**: Feature checklists, greenfield design, implementation details, niche scenarios (<5% adoption).

**Limitations**: Generic scenarios lack domain context (customize for industry); framework misapplication risk (include limitations); depth over speed trade-off.

### Citations

**Format**: APA 7th + [EN]/[ZH] | **Inline**: `[Ref: ID]` where ID = G#(Glossary), T#(Tool), L#(Literature), A#(Citation)  
**Distribution**: EN 50–70%, ZH 20–40%, Other 5–15% | **Types** (≥3): Frameworks, Research, Case studies, Tools

### Decision Criticality Framework (NEW)

**Include scenario if ≥1 criterion satisfied**:
- **Blocks Decision**: Directly impacts roadmap prioritization, go/no-go, or strategic pivot (revenue >$1M, market entry, product pivot)
- **Creates Risk**: Material competitive threat, churn signal (>5% monthly), or strategic misalignment
- **Affects ≥2 Stakeholders**: Multi-team impact (PM + Exec, PM + Eng, PM + Sales, etc.)
- **Actively Evolving**: Product/market/org dynamics changing in past 3–6 months
- **Quantified Impact**: Revenue $, pipeline $, adoption %, retention %, or market share

**Exclude scenario if**:
- Niche/legacy (<5% adoption)
- Orthogonal/nice-to-have (training only, no decision impact)
- Already covered in existing scenarios
- Speculative or hypothetical (no current market signal)

**Target**: 100% of scenarios satisfy ≥1 criterion

### Quality Gates (ANY fail = stop, fix, re-validate ALL)

| Gate | Pass Criteria | Mitigation |
|------|---------------|------------|
| **Decision Criticality** | 100% satisfy ≥1 criterion | Remove non-critical scenarios |
| **Recency** | ≥50% last 3yrs (≥70% AI/platform) | Flag outdated with caveats |
| **Diversity** | ≥3 source types; no type >25% | Expand research |
| **Per-Capability** | Each: ≥2 authoritative + ≥1 tool | Add missing sources |
| **Links** | 100% accessible/archived | Use Web Archive |
| **Cross-Refs** | 100% resolve; no orphans | Fix broken references |

## Execution

### Step 1: Plan Allocation

Distribute 6–8 decision-critical scenarios (25/50/25% B/I/A). Allocate per capability using the Quantitative Floors: Strategy & Prioritization (2–3), Metrics & Decision-Making (2–3), Stakeholder Alignment (1–2), (Optional) GTM (1). Ensure each capability has ≥1B or ≥1I; overall, ≥2A scenarios.

**Example** (8): Strategy & Prioritization (3): 1B/1I/1A | Metrics & Decision-Making (3): 0B/2I/1A | Stakeholder Alignment (2): 1B/1I/0A = **2B/4I/2A**

**Decision Criticality Check**: Verify each scenario satisfies ≥1 criterion (Blocks/Risk/Stakeholders/Evolving/Quantified)

### Step 2: Build References (BEFORE scenarios) — 60% reduction

| Type | Floor | Core Elements |
|------|-------|---------------|
| **Glossary** | ≥8 | RICE, JTBD, North Star, PMF, OKR, Continuous Discovery, Feature Factory, Churn<br>**Format**: G#. Term \| Definition \| Use cases \| Related \| Limitations |
| **Tools** | ≥3 | Analytics (Mixpanel or Amplitude), Roadmapping (ProductBoard), Research (UserTesting)<br>**Format**: T#. Tool \| Category \| Pricing \| Users \| Update (Q# YYYY) \| Integrations (≥3) \| URL |
| **Literature** | ≥4 (≥1 ZH) | EN: Cagan (*Inspired*), Torres (*Continuous Discovery*) \| ZH: 俞军<br>**Format**: L#. Author, Title, Year \| Summary \| Frameworks \| Relevance |
| **Citations** | ≥8 | APA 7th + [EN]/[ZH] \| ≥50% last 3yrs<br>**Format**: A#. APA + language tag |

**Run Gates 1–6 after completion**

### Step 3: Generate Scenarios (batch 2–3 → self-check)

**Format**: "When [role] faces [decision-blocking conflict], how does product enable decision?" | "Market signal: [quantified risk], how prioritize?"  
**Include**: Revenue impact (>$1M), stakeholder conflict (≥2 roles), strategic ambiguity, time pressure  
**Test**: ≥2 dimensions (Product/Business/Strategic/Operational)  
**Avoid**: Feature checks ("Has X?", "Supports Y?"), niche scenarios, training-only scenarios

**Decision-Critical Examples**:
- **B**: "Top 5 customers (40% revenue) request feature misaligned with mass-market vision. Prioritize?"
- **I**: "Churn 8% (target: 5%), roadmap full, sales wants 3 features. How prioritize?"
- **A**: "CEO allocates $5M for ONE bet: API platform, mobile app, or international. How enable decision?"

**Structure** (150–250 words):
1. **Decision Context**: 1-sentence decision-blocking conflict (revenue/strategic/risk)
2. **Framework** [Ref: G#/A#]: Cite relevant frameworks (RICE, JTBD, North Star)
3. **Multi-dimensional**: ≥2 of Product/Business/Strategic/Operational
4. **Workflow**: Step-by-step product support (3–4 steps)
5. **Trade-off analysis**: ≥2 options with pros/cons/risks
6. **Stakeholder impact**: ≥2 roles, their positions, deliverables
7. **Success metrics**: Quantified targets (revenue $, adoption %, retention %) + 6–12mo timeframe
8. **Limitations**: Assumptions and boundaries
9. **Decision Criticality** [NEW]: Which criterion satisfied (Blocks/Risk/Stakeholders/Evolving/Quantified)

**Self-Check** (per 2–3): ✓ Decision-critical \| ✓ ≥2 dimensions \| ✓ 150–250 words \| ✓ ≥1 cite \| ✓ Quantified impact \| ✓ Complexity matches depth

### Step 4: Create Visuals (≥1 diagram + ≥1 table per capability) — Compressed

| Capability | Diagram | Table |
|------------|---------|-------|
| **Strategy & Prioritization** | Roadmap (now/next/later) OR Value/Effort 2×2 | Decision matrix (≥2 options × ≥5 dimensions) |
| **Metrics & Decision-Making** | AARRR funnel OR cohort retention curve | Impact metrics (baseline, target, 6–12mo) |
| **Stakeholder Alignment** | Power/Interest 2×2 | Engagement plan (role, position, action) |
| **(Optional) GTM** | Growth loop | Channel strategy |

**Requirements**: Include units/timeframes; cite sources; ≥70% scenarios reference visuals; total ≥3 diagrams + ≥3 tables

### Step 5: Populate References

Use formats from Step 2. **Verify**: ✓ 100% [Ref: ID] resolve \| ✓ No orphans \| ✓ All fields complete \| ✓ [EN]/[ZH] tags

### Step 6: Run 12-Point Validation (Streamlined)

**Checklist** (ANY fail = stop, fix, re-run ALL):
1. **Floors**: G≥8, T≥3, L≥4, A≥8, UC=6–8, 25/50/25% (±5%)
2. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Stakeholders/Evolving/Quantified)
3. **Citations**: ≥70% ≥1 cite; ≥30% ≥2 cites
4. **Language**: EN 50–70%, ZH 20–40%, Other 5–15%
5. **Recency**: ≥50% from 3yrs (≥70% AI/platform)
6. **Diversity**: ≥3 types; no type >25%
7. **Links**: 100% accessible/archived
8. **Cross-Refs**: 100% resolve; no orphans
9. **Word Count**: Sample 3; 100% within 150–250
10. **Workflows**: 100% concrete (not feature checks); ≥2 dimensions
11. **Per-Capability**: 3/3 meet ≥2 authoritative + ≥1 tool
12. **Scenario Quality**: ≥70% enable decision-making (not yes/no)

### Step 7: Quality Review

**Criteria** (≥4/6 must pass):

| Criterion | Pass ✓ | Fail ✗ |
|-----------|--------|--------|
| **Clarity** | Single focused scenario | Multiple unrelated topics |
| **Capability** | Validates workflow depth | Checks feature existence |
| **Depth** | Enables trade-off demonstration | Binary yes/no answer |
| **Realism** | Enterprise-grade constraints | Unrealistic requirements |
| **Discriminative** | Tests capability depth | Common baseline feature |
| **Alignment** | Label matches content depth | Mismatch B/I/A designation |

**Pre-Submission**: ✓ 12 validations \| ✓ Floors met \| ✓ 6 gates cleared \| ✓ TOC links work \| ✓ No placeholders \| ✓ Sample 5 meet ≥4/6 criteria

**Pilot**: 2–3 users → 1 demo each → feedback → iterate

## Validation (Streamlined)

### Report (ANY fail = stop, fix, re-run ALL)

| # | Check | Measurement | Pass Criteria | Result | Status |
|---|-------|-------------|---------------|--------|--------|
| 1 | Floors | G:__ T:__ L:__ A:__ UC:__ (__B/__I/__A) | G≥8, T≥3, L≥4, A≥8, UC:6-8, 25/50/25% (±5%) | | PASS/FAIL |
| 2 | Decision Criticality | __/__ satisfy ≥1 criterion | 100% (Blocks/Risk/Stakeholders/Evolving/Quantified) | | PASS/FAIL |
| 3 | Citations | __%≥1, __%≥2 | ≥70% ≥1, ≥30% ≥2 | | PASS/FAIL |
| 4 | Language | EN:__%, ZH:__%, Other:__% | EN:50-70%, ZH:20-40%, Other:5-15% | | PASS/FAIL |
| 5 | Recency | __% from 3yrs | ≥50% (≥70% AI/platform) | | PASS/FAIL |
| 6 | Diversity | __ types; max __% | ≥3 types, no type >25% | | PASS/FAIL |
| 7 | Links | __/__ accessible | 100% | | PASS/FAIL |
| 8 | Cross-Refs | __/__ resolved | 100% | | PASS/FAIL |
| 9 | Word Count | __/3 compliant | 100% within 150-250 | | PASS/FAIL |
| 10 | Workflows | __/__ concrete | 100% concrete (not feature checks); ≥2 dimensions | | PASS/FAIL |
| 11 | Per-Capability | __/3 meet evidence | 3/3 (≥2 authoritative + ≥1 tool) | | PASS/FAIL |
| 12 | Quality | __% enable decision | ≥70% enable decision-making (not yes/no) | | PASS/FAIL |

### Quality Examples (≥2 fails = rewrite)

1. **Clarity**: ✓ "Activation vs. churn?" ✗ "Retention + database + API"
2. **Capability**: ✓ "CEO wants AI—support decision?" ✗ "Has AARRR dashboard?"
3. **Depth**: ✓ "Choose ONE: API/mobile/intl ($5M)" ✗ "Build mobile—yes/no?"
4. **Realism**: ✓ "Sales wants 3 features ($5M). Prioritize?" ✗ "Design Instagram in 45min"
5. **Discriminative**: ✓ "When does RICE mislead?" ✗ "Includes RICE calculator?"
6. **Alignment**: B (execution) \| I (strategy/trade-offs) \| A (portfolio/P&L/vision)

## Output Format (Streamlined)

### Document Structure

**TOC**: Context → Requirements → Execution (Steps 1-7) → Validation → Use Cases by Capability (8.1 Strategy & Prioritization | 8.2 Metrics & Decision-Making | 8.3 Stakeholder Alignment | 8.4 GTM optional) → References (9.1 Glossary | 9.2 Tools | 9.3 Literature | 9.4 Citations) → Validation Report

### Capability Overview (Decision-Critical)

**Total**: [6–8] | **Distribution**: [X]B ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%)

| # | Capability | Range | Count | Mix | Artifacts |
|---|------------|-------|-------|-----|-----------|
| 1 | Strategy & Prioritization | UC1–3 | 3 | 1B/1I/1A | 1 diagram+table |
| 2 | Metrics & Decision-Making | UC4–6 | 3 | 0B/2I/1A | 1 diagram+table |
| 3 | Stakeholder Alignment | UC7–8 | 2 | 1B/1I/0A | 1 diagram+table |
| | **Total** | | **8** | **2B/4I/2A** | **3+3** |

**Usage**: Select 1 capability (2–3 scenarios) → demonstrate 1–2 per session (5–10 min/scenario)

### Use Case Template (Decision-Critical)

---

**UC#: [Decision-blocking conflict: revenue/strategic/risk impact]**

**Complexity**: [B/I/A] | **Capability**: [Domain] | **Decision Criticality**: [Blocks/Risk/Stakeholders/Evolving/Quantified]

**Key Capability**: [1 sentence—decision-blocking conflict tested]

**Validation** (150–250 words):
1. **Decision Context**: [Quantified conflict: revenue >$1M, churn >5%, market risk]
2. **Framework**: Implements [Ref: G#/A#] via [application]
3. **Multi-dimensional**: ≥2 of Product/Business/Strategic/Operational
4. **Workflow**: "First, [action]. Second, [action]. Third, [action]." (3–4 steps)
5. **Trade-offs**: "Option A: [pros]/[cons]/[risks]. Option B: [pros]/[cons]/[risks]." (≥2 options)
6. **Stakeholder Impact**: ≥2 roles, positions, deliverables
7. **Success Metrics**: "[Metric] (baseline: [X], target: [Y] in 6–12mo)" (quantified)
8. **Limitations**: "Assumes [X]; may not apply if [Y]"

**Artifact**: [Type with structure] | **Decision Criticality Justification**: [Why this scenario is decision-critical]

---

### Reference Formats

| Type | Format |
|------|--------|
| **Glossary** | G#. **Term** (Acronym) \| Definition \| Use cases \| Related \| Limitations |
| **Tools** | T#. **Tool** (Category) \| Description \| Pricing \| Users \| Update (Q# YYYY) \| Integrations (≥3) \| URL |
| **Literature** | L#. Author. (Year). *Title*. Publisher. \| Summary \| Frameworks \| Relevance \| [Lang] |
| **Citations** | A#. [APA 7th]. [Lang] |

**APA 7th**:
- **Books**: `Author, A. (Year). *Title*. Publisher. [EN]`
- **Articles**: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI [EN]`
- **Web**: `Organization. (Year, Month Day). *Title*. Site. URL [EN]`
- **Chinese**: `俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH]`

## Example (Decision-Critical)

**UC1: Top 5 enterprise customers (40% revenue) request feature misaligned with mass-market vision. Prioritize?**

**Complexity**: Advanced | **Capability**: Strategy & Prioritization | **Decision Criticality**: [Blocks/Risk/Stakeholders/Evolving/Quantified]

**Key Capability**: Tests revenue protection vs. long-term PMF under stakeholder pressure; distinguishes strategic decision support from roadmap tools.

**Validation** (210 words):

**Decision Context**: Enterprise revenue $2M (40% total), churn risk if declined, mass-market vision at risk if customized. Blocks roadmap prioritization & strategic pivot.

**Framework**: RICE + JTBD + North Star [Ref: G2, G7, G4]. RICE quantifies reach/impact/confidence/effort. JTBD reveals underlying customer needs (may differ from feature request). North Star ensures alignment with long-term outcomes [Ref: A1, A6].

**Multi-dimensional Analysis**:
- **Product**: Custom feature vs. generalized solution
- **Business**: Revenue protection ($2M) vs. acquisition growth (5K+ users)
- **Strategic**: Feature factory risk vs. PMF strengthening
- **Operational**: Tech debt (custom) vs. velocity (reusable)

**Workflow**: (1) Conduct JTBD interviews with enterprise to uncover underlying problem. (2) Evaluate RICE: Enterprise (Reach:5/$2M, Impact:high, Confidence:high, Effort:unknown) vs. Mass-market (Reach:5K+, Impact:med/user, Confidence:med, Effort:similar). (3) Assess North Star impact: Does generalized solution strengthen or dilute vision?

**Trade-offs**: (A) Generalized feature: serves both segments, strengthens PMF, longer timeline, higher uncertainty. (B) Enterprise custom: protects $2M, risks fragmentation/debt, alienates mass-market. (C) Premium tier: monetizes customization, adds operational complexity. (D) Decline: maintains vision, risks churn/competition.

**Stakeholders**: CEO (revenue/strategy), VP Eng (velocity/debt), VP Sales (customer retention), PM (roadmap/vision).

**Success Metrics**: Enterprise retention (+20%), mass-market adoption (≥30% in 6mo), tech debt (≤10% velocity), support costs (flat/declining).

**Limitations**: Assumes enterprise needs generalizable; may not apply if truly custom.

**Decision Criticality Justification**: Blocks roadmap prioritization (revenue >$1M at risk), affects ≥2 stakeholders (CEO + VP Eng + VP Sales), creates strategic risk (PMF dilution), quantified impact ($2M retention vs. $500K acquisition).

**Artifact**:

| Criterion | Enterprise | Mass Market | Weight | E Score | M Score |
|-----------|------------|-------------|--------|---------|---------|
| Revenue (12mo) | $2M (retention) | $500K (acquisition) | 30% | 9 | 3 |
| Strategic alignment | Low (custom) | High (vision) | 25% | 2 | 9 |
| Reach | 5 customers | 5K+ users | 20% | 1 | 9 |
| Velocity impact | High (complex) | Low (reusable) | 15% | 2 | 8 |
| Competitive moat | Low (replicable) | High (differentiator) | 10% | 3 | 9 |
| **Weighted** | | | | **4.8** | **7.1** |

**Recommendation**: Generalized mass-market feature + enterprise premium services for edge cases (decision: prioritize mass-market, offer professional services to enterprise)
