# Finance Q&A Generator: Decision-Critical Scenarios (Minimal Viable)

Generate **6–12 decision-critical Q&A pairs** for informed financial decision-making with limited time.

**Cadence**: On-demand | **Effort**: 4–6h | **Validity**: Evergreen (refresh annually or when financial context changes)

**Scope**: Decision-critical finance scenarios only—capital allocation, risk management, valuation, financial planning. For finance leaders (5–15yrs experience) facing ambiguous, multi-variable decisions.

**Exclusions**: Academic theory, niche instruments (<5% adoption), vendor marketing, speculation.

---

## Scope & Constraints

**Purpose**: Test practical judgment on decisions that **block go/no-go, create material risk, or affect ≥2 stakeholders**  
**Output**: 6–12 Q&A (150–250w) | 3–4 MECE decision-critical domains (1–3 Q&A each) | Difficulty F:I:A = 25:50:25% (±5pp)  
**Sources**: English 60–70%, Chinese 20–30%, Other 5–10% | ≥50% published within 3yrs (≥70% for rates/markets topics) | Theory-to-practice ratio 20–40% / 60–80%  
**Assumptions**: Candidates know core frameworks; face ambiguous, multi-variable decisions requiring trade-off analysis + quantified impact

---

## Quality Standards

**Content requirements:**
- **Scenario-based**: ≥70% test judgment with multi-variable constraints, trade-offs, ambiguity
- **Evidence-based**: ≥80% frameworks cited with sources + limitations; verify against ≥2 authoritative sources
- **Citations**: ≥70% answers ≥1 [Ref: ID], ≥30% ≥2; all resolve correctly
- **Balanced**: ≥50% include trade-offs, alternatives, counterarguments, "when NOT to use"
- **Reasoning**: ≥60% include step-by-step logic chains with evidence
- **Insights**: Each Q&A has non-obvious, decision-useful, falsifiable, concrete insight
- **Uncertainty**: Flag conflicts/uncertainty with qualifiers; cite confidence levels

**Decision Criticality Framework** (NEW - MANDATORY)
- **Include if ≥1 criterion satisfied**:
  - **Blocks Decision**: Directly impacts capital allocation, M&A go/no-go, risk posture, or strategic pivot
  - **Creates Material Risk**: Quantified threat (>5% variance, regulatory breach, liquidity crisis, credit downgrade)
  - **Affects ≥2 Stakeholders**: CFO + Treasurer, Controller + Risk Officer, CEO + Board
  - **Requires Action**: 1–6mo action window (not speculative)
  - **Quantified Impact**: Revenue $, WACC bps, NPV $, risk metrics (VaR, Duration), or compliance deadline
- **Exclude if**: Niche/legacy (<5% adoption), Orthogonal/nice-to-have, Already covered, Speculative

**Reference requirements (collect BEFORE Q&A):**
- **G#≥8** (Glossary): CAPM, WACC, NPV, IRR, DCF, ROIC, VaR, Duration (only decision-critical terms)
- **T#≥4** (Tools): Excel/Python, Bloomberg, Refinitiv, Scenario modeling tool
- **L#≥5** (Literature): Damodaran, Graham, CFA Institute, Fabozzi, 1 Chinese reference
- **A#≥8** (Citations): APA 7th + DOI + [EN]/[ZH]/[Other] (60% reduction, all decision-critical)
- **Quality tiers**: Academic/Standards > Central Banks/Regulators > Rating Agencies > Asset Managers
- **Diversity**: ≥3 types, no source >25%, prefer DOIs, all accessible

**Artifacts:** ≥1 diagram + ≥1 table per domain (compressed)

---

## Finance Domains (Decision-Critical Only)

| Domain | Scope | Decision Criticality | Examples |
|--------|-------|---------------------|----------|
| **Capital Allocation & Valuation** | M&A, capex, divestment, cost of capital, project evaluation | Blocks M&A go/no-go, capex decisions, strategic pivot | WACC changes, NPV sensitivity, DCF assumptions, LBO models |
| **Risk Management & Hedging** | Risk measurement, mitigation, portfolio protection, liquidity | Creates material risk (>5% variance, credit downgrade, liquidity crisis) | VaR thresholds, rate/FX hedging, tail risk, stress testing |
| **Financial Planning & Variance** | Budgeting, forecasting, performance metrics, escalation triggers | Blocks budget/forecast decisions, triggers escalation | Forecast accuracy, variance >10%, cash flow stress, KPI targets |
| **Corporate Finance & Capital Structure** | Debt/equity decisions, refinancing, covenant compliance | Affects ≥2 stakeholders (CFO + Treasurer, CEO + Board) | Interest rate changes, debt covenants, refinancing windows, credit ratings |

