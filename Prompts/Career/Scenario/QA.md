# PM Scenario Generator

**Purpose**: Generate 25–30 evidence-based PM scenarios to validate capabilities across 6 domains (Strategy, Discovery, Prioritization, Metrics, Stakeholder, GTM) at 3 complexity levels.

**Context**: For PM teams, training, executive alignment. Assumes PM framework knowledge (RICE, JTBD, OKR, AARRR).

**Constraints**: 150–300 words/scenario; ≥70% cited; realistic conflicts (priorities, resources, stakeholder pressure); 10–15min/scenario.

**Terms**: **B/I/A** = Basic (execution) / Intermediate (trade-offs) / Advanced (portfolio/P&L/vision) | **MECE** = Mutually Exclusive, Collectively Exhaustive | **RICE** = Reach, Impact, Confidence, Effort | **JTBD** = Jobs-To-Be-Done | **PMF** = Product-Market Fit | **North Star** = Key value metric

## Table of Contents
1. [Requirements](#requirements)
2. [Execution](#execution)
3. [Validation](#validation)
4. [Output Format](#output-format)
5. [Example](#example)

## Requirements

### Quantitative Floors

| Component | Requirements |
|-----------|--------------|
| **Scenarios** | 25–30 \| 20/40/40% B/I/A (±5%) \| 150–300 words \| ≥70% ≥1 cite, ≥30% ≥2 cites |
| **Capabilities** (MECE) | Strategy (5–6) \| Discovery (4–5) \| Prioritization (5–6) \| Metrics (4–5) \| Stakeholder (4–5) \| GTM (4–5) |
| **References** | Glossary ≥10 \| Tools ≥5 \| Literature ≥6 (≥2 Chinese) \| Citations ≥12 APA 7th + [EN]/[ZH] |
| **Visuals** | ≥1 diagram + ≥1 table per capability |
| **Scaling** | >30 scenarios: multiply floors by 1.5× |

**Outcomes**: Capability validation, maturity assessment (85%+ alignment, 30% faster planning), executive alignment (2 sessions vs. 6+ months).

**Scope**: Multi-stakeholder conflicts, resource limits, strategic ambiguity, data interpretation, trade-offs.  
**Excluded**: Feature checklists, greenfield design, implementation details.

**Limitations**: Generic scenarios lack domain context (customize for industry); framework misapplication risk (include limitations); depth over speed trade-off.

### Citations

**Format**: APA 7th + [EN]/[ZH] | **Inline**: `[Ref: ID]` where ID = G#(Glossary), T#(Tool), L#(Literature), A#(Citation)  
**Distribution**: EN 50–70%, ZH 20–40%, Other 5–15% | **Types** (≥3): Frameworks, Research, Case studies, Tools

### Quality Gates (ANY fail = stop, fix, re-validate ALL)

| Gate | Pass Criteria | Mitigation |
|------|---------------|------------|
| **Recency** | ≥50% last 3yrs (≥70% AI/platform) | Flag outdated with caveats |
| **Diversity** | ≥3 source types; no type >25% | Expand research |
| **Per-Capability** | Each: ≥2 authoritative + ≥1 tool | Add missing sources |
| **Tool Detail** | Pricing, users, update ≤18mo, ≥3 integrations | Update or replace |
| **Links** | 100% accessible/archived | Use Web Archive |
| **Cross-Refs** | 100% resolve; no orphans | Fix broken references |

## Execution

### Step 1: Plan Allocation

Distribute 25–30 scenarios (20/40/40% B/I/A). Each capability: 4–6 scenarios with ≥1B, ≥1I, ≥1A.

**Example** (30): Strategy (5): 1B/2I/2A | Discovery (5): 1B/2I/2A | Prioritization (6): 1B/2I/3A | Metrics (5): 1B/2I/2A | Stakeholder (4): 0B/2I/2A | GTM (5): 1B/2I/2A = **6B/12I/12A**

### Step 2: Build References (BEFORE scenarios)

| Type | Floor | Core Elements |
|------|-------|---------------|
| **Glossary** | ≥10 | RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST<br>**Format**: G#. Term \| Definition \| Use cases \| Related \| Limitations |
| **Tools** | ≥5 | Analytics (Mixpanel, Amplitude), Roadmapping (ProductBoard), Research (Dovetail), Collaboration (Miro), Feedback (Pendo)<br>**Format**: T#. Tool \| Category \| Pricing \| Users \| Update (Q# YYYY) \| Integrations (≥3) \| URL |
| **Literature** | ≥6 (≥2 ZH) | EN: Cagan (*Inspired*), Olsen (*Lean Product Playbook*), Torres (*Continuous Discovery*) \| ZH: 俞军, 梁宁, 苏杰<br>**Format**: L#. Author, Title, Year \| Summary \| Frameworks \| Relevance |
| **Citations** | ≥12 | APA 7th + [EN]/[ZH] \| ≥50% last 3yrs<br>**Format**: A#. APA + language tag |

**Run Gates 1–6 after completion**

### Step 3: Generate Scenarios (batch 5 → self-check)

**Format**: "How does product support...", "Product enables...", "When [role] needs X, product provides..."  
**Include**: Time constraints, resource limits, stakeholder pressure, conflicting data  
**Test**: ≥2 dimensions (Product/Business/Strategic/Operational)  
**Avoid**: Feature checks ("Has X?", "Supports Y?")

**Complexity Examples**:
- **B**: "How does product track activation metrics for new feature?"
- **I**: "Churn 8% (target: 5%) but roadmap full. How support retention vs. new features?"
- **A**: "CEO allocates $5M for ONE bet: API platform, mobile app, or international. How enable decision?"

**Structure** (150–300 words):
1. **Key Capability**: 1-sentence workflow/feature tested
2. **Framework** [Ref: G#/A#]: Cite relevant frameworks
3. **Multi-dimensional**: ≥2 of Product/Business/Strategic/Operational
4. **Concrete workflow**: Step-by-step product support
5. **Trade-off analysis**: Options with pros/cons/risks
6. **Stakeholder deliverables**: Role-specific outputs
7. **Success metrics**: Quantified targets + timeframes
8. **Limitations**: Assumptions and boundaries
9. **Artifact** (optional): Matrix, journey, dashboard, roadmap

**Self-Check** (per 5): ✓ Scenario-based \| ✓ ≥2 dimensions \| ✓ 150–300 words \| ✓ ≥3/5 ≥1 cite, ≥1/5 ≥2 cites \| ✓ Complexity matches depth

### Step 4: Create Visuals (≥1 diagram + ≥1 table per capability)

| Capability | Diagram | Table |
|------------|---------|-------|
| **Strategy** | Roadmap (now/next/later), competitive 2×2 | Decision matrix |
| **Discovery** | User journey, research synthesis | Interview guide |
| **Prioritization** | OST, Value/Effort 2×2 | RICE scorecard |
| **Metrics** | AARRR funnel, cohort retention | Dashboard mockup |
| **Stakeholder** | Power/Interest 2×2 | Engagement plan, RACI |
| **GTM** | Growth loop | Channel strategy, launch plan |

**Requirements**: Include units/timeframes; cite sources; ≥50% scenarios reference visuals

### Step 5: Populate References

Use formats from Step 2. **Verify**: ✓ 100% [Ref: ID] resolve \| ✓ No orphans \| ✓ All fields complete \| ✓ [EN]/[ZH] tags

### Step 6: Run 12-Point Validation

**Checklist** (ANY fail = stop, fix, re-run ALL):
1. **Floors**: G≥10, T≥5, L≥6, A≥12, UC=25–30, 20/40/40% (±5%)
2. **Citations**: ≥70% ≥1 cite; ≥30% ≥2 cites
3. **Language**: EN 50–70%, ZH 20–40%, Other 5–15%
4. **Recency**: ≥50% from 3yrs (≥70% AI/platform)
5. **Diversity**: ≥3 types; no type >25%
6. **Links**: 100% accessible/archived
7. **Cross-Refs**: 100% resolve; no orphans
8. **Word Count**: Sample 5; 100% within 150–300
9. **Key Capabilities**: 100% concrete workflows (not features)
10. **Per-Capability**: 6/6 meet ≥2 authoritative + ≥1 tool
11. **Frameworks**: ≥80% correctly cited with limitations
12. **Scenario Quality**: ≥70% enable demonstration (not yes/no)

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

## Validation

### Report (ANY fail = stop, fix, re-run ALL)

| # | Check | Measurement | Pass Criteria | Result | Status |
|---|-------|-------------|---------------|--------|--------|
| 1 | Floors | G:__ T:__ L:__ A:__ UC:__ (__B/__I/__A) | G≥10, T≥5, L≥6, A≥12, UC:25-30, 20/40/40% (±5%) | | PASS/FAIL |
| 2 | Citations | __%≥1, __%≥2 | ≥70% ≥1, ≥30% ≥2 | | PASS/FAIL |
| 3 | Language | EN:__%, ZH:__%, Other:__% | EN:50-70%, ZH:20-40%, Other:5-15% | | PASS/FAIL |
| 4 | Recency | __% from 3yrs | ≥50% (≥70% AI/platform) | | PASS/FAIL |
| 5 | Diversity | __ types; max __% | ≥3 types, no type >25% | | PASS/FAIL |
| 6 | Links | __/__ accessible | 100% | | PASS/FAIL |
| 7 | Cross-Refs | __/__ resolved | 100% | | PASS/FAIL |
| 8 | Word Count | __/5 compliant | 100% within 150-300 | | PASS/FAIL |
| 9 | Workflows | __/__ concrete | 100% concrete (not feature checks) | | PASS/FAIL |
| 10 | Per-Capability | __/6 meet evidence | 6/6 (≥2 authoritative + ≥1 tool) | | PASS/FAIL |
| 11 | Frameworks | __/__ correct+cited | ≥80% | | PASS/FAIL |
| 12 | Quality | __% enable demo | ≥70% scenario-based | | PASS/FAIL |

### Quality Examples (≥2 fails = rewrite)

1. **Clarity**: ✓ "Activation vs. churn?" ✗ "Retention + database + API"
2. **Capability**: ✓ "CEO wants AI—support decision?" ✗ "Has AARRR dashboard?"
3. **Depth**: ✓ "Choose ONE: API/mobile/intl ($5M)" ✗ "Build mobile—yes/no?"
4. **Realism**: ✓ "Sales wants 3 features ($5M). Prioritize?" ✗ "Design Instagram in 45min"
5. **Discriminative**: ✓ "When does RICE mislead?" ✗ "Includes RICE calculator?"
6. **Alignment**: B (execution) \| I (strategy/trade-offs) \| A (portfolio/P&L/vision)

## Output Format

### Document Structure

**TOC**: Context → Requirements → Execution (Steps 1-7) → Validation → Use Cases by Capability (8.1 Strategy | 8.2 Discovery | 8.3 Prioritization | 8.4 Metrics | 8.5 Stakeholder | 8.6 GTM) → References (9.1 Glossary | 9.2 Tools | 9.3 Literature | 9.4 Citations) → Validation Report

### Capability Overview

**Total**: [25–30] | **Distribution**: [X]B ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%)

| # | Capability | Range | Count | Mix | Artifacts |
|---|------------|-------|-------|-----|-----------|
| 1 | Strategy | UC1–5 | 5 | 1B/2I/2A | 1 diagram+table |
| 2 | Discovery | UC6–10 | 5 | 1B/2I/2A | 1 diagram+table |
| 3 | Prioritization | UC11–16 | 6 | 1B/2I/3A | 1 diagram+table |
| 4 | Metrics | UC17–21 | 5 | 1B/2I/2A | 1 diagram+table |
| 5 | Stakeholder | UC22–25 | 4 | 0B/2I/2A | 1 diagram+table |
| 6 | GTM | UC26–30 | 5 | 1B/2I/2A | 1 diagram+table |
| | **Total** | | **30** | **6B/12I/12A** | **6+6** |

**Usage**: Select 1–2 capabilities (5–10 scenarios) → demonstrate 3–4 per session

### Use Case Template

---

**UC#: [Scenario with constraints, competing priorities, stakeholder pressure]**

**Complexity**: [B/I/A] | **Capability**: [Domain]

**Key Capability**: [1 sentence—specific workflow tested]

**Validation** (150–300 words):
1. **Framework**: Implements [Ref: G#/A#] via [application]
2. **Multi-dimensional**: ≥2 of Product/Business/Strategic/Operational
3. **Workflow**: "First, [action]. Second, [action]. Third, [action]."
4. **Trade-offs**: "Option A: [pros]/[cons]/[risks]. Option B: [pros]/[cons]/[risks]."
5. **Alternatives**: "Could support [Z] if [constraint changes]"
6. **Deliverables**: "Generates [artifact] for [role] with [elements]"
7. **Success**: "[Metric] (baseline: [X], target: [Y] in [timeframe])"
8. **Limitations**: "Assumes [X]; may not apply if [Y]"

**Artifact** *(optional)*: [Type with structure]

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

## Example

**UC1: How does product support decision when top 5 enterprise customers (40% revenue) request feature misaligned with mass-market vision?**

**Complexity**: Advanced | **Capability**: Strategy

**Key Capability**: Tests revenue protection vs. long-term PMF; distinguishes strategic decision support from roadmap tools.

**Validation** (248 words):

Enables multi-dimensional evaluation [Ref: A1]. **First, facilitates JTBD discovery** [Ref: A7]—identifies problems customers solve. Surfaces that requests mask deeper needs, revealing generalized solutions [Ref: A6].

**Second, quantifies with RICE** [Ref: G2]. Enterprise: Reach (5/$2M), Impact (high retention/low acquisition), Confidence (high), Effort (unknown if custom). Mass-market: Reach (5K+ users), Impact (med/user, high cumulative), Confidence (med), Effort (similar). Recognizes RICE won't capture strategic value—provides decision matrix [Ref: T2].

**Third, assesses against North Star** [Ref: G4]. Evaluates whether this moves toward outcomes or becomes feature factory [Ref: G9]. Identifies if generalized ("custom fields" → "flexible schema"), both segments benefit and strengthen PMF [Ref: G5].

**Trade-off visualization**: Displays (1) Enterprise version: protects $2M but risks fragmentation/debt; (2) Generalized: serves both but longer timeline/higher uncertainty; (3) Decline: maintains vision but risks churn/competition; (4) Premium tier: monetizes customization but adds operational complexity.

**Alternative suggestions**: Recommends professional services, partner ecosystem, configuration tools [Ref: L3].

**Stakeholder features**: Generates presentation with analysis, recommendation, trade-offs, criteria, precedent implications—product principles matter [Ref: T2].

**Success criteria**: Tracks enterprise retention (+20%), mass-market adoption (≥30% in 6mo), tech debt (≤10% velocity impact), support costs (flat/declining).

**Limitations**: Assumes enterprise needs generalizable; may not apply if truly custom.

**Artifact**:

| Criterion | Enterprise | Mass Market | Weight | E Score | M Score |
|-----------|------------|-------------|--------|---------|---------|
| Revenue (12mo) | $2M (retention) | $500K (acquisition) | 30% | 9 | 3 |
| Strategic alignment | Low (custom) | High (vision) | 25% | 2 | 9 |
| Reach | 5 customers | 5K+ users | 20% | 1 | 9 |
| Velocity impact | High (complex) | Low (reusable) | 15% | 2 | 8 |
| Competitive moat | Low (replicable) | High (differentiator) | 10% | 3 | 9 |
| **Weighted** | | | | **4.8** | **7.1** |

**Recommendation**: Generalized mass-market feature + enterprise premium services for edge cases

**Confidence**: High (established frameworks; common PM scenario)
