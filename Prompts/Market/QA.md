# Interview Q&A Generator: Marketing Leadership

Generate 25–30 scenario-based interview Q&A pairs testing judgment and decision-making for Senior Manager/Director/VP Marketing roles.

---

## Task Definition

**Target Roles**: Senior Marketing Manager, Director, VP Marketing  
**Output**: 25–30 Q&A pairs (150–300 words each) with citations, artifacts, and validation  
**Coverage**: 6 MECE marketing domains (4–6 Q&A per domain)  
**Difficulty**: 20% Foundational, 40% Intermediate, 40% Advanced (±5pp)  
**Languages**: EN 50–70%, ZH 20–40%, Other 5–15%  
**Recency**: ≥50% sources <3yr (≥70% for digital/social topics)

---

## Core Requirements

### Quality Standards
- **Scenario-based**: ≥70% test judgment (not recall); multi-variable with constraints
- **Citations**: ≥70% have ≥1 [Ref: ID], ≥30% have ≥2; all resolve correctly
- **Evidence-based**: ≥80% frameworks correct with citations + limitations
- **Balanced**: ≥50% acknowledge trade-offs; include alternatives and "when NOT to use"
- **Reasoning**: ≥60% include explicit logic chains
- **Insights**: Each Q&A has non-obvious, decision-useful, falsifiable insight

### References (Collect Before Q&A Generation)
- **G#≥10** (Glossary): STP, CAC, LTV, MQL, ABM, Attribution, Brand Equity, AIDA, 4Ps, Segmentation
- **T#≥5** (Tools): Name, pricing, users, integrations, last update ≤18mo, URL
- **L#≥6** (Literature): EN+ZH authoritative texts (Kotler, Ries & Trout, Godin)
- **A#≥12** (APA 7th): Author (Year). Title. Source. DOI [EN]/[ZH]/[Other]
- **Quality tiers**: Academic > Government > Consultancy > Vendor > Trade > Practitioner
- **Diversity**: ≥3 types, no source >25%, prefer DOIs, all links accessible

### Artifacts
Per cluster: ≥1 diagram + ≥1 table (journey maps, matrices, funnels, decision trees, comparisons)

## Marketing Domains (MECE)

| Domain | Scope |
|--------|-------|
| **Market Research & Analysis** | Market sizing, competitive intel, trend analysis, customer research |
| **Marketing Strategy & Planning** | GTM strategy, positioning, budget allocation, portfolio management |
| **Brand Positioning & Messaging** | Brand identity, value proposition, messaging, differentiation |
| **Customer Segmentation & Targeting** | Segmentation, personas, targeting criteria, prioritization |
| **Channels & Campaign Management** | Channel selection, campaign planning, content strategy, media buying |
| **Marketing Metrics & Analytics** | KPIs, attribution, ROI analysis, dashboards, experimentation |

---

## Terminology

**STP**: Segmentation, Targeting, Positioning  
**CAC**: Customer Acquisition Cost = (Sales + Marketing) / New Customers  
**LTV**: Lifetime Value = ARPU × Lifespan; Healthy: LTV:CAC ≥3:1  
**MQL/SQL**: Marketing/Sales Qualified Lead  
**ABM**: Account-Based Marketing  
**MTA**: Multi-Touch Attribution  
**MMM**: Marketing Mix Modeling  
**Brand Equity**: Value premium from brand awareness, associations, quality, loyalty

---

## Verification & Accuracy

**Cross-check**: Statistics/frameworks/claims against ≥2 independent authoritative sources  
**Tool specs**: Verify pricing, features, integrations, update dates from official docs  
**Uncertainty**: Flag with qualifiers ("likely", "emerging evidence"), cite confidence levels  
**Conflicts**: Present both perspectives with citations  
**Outdated**: State publication date, note if superseded

**Authoritative sources** meet ≥1: Peer-reviewed academic; 10+ years senior practitioner; framework originator; data-backed with disclosed methodology; industry standard (cited by multiple authoritative sources)

**Quality tiers** (highest→lowest): Academic/Industry Standards → Government Stats → Top Consultancies → Vendor Docs → Trade Publications → Practitioner Blogs

---

## Difficulty Levels