---

## Core Terminology

**CAPM**: E(R) = Rf + β(Rm - Rf), expected return based on systematic risk  
**WACC**: (E/V)×Re + (D/V)×Rd×(1-Tc), weighted cost of capital  
**NPV**: ΣCFt/(1+r)^t - Initial Investment, value creation measure  
**IRR**: Discount rate where NPV=0  
**Sharpe Ratio**: (Rp - Rf)/σp, risk-adjusted return  
**Beta**: Cov(Ri,Rm)/Var(Rm), systematic risk measure  
**DCF**: Valuation via discounted cash flows  
**EBITDA**: Earnings Before Interest, Taxes, Depreciation, Amortization  
**FCF**: Operating Cash Flow - CapEx  
**Alpha**: Excess return vs. benchmark  
**VaR**: Value at Risk, potential loss at confidence level  
**Duration**: Bond price sensitivity to interest rates  
**Convexity**: Second-order duration effect  
**ROIC**: NOPAT / Invested Capital  
**EV/EBITDA**: Enterprise Value / EBITDA multiple

---

## Difficulty Levels

| Level | % | Complexity | Frameworks | Theory:Practice | Min Requirements |
|-------|---|------------|------------|-----------------|------------------|
| **F** | 25±5 | Single variable, clear constraints | 1–2 standard | 60:40 | 2-step logic, 1 framework, 1 limitation, 1 citation |
| **I** | 50±5 | 2–3 variables, ambiguous constraints | 2–3, compare trade-offs | 40:60 | 3-step logic, 2 frameworks, trade-offs, 2 limitations, 2+ citations |
| **A** | 25±5 | Multi-variate, conflicting constraints | 3+, critique/adapt | 20:80 | 4–5 step logic, 3+ frameworks, alternatives, roadmap, 3+ limitations, 3+ citations |

---

## Answer Structure (150–250w, streamlined)

1. **Context** (~25w): Restate scenario, decision point, challenge
2. **Analysis** (~40w): Root causes, frameworks [Ref: ID], assumptions, quantified impact
3. **Reasoning** (~50w): Step-by-step logic [Ref: ID], trade-offs, alternatives
4. **Recommendations** (~50w): Actionable steps, priorities, decision criteria [Ref: ID]
5. **Limitations** (~20w): Constraints, "when NOT to use", risks [Ref: ID]
6. **Key Insight**: Non-obvious, decision-useful, falsifiable, quantified

---

## Examples by Difficulty

### F (20%): Explain + Apply
**Q**: What is CAPM and when is it most appropriate?  
**A** (~150w): CAPM [Ref: G1] calculates expected return: E(R) = Rf + β(Rm - Rf), where Rf is risk-free rate, β is systematic risk, and Rm is market return [Ref: L1]. Use for: (1) Cost of equity estimation in WACC [Ref: G2], (2) Required returns for capital budgeting [Ref: L2], (3) Performance evaluation vs. risk-adjusted benchmark. **Limitations**: Assumes single-period, homogeneous expectations, perfect markets, mean-variance optimization [Ref: L3]. Fails in emerging markets (low correlation), private equity (illiquid), or when specific risk dominates. Beta unstable in small-cap, high-growth stocks [Ref: A5]. Multi-factor models (Fama-French) often superior [Ref: L4].

### I (40%): Diagnose + Apply Multiple
**Q**: Portfolio: 60% equity (β=1.2), 40% bonds (duration=7yrs). Fed signals +200bps hikes. Sharpe ratio 0.85. Adjust allocation?  
**A** (~180w): Rising rates impact both [Ref: G11, G12]: (1) Bonds: 7-yr duration → ~14% price decline for +200bps [Ref: L1]; (2) Equities: Higher discount rates compress valuations, β>1 amplifies volatility [Ref: G6]. Current Sharpe 0.85 is solid [Ref: G5] but vulnerable. **Approach**: Scenario analysis [Ref: T2] modeling: +100/+200/+300bps over 12-18mo. Rebalance to: (1) Reduce duration to 3-4yrs via short-term bonds/TIPS [Ref: L3]; (2) Lower equity to 50%, increase cash/alternatives to 10-15%; (3) Tilt equity to value/financials (benefit from rate hikes) [Ref: L5]; (4) Consider rate hedges (receiver swaps, bond puts) [Ref: G8]. **Limitations**: Timing risk—if Fed pivots, miss rally [Ref: A8]. Transaction costs 10-25bps [Ref: T4]. Alternatives illiquid. Need 3-6mo [Ref: L2].

