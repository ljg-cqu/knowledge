# Operations & Supply Chain News Intelligence Q&A

Act as an operations & supply chain analyst. Generate 4–6 decision-critical Q&As from recent industry news for senior leaders. Use only this prompt and web search; fully self-contained.

**Cadence**: Monthly | 4–6h effort | Expires: 4 weeks from generation.

**Scope**: Decision-critical news (supply disruptions, supplier risk, cost shocks, regulatory/safety changes, capacity constraints) in mature organizations.

**Exclusions**: R&D, marketing, incremental improvements, rumors, stale news (>4mo HV, >6mo MV).

**Freshness**:
- **High-Velocity** (Disruptions, Logistics, Supplier Risk): ≥75% <1mo (≥25% 1–7d), ≥95% <2mo, 100% ≤4mo
- **Medium-Velocity** (Technology, Inventory/Demand): ≥65% <2mo (≥20% 1–14d), ≥90% <3mo, 100% ≤6mo
- **Long-Tail** (Safety/Regulatory, Resilience): ≥50% <6mo, ≥80% <12mo, 100% ≤18mo
- **Overall**: ≥70% <2mo, ≥90% <4mo, 100% ≤12mo

**Decision Criticality** (≥1 criterion):
1. Blocks decisions (sourcing, capacity, suppliers, resilience)
2. Creates risk (disruptions, incidents, breaches, >5% cost shocks)
3. Affects ≥2 core roles
4. Requires action (1-6mo window)
5. Quantified impact (lead time %, capacity %, cost/unit, etc.)

---

## Framework

**Stakeholders** (5 core): COO, VP Supply Chain, Plant Manager, Procurement Head, Quality Lead.

**Cycles** (4): Source (procurement, suppliers), Make (production, capacity), Deliver (logistics, lead times), Enable (safety, compliance).

**Categories** (4):
1. Supply Chain & Logistics Disruptions
2. Procurement & Supplier Risk
3. Manufacturing & Capacity
4. Quality, Safety & Compliance

**Relevance**: Meet freshness and ≥1 criticality criterion; prioritize quantified impacts affecting ≥2 roles.

---

## Requirements

**Q&A**: 4–6 total (1-2/cycle), 200–300 words each, news-driven, ≥1 cite (≥30% ≥2 cites), cover ≥1 category + impact + decision.

**Coverage**: Cycles (4, skip if no news), Categories (min: Logistics ≥50%, Supplier ≥40%, Mfg ≥25%, Safety ≥25%), Criticality (100% ≥1 criterion), Stakeholders (≥4/5).

**References**: Build before Q&A: G≥8 (terms used), N≥4-5, L≥2, M≥2, S≥2, R≥2, A≥6.

**Visuals**: ≥2 diagrams + ≥1 table.

**Gates** (fail any = stop):
1. Criticality: 100% ≥1 criterion
2. News: 100% cited, fresh; 0% marketing/rumors
3. Impact: 100% ≥2 cycles + ≥2 roles + quantified
4. Decision: 100% clear + rationale + timeline
5. Sources: ≥3 types, ≤50%/type, valid URLs
6. Actionability: 100% concrete

---

## Execution

### 1. Discovery & Curation
Record date (YYYY-MM-DD). Identify domain (e.g., "Global Automotive Supply Chain").

**Search** (≥10-15 candidates, tiered):
- Tier 1 (1-7d): Key terms + date range
- Tier 2 (7-30d): Same
- Tier 3 (1-6mo): Regulatory/safety

**Sources**: Prioritize Supply Chain Dive, Logistics Mgmt, IndustryWeek, Maersk, DHL, McKinsey, OSHA, EPA. Avoid marketing/rumors.

**Tools**: Perplexity, ChatGPT, Google.

**Curate**: ≥10-15 (Disrupt ≥4, Supplier ≥3, Mfg ≥2, Safety ≥2); check age, source, criticality, details, metrics (cross-check if needed, flag uncertainty).

**Verify/Allocate**: Ensure criticality; allocate 4-6 Qs across cycles/categories/roles.

### 2. Build References
**Format**: G# (term, def+analogy, context), N# (news, source, date, cat, URL), etc.

**Citation**: [Ref: N1][n1] in text, [n1]: URL at end.

**Floors**: As above.

**Glossary**: Terms used only; plain language, analogies, context, examples.

**News**: Title (Source, MM/DD): Summary | Cat | URL | Criterion.

### 2.5 Opportunistic Refresh (Optional)
If major disruption (24–72h, affects ≥3 Qs): Quick search, add 1-2 items, adjust Qs.

### 3. Generate Q&A
Review glossary; track terms.

**Patterns**: Decision-focused questions.

**Avoid**: Generic, hype, unattributed, stale, speculative.

**Structure** (200–300w):
1. ### Qn: Question
2. #### News: What/when/why/category; cite.
3. #### Impact: Consequences ≥2 cycles, quantified.
4. #### Stakeholders: ≥2 roles affected, concerns/actions.
5. #### Options & Decision: ≥2 options, benefits/costs/risks; recommend + timeline + limitations.
6. #### Actions & Measures: Immediate/short-term actions, owners, 1–3 metrics, monitoring.
7. #### References: Links.

**Self-Check**: Fresh, critical, ≥2 cycles/roles, clear decision, word count, quantified, cited, actionable, terms in glossary.

### 4. Visuals
≥2 diagrams (Mermaid) + ≥1 table; e.g., risk heatmap, decision tree, impact matrix.

**Checks**: Links valid, ages OK, floors met, decisions clear with rationale/timeline/roles/actions.

### 5. Review & Validate
**Quantitative**: Floors, glossary 100%, cycles/categories/roles covered, citations, word counts, visuals, ages.

**Qualitative**: Fresh/hype-free, criticality 100%, ≥2 cycles/roles/quantified, ≥3 source types, actionable/evidence-based, search documented.

**Checklist**: All pass; no placeholders; URLs valid; dates recorded.

---

## Validation Report

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | Freshness | HV: __%<1mo (1-7d:__%), __%<2mo; MV: __%<2mo (1-14d:__%); Overall: __%<2mo | Per rules | | PASS/FAIL |
| 2 | Floors | G:__ N:__ L:__ M:__ S:__ R:__ A:__ Q:__ | ≥8,4-5,2,2,2,2,6,4-6 | | PASS/FAIL |
| 3 | Glossary | __% terms; __% analogies | 100%; ≥50% | | PASS/FAIL |
| 4 | Cycles | __/4 (1-2Q); total __ | 4/4; 4-6 | | PASS/FAIL |
| 5 | Categories | Disrupt __% Supplier __% Mfg __% Safety __% | ≥50,40,25,25% | | PASS/FAIL |
| 6 | Roles | __/5 | ≥4 | | PASS/FAIL |
| 7 | Criticality | __% ≥1 criterion | 100% | | PASS/FAIL |
| 8 | Impact | __% ≥2 cycles+roles+quantified | 100% | | PASS/FAIL |
| 9 | Decision | __% decision+rationale+timeline | 100% | | PASS/FAIL |
| 10 | Citations | __% ≥1 cite | 100% | | PASS/FAIL |
| 11 | Words | __% 200-300w | 100% | | PASS/FAIL |
| 12 | Visuals | Diag __; Tab __ | ≥2; ≥1 | | PASS/FAIL |
| | Meta | Start: __ End: __ Expires: [+4wk] | | INFO |
| | Age Dist | <1mo __% (1-7d __%) 1-2mo __% 2-4mo __% | Per rules | | INFO |
| | OVERALL | All checks | All PASS | | PASS/FAIL |