| Level | % | Complexity | Frameworks | Theory:Practice | Min Elements |
|-------|---|------------|------------|-----------------|--------------|
| **F** | 20% | Single variable, clear constraints | 1–2 standard | 60:40 | 2-step logic, 1 framework, 1 limitation |
| **I** | 40% | 2–3 variables, ambiguous constraints | 2–3, compare trade-offs | 40:60 | 3-step logic, 2 frameworks, trade-offs, 2 limitations |
| **A** | 40% | Multi-variate, conflicting constraints | 3+, critique/adapt | 20:80 | 4–5 step logic, 3+ frameworks, alternatives, roadmap, 3+ limitations |

---

## Answer Structure (Required for All Q&A)

1. **Context**: Restate scenario and challenge (1–2 sentences)
2. **Analysis**: Diagnose root causes with frameworks [Ref: ID]; state assumptions (2–3 sentences)
3. **Reasoning**: Step-by-step logic with evidence [Ref: ID] (3–4 sentences)
4. **Recommendations**: Actionable steps, priorities, trade-offs [Ref: ID] (3–4 sentences)
5. **Implementation** (I/A only): Sequence, timelines, resources (2–3 sentences)
6. **Metrics** (I/A only): Success measures, projected outcomes (1–2 sentences)
7. **Limitations**: Constraints, "when NOT to use", uncertainties (2–3 sentences)
8. **Key Insight**: Non-obvious, decision-useful, falsifiable insight (included with question)

---

## Examples by Difficulty

### Foundational (20%): Explain + Apply Basic Framework
**Q**: What is STP and when is it used?  
**A** (~150w): STP is a three-stage framework [Ref: G1] for market strategy: (1) Segmentation divides markets into distinct groups; (2) Targeting selects segments to serve; (3) Positioning defines brand perception vs. competitors [Ref: L1]. Use for market entry, product launches, rebranding in fragmented markets. **Limitations**: Assumes stable, identifiable segments—may fail in rapidly evolving or highly personalized markets [Ref: L4].

### Intermediate (40%): Diagnose + Apply Multiple Frameworks
**Q**: B2B SaaS has CAC $1,200, LTV $3,800 (LTV:CAC 3.2:1). Marketing wants mid-market expansion from SMB. Assess feasibility.  
**A** (~180w): Current LTV:CAC 3.2:1 is healthy [Ref: G5]. Mid-market expansion must maintain ≥3:1. Key variables: (1) CAC increases (longer cycles, senior buyers) [Ref: A11]; (2) LTV may increase (higher ARPU, lower churn) [Ref: G5]. **Approach**: Benchmark comparable SaaS [Ref: T3]; pilot 20 accounts for 3 months [Ref: L5]; model 12-month LTV. **Decision**: Proceed if pilot shows LTV:CAC ≥3:1, payback <18mo. **Limitations**: Mid-market requires different positioning [Ref: G1], sales infrastructure, product capabilities—CAC alone insufficient. Pilot may have selection bias.

### Advanced (40%): Synthesize + Justify Strategy
**Q**: $10M budget, brand awareness -8pts YoY, performance marketing ROAS +15% YoY. CEO wants "more performance." Respond and propose strategy.  
**A** (~280w): Performance is cannibalizing brand demand—classic "efficiency trap" [Ref: L4, A10]. Declining awareness shrinks consideration; performance captures existing demand but doesn't create it [Ref: L4]. ROAS gains reflect attribution bias (last-click over-credits bottom-funnel) [Ref: G6, A12]. **Response**: "Gains are unsustainable. We're harvesting brand equity faster than building it. Propose 60/40 brand/performance split [Ref: L4, A10]." **Strategy**: (1) Q1-Q2: Shift 20% to brand (video, sponsorships) [Ref: L3]; test brand lift [Ref: T1]; (2) Q3-Q4: Launch campaign targeting +5pts awareness; geo holdouts [Ref: A11]; (3) Year 2: Rebalance to 60/40. **Alternative**: 100% performance if low competition and prioritizing market share—risks commoditization. **When NOT**: Early-stage startups without brand equity [Ref: L5]. **Limitations**: Brand effects lag 6–18mo [Ref: L4]; ROAS dips short-term; requires CEO buy-in.

---

## Balanced Perspectives (Required)

Include multiple viewpoints: Brand vs. Performance | B2B vs. B2C | DTC vs. Marketplace | Global vs. Local  
Include in answers: Alternative frameworks, "when NOT to use", biases [Ref: ID], counterarguments

**Insight requirements**: Non-obvious, decision-useful, falsifiable, concrete  
✅ "Tests efficiency vs. effectiveness trade-offs; distinguishes strategists balancing short-term ROAS with long-term brand equity"  
❌ "About marketing strategy"

---

## Process