### A (40%): Synthesize + Justify
**Q**: $500M AUM, tracking error 3.2% vs. benchmark, alpha -0.3% (3yr). CIO wants "more active management." Respond.  
**A** (~250w): Negative alpha + 3.2% tracking error signals "closet indexing" inefficiency [Ref: L4, A10]. High fees for index-like returns. Two paths: truly active (6-8% TE, target 2-3% alpha) or passive (0.2% TE, lower fees) [Ref: L3, A12]. Current position unsustainable [Ref: G10]. **Response**: "Data shows neither fish nor fowl. Need decisive choice: genuine active or embrace passive." **Analysis**: (1) Attribution analysis [Ref: T1] by sector/factor—where alpha leaks? (2) Holdings-based TE [Ref: T3]: are high-conviction bets sized appropriately? (3) Turnover: is portfolio rebalanced to maintain active weights? [Ref: L5] (4) Benchmark fit [Ref: A11]. **Recommendations**: 3-phase [Ref: L2]: (1) M1-3: Full attribution + manager review; identify skill vs. luck [Ref: T1, T3]; (2) M4-6: If skill exists, increase conviction (30-50 holdings, 6-8% TE, concentrated sectors) [Ref: L4]; if not, transition to factor/smart beta (fees 15-40bps) [Ref: L6]; (3) M7-12: Monitor Sharpe, Information Ratio quarterly [Ref: G5, A9]. **Alternative**: Multi-manager core-satellite (passive core 70%, active satellites 30%) balances cost-alpha [Ref: L7]. **When NOT**: Market regime shifts (volatility, liquidity) may temporarily hurt active [Ref: A10]. **Limitations**: Active requires 3-5yr to prove skill [Ref: L4, A12]. Transition costs 30-80bps [Ref: T4]. Governance/career risk if underperforms year 1-2. Factor models have 15-25% explanatory gaps [Ref: L3].

---

## Process (Minimal Viable, 4–6h)

1. **Reference Collection** (1–1.5h): Collect G#≥8, T#≥4, L#≥5, A#≥8 BEFORE Q&A; verify language mix, recency, diversity
2. **Topic Planning** (30min): Select 3–4 decision-critical domains | Allocate 1–3 Q&A each (6–12 total) | Assign F:I:A = 25:50:25 (±5pp)
3. **Q&A Generation** (2–2.5h): Scenario-based questions ("How would you...", "You observe..."), single ask, ≥70% test judgment | Follow answer structure | Cite [Ref: ID] | Include alternatives + "when NOT to use" | Quantify impact | Checkpoint per 3 Q&A
4. **Artifacts** (30–45min): Create ≥1 diagram + ≥1 table per domain (compressed)
5. **Validation** (30–45min): Run 12-check list—ALL PASS required; FAIL → fix → re-validate

---

## Validation Checklist (12 Streamlined Checks)

| # | Check | Criteria | Purpose |
|---|-------|----------|---------|
| 1 | **Decision Criticality** | 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified) | Core requirement |
| 2 | Ref counts | G≥8, T≥4, L≥5, A≥8 | Source sufficiency |
| 3 | Q&A counts | 6–12 total, 3–4 domains, F:I:A 25:50:25 (±5pp) | Scope compliance |
| 4 | Citations | ≥70% ≥1 [Ref], ≥30% ≥2 | Evidence-based |
| 5 | Language | EN 60–70%, ZH 20–30%, Other 5–10% | Diverse views |
| 6 | Recency | ≥50% <3yr (≥70% for rates/markets) | Current practices |
| 7 | Links | All functional/archived, prefer DOIs | Verifiable |
| 8 | Word count | Sample 5: all 150–250w | Consistency |
| 9 | Quantified Impact | All Q&As include metrics ($, %, bps, timeframe) | Decision-critical |
| 10 | Trade-offs | ≥50% include alternatives, "when NOT to use" | Balanced |
| 11 | Artifacts | Each domain: ≥1 diagram + ≥1 table | Visual support |
| 12 | Final Review | All checks pass, TOC working, no broken cites | Readiness |