### 1. Topic Planning
Select 5–6 domains, allocate 4–6 Q&A per domain (total 25–30), assign difficulty F:I:A = 20:40:40 (±5pp)

### 2. Reference Collection (Before Q&A Generation)
Collect and verify: G#≥10, T#≥5, L#≥6, A#≥12  
Verify: Language mix, recency, diversity, ≥3 types, no source >25%, all links accessible

### 3. Q&A Generation
**Questions**: Scenario-based ("How would you...", "You observe X..."), single ask, test judgment (≥70%)  
**Answers** (150–300w): Follow Answer Structure—Context → Analysis [Ref: ID] → Reasoning [Ref: ID] → Recommendations [Ref: ID] → Implementation (I/A) → Metrics (I/A) → Limitations ("when NOT to use")  
**Checkpoint every 5 Q&A**: Word count, citations, insights, limitations, perspectives

### 4. Artifacts  
Per cluster: ≥1 diagram + ≥1 table (use markdown/ASCII art)

### 5. References
Format: G# (term, definition, usage), T# (name, pricing, users, integrations, update, URL), L# (author, title, topics), A# (APA 7th + [EN]/[ZH])

### 6. Validation
Run 17-step checklist. **MANDATORY: All PASS. FAIL → stop, fix, re-validate**

---

## Validation Checklist (All PASS Required)

| # | Check | Criteria |
|---|-------|----------|
| 1 | Counts | G≥10, T≥5, L≥6, A≥12 \| Q&A 25–30 \| Difficulty 20/40/40% (±5pp) |
| 2 | Citations | ≥70% answers ≥1, ≥30% answers ≥2 |
| 3 | Language | EN 50–70%, ZH 20–40%, Other 5–15% |
| 4 | Recency | ≥50% <3yr (≥70% digital/social) |
| 5 | Diversity | ≥3 types, no source >25% |
| 6 | Links | All accessible/archived (prefer DOIs) |
| 7 | Cross-refs | All [Ref: ID] resolve |
| 8 | Word count | Sample 5: all 150–300 |
| 9 | Key Insights | All concrete (opportunity/trade-off/conflict/challenge) |
| 10 | Per-cluster | ≥2 authoritative + ≥1 tool |
| 11 | Frameworks | ≥80% correct with citations + limitations |
| 12 | Judgment | ≥70% scenario-based (not recall) |
| 13 | Accuracy | Sample 5: factually correct, cross-validated |
| 14 | Balance | ≥50% acknowledge limitations/trade-offs |
| 15 | Reasoning | ≥60% include logical explanation |
| 16 | Artifacts | Each cluster: ≥1 diagram + ≥1 table |
| 17 | TOC | Present and links work |

---

## Common Pitfalls

**Question Issues**: Too broad (not specific scenario) | Recall-based (not judgment) | No constraints (unrealistic) | Single-variable (not complex) | Role misalignment

**Answer Issues**: No citations | Vague recommendations (not actionable) | Missing limitations/"when NOT to use" | No alternatives | Theory-heavy without application | No key insight

---

## Output Structure

```markdown
# Interview Q&A - Marketing Professional

## Contents
TOC linking to: Topic Overview | 6 Domain Sections | Reference Sections (Glossary, Tools, Literature, Citations) | Validation Report

## Topic Overview
Table showing: Domain | Question Range | Count | Difficulty Mix (F/I/A)

## Domain 1: [Name]

### Q#: [Scenario-based question]
**Difficulty**: [F/I/A] | **Domain**: [Name]  
**Key Insight**: [Non-obvious, decision-useful, falsifiable, concrete]

**Answer** (150–300 words):  
[Context → Analysis [Ref: ID] → Reasoning [Ref: ID] → Recommendations [Ref: ID] → Implementation (I/A) → Metrics (I/A) → Limitations]

**Artifact**: [Diagram/table using markdown/ASCII]

[Repeat for 4–6 Q&A per domain]

[Repeat for all 6 domains]

## Reference Sections

### Glossary (≥10)
**G#. Term**: Definition. **Use**: Context.

### Tools (≥5)
**T#. Name**: Description. Pricing: $X. Users: Nm+. Integrations: [List]. Update: Q# YYYY. URL: [link]

### Literature (≥6, EN+ZH)
**L#.** Author (Year). *Title*. Publisher. [Topics]

### Citations (≥12, APA 7th + language tags)
**A#.** Author (Year). Title. Source. DOI [EN]/[ZH]/[Other]

## Validation Report
17-row table with: # | Check | Criteria | Status | Notes  
**Final Status**: ✅ ALL PASS or ❌ [list failures]
```

## Complete Example

**Q**: How would you determine optimal channel mix when CAC increased 45% YoY and LTV:CAC dropped from 4.5:1 to 2.8:1?

**Difficulty**: Advanced | **Domain**: Metrics & Analytics, Channels & Campaigns  
**Key Insight**: Tests diagnosis of efficiency deterioration and rebalancing based on unit economics; distinguishes holistic optimizers balancing short-term performance with long-term brand building from vanity metric chasers optimizing narrow KPIs.

**Answer** (285 words):

**Context**: CAC increasing 45% with LTV:CAC dropping from 4.5:1 to 2.8:1 indicates unit economics deterioration—a critical threat to sustainable growth [Ref: G4, G5].

**Analysis**: Three likely root causes [Ref: A11]: (1) Declining lead quality (converting less-qualified leads with higher churn), (2) Channel saturation (diminishing returns as addressable audience shrinks), (3) Competitive pressure (competitors bidding up ad prices). Decompose CAC by channel and cohort using analytics platforms [Ref: T1, T2] to isolate cause.

**Reasoning**: Multi-touch attribution [Ref: G6] reveals true contribution vs. last-click, which over-credits bottom-funnel while undervaluing awareness touchpoints [Ref: A12, T1]. Calculate channel-specific LTV:CAC; healthy channels maintain ≥3:1 [Ref: L1, G5]. This distinguishes efficient from saturated channels [Ref: A10].

**Recommendations**: Three-phase rebalancing [Ref: L2]: (1) **Immediate** (Month 1): Pause/reduce spend on LTV:CAC <2:1 channels; reallocate to ≥3:1 channels. (2) **Medium-term** (Months 2–3): Test new channels (partnerships, community, referral, organic) [Ref: G9, L3]; pilot with 10% freed budget. (3) **Long-term** (Months 4–6): Improve conversion via CRO [Ref: T1]; increase LTV through retention/upsell [Ref: T2, T4]. Use MMM [Ref: G6] to simulate outcomes.

**Metrics**: Target CAC $200 (−23%), LTV:CAC 4.0:1 (+43%), payback <12mo.

**When NOT to use**: If CAC increase is strategic up-market expansion (higher ARPU justifies higher CAC), maintain mix but adjust LTV expectations.

**Limitations**: Attribution models have inherent biases—no model captures perfect causality [Ref: G6, A12]. External factors (seasonality, market shifts, competition) confound metrics. Rapid channel shifts risk brand momentum loss and undervalue long-term brand-building absent from short-term LTV [Ref: L4, A10].

**Artifact**:
```
Channel Mix Analysis & Rebalancing Dashboard

Current: CAC $180→$261 (+45%) | LTV $810→$730 (−10%) | LTV:CAC 4.5:1→2.8:1 (−38%)
Target:  CAC $200 | LTV $900 | LTV:CAC 4.0:1

┌─────────────┬─────┬─────┬────────┬──────────────┐
│ Channel     │ Mix │ CAC │LTV:CAC │ Action       │
├─────────────┼─────┼─────┼────────┼──────────────┤
│Paid Search  │ 35% │ $220│  3.3:1 │ Maintain     │
│Paid Social  │ 25% │ $340│  2.1:1 │ Reduce 40%   │
│Content/SEO  │ 15% │  $95│  7.7:1 │ Increase 50% │
│Events       │ 15% │ $420│  1.7:1 │ Pause        │
│Email        │  5% │  $60│ 12.2:1 │ Scale 3x     │
│Partnerships │  5% │ $140│  5.2:1 │ Test & Expand│
└─────────────┴─────┴─────┴────────┴──────────────┘

Plan: M1: Cut Paid Social 40%, Events 100% → Save $200K
      M1-2: +Content 50%, +Email 3x → Invest $100K
      M2-3: Test Partnerships/Community/Referral → Invest $100K
Outcome: CAC $200 (−23%), LTV:CAC 4.0:1 (+43%), Payback <12mo
```

---

## Usage Instructions

1. Collect all references (G#≥10, T#≥5, L#≥6, A#≥12) before generating Q&A
2. Generate 25–30 Q&A across 6 domains, 20:40:40 F:I:A difficulty
3. Include ≥1 diagram + ≥1 table per domain cluster
4. Run 17-step validation checklist—all must PASS before finalizing
5. Use structured output format with TOC, Q&A, references, validation report