**Final**: ✅ ALL PASS → deliver | ❌ List failures → fix → re-validate

---

## Common Pitfalls

**Questions**: ❌ Too broad → ✅ Specific scenario | ❌ Recall → ✅ Judgment | ❌ No constraints → ✅ Multi-variable | ❌ Entry-level → ✅ Leadership

**Answers**: ❌ No citations → ✅ All cited | ❌ Vague → ✅ Actionable ("Rebalance to 60/40, stress test ±200bps, 95% VaR") | ❌ No limitations → ✅ "When NOT" + risks | ❌ Single approach → ✅ 2+ alternatives | ❌ Theory-heavy → ✅ 60–80% practice | ❌ Obvious insight → ✅ Non-obvious, falsifiable

**Insights**: ✅ "Tests risk-return optimization; distinguishes asset allocators from return chasers" | ❌ "About investment strategy" (vague, obvious)

---

## Output Structure (Minimal Viable)

```markdown
# Finance Q&A - Decision-Critical Scenarios

## Contents
[TOC with links to: Overview | 3–4 Domains | References | Validation]

## Topic Overview
| Domain | Range | Count | F/I/A | Decision Criticality |
| **Capital Allocation & Valuation** | Q1–Q3 | 1–3 | 25/50/25 | Blocks M&A, capex, strategic pivot |
| **Risk Management & Hedging** | Q4–Q6 | 1–3 | 25/50/25 | Creates material risk (>5% variance) |
| **Financial Planning & Variance** | Q7–Q9 | 1–3 | 25/50/25 | Blocks budget/forecast decisions |
| **Corporate Finance & Capital Structure** | Q10–Q12 | 1–3 | 25/50/25 | Affects ≥2 stakeholders |

## Domain 1: [Name]
### Q#: [Scenario]
**Difficulty**: [F/I/A] | **Domain**: [Name] | **Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified]

**Answer** (150–250w):
**Context**: [Challenge, decision point]
**Analysis**: [Root causes, frameworks] [Ref: ID]
**Reasoning**: [Steps, trade-offs] [Ref: ID]
**Recommendations**: [Actions, decision criteria] [Ref: ID]
**Limitations**: [Constraints, when NOT, risks] [Ref: ID]
**Key Insight**: [Non-obvious, quantified, falsifiable]

**Artifact**:
```
[Diagram/table]
```

[Repeat for all domains]

## Reference Sections
### Glossary (≥8)
**G#. Term**: Definition. **Use**: Context.

### Tools (≥4)
**T#. Name**: Desc. **Pricing**: $X. **Users**: AUM/Users. **Update**: Q# YYYY. **URL**: [link]

### Literature (≥5)
**L#.** Author (Year). *Title*. Publisher. [Topics]

### Citations (≥8)
**A#.** Full APA 7th. DOI. [EN/ZH/Other]

## Validation Report
[12-row table: # | Check | Criteria | Status | Notes]
**Final**: ✅ ALL PASS or ❌ [failures]
```

---

## Usage Summary (Minimal Viable)

1. **Collect refs** (1–1.5h): G≥8, T≥4, L≥5, A≥8 BEFORE Q&A; verify language mix, recency
2. **Generate 6–12 Q&A** (2–2.5h): 3–4 decision-critical domains, F:I:A 25:50:25 | Quantify impact | Include trade-offs
3. **Create artifacts** (30–45min): ≥1 diagram + ≥1 table per domain
4. **Run 12-check validation** (30–45min): Decision Criticality (100%), Quantified Impact (100%), Citations, Trade-offs—ALL PASS required
5. **Use output structure**: TOC, Q&A with Decision Criticality field, references, validation

**Success Criteria**: 12 checks pass | 100% decision-critical | Questions test judgment on go/no-go decisions | Answers quantified + cited + trade-offs | Insights non-obvious, falsifiable | References authoritative, current, diverse

**Effort**: 4–6h total | **Validity**: Evergreen (refresh annually or when financial context changes)